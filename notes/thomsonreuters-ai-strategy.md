# Note · Thomson Reuters' AI strategy — an incumbent that rents the frontier labs' brains, sells its own content and editors as the trust layer, and has just built a $40M model as a hedge

> Strategy / technology note · Maps to **E10** (Digital & AI Transformation — build/partner/buy, multi-model, agentic, own model), **Course 04** (Competitive Strategy — content moat vs. commoditizing complements, supplier power of model labs), **Course 10** (Entrepreneurship & Venture — buying AI startups, corporate VC), **Course 07** (Data, Analytics & Decision-Making — RAG, evaluation, "verification layer"), **E8** (how AI is told to investors) · Written 2026-10-25 · Part of [[thomsonreuters-hub]]; companions [[thomsonreuters-capital-allocation]] and [[thomsonreuters-mission-forces]]

- **Source:** 77 TR AI and product releases 2019–2026, the Casetext call slides (Jun 2023), the 2021 Investor Day transcript (Wong, Martens, Malhotra on pre-GenAI AI) and every results release from 2023 on (AI spend figures, Reuters AI licensing) — all in `_ingest/raw/thomsonreuters/articles.jsonl`. Every usage and performance figure below is **TR's own claim**. None was independently audited, and most come from TR-run surveys or launch releases. No competitor (Harvey, LexisNexis+ AI, Bloomberg Law) is named anywhere in the AI corpus.
- **Core claim:** TR's AI story has four phases. The constant underneath is a *moat claim*: the model is a commodity, and TR's edge is **1.9B+ authoritative documents, 1.4B KeyCite signals and thousands of attorney editors** that make an answer defensible.
  - **2018–22, machine learning inside products.** Westlaw Edge, then Westlaw Precision, "the largest-ever investment in our editorial operations".
  - **2023, build, partner, buy.** **Casetext, $650M**, whose CoCounsel was "Built on Open AI's GPT-4". AI spend of **$100M+ a year**.
  - **2024–25, a multi-model, agentic platform.** OpenAI, Google and Anthropic models run side by side. Safe Sign and Materia acquired. **$200M+ a year**.
  - **2026, "fiduciary-grade AI".** Next-gen CoCounsel Legal "rebuilt on Anthropic's Claude Agent SDK", CoCounsel served *inside* Claude via MCP, and **"Thomson", TR's own LLM**: open-source base, **$40M**, trained on **under 10%** of TR content so far.
  - Over the same years, the selling point moved from *owning content* to *owning verification* to *owning the model too*. Each move is a response to the same threat: the labs TR rents from can sell to TR's customers directly. TR's results support the strategy so far: Big 3 organic growth went from 7% (2022) to 9–10% (2026). The lab threat is still the one TR never names.

---

## 1. Chronology

| Date | Milestone | TR's numbers |
|---|---|---|
| 2019–20 | Westlaw Edge features (Quick Check, litigation analytics); TR Labs incubator; IBM Watson regulatory partnership | AI/ML "for more than 25 years" (TR, Feb 2020) |
| Mar 16 2021 | Investor Day: content-driven technology company. Wong: "AI models are only as good as the data that trains them." Martens: "It's the highest resolution legal data there is, period." | 1,000+ attorney editors; Edge on >50% of US Westlaw ACV |
| Sep 14 2022 | **Westlaw Precision**: 250+ new attorney editors tagging the law | Research "more than twice as fast" |
| 2022 | ThoughtTrace (contract AI), PLX AI (AI financial news, exclusive to LSEG) | — |
| Apr / Jun 2023 | TR's own surveys: a "trust gap". 82% say GenAI can be applied to legal work; only **4%** use it (Jun) | — |
| May 23 2023 | GenAI vision; Microsoft 365 Copilot plugin; "build, buy and partner" | — |
| Jun 26 → Aug 17 2023 | **Casetext**: $650M cash, ~100 staff, funded from LSEG sales; "$100M+ Organic AI Investment per Year" | CoCounsel "Built on Open AI's GPT-4" |
| Nov 1 / 15 2023 | GenAI strategy: AI-Assisted Research on Westlaw (RAG to stop invented citations); Open Arena internal LLM sandbox; 26,000 staff upskilled | AI spend "more than $100 million" a year |
| Apr 17 2024 | "GenAI assistant for every professional": CoCounsel becomes the umbrella brand (legal, tax, risk, media) | Powered by GPT-4 |
| Aug 12 2024 | **CoCounsel 2.0**, multi-LLM, testing Gemini 1.5 Pro | "more than 1,000 data scientists and AI and machine learning experts" |
| Aug / Oct 2024 | **Safe Sign** (UK legal-LLM startup) and **Materia** (agentic tax/accounting) acquired; prices undisclosed | — |
| Nov 5 / 25 2024 | AI spend "more than $200 million in 2024". Custom OpenAI o1-mini model tested; Claude 3.5 and Gemini evaluated | "1,400% increase in CoCounsel users in less than a year" |
| Jun 2 2025 | **Agentic Intelligence** platform (CoCounsel for tax, audit and accounting) | "20B+ documents, 15+ petabytes", "4,500 subject matter experts and 180+ AI engineers" |
| Aug 5 2025 | **CoCounsel Legal with Deep Research**; Westlaw Advantage; "benchmarked multi-model architecture" | 20,000+ firms and departments |
| Oct–Dec 2025 | $200M+ organic AI spend a year (Ramanathan); OpenAI, Anthropic, Google, Microsoft named as partners; Imperial College frontier-AI lab (5 years, joint foundation-model training) | — |
| Jan 2026 | Trust in AI Alliance (Anthropic, AWS, Google Cloud, OpenAI); 200+ law schools | — |
| **Feb 24 2026** | **One million CoCounsel users** in 107 countries. Notes to editors: "developing a proprietary large language model" | — |
| **May 12 2026** | **Anthropic partnership expanded**: CoCounsel Legal available *inside Claude* via MCP; next-gen CoCounsel Legal "rebuilt on Anthropic's Claude Agent SDK" | 1.9B Westlaw and Practical Law documents; 1.4B KeyCite signals |
| May 27 2026 | **"Fiduciary-Grade AI"** standard: grounded in authority, privacy by architecture, human expertise, transparent reasoning | — |
| Aug 20 2026 | Next-gen CoCounsel Legal goes live (agentic, Claude Agent SDK); planned MCP link to AWS's Amazon Quick | — |
| **Aug 24 2026** | **"Thomson"**: TR's first proprietary LLM. Open-source base; small open-weight version on Hugging Face (non-commercial); CoCounsel "remains multi-model by design" | **$40M** (talent + compute); "less than 10%" of TR content used so far |
| Oct 22 2026 | Next-gen CoCounsel Tax, Audit & Accounting (code execution, MCP) | — |

## 2. The moat argument, as it evolved (verbatim)

| Phase | What TR says the edge is |
|---|---|
| 2021 | Wong: "AI models are only as good as the data that trains them." |
| 2023 | Casetext slides: "Authoritative, Trusted Content", "Subject Matter Expertise", "Distribution Footprint", "World-Class AI Talent" |
| 2024 | Dahn (Westlaw): "When we tried to solve claims research issues with AI alone, it didn’t work very well". The fix was editors writing new content for the AI. |
| 2025 | Wong: "Agentic AI isn’t a marketing buzzword. It’s a new blueprint for how complex work gets done," and "What others are calling agentic, we’ve already had in the market." |
| Feb 2026 | Hasker: "CoCounsel is built for moments when being almost right is not good enough." Release: "Thomson Reuters is not participating in the AI race. It is defining how AI operates in the world's highest-stakes work." |
| May 2026 | Hron: "trust in AI is a property of the system itself, built into the architecture and verifiable at every step" |
| Aug 2026 | "Thomson Reuters is betting the next horizon will be won in the verification layer." … "Now it owns the model too." Hron: "For years, the AI industry has treated scale as the answer: bigger models, more compute, more money." |
| Oct 2026 | Hron, conceding parity on features: "The code execution piece is table stakes now; every company in this space has it." |

**The arc:**
- *Data* (2021) → *data + talent + distribution* (2023) → *agentic workflow* (2025) → *verification and liability* (2026) → *ownership of the model* (Aug 2026).
- Each step narrows what TR claims is uniquely its own.
- Each step also shifts the claim toward something a frontier lab can't easily copy: editor-validated citations, a legal record of every reasoning step, and model weights TR controls.

## 3. The economics (what the releases show)

- **Spend:** "$100M+" a year (2023) → "more than $200 million in 2024" → "$200 million annually over the next few years" (2025). Accrued capex rose to ~8% of revenue from 2023, which TR attributes partly to AI.
- **Growth it coincides with:**
  - Big 3 organic growth: 7% (2022–23) → 9% (2024–25) → 9–10% (2026 guide).
  - Total organic: 6% → 7% → ~8%.
  - Legal segment margin: ~47–48%.
  - TR attributes Q3 2025 growth to "the impact of our agentic AI solutions like CoCounsel Legal and CoCounsel for tax, audit and accounting" (Hasker, Nov 4 2025).
- **The model bill vs. owning one:** the "Thomson" release says frontier labs "have typically spent billions of dollars on compute". TR spent $40M by "starting from a strong open-source foundation". The pitch is inference cost and control ("without the heavy inference costs of typical frontier models"), not raw capability. Academic testers said its citations were "generally competitive with leading frontier models".
- **Reuters' side door:** in 2023–24 Reuters sold content to AI developers. That was "Generative AI related content licensing revenue that was largely transactional in nature". It lifted Reuters to +17% organic in Q1 2024, then reversed to −7% in Q1 2025. TR's content was briefly a *supplier* to the labs it competes with.

## 4. What the claims don't prove

1. **Usage ≠ revenue.** "One million professionals" and "1,400% increase in CoCounsel users" are seat or user counts. TR never discloses CoCounsel revenue, price, attach rate or churn. Casetext's revenue was never given, even at acquisition.
2. **Every benchmark is TR-run or TR-selected.** "Twice as fast" (Precision), "as much as 60% of the time" (UK launch) and "on par with the latest frontier models" (Thomson) come from internal or partner evaluations. The academic testers quoted on Thomson were TR's chosen evaluators. One of them noted that in one test all three models answered correctly.
3. **Expert and engineer counts don't reconcile across releases:** 1,000+ data scientists (2024) vs. 180+ AI engineers (2025); 4,500 vs. 2,600 domain experts (2025 vs. 2026). Treat them as marketing ranges.
4. **"Fiduciary-grade" is TR's own trademark-style standard** ("Fiduciary-Grade AI™"), defined by TR and graded by TR. No regulator, bar association or court uses the term in the corpus.
5. **Multi-model is both a hedge and a dependency.** "Partnering with leading LLM providers is a key part of our strategy" (Wong, 2024) and "rebuilt on Anthropic's Claude Agent SDK" (2026) both say the reasoning engine is someone else's. Thomson is so far deployed in one feature (Tabular Analysis).

## 5. Strategic read (inference — not TR's words)

- **Complement-commoditization in reverse.** The classic play is to make your complement cheap. TR's problem is that *it* might become the complement: the content and tool layer behind a Claude, ChatGPT or Copilot interface. The May 2026 MCP deal is the clearest sign. TR chose to be **inside Claude** rather than keep users only in TR's own interface. That trade buys reach and gives up the interface.
- **Why build "Thomson" at all?** There are three reasons, in order of weight:
  1. **Supplier power.** With three lab suppliers who are also potential competitors, owning a capable fallback model caps their pricing power and protects margins.
  2. **Inference cost** in high-volume workflows: tabular review and bulk document review.
  3. **Sovereignty and privacy** ("sovereign AI options to come"), which suit government and non-US customers.

  At $40M it is an option, not a bet. It is ~2% of one year's FCF (derived).
- **Why not buy bigger?** TR returned ~$10B to holders during 2022–26 and paid $650M for its biggest AI deal (see [[thomsonreuters-capital-allocation]]). Its implicit bet is that **the scarce asset is verified content, not the model**. If that's right, renting models and returning cash beats buying an AI company at peak prices. If it's wrong, TR will have funded its competitors' customers' adoption.
- **The real moat may be liability, not content.** "Almost right is not good enough" turns professional malpractice risk into a buying criterion. A lawyer who cites a hallucinated case faces sanctions. A tool that ties every claim to KeyCite-validated authority sells insurance as much as productivity. That is Christensen's sustaining-innovation logic: the incumbent wins where the top of the market pays for reliability.
- **Where the risk is concentrated:** legal research. Westlaw's "premium" (2021) depended on editors tagging the law. If frontier models plus public case law get "good enough" for the middle market, the price umbrella over Westlaw shrinks from below. TR's own surveys show midsize and small firms gaining share ([[thomsonreuters-mission-forces]]).

## 6. Canon lenses

- **Innovator's dilemma** ([[canon-christensen-innovators-dilemma]]): GenAI started as a *sustaining* innovation for TR (better Westlaw), and that's how TR frames it. The disruptive version would be "good enough" AI legal research sold cheaply to small firms and consumers by a lab. TR's answer is to move up-market ("fiduciary-grade") and down-market through partners (CoCounsel in Claude) at the same time.
- **Cornered resource and counter-positioning** ([[canon-helmer-7-powers]]): TR's cornered resource is the editorial corpus (the West Key Number System, KeyCite, 2,600+ experts). Counter-positioning cuts against TR. A lab can price AI legal research per token, and TR, with a Westlaw subscription franchise, would be slow to copy that.
- **Information goods economics** ([[canon-shapiro-varian-information-rules]]): high fixed cost and near-zero marginal cost. Versioning ("CoCounsel Core" vs. full) and lock-in through integration into Word, Teams and Claude are textbook moves. The labs bring the same economics with larger fixed costs.
- **Supplier power** ([[canon-porter-competitive-strategy]]): the frontier labs are concentrated suppliers of a key input and possible forward integrators. TR's response follows Porter: multi-sourcing (multi-model), a backward-integration option (Thomson) and switching-cost reduction (MCP standard).
- **Platform position** ([[canon-parker-platform-revolution]]): putting CoCounsel inside Claude is a bet on being a complement to a platform rather than being the platform.

## 7. Practitioner counterpoint

- **For TR:**
  - Growth accelerated as AI shipped.
  - TR's customers are risk-averse professionals who buy on trust. An AI-native competitor can't buy 150 years of editorial classification.
  - The partner strategy gave TR the best models at each moment without picking a winner.
  - Its acquisitions (Casetext in 2023) put it in production ~2 years before most incumbents.
- **Against TR:**
  - TR doesn't control the engine.
  - Its moat claim keeps narrowing.
  - It still hasn't shown monetization data.
  - The frontier labs are now selling directly to law firms. The corpus never mentions this, which is itself a tell.
  - Hron's "table stakes" line concedes that features don't differentiate.
  - If verification becomes a standard API (citations plus validation), the remaining moat is the editorial corpus, which is exactly the asset Reuters was *licensing to AI developers* in 2024.
- **Synthesis:** TR has executed the incumbent playbook well and early. The test is margin, not adoption. Legal's ~47–48% margin has to hold while TR pays lab suppliers and prices against AI-native rivals.

## 8. Open questions

1. CoCounsel revenue, ARPU and gross margin after model costs. Will TR ever disclose them?
2. Thomson's adoption path: from one feature (Tabular Analysis) to the default model inside CoCounsel? And at what quality bar?
3. Terms of the Anthropic relationship: exclusivity, revenue share, data use.
4. Does Reuters resume AI content licensing, and to whom?
5. How do law firms' own AI programs (in-house builds, direct lab contracts) change TR's pricing power by 2028?

**Links:** [[thomsonreuters-hub]] · [[thomsonreuters-capital-allocation]] · [[thomsonreuters-change-program]] · [[thomsonreuters-people]] · [[thomsonreuters-mission-forces]] · [[thomsonreuters-outside-voices]] · [[tradeweb-tech-ai-data]] (a venue's version of *data is the moat*) · [[tradeweb-ai-price]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[lseg-hub]] · [[wss-ai-economics]] · [[canon-christensen-innovators-dilemma]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-porter-competitive-strategy]] · [[canon-parker-platform-revolution]]

---
### Rep
Using this note's numbers:
(a) TR spent ~$200M a year on AI in 2024–25 and paid $650M for Casetext. Express the Thomson model's $40M as a share of one year's AI spend, and the Casetext price as years of organic AI spend.
(b) Suppose CoCounsel's one million users paid an average of $1,000 a year (a hypothetical, not TR's figure). Compare that revenue with TR's 2025 revenue of $7,476M. Then list the three disclosures you'd need to replace the hypothetical.
(c) Write a five-sentence memo to Hasker arguing *either* for or against a $3B+ AI acquisition in 2027, using the leverage figures in [[thomsonreuters-capital-allocation]] §5.

*Answers for (a)/(b):* (a) $40M / $200M = **20%** of one year's AI spend; $650M / $200M ≈ **3.3 years** of spend. (b) 1M × $1,000 = $1.0B ≈ **13%** of 2025 revenue. You'd need CoCounsel revenue (or ARPU), paid vs. free/trial seats, and overlap with existing Westlaw/Checkpoint subscriptions (how much is new money vs. repackaged).

**Sources (thomsonreuters.com press releases unless noted):**
[2021 Investor Day transcript, Mar 16 2021](https://ir.thomsonreuters.com/static-files/d7d038bf-b689-4db3-abd6-c124f66ad807) · [Westlaw Precision, Sep 14 2022](https://www.thomsonreuters.com/en/press-releases/2022/september/thomson-reuters-debuts-westlaw-precision) · [GenAI vision, May 23 2023](https://www.thomsonreuters.com/en/press-releases/2023/may/thomson-reuters-brings-forward-vision-to-redefine-the-future-of-professionals-with-content-driven-ai-technology) · [Casetext deal, Jun 26 2023](https://www.thomsonreuters.com/en/press-releases/2023/june/thomson-reuters-corporation-signs-definitive-agreement-to-acquire-casetext) · [Casetext call slides](https://ir.thomsonreuters.com/static-files/720c4c28-cbe7-458c-937d-8dadb1de2e10) · [GenAI strategy, Nov 1 2023](https://www.thomsonreuters.com/en/press-releases/2023/november/thomson-reuters-unveils-generative-ai-strategy-designed-to-transform-the-future-of-professionals) · [CoCounsel 2.0, Aug 12 2024](https://www.thomsonreuters.com/en/press-releases/2024/august/thomson-reuters-unveils-cocounsel-2-0) · [Q3 2024 results, Nov 5 2024](https://www.thomsonreuters.com/en/press-releases/2024/november/thomson-reuters-reports-third-quarter-2024-results) · [Custom OpenAI model, Nov 25 2024](https://www.thomsonreuters.com/en/press-releases/2024/november/thomson-reuters-cocounsel-tests-custom-llm-from-openai-broadening-its-multi-model-product-strategy) · [Agentic Intelligence, Jun 2 2025](https://www.thomsonreuters.com/en/press-releases/2025/may/thomson-reuters-ushers-in-the-next-era-of-ai-with-launch-of-agentic-intelligence) · [One million users, Feb 24 2026](https://www.thomsonreuters.com/en/press-releases/2026/february/one-million-professionals-turn-to-cocounsel-as-thomson-reuters-scales-ai-for-regulated-industries) · [Anthropic partnership, May 12 2026](https://www.thomsonreuters.com/en/press-releases/2026/may/thomson-reuters-and-anthropic-expand-partnership-to-connect-claude-with-cocounsel-legal) · [Fiduciary-grade standard, May 27 2026](https://www.thomsonreuters.com/en/press-releases/2026/may/thomson-reuters-standard-for-high-stakes-ai) · [Next-gen CoCounsel Legal, Aug 20 2026](https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-launches-next-generation-of-cocounsel-legal-the-ai-ecosystem-built-for-legal-professionals) · [Thomson LLM, Aug 24 2026](https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-leverages-its-world-class-data-assets-to-launch-its-own-frontier-model) · [CoCounsel Tax, Audit & Accounting, Oct 21 2026](https://www.thomsonreuters.com/en/press-releases/2026/october/thomson-reuters-launches-ai-for-tax-and-audit-that-knows-the-answer-and-why-it-is-right)
