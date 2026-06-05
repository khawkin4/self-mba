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
<title>{title}</title><link rel="stylesheet" href="{css}"></head><body>"""

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
    return HEAD.format(title=f"{c} · {title}", css="style.css") + f"""
{'<div id="progress"></div>' if lesson else ''}
<header class="mod-header"><a href="index.html" class="home">← All modules</a>
<div class="badge {('exec' if track=='exec' else 'core')}">{esc(c)}</div>
<h1>{esc(title)}</h1></header>
<nav class="toc">{" ".join(toc)}</nav>
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
            lesson_tag = '<span class="lesson-tag">✦ Lesson ready</span>' if load_lesson(track, mid) else '<span class="lesson-tag pending">Sources only</span>'
            out.append(f"""<a class="mcard" href="{track}-{mid}.html" data-mod="{track}-{mid}">
<div class="mcard-top"><span class="badge {('exec' if track=='exec' else 'core')}">{esc(c)}</span>{lesson_tag}<span class="done-tick">✓</span></div>
<h3>{esc(title)}</h3>
<div class="mstats"><span>{len(v)} lectures</span><span>{words:,} words</span>{f'<span>{len(r)} threads</span>' if r else ''}{f'<span>{len(e)} filings</span>' if e else ''}</div></a>""")
        return "".join(out)
    return HEAD.format(title="The Compounding MBA", css="style.css") + f"""
<header class="hero">
<h1>The Compounding MBA</h1>
<p class="sub">A self-directed, master's-level business education — assembled from elite sources and made browsable.</p>
<div class="corpus"><b>{stats['modules']}</b> modules · <b>{stats['videos']}</b> lectures · <b>{stats['words']:,}</b> words · <b>{stats['threads']}</b> discussions · <b>{stats['filings']}</b> filings <span class="dim">· pulled {stats['date']}</span></div>
<input id="q" placeholder="Filter modules…" oninput="filt()">
</header>
<main>
<h2 class="track-h">Core Curriculum</h2>
<div class="grid">{cards('core')}</div>
<h2 class="track-h">Executive Track</h2>
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
:root{--bg:#faf8f4;--card:#fff;--ink:#1c1a17;--dim:#6b6356;--line:#e7e1d6;--core:#2f6f4f;--exec:#7a3b8f;--accent:#b45309;--sig:#fef3c7;--sighi:#fde68a}
@media(prefers-color-scheme:dark){:root{--bg:#16140f;--card:#211e18;--ink:#ece7dd;--dim:#9b9384;--line:#332e25;--sig:#3a330f;--sighi:#4d4310}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
a{color:inherit}main{max-width:820px;margin:0 auto;padding:0 20px 80px}
/* hero / index */
.hero{max-width:820px;margin:0 auto;padding:64px 20px 28px;text-align:center}
.hero h1{font-size:2.6rem;margin:0 0 8px;letter-spacing:-.02em}
.sub{color:var(--dim);font-size:1.1rem;margin:0 auto 20px;max-width:600px}
.corpus{font-size:.92rem;color:var(--dim);margin-bottom:22px}.corpus b{color:var(--ink)}.dim{opacity:.7}
#q{width:100%;max-width:420px;padding:12px 16px;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--ink);font-size:1rem}
.track-h{max-width:820px;margin:36px auto 14px;padding:0 20px;font-size:1.15rem;letter-spacing:.04em;text-transform:uppercase;color:var(--dim)}
.grid{max-width:820px;margin:0 auto;padding:0 20px;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px}
.mcard{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;text-decoration:none;transition:.15s}
.mcard:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.08);border-color:var(--accent)}
.mcard h3{margin:10px 0 12px;font-size:1.12rem;line-height:1.3}
.mstats{display:flex;flex-wrap:wrap;gap:6px}.mstats span{font-size:.74rem;color:var(--dim);background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:2px 7px}
.badge{display:inline-block;font-weight:700;font-size:.78rem;color:#fff;border-radius:6px;padding:3px 9px}
.badge.core{background:var(--core)}.badge.exec{background:var(--exec)}
/* module page */
.mod-header{max-width:820px;margin:0 auto;padding:40px 20px 10px}
.home{color:var(--dim);text-decoration:none;font-size:.9rem}
.mod-header h1{font-size:2.1rem;margin:12px 0 0;letter-spacing:-.02em}
.toc{position:sticky;top:0;z-index:5;background:var(--bg);max-width:820px;margin:0 auto;padding:12px 20px;border-bottom:1px solid var(--line);display:flex;gap:18px}
.toc a{color:var(--dim);text-decoration:none;font-size:.9rem;font-weight:600}.toc a:hover{color:var(--accent)}
section{margin-top:38px}section h2{font-size:1.4rem;border-bottom:2px solid var(--line);padding-bottom:8px}
.count{font-size:.8rem;color:var(--dim);font-weight:400;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:1px 10px;margin-left:6px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:14px 0}
.card-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.ttl{font-weight:600;font-size:1.08rem;text-decoration:none;line-height:1.35}.ttl:hover{color:var(--accent);text-decoration:underline}
.meta{color:var(--dim);font-size:.85rem;margin-top:5px}
.sig,.sig-hi{font-size:.7rem;border-radius:5px;padding:2px 7px;color:#7a5a00;background:var(--sig);white-space:nowrap}.sig-hi{background:var(--sighi);font-weight:600}
.tr{margin-top:12px}.tr summary{cursor:pointer;color:var(--accent);font-weight:600;font-size:.9rem}
.tr-body{margin-top:12px;font-family:Georgia,"Times New Roman",serif;font-size:1.05rem;line-height:1.75;border-left:3px solid var(--line);padding-left:18px;max-height:560px;overflow:auto}
.tr-body p{margin:0 0 14px}.no-tr{margin-top:10px;color:var(--dim);font-size:.88rem;font-style:italic}
.excerpt{color:var(--dim);font-size:.92rem;margin:10px 0 0}
.edgar{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:14px 0;font-family:ui-monospace,Menlo,monospace;font-size:.85rem;white-space:pre-wrap;line-height:1.55}
.edgar h3{font-family:inherit;font-size:1.1rem;margin:0 0 6px;font-weight:700}.edgar h4{margin:14px 0 4px;color:var(--accent);font-size:.95rem}
.empty{color:var(--dim)}
.pn-wrap{max-width:820px;margin:40px auto;padding:0 20px;display:flex;justify-content:space-between;gap:12px}
.pn{flex:1;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;text-decoration:none;color:var(--dim);font-weight:600}
.pn.next{text-align:right}.pn:hover{border-color:var(--accent);color:var(--ink)}
.top{position:fixed;bottom:22px;right:22px;background:var(--accent);color:#fff;border-radius:50%;width:46px;height:46px;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.2)}
footer{max-width:820px;margin:0 auto;padding:30px 20px;color:var(--dim);font-size:.82rem;text-align:center;border-top:1px solid var(--line)}
footer code,.dim code{background:var(--card);padding:1px 5px;border-radius:4px}
.lesson-tag{font-size:.66rem;font-weight:700;color:var(--core);background:rgba(47,111,79,.12);border-radius:20px;padding:2px 8px}
.lesson-tag.pending{color:var(--dim);background:var(--bg);border:1px solid var(--line);font-weight:500}
/* ---------- LESSON typography ---------- */
.lesson{font-size:1.06rem;line-height:1.72}
.lesson h2{font-size:1.5rem;margin-top:36px;border:0;padding:0;letter-spacing:-.01em}
.lesson h3{font-size:1.1rem;margin:0 0 8px}
.lesson .lead{font-size:1.2rem;line-height:1.6;color:var(--ink)}
.lesson em{font-style:italic;color:var(--accent)}
.big-idea{background:linear-gradient(135deg,rgba(47,111,79,.1),rgba(180,83,9,.08));border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:22px 0}
.big-idea h3{color:var(--core)}.big-idea ul{margin:8px 0 0;padding-left:20px}.big-idea li{margin:6px 0}
dl.terms{margin:18px 0}dl.terms dt{font-weight:700;font-size:1.05rem;margin-top:16px}
dl.terms dt .aka{font-weight:400;font-size:.85rem;color:var(--dim);font-style:italic}
dl.terms dd{margin:4px 0 0;padding-left:0;color:var(--ink)}
.equation{font-family:Georgia,serif;font-size:1.5rem;text-align:center;background:var(--card);border:2px solid var(--accent);border-radius:12px;padding:18px;margin:20px 0;letter-spacing:.02em}
figure.viz{margin:24px 0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}
figure.viz svg{width:100%;height:auto}
figure.viz figcaption{font-size:.88rem;color:var(--dim);margin-top:12px;text-align:center}
.vlabel{font:600 12px sans-serif;fill:var(--dim)}.vlabel-in{font:600 12px sans-serif;fill:var(--accent)}
.bar-txt{font:700 14px sans-serif;fill:#fff;text-anchor:middle}.bar-txt-sm{font:700 11px sans-serif;fill:#fff;text-anchor:middle}
.bar-asset{fill:#475569}.bar-liab{fill:#b45309}.bar-eq{fill:#2f6f4f}
.bar-rev{fill:#475569}.bar-gross{fill:#2f6f4f}.bar-net{fill:#b45309}
.example{background:var(--card);border-left:4px solid var(--core);border-radius:0 12px 12px 0;padding:16px 22px;margin:20px 0}
.example p{margin:8px 0}
.pitfall{background:rgba(180,83,9,.08);border:1px solid rgba(180,83,9,.3);border-radius:14px;padding:16px 22px;margin:20px 0}
.pitfall.subtle{background:var(--card);border-color:var(--line)}.pitfall h3{margin-bottom:6px}
.quiz details{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:10px 0}
.quiz summary{cursor:pointer;font-weight:600}.quiz details[open] summary{margin-bottom:8px;color:var(--accent)}
.apply-box{background:linear-gradient(135deg,rgba(180,83,9,.12),rgba(47,111,79,.08));border:1px solid var(--accent);border-radius:14px;padding:18px 24px;margin:28px 0}
.apply-box h3{margin-bottom:6px}.apply-box code{background:var(--bg);padding:2px 6px;border-radius:5px;font-size:.9rem}
.source-divider{text-align:center;margin:44px 0 8px;border-top:1px solid var(--line)}
.source-divider span{position:relative;top:-12px;background:var(--bg);padding:0 16px;color:var(--dim);font-size:.85rem;text-transform:uppercase;letter-spacing:.08em}
/* ---------- INTERACTIVE COMPONENTS ---------- */
#progress{position:fixed;top:0;left:0;height:4px;width:0;background:linear-gradient(90deg,var(--core),var(--accent));z-index:50;transition:width .1s}
.tip{position:absolute;z-index:60;background:#1c1a17;color:#fff;font-size:.82rem;padding:8px 12px;border-radius:8px;max-width:260px;pointer-events:none;opacity:0;transform:translate(-50%,-100%);transition:opacity .12s;box-shadow:0 6px 20px rgba(0,0,0,.3)}
.tip.show{opacity:1}
.hot{cursor:pointer;transition:opacity .15s}.hot:hover{opacity:.85}.hot.active{stroke:var(--ink);stroke-width:2}
/* flip cards */
.fc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin:20px 0}
.fc{perspective:900px;background:none;border:0;padding:0;height:120px;cursor:pointer;font:inherit;text-align:left}
.fc-inner{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.fc.flipped .fc-inner{transform:rotateY(180deg)}
.fc-f,.fc-b{position:absolute;inset:0;backface-visibility:hidden;border:1px solid var(--line);border-radius:12px;padding:14px;display:flex;flex-direction:column;justify-content:center}
.fc-f{background:var(--card)}.fc-f b{font-size:1.05rem}.fc-f .hint{font-size:.72rem;color:var(--dim);margin-top:auto}
.fc-b{background:var(--core);color:#fff;transform:rotateY(180deg);font-size:.85rem;line-height:1.4}
/* reveal */
.reveal{border:1px solid var(--line);border-radius:12px;margin:12px 0;overflow:hidden;background:var(--card)}
.reveal-q{width:100%;text-align:left;background:none;border:0;padding:16px 18px;font:600 1.05rem inherit;color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:10px}
.reveal-q::after{content:"+";color:var(--accent);font-size:1.3rem;flex:none}
.reveal.open .reveal-q::after{content:"−"}
.reveal-a{max-height:0;overflow:hidden;transition:max-height .3s;padding:0 18px}
.reveal.open .reveal-a{max-height:340px;padding:0 18px 16px}
/* quiz */
.quizq{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:14px 0}
.quizq .q{font-weight:600;margin:0 0 12px}
.opt{display:block;width:100%;text-align:left;background:var(--bg);border:1px solid var(--line);border-radius:9px;padding:11px 14px;margin:7px 0;font:inherit;cursor:pointer;transition:.12s}
.opt:hover{border-color:var(--accent)}.quizq.done .opt{cursor:default}
.opt.right{background:rgba(47,111,79,.16);border-color:var(--core);font-weight:600}
.opt.wrong{background:rgba(180,40,40,.14);border-color:#b42828}
.fb{display:none;margin:12px 0 0;padding:12px 14px;background:var(--bg);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;font-size:.92rem}
.fb.show{display:block}
/* source quote */
.srcq{margin:18px 0;padding:16px 20px;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--exec);border-radius:0 12px 12px 0}
.srcq p{margin:0 0 8px;font-style:italic}.srcq cite{font-style:normal;font-size:.85rem;color:var(--dim)}
.srcq cite a{color:var(--exec);text-decoration:none;font-weight:600}.srcq cite a:hover{text-decoration:underline}
.src-list{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 20px;margin:18px 0;font-size:.9rem}
.src-list h4{margin:0 0 8px}.src-list a{color:var(--exec);text-decoration:none}.src-list li{margin:5px 0}
/* completion */
.done-wrap{max-width:820px;margin:30px auto 0;padding:0 20px;text-align:center}
#mark-done{background:var(--card);border:1.5px solid var(--line);border-radius:30px;padding:12px 26px;font:600 .95rem inherit;color:var(--dim);cursor:pointer;transition:.15s}
#mark-done .cp-tick{opacity:.3}#mark-done .cp-on{display:none}
#mark-done:hover{border-color:var(--core)}
#mark-done.checked{background:var(--core);color:#fff;border-color:var(--core)}
#mark-done.checked .cp-tick{opacity:1}#mark-done.checked .cp-on{display:inline}#mark-done.checked .cp-off{display:none}
.done-tick{margin-left:auto;color:var(--core);font-weight:800;opacity:0;transition:.15s}
.mcard.completed .done-tick{opacity:1}.mcard.completed{border-color:var(--core)}
.mcard-top{display:flex;align-items:center;gap:8px}
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
