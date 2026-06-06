# Note · Porter — *Competitive Strategy*

> Canon · Cluster: Strategy · Maps to **Course 04** (Competitive Strategy), **Course 12** (Capstone)

- **Source:** Michael Porter, *Competitive Strategy* (1980) + "What Is Strategy?" (HBR, 1996)
- **Core claim:** Industry **structure** determines profitability. Your job is to position where
  the forces are favorable — or to reshape them. Strategy is choosing a *distinct* position, not
  doing the same things better (that's operational effectiveness, which competes away).
- **Framework:**
  - **Five Forces:** new entrants · supplier power · buyer power · substitutes · rivalry.
  - **Generic strategies:** cost leadership · differentiation · focus. Being **"stuck in the
    middle"** (no clear position) is the worst outcome.
  - **Value chain:** decompose the business into activities; ask where you create *distinct* value
    vs. where you're a commodity.
- **Applies when:** assessing the attractiveness of an industry and finding a defensible position
  within it — the canonical first-pass on any market.
- **Breaks when:** Five Forces is a **static snapshot** of a stable industry — it underweights
  *dynamics*: disruption ([[canon-christensen-innovators-dilemma]]), strategic inflection points
  ([[canon-grove-only-the-paranoid-survive]]), and network/platform effects where the forces
  invert. It also names *that* you need advantage but is thin on *which kinds endure* — Helmer's
  taxonomy is the sharper tool there ([[canon-helmer-7-powers]]). And industry boundaries
  themselves blur, making "the industry" hard to scope.
- **Practitioner counterpoint:** *(researched 2026-06-05 — r/strategy + Lenny's Podcast transcripts corpus)*
  The corpus splits hard on Porter. Strategy theorists *defend* him: Roger Martin calls the "all
  about positioning" reading a **deliberate caricature** by jealous academics — *"they caricatured
  what he said, which he never did… he said it's all about finding a place that is structurally
  attractive"* — and still teaches the generic-strategy trade-off as bedrock: *"you have to be
  either differentiated or low cost, there's no way to protect yourself if you're not one of those
  two"* (Lenny's Podcast). **But the *operators* push back on the framework's altitude:** Richard
  Rumelt, who taught Five Forces for years, concluded *"this isn't strategy — these are analytical
  tools… for looking at competition, but they're [not] strategy"* (Lenny's Podcast). And r/strategy
  practitioners report the real failure isn't analysis at all: the top thread **"Most organizations
  don't need a new strategy" (45↑)** argues *"the strategy itself is fine… the real issues are
  people are not aligned… roles and ownership are unclear… meetings are full of updates, but short
  on decisions."* Five Forces structures the diagnosis; it doesn't move the org.
- **Researched layer** *(2026-06-05)*
  - **Canonical explanation (sourced):** Porter's enduring core is the generic-strategy choice —
    you must pick a *distinct* position, not be "stuck in the middle." Roger Martin restates it as
    the still-binding constraint: *"you have to be either differentiated or low cost, there's no way
    to protect yourself if you're not one of those two"* (Lenny's Podcast, Roger Martin). And the
    cost-leadership path carries Porter's structural caveat — *"it is rare that you can be the cost
    leader without having dominant scale in the territory in which you're operating."*
  - **Real application (mined):** Martin maps Porter onto the modern "where to play / how to win"
    cascade and onto moats — when the host frames it as *"castles with moats… is there a way you
    think about types of barriers,"* Martin points to Helmer's **Seven Powers** as the sharper
    taxonomy of *which* advantages endure — exactly the "thin on which kinds endure" gap this note
    flags. Concretely: Intuit's choice to extend "where to play" into small-business software
    *"and what came out of that… QuickBooks"* (ArtCenter, Roger Martin) is a Porter positioning
    move executed as a deliberate trade-off.
  - **Where the corpus pushes back on the book:** two critiques surface. (1) *Altitude* — Rumelt:
    Five Forces and the matrices are *"analytical tools… for looking at competition, but they're
    [not] strategy"* (Lenny's Podcast, Richard Rumelt); the framework diagnoses, it doesn't decide.
    (2) *Execution* — r/strategy's "Most organizations don't need a new strategy" (45↑) argues the
    binding constraint is usually **alignment and decision-making, not the positioning analysis**.
    A separate MBA-bound reader's thread still ranks **"Competitive Strategy by Michael Porter"**
    first among corporate-strategy reads (34↑), so the book's canon status holds — the corpus just
    insists it's a *starting structure*, not the strategy itself.
  - **Sources in corpus:** Lenny's Podcast — "5 essential questions to craft a winning strategy |
    Roger Martin" (youtube.com/watch?v=y7SN4FK8noY) · Lenny's Podcast — "Good Strategy, Bad Strategy
    | Richard Rumelt" (youtube.com/watch?v=4uWKEG0s9Kc) · ArtCenter College of Design — "Roger
    Martin on How Strategy Really Works" (youtube.com/watch?v=DDXn2Wry_HY) · r/strategy "Most
    organizations don't need a new strategy" (45↑) · r/strategy "Which of these books is good for
    corporate strategy?" (34↑) · r/strategy "Playing to Win: How Strategy Really Works (one
    paragraph review)" (102↑).
- **Links:** [[canon-helmer-7-powers]] · [[canon-christensen-innovators-dilemma]] ·
  [[canon-grove-only-the-paranoid-survive]] · [[canon-lafley-martin-playing-to-win]] ·
  [[04-strategy-five-forces]] · [[aapl-10k-fy2025]]

---
### Rep
Run Five Forces on a competitor using their real 10-K Item 1A risk factors
(`python3 _ingest/edgar.py filings <TICKER> --form 10-K`). Their disclosed risks *are* the forces.
