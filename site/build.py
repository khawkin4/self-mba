#!/usr/bin/env python3
"""
Static-site generator for the Compounding MBA.

Reads the latest raw pull (_ingest/raw/<date>/) and emits a browsable,
scrollable course site into site/dist/:
  - index.html            module grid (Core + Executive), corpus stats, search
  - <track>-<module>.html one page per module: videos w/ collapsible transcripts,
                          Reddit discussions, EDGAR financials
  - style.css

Stdlib only. No server needed — open site/dist/index.html in a browser.
Rebuild anytime after a new pull:  python3 site/build.py
"""
import glob, html, json, os, re
from datetime import date

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "self-mba")
INGEST = os.path.join(ROOT, "_ingest")
LESSONS = os.path.join(ROOT, "lessons")
DIST = os.path.join(ROOT, "site", "dist")

def load_lesson(track, mid):
    p = os.path.join(LESSONS, f"{track}-{mid}.html")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None

TITLES = {
    "01-accounting": "Accounting", "02-corporate-finance": "Corporate Finance & Valuation",
    "03-micro-strategy": "Microeconomics & Strategy", "04-competitive-strategy": "Competitive Strategy",
    "05-marketing-brand": "Marketing & Brand", "06-operations": "Operations & Supply Chain",
    "07-data-analytics": "Data, Analytics & Decisions", "08-negotiation": "Negotiation",
    "09-leadership-ob": "Leadership & Org Behavior", "10-entrepreneurship": "Entrepreneurship & Venture",
    "11-global-macro": "Global Strategy & Macro", "12-capstone": "Capstone",
    "E1-leading-at-scale": "Leading at Scale", "E2-capital-allocation": "Capital Allocation",
    "E3-mergers-acquisitions": "M&A & Restructuring", "E4-governance-board": "Governance & The Board",
    "E5-transformation": "Transformation at Scale", "E6-crisis-leadership": "Crisis Leadership",
    "E7-exec-presence-comms": "Executive Presence & Comms", "E8-stakeholder-ir": "Stakeholder & Investor Relations",
    "E9-geopolitics-macro": "Geopolitics & Macro", "E10-digital-ai": "Digital & AI Transformation",
    "E11-operating-system": "Personal Operating System", "E12-culture-strategy": "Culture as Strategy",
}

def esc(s):
    return html.escape(str(s if s is not None else ""))

def latest_raw():
    dirs = sorted(glob.glob(os.path.join(INGEST, "raw", "*")))
    dirs = [d for d in dirs if os.path.isdir(d) and re.search(r"\d{4}-\d{2}-\d{2}$", d)]
    if not dirs:
        raise SystemExit("No raw pulls found. Run _ingest/pull.py first.")
    return dirs[-1]

def fmt_int(v):
    try: return f"{int(float(v)):,}"
    except (ValueError, TypeError): return str(v or "")

def fmt_dur(v):
    try:
        s = int(float(v)); return f"{s//60}:{s%60:02d}"
    except (ValueError, TypeError): return ""

def code(track, mid):
    return mid.split("-")[0].upper() if track == "exec" else mid.split("-")[0]

def load_module(mdir):
    vids, reddit = [], []
    for f in sorted(glob.glob(os.path.join(mdir, "yt_*.json"))):
        try: vids += json.load(open(f))
        except Exception: pass
    for f in sorted(glob.glob(os.path.join(mdir, "reddit_*.json"))):
        try: reddit += json.load(open(f))
        except Exception: pass
    # de-dupe videos by id, keep highest signal
    seen = {}
    for v in vids:
        k = v.get("id")
        if k not in seen or int(v.get("signal", 0) or 0) > int(seen[k].get("signal", 0) or 0):
            seen[k] = v
    vids = sorted(seen.values(), key=lambda v: (int(v.get("signal", 0) or 0), len(v.get("transcript") or "")), reverse=True)
    reddit = [r for r in reddit if r.get("title")]
    reddit.sort(key=lambda r: (int(r.get("signal", 0) or 0), int(float(r.get("ups", 0) or 0))), reverse=True)
    edgar = []
    for f in sorted(glob.glob(os.path.join(mdir, "edgar_*.txt"))):
        edgar.append(open(f, encoding="utf-8").read())
    return vids, reddit, edgar

def sig_badge(s):
    s = int(s or 0)
    if s <= 0: return ""
    cls = "sig-hi" if s >= 2 else "sig"
    return f'<span class="{cls}">signal {s}</span>'

# ---------- page rendering ----------
HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0c100e">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..600&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}"></head><body>
<div class="grain" aria-hidden="true"></div><div class="atmos" aria-hidden="true"></div>"""

def render_video(v):
    tr = (v.get("transcript") or "").strip()
    meta = " · ".join(x for x in [esc(v.get("channel")), fmt_dur(v.get("duration")),
                                  (fmt_int(v.get("views")) + " views") if v.get("views") not in (None, "", "NA") else ""] if x)
    body = ""
    if tr:
        # paragraphize a flat transcript for readability
        paras = re.split(r"(?<=[.!?])\s+(?=[A-Z])", tr)
        chunks, buf = [], ""
        for p in paras:
            buf += p + " "
            if len(buf) > 600:
                chunks.append(buf.strip()); buf = ""
        if buf.strip(): chunks.append(buf.strip())
        inner = "".join(f"<p>{esc(c)}</p>" for c in chunks)
        words = len(tr) // 5
        body = f"""<details class="tr"><summary>Read transcript · ~{words:,} words · {words//150} min read</summary>
<div class="tr-body">{inner}</div></details>"""
    else:
        body = '<div class="no-tr">No transcript available — watch on YouTube.</div>'
    return f"""<article class="card vid">
<div class="card-head"><a class="ttl" href="{esc(v.get('url'))}" target="_blank" rel="noopener">{esc(v.get('title'))}</a> {sig_badge(v.get('signal'))}</div>
<div class="meta">{meta}</div>{body}</article>"""

def render_reddit(r):
    txt = (r.get("selftext") or "").strip()
    excerpt = (txt[:600] + "…") if len(txt) > 600 else txt
    return f"""<article class="card thread">
<div class="card-head"><a class="ttl" href="{esc(r.get('url'))}" target="_blank" rel="noopener">{esc(r.get('title'))}</a> {sig_badge(r.get('signal'))}</div>
<div class="meta">r/{esc(r.get('sub'))} · ▲ {fmt_int(r.get('ups'))} · 💬 {fmt_int(r.get('comments'))} · u/{esc(r.get('author'))}</div>
{('<p class="excerpt">'+esc(excerpt)+'</p>') if excerpt else ''}</article>"""

def render_edgar(blocks):
    out = []
    for b in blocks:
        lines = []
        for ln in b.splitlines():
            if ln.startswith("## "): lines.append(f"<h4>{esc(ln[3:])}</h4>")
            elif ln.startswith("# "): lines.append(f"<h3>{esc(ln[2:])}</h3>")
            else: lines.append(esc(ln))
        out.append('<div class="edgar">' + "\n".join(lines) + "</div>")
    return "".join(out)

def render_module(track, mid, vids, reddit, edgar, prevnext, lesson=None):
    c = code(track, mid)
    title = TITLES.get(mid, mid)
    toc = []
    if lesson: toc.append('<a href="#lesson">Lesson</a>')
    toc.append('<a href="#videos">Source: Lectures</a>')
    if reddit: toc.append('<a href="#discuss">Discussions</a>')
    if edgar: toc.append('<a href="#fin">Financials</a>')
    sections = []
    if lesson:
        sections.append(f'<section id="lesson" class="lesson">{lesson}</section>')
        sections.append('<div class="source-divider"><span>Source material — go deeper</span></div>')
    vids_html = "".join(render_video(v) for v in vids) or "<p class='empty'>No lectures pulled.</p>"
    sections.append(f'<section id="videos"><h2>Lectures <span class="count">{len(vids)}</span></h2>{vids_html}</section>')
    if reddit:
        sections.append(f'<section id="discuss"><h2>Practitioner Discussions <span class="count">{len(reddit)}</span></h2>{"".join(render_reddit(r) for r in reddit)}</section>')
    if edgar:
        sections.append(f'<section id="fin"><h2>Live Financials (SEC EDGAR) <span class="count">{len(edgar)}</span></h2>{render_edgar(edgar)}</section>')
    pn = ""
    if prevnext[0]: pn += f'<a class="pn" href="{prevnext[0][0]}">← {esc(prevnext[0][1])}</a>'
    if prevnext[1]: pn += f'<a class="pn next" href="{prevnext[1][0]}">{esc(prevnext[1][1])} →</a>'
    done_btn = (f'<button id="mark-done" data-mod="{track}-{mid}.html"><span class="cp-tick">✓</span> '
                f'<span class="cp-on">Module complete</span><span class="cp-off">Mark module complete</span></button>') if lesson else ""
    track_name = "Executive Track" if track == "exec" else "Core Curriculum"
    return HEAD.format(title=f"{c} · {title}", css="style.css") + f"""
{'<div id="progress"></div>' if lesson else ''}
<header class="mod-header {('exec' if track=='exec' else 'core')}">
<a href="index.html" class="home">← Index</a>
<div class="eyebrow"><span class="num">{esc(c)}</span> {track_name}</div>
<h1>{esc(title)}</h1>
<div class="hairline"></div></header>
<nav class="toc">{" ".join(toc)}</nav>"""+f"""
<main>{"".join(sections)}</main>
<div class="done-wrap">{done_btn}</div>
<div class="pn-wrap">{pn}</div>
<a href="#" class="top">↑ Top</a>
<script src="lesson.js"></script>
</body></html>"""

def render_index(modules, stats):
    def cards(track):
        out = []
        for mid, v, r, e in modules[track]:
            c = code(track, mid); title = TITLES.get(mid, mid)
            words = sum(len(x.get("transcript") or "") for x in v) // 5
            ready = load_lesson(track, mid)
            lesson_tag = '<span class="lesson-tag">Lesson ready</span>' if ready else '<span class="lesson-tag pending">Sources only</span>'
            metas = [f"{len(v)} lectures", f"{words:,} words"]
            if r: metas.append(f"{len(r)} threads")
            if e: metas.append(f"{len(e)} filings")
            out.append(f"""<a class="mcard {('exec' if track=='exec' else 'core')}{' ready' if ready else ''}" href="{track}-{mid}.html" data-mod="{track}-{mid}">
<div class="mcard-num">{esc(c)}</div>
<div class="mcard-body">
<div class="mcard-top">{lesson_tag}<span class="done-tick">✓ done</span></div>
<h3>{esc(title)}</h3>
<div class="mstats">{"".join(f'<span>{m}</span>' for m in metas)}</div></div>
<span class="mcard-arrow">→</span></a>""")
        return "".join(out)
    return HEAD.format(title="The Compounding MBA", css="style.css") + f"""
<header class="hero">
<div class="eyebrow">Self-directed · Master's level</div>
<h1>The Compounding <em>MBA</em></h1>
<p class="sub">A master's-level business education, distilled from elite sources into interactive, visual lessons — and grounded in primary data.</p>
<div class="ticker"><span><b>{stats['modules']}</b> modules</span><span><b>{stats['videos']}</b> lectures</span><span><b>{stats['words']:,}</b> words</span><span><b>{stats['threads']}</b> discussions</span><span><b>{stats['filings']}</b> filings</span></div>
<input id="q" placeholder="Search modules…" oninput="filt()">
</header>
<main>
<div class="track-head"><span class="th-label">Core Curriculum</span><span class="th-rule"></span><span class="th-count">12 modules</span></div>
<div class="grid">{cards('core')}</div>
<div class="track-head"><span class="th-label">Executive Track</span><span class="th-rule"></span><span class="th-count">12 modules</span></div>
<div class="grid">{cards('exec')}</div>
</main>
<footer>Generated from <code>~/self-mba/_ingest/raw/{stats['date']}</code> · rebuild with <code>python3 site/build.py</code></footer>
<script>
function filt(){{var q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('.mcard').forEach(function(c){{
c.style.display = c.textContent.toLowerCase().includes(q) ? '' : 'none';}});}}
</script>
<script src="index.js"></script>
</body></html>"""

CSS = """
:root{
--bg:#0c100e;--bg2:#0e1411;--surface:#141c18;--surface2:#1a241e;
--line:#273330;--line2:#36443f;
--ink:#f1ebda;--ink2:#d7d1c0;--dim:#8d978a;
--brass:#cba24f;--brass2:#e6cb86;--core:#84ad8a;--exec:#cf8a5f;
--wrong:#cf6a5a;
--serif:'Fraunces',Georgia,serif;--read:'Newsreader',Georgia,serif;--mono:'IBM Plex Mono',ui-monospace,monospace;
--wrap:880px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink2);font:18px/1.72 var(--read);-webkit-font-smoothing:antialiased;overflow-x:hidden}
::selection{background:var(--brass);color:#0c100e}
a{color:inherit}main{max-width:var(--wrap);margin:0 auto;padding:0 24px 100px;position:relative;z-index:2}
.grain{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.05;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.atmos{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(1200px 620px at 50% -8%,rgba(203,162,79,.13),transparent 58%),radial-gradient(900px 520px at 88% 12%,rgba(132,173,138,.07),transparent 55%)}
::-webkit-scrollbar{width:11px;height:11px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--line2);border-radius:8px;border:3px solid var(--bg)}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
/* ---------- HERO / INDEX ---------- */
.hero{max-width:var(--wrap);margin:0 auto;padding:clamp(70px,14vh,140px) 24px 40px;position:relative;z-index:2}
.eyebrow{font:500 .72rem/1 var(--mono);letter-spacing:.32em;text-transform:uppercase;color:var(--brass);animation:rise .7s .05s both}
.hero h1{font:300 clamp(3.4rem,11vw,7rem)/.92 var(--serif);color:var(--ink);letter-spacing:-.025em;margin:.28em 0 .12em;animation:rise .9s .12s both}
.hero h1 em{font-style:italic;font-weight:400;color:var(--brass2)}
.sub{font-size:1.24rem;line-height:1.55;color:var(--dim);max-width:34ch;margin:0 0 30px;animation:rise .8s .26s both}
.ticker{display:flex;flex-wrap:wrap;gap:0 26px;font:500 .78rem/2.4 var(--mono);letter-spacing:.04em;color:var(--dim);text-transform:uppercase;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:10px 0;margin-bottom:30px;animation:rise .8s .4s both}
.ticker b{color:var(--brass2);font-weight:600}
#q{width:100%;max-width:440px;padding:14px 4px;border:0;border-bottom:1px solid var(--line2);background:transparent;color:var(--ink);font:1.05rem var(--read);animation:rise .8s .5s both;transition:border-color .2s}
#q::placeholder{color:var(--dim);font-style:italic}#q:focus{outline:0;border-color:var(--brass)}
/* track header */
.track-head{display:flex;align-items:center;gap:18px;max-width:var(--wrap);margin:54px auto 22px;padding:0 24px}
.th-label{font:500 .82rem/1 var(--mono);letter-spacing:.24em;text-transform:uppercase;color:var(--ink);white-space:nowrap}
.th-rule{flex:1;height:1px;background:linear-gradient(90deg,var(--line2),transparent)}
.th-count{font:.78rem var(--mono);color:var(--dim);white-space:nowrap}
/* module cards */
.grid{max-width:var(--wrap);margin:0 auto;padding:0 24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:0;border-top:1px solid var(--line)}
.mcard{display:flex;align-items:stretch;gap:0;text-decoration:none;border-bottom:1px solid var(--line);border-right:1px solid var(--line);position:relative;overflow:hidden;animation:rise .6s both;transition:background .25s}
.mcard::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--brass);transform:scaleY(0);transform-origin:top;transition:transform .3s}
.mcard:hover{background:var(--surface)}.mcard:hover::before{transform:scaleY(1)}
.mcard.exec::before{background:var(--exec)}
.mcard-num{font:300 2.7rem/1 var(--serif);color:var(--line2);padding:22px 0 22px 24px;min-width:84px;transition:color .25s}
.mcard:hover .mcard-num{color:var(--brass)}.mcard.exec:hover .mcard-num{color:var(--exec)}
.mcard-body{flex:1;padding:22px 16px 22px 4px}
.mcard-top{display:flex;align-items:center;gap:10px;min-height:20px}
.mcard h3{font:400 1.4rem/1.2 var(--serif);color:var(--ink);margin:8px 0 12px;letter-spacing:-.01em}
.mstats{display:flex;flex-wrap:wrap;gap:0 14px;font:.72rem/1.6 var(--mono);color:var(--dim);text-transform:uppercase;letter-spacing:.04em}
.mcard-arrow{align-self:center;padding-right:22px;color:var(--brass);font-size:1.3rem;opacity:0;transform:translateX(-8px);transition:.25s}
.mcard:hover .mcard-arrow{opacity:1;transform:none}.mcard.exec .mcard-arrow{color:var(--exec)}
.lesson-tag{font:500 .64rem/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--core);border:1px solid color-mix(in srgb,var(--core) 40%,transparent);border-radius:30px;padding:4px 9px}
.exec .lesson-tag{color:var(--exec);border-color:color-mix(in srgb,var(--exec) 40%,transparent)}
.lesson-tag.pending{color:var(--dim);border-color:var(--line2)}
.done-tick{margin-left:auto;font:500 .64rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--core);opacity:0}
.mcard.completed .done-tick{opacity:1}.mcard.completed{background:color-mix(in srgb,var(--core) 7%,transparent)}
/* ---------- MODULE PAGE ---------- */
.mod-header{max-width:var(--wrap);margin:0 auto;padding:clamp(40px,8vh,80px) 24px 0;position:relative;z-index:2}
.home{font:500 .74rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);text-decoration:none;transition:color .2s}.home:hover{color:var(--brass)}
.mod-header .eyebrow{margin-top:26px;color:var(--dim)}.mod-header .eyebrow .num{color:var(--brass);font-weight:600}
.mod-header.exec .eyebrow .num{color:var(--exec)}
.mod-header h1{font:300 clamp(2.6rem,6vw,4.2rem)/1 var(--serif);color:var(--ink);letter-spacing:-.02em;margin:.18em 0 .5em}
.hairline{height:1px;background:linear-gradient(90deg,var(--brass),transparent 70%)}
.mod-header.exec .hairline{background:linear-gradient(90deg,var(--exec),transparent 70%)}
.toc{position:sticky;top:0;z-index:20;backdrop-filter:blur(12px);background:color-mix(in srgb,var(--bg) 82%,transparent);max-width:var(--wrap);margin:0 auto;padding:16px 24px;border-bottom:1px solid var(--line);display:flex;gap:24px;flex-wrap:wrap}
.toc a{font:500 .74rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);text-decoration:none;transition:color .2s}.toc a:hover{color:var(--brass)}
section{margin-top:56px}
section>h2{font:300 clamp(1.7rem,3.5vw,2.3rem) var(--serif);color:var(--ink);letter-spacing:-.01em;border-bottom:1px solid var(--line);padding-bottom:12px;display:flex;align-items:baseline;gap:12px}
.count{font:.72rem var(--mono);color:var(--dim);letter-spacing:.08em}
/* source cards */
.card{background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:20px;margin:14px 0;transition:border-color .2s}.card:hover{border-color:var(--line2)}
.card-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.ttl{font:500 1.18rem/1.35 var(--read);color:var(--ink);text-decoration:none}.ttl:hover{color:var(--brass2)}
.meta{font:.74rem/1.6 var(--mono);color:var(--dim);text-transform:uppercase;letter-spacing:.03em;margin-top:7px}
.sig,.sig-hi{font:.64rem var(--mono);letter-spacing:.08em;text-transform:uppercase;border-radius:30px;padding:3px 9px;color:var(--brass);border:1px solid color-mix(in srgb,var(--brass) 40%,transparent);white-space:nowrap}.sig-hi{color:var(--brass2);background:color-mix(in srgb,var(--brass) 14%,transparent)}
.tr{margin-top:14px}.tr summary{cursor:pointer;font:500 .74rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--brass);list-style:none}.tr summary::-webkit-details-marker{display:none}.tr summary::before{content:"▸ ";color:var(--brass)}.tr[open] summary::before{content:"▾ "}
.tr-body{margin-top:14px;font:1.12rem/1.85 var(--read);color:var(--ink2);border-left:2px solid var(--brass);padding-left:22px;max-height:580px;overflow:auto}
.tr-body p{margin:0 0 16px}.no-tr{margin-top:10px;color:var(--dim);font-style:italic;font-size:.92rem}
.excerpt{color:var(--ink2);font-size:1rem;margin:12px 0 0;opacity:.85}
.edgar{background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:20px;margin:14px 0;font:.84rem/1.6 var(--mono);color:var(--ink2);white-space:pre-wrap}
.edgar h3{font:600 1.1rem var(--mono);color:var(--ink);margin:0 0 6px}.edgar h4{font:.95rem var(--mono);color:var(--brass);margin:16px 0 4px}
.empty{color:var(--dim);font-style:italic}
.pn-wrap{max-width:var(--wrap);margin:50px auto;padding:0 24px;display:flex;justify-content:space-between;gap:14px;position:relative;z-index:2}
.pn{flex:1;background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:18px;text-decoration:none;color:var(--dim);font:500 .82rem var(--mono);letter-spacing:.04em;transition:.2s}
.pn.next{text-align:right}.pn:hover{border-color:var(--brass);color:var(--ink)}
.top{position:fixed;bottom:26px;right:26px;z-index:40;background:var(--brass);color:#0c100e;border-radius:50%;width:48px;height:48px;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:0 6px 22px rgba(0,0,0,.4);font-size:1.1rem}
footer{max-width:var(--wrap);margin:0 auto;padding:36px 24px;color:var(--dim);font:.78rem/1.8 var(--mono);text-align:center;border-top:1px solid var(--line);position:relative;z-index:2}
footer code{color:var(--ink2)}
/* ---------- LESSON TYPOGRAPHY ---------- */
.lesson{font-size:1.16rem;line-height:1.78}
.lesson h2{font:300 clamp(1.8rem,4vw,2.6rem) var(--serif);color:var(--ink);letter-spacing:-.015em;margin:52px 0 14px;padding-top:14px;border-top:1px solid var(--line)}
.lesson h3{font:500 1.15rem var(--read);color:var(--ink);margin:0 0 8px}
.lesson p{margin:0 0 18px}
.lead{font:300 1.5rem/1.5 var(--read);color:var(--ink);margin-bottom:8px!important}
.lead::first-letter{font:600 4.2rem/.8 var(--serif);float:left;color:var(--brass);padding:6px 12px 0 0}
.lesson em{font-style:italic;color:var(--brass2)}
.lesson b{color:var(--ink);font-weight:600}
.equation{font:400 clamp(1.6rem,5vw,2.4rem) var(--serif);text-align:center;background:var(--surface);border:1px solid var(--brass);border-radius:4px;padding:26px;margin:24px 0;color:var(--ink);letter-spacing:.01em}
figure.viz{margin:28px 0;background:var(--surface);border:1px solid var(--line);border-radius:4px;padding:26px}
figure.viz svg{width:100%;height:auto}
figure.viz figcaption{font:.92rem/1.5 var(--read);font-style:italic;color:var(--dim);margin-top:14px;text-align:center}
.vlabel{font:500 12px var(--mono);fill:var(--dim);text-transform:uppercase;letter-spacing:.04em}.vlabel-in{font:600 12px var(--mono);fill:var(--brass)}
.bar-txt{font:600 13px var(--mono);fill:#0c100e;text-anchor:middle}.bar-txt-sm{font:600 11px var(--mono);fill:#0c100e;text-anchor:middle}
.bar-asset{fill:#46564e}.bar-liab{fill:var(--exec)}.bar-eq{fill:var(--core)}
.bar-rev{fill:#46564e}.bar-gross{fill:var(--core)}.bar-net{fill:var(--brass)}
.bar-asset~.bar-txt,.bar-rev~.bar-txt{fill:var(--ink)}
.example{background:var(--surface);border-left:3px solid var(--core);border-radius:0 4px 4px 0;padding:18px 24px;margin:22px 0}
.example p{margin:10px 0}
.pitfall{background:color-mix(in srgb,var(--exec) 9%,transparent);border:1px solid color-mix(in srgb,var(--exec) 32%,transparent);border-radius:4px;padding:18px 24px;margin:22px 0}
.pitfall.subtle{background:var(--surface);border-color:var(--line)}.pitfall h3{color:var(--exec);margin-bottom:6px}.pitfall.subtle h3{color:var(--brass)}
.apply-box{background:linear-gradient(135deg,color-mix(in srgb,var(--brass) 14%,transparent),color-mix(in srgb,var(--core) 8%,transparent));border:1px solid var(--brass);border-radius:4px;padding:22px 26px;margin:32px 0}
.apply-box h3{color:var(--brass2);margin-bottom:6px}
.apply-box code,.lesson code,.lead code{background:var(--bg);border:1px solid var(--line);padding:2px 7px;border-radius:4px;font:.88rem var(--mono);color:var(--brass2)}
.source-divider{text-align:center;margin:60px 0 10px;border-top:1px solid var(--line)}
.source-divider span{position:relative;top:-11px;background:var(--bg);padding:0 18px;font:500 .74rem var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
/* ---------- INTERACTIVE COMPONENTS ---------- */
#progress{position:fixed;top:0;left:0;height:3px;width:0;background:linear-gradient(90deg,var(--brass),var(--core));z-index:50;transition:width .1s}
.tip{position:absolute;z-index:60;background:var(--surface2);border:1px solid var(--brass);color:var(--ink);font:.84rem/1.45 var(--read);padding:10px 14px;border-radius:6px;max-width:280px;pointer-events:none;opacity:0;transform:translate(-50%,-100%);transition:opacity .12s;box-shadow:0 10px 30px rgba(0,0,0,.5)}
.tip.show{opacity:1}
.hot{cursor:pointer;transition:opacity .15s}.hot:hover{opacity:.82}.hot.active{stroke:var(--ink);stroke-width:2}
.fc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(172px,1fr));gap:14px;margin:24px 0}
.fc{position:relative;display:block;background:none;border:0;padding:0;height:152px;cursor:pointer;font:inherit;text-align:left}
.fc-inner{display:block;position:relative;width:100%;height:100%}
.fc-f,.fc-b{position:absolute;inset:0;border:1px solid var(--line2);border-radius:6px;padding:16px;display:flex;flex-direction:column;justify-content:space-between;transition:opacity .35s,transform .35s}
.fc-f{background:linear-gradient(165deg,var(--surface2),var(--surface));box-shadow:inset 0 1px 0 color-mix(in srgb,var(--brass) 18%,transparent)}
.fc:hover .fc-f{border-color:var(--brass)}
.fc-f b{font:400 1.34rem var(--serif);color:var(--ink)}
.fc-f .hint{font:.6rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass);white-space:nowrap;opacity:.85}
.fc-b{background:linear-gradient(150deg,var(--core),#5f8a6c);color:#0c140f;font-size:.95rem;line-height:1.46;justify-content:center;opacity:0;transform:scale(.97);pointer-events:none}
.fc.flipped .fc-f{opacity:0;transform:scale(.97)}
.fc.flipped .fc-b{opacity:1;transform:none}
.reveal{border:1px solid var(--line);border-radius:5px;margin:12px 0;overflow:hidden;background:var(--surface);transition:border-color .2s}.reveal.open{border-color:var(--brass)}
.reveal-q{width:100%;text-align:left;background:none;border:0;padding:18px 20px;font:400 1.2rem var(--serif);color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:10px}
.reveal-q::after{content:"+";color:var(--brass);font:300 1.6rem var(--serif);flex:none}.reveal.open .reveal-q::after{content:"–"}
.reveal-a{max-height:0;overflow:hidden;transition:max-height .35s ease}.reveal-a p{padding:0 20px;margin:0 0 18px}.reveal.open .reveal-a{max-height:360px}
.quizq{background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:22px;margin:16px 0}
.quizq .q{font:500 1.12rem var(--read);color:var(--ink);margin:0 0 14px}
.opt{display:block;width:100%;text-align:left;background:var(--bg);border:1px solid var(--line2);border-radius:4px;padding:13px 16px;margin:8px 0;font:1rem var(--read);color:var(--ink2);cursor:pointer;transition:.15s}
.opt:hover{border-color:var(--brass);color:var(--ink)}.quizq.done .opt{cursor:default}
.opt.right{background:color-mix(in srgb,var(--core) 18%,transparent);border-color:var(--core);color:var(--ink)}.opt.right::after{content:" ✓";color:var(--core);font-weight:700}
.opt.wrong{background:color-mix(in srgb,var(--wrong) 16%,transparent);border-color:var(--wrong)}
.fb{display:none;margin:14px 0 0;padding:14px 16px;background:var(--bg);border-left:3px solid var(--brass);border-radius:0 4px 4px 0;font-size:.98rem}
.fb.show{display:block;animation:rise .4s both}
.srcq{margin:22px 0;padding:18px 22px;background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--exec);border-radius:0 4px 4px 0}
.srcq p{margin:0 0 10px;font:italic 1.18rem/1.55 var(--read);color:var(--ink)}
.srcq cite{font:.76rem var(--mono);letter-spacing:.03em;text-transform:uppercase;color:var(--dim);font-style:normal}
.srcq cite a{color:var(--exec);text-decoration:none}.srcq cite a:hover{color:var(--brass2)}
.src-list{background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:18px 24px;margin:22px 0}
.src-list h4{font:500 .8rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass);margin:0 0 10px}
.src-list ul{margin:0;padding-left:18px}.src-list li{margin:6px 0}.src-list a{color:var(--ink2);text-decoration:none}.src-list a:hover{color:var(--brass2)}
.done-wrap{max-width:var(--wrap);margin:40px auto 0;padding:0 24px;text-align:center;position:relative;z-index:2}
#mark-done{background:transparent;border:1px solid var(--line2);border-radius:40px;padding:14px 30px;font:500 .8rem var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--dim);cursor:pointer;transition:.2s}
#mark-done .cp-tick{opacity:.35}#mark-done .cp-on{display:none}
#mark-done:hover{border-color:var(--core);color:var(--ink)}
#mark-done.checked{background:var(--core);color:#0c140f;border-color:var(--core)}
#mark-done.checked .cp-tick{opacity:1}#mark-done.checked .cp-on{display:inline}#mark-done.checked .cp-off{display:none}
@media(max-width:640px){.grid{grid-template-columns:1fr}.mcard-num{font-size:2rem;min-width:64px;padding-left:18px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto}}
"""

LESSON_JS = r"""
(function(){
  var bar=document.getElementById('progress');
  if(bar){addEventListener('scroll',function(){
    var h=document.documentElement,sc=h.scrollTop,mx=h.scrollHeight-h.clientHeight;
    bar.style.width=(mx>0?100*sc/mx:0)+'%';},{passive:true});}
  // flip cards
  document.querySelectorAll('.fc').forEach(function(c){
    c.addEventListener('click',function(){c.classList.toggle('flipped');});});
  // click-to-reveal
  document.querySelectorAll('.reveal .reveal-q').forEach(function(q){
    q.addEventListener('click',function(){q.parentNode.classList.toggle('open');});});
  // MCQ quiz w/ instant feedback
  document.querySelectorAll('.quizq').forEach(function(q){
    var correct=+q.dataset.correct, opts=q.querySelectorAll('.opt');
    opts.forEach(function(b,i){b.addEventListener('click',function(){
      if(q.classList.contains('done'))return; q.classList.add('done');
      b.classList.add(i===correct?'right':'wrong');
      if(i!==correct)opts[correct].classList.add('right');
      var fb=q.querySelector('.fb'); if(fb)fb.classList.add('show');});});});
  // SVG / element hotspots -> floating tooltip
  var tip=document.createElement('div'); tip.className='tip'; document.body.appendChild(tip);
  function place(e){var t=e.touches?e.touches[0]:e; tip.style.left=t.clientX+'px';
    tip.style.top=(t.clientY+window.scrollY-12)+'px';}
  document.querySelectorAll('[data-tip]').forEach(function(el){
    el.classList.add('hot');
    function show(e){tip.textContent=el.dataset.tip; tip.classList.add('show'); place(e);}
    el.addEventListener('mouseenter',show); el.addEventListener('mousemove',place);
    el.addEventListener('mouseleave',function(){tip.classList.remove('show');});
    el.addEventListener('click',function(e){show(e);
      document.querySelectorAll('[data-tip].active').forEach(function(o){if(o!==el)o.classList.remove('active');});
      el.classList.toggle('active');});});
  document.addEventListener('click',function(e){
    if(!e.target.closest('[data-tip]'))tip.classList.remove('show');});
  // module completion (persisted; surfaced on index)
  var done=document.getElementById('mark-done');
  if(done){var key='mba-done-'+(done.dataset.mod||location.pathname.split('/').pop());
    if(localStorage.getItem(key)==='1')done.classList.add('checked');
    done.addEventListener('click',function(){done.classList.toggle('checked');
      localStorage.setItem(key,done.classList.contains('checked')?'1':'0');});}
})();
"""

INDEX_JS = r"""
(function(){document.querySelectorAll('.mcard[data-mod]').forEach(function(c){
  if(localStorage.getItem('mba-done-'+c.dataset.mod+'.html')==='1')c.classList.add('completed');});})();
"""

def main():
    raw = latest_raw()
    pull_date = os.path.basename(raw)
    manifest = json.load(open(os.path.join(INGEST, "manifest.json")))
    os.makedirs(DIST, exist_ok=True)
    open(os.path.join(DIST, "style.css"), "w").write(CSS)
    open(os.path.join(DIST, "lesson.js"), "w").write(LESSON_JS)
    open(os.path.join(DIST, "index.js"), "w").write(INDEX_JS)

    modules = {"core": [], "exec": []}
    order = []  # (track, mid, filename, title)
    for track in ("core", "exec"):
        for mid in manifest.get(track, {}):
            if mid.startswith("_"): continue
            mdir = os.path.join(raw, track, mid)
            v, r, e = load_module(mdir) if os.path.isdir(mdir) else ([], [], [])
            modules[track].append((mid, v, r, e))
            order.append((track, mid, f"{track}-{mid}.html", TITLES.get(mid, mid)))

    # module pages with prev/next
    flat = [(t, m, modules[t][i][1], modules[t][i][2], modules[t][i][3])
            for t in ("core", "exec") for i, (m, *_ ) in enumerate(modules[t])]
    for idx, (track, mid, v, r, e) in enumerate(flat):
        prev = (order[idx-1][2], f"{code(*order[idx-1][:2])} {order[idx-1][3]}") if idx > 0 else None
        nxt = (order[idx+1][2], f"{code(*order[idx+1][:2])} {order[idx+1][3]}") if idx < len(flat)-1 else None
        page = render_module(track, mid, v, r, e, (prev, nxt), lesson=load_lesson(track, mid))
        open(os.path.join(DIST, f"{track}-{mid}.html"), "w", encoding="utf-8").write(page)

    stats = {
        "date": pull_date, "modules": len(flat),
        "videos": sum(len(v) for _,_,v,_,_ in flat),
        "words": sum(len(x.get("transcript") or "") for _,_,v,_,_ in flat for x in v) // 5,
        "threads": sum(len(r) for _,_,_,r,_ in flat),
        "filings": sum(len(e) for _,_,_,_,e in flat),
    }
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(render_index(modules, stats))
    print(f"Built site -> {DIST}")
    print(f"  {stats['modules']} module pages · {stats['videos']} lectures · {stats['words']:,} words · {stats['threads']} threads")
    print(f"  open: {os.path.join(DIST, 'index.html')}")

if __name__ == "__main__":
    main()
