# Big ERN's Safe Withdrawal Rate Series: the rules, the numbers, what a 30-year-old should take

> **Sources:** Karsten Jeske ("Big ERN"), *Early Retirement Now*, Safe Withdrawal Rate Series, Parts 1–66
> (Dec 2016 – Oct 19 2026) plus the companion "Ten Lessons from Ten SWR Case Studies" (Jan 2018). All 67 posts
> pulled 2026-11-01 from earlyretirementnow.com (index page plus a monthly archive page for Part 16, which the
> index doesn't link). Raw text kept locally only. Summarized in my own words; numbers are ERN's simulation outputs
> on his US data (1871 onward, monthly, real returns), **not independently re-run**.
>
> **What it adds:** [[portfolio-methodology-educators]] uses ERN for one line ("3.5% is the new 4%"). This note
> holds the rest of the rulebook: withdrawal rate by horizon and allocation, the CAPE rule, sequence risk, the
> glidepaths before and after retirement, the claims he tested and rejected (yield shield, flexibility, Bengen's
> 2026 portfolio), and the one he newly accepts (TIPS ladders at 3% real).
>
> **Maps to:** **E11** (personal operating system), **Course 07** (decisions under uncertainty), **E2** (capital
> allocation). Extends [[unit-10-personal-finance-operating-system]].
>
> **Lens:** **Decide** (primary), with **Understand** for the sequence-risk mechanics.
> **Methodology steps served:** **1** (target number), **2** (glidepath, before and after retirement), **4**
> (rebalancing cadence), **8** (the review rule). Some help for **7** (what to measure).
>
> ⚠ **Bias / limits.** ERN sells no products, but he's an early retiree with a 50–60-year horizon and a bequest
> goal, so his defaults are deliberately conservative. Only US history, which is the best-performing market of the
> century (survivorship). His own simulations disagree with Bengen's by 33–47bp on the *same* portfolio, so treat
> any SWR to two decimals as false precision. He is combative about rival ideas. Not advice.

---

## Core claim

A withdrawal rate isn't a constant. It depends on **horizon, final-value target, starting valuation (CAPE) and
allocation**, and the worst case is set by the **first ~10 years of returns** (sequence risk). For a long early
retirement starting from expensive equities, the failsafe sits around **3.25–3.5%**, not 4%. The tools that
actually move it are few: a lower rate, a rising equity glidepath, a valuation-linked rule, and, at today's real
yields, a partial TIPS ladder. Most popular "fixes" don't hold up in the data.

## Framework

### 1. Withdrawal rate by horizon and allocation (Parts 1–3, Ten Lessons)
| Setup (ERN, 1871– data) | Result |
|---|---|
| 4% WR, 50/50, 30 years | ~95% success |
| 4% WR, 50/50, 60 years | ~65% success (failure rate ~7× higher) |
| 5% WR | "unacceptably" low success even at 30 years |
| 80/20, 60 years | stubborn episodes at 3.5–4%, hence the slogan *"3.5% is the new 4%"* (Part 1) |
| 60-year horizon + bequest + high CAPE | **~3.25%** (Part 3) |
| 30-year, 75/25, start CAPE > 20 (Part 66 benchmark) | **3.82%** failsafe (1929 and 1968 cohorts) |
| 50-year, 75/25, keep 25% real, CAPE > 20 (Part 66) | **3.23%** failsafe |

- **Depletion vs preservation barely matters over 60 years** (Part 2, 80/20): preserve capital 3.92%, leave 50%
  4.12%, deplete to zero 4.33%. Over 30 years, depletion buys much more. So an early retiree should plan close to
  capital preservation; the "I'll spend it down" lever is weak.
- **Allocation:** over long horizons more equity raises success; bonds can go through multi-decade real droughts.
  His case-study verdict: **70/30 to 80/20 is the most robust in retirement**; both 50% and 100% had ugly failure
  rates (Ten Lessons #4). Part 3 had earlier argued ~100% equities unless CAPE > 30. The later view is the one
  he applies.

### 2. Valuation: the CAPE rule (Parts 3, 18, 54, 66)
- Historical 30-year SWR rises with the CAPE earnings yield (1/CAPE); a failsafe needs a further ~125bp haircut
  off the fitted line (Part 54).
- **Dynamic rule: WR = a + b × (1/CAPE).** His default is **a = 1.75%, b = 0.5** (Part 18). At CAPE 27 that's
  1.75% + 0.5/27 ≈ **3.6%**; at CAPE 20, 4.25%. When prices fall, 1/CAPE rises, so withdrawals fall less than the
  portfolio does.
- Part 54 tested a bolder version, WR = 1/CAPE (a = 0, b = 1). It failed in the 1920s, 30s and 70s. His
  safer variant: **a = −0.25%, b = 0.9, cap at 10%**.
- He uses his own adjusted CAPE as well as Shiller's. As of 10/16/2026: **39.58 Shiller, 35.44 ERN** (Part 66),
  which is "nosebleed" territory. The default rule then gives ~3.0–3.2%.
- Part 54 (Oct 2022, after a 25%+ real drawdown) declared "the 4% Rule works again". Valuation-linked means the
  safe number moves **both ways**.

### 3. Sequence risk (Parts 14, 15, 22, 37, 38, 53)
- It is **symmetric and zero-sum** between savers and retirees (Part 14): a crash hurts the retiree who's selling
  and helps the saver who's buying.
- **Savers face it too.** A lump sum doesn't. Spreading equity risk evenly over a lifetime helps: go 100% equities
  early, and don't prepay low-rate debt before you have a critical mass invested (Part 15). High-rate debt first.
- **Endogenous timing** (Part 22): retiring when you hit "25×" makes you likelier to retire right after a bull run.
  Failure rates rise, though not dramatically.
- **It never ends** (Part 38). Every review is day one again: recompute from today's portfolio, remaining horizon
  and CAPE. His line: *"Sequence. Risk. Will. Not. Go. Away!"*
- A well-planned retiree in a bear market shallower than 1929 or 1973 may get to **raise** spending afterwards
  (Part 37).

### 4. Glidepaths
- **Before retirement** (Part 43): for a high saver with a short runway, **100% equities is "not crazy"**. With
  more risk aversion, still start at 100% and walk down over the **last 2.5–5 years**. Standard target-date funds
  are already below ~70% equities ten years out, which is too early for FIRE savers.
- **After retirement** (Parts 19–20): a **rising** equity path, e.g. 60%→100% or 70%→90%. In the first decade, over
  60% of withdrawals then come from bonds, versus under 15% with a fixed 80/20.
  - Worth only about **+5% of sustainable spending** (Part 66 puts it at ~7%). It's insurance: it costs you in good
    paths and pays in bad ones.
  - Ramp fast, over about one bear-plus-bull cycle, not 30 years.
  - It **only helps when the starting CAPE is above ~20**. Below 20, a high static equity weight did best.
  - He rejects the Kitces/Pfau glidepaths specifically: they were calibrated on Monte Carlo, which misses valuation
    mean reversion, and they did poorly on historical data.

### 5. Dividends: the "yield shield" (Parts 29–31, 40)
- Tilting to high yield (dividend stocks, preferreds, high-yield bonds) to avoid selling shares **made sequence
  risk worse in 2007–09**: dividends were cut and credit sold off just when they were needed. He compares it to
  prescribing cigarettes for lung health.
- **Living off dividends** (Part 40): bad cohorts started at 1–3.3% yield, and real dividend income fell toward ~1%
  of the starting portfolio. With the S&P yielding under 2%, it only works for people with other income that
  fades out over 10–20 years. A bond-then-equity glidepath gets the same effect more cheaply.

### 6. Bengen's new portfolio (Part 65, Sep 28 2026)
- **Bengen's proposal:** 55% equities split equally across US large, mid, small, micro and international; 40%
  intermediate Treasuries; 5% T-bills. He claims 4.7% failsafe, 5.25–5.5% "with flexibility", and possibly 7% once
  valuations normalize.
- **ERN's replication:** the plain 55/40/5 gives **3.82%** (Bengen says 4.15%). The full Bengen mix gives **4.23%**
  (Bengen says 4.70%), and only if the 1926–81 small-cap premium repeats.
- **Starting at CAPE > 20, 50-year horizon:** 4.7% failed **58.1%** of the time and 5.5% failed **98.7%**. Even in
  his best case (short horizon, depletion), he puts 5.5% at a ~50% failure rate when CAPE > 20.
- **Without the small-cap premium (SMB):** you're back to ~3.8–4.0% (30 years) or ~3.25% (50 years).
- **Verdict:** this is stock-picking, not diversification. You can hold the portfolio, but don't raise your SWR for
  it. The same pattern shows up in Part 26 (a hindsight small-value tilt "would have" given 5.25%; large-growth gave
  under 3%) and Part 62 (adding small-cap value at zero future alpha just adds volatility).

### 7. TIPS (Part 61 → Part 66, Oct 19 2026)
- **2024 (Part 61):** "safety first" with TIPS and annuities was too expensive for 50+ year horizons. SPIAs carry
  inflation risk.
- **2026 rates:** 20–30-year TIPS yield **>3% real** (a 30-year bond at 3.17%). A full ladder costs just under
  **$2M per $100k/yr real income**, i.e. **~5.05% for 30 years with zero upside**.
- **Best use is partial**, optimized alongside a near-100%-equity remainder:
  - **30 years, depletion OK.** Benchmark is 3.82%. Results range from +11% to +32% budget:
    - 4.74% while keeping a $500k end cushion.
    - 4.44% when targeting median final value at 100% of the start.
    - About +11% even when the equity sleeve must stay at $500k or more.
  - **50 years, 25% final target.** Benchmark is 3.23%. An ~$882k ladder per $1M gives **4.07% (4.36% post-1926)**,
    and the median still ends near 2× real.
  - **Conservative case** (only ~a quarter converted): **~+7%**, about the same as a glidepath.
- **TIPS ETF ≠ ladder.** Swapping 25% nominal bonds for the TIP ETF changed 75/25 returns by about 1bp and raised
  equity beta. No SWR gain.
- **Caveats:**
  - Taxable accounts are a problem: you pay tax on the inflation accretion every year, and selling appreciated
    stock to buy TIPS triggers gains. So hold TIPS in tax-advantaged accounts.
  - At ~2.25% real the gain shrinks to ~4%.
  - Small tail risk of CPI manipulation.

### 8. Tested and mostly rejected or marginal
- **Spending flexibility** (Parts 9–10, 23–25, 58): to matter, cuts are ~30% and last until the portfolio recovers
  in real terms, which can take a decade or more.
  - Guyton-Klinger with a 5–6% start implies deep cuts that its backers rarely show.
  - It also creates "false alarm" cuts. The Dec 1972 cohort was ~70% down within 10 years yet would have survived.
- **Buckets** (48, 55): a relabelled glidepath at best.
- **Risk parity / All Weather** (64): systematically worse than 75/25.
- **Paid-off home** (57): small help, via its real yield.
- **Rebalancing frequency** (39): barely matters; quarterly is fine.
- **Partly positive:**
  - Gold (34) hedged both the 1970s and 2008, though ERN still didn't buy any.
  - Momentum / trend-following across equity, bond and gold (63): worst 30-year cohort 4.07% (1937); 1960s 4.79%.
  - Delaying retirement by one more year (42): pre-retirement flexibility is cheaper than post-retirement cuts.

## Applies when

You have a pile of money and a long, mostly fixed real spending need. For a ~30-year-old accumulating, the rules
translate to:

- **Step 1, target number.** Write two numbers into the IPS:
  - **Traditional (30-year) retirement:** ~26× spending (≈3.8%).
  - **Early (50-year) retirement starting from today's valuations:** **~29–31×** (3.25–3.5%).
  - Net out expected Social Security or pensions later (Parts 4, 17, 56). His spreadsheet handles this, with a
    haircut for benefit cuts.
  - Spending creep matters more than most variables: **+1%/yr real creep means cutting the initial budget by more
    than 10%**, and +2% means about 20% (Part 47). Get the baseline budget right, including lumpy items such as home
    repairs.
- **Step 2, glidepath.**
  - **Accumulation:** ~100% equities, invest before prepaying cheap debt, and de-risk only in the last ~2.5–5 years
    before the date (Parts 15, 43).
  - **First decade of retirement:** a rising path (e.g. 60→100%) if CAPE > 20 at the start.
  - **At retirement:** consider moving part of the tax-advantaged money into a TIPS ladder if real yields are
    still ~3%.
  - **Don't** add small-value, high-yield or risk-parity sleeves *in order to justify* a higher withdrawal rate.
- **Step 4, rebalancing.** A calendar rule (quarterly or annual) is fine. Don't over-engineer it.
- **Step 8, review.** Use the "Groundhog Day" rule. At each annual review, recompute the safe rate from current
  assets, remaining horizon and CAPE (e.g. 1.75% + 0.5/CAPE). Don't anchor to the day-one number.
- **Step 7, measure.** Track the **CAPE-conditioned failsafe**, not the unconditional success rate.

## Breaks when

- **Non-US or regime change.** All results are US history; an international investor or a regime break can do
  worse. Model uncertainty is beyond the CAPE conditioning (he concedes this in Part 46).
- **Small effective sample.** Over 50–60-year horizons there are only a few independent historical paths; the
  "failsafe" is really the worst of perhaps 3–4 distinct episodes (1900s/1910s, 1929, 1937, 1966–72).
- **High savings rate is assumed.** Part 43's "100% equities until retirement" assumes a 50%+ savings rate and a
  flexible date. A low saver, or someone with a fixed date, gets less from it.
- **Valuation signal can stay "wrong".** CAPE has been above 20 for most of the last 30 years; a valuation rule
  can keep you underspending for decades.
- **Rates move.** The TIPS result depends on real yields above 3% at the moment you buy.

## Practitioner counterpoint

- **Bengen** (5.5%) and **Merriman** (5%) argue that diversified tilts plus flexibility justify more.
- **Kitces/Pfau** favour their own Monte-Carlo-calibrated rising glidepaths.
- **Ayres & Nalebuff** push leverage while young. ERN's Parts 49/52 look at leverage only *in retirement*.
- **Utility view:** a flexible retiree may rationally prefer higher average spending with variable cuts. ERN's
  answer (Part 58) is that flexibility advocates must show the *time series* of cuts in the worst cohort, not just
  the initial rate.
- **Note the tension with the methodology note.** [[portfolio-methodology-educators]] groups "ERN and Pfau/Kitces"
  together as favouring rising glidepaths. That's true of the direction, but ERN explicitly rejects their calibrated
  paths (Part 20).

## Links

- [[portfolio-methodology-educators]]: steps 1, 2, 4, 8.
- [[unit-10-personal-finance-operating-system]]
- [[bet-sizing-conviction]]: a withdrawal rate is a sizing decision under an estimated *p*, so be conservative
  when the estimate is shaky.
- [[canon-taleb-black-swan]]: the failsafe is set by the tails.
- [[canon-klarman-margin-of-safety]]: the CAPE haircut is a margin of safety.
- [[canon-kahneman-thinking-fast-and-slow]]: anchoring to the 4% headline.
- [[canon-mauboussin-success-equation]]: one cohort's luck isn't the rule.
- [[canon-duke-thinking-in-bets]]: judge the plan, not the path.

## The one-line habit

Every year, pretend it's your first day of retirement. Recompute the rate from today's balance, remaining years
and CAPE, and only then decide what to spend.
