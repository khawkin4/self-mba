# Note · S&P Global AI & the data layer — betting it can be the trusted data *inside* everyone else's AI tools instead of owning the screen

> Practitioner / strategy note · Maps to **E10** (Digital & AI Transformation — build vs partner vs distribute), **Course 04** (Competitive Strategy — platform power, disintermediation, coopetition), **Course 07** (Data, Analytics & Decision-Making — "AI-ready" data, verifiability, metric claims) · Written 2026-10-25 · Part of [[spglobal-hub]]; companions [[spglobal-pricing-fixed-income]], [[spglobal-people]], [[tradeweb-tech-ai-data]]

- **Source:** the S&P Global corpus at `_ingest/raw/spglobal/articles.jsonl`. That covers about 60 AI-related press and IR releases from May 2020 to Oct 22 2026, the annual-report letters for 2019 to 2025, and the Investor Day 2025 deck. Everything here is S&P's own material or partner quotes S&P chose to print. There are no earnings-call transcripts, no analyst views and no usage or revenue figures for AI products beyond a few user counts.
- **Core claim:** S&P bought Kensho in 2018. In the 2019–2020 earnings releases it shows up as a **margin drag and a retention cost**. It then became a product workshop: Scribe, NERD, Classify, ChatIQ and AI Benchmarks. From **Nov 2024** it became a **distribution pipe**:
  - Kensho LLM-ready API (Nov 2024).
  - MCP server into **Claude** (Jul 2025).
  - Microsoft Copilot, AWS, Google Cloud, IBM, Salesforce and Cohere followed.
  - Two retrieval modes were packaged as the **S&P Global AI Data Portal** (Jul 2026).

  In **July 2026** S&P reorganised Market Intelligence around it: half the division is now called **Kensho Data & Platforms**.

  The bet is that the value sits in licensed, cited data, not in the interface. S&P says it has invested over $1 billion. The risk is the mirror image of the bet: once the analyst works inside Claude or Copilot, S&P's terminal (Capital IQ Pro) is no longer where the customer relationship lives. What S&P earns then depends on how strong its licence is.

---

## 1. Chronology

| Date | Event | What S&P says or shows |
|---|---|---|
| Apr 2018 | **Kensho acquired** (date per later releases; price not in corpus) | — |
| 2019-05-02 | Q1 2019: operating margin down 40bp "primarily due our investment in artificial intelligence and analytics through the acquisition of Kensho" | AI first appears as a cost |
| 2019 AR | Peterson: "Kensho, the AI business we acquired in 2018, has become a catalyst for innovation and change" | *Kensho retention related expense* of **$31M (2018), $21M (2019), $11M (2020), $2M (2021)** is adjusted out of results |
| 2020-05-14 | **Kensho Scribe** (speech-to-text) trained on NVIDIA NeMo | MI has transcribed "more than 100,000 hours of earnings calls". Coverage is up "by more than 25%" |
| 2020-05-27 | S&P Global **Marketplace** launched with Kensho tools | Discovery layer for datasets |
| 2021 | Kensho NERD on Marketplace; Platts "Faster Price Assessments: powered by Kensho AI"; AI Document Viewer on Capital IQ Pro | AI goes inside existing products |
| 2023-03-02 | **Kensho Classify** (NLP) | Pre-LLM product, sold through Marketplace |
| Late 2023 | Kensho CEO **Bhavesh Dayalji** also becomes **Chief AI Officer**. CIO Swamy Kocherlakota becomes Chief Digital Solutions Officer and sponsors AI. An **AI Accelerator** is set up. ChatIQ is piloted | Governance formalised (AR23) |
| 2024-02-06 | Generative AI search on Marketplace | First LLM product launch |
| 2024-04-03 | **S&P AI Benchmarks by Kensho** (beta): a public leaderboard scoring LLMs on finance and quant reasoning | S&P grades the models as well as feeding them |
| Apr 2024 | LLM-ready API in private beta with "a select group of customers" | — |
| 2024-11-12 | **ChatIQ** and **Document Intelligence** launched in Capital IQ Pro | AI inside the terminal |
| **2024-11-13** | **Kensho LLM-ready API** in open beta for "GPT, Gemini, or Claude" | **The pivot**: S&P's data goes into *other companies'* models |
| 2025-01-06 / 06-09 | ProntoNLP and TeraHelix acquired (terms undisclosed) | Small AI tuck-ins |
| 2025-04-21 | Commodity Insights AI agent in **Microsoft 365 Copilot** | — |
| **2025-07-15** | **Anthropic**: a Kensho MCP server puts Capital IQ Financials and transcripts into **Claude** | First named frontier-LLM channel |
| 2025-10-08 / 10-14 | **IBM** watsonx Orchestrate agents; Document Intelligence on **Salesforce** AgentExchange | Trials are free; "full access available with a S&P Global Market Intelligence license" |
| 2025-11-13 | Investor Day lists AI partners: Anthropic, Google, IBM, Microsoft, Rogo, Salesforce, plus an NVIDIA R&D partnership. Data estate "350PB+". The safe-harbour statement lists generative AI among competitive risks | Strategy and risk stated side by side |
| 2025-12-01 / 12-10 | **AWS** (two MCP servers in Quick Suite); **Google Cloud** (data unified on BigQuery; agents on Gemini Enterprise) | Every hyperscaler now covered |
| 2026-03-15 (AR25) | Cheung: "over $1 billion invested in AI"; Fortune AIQ 50 rank #12 | — |
| 2026-06-08 | **Cohere** (North, a sovereign/on-premise platform) | Channel for regulated users |
| **2026-07-06** | **MI operating model** reorganised. **Kensho Data & Platforms** (co-head Sally Moore) contains *Kensho Data*, now "the client-facing data product and AI delivery layer", and *Platforms* (Capital IQ, RatingsDirect, Visible Alpha, With Intelligence). Dayalji becomes "Head of Kensho Data & Intelligence" | AI becomes the organising principle of MI |
| 2026-07-21 | **Adaptive Retrieval** launched. Together with Deterministic Retrieval (the LLM-ready API) it forms the **S&P Global AI Data Portal** | S&P says it is "the first to offer customers two complementary ways to retrieve data" |
| 2026-07-23 | **Farsight** partnership plus a minority stake (AI-generated pitch books and CIMs inside Capital IQ Pro) | The partner's CEO says data access is no longer the battleground (§5) |
| 2026-08-12 | Microsoft expansion: Copilot in Excel connector and a Copilot Cowork plugin | — |
| 2026-09-28 / 10-15 | Ratings data (RatingsXpress, "nearly 1 million" ratings) and Visible Alpha consensus added to the AI Data Portal | Even Ratings content flows out through MCP |
| 2026-10-22 | iLEVEL MCP server into Copilot and Claude; native iLEVEL Agent | Private-markets data too |

## 2. The strategy in S&P's own words

- **Distribute to every model.** Dayalji, Nov 2024: "we want to make our data more easily and immediately accessible to the entire LLM ecosystem," and the goal is "to be the go-to partner for customers looking to capitalize on their investments in AI."
- **Meet the user where they already work.** Dayalji, Jul 2025: "S&P Global is committed to meeting our customers where their workflows take place,". Moore, Aug 2026: "We are meeting clients where they work, embedding S&P Global's trusted, high-quality data directly into their workflows".
- **Verifiability is the product.** The Jul 2026 release says "AI agents and LLMs need data that is properly cited, verifiable, and auditable." Back in Nov 2024 the API already returned "the function calls or generated code as an audit trail."
- **AI raises the value of proprietary data.** Cheung, AR25: "As AI increasingly permeates every sector, customers are placing an even higher value on S&P Global's proprietary benchmarks, data, and tools". She adds that these "comprise over 95 percent of our revenue".
- **Retrieval is only the first step.** Dayalji, Jul 2026: "For S&P Global, the data retrieval layer is only the beginning."
- **The reorganisation is about margins.** Cheung, Jul 2026: "These changes within Market Intelligence align our capabilities, enabling us to elevate the customer experience while growing our revenue and improving margins."

## 3. Usage and investment numbers (all S&P-stated)

| Metric | Value | Source |
|---|---|---|
| Cumulative AI investment | "over $1 billion" including Kensho | AR25 CEO letter |
| Capital IQ Pro GenAI users | "more than 60,000 users" a few months after launch | AR24 |
| Internal copilot (Spark Assist) | "Approximately 29,000 of our people" in year one; 1,300 prompts | AR24 |
| Data estate | "350PB+"; 535 unique datasets; "10M+" monthly data units processed via AI | Investor Day 2025 |
| Transcription | 100,000+ hours (2020) → "1 million+ Hours transcribed" | 2020-05-14; Investor Day 2025 |
| Ratings via the AI portal | "nearly 1 million issuer and security-level credit ratings" | 2026-09-28 |

None of these are revenue figures. S&P does not disclose AI revenue, the price of the LLM-ready API, or how much of Capital IQ Pro usage now runs through third-party AI tools.

## 4. What the claims don't prove

1. **There is no revenue line.** "Over $1 billion invested" is an input. "60,000 users" may count anyone who clicked once. No release says whether AI products grow revenue or only defend renewals. The 2026 reorganisation release talks about margins, not AI revenue.
2. **"First" and "only" claims are self-certified.** "The first to offer customers two complementary ways to retrieve data" is S&P's own ranking. Bloomberg, LSEG and FactSet are never named, so the claim is not tested against anyone.
3. **The timeline drifts.** The Jul 2026 release says the LLM-ready API "has been available to customers since 2025". The Nov 2024 release says it was in open beta then and in private beta "since April 2024". This is minor, but it shows how marketing dates move.
4. **"Verifiable" is asserted, not audited.** The AI Benchmarks leaderboard is S&P grading other companies' models. Nothing in the corpus shows an independent accuracy test of S&P's own retrieval answers.
5. **The governance is still changing.** The Chief AI Officer title appears in releases up to Jun 2026. From Jul 2026 Dayalji is "Head of Kensho Data & Intelligence", and a new Chief Technology & Transformation Officer (Bhathena, Apr 2026) now owns the Enterprise Data Organization. Who owns AI strategy at group level is unclear from outside. See [[spglobal-people]].
6. **The risk factor contradicts the letter's tone.** The Investor Day 2025 safe harbour lists "competitive products (including those incorporating generative artificial intelligence". The CEO letter speaks of "more tailwinds than headwinds". Both can be true, but only the letter is promotional.

## 5. Strategic read (inference — not stated by S&P Global)

- **This is a deliberate trade of interface for reach.** S&P's growth engine (MI, about $4.8B of subscription revenue TTM Sep 2025 per Investor Day 2025) sold *seats* on Capital IQ Pro plus *feeds* (Xpressfeed, Snowflake). The AI channel moves value from seats to feeds. That is fine for the licence fee. It is risky for seat counts if analysts stop opening the terminal.
- **The moat argument rests on licensing, not technology.** MCP servers and retrieval layers are easy to copy. What is hard to copy is legally licensed, entity-linked data: CIQ IDs, Compustat history, transcripts, ratings. Note that S&P made the **CIQ ID free on DUNL.org** in Sep 2025 ([[spglobal-pricing-fixed-income]]). It gives the key away so that the data it locks is easy to join to.
- **Farsight's CEO names the threat.** In S&P's own release (2026-07-23) they say: "The industry has spent years competing on access to data. The next frontier is helping firms turn that data into client-ready work". If they are right, data becomes a supplier input to whoever owns the workflow. S&P's answer is to buy into the workflow (a minority stake, Platforms under Kensho), not to fight it.
- **The model companies have more channels than S&P does.** Anthropic, Microsoft, Google, AWS, Salesforce and Cohere each get S&P data as one of many sources. S&P is one of several premium suppliers to each. This is coopetition where the platform owner sets the terms of the shelf.
- **Contrast with Tradeweb.** Tradeweb's AI ([[tradeweb-tech-ai-data]], [[tradeweb-ai-price]]) is built from its **own flow**: every automated RFQ is a labelled training record. S&P's AI is built on **content it already owns or licenses**, delivered to someone else's model. Tradeweb's AI makes its venue stickier. S&P's AI makes its data more portable. The two are opposite bets on where value sits.
- **Ratings is now in the pipe too.** RatingsXpress through MCP to "GPT, Gemini and Claude" puts a regulated opinion product into generic chat tools. That raises a firewall question S&P keeps answering with disclaimers, which matters for [[spglobal-digital-assets]] and Ratings governance.

## 6. Canon lenses

- **Platforms and who owns the customer** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]], [[canon-cusumano-business-of-platforms]]): the LLM front ends are becoming the multi-sided platform. S&P has chosen to be a high-quality supplier on several platforms rather than to defend its own.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Microsoft, Google and AWS are S&P's distributors, its cloud vendors and, potentially, future data rivals. Value creation is shared; value capture depends on who is harder to replace.
- **Information goods and lock-in** ([[canon-shapiro-varian-information-rules]]): give away the identifier, version the data (Deterministic vs Adaptive), and charge for the licence. The free CIQ ID is classic Shapiro–Varian.
- **Power** ([[canon-helmer-7-powers]]): the claimed powers are *cornered resource* (proprietary data) and *switching costs* (entity linking, history). Neither depends on owning the interface. Whether it is *counter-positioning* against Bloomberg's closed terminal is worth testing.
- **Disruption** ([[canon-christensen-innovators-dilemma]]): AI copilots look like a "good enough" low-end interface. By feeding them S&P avoids being disrupted on data. It may still be disrupted on the terminal.

## 7. Practitioner counterpoint

- **For S&P:** buy-side and bank users really do want S&P data inside the tools they already use. The LLM-ready API returns structured, cited answers. That is better than an LLM guessing a number from the web, and it is the feature banks' model-risk teams ask for. Being in every model at once is cheaper than building a competing chat front end.
- **Against:** a desk using Claude or Copilot to blend S&P with Bloomberg, LSEG and internal data no longer *feels* the difference between vendors. Renewal negotiations then become a price-per-dataset discussion. The 2026 reorganisation's talk of "improving margins" in MI, the lowest-margin division (adjusted ~31–35% in 2021–23 per earnings releases), suggests the economics are not yet obvious.
- **Both:** the test is in the 10-K, not the press releases. Watch MI subscription growth, the seat vs enterprise-licence mix, and whether S&P ever splits out AI-channel revenue.

## 8. Open questions to track

1. **Pricing:** is the AI Data Portal charged per seat, per call, or as part of an enterprise licence? Does the Chief Client Office's enterprise deal (Barclays, 2025) bundle it?
2. **Usage:** what share of Capital IQ data is now consumed through MCP or third-party AI rather than the terminal?
3. **Governance:** who owns AI strategy at group level after the Chief AI Officer title disappeared in Jul 2026: Bhathena (CTTO), Moore (Kensho Data & Platforms) or Dayalji?
4. **Accuracy:** will S&P publish its own retrieval accuracy on its AI Benchmarks leaderboard?
5. **Ratings firewall:** do regulators (SEC, ESMA) say anything about ratings data being delivered through generic LLM tools?
6. **Competitors:** how do Bloomberg ([[bloomberg-hub]]) and LSEG ([[lseg-hub]]) answer? Do they also put data inside Claude and Copilot, or defend the terminal?

**Links:** [[spglobal-hub]] · [[spglobal-pricing-fixed-income]] (the free CIQ ID and the data being distributed) · [[spglobal-people]] (Dayalji, Moore, Bhathena) · [[spglobal-mission-forces]] · [[spglobal-outside-voices]] (Farsight, Microsoft, Google) · [[spglobal-digital-assets]] · [[tradeweb-tech-ai-data]] (the opposite AI bet) · [[tradeweb-ai-price]] · [[bloomberg-hub]] · [[lseg-hub]] · [[wss-ai-economics]] · [[bloomberg-terminal-instrumentation]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-parker-platform-revolution]] · [[canon-cusumano-business-of-platforms]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
Three short computations. Where an input is not disclosed, the assumption is labelled.

**(a) The cost of Kensho, as reported.** Add up the Kensho retention expense S&P adjusted out of results: $31M (2018) + $21M (2019) + $11M (2020) + $2M (2021). Then compare the total with the "over $1 billion invested in AI" (2018–2025). *(Answer: **$65M**, about 6.5% of the $1B. Spread over the eight years 2018–2025, the $1B is about **$125M a year**. In one paragraph: why might a company adjust retention pay out of "adjusted" earnings, and what does that hide about the true cost of buying talent?)*

**(b) Seats vs feeds.** *Assume* (not disclosed) that 40% of MI's ~$4.8B subscription revenue is desktop seats priced at ~$25,000 a year. That is about **77,000 seats**. If AI tools let a client cut seats by 20% and S&P recovers only half of that lost revenue through a data licence for the AI channel, what is the net revenue change? *(Answer: seats revenue $1.92B × 20% = $384M lost; half recovered = $192M; net **−$192M**, about −4% of the $4.8B. Then redo it with 80% recovery and say what licence terms S&P would need to get there.)*

**(c) Reading "60,000 users".** Capital IQ Pro GenAI had "more than 60,000 users" a few months after launch. If the user base were ~77,000 seats (from b), what adoption rate does that imply? *(Answer: **~78%**.)* List two reasons that number overstates real usage and one metric you would ask for instead, such as weekly active users or queries per user.

---
**Sources (S&P Global press/IR; corpus `_ingest/raw/spglobal/articles.jsonl`, accessed 2026-10-25):**
- [Q1 2019 results (Kensho margin), 2019-05-02](https://investor.spglobal.com/news-releases/news-details/2019/SP-Global-Reports-First-Quarter-Results-2019-5-2/default.aspx)
- [2019 Annual Report letter, 2020](https://s29.q4cdn.com/690959130/files/doc_financials/2019/ar/2019-Annual.pdf)
- [Kensho Scribe / NVIDIA, 2020-05-14](https://press.spglobal.com/2020-05-14-Kensho-Collaborates-with-NVIDIA-to-Advance-Automatic-Speech-Recognition)
- [Kensho Classify, 2023-03-02](https://press.spglobal.com/2023-03-02-Kensho-Technologies-Launches-a-Natural-Language-Processing-Solution-that-Conceptually-Understands-and-Classifies-Documents)
- [2023 CEO letter (Chief AI Officer, AI Accelerator), 2024](https://www.spglobal.com/en/annual-reports/2023/ceo-letter)
- [Marketplace GenAI search, 2024-02-06](https://press.spglobal.com/2024-02-06-S-P-Global-Launches-Generative-AI-Search-on-the-S-P-Global-Marketplace)
- [S&P AI Benchmarks by Kensho, 2024-04-03](https://press.spglobal.com/2024-04-03-S-P-Global-Redefines-Financial-AI-Benchmarking-with-S-P-AI-Benchmarks-by-Kensho-Beta)
- [ChatIQ / Document Intelligence, 2024-11-12](https://press.spglobal.com/2024-11-12-S-P-Global-Transforms-S-P-Capital-IQ-Pro-Experience-with-the-Launch-of-New-Generative-AI-Powered-Capabilities)
- [Kensho LLM-ready API, 2024-11-13](https://press.spglobal.com/2024-11-13-S-P-Global-Launches-Kensho-LLM-ready-API-beta-,-Making-its-Structured-Data-Accessible-for-Generative-AI)
- [2024 Annual Report letters (60,000 users, Spark Assist), 2025](https://s29.q4cdn.com/690959130/files/doc_financials/2024/ar/S-P-Global-2024-Annual-Report.pdf)
- [ProntoNLP, 2025-01-06](https://investor.spglobal.com/news-releases/news-details/2025/SP-Global-Acquires-ProntoNLP-Expanding-its-Generative-AI-Powered-Product-Portfolio/default.aspx)
- [Microsoft 365 Copilot (commodities), 2025-04-21](https://press.spglobal.com/2025-04-21-S-P-Global-Launches-AI-Ready-Commodities-Data-Integrated-With-Microsoft-365-Copilot)
- [Anthropic / Claude, 2025-07-15](https://press.spglobal.com/2025-07-15-S-P-Global-and-Anthropic-Announce-Integration-of-S-P-Globals-Trusted-Financial-Data-into-Claude)
- [IBM watsonx, 2025-10-08](https://press.spglobal.com/2025-10-08-S-P-Global-and-IBM-Deploy-Agentic-AI-to-Improve-Enterprise-Operations)
- [Salesforce AgentExchange, 2025-10-14](https://press.spglobal.com/2025-10-14-S-P-Global-Launches-S-P-Capital-IQ-Pro-Document-Intelligence-on-Salesforces-AgentExchange,-Transforming-Document-Analysis-with-Generative-AI)
- [Investor Day 2025 slides, 2025-11-13](https://s29.q4cdn.com/690959130/files/doc_events/2025/SP-Global-Investor-Day-Slides-11-13-2025.pdf)
- [AWS MCP servers, 2025-12-01](https://press.spglobal.com/2025-12-01-S-P-Global-Collaborates-with-AWS-to-Bring-Trusted-Data-Directly-to-Customer-AI-Workflows)
- [Google Cloud, 2025-12-10](https://press.spglobal.com/2025-12-10-S-P-Global-Advances-AI-Powered-Enterprise-Transformation-Through-Strategic-Partnership-with-Google-Cloud)
- [2025 CEO letter ($1B, 95%), 2026](https://www.spglobal.com/en/annual-reports/2025/ceo-letter)
- [Cohere, 2026-06-08](https://press.spglobal.com/2026-06-08-S-P-Global-Expands-AI-Ecosystem-Reach-with-Cohere-to-Power-Trusted,-Agentic-Workflows-for-Financial-Institutions)
- [MI operating model, 2026-07-06](https://investor.spglobal.com/news-releases/news-details/2026/SP-Global-Evolves-Market-Intelligence-Operating-Model-to-Accelerate-Agentic-Solutions-Platform-Capabilities-and-Innovation-Announces-Executive-Leadership-Changes/default.aspx)
- [Adaptive Retrieval / AI Data Portal, 2026-07-21](https://press.spglobal.com/2026-07-21-S-P-Global-Launches-Adaptive-Retrieval,-Giving-Customers-a-New-Way-to-Access-Data-Across-AI-and-Agentic-Workflows)
- [Farsight, 2026-07-23](https://press.spglobal.com/2026-07-23-S-P-Global-Market-Intelligence-Partners-with-Farsight-to-Launch-AI-powered-Financial-Workflow-Capability-for-Capital-IQ-Pro)
- [Microsoft expansion, 2026-08-12](https://press.spglobal.com/2026-08-12-S-P-Global-Expands-Collaboration-with-Microsoft,-Brings-Breadth-of-Essential-Intelligence-to-Microsoft-365-Copilot)
- [RatingsXpress on AI Data Portal, 2026-09-28](https://press.spglobal.com/2026-09-28-S-P-Global-brings-Credit-Ratings-to-the-S-P-Global-AI-Data-Portal)
- [iLEVEL MCP, 2026-10-22](https://press.spglobal.com/2026-10-22-S-P-Global-Expands-AI-Powered-Capabilities-Across-Private-Markets)
