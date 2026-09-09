I now have comprehensive coverage across all requested topics. Here is the full research report.

---

## Academic Frameworks and Key Papers on Backtesting Methodology in Finance

### 1. Foundational Papers on Data Snooping and Multiple Testing

**Lo and MacKinlay (1990), "Data-Snooping Biases in Tests of Financial Asset Pricing Models"**
Published in *The Review of Financial Studies*, vol. 3(3), pp. 431-467. This is the seminal paper that formally identified the data-snooping problem in finance: when portfolios are sorted on empirically motivated characteristics (e.g., market cap), the resulting test statistics are biased. Both analytical and Monte Carlo results showed these biases to be substantial. This paper launched the entire literature on correcting for specification search in financial research.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227465
- Oxford Academic: https://academic.oup.com/rfs/article-abstract/3/3/431/1592120

**White (2000), "A Reality Check for Data Snooping"**
Published in *Econometrica*, vol. 68(5), pp. 1097-1126. White introduced a bootstrap procedure that tests whether the best model from a specification search has genuine predictive superiority over a benchmark, controlling for the full universe of models examined. The null hypothesis is that no alternative model is superior to the benchmark; the bootstrap accounts for dependencies among the test statistics. This remains one of the most cited multiple-testing corrections in quantitative finance.
- Econometrica: https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0262.00152

**Hansen (2005), "A Test for Superior Predictive Ability"**
Published in *Journal of Business & Economic Statistics*. Hansen refined White's Reality Check with the Superior Predictive Ability (SPA) test, which re-centers the null distribution and is less conservative -- specifically, it is less sensitive to the inclusion of clearly poor models that drag down power in White's original framework.
- ResearchGate: https://www.researchgate.net/publication/4724332_A_Test_for_Superior_Predictive_Ability

**Romano and Wolf (2005), Stepwise Multiple Testing**
Extended the framework to a stepwise procedure that controls the family-wise error rate while identifying *all* strategies that significantly outperform a benchmark, not just the single best one.

---

### 2. Harvey, Liu, and Zhu: The Multiple Testing Crisis

**Harvey, Liu, and Zhu (2016), "...and the Cross-Section of Expected Returns"**
Published in *The Review of Financial Studies*, vol. 29(1), pp. 5-68. This paper catalogued hundreds of published factors purporting to explain cross-sectional returns and argued that the conventional t-ratio threshold of 2.0 is far too low given the cumulative data mining. They provide a time series of historical significance cutoffs from 1967 onward (accounting for correlation among tests and publication bias) and conclude that new factors should clear a t-statistic of at least 3.0. The paper's stark conclusion: most claimed research findings in financial economics are likely false.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2249314
- Oxford Academic: https://academic.oup.com/rfs/article/29/1/5/1843824

**Harvey and Liu (2015), "Backtesting"**
Published in *The Journal of Portfolio Management*, Fall 2015. This companion paper operationalizes the multiple-testing framework for practitioners, introducing Sharpe ratio haircuts and in-sample/out-of-sample testing adjustments.
- Duke PDF: https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2345489

---

### 3. Bailey and Lopez de Prado: Overfitting Quantification

**Bailey, Borwein, Lopez de Prado, and Zhu (2014/2017), "The Probability of Backtest Overfitting"**
Published in *Journal of Computational Finance*. Introduced Combinatorially Symmetric Cross-Validation (CSCV), a numerical method that estimates the probability that a backtest is overfitted by partitioning the time series into sub-matrices, fitting on half and testing on the complementary half across all symmetric combinations. The key output is PBO (Probability of Backtest Overfitting), a single number between 0 and 1 that quantifies the risk. Strategies with PBO above 0.5 are considered suspect.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
- Direct PDF: https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf

**Bailey and Lopez de Prado (2014), "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality"**
Published in *The Journal of Portfolio Management*, vol. 40(5), pp. 94-107. The Deflated Sharpe Ratio (DSR) adjusts the observed Sharpe ratio for (a) the number of trials conducted (selection bias under multiple testing), (b) the non-normality of returns (skewness and kurtosis), and (c) the correlation structure of the strategies tested. It produces a deflated p-value that represents the probability of observing the reported Sharpe ratio under the null of zero skill.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
- Wikipedia: https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio

**Lopez de Prado (2018), *Advances in Financial Machine Learning* (Wiley)**
This book is the primary reference for modern ML-aware backtesting. Key chapters cover: meta-labeling, triple-barrier labeling, fractional differentiation, purged/embargoed cross-validation, combinatorial purged cross-validation, and the deflated Sharpe ratio. The book's thesis is that standard ML cross-validation fails on financial time series because of serial correlation and label leakage, and that backtesting must be treated as the final step in a carefully structured research pipeline, not a discovery tool.
- Amazon/Wiley: https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086

---

### 4. Purged and Embargoed Cross-Validation

Lopez de Prado (2017) introduced two mechanisms to prevent information leakage in k-fold CV on financial time series:

- **Purging**: Remove from the training set any observation whose label overlaps in time with labels in the test set. Financial labels often depend on future prices (e.g., a return computed over a forward window), so a training observation near the test boundary can embed information about test-set outcomes.

- **Embargo**: After purging, additionally exclude a buffer of training observations immediately following each test fold, accounting for serial correlation that decays over time but does not vanish at the fold boundary.

- **Combinatorial Purged Cross-Validation (CPCV)**: The advanced extension creates C(N,k) train/test combinations from N partitions, each with purging and embargo applied, producing a distribution of out-of-sample paths rather than a single walk-forward equity curve. This allows estimation of the PBO directly from cross-validation.

Source: https://en.wikipedia.org/wiki/Purged_cross-validation (note: Wikipedia article was returning 404 at fetch time but the content is well-documented in Lopez de Prado's book and SSRN papers)

---

### 5. Walk-Forward Optimization

Introduced by Robert E. Pardo in *Design, Testing and Optimization of Trading Systems* (1992, expanded 2008). The procedure:
1. Optimize strategy parameters on an in-sample window.
2. Apply those parameters to a reserved out-of-sample window immediately following.
3. Slide the window forward by the out-of-sample length.
4. Repeat until data is exhausted.
5. Concatenate out-of-sample results to form the "walk-forward equity curve."

Walk-forward is now considered the gold standard for strategy validation because it preserves chronological ordering and forces re-optimization across multiple market regimes. A strategy that performs well out-of-sample across many re-optimizations is considered robust.

Source: https://en.wikipedia.org/wiki/Walk_forward_optimization

---

### 6. Backtesting Protocol for the ML Era

**Arnott, Harvey, and Markowitz (2019), "A Backtesting Protocol in the Era of Machine Learning"**
Published in *Journal of Financial Data Science*, vol. 1(1), pp. 64-74. This paper proposes a structured protocol for quantitative researchers using ML, emphasizing: (a) economic motivation must precede data mining, (b) a research budget (number of trials) should be declared ex ante, (c) multiple-testing corrections must be applied, and (d) out-of-sample validation should follow a pre-registered plan. The paper explicitly warns that ML's ability to find patterns in noise is orders of magnitude greater than traditional econometrics, making disciplined backtesting protocols even more critical.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654
- Duke PDF: https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf

---

### 7. The Three Types of Backtests

**Joubert, Sestovic, Barziy, Distaso, and Lopez de Prado (2024), "The Three Types of Backtests"**
Published via ADIA Lab. This recent paper taxonomizes backtests into three categories:
1. **Walk-Forward Testing** -- the most common; sequential historical replay.
2. **Resampling** -- generates multiple alternative paths from historical data (bootstrap-based).
3. **Monte Carlo Simulation** -- synthesizes paths from estimated distributional parameters.

Each type has distinct failure modes: walk-forward suffers from single-path dependence, resampling can destroy temporal structure, and Monte Carlo depends critically on distributional assumptions. The paper recommends using all three in combination.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4897573
- ADIA Lab: https://www.adialab.ae/research-series/the-three-types-of-backtests

---

### 8. CFA Institute Guidelines

The CFA Institute includes "Backtesting and Simulation" as a formal reading in the Level II curriculum (current 2026 edition). Their framework covers:

- **Rolling-window backtesting** as the core methodology (5 steps: specify hypothesis, determine rules, form portfolio, rebalance, compute metrics).
- **Three pitfalls**: survivorship bias, look-ahead bias, and data snooping.
- **Complementary techniques**: historical scenario analysis, Monte Carlo simulation, sensitivity analysis.
- **Fat tails warning**: asset returns exhibit negative skewness and excess kurtosis, so normal-distribution assumptions understate tail risk.
- **Ethics**: CFA Standards require disclosure of material limitations and risks of hypothetical/backtested performance to clients.

Source: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation

---

### 9. Additional Noteworthy SSRN Papers

**Arakelian et al. (2024), "A Discussion Paper for Possible Approaches to Building a Statistically Valid Backtesting Framework"**
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4893677

**Arian, Norouzi, and Seco (2024), "Backtest Overfitting in the Machine Learning Era"**
Compared K-Fold, Walk-Forward, and CPCV in a synthetic controlled environment. Found that CPCV outperforms alternatives in mitigating overfitting, with lower PBO scores.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4686376
- ScienceDirect: https://www.sciencedirect.com/science/article/abs/pii/S0950705124011110

**Schumann (2019), "Backtesting"**
A practical survey of backtesting methods for portfolio strategies.
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3374195

---

### 10. Summary of Multiple-Testing Corrections Hierarchy

| Method | Controls | Power | Use Case |
|---|---|---|---|
| Bonferroni | FWER (family-wise error rate) | Lowest -- overly conservative | Few tests, zero false-positive tolerance |
| Holm-Bonferroni | FWER (stepwise) | Better than Bonferroni | Moderate number of tests |
| White's Reality Check (2000) | FWER via bootstrap | Moderate, but sensitive to poor models | Benchmark vs. many alternatives |
| Hansen's SPA (2005) | FWER via re-centered bootstrap | Higher than White's | Same setting, more power |
| Romano-Wolf Stepwise | FWER, identifies all significant | Highest FWER control | Identifying all outperformers |
| Benjamini-Hochberg | FDR (false discovery rate) | Highest overall | Large-scale exploratory search |
| Deflated Sharpe Ratio | Selection bias + non-normality | Strategy-specific | Evaluating a single "best" strategy |

The field has converged on the view that **any backtested result must be accompanied by a disclosure of the number of trials conducted**, and that raw Sharpe ratios or t-statistics without multiple-testing adjustment are essentially meaningless for strategy selection.