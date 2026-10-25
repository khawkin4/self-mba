# Note · Bloomberg private markets — partner, then buy: build the public-to-private bridges in-house, rent the GP feeds and benchmarks, and buy only the LP document network after integrating with it first

> M&A / strategy note · Maps to **E3** (M&A, Deals & Restructuring — staged entry, integration-as-diligence), **E2** (Capital Allocation — build vs buy, real options), **Course 04** (Competitive Strategy — adjacency, coopetition), **Course 07** (Data, Analytics & Decision-Making — sizing denominators, benchmark choice), **Course 02** (Corporate Finance — comps, multiples) · Written 2026-10-25 · Part of [[bloomberg-hub]]; companions [[bloomberg-indices]], [[bloomberg-enterprise-data]], [[bloomberg-buyside-stack]], [[bloomberg-ai-strategy]]

- **Source:** Bloomberg corpus (`_ingest/raw/bloomberg/articles.jsonl`). About **25 items, Oct 15 2024 – Oct 1 2026**, read in full. Deal and product releases: Daphne, Hamilton Lane indices, leveraged loan indices ×2, BDC index article, DLEN, MAC3 privates, Canoe integration, Canoe agreement, Canoe close, CLO data, Clearwater ×2, TOTALFI. Framing pieces: Foster panel (Sep 2025), Phillips/SuperReturn (Jan 2026), BI private credit survey (Oct 2025), Sadiq podcast (Nov 2025), APAC surveys. Context: regulatory briefs (ECB Dec 2024, EO Aug 2025, IMF Nov 2025, APAC Feb 2026, Bank of Canada / FSB Sep 2026) and the Dimensional podcast (May 2025). **Bloomberg is private.** The corpus has no Canoe price, no Canoe revenue and no private-markets revenue line, and this note invents none. Competitor deal terms come from sibling notes and are labeled as such.
- **Core claim:** Bloomberg entered private markets in **three layers, each with a different make-or-buy answer**. (1) **Build** wherever its existing public-markets assets do the work: BVAL-priced leveraged loan indices (Oct 2024, Jul 2025), a BDC bond index (Nov 2025), the DLEN direct-lending database built from BDC filings plus Bloomberg News (**15,000+ loans, ~$1T deal flow**, Apr 2026), MAC3 private-fund risk models (**~50,000 funds**, Apr 2026) and CLO loan-level data (Sep 2026). All of them are keyed to FIGI. (2) **Partner or take a minority stake** for content that GPs own: Daphne (Feb 2025, beside Apollo, Hamilton Lane and Motive) and Hamilton Lane's **20 indices on 7,000+ funds** (Oct 2025). (3) **Buy** the one asset it could not build, which is Canoe's permissioned GP→LP document flow (**500+ clients, $11T AUS, 44,000+ funds, 1.5M documents a month**). It bought only after **112 days** of a live certified integration into PORT Enterprise. The deal was agreed **Jul 29 2026** and closed **Oct 1 2026**, 64 days later, at an undisclosed price. The CEO's own wording (*become a leader*) concedes that Bloomberg is not one yet.

---

## 1. Chronology — the spine

All figures are as Bloomberg states them ("BBG says") unless another source is named.

| Date | Event | Numbers stated |
|---|---|---|
| 2024-10-15 | **US Leveraged Loan Index** (LOAN) plus Syndicated Loans Data Solutions, priced by BVAL | 74,000 active loan tranches. Index: 1,300 loans, $1.3T market value, history from Jan 2019 |
| 2024-11-04 | Brad Foster is still titled *Global Head of Fixed Income Product* (Euroclear ISIN release) | — |
| **2025-02-10** | **Daphne** strategic partnership and investment. Bloomberg joins Apollo, Motive Partners and Hamilton Lane as investors, and a Bloomberg designee takes a board seat. Apollo is the expected first publisher to the Terminal. Foster's new title: *Head of Fixed Income & Private Markets* | Investment size undisclosed. Hamilton Lane: $956B AUM/AUS (Dec 2024) |
| 2025-05-29 | Credit Edge podcast: Dimensional says public HY beats private credit | Dimensional manages $790B |
| 2025-06-06 | BSL primer (index team) | BSLs $2T globally. LOAN +40.58% Jan 2019 – Apr 2025 |
| 2025-07-09 | **Clearwater** partnership: Bloomberg front office plus Clearwater accounting, *open and modular* | Clearwater: $8.8T AUS |
| 2025-07-22 | **European (ELOAN) and Global (GLOAN) loan indices** | GLOAN 1,759 loans, $1.8T. ELOAN 462 loans, €340B. ~100 sub-indices. 82,000+ active loans. US LOAN +43.81% since inception vs US HY +40.59% |
| 2025-08-07 | US executive order on alternatives in 401(k)s (Aug 2025 regulatory brief) | >90M Americans in DC plans |
| 2025-09-10 | Hedge Fund & Alternative Manager Forum: Foster, Apollo's Vanek, McDermott's Koscuiszka | Apollo: direct lending ~$1.7T; with asset-backed and IG it *tops $40 trillion* |
| 2025-10-15 | **BI Private Credit Survey** (140 respondents, Sep 8–22) | Private credit could replace **15%** of BI's addressable fixed income (+5pp vs Apr 2025). 2–5% of the **$12T** DC market. 46% expect a 200bp spread premium |
| 2025-10-22 | TOTALFI index launched to complement the Agg; securitized credit indices promised for 2026 | — |
| **2025-10-29** | **Hamilton Lane private market indices** on the Terminal ({HLNE}) and Data License | **20 indices, 7,000+ funds**, from 2000, quarterly, FIGI-linked. HL $986B AUM/AUS. *Not for use as a financial benchmark* |
| 2025-11-20 | **US BDC Aggregate Eligible Index** (BDCUSAGG) article, co-written by Mark Phillips (*Global Head of Private Credit*) | BDC AUM ~4x since end-2020 to ~$450B. Private credit ~$2T. 33 issuers. +14.32% Jan 2022 – Oct 2025 vs Agg +0.07% |
| 2025-11-27 | BI Asia Private Wealth Survey (100 respondents) | 55% struggle to track illiquid assets. 80% want cross-asset analytics |
| 2026-01-08 | Phillips at SuperReturn: public and private credit *merging* | **$41T** addressable credit market. Private credit could replace up to 15% of it |
| 2026-03-17 | Bloomberg × WatersTechnology APAC survey (50 firms) | 62% plan more private-markets exposure, led by private credit |
| **2026-04-02** | **MAC3 private fund risk models** (PE, private credit, real estate, infrastructure, hedge funds, liquid alts) | ~50,000 private funds. MAC3 has 3,000+ factors and 800+ clients |
| **2026-04-08** | **Canoe certified integration** into PORT Enterprise via SFTP, FIGI as the fund ID. Arizona State Retirement System quoted | PORT Enterprise 800+ clients |
| **2026-04-15** | **DLEN** Private Direct Lending Data | **15,000+** de-duplicated loans, **~$1T** deal flow, all US BDC filings plus News, M&A disclosures and submissions. 6 years of history. One FIGI per loan |
| **2026-07-29** | **Definitive agreement to acquire Canoe**. Kliatchko frames it as a repeat of the Terminal's public-markets play | Canoe: **500+** clients, **$11T+ AUS**, **44,000+ funds**, **1.5M docs a month**. Bloomberg: 3M+ private companies, 50,000 funds, **16,000** direct loans. Price undisclosed. Jefferies advised Canoe |
| 2026-09-22 | NFU Mutual picks Bloomberg plus Clearwater | NFUM ~$32B. Clearwater now *>$10 trillion* and lists *private markets workflows* |
| 2026-09-23 | **CLO Data** (loan-level collateral, FIGI-mapped, ASKB planned) | — |
| 2026-09-28 | Regulatory brief: Bank of Canada on private credit; FSB Chair on leverage and AI | Canada ~$500B exposure: life insurers >$200B (~22% of assets), pensions $215B, funds $54B, bank loans to managers ≥$40B |
| **2026-10-01** | **Canoe acquisition completed**. Canoe is *a translation layer*. ASKB, IBOR and pre-investment screening are promised | 64 days from signing to close |

Elapsed time: Daphne → Hamilton Lane **261 days**; Hamilton Lane → Canoe integration **161**; integration → agreement **112**; agreement → close **64**. Daphne → Canoe close is **598 days**, about 20 months.

## 2. The three layers, and who owns what

| Layer | Make / partner / buy | Asset | Why that choice (stated or *inferred*) |
|---|---|---|---|
| Public windows into private credit | **Build** | LOAN/ELOAN/GLOAN (BVAL-priced), BDCUSAGG, DLEN, CLO data, TOTALFI | Inputs are already in Bloomberg: BDC 10-Q schedules, News, BVAL, FIGI. *Inferred:* marginal cost is low and the index factory is reused ([[bloomberg-indices]], [[bloomberg-pricing-bval-ibval]]) |
| Risk and analytics on privates | **Build** | MAC3 private-fund models, PORT total-portfolio view | Menchero: "risk is often measured in silos". Bloomberg's own fund database (~50,000) supplies the inputs |
| GP-published fund data | **Minority stake + board seat** | Daphne | GPs own the data and choose distributors. Daphne makes Bloomberg one channel among many |
| Benchmarks | **License / distribute** | Hamilton Lane indices | HL owns the LP cash-flow history. The indices are explicitly not financial benchmarks, which keeps BISL's benchmark-administrator duties out of scope (*inferred*) |
| LP-side document extraction | **Buy** | Canoe | A permissioned network of 500+ LPs and 44,000 funds can't be built from public filings |
| Fund accounting / IBOR | **Partner** | Clearwater | Flatman's pitch is against "relying on a single provider that may not meet all their needs". But the Canoe close now promises an *integrated Investment Book of Record across public and private assets* (see §5) |

## 3. How the narrative moved

1. **2024 – early 2025: loans as the bridge.** Private credit enters through syndicated loans, with the classic Bloomberg pitch of *transparency for an opaque asset class*. Foster's retitling, from fixed income product to *Fixed Income & Private Markets*, between Nov 2024 and Feb 2025 is the first organisational signal. Foster: "Private markets is a strategic priority for Bloomberg" (2025-02-10).
2. **Mid-2025: privates are just credit.** Foster says "really the only thing that defines it as private nowadays is the source of capital" (2025-09-10). If that is true, a fixed-income franchise can run private markets, and the org chart follows.
3. **Late 2025: the market is huge.** The size claims escalate: ~$2T private credit (Nov), then Phillips' $41T *addressable* market (Jan 2026), with a BI survey's 15% replacement rate on top. Phillips: "Allocators aren’t running two portfolios anymore."
4. **H1 2026: total portfolio.** MAC3, Canoe→PORT and DLEN arrive in a 13-day window (Apr 2–15). Foster: "Total portfolio management requires interoperability across public and private data".
5. **H2 2026: buy and concede.** Kliatchko: "Today, private markets are primed to undergo a similar transformation". At close: "meaningfully advances our efforts to become a leader in this space". The language moves from *strategic priority* to *defining step*, an admission of catch-up.

## 4. What the claims don't prove

1. **The market size is a moving denominator.** The figures are ~$1T (DLEN deal flow), ~$1.7T (Apollo, direct lending), ~$2T (BDC article, private credit), *tops $40 trillion* (Apollo, adding asset-backed and IG) and $41T (Phillips, *addressable credit*). The 15% replacement rate is a **survey opinion** from 140 people, five points higher than six months earlier. 15% × $41T = ~$6.2T, about 3x the private credit Bloomberg itself cites.
2. **The BDC index comparison uses the wrong base.** "has delivered double digits returns in recent years" is set against the Agg (+0.07%, duration 6.02). The like-for-like index is US Corporate 1–5Y BBB (duration 2.70), which returned +12.51% against BDCUSAGG's +14.32%. Annualized over 3.75 years that is **~3.6% vs ~3.2%**, a gap of about 0.4pp a year, with BDCUSAGG at longer duration (3.09) and ~100bp more yield. The release says so itself, but leads with the Agg.
3. **Loan-count drift.** DLEN had *more than 15,000* loans on Apr 15 and *16,000* on Jul 29. That is either ~1,000 new loans in 105 days or rounding; nothing reconciles it.
4. **Daphne goes quiet.** Daphne appears in Feb 2025 and in a single line in Oct 2025. Neither Canoe release mentions it. No Apollo data on the Terminal is ever reported live, so the first layer's outcome is unknown.
5. **Integration ≠ adoption.** The only integration evidence is a single client quote: ASRS says "This was one of the easiest integrations that our operations team has managed." There is no count of mutual clients, flows or fund records.
6. **Silence on the 2026 private-credit stress.** Goldman's corpus records BDC redemption requests of about 10% unannualized in Q1 2026 against a 5% cap (context, from [[goldman-awm-private-credit]]). Bloomberg launched DLEN, with *non-accrual status* fields, in the middle of that stress, and its releases never mention it.
7. **Hand-picked voices.** The voices quoted are Apollo, Hamilton Lane, Canoe and ASRS, all partners, acquirees or their clients. The independent skeptic is Dimensional's Rizova: "There is no outperformance relative to high-yield public bonds" (2025-05-29). Turetsky (Ares) concedes on fundamentals that "no one’s been able to get the data on large enough scale".
8. **The regulator frame is thinner than it looks.** The Bank of Canada piece does warn on private credit: "transparency is limited, leverage is difficult to measure". The **FSB** item in the same brief warns about frontier-AI cyber risk, leverage in equity markets and leveraged ETFs, **not private credit specifically**. The private-credit stability warnings in the corpus come from the ECB (Dec 2024: banks cannot systematically identify co-lending), the IMF (Oct 2025 GFSR on NBFIs) and ASIC/HKMA (Feb 2026).

## 5. Strategic read (inference — not stated by Bloomberg)

- **Integration-as-diligence.** A 112-day certified integration let Bloomberg test Canoe's data quality, FIGI mapping and client pull on real PORT clients before signing. The seller learned too. Eiswerth: "When we partnered with Bloomberg earlier this year on our PORT integration, we saw firsthand what becomes possible". Information was symmetric, so the integration probably bought **certainty more than a discount**. The 64-day close is consistent with low integration risk and no long antitrust review.
- **Staged real options.** Daphne is a cheap call (minority stake plus board seat). Hamilton Lane is a zero-capital option on benchmark demand. The Canoe integration is an option with information attached, and the acquisition is the exercise. Peers bought outright and early instead (comps in §6).
- **Buy the network, build the dataset.** Bloomberg builds wherever public inputs exist (BDC filings, BVAL loan marks). It buys where the asset is *permissioned relationships*: LPs who route GP documents through Canoe. That mirrors its public-markets history, where Bloomberg built the data and bought distribution only rarely.
- **The GPs are on every side.** Hamilton Lane invested in Daphne, licenses indices to Bloomberg and was a Canoe shareholder paid out by Bloomberg. Goldman Sachs Alternatives, Blackstone and Carlyle AlpInvest backed Canoe. Motive backed Daphne and sold With Intelligence to S&P (context, from [[spglobal-mission-forces]]). *Read:* alternative managers spread their bets across every data rail so that no single vendor controls GP reporting. That limits Bloomberg's pricing power over GPs.
- **The Clearwater tension.** In 2025 the pitch was *we won't build accounting*. Post-Canoe, the pitch is an *integrated IBOR across public and private*, while Clearwater's 2026 boilerplate claims *private markets workflows*. Watch whether this partnership drifts into competition ([[bloomberg-buyside-stack]]).
- **The prize is the reference, as in public markets.** FIGI on every fund and loan, BVAL on loans, Bloomberg indices on loans and BDCs, and ASKB on top. This is the price → index → protocol loop of [[bloomberg-hub]] applied to privates. The missing piece is a *Bloomberg-administered* private-fund benchmark: HL's indices are informational only.

## 6. Comparison: how peers entered private-markets data

| Acquirer → target | When | Terms | Path | Source |
|---|---|---|---|---|
| **Bloomberg → Canoe** | Agreed 2026-07-29, closed 10-01 | Undisclosed, private buyer | Stake (Daphne) → license (HL) → integrate → buy | This corpus |
| BlackRock → Preqin | Jun 2024 → Mar 2025 (246 days) | £2.55B (~$3.2B) cash; ~$240M recurring revenue; ~13x revenue | Bought outright, then plugged into Aladdin | (context, from [[blackrock-private-markets]], [[blackrock-aladdin-data]]) |
| S&P → With Intelligence | Oct 2025 | $1.8B for ~$130M revenue (~14x) | Bought outright from Motive | (context, from [[spglobal-mission-forces]]) |
| LSEG → Octus | Agreed 2026-10-22 | $3.535B cash, debt-funded; >$300M revenue, ~40% margin (~11–12x revenue) | Bought outright, light integration | (context, from [[lseg-capital-allocation]]) |
| Tradeweb → Trumid | Agreed 2026-10-19 | ~$1.97B incl. tax assets | Execution, not data; pairs with LSEG's Octus | (context, from [[ice-marketaxess-deal]], [[lseg-tradeweb-control]]) |
| ICE → MarketAxess | Agreed 2026-07-30, **one day after Canoe** | See sibling note | Venue consolidation | (context, from [[ice-marketaxess-deal]]) |
| Goldman | 2025–26 | Built private credit internally; bought distribution (e.g. T. Rowe stake up to $1B) | Build product, buy channel | (context, from [[goldman-awm-private-credit]]) |

MSCI–Burgiss appears only as a line in [[lseg-capital-allocation]], which says Preqin, Burgiss and With Intelligence all went to rivals. No terms are in any sibling corpus. *Read:* by mid-2026 the large independent private-markets datasets were gone. Canoe was among the last scaled LP-side assets, which helps explain why Bloomberg exercised the option when it did.

## 7. Canon lenses

- **Make vs buy / the firm's boundary** ([[canon-alchian-demsetz-firm]]): Bloomberg internalises what it can meter and monitor itself (index rules, BVAL marks, FIGI). It buys only where team production depends on outside relationships (Canoe's LP community).
- **Staged bets** ([[canon-duke-thinking-in-bets]], [[canon-taleb-antifragile]]): each step is small and reversible until the last one. The integration converted uncertainty about the deal into risk that could be priced.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Hamilton Lane, Apollo and Clearwater are each supplier, complementor and potential rival. Their *added value* sets how much Bloomberg can capture.
- **Standards and lock-in** ([[canon-shapiro-varian-information-rules]]): FIGI is open but Bloomberg-administered. Making it the private-fund key ties privates to Bloomberg's security master without a closed standard.
- **7 Powers** ([[canon-helmer-7-powers]]): Canoe is a *cornered resource* (permissioned document flows) and creates *switching costs* once LP reporting cycles run through PORT.
- **Lemons and appraisal marks** ([[canon-akerlof-market-for-lemons]]): GP-reported, appraisal-based data is the input. Better plumbing does not fix biased marks, which is Dimensional's and Turetsky's point.
- **Margin of safety** ([[canon-klarman-margin-of-safety]]): an undisclosed price means outsiders can't judge it, and the peer comps of 11–14x revenue were set at a cyclical high.

## 8. Practitioner counterpoint

- **For Bloomberg:** the sequence is disciplined. It spent little until it had live evidence, built what its data already supported, and closed fast. The pieces interlock: DLEN feeds FIW/YAS, Canoe feeds PORT and MAC3, and everything is FIGI-keyed. That combination is hard for a single-asset rival to copy. BI's own surveys (55% struggle to track illiquid assets, 80% want cross-asset analytics, 62% of APAC firms adding privates) suggest real demand, even though they are vendor surveys.
- **Against:** Bloomberg is late. BlackRock (Preqin in Aladdin), S&P, LSEG and MSCI hold scaled datasets, and the GPs deliberately multi-home. Bloomberg's strength, public-markets transparency, assumes that privates *want* to be marked like publics. Many LPs value the smoothing (Turetsky on vol). And the retail and 401(k) tailwind (BI: 2–5% of $12T) arrives with the scrutiny Koscuiszka predicted: "back-to-basics with private credit, with a focus on disclosures, valuation, and AI".
- **Both:** an allocator evaluating the stack should test whether Canoe→PORT data reconciles with GP capital-account statements, quarter by quarter, before trusting MAC3 private-fund risk numbers.

## 9. Open questions to track

1. **Canoe price and revenue.** Any leak, or Canoe headcount and client counts in 2027 releases?
2. **Daphne.** Is it folded in, written off or left dormant? Does Apollo data ever go live on the Terminal?
3. **A Bloomberg private-fund benchmark.** Will BISL administer one (HL or Canoe-derived), or stay *informational only*?
4. **Clearwater.** Does the IBOR promise lead to overlap, a deeper partnership or a split?
5. **DLEN through stress.** Do non-accrual and PIK fields show the 2026 BDC stress, and does Bloomberg publish on it?
6. **ASKB on privates.** When does permissioned Canoe data reach ASKB, and how are GP/LP entitlements enforced ([[bloomberg-ai-strategy]])?
7. **Securitized indices** promised for 2026 with TOTALFI: do they ship, and do they include private ABF?
8. **Exits by GP backers.** Do Goldman Sachs Alternatives, Blackstone and Hamilton Lane, now paid out, keep routing data through Canoe on neutral terms?

**Links:** [[bloomberg-hub]] · [[bloomberg-indices]] (LOAN, BDCUSAGG, TOTALFI) · [[bloomberg-pricing-bval-ibval]] (BVAL on loans) · [[bloomberg-enterprise-data]] (Data License, FIGI) · [[bloomberg-buyside-stack]] (PORT, MAC3, Clearwater) · [[bloomberg-ai-strategy]] (ASKB) · [[bloomberg-people]] · [[bloomberg-outside-voices]] · [[bloomberg-mission-forces]] · [[bloomberg-terminal-instrumentation]] · [[blackrock-private-markets]] · [[blackrock-aladdin-data]] · [[goldman-awm-private-credit]] · [[lseg-capital-allocation]] · [[lseg-tradeweb-control]] · [[ice-marketaxess-deal]] · [[spglobal-mission-forces]] · [[tradeweb-credit]] · [[wss-private-markets-wealth]] · [[wss-credit-distressed]] · [[canon-alchian-demsetz-firm]] · [[canon-duke-thinking-in-bets]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]]

---
### Rep
Three computations. Bloomberg-stated numbers are marked BBG. Everything else is a labeled assumption.

**(a) Canoe unit economics and a price bracket.** BBG: 500+ clients, $11T AUS, 44,000 funds, 1.5M documents a month. Compute AUS per client, documents per fund per month and documents per client per month. *(Answer: $22B; ~34; ~3,000.)* The price is undisclosed. **Assume** revenue per client of $100k–$300k, so revenue is $50–150M. Apply the peer range of ~11x (Octus) to ~14x (With Intelligence) revenue. *(Answer: ~$0.55B to ~$2.1B.)* Explain why a 2026 private buyer with no public multiple to protect might pay less than BlackRock's 13x, or more.

**(b) Integration as a real option (hypothetical values).** Canoe is worth V = $1.5B to Bloomberg if integration proves out (p = 0.6), and $0.6B if not. Ask price P = $1.2B. (i) Buying blind: EV = 0.6×1.5 + 0.4×0.6 − 1.2 = **−$0.06B**. (ii) Integrate first at cost $10M, then buy only in the good state: 0.6×(1.5 − 1.2) − 0.01 = **+$0.17B**. The value of information is ≈ $0.17B. (iii) Now the seller also learns, and the price rises to $1.4B in the good state: 0.6×0.1 − 0.01 = **+$0.05B**. Use Eiswerth's quote to argue which case 2026 looked like, and how Daphne and Hamilton Lane fit as cheaper options earlier in the tree.

**(c) Grade the BDC index claim.** BBG: BDCUSAGG +14.32%, US Agg +0.07%, US Corp 1–5Y BBB +12.51%, Jan 2022 – Oct 2025 (3.75 years). Durations are 3.09 / 6.02 / 2.70, and yield to worst is 5.41% / 4.33% / 4.44%. Annualize each. *(Answer: ~3.6%, ~0.0%, ~3.2%.)* Which comparator is fair? How much of the ~0.4pp a year gap could ~0.97% more yield and 0.39 more duration explain? Then size Phillips' claim: 15% of $41T vs ~$2T of private credit today. *(≈ $6.2T, ~3x.)* Write one sentence on what evidence would make that forecast credible.

---
**Sources (Bloomberg corpus, `_ingest/raw/bloomberg/articles.jsonl`, read 2026-10-25):**
- [US Leveraged Loan Index, 2024-10-15](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-accelerates-its-presence-in-loans-market-with-launch-of-a-new-leveraged-loan-index-based-on-new-syndicated-loans-data-and-pricing-solution/)
- [Regulatory brief: ECB on PE/PC exposures, 2024-12-16](https://www.bloomberg.com/professional/insights/regulation/december-global-regulatory-brief-risk-capital-and-financial-stability/)
- [Daphne partnership and investment, 2025-02-10](https://www.bloomberg.com/company/press/bloomberg-and-daphne-partner-to-streamline-access-to-reliable-private-markets-data/)
- [Dimensional on private vs public HY, 2025-05-29](https://www.bloomberg.com/professional/insights/markets/dimensional-says-public-debt-has-the-edge-over-private/)
- [Broadly syndicated loans primer, 2025-06-06](https://www.bloomberg.com/professional/insights/markets/broadly-syndicated-loans-market-size-structure-and-historical-return-profile/)
- [Clearwater partnership, 2025-07-09](https://www.bloomberg.com/company/press/bloomberg-and-clearwater-analytics-partner-to-optimize-investment-management-workflows/)
- [European and Global loan indices, 2025-07-22](https://www.bloomberg.com/company/press/bloomberg-broadens-leveraged-loan-indices-and-data-solutions-to-european-and-global-markets/)
- [Regulatory brief: 401(k) EO, 2025-08-28](https://www.bloomberg.com/professional/insights/regulation/august-global-regulatory-brief-risk-capital-and-financial-stability/)
- [Private credit panel (Foster, Vanek, Koscuiszka), 2025-09-10](https://www.bloomberg.com/professional/insights/financial-services/a-changing-landscape-for-private-credit/)
- [BI Private Credit Survey, 2025-10-15](https://www.bloomberg.com/company/press/private-credit-could-replace-15-of-traditional-fixed-income-as-asset-class-rides-tailwinds-according-to-bloomberg-intelligence-survey/)
- [TOTALFI launch, 2025-10-22](https://www.bloomberg.com/company/press/bloomberg-indices-launches-bloomberg-us-total-fixed-income-market-index-to-capture-the-full-investable-us-fixed-income-universe/)
- [Hamilton Lane indices on Terminal, 2025-10-29](https://www.bloomberg.com/company/press/bloomberg-adds-hamilton-lane-private-market-indices-to-the-bloomberg-terminal/)
- [Private market data at scale (Sadiq podcast), 2025-11-04](https://www.bloomberg.com/professional/insights/data/how-companies-integrate-private-market-data-at-scale/)
- [BDC-issued debt index, 2025-11-20](https://www.bloomberg.com/professional/insights/markets/bdc-issued-debt-a-public-window-into-private-credit-issuers/)
- [Regulatory brief: IMF on NBFIs, 2025-11-25](https://www.bloomberg.com/professional/insights/regulation/november-global-regulatory-brief-risk-capital-and-financial-stability-2/)
- [Asia private wealth integration gap, 2025-11-27](https://www.bloomberg.com/professional/insights/financial-services/the-integration-gap-can-your-tech-keep-up-with-asias-private-wealth-boom/)
- [$41T credit market (Phillips), 2026-01-08](https://www.bloomberg.com/professional/insights/markets/41-trillion-credit-market-how-is-private-credit-reshaping-the-landscape/)
- [APAC Regulatory Outlook, 2026-02-02](https://www.bloomberg.com/professional/insights/regulation/apac-regulatory-outlook-2026/)
- [APAC buy-side survey, 2026-03-17](https://www.bloomberg.com/professional/insights/artificial-intelligence/apac-buy-side-firms-embrace-ai-automation-to-optimize-business-processes/)
- [MAC3 private-asset models, 2026-04-02](https://www.prnewswire.com/news-releases/bloomberg-expands-mac3-risk-models-for-enhanced-portfolio-and-risk-forecasting-across-public-and-private-investments-302732596.html)
- [Canoe integration, 2026-04-08](https://www.bloomberg.com/company/press/canoe-intelligence-and-bloomberg-launch-integration-to-automate-private-fund-data-delivery-supporting-a-total-portfolio-view/)
- [DLEN direct lending data, 2026-04-15](https://www.prnewswire.com/news-releases/bloomberg-introduces-comprehensive-private-direct-lending-data-for-deeper-private-credit-market-insights-302742628.html)
- [Canoe acquisition agreed, 2026-07-29](https://www.prnewswire.com/news-releases/bloomberg-to-acquire-canoe-intelligence-taking-a-defining-step-in-its-mission-to-transform-private-markets-investing-302837466.html)
- [NFU Mutual / Clearwater, 2026-09-22](https://www.prnewswire.com/news-releases/nfu-mutual-selects-bloomberg-and-clearwater-analytics-for-front-to-back-investment-management-workflow-302885834.html)
- [CLO Data, 2026-09-23](https://www.prnewswire.com/news-releases/bloomberg-launches-comprehensive-clo-reference-data-solution-connecting-insights-across-the-investment-lifecycle-302886975.html)
- [Regulatory brief: Bank of Canada, FSB, 2026-09-28](https://www.bloomberg.com/professional/insights/regulation/september-2026-global-regulatory-brief-private-credit-credit-risk-reform-and-liquidity-reporting/)
- [Canoe acquisition completed, 2026-10-01](https://www.bloomberg.com/company/press/bloomberg-completes-canoe-intelligence-acquisition-advancing-strategy-to-transform-private-markets-investing/)
