# Hedge funds and trading: how liquid capital is raised, risked, levered and blown up

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-capital-markets-ma]] [[wss-credit-distressed]] [[wss-private-markets-wealth]] [[wss-rates-macro]] [[wss-technicals-career]]

> **Sources:** **35 long-form videos + 23 shorts** from The Wall Street Skinny (Kristen Kelly, ex-Morgan
> Stanley IBD/converts; Jen Saarbach, ex-Morgan Stanley and Lehman rates sales). Raw at
> `_ingest/raw/2026-10-04/media/wall-street-skinny/` (cluster `trading-hedge-funds` in `_clusters.json`
> and `_clusters_pass2.json`). Pass 1 (13 videos, 19 shorts) covered the Situational Awareness blow-up,
> Imperium IR (Kate Bauman), Fortress (Elizabeth Burton), *Moneyball*, Soros vs. the BoE, Citadel's
> white-label S&T, Millennium's stops, PE vs. hedge fund careers, Tacora HEIs and AB Commodities on
> Hormuz. Pass 2 added the primary sources that pass 1 had to reconstruct: *Options Trading 101* (Andis
> Tanner, 20 years an equity-options market maker), *Trading Equities and Options 101* (Dan Nathan),
> *ETFs 101* (Brian Weinstein, Morgan Stanley Investment Management), *Index Trading Basics*, *Hedge
> Funds 101: L/S Equity* (David Sensa, Islander Capital), *The Real-Life "Billions"* (Kat Sosnick, ex-Tiger,
> Pequot, Perry), the contrarian L/S episode (Avery Sheffield, VantageRock), *Equity Research 101* (Steve
> Haggerty, ex-BofA Merrill), the global macro PM episode (Ashish Goyal), Bridgewater co-CIO Karen
> Karniol-Tambour, Pete Muller (PDT Partners), *Quant Investing 101* (Stacie Mintz, PGIM), Sarah Kapnick
> (JPMorgan climate advisory), *Credit Trading 101*, *Fixed Income S&T 101*, Industry S2E8 (Soros, insider
> trading) and a Sharpe short. Read from other clusters because they fill this note's gaps: the
> basis-trade blowup episode, *Commodities feat. Guy Adami*, Industry S2E6 (GameStop), the Treasury
> futures DV01 short and the 10-year block-trade short. Three Industry recaps (S2E5, S1E4, S1E2) were
> skimmed; they are plot-heavy and changed nothing. Several transcripts are machine-translated and
> garbled, so read quotes as paraphrase.
>
> **Maps to:** Course 02 (Corporate Finance: risk, return, leverage, cost of capital), Course 07 (Data &
> Decisions: Sharpe, sample size, base rates, factor models), Course 11 (Global Strategy & Macro: rates,
> central banks, oil, gold), Exec **E2** (Capital Allocation: the allocator's seat), **E6** (Crisis: forced
> selling, squeezes, margin spirals), **E8** (Stakeholder & Investor Relations: raising and keeping LP
> capital), **E9** (Geopolitics & Macro).
>
> ⚠ **Bias:** both hosts are ex-sell-side, and Jen's career was covering hedge funds. They admire the
> *risk machinery* of the big pod shops and are skeptical of bank regulation and of private marks. Guests
> talk their book: Bauman sells an event-driven fund, Burton sells Fortress credit, Weinstein sells
> active and options-income ETFs, Mintz sells quant equity as a "complement", Lascaratos calls his firm
> "the Citadel of commodities", and Nathan and Adami are TV pundits whose bear case is a brand. The
> L/S guests' best stories (Netflix 2012, Amazon 1997, Rexall) are survivor anecdotes; nobody describes
> their worst trade in detail. Where a figure is a guest's marketing claim, it is flagged.

---

## What this adds to the program

The repo already has the **org chart** of a trading business ([[trading-floor-mechanics]]: buy/sell side,
front/middle/back office, the three sell-side seats, the prop desk as a learning machine). It has the
**statistics of backtests** (`quant-backtesting/`: deflated Sharpe, overfitting, Carver's vol targeting,
factor models) and **2-and-20 as PE carry** ([[tiger-sisters-private-capital-101]]). The rates sibling
([[wss-rates-macro]]) teaches DV01, repo, swaps and the basis trade from the market's side. What the
program lacked was the *economics and failure modes of liquid, levered capital*, and the instruments
those funds use. This note adds:

- **The hedge fund as a business, not a strategy.** The 2% keeps the lights on and AUM drives everything
  else. Liquidity terms decide who survives a drawdown. PDT's seven-year lockup shows the other end of the
  spectrum: a fund confident enough to plan to give its investors' money back.
- **The instruments explained by the people who make markets in them.** How a dealer prices 10,000 calls
  in two minutes, why 16 vol means 1% a day, how a straddle reveals the market's earnings forecast, and how
  ETF creation/redemption keeps a price honest and makes the wrapper tax-efficient.
- **The death and squeeze mechanics.** Leverage, then margin, then forced selling. Short borrow that can be
  recalled, gamma squeezes, and pod stop-losses that make short interest a poor guide to how far a stock
  can run. Situational Awareness, GameStop, the 2007 quant quake and the basis trade are one causal story.
- **Three ways to pick stocks, compared.** Fundamental L/S (variant perception, catalysts, primary research),
  factor quant (systematized fundamentals across 40,000 stocks) and stat-arb quant (forecasting minutes to a
  year). Each has a characteristic way of failing.
- **Regulatory displacement as a general law.** Every constraint on banks moves the activity somewhere less
  regulated: prop trading to hedge funds (Volcker), market making to HFT firms (balance sheet), lending to
  private credit. The hosts and guests reach this independently.

## Concept map

| # | Concept | One-line definition | Why it matters | In repo? |
|---|---|---|---|---|
| 1 | Hedge fund business model | 2% on AUM plus 20% of gains on *redeemable* capital | Fees, liquidity and lockups decide strategy and survival | partial (PE 2-and-20) |
| 2 | Strategy taxonomy | L/S, macro, RV, credit, event, quant, multi-strat | Each sells a different return stream to a different sleeve | partial |
| 3 | Indices and benchmarks | Rule-based baskets that define "the market" | Every alpha claim is relative to one | partial (closing auction in GLOSSARY) |
| 4 | ETFs: creation, redemption, arbitrage | A basket that trades like a stock, kept honest by APs | Passive flows, tax efficiency, bond-market structure | partial (24/5 note, GLOSSARY) |
| 5 | Beta vs. alpha | Market return vs. skill return | Don't pay hedge fund fees for beta | partial |
| 6 | Sharpe and relative-risk metrics | Return per unit of volatility; tracking error, IR | The metrics capital is allocated on | partial (deflated Sharpe) |
| 7 | Options: payoffs, pricing, uses | Rights to buy/sell; vol, skew, Greeks, implied move | Hedging, leverage, sentiment, and dealer flows | n |
| 8 | Fundamental L/S and the research supply chain | Variant perception plus catalysts, sized by conviction | The classic hedge fund; what research is for | partial (stock-picking, research economics) |
| 9 | Short selling and squeezes | Borrowing to sell; recall, rebate, gamma | Why shorts are fragile and squeezes violent | partial (bond shorts in technicals) |
| 10 | Multi-manager pod shops | Many small PMs, tight stops, fund leverage | The dominant form; now moves the market | partial (Citadel pods) |
| 11 | Quant investing | Factor and stat-arb models applied systematically | Removes emotion; fails when crowded | partial (`quant-backtesting/`) |
| 12 | Leverage, margin & forced selling | Borrowed exposure a lender can call | Why being right is not enough | n |
| 13 | Duration & DV01 | Converting a rate move into dollars | Sizing per basis point; futures DV01 | y ([[wss-rates-macro]] §2) |
| 14 | Repo, bank capital & non-bank dealers | Financing bonds with bonds; Basel; Citadel Securities | How leverage is manufactured and where it migrates | partial |
| 15 | Treasury basis trade | Cash vs. futures convergence, short volatility | The most crowded levered trade in rates | y ([[wss-rates-macro]] §11) |
| 16 | Reading rates | Futures-implied Fed odds, QE vs. not, the 10-year | Prices as probabilities | y ([[wss-rates-macro]] §4, §7) |
| 17 | Global macro and central-bank credibility | "Trading countries"; Soros vs. the BoE | Asymmetric payoffs against unsustainable policy | n |
| 18 | Commodities: physical, gold, floor | Marginal barrel, spreads, gold as anti-fiat | Real-economy prices; the pit as a market | n |
| 19 | Capital raising & the allocator's seat | IR as revenue, ODD, lockups, governance | E8 in practice | n |
| 20 | Moneyball as a trading playbook | Mispriced traits, sample size, edge decay | Statistical edge and why copying kills it | partial (Mauboussin) |

---

## 1 · The hedge fund business model: 2-and-20 on redeemable capital

**What it is.** A hedge fund is a pool of investor (LP) money that can trade almost anything, long or
short, with leverage and derivatives. It typically charges about 2% of assets and about 20% of profits.
What separates it from PE is not the fee. It is that **the capital can leave**: redemptions can be daily,
quarterly or annual, against PE's 5–10 year lock.

**How it works.**
- Fee arithmetic, from the hosts: $1bn AUM pays $20m a year in management fees, win or lose. Turn $1bn
  into $3bn and the 20% performance fee earns $400m. Growing AUM from $1bn to $10bn "10x's" the fee
  base, which pays for better traders, which attracts more capital. The IR guest calls this a flywheel.
- **Hurdles** (a minimum return before the 20% applies) and **high-water marks** (no performance fee after
  a loss until the old peak is regained). So in Bauman's words the 2% keeps the lights on.
- Hedge funds are judged on *annual* marked-to-market returns. PE is judged over 5–7 years on appraisals.
- **Lockup as a strategic weapon.** Pete Muller's pitch after PDT's 2012 spin-out from Morgan Stanley: one
  institution, $500m, "our fees are higher than anybody else", and a **seven-year lockup**, because PDT
  intended to take the fund fully internal and hand the money back. It did exactly that after seven years
  (the RenTech Medallion path). Other LPs asked for the same deal and were refused. BlueCrest made the same
  move in 2015, becoming a family office; Ashish Goyal notes its headline returns (150% in one year) come
  from levering partners' own capital.
- **Fee compression**: hedge funds "paid not to be correlated" lagged the zero-rate bull market and cut
  fees. PE, effectively levered long the same market, did not.
- **Tax**: carried interest gets long-term capital-gains treatment. TCJA (2017) set a 3-year holding period
  for that treatment, which bites short-horizon hedge funds and not 5-year PE holds.
- **Payout vs. a bank.** Jen's comparison: a bank trader who makes $100m is paid a small slice, because
  profits are netted across the division; a prop shop keeps what it makes; a hedge fund pays out far more
  per dollar than a bank but can fire you the same day.

**Business significance / value.** Value is captured by the GP through fees on scale. Because the
management fee scales with AUM rather than skill, a hedge fund's equity value is mostly a function of
*sticky AUM*. Hence the push into longer-locked products, SMAs and funds of one (§19). The firms with the
best records do the opposite: they shrink outside capital to keep the edge for themselves.

**Forces & impact.** Low rates helped levered-beta strategies (PE) and hurt hedge funds whose job was to
hedge beta away. Higher rates and wider dispersion bring demand back. At iConnections 2026 equity L/S and
macro funds were getting the meetings while private credit was "less sexy". Second-order: a talent war,
with reported $100m sign-on packages for PMs moving between Citadel, Millennium and Balyasny.

**With vs. without.** Without redeemable capital, hedge funds could hold through drawdowns the way PE does,
but they would lose their selling point (liquidity) and their discipline (public marks). PDT's lockup shows
a third path: patient capital bought with a track record. The structure is a trade between
**accountability and survivability**.

**Applies when / Breaks when.** Works when returns are uncorrelated enough to justify fees and LPs are
patient. Breaks when a drawdown triggers redemptions, which force sales, which deepen the drawdown: a run
on the bank, in the hosts' words.

**Channel example.** *Private Equity vs. Hedge Funds* (2023); *Head of Investor Relations at $3 Billion
Hedge Fund Tells All*; *Pete Muller on Building… PDT Partners*; *Portfolio Manager at World's Top Hedge
Funds… Global Macro* (BlueCrest).

**Counterpoint.** The hosts frame PE's structure as superior. Since 2023 PE has had its own liquidity
reckoning (continuation funds, gated evergreen vehicles): locked capital postpones the reckoning rather than
removing it. Muller's seven-year pitch worked because PDT already had a 20-year record inside Morgan
Stanley. It is not a template for a new manager.

**Links:** [[tiger-sisters-private-capital-101]] · [[trading-floor-mechanics]] §2, §5 ·
[[canon-jensen-meckling-agency-theory]] · `quant-backtesting/research/renaissance-technologies.md`.

---

## 2 · The strategy taxonomy: what each fund is actually selling

**What it is.** "Hedge fund" is a legal and fee wrapper, not a strategy. Each style produces a different
return stream and sits in a different allocator bucket.

**How it works.**
- **Equity long/short.** Long the companies you like, short the ones you don't (§8). Two sub-species
  (Sensa): *long-biased* single-manager funds that keep net long exposure and want some market beta, and
  *beta- or factor-neutral* pods whose long and short books match by size, sector and factor (§10).
- **Global macro.** Ashish Goyal: macro is "trading countries". For each of the G7 and EM Asia he reads the
  cycle, the central bank, the fiscal position and external balances, then asks whether the curve, the long
  end, the currency and the equity index are priced right (§17).
- **Relative value.** Two related instruments mispriced against each other, levered heavily: the basis trade
  (§15), oil time spreads (§18), index vs. single-stock volatility (dispersion, §7).
- **Credit, convertible arbitrage.** Ken Griffin started Citadel as a convert-arb fund. In 2008 convert-arb
  funds that delta-hedged bank convertibles blew up when the short-selling ban removed the hedge.
- **Event-driven** (Imperium, ~$3bn, per Bauman), five buckets: transactional (mergers), structural
  (spin-offs), stressed/distressed, legal/regulatory, and activist (Imperium avoids it). The first two are
  pro-cyclical, the third counter-cyclical, so a diversified event book has a built-in hedge.
- **Quant** (§11). Mintz's three types: high-frequency (nanoseconds), trend-following, and fundamental factor
  investing. Muller adds statistical arbitrage over horizons "from a minute to a year".
- **Multi-strat / multi-manager** (§10). Goyal: teams are sliced by asset class (equity, credit, commodities,
  macro) and by style (directional, relative value, systematic), in any combination.
- **"Hedge funds that aren't."** Burton notes credit managers who never short, and funds that drop the word
  "hedge" when allocators exclude the label.

**Business significance / value.** Allocators buy *a role in a portfolio*, not a fund. Bauman's advice is to
arrive with the LP's memo already written: which role you fill and what you replace.

**Forces & impact.** Rate regimes and deal cycles rotate which buckets are "on". Labels follow allocator
fashion: after 2008 "distressed" became "special situations", then "credit opportunities".

**With vs. without.** Without the taxonomy an LP compares a merger-arb fund's 8% to the S&P's 20% and fires
it, missing that the fund's return stream is uncorrelated and its drawdowns shallow.

**Applies when / Breaks when.** Useful until style drift: a "macro" fund that is really levered long tech, or
an RV book whose two legs both lose (Situational Awareness, §12).

**Channel example.** *Hedge Funds 101 | Long/Short Equity Edition*; *Global Macro* (Goyal); *Quant Investing
101*; *Head of IR at $3 Billion Hedge Fund*.

**Counterpoint.** Bauman's "all five buckets firing" is a fundraising line delivered at a capital-intro
conference. The taxonomy also understates convergence: pods now run L/S, macro and RV teams under one roof.

**Links:** `quant-backtesting/research/citadel.md`, `…/bridgewater.md`, `…/renaissance-technologies.md` ·
[[sec-filing-intelligence]].

---

## 3 · Indices and benchmarks: what "the market" means

**What it is.** An index is a rule-based list of securities with weights, published as a single number. "The
market went up" almost always means the S&P 500. You cannot buy an index directly; you buy a fund, an ETF
(§4) or a futures contract that tracks it. Indices exist for two reasons: to give passive investors the
market's return cheaply, and to give active managers a yardstick.

**How it works.**
- **Construction, as the hosts describe it.** The S&P 500 is market-cap weighted and committee-selected, with
  size, liquidity and profitability screens (positive earnings over the last four quarters). So it is "a
  little better than other stocks": a quality filter, not a neutral sample. The Nasdaq indices lean to tech.
- **The bond equivalent** is the Bloomberg (formerly Lehman, then Barclays) Aggregate: market-value weighted,
  investment grade only (BBB-/Baa3 or better), at least a year to maturity, a minimum issue size, and a large
  Treasury share, so it moves with monetary policy. It also holds agencies, MBS and ABS.
- **Benchmark vs. absolute return.** Long-only mutual funds and pension sleeves are judged against an index;
  most hedge funds are judged on absolute return, depending on the mandate. The hosts' endowment example:
  35–40% equities, 10–15% bonds, 30–35% alternatives.
- **Concentration.** Karniol-Tambour, the day after DeepSeek (January 2025): the Magnificent 7 were about a
  third of the S&P 500, other tech about 12% more. Almost half the "diversified" index was a bet on one
  theme, which is why a single AI headline moved it.
- **Access.** Retail uses index funds and ETFs; institutions also use index futures, which need margin, are
  levered and come in large contract sizes. Dan Nathan's first job had a phone line to the CME floor for
  index futures beside one to the NYSE.

**Business significance / value.** Index providers sell licenses; fund sponsors sell cheap access; active
managers sell beating it. The index's rules decide who must buy a stock (inclusion) and therefore move prices
on their own (see [[wss-capital-markets-ma]] §8 on index inclusion).

**Forces & impact.** Passive flows buy every day regardless of news. Guy Adami and Avery Sheffield both
argue this, plus a perceived Fed backstop, explains a market that "takes the stairs up and the elevator
down". Adami's warning: "when passive becomes active", it is on the way down. Concentration raises single-name
risk inside nominally diversified products.

**With vs. without.** Without indices, "beat the market" is unmeasurable and passive investing impossible.
With cap-weighted indices, money flows to what has already risen, so the benchmark itself becomes a
momentum strategy.

**Applies when / Breaks when.** A benchmark is meaningful when it matches the manager's opportunity set. It
breaks when a manager picks a flattering one, or when concentration turns the index into a sector bet.

**Channel example.** *Index Trading (SPX, NASDAQ, etc.) Basics and Why You Should Care*; *Bridgewater Co-CIO
Karen Karniol-Tambour*; *Commodities feat. Guy Adami*.

**Counterpoint.** The index episode is short, machine-translated and loose: it calls the S&P ETF "SPX" (the
index ticker; the ETF is SPY), puts Treasuries at "about a third" of the Agg (closer to 40–45%) and garbles
the hedge fund fee. The actual S&P earnings rule requires a positive sum over four quarters *and* a positive
latest quarter. Treat it as orientation only.

**Links:** GLOSSARY "Closing auction" · [[market-structure-24-5-trading]] · [[wss-capital-markets-ma]] §8 ·
[[unit-10-personal-finance-operating-system]].

---

## 4 · ETFs: a basket that trades like a stock, kept honest by arbitrage

**What it is.** An exchange-traded fund is a wrapper that delivers a basket of securities (stocks, bonds,
commodities, options strategies) in a single share that trades on an exchange all day. Weinstein's two
distinguishing features versus a mutual fund: **intraday trading** and **tax efficiency**. The US market is
roughly $11–12tn across about 10,000 funds, per the hosts.

**How it works.**
- **The mutual fund problem.** A mutual fund prices once, at the 4pm NAV. If $100 comes in and $50 goes
  out, the PM must invest the net $50 (or sell holdings to meet net redemptions). Those sales realize
  capital gains that every holder is taxed on.
- **The ETF's three cases** (Weinstein):
  1. *Normal day*: buyers and sellers trade existing shares with each other on the exchange. The underlying
     never moves and the PM never sees it.
  2. *Excess demand*: an **authorized participant** or lead market maker (Jane Street, Citadel, Virtu, some
     banks) **creates** shares by delivering the basket (say the 500 S&P stocks at index weights) to the fund
     in exchange for new ETF shares.
  3. *Excess selling*: the AP **redeems** ETF shares and receives the basket back; the shares are destroyed.
- **Arbitrage keeps the price honest.** If the ETF trades above the value of its basket, the AP buys the
  basket, creates shares and sells them; below, it does the reverse. Kristen recalls Michael Lewis's
  "ham sandwich" from *Going Infinite*: Jane Street buying the bread and ham when they were cheaper than the
  sandwich. Holdings are published daily (mutual funds publish monthly or quarterly), because market makers
  cannot hedge what they cannot see. Non-transparent ETFs have largely failed for this reason.
- **Premiums and discounts are the price of liquidity.** If everyone wants out, a basket worth $100 may only
  fetch $98. Bond ETFs traded at deep discounts in March 2020; when the Fed announced it would buy
  investment-grade bonds, they flipped to premiums because APs could not source bonds fast enough.
- **The tax trick.** In a redemption the fund can hand the AP its lowest-cost-basis lots. The gains leave the
  fund without a sale, so they are never realized. This matters most in equities, where gains are larger.
- **Pricing.** Market makers' algorithms continuously value the basket. Where the underlying trades often, the
  spread can be a penny or "locked". Weinstein's "garage ETF" of Uruguayan local bonds might be fair at 50
  but quoted 47 bid, 53 offered, and nobody trades. "Trading begets trading."
- **Launch and primary/secondary.** Launching is like an IPO: issue, say, 10,000 shares at $50 to the market
  maker, cash goes into "the box", then secondary trading follows. Creates and redeems are the ongoing
  primary market. Before launch the sponsor's capital-markets team lines up the lead market maker; if market
  makers won't quote it, the fund dies. Big blocks ($100m of a loan ETF) are priced as risk by a market
  maker who hedges with HY or S&P exposure for days.
- **Fees.** LQD's expense ratio is 14bp; active fixed-income ETFs run roughly 15–40bp; old mutual funds were
  over 1%. Weinstein says fees have now stabilized.
- **Leveraged and inverse ETFs** (TBT, 2x short the long bond) "don't move like you'd predict": daily
  rebalancing means they buy on up days and sell on down days. Tanner adds that this rebalancing amplified
  MicroStrategy's volatility. For hedging, not holding.
- **Why mutual funds survive.** Most 401(k) plans still use them, some investors want privacy, and Europe's
  UCITS/SICAV wrappers are mutual-fund style.
- **Hot categories (2024).** Options-income ETFs that own an index and sell calls (Weinstein calls them the
  cousin of 0DTE), hedged-equity ETFs that buy puts, and active bond ETFs.

**Business significance / value.** Scale and first-mover advantage dominate. Once one S&P or IG ETF is the
liquid one, a clone has little reason to exist, though dozens of new issuers launch hundreds of funds a year.
The arbitrage profit goes to the APs and market makers; the sponsor earns the expense ratio. The structure
**changed the bond market**: LQD, HYG and TLT let investors trade baskets of credit and duration that were
untradeable as individual bonds. Weinstein's line: if you don't know the price of a basket of bonds, you
probably shouldn't be trading bonds.

**Forces & impact.**
- SEC Rule 6c-11 (2019; the transcript says "60/11") let managers launch ETFs without individual exemptions,
  which opened the door to active and mutual-fund-clone ETFs.
- Post-2008 balance-sheet rules explain who the market makers are: Weinstein says in 2006 the banks would
  have done it; now it is too balance-sheet intensive, so HFT firms dominate.
- Passive concentration gives a few sponsors (BlackRock, Vanguard, State Street, Fidelity) most proxy votes.
  Weinstein calls it a real issue, not an evil empire.
- Under 24/5 trading, bond ETFs become the only credit price at 2am ([[market-structure-24-5-trading]]).

**With vs. without.** Without ETFs, retail diversification means mutual funds (end-of-day prices, embedded
tax drag) and institutions trade bonds one CUSIP at a time. With them, a liquidity mismatch appears: a share
that trades every second wrapped around bonds that trade weekly. In calm markets the AP absorbs it; in a
panic the discount shows it.

**Applies when / Breaks when.** Works when the underlying is liquid enough for APs to hedge and the basket is
transparent. Breaks when the underlying market shuts or seizes (March 2020 credit, emerging markets), when
the AP steps back, or when a leveraged ETF meets a choppy market.

**Channel example.** *Exchange Traded Funds (ETFs) 101* (Brian Weinstein, MSIM, November 2024).

**Counterpoint.** Weinstein runs an ETF business and pitches his own funds (Parametric's options-income ETF,
Eaton Vance active bond ETFs) on air, including a "best tax treatment" claim against unnamed competitors.
His statement that ETFs are "not really allowed" in 401(k)s overstates it: the barrier is plan design and
recordkeeping, not a legal ban. One quote ("QQQ at 109.48") is garbled: the ticker he was reading was a
bond ETF, given his own description. Treat the ETF-vs-mutual-fund fee gap as partly selective: large passive
mutual funds can be as cheap.

**Links:** GLOSSARY "ETF premium / discount to NAV" · [[market-structure-24-5-trading]] ·
[[wss-capital-markets-ma]] §8 · [[wss-private-markets-wealth]] §8 (semi-liquid wrappers, the same
liquidity-mismatch problem in private assets).

---

## 5 · Beta vs. alpha: don't pay 2-and-20 for the market

**What it is.** **Beta** is how much a portfolio moves with the market: 1 moves with it, above 1 amplifies it,
below 1 dampens it. **Alpha** is the return left after beta, attributed to skill.

**How it works.** Bauman: beta can be bought almost free through an index ETF (§4), so hedge fund fees are
only justified by alpha. Imperium targets a **beta of 0 to 0.1** by hedging out industry and macro exposure,
with 20–35 positions carrying 70–80% of the risk in "less followed" companies of a couple of billion dollars.
Weinstein's version for long-only: pay basis points for beta, pay more for active only where it can earn its
keep (high yield, loans, EM, small caps). Mintz: in large-cap US "you're not getting a ton of alpha", so take
little risk there. Karniol-Tambour adds a sharper claim (§6): a benchmark-hugging portfolio "inherits" the
benchmark, so the same skill earns more when unconstrained.

**Business significance / value.** Beta neutrality is what the LP pays for. A beta-0 fund returning 8% adds
return without adding market risk. Apollo's investor-day meme shows the fight over attribution.

**Forces & impact.** In a one-way bull market beta was cheap and good, and alpha looked expensive. When
dispersion rises, stock selection matters again. Karniol-Tambour: correlations between individual stocks are
low even when indices feel tightly linked, so the opportunity exists below index level.

**With vs. without.** Without the split, a levered-long manager in a bull market looks like a genius and
charges alpha fees for beta.

**Applies when / Breaks when.** Beta is estimated from history. It breaks when correlations jump in a crisis
and "low beta" books suddenly move with the market because everyone sells the same crowded names.

**Channel example.** *Head of IR at $3 Billion Hedge Fund*; *ETFs 101*; *Quant Investing 101*; *Bridgewater
Co-CIO*.

**Counterpoint.** A beta of 0.1 "to the S&P" can hide factor betas (momentum, crowding) that behave like market
risk in a squeeze (§10, §11). Measured alpha is only as good as the benchmark chosen.

**Links:** [[bloomberg-terminal-instrumentation]] · `quant-backtesting/research/aqr-capital.md` (factors as
"alternative beta") · `…/factor-models-regime-detection.md`.

---

## 6 · The Sharpe ratio, relative-risk metrics, and the arithmetic of losses

**What it is.** The Sharpe ratio is excess return over the risk-free rate divided by the volatility of returns:
how much you earned per unit of turbulence. Above 1 is good, 2 better, 3 excellent. Benchmark-relative
managers use the cousins: **tracking error** (how far returns deviate from the benchmark) and the
**information ratio** (outperformance per unit of tracking error).

**How it works.** Jen's arithmetic: risk-free 5%, fund returns 10%, excess 5%.
- Divide by 2% volatility: Sharpe 2.5, "you look like a hero".
- Divide by 20% volatility: Sharpe 0.25, like clinging to a mechanical bull.

Reported figures (WSJ, summarized by the hosts): Millennium about **2.6** on $69bn AUM with one down year;
peers about **1.1**; the S&P about **0.3**.

Why volatility deserves the penalty: losses compound asymmetrically. Down 50% then up 25% leaves you at
0.5 × 1.25 = 0.625, still down 37.5%. Recovering −50% takes +100%.

**Win rates are low even for the best.** Dan Nathan: the best traders win about 52% of the time. Steve
Haggerty cites Alpha Theory's data that only about half the stocks in a typical PM's portfolio move the right
way. Returns come from sizing winners bigger than losers, not from being right often.

**Relative metrics in practice.** Mintz (PGIM quant equity, ~$60bn): clients care about tracking error and
information ratio, "bang for your buck". Karniol-Tambour's Bridgewater research: with the same stock-picking
signal, a benchmark-relative portfolio beats the benchmark reliably by about 3% a year (the transcript says
"every day") but inherits everything else the benchmark does; an unconstrained portfolio has huge tracking
error but outperforms more.

**Business significance / value.** Sharpe is the metric capital is allocated on inside pod shops (§10) and by
LPs (§19). A smooth 5% stream can be levered into 15%, which is the pod-shop model. Tracking error is the
budget long-only allocators give active managers.

**Forces & impact.** Higher risk-free rates raise the bar. Sharpe rewards *suppressing visible volatility*,
which pushes managers toward strategies with smooth returns and rare large losses (short volatility, §15) and
toward illiquid assets marked infrequently. Tracking-error budgets push long-only managers toward index
hugging, which Karniol-Tambour argues wastes their skill.

**With vs. without.** Without a risk-adjusted metric, raw return wins, and raw return is easiest to get by
adding leverage or selling tail risk.

**Applies when / Breaks when.** Valid for roughly normal, frequently marked returns. Breaks for (a) nickels in
front of steamrollers, (b) appraisal-marked private assets, (c) backtests where many trials inflate the best
Sharpe (deflated Sharpe in `quant-backtesting/`).

**Channel example.** *How do Sharpe Ratios work?* (short); *Apollo's Quest to Double AUM, Sharpe Ratios, and
the CAIS Summit*; *Quant Investing 101*; *Bridgewater Co-CIO*.

**Counterpoint.** The S&P's "0.3" depends on the period; long-run estimates are nearer 0.4–0.5. Millennium's
2.6 is self-reported via press and net of a pass-through expense model the hosts don't mention.
Karniol-Tambour's unconstrained-portfolio claim is also the case for Bridgewater's own product.

**Links:** `quant-backtesting/research/lopez-de-prado.md` · `…/harvey-liu-zhu-backtesting-pitfalls.md` ·
`…/robert-carver-systematic-trading.md` · [[canon-taleb-black-swan]] · [[canon-mauboussin-success-equation]].

---

## 7 · Options: payoffs, how a dealer prices them, and what they reveal

**What it is.** A **call** is the right to buy at a set price (the strike) by a set date; a **put** is the right
to sell. The buyer pays a **premium** and can lose no more than that. The seller collects the premium and takes
the risk. An option's price depends on the stock price, strike, time, rates and above all **implied
volatility**: the market's estimate of how much the stock will move.

**How it works.**
- **Three uses for an investor** (Nathan, with Microsoft at $100 as the running example):
  1. *Yield enhancement.* Own the stock long term and sell an out-of-the-money call every couple of months: a
     "synthetic dividend". You keep the premium if the stock stays below the strike.
  2. *Leverage with defined risk.* Buy calls into catalysts (earnings next week, a user conference after). The
     most you lose is the premium.
  3. *Insurance.* Buy the 95 put for $2: below $93 (strike minus premium) you are protected, so the worst
     case is $7. Doing it constantly drags returns, because you want the insurance to expire worthless.
  - *Zero-cost collar*: sell the 110 call for $2, buy the 90 put for $2. You keep gains up to $110 and are
    protected below $90. The same structure protects the stock leg of an M&A offer ([[wss-capital-markets-ma]]
    §12: Netflix/WBD's $4.50 stock component and its 0.046 fixed ratio below $97.91).
- **Two Greeks that matter to most people** (Nathan): **delta**, how much the option moves per $1 in the stock,
  and **theta**, how much value it loses each day. A call that doesn't rise with the stock is delta and theta
  at work.
- **The 16 rule** (Tanner): annualized vol ÷ 16 ≈ daily move, because there are about 256 trading days and
  √256 = 16. So **16 vol ≈ 1% a day, 32 vol ≈ 2%**, and 100 vol ≈ 6% a day, every day, which almost no stock
  sustains. MicroStrategy traded around 120 vol.
- **The implied move from a straddle** (Nathan): with Microsoft at $100 reporting Thursday night, the Friday
  $100 call costs $2 and the put $2. A straddle (both) costs $4, so the stock must close above $104 or below
  $96 to profit: a **4% implied move**. If it has averaged 2% over eight quarters with a 4% maximum, the
  options are expensive. Rule: at-the-money straddle ÷ strike ≈ expected move.
- **How a dealer prices a request** (Tanner, 20 years a single-stock market maker). A hedge fund wants 10,000
  Target calls a week before earnings and asks three banks. In about two minutes the trader weighs existing
  inventory in Target and correlated retailers (Walmart, Costco), how much stock the hedge needs and what it
  costs, the loss if the stock moves 50%, and who else might sell. He shows $2.00 against rivals' $2.05 and
  $2.10, wins, earns a few cents, then **delta-hedges** by trading stock. Index desks get asked for $5–10bn of
  S&P puts; the binding constraint is the bank's loss limit if the S&P falls 10%.
- **Pricing earnings with no history.** Instacart's first report: the desk used DoorDash, Grubhub and
  similar-sized tech names, adjusted for financial and operating leverage, got 9–11%, and offered at about a
  13% implied move (the transcript's "133%" is a garble). The client didn't trade: too wide.
- **OTC vs. listed.** Big banks prefer over-the-counter trades because nobody else sees the 10,000 calls, which
  buys time to hedge. Tanner's split: about 50/50 OTC at a bulge bracket, about 95% listed at a small bank.
  Clients accept bulge terms because the same bank controls IPO allocations, prime financing and corporate
  access. A client who "sprays the street" leaves a footprint and gets policed.
- **Skew as sentiment** (Nathan). Normally downside puts cost more than equally distant calls, because
  investors pay for protection. In 2024 Nvidia's 10% out-of-the-money calls cost more than its puts: demand to
  own it any way possible.
- **Put/call ratio** (pass 1). The equity ratio normally ran about 0.6–0.7 (CBOE 2006–2019); 0.4 means far
  more call buying than usual. The contrarian read: crowded positioning sets up disappointment.
- **Index puts don't hedge single names (dispersion).** Index vol is lower than the vol of its members because
  their moves offset. Desks trade the gap as a basis (long single-name vol, short index vol). Situational
  Awareness hedged a concentrated AI book with S&P puts that barely moved (§12).
- **The evolution of expiries.** Monthly (third Friday), then quarterly, LEAPs (about two years), weeklies,
  and now daily (0DTE), mostly on SPY. Listed single-stock options go out about 2.5 years; S&P options to 10
  years for variable-annuity hedgers. Convertibles run five years, so convert-arb funds hedge a long option
  with shorter ones.

**Business significance / value.** End users: hedge funds (the main single-stock buyers, around catalysts),
insurers (variable annuities), pensions and mutual funds (protection and income). The dealer earns the spread
and the **volatility risk premium**: Sensa's blunt version is that implied vol is usually higher than
realized, so buyers overpay and dealers "should always come out ahead" if they hedge well. Since 2006 the flow
has shifted from hedge funds buying options to investors *selling* them for yield, amplified by zero rates.
Retail made options a profit center for brokers: Nathan cites Robinhood getting about half its quarterly
revenue from options, because stocks now trade at zero spread while options still have one.

**Forces & impact.**
- Spreads compressed from nickels, dimes and quarters to pennies; Citadel, Jane Street and Susquehanna took
  share from banks.
- **Dealer hedging moves the underlying.** A dealer short calls must buy stock as it rises. In thin names this
  is decisive: Tanner's example is a $200m company where a client wants $10m of options, 5% of the company.
  In May–June 2020, bankrupt energy names (Chesapeake, Oasis; Hertz outside energy) ran 10–20x on retail
  buying, and desks short calls had to buy stock at a $3–4bn market cap in companies they knew were worth
  nothing. This is the gamma squeeze GameStop made famous (§9).
- Buffett sold long-dated index puts (S&P, Nikkei, Euro Stoxx) before 2008 on the view that long-dated vol
  was overpriced and the premium was useful float.

**With vs. without.** Without options, a fund hedges only by selling or shorting, which is crude, taxable and
capital-hungry. Without implied vol and skew, the market's forecast of an event's size is invisible.

**Applies when / Breaks when.** Options price risk well when the dealer can hedge continuously in a liquid
underlying. They break when the hedge itself moves the market (small caps, squeezes), when realized vol
explodes past implied (short-vol sellers), or when index hedges meet dispersion.

**Channel example.** *Options Trading 101* (Andis Tanner); *Trading Equities and Options 101* (Dan Nathan,
August 2024); *Hedge Funds 101* (Sensa on rarely using options); short *Equity Put/Call Ratio at Extreme
Lows*.

**Counterpoint.** Both guests say most people should not trade options (Tanner: 98–99% of retail and 75% of
professionals). That is honest, but they also come from the selling side of a business that profits from
retail buying. Nathan's Robinhood figure is closer to half of *transaction-based* revenue (Q2 2024), not
half of total revenue. The 16 rule is an approximation (√252 ≈ 15.9) and assumes normal moves; earnings days
are not normal.

**Links:** [[canon-kahneman-thinking-fast-and-slow]] (herding) · [[canon-tetlock-superforecasting]] (implied
move as a forecast to score) · [[canon-taleb-black-swan]] · [[wss-capital-markets-ma]] §12 ·
`quant-backtesting/research/main-compilation.md`.

---

## 8 · Fundamental long/short and the research supply chain

**What it is.** Fundamental L/S funds buy companies whose value they think the market underrates and short
those it overrates, using their own research. The edge they claim is a **variant perception**: a view that
differs from consensus, is right, and has a **catalyst** that will make the market notice. Sell-side research
is one input; it is not the edge.

**How it works.**
- **Portfolio shape** (Sensa, Islander Capital, long-biased TMT). Per $100 of capital: a long book of about
  $100 across 15–20 names, half the money in the top five or six, held for years; a short book of $40–60
  across 10–20 more catalyst-driven names, held for under a year. **Gross exposure** (long + short) stays at
  150% or less; **net exposure** (long − short) around 40–60%. Pods run gross at 300–500% (§10). Sosnick ran
  a consumer book of up to $1bn at Perry Capital with 20–30% leverage.
- **Primary research is the differentiator.** Sensa: models and DCFs are table stakes ("if our business was as
  simple as building a model computers would do it"). The edge comes from networks: CEOs and CFOs (be one of
  the few investors they remember, by knowing what keeps them up at night), former executives, disruptors.
  Sell-side analysts are used to read *other investors*: they talk to 50 funds and know both the bull and bear
  case. Sosnick's version is shoe-leather: store visits with Costco's CEO and CFO every six weeks, and her
  "back of the plane" rule (watch what ordinary travelers wear and open first when Wi-Fi returns).
- **Case: Netflix 2012** (Sensa). After the Qwikster botch, 35 sell-side analysts covered it, three rated it a
  buy, short interest was over 20%, and the company was worth about $3bn. His fund bought about 1% of it. The
  inputs: Disney, CBS and Fox said Netflix was no threat and they would sell it more content (playing the
  quarterly game while Netflix played the ten-year one); AMC's shows gained about 100% in new-season viewers
  after their back seasons hit Netflix. The math: about 25m subscribers heading to 30m; HBO had about 30m US
  subscribers and its US business was worth $8–10bn; so "the HBO of the web" at $3bn was cheap. He rebuilt in
  2016 when a post-launch churn spike in new markets was misread as maturity; the stock roughly doubled in 12
  months. The lesson he draws: public markets over-extrapolate every data point.
- **Case: Amazon 1997** (Sosnick at Pequot). She nearly skipped the roadshow ("selling books online?"), stayed
  after hearing Bezos laugh, and then attended every breakfast and one-on-one because **IPO allocation depends
  on fund size and how many meetings you show up for**.
- **Contrarian process** (Sheffield). Stocks now move less on fundamental value than on the data point the
  crowd anchors to. Her process reverse-engineers that: where is value, what is the anchor, what catalyst
  shifts it, and how much pain sits on the other side. **Asymmetry** is not just a low multiple; it is how
  crowded the other side is and how big the move after the catalyst. Her August 2024 example: US legacy
  airlines at 4–6x earnings and European carriers at low single digits after a summer of overcapacity, while
  weak low-cost rivals were restructuring and an activist was forcing capacity cuts. Capacity down, fares
  stabilize, multiples re-rate; the stocks rallied. Idea sourcing starts at the extremes of valuation and
  sentiment, then waits for real-time data (weekly capacity and pricing feeds) or a management statement
  ("we're serious about spending") to turn.
- **The research supply chain** (Haggerty, ex-head of research at BofA Merrill). The analyst's job is to decide
  whether a stock is **mispriced** against intrinsic value, not whether a quarter beats. "The sell side advises
  and the buy side invests." Sector teams of 3–5 cover 15–25 stocks, about six per person, chosen by size and
  liquidity because the bank earns from trading them. Research has no P&L of its own; it is paid through
  commissions on trades the ideas generate, prime brokerage, and contributions from banking and wealth
  management ([[wss-technicals-career]] §4.17 covers the economics). Its three functions: inform, advise,
  facilitate (corporate access). Funds steer commissions to banks for research, models and conferences;
  small funds outsource execution (Sensa uses BTIG).
- **Filings and disclosure.** Managers above the 13F threshold file their US long holdings within 45 days of
  quarter end (March 31 → May 15); shorts, cash and most derivatives are excluded. Some European countries
  require short disclosure, privately at one threshold and publicly at a higher one. Companies can also watch
  custodial reports and see stock leaving a prime broker.

**Business significance / value.** This is the hedge fund most people picture, and the training ground for
Tiger, its "cubs" (Sosnick reported to Steve Mandel, later Lone Pine) and most of today's single managers.
Value is created when research changes the price toward the truth; it is captured by the fund through
concentration in its best ideas. Sensa's view of the PM's job: know which five ideas have a near-term variant
perception and put the capital there.

**Forces & impact.**
- Information arbitrage is gone. Haggerty used to collect GM's earnings release in the GM building lobby; Reg FD
  (2000), Bloomberg, FactSet and email erased that edge, so it moved to models, conferences, expert calls,
  and now unstructured data with Python and LLMs. Nathan, who started at SAC, calls qualitative stock picking
  largely "out the window".
- Large-cap volatility has risen (Netflix ±15% in a day, Meta +10% after hours), which lets big funds generate
  alpha in liquid names (Sosnick).
- Companies stay private longer (about 1,200 unicorns), so public L/S funds meet growth later; Fidelity,
  Wellington and T. Rowe now run private research teams and crossover funds (Haggerty).
- Pods' factor-neutral, levered books create non-fundamental volatility (§10). For a long-biased fund with a
  healthy balance sheet, Sensa calls that opportunity.

**With vs. without.** Without fundamental L/S, prices are set by index flows, momentum and factor models, with
nobody paid to find the Netflix of 2012 or short the Rexall of 1999 (§9). With it, the market gets price
discovery, but from funds that are themselves fragile to squeezes and redemptions.

**Applies when / Breaks when.** Works when the variant view is right *and* a catalyst arrives within the
fund's holding period. Breaks when the market anchors elsewhere longer than you can wait (Sheffield: stocks
whose earnings haven't changed since 2022 doubled), when a secular decline masquerades as a dip (Sosnick: Bed
Bath & Beyond was a falling knife, Disney+ panic was a dip), or when you mistake charisma for analysis.

**Channel example.** *Hedge Funds 101 | Long/Short Equity Edition* (David Sensa; transcript spelling varies);
*The Real-Life "Billions"* (Kat Sosnick); *Succeeding as a Contrarian Equity L/S PM* (Avery Sheffield, January
2025); *Equity Research 101* (Steve Haggerty).

**Counterpoint.** Every case on air is a winner told years later. Sosnick frames the Amazon call as intuition
(and as a female edge); she also misdates it, saying Amazon listed as the bubble was deflating, when it IPO'd
in May 1997, years before the peak. Sensa's Netflix math is a back-of-envelope comp to HBO; it worked because
the business then grew far beyond HBO, not because the comp was precise. Haggerty's claim that hedge funds
won't hire sell-side analysts with more than 3–4 years is a generalization, as Sheffield's own path shows.

**Links:** [[tiger-sisters-stock-picking]] · [[wss-technicals-career]] §4.17 · [[trading-floor-mechanics]] §3c ·
[[sec-filing-intelligence]] · [[canon-klarman-margin-of-safety]] · [[canon-munger-poor-charlies-almanack]].

---

## 9 · Short selling and squeezes: why shorts are fragile

**What it is.** To short a stock you borrow shares (through a prime broker, from a long holder who lends
them), sell them, and later buy them back to return. You profit if the price falls. The loss is unbounded if it
rises. A **short squeeze** is when rising prices force shorts to buy, which pushes prices higher, which forces
more buying.

**How it works.**
- **The mechanics** (Sensa). The lender can **recall** the shares at any time; you must then buy them back or
  re-borrow elsewhere. You pay a **borrow fee**: cheap for easy-to-borrow "GC" names, expensive and volatile for
  crowded shorts (1% today, 5% next week). On a 1% fee on a $100 stock you pay $1 a year, and the bank and the
  lender split it. You also pay any dividend if you are short on the record date (no daily accrual, unlike bond
  coupons). Offsetting that, you earn a **rebate**: interest on the cash from the sale. At zero rates it was
  worth nothing; at 5% it exceeds most borrow costs, which Sensa says made shorting "more lucrative" again.
- **Shorts as alpha, not hedge.** Sosnick, nicknamed "the Grim Reaper" at Pequot, ran shorts as a profit source
  because consumer companies have finite life cycles. Her Rexall Sundown short: a one-product vitamin company
  (glucosamine) rose about 60% when Walmart took the product; the short ran against her and she kept adding
  until her boss flagged that short losses have no ceiling. She drove to Walmarts in four or five cities and
  found the back rooms stacked with unsold Rexall boxes: channel stuffing. The stock collapsed two quarters
  later.
- **GameStop, January 2021** (Industry S2E6 breakdown). Keith Gill ("Roaring Kitty", a CFA) bought about $53k
  of calls in 2019 on a turnaround view. Short interest was public and enormous; Melvin Capital had published
  bearish research. Ryan Cohen joining the board gave Reddit's WallStreetBets a trigger. Between January 11 and
  27 the stock rose over 1,500%, from about $17 to an intraday print near $500; Gill's stake was reportedly
  worth $48m; US share volume on January 27 exceeded the October 2008 peak. Melvin lost about half its capital
  in the month, took a rescue from Citadel and Point72 and closed in 2022; D1 lost about 20%. The hosts add the
  **gamma squeeze**: dealers who sold calls had to buy stock to stay hedged, compounding the move (§7).
- **Earlier squeezes.** Volkswagen 2008 (Porsche cornered the float, VW briefly became the world's most valuable
  company while markets crashed) and the bankrupt energy names of mid-2020 that Tanner's desk lived through.
- **Short interest no longer measures squeeze risk** (Sheffield). If the shorts are pods with stop-losses, a
  small adverse move triggers stops, algorithms chase, passive follows, and the stock overshoots far beyond
  what the short-interest number suggested.
- **Bond shorts** work through repo and reverse repo, with recall and settlement-fail risk; the Ferrari-trader
  short (§13) is a fail-to-deliver story. See [[wss-technicals-career]] §4.13.

**Business significance / value.** Shorts finance the market's skepticism: they find frauds and channel
stuffing, and they lend liquidity. Prime brokers earn borrow fees and lend against the proceeds. Kristen's
counterpoint to the anti-short mood of 2021: propping up a company with no future misallocates capital that
could go somewhere productive.

**Forces & impact.** Retail coordination, call buying and dealer hedging made squeezes faster. Pods made them
more frequent. The result, per Sosnick and Sheffield, is that few fundamental L/S funds still run dedicated
short books; some run none. Fewer shorts means less price discovery on the downside.

**With vs. without.** Without short selling, overvaluation and fraud persist longer (Rexall, Theranos-style
stories). With it, the short seller bears unbounded loss and a lender who can end the trade.

**Applies when / Breaks when.** Works when the thesis has a nearer catalyst than the squeeze, borrow is stable,
and the position is small relative to float. Breaks when float is cornered, borrow is recalled, a retail
crowd or dealer hedging takes over, or stop-loss-driven shorts all cover at once.

**Channel example.** *Hedge Funds 101* (borrow, rebate, recall); *The Real-Life "Billions"* (Rexall);
*Industry S2E6 "Short to the Point of Pain"* (GameStop); *Options Trading 101* (energy squeezes, VW).

**Counterpoint.** The GameStop figures are relayed from press; the intraday high was about $483 on January 28.
Sosnick's Rexall story is a single anecdote; a field check that shows unsold stock can also mean a seasonal
build. "Unlimited loss" is true but overstated as a description of how professional shorts are run: position
sizing and stops cap it, at the cost of being forced out early.

**Links:** [[canon-taleb-antifragile]] · [[canon-perrow-normal-accidents]] (tight coupling: stops, dealers,
algos) · [[canon-akerlof-market-for-lemons]] · [[wss-technicals-career]] §4.13.

---

## 10 · Multi-manager pod shops: many small bets, tight leashes, big footprint

**What it is.** A multi-manager ("pod shop": Millennium, Citadel, Balyasny, Point72) splits capital among dozens
or hundreds of PMs. Each runs a small, low-beta, risk-limited book. Losers are cut fast, and the firm survives
any single PM's failure.

**How it works.**
- **Leverage stacks.** Kristen's sketch: $100 from LPs, about 5x at fund level, about $500 to PMs, then
  instrument leverage on top. Sensa: $100 of capital, $500 of notional across long and short books.
- **Factor neutrality** (Sensa). If 60% of your long book is large cap, 60% of your short book must be. If 30%
  of longs are healthcare, so are 30% of shorts. What remains is meant to be pure stock-specific return.
- **Stop-losses as capital allocation.** WSJ example: a PM given $1bn who loses $50m (5%) gets "a tap on the
  shoulder" and maybe a 50% capital cut; another $25m and he may be fired. Goyal on how this tightened: 15
  years ago a $100m book could lose $10–12m before being unwound; now $4–5m, perhaps $6m after two or three
  serious conversations.
- **The Buffett test.** Goyal: Buffett's October 2008 "buy American" call would have been stopped out "55
  times" at a modern multi-strat. (Pass 1 relayed this second-hand as "five times in the first 12 minutes";
  the primary source says 55.) The distinction he draws is macro *investing* versus macro *trading*: if six
  rate cuts are priced and you think three, the market can price eight before the Fed delivers three, and half
  the industry is stopped out first.
- **Fund-level risk.** Committees set limits by asset class and curve bucket (5y, 10y, 30y; euro, sterling,
  yuan) above individual PM limits. A **management book** hedges crowding: if eight of ten pods are long
  10-year Treasuries, the risk committee buys options or a correlated hedge at fund level. Some funds require
  PMs to keep risk deployed on average through the year; one asked Goyal to make 8% a month.
- **The center book.** Sensa: if a PM is known to be good at trading Procter & Gamble, the platform's
  algorithm can buy alongside her, "a box behind her", which amplifies every move.
- **Roles.** Analyst, sub-PM, junior PM, associate PM; who takes risk varies by fund. Goyal: perhaps four of
  60 pods make the outsized money.
- **Origins.** Citadel nearly failed in 2008 and is credited with surviving through term financing and
  two-year capital locks. Jen calls the pod shop "the Billy Beane of trading" (§20).

**Business significance / value.** If each PM's Sharpe is modest and PMs are uncorrelated, portfolio Sharpe
rises with roughly the square root of the number of independent bets. That is how Millennium reports about 2.6
while individual PMs are ordinary. The firm captures that value; the PM bears the career risk.

**Forces & impact.**
- Strong 2022 returns brought huge 2023–24 inflows (Sensa). Their footprint changed the market: "when
  platforms sneeze, everybody gets the coronavirus", in Sensa's paraphrased line. A disappointing Tesla print
  sends all of tech swinging.
- Sheffield thinks pods, more than passive, are the biggest post-COVID change: their PMs are valuation-agnostic
  (long at 100, short at 99), levered and stopped out together, so squeezes and air pockets follow (§9).
- The talent war pushes PM pay, and so pass-through costs to LPs, sharply higher.

**With vs. without.** Without tight leashes, one PM's conviction trade can sink the fund (Situational Awareness
was effectively one book at 4x, §12). With them, the firm cannot hold long-horizon, high-volatility theses: it
gives up Buffett-style returns to buy survival.

**Applies when / Breaks when.** Works when PM returns are truly independent and markets liquid enough to cut
fast. Breaks when every pod is in the same trade and stops trigger together; the stop-loss then becomes the
contagion mechanism.

**Channel example.** *Hedge Funds 101* (factor rules); *Global Macro PM* (Goyal: stops, risk buckets, management
book); *Contrarian L/S PM* (Sheffield); *Apollo's Quest to Double AUM* (Millennium stops).

**Counterpoint.** The hosts present the pod shop as risk management perfected. Its stability depends on leverage
that is only safe while its trades stay uncrowded, and the same structure that saves the firm fires the people.
If the best long-term trade of 2008 is unholdable, the format selects for short-horizon edge, not truth.

**Links:** `quant-backtesting/research/citadel.md` · [[trading-floor-mechanics]] §5 ·
[[canon-taleb-antifragile]] · [[canon-perrow-normal-accidents]].

---

## 11 · Quant investing: systematic judgment and its failure modes

**What it is.** Quant investing uses mathematical models to find opportunities, build portfolios and control
risk, with little day-to-day human discretion: humans build the models, the models trade. Mintz's case for it:
humans are emotional and biased in the moment, models apply the same expertise across tens of thousands of
stocks every day.

**How it works.**
- **Types** (Mintz): high-frequency (capturing tiny price changes in microseconds), trend-following, and
  **fundamental factor investing**, PGIM's style: a systematic version of what a discretionary manager does,
  buying good growth and high quality at a reasonable price. Muller's PDT does **statistical arbitrage**:
  forecasts over horizons from a minute to a year using any data, careful controls against overfitting, a
  model of its own market impact, and optimization for "dollars made per unit of risk".
- **Factors.** A factor is a scored characteristic compared across companies. A P/E relative to peers or
  history was "quant 101 thirty years ago". Today PGIM's innovation factor runs natural-language processing
  over news, 10-Ks and earnings transcripts, cleans the data and converts it to a score.
- **Theory first.** PGIM wants a fundamental reason a signal works, because a backtest alone doesn't say why it
  should persist. Each new factor must have a realistic decay rate, not be crowded, and not double-count an
  existing factor; adding one dilutes the others' weights. A biweekly research meeting presses the researcher,
  and three people decide.
- **What the quant does all day.** Juniors scrub data, watch cash flows to stay fully invested, and run the
  stock-selection and portfolio-construction models for the PM. Research juniors build factors with seniors.
- **Clients and use.** Quant equity sells consistency: "we're not going to surprise on the upside or the
  downside" (Mintz). It complements concentrated managers: PGIM built a pension an emerging-markets-ex-LatAm
  portfolio around its favorite LatAm manager. Some clients put all their equity in quant to spend their risk
  budget elsewhere (private credit, real estate).
- **The emotional edge** (Muller). In a systematic fund the only decision is whether to trust or change the
  model. He still feels overconfidence and fear after 33 years; he just doesn't act on them. His poker lesson:
  recognize when you are "on tilt" and walk away.

**Business significance / value.** Quant firms capture scale economies in research: one model covers 40,000
stocks. The best (RenTech, PDT) end up running their own money. Their staff are physicists, mathematicians and
computer scientists in what Muller calls a research lab; Kapnick notes her climate-science PhD cohort went to
Millennium, Citadel and D.E. Shaw. The culture problem is getting brilliant people to collaborate.

**Forces & impact.** Quant strategies scale, so success attracts capital and crowding.
- **The August 2007 quant quake** (Muller). After years of success everyone piled into similar quant trades with
  rising leverage. One overlevered firm began liquidating as credit stress built; relative valuations "went
  crazy" while the index barely moved, so non-quants didn't notice. Several funds blew up; PDT "lost our entire
  year in a week" and recovered to finish the year fine.
- **The quant winter, 2018–20** (Mintz). Many models leaned on value (cheapness). Value underperformed "worse
  than we thought it could get" for years; PGIM cut its value weight and strengthened quality and growth.
- **Shocks** like Liberation Day (April 2025) or COVID detach prices from fundamentals; factor models lag, then
  recover as data reflects reality. The discipline is not to "freak out".
- Generative AI: PGIM uses NLP in its models but not generative AI, because it wants to know *why* it owns a
  stock; it uses AI for code and summaries.

**With vs. without.** Without quants, markets lose cheap, emotionless liquidity and broad price discipline
across thousands of small names. With them, crowding creates a hidden common factor that unwinds violently,
invisible at the index level.

**Applies when / Breaks when.** Works when signals have an economic reason, are not crowded, and the regime
resembles the training data. Breaks in crowded deleveraging (2007), long regime shifts (value 2018–20) and
narrative shocks.

**Channel example.** *Quant Investing 101 feat. PGIM's Stacie Mintz* (October 2025); *Pete Muller on Building…
PDT Partners*; short *Highest Paid Hedge Fund Manager… You CAN Beat the Market*; *Sarah Kapnick*.

**Counterpoint.** Mintz is selling a product designed to be complementary and low-surprise; "theory first" is
also good marketing against black-box rivals. Muller's account of 2007 and 2008 is the founder's; the spin-out
"incredibly amicable" story omits what he calls the most painful negotiation of his life. For the statistics of
whether a backtested edge is real, do not rely on the channel: use `quant-backtesting/`.

**Links:** `quant-backtesting/research/lopez-de-prado.md` · `…/harvey-liu-zhu-backtesting-pitfalls.md` ·
`…/academic-frameworks-multiple-testing.md` · `…/factor-models-regime-detection.md` · `…/aqr-capital.md` ·
`…/de-shaw.md` · `…/renaissance-technologies.md` · [[canon-mauboussin-success-equation]].

---

## 12 · Leverage, margin and forced selling: why being right is not enough

**What it is.** Leverage means controlling more exposure than your equity, using borrowed money, borrowed
securities or derivatives. The lender, usually a **prime broker**, marks positions daily and demands more
collateral (**margin**) when they fall. If you cannot post it, you sell, and selling a large book pushes prices
against you.

**How it works.**
- **Prime broker guardrails** (Sensa): exposure limits, single-name and sector thresholds, all designed against
  an Archegos, the family office that hid leverage in swaps across several banks, none of which saw the whole
  book. The banks lost billions.
- **Situational Awareness, as the channel reconstructs it** (July 2026):
  - Leopold Aschenbrenner launched the fund in 2024 with about $225m from Stripe's founders and others.
  - Leverage about **4:1**. Reported "AUM" peaked around $45bn on July 1 and fell to about $10bn by month-end;
    that figure is gross exposure, not money raised.
  - Book: long energy, neoclouds and data centers, memory (SK Hynix, SanDisk); short logic chips (Nvidia, AMD,
    Qualcomm) and application software (Workday, Adobe, Intuit, Salesforce).
  - **Both legs lost at once**: AI infrastructure fell up to about 50% while software held up.
  - Margin calls followed; Jane Street and Millennium passed; **Citadel bought the public book** on July 30.
  - Spillover: SK Hynix and Samsung's memory unit are over half the KOSPI; about 1.2m Korean accounts got margin
    calls. The fund was reportedly still up about 80% on the year.
- **Comparables:** LTCM (over 25:1, right but margin-called before convergence), Lehman (about 32:1), FTX/Alameda.
  The 2007 quant quake (§11) and GameStop (§9) are the same mechanism in other markets.
- **Leverage norms:** 4–5:1 on single stocks is large; 20–50:1 on Treasuries is routine because they move far
  less (§13).

**Business significance / value.** Prime brokerage lends cash and securities against collateral. The forced
seller's loss is the patient buyer's gain: Citadel buying a distressed book at a discount is a
liquidity-provision business.

**Forces & impact.** Rising volatility raises margin, which forces sales, which raises volatility. Concentrated
books in small markets turn one fund's deleveraging into a national event. Once a cause can be named ("just one
fund blew up"), sentiment can snap back fast.

**With vs. without.** Without leverage, Situational Awareness would have had a bad month and kept its thesis.
With it, timing mattered more than truth: the market can stay irrational longer than you can stay solvent.

**Applies when / Breaks when.** Works while volatility is low and funding stable. Breaks when volatility jumps,
correlations go to 1 and the lender, who ranks ahead of you, decides your holding period.

**Channel example.** *The Biggest Hedge Fund Blow-Up of 2026 EXPLAINED: Situational Awareness* plus two shorts;
*Hedge Funds 101* (Archegos).

**Counterpoint.** The two shorts disagree on details; the figures are press reports, not filings. The ad hominem
jokes about the founder's age don't survive the hosts' own concession that the thesis was +80% YTD and the
failure was risk management. "Being early is the same as being wrong" is true for levered capital and false for
unlevered capital, and that distinction is the whole lesson.

**Links:** [[canon-perrow-normal-accidents]] · [[canon-taleb-black-swan]] · [[canon-klarman-margin-of-safety]] ·
`acumen/` (right thesis, wrong sizing).

---

## 13 · Duration and DV01: converting basis points into dollars

**What it is.** A bond's price moves opposite to its yield, and longer bonds move more. **Duration** is the
conversion factor; **DV01** is the dollar P&L for a one-basis-point move. Professionals size in DV01, not
notional. The rates sibling teaches the mechanics in depth ([[wss-rates-macro]] §2); this section keeps the
fund-seat examples.

**How it works.**
- Jen's Iran-war example: $100m of 2-years (duration ≈ 1.8, +60bp) loses about **$1.08m**; $100m of 10-years
  (duration ≈ 8, +50bp) loses **$4m**. The smaller move lost almost 4x more.
- Sizing by DV01 (Citadel episode): to make $1m on a 10bp move in 2-years you need $100k/bp, about **$555m of
  2-year notes**, more than half a $1bn fund. So it is financed in repo (§14): this is where 20:1 comes from.
- **Futures DV01** (short, worked by Jen). A futures contract has no coupon; its DV01 comes from the
  cheapest-to-deliver bond, adjusted by a conversion factor. With an illustrative CTD DV01 of 6.6 and a
  conversion factor of 0.99, futures DV01 ≈ 6.53 per $100 face. Someone sold **78,000** 10-year (TY)
  contracts at $100k face each: 6.534 ÷ 10,000 × 78,000 × $100,000 ≈ **$5.1m per basis point**. When yields
  rose 5–10bp that day, the seller was up $25–50m, if it wasn't a hedge (perhaps against heavy call open
  interest).
- **What DV01 costs when a hedge fails** (the "Ferrari-loving trader" short). A client sold about $2.6bn of long
  bonds he didn't own; dealers bought, hedged by going short, and waited for delivery that never came. COVID
  lockdowns sparked a rally instead of a sell-off. Jen's math: DV01 about $4.2m × a 50bp rally ≈ **$210m**; the
  street's reported loss was about $250m.

**Business significance / value.** DV01 is the common currency across bonds, swaps and futures: it lets a desk
add up risk, hedge and set limits.

**Forces & impact.** Long-end volatility (30-year yields above 5% for the longest stretch since 2007) and war
headlines hurt long-duration holders most, which is why macro funds blow up on geopolitics.

**With vs. without.** Without DV01, 20:1 on 2-years looks reckless and 4:1 on 10-years looks prudent, when they
are risk-equivalent.

**Applies when / Breaks when.** First-order approximation; breaks for large moves (convexity), callables and
mortgages, and curve twists.

**Channel example.** Shorts *Duration & DV01*, *How to Calculate Treasury Futures DV01*, *Largest 10 Year Treasury
Futures Block Trade EVER?*, *Ferrari Loving Trader Cost Wall Street a Quarter Billion*; *The Skinny on Citadel
White Label S&T*.

**Counterpoint.** Jen's futures formula multiplies by the conversion factor; the usual convention divides the
CTD's DV01 by it. With a factor near 0.99 the difference is about 2%. The "$100m of 10-years at DV01 7.5 =
$775,000" line in the short is a garble for $75,000. The Ferrari short gives yields of "3.72% to 3.2%" for
February–March 2020; long-bond yields were nearer 2% falling to about 1%, though the 50bp × DV01 arithmetic
stands.

**Links:** [[wss-rates-macro]] §2, §11 · [[unit-06-whats-a-business-worth]] · `quant-backtesting/research/bloomberg-tradeweb.md`.

---

## 14 · Repo, bank capital and the non-bank dealer

**What it is.** **Repo** is a collateralized loan: buy bonds, lend them to a bank as collateral, borrow cash to
pay for them. Banks fund this from a balance sheet that must be backed by capital. When that capital is
expensive, dealing and lending migrate outside bank regulation. [[wss-rates-macro]] §10 covers repo, SOFR and
swap mechanics.

**How it works.**
- A $1bn fund wanting $555m of 2-years (§13) repos them; that is how hedge funds are levered.
- Basel III "endgame" raises the capital charge on repo, inventory and derivatives, so dealers ration balance
  sheet; liquidity thins, spreads widen.
- **Citadel Securities** is a broker-dealer and market maker outside bank capital rules. Bloomberg reported it
  might offer **white-label S&T to banks**, letting them outsource dealing without the balance-sheet charge,
  mirroring banks outsourcing lending to private credit. In the basis-trade episode Jen notes Citadel is both
  dealer and hedge fund: "the basis trader and the prime broker".
- **The same displacement in other markets.** ETF market making went to Jane Street, Citadel and Virtu because
  it became too balance-sheet intensive for banks (§4). Equity options market making went the same way (§7).
  Bank prop trading moved to hedge funds after the Volcker rule (Goyal, Muller; [[trading-floor-mechanics]] §5).
  Credit desks shifted from principal risk to agency matching ([[wss-credit-distressed]] §4).
- **Electronification:** clients now send RFQs to about ten dealers at once, compressing spreads and sales
  headcount. Equity commissions fell from about 6 cents a share (Adami, Goldman late 1990s) to fractions of a
  cent. Adami's explanation for why clients ever paid 6 cents: access to the IPO calendar, research, and the
  dealer's willingness to take the occasional big block ("bid wanted 5 million GE").

**Business significance / value.** Balance sheet is the scarce input of market making. Whoever has cheap balance
sheet captures spread: banks before 2008, non-bank market makers and private credit now. A cost imposed on
incumbents is a subsidy to their unregulated substitutes.

**Forces & impact.** Regulation aimed at 2008 pushes leverage into shadow banking. Burton's traffic analogy:
adding highway lanes floods someone else's basement. The policy lever in the other direction is SLR relief,
which would make it cheaper for banks to hold Treasuries (§15).

**With vs. without.** With bank capital rules, banks are safer, markets less liquid and risk moves to non-banks.
Without them, 2008-style bank leverage. Neither removes the risk; they choose where it sits.

**Applies when / Breaks when.** Displacement holds while the activity is profitable and an unregulated vehicle
exists. It breaks when regulators follow the activity (the SEC's Treasury central-clearing mandate).

**Channel example.** *The Skinny on Citadel White Label Sales and Trading*; *Fortress Chief Strategist*; *ETFs
101*; *Commodities feat. Guy Adami*.

**Counterpoint.** This is the hosts' strongest bias; both are ex-bank and resent post-2008 rules. Kristen pushes
back on air that regulation "on the whole" makes things safer. The white-label rumor is one Bloomberg report.

**Links:** [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] §4, §5 · [[wss-rates-macro]] §10 ·
[[wss-credit-distressed]] §4 · [[canon-meadows-thinking-in-systems]].

---

## 15 · The Treasury basis trade: short volatility dressed as arbitrage

**What it is.** Treasury futures structurally trade rich to the cash bonds deliverable into them. A fund buys the
cash bonds (repo-financed), sells the futures, and waits for the two to converge at delivery. It is close to
riskless *if held to the end* and **implicitly short volatility**, because anything that widens the gap first
creates mark-to-market losses. [[wss-rates-macro]] §11 teaches the contract and CTD mechanics; this section is
the fund's view.

**How it works.**
- **Why futures are rich** (Jen). There are three ways to get $100m of 10-year exposure: spend $100m on bonds
  (most balance sheet), finance bonds in repo (put up, say, $10m and borrow $90m), or use derivatives (futures
  on small exchange margin, or a receive-fixed swap with no cash up front). Real-money investors and banks
  prefer the derivatives because they use least balance sheet, so futures and swaps trade rich and cash bonds
  cheap. That is also why swap spreads are negative.
- **The trade.** The gap is a couple of basis points, so it is levered about 20:1 "or significantly more" (Matt
  Levine's podcast: up to 100x). Carry example: a 5% coupon financed at 4% repo earns 1%, plus roll-down; a repo
  spike to 6–10% turns it negative.
- **The failure path.** A shock cheapens cash Treasuries against futures. The cash leg marks down, amplified by
  leverage; if futures rally, margin is due on the short too. The PM stops out and dumps cash bonds into a
  falling market.
- **April 2025.** Apollo's Torsten Slok estimated the trade at about **$800bn** (from hedge fund futures shorts
  and prime-brokerage repo). Reported damage that week: one PM stopped out for about $140m, another $30m, a
  rumored $400m; Jen had worked with all three. Against $36tn of debt and a $39bn 10-year auction, that was not
  systemic.
- **Jen's verdict: symptom, not cause.** The cause was a repricing of US assets after the tariffs, with no
  flight to quality into Treasuries. Her evidence: swap spreads collapsed (30-year near −100bp), meaning
  investors preferred derivatives to cash Treasuries across the board, not just that one crowded trade unwound.
- **Fixes.** The biggest lever is SLR relief to make bank Treasury holdings cheaper; others are QE, direct Fed
  bidding at auctions (never done) and repo facilities. Rate cuts matter least, "like filing your nails to lose
  ten pounds".
- Goyal: RV fixed income, including the basis, is a "bread-and-butter" business at multi-strats, run straight
  through COVID.

**Business significance / value.** Basis traders supply balance sheet to the Treasury market: asset managers
who want duration buy futures, basis funds hold the bonds. Useful liquidity, paid for by a carry spread, that
can vanish when needed.

**Forces & impact.** Rising Treasury supply and constrained dealers grow the trade. Its size makes it systemic.
Public marks plus redemption rights turn temporary losses into realized ones.

**With vs. without.** Without basis traders, futures trade persistently rich and funding the deficit costs more.
With them, the Treasury market has a large, levered, crowded weak point.

**Applies when / Breaks when.** Works in calm funding markets. Breaks in a dash for cash (March 2020) or a
safe-haven break (April 2025), when repo haircuts rise and everyone exits together.

**Channel example.** *Bond Market Chaos: Unpacking the Basis Trade Blowup Theory. Cause… or Convenient Excuse?*
(April 2025); short *The Most Profitable Trade on Wall Street That Keeps Blowing Up Hedge Funds*.

**Counterpoint.** Calling it arbitrage understates the tail: a trade profitable until a liquidity crisis is
selling insurance. Jen's "symptom" view rests on one week's reported losses; she concedes such damage can take
time to surface. Slok's $800bn is an estimate from positioning data, not a measured book.

**Links:** [[wss-rates-macro]] §10, §11, §16 · §6 (high Sharpe, hidden tail) · §12 · [[canon-taleb-black-swan]].

---

## 16 · Reading the rates market: implied Fed odds, QE vs. not-QE, and the 10-year

**What it is.** Market prices encode forecasts. Fed funds futures imply the odds of a rate change; balance-sheet
operations are often called "QE" when they are not; Burton anchors everything on the 10-year. The full treatment
is [[wss-rates-macro]] §4 and §7; this keeps the trader's angle.

**How it works.**
- **Implied hike odds** (short *Will the Fed Hike Rates?*). Effective rate 3.63%; the September contract at 96.29
  implies 3.71% for the month; with the meeting on day 16 of 30, (30 × 3.71 − 16 × 3.63) / 14 = **3.80%**, so
  (3.80 − 3.63) / 0.25 = **68% odds of a hike**.
- **Not QE.** The Fed rolling about $71bn of $76bn maturing debt is reinvestment; Treasury buybacks reshuffle debt.
  QE means expanding the balance sheet with new reserves.
- **The 10-year as master variable** (Burton): it embeds inflation expectations and prices mortgages and DCF
  discount rates. Adami's curve warning (March 2024): the record inversion is not what hurts, the re-steepening
  is.
- **Trading the gap between priced and expected** (Goyal, early 2024): six cuts priced for 2024; if you think
  three or four, express it in Fed funds futures, 2-year SOFR, 2-year Treasuries or options, whichever is most
  mispriced. By airing, three or four were priced.

**Business significance / value.** Implied probabilities turn macro noise into numbers you can size, matching
`acumen/`'s probabilistic discipline.

**Forces & impact.** Record open interest around the July 2026 meeting; Citadel Securities' hike call moved odds
from about 20% to 40%. Adami: with $9–10tn of debt rolling in 2024 and a BoJ that hiked yet saw the yen weaken,
foreign selling could push US yields up even with a dovish Fed, because the Fed controls only the front end.

**With vs. without.** Without futures-implied odds, "the market expects a hike" is opinion; with them it is a
number that can be wrong in a measurable way.

**Applies when / Breaks when.** The odds math assumes a 25bp increment and no risk premium.

**Channel example.** Shorts *Will the Fed Hike Rates?*, *Did the Fed Secretly Start QE Again?*, *Is the Treasury
Secretly Doing QE?*; *$53 Billion Hedge Fund Chief Strategist*; *Global Macro PM*; *Commodities feat. Guy Adami*.

**Counterpoint.** Burton's aside that Black-Litterman is "an adjustment to Black-Scholes" is wrong (it is a
portfolio-allocation model). Adami's "rates go higher, not lower" view is a pundit's call; check it against what
happened.

**Links:** [[wss-rates-macro]] §4, §7, §17 · [[unit-06-whats-a-business-worth]] · [[canon-tetlock-superforecasting]].

---

## 17 · Global macro: trading countries, and the Soros template

**What it is.** Global macro funds take positions on whole economies through rates, currencies, equity indices
and commodities. The classic opportunity is a policy the economy cannot sustain, such as a currency **peg**:
either nothing happens or the currency drops sharply, an **asymmetric** payoff.

**How it works.**
- **The modern process** (Goyal, Citadel/BlueCrest/Balyasny). For each country: where is it in the cycle; is the
  curve priced right; does the fiscal position make the long end safe; is the currency cheap on growth,
  inflation and rate models; is the index fairly valued. Then choose the expression with the best relative value
  (§16). Since the 2011 euro crisis, geopolitics has become a core input.
- **What changed.** "Want to be the next George Soros" now gets you laughed out of an interview: macro funds add
  momentum, relative value and small drawdown limits, so *timing* matters as much as the view (§10). The skill
  Goyal calls macro's biggest alpha is scaling risk up when you have a view and down when you don't.
- **The Soros trade, 1992** (told twice on the channel):
  1. The ERM (1979) pegged European currencies while each kept its own central bank. The UK joined in 1990,
     already slipping into recession.
  2. German reunification pulled capital into Deutsche marks; the Bundesbank refused to cut rates.
  3. A roughly 30-year-old analyst (Scott Bessent, now Treasury Secretary) flagged it; Soros and Stanley
     Druckenmiller built a short reported at **£15bn**. The peg capped the downside.
  4. On **September 16, 1992**, the UK hiked from 10% to 12%, then announced another 300bp, and bought sterling in
     $300m–$1bn clips from about $40bn of reserves.
  5. The UK left the ERM; sterling fell sharply. The fund made about $1bn on the trade, likely more across other
     expressions. The world learned a month later from a Fiat CEO quip and a Daily Mail front page.

**Business significance / value.** Macro funds profit when policy and economics diverge; the social value argued
is faster price discovery. The cost fell on UK reserves and credibility. The hosts' link to now: Bessent
understands better than anyone how central-bank credibility is spent.

**Forces & impact.** Capital mobility, divergent growth and policy rigidity drove 1992. Goyal's 2024 macro view
shows the same toolkit applied to China (no large stimulus after COVID, unlike 2009) and to US savings that
lasted longer than expected. Second-order effects of 1992: inflation targeting in the UK and the case for full
monetary union rather than half-pegs.

**With vs. without.** Without speculators, the UK might have defended longer at higher social cost. Without the
peg, there is no one-way bet.

**Applies when / Breaks when.** Anti-peg trades work when reserves are finite and the economy cannot bear high
rates. They fail against a credible defender with deep reserves or capital controls, where the short just pays
carry. Modern macro breaks on timing: the right trade at the wrong time is the wrong trade.

**Channel example.** *Portfolio Manager at World's Top Hedge Funds (and 1st Blind Trader) Breaks Down Global Macro
Trading* (Ashish Goyal, early 2024; pass 1 spelled him "Goel"); *The Craziest Hedge Fund Trade of All Time*;
*Industry S2E8* (which adds Rob Johnson executing trades from his car phone).

**Counterpoint.** The Soros figures are folklore-grade: the position is often cited at about $10bn, the second
hike never took effect, and sterling's one-day fall against the DM was smaller than 15%. Goyal's "S&P is the
wrong benchmark for hedge funds" is true and convenient for a hedge fund PM.

**Links:** [[canon-schelling-strategy-of-conflict]] · [[canon-neustadt-may-thinking-in-time]] ·
[[canon-allison-essence-of-decision]] · [[wss-rates-macro]] §14, §15.

---

## 18 · Commodities: the marginal barrel, gold as anti-fiat, and the pit as a market

**What it is.** Commodities are physical goods (oil, gas, metals, grains) traded both as cargoes and as futures.
Prices are set by the marginal unit, and traders profit from the spreads between grades, places and dates.
Gold is the exception: a monetary asset more than an industrial one.

**How it works.**
- **Physical oil** (Lascaratos, pass 1). WTI usually trades below Brent; the world burns about 100m barrels a day
  with 4–5m spare; shale needs about $50; Hormuz carries about 20% of supply. VLCC rates jumped from $30–40k to
  about $200k a day when the Iran war began. **Contango** (futures above spot) pays storage; **backwardation**
  (spot above futures) says scarcity now, calm later; oil was about $10 backwardated. The trading house is
  "physically informed, derivatives enhanced", with about four derivative trades per physical cargo.
- **Gold** (Adami, March 2024, gold at an all-time high). Central banks have been quietly adding reserves, which
  he reads as "hedging their own ineptitude". Gold hedges inflation, but only when the Fed isn't credibly fighting
  it (it lagged in 2022); it also hedges geopolitics and fiat money. Bitcoin is a bet against central bankers;
  its first top (late 2021) coincided with the Fed abandoning zero rates.
- **Relative value across metals.** The gold/silver ratio historically mean-reverted, but silver sat about 50%
  below its high while gold made new ones; silver lost industrial demand when film (Kodak) died. Copper is a
  construction proxy; a copper breakout contradicted the Fed's "inflation slain" story.
- **The pit.** Trading Places' NYMEX scene was accurate. Floor traders watched futures; upstairs desks traded the
  futures-vs-cash arbitrage with clients. **Self-policing**: a local who reneged on a $15 trade that closed at $14
  was let off once, then nobody in the ring would trade with him again. Electronic trading cut NYSE floor
  headcount to a small fraction of the 1980s level.
- **Commodities desks make two-way markets**: a client like Sir James Goldsmith would never say whether he was
  buying or selling, unlike equity agency orders.
- **Weather as an input.** Merrill's Houston energy desk had two ex-National Weather Service meteorologists to get
  models faster (Tanner). Kapnick built seasonal winter forecasts that predict gas demand.

**Business significance / value.** The trading house earns by knowing where the barrel is needed and getting it
there; now that drones count inventories, edge has moved to structure and risk-taking. Gold and copper act as
the market's independent check on central-bank narratives.

**Forces & impact.** Geopolitics moves the marginal barrel and shipping together; sanctions created a "dark
fleet". Central-bank gold buying reflects distrust of reserve currencies.

**With vs. without.** Without traders, refiners depend on single producers. Without spread markets, there is no
signal to store, ship or switch fuels. Without the floor, markets are more efficient and lose the reputational
policing and the apprenticeship Adami values.

**Applies when / Breaks when.** Relative value works while spread relationships hold; breaks when flows stop
(insurance cancelled), when futures force delivery you can't take (negative WTI, April 2020), or when ratios stop
mean-reverting because the underlying demand changed (silver).

**Channel example.** *"Citadel of Oil & Gas Shipping and Trading" CEO*; *What YOU Must Know About Commodities feat.
Guy Adami*; *Options Trading 101* (Houston rotation); *Sarah Kapnick*.

**Counterpoint.** Several Lascaratos figures are garbled (Hormuz is about 20m bpd; "$67 per barrel for the ship"
should be about $4). Adami's "cumulative inflation of almost 20% under Biden" is roughly right on CPI but offered
as politics. The gold-as-ineptitude-hedge story is a narrative; central-bank buying also reflects sanctions risk
on dollar reserves after 2022.

**Links:** [[canon-mankiw-principles-of-economics]] · [[canon-goldratt-the-goal]] · [[canon-taleb-antifragile]] ·
Course 06 (supply chain).

---

## 19 · Capital raising and the allocator's seat

**What it is.** Hedge funds get capital from **allocators** (pensions, endowments, sovereign funds, insurers,
family offices, wealth platforms) through IR teams, placement agents or capital introduction. The allocator
underwrites the manager; IR translates between PMs and money.

**How it works.**
- **IR is a revenue seat** (Bauman): know the target's portfolio, write their memo, show the 4–5 things that
  differentiate you and who they will stack you against, and above all a **repeatable process**.
- **The lifecycle:** months to years (one investor took seven); capital-intro conferences (iConnections: about
  19,000 meetings); then operational due diligence, risk meetings and consultant gatekeepers.
- **No deadline**: hedge funds are evergreen, so urgency has to be manufactured. **Diversify the investor base**
  by size, type and region, and call investors *before* bad news.
- **Lockups as a negotiated asset** (Muller, §1): a track record buys a seven-year lock at top fees.
- **The allocator side** (Burton): a Black-Litterman sanity check showed a famous fund needed about 25% a year to
  justify its weight against about 2% realized; allocators are fully invested, so every new allocation is
  one-in-one-out; exclusion rules push the same risk into SMAs; public pensions are locked out of top VC by FOIA.
- **Governance drives passive** (Karniol-Tambour): CIOs privately know concentration is bad but avoid the
  governance hassle; being right 70% of the time still gets you called an idiot for not staying passive.
- **Completion mandates** (Mintz): quant managers build portfolios around a client's concentrated managers.
- **Distribution to wealth**: platforms digitize subscription documents as megafunds chase retail capital.

**Business significance / value.** Fees scale with AUM (§1), so the capital raiser sits in the revenue line. Every
incentive problem in the chain (GP fees, consultant gatekeeping, pension headline-aversion) shows up in what
gets funded.

**Forces & impact.** Full allocation makes fundraising a share-shift game. AI speeds diligence and widens the gap
between nimble and slow allocators. Governance pressure pushes institutions toward passive just as concentration
raises its risk.

**With vs. without.** Without ODD and consultants, frauds get funded. Without base diversification, one LP's
redemption can force the liquidation in §12.

**Applies when / Breaks when.** Relationship raising works with repeat players and breaks when performance does.

**Channel example.** *Head of Investor Relations at $3 Billion Hedge Fund Tells All*; *$53 Billion Hedge Fund
Chief Strategist*; *Pete Muller*; *Bridgewater Co-CIO*; *Quant Investing 101*.

**Counterpoint.** The most promotional material in the cluster: Bauman pitches on camera, CAIS is close to a
sponsored spot. Burton is the corrective, doubting allocators' own rules. Fortress describes itself as a credit
manager, not the hosts' "$53bn hedge fund".

**Links:** [[trading-floor-mechanics]] · [[canon-cialdini-influence]] · [[canon-jensen-meckling-agency-theory]] ·
[[canon-march-primer-decision-making]] · [[wss-private-markets-wealth]] §9.

---

## 20 · Moneyball as a trading playbook: mispriced traits, sample size, edge decay

**What it is.** In the hosts' reading, *Moneyball* is a finance book: a budget-constrained team found traits the
market underpriced, bought them cheaply and won, until everyone copied it.

**How it works.**
- **Efficiency metric.** A minimum-wage roster cost about $7m and would win about 49 games; the playoffs need about
  95. The A's paid about **$500k per win** against the Rangers' about **$3m**; ($40m − $7m) / (103 − 49) ≈ **$611k
  per marginal win**.
- **Mispriced traits.** On-base percentage correlated most with winning; in DePodesta's model a point of OBP was
  worth **3x** a point of slugging, against conventional sabermetrics' 1.5x and scouts' near-zero.
- **Sample size.** A .300 and a .275 hitter differ by about one hit every two weeks; over 15 games the .275 hitter
  out-hits the .300 hitter about 40% of the time. Nathan's 52% win rate (§6) is the trading version.
- **Edge decay.** The Red Sox copied it and won in 2004; now the method is table stakes.
- **The postseason lesson.** A best-of-7 is a small sample; in trading there is no World Series, so never
  manufacture one by betting the book.

**Business significance / value.** The cleanest case of capital efficiency under constraint. Rich teams overpay for
consensus; too much money removes the pressure to be smart (the hosts' SoftBank/WeWork link).

**Forces & impact.** Data availability spread the insight. League economics set the stakes (MLB's weak revenue
sharing vs. the NFL's cap).

**With vs. without.** Without statistical valuation, scarce capital pays the "looks the part" premium. Without
small-sample humility, a good season is mistaken for skill.

**Applies when / Breaks when.** Works while a measurable trait is mispriced and samples are large. Breaks once
copied (quant crowding, §11) and in small-sample, winner-take-all settings.

**Channel example.** *Parallels Between Managing a Hedge Fund and a Baseball Team | "Moneyball" Deep Dive*.

**Counterpoint.** The hosts' curse and clutch stories are the anecdote the book debunks; their NFL TV numbers are
loose; the book's A's never won a title.

**Links:** [[canon-mauboussin-success-equation]] · [[canon-kahneman-thinking-fast-and-slow]] ·
[[canon-dixit-nalebuff-thinking-strategically]] · [[canon-helmer-7-powers]] ·
`quant-backtesting/research/harvey-liu-zhu-backtesting-pitfalls.md`.

---

### Side note: catastrophe bonds (insurance risk sold to hedge funds)

Kapnick structured cat bonds at Goldman during Katrina. A **cat bond** transfers a defined peril (hurricane,
earthquake, European windstorm, flood) from an insurer or reinsurer to capital-markets investors. If the event
crosses a preset trigger (a wind speed, a Category 3 landfall, a flood level), some or all of the principal goes
to the sponsor to pay claims; otherwise investors collect a high coupon. Buyers want the return because it is
**uncorrelated** with markets. Jen's challenge: triggers can be drafted so narrowly that they rarely pay, unlike a
CDS that triggers on a missed coupon ([[wss-credit-distressed]] §17). Kapnick's challenge to the models: they are
calibrated on past data for a 3–5 year risk in a changing climate. Her probability lesson applies to any tail
trade: a "1-in-100-year" event has a 1% chance each year, about 4.9% over five years and **26% over a 30-year
mortgage** (1 − 0.99³⁰), and more if the climate is shifting.

### Side note: home-equity investments

A hedge fund acting as a specialty lender (Tacora Capital, Keri Findley): buy a share of a homeowner's future
equity for cash today. The worked example ($50k for a third of the equity, a $133k claim on day one) and the
risks are in [[wss-private-markets-wealth]] §13.

---

## How the concepts connect

```
Fee model (1): 2% on AUM -> AUM growth is the business -> IR as revenue (19)
        |                                         \-- best records shrink outside capital (PDT, BlueCrest)
        v
Allocator demands uncorrelated alpha (5) -> judged on Sharpe / tracking error (6) vs. an index (3)
        |                                     \-- cheap beta via ETFs (4) -> passive flows lift the index
        v
Three ways to find alpha: fundamental L/S (8) | quant factors / stat arb (11) | macro (17)
        |          \-- shorts (9) need borrow; options (7) express and hedge views
        v
High Sharpe + low beta -> justifies LEVERAGE (10 pods; 13 DV01 sizing; 14 repo)
        |           \-- bank capital rules push dealing to HFT/non-banks (14): ETFs, options, Citadel
        v
Crowded "safe" trades: basis (15), factor-neutral pods (10), quant factors (11), RV books (12)
        |
        v
Shock (war, tariffs, Fed surprise (16), AI sell-off, retail squeeze) -> correlations -> 1
        |      \-- index puts miss dispersion (7); dealers short gamma chase (7, 9)
        v
Stops + margin + redemptions + recalls (1, 9, 10, 12) -> forced buying/selling into own footprint
        |      \-- short interest understates squeeze risk when shorts are stopped-out pods (9)
        v
Patient balance sheet buys the book at a discount (Citadel, 12)
   = the asymmetry Soros exploited against a forced defender (17)

Warnings in advance: put/call at 0.4 and call skew (7), record Fed-futures open interest (16),
ETF discounts (4), backwardation, copper vs. gold (18). Moneyball (20) is the counter-discipline:
many small bets, no "World Series" wagers, humility about 52% win rates.
```

The common thread: **the holding period belongs to whoever funds you.** LPs decide it through redemptions, the
prime broker through margin, the stock lender through recall, the risk committee through stops. Strategy quality
matters only within the holding period your capital structure allows, which is why the firms that could (PDT,
RenTech, BlueCrest) chose to fund themselves.

---

## Retrieval questions

1. **A beta-0.1 fund returned 9% while the S&P returned 22%. Why might an allocator still prefer it?** Its return
   is mostly alpha and uncorrelated; beta can be bought for basis points via an ETF. The question is Sharpe and
   portfolio role, not raw return.
2. **An ETF holding illiquid bonds trades at a 3% discount in a panic. Who could close the gap, and why don't
   they?** APs could buy the cheap ETF and redeem it for bonds, but they must then sell those bonds into a frozen
   market or hold them on balance sheet. The discount is the price of the liquidity the ETF promised.
3. **Why is an ETF usually more tax-efficient than an identical mutual fund?** Redemptions are met in kind; the
   fund hands APs its lowest-basis lots, so gains leave without a sale. A mutual fund must sell to meet net
   redemptions and distributes the gains.
4. **A stock is at $100; the weekly at-the-money call and put cost $2.50 each. What move is priced, and what would
   make you sell the straddle?** About 5% ($5 / $100). Sell if its realized earnings moves have averaged well below
   5% and nothing suggests this quarter is different.
5. **Implied vol is 48. Roughly how big a daily move does that imply?** 48 ÷ 16 ≈ 3% a day.
6. **Why did desks short calls on bankrupt energy stocks in 2020 lose money on companies they knew were worth
   zero?** Delta-hedging forced them to buy stock as retail pushed prices up; risk limits fixed their holding
   period before fundamentals could win.
7. **A long-biased L/S fund is 100% long and 50% short. What are its gross and net exposure, and what does each
   tell you?** Gross 150% (total risk and leverage), net 50% (market direction). A pod might be 250% long and 250%
   short: 500% gross, zero net.
8. **Why did higher interest rates make shorting more attractive?** The short seller earns a rebate on the sale
   proceeds; at 5% it can exceed the borrow fee, so a flat stock now pays carry instead of costing it.
9. **Why might short interest of 15% understate how far a squeeze can run?** If the shorts are pods with tight
   stops, small moves trigger mass covering, algorithms chase and dealers short calls buy stock.
10. **Why does losing 7.5% get a Millennium PM fired when it's a routine month for a retail investor?** The PM's
    capital is levered several times at fund level; tight stops keep hundreds of levered books from producing a
    fund-level loss.
11. **What happened in August 2007 that index investors barely noticed?** Crowded, levered quant funds unwound
    similar long/short books at once; relative values blew out while the index was flat.
12. **Situational Awareness ran a "market-neutral" L/S book. How did it lose on both sides, and why did leverage
    turn a bad month into a forced sale?** The legs were separate bets, not hedges, and both reversed; at 4:1 a 25%
    gross loss wipes out equity, and margin fixes the holding period.
13. **78,000 TY contracts with a futures DV01 of about 6.5 per $100 face. What is the position's risk per basis
    point?** 6.5 / 10,000 × 78,000 × $100,000 ≈ $5.1m.
14. **Why is the basis trade "short volatility" if it's an arbitrage, and why did Jen call its April 2025 unwind a
    symptom?** Convergence is certain only at delivery; shocks widen the gap first and force exits. Swap spreads
    collapsing across the board showed a broad flight from cash Treasuries, not one crowded trade.
15. **The September Fed funds future is 96.29, the effective rate 3.63%, the meeting on day 16 of 30. Implied hike
    odds?** (30 × 3.71 − 16 × 3.63) / 14 = 3.80; (3.80 − 3.63) / 0.25 ≈ 68%.
16. **Why did Soros's sterling short have such favorable risk/reward, and why would Goyal's employers still stop
    him out of a similar view today?** The peg capped the upside of sterling and the UK lacked room for high
    rates. Modern multi-strats impose small drawdown limits, so a correct view that moves against you first is
    cut before it pays.
17. **A 1-in-100-year flood. What's the chance of at least one over a 30-year mortgage?** 1 − 0.99³⁰ ≈ 26%, in a
    static climate.
18. **The A's paid about $611k per marginal win. Why did the strategy stop working, and what's the trading
    analogue?** It was copied; mispriced traits got repriced. Published or crowded quant factors decay the same
    way (value 2018–20).

---

## Gaps (still missing after pass 2)

Pass 2 recovered every primary source pass 1 had to reconstruct (options, ETFs, index trading, Sharpe, L/S,
equity research, macro PM, Bridgewater, PDT, PGIM quant, the basis blowup, commodities). Still without a
transcript in the catalog:

- **Industry S2E2 "Giant Squid"** (block trades, IPOs vs. other equity offerings).
- Shorts: *Wellington's Head of U.S. Macro with one simple rule for trading the long end*; *What are inflation
  breakevens in bond trading?*; *8 must know technicals for sales and trading interviews*; *Tell me a Wall Street
  trader is on his mandatory two-week vacation…* (the compliance rule that forces traders away from their books);
  *Investment Banking vs. Sales and Trading Lifestyle*; *Hedge Funds vs. PE*; *The Most Lucrative Wall Street
  Careers: PE vs. Hedge Funds*.

Present in the folder but owned by the rates sibling and not folded in here (see [[wss-rates-macro]]): Steve
Eisman on tariff panic, Matt Hornbach's *Fixed Income Strategy 101*, the Wellington and "$1 trillion firm" macro
episodes, *Finance, Philosophy, and the Yen Carry Trade*, Jamie Patton (TCW), *It Wasn't Equity Turmoil That
Spooked Trump*, and the FX and Dimon shorts.
