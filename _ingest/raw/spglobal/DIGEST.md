# S&P Global — corpus digest (2019-01-01 → 2026-10-25)

Stage: **read-first**. This file says what is in the corpus and what looks worth a note. It writes no notes. Lens: market structure (venues, data/pricing/indices, electronification, AI, tokenization, M&A), plus people, mission and headwinds/tailwinds.

Files in this folder:
- `index.tsv`: 1,707 rows (date, type, status, title, url). Every press/IR item found from 2019 onward, each marked `fetched` or `skipped: <reason>`.
- `articles.jsonl`: 492 full texts (date, type, topic, title, url, text). Boilerplate ("About S&P Global", forward-looking statements) is trimmed. Earnings releases are capped at 15k characters, so the financial tables are cut off.
- `DIGEST.md`: this file.

Quotes are verbatim and ≤25 words. Each carries a date and a source URL. Every quote in this file was checked by script against `articles.jsonl` (§10). The S&P pricing business is already covered in `notes/tradeweb-ai-price.md` §5, so this digest only adds to it and does not repeat it.

---

## 1. What the corpus is

**Sources**
| Source | How it was obtained | Items |
|---|---|---|
| press.spglobal.com (newsroom; all divisions) | curl works. Listing pages `index.php?s=2429&l=100&year=Y&category=C`, crawled year by year and per division category | 1,400 indexed (2019+) |
| investor.spglobal.com (Q4 IR site) | The HTML is behind Cloudflare. The public JSON feed `/feed/PressRelease.svc/GetPressReleaseList` (the page's own API key, `bodyType=2`) returns full bodies and works with curl | 291 indexed |
| Annual reports 2019–2022 and 2024 (PDF, q4cdn) | curl; only the chairman/CEO letter front section is kept | 5 |
| Annual reports 2023 and 2025 (web letters) | spglobal.com blocks curl, so these were read in the built-in browser with a same-origin fetch | 5 (CEO letter, chairman letter, 2023 overview) |
| Investor Day 2022, Investor Day 2025, Mobility Global Investor Day 2026, Special Meeting 2021 (merger vote), 2024 AGM slides, COVID letter 2020 | PDF via curl | 6 |

Press and IR items with the same title and year were de-duplicated, keeping the IR copy. 16 long-form documents were added on top.

**Counts by year** (index rows: fetched / skipped)
| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| fetched | 32 | 41 | 66 | 53 | 76 | 72 | 82 | 71 |
| skipped | 139 | 183 | 237 | 172 | 146 | 134 | 111 | 92 |

The fetched texts total about 2.4M characters. By type: 347 press releases, 129 IR releases, 6 investor-day/meeting decks, 10 annual-report letters or pages.

**What was skipped, and why** (1,214 rows; each reason is in `index.tsv`)
- 363 index rebalancing / *set to join S&P 500* notices.
- 89 Case-Shiller house-price releases.
- 3 PMI releases.
- 120 Ratings commentary: ESG Evaluation scores, alignment opinions, "report says" research, defaults.
- 118 Platts price-assessment launches, plus conference promos: Commodity Insights market commentary, out of scope per the brief.
- 119 market-statistics releases: buybacks, CUSIP volumes, multichannel TV, bank rankings, surveys.
- 101 earnings-date and conference notices; 53 dividend and senior-notes notices; 8 annual-meeting and fact-book notices.
- 63 award notices.
- 150 titles with no corporate or market-structure keyword. These were reviewed only as titles: Platts outlooks, Foundation grants, energy studies.

The title filter was tuned by hand after a first pass wrongly skipped the S&P 500 / Hyperliquid perpetuals licence and the GICS and MegaCap consultations. A few relevant items may still sit in the *off-lens* bucket, because those were judged on title alone.

**Gaps (important)**
1. **The 2023 Q2/Q3 and all 2024–2026 earnings releases in the IR feed are stubs.** They only link to a PDF, so the corpus has no quarterly segment numbers after Q1 2023. Annual figures come from the letters and investor-day decks. If you choose the financials note, pull the quarterly earnings PDFs from `investor.spglobal.com/quarterly-earnings`.
2. **No earnings-call transcripts.** The IR site doesn't host them. That means no analyst Q&A and therefore no sell-side skeptics.
3. **No third-party press** (Bloomberg, FT, Reuters): *outside voices* are only the people S&P chose to quote.
4. The 2019 annual-report letter text is cut off mid-tribute in the PDF extraction.
5. The 2025 annual-report PDF was blocked. The web CEO and chairman letters were used instead, and they appear to be the same text.

---

## 2. Chronology — the 36 events that matter

| Date | Event | Why it matters |
|---|---|---|
| 2019-01-28 | Ratings becomes the first wholly foreign-owned credit rating agency (CRA) cleared to rate China's domestic bond market | Ratings used as a way into a market. A CSRC exchange-market licence follows on 2020-10-26 |
| 2019-03-01 | S&P 500 and the DJIA become the first benchmarks endorsed into the EU under the Benchmark Regulation (BMR) | Regulation as a moat for index licensing |
| 2019-03-18 | SPIAS (advisory, $33B advised) sold to Goldman Sachs Asset Management | Exit from investment advice, which keeps the "independent benchmark" stance clean |
| 2019-11-21 | Agrees to buy RobecoSAM's ESG ratings business (SAM/CSA) | Start of the ESG build-out (§6) |
| 2020-04-08 | S&P DJI–IHS Markit index collaboration (S&P 500 + iBoxx + CDX + iTraxx) | The two companies' first visible tie-up, seven months before the merger |
| 2020-05 to 09 | Kensho Scribe on NVIDIA; S&P Global Marketplace; Snowflake distribution | The early *distribute data everywhere* pattern |
| 2020-09-30 | Dick Thornburgh named Non-Executive Chairman; Ian Livingston joins the board | The board that steered the merger and the CEO succession |
| **2020-11-30** | **All-stock merger with IHS Markit (IHS EV $44B)**; ~$480M cost synergies (later raised to $600M) and $350M revenue synergies | The defining deal: brings iBoxx, CDX/iTraxx, evaluated pricing, MarkitSERV, Ipreo, Mobility and OPIS |
| 2020-12-16 | Post-merger structure: Kansler (IHS) runs combined MI; Cheung runs Ratings plus ESG | The target's executive ran MI. Cheung's path to CEO begins |
| 2021-03-11 | ~99% of SPGI votes approve the merger | Regulators become the gating item |
| 2021-05-17 | S&P DJI pays a $9M SEC penalty over an undisclosed QA mechanism on a VIX-futures index (Feb 5 2018) | Benchmark-integrity enforcement |
| 2021-07-21 | Platts and ICE run a joint consultation on the Brent complex (WTI Midland added in 2022) | Benchmark administrator and futures venue co-govern the oil benchmark |
| 2021-10-22 / 11-12 / 12-27 | EC, DOJ and CMA remedies: **CUSIP Global Services → FactSet ($1.925B)**, **OPIS/CMM/PCW → News Corp (~$1.15B)**, Base Chemicals → News Corp ($295M), and a commitment to sell LCD | Regulators made S&P sell assets to rivals, including CUSIP, a near-monopoly asset of its own |
| **2022-02-28** | **Merger closes** (~$140B EV; six divisions); $12B accelerated share repurchase (ASR) | The modern SPGI |
| 2022-04-04 | LCD and leveraged-loan indices → Morningstar ($650M) | An EC condition |
| 2022-05-17 | Ratings sets up a DeFi group (Chief DeFi Officer Chuck Mounts) | The first digital-assets organisation inside S&P |
| 2022-06-01 | **2022 guidance suspended**; Ratings revenue hit of up to $600M | The merger closed into a collapse in debt issuance |
| 2022-12-01 | Investor Day: "Powering Global Markets", Vitality Index, 2025/26 targets | The post-merger strategic reset |
| 2023-01-17 → 05-02 | Engineering Solutions → KKR ($975M) | A merger asset sold within a year |
| 2023-02-08 | AWS named preferred cloud | Infrastructure choice |
| 2023-06-22 | Bloomberg TSOX linked to MI InvestorAccess (primary bond workflow) | Working with the main desktop rival |
| 2023-12-07 | CFO Ewout Steenbergen departs; ~1 year with an interim CFO (Craig) until Aboaf (Feb 2025) | Leadership gap during the CEO handover |
| 2023-12-12 | Ratings launches Stablecoin Stability Assessments (USDT scored 4) | Ratings brand applied to crypto, labelled "not a rating" |
| 2024-02-20 / 05-01 | Visible Alpha acquired; Fincentric (Markit Digital) and later PrimeOne sold | More pruning of IHS Markit assets |
| **2024-06-27** | **CEO succession announced: Martina Cheung succeeds Doug Peterson on 2024-11-01**; Yann Le Pallec to run Ratings | The central people event |
| 2024-10-17 | Cheung's leadership team: Saha → MI + Chief Enterprise Data Officer; Kansler out; Sustainable1 folded into Commodity Insights; Chief Purpose Officer role ends | New operating model; ESG demoted |
| **2024-10-31** | **MI–MarketAxess two-way data deal: CP+ prices go into S&P Evaluated Bond Pricing**; S&P bond reference data goes to MarketAxess | A venue's AI price feeds the evaluator. The corpus never mentions it again (§8) |
| 2024-11-13 | Kensho LLM-ready API (beta) for "GPT, Gemini, or Claude" | Start of the AI distribution strategy |
| 2025-04-14 → 10-10 | **OSTTRA sold to KKR ($3.1B EV, split 50/50 with CME)** | Exit from post-trade infrastructure (MarkitWire, triReduce, traiana) |
| 2025-04-29 | Intent to spin off Mobility | The merger perimeter shrinks again |
| 2025-07-15 | **Anthropic partnership**: Kensho MCP server puts Capital IQ data inside Claude | The first named frontier-LLM channel. AWS, Google, Microsoft, IBM, Salesforce and Cohere follow |
| 2025-10-02 | Catherine Clay (from Cboe) named S&P DJI CEO, replacing Dan Draper | A derivatives and exchange-data executive now runs the index business |
| 2025-10-15 | **With Intelligence acquired for $1.8B** | Biggest 2025 deal: private-markets data |
| 2025-11-13 | Investor Day: mission becomes **"Advancing Essential Intelligence"**; AI partner roster; new 3–5 year targets | The Cheung-era strategy |
| 2026-03-18 | **S&P 500 licensed for perpetual futures on Hyperliquid** (Trade[XYZ]) | The flagship index licence reaches a decentralised 24/7 venue |
| 2026-05-26 → **07-06** | MI President Saha leaves. **MI is split into Kensho Data & Platforms (Sally Moore) and Enterprise Solutions (Darren Thomas)**; pricing and reference data go to Enterprise Solutions; Credit Analytics goes to Ratings | The July 2026 reorganisation (§8) |
| 2026-07-01 | Mobility Global (MBGL) spin completed | Four divisions remain |
| 2026-09-14 / 09-17 | Leads Kaiko Series B-2; agrees to buy OpenZeppelin (smart-contract security, reporting to Ratings) | Digital assets become an M&A theme |
| **2026-10-13** | **First on-chain OTC swap on a tokenized benchmark**: total return swap (TRS) on the iBoxx USD Liquid IG index (tokenized by Kaiko on Canton), DRW vs Marex on Derivnex | An IHS Markit benchmark carried onto tokenized rails |

---

## 3. People

### Who leads (as of Oct 2026)
- **Martina Cheung**: President & CEO since 2024-11-01. Joined Ratings in 2010, then Chief Strategy Officer, then head of MI (2019–20), Ratings plus ESG/Sustainable1 (2021–24), then CEO.
- **Eric Aboaf**: CFO from Feb 2025 (previously CFO of State Street). Also owns strategy and M&A.
- **Ian Livingston**: Chairman since 2025-05-07 (previously BT CEO). He succeeded **Dick Thornburgh** (2020–25).
- Division heads:
  - **Yann Le Pallec**: Ratings.
  - **Catherine Clay**: S&P DJI, since Nov 2025.
  - **Dave Ernsberger**: S&P Global Energy (renamed from Commodity Insights in 2025).
  - **Sally Moore** (Kensho Data & Platforms) and **Darren Thomas** (Enterprise Solutions): co-heads of MI.
- Technology and AI:
  - **Firdaus Bhathena**: Chief Technology & Transformation Officer since Apr 2026 (previously FIS).
  - **Bhavesh Dayalji**: Kensho. In July 2026 his title changed from "Chief AI Officer" to "Head of Kensho Data & Intelligence".
- **Daniel Yergin**: Vice Chairman (from IHS Markit) and the CERAWeek figurehead.
- **Thomas Kim**: Chief Legal Officer from Oct 2026 (previously Thomson Reuters and Gartner). He replaces Steve Kemps.

### Who left, and when
| Person | Role | When and why |
|---|---|---|
| Doug Peterson | CEO 2013–24 | Planned succession, announced 2024-06-27. Board seat until May 2025; adviser until the end of 2025 |
| Ewout Steenbergen | CFO 2016–24 | Announced 2023-12-07 ("another professional opportunity"). Previously ran Kensho and Engineering Solutions |
| Adam Kansler | MI President (from IHS Markit) | Replaced in Oct 2024 |
| Saugata Saha | Platts/CI → MI and Chief Enterprise Data Officer | Left 2026-07-30. MI was then split rather than given a new president |
| Dan Draper | S&P DJI CEO 2020–25 | Replaced by an outsider from Cboe |
| Edouard Tavernier | Mobility | Replaced by Bill Eager (CARFAX) ahead of the spin |
| John Berisford | Ratings President / merger integration office | Left at the end of 2022 |
| Lance Uggla | IHS Markit CEO | Special adviser for one year after the close |
| Dimitra Manis | Chief Purpose Officer | Role abolished Oct 2024 |

Churn is concentrated in **MI**: three leaders in two years (Kansler, then Saha, then two co-heads).

### Signature views, with quotes

**Doug Peterson** (CEO to Oct 2024). His view: crises raise demand for S&P's products, scale is the strategy, and AI sits inside existing franchises.
- "The demand for our ratings, benchmarks, research, data, and analytics is greater than ever during uncertain and volatile markets," (2020-10-27, [Q3 2020 results](https://investor.spglobal.com/news-releases/news-details/2020/SP-Global-Revenue-Increased-9-In-The-Third-Quarter-With-Growth-Across-All-Four-Divisions-2020-10-27/default.aspx))
- "This merger increases scale while rounding out our combined capabilities" (2020-11-30, [merger announcement](https://investor.spglobal.com/news-releases/news-details/2020/SP-Global-and-IHS-Markit-to-Merge-in-All-Stock-Transaction-Valuing-IHS-Markit-at-44-Billion-Powering-the-Markets-of-the-Future-2020-11-30/default.aspx))
- "are ahead of schedule on cost and revenue synergies despite a challenging macro environment." (2022-08-02, [Q2 2022](https://investor.spglobal.com/news-releases/news-details/2022/SP-GLOBAL-DEMONSTRATES-RESILIENCE-IN-SECOND-QUARTER-RESULTS/default.aspx)). This was said in a quarter when adjusted revenue fell 5%.
- "our financial performance in 2022 did not match" (2022 annual report letter, [AR22](https://s29.q4cdn.com/690959130/files/doc_financials/2022/ar/S-P-Global-2022-Annual-Report.pdf)). A rare admission.
- "Generative AI was one of the biggest global news stories last year. It’s really a game changer." (2023 annual report, [CEO letter](https://www.spglobal.com/en/annual-reports/2023/ceo-letter))

**Martina Cheung** (CEO from Nov 2024). Her view moved from *data and technology serve the customer* (MI, 2020) to *proprietary data becomes more valuable because of AI* (2025–26), and then to "trusted, connected" data as the scarce good.
- "Technology and data science are playing a crucial role in how we bring value to our customers," (2020-05-14, [Kensho/NVIDIA](https://press.spglobal.com/2020-05-14-Kensho-Collaborates-with-NVIDIA-to-Advance-Automatic-Speech-Recognition))
- "The launch of S&P Global Sustainable1 signifies the critical intersection between sustainability and business performance" (2021-04-22, [Sustainable1](https://press.spglobal.com/2021-04-22-S-P-Global-unveils-new-ESG-and-sustainability-organization-S-P-Global-Sustainable1)). Peak ESG framing.
- "Separating Mobility will allow us to continue to focus on our core businesses and pursue our growth strategy," (2025-04-29, [Mobility spin](https://investor.spglobal.com/news-releases/news-details/2025/SP-Global-Announces-Intent-to-Separate-Mobility-Segment-into-Standalone-Public-Company/default.aspx))
- "As AI increasingly permeates every sector, customers are placing an even higher value on S&P Global’s proprietary benchmarks, data, and tools" (2025 annual report, [CEO letter](https://www.spglobal.com/en/annual-reports/2025/ceo-letter))
- "we are seeing more tailwinds than headwinds." (same letter)
- "In a world where data is abundant, but not all created equal, customers need trusted, connected, essential intelligence that brings context and conviction to decision-making" (2026-07-06, [MI operating model](https://investor.spglobal.com/news-releases/news-details/2026/SP-Global-Evolves-Market-Intelligence-Operating-Model-to-Accelerate-Agentic-Solutions-Platform-Capabilities-and-Innovation-Announces-Executive-Leadership-Changes/default.aspx))
- "These changes within Market Intelligence align our capabilities, enabling us to elevate the customer experience while growing our revenue and improving margins." (same, 2026-07-06). The reorganisation is framed around margins.

**Bhavesh Dayalji** (Kensho). His view: go where the user already works, inside other companies' LLMs.
- "we want to make our data more easily and immediately accessible to the entire LLM ecosystem," (2024-11-13, [LLM-ready API](https://press.spglobal.com/2024-11-13-S-P-Global-Launches-Kensho-LLM-ready-API-beta-,-Making-its-Structured-Data-Accessible-for-Generative-AI))
- "S&P Global is committed to meeting our customers where their workflows take place," (2025-07-15, [Anthropic](https://press.spglobal.com/2025-07-15-S-P-Global-and-Anthropic-Announce-Integration-of-S-P-Globals-Trusted-Financial-Data-into-Claude))
- "As agentic workflows become the norm, we deliver value by ensuring that customers can access our data seamlessly and accurately, wherever they work." (2026-06-08, [Cohere](https://press.spglobal.com/2026-06-08-S-P-Global-Expands-AI-Ecosystem-Reach-with-Cohere-to-Power-Trusted-Agentic-Workflows-for-Financial-Institutions))

**Sally Moore** (Chief Client Officer, now co-head of MI). She came from IHS Markit (Markit credit and loans; Thomson Reuters LPC before that).
- "The use of AI in financial services is rapidly accelerating and evolving, from tightly controlled workflows to fully autonomous, multi-agent systems" (2026-07-21, [Adaptive Retrieval](https://press.spglobal.com/2026-07-21-S-P-Global-Launches-Adaptive-Retrieval,-Giving-Customers-a-New-Way-to-Access-Data-Across-AI-and-Agentic-Workflows))

**Index leadership.** The line runs from *independent provider offering choice* to "benchmarks on-chain".
- Matturri: "Our philosophy as an independent index provider is to offer choice to investors." (2019-04-08, [S&P 500 ESG](https://press.spglobal.com/2019-04-08-S-P-Dow-Jones-Indices-Launches-ESG-Index-Based-on-Iconic-S-P-500-R))
- Roffman: "Traditional financial markets and digital assets are no longer mutually exclusive markets," (2021-05-04, [crypto indices](https://press.spglobal.com/2021-05-04-S-P-Dow-Jones-Indices-Launches-Cryptocurrency-Index-Series-Including-S-P-Bitcoin-Index))
- Drinkwater: "We believe digitally-native investors should demand the institutional-quality standards that define our indices" (2026-03-18, [Hyperliquid](https://press.spglobal.com/2026-03-18-S-P-Dow-Jones-Indices-Licenses-S-P-500-R-to-Trade-XYZ-for-Perpetual-Contracts-on-Hyperliquid))
- Drinkwater: "This transaction shows how established benchmark infrastructure can support new institutional market structures" (2026-10-13, [Derivnex](https://press.spglobal.com/2026-10-13-S-P-Dow-Jones-Indices-and-Kaiko-Enable-First-On-chain-OTC-Swap-Referencing-a-Tokenized-Benchmark,-Executed-by-DRW-and-Marex-on-Derivnex))

**Ratings and digital assets.**
- Elizabeth Mann (Ratings CFO): "Decentralized finance has the potential to redefine the financial markets in ways that have not been seen since the early days of fintech and e-commerce," (2022-05-17, [DeFi group](https://press.spglobal.com/2022-05-17-S-P-Global-Ratings-Establishes-Decentralized-Finance-DeFi-Group-Amidst-Heightened-Investor-Interest))
- Le Pallec: "Our digital assets strategy centers on bringing trusted data, benchmarks and transparent risk assessment to markets as they move onchain" (2026-09-17, [OpenZeppelin](https://investor.spglobal.com/news-releases/news-details/2026/SP-Global-Announces-Agreement-to-Acquire-OpenZeppelin/default.aspx))

**Pricing and fixed-income data** (the evaluated-pricing voice is thin, and mid-level only).
- Warren Breakstone: "High-quality and independent pricing across a wide range of fixed income classes is in elevated demand," (2023-06-28, [loan pricing](https://press.spglobal.com/2023-06-28-S-P-Global-Market-Intelligence-Launches-Loan-Pricing-and-Analytics-in-S-P-Capital-IQ-Pro-Platform-Expansion))
- Saha: "The expansion of private credit and the emergence of secondary trading necessitates common identifiers," (2025-06-24, [LXIDs](https://press.spglobal.com/2025-06-24-S-P-Global-Expands-Private-Markets-Offering-With-Private-Credit-Identifiers-Using-LoanX-IDs))

**Board on AI.**
- Livingston: "the growth of artificial intelligence, which provides significant opportunities for the business and some potential challenges." (2025 annual report, [chairman letter](https://www.spglobal.com/en/annual-reports/2025/chairman-letter))
- Thornburgh on Peterson: "Doug led the evolution of our Company from a diversified publishing holding company to a focused, markets-oriented information services company." (2024-06-27, [succession](https://investor.spglobal.com/news-releases/news-details/2024/SP-Global-Announces-Leadership-Succession/default.aspx))

### How views shifted
1. **AI moves from cost line to product, then to channel.** 2019–20 earnings treat Kensho as margin drag ("Kensho retention-related expenses" was still adjusted out in Q4 2020). In 2023 it becomes products (ChatIQ, Classify). From 2024 it becomes a distribution channel through third-party LLMs (LLM-ready API → MCP → AI Data Portal). In July 2026 Kensho is the name of half of MI.
2. **ESG rises and is retreated from** (§6). The 2021 Sustainable1 launch gives way to the 2025 framing of "energy expansion, not replacement".
3. **Breadth gives way to focus.** Peterson's case for the merger was scale and "rounding out". Cheung's moves are subtraction: Engineering Solutions, Fincentric, PrimeOne, OSTTRA, Mobility, EDM/thinkFolio and upstream software were all sold or spun.

---

## 4. Mission and identity, as stated

| Period | Phrase | Source |
|---|---|---|
| 2018–2021 | Vision **"Powering the Markets of the Future"**; purpose "Accelerating Progress"; boilerplate *essential intelligence … make decisions with confidence/conviction* | AR19, merger headline 2020-11-30 |
| 2021 | "The Next Era of Essential Intelligence"; new values *discovery, partnership, integrity* | AR21 |
| 2022–2024 | Vision **"Powering Global Markets"** (five pillars); purpose **"Accelerate Progress"** | Investor Day 2022, AR22, AR23 |
| 2025– | Mission **"Advancing Essential Intelligence"**; three objectives: Advancing Market Leadership, Expanding into High-growth Adjacencies, Amplifying Enterprise Capabilities and AI | Investor Day 2025, AR25 |
| 2026 | Clay ties the mission to DeFi: "our mission to advance essential intelligence by bridging traditional and decentralized finance" | 2026-09-14 Kaiko release |

Things to notice:
- **"Accelerate Progress" disappears** from the 2025 letters.
- **"Automotive markets"** stayed in the corporate boilerplate in October 2025, six months after the Mobility spin was announced.
- **Divisions still say "confidence" while corporate says "conviction"**, even in 2026. The brand was never fully unified after the merger.
- In April–July 2024 the boilerplate quietly swapped **ESG for sustainability**.
- The direction of travel is from *we power markets*, which is about infrastructure and breadth, to *we are the trusted data layer*, which is about AI.

---

## 5. Tailwinds, headwinds and challenges

**A** = the company says it. **I** = inferred by me or the readers.

### Tailwinds
| Tailwind | Evidence | |
|---|---|---|
| Volatility and crises raise demand; Ratings benefits from refinancing waves | Q2 2020 Ratings revenue +26% and adjusted margin 69.1%. Investor Day 2025: $8T+ of S&P-rated corporate debt maturing over 3 years vs a $6.5T average | A |
| Passive and indexing growth | ETF AUM on S&P indices: $1.7T (2019) → $2.8T (2021). Investor Day 2025: $27.7T indexed or benchmarked | A |
| AI makes proprietary data more valuable | >95% of revenue from proprietary data and tools (Investor Day 2025, AR25); "over $1 billion" invested in AI since 2018 | A. The claim is S&P's own and untested |
| Private markets and private credit | Private-markets revenue ~$400M (2022) → $535M (2024); With Intelligence ($1.8B); LXIDs; Cambridge Associates/Mercer | A |
| Energy expansion and AI data centres | Investor Day 2025: electricity demand ~3x by 2050; datacenterHawk and Enertel acquired | A |
| Digital assets gaining regulatory clarity | GENIUS Act cited; stablecoins "$301bn" (2025-10-14); vault deposits $1.5B → ~$10B (2024→2026) | A |
| Regulation creates data demand | EU BMR, IOSCO, SEC Rule 2a-5 (PVR Source), T+1 (DTCC ALERT link), SEC 10c-1a, SFTR | A |

### Headwinds and challenges
| Headwind | Evidence | |
|---|---|---|
| **Ratings is cyclical** | 2022: guidance suspended (2022-06-01); transaction revenue −31% / −44% / −56% (Q1–Q3); pro forma revenue −4% | A |
| **Integration took longer than promised** | Close slipped from 2H21 to Q4'21 to Q1'22. Revenue synergies were ~$16M run-rate nine months after close vs a $350M target (Investor Day 2022). Cost synergies came much faster | A (figures) / I (reading) |
| **Forced divestitures to rivals** | CUSIP to FactSet, LCD to Morningstar, OPIS to News Corp | A |
| **ESG forecasts missed** | ~$600M by 2025 (AR21) and $800M by 2026 (AR22) vs $359M actual in 2024 (AR24) | A (figures) / I (reading) |
| **Regulatory and compliance costs** | SEC: $9M (DJI, 2021), $2.5M (Ratings, 2022), $20M (Ratings off-channel communications, 2024) | A |
| **AI as a competitive threat** | The Investor Day 2025 safe harbour lists "competitive products (including those incorporating generative artificial intelligence" | A (risk factor) |
| **LLMs could take over the customer interface** | S&P puts its data inside Claude, Copilot, Gemini and Cohere, so the terminal (Capital IQ Pro) is no longer the only place users meet the data. Value then depends on licensing. Farsight's CEO argues the data-access moat is ending (§7) | I |
| **MI growth and margin pressure** | MI is the lowest-margin division (adjusted 31–35% vs Ratings and DJI above 55%). Q4'22: "slower growth in Desktop and declines in Enterprise Solutions". The 2026 reorganisation is pitched as "improving margins" | A (figures) / I |
| **Leadership churn** | A one-year CFO gap; three MI leaders in two years; DJI and Mobility heads replaced in 2025; a new CTTO and CLO in 2026 | I |
| **The AI boom is a credit risk in S&P's own research** | Ratings: "all six hyperscalers to generate negative free operating cash flow in 2026 and 2027" (2026-08-27) | A (Ratings research) |
| **Geopolitics** | Russia exit (Commodity Insights' biggest headwind in 2022); tariffs (Investor Day 2025 market-forces slide) | A |
| **Capital return beyond its own framework** | Since 2022, 145% of adjusted FCF returned vs an "at least 85%" target. Funded by divestiture proceeds and debt | A (figure) / I (reading) |

---

## 6. ESG: the clearest case of a narrative reversing

- **2019–21:** SAM/CSA bought; ESG Scores launched; Trucost; Sustainable1 (launched under Cheung); GFANZ; a net-zero-linked revolver.
- **2022:** Peterson writes an open letter on ESG scores, and the 2022 annual report sets an $800M-by-2026 target.
- **2024:** *ESG* is replaced by *sustainability* in the boilerplate (Apr→Jul); Sustainable1 is folded into Commodity Insights (Oct); the Chief Purpose Officer role ends.
- **2025:** Cheung writes "The next two decades will be characterized by energy expansion, not replacement" ([AR25](https://www.spglobal.com/en/annual-reports/2025/ceo-letter)).

The same executive built the ESG franchise and then folded it into another division. It makes a clean case study for course 11 (Responsible Business).

---

## 7. Outside voices and skeptics in the corpus

**Partners** (everyone is supportive by design):
- Lance Uggla (IHS Markit): "This transaction is a win for both IHS Markit and S&P Global" (2020-11-30).
- Kat Sweeney (MarketAxess) on the CP+ deal: "will enable our firms to close the gaps between best execution, intraday trading decisions and end-of-day valuation," (2024-10-31, [MarketAxess deal](https://press.spglobal.com/2024-10-31-S-P-Global-Market-Intelligence-and-MarketAxess-Announce-Strategic-Fixed-Income-Data-Partnership))
- Terry Duffy (CME) on OSTTRA: "OSTTRA has generated significant growth over the past several years" (2025-04-14).
- Others: Thomas Kurian (Google Cloud), Bill Borden (Microsoft), Sergey Nazarov (Chainlink), Ambre Soubiran (Kaiko), Stephen Dainton (Barclays, a data contributor to S&P pricing).

**The few that cut against S&P's own story:**
- **Farsight CEO Samir Dutta**, quoted inside an S&P release (2026-07-23), says the data moat is ending: "The industry has spent years competing on access to data. The next frontier is helping firms turn that data into client-ready work" ([Farsight](https://press.spglobal.com/2026-07-23-S-P-Global-Market-Intelligence-Partners-with-Farsight-to-Launch-AI-powered-Financial-Workflow-Capability-for-Capital-IQ-Pro)).
- **S&P MI's own Quantamental research**, six weeks before the $44B all-stock deal: "Large mergers and acquisitions often negatively impact growth, profitability, and returns" (2020-10-19, [report](https://press.spglobal.com/2020-10-19-Four-key-CEO-practices-can-increase-corporate-value-S-P-Global-Market-Intelligence-report-finds)).
- **Regulators**, via remedies rather than words:
  - CMA concerns were limited to UK commodity and petrochemical price assessments.
  - The EC demanded the CUSIP and LCD sales.
  - The DOJ required the OPIS sale.
  - The SEC brought three settlements: 2021, 2022 and 2024.
- **Market users pushing back:** Platts withdrew a Dated Brent CIF change within about three weeks (2021-03-10). GICS reclassifications were dropped for "lack of market consensus" (2022-03-31).
- **Missing:** there are no analysts, short-sellers or press critics in the corpus (see gaps in §1).

---

## 8. Links to the Tradeweb study

1. **The pricing contest: S&P sides with MarketAxess, and so sits on the opposite side from Tradeweb.**
   - MarketAxess CP+ feeds S&P Evaluated Bond Pricing (2024-10-31). That release covers 1.2M+ bonds, with CP+ updating every 15–60 seconds and integration from H1 2025.
   - **After that one release, the corpus never mentions MarketAxess or CP+ again. That includes 2025 and 2026, and the news that ICE agreed to buy MarketAxess (2026-07-30; see the ICE sibling note).** S&P has said nothing public about change of control.
   - The July 2026 reorganisation puts "pricing and reference data" in Enterprise Solutions. That treats pricing as workflow plumbing, not a growth line, which matches `tradeweb-ai-price` §5.
   - New detail not in that note: **Barclays contributes its own data to S&P cross-asset pricing** (2025-07-23), and **Evaluated Loan Pricing** now covers 8,000+ leveraged loans (2024-07-09). Evaluated pricing therefore rests on two inputs: dealer contributions and a venue feed (CP+), not on S&P's own trade data or model.
2. **iBoxx and CDX/iTraxx, where the two companies cooperate.**
   - First fully electronic iBoxx TRS on Tradeweb's SEF (2021-03-26, Tradeweb corpus).
   - In Oct 2026 S&P takes iBoxx **on-chain**: a TRS on the tokenized iBoxx USD Liquid IG index on Canton, via Derivnex, DRW and Marex. Tradeweb is not involved.
   - **Both S&P Global and Tradeweb invested in Digital Asset (Canton)'s $355M raise** (2026-06-11, Tradeweb corpus).
   - Both took part in the DTCC tokenized-collateral pilot (2026-07-15, Tradeweb corpus).
   - So they share the same tokenization rail but run separate products on it.
3. **OSTTRA/MarkitWire is shared plumbing.**
   - Tradeweb's first electronic swaption termination (2026-02-11) and its bilateral IRS unwinds (2026-09-30) confirm on **OSTTRA's MarkitWire**.
   - S&P sold OSTTRA to KKR in Oct 2025. Tradeweb's new bilateral-termination business therefore depends on infrastructure that S&P built at Markit and has now left to private equity.
4. **Primary markets.**
   - S&P MI InvestorAccess (from Ipreo) connected to Tradeweb in European primary (2022-09-29, Tradeweb corpus).
   - Separately, S&P connected InvestorAccess to **Bloomberg TSOX** (2023-06-22).
   - S&P is building an issuance utility that plugs into every venue rather than picking one.
5. **People.**
   - S&P's new CLO **Thomas Kim** "led the separation" of Thomson Reuters' Financial & Risk unit, which became Refinitiv (2026-10-09). Refinitiv was Tradeweb's controlling shareholder.
   - Sally Moore came from Thomson Reuters LPC and Markit.
   - No executive has moved directly between S&P and Tradeweb.
6. **A contradiction to keep in view.** Tradeweb's pitch is that a *trade-driven* price (Ai-Price) is the better ruler. S&P's 2023 line is that "independent pricing" is "in elevated demand", yet in 2024 it imported a *venue's* price to make its evaluations "more consistent". Both companies are effectively conceding that venue flow now sets the reference price.

---

## 9. Recommendation: what's worth noting

Ranked by how much each note teaches per minute of the user's time.

| # | Candidate note (slug) | One-line thesis | Why it's worth your time | Serves |
|---|---|---|---|---|
| 1 | `spglobal-ihs-markit-merger` | **The $44B merger's real price was paid in remedies and in the year after closing.** Regulators made S&P sell CUSIP, LCD and OPIS to rivals. 2022 revenue fell. Within four years Engineering Solutions, OSTTRA, Mobility and several Markit software lines were gone. | A complete, dated M&A case with numbers at every step: price, synergy targets vs actuals, remedies, guidance cuts, a $12B ASR and the disposals. It also contains S&P's own research warning against large stock deals. | **E3** M&A, **02** Corporate Finance, **04** Strategy |
| 2 | `spglobal-ai-data-layer` | **S&P is betting it can be the trusted data layer *inside* other companies' LLMs instead of owning the screen.** The path runs from the Kensho API to MCP, then to the AI Data Portal, and in July 2026 to an MI reorganised around Kensho. | This is the main AI strategy question for every data vendor (Bloomberg, LSEG and FactSet face it too). The corpus documents each step, includes one skeptic (Farsight), and shows the margin framing of the reorganisation. | **E10** Digital & AI, **04** Strategy (platform power, disintermediation) |
| 3 | `spglobal-benchmarks-onchain` | **The index licence follows liquidity to wherever it trades: S&P 500 perpetuals on Hyperliquid, a tokenized S&P 500 fund, an iBoxx TRS on Canton, Kaiko and OpenZeppelin.** | Concrete market-structure firsts in 2025–26. They tie into the Tradeweb/Canton thread and set up the BlackRock, JPMorgan and Goldman tokenization sessions. Also note the tension: S&P refuses megacap exceptions to protect index rules while licensing leveraged 24/7 perpetuals. | **04** Strategy, **E9** Macro/market structure, **E10** |
| 4 | `spglobal-leadership-succession` | **A textbook planned CEO succession, followed by two years of turnover underneath it.** Cheung's ten-year path (MI → Ratings/ESG → CEO), a one-year CFO gap, and three MI leaders in two years. | Lets you compare a well-run board process (announced in June, effective in November, the outgoing CEO stays as adviser) with execution churn below it. Good material for an executive-track case. | **E1** Leading at Scale, **E4** Governance, **09** Leadership |
| 5 | `spglobal-esg-reversal` | **One executive built an ESG franchise and then folded it.** An $800M target met $359M actual, the wording changed, and the message became "energy expansion, not replacement". | A short, dated lesson in narrative risk and in forecasting against hype. | **11** Responsible Business, **E5** Transformation, **07** Decision-making (base rates) |
| 6 | *Update, not new:* `tradeweb-ai-price` §5 | Add Barclays' data contribution, Evaluated Loan Pricing, S&P's silence on CP+ after the ICE–MarketAxess deal, and pricing filed under Enterprise Solutions in July 2026 | Four facts; not worth a standalone note | **04** |

**What is NOT worth noting, and why**
- **Mobility monthly auto-sales and forecast releases (~60 items).** These cover auto demand, not market structure. The spin-off belongs inside note #1.
- **Platts price-assessment launches, CERAWeek promotions and energy outlooks.** They are commodity commentary and outside the lens. The one exception is the Platts/ICE Brent co-governance, which is a single line in #3 or #1.
- **Ratings ESG Evaluations, SPOs and "report says" items.** They are ratings research, not corporate strategy.
- **S&P DJI index launches** (ESG, carbon, factor, private equity). There are many and each one adds little. Only the on-chain and venue-licensing items belong in #3.
- **Quarterly results in this corpus.** After Q1 2023 they are stubs. A financials note would need the earnings PDFs first (§1 gap 1).
- **Capital IQ Pro release notes.** These are incremental feature lists. They are evidence for #2, not a subject of their own.

---

## 10. Quote verification

Every quoted string in this file was checked with `verify_quotes.py` (kept in the session scratchpad, not the repo) against the `text` of `articles.jsonl`. Before comparing, whitespace was collapsed and curly quotes and apostrophes were normalised. The result is recorded below the line.


**Result (2026-10-25):** 73 verified, 0 missing, 73 total. Paraphrased labels are in italics, not quotation marks. The Tradeweb-side facts in §8 (iBoxx TRS 2021, Canton raise 2026-06-11, DTCC pilot 2026-07-15, OSTTRA/MarkitWire 2026-02-11 and 2026-09-30, InvestorAccess 2022-09-29) were checked against `_ingest/raw/tradeweb/articles-2019-2026.jsonl`. The ICE–MarketAxess deal date comes from the read-ice sibling session note.
