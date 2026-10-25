# Note · ICE fixed-income data — an evaluated-pricing incumbency that grades the market, then sells the grade as execution, index plumbing and AI feeds

> Company-study / market-structure note · Maps to **Course 04** (Competitive Strategy — incumbency, bundling, vertical stacks), **Course 07** (Data, Analytics & Decision-Making — self-measured accuracy, baselines, TCA), **Course 03** (Microeconomics & Strategy Foundations — information asymmetry, who sees the trades), **Course 05** (Marketing & Brand — implicit competitor positioning), **E10** (Digital & AI — MCP distribution, AI pre-trade), **E3** (M&A — the 2015–18 data roll-up) · Written 2026-10-25 · Part of [[ice-hub]]; companions [[ice-marketaxess-deal]], [[ice-benchmarks-iba]], [[tradeweb-ai-price]]

- **Source:** ICE corpus at `_ingest/raw/ice/articles.jsonl`. **41 items** read in full: 22 IR press releases (Feb 2020 – Sep 2026, plus two earnings releases for segment revenue), 17 ice.com Insights pieces (most undated in the scrape; in-text dates given where printed, Aug 2022 – Jul 2025), and two "Inside the ICE House" transcripts (Jackson 2018-10-25, Edmonds 2026-01-14), plus Lynn Martin's 2022-03-08 episode for one line. Insights dates in the file are unreliable; "(in-text)" means the date printed in the article, "undated" means none. Linked PDFs and whitepaper charts were not available, so no TCA figure that lives only in a chart is used.
- **Core claim:** ICE's fixed-income franchise is not a trading venue. It is an **evaluated-pricing incumbency** assembled by purchase: Interactive Data (2015), S&P's securities evaluations business (2016) and the BofA Merrill Lynch indices (2017), which ICE says now price **~3 million instruments**. Everything else is that price reused. Best Execution, Size-Adjusted Pricing, Liquidity Indicators and TCA all measure trades *against CEP*. ICE Bonds' RMA, portfolio auctions and ICE Select price off CEP. ICE indices use ICE evaluations, so the $794B of passive AUM tracking them is graded by the same ruler. Compass and the MCP feed sell the same ruler to the buy side's AI. FY25 makes the shape plain: **Fixed Income Data & Analytics $1,234M vs Fixed Income Execution $125M**, about 10 to 1. ICE also argues both sides of the key question. One Insights piece says “data and technology do not create liquidity”; others sell data as the thing that makes markets. The accuracy claim (evaluations **38% IG / 79% HY** "closer to the next trade" since 2018) is real, but it is relative to ICE's own 2018 model. The boilerplate under the same pieces says ICE “does not have access to all relevant trade-related data or dealer quotes”. Buying MarketAxess (see [[ice-marketaxess-deal]]) is the logical end: the grader buys the flow it was grading from outside.

---

## 1. Chronology — the data spine

All figures as ICE states them ("ICE says") unless another source is named.

| Date | Event | Numbers stated |
|---|---|---|
| 2015–2018 | Roll-up, as retold in the Apr 2024 Edmonds profile: Interactive Data (2015), S&P securities evaluations + Credit Market Analysis (2016), BofA fixed-income index platform (2017), BondPoint (from Virtu), TMC Bonds (closed summer 2018). | — |
| 2018-10-25 | Ben Jackson (podcast): ICE went after IDC as “the golden record for reference data”, and pricing, *before* execution, because rivals that started with execution “have failed”. | — |
| 2019-08-05 | MOVE index family bought from BofA (see [[ice-benchmarks-iba]]). | ICE Data Indices "second largest fixed income index provider", >$1T benchmarked |
| 2020-02-13 | ICE Bonds Portfolio Auction inside BlackRock **Aladdin**, priced at-the-market off **CEP** or at-the-close off end-of-day evaluations. | — |
| 2020-04-29 | **ICE Select**: one screen over BondPoint, TMC and Credit Trade, bundled with CEP, Liquidity Indicators and Best Execution. | — |
| 2021-01-05 | ICE Bonds record PT quarter. | $1.9B notional (Q4 2020) |
| 2021-07-21 | Index business disclosure. | ETF AUM on ICE indices **<$100B (end-2017) → >$300B**; ~$60B switching in 2021 ($24B done in H1, $36B announced) |
| 2022-06-13 | **Best Execution** platform more than doubles coverage. | **>2 million** securities, many outside TRACE and MSRB |
| Aug 2022 (in-text) | Borstelmann: muni e-trading "at a tipping point"; venue sold with CEP, AAA curve, Liquidity Indicators, Best Ex. | 450+ LPs, 367,000+ CUSIPs, fill rates >99%, institutional adoption +250% YoY; Greenwich: 11% of muni volume electronic (May 2022) |
| ~2022 (undated) | Nicoletta, "trading-centric to data-centric". | — |
| 2023-07-31 | RMA dealer sweeps relaunched; CEP proposes the price level. | 50 firms, 400+ users |
| Aug 2023 (in-text) | Trading Analytics papers: TCA = trades vs CEP, five-day 15-minute lookback, regressed on Liquidity Indicators. | ~3 million instruments covered |
| Dec 22 2023 | ICE indices switch early-close days to a **4pm Fair Value** price. | Tracking error −~5bp average; −13bp USIG, −~40bp TLT on Dec 29 2023 |
| Feb/May 2024 (in-text) | **Size-Adjusted Pricing** whitepaper (SAP offered since 2018 inside Best Ex). | Muni micro-lot cost "virtually cut in half" in seven years |
| Apr 2024 (in-text) | Edmonds takes over FIDS (≈2,300 staff, moves to Atlanta). | — |
| ~2024 (undated) | Monahan: "A leap forward for ICE's Evaluations". | **38% IG / 79% HY** closer to next trade since 2018 |
| Sep 2024 (in-text) | "Supporting better outcomes for small bond trades" (ICE TMC). | 500+ LPs, >125,000 average daily CUSIPs offered |
| 2025-05-06 | PIVC follow-on auction added to RMA. | 66+ firms, 700+ users; Q1 2025 corporates $62B (+27%), munis $48B (+26%) |
| 2025-06-24 | Spread-based click-to-trade for corporates on ICE TMC. | TRACE trades 22.7M (2022) → 32.3M (2024); <$100k = 68.5% |
| 2026-01-06 | 2025 milestones. | ICE Bonds corporates $232.5B (+10%), munis $225.5B (+27%); passive AUM on ICE indices **$794B** (vs $647B); >$2T total benchmarked; ETF Hub 76,908 orders (+42%), $4.77T cumulative |
| 2026-01-28 / 02-11 | Reddit, then Polymarket "Signals and Sentiment" (ICE exclusive institutional distributor of Polymarket data). | — |
| 2026-03-17 / 07-27 | ICE Private Credit Intelligence (Apollo anchor), then ICE IDs for private credit. | "$40 trillion private credit market"; reference data on 35M+ instruments |
| **2026-06-09** | **ICE Compass**: AI dealer rankings and price-commitment estimates; T. Rowe Price anchor. | evaluations on ~3M instruments |
| **2026-07-29** | ICE fixed-income data over **MCP**, “currently available in Claude”; priced on value of data, not compute. | EOD evaluations on >3M instruments, ~160 data points per ID |
| 2026-07-30 | ICE agrees to buy MarketAxess (deal analysis in [[ice-marketaxess-deal]]). | — |

**Segment economics (earnings releases):** FY25 FIDS revenue $2,419M (+5%): Fixed Income Data & Analytics **$1,234M** (+5%), Data & Network Technology $722M, CDS Clearing $338M, Fixed Income Execution **$125M** (+8%). In 2Q26, execution was $31M (−4%) and FI data & analytics $333M (+9%).

## 2. One ruler, many products

| Product | What it measures or does | What it is benchmarked against |
|---|---|---|
| **CEP** (Continuous Evaluated Pricing, since 2015) | Streaming intraday evaluations for the round-lot institutional size (typically $1mm+) | Next trade, versus ICE's own 2018 baseline (§3) |
| **Best Execution** | Trade-by-trade execution score, >2M securities | Distributions of trades **around CEP** at trade time |
| **Size-Adjusted Pricing** | Bid/ask by side and size for odd and micro lots | The Best Ex distribution around CEP, extrapolated by size |
| **Liquidity Indicators** (and 2025 index Liquidity Metrics) | Projected trade capacity, time-weighted ADV, turnover | Modelled; ICE admits ADV-style history misleads |
| **Trading Analytics / TCA** | Expected cost in dollars for a list of trades | CEP, regressed on Liquidity Indicators |
| **ICE Bonds** protocols (RMA, PIVC, Portfolio Auction) | Venue | Proposed prices come **from CEP** |
| **ICE indices** + 4pm Fair Value | ETF benchmarks | ICE evaluations; Fair Value is calculated by ICE Data Pricing & Reference Data |
| **Compass**, **MCP feed** | AI dealer ranking; AI-delivered evaluations | Built "on" CEP, liquidity metrics and indices |

The design choice is explicit. ICE calls benchmarking against CEP a differentiator, saying that “a common alternative is to use a price differential analysis from a previous trade or end of day price” (Aug 2023, in-text). Trading Analytics is pitched as a substitute for the missing bond consolidated tape: “This is the void that ICE Trading Analytics can help to fill.” (Aug 2023, in-text). The bundle was sold as a bundle from the start. Marshall Nicholson's 2020 pitch was that portfolio auctions off CEP let managers “execute as close as possible to NAV prices, significantly reducing tracking errors against benchmarks” (2020-02-13). Edmonds called PIVC “a powerful example of how execution and data can come together to create measurable benefits for our clients” (2025-05-06).

## 3. The accuracy claim, read carefully — and a correction to [[tradeweb-ai-price]]

- **What ICE says (Monahan, undated, ~2024 by inference from "past six years"):** “since 2018, for US Investment Grade bonds, our evaluations are on average 38% closer to the next trade price” and “For US high yield bonds, that figure is 79%.” Monahan calls the CEP upgrade “by far the biggest leap in product enhancement ICE has implemented since launching the service in 2015”.
- **What it is:** a *relative* improvement of ICE's model against **its own 2018 version**. No absolute error (bp or points), no median vs mean, no liquidity buckets, no side adjustment and no competitor appear.
- **What ICE admits in the same piece:** before the upgrade, “we did not have a systematic way to change our bid/ask spread - it required a manual action”. For comparable-bond updates on illiquid names: “We currently use a manual approach for this.” The 79% HY gain is therefore partly the removal of a manual lag, which says the 2018 baseline was weak, not that today's level is strong (inference).
- **What the legal text says:** almost every Insights piece carries ICE's RIA disclaimer. ICE Data Pricing & Reference Data is an SEC-registered investment adviser. It says it “does not have access to all relevant trade-related data or dealer quotes” and its analytics “may not generate results that correlate to actual outcomes”. That is boilerplate, but it is also the structural truth of evaluated pricing. Edmonds says ICE is “pricing 3.2 million bonds every day around the globe” while only “25 to 40,000” trade on a given day (2026-01-14). So about **1%** of the evaluated universe prints on any day.
- **Correction (do not edit the other note):** [[tradeweb-ai-price]] §3 says ICE back-tests CEP against the next round-lot trade but *publishes no figure*. ICE does publish a figure: a relative improvement of 38% (IG) and 79% (HY) versus 2018. It publishes **no absolute error and no head-to-head**, so that note's broader point (no vendor publishes a side-matched, competitor-inclusive test) still holds. The wording should change to "publishes only a self-relative improvement".
- **Not comparable to Ai-Price's ~30%.** Tradeweb's ~30% is *model vs the naive last-print predictor*. ICE's 38%/79% is *model today vs ICE's model in 2018*. Different baselines, different questions: "is the model better than doing nothing?" against "is the model better than it used to be?" Neither answers "is it better than BVAL, CP+ or Ai-Price?"

## 4. "Data does not create liquidity" — and the pieces that say it does

- **Nicoletta (undated, ~2022 by inference: "volatile markets like we've seen this year"):** “While data and technology do not create liquidity, it can be used to more efficiently source liquidity and power trading workflows to improve execution quality”. The problem, in this telling, is that “Data fragmentation is the key problem that the market is trying to solve for.” The sequence is aggregation, then pre-trade contextualization, then "no touch" trades.
- **The counter-texts, also ICE's:**
  - Undated odd-lot piece: “new data - and the technology to distill it - can boost asset class liquidity”.
  - Sep 2024 (in-text) TMC paper: the data “underscore the ability of alternative liquidity providers to create higher quality markets across a range of instruments by employing a more data-driven approach”.
  - Edmonds, 2025 outlook: index management, e-trading, ETFs and small trades together are “boosting liquidity, transparency and trading speed”.
- **Why both stories are needed (inference).** To sell to dealers and to regulators, ICE's data is neutral plumbing that only *finds* liquidity. To sell to venues, LPs and the buy side, the same data *makes* markets possible. The MarketAxess deal settles the tension in practice. If data alone made liquidity, ICE Bonds (about $31M of revenue a quarter) would not have needed to buy an institutional network.
- **Lynn Martin's version (2022-03-08):** “data is the most important output of fully-transparent liquid markets, but then it's a really important input to finding fair value.” The circularity is the business model: thin markets need fair-value inputs, and ICE sells them; deeper markets produce more output data, and ICE sells that too.

## 5. Indices and the ETF stack

- **Growth:** ETF AUM on ICE indices went from **<$100B (end-2017) to >$300B (mid-2021)**. Passive AUM was about **$670B (Sep 2024)**, **$647B (end-2024)** and **$794B (end-2025)**; total active-plus-passive is over **$2T**. Lynn Martin: “The accelerating adoption and growth of passive investing has been an important driver of organic growth for our index business” (2021-07-21).
- **Switches:** about $60B of ETFs announced moves to ICE benchmarks in 2021 (release); the 2021 shareholder letter says five managers moved "over $66 billion". Index switches are won one fund at a time and are lumpy.
- **The 4pm Fair Value move, an implicit jab at rival index vendors.** On SIFMA early-close days bonds stop at 1pm while ETFs trade to 4pm. Since Dec 22 2023 ICE prices its indices at 4pm with a factor model. ICE says this “reduces tracking error by ~5 bps on average across all early close days”. On Dec 29 2023, TLT (ICE index) stayed in line while SPTL and VGLT, which are, in ICE's words, “benchmarked other index providers”, lagged by about 40bp. ICE does not name those providers (context, not from ICE corpus: the SPDR and Vanguard long-Treasury funds track Bloomberg indices).
- **Stack:** index (ICE Data Indices) → evaluation (ICE PRD) → listing (NYSE: “Because ICE has two-thirds of the U.S. listed ETF market via NYSE, we can maintain strong liquidity by directing listing fees into liquidity programs.”, Jul 2023, in-text) → iNAV/IOPV (3,000+ calculations, >$4T AUM) → primary market (ETF Hub, $4.77T cumulative). Varun Pawar: “Connectivity to this wider ecosystem to support ETF issuers means ICE Indices is in a unique position versus any other competitor.” (undated).
- **Headroom, by Edmonds' own number:** in equities 31% of trading follows passive; “In the bond market, it's single digits.”, “Less than three.” (2026-01-14).

## 6. ICE Bonds as the data-plus-venue bundle (deal analysis stays in [[ice-marketaxess-deal]])

- **Munis:** ICE TMC is the core. Munis rose to $225.5B in 2025 (+27%) with >4M trades. The ICE AAA muni curve updates every 5–10 minutes “based on actual trades rather than indications from dealers” (Aug 2022, in-text).
- **Corporates:** spread-based click-to-trade (Jun 2025) is pitched as “preventing RFQ-associated information leakage”, the same leakage argument Jackson made in 2018 and Tradeweb now makes against A2A ([[tradeweb-a2a-information-leakage]]).
- **Dealer-to-dealer:** RMA sweeps and PIVC, priced from CEP. Registered firms rose from 50 (Jul 2023) to 66+ (May 2025).
- **MBS:** click-to-trade, then an anonymous RFQ on TMC (Apr 2025). ICE plans to integrate ICE Mortgage Technology pricing. ICE says MBS volume doubled in 2025 but gives no base.
- **The 2024 MarketAxess link** (TMC ↔ Open Trading) paired ICE's “retail brokerage and wealth management presence” with MarketAxess's institutional base. That is ICE's own admission of where each side was strong.

## 7. AI: selling the ruler to the models

- **Edmonds (Apr 2024, in-text):** “They’re going to need our data at the end of the day in order to drive those models”. In the 2026 outlook: “the rise of AI has elevated the value of proprietary data, whether it be sentiment data or the pricing of illiquid fixed income securities.” A year earlier, the 2025 outlook said AI and machine learning “is still nascent in bond markets”.
- **Compass (2026-06-09)** pools the client's own RFQ data, counterparties' bids/offers/IOIs and ICE's streams to “estimate trading counterparty price commitment prior to indicating trading intent”. Pawar: “By pooling together data from across firms, trading counterparties and ICE’s vast data warehouse”. The pitch puts ICE inside **dealer selection**, the layer Tradeweb's SNAP+ also targets ([[tradeweb-credit]]).
- **MCP (2026-07-29)** delivers EOD evaluations, the Enhanced Evaluation Transparency fields, the AAA muni curve, UST benchmark data and TRACE/RTRS. Edmonds frames it as “built on the principle that users should pay for the value of the data delivered, rather than the volume of compute consumed”. Unlike Tradeweb's Ai-Price, which [[tradeweb-ai-price]] found had no MCP or agent distribution, ICE is already live in Claude.
- **New inputs:** Reddit and Polymarket sentiment are mapped through ICE's entity database. Edmonds: “It’s so rare for new datasets like this to become available at such a quick pace” (2026-02-11). Private credit is the next "illiquid security" to grade: Private Credit Intelligence with Apollo, then ICE IDs, which Edmonds calls “the cornerstone that we build everything else off of” (2026-07-27). The playbook is the same as IDC's: identifiers and reference data first, pricing second, execution later. Edmonds's 2026 outlook forecasts that “efforts to create a syndicated loan market” will be a defining trend.
- **Implicit Bloomberg jabs:** ICE Connect is sold as a scalpel against a “Swiss army knife”, “at a cost significantly below other premium data services” (Oct 2024, in-text). Terminal subscriptions run to “often equivalent of many thousands of U.S. dollars a month”, and “some terminals currently only facilitate the input of one CUSIP at a time” (2025-06-09). Bloomberg is never named ([[bloomberg-terminal-instrumentation]], [[bloomberg-hub]]).

## 8. What the claims don't prove

1. **ICE is the referee of its own game.** Best Ex scores, SAP, TCA compression, RMA prices and the FINRA PT-flag study (2023-05-15), where ICE reads HY portfolio-trade prices landing at zero difference to CEP as proof that “our published CEP prices are reflective of the reported price” all measure markets against CEP. If CEP is biased, everything downstream inherits the bias, and the 4pm Fair Value model is a CEP-style model too.
2. **Relative accuracy with no level.** 38%/79% "closer" with no 2018 level cannot be turned into bp. An HY error that was large and manual in 2018 can fall 79% and still be wide.
3. **The compression story needs residual inefficiency.** SAP celebrates micro-lot costs halving, then says “white space” gaps remain between large- and small-trade inside markets. That gap is what keeps SAP worth buying (inference).
4. **Metrics drift.** Index AUM is quoted as "ETF AUM" (2021, 2025 letter), "passive funds" (2026-01-06) and "passively managed products" (Sep 2024, $670B, *above* the end-2024 $647B). Index counts go "over 5,000" → "over 7,000" → "over 8,000" across releases. 2021 switches are $60B in one release and $66B in the letter.
5. **No denominators for ICE Bonds.** Records in notional, never market share. The MBS doubling has no base. The two venue papers give LP and CUSIP counts, not ICE's share of TRACE or MSRB.
6. **Private-credit sizing doesn't reconcile.** "The $40 trillion private credit market" (Mar 2026 release) against Edmonds' private credit that crossed “the $3 trillion AUM threshold” (2026 outlook). One is probably a market-wide claim, the other fund AUM; the releases don't say which.
7. **Survivorship.** No piece covers March 2020 evaluation quality, a CEP outage or a mispricing episode. The undated Nicoletta and Monahan pieces carry no date, so they cannot be checked against market events.

## 9. Strategic read (inference — not stated by ICE)

- **Power is cornered resource plus switching costs, not network effects.** IDC's 40-year evaluation history, the RIA regulatory wrapper, and the fact that fund boards and auditors already sign off on ICE's EOD marks make the evaluation hard to dislodge. Every downstream tool (TCA history, index rules, auto-ex tolerances) re-baselines if a client switches.
- **The flow problem is the weak point.** An evaluator that sees ~1% of its universe trade each day is an inference engine built on other people's prints. Tradeweb (Ai-Price on its own flow) and MarketAxess (CP+ on Open Trading flow) built evaluators from venues. ICE built venues from an evaluator and never got the institutional flow. Buying MarketAxess fixes that input problem ([[ice-marketaxess-deal]]), and the same logic drives [[ice-benchmarks-iba]], where IBA's rates depend on Tradeweb's data.
- **AI distribution flips the cost curve.** If an LLM agent is the new terminal, "pay for value, not compute" lets ICE price per evaluation rather than per seat. That bypasses the terminal bundle ICE has been attacking.
- **Index royalties are the cleaner moat.** The ETF stack (index → NYSE listing with fee-funded LP programs → ETF Hub → iNAV) compounds with passive growth and is less exposed to an AI-native pricing entrant than evaluations are.

## 10. Canon lenses

- **Helmer** ([[canon-helmer-7-powers]]): cornered resource (history, coverage, regulatory standing) and switching costs. The question is whether venue-born evaluators turn "process power" into a cheaper, flow-native substitute.
- **Shapiro–Varian** ([[canon-shapiro-varian-information-rules]]): versioning the same information good. EOD, CEP, SAP, Best Ex, Liquidity Indicators, Compass and MCP are one dataset sold at different resolutions and prices.
- **Akerlof** ([[canon-akerlof-market-for-lemons]]): in thin markets the party with the better price estimate extracts rent. SAP and Best Ex sell the small investor a defence against the dealer's information edge.
- **Christensen** ([[canon-christensen-innovators-dilemma]]): an LLM querying TRACE plus a cheap model is a low-end substitute for an evaluation. ICE's answer is to become the data inside the LLM.
- **Kahneman–Sibony–Sunstein** ([[canon-kahneman-sibony-sunstein-noise]]): human evaluators plus manual bid/ask changes are a noise source. The 79% HY gain is mostly noise reduction.
- **Brandenburger–Nalebuff** ([[canon-brandenburger-nalebuff-coopetition]]): ICE sells evaluations to MSCI and indexes for issuers whose ETFs compete with funds on rival indices. In 2024 it linked ICE Bonds to the MarketAxess network it then agreed to buy.

## 11. Practitioner counterpoint

- **For ICE:** evaluated pricing is a regulated, audited, boring utility, and boring is the point. Coverage of ~3M instruments, munis and securitized products that trade-driven models can't touch, and decades of fund-accounting acceptance are hard to replicate. The SS&C 2025 vendor study cited in [[tradeweb-ai-price]] includes ICE, so outside benchmarking exists, even if ICE doesn't quote it.
- **Against:** a buy-side desk should never score its dealers with the same vendor's price that its dealers' venue uses to propose trades. Use at least one independent mid (next TRACE print, CBBT, CP+ or Ai-Price) and compare by side and size.
- **Both:** the accuracy claim is honest about what it is (self-relative), and the manual-step admission is unusually candid. The fair ask is a published absolute error by liquidity bucket, next to the 2018 baseline.

## 12. Open questions to track

1. Will ICE publish absolute CEP error (bp/points, by bucket), or enter a public head-to-head?
2. After MarketAxess closes, does CP+ get folded into CEP or kept separate? Does S&P's CP+ licence survive ([[tradeweb-ai-price]] §5)?
3. MCP: which AI platforms beyond Claude, and does value-based pricing raise or cut revenue per user?
4. Compass adoption beyond T. Rowe Price, and any evidence it changes dealer hit rates.
5. Do index switches continue (passive AUM above $1T)? Does the 4pm Fair Value approach become an industry standard or a differentiator?
6. Private credit: does ICE get a pricing role, not only identifiers, and with which originators beyond Apollo?
7. Does the "data does not create liquidity" line survive once ICE owns a big institutional venue?

**Links:** [[ice-hub]] · [[ice-marketaxess-deal]] (the flow purchase) · [[ice-benchmarks-iba]] (input dependence in rates) · [[ice-strategy-financials]] (segment economics) · [[ice-mortgage-technology]] (MBS data flywheel) · [[ice-people]] (Edmonds, Martin, Pawar) · [[tradeweb-ai-price]] (corrected in §3) · [[tradeweb-credit]] · [[tradeweb-a2a-information-leakage]] · [[tradeweb-tech-ai-data]] · [[spglobal-indices-benchmarks]] · [[bloomberg-terminal-instrumentation]] · [[market-structure-24-5-trading]] · [[wss-credit-distressed]] · [[wss-private-markets-wealth]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-akerlof-market-for-lemons]] · [[canon-christensen-innovators-dilemma]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-brandenburger-nalebuff-coopetition]]

---
### Rep
Three computations with numbers from this note.

**(a) What "38% / 79% closer" can and can't mean.** Suppose ICE's 2018 mean absolute error to the next trade was 40c (IG) and $1.20 (HY). Compute today's implied errors, then compute the error Tradeweb's ~30%-better-than-last-print claim would imply if last-print error were 50c (IG). *(Answer: IG 0.62 × 40c = **24.8c**; HY 0.21 × $1.20 = **25.2c**; Ai-Price 0.70 × 50c = **35c**. The comparison is meaningless, because the baselines differ: ICE-2018 vs naive last print, and you invented both levels. State in one sentence what single published number would make the two claims comparable: the same next-trade error, on the same trades, same side.)*

**(b) TCA in dollars and bp.** ICE's Aug 2023 example: a trade with expected cost **$2,000** executed at a Best Ex score of 60 realizes a **+$1,200** impact, net **$800**. Assume it was a $1mm 10-year IG bond with spread duration 8. Express both costs in price points and in spread bp, and the saving as a percentage. *(Answer: $2,000 / $1mm = **0.20 pts** ≈ 0.20/8 × 100 = **2.5bp**; $800 = **0.08 pts** ≈ **1.0bp**; saving **60%**. Then: which price defined "expected"? CEP. Rerun the logic if CEP was 0.05 pts rich at trade time.)*

**(c) Index AUM growth, bounded.** ETF AUM on ICE indices was **<$100B** at end-2017, **>$300B** by mid-2021 and **$794B** at end-2025. Compute the minimum CAGR 2017–25 and the maximum CAGR mid-2021–25. Then the 2024→25 growth. *(Answer: (7.94)^(1/8) − 1 ≥ **29.6%** a year; (794/300)^(1/4.5) − 1 ≤ **24.1%**; 794/647 − 1 = **22.7%**. Growth is slowing in rate but not in dollars (+$147B in 2025). Then ask how much of 2025 was market moves versus flows and switches. ICE doesn't split it.)*

---
**Sources (ICE corpus, `_ingest/raw/ice/articles.jsonl`):**
- [Jackson, Revolutionizing Fixed Income (podcast), 2018-10-25](https://www.ice.com/insights/conversations/inside-the-ice-house/revolutionizing-fixed-income-with-ben-jackson-president-of-ice)
- [MOVE acquisition, 2019-08-05](https://ir.theice.com/press/news-details/2019/Intercontinental-Exchange-Announces-Agreement-to-Acquire-the-Merrill-Lynch-Option-Volatility-Estimate-MOVE-Index-from-Bank-of-America-Merrill-Lynch/default.aspx)
- [ICE Bonds × Aladdin portfolio auction, 2020-02-13](https://ir.theice.com/press/news-details/2020/ICE-Bonds-Completes-Integration-with-BlackRocks-Aladdin-to-Offer-Fixed-Income-Portfolio-Auction-Functionality-to-Investment-Managers-/default.aspx)
- [ICE Select, 2020-04-29](https://ir.theice.com/press/news-details/2020/Intercontinental-Exchange-Launches-ICE-Select-for-Consolidated-Access-to-ICE-Bonds-Liquidity-and-Protocols/default.aspx)
- [ICE Bonds record PT, 2021-01-05](https://ir.theice.com/press/news-details/2021/ICE-Bonds-Announces-Record-Notional-Volume-for-Portfolio-Trading/default.aspx)
- [Index business growth, 2021-07-21](https://ir.theice.com/press/news-details/2021/Passive-Investing-and-ETF-Benchmark-Transitions-Drive-Strong-Growth-in-ICEs-Index-Business/default.aspx)
- [Lynn Martin podcast, 2022-03-08](https://www.ice.com/insights/conversations/inside-the-ice-house/nyse-president-lynn-martin-is-bullish-on-using-data-to-move-markets)
- [Best Execution >2M securities, 2022-06-13](https://ir.theice.com/press/news-details/2022/ICE-Best-Execution-Platform-Expands-Coverage-to-Over-2-Million-Fixed-Income-Securities/default.aspx)
- [Muni digitization tipping point, in-text Aug 2022](https://www.ice.com/insights/fixed-income-data/municipal-bond-digitization-at-a-tipping-point)
- [Nicoletta, trading-centric to data-centric, undated](https://www.ice.com/insights/fixed-income-data/fixed-income-from-trading-centric-to-data-centric)
- [Monahan, Tackling challenges around Best Execution, undated](https://www.ice.com/insights/fixed-income-data/tackling-challenges-around-best-execution)
- [An efficiency leap for FI managers, undated](https://www.ice.com/article/fixed-income/an-efficiency-leap-for-fixed-income-managers)
- [RMA relaunch, 2023-07-31](https://ir.theice.com/press/news-details/2023/ICE-Expands-Fixed-Income-Liquidity-Offering-With-Relaunch-of-Enhanced-Sweeps-Protocol-for-Corporate-Bonds/default.aspx)
- [Launching your ETF, in-text Jul 2023](https://www.ice.com/insights/fixed-income-data/launching-your-etf-three-things-to-know)
- [ICE Trading Analytics, in-text Aug 2023](https://www.ice.com/insights/fixed-income-data/ice-trading-analytics)
- [Trading Analytics: a quantitative approach, in-text Aug 2023](https://www.ice.com/insights/fixed-income-data/trading-analytics-applying-a-quantitative-approach)
- [FI ETFs and the 4pm Fair Value, in-text Feb 2024](https://www.ice.com/insights/fixed-income-data/fixed-income-etfs-when-market-structure-affects-pricing)
- [Size-Adjusted Pricing whitepaper, in-text Feb/May 2024](https://www.ice.com/insights/fixed-income-data/ice-size-adjusted-pricing-for-fixed-income)
- [Edmonds takes the reins (WatersTechnology reprint), in-text Apr 2024](https://www.ice.com/insights/fixed-income-data/chris-edmonds-takes-the-reins-at-ice-fixed-income-and-data-services)
- [Monahan, A leap forward for ICE's Evaluations, undated](https://www.ice.com/insights/fixed-income-data/a-leap-forward-for-ice-evaluations)
- [ICE Bonds × MarketAxess link, 2024-08-05](https://ir.theice.com/press/news-details/2024/ICE-Bonds-and-MarketAxess-Connect-Liquidity-Networks-to-Bring-Greater-Efficiency-to-Municipal-and-Corporate-Bond-Markets/default.aspx)
- [Supporting better outcomes for small bond trades, in-text Sep 2024](https://www.ice.com/insights/fixed-income-data/supporting-better-outcomes-for-small-bond-trades)
- [ICE Connect, Swiss army knife, in-text Oct 2024](https://www.ice.com/insights/fixed-income-data/navigating-global-markets-with-a-customizable-data-platform)
- [Edmonds, Fixed income in 2025, undated (~Dec 2024)](https://www.ice.com/insights/fixed-income/fixed-income-in-2025)
- [MBS RFQ on ICE TMC, 2025-04-16](https://ir.theice.com/press/news-details/2025/ICE-Bonds-Enhances-MBS-Trading-With-New-RFQ-Protocol-on-ICE-TMC-Platform/default.aspx)
- [PIVC, 2025-05-06](https://ir.theice.com/press/news-details/2025/ICE-Expands-Fixed-Income-Liquidity-Offering-With-Launch-of-Price-Improvement-Volume-Clearing/default.aspx)
- [Wealth-management technologies, 2025-06-09](https://www.ice.com/insights/fixed-income-data/three-financial-technologies-redefining-modern-wealth-management)
- [Institutional and retail converging, 2025-06-24](https://www.ice.com/insights/fixed-income-data/institutional-and-retail-trading-converging-in-us-corporate-bonds)
- [Liquidity metrics for bond indices, 2025-07-08](https://www.ice.com/insights/liquidity-metrics-for-bond-indices-offer-rich-opportunity)
- [Edmonds, Fixed income in 2026, undated (data to Nov 2025)](https://www.ice.com/insights/fixed-income/fixed-income-in-2026)
- [2025 data-business milestones, 2026-01-06](https://ir.theice.com/press/news-details/2026/ICE-Announces-Milestones-Across-its-Data-Business-in-2025-Including-Record-Fixed-Income-Trading-and-Clearing-Volume/default.aspx)
- [Edmonds podcast on prediction markets and data, 2026-01-14](https://www.ice.com/insights/conversations/inside-the-ice-house/ices-chris-edmonds-on-prediction-markets-data-innovation-and-how-technology-is-reshaping-trading)
- [Reddit Signals and Sentiment, 2026-01-28](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Launches-Reddit-Signals-and-Sentiment-Tool-Providing-Actionable-Market-Indicators-for-Investors/default.aspx)
- [FY25 results (segment table), 2026-02-05](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Reports-Strong-Full-Year-2025-Results/default.aspx)
- [Polymarket Signals and Sentiment, 2026-02-11](https://ir.theice.com/press/news-details/2026/ICE-Launches-Polymarket-Signals-and-Sentiment-Tool-Turning-Crowd-Sourced-Dynamic-Views-into-Market-Opportunities/default.aspx)
- [Private Credit Intelligence with Apollo, 2026-03-17](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Launches-ICE-Private-Credit-Intelligence-with-Apollo-as-Anchor-Partner/default.aspx)
- [ICE Compass, 2026-06-09](https://ir.theice.com/press/news-details/2026/ICE-Launches-AI-Powered-Fixed-Income-Pre-Trade-Analytics-for-Buyside-Investors/default.aspx)
- [ICE IDs for private credit, 2026-07-27](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Announces-Launch-of-ICE-IDs-for-Private-Credit/default.aspx)
- [FI data over MCP / AI platforms, 2026-07-29](https://ir.theice.com/press/news-details/2026/ICEs-Fixed-Income-Data-Now-Available-to-Licensed-Users-Over-Leading-AI-Platforms/default.aspx)
- [2Q26 results (segment table), 2026-07-30](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Reports-Second-Quarter-2026/default.aspx)
- [ICE to acquire MarketAxess, 2026-07-30](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-to-Acquire-MarketAxess-Creating-a-Premier-Fixed-Income-Marketplace/default.aspx)
