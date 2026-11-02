# Rational Reminder: what the evidence says about building a portfolio

> **Sources:** 26 Rational Reminder episode pages (rationalreminder.ca/podcast), pulled 2026-11-01 with full
> transcripts or show notes: eps 6, 72 (asset location); 117, 135, 229, 340 (withdrawal rates, lifecycle model);
> 125, 262, 430 (human capital, leverage); 129, 213, 227, 394 (factors, cap weighting, equal weight); 281, 284,
> 350, 374 (Cederburg lifecycle research, target-date funds); 343, 373, 388, 416 (choosing an allocation in
> practice, 100% equity, all-in-one ETFs); 379 (currency hedging); 397, 432 (leveraged ETFs); 431, 433 (the
> latest two). Hosts are Ben Felix with Cameron Passmore (early years), and later Dan Bortolotti, Mark McGrath and
> Ben Wilson, all at PWL Capital. Raw text stays local in `_ingest/raw/2026-11-01/rational-reminder/`. Summarized
> in my own words.
>
> **What it adds:** [[portfolio-methodology-educators]] names Ben Felix as a teacher for steps 1–4. This note
> pulls out the actual numbers and decision rules from the show, so steps 1 (risk profile), 2 (allocation and
> tilts), 3 (location) and the withdrawal side of step 1 have sources you can check.
>
> **Maps to:** **Course 07** (decisions under uncertainty), **E11** (personal operating system). Extends
> [[unit-10-personal-finance-operating-system]].
>
> **Lens:** **Decide**, with some **Understand** (asset pricing, how leveraged ETFs work).
> **Methodology steps served:** 1 (objectives, risk capacity, withdrawal rate), 2 (allocation, glide path,
> factor tilts), 3 (implementation, asset location), 4 (rebalancing), 8 (review).
>
> ⚠ **Bias:** PWL Capital is a fee-based advisor (bought by OneDigital in 2025; ep 343 addresses this). The
> show is evidence-led but argues for low-cost, factor-tilted funds (Dimensional and Avantis appear often), and
> its audience is **Canadian**. Not advice.

---

## Core claim

Risk is a three-part constraint, not a single number. Once you take long-horizon, global data seriously, the
stock/bond decision looks very different from the usual "100 minus age" and target-date advice. Bonds are less
safe over 30 years than they look month to month. Factor tilts have small but positive expected value after
fees. Tax-account tricks mostly change *what you really own*, not your free lunch.

## Framework

### 1. The risk profile: three parts, and the smallest one wins (eps 343, 373, 388)
- **Behavioural loss tolerance:** what you will actually sit through. They break it into six elements, from
  John Grable's framework. The one that matters most is *risk composure*, meaning how you behaved in a real
  drawdown. A questionnaire can't measure that.
  - Men tend to overestimate their tolerance and women to underestimate it (Grable, as cited by Felix).
  - PWL maps a "high" psychometric score to **70–100% equity**. The questionnaire is a constraint on the
    allocation, not the answer.
- **Ability (capacity) to take risk:** set by horizon, liquidity needs and other assets. Using the example from
  Grable's CFA text:
  - **Low:** horizon under 5 years, or withdrawing **≥5% of the portfolio a year**, with no other assets or
    income.
  - **High:** 10+ years, no withdrawals, and a backstop such as a pension.
- **Need:** the return your plan actually requires. A Monte Carlo plan sometimes shows a retiree can drop risk
  (one couple's plan worked at 20/80). Sometimes it shows they can add risk (an 80-year-old couple with pensions
  went to 70/30).
- **Bortolotti's rule for beginners (ep 388):** start balanced, around 60% (80% at most). Only move to 100%
  equity if, in the middle of a 20–30% fall, you can still say you're comfortable with it.
- **Drawdown sizes to quote (ep 373, Canadian data since 1970):**
  - 100% stocks fell **48%** in 2008 and took about **4 years** to recover.
  - A 40/60 portfolio fell **19%** and recovered in about **9 months**.
  - $1 grew to about $130 in 100% stocks, $98 in 60/40, and $49 in 100% bonds.

### 2. Human capital and pensions are assets on the balance sheet (eps 125, 262, 373, 416, 430)
- **Gomes (ep 262):** what matters is the ratio of human capital (the present value of your future wages) to
  financial wealth. When that ratio is high, you already hold a large implicit safe asset, so the financial
  portfolio can be riskier.
- **Bond-like or stock-like?** A stable job (tenured, government) behaves like a bond. Commission or
  single-industry income behaves like a stock, and calls for less equity and, per ep 125, *less* life insurance.
- **Defined benefit pension:** treat it as part of the fixed-income side.
  - Illustration: a $70k/yr pension over 30 years, discounted at 4%, is worth about **$1.2M** in present value.
  - The catch is behavioural. With the bonds sitting outside the portfolio, the visible portfolio swings more.
- **Leverage when young (ep 430; theory from Bodie, Merton and Samuelson, 1992):** if your human capital is safe
  and your financial wealth is low, models say borrow to reach your target equity exposure.
  - Felix's caveat: test that "safe human capital" assumption hard, because job loss and market crashes tend to
    come together.
  - His closing question: if your goals work without leverage, do you need it at all?

### 3. Lifecycle allocation: Cederburg's challenge (eps 284, 350, 281, 374)
- **The paper:** Anarkulova, Cederburg and O'Doherty, "Beyond the Status Quo" (SSRN 4590406).
  - Data: 39 developed countries, 1890–2023, more than 2,650 country-years.
  - Method: block bootstrap, which keeps fat tails and mean reversion in the data.
  - Assets: domestic stocks, international stocks, bonds, bills. "Domestic" means *your own country*, not the US.
- **Base case result:** a fixed **33% domestic / 67% international stocks, 0% bonds, 0% bills**, held for life.
  - Utility is flat across a wide range of domestic weights (roughly 15–60%).
- **Equivalent savings rate** (how much you'd have to save under each strategy to match 10% saved in the
  optimal one):
  - A 60/40 domestic stock/bond mix needs **19.1%**.
  - An age-based glide path only lowers it to **9.93%**, so the glide path adds almost nothing.
- **Target-date fund comparison:** the TDF they studied starts at about 90% equity and ends at about **83% bonds
  and bills** in retirement.
  - All-equity strategies reach retirement with about **30% more wealth**.
  - They are *less* likely to run out in retirement, and even the 1st-percentile outcome is better.
- **Why bonds look worse over long horizons:**
  - Average real bond return in the sample: about **1%/yr**.
  - Per-period bond variance at 30 years is **2.3×** the 1-year figure. International stocks fall to about
    **0.75×**, because of mean reversion.
  - Over long horizons, bonds become *more* correlated with domestic stocks than international stocks are.
  - US 10-year Treasuries lost about **30% in real terms** over 2021–22.
- **Is the US special?** If you give it 50% odds, the result is about 60% US / 40% international, roughly world
  market weights. Holding a *home bias* above that needs more than 50% conviction that US outperformance will
  continue.
  - Counterpoint from Cederburg: a market believed to be special gets priced higher, which *lowers* its future
    returns.
- **Correlated human capital:** cut the domestic stock weight by about **3 points for every 0.1** of
  correlation between your income and the home market. The model moves that weight to international stocks,
  never to bonds.
- **Leverage in the model:**
  - At about a **1.4%** borrowing spread, the optimal portfolio is 155% exposure to the same mix.
  - At a **12%** retail margin rate, no leverage.
  - A levered 60/40 is far worse than unlevered all-equity: it needs about **19%** savings to match 10%.
  - Cederburg himself won't lever his retirement savings, because funding dries up in a crisis.
- **Target-date funds in practice (David C. Brown, ep 374):** they trail replicating benchmarks by about
  **1%/yr**. Tactical deviations from the stated glide path cost about **10bp**.

### 4. Factor tilts versus plain cap weighting (eps 129, 213, 227, 394, 416)
- **Historical premiums**, US value-weighted, 1963 to mid-2020 (ep 129):
  - Size **1.58%/yr**, value **1.99%**, profitability **2.59%**.
  - The academic long/short factors are larger.
  - Premiums were positive over 10-year windows about 71% (size), 86% (profitability) and 98% (investment) of
    the time.
  - PWL's 2020 model portfolio held about 30% small caps, against about 10% in the market.
- **Expected after fees (ep 213, 2022):** a broad tilted fund (AVUS) had about **50bp** of extra expected return
  over a total-market fund (ITOT) before fees. That falls to about **38bp** after a 12bp fee gap.
  - Felix's verdict: worth it as a diversifier of independent premiums, but the number is low, and you need to
    be able to live with tracking error.
- **Who should just own the market (ep 227):** the "average" investor should. In ICAPM terms, you tilt *toward*
  or *away from* factors depending on how they hedge your own bad states.
  - Betermier's data on the drift toward value as people age: about **60%** explained by age, **20%** by human
    capital, **20%** by balance-sheet strength.
- **Equal weight is a hidden factor bet (ep 394):** it means small, value and high volatility, plus *negative*
  momentum from rebalancing, plus hidden spread costs from turnover.
  - Over the last 10 years, the S&P 500 equal-weight ETF returned **12.93%** a year against SPY's **15.73%**.
    Since 2003 it is ahead by only **9bp**.
  - Felix's take: if you want those exposures, buy them directly in a factor fund.
- ⚠ **The 2025 internal PWL debate** over tilts vs cap weight, mentioned in the methodology note, **was not found
  in these episodes**. Bortolotti uses cap-weighted all-in-one ETFs (VEQT) for many clients, and Felix runs
  tilted portfolios. That is a disagreement in practice, not a recorded debate. **[unverified as a specific
  episode]**
- **US vs international (ep 416):**
  - Over 30 years the US returned **7.96%** real and ex-US **2.37%**.
  - Asness (as cited): from 1980 to 2020 the US beat EAFE by **2.1%/yr**, but only **0.4%** after adjusting for
    changes in valuation.
  - Their conclusion: hold global diversification as the default.

### 5. Asset location: what you own after tax (eps 6, 72, 416)
- **The principle, which transfers to the US:** a tax-deferred account partly belongs to the government. At a
  50% future tax rate:
  - $400k of bonds in the deferred account plus $600k of stocks in taxable *looks like* 60/40.
  - After tax, it is really **75/25**.
  - Much of the apparent gain from "bonds in the deferred account" comes from quietly taking more equity risk.
- Felix's 2018–19 modelling found that location adds questionable value unless you can forecast returns, and an
  all-in-one fund that rebalances itself can be worth more than optimal location.
- **All-in-one vs component ETFs (ep 416):**
  - The **14bp** fee saving in the example compounds to about $300k on a $1M portfolio over 30 years, which is
    only about **$40k in present value** (at 7%).
  - Drift and bad rebalancing discipline can easily eat it.

### 6. Withdrawal rates: a tool, not a rule (eps 117, 135, 229, 340)
- **Bengen (ep 135):** the 4% rule (1994) came from US data on a 50/50 portfolio. Adding small caps pushed it
  toward about 4.5%, and he now argues it could be higher.
- **Global data (Anarkulova, Cederburg and O'Doherty, ep 229):** for a 65-year-old couple in 2022, 4% had a
  **17.4%** chance of running out before death.
  - A 5% failure tolerance gives **2.26%**.
  - In 18 other countries, 4% failed between **8% and 62%** of the time.
- **Factor tilts and safe withdrawal rate** (Felix's own 50-year backtests, ep 117):
  - US total market **3.1%**, S&P 500 3.35%, market-wide growth 2.85%.
  - US small value **3.6%** (the highest), small growth **1.9%**.
  - Tilting helped, but not up to 4%.
- **The lifecycle model (Ben Mathew, ep 340):** instead of a fixed real withdrawal, amortize total wealth into a
  spending path that *adjusts* when the portfolio falls (his TPAW planner). It trades a hard failure for
  variable spending.

### 7. Leveraged ETFs: corrected views (eps 397, 430, 432)
- **Felix's correction:** he used to say the daily reset itself causes "decay". He no longer does. Volatility
  causes the drag, not the reset.
- **The volatility drag in numbers:** a market that goes +10% then −10% loses 1%. A 2× fund over the same two
  days loses 4%.
- **Costs:** fund fees are about 1%/yr for broad leveraged funds. Total cost including financing can exceed
  **5%/yr**.
- **Single-stock leveraged ETFs** (34 funds, Bessembinder) trail a frictionless levered benchmark by about
  **0.8%/month** for long funds and **1%/month** for short funds.
- **The modest-leverage idea (Sammon and Murray):** for a long-term investor, about **1.25×** fits portfolio
  theory better than 2×. ⚠ No such fund was verified to exist.

## Canadian-only vs what transfers to a US investor

| Canadian-specific (skip or translate) | Transfers to the US |
|---|---|
| RRSP/TFSA/RESP mechanics, the dividend tax credit, the Smith Maneuver, prescribed-rate loans | The after-tax-allocation idea (works the same way with a 401(k)/traditional IRA as the "RRSP" and a Roth as the "TFSA") |
| Home bias toward Canadian stocks (VEQT is about 30% Canada), and the CAD's tendency to fall in crises, which argues against hedging (ep 379) | Cederburg's domestic/international results (built for *any* developed-country investor) |
| VEQT/XEQT and other Canadian ETF products, trading expense ratio disclosure | Risk-profile framework, human capital and pension treatment, factor evidence, equal-weight critique, withdrawal-rate evidence, leveraged-ETF mechanics |
| Pension commuted-value decisions (ep 385, not pulled) | The idea that a defined benefit pension (or Social Security) counts as bond-like wealth |

For US rules on account types and location, use Bogleheads/Kitces, as [[portfolio-methodology-educators]]
advises.

## Applies when
- You are writing the IPS: risk profile, target allocation, the domestic/international split, and whether to
  tilt.
- You are choosing between a target-date fund, an all-in-one fund, or DIY components.
- You are testing a retirement number against something tougher than 4%.

## Breaks when
- **Behaviour.** Cederburg's 100% equity result assumes you never sell. Bortolotti's whole point is that most
  people do. The model's best answer is useless if you abandon it in a 48% drawdown
  ([[canon-kahneman-thinking-fast-and-slow]]).
- **Model risk.** A bootstrap still only shows outcomes from the past. Utility functions, 10% savings rates and
  Social Security assumptions all drive the results. Critics (unnamed here) disputed the paper; Cederburg says
  some hadn't read it closely.
- **Factor premiums shrink or vanish.** A 38bp expected edge with years of tracking error is easy to give up on
  at the worst moment.
- **Leverage needs funding.** Margin and Lombard credit dry up in crises, and the "safe human capital"
  assumption fails at the same time ([[canon-taleb-black-swan]]).

## Practitioner counterpoint
- **The practitioners disagree with the model.** The professors (Cederburg, Gomes) argue for more equity. The
  advisers on the same show (Bortolotti, Bibi) mostly talk clients *down* to 60–70%, because people
  overestimate their tolerance. The model and the practitioners agree on the inputs and diverge on how much
  behaviour costs.
- **The fee incentive cuts both ways.** PWL sells advice, and "DIY 100% equity is risky for beginners" is also a
  reason to hire an advisor. Weigh it accordingly.

## Links
[[portfolio-methodology-educators]] (the 8-step method this feeds) · [[unit-10-personal-finance-operating-system]]
· [[bet-sizing-conviction]] (leverage as sizing; Kelly logic behind "optimal leverage") ·
[[tiger-sisters-wealth-mechanics]] · [[canon-mauboussin-success-equation]] (judge a tilt over decades, not one
bad stretch) · [[canon-kahneman-thinking-fast-and-slow]] · [[canon-taleb-black-swan]]

## The one-line habit
Write your allocation **after tax and including human capital and pensions**, then check that you would still
hold it 30% down.
