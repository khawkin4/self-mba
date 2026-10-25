# Note · S&P Global hub — a ratings-and-benchmarks toll road that bought breadth with IHS Markit, spent four years giving it back, and now bets the remainder on being the data layer inside other people's AI

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy), **Course 02** (Corporate Finance & Valuation), **Course 07** (Data, Analytics & Decision-Making), **Course 09** (Leadership & Org Behavior), **Course 11** (Global Strategy, Macro & Responsible Business), **E1** (Leading at Scale), **E2** (Capital Allocation), **E3** (M&A), **E4** (Governance), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Entry point for the ten S&P Global notes

- **Source:** S&P Global's own corporate record, 2019-01-01 → 2026-10-25. The index covers **1,707 items** (`_ingest/raw/spglobal/index.tsv`):
  - press.spglobal.com newsroom, all divisions;
  - the investor.spglobal.com release feed;
  - annual-report shareholder letters for 2019–2025;
  - the 2022 and 2025 investor-day decks, the 2026 Mobility Global investor-day deck and the 2021 merger-vote slides.

  **492 substantive texts** were read in full (`articles.jsonl`). Excluded: 1,214 routine items (index rebalancing, Case-Shiller, Platts price launches, ratings commentary, dividend, date and award notices); each exclusion reason is listed in the index. Reading digest: `_ingest/raw/spglobal/DIGEST.md`.

  **Gaps:** the earnings releases from mid-2023 onward are link-only stubs, so the quarterly segment numbers after Q1 2023 are missing. There are no earnings-call transcripts and no third-party press.
- **Core claim:** S&P Global sells *opinions and reference numbers that regulated workflows must use*: credit ratings, the S&P 500 and its licences, Platts benchmarks, and Capital IQ data. The business compounds through volatility, refinancing waves and passive investing. Its story has three acts:
  1. **2019–2022, breadth.** "Powering the Markets of the Future" leads to the **$44B all-stock IHS Markit merger**. That brought iBoxx, CDX/iTraxx, evaluated pricing, Ipreo, OSTTRA, Mobility and Engineering Solutions.
  2. **2022–2025, subtraction.** Regulators forced sales to rivals: CUSIP to FactSet, LCD to Morningstar, OPIS to News Corp. Guidance was suspended in the first year. Then S&P chose to sell or spin off Engineering Solutions, OSTTRA, Mobility and several Markit software lines. A planned CEO succession (Peterson → Cheung, Nov 2024) presided over the pruning.
  3. **2024–2026, the AI layer.** Kensho's API and MCP servers put S&P data *inside* Claude, Copilot, Gemini and Cohere. In July 2026 Market Intelligence was reorganised around "Kensho Data & Platforms". In parallel, the index licence follows liquidity onto Hyperliquid and Canton.

  The unresolved question is whether proprietary data stays the scarce good once LLM front-ends and venue-owned prices sit between S&P and the user.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[spglobal-people]] | A textbook CEO succession on top, two years of churn underneath | Who runs S&P, profiles with dated quotes, where views shifted |
| [[spglobal-mission-forces]] | The mission words changed three times; the operating truth never did | Mission lines and boilerplate drift, tailwinds and headwinds, forces map, crisis tests, scenarios |
| [[spglobal-outside-voices]] | Partners praise the rails; the real outside verdicts come as regulator remedies | Stakeholder map, regulators, skeptics, competitors as seen in the corpus |
| [[spglobal-strategy-financials]] | A cyclical ratings engine plus subscription ballast, with capital return beyond its own framework | Revenue, EPS and margins 2018–25; targets; synergies; buybacks; the deal list |
| [[spglobal-ihs-markit-merger]] | The $44B merger's real price was paid in remedies and in the first year after closing | The deal, the remedies, the 2022 slump, every disposal, what survived |
| [[spglobal-ai-data-layer]] | From Kensho as a cost line to S&P as the data layer inside other firms' LLMs | Kensho → LLM-ready API → MCP → AI Data Portal → the July 2026 MI reorg |
| [[spglobal-pricing-fixed-income]] | Evaluated pricing now rests on dealer and venue inputs; the moat is the indices and identifiers | Coverage numbers, CP+, Barclays, loans, identifiers, primary-market plumbing |
| [[spglobal-indices-benchmarks]] | S&P DJI is a licensing toll booth whose moat is regulatory status plus venue partners | CME JV, Cboe, GICS with MSCI, BMR/IOSCO, SEC penalty, iBoxx and CDX |
| [[spglobal-digital-assets]] | The benchmark and ratings brand follows liquidity on-chain, labelled "not a rating" | Stablecoin assessments, tokenized S&P 500, Hyperliquid perpetuals, Kaiko, OpenZeppelin, tokenized iBoxx |
| [[spglobal-esg-reversal]] | One executive built an ESG franchise and then folded it | Forecasts vs actuals, wording changes, "energy expansion, not replacement" |

**Suggested order:** people → mission-forces → strategy-financials → ihs-markit-merger → pricing-fixed-income → indices-benchmarks → ai-data-layer → digital-assets → esg-reversal → outside-voices. Read [[tradeweb-ai-price]] §5 before pricing-fixed-income.

## 2. Timeline, 2019–2026

| Date | Event | Why it matters |
|---|---|---|
| 2019-01-28 | Ratings becomes the first wholly foreign-owned credit rating agency (CRA) cleared to rate China's domestic bond market | Ratings used as market access ([[spglobal-outside-voices]]) |
| 2019-03-01 | The S&P 500 and the DJIA are the first benchmarks endorsed into the EU under the Benchmarks Regulation (BMR) | Regulatory status is the index moat ([[spglobal-indices-benchmarks]]) |
| 2019–2020 | SAM/RobecoSAM, ESG Scores, Trucost; Kensho on NVIDIA; Marketplace; Snowflake | The ESG build-out begins; distribution goes to the cloud |
| 2020-04-08 | Index collaboration between S&P DJI and IHS Markit (S&P 500 + iBoxx + CDX + iTraxx) | A first tie-up, seven months before the merger |
| **2020-11-30** | **IHS Markit merger agreed** (IHS EV $44B, all-stock) | Act 1 ([[spglobal-ihs-markit-merger]]) |
| 2021-05-17 | S&P DJI pays a $9M SEC penalty (VIX-futures index QA) | Benchmark integrity |
| 2021-10 → 12 | Remedies: CUSIP → FactSet $1.925B; OPIS → News Corp ~$1.15B; LCD commitment | Regulators make S&P create competitors |
| **2022-02-28** | **Merger closes** (~$140B EV); $12B accelerated share repurchase (ASR) | The modern SPGI |
| 2022-06-01 | 2022 guidance suspended; Ratings revenue at risk by up to $600M | The deal closes into an issuance collapse |
| 2022-12-01 | Investor Day: "Powering Global Markets"; 2025/26 targets | The strategy reset |
| 2023-05-02 | Engineering Solutions → KKR ($975M) | Act 2 begins |
| **2024-06-27** | **Cheung named to succeed Peterson (effective 2024-11-01)** | [[spglobal-people]] |
| 2024-10-17 | New leadership team; Sustainable1 folded; Chief Purpose Officer role ends | [[spglobal-esg-reversal]] |
| **2024-10-31** | **MI–MarketAxess data deal: CP+ feeds S&P Evaluated Bond Pricing** | [[spglobal-pricing-fixed-income]]; [[tradeweb-ai-price]] §5 |
| 2024-11-13 | Kensho LLM-ready API (beta) | Act 3 begins ([[spglobal-ai-data-layer]]) |
| 2025-04 → 10 | OSTTRA → KKR ($3.1B EV, 50/50 with CME); Mobility spin-off announced | Exit from post-trade; perimeter shrinks |
| 2025-07-15 | Anthropic: Kensho MCP server brings Capital IQ data into Claude | First named frontier-LLM channel |
| 2025-10-02 | Catherine Clay (from Cboe) named CEO of S&P DJI | A derivatives and exchange-data leader for indices |
| 2025-10-15 | With Intelligence acquired ($1.8B) | Private-markets data |
| 2025-11-13 | Investor Day: "Advancing Essential Intelligence" | The Cheung-era mission ([[spglobal-mission-forces]]) |
| 2026-03-18 | S&P 500 licensed for perpetual futures on Hyperliquid | [[spglobal-digital-assets]] |
| 2026-07-01 | Mobility Global spin completed | Four divisions remain |
| **2026-07-06** | **MI split into Kensho Data & Platforms and Enterprise Solutions; pricing goes to Enterprise Solutions** | The AI-era org chart |
| 2026-09 | Kaiko Series B-2 lead; OpenZeppelin agreed | Digital assets become an M&A theme |
| 2026-10-13 | First on-chain OTC swap on a tokenized benchmark (iBoxx USD Liquid IG; Canton; DRW vs Marex) | An IHS Markit benchmark moved onto tokenized rails |

## 3. Six patterns across the notes

1. **Buy breadth, then prune to the toll roads.** Almost everything sold after 2022 was workflow software or low-margin breadth: Engineering Solutions, Fincentric, PrimeOne, EDM/thinkFolio, upstream software, Mobility. What stayed has *benchmark or opinion status* that others must reference: ratings, S&P 500, iBoxx, CDX/iTraxx, Platts. *(Inference.)* See [[spglobal-ihs-markit-merger]].
2. **Regulators write the competitive map.** EU BMR and IOSCO status protect the index franchise. Merger remedies created rivals (FactSet in identifiers, Morningstar in leveraged loans, News Corp in price reporting). SEC settlements in 2021, 2022 and 2024 are the price of operating that franchise. Compare Tradeweb, where mandates *created* the business ([[tradeweb-derivatives-regulation]]).
3. **Distribute everywhere, own the licence.** The same move repeats: Snowflake (2020), AWS (2023), Databricks, Kensho API (2024), MCP into Claude, Copilot, Gemini and Cohere (2025–26), S&P 500 perpetuals on Hyperliquid, tokenized iBoxx on Canton. S&P lets other platforms own the front end and keeps the licence fee. The bet only works if the data stays scarce. Farsight's CEO, quoted in an S&P release, says it won't ([[spglobal-outside-voices]]).
4. **Volatility is fuel; issuance droughts are the real risk.** Q2 2020 Ratings revenue rose 26% during COVID. In 2022 transaction revenue fell 31%, 44% and 56% in successive quarters and guidance was suspended. The subscription businesses (MI, Platts, Indices) are ballast, not the engine. See [[spglobal-strategy-financials]].
5. **Narratives turn faster than businesses.** "Powering the Markets of the Future" became "Powering Global Markets", then "Advancing Essential Intelligence". ESG went from flagship to folded inside three years. "Automotive markets" stayed in the boilerplate after the Mobility exit was announced. Divisions still say "confidence" while corporate says "conviction". See [[spglobal-mission-forces]] and [[spglobal-esg-reversal]].
6. **Reference prices are migrating to venues, and S&P is on the far side of the venue that matters.** S&P imported MarketAxess CP+ into its evaluations. ICE is now buying MarketAxess. Tradeweb owns Ai-Price and partners with FTSE Russell for benchmark prices. S&P's credit moat is therefore the *indices* (iBoxx, CDX/iTraxx), not the *prices*. See [[spglobal-pricing-fixed-income]], [[tradeweb-ai-price]], [[marketaxess-hub]] and [[ice-hub]].

## 4. Where S&P Global and Tradeweb touch

| Point of contact | Relationship | Evidence |
|---|---|---|
| iBoxx TRS on Tradeweb's swap execution facility (2021) | S&P index, Tradeweb venue (cooperation) | Tradeweb corpus 2021-03-26 |
| InvestorAccess ↔ Tradeweb in European primary markets (2022) | S&P issuance utility, Tradeweb secondary | Tradeweb corpus 2022-09-29 |
| OSTTRA MarkitWire confirms Tradeweb's swaption and IRS terminations (2026) | Infrastructure built at S&P/Markit and sold to KKR; now a Tradeweb dependency | Tradeweb corpus 2026-02-11, 2026-09-30 |
| Digital Asset (Canton) $355M raise; DTCC tokenized-collateral pilot (2026) | Both are investors and participants on the same rail, with separate products | Tradeweb corpus 2026-06-11, 2026-07-15 |
| Evaluated pricing vs Ai-Price | S&P sides with MarketAxess CP+; Tradeweb sides with FTSE Russell | [[tradeweb-ai-price]] §5, [[spglobal-pricing-fixed-income]] |
| People | No direct moves. S&P CLO Thomas Kim led the separation of Thomson Reuters' Financial & Risk unit (Refinitiv, Tradeweb's former controlling owner) | 2026-10-09 release; [[thomsonreuters-hub]], [[lseg-hub]] |

## 5. Cross-note open questions

1. **CP+ after ICE.** Does the MarketAxess data deal survive ICE's purchase (expected close H1 2027)? If not, what replaces it as S&P's corporate-bond input? ([[spglobal-pricing-fixed-income]])
2. **Licence economics in the LLM channel.** Do MCP and API deliveries into Claude, Copilot and Gemini grow licence revenue, or do they cannibalise Capital IQ Pro seats? Watch MI growth and margin under the July 2026 structure. ([[spglobal-ai-data-layer]])
3. **Quarterly numbers.** Pull the 2024–2026 earnings PDFs (the corpus has only stubs). Check MI's growth and margin trend and the post-spin four-division recast. ([[spglobal-strategy-financials]])
4. **Ratings firewall.** Credit Analytics moved into Ratings, OpenZeppelin reports to the Ratings President, and ratings data is now in the AI portal. How do the EU and US CRA rules treat this? ([[spglobal-outside-voices]], [[spglobal-digital-assets]])
5. **Leadership stability.** Does the two-co-head MI structure hold through 2027? ([[spglobal-people]])
6. **On-chain licensing.** Do Hyperliquid and Canton deals produce licence revenue big enough to appear in Indices' disclosures? ([[spglobal-digital-assets]])

**Links:** [[spglobal-people]] · [[spglobal-mission-forces]] · [[spglobal-outside-voices]] · [[spglobal-strategy-financials]] · [[spglobal-ihs-markit-merger]] · [[spglobal-ai-data-layer]] · [[spglobal-pricing-fixed-income]] · [[spglobal-indices-benchmarks]] · [[spglobal-digital-assets]] · [[spglobal-esg-reversal]] · [[tradeweb-hub]] · [[tradeweb-ai-price]] · [[tradeweb-tech-ai-data]] · [[tradeweb-derivatives-regulation]] · [[ice-hub]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[lseg-hub]] · [[thomsonreuters-hub]] · [[blackrock-hub]] · [[wss-capital-markets-ma]] · [[wss-credit-distressed]] · [[sec-filing-intelligence]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-porter-competitive-strategy]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
Write a one-page **memo to S&P Global's board** on one question: *Is Market Intelligence still a core business?* Use only numbers from these notes.

1. Compare MI's adjusted margin with Ratings' and Indices' ([[spglobal-strategy-financials]]). With 2021 levels of roughly 34%, 64% and 70%, how many points of enterprise margin does MI cost at its ~30% revenue weight? *(Rough answer: if MI ran at the ~60% average of Ratings and Indices instead of 34%, enterprise margin would rise by about 0.30 × 26 ≈ 8 points. That is the cost of keeping MI, before counting its data's value to the other divisions.)*
2. Name the two assets inside MI that the AI strategy depends on (Capital IQ data; Kensho), and one MI asset that rests on a venue's feed (evaluated bond pricing via CP+).
3. Using pattern 1, say which MI pieces you would keep, sell or spin, and why.
4. Name the single fact you would need before voting: for example, ICE's intentions for CP+, or how much MI revenue now arrives through LLM channels.

**Corpus refresh:** press.spglobal.com works with plain `curl` (listing `index.php?s=2429&l=100&year=Y&category=C`). For the IR side, use the Q4 JSON feed `investor.spglobal.com/feed/PressRelease.svc/GetPressReleaseList` with `bodyType=2`. www.spglobal.com blocks scripts; use a same-origin `fetch` in the built-in browser. Rebuild with the scratchpad scripts described in `DIGEST.md` §1.
