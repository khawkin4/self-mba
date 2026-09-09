I now have sufficient material to compile a thorough report. Here are the findings.

---

## Backtesting System Architecture for Systematic Trading: Research Report

### 1. Event-Driven vs Vectorized Backtesting

These two paradigms represent the fundamental architectural split in backtesting system design.

**Vectorized backtesting** operates on entire price histories as NumPy/pandas arrays, expressing strategies as array operations with no Python loops. Frameworks like VectorBT leverage NumPy and Numba for fully vectorized computation. The advantage is raw speed -- parameter sweeps and Monte Carlo simulations that would take hours in an event loop complete in seconds. The downside is that vectorized approaches assume fills at the next bar's open or close and ignore intra-bar realities (slippage, partial fills, bid-ask spreads). This can produce misleading results: a strategy that looks profitable in a vectorized backtest can become a clear loss-maker after realistic execution modeling.

**Event-driven backtesting** simulates a live trading environment by sequentially processing discrete events. The canonical architecture (documented thoroughly by QuantStart) has four core event types -- MARKET, SIGNAL, ORDER, and FILL -- flowing through an in-memory event queue. The component classes are:

- **DataHandler**: abstract base class providing a unified interface for historical and live market data, generating MarketEvents at each heartbeat
- **Strategy**: consumes MarketEvents and generates SignalEvents (ticker, direction LONG/SHORT, timestamp)
- **Portfolio**: converts SignalEvents into OrderEvents while managing position tracking and risk
- **ExecutionHandler**: simulates brokerage execution, processing OrderEvents into FillEvents that model fees, commission, and slippage

The event loop has two levels: an outer "heartbeat" loop that advances market data via `bars.update_bars()`, and an inner loop that drains the event queue, routing each event to its handler. This eliminates lookahead bias by construction -- data is drip-fed as events, exactly as it would arrive in production.

**When to use each**: The industry consensus is a hybrid workflow. Use vectorized backtests for rapid screening and narrowing a universe of strategy candidates, then migrate promising designs into an event-driven framework for final validation before live deployment. Backtrader and Zipline (zipline-reloaded) are the established event-driven frameworks; VectorBT is the standard vectorized engine. For production-grade event-driven systems, NautilusTrader has emerged as a strong open-source option with high-fidelity execution modeling.

Sources: [QuantStart Event-Driven Backtesting Part I](https://www.quantstart.com/articles/Event-Driven-Backtesting-with-Python-Part-I/), [Interactive Brokers: Vector-Based vs Event-Based](https://www.interactivebrokers.com/campus/ibkr-quant-news/a-practical-breakdown-of-vector-based-vs-event-based-backtesting/), [BullAlert: Best Python Backtest Engines 2026](https://bullalert.ai/blog/best-python-backtest-engines-2026/)

---

### 2. Professional Quant Firm Backtesting Architecture

Institutional quant firms almost universally build custom in-house backtesting infrastructure. Per QuantStart, this is driven by regulatory constraints, investor relations/reporting requirements, and auditability -- needs that commercial or open-source solutions rarely satisfy out of the box.

**Key architectural patterns**:

- **Securities Master Database**: Production systems use PostgreSQL or HDF5 (not CSV files), handling tick-level data, corporate actions adjustments, and survivorship bias correction.
- **Modular separation of concerns**: Strategy logic, risk management, portfolio construction, and execution handling are isolated modules. The risk module can independently modify, add, or veto orders -- e.g., adding hedges to maintain market neutrality. This modularity also enables the critical capability of swapping the data source and execution handler to transition from backtesting to live trading without touching strategy code.
- **Portfolio and Order Management**: Described as "the heart" of institutional systems, managing transitions from current to desired portfolio states.
- **CI/CD pipeline for strategies**: Firms define granular access controls and a validated deployment pipeline from research sandbox to live trading, with continuous monitoring for data latency, backtest integrity, and compliance.
- **Validation methodology**: Walk-forward analysis (expanding and rolling windows) to prevent overfitting, out-of-sample testing for robustness, and Monte Carlo permutation tests for statistical significance.

**Technology stack**: Python dominates the research layer (end-to-end research, backtesting, deployment, monitoring). C++ remains common for performance-critical execution paths. Open-source frameworks like QSTrader implement the institutional pattern in Python with abstract base classes for each component.

Sources: [QuantStart: Should You Build Your Own Backtester?](https://www.quantstart.com/articles/Should-You-Build-Your-Own-Backtester/), [QSTrader Fee Model Hierarchy](https://www.quantstart.com/articles/qstrader-fee-model-class-hierarchy/), [AWS: Build and Backtest Systematic Trading Strategies](https://aws.amazon.com/blogs/industries/how-to-build-and-backtest-systematic-trading-strategies-on-aws-with-aws-batch-and-airflow/)

---

### 3. Transaction Cost Modeling

Transaction costs are the single most common reason backtests fail to translate into live profitability. Models range from simple to sophisticated:

**Flat Model**: Fixed cost per trade regardless of size. Only valid when trade sizes are constant and liquidity/volatility remain stable. Simplest to implement but rarely accurate.

**Linear (Percentage) Model**: Costs scale proportionally with trade volume. QSTrader implements this via `PercentFeeModel` with `commission_pct` and `tax_pct` parameters applied to `abs(consideration)` (price x quantity). Tends to overestimate costs for small trades and underestimate for large ones.

**Piecewise-Linear Model**: Segments the trade-size spectrum into ranges with different linear equations. Widely adopted in industry as a practical middle ground achieving significantly better accuracy than flat or linear models.

**Quadratic Model**: The most realistic static approach, mirroring actual market behavior where costs grow nonlinearly with order size. Still diverges from realized costs due to changing liquidity, volatility, and latency.

**Spread-based slippage estimation**: The standard approximation is `slippage = c1 * mean_spread + c2`, where coefficients are fitted from production execution data.

**Implementation in QSTrader**: The fee model uses an abstract base class (`FeeModel`) with three methods: `_calc_commission`, `_calc_tax`, and `calc_total_cost`. Concrete implementations (ZeroFeeModel, PercentFeeModel) integrate with the brokerage module that tracks asset transactions and corporate actions. The method signatures accept `asset` (for per-asset-class rates), `quantity`, `consideration`, and an optional `broker` reference for historical commission lookups.

Sources: [BSIC: Transaction Cost Modelling](https://bsic.it/backtesting-series-episode-5-transaction-cost-modelling/), [QSTrader Fee Model Class Hierarchy](https://www.quantstart.com/articles/qstrader-fee-model-class-hierarchy/), [QuantPedia: The Price of Transaction Costs](https://quantpedia.com/the-price-of-transaction-costs/)

---

### 4. Slippage Modeling and Market Impact

#### The Almgren-Chriss Model

The Almgren-Chriss (2000) framework formulates large-order execution as a stochastic optimal control problem. It decomposes market impact into two components:

- **Permanent impact**: Accumulated price shift from all transactions up to time t, modeled as `gamma * (X_t - X_0)` where gamma is a positive constant. Linearity is assumed because it guarantees absence of price manipulation (round-trip trades cannot generate profit).
- **Temporary impact**: Affects only the execution price, not the market price. The realized execution price is `S_tilde = S_t + eta * v_t` where `v_t = -dx/dt` is the rate of trading and eta is the temporary impact coefficient.

The price dynamics follow `dS_t = sigma * dW_t + k * v_t * dt`, combining Brownian motion (random fluctuation) with permanent impact proportional to liquidation rate.

The optimization objective balances execution cost against risk: `J(q) = integral_0^T { V_t * L(q'(t)/V_t) + (1/2) * gamma * sigma^2 * q(t)^2 } dt`, where gamma > 0 is the risk aversion coefficient determining liquidation urgency. High gamma means liquidate quickly (accepting more market impact to reduce variance); low gamma means trade slowly (accepting price risk to minimize impact).

#### Kyle's Lambda

Kyle (1985) models price impact through the lens of information asymmetry between three players: an informed insider, noise traders, and a market maker. The equilibrium produces:

- **Market maker pricing rule**: `p = p_0 + lambda * q`, where q is aggregate observed order flow
- **Lambda formula**: `lambda = (1/2) * (sigma_p0 / sigma_u)`, where sigma_p0 is uncertainty about true asset value and sigma_u is noise trader volume variance
- **Informed trader strategy**: order size = `beta * (V - p_0)` where `beta = sigma_u^2 / sigma_p0^2`

Lambda's reciprocal (1/lambda) measures market depth -- the order flow needed to move price by one dollar. Higher lambda means a less liquid market where the same order flow causes larger price moves. Critically, more unpredictable noise trading (larger sigma_u) makes lambda smaller because the market maker cannot distinguish informed from noise volume, providing cover for informed traders.

#### The Square Root Law

The empirically dominant model for institutional execution is `I(Q) = Y * sigma * sqrt(Q/V)`, where Q is total executed volume, V is average daily volume, sigma is daily volatility, and Y is a normalization constant of order 1. Implementation shortfall integrates this: `S(Q) = (2/3) * Y * sigma * sqrt(Q/V) * Q`. This relationship has been validated across equities, futures, options, and crypto markets. It breaks down at extreme participation rates (below 0.5% or above 20%).

The Obizhaeva-Wang (2013) model adds exponential decay with participation-rate sensitivity. Almgren et al. (2005) uses power-law functions where unit costs decrease proportionally to execution speed raised to approximately the 0.6 exponent.

Sources: [Genius Mathematics: Almgren-Chriss Model](http://mathematicsconsultants.com/2021/10/23/optimal-liquidation-algorithms-the-almgren-chriss-model/), [Kyle Model: Price Impact & Kyle's Lambda](https://faustiandreams.github.io/2022-09-10/kyle-model), [EmergentMind: Square-Root Law](https://www.emergentmind.com/topics/square-root-law-of-market-impact), [Almgren-Chriss Market Impact Model](https://www.emergentmind.com/topics/almgren-chriss-market-impact-model)

---

### Open-Source Implementations Referenced

| Framework | Architecture | Language | Notes |
|-----------|-------------|----------|-------|
| **VectorBT** | Vectorized | Python (NumPy/Numba) | Fast parameter sweeps, Monte Carlo |
| **Backtrader** | Event-driven | Python | Mature, large community, slowed development |
| **Zipline-reloaded** | Event-driven + Pipeline API | Python | Factor investing, ML integration, complex data ingestion |
| **QSTrader** | Event-driven | Python | Institutional-pattern OOP, modular fee models |
| **NautilusTrader** | Event-driven | Python/Rust | Production-grade, high-fidelity execution modeling |