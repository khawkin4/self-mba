# Note · Bloomberg Enterprise Data — selling the Terminal's data without the Terminal, through other people's clouds, while keeping the licence as the leash

> Strategy / data-business note · Maps to **Course 04** (Competitive Strategy: channels, coopetition, who owns the customer), **Course 07** (Data, Analytics & Decision-Making: point-in-time data, self-reported counts, evaluation cost), **Course 05** (Marketing & Brand: versioning, entitlements, free identifiers), **E10** (Digital & AI Transformation: cloud, marketplaces, MCP), **E3** (M&A, Deals & Restructuring: RegTek, Second Measure, ArcticDB as a partnership in place of a purchase) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-ai-strategy]], [[bloomberg-pricing-bval-ibval]], [[bloomberg-buyside-stack]], [[bloomberg-terminal-instrumentation]]

- **Source:** about 45 Bloomberg items in `_ingest/raw/bloomberg/articles.jsonl` (press releases on bloomberg.com via Wayback, PR Newswire releases for 2024–26, Insights articles and one Tech-at-Bloomberg story), **Aug 2019 – Oct 22 2026**, each read in full for the facts used here. Bloomberg is private. There is **no revenue, margin, client count or price** for Enterprise Data anywhere in the corpus. The only usage figure is PORT Enterprise's "more than 600 clients" (2024-12-04). Every number below is a Bloomberg boilerplate or launch claim unless another source is named.
- **Core claim:** Enterprise Data is Bloomberg's way of selling Terminal-grade content to machines that don't need the screen. Real-time data goes out as B-PIPE, bulk data as Data License, and both get managed for the client through DL+. It now reaches clients through *their* infrastructure: AWS (2019), Google Cloud (2022), a Snowflake Native App (2023), AWS/Azure/GCP for tick data (2024), Kaiko on the Canton chain (2026) and an MCP server for clients' AI agents (2026). The catalogue claim grew from **50 million securities and 15,000–30,000 fields** (2022–23) to **100 million securities and 50,000 fields** (Sep 2026). The pattern I infer: Bloomberg lets the hyperscalers, Snowflake and blockchains carry the bytes, but it never lets them hold the **entitlement**. Every channel checks a Bloomberg Data License before it returns data. So the marketplaces are pipes, not stores, and Bloomberg keeps the customer. Tony McManus's 2026 line sums up the pitch: "Connections were never the hard part. Readiness is".

---

## 1. Chronology — the spine

| Date | Event | Numbers stated (Bloomberg unless noted) |
|---|---|---|
| 2018 / Feb 2019 | **Enterprise Access Point (EAP)** launches. One release dates it to 2018, another to February 2019 (§4). | — |
| 2019-08-13 | Buys **RegTek.Solutions** and folds it into **RHUB** (Regulatory Reporting Hub). | No price |
| **2019-09-12** | **B-PIPE on AWS** worldwide. A US-only cloud launch came first. Bloomberg calls it "one of the only cloud native real-time data products suitable for capital markets use cases". | 35m instruments, 330+ exchanges, 5,000+ contributors |
| **2020-05-06** | **Data License Plus (DL+)**: a managed service that merges a client's Bloomberg data into one linked dataset. Launch was "accelerated" by COVID. | — |
| 2020-05-13 | EAP becomes a **self-service marketplace** with click-to-buy and a dataset creator. | — |
| 2020-07-06 | Brazil's **ABNT** adopts FIGI (NBR 16885:2020). | "over 700 million FIGIs issued" |
| 2020-09-16 | EAP alt-data shelf expands. | **60+** third-party vendors, "three-fold" since launch |
| **2020-12-24** | Completes the **Second Measure** acquisition (card-spend analytics). | No price |
| 2021-09-15 | **ASC X9.145-2021** makes FIGI a US national standard (OMG standard since 2014; ABNT 2020). | — |
| **2021-09-29** | **BQuant Enterprise**: a cloud Python/Jupyter platform with Bloomberg data loaded. | — |
| 2021-10-14 | First **crypto FIGIs**, with Kaiko as Certified Provider. | All fiat-denominated BTC and ETH instruments |
| 2021-11-04 | **Server API (SAPI)** explainer: Terminal entitlements feed a client's server apps. | Four service tiers |
| 2022-01-20 | Sony Bank runs B-PIPE, BVAL and Data License inside its own AWS stack. | DL: **50m securities, 30k fields** |
| **2022-03-10** | **B-PIPE on Google Cloud**. | 35m instruments, 330+ exchanges, **80bn ticks a day** |
| 2022-04-27 | LEI Common Data Format 3.1. Bloomberg is an accredited LEI **Local Operating Unit** and gains a second accreditation, for funds. | Six new entity-category fields |
| 2022-07-13 | M&G picks Bloomberg **sanctions data**, delivered through DL+. | 10 jurisdictions monitored |
| 2023-02-27 | **ArcticDB**: Man Group's DataFrame database goes into BQuant under a multi-year open-source agreement. | "over one million downloads since 2015" |
| 2023-04-11 | Vancity takes PORT Enterprise and Data License. | DL: 50m securities, **15k fields** |
| 2023-06-06 | **Funds Data Solution** on Data License. | 135,000 funds, 12,000 ETPs |
| **2023-06-28** | **DL+ Snowflake Native App**, announced at Snowflake Summit. Clients provision their own DL subscriptions inside their Snowflake account. | 50m securities, **40k fields** |
| **2023-09-07** | **ALTD<GO>** on the Terminal. Second Measure is the flagship source; Placer.ai is the launch partner. | 300+ public tickers. 7-day lag (story) |
| 2024-01-10 | BTCA Data Access API joins TCA data to DL reference and pricing data. | DL: **70m securities, 40k fields** |
| **2024-04-09** | **Point-in-Time** company financials, estimates and pricing for quants. | — |
| 2024-05-22 | Second Measure feeds on **Data License** for the first time. | 20m+ consumer panel. 3,000+ companies, 4,000+ brands. **3-day lag** |
| 2024-09-09 | **BSM U.S. Consumer Spend Index** in ECAN. | Consumer spending ≈ "nearly 70 percent" of GDP |
| **2024-09-17** | **Virtual Data Room (VDR)**: try bulk datasets in hosted Jupyter notebooks before subscribing. | Evaluations "upwards of 90 days", over half of that admin |
| 2024-10-01 | OHLC bars on Tick History, "natively available on AWS, Azure and GCP". | 350+ exchanges, 70m+ instruments |
| 2024-11-25 | Baader Bank takes SFDR data. | 16,000+ companies |
| **2024-12-04** | **PORT Enterprise data to Snowflake via DL+**. | PORT Enterprise "more than 600 clients" |
| 2025-01-14 | Research-data survey of 150+ quants. | 37% say historical-data quality is the top challenge. 72% can evaluate ≤3 datasets at a time. 65% take ≥1 month per dataset. 62% want cloud delivery |
| 2025-01-28 | **NAIC** principles-based bond classification for insurers. | Four classification fields |
| 2025-02-06 | Vietnam Maritime Bank adopts B-PIPE. | 35m instruments, **350+** exchanges |
| 2025-06-04 | **Similarweb** web traffic added to ALTD. | Coverage to 3,000+ companies. 7-day lag, 5 years of history |
| 2025-09-16 | **HQLA** solution extended to the UAE and Qatar. | 12 jurisdictions. Four core datasets |
| 2025-12-04 | BQuant **Code Crunch** in London: T. Rowe Price, Atlantic House, J.P. Morgan. | Four-month programme |
| 2026-01-22 | Second quant survey. | **54%** have not started on GenAI. 72% want sector-specific data |
| **2026-01-28** | **Alt-data entitlements** in ALTD: premium Placer.ai and Similarweb metrics. | 5,000+ KPI estimates. Lag 3–5 days entitled vs 7–14 days without |
| **2026-02-26** | **Kaiko + Canton**: DL security master and evaluated pricing to be available on-chain for tokenized UST and repo. | Phase 1 only. No live date |
| 2026-05-07 | **Point-in-time economic data** on DL. | 3,000+ indicators, 100+ economies, history from 1997 |
| 2026-09-23 | **CLO reference data**, including loan-level data, on DL; ASKB access planned. | — |
| **2026-09-29** | **Enterprise MCP** over DL+. McManus is now 'Global Head of Enterprise Data and Indices'. | **100m+ securities, 50k+ fields** |
| 2026-09-30 | **Stablecoin dashboard** (RWAS<GO>) using Allium data. | Covers every coin >$100m supply, "collectively more than 98% of the market". Stablecoin supply >$300bn |
| 2026-10-22 | **Basel crypto exposure classification** (BCBS Groups 1a–2b). | ~1,700 funds flagged, about half with undeclared crypto exposure. 125,000 fund tickers covered |

## 2. The product stack, by how data leaves Bloomberg

| Layer | Product | What it sells | Channel it rides | Leash it keeps |
|---|---|---|---|---|
| Real-time | **B-PIPE**, SAPI | Normalised tick data and the Terminal's real-time feed into client apps | On-prem, hosted, AWS (2019), Google Cloud (2022) | Exchange and Bloomberg entitlements. SAPI reuses "existing Bloomberg Terminal exchange entitlements" |
| Bulk / batch | **Data License**, Tick History, PiT, Funds, CLO | Reference, pricing, regulatory, fundamentals and history | SFTP, REST, AWS/Azure/GCP, data.bloomberg.com | The DL contract, per content domain |
| Managed data | **DL+** | Linked, modelled 'unified data model' of what the client already licenses | Snowflake Native App (2023), PORT to Snowflake (2024), MCP (2026) | Provisioning of "their set of Bloomberg Data License subscriptions" |
| Discovery | **EAP** (2018/19), **VDR** (2024) | Catalogue, samples, click-to-buy, test-drive notebooks | Bloomberg's own web | Bloomberg runs the storefront itself; no third-party marketplace is named as a sales channel |
| Compute | **BQuant Enterprise** (+ ArcticDB) | Hosted research environment with the data pre-wired | Bloomberg-managed cloud, client S3 buckets | Data never leaves Bloomberg's entitlement model |
| Alt data | EAP shelf (60+ vendors), **Second Measure**, ALTD | Third-party and owned alt data next to fundamentals | Terminal (ALTD) and DL | Owned panel (BSM) plus resold vendor entitlements |
| Identity | **FIGI**/OpenFIGI, LEI LOU | Free, open identifiers | OMG, ABNT, X9, Kaiko | None on the ID. The leash sits on the data joined to it |
| Regulatory | RHUB/RegTek, sanctions, SFDR, HQLA, NAIC, Basel crypto | Rule-mapped classification fields | DL and DL+ | Methodology and updates |
| On-chain | Kaiko/Canton, Allium | DL data on-chain; on-chain data on the Terminal | Canton Network; RWAS<GO> | "Entitlement controls are designed to ensure only licensed participants can access Bloomberg data, consistent with traditional data licensing frameworks." |

## 3. How the narrative moved

1. **2019–2020: 'same data, your deployment'.** B-PIPE in the cloud gives "the same normalized, consolidated real-time market data available through the Bloomberg Terminal". The buy-side quote is about cost. Balyasny: "Connecting to B-PIPE on AWS allows us to capitalize on several operational efficiencies, while reducing our overall spend." DL+ and the EAP marketplace are framed as remote-work fixes during COVID.
2. **2020–2021: build or buy alt data and quant tooling.** Second Measure is acquired. EAP reaches 60+ vendors. BQuant Enterprise launches. McManus's argument is democratisation: "the high cost of entry has put the majority of firms at a disadvantage".
3. **2022–2023: the client's cloud becomes the venue.** Google Cloud: "Bloomberg is the only financial data provider to enable cloud-native access to tick-for-tick data." Then Snowflake. Snowflake's own executive puts the distribution logic plainly: "Bloomberg is able to distribute its app to thousands of Snowflake customers, without these customers having to move or expose their data".
4. **2024–2025: quant 'readiness' products.** Point-in-time data, the VDR, OHLC bars and BSM on DL. Two surveys supply the demand story (evaluation takes ≥1 month for 65%). Angana Jacob: "Without historical point-in-time data, models can overestimate returns due to survivorship bias and look ahead bias."
5. **2026: data as context for agents and for chains.** MCP over DL+, Kaiko on Canton, Allium. McManus: "the bottleneck facing financial institutions has shifted from model capability to data readiness". In this framing, metadata is the product: "On its own, a last price doesn’t say what currency it’s in or what kind of price it is."

## 4. What the claims don't prove

1. **The counts drift, and they aren't date-matched.** DL fields: **30k** (Sony, Jan 2022), **15k** (Vancity, Apr 2023), **40k** (Snowflake, Jun 2023 and Jan/Dec 2024), **50k** (MCP, Sep 2026). Securities: **50m** (2022–23), then **70m** (2024), then **100m** (2026). A drop from 30k to 15k fields in 15 months is a boilerplate inconsistency, not shrinkage. Treat every count as marketing copy for that date (the DIGEST flags the same problem, credibility row).
2. **B-PIPE's instrument count is frozen.** It is **35m instruments** in 2019, 2022 and 2025, while exchanges go from **330+** to **350+**. Either coverage stopped growing or nobody updated the copy. Tick History quotes **70m+** instruments in 2024, so the definitions differ by product.
3. **Even the launch dates conflict.** EAP was "launched in 2018" (May 2020) but had its "introduction in February 2019" (Sep 2020). ALTD runs on "a mere seven-day lag" (story, 2023), BSM feeds on DL at "a 3-day lag" (2024), and un-entitled ALTD runs at 7–14 days (2026). These are three products at three resolutions, sold as one dataset.
4. **'Only' and 'first' claims are unverified.** ‘only financial data provider’ with cloud-native tick data (2022) and "one of the only" cloud real-time products (2019) come with no competitor named. That fits the corpus-wide pattern: Bloomberg names no competitor (DIGEST §0).
5. **Distribution reach is not uptake.** "thousands of Snowflake customers" is Snowflake's installed base, not Bloomberg's adoption. No release gives the number of DL+ Snowflake installs, B-PIPE cloud clients or MCP users. PORT Enterprise's 600+ is the only count.
6. **The surveys are self-serving.** Each is ~150 respondents from Bloomberg's own client workshops. The headline (54% have not started GenAI because of 'data readiness') is the answer that sells DL+ and MCP. The release itself hedges: the gap "is likely driven less by a lack of appetite".
7. **Tokenization is an intent, not a service.** Kaiko/Canton is an "initiative" that is "intended to focus initially" on UST and repo. It has a beta sign-up, no go-live and no named bank user. Allium is a Terminal dashboard of someone else's on-chain data.
8. **An open identifier doesn't prove open data.** "over 700 million FIGIs issued" counts issuance, not use. The corpus has no comparison with CUSIP or ISIN adoption, and crypto FIGIs tie to ISINs only "with appropriate licensing".

## 5. Strategic read (inference — not stated by Bloomberg)

- **Who owns the customer? Bloomberg still does, by design.** Every hyperscaler and marketplace release reads 'bring your own licence'. The Snowflake app provisions DL subscriptions the client already holds. MCP "validates a firm’s entitlements before returning data on any agent request, under standard Data License rights." Kaiko's text keeps "IP ownership, licensing compliance, and auditability". The cloud takes the hosting cost and the integration friction. Bloomberg keeps the price list, the contract and the usage audit. That is the opposite of a marketplace in which Snowflake or AWS owns checkout.
- **But the interface is leaking.** Each channel moves the client's daily attention from the Terminal to the client's own warehouse, notebook or agent. The ALTD story shows the tension: a client with many analysts "but only one of them has a Terminal subscription". Enterprise Data can grow while seats stagnate. LSEG shows the same split in its own numbers: Data & Feeds grows ~7% and Workflows ~3% (context, from [[lseg-workspace-data]]). Bloomberg's private books hide whether that is happening to it.
- **Peers made different bets on the channel.** S&P runs its own Marketplace and also sells through Snowflake/Xpressfeed and MCP servers inside Claude, Copilot, AWS and Google (context, from [[spglobal-ai-data-layer]]). ICE delivers fixed-income data over MCP, available in Claude, prices on data value (context, from [[ice-fixed-income-data]]). Aladdin went to Azure (2020) and Snowflake (2021) as an operating layer (context, from [[blackrock-aladdin-data]]). Bloomberg's MCP is **Bloomberg-hosted, client-agent-agnostic**, and names no LLM partner. It also leads the MCP Financial Services Interest Group, so it shapes the standard rather than buying a slot in someone's assistant. That is a stronger position on owning the customer and a weaker one on reach.
- **Give away the key, sell the lock.** FIGI is free ("available free of charge with no material impediments on use") and has been standardised three times (OMG 2014, ABNT 2020, X9 2021). Crypto FIGIs (2021) arrived before Bloomberg offered any crypto data products. S&P later made its CIQ ID free on DUNL (context, from [[spglobal-ai-data-layer]]): same move. The identifier lowers the cost of joining everything else to Bloomberg's data.
- **Regulation is the steadiest demand driver.** Sanctions (10 jurisdictions), SFDR (16k companies), HQLA (12 jurisdictions), NAIC, EMIR/MiFID reporting via RHUB and Basel crypto groups all turn rule changes into fields that must be bought and refreshed. The NAIC piece says it outright: "This can largely be characterized as a data problem". This business is low-glamour and high-retention.
- **Alt data shows buy versus partner.** Bloomberg *bought* the one dataset it calls "the most in-demand type" (card spend, Second Measure) and *partnered* for the rest: foot traffic (Placer.ai), web traffic (Similarweb) and 60+ EAP vendors. Then it *versioned* the result: free ALTD at 7–14 days, entitled at 3–5 days, DL feeds at 3 days.
- **Tokenization as data-on-chain** fits the 'neutral layer' mission (DIGEST §5). Bloomberg doesn't run a chain or issue tokens. It licenses the security master and evaluated price onto whichever chain wins, with entitlements intact. Peers bet the other way, on owned rails (see [[jpmc-kinexys-deposit-tokens]], [[blackrock-digital-assets]]).

## 6. Canon lenses

- **Information goods** ([[canon-shapiro-varian-information-rules]]): one dataset versioned by latency (ALTD 7–14 vs 3–5 days), by delivery (Terminal, SAPI, B-PIPE, DL, DL+) and by readiness (raw, linked, point-in-time, MCP metadata). Free FIGI is the classic complement to a priced good.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): AWS, Google, Snowflake and Kaiko are complementors who could also become rivals for the customer relationship. The entitlement check is how Bloomberg keeps the value-net position.
- **Platforms** ([[canon-cusumano-business-of-platforms]], [[canon-hagiu-wright-multi-sided-platforms]]): EAP's 60 vendors make Bloomberg a two-sided marketplace. The Snowflake app makes Bloomberg a complementor on someone else's platform. The firm runs both postures at once.
- **Powers** ([[canon-helmer-7-powers]]): switching costs (point-in-time history and linked IDs can't be rebuilt cheaply), cornered resource (Second Measure panel, BVAL) and process power (the 'readiness' metadata).
- **Disruption** ([[canon-christensen-innovators-dilemma]]): warehouse-native and agent-native delivery are the low-end path by which cheaper data reaches 'good enough'. Bloomberg's answer is to sustain from above with metadata, not to cut price.
- **Noise and measurement** ([[canon-kahneman-sibony-sunstein-noise]]): field and securities counts that move ±50% between releases are noise. Score them by date, not by headline.

## 7. Practitioner counterpoint

- **For Bloomberg:** the cloud moves are early and real. B-PIPE was on AWS in 2019, three years before the Google deal, and a bank client (Sony Bank) runs trading and risk fully in the cloud. Point-in-time data and VDR address real quant pain: 65% of survey respondents need a month or more to evaluate one dataset. Client quotes from M&G ("robust trade screening process"), Morgan Stanley (Basel look-through) and MUFG AM ("allows us to drive innovation faster and more efficiently than building these systems ourselves") describe workflows, not just praise.
- **Against:** the moat claims rest on self-reported counts that don't reconcile. Every channel is a cost-saving story told by the buyer (Balyasny: "reducing our overall spend"), which also means pricing pressure. And the cloud marketplaces that host Bloomberg today host LSEG, S&P and FactSet next door, which lowers the cost of a side-by-side test. VDR exists because rivals are one notebook away.
- **Both:** a data buyer should test Bloomberg's counts against their own entitlement (fields actually delivered, securities with non-null values) and run the VDR evaluation against a second vendor in the same Snowflake account. Treat 'readiness' as a hypothesis: measure how much reconciliation it actually removes.

## 8. Open questions to track

1. **Channel economics.** Does Bloomberg ever list a priced (not bring-your-own-licence) product on Snowflake, AWS or Azure Marketplace? That would be the signal that the marketplace owns checkout.
2. **MCP partners.** Will Enterprise MCP name an LLM or assistant channel (Claude, Copilot, Gemini), as S&P and ICE already have? Will the planned real-time extension carry B-PIPE entitlements?
3. **Kaiko/Canton go-live.** Is there a first on-chain repo or collateral workflow using Bloomberg evaluated pricing, and with which banks?
4. **Count reconciliation.** Does a single, dated catalogue count (securities, fields, instruments) appear, or does the 15k/30k/40k/50k drift continue?
5. **Seats vs feeds.** Any sign (Terminal user counts, BI commentary) that enterprise delivery is cannibalising Terminal seats?
6. **FIGI vs CUSIP.** Does any regulator mandate FIGI? Note that the US Financial Data Transparency Act joint data standard was contested (context, not from Bloomberg; verify before use).
7. **Regulatory pipeline.** Basel crypto rules, NAIC and SEC Treasury clearing: which becomes the next DL field set?

**Links:** [[bloomberg-hub]] · [[bloomberg-ai-strategy]] (MCP, ASKB, readiness) · [[bloomberg-pricing-bval-ibval]] (the evaluated prices that DL and Kaiko distribute) · [[bloomberg-buyside-stack]] (PORT, BTCA, AIM as data consumers) · [[bloomberg-private-markets]] (DLEN, Canoe as data feeds) · [[bloomberg-people]] (McManus, Lai, Doherty, Jacob) · [[bloomberg-mission-forces]] · [[bloomberg-outside-voices]] · [[bloomberg-terminal-instrumentation]] · [[lseg-workspace-data]] · [[spglobal-ai-data-layer]] · [[spglobal-pricing-fixed-income]] · [[ice-fixed-income-data]] · [[blackrock-aladdin-data]] · [[tradeweb-tech-ai-data]] · [[jpmc-kinexys-deposit-tokens]] · [[blackrock-digital-assets]] · [[wss-ai-economics]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-cusumano-business-of-platforms]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-helmer-7-powers]] · [[canon-christensen-innovators-dilemma]] · [[canon-kahneman-sibony-sunstein-noise]]

---
### Rep
Three short computations with numbers from this note.

**(a) Catalogue growth, or copy growth?** DL securities: 50m (Snowflake release, Jun 2023) → 100m (MCP, Sep 2026). Compute the implied CAGR over 3.25 years. *(Answer: 2^(1/3.25) − 1 ≈ **23.8%** a year.)* Fields: 40k (Jun 2023) → 50k (Sep 2026). *(Answer: 1.25^(1/3.25) − 1 ≈ **7.1%** a year.)* Now redo the field CAGR from Vancity's 15k (Apr 2023): *(50/15)^(1/3.4) − 1 ≈ **42%** a year.)* In one paragraph, say which base you would defend in front of a data-procurement committee and why a three-fold spread in the answer means you should ask for the entitlement-level count.

**(b) What the VDR is worth.** Bloomberg says a data evaluation takes up to **90 days**, more than half of it admin. The 2025 survey says 72% of teams can run **≤3** evaluations at a time. Take a team running 3 parallel evaluations of 90 days, so 12 a year. If VDR removes the admin half (90 → 45 days), how many can the team run? *(Answer: 3 × 365/45 ≈ **24** a year, double.)* Assume each evaluation ties up one quant at $300k a year fully loaded (assumption, not from Bloomberg) for its duration. What is the saving per evaluation? *(Answer: 45/365 × $300k ≈ **$37k**.)* Then ask the strategic question: who benefits more from faster evaluation, the incumbent or the challenger whose data the client is also testing?

**(c) Alt-data lag as a product tier.** A quarter is ~91 days, and the company reports ~30 days after quarter end. Un-entitled ALTD runs at **7–14 days** lag; entitled at **3–5 days**. On report day, what share of the quarter's data has each tier already shown, and how many days of 'post-quarter' lead does each give? *(Answer: both cover 100% of the quarter by report day. The difference is how soon after quarter end the full quarter is visible: day 14 vs day 5, so **16 vs 25 days** of lead before the print.)* Price the tier: if Lai's average fund spends "as much as $1 million" a year on alt data, what premium for 9 extra days of lead would you accept? Defend the number with a hit-rate assumption.

---
**Sources (Bloomberg corpus, `_ingest/raw/bloomberg/articles.jsonl`, read 2026-10-25):**
- [RegTek.Solutions acquisition, 2019-08-13](https://www.bloomberg.com/company/press/bloomberg-acquires-regtek-solutions/)
- [B-PIPE on AWS, 2019-09-12](https://www.bloomberg.com/company/press/bloomberg-launches-real-time-data-in-the-cloud-for-global-clients/)
- [Data License Plus, 2020-05-06](https://www.bloomberg.com/company/press/bloomberg-launches-new-data-management-solution-to-increase-operational-efficiency-for-clients/)
- [EAP marketplace, 2020-05-13](https://www.bloomberg.com/company/press/bloomberg-simplifies-data-discovery-access-and-integration/)
- [ABNT FIGI standard, 2020-07-06](https://www.bloomberg.com/company/press/abnt-launches-standard-on-financial-instrument-global-identifier/)
- [EAP alt data 60+ vendors, 2020-09-16](https://www.bloomberg.com/company/press/bloomberg-expands-alternative-data-offering/)
- [Second Measure completed, 2020-12-24](https://www.bloomberg.com/company/press/second-measure/)
- [ASC X9 FIGI, 2021-09-15](https://www.bloomberg.com/company/press/asc-x9-publishes-u-s-standard-for-the-financial-instrument-global-identifier/)
- [BQuant Enterprise, 2021-09-29](https://www.bloomberg.com/company/press/bloombergs-bquant-enterprise-accelerates-financial-services-firms-time-to-market-for-generating-quantitative-investment-strategies/)
- [Crypto FIGIs with Kaiko, 2021-10-14](https://www.bloomberg.com/company/press/bloomberg-and-kaiko-issue-first-financial-instrument-global-identifiers-for-crypto-assets/)
- [Server API, 2021-11-04](https://www.bloomberg.com/professional/insights/data/bloombergs-server-api-what-you-need-to-know/)
- [Sony Bank on AWS, 2022-01-20](https://www.bloomberg.com/company/press/sony-bank-to-differentiate-its-business-by-adopting-bloombergs-value-added-data-and-cutting-edge-delivery-technology-for-fully-cloud-based-computing/)
- [B-PIPE on Google Cloud, 2022-03-10](https://www.bloomberg.com/company/press/bloomberg-empowers-event-driven-decision-making-with-real-time-data-access-on-google-cloud/)
- [LEI CDF 3.1, 2022-04-27](https://www.bloomberg.com/company/press/bloomberg-releases-new-common-data-format-3-1-dataset-for-legal-entity-identifiers/)
- [M&G sanctions data, 2022-07-13](https://www.bloomberg.com/company/press/mg-investments-selects-bloomberg-enterprise-data-as-sanctions-data-provider/)
- [ArcticDB with Man Group, 2023-02-27](https://www.bloomberg.com/company/press/man-group-brings-powerful-dataframe-database-product-arcticdb-to-market-with-bloomberg/)
- [Vancity, 2023-04-11](https://www.bloomberg.com/company/press/vancity-investment-management-selects-bloomberg-to-streamline-portfolio-management/)
- [Funds Data Solution, 2023-06-06](https://www.bloomberg.com/company/press/bloomberg-launches-funds-data-solution-enhancing-insights-and-connectivity-across-the-investment-lifecycle/)
- [DL+ Snowflake Native App, 2023-06-28](https://www.bloomberg.com/company/press/bloomberg-simplifies-data-management-with-new-snowflake-native-app-in-the-data-cloud/)
- [ALTD launch, 2023-09-07](https://www.bloomberg.com/company/press/bloomberg-makes-alternative-data-accessible-alongside-traditional-financial-data/)
- [Building ALTD (story), 2023-09-07](https://www.bloomberg.com/company/stories/what-took-build-altd-bloomberg-terminal-alternative-data-function/)
- [BTCA Data Access, 2024-01-10](https://www.bloomberg.com/company/press/bloomberg-launches-data-enrichment-tool-to-enhance-transaction-cost-analysis/)
- [Point-in-Time company data, 2024-04-09](https://www.bloomberg.com/company/press/bloomberg-launches-point-in-time-data-solution-that-gives-quants-a-competitive-edge/)
- [BSM on Data License, 2024-05-22](https://www.bloomberg.com/company/press/bloomberg-makes-proprietary-alternative-data-available-alongside-traditional-enterprise-content/)
- [BSM Consumer Spend Index, 2024-09-09](https://www.bloomberg.com/company/press/bloomberg-launches-bloomberg-second-measure-u-s-consumer-spend-index/)
- [Virtual Data Room, 2024-09-17](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-launches-virtual-data-room-to-seamlessly-evaluate-its-extensive-catalog-of-data-for-faster-decision-making/)
- [OHLC bars / Tick History, 2024-10-01](https://www.bloomberg.com/company/press/bloomberg-launches-fully-customizable-intraday-quant-pricing-solution-for-investment-research/)
- [Baader SFDR, 2024-11-25](https://www.bloomberg.com/professional/insights/press-announcement/baader-bank-selects-bloombergs-comprehensive-esg-data-for-sfdr-reporting/)
- [PORT to Snowflake via DL+, 2024-12-04](https://www.prnewswire.com/news-releases/bloomberg-announces-port-enterprise-data-delivery-to-snowflake-with-data-license-plus-dl-302321571.html)
- [Research data survey, 2025-01-14](https://www.bloomberg.com/company/press/coverage-timeliness-and-quality-of-data-the-key-challenge-for-quants-research-analysts-and-data-scientists-according-to-bloomberg-research-survey/)
- [NAIC classification, 2025-01-28](https://www.bloomberg.com/professional/insights/financial-services/naic-principles-based-bond-classification-a-data-driven-approach/)
- [Vietnam Maritime Bank B-PIPE, 2025-02-06](https://www.bloomberg.com/company/press/vietnam-maritime-commercial-joint-stock-bank-adopts-bloomberg-bpipe-to-optimize-its-fx-pricing-engines-and-digital-transformation/)
- [Similarweb in ALTD, 2025-06-04](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-expands-alternative-data-offering-with-web-traffic-data-from-similarweb/)
- [MUFG AM BQuant, 2025-09-07](https://www.bloomberg.com/company/press/mitsubishi-ufj-asset-management-powers-digital-transformation-of-its-investment-workflows-with-bloombergs-bquant-enterprise/)
- [HQLA Middle East, 2025-09-16](https://www.bloomberg.com/company/press/fintech-gate-bloomberg-expands-hqla-solution-to-middle-east/)
- [Code Crunch London, 2025-12-04](https://www.bloomberg.com/company/press/bquant-code-crunch-hackathon-in-london-showcases-cutting-edge-quant-finance-innovation/)
- [Quant AI survey, 2026-01-22](https://www.prnewswire.com/news-releases/quants-increase-focus-on-sector-specific-data-as-ai-adoption-evolves-bloomberg-research-data-survey-finds-302667587.html)
- [Alt-data entitlements, 2026-01-28](https://www.prnewswire.com/news-releases/bloomberg-introduces-alternative-data-entitlements-on-the-terminal-for-increased-alpha-discovery-302672684.html)
- [Kaiko / Canton on-chain data, 2026-02-26](https://www.prnewswire.com/news-releases/bloomberg-and-kaiko-collaborate-on-initiative-to-develop-on-chain-data-access-for-tokenized-markets-302698044.html)
- [Point-in-time economic data, 2026-05-07](https://www.prnewswire.com/news-releases/bloomberg-introduces-point-in-time-economic-data-to-power-quantitative-research-and-strategy-development-302765281.html)
- [CLO reference data, 2026-09-23](https://www.prnewswire.com/news-releases/bloomberg-launches-comprehensive-clo-reference-data-solution-connecting-insights-across-the-investment-lifecycle-302886975.html)
- [Enterprise MCP, 2026-09-29](https://www.bloomberg.com/company/press/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications/)
- [Allium stablecoin dashboard, 2026-09-30](https://www.bloomberg.com/company/press/bloomberg-launches-stablecoin-dashboard-on-the-terminal-powered-by-data-from-allium/)
- [Basel crypto classification, 2026-10-22](https://www.prnewswire.com/news-releases/bloomberg-enables-scalable-crypto-asset-exposure-classification-under-basel-framework-302916012.html)
