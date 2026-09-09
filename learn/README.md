# Learn — the beginner on-ramp

> For **someone who has not entered the domain.** This is the ground floor *below* the canon
> (`notes/canon`) and the course lessons (`lessons/`), which assume some footing. Here we teach from
> zero, and climb toward the case-method gym (`acumen/`) at the top.

## The teaching model — every unit carries four pillars
A beginner needs all four, in order. A unit isn't done until it has all four.

1. **Material** — *what* we're learning and *where* it comes from (the concept + the source).
2. **Understanding** — the idea in plain language, built on intuition and an everyday analogy — not
   raw text dumped on a novice.
3. **Example (real, EDGAR × event)** — the concept shown in a *real company's actual filing*,
   correlated to a *real, datable event*. This is the differentiator: a static textbook teaches with
   frozen hypotheticals; we teach with live, primary-sourced, event-correlated reality. **Historical**
   examples for hindsight; **real-time** (via the web) for current relevance.
4. **Application** — a small, graded exercise the beginner can actually do — building toward real
   decisions (and eventually the `acumen/` case method).

## Unit template rules (hardened by validation — see `VALIDATION.md`)
Every unit must:
1. **Define every term on first use** — a "Plain words first" block up top for any jargon (10-K, SEC,
   EDGAR, fiscal year, debt, leverage, equity, OCF, "booked," "B"=billion…). A novice knows none of it.
2. **Show every computation as a step**, not a result — decimal→% (×100), how a "swing" is measured,
   compute the ugly numbers (don't write "deeply negative").
3. **Keep the core Application code-free** — exercises a beginner can do with pen and paper; any
   `edgar.py` command is a clearly-labeled **optional** extra ("only if you have the project set up").
4. **Never test what wasn't taught** — assessment maps 1:1 to the unit's own objectives.

## The arc (how it climbs)
`learn/` (zero → literacy, this dir) → `lessons/` (taught course material) → `notes/canon`
(the framework library) → `acumen/` (the case method — make real calls, get red-teamed).

You earn your way up. You don't start at the Intel board memo; you start at "how does a company make
money," and the rungs build to it.

## Why EDGAR × events
EDGAR gives the *ground truth* (what the company actually reported); known events (historical or
pulled live from the web) give the *why*. Pairing them turns an abstract framework into something a
beginner can see happen to a real business. That bridge is the core of how we build *understanding*,
not just knowledge.

## The beginner sequence
Each unit is four-pillar and grounded in a real EDGAR × event example. The first arc (01–04) is
**financial literacy** — taught on one running case (Royal Caribbean through COVID) so it compounds.
Then we widen to growth, value, and the competitive landscape, which hands off to `lessons/` and
`notes/canon`, and finally to the `acumen/` case method.

**Arc A — Financial literacy (read any company):**
- [x] `unit-01-reading-the-scoreboard.md` — revenue, profit & margin (income statement). RCL × COVID.
- [x] `unit-02-cash-vs-profit.md` — why a profitable company can run out of cash (cash flow). RCL × COVID.
- [x] `unit-03-what-a-company-owns-and-owes.md` — the balance sheet & equity as shock absorber. RCL × COVID.
- [x] `unit-04-is-it-healthy.md` — the 3-minute health check (margin + cash + leverage), capstone. RCL × COVID.

**Arc B — Value & growth (what's a company worth):**
- [x] `unit-05-growth-and-returns.md` — why growth isn't always good. Peloton's COVID boom/bust.
- [x] `unit-06-whats-a-business-worth.md` — a company = its future cash, discounted to today.

**Arc C — The landscape (why some businesses are just better):**
- [x] `unit-07-the-landscape-moats.md` — moats / competitive advantage. Mastercard's durable margins vs cruise lines. Bridge to `notes/canon`.
- [x] `unit-09-capital-light-businesses.md` — capital-light / "royalty" businesses (pairs with 07). Domino's vs Texas Roadhouse: same industry, opposite capital model. From Ackman via `notes/media-practitioner-playbook` §3.
- [x] `unit-08-reading-the-words.md` — reading the 10-K's words (risk factors & MD&A) — qualitative literacy.

**Arc D — Your own balance sheet (personal finance):**
- [ ] `unit-10-personal-finance-operating-system.md` — turn the same investor lens on *yourself*: index funds, automation + 401k match, emergency fund, the 30×/4% targets, family-office-of-one cadence. From the Tiger Sisters PF-101 episode (`notes/tiger-sisters-insights`). **⚠ not yet run through `VALIDATION.md` flywheel** — arithmetic manually checked (all "Check yourself" answers correct), but beginner-clarity + objective-alignment gates pending.

**Then → climb the ladder:** `lessons/` (taught courses) → `notes/canon` (frameworks) → `acumen/`
(the case method: make real calls, get red-teamed).

> Arc A is built and self-contained — enough to open any public company and form a first opinion.
> 05–08 extend the same four-pillar, EDGAR×event template.
