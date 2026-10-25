# Note · Cross-company capability matrix — the market is sorting into four stacks, and the empty cells next to each stack are the next deals

> Cross-company analysis note · Maps to **Course 04** (Competitive Strategy — vertical integration, platform stacks, white space), **E3** (M&A — predicting targets), **E2** (Capital Allocation), **Course 03** (Microeconomics — complements and bottlenecks), **E9** (market structure and regulation) · Written 2026-10-25 · Part of the cross-company set: [[cross-company-attention-map]], [[cross-company-say-vs-do]]

- **Source:** `_ingest/raw/attention/capability_matrix.json`, built from the ten company note sets and digests (`notes/<company>-*.md`, `_ingest/raw/<company>/DIGEST.md`). Every non-zero cell carries a one-line evidence string and a source. Levels: **3** = core or market leader, **2** = meaningful business, **1** = small, pilot, minority stake or partnership only, **·** = absent. **→** = acquired or launched 2019–2026; **↓** = divested or retreated. Also 56 relationship edges between the ten firms.
- **Core claim:** Across the 19 layers of the trade-and-data chain, four firms have assembled near-complete **stacks** that combine price, benchmark, distribution and execution: **LSEG (with Tradeweb), ICE (with MarketAxess from 2027), Bloomberg and S&P Global**. The two banks and BlackRock sit on top of all four as clients, co-owners and suppliers. The stacks are converging on the same few gaps: **private-markets data and trading, US Treasury clearing, tokenized settlement, and AI products sold to clients**. Almost every 2024–26 deal in the study filled one of them. The empty cells that remain are the best guide to who buys what next.

---

## 1. The matrix

| Capability | TW | ICE | MKTX | BBG | SPGI | LSEG | TRI | GS | JPM | BLK |
|---|---|---|---|---|---|---|---|---|---|---|
| Evaluated pricing | 2 | **3** | 2 | **3**→ | 2 | 2 | · | · | · | · |
| Indices & benchmarks | 2 | **3**→↓ | 1→ | **3**→ | **3**→ | **3** | · | · | 2 | 1→ |
| Credit ratings & research | · | · | · | 1 | **3** | 2→ | · | 1 | 1 | · |
| Desktop / terminal | · | 1 | · | **3** | **3** | **3**→ | ·↓ | 1 | 1 | · |
| Data feeds & licensing | 2 | **3**→ | 1→ | **3**→ | **3**↓ | **3**→ | 1 | 1→ | 1→ | 1→ |
| Buy-side OMS / portfolio tech | · | 1→ | 1→ | **3**↓ | ·↓ | 1 | · | · | 1 | **3**→ |
| Venue: rates | **3**→ | 1 | 1→ | **3**→ | · | **3**→↓ | ·↓ | 1 | 1 | · |
| Venue: credit | **3**→ | 2→ | **3**↓ | 2 | · | **3**→ | · | 1 | · | · |
| Venue: equities & ETFs | 2 | **3** | 1→ | 2 | · | **3**↓ | · | 1 | 1 | 1→ |
| Venue: futures & commodities | 1→ | **3**→ | · | 1→ | · | ·↓ | · | · | · | · |
| Clearing (CCP) | · | **3**→ | · | · | ·↓ | **3**→ | · | · | · | · |
| Listings & primary markets | 1 | **3** | · | 1→ | 2 | 2↓ | · | **3** | **3** | · |
| Dealer market-making | · | · | · | · | · | · | · | **3** | **3** | · |
| Asset management | · | · | · | · | ·↓ | · | · | **3**→ | **3** | **3** |
| Private markets data/access | 1→ | · | · | 2→ | 2→ | 1→ | · | **3**→ | 2→ | **3**→ |
| Tokenization rails | 1→ | 1→↓ | · | 1→ | 1→ | 1→ | · | 1→↓ | 2→ | 2→ |
| AI products | 2→ | 1→ | 1→ | 2→ | 2→ | 2→ | 2→ | 1→ | 1 | 1→ |
| Mortgage tech | 1→ | **3**→ | · | · | · | · | · | · | 1 | · |
| Payments | 1→ | · | · | · | · | · | 1→ | 1→↓ | **3**→ | · |
| **Breadth (sum of levels)** | 22 | 31 | 11 | 30 | 21 | 32 | 4 | 21 | 26 | 15 |

*Judgement calls, from the matrix builder:*
- **Listings:** banks score 3 as underwriters, not as venues.
- **LSEG's venue levels** count Tradeweb, which it consolidates.
- **Thomson Reuters** scores near zero because it sold the financial business. Its AI score (2) is for legal and tax products, not markets.

## 2. Four stacks

| Stack | Holds (3s) | Missing or thin | 2019–26 moves that built it |
|---|---|---|---|
| **LSEG + Tradeweb** | Indices (FTSE Russell, WGBI), desktop (Workspace), feeds, rates and credit venues (Tradeweb), equities venue, clearing (LCH) | Futures (sold Borsa/IDEM, 2021), buy-side OMS (1), **US Treasury clearing**, private-markets data (1: Octus pending), evaluated pricing only 2 | Refinitiv (2021), Microsoft deal (2022), FTSE prices from Tradeweb (2023–25), PTS buy-back (2025), Octus (2026); Tradeweb's Nasdaq FI, Yieldbroker, r8fin, ICD and **Trumid** (2026) |
| **ICE + MarketAxess** | Evaluated pricing, indices, feeds, equities venue, futures/energy, clearing, listings, mortgage tech; credit venue becomes 3 with MarketAxess | **Desktop (1)**, buy-side OMS (1), **private markets (0)**, ratings (0), rates venue only 1 | Ellie Mae (2020), Black Knight (2023), ICE Bonds build (2019–26), **MarketAxess (2026)** |
| **Bloomberg** | Evaluated pricing (BVAL), indices (Bloomberg Agg), desktop, feeds, buy-side OMS (AIM/EMSX, slipping), rates venue | **Clearing (0)**, futures (1), listings (1), credit venue 2, no ratings | Bloomberg indices expansion, private-markets data, Terminal AI, Clearwater partnership (instead of building accounting) |
| **S&P Global** | Ratings, indices, desktop (Capital IQ), feeds | **No venue, no clearing**; evaluated pricing 2 and dependent on CP+ | IHS Markit (2022) and divestitures (clearing, OSTTRA stake, Engineering Solutions); With Intelligence (private markets); Kensho/AI |

**The pattern:**
- **The stacks hold their own price.** Each owns a pricing or benchmark franchise and is buying or building the trading and distribution layers around it. ICE bought the flow (MarketAxess). LSEG got the flow by inheritance (Tradeweb). Bloomberg built it. S&P owns none.
- **S&P is the exposed one.** Its corporate-bond evaluated prices partly rest on MarketAxess's CP+ feed, which ICE will own from H1 2027 ([[spglobal-pricing-fixed-income]], [[ice-marketaxess-deal]]).

## 3. The clients on top

| Firm | Where it's a 3 | Role toward the stacks |
|---|---|---|
| **Goldman** | Dealer, underwriting, asset management, private markets | Liquidity provider to every venue. Co-owner of LSEG's post-trade business. Co-investor with Tradeweb in Digital Asset (Canton). Advised Trumid on its sale |
| **JPMorgan** | Dealer, underwriting, asset management, payments | Founding Tradeweb owner and dealer. First bank to host Treasury algos on Tradeweb. Kinexys tokens as a rival settlement rail. Advised MarketAxess on its sale |
| **BlackRock** | Asset management, buy-side OMS (Aladdin), private markets | Anchor client of every venue. Aladdin is the buy-side's main distribution channel (Tradeweb credit inside Aladdin since 2022). Index licensee of S&P and FTSE Russell (>$430bn on FTSE products) |

**The control point is BlackRock's Aladdin.** Venues compete for placement inside it, and index providers depend on iShares mandates. BlackRock's own moves into indices (Preqin, to "index private markets") and venues (ETF RFQ, 1→) are small, but they're aimed at the toll-takers ([[blackrock-anchor-client]], [[blackrock-aladdin-data]]).

## 4. Where the firms are focused (→ moves) vs where they aren't

**Where everyone moved at once (2024–26):**
- **Private markets:** Bloomberg, S&P (With Intelligence), LSEG (Octus), BlackRock (GIP, HPS, Preqin), Goldman, JPMorgan and Tradeweb (MAXEX). **Not ICE, MarketAxess or Thomson Reuters.**
- **Tokenization:** all except MarketAxess and Thomson Reuters. Most are at level 1 (pilots and stakes). Goldman spun its platform out, and ICE deconsolidated Bakkt.
- **AI products:** all ten, but only Thomson Reuters, Bloomberg, S&P, LSEG and Tradeweb reach 2. None reaches 3.

**Where nobody is moving:** layers held by one or two incumbents that no one is challenging.
- **Clearing:** only ICE and LSEG. S&P exited. Tradeweb, Bloomberg and MarketAxess have no CCP, yet the Treasury clearing mandate (cash Dec 2026, repo Jun 2027) makes it the most important new piece of US infrastructure.
- **Credit ratings:** S&P alone at 3 (LSEG 2 via Octus/LPC research). No new entrant.
- **Dealer market-making:** only the banks. The venues court non-bank liquidity providers (Citadel Securities, Jane Street) instead of competing with them.

**Retreats (↓):**
- **MarketAxess:** credit venue, from share loss to the ICE sale.
- **S&P:** clearing, feeds and OMS (post-IHS divestitures).
- **LSEG:** futures, equities and listings (the Borsa sale; the UK listings decline).
- **Bloomberg:** OMS share slipping.
- **Thomson Reuters:** everything financial.
- **Goldman:** consumer payments and tokenization (spun out).

## 5. The empty cells: likely next moves (inference, ranked)

1. **ICE → private-markets data or pricing (0).** Every other stack bought here in 2024–26, and ICE's evaluated pricing has no private-credit coverage. It's a natural tuck-in once MarketAxess closes and leverage is back toward 3.0×.
2. **S&P → a venue-sourced price feed, or a pricing acquisition (2, fragile).** If CP+ stays with ICE, S&P needs a non-competitor trade-derived price. Candidates: Tradeweb/LSEG (awkward), Bloomberg (rival), or an independent like Trumid's FVMP, which Tradeweb now owns.
3. **LSEG/Tradeweb → US Treasury clearing (0 in the US).** ICE has run an alternative Treasury clearer since February 2026. LCH entering the US, or a Tradeweb partnership with an existing clearer, would complete the rates stack before the mandates bite.
4. **Tradeweb → private-credit trading (1).** It cites a "$35T" private-credit opportunity but owns only a MAXEX stake. Paired with LSEG's Octus data, a trading product is the obvious move ([[tradeweb-mission-forces]]).
5. **Bloomberg → clearing or a credit venue upgrade (0 / 2).** It is the only stack without a CCP, and its credit venue trails Tradeweb and MarketAxess.
6. **BlackRock → indices or pricing (1 / 0).** Preqin is the first step from index *licensee* to index *owner*. A benchmark acquisition would cut its index rents ([[blackrock-private-markets]]).

## 6. The relationship network (56 edges)

| Edge type | Count | Most consequential |
|---|---|---|
| Partnership | 11 | FTSE Russell administers the Tradeweb closing prices that set the WGBI (2024–25) |
| People moves | 9 | Schwimmer (Goldman → LSEG CEO); Pluta (JPM → Tradeweb President, 2023–24); Remyn Stone (Bloomberg → LSEG D&A); Blaugrund (Tradeweb → NYSE → ICE tokenization) |
| Client | 9 | BlackRock → every venue via Aladdin; JPM → Tradeweb (Treasury algos) |
| Data licence | 6 | CP+ → S&P evaluated pricing (2024); ICE benchmark admin uses Tradeweb data (Term SONIA, UST closes) |
| Competitive overlap | 5 | ICE + MarketAxess vs Tradeweb + Trumid (Jul vs Oct 2026) |
| Former ownership | 4 | Thomson → Refinitiv → LSEG; Goldman and JPM as founding Tradeweb dealers |
| Co-investment | 3 | Goldman, Tradeweb, DRW and Citadel Securities in Digital Asset (Canton) |
| Advisor | 3 | Goldman for Trumid; JPM for MarketAxess (sell side); JPM for Tradeweb on ICD |
| Board interlock / ownership / acquisition / divestiture | 6 | LSEG → Tradeweb (50.9% / 89.9%); ICE → MarketAxess; Apple Card, Goldman → JPM |

**Reading it:** the network is dense and runs both ways. The same two banks advised the buyer's rival and the seller in the two 2026 credit deals. ICE's benchmark unit depends on Tradeweb data while ICE competes with Tradeweb in credit. Coopetition is the norm, not the exception ([[canon-brandenburger-nalebuff-coopetition]]).

## 7. Tying the three cross-company notes together

| Question | Attention map says | Say-vs-do says | Capability matrix says |
|---|---|---|---|
| Where are firms focused? | AI and tokens everywhere since 2023; private markets at BlackRock, Goldman, S&P | Bets carry 5–60% of attention and ~0% of revenue | Bets show up as → at level 1–2. Nobody reaches 3 in AI or tokens |
| What pays the bills? | Under-told | Rates (TW), credit (MKTX), energy and mortgages (ICE), ratings (SPGI), iShares (BLK), trading (GS) | The 3s that nobody is attacking: clearing, ratings, dealer balance sheet |
| What's fragile? | Never discussed | Outages, control and client concentration live only in the 10-K | Single points: WGBI on Tradeweb prices; S&P pricing on CP+; buy-side on Aladdin |
| What's next? | Private markets is the venues' blind spot | Under-covered growth lines (repo, energy, financing) | Empty cells: ICE private markets, S&P pricing, LSEG US Treasury clearing, Tradeweb private credit |

## 8. What the matrix doesn't prove

1. **Levels are judgement on public evidence.** A "2" for AI at LSEG and at Tradeweb are different things. The cell evidence strings in the JSON are the place to check.
2. **Breadth isn't strength.** MarketAxess (11) was profitable and focused, and Thomson Reuters (4) chose narrowness deliberately. Breadth measures optionality and exposure, not returns.
3. **Pending deals are counted as moves.** MarketAxess (ICE), Trumid (Tradeweb) and Octus (LSEG) haven't closed yet (targets H1 2027).
4. **Private Bloomberg** is scored from its own announcements only.

## 9. Canon lenses

- **Vertical integration and complements** ([[canon-porter-competitive-strategy]], [[canon-shapiro-varian-information-rules]]): owning the price *and* the trade lets a stack capture the complement's margin. That's why the evaluators bought the flow.
- **Platform envelopment** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): each stack is enveloping its neighbours' layers, so the cells next to a stack are where envelopment happens next.
- **Bottlenecks** ([[canon-goldratt-the-goal]]): clearing and Aladdin are the chokepoints. Whoever holds them sets terms for the rest.
- **Seven Powers** ([[canon-helmer-7-powers]]): cornered resources (benchmarks, ratings licences), switching costs (desktops, Aladdin), network economies (venues).

## 10. Open questions

1. Does ICE make a private-markets data acquisition within 18 months of closing MarketAxess?
2. Does S&P's CP+ partnership survive the ICE change of control, and what replaces it if not?
3. Who clears US Treasuries for Tradeweb's clients when the mandate arrives: FICC, ICE, CME, or LCH entering?
4. Does BlackRock buy or build an index franchise for private markets?
5. Does any stack reach level 3 in AI, meaning disclosed AI revenue, by 2028?

**Links:** [[cross-company-attention-map]] · [[cross-company-say-vs-do]] · [[tradeweb-hub]] · [[tradeweb-mission-forces]] · [[lseg-hub]] · [[lseg-tradeweb-control]] · [[ice-hub]] · [[ice-marketaxess-deal]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[spglobal-pricing-fixed-income]] · [[thomsonreuters-hub]] · [[goldman-hub]] · [[jpmc-hub]] · [[blackrock-hub]] · [[blackrock-anchor-client]] · [[blackrock-aladdin-data]] · [[blackrock-private-markets]] · [[canon-porter-competitive-strategy]] · [[canon-shapiro-varian-information-rules]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-parker-platform-revolution]] · [[canon-goldratt-the-goal]] · [[canon-helmer-7-powers]] · [[canon-brandenburger-nalebuff-coopetition]]

---
### Rep
1. **Score a deal.** For each pending deal (ICE–MarketAxess, Tradeweb–Trumid, LSEG–Octus), list which matrix cells change and by how much. Which deal fills the most valuable empty cell, and why?
2. **Predict and log.** Pick two cells from §5. Write each as a dated, checkable prediction ("By 2027-12-31, ICE announces a private-markets data or pricing acquisition") with your probability. Add them to `acumen/JUDGMENT-LEDGER.md` for scoring later.
3. **Stress test.** Assume Tradeweb's closing-price feed fails at the London close on a WGBI rebalance day. Trace the impact through the relationship edges in §6. Who is affected, in what order, and what does each firm's risk-factor section ([[cross-company-say-vs-do]] §3) say they would do?
