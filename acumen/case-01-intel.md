# Case 01 — Intel (INTC): the capital-allocation crux

> **Status:** OPEN — awaiting your memo.
> **Rep type:** capital allocation + competitive strategy. No answer key — this is a genuinely
> contestable, live decision. Take a position.

## The brief
You're advising **Intel's board**. Intel is the company Andy Grove ran — and the one his own
*"only the paranoid survive"* warning now indicts: it missed mobile, missed the AI-accelerator wave,
ceded process leadership to TSMC, and has bet the company on a capital-hungry strategy to become a
leading-edge **foundry** (manufacturing chips for others), pouring tens of billions into fabs while
its core CPU franchise erodes and free cash flow is under pressure.

**The decision:** Over the next 3 years, what should Intel do with its capital — **commit to the
foundry/IDM bet, or retreat toward a lighter (fabless-leaning) model** — and **what is the single
thing that, if wrong, sinks your plan?**

This is a real capital-allocation call: the "CEO's #1 job" (Thorndike, *The Outsiders*; Bezos on
reversible vs. one-way doors). It forces diagnosis (the crux), a position with conviction, real
numbers, a landscape read, and the bear case.

## Pull the real data (don't use my framing as fact — verify)
```
python3 _ingest/edgar.py company INTC          # overview + recent filings + key financials
python3 _ingest/edgar.py filings INTC --form 10-K   # the actual 10-K (read Item 1A risk factors + MD&A)
python3 _ingest/edgar.py facts INTC            # XBRL fundamentals (capex, FCF, cash, debt, margins)
```
Anchor every claim to a real figure: capex vs. operating cash flow, cash & debt, gross-margin trend,
segment mix. Compare against the competitive reality (TSMC's process lead, Nvidia's accelerator
dominance, AMD on TSMC).

## Canon to bring to bear (the shelf behind the call)
`canon-grove-only-the-paranoid-survive` (strategic inflection point) · `canon-christensen-innovators-dilemma`
(disruption) · `canon-helmer-7-powers` (is there still a moat? which one?) · `canon-rumelt-the-crux`
(name the one pivotal solvable challenge) · `canon-bezos-shareholder-letters` (one-way vs two-way door) ·
`canon-klarman-margin-of-safety` (don't bet so big one surprise is fatal).

## Your deliverable — paste it under the line below
A **1-page board memo** to the spec in `README.md`:
1. **Recommendation (BLUF)** — the call, one sentence.
2. **The crux** — the pivotal, solvable challenge it all turns on.
3. **Why — three reasons**, each with a real figure from the filings.
4. **The fatal risk + mitigation** — the one thing that sinks it.
5. **The ask** — what you want the board to approve.

Take a side. "It depends" is a fail. When you've written it, paste it below and I red-team it.

---
## YOUR MEMO
*(paste here)*

---
## RED-TEAM (mine, after you submit)
*(scores on the 6-dimension rubric + the bear case + the boardroom question that sinks you)*
