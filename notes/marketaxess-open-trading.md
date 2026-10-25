# Note · MarketAxess Open Trading — all-to-all won the crisis argument and lost the routing argument; both venues now sell curation

> Practitioner / market-structure note · Maps to **Course 03** (Microeconomics — adverse selection, the winner's curse, auctions), **Course 04** (Competitive Strategy — counter-positioning, a brand built on one protocol), **Course 07** (Data, Analytics & Decision-Making — self-benchmarking, selection bias, counterfactual baselines), **E6** (Crisis Leadership & Resilience — liquidity in March 2020), **E8** (Stakeholder & Investor Relations — a KPI that disappears) · Written 2026-10-25 · Part of [[marketaxess-hub]]; companions [[marketaxess-protocols-automation]], [[marketaxess-data-cp-plus]], [[tradeweb-a2a-information-leakage]]

- **Source:** MarketAxess corpus (`_ingest/raw/marketaxess/articles.jsonl`), about **45 items** used: 22 earnings releases (4Q18–3Q26) and 8 news releases quoting Open Trading share and savings; the FY2019–FY2025 letters; the Dec 2025 Goldman Sachs deck; and about 25 Knowledge Center pieces (AxessPoints 2019–2026, the *Blockbusting* series, *How trades move markets*, the Targeted RFQ / AI Select / axes pieces, Oracle, Stellantis, Fed-day). Range **Jan 2019 – Oct 2026**. Caveats: most Knowledge Center dates are estimates (*How trades move markets* is stamped 2025 but uses an H2 2025 sample, so it is about 2026; *Seizing the opportunity* is stamped 2024 but cites a Nov 2024 launch and later data). Earnings texts are narrative only, with tables cut off. No call transcripts. Every price-improvement figure is MarketAxess's own estimate.
- **Core claim:** Open Trading (OT), MarketAxess's anonymous all-to-all pool, was the company's identity and its proof in stress. Its share of credit volume went **27% (2019) → 35% (March 2020) → record 37% (3Q22) and 38% (4Q22)**, then sat flat at **33–36%** through 4Q24, after which it stopped being headlined. Estimated client savings were **over $1B in 2020** (the letter says $1.1B, against $689M of revenue), **$570M in 2021**, **$945M in 2022** and either **$702M or ~$470M in 2023** (the 4Q23 release and the FY23 letter disagree). The last quarterly figure is **$119M in 3Q24**. MarketAxess's research says all-to-all does not leak: post-trade impact is a median **13% of bid-ask** in US HG, and adding OT to a dealer list leaves it roughly unchanged. Yet from 2024 its products moved to **curation**: Targeted RFQ, Smart Dealer Select, AI Select, Targeted Axes and Disclosed Open Trading. Its own research concedes the winner's curse and *selective distribution* for large illiquid trades. That is the same turn Tradeweb made in 2026 (*blast all → select smart*). The two venues disagree on how big the A2A leakage increment is (≈0 vs ≈0.07–0.15bp), and each measures it with its own reference price (CP+ vs Ai-Price).

---

## 1. Chronology — the share, the savings and the network

All figures are as MarketAxess states them (*MKTX says*) unless marked *derived*. *Share* = OT volume ÷ total credit volume on products where OT is offered. *Savings* (renamed *estimated price improvement* from 2023) = taker savings + provider savings (definitions in §2).

| Date (source) | OT share of credit volume | OT savings / price improvement | Volume / ADV / network | Context |
|---|---|---|---|---|
| 4Q18 (Jan 2019 release) | — | $57M in the quarter, a record | OT volume $117.5B (+96.5%); FY18 $376.5B | McVey: savings rise as credit spreads widen |
| 1Q19 (Live Markets release) | 26% of total volume | $51M taker + $44M provider | >$134B (+66%) | First split of the two savings legs |
| FY2019 (letter) | **27%** | $385M (per the Apr 2020 munis release) | OT volume $542.8B (+44%) | — |
| **Mar 2020** (FY19 letter) | **35%** | — | 10,000+ remote users onboarded | COVID; McVey calls OT liquidity "essential to the functioning of credit markets" |
| 1–3Q20 | 32% | $852M | $643B (+60%) | Savings above revenue "for the second quarter in a row" (2Q20) |
| **FY2020** (Jan 2021 release; FY20 letter) | about a third | **>$1B** (release) / **$1.1B** (letter) | $861.1B (+61%); 1,600+ OT firms; 25,000 daily opportunities, $16B notional | Revenue $689M, so savings ≈ **1.6x revenue** (*derived*) |
| 1Q21 | 33% | $196M | record $246.3B | Greenwich: A2A was 12% of US IG volume in 2020, mostly MKTX |
| 1–3Q21 | 32% | $445M | — | Low-volatility year |
| FY2021 (letter) | 35% (per the 4Q22 release comparison) | **$570M** | ~1,700 counterparty firms | Revenue $699M, so ≈ 0.8x (*derived*) |
| 2Q22 / 3Q22 | 35% / **37% record** | $238M ($1,030/mm) / $260M ($1,141/mm) | — | Rate shock |
| **FY2022** (4Q22 release; letter) | **36% record** (4Q22: **38%**) | **$945M** ($1,006/mm) | 1,700 OT firms | Letter: price improvement "in excess of our total annual revenue" ($718M) |
| 1Q23 | 37% (record US HG OT share 34%) | $252M ($902/mm) | record OT ADV $4.5B | — |
| 2Q23 / 3Q23 | 34% / 33% | $157M / $120M | — | 3Q23: down "on lower credit spread volatility" |
| **FY2023** | 36% (4Q23) | **$702M** (4Q23 release) vs **~$470M** (FY23 letter) | — | The two figures do not reconcile (§5) |
| 1Q24 / 2Q24 / 3Q24 | 34% / 34% / 35% | $141M / $110M / **$119M** (last figure published) | — | — |
| 4Q24 (Feb 2025 release) | 35% | not reported | OT ADV $4.1B (+2%) | Last time share is stated |
| 1Q25 | not reported | not reported | **record OT ADV $4.8B** | Tariff shock |
| FY2025 (letter; GS deck) | EM 27% / Eurobonds 26% (2020–24 average) | not reported | **1,000+ unique liquidity providers**; ~$4bn a day, 2,000+ participants (blurbs) | OT is recast as one plank of *differentiated liquidity* |

**Three readings from the table.** (1) Share moved with stress: up 8pp in March 2020 and 11pp from 2019 to 4Q22, then flat for two years. (2) Savings swing much more than share. Between 2020 and 2021 they halved while share held at about a third. That is expected if savings are mostly the spread between the winning price and the cover, which collapses when spreads are calm. (3) The disclosure trail runs out in order: penetration headlines after 4Q24, savings after 3Q24, and the savings-versus-revenue comparison after FY22.

## 2. How the savings are defined — and what that baseline assumes

The definition is printed as a footnote in every release from 2019 to 2024:

| Leg | MKTX definition | What it assumes (inference) |
|---|---|---|
| **Taker** (inquiry sender) | "the difference between the winning price and the best disclosed dealer cover price" | Without OT you would have traded at your best disclosed dealer's price. That is reasonable, but it is the *second*-best price in the stack, and dealers may have quoted differently had they known OT was absent. |
| **Provider** (OT responder) | the winning price versus "then current Composite+ bid or offer level", on the opposite side | Without OT the provider would have crossed the whole CP+ spread as a taker. That is the **maximum-cost** counterfactual, the same objection [[tradeweb-credit]] §4.2 makes to Tradeweb's Net Spotting savings. It is also measured against MKTX's own model. |

- **Both legs can be booked on one trade.** If an investor's OT bid fills another investor's OT-routed sell, the seller logs taker savings against the dealer cover and the buyer logs provider savings against CP+. MarketAxess's total adds the two (*inference*: the releases never say whether the same print is counted twice).
- **Pre-trade versions of the same metric.** *Estimating pre-trade OT cost savings* (undated) says taker savings have a "direct linear relationship" with the cover delta: a 1.5bp cover implies 1.8bp of savings, a 2bp cover 2.5bp, and "The correlation is an extremely high at 0.99." The 2019 provider study says provider savings run at "80-100% of bid/ask" (R² 79%). When bid/ask is 4bp, "the OTCS is expected to be 3.5 bps."
- **Read:** a 0.99 correlation with the cover delta is close to an identity. Savings are mostly *the dispersion of the quote stack*, which is why they double in stress and halve in calm markets. They measure how wide the market is, not how much OT adds net of what it leaks. MKTX's dealer-side version makes the same point: dealer OT savings in US IG went "from 5bps (Feb) to almost 17bps (March)" 2020, a 260% rise.

## 3. The evidence papers — what MarketAxess's research claims

| Paper (date, est.) | Sample / ruler | Finding (MKTX says) | Caveat it states itself |
|---|---|---|---|
| *Pre-trade OT cost savings, liquidity providers* (2019) | US IG, CP+ | Provider savings = 80–100% of the CP+ bid/ask | — |
| *Understanding TCA Outcomes in US IG* (2020) | US IG Jan–Nov 2020, TCA vs CP+ | Each extra response worth "~0.36 bps" (R² 93%); MKTX trades beat other TRACE activity by 1.1bp | — |
| *TCA Outcomes in European Credit* (2021) | Euro credit, vs CP+ | ~1.2 euro cents per extra response (R² >95%). Prescription: "invite as many disclosed dealers as possible alongside seeking anonymous liquidity via Open Trading®" | — |
| *Dealer RFQ Cost Savings via OT* (2020) | Dealer RFQs | 43% of dealer-RFQ trades are with non-dealers; non-dealer wins in US IG went from 28% to 50% in 2020; 7.6bp US IG savings in Q3 2020 | Saving is measured against the best dealer response |
| ***Blockbusting* Part 1** (2023) | US IG Q2 2023 | Tradability ≥5 lifts hit rates from 48–52% to 77–81%; blocks >$5mm still get 5+ prices | "Tradability does not directly address the challenge of information leakage" |
| ***Blockbusting* Part 2** (2023) | EUR IG, March 2023 stress, CP+ moves out to 120 min | No difference in impact across dealer count × OT; OT penetration 27.11%, 1.73 responses | Concludes "the additional access to liquidity that Open Trading provides outweighs the potential information leakage" |
| ***Blockbusting* Part 4** (Aug 2024) | US HG $5–10mm, >5yr, H1 2024 | "No deterioration in the quality of execution" from $1mm to $10mm; 26% of blocks at CP+ mid or better | Excludes trades under $1mm |
| ***How trades move markets*** (~2026) | **186,000 US HG + 52,000 EUR IG** trades, H2 2025, $150k–$25mm, CP+ mid 30 min after | Median impact **13%** (US HG) / **11%** (EUR IG) of bid-ask. Low-liquidity bonds 19% vs 11%. Impact plateaus above ~$2mm. Trading with the skew costs ~17% vs 8% against. Adding three counterparties ≈ 1% of spread in price improvement. "access to all-to-all liquidity is not the market impact penalty box." | "The model incorporates the traded level into its next prediction", so the study keeps only trades within one bid-ask of CP+. And: "Larger and less liquid trades may still call for more selective distribution." |

**What is strong here.** The 2026 study is the best piece in the corpus. It has a large N, states its sample filter, reports the full impact distribution (5th–95th percentile), separates liquidity, size and skew, and admits the CP+ circularity. Its hierarchy (liquidity → size → execution choice) is plausible and matches Tradeweb's finding that illiquid bonds leak 2–3x more ([[tradeweb-a2a-information-leakage]] §3).

## 4. The curation turn — 2024–2026

| Product (first seen) | What it does | Numbers MKTX gives | The language |
|---|---|---|---|
| **Targeted RFQ** (TRFQ; EM/Eurobonds Nov 2024, US credit 2Q25) | For tickets **>$3mm**, suggests up to **8** axed or recently active dealers; each dealer is told how many rivals it faces and why it was picked | Hit ratios ~**13%** above the platform average; clients invite **80%** of recommended dealers; electronic blocks >$3M **+22%** YTD in Asia; 100+ clients, 40 dealers | "maximising competition while minimising information leakage"; dealers wanted "a more contained environment with more transparency on the number of competing dealers" (Dan Burke) |
| **Smart Dealer Select** (SDS) | Picks disclosed dealers for sensitive inquiries from axes and activity; later adds TraX Active Dealers (~60% of EM HC APAC, ~70% of CEEMEA trade data) | Hit rates **>70%** for users (Asia) | For "larger—and more sensitive—inquiries" |
| **AI Select** (2025–26) | Ranks dealers on 30–60 weighted metrics (win rates, responsiveness, outcomes) | Best dealer predicted in **59%** of backtests (top-3 invited, one won) | "Instead of “blasting” inquiries broadly, traders can engage a curated set of counterparties" |
| **Targeted Axes** (pilot Nov 2025) | Dealers send firm, disclosed axes to chosen clients only; clients can *circle*; no last look | Pilot concluded with "strong feedback" | "without broadcasting it to the market" |
| **Disclosed Open Trading**, Bridge, Crossing (2025–26) | Name give-up *inside* the OT network, settled through MKTX; can go to "a single known dealer" | — | "bridge the gap between full disclosure and full anonymity" |
| X-Pro RFQ (3Q26) | Targeted and direct block workflows plus "AI-powered dealer selection" in one ticket | — | Concannon, 3Q26 |

**The concession, in MarketAxess's own words.** The Asia blocks piece: "Given the risk of the winner’s curse, sell side dealers could adopt a more defensive strategy when pricing bonds in anonymous liquidity pools." The impact study's hedge on *selective distribution*. And *AI in fixed income*: "By ensuring that large trades are directed only toward the most relevant counterparties, market impact can be reduced". The pitch changed from *add everyone* (2020–21 TCA papers) to *add the right ones* (2024–26), while the research headline stayed *A2A does not leak*.

## 5. What the claims don't prove

1. **The ruler is MarketAxess's own.** Savings (provider leg), TCA, *Blockbusting* and the 2026 impact study all use **CP+**, which is built partly from MKTX's own RFQ flow and updates on the traded level. This is the same problem [[tradeweb-a2a-information-leakage]] §4.1 raises about Ai-Price. MKTX at least names it and filters for it. Tradeweb's paper does not.
2. **Selection, not protocol.** Clients choose whether to tick the OT box. If informed or urgent sellers avoid OT on sensitive tickets (which is exactly what TRFQ and SDS are designed to let them do), then the OT-included group is biased toward benign trades, and *no measurable difference* is partly the routing working. The more curation tools succeed, the harder it gets to read the impact study causally.
3. **Savings are a gross figure.** No release nets savings against impact, against fees, or against the price the cover dealer would have shown without OT. *Savings exceed revenue* compares a gross client benefit with the company's revenue. It does not show that clients are net ahead.
4. **The numbers don't reconcile.** FY2023 price improvement is **$702M** in the 4Q23 release and **~$470M** in the FY23 letter, three months later (the quarters sum to $252M + $157M + $120M + $173M = $702M, *derived*). FY2020 is "over $1 billion" in the release and "$1.1 billion" in the letter. The share basis also shifts between *total global trading volume* (2019) and *credit volume where OT is offered* (2021 on).
5. **Survivorship in the stress stories.** The March 2020, March 2023, April 2025, Oracle and Fed-day pieces were published after OT did well. The Stellantis AxessPoint is the honest exception (§6). Mexico's USD-name OT share fell from 41% to 26% between 2020 and 2021 in a piece that does not flag it.
6. **The KPI vanished as the core stalled.** Penetration and savings were the headline proof from 2019 to 2022. They stopped as US HG share fell from 22.8% (4Q20) to 18.4% (4Q24) ([[marketaxess-strategy-financials]]). Flat OT share alongside falling HG share means OT stayed a constant slice of a shrinking pie.

## 6. Stress readings — where OT carries the market, and where it didn't

| Episode | Reading (MKTX says) | What it shows |
|---|---|---|
| **COVID, Mar 2020** | OT 35% of credit volume; US HG/HY OT penetration hit **46%** in one week, with 3.6bp (HG) and 59c (HY) of price improvement; EM OT +40%, dealers taking liquidity +258% | OT as the counterparty of last resort |
| **2022 rate shock** | Bid/ask 30% wider, but firm prices back steady and anonymous responses rising | Depth held where spreads did not |
| **SVB/CS, Mar 2023** (EUR IG) | No extra impact from OT; penetration 27.11% in line with other months | The no-leakage claim, in stress |
| **Tariff shock, Apr 2025** | Penetration 39% HG (1.87bp) / 38% HY (37c); OT more than doubled HG price improvement; algos ~80% of prices vs a fall from 60% to 50% in COVID; HG prices per RFQ 13.2 → 6.6 → 11.3 in a week | Stress is now absorbed by algos as well as by OT |
| **Fed days** (2024–26) | OT share of won trades "just under 30%" right after a release vs 23% on a normal Wednesday; cost <0.2bp worse | Small, regular stress events |
| **EM / MENA / Argentina** | OT 42% of EM hard currency (2020); 47% of MENA volume (2025); Argentina OT ADV $255m vs $176m (Oct 2025) | OT is strongest where dealer panels are thin |
| **Oracle** (data to Jul 28 2026) | OT share of won RFQs **20% → 30–40%** as ORCL widened to BB levels, vs ~25% typical in IG | OT share works as a *stress gauge* for one issuer |
| **Stellantis** (Feb–Sep 2026) | Seasoned-senior OT share **fell** 19.1% → 13.1%; OT rose only in new hybrids. "Open Trading rose in newly issued hybrids, not in seasoned senior bonds." | Not every repricing sends flow to OT. A two-way, issuer-specific move did not. |

## 7. Who supplies OT liquidity

- **Dealers as takers and providers.** "Dealers taking liquidity now make up nearly one-third of Open Trading volumes" (2026). The GS deck: **33%** of OT volume is initiated by dealers. Dealer RFQs routed to OT trade 43% with non-dealers (2020). Patrick Bailey says OT is the number one counterparty for most clients, and often "a top counterparty for even the largest bulge-bracket dealers".
- **Non-dealers.** "22% of OT trading volume responded to by non-dealers" (GS deck, 3Q25), so about **78% of OT volume is answered by dealers** (*derived*). OT is mainly a way for dealers to provide liquidity anonymously, not a buy-side-to-buy-side market. Named non-banks include Flow Traders (anonymous on OT for "many years", disclosed from Dec 2021), Virtu, Citadel Securities and Jane Street (RFQ-hub), ETF arbitrageurs (LQD/HYG names were 61% of 2022 OT inquiry volume) and systematic funds.
- **Algos.** Dealer algos answer **96%** of client RFQs in US/EUR HG and HY. In Q1 2025 they were the counterparty on **88%** of US HG trades (+21pp since Q1 2021), averaging 11 responses per inquiry: "It is becoming clear that algos are dominating the liquidity pool". Algos quote "$3–5 million" in liquid names and "increasingly remain switched on". **Inference:** a large share of what reaches clients as *anonymous all-to-all* is bank algos recycling risk. OT's resilience now depends on a handful of dealers keeping their models on, which is a concentration risk the research does not name.

## 8. Against Tradeweb — convergence, and where the evidence conflicts

| | MarketAxess | Tradeweb (context, from [[tradeweb-a2a-information-leakage]], [[tradeweb-credit]]) |
|---|---|---|
| A2A brand | OT since 2013; share 33–38% of credit volume | AllTrade: 25% IG / 43% HY of in-comp RFQ volume (2021), 32% HG / 44% HY (2023); *#4 dealer* with $1,573/mm price improvement (2021) |
| Benefit leg | Taker savings ≈ 1.2x the cover delta; $902–1,141/mm (2022–23); +0.36bp per extra response | A2A **+0.2bp** better execution than voice, IG >$1mm, 2025 (Ai-Price); tariff shock: A2A wins beat next-best disclosed by $2,751/mm IG |
| Impact leg | Median 13% of bid-ask, **≈ no OT increment** | **+0.07–0.09bp** buys / **+0.14–0.15bp** sells; ~0.2–0.3bp in illiquid bonds; 0.17bp more impact than voice |
| Net | Not computed | ≈ **+0.03bp** A2A ahead (0.2 − 0.17), from TW's own blog |
| Ruler | CP+ (MKTX model, uses MKTX flow) | Ai-Price (TW model, uses TW flow) |
| Product it sells | TRFQ, SDS, AI Select, Targeted Axes, DOT | SNAP+ (AI dealer selection) |
| Year of the turn | 2024 (TRFQ) → 2026 (AI Select, *blasting* language) | 2026 (*blast all → select smart*) |

- **Where they agree.** Impact is real and small. It is concentrated in illiquid bonds and in trades with the skew. The answer for large or illiquid tickets is a data-ranked shortlist. Both now sell an AI dealer recommender.
- **Where they conflict.** On the *increment* from going wide: MKTX finds roughly zero, Tradeweb finds a positive, side-asymmetric effect. **A rough reconciliation (inference):** MKTX's 13% of bid-ask on a ~1.5bp US HG CP+ spread (the BBB benchmark in the Oracle piece) is about **0.2bp** of total impact (*derived*), which is the same order as Tradeweb's 0.17bp. The disagreement is about attribution within a ~0.2bp move, inside most desks' TCA noise. Each venue's design fits its product. MKTX compares OT-plus-dealers with dealers-only on its own RFQs. Tradeweb compares A2A with *voice*.
- **Neither publishes the net.** MKTX reports gross savings and the impact study separately. Tradeweb's net comes from a blog, not the paper. Neither runs the test on the other's reference price.

## 9. How the narrative moved

1. **2019–2020: OT is the moat and the crisis proof.** Savings above revenue. "Without the open market — with its large, diverse pool of different types of participants" (FY19 letter). The NY Fed SMCCF eligible-seller designation confirms OT's role.
2. **2021: breadth is the prescription.** TCA papers tell clients to add every dealer plus OT. OT "now underpins nearly all of our trading protocols and products" (FY21 letter).
3. **2022–2023: record share, leakage answered with data.** "As traditional sources of liquidity have become scarcer, the importance of our all-to-all solution has increased" (FY22 letter). *Blockbusting* Part 2 says OT outweighs leakage.
4. **2024–2025: curation ships, metrics go quiet.** TRFQ and SDS arrive and the winner's-curse admission appears. Savings stop after 3Q24 and share after 4Q24.
5. **2026: two messages at once.** The research says OT "is not the market impact penalty box". The product marketing says stop "blasting". OT becomes one tool among several, and the volatility pieces say OT suits "the majority of market participants, but not all."

## 10. Strategic read (inference — not stated by MarketAxess)

- **OT was a counter-positioning moat that eroded once dealers automated.** In 2013–2020 incumbent dealers would not join an anonymous pool that competed with them, so MKTX owned it. Once dealer algos became the main OT responders (about 78% of OT volume is dealer-answered), the pool no longer sat outside dealer economics. It became one more channel where dealers recycle risk. Tradeweb could build AllTrade on top of its dealer franchise without the brand conflict.
- **The curation turn is a dealer-retention move.** TRFQ was designed on dealer feedback (Burke). DealerAxess, Mid-X and Targeted Axes court the sell side. A venue whose growth now depends on dealer-initiated flow ([[marketaxess-protocols-automation]]) cannot keep telling clients to broadcast to everyone.
- **OT is insurance priced by volatility.** The asset is real in March 2020, Oracle-style single-name stress and EM, and worth little in a calm IG tape. That is the business's volatility dependence in miniature ([[marketaxess-hub]] pattern 1).
- **Under ICE** (Jul 2026 deal, [[marketaxess-ice-deal]]): the 2024 ICE Bonds link already joins ICE's retail ATS to OT. The likely use (*speculation*) is OT as the institutional anonymous layer under a retail-plus-institutional network, with curation tools for the buy-side block business.

## 11. Canon lenses

- **Winner's curse and adverse selection** ([[canon-akerlof-market-for-lemons]], Course 03): in a wide anonymous auction the winning responder has the most optimistic quote and faces the most informed counterparty. Defensive quoting is the rational response. MKTX names it for Asia blocks.
- **Counter-positioning** ([[canon-helmer-7-powers]]): OT worked while dealers could not copy it without cannibalising their franchise. That power decays once incumbents (and Tradeweb) find a version that does not hurt them.
- **Selection bias and noise** ([[canon-kahneman-sibony-sunstein-noise]], Course 07): observational protocol comparisons fail when the chooser knows more than the regression. Curation tools make the selection worse.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): OT's value came from adding sides (non-dealers, ETF arbitrageurs, dealers as takers). The 22% non-dealer response share shows how far that went: real, but a minority.
- **Information goods** ([[canon-shapiro-varian-information-rules]]): CP+ is both the ruler and a product. Whoever owns the benchmark frames the debate.

## 12. Practitioner counterpoint

- **For MarketAxess:** OT's crisis performance is visible outside its own data. The NY Fed used the venue in 2020, Greenwich credits MKTX with most US IG A2A, and Tradeweb's own tariff-shock numbers show anonymous A2A beating disclosed quotes by thousands of dollars per million. Buy-side panelists (RBC BlueBay: "The Street is much more bought in than it was previously") describe finding counterparties they did not know existed.
- **Against:** savings are a gross, self-measured, cover-based figure that swings with spreads. Most OT liquidity is dealer algos. A desk selling $8mm of a liquidity-score-3 bond cares about the tail, not the median, and both venues concede the tail leaks.
- **Both:** run your own TCA on a third-party mid, split by side, liquidity score and *OT ticked or not*, and on the subset where curation tools were used. Treat each venue's paper as a hypothesis to test.

## 13. Open questions to track

1. Will ICE resume reporting OT share and price improvement, or fold OT into a broader *liquidity network* metric?
2. Can MKTX's impact study be rerun on Ai-Price, BVAL or next-TRACE-print mids, and Tradeweb's on CP+?
3. What share of TRFQ, SDS and AI Select tickets also tick OT? Is curation replacing OT or adding to it?
4. Does the non-dealer response share (22%) rise or fall as algos grow? Is a one-week algo pullback in stress (April 2025 halved HG prices per RFQ for a day) the new tail risk?
5. Which FY2023 price-improvement figure is right, $702M or ~$470M, and was methodology changed?

**Links:** [[marketaxess-hub]] · [[marketaxess-protocols-automation]] · [[marketaxess-data-cp-plus]] · [[marketaxess-strategy-financials]] · [[marketaxess-ice-deal]] · [[marketaxess-international-rates]] · [[tradeweb-a2a-information-leakage]] · [[tradeweb-credit]] · [[tradeweb-ai-price]] · [[tradeweb-hub]] · [[blackrock-hub]] · [[ice-hub]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[wss-credit-distressed]] · [[canon-akerlof-market-for-lemons]] · [[canon-helmer-7-powers]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-parker-platform-revolution]] · [[canon-shapiro-varian-information-rules]]

---
### Rep
You are selling **$8mm** of a US IG bond, spread duration **7**, CP+ bid-ask **1.5bp**, best disclosed cover **1.5bp** behind the best dealer bid. Use only this note's numbers.
(a) MKTX's pre-trade rule says taker savings ≈ 1.8bp for a 1.5bp cover. What is that in dollars if OT wins? (b) MKTX's median post-trade impact is 13% of bid-ask; Tradeweb's sell-side A2A leakage increment is ~0.15bp (or ~0.3bp in illiquid bonds). Convert each to dollars. (c) On Tradeweb's own figures (+0.2bp execution, −0.17bp impact), what is A2A's net edge in dollars on this ticket? (d) One paragraph: why (a) overstates the net benefit, and which two fields from your own TCA would settle it.

*(a) $8,000,000 × 7 × 0.00018 ≈ **$10,080**. (b) MKTX: 13% × 1.5bp ≈ 0.195bp → 8,000,000 × 7 × 0.0000195 ≈ **$1,092** of total impact, with roughly zero attributed to OT. Tradeweb: 0.15bp → **$840**, or 0.3bp → **$1,680** in illiquid names. (c) 0.03bp → 8,000,000 × 7 × 0.000003 ≈ **$168**. (d) The $10,080 is a gross figure against the second-best quote, measured on the venue's own model, and only when OT wins. The realistic net edge sits between (c) and (a) minus (b). Pull *OT ticked (Y/N)* and *post-trade mid move on a third-party price at +30 min*, split by liquidity score.*

---
**Sources (MarketAxess corpus, `_ingest/raw/marketaxess/articles.jsonl`, accessed 2026-10-25):**
- [4Q18 results, 2019-01-30](https://investor.marketaxess.com/news/news-details/2019/MarketAxess-Reports-Fourth-Quarter-2018-Revenues-of-112.4-Million-Pre-Tax-Income-of-56.1-Million-and-Diluted-EPS-of-1.21-01-30-2019/default.aspx) · [Live Markets announcement, 2019-05-09](https://investor.marketaxess.com/news/news-details/2019/MarketAxess-Developing-Live-Order-Book-for-Institutional-Fixed-Income-Market-05-09-2019/default.aspx)
- [2019 letter, 2020-04-29](https://s201.q4cdn.com/767283836/files/doc_financials/2019/ar/MKTX_Annual-Report_2019.pdf) · [2020 letter, 2021-04-28](https://s201.q4cdn.com/767283836/files/doc_financials/2020/ar/MKTX_Annual-Report_2020.pdf.pdf) · [2021 letter, 2022-04-27](https://s201.q4cdn.com/767283836/files/doc_financials/2021/ar/Proxy-book-2022-color.pdf) · [2022 letter, 2023-04-26](https://s201.q4cdn.com/767283836/files/doc_financials/2022/ar/Posting-179619_MarketAxess-Holdings_COMBO-PRoxy-AR_WEB-HOSTING_rev2_MS.pdf) · [2023 letter, 2024-04-24](https://s201.q4cdn.com/767283836/files/doc_financials/2023/ar/327161_MARKETAXESS-HOLDINGS-INC-_10K_2024_V1_PWO-34656_PROOF_rev3_MS_DY.pdf) · [2025 letter, 2026-04-29](https://s201.q4cdn.com/767283836/files/doc_financials/2025/ar/MarketAxess-Holdings-Inc-2025-10-K-ARS.pdf)
- [Goldman Sachs / Live Markets, 2020-10-21](https://investor.marketaxess.com/news/news-details/2020/Goldman-Sachs-Adds-Streaming-Firm-Pricing-to-MarketAxess-Live-Markets-Order-Book-10-21-2020/default.aspx) · [Barclays / Live Markets, 2021-05-27](https://investor.marketaxess.com/news/news-details/2021/Barclays-Adds-Streaming-Firm-Pricing-To-MarketAxess-Live-Markets-Order-Book-05-27-2021/default.aspx) · [Flow Traders, 2021-12-07](https://investor.marketaxess.com/news/news-details/2021/Flow-Traders-Takes-a-New-Market-Position-as-an-Active-Liquidity-Provider-on-MarketAxess-12-07-2021/default.aspx)
- [4Q20 results, 2021-01-27](https://investor.marketaxess.com/news/news-details/2021/MarketAxess-Reports-Fourth-Quarter-2020-Revenues-of-171.3-Million-Operating-Income-of-91.7-Million-and-Diluted-EPS-of-1.91-01-27-2021/default.aspx) · [4Q22 results, 2023-01-25](https://investor.marketaxess.com/news/news-details/2023/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2022-Results/default.aspx) · [4Q23 results, 2024-01-31](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2023-Results/default.aspx) · [3Q24 results, 2024-11-06](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-Third-Quarter-2024-Financial-Results/default.aspx) · [4Q24 results, 2025-02-06](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx) · [1Q25 results, 2025-05-07](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Reports-First-Quarter-2025-Financial-Results/default.aspx) · [3Q26 results, 2026-10-23](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Third-Quarter-2026-Financial-Results/default.aspx); other quarterly figures from the 2020–2024 earnings releases listed in `index.tsv`
- [GS Financial Services Conference deck, 2025-12-09](https://s201.q4cdn.com/767283836/files/doc_downloads/2025/12/11/Goldman-Sachs-Financial-Services-Conference-Final.pdf)
- [Pre-trade OT cost savings, liquidity providers, 2019](https://www.marketaxess.com/articles/axesspoint_pre-trade-open-trading-cost-savings_liquidity-providers) · [Estimating pre-trade OT cost savings, undated](https://www.marketaxess.com/articles/axesspoint_estimating-pre-trade-open-trading-cost-savings) · [Dealer RFQ cost savings, 2020](https://www.marketaxess.com/articles/axesspoint_dealer-rfq-cost-savings-via-open-trading) · [TCA outcomes US IG, 2020](https://www.marketaxess.com/articles/axesspoint_understanding-tca-outcomes-in-us-Investment-grade) · [TCA outcomes European credit, 2021](https://www.marketaxess.com/articles/axesspoint_understanding-tca-outcomes-in-european-credit-markets)
- [Diverse participants (2020, re-posted 2025)](https://www.marketaxess.com/articles/axesspoint-diverse-participants-create-liquidity-opportunities-during-credit-market-stress) · [We're here to help, undated](https://www.marketaxess.com/whats-new/whats-new-we-re-here-to-help-open-trading-is-how) · [A tale of two metrics, 2022](https://www.marketaxess.com/articles/a-tale-of-two-metrics_us-ig-corporate-bond-market-liquidity-in-2022)
- [Blockbusting Part 1, 2023](https://www.marketaxess.com/articles/blockbusting-part-1-pre-trade-intelligence-and-understanding-market-depth) · [Part 2, 2023](https://www.marketaxess.com/articles/blockbusting-part-2-examining-market-impact-of-client-inquiries) · [Part 4, 2024-08](https://www.marketaxess.com/articles/blockbusting-part-4-block-execution-in-ushg) · [How trades move markets, ~2026](https://www.marketaxess.com/articles/how-trades-move-markets-a-data-driven-exploration-of-market-impact)
- [Pre-Trade data strategy, undated](https://www.marketaxess.com/articles/pre-trade-data-strategy-optimizing-protocol-selection-in-european-credit) · [Scaling up EM HC with Targeted RFQ, undated](https://www.marketaxess.com/articles/scaling-up-em-hard-currency-trading-with-targeted-rfq) · [Seizing the opportunity (Asia blocks), ~2025](https://www.marketaxess.com/articles/seizing-the-opportunity-how-electronic-trading-is-enabling-larger-trades-in-asia-credit) · [Smart Dealer Select enhanced, undated](https://www.marketaxess.com/whats-new/whats-new-your-smart-dealer-select-now-enhanced)
- [Sourcing liquidity through a connected ecosystem, 2026-02](https://www.marketaxess.com/articles/sourcing-liquidity-through-a-connected-ecosystem) · [OT: sourcing liquidity in times of volatility, 2026-02](https://www.marketaxess.com/articles/open-trading-sourcing-liquidity-in-times-of-volatility) · [Targeted axes, 2026-02](https://www.marketaxess.com/articles/targeted-axes-precision-control-and-efficiency) · [Axe quality in electronic credit markets, 2026-02](https://www.marketaxess.com/articles/axe-quality-in-electronic-credit-markets-what-the-data-tells-us) · [AI in fixed income, 2026-02](https://www.marketaxess.com/articles/ai-in-fixed-income-from-fragmentation-to-intelligent-execution)
- [April volatility AxessPoint, 2025](https://www.marketaxess.com/articles/axesspoint-credit-markets-showed-resilience-through-april-volatility) · [Algos in block trading, 2025](https://www.marketaxess.com/articles/axesspoint-the-expanding-role-of-algos-in-block-trading-and-market-liquidity) · [Fed-day dynamics, ~2026](https://www.marketaxess.com/articles/fed-day-dynamics-in-a-post-forward-guidance-era) · [Oracle, 2026](https://www.marketaxess.com/articles/axesspoint-oracle-investment-grade-rating-high-yield-reality) · [Stellantis, 2026](https://www.marketaxess.com/articles/axesspoint-stellantis-sector-pressure-and-issuer-specific-repricing) · [DealerAxess (WatersTechnology), 2025-09-16](https://www.marketaxess.com/articles/marketaxess-enhances-dealer-value-through-its-new-dealeraxess-service)
