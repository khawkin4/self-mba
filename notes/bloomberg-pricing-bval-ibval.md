# Note · Bloomberg evaluated pricing (BVAL → IBVAL) — owning the reference price, then making every protocol, index and future clear against it

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — cornered resource, vertical integration, who owns the ruler), **Course 07** (Data, Analytics & Decision-Making — self-graded accuracy, coverage denominators, baselines), **Course 03** (Microeconomics & Strategy Foundations — information asymmetry, reference-price conflicts), **Course 11** (Global Strategy, Macro & Responsible Business — China/Hong Kong pricing roles, local valuation regimes), **E10** (Digital & AI Transformation — ML pricing as product), **E9** (Geopolitics & Macro — CFETS, NAFMII) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-indices]], [[bloomberg-electronic-trading]], [[bloomberg-enterprise-data]], [[tradeweb-ai-price]]

- **Source:** Bloomberg corpus `_ingest/raw/bloomberg/articles.jsonl`, about **35 items** that mention BVAL, IBVAL, CBBT, LQA, MIPD or a market-on-close (MOC) reference, **Jun 2021 – Oct 2026**. They are press releases (bloomberg.com via Wayback, plus PR Newswire for 2026), Professional Insights pieces (Krein/Simek pricing series, Sharaby on credit futures, the Singapore summit write-up, APAC Regulatory Outlook 2026), one Tech-at-Bloomberg story (the IBVAL build, 2023-12-04) and Chartis award releases. One quote comes from the Tradeweb corpus (Hult). Bloomberg is private: there is **no revenue, price or client count for BVAL anywhere in the corpus**. The IBVAL back-test whitepaper is *not* in the corpus; its figures are cited from [[tradeweb-ai-price]] as context.
- **Core claim:** Bloomberg's fixed-income position does not depend on venue share, which it never publishes. It depends on **owning the reference price**. BVAL (launched 2008, "over 2.5 million" to "2.8 million" securities depending on the release) became the input to MIPD, LQA-adjacent analytics, the loan indices and the portfolio-trading (PT) basket reference. IBVAL started as "BVAL’s intraday pricing product" (2022), was relaunched as **IBVAL Front Office** (Oct 2023: ~30k USD corporates, as fast as every 15s, ML), was extended to Europe (Apr 2024), Asia and Australia (2025), and by Feb 2026 is described as "now the default pricing source on the Bloomberg Terminal" for >90k bonds. The same price is then reused as the **close in MOC list trades** (EGB, Apr 2024), the engine of the **Tradable Trackers**, the fair-value input for **CME/Eurex futures on Bloomberg indices**, the yardstick for dealer responses inside Rule Builder, and a quasi-public utility (HKSAR calculating agent; BVAL on CFETS). What Bloomberg does not publish is an **accuracy number**. The BVAL Score measures data density, not error. The only back-test figures (‘centered’; 92% inside CBBT) grade Bloomberg against Bloomberg, and coverage counts drift from release to release.

---

## 1. Chronology — the spine

All figures as Bloomberg states them ("BBG says") unless another source is named.

| Date | Event | Numbers stated |
|---|---|---|
| **2008** | BVAL launched (per the 2023-12-04 story), born of the crisis need for "more robust independent pricing" | — |
| 2020-10-28 | BBH + Bloomberg BSKT ETF primary-market workflow. Evaluated pricing pitched as the intraday ETF tracker | — |
| **2021-06-09** | **Portfolio Trading Basket Builder (PTBB)**: baskets compared to BVAL and **CBBT**, RFQ to up to 6 dealers via BOLT | BVAL "over 2.7 million securities" |
| 2021-07-27 | **MIPD** (market-implied probability of default) built on BVAL data | 36,000+ issuers, 1–20y term structure |
| 2021-08-02 | Distributes **BPAM** (Malaysia's accredited evaluator) on the Terminal | — |
| 2021-09-15/24 | Southbound Bond Connect: BVAL shown on the **CFETS** platform, the first time on a third-party system in China | BVAL "over 2.5 million securities" |
| 2021-09-22 | Fixed-income pre-trade TCA model, calibrated on 5 years of trades, with the CBBT bid-ask as an input | — |
| 2022-01-20 | Sony Bank takes BVAL into AWS as its ‘official valuation’ for traders and middle office | BVAL ">2.5 million" |
| **2022-06-23** | **Tradable Trackers** announced, priced by IBVAL, "BVAL’s intraday pricing product" | First tracker 200 bonds, due Q4 2022 |
| 2022-07-12 → 2023-10-25 | Chartis "Evaluated Pricing and Data" wins, five years running | BVAL 2.5m (Jul 2022) → 2.7m (Jul 2023) → 2.8m (Oct 2023) |
| **2023-10-17** | **IBVAL Front Office** launched on the Terminal (IBVL PCS) and B-PIPE. Engine for the Tradable Trackers | ~30,000 TRACE-eligible USD IG/HY, "as fast as every 15 seconds" |
| 2023-12-04 | Build story: ensemble of regression trees, Iceberg/Trino data lake, retrain in under 6 hours | BVAL "2.8 million securities, 10 times per day". 6–7bn ticks/day ingested, 300k/s peak. 350,000+ Terminal users |
| 2024-02-21 | IBVAL embedded in **AIM, ETOMS, Rule Builder (RBLD)** | "nearly 30,000" USD bonds |
| **2024-04-16** | **IBVAL to EUR/GBP** IG and HY (all bonds in the flagship Europe/UK indices). BVAL Score 1–10, I- and G-spreads added | — |
| **2024-04-24** | **First EGB MOC list trade referencing BVAL as the close** (J.P. Morgan vs a European insurer, on Bloomberg's MTF, via PTBB) | — |
| 2024-06 / 09 | Credit futures on Bloomberg indices listed at CME and Eurex (see [[bloomberg-indices]]) | — |
| 2024-07-02 | Chartis 2024 | IBVAL "approximately 45,000" USD/GBP/EUR credit bonds |
| 2024-09-09 | Krein/Simek "pricing is foundational to automation". IBVAL live in RBLD and PTBB | — |
| 2024-10-15 | **US Leveraged Loan Index** built on BVAL loan pricing | 1,300 loans, $1.3tn; 74,000 tranches priced |
| **2024-12-16** | **HKSAR official calculating agent** (GSBP/IBP green and infrastructure bonds), indicative prices and yields twice a day since 2024-10-23 | HKD 5.5bn and CNY 1bn inaugural issues |
| 2025-04-10 | Tradable Trackers described. Used with PTBB and FAIR<GO> for futures fair value | 5 tickers. ~100 issuers (~200 HY), 2 bonds each. R² 99.5% vs US IG Corporate |
| 2025-07-07 | Krein (Pricing & Valuations Summit, May 2025): PT share of US IG risk trades | ~25% (Mar 2025), from just over 20% (Jan) |
| 2025-07-22 | Global and European leveraged loan indices on BVAL | GLOAN $1.8tn; 82,000+ loans |
| 2025-11-17 | **Australia**: BVAL adds 600 ABS to 1,600 RMBS. IBVAL during Australian hours. Mid/ask issuer curves "from requirements" of APRA | — |
| 2025-11-26 | Singapore summit: IBVAL used as a dealer-response benchmark in Rule Builder. **Asia coverage "50,000 to 100,000 bonds by year-end"** | — |
| **2026-02-02** | APAC Regulatory Outlook: **NAFMII bond-valuation guideline** effective April 2026 | — |
| **2026-02-18** | Sharaby: IBVAL is "now the default pricing source on the Bloomberg Terminal". Govvies every second | **>90,000 bonds globally**. 10 futures, ~$300bn notional traded, OI >$4.5bn (Sept 2025) |
| 2026-02-26 | Kaiko/Canton: Data License **evaluated pricing on-chain** for tokenized UST and repo | — |
| 2026-06-02 | Spread-to-Benchmark quoting for EUR/GBP PT baskets, alongside BVAL-referenced spread workflows | — |
| 2026-10-04 | First fully automated **JGB MOC** (BB3P/Hikene reference, not BVAL). MOC now spans UST, Canada, Gilts, EGBs, JGBs | — |

## 2. The product stack, and what each layer reuses

| Layer | What it is | Refresh / coverage (BBG-stated) | Reused by |
|---|---|---|---|
| **BVAL** | End-of-day / multi-snapshot evaluated pricing, bonds and OTC derivatives; BVAL Score 1–10 | 2.5m–2.8m securities, "10 times per day" | MIPD, loan indices, PTBB reference, EGB MOC close, HKSAR-style roles, CFETS display, Data License, on-chain via Kaiko |
| **IBVAL Front Office** | ML (tree ensemble) intraday price, trained on TRACE plus contributed quotes and trades | 15s (corporates), 1s (liquid govvies); 30k → 45k → >90k bonds | Terminal default, B-PIPE, AIM, ETOMS, RBLD, PTBB, Tradable Trackers |
| **CBBT** | "a weighted average of dealer-contributed near real-time prices on Bloomberg’s Fixed Income Trading solution (FIT) during trading hours" | — | PTBB comparison, pre-trade TCA input, the automation-performance study, SOFR-liquidity evidence (2022) |
| **LQA / MIPD** | ML liquidity cost (since 2016) and market-implied default probability | MIPD 36k issuers | Regulatory liquidity reporting (SFC), risk |
| **Tradable Trackers** | Liquid-subset bond indices priced by IBVAL | ~15s | Futures fair value (FAIR), PT replication, iNAV |
| **MOC / list trading** | All-or-none list at a close reference | BVAL (EGB), BB3P (JGB) | Bloomberg MTF, TSOX, RBLD |

The design choice is to make **one price appear everywhere**. Krein and Simek frame it as "Pricing for corporate bonds has three core principles: It must be consistent, it must be readily available, and it must be high-quality." Of the three, the corpus documents the first two at length. It does not document the third.

## 3. How the narrative moved

1. **2008–2021: the independent evaluator.** Boilerplate calls BVAL "independent and transparent", built for thinly traded securities, and sold to the middle office. Brad Foster's MIPD pitch is that CDS is too thin, saying "while CDS prices can serve as indicators, they are often limited with fewer issuers traded and reduced liquidity", so BVAL data stands in.
2. **2021–2022: the price moves into the trade.** PTBB puts BVAL and CBBT next to dealer quotes. Tradable Trackers make an index tradable intraday, with IBVAL "enhanced to bridge the gap between trading and index pricing". Sony Bank wants its traders to see the middle office's ‘official valuation’.
3. **2023–2024: ML and the front office.** IBVAL is relaunched as "a new offering, distinct from but complementary to Bloomberg’s leading evaluated pricing service, BVAL". O'Brien's origin story: "With the electronification of fixed income markets, plus internal needs, we recognized there was a clear demand for intraday pricing". The moat claim is scale: "it’s really the scale of our data that enables us to lead in this category and be best-in-class." Europe follows within six months, and BVAL becomes the **close** in an MOC protocol.
4. **2024–2025: the utility role.** Bloomberg is appointed HKSAR calculating agent and cites a record of "calculating and distributing reference rates on behalf of central banks, ministry of finance and market associations". It adds loan pricing and indices, and APRA-driven curves in Australia.
5. **2026: the default.** "IBVAL, available for more than 90,000 bonds globally, is now the default pricing source on the Bloomberg Terminal." The framing becomes a continuum: "Harmonized analytics mean that an ETF, an index and a futures contract can now be evaluated on an apples-to-apples basis in real time." No release says when the default switched or what it replaced.

## 4. The loop: price → index → protocol → futures

```
 TRACE + contributed quotes/trades + FIT/CBBT flow
        │
   BVAL (EOD, 2.8m) ──► Bloomberg indices (loans on BVAL; Agg family) ──► CME/Eurex credit futures
        │                        ▲                                         │
   IBVAL (15s, >90k) ──► Tradable Trackers ──► FAIR<GO> fair value ◄───────┘ executed via EMSX / RFQe
        │
        └─► PTBB / MOC-to-BVAL / RBLD limits / dealer-response scoring ──► Bloomberg MTF, BOLT, TSOX
```

*Inference:* each arrow lifts switching costs. A desk that sets Rule Builder tolerances against IBVAL, builds PT baskets against BVAL, closes EGB lists at BVAL and hedges with a future whose fair value comes from an IBVAL tracker has four workflows to re-baseline if it changes pricer. Tradeweb is building the same loop from the venue side (Ai-Price → AiEX → FTSE closing prices; context, from [[tradeweb-ai-price]]). Bloomberg builds it from the data side. Tradeweb's CEO names the threat, which Bloomberg never does: "There was always Bloomberg looming out there at a minimum as a data company that was beginning to show prices for things." (Hult, 2026-08-05, Tradeweb corpus)

## 5. Competitive frame (context, from sibling notes)

| Vendor | Product | Published accuracy | Starting asset |
|---|---|---|---|
| **Bloomberg** | BVAL / IBVAL FO | ‘centered’; 92% of trades inside CBBT bid/ask (context, from [[tradeweb-ai-price]]); BVAL Score not an error metric | Terminal flow, FIT/CBBT, TRACE, 2.8m-security history |
| **ICE** | Evaluations, CEP (since 2015) | 38% IG / 79% HY ‘closer to the next trade’ vs ICE's own 2018 model (context, from [[ice-fixed-income-data]]) | ~3m instruments by roll-up; buying MarketAxess flow |
| **MarketAxess** | CP+ | MAD on-platform vs off-platform trades; no vendor head-to-head (context, from [[marketaxess-data-cp-plus]]) | Inquiry exhaust incl. did-not-trade prices |
| **Tradeweb** | Ai-Price | ~30% better than last-print predictor (context, from [[tradeweb-ai-price]]) | Own RFQ/PT flow |
| **S&P Global** | Evaluated Bond Pricing | none; rents CP+ for corporates (context, from [[spglobal-pricing-fixed-income]]) | Quotes/composites, audit trail |

Bloomberg is the only one that owns **pricer + index administrator (BISL) + venues + desktop** without a parent or a pending deal. ICE gets close only once MarketAxess closes (context, from [[ice-fixed-income-data]]). The only independent bake-off cited anywhere in the sibling notes, SS&C's 2025 vendor study, includes BVAL; no published ranking for it appears in the corpus.

## 6. What the claims don't prove

1. **No accuracy number at all.** In ~35 items, Bloomberg never states an error statistic for BVAL or IBVAL: no bp, no points, no hit rate by liquidity bucket. The words are qualitative ("high-quality", "accurate", "defensible"). The Feb 2024 piece claims IBVAL "was carefully built to address both usability and accuracy considerations". That is a design goal, not a result.
2. **The BVAL Score is a data-density score.** Bloomberg says so itself: "A lower score indicates there was less comparable market data available to derive the IBVAL price." A 9 means many inputs, not small error. Treating it as confidence is the client's inference.
3. **The one back-test grades Bloomberg against Bloomberg.** The ‘92% inside CBBT bid/ask’ figure (context, from [[tradeweb-ai-price]]) uses Bloomberg's own dealer composite as the ruler. A test inside a band is only as strict as the band is narrow, and for illiquid HY the CBBT band can be wide. ‘Centered’ says the bias is near zero, not that dispersion is small.
4. **Awards are self-submitted.** The five Chartis wins rest on a process the release itself describes: "Placement in Chartis ranking reports is determined based on the detailed research submissions of participating companies". They are not a trade-level test.
5. **Coverage drifts and sometimes runs backwards.**
   - BVAL: "over 2.7 million" (Jun 2021) → "over 2.5 million" (Sept 2021, Jan 2022, Jul 2022) → 2.7m (Jul 2023) → 2.8m (Oct 2023). Different universes (all asset classes vs fixed income) are mixed without labels.
   - IBVAL: ~30k (Oct 2023) → ~45k (Jul and Dec 2024) → Asia "from 50,000 to 100,000 bonds by year-end" (Nov 2025) → **"more than 90,000 bonds globally"** (Feb 2026). A global total below the Asia target means either the target slipped or the counts measure different things.
   - Refresh: "as fast as every 15 seconds" (2023–24) vs "nearly every 15 seconds" (Dec 2024). Both are ceilings, not the median update interval for an illiquid bond.
   - Tradable Trackers: "200 liquid bonds" (2022–23) vs ~100 issuers × 2 bonds (IG) and ~200 issuers (HY) (2025).
6. **The input story wobbles.** The 2023 launch lists "TRACE, contributed quotes and trades, and more". Sept 2024 says "Bond prices are the only inputs", while Feb 2024 says illiquid bonds require "adjacent bonds and market betas (such as indexes and ETFs) to establish reasonable pricing guideposts". If ETF and index betas are excluded, stress-period pricing of illiquid names is exactly where the model is least tested.
7. **The reference-price conflict is never discussed.** When BVAL is the MOC close on Bloomberg's own MTF, Bloomberg is pricer, venue operator and (via BISL) index administrator for the benchmark the client tracks. No release mentions governance, challenge processes for an MOC close, or what happens when BVAL is wrong at 4pm.
8. **Survivorship.** No piece covers BVAL or IBVAL in March 2020, the 2022 gilt crisis or April 2025. The LQA profile admits the credibility problem from the inside: "Bloomberg has long proven to its own satisfaction through backtests that its machine learning liquidity models are more accurate". Bloomberg's own TCA team writes that fixed-income raw material is "often sparse, fragmented, flat-out stale or incomplete." (2026-10-13)
9. **‘Default pricing source’ is undated and undefined.** The release does not say for which users, functions or asset classes, or what share of Terminal price displays it now drives.

## 7. Strategic read (inference — not stated by Bloomberg)

- **The price is the cornered resource; the venue is the monetiser.** Bloomberg never publishes credit venue share. It does not need to: if the default price on 350k+ screens is IBVAL, every RFQ on any venue is judged against a Bloomberg number. That is the counter-model to Tradeweb's flow-first play in [[tradeweb-credit]].
- **‘Default’ is a distribution weapon, not a quality claim.** Making IBVAL the Terminal default turns a premium feed into the habit-forming baseline traders see first, the same tactic as a browser's default search engine. The sale then happens in B-PIPE and Data License, where the money is (see [[bloomberg-enterprise-data]]).
- **The loop is fragile where the input is thin.** Trade-driven ML pricing is strongest in liquid USD IG, where Tradeweb, MarketAxess and ICE also see flow. Bloomberg's edge is breadth (2.8m securities, loans, ABS/RMBS, Asia). That edge is the least verifiable one, and it is the one the 2026 NAFMII guideline targets in China.
- **China is the exposure.** BVAL displayed on CFETS (2021, reaffirmed 2025) is a privilege granted by a state venue. NAFMII's guideline aims to "level the playing field for valuation providers within the interbank bond market". Read with the BPAM precedent (a regulator-accredited local evaluator, which Bloomberg distributes), the likely path is local champions accredited onshore, with Bloomberg reduced to a distributor there. Bloomberg's brief reports the rule without comment.
- **Sovereign utility roles are the moat's legitimacy layer.** HKSAR calculating agent, ISDA fallback agent and IBOR fallbacks (see [[bloomberg-indices]]) make Bloomberg's numbers official. Each role is low-revenue but hard to dislodge, and it lends authority to the commercial price.
- **On-chain pricing is the same play on new rails.** Kaiko/Canton puts Data License evaluated pricing on-chain so counterparties "reference a single, verifiable source, reducing reconciliation risk". Tokenized collateral needs a mark, and Bloomberg wants to be the mark rather than the chain.

## 8. Canon lenses

- **Cornered resource and switching costs** ([[canon-helmer-7-powers]]): history and coverage are the cornered resource. Embedding in AIM/ETOMS/RBLD/PTBB/MOC creates switching costs that are procedural, not contractual.
- **Information goods and versioning** ([[canon-shapiro-varian-information-rules]]): BVAL EOD, multi-snapshot, IBVAL 15s, IBVAL 1s govvies, Score, curves and on-chain marks are one dataset sold at different resolutions.
- **Vertical integration and buyer power** ([[canon-porter-competitive-strategy]]): pricer + index + venue + desktop reduces dependence on any one channel. It also invites the conflict question in §6.7.
- **Measurement and noise** ([[canon-kahneman-sibony-sunstein-noise]]): a vendor that sets the ruler (CBBT), the score (BVAL Score) and the default display should be treated as an unaudited forecaster until scored externally.
- **Systems loops** ([[canon-meadows-thinking-in-systems]]): price → index → future → hedge flow → TRACE prints → price is a reinforcing loop. If traders anchor on IBVAL, prints cluster near IBVAL and back-tests flatter it (reflexivity).
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Bloomberg distributes BPAM and reports NAFMII neutrally while competing to be the onshore mark.

## 9. Practitioner counterpoint

- **For Bloomberg:** BVAL is a 17-year, regulator-facing utility used for NAVs, risk and audit, in asset classes (ABS, RMBS, loans, munis, Asia credit) that trade-driven newcomers barely cover. The IBVAL build details (tree ensembles, retrain under six hours, 6–7bn ticks a day) are concrete and plausible. The Ortiz line, "we ultimately settled on using tree-based methods as these methods could scale better when compared to the alternatives", reads like engineering, not marketing. J.P. Morgan and BlackRock appearing as first MOC counterparties suggests large firms accept the reference.
- **Against:** ‘default’ plus ‘no published error’ is a trust-me position, and so is a BVAL Score that measures inputs, not outcomes. In thin markets a model that predicts the next print may simply learn the dealer composite. Clients who use IBVAL as the referee of dealer responses inside Rule Builder ("compare dealer responses against Bloomberg’s IBVAL pricing source") are delegating best-execution judgment to an unaudited model.
- **Both:** a desk should run its own **side-matched, out-of-sample** test (IBVAL vs CP+, CEP, Ai-Price, next round-lot TRACE print), split by liquidity bucket and stress window, before letting any vendor price set auto-ex limits or MOC closes. That is the same test [[tradeweb-ai-price]] asks Tradeweb to publish.

## 10. Open questions to track

1. Will Bloomberg publish an **absolute IBVAL error** (bp or points, by bucket, including March 2020 or April 2025), or enter SS&C's ranking publicly?
2. When did IBVAL become the **Terminal default**, and for which functions? Is BVAL still the default anywhere?
3. **Coverage reconciliation:** did Asia reach 100k? What is the universe behind ">90,000 globally"?
4. **NAFMII:** does BVAL keep its CFETS display after April 2026? Does an onshore accredited evaluator replace it?
5. Does **MOC-to-BVAL** spread beyond EGBs (UST, Gilts, credit)? What is the governance for challenging a BVAL close?
6. **Credit futures:** do open interest and volume on Bloomberg-index futures keep growing past ~$300bn cumulative notional? Does Cboe/ICE (MSCI MarketAxess indices) take share?
7. After **ICE–MarketAxess** closes, does an ICE CEP + CP+ stack force Bloomberg to publish accuracy to defend mandates?
8. Does on-chain evaluated pricing (Kaiko/Canton) become a reference in a live tokenized repo or collateral workflow?

**Links:** [[bloomberg-hub]] · [[bloomberg-indices]] (Agg, Tradable Trackers, futures, fallbacks) · [[bloomberg-electronic-trading]] (MTF, BOLT, MOC, PTBB, RFQe) · [[bloomberg-enterprise-data]] (Data License, B-PIPE, Kaiko) · [[bloomberg-buyside-stack]] (AIM, RBLD, BTCA) · [[bloomberg-ai-strategy]] · [[bloomberg-mission-forces]] · [[bloomberg-outside-voices]] · [[bloomberg-people]] · [[bloomberg-terminal-instrumentation]] (the Terminal as interface; not repeated here) · [[tradeweb-ai-price]] · [[tradeweb-credit]] · [[ice-fixed-income-data]] · [[marketaxess-data-cp-plus]] · [[spglobal-pricing-fixed-income]] · [[market-structure-24-5-trading]] · [[wss-credit-distressed]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-porter-competitive-strategy]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-meadows-thinking-in-systems]] · [[canon-brandenburger-nalebuff-coopetition]]

---
### Rep
Three short computations with numbers from this note. Assumptions are labelled.

**(a) Refresh-frequency math.** IBVAL updates "as fast as every 15 seconds". Assume a 9-hour US credit session (8:00–17:00 ET; an assumption, not a Bloomberg figure). How many price updates per bond per day at the ceiling, and across 30,000 bonds (Oct 2023) and 90,000 bonds (Feb 2026)? Compare with BVAL's 2.8m securities × 10 snapshots, and with the 6–7bn ticks a day IBVAL ingests. *(Answer: 4/min × 540 min = **2,160** per bond. × 30k = **64.8m**; × 90k = **194.4m** a day. BVAL: 2.8m × 10 = **28m**. Ingest per output at 30k bonds: 6.5bn / 64.8m ≈ **100 ticks in per price out**. Then argue: for an HY bond that trades twice a week, how many of those 2,160 updates carry new information? What does "as fast as" hide?)*

**(b) Coverage growth and drift.** IBVAL went from ~30k (Oct 2023) to >90k (Feb 2026), about 2.33 years. Compute the CAGR. Then compute IBVAL's share of the BVAL universe at 2.8m. Finally, explain the inconsistency between Nov 2025's Asia target of 100k by year-end and Feb 2026's 90k global total. *(Answer: 3^(1/2.33) − 1 ≈ **60% a year**. 90k / 2.8m ≈ **3.2%** of BVAL's universe is priced intraday. BVAL itself: 2.7m (Jun 2021) → 2.8m (Oct 2023) ≈ **+1.6% a year**, essentially flat. Growth is in resolution, not breadth. Write two hypotheses for the 100k vs 90k gap and the one document that would settle each.)*

**(c) Who pays when the reference is off: a basket and a future.** (i) A client sells a €200mm EGB list MOC-to-BVAL, and the dealer bids BVAL close − 3c (price points per 100). Cost is €200mm × 0.03/100 = **€60,000**. Now suppose the BVAL close is 2c *rich* to where the bonds actually clear that evening. Who gains, and by how much? *(Answer: the client receives a price 2c too high, so €200mm × 0.02/100 = **€40,000** moves from dealer to client. If BVAL is 2c cheap, the same amount moves the other way. The reference owner, Bloomberg, also runs the MTF. State the governance you'd demand.)* (ii) A credit index future: last index close 1,000.0; the Tradable Tracker shows −0.40% since that close in FAIR<GO>; cost of carry to expiry +0.15%. Estimate iNAV and fair future. *(Answer: iNAV = 1,000 × (1 − 0.004) = **996.0**; fair ≈ 996.0 × 1.0015 ≈ **997.5**. With the tracker's R² of 99.5% vs the parent index, what tracking error would you assume on a stress day, and how would that change a basis trade?)*

---
**Sources (Bloomberg corpus, `_ingest/raw/bloomberg/articles.jsonl`, read 2026-10-25):**
- [BBH + BSKT ETF primary market, 2020-10-28](https://www.bloomberg.com/company/press/brown-brothers-harriman-and-bloomberg-collaborate-to-develop-real-time-etf-primary-market-workflow-solution/)
- [Portfolio Trading Basket Builder incorporating BVAL, 2021-06-09](https://www.bloomberg.com/company/press/bloomberg-launches-portfolio-trading-basket-builder-incorporating-bval/)
- [MIPD credit risk indicator, 2021-07-27](https://www.bloomberg.com/company/press/bloomberg-launches-market-driven-daily-credit-risk-indicator/)
- [BPAM evaluated pricing on the Terminal, 2021-08-02](https://www.bloomberg.com/company/press/bond-pricing-agency-malaysias-evaluated-bond-pricing-data-now-on-bloomberg-terminal/)
- [Bloomberg and CFETS, Southbound Bond Connect, 2021-09-15](https://www.bloomberg.com/company/press/bloomberg-and-cfets-jointly-launch-new-solutions-to-facilitate-trading-on-southbound-bond-connect/)
- [Southbound day one, 2021-09-24](https://www.bloomberg.com/company/press/bloomberg-facilitated-trades-for-seven-hong-kong-market-makers-on-first-trading-day-of-southbound-bond-connect/)
- [Fixed income pre-trade TCA model, 2021-09-22](https://www.bloomberg.com/company/press/bloomberg-introduces-new-fixed-income-pre-trade-tca-model/)
- [Sony Bank BVAL on AWS, 2022-01-20](https://www.bloomberg.com/company/press/sony-bank-to-differentiate-its-business-by-adopting-bloombergs-value-added-data-and-cutting-edge-delivery-technology-for-fully-cloud-based-computing/)
- [Tradable Trackers announced, 2022-06-23](https://www.bloomberg.com/company/press/bloombergs-tradeable-trackers-will-advance-innovation-in-the-fixed-income-markets/)
- [Chartis 2022, 2022-07-12](https://www.bloomberg.com/company/press/bloomberg-ranks-1-in-2022-chartis-risktech-buyside-50-report/) · [Chartis 2023, 2023-07-06](https://www.bloomberg.com/company/press/bloomberg-ranks-1-in-2023-chartis-risktech-buyside-50-report/) · [Chartis RiskTech100, 2023-10-25](https://www.bloomberg.com/company/press/bloomberg-earns-ninth-place-overall-in-chartis-risktech100-ranking/) · [Chartis STORM 2024, 2024-07-02](https://www.bloomberg.com/company/press/bloomberg-storm24-wins/)
- [IBVAL Front Office launch, 2023-10-17](https://www.bloomberg.com/company/press/bloomberg-launches-front-office-pricing-solution-providing-greater-visibility-into-fixed-income-trading/)
- [LQA explainable ML (Risk.net licensed), 2023-11-17](https://www.bloomberg.com/professional/insights/data/leveraging-machine-learning-to-bolster-liquidity-models/)
- [How Bloomberg built IBVAL, 2023-12-04](https://www.bloomberg.com/company/stories/how-bloomberg-uses-machine-learning-intraday-pricing-transparency/)
- [Real-time pricing: accuracy and usability, 2024-02-21](https://www.bloomberg.com/professional/insights/data/real-time-pricing-the-powerful-combination-of-accuracy-and-usability/)
- [IBVAL to Europe, 2024-04-16](https://www.bloomberg.com/company/press/bloomberg-expands-ibval-front-office-pricing-to-europe-backed-by-contextual-metadata-for-greater-transparency/)
- [First EGB MOC spread to BVAL, 2024-04-24](https://www.bloomberg.com/company/press/bloomberg-announces-first-trade-of-egb-market-on-close-spread-to-bval-price/)
- [Pricing foundational to automation, 2024-09-09](https://www.bloomberg.com/professional/insights/data/pricing-insights-why-pricing-is-foundational-to-automation/)
- [US Leveraged Loan Index on BVAL, 2024-10-15](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-accelerates-its-presence-in-loans-market-with-launch-of-a-new-leveraged-loan-index-based-on-new-syndicated-loans-data-and-pricing-solution/)
- [Risk survey, IBVAL ~45k bonds, 2024-12-11](https://www.bloomberg.com/company/press/bloomberg-survey-reveals-geopolitical-risk-is-top-of-mind-for-market-participants/)
- [HKSAR official calculating agent, 2024-12-16](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-named-official-calculating-agent-for-hksar-government-sustainable-bonds-and-infrastructure-bonds/)
- [Tradable Trackers for volatile markets, 2025-04-10](https://www.bloomberg.com/professional/insights/trading/tradable-trackers-realtime-bond-indices-for-volatile-markets/)
- [Portfolio trading podcast (Krein), 2025-07-07](https://www.bloomberg.com/professional/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/)
- [Global leveraged loan indices, 2025-07-22](https://www.bloomberg.com/company/press/bloomberg-broadens-leveraged-loan-indices-and-data-solutions-to-european-and-global-markets/)
- [Southbound toolkit (BVAL on CFETS), 2025-09-23](https://www.bloomberg.com/company/press/bloomberg-tailors-toolkit-to-empower-southbound-bond-connect-participation/)
- [Australian bond pricing, 2025-11-17](https://www.bloomberg.com/company/press/bloomberg-expands-pricing-for-australian-bonds-with-comprehensive-coverage-intraday-access-and-enhanced-curves/)
- [Intelligent automation for front office, 2025-11-26](https://www.bloomberg.com/professional/insights/artificial-intelligence/intelligent-automation-for-front-office/)
- [APAC Regulatory Outlook 2026 (NAFMII), 2026-02-02](https://www.bloomberg.com/professional/insights/regulation/apac-regulatory-outlook-2026/)
- [Tradable products reshaping credit markets, 2026-02-18](https://www.bloomberg.com/professional/insights/trading/how-tradable-products-and-modern-market-infrastructure-are-reshaping-credit-markets/)
- [Kaiko on-chain data, 2026-02-26](https://www.prnewswire.com/news-releases/bloomberg-and-kaiko-collaborate-on-initiative-to-develop-on-chain-data-access-for-tokenized-markets-302698044.html)
- [Spread-to-Benchmark PT baskets, 2026-06-02](https://www.prnewswire.com/news-releases/bloomberg-introduces-spread-to-benchmark-quoting-for-eur-and-gbp-portfolio-trading-baskets-302787922.html)
- [JGB MOC automation, 2026-10-04](https://www.prnewswire.com/news-releases/bloomberg-electronic-markets-brings-automation-to-its-japanese-government-bond-market-on-close-functionality-302897776.html)
- [Beyond the benchmark (BTCA), 2026-10-13](https://www.bloomberg.com/professional/insights/financial-services/beyond-the-benchmark-using-advanced-analytics-to-navigate-fixed-income-trading-costs/)
- Context, not in corpus: [Bloomberg IBVAL back-test, via tradeweb-ai-price](https://www.bloomberg.com/professional/insights/data/pricing-insights-analyzing-quote-data-across-global-credit-markets)
