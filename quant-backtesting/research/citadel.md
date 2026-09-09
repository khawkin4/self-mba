Here is the comprehensive research report on Citadel LLC and Citadel Securities.

---

## 1. Citadel LLC vs. Citadel Securities: Structure and Difference

These are **separate legal entities**, both founded by Ken Griffin, with distinct management, technology infrastructure, and compliance programs. Federal law requires information barriers between them.

**Citadel LLC** is a multi-strategy hedge fund founded in 1990, managing **$66 billion** in investment capital as of February 2026. It pools money from institutional investors and wealthy individuals, deploying strategies across equities, fixed income, commodities, credit, and quantitative. Its flagship Wellington fund has achieved approximately **19% annualized returns** since inception.

**Citadel Securities** is a market maker and broker-dealer established in 2002. It executes trades for retail and institutional clients, handling approximately **40% of U.S. retail equity volume** and serving as the leading Designated Market Maker on the NYSE. In January 2022, Sequoia Capital and Paradigm invested **$1.15 billion** for a minority stake, valuing the firm at **$22 billion**.

**Revenue models differ fundamentally**: the hedge fund profits from investment returns on managed capital. Citadel Securities earns through bid-ask spread capture and payment for order flow (PFOF) arrangements. The hedge fund falls under Investment Advisers Act fiduciary obligations; Citadel Securities falls under SEC/FINRA broker-dealer oversight.

Sources: [LegalClarity](https://legalclarity.org/citadel-securities-vs-citadel-the-key-differences/), [QuantBrainteasers](https://quantbrainteasers.com/blog/citadel-vs-citadel-securities/), [CNBC - Sequoia](https://www.cnbc.com/2022/01/11/citadel-securities-valued-at-22-billion-after-investment-from-sequoia-paradigm.html), [Citadel Securities PR](https://www.citadelsecurities.com/news-and-insights/citadel-securities-announces-1-15-billion-investment-from-sequoia-and-paradigm/)

---

## 2. Systematic Trading Strategies (Citadel LLC)

Griffin launched Citadel at age 22 with **convertible bond arbitrage**, expanding into statistical arbitrage (1994), fixed-income macro (1999), fundamental equities (2001), and commodities (2002).

**Post-2008 pod structure**: The firm reorganized into discrete "pods" -- teams of 4-8 professionals led by portfolio managers with specific sector mandates. Multiple equity units (Global Equities, Surveyor Capital, Ashler Capital) create internal competition while maintaining market neutrality.

**Key strategy areas**:

- **Equities**: Fundamental long/short (market-neutral), statistical arbitrage across 15,000+ securities in 30+ countries, pairs trading, factor investing, mean reversion, and ML-driven pattern detection in order flow and sentiment.
- **Fixed Income & Macro**: Interest rate swaps, government bonds, FX, yield curve modeling. Positioned early for 2022 rate hikes, capturing outsized gains.
- **Commodities**: Deep supply-demand research including satellite crop imagery, proprietary weather forecasting, physical market participation (storage, tanker chartering).
- **Credit**: Convertible arbitrage, high-yield/distressed, structured credit, CLO tranches, capital structure arbitrage.
- **Global Quantitative Strategies (GQS)**: Founded 2012, trades 15,000+ instruments across 30+ countries using neural networks, NLP on news/social media, and ensemble methods combining hundreds of weak predictors.

**Performance**: Wellington gained +15.1% in 2024 and +10.2% in 2025. The three largest funds generated **$56.8 billion** in gains from 2021 through September 2024. Overall, the firm has generated **$60+ billion** in net gains since inception.

Sources: [DayTrading.com](https://www.daytrading.com/citadel-ken-griffin-strategies), [CNBC 2024](https://www.cnbc.com/2025/01/02/ken-griffins-flagship-hedge-fund-at-citadel-climbs-15point1percent-in-2024.html), [CNBC 2025](https://www.cnbc.com/2026/01/02/ken-griffins-flagship-hedge-fund-at-citadel-rises-10point2percent-in-volatile-2025.html), [Hedgeweek - $57B](https://www.hedgeweek.com/citadel-prospectus-reveals-57bn-in-gains-from-largest-funds/), [Stanford GSB](https://www.gsb.stanford.edu/insights/ken-griffin-investing-winning-why-hes-focused-future)

---

## 3. Citadel Securities: Market Making Methodology and Scale

Citadel Securities executes over **$400 billion in trades daily**, processes over 35% of U.S. equity trades (exceeding the entire Nasdaq exchange), and serves 1,600+ institutional clients including sovereign wealth funds and central banks. About one-sixth of its 1,800 employees hold PhDs.

**Financial scale**: In FY2024, net trading revenue reached **$9.7 billion** (+55% YoY), EBITDA hit $5.2 billion (+87% YoY), and net income exceeded $4.2 billion. In FY2025, revenue surged to a record **$12.2 billion** (+25% YoY) with ~$6.5 billion EBITDA. Q1 2025 alone delivered $3.4 billion in revenue and $1.7 billion net income (58% EBITDA margin).

**Methodology**: The firm processes trillions of data points with high-frequency algorithms. Revenue is built on capturing the bid-ask spread across massive electronic order flow -- small per-trade margins multiplied by enormous volume. The firm calculates exposure across multiple business lines and product sets, capturing netting effects across client and proprietary positions. In 2025, they expanded "high-touch" services where humans complement machines.

**PFOF**: Citadel Securities spent approximately **$2.6 billion annually** on payment for order flow (2020-2021), with $1.7 billion on options and $877 million on equities. They are the largest consolidator of retail options flow per SEC data.

**Expansion**: The firm is scaling into U.S. Treasuries, corporate credit, and European government bonds, with offices opened in Tokyo and Paris (2024).

Sources: [Google Cloud Blog](https://cloud.google.com/transform/citadel-securities-reimagine-quantitative-reseach-cloud-scale-speed), [Hedgeweek - $9.7B](https://www.hedgeweek.com/griffins-citadel-securities-reports-record-9-7bn-trading-revenue/), [Bloomberg - $12B](https://www.bloomberg.com/news/articles/2026-03-24/citadel-securities-nets-record-12-billion-trading-haul-in-2025), [Hedgeweek - Q1](https://www.hedgeweek.com/citadel-securities-smashes-q1-records-with-3-4bn-in-trading-revenue/), [The TRADE - PFOF](https://www.thetradenews.com/citadel-securities-forks-out-2-6-billion-annually-for-payment-for-order-flow-and-most-of-its-on-options/), [Risk.net](https://www.risk.net/awards/7962597/flow-market-maker-of-the-year-citadel-securities)

---

## 4. Market Microstructure and Order Flow

Citadel Securities' core business is providing liquidity by standing on both sides of the market. Their edge comes from:

- **Scale-driven netting**: Calculating exposure across all business lines and product sets to capture more netting effects than competitors.
- **Speed**: Ultra-low-latency infrastructure with kernel bypass networking (DPDK, Solarflare), CPU pinning, lock-free data structures, and FPGA hardware acceleration.
- **Statistical modeling**: Hundreds of quantitative researchers build pricing models for hundreds of thousands of securities, using statistical models to manage inventory risk in real time.
- **PFOF flywheel**: Retail brokerages route orders to Citadel Securities in exchange for compensation. This gives Citadel access to predominantly uninformed retail flow (lower adverse selection risk), allowing tighter spreads. They handle ~40-45% of all U.S. retail equity orders.

The firm is the largest Designated Market Maker on the NYSE and operates across equities, options, fixed income, and FX globally.

Sources: [Trade Ideas](https://www.trade-ideas.com/2025/05/10/citadel-securities-the-invisible-hand-behind-retail-trading/), [TechInterview](https://www.techinterview.org/companies/citadel-securities/), [Risk.net](https://www.risk.net/awards/7958404/flow-market-maker-of-the-year-citadel-securities)

---

## 5. Technology Infrastructure

**Cloud compute at scale**: Through a partnership with Google Cloud, Citadel Securities runs over **1 million cores concurrently** for quantitative research. They reframed their approach from "replicate on-prem in cloud" to "what's the most productive, scalable, cost-efficient research platform?" Single workloads that once took hours now complete in seconds. Cost-per-research-hour dropped "precipitously." The platform uses 200 Gbps connectivity, dedicated interconnects from their data centers, and a mix of on-demand, preemptible, GPU-accelerated, and compute-optimized instances.

**Low-latency trading**: The firm employs FPGA engineers, kernel bypass networking, lock-free data structures, and CPU pinning for trading infrastructure. They operate global data centers with co-located racks for low-latency market connectivity.

**Engineering culture**: "CitadelX" is an elite internal engineering group. Site reliability engineers combine software and systems engineering to power strategies at speed and scale. Head of Research Platform is Costas Bekas.

Sources: [Google Cloud Blog](https://cloud.google.com/transform/citadel-securities-reimagine-quantitative-reseach-cloud-scale-speed), [TechInterview](https://www.techinterview.org/companies/citadel-securities/), [Citadel Securities Careers](https://www.citadelsecurities.com/careers/quantitative-research/)

---

## 6. Published Research and Researcher Profiles

Citadel LLC has **19 researchers/authors** who have collectively produced **33 publications** receiving **850 citations** (per SciSpace). Notable authors include Frank Fehle and G. Luckjiff. However, detailed paper titles and topics are not publicly enumerated -- the firm is notably secretive about proprietary research.

**Key research leaders**:
- **Peng Zhao** (CEO, Citadel Securities): PhD-holding "math prodigy" hand-picked by Griffin, profiled in Bloomberg Businessweek.
- **Perry Vais**: Head of Equity Quantitative Research at Citadel, overseeing research and analytics for equity platforms.
- **Costas Bekas**: Head of Research Platform at Citadel Securities.

72% of researchers hold advanced degrees; 65% come from computer science backgrounds. Citadel Securities employs hundreds of quantitative researchers building pricing models for thousands of securities.

Sources: [SciSpace - Citadel LLC](https://scispace.com/institutions/citadel-llc-2muw4r60), [Citadel Careers](https://www.citadel.com/careers/quantitative-research/), [Citadel Securities Careers](https://www.citadelsecurities.com/careers/quantitative-research/), [Bloomberg via Citadel Securities](https://www.citadelsecurities.com/news-and-insights/ceo-peng-zhao-profiled-in-bloomberg-businessweek-ken-griffins-hand-picked-math-prodigy-runs-market-making-empire/)

---

## 7. Ken Griffin's Public Statements

**On AI (May-July 2026)**: Griffin's views shifted dramatically. At Davos 2026, he dismissed much AI as "garbage." By May 2026 at Stanford, he acknowledged "for the first time, AI is real" and said he "went home one Friday actually fairly depressed" at the implications. He noted that work previously requiring teams of PhDs for weeks is now completed by AI agents in hours. He drew a distinction between modest 15-25% software engineering gains and far more disruptive knowledge-work transformation. He stated there would be "no reduction to headcount at Citadel" -- framing gains as expanding capacity. Citadel introduced an internal AI assistant for equities research.

**On risk management**: "Risk management is the pillar of stability" at the intersection of opportunity. The Portfolio Construction & Risk Group reports directly to Griffin, independent of trading desks.

**On investing**: At Stanford, Griffin said successful investors "know when they have an advantage and they press it." He noted Citadel's alpha win rate is only **54%**, framing this as "remarkable." He emphasizes analyzing wins over fixating on losses.

**On talent**: Griffin hires "winners in life" not just finance specialists -- physicists, engineers, computer scientists. Stars earn eight-figure bonuses; underperformers face quick exits.

**On markets (2025-2026)**: Griffin warned that the Japanese bond sell-off is an "explicit warning" for U.S. policymakers and that "bond vigilantes" may emerge if fiscal discipline erodes. He cautioned that rate hikes remain possible.

Sources: [The Deep Dive - AI](https://thedeepdive.ca/ken-griffin-ai-citadel-shift/), [Fortune - AI](https://fortune.com/2026/05/18/billionaire-ken-griffin-ai-garbage-depressed-dramatic-impact-society/), [Stanford GSB](https://www.gsb.stanford.edu/insights/ken-griffin-investing-winning-why-hes-focused-future), [Yahoo Finance - Inflation](https://finance.yahoo.com/economy/policy/articles/citadels-ken-griffin-just-said-092600224.html), [Davos 2026](https://www.weforum.org/meetings/world-economic-forum-annual-meeting-2026/sessions/conversation-with-ken-griffin-president-and-ceo-of-citadel/), [Goldman Sachs](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/citadels-ken-griffin-on-ai-us-china-tensions-and-us-data-centers)

---

**Peng Zhao (Citadel Securities CEO) on market making**: At the 2025 Future of Global Markets conference with Sequoia's Alfred Lin, Zhao discussed how AI, automation, and client obsession are transforming markets. He emphasized: "The most valuable resource today isn't GPUs -- it's talent." He warned against superficial AI adoption, arguing the real advantage lies in combining proprietary data, technical expertise, and workflow integration.

Sources: [Milken Institute panel](https://milkeninstitute.org/content-hub/event-panels/conversation-citadel-securities-ceo-peng-zhao), [Citadel Securities - Zhao & Lin](https://www.citadelsecurities.com/news-and-insights/future-of-global-markets-2025-conference/ceo-peng-zhao-sequoias-alfred-lin-discuss-the-future-of-markets/)