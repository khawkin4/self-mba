I now have comprehensive research across all three parts. Here is the full report:

---

## PART 1: Harvey, Liu, Zhu -- "...and the Cross-Section of Expected Returns"

### The Core Paper

**Title:** "...and the Cross-Section of Expected Returns"
**Authors:** Campbell R. Harvey, Yan Liu, Heqing Zhu
**Publication:** Review of Financial Studies, Volume 29, Issue 1, January 2016, Pages 5-68
**DOI:** 10.1093/rfs/hhv059
**NBER Working Paper:** No. 20592 (October 2014)
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2249314 (earlier version) and https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2513152
**NBER:** https://www.nber.org/papers/w20592
**PDF:** https://www.nber.org/system/files/working_papers/w20592/w20592.pdf

**Core Argument:** The paper documents that researchers had published at least 316 factors claimed to predict stock returns between 1967 and 2014, with publication rates accelerating from a handful per year in the 1970s-80s to over 40 per year by the 2010s. The standard academic practice accepts factors with t-statistics above 2.0 as significant. However, when hundreds of factors are tested on overlapping datasets, approximately 16 would appear significant purely by chance even if none were real. The authors argue that most claimed research findings in financial economics are likely false -- echoing a parallel conclusion from the medical literature (Ioannidis 2005).

**Proposed T-Statistic Thresholds:**
- Original standard: t > 2.0
- By 2012 (given cumulative testing): t > 3.0 minimum for credibility
- The threshold rises over time as cumulative testing increases false discovery risk
- The paper provides a time series of historical significance cutoffs from 1967 forward and projects 20 years ahead

**Statistical Framework:** The paper applies three multiple testing corrections:
- Bonferroni correction (most conservative)
- Holm correction (moderately conservative)
- Benjamini-Hochberg-Yekutieli method (controls false discovery rate)
The method allows for correlation among the tests as well as missing data.

**Factors Most Likely Genuine:** Established factors like the original Fama-French factors (market, size, value) and momentum show t-statistics well above 3.0 and survive the higher threshold. Exotic or niche factors typically fail.

**Source:** https://foxholm.com/q/research/harvey-liu-zhu-cross-section/

### The "Factor Zoo" Problem

**Title:** "A Census of the Factor Zoo"
**Authors:** Campbell R. Harvey, Yan Liu
**SSRN:** https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3712479_code16198.pdf?abstractid=3341728

Harvey documented that the rate of factor production is out of control, with over 400 factors published in top journals. Many are false discoveries -- lucky findings that exploit data mining rather than genuine economic relationships. The incentive structure of academic publishing (journals prefer novel, significant results) exacerbates the problem.

### Campbell Harvey's Other Work on This Topic

Harvey's research page (https://people.duke.edu/~charvey/research.htm) lists a comprehensive body of work:

1. **"Backtesting"** (2015) -- with Yan Liu. Journal of Portfolio Management, 42:1, 13-28. Won the 2016 Bernstein Fabozzi/Jacobs Levy Award. Proposes an alternative to the commonly practiced 50% discount applied to reported Sharpe ratios. Provides a Sharpe ratio "haircut" methodology and a profit hurdle that any strategy needs to achieve to be deemed significant.
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2345489
   - PDF: https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF

2. **"Multiple Testing in Economics"** (2013) -- with Yan Liu. Proposes a framework for multiple hypothesis testing in economics research, allowing for correlation among tests and incomplete data.
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2358214

3. **"False (and Missed) Discoveries in Financial Economics"** (2020) -- with Yan Liu. Journal of Finance, 75:5, 2503-2553. Proposes a double bootstrap method to establish a t-statistic hurdle associated with a specific false discovery rate (e.g., 5%). Addresses both Type I errors (false positives) and Type II errors (missed genuine discoveries).
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073799
   - Wiley: https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12951
   - arXiv: https://arxiv.org/abs/2006.04269

4. **"An Evaluation of Alternative Multiple Testing Methods for Finance Applications"** (2020) -- with Yan Liu, Alessio Saretto. Review of Asset Pricing Studies, 10:2, 199-248.
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3480087

5. **"Lucky Factors"** (2021) -- with Yan Liu. Journal of Financial Economics, 141:2, 413-435. Proposes a bootstrap model selection framework that accounts for multiple hypothesis testing.

6. **"A Backtesting Protocol in the Era of Machine Learning"** (2019) -- with Rob Arnott and Harry Markowitz. Journal of Financial Data Science, 1:1, 64-74. Develops a research protocol for ML applications in finance, addressing p-hacking through multiple testing.
   - SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654
   - PDF: https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf

7. **"Presidential Address: The Scientific Outlook in Financial Economics"** (2017). Journal of Finance, 72:4, 1399-1440. Harvey's AFA presidential address covering the broader crisis in financial economics research methodology.
   - SSRN: https://www.ssrn.com/abstract=2893930
   - Wiley: https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12530

8. **"Replication in Financial Economics"** (2020). Critical Finance Review, 8:1-2, 1-9.

---

## PART 2: Bailey, Borwein, Lopez de Prado, Zhu

### Probability of Backtest Overfitting (PBO)

**Title:** "The Probability of Backtest Overfitting"
**Authors:** David H. Bailey, Jonathan M. Borwein, Marcos Lopez de Prado, Qiji Jim Zhu
**Published:** Journal of Computational Finance (Risk Journals), 2015
**Originally posted:** September 1, 2013
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
**Full PDF:** https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
**WMU ScholarWorks:** https://scholarworks.wmich.edu/math_pubs/42/
**Mathematical Appendices SSRN:** https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2568435_code434076.pdf?abstractid=2568435

**Key Argument:** Standard statistical techniques designed to prevent regression overfitting (such as hold-out) are unreliable in the context of investment backtests. The authors propose a general framework to estimate the probability that a particular backtest is overfit, using Combinatorially Symmetric Cross-Validation (CSCV).

### The CSCV Method

CSCV works as follows:
1. Takes a matrix M of returns across N alternative strategy configurations and T time periods
2. Partitions the data into S sub-samples
3. Generates all combinatorial splits into in-sample and out-of-sample halves
4. For each split, identifies the best-performing configuration in-sample and measures its out-of-sample performance
5. Computes PBO as the proportion of splits where the in-sample optimal configuration underperforms out-of-sample

**Outputs:**
- PBO: probability that in-sample performance will not replicate out-of-sample
- Performance degradation: gap between backtested and expected forward performance
- Probability of loss: risk that the strategy will lose money
- Stochastic dominance: comparative strategy rankings

**R Package:** The `pbo` CRAN package implements CSCV: https://cran.r-project.org/web/packages/pbo/readme/README.html
**Python Package:** https://github.com/esvhd/pypbo

### "Pseudo-Mathematics and Financial Charlatanism"

**Title:** "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance"
**Authors:** David H. Bailey, Jonathan Borwein, Marcos Lopez de Prado, Qiji Jim Zhu
**Published:** Notices of the American Mathematical Society, 2014
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308659
**WMU ScholarWorks:** https://scholarworks.wmich.edu/math_pubs/40/

**Key Finding:** High simulated performance is easily achievable after backtesting a relatively small number of alternative strategy configurations. The higher the number of configurations tried, the greater the probability that the backtest is overfit. Because analysts rarely report the number of configurations tried, investors cannot evaluate the degree of overfitting in most investment proposals.

### The Deflated Sharpe Ratio (DSR)

**Title:** "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality"
**Authors:** David H. Bailey, Marcos Lopez de Prado
**Published:** Journal of Portfolio Management, 40(5), pp. 94-107, July 2014
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
**PDF:** https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf

**What It Does:** The DSR corrects for two leading sources of performance inflation: (1) selection bias under multiple testing, and (2) non-normally distributed returns. It computes a probabilistic Sharpe ratio (PSR) -- the probability that an estimated SR exceeds a benchmark SR -- then deflates it to account for the number of trials conducted.

**Related:** "Deflating the Sharpe Ratio" -- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2465675

### Minimum Backtest Length (MinBTL)

Bailey and Lopez de Prado proposed the MinBTL metric to determine the minimum number of years of backtest data needed to avoid selecting a strategy with a high in-sample Sharpe ratio but zero or negative out-of-sample performance. This directly connects to the DSR framework.

### Statistical Overfitting and Backtest Performance

**Authors:** David H. Bailey, Stephanie Ger, Marcos Lopez de Prado, Alexander Sim, Kesheng Wu
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2507040
**PDF:** https://sdm.lbl.gov/oapapers/ssrn-id2507040-bailey.pdf

### Lopez de Prado's "10 Reasons Most Machine Learning Funds Fail"

**Published:** Journal of Portfolio Management, 44:6, 120, January 2018
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104816

Key backtesting-related pitfalls include:
1. **The Sisyphus Paradigm** -- siloed PhD approach where each person independently produces a strategy, leading to overfitting
2. **Research Through Backtesting** -- treating backtesting as a research tool rather than a validation tool; backtesting is not research
3. **Chronological Sampling** -- improper time-series splitting
4. **Cross-Validation Leakage** -- standard k-fold CV leaks information in financial time series
5. **Fixed-Time Horizon Labeling** -- arbitrary labeling windows
6. **Learning Side and Size Simultaneously** -- conflating direction and magnitude
7. **Weighting of Non-IID Samples** -- treating dependent financial observations as independent

Earlier presentation version (7 reasons): SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3031282

### Advances in Financial Machine Learning (Book)

Lopez de Prado's 2018 book (Wiley) consolidates these methods, including purged cross-validation with embargo as the recommended approach for financial ML validation.

---

## PART 3: General Academic Work on Backtesting Pitfalls

### Walk-Forward Testing / Walk-Forward Optimization

**Origin:** Robert E. Pardo, "Design, Testing and Optimization of Trading Systems" (1st ed. 1992, 2nd ed. 2008, Wiley). ISBN: 0-471-55446-4 (1st ed.), 978-0-470-12801-5 (2nd ed.).

**Methodology:**
1. Optimize strategy parameters using in-sample historical data over a defined time window
2. Test the resulting parameters on the immediately following out-of-sample period
3. Record results
4. Roll forward by shifting the entire window
5. Repeat until reaching the end of available data
6. Aggregate all out-of-sample results to assess robustness

**Two Variants:**
- **Anchored WFO:** Each walk has a common beginning point; training window grows over time
- **Non-anchored (Rolling) WFO:** Each walk has a different starting point but the same training window length

**Why It Matters:** Walk-forward analysis simulates how a strategy would have actually performed if deployed with periodic reoptimization. It is the test that overfit strategies cannot pass. Unlike a single train/test split, it produces multiple out-of-sample periods, giving a distribution of performance rather than a single point estimate.

**Sources:**
- Wikipedia: https://en.wikipedia.org/wiki/Walk_forward_optimization
- Interactive Brokers: https://www.interactivebrokers.com/campus/ibkr-quant-news/the-future-of-backtesting-a-deep-dive-into-walk-forward-analysis/
- QuantInsti: https://blog.quantinsti.com/walk-forward-optimization-introduction/

### Out-of-Sample Validation for Time Series

**Why Standard Train/Test Splits Are Problematic:**
1. **Non-stationarity:** Financial time series have changing statistical properties. Parameters estimated on one period do not apply to different market dynamics.
2. **Temporal dependence:** Observations are not independent; shuffling data violates the time structure.
3. **Single regime risk:** A single fixed split may land entirely within one market regime, producing results that do not generalize.
4. **Look-ahead risk with random splits:** Even when folds are kept ordered, cross-validation can produce runs where the validation set occurs before the training set.

**Proper Approaches:**
- Rolling/expanding window splits with a time lag between training and test sets
- Walk-forward validation (see above)
- Purged cross-validation with embargo (see below)

**Source:** https://medium.com/balaena-quant-insights/train-test-split-cross-validation-and-walk-forward-testing-for-on-chain-factors-b5fcf01572e2

### Cross-Validation for Financial Time Series

**Why Standard K-Fold Fails:**
- Assumes observations are independent (financial observations are not)
- Financial labels are often built over overlapping time windows
- Random shuffling lets the model see future information, causing data leakage
- Results in inflated performance metrics

**Purged Cross-Validation (Lopez de Prado, 2017):**
- Developed at Guggenheim Partners / Cornell University
- **Purging:** Removes from the training set any observation whose label overlaps in time with labels in the testing set
- **Embargo:** Excludes training observations within a specified time window after the testing set to prevent serial correlation leakage
- Reduces risk of inflated metrics from overlapping information
- Ensures the model evaluates only on truly unseen data

**Combinatorial Purged Cross-Validation (CPCV):**
- Extension using k-p folds for training where p > 1 allows multiple test folds
- Generates thousands of train/test splits so every part of the series is tested multiple times
- Shown to have lower PBO and superior DSR test statistics compared to traditional methods
- Overcomes the limitation of walk-forward CV that produces only a single backtest path

**Key Sources:**
- Medium (pitfalls): https://bhakta-works.medium.com/the-pitfalls-of-standard-cross-validation-in-financial-machine-learning-aec03f672179
- GitHub (scikit-learn compatible implementation): https://github.com/eslazarev/purged-cross-validation
- Trading Interview: https://www.tradinginterview.com/courses/machine-learning/lessons/cross-validation-for-financial-data-purging-and-embargoing/
- Towards AI: https://towardsai.com/p/l/the-combinatorial-purged-cross-validation-method

### Survivorship Bias

**Definition:** Testing strategies only on assets that exist today, ignoring those that were delisted, went bankrupt, or were acquired during the test period.

**Key Academic Reference:** Elton, Gruber, Blake -- "Survivorship Bias and Mutual Fund Performance," Review of Financial Studies, 1996, Volume 9, Pages 1097-1120.
- SSRN: https://www.ssrn.com/abstract=6701
- Oxford Academic: https://academic.oup.com/rfs/article-abstract/9/4/1097/1580100

**Quantitative Impact:**
- Elton, Gruber, Blake found survivorship bias overstated average mutual fund returns by roughly 0.9% per year
- Bianchi and Koutmos found a 2.1% annual overestimation during the 2008 financial crisis
- Over a 10-year backtest, ~1% per year accumulates into the difference between a mediocre and apparently good strategy

**Related Work:** Carhart, Carpenter, Lynch, Musto -- "Mutual Fund Survivorship," Review of Financial Studies, 2002.
- PDF: https://pages.stern.nyu.edu/~alynch/pdfs/rfs02cclm.pdf

**How to Mitigate:** Use survivorship-bias-free datasets (available from institutional data vendors like CRSP) that include delisted and bankrupt companies with their full return history including delisting returns.

**Sources:**
- LuxAlgo: https://www.luxalgo.com/blog/survivorship-bias-in-backtesting-explained/
- Bookmap: https://bookmap.com/blog/survivorship-bias-in-market-data-what-traders-need-to-know
- CFA (AnalystPrep): https://analystprep.com/study-notes/cfa-level-2/problems-in-backtesting/
- Apollo-8: https://www.apollo-8.ch/post/why-backtests-lie

### Look-Ahead Bias

**Definition:** Using information in a backtest that would not have been available at the time the trade decision was made.

**Common Examples:**
1. **Restated earnings data:** Company reports Q2 earnings in July, revises in September. If the backtest uses the revised figure when evaluating a signal generated in August, it incorporates future information.
2. **Index membership changes:** Testing a strategy on "the S&P 500" using today's constituents rather than the constituents as they existed on each historical date.
3. **Future price data in indicators:** Computing moving averages or indicators using future closing prices.
4. **Point-in-time data issues:** Using financial statement data before its actual publication date. Swiss real estate fund reports show a median 73-day delay between fiscal-year close and release.

**Impact:** Even a single bar of future data leaking into a signal calculation can produce equity curves that look institutional-grade but collapse immediately in live trading.

**How to Mitigate:** Use point-in-time databases that record the actual publication timestamp of each data item, not just the reference period. Verify all data timestamps and release dates. Conduct code reviews for time-alignment errors.

**Sources:**
- Wall Street Mojo: https://www.wallstreetmojo.com/look-ahead-bias/
- Michael Harris (Medium): https://mikeharrisny.medium.com/look-ahead-bias-in-backtests-and-how-to-detect-it-ad5e42d97879
- MarketCalls: https://www.marketcalls.in/machine-learning/understanding-look-ahead-bias-and-how-to-avoid-it-in-trading-strategies.html
- arXiv (2025, LLM-specific): https://arxiv.org/pdf/2605.24564

### Transaction Cost Modeling in Backtests

**The Problem:** Ignoring trading frictions (commissions, bid-ask spreads, slippage, market impact) flatters backtest results. A strategy whose edge disappears at 20 bps of costs per trade has no genuine edge.

**Cost Components:**
- **Explicit costs:** Commissions, exchange fees, taxes (fixed schedule, easily modeled)
- **Implicit costs:** Market impact and slippage (account for the majority of total transaction costs, extremely challenging to model precisely)

**Key Market Impact Models:**

1. **Almgren-Chriss (2000):** Foundational framework for optimal trade execution. Balances permanent market impact (lasting price changes), temporary market impact (immediate price changes), and timing risk. Produces a closed-form optimal trading trajectory (hyperbolic sine function).
   - Original paper: https://www.smallake.kr/wp-content/uploads/2016/03/optliq.pdf
   - Overview: https://questdb.com/glossary/optimal-execution-strategies-almgren-chriss-model/

2. **Almgren et al. (2005) Structural Model:**
   Cost = (I/2) x sign(n) x mu x sigma x |n/(V x T)|^(3/5)
   With calibrated parameters gamma = 0.314, eta = 0.142

3. **Northfield Model (2009):** Square-root scaling: c = B|n| + C|n|^0.5 (R-squared = 0.7989)

4. **Frazzini, Israel, Moskowitz (2017):** Empirical study of $1.7 trillion in live trades found median transaction cost of 4.9 bps for U.S. stocks, with ~85% being permanent price impact. Costs rise to ~40 bps for trades at 10% of typical volume.

5. **Roll (1984):** Effective spread estimation from serial price correlation.

**Empirical Benchmarks:** Engle, Ferstenberg, Russell (2012) found averages of 8.8 bps (NYSE) and 13.8 bps (NASDAQ).

**Strategy-Specific Effects:** Trend-following strategies suffer most from slippage; mean reversion strategies suffer least.

**Sources:**
- BSIC Bocconi: https://bsic.it/modelling-transaction-costs-and-market-impact/
- BSIC PDF: https://bsic.it/wp-content/uploads/2023/04/Modelling-transaction-costs-for-pdf.pdf
- BSIC Backtesting Series: https://bsic.it/backtesting-series-episode-5-transaction-cost-modelling/
- QuantStart: https://www.quantstart.com/articles/Successful-Backtesting-of-Algorithmic-Trading-Strategies-Part-II/
- Exegy: https://www.exegy.com/avoiding-slippage-equities-trading-with-backtesting/
- ResearchGate: https://www.researchgate.net/publication/384458498_The_impact_of_transactions_costs_and_slippage_on_algorithmic_trading_performance

### Additional: The Seven Sins of Quantitative Investing

**Source:** Luo, Yin, M. Alvarez, S. Wang, J. Jussa, A. Wang, G. Rohal (2014). Deutsche Bank Markets Research.
- PDF: https://hudsonthames.org/wp-content/uploads/2022/01/DB-201409-Seven_Sins_of_Quantitative_Investing.pdf
- Summary: https://portfoliooptimizationbook.com/book/8.2-seven-sins.html

The seven sins:
1. Survivorship bias
2. Look-ahead bias
3. Storytelling bias (ex-post narrative creation)
4. Overfitting and data snooping
5. Turnover and transaction costs
6. Outliers (strategy success depending on rare events)
7. Asymmetric pattern and shorting cost (assuming unlimited cheap short-selling)

### Additional: Regime Change / Non-Stationarity

Strategies calibrated on one historical period learn rules specific to that era and fail when conditions change. This is a fundamental limitation of all backtesting. Detection methods include the Zivot-Andrews test (one structural break) and Bai-Perron method (multiple breaks). Segmented analysis -- splitting the series into pre- and post-break periods -- is the standard mitigation.

**Sources:**
- arXiv: https://arxiv.org/html/2602.00073v1
- PapersWithBacktest: https://paperswithbacktest.com/course/structural-breaks-financial-time-series

---

## Summary of Key SSRN Paper Links

| Paper | SSRN ID | URL |
|---|---|---|
| Harvey, Liu, Zhu -- "...and the Cross-Section of Expected Returns" | 2249314 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2249314 |
| Harvey, Liu -- "Multiple Testing in Economics" | 2358214 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2358214 |
| Harvey, Liu -- "False (and Missed) Discoveries" | 3073799 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073799 |
| Harvey, Liu -- "Backtesting" | 2345489 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2345489 |
| Harvey -- "Presidential Address" | 2893930 | https://www.ssrn.com/abstract=2893930 |
| Harvey, Liu, Saretto -- "Evaluation of Multiple Testing Methods" | 3480087 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3480087 |
| Harvey, Liu -- "Census of the Factor Zoo" | 3341728 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3341728 |
| Arnott, Harvey, Markowitz -- "Backtesting Protocol" | 3275654 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654 |
| Bailey, Borwein, LdP, Zhu -- "Probability of Backtest Overfitting" | 2326253 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 |
| Bailey, Borwein, LdP, Zhu -- "Pseudo-Mathematics" | 2308659 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308659 |
| Bailey, LdP -- "Deflated Sharpe Ratio" | 2460551 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551 |
| LdP -- "Deflating the Sharpe Ratio" | 2465675 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2465675 |
| Bailey et al. -- "Statistical Overfitting and Backtest Performance" | 2507040 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2507040 |
| LdP -- "10 Reasons ML Funds Fail" | 3104816 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104816 |
| Elton, Gruber, Blake -- "Survivorship Bias" | 6701 | https://www.ssrn.com/abstract=6701 |