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
import glob, html, json, os, re, time
from datetime import date

BUILD_VER = str(int(time.time()))

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "self-mba")
INGEST = os.path.join(ROOT, "_ingest")
LESSONS = os.path.join(ROOT, "lessons")
DIST = os.path.join(ROOT, "site", "dist")

def load_lesson(track, mid):
    p = os.path.join(LESSONS, f"{track}-{mid}.html")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None

def load_summaries(track, mid):
    """Per-lecture extracted key points: { video_id: {gist, points[]} }."""
    p = os.path.join(ROOT, "summaries", f"{track}-{mid}.json")
    if os.path.exists(p):
        try: return json.load(open(p))
        except Exception: pass
    return {}

# Discussions (curated Reddit) didn't earn its place as a standalone section — the
# practitioner signal is better woven into lessons. Data stays on disk; flip to re-enable.
SHOW_DISCUSSIONS = False

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
    # --- The Canon (reading layer): one cluster per book-group ---
    "strategy": "Strategy", "leadership-presence": "Leadership & Presence",
    "mental-models": "Mental Models & Thinking", "org-design-mechanisms": "Org Design & Mechanisms",
    "landscape-competitive": "Landscape & Competitive", "negotiation-influence": "Negotiation & Influence",
    "execution-operations": "Execution & Operations", "culture-change": "Culture & Change",
    "risk-fragility": "Risk, Uncertainty & Fragility", "product-innovation": "Product Thinking & Innovation",
    "power-politics": "Power & Org Politics", "personal-effectiveness": "Personal Effectiveness",
    "financial-literacy": "Financial Literacy for Operators", "behavioral-decision": "Behavioral Design & Decision Science",
    "game-theory": "Game Theory & Strategic Interaction", "platform-strategy": "Network Effects & Platform Strategy",
    "systems-complexity": "Systems Thinking & Complexity", "information-communication": "Information & Communication",
    "economics-incentives": "Economics & Incentive Design", "history-judgment": "History & Judgment",
    "communication-storytelling": "Communication & Storytelling", "design-problem-solving": "Design Thinking & Problem-Solving",
    "ethics-judgment": "Ethics & Judgment",
}

# Canon clusters in display order → card codes C1..C23 (a reading layer, not a strict sequence)
CANON_ORDER = [
    "strategy", "leadership-presence", "mental-models", "org-design-mechanisms", "landscape-competitive",
    "negotiation-influence", "execution-operations", "culture-change", "risk-fragility", "product-innovation",
    "power-politics", "personal-effectiveness", "financial-literacy", "behavioral-decision", "game-theory",
    "platform-strategy", "systems-complexity", "information-communication", "economics-incentives",
    "history-judgment", "communication-storytelling", "design-problem-solving", "ethics-judgment",
]
CANON_CODE = {slug: f"C{i+1}" for i, slug in enumerate(CANON_ORDER)}

# Technical Foundations (benchmark gap-fillers) → cards G1..G5
TITLES.update({
    "managerial-accounting": "Managerial & Cost Accounting",
    "statistics-quant": "Quantitative Methods & Statistics",
    "marketing-strategy": "Marketing Strategy & Positioning",
    "information-systems": "Information Systems & Data",
    "business-law": "The Legal Environment of Business",
    "entrepreneurial-finance": "Entrepreneurial Finance",
})
GAP_ORDER = ["managerial-accounting", "statistics-quant", "marketing-strategy", "information-systems", "business-law", "entrepreneurial-finance"]
GAP_CODE = {slug: f"G{i+1}" for i, slug in enumerate(GAP_ORDER)}

# ---------- SVG icon system (replaces all emoji) ----------
IC = {
    'check': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8.5l3.5 3.5 6.5-7"/></svg>',
    'pencil': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 2l3.5 3.5L5.5 14H2v-3.5z"/></svg>',
    'target': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="8" cy="8" r="6.5"/><circle cx="8" cy="8" r="3.5"/><circle cx="8" cy="8" r=".8" fill="currentColor"/></svg>',
    'comment': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M1.5 1.5h13v9h-7l-4 3.5v-3.5h-2z"/></svg>',
    'arrow-r': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h10m-4-4l4 4-4 4"/></svg>',
    'arrow-l': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 8H3m4-4l-4 4 4 4"/></svg>',
    'arrow-up': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10l4-4 4 4"/></svg>',
    'diamond': '<svg class="ic" viewBox="0 0 16 16" fill="currentColor" opacity=".55"><path d="M8 2l5 6-5 6-5-6z"/></svg>',
    'signal': '<svg class="ic ic-signal" viewBox="0 0 16 16" fill="currentColor"><rect x="1.5" y="10" width="2.5" height="5" rx=".6"/><rect x="6" y="6" width="2.5" height="9" rx=".6"/><rect x="10.5" y="2" width="2.5" height="13" rx=".6"/></svg>',
    'play': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M4 2.5v11l9.5-5.5z"/></svg>',
    'chart': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 14V8"/><path d="M6 14V4"/><path d="M10 14V9"/><path d="M14 14V2"/></svg>',
    'home': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M1.5 7.5L8 1.5l6.5 6"/><path d="M3 7v7h10V7"/><path d="M6.5 14v-4h3v4"/></svg>',
    'external': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 9v5H2V4h5"/><path d="M9 1h6v6"/><path d="M15 1L7.5 8.5"/></svg>',
    'doc': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 1.5h6.5l3.5 3.5v9.5h-10z"/><path d="M10 1.5v3.5h3.5"/><path d="M6 7h4M6 9.5h4M6 12h2.5"/></svg>',
    'lesson': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><rect x="2" y="1" width="12" height="14" rx="1.5"/><path d="M5 5h6M5 8h6M5 11h3"/></svg>',
    'folder': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M1.5 3.5h4.5l2 2h6v8.5h-13z"/></svg>',
}

import math
def svg_progress_ring(pct, r=22, sw=3.5, color="var(--core)"):
    circ = 2 * math.pi * r
    offset = circ * (1 - pct / 100)
    d = (r + sw + 1) * 2
    cx = cy = r + sw + 1
    return (f'<svg class="prog-ring" viewBox="0 0 {d} {d}" width="{d}" height="{d}">'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--line)" stroke-width="{sw}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}" '
            f'stroke-linecap="round" transform="rotate(-90 {cx} {cy})"/>'
            f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
            f'class="prog-pct">{int(pct)}%</text></svg>')

def esc(s):
    return html.escape(str(s if s is not None else ""))

def latest_raw():
    dirs = sorted(glob.glob(os.path.join(INGEST, "raw", "*")))
    dirs = [d for d in dirs if os.path.isdir(d) and re.search(r"\d{4}-\d{2}-\d{2}$", d)]
    if not dirs:
        raise SystemExit("No raw pulls found. Run _ingest/pull.py first.")
    with_modules = [d for d in dirs if os.path.isdir(os.path.join(d, "core"))]
    return with_modules[-1] if with_modules else dirs[-1]

def fmt_int(v):
    try: return f"{int(float(v)):,}"
    except (ValueError, TypeError): return str(v or "")

def fmt_dur(v):
    try:
        s = int(float(v)); return f"{s//60}:{s%60:02d}"
    except (ValueError, TypeError): return ""

def code(track, mid):
    if track == "canon": return CANON_CODE.get(mid, IC['diamond'])
    if track == "gaps": return GAP_CODE.get(mid, IC['diamond'])
    return mid.split("-")[0].upper() if track == "exec" else mid.split("-")[0]

def load_module(mdir):
    vids, reddit = [], []
    for f in sorted(glob.glob(os.path.join(mdir, "yt_*.json"))):
        try: vids += json.load(open(f))
        except Exception: pass
    # Prefer the educationally re-scored, curated Reddit set; fall back to raw pulls.
    curated = os.path.join(mdir, "curated_reddit.json")
    if os.path.exists(curated):
        try: reddit = json.load(open(curated))
        except Exception: pass
    else:
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
    reddit.sort(key=lambda r: (int(r.get("edu_score", 0) or 0), int(r.get("signal", 0) or 0), int(float(r.get("ups", 0) or 0))), reverse=True)
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
<meta name="theme-color" content="#faf7f2">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..600&family=Literata:ital,opsz,wght@0,7..72,300..600;1,7..72,300..500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}?v=""" + BUILD_VER + """"></head><body>"""

def render_video(v, summary=None):
    tr = (v.get("transcript") or "").strip()
    url = esc(v.get("url"))
    meta = " · ".join(x for x in [esc(v.get("channel")), fmt_dur(v.get("duration")),
                                  (fmt_int(v.get("views")) + " views") if v.get("views") not in (None, "", "NA") else ""] if x)
    watch = f'<a class="watch" href="{url}" target="_blank" rel="noopener">Watch ↗</a>' if url else ""
    # Extracted key points — read it here, no need to leave for YouTube.
    summ = ""
    if summary and summary.get("points"):
        pts = "".join(f"<li>{esc(p)}</li>" for p in summary["points"])
        gist = f'<p class="lec-gist">{esc(summary.get("gist",""))}</p>' if summary.get("gist") else ""
        summ = f'<div class="lec-sum">{gist}<ul class="lec-pts">{pts}</ul></div>'
    # Transcript stays as an optional collapsed extra.
    tr_html = ""
    if tr:
        paras = re.split(r"(?<=[.!?])\s+(?=[A-Z])", tr)
        chunks, buf = [], ""
        for p in paras:
            buf += p + " "
            if len(buf) > 600:
                chunks.append(buf.strip()); buf = ""
        if buf.strip(): chunks.append(buf.strip())
        inner = "".join(f"<p>{esc(c)}</p>" for c in chunks)
        words = len(tr) // 5
        lbl = "Full transcript" if summ else f"Read transcript · ~{words:,} words"
        tr_html = f'<details class="tr"><summary>{lbl}</summary><div class="tr-body">{inner}</div></details>'
    elif not summ:
        tr_html = '<div class="no-tr">No transcript available — watch on YouTube.</div>'
    return f"""<article class="card vid">
<div class="card-head"><span class="ttl">{esc(v.get('title'))}</span> {sig_badge(v.get('signal'))}</div>
<div class="meta">{meta}{(' · ' + watch) if watch else ''}</div>{summ}{tr_html}</article>"""

def render_reddit(r):
    txt = (r.get("selftext") or "").strip()
    excerpt = (txt[:600] + "…") if len(txt) > 600 else txt
    return f"""<article class="card thread">
<div class="card-head"><a class="ttl" href="{esc(r.get('url'))}" target="_blank" rel="noopener">{esc(r.get('title'))}</a> {sig_badge(r.get('signal'))}</div>
<div class="meta">r/{esc(r.get('sub'))} · ▲ {fmt_int(r.get('ups'))} · {IC['comment']} {fmt_int(r.get('comments'))} · u/{esc(r.get('author'))}</div>
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

def render_module(track, mid, vids, reddit, edgar, prevnext, lesson=None, summaries=None):
    c = code(track, mid)
    title = TITLES.get(mid, mid)
    summaries = summaries or {}
    show_disc = SHOW_DISCUSSIONS and reddit
    toc = []
    if lesson: toc.append('<a href="#lesson">Lesson</a>')
    toc.append('<a href="#videos">Lectures · learn</a>')
    if show_disc: toc.append('<a href="#discuss">Discussions · reality</a>')
    if edgar: toc.append('<a href="#fin">Data · apply</a>')
    sections = []
    if lesson:
        sections.append(f'<section id="lesson" class="lesson">{lesson}</section>')
        # The connective tissue: name the learning loop so the sources aren't a junk drawer.
        modes = ["<b>learn</b> the theory (Lectures)"]
        if show_disc: modes.append("<b>stress-test</b> it against reality (Discussions)")
        if edgar: modes.append("<b>apply</b> it to real data (Financials)")
        sections.append(
            '<div class="source-divider"><span>How to go deeper</span></div>'
            f'<p class="loop-line">The lesson above was <b>distilled from the sources below.</b> '
            f'Use them to {" → ".join(modes)}.</p>')
    vids_html = "".join(render_video(v, summaries.get(v.get("id"))) for v in vids) or "<p class='empty'>No lectures pulled.</p>"
    n_sum = sum(1 for v in vids if summaries.get(v.get("id")))
    obj = ("The key points of each talk, extracted so you can learn them here — no need to leave. "
           "Open the full transcript or watch only if you want more.") if n_sum else \
          ("The frameworks taught above come from these talks — watch any to go deeper on a concept.")
    sections.append(
        f'<section id="videos"><h2>Lectures <span class="count">{len(vids)}</span></h2>'
        f'<p class="section-obj"><span class="obj-tag">Learn</span> {obj}</p>'
        f'{vids_html}</section>')
    if show_disc:
        sections.append(
            f'<section id="discuss"><h2>Practitioner Reality-Check <span class="count">{len(reddit)}</span></h2>'
            f'<p class="section-obj"><span class="obj-tag">Stress-test</span> Does the theory survive the real world? Curated from working practitioners — where they confirm, complicate, or push back on the frameworks.</p>'
            f'{"".join(render_reddit(r) for r in reddit)}</section>')
    if edgar:
        sections.append(
            f'<section id="fin"><h2>The Primary Data <span class="count">{len(edgar)}</span></h2>'
            f'<p class="section-obj"><span class="obj-tag">Apply</span> The real SEC filings <b>behind the worked example above.</b> Run <code>edgar.py company TICKER</code> to do your own analysis.</p>'
            f'{render_edgar(edgar)}</section>')
    pn = ""
    if prevnext[0]: pn += f'<a class="pn" href="{prevnext[0][0]}">{IC["arrow-l"]} {esc(prevnext[0][1])}</a>'
    if prevnext[1]: pn += f'<a class="pn next" href="{prevnext[1][0]}">{esc(prevnext[1][1])} {IC["arrow-r"]}</a>'
    done_btn = (f'<button id="mark-done" data-mod="{track}-{mid}.html"><span class="cp-tick">{IC["check"]}</span> '
                f'<span class="cp-on">Module complete</span><span class="cp-off">Mark module complete</span></button>') if lesson else ""
    track_name = {"exec": "Executive Track", "canon": "The Canon · Reading Layer",
                  "gaps": "Technical Foundations"}.get(track, "Core Curriculum")
    return HEAD.format(title=f"{c} · {title}", css="style.css") + f"""
{'<div id="progress"></div>' if lesson else ''}
<header class="mod-header {('exec' if track=='exec' else 'core')}">
<a href="index.html" class="home">{IC['arrow-l']} Index</a>
<div class="eyebrow"><span class="num">{esc(c)}</span> {track_name}</div>
<h1>{esc(title)}</h1>
<div class="hairline"></div></header>
<nav class="toc">{" ".join(toc)}</nav>"""+f"""
<main>{"".join(sections)}</main>
<div class="done-wrap">{done_btn}</div>
<div class="pn-wrap">{pn}</div>
<a href="#" class="top">{IC['arrow-up']}</a>
<script src="lesson.js?v={BUILD_VER}"></script>
</body></html>"""

def render_index(modules, stats):
    # Compute lesson coverage per track
    cov = {}
    for track in ("core", "exec", "canon", "gaps"):
        total = len(modules[track])
        ready = sum(1 for mid, v, r, e in modules[track] if load_lesson(track, mid))
        cov[track] = (ready, total, int(ready / total * 100) if total else 0)
    total_lessons = sum(c[0] for c in cov.values())
    total_modules = sum(c[1] for c in cov.values())
    overall_pct = int(total_lessons / total_modules * 100) if total_modules else 0

    def cards(track):
        out = []
        for mid, v, r, e in modules[track]:
            c = code(track, mid); title = TITLES.get(mid, mid)
            words = sum(len(x.get("transcript") or "") for x in v) // 5
            ready = load_lesson(track, mid)
            lesson_tag = f'<span class="lesson-tag">{IC["lesson"]} Lesson ready</span>' if ready else f'<span class="lesson-tag pending">{IC["folder"]} Sources only</span>'
            metas = [f"{len(v)} lectures", f"{words:,} words"]
            if r: metas.append(f"{len(r)} threads")
            if e: metas.append(f"{len(e)} filings")
            out.append(f"""<a class="mcard {('exec' if track=='exec' else 'core')}{' ready' if ready else ''}" href="{track}-{mid}.html" data-mod="{track}-{mid}">
<div class="mcard-num">{esc(c)}</div>
<div class="mcard-body">
<h3>{esc(title)}</h3>
<div class="mcard-drawer">
<div class="mcard-top">{lesson_tag}<span class="done-tick">{IC["check"]} done</span></div>
<div class="mstats">{"".join(f'<span>{m}</span>' for m in metas)}</div></div></div>
<span class="mcard-arrow">{IC["arrow-r"]}</span></a>""")
        return "".join(out)

    def track_head(label, track, count_label, color="var(--core)"):
        r, t, pct = cov[track]
        ring = svg_progress_ring(pct, r=18, sw=3, color=color)
        return (f'<div class="track-head">'
                f'<span class="th-label">{label}</span><span class="th-rule"></span>'
                f'<span class="th-cov">{ring}<span class="th-cov-label">{r}/{t} lessons</span></span>'
                f'<span class="th-count">{count_label}</span></div>')

    # Visual stats dashboard
    stats_viz = f"""<div class="stats-dash">
<div class="stat-card"><div class="stat-num">{stats['modules']}</div><div class="stat-label">modules</div></div>
<div class="stat-card"><div class="stat-num">{stats['videos']}</div><div class="stat-label">lectures</div></div>
<div class="stat-card"><div class="stat-num">{stats['words']:,}</div><div class="stat-label">words of transcript</div></div>
<div class="stat-card"><div class="stat-num">{total_lessons}</div><div class="stat-label">interactive lessons</div>
<div class="stat-bar-wrap"><div class="stat-bar-fill" style="width:{overall_pct}%"></div></div>
<div class="stat-sub">{overall_pct}% coverage</div></div>
</div>"""

    return HEAD.format(title="The Compounding MBA", css="style.css") + f"""
<header class="hero">
<div class="eyebrow">Self-directed · Master's level</div>
<h1>The Compounding <em>MBA</em></h1>
<p class="sub">A master's-level business education, distilled from elite sources into interactive, visual lessons — grounded in primary data.</p>
{stats_viz}
<div class="exam-links">
<a class="exam-link" href="exam.html">{IC['pencil']} <span class="exam-title">Self-diagnostic</span> <span class="exam-sub">recall</span> {IC['arrow-r']}</a>
<a class="exam-link bench" href="benchmark-exam.html">{IC['target']} <span class="exam-title">Calibrated benchmark</span> <span class="exam-sub">exam-level</span> {IC['arrow-r']}</a>
</div>
<input id="q" placeholder="Search modules…" oninput="filt()">
</header>
<main>
{track_head('Core Curriculum', 'core', '12 modules', 'var(--core)')}
<div class="grid">{cards('core')}</div>
{track_head('Executive Track', 'exec', '12 modules', 'var(--exec)')}
<div class="grid">{cards('exec')}</div>
{track_head('The Canon · Reading Layer', 'canon', '23 clusters', 'var(--brass)')}
<div class="grid">{cards('canon')}</div>
{track_head('Technical Foundations', 'gaps', f'{len(modules["gaps"])} modules', 'var(--core)')}
<div class="grid">{cards('gaps')}</div>
</main>
<footer>Generated from <code>~/self-mba/_ingest/raw/{stats['date']}</code> · rebuild with <code>python3 site/build.py</code></footer>
<script>
function filt(){{var q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('.mcard').forEach(function(c){{
c.style.display = c.textContent.toLowerCase().includes(q) ? '' : 'none';}});}}
</script>
<script src="index.js?v=""" + BUILD_VER + """"></script>
</body></html>"""

CSS = """
:root{
--bg:#faf7f2;--bg2:#f3efe8;--surface:#ffffff;--surface2:#f0ece5;
--line:#e2ddd4;--line2:#d0c9be;
--ink:#1c1917;--ink2:#3d3833;--dim:#8a837a;
--brass:#9a7b2e;--brass2:#7a6121;--core:#2d7a4a;--exec:#b86e1a;
--wrong:#c4372a;
--serif:'Fraunces',Georgia,serif;--read:'Literata',Georgia,serif;--mono:'IBM Plex Mono',ui-monospace,monospace;
--wrap:920px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink2);font:19px/1.78 var(--read);-webkit-font-smoothing:antialiased;overflow-x:hidden}
::selection{background:var(--brass);color:#fff}
a{color:inherit}main{max-width:var(--wrap);margin:0 auto;padding:0 24px 100px;position:relative;z-index:2}
/* ---------- SVG ICON SYSTEM ---------- */
.ic{display:inline-block;width:1em;height:1em;vertical-align:-.125em;flex-shrink:0}
.ic-signal{width:1.1em}
.lesson-tag .ic,.exam-link .ic,.done-tick .ic,.home .ic,.mcard-arrow .ic,.pn .ic,.top .ic,.cp-tick .ic{width:.85em;height:.85em}
.top .ic{width:1.2em;height:1.2em;vertical-align:-.1em}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
/* ---------- HERO / INDEX ---------- */
.hero{max-width:var(--wrap);margin:0 auto;padding:clamp(56px,10vh,100px) 24px 36px;position:relative;z-index:2}
.eyebrow{font:500 .72rem/1 var(--mono);letter-spacing:.32em;text-transform:uppercase;color:var(--brass);animation:rise .7s .05s both}
.hero h1{font:300 clamp(3rem,9vw,5.5rem)/.94 var(--serif);color:var(--ink);letter-spacing:-.025em;margin:.28em 0 .12em;animation:rise .9s .12s both}
.hero h1 em{font-style:italic;font-weight:400;color:var(--brass)}
.sub{font-size:1.2rem;line-height:1.6;color:var(--dim);max-width:38ch;margin:0 0 32px;animation:rise .8s .26s both}
/* stats dashboard */
.stats-dash{display:flex;flex-wrap:wrap;gap:20px;margin-bottom:32px;animation:rise .8s .35s both}
.stat-card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:20px 24px;flex:1;min-width:130px;box-shadow:0 1px 3px rgba(0,0,0,.04);transition:border-color .2s,box-shadow .2s}
.stat-card:hover{border-color:var(--line2);box-shadow:0 4px 12px rgba(0,0,0,.07)}
.stat-num{font:600 clamp(1.6rem,4vw,2.2rem) var(--serif);color:var(--brass);letter-spacing:-.02em}
.stat-label{font:500 .7rem var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin-top:4px}
.stat-bar-wrap{height:4px;background:var(--line);border-radius:4px;margin-top:10px;overflow:hidden}
.stat-bar-fill{height:100%;background:linear-gradient(90deg,var(--core),var(--brass));border-radius:4px;transition:width .6s ease}
.stat-sub{font:500 .64rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--core);margin-top:6px}
/* exam links */
.exam-links{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:32px;animation:rise .8s .45s both}
.exam-link{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border:1px solid var(--line2);border-radius:8px;color:var(--ink2);text-decoration:none;font:600 .8rem var(--mono);letter-spacing:.05em;transition:.2s}
.exam-link:hover{border-color:var(--brass);color:var(--ink);background:var(--surface);box-shadow:0 2px 8px rgba(0,0,0,.06)}
.exam-link.bench{border-color:color-mix(in srgb,var(--brass) 50%,transparent);color:var(--brass)}
.exam-link.bench:hover{border-color:var(--brass);background:color-mix(in srgb,var(--brass) 6%,transparent)}
.exam-title{text-transform:uppercase}.exam-sub{color:var(--dim);font-weight:400}
.exam-link .ic:last-child{opacity:.4;transition:opacity .2s}.exam-link:hover .ic:last-child{opacity:1}
/* progress rings */
.prog-ring{flex-shrink:0}
.prog-pct{font:600 .6rem var(--mono);fill:var(--ink2);letter-spacing:.02em}
#q{width:100%;max-width:440px;padding:14px 4px;border:0;border-bottom:1px solid var(--line2);background:transparent;color:var(--ink);font:1.1rem var(--read);animation:rise .8s .5s both;transition:border-color .2s}
#q::placeholder{color:var(--dim);font-style:italic}#q:focus{outline:0;border-color:var(--brass)}
/* track header */
.track-head{display:flex;align-items:center;gap:14px;max-width:var(--wrap);margin:48px auto 18px;padding:0 24px}
.th-label{font:500 .82rem/1 var(--mono);letter-spacing:.24em;text-transform:uppercase;color:var(--ink);white-space:nowrap}
.th-rule{flex:1;height:1px;background:var(--line)}
.th-cov{display:flex;align-items:center;gap:8px;white-space:nowrap}
.th-cov-label{font:.68rem var(--mono);color:var(--dim);letter-spacing:.04em;text-transform:uppercase}
.th-count{font:.78rem var(--mono);color:var(--dim);white-space:nowrap}
/* module cards — file-cabinet drawer */
.grid{max-width:var(--wrap);margin:0 auto;padding:0 24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.mcard{display:flex;align-items:center;gap:0;text-decoration:none;background:var(--surface);border:1px solid var(--line2);border-radius:10px;position:relative;overflow:hidden;animation:rise .6s both;box-shadow:0 1px 4px rgba(0,0,0,.06);transition:border-color .25s,box-shadow .25s}
.mcard:hover{border-color:var(--brass);box-shadow:0 6px 20px rgba(0,0,0,.09)}
.mcard-num{font:300 2rem/1 var(--serif);color:var(--line2);padding:18px 0 18px 20px;min-width:60px;transition:color .25s}
.mcard:hover .mcard-num{color:var(--brass)}.mcard.exec:hover .mcard-num{color:var(--exec)}
.mcard-body{flex:1;padding:18px 14px 18px 6px}
.mcard h3{font:400 1.18rem/1.25 var(--serif);color:var(--ink);margin:0 0 0;letter-spacing:-.01em;transition:color .2s}
.mcard:hover h3{color:var(--brass)}.mcard.exec:hover h3{color:var(--exec)}
.mcard-drawer{max-height:0;overflow:hidden;transition:max-height .35s ease,opacity .3s;opacity:0}
.mcard:hover .mcard-drawer{max-height:120px;opacity:1}
.mcard-top{display:flex;align-items:center;gap:8px;margin-top:8px;min-height:0}
.mstats{display:flex;flex-wrap:wrap;gap:0 12px;font:.7rem/1.6 var(--mono);color:var(--dim);text-transform:uppercase;letter-spacing:.04em;margin-top:4px}
.mcard-arrow{align-self:center;padding-right:18px;color:var(--brass);font-size:1.1rem;opacity:0;transform:translateX(-6px);transition:.25s}
.mcard:hover .mcard-arrow{opacity:1;transform:none}.mcard.exec .mcard-arrow{color:var(--exec)}
.lesson-tag{font:500 .62rem/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--core);border:1px solid color-mix(in srgb,var(--core) 35%,transparent);border-radius:20px;padding:3px 8px}
.exec .lesson-tag{color:var(--exec);border-color:color-mix(in srgb,var(--exec) 35%,transparent)}
.lesson-tag.pending{color:var(--dim);border-color:var(--line2)}
.done-tick{margin-left:auto;font:500 .62rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--core);opacity:0}
.mcard.completed .done-tick{opacity:1}.mcard.completed{background:color-mix(in srgb,var(--core) 5%,transparent)}
/* ---------- MODULE PAGE ---------- */
.mod-header{max-width:var(--wrap);margin:0 auto;padding:clamp(40px,8vh,80px) 24px 0;position:relative;z-index:2}
.home{font:500 .74rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);text-decoration:none;transition:color .2s}.home:hover{color:var(--brass)}
.mod-header .eyebrow{margin-top:26px;color:var(--dim)}.mod-header .eyebrow .num{color:var(--brass);font-weight:600}
.mod-header.exec .eyebrow .num{color:var(--exec)}
.mod-header h1{font:300 clamp(2.6rem,6vw,4.2rem)/1 var(--serif);color:var(--ink);letter-spacing:-.02em;margin:.18em 0 .5em}
.hairline{height:1px;background:linear-gradient(90deg,var(--brass),transparent 70%)}
.mod-header.exec .hairline{background:linear-gradient(90deg,var(--exec),transparent 70%)}
.toc{position:sticky;top:0;z-index:20;backdrop-filter:blur(12px);background:color-mix(in srgb,var(--bg) 90%,transparent);max-width:var(--wrap);margin:0 auto;padding:16px 24px;border-bottom:1px solid var(--line);display:flex;gap:24px;flex-wrap:wrap}
.toc a{font:500 .74rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);text-decoration:none;transition:color .2s}.toc a:hover{color:var(--brass)}
section{margin-top:56px}
section>h2{font:300 clamp(1.7rem,3.5vw,2.3rem) var(--serif);color:var(--ink);letter-spacing:-.01em;border-bottom:1px solid var(--line);padding-bottom:12px;display:flex;align-items:baseline;gap:12px}
.count{font:.72rem var(--mono);color:var(--dim);letter-spacing:.08em}
/* source cards */
.card{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:20px;margin:14px 0;transition:border-color .2s,box-shadow .2s}.card:hover{border-color:var(--line2);box-shadow:0 2px 8px rgba(0,0,0,.04)}
.card-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.ttl{font:500 1.18rem/1.35 var(--read);color:var(--ink);text-decoration:none}.ttl:hover{color:var(--brass)}
.meta{font:.74rem/1.6 var(--mono);color:var(--dim);text-transform:uppercase;letter-spacing:.03em;margin-top:7px}
.sig,.sig-hi{font:.64rem var(--mono);letter-spacing:.08em;text-transform:uppercase;border-radius:30px;padding:3px 9px;color:var(--brass);border:1px solid color-mix(in srgb,var(--brass) 40%,transparent);white-space:nowrap}.sig-hi{color:var(--brass);background:color-mix(in srgb,var(--brass) 10%,transparent)}
.watch{font:.7rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--brass);text-decoration:none;white-space:nowrap}.watch:hover{color:var(--brass2)}
.lec-sum{margin-top:14px;border-left:2px solid var(--core);padding-left:18px}
.lec-gist{font:500 1.08rem/1.5 var(--read);color:var(--ink);margin:0 0 10px}
.lec-pts{margin:0;padding-left:0;list-style:none}
.lec-pts li{position:relative;padding-left:22px;margin:8px 0;color:var(--ink2);line-height:1.55}
.lec-pts li::before{content:"→";position:absolute;left:0;color:var(--core);font-weight:600}
.tr{margin-top:14px}.tr summary{cursor:pointer;font:500 .74rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dim);list-style:none}.tr summary:hover{color:var(--brass)}.tr summary::-webkit-details-marker{display:none}.tr summary::before{content:"▸ ";color:var(--brass)}.tr[open] summary::before{content:"▾ "}
.tr-body{margin-top:14px;font:1.12rem/1.85 var(--read);color:var(--ink2);border-left:2px solid var(--brass);padding-left:22px;max-height:580px;overflow:auto}
.tr-body p{margin:0 0 16px}.no-tr{margin-top:10px;color:var(--dim);font-style:italic;font-size:.92rem}
.excerpt{color:var(--ink2);font-size:1rem;margin:12px 0 0;opacity:.85}
.edgar{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:20px;margin:14px 0;font:.84rem/1.6 var(--mono);color:var(--ink2);white-space:pre-wrap}
.edgar h3{font:600 1.1rem var(--mono);color:var(--ink);margin:0 0 6px}.edgar h4{font:.95rem var(--mono);color:var(--brass);margin:16px 0 4px}
.empty{color:var(--dim);font-style:italic}
.pn-wrap{max-width:var(--wrap);margin:50px auto;padding:0 24px;display:flex;justify-content:space-between;gap:14px;position:relative;z-index:2}
.pn{flex:1;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:18px;text-decoration:none;color:var(--dim);font:500 .82rem var(--mono);letter-spacing:.04em;transition:.2s}
.pn.next{text-align:right}.pn:hover{border-color:var(--brass);color:var(--ink);box-shadow:0 2px 8px rgba(0,0,0,.05)}
.top{position:fixed;bottom:26px;right:26px;z-index:40;background:var(--brass);color:#fff;border-radius:50%;width:48px;height:48px;display:flex;align-items:center;justify-content:center;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.15);font-size:1.1rem}
footer{max-width:var(--wrap);margin:0 auto;padding:36px 24px;color:var(--dim);font:.78rem/1.8 var(--mono);text-align:center;border-top:1px solid var(--line);position:relative;z-index:2}
footer code{color:var(--ink2)}
/* ---------- LESSON TYPOGRAPHY ---------- */
.lesson{font-size:1.16rem;line-height:1.78}
.lesson h2{font:300 clamp(1.8rem,4vw,2.6rem) var(--serif);color:var(--ink);letter-spacing:-.015em;margin:52px 0 14px;padding-top:14px;border-top:1px solid var(--line)}
.lesson h3{font:500 1.15rem var(--read);color:var(--ink);margin:0 0 8px}
.lesson p{margin:0 0 18px}
.lead{font:300 1.5rem/1.5 var(--read);color:var(--ink);margin-bottom:8px!important}
.lead::first-letter{font:600 4.2rem/.8 var(--serif);float:left;color:var(--brass);padding:6px 12px 0 0}
.lesson em{font-style:italic;color:var(--brass)}
.lesson b{color:var(--ink);font-weight:600}
.equation{font:400 clamp(1.6rem,5vw,2.4rem) var(--serif);text-align:center;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:26px;margin:24px 0;color:var(--ink);letter-spacing:.01em;box-shadow:0 1px 4px rgba(0,0,0,.04)}
figure.viz{margin:28px 0;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:26px}
figure.viz svg{width:100%;height:auto}
figure.viz figcaption{font:.92rem/1.5 var(--read);font-style:italic;color:var(--dim);margin-top:14px;text-align:center}
.vlabel{font:500 12px var(--mono);fill:var(--dim);text-transform:uppercase;letter-spacing:.04em}.vlabel-in{font:600 12px var(--mono);fill:var(--brass)}
.bar-txt{font:600 13px var(--mono);fill:var(--ink);text-anchor:middle}.bar-txt-sm{font:600 11px var(--mono);fill:var(--ink);text-anchor:middle}
.bar-asset{fill:color-mix(in srgb,var(--core) 30%,var(--bg2))}.bar-liab{fill:var(--exec)}.bar-eq{fill:var(--core)}
.bar-rev{fill:color-mix(in srgb,var(--core) 30%,var(--bg2))}.bar-gross{fill:var(--core)}.bar-net{fill:var(--brass)}
.bar-asset~.bar-txt,.bar-rev~.bar-txt{fill:var(--ink)}
.example{background:color-mix(in srgb,var(--core) 5%,transparent);border-left:3px solid var(--core);border-radius:0 8px 8px 0;padding:18px 24px;margin:22px 0}
.example p{margin:10px 0}
.pitfall{background:color-mix(in srgb,var(--exec) 6%,transparent);border:1px solid color-mix(in srgb,var(--exec) 25%,transparent);border-radius:8px;padding:18px 24px;margin:22px 0}
.pitfall.subtle{background:var(--surface);border-color:var(--line)}.pitfall h3{color:var(--exec);margin-bottom:6px}.pitfall.subtle h3{color:var(--brass)}
.apply-box{background:color-mix(in srgb,var(--brass) 8%,transparent);border:1px solid color-mix(in srgb,var(--brass) 30%,transparent);border-radius:8px;padding:22px 26px;margin:32px 0}
.apply-box h3{color:var(--brass);margin-bottom:6px}
.apply-box code,.lesson code,.lead code{background:var(--bg2);border:1px solid var(--line);padding:2px 7px;border-radius:4px;font:.88rem var(--mono);color:var(--brass)}
.source-divider{text-align:center;margin:60px 0 10px;border-top:1px solid var(--line)}
.source-divider span{position:relative;top:-11px;background:var(--bg);padding:0 18px;font:500 .74rem var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--dim);display:inline-block}
.loop-line{max-width:62ch;margin:0 auto 8px;text-align:center;font:1.02rem/1.6 var(--read);color:var(--dim)}.loop-line b{color:var(--ink2)}
.section-obj{font:1rem/1.55 var(--read);color:var(--dim);margin:0 0 18px;padding:12px 16px;background:var(--surface);border-radius:4px;border-left:3px solid var(--line2)}
.section-obj b{color:var(--ink2)}.section-obj code{background:var(--bg);border:1px solid var(--line);padding:1px 6px;border-radius:4px;font:.84rem var(--mono);color:var(--brass2)}
#videos .section-obj{border-left-color:var(--core)}#discuss .section-obj{border-left-color:var(--exec)}#fin .section-obj{border-left-color:var(--brass)}
.obj-tag{display:inline-block;font:600 .64rem var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--bg);padding:3px 9px;border-radius:30px;margin-right:8px;vertical-align:middle}
#videos .obj-tag{background:var(--core)}#discuss .obj-tag{background:var(--exec)}#fin .obj-tag{background:var(--brass)}
/* ---------- INTERACTIVE COMPONENTS ---------- */
#progress{position:fixed;top:0;left:0;height:3px;width:0;background:linear-gradient(90deg,var(--brass),var(--core));z-index:50;transition:width .1s}
.tip{position:absolute;z-index:60;background:var(--surface);border:1px solid var(--line2);color:var(--ink);font:.84rem/1.45 var(--read);padding:10px 14px;border-radius:8px;max-width:280px;pointer-events:none;opacity:0;transform:translate(-50%,-100%);transition:opacity .12s;box-shadow:0 6px 20px rgba(0,0,0,.1)}
.tip.show{opacity:1}
.hot{cursor:pointer;transition:opacity .15s}.hot:hover{opacity:.82}.hot.active{stroke:var(--ink);stroke-width:2}
.fc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(172px,1fr));gap:14px;margin:24px 0}
.fc{position:relative;display:block;background:none;border:0;padding:0;height:152px;cursor:pointer;font:inherit;text-align:left}
.fc-inner{display:block;position:relative;width:100%;height:100%}
.fc-f,.fc-b{position:absolute;inset:0;border:1px solid var(--line);border-radius:8px;padding:16px;display:flex;flex-direction:column;justify-content:space-between;transition:opacity .35s,transform .35s}
.fc-f{background:var(--surface);box-shadow:0 1px 3px rgba(0,0,0,.04)}
.fc:hover .fc-f{border-color:var(--brass);box-shadow:0 3px 10px rgba(0,0,0,.07)}
.fc-f b{font:400 1.34rem var(--serif);color:var(--ink)}
.fc-f .hint{font:.6rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass);white-space:nowrap;opacity:.85}
.fc-b{background:var(--core);color:#fff;font-size:.95rem;line-height:1.46;justify-content:center;opacity:0;transform:scale(.97);pointer-events:none;border-color:var(--core)}
.fc.flipped .fc-f{opacity:0;transform:scale(.97)}
.fc.flipped .fc-b{opacity:1;transform:none}
.reveal{border:1px solid var(--line);border-radius:8px;margin:12px 0;overflow:hidden;background:var(--surface);transition:border-color .2s}.reveal.open{border-color:var(--brass)}
.reveal-q{width:100%;text-align:left;background:none;border:0;padding:18px 20px;font:400 1.2rem var(--serif);color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:10px}
.reveal-q::after{content:"+";color:var(--brass);font:300 1.6rem var(--serif);flex:none}.reveal.open .reveal-q::after{content:"–"}
.reveal-a{max-height:0;overflow:hidden;transition:max-height .35s ease}.reveal-a p{padding:0 20px;margin:0 0 18px}.reveal.open .reveal-a{max-height:360px}
.quizq{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:22px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,.03)}
.quizq .q{font:500 1.12rem var(--read);color:var(--ink);margin:0 0 14px}
.opt{display:block;width:100%;text-align:left;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:13px 16px;margin:8px 0;font:1rem var(--read);color:var(--ink2);cursor:pointer;transition:.15s}
.opt:hover{border-color:var(--brass);color:var(--ink)}.quizq.done .opt{cursor:default}
.opt.right{background:color-mix(in srgb,var(--core) 12%,transparent);border-color:var(--core);color:var(--ink);position:relative;padding-right:36px}
.opt.right::after{content:"";position:absolute;right:14px;top:50%;transform:translateY(-50%);width:16px;height:16px;background:var(--core);-webkit-mask:url("data:image/svg+xml,%3Csvg viewBox='0 0 16 16' fill='none' stroke='%23fff' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 8.5l3.5 3.5 6.5-7'/%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg viewBox='0 0 16 16' fill='none' stroke='%23fff' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 8.5l3.5 3.5 6.5-7'/%3E%3C/svg%3E") center/contain no-repeat}
.opt.wrong{background:color-mix(in srgb,var(--wrong) 16%,transparent);border-color:var(--wrong)}
.fb{display:none;margin:14px 0 0;padding:14px 16px;background:var(--bg2);border-left:3px solid var(--brass);border-radius:0 6px 6px 0;font-size:.98rem}
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
#mark-done .cp-tick{opacity:.35;display:inline-flex}#mark-done .cp-on{display:none}
#mark-done:hover{border-color:var(--core);color:var(--ink)}
#mark-done.checked{background:var(--core);color:#fff;border-color:var(--core)}
#mark-done.checked .cp-tick{opacity:1}#mark-done.checked .cp-on{display:inline}#mark-done.checked .cp-off{display:none}
@media(max-width:640px){.grid{grid-template-columns:1fr;gap:10px}.mcard-num{font-size:1.6rem;min-width:48px;padding-left:16px}.stats-dash{gap:10px}.stat-card{min-width:0;padding:16px}}
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

    modules = {"core": [], "exec": [], "canon": [], "gaps": []}
    order = []  # (track, mid, filename, title)
    for track in ("core", "exec", "canon", "gaps"):
        for mid in manifest.get(track, {}):
            if mid.startswith("_"): continue
            mdir = os.path.join(raw, track, mid)
            v, r, e = load_module(mdir) if os.path.isdir(mdir) else ([], [], [])
            modules[track].append((mid, v, r, e))
            order.append((track, mid, f"{track}-{mid}.html", TITLES.get(mid, mid)))

    # module pages with prev/next
    flat = [(t, m, modules[t][i][1], modules[t][i][2], modules[t][i][3])
            for t in ("core", "exec", "canon", "gaps") for i, (m, *_ ) in enumerate(modules[t])]
    for idx, (track, mid, v, r, e) in enumerate(flat):
        prev = (order[idx-1][2], f"{code(*order[idx-1][:2])} {order[idx-1][3]}") if idx > 0 else None
        nxt = (order[idx+1][2], f"{code(*order[idx+1][:2])} {order[idx+1][3]}") if idx < len(flat)-1 else None
        page = render_module(track, mid, v, r, e, (prev, nxt),
                             lesson=load_lesson(track, mid), summaries=load_summaries(track, mid))
        open(os.path.join(DIST, f"{track}-{mid}.html"), "w", encoding="utf-8").write(page)

    stats = {
        "date": pull_date, "modules": len(flat),
        "videos": sum(len(v) for _,_,v,_,_ in flat),
        "words": sum(len(x.get("transcript") or "") for _,_,v,_,_ in flat for x in v) // 5,
        "threads": sum(len(r) for _,_,_,r,_ in flat),
        "filings": sum(len(e) for _,_,_,_,e in flat),
    }
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(render_index(modules, stats))
    # regenerate the diagnostic + calibrated-benchmark exams
    import subprocess
    subprocess.run(["python3", os.path.join(INGEST, "build_exam.py")], check=False)
    subprocess.run(["python3", os.path.join(INGEST, "build_benchmark.py")], check=False)
    print(f"Built site -> {DIST}")
    print(f"  {stats['modules']} module pages · {stats['videos']} lectures · {stats['words']:,} words · {stats['threads']} threads")
    print(f"  open: {os.path.join(DIST, 'index.html')}")

if __name__ == "__main__":
    main()
