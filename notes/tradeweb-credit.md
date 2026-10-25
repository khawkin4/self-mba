# Note · Tradeweb in US & European credit — share won by wiring the workflow around the trade, then graded with its own rulers

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — adjacency, platform share), **Course 06** (Operations — workflow bottlenecks, automation), **Course 07** (Data, Analytics & Decision-Making — denominators, self-measured KPIs), **Course 03** (Microeconomics — adverse selection, auctions), **E10** (Digital & AI Transformation), **E8** (Stakeholder & Investor Relations — reading a company's own narrative) · Written 2026-10-24 · Part of [[tradeweb-hub]]; companions [[tradeweb-ai-price]], [[tradeweb-a2a-information-leakage]]

- **Source:** Tradeweb newsroom, **95 items** tagged to credit (news releases, blogs, "Market Insights", reprinted press), **Feb 22 2019 – Aug 5 2026**, at `_ingest/raw/tradeweb/bucket-credit.jsonl`. Dates are the newsroom listing dates; several 2019–2020 blogs carry a re-publication stamp of Jan 4 2021 in their body. PDFs linked in the items were not opened. No item covers a Trumid acquisition; MarketAxess appears only in reprinted third-party press.
- **Core claim:** Tradeweb did not take US credit share by out-competing MarketAxess at the RFQ itself. It won by electronifying the **work around the trade**: Treasury spotting and hedging, voice-trade processing, baskets (portfolio trading), auto-execution rules and a model reference price. Its US high-grade TRACE share went from **11.8% (2019 YTD)** to **22.5% (Q1 2022)**, and its fully electronic HG share from **3.5% (Q3 2018)** to a record **19.7% (Apr 2024)**. Nearly every quality metric it publishes for these tools is measured on Tradeweb's own data, against Tradeweb's own price (Ai-Price), using Tradeweb's own estimate of the market. Since 2026 the story has turned from "show your order to everyone" to "choose your dealers carefully" (SNAP+), and from "our share is rising" to "the TRACE denominator is inflated."

---

## 1. Chronology — the spine

All figures are as Tradeweb states them ("TW says"), unless another source is named.

| Date | Event | Numbers stated |
|---|---|---|
| **Jan 2019** | Launches **electronic portfolio trading (PT)** for US corporates. Calls itself the first platform to do so. | — |
| 2019-02-22 | Blog (Conlin): electronification is under-counted because spotting, voice processing and A2A are invisible in e-share stats. | E-execution "roughly 20%" of US corporate volume. $152bn netted in 2018, giving "$2.8 million" of savings. NOC/LMT spotting example saves $7,881. |
| 2019-06-27 | Tradeweb Direct (retail) streams piped into the institutional RFQ. | $6bn+ actionable per side in 6,000+ CUSIPs. 16,000 live markets ≥$250k a day. Responders up 40–50%. Direct is >18% of anonymous trades under $250k. |
| **2019-10-08** | PT moves to **multi-dealer competition** (in-comp), with buys and sells in one basket. | $21bn PT YTD (to Aug 31). Single trades up to $1bn. 13.8% of HG blocks >$5m. 11.8% of HG TRACE YTD. >$3.0bn daily across 600+ participants. Ai-Price covers 18,000+ bonds. |
| 2019-10-24 | Munis: Tradeweb Direct integrates with Investortools Perform. | 20% of MSRB-reported muni trades. 190+ dealers, 280+ clients. $47bn of munis YTD. |
| 2019-10-28 | Business Insider reprint: banks are racing into PT. MarketAxess PT due "in November". | >$25bn of TW PT by end-Sept. Average PT is $50–100m. |
| **2019-11-21** | **PT for European credit** launches. | PT activity >$29bn (end-Oct). BlackRock estimate: $50bn of market-wide PT in H1 2019. |
| 2020-01-14 | Net Spotting explained (The TRADE). | ~90% of TW HG trades carry a Treasury hedge. "$147 billion" spotted. Firm participation up 70% since 2018. |
| Mar 2020 | COVID: Treasury spotting breaks down. | 30Y UST bid/offer **28x** wider than in February. Spotting a +90 AAPL '45 trade costs $110,816, or **5bp**. |
| 2020-05-18 | Greenwich study of TW **convertibles** RFQ data (2019–Q1 2020). | Average response 69bp wide. Best bid/offer (BBO) **20bp**. **13.6%** of RFQs locked or crossed. |
| 2020-06-26 | Europe: PT vs lists in the sell-off. | Half of European lists leave lines unexecuted. ~95% of portfolios priced in full. 13 US / 10 European PT dealers. |
| 2020-07-23 | "Certainty of execution" becomes the PT pitch. | PT **$43bn in 2019**, >$60bn in H1 2020. Non-comp trades up to $2.3bn. Clients want ≥25% of execution via PT. |
| 2020-07-29 | Cboe IBHY futures EFP on Dealerweb. | TW HY cash credit has "doubled in two years" to **4% of TRACE**. |
| 2020-09-09 | Tradeweb Direct becomes a counterparty to the **NY Fed SMCCF**, with A2A access. | — |
| 2020-12-15 | Curatia reprint on PT growth. | Market PT share of TRACE: 1% (start-2019) → 2% (start-2020) → 3% (pandemic) → 4.5% (Oct 2020). Record $35bn market PT in Oct. Lines per PT up from 89 to 109. |
| **2021-01-27** | **Multi-Client Net Spotting** launches: hedges are netted across all clients spotting at the same moment. | **$818bn** submitted for spotting in 2020. Credit ADV $22.1bn. Dec 2020: **19.3% HG / 6.9% HY** TRACE. Savings of $27.35m since 2019. 40.3% of eligible volume netted. |
| 2021-04-08 | First PT data blog (Husveth). | US PT **$123bn in 2020** ("nearly tripling"). $57bn in Q1 2021. Average PT $90.2m, 189 lines, 78/18/4 IG/HY/EM. Hit rate 92.3% (2020), 96.3% (Q1 2021). |
| 2021-06-10 | AllTrade (TW's all-to-all network) white paper. | A2A ~30% of RFQ e-volume. AllTrade = 43% (HY) / 25% (IG) of in-comp RFQ volume. AiEX = 28.8% IG / 32% HY. 700+ firms. Rematch (unmatched dealer session risk) offered into A2A. |
| 2021-10-14 | PT **Trade at Close**. | $416.9bn PT since launch, $227.5bn of it in 2021 to Sept. Sept 2021: **21.0% IG / 9.5% HY** TRACE. Ai-Price ~25,000 bonds. |
| 2021-11-23 | PT execution quality, measured vs **Ai-Price**. | Average %BOS captured 43% (35% volume-weighted). 44% of lines better than Ai-Price mid. 95% hit rate. |
| 2021-11-30 | "Building a Better Credit RFQ". | AllTrade ranks as the "**#4 dealer**" with $1,573/mm price improvement. AiEX ≈ **54% of IG** / 38% of HY RFQ tickets. Single day >30% of IG TRACE (June). IG volume +65%, HY +160% vs 2020. |
| 2022-04-06 | **Ai-Price for munis**. | ~880,000 bonds, end-of-day. TW handles 1 in 6 MSRB trades. |
| **2022-05-17** | PT capacity >2,000 lines. Spread-at-close. | PT ADV **$1.4bn** in Q1 2022, up "more than 725%" since launch. ~30% of PTs trade at close. Credit ADV $33.2bn. **22.5% HG / 10.9% HY** TRACE in Q1 2022. |
| 2022-06-23 | Spotlight Dealer Diversity Program. Diverse dealers can intermediate A2A fills. | 14 named dealers at launch. |
| 2022-11-09 | Europe: automation. | **58%** of European in-comp credit trades via AiEX in H1 2022. SNAP IOI dealers fill "at mid or better" on average. |
| **2022-12-06** | **BlackRock Aladdin** multi-year partnership (phase 1: Ai-Price inside Aladdin). | 1,100+ credit clients. Credit ADV >$29.7bn (first three quarters of 2022). |
| 2023-01-30 | PT review of 2022. | US PT **>$270bn** (+19%), users +30%. Average line $690k → $590k. In-comp share 77%. Hit rate 91% (vs 94%). |
| **2023-05-15** | **FINRA PT flag on TRACE** takes effect. | TW says this validates its earlier TRACE-scraping estimate. |
| 2023-06-14 | SVB / Credit Suisse stress test. | AiEX share of RFQ volume dipped 27% → 20.5% (vs ~**0.3%** in Mar 2020). E-trading back to normal within a week. |
| 2023-12-11 | Aladdin phase 2 (AllTrade inside Aladdin). | AllTrade 32% HG / 44% HY of in-comp RFQ. Record **$137bn** AllTrade in Q3 2023 (+50%). Fully electronic share: **16.6% HG** (vs 3.5% Q3 2018), **7.8% HY** (vs 1.2%). |
| 2024-04-10 | SNAP IOI for European RFQs, sourcing from Sweep sessions. | ~€20bn across 7,000+ ISINs. "Wins about 30% of time with 20+% better TCA." |
| 2024-05-02 | PT cost drivers. | %BOS ~30% (2022) → 40–45%. Drivers: line size, liquidity, overlap with LQD/HYG, and the **ETF premium/discount**. |
| **2024-05-21** | "Inflection point in IG." | Record **19.7%** fully electronic HG TRACE (Apr 2024). Fully electronic HG ADV +62% to $6.7bn (Q1). Greenwich: IG e-share 25% (2019) → ~45%. HY "stuck at about 30%". |
| 2024-06-13 | **RFQ Edge**: PT analytics added to the RFQ list ticket. | Ai-Price ~30,000 bonds. May 2024: 17.6% HG / 7.5% HY fully electronic. |
| 2024-10-16 | 10th anniversary of the US corporate bond marketplace. | Greenwich (Sept 2024): **IG 50% / HY 32%** electronic. |
| 2024-11-14 | Convertibles (Greenwich reprint). | TW converts spreads ~80bp (2022) → <40bp (H1 2024). Dealers 12 → 22. Trades >$5m +45% YoY. |
| 2024-11-21 | Five years of European PT. | Jan–Sep volume +56%. Mixed IG/HY +280%, HY +123%. Dealers 15 (2021) → 20. |
| **2025-01-23** | PT review of 2024. | Market PT **11.4% of TRACE in Dec 2024** (17.5% of dealer-to-client). ~9% for the year (Bloomberg reprint). Market PT **>$1tn**. TW PT clients +21%. |
| 2025-04-08 | PT extended to European government bonds. | 2024 global TW PT **$698bn across 9,134 trades**. |
| **2025-05-07** | Tariff shock ("Liberation Day") stress test. | PT 11.3% of April TRACE. HY PT a record **20% of TRACE** (Apr 10, 15). IG spreads ~15bp wider (per Ai-Price). Net Spotting saves ~$355/mm (+119% vs March; Mar 2020 was +2,800%). Anonymous A2A wins beat the next-best disclosed quote by $2,751/mm (IG) and $8,046/mm (HY). |
| 2025-08-05 | H1 2025 review. | US + EU PT +30% YoY. Euro RFQ +18%, Euro PT +10%. Credit ETF notional $91bn. |
| **2026-03-31** | "Blast all → **select smart**": SNAP+ (AI dealer selection). | A2A volume up "almost 300%" 2020–2025. IG >$1m: A2A is **+0.2bp better** on execution but has **0.17bp more** market impact than voice. |
| 2026-05-13 | Information-leakage white paper (see [[tradeweb-a2a-information-leakage]]). | — |
| 2026-06-23 | **Spread trading for European credit PT**. | Q1 2026 global PT **$258.4bn**, +40% QoQ. |
| **2026-06-30** | "What TRACE is showing beneath the surface": the denominator argument. | Affiliate back-to-back prints rose from ~3% (Q1 2024) to **>9%** of IG TRACE (Q1 2026), about $125bn in Mar 2026. TW says this understates its fully electronic share by ~1pp → **~2pp**. SR-FINRA-2026-009 is pending. IG ADV ~$40bn (2025), ~$50bn (Q1 2026). |
| 2026-07-17 | SNAP+ extended to EM portfolio trading. | Self-classified "minimal-risk" under the EU AI Act. |

## 2. The five machines, and their best numbers

| Machine | What it does | Headline metric (TW-stated) | Who measures |
|---|---|---|---|
| **Net Spotting** (2019→MCNS 2021) | Nets the Treasury hedges on IG spread trades across dealers, then across clients, at one composite price | $818bn submitted (2020). $27.35m saved since 2019. ~40–50% of eligible / spread-based volume | TW, against a "pay full bid/ask on every leg" baseline |
| **Portfolio trading** | Prices a whole basket all-or-none, with one counterparty | US PT $43bn (2019) → $123bn (2020) → >$270bn (2022). Global $698bn (2024), $258.4bn in Q1 2026 alone | TW volumes. Market share was a TW TRACE estimate until the May 2023 flag |
| **AiEX** | Rules-based auto-execution inside the RFQ | ~54% of IG RFQ tickets (Nov 2021). 58% of European in-comp (H1 2022) | TW. Denominators shift (tickets vs volume vs trades) |
| **AllTrade (A2A)** + Direct + Rematch | Pools institutional, retail and dealer-session liquidity anonymously | 32% HG / 44% HY of in-comp RFQ (2023). "#4 dealer". Volume +~300% 2020–25 | TW |
| **Ai-Price** | Model bid/offer used as the reference for TCA, PT, AiEX limits and iNAV | 18k → 30k bonds. Munis 880k | TW. See [[tradeweb-ai-price]] |

**Market-wide context Tradeweb cites (Coalition Greenwich):** US corporates ~20% electronic (early 2019). IG 30% (Jul 2019). IG 40% / HY 30% vs 8% / 2% in 2013 (Dec 2023). IG ~45% (May 2024). IG 50% / HY 32% (Sept 2024). "Roughly half" still traded by phone (Mar 2026).

## 3. How the narrative moved

1. **2019 – early 2020: "the tape undercounts us."** E-share figures miss the workflow: voice-processed trades, spotting, and pre-trade data routed into the OMS. PT is pitched as plumbing for the bond-ETF create/redeem cycle. The positioning is **evolutionary, not disruptive**. Conlin says so explicitly in 2024: startups that "preached disruption" found credit "not like the others."
2. **2020–2021: COVID as proof.** The vocabulary shifts from cost to **certainty of execution**. PT volume roughly triples. Net Spotting's value peaks when Treasury bid/offers blow out. "Automation didn't switch off this time" (Oct 2021).
3. **2022–2023: resilience and distribution.** The story is that e-trading is "sticky" through rate shock, SVB and Credit Suisse. Tradeweb distributes through Aladdin. Share figures shift toward **fully electronic** share, quoted as multiples of a 2018 base ("5-fold", "nearly 7-fold"). The last total-HG share in this bucket is Q1 2022 (22.5%).
4. **2024–2025: analytics in the ticket.** PT reaches records (11.4% of TRACE, >$1tn). Pre-trade cost models and RFQ Edge appear. The tariff shock is presented as a second stress test passed.
5. **2026: reversal on breadth, fight over the denominator.** The 2021 line was that A2A is a top-4 dealer. The 2026 line is that A2A **leaks**, so clients should "select smart" with AI-picked dealers. Meanwhile, flat-looking IG share is explained as duplicate affiliate prints inflating TRACE.

## 4. What the claims don't prove

1. **Tradeweb is the referee of its own game.** PT %BOS, "better than mid", A2A leakage and spotting savings are all scored against **Ai-Price** or Tradeweb composites. There is no third-party price, no competitor and no independent TCA vendor in any of these comparisons.
2. **The baselines flatter the product.** Net Spotting "savings" assume the client otherwise pays the **full** Treasury bid/ask on every leg. That is the maximum-cost case; the Jan 2021 paper says "maximum possible trade cost." "Better than mid vs Ai-Price" depends on how wide the model's own bid/offer is.
3. **The market-size numbers were Tradeweb's model.** Before the May 2023 TRACE flag, PT's share of TRACE came from Tradeweb clustering same-time prints, then adding back its own trades. A 2020 reprint also notes the tape capped sizes and MarketAxess did not report PT. The trend is credible; the levels were estimates.
4. **The figures don't reconcile across releases.**
   - Net Spotting 2020: **$818bn** "submitted for spotting" (Jan 2021) vs **$326bn** "credit trades submitted for Net Spotting" (Oct 2021).
   - Trade at Close to Sept 2021: **$1.4bn** (Oct 2021 release) vs **USD13.9bn** (Sept 2022 Asia article).
   - AllTrade launch: "early 2018" (2021) vs "launch in 2017" (2023).
   - Net Spotting "launched in early 2019", yet $152bn was netted "in 2018".
   - The Oct 2021 piece says automation stayed on in 2020; the June 2023 piece says AiEX fell to ~0.3% of RFQ volume in March 2020.
   - US PT 2019 is $43bn in one place; global vs US totals are mixed elsewhere.
5. **The metrics change.** AiEX is quoted as % of trades, % of tickets, % of in-comp volume and % of RFQ volume. Share is quoted as total HG TRACE, then fully electronic HG TRACE, then fully electronic adjusted for duplicates. Each switch may be legitimate, but together they make trend lines hard to rebuild.
6. **Survivorship in the stress stories.** Stress-test posts (Mar 2020, Mar 2023, Apr 2025) are written after the platform performed well. The 2022 drawdown gets a "challenging year" mention, but no comparable "what broke" piece exists. PT's in-comp share fell from March 2022 as clients hid baskets from dealers; that detail appears once.
7. **The denominator argument is self-serving and timed.** It was published when IG share looked flat. Its scale (>9% of IG *volume*) is Tradeweb's; FINRA's own figure (5.7% of corporate *transactions*, broader product set) is a different measure. The rule (SR-FINRA-2026-009) is not final.
8. **Competitors are absent.** No MarketAxess share comparison, nothing on Open Trading, no Trumid, no Bloomberg. "First platform" claims (PT 2019, spotting) are unverified within the file.

## 5. Strategic read (inference — not stated by Tradeweb)

- **The moat is the rates adjacency.** IG trades on spread to a Treasury. Tradeweb runs a 20+ dealer Treasury composite and a big UST marketplace, so it can **close the hedge inside the same system**. Spotting → Net Spotting → MCNS → Bulk Crossing → spread trading for European PT is one capability reused for a decade. That explains why TW's share is strong in IG and weaker in HY. Tradeweb half-admits this in May 2024: HY "trade[s] on price", so the hedging innovations don't apply.
- **Aggregating its own silos.** Institutional RFQ + Tradeweb Direct retail streams + Dealerweb sweep leftovers (Rematch, SNAP IOI) form a liquidity pool a single-segment venue cannot copy cheaply. This is multi-sided platform logic with the sides inside one firm.
- **PT rides the ETF arbitrage.** TW's own regression says PT cost depends on ETF overlap and the **ETF premium/discount**. PT growth is therefore partly a bet on bond-ETF growth and on a few ETF-making dealers. Concentration risk sits on the dealer side.
- **Ai-Price is the hidden keystone.** It is the ruler for TCA, PT pricing, AiEX tolerances, iNAVs and research claims. Once clients set auto-ex limits and TCA history against it, switching venues means re-baselining everything (see [[tradeweb-ai-price]] §7).
- **"Select smart" is dealer-friendly positioning.** Tradeweb's 2021 marketing praised A2A breadth. Its 2026 marketing praises curated dealer lists. That suits a venue whose franchise is dealer relationships and whose rival (context, not from Tradeweb: MarketAxess, now being bought by ICE per [[tradeweb-ai-price]] §4) built its brand on A2A. Its own blog shows A2A still nets about **+0.03bp** (0.2 − 0.17) better than voice on IG >$1m. The "leakage" headline is smaller than the framing suggests.
- **Where the next share comes from:** larger HY tickets (HY PT size +43% in Apr 2025, HY RFQ clips +15% in Q1 2025), Europe (spread trading for PT, SNAP IOI), EM/CNH, and private credit infrastructure (the Quorim tie-up, Aug 2026, is plumbing, not trading).

## 6. Canon lenses

- **Sustaining vs disruptive** ([[canon-christensen-innovators-dilemma]]): Tradeweb's credit playbook is textbook *sustaining* innovation sold to incumbent dealers and big buy-sides. It worked where the "disruptor" fintechs, by TW's telling, failed. The test is whether an A2A-native or AI-native entrant is the real disruptor that dealer-friendly incumbents can't follow.
- **Find the bottleneck** ([[canon-goldratt-the-goal]]): the binding constraint in IG execution was the Treasury spot and its phone delay ("up to a fifteen-minute time lag"), not the RFQ. Fix the constraint and throughput (e-share) follows.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): AllTrade adds sides (retail, wholesale sessions, diverse dealers as intermediaries) without changing anyone's workflow. "Doesn't alter the screen" is a deliberate choice that lowers participation costs.
- **Lemons** ([[canon-akerlof-market-for-lemons]]): early PT critics said sellers "tuck[ed] unattractive bonds" into baskets. That is adverse selection, and dealers answer it by pricing the whole basket wider. TW's remedy is information: pre-trade analytics, liquidity scores and ETF overlap.
- **Lock-in through information goods** ([[canon-shapiro-varian-information-rules]]): reference prices and TCA history create switching costs. The Aladdin integration puts Ai-Price on the buy-side's main screen.
- **Power** ([[canon-helmer-7-powers]]): scale economies in netting (MCNS savings rise with pool size: "increases along with the size of the Tradeweb liquidity pools") plus switching costs. Netting is one of the few places where network effects in OTC trading are mechanical, not just asserted.
- **Measurement and noise** ([[canon-kahneman-sibony-sunstein-noise]], [[canon-tetlock-superforecasting]]): when the vendor sets the ruler, the denominator and the baseline, treat each KPI as a forecast to be scored externally, not a fact.

## 7. Practitioner counterpoint

- **For Tradeweb:** the gains are real and visible outside its own releases. Greenwich e-share data, the FINRA PT flag and Bloomberg's ">$1tn" PT story all point the same way. Buy-side quotes in the file, from Invesco ("hundreds of CUSIPs in an hour"), AllianceBernstein, Agilon, L&G and Royal London, describe workflow savings that are hard to fake. Net Spotting is a mechanically sound idea: netting offsetting hedges *must* save bid/ask.
- **Against:** much of the "electronic" volume is voice-agreed and then processed on the platform. Portfolio trading concentrates risk transfer in a handful of ETF-linked market makers. And the client experience in stress (PT in-comp share fell in 2022, RFQ responses thinned in April 2025) shows that "certainty of execution" is bought with **price**, not given free.
- **Both:** a desk choosing between protocols should run its **own** TCA on a third-party mid (CBBT, CP+, next TRACE print), split by side and liquidity. It should treat Tradeweb's numbers as hypotheses to test, as [[tradeweb-a2a-information-leakage]] §7 argues.

## 8. Open questions to track

1. **Total HG TRACE share after Q1 2022.** Does it continue above 22.5%, and how does it compare on a duplicate-adjusted basis? Track the monthly reports.
2. **SR-FINRA-2026-009.** Is it approved? If so, does Tradeweb's reported fully electronic IG share jump by ~2pp mechanically?
3. **HY.** Does HY e-share break out of ~30–32%? Do TW's HY PT (20% TRACE days) and larger HY RFQ clips become a trend?
4. **SNAP+ evidence.** Will Tradeweb publish SNAP+ vs A2A vs voice on a non-TW price, netting improvement against impact?
5. **PT dependence on ETFs.** What happens to PT cost and hit rates in a bond-ETF outflow or a large discount episode?
6. **Reconciliation.** Will the Net Spotting volume ($818bn vs $326bn) and Trade-at-Close figures be cleared up in a 10-K or investor deck?
7. **Europe.** Does spread trading for European PT pull European share the way spotting pulled US IG?
8. **Competitive response.** How does ICE-owned MarketAxess (context, not from Tradeweb) answer on spotting, PT analytics and dealer selection?

**Links:** [[tradeweb-hub]] · [[tradeweb-ai-price]] (the ruler behind §4.1) · [[tradeweb-a2a-information-leakage]] (the 2026 leakage study and SNAP+) · [[market-structure-24-5-trading]] (OTC/RFQ market structure) · [[trading-floor-mechanics]] · [[wss-credit-distressed]] · [[wss-trading-hedge-funds]] · [[wss-rates-macro]] (the Treasury leg that makes spotting matter) · [[bloomberg-terminal-instrumentation]] · [[canon-christensen-innovators-dilemma]] · [[canon-goldratt-the-goal]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-akerlof-market-for-lemons]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]]

---
### Rep
Three short computations with numbers from this note.

**(a) Net Spotting, by hand.** A client buys $50mm NOC '47 (dealer hedge: buy $37.9mm old 30Y) and sells $30mm LMT '46 (dealer hedge: sell $25.2mm). The UST is quoted 100-02+/100-03+, so the bid/ask is 1/32. Without netting, the client pays the full bid/ask on the offsetting $25.2mm. What does netting save? *(Answer: $25.2mm × (1/32)/100 = **$7,875**. Tradeweb says "almost $7,900". In March 2020 the 30Y bid/offer was ~$1.44 wide, about 46/32. Recompute, and explain why the product's value is highest exactly when markets are worst.)*

**(b) A2A vs voice, netted.** Use the Mar 2026 blog: A2A is +0.2bp better on execution and costs 0.17bp more in market impact (IG >$1m). For a $10mm trade with spread duration 7, compute each leg in dollars and the net. *(Answer: $1,400 − $1,190 = **+$210** in favour of A2A.)* Then decide: at what size premium on impact (say impact doubles for $25mm+ blocks) does SNAP+ or voice win? What third-party price would you use to check?

**(c) The denominator.** Tradeweb reported a record 19.7% fully electronic HG share in Apr 2024 and says duplicate affiliate prints were ~3% of IG TRACE then and >9% by Q1 2026. Compute the duplicate-adjusted share for each: s / (1 − d). *(Answer: 19.7/0.97 ≈ **20.3%**, +0.6pp; 19.7/0.91 ≈ **21.6%**, +1.9pp.)* Compare with Tradeweb's "~1pp → ~2pp". In one paragraph, say whether a pure denominator effect can explain flat reported share, and what data would falsify Tradeweb's claim.

---
**Sources (Tradeweb newsroom, accessed via bucket file 2026-10-24):**
- [Electronification blog, 2019-02-22](https://www.tradeweb.com/newsroom/media-center/insights/blog/electronification-and-the-technology-revolution-in-corporate-bond-trading/)
- [Retail streams into institutional, 2019-06-27](https://www.tradeweb.com/newsroom/media-center/in-the-news/fixed-income-outlook-expanded-access-to-liquidity-and-opportunities-amidst-trade-tension/)
- [PT expansion, 2019-10-08](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-expands-portfolio-trading-for-corporate-bonds/)
- [European credit PT, 2019-11-21](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-launches-portfolio-trading-for-european-credit-bonds/)
- [Convertibles RFQ study, 2020-05-18](https://www.tradeweb.com/newsroom/media-center/in-the-news/crossed-locked-and-loaded-trading-convertible-bonds/)
- [March Madness / spotting, 2020-08-13](https://www.tradeweb.com/newsroom/media-center/insights/blog/march-madness-in-corporate-bonds/)
- [SMCCF counterparty, 2020-09-09](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-direct-added-as-counterparty-to-new-york-feds-secondary-market-corporate-credit-facility/)
- [Net Spotting white paper, 2021-01-04](https://www.tradeweb.com/newsroom/media-center/insights/commentary/net-spotting-reducing-trading-costs-for-u.s.-corporate-bonds)
- [Multi-Client Net Spotting, 2021-01-27](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-introduces-next-generation-spotting-for-u.s.-credit-trading)
- [Initial impact of PT, 2021-04-08](https://www.tradeweb.com/newsroom/media-center/insights/blog/the-introduction-and-initial-impact-of-portfolio-trading/)
- [Sizing the PT market, 2021-05-18](https://www.tradeweb.com/newsroom/media-center/insights/blog/deciphering-the-size-of-the-portfolio-trading-market/)
- [AllTrade, 2021-06-10](https://www.tradeweb.com/newsroom/media-center/insights/commentary/connecting-the-dots-of-innovation--a-breakthrough-in-all-to-all-trading/)
- [Five credit trends, 2021-10-04](https://www.tradeweb.com/newsroom/media-center/insights/commentary/well-that-was-crazy.-now-what)
- [Trade at Close, 2021-10-14](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-enhances-portfolio-trading-introduces-trade-at-close-functionality/)
- [PT execution quality, 2021-11-23](https://www.tradeweb.com/newsroom/media-center/insights/blog/measuring-execution-quality-for-portfolio-trading/)
- [Better credit RFQ, 2021-11-30](https://www.tradeweb.com/newsroom/media-center/insights/blog/building-a-better-credit-rfq/)
- [PT enhancements, 2022-05-17](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-introduces-enhanced-functionality-for-portfolio-trading/)
- [BlackRock Aladdin, 2022-12-06](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-announces-partnership-with-blackrock-to-further-electronify-corporate-bond-market/)
- [PT 2022 review, 2023-01-30](https://www.tradeweb.com/newsroom/media-center/insights/blog/portfolio-trading-trends-a-breakdown-of-2022/)
- [SVB/CS stickiness, 2023-06-14](https://www.tradeweb.com/newsroom/media-center/insights/blog/electronic-credit-trading-defies-volatility-stay-surprisingly-sticky/)
- [Aladdin phase 2, 2023-12-11](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-enters-next-phase-of-partnership-with-blackrock/)
- [PT cost drivers, 2024-05-02](https://www.tradeweb.com/newsroom/media-center/insights/blog/analyzing-execution-quality-in-portfolio-trading/)
- [IG inflection, 2024-05-21](https://www.tradeweb.com/newsroom/media-center/insights/commentary/electronic-credit-trading-approaching-inflection-point-in-ig/)
- [RFQ Edge, 2024-06-13](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-launches-enhanced-rfq-functionality-for-credit-markets/)
- [PT in 2024, 2025-01-23](https://www.tradeweb.com/newsroom/media-center/insights/blog/portfolio-trading-in-2024-advancing-transparency-and-efficiency-in-credit-markets/)
- [Tariff tumult, 2025-05-07](https://www.tradeweb.com/newsroom/media-center/insights/blog/credit-markets-put-to-the-test-in-tariff-tumult/)
- [Blast all → select smart, 2026-03-31](https://www.tradeweb.com/newsroom/media-center/insights/blog/from-blast-all-to-select-smart-how-dealer-selection-is-evolving/)
- [Info leakage, 2026-05-13](https://www.tradeweb.com/newsroom/media-center/insights/blog/information-leakage-in-us-credit-evidence-from-all-to-all-rfqs/)
- [Euro PT spread trading, 2026-06-23](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-launches-spread-trading-for-european-credit-portfolios/)
- [TRACE beneath the surface, 2026-06-30](https://www.tradeweb.com/newsroom/media-center/insights/blog/understanding-ig-market-share-data-what-trace-is-showing-beneath-the-surface/)
