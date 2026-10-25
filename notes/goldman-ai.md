# Note · Goldman Sachs AI — developers and back office first, redeployment instead of cuts, a deliberately modest 'OneGS 3.0', and a bank that stages the AI debate while earning fees from the boom

> Technology-strategy / org note · Maps to **E10** (Digital & AI Transformation for Leaders — sequencing use cases, build vs buy, expectation management), **Course 07** (Data, Analytics & Decision-Making — grounding, provenance, forecast accountability), **Course 09** (Leadership & Organizational Behavior — change management, apprenticeship, the 'no job apocalypse' promise), with touches of **E5** (Transformation at Scale) and **E8** (how the story is told to investors) · Written 2026-10-25 · Companion to [[goldman-hub]], [[goldman-awm-private-credit]], [[goldman-markets-platforms]], [[wss-ai-economics]], [[tradeweb-tech-ai-data]], [[tradeweb-ai-price]]

- **Source:** Goldman Sachs corpus (`_ingest/raw/goldman/articles.jsonl`), **~35 items, Sep 12 2019 – Sep 8 2026**: 9 hiring/office releases (Argenti/Lahtiranta, Melissa Goldman, Marcu, Vemulapalli, Kotsovinos, Keswani, Leslie as CAO, Bellevue), the 2023–2025 shareholder letters and the Investor Day 2020 deck, 7 Argenti articles, Solomon's *Exchanges* episodes (Feb 2023, Jan 2024, Jan 2025, Jan 2026), the *AI Exchanges* series (Lee/Posnett, Argenti, Osman Ali, Churchman), the Jun 2024 *Top of Mind* skeptic issue and its podcast (Covello, Acemoglu), Griffin at Apex (Jul 2026) and the AI-debt credit episode (Aug 2026). Reader maps: `reader-notes/notes-E1.md`, `notes-E2.md`, `notes-A.md`, `notes-C.md`. **All of it is Goldman's own channel**: the skeptics are GS's own Head of Equity Research and guests GS invited. **Missing:** any adoption metric (users, prompts, tickets), any cost or savings figure for the AI programme, headcount by function, Marquee usage or revenue, earnings-call Q&A, and any account from staff or clients. **Date quirks:** the Feb 2023 Sheridan/Rangan page blurb gives two wrong dates (the transcript says recorded Feb 13 2023); the 2024 letter is dated 2024-12-31 but was published in spring 2025, after the GS AI Assistant launch; podcasts are typically published 2–20 days after recording.
- **Core claim:** Goldman's AI programme is narrower and more conventional than its labels. It started where outputs are **verifiable** (code: "pretty much every developer" has AI in the IDE by Mar 2025), went firmwide as a chat layer (the **GS AI Assistant**, announced on *AI Exchanges* in Jan 2025), and is now aimed at **six back-office workstreams**, starting with **client onboarding/KYC** (OneGS 3.0, 2025 letter). Solomon frames OneGS 3.0 as smaller than it sounds ("narrower than that grand vision of reimagining the firm") and promises **redeployment, not cuts**: the engineer count reads **~12,000 in Jan 2025 and "over 12,000" in Sep 2026**, about a quarter of staff, as it was in 2019. The talent model is to **hire senior builders from Big Tech** (AWS, Amazon AGI, Google ×2, AMD) and open an office in **Bellevue** next to them. Meanwhile GS **publishes its own AI bull-vs-bear debate** — Lee, Rangan, Sheridan and Briggs against Covello and Acemoglu — while earning advisory, underwriting and trading fees from the capex boom (AI ~**18% of 2026 IG supply**). Two GS voices add the sharpest operating lessons: **Osman Ali** (LLM herding may make markets *less* efficient) and **Chris Churchman** (Marquee AI: "a demo is judged on its best day, whereas a product is judged on its worst day").

---

## 1. Chronology — Argenti's arc and the firm's

| Date | Event / statement | Detail |
|---|---|---|
| Sep 12 2019 | **Marco Argenti** joins as co-CIO from AWS (with co-CIO George Lee); **Atte Lahtiranta** CTO from Verizon Media | Remit is cloud, core engineering, platforms: "digital platforms that seamlessly integrate execution, analytics and content will increasingly define how our clients choose to transact" |
| Oct 2019 | Solomon: "more than 25 percent of the people who work here are engineers" | — |
| Jan 29 2020 | **Investor Day**: Argenti and Stephanie Cohen present *Innovation* ("Simplify the complex services we provide to clients into component pieces"); **9K+ engineers**; $4bn 2019 engineering spend (~53% run, ~47% change) | AI is not a theme yet; platforms and APIs are |
| Feb 2023 | Solomon: "we're still in the early stage of testing" | Rangan (Research): "We'll all have copilots." |
| Apr 18 2023 | Argenti (London): "The revolution here is the revolution of knowledge," | Printing-press analogy |
| May 22 2023 | **AI Forward** with SV Angel (~400 attendees). Argenti: "We need to think as big as we can…before AI thinks bigger than we do." | Billed as sole CIO by now |
| Dec 21 2023 | Argenti's 2024 predictions: hybrid AI, RAG plus prompting matching fine-tuned models in most use cases, capital shifting to the application layer | "Everyone I speak with has ROI in mind as almost the first-order priority." |
| 2023 letter | Solomon cites McKinsey's 20–45% developer-productivity range, then: adoption "will lag" | "There’s no question that generative AI is going to disrupt a wide range of industries. But I believe it’s important to keep perspective." |
| Jan 2024 | Solomon: "Euphoria cools. But that has nothing to do with the efficacy of the technology" | GS has picked "a narrow set of use cases that we can really execute on" |
| Jun 25 2024 | *Top of Mind* #129, *Gen AI: too much spend, too little benefit?* | Covello and Acemoglu vs Briggs, Rangan, Sheridan |
| Oct 7 2024 | **Melissa Goldman** rejoins from Google as head of Technology Engineering for GBM | — |
| 2024 letter | Three-year efficiency programme "including through the use of artificial intelligence solutions"; tools named: "a developer copilot coding assistant, our natural-language GS AI assistant" | Efficiencies "will allow us to further invest for growth" |
| Jan 9 2025 | Argenti's 2025 predictions | "The first AI “layoffs” could eventually emerge, in which AI models will be replaced by better AI tools or humans…" |
| Jan 27–29 2025 | Solomon (DeepSeek week): compute "very expensive"; engineering productivity is "the most obvious" use; "we have 12,000 engineers in our organization" of 46–47,000. **GS AI Assistant** announced by Lee on the first *AI Exchanges* (published Feb 4) | See §2 |
| Mar 6 2025 (pub. Mar 25) | Argenti on *AI Exchanges*: developers are "the first area that in Goldman has gained real traction"; AI Assistant "really like your desktop for AI"; "we are all pretty much AI illiterate" | Wants AI "as natural as Google" for every employee |
| Mar 17 2025 | **Daniel Marcu** from Amazon AGI as Global Head of AI Engineering and Science | Mandate: "productivity and efficiency" |
| Jul 9 2025 | Argenti's *Fortune* op-ed on AI natives and supervising agents | "The failure mode here is not technological, it’s organizational." |
| Oct 2025 | Argenti: verifiability is the bottleneck (the 'hot and cold' analogy); "We are looking at every single process in the firm right now…" Q3 results: "operate more efficiently… helped by new AI technologies" | — |
| 2025 letter | **OneGS 3.0** launched, "our new operating model propelled by AI"; six workstreams: "client onboarding/KYC, vendor management, regulatory reporting, lending, enterprise risk management, and sales enablement" | Gains to be re-invested |
| Jan 20 2026 (pub. Jan 23) | Solomon resets expectations: OneGS 3.0 is "narrower than that grand vision"; KYC/onboarding first; "I'm not in the job apocalypse camp." | "Changing processes in a big enterprise is hard work." |
| Jan 22 2026 | Argenti's 2026 predictions: models as the new operating system, agents priced in tokens, the 'gigawatt ceiling' | "As a result, those who own the models will own the new operating systems that power AI agents." |
| Apr 6 2026 | **Archana Vemulapalli** from AMD (ex-AWS, IBM) as Global Head of AI Product Management and Strategic Relations | Leads engagement "with frontier AI labs and AI application providers" |
| May 5 2026 | **Ericka Leslie** becomes CAO to drive OneGS 3.0 | The operating overhaul gets an owner on the Management Committee |
| Jul 6 2026 | **Evan Kotsovinos** from Google (privacy, safety, security; AI safety) as head of AWM Engineering | — |
| Aug 2026 | Churchman on **Marquee AI**, "only available internally right now" | §4 |
| Sep 3 2026 | **Dinesh Keswani** (Nomura CTOO; earlier HSBC, Microsoft, GoDaddy) as co-head and CTO of The Core Engineering | A bank CTO, not Big Tech, for the back-office core OneGS 3.0 targets |
| Sep 8 2026 | **Bellevue** engineering office, >125 seats for AI and cloud; "over 12,000 engineers… roughly one-quarter" of staff | "we know our people are still this firm’s greatest asset" |

**Argenti's arc in one line:** platform engineer (2019) → knowledge-revolution evangelist (2023) → change-management realist (2025: "AI illiterate", "mindful disruptors") → process redesigner (late 2025: make processes machine-verifiable) → industry forecaster (2026: models as the OS, power as the limit). The constant is grounding and human judgement in the loop.

## 2. The GS AI Assistant and the 12,000 engineers

- **Launch.** Lee, recorded Jan 29 2025: "We launched our GS AI Assistant which allows more people across the firm to get access to leading-edge models" and "AI is, in many ways, prolific throughout the firm, but this is the broadest and most general purpose offering we've made." He says it is built to be "safer, more reliable, and more compliant" as befits a regulated institution. By March Argenti says GS is "deploying at scale" what is "really like your desktop for AI."
- **What it is:** a firm-wrapped interface to third-party frontier models, grounded on GS content. Named live uses (Argenti, Mar 2025): drafting research, PWM portfolio summaries with a 'Goldman lens', a translation tool tuned to GS jargon.
- **What isn't disclosed:** user counts, usage, models used, cost, or any productivity number.
- **Engineers as the first target.** Solomon (Jan 2025): "We would have more if we weren't constrained by our desire to drive returns in our business." The logic: if AI raises output per engineer, GS gets the capacity of more engineers without the cost.

| Engineer headcount | Source |
|---|---|
| ">25 percent" of staff (~2019) | Solomon, Oct 2019 |
| **9K+** | Investor Day, Jan 2020 |
| **12,000** of 46–47,000 (~26%, *derived*) | Solomon, Jan 2025 |
| **"over 12,000"**, ~one-quarter | Bellevue release, Sep 2026 |

**Read:** a flat engineer count during the AI rollout supports Solomon's *redeploy* message. It also means any productivity gain shows up as more output per engineer, which the corpus never measures *(inference)*.

## 3. Hires from Big Tech

| Year | Hire | From | Role |
|---|---|---|---|
| 2019 | Marco Argenti | AWS (VP Technology) | Co-CIO → CIO |
| 2019 | Atte Lahtiranta | Verizon Media | CTO |
| 2024 | Melissa Goldman | Google (corporate engineering); ex-JPMorgan | GBM Technology Engineering |
| 2025 | Daniel Marcu | Amazon AGI | Global Head of AI Engineering and Science |
| 2026 | Archana Vemulapalli | AMD; ex-AWS, IBM | Global Head of AI Product Management and Strategic Relations |
| 2026 | Evan Kotsovinos | Google (privacy, safety, security) | Head of AWM Engineering |
| 2026 | Dinesh Keswani | Nomura; ex-HSBC, Microsoft | Co-head / CTO, The Core Engineering |
| 2026 | Bellevue office | Next to the Amazon and Microsoft talent pool | >125 AI and cloud seats |

**Read** *(inference)*: GS hires leaders from the firms that build the models and the cloud, and mostly the *enterprise* side of them (AWS product, Google corporate engineering, AMD enterprise AI), not research scientists. Vemulapalli's job is **vendor management with frontier labs**: GS is a buyer and integrator, not a model builder. Kotsovinos's AI-safety background in AWM signals that client-facing AI in wealth is a governance problem first. Keswani is the exception that proves the rule: the Core (back office) gets a bank CTO.

## 4. Marquee AI — the build lessons

Chris Churchman (Head of Marquee; co-chair of the GBM AI Working Group), with George Lee and Allison Nathan, Aug 2026:
- **What it does:** "Marquee AI, which is only available internally right now," breaks a question into research topics, pulls GS research, trading-floor commentary and Market View widgets ("like Pinterest for capital markets"; "millions" of expert-built widgets on vendor data), and returns sentence-level grounded answers. Lee says the plan is to "ultimately extend it to clients."
- **The paradigm:** "we've gone from a world where users learn software to where software learns users."
- **Build waste:** embedding pipelines and chunking became "pointless" when context windows grew to 128,000 and then a million tokens. Lesson: "Don't bet against the model, basically. That's the key."
- **Reliability:** a system right 90% of the time forces the user to check every fact; a web-grounded model admitted "I'm better at sounding thorough than being thorough." So the firm builds its own grounding framework.
- **Product standard:** "But like a demo is judged on its best day, whereas a product is judged on its worst day, right?"
- **The next frontier:** prompt → context → agentic → environment engineering → *mandate engineering*: what agents may do "under whose authority, in whose name". Autonomy grows "once there's an insurance market or a liability market" for agents. He flags security with "Recent headlines notwithstanding."
- **The people risk:** "there's a huge danger here that in the era of AI, we outsource our reasoning to these models, and we have cognitive atrophy". Automating the junior trader's price request may thin the pipeline of seniors who understand pricing.

**Compare Tradeweb** ([[tradeweb-tech-ai-data]]): Tradeweb launched **TARA**, a client-facing AI research assistant for credit traders, in Jun 2026, while Marquee AI was still internal in Aug 2026. The venue ships to clients first; the dealer keeps it inside until provenance is solid *(inference)*. Both are fighting for the same buy-side screen ([[tradeweb-ai-price]]).

## 5. Markets: compute, efficiency and AI debt

- **Market makers' compute (Griffin, Jun 2026).** Transformer models improved Citadel's ability "to both price and manage risk"; large market makers are "spending today hundreds of millions of dollars on compute", and "people who have lower margin businesses won't be able to bear that cost impact." An agentic system cut paper replication from **six to eight weeks to two to three hours**, with "no reduction to headcount at Citadel". He teases: "We do summarize Goldman Sachs' research, I'm sorry to say." **Implication** *(inference)*: compute is a new fixed cost that concentrates liquidity provision among the largest firms, GS among them.
- **AI may make markets less efficient (Osman Ali, GSAM QIS, May 2026).** LLMs spread price discovery into small caps and EM, but "these models, again, in the hands of the average person will create herd behavior", making markets "probably less efficient and more predictable". Ali says "more than 50% of what we think drives the stock's return over the next 12 months is not the fundamentals of the business." The QIS team is "about a 100 person team", roughly unchanged, while using small fine-tuned models. Lee calls the thesis counter-consensus.
- **AI debt in the IG market (Lynam and Ablon, Aug 2026).** Nearly **$500bn** of AI-related debt issued in 2026 to date; hyperscalers **$194bn** vs **$108bn** in all of 2025 (only ~40% of the AI total). AI share of IG supply: **$10bn / 1% (2024) → $108bn / ~7% (2025) → ~18% (2026)**. 40% of 15-year-plus IG issuance is AI-linked; **Amazon is now the largest duration weight** in the IG index (from #20), Google #18 (from #86). Debt funds 27% of hyperscaler capex in 2025, ~one-third in 2026, a **35% peak in 2027**. The AI leader basket widened from 74bp tights to nearly twice that. The binding constraint is investors' concentration limits: the largest US bank issuers each have under $175bn of index debt and under 2.3% of the index.

## 6. The staged debate — and the fees

| Side | Voice | Claim | Line |
|---|---|---|---|
| Bull | **George Lee** (ex-CIO; GS Global Institute) | DeepSeek-style cost collapse plus Jevons paradox means more use; firms must invest despite unclear ROI | "I think this answers some of Jim's principal concerns. Not all of them but some of them." |
| Bull | **Kash Rangan, Eric Sheridan** (Research) | Infrastructure first, then platforms, then apps; capex in line with past cycles | "Spending is certainly high today in absolute dollar terms. But this capex cycle seems more promising than even previous capex cycles." |
| Bull | **Joseph Briggs** (economics) | Gen AI automates 25% of tasks; +9% productivity and +6.1% GDP over a decade | — |
| Bear | **Jim Covello** (GS Head of Global Equity Research) | An expensive technology replacing cheap labour; Nvidia as a single-supplier choke point; gains competed away | "So, the crucial question is: What $1tn problem will AI solve?" · "we’ve found that AI can update historical data in our company models more quickly than doing so manually, but at six times the cost." |
| Bear | **Daron Acemoglu** (MIT) | ~4.6% of tasks cost-effectively automated in 10 years; ~0.5% productivity and ~0.9–1% GDP | "But that impact is not a law of nature." |
| Practitioner-skeptic | **Ken Griffin** (Citadel) | AI is powerful, but CEOs' productivity stories at one dinner were about ML, optimisation and digitisation | "Not one involved AI." |
| Macro | **Jan Hatzius** (Chief Economist) | +1.5pp a year productivity; 6–7% of employment displaced over time | "The really important point to keep in mind is that disruption tends not to be a linear process." |

**The fee side of the same firm:** Solomon on the Industry Ventures close: "Technology and AI-led innovation should be a catalyst for significant capital markets activity in 2026". Posnett (Jan 2025) expects more AI-driven strategic M&A; Gutman (Mar 2026): AI is "driving a view that scale is critical". The credit desk sells AI-leader baskets and underwrites the hyperscaler bonds at ~18% of IG supply. Even Covello advised staying long the infrastructure trade because "bubbles take a long time to burst" (paraphrase).

**Read** *(inference)*: publishing both sides is good research practice and good business. GS's research credibility rises with the visible bear; its banking franchise earns on the capex either way; and its internal programme is sized cautiously, as the bear would want. The hedge is coherent. What it never does is score the debate: Covello's Jun 2024 window of 12–18 months for compelling use cases closed by end-2025 with spending still rising, and no GS item says who was right.

## 7. What the claims don't prove

1. **No adoption or savings metric exists in the corpus.** 'Every developer' and 'at scale' are not numbers. The McKinsey 20–45% figure Solomon cited is a forecast about other firms.
2. **Flat headcount is consistent with two stories:** redeployment to growth, or attrition-led shrinkage in targeted functions offset by hiring elsewhere. Function-level headcount (KYC, operations) would tell them apart, and it isn't disclosed.
3. **OneGS 3.0's six workstreams have no stated targets** in the corpus: Solomon says there are goals on efficiency, automation, client and employee experience, but none is quantified.
4. **Marquee AI is internal and unmeasured.** 'It doesn't hallucinate' is followed immediately by a hypothetical 90% example; no accuracy or usage data is given.
5. **The bull-bear debate is curated.** Both sides speak on GS channels with GS hosts; no outside bull or bear of GS's *own* AI programme appears.
6. **Research forecasts move.** Data-centre power demand was raised from +165% to +175% by 2030; the AI-debt share forecasts are estimates, not outcomes.

## 8. Strategic read *(inference)*

- **Sequencing by verifiability is the right call.** Code compiles or fails; KYC files pass or fail review. Argenti's 'hot and cold' framing explains why GS started there and why judgement-heavy work (pricing, advice) comes later. This matches the maker/checker/signer chain Jung Min says agents will take over.
- **The promise of no cuts is also a retention device.** Talent competition with Big Tech is acute (§3). Telling 12,000 engineers that AI makes them more valuable, not redundant, protects the hiring pipeline.
- **The narrow label protects credibility.** After the consumer reversal ([[goldman-consumer-retreat]]), Solomon under-promises. If OneGS 3.0 produces savings, they will look like upside.
- **The moat is context, not models.** GS buys models (Vemulapalli's lab relationships) and builds what models can't learn: entitlements, mandates, proprietary data, and the right to stand behind an answer. Churchman's "mandate engineering" is a regulated bank's comparative advantage.
- **Compute favours the big.** Griffin's point applies to GS's market making: rising compute cost is a scale barrier that hurts smaller dealers more ([[goldman-markets-platforms]]).
- **AI risk sits in other books too.** The same software borrowers AI threatens sit in private-credit portfolios ([[goldman-awm-private-credit]]), and the same hyperscaler bonds sit in IG indices.

## 9. Canon lenses

- **Change management** ([[canon-kotter-leading-change]]): Argenti's "mindful disruptors" are a guiding coalition; Solomon's "hard work" is Kotter's warning about declaring victory early.
- **Disruption from below** ([[canon-christensen-innovators-dilemma]]): Lee's 'faster horses versus the automobile' worry is the incumbent's dilemma. GS chooses sustaining uses (developer productivity, KYC) over business-model change.
- **Build-measure-learn** ([[canon-ries-lean-startup]]): Churchman's demo-vs-product line and the wasted RAG work are lean lessons, minus the measurement GS doesn't publish.
- **Forecast accountability** ([[canon-tetlock-superforecasting]]): Covello's 12–18-month window, Sheridan's 6–18 months and Lee's 'deploy and scale' 2025 were checkable forecasts that nobody scored.
- **System effects and herding** ([[canon-jervis-system-effects]]): Ali's thesis is a system effect — individually rational use of the same models produces collective predictability.
- **Information economics** ([[canon-shapiro-varian-information-rules]]): Marquee's widgets and GS research are information goods; an AI layer raises their value only if provenance survives.
- **Scale economies** ([[canon-helmer-7-powers]]): compute as a fixed cost turns AI into a scale power in market making.

## 10. Practitioner counterpoint

- **Bull:** GS sequenced AI sensibly, hired real builders, kept engineers, set a modest public bar and put a CAO in charge of the operating change. It earns from the boom whatever the ROI turns out to be, and its research brand gained from hosting the most-cited AI skeptic.
- **Skeptic:** six years after hiring an AWS executive, GS can't give one number on what AI has saved, how many people use it, or what Marquee earns. 'Narrower than the grand vision' can be an honest reset or a pre-emptive excuse. The debate it stages is free advertising for both its research and its underwriting.
- **Synthesis:** judge GS on OneGS 3.0's first disclosed metric, most likely KYC/onboarding cycle time or cost, and on whether Marquee AI reaches clients with grounding intact.

## 11. Open questions to track

1. Any quantified OneGS 3.0 target or result (cost, cycle time, headcount by workstream), now owned by CAO Leslie.
2. GS AI Assistant usage and the models behind it; how Vemulapalli's lab relationships are structured.
3. Marquee AI's client launch, pricing, and accuracy disclosure vs Tradeweb's TARA.
4. Engineer count and non-engineer headcount in 2027: does 'redeploy' hold?
5. AI share of IG supply after the 2027 peak in debt-financed capex; AI leader basket spreads.
6. Whether Ali's herding factor shows up in QIS performance.
7. A Research follow-up that scores Covello's 2024 call.

**Links:** [[goldman-hub]] · [[goldman-awm-private-credit]] (AI-exposed software loans; AI as deal catalyst) · [[goldman-markets-platforms]] (Marquee, market making, compute) · [[goldman-one-gs-culture]] (OneGS 3.0 as the next One GS) · [[goldman-people]] · [[goldman-outside-voices]] · [[goldman-consumer-retreat]] · [[wss-ai-economics]] (capex financing, power, valuation) · [[tradeweb-tech-ai-data]] (AiEX, TARA, automation as product) · [[tradeweb-ai-price]] (pricing models and data economics) · [[wss-credit-distressed]] · [[canon-kotter-leading-change]] · [[canon-christensen-innovators-dilemma]] · [[canon-ries-lean-startup]] · [[canon-tetlock-superforecasting]] · [[canon-jervis-system-effects]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]]

---
### Rep
Using only this note's numbers:
(a) **Engineer share.** Compute engineers as a share of staff in Jan 2025 (12,000 of 46–47,000). If GS kept headcount flat and AI raised engineering output by McKinsey's 20–45%, how many engineer-equivalents of extra capacity is that?
(b) **Griffin's ratio.** Six to eight weeks of a researcher's time (assume 40 hours a week) became two to three hours. What is the range of the time-reduction ratio?
(c) **Hyperscaler capex from the debt numbers.** 2025 hyperscaler issuance was $108bn and funded 27% of capex. What capex does that imply? If 2026 issuance ends at one-third of capex and capex is $600bn, how much more must they issue after the $194bn already done?
(d) **Judgement.** As the CAO running OneGS 3.0, choose the one metric you would publish for the KYC/onboarding workstream in the first year, and say how you would prevent it from being gamed.

*Answers for (a)–(c):* (a) 12,000 / 46,500 ≈ **25.8%**; 12,000 × 0.20–0.45 = **2,400–5,400** engineer-equivalents, which is why Solomon calls engineering the "most obvious" use. (b) 6 × 40 = 240 hours ÷ 3 = **80×** at the low end; 8 × 40 = 320 hours ÷ 2 = **160×** at the high end. (c) $108bn ÷ 0.27 ≈ **$400bn** of 2025 capex *(derived)*; one-third of $600bn = $200bn, so **~$6bn** more after $194bn (the $600bn figure is a hypothetical for the exercise, not from GS).

**Sources (goldmansachs.com, via `_ingest/raw/goldman/articles.jsonl`):**
[Argenti/Lahtiranta hire, Sep 12 2019](https://www.goldmansachs.com/pressroom/press-releases/2019/marco-argenti-atte-lahtiranta-join-goldman-sachs) · [Solomon year two, Oct 1 2019](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/09-23-2019-david-solomon-first-year) · [Investor Day 2020 deck, Jan 29 2020](https://www.goldmansachs.com/investor-relations/investor-day-2020/presentations/consolidated-presentations.pdf) · [Sheridan/Rangan, Feb 21 2023](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-21-2023-sheridan-rangan) · [Solomon, Feb 24 2023](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-24-2023-david-solomon) · [Argenti, Apr 18 2023](https://www.goldmansachs.com/insights/articles/ai-could-revolutionize-human-knowledge-goldman-sachs-marco-argenti-says) · [AI Forward, Jun 22 2023](https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/ai-forward-2023) · [Argenti 2024 predictions, Dec 21 2023](https://www.goldmansachs.com/insights/articles/a-new-generation-of-ai-tools-and-models-is-emerging) · [2023 letter](https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2023-annual-report/multimedia/letter-to-shareholders.pdf) · [Solomon, Jan 23 2024](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/01-23-24-solomon) · [Top of Mind #129, Jun 25 2024](https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too-much-spend-too-little-benefit) · [Skeptic podcast, Jul 16 2024](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/a-skeptical-look-at-ai-investment) · [Melissa Goldman, Oct 7 2024](https://www.goldmansachs.com/pressroom/press-releases/2024/melissa-goldman-rejoins-goldman-sachs) · [2024 letter](https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2024-annual-report/multimedia/letter-to-shareholders.pdf) · [Argenti 2025 predictions, Jan 9 2025](https://www.goldmansachs.com/insights/articles/what-to-expect-from-ai-in-2025-hybrid-workers-robotics-expert-models) · [Solomon, Jan 29 2025](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/david-solomon-on-global-business-environment-ai-and-rise-of-private-credit) · [AI Exchanges: Lee/Posnett, Feb 4 2025](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/ai-exchanges-will-falling-costs-drive-new-opportunities) · [Marcu, Mar 17 2025](https://www.goldmansachs.com/pressroom/press-releases/2025/daniel-marcu-joins-gs-as-partner-and-global-head-of-ai-engineering-and-science) · [AI Exchanges: Argenti, Mar 25 2025](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/ai-exchanges-cio-marco-argenti-on-the-future-of-ai-in-the-workplace) · [Argenti in Fortune, Jul 9 2025](https://www.goldmansachs.com/insights/articles/fortune-we-must-prepare-ai-natives-to-shape-the-future-of-work) · [Communacopia, Oct 7 2025](https://www.goldmansachs.com/insights/articles/what-will-it-take-for-companies-to-capitalize-on-the-rise-of-ai) · [Q3 2025 results, Oct 14 2025](https://www.goldmansachs.com/pressroom/press-releases/2025/2025-10-14-q3-results) · [2025 letter](https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2025/letter-to-shareholders.pdf) · [IV close, Jan 5 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/goldman-sachs-completes-acquisition-of-industry-ventures) · [Argenti 2026 predictions, Jan 22 2026](https://www.goldmansachs.com/insights/articles/what-to-expect-from-ai-in-2026-personal-agents-mega-alliances) · [Solomon on OneGS 3.0, Jan 23 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/goldman-sachs-chairman-and-ceo-david-solomon-on-ai-m-and-a-and-markets) · [GSI co-CEOs, Mar 16 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/goldman-sachs-internationals-co-ceos-on-europes-opportunity-ai-and-market-volatility) · [Vemulapalli, Apr 6 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/archana-vemulapalli-joins-goldman-sachs-as-partner-and-head-of-ai-product-management) · [Leslie as CAO, May 5 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/goldman-sachs-announces-leadership-updates-may-5-2026) · [Osman Ali, May 6 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/will-ai-make-markets-less-efficient) · [Kotsovinos, Jul 6 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/evan-kotsovinos-joins-goldman-sachs-as-partner-and-head-of-asset-and-wealth-management-engineering) · [Griffin, Jul 9 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/citadels-ken-griffin-on-ai-us-china-tensions-and-us-data-centers) · [AI debt, Aug 5 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/how-ai-debt-is-reshaping-the-credit-market) · [Churchman, Aug 24 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/building-ai-systems-for-capital-markets) · [Keswani, Sep 3 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/dinesh-keswani-joins-gs-as-co-head-of-core-engineering) · [Bellevue, Sep 8 2026](https://www.goldmansachs.com/pressroom/press-releases/2026/goldman-sachs-opens-new-engineering-office-in-bellevue-washington)
