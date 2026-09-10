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
import glob, html, json, os, re, shutil, time
from collections import Counter
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

STOP_WORDS = frozenset("""
a about above after again against all am an and any are aren't as at be because been
before being below between both but by can't cannot could couldn't did didn't do does
doesn't doing don't down during each few for from further get got had hadn't has hasn't
have haven't having he he'd he'll he's her here here's hers herself him himself his how
how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most
mustn't my myself no nor not of off on once one only or other ought our ours ourselves
out over own really right said same shan't she she'd she'll she's should shouldn't so
some such than that that's the their theirs them themselves then there there's these they
they'd they'll they're they've this those through to too under until up us very was
wasn't we we'd we'll we're we've were weren't what what's when when's where where's
which while who who's whom why why's will with won't would wouldn't you you'd you'll
you're you've your yours yourself yourselves also just like going gonna know think well
yeah yes actually going get gets got way things thing make much many even still also
want kind lot really much just like think going know would could well right sort
never okay look take give need come called tell maybe often feel find help done
might mean means always better best another first next last long every back around
nbsp didn doesn didn didn wasn weren hadn hasn isn aren couldn wouldn shouldn
work time different example little great three part book today something trying making
point good course important question number made talk person understand years
people come called start problem maybe often information feel long today
every something doesn back last point mean good find trying making done
might person understand help always better best means around world look give
take need come called tell maybe often feel long today little great three part
year years second life case idea five game break sheet forward effects
call used talking sure real hard must model system based high able
without everything getting looking fact saying build keep goes seen open
place means quite across whole already enough using given works says
comes less times four questions working hand terms type making play
sense line single left through talk number write read show level move
wrong makes create focus true same trying
""".split())

DOMAIN_TERMS = frozenset("""
valuation revenue profit margin equity debt capital asset liability cash flow
npv irr wacc dcf ebitda roi balance sheet income statement dividend bond stock
share market portfolio risk return investment strategy competitive advantage
moat pricing brand marketing customer acquisition retention churn funnel
segmentation positioning differentiation supply chain operations logistics
inventory capacity lean six sigma agile scrum leadership management team
culture innovation disruption entrepreneurship startup venture scaling
negotiation persuasion influence stakeholder governance compliance regulation
ethics corporate social responsibility merger acquisition restructuring
synergy due diligence integration economics micro macro gdp inflation monetary
fiscal policy trade globalization exchange rate geopolitics analytics data
statistics regression correlation hypothesis bayesian machine learning ai
digital transformation automation technology blockchain fintech communication
presentation executive presence board director ceo cfo coo strategy framework
porter five forces swot pestel value chain competitive dynamics game theory
nash equilibrium principal agent moral hazard adverse selection behavioral
decision heuristic bias prospect theory anchoring framing nudge systems
thinking complexity network effects platform two sided market switching cost
accounting accrual depreciation amortization goodwill impairment audit tax
budget variance cost allocation transfer pricing break even contribution
leverage beta capm arbitrage hedge option derivative futures forward swap
""".split())

def extract_wordcloud(flat):
    """Extract top words from all transcripts, return list of {word, size}."""
    freq = Counter()
    for _, _, vids, _, _ in flat:
        for v in vids:
            text = (v.get("transcript") or "").lower()
            words = re.findall(r"[a-z]{4,}", text)
            for w in words:
                if w not in STOP_WORDS:
                    freq[w] += 1
    # Score: domain terms get 5x boost; filter out low-signal words
    scored = {}
    for w, c in freq.items():
        if w in DOMAIN_TERMS:
            scored[w] = c * 5
        elif c > 300:
            scored[w] = c
    top = sorted(scored.items(), key=lambda x: -x[1])[:40]
    if not top:
        return []
    mx = top[0][1]
    return [{"w": w, "s": round(0.3 + 0.7 * c / mx, 2)} for w, c in top]

def extract_graph(flat, modules):
    """Build a knowledge graph: nodes = modules, edges = shared key terms."""
    mod_terms = {}
    for track, mid, vids, _, _ in flat:
        key = f"{track}-{mid}"
        text = " ".join((v.get("transcript") or "") for v in vids).lower()
        words = set(re.findall(r"[a-z]{3,}", text))
        mod_terms[key] = words & DOMAIN_TERMS

    nodes = []
    for track, mid, vids, _, _ in flat:
        key = f"{track}-{mid}"
        nodes.append({"id": key, "label": TITLES.get(mid, mid), "track": track})

    edges = []
    keys = list(mod_terms.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            shared = mod_terms[keys[i]] & mod_terms[keys[j]]
            if len(shared) >= 5:
                edges.append({"s": keys[i], "t": keys[j], "w": len(shared)})

    edges.sort(key=lambda e: -e["w"])
    edges = edges[:120]
    connected = set()
    for e in edges:
        connected.add(e["s"])
        connected.add(e["t"])
    nodes = [n for n in nodes if n["id"] in connected]
    return {"nodes": nodes, "edges": edges}

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

DESCRIPTIONS = {
    # --- Core ---
    "01-accounting": "Financial statements, balance sheets, income statements, cash flow — reading a 10-K like an analyst.",
    "02-corporate-finance": "Valuation frameworks, DCF, NPV, IRR, WACC, cost of capital, and how firms make financing decisions.",
    "03-micro-strategy": "Supply & demand, elasticity, market structures, pricing power, and the economics behind strategic choices.",
    "04-competitive-strategy": "Porter's Five Forces, competitive advantage, moats, positioning, and industry dynamics.",
    "05-marketing-brand": "Category design, positioning, brand strategy, customer segmentation, and go-to-market frameworks.",
    "06-operations": "Supply chain design, process optimization, lean principles, capacity planning, and Six Sigma fundamentals.",
    "07-data-analytics": "Statistical thinking, regression, Bayesian reasoning, decision analysis, and data-driven management.",
    "08-negotiation": "Distributive and integrative negotiation, BATNA, tactical empathy, and deal architecture.",
    "09-leadership-ob": "Organizational behavior, team dynamics, motivation theory, culture building, and adaptive leadership.",
    "10-entrepreneurship": "Startup formation, venture mechanics, product-market fit, funding, and scaling from zero to one.",
    "11-global-macro": "Country risk, exchange rates, trade policy, capital flows, and investing in emerging markets.",
    "12-capstone": "Integrative strategy: pulling together finance, operations, marketing, and leadership into a cohesive business view.",
    # --- Executive ---
    "E1-leading-at-scale": "Leading organizations past the founder stage — structure, delegation, alignment, and executive decision-making.",
    "E2-capital-allocation": "Where to deploy capital: buybacks, dividends, M&A, organic growth, and the Buffett/Thorndike playbook.",
    "E3-mergers-acquisitions": "Deal origination, due diligence, valuation in M&A, integration planning, and restructuring.",
    "E4-governance-board": "Board composition, fiduciary duties, shareholder activism, proxy fights, and corporate governance best practices.",
    "E5-transformation": "Leading large-scale organizational change — turnarounds, digital transformation, and managing resistance.",
    "E6-crisis-leadership": "Leading through crises: rapid decision-making, stakeholder communication, and organizational resilience.",
    "E7-exec-presence-comms": "Executive communication, public speaking, storytelling, and commanding a room with authority.",
    "E8-stakeholder-ir": "Investor relations, earnings calls, shareholder communication, and managing the capital markets narrative.",
    "E9-geopolitics-macro": "Geopolitical risk, global macro trends, trade wars, sanctions, and their impact on business strategy.",
    "E10-digital-ai": "Digital strategy, AI adoption, technology-driven transformation, and building tech-forward organizations.",
    "E11-operating-system": "Personal productivity systems, mental models, energy management, and building an executive routine.",
    "E12-culture-strategy": "Culture as competitive advantage — building, measuring, and evolving organizational culture intentionally.",
    # --- Canon ---
    "strategy": "Foundational strategy texts: Good Strategy/Bad Strategy, Playing to Win, and the art of strategic clarity.",
    "leadership-presence": "Leadership philosophy and executive presence from Sinek, Willink, and the great leadership thinkers.",
    "mental-models": "Thinking tools: Munger's latticework, Farnam Street models, and frameworks for better judgment.",
    "org-design-mechanisms": "How organizations actually work — incentives, structure, bureaucracy, and mechanism design.",
    "landscape-competitive": "Competitive analysis beyond Porter: Blue Ocean, disruption theory, and strategic positioning.",
    "negotiation-influence": "Influence, persuasion, and negotiation science from Cialdini, Voss, and behavioral research.",
    "execution-operations": "The Goal, Theory of Constraints, bottleneck thinking, and the art of operational execution.",
    "culture-change": "Leading change: Kotter's model, organizational transformation, and making culture shifts stick.",
    "risk-fragility": "Taleb's antifragility, Black Swans, risk management, and thriving under uncertainty.",
    "product-innovation": "Product thinking, innovation frameworks, design-driven development, and the innovator's dilemma.",
    "power-politics": "Organizational power, political dynamics, and the realist tradition from Greene and Pfeffer.",
    "personal-effectiveness": "Deep work, deliberate practice, time management, and the science of peak performance.",
    "financial-literacy": "Financial literacy for non-finance operators — reading statements, thinking about value, and capital decisions.",
    "behavioral-decision": "Kahneman, Thaler, and the psychology of decisions — biases, heuristics, and nudge architecture.",
    "game-theory": "Nash equilibrium, strategic interaction, mechanism design, and applying game theory to business.",
    "platform-strategy": "Network effects, platform economics, two-sided markets, and winner-take-all dynamics.",
    "systems-complexity": "Systems thinking, feedback loops, emergence, complexity theory, and unintended consequences.",
    "information-communication": "Information theory, crucial conversations, feedback systems, and communication as infrastructure.",
    "economics-incentives": "Incentive design, principal-agent problems, moral hazard, adverse selection, and market failures.",
    "history-judgment": "Historical case studies, pattern recognition, and developing judgment through studied experience.",
    "communication-storytelling": "Narrative structure, business storytelling, and communicating ideas that move people to action.",
    "design-problem-solving": "Design thinking, structured problem-solving, first-principles reasoning, and creative frameworks.",
    "ethics-judgment": "Business ethics, moral reasoning, stakeholder theory, and making defensible decisions under pressure.",
    # --- Technical Foundations ---
    "managerial-accounting": "Cost accounting, variance analysis, budgeting, transfer pricing, and internal decision support.",
    "statistics-quant": "Probability, distributions, hypothesis testing, regression, and quantitative methods for business.",
    "marketing-strategy": "Marketing frameworks, positioning strategy, segmentation, and competitive marketing analysis.",
    "information-systems": "Enterprise IT, database fundamentals, systems architecture, and technology management.",
    "business-law": "Contracts, torts, regulatory compliance, intellectual property, and the legal environment of business.",
    "entrepreneurial-finance": "Venture financing, term sheets, cap tables, startup valuation, and investor economics.",
}

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
    'flame': '<svg class="ic" viewBox="0 0 16 16" fill="currentColor"><path d="M8 1C6.5 3.5 4 5 4 8.5a4 4 0 008 0c0-1.5-.5-2.5-1.5-3.5-.5 1-1.5 1.5-2.5 1.5C8 5 8.5 3 8 1z"/></svg>',
    'star': '<svg class="ic" viewBox="0 0 16 16" fill="currentColor"><path d="M8 1l2.2 4.6L15 6.3l-3.5 3.5.8 4.8L8 12.3 3.7 14.6l.8-4.8L1 6.3l4.8-.7z"/></svg>',
    'trophy': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"><path d="M5 14h6M8 11v3M4 1h8v5a4 4 0 01-8 0V1z"/><path d="M4 3H2v2a2 2 0 002 2M12 3h2v2a2 2 0 01-2 2"/></svg>',
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
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
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
    if prevnext[0]:
        pn += f'<a class="pn" href="{prevnext[0][0]}"><span class="pn-dir">{IC["arrow-l"]} Previous</span><span class="pn-title">{esc(prevnext[0][1])}</span><span class="pn-key">←</span></a>'
    if prevnext[1]:
        pn += f'<a class="pn next" href="{prevnext[1][0]}"><span class="pn-dir">Next {IC["arrow-r"]}</span><span class="pn-title">{esc(prevnext[1][1])}</span><span class="pn-key">→</span></a>'
    done_btn = (f'<button id="mark-done" data-mod="{track}-{mid}.html"><span class="cp-tick">{IC["check"]}</span> '
                f'<span class="cp-on">Module complete</span><span class="cp-off">Mark module complete</span></button>') if lesson else ""
    track_name = {"exec": "Executive Track", "canon": "The Canon · Reading Layer",
                  "gaps": "Technical Foundations"}.get(track, "Core Curriculum")
    track_tab = {"exec": "#t-exec", "canon": "#t-canon", "gaps": "#t-gaps"}.get(track, "#t-core")
    desc = DESCRIPTIONS.get(mid, "")
    desc_html = f'<p class="mod-desc">{esc(desc)}</p>' if desc else ""
    return HEAD.format(title=f"{c} · {title}", css="style.css") + f"""
{'<div id="progress"></div>' if lesson else ''}
<header class="mod-header {('exec' if track=='exec' else 'core')}">
<nav class="breadcrumb">
<a href="index.html">Index</a><span class="sep">›</span>
<a href="index.html{track_tab}">{track_name}</a><span class="sep">›</span>
<span class="current">{esc(c)} {esc(title)}</span>
</nav>
<h1>{esc(title)}</h1>
{desc_html}
<div class="hairline"></div></header>
<nav class="toc">{" ".join(toc)}</nav>"""+f"""
<main>{"".join(sections)}</main>
<div class="done-wrap">{done_btn}</div>
<div class="toast" id="toast"></div>
<div class="pn-bar"><div class="pn-wrap">{pn}</div></div>
<a href="#" class="top">{IC['arrow-up']}</a>
<script src="chart.min.js"></script>
<script src="lesson.js?v={BUILD_VER}"></script>
<script>document.body.classList.add('mod-enter');</script>
</body></html>"""

def render_index(modules, stats, wc_data=None, graph_data=None, sources=None):
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
            desc = DESCRIPTIONS.get(mid, "")
            desc_html = f'<p class="mcard-desc">{esc(desc)}</p>' if desc else ""
            src = (sources or {}).get(mid, [])
            src_html = f'<p class="mcard-src">{", ".join(esc(s) for s in src)}</p>' if src else ""
            out.append(f"""<a class="mcard {('exec' if track=='exec' else 'core')}{' ready' if ready else ''}" href="{track}-{mid}.html" data-mod="{track}-{mid}" data-track="{track}">
<div class="mcard-num">{esc(c)}</div>
<div class="mcard-body">
<h3>{esc(title)}</h3>
{desc_html}{src_html}
<div class="mcard-drawer">
<div class="mcard-top">{lesson_tag}<span class="done-tick">{IC["check"]} done</span></div>
<div class="mstats">{"".join(f'<span>{m}</span>' for m in metas)}</div></div></div>
<span class="mcard-done-dot"></span>
<span class="mcard-arrow">{IC["arrow-r"]}</span></a>""")
        return "".join(out)

    def track_head(label, track, count_label, color="var(--core)"):
        r, t, pct = cov[track]
        ring = svg_progress_ring(pct, r=18, sw=3, color=color)
        return (f'<div class="track-head" data-collapse="{track}">'
                f'<span class="th-label">{label}</span><span class="th-rule"></span>'
                f'<span class="th-cov">{ring}<span class="th-cov-label">{r}/{t} lessons</span></span>'
                f'<span class="th-count">{count_label}</span>'
                f'<button class="th-toggle" aria-label="Collapse section">{IC["arrow-up"]}</button></div>')

    # Visual stats dashboard (data-target for animated counters)
    stats_viz = f"""<div class="stats-dash">
<div class="stat-card"><div class="stat-num" data-target="{stats['modules']}">0</div><div class="stat-label">modules</div></div>
<div class="stat-card"><div class="stat-num" data-target="{stats['videos']}">0</div><div class="stat-label">lectures</div></div>
<div class="stat-card"><div class="stat-num" data-target="{stats['words']}">0</div><div class="stat-label">words of transcript</div></div>
<div class="stat-card"><div class="stat-num" data-target="{total_lessons}">0</div><div class="stat-label">interactive lessons</div>
<div class="stat-bar-wrap"><div class="stat-bar-fill" style="width:0%" data-width="{overall_pct}"></div></div>
<div class="stat-sub">{overall_pct}% coverage</div></div>
</div>"""

    # Gamification bar
    gami_bar = f"""<div class="gami-bar">
<div class="xp-display">{IC['star']} <span class="xp-num" id="xp-count">0</span> <span class="xp-label">XP</span></div>
<div class="level-badge" id="level-badge">Analyst</div>
<div class="streak-display" id="streak-display">{IC['flame']} <span class="streak-num" id="streak-num">0</span> <span class="streak-label">day streak</span></div>
</div>"""

    return HEAD.format(title="The Compounding MBA", css="style.css") + f"""
<header class="hero">
<div class="eyebrow">Self-directed · Master's level</div>
<h1>The Compounding <em>MBA</em></h1>
<p class="sub">A master's-level business education, distilled from elite sources into interactive, visual lessons — grounded in primary data.</p>
{stats_viz}
{gami_bar}
<div class="exam-links">
<a class="exam-link" href="exam.html">{IC['pencil']} <span class="exam-title">Self-diagnostic</span> <span class="exam-sub">recall</span> {IC['arrow-r']}</a>
<a class="exam-link bench" href="benchmark-exam.html">{IC['target']} <span class="exam-title">Calibrated benchmark</span> <span class="exam-sub">exam-level</span> {IC['arrow-r']}</a>
</div>
<input id="q" placeholder="Search modules…" oninput="filt()">
<div class="filter-chips">
<button class="chip active" data-filter="all">All</button>
<button class="chip" data-filter="lesson">{IC['lesson']} Has lesson</button>
<button class="chip" data-filter="completed">{IC['check']} Completed</button>
<button class="chip" data-filter="not-started">Not started</button>
</div>
</header>
<nav class="track-tabs" id="track-tabs">
<a href="#t-core" class="tt active" data-track="core">Core</a>
<a href="#t-exec" class="tt" data-track="exec">Executive</a>
<a href="#t-canon" class="tt" data-track="canon">Canon</a>
<a href="#t-gaps" class="tt" data-track="gaps">Foundations</a>
<a href="#t-explore" class="tt" data-track="explore">Explore</a>
</nav>
<main>
<section id="t-core" class="track-section">
{track_head('Core Curriculum', 'core', '12 modules', 'var(--core)')}
<div class="grid">{cards('core')}</div>
</section>
<section id="t-exec" class="track-section">
{track_head('Executive Track', 'exec', '12 modules', 'var(--exec)')}
<div class="grid">{cards('exec')}</div>
</section>
<section id="t-canon" class="track-section">
{track_head('The Canon · Reading Layer', 'canon', '23 clusters', 'var(--brass)')}
<div class="grid">{cards('canon')}</div>
</section>
<section id="t-gaps" class="track-section">
{track_head('Technical Foundations', 'gaps', f'{len(modules["gaps"])} modules', 'var(--core)')}
<div class="grid">{cards('gaps')}</div>
</section>
<section id="t-explore" class="track-section">
<div class="track-head">
<span class="th-label">Explore</span><span class="th-rule"></span>
<span class="th-count">word cloud · knowledge graph</span></div>
<div class="explore-wrap">
<div class="explore-panel">
<h3 class="explore-title">{IC['chart']} Concept Cloud</h3>
<p class="explore-sub">Top terms from {stats['words']:,} words of transcript</p>
<canvas id="wc-canvas"></canvas>
</div>
<div class="explore-panel explore-panel-wide">
<h3 class="explore-title">{IC['target']} Knowledge Graph</h3>
<p class="explore-sub">Modules connected by shared domain concepts — drag to orbit</p>
<div id="kg-mount"></div>
<div class="kg-tooltip" id="kg-tip"></div>
</div>
</div>
</section>
</main>
<div class="toast" id="toast"></div>
<footer></footer>
<script>
function filt(){{var q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('.chip').forEach(function(c){{c.classList.remove('active');}});
document.querySelector('.chip[data-filter="all"]').classList.add('active');
document.querySelectorAll('.mcard').forEach(function(c){{
c.style.display = c.textContent.toLowerCase().includes(q) ? '' : 'none';}});}}
</script>
<script src="index.js?v=""" + BUILD_VER + """"></script>
<script>
var WC_DATA=""" + json.dumps(wc_data or []) + """;
var KG_DATA=""" + json.dumps(graph_data or {"nodes":[],"edges":[]}) + """;
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>
<script src="explore.js?v=""" + BUILD_VER + """"></script>
</body></html>"""

CSS = """
:root{
--bg:#faf7f2;--bg2:#f3efe8;--surface:#ffffff;--surface2:#f0ece5;
--line:#e2ddd4;--line2:#d0c9be;
--ink:#1c1917;--ink2:#3d3833;--dim:#8a837a;
--brass:#9a7b2e;--brass2:#7a6121;--core:#2d7a4a;--exec:#b86e1a;
--wrong:#c4372a;
--serif:'Lexend',system-ui,sans-serif;--read:'Lexend',system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,monospace;
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
.mcard-desc{font:.82rem/1.5 var(--read);color:var(--dim);margin:5px 0 0;letter-spacing:-.005em}
.mcard-src{font:500 .68rem/1 var(--mono);color:var(--brass);margin:6px 0 0;letter-spacing:.02em;text-transform:uppercase;opacity:.7}
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
.mod-header h1{font:300 clamp(2.6rem,6vw,4.2rem)/1 var(--serif);color:var(--ink);letter-spacing:-.02em;margin:.18em 0 .3em}
.mod-desc{font:.92rem/1.6 var(--read);color:var(--dim);margin:0 0 .5em;max-width:560px}
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
.tr-body{margin-top:14px;font:1.08rem/1.9 var(--read);color:var(--ink2);border-left:2px solid var(--brass);padding-left:22px;column-count:1}
@media(min-width:860px){.tr-body{column-count:2;column-gap:36px;column-rule:1px solid var(--line)}}
.tr-body p{margin:0 0 16px}.no-tr{margin-top:10px;color:var(--dim);font-style:italic;font-size:.92rem}
.excerpt{color:var(--ink2);font-size:1rem;margin:12px 0 0;opacity:.85}
.edgar{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:20px;margin:14px 0;font:.84rem/1.6 var(--mono);color:var(--ink2);white-space:pre-wrap}
.edgar h3{font:600 1.1rem var(--mono);color:var(--ink);margin:0 0 6px}.edgar h4{font:.95rem var(--mono);color:var(--brass);margin:16px 0 4px}
.empty{color:var(--dim);font-style:italic}
/* breadcrumb */
.breadcrumb{display:flex;align-items:center;gap:6px;font:500 .72rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dim);flex-wrap:wrap}
.breadcrumb a{color:var(--dim);text-decoration:none;transition:color .2s}.breadcrumb a:hover{color:var(--brass)}
.breadcrumb .sep{opacity:.4;font-size:.6rem}
.breadcrumb .current{color:var(--ink)}
/* prev/next bar — sticky bottom */
.pn-bar{position:sticky;bottom:0;z-index:15;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(12px);border-top:1px solid var(--line);margin-top:40px}
.pn-wrap{max-width:var(--wrap);margin:0 auto;padding:12px 24px;display:flex;justify-content:space-between;gap:14px;position:relative;z-index:2}
.pn{flex:1;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:14px 16px;text-decoration:none;color:var(--dim);transition:.2s;display:flex;flex-direction:column;gap:3px}
.pn-dir{font:600 .62rem var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--brass);display:flex;align-items:center;gap:4px}
.pn-dir .ic{width:.7em;height:.7em}
.pn-title{font:400 .88rem var(--read);color:var(--ink);line-height:1.3}
.pn.next{text-align:right;align-items:flex-end}
.pn:hover{border-color:var(--brass);box-shadow:0 2px 10px rgba(0,0,0,.06)}
.pn-key{font:.58rem var(--mono);color:var(--dim);opacity:.5;margin-top:2px}
@media(max-width:640px){.pn-wrap{flex-direction:column}.pn-key{display:none}}
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
figure.chart-wrap{margin:28px 0;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:20px 20px 14px}
figure.chart-wrap canvas{max-height:340px}
figure.chart-wrap figcaption{font:.86rem/1.5 var(--read);font-style:italic;color:var(--dim);margin-top:10px;text-align:center}
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
.fc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin:24px 0}
.fc{position:relative;display:block;background:none;border:0;padding:0;min-height:180px;cursor:pointer;font:inherit;text-align:left}
.fc-inner{display:block;position:relative;width:100%;height:100%;min-height:inherit}
.fc-f,.fc-b{position:absolute;inset:0;border:1px solid var(--line);border-radius:10px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;transition:opacity .3s cubic-bezier(0,0,.2,1),transform .3s cubic-bezier(0,0,.2,1)}
.fc-f{background:var(--surface);box-shadow:0 1px 3px rgba(0,0,0,.04)}
.fc:hover .fc-f{border-color:var(--brass);box-shadow:0 4px 14px rgba(0,0,0,.08)}
.fc-f b{font:400 1.28rem var(--serif);color:var(--ink)}
.fc-f .hint{font:.58rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass);white-space:nowrap;opacity:.7}
.fc-b{background:var(--core);color:#fff;font:.88rem/1.6 var(--read);justify-content:center;opacity:0;transform:scale(.97);pointer-events:none;border-color:var(--core);padding:22px 20px}
.fc.flipped .fc-f{opacity:0;transform:scale(.97)}
.fc.flipped .fc-b{opacity:1;transform:none}
@media(hover:hover){.fc:hover .fc-f{opacity:0;transform:scale(.97)}.fc:hover .fc-b{opacity:1;transform:none}}
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
/* ---------- STICKY TRACK TABS ---------- */
.track-tabs{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(12px);max-width:100%;padding:10px 24px;display:flex;gap:4px;border-bottom:1px solid var(--line);justify-content:center}
.tt{font:500 .72rem var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--dim);text-decoration:none;padding:8px 18px;border-radius:20px;transition:color .2s,background .2s;white-space:nowrap}
.tt:hover{color:var(--ink);background:var(--surface)}
.tt.active{color:var(--brass);background:color-mix(in srgb,var(--brass) 10%,transparent)}
.track-section{scroll-margin-top:60px}
.th-toggle{background:none;border:1px solid var(--line);border-radius:6px;padding:4px 8px;cursor:pointer;color:var(--dim);transition:.2s;display:flex;align-items:center;margin-left:8px}
.th-toggle:hover{color:var(--brass);border-color:var(--brass)}
.th-toggle .ic{transition:transform .25s cubic-bezier(0,0,.2,1)}
.track-section.collapsed .th-toggle .ic{transform:rotate(180deg)}
.track-section.collapsed .grid{display:none}
/* ---------- FILTER CHIPS ---------- */
.filter-chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px;animation:rise .8s .55s both}
.chip{font:500 .68rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dim);background:transparent;border:1px solid var(--line);border-radius:20px;padding:6px 14px;cursor:pointer;transition:.2s;display:inline-flex;align-items:center;gap:5px}
.chip .ic{width:.7em;height:.7em}
.chip:hover{border-color:var(--brass);color:var(--ink)}
.chip.active{background:var(--brass);color:#fff;border-color:var(--brass)}
/* ---------- GAMIFICATION ---------- */
.gami-bar{display:flex;align-items:center;gap:20px;margin:20px 0 8px;animation:rise .8s .42s both;flex-wrap:wrap}
.xp-display{display:flex;align-items:center;gap:6px;font:600 .78rem var(--mono);color:var(--brass);letter-spacing:.06em}
.xp-display .ic{width:1.1em;height:1.1em;color:var(--brass)}
.xp-num{font:700 1.3rem var(--serif);color:var(--brass)}
.xp-label{font:500 .64rem var(--mono);text-transform:uppercase;letter-spacing:.12em;color:var(--dim)}
.level-badge{font:600 .66rem var(--mono);letter-spacing:.1em;text-transform:uppercase;background:linear-gradient(135deg,var(--brass),var(--core));color:#fff;padding:5px 14px;border-radius:20px;white-space:nowrap}
.streak-display{display:flex;align-items:center;gap:5px;font:500 .72rem var(--mono);color:var(--exec);letter-spacing:.06em}
.streak-display .ic{width:1em;height:1em;color:var(--exec)}
.streak-num{font:700 1.1rem var(--serif)}
.streak-label{font:500 .64rem var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--dim)}
/* toast notification */
.toast{position:fixed;bottom:32px;left:50%;transform:translateX(-50%) translateY(80px);z-index:100;background:var(--core);color:#fff;font:500 .8rem var(--mono);letter-spacing:.06em;padding:14px 28px;border-radius:40px;box-shadow:0 8px 30px rgba(0,0,0,.18);opacity:0;transition:transform .5s cubic-bezier(.34,1.56,.64,1),opacity .4s;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast .xp-plus{margin-left:10px;font-weight:700;color:color-mix(in srgb,#fff 85%,var(--brass))}
/* --- Material motion: deceleration curve (0,0,.2,1) --- */
@keyframes card-enter{from{opacity:0;transform:translateY(16px) scale(.94)}to{opacity:1;transform:none}}
.mcard{opacity:0}.mcard.card-enter{animation:card-enter .35s cubic-bezier(0,0,.2,1) both}
/* container transform: card click */
@keyframes card-exit{to{transform:scale(1.04);opacity:0}}
.mcard.navigating{animation:card-exit .2s cubic-bezier(.4,0,1,1) forwards;pointer-events:none}
/* shared z-axis: module page entry */
@keyframes page-enter{from{opacity:0;transform:translateY(24px) scale(.95)}to{opacity:1;transform:none}}
body.mod-enter .mod-header,body.mod-enter main,body.mod-enter .pn-bar{animation:page-enter .4s cubic-bezier(0,0,.2,1) both}
body.mod-enter main{animation-delay:.08s}
body.mod-enter .pn-bar{animation-delay:.14s}
/* fade through: tab landing highlight */
@keyframes section-land{0%{background:color-mix(in srgb,var(--brass) 8%,transparent)}100%{background:transparent}}
.track-section.landing .track-head{animation:section-land .8s ease both}
/* completion visible at rest */
.mcard.completed{border-left:3px solid var(--core);background:color-mix(in srgb,var(--core) 4%,transparent)}
.mcard-done-dot{width:8px;height:8px;border-radius:50%;background:var(--core);position:absolute;top:12px;right:12px;opacity:0;transition:opacity .3s,box-shadow .3s}
.mcard.completed .mcard-done-dot{opacity:1}
@keyframes pulse-dot{0%,100%{box-shadow:0 0 0 0 color-mix(in srgb,var(--core) 40%,transparent)}50%{box-shadow:0 0 0 8px transparent}}
.mcard.just-completed .mcard-done-dot{animation:pulse-dot .8s ease 3}
/* stat counter glow */
@keyframes count-glow{0%{text-shadow:0 0 0 transparent}50%{text-shadow:0 0 14px color-mix(in srgb,var(--brass) 25%,transparent)}100%{text-shadow:0 0 0 transparent}}
.stat-num.counted{animation:count-glow .8s ease}
/* level-up bounce */
@keyframes level-pop{0%{transform:scale(1)}40%{transform:scale(1.18)}100%{transform:scale(1)}}
.level-badge.level-up{animation:level-pop .5s ease}
/* module done button celebration */
@keyframes check-bounce{0%{transform:scale(1)}30%{transform:scale(1.25)}60%{transform:scale(.9)}100%{transform:scale(1)}}
#mark-done.just-checked{animation:check-bounce .5s ease}
/* confetti burst */
@keyframes confetti-fall{0%{transform:translateY(0) rotate(0);opacity:1}100%{transform:translateY(100vh) rotate(720deg);opacity:0}}
.confetti{position:fixed;top:-10px;z-index:200;width:8px;height:8px;border-radius:2px;pointer-events:none;animation:confetti-fall 2.5s ease-in forwards}
/* ---------- EXPLORE: WORD CLOUD + KNOWLEDGE GRAPH ---------- */
.explore-wrap{display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:900px){.explore-wrap{grid-template-columns:1fr 1fr}}
.explore-panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:28px;position:relative;overflow:hidden;min-width:0;min-height:400px}
.explore-panel-wide{overflow:visible}
.explore-title{font:500 .82rem var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ink);margin:0 0 4px;display:flex;align-items:center;gap:8px}
.explore-title .ic{color:var(--brass)}
.explore-sub{font:.78rem var(--read);color:var(--dim);margin:0 0 20px}
#wc-canvas{width:100%;height:auto;display:block;border-radius:8px;min-height:320px}
#kg-mount{width:100%;aspect-ratio:4/3;border-radius:8px;overflow:hidden;cursor:grab;position:relative;min-height:360px}
@media(min-width:900px){#kg-mount{aspect-ratio:1/1}}
#kg-mount:active{cursor:grabbing}
#kg-mount canvas{display:block;width:100%!important;height:100%!important;border-radius:8px}
.kg-tooltip{position:absolute;z-index:10;background:var(--surface);border:1px solid var(--line2);border-radius:8px;padding:10px 14px;font:.82rem var(--read);color:var(--ink);pointer-events:none;opacity:0;transition:opacity .15s;box-shadow:0 4px 16px rgba(0,0,0,.1);max-width:240px;white-space:nowrap}
.kg-tooltip.show{opacity:1}
@media(min-width:760px){.explore-wrap{grid-template-columns:1fr 1.6fr}}
/* mobile fallback: show drawer on touch devices */
@media(hover:none){.mcard-drawer{max-height:120px;opacity:1}.mcard-arrow{opacity:.5;transform:none}}
@media(max-width:640px){.grid{grid-template-columns:1fr;gap:10px}.mcard-num{font-size:1.6rem;min-width:48px;padding-left:16px}.stats-dash{gap:10px}.stat-card{min-width:0;padding:16px}.gami-bar{gap:12px}.track-tabs{gap:2px;padding:8px 12px}.tt{padding:6px 12px;font-size:.65rem}.filter-chips{gap:6px}.chip{padding:5px 10px;font-size:.62rem}}
@media(max-width:480px){.track-tabs{overflow-x:auto;justify-content:flex-start;-webkit-overflow-scrolling:touch}.track-tabs::-webkit-scrollbar{display:none}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto}.mcard{opacity:1}}
"""

LESSON_JS = r"""
(function(){
  var bar=document.getElementById('progress');
  if(bar){addEventListener('scroll',function(){
    var h=document.documentElement,sc=h.scrollTop,mx=h.scrollHeight-h.clientHeight;
    bar.style.width=(mx>0?100*sc/mx:0)+'%';},{passive:true});}
  // keyboard nav: ← → for prev/next
  var prevLink=document.querySelector('.pn:not(.next)');
  var nextLink=document.querySelector('.pn.next');
  document.addEventListener('keydown',function(e){
    if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'||e.target.isContentEditable)return;
    if(e.key==='ArrowLeft'&&prevLink){prevLink.click();}
    if(e.key==='ArrowRight'&&nextLink){nextLink.click();}
  });
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
    done.addEventListener('click',function(){
      done.classList.toggle('checked');
      localStorage.setItem(key,done.classList.contains('checked')?'1':'0');
      if(done.classList.contains('checked')){
        done.classList.add('just-checked');
        setTimeout(function(){done.classList.remove('just-checked');},600);
        // update streak
        try{
          var today=new Date().toISOString().slice(0,10);
          var sk=JSON.parse(localStorage.getItem('mba-streak')||'{"d":0,"last":""}');
          var yesterday=new Date(Date.now()-864e5).toISOString().slice(0,10);
          if(sk.last!==today){
            sk.d=(sk.last===yesterday)?sk.d+1:1;
            sk.last=today;
            localStorage.setItem('mba-streak',JSON.stringify(sk));}
        }catch(e){}
        // toast
        var toast=document.getElementById('toast');
        if(toast){
          var track=(done.dataset.mod||'').split('-')[0];
          var xpVal={core:100,exec:120,canon:80,gaps:90}[track]||80;
          toast.innerHTML='Module complete! <span class="xp-plus">+'+xpVal+' XP</span>';
          toast.classList.add('show');
          setTimeout(function(){toast.classList.remove('show');},2800);
          // confetti burst
          for(var i=0;i<24;i++){
            var c=document.createElement('div');c.className='confetti';
            c.style.left=Math.random()*100+'vw';
            c.style.background=['#9a7b2e','#2d7a4a','#b86e1a','#c4372a','#4a90d9'][i%5];
            c.style.animationDelay=Math.random()*0.8+'s';
            c.style.animationDuration=(2+Math.random()*1.5)+'s';
            c.style.width=(6+Math.random()*6)+'px';
            c.style.height=(6+Math.random()*6)+'px';
            document.body.appendChild(c);
            setTimeout(function(el){el.remove();},(4000),c);}
        }
      }
    });}
  // ====== Chart.js auto-init ======
  if(typeof Chart!=='undefined'){
    var COLORS={brass:'#9a7b2e',core:'#84ad8a',exec:'#b86e1a',dim:'#7a7568',ink:'#2c2a25',
      line:'#d9d4cb',surface:'#f2ede6',red:'#cf6a5a',blue:'#4a90d9',teal:'#2d8a7a',
      purple:'#7a5fa0',orange:'#d4842a'};
    Chart.defaults.font.family="'Lexend',sans-serif";
    Chart.defaults.color=COLORS.dim;
    Chart.defaults.plugins.legend.labels.usePointStyle=true;
    Chart.defaults.plugins.legend.labels.boxWidth=8;
    Chart.defaults.elements.bar.borderRadius=4;
    Chart.defaults.elements.bar.borderSkipped=false;
    Chart.defaults.scale.grid={color:'rgba(0,0,0,.06)'};
    Chart.defaults.scale.border={display:false};
    function patchCallbacks(obj){
      if(!obj||typeof obj!=='object')return;
      Object.keys(obj).forEach(function(k){
        if(k==='callback'&&obj[k]==='PERCENT'){obj[k]=function(v){return v+'%'};}
        else if(k==='callback'&&obj[k]==='DOLLAR'){obj[k]=function(v){return '$'+v+'B'};}
        else if(k==='callback'&&obj[k]==='DOLLAR_PLAIN'){obj[k]=function(v){return '$'+v};}
        else if(k==='callback'&&obj[k]==='PLAIN'){obj[k]=function(v){return v.toLocaleString()};}
        else patchCallbacks(obj[k]);
      });
    }
    document.querySelectorAll('canvas[data-chart]').forEach(function(cvs){
      try{
        var cfg=JSON.parse(cvs.dataset.chart);
        patchCallbacks(cfg);
        if(!cfg.options)cfg.options={};
        if(cfg.options.animation===undefined){
          cfg.options.animation={duration:800,easing:'easeOutQuart'};
        }
        if(!cfg.options.plugins)cfg.options.plugins={};
        if(!cfg.options.plugins.tooltip)cfg.options.plugins.tooltip={};
        cfg.options.plugins.tooltip.backgroundColor='rgba(44,42,37,.92)';
        cfg.options.plugins.tooltip.cornerRadius=6;
        cfg.options.plugins.tooltip.padding=10;
        new Chart(cvs,cfg);
      }catch(e){console.warn('Chart init error:',e);}
    });
  }
})();
"""

INDEX_JS = r"""
(function(){
  // --- Completion state ---
  document.querySelectorAll('.mcard[data-mod]').forEach(function(c){
    if(localStorage.getItem('mba-done-'+c.dataset.mod+'.html')==='1')c.classList.add('completed');
  });

  // --- XP + Level system ---
  var XP={core:100,exec:120,canon:80,gaps:90};
  var LVL=[[0,'Analyst'],[300,'Associate'],[700,'Senior Associate'],[1200,'VP'],
    [2000,'Director'],[3000,'SVP'],[4200,'Managing Director'],[5000,'C-Suite']];
  function calcXP(){
    var xp=0;
    document.querySelectorAll('.mcard.completed').forEach(function(c){
      xp+=(XP[c.dataset.track]||80);});
    return xp;}
  function getLevel(xp){
    var lv=LVL[0];
    for(var i=0;i<LVL.length;i++){if(xp>=LVL[i][0])lv=LVL[i];}
    return lv;}
  var xp=calcXP(),lv=getLevel(xp);
  var xpEl=document.getElementById('xp-count');
  var lvlEl=document.getElementById('level-badge');
  if(xpEl){
    var cur=0,target=xp,dur=800,st=null;
    function stepXP(ts){
      if(!st)st=ts;var p=Math.min((ts-st)/dur,1);
      var e=1-Math.pow(1-p,3);
      xpEl.textContent=Math.floor(target*e);
      if(p<1)requestAnimationFrame(stepXP);}
    requestAnimationFrame(stepXP);}
  if(lvlEl)lvlEl.textContent=lv[1];

  // --- Streak ---
  try{
    var today=new Date().toISOString().slice(0,10);
    var sk=JSON.parse(localStorage.getItem('mba-streak')||'{"d":0,"last":""}');
    var sEl=document.getElementById('streak-num');
    if(sEl){
      var yesterday=new Date(Date.now()-864e5).toISOString().slice(0,10);
      if(sk.last===today)sEl.textContent=sk.d;
      else if(sk.last===yesterday)sEl.textContent=sk.d;
      else sEl.textContent=0;
    }
  }catch(e){}

  // --- Animated stat counters ---
  function animNum(el){
    var raw=el.dataset.target;if(!raw)return;
    var t=parseInt(raw.replace(/,/g,''),10);
    if(isNaN(t)){el.textContent=raw;return;}
    var dur=1400,st=null;
    function step(ts){
      if(!st)st=ts;var p=Math.min((ts-st)/dur,1);
      el.textContent=Math.floor(t*(1-Math.pow(1-p,3))).toLocaleString();
      if(p<1)requestAnimationFrame(step);
      else{el.textContent=t.toLocaleString();el.classList.add('counted');}
    }
    requestAnimationFrame(step);
  }
  var sObs=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){animNum(e.target);sObs.unobserve(e.target);}
    });},{threshold:0.3});
  document.querySelectorAll('.stat-num[data-target]').forEach(function(el){sObs.observe(el);});

  // --- Animate stat bar fill ---
  var barFill=document.querySelector('.stat-bar-fill[data-width]');
  if(barFill){
    var bObs=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          e.target.style.width=e.target.dataset.width+'%';
          bObs.unobserve(e.target);}
      });},{threshold:0.3});
    bObs.observe(barFill);}

  // --- Card entrance stagger (per-section, Material deceleration) ---
  var sections=document.querySelectorAll('.track-section');
  sections.forEach(function(sec){
    var idx=0;
    var obs=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          e.target.style.animationDelay=(idx%12)*0.04+'s';
          e.target.classList.add('card-enter');
          idx++;obs.unobserve(e.target);}
      });},{threshold:0.05,rootMargin:'40px'});
    sec.querySelectorAll('.mcard').forEach(function(c){obs.observe(c);});
  });

  // --- Container transform: card click animation ---
  document.querySelectorAll('.mcard[href]').forEach(function(c){
    c.addEventListener('click',function(e){
      e.preventDefault();
      try{sessionStorage.setItem('mba-scroll',window.scrollY);
        var active=document.querySelector('.tt.active');
        if(active)sessionStorage.setItem('mba-tab',active.getAttribute('data-track'));
      }catch(x){}
      c.classList.add('navigating');
      var href=c.getAttribute('href');
      setTimeout(function(){window.location.href=href;},180);
    });
  });

  // --- Scroll + tab restoration on return ---
  try{
    var savedScroll=sessionStorage.getItem('mba-scroll');
    if(savedScroll!==null){
      window.scrollTo(0,parseInt(savedScroll,10));
      sessionStorage.removeItem('mba-scroll');
      document.querySelectorAll('.mcard').forEach(function(c){c.style.animation='none';c.style.opacity='1';});
    }
    var savedTab=sessionStorage.getItem('mba-tab');
    if(savedTab){sessionStorage.removeItem('mba-tab');}
  }catch(x){}

  // --- Sticky tabs scroll spy ---
  var tabs=document.querySelectorAll('.tt');
  var secs=document.querySelectorAll('.track-section');
  if(tabs.length&&secs.length){
    var spy=function(){
      var pos=window.scrollY+140,act=0;
      secs.forEach(function(s,i){if(s.offsetTop<=pos)act=i;});
      tabs.forEach(function(t,i){t.classList.toggle('active',i===act);});};
    window.addEventListener('scroll',spy,{passive:true});
    tabs.forEach(function(t){
      t.addEventListener('click',function(e){
        e.preventDefault();
        var sec=document.querySelector(t.getAttribute('href'));
        if(sec){
          window.scrollTo({top:sec.offsetTop-60,behavior:'smooth'});
          sec.classList.remove('landing');
          void sec.offsetWidth;
          sec.classList.add('landing');
        }
      });
    });
  }

  // --- Filter chips ---
  document.querySelectorAll('.chip').forEach(function(chip){
    chip.addEventListener('click',function(){
      document.querySelectorAll('.chip').forEach(function(c){c.classList.remove('active');});
      chip.classList.add('active');
      var f=chip.dataset.filter;
      document.querySelectorAll('.mcard').forEach(function(c){
        var show=true;
        if(f==='lesson')show=c.classList.contains('ready');
        else if(f==='completed')show=c.classList.contains('completed');
        else if(f==='not-started')show=!c.classList.contains('completed');
        c.style.display=show?'':'none';
      });
      document.getElementById('q').value='';
    });
  });
  // --- Track section collapse/expand ---
  document.querySelectorAll('.th-toggle').forEach(function(btn){
    btn.addEventListener('click',function(e){
      e.preventDefault();
      var sec=btn.closest('.track-section');
      sec.classList.toggle('collapsed');
      var track=btn.closest('.track-head').dataset.collapse;
      if(track){
        try{
          var st=JSON.parse(localStorage.getItem('mba-collapsed')||'{}');
          st[track]=sec.classList.contains('collapsed');
          localStorage.setItem('mba-collapsed',JSON.stringify(st));
        }catch(e){}
      }
    });
  });
  try{
    var st=JSON.parse(localStorage.getItem('mba-collapsed')||'{}');
    Object.keys(st).forEach(function(track){
      if(st[track]){
        var head=document.querySelector('.track-head[data-collapse="'+track+'"]');
        if(head)head.closest('.track-section').classList.add('collapsed');
      }
    });
  }catch(e){}
})();
"""

EXPLORE_JS = r"""
(function(){
  var COLORS={core:[45,122,74],exec:[184,110,26],canon:[154,123,46],gaps:[122,97,33]};
  var BG=[250,247,242];

  // ====== WORD CLOUD — canvas spiral packing, 0° + 90° ======
  var wcCvs=document.getElementById('wc-canvas');
  if(wcCvs && typeof WC_DATA!=='undefined' && WC_DATA.length){
    var panel=wcCvs.parentElement;
    var pw=panel.clientWidth-56;
    var W=Math.max(pw,260),H=Math.round(W*1.1);
    var dpr=window.devicePixelRatio||1;
    wcCvs.width=W*dpr;wcCvs.height=H*dpr;
    wcCvs.style.width=W+'px';wcCvs.style.height=H+'px';
    var ctx=wcCvs.getContext('2d');
    ctx.scale(dpr,dpr);
    var placed=[];
    var sorted=WC_DATA.slice().sort(function(a,b){return b.s-a.s;});
    var ck=['core','exec','canon','gaps','core'];
    function colorFor(i){var c=COLORS[ck[i%5]]||COLORS.core;return 'rgb('+c[0]+','+c[1]+','+c[2]+')';}
    function measure(word,size,rot){
      ctx.font=(size>18?'600 ':'500 ')+size+'px Lexend,system-ui,sans-serif';
      var m=ctx.measureText(word);
      var tw=m.width+4,th=size*1.1+2;
      return rot?{w:th,h:tw,tw:tw,th:th}:{w:tw,h:th,tw:tw,th:th};
    }
    function overlaps(x,y,w,h){
      for(var i=0;i<placed.length;i++){
        var p=placed[i];
        if(x<p.x+p.w&&x+w>p.x&&y<p.y+p.h&&y+h>p.y)return true;
      }
      return false;
    }
    sorted.forEach(function(d,i){
      var size=Math.round(13+d.s*22);
      var rot=i>2&&Math.random()<0.3;
      var m=measure(d.w,size,rot);
      var cx=W/2,cy=H/2;
      var step=3,angle=0,r=0,found=false;
      for(var tries=0;tries<800;tries++){
        var px=cx+Math.cos(angle)*r-m.w/2;
        var py=cy+Math.sin(angle)*r-m.h/2;
        if(px>=0&&py>=0&&px+m.w<=W&&py+m.h<=H&&!overlaps(px,py,m.w,m.h)){
          placed.push({x:px,y:py,w:m.w,h:m.h,word:d.w,size:size,rot:rot,color:colorFor(i),s:d.s});
          found=true;break;
        }
        angle+=0.6;r+=step*0.12;
      }
    });
    function drawCloud(){
      ctx.clearRect(0,0,W,H);
      placed.forEach(function(p){
        ctx.save();
        ctx.font=((p.size>18?'600 ':'500 ')+p.size+'px Lexend,system-ui,sans-serif');
        ctx.fillStyle=p.color;
        ctx.globalAlpha=0.5+p.s*0.5;
        if(p.rot){
          ctx.translate(p.x+p.w/2,p.y+p.h/2);
          ctx.rotate(-Math.PI/2);
          ctx.textAlign='center';ctx.textBaseline='middle';
          ctx.fillText(p.word,0,0);
        }else{
          ctx.textAlign='left';ctx.textBaseline='top';
          ctx.fillText(p.word,p.x+2,p.y+1);
        }
        ctx.restore();
      });
    }
    var wcObs=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){drawCloud();wcObs.unobserve(e.target);}});
    },{threshold:0.1});
    wcObs.observe(wcCvs);
  }

  // ====== 3D KNOWLEDGE GRAPH (Three.js) ======
  var mount=document.getElementById('kg-mount');
  var tip=document.getElementById('kg-tip');
  if(!mount||typeof THREE==='undefined'||typeof KG_DATA==='undefined'||!KG_DATA.nodes.length)return;

  var rect=mount.getBoundingClientRect();
  var W3=Math.round(rect.width)||500,H3=Math.round(W3*10/16);
  var scene=new THREE.Scene();
  scene.background=new THREE.Color(BG[0]/255,BG[1]/255,BG[2]/255);
  var camera=new THREE.PerspectiveCamera(50,W3/H3,1,2000);
  camera.position.set(0,0,220);
  var renderer=new THREE.WebGLRenderer({antialias:true});
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(W3,H3);
  mount.appendChild(renderer.domElement);

  var ambient=new THREE.AmbientLight(0xffffff,0.6);
  scene.add(ambient);
  var dir=new THREE.DirectionalLight(0xffffff,0.8);
  dir.position.set(100,200,150);scene.add(dir);

  var tcHex={core:0x2d7a4a,exec:0xb86e1a,canon:0x9a7b2e,gaps:0x7a6121};
  var maxW=Math.max.apply(null,KG_DATA.edges.map(function(e){return e.w;}))||1;
  var nodeObjs=[],nodeMap={},edgeLines=[];

  KG_DATA.nodes.forEach(function(n,i){
    var phi=Math.acos(-1+2*i/KG_DATA.nodes.length);
    var theta=Math.sqrt(KG_DATA.nodes.length*Math.PI)*phi;
    var R=60+Math.random()*20;
    var geo=new THREE.SphereGeometry(2.5,16,12);
    var mat=new THREE.MeshPhongMaterial({color:tcHex[n.track]||0x8a837a,shininess:80});
    var mesh=new THREE.Mesh(geo,mat);
    mesh.position.set(R*Math.sin(phi)*Math.cos(theta),R*Math.sin(phi)*Math.sin(theta),R*Math.cos(phi));
    mesh.userData={id:n.id,label:n.label,track:n.track,vx:0,vy:0,vz:0};
    scene.add(mesh);
    nodeObjs.push(mesh);
    nodeMap[n.id]=mesh;
  });

  KG_DATA.edges.forEach(function(e){
    var s=nodeMap[e.s],t=nodeMap[e.t];
    if(!s||!t)return;
    var geo=new THREE.BufferGeometry().setFromPoints([s.position,t.position]);
    var op=0.06+0.14*(e.w/maxW);
    var mat=new THREE.LineBasicMaterial({color:0x9a7b2e,transparent:true,opacity:op});
    var line=new THREE.Line(geo,mat);
    line.userData={s:s,t:t,w:e.w,baseOp:op};
    scene.add(line);
    edgeLines.push(line);
  });

  // 3D force simulation
  function tick3D(){
    var damp=0.9,rep=800,k=0.006;
    for(var i=0;i<nodeObjs.length;i++){
      var n=nodeObjs[i],p=n.position,d=n.userData;
      d.vx-=p.x*0.0008;d.vy-=p.y*0.0008;d.vz-=p.z*0.0008;
      for(var j=i+1;j<nodeObjs.length;j++){
        var m=nodeObjs[j],q=m.position,md=m.userData;
        var dx=p.x-q.x,dy=p.y-q.y,dz=p.z-q.z;
        var d2=dx*dx+dy*dy+dz*dz+1;
        var f=rep/d2,dist=Math.sqrt(d2);
        var fx=dx/dist*f,fy=dy/dist*f,fz=dz/dist*f;
        d.vx+=fx;d.vy+=fy;d.vz+=fz;
        md.vx-=fx;md.vy-=fy;md.vz-=fz;
      }
    }
    for(var i=0;i<edgeLines.length;i++){
      var e=edgeLines[i],sp=e.userData.s.position,tp=e.userData.t.position;
      var dx=tp.x-sp.x,dy=tp.y-sp.y,dz=tp.z-sp.z;
      var dist=Math.sqrt(dx*dx+dy*dy+dz*dz)||1;
      var ideal=25+15*(1-e.userData.w/maxW);
      var f=(dist-ideal)*k;
      var fx=dx/dist*f,fy=dy/dist*f,fz=dz/dist*f;
      e.userData.s.userData.vx+=fx;e.userData.s.userData.vy+=fy;e.userData.s.userData.vz+=fz;
      e.userData.t.userData.vx-=fx;e.userData.t.userData.vy-=fy;e.userData.t.userData.vz-=fz;
    }
    for(var i=0;i<nodeObjs.length;i++){
      var n=nodeObjs[i],d=n.userData;
      d.vx*=damp;d.vy*=damp;d.vz*=damp;
      n.position.x+=d.vx;n.position.y+=d.vy;n.position.z+=d.vz;
    }
    edgeLines.forEach(function(line){
      var pts=[line.userData.s.position,line.userData.t.position];
      line.geometry.setFromPoints(pts);
    });
  }

  // Manual orbit controls
  var isDrag=false,prevX=0,prevY=0;
  var spherical={theta:0,phi:Math.PI/2,r:220};
  function updateCam(){
    camera.position.set(
      spherical.r*Math.sin(spherical.phi)*Math.cos(spherical.theta),
      spherical.r*Math.cos(spherical.phi),
      spherical.r*Math.sin(spherical.phi)*Math.sin(spherical.theta));
    camera.lookAt(0,0,0);
  }
  mount.addEventListener('pointerdown',function(e){isDrag=true;prevX=e.clientX;prevY=e.clientY;mount.setPointerCapture(e.pointerId);});
  mount.addEventListener('pointermove',function(e){
    if(!isDrag)return;
    spherical.theta-=(e.clientX-prevX)*0.008;
    spherical.phi=Math.max(0.1,Math.min(Math.PI-0.1,spherical.phi-(e.clientY-prevY)*0.008));
    prevX=e.clientX;prevY=e.clientY;
    updateCam();
  });
  mount.addEventListener('pointerup',function(){isDrag=false;});
  mount.addEventListener('wheel',function(e){
    e.preventDefault();
    spherical.r=Math.max(80,Math.min(500,spherical.r+e.deltaY*0.3));
    updateCam();
  },{passive:false});

  // Raycaster for hover
  var raycaster=new THREE.Raycaster();
  raycaster.params.Points={threshold:5};
  var mouse=new THREE.Vector2();
  var hovMesh=null;
  mount.addEventListener('mousemove',function(e){
    if(isDrag)return;
    var r=mount.getBoundingClientRect();
    mouse.x=((e.clientX-r.left)/r.width)*2-1;
    mouse.y=-((e.clientY-r.top)/r.height)*2+1;
    raycaster.setFromCamera(mouse,camera);
    var hits=raycaster.intersectObjects(nodeObjs);
    var newHov=hits.length?hits[0].object:null;
    if(newHov!==hovMesh){
      if(hovMesh)hovMesh.scale.set(1,1,1);
      hovMesh=newHov;
      if(hovMesh){
        hovMesh.scale.set(1.8,1.8,1.8);
        edgeLines.forEach(function(l){
          var conn=l.userData.s===hovMesh||l.userData.t===hovMesh;
          l.material.opacity=conn?0.6:0.03;
        });
        nodeObjs.forEach(function(n){
          if(n===hovMesh){n.material.emissive.setHex(0x333300);return;}
          var conn=false;
          edgeLines.forEach(function(l){if((l.userData.s===hovMesh&&l.userData.t===n)||(l.userData.t===hovMesh&&l.userData.s===n))conn=true;});
          n.material.opacity=conn?1:0.15;n.material.transparent=!conn&&n!==hovMesh;
        });
        if(tip){
          var conns=edgeLines.filter(function(l){return l.userData.s===hovMesh||l.userData.t===hovMesh;}).length;
          tip.innerHTML='<b>'+hovMesh.userData.label+'</b><br><span style="color:var(--dim);font-size:.72rem">'+conns+' connections · '+hovMesh.userData.track+'</span>';
          tip.classList.add('show');
          tip.style.left=(e.clientX-mount.getBoundingClientRect().left+14)+'px';
          tip.style.top=(e.clientY-mount.getBoundingClientRect().top-36)+'px';
        }
      }else{
        edgeLines.forEach(function(l){l.material.opacity=l.userData.baseOp;});
        nodeObjs.forEach(function(n){n.material.opacity=1;n.material.transparent=false;n.material.emissive.setHex(0);});
        if(tip)tip.classList.remove('show');
      }
    }
  });
  mount.addEventListener('click',function(){
    if(hovMesh)window.location.href=hovMesh.userData.id+'.html';
  });

  var simSteps=0,maxSim=200;
  function animate(){
    requestAnimationFrame(animate);
    if(simSteps<maxSim){tick3D();simSteps++;}
    renderer.render(scene,camera);
  }
  var kgObs=new IntersectionObserver(function(es){
    es.forEach(function(e){if(e.isIntersecting){animate();kgObs.unobserve(e.target);}});
  },{threshold:0.05});
  kgObs.observe(mount);
})();
"""

def main():
    raw = latest_raw()
    pull_date = os.path.basename(raw)
    manifest = json.load(open(os.path.join(INGEST, "manifest.json")))
    os.makedirs(DIST, exist_ok=True)
    open(os.path.join(DIST, "style.css"), "w").write(CSS)
    open(os.path.join(DIST, "lesson.js"), "w").write(LESSON_JS)
    open(os.path.join(DIST, "index.js"), "w").write(INDEX_JS)
    open(os.path.join(DIST, "explore.js"), "w").write(EXPLORE_JS)
    chart_src = os.path.join(ROOT, "site", "chart.min.js")
    if os.path.exists(chart_src):
        shutil.copy2(chart_src, os.path.join(DIST, "chart.min.js"))

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
    sources = {}
    for track, mid, v, _, _ in flat:
        ch = Counter(x.get("channel", "") for x in v if x.get("channel"))
        sources[mid] = [name for name, _ in ch.most_common(3)]

    wc_data = extract_wordcloud(flat)
    graph_data = extract_graph(flat, modules)
    print(f"  word cloud: {len(wc_data)} terms · knowledge graph: {len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges")
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(render_index(modules, stats, wc_data, graph_data, sources))
    # regenerate the diagnostic + calibrated-benchmark exams
    import subprocess
    subprocess.run(["python3", os.path.join(INGEST, "build_exam.py")], check=False)
    subprocess.run(["python3", os.path.join(INGEST, "build_benchmark.py")], check=False)
    print(f"Built site -> {DIST}")
    print(f"  {stats['modules']} module pages · {stats['videos']} lectures · {stats['words']:,} words · {stats['threads']} threads")
    print(f"  open: {os.path.join(DIST, 'index.html')}")

if __name__ == "__main__":
    main()
