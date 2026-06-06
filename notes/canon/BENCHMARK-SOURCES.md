# Benchmark sources — wide-net capture → depth queue

> **Strategy:** wide net to capture, then individual processing time for depth, then synthesis.
> This file is the *capture* layer: a broad catalog of real, public, previously-administered exams
> and question sets, tiered by fidelity. Verified live June 2026. **Copyright:** everything here is
> linked, never copied — these items are © their authors (Damodaran retains rights; MIT OCW is
> CC BY-NC-SA; CFA/CPA/CLEP are protected). The benchmark = open the source, answer it, score against
> its published key. Nothing reproduced in-repo.

## Tier 1 — GOLD: real exams *with full answer keys* (scoreable as-is)

| Domain | Source | What's there | Link |
|---|---|---|---|
| **Finance / Valuation** | Damodaran (NYU Stern) | Corp-finance **midterms 1986–1997** + quizzes 1–3 + final, all w/ Excel keys | `pages.stern.nyu.edu/~adamodar/New_Home_Page/cfprob0.html` |
| **Finance / Valuation** | Damodaran | Valuation quizzes 1–3 (DCF → relative → private) + final, Excel keys | `pages.stern.nyu.edu/~adamodar/New_Home_Page/eqexam.htm` |
| **Finance** | MIT OCW 15.401 Finance Theory I | sample midterm + final w/ solutions; + *Finance Problems & Solutions Collection* | [ocw 15.401 exams](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/exams/) |
| **Finance** | MIT OCW 15.402 Finance Theory II | practice midterm + final (capital structure, FCF, WACC, APV) | ocw.mit.edu (15-402) |
| **Accounting** | MIT OCW 15.501 Fin. & Mgmt Accounting | finals from multiple semesters + solutions + formula sheet | [ocw 15.501 exams](https://ocw.mit.edu/courses/15-501-introduction-to-financial-and-managerial-accounting-spring-2004/pages/exams/) |
| **Economics** | MIT OCW 14.01 Microeconomics | **midterm + final WITH solutions** (Fall 2023 & Fall 2011) + problem sets | [ocw 14.01 (2023)](https://ocw.mit.edu/courses/14-01-principles-of-microeconomics-fall-2023/) |
| **Finance / Markets** | Open Yale ECON 252 (Shiller) | midterm + final w/ solutions (~50% math/theory, 50% concept) | [oyc ECON 252](https://oyc.yale.edu/economics/econ-252) |
| **Finance / Ethics / Quant** | CFA Institute | 10 official Level-I sample Qs free + 20 via form; full mocks in ecosystem | [CFA sample qs](https://www.cfainstitute.org/programs/cfa-program/cfa-program-level-i-sample-questions) · [mocks](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/mock-exam-and-practice-questions) |
| **Accounting** | AICPA | **140 released CPA exam questions** (answers given) + blueprints | [A71 free CPA qs](https://www.another71.com/lpc/cpa-exam-questions/) |
| **Foundations (multi)** | CollegeBoard CLEP | sample questions per exam (Fin. Acct, Mgmt, Marketing, IS, Business Law, Micro/Macro) | [CLEP practice](https://clep.collegeboard.org/prepare-for-an-exam/practice-questions-study-guides) |

## Tier 2 — SILVER: real past exams, partial/no keys (usable, must self-verify)
- **International university MBA past papers** — real, posted exams across the domains the elite US schools *don't* expose:
  - Marketing Management — VTU (`vtu.ac.in/pdf/QP/20MBA15.pdf`), Delhi University, Savitribai Phule Pune University, VMOU.
  - Operations Management, Strategic Management, Organizational Behavior — VTU / Anna University / SIETK / MRCET question banks + previous-year papers.
  - These are genuine sat exams; answer keys are often absent → pair with the calibrated bank for scoring.

## Tier 3 — question banks / aggregators (breadth, uneven quality)
- Cracku (CAT/XAT/IIFT solved), Universal Teacher Publications, SIMS Bangalore old papers, Studocu/Scribd/Course Hero uploads (incl. real Wharton/MIT course exams, quality varies).
- Wharton FNCE 611/612 & ACCT 611 **waiver/placement exams** (full PDFs, `mba-inside.wharton.upenn.edu`).

## Coverage by domain (what the net caught)
| Domain | Best available | Fidelity |
|---|---|---|
| Finance / Valuation | Damodaran + MIT 15.401/402 + Yale 252 + CFA | **GOLD** (deep, keyed) |
| Accounting | MIT 15.501 + AICPA 140 + CLEP | **GOLD** |
| Economics | MIT 14.01 (keyed) + CLEP Micro/Macro | **GOLD** |
| Quant & Statistics | CFA quant + MIT problem sets + GMAT official | Gold-ish |
| Management/OB · Marketing · Operations · Strategy | CLEP (Mgmt/Mktg) + intl. past papers + our calibrated bank | **SILVER** (elite schools are case-based, no public exams) |
| Legal & Ethical | CLEP Business Law + CFA Ethics | Silver |
| Information Systems · International | CLEP IS + intl. past papers | Silver |

**Honest pattern (same as the coverage scorecard):** the *quantitative* half (finance, accounting,
economics) has GOLD real-exam benchmarks with keys; the *qualitative* half is case-taught at elite
schools, so it has no clean public exams — there, the standardized certs (CLEP) + our calibrated
bank + international past papers are the realistic benchmark.

## Depth queue — "individual processing time" (process top-down)
1. **Damodaran Valuation final** — open PDF, work it, score vs the Excel key → the highest-fidelity single test of the core stack.
2. **MIT 14.01 Micro final (Fall 2023, keyed)** — economics, clean solutions.
3. **MIT 15.501 Accounting final + AICPA 140** — accounting depth.
4. **Yale ECON 252 final (Shiller)** — markets/behavioral finance.
5. **CFA Level-I sample set** — cross-domain, professional standard.
Each: log score + per-topic misses → feeds the synthesis layer (BENCHMARK-MFT-MBA.md domain map) and
points to which lessons to deepen.

## Depth-pass log (real exams, worked vs. published key)

> Worked from the source PDF, scored against the official Excel key; exam content not reproduced.

| Date | Source | Scope | Score | Notes |
|---|---|---|---|---|
| 2026-06-06 | Damodaran Valuation **Quiz 1, Fall 1997** | 3 problems (implied ERP · FCFE · FCFF) | **3/3 exact** | Caught both traps: normalized NI off book-equity×ROE (not the bad-year figure) + resolved contradictory equity figures into a 25% market debt ratio; matched the implied-ERP convention (2.68%) and pre-flagged the key's 2.5% alternative. |
| 2026-06-06 | Damodaran Valuation **Final, Fall 1997** (2-hr, worth 30%) | 11 sub-parts: multi-stage FCFE, FCFF w/ ROC reinvestment, Value/Sales (+relevered β restructuring), Black-Scholes equity-as-option, EVA synergy | **27/30 (90%)** | Exact matches on P1 (TV 23.01, value 10.67), P2 (netcapex 36, value 1134), P3 (V/S 0.552 → relevered 0.887), P4a (N(−d2) bankruptcy), P5 EVA (G&P 2700, BandAdd 800, synergy 1604). **One miss — P4b:** declared the debt face value "missing" when it was recoverable by back-solving the BS equity equation from 4a's d1/d2 (key K≈99.7 → 8.6%). A **multi-step-linkage** failure, not arithmetic — the exact pattern the Wharton/Brookings studies predicted. |

### Synthesis (depth pass so far)
On real, keyed graduate valuation exams the finance/valuation reasoning is **strong (90%+)**: it nails
multi-stage DCF, FCFF/FCFE, relevering beta, Value/Sales, EVA, and option-based equity valuation. The
**single recurring risk is multi-step linkage** — carrying one part's output into the next — not the
math itself. Mitigation for the platform: when a problem spans parts, *explicitly* check whether an
"unknown" is derivable from a prior part before declaring it missing. Next depth items (breadth):
MIT 14.01 micro final, AICPA accounting set, Yale ECON 252.

**Read:** clean pass on the *fundamentals* tier (Quiz 1 = "be brief", 1–4 pts/problem). The real
stress test is the **finals.pdf** multi-stage problems (3-stage FCFF with margin/ROIC fade, terminal
value, relative-valuation cross-checks) — exactly the multi-step arithmetic where the Wharton (2023)
and Brookings (2025) studies found models stumble. Next depth item: work one full valuation *final*
problem, not a quiz.
