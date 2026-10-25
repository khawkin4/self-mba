# Note · Bloomberg's mission and the forces on it — from "news leader" with a "critical edge" to "fairness to markets": the identity moved from selling an information edge to selling neutral market infrastructure, and the forces now push the same way (electronification, mandates, passive, private markets, AI) while the threats move up the stack (cloud marketplaces, LLMs, public tapes)

> Strategy / environment-scan note · Maps to **Course 04** (Competitive Strategy: five forces, vertical integration, coopetition), **Course 11** (Global Strategy & Macro: China, India, Gulf, Brexit benchmark rules), **E5** (Transformation: Terminal company → data, index and workflow estate), **E6** (Crisis Leadership: COVID 2020, LIBOR cliff, ESG backlash, 2026 energy shock), **E9** (Geopolitics & Macro), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-people]], [[bloomberg-outside-voices]]; mirror of [[tradeweb-mission-forces]]

- **Source:** the Bloomberg corpus (`_ingest/raw/bloomberg/articles.jsonl`, **850 items**, Jan 2019 – Oct 22 2026). This covers bloomberg.com press, Professional Insights, Stories and the legacy blog (via Wayback copies, because bloomberg.com blocks scripted access), plus PR Newswire. Every "About Bloomberg" variant was dated by the readers (`reader-notes/P1–P3`, DELTA). Everything here is Bloomberg's own channels: a record of what it *wants said*. It has no financials, no Terminal price and no market share for its venues. The one exception is its own research arm, Bloomberg Intelligence (BI).
- **Core claim:** Bloomberg has no stated mission statement in the corpus. It has **boilerplate that changed once, decisively**. From 2019 to mid-2022 it is the "news leader" whose network gives decision makers "a critical edge". From mid-2022 it is "trusted data, news, and insights that bring transparency, efficiency, and fairness to markets". In 2026 the boilerplate splinters into business-line versions, some without "news" or "fairness" at all. Judged by actions, the mission is **to be the neutral layer every participant passes through**: price, benchmark, identifier, workflow and now AI context. Bloomberg avoids becoming the principal venue, the chain, or the model.
  - **Tailwinds** are structural: bond electronification, rate and settlement transitions, market openings, passive and ETF growth, regulation-as-product, private markets, and AI's hunger for clean data.
  - **Threats** are moving up the stack: hyperscaler and Snowflake marketplaces between Bloomberg and the client, LLM interfaces that could commoditise the screen, public consolidated tapes and free Treasury data, vendor-suite rivals (Aladdin) on the buy-side, and its own **China** exposure, which no Bloomberg voice ever discusses.

---

## 1. Mission and identity

### 1a. What Bloomberg says it is (verbatim, dated)

| When | Line | Where |
|---|---|---|
| 2019 → mid-2022 (BI releases still use it in 2026) | "Bloomberg, the global business and financial information and news leader, gives influential decision makers a critical edge" … "connecting them to a dynamic network of information, people and ideas." | About Bloomberg (P1, P2) |
| same era | "The company’s strength – delivering data, news and analytics through innovative technology, quickly and accurately – is at the core of the Bloomberg Terminal." | About Bloomberg |
| May/Jul 2022 → 2026 | "Bloomberg is a global leader in business and financial information, delivering trusted data, news, and insights that bring transparency, efficiency, and fairness to markets." | About Bloomberg (first seen 2022-05-26 / 2022-07-19) |
| 2024 → 2026 | "For more than four decades, the Bloomberg Terminal has revolutionized the financial services industry by bringing transparency and innovation to the capital markets." | About the Terminal |
| 2024 → 2026 | "Since 2009, Bloomberg has been building and using artificial intelligence (AI) in the finance domain" | About AI at Bloomberg |
| 2019 → 2026 | "Bloomberg provides an independent, transparent approach to indexing for customers across the globe." | Indices |
| 2022-11-08 | "Bloomberg has established a 40-year legacy of democratizing access to reliable data and building world-leading technology infrastructure" | FAST-Infra |
| 2026 (Enterprise Data) | "Through its Enterprise Data business, Bloomberg provides high-quality, fit-for-purpose datasets that power research, risk management, and execution across the global financial ecosystem." | Point-in-time data, crypto classification |
| 2026 (trading analytics) | "Bloomberg is a global leader in business and financial information, delivering trusted data, analytics and technology solutions to help organizations make better decisions." | Pre-trade TCA API |
| 2026-07-29 (CEO) | "Over four decades ago, Bloomberg revolutionized the finance industry by bringing transparency and efficiency to public markets." | Canoe |
| 2020-05-31 (founder) | "nearly all of our company’s profits go to support Bloomberg Philanthropies" | Staff memo |

### 1b. How the identity moved

1. **2019–22: edge vendor.** The pitch is a *critical edge* through a *network of people*. The Terminal is the named product. "News" leads. This is the identity [[bloomberg-terminal-instrumentation]] describes: aggregation, cross-asset grammar and the IB network.
2. **Mid-2022 → 2025: market steward.** ‘Transparency, efficiency, and fairness to markets’ is a *market-structure* claim, not a product claim. The Terminal is no longer named. The change coincides with Bloomberg co-bidding to run the EU bond consolidated tape (explored Jun 2022, see [[bloomberg-consolidated-tape]]). It also coincides with the build-out of pricing-referenced protocols ([[bloomberg-pricing-bval-ibval]]). *(Inference: when you want to be a tape provider and a benchmark administrator, "fairness" is the qualification.)*
3. **2026: business-line identities.** Enterprise Data says "fit-for-purpose datasets". Trading analytics says "data, analytics and technology solutions". Neither says "news" or "fairness". The CEO reaches back to the founding story for private markets. *(Inference: one brand, three businesses — data utility, workflow and venue tech, and the Terminal with AI — each needing its own pitch.)*

### 1c. Values and culture claims
- "open source first" (Edwards, 2023). Build in-house: "There are no good open source or commercial Market Data software solutions that our engineers can pull off the shelf" (2022).
- Human expertise in the loop: a Global Data team of 1,000+ and thousands of annotators ([[bloomberg-ai-strategy]]).
- Engineers are "more than one-third" of staff (2023). The AI group is 400+ by 2026 (Vault release).
- Philanthropy as purpose: profits go to Bloomberg Philanthropies, and so do Bloomberg Beta returns.

### 1d. What Bloomberg actually optimises for (inference, judged by actions)
- **Being the reference, not the counterparty.** It publishes the price (BVAL/IBVAL), the benchmark (Agg, BCOM, BFIX, fallbacks), the identifier (FIGI) and the TCA (BTCA). Then it builds protocols that *reference* its own numbers: the MOC-to-BVAL close and PT baskets priced off BVAL/CBBT.
- **Distribution everywhere, ownership of the data model.** It ships data to AWS, GCP and Snowflake, on-chain (Kaiko/Canton), and into client AI (Enterprise MCP). FIGI and the "data model" are what stays Bloomberg's.
- **Never be the venue that has to win share.** Venue releases avoid share claims. The only share number in 850 items is BI's report of EMSX *losing* share.
- **Long-horizon, opinion-free relationships with states.** CFETS since 2017, PBOC approvals, HKMA, India's NDS-OM, Qatar's auction system, Saudi CMA. Bloomberg never comments on risk in these markets.

---

## 2. Tailwinds

| Tailwind | Evidence (who says, when) | Admitted / Inferred |
|---|---|---|
| **Credit electronification needs intraday prices** | O'Brien: "With the electronification of fixed income markets, plus internal needs, we recognized there was a clear demand for intraday pricing" (Dec 2023). Coalition Greenwich via Sharaby: ~44% of US corporate volume electronic (Feb 2026). Krein: PT ~25% of US IG risk trades (Mar 2025) | A |
| **Portfolio trading and ETFs** | >500 ETFs track a Bloomberg FI index (2024). Credit index futures on CME/Eurex reach ~$300bn notional (Dec 2025). Kazi: passive/ETF flows "are really driving the growth" | A |
| **Rate and settlement transitions** | €STR/SOFR firsts (2019–20); ISDA fallbacks (2021); 73% of USD swaps on Bloomberg are SOFR (Feb 2022); BFIX T+1 (2024); JIBAR fallback agent (2025); Treasury clearing playbook (Oct 2026) | A |
| **Market openings** | China (Agg inclusion 2019, Bond/Swap Connect, repo), India (FAR inclusion 2024, IGB e-trading 2026), Gulf (Qatar auction 2025, Riyadh office 2026) | A |
| **Regulation as product** | FRTB, UMR, SFDR, EMIR Refit, MiFIR, Basel crypto classification, voice surveillance: "As regulatory expectations around voice surveillance continue to rise" (2026) | A |
| **Private markets** | Foster: "Private markets is a strategic priority for Bloomberg" (2025). Canoe deal (2026) | A |
| **AI needs clean data** | McManus: "the bottleneck facing financial institutions has shifted from model capability to data readiness" (Sep 2026) | A (self-serving) |
| **Passive overtaking active** | BI (Seyffart): passive likely overtakes active in US funds by ~2026 (2021) | A (BI) |

## 3. Headwinds and challenges

| Headwind | Evidence | A / I |
|---|---|---|
| **Fixed-income data is sparse and fragmented**, which caps how good any evaluated price can be | "Intraday pricing in fixed income is particularly challenging as information is fragmented" (Oct 2023). BTCA team: "Most of these models were built for centralized, high-volume equity markets and then retrofitted for fixed income as an afterthought." (Oct 2026) | A |
| **Public goods could undercut paid data**: consolidated tapes, TRACE speed-ups, FINRA next-day UST data | Bloomberg's own regulatory briefs (2024–25) track them closely. The incumbent tape JV quit in Dec 2023 | A (reported) / I (risk) |
| **Losing EMS share** | BI: "Bloomberg AIM leads OMS, followed by Charles River, while Bloomberg EMSX is still the top EMS but is losing share to rivals" (Dec 2025). EMSX 52% → 41% | A (own research arm) |
| **Vendor-suite rivals on the buy-side** | Flatman on managers "relying on a single provider" (Jul 2025). Bloomberg partners with Clearwater rather than build accounting | I |
| **Late to private markets** | Kliatchko: the deal "advances our efforts to become a leader in this space" (Oct 2026) | A (implicitly) |
| **ESG backlash hits a big product line** | ~30% of 2022–23 releases were ESG. BI frames ESG as "under pressure" (2023). Launches continue | A / I |
| **China and geopolitics** | No Bloomberg voice names a risk. ICMA does: "Even though the pandemic and geopolitical situation will create lasting risks" (2020). China's NAFMII valuation guideline (Apr 2026) aims to "level the playing field for valuation providers" | I |
| **Post-Brexit benchmark licensing** | BISL needed ESMA Art. 32 recognition from 2026-01-01 to keep EU benchmark use | A |
| **GenAI reliability** | Bloomberg's own research found RAG can make LLMs less safe (Apr 2025). 50% of UK leaders cite hallucinations (Apr 2026 poll) | A |
| **Credibility of its own numbers** | Electronic Markets dealer counts "over 1,500" vs "over 800". Ticker Plant "200 billion" vs "200 million" items a day. Data License 15k vs 40k fields. AIM stats frozen for 15 months | I |

---

## 4. Forces map, 2026 (five forces + regulation + technology)

| Force | Read for Bloomberg | Direction |
|---|---|---|
| **Rivalry** | Fragmented by layer:<br>• Pricing: ICE, S&P, LSEG, MarketAxess CP+ (→ ICE), Tradeweb Ai-Price ([[tradeweb-ai-price]], [[ice-fixed-income-data]], [[marketaxess-data-cp-plus]], [[spglobal-pricing-fixed-income]])<br>• Indices: S&P DJI, FTSE Russell, MSCI, ICE ([[lseg-ftse-russell-indices]], [[spglobal-indices-benchmarks]], [[ice-benchmarks-iba]])<br>• Venues: Tradeweb, MarketAxess (→ ICE), Trumid (→ Tradeweb)<br>• OMS/EMS: Aladdin, Charles River, FlexTrade<br>• Desktops: LSEG Workspace ([[lseg-workspace-data]]) | ↑ The 2026 consolidations (ICE–MarketAxess, Tradeweb–Trumid, LSEG–Octus) each pair a venue or data firm with a missing layer. Bloomberg already holds every layer |
| **Buyer power** | Large banks and asset managers can build in-house (BI: in-house OMS 11%), co-develop (Man Group ArcticDB) or switch EMS (EMSX share falls). Dealer consortia own rival plumbing (DirectBooks) | ↑ in execution tech, ↓ in reference data |
| **Supplier power** | Exchanges (data fees), dealers (quotes that feed CBBT and BVAL), cloud platforms (AWS, GCP, Snowflake marketplaces), AI-model providers | ↑ Cloud marketplaces sit between Bloomberg and the client; MCP is the counter |
| **Substitutes** | Public tapes and TRACE; free or cheap terminals for equities ([[bloomberg-terminal-instrumentation]] §1); general LLMs answering finance questions; on-chain data | ↑ at the edges. The Terminal note's ‘commodity Layer 1’ argument now applies to AI |
| **Entry** | Fintech pricing and AI firms (Kaiko, Allium, Canoe, Daphne), which Bloomberg partners with or buys | Bloomberg's habit is partner, then buy ([[bloomberg-private-markets]]) |
| **Regulation** | Benchmark rules (BMR, IOSCO), MiFIR tape and cost-of-data rules, SEC Treasury clearing, Basel crypto, AI rules | Mostly a tailwind (demand for compliance data). The tape and data-cost rules are the exception |
| **Technology** | Cloud, ML pricing, LLM agents, tokenization | Bloomberg's answer is to be the *context layer*: Enterprise MCP, ASKB grounded on IB chats, data on Canton |

## 5. Crisis tests — what each one revealed

| Crisis | What Bloomberg said or did | Revealed |
|---|---|---|
| **COVID, Mar 2020** | DL+ release pulled forward; MAP usage up "300%"; LQA work found TRACE volumes held but trade costs rose 5–20x (P7, Apr 2020); AIM executions +85% week over week (2021 blog) | Liquidity = cost, not volume. That is the data case for LQA and later IBVAL. Remote work accelerated data-in-cloud |
| **LIBOR cessation, 2021–23** | Fallback calculator, BSBY bid, SOFR-share data from its own venues | Bloomberg plays every role in a transition: venue, benchmark, calculator. The one failure (BSBY) is never discussed |
| **ESG backlash, 2022–24** | Continued launches. BI admits "under pressure" | No retreat in product messaging: a platform hedges by carrying everyone's ratings (MSCI, Sustainalytics) |
| **SVB / Credit Suisse, Mar 2023** | Nothing in the corpus | Absence: Bloomberg doesn't publish stress-test narratives the way Tradeweb does ([[tradeweb-mission-forces]] §5) |
| **US–Iran war, Q1 2026** | BCOM +24% and BCOM Energy +63% in Q1. New liquidity-weighted oil and gas index adds Murban, TTF, NBP | Index design marketed as validated by the shock |

## 6. Scenarios to 2030 (inference, not Bloomberg's)

1. **Reference-price utility (base case).** IBVAL becomes the de facto intraday mark for global credit. Bloomberg indices plus futures plus Tradable Trackers form a credit ‘equity-like’ complex. Venues compete on top of Bloomberg's numbers. *Signal:* more MOC and PT protocols referencing BVAL, and third-party venues licensing IBVAL.
2. **Unbundled by the cloud.** Snowflake/AWS marketplaces and client AI agents make the Terminal one source among many. Bloomberg keeps data-licensing revenue but loses the screen. *Signal:* Enterprise MCP adoption outpacing ASKB; price pressure in Data License renewals (not observable in the corpus).
3. **Public tape erodes the data rent.** EU/UK bond tapes plus faster TRACE and free UST data compress the value of composite quotes (CBBT) and evaluated pricing in liquid bonds. Value shifts to illiquid and private assets, which is exactly where Canoe and DLEN point. *Signal:* Bloomberg product launches skew further to private credit, loans, CLOs and securitized.
4. **Geopolitical break in China.** A sanctions or data-localisation event cuts the CFETS, Bond Connect and Swap Connect business and the China weight in the Agg becomes political. *Signal:* NAFMII-style local-provider rules; index consultations on China weight.

## 7. Canon lenses

- [[canon-porter-competitive-strategy]] — Bloomberg's answer to five forces is **vertical integration across information layers**: price → index → identifier → workflow → venue. Every rival consolidation of 2026 is an attempt to assemble the stack Bloomberg already holds.
- [[canon-helmer-7-powers]] — *Cornered resource:* proprietary pricing inputs, the IB chat graph and the annotated-document corpus. *Switching costs:* FIGI-keyed data models, BVAL history in valuation policies, AIM/PORT integration. *Counter-positioning:* a private firm can run a 40-year horizon without quarterly disclosure.
- [[canon-shapiro-varian-information-rules]] — Version and bundle: ALTD is folded into the Terminal subscription, and basic Credit Benchmark data comes at no extra charge. Information goods with lock-in through standards (FIGI) and formats (BQL, DL+).
- [[canon-brandenburger-nalebuff-coopetition]] — Bloomberg co-bids with Tradeweb and MarketAxess (tape), partners with S&P (primary bonds), MSCI (ESG indices), Clearwater (accounting) and CME (Eris trackers), and competes with all of them.
- [[canon-meadows-leverage-points]] — The highest-leverage point Bloomberg controls is *the rules of measurement* (benchmarks, reference prices, TCA). It changes behaviour without being a participant.
- [[canon-taleb-antifragile]] — Volatility increases demand for prices, risk and TCA (COVID, 2026 energy shock). The fragility is concentrated in one geopolitical exposure (China) and in being the single source behind many automated decisions.

## 8. Open questions to track

1. Is the 2026 boilerplate split deliberate (separate businesses) or drift? Does "fairness to markets" survive in corporate releases in 2027?
2. Who are Bloomberg's CEO, President and Chairman *formally*, and when were Kliatchko and Zammitt appointed? (Outside the corpus.)
3. Does any third-party venue adopt IBVAL as a closing or reference price?
4. Does EU/UK tape adoption visibly change Bloomberg's pricing or data launches toward illiquid and private assets?
5. Does BI publish a follow-up European trading study in 2026, and does EMSX share keep falling?
6. China: any Bloomberg statement on NAFMII valuation rules or on China's weight in the Global Agg?

**Links:** [[bloomberg-hub]] · [[bloomberg-people]] · [[bloomberg-outside-voices]] · [[bloomberg-pricing-bval-ibval]] · [[bloomberg-indices]] · [[bloomberg-electronic-trading]] · [[bloomberg-consolidated-tape]] · [[bloomberg-ai-strategy]] · [[bloomberg-enterprise-data]] · [[bloomberg-private-markets]] · [[bloomberg-buyside-stack]] · [[bloomberg-terminal-instrumentation]] · [[tradeweb-mission-forces]] · [[ice-mission-forces]] · [[lseg-mission-forces]] · [[spglobal-mission-forces]] · [[marketaxess-mission-forces]] · [[canon-porter-competitive-strategy]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-meadows-leverage-points]] · [[canon-taleb-antifragile]]

---
### Rep
**(a) Boilerplate as evidence.** Count the words "news", "Terminal" and "fairness" in the two About Bloomberg versions quoted in §1a. *(Answer: 2019 version: news 1, Terminal 1, fairness 0. 2022 version: news 1, Terminal 0, fairness 1.)* In one paragraph, argue whether the swap of "Terminal" for "fairness" is a strategy change or a PR change. Use one action from §1d as evidence either way.

**(b) Forces arithmetic.** BI's study shows EMSX falling from 52% to 41% of European buy-side EMS usage in a year. If the decline continues linearly, in what year does EMSX fall below Charles River's OMS share (23%)? *(Answer: −11pp a year → 30% in 2026, 19% in 2027, so below 23% during 2027.)* Then name two reasons from §3 and §4 why linear extrapolation is wrong. (Example: the switching costs in [[bloomberg-buyside-stack]].)

**(c) Scenario signals.** For each §6 scenario, write the one Bloomberg press release that would most surprise you in 2027. Set a reminder to check the PR Newswire Bloomberg newsroom in Oct 2027.

---
**Sources (in `_ingest/raw/bloomberg/articles.jsonl`):**
- [About Bloomberg, old wording, e.g. LIC MF, 2021-12-20](https://www.bloomberg.com/company/press/lic-mutual-fund-adopts-bloomberg-solutions-for-enterprise-wide-digital-transformation/)
- [About Bloomberg, new wording, e.g. Polymer, 2022-05-26](https://www.bloomberg.com/company/press/polymer-capital-forms-data-and-technology-partnership-with-bloomberg/)
- [AI earnings call summaries (About the Terminal / AI), 2024-01-22](https://www.bloomberg.com/company/press/bloomberg-launches-ai-powered-earnings-call-summaries/)
- [Point-in-time economic data (Enterprise Data boilerplate), 2026-05-07](https://www.prnewswire.com/news-releases/bloomberg-introduces-point-in-time-economic-data-to-power-quantitative-research-and-strategy-development-302765281.html)
- [Pre-trade TCA API (trading boilerplate), 2026-07-08](https://www.prnewswire.com/news-releases/bloomberg-launches-pre-trade-tca-api-bringing-execution-intelligence-into-proprietary-trading-workflows-302820323.html)
- [FAST-Infra, 2022-11-08](https://www.bloomberg.com/company/press/fast-infra-announces-fast-infra-sustainable-infrastructure-label-secretariat-and-data-repository/)
- [To the Bloomberg family, 2020-05-31](https://www.bloomberg.com/company/press/to-the-bloomberg-family/)
- [Canoe acquisition, 2026-07-29](https://www.prnewswire.com/news-releases/bloomberg-to-acquire-canoe-intelligence-taking-a-defining-step-in-its-mission-to-transform-private-markets-investing-302837466.html)
- [Canoe completed, 2026-10-01](https://www.bloomberg.com/company/press/bloomberg-completes-canoe-intelligence-acquisition-advancing-strategy-to-transform-private-markets-investing/)
- [ArcticDB, 2023-02-27](https://www.bloomberg.com/company/press/man-group-brings-powerful-dataframe-database-product-arcticdb-to-market-with-bloomberg/)
- [Ticker Plant, 2022-03-05](https://www.bloomberg.com/company/stories/how-bloomberg-handles-a-massive-wave-of-real-time-market-data-in-microseconds/)
- [IBVAL ML story, 2023-12-04](https://www.bloomberg.com/company/stories/how-bloomberg-uses-machine-learning-intraday-pricing-transparency/)
- [IBVAL Front Office launch, 2023-10-17](https://www.bloomberg.com/company/press/bloomberg-launches-front-office-pricing-solution-providing-greater-visibility-into-fixed-income-trading/)
- [Credit market infrastructure (Sharaby), 2026-02-18](https://www.bloomberg.com/professional/insights/trading/how-tradable-products-and-modern-market-infrastructure-are-reshaping-credit-markets/)
- [Portfolio trading podcast, 2025-07-07](https://www.bloomberg.com/professional/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/)
- [Indices 2025 outlook, 2025-01-24](https://www.bloomberg.com/professional/insights/markets/indices-2025-outlook-fixed-income/)
- [SOFR liquidity, 2022-02-09](https://www.bloomberg.com/professional/insights/regulation/sofr-liquidity-eclipses-libor/)
- [Treasury clearing, 2026-10-08](https://www.bloomberg.com/professional/insights/regulation/cash-now-repo-next-planning-for-the-u-s-treasury-clearing-transition/)
- [Vault BSpeech, 2026-05-14](https://www.prnewswire.com/news-releases/bloomberg-vault-integrates-bspeech-unlocking-multi-language-voice-transcription-capabilities-across-50-languages-for-compliance-professionals-302771957.html)
- [Daphne, 2025-02-10](https://www.bloomberg.com/company/press/bloomberg-and-daphne-partner-to-streamline-access-to-reliable-private-markets-data/)
- [Enterprise MCP, 2026-09-29](https://www.bloomberg.com/company/press/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications/)
- [BI passive vs active, 2021-03-11](https://www.bloomberg.com/professional/insights/markets/passive-likely-overtakes-active-by-2026-earlier-if-bear-market/)
- [BTCA fixed income, 2026-10-13](https://www.bloomberg.com/professional/insights/financial-services/beyond-the-benchmark-using-advanced-analytics-to-navigate-fixed-income-trading-costs/)
- [BI EET technology, 2025-12-08](https://www.bloomberg.com/professional/insights/trading/european-institutional-equity-trading-study-technology/)
- [Clearwater partnership, 2025-07-09](https://www.bloomberg.com/company/press/bloomberg-and-clearwater-analytics-partner-to-optimize-investment-management-workflows/)
- [Hong Kong/GBA panel (ICMA), 2020-10-16](https://www.bloomberg.com/company/press/capturing-cross-border-investment-opportunities-in-hong-kong-and-the-greater-bay-area/)
- [APAC Regulatory Outlook 2026, 2026-02-02](https://www.bloomberg.com/professional/insights/regulation/apac-regulatory-outlook-2026/)
- [BISL EU BMR recognition, 2025-12-18](https://www.bloomberg.com/company/press/bloomberg-index-services-limited-receives-recognition-under-the-eu-benchmark-regulation/)
- [RAG safety research, 2025-04-28](https://www.bloomberg.com/company/press/bloomberg-ai-researchers-mitigate-risks-of-unsafe-rag-llms-and-genai-in-finance/)
- [UK AI survey, 2026-04-21](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-survey-uk-finance-leaders-say-inaccurate-outputs-are-the-biggest-barrier-to-ai-adoption/)
- [Liquidity in a new abnormal (LQA), 2020-04-09](https://www.bloomberg.com/professional/blog/assessing-liquidity-for-a-new-abnormal/)
- [US–Iran war and commodities, 2026-04-02](https://www.bloomberg.com/professional/insights/commodities/what-the-us-iran-war-means-for-commodity-markets-and-portfolios/)
