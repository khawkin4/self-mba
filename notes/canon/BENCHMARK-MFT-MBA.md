# Coverage Benchmark — The Compounding MBA vs. a standardized MBA blueprint

> **What this is:** an honest scorecard of whether this self-MBA *covers the content domains an
> accredited MBA is expected to* — benchmarked against the **ETS Major Field Test in MBA (MFT-MBA)**
> and the **Common Professional Component (CPC)** used by ACBSP/IACBE accreditation. Both test the
> same ~12 domains; they are the closest thing to a standardized "MBA knowledge" benchmark.
>
> **What this is NOT:** a measure of *your* mastery (that needs a scored exam — see "Next" below),
> and not exact exam weights (ETS doesn't publish precise percentages; emphasis bands below are
> directional). Built 2026-06-06 from an empirical keyword probe of the 82 canon notes + 33 lessons
> + curriculum.

## Scorecard

Legend: ✅ Covered at depth · 🟡 Partial (present but light or one-sided) · 🔴 Gap

| # | MFT-MBA / CPC domain | Exam emphasis | Verdict | Where it's covered | The gap |
|---|---|---|---|---|---|
| 1 | **Strategy / Strategic Integration** | High | ✅✅ | Canon: Strategy, Landscape & Competitive, Game Theory, Design-Thinking clusters · Courses 04, 11, 12 · all 12 Exec modules. *(67 files)* | If anything **over-indexed** — this is the spine of the whole build. |
| 2 | **Management, OB, Leadership & HR** | High | ✅ | Canon: Leadership & Presence, Org Design, Culture & Change, Power & Politics, Personal Effectiveness · Courses 09, E1/E5/E12. *(70 files)* | **HR mechanics** (comp design, recruiting, perf-management systems) are lighter than the leadership canon. |
| 3 | **Operations / Supply Chain** | Med | ✅ | Canon: Execution & Operations (Goldratt, Ohno, 4DX), Systems & Complexity (Sterman bullwhip) · Course 06. *(65 files)* | Quantitative ops (inventory models, queuing, linear programming) is conceptual, not computational. |
| 4 | **Economics (Micro + Macro)** | Med | ✅ | Canon: Economics & Incentive Design (Mankiw, Akerlof, agency, lemons), Game Theory · Courses 03, 11, E9. *(23 files)* | **Micro strong; macro** (monetary/fiscal policy mechanics, IS-LM) lighter. |
| 5 | **Finance** | High | ✅ | Course 02 (DCF/WACC/NPV), E2 capital allocation, E3 M&A · Canon: Klarman, Mauboussin · **live EDGAR data**. *(10 files)* | Canon finance books are few (2); depth rests on the Damodaran-style course layer + data, not the canon. |
| 6 | **Communication & Integration (capstone)** | Med | ✅ | Canon: Communication & Storytelling (Minto, Duarte, Sinek), Information & Communication (Shannon, Tufte, Difficult/Crucial Conversations) · Course E7 · Course 12 capstone. | Solid. |
| 7 | **Marketing** | High | ✅ *(closed 6-06)* | **`gaps-marketing-strategy` lesson** (April Dunford positioning, Byron Sharp's laws of growth, STP, CAC/LTV unit economics) · Course 05 · Canon persuasion (Cialdini, Sinek). | Was 🟡 — persuasion ≠ marketing strategy. Now has a dedicated STP/positioning/unit-economics lesson. |
| 8 | **Quantitative Analysis & Statistics** | High | ✅ *(closed 6-06)* | **`gaps-statistics-quant` lesson** (StatQuest-style regression, hypothesis testing, p-values, confidence intervals) · Course 07 · decision-science canon (Kahneman, Tetlock, Taleb). | Was 🟡 — could reason about uncertainty, not compute it. Now teaches the actual methods. |
| 9 | **Accounting (Financial + Managerial)** | High | ✅ *(closed 6-06)* | **Financial**: Course 01 + AAPL 10-K + EDGAR. **Managerial**: new **`gaps-managerial-accounting` lesson** (CVP/break-even, contribution margin, ABC, variance analysis). | Was 🟡 — managerial accounting was a 0-coverage hole; now taught. |
| 10 | **Legal & Ethical Environment** | Med | ✅ *(closed 6-06)* | **Ethics**: Badaracco, Sandel · Governance E4. **Law**: new **`gaps-business-law` lesson** (contracts, IP, employment law, antitrust). | Was 🟡 — ethics covered, business law absent; law lesson now added. |
| 11 | **International / Global Business** | Med | 🟡 | Course 11 (global strategy), E9 (geopolitics) · Canon: History & Judgment (Thucydides, Allison, Clausewitz), Jervis. | Geopolitics/strategy covered; **technical IB** (trade theory, FX/hedging, market-entry modes, global supply chains) still lighter. *(only remaining partial)* |
| 12 | **Information Systems (MIS)** | Med | ✅ *(closed 6-06)* | **New `gaps-information-systems` lesson** (what an MIS is, ERP/enterprise systems, relational-database fundamentals, data governance) · E10 for AI/digital strategy. | Was 🔴 (the clearest gap) — now has a dedicated IS-fundamentals lesson. |

## The headline

**Baseline (2026-06-06, first pass):** 7 of 12 domains covered at depth; 4 partial; 1 outright gap (MIS).
The split wasn't random — everything in the *thinking* half of an MBA was strong (strategy,
leadership/OB, operations, economics, decision-making, communication) and every hole was in the
*technical/compliance* half. That's the **signature of a great-books canon**: enduring books cluster
around *ideas that compound*, not *procedures that get tested*.

**After the gap-closing pass (2026-06-06):** **11 of 12 domains now covered**, 1 partial (International
Business), 0 gaps. A **Technical Foundations** track added 5 lessons — managerial accounting,
quantitative methods/statistics, marketing strategy, information systems, and business law — built
from real lecture corpus (Edspira, StatQuest, April Dunford, MIS/data-governance, attorney-taught law).
- **Caveat on depth:** the gap domains are now *covered* (each has a dedicated, source-grounded lesson)
  but at **introductory, single-lesson depth** — not the multi-book depth of the strategy or leadership
  canon. They close the *coverage* gap; deepening (more books/lectures per domain) is the next tier.
- **Only remaining partial:** technical International Business (trade theory, FX/hedging, entry modes).
- Rough read now: you'd plausibly **hold your own across all MFT-MBA sub-scores**, strongest on
  strategy/management/integration, with the technical sub-scores moved from "would trail" to "competent."

## Closing the gaps — DONE (2026-06-06)

All five flagged gaps now have dedicated lessons in the **Technical Foundations** track
(`lessons/gaps-*.html`), built via `_research_gaps.py` → `gap_lessons_workflow.js`:

- [x] **Managerial / Cost Accounting** — `gaps-managerial-accounting` (Edspira: CVP/break-even, contribution margin, ABC, variance analysis).
- [x] **Quantitative Methods & Statistics** — `gaps-statistics-quant` (StatQuest: regression, hypothesis testing, p-values, confidence intervals).
- [x] **Marketing Strategy** — `gaps-marketing-strategy` (April Dunford positioning, Byron Sharp growth laws, STP, CAC/LTV).
- [x] **Information Systems** — `gaps-information-systems` (MIS, ERP, relational databases, data governance).
- [x] **Business Law** — `gaps-business-law` (contracts, IP, employment, antitrust).

### Next tier (depth, not coverage)
- [ ] **Deepen** each gap lesson from single-lesson → multi-source (e.g. add a marketing canon: Kotler, Byron Sharp's book, Ries & Trout *Positioning*; more StatQuest method coverage).
- [ ] **International Business** — the one remaining partial: a lesson on trade theory, FX/hedging, market-entry modes, global supply chains.
- [ ] **Benchmark yourself** — assemble the lesson quizzes into a scored diagnostic blueprinted to these domain weights; optionally sit CLEP (foundations) / CFA L1 (finance) externally.

## Next (to benchmark *you*, not just the curriculum)

- **Internal diagnostic exam** — assemble the ~100 existing lesson quiz questions + generate new ones, blueprinted to the domain weights above, scored. Gives a baseline + re-test.
- **External, individually-takeable** — **CLEP** business suite (foundations, ~$95 each, self-administered) and/or **CFA Level 1** (a brutal external benchmark for the finance/valuation clusters).
