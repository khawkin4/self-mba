# External Benchmark — calibrating against the real exams

> The "benchmark against actuals" anchor. Two parts: **(1)** the real, individually-sittable exams,
> their published blueprints, and links to their **official free practice** (go take the genuine
> article); **(2)** an **original, exam-calibrated question bank** we generate to those blueprints
> (`benchmark-exam.html`) — written to real-exam difficulty/format, NOT copied from any exam
> (their items are copyrighted). Verified June 2026.

## The real exams (sit these for a true score)

### CFA Level 1 — the deep finance benchmark
- **Format:** 180 multiple-choice questions, **3 options each**, two 90-question sessions, 4h30m.
- **Topic weights (2026, unchanged from 2025):** Ethics **15–20%** · Financial Statement Analysis 11–14% · Equity 11–14% · Fixed Income 11–14% · Portfolio Mgmt 8–12% · Alternatives 7–10% · Quant 6–9% · Economics 6–9% · Corporate Issuers 6–9% · Derivatives 5–8%.
- **Official practice:** CFA Institute Level I candidate resources (free sample/practice questions + a learning-ecosystem mock). → cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam
- **Maps to our domains:** Finance, Economics, Quantitative & Statistics, Legal & Ethical (Ethics).

### GMAT Focus Edition — quant + reasoning benchmark
- **Format:** 3 sections × 45 min, scored 60–90 each (total 205–805):
  - **Quantitative Reasoning** — 21 problem-solving Qs, 5 options (no geometry).
  - **Verbal Reasoning** — 23 Qs: Critical Reasoning + Reading Comprehension (no sentence correction).
  - **Data Insights** — 20 Qs: Data Sufficiency, Multi-Source Reasoning, table/graph analysis.
- **Official practice (FREE):** GMAT Focus **Official Starter Kit** = 2 full practice exams + concept reviews; +367 authentic questions in the paid bank. → mba.com/exams/gmat-exam/about/exam-content
- **Maps to our domains:** Quantitative & Statistics, Economics (quant), Strategy/Integration (Critical Reasoning), Communication (Reading Comp).

### CLEP business suite — foundations, individually sittable (~$95, credit-granting)
- **Financial Accounting** — ~75 Qs / 90 min. **Principles of Management** — ~100 Qs / 90 min.
  Also: **Principles of Marketing**, **Information Systems**, **Introductory Business Law**,
  **Principles of Microeconomics / Macroeconomics**.
- **Official practice:** free sample questions on each exam page. → clep.collegeboard.org/prepare-for-an-exam/practice-questions-study-guides
- **Maps to our domains:** Accounting, Management & OB, Marketing, Information Systems, Legal & Ethical, Economics — i.e. **exactly the technical/foundations half** the benchmark scorecard flagged.

### ETS Major Field Test — MBA (the program-outcomes benchmark)
- Institution-administered (can't self-sit); ~124 Qs across the ~10 MBA domains. Its **domain blueprint** is what `BENCHMARK-MFT-MBA.md` scores coverage against and what our calibrated bank is weighted to.

## Our domain → which real exam benchmarks it

| Our domain | Closest real benchmark | Calibrated question style |
|---|---|---|
| Finance | CFA L1 (FSA/Equity/FI) | CFA 3-option, computational + concept |
| Accounting | CLEP Financial Accounting | CLEP application |
| Economics | CLEP Micro/Macro · CFA Econ | concept + GMAT quant word-problem |
| Quantitative & Statistics | GMAT Quant + Data Insights · CFA Quant | problem-solving + data-sufficiency |
| Strategy / Integration | MFT-MBA · GMAT Critical Reasoning | scenario / argument analysis |
| Marketing | CLEP Principles of Marketing | application scenario |
| Management & OB | CLEP Principles of Management · MFT-MBA | applied judgment |
| Operations | MFT-MBA · GMAT Data Insights | quantitative scenario |
| Information Systems | CLEP Information Systems | concept + scenario |
| Legal & Ethical | CLEP Business Law · CFA Ethics | scenario / standards application |
| International Business | MFT-MBA international | scenario |
| Communication | GMAT Reading Comp (adjacent) | applied judgment |

## Real, previously-administered exams (public, WITH answer keys)

> The truest "actuals": real graduate exams that were given to real students, posted free with
> solutions. Verified live June 2026. **Copyright:** these are © their authors (Damodaran posts
> freely but retains rights; MIT OCW is CC BY-NC-SA). The benchmark = *point the model (or yourself)
> at the source PDF and score against the posted answer key* — do **not** copy the questions into
> this repo. Each is a real, scoreable test battery.

### Finance & Valuation — Aswath Damodaran (NYU Stern) · the motherlode
The world's valuation authority, decades of his actual exams + Excel answer keys, free:
- **Corporate Finance exams** — quizzes 1–3, a final, and **midterms spanning 1986–1997**, each with
  Excel solution keys. → `pages.stern.nyu.edu/~adamodar/New_Home_Page/cfprob0.html`
- **Valuation exams** — Quiz 1 (DCF basics), Quiz 2 (DCF loose ends + relative), Quiz 3 (relative +
  private-company), Final (all valuation), all with Excel keys; an extensive historical set. →
  `pages.stern.nyu.edu/~adamodar/New_Home_Page/eqexam.htm`
- **Why it's ideal:** it *is* the valuation/capital-structure/risk hierarchy this project ranks first —
  hundreds of graded, numerical, graduate-level questions with worked keys.

### MIT Sloan — MIT OpenCourseWare (real Sloan course exams + solutions, free)
- **15.401 Finance Theory I** (Fall 2008) — sample midterm + final with solution keys; most exam items
  drawn from the posted *MIT Sloan Finance Problems and Solutions Collection*. →
  `ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/exams/`
- **15.501 Introduction to Financial & Managerial Accounting** (Spring 2004) — finals from multiple
  semesters (e.g. Dec-2002 final + solution), midterms, and an exam formula sheet. →
  `ocw.mit.edu/courses/15-501-introduction-to-financial-and-managerial-accounting-spring-2004/pages/exams/`
- **15.402 Finance Theory II** — practice midterm + final (capital structure, FCF valuation, WACC, APV).

### Wharton (scattered, public)
- FNCE 611/612 & ACCT 611 **waiver/placement exams** (full PDFs on `mba-inside.wharton.upenn.edu`).
- FNCE 100 (Corporate Finance) midterm solutions on the instructor's `finance.wharton.upenn.edu` page.
- *No* standardized "Wharton MBA final" exists — each professor writes their own; Terwiesch's 2023
  operations-management exam (`mackinstitute.wharton.upenn.edu`) was a one-off research release.

### Using these as a battery (no copying required)
1. Pick a source exam (e.g. a Damodaran valuation final) — open the PDF from the link above.
2. Answer it (you, or the model) **from the source**; grade against the posted Excel/PDF key.
3. Record the score per topic; map to this file's domain table. Repeat across sources for breadth.
> This is the highest-fidelity benchmark available for the finance/valuation stack — real exams, real
> keys, real difficulty — and it sidesteps the copyright problem because nothing is reproduced here.

## How to read your two scores
- **`benchmark-exam.html`** (our calibrated bank): an *application-level* proxy — harder than the
  lesson recall quizzes, written to the blueprints above. A weak domain here = a real study target.
- **A real official practice exam** (CLEP sample / GMAT Starter Kit / CFA mock): the *true* external
  score. Sit one, bring the result back, and we map it to these domains + build a targeted plan.

**Sources:** [CFA Level I (CFA Institute)](https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam) · [2026 L1 topic weights (soleadea)](https://soleadea.org/cfa-level-1/topic-weights) · [GMAT exam content (mba.com)](https://www.mba.com/exams/gmat-exam/about/exam-content) · [CLEP practice questions (College Board)](https://clep.collegeboard.org/prepare-for-an-exam/practice-questions-study-guides) · [CLEP Financial Accounting](https://clep.collegeboard.org/clep-exams/financial-accounting) · [CLEP Principles of Management](https://clep.collegeboard.org/clep-exams/principles-management)
