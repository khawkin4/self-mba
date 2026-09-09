I now have comprehensive findings. Here is the full research report.

---

## AQR Capital Management Research: Backtesting, Factor Investing, and Data Mining

### 1. CLIFF ASNESS'S BLOG POSTS / PERSPECTIVES ON DATA MINING AND BACKTESTING

These are from AQR's "Cliff's Perspective" blog series, authored by Cliff Asness directly.

**A. "Lies, Damned Lies, and Data Mining"** (April 12, 2017)
- URL: https://www.aqr.com/Insights/Perspectives/Lies-Damned-Lies-and-Data-Mining
- PDF: https://www.aqr.com/-/media/AQR/Documents/Insights/Perspectives/Lies-Damned-Lies-and-Data-Mining.pdf
- This is the single most directly relevant piece. Asness defends AQR against Rob Arnott's Bloomberg/Businessweek accusation that AQR's factors are data-mined. Key arguments:
  - Data mining (finding random in-sample patterns that don't repeat) is a real problem: "Random doesn't tend to repeat so data mining often fails to produce attractive real life returns going forward."
  - AQR believes in a **limited** set of genuine factors meeting three criteria: (1) strong in-sample AND out-of-sample evidence across time/geography/asset classes, (2) economic stories explaining why they work, (3) theoretical models with testable implications.
  - For equities, AQR identifies **three core factors**: value, momentum, and quality. Asness explicitly rejects many popular anomalies (small-firm effects, January effects).
  - Using multiple measures per factor theme is **robust measurement, not overfitting**: "Averaging across a host of similar related measures can reduce [measurement] errors."
  - Rejects Arnott's "richening" critique (that researchers mistake factor characteristic appreciation for repeatable returns) by showing turnover effects undercut the critique.

**B. "It's Not Data Mining -- Not Even Close"** (June 2, 2015)
- URL: https://www.aqr.com/cliffs-perspective/it-is-not-data-mining-not-even-close
- Asness presents out-of-sample performance data for SMB, HML, and UMD:
  - In-sample (1927-1991): SMB 2.8-3.2%, HML 4.7-5.1%, UMD 8.9-10.1%
  - Out-of-sample (1992-2015): SMB 2.6%, HML 3.6%, UMD 6.1%
  - All spreads remained economically meaningful with statistically insignificant decay.
- Core argument: "If a researcher discovered an empirical result only because she tortured the data until it confessed, one would not expect it to work outside the torture zone."
- Acknowledges Fischer Black's 1990 skepticism was reasonable at the time but is now obsolete given decades of out-of-sample confirmation.

**C. "Factor Timing is Hard"** (March 15, 2017)
- URL: https://www.aqr.com/cliffs-perspective/factor-timing-is-hard
- PDF: https://images.aqr.com/-/media/AQR/Documents/Insights/Perspectives/Factor-Timing-is-Hard.pdf
- Argues factor timing is harder than market timing due to higher turnover in long-short factor strategies.
- Warns that selecting factors based on 3-5 year performance creates "poor results in a world where data mining is a problem."
- Criticizes Research Affiliates (Arnott et al.) for "poorly designed tests" including long-horizon regressions on high-turnover factors.
- Warns about crowding risks from growing popularity of factor investing.

---

### 2. CORE AQR RESEARCH PAPERS

**A. "Value and Momentum Everywhere"**
- Authors: Cliff Asness, Tobias J. Moskowitz, Lasse H. Pedersen
- Published: The Journal of Finance, June 2013
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Value-and-Momentum-Everywhere
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2174501
- NYU Stern PDF: https://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf
- Datasets: https://www.aqr.com/Insights/Datasets/Value-and-Momentum-Everywhere-Factors-Monthly
- Key findings: Consistent value and momentum return premia across 8 diverse markets and asset classes. Value and momentum are negatively correlated with each other but correlate more strongly across asset classes than passive exposures. A three-factor model describes 48 global test assets. Global funding liquidity risk is a partial source of these patterns.

**B. "Fact, Fiction and Momentum Investing"**
- Authors: Cliff Asness, Andrea Frazzini, Ronen Israel, Tobias J. Moskowitz
- Published: The Journal of Portfolio Management, 40th Anniversary Issue, September 30, 2014
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Fact-Fiction-and-Momentum-Investing
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2435323
- PDF: https://images.aqr.com/-/media/AQR/Documents/Insights/Interviews/PA--Fact-Fiction-and-Momentum-Investing-FINAL.pdf
- Supplement: https://www.aqr.com/Insights/Research/Interviews/Fact-Fiction-and-Momentum-Investing-Supplement
- Documents momentum across 212 years of U.S. data (1801-2012), 40+ countries, and 12+ asset classes. Debunks 10 common myths about momentum investing (too small, only short-side, only small caps, can't survive trading costs, etc.).

**C. "Fact, Fiction and Value Investing"**
- Authors: Cliff Asness, Andrea Frazzini, Ronen Israel, Tobias J. Moskowitz
- Published: The Journal of Portfolio Management, Fall 2015
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Fact-Fiction-and-Value-Investing
- PDF: https://images.aqr.com/-/media/AQR/Documents/Journal-Articles/JPM-Fact-Fiction-and-Value-Investing.pdf
- SSRN: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2998011_code77768.pdf?abstractid=2595747
- Supplement: https://www.aqr.com/Insights/Research/Journal-Article/Fact-Fiction-and-Value-Investing-Supplement
- Won Outstanding Article in the 17th Annual Bernstein Fabozzi/Jacobs Levy Awards. Challenges misconceptions about value investing (only for concentrated portfolios, passive strategy, buying inferior companies, redundant factor, etc.).

**D. "Fact, Fiction, and Factor Investing"**
- Authors: Michele L. Aghassi, Cliff Asness, Charles Fattouche, Tobias J. Moskowitz
- Published: The Journal of Portfolio Management, December 31, 2022
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Fact-Fiction-and-Factor-Investing
- Won 25th Annual Bernstein Fabozzi/Jacobs Levy Award for Best Article (2023).
- Examines factor investing myths including performance challenges during 2018-2020 and subsequent recovery.
- Practical applications: https://www.aqr.com/Insights/Research/Journal-Article/Fact-Fiction-and-Factor-Investing-Practical-Application

---

### 3. REPLICATION CRISIS AND P-HACKING PAPERS

**A. "Is There a Replication Crisis in Finance?"**
- Authors: Theis Ingerslev Jensen, Bryan T. Kelly, Lasse H. Pedersen
- Published: The Journal of Finance, May 26, 2023
- AQR page: https://www.aqr.com/Insights/Research/Working-Paper/Is-There-a-Replication-Crisis-in-Finance
- Won a 2023 Distinguished Paper Award in the Dimensional Fund Advisors Prizes from The Journal of Finance.
- Key findings: The majority of asset pricing factors CAN be replicated. They cluster into 13 themes. They work out-of-sample across 93 countries. The large number of observed factors actually **strengthens** evidence rather than weakening it (a "multiple testing paradox"). Concludes the replication crisis is overstated.

**B. "A Data Science Solution to the Multiple-Testing Crisis in Financial Research"**
- Author: Marcos Lopez de Prado
- Published: The Journal of Financial Data Science, January 31, 2019
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/A-Data-Science-Solution-to-the-Multiple-Testing-Crisis-in-Financial-Research
- Addresses "selection bias under multiple testing" (SBuMT) -- the problem of reporting only the most favorable outcome from many analyses. Proposes the **Deflated Sharpe Ratio** as a corrective framework.

**C. "Corporate Bond Factors: Replication Failures and a New Framework"**
- Authors: Jens Dick-Nielsen, Peter Feldhutter, Lasse H. Pedersen, Christian Stolborg
- Published: October 5, 2023
- AQR page: https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework
- Documents that corporate bond factor literature suffers from "replication failures, inconsistent methodological choices, and the lack of a common error-free dataset." Most tested factors failed to replicate, though equity signals showed cross-asset predictive power.

---

### 4. AQR INSIGHT AWARD WINNERS (Relevant to Methodology)

**"Taming the Factor Zoo: A Test of New Factors"** (2018 AQR Insight Award winner)
- Authors: Guanhao Feng, Stefano Giglio, Dacheng Xiu
- Published: The Journal of Finance, 2020
- AQR-hosted PDF: https://www.aqr.com/-/media/AQR/Documents/AQR-Insight-Award/2018/Taming-the-Factor-Zoo.pdf
- Award page: https://www.aqr.com/Insights/Perspectives/AQR-Insight-Award-2018
- Used a factor library of 150 risk factors (1976-2017) including AQR factors. Key finding: with few exceptions (profitability, investment), new factors beyond the established set are redundant. Proposes a machine-learning-based model selection method.

---

### 5. ADDITIONAL RELEVANT AQR PAPERS AND WHITE PAPERS

**A. "Measuring Factor Exposures: Uses and Abuses"**
- Authors: Ronen Israel, Adrienne Ross
- Published: The Journal of Alternative Investments, Summer 2017
- AQR page: https://www.aqr.com/Insights/Research/White-Papers/Measuring-Factor-Exposures
- PDF: https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/JAI_Summer_2017_AQR.PDF
- Practical guide on measuring factor exposures. Discusses pitfalls in regression analysis and how factor construction design matters more than expected. Warns that without proper modeling, factor exposures may be misconstrued as alpha.

**B. "Craftsmanship Alpha: An Application to Style Investing"**
- Authors: Ronen Israel, Sarah Jiang, Adrienne Ross
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Craftsmanship-Alpha-An-Application-to-Style-Investing
- PDF: https://images.aqr.com/-/media/AQR/Documents/Insights/Working-Papers/AQR--Craftsmanship-Alpha.pdf
- Discusses how implementation details ("craftsmanship") in factor strategies generate additional alpha beyond raw factor exposures.

**C. "Understanding Style Premia"**
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Understanding-Style-Premia
- PDF: https://images.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/Understanding-Style-Premia.pdf
- Describes the intuition and evidence underlying investing styles and a strategy to access these returns in a liquid, market-neutral framework.

**D. "Investing with Style"**
- Authors: A. Ilmanen, R. Israel, T. Moskowitz (2012 AQR white paper)
- PDF: https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/JOIM-Investing-With-Style.pdf
- Published in Journal of Investment Management, 2015.

**E. "Betting Against Beta"**
- Authors: Andrea Frazzini, Lasse H. Pedersen
- Published: Journal of Financial Economics, 111: 1-25, 2013
- AQR page: https://www.aqr.com/Insights/Research/Journal-Article/Betting-Against-Beta
- Dataset: https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Equity-Factors-Monthly

**F. "The Less-Efficient Market Hypothesis"**
- Author: Cliff Asness
- Published: The Journal of Portfolio Management
- Won Outstanding Article recognition in the 26th Annual Bernstein Fabozzi/Jacobs Levy Awards (2025)
- Award page: https://www.aqr.com/About-Us/News/2025/AQRs-The-Less-Efficient-Market-Hypothesis-Wins-Outstanding-Article-Recognition-in-26th-Annual-Bernstein-Fabozzi-Jacobs-Levy-Awards
- Argues markets have become **less** informationally efficient over the past 30+ years in relative pricing of common stocks, particularly over medium horizons.

**G. "Academic Alpha"** (August 2026, most recent)
- Authors: Thomas Maloney, Tobias J. Moskowitz
- AQR page: https://www.aqr.com/Insights/Research/White-Papers/Academic-Alpha
- Introduces style premia investing and how well-researched, skillfully implemented strategies can provide liquid, transparent, cost-effective uncorrelated returns.

---

### 6. CLIFF ASNESS'S PUBLIC STATEMENTS (INTERVIEWS / EXTERNAL)

**Hoover Institution Interview: "Cliff Asness on Factor Investing and the History of Financial Economics"**
- URL: https://www.hoover.org/research/cliff-asness-factor-investing-and-history-financial-economics
- Key quotes and positions:
  - "If we get half a backtest going forward, we'll be thrilled" -- acknowledging data mining effects.
  - Factors most susceptible to disappearing are those based on legal information advantages (temporary edges from better data/faster execution), not persistent market inefficiencies.
  - AQR's approach: trade strategies for extended periods BEFORE publishing research. "Trading first, publishing later" validates against live markets.
  - Value and momentum are more durable because they reflect fundamental risk premiums or deep behavioral patterns.
  - Combines empirical strength AND theoretical coherence when evaluating factors, though strong empirical results sometimes precede satisfactory explanations.

**Chicago Booth Review: "Why Cliff Asness Believes Markets Are Getting Dumber"**
- URL: https://www.chicagobooth.edu/review/capitalisnt-why-cliff-asness-believes-markets-are-getting-dumber
- Podcast/interview on the "Less Efficient Market Hypothesis."

---

### 7. KEY RESOURCE PAGES

- **AQR Research Library (main page):** https://www.aqr.com/Insights/Research
- **AQR White Papers index:** https://www.aqr.com/Insights/Research/White-Papers
- **AQR Datasets (factor data for download):** https://www.aqr.com/Insights/Datasets
- **AQR Insight Award page:** https://www.aqr.com/About-Us/AQR-Insight-Award
- **AQR Further Reading (systematic equities):** https://www.aqr.com/Learning-Center/Systematic-Equities/Further-Reading

---

### SUMMARY OF ASNESS/AQR POSITION ON DATA MINING

Asness's consistent position across all these writings:

1. **Data mining is real and dangerous** -- he does not dismiss the concern. "I'm always in a panic that [our strategies are] the result of data mining or survivorship bias."

2. **But the core factors survive the test** -- value, momentum, and quality have passed out-of-sample validation across time periods (212 years for U.S. momentum), geographies (93 countries per the Jensen/Kelly/Pedersen paper), and asset classes (8 asset classes per "Value and Momentum Everywhere").

3. **Three defenses against data mining**: (a) out-of-sample replication, (b) economic rationale/theory for why the factor exists, (c) trading the strategy live before publishing.

4. **The factor zoo is mostly redundant** -- most of the 400+ published factors collapse into roughly 13 themes, and few new factors add pricing information beyond the established ones.

5. **AQR sticks to few factors** -- value, momentum, quality (and sometimes carry/defensive). They explicitly reject the proliferation approach.

6. **Expect decay but not death** -- "if we get half a backtest going forward, we'll be thrilled" -- honest acknowledgment that live performance will trail backtests, but the premium should survive.