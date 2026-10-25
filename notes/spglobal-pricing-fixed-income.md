# Note · S&P Global pricing, reference data & fixed-income plumbing — an evaluator that rents other people's prices; the real moats are the identifiers and the indices

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — complements, standards, coopetition with venues), **Course 06** (Operations — settlement, loan administration, straight-through processing), **Course 07** (Data, Analytics & Decision-Making — what a "price" is, coverage denominators), **E10** (Digital & AI Transformation — data plumbing as the AI substrate) · Written 2026-10-25 · Part of [[spglobal-hub]]; companions [[tradeweb-ai-price]] (§5 is the base layer for this note), [[spglobal-ai-data-layer]], [[spglobal-ihs-markit-merger]]

- **Source:** S&P Global press and IR releases in `_ingest/raw/spglobal/articles.jsonl`, specifically about 35 items on pricing, reference data, identifiers, loans and primary markets, dated Jan 2021 to Oct 2026, plus the Investor Day 2022 and 2025 decks. One Tradeweb release (2022-09-29) comes from `_ingest/raw/tradeweb/articles-2019-2026.jsonl`. **[[tradeweb-ai-price]] §5 already covers** the IHS Markit pricing inheritance, liquidity scores, PriceViewer, the method contrast with Ai-Price, and the first read of the CP+ deal. This note does not repeat those points. It adds the timeline, the coverage numbers, the inputs, identifiers, plumbing and organisation that §5 does not cover.
- **Core claim:** S&P's evaluated-pricing business is mainly an **aggregator of other firms' prices**:
  - dealer contributions (Barclays signed up in 2025),
  - parsed quotes and composites (loans),
  - since Oct 2024, a venue's AI price feed, MarketAxess **CP+**.

  It is sold mainly as **regulatory evidence**: SEC Rule 2a-5 diligence, fair-value support and a challenge trail. S&P's own coverage figures conflict from one release to the next.

  In **July 2026** S&P filed "pricing and reference data" under **Enterprise Solutions**. That treats pricing as infrastructure inside a loan-and-software vertical, not as a growth product.

  The durable assets in fixed income are elsewhere:
  - **identifiers**: S&P had to sell **CUSIP** to FactSet in 2021–22 and now pushes **LXIDs** and a free **CIQ ID**;
  - **workflow plumbing**: ClearPar, WSO, Debtdomain, InvestorAccess;
  - the **indices** that derivatives reference: **iBoxx, CDX, iTraxx**.

  Since ICE agreed to buy MarketAxess (Jul 2026), S&P has said nothing in public about CP+.

---

## 1. Chronology

| Date | Event | Numbers / words stated |
|---|---|---|
| 2021-01-19 | CUSIP accreditation renewed by ANSI X9 | "more than 62.8 million CUSIP identifiers" assigned; at least 9.4M active |
| **2021-12-27** | Merger remedy: **CUSIP Global Services → FactSet** for **$1.925B**. Base Chemicals → News Corp for $295M | ~$1.3B aggregate net proceeds, "net of taxes and payments to CGS's industry partner" |
| 2022-03-01 | CUSIP sale to FactSet completed | — |
| 2022-04-04 | LCD and leveraged-loan indices → Morningstar ($650M; an EC condition) | S&P exits loan news and indices for now (see [[spglobal-ihs-markit-merger]]) |
| 2022-07-14 | **PVR Source** for **SEC Rule 2a-5** fair-value vendor diligence | Methodology documents, back-testing, "aggregated challenge statistics" |
| 2022-09-29 | **Tradeweb integrates InvestorAccess** (European credit, covered and SSA primary) | Tradeweb corpus. Orders go into the syndicate's book and allocations come back |
| 2022-12-01 | Investor Day 2022 lists **CDX, iBoxx, iTraxx, ClearPar** among "Our Strengths"; MI prices "2.5M+" FI instruments daily | "ETD and CDS fees correlate with volatility" |
| 2023 | *Pricing, Valuations and Reference Data (MI)* named a key contributor to Vitality (new-product) revenue | 2024 AGM slides |
| 2023-04-04 | Equity InvestorAccess (equity primary orders and allocations) | — |
| 2023-06-20 | FI ETF distribution forecasts built on Evaluated Bond Pricing | EBP gives "daily prices on 2.3 million" government, sovereign, corporate, securitized and municipal instruments |
| **2023-06-22** | **Bloomberg TSOX ↔ InvestorAccess** for syndicated primary bonds | The main desktop rival becomes a distribution partner |
| 2023-06-28 | Loan pricing, analytics and liquidity scores added to Capital IQ Pro | "High-quality and independent pricing across a wide range of fixed income classes is in elevated demand," (Breakstone) |
| 2024-03-13 | Onboarding Accelerator ↔ **DTCC ALERT** (settlement instructions) for **T+1** | — |
| 2024-06-18 | Bond Reference Data adds sustainability fields | Reference data "powers intraday and end of day pricing on 2.9 million active global securities" |
| 2024-06-20 | Capital IQ Pro adds "more than 19.4 million" FI securities | Desktop distribution of IHS Markit content |
| **2024-07-09** | **Evaluated Loan Pricing**: 8,000+ leveraged loans; one price per loan "be it composite or evaluated" | 400,000+ identifiers mapped; 20+ years of history |
| 2024-10-10 | Lending suite statistics | "more than 32,000 active loans", "460 billion USD" private debt tracked, "more than 1 trillion USD" serviced |
| **2024-10-31** | **MarketAxess partnership**: CP+ (two-sided, every 15–60s) goes into Evaluated Bond Pricing; S&P Bond Reference Data goes into MarketAxess products | EBP described as "over 1.2 million Corporate, Sovereign and Municipal bonds". Integration "expected to start in the first half of 2025" |
| 2024-11-01 | PrimeOne (IHS Markit) sold to TS Imagine | Terms undisclosed |
| 2025-01-07 | 4.6M munis added to Capital IQ Pro, about 6M in total; "over 26 million" FI securities | Includes liquidity scores and end-of-day pricing |
| **2025-06-24** | **LXIDs extended to private credit** | "over 70,000 existing LXIDs" |
| **2025-07-23** | **Barclays** enterprise deal: Barclays "will contribute its data to S&P Global's cross-asset pricing and valuation services" | Bonds, loans, credit and derivatives |
| **2025-09-11** | **CIQ IDs published free on DUNL.org** | "over 25 million company records"; Creative Commons |
| 2025-10-10 | **OSTTRA sold to KKR** ($3.1B EV, 50/50 with CME) | Post-trade exit (MarkitWire; see §5) |
| 2025-10-22 | Capital IQ Pro adds "nearly 3,600 new issuers" to CDS coverage | — |
| 2025-11-13 | Investor Day 2025: planned new MI business line **Risk & Valuations Services** to hold *Pricing (Bond/CDS/Loan)* and *Valuations and Reference Data* after the Mobility spin | Pricing grouped with front-office tools |
| 2025-11-20 | WSO Compliance Insights for private credit and CLO managers | — |
| 2026-01-12 | EDM and thinkFolio (Markit enterprise data and buy-side OMS) sold to STG | Software pruning |
| 2026-03-03 | **DataXchange and AmendX** for loan agents, integrated with Debtdomain | "agents are still managing billion-dollar deals with Excel and email, creating massive operational risk," (Darren Thomas) |
| 2026-03-12 | "over 4 million structured securities" added to Capital IQ Pro | — |
| **2026-07-06** | **MI reorganisation**: "Pricing and reference data, including consensus pricing and valuation methodologies across public and private markets, will be part of Enterprise Solutions" | **Reverses the Nov 2025 plan** to put pricing in Risk & Valuations Services. Enterprise Solutions has "a focus on the most differentiated software assets" |
| 2026-07-16 | ETF Intelligence (15,000+ ETFs) | Paul Wilson, *Head of Data, Pricing, Valuations & Analytics* |
| 2026-07-30 | (context, from the [[ice-hub]] sibling note) **ICE agrees to buy MarketAxess** | **No S&P release mentions it, or CP+, afterwards** |
| 2026-10-13 | Tokenized **iBoxx USD Liquid IG** TRS on Canton | See [[spglobal-digital-assets]] |

## 2. The coverage numbers do not reconcile

| Release | Figure | What it counts |
|---|---|---|
| Investor Day 2022 / 2025 | "2.5M+" | FI instruments "priced daily" |
| 2023-06-20 | 2.3M | EBP daily prices across government, sovereign, corporate, securitized and municipal |
| 2024-06-18 | 2.9M | Securities whose *reference data* powers intraday and end-of-day pricing |
| 2024-10-31 | 1.2M+ | EBP corporate, sovereign and municipal bonds only |
| 2024-06 → 2025-01 | 19.4M added → 26M+ | Securities with reference *and* pricing data on Capital IQ Pro (desktop coverage) |
| [[tradeweb-ai-price]] §5 | 86,500+ corporates on 4M+ price observations (2022 data sheet) | Corporate bonds with an evaluated price |

*Reading (inference):* these are different universes. One counts instruments with any daily price, one counts corporates with an evaluation backed by observations, and one counts anything with a terms-and-conditions record. The trouble is that S&P never says which is which. A buyer comparing S&P with ICE or Bloomberg BVAL coverage should ask for **corporates with an observation-backed price on a given day**, not the headline number.

## 3. Where the prices come from

1. **Dealer contributions and parsed quotes.** The loan engine is "Built based on contributor-based loan pricing engines, sophisticated parsing technology, and supplemented with an evaluated methodology" (2024-07-09). Barclays now contributes for bonds, loans, credit and derivatives (2025-07-23).
2. **A venue's model price.** MarketAxess CP+ is "powered by AI and proprietary data", including MarketAxess's trading platform and TraX data (2024-10-31). Its own head of data, Kat Sweeney, said CP+ inside EBP would "close the gaps between best execution, intraday trading decisions and end-of-day valuation,".
3. **S&P's own evaluators and methodology.** These are documented for auditors through PVR Source: "clients want a detailed understanding of processes and methodologies used by vendors for fair value pricing." (Shetty, 2022).

S&P owns the methodology, the client relationship and the audit trail. It does **not** own a trade tape. Tradeweb (Ai-Price on its own flow), ICE (an evaluator plus, once the deal closes, MarketAxess) and Bloomberg (BVAL plus its terminal flow) each own one of the inputs that S&P rents.

## 4. Identifiers: the moat S&P lost, and the ones it is building

- **Lost:** CUSIP, the US identifier standard, was sold to FactSet as a merger remedy. In Jan 2021 S&P was celebrating its accreditation. In Dec 2021 Peterson called the sale "an important milestone in our progress toward satisfying the required regulatory conditions". See [[spglobal-ihs-markit-merger]].
- **Building:**
  - **LXIDs** for loans, now for private credit. Saha: "The expansion of private credit and the emergence of secondary trading necessitates common identifiers,".
  - The **CIQ ID** made free on DUNL.org, to make it "the standard company identifier for all S&P Global data".
- *Inference:* giving the key away is how you make S&P's paid data the easiest data to join to. LSEG's PermID and Bloomberg's FIGI play the same game ([[lseg-hub]], [[bloomberg-hub]]). It also feeds the AI strategy, because entity-linked data is what makes LLM answers verifiable ([[spglobal-ai-data-layer]]).

## 5. Plumbing: S&P connects to every venue rather than being one

- **Primary markets.** InvestorAccess and Equity Bookbuild (from IHS Markit's Ipreo) connect to **Tradeweb** (2022) and to **Bloomberg TSOX** (2023). Tradeweb's release quotes S&P's Chris Sztam: "Buy-side traders using Tradeweb are now able to send orders electronically into the orderbook being managed by the syndicate banks". S&P sits underneath the venues, not beside them.
- **Loans.** ClearPar settlement, WSO portfolio administration, Debtdomain, and the 2026 DataXchange/AmendX for agents. This is middle- and back-office software for the leveraged-loan and private-credit market.
- **Settlement.** The DTCC ALERT link for T+1 (2024). Brittany Garland: "It will streamline a manual, antiquated process, maximizing efficiency and minimizing trade settlement failures,".
- **Post-trade derivatives: exited.** OSTTRA (MarkitWire, the CME JV) was sold to KKR in Oct 2025. Tradeweb's 2026 electronic swaption and bilateral IRS terminations still confirm on MarkitWire ([[tradeweb-derivatives-regulation]]). Tradeweb's new bilateral business therefore depends on infrastructure that S&P built and then sold.

## 6. The real moat: indices that derivatives reference

- From Investor Day 2022: "Our indices underlie the most liquid financial products in the market for both equity and credit". **CDX and iTraxx** carry the CDS index market. **iBoxx** underlies bond ETFs, iBoxx futures and TRS.
- The same deck says these fees are counter-cyclical: "ETD and CDS fees correlate with volatility". An evaluator earns from calm, recurring subscriptions. An index owner also earns from turmoil.
- iBoxx keeps getting extended:
  - TRS on Tradeweb's SEF (2021, Tradeweb corpus).
  - The iBoxx USD Leveraged Loan Indices folded into the **S&P UBS Leveraged Loan Indices** (Dec 2024).
  - A **tokenized iBoxx TRS** on Canton (Oct 2026; [[spglobal-digital-assets]]).
- *Inference:* a trade-driven AI price (Ai-Price, CP+) is a direct threat to the evaluator. It is no threat to the index licence. That is why §5 of [[tradeweb-ai-price]] places S&P's credit moat in index royalties, and the 2026 placement of pricing under Enterprise Solutions is consistent with that view.

## 7. What the claims don't prove

1. **"Independent" pricing that relies on outside inputs.** S&P calls its pricing "independent", yet it now takes a venue's AI price and a dealer's contributed data. "Independent" here means *not the client's own mark*, not *free of input dependence*.
2. **No accuracy evidence.** No release gives back-test error, how often prices are challenged, or how much CP+ improved EBP. PVR Source hosts "back testing reports", but only for clients.
3. **The CP+ result was never reported.** Integration was "expected to start in the first half of 2025". No later release says it went live, what changed, or whether the partnership is exclusive (the "exclusive access" wording in [[tradeweb-ai-price]] §5 comes from a 2025 S&P web page outside this corpus).
4. **The org chart changed its mind.** Investor Day 2025 planned a front-office *Risk & Valuations Services* line for pricing. Eight months later pricing sits in *Enterprise Solutions*. The corpus does not explain the switch.
5. **Coverage numbers** (§2) cannot be compared across releases.

## 8. Strategic read (inference — not stated by S&P Global)

- **ICE–MarketAxess puts S&P's main corporate-bond price input in a competitor's hands.** ICE runs a large evaluated-pricing business ([[ice-hub]]). Once MarketAxess closes (H1 2027), S&P's CP+ feed comes from its largest pricing rival. S&P's options:
  1. renegotiate;
  2. lean harder on dealer contributions (the Barclays model, scaled to more banks);
  3. license Tradeweb's Ai-Price, though Tradeweb's benchmark partner is FTSE Russell/LSEG;
  4. buy or build a trade-derived price;
  5. accept being a methodology-and-audit wrapper around other firms' prices.

  The 2025 Barclays deal looks like a hedge toward option 2.
- **The pricing move is a demotion, and probably a sensible one.** Inside Enterprise Solutions, pricing feeds ClearPar, WSO, iLEVEL and the loan tools. That is where clients need a mark every day (loan administration, CLO compliance, private-credit valuation), and where a venue's AI price is least available. Private credit has no TRACE and no CP+, so S&P's composite-plus-evaluated method has no trade-driven rival there.
- **Private credit is the battleground that suits S&P.** LXIDs, DataXchange/AmendX, WSO Compliance Insights, iLEVEL, With Intelligence ([[spglobal-strategy-financials]]) and S&P Lincoln indices (DJI) all point the same way. In private credit, the identifier, the agent's records and the valuation mark are all still being invented.

## 9. Canon lenses

- **Complements and commoditising them** ([[canon-shapiro-varian-information-rules]]): S&P gives away the identifier (CIQ ID), the complement, so its priced data is easier to use. Venues do the reverse: they make prices cheap and keep the flow.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Bloomberg (TSOX), Tradeweb (InvestorAccess), MarketAxess (CP+) and ICE (Brent, through Platts) are all partners on one product and rivals on another. S&P's value depends on staying the neutral connector.
- **Power** ([[canon-helmer-7-powers]]): *switching costs* in loan administration and fair-value audit trails; *cornered resource* in CDX/iTraxx/iBoxx index IP. Evaluated pricing alone has weak power because its inputs are rented.
- **Bottlenecks** ([[canon-goldratt-the-goal]]): in loan markets the constraint is settlement and agent administration ("Excel and email"), not price discovery. S&P is investing where the constraint is.
- **Five forces** ([[canon-porter-competitive-strategy]]): supplier power rises sharply when the price input (MarketAxess) is bought by a rival (ICE).

## 10. Practitioner counterpoint

- **For S&P:** fund administrators, valuation committees and auditors care about a defensible, documented, challengeable price more than about the "best" intraday predictor. Most fixed-income securities trade rarely. For them an evaluated price with a challenge process *is* the product. S&P's IHS Markit heritage (Markit loan pricing, iBoxx dealer pricing) is deep, and the private-credit tools have few equals.
- **Against:** in liquid IG and HY, trade-driven prices (Ai-Price, CP+, BVAL fed by terminal flow) are converging on the venues. An evaluator without a tape is squeezed between venues that sell prices cheaply and a rival evaluator (ICE) that is about to own one of the best feeds.
- **Both:** a buyer should ask S&P for the share of daily evaluations backed by an observation, the median challenge rate, and what happens to the CP+ input if ICE ends the contract.

## 11. Open questions to track

1. Did CP+ integration ever go live, and is it exclusive? What does the contract say about change of control at MarketAxess ([[marketaxess-hub]])?
2. After the deal closes, does ICE offer CP+ to S&P on the same terms, or bundle it with ICE Data Services?
3. How many more dealers sign Barclays-style contribution deals?
4. What is the revenue of *Pricing (Bond/CDS/Loan)*? It has never been disclosed. Does the recast segment reporting (Jul 2026) reveal Enterprise Solutions revenue?
5. Do LXIDs become the market standard for private credit, or does a CUSIP-style utility (now owned by FactSet) win?
6. Will S&P ever license Tradeweb's Ai-Price ([[tradeweb-ai-price]]), or is the FTSE Russell/LSEG tie-up exclusive in effect?

**Links:** [[spglobal-hub]] · [[tradeweb-ai-price]] (§5 is the base layer) · [[spglobal-ai-data-layer]] · [[spglobal-ihs-markit-merger]] (CUSIP, LCD, OSTTRA disposals) · [[spglobal-digital-assets]] (tokenized iBoxx) · [[spglobal-indices-benchmarks]] · [[spglobal-strategy-financials]] · [[tradeweb-credit]] · [[tradeweb-derivatives-regulation]] (MarkitWire) · [[marketaxess-hub]] · [[ice-hub]] · [[bloomberg-hub]] · [[lseg-hub]] · [[wss-credit-distressed]] · [[market-structure-24-5-trading]] · [[canon-shapiro-varian-information-rules]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-helmer-7-powers]] · [[canon-goldratt-the-goal]] · [[canon-porter-competitive-strategy]]

---
### Rep
Three short computations with numbers from this note.

**(a) Reconcile the coverage.** EBP prices 2.3M instruments across government, sovereign, corporate, securitized and municipal (2023). The MarketAxess release says 1.2M+ corporate, sovereign and municipal (2024). *Assume* both are on the same basis. How many instruments are government, agency or securitized? What share of EBP does CP+ (credit, rates and EM only) touch at most? *(Answer: about **1.1M** outside the corporate/sovereign/muni set. CP+ touches at most the 1.2M, about **52%**. Corporates alone, at ~86,500 per [[tradeweb-ai-price]] §5, are about **4%** of 2.3M. That is the slice where CP+ matters most and where TRACE gives observations.)*

**(b) The cost of the CUSIP remedy.** Gross proceeds were CGS $1.925B + Base Chemicals $295M. S&P expected about $1.3B net "of taxes and payments to CGS's industry partner". How much leaked to tax and the partner (the ABA), and what share of gross is that? *(Answer: $2.22B − $1.3B = **~$0.92B**, about **41%**.)* In one paragraph: why might losing CUSIP cost more than the $0.92B? Think about lock-in on identifiers versus a one-off sale price.

**(c) Price frequency.** CP+ updates every 15–60 seconds. [[tradeweb-ai-price]] §5 says EBP publishes seven regional snapshots a day. Over a 6.5-hour US session, how many CP+ updates is that per bond, and how many per EBP snapshot? *(Answer: 390–1,560 updates; with ~7 snapshots, **~56–223 CP+ ticks per snapshot**.)* Then argue which client needs which: an auditor of a fund's NAV, an algo trading desk, a CLO manager running daily compliance tests.

---
**Sources (S&P Global press/IR unless noted; accessed 2026-10-25):**
- [CUSIP accreditation, 2021-01-19](https://press.spglobal.com/2021-01-19-CUSIP-Global-Services-Receives-Accreditation-Renewal-for-CUSIP-Identifier-as-U-S-Standard-for-Unique-Security-Identification)
- [CUSIP / Base Chemicals sale agreements, 2021-12-27](https://investor.spglobal.com/news-releases/news-details/2021/SP-Global-and-IHS-Markit-Announce-Agreements-to-Sell-Base-Chemicals-and-CUSIP-Businesses/default.aspx)
- [CUSIP sale completed, 2022-03-01](https://investor.spglobal.com/news-releases/news-details/2022/SP-Global-Completes-Sale-of-CUSIP/default.aspx)
- [PVR Source / SEC 2a-5, 2022-07-14](https://press.spglobal.com/2022-07-14-S-P-Global-Market-Intelligence-launches-PVR-Source-to-help-clients-comply-with-new-SEC-Rule-2a-5)
- [Tradeweb × InvestorAccess (Tradeweb newsroom), 2022-09-29](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-collaborates-with-sp-global-market-intelligence-to-connect-primary-and-secondary-markets-in-europe/)
- [Investor Day 2022 slides, 2022-12-01](https://s29.q4cdn.com/690959130/files/doc_downloads/2022/12/S-P-Global-Investor-Day-2022-Slides-12-1-2022.pdf)
- [Equity InvestorAccess, 2023-04-04](https://press.spglobal.com/2023-04-04-S-P-Global-Market-Intelligence-launches-Equity-InvestorAccess-platform-to-streamline-new-issuance-workflows)
- [FI ETF distribution forecasting (EBP 2.3M), 2023-06-20](https://press.spglobal.com/2023-06-20-S-P-Global-Market-Intelligence-adds-Fixed-Income-ETF-distribution-forecasting-to-its-suite-of-Dividend-Forecasting-products)
- [Bloomberg TSOX × InvestorAccess, 2023-06-22](https://press.spglobal.com/2023-06-22-Bloomberg-and-S-P-Global-Market-Intelligence-Launch-Integrated-Solution-to-Streamline-Syndicated-Primary-Bond-Market-Workflows)
- [Loan pricing on Capital IQ Pro, 2023-06-28](https://press.spglobal.com/2023-06-28-S-P-Global-Market-Intelligence-Launches-Loan-Pricing-and-Analytics-in-S-P-Capital-IQ-Pro-Platform-Expansion)
- [DTCC ALERT / T+1, 2024-03-13](https://press.spglobal.com/2024-03-13-S-P-Global-Market-Intelligence-to-Collaborate-with-DTCC-on-T-1-Offering)
- [2024 AGM slides (Vitality contributors), 2024-05-01](https://s29.q4cdn.com/690959130/files/doc_downloads/2025/04/S-P-Global-2024-Annual-Shareholders-Meeting-Slides-5-1-2024.pdf)
- [Bond Reference Data (2.9M), 2024-06-18](https://press.spglobal.com/2024-06-18-S-P-Global-Market-Intelligence-expands-Reference-Bond-Data-with-addition-of-Sustainability-granularity)
- [Capital IQ Pro 19.4M FI securities, 2024-06-20](https://press.spglobal.com/2024-06-20-S-P-Capital-IQ-Pro-Expands-Fixed-Income-and-Gen-AI-Powered-Summarization-Capabilities)
- [Evaluated Loan Pricing, 2024-07-09](https://press.spglobal.com/2024-07-09-S-P-Global-Market-Intelligence-Unveils-Expanded-Loan-Pricing-Solution)
- [Lending Solutions, 2024-10-10](https://press.spglobal.com/2024-10-10-S-P-Global-Market-Intelligence-Lending-Solutions-Driving-Market-Innovation-and-Connectivity-through-an-Expanded-Product-Suite,-Enabling-Shorter-Loan-Settlement-Times)
- [MarketAxess CP+ partnership, 2024-10-31](https://press.spglobal.com/2024-10-31-S-P-Global-Market-Intelligence-and-MarketAxess-Announce-Strategic-Fixed-Income-Data-Partnership)
- [PrimeOne sale, 2024-11-01](https://investor.spglobal.com/news-releases/news-details/2024/SP-Global-Completes-Sale-of-PrimeOne/default.aspx)
- [S&P UBS Leveraged Loan Indices, 2024-12-04](https://press.spglobal.com/2024-12-04-S-P-Dow-Jones-Indices-and-UBS-Launch-S-P-UBS-Leveraged-Loan-Indices)
- [Munis on Capital IQ Pro (26M+), 2025-01-07](https://press.spglobal.com/2025-01-07-S-P-Global-Market-Intelligence-Expands-Fixed-Income-Coverage-with-the-addition-of-4-6-Million-Municipal-Securities-on-S-P-Capital-IQ-Pro)
- [LXIDs for private credit, 2025-06-24](https://press.spglobal.com/2025-06-24-S-P-Global-Expands-Private-Markets-Offering-With-Private-Credit-Identifiers-Using-LoanX-IDs)
- [Barclays agreement, 2025-07-23](https://press.spglobal.com/2025-07-23-S-P-Global-and-Barclays-Partner-on-a-Multi-Year-Strategic-Agreement)
- [CIQ IDs on DUNL.org, 2025-09-11](https://press.spglobal.com/2025-09-11-S-P-Global-ushers-new-era-of-open-data-access-Introduces-S-P-Capital-IQ-Identifiers-on-DUNL-org)
- [CDS coverage +3,600 issuers, 2025-10-22](https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ)
- [Investor Day 2025 slides (Risk & Valuations Services), 2025-11-13](https://s29.q4cdn.com/690959130/files/doc_events/2025/SP-Global-Investor-Day-Slides-11-13-2025.pdf)
- [WSO Compliance Insights, 2025-11-20](https://press.spglobal.com/2025-11-20-S-P-Global-Launches-WSO-Compliance-Insights-to-Streamline-Credit-Risk-Management)
- [EDM / thinkFolio sale, 2026-01-12](https://press.spglobal.com/2026-01-12-S-P-Global-Completes-Sale-of-EDM-and-thinkFolio-Businesses)
- [DataXchange / AmendX, 2026-03-03](https://press.spglobal.com/2026-03-03-S-P-Global-Launches-DataXchange-and-AmendX-to-Transform-Private-Credit-and-Syndicated-Loan-Management)
- [Capital IQ Pro 4M+ structured securities, 2026-03-12](https://press.spglobal.com/2026-03-12-S-P-Global-Enhances-Capital-IQ-Pro-with-Expanded-Fixed-Income,-Biopharma-and-Private-Markets-Data-Content-and-AI-Capabilities)
- [MI operating model (pricing → Enterprise Solutions), 2026-07-06](https://investor.spglobal.com/news-releases/news-details/2026/SP-Global-Evolves-Market-Intelligence-Operating-Model-to-Accelerate-Agentic-Solutions-Platform-Capabilities-and-Innovation-Announces-Executive-Leadership-Changes/default.aspx)
- [ETF Intelligence, 2026-07-16](https://press.spglobal.com/2026-07-16-S-P-Global-Market-Intelligence-Launches-ETF-Intelligence)
