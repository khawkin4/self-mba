# Note · Bloomberg and the EU/UK bond consolidated tape — three rival APA owners tried to run the public utility that would price their own data, quit after 534 days, and Bloomberg has written about the tape ever since without once mentioning its own bid

> Practitioner / market-structure note · Maps to **Course 03** (Microeconomics — public goods, versioning, incentive design), **Course 04** (Competitive Strategy — coopetition, incumbents vs a utility), **Course 11** (Global Strategy, Macro & Responsible Business — EU/UK market-structure regulation), **Course 07** (Data, Analytics & Decision-Making — trade-count vs notional transparency, survey denominators), **E8** (Stakeholder & Investor Relations — reading a company's silences), **E9** (Geopolitics & Macro for Decision-Makers — EU/UK regulatory divergence) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-enterprise-data]], [[bloomberg-electronic-trading]], [[bloomberg-pricing-bval-ibval]], [[tradeweb-derivatives-regulation]], [[marketaxess-data-cp-plus]]

- **Source:** Bloomberg corpus (`_ingest/raw/bloomberg/articles.jsonl`): the three joint statements (2022-06-22 and 2023-05-23 on Bloomberg's press page; the 2023-12-08 exit statement present in the corpus **only via Tradeweb's newsroom**), the Bridge launch (2022-03-15), seven Bloomberg Professional Services regulatory pieces (Feb 2024 – Oct 2025), the BI European Institutional Equity Trading Study (2025-12-08) and a 2026-10-13 TCA piece. Tradeweb corpus (`_ingest/raw/tradeweb/articles-2019-2026.jsonl`): APARMA launch (2022-05-27) and four transparency blogs (Dec 2025 – Jun 2026). Sibling notes give the MarketAxess and Tradeweb sides. Bloomberg is private: there are no revenue or data-line numbers anywhere in the corpus, so none appear here.
- **Core claim:** In 2022–23 the three largest fixed-income APA operators (Bloomberg, MarketAxess, Tradeweb) formed a JV to bid for ESMA's bond consolidated-tape-provider (CTP) mandate, pitching it as a tape built on *existing infrastructure*, i.e. theirs. They signed in May 2023 (Neil Ryan to lead, FINBOURNE as tech), then walked away on 2023-12-08, citing "uncertain outcomes around product definitions and structural complexities". Bloomberg then wrote at least **seven** regulatory pieces (2024–25) covering CTP rules, revenue redistribution, the cost of market data, TRACE 1-minute and FINRA's next-day Treasury data, with **zero** references to its own bid. Its own research arm (BI, Dec 2025) found only **28%** of European equity buy-side desks interested in switching to a tape and said the EU design "doesn’t yet appear to be a viable alternative to market feeds". *Inference:* a public tape is a substitute at the low end of the vendor's data stack; the incumbents' best move was to shape it, then to not own it, then to sell the layer above it.

---

## 1. Chronology — the spine

All figures as the named source states them.

| Date | Event | Numbers / words stated |
|---|---|---|
| **2022-03-15** | Bloomberg launches **Bridge**, all-to-all bond RFQ, "supported by dedicated Goldman Sachs intermediation desks". Europe go-live Q2 2022 | 3,700+ institutional and dealer firms in network. Greenwich: US corporate A2A ~5% (2017) → 12% (2020). No go-live follow-up release ever appears in the corpus (P2) |
| 2022-05-27 | **APARMA** (APAs and ARMs Association) founded by affiliates of Bloomberg, Cboe Europe, Euronext, LSE, MarketAxess and Tradeweb (Tradeweb newsroom) | 6 founders. Chair: Chris Smith (MarketAxess). Goal: make sure "the voices of APA and ARM operators – whose activities are critical to the achievement of policy goals – are heard" |
| **2022-06-22** | Bloomberg, MarketAxess and Tradeweb **jointly explore** an EU fixed-income CTP bid | Says they are "in a unique position to deliver a reliable, efficient and cost-effective consolidated tape service". JV to be "established and operated independently from our respective businesses". EU only |
| same release | The *About MarketAxess* boilerplate on Bloomberg's own page | Open Trading is "widely regarded as the preferred all-to-all trading solution in the global credit markets" — **99 days** after Bloomberg launched Bridge against it |
| **2023-05-23** | **JV agreement signed**; **Neil Ryan** appointed to lead; **FINBOURNE** chosen as tech provider after a tender | Ryan: "Our motivation is to improve transparency and spur electronification in the fixed income space." Parties aim to "make a meaningful investment in winning the tender for the European bond CT". Ryan has 30+ years' experience, per the release |
| same | FINBOURNE CEO Thomas McHugh on the partners | "highly experienced in fixed income markets and running regulated Approved Publication Arrangements (APAs)" |
| **2023-12-08** | The three **will not form** the CTP company, for the EU **or the UK** (first UK mention) | "the risk and complexity of delivering this project under a joint venture from our three firms". Costs and timeline would "significantly increase". In the Bloomberg corpus this exists only as a Tradeweb newsroom page |
| 2024-02-05 | Bloomberg reg brief: EU Parliament adopts MiFIR-D. ESMA calendar: Q2 2024 bond transparency, **CTP**, cost of market data; ESMA tape hearings in mid-Feb. FINRA files **TRACE 15 → 1 minute** | No mention of the JV, two months after it ended |
| 2024-02-13 | EU Regulatory Outlook 2024 | ESMA to deliver draft rules for market data costs, bond transparency and "the consolidated tape regime" |
| 2024-04-03 | Reg brief: MiFIR-D in the Official Journal. Tapes to publish "as close as possible to real time". FINRA to disseminate individual **UST** trades | UST data "available free of charge for non-professional and non-commercial purposes on a next-day basis"; pros buy a subscription. End-of-day file from 2024-03-25, 6-month-delayed historic from 2024-04-01 |
| 2024-06-12 | Reg brief: first ESMA MiFIR 2 consultations — CTP input/output data, "the methodology for the equity CTP to redistribute revenue to data contributors", APA/ARM authorisation, data on a "reasonable commercial basis" | Redistribution is described for the **equity** CTP only |
| 2025-07-01 | Bloomberg Regulatory Data Solutions (Kate Lee et al.): EU makes the market determine bond liquidity | Liquid bonds "expected to jump 20 fold to over 24,000"; liquid = ~88% of trades, 95% of volume. Tapes in EU and UK "from next year". Pitch: updated MiFID data fields via Data License |
| 2025-07-08 | Reg brief: Commission adopts final MiFIR technical rules that "pave the way for the launch of the consolidated tapes in 2026"; FINRA/MSRB move to **rescind** the 1-minute TRACE rule (SEC had approved it Sep 2024) | Redistribution again listed "for shares and ETFs" |
| 2025-10-30 | Reg brief: ESMA transition statement; transparency manual adds a section on CTP input/output data | — |
| 2025-12-01 / 2026-03-02 | UK, then EU, revised bond transparency regimes go live (Tradeweb blogs) | UK bond tape first, "potentially as early as June 2026"; EU regime runs "at least 9 months ahead" of the EU tape (Tradeweb, Dec 2025 / Feb 2026) |
| **2025-12-08** | **BI European Institutional Equity Trading Study** (Nicholas Phillips): 100+ buy-side heads of trading | **28%** would switch to a tape; **24%** favour the EU design (post-trade + L1); **72%** want a pre- and post-trade UK equity tape; **~25%** name a tape as the top reform; **48%** think the EU will ever do a full pre-trade tape. EU equity tape at tender stage "with just one potential provider stepping forward so far". FCA "prioritizing a consolidated tape for fixed income before considering equities" |
| 2026-06-23 | Tradeweb: six months UK / three months EU data | By T+1, "ca. 90% of trades and almost half of the executed notional volume published". Some firms are "waiting for official tape infrastructure before investing more heavily in analytics" |
| 2026-10-13 | Bloomberg TCA piece | "improved post-trade transparency" credited for richer data; still no tape, no JV |

**Context from sibling notes (not from Bloomberg):** MarketAxess launched its own commercial **TraX Tape** on 2026-06-18, built to sit on top of the public CTPs, and cites a planned ESMA bond-tape go-live of Q1 2027 (context, from [[marketaxess-data-cp-plus]]). ICE agreed to acquire MarketAxess on 2026-07-30 (context, from [[marketaxess-hub]]). An LSEG release of 2026-09-11 says LSEG will carry the European **equity** tape operated by EuroCTP (context, LSEG newsroom, not from Bloomberg).

## 2. The arc in three moves

1. **Shape (2022): organise the incumbents, then bid.** APARMA (May) gives the APA operators a lobbying voice; the tape statement (June) follows within 26 days. The pitch has three planks: *expertise in APAs*, *existing infrastructure*, *independent JV*. The first two are the incumbents' assets; the third is the reassurance regulators need to accept them.
2. **Commit, then exit (2023).** The May 2023 signing is the high point: a named leader, a tech vendor picked after a *detailed and rigorous evaluation*, the word "meaningful investment". Seven months later the exit statement gives no number, blames no regulator, names no owner, and adds the UK to the list of things they won't do.
3. **Narrate as a neutral (2024–26).** Bloomberg's Regulatory Affairs and Regulatory Data teams cover every tape milestone as client-facing compliance news and sell data fields for the new regime. BI publishes buy-side scepticism about the (equity) tape. The JV disappears from the record: DELTA confirms zero uses of *tape* in the Aug 2024 brief and the 2025 risk briefs, and no Bloomberg item mentions the JV after Dec 2023.

### What Bloomberg's later briefs cover, and what they leave out

| Brief (date) | Tape-related topics covered | Bloomberg's own bid mentioned? |
|---|---|---|
| Trading and markets, Feb (2024-02-05) | MiFIR-D adoption; ESMA calendar (CTP, cost of market data); ESMA tape hearings for *potential applicants*; TRACE 1-minute filing | No |
| EU Regulatory Outlook (2024-02-13) | Draft rules on market data costs, bond transparency, the tape regime | No |
| Trading and markets, Apr (2024-04-03) | EU-level tapes, near-real-time publication; FINRA next-day UST data | No |
| Trading and markets, Jun (2024-06-12) | CTP input/output data, equity revenue redistribution, APA/ARM authorisation, CTP applicant assessment | No |
| Regulatory Data Solutions (2025-07-01) | Liquid bonds ×20, EU/UK deferral divergence, tapes *from next year*; product pitch | No |
| Trading and markets, Jun (2025-07-08) | Final technical rules, tapes in 2026; TRACE 1-minute rescission | No |
| Trading and markets, Oct (2025-10-30) | ESMA manual section on CTP input/output data | No |
| BI equity study (2025-12-08) | Buy-side demand for tapes; tender with one candidate (equities); FCA bonds first | No |

Eight items, zero mentions. The Feb 2024 brief even reports ESMA's hearing *for potential applicants*, about two months after Bloomberg stopped being one.

### The same JV, seen from three newsrooms

| | Bloomberg | Tradeweb | MarketAxess |
|---|---|---|---|
| Where the exit statement lives | Not on its press page in the corpus | Newsroom, tagged *Regulation* | IR site (context, from [[marketaxess-data-cp-plus]]) |
| What came next | Neutral reg briefs + regulatory data fields; BI survey | Transparency analytics blogs from its MTF/APA data, UK tape *next* ([[tradeweb-derivatives-regulation]]) | TraX Tape, a commercial layer above the public CTPs (context, from [[marketaxess-data-cp-plus]]) |
| Rival named elsewhere? | Never (DIGEST: zero competitor naming across 850 items) | Bloomberg/MKTX appear only as JV partners ([[tradeweb-outside-voices]]) | Same ([[marketaxess-outside-voices]]) |
| Post-exit story | Silence about itself | *Visibility must become usable data* | *Reforms deliver choice, not consolidation* (paraphrase) |

The three converge on one move after the exit: each sells *interpretation* of the public data rather than the data itself. Bloomberg is the only one that never returns to the subject of its own participation.

## 3. What the claims don't prove

1. **'Product definitions' is a reason, not an explanation.** The exit statement gives no cost, timeline, or design detail. It could mean ESMA's bond scope, the deferral regime, revenue rules, or the partners' disagreement with each other. The text cannot separate *regulatory uncertainty* from *three rivals unable to agree*.
2. **'Independent from our respective businesses' was never tested.** A JV owned by the three largest data contributors, selling to the same clients that buy their data, has an obvious conflict. No governance detail (board, pricing, data-access rules) was ever published.
3. **'Cost-effective' and 'fair to contributors and consumers' have no numbers.** No fee, no price for the data inputs, no revenue model. In the briefs Bloomberg itself summarises, ESMA's revenue redistribution is specified for the **equity** CTP; nothing in the corpus says bond contributors get paid.
4. **The BI survey is about equities, not bonds.** 28% / 24% / 72% measure European *equity* traders' views of the *equity* tape. Bloomberg sells direct equity feeds and data; BI's disclaimer says Bloomberg offers products in the areas researched. It is the closest Bloomberg comes to an opinion on tapes, but it cannot be read across to bonds without care.
5. **Silence is evidence only of choice.** The briefs are written by regulatory specialists as neutral roundups. Leaving out the JV may be house style rather than embarrassment. It is still notable that a brief listing the CTP timetable two months after the exit omits that Bloomberg was a would-be applicant.
6. **'Transparency' is in Bloomberg's own boilerplate** (*delivering trusted data, news, and insights that bring transparency, efficiency, and fairness to markets*, live from May 2022). That text ran under all three tape releases. Missions are not evidence of behaviour.

## 4. Strategic read (inference — not stated by Bloomberg)

- **A tape is a public good the incumbents already half-produce.** The APAs publish the prints; each vendor then sells the cleaned, aggregated, enriched view. A single free-or-cheap consolidated feed substitutes for the *bottom* of that stack. The 2022 bid looks like an attempt to make sure the utility was built on, and governed by, the people whose data rents it threatened.
- **Running it was the worse option once the rules were fixed.** A regulated CTP has capped commercial freedom (*reasonable commercial basis*), mandated output, liability for data quality and, for equities, a duty to share revenue. Owning a one-third share of a regulated utility that cannibalises your own enrichment business is a poor trade compared with *contributing, complying and selling the layer above*. MarketAxess's TraX Tape (2026) is the cleanest proof of that path (context, from [[marketaxess-data-cp-plus]]); Bloomberg's equivalent is regulatory data fields via Data License ([[bloomberg-enterprise-data]]).
- **Transparency in counts is not transparency in size.** Tradeweb's 2026 data: ~90% of trades but only ~half of notional visible by T+1. The block-sized information that matters to dealers and price models stays deferred. That residual is where evaluated pricing (BVAL/IBVAL, Ai-Price, CP+) earns its keep ([[bloomberg-pricing-bval-ibval]], [[tradeweb-ai-price]]).
- **Coopetition on rules, war on flow.** Bloomberg co-bid with MarketAxess three months after launching Bridge against Open Trading, and printed MarketAxess's claim to be the *preferred* A2A venue on its own press page. The two activities sit on different layers: rules and utilities (shared) vs execution and pricing (fought over). The boilerplate slip shows how little the firms edited each other's text, not a concession.
- **The exit was jointly staged.** One statement, no blame, *independently committed* to the goal. Bloomberg left the record on Tradeweb's (and MarketAxess's) sites. That limits reputational cost with regulators, who remain each firm's licensor for MTFs and APAs.
- **Next fight: the price of contributor data and the EU/UK split.** Divergent deferral regimes (EU 15 minutes to four weeks; UK one day to three months, per Bloomberg 2025-07-01) create work that only data vendors can package. Divergence is a revenue source, not a problem, for Regulatory Data Solutions.

## 5. Canon lenses

- **Public goods** ([[canon-mankiw-principles-of-economics]]): market data is non-rival and only partly excludable (by delay and licence). Regulators make the delayed version free (FINRA next-day UST data for non-professionals) and leave the real-time version for sale. Free-riding explains why no single firm builds a tape alone and why the state has to tender one.
- **Versioning and lock-in** ([[canon-shapiro-varian-information-rules]]): the tape is a regulator-imposed *low version*. Incumbents respond by moving their paid version up: enriched, de-duplicated, direction-flagged, joined to evaluated prices and workflow.
- **Coopetition / value net** ([[canon-brandenburger-nalebuff-coopetition]]): Bloomberg, MarketAxess and Tradeweb are competitors (Bridge vs Open Trading; IBVAL vs CP+ vs Ai-Price) and complementors (APARMA, the tape). Map who adds value when the tape exists: clients and regulators gain, the incumbents' basic data loses.
- **Commitment and focal points** ([[canon-schelling-strategy-of-conflict]]): a public three-way bid is a signal to ESMA that the incumbents can deliver, which may deter weaker bidders. A jointly worded exit is a coordinated retreat that leaves no one exposed.
- **Five forces** ([[canon-porter-competitive-strategy]]): a tape lowers buyers' information disadvantage and switching costs and gives a new entrant (the CTP) a regulated position in the data value chain. APAs are suppliers to it, with weakened bargaining power if contribution is mandatory and unpaid.
- **Lemons** ([[canon-akerlof-market-for-lemons]]): opaque bond prices favour the better-informed side (dealers, big platforms). A tape narrows the gap, but deferral of large trades keeps the most informative prints private. That is the policy compromise in one sentence.
- **Team production** ([[canon-alchian-demsetz-firm]]): a three-owner JV whose owners compete in the downstream market has a monitoring and shirking problem built in. 'Structural complexities' may be partly this.

## 6. Practitioner counterpoint

- **For the incumbents:** they did have the plumbing. APAs already collect and publish the prints; FINBOURNE was picked after a tender; Tradeweb's data shows the real-time publication jump came from regimes the APAs implemented. Walking away from an undefined, regulated, low-margin mandate is ordinary capital discipline. The BI survey suggests buyers would not pay much for the proposed design anyway (equities: 28% interest).
- **Against:** the bid was framed as a public service and dropped as soon as it stopped being cheap, which is what a public-good problem predicts. Bloomberg's later briefs present the tape as neutral news, without disclosing that it tried to run it. That is a gap a careful reader of Bloomberg's regulatory content should keep in mind.
- **Both:** for a buy-side desk, the practical test is the one Tradeweb names: does the official tape become *usable data*? Compare the tape against a vendor feed on coverage of notional, not trade count, and on latency and duplicates.

## 7. Open questions to track

1. **Who won the EU bond CTP tender, and who runs the UK bond tape?** Neither is stated in the Bloomberg or Tradeweb corpora or in the sibling notes. BI says only that the EU *equity* tender had one candidate (Dec 2025); LSEG names EuroCTP for equities (context). Open.
2. **Go-live dates.** UK bond tape *potentially* June 2026 (Tradeweb, Dec 2025); EU bond tape planned Q1 2027 (context, from [[marketaxess-data-cp-plus]]). Do they ship on time?
3. **Contributor economics.** Do bond APAs (Bloomberg's included) get any revenue share or cost recovery, or only the equity contributors?
4. **Does Bloomberg ever mention its bid?** Watch the next Global Regulatory Briefs and any Bloomberg response to the tape going live.
5. **Does the tape change behaviour?** Track the trade-vs-notional gap (90% vs ~50% at T+1) and whether deferrals shrink in later ESMA/FCA reviews.
6. **Bloomberg's paid layer.** Does Bloomberg launch an enriched tape product (as MarketAxess did with TraX Tape) or keep to data fields, BVAL and TCA?
7. **US analogues.** The TRACE 1-minute rule was approved (Sep 2024) and then moved to rescission (Jul 2025). Does a US push for faster bond data return, and does Bloomberg cover it as neutrally?
8. **Ownership shifts.** With ICE buying MarketAxess and Tradeweb buying Trumid (context, from sibling hubs/corpus, 2026), would a re-formed incumbent bid even be possible?

**Links:** [[bloomberg-hub]] · [[bloomberg-enterprise-data]] (Regulatory Data Solutions, Data License) · [[bloomberg-electronic-trading]] (Bridge) · [[bloomberg-pricing-bval-ibval]] (the price that fills the deferral gap) · [[bloomberg-outside-voices]] · [[bloomberg-terminal-instrumentation]] · [[tradeweb-derivatives-regulation]] (APARMA, UK/EU transparency data) · [[tradeweb-outside-voices]] · [[marketaxess-data-cp-plus]] (TraX Tape, €80bn vs €32bn) · [[marketaxess-open-trading]] · [[ice-fixed-income-data]] (ICE pitching analytics as a substitute for a missing tape) · [[goldman-markets-platforms]] (the dealer view of the EU tape) · [[tradeweb-ai-price]] · [[canon-mankiw-principles-of-economics]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-schelling-strategy-of-conflict]] · [[canon-porter-competitive-strategy]] · [[canon-akerlof-market-for-lemons]] · [[canon-alchian-demsetz-firm]]

---
### Rep
Four short computations with numbers from this note.

**(a) The clock.** Explore 2022-06-22 → sign 2023-05-23 → exit 2023-12-08. How long did each phase last, and how long after Bridge (2022-03-15) did Bloomberg print MarketAxess's *preferred A2A* boilerplate? *(Answer: **335** days to sign, **199** days to exit, **534** days total, about 17.5 months. Bridge → tape release = **99** days.)* In two sentences, say what a 199-day gap between "meaningful investment" and exit suggests about what was learned in that window.

**(b) Count vs size.** Tradeweb: by T+1, ~90% of trades but ~50% of notional are published. What is the average size of an unpublished trade relative to a published one? *(Answer: unpublished = 10% of trades holding 50% of notional, so 0.5/0.1 = 5.0 vs 0.5/0.9 ≈ 0.56 per unit trade; ratio ≈ **9×**.)* Explain why a tape that shows 90% of trades may still leave a block trader reaching for an evaluated price.

**(c) The liquid-bond jump.** Bloomberg (2025-07-01): liquid bonds jump 20-fold to over 24,000, covering ~88% of trades and 95% of volume. How many bonds were liquid before? *(Answer: 24,000 / 20 ≈ **1,200**.)* If the tape publishes liquid-bond trades in near real time and deferral rules hold back large sizes, what is the upper bound on volume the tape can show in real time? *(≤95%, and in practice far less, per (b).)*

**(d) Cannibalisation, hypothetical.** BI: 28% of buy-side desks would consider switching to a tape. Suppose (illustrative assumption, not Bloomberg data) a vendor's European feed line has 100 equal-paying clients, and each switcher cuts feed spend by half. Revenue at risk? *(Answer: 28 × 50% = **14%** of the line.)* Now apply the 24% who like the EU design as the realistic switcher pool: **12%**. Then argue, using [[canon-shapiro-varian-information-rules]], what a vendor would build to win that 12% back.

---
**Sources (accessed via corpus files 2026-10-25):**
- [Bloomberg Bridge launch, 2022-03-15](https://www.bloomberg.com/company/press/bloomberg-launches-global-all-to-all-bond-trading-service/)
- [APARMA launch (Tradeweb newsroom), 2022-05-27](https://www.tradeweb.com/newsroom/media-center/news-releases/apas-and-arms-launch-new-trade-association-aparma/)
- [Explore EU consolidated tape, 2022-06-22](https://www.bloomberg.com/company/press/consolidated-tape/)
- [JV agreement signed, 2023-05-23](https://www.bloomberg.com/company/press/jv-ctp-initiative/)
- [Joint statement ending the JV (Tradeweb newsroom), 2023-12-08](https://www.tradeweb.com/newsroom/media-center/news-releases/statement-from-bloomberg-marketaxess-and-tradeweb-on-joint-venture-agreement/)
- [Global Regulatory Brief: Trading and markets, Feb 2024, 2024-02-05](https://www.bloomberg.com/professional/insights/markets/global-regulatory-brief-trading-and-markets-february-edition-1/)
- [EU Regulatory Outlook 2024, 2024-02-13](https://www.bloomberg.com/professional/insights/regulation/eu-regulatory-outlook-2024/)
- [Global Regulatory Brief: Trading and markets, Apr 2024, 2024-04-03](https://www.bloomberg.com/professional/insights/regulation/global-regulatory-brief-trading-and-markets-april-edition-1/)
- [Global Regulatory Brief: Trading and markets, Jun 2024, 2024-06-12](https://www.bloomberg.com/professional/insights/regulation/global-regulatory-brief-trading-and-markets-june-edition-1/)
- [EU and UK MiFIR/MiFID II reforms: data challenges, 2025-07-01](https://www.bloomberg.com/professional/insights/data/eu-and-uk-mifir-mifid-ii-reforms-navigating-the-upcoming-data-challenges/)
- [June Global Regulatory Brief: Trading and markets, 2025-07-08](https://www.bloomberg.com/professional/insights/regulation/june-global-regulatory-brief-trading-and-markets/)
- [October Global Regulatory Brief: Trading and markets, 2025-10-30](https://www.bloomberg.com/professional/insights/regulation/october-global-regulatory-brief-trading-and-markets/)
- [BI European Institutional Equity Trading Study: Regulation and market structure, 2025-12-08](https://www.bloomberg.com/professional/insights/trading/european-institutional-equity-trading-study-regulation-and-market-structure/)
- [Tradeweb: First look, UK regime week 1, 2025-12-08](https://www.tradeweb.com/newsroom/media-center/insights/blog/first-look-week-1-of-the-uks-new-transparency-regime-calibration/)
- [Tradeweb: Early lessons from the UK regime, 2026-02-19](https://www.tradeweb.com/newsroom/media-center/insights/blog/from-implementation-to-insight-early-lessons-from-the-uks-new-transparency-regime--and-what-comes-next-in-the-eu/)
- [Tradeweb: From dark to light, 2026-06-23](https://www.tradeweb.com/newsroom/media-center/insights/blog/from-dark-to-light-bond-transparencys-next-test/)
- [Bloomberg: Beyond the benchmark (TCA), 2026-10-13](https://www.bloomberg.com/professional/insights/financial-services/beyond-the-benchmark-using-advanced-analytics-to-navigate-fixed-income-trading-costs/)
