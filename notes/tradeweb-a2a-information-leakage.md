# Note · Tradeweb on A2A information leakage — a real effect, measured with the vendor's own ruler

> Practitioner / market-structure note · Maps to **Course 07** (Data, Analytics & Decision-Making — regression design, selection bias), **Course 04** (Competitive Strategy), **Course 11** (Global Strategy & Macro), **E-track** competitive strategy · Written 2026-10-24 · Companion to [[tradeweb-ai-price]]

- **Source:** Caretti, Mahajan & Husveth (Tradeweb U.S. Credit), *Information Leakage in US Credit: Evidence from All-to-All RFQs*, whitepaper, May 13 2026 ([PDF](https://www.tradeweb.com/49a042/globalassets/newsroom/market-insights/2026/5.13.26-credit-whitepaper/information-leakage-in-us-credit-5.13.26b-final-1.pdf)).
- **Core claim:** Broadcasting a bond order to everyone (all-to-all RFQ) moves the price against you more than a bilateral voice trade with one dealer: about **+0.07–0.09 bp for buys, +0.14–0.15 bp for sells**, rising to **~0.2–0.3 bp in less-liquid bonds**, over the first ~30 minutes. The effect is plausible and consistent across both directions. But it is small, it is measured with Tradeweb's own pricing model, and the paper ends by promoting Tradeweb's targeted-RFQ product (SNAP+).

---

## 1. The question

Two ways to execute a large IG corporate bond trade:

| | **All-to-all (A2A) RFQ** | **Voice / bilateral** |
|---|---|---|
| Who sees the order | Many counterparties, incl. anonymous buy-side | One dealer |
| Price competition | High — tighter fills | Low |
| Information exposure | High — many people now know your side | Low |
| Who bears adverse selection | Spread across responders | The one dealer |

The paper measures only the cost side: does the wider exposure push the market against you *after* you trade, before the print is public?

## 2. Design

- **Sample:** Tradeweb client A2A and voice-processed trades, Jan 1 2025 – Apr 30 2026; **IG only, spread-quoted, > $1mm notional**. No sample counts given.
- **Outcome:** cumulative log change in the bond's **Ai-Price** mid (in spread terms), in 5-minute steps from acceptance out to 100 minutes. Signed so positive = moved in the direction of your trade (spreads tighten after a buy, widen after a sell).
- **Model:** Gaussian GLM (i.e. weighted OLS), one regression per horizon, buys and sells separately:
  `move ~ β₀ + β_A2A·[A2A] + β_vol·log(size) + β_liq·LiquidityScore`
- **Weights:** within each day, A2A and voice get equal total weight (the class-balancing weight `N_d / 2N_c,d`). The authors admit an unweighted fit gives similar answers.
- **Identification:** conditional independence — once you control for size and liquidity, which protocol the client chose is unrelated to what the price does next. The authors call the result "quasi-causal."

## 3. Results (read off the charts by eye)

| Segment | β_A2A plateau | Shape |
|---|---|---|
| **Buys**, all | ~0.07–0.09 bp | Slight dip in the first 10 min, rises to plateau by ~30 min, CI touches zero by 100 min |
| **Sells**, all | ~0.14–0.15 bp | Flat for 10 min, steep rise to plateau by ~25 min, holds until ~95 min |
| Buys, liquidity score ≤ 5 | ~0.2–0.32 bp | Peaks ~60 min, wide CI that crosses zero late |
| Buys, liquidity score > 5 | ~0.05–0.07 bp | Tight CI |
| Sells, liquidity score ≤ 5 | ~0.25–0.32 bp | Wide CI |
| Sells, liquidity score > 5 | ~0.10–0.12 bp | Tight CI |

- **Sells leak about twice as much as buys.** That fits the usual asymmetry: a seller in credit usually needs the dealer to take on inventory, and dealers price that risk more heavily than they price a buyer's request.
- **The ~10-minute lag before the move** is interesting. If the move were mechanical (the model reacting to the RFQ itself), you might expect it at once. A lag fits responders who lost the auction hedging or repricing. That is the paper's best piece of evidence and it doesn't remark on it.

## 4. What it doesn't prove — the gaps

1. **The ruler is Tradeweb's own model.** Per [[tradeweb-ai-price]] §1, Ai-Price takes **Tradeweb's own RFQ flow** as an input. An A2A RFQ sent to many responders generates many quotes on Tradeweb. If those quotes feed the mid, part of the "leakage" is the model seeing the auction, not the market reacting to it. The paper needs a robustness check using a price Tradeweb doesn't build (CBBT, CP+, or the next TRACE print).
2. **Selection, not protocol.** Clients choose A2A or voice for reasons size and liquidity don't capture — urgency, information, whether the bond is "in play" that day, whether the dealer is already axed. An informed seller who needs out *now* blasts A2A; that seller's bond would have widened anyway. Two controls cannot absorb that. "Quasi-causal" is too strong.
3. **The "pre-TRACE window" doesn't fit the rules.** TRACE's 15 minutes is a **reporting deadline**, and prints go public when reported ([[tradeweb-ai-price]] §3.4, §6). For a 100-minute window to be entirely pre-public, voice-processed trades would need to be reported late, which the paper doesn't explain. For trades > $5mm, the size is capped as "5MM+" but the print itself is public. Most of the curve is probably *post*-dissemination.
4. **Cost without benefit.** The paper says A2A has "proven" better execution and then measures only the leakage. The decision a desk actually faces is *price improvement − leakage*. Tradeweb's own teaser blog six weeks earlier (*From "Blast All" to "Select Smart"*, Mar 31 2026) gives both legs for 2025 IG > $1mm: A2A is **~0.2 bp better on execution** and has **~0.17 bp more market impact** than voice, also measured with Ai-Price. On Tradeweb's own numbers **A2A still nets ~+0.03 bp ahead**. The whitepaper drops the benefit leg, and the "leakage" framing reads stronger than the data.
5. **Thin reporting.** No N, no coefficient tables, no standard-error method (the 100-minute horizons overlap, so errors are serially correlated across the curve), and no explanation of how a unitless log change becomes "bps."
6. **"Voice" isn't defined.** Voice-processed trades on Tradeweb are often agreed by phone and then booked on the platform. Agreement time and booking time can differ, so the start of the clock (t₀) may not mean the same thing for the two groups.

## 5. The strategic read

- **Every venue publishes the study that sells its product.** MarketAxess has spent years publishing evidence that Open Trading (its A2A) saves clients money. Tradeweb, which overtook MarketAxess in IG share ([[tradeweb-ai-price]] §6) and whose growth leans on RFQ and portfolio trading, publishes evidence that broadcasting has a cost — and that **SNAP+** (choose dealers using past hit rates and real-time activity) is the middle ground. Read the two side by side.
- **The finding is still plausibly true.** Losers in a wide auction learn your side and size. That is old microstructure (the winner's curse in reverse: the losers are informed). Equities solved it with conditional orders and dark pools; credit is going through the same arc: "blast all" → "select smart" (the title of the companion Tradeweb blog, Demina, Mahajan & Husveth 2026).
- **Dealers:** the paper's second implication is that the dealer who wins an A2A sell faces adverse price movement afterwards. That pushes dealers to quote A2A requests wider — so leakage is partly paid for in the quote, not just the move.

## 6. Canon lenses

- **Selection bias** ([[canon-kahneman-sibony-sunstein-noise]], Course 07): observational protocol comparisons are the textbook case — the chooser knows more than the regression.
- **Information goods & positioning** ([[canon-shapiro-varian-information-rules]], [[canon-helmer-7-powers]]): the venue that owns the pricing model, the protocol and the study controls the frame. That is power, not proof.
- **Explore vs exploit in dealer selection:** SNAP+ is a recommender system over dealers; it trades exposure (fewer eyes) for competition (fewer quotes). Same trade-off as the paper, set by an algorithm instead of the trader.

## 7. Practitioner counterpoint

- For: buy-side traders do talk about A2A "showing your hand," especially on large sells in illiquid names. The paper's liquidity split matches that intuition.
- Against: a 0.1 bp effect on the median IG trade is inside most desks' TCA noise, and the paper doesn't report price improvement on the same trades.
- Both: the right use of this paper is as a **hypothesis for your own TCA** — split your own A2A vs targeted fills by liquidity and side, and measure on a third-party price.

## 8. What to ask Tradeweb

1. Re-run the regressions on CP+ / CBBT / next-TRACE-print mids instead of Ai-Price.
2. Show Ai-Price's input timestamps: does an open A2A RFQ affect the mid?
3. Report N, coefficient tables and standard errors clustered by day/bond.
4. Report price improvement vs Ai-Price at execution on the same trades, so leakage and price improvement can be netted.
5. Add a **SNAP+ arm**. The paper argues for it but doesn't measure it. The only SNAP+ numbers published are *estimated* savings of 0.055–0.096 bp from a 15,000-trade **GBP swaps** pilot (Apr 2025, [[tradeweb-tech-ai-data]]). None exist for credit.
6. Explain the TRACE timing: what share of the 100-minute window is actually before dissemination?

**Links:** [[tradeweb-hub]] · [[tradeweb-credit]] (the credit franchise and SNAP+ launch) · [[tradeweb-ai-price]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[wss-credit-distressed]] · [[wss-trading-hedge-funds]] · [[bloomberg-terminal-instrumentation]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]] · [[canon-kahneman-sibony-sunstein-noise]]

---
### Rep
You're a buy-side trader selling $8mm of a bond with liquidity score 3. Using the paper's ~0.3 bp leakage for low-liquidity sells: (a) what's that in dollars on a bond with spread duration 7? (Hint: $ ≈ notional × duration × Δspread.) (b) How many basis points of price improvement would A2A need to win versus voice for A2A to still come out ahead? (c) One paragraph: why the paper cannot answer (b), and what data you'd pull from your own TCA to answer it.

*Answer for (a):* $8,000,000 × 7 × 0.00003 ≈ **$1,680**. That's the size of the effect — small per trade, real across a book.
