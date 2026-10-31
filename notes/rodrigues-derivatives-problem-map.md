# Derivatives & quant math, indexed by the problem each concept solves (André Luiz Rodrigues)

> **Sources:** 252 educational LinkedIn posts by **André Luiz Rodrigues** (Capital Markets Technology
> Director; mathematician, ~20 years building pricing and risk systems), pulled from his activity feed on
> 2026-10-31. The feed held 379 posts: 75 reposts of other authors, 1 duplicate and 51 greetings,
> certifications and announcements were dropped. Most posts carry a hand-drawn whiteboard with the
> equations (239 of 252 have a visual). Summarized in own words, not reproduced.
>
> **Raw corpus is local-only.** His posts and images are his copyrighted work and this repo is public, so
> the corpus and its reader live in `_ingest/raw/2026-10-31/linkedin/andre-rodrigues/`, which is
> **gitignored**. Open `index.html` there to read every post with its whiteboard, filtered by topic,
> problem and party. `posts.json` holds the same data with tags; `build.py` regenerates both from
> `feed_raw.json`.
>
> **Time window:** December 2025 to October 2026. Dates are approximate (worked out from LinkedIn's
> relative "3mo" labels).
>
> **Maps to:** **Course 02** (valuation: discounting and the risk-free curve under every DCF), **Course 07**
> (models, calibration, reading probabilities off prices), **Course 11 / E9** (rates, FX, emerging-market
> plumbing), **E2** (capital allocation: funding and capital cost), **E6** (crisis: 2008, negative rates,
> margin spirals), **E10** (AI and quantum in a regulated, model-heavy industry).
>
> ⚠ **Bias.** He is a builder of pricing and risk systems, so he frames most problems as *model or
> architecture* problems and under-weights incentives, politics and sales. Posts are written for
> LinkedIn reach: contrarian hooks ("Stop trusting N(d1)", "Stop summing your Vega") overstate the
> point, which is usually standard practitioner caution. A few posts on quantum computing and AI policy are
> more enthusiastic than evidenced. The historical failure cases in the map below are **added context
> from this note**, not claims from his posts.

---

## What this adds to the program

- **A derivatives layer the repo did not have.** [[wss-rates-macro]] covers bond math, DV01 and the
  curve from a rates salesperson's seat; [[wss-trading-hedge-funds]] covers options only as put/call
  ratios. Nothing in `notes/`, `learn/` or `GLOSSARY.md` explains *how a derivative is priced, risked,
  hedged and charged for credit and funding*. This corpus does, end to end, with the math on a whiteboard.
- **A problem-first index.** Topic labels ("options", "rates") say what a post is *about*. The tags here
  say what problem it *solves* and *for whom*, which is the question an MBA reader actually has.
- **The technologist's view.** His recurring claim is that pricing errors come from architecture more
  often than from math. That is the bridge to [[bloomberg-hub]], [[tradeweb-ai-price]] and the vendor
  economics in the company studies.

---

## The six problems every derivative position creates

Almost every concept he teaches answers one of six questions. They stack: each one assumes the one
above it is solved.

| # | Problem | Who has it | Concepts (his posts) | What goes wrong without it (added context) |
|---|---|---|---|---|
| **P1** | **Value it.** What is this contract worth today? | Dealers, funds, auditors, anyone who must mark a book | Risk-neutral pricing, discounting, curve building (SOFR, Fed Funds), Black-Scholes as a heat equation, PDE boundary conditions, Monte Carlo, trees | No agreed value means no trading, no accounting, no collateral. The LIBOR scandal forced a decade-long rebuild of the curves under ~$300tn of contracts. |
| **P2** | **Measure the risk.** How much do I lose if the market moves? | Trading desks, risk managers, regulators | Greeks and their failure modes, Taylor expansion of P&L, VaR and the "turkey problem", PCA on curves, Jacobians and gradients as sensitivities, risk attribution | Hidden exposure blows up in one day: short-volatility products in Feb 2018; JPMorgan's 2012 "London Whale," where a VaR model change understated risk. |
| **P3** | **Hedge it.** How do I neutralize a risk I don't want to own? | Corporates (exporters, importers), funds, the dealers who take the other side | Replication and forwards, option strategies as building blocks (spreads, condors, butterflies, diagonals), futures and NDFs, Brazil's synthetic onshore dollar | Hedges that are really bets. Sadia and Aracruz lost billions in 2008 on FX structures sold as protection. |
| **P4** | **Will they pay?** What if the other side defaults? | Banks with uncollateralized trades, CCPs | CVA/DVA and the XVA family, copulas and joint default (Li, Sklar), Poisson default intensities | 2008: banks lost more from marking counterparty risk (CVA) than from actual defaults, per the Basel Committee. Archegos (2021) repeated it. |
| **P5** | **Fund it.** Can I carry the position and meet the margin calls? | Bank treasury and XVA desks, pension funds, CCPs | FVA/MVA/KVA, funding curves, CDI/SELIC/SOFR as funding anchors, settlement conventions, stale pricing in private assets | Solvent but illiquid: the 2022 UK pension (LDI) crisis was a margin-call spiral, not a solvency problem. |
| **P6** | **Compute it.** Can the systems produce all of the above fast, consistently and explainably? | Bank technology, vendors, fintechs | Curve-engine architecture, numerical methods, physics-informed neural networks, neural curve fitting vs. Nelson-Siegel-Svensson, quantum computing | Two systems disagree on one trade; an overnight risk run misses its window; nobody can explain a P&L move. When rates went negative, models that assumed log-normal rates (Black-76) stopped producing prices. |

**How they chain.** You cannot hedge (P3) what you cannot measure (P2), and you cannot measure what you
cannot value (P1). **XVA is what P1 looks like once the clean assumptions fail**: it re-prices the trade
for P4 (default) and P5 (funding and capital). P6 sits under all of them, because every number above is
produced by a system.

### Where his posts concentrate (tag counts; a post can carry several problems)

| Problem | Posts | Banks & dealers | Corporates | Investors & funds | Regulators & infra | Tech & vendors |
|---|---|---|---|---|---|---|
| P1 Value it | 95 | 51 | 10 | 21 | 22 | 20 |
| P2 Measure the risk | 76 | 50 | 1 | 24 | 11 | 12 |
| P3 Hedge it | 93 | 70 | 9 | 18 | 29 | 6 |
| P4 Will they pay | 11 | 8 | 1 | 3 | 1 | 1 |
| P5 Fund it | 44 | 34 | 3 | 8 | 19 | 2 |
| P6 Compute it | 49 | 13 | 1 | 4 | 5 | 40 |

Read the gaps as much as the mass. **P4 (counterparty) has 11 posts** and the XVA thread only started in
October 2026, so pair it with an XVA textbook. **Corporates appear in only 13 posts**, almost all in the
Brazil series: he writes from the dealer's side of the trade.

Tags are keyword-based and meant as a starting index, not a verdict. 9 posts carry no problem tag.

---

## His series, read as short courses

He posts in sequences. Read in order, each one is a short course on one problem.

| Series | When | Problem | What it builds |
|---|---|---|---|
| **Math toolkit** | Jan 2026, Sep 2026 | P1, P2, P6 | Gradients, Jacobians, Hessians, optimization (gradient descent to metaheuristics), PCA, Taylor expansion, Fourier, Itô, Sklar. The sensitivities in P2 *are* these derivatives. |
| **Options as building blocks** | Mar–Apr 2026 | P3 | Covered call → protective put → verticals → calendars → diagonals → butterflies → condors → double diagonal. Each structure is a different bet on price, time or volatility. |
| **Greeks in practice** | Mar 2026 | P2 | Why delta-hedged books still lose, why summing vega across expiries is wrong, gamma near expiry (0DTE), theta as the price of gamma. |
| **Exotics** | May 2026 | P1, P3 | Single → double barriers, Asians, TARFs, accumulators, quantos, PRDCs. Path-dependence breaks closed-form pricing, which pushes you into P6. |
| **Curve building** | Aug 2026 | P1, P5, P6 | Fed Funds and SOFR curves, risk-free discounting, why curve construction is system design. |
| **Brazil onshore dollar** | Oct 2026 | P3, P5 | Why a non-convertible currency forces a separate onshore dollar curve (cupom cambial), and the instruments that trade it (DDI, FRC, NDFs, CDI swaps). How a local bank absorbs an exporter's hedge. |
| **Rates when models break** | Oct 2026 | P1, P6 | Negative rates vs. log-normal models, inflation linkers, curve-slope trades and the hedge ratios that keep them direction-neutral. |
| **XVA** | Oct 2026 (ongoing) | P4, P5 | Why pre-2008 pricing assumed risk-free funding and safe counterparties; CVA, then DVA and its "phantom profit" paradox. |
| **AI and quantum in finance** | Dec 2025–Feb 2026, Oct 2026 | P6 | Transformers and BERT vs. GPT, PINNs that respect no-arbitrage, neural nets vs. parametric curves, quantum algorithms and the encryption threat. |

---

## Where the problems are still open (the MBA angle)

P1–P3 are largely solved for large banks; the money and the friction are in P4–P6 and in the
under-served parties.

1. **XVA compute cost (P4–P6).** XVA needs portfolio-wide Monte Carlo across every counterparty and
   scenario. Banks spend on GPUs, algorithmic differentiation and neural approximations of slow pricers
   (his PINN and neural-curve posts). This is the vendor wedge for [[bloomberg-hub]]-style platforms.
2. **Mid-market corporate hedging (P3).** The Brazil series shows a local dealer manufacturing dollar
   liquidity for an exporter. The exporter usually cannot evaluate what it bought, and 2008 showed the cost.
   Hedge transparency for mid-size treasurers is an open product problem. See [[tradeweb-derivatives-regulation]].
3. **Consistency and explainability (P6).** Front office, risk and finance often run separate engines
   that disagree. His "bad architecture, not bad math" claim is the thesis; regulators asking for every
   number to be explained is the forcing function.
4. **Liquidity under stress (P5).** Margin spirals (LDI 2022, March 2020) show funding risk is
   under-modeled outside large banks. His private-markets post adds the mirror image: smoothed private
   marks hide volatility until a liquidity event forces a real price ([[wss-private-markets-wealth]]).

---

## Suggested reading path

1. **Math toolkit** posts, alongside the textbooks: Hull, *Options, Futures, and Other Derivatives*, for
   P1–P3; Shreve, *Stochastic Calculus for Finance*, for the notation on his whiteboards.
2. **Options as building blocks**, then **Greeks in practice** (P3 → P2).
3. **Curve building**, then **Rates when models break** (P1 at its foundation).
4. **Exotics**, then **Numerical methods** (where P1 forces P6).
5. **XVA** with Gregory, *The xVA Challenge* (P4–P5; his coverage is thin here).
6. **Brazil onshore dollar** as a case study of all six problems at once inside one market.
7. **AI and quantum** last, as a view on where P6 is heading.

Each step pairs with one buildable exercise for `quant-backtesting/` or an Acumen case: a SOFR curve
bootstrapper (P1), a Black-Scholes pricer with Greeks and a Taylor P&L explain (P2), a delta-hedging
simulation that shows hedge slippage (P3), a barrier option by Monte Carlo vs. PDE (P6), and a one-netting-set CVA (P4).
[[fourier-use-cases]] already has a Fourier pricing demo that matches his Fourier posts.

---

## Links

[[wss-rates-macro]] [[wss-credit-distressed]] [[wss-trading-hedge-funds]] [[wss-private-markets-wealth]]
[[trading-floor-mechanics]] [[tradeweb-derivatives-regulation]] [[fourier-use-cases]]
[[canon-taleb-black-swan]] (VaR and the turkey problem) [[canon-taleb-antifragile]]
[[canon-tetlock-superforecasting]] (models as maps, not truth)

## Gaps

- **Counterparty and funding (P4, P5) are thin:** 11 and 44 posts. XVA started in October 2026 and is
  ongoing; re-pull in a few months.
- **No permalinks:** the activity feed did not expose links for most posts, so posts are referenced by
  series and topic, not URL.
- **Images are capped at the sizes LinkedIn served** (mostly 1280px, a few at 160–480px).
- **Tags are keyword-based.** Spot-checked, not hand-labeled; expect some posts in a neighbouring bucket.
