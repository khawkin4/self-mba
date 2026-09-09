Here is the comprehensive research report on Ernest Chan's work in algorithmic trading.

---

## Ernest Chan: Algorithmic Trading Research Report

### Background and Career

Dr. Ernest P. Chan holds a PhD in theoretical physics from Cornell University and a B.Sc. in physics from the University of Toronto. His entry into finance was catalyzed by IBM colleagues Bob Mercer and Peter Brown, who left to join Renaissance Technologies, sparking Chan's curiosity about quantitative hedge funds. He subsequently worked as a machine learning researcher at IBM's T.J. Watson Research Center (Human Language Technologies), then moved to Morgan Stanley's AI group in Manhattan. He also held roles at Credit Suisse as a proprietary trader, and at hedge funds including Mapleridge, Millennium Partners, and MANE. His career since 1994 has centered on developing statistical models and computer algorithms to find patterns in large datasets.

Sources: [Databento profile](https://databento.com/blog/quants-worth-following-ernie-chan), [Interactive Brokers article](https://www.interactivebrokers.com/campus/ibkr-quant-news/dr-ernest-chans-journey-the-promise-and-limits-of-ai-and-machine-learning-for-investing/), [CMT Association](https://cmtassociation.org/presenter/ernest-chan/)

---

### His Three Books

**1. Quantitative Trading: How to Build Your Own Algorithmic Trading Business (2008, 2nd ed. 2021)**

This book lays out Chan's full framework for an independent quantitative trader. Key concepts include:

- **Strategy sourcing and screening**: Source ideas from academic research, blogs, forums, and market observation. Screen across five dimensions -- time commitment, programming skill, capital requirements, return/risk alignment, and competitive positioning versus institutions.
- **Backtesting methodology**: Strict out-of-sample validation, realistic transaction costs, survivorship-bias-free data. He advocates at least one-third of the sample reserved for out-of-sample testing.
- **Kelly Criterion for position sizing**: The mathematical foundation for optimal leverage, maximizing long-term compound growth. In practice, he recommends "fractional Kelly" (typically half-Kelly) to reduce volatility and drawdown risk.
- **Sharpe ratio as primary metric**: Chan considers the Sharpe ratio the single best performance measure. He notes that higher-frequency strategies benefit from naturally higher Sharpe ratios.
- **Niche advantage philosophy**: Individual traders should find strategies "outside major hedge fund coverage" and survive "in the cracks" of institutional blind spots.
- **Risk-first approach**: Categorizes risk into portfolio-level, leverage, model, operational, and psychological risk. Survival enables long-term profit accumulation.

Sources: [MathWorks listing](https://www.mathworks.com/academia/books/quantitative-trading-chan.html), [Amazon](https://www.amazon.com/Quantitative-Trading-Build-Algorithmic-Business/dp/1119800064), [BlockEden summary](https://blockeden.xyz/blog/2025/07/26/quatitive-trading/)

**2. Algorithmic Trading: Winning Strategies and Their Rationale (2013)**

This second book moves from infrastructure to strategy implementation. Key concepts:

- **Mean reversion vs. momentum**: A detailed comparative framework. Mean reversion strategies are counter-trend (prices revert to historical means), optimal in ranging markets. Momentum strategies are trend-following, optimal in news-driven trending markets. Identifying the current market regime (trending vs. ranging) is essential.
- **Cointegration**: Distinguished from correlation. A cointegrated pair has a linear combination whose spread is stationary over time; correlated assets merely move together temporarily.
- **Johansen test**: Multivariate cointegration test for determining optimal hedge ratios across multiple assets to create stationary spreads.
- **Regime switching**: How market regime changes affect strategy selection and performance.
- **Implementation in MATLAB**: Provides working code for each strategy, bridging theory to practice.

Sources: [Wiley](https://www.wiley.com/en-us/Algorithmic+Trading:+Winning+Strategies+and+Their+Rationale-p-9781118460146), [Goodreads](https://www.goodreads.com/en/book/show/17848897-algorithmic-trading), [Amazon](https://www.amazon.com/Algorithmic-Trading-Winning-Strategies-Rationale/dp/1118460146)

**3. Machine Trading: Deploying Computer Algorithms to Conquer the Markets (2017)**

The third book extends into machine learning and automation:

- **Factor models**, including those derived from options markets, useful for short-term traders
- **Time series techniques**: ARIMA, VAR, and state-space models with hidden variables
- **Machine learning**: Techniques specifically chosen to reduce overfitting, a problem Chan considers endemic in quant finance
- **Options and volatility strategies**, including portfolio-level options positions
- **Execution technology**: Broker selection, API-based automated execution, and cost-effective data vendors
- **Portfolio optimization**: Simplified allocation methods across assets and strategies

Sources: [Amazon](https://www.amazon.com/Machine-Trading-Deploying-Computer-Algorithms/dp/1119219604), [Google Play](https://play.google.com/store/books/details/Machine_Trading_Deploying_Computer_Algorithms_to_C?id=FtfPDQAAQBAJ)

---

### Mean Reversion Methodology

Chan is most closely associated with mean reversion and statistical arbitrage. His framework rests on several pillars:

- **Augmented Dickey-Fuller (ADF) test**: Tests for unit roots in a spread; rejection of the null hypothesis confirms stationarity and suitability for mean-reversion trading.
- **Hurst exponent**: H < 0.5 indicates a mean-reverting series; H = 0.5 is a random walk; H > 0.5 is trending. He uses this to filter tradeable pairs.
- **Ornstein-Uhlenbeck process and half-life**: Calculates how long a spread typically takes to revert halfway to its mean, which determines optimal holding period and exit timing.
- **Trading signals**: Entry when spread deviates beyond a threshold (e.g., 2 standard deviations from mean), often implemented via Bollinger Bands on the spread rather than individual prices. Classic examples include the EWA/EWC (Australia/Canada ETF) pair and the GLD/GDX (gold/gold miners) ratio.
- **Dynamic hedge ratios via Kalman filtering**: Rather than static hedge ratios, Chan advocates adaptive ratios that update as the relationship evolves.
- **Regime detection**: Identifies when cointegrating relationships break down, signaling the strategy should be paused.

Sources: [QuantStrategy.io](https://quantstrategy.io/blog/mean-reversion-strategies-implementing-ernest-chans/), [QuantInsti webinar](https://blog.quantinsti.com/webinar-basics-of-mean-reversion-strategies-by-dr-ernest-p-chan/), [QuantConnect implementation](https://www.quantconnect.com/forum/discussion/11974/mean-reversion-pairs-trading-from-ernest-chan-039-s-algorithmic-trading-book/)

---

### Momentum Strategies

Chan treats momentum as the complement to mean reversion. His comparative framework:

- Momentum positions follow trends; mean reversion positions are contrarian.
- Stop-losses are critical for momentum (signal a reversal) but risky for mean reversion (exit before the reversion completes).
- Momentum works best in news-driven, trending markets across multiple asset classes. Academic research cited by QTS demonstrates that momentum effects persist for 3-12 months across commodities, currencies, and interest rate instruments.

Sources: [BlockEden summary](https://blockeden.xyz/blog/2025/07/26/quatitive-trading/), [QTS Capital](https://qtscm.com/)

---

### Blog: epchan.blogspot.com

Chan's blog "Quantitative Trading" at epchan.blogspot.com has been a pioneering resource for statistical arbitrage education. Notable recent themes (2025 posts) include:

- Deep latent variable models applied to factor modeling
- Feature selection using generative AI techniques
- Transformers for financial time series (self-attention mechanisms)
- Deep reinforcement learning for portfolio optimization
- LLM improvements for trading-related tasks
- Dimensionality reduction (e.g., covariance matrix of 500 stocks has 125,250 parameters; latent factors compress this)

Key historical blog posts include his seminal explanation that cointegration is not correlation (2006), Kelly formula applications (2009), Kelly vs. Markowitz portfolio optimization (2014), and cointegration trading with log prices vs. prices (2013).

Sources: [epchan.blogspot.com](http://epchan.blogspot.com/), [Kelly formula post](http://epchan.blogspot.com/2009/02/kelly-formula-revisited.html), [Cointegration post](http://epchan.blogspot.com/2006/11/cointegration-is-not-same-as.html)

---

### Companies

**QTS Capital Management, LLC (founded 2011)**: A global multi-strategy quantitative investment firm where Chan serves as non-executive chairman. Strategies include trend-following in commodities/currencies/rates, roll-yield capture from contango/backwardation patterns (targeting 200-400 bps annual roll yield in energy/agriculture), and a "Tail Reaper" strategy using 100+ features to dynamically allocate between its own signals and E-mini S&P 500 futures. The firm claims virtually zero correlation to the S&P 500 and convexity during severe equity downturns. Led by a team of mathematicians and physicists.

**PredictNow.ai (founded 2020)**: A fintech startup where Chan serves as chief scientific officer. It uses machine learning to optimize trading strategies, offering predictive insights on the probability of profit for the next trade. Chan has stated plans to expand beyond asset management into sectors like oil and gas. His key observation: "Finance is maybe the hardest domain for AI because of the low signal-to-noise ratio," which means solutions that work in finance can transfer to other industries.

Sources: [QTS Capital](https://qtscm.com/), [AlphaMaven profile](https://alpha-maven.com/industry/hedge-fund/contact-profile/ernest-chan-qts-capital-management), [Rebellion Research interview](https://www.rebellionresearch.com/dr-ernest-chan-founder-predictnow-ai-chairman-qts-capital-on-artificial-intelligence-cloud-quantum-computing-no-code-development-platforms), [Alpaca podcast](https://alpaca.markets/learn/podcast-episode3), [Mutiny Fund interview](https://mutinyfund.com/ernest-chan-qts-capital-management/)

---

### Backtesting Pitfalls

Chan has written and presented extensively on backtesting biases. He has a dedicated presentation ("Backtesting and its Pitfalls") available at epchan.com. His framework identifies three primary biases, all of which inflate backtest performance:

1. **Look-ahead bias**: Using information not available at the time of the trade (e.g., using tomorrow's prices for today's signals). Solution: use strictly lagged data. One of the most common programming errors.

2. **Survivorship bias**: Backtesting against the current stock universe rather than the historical universe (which included companies that delisted, went bankrupt, or were acquired). Chan warns that free data sources like Yahoo Finance typically have this bias; survivorship-bias-free databases are expensive.

3. **Data-snooping bias (overfitting)**: Fitting too many parameters or trading rules to historical data, then reporting only the best results. Solutions: limit the number of free parameters, enforce strict out-of-sample testing, and be suspicious of strategies that only work with very specific parameter choices.

Additional pitfalls he warns about:
- Insufficient sample sizes creating statistical unreliability
- Neglecting transaction costs and slippage
- Strategies dependent on a few large trades rather than consistent edge
- Live results typically underperform backtested returns due to slippage, latency, and market impact

Sources: [epchan.com backtesting PDF](https://epchan.com/img/links/Backtesting-and-its-Pitfalls.pdf), [BlockEden summary](https://blockeden.xyz/blog/2025/07/26/quatitive-trading/), [Sobrief summary](https://sobrief.com/books/quantitative-trading)

---

### Teaching and Influence

Chan has taught at Northwestern University and QuantInsti (as EPAT faculty), regularly mentors emerging traders, and offers workshops on mean reversion, cryptocurrency trading, and AI applications in finance. His blog was among the first to publicly reveal statistical arbitrage strategies like pairs trading, making previously institutional-grade knowledge accessible to retail quants. His Twitter/X handle is @echanQT.

Sources: [QuantInsti faculty page](https://www.quantinsti.com/faculty/ernest-chan), [Twitter/X](https://x.com/echanQT)