I now have comprehensive material. Let me compile the full report.

---

Here is the complete research report on Marcos Lopez de Prado's work on backtest overfitting and related topics.

---

## 1. KEY PUBLICATIONS

### A. "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality"

- **Authors:** David H. Bailey, Marcos Lopez de Prado
- **SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
- **Journal publication:** The Journal of Portfolio Management, 40(5): 94-107, 2014
- **Direct PDF (Bailey's site):** https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf
- **Related companion paper ("Deflating the Sharpe Ratio"):** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2465675

**What it says:** The DSR corrects for two leading sources of performance inflation: (1) selection bias under multiple testing -- when researchers test many strategies and report only the best, the winner is likely a statistical fluke; and (2) non-normally distributed returns (skewness and kurtosis). The DSR deflates the observed Sharpe ratio by the number of independent trials conducted, the variance of Sharpe ratio estimates across those trials, the sample length, and non-normality of returns. A strategy showing a backtested Sharpe of 1.0 might deflate to 0.4 or lower after correction. The DSR builds on the Probabilistic Sharpe Ratio (PSR), which itself adjusts for skewness, kurtosis, and sample length.

**2025 follow-up:** Lopez de Prado, Alexander Lipton, and Vincent Zoonekynd published "How to Use the Sharpe Ratio" (September 2025) synthesizing the full inference framework (PSR, MinTRL, DSR, oFDR). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5520741 -- with replication code at https://github.com/zoonek/2025-sharpe-ratio. In 2026, he also posted seminar slides "Sharpe Ratio Inference: A New Standard for Decision-Making and Reporting" at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5950754.

---

### B. "Advances in Financial Machine Learning" (Wiley, 2018)

- **Publisher page:** https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086
- **SSRN Chapter 1 excerpt:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104847
- **ISBN:** 978-1-119-48208-6

**Key concepts from the book:**

1. **Fractional Differentiation** -- Uses non-integer-order differencing (backshift operators with binomial-coefficient weights) to make financial time series stationary while preserving long-range memory. Finds the minimum differencing parameter d that achieves stationarity without discarding excess information. Solves the stationarity-vs-memory tradeoff that integer differencing (d=1) destroys.

2. **Triple Barrier Method** -- A labeling technique placing three barriers around each observation: a profit-take (upper), a stop-loss (lower), and an expiration (vertical/time). The label is determined by which barrier price hits first: +1 for profit target, -1 for stop loss, and sign(return) or 0 at expiration. Incorporates realistic trading mechanics (path-dependent, not just endpoint returns) and dynamically sets barriers based on per-observation volatility.

3. **Meta-Labeling** -- A two-stage classification approach. Stage 1: train a high-recall model to identify the side of the bet (buy/sell). Stage 2: train a secondary binary classifier to determine whether to actually place the bet (bet sizing). This separates directional forecasting from position-sizing decisions, correcting for low precision without sacrificing recall.

4. **Combinatorial Purged Cross-Validation (CPCV)** -- Standard k-fold CV leaks information in financial time series because labels overlap in time. Purged k-fold CV removes training samples temporally close to test samples and adds an embargo gap. CPCV generalizes this: it partitions observations into N ordered groups, selects k groups for testing (yielding C(N,k) possible splits), and combines test sets from different splits into ordered backtest paths. This generates many backtest paths, enabling direct estimation of the probability of backtest overfitting.

5. **Information-Driven Bars** -- Tick/volume/dollar imbalance bars that sample based on informed trading activity rather than fixed time intervals, producing returns with more favorable statistical properties.

6. **Hierarchical Risk Parity (HRP)** -- A portfolio construction method using graph theory and machine learning (hierarchical clustering on the correlation matrix) instead of mean-variance optimization. Does not require matrix inversion, works on singular covariance matrices, and produces lower out-of-sample variance than Markowitz CLA in Monte Carlo tests. SSRN paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678

---

### C. "The Probability of Backtest Overfitting" (PBO)

- **Authors:** David H. Bailey, Jonathan M. Borwein, Marcos Lopez de Prado, Qiji Jim Zhu
- **SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
- **Journal:** Journal of Computational Finance, February 2015
- **Also at:** https://escholarship.org/uc/item/4w1110bb and Western Michigan University: https://scholarworks.wmich.edu/math_pubs/42/
- **Mathematical Appendices:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2568435
- **Open-source Python implementation (pypbo):** https://github.com/esvhd/pypbo

**What it says:** Standard overfitting controls (hold-out, k-fold) are unreliable for investment backtests. The authors propose Combinatorially Symmetric Cross-Validation (CSCV), a numerical method that estimates the probability that a given backtest is overfit. CSCV partitions historical data into subsets, evaluates strategy performance across all combinatorial splits, and computes the fraction of configurations where in-sample optimality does not translate to out-of-sample performance. The framework demonstrates that the act of searching over many strategy configurations makes out-of-sample disappointment a statistically predictable outcome unless the research process is explicitly controlled and corrected.

---

### D. "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance"

- **Authors:** David H. Bailey, Jonathan M. Borwein, Marcos Lopez de Prado, Qiji Jim Zhu
- **SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308659
- **Published in:** Notices of the American Mathematical Society, 61(5): 458-471, May 2014
- **Full text (AMS):** https://www.ams.org/notices/201405/rnoti-p458.pdf
- **Western Michigan University repository:** https://scholarworks.wmich.edu/math_pubs/40/

**What it says:** The paper proves that high simulated performance is easily achievable after backtesting a relatively small number of alternative strategy configurations. Using just five years of historical data, testing as few as 45 portfolio configurations virtually guarantees finding one with an artificially inflated Sharpe ratio that will not hold out-of-sample. Because most financial analysts and academics rarely report the number of configurations tried, investors cannot evaluate the degree of overfitting. The authors assert that backtesting overfitting is widespread in both academic finance and commercial investment products, and they criticize mathematicians for remaining silent while investment professionals misuse statistical techniques, calling that silence complicity.

---

### E. Full SSRN Paper Inventory (Backtesting/Overfitting cluster)

| Paper | SSRN ID | URL |
|-------|---------|-----|
| What to Look for in a Backtest | 2308682 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308682 |
| Pseudo-Mathematics and Financial Charlatanism | 2308659 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2308659 |
| The Probability of Backtest Overfitting | 2326253 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 |
| The Deflated Sharpe Ratio | 2460551 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551 |
| Deflating the Sharpe Ratio | 2465675 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2465675 |
| Optimal Trading Rules Without Backtesting (with Peter Carr) | 2502613 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2502613 |
| Mathematical Appendices to PBO | 2568435 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2568435 |
| Backtesting (survey chapter) | 2606462 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2606462 |
| Determining Optimal Trading Rules Without Backtesting (with Carr, revised) | 2658641 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2658641 |
| Building Diversified Portfolios that Outperform Out-of-Sample (HRP) | 2708678 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678 |
| Stock Portfolio Design and Backtest Overfitting | 2739335 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2739335 |
| Backtest Overfitting in Financial Markets | 2731886 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2731886 |
| How Hard Is It to Pick the Right Model? MCS and Backtest Overfitting | 3044740 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3044740 |
| The 7 Reasons Most ML Funds Fail (slides) | 3031282 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3031282 |
| The 10 Reasons Most ML Funds Fail | 3104816 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104816 |
| AFML Chapter 1 | 3104847 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104847 |
| Tactical Investment Algorithms | 3459866 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3459866 |
| Escaping The Sisyphean Trap | 3916692 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3916692 |
| Causal Factor Investing | 4205613 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4205613 |
| Where are the Factors in Factor Investing? | 4336002 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4336002 |
| Ranking Empirical Evidence in Finance | 4425855 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4425855 |
| Overcoming Markowitz's Instability with HRP (with Antonov, Lipton) | 4748151 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4748151 |
| How to Use the Sharpe Ratio (with Lipton, Zoonekynd) | 5520741 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5520741 |
| Sharpe Ratio Inference (2026 seminar slides) | 5950754 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5950754 |

His SSRN author page: https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=434076 (ranked among the 10 most-read authors in Economics on SSRN).

---

## 2. CURRENT AFFILIATION

Your guess was correct -- both Cornell and Abu Dhabi Investment Authority. Full picture:

- **Abu Dhabi Investment Authority (ADIA)** -- Global Head of Quantitative R&D. ADIA is one of the world's largest sovereign wealth funds.
- **ADIA Lab** -- Founding board member. Abu Dhabi's research center for data and computational sciences. Bio page: https://www.adialab.ae/bios/professor-marcos-lopez-de-prado
- **Cornell University** -- Professor of Practice, College of Engineering (teaches ORIE 5256, Special Topics in Financial Engineering). Also FinTech Faculty at the School of Business.
- **Khalifa University of Science and Technology** -- Professor of Practice, Department of Mathematics.
- **Lawrence Berkeley National Laboratory** -- Research Fellow, Office of Science (U.S. Department of Energy). Has held this since 2011.
- **The Journal of Financial Data Science** -- Founding co-editor.

**Prior roles (not current):**
- Guggenheim Partners -- Senior Managing Director, founded Quantitative Investment Strategies (~$13B AUM, information ratio of 2.3)
- AQR Capital Management -- Partner and first Head of Machine Learning
- True Positive Technologies -- Founder (advisory clients with >$1T combined assets, patent licensing valued at eight figures)

**Education:** Two PhDs from Universidad Complutense de Madrid -- financial econometrics (2003) and mathematical finance (2011, received Extraordinary PhD Award in 2013). Postdoctoral research at Harvard and Cornell.

**Recent honors:**
- International Member, Spain's Royal Academy of Engineering (elected 2026) -- lifetime distinction held by only 71 scientists worldwide. Press release: http://www.prnewswire.com/news-releases/spains-royal-academy-of-engineering-elects-professor-marcos-lopez-de-prado-as-international-member-302816778.html
- Knight Officer of the Royal Order of Civil Merit, appointed by King Felipe VI (2024)
- Bernstein Fabozzi/Jacobs Levy Award (2024), Journal of Portfolio Management
- Buy-Side Quant of the Year (2021), Risk.net
- Erdos number of 2; Einstein number of 4
- 15 patents; testified before U.S. Congress on AI policy; over 100 published journal articles

Full CV: https://www.quantresearch.org/Vita.htm

---

## 3. TALKS, PRESENTATIONS, AND INTERVIEWS

### YouTube Talks
- **"Dangers of Backtest Overfitting"** (April 2016): https://www.youtube.com/watch?v=QxhxLwNbMMg
- **"How Overfit Is Your Backtest?"** (June 2026, survey of the PBO body of work): https://www.youtube.com/watch?v=T-W0OzzoMKM
- **"The Dangers of Backtesting" (Book Chapter 11)**: https://www.youtube.com/watch?v=sGcov6tOQ7k

### Major Interview
- **CFA Institute: "Conversations with Frank Fabozzi, CFA" featuring Marcos Lopez de Prado** (March 18, 2025). Topics: responsible AI use in finance, factor investing limitations, causal inference models. URL: https://rpc.cfainstitute.org/research/multimedia/2025/conversations-with-frank-fabozzi-featuring-marcos-lopez-de-prado (also at https://www.cfainstitute.org/insights/events/2025/frank-fabozzi-marcos-lopez-de-prado-webinar)

### Conference Keynotes
- **Fordham Quant** keynote speaker (January 2026)
- **QuantCon 2018** keynote (the "7 Reasons Most ML Funds Fail" talk; discussed on EliteTrader: https://www.elitetrader.com/et/threads/the-7-reasons-most-machine-learning-funds-fail-marcos-lopez-de-prado-from-quantcon-2018.331987/)
- **Quant Strats UK**: https://www.alphaevents.com/events-quantstratsuk/speakers/marcos-lopez-de-prado

### Full Lecture Archive (2012-2026)
His complete lectures page at https://quantresearch.org/Lectures.htm lists 60+ presentations with SSRN slide links. Highlights by year:

- **2026:** "What is the False Discovery Rate in Finance?"; "Sharpe Ratio Inference: A New Standard"
- **2025:** "Investment Lessons from Cosmology"; "Causal AI & Sustainability"; "Financial Machine Learning: An Engineering Problem"; "AI Challenges in Mathematical Investing"
- **2024:** "Causal Factor Analysis"; "The Role of Causal Inference"; "Why Has Factor Investing Failed?"
- **2021:** "Detection of False Investment Strategies through FWER and FDR"
- **2020:** "Overfitting: Causes and Solutions"; "Three Quant Lessons from COVID-19"
- **2018:** "A Practical Solution to the Multiple-Testing Crisis in Financial Research"; "How the Sharpe Ratio Died, But Came Back to Life"
- **2015:** "Backtesting"; "Illegitimate Science: Why Most Empirical Discoveries in Finance Are Likely Wrong"
- **2014:** "Deflating the Sharpe Ratio"; "Optimal Trading Rules Without Backtesting"
- **2013:** "What to Look for in a Backtest"

### Notable Quote (from X/Twitter, 2019)
Lopez de Prado on backtesting philosophy: "If a strategy does not perform well in a backtest, do not tweak it (overfit) until the backtest looks good. Instead, investigate how the research process misled you into backtesting a false strategy. Fix the research process, not the strategy." (Source: https://x.com/lopezdeprado/status/1138716396248915968)

---

## Books (Complete List)

1. **Advances in Financial Machine Learning** (Wiley, 2018) -- the standard graduate reference
2. **Machine Learning for Asset Managers** (Cambridge University Press, Elements in Quantitative Finance, 2020) -- focuses on clustering and portfolio construction for practitioners
3. **Causal Factor Investing** (Cambridge University Press, 2023) -- causal inference applied to factor investing