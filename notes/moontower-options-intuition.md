# Moontower: Options Intuition, Premium Skepticism, and Sizing in Your Head

> **Sources:** Kris Abdelmessih's *Moontower* Substack (moontower.substack.com). Pulled 2026-11-01 via the public
> archive API: **107 free posts** saved locally: every free post from 2025-10-15 to 2026-11-01, plus 22 evergreen
> options-education posts from 2023–2025 (*Mission Plan #4: Vega & Theta*, *Why Put-Call Parity Is Such A Deep
> Insight*, *Kelly Math Weirdness*, *Limit Orders vs Selling Options*, *Primer #2*, *Learning Options From Scratch*,
> and others). **Paid posts skipped**, including *the "rewind" tail hedge* (2026-10-22), *are the options market's
> odds any good?* (2026-10-29), *"how i invest"* and *sizing directional option trades*. Ideas from those are not
> in this note. Summarized in own words.
>
> **What it adds:** [[portfolio-methodology-educators]] step 6 says "options only with a stated purpose" and names
> implied vs realized vol as the core skill. Moontower supplies the working tools behind that sentence: how to
> read what an option chain is pricing, why selling premium is not "income", and Kelly arithmetic simple enough to
> do in your head.
>
> **Lens:** **Decide** (step 6 options, step 5 sizing), with some **Understand** (market-maker economics) and
> **Run** (greeks P/L attribution). **Methodology steps served: 6 (primary), 5 (sizing), 7 (performance
> attribution).**
>
> **Maps to:** **Course 07** (decisions under uncertainty), **E2** (capital allocation). Extends
> [[bet-sizing-conviction]].
>
> ⚠ **Bias and incentives:**
> - He sells **moontower.ai**, a paid options-analytics platform (dashboards, vol screeners, an MCP connector for
>   LLMs; it runs an annual 20%-off sale). Many free posts end in a tool demo. His thesis that "selling options
>   without analysis earns only average VRP" is true, and it is also the sales pitch for the tool.
> - He also sells **$500/hour consulting calls** and newsletter advertising.
> - The *IncomeSTKd* ETF review (2026-04-15) was **commissioned and paid for by Convexitas**, the fund's sub-advisor.
>   He discloses this and says he kept editorial control. Read it as a sponsored teardown, not an independent one.
> - He co-hosted a "Trading Lab" at the Robinhood Summit (Sep 2026), and the live trade in this note was placed
>   there. A broker-adjacent stage.
> - Against all that, his core message works against activity: most people shouldn't trade options, and "easy
>   returns" pitches are grift. That cuts against what a broker or a tool vendor would want to say.

---

## Core claim

**An option is a bet on volatility before it is a bet on direction.** Every call or put, covered or naked, is a
position in how much the stock will move relative to what the market already priced. Two consequences follow:

1. Option premium is **not income**. It is the market price of a risk you have taken on.
2. Options pay off only when you have a **specific** view on size and timing. A vague view ("I like this stock")
   is better expressed with the stock itself.

Sizing has to sit on top of both. He calls bet sizing one of the most important skills in risk-taking, the one
people are worst at, and one where being far above average takes little effort.

## Framework

### 1. What an option chain prices
- **Straddle ≈ 0.8 × one standard deviation** of the move to expiry. Traders invert it as *vol ≈ straddle × 1.25*.
  An ATM straddle covers about the middle ~79% of a normal distribution. A move beyond the straddle in one
  direction is priced at about **21%**.
- **Event-vol decomposition** (HOOD case, 2026-01-14). Treat total variance to an expiry as a pizza. The earnings
  day takes one large slice (HOOD: an ~8.55% expected move, about 170% annualized for that day). The remaining
  ordinary days share the rest (about 54% annualized). A good first guess for the earnings slice is the **mean
  absolute move over the last 4–8 earnings**. If the ex-earnings term structure then looks smooth, the market agrees
  with that move size. If it looks lumpy, the market is pricing a different move.
- **Screen artifacts.** A 30-day constant-maturity IV can show a name as "cheap" just because earnings sit right at
  the edge of the window and get no weight. Look at the expiry that contains the event.
- **Implied dividends.** The options market prices future dividends. In Sep 2026 NKE options implied a dividend
  about 50% below the current payout a year out, so the market already expected a cut. (Ties to
  [[apply-stock-picking-nke]].)

### 2. Premium selling is not income
- **Theta is not an edge.** It is the cost of gamma, and it can be too cheap or too expensive. His example: a $100
  stock with a 10% chance of reaching $200. The 150 call is actuarially worth about $5, so selling it for $1 is
  selling at 80% below fair value, however steady the theta feels.
- **Selling above realized vol wins on average, along a messy path-dependent route.** Sell that same call for $6 and
  you still lose 10% of the time.
- **The dividend analogy.** A covered-call "cash flow" is like a dividend: it reshuffles returns between buckets. It
  is not extra edge. A high hit rate is not the same as positive expectancy.
- **Average VRP is low-resolution.** The volatility risk premium varies across names (some are cheap and some are
  rich against a baseline) and over time (it shrinks when asset managers crowd into option selling). Selling
  without analysis earns about the **average** premium: roughly fair pay for underwriting a skewed, insurance-like
  liability. Earning more takes labour: research, sizing, execution, management.
- **Limit orders vs short puts** (2024-07-10). He compares a GTC buy limit with a sold put when the stock gaps down
  15% overnight. My reading of the framing, since the worked comparison was an image I couldn't see: a resting
  limit is a free option you give the market. A sold put at least charges for that gap risk. Either way, "outright
  calls and puts are always vol trades".
- **Iron condors** are, in his words, often "marketed as a less risky way to sell a strangle". The wings cap the
  loss but don't change the bet (2026-10-11).

### 3. Greeks P/L attribution for a short straddle (Mission Plan #4, 2024)
Worked example: sell 10 one-month 50-strike straddles at 24% vol.
- Position greeks: about **+$167/day theta**, **$114 vega**, gamma that adds about 232 short deltas per $1 move.
- 24% annual vol ≈ **1.5% per day** (24% / √251).
  - A 1% move nets about **+$138** (theta $167 minus about $29 of gamma loss).
  - A 4% move nets about **−$297** (theta $167 minus about $464).
- Expected edge if fair vol is 20%: 4 vol points × $114 = **~$456 over the whole trade**. Daily P/L swings are
  ~$200 now and ~$600 near expiry. Edge is small next to the noise.
- **Near expiry with the stock pinned at the strike, theta and gamma roughly triple.** Vega shrinks, but the IV
  itself gets jumpier, so the risk does not shrink.
- Size short-vol positions **backwards from the loss you'll accept**, using vega and gamma, not the premium
  collected.

### 4. Specific views and defined-risk structures (NKE live trade, 2026-09-30)
- Stock ~$36. The earnings straddle was ~$3 (~8%), so the 36 call cost ~$1.50 and paid **1-to-1** on an 8% rally.
- The **38.5/39 call spread cost $0.12 to make $0.38: just over 3-to-1** on the same $39 outcome. The outright call
  costs more because it also pays for rallies of 10–20%. Vagueness costs money. A specific view earns leverage,
  at the price of mostly total losses when wrong.
- Break-even probability at 3-to-1 is **25%**. A normal model gives ~21%, but earnings outcomes are closer to binary,
  so a trader's 40% is arguable. **[Unverified, the trader's own estimate.]**
- **Kelly:** f\* = p − q/b = 0.40 − 0.60/3 = **20%** of a $5,000 sleeve ≈ 83 spreads. **He bought ~40 (half
  Kelly).** Defined-risk binaries suit Kelly because the sizing already assumes a total loss when wrong.
- Outcome: NKE fell, and the mirror-image put spread also expired worthless at the close. Judge the process, not
  the result ([[canon-duke-thinking-in-bets]]).

### 5. Kelly in your head (2026-09-13; 2024-03-03)
- **f\* = p − q/b.** Fair coin at even odds → 0. A 60% coin at even odds → 20%. Rolling a 6 at 8-to-1 → 6.25%. A
  −200 favourite you think wins 75% of the time → 25%. Zero or negative → don't bet.
- **Full Kelly is too big for almost everyone,** because your *p* is an estimate. Half Kelly gives up about a quarter
  of the growth and roughly halves drawdowns. Quarter Kelly or less is common in practice. Betting above full Kelly
  destroys compound growth even on a positive-EV bet. He cites the Haghani-Dewey coin-flip study (the Elm Wealth
  team behind the experiment in [[bet-sizing-conviction]]).
- **Kelly favours negatively skewed bets** (*Kelly Math Weirdness*). Two bets with the same 10% expectancy: a
  10%-chance 10-to-1 long shot gets **~1%** of bankroll, while a 90%-chance +22% bet gets **nearly half**. Kelly sees
  variance, not skew or tail shape. That is exactly how option *selling* (high win rate, negative skew) gets
  over-sized. Use Sinclair's skew-adjusted Kelly for options.

### 6. Investing vs trading, and where alpha lives
- **Investing** is pay for patience and risk tolerance (beta). **Trading** is pay for research and labour that must
  out-work the competition, so look for games the best players skip.
- "Anyone promising easy returns is either inexperienced, stupid, or lying" (*So you're interested in trading…*,
  2025-10-22, republished 2026-10-28).
- **Paradox of provable alpha** (2026-11-01): high-turnover strategies with provable edge (HFT) don't want outside
  money. Long-horizon managers can never prove skill statistically, so fees settle wherever the market will bear,
  in what he calls a lemons market ([[canon-akerlof-market-for-lemons]]).
- He calls return forecasts close to pointless. **Vols are more predictable than returns,** so he sizes by
  volatility and assumes he knows nothing about direction.
  - Elm Wealth's Sep 30 2026 assumptions, as he quotes them: US stocks **2.92% real**, 10-yr TIPS **2.91% real**, so an
    equity premium over TIPS of about **0.01%**.
  - The Ibbotson SBBI 50th-anniversary forecast: **5.6% real** for 2026–2050.
  - **[Third-party figures as relayed, not checked against the originals.]**

## Applies when
- You hold, or plan to buy, a stock and are thinking about a covered call, a cash-secured put, or a hedge. Run the
  replication check first: what vol am I selling, and against what fair value?
- You have a dated, sized view (earnings, a Fed meeting, a catalyst) and want defined-risk leverage on being right.
- Any binary or near-binary bet in life or work where you can estimate the odds. Kelly gives the ceiling; size at
  ½–¼ of it.

## Breaks when
- **The probability is made up.** Kelly multiplies whatever error is in *p*. The NKE trade rests on a guessed 40%.
- **Non-binary, path-dependent positions.** Short straddles and covered calls don't have a clean "lose 100%" case,
  so naive Kelly mis-sizes them. Size from vega and gamma scenarios instead.
- **Execution costs.** Every option adjustment crosses a bid/ask. His caveat is that options force you into a chain
  of later decisions. For a small account, wide spreads can erase a 3-to-1 payoff.
- **Taxes and account rules.** Short-dated option gains are mostly short-term in taxable accounts. IRAs restrict
  spreads and margin. Not covered in the posts.

## Practitioner counterpoint
- **tastytrade's** mechanical rules (sell at high IV rank, ~45 DTE, take profit at 50%) treat the average VRP as
  the edge. Moontower's reply: the average VRP is fair pay for tail risk, not alpha, and early exits raise the hit
  rate without removing the tail.
- **The fund industry's view** (Calamos, Convexitas): systematic put-writing in a good wrapper earns a real premium
  for real risk, with tax benefits. Moontower's own sponsored review partly agrees: the wrapper beats a DIY margin
  account on financing, rebalancing and taxes. He still flags untested risk in a vol regime shift.
- Swedroe ([[swedroe-factors-rebalancing]]) reaches the same view of the VRP from the factor side: income for
  bearing risk, not a return of capital.

## Links
[[portfolio-methodology-educators]] (step 6) · [[bet-sizing-conviction]] (Kelly, Elm Wealth experiment) ·
[[apply-stock-picking-nke]] (the same NKE, seen through its option chain) · [[canon-duke-thinking-in-bets]] ·
[[canon-tetlock-superforecasting]] (calibrating *p*) · [[canon-taleb-black-swan]] (negative skew of premium
selling) · [[canon-akerlof-market-for-lemons]] (manager fees) · [[canon-mauboussin-success-equation]] ·
[[rodrigues-derivatives-problem-map]] (the institutional **Run** view of the same greeks) ·
[[trading-floor-mechanics]] · [[swedroe-factors-rebalancing]]

## The one-line habit
Before any option trade, write: **the vol I'm paying or selling, the vol I think is fair, the specific move and
date I'm betting on, and the Kelly fraction, halved.** If you can't fill in the second or third line, trade the
stock or don't trade.
