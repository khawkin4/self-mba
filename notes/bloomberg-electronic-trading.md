# Note · Bloomberg electronic trading — venues sold as workflow, one ‘first trade’ at a time, with no market share ever disclosed

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — bundling, counter-positioning, coopetition with dealers), **Course 06** (Operations — automation, straight-through processing, done-away clearing), **Course 07** (Data, Analytics & Decision-Making — boilerplate KPIs, self-run studies, missing denominators), **Course 11** (Global Strategy, Macro & Responsible Business — China, India, Gulf, Australia market openings), **E9** (Geopolitics & Macro for Decision-Makers), **E10** (Digital & AI Transformation — rules-based and API execution) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-pricing-bval-ibval]], [[bloomberg-buyside-stack]], [[bloomberg-indices]], [[bloomberg-consolidated-tape]], [[bloomberg-terminal-instrumentation]]

- **Source:** Bloomberg corpus `_ingest/raw/bloomberg/articles.jsonl`, about **45 items** used, **Jul 2 2019 – Oct 8 2026**. They include about 35 press releases (bloomberg.com archive copies to 2025, PR Newswire for 2026) and about 10 Insights pieces (the SOFR venue-data article, the ETOMS sell-side piece, the RFQe/Sun Life case study, the portfolio-trading podcast, and the Treasury clearing article). Reader notes P1–P3, P5 and DELTA were used to find items. The Hult quote comes from `_ingest/raw/tradeweb/articles-2019-2026.jsonl`. Caveats: the Wayback archive is thin for 2024 and 2026, so a missing follow-up release may be an archive gap, not a corporate silence. Bloomberg is private and publishes **no venue revenue, ADV or market share**.
- **Core claim:** Bloomberg runs regulated venues on three continents: BSEF (US SEF), BMTF (UK MTF), BTFE (Netherlands MTF) and the Tradebook entities in Singapore and Hong Kong. Its trading brands are FIT, FXGO, RFQe, BOLT, BSKT, TSOX and ETOMS/TOMS, grouped as *Electronic Trading Solutions*, renamed **Bloomberg Electronic Markets** between Jul and Sep 2025. Yet it never markets them as venues competing for share. Every release is a **protocol in a market**, usually with a named **first trade**: €STR swap (2019), SOFR/EFFR compression (2020), EGB market-on-close to BVAL (2024), Qatar auction (2024), Australian EFP and ETFs, ABS BWIC and Indian govvies (2026), fully automated JGB MOC (Oct 2026). The only hard venue figures in eight years are **73% of USD swaps on Bloomberg being SOFR** and venue volume **up ~31% YoY** (Jan 2022), plus **+58%** FX options growth on FXGO (Sep 2026). Even the dealer count in the boilerplate swings between **1,500** and **800**. Read it as a strategy: the venue is a feature of the Terminal and the pricing stack, so share is never the scoreboard.

---

## 1. Chronology — the spine

All figures as Bloomberg states them, unless another source is named.

| Date | Event (venue / protocol) | Numbers stated |
|---|---|---|
| 2019-07-02 | Bond Connect: block allocation, ABS on Bloomberg's access channel | Foreign holdings of onshore bonds 1.88tn yuan (May 2019) |
| 2019-09-25 | Bond Connect: Terminal shows **all** CFETS dealer prices. CIBM Direct allocation goes straight to the agent bank, with no VCON re-keying | Before: "Previously, global investors had access to only five of the most competitive prices for a given bond that trades on Bond Connect." |
| **2019-10-08** | **First electronic €STR swap** on BMTF (LBBW vs J.P. Morgan, 5y RFQ). BTFE live too; BSEF from Oct 21 | Tenors out to 70y. LCH clearing Oct 21, Eurex Nov 18. Platforms used by "more than 1,000" institutions |
| 2020-06-24 | FXGO approved as an electronic trading platform in Malaysia (BNM) | — |
| 2020-10-28 | CIBM-Direct RFQ: first trades by CCB Singapore (event write-up) | China bond market "$16 trillion" |
| **2020-10-28** | **BBH + BSKT**: ETF primary-market workflow | "the first real-time solution" for AP order-taking |
| **2020-11-12** | **First electronic SOFR vs EFFR compression** on BSEF, via BOLT, cleared at CME | SOFR tradable on Bloomberg since 2018 |
| 2020-11-23 | FXGO pre-trade supplementary cost tool (Pictet AM) | FXGO: **5,000+ firms, 140 countries, 800+ LPs**. FX market >$6tn a day |
| 2021-02-05 | Danone FXGO case study | 800+ LPs, **2,500** trading desks. Saves 50 hours a year |
| **2021-06-09** | **Portfolio Trading Basket Builder (PTBB)** with BVAL/CBBT references | Up to **six** dealers in competition. BVAL >2.7m securities. Builds on Dec 2020 ‘RFQ to Many’ |
| 2021-06-28 | Rule Builder for ETFs via RFQe (Indosuez, first bank) | — |
| 2021-09-24 | **Southbound Bond Connect** day 1 via TOMS ↔ CFETS. BVAL shown on CFETS | 7 HK market makers, 40+ onshore investors. By Oct 25: "Eight out of the 13 designated dealers have been using Bloomberg Southbound Bond Connect" |
| 2021-12-01 | COMSTAR (CFETS subsidiary) API link to FXGO | — |
| **2022-02-09** | Bloomberg's own venue data on the SOFR transition | Venue volume **+~31%** YoY (Jan). **73%** of USD swaps on Bloomberg are SOFR. **30** SOFR dealers. CBBT SOFR bid-offer below LIBOR from Oct 2021 |
| **2022-03-15** | **Bloomberg Bridge**: all-to-all RFQ for corporate and EM bonds, "supported by dedicated Goldman Sachs intermediation desks" | Network "over 3,700" firms. Greenwich: US A2A ~5% (2017) → 12% (2020). Europe Q2 2022, then US/APAC. **No later release in the corpus** |
| 2022-06-08 | Rule Builder at Baader Bank (equities) | — |
| 2023-03-07 | Central Bank of Azerbaijan: FXGO, BMatch CLOB, deposit RFQ, surveillance | — |
| **2023-03-13 → 10-03** | **Broadway Technology** acquired. CMA clears Sep 6. Merged with ETOMS | Broadway serves "more than half of the top 50 banks in the world" |
| 2023-04-20 | ETOMS sell-side piece (Simek, Tsou) | "ETOMS is integrated with over 40 global trading venues" |
| **2023-05-15** | **Northbound Swap Connect** day 1 via BBTI → CFETS | 20+ offshore investors traded. 20 onshore dealers designated |
| **2023-05-24** | Rule Builder: Timed Release, Order Rerun, economic-data triggers | Rates automation "more than doubled since 2021". Round-lot (>$5m) activity up nearly **5x** |
| 2023-06-20 | **D&I Dealer** initiative extended to US Treasuries (CastleOak, Mischler, Tigress; program dates from 2017) | Firms with over 10 trillion in AUM signed up, per Mischler. ETS: 175 markets, 9,000 firms, **1,500** dealers |
| **2024-03-13** | Rule Builder study on BTCA data | 23m orders (2022–23). RBLD orders beat manual by **38%** (US) / **68%** (EU). Desks +30% / +36% |
| **2024-04-24** | **First EGB MOC list trade referencing BVAL** (J.P. Morgan with a European insurer) | All-or-none via PTBB |
| 2024-11-30 | RFQe + AIM case study (Sun Life AM HK, ~HK$130bn) | The benefits section is unfilled template text: "Lorem ipsum dolor sit amet" |
| **2024-12-26 / 2025-01-19** | **Qatar Central Bank** primary-dealer auctions on the **Bloomberg Auction System** plus AIM | First auction Dec 26 2024. Later phases: cross-border access, secondary liquidity |
| 2025-02-10 → 09-29 | Offshore RMB repo via BOLT REPO ↔ CFETS. Extended to onshore repo in Sep | 17+ banks named on day 1 (Sep 29) |
| 2025-07-07 | PT podcast (Krein, Kazi, Wells Fargo) | Krein: PT ≈ "about 25% of U.S. investment grade activity" (Mar 2025) |
| 2025-10-16 | ICBC Luxembourg: first Swap Connect trade in Europe (after ICBC Dubai) | Boilerplate now says **800** dealers |
| 2026-02-09 | BSKT for ETF Shares (Australia) | — |
| **2026-05-20** | **Australian EFP** contingent bond-vs-future package (HESTA, ANZ) | — |
| 2026-06-02 | PTBB spread-to-benchmark quoting for EUR/GBP | — |
| **2026-06-15** | **ABS BWIC/OWIC** list workflow with response windows. First trade done | US and EMEA rollout |
| **2026-07-09** | **First electronic Indian govvie (IGB) trade** for FPIs via NDS-OM (State Street IM) | Follows India FAR inclusion in the EM local-currency index |
| 2026-07-30 | RFQe for Australian-listed ETFs, options and futures, after an ASIC amendment. First trade done | — |
| **2026-09-14** | **FX Options RFQ API** on FXGO | FX options volume **+58%** YoY since Aug 2025; hedge funds **+75%**. 30+ algo providers |
| **2026-10-04** | **First fully automated JGB MOC** to BB3P (BlackRock collaborated) | MOC now in USTs, Canadas, Gilts, EGBs, JGBs |
| **2026-10-08** | Treasury clearing article (Kleinbauer, Benham) | Cash Dec 31 2026, repo Jun 30 2027. CCAs: FICC, CMESC, ICE Clear Credit |

## 2. The machines, and what Bloomberg says about each

| Machine | What it does | Best Bloomberg number | What is missing |
|---|---|---|---|
| **BSEF / BMTF / BTFE** (rates, CDS, FX derivs) | Regulated D2C swaps RFQ, list trading (BOLT), compression | 73% SOFR share *on Bloomberg*. Volume +31% YoY. 30 dealers (Jan 2022) | Any share of industry SEF volume. Any ADV |
| **FIT / TSOX / PTBB / MOC** (cash bonds) | RFQ, lists, PT baskets, close-referenced trades priced to BVAL or BB3P | Six-dealer PT. MOC in five sovereign markets | PT or MOC volumes. Hit rates |
| **Bridge / D&I dealers** | Intermediated all-to-all (Goldman). Diverse dealers in front of traditional liquidity | 3,700 firms in the network. 10tn+ AUM signed up (per Mischler) | Bridge go-live. Any A2A volume |
| **FXGO** | Multi-bank FX RFQ, streams, algos, chat dealing, central-bank solutions | 5,000+ firms, 800+ LPs (2020). FX options +58% (2026) | Any ADV (FX is the one asset class where peers publish ADV monthly) |
| **RFQe / BSKT** | ETF secondary-market RFQ. ETF create/redeem workflow | — | Any number at all |
| **Rule Builder** | No-code rules routing low-touch orders to Bloomberg venues | Rates automation 2x since 2021. 38% / 68% outperformance | Share of flow automated. Selection controls |
| **ETOMS / TOMS + Broadway** | Sell-side OEMS, connectivity to 40+ venues, low-latency rates market-making | 16,300 sell-side users (2021) | Revenue. Client count after the merger |
| **Gateways** (CFETS, NDS-OM, QCB, ASIC) | Plug the Terminal into someone else's market infrastructure | Day-1 counts (7, 8/13, 20+, 17+ banks) | Volume through any gateway |

## 3. How the narrative moved

1. **2019–2022: the rate transition as proof.** The same Nicholas Bean sentence is reused twice: "Being the first to market with €STR swap electronic trading functionality is a clear demonstration of Bloomberg’s commitment" (2019), then "Being the first to market with our SOFR compression trading offering is a clear demonstration of Bloomberg’s commitment" (2020). The venue's job is to make a regulator-driven migration painless.
2. **2021–2023: workflow tools and buying in.** PTBB, Rule Builder, Bridge, then Broadway, which "will fill a gap in our product portfolio". This is the only admission of weakness in the theme, and it concerns the **sell-side** low-latency stack, not the buy-side venue.
3. **2019–2025: China as the gateway business.** Every China release is a joint release with CFETS, with day-1 counts and no volumes. Bloomberg is "a PBOC approved third-party electronic trading solutions provider". It is a licensee of the state's own infrastructure, not a rival to it.
4. **2025–2026: Electronic Markets, everywhere at once.** After the rename, cadence rises: Australia ×3, ABS, India, FX options API, JGB automation in ten months. The verbs move from *trade* to *automate* (API, Rule Builder, STP).
5. **Oct 2026: clearing as the next workflow.** The Treasury piece says the pre-trade check that done-away clearing needs is "the infrastructure for which has been in place on Bloomberg since the launch of its Swap Execution Facility". It also admits that "much of the done-away infrastructure the repo market will need is still being developed".

## 4. What the claims don't prove

1. **There is no denominator anywhere.** "73% of the USD swaps market on Bloomberg is now SOFR swaps" is a mix share *inside* Bloomberg, not Bloomberg's share of the market. +31%, 2x and +58% are growth rates with no base. Contrast Tradeweb, which reports **52% of industry SEF volume** for TW SEF in 2024 (context, from [[tradeweb-derivatives-regulation]]), and MarketAxess, which reported Open Trading at **27% → 38%** of its credit volume (context, from [[marketaxess-open-trading]]).
2. **The boilerplate KPIs drift.** The same paragraph claims "over 1,500 dealers" (Jun 2023, Apr 2024, May/Jun/Jul/Oct 2026) and "over 800 dealers" (Sep and Oct 2025, Jun and Sep 2026). Client firms are always 9,000 and markets always 175. In this corpus the 800 version appears on every London- and Hong Kong-datelined release from Sep 2025, while Sydney, New York, Mumbai and Tokyo say 1,500. The one exception is the London EGB release of Apr 2024, which says 1,500. A 47% swing in the headline liquidity count, depending on the issuing office, means neither number is an audited metric. The 800 may be a stale FXGO figure (FXGO said "800+ LPs" in 2020).
3. **The Rule Builder study is self-run and selection-biased.** It uses BTCA data on firms that chose RBLD, routing orders the rules flagged as low-touch. The claim "orders that used RBLD outperformed manual orders by 38%" compares easy orders with hard ones. The Rep below shows the desk-level numbers imply implausibly high automation shares unless selection explains much of the gap.
4. **‘First trade’ is a marketing unit, not an adoption metric.** Fourteen of the dated rows are first trades or day-1 counts. None is followed by a 12-month volume. Bridge is the extreme case: announced for Europe "in Q2 2022 and subsequently in the US and APAC", with no go-live, volume or Goldman follow-up anywhere in the corpus (the archive gap caveat applies).
5. **Gateways are rented, not owned.** CFETS, NDS-OM (Clearcorp), QCB and the HKMA rules set the scope, eligible dealers and timing. Southbound access depended on 13 HKMA-designated dealers, of whom Bloomberg had 8. Exclusivity was never claimed and does not exist: Tradeweb launched on Bond Connect, Southbound and Swap Connect too (context, from [[tradeweb-rates-em]]).
6. **The reference price is Bloomberg's own.** MOC-to-BVAL, PT baskets against BVAL/CBBT, and CBBT as the SOFR liquidity evidence: in each, the venue's quality is measured with the vendor's own ruler (see [[bloomberg-pricing-bval-ibval]]). This is the same flaw [[tradeweb-credit]] finds with Ai-Price.
7. **Some case studies are unfinished.** The Sun Life RFQe page lists ‘best price trades achieved per year’ with no figures, and its benefits paragraph is template text.

## 5. Strategic read (inference — not stated by Bloomberg)

- **The venue is a bundling device, not a profit centre to defend.** If Terminal seats are the revenue (context: Bloomberg discloses none), an RFQ that keeps the trader inside the Terminal raises retention whatever its share. So Bloomberg can enter a market at 1 trade (Qatar, IGB, ABS) without needing a share story. Tradeweb and MarketAxess, as listed venues paid by fee per million, cannot. This is counter-positioning ([[canon-helmer-7-powers]]): rivals can't copy ‘venue as a free feature’ without wrecking their P&L.
- **The trader's intent is captured upstream.** Rule Builder "alleviates the need to integrate the technology into their own in-house systems", and its rules route "on Bloomberg venues". FX chat quotes become structured (MYQ, Apr 2026). The FX options API gives systematic funds programmatic RFQ. Each of these moves the routing decision into Bloomberg's software before any venue competes for it.
- **Price → protocol is the moat that matters.** MOC to BVAL (EGB) and BB3P (JGB), and PT to BVAL. Once a closing reference is Bloomberg's, the venue that executes ‘at the close’ is naturally Bloomberg's. This mirrors Tradeweb's FTSE/ICE closing prices from the venue side (context, from [[tradeweb-rates-em]]).
- **Sell-side and buy-side on both ends.** ETOMS connects dealers to 40+ venues, including rivals. Broadway adds low-latency rates. TOMS answers Southbound RFQs. Bloomberg profits whichever venue the dealer quotes on: the arms-dealer position that Tradeweb, as a venue, does not hold.
- **Dealers as partners, never rivals.** J.P. Morgan is the counterparty on the €STR (2019) and EGB MOC (2024) firsts. Goldman staffs Bridge. JPMC's own corpus names no venue at all (context, from [[jpmc-markets-venues]]). Goldman is simultaneously broker, venue and principal (context, from [[goldman-markets-platforms]]). Bridge looks like a dealer-friendly answer to Open Trading: intermediated, not anonymous peer-to-peer. Its silence suggests that answer did not scale.
- **D&I as a liquidity-routing feature.** CastleOak's line, "a lower cost alternative for clients while still fulfilling best execution requirements", plus the Treasury white label, preceded Tradeweb's Spotlight program (2022, 14 dealers; context, from [[tradeweb-credit]]) by five years. It recruits buy-side mandates to Bloomberg RFQ at no cost to the big dealers behind it.
- **Geography is where the growth is.** China, India, Qatar, Malaysia, Azerbaijan, Australia: the venue follows the index inclusion (FAR → IGB) or the central bank's modernisation plan. The risk is political. Bloomberg's voice never mentions it (see [[bloomberg-mission-forces]]).
- **Treasury clearing is the next test.** Tradeweb (credit-check hub, Sponsored Repo; [[tradeweb-derivatives-regulation]]) and ICE Clear Credit (live Feb 3 2026; [[ice-clearing-treasury]]) are making the same claim. Whoever sits on the done-away pre-trade check owns a toll on repo after Jun 30 2027.

## 6. Canon lenses

- **Bundling and information goods** ([[canon-shapiro-varian-information-rules]]): the venue is a complement priced inside the seat. Switching costs come from rules, TCA history and chat, not from fees.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]], [[canon-cusumano-business-of-platforms]]): FXGO and BSEF bring dealers and buy-side together, but Bloomberg monetises the user side (seats), not transactions. That inverts the usual subsidy logic.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): dealers are suppliers, complementors (Bridge) and rivals (single-dealer platforms). The consolidated-tape JV made Tradeweb and MarketAxess partners at the same time; Bloomberg's own release carried MarketAxess calling Open Trading "widely regarded as the preferred all-to-all trading solution in the global credit markets", three months after Bridge (see [[bloomberg-consolidated-tape]]).
- **Sustaining innovation** ([[canon-christensen-innovators-dilemma]]): every protocol digitises an existing voice practice (EFP, BWIC, MOC). None disrupts the dealer.
- **Focal points** ([[canon-schelling-strategy-of-conflict]]): a closing price works because everyone uses it. Owning BVAL and BB3P-linked workflows makes Bloomberg's close the focal point.
- **Five forces** ([[canon-porter-competitive-strategy]]): sovereign gateways (CFETS, Clearcorp, QCB) are powerful suppliers that can license a second provider at will.
- **Noise and self-measurement** ([[canon-kahneman-sibony-sunstein-noise]]): a KPI that swings 1,500 ↔ 800 by press office is noise. Treat it as an unrated forecast.

## 7. Practitioner counterpoint

- **For Bloomberg:** the breadth is real and checkable from the outside. Counterparties are named (LBBW, J.P. Morgan, CME, BlackRock, State Street, HESTA, ANZ, ICBC). Regulators approve it (BNM, PBOC, ASIC, CFTC/FCA venue licences). Tradeweb's own CEO concedes the threat: "There was always Bloomberg looming out there at a minimum as a data company that was beginning to show prices for things." A trader who already lives in the Terminal gets RFQ, analytics, chat, TCA and automation in one place. That integration benefit is hard to price but obvious on a desk.
- **Against:** in the deepest markets the price is set elsewhere. USTs price on interdealer CLOBs and futures. US credit share is a Tradeweb/MarketAxess fight, measured on TRACE. US ETF RFQ: Tradeweb says $930bn in 2025 alone (context, from [[tradeweb-equities-retail]]). Bloomberg's silence on share is consistent with being a strong #2 or #3 in many places and #1 in few. And a Terminal-bundled venue is vulnerable when clients move to APIs and third-party EMSs. Bloomberg's own BI study shows EMSX losing European share (see [[bloomberg-buyside-stack]]).
- **Both:** a desk should judge Bloomberg's venues on its **own** TCA against a non-Bloomberg reference (TRACE/next print, the Tradeweb or ICE close, the futures-implied level). It should not use BVAL, CBBT or BTCA alone, the same rule [[tradeweb-credit]] §7 applies to Tradeweb.

## 8. Open questions to track

1. **Bridge.** Did it ever go live in the US and APAC? Is Goldman still the intermediary? Is it quietly folded into D&I/DirectPool-style intermediation?
2. **Dealer count.** Will Bloomberg reconcile 1,500 vs 800? Which one matches FXGO's LP list and FIT's dealer list?
3. **Treasury clearing.** After Dec 31 2026 (cash) and Jun 30 2027 (repo), does Bloomberg's SEF-era pre-trade check win done-away flow, or does Sponsored Repo make it irrelevant?
4. **MOC reach.** Will MOC-to-BVAL spread from EGBs to credit (US IG), where it would compete directly with Tradeweb's close and MarketAxess's auctions?
5. **Broadway.** Do sell-side rates wins appear (named banks, venues connected) three years after the deal?
6. **China risk.** Does the NAFMII valuation guideline (Apr 2026) or geopolitics change CFETS's appetite for a US vendor on Swap Connect and repo?
7. **Any share number.** Will a regulator's data (CFTC SEF volumes, ESMA MTF data, FINRA UST data) let an outsider size BSEF/BMTF? That would be the first independent check.
8. **ICE–MarketAxess and Tradeweb–Trumid.** Do the consolidations push Bloomberg to defend venue share explicitly for the first time?

**Links:** [[bloomberg-hub]] · [[bloomberg-pricing-bval-ibval]] (the ruler behind MOC and PT) · [[bloomberg-buyside-stack]] (AIM/EMSX/BTCA, EMSX share) · [[bloomberg-indices]] (index first, venue second: China, India) · [[bloomberg-consolidated-tape]] · [[bloomberg-mission-forces]] · [[bloomberg-people]] · [[bloomberg-outside-voices]] · [[bloomberg-terminal-instrumentation]] · [[tradeweb-hub]] · [[tradeweb-credit]] · [[tradeweb-rates-em]] · [[tradeweb-equities-retail]] · [[tradeweb-derivatives-regulation]] · [[marketaxess-open-trading]] · [[marketaxess-protocols-automation]] · [[goldman-markets-platforms]] · [[jpmc-markets-venues]] · [[ice-clearing-treasury]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[wss-rates-macro]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-schelling-strategy-of-conflict]]

---
### Rep
Three short computations with numbers from this note.

**(a) The SOFR mix, without a denominator.** In Jan 2022 Bloomberg's venue volume was +31% YoY and 73% of USD swaps on Bloomberg were SOFR. Treat the +31% as applying to USD swaps (an assumption; Bloomberg gives it for all venues). Index Jan 2021 USD volume = 100. What is LIBOR volume in Jan 2022, and the minimum fall in LIBOR volume if Jan 2021 was all LIBOR? *(Answer: 131 × 0.27 ≈ **35.4**, so LIBOR fell **≥64.6%**, while SOFR went from ~0 to 131 × 0.73 ≈ **95.6**.)* Then explain why none of this tells you whether BSEF gained or lost share against TW SEF's stated 52%. What public dataset would?

**(b) Unpicking the Rule Builder study.** The study says RBLD orders beat manual orders by 38% (US) and 68% (EU), and RBLD desks overall did 30% / 36% better than non-RBLD firms. Assume RBLD firms' manual orders cost the same as non-RBLD firms' manual orders. Then desk cost = 1 − 0.38a, where a is the automated share. Solve 1 − 0.38a = 0.70 and 1 − 0.68a = 0.64. *(Answer: US a ≈ **79%**, EU a ≈ **53%**.)* A 79% automation share for equity desks in 2022–23 is implausible. So either RBLD firms' manual orders were also better (selection: better desks adopt tools), or the order mix differs. Name two controls BTCA should have published.

**(c) The dealer-count swing.** The boilerplate says 9,000 client firms and either 1,500 or 800 dealers. Compute clients per dealer under each, and the percentage gap. *(Answer: **6.0** vs **11.25** clients per dealer. 800 is **47%** below 1,500.)* Map the 800 versions to their datelines (London, Hong Kong; one London 1,500 exception in Apr 2024) and write one sentence on what a buy-side due-diligence questionnaire should ask Bloomberg for instead: active responding dealers per asset class, per quarter.

---
**Sources (Bloomberg corpus, accessed 2026-10-25):**
- [China bond offering upgrade, 2019-07-02](https://www.bloomberg.com/company/press/bloomberg-upgrades-china-bond-offering-for-global-investors/)
- [All Bond Connect dealer prices / CIBM Direct, 2019-09-25](https://www.bloomberg.com/company/press/bloomberg-announces-further-enhancements-china-bond-offering/)
- [First €STR swap on BMTF, 2019-10-08](https://www.bloomberg.com/company/press/first-fully-electronic-estr-swap-trade-executed-via-bloombergs-uk-mtf/)
- [FXGO in Malaysia, 2020-06-24](https://www.bloomberg.com/company/press/bloomberg-will-now-offer-fxgo-as-an-approved-electronic-trading-platform-in-malaysia/)
- [CIBM-Direct RFQ event, 2020-10-28](https://www.bloomberg.com/company/press/capturing-investment-opportunities-in-chinas-16-trillion-bond-market/)
- [BBH + BSKT, 2020-10-28](https://www.bloomberg.com/company/press/brown-brothers-harriman-and-bloomberg-collaborate-to-develop-real-time-etf-primary-market-workflow-solution/)
- [SOFR/EFFR compression on BSEF, 2020-11-12](https://www.bloomberg.com/company/press/first-electronic-sofr-vs-fed-funds-compression-trade-executed-via-bloomberg-sef/)
- [FXGO cost analysis tool, 2020-11-23](https://www.bloomberg.com/company/press/bloomberg-fxgo-adds-supplementary-cost-analysis-tool/)
- [Danone FXGO case, 2021-02-05](https://www.bloomberg.com/professional/insights/markets/food-and-beverages-leader-transforms-fx-for-transparency-and-real-time-efficiency/)
- [PT Basket Builder, 2021-06-09](https://www.bloomberg.com/company/press/bloomberg-launches-portfolio-trading-basket-builder-incorporating-bval/)
- [Rule Builder for ETFs (Indosuez), 2021-06-28](https://www.bloomberg.com/company/press/indosuez-wealth-management-becomes-first-bank-to-automate-etf-trading-with-bloomberg-rule-builder/)
- [Southbound solutions, 2021-09-15](https://www.bloomberg.com/company/press/bloomberg-and-cfets-jointly-launch-new-solutions-to-facilitate-trading-on-southbound-bond-connect/) · [day 1, 2021-09-24](https://www.bloomberg.com/company/press/bloomberg-facilitated-trades-for-seven-hong-kong-market-makers-on-first-trading-day-of-southbound-bond-connect/) · [indicative prices, 2021-10-25](https://www.bloomberg.com/company/press/bloomberg-and-cfets-jointly-offer-indicative-prices-from-market-makers-on-southbound-bond-connect/)
- [COMSTAR–FXGO, 2021-12-01](https://www.bloomberg.com/company/press/comstar-and-bloomberg-fxgo-introduce-a-joint-solution-to-help-financial-institutions-improve-efficiency-of-fx-transactions/)
- [SOFR liquidity eclipses LIBOR, 2022-02-09](https://www.bloomberg.com/professional/insights/regulation/sofr-liquidity-eclipses-libor/)
- [Bloomberg Bridge, 2022-03-15](https://www.bloomberg.com/company/press/bloomberg-launches-global-all-to-all-bond-trading-service/)
- [CT exploration (MarketAxess boilerplate), 2022-06-22](https://www.bloomberg.com/company/press/consolidated-tape/)
- [Azerbaijan central bank, 2023-03-07](https://www.bloomberg.com/company/press/central-bank-of-azerbaijan-adopts-bloomberg-spot-matching-and-deposit-trading-solutions/)
- [Broadway agreement, 2023-03-13](https://www.bloomberg.com/company/press/bloomberg-enters-agreement-to-acquire-broadway/) · [CMA, 2023-09-06](https://www.bloomberg.com/company/press/cma-review-of-the-bloomberg-acquisition-of-broadway-technology-is-complete/) · [close, 2023-10-03](https://www.bloomberg.com/company/press/bloomberg-completes-acquisition-of-broadway-technology/)
- [ETOMS sell-side piece, 2023-04-20](https://www.bloomberg.com/professional/insights/trading/the-sell-side-is-seizing-the-benefits-of-digital-transformation/)
- [Swap Connect solution, 2023-05-05](https://www.bloomberg.com/company/press/bloomberg-collaborates-with-cfets-to-launch-new-solution-to-facilitate-swap-connect-trading/) · [day 1, 2023-05-15](https://www.bloomberg.com/company/press/bloomberg-facilitated-trades-for-offshore-investors-on-first-trading-day-of-swap-connect/)
- [Rule Builder enhancements, 2023-05-24](https://www.bloomberg.com/company/press/bloomberg-enhances-automated-trading-solutions-to-strengthen-client-execution/)
- [D&I Dealer initiative, 2023-06-20](https://www.bloomberg.com/company/press/bloomberg-expands-di-dealer-initiative/)
- [Rule Builder study, 2024-03-13](https://www.bloomberg.com/company/press/bloomberg-study-finds-automated-equity-trading-results-in-improved-performance/)
- [EGB MOC to BVAL, 2024-04-24](https://www.bloomberg.com/company/press/bloomberg-announces-first-trade-of-egb-market-on-close-spread-to-bval-price/)
- [Sun Life RFQe case, 2024-11-30](https://www.bloomberg.com/professional/insights/trading/optimizing-etf-trades-how-sun-life-leverages-bloombergs-rfqe/)
- [Qatar Central Bank, 2025-01-19](https://www.bloomberg.com/company/press/qatar-central-bank-enhances-financial-market-infrastructure-with-bloomberg-solutions/)
- [Offshore RMB repo, 2025-02-10](https://www.bloomberg.com/company/press/bloomberg-launches-new-solution-to-facilitate-bond-connect-offshore-rmb-bond-repurchase-trading-in-collaboration-with-cfets/) · [onshore expansion, 2025-09-29](https://www.bloomberg.com/company/press/bloomberg-rmb-repo-trading-solution-expands-reach-supporting-onshore-liquidity-access-for-global-investors/)
- [PT podcast, 2025-07-07](https://www.bloomberg.com/professional/insights/markets/how-is-portfolio-trading-changing-the-fixed-income-landscape/)
- [Southbound toolkit, 2025-09-22](https://www.bloomberg.com/company/press/bloomberg-tailors-toolkit-to-empower-southbound-bond-connect-participation/)
- [ICBC Swap Connect Europe, 2025-10-16](https://www.bloomberg.com/company/press/icbc-executes-first-swap-connect-trade-on-bloomberg-in-europe/)
- [ETF Shares BSKT, 2026-02-09](https://www.prnewswire.com/news-releases/etf-shares-selects-bloomberg-to-electronify-etf-primary-markets-workflows-302682604.html)
- [MYQ FX chat prices, 2026-04-13](https://www.prnewswire.com/news-releases/bloomberg-launches-fx-price-monitoring-tool-to-help-investors-discover-insights-from-their-chats-302740090.html)
- [Australian EFP, 2026-05-20](https://www.prnewswire.com/news-releases/bloomberg-expands-exchange-for-physical-offering-for-the-australian-markets-302777693.html)
- [EUR/GBP PT spread quoting, 2026-06-02](https://www.prnewswire.com/news-releases/bloomberg-introduces-spread-to-benchmark-quoting-for-eur-and-gbp-portfolio-trading-baskets-302787922.html)
- [ABS BWIC workflow, 2026-06-15](https://www.prnewswire.com/news-releases/bloomberg-introduces-electronic-trading-workflow-for-asset-backed-securities-302800245.html)
- [Indian government bonds, 2026-07-09](https://www.prnewswire.com/news-releases/bloomberg-introduces-electronic-trading-workflow-for-indian-government-bonds-302821054.html)
- [Australian ETFs/options/futures RFQe, 2026-07-30](https://www.prnewswire.com/news-releases/bloomberg-expands-electronic-trading-for-onshore-listed-australian-etfs-options-and-futures-302839438.html)
- [FX Options RFQ API, 2026-09-14](https://www.prnewswire.com/news-releases/bloomberg-electronic-markets-bring-full-programmatic-execution-support-to-fx-options-trading-302877140.html)
- [JGB MOC automation, 2026-10-04](https://www.prnewswire.com/news-releases/bloomberg-electronic-markets-brings-automation-to-its-japanese-government-bond-market-on-close-functionality-302897776.html)
- [Treasury clearing, 2026-10-08](https://www.bloomberg.com/professional/insights/regulation/cash-now-repo-next-planning-for-the-u-s-treasury-clearing-transition/)
- Tradeweb side: [Hult interview, 2026-08-05](https://www.tradeweb.com/newsroom/media-center/in-the-news/interview-with-the-ceo-billy-hult-tradeweb/)
