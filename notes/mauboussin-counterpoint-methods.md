# Mauboussin & Callahan: Reading the Price, Then Scoring Yourself

> **Sources:** 20 research papers by Michael Mauboussin (with Dan Callahan from 2013 on), pulled 2026-11-01 into
> `_ingest/raw/2026-11-01/mauboussin/` (PDF + text, local only). The main ones: *Everything Is a DCF Model*
> (2021), *Market-Expected Return on Investment* (2021), *The Math of Value and Growth* (2020), *The Impact of
> Intangibles on Base Rates* (2021), *ROIC and the Investment Process* (2023), *Capital Allocation: Results,
> Analysis, and Assessment* (2022), *Valuation Multiples* (2024), *Cost of Capital* (2023), *Confidence* (2023),
> *Feedback* (2022), *BIN There, Done That* (2020), *Dispersion & Alpha Conversion* (2020), *Pattern Recognition*
> (2023), *Who Is On the Other Side?* (2019 BlueMountain edition). Also *Where's the Bar?* (2001), *Calculating
> ROIC* (2014) and *Economic Returns, Reversion to the Mean* (2013). The paper list comes from the complete-works
> index on michaelmauboussin.com, which links each paper. Summarized in own words.
>
> **⚠ Blocked:** every PDF on morganstanley.com returned an Akamai 403, both to scripts and to the fetch tool.
> That covers all papers from mid-2024 on: *Measuring the Moat* (2024), *Probabilities and Payoffs* (2025),
> *Capital Allocation (Updated)* (2025), *Drawdowns and Recoveries* (2025), *Who Is On the Other Side?* (2026
> edition), *Bayes and Base Rates* 1.0 and 2.0 (2026), *Competitive Advantage Period* (2026), *Opportunities and
> Expectations* (2026), *The Wisdom of Crowds in Markets* (2026) and *To Free or Not to Free (Cash Flow)* (dated
> 2026-09-18 on the author's site). Their titles and dates are confirmed. Their contents are **not** summarized
> here. The claim in [[portfolio-methodology-educators]] that "direct URLs work" did not hold on 2026-11-01.
>
> **What it adds:** [[canon-mauboussin-success-equation]] covers the skill-vs-luck *idea*. This note covers the
> *working tools*: how to read what a price assumes (step 5), and how to build a measurement system that tells
> skill from luck (step 7).
>
> **Lens:** **Decide** (primary) and **Understand**. **Methodology steps:** **5** (valuation inside the
> satellite-stock process), **7** (measurement and the decision journal), with support for **8** (review against
> signposts, not price). **Maps to:** Course 02 (valuation), Course 07 (decisions under uncertainty), E2
> (capital allocation).
>
> **⚠ Bias:** Counterpoint Global is an active growth-equity manager at Morgan Stanley IM. Research showing that
> active skill exists, and that intangible-heavy companies are mis-measured, supports its product. The papers
> are careful and well footnoted, but most of the data is FactSet/Counterpoint's own. Not advice.

---

## Core claim

You don't need to know what a stock is "worth." You need to know **what its price already assumes**, and
whether those assumptions are likely to be revised. Excess returns come from **revisions in expectations**, not
from owning good companies. That makes the edge measurable, and so it should be measured: write down the
forecast that the variant view depends on, score it, and decompose your results.

## Framework, step 5: reading the price

**1. Everything is a DCF, so use the DCF backwards.**
- Multiples are compressed DCFs. In a survey of about 2,000 analysts, P/E was used 88% of the time and
  EV/EBITDA 77%.
- The continuing value is typically 70–80% of a DCF's value, and it is usually set with an exit multiple. Most
  "DCFs" are therefore multiples underneath.
- The fix is to stop solving for value and solve for the assumptions instead: **what must you believe about
  growth, returns and the length of the advantage to justify today's price?** Then judge whether that is likely.
- "You have to earn the right to use a multiple" (Mauboussin & Callahan, 2021). You earn it by showing how the
  multiple links back to the value drivers.
- The method doesn't apply to assets without cash flows: crypto, art, gold.

**2. The anchors for the multiple math** (*Math of Value and Growth*):
- **Commodity P/E = 1 / cost of equity.** This is the multiple for a business that creates no value.
  - At an 8% cost of equity it is 12.5×. It averaged 10.7× from 1961 to 2020 and fell to 5.1× in 1981.
  - The S&P 500's actual P/E has run about 35% above it, mostly in a range of 20–65% above.
- **Growth only adds value when ROIIC exceeds the cost of capital.** If the return on new capital equals the
  cost of capital, growth adds nothing. If it is lower, faster growth destroys value faster.
- **Small changes in near-term earnings imply large changes in the multiple.** Example: 10% NOPAT growth, a 20%
  ROIIC and a 6.7% cost of capital give 32.3×. Cutting growth to 7% lowers next year's earnings by only 2.7%, but
  the warranted P/E falls about 23%, to 24.9×. A "market overreaction" to a small miss may be a correct re-rating
  of the growth path.
- **MEROI** (market-expected return on investment) is the return on future investment that the price implies.
  It sets the bar the company has to clear. To compute it you have to separate SG&A into expense and
  intangible investment.

**3. Use base rates to check the implied path.**
- Combine the **inside view** (the analyst model, a causal story) with the **outside view** (how a reference
  class of similar companies actually performed). The combination forecasts better than either alone.
- In their experience, people under-use base rates far more often than they over-use them.
- **Benchmark:** in 1950–2015 data, no company with $100B or more of sales had grown at a mid-teens rate for
  about a decade. Amazon then broke that base rate, on track for about 28% six-year growth through 2022.
- **Intangibles widen both tails.** Intangible assets scale cheaply, so winners can grow faster than history
  shows. They also become obsolete with little salvage value, so losers can fall faster (BlackBerry: −26.7% a
  year over a decade).
  - Russell 3000 intangible investment was about $1.8T in 2020, against about $0.8T of capex.
  - Base rates still apply, but weight the tails more heavily for intangible-heavy companies.
- **Base rate for ROIC persistence** (Russell 3000 excluding financials and real estate, rolling 3-year windows,
  1990–2022, intangible-adjusted ROIC):

  | Start quintile → | stays put | ends in top | ends in bottom |
  |---|---|---|---|
  | Top (5) | **48%** | n/a | 15% |
  | Bottom (1) | **41%** | 12% | n/a |

  Annualized 3-year TSR: bottom→top **+33%**, top→bottom **−11%**, top→top +20%.
  - **The return is in the *change* in ROIC, not its level.** The risk-adjusted returns of four of the five
    starting quintiles were similar. Buying "quality" earns nothing extra if the price already assumes it stays
    quality.
  - Capitalizing intangibles leaves the median ROIC about the same but pulls the extremes toward the average.

**4. Name who is on the other side (BAIT).** Before any active trade, name the inefficiency you are exploiting:
- **Behavioral:** crowd errors such as over-extrapolation and sentiment. Opportunities arise when crowd
  diversity breaks down, and they are collective, not individual.
- **Analytical:** weighting information better, updating more like a Bayesian, using a longer time horizon
  (time arbitrage), or anticipating a change in the narrative.
- **Informational:** legal information others lack, or information others are slow to process because
  attention is limited or the topic is complex.
- **Technical:** forced sellers, fund-flow pressure, or providing liquidity when arbitrageurs are capital-starved.

If you can't name the category, assume you are the one providing the edge to someone else.

**5. Capital allocation is a value driver.** These are average results, and individual cases vary widely.
- **Associated with positive excess TSR on announcement:** spin-offs, divestitures, dividend initiations,
  buybacks, debt paydown, capex.
- **Roughly neutral:** R&D, and M&A for the buyer.
- **Negative:** equity issuance (IPOs and secondary offerings). High asset growth also predicts low TSR.
- **Five principles for judging management:**
  1. Allocate capital zero-based.
  2. Fund strategies, not projects. A good project inside a bad strategy is still a bad use of capital.
  3. Don't ration capital, but require returns above its cost.
  4. Zero tolerance for bad growth.
  5. Know what the assets are worth and act on it.

## Framework, step 7: measurement and the decision journal

**1. Score the variant view, not the stock.**
- Break the thesis into a few dated, measurable forecasts with probabilities. Example from the paper: "more than
  110 new subscribers this quarter, 80%," where the market has priced in about 100.
- Score them with a **Brier score**: (forecast − outcome)² for the event plus the same for the non-event. The
  scale runs 0–2, and lower is better. An 80% call that comes true scores 0.08.
- Most firms already have the raw data to do this and don't. The paper's explanation is that after a miss we
  build a flattering story instead of recording the error.

**2. Linchpin analysis** (borrowed from the CIA) for the thesis page:
1. List the key drivers.
2. State the linchpin assumptions about how each will behave.
3. Give the evidence for each.
4. Set **signposts** that would make an assumption unreliable.
5. Name the triggers that would reverse the outcome.

Review against the signposts, not the price (step 8).

**3. Log non-decisions.** Stocks you looked at and passed on stay in the database and get reviewed too. Audit
decisions that worked as well as those that failed, because a good outcome can come from a bad process plus luck.

**4. Record confidence separately from probability** (*Confidence*, 2023). A 50% can mean a well-understood
coin-flip or total ignorance. Log three things next to each probability:
- **Reliability of the evidence:** is there enough information to reach a sound conclusion?
- **Range of reasonable opinion:** how wide could informed views be?
- **Responsiveness to new information:** how likely is more data to change the thesis?

Stop researching when more information is unlikely to change the decision. Let confidence inform the
position weight ([[bet-sizing-conviction]]).

**5. Decompose performance every quarter or year** (*Dispersion & Alpha Conversion*):
1. **Selection:** compare an equal-weighted copy of the starting holdings with the benchmark. Your *batting
   average* is the share of holdings that made money.
2. **Sizing:** compare the starting weights, held unchanged, with the equal-weighted copy. *Slugging ratio* is
   the average gain on winners divided by the average loss on losers.
3. **Activity:** compare the actual portfolio with the starting weights held unchanged. Look at buys and sells
   separately.
4. **Opportunity set:** check the return dispersion in the sectors where you were active. Skill can only show up
   where dispersion is high.
- **Rule of thumb** (Ronald Van Loon, cited in the paper): IC ≈ 1.6 × [batting average − 1/(1 + slugging)].
  At a 30% batting average with a 2.6 slugging ratio, the information ratio is about 0.3, the same as at 80% with
  0.3. You can be right far less than half the time and still add value.

**6. Reduce noise before bias** (*BIN*, building on Satopää, Tetlock and colleagues):
- The study's main finding is that cutting **noise** improved forecasts about **twice as much** as cutting bias
  or adding information.
- A noise index is the gap between two judgments divided by their average. About 10% is tolerable. Noise audits
  in insurance and finance found 40–60%.
- **Remedies:** average independent judgments, use algorithms or checklists (for sizing, for example), and use
  red teams and premortems for bias.
- In the Good Judgment Project, about 2% of forecasters were "superforecasters." Their habits are trainable.

**7. Trust gut pattern-recognition only in valid domains.** Intuition works where cause and effect are stable
and feedback is fast and accurate, as in chess. Most market and economic prediction doesn't meet that bar. An
expert is someone with a predictive model that works, not just someone with experience.

## Applies when
- You hold satellite stocks or argue for one in an apply rep ([[apply-stock-picking-nke]]): reverse the price
  first, then form a view.
- You need a scorecard for step 7. The repo still lacks one, and the Brier + linchpin + four-step decomposition
  above is enough to build it.
- You are judging a CEO's capital allocation in a company study.

## Breaks when
- **Implied expectations aren't unique.** A price can be solved for many combinations of growth, margin and
  advantage period. Reverse-DCF narrows the question; it doesn't give one answer.
- **The reference class shifts.** Amazon broke the large-company growth base rate, and intangibles widen both
  tails, so a base rate can anchor you to the wrong world.
- **Too few decisions to score.** A personal portfolio with 10 positions produces too few resolved forecasts
  per year for Brier scores or batting averages to separate skill from luck for several years. Treat early
  scores as calibration practice, not as a verdict.
- **ROIC is hard to measure.** Results change with how intangibles, leases and excess cash are treated. Pick one
  method and use it consistently.
- **Source incentive.** The data and framing come from a seller of active management (see ⚠ Bias).

## Practitioner counterpoint
- The same papers say the market is *usually* the better forecaster. The wisdom of crowds is why *Everything Is
  a DCF* says most investors can defer to the price.
- For a personal investor, the honest output of the BAIT test is often "I have no edge here." That points back
  to the core index holding (steps 2–3), not to more research.
- Damodaran (narrative → numbers) is the complement: Mauboussin asks what the price believes, Damodaran asks what
  the story is worth. Use both and compare the gap.
- Klarman would add a margin of safety on top of any implied-expectations gap ([[canon-klarman-margin-of-safety]]).

## Links
[[portfolio-methodology-educators]] (steps 5 and 7) · [[canon-mauboussin-success-equation]] (the concept
behind step 7) · [[bet-sizing-conviction]] (confidence → size) · [[canon-tetlock-superforecasting]] (Brier,
superforecasters) · [[canon-kahneman-sibony-sunstein-noise]] (noise audits) · [[canon-duke-thinking-in-bets]]
(decision ≠ outcome) · [[canon-kahneman-thinking-fast-and-slow]] (inside vs outside view) ·
[[canon-klarman-margin-of-safety]] · [[canon-helmer-7-powers]] (sources of a durable ROIC spread) ·
[[unit-05-growth-and-returns]] · [[unit-06-whats-a-business-worth]] · [[unit-07-the-landscape-moats]] ·
[[apply-stock-picking-nke]] · [[canon-jensen-meckling-agency-theory]] (management incentives in capital
allocation)

## The one-line habit
Before buying, write: **"The price assumes X. I think Y, because of [BAIT category]. Signpost: Z by [date], p =
__."** Score it when the date arrives.
