# Apply rep: the six derivatives problems, run against the ten market-infrastructure firms

> **What this is.** An Apply rep, like [[apply-wss-to-venture]]. It takes the six problems from
> [[rodrigues-derivatives-problem-map]] and tests them against the ten company studies summarized in
> [[cross-company-capability-matrix]].
>
> **The question.** The company studies map the **supply side**: who sells pricing, risk systems, venues and
> clearing, and how they bought their way into each layer. The derivatives corpus maps the **demand side**:
> what problem each of those products solves, and why the problem is hard. Run together, does "which of the six
> problems does this firm carry or sell?" explain where the moats are, where the money is moving, and what gets
> bought next?
>
> **Provenance.** Company figures are as each company states them, taken from the company notes cited inline.
> The six-problem frame comes from Rodrigues's posts. Lines marked *(added context)* are general market history
> from this note, not from either source. Like the company notes, the evidence is mostly each firm's own voice, so
> it shows what firms *claim* to solve, not independently measured share.
>
> Maps to **Course 04** (Competitive Strategy: moats), **Exec E2** (Capital Allocation), **E6** (Crisis),
> **E10** (Digital & AI), **Course 11** (Global Macro).

---

## The six problems against the ten firms, in one table

Who **sells** the solution (venue, data or utility) versus who **carries** the problem on its own balance
sheet. Firm abbreviations as in the capability matrix.

| Problem | Sold as | Main sellers (matrix level 3) | Who carries it | Evidence |
|---|---|---|---|---|
| **P1 Value it** | Evaluated pricing, indices, curves | ICE, BBG, LSEG (FTSE Russell), SPGI (indices) | Every holder that must mark a book | ICE prices ~3m instruments; BVAL 2.8m securities ([[ice-fixed-income-data]], [[bloomberg-pricing-bval-ibval]]) |
| **P2 Measure the risk** | Risk and portfolio platforms | BLK (Aladdin), BBG (AIM/PORT) | Funds, dealers | Aladdin began as BlackRock's internal risk system ([[blackrock-aladdin-data]]); Goldman's SecDB in the 1990s ([[goldman-markets-platforms]]) |
| **P3 Hedge it** | Venues, algos, dealer liquidity | TW (rates), MKTX (credit), ICE (futures), GS/JPM (dealers) | Corporates, funds, then dealers who take the other side | TW SEF: $150tn, 52% of SEF volume in 2024 ([[tradeweb-derivatives-regulation]]) |
| **P4 Will they pay** | Central clearing | ICE (CDS), LSEG/LCH (swaps) | Banks for bilateral trades; the CCP and its members for cleared ones | ICE Clear Credit >80% of CDS clearing; SwapClear >90% of cleared IRS ([[ice-clearing-treasury]], [[lseg-post-trade-clearing]]) |
| **P5 Fund it** | Financing, margin utilities, capital | GS/JPM (financing), LSEG (Acadia) | Dealers' balance sheets, then nonbanks | Goldman financing: 19% of markets revenue (2018) → ~46% (Q3 2026) ([[goldman-markets-platforms]]) |
| **P6 Compute it** | Pricing engines, AI pricing, cloud platforms | BBG, ICE, TW, BLK | Everyone, invisibly | BVAL's ML retrains in under 6 hours; Tradeweb Ai-Price ([[tradeweb-ai-price]]) |

Two firms appear on nearly every row: **LSEG and ICE**. They are the only two that sell both a P1 reference price and
a P4 clearing house. The capability matrix calls them "near-complete stacks". In six-problem terms, they own the
problem at the bottom (P1) and the one regulators made mandatory (P4).

---

## Concept 1 · Whoever owns the reference price sits under everything else (P1)

**The derivatives idea:** every other problem uses P1 as an input. Risk (P2) is the change in a price; a hedge (P3)
is sized off a price; CVA (P4) is a price adjustment; margin (P5) is called on a price move.

**What the companies show:**
- **ICE.** Its fixed-income business earns **$1,234M from data and analytics against $125M from execution** (FY25,
  about 10:1). Best execution, TCA, liquidity scores, ICE indices and ICE's own venue all measure trades against
  ICE's evaluated price ([[ice-fixed-income-data]]).
- **Bloomberg.** Its position doesn't depend on venue share, which it never publishes. It depends on owning BVAL and
  then making protocols, indices and futures settle against it ([[bloomberg-pricing-bval-ibval]]).
- **S&P is the exposed case.** It sells pricing mainly as regulatory evidence (SEC Rule 2a-5), and part of its
  corporate-bond pricing rests on MarketAxess's CP+ feed, which ICE will own from 2027
  ([[spglobal-pricing-fixed-income]]). An evaluator that rents its prices has a weak P1 position.
- **A clearing house can make P1 decisions for the whole market.** LCH moved to SOFR discounting in October 2020
  across >1m contracts and $120tn notional ([[lseg-post-trade-clearing]]). One discount-curve switch at a CCP
  re-valued a large part of the swaps market.

**Verdict:** this is the strongest fit. The firms with the highest-margin, stickiest businesses own a P1 price that other
products are graded against. Execution is the cheaper layer on top.

---

## Concept 2 · The risk system becomes the language (P2)

**The derivatives idea:** risk numbers are model-defined and fragile. Greeks are first-order approximations, vega
isn't additive across expiries, and VaR is blind past its cutoff. Whatever system defines your risk numbers also
defines what your desk is allowed to do.

**What the companies show:** Aladdin went from BlackRock's internal risk system to cloud SaaS, then to a portfolio
workflow, a connectivity layer and a data business. Technology revenue roughly doubled from $785M (2018) to about
$1.5B (2023) ([[blackrock-aladdin-data]]). The capability matrix names Aladdin "the control point": venues compete
to be placed inside it ([[blackrock-anchor-client]]). Goldman took the same path from SecDB (firm-wide risk aggregation)
to Marquee, which pushes its models to clients' desktops ([[goldman-markets-platforms]]).

**Verdict:** this fits, and explains *why* the switching costs are high. Changing risk platforms means changing the
definitions your limits, reports and committees use. The derivatives lens adds the warning: the platform's
risk numbers are only as good as its model choices, and clients rarely test them.

---

## Concept 3 · Hedging moved to venues because regulation standardized it (P3)

**The derivatives idea:** a hedge only transfers risk cleanly if the instrument is standard and the other side is
reliable. Custom hedges stay with dealers.

**What the companies show:**
- **Swaps.** Tradeweb's swaps business was "made by regulation". Clearing mandates standardized swaps, trading
  mandates pushed them onto venues, and the LIBOR → SOFR switch forced the market to rebook positions through
  Tradeweb ([[tradeweb-derivatives-regulation]]).
- **Credit.** MarketAxess's all-to-all pool rose from 27% (2019) to 35% of credit volume in March 2020, when dealers
  pulled back ([[marketaxess-open-trading]]).
- **Dealers.** Goldman didn't fight electronification. It became broker, venue operator, principal and data
  distributor at once ([[goldman-markets-platforms]]).

**What the derivatives corpus adds:** the corporate hedge is still bespoke. His Brazil series shows a local dealer
building synthetic onshore dollars to absorb an exporter's forward. No venue in the ten studies serves that client
directly, and corporates appear in only 13 of his posts.

**Verdict:** this fits standardized hedges. It doesn't reach the corporate end-user, which is a gap in both sources.

---

## Concept 4 · A clearing house is CVA, centralized (P4)

**The derivatives idea:** with a bilateral trade, each bank prices the other's default risk through CVA and holds
capital against it. Central clearing replaces many bilateral exposures with one counterparty, the CCP, which nets
them and backs them with margin and a default fund shared by its members.

**What the companies show:**
- **ICE.** ICE Clear Credit was founded during the 2008 crisis and now claims **>80% of CDS clearing**, with a record
  **$2.678tn cleared in a day** (Mar 20 2026) ([[ice-clearing-treasury]]). The note's verdict is that **"the moat is
  netting"**: one pool, one margin model, offsets "as high as 98%".
- **LCH.** SwapClear has **>90% of cleared interest-rate swap notional** ($1,941trn in 2025). LSEG paid **£1.15bn** to
  buy back revenue it had shared with its dealer-members ([[lseg-post-trade-clearing]]).
- **Clients push back on who bears losses.** Goldman, BlackRock, JPMorgan and others co-wrote a 2019 paper asking
  CCPs to put more of their own capital first in line ([[goldman-markets-platforms]]).

**Why netting creates winner-take-most:** netting reduces both the exposure (the P4 cost) and the margin (the P5 cost).
The bigger the pool, the more trades offset, the cheaper it is to clear there, and the more trades arrive. That is why
ICE has to sell "choice" in Treasury clearing *against* netting: the incumbent, FICC, already holds the netting set.

**Verdict:** this is the clearest link between the two sources. XVA is what P4 costs when you *don't* clear; the CCP
franchises are what P4 earns when a regulator makes clearing mandatory.

---

## Concept 5 · Funding and capital are where the money moved (P5)

**The derivatives idea:** FVA, MVA and KVA are real costs charged to trades: funding the position, posting initial
margin, and holding regulatory capital. When rules raise those costs, activity moves to whoever carries them cheapest.

**What the companies show:**
- **JPMorgan** has made one argument for six years: capital rules (G-SIB surcharge, SLR, Basel III endgame)
  treat Treasuries and market-making as riskier than they are. That shrinks dealer balance sheets and pushes
  intermediation to nonbanks ([[jpmc-capital-regulation]]). In XVA terms, this is a fight over **KVA**.
- **Goldman** took the other side of the same fact. If balance sheet is scarce, charge for it. Financing grew from
  **19% of markets revenue (2018) to ~46% (Q3 2026)** ([[goldman-markets-platforms]]).
- **Uncleared trades still need margin.** LSEG bought Acadia (margin for uncleared trades: 2,000+ participants, >$1tn
  of collateral a day) and calls the uncleared market "comparable to" the cleared one
  ([[lseg-post-trade-clearing]]).
- **The rates layer.** [[wss-rates-macro]] and [[wss-trading-hedge-funds]] show the same constraint in the basis trade
  and repo: "the holding period belongs to whoever funds you."

**Verdict:** this fits strongly, and it's the one most likely to be underrated. P1–P4 are mostly solved and
productized. P5 is where pricing power has moved since 2018, for dealers and for margin utilities.

---

## Concept 6 · AI lands on P1 and P6 first, and quant finance supplies the test (P6)

**The derivatives idea:** ML models are function approximators. In pricing they must respect no-arbitrage, hold up
out of sample and survive stress periods. A model that fits the data but breaks those rules is a hidden P2 risk.

**What the companies show:** the attention map finds that since 2023 all ten firms converged on "AI and tokens"
([[cross-company-attention-map]]). The AI products that actually shipped are P1 engines: BVAL's regression-tree
ensemble, IBVAL intraday pricing, Tradeweb Ai-Price, ICE's continuous evaluated prices. Tradeweb's "~30% better
than the last trade" is the floor test, not a head-to-head with other evaluators ([[tradeweb-ai-price]]).

**Verdict:** this fits. The derivatives corpus supplies the questions to ask any AI pricing claim: compared with
what, out of sample, through a stress period, and does it respect arbitrage bounds? None of the vendors publish
that test.

---

## Concept 7 · 2008 created the demand; rules keep creating it

Most of the moats in the matrix trace back to a rule that made one of the six problems mandatory, standard and
measurable.

| When | Rule or event | Problem it made mandatory | Who it built |
|---|---|---|---|
| 2008 | Crisis need for "more robust independent pricing" | P1 | Bloomberg BVAL ([[bloomberg-pricing-bval-ibval]]) |
| 2009 | CDS clearing pushed by US regulators | P4 | ICE Clear Credit ([[ice-clearing-treasury]]) |
| 2010s *(added context)* | Dodd-Frank and EMIR clearing and trading mandates; CVA capital charges | P3, P4 | LCH SwapClear, Tradeweb SEF ([[tradeweb-derivatives-regulation]]) |
| 2016–17 | Uncleared margin rules phase in *(added context)* | P5 | Acadia, later LSEG ([[lseg-post-trade-clearing]]) |
| 2020–23 | LIBOR → SOFR | P1 | Tradeweb's rebooking tools; LCH's discounting switch |
| 2022 | SEC Rule 2a-5 (fund fair-value diligence) | P1 | S&P PVR Source ([[spglobal-pricing-fixed-income]]) |
| 2026–27 | US Treasury clearing mandate (cash Dec 31 2026, repo Jun 30 2027) | P4, P5 | ICE's entry ("would not have entered without it"); JPM sponsored clearing ([[ice-clearing-treasury]], [[jpmc-capital-regulation]]) |

**Verdict:** for this industry, regulation creates demand rather than just limiting it. The pattern
predicts the next deals: watch for rules that make a problem mandatory in a market where it is still bilateral or
manual.

---

## Concept 8 · The problems move; the revenue moves with them

| Problem | Used to sit with | Moved to | What the move did to revenue |
|---|---|---|---|
| P1 Value it | Each dealer's own marks | Independent evaluators and index providers | Created the data businesses (ICE about 10:1 data over execution) |
| P2 Measure the risk | In-house systems | Platforms (Aladdin, Marquee) | Turned a cost centre into SaaS revenue and a control point |
| P3 Hedge it | Voice dealers | Electronic venues | Venue fees, then data from the flow ([[tradeweb-rates-em]]) |
| P4 Will they pay | Bilateral bank XVA desks | CCPs | The deepest moats in the study (>80%, >90% shares) |
| P5 Fund it | Bank balance sheets | Nonbanks, dealer financing desks, margin utilities | Goldman financing ~46% of markets revenue; JPM's capital fight |
| P6 Compute it | Internal quant teams | Vendors' engines and cloud platforms | AI pricing products; the "AI and tokens" convergence |

---

## Where the gaps are: the matrix's four gaps, in six-problem terms

The capability matrix found every stack converging on four gaps. Each one is a six-problem story:

1. **US Treasury clearing (P4 + P5).** A new mandate moves counterparty risk and margin into CCPs. The fight is over
   who holds the netting set.
2. **Private markets data and trading (P1).** His post on smoothed private marks says low reported volatility is stale
   pricing, not low risk. Whoever builds a credible private-markets price owns the P1 position there. That is
   BlackRock's Preqin bet ([[blackrock-aladdin-data]]).
3. **Tokenized settlement (P5).** The pitch is faster collateral movement and less funding tied up in settlement,
   which is a P5 cost cut, not a new market ([[jpmc-kinexys-deposit-tokens]]).
4. **AI products sold to clients (P6 on top of P1).** These are only as good as the reference price underneath them
   (Concept 6).

The derivatives corpus adds three gaps the company studies don't show:

- **XVA compute for mid-size banks (P4–P6).** It needs portfolio-wide Monte Carlo, and no firm in the study sells it
  as a headline product.
- **Corporate hedging transparency (P3).** No firm in the study serves the end-user corporate directly.
- **Margin for uncleared trades (P5).** Only LSEG/Acadia has a position, and LSEG calls the market as large as the
  cleared one.

---

## Verdict: where the six-problem lens applies and where it breaks

- **It explains well:** why data beats execution on margin (P1); why clearing houses are the deepest moats (P4
  netting); why dealers moved into financing (P5); why every stack wants a reference price; and why rules predict
  deals.
- **It explains weakly:** listings, mortgage technology (ICE's Ellie Mae and Black Knight), credit ratings and
  desktops. Those are distribution and workflow businesses, not risk-transfer ones, and the lens has little to say
  about them.
- **Bias on both sides:** the company notes are mostly each firm's own voice. Rodrigues writes from the dealer's and the
  system builder's seat. Neither source covers the corporate end-user well.

---

## Retrieval questions

1. *Why does ICE earn ten times more from fixed-income data than from fixed-income trading?* Its evaluated price is
   the P1 ruler: best execution, TCA, indices and its own venue are all graded against it. Execution is a
   replaceable layer on top of the price.
2. *How is a clearing house related to CVA?* CVA is the cost of bilateral counterparty risk (P4). A CCP replaces many
   bilateral exposures with one netted exposure backed by margin and a shared default fund. Clearing is the
   institutional substitute for each bank pricing CVA itself.
3. *Why is clearing winner-take-most?* Netting cuts both exposure and margin, so a bigger pool is cheaper to clear in,
   which attracts more trades. That's why ICE must sell "choice" against FICC's existing netting set in Treasuries.
4. *What is Dimon really arguing about, in XVA terms?* KVA: the cost of the regulatory capital that trades consume.
   Higher capital charges make dealers charge more or step back, and the activity moves to nonbanks.
5. *Why did Goldman's financing share of markets revenue more than double?* Capital rules made balance sheet scarce
   (P5), so the dealer charges for it. Its moat moved from execution to financing.
6. *What should you ask about an AI pricing claim like "30% better"?* Better than what (last trade is the floor),
   out of sample, through a stress period, and does it respect no-arbitrage? Those are the P6 tests from quant finance.
7. *Which rule built which moat?* BVAL from the 2008 pricing crisis, ICE Clear Credit from 2009 CDS clearing,
   Tradeweb swaps from trading mandates, S&P PVR Source from Rule 2a-5, ICE's Treasury entry from the 2026–27
   clearing mandate.

---

## Open questions to resolve with better data

- **Independent share data for clearing and evaluated pricing.** All shares here are self-reported.
- **Head-to-head pricing accuracy** (BVAL vs ICE vs CP+ vs Ai-Price), out of sample and through a stress period.
- **XVA vendors** (Murex, Numerix, Quaternion and others) are outside the ten studies. A pull on them would test whether
  XVA compute is a real gap or just one this repo hasn't covered.
- **Corporate treasurers' side of hedging:** no source in the repo speaks for them.

## Links

[[rodrigues-derivatives-problem-map]] [[cross-company-capability-matrix]] [[cross-company-attention-map]]
[[ice-fixed-income-data]] [[ice-clearing-treasury]] [[lseg-post-trade-clearing]] [[bloomberg-pricing-bval-ibval]]
[[spglobal-pricing-fixed-income]] [[tradeweb-derivatives-regulation]] [[tradeweb-ai-price]] [[tradeweb-rates-em]]
[[marketaxess-open-trading]] [[blackrock-aladdin-data]] [[blackrock-anchor-client]] [[goldman-markets-platforms]]
[[jpmc-capital-regulation]] [[jpmc-kinexys-deposit-tokens]] [[wss-rates-macro]] [[wss-trading-hedge-funds]]
[[apply-wss-to-venture]]
