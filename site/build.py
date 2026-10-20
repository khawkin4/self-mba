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
IC.update({
    'search': '<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14"/></svg>',
    'sun': '<svg class="ic ic-sun" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="8" cy="8" r="3"/><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M3.4 12.6l1.4-1.4M11.2 4.8l1.4-1.4"/></svg>',
    'moon': '<svg class="ic ic-moon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M13.5 10A6 6 0 016 2.5a6 6 0 107.5 7.5z"/></svg>',
})

# Global chrome: one sticky nav on every page (home, modules, library, exams).
SITE_NAV = f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-nav"><div class="sn-inner">
<a class="brand" href="index.html"><span class="brand-mark">C</span><span>The Compounding MBA</span></a>
<nav class="sn-links" aria-label="Site">
<a href="index.html#path" data-nav="path">Path</a>
<a href="index.html#t-library" data-nav="library">Library</a>
<a href="index.html#t-explore" data-nav="explore">Explore</a>
<a href="exam.html" data-nav="exam">Exams</a>
</nav>
<span class="sn-spacer"></span>
<button class="sn-search" id="open-search" type="button" aria-label="Search">{IC['search']}<span>Search</span><kbd>⌘K</kbd></button>
<button class="sn-theme" id="theme-toggle" type="button" aria-label="Toggle dark mode">{IC['sun']}{IC['moon']}</button>
</div></header>"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500'
         '&family=Lexend:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#faf7f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131210" media="(prefers-color-scheme: dark)">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%231c1917'/%3E%3Ctext x='16' y='22' text-anchor='middle' font-family='Georgia,serif' font-style='italic' font-size='19' fill='%23faf7f2'%3EC%3C/text%3E%3C/svg%3E">
<script>try{{var t=localStorage.getItem('mba-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
""" + FONTS + """
<link rel="stylesheet" href="{css}?v=""" + BUILD_VER + """"></head><body>
""" + SITE_NAV
FOOT = '<script src="site.js?v=' + BUILD_VER + '"></script></body></html>'

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

def slugify(text):
    t = re.sub(r"<[^>]+>", "", text)
    t = html.unescape(t).lower()
    t = re.sub(r"^\s*\d+[a-z]?\s*[·.:-]\s*", "", t)  # drop leading "3 · "
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60] or "section"

def anchor_headings(frag):
    """Give lesson <h2>s stable ids (deep links + search) without touching lessons/*.html."""
    seen = {}
    def sub(m):
        base = slugify(m.group(2)); n = seen.get(base, 0); seen[base] = n + 1
        sid = base if n == 0 else f"{base}-{n+1}"
        return f'<h2 id="{sid}"{m.group(1)}>{m.group(2)}</h2>'
    return re.sub(r"<h2((?:\s[^>]*)?)>(.*?)</h2>", sub, frag, flags=re.S)

def lesson_headings(frag):
    out, seen = [], {}
    for m in re.finditer(r"<h2(?:\s[^>]*)?>(.*?)</h2>", frag, flags=re.S):
        raw = m.group(1); base = slugify(raw); n = seen.get(base, 0); seen[base] = n + 1
        sid = base if n == 0 else f"{base}-{n+1}"
        txt = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
        txt = re.sub(r"^\s*\d+[a-z]?\s*[·]\s*", "", txt)
        if txt: out.append((txt, sid))
    return out

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
        sections.append(f'<section id="lesson" class="lesson">{anchor_headings(lesson)}</section>')
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
<div id="progress"></div>
<header class="mod-header {('exec' if track=='exec' else 'core')}">
<nav class="breadcrumb">
<a href="index.html">Home</a><span class="sep">›</span>
<a href="index.html{track_tab}">{track_name}</a><span class="sep">›</span>
<span class="current">{esc(c)} {esc(title)}</span>
</nav>
<h1>{esc(title)}</h1>
{desc_html}
<div class="hairline"></div></header>
<nav class="toc">{" ".join(toc)}</nav>"""+f"""
<main id="main">{"".join(sections)}</main>
<div class="done-wrap">{done_btn}</div>
<div class="toast" id="toast"></div>
<nav class="pn-bar" aria-label="Previous and next module"><div class="pn-wrap">{pn}</div></nav>
<a href="#" class="top">{IC['arrow-up']}</a>
<script src="chart.min.js"></script>
<script src="lesson.js?v={BUILD_VER}"></script>
<script>document.body.classList.add('mod-enter');</script>
""" + FOOT

def render_index(modules, stats, wc_data=None, graph_data=None, sources=None, library=None):
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

    def track_head(label, track, count_label, color="var(--core)", kicker=""):
        r, t, pct = cov[track]
        ring = svg_progress_ring(pct, r=16, sw=3, color=color)
        return (f'<div class="track-head" data-collapse="{track}">'
                f'<span class="th-label"><small>{esc(kicker)}</small>{label}</span><span class="th-rule"></span>'
                f'<span class="th-cov">{ring}<span class="th-cov-label">{r}/{t} lessons</span></span>'
                f'<span class="th-count">{count_label}</span>'
                f'<button class="th-toggle" aria-label="Collapse section">{IC["arrow-up"]}</button></div>')

    # ---- hero: compact numbers + progress card ----
    stats_viz = f"""<div class="stats-dash">
<div class="stat-card"><div class="stat-num" data-target="{stats['modules']}">0</div><div class="stat-label">modules</div></div>
<div class="stat-card"><div class="stat-num" data-target="{stats['videos']}">0</div><div class="stat-label">lectures</div></div>
<div class="stat-card"><div class="stat-num" data-target="{(library or {}).get('doc_count', 0)}">0</div><div class="stat-label">library docs</div></div>
<div class="stat-card"><div class="stat-num" data-target="{total_lessons}">0</div><div class="stat-label">interactive lessons</div>
<div class="stat-bar-wrap"><div class="stat-bar-fill" style="width:0%" data-width="{overall_pct}"></div></div>
<div class="stat-sub">{overall_pct}% coverage</div></div>
</div>"""
    progress_card = f"""<div class="progress-card">
<div class="gami-bar">
<div class="xp-display">{IC['star']} <span class="xp-num" id="xp-count">0</span> <span class="xp-label">XP</span></div>
<div class="level-badge" id="level-badge">Analyst</div>
<div class="streak-display" id="streak-display">{IC['flame']} <span class="streak-num" id="streak-num">0</span> <span class="streak-label">day streak</span></div>
</div>
<div class="exam-links">
<a class="exam-link" href="exam.html">{IC['pencil']} <span class="exam-title">Self-diagnostic</span> <span class="exam-sub">recall</span> {IC['arrow-r']}</a>
<a class="exam-link bench" href="benchmark-exam.html">{IC['target']} <span class="exam-title">Benchmark</span> <span class="exam-sub">exam-level</span> {IC['arrow-r']}</a>
</div></div>"""

    # ---- the path: five stages read as one program ----
    lib_by = {c['slug']: c for c in (library or {}).get('collections', [])}
    def stage(n, key, href, kicker, title, desc, meta, docs=None, track=None):
        data = f' data-track="{track}"' if track else ''
        if docs: data += f" data-docs='{json.dumps(docs)}'"
        return (f'<li class="stage" data-stage="{key}"{data}><a href="{href}">'
                f'<span class="stage-top"><span class="stage-kicker">{esc(kicker)}</span><span class="stage-n">{n}</span></span>'
                f'<b>{esc(title)}</b><p class="stage-desc">{esc(desc)}</p>'
                f'<span class="stage-meta"><span>{esc(meta)}</span><span class="stage-prog">Not started</span></span>'
                f'<span class="stage-bar"><i data-width="0"></i></span></a></li>')
    learn = lib_by.get('learn', {}); acumen = lib_by.get('acumen', {})
    stages = "".join([
        stage(0, 'learn', 'lib-learn.html', 'On-ramp', 'Zero to financial literacy',
              'Ten four-pillar units: concept, plain language, a real filing, an exercise.',
              f"{learn.get('count', 10)} units", docs=learn.get('hrefs')),
        stage(1, 'core', '#t-core', 'Core', 'The twelve-course curriculum',
              'Accounting to capstone — interactive lessons distilled from lectures and filings.',
              f"{cov['core'][1]} courses", track='core'),
        stage(2, 'exec', '#t-exec', 'Executive', 'Leading at scale',
              'Capital allocation, M&A, governance, crisis — the operator-to-executive turn.',
              f"{cov['exec'][1]} courses", track='exec'),
        stage(3, 'canon', '#t-canon', 'Canon', 'The reading layer',
              'Twenty-three book clusters, each with its core claim, framework and failure modes.',
              f"{cov['canon'][1]} clusters", track='canon'),
        stage(4, 'acumen', 'lib-acumen.html', 'Acumen Gym', 'Judgment under uncertainty',
              'Live cases, no answer key. Memos that get red-teamed, scored in a ledger.',
              f"{acumen.get('count', 0)} cases", docs=acumen.get('hrefs')),
    ])
    path_html = f"""<section id="path" class="path">
<div class="sec-head"><span class="kicker">The path</span><h2>Five stages, one program.</h2>
<p>Start wherever your foundation is. Lessons compound: each stage assumes the one before and feeds the next.</p></div>
<ol class="stages">{stages}</ol>
<div class="path-aside">
<a class="aside-card" href="#t-gaps"><span class="kicker">As needed</span><span><b>Technical Foundations</b> · {cov['gaps'][1]} prerequisite modules — cost accounting, statistics, law, venture finance.</span></a>
<a class="aside-card" href="#t-library"><span class="kicker">Alongside</span><span><b>Library</b> · {(library or {}).get('doc_count', 0)} documents: field notes, canon distillations, quant lab, glossary.</span></a>
</div></section>"""

    toolbar = f"""<div class="toolbar">
<input id="q" placeholder="Filter modules…" oninput="filt()" aria-label="Filter modules">
<div class="filter-chips">
<button class="chip active" data-filter="all">All</button>
<button class="chip" data-filter="lesson">{IC['lesson']} Has lesson</button>
<button class="chip" data-filter="completed">{IC['check']} Completed</button>
<button class="chip" data-filter="not-started">Not started</button>
</div></div>"""

    return HEAD.format(title="The Compounding MBA", css="style.css") + f"""
<header class="hero">
<div class="eyebrow">Self-directed · Master's level · Updated {max(stats['date'], (library or {}).get('latest',[{}])[0].get('updated',''))}</div>
<h1>The Compounding <em>MBA</em></h1>
<p class="sub">A master's-level business education distilled from elite sources into interactive lessons, a reading canon and a library of practitioner notes — grounded in primary data.</p>
<div class="hero-cta">
<a class="cta" id="hero-cta" href="doc-learn-unit-01-reading-the-scoreboard.html" data-start="doc-learn-unit-01-reading-the-scoreboard.html"><span class="cta-label" id="cta-label">Start the On-ramp</span><span class="cta-sub" id="cta-sub">Unit 01 · Reading the scoreboard · 15 min</span>{IC['arrow-r']}</a>
<a class="cta-alt" href="#path">See the whole path</a>
</div>
<div class="hero-grid">{stats_viz}{progress_card}</div>
</header>
<main id="main">
{path_html}
{toolbar}
<section id="t-core" class="track-section" data-track="core">
{track_head('Core Curriculum', 'core', '12 courses', 'var(--core)', 'Stage 1')}
<div class="grid">{cards('core')}</div>
</section>
<section id="t-exec" class="track-section" data-track="exec">
{track_head('Executive Track', 'exec', '12 courses', 'var(--exec)', 'Stage 2')}
<div class="grid">{cards('exec')}</div>
</section>
<section id="t-canon" class="track-section" data-track="canon">
{track_head('The Canon', 'canon', '23 clusters', 'var(--canon)', 'Stage 3 · Reading layer')}
<div class="grid trunc" data-show="8">{cards('canon')}</div>
<button class="show-all" type="button" data-for="t-canon">Show all {cov['canon'][1]} clusters {IC['arrow-up']}</button>
</section>
<section id="t-gaps" class="track-section" data-track="gaps">
{track_head('Technical Foundations', 'gaps', f'{len(modules["gaps"])} modules', 'var(--gaps)', 'Prerequisites · as needed')}
<div class="grid">{cards('gaps')}</div>
</section>
{library_html(library)}
<section id="t-explore" class="track-section" data-track="explore">
<div class="track-head">
<span class="th-label"><small>Map</small>Explore</span><span class="th-rule"></span>
<span class="th-count">concept cloud · knowledge graph</span></div>
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
<footer>Built from {stats['videos']} lectures · {stats['words']:,} transcript words · {stats['filings']} SEC filings · {(library or {}).get('doc_count', 0)} library documents. Press <kbd>⌘K</kbd> to search anything.</footer>
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
""" + FOOT

def library_html(lib):
    if not lib: return ""
    cards = "".join(f'''<a class="lcard" href="lib-{c['slug']}.html" data-coll="{c['slug']}">
<span class="lcard-kicker">{esc(c['kicker'])}</span><h3>{esc(c['label'])}</h3><p>{esc(c['desc'])}</p>
<span class="lcard-meta"><span class="lcard-read" data-docs='{json.dumps(c.get('hrefs', []))}'></span>{c['count']} docs · {c['words']:,} words · {c['updated']}</span></a>''' for c in lib["collections"])
    latest = "".join(f'''<li><a href="{d['href']}"><span class="lt-coll">{esc(d['coll'])}</span><span class="lt-title">{esc(d['title'])}</span><span class="lt-date">{d['updated']}</span></a></li>''' for d in lib["latest"])
    return f'''<section id="t-library" class="track-section" data-track="library">
<div class="track-head"><span class="th-label"><small>Alongside the path</small>Library</span><span class="th-rule"></span>
<span class="th-count">{lib['doc_count']} documents · {lib['doc_words']:,} words</span></div>
<div class="lib-grid">
<div class="lgrid">{cards}</div>
<div class="latest"><div class="latest-label">Latest additions</div><ol class="latest-list">{latest}</ol></div>
</div>
</section>'''


# Stylesheet lives in site/style.css (copied to dist by main()); shared runtime in site/site.js.
CSS = open(os.path.join(ROOT, "site", "style.css"), encoding="utf-8").read()
SITE_JS = open(os.path.join(ROOT, "site", "site.js"), encoding="utf-8").read()


LESSON_JS = r"""
(function(){
  // (reading-progress bar is driven by site.js)
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
    c.setAttribute('aria-pressed','false');
    c.addEventListener('click',function(){var on=c.classList.toggle('flipped');c.setAttribute('aria-pressed',on?'true':'false');});});
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
    try{var cs=getComputedStyle(document.documentElement);
      COLORS.dim=cs.getPropertyValue('--dim').trim()||COLORS.dim;
      COLORS.ink=cs.getPropertyValue('--ink').trim()||COLORS.ink;}catch(e){}
    Chart.defaults.font.family="'Lexend',sans-serif";
    Chart.defaults.color=COLORS.dim;
    Chart.defaults.plugins.legend.labels.usePointStyle=true;
    Chart.defaults.plugins.legend.labels.boxWidth=8;
    Chart.defaults.elements.bar.borderRadius=4;
    Chart.defaults.elements.bar.borderSkipped=false;
    Chart.defaults.scale.grid={color:(document.documentElement.getAttribute('data-theme')==='dark'||(!document.documentElement.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches))?'rgba(255,255,255,.08)':'rgba(0,0,0,.06)'};
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

  // --- Animate bar fills (hero coverage + path stage bars) ---
  var bObs=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){
        e.target.style.width=e.target.dataset.width+'%';
        bObs.unobserve(e.target);}
    });},{threshold:0.3});
  document.querySelectorAll('.stat-bar-fill[data-width],.stage-bar i[data-width]').forEach(function(el){bObs.observe(el);});

  // --- Hero CTA: first visit → start the On-ramp; returning → continue the last item ---
  try{
    var last=JSON.parse(localStorage.getItem('mba-last')||'null');
    var cta=document.getElementById('hero-cta');
    if(last&&last.h&&cta){
      cta.href=last.h;cta.classList.add('is-continue');
      document.getElementById('cta-label').textContent='Continue: '+last.t;
      document.getElementById('cta-sub').textContent=(last.c||'Where you left off');
    }
  }catch(e){}

  // --- Path stages: the reader's own progress (modules from mba-done-*, docs from mba-read-*) ---
  function isRead(h){try{return localStorage.getItem('mba-read-'+h)==='1';}catch(e){return false;}}
  document.querySelectorAll('.stage').forEach(function(st){
    var done=0,total=0;
    if(st.dataset.track){var cs=document.querySelectorAll('.mcard[data-track="'+st.dataset.track+'"]');total=cs.length;
      cs.forEach(function(c){if(c.classList.contains('completed'))done++;});}
    else if(st.dataset.docs){try{var docs=JSON.parse(st.dataset.docs);total=docs.length;done=docs.filter(isRead).length;}catch(e){}}
    var pct=total?Math.round(100*done/total):0;
    var lbl=st.querySelector('.stage-prog'),bar=st.querySelector('.stage-bar i');
    if(lbl)lbl.textContent=done===0?'Not started':(done===total?'Complete':done+'/'+total+' done');
    if(bar)bar.dataset.width=pct;
    st.classList.toggle('started',done>0);st.classList.toggle('complete',total>0&&done===total);
  });

  // --- Long sections collapsed behind "Show all" ---
  document.querySelectorAll('.show-all').forEach(function(btn){
    var grid=document.querySelector('#'+btn.dataset.for+' .grid');
    btn.addEventListener('click',function(){grid.classList.remove('trunc');btn.remove();});
  });
  function untrunc(){document.querySelectorAll('.grid.trunc').forEach(function(g){g.classList.remove('trunc');});document.querySelectorAll('.show-all').forEach(function(b){b.remove();});}
  var qEl=document.getElementById('q');if(qEl)qEl.addEventListener('input',untrunc,{once:true});
  document.querySelectorAll('.chip:not([data-filter="all"])').forEach(function(c){c.addEventListener('click',untrunc,{once:true});});

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
    var cst=JSON.parse(localStorage.getItem('mba-collapsed')||'{}');
    Object.keys(cst).forEach(function(track){
      if(cst[track]){
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
  // Panel background follows the theme (word cloud + graph render on var(--surface)).
  var BG=[255,255,255];
  try{var hex=getComputedStyle(document.documentElement).getPropertyValue('--surface').trim();
    if(/^#[0-9a-f]{6}$/i.test(hex))BG=[parseInt(hex.slice(1,3),16),parseInt(hex.slice(3,5),16),parseInt(hex.slice(5,7),16)];
    var isDark=BG[0]<128;
    if(isDark){COLORS={core:[93,185,129],exec:[221,143,63],canon:[207,167,82],gaps:[127,158,197]};}
  }catch(e){}

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
    open(os.path.join(DIST, "site.js"), "w").write(SITE_JS)
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

    import library as _library
    lib = _library.build(ROOT, DIST, HEAD, FOOT)
    # Global search index (⌘K): library docs + every module + the exams.
    track_label = {"core": "Core", "exec": "Executive", "canon": "Canon", "gaps": "Foundations"}
    search = [dict(t=TITLES.get(mid, mid), h=f"{track}-{mid}.html", c=track_label[track], k=code(track, mid))
              for track, mid, _, _, _ in flat]
    search += [dict(t="Self-diagnostic exam", h="exam.html", c="Exams", k=""),
               dict(t="Calibrated benchmark exam", h="benchmark-exam.html", c="Exams", k="")]
    for track, mid, _, _, _ in flat:
        frag = load_lesson(track, mid)
        if not frag: continue
        for txt, sid in lesson_headings(frag):
            search.append(dict(t=txt, h=f"{track}-{mid}.html#{sid}", c=track_label[track], k="", p=TITLES.get(mid, mid)))
    search += lib["search"]
    open(os.path.join(DIST, "search-index.json"), "w", encoding="utf-8").write(json.dumps(search, separators=(",", ":")))

    wc_data = extract_wordcloud(flat)
    graph_data = extract_graph(flat, modules)
    print(f"  word cloud: {len(wc_data)} terms · knowledge graph: {len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges")
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(render_index(modules, stats, wc_data, graph_data, sources, lib))
    # regenerate the diagnostic + calibrated-benchmark exams (they pick up the shared chrome)
    json.dump({"head": HEAD, "foot": FOOT}, open(os.path.join(DIST, "_chrome.json"), "w"))
    import subprocess
    subprocess.run(["python3", os.path.join(INGEST, "build_exam.py")], check=False)
    subprocess.run(["python3", os.path.join(INGEST, "build_benchmark.py")], check=False)
    print(f"Built site -> {DIST}")
    print(f"  {stats['modules']} module pages · {stats['videos']} lectures · {stats['words']:,} words · {stats['threads']} threads")
    print(f"  open: {os.path.join(DIST, 'index.html')}")

if __name__ == "__main__":
    main()
