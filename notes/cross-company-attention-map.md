# Note · Cross-company attention map — ten market-structure firms, 4,592 newsroom items: each has a fingerprint, and since 2023 they have all converged on the same two words, AI and tokens

> Cross-company analysis note · Maps to **Course 04** (Competitive Strategy — positioning, convergence), **Course 07** (Data, Analytics & Decision-Making — text classification, validation, base rates), **E8** (Stakeholder & Investor Relations — narrative as strategy), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Part of the cross-company set: [[cross-company-say-vs-do]], [[cross-company-capability-matrix]]

- **Source:** the ten company corpora built for this repo: 4,592 newsroom items, 2019 – Oct 2026 (Tradeweb 481, ICE 783, MarketAxess 359, Bloomberg 850, S&P Global 492, LSEG 804, Thomson Reuters 293, Goldman 262, JPMorgan 165, BlackRock 103). Tagged by `_ingest/attention.py` against the shared 24-topic taxonomy in `_ingest/attention_taxonomy.json`. Outputs are in `_ingest/raw/attention/` (`article_tags.csv`, `share_by_company.csv`, `share_by_year.csv`).
- **Core claim:** What a company publishes is a cheap, honest signal of what management wants to be known for. Every firm has a distinct fingerprint that matches its strategy: Tradeweb is rates plus e-trading, MarketAxess credit, ICE listings, mortgages and derivatives, LSEG indices, S&P commodities and ratings, Bloomberg workflow, Thomson Reuters AI, JPMorgan payments and tokens, and BlackRock private markets. Since 2023, though, the fingerprints have converged. AI went from under 5% of almost everyone's output to 10–60%, and tokenization followed one to two years later. Three things almost nobody talks about: their own **fees**, their own **outages**, and (outside BlackRock and Goldman) **private markets**, the one growth area where the venues have no product.

---

## 1. Method, and how far to trust it

- **Taxonomy:** 24 topics: 16 business lines (credit, rates, derivatives and clearing, equities/ETF, commodities, mortgages, listings, indices, pricing/data, workflow/desktop, ratings/research, private markets, retail/wealth, payments, AI, digital assets) plus 8 cross-cutting themes (e-trading, ESG, regulation, deals/results, people, fees, operational risk, international). Multi-label.
- **Tagger:** a transparent keyword scorer. Title hits count 3, body hits count 1, only the first 6,000 characters of the body are scored, and the corporate "About us" boilerplate is cut off first. Each topic has its own threshold.
- **Validation:** an independent annotator labelled a stratified sample of **160 articles** blind (16 per company), from definitions only. Against those labels the tagger scores **micro precision 0.67, recall 0.78, F1 0.72**. The thresholds were tuned on the same sample, so treat this as an in-sample upper bound.
- **Reliability tiers (F1):**
  - **High (≥0.8):** AI 0.89, digital assets 0.96, commodities 0.96, deals/results 0.91, derivatives 0.83, ESG 0.82, international 0.81.
  - **Medium (0.6–0.8):** credit, rates, equities, indices, pricing/data, workflow, e-trading, people, regulation.
  - **Low:** ratings/research (0.29), retail (0.50), risk (0.22), fees (no gold examples).
  - Low-tier topics are used here only for "near zero everywhere" statements, which don't depend on precision.
- **Comparability caveats:**
  1. **Filtered corpora.** Goldman, JPMorgan and BlackRock were filtered to the market-structure lens when collected (consumer banking, philanthropy and fund launches were skipped). Their shares describe that slice, not their whole newsroom.
  2. **Different source mixes.** LSEG's corpus includes 36 call transcripts and 7 annual reports, Bloomberg's is half "Insights" posts, and JPMorgan's includes 14 shareholder letters.
  3. **2026 runs to October only.**
  4. **The unit is the share of articles touching a topic**, not word share.

## 2. The fingerprints (share of articles, 2019–2026)

| Company | n | Top topics | Most distinctive (× the ten-company average) |
|---|---|---|---|
| Tradeweb | 481 | e-trading 48%, rates 30%, credit 20%, workflow 17% | rates ×4.2, e-trading ×3.5, credit ×2.6 |
| MarketAxess | 359 | e-trading 46%, credit 39%, pricing/data 22% | credit ×5.2, e-trading ×3.4 |
| ICE | 783 | derivatives/clearing 30%, pricing/data 26%, commodities 20%, indices 17%, listings 16% | listings ×5.8, mortgages ×5.0, derivatives ×4.2 |
| LSEG | 804 | pricing/data 37%, indices 26%, deals/results 22% | indices ×2.8, derivatives ×2.3 |
| S&P Global | 492 | deals/results 26%, pricing/data 25%, ESG 23%, commodities 17%, AI 15% | commodities ×3.0, ratings ×2.4, ESG ×2.2 |
| Bloomberg | 850 | workflow 30%, pricing/data 27%, ESG 21%, indices 18% | workflow ×2.2, international ×2.1 |
| Thomson Reuters | 293 | AI 32%, deals/results 30%, workflow 20%, people 18% | AI ×2.8, people ×1.6 |
| Goldman (filtered) | 262 | deals/results 52%, equities 20%, retail 13% | equities ×2.0, retail ×2.0 |
| JPMorgan (filtered) | 165 | tokens 36%, payments 29%, deals/results 26% | payments ×7.0, tokens ×5.5, risk ×3.2 |
| BlackRock (filtered) | 103 | deals/results 43%, private markets 29%, people 28%, ESG 19% | private markets ×5.2, retail ×2.7 |

**Reading it:** the fingerprints match each strategy. The surprises are in what *isn't* there:
- **S&P says little about ratings** (ratings/research tagged ~7%), even though ratings are its second-biggest business ([[cross-company-say-vs-do]]).
- **ICE says little about its own bond venue.** Credit is 8% of its output, mostly data, against 39% at MarketAxess. It bought MarketAxess instead of explaining ICE Bonds ([[ice-marketaxess-deal]]).
- **Thomson Reuters talks about AI more than about the legal, tax and accounting software that is 82% of its revenue.**

## 3. Five movements over time (share of each year's articles)

**3a. The AI wave reached the firms in a set order: content and data firms first, then banks, then venues.**

| | 2019–22 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Thomson Reuters | 3–6% | **40%** | 60% | 62% | 54% |
| Bloomberg | 0–10% | 18% | 22% | 26% | 19% |
| S&P Global | 0–3% | 8% | 15% | 34% | 35% |
| Goldman | 0% | 11% | 23% | 21% | 28% |
| JPMorgan | 0% | 8% | 23% | 24% | 19% |
| LSEG | 1–4% | 3% | 2% | 19% | **32%** |
| MarketAxess | 0–3% | 5% | 6% | 6% | **24%** |
| Tradeweb | 1–3% | 2% | 0% | 8% | 14% |
| ICE | 0–1% | 1% | 2% | 0% | 10% |

Thomson Reuters pivoted in the year after ChatGPT and its Casetext deal ([[thomsonreuters-ai-strategy]]). The venues (Tradeweb, MarketAxess, ICE) got there two to three years later, and ICE barely at all until 2026. That fits who is exposed: AI threatens the businesses built on documents and desktops first, and execution venues last.

**3b. Tokenization: one bank leads, the venues follow, and MarketAxess is absent.**
- **JPMorgan:** 23% (2022), 27% (2024), **52% (2025)**. Kinexys deposit tokens are the bank's most-published market-structure story ([[jpmc-kinexys-deposit-tokens]]).
- **Tradeweb:** 0% until 2023, then 9%, 14% and **25%** (2024–26).
- **Goldman:** spiked to 17% in 2021, then 13% in 2025, then **0%** in 2026 after its digital-asset platform was spun out ([[goldman-digital-assets]]).
- **MarketAxess:** 0% in every year.

**3c. Private markets: the asset managers and data firms moved, the venues didn't.**
- **BlackRock:** 27% (2023), **52%** (2024, the year of GIP, HPS and Preqin), 35–40% after.
- **Goldman:** 17–21% from 2023. **S&P Global:** 15% from 2025. **Bloomberg:** 13% in 2026.
- **The venues:** Tradeweb, MarketAxess and ICE are at 0–6% in every year. That gap is visible again in the capability matrix ([[cross-company-capability-matrix]]).

**3d. ESG collapsed everywhere.**
- **BlackRock:** 54–58% (2020–21) to 20% (2022) to single digits, then **0%** in 2026 ([[blackrock-stewardship-backlash]]).
- **Bloomberg:** 36% (2023) to **3%** (2026).
- **S&P Global:** 39% to 12–16%. **LSEG:** 25% to 7%. **ICE:** 22% (2022) to 3%.
- Every firm retreated at the same time, which points to the political climate, not to separate strategic decisions.

**3e. Operational risk entered the conversation in 2025–26.**
- JPMorgan 17% in 2026, LSEG 10% in 2025–26, MarketAxess 11% in 2025, Tradeweb 4–5%.
- It was near zero before. Much of it is about other people's resilience (market stress, clearing, tokenized settlement), not the firm's own outages (see the silence audit in [[cross-company-say-vs-do]]).

## 4. What almost nobody publishes

- **Their own fees.** Share of articles that mention fee rates, take rates or price changes:
  - **MarketAxess: 5–13% every year.** The fee-per-million table is in every earnings release, and its falling fees are the story ([[marketaxess-strategy-financials]]).
  - Everyone else: 0–6%. ICE, S&P and JPMorgan are 0% in every year.
  - The firm with the pricing problem is the only one that talks about pricing.
- **Their own operational failures.** See [[cross-company-say-vs-do]] §3.
- **Credit outside the two credit venues.** Credit is 20% at Tradeweb and 38–58% at MarketAxess, against at most 14% anywhere else. Bloomberg, LSEG and S&P sell the prices and indices credit trades on, but write about credit itself only 0–4% of the time.

## 5. What the attention map does not prove

1. **Attention is intent, not performance.** It shows what management wants known. Revenue and filings test whether it's real; see [[cross-company-say-vs-do]].
2. **Newsrooms over-sample launches.** New products get releases, while mature cash cows get earnings tables. That alone biases every company toward its newest bets.
3. **Keyword tagging misses framing.** "AI" in a 2026 Tradeweb release and in a 2023 Thomson Reuters release can mean very different depths of commitment. The company notes give the qualitative read.
4. **Filtered corpora** (Goldman, JPMorgan, BlackRock) are not comparable on retail, consumer or fund topics.

## 6. Strategic read (inference)

- **Convergence is a risk signal.** When ten firms with different businesses all lead with AI and tokens, the messaging stops differentiating them. The firms whose AI story is backed by a revenue line (Thomson Reuters' CoCounsel, LSEG's data licensing to model makers, Bloomberg's terminal AI) are in a different position from the venues, whose AI is internal tooling and dealer selection ([[tradeweb-tech-ai-data]]).
- **Order of arrival follows exposure.** Thomson Reuters moved first because AI threatens legal research directly. Bloomberg and S&P followed because AI threatens desktops and data. The venues moved last because the trade still has to clear somewhere. ICE's near-silence until 2026 is consistent with a business whose swings come from energy futures and whose biggest bet is mortgages ([[ice-strategy-financials]]).
- **Private markets is the open flank for venues.** Asset managers (BlackRock) and data firms (S&P, Bloomberg, LSEG via Octus) all moved in 2024–26. No venue has a private-credit trading product at scale. Tradeweb's MAXEX stake is the closest.

## 7. Canon lenses

- **Signalling and cheap talk** ([[canon-dixit-nalebuff-thinking-strategically]]): press releases cost little, so they reveal intent but not commitment. Commitment shows up in deals and capex ([[cross-company-capability-matrix]]).
- **Isomorphism and herding** ([[canon-taleb-black-swan]], [[canon-kahneman-thinking-fast-and-slow]]): the simultaneous ESG retreat and AI rush look more like social proof than ten independent decisions.
- **Innovator's dilemma** ([[canon-christensen-innovators-dilemma]]): the incumbents most exposed to a technology talked about it first. The least exposed waited.
- **Measurement** ([[canon-tufte-visual-display]]): the share-of-voice table only means something with its validation numbers next to it.

## 8. Open questions

1. Does AI attention at the venues (Tradeweb 14%, ICE 10% in 2026) turn into disclosed AI revenue by 2027, or stay internal tooling?
2. Will MarketAxess under ICE keep publishing fee-per-million tables?
3. Does tokenization at Tradeweb (25% of 2026 output) produce a revenue line? It is currently ~$12M of "other" ([[cross-company-say-vs-do]]).
4. Who is the first venue to launch private-credit trading at scale?

**Links:** [[cross-company-say-vs-do]] · [[cross-company-capability-matrix]] · [[tradeweb-hub]] · [[ice-hub]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[lseg-hub]] · [[thomsonreuters-hub]] · [[goldman-hub]] · [[jpmc-hub]] · [[blackrock-hub]] · [[thomsonreuters-ai-strategy]] · [[jpmc-kinexys-deposit-tokens]] · [[goldman-digital-assets]] · [[blackrock-stewardship-backlash]] · [[marketaxess-strategy-financials]] · [[ice-marketaxess-deal]] · [[tradeweb-tech-ai-data]] · [[canon-dixit-nalebuff-thinking-strategically]] · [[canon-christensen-innovators-dilemma]] · [[canon-kahneman-thinking-fast-and-slow]] · [[canon-taleb-black-swan]] · [[canon-tufte-visual-display]]

---
### Rep
1. Open `_ingest/raw/attention/article_tags.csv`. Pick one company, and read the titles of 20 articles tagged `ai` in 2026 and 20 tagged `ai` in 2023. Classify each as **product** (sold to clients), **internal** (tooling, efficiency) or **commentary**. Did the mix change, or only the volume?
2. Using §3a, compute each company's AI "lag": the first year its AI share passed 15%. Rank them, and compare the ranking with how much of each firm's revenue is desktops and documents ([[cross-company-say-vs-do]] §2). Does exposure predict speed?
3. *Re-run:* `python3 _ingest/attention.py --validate` prints precision and recall by topic. Add three keywords to the weakest topic (`risk_resilience`) and see whether its F1 rises without the others falling.
