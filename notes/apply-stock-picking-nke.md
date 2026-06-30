# Apply · Stock-Picking Framework → NIKE (NKE)

> **An "Apply" rep, not investment advice.** This runs Imran Khan's framework ([[tiger-sisters-stock-picking]]) end-to-end on a real company, using primary SEC data pulled via `_ingest/edgar.py` (CIK 320187) on 2026-06-29. All financials are from Nike's XBRL company-facts and 10-K filings; the only non-SEC input is the live share price, which the SEC doesn't carry — flagged **[verify]** wherever it appears. The point is the *process*, and to prove the framework produces a defensible verdict. Maps to Course 02. Pairs with [[unit-06-whats-a-business-worth]].

## Why NKE for the rep
A genuine "is it **cheap** or is it **broken**?" case — exactly the setup Khan says is the only interesting one. Nike is a blue-chip brand trading far below its 2021 highs after a self-inflicted strategy error, a broad sales decline, and a CEO change. Consensus is split between "iconic brand on sale" and "structurally impaired." Perfect for the framework.

---

## Step 1 — Do I understand the business? (circle of competence)
Yes, well enough. Nike designs and markets footwear/apparel; it **outsources manufacturing** (mostly Vietnam, Indonesia, China) and sells through two channels: **wholesale** (Foot Locker, Dick's, etc.) and **NIKE Direct** (own stores + Nike.com / SNKRS app). The economics are brand + design + distribution, not factories. The value driver is **pricing power from brand heat**, and the swing factor is **product innovation cadence** plus **channel strategy**. Understandable → proceed.

## Step 2 — Read the primary documents (10-K / 10-Q via EDGAR)
Pulled FY2025 10-K (filed 2025-07-17, FY end 2025-05-31) and FY2024 10-K (filed 2024-07-25). The verifiable empirical picture (XBRL, $B):

| Metric (FY end May 31) | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|--:|--:|--:|--:|--:|
| Revenue | 44.54 | 46.71 | 51.22 | **51.36** | 46.31 |
| Gross profit | 19.96 | 21.48 | 22.29 | 22.89 | 19.79 |
| Net income | 5.73 | 6.05 | 5.07 | 5.70 | **3.22** |
| Operating cash flow | 6.66 | 5.19 | 5.84 | 7.43 | **3.70** |
| Diluted EPS ($) | 3.56 | 3.75 | 3.23 | 3.73 | **2.16** |
| Gross margin | 44.8% | 46.0% | 43.5% | 44.6% | **42.7%** |
| Net margin | 12.9% | 12.9% | 9.9% | 11.1% | **7.0%** |
| EBIT margin (10-K) | 14.7% | — | 12.1% | 12.7% | **8.2%** |
| Dividend / share ($) | — | — | 1.325 | 1.45 | **1.57** |

What the documents actually say (MD&A): revenue **−10% (−9% currency-neutral)** in FY25, down across **every geography** (North America, EMEA, Greater China) and most product lines (Men's, Jordan, Women's, Kids'); **NIKE Direct −13%**, wholesale −7%; footwear −12%. This is a **broad-based decline, not one bad region** — the most important single fact in the filing.

## Step 3 — Be curious; ask "why" (×N)
- **Why did revenue fall off the FY24 peak?** Largely self-inflicted: the prior strategy over-rotated to **DTC** and pulled back from wholesale accounts, ceding shelf space; plus a thin **innovation pipeline** (over-milking retro franchises — Air Force 1, Dunk — while On, Hoka, New Balance took share).
- **Why did net income fall *twice as fast* as revenue** ($5.70B→$3.22B, −44% vs revenue −10%)? **Operating deleverage + margin compression**: gross margin −190bps (markdowns/discounting to clear inventory, channel mix) on a shrinking top line. Earnings are far more cyclical than sales here.
- **Why did operating cash flow halve?** Working-capital unwind + lower earnings. Watch whether it rebounds as inventory normalizes.
- **Why is the dividend *up* while earnings collapsed?** Payout ratio jumped to **1.57 / 2.16 ≈ 73%** (from ~39% in FY24). Nike is defending its dividend-growth streak through the trough — a signal of management confidence *or* of a streak being protected past the point of comfort. Either way, less cushion.

## Step 4 — Stress-test the consensus (the fear, and is it right?)
**The embedded fear:** Nike has lost its innovation edge and brand heat permanently; competitors have structurally taken share; FY25 is the new normal, not a trough.

Is the consensus right or wrong? **Partly right** — the decline is real, broad, and self-inflicted, and the recovery is **unproven**. But the bear case requires believing the damage is *permanent*, and there are concrete reasons it may be cyclical/fixable:
- **A specific, reversible cause** (the DTC-over-rotation + wholesale retreat) with a **named fix already underway**: CEO **Elliott Hill** returned Oct 2024 (a 30-year Nike veteran) explicitly to **re-engage wholesale** and **refocus on sport/innovation**.
- The brand, scale, and distribution moat is intact; this isn't a balance-sheet or demand-destruction story.

Khan's discipline applies here: **don't be contrarian for its own sake.** "Consensus can be right for 1–4 years." Even if the thesis is right, the turnaround could take multiple years and another guide-down first. **Contrarian with the right timing** — being early is indistinguishable from being wrong.

## Step 5 — Trust factor (does it drive/erode the multiple?)
- **Trust intact on the balance sheet / governance** — clean disclosure, no accounting red flags, investment-grade, dividend maintained.
- **Trust dented on execution** — the prior strategy *was* the error, so management credibility took a real hit; the bull case rests on a **new (returning) CEO's unproven turnaround**.
- **Filing-language diff (FY25 vs FY24 10-K, Item 1A risk factors):** risk-factor language is **largely stable** — Nike did *not* add dramatic new risk factors; modal usage drifted only slightly toward hedging (**"may" 63→67, "will" 17→14**). The substantive change is in **MD&A candor**: FY25 lays the across-the-board decline bare and **dropped the "wholesale equivalent revenues" non-GAAP metric** (tied to an ERP rollout). Reading that two ways: (a) cleaner reporting, or (b) quietly retiring a flattering metric mid-decline. *(Caveat: my section extraction is a heuristic on the cleaned HTML; treat the modal counts as directional, not exact.)*

## Step 6 — Valuation LAST (what's priced in?)
Verifiable inputs: FY25 diluted EPS **$2.16** (trough); 5-yr "normalized" EPS ~**$3.2–3.7**; ~**1.49B** diluted shares (back-solved from $3.22B NI ÷ $2.16).

The framing, not a price target: at any given share price **P [verify current]**, the market is choosing which earnings base to capitalize:
- On **trough** EPS ($2.16), a given P looks like a high P/E → market is paying *up* for a recovery it believes is coming.
- On **normalized** EPS (~$3.5), the same P is a much lower multiple → market is treating FY25 as temporary.

So **"is it cheap?" is really "which earnings number is real?"** That's the whole debate restated as a valuation question — exactly Khan's point that **valuation measures how much of the recovery is already priced in.** If P implies the market already expects a full snap-back to ~$3.7 EPS, the risk/reward is poor (good news priced in, "any mistake gets hit hard"). If P implies the market is capitalizing near-trough earnings, the margin of safety is real ([[canon-klarman-margin-of-safety]]). **Action item to finish the rep: pull today's price, divide by both $2.16 and ~$3.5, and see which world you're being asked to buy.**

## Step 7 — Verdict + sizing
**Verdict: a "show-me" turnaround, not a screaming buy — and explicitly *not* a value trap on the evidence.** The fear is partly true (real, broad, self-inflicted decline) but the cause is **identifiable and being addressed**, the moat is intact, and FY25 reads as an **earnings trough** rather than structural impairment. That's a *fixable* discount, which is the good kind — but the fix is unproven and could take years.
- **Disqualifier to respect:** if you can't get comfortable that the innovation pipeline is genuinely reloading (not just retro re-runs) and that wholesale re-entry is regaining shelf space, it's a pass — those are the load-bearing assumptions.
- **Sizing (Khan's rule):** this is a multi-year, lumpy, headline-driven name → only sizeable if your **horizon is 3–5+ years and your pain tolerance** can stomach another guide-down. Size to *your* parameters, not anyone's tip.

### How I'd know I'm wrong (the disconfirming checklist)
1. **Gross margin keeps falling** below ~42% (says it's pricing power loss, not transient markdowns).
2. **NIKE Direct *and* wholesale both still shrinking** 2+ more quarters (turnaround not landing).
3. **Greater China keeps deteriorating** (structural, not cyclical).
4. **Dividend frozen or payout >100%** of earnings (confidence signal flips).
5. **New product cycles fail to move the share trend** (the brand-heat thesis breaks).

---

## What this rep exercised (and its limits)
- **Closed the README loop:** research framework → `edgar.py` real data → produced output. First live use of the EDGAR engine for an analysis.
- **Real, reproducible:** every number above is from SEC XBRL / 10-Ks; rerun `python3 _ingest/edgar.py company NKE` and `facts NKE` to refresh.
- **Limits:** no live price (do Step 6's division yourself); risk-factor diff is heuristic; this is an educational rep, **not advice**; I did not model FCF or a DCF (next rep could, using [[unit-06-whats-a-business-worth]]).

## Cross-links
- [[tiger-sisters-stock-picking]] — the framework being applied.
- [[unit-06-whats-a-business-worth]] — valuation-as-what's-priced-in; natural home for a follow-up DCF rep.
- [[canon-klarman-margin-of-safety]] — "cheap for a reason" vs. genuine margin of safety; the value-trap test.
- [[canon-mauboussin-success-equation]] — separating skill (fixable strategy error) from luck (cycle/FX); expectations vs. fundamentals.
- [[canon-kahneman-thinking-fast-and-slow]] — guarding against the halo (great brand ⇒ must-be-fine) and recency (trough ⇒ permanent) biases.
