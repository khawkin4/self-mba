I now have thorough coverage. Here is the complete research report.

---

## Robert Carver's Systematic Trading Framework: Research Report

### Background

Robert Carver spent over a decade in the City of London. He traded exotic derivative products at Barclays Investment Bank, then served as a portfolio manager at AHL (Man Group) -- one of the world's largest systematic hedge funds. At AHL he created the firm's fundamental global macro strategy and managed a multi-billion dollar fixed income portfolio. He left the industry in 2013 to trade independently and write. He holds a Bachelor's in Economics from the University of Manchester and a Master's from Birkbeck College, University of London.

---

### 1. "Systematic Trading" (2015) -- Key Concepts and Framework Structure

Published September 2015 by Harriman House, this is Carver's foundational book. Its central argument is that traders should build rule-based, automated systems rather than relying on discretionary judgment. The framework is modular, separating three concerns:

**Trading rules** (signal generation, independent of account size), **volatility targeting** (risk appetite, dependent on account size), and **position sizing / instrument weighting** (allocating risk across positions).

**Three trader types.** The book addresses asset allocators (buy-and-hold investors adding systematic rebalancing), semi-automatic traders (discretionary traders who use rules to discipline decisions), and staunch systems traders (fully automated). Each type uses the same framework but configures it differently.

**Forecast scaling.** All trading signals are normalized to a common scale: 0 = neutral, +10 = standard long, -10 = standard short, with extremes capped at +/-20. The average absolute forecast value is 10. This normalization allows different rules to be combined on a common basis and prevents any single rule from dominating.

**Forecast combination.** Multiple rules (e.g., EWMAC trend-following at different speeds, carry) are combined via weighted averages called "forecast weights." Carver's preferred method is "handcrafting": group rules by correlation, allocate equal weight within groups, then across groups. He explicitly warns against blind computer optimization of weights, calling equal weighting "hard to beat."

**Diversification multiplier.** When combining less-correlated forecasts, portfolio volatility drops below the weighted sum. The forecast diversification multiplier (FDM) corrects for this: FDM = target volatility / combined volatility. Example: two forecasts with 10% vol and 0.5 correlation yield 8.66% combined vol, so FDM = 1.15. Carver caps the multiplier at 2.5 and floors correlations at zero to avoid inflated values.

**Trading rules discussed.** EWMAC (exponentially weighted moving average crossover) at multiple speeds (e.g., 16/64, 32/128, 64/256 day pairs), and carry (profiting from yield differentials / term structure). He emphasizes running many variations simultaneously rather than selecting the single "best" from backtests.

Sources:
- [Pan Macmillan page](https://www.panmacmillan.com/authors/robert-carver/systematic-trading/9780857194459)
- [Goodreads](https://www.goodreads.com/book/show/25900953-systematic-trading)
- [7 Circles review -- Frameworks and Forecasts](https://the7circles.uk/systematic-trading-3-frameworks-and-forecasts/)

---

### 2. pysystemtrade -- Architecture and Capabilities

pysystemtrade is the open-source Python implementation of the book's framework. Originally released December 2015 by Carver (GitHub: robcarver17), primary maintenance passed to Andy Geach in 2024, and in January 2026 the repository moved to the pst-group GitHub organization.

**Three functions.** (1) A backtesting engine for strategy validation. (2) An implementation of all the optimization and system design principles from Carver's books. (3) A fully automated production trading system for futures via Interactive Brokers (using the ib_async library).

**Module architecture:**

| Module | Role |
|---|---|
| `systems` | Strategy implementation: forecasting rules, combination, position sizing |
| `sysdata` | Data management and persistence layer |
| `sysbrokers` | Broker connection interfaces (IB) |
| `sysexecution` | Order routing and trade execution |
| `sysproduction` | Production trading orchestration |
| `syscontrol` | System control and scheduling |
| `sysquant` | Quantitative analysis utilities |
| `sysobjects` | Core data objects (futures contracts, positions) |
| `syslogdiag` / `syslogging` | Logging and diagnostics |
| `dashboard` | Monitoring interface |

**Data sources.** The system handles futures data through the `sysdata` module with specialized classes for different asset types. It supports historical data for 100+ futures instruments across bonds, equities, commodities, and currencies.

**Optimization methods.** Three approaches for computing forecast weights: (1) Bootstrapping (preferred) -- Monte Carlo resampling with configurable runs (typically 200) and sample length (e.g., 104 weeks); (2) Shrinkage -- faster, with configurable shrinkage to Sharpe ratio (~0.90) and to correlation (~0.50); (3) Single-period -- explicitly discouraged. Both weights and multipliers use EWMA smoothing to prevent excessive turnover from parameter updates.

**License.** GNU GPL v3, with explicit financial risk disclaimers.

Sources:
- [pysystemtrade GitHub (pst-group)](https://github.com/pst-group/pysystemtrade)
- [Carver's blog -- pysystemtrade page](https://qoppac.blogspot.com/p/pysystemtrade.html)
- [Carver's blog -- Correlations, Weights, Multipliers](https://qoppac.blogspot.com/2016/01/correlations-weights-multipliers.html)

---

### 3. Backtesting Methodology (Blog and Interviews)

Carver's blog "This Blog is Systematic" (qoppac.blogspot.com) is the primary extension of his books. Key methodological positions:

**Walk-forward testing critique.** Carver argues most traders use windows far too short for statistical validity. His research indicates you need approximately 10 years minimum of data to reliably judge rule profitability. One-year walk-forward windows cannot separate signal from noise.

**Overfitting avoidance.** Four criteria for a good trading rule: (1) not overfitted, (2) relatively simple (fewer parameters), (3) understandable, (4) has a plausible economic explanation. He includes the opposite of a given trading rule in backtests to avoid implicit fitting, then only carries positive-Sharpe rules into optimization.

**Averaging beats selection.** A counterintuitive finding he emphasizes: averaging multiple rule variations significantly outperforms selecting the single best performer from each backtest window. Trading returns are noisy year-to-year, so apparent "best" rules benefited from luck.

**Continuous vs. binary signals.** He advocates continuous forecasts that scale position size proportionally to signal strength, producing smoother equity curves, lower transaction costs, and better signal-to-noise ratios compared to on/off signals.

**Alternative beta, not alpha.** Carver challenges the idea of hidden alpha: "I don't really believe there are a huge number of trading rules that exist, which are doing something extraordinarily interesting." He focuses on persistent, documented market effects -- equity risk premiums, term structure premiums, trend following -- which he calls "alternative beta."

Sources:
- [This Blog is Systematic](https://qoppac.blogspot.com/)
- [Better System Trader #026 -- Trading Rules and Overfitting](https://bettersystemtrader.com/026-robert-carver/)
- [Blog start page](https://qoppac.blogspot.com/p/systematic-trading-start-here.html)

---

### 4. Position Sizing and Risk Management

**Core principle.** "Position sizing and risk management are the same thing" -- they happen simultaneously when entering a trade, not as separate afterthoughts.

**Volatility targeting.** The most important design decision. Expressed as annual standard deviation of returns. Carver's rule of thumb: your volatility target should match your expected Sharpe ratio. SR of 0.25 implies a 25% volatility target.

**Half-Kelly.** Backtested Sharpe ratios should be reduced by 25-33% for overfitting. He then applies half-Kelly sizing (half the Kelly-optimal bet), and for negative-skew strategies, quarter-Kelly (another 50% reduction).

**Position sizing formula chain:**
1. Calculate the **block value** -- dollar loss per 1% price move (e.g., oil at $50, 1000-barrel contract = $500).
2. Estimate **daily volatility** using an exponentially weighted moving average (he uses EMA-36, equivalent to ~25-day lookback).
3. Calculate daily instrument currency volatility = block value x daily vol %.
4. **Volatility scalar** = daily cash volatility target / daily instrument currency volatility. This gives the number of contracts for a neutral (+10) forecast.
5. Scale by the actual forecast (e.g., forecast of +15 means 1.5x the scalar).

**Volatility floor.** To guard against low-volatility environments preceding sudden spikes, Carver sets a minimum assumed volatility based on long-run historical averages. If long-term vol averaged 10% but currently sits at 1%, he uses 5% for sizing.

**Position inertia rule.** "If an existing position is within 10% of the target position, don't trade." This reduces transaction costs without meaningful performance impact.

**Five risk categories.** Beyond market risk: liquidity risk, counterparty risk, infrastructure risk (citing Knight Capital's $440M loss), and model risk ("your model of how risk works is wrong").

**Risk management sequence.** (1) Awareness -- recognize exposure exists. (2) Measurement -- quantify expected vs. realized losses. (3) Control -- act if tolerance is breached. He favors systematic approaches over discretionary overrides, recommending incorporating option-implied volatility into risk models rather than manual intervention.

Sources:
- [7 Circles -- Volatility Targeting and Position Sizing](https://the7circles.uk/systematic-trading-4-volatility-targeting-and-position-sizing/)
- [Better System Trader #070 -- Risk Management](https://bettersystemtrader.com/070-risk-management-robert-carver/)
- [Top Traders Unplugged -- When Position Sizing Saves You](https://www.toptradersunplugged.com/podcast/when-position-sizing-saves-you-ft-rob-carver)

---

### 5. Other Books

Robert Carver has published four books total:

**Smart Portfolios** (September 2017, Harriman House). A practical guide to building and maintaining intelligent investment portfolios. Covers blending assets with different risk levels, portfolio construction suited to investor risk tolerance. Provides practical methods, rules of thumb, and techniques. Aimed more at long-only investors than active traders.

**Leveraged Trading** (October 2019, Harriman House). Aimed at traders using FX, stocks on margin, CFDs, spread bets, and futures. Shows how to use trading systems to manage leverage safely, with systems designed to use the correct amount of leverage and trade at suitable frequency. Bridges the gap between his institutional-grade "Systematic Trading" framework and retail traders using leveraged products.

**Advanced Futures Trading Strategies** (April 2023, Harriman House). 638 pages covering 30 fully tested strategies across 100+ tradable instruments using 50+ years of data. Builds progressively from buy-and-hold through trend following, carry, calendar spreads, breakouts, and fast mean reversion. Rated 4.19/5 on Goodreads (59 ratings). Reviewers note each strategy illustrates concepts necessary for understanding the full system, rather than being standalone. Some reviewers flagged that certain mean reversion strategies contain documented lookahead bias issues.

Sources:
- [Smart Portfolios on Amazon](https://www.amazon.com/Smart-Portfolios-maintaining-intelligent-investment/dp/085719531X)
- [Leveraged Trading on Pan Macmillan](https://www.panmacmillan.com/authors/robert-carver/leveraged-trading/9780857197214)
- [Advanced Futures Trading Strategies on Harriman House](https://harriman-house.com/authors/robert-carver/advanced-futures-trading-strategies/9780857199683)
- [Advanced Futures Trading Strategies on Goodreads](https://www.goodreads.com/en/book/show/60784531-advanced-futures-trading-strategies)
- [Carver author page on Goodreads](https://www.goodreads.com/author/show/14163231.Robert_Carver)

---

### Summary of Key Technical Principles

1. **Normalize everything to forecasts scaled -20 to +20**, average absolute value 10.
2. **Combine rules by averaging, not selecting.** Handcraft weights by correlation grouping; equal weight within groups.
3. **Volatility target = expected Sharpe ratio**, then apply half-Kelly (quarter-Kelly for negative skew).
4. **Position size = volatility scalar x (forecast / 10)**, where the scalar is derived from daily cash vol target divided by instrument currency volatility.
5. **Cap diversification multiplier at 2.5**, floor correlations at zero.
6. **10% position inertia buffer** -- don't trade if within 10% of target.
7. **Minimum 10-year data** for any statistical judgment on rule profitability.
8. **Run many rule variations simultaneously** rather than optimizing to a single "best" rule.
9. **Alternative beta, not alpha** -- focus on documented, persistent market effects with clear economic rationale.
10. **Volatility floor** -- never size positions based on unusually low current volatility without a long-run floor.