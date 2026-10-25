# Note · Thomson Reuters through outside eyes — buyers of its assets, sellers of its AI engines, customers who keep a lawyer in the loop, and a few analysts and academics who asked the hard question once

> Stakeholder / outside-view note · Maps to **E8** (Stakeholder & Investor Relations — whose voice gets printed and why), **Course 04** (Competitive Strategy — suppliers, buyers, complementors, missing rivals), **Course 08** (Negotiation & Influence — reading counterparties in deal releases), **E10** (Digital & AI Transformation — partner and customer framing of AI), **E4** (governance — the controller's voice) · Written 2026-10-25 · Part of [[thomsonreuters-hub]]; companions [[thomsonreuters-people]] and [[thomsonreuters-mission-forces]]

- **Source:** every non-TR voice in the 293 corpus items, 2019–2026 (`_ingest/raw/thomsonreuters/articles.jsonl`). That covers deal counterparties (LSEG, KKR, TPG, Pagero, Shin Nippon), AI partners (OpenAI, Anthropic, Microsoft, AWS, Google, Imperial College), customers quoted in launches, the academics TR chose as evaluators, the Georgetown co-authors of the legal-market reports, a government customer (Ontario AG), and the sell-side analysts in the 2021 Investor Day Q&A.
- **Selection-bias warning:** TR chose every voice here. Partner and customer lines are co-written press-release quotes. The only voices TR didn't script are the **analyst questions** at the 2021 Investor Day, and even those were partly relayed by TR's head of IR. The corpus has **no** competitor comment, no regulator criticism, no unhappy customer, no Blackstone or Microsoft quote on the LSEG trades, and no reaction to the Thomson LLM from a lab.
- **Core claim:** The outside voices fall into four groups:
  1. **Counterparties to TR's portfolio moves** (LSEG's Schwimmer, KKR's Dillard, Pagero's founders). Each praises the asset it is *buying* or the partnership it *gets*.
  2. **AI suppliers** (OpenAI, Anthropic, Microsoft). They praise TR's *content* as the thing their models need. That is flattering, and also a reminder of who has the engine.
  3. **Customers.** They praise speed and add a safeguard in the same breath: lawyers review all output, models "do not train on client data", or use is "experimental".
  4. **Independent framing.** Georgetown's co-authors, academic testers and 2021 analysts are the only sources of doubt. That doubt is about TR's *markets* and *valuation*, never its AI claims.

---

## 1. Stakeholder map

| Group | Who (in corpus) | What they want from TR | Power over TR |
|---|---|---|---|
| Controlling owner | Woodbridge (Thomson family, ~66–70%) | Dividend streak, long horizon, Trust Principles | Decisive: votes, float cap, board |
| Guardian | Founders Share Company (Williams → Toope) | Reuters independence | Veto-like over control changes |
| Former parent of markets business | Blackstone consortium (co-owner of the LSEG holding) | Orderly joint exit | Joint decisions on every sale |
| Acquirer and channel | LSEG (Schwimmer; TR's Erin Brown on its board 2021–24) | Exclusive Reuters feed to 2048; buyback of its own shares | Sole buyer of Reuters in finance |
| AI suppliers | OpenAI (Lightcap, Weil), Anthropic (Scott White), Microsoft (Raghavan), AWS, Google | Distribution into regulated professions; TR's content as grounding | High: they supply the engine and could sell direct |
| Buyers of TR assets | KKR (Dillard: Print), TPG (Elite), Karnov (Spain), Internet Brands (FindLaw) | Cash-generating declining or adjacent assets | Low after close (except KKR's minimum-return right) |
| Targets | Casetext (Heller), Materia (Merlini), Pagero (Nilsson), Shin Nippon (Westlaw Japan) | Scale and distribution | — |
| Customers | Greenberg Traurig, Morgan Lewis (Nihill), Addleshaw Goddard, Linklaters, US federal judiciary (AO), Ontario courts | Speed with defensibility | Collective: retention ~90%+ |
| Independent framers | Georgetown Law (James W. Jones et al.), Oxford Saïd, academic testers (Choi, Dahan, Steffek) | Research access, credibility | Reputational |
| Investors | 2021 analysts: BMO (Casey), Morgan Stanley (Kaplan), JPMorgan (Steinerman), RBC (McReynolds), BofA (Bisbee), Barclays, Lincoln Square (Hoffman) | Growth credibility, use of LSEG cash | Price of capital |

## 2. Counterparties: each praises what it is buying

- **LSEG, Jan 17 2023** (while TR was selling LSEG shares): Schwimmer said "This collaboration will broaden our news offering, enhancing the speed and analysis of breaking news". LSEG got 100 new markets reporters and exclusive AI breaking news (PLX). Inference: LSEG paid for that partly in goodwill and consent to lock-up variations. See [[thomsonreuters-refinitiv-lseg-exit]].
- **KKR, Jul 14 2026:** Dillard called TR's print business the "gold standard for printed reference materials". KKR also got a TR promise of "a minimum return on its equity investment… under certain circumstances". The praise and the downside protection arrived together.
- **Pagero, 2024:** the target's board recommended TR's SEK 50 offer after competing bids from Vertex and Avalara. A bidding war is the most credible outside valuation in the corpus. Two strategic buyers thought e-invoicing compliance was worth fighting for.
- **Investors in 2018–19:** they took $10B of F&R proceeds back through a tender offer and a return of capital. Their voice is the size of the tender response, not a quote.

## 3. AI suppliers: *your content, our engine*

- **OpenAI (Lightcap, Apr 2024):** "By powering solutions like CoCounsel, their new professional-grade AI Assistant, together we make knowledge workers more creative and productive". **Weil (Nov 2024)** on the custom o1-mini: "Building a custom o1-mini model into CoCounsel equips legal professionals with advanced AI reasoning capabilities".
- **Anthropic (Scott White, May 2026):** "Integrating Claude with CoCounsel Legal brings together leading AI with trusted legal content and workflows". That same release made CoCounsel available *inside Claude* via MCP.
- **Microsoft (Raghavan, May 2024):** "We are committed to extending Microsoft Copilot to enable new functionalities for our customers." Microsoft was at once a Copilot partner, an LSEG shareholder (it bought from TR and Blackstone in 2023) and a TR board connection (Kirk Koenigsbauer, director from 2020).
- **Read:** every supplier quote values TR's *content and distribution*. None values TR's *models*. The Aug 2026 Thomson LLM launch has no lab quote at all. *(Inference: owning a model is the one move the suppliers wouldn't endorse.)*

## 4. Customers: enthusiasm with a lawyer in the loop

- **Morgan Lewis (Colleen Nihill, Aug 2025):** "Deep Research stands out for its ability to reason".
- **Greenberg Traurig (Aug 2026)**, AmLaw 20, four-year collaboration. The release spells out the firm's controls:
  - AI work product is "reviewed by lawyers handling the matter and by supervising shareholders before they reach a client".
  - AI models "do not train on client data".
- **Linklaters (Mar 2024)**: used CoCounsel Core "in an experimental capacity".
- **Magone and Company (Dec 2024)**: younger staff "had been using ChatGPT". The consumer tool came first. TR's sale was partly about controlling that use.
- **Ontario AG Doug Downey (Aug 2020, CaseLines):** "a robust, online digital platform with a proven track record in courts around the globe". This is the government-as-customer voice, before GenAI.
- **US Courts (AO), Apr 2025:** a multi-year contract with options for 25,000+ legal professionals. Ramanathan: "We are honored that the AO continues to trust our legal research solutions."
- **Read:** customers are buying **speed under supervision**. None describes replacing a lawyer. Every safeguard they mention (review, no training on client data, experimental use) is a feature TR then built into "fiduciary-grade". TR turned its customers' risk controls into its product spec.

## 5. Skeptics and independent framing

**Analysts at the 2021 Investor Day** (the only unscripted outside voices):

| Analyst (firm) | Question | Answer, and what it revealed |
|---|---|---|
| Tim Casey (BMO) | Why believe 5–6% organic growth? | Hasker: 2019's 3.7% was "driven by price and strong retention rates"; "nothing in there that's a huge leap of faith". *Pricing power is the growth engine.* |
| Toni Kaplan (Morgan Stanley) | Why is transformation easier now? | Roth: SaaS tooling is mature; adoption is the hard part |
| Manav (Barclays) | Do buyback limits force M&A? | Eastwood: the Woodbridge float cap (~70%); Hasker: "pretty full valuations", high bar |
| Vince Valentini (firm not stated) | LSEG shares sold? Does COVID demand reverse? | Eastwood: none sold yet; Hasker: changes "not reversible" |
| Andrew Steinerman (JPMorgan) | Does self-serve shrink sales forces? | Digital is additive |
| Drew McReynolds (RBC) | What surprised the new team? What's unfinished by 2023? | Product design and silos; international and risk/fraud |
| Sam Hoffman (Lincoln Square) | Why the discount to business-services peers? Limited TAM? | Hasker: "polar opposite view". No data offered |
| Gary Bisbee (BofA) | Where do $600M of savings come from? | Procurement (~$4B addressable), location, real estate, product consolidation. *Bisbee became TR's own head of IR ten months later.* |

**Georgetown Law / TR legal-market reports** (co-authored, so semi-independent):
- James W. Jones (2019): "For many years, it was largely assumed by both firms and clients that legal work was labor intensive, could only be performed by lawyers".
- 2022: "The traditional law firm response of just throwing more money at the problem is not likely to work as well going forward."
- 2023: partners "may feel significantly less well-off than in 2021".
- Peer Monitor (2022): rising associate costs plus turnover is "likely not a sustainable formula".
- The Sept 2023 Australian report names a "No Road where generative AI has no significant strategic impact and the hype is disproportionate to its actual utility." It is the only written allowance in the corpus that AI could fail to matter.

**Academic testers of the Thomson LLM** (Aug 2026, chosen by TR):
- Jonathan Choi: "I preferred Thomson's responses overall".
- A second evaluator found citation quality "generally competitive with leading frontier models".
- One test noted "All three models answered the questions correctly". On those questions, at least, the models were indistinguishable.
- Felix Steffek (Cambridge, on the Imperial lab, Dec 2025) noted "significant challenges that foundational research needs to address".

## 6. Competitors as seen in the corpus

- **Named once (2021, Beastrom):** LexisNexis, "most significant competitor" to Westlaw and Practical Law; Bloomberg Law "attempting to break into the space".
- **Named only as rival bidders:** Vertex and Avalara (Pagero, 2024).
- **Never named:** RELX (LexisNexis's parent), Wolters Kluwer, Intuit, Harvey and every other AI-native legal startup. The frontier labs appear only *as partners*.
- **Implied:**
  - Wong: "What others are calling agentic, we’ve already had in the market."
  - The "Thomson" release: "Frontier labs have typically spent billions of dollars on compute".
  - Hron: "every company in this space has it".
- *Read (inference):* naming no competitors is a choice. It keeps the story on trust, where TR leads, and off features and price, where it may not. For the competitive picture, use outside sources. The corpus can't provide one.

## 7. Canon lenses

- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): the AI labs are TR's suppliers, complementors (MCP inside Claude) and potential competitors at once. LSEG was investee, channel and buyer of TR's shares. Apply the value-net exercise to Anthropic: who gains if CoCounsel lives inside Claude?
- **Persuasion through social proof** ([[canon-cialdini-influence]]): AmLaw firms, the federal judiciary and "one million professionals" are classic social proof. The safeguards customers mention are the real buying criteria.
- **Supplier power** ([[canon-porter-competitive-strategy]]): concentrated model suppliers with forward-integration options are the force TR's outside voices most clearly reveal, by what they praise (content) and what they don't (TR's models).
- **Reading the other side** ([[canon-fisher-ury-getting-to-yes]]): KKR's minimum-return clause and LSEG's lock-up consents show each counterparty's real interests behind the positional praise.

## 8. Open questions

1. What do LexisNexis, Harvey and the labs say about TR? That needs outside sources: earnings calls, press, the [[bloomberg-hub]] and [[spglobal-hub]] corpora for comparison.
2. Did Blackstone or Microsoft ever comment on the LSEG trades? Check their releases.
3. Are there customer departures or price complaints? Retention (~90%+) is the only aggregate signal.
4. Will Anthropic or OpenAI quote on Thomson, or stay silent?

**Links:** [[thomsonreuters-hub]] · [[thomsonreuters-people]] · [[thomsonreuters-mission-forces]] · [[thomsonreuters-ai-strategy]] · [[thomsonreuters-refinitiv-lseg-exit]] · [[thomsonreuters-capital-allocation]] · [[tradeweb-outside-voices]] (the same selection-bias problem at a venue) · [[lseg-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-cialdini-influence]] · [[canon-porter-competitive-strategy]] · [[canon-fisher-ury-getting-to-yes]]

---
### Rep
Take three outside quotes from §2–§4: one counterparty, one AI supplier, one customer. For each, write:
- (a) the speaker's incentive;
- (b) what the quote *doesn't* say;
- (c) the one fact that would confirm or refute it.

Then write the question you'd have asked at the 2021 Investor Day that none of the eight analysts asked.

*Model answer:* the missing question was ***What happens to Westlaw's premium if a general-purpose AI model can do research on public case law?*** In Mar 2021 no analyst asked about AI substitution. Twenty months later it became the central question.

**Sources:**
[2019 State of the Legal Market (Jones), Jan 9 2019](https://www.thomsonreuters.com/en/press-releases/2019/january/rebuilding-the-law-firm-model-2019-report-on-the-state-of-the-legal-market) · [CaseLines (Downey), Aug 13 2020](https://www.thomsonreuters.com/en/press-releases/2020/august/thomson-reuters-acquires-caselines) · [2021 Investor Day transcript, Mar 16 2021](https://ir.thomsonreuters.com/static-files/d7d038bf-b689-4db3-abd6-c124f66ad807) · [Peer Monitor Q4 2021, Feb 14 2022](https://www.thomsonreuters.com/en/press-releases/2022/february/incredibly-strong-demand-closes-out-2021-but-year-of-talent-challenges-loom) · [LSEG–TR news pact, Jan 17 2023](https://www.thomsonreuters.com/en/press-releases/2023/january/lseg-and-thomson-reuters-announce-joint-commitments-to-enhance-the-value-of-financial-and-markets-news-service-as-part-of-long-term-partnership) · [UK CoCounsel launch (Linklaters), Mar 12 2024](https://www.thomsonreuters.com/en/press-releases/2024/march/thomson-reuters-cocounsel-core-leading-legal-genai-assistant-and-ai-assisted-research-on-westlaw-edge-rollout-to-uk-legal-professionals) · [OpenAI (Lightcap), Apr 17 2024](https://www.thomsonreuters.com/en/press-releases/2024/april/thomson-reuters-announces-expanded-vision-to-provide-genai-assistant-for-every-professional-it-serves) · [Microsoft Build, May 21 2024](https://www.thomsonreuters.com/en/press-releases/2024/may/thomson-reuters-showcases-the-power-of-cocounsel-combined-with-microsoft-copilot-during-the-2024-microsoft-build-keynote) · [OpenAI custom model (Weil), Nov 25 2024](https://www.thomsonreuters.com/en/press-releases/2024/november/thomson-reuters-cocounsel-tests-custom-llm-from-openai-broadening-its-multi-model-product-strategy) · [CoCounsel Legal (Morgan Lewis), Aug 5 2025](https://www.thomsonreuters.com/en/press-releases/2025/august/thomson-reuters-launches-cocounsel-legal-transforming-legal-work-with-agentic-ai-and-deep-research) · [Anthropic partnership, May 12 2026](https://www.thomsonreuters.com/en/press-releases/2026/may/thomson-reuters-and-anthropic-expand-partnership-to-connect-claude-with-cocounsel-legal) · [KKR print JV, Jul 14 2026](https://www.thomsonreuters.com/en/press-releases/2026/july/thomson-reuters-and-kkr-announce-joint-venture-for-thomson-reuters-global-print-business) · [Thomson LLM (academic testers), Aug 24 2026](https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-leverages-its-world-class-data-assets-to-launch-its-own-frontier-model) · [Greenberg Traurig, Aug 26 2026](https://www.thomsonreuters.com/en/press-releases/2026/august/greenberg-traurig-deploys-the-next-generation-of-cocounsel-legal)
