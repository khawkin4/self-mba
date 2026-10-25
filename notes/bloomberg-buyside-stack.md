# Note · Bloomberg buy-side stack — the OMS war is being fought on switching costs, and Bloomberg is quietly trading 'integrated' for 'composable' because its own research shows the bundle leaking at the EMS layer

> Practitioner / competitive-strategy note · Maps to **Course 04** (Competitive Strategy — switching costs, bundling, coopetition), **Course 03** (Microeconomics — complements, bundling, two-sided referee problems), **Course 06** (Operations — front-to-back workflow, automation), **Course 07** (Data, Analytics & Decision-Making — survey denominators, frozen boilerplate), **E10** (Digital & AI Transformation — API-first operating models), **E8** (Stakeholder & Investor Relations — reading a private company's own narrative) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-electronic-trading]], [[bloomberg-pricing-bval-ibval]], [[bloomberg-private-markets]], [[blackrock-aladdin-data]]

- **Source:** Bloomberg corpus at `_ingest/raw/bloomberg/articles.jsonl`. About 120 items mention AIM, PORT, EMSX, BTCA, MARS, MAC3, Rule Builder (RBLD), RFQe, CTM, Vault or the buy-side unit, **Sep 2019 – Oct 2026**: client-win releases (PR Newswire and bloomberg.com/company/press), Professional Services 'Insights', Bloomberg Intelligence (BI) survey notes and BTCA product blogs. Reader notes P5–P8 and DELTA were used to find items; every number below was re-read in the full text. Bloomberg is private and **no revenue, seat or margin figures for the buy-side unit exist in the corpus.** The only hard competitive data is BI's European Institutional Equity Trading (EET) study, published **Aug 7 and Dec 8 2025**, which carries BI's standard disclaimer: "Any views in this note are those of the author and Bloomberg Intelligence and don’t necessarily reflect those of Bloomberg LP."
- **Core claim:** Bloomberg sells a full buy-side stack: research (RMS) → portfolio analytics and risk (PORT/PORT Enterprise, MAC3, MARS) → order management (AIM) → execution (EMSX, TSOX, FXEM, RFQe, Rule Builder) → measurement (BTCA) → post-trade (CTM matching, RHUB reporting) → surveillance (Vault), all tied to the Terminal. Through 2025 the pitch was the **integrated bundle**. By 2026 the same unit calls itself **modular, API-first and composable**, partners with Clearwater for accounting instead of building it, and sells TCA as a **neutral referee** that scores other vendors' executions. Read this as a strategic retreat to the layers where Bloomberg's switching costs are strongest (OMS, analytics, data, measurement). Its own research arm shows the bundle leaking in Europe: **EMSX fell from 52% to 41% EMS share in one year**, while **AIM (24%) leads Charles River (23%) by only 1pp** and **Aladdin is at 13%** (BI EET, Aug 2025). Meanwhile the company's self-reported AIM stats did not change for **~28 months at a time**.

---

## 1. Chronology — the spine

All figures are as Bloomberg states them ('BBG says') unless BI or a client is named.

| Date | Event | Numbers stated |
|---|---|---|
| 2019-08-26 | China Industrial Securities adopts 'Buy-Side Solutions' (AIM, BTCA, Vault) | — |
| **2020-09-29** | First AIM/PORT boilerplate in the corpus (Charles Taylor IM win) | AIM: "nearly 15,000 professionals", 900+ firms, 90+ countries, **>$17tn**. PORT: **93 of top 100** managers, **47,000** active users |
| 2020-11-03 | **Lombard Odier IM** expands PORT Enterprise (AIM client since before 2019) | Peckett: "Our integrated and scalable buy-side solutions support the entire front-to-back workflows for our clients" |
| 2021-04-16 | BTCA peer-analytics blog: the fixed-income peer universe thins as filters are added | Example firm −0.98bp vs peers −12.69bp (GB bonds, arrival price) |
| 2021-04-26 | Peckett blog: COVID load test | AIM Q1 2020 executions +85% week on week. PORT daily hits +80% |
| **2021-06-28** | **Indosuez** is the first bank to automate ETF trading with Rule Builder on RFQe | Sawhney: rules run on Bloomberg, "which alleviates the need to integrate the technology into their own in-house systems" |
| 2021-10-04 | BI: algo wheels in Europe lag the US | US wheel use **64%**. Europe 8.8 providers per wheel vs US 8.4 |
| 2022-07-19 | Vault investment in Insightful Technology (Soteria) | 120+ e-comms, voice, video, mobile and trade channels |
| 2022-09-22 | Baader Bank RBLD case study | RBLD trades **+16%** vs arrival price compared with manual |
| 2023-02 → 05 | AIM AUM boilerplate jumps from $17tn to **$22tn** (last $17tn: Feb 8 2023; first $22tn: May 9 2023) | Users (~15,000) and firms (900+) unchanged |
| 2023-04-11 | Vancity win; first PORT Enterprise client count | PORT Enterprise **>550 clients**. PORT 47,000 users across 15,000 firms |
| 2023-05-24 | Rule Builder enhancements (timed release, order rerun, econ-data triggers) | "Fixed income Rates activity automated through RBLD has more than doubled since 2021". Round lots >$5m ~5x |
| 2023-07-12 | 'Open architecture' insight: Terminal Connect, APIs, third-party integration | — |
| **2024-03-13** | BTCA study of RBLD: **23m orders**, 2022–23 | RBLD firms' overall performance +30% (US) / +36% (EU). RBLD orders beat manual by **38% (US) / 68% (EU)** on implementation shortfall |
| 2024-04-03 | Buy-side trends (Strevens, Mirsepassi): T+1 via CTM + SWIFT | "97% of all trades going through our system are matched on T+0 and 70% of all trades are sent to settlement on T+0" |
| 2024-06-27 | PORT sustainability tools | PORT Enterprise **>650 clients** |
| 2024-11-30 | **Sun Life HK** case study: RFQe inside AIM for ETF trades | "After evaluating several ETF trading solutions, SAM chose Bloomberg’s RFQe as it can streamline ETF trading within a comprehensive offering." |
| 2024-12-04 | PORT Enterprise data to Snowflake via DL+ | PORT Enterprise **>600 clients** (down from 650 six months earlier) |
| 2025-01-19 | Qatar Central Bank: Bloomberg Auction System + AIM for primary dealers | First auction Dec 26 2024 |
| 2025-02-05 | MARS adds SEC 18f-4 / AIFMD / UCITS / NI 81-102 VaR | MARS: >1,100 professionals at 900+ firms |
| **2025-03-04** | **Goodbody**: AIM added on top of existing TOMS/RHUB sell-side use | "The ability to have an OMS solution embedded within the same technology infrastructure as our existing Bloomberg sell-side solutions adds significant value" |
| **2025-03-26** | **LGT Wealth Management**: AIM + PORT Enterprise + BTCA + RHUB, including acquired abrdn Capital funds | Ribas: 'interoperability and integration' is the stated strength |
| **2025-07-09** | **Clearwater Analytics partnership**: front-to-back with Clearwater accounting | "an open and modular approach". Flatman: "relying on a single provider that may not meet all their needs". Clearwater AUM >$8.8tn |
| **2025-08-07** | **BI EET 2025 (preview)** | OMS: **AIM 24%** (+1pp), **Charles River 23%** (gap was 3pp), **Aladdin 13%**, in-house 11%. EMS: **EMSX 41% (from 52%)**. Algo wheels **42%** (from 33%) |
| 2025-09-23 | AI Portfolio Commentary in PORT Enterprise. Unit renamed **'Investment Management Solutions'** in boilerplate | PORT Enterprise **>750 clients** |
| 2025-09-30 | Maxwealth (QDII) win: last AIM boilerplate in the corpus | Still ~15,000 / 900+ / **$22tn**, ~28 months unchanged |
| 2025-11-26 | Singapore summit: IBOR / Total Portfolio View, Clearwater tax-lot plug-in, ML in Rule Builder | "Most firms, Lewis noted, still lack a single authoritative IBOR" |
| **2025-12-08** | **BI EET 2025 (technology)** | OMS changed after 2020: **41%** (+23pp). "nearly a quarter haven’t made a change in more than 15 years". 73% rely on third-party post-trade TCA, 11% on brokers |
| 2026-04-02 | MAC3 expanded to public + private assets; boilerplate back to 'buyside solutions' | PORT Enterprise **>800 clients** |
| 2026-05-21 | **Pacer**: AIM + EMSX + RBLD Optimizer for ETF rebalances | First 'composable' boilerplate: "composable solutions that enable firms to assemble an operating model aligned to their strategy, scale and priorities" |
| **2026-05-29** | **Lombard Odier** group-wide risk: AIM + PORT Ent + MARS + Data Validation Service | Ribas: "a modern API-first architecture that enhances transparency and streamlines operations". Client: "By relying on a single, consistent framework, we strengthen risk oversight" |
| 2026-06-23 | **Mackenzie** adopts MAC3 (C$265bn AUM, May 31 2026) | 3,000+ factors, daily. "A portfolio should only carry the risk we intend." |
| **2026-07-08** | **Pre-Trade TCA API** (fixed income + equities) | AllianzGI: "In our testing, estimated transaction costs closely aligned with realized execution costs." 15 years of execution research |
| 2026-07-13 | **TimesSquare**: PORT + RMS Enterprise | Ribas titled 'Global Head of Buy-Side Solutions' |
| 2026-08-05 | Vault AI surveillance models (insider dealing, personal trading) | Impax: fewer false positives |
| **2026-08-26** | **Brandes**: AIM + PORT Ent + EMSX + BTCA + indices | "bring together order management, trading and risk analytics within a single workflow". Ribas now 'Global Head of Buy-Side *Enterprise* Solutions' |
| **2026-09-22** | **NFU Mutual** (~$32bn): Bloomberg front office + Clearwater accounting | "a seamless, flexible front-to-back composable operating model". Clearwater AUM now >$10tn |
| **2026-10-04** | **JGB market-on-close automation** (Rule Builder + TSOX), co-developed with **BlackRock** | BlackRock's Chaudhry: "we were pleased to collaborate with Bloomberg on introducing the protocol" |
| 2026-10-13 | BTCA blog (Googe, Abd Allah): fixed-income TCA skeptic piece | "Bloomberg combines execution data from Bloomberg and third-party trading systems, enabling firms to evaluate all trading activity, not just trades executed on Bloomberg." |

## 2. The stack, layer by layer, with its best numbers

| Layer | Product(s) | Headline metric (source) | Lock-in mechanism | Contested by |
|---|---|---|---|---|
| Research | RMS Enterprise | — (folded into PM workflow, 2025) | Analyst history, tear sheets | In-house, CRMs |
| Portfolio & risk analytics | PORT / PORT Enterprise, MAC3, MARS | 93/100 top managers, 47,000 users (2020–21). PORT Ent >550 → >800 clients (2023–26). MARS >1,100 users, 900+ firms (2025) | Attribution history, factor-model continuity, risk limits calibrated to MAC3 | MSCI/Barra, Aladdin risk (context, not from Bloomberg) |
| Order management | AIM (+ PM&lt;GO&gt;) | ~15,000 users, 900+ firms, $17tn → $22tn (BBG). **24% European OMS share** (BI) | Compliance rules, position book, custodian feeds | **Charles River 23%**, **Aladdin 13%**, in-house 11% (BI) |
| Execution | EMSX, TSOX, FXEM, RFQe, Rule Builder | **EMSX 41%** EMS share (from 52%) (BI). RBLD rates volume >2x since 2021 | Broker connectivity, automation rules | Virtu, FlexTrade, Instinet Newport (13% each among large firms), Ullink (BI) |
| Measurement | BTCA, Pre-Trade TCA API | 23m orders in the RBLD study. 73% of desks rely on third-party post-trade TCA (BI) | Peer universe, TCA history | Independent TCA vendors, broker TCA (only 11% trusted, BI) |
| Post-trade & regulatory | CTM, RHUB, IBOR | 97% matched / 70% to settlement on T+0 (BBG, 2024) | Settlement plumbing | Custodians, Clearwater (accounting) |
| Surveillance | Vault | 120+ channels (2022). AI models (2026) | Archive of IB chat and voice | Specialist surveillance vendors |

**Read across the table:** the layers with the strongest lock-in (analytics history, OMS rules, TCA history, the chat archive) are where Bloomberg holds share or publishes growth. The layer it is losing, the EMS, is the one where switching is cheapest: broker FIX connections are standard, and an EMS can sit under any OMS.

## 3. How the narrative moved

1. **2020–2021: 'integrated front-to-back'.** Releases lead with "Integrated OMS" (Lombard Odier 2020, All Nippon 2023). The proof points are scale (93/100, $17tn) and resilience (COVID volumes). Clients praise consolidation: "Instead of having several separate systems, we now have all securities defined and disseminated in one way across our organization" (Lombard Odier IM, 2020).
2. **2021–2024: automation and measurement as the glue.** Rule Builder plus BTCA close a loop. Bloomberg automates the order, then scores the automation with its own TCA (Baader +16%, the 23m-order study). Openness first appears as 'open architecture' (Jul 2023), meaning APIs into the Bloomberg stack rather than modularity.
3. **Jul 2025: the Clearwater turn.** Bloomberg declines to build accounting and partners instead, framing the choice against "relying on a single provider" (read: Aladdin, which Bloomberg never names). Weeks later BI publishes the EMSX share loss.
4. **Sep 2025 – Apr 2026: naming churn.** The boilerplate changes from 'Buy-Side Solutions … through a suite of integrated offerings' (2023–Aug 2025) to 'Investment Management Solutions … with a modular and flexible approach' (Sep–Dec 2025), then to 'buyside solutions' (Apr 2026), then back to 'Buy-Side Solutions' (May 2026 on). Leader titles move too: Peckett, 'Global Head of Buy-Side Solutions' (2020) → '…Product' (2021); Alves, 'Global Head of Buy-Side OMS' (2023) → '…Order and Investment Management Solutions' (2024–25); Ribas, 'Global Head of Buy-Side Solutions' (2025–Jul 2026) → '…Enterprise Solutions' (Aug 2026).
5. **2026: 'composable' and 'API-first'.** Pacer (May), Lombard Odier (May) and NFU (Sep) carry the new words. TCA becomes an API that runs on *any* firm's flow, and BTCA is pitched as ingesting third-party execution data. Clients are still quoted praising a 'single workflow' (Brandes) and a 'single, consistent framework' (Lombard Odier). The vendor's language has moved; the buyer's has not.

## 4. What the claims don't prove

1. **The AIM boilerplate is frozen, not measured.** It said $17tn from Sep 2020 to Feb 2023 (~29 months), then $22tn from May 2023 to Sep 2025 (~28 months). Users (~15,000) and firms (900+) never moved in five years, and no AIM figure appears after Sep 2025. A +29% AUM jump with flat users and firms is a re-statement, not a trend. Don't use these as time series.
2. **PORT counts drift and mix units.** PORT Enterprise is >550 (Apr 2023), >650 (Jun 2024), >600 (Dec 2024), >750 (Sep 2025), >800 (Apr 2026), so the series falls once. PORT's '15,000 client firms' (2021–25) is a different universe from AIM's 900 firms; it probably counts Terminal-level PORT access. The '93 of the top 100' line disappears after 2021.
3. **The only share data comes from Bloomberg's own research arm and one region.** EET covers European buy-side *equity* traders. The 2025 algo-wheel figure rests on 103 head and senior traders. It says nothing about US OMS share, fixed income EMS (TSOX) or multi-asset. Its candour (EMSX down 11pp) is a credibility signal, but its sample is small (Rep (a)).
4. **'Bloomberg alone shed 11%' versus a 23pp jump in renewals.** The same study shows OMS and EMS renewal after 2020 both up 23pp from the prior survey. A swing that big in one year more likely reflects a change in sample composition than true market churn. The EMSX decline may be partly a sample effect.
5. **The automation studies grade Bloomberg with Bloomberg.** RBLD's +38%/+68% is measured in BTCA against Bloomberg-computed arrival prices, on firms that *chose* to automate their easiest flow. It is a selection effect until proven otherwise. The BTCA team itself concedes that pre-trade models face skepticism; BI reports that only 52% of the 64% who estimate pre-trade costs use them at the point of execution.
6. **Client wins are a numerator without a denominator.** LGT, Lombard Odier, Brandes, TimesSquare, NFU, Mackenzie, Pacer, Goodbody, Gravis, BayernInvest, Triodos and others are announced. No loss is ever announced, and several wins are expansions of existing clients (Lombard Odier, Brandes, TimesSquare, Mackenzie, Goodbody).
7. **'Neutral referee' is asserted, not audited.** BTCA scores executions on EMSX, RFQe and Rule Builder, which Bloomberg sells. It also cites "one of the industry’s largest peer networks" without a size. The 2021 peer blog admits "The more granular the analysis, meaning the more groups that are combined, the fewer observations are available."

## 5. Strategic read (inference — not stated by Bloomberg)

- **Defend the sticky layers, concede the liquid ones.** Re-implementing an OMS means migrating compliance rules, position history and custodian feeds; BI finds nearly a quarter of desks unchanged for 15+ years. An EMS is a routing screen over standard FIX. Bloomberg's 2026 moves (AIM-anchored wins, MAC3 into PORT, a TCA API, IBOR) all deepen the sticky layers. Losing 11pp of EMS share hurts less if the OMS, the analytics and the *measurement of the rival EMS* remain Bloomberg's.
- **'Composable' is a rival-specific weapon.** Aladdin's pitch is one platform and one book of record (context, from [[blackrock-aladdin-data]]: tech revenue ~$1.5bn in 2023 and +16% organic ACV in 2025, with Charles River and Clearwater in its own benchmark set). Bloomberg cannot out-integrate a firm that runs $10tn+ on its own system, so it reframes integration as concentration risk. The irony: Clearwater's own boilerplate sells "integrating portfolio management, trading, investment accounting, reconciliation, regulatory reporting, performance, compliance, and risk analytics in one unified system". By 2026 it calls itself "the natively agentic investment management platform built on a single, continuously reconciled investment record". The partner covets the front office. *(Context, not from Bloomberg: Clearwater bought the OMS/PMS vendor Enfusion in 2025, which made it a direct AIM competitor for hedge funds. Hedged; verify.)*
- **Coopetition is the operating mode, not an exception.** BlackRock is the #3 European OMS rival (13%, rising) and the co-designer of Bloomberg's JGB MOC automation (Oct 2026). Tradeweb pipes Ai-Price and AllTrade into Aladdin (context, from [[tradeweb-credit]]). Clearwater partners on insurers while building a front office. Goodbody buys sell-side TOMS and buy-side AIM from the same vendor. Each counterparty is a complement in one layer and a substitute in another ([[canon-brandenburger-nalebuff-coopetition]]).
- **TCA is the toll booth that survives unbundling.** If the stack unbundles, whoever measures execution quality across all vendors keeps a seat at every desk. BI's own data supports the bet: buy-side traders trust third parties (73% reliant) and distrust brokers (11%). The 2026 API and third-party data ingestion turn BTCA from a feature of EMSX into an independent product. The risk is that the referee also owns teams in the game (§4.7).
- **Bundle pull-through still works where it matters.** The win list shows land-and-expand: TOMS → AIM (Goodbody), AIM → PORT Ent (Lombard Odier 2019–20, Brandes 2026), PORT → group-wide MARS (Lombard Odier 2026), indices riding along (Lombard Odier, Brandes; see [[bloomberg-indices]]). The pricing link matters too: BVAL/IBVAL and CBBT feed PORT, MAC3 and BTCA benchmarks ([[bloomberg-pricing-bval-ibval]]). The data layer is the real bundle; the screens are its delivery mechanism ([[bloomberg-terminal-instrumentation]]).

## 6. Canon lenses

- **Switching costs and lock-in** ([[canon-shapiro-varian-information-rules]], [[canon-helmer-7-powers]]): attribution history, factor-model continuity and TCA baselines are *durable* switching costs, because history cannot be ported. EMS routing is a *transient* one. The share data sorts the layers exactly this way.
- **Coopetition / value net** ([[canon-brandenburger-nalebuff-coopetition]]): map BlackRock, Clearwater and State Street as complementors in some layers and competitors in others. Bloomberg's 'added value' is highest where it is both the data source and the measurer.
- **Five forces** ([[canon-porter-competitive-strategy]]): buyer power rises as API-first stacks lower the cost of swapping modules. Bloomberg's answer is to *become* the modularity standard (the Clearwater plug-in, the TCA API) rather than resist it.
- **Platforms and bundling** ([[canon-cusumano-business-of-platforms]], [[canon-hagiu-wright-multi-sided-platforms]]): bundling pays when the components' values are negatively correlated across buyers. Composable selling is a bet that buyers now value components *differently*, so mixed bundling beats pure bundling.
- **Disruption from below** ([[canon-christensen-innovators-dilemma]]): cloud-native, single-instance rivals (Clearwater, Enfusion-type) attack from the insurer and hedge-fund segments first. Note that BI shows AIM leading in *small and medium* firms (31%/30%), and Charles River leading in large ones (33%).
- **Noise and self-grading** ([[canon-kahneman-sibony-sunstein-noise]]): treat the RBLD outperformance and any 1–3pp survey moves as hypotheses, not findings.

## 7. Practitioner counterpoint

- **For Bloomberg:** BI publishing EMSX's 11pp loss is unusually honest for a vendor's research arm. The Terminal plus AIM plus IB chat remains the default desktop for many small and mid-size managers (AIM 31%/30% in those segments). Client language is consistent over six years: fewer systems, one security master, one workflow. The JGB MOC co-build with BlackRock shows that even the biggest rival finds Bloomberg's venue and automation layer worth using.
- **Against:** the EMS is where traders spend their day, and losing it to Virtu, FlexTrade and Newport erodes the data and order flow that feed BTCA's peer universe. The boilerplate stats are stale, so the scale claim is unverifiable. 'Composable' may be a euphemism for losing the full-stack mandates to Aladdin and Charles River at large firms.
- **Both:** a COO choosing a stack should price the *exit*, not the entry. Ask for data-export terms on attribution history, TCA history and compliance rules. Test whether BTCA scores third-party EMS fills as fairly as EMSX fills. Insist on an IBOR that is not owned by the execution vendor.

## 8. Open questions to track

1. **EET 2026:** does EMSX stabilise above 40%, and does Charles River pass AIM (it closed 2pp in one year)?
2. **AIM boilerplate:** will Bloomberg publish a new AIM user/AUM figure, or drop the line (none since Sep 2025)?
3. **Clearwater:** does the partnership survive Clearwater's own front-office push? Watch for a second accounting partner, or for Bloomberg building or buying an IBOR/accounting book (the 2025 summit points to IBOR).
4. **BTCA neutrality:** will Bloomberg publish TCA comparing EMSX and non-Bloomberg EMS fills on the same benchmark?
5. **Aladdin coopetition:** more BlackRock co-built protocols (MOC in other markets), or a visible rupture?
6. **Private assets:** does Canoe (completed Oct 2026) plus MAC3 privates make PORT a whole-portfolio rival to Aladdin + Preqin? See [[bloomberg-private-markets]].
7. **Naming:** which label sticks, Buy-Side Solutions, Investment Management Solutions or Enterprise Solutions? Title churn sometimes precedes a reorganisation (see [[bloomberg-people]]).

**Links:** [[bloomberg-hub]] · [[bloomberg-electronic-trading]] (venues, RFQe, Rule Builder, MOC) · [[bloomberg-pricing-bval-ibval]] (the price inside PORT and BTCA) · [[bloomberg-indices]] · [[bloomberg-private-markets]] (Canoe, MAC3 privates) · [[bloomberg-enterprise-data]] (DL+, Snowflake) · [[bloomberg-ai-strategy]] · [[bloomberg-people]] · [[bloomberg-outside-voices]] · [[bloomberg-mission-forces]] · [[bloomberg-terminal-instrumentation]] · [[blackrock-aladdin-data]] · [[blackrock-hub]] · [[tradeweb-credit]] · [[tradeweb-tech-ai-data]] · [[tradeweb-a2a-information-leakage]] · [[ice-marketaxess-deal]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]] · [[canon-porter-competitive-strategy]] · [[canon-cusumano-business-of-platforms]] · [[canon-christensen-innovators-dilemma]] · [[canon-kahneman-sibony-sunstein-noise]]

---
### Rep
Four computations with numbers from this note.

**(a) Is AIM really ahead of Charles River?** BI EET 2025: AIM 24% (+1pp, so 23% in 2024) and Charles River 23% (the gap was 3pp, so 20% in 2024). Assume n ≈ 103 respondents (the trader count BI cites). (i) Compute each vendor's one-year change. *(AIM +1pp, CRD +3pp.)* (ii) Compute the standard error of the AIM−CRD difference in one multinomial sample: SE = √[(p₁ + p₂ − (p₁ − p₂)²)/n]. *(√[(0.47 − 0.0001)/103] ≈ **6.8pp**; the 1pp gap is ~0.15 SE, which is statistical noise.)* (iii) If the trend held, when would Charles River lead? *(Gap closes 2pp a year, so next survey: CRD 26% vs AIM 25%.)* Write one sentence a Bloomberg product head could and could not claim from this.

**(b) The EMS leak, decomposed.** EMSX 52% → 41%. The top four EMS vendors lost a combined 15pp. (i) Absolute and relative EMSX decline? *(−11pp; −11/52 = **−21%**.)* (ii) Bloomberg's share of the top-four loss? *(11/15 ≈ **73%**.)* (iii) Implied churn: 41% of desks changed OMS after 2020, so roughly five years gives ~8% a year and an average tenure of ~12 years. Can an 8%-a-year churn market lose 11pp from one vendor in one year? *(Only if nearly every switcher left EMSX, or the sample changed, as §4.4 argues.)* Decide which explanation the Dec 2025 renewal data (+23pp) supports.

**(c) Frozen boilerplate.** AIM is $22tn / 900 firms / ~15,000 users. (i) Average AUM per firm and per user? *(≈ **$24.4bn** per firm; ≈ **$1.47bn** per user, up from $1.13bn at $17tn.)* (ii) The $17tn → $22tn jump is +29% with zero user or firm growth. Over 2020–2025, would you expect market beta alone to explain it, with user counts flat? (iii) PORT Enterprise went >550 (Apr 2023) → >800 (Apr 2026). Compute the CAGR. *((800/550)^(1/3) − 1 ≈ **13.3%**.)* Then explain the 650 → 600 dip (Jun → Dec 2024) as rounding, a redefinition or real churn, and say what you'd ask Bloomberg to resolve it.

**(d) Pricing the automation claim.** Assume a desk's manual implementation shortfall is −10bp on $2bn of annual European equity flow. BTCA says RBLD orders beat manual by 68% in Europe. (i) Dollar value if that held for all flow? *(6.8bp × $2bn = **$1.36m** a year.)* (ii) Now assume only the easiest 40% of flow is automated, and that half of the measured edge is selection (easy orders). Recompute. *(0.4 × $2bn × 3.4bp = **$272k**.)* (iii) Name one third-party benchmark you would use to test the claim. Given BI's 73%/11% trust split, say why the answer should not come from BTCA alone.

---
**Sources (Bloomberg corpus, `_ingest/raw/bloomberg/articles.jsonl`, accessed 2026-10-25):**
- [Charles Taylor IM / AIM-PORT boilerplate, 2020-09-29](https://www.bloomberg.com/company/press/charles-taylor-investment-management-selects-bloomberg-to-streamline-investment-workflow/)
- [Lombard Odier IM, PORT Enterprise, 2020-11-03](https://www.bloomberg.com/company/press/bloomberg-streamlines-investment-and-risk-management-at-lombard-odier-investment-managers/)
- [BTCA peer analytics, 2021-04-16](https://www.bloomberg.com/professional/blog/addressing-the-confidence-challenge-of-peer-analytics-in-post-trade-tca/)
- [Peckett, buy-side partner, 2021-04-26](https://www.bloomberg.com/professional/blog/a-buy-side-technology-partner-thats-on-your-side/)
- [Indosuez Rule Builder on RFQe, 2021-06-28](https://www.bloomberg.com/company/press/indosuez-wealth-management-becomes-first-bank-to-automate-etf-trading-with-bloomberg-rule-builder/)
- [BI algo wheels, 2021-10-04](https://www.bloomberg.com/professional/blog/algo-wheels-can-revolutionize-buyside-trading-but-scale-needed/)
- [Rule Builder enhancements, 2023-05-24](https://www.bloomberg.com/company/press/bloomberg-enhances-automated-trading-solutions-to-strengthen-client-execution/)
- [Open architecture, 2023-07-12](https://www.bloomberg.com/professional/insights/markets/4-advantages-of-bloombergs-open-architecture/)
- [RBLD/BTCA automation study, 2024-03-13](https://www.bloomberg.com/company/press/bloomberg-study-finds-automated-equity-trading-results-in-improved-performance/)
- [Buy-side trends / CTM T+0, 2024-04-03](https://www.bloomberg.com/professional/insights/markets/buy-side-tech-trends-to-watch-in-2024/)
- [Sun Life RFQe, 2024-11-30](https://www.bloomberg.com/professional/insights/trading/optimizing-etf-trades-how-sun-life-leverages-bloombergs-rfqe/)
- [MARS 18f-4, 2025-02-05](https://www.bloomberg.com/company/press/bloomberg-enhances-mars-market-risk-support-of-derivatives-risk-regulations/)
- [Goodbody AIM, 2025-03-04](https://www.prnewswire.com/news-releases/goodbody-enhances-portfolio-management-workflow-with-adoption-of-bloomberg-aim-302391024.html)
- [LGT Wealth Management, 2025-03-26](https://www.prnewswire.com/news-releases/bloombergs-integrated-buy-side-solutions-selected-by-lgt-wealth-management-to-help-streamline-workflows-and-power-future-growth-302411067.html)
- [Clearwater partnership, 2025-07-09](https://www.bloomberg.com/company/press/bloomberg-and-clearwater-analytics-partner-to-optimize-investment-management-workflows/)
- [BI EET 2025 technology, algo and TCA trends, 2025-08-07](https://www.bloomberg.com/professional/insights/artificial-intelligence/eet-2025-technology-algo-and-tca-trends/)
- [Intelligent automation / IBOR summit, 2025-11-26](https://www.bloomberg.com/professional/insights/artificial-intelligence/intelligent-automation-for-front-office/)
- [BI EET technology study, 2025-12-08](https://www.bloomberg.com/professional/insights/trading/european-institutional-equity-trading-study-technology/)
- [Pacer RBLD Optimizer, 2026-05-21](https://www.prnewswire.com/news-releases/pacer-advisors-streamlines-etf-rebalancing-workflow-with-bloombergs-order--execution-management-solutions-302778127.html)
- [Lombard Odier group risk, 2026-05-29](https://www.prnewswire.com/news-releases/lombard-odier-enhances-investment-risk-framework-across-the-group-through-expanded-collaboration-with-bloomberg-302784784.html)
- [Mackenzie MAC3, 2026-06-23](https://www.prnewswire.com/news-releases/mackenzie-investments-implements-bloombergs-multi-asset-risk-model-to-enhance-portfolio-risk-forecasting-302807292.html)
- [Pre-Trade TCA API, 2026-07-08](https://www.prnewswire.com/news-releases/bloomberg-launches-pre-trade-tca-api-bringing-execution-intelligence-into-proprietary-trading-workflows-302820323.html)
- [TimesSquare, 2026-07-13](https://www.prnewswire.com/news-releases/timessquare-capital-management-selects-bloombergs-buy-side-solutions-for-unified-portfolio-and-research-management-302823391.html)
- [Vault AI models, 2026-08-05](https://www.prnewswire.com/news-releases/bloomberg-vault-introduces-new-ai-powered-communications-surveillance-models-302843724.html)
- [Brandes, 2026-08-26](https://www.prnewswire.com/news-releases/brandes-investment-partners-selects-bloomberg-buy-side-solutions-to-modernize-investment-management-302859841.html)
- [NFU Mutual + Clearwater, 2026-09-22](https://www.prnewswire.com/news-releases/nfu-mutual-selects-bloomberg-and-clearwater-analytics-for-front-to-back-investment-management-workflow-302885834.html)
- [JGB MOC automation with BlackRock, 2026-10-04](https://www.prnewswire.com/news-releases/bloomberg-electronic-markets-brings-automation-to-its-japanese-government-bond-market-on-close-functionality-302897776.html)
- [BTCA fixed income benchmarks, 2026-10-13](https://www.bloomberg.com/professional/insights/financial-services/beyond-the-benchmark-using-advanced-analytics-to-navigate-fixed-income-trading-costs/)
