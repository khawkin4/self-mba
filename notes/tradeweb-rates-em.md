# Note · Tradeweb rates, government bonds & EM — the moat is the plumbing, and the next leg is turning plumbing into benchmarks and new countries

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — platforms, multi-sided networks), **Course 07** (Data, Analytics & Decision-Making — liquidity metrics, regression design), **Course 11** (Global Strategy, Macro & Responsible Business — China, Japan, Korea, Saudi, rate-benchmark reform), **E9** (Geopolitics & Macro for Decision-Makers), **E10** (Digital & AI Transformation) · Written 2026-10-24 · Companion to [[tradeweb-ai-price]] and [[tradeweb-a2a-information-leakage]]

- **Source:** Tradeweb newsroom (news releases, blogs, "Market Insights" commentary, reprinted press interviews), **75 items, Jun 18 2019 – Oct 9 2026**, rates / government bonds / repo / mortgages / EM / APAC bucket (`_ingest/raw/tradeweb/bucket-rates.jsonl`). PDF links cited, not opened. About 10 items are off-theme (DEI/awards profiles, Asia ETFs, European primary-market credit, TCA awards) and are left to [[tradeweb-hub]].
- **Core claim:** Tradeweb's rates story is not about one product. It is a **repeatable playbook**: (1) move a voice market onto RFQ, (2) add protocols and automation (direct streams, sessions, AiEX, RFM, list and close trading), (3) turn the flow into **data and official-looking benchmarks** (Gilt/UST/EGB closing prices, CMT rates, the Liquidity Cost Index), then (4) run the same playbook in the next country (China 2017 → Japan → Korea → Saudi 2025–26) or the next product (repo, specified pools, EM swaps, whole loans). The numbers Tradeweb publishes are almost all **self-reported, defined loosely, and chosen to flatter**, but taken together they describe a real flywheel. The weak point is the benchmark business: it sits on Tradeweb's own flow and is administered by its controlling shareholder's index arm.

---

## 1. Chronology — the spine

*All figures are Tradeweb's unless marked. "ADV" = average daily volume. Where a figure looks inconsistent with another, see §3.*

| Date | Event / metric | Detail (as stated) |
|---|---|---|
| Jul 3 2017 | **Bond Connect** launches; Tradeweb is the first offshore trading link | Tradeweb says it helped design the scheme with PBOC, HKMA, CFETS and HKEX |
| late 2017 | Direct streams in on-the-run (OTR) USTs for dealers/PTFs via **Dealerweb** (ATS) | Streaming firm two-way prices, bilateral |
| Sep 2018 | AiEX (rules-based auto-execution) goes live on Bond Connect; first Bond Connect platform with pre/post-trade block allocation | "Still the only Bond Connect platform offering automated trading" (Dec 2019) |
| Jun 18 2019 | Greenwich piece reprinted: **>60%** of UST trading on electronic venues; direct streaming **7.6%** of UST volume in May 2019, from ~0 five years earlier | ~two-thirds of UST trading (voice + electronic) is name-disclosed |
| Jul 3 2019 | Bond Connect year 2: **$280bn** cumulative, >18,000 trades, ADV **$1.1bn** in June 2019 (+406% since Jul 2017); onshore dealers 34 → 47; 1,038 approved investors. Dealer streaming prices + CFETS **iDeal** messaging | BIS: ~$12.9tn China bonds, only ~**2.4%** held offshore |
| Jul 22 2019 | Direct streams expanded; **STAQ** (firm streams) for institutional investors. Q2 2019 UST ADV record **$82.7bn** (+26.6% YoY); industry direct-streams share "approaching 10%" (Tradeweb estimate) | Streams ADV "more than quadrupled" YoY |
| Sep 10 2019 | **Tradeweb ICE U.S. Treasury Closing Prices** (IBA administrator, IOSCO, EY assurance) | >900 securities; Tradeweb then traded ~$80bn/day in USTs, prices from "as many as thirty" dealers; 3pm snap; modelled on the Gilt closes Tradeweb took over from the UK DMO in 2017 |
| Q3 2019 | Rates = **69%** of platform ADV, repo/money markets a further **28%** (Risk.net, Dec 2019) | Credit + equities a "small slice" |
| Dec 20 2019 | List trading on Bond Connect (40 trades/list; sub-accounts 30 → 50) | Price sourcing "could take up to half a day" before |
| Mar 2020 | COVID: platform ADV **>$1tn** for the month; UST **>$100bn** ADV; "busiest month ever" | Kirby: in this crisis clients fell back to plain RFQ, not the phone |
| May 5 2020 | April 2020 monthly: UST ADV **$89.0bn** (+16.7%), EGB **$27.3bn** (+23.4%), mortgages **$173.9bn**, rates derivatives **$199.7bn**, repo **$223.1bn** (+18.7%) | One-day records in UST, EGB, US credit on Apr 30 |
| Jun 5 2020 | Closing prices "pass the volatility test": 2-second captures from 2:59:30–3:00pm, **17** liquidity providers, outlier exclusion. Tradeweb becomes **exclusive** D2C quote source for ICE Swap Rate "Level 2" | Mar 11 2020 10y range 0.643%–0.860% |
| Jul 16 2020 | **Tradeweb ICE CMT Rates** published for consultation (VWAP 8am–3pm, 12 tenors, 18-month test) | No launch follow-up in the bucket |
| Jul 29 2020 | Bond Connect year 3: **$516bn** cumulative; June 2020 ADV **$1.25bn**; H1 2020 ADV $934mm vs $875mm H1 2019; average tenor 9.1y (6.5y in 2019) | Mostly CGBs and policy-bank bonds |
| Aug 2020 | First fully electronic RFQ into **CIBM Direct** (previously phone only) | — |
| Sep 22 2020 | **Specified pools**: mortgage originators can trade alongside the secondary market | TBA volume on Tradeweb ">$32tn" in first 8 months of 2020; SIFMA spec-pool market $25.9bn/day |
| Oct 7 2020 | SSA: ~**45%** of tickets via AiEX (70% of tickets < $500k); >40% of SSA volume against dealer axes, 60% of that via API axes; 15 currencies | EU €750bn recovery-fund issuance flagged as next test |
| Dec 15 2020 | EM 2020 YTD **>$742bn**: EM IRS **$432bn**, EM CDS **$50bn**, China bonds **>$249bn**; >350 active EM clients; EM-only portfolio trades ~$1.3bn | Portfolio trades with EM line items +300% since Q1 2019 |
| Jan 11 2021 | EGB: >50% of EUGV tickets via AiEX in Q3/Q4 2020; ~20% of gilts via trade-at-close lists; hit rates back above 70% by late Mar 2020 | March 2020 largest month, +40% YoY |
| Mar 5 2021 | Tradeweb regression: the EU recovery-fund announcement tightened 10y bid/offer **0.3–0.5bp** (ES, IT, PT), **>2bp** (GR), ~0.1bp (DE) | Jan 2019–Feb 2021, monthly |
| May 18 2021 | Repo ADV ~**$112bn** (Q1 2020) → **$215bn** (Q1 2021); term RFQs out to 2 years | Dealer-to-client term balances $712bn (Q1 2021) |
| Sep 8 2021 | LIBOR → RFR: **21** SONIA market makers, **25** €STR, **19** SOFR; >400 SONIA/LIBOR portfolios switched; Q1 2021 first quarter with majority of sterling swaps in SONIA | Compression tool re-purposed for switches |
| Sep 15 2021 | **Southbound Bond Connect** launch partner (live Sep 24); **>$900bn** CNY bonds traded via Tradeweb since 2017 | China called a "$15 trillion onshore bond market" |
| Jan 24 2022 | EGB: ~**60%** of tickets fully automated (Oct 2021); 42 LPs in UK/Europe; APA serving >100 firms | — |
| Jan 31 2022 | Repo: 2021 ADV **$336.8bn**; Fed RRP >$1.8tn peak | SFTR (Jul 2020) cited as the post-trade "hook" |
| Feb 7 2022 | **Jump Trading** streams EGBs via EUGV STAQ API; Jan 2022 EGB ADV record **$37.0bn** (+22.2%) | >40 market makers, 19 countries, 6 currencies |
| Feb 10 2022 | 2021 UST ADV on Tradeweb **>$120bn** (+32.2%); RFQ+ (RFQ checked against live streams); trade-at-close lists | Buy-side quotes: SSGA, JPMAM, Vanguard |
| Aug 4 2022 | TIPS: HHI **0.13** (vs 0.08 nominal USTs); sub-second auto-quotes ~**70%** of responses (from ~50%); AiEX >20% of TIPS tickets; **Citadel Securities** starts TIPS market-making | Tradeweb TIPS volume "more than doubled" 2016–21 |
| Oct 18 2022 | EM IRS in **13** markets; 2021: APAC IRS +116%, yen swaps +42%, JGBs +28% | Platform ADV >$1tn in 2021 |
| Jan 10 2023 | EGB: Sep 2022 record month; Oct 2022 gilt volume 2× Oct 2021 (UK mini-Budget); dealer quote ratio ~85%, client hit ratio **75%**; **70%** of client tickets fully automated | ECB depo −50bp → 200bp in 2022 |
| May 15 2023 | **Swap Connect** live (CNY IRS via OTC Clear); Tradeweb a launch platform | >1tn yuan (~$138bn) in year 1, per domestic media |
| May 24 2023 | **Tradeweb FTSE Euro Government Bond Closing Prices** (FTSE Russell administrator, Tradeweb calculation agent); Q1 2023 EGB ADV record **$42.4bn** | Same method as the UK Gilt closes |
| Jan 11 2024 | Mexico TIIE-28 → F-TIIE; Tradeweb traded **>$660bn** TIIE-28 in 2023 | Mexican swaps market cited as $4.9tn |
| Jan 31 2024 | Cleared EM IRS in **16** currencies; EM IRS composite/curve data product launched | Asian: HKD, CNY, INR, KRW, SGD, TWD, THB |
| Apr 2 2024 | **ECB** re-awards Tradeweb two ETP framework agreements (also won in 2015): EGBs, covered, repo, USTs, JGBs, SSA, USD/JPY IRS | 4 years + 2 + 2 |
| Jun 10 2024 | **Tradeweb FTSE U.S. Treasury Closing Prices** replace the ICE-administered series in the newsroom narrative: bid/offer as well as mid, 3pm and 4pm snaps, incl. bills, STRIPS, TIPS | EU/UK BMR + IOSCO |
| Jul 25 2024 | Cross-market (non-contingent) trading: EUR IRS +100% and EGB +75% (Q2 2024 vs Q2 2023, delta terms), EGB >€1bn ADV; repo + OIS-hedge workflow; Dubai office | — |
| Feb 4 2025 | Coalition Greenwich MBS study (39 buy-side traders, Tradeweb data): ~60% trade almost all TBAs on venues; >75% of ABS/CMO/spec-pool/CMBS still phone/chat for most respondents | Commissioned/co-published with Tradeweb |
| Feb–May 2025 | Israel **Telbor → SHIR** (cessation Jun 30 2025; LCH conversion May 17 2025); "$1.4tn swaps market" | SHIR = BOI policy rate, so it is effectively a policy-rate swap |
| May 6 2025 | Tariff shock: Tradeweb **UST OTR T-Cost** 0.03 → **0.17bp** (Apr 2025) vs 0.05 → **0.58bp** (Mar 2020); **$472.5bn** one-day US government bond volume on Apr 9 2025; 10y +49bp Apr 4–11 | Gilts spiked more than EGBs |
| May 29 2025 | Novaprime × Tradeweb mortgage-pipeline hedging on the **Canton Network** | Digital-asset tie-in |
| Sep 26 2025 | UST closing price window cut to the **one second** before 4:00pm, effective Oct 17 2025 | Was 30 seconds at 3pm in 2019 |
| Oct 2025 | **Saudi ATS** launched after selection by the CMA; first trade BlackRock vs BNP Paribas | Kingdom's first regulated electronic bond market |
| Dec 18 2025 | **JGBs**: Tradeweb JGB volume +~350% (2020–24), +23% YoY (Q1–Q3 2025); offshore ~two-thirds of flow; domestic share <20% → >35%; electronic share of JGB D2C est. **45–50%** (vs ~25% in 2019); yen swaps 30–40% electronic, "majority" on Tradeweb | JGB lists up to 60 lines; Hikene (at-close) trading |
| Jan 9 2026 | After the order for Fannie/Freddie to buy **$200bn** MBS: MBS T-Cost +~500% vs 1-year median while UST T-Cost stayed below median; MBS >20bp tighter vs USTs | Shown via the new index |
| Feb 12 2026 | Strategic investment in **MAXEX** (residential whole-loan exchange, ~400 lenders, >250 PLS deals) | Terms not disclosed; Troy Dixon joins board |
| Mar 24 2026 | **Tradeweb Liquidity Cost Index** (realised T-Cost, realised vol, composite width) across USTs, swaps, TBAs, CDX IG | Live intraday series "planned" |
| Mar 27 2026 | Tradeweb-commissioned FT Longitude survey: 71% (85/120) of Asia traders mostly electronic vs 9% "five years ago" | — |
| Apr 17 2026 | **JIBAR → ZARONIA**: first ZARONIA trade on Tradeweb (Rand Merchant Bank) early 2026; no new JIBAR from May 2026; CCP conversion in Nov; cessation Dec 2026 | — |
| Jul 7 2026 | **Korea WGBI** inclusion (phase-in Apr–Nov 2026); KTBs ~2% of index; market "approaching US$1tn" | "One of the region's most active markets on our platform" |
| Sep 17 2026 | Saudi **local-to-local** trading: GIB Capital × Saudi Awwal Bank, settled via Muqassa/Edaa | Domestic route added to the offshore one |
| Oct 9 2026 | APAC local-currency bonds: Tradeweb dealer participation "roughly doubled" since Jan 2026; AiEX gains **RFM price evaluation**, dynamic liquidity check, RFQ Pro exception handling, batch release around market closes | ADB: EM East Asia LCY bonds $30.6tn end-2025 (ASEAN ~$2.7tn) |

**Scale backdrop (boilerplate at the foot of each release):** platform ADV ">$540bn" (Mar 2019) → ">$1tn" (2021–22) → ">$1.4tn" (Apr 2024) → ">$2.2tn" (May 2025) → ">$2.6tn" (Feb 2026) → ">$2.9tn" (Sep 2026). Clients ~2,500 in 60 countries → >3,000 in 85+. Four-quarter trailing notional, not revenue. Repo and swaps inflate it.

## 2. The narrative and how it shifted

1. **2019 — "we are a search engine; everything goes digital."** Olesky (Risk.net, Dec 2019): Tradeweb is "essentially search"; addressable market $6.5tn/day; even USTs "40% … still not electronic". The rates pitch was **protocol breadth**: RFQ (Tradeweb's own 1998 invention), CLOB via Dealerweb, sessions (Sweep), and direct streams. Streams were first seen as a threat to venues, and Tradeweb chose to **aggregate them rather than fight them** (the 1990s-equities analogy in the Greenwich piece). At the same time, a **benchmark** sideline (Gilt closes, then UST closes) and **China** as a first-mover access franchise.
2. **2020–21 — COVID as proof of concept.** The repeated line is that in March 2020 clients "reverted to … RFQ", not to the phone, unlike 2008 when "our screens went literally blank" (Bruni). Repo (SFTR audit trails), EM swaps (+65% QoQ in Q1 2020), the 20Y bond and issuance studies all serve one argument: **volatility now helps the venue**. The research arm (Jonathan Rick) puts out macro-flavoured studies — elections, TIPS, the EU recovery fund — that double as marketing for Tradeweb data.
3. **2022–23 — the rate shock and automation.** The message shifts from "electronic vs voice" to "**not whether to automate, but how much**" (EGB 60% → 70% of tickets automated). New non-bank liquidity (Jump in EGBs, Citadel in TIPS) is presented as more depth, not disintermediation. The firm becomes the **plumbing for rate-benchmark reform**: SONIA/SOFR/€STR switches, then F-TIIE, SHIR and ZARONIA, each with a resource centre and NPV-list conversion tool.
4. **2024–26 — data products, sovereign-grade infrastructure, frontier geographies.** Closing prices move to **FTSE Russell** (EGBs 2023, USTs 2024) and gain bid/offer. A **Liquidity Cost Index** turns T-Cost into a public reference. The ECB re-award, the Saudi CMA mandate and Korea's WGBI entry recast Tradeweb as **national market infrastructure**. Mortgages extend from agency TBA/spec pools into **private residential credit** (MAXEX) and DLT (Canton). The 2026 APAC line, "from access to execution", says the access problem is solved and the money is now in workflow automation.

**The constant:** "collaborative innovation". Every launch is framed as client-requested. The thing that actually changes is **what Tradeweb sells**: execution (2019) → execution plus automation (2022) → execution plus automation plus reference data and country infrastructure (2024–26).

## 3. What the claims don't prove

1. **Almost every number is self-reported and undefined.** "ADV" moves between all-client and institutional-only, and between single-counted and double-counted repo. Repo ADV is "around **$112bn**" for Q1 2020 in one 2021 interview, yet April 2020's monthly report gives repo ADV of **$223.1bn**, up 18.7% YoY. Both cannot be the same metric. EGB volumes are quoted in USD, and EGB cross-market growth "in delta terms". Read every figure as **Tradeweb-defined**.
2. **Internal arithmetic slips.** The May 2025 blog says the March 2020 T-Cost "surged roughly **20x**, climbing from 0.05bps to 0.58bps". That is **11.6x**. It also dates the peak "March 8", which was a Sunday. The 2021 EM interview footnotes "$420bn YTD … as of June 2020" for EM swaps, but the Dec 2020 blog has only $432bn for the whole of 2020 (the footnote probably means 2021). The closing-price source is "as many as thirty" dealers (2019) and then "17 different liquidity providers" (2020). These are small errors, but they show the numbers are not audited the way 10-K figures are.
3. **Tickets ≠ notional.** "70% of client tickets fully automated" (EGB) and "45% of SSA tickets via AiEX" are **count** shares, and the counts are dominated by small tickets (70% of <$500k SSA tickets). The automated share of **risk** is unreported. AiEX's "8% improvement on bid-offer capture" vs RFQ (Bruni 2022) has no definition, no sample and no control for which orders were automated (easy ones).
4. **Market-share estimates come from the seller.** Direct streams at "approaching 10%" of UST volume, JGB electronic share at 45–50% ("our own estimates from conversations … with dealers and JSDA data"), and "majority" of electronic yen swaps are all Tradeweb estimates of markets it competes in. No denominator is published.
5. **Surveys built to agree.** The 2026 Asia survey was commissioned by Tradeweb (FT Longitude fielded it). "71% now vs 9% five years ago" compares a current answer with a **remembered** one from the same respondents, which is a recall-bias design. The 2025 MBS study is 39 traders and uses Tradeweb data.
6. **The regressions are thin.** The EU recovery-fund study runs one OLS per country on **~26 monthly observations** (Jan 2019–Feb 2021) with a post-Aug-2020 dummy. That dummy cannot separate the EU fund from PEPP, vaccine news or the general post-COVID normalisation. The issuance regression "didn't have strong explanatory power" for notes, and Tradeweb says so, which is to its credit.
7. **Benchmark conflicts.** Closing prices are calculated **from Tradeweb's own platform quotes**. Since 2023–24 they are administered by **FTSE Russell, an LSEG business**, and the 2019 Risk.net piece notes Refinitiv, later acquired by LSEG, held a **54%** controlling stake in Tradeweb. The 2025 change to a **one-second** window just before 4pm makes the price more "executable" but also more exposed to a single quote update. No surveillance statistics or manipulation tests are published.
8. **Survivorship in the newsroom.** CMT Rates (2020 consultation) never reappears. ICE-administered UST closes quietly become FTSE-administered. Bond Connect cumulative totals stop after 2021, and Swap Connect volume is sourced to "domestic media", not Tradeweb. Silence after a launch is itself information.
9. **"Volatility helps us" is unproven across cycles.** The evidence covers three stress episodes (Mar 2020, Sep–Oct 2022, Apr 2025), all of them central-bank-backstopped. Bruni's own example (2008, "screens went literally blank") shows that a stress episode in which dealers' balance sheets are the problem can still empty a venue.

## 4. Strategic read *(inference, not Tradeweb's claims)*

- **Rates is the cash engine and the moat is network plus integration, not protocol.** Every protocol (RFQ, streams, RFM, sessions) gets copied. What doesn't get copied easily is being wired into ~3,000 clients' OMSs, being a regulated venue in many jurisdictions (EU MTF, UK, Dealerweb ATS, HK/SG, CMA-supervised Saudi ATS), and being chosen by central banks (ECB twice) and regulators (CFETS twice, CMA). Those are **switching-cost and cornered-resource** powers ([[canon-helmer-7-powers]]).
- **The playbook is a country-by-country land grab with a time limit.** China shows the template: be the first link, embed with the state operator, add familiar tools (allocations, lists, AiEX), then report cumulative volume. Korea (WGBI) and Saudi (CMA mandate) follow it. The risk is that each access scheme is **policy-granted**. CFETS, CMA or a sanctions regime can widen access to competitors, or close it.
- **Benchmarks turn flow into rent.** A closing price that index funds, ETF issuers and trade-at-close contracts reference is a **focal point** ([[canon-schelling-strategy-of-conflict]]). Once a WGBI index uses Tradeweb FTSE closes, clients are pulled toward trading at Tradeweb's close on Tradeweb. That is the most durable asset in this bucket, and also the one most exposed to a governance scandal (see the LIBOR history Tradeweb itself recounts).
- **Coopetition with liquidity providers.** Dealers were Tradeweb's founders and owners (46% before the IPO, 17.3% after the Oct 2019 follow-on). PTFs (Jump, Citadel, XR, Virtu) now stream to those same dealers through Tradeweb. Tradeweb stays neutral by **aggregating whoever is cheapest** (RFQ+, STAQ) ([[canon-brandenburger-nalebuff-coopetition]]).
- **Mortgages are the under-electronified prize.** By Tradeweb's and Greenwich's account, TBAs are on screen while spec pools, CMOs, CMBS and whole loans are mostly phone/chat. MAXEX and Canton are cheap options on that market rather than core bets (terms undisclosed). The Jan 2026 MBS T-Cost spike shows Tradeweb already has the data to sell into this segment.
- **Rate-benchmark reform is a recurring, under-appreciated revenue event.** Each IBOR → RFR switch (GBP, USD, EUR, MXN, ILS, ZAR) forces portfolio-wide re-coupon/switch trades by a fixed date, executed through Tradeweb's NPV list tool. It is low-glamour, high-certainty volume, and the list of remaining IBORs is short.

## 5. Canon lenses

- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): each new market is a chicken-and-egg problem. Tradeweb's lever is to bring the dealer side first (34 → 47 Bond Connect dealers; dealer participation in APAC LCY "roughly doubled"), then advertise buy-side counts.
- **Focal points** ([[canon-schelling-strategy-of-conflict]]): a closing price is valuable because everyone uses the same one. In the Bloomberg example, three funds marked the same Treasury at 101.1880 / 101.1820 / 101.1758.
- **Information goods** ([[canon-shapiro-varian-information-rules]]): composites, T-Cost indices and closing prices are near-zero marginal cost by-products of trading. They can be priced by value (index licensing) and versioned (EOD vs live intraday "planned").
- **Disruption from below** ([[canon-christensen-innovators-dilemma]]): direct streaming began as PTF-led disintermediation of venues. Tradeweb absorbed it within ~2 years instead of defending RFQ margins.
- **Normal accidents** ([[canon-perrow-normal-accidents]]): tightly coupled cash–futures–repo trades (basis trades, which Tradeweb now electronifies) are where March-2020-type failures start. A faster venue makes the coupling tighter, not looser.
- **Noisy evidence** ([[canon-kahneman-sibony-sunstein-noise]]): commissioned surveys and single-dummy regressions are the kind of evidence that confirms the commissioner's view.

## 6. Practitioner counterpoint

- **For Tradeweb:** buy-side heads quoted by name (SSGA, JPMAM, Vanguard) describe concrete workflow wins: trade-at-close lists, voice processing, electronic basis. Those are what make a desk stay. EGB hit ratios of ~75% through the 2022 gilt crisis, and T-Cost staying a fraction of March 2020 in April 2025, are consistent with a venue that holds up under stress.
- **Against:** in USTs the price is set in the interdealer CLOB (BrokerTec/CME, Fenics) and futures; Tradeweb's own 2019 piece calls the CLOB "the benchmark price for the entire market". D2C venues price **off** that. In China, Bloomberg also has RFQ links to CFETS (Caixin piece). First-link status did not mean exclusivity.
- **Both:** the best evidence for the moat is not any statistic here. It is that central banks, sovereign regulators and index administrators keep choosing Tradeweb. That cannot be faked in a blog post.

## 7. Open questions to track

1. Does Tradeweb publish **share of the Korean/WGBI flow** or KTB volumes after the Nov 2026 phase-in completes, or just "engagement"?
2. Saudi ATS: volumes, number of local dealers, and whether the CMA licenses a second venue.
3. Do **Tradeweb FTSE UST closes** get adopted in a major index (e.g. FTSE WGBI pricing, which the Sep 2025 note says they are "intended" for)? Any surveillance disclosures on the 1-second window?
4. Liquidity Cost Index: does the **live intraday** version ship, is it licensed, and does anyone outside Tradeweb cite it in a stress event?
5. MAXEX: any disclosed volume or a step-up to control?
6. Repo: how much is **cleared/sponsored** versus bilateral as the SEC Treasury clearing mandate phases in *(context, not from Tradeweb)*. The bucket is silent on this.
7. China: Bond Connect / Swap Connect volumes after 2021 are not in the newsroom. Is that slower growth, or just a change in disclosure?
8. Remaining RFR switches after ZARONIA (Dec 2026). When this event-driven volume runs out, what replaces it?

## 8. One-line takeaway

Tradeweb's rates franchise compounds by being **first, wired-in and neutral** in each new market, and it is now converting that position into **reference data and state-sanctioned infrastructure**. Treat the volume and automation statistics as marketing. Treat the mandates (ECB, CFETS, CMA, FTSE Russell) as the real evidence.

**Links:** [[tradeweb-hub]] · [[tradeweb-ai-price]] · [[tradeweb-a2a-information-leakage]] · [[wss-rates-macro]] · [[market-structure-24-5-trading]] · [[market-structure-24-5-institutional-response]] · [[trading-floor-mechanics]] · [[wss-trading-hedge-funds]] · [[bloomberg-terminal-instrumentation]] · [[canon-helmer-7-powers]] · [[canon-schelling-strategy-of-conflict]] · [[canon-shapiro-varian-information-rules]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-perrow-normal-accidents]]

---
### Rep
You run execution for a $40bn global bond fund. Use only numbers from this note unless told otherwise.

**(a) Check the vendor's maths.** Tradeweb's UST OTR T-Cost went 0.05 → 0.58bp (Mar 2020) and 0.03 → 0.17bp (Apr 2025). Compute each peak-to-baseline multiple, and compare the first with Tradeweb's "roughly 20x".

**(b) Put it in dollars.** You must sell $500mm of 10y notes at each peak. Assume modified duration 8.5 *(your assumption)*, so DV01 ≈ $500mm × 8.5 × 0.0001 = **$425,000/bp**. What is the liquidity cost at 0.58bp and at 0.17bp?

**(c) Reconcile cumulative and ADV.** Bond Connect on Tradeweb: $280bn cumulative (Jul 2019) → $516bn (Jun 2020) → >$900bn (Sep 2021). With ~250 trading days a year, what ADV does each interval imply? Does the first interval match Tradeweb's reported H1 2020 ADV of $934mm?

**(d) Decide.** One paragraph: if you could fund only one of Tradeweb's 2026 bets — Korea WGBI/APAC LCY automation, Saudi ATS, or MAXEX whole loans — which has the best ratio of addressable flow to policy risk, and which number in §1 would you most want audited first?

*Answers:* (a) 11.6x and ~5.7x. The "20x" is wrong as stated. (b) ~$246,500 vs ~$72,250, a ~$174k difference on one trade. (c) ($516bn − $280bn) / ~250 days ≈ **$0.94bn/day**, which matches the $934mm H1 2020 ADV. ($900bn − $516bn) / ~300 days (15 months) ≈ **$1.28bn/day**, so growth continued but slowed in relative terms.

---
### Sources (Tradeweb newsroom, via `_ingest/raw/tradeweb/bucket-rates.jsonl`)
- 2019-06-18 [How Bilateral Streams for U.S. Treasuries Really Work](https://www.tradeweb.com/newsroom/media-center/in-the-news/how-bilateral-streams-for-u.s.-treasuries-really-work)
- 2019-07-03 [Price Streams and iDeal for Bond Connect](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-introduces-price-streams-and-ideal-messaging-tool-for-bond-connect-investors/) · [Two Years, $280bn – Bond Connect](https://www.tradeweb.com/newsroom/media-center/insights/blog/two-years-$280-billion-in-trades--chinas-bond-connect-celebrates-second-anniversary-with-record-volumes-and-new-features-on-tradeweb/)
- 2019-07-22 [Direct Streams in U.S. Treasuries](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-expands-direct-streams-capabilities-in-u.s.-treasuries)
- 2019-09-10 [Tradeweb ICE U.S. Treasury Closing Prices](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-markets-and-ice-benchmark-administration-launch-tradeweb-ice-u.s.-treasury-closing-prices) · [FT: new benchmark for $16tn market](https://www.tradeweb.com/newsroom/media-center/in-the-news/tradeweb-lines-up-new-benchmark-for-$16tn-treasuries-market/)
- 2020-05-05 [Robust April Trading (monthly)](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-reports-robust-april-trading/)
- 2020-06-05 [Closing Prices Pass the Volatility Test](https://www.tradeweb.com/newsroom/media-center/insights/blog/tradeweb-ice-u.s.-treasury-closing-prices-pass-the-volatility-test)
- 2020-07-16 [Tradeweb ICE CMT Rates consultation](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-markets-and-ice-benchmark-administration-introduce-tradeweb-ice-cmt-rates--for-review-and-comment-by-market-participants/)
- 2020-07-29 [Bond Connect third anniversary](https://www.tradeweb.com/newsroom/media-center/insights/blog/500-billion-reasons-to-celebrate-the-third-anniversary-of-bond-connect/)
- 2020-09-22 [Mortgage (spec pool) platform expansion](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-announces-expansion-of-mortgage-trading-platform/)
- 2020-10-07 [Best SSA Platform (AiEX/axes)](https://www.tradeweb.com/newsroom/media-center/in-the-news/best-ssa-bond-trading-platform-tradeweb/)
- 2020-11-19 [Key Takeaways from the UST Market in March 2020](https://www.tradeweb.com/newsroom/media-center/insights/blog/key-takeaways-from-the-us-treasury-market-in-march-2020/)
- 2020-12-15 [New Pathways to EM Opportunities](https://www.tradeweb.com/newsroom/media-center/insights/blog/electronification-puts-spotlight-on-emerging-markets-fixed-income/)
- 2021-03-05 [EU funding plan bolsters country-bond liquidity](https://www.tradeweb.com/newsroom/media-center/insights/commentary/bold-european-union-funding-plan-bolsters-country-bond-liquidity/)
- 2021-05-18 [Term repo demand rises](https://www.tradeweb.com/newsroom/media-center/in-the-news/dealers-offer-two-year-quotes-as-term-repo-demand-rises/)
- 2021-09-08 [European Markets Choice Awards (Bruni: RFRs, China)](https://www.tradeweb.com/newsroom/media-center/in-the-news/european-markets-choice-awards-winner-tradeweb/)
- 2021-09-15 [Southbound Bond Connect](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-partners-with-cfets-to-launch-southbound-bond-connect-extending-china-footprint/)
- 2022-01-31 [Electronic Repo in the Spotlight](https://www.tradeweb.com/newsroom/media-center/insights/blog/electronic-repo-trading-takes-a-turn-in-the-spotlight/)
- 2022-02-07 [Jump Trading joins EGB marketplace](https://www.tradeweb.com/newsroom/media-center/news-releases/jump-trading-joins-tradewebs-european-government-bond-marketplace/)
- 2022-08-04 [Yes, 'People' Are Worried About Inflation (TIPS)](https://www.tradeweb.com/newsroom/media-center/insights/commentary/yes-people-are-worried-about-inflation/)
- 2023-01-10 [Market Innovations Boost EGB Liquidity](https://www.tradeweb.com/newsroom/media-center/insights/blog/market-innovations-boost-egb-liquidity-in-volatile-times/)
- 2024-04-02 [ECB selects Tradeweb](https://www.tradeweb.com/newsroom/media-center/news-releases/european-central-bank-selects-tradeweb-to-supply-electronic-trading-platforms/)
- 2024-06-10 [Tradeweb FTSE U.S. Treasury Closing Prices](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-and-ftse-russell-extend-benchmark-closing-prices-to-u.s.-treasury-markets)
- 2025-02-04 [Electronification Set to Grow in MBS (Greenwich)](https://www.tradeweb.com/newsroom/media-center/in-the-news/electronification-is-set-to-grow-in-mbs-markets/)
- 2025-05-06 [Tariffs Stress-Testing Liquidity](https://www.tradeweb.com/newsroom/media-center/insights/blog/bond-market-turbulence-how-tariffs-are-stress-testing-liquidity/)
- 2025-09-26 [UST closing-price methodology change](https://www.tradeweb.com/newsroom/media-center/in-the-news/change-to-the-tradeweb-ftse-us-treasury-benchmark-closing-price-methodology/)
- 2025-12-18 [Transforming Japan's Trading Landscape](https://www.tradeweb.com/newsroom/media-center/in-the-news/transforming-japans-trading-landscape/)
- 2026-02-12 [Investment in MAXEX](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-makes-investment-in-maxex-to-expand-access-to-the-institutional-marketplace-for-u.s.-residential-mortgages)
- 2026-03-24 [Liquidity Cost Index](https://www.tradeweb.com/newsroom/media-center/insights/blog/measuring-what-matters-a-new-lens-on-liquidity-in-u.s.-rates)
- 2026-04-17 [ZARONIA transition](https://www.tradeweb.com/newsroom/media-center/insights/blog/preparing-for-the-zaronia-transition-key-milestones-and-what-comes-next/)
- 2026-07-07 [Korea's WGBI Inclusion](https://www.tradeweb.com/newsroom/media-center/insights/blog/koreas-wgbi-inclusion-is-driving-a-new-phase-of-investor-engagement/)
- 2026-09-17 [Saudi local-to-local execution](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-expands-saudi-debt-market-access-with-domestic-execution-capabilities/)
- 2026-10-09 [From Access to Execution: APAC LCY](https://www.tradeweb.com/newsroom/media-center/insights/blog/from-access-to-execution-scaling-apac-local-currency-bond-trading/)
