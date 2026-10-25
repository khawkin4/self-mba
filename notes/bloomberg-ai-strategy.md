# Note · Bloomberg AI strategy — from ‘best financial LLM’ to ‘AI built on Bloomberg’: the model was dropped, the data factory and the chat network became the product

> Strategy / technology note · Maps to **E10** (Digital & AI Transformation — build vs partner, pilot to production, governance), **Course 04** (Competitive Strategy — complements, switching costs, open standards), **Course 07** (Data, Analytics & Decision-Making — annotation, evaluation, survey denominators), **Course 06** (Operations — human-in-the-loop workflow redesign) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-terminal-instrumentation]], [[bloomberg-enterprise-data]], [[bloomberg-buyside-stack]], [[bloomberg-people]]

- **Source:** about 40 AI items in the Bloomberg corpus (`_ingest/raw/bloomberg/articles.jsonl`), **Sep 24 2020 – Oct 15 2026**. They are press releases (bloomberg.com and PR Newswire), *Tech At Bloomberg* stories, Bloomberg Intelligence (BI) research and Bloomberg-run surveys. Reader notes P4, P7, P3 and P8 cover the same items. Everything is Bloomberg's own channel, and Bloomberg is private, so there is **no AI spend, price, usage or revenue figure anywhere**. The only ‘adoption’ claim is qualitative (ASKB "most rapidly adopted"). The ~45 BI sector pieces on the AI boom (chips, power, capex) are market research, not company strategy, and are used only in §1 and §4.
- **Core claim:** Bloomberg tells one AI story in three registers, and the register changed while the asset underneath did not.
  - **2009–2022: ML as plumbing.** A news-sentiment analytic (2009), search (2012) and a human-in-the-loop data factory. Thousands of Data-department analysts annotate, and models extract. The headline result is time to client "from months to minutes".
  - **2023: the model as moat.** **BloombergGPT** (Mar 30 2023): 50bn parameters, a **363bn-token** proprietary corpus plus 345bn public tokens. It was a research paper, not a product, and **it is never mentioned again** in any later item in the corpus.
  - **2024–2026: the data and the network as the product.** Features shipped in a steady cadence: earnings-call summaries (Jan 2024) → news summaries (Jan 2025) → Document Insights (Apr 2025) → Document Search & Analysis (Jun 2025) → **ASKB** (beta by Apr 2026, GA Oct 15 2026) → **Enterprise MCP** (Sep 29 2026). The 2026 claim is Edwards's "This isn’t Bloomberg building on AI. It’s AI built on Bloomberg."
  - [[bloomberg-terminal-instrumentation]] argues the Terminal's moat is the **interface plus the IB network**, not the data. This note shows Bloomberg's AI moves are aimed at exactly that point. ASKB reads the client's own IB chats ("roughly 40 million" a day). Enterprise MCP carries entitlements and metadata out to clients' own agents. The model is treated as interchangeable.

---

## 1. Chronology — the spine

*All figures are as Bloomberg states them, unless another source is named.*

| Date | Event | Numbers stated |
|---|---|---|
| **2009** | First ML product: a Terminal analytic for the sentiment of news stories (per Meet the Team, Jul 2024, and Kothari, Jul 2025) | — |
| 2012 / 2020 | Search built into the Terminal. Neural nets for news themes (Kothari) | — |
| 2020-09-24 | Global Data + CTO Data Science publish *Best Practices for Managing Data Annotation Projects* (Tseng, Stent, CDO Maida) | Drawn from 30+ annotation project managers |
| 2022-03-04 | Ticker Plant story: **build, not buy**. Edwards: "There are no good open source or commercial Market Data software solutions that our engineers can pull off the shelf" | "over 200 billion pieces of financial information" a day. ~80bn queries a day. 6,500+ engineers. Market-data team of ~400 |
| **2023-03-30** | **BloombergGPT** paper (arXiv 2303.17564). Edwards: "we see tremendous value in having developed the first LLM focused on the financial domain" | **50bn** parameters. **363bn** financial + 345bn public = **700bn+** tokens. Forty years of archive |
| 2023-05-11 | *Humans in the Loop* story. Mann: "reduced from months to minutes" (in some cases). MODL<GO> is the showcase | "over 200 million pieces of financial information every day". "thousands of analysts" in Data |
| 2023-06-01 | BI: GenAI market **$1.3tn by 2032** from $40bn in 2022 (42% CAGR). Restated Mar 2024 (~43%) | ~$280bn of new software revenue |
| **2024-01-22** | **AI-Powered Earnings Call Summaries**, the first GenAI feature. "Bloomberg Intelligence analysts help train the large language models". Click-through to transcript excerpts | DS<GO> searches "hundreds of millions" of documents |
| 2024-07-29 | Summaries + DS on mobile and Vision Pro. AI Engineering profile | **>350** AI researchers/engineers. >100 papers in 3 years. 4 sites |
| 2024 Q3 | Internal GenAI tools protocol prototyped (server SDK, middleware) *before* MCP existed (Jul 2025 story) | — |
| **2025-01-15** | **AI-Powered News Summaries**: three bullets on top of Bloomberg News stories, evaluated by subject-matter experts | — |
| 2025-02-25 | Envoy AI Gateway v0.1 (with Tetrate, CNCF), open source | — |
| **2025-04-07** | **Document Insights** ('Ask a Question', Key Notes), "an evolution of" earnings summaries. BI analysts helped train it | Library: **>200 million** company documents. 5,000+ news stories a day |
| **2025-04-28** | RAG-safety and finance risk-taxonomy papers (NAACL, FAccT) | 5,000+ harmful questions, **11** LLMs, **16** safety categories |
| 2025-05-29 | Fixed-income term-sheet extraction story: human-in-the-loop annotation by "our best people" | — |
| **2025-06-16** | **Document Search & Analysis** announced; Terminal release "by the end of 2025". Beta users: Schroders, Bernstein, Mizuho, Bantleon | Library: **>400 million** documents |
| 2025-07-14 | *Bloomberg embraces MCP*: internal approach converged on the open standard | — |
| 2025-09-23 | **AI Portfolio Commentary** in PORT Enterprise: attribution + news → written return drivers | PORT Enterprise: **750+** clients |
| 2025-11-24 | AI Summary in Company News (CN<GO>). News summaries extended beyond Bloomberg News | — |
| 2025-11-25 | PExA text-to-SQL agent | 70.2% on Spider 2.0 (Snow), a top position |
| 2025-12-17 | Survey of European finance leaders (Stent) | 300+ respondents. 75% fear lost profit/obsolescence. 6% say overhyped |
| 2026-01-22 | Research-data survey of quants | 150+ respondents. **54%** have not begun GenAI. 72% want sector data |
| **2026-04-21** | UK AI-in-Finance poll. **ASKB "now in beta"**, 2026 roadmap | 100+ respondents. **50%** hallucination, 27% explainability |
| 2026-05-14 / 08-05 | **Vault**: BSpeech voice transcription (50+ languages), then Insider Dealing and Personal Trading AI policies | **>400** AI researchers/engineers |
| 2026-08-18 | ASKB on mobile: persistent session across devices, personalisation | — |
| **2026-09-29** | **Enterprise MCP** over Data License Plus. Bloomberg "started and leads the MCP Financial Services Interest Group" | **100M+** securities, **50,000+** fields. 3 launch Skills |
| **2026-10-15** | **ASKB GA**: IB chats, Worksheets, Bloomberg Drive brought in as context | ~**40m** IB chats a day. 3 months of chat history |

## 2. The four layers, and their best numbers

| Layer | What it is | Best stated metric | What's missing |
|---|---|---|---|
| **Data factory** (2009→) | Analysts annotate, models extract and tag (entities, topic codes, dividends, term sheets), humans QA against "golden" sets | "months to minutes". 200m (or 200bn) items a day | Error rates, cost per item, analyst headcount trend |
| **Research model** (2023) | BloombergGPT | 50bn params. Beats similar-size open models on finance NLP (Bloomberg's benchmarks) | Any deployment. Any later mention |
| **Terminal features** (2024→) | Summaries → Document Insights → DS&A → ASKB, PORT commentary, Vault policies | Library 200m → 400m docs (10 weeks apart). ASKB "most rapidly adopted" | Users, prompts, accuracy, price. Which model runs underneath |
| **Distribution layer** (2025→) | Envoy AI Gateway, internal tools protocol → MCP, Enterprise MCP, agents on mobile | 100M+ securities, 50k+ fields under DL rights | Customer count (LSEG discloses one, see §6) |

## 3. How the narrative moved

1. **2020–2023: the factory story.** The pitch is that domain experts plus ML beat both alone. Mann: "It’s really a transfer of human skill from manually extracting data points to thinking about defining and creating workflows." Papadimitriou (2025): "We quickly realized that we needed our best people for the annotation work." Annotation is presented as a skill, not a cost to be cut.
2. **March 2023: the model story.** "The quality of machine learning and NLP models comes down to the data you put into them" (Mann). The data is the argument, and the 50bn-parameter model is the proof. This is the only time Bloomberg argues *we have a better model*.
3. **2024–2025: the feature story.** No model name is ever given. Every release instead stresses who trained or checked it (BI analysts, "subject matter experts"), click-through attribution, and the mission line "reimagine the Bloomberg Terminal for the age of AI". The infrastructure team says the hard part was production, not models: "Teams could build impressive demos in days, but it took much longer to get them production-ready for clients to use" (Musial, 2025).
4. **2026: the readiness and network story.** McManus: "the bottleneck facing financial institutions has shifted from model capability to data readiness". ASKB answers are "grounded in Bloomberg’s own decades of experience in market data, analytics, and industry partnerships, not a general AI model". The boilerplate gains "agentic AI architectures" (the Apr 2026 survey version lacks it; Aug, Sep and Oct 2026 versions have it).

## 4. What the claims don't prove

1. **No usage, no money.** ASKB's "most rapidly adopted" claim has no denominator. There is no ASKB user count, no Enterprise MCP client count and no price. The only seat counts in the corpus are old ("Over 325,000" in 2022, ">350,000" in Dec 2023). Compare LSEG, which counts MCP customers quarter by quarter (context, from [[lseg-ai-everywhere]]).
2. **BloombergGPT's fate is unexplained.** The Mar 2023 release said it "will assist Bloomberg in improving existing financial NLP tasks". No later release says whether summaries, DS&A or ASKB use it, a successor, or third-party models. Silence fits a quiet write-down of the in-house frontier-model bet. *That is inference.*
3. **Accuracy is asserted, never measured in public.** Trust is attributed to citations and expert review. No hallucination rate is published for any product, even though Bloomberg's own poll says this is the buyer's first concern. The one hard evaluation result (PExA, 70.2%) is a public benchmark, not a product.
4. **The surveys are Bloomberg's own audiences.** The UK poll is a live vote of 100+ summit attendees; the European one 300+; the quant one 150+ at client workshops. They then justify Bloomberg's product design (attribution, data readiness). A 50% share among ~100 respondents carries roughly ±10pp of sampling error, before any selection bias.
5. **Self-reported counts drift.** Ticker Plant: "200 billion" items a day (2022) vs "200 million" (2023). The document library grew from >200m (Apr 2025) to >400m (Jun 2025), probably a redefinition (adding news and research) rather than growth. AI headcount went 350+ (2024) to 400+ (2026) with no breakdown.
6. **‘Leads the MCP group’ is self-certified.** Bloomberg says its engineers are "the primary authors of proposals" on enterprise governance in MCP. No outside party in the corpus confirms it.
7. **The RAG paper cuts both ways.** It found "large increases in unsafe responses under the RAG setting". ASKB is, by its own description, retrieval over chats, files and news. The paper is safety *research*, not evidence that ASKB is safe.

## 5. Strategic read (inference — not stated by Bloomberg)

- **The model was a means; the factory was the asset.** BloombergGPT showed that the 40-year archive is training-grade. Once general models got good enough, the cheaper play was to keep the archive as context and evaluation sets, not as training data. Fifteen years of annotation pipelines became evaluation and guardrail pipelines.
- **ASKB monetises the moat [[bloomberg-terminal-instrumentation]] identified.** IB chat is the one asset that note grades as having *no substitute at any price* (its §2). Indexing three months of a client's chats turns network lock-in into *context* lock-in. A rival model can match Bloomberg's data. It cannot read your counterparties' messages from this morning. Switching costs now include your own searchable history.
- **Enterprise MCP is a hedge against the desktop.** If analysts move to Claude, Copilot or in-house agents, Bloomberg wants its entitled data and metadata to be the tool those agents call. That keeps licence economics (DL rights, entitlement checks) when the screen is lost. This is the same move LSEG and S&P made, but a year later and without naming any model lab as a partner.
- **Build, not buy, extends to AI infrastructure.** The Ticker Plant logic (nothing to pull "off the shelf") reappears: an internal tools protocol in Q3 2024, then convergence on MCP because "it was being built in the open". Bloomberg builds the middleware (identity, entitlements, guardrails) and adopts standards for the connection itself. It doesn't acquire AI startups (contrast TR's $650M Casetext, S&P's Kensho).
- **The governance message is a market-structure position.** Vault surveillance, RAG-safety research, a finance risk taxonomy and "attribution" all set the standard Bloomberg itself meets: entitled, cited, auditable. That favours incumbents with clean licence rights over startups that scrape.
- **The house skeptics are useful, and tolerated.** The BTCA product managers wrote that most AI TCA models "were built for centralized, high-volume equity markets and then retrofitted for fixed income as an afterthought". BI's European buy-side study found "AI and alternative data rank lowest" among traders' technology priorities, with AI in internal algos unused by 92%. Corporate messaging is agentic. The desk-level evidence Bloomberg itself publishes says adoption in execution is early.

## 6. Comparison — six incumbents, one pattern

| Firm | Own model? | Main AI surface | Distribution to others' agents | Numbers disclosed |
|---|---|---|---|---|
| **Bloomberg** | BloombergGPT 2023, then silence | ASKB inside the Terminal + IB/Drive context | Enterprise MCP (Sep 2026) | 400+ AI staff. No usage or revenue |
| LSEG | No | Workspace AI Search | MCP via Microsoft, then Claude/ChatGPT | MCP **300+** customers, AI Search 47,000 users (Oct 2026) (context, from [[lseg-ai-everywhere]]) |
| S&P Global | No (Kensho bought 2018) | Capital IQ Pro / ChatIQ | Kensho MCP into Claude (Jul 2025), AI Data Portal | *over $1bn* cumulative AI investment (context, from [[spglobal-ai-data-layer]]) |
| Thomson Reuters | "Thomson", $40M (Aug 2026) | CoCounsel | CoCounsel inside Claude via MCP (May 2026) | $200M+ a year AI spend. 1M users (context, from [[thomsonreuters-ai-strategy]]) |
| Tradeweb | No | TARA chat (Jun 2026), Ai-Price | API / Python | AiEX 58% of tickets (context, from [[tradeweb-tech-ai-data]]) |
| Goldman Sachs | No | GS AI Assistant (internal) | — | ~12,000 engineers, flat (context, from [[goldman-ai]]) |

**Read:** Bloomberg and TR are the only two that trained their own model. Bloomberg went first (2023) and went quiet; TR went last (2026) and calls it a hedge. Everyone converges on MCP as the outlet. Bloomberg is the only one whose differentiator is **client-generated** content (chats), not just licensed content. It is also the least transparent on numbers, because it is private and has no investors to tell.

## 7. Canon lenses

- **Cornered resource and switching costs** ([[canon-helmer-7-powers]]): the archive and the IB graph are cornered resources. ASKB adds a personal switching cost (your indexed history).
- **Complements and open standards** ([[canon-shapiro-varian-information-rules]], [[canon-cusumano-business-of-platforms]]): adopting MCP commoditises the connector so the scarce part, entitled data plus metadata, keeps its price. The risk is that model owners commoditise the data provider instead.
- **Sustaining innovation** ([[canon-christensen-innovators-dilemma]]): every 2024–26 feature makes the existing seat better for existing users. The disruption test is whether a cheap agent over public filings is ‘good enough’ for the low end, which the instrumentation note argues is already true for equity fundamentals.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]]): ASKB's chat feature gets more valuable the more your counterparties chat on IB. AI deepens a network effect rather than creating one.
- **Noise and evaluation** ([[canon-kahneman-sibony-sunstein-noise]]): Bloomberg's "golden copy" annotation sets are a noise audit by design. The gap is that it never publishes the results.
- **Normal accidents** ([[canon-perrow-normal-accidents]]): the RAG finding (retrieval makes safe models unsafe) is a tight-coupling failure. Adding a component meant to reduce error introduced a new one.

## 8. Practitioner counterpoint

- **For Bloomberg:** it has the most credible data-factory story of the six. It published annotation practice in 2020, two years before ChatGPT. Its features ship with click-to-source attribution, which a regulated user needs. Client quotes are specific: NatWest's Richardson calls Document Insights "a godsend" on heavy earnings days; Impax says Vault's models "have substantially improved alert quality and reduced false positives". Building on open standards instead of locking clients into one model is defensible.
- **Against:** none of it is measured in public. A trader cannot compare ASKB's error rate to a Claude-plus-filings setup. Russell Investments' CTO, on Bloomberg's own stage: "I think we’re still in the honeymoon period. I don’t think many companies are actually thinking about ROI." BI's own survey shows desks are barely using AI in execution.
- **Both:** a desk should test ASKB or Enterprise MCP on its own evaluation set, with a known answer key (positions, corporate actions, deal terms). It should score citation accuracy as well as answer accuracy, and repeat the test after model changes Bloomberg won't announce.

## 9. Open questions to track

1. Which model(s) run ASKB? Does Bloomberg ever name a lab partner, or revive BloombergGPT?
2. The first ASKB user or Enterprise MCP client number, and whether ASKB is priced separately from the seat.
3. Does the promised Terminal-subscriber MCP solution put ASKB-grade data into Claude, Copilot or ChatGPT? That would be the LSEG move.
4. Real-time data over Enterprise MCP (promised). Price freshness is where Bloomberg's Ticker Plant moat is largest.
5. Does chat indexing raise compliance pushback? IB chats are surveillance records (see Vault) and now also AI context.
6. Canoe inside ASKB (stated in the 2026 deal releases): do private-markets documents become the next proprietary context set? See [[bloomberg-private-markets]].
7. Does AI headcount keep growing past 400 while Data-department analyst numbers fall? That would show the human-in-the-loop ratio changing.

**Links:** [[bloomberg-hub]] · [[bloomberg-terminal-instrumentation]] (the interface + IB moat this note extends) · [[bloomberg-enterprise-data]] (DL+, the base of Enterprise MCP) · [[bloomberg-buyside-stack]] (PORT, BTCA, AIM) · [[bloomberg-pricing-bval-ibval]] (ML pricing, IBVAL) · [[bloomberg-private-markets]] · [[bloomberg-people]] · [[bloomberg-outside-voices]] · [[bloomberg-mission-forces]] · [[lseg-ai-everywhere]] · [[spglobal-ai-data-layer]] · [[thomsonreuters-ai-strategy]] · [[goldman-ai]] · [[tradeweb-tech-ai-data]] · [[tradeweb-ai-price]] · [[wss-ai-economics]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-cusumano-business-of-platforms]] · [[canon-christensen-innovators-dilemma]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-perrow-normal-accidents]]

---
### Rep
Four short computations, all with numbers from this note.

**(a) How proprietary was BloombergGPT?** The corpus was 363bn financial tokens plus 345bn public. What share was Bloomberg's own? *(Answer: 363 / 708 ≈ **51%**.)* Then argue in one paragraph: if half of the model's diet was public text, how much of its edge could a general model with retrieval over the same 363bn tokens recover? Use §4.2 and §5 bullet 1.

**(b) Check BI's forecast arithmetic.** BI says GenAI grows from $40bn (2022) to $1.3tn (2032) at a 42% CAGR, later revised to $1.8tn by 2032. Verify the first figure and compute the implied CAGR of the second on the same base. *(Answer: (1,300/40)^(1/10) = 32.5^0.1 ≈ **1.42**, so 42% checks out. (1,800/40)^(1/10) = 45^0.1 ≈ **1.46**, about 46%, if the base is unchanged. The upgrade is +38% in the end-state.)* Which number in the 2025 restatement would you need before treating it as a forecast that was scored, not just raised?

**(c) What does ASKB's chat window hold?** About 40m IB chats a day. ASKB reads three months of history (~63 trading days). Bloomberg last stated >350,000 users (Dec 2023). Compute the chats in a full window across all clients, and the average chats per user per day. *(Answer: 40m × 63 ≈ **2.5bn** chats. 40m / 350k ≈ **114** chats per user per day. Users are not chatters, so treat this as an upper bound per seat.)* Explain why that volume is a switching cost no data vendor without a chat network can match.

**(d) Survey error.** In the Apr 2026 poll, 50% of ~100 respondents named hallucination their main concern and 32% picked source attribution as the top confidence factor. Compute an approximate 95% interval for each. *(Answer: 1.96 × √(0.5×0.5/100) ≈ ±**9.8pp**, so 40–60%. For 32%: 1.96 × √(0.32×0.68/100) ≈ ±**9.1pp**, so 23–41%.)* Attribution (32%), error checking (30%) and human oversight (25%) overlap within error. Does the poll really support Bloomberg's ‘attribution first’ design, or only ‘something verifiable’?

---
**Sources (Bloomberg corpus, accessed via `articles.jsonl` 2026-10-25):**
- [Data annotation best practices, 2020-09-24](https://www.bloomberg.com/company/stories/bloombergs-global-data-cto-data-science-teams-publish-best-practices-for-data-annotation-projects/)
- [Ticker Plant, 2022-03-04](https://www.bloomberg.com/company/stories/how-bloomberg-handles-a-massive-wave-of-real-time-market-data-in-microseconds/)
- [BloombergGPT, 2023-03-30](https://www.bloomberg.com/company/press/bloomberggpt-50-billion-parameter-llm-tuned-finance/)
- [Humans in the Loop, 2023-05-11](https://www.bloomberg.com/company/stories/humans-in-the-loop-ai-machine-learning-in-the-bloomberg-terminal/)
- [BI GenAI $1.3tn, 2023-06-01](https://www.bloomberg.com/company/press/generative-ai-to-become-a-1-3-trillion-market-by-2032-research-finds/)
- [Earnings Call Summaries, 2024-01-22](https://www.bloomberg.com/company/press/bloomberg-launches-ai-powered-earnings-call-summaries/)
- [BI GenAI restated, 2024-03-08](https://www.bloomberg.com/professional/insights/data/generative-ai-races-toward-1-3-trillion-in-revenue-by-2032/)
- [GenAI on mobile, 2024-07-29](https://www.bloomberg.com/company/press/bloomberg-releases-gen-ai-enhanced-solution-on-mobile-apps/)
- [Meet the Team: AI Engineering, 2024-07-29](https://www.bloomberg.com/company/stories/meet-the-team-artificial-intelligence-ai-engineering/)
- [News Summaries, 2025-01-15](https://www.bloomberg.com/company/press/bloomberg-launches-gen-ai-summarization-for-news-content/)
- [Envoy AI Gateway, 2025-02-25](https://www.bloomberg.com/company/press/tetrate-and-bloomberg-release-open-source-envoy-ai-gateway-built-on-cncfs-envoy-gateway-project/)
- [Document Insights, 2025-04-07](https://www.prnewswire.com/news-releases/bloomberg-accelerates-financial-analysis-with-gen-ai-document-insights-302421875.html)
- [RAG safety papers, 2025-04-28](https://www.bloomberg.com/company/press/bloomberg-ai-researchers-mitigate-risks-of-unsafe-rag-llms-and-genai-in-finance/)
- [Fixed-income term sheets, 2025-05-29](https://www.bloomberg.com/company/stories/transforming-fixed-income-data-management-with-ai-and-human-expertise/)
- [Document Search & Analysis, 2025-06-16](https://www.bloomberg.com/professional/insights/press-announcement/investors-to-streamline-alpha-generating-research-with-bloombergs-latest-ai-offering/)
- [Bloomberg embraces MCP, 2025-07-14](https://www.bloomberg.com/company/stories/closing-the-agentic-ai-productionization-gap-bloomberg-embraces-mcp/)
- [PORT AI Portfolio Commentary, 2025-09-23](https://www.bloomberg.com/company/press/bloomberg-advances-portfolio-analytics-with-launch-of-ai-portfolio-commentary-in-port-enterprise/)
- [Investment research panel (Jaskoll), 2025-10-30](https://www.bloomberg.com/professional/insights/markets/how-is-investment-research-transformed-by-ai/)
- [BI GenAI $1.8tn, 2025-11-03](https://www.bloomberg.com/professional/insights/artificial-intelligence/inside-ais-rapid-expansion-what-investors-need-to-know/)
- [Expanded news AI, 2025-11-24](https://www.bloomberg.com/company/press/investors-harness-bloombergs-expanded-ai-tools-to-discover-and-summarize-news/)
- [BI European equity trading study: technology, 2025-12-08](https://www.bloomberg.com/professional/insights/trading/european-institutional-equity-trading-study-technology/)
- [European leaders survey, 2025-12-17](https://www.bloomberg.com/company/press/bloomberg-survey-three-quarters-of-european-finance-leaders-fear-losing-market-share-or-becoming-obsolete-without-ai/)
- [Quant research-data survey, 2026-01-22](https://www.prnewswire.com/news-releases/quants-increase-focus-on-sector-specific-data-as-ai-adoption-evolves-bloomberg-research-data-survey-finds-302667587.html)
- [UK AI poll + ASKB beta, 2026-04-21](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-survey-uk-finance-leaders-say-inaccurate-outputs-are-the-biggest-barrier-to-ai-adoption/)
- [Vault BSpeech, 2026-05-14](https://www.prnewswire.com/news-releases/bloomberg-vault-integrates-bspeech-unlocking-multi-language-voice-transcription-capabilities-across-50-languages-for-compliance-professionals-302771957.html)
- [Vault AI surveillance, 2026-08-05](https://www.prnewswire.com/news-releases/bloomberg-vault-introduces-new-ai-powered-communications-surveillance-models-302843724.html)
- [ASKB on mobile, 2026-08-18](https://www.prnewswire.com/news-releases/bloomberg-extends-askb-on-mobile-investment-ideas-dont-stop-when-financial-professionals-leave-the-desk-302853450.html)
- [Enterprise MCP, 2026-09-29](https://www.bloomberg.com/company/press/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications/)
- [BTCA fixed-income TCA, 2026-10-13](https://www.bloomberg.com/professional/insights/financial-services/beyond-the-benchmark-using-advanced-analytics-to-navigate-fixed-income-trading-costs/)
- [ASKB GA, 2026-10-15](https://www.bloomberg.com/professional/insights/press-announcement/the-next-evolution-of-askb-your-insights-bloombergs-intelligence-one-conversation/)
