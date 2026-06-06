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
- **Practitioner counterpoint:** (fill via `research` → r/strategy, r/consulting) — consultants
  use Five Forces constantly but warn it's a *structuring* device, not an answer; the insight is
  in scoping the industry correctly.
- **Links:** [[canon-helmer-7-powers]] · [[canon-christensen-innovators-dilemma]] ·
  [[canon-grove-only-the-paranoid-survive]] · [[canon-lafley-martin-playing-to-win]] ·
  [[04-strategy-five-forces]] · [[aapl-10k-fy2025]]

---
### Rep
Run Five Forces on a competitor using their real 10-K Item 1A risk factors
(`python3 _ingest/edgar.py filings <TICKER> --form 10-K`). Their disclosed risks *are* the forces.
