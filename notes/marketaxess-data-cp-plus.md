# Note · MarketAxess data, CP+ & TraX — the venue turned its inquiry exhaust (including trades that never happened) into prices, tapes and indices, but the data line stayed small and the accuracy evidence stayed self-graded

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — data as a platform by-product, who owns the reference price), **Course 07** (Data, Analytics & Decision-Making — what a MAD comparison does and doesn't measure, shifting denominators), **Course 02** (Corporate Finance & Valuation — sizing a data line inside a $5.7B EV deal), **E10** (Digital & AI Transformation — "AI-based" pricing as product and as label), **E3** (M&A — why ICE wanted the flow) · Written 2026-10-25 · Part of [[marketaxess-hub]]; companions [[marketaxess-international-rates]], [[marketaxess-open-trading]], [[marketaxess-ice-deal]], [[tradeweb-ai-price]], [[tradeweb-tech-ai-data]]

- **Source:** MarketAxess corpus (`_ingest/raw/marketaxess/articles.jsonl`), **~45 items, Apr 2019 – Oct 2026**: IR releases (Refinitiv 2019, Regulatory Reporting Hub 2020, Axess All Prints, MKTX 400 and MSCI 2022, the three Bloomberg/MarketAxess/Tradeweb consolidated-tape statements 2022–23, S&P Global 2024, muni CP+ 2024, TraX Tape 2026, Arcesium 2026), the ICE release on MSCI MarketAxess futures (Dec 2024), 32 earnings releases for the services-revenue lines, the FY19–FY25 letters, the 2021 Investor Day and Dec 2025 Goldman Sachs decks, and ~20 Knowledge Center pieces on CP+, TraX, SensAI and transparency reform. **Caveats:** earnings releases are cut before the financial tables, so some full-year services lines are derived by summing quarters (labelled). Most Knowledge Center dates are estimates; *Bringing transparency to the muni marketplace* is tagged 2017 but describes the Dec 2024 muni CP+ launch. The CP+ whitepaper and the SS&C study itself are not in the corpus. No call transcripts.
- **Core claim:** MarketAxess's data business rests on one asset rivals can't buy: the full stack of dealer responses on every inquiry, **including the ones that did not trade** (*1.6 million* firm prices on did-not-trade inquiries in US IG in Q4 2023 alone). From that it built **CP+** (launched 2017; "over 24,000 bonds" in 2019 → "more than 33,000 instruments" as the corporate boilerplate → *~930,000* munis from Dec 2024; two-sided every 15–60 seconds), the **TraX** post-trade/APA/ARM hub (enlarged by Deutsche Börse's Regulatory Reporting Hub, Nov 2020), the **Axess All** EU tapes, tradable **indices** (MKTX 400 → SSGA's LQIG ETF; MSCI MarketAxess indices → ICE futures) and the **TraX Tape** (Jun 2026). Distribution went through rivals and partners: **Refinitiv** (2019, now LSEG, Tradeweb's controlling shareholder), **S&P Global** (Oct 2024, CP+ inside S&P Evaluated Bond Pricing), FactSet, Arcesium. But the money stayed modest: information services were **$39.3M in FY22** and about **$53M in FY25** (derived from quarters), ~6% of revenue; all services together were a record **$111.6M** (13%). The accuracy story is self-graded: the headline **MAD of 1.095bp vs 1.395bp** compares on- vs off-platform *trades* against CP+, which MKTX itself says measures trade consistency, and the 2025 SS&C study is cited only as *among the top*, with no error figure and **no head-to-head against BVAL, ICE, Ai-Price or Trumid**. The strategic point is the buyer: ICE, the evaluated-pricing incumbent, is buying the flow that S&P's corporate evaluations now lean on.

---

## 1. Chronology — the data stack, as MarketAxess states it

*All figures are MarketAxess's (or the named partner's) unless marked derived.*

| Date | Event | Detail (as stated) |
|---|---|---|
| 2015 | **Axess All** launched | Described in 2022 as "the first intra-day trade tape for the EU and UK fixed income markets": delayed, aggregated by bond, ~7,000 instruments |
| May 2017 | **Composite+ (CP+)** launched | 2021 Investor Day: *Launched May 2017*; muni release: "First introduced to the market in 2017" |
| Feb 27 2019 | Dutch AFM approves Trax NL as a DRSP (APA + ARM) | Post-Brexit EU reporting and transparency footprint |
| Apr 11 2019 | **Refinitiv** redistributes CP+ and Axess All on Elektron | CP+: "updates up to every 15 seconds on over 24,000 bonds", combining TRACE with platform and Trax data. Refinitiv's Carley: best-execution pressure means traders "need more data" |
| Apr 2020 | FY19 letter calls Composite+ "our AI-based, real-time bond pricing solution" | Pitched as the engine behind automation (Auto-X), not as a product line |
| May 2020 | **Sonar** (post-trade reporting surveillance) | Uses the industry-wide reporting data set of "900+ clients" |
| Sep 23 → Nov 30 2020 | **Regulatory Reporting Hub** bought from Deutsche Börse via Trax NL | MiFID II / EMIR transaction reporting, APA and ARM services; Germany, France, Nordics. Added **$13.0M** of 2021 reporting revenue |
| Mar 9 2022 | **Axess All Prints** | Real-time trade-by-trade prices "on over 15,000 executed trades across approximately 4,250 unique instruments" |
| Mar 16 2022 | **MKTX US IG 400**, first tradable index | Built on Relative Liquidity Score and CP+; SSGA's SPDR MarketAxess IG 400 ETF (**LQIG**) launched May 12 2022 (release body not retrievable; named in the 2Q22 results) |
| Apr 28 2022 | **MSCI** strategic collaboration | MarketAxess liquidity data (RLS, Tradability) into MSCI indexes and analytics; MSCI ESG ratings the other way. "subject to the execution of definitive agreements" |
| Jun 22 2022 | **Bloomberg, MarketAxess and Tradeweb** "jointly explore" an EU fixed-income consolidated-tape bid | As a JV "established and operated independently from our respective businesses" |
| May 23 2023 | JV agreement **signed** | Neil Ryan to lead; FINBOURNE chosen as technology provider |
| Dec 8 2023 | JV **abandoned** | Cited "risk and complexity" and "uncertain outcomes around product definitions and structural complexities" |
| Jan 31 2024 | MKTX stops publishing EM and Eurobond market share | Those shares "historically have been derived from MarketAxess TraX data"; methodology under review |
| Apr 2024 | *CP+ under the hood* | On-/off-platform MAD comparison, DNT impact study (§3) |
| Oct 31 2024 | **S&P Global Market Intelligence** partnership | S&P bond reference data into MKTX; CP+ into S&P Evaluated Bond Pricing (**1.2M+** bonds); integration expected to start 1H25 |
| Dec 5 2024 | **CP+ for munis** | "~930,000 municipal bonds" |
| Dec 12 2024 | **ICE** lists **MSCI MarketAxess** tradable corporate bond index futures | Four contracts (USD IG/HY, EUR IG/HY); methodology uses MKTX Relative Liquidity Scores |
| Jun 2 2025 | S&P's Gonska: S&P's service has "exclusive access to MarketAxess CP+" | Munis named as S&P's next priority |
| 2025 | *CP+ ranks as a top provider in the 2025 SS&C* study | "over 350,000 firm prices back per day" (Q3 2025); covering "over 97% of market prints daily" |
| Dec 9 2025 | GS deck | CP+ "provided to our partner, SPGI, as input into evaluated price for large index funds/ETFs"; "400M+ responses annually" |
| Jun 18 2026 | **TraX Tape** launched (London) | Consolidated, de-duplicated, direction-flagged, CP+-enriched |
| Oct 7 2026 | **Arcesium** integrates CP+ and TraX (Aquata, Opterra) | TraX covers "more than 42,000 global fixed income instruments"; Repo Match: 127 firms, >$700bn matched ADV |

## 2. The money — how big the data line actually is

| Period | What MKTX reports | Amount | Note |
|---|---|---|---|
| FY2018 → FY2019 | *All other revenue* (information + post-trade + other) | $44.7M → $47.5M | FY19 increase "principally due to higher information services revenue of $2.5 million" |
| 2016 → 2Q21 TTM | Market data revenue (Investor Day chart) | ~9% 5-year CAGR | Composite+, Axess All, Trax, BondTicker and bulk data shown as one line; values not legible in extraction |
| FY2020 | All other revenue | $54.7M (+15.1%) | Includes $3.6M of new data sales |
| FY2021 | All other revenue | $77.9M (+42.5%) | $13.0M of the $23.3M increase is the Deutsche Börse hub |
| FY2022 | Information services / post-trade services | **$39.3M** / **$36.9M** | Info +3% (≈+9% ex-FX); post-trade −5% |
| FY2023 | Information + post-trade | ~$87M (+14%, FY23 letter) | Info ≈ **$46.4M** (derived, sum of quarters $11.0/11.7/11.8/11.9M) |
| FY2024 | Services (info + post-trade + technology) | **$105.4M** (+18%) | Now includes Pragma technology services; info ≈ **$50.6M** (derived) |
| FY2025 | Services | **$111.6M** (+6%) | Info ≈ **$53.3M** (derived: $12.9/13.1/13.8/13.5M); post-trade ≈ $44.5M (derived) |
| 2Q26 / 3Q26 | Services; information services | $31.5M (record) / $30.5M; info $16.1M (+$3.0M) / $15.2M (+10%) | Growth "driven by net new contract revenue" |

*Derived reads.* Information services were ~**6.3%** of FY25 revenue ($53.3M / $846.3M). For scale: Tradeweb's market-data line was $133.7M in FY25 (context, from [[tradeweb-ai-price]]), so MKTX's information line is ~**40%** of Tradeweb's. ICE's FY25 fixed-income data & analytics revenue was $1,234M (context, from [[tradeweb-ai-price]]), about **23×** MKTX's. Valued as a stand-alone line, CP+ cannot be what ICE paid ~$5.7B for. Its value is as an *input* to execution (Auto-X, Mid-X, auctions, PT) and to someone else's much larger pricing business.

## 3. CP+ machinery — what the inputs are and what the "accuracy" numbers measure

**The moat claim.** CP+ "uses the entire stack of inquiry responses sent to the platform by liquidity providers, regardless of whether the bond traded or not" (SS&C piece). In Q4 2023 US IG the platform saw "more than 1.6 million firm prices back on DNTs". The study finds DNTs move CP+ about as much as a real trade from elsewhere: "The magnitude of this impact is comparable to that of an off-platform trade." Its conclusion: platform context "sets CP+ apart from pricing solutions that rely solely on public trade tapes."

**The numbers MarketAxess publishes:**
- **MAD, Q4 2023, US IG, trades ≥ $150k:** "the CP+ MAD was 1.095 bps for on-platform trades and 1.395 bps for off-platform trades". Off-platform dispersion is ~27% higher (derived). Read the caveat MKTX itself prints: with CP+ fixed, "comparing the MAD is effectively measuring the consistency of the traded levels on and off platform". This is a test of **trade quality**, not of **CP+ against a rival**. It also flatters on-platform trades that CP+ already sees: 96% of US IG client RFQs went to Open Trading, and CP+ prices are the reference those trades are struck against.
- **Update response:** a trade 4bp inside the CP+ side moves CP+ 1.24bp (median); an on-platform trade 2bp away moves it 1.54bp; a DNT best level 5bp inside moves it 1.5bp. That shows the model **shrinks** toward new prints (good: no overfitting). It is not an error statistic.
- **Stress dispersion (Euro IG, 2020):** "74% trade levels were within 10 cents of Composite+ side" in January, 25% in March, 65% in October. The one stress number in the corpus, and it shows the hit rate collapsing by two-thirds at the point of maximum need.
- **Retail:** orders under $150k have average TCA "within 1 cent of CP+ side".
- **SS&C 2025:** CP+ "has once again ranked among the top pricing providers". No rank, no error, no peer names in the MKTX write-up.

**The boilerplate drifts.** Coverage is "more than 33,000 instruments" (2023–24 AxessPoints), "more than 25,000 instruments globally" (a 2025 AxessPoint), "more than 350,000 bonds globally" (the muni piece, presumably counting munis), and "~930,000" munis. Activity is "nearly 30 million levels per day", "nearly 20 million", "over 30 million" and "more than 50 million". Coverage is "90-95% of trading activity", "over 97% of market prints" and "100% coverage in its markets". None of these is wrong on its own definitions, but none comes with one.

**Cross-check with [[tradeweb-ai-price]].** That note's landscape table lists CP+ with *none* published for accuracy and finds no vendor publishing a same-side baseline. Trumid claims its FVMP beats CP+ by 11% (self-reported). The MKTX corpus doesn't change any of that. It adds one thing: SS&C's independent study includes MarketAxess but not Tradeweb, and MKTX publicises its placing without the numbers.

## 4. TraX and the European tape — selling the gap between regulation and usability

- **The reform.** FCA and ESMA reforms lift real-time publication of corporate bond prices to an estimated **80–90%** of trades, from ~**30%**. But the two regimes create "68 distinct deferral scenarios across corporate and sovereign bonds", and MKTX estimates **~15%** of IG corporate volume still gets the longest deferral (three months FCA, four weeks ESMA).
- **What TraX shows that the tape doesn't.** In the first week of December 2025, TraX showed **€80bn** a day of clean IG corporate volume versus an estimated **€32bn** visible from combined FCA and ESMA reporting, so public data showed ~40% of the market (derived). APAs delayed ~75% of volumes. In January 2026 TraX published **233,342** trades that would not have been published under either regime.
- **Quality.** "nearly 40% of published trades from the top 10 APAs are not immediately usable, most commonly due to duplication" (Q1 2025 data).
- **The model.** TraX Volume aggregates data from "more than 50 dealers and clients" who contribute in exchange for access. It is a *give-to-get* club. TraX covered "85% of the European" market in 2025, up from the ~75% (2Q22) and ~70% (3Q22) MKTX used as its Eurobond share denominator.
- **The pitch.** "Europe’s transparency reforms promised consolidation; instead, they are delivering choice." And: the US shows the end state "is rarely “raw tape only”". Berry: "The data tells you what happened, and TraX Tape tells you what it means."
- **The consolidated-tape arc.** Explore (Jun 2022) → sign (May 2023) → abandon (Dec 2023) → MKTX's own commercial tape (Jun 2026) built to sit **on top of** the public CTPs it once bid to run. A *Predictions 2023* piece expected a tape in "18-24 months"; per a 2026 MKTX piece, the ESMA tape's planned go-live is Q1 2027, after TraX Tape launched.
- **Post-trade AI.** SensAI: "more than 1 billion trades were replayed via this ARM" in 2023, on average 243 days after trade date. The moat line: "The only other entities with access to MarketAxess’s multi-firm data set are regulators."

## 5. How the narrative moved

1. **2019–21: data as fuel for automation.** CP+ is "AI-based" (FY19 letter), then "A.I.-powered" (FY21). Its job is to set Auto-X and Mid-X levels and define Open Trading *provider savings*. Distribution goes through Refinitiv. Data revenue is buried in *all other revenue*.
2. **2022–23: data as product and index.** Axess All Prints, the MKTX 400, MSCI. Concannon: "MarketAxess has a unique view into the traditionally fragmented and less liquid fixed income market." Information services get their own line. The three rivals try to build the EU tape together and give up.
3. **2024–25: data as someone else's valuation input.** S&P EVB, ICE futures, FactSet, the ETF/NAV pitch with DWS. Sweeney: the goal is to "close the gaps between best execution, intraday trading decisions and end-of-day valuation". In the FY25 letter CP+ becomes the third leg of the *MarketAxess advantage*.
4. **2026: data as the asset in a sale.** TraX Tape, Arcesium. Then ICE, whose data business dwarfs MKTX's, buys the flow.

## 6. What the claims don't prove

1. **No head-to-head accuracy.** No CP+ error statistic against BVAL, ICE CEP, S&P, Ai-Price or FVMP appears anywhere in 359 items. The only external benchmark (SS&C) is reported as a placing without a number.
2. **The MAD test is about the trades, by MKTX's own description.** Lower dispersion of on-platform trades against CP+ is also what you'd expect if on-platform trades are *anchored on* CP+ (Auto-X pegs, provider-savings definitions, Mid-X strikes). That's reflexivity, not proof of edge.
3. **Undefined coverage.** 25k vs 33k vs 350k vs 930k instruments; 90–95% vs 97% vs 100% coverage. Without a fixed universe, "coverage" can't be compared over time or against rivals.
4. **Stress evidence cuts the other way.** The one stress cut (Euro IG, March 2020: 74% → 25% within 10c) is the case for a model price, and the weakness of one, in the same chart.
5. **The tape numbers are TraX measuring the public tapes TraX competes with.** €80bn vs €32bn and 40% unusable come from MKTX's own cleansing algorithm on its own contributor data. Its age is also inconsistent: "refined over 10 years" (Jun 2026 release) vs "refined for over 20 years" (the 2026 research piece).
6. **Index and ETF traction is never sized.** No LQIG assets, no futures open interest, no index licence revenue. Announced products (Virtu eNAV in 2019) are still "upcoming" in a 2025 AxessPoint.
7. **Exclusivity is S&P's word, not a disclosed term.** "exclusive access to MarketAxess CP+" comes from S&P's Gonska. Its scope, duration and change-of-control treatment are not in the corpus.
8. **Self-sourced superlatives.** A What-if blog credits MKTX with an "electronic credit trading market share of over 70%" in the same paragraph that puts it at ~20% of TRACE IG volume. Whatever the denominator, it isn't stated.

## 7. Strategic read *(inference — not stated by MarketAxess)*

- **The asset is the inquiry log, not the model.** Anyone can fit a gradient-boosted model to TRACE. Only the venue sees *who was asked, who answered, at what level, and who passed*. DNTs are the part of the order book that TRACE never shows. That is a cornered resource ([[canon-helmer-7-powers]]). It also explains the 2024 disclosure retreat: TraX-derived EM and Eurobond shares were dropped exactly as the data started being sold to others.
- **MKTX chose to be an input supplier, not a pricing brand.** Rather than fight ICE and Bloomberg for evaluated-pricing mandates, it put CP+ inside S&P's EVB. That brought distribution without the auditor-facing burden, but it gave up ownership of the end-of-day price that ETF NAVs and index funds settle on. It is coopetition on S&P's terms ([[canon-brandenburger-nalebuff-coopetition]]).
- **The venue-line sort now has a crossover.** [[tradeweb-ai-price]] reads the market as S&P ↔ MKTX, LSEG/FTSE ↔ Tradeweb, with ICE and Bloomberg integrated. The MKTX corpus confirms it and adds a twist: CP+'s first redistributor (2019) was Refinitiv, now LSEG. After the ICE close, **S&P's corporate evaluations rest on a feed owned by a direct evaluated-pricing competitor**. That is the clearest antitrust and partner-retention question in [[marketaxess-ice-deal]] (see also [[spglobal-hub]], [[ice-hub]], [[lseg-hub]]).
- **TraX Tape is a hedge against the regulation that funded TraX.** APA and ARM revenue is compliance rent. A free public CTP erodes the basic tape, so MKTX moves up a layer: direction flags, de-duplication, CP+ context. That is the TRACE-enhanced-data playbook moved to Europe. The abandoned JV suggests the rivals concluded the regulated baseline isn't where the margin is.
- **Why ICE wanted it.** ICE already owns the evaluated-pricing book, index franchises and the MSCI futures that use MKTX liquidity scores. CP+ and DNT data are a real-time, trade-adjacent feed to sit under them ([[canon-shapiro-varian-information-rules]]: near-zero marginal cost, value in bundling). The data line is small in revenue and large in **option value** inside a bigger stack.

## 8. Canon lenses

- **Information goods** ([[canon-shapiro-varian-information-rules]]): CP+ is versioned (intraday FIX, files, Excel, EOD inside S&P) and priced by use case. The lock-in is that clients tune Auto-X rules and TCA history against it.
- **Cornered resource / counter-positioning** ([[canon-helmer-7-powers]]): pure evaluators can't see DNTs. MKTX can't match their audit trail and coverage of the illiquid tail, hence the S&P deal.
- **Noise** ([[canon-kahneman-sibony-sunstein-noise]]): DWS's Lenamon frames pricing skew between evaluated prices and traded levels as a tracking-error cost. A shared reference price cuts noise and concentrates model risk.
- **Calibration** ([[canon-tetlock-superforecasting]]): a two-sided price implies an uncertainty band. Publishing hit rates inside it by liquidity bucket would be the honest scorecard.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): the three rivals co-bid for the EU tape, then each sold its own enrichment layer.

## 9. Practitioner counterpoint

- **For:** S&P chose to plug CP+ into its flagship evaluation service rather than build its own, and ICE built futures on MKTX liquidity scores. Those are revealed preferences by the two firms best placed to judge. DWS uses CP+ in its ETF create/redeem workflow, and the DNT data is genuinely unique.
- **Against:** the data business is ~6% of revenue after seven years of effort, with no published head-to-head accuracy and coverage claims that move with the brochure. A buyer can't tell from the corpus whether CP+ beats BVAL on the bonds that matter (illiquid, stressed). DWS's endorsement is hedged: "a great tool to help us potentially minimize tracking error".
- **Both:** CP+ is probably excellent where MKTX has flow (US IG/HY, EM hard currency) and borrowed elsewhere (S&P covers "very illiquid bonds"). Its proven value is as the price that MKTX's own protocols clear against. That's why it's worth more to an owner of protocols plus evaluations (ICE) than to the market as a stand-alone feed.

## 10. Open questions to track

1. Does the S&P–CP+ arrangement survive ICE's change of control, and does S&P disclose terms or a replacement plan?
2. Will ICE publish CP+ in its own evaluated-pricing stack, or keep it as an execution-only input?
3. Any CP+ error statistic against a named competitor, or a same-side baseline, after the merger (or in the 2026 SS&C study)?
4. TraX Tape: paying subscribers, and how it is licensed once the ESMA and FCA CTPs go live?
5. LQIG assets and MSCI MarketAxess futures open interest: do the indices have traction or only announcements?
6. Does post-trade (APA/ARM, SensAI) grow once deferrals shorten, or shrink as public tapes commoditise it?
7. Will the EM and Eurobond share series (dropped Jan 2024) come back on an ICE basis?

**Links:** [[marketaxess-hub]] · [[marketaxess-international-rates]] · [[marketaxess-open-trading]] · [[marketaxess-ice-deal]] · [[marketaxess-protocols-automation]] · [[marketaxess-strategy-financials]] · [[tradeweb-ai-price]] · [[tradeweb-tech-ai-data]] · [[tradeweb-hub]] · [[spglobal-hub]] · [[ice-hub]] · [[lseg-hub]] · [[bloomberg-hub]] · [[blackrock-hub]] · [[market-structure-24-5-trading]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-tetlock-superforecasting]]

---
### Rep
You run pricing and valuation at a $60bn bond-fund complex that uses S&P evaluated prices for NAV. ICE's purchase of MarketAxess closes in 1H 2027. Use only numbers from this note.

**(a) Size the line.** From the quarterly figures, compute FY25 information-services revenue and its share of FY25 revenue ($846.3M). Compare it with Tradeweb's FY25 market-data revenue ($133.7M) and ICE's FY25 fixed-income data & analytics revenue ($1,234M).

**(b) Read the MAD.** CP+ MAD is 1.095bp on-platform vs 1.395bp off-platform. Compute the ratio. In one sentence, say what the comparison does and does not show about CP+ versus a competitor.

**(c) Price the gap.** TraX shows €80bn a day of IG volume vs €32bn publicly visible. What share of the market does the public tape show? If 40% of APA prints need cleaning, what share of the true market is immediately usable from public sources alone (assume the 40% applies uniformly)?

**(d) Decide.** One paragraph: do you ask S&P for a contractual commitment on CP+ inputs past the ICE close, and what single number from MarketAxess would change your answer?

*Answers:* (a) $12.9 + 13.1 + 13.8 + 13.5 = **$53.3M**, ~**6.3%** of revenue; ~**40%** of Tradeweb's market-data line and ~**4.3%** of ICE's. (b) 1.395 / 1.095 ≈ **1.27×**. It shows on-platform trades sit closer to CP+ than off-platform ones. It does not compare CP+ to any other vendor's price, and by MKTX's own description it measures trade consistency. (c) 32 / 80 = **40%** visible. 40% × 60% clean ≈ **24%** of true volume usable as-is. (d) Yes, because after the close your evaluator's corporate input is owned by a competitor. The number that would change it is a published CP+ error against BVAL or ICE on the same illiquid trades. If CP+ is no better, the dependency isn't worth defending.

---
**Sources (MarketAxess corpus, `_ingest/raw/marketaxess/articles.jsonl`, accessed 2026-10-25):**
- [Refinitiv to Redistribute MarketAxess’ Fixed Income Market Data Solutions, 2019-04-11](https://investor.marketaxess.com/news/news-details/2019/Refinitiv-to-Redistribute-MarketAxess-Award-Winning-Fixed-Income-Market-Data-Solutions-04-11-2019/default.aspx)
- [2019 Annual Report: Letter to Stockholders, 2020-04-29](https://s201.q4cdn.com/767283836/files/doc_financials/2019/ar/MKTX_Annual-Report_2019.pdf) · [2021 Letter, 2022-04-27](https://s201.q4cdn.com/767283836/files/doc_financials/2021/ar/Proxy-book-2022-color.pdf) · [2022 Letter, 2023-04-26](https://s201.q4cdn.com/767283836/files/doc_financials/2022/ar/Posting-179619_MarketAxess-Holdings_COMBO-PRoxy-AR_WEB-HOSTING_rev2_MS.pdf) · [2023 Letter, 2024-04-24](https://s201.q4cdn.com/767283836/files/doc_financials/2023/ar/327161_MARKETAXESS-HOLDINGS-INC-_10K_2024_V1_PWO-34656_PROOF_rev3_MS_DY.pdf) · [2025 Letter, 2026-04-29](https://s201.q4cdn.com/767283836/files/doc_financials/2025/ar/MarketAxess-Holdings-Inc-2025-10-K-ARS.pdf)
- [Data is king, 2020-05](https://www.marketaxess.com/articles/data-is-king) · [MarketAxess to Acquire Regulatory Reporting Hub, 2020-09-23](https://investor.marketaxess.com/news/news-details/2020/MarketAxess-to-Acquire-Regulatory-Reporting-Hub-from-Deutsche-Brse-Group-09-23-2020/default.aspx)
- [2021 Virtual Investor Day presentation, 2021-09-14](https://s201.q4cdn.com/767283836/files/doc_presentation/2021/09/2021-Investor-Day-Presentation.pdf) · [Goldman Sachs 2025 Financial Services Conference presentation, 2025-12-09](https://s201.q4cdn.com/767283836/files/doc_downloads/2025/12/11/Goldman-Sachs-Financial-Services-Conference-Final.pdf)
- [Axess All Prints launch, 2022-03-09](https://investor.marketaxess.com/news/news-details/2022/MarketAxess-Launches-Axess-All-Prints-Offering-Real-Time-Price-Transparency-for-EU-and-UK-Fixed-Income-Markets-03-09-2022/default.aspx) · [Launch of Tradable Index (MKTX 400), 2022-03-16](https://investor.marketaxess.com/news/news-details/2022/MarketAxess-Expands-Data-Intelligence-Suite-With-Launch-of-Tradable-Index-03-16-2022/default.aspx) · [MSCI and MarketAxess Strategic Collaboration, 2022-04-28](https://investor.marketaxess.com/news/news-details/2022/MSCI-and-MarketAxess-Announce-Strategic-Collaboration-on-Liquid-Fixed-Income-Indexes-Portfolio-Construction-Solutions-and-ESG-Data-04-28-2022/default.aspx)
- [Bloomberg, MarketAxess and Tradeweb Explore EU Consolidated Tape, 2022-06-22](https://s201.q4cdn.com/767283836/files/doc_news/2023/03/bloomberg-marketaxess-and-tradeweb-explore-eu-consolidated-tape-for-fixed-income_22-june-2022.pdf) · [Sign Joint Venture Agreement, 2023-05-23](https://investor.marketaxess.com/news/news-details/2023/Bloomberg-MarketAxess-and-Tradeweb-Sign-Joint-Venture-Agreement/default.aspx) · [Statement on Joint Venture Agreement, 2023-12-08](https://investor.marketaxess.com/news/news-details/2023/Statement-from-Bloomberg-MarketAxess-and-Tradeweb-on-Joint-Venture-Agreement/default.aspx)
- [Use AI and be more human, 2022](https://www.marketaxess.com/articles/use-ai-and-be-more-human) · [Regulatory reporting inaccuracies, 2023](https://www.marketaxess.com/articles/regulatory-reporting-inaccuracies-its-better-to-know-than-be-told) · [Predictions: Will 2023 be the year of transparency, 2023](https://www.marketaxess.com/articles/will-2023-be-the-year-of-transparency-in-fixed-income-markets)
- [CP+ under the hood, 2024-04](https://www.marketaxess.com/articles/cp-plus-under-the-hood-how-trades-and-inquiries-impact-pricing) · [AxessPoint: Euro IG price dispersion during volatility, undated (2020)](https://www.marketaxess.com/articles/axesspoint_euro-investment-grade-price-dispersion-during-volatility) · [What if fixed income index constituents were accurately priced in real-time?, undated](https://www.marketaxess.com/articles/what-if-fixed-income-index-constituents-were-accurately-priced-in-real-time) · [The power of data in trading protocol selection, undated](https://www.marketaxess.com/articles/the-power-of-data-in-trading-protocol-selection)
- [S&P Global MI and MarketAxess Strategic Fixed-Income Data Partnership, 2024-10-31](https://investor.marketaxess.com/news/news-details/2024/SP-Global-Market-Intelligence-and-MarketAxess-Announce-Strategic-Fixed-Income-Data-Partnership-2024-RkDUQUX-8E/default.aspx) · [S&P Global MI × MarketAxess collaborate (Traders Magazine), 2025-06-02](https://www.marketaxess.com/articles/sp-global-market-intelligence-marketaxess-collaborate) · [CP+ for ETFs, 2026](https://www.marketaxess.com/articles/cp-for-etfs-improving-etf-portfolio-management-with-predictive-pricing)
- [CP+ expands to Municipal Bonds, 2024-12-05](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Expands-AI-Powered-Pricing-Engine-to-Cover-Municipal-Bonds/default.aspx) · [Bringing transparency to the muni marketplace (tagged 2017, ~2024–25)](https://www.marketaxess.com/articles/bringing-transparency-to-the-muni-marketplace-with-ai-powered-pricing)
- [ICE Launches MSCI MarketAxess Tradable Corporate Bond Index Futures, 2024-12-12](https://ir.theice.com/press/news-details/2024/ICE-Launches-MSCI-MarketAxess-Tradable-Corporate-Bond-Index-Futures-to-Help-Investors-Hedge-Corporate-Bond-Exposure/default.aspx)
- [CP+ ranks as a top provider in the 2025 SS&C study, 2025](https://www.marketaxess.com/articles/cp-ranks-as-a-top-provider-in-the-2025-ss-and-c-fixed-income-study) · [AxessPoint: retail corporate bond trading, 2025](https://www.marketaxess.com/articles/axesspoint-the-new-era-of-corporate-bond-trading-for-retail-investors)
- [Europe’s bond transparency regimes put data in the spotlight, 2025](https://www.marketaxess.com/articles/europe-s-bond-transparency-regimes-put-data-in-the-spotlight) · [The market is adapting: six months of transparency reform, 2026](https://www.marketaxess.com/articles/the-market-is-adapting-what-six-months-of-transparency-reform-reveal-about-how-bonds-trade) · [Enhancing data usability under new regulatory changes, 2026](https://www.marketaxess.com/articles/enhancing-data-usability-and-market-visibility-under-new-regulatory-changes) · [MarketAxess Introduces TraX Tape, 2026-06-18](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Introduces-TraX-Tape-Delivering-an-Enriched-View-of-Bond-Market-Activity/default.aspx) · [Arcesium Integrates Additional MarketAxess Data, 2026-10-07](https://investor.marketaxess.com/news/news-details/2026/Arcesium-Integrates-Additional-MarketAxess-Data-and-Analytics-to-Enhance-Fixed-Income-Workflows-2026-kGl0BkGatP/default.aspx)
- Earnings releases for services revenue: 4Q18, 4Q19, 4Q20, 4Q21, 4Q22, 1Q23–4Q23, 1Q24–4Q24, 1Q25–4Q25, 1Q26–3Q26 (investor.marketaxess.com, 2019-01-30 → 2026-10-23)
