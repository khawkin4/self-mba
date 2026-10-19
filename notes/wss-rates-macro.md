# Rates & macro: how the price of money is set, moved and transmitted (Wall Street Skinny)

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-capital-markets-ma]] [[wss-credit-distressed]] [[wss-private-markets-wealth]] [[wss-technicals-career]] [[wss-trading-hedge-funds]]

> **Sources:** 84 transcripts read from the `rates-macro` cluster across two passes; 77 used (33 long
> videos, 44 shorts), from *The Wall Street Skinny* (Jen Saarbach, a decade as a rates specialist at Morgan Stanley / Lehman /
> Barclays; Kristen Kelly, ex-Morgan Stanley IBD). Guests whose material is used: **Mike Medeiros**
> (Head of US Macro, Wellington; two episodes, Jan 2026 and Sep 2026), **Elizabeth Burton** (Chief
> Strategist, Fortress), **Alicia Levine** (BNY Wealth), **Guy Adami** (CNBC / RiskReversal), an oil
> and shipping trading CEO, and a 90-second Q&A clip with **Treasury Secretary Scott Bessent**. Pass 2
> adds **Matt Hornbach** (global head of macro strategy, Morgan Stanley; Sep 2025), **John Normand**
> (ex-JPM cross-asset strategy, now AustralianSuper; 2024), **Jamie Patton** (co-head of global rates,
> TCW; Sep 2024), **Steve Eisman** (*The Big Short*; Apr 2025) and **Ashish Goyal** (global macro PM;
> 2024), plus the hosts' own emergency episodes on the April 2025 tariff panic, the basis trade, Fed
> independence and the end of QT. One short from the `culture-other` cluster (`GbZpAPJwCdY`, on reserves and the 2019 repo spike) is borrowed
> for §7. Raw at `_ingest/raw/2026-10-04/media/wall-street-skinny/`. Seven cluster files had nothing on
> rates (a pay survey, a SPAC breakdown, a PE leverage episode, career shorts, an ad) and are only
> skimmed; seven pass-2 files added nothing new (listed under Gaps).
>
> **Time window:** mostly April 2025 (tariff panic) to September 2026 (the first Warsh hike), with
> earlier anchors (the LIBOR end in July 2023, 2023 "101" episodes, Normand and Goyal in 2024, the Sep
> 2024 first cut). The transcripts follow one cycle all the way through, and that cycle is the note's spine: Powell cuts → Iran-war oil
> shock → chair transition → Bessent buybacks → hike. Dates are worked out from the episodes; figures are
> as stated on air.
>
> **Maps to:** **Course 11** (Global Strategy & Macro: this note is the rates layer the
> [core-11 lesson](../lessons/core-11-global-macro.html) points to but never builds), **E9**
> (Geopolitics & Macro: the [E9 lesson](../lessons/exec-E9-geopolitics-macro.html) traces
> chokepoint → oil → inflation → rates → assets and then stops; this note picks up from "rates"),
> **Course 02** (the 10-year is the risk-free input to every DCF), **E2** (capital allocation: funding
> cost, duration of liabilities), **Course 07** (reading probabilities off prices).
>
> ⚠ **Bias:** both hosts are ex-sell-side, and Jen's training shows. She is good on mechanics, quick to
> call something a crisis, and she *labels* her own speculation ("conspiracy corner"); the note keeps
> those labels. In April 2025 she calls herself the "leader of the panicking party," and the note airs
> Eisman's calm counter-case alongside. Two segments are **paid ads** (the Public.com bond account behind the 6.7% corporate-bond
> examples; Ground News), so read their framing as marketing even where the arithmetic is right. Medeiros
> works at a long-only asset manager and argued "not restrictive / sell bonds" consistently across both
> appearances. Hornbach runs sell-side strategy; Patton was long duration at TCW when she argued that
> cuts transmit weakly; Normand works for a pension fund and argues stay-invested. Burton runs strategy at a credit shop and argues that the risk is in PE, not credit. The
> hosts clearly admire Bessent and Warsh, so policy-maker motives get a charitable reading. Several stated
> figures are wrong or dated; each one is flagged where it appears.

---

## What this adds to the program

- **A rates layer the repo did not have.** `GLOSSARY.md`, `learn/` and `notes/` contain nothing on bond
  math, duration, the yield curve, the Fed's machinery or Treasury debt management. Core-11 teaches
  country risk and scenario planning, and E9 stops at "the Fed looks less likely to cut." This note
  supplies the next link in the chain: *how* a policy rate, a bond auction or a buyback reprices a
  mortgage, a corporate bond or a DCF.
- **The practitioner conversion factor.** Bond P&L is duration × Δyield × notional, and desks size
  trades in **DV01** (dollars per basis point), not in notional. With that one idea you can read every
  "macro fund blew up" headline.
- **Fed ≠ Treasury ≠ GSEs.** There are three separate levers on long rates: Fed QE, Treasury buybacks
  and issuance mix, and Fannie/Freddie MBS buying. In 2026 they pointed in *different directions*. That
  split is the most useful framework in the cluster and the one the media got most wrong.
- **Reading probabilities off prices.** The fed-funds-futures arithmetic behind "68% chance of a hike"
  is worked in full. It applies Course 07 and [[canon-tetlock-superforecasting]] to a market that sets
  the price of money.
- **The plumbing behind "the bond market broke."** Cash vs. futures vs. swaps, why futures trade rich,
  how the basis trade levers that gap, why swap spreads are negative, and what LIBOR → SOFR changed (§10,
  §11). [[wss-trading-hedge-funds]] covers the same basis trade from the fund seat.
- **Carry and tariffs as rate stories.** The yen carry trade (§15) and the April 2025 episode in which
  tariffs made Treasuries, stocks and the dollar fall together (§16), with Eisman's counter-case.
- **A dated case study of institutional stress.** It covers a chair transition, a criminal probe of a
  sitting chair, a hawkish appointee who surprised everyone, and the Taylor-rule framework for
  measuring "independence" with a number rather than adjectives.

---

## Concept map

| # | Concept | One line | Why it matters to a business | In repo? |
|---|---|---|---|---|
| 1 | Bond price/yield & the yield stack | Yield = risk-free rate + credit spread; price moves opposite to yield | It is your borrowing cost, and it moves for two separate reasons | partial (core-11 risk-free/CDS cards) |
| 2 | Duration, DV01, convexity | A conversion factor from a rate move to a dollar P&L | Sizes interest-rate risk on any asset or liability | n |
| 3 | Yield curve, term premium, curve trades | The price of money at each maturity, and bets on its shape | The Fed sets one point; you borrow at the others | n |
| 4 | FOMC & market-implied odds | A 12-vote committee sets an overnight range; futures price its path | Tells you what is already priced in before you act | n |
| 5 | Neutral rate, Taylor rule, financial conditions | Is policy actually tight? Measure it, don't assert it | Separates "rates are high" from "rates are restrictive" | n |
| 6 | Fed independence & the "third mandate" | Political pressure to fund the government cheaply | It decides whether the long end trusts the central bank | n |
| 7 | QE vs QT vs reserve management | The Fed's balance sheet as a second policy tool, and its plumbing | Long rates, mortgage rates and funding stress | n |
| 8 | Treasury auctions & who buys | How $-trillions of debt is sold, and the new bill buyers | Auction results move the whole curve in minutes | n |
| 9 | Treasury buybacks & debt management | The Treasury reshaping its own debt | A quiet lever on long yields, distinct from QE | n |
| 10 | Repo, SOFR, swaps, swap spreads | Funding, and the synthetic bond that lets you skip it | Every floating-rate loan and every hedge prices here | n |
| 11 | Treasury futures, CTD, basis trade | Exchange-traded duration, its DV01, and the levered cash-futures arbitrage | Liquidity in the risk-free market depends on levered funds | partial ([[wss-trading-hedge-funds]] §9; GLOSSARY "Basis trade") |
| 12 | Mortgage-rate drivers & housing policy | 30y mortgage ≈ 10y Treasury + spread, not the 30y | Explains why Fed cuts don't lower mortgage rates | n |
| 13 | Inflation measurement & pass-through | CPI vs PCE, base effects, real vs nominal, breakevens | The input that drives the Fed's reaction function | partial (E9 oil→inflation chain) |
| 14 | FX & the dollar | Rate differentials, pegs, hedging costs, the dollar as relief valve | Imported costs, foreign demand for your debt | partial (E9 tariffs) |
| 15 | Carry & the yen carry trade | Borrow cheap money, own expensive money, until the elevator drops | FX gaps can erase an asset's return in a quarter | n |
| 16 | Tariffs & the April 2025 safe-haven break | Who pays a tariff, the reciprocal formula, and why Treasuries fell with stocks | Input costs, and proof the risk-free rate has a credibility term | partial (E9 tariffs) |
| 17 | Recession indicators | The curve, payroll breakevens, and the folklore | When to de-risk, and when *not* to | n |

---

## 1 · Bond price/yield and the yield stack

**What it is.** A bond is a loan. You pay a price today and receive fixed coupons plus principal later.
The **yield** is the return those fixed cash flows imply at today's price, so when market yields rise
the price of an existing bond falls, and the reverse. For a company, the yield it pays splits into two
parts: a **risk-free rate** (the Treasury yield of the same maturity) plus a **credit spread**, which
compensates the lender for the chance the company doesn't pay.

**How it works.** The hosts' figures (Public bond-account ad, 2024): a 5-year Treasury at **5%** plus a
**170bp** spread gives a **6.7%** corporate yield. Two separate things can make you money:
- *Rates rally:* the risk-free part falls and every fixed-rate bond gains (sized in §2).
- *Spreads tighten:* Treasuries stay at 5% but the spread compresses 170 → 150bp, so new bonds price at
  6.5% and your locked-in 6.7% bond is worth more. You gain with no change in Fed policy.

The tariff short shows the other direction: Treasuries at **4%** + 150bp = **5.5%**, and tariffs widen
the spread. The channel is **covenants**. With $400mm of debt and $100mm of EBITDA, leverage is
400/100 = **4.0×**, inside a 6× maintenance covenant. If tariffs halve EBITDA to $50mm, leverage becomes
400/50 = **8.0×** and the covenant is breached *without borrowing another dollar*.

**Business significance.** Every corporate borrowing decision reflects both legs. A CFO who watches only
the Fed misses half the cost. In April 2025 Treasury yields fell (a flight to safety) while corporate
all-in costs *rose*, because the spread leg widened more than the base leg fell. The hosts' summary:
what's good for the US government is not necessarily good for companies.

**Forces & impact.** The base rate follows policy expectations, inflation and term premium (§3). The
spread follows default risk, which is driven by input costs, demand, and how close covenants are to
tripping. It also follows **demand for income**: in August 2025 IG spreads were at 30-year tights despite
tariff uncertainty, and Jen calls it a "cash trap". With rate cuts priced in, few IPO exits, and equities
"priced on the moon", money has nowhere to go except high-grade bonds, which compresses spreads.
Second-order effect: tight spreads remove the cushion, so repricing comes "up by the stairs, down by the
elevator shaft."

**With vs. without.** Without a separate credit spread, every borrower would pay the sovereign rate and
lenders would have no price at which to take default risk. Credit would then be rationed by
relationship, not price, which is roughly how bank lending worked before deep bond markets. When the
mechanism breaks (spreads gap wider all at once), refinancing windows close, and the companies that
most need to roll debt are shut out first.

**Applies when / Breaks when.** The decomposition holds whenever a liquid sovereign curve exists. It
breaks when the "risk-free" leg itself carries risk (§6: the US is rated AA, below Microsoft and J&J,
which the hosts point out), or when spreads are too tight to carry information. Burton's point is that
OAS and the MOVE index can tell contradictory stories in the same week.

**Channel example.** *Tariff Fallout: Why Are Credit Spreads Widening?* (short); *How Does Investing in
Corporate Bonds Work?* (short, ad); *Chamath's New SPAC… The Fed vs. FOMC* (Aug 2025, 30-year-tight
spreads); *Oracle CDS: the "Anti-AI Trade"* (Nov 2025: Oracle CDS wider by ~95bp versus a modest move in
CDX IG, which made Oracle the market's chosen hedge against AI).

**Counterpoint.** The 6.7%-yield examples are ad copy, and a 10-bond "IG and high-yield" basket is not
risk-free carry. The covenant example assumes maintenance covenants. Much 2021–25 issuance was
covenant-lite, which, as Medeiros notes, is itself a late-cycle sign.

**Links.** [[canon-klarman-margin-of-safety]] (reaching for yield = no margin) ·
[core-11 lesson](../lessons/core-11-global-macro.html) (sovereign CDS, risk-free rate) · the sibling
[[wss-credit-distressed]] for private credit and PIK.

---

## 2 · Duration, DV01 and convexity

**What it is.** If an oil stock rises 1%, you make 1%. Bonds don't work that way. **Duration** converts
a change in yield into a percentage change in price; textbook-wise it is the weighted-average time to
get your money back. A 10-year zero-coupon bond has duration 10. A 10-year coupon bond pays cash
earlier, so its duration is lower (~8). **DV01** ("dollar value of an 01") is the same idea in dollars:
how much you make or lose per one-basis-point move. **Convexity** is the curvature that duration's
straight line misses.

**How it works.** Rule of thumb: **P&L ≈ −duration × Δyield × notional.**
- *The blackjack-table framing* (DV01 short): before you sit down you pick the $10 table or the $1,000
  table. Duration is how a trader picks the table. A 10-year Treasury with a 5% semi-annual coupon has
  duration ~**7.5** (a 10-year zero would be 10). On **$100mm**, a 1bp rally (5.00% → 4.99%) earns
  7.5 × 0.0001 × $100mm = **$75,000**.
- *Sizing runs the formula backwards:* a trader who wants "$100k per bp" buys $100,000 / (7.5 × 0.0001)
  = **~$133mm** of 10s. Conviction is expressed in DV01; the notional is whatever falls out.
- *The issuer's side of the same number* (Apr 2025): a **$25B** 10-year auction carries roughly
  $25B × 7.5 × 0.0001 = **$18.75mm per bp**. A 50bp backup into an auction is therefore close to
  **$1B** of extra present-value interest cost to the Treasury on one auction alone.
- *$1,000 corporate bond, duration 4.3* (Public ad): each 1bp move is worth 4.3bp of price, or **$0.43**
  per $1,000. Yields fall 100bp (6.7% → 5.7%), so the gain ≈ 4.3 × 1.00% × $1,000 = **$43**, a little
  more in practice because of convexity.
- *Convexity, intuitively* (Public ad, short): in the duration formula the yield sits in the
  denominator. When yields fall to 5.7%, you divide by a smaller number, so duration rises (say 4.3 →
  4.4): you make money *faster* as rates rally. When yields rise, duration shrinks: you lose money
  *more slowly*. That curved price-yield line is **positive convexity**, and it is a property of
  option-free bonds.
- *A dealer's DV01 gone wrong* (short, Feb–Mar 2020): a trader facilitated a client who sold **$2.6B**
  of long bonds, hedged by going short, and was then never delivered the bonds. The position carried
  ~**$4.2mm DV01**; as COVID hit, long bonds rallied ~50bp instead of selling off, and 4.2 × 50 ≈
  **$210mm**, with the hosts putting the final loss near **$250mm**. A "flat" market maker can lose a
  quarter of a billion dollars when the risk it thought was hedged is not.
- *Iran war, March 2026, two traders each long $100mm* (DV01 short):
  - 2-year: yield 3.40% → 4.00% (+60bp), duration 1.8 → 1.8 × 0.60% × $100mm ≈ **−$1.1mm**
  - 10-year: 3.96% → 4.45% (+~50bp), duration 8 → 8 × 0.50% × $100mm = **−$4.0mm**

  The smaller yield move lost nearly 4× more money. This is why desks **flip the question**. They don't
  ask "how much did $100mm lose?" They ask "how many bonds give me $100k per bp?" A fund that wants
  "$1mm per bp" ends up with enormous notionals, and the hosts' tagline was that this is why the Iran
  war blew up macro funds.

**Business significance.** Duration is the unit of interest-rate risk on *both* sides of a balance
sheet: a pension's liabilities, a bank's securities book (SVB's 2023 failure was a duration mismatch),
an insurer's annuities, a homeowner's fixed mortgage. Matching DV01 is how a CFO hedges a planned bond
issue. It is also how a "duration-weighted" curve trade (§3) becomes indifferent to the level of rates.

**Forces & impact.** Duration rises as coupon falls, maturity lengthens and yields drop, so low-rate
eras manufacture duration risk. The 1.375% Aug-2050 Treasury issued in 2020 trades near **46 cents on
the dollar** (§9) because its duration was huge when rates rose 400bp. Second order: when everyone
sizes in DV01, a vol spike forces simultaneous de-risking across funds.

**With vs. without.** Without a duration-type conversion, a "$100mm 2-year" and a "$100mm 10-year" look
like the same risk. Sizing by notional systematically under-hedges long bonds and over-hedges short
ones. Convexity is the tell when the approximation fails: mortgages have **negative convexity** (§12)
because borrowers refinance when rates fall, so the holder's gains are capped while losses aren't.

**Applies when / Breaks when.** Duration works for small parallel moves in option-free bonds. It breaks
for large moves (convexity dominates), for bonds with embedded options (callables, MBS), and for
non-parallel curve moves, which is why §12 uses *partial* (key-rate) durations.

**Channel example.** *Duration & DV01: the best explanation of the magic conversion factor* (short,
Mar 2026); *What is "DV01" and how is it used? An intuitive explanation* (short); *Convexity Intuition
Explained* (short, Public ad); *How do bonds work?* (Public ad, 2024); *Ferrari Loving Trader Cost Wall
Street a Quarter Billion Dollars* (short); *It Wasn't Equity Turmoil That Spooked Trump* (Apr 2025,
auction DV01).

**Counterpoint.** The shorts loosely conflate modified duration and DV01. Strictly, DV01 = modified
duration × price × 0.0001, a dollar figure, not a percentage; the futures video (§11) gets the
Macaulay → modified → dollar sequence right. "Blew up because of duration" is also incomplete: the
losses came from leverage *on* duration plus crowded curve positioning (§3). **Likely error in the
Ferrari short:** it puts long-bond yields at ~3.72% in Feb 2020 falling to ~3.2%. The 30-year was
nearer **2.0% → 1.2%** over that window, so the bp move was larger than stated and the yield levels are
wrong; the order of magnitude of the loss is still plausible. The auction "$1B" is a present-value
cost to the issuer only if the Treasury could otherwise have sold at the pre-backup yield.

**Links.** [[canon-taleb-antifragile]] (convexity as the shape of payoffs; negative convexity = fragile)
· [[canon-perrow-normal-accidents]] (tightly coupled, uniformly sized risk) · Course 02 (discounting is
the same math run in reverse).

---

## 3 · Yield curve, term premium, and curve trades

**What it is.** The **yield curve** plots yields from overnight to 30 years. Normally it slopes upward,
because lending for longer means more opportunity cost, more inflation risk and (for non-sovereigns)
more default risk. The extra yield for duration is the **term premium**. A **curve trade** bets on the
*shape* of the curve rather than its level.

**How it works.**
- *Normal vs. inverted:* 2s at 4.00% and 10s at 4.50% is a +50bp normal curve. 2s at 4.50% and 10s at
  4.00% is a −50bp inversion.
- *Steepener:* buy 2s, sell 10s, duration-weighted so a parallel move is P&L-neutral. You profit if the
  spread widens. A **bull steepener** comes from the front end rallying (the Fed cuts). A **bear
  steepener** comes from the long end selling off (fiscal or inflation fear). The **flatteners** are
  the mirror images.
- *2025, US:* after the "One Big Beautiful Bill", the curve steepened, but **bull**, with 2s falling on
  cut expectations, not 30s rising. *Europe at the same time:* the ECB cut ~8 times (~200bp total) and
  long-end Bund/OAT/Gilt yields *rose*, a **bear** steepener driven by term premium on fiscal
  expansion. The policy rate and the long end can move in opposite directions.
- *Sep 2024, the dovish cut that steepened the wrong way* (Jamie Patton, TCW): pricing was split
  ~50/50 between 25 and 50bp; the Fed went 50 but the dots kept the *total* easing unchanged, only
  front-loaded. Faster-but-not-bigger easing should not rally the long end, so 2s rallied, 10s sold off
  (a **bear steepener**) and mortgage borrowers got nothing.
- *Sep 2025, carry as rent* (Matt Hornbach, Morgan Stanley): the one thing to watch for the curve is
  the Fed, because cuts pull short rates down more than long rates. The 2025 steepening was a **bull**
  steepener on that pattern. Carry is "the rent you pay" to hold a position; a steepener is a
  **negative-carry** trade, so Morgan Stanley chose **3s/30s in Treasuries** to keep the rent low (the
  SOFR swap version cost more, §10) and to avoid paying for timing it could not control.
- *Aug 2025, steepening from both ends:* the attempt to fire Governor Cook produced a bull move at the
  front (more cuts) and a bear move at the long end (less discipline) at the same time.
- *2026:* "long steepeners" was the consensus trade going into the year. The curve had been a "Nike
  swoosh" (funds 3.50–3.75%, a dip to ~3⅜% at 2 years, then up). The March Iran-war oil shock turned
  one priced cut into ~two priced *hikes* and the curve **bear-flattened** globally, which "carted
  everybody out" (Jen); Caxton reportedly lost ~**$1.3B** on long-gilt steepeners. After the September
  Warsh hike the curve bear-flattened again: 2s and 5s rose, and 30s held.

**Business significance.** The Fed sets one point. Companies, homeowners and governments borrow
everywhere else on the curve. Banks earn the slope, borrowing short and lending long, so a flattening
curve hits bank equities even when the Fed hikes (Medeiros, Sep 2026). Issuers choose a tenor by reading
the curve: term out when long rates are cheap, stay short when the curve is steep.

**Forces & impact.** The front end follows policy expectations. The long end follows growth, inflation
expectations, term premium, supply, and credibility (§6). Medeiros's structural case for steepening is
fiscal: public debt replaced private debt after 2008, so the *private* economy is less rate-sensitive
(private debt-service ratios near 30-year lows) while the *public* balance sheet is more exposed. Global
long ends are rising together. US 30s held above 5% for the longest stretch since 2007. German 30s
underperformed US 30s over 12 months. Term premium rose *most in the countries that cut most* while
inflation was still above target. Dutch pension reform removes a structural receiver of long-dated
swaps, and the hosts cite an estimate of **~$20mm DV01** of effective paying as those positions unwind.

**With vs. without.** Without a term structure there is one price for all money, so a 30-year factory
gets financed as if it were an overnight loan, and nobody is paid to hold duration. When the long end
"comes unglued", as with Gilts in 2022 or US Treasuries in April 2025 ("essentially bidless for three
or four weeks", Medeiros), mortgage rates, corporate long-bond costs and the government's own interest
bill all reprice at once, whatever the central bank does.

**Applies when / Breaks when.** Curve trades work when the macro driver is identified correctly: a
bull steepener needs cuts, a bear steepener needs a fiscal or inflation scare. They break on crowding.
When everyone holds the same steepener, a labor-market surprise that prices *out* cuts bear-flattens
the curve and stops everyone out at once (Medeiros's Jan 2026 warning, which came true in March).

**Channel example.** *What is a yield curve steepener?* (short); *From Fixed Income Sales to the Buy
Side feat. Jamie Patton* (Sep 2024); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025); *Is
This the End of the Federal Reserve?* (Aug 2025); *Chamath's New SPAC… Europe's Yield Curve Warning*
(Aug 2025); *Head of US Macro at $1 Trillion Firm: 4 Forces…* (Jan 2026); *Wall Street is Watching
Something More Concerning than Oil* (Mar 2026); *Why Stocks Could Drop 10% Before Year-End* (Sep 2026).

**Counterpoint.** "Term premium" is model-dependent (ACM vs. Kim-Wright estimates differ) and is often
used as a residual name for "whatever we can't explain." Medeiros's "countries that cut most saw the
largest term-premium rise" is a correlation across a handful of countries, and fiscal expansion is a
plausible common cause.

**Links.** [[canon-meadows-thinking-in-systems]] (front end = policy stock, long end = expectations
loop) · [[canon-sterman-business-dynamics]] (delays: curve signals lead the real economy by 18–36
months, see §17).

---

## 4 · The FOMC and market-implied rate odds

**What it is.** "Fed" is short for Federal Reserve, not an acronym. The acronym is **FOMC**, the Federal
Open Market Committee, which votes by majority to set a **target range** for the overnight rate at which
banks lend reserves to each other. The chair leads the messaging but has **no veto**. The fed funds
futures market turns traders' bets on those votes into prices, and therefore into probabilities.

**How it works.**
- *Composition (as the hosts gave it):* 12 voters out of 19 participants. The 7 Board governors serve
  14-year terms, the chair (also a governor) a renewable 4-year term as chair, and regional bank
  presidents rotate in. The **dot plot** (Summary of Economic Projections) shows each participant's
  rate path anonymously.
- *Futures arithmetic* (short, Sep 2026, target 3.50–3.75%, effective rate **3.63%**, meeting on the
  16th of a 30-day month):
  - The contract settles to the month's average effective rate, so implied rate = 100 − price =
    100 − 96.29 = **3.71%**
  - Known days: 16 at 3.63. Solve for the post-meeting rate: (30 × 3.71 − 16 × 3.63) / 14 =
    (111.30 − 58.08) / 14 = **3.80%**
  - Expected change: 3.80 − 3.63 = 17bp; 17 / 25 = **68%** odds of a 25bp hike
  - Year-end: the January contract (no meeting until late January, so it captures December's
    decision) implies 4.10%, and (4.10 − 3.63) / 0.25 = **1.88 hikes** priced
- *Outcome:* the FOMC hiked 25bp to **3.75–4.00%**, unanimously. It was ~90% priced by meeting day after
  a hot CPI (Medeiros).
- *Who can be appointed, and why it matters* (Aug 2025 emergency episode): all 12 regional presidents'
  5-year terms expire together on **Feb 28, 2026**, and presidents need Board approval. Control a Board
  majority (Waller, Bowman, Miran in Kugler's seat, plus Cook's seat if she could be removed = 4 of 7)
  and you influence who the presidents are, and therefore the whole committee.
- *Reading the package, not the headline* (Hornbach, Sep 2025 cut): the median dot moved to 75bp of
  2025 cuts, a dovish first read, but only on a razor's edge; the only dissent was Miran (for 50), not
  Waller or Bowman. The SEP put Q4 unemployment at an *average* of **4.5%** against 4.3% at the time, which
  implies a December print near 4.6%, yet showed only one 2026 cut. Hornbach found that hard to square.
- *Forward guidance trumps the move* (Patton, Sep 2024): the market trades the Fed's action *versus
  what was priced* and the path the dots imply. A 50bp cut with unchanged total easing read as "bigger
  now, slower later."
- *Fed-day craft:* desks diff the new statement against the old one word by word ("may" vs "will",
  where the comma sits), then trade the press conference separately; under Powell the two often gave
  opposite vibes (Hornbach, Jen).

**Business significance.** Every floating-rate borrower (SOFR loans, credit cards, leveraged loans)
reprices off this rate. More important, the *pricing* tells you what is already in the market. A CFO
deciding whether to lock a rate is trading against the futures-implied path, not against the headline.
Two days before Warsh's first meeting, a 25bp hike was priced, so the move itself carried little
information. The surprise was in the *guidance* (one more hike signaled, versus three priced).

**Forces & impact.** The dual mandate (maximum employment, ~2% inflation) drives the reaction function.
Communication is a policy tool in its own right. Powell ran an open Fed, with dots, frequent speeches and
public dissent. Jen argues this lowered event-day risk but added noise, because his press conferences
sometimes contradicted the statement. **Warsh wants the opposite**: "do less", fewer forward-guidance
crutches, disagreements settled behind closed doors before a unified statement. The second-order effect
Jen derives from option pricing: if all information arrives on FOMC days, those days need higher
**event-day variance weighting** in short-dated options. Medeiros (Sep 2026) adds that forward guidance
is a zero-lower-bound tool and doesn't fit 3%-plus inflation, so front-end vol should rise structurally.

**With vs. without.** Without futures, "what's priced" is guesswork assembled from surveys and pundits.
With them, any reader can extract a market probability in three lines of arithmetic. Without a
committee structure, a single appointee could set rates, which is the fear behind the 2025–26
independence fight (§6). The committee is the main reason one dovish appointee (Miran) could only
dissent, not cut.

**Applies when / Breaks when.** The arithmetic assumes 25bp increments, a stable effective rate inside
the range, and no term or risk premium in the futures price. It breaks around liquidity events, when the
effective rate drifts within the range (§7), and for far-dated contracts, where risk premia blur
"expectation" into "price."

**Channel example.** *Will the Fed hike rates? Wall Street trading demystified* (short, Sep 2026); *Is
This the End of the Federal Reserve? Emergency Episode* (Aug 2025); *Fixed Income Strategy 101 feat.
Matt Hornbach* (Sep 2025); *From Fixed Income Sales to the Buy Side feat. Jamie Patton* (Sep 2024); *Who
truly controls interest rate cuts* (short); *Every New Fed Chair Has Crashed the Market* (Apr 30 2026:
4 dissents at Powell's last meeting, Miran dovish; Hammack, Logan and Kashkari objecting to easing
language); *Trump's new Fed chair shocks the market* (short, Warsh's first FOMC: "we will deliver price
stability", yet rates sold off only ~8bp because, as Jen put it, anyone listening to his actual words
expected it).

**Counterpoint.** **Inconsistency across episodes:** in one 2026 episode the hosts count 7 governors + 4
rotating presidents = 11. The Aug 2025 episode gets it right: the 12th voter is the **New York Fed
president, a permanent voter**. That episode also says the dot plot projects "five years" out; it covers
the current and next 2–3 year-ends plus a longer-run dot. The press's "most dissents since 1992" was
disputed on air by the hosts themselves. And "68% chance" is a risk-neutral price, not a forecast. It
embeds hedging demand, which is the gap between market odds and real odds that
[[canon-tetlock-superforecasting]] warns about.

**Links.** [[canon-allison-essence-of-decision]] (the FOMC as an organizational and bureaucratic-politics
actor, not a unitary rational one) · [[canon-schelling-strategy-of-conflict]] (forward guidance as a
coordinating focal point; Warsh's withdrawal of it) · [[canon-tetlock-superforecasting]].

---

## 5 · Neutral rate, the Taylor rule, and financial conditions

**What it is.** The **neutral rate (r\*)** is the policy rate that is "not too hot, not too cold". It
keeps nominal growth stable with no inflation or employment pressure. Nobody observes it. The **Taylor
rule** is a formula that outputs where policy "should" be from r\*, the inflation gap and the
unemployment gap. **Financial conditions** (stocks, credit spreads, the dollar, long yields) are the
channel through which the policy rate reaches the real economy.

**How it works.** Medeiros's two cross-checks:
- *Jan 2026:* the 10-year at ~**4.15%** versus Q3 nominal GDP growth of **~8%**, nearly 300bp below.
  Borrowing costs far below the economy's nominal growth rate are not restrictive. Policy is loose.
- *Jan 2026, independence gauge:* the policy rate was ~**150bp** below the Taylor rule, which is within
  history. The 1970s averaged 200–300bp below, and Japan in 2026 was ~200–250bp below.
- *Sep 2026:* the gap had widened to ~**200bp**. Warsh said three times that financial conditions were
  too loose. Medeiros maps one more hike before year-end to **5–10% lower** S&P, as conditions tighten
  to close the gap.
- *Nobody knows r\*:* in Sep 2024 the FOMC's longer-run dots ranged from **2.375% to 3.75%**, with no
  more than three participants at any level. Patton's image: 19 pilots promising a soft landing who
  can't agree on the runway's elevation.
- *Hornbach's R − G rule for risk assets:* in a Gordon-growth framing, the discount rate on future cash
  flows is the **real rate minus growth expectations**. If real rates rise and growth expectations rise
  by the same amount, the discount rate is unchanged and equities need not fall. In Sep 2025 real rates
  were inching down while growth expectations rose, which he offered as the reason stocks kept going up.
- *When cheap credit doesn't bite:* Hornbach's formative read in Japan was Richard Koo's **balance-sheet
  recession**. Lowering the *price* of credit need not raise *demand* for it if borrowers are
  structurally insolvent and using cash flow to repay debt (Japanese corporates in the 1990s; US
  households after 2008). That view made him a long-running Treasury bull after the GFC.
- *Demand as evidence:* record IG issuance at the tights and hyperscaler debt absorbed at higher yields
  means rates have not yet found the level that bites. Price discovery continues until demand breaks.

**Business significance.** "Rates are high" and "rates are restrictive" are different claims. A 4% 10-year
with 8% nominal growth means revenue grows faster than funding costs, which is supportive of leverage,
capex and equity multiples. Treating level as tightness was the 2023–25 consensus error behind the
recession calls that "never happened" (Levine).

**Forces & impact.** Medeiros argues r\* is higher than the 2010s because of fiscal deficits, AI capex,
deregulation (~0.5% of GDP) and a labor force shrinking as immigration reverses. When policy stays
below rule-implied levels, the short-run effect is good for stocks. The longer-run reflex runs through
the long end and the **dollar, "the relief valve"**, and then into inflation expectations.

**With vs. without.** Without a rule-based yardstick, "Fed independence" and "tight policy" remain
adjectives argued along partisan lines. With one, you can rank countries by the gap and position
accordingly. Medeiros's mentor's rule: *buy the long end of central banks guarding against inflation,
sell the long end of those that aren't.*

**Applies when / Breaks when.** Useful as a gap signal, not a target. No central bank follows Taylor
mechanically, and the output depends entirely on the r\* you plug in. It breaks at structural breaks
(pandemic labor data, supply shocks) where the output gap is mis-measured.

**Channel example.** *Head of US Macro at $1 Trillion Firm* (Jan 2026); *Why Stocks Could Drop 10% Before
Year-End* (Sep 2026); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025: R − G, Koo); *From Fixed
Income Sales to the Buy Side feat. Jamie Patton* (Sep 2024: dot dispersion).

**Counterpoint.** Comparing the 10-year to *one quarter* of nominal GDP (8%, boosted by a post-shutdown
rebound) flatters the "loose" case; trend nominal growth was closer to 5%. Medeiros was early. His Jan
2026 "neither cut nor hike" became a hike only after an oil shock he did not forecast. Burton's
counter-view from April 2026 is that inflation would *calm down* after March. Hornbach admits the R − G
rule cannot be tested: there is no time series of growth expectations, only his read of the room.

**Links.** [[canon-mankiw-principles-of-economics]] (money, inflation, the Phillips trade-off) ·
[[canon-meadows-leverage-points]] (the policy rate as a parameter; financial conditions as the loop it
acts through).

---

## 6 · Fed independence, the chair transition, and the "third mandate"

**What it is.** The Fed is designed to be insulated from the executive so it can raise rates when that is
unpopular. The pressure point is the so-called **third mandate**. The Federal Reserve Act really does
list three goals: maximum employment, stable prices and *moderate long-term interest rates*. Powell's
reading (Sep 2025, via Hornbach) is that moderate long rates are the *result* of the first two, and
Hornbach adds that "moderate" does not mean low. The political version reads it as keeping Treasury
interest costs manageable. When that becomes the only mandate, monetary policy is being used to solve a
fiscal problem (**fiscal dominance**).

**How it works.** The 2025–26 sequence as the transcripts record it:
- Apr 2025: during the tariff panic Powell (Chicago, Apr 16) declines to offer a "Fed put"; Trump posts
  that Powell's "termination cannot come fast enough," the WSJ reports he is asking advisers about it,
  stocks fall back toward post-Liberation-Day lows and the dollar hits a 3-year low, and within a day
  the President walks it back. Jen's read: the market, not advisers, stayed his hand. Her line in the
  short: fire the chair and the "laws of physics" stop holding, so even a low policy rate won't produce
  low long rates once confidence in the bond market goes.
- *The independence argument is about perception* (Aug 2025): if a governor can be removed on an
  accusation, every later decision is read as political whether or not it is. "Don't fight the Fed"
  only works when the Fed is believed; a Fed seen as captured invites the market to fight it.
- Aug 2025: Governor Kugler resigns early, and **Stephen Miran** (a tariff theorist favoring lower rates)
  fills the seat through Jan 31 2026. The administration moves against Governor **Lisa Cook** over
  alleged mortgage fraud. The hosts note that she is a Biden appointee and that the press reads it as
  political.
- Early 2026: the DOJ opens a criminal probe of **Powell** over Fed headquarters renovation costs.
  Senator **Tillis** blocks any nominee until it is dropped, and Murkowski and others back him. Medeiros
  reads this Congressional check as "the system working," and it made him *less* worried about the long
  end.
- Powell's chair term ends **May 15 2026**, but his governor term runs to **2028**. He chooses to stay as
  a governor, which is unprecedented in the modern era.
- **Kevin Warsh** is confirmed. He is a 2006–11 governor, a balance-sheet hawk who opposed and then
  joined Bernanke's QE, and Druckenmiller-trained, as is Bessent. His agenda: steer with short rates, not
  the balance sheet ("indirect… hits financial instruments first"), keep the Fed out of fiscal policy,
  and run a unified, less talkative Fed. Jen's read: expect a **cut-plus-steeper-curve** regime.
- Result: Warsh's first FOMC was hawkish, and he **hiked** in September 2026. Jen: "once and for all"
  this ended the sock-puppet narrative.
- *Why the third mandate tempts:* on Jen's April 2025 numbers, a 25bp cut across the whole curve saves
  0.25% × $9.1T = **$22.8B/yr**, and 100bp saves **$91B**, against a **$1.8T** deficit. The weighted
  average maturity of the debt is ~**6 years**, so short-rate cuts alone barely touch the bill. Long
  rates have to fall and stay down through a year of auctions.

**Business significance.** Credibility sets the long end, and the long end sets mortgage rates,
corporate term funding and DCF discount rates. A central bank seen to be funding the government gets a
lower front end and a *higher* long end plus a weaker currency, which is the worst mix for anyone
borrowing long or importing.

**Forces & impact.** Debt (~$37T at the Warsh hearing, $40T crossed by Sep 2026, on the hosts' figures),
an electorate that won't accept either tax rises or entitlement cuts, and midterms. Jen's own drift is
the honest part. A rates purist all her career, she says aloud the US has "crossed the Rubicon", and asks
how the debt gets financed *without* monetary policy. She offers a heroin/methadone analogy, and lists
the tail options: "polite defaults", retroactive call features, the Fed buying directly at auction. The
channel works through two of them in detail. An *Odd Lots* episode (Apr 2025) asked how ironclad
Treasury documentation really is and floated a pen-stroke swap of all outstanding debt into 100-year
paper; Jeffrey Gundlach's "polite default" (Mar 2026) would force-extend short debt to 30 years at the
same coupon or cut coupons outright. Jen: "hard pass," because you get to break that glass exactly once,
and then no one buys your next auction. Kristen maps it to private-equity liability-management
exercises ("creditor-on-creditor violence," the Caesars restructuring).

**With vs. without.** With independence, the long end trusts that inflation will be fought, so the
government borrows long at a modest term premium. Without it you get the 1970s template (policy 200–300bp
below Taylor), currency weakness and inflation expectations that come loose, and Medeiros's rule says
sell that country's long bonds. The "chairman's curse" episode is the market version of the same
uncertainty: Greenspan (1987, Black Monday), Bernanke (2006, curve inverts on day one), Powell (Feb 2018,
"Volmageddon" on his first day).

**Applies when / Breaks when.** Independence is protected by institutions (governor terms, a committee,
Senate confirmation) only as long as Congress enforces them. It breaks when the confirmation process
selects for loyalty, or when debt service crowds out other spending enough that markets *expect*
accommodation regardless of who sits in the chair.

**Channel example.** *Is This the End of the Federal Reserve? Emergency Episode* (Aug 2025, Cook);
*Jerome Powell Isn't Coming to Save Us* (Apr 18 2025); *FX101, Operation Twist and Yale's $6bn Sale*
(Apr 2025, the termination post and walk-back, the 100-year swap idea); *Why Firing the Fed Chair May Not
Lead to Low Rates* (short); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025, the statutory
third mandate); *Wall Street is Watching Something More Concerning than Oil* (Mar 2026, polite default);
*Kevin Warsh's Senate Hearing: What You Need to Know* (short, Apr 2026); *Why is
Trump trying to fire Fed Chair Powell?* (short, Apr 2026); *Every New Fed Chair Has Crashed the Market*
(Apr 30 2026); *The truth behind the debt-refinancing theory* (short, Apr 2025); *New Fed Governor
Miran* (short, Aug 2025).

**Counterpoint.** The "chairman's curse" is three anecdotes with no base rate, and the hosts overstate
it: on Black Monday the S&P fell **~20.5%**, not "~26%" (the Dow fell 22.6%). Volmageddon was a
short-vol ETP blowup (XIV), not caused by Powell. The $9.1T base in the refinancing math looks like the
debt *rolling* within a year, not the total stock, so the savings arithmetic is narrower than "rates
across the curve" implies. The ⚠ here is that the hosts' admiration for Warsh as a "serious person" is
earned on his track record, but it is still a prior.

**Links.** [[canon-neustadt-may-thinking-in-time]] (the 1970s analogy and its limits) ·
[[canon-jensen-meckling-agency-theory]] (principal-agent: who the Fed works for) · [[canon-taleb-black-swan]].

---

## 7 · QE vs. QT vs. reserve management: the balance sheet and its plumbing

**What it is.** **Quantitative easing (QE)** is the Fed buying long-dated Treasuries and MBS (and
briefly corporate bonds in 2020) and paying with newly created bank reserves. It pushes long yields down
and puts cash in banks' hands. **Quantitative tightening (QT)** lets those holdings mature without
reinvestment. **Reserve management purchases** buy *bills* to keep reserves "ample" for the plumbing.
They expand the balance sheet without targeting long rates.

**How it works.**
- *QE transmission (2008):* the Fed cannot set mortgage rates. Mortgages have an expected life of ~5–7
  years, so the Fed bought 5s, 7s and 10s (and 30s, "the whole curve") to pull down the risk-free rate
  off which mortgages price. Kristen explains why it's called "printing money": a dealer sells bonds to
  the Fed and finds new money in its account that didn't exist before.
- *QT and SOMA reinvestment (May 2025 short):* QT allowed up to **$25B/month** of Treasury runoff, cut to
  **$5B** from April 2025. In a refunding month with **$76B** of SOMA Treasuries maturing, the Fed buying
  ~**$71B** at auction (e.g. $20B 3s, ~$15B 10s) is *replacement*, so the balance sheet still shrinks.
  The internet called it "secret QE." It was not.
- *Reserves (Aug 2025 short, borrowed):* the balance sheet was down ~$2.5T from peak, almost all of it
  drained from the **reverse repo facility**. That left bank reserves (~$3.3T) as the system's buffer,
  with ~10% of GDP as a rough floor. Tax days drain reserves, and in Sep 2019 that produced the "repo
  spike": GC jumped from ~2–2.5% to ~6% in a day, "collapsed the basis trade" and, on the hosts' telling, created the
  **Standing Repo Facility** (see Counterpoint for the actual sequence).
- *Operation Twist* (FX101 episode, Apr 2025): balance-sheet *composition* is a tool separate from size.
  By 2011 the Fed's QE holdings had aged toward the front end, so rather than grow the balance sheet it
  sold short-dated Treasuries and bought long-dated ones, about **$667B** in total (the maturity
  extension program), to push long yields down relative to short ones. Jen is candid that the later
  flattening and inversion had many causes besides Twist.
- *How QE actually happened on a desk:* clients' offers were written on paper sheets before an 11am
  cutoff and run to whoever had a Fed terminal; the Fed picked levels. Always in the secondary market:
  the Fed cannot buy new-money debt directly from the Treasury, and it cannot forgive Treasury debt it
  holds. At auctions it only **rolls maturing SOMA holdings** (the "SOMA add-on" line in results).
- *Hornbach's critique* (Sep 2025): the first QE rounds answered a deflationary shock, but the later
  rounds, including the maturity extension program, were spent chasing ~30bp of core-PCE shortfall
  (1.7% vs 2%). The mandate is stable prices, not exactly 2%, and he enjoyed a decade of predictable
  prices living in Japan.
- *Oct 29 2025: QT ends.* Alongside a priced-in 25bp cut, the Fed ended runoff effective Dec 1, which
  Hornbach had told the hosts six weeks earlier it would not do. The tell was in funding markets: fed
  funds minus SOFR went from about −6/−7bp to about **−30bp** at October month-end, and standing repo
  usage rose. Agency MBS paydowns now roll into **bills**. Jen's second-order chain: Fed bill demand
  richens the front end, nudges the Treasury toward more bills and fewer 20s/30s, which also richens the
  long end and shortens the debt's maturity. "Not an Operation Twist, but a step in that direction."
- *Dec 2025:* a 25bp cut plus **reserve management purchases** of bills through April. April is tax-day
  inflows to the TGA, and also Powell's last month as chair (Jen).
- Medeiros: the Fed thinks ample reserves ≈ **10–12% of GDP**; the balance sheet ≈ 25% of GDP. It is not
  technically QE, but "the balance sheet is not going down. So you can call it whatever you want."

**Business significance.** QE lowered every long-dated funding cost, including 2–3% mortgages, cheap
LBO debt and zero-rate SPAC mania (Jen ties the 2020 SPAC boom to ZIRP). Reserve scarcity is a quieter
risk. When repo spikes, every levered holder of Treasuries (hedge funds in the basis trade, dealers)
faces margin calls at the same moment.

**Forces & impact.** QE is break-glass. Jen and Kristen argue that its normalization from 2008 onward,
and its repetition in 2020, created both the 9% CPI print and the housing-affordability crisis (house
prices roughly doubled 2018→2025 on their figures). Warsh's whole program is to stop using the balance
sheet. Second order: a smaller-balance-sheet Fed leaves the long end to the market and the Treasury (§9),
so expect a steeper curve and more term-premium volatility.

**With vs. without.** Without QE in 2008–09, the hosts concede, the bottom would have fallen out "into a
depression and not a recession." With QE as a permanent tool, asset prices embed a central-bank put and
inflation risk. Without ample reserves, the funding market seizes (2019). With permanently ample
reserves, Medeiros warns, you have "created permissive [conditions] for risk."

**Applies when / Breaks when.** QE works when there is a disinflationary crisis and a transmission
blockage. Using it during real inflation would be "pouring gasoline on the fire" (Jen, Mar 2026). Reserve
management works as long as the Fed can find the scarcity point *before* it is hit. In 2019 it couldn't.

**Channel example.** *Did the Fed secretly start QE again?* (short, May 2025); *The Fed: is this new QE?*
(short, Dec 2025); *Who controls mortgage rates?* (short, Mar 2026); *The potential financial crisis
that no one is talking about* (short, Aug 2025, `culture-other` cluster); *FX101, Operation Twist and
Yale's $6bn Sale* (Apr 2025); *Meta & xAI as Project Finance 101 PLUS… the Fed's Insane Press Conference*
(Oct 31 2025, end of QT); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025); *Wall Street is
Watching Something More Concerning than Oil* (Mar 2026, open market operations and SOMA add-ons).

**Counterpoint.** "QE caused 9% inflation" overstates it. 2021–22 also had fiscal transfers, supply
shocks and energy. Japan ran QE for two decades without that outcome, though Burton's answer is that
"the US is not Japan." The hosts' 2019 numbers are approximate: SOFR printed ~5.25% with intraday GC
trades near 10%. Jen also admits on air that her Aug-2025 "precipice of crisis" call was dramatic, and
that the Fed simply ended QT. **Sequence error:** in 2019 the Fed responded with temporary repo
operations and bill purchases; the Standing Repo Facility was created in **July 2021**. The Aug 2025
episode also puts interest on reserves *at* the floor; it is set inside the range, with the reverse repo
rate at the bottom. Hornbach's "QT won't end this year" call (Sep 2025) was wrong within six weeks, a
reminder that even the most senior strategist's balance-sheet forecasts are guesses about a committee.
The Oct 2025 episode implies runoff was MBS-only; Treasury runoff (capped at $5B/month) ended too.

**Links.** [[market-structure-24-5-trading]] (Treasury central clearing, repo mandate 2027, Fedwire
hours: the same plumbing) · [[canon-perrow-normal-accidents]] (tight coupling in funding markets) ·
[[canon-taleb-antifragile]].

---

## 8 · Treasury auctions and who buys the debt

**What it is.** The US Treasury sells debt on a published calendar: bills weekly, 2s/3s/5s/7s monthly,
and new 10s, 20s and 30s quarterly at the **refunding** (February, May, August, November) with smaller
**reopenings** in the following months. Auctions are **single-price ("Dutch")**: everyone pays the
yield at which the last dollar clears.

**How it works.**
- Bonds trade before they exist as **when-issued (WI)** securities, quoted as a spread to the current
  on-the-run, so traders can price the "roll".
- *Bidders:* **direct** (an account with the Treasury), **indirect** (bidding through a primary dealer
  or, in practice, the NY Fed), and **dealers**, who are obliged to bid. Competitive bids are capped at
  **35%** of the auction and non-competitive bids at **$10mm** (retail).
- *Example:* $25B 10s are offered, and the yield on the 25-billionth dollar is the clearing level for all.
  Results come out just after **1:00pm**. Clearing above the 1pm WI yield is a **tail** (weak), at it is
  **on the screws**, below it means it **stopped through** (strong).
- *Pricing the WI* (Mar 2026 episode): with the on-the-run 5-year at **4.00%**, the new 5-year adds a
  month of term premium plus a supply concession, worth ~1bp, so the WI trades at **4.01%**. Clearing at
  3.99 is a 2bp stop-through; 4.01 is on the screws; 4.03 is a 2bp tail. Context matters: a 2bp
  stop-through after a 10bp pre-auction concession is not strong. Primary dealers must bid, so a high
  **dealer takedown** means end demand was missing; dealers then "puke" the paper into the market.
- *April 2025 sequence* (Apr 11 episode): the 10-year went from ~3.9% after Liberation Day to ~4.5%. The
  3-year tailed ~2.5–3bp with the lowest direct share since COVID. The 10-year cheapened **18bp** into
  its auction, stopped through, but showed **1.4%** direct versus a ~17.5% recent average. Ten minutes
  later the 90-day tariff pause was announced. The 30-year the next day drew ~30% direct, which Jen read
  as the world signalling approval. Her frame: foreigners hold ~25–30% of US debt and can "vote with
  their wallets" at auction.
- *March 2026, the front end:* 2s, 5s and 7s all tailed during the Iran oil shock; dealer takedown in
  the 2-year was ~**24%** against a ~10% 12-month average. Jen notes 2-years carry little DV01, so front-end
  tails matter less than long-end ones.
- *The 20-year is the wrong canary* (short): the 20-year was reintroduced only in 2020 and has little
  natural demand, a "size 10⅛ shoe," so it structurally trades cheap to 10s and 30s; a 1¼bp tail there is
  ordinary, not a confidence crisis.
- *July 2025 7-year:* **33% direct**, a record, and stopped **2.5bp through** after rallying into the
  auction. Jen "ate her words" from April, when low direct takedown fed fears of a foreign buyer strike.
- *New bill buyers (stablecoins):* the GENIUS Act (July 2025) requires stablecoins to be backed by
  T-bills and similar assets. Stablecoins outstanding were ~**$260B** (July 2025), and Bessent projected
  **$2T**. More stablecoins mean a structural **bid for bills**, which pushes front-end yields down
  without a Fed cut. Kristen calls it a "chip-maker" business model: hold yielding bills, issue a
  non-yielding token.

**Business significance.** Auctions are the largest recurring supply events in global finance, so a tail
can reprice the whole curve, and with it mortgage rates and corporate issuance windows, within minutes.
Corporate treasurers time issuance around auction weeks and refunding months. Weak foreign demand is the
single scariest signal for a deficit country, because "there'll always be a buyer of US debt, the
question is at what rate" (Adami).

**Forces & impact.** Supply: deficits and the issuance mix (§9). Demand: foreign reserve managers, banks
(balance-sheet capacity), money funds (bills), pensions and insurers (long end), and now stablecoins.
Second order: if stablecoins become the marginal bill buyer, the Treasury is pushed to issue shorter,
which raises rollover risk. Jen's labeled speculation: weakening the dollar → crypto revival → stablecoin
growth → more bill demand, with a Trump family stablecoin business adding a conflict of interest.

**With vs. without.** Without a predictable calendar the market would have to price issuance-surprise
risk into every yield. That predictability is why Jen bristles at influencers calling auction *sizes*
surprising: only the *outcomes* are news. Without single-price auctions, bidders would shade bids to
avoid the winner's curse and raise the government's cost.

**Applies when / Breaks when.** The bidder-mix signal works only if categories map to real investor
types. Auctions function smoothly until dealer balance sheets are full (§9) or a buyer class retreats
together (April 2025).

**Channel example.** *The best explanation of Treasury auctions* (short); *It Wasn't Equity Turmoil That
Spooked Trump — It Was the Bond Market* (Apr 11 2025); *Wall Street is Watching Something More Concerning
than Oil* (Mar 31 2026); *Why the 20 year US Treasury bond auction isn't the canary in the coal mine*
(short); *AI Collusion in Trading,
Figma IPO and Could Stablecoins Lower Interest Rates?* (late July 2025); *If the Fed won't cut,
could stablecoins be the key?* (short, 2025).

**Counterpoint.** **Likely error:** Jen treats *direct* bidder share as the proxy for foreign
governments ("you automatically think China"). The standard reading is the reverse. Foreign official
accounts usually bid through the NY Fed and show up as **indirect**, and directs are largely domestic
money managers. Treat her foreign-demand inferences from direct takedown with caution. This matters for
the April 2025 story: the April 9 10-year with its tiny direct share also drew a near-record **indirect**
share (~88%) and low dealer takedown, which is the opposite of a foreign buyer strike. The stress that
week was in the secondary market, swap spreads and basis unwinds (§10, §11), so "the auctions forced the
pause" is a stronger claim than the auction data supports. Stablecoin sizing
comes from interested parties (Bessent, Circle's CEO at $10T), and Jen herself flags that as bias.

**Links.** [[trading-floor-mechanics]] (dealer balance sheets, sales vs. trading roles) ·
[[canon-akerlof-market-for-lemons]] (why single-price design reduces adverse selection in bidding).

---

## 9 · Treasury buybacks and debt management

**What it is.** The Treasury can repurchase its own old bonds and fund the purchase with new issuance
elsewhere on the curve. It is **not QE**: no new money is created, and the total debt is unchanged. What
changes is *where* the duration sits and who has to hold it.

**How it works.**
- *The "cash for clunkers" problem:* old off-the-run bonds such as the **1.375% Aug-2050**, issued in
  2020 near zero rates, trade near **46 cents** after a 400bp+ selloff. Nobody trades them. They clog
  dealer balance sheets that primary dealers need for mandatory auction bidding.
- *Program:* started in 2024 at ~$2B a month (barely noticed). On **Aug 19 2026** Bessent announced it
  would at least double long-end (10–30y) buybacks, to ~$4B+. The Treasury can reject offers it
  considers rich, unlike the Fed's price-insensitive QE.
- *Three ways to fund it, three different effects* (Jen):
  1. **Bills:** moves supply to where demand is deepest, almost no duration, a rounding error at bill
     scale.
  2. **2s/5s:** adds duration at the front end. Front yields rise and the curve flattens, a **stealth
     hike** that does Warsh's tightening while the headline reads "Treasury supports bonds."
  3. **Treasury General Account cash:** injects cash that wasn't in the system. That is effectively QE by
     the Treasury, and it would undo the logic above.
- Jen's "Prestige" thesis (labeled speculation): the market saw yield suppression, while the real trick
  was option 2, Bessent doing "Warsh's dirty work." Medeiros (Sep 2026) expects options 1 and 2. He
  doubts option 3 because of the 2027 debt ceiling: draining the TGA in extraordinary measures risks an
  "accidental default."
- Bessent in his own words: his job is to "truncate the very bad outcome", meaning a liquidity failure.
  Economics is "biology", not physics, and the Treasury slows things down while hedge funds speed them
  up.

**Business significance.** The issuance mix is a lever on long yields, and hence on mortgages and
corporate long bonds, that doesn't need the Fed. The buyback increase came just before September's heavy
IG calendar, including AI hyperscaler issuance. 30-year bonds from Meta were ~40bp wider and Oracle /
SpaceX ~60bp wider within a month of issue. Making room in the long end matters for every issuer.

**Forces & impact.** It **shortens the weighted-average maturity** of the debt. Bessent had criticized
Yellen for not terming out at 1% in 2020. Kristen defends Yellen with hindsight bias (everyone,
including her own ARM refinancings, assumed zero rates forever). Jen defends Bessent: terming out *now*,
at 20-year-high yields, could itself trigger a refinancing crisis. The cost is rollover risk: debt that
needed no attention for 30 years now needs refinancing in 2–5. "Not kicking the can down the road…
kicking the can across the room."

**With vs. without.** Without buybacks, illiquid off-the-runs sit on dealer balance sheets, shrinking
auction capacity, which in a stress event turns into a failed or badly tailed auction. With aggressive
buybacks funded short, long yields get a modest anchor, at the price of a structurally shorter debt
profile and more frequent refinancing at whatever rates prevail.

**Applies when / Breaks when.** It is a liquidity tool when used in size. As a yield-control tool it
is limited by scale: $4B a month against ~$20B per long-bond auction. It breaks into quasi-QE if funded
from the TGA.

**Channel example.** *I got the chance to ask Scott Bessent ONE question* (Sep 3 2026, with the
90-second clip as a short); *The truth about Bessent's Treasury buybacks* (short); *Is the Treasury
secretly doing QE?* (short).

**Counterpoint.** The "stealth hike" depends on the funding choice, which won't be known until the
refunding announcement after the midterms. Druckenmiller (in a WSJ op-ed) argued the move damaged
Treasury credibility. The hosts answer with an AI-detection score on his op-ed, which is a jab at the
messenger and doesn't address his argument. Buying back bonds at 46 does *not* "save half the money" in
any real sense: the Treasury pays market value and then refinances at today's higher coupons.

**Links.** [[canon-dixit-nalebuff-thinking-strategically]] (Treasury and Fed as players with different
payoffs) · §7 (QE contrast) · §12 (why long yields = mortgage politics).

---

## 10 · Repo, SOFR and interest-rate swaps

**What it is.** **Repo** (repurchase agreement) is a short-term loan secured by a bond: you sell
Treasuries to a dealer and agree to buy them back tomorrow at a slightly higher price, and that price
difference is the overnight **general collateral (GC)** rate. **SOFR** (Secured Overnight Financing
Rate) is the benchmark computed from those trades. It replaced LIBOR and now sits under most
floating-rate loans and swaps. An **interest-rate swap** exchanges fixed for floating payments on a
notional. A *receive-fixed* swap is a **synthetic bond funded at SOFR**.

**How it works.**
- *Three ways to own 10-year duration* (basis-trade episode, Apr 2025), from most to least balance
  sheet: (1) pay **$100mm cash** for the bonds; (2) put ~10% down and **finance $90mm in repo**,
  pledging the bonds as collateral, "just like buying a house"; (3) go synthetic with **futures** (§11)
  or a **receive-fixed swap**. Real-money investors default to the derivatives because they consume the
  least balance sheet.
- *Carry and roll-down on the repo route:* a bond with a **5%** coupon financed at **4%** GC earns
  **1%** a year if nothing moves. That is positive **carry**. On an upward-sloping curve the bond also
  **rolls down** to a lower-yielding maturity as it ages, so its price drifts up even with an unchanged
  curve. The risk is the floating leg: if overnight repo jumps to 6–10%, the 5% coupon no longer covers
  the funding.
- *Synthetic route:* receive fixed / pay SOFR on $100mm notional. Same cash flows, no principal, no cash
  up front (a **par swap** has zero NPV at inception), but both sides post margin as the NPV moves.
  After 2008, swaps moved from bilateral contracts to central clearing, because a positive-NPV swap
  facing Lehman became an unsecured claim in bankruptcy.
- *LIBOR → SOFR* (*What is SOFR??*, filmed the day after the last USD LIBOR fixing, June 30 2023).
  LIBOR was a panel of banks *self-reporting* where they would lend to each other *unsecured* for terms
  of 3, 6 or 12 months, so it carried a bank-credit component and could be rigged (and was). SOFR differs
  in three ways: it is **secured** by Treasuries (no bank credit risk), it is **computed from actual
  trades** rather than submissions, and it is **overnight and backward-looking**, "basically the same
  as GC." Fed funds, by contrast, is banks lending *reserves* to each other **unsecured**, which is why
  the two can decouple under stress.
- *What the switch broke:* **term SOFR** (anything longer than overnight) is a bespoke, bilaterally
  traded rate available only to some users, with no interdealer market for dealers to hedge in; legacy
  LIBOR loans needed **credit spread adjustments** bolted on to compensate lenders for losing the bank-
  credit component.
- *Swap spreads* = 10y swap rate − 10y on-the-run Treasury yield. Under LIBOR they were **positive**
  (swap rates carried bank credit; Treasuries were risk-free): at a 10bp spread and 10s at 5%, you could
  pay or receive fixed for 10 years at 5.10%. With QE in 2008 they went **negative for the first time**,
  30-year spreads collapsing to roughly **−60bp**, meaning the market would rather face interbank credit
  than hold 30-year US credit and its balance-sheet cost. Post-crisis capital rules kept them negative.
  In April 2025 30-year spreads got close to **−100bp**.
- *The sign trap:* desk language still treats spreads as if positive, so −20 → −10 is "widening" and
  −20 → −30 is "tightening."
- *Swap spreads as a diagnostic* (July 2026): if Treasuries were selling off because of *idiosyncratic*
  supply (crowding out by tech debt), swap spreads would tighten. They didn't. Jen concludes it wasn't
  Treasury-specific: "nobody wants anything", meaning insufficient risk premium across asset classes.
- *Expressing a view in swaps vs. Treasuries* (Hornbach, Sep 2025): a curve steepener in the SOFR swap
  curve would cost "much more" negative carry than the same steepener in Treasuries, so Morgan Stanley
  recommended the Treasury version (§3).

**Business significance.** Every corporate floating-rate loan is SOFR + spread, so swaps are how a CFO
turns floating into fixed (or the reverse) without refinancing. Pensions and insurers *receive* fixed
in long swaps to match liabilities, which is why Dutch pension reform matters for long-end rates (§3).
Swap pricing is also the market's cleanest read on whether a Treasury move is about rates or about
Treasury supply and balance sheet. Repo is the hinge of the whole system: Eisman's argument that the
dollar's reserve status is safe rests on overnight repo being a multi-trillion-dollar market that runs
almost entirely on Treasury collateral (§16).

**Forces & impact.** Repo rates track Fed policy and reserve scarcity (§7). The Fed keeps the effective
rate inside its target range with administered rates: a **floor** from interest on reserve balances
(banks only) and the reverse repo facility (money funds and others lend cash to the Fed), and a
**ceiling** from the standing repo facility and the discount window (the Fed lends cash). Swap spreads
track Treasury supply versus dealer balance-sheet capacity and regulation (the supplementary leverage
ratio, the central-clearing mandate). When balance sheet is scarce, the synthetic gets relatively more
valuable and Treasuries cheapen versus swaps, which is the negative-swap-spread world.

**With vs. without.** Without swaps, every hedge needs physical bonds and the balance sheet to carry
them. Duration management would be costlier and concentrated in the few institutions with balance
sheet. Without a deep repo market, Treasuries lose their "cash-equivalent" status, because you can't
borrow against them overnight, and their yields must rise to compensate. Without SOFR's transaction
base, the benchmark under trillions of loans is whatever a dozen banks say it is.

**Applies when / Breaks when.** The synthetic-bond equivalence holds while repo funds smoothly. It
breaks in funding stress (2019, March 2020), when GC jumps above SOFR expectations, and levered basis and
swap-spread positions get hit together. It also breaks when the *collateral itself* is doubted: Jen
reads April 2025's collapse in swap spreads as investors preferring any derivative to owning a cash
Treasury.

**Channel example.** *Bond Market Chaos: Unpacking the Basis Trade Blowup Theory* (Apr 2025); *What is
SOFR??* (July 2023); *How does an interest rate swap work?* (2024); *Fixed Income Strategy 101 feat.
Matt Hornbach* (Sep 2025); *Why Jamie Dimon Won't Buy Stocks OR Bonds Right Now* (July 2026, swap-spread
read).

**Counterpoint.** The swap-spread inference is sound in direction but swap spreads also move on
regulation and dealer capacity, not only on Treasury-specific supply, so "nobody wants Treasuries" and
"nobody has balance sheet for Treasuries" look identical on the screen. The 2008 explanation (fear of
a QE-driven debt trap) is the hosts' story; the standard account puts more weight on dealer balance-sheet
collapse and on swap demand from hedgers. The SOFR video's worries about term-SOFR liquidity date from
2023 and have eased as CME term SOFR became the loan market default.

**Links.** [[market-structure-24-5-trading]] (SEC Treasury clearing mandate: cash Dec 2026, repo June
2027) · [[trading-floor-mechanics]] · [[canon-akerlof-market-for-lemons]] (why an unsecured,
self-reported benchmark invited manipulation).

---

## 11 · Treasury futures, cheapest-to-deliver, and the basis trade

**What it is.** A **Treasury futures contract** is an exchange-traded promise to deliver Treasuries at
a future date (quarterly expiries). It is not tied to one bond: at expiry the short may deliver any bond
from a **basket of eligible securities**, and one of them is mathematically the **cheapest to deliver
(CTD)**. The **basis** is the price gap between that cash bond and the futures contract. The **basis
trade** buys the cheap cash bond, finances it in repo, and sells the rich future, waiting for the two to
converge at expiry.

**How it works.**
- *Contract mechanics:* the 10-year contract (**TY**) is **$100,000** face per contract. You post a
  small margin to the exchange and are marked daily, so a futures position is inherently levered. A
  forward is the same promise negotiated bilaterally and unmargined; futures are standardized, cleared
  and margined (the hosts sort this out on air).
- *The basket:* TY delivers aged notes, not the on-the-run 10-year: recent 7-years, 10-years issued ~3
  years ago, even old 30-year bonds with ~7 years left. Jen says the contract really trades like the
  **7-year** point.
- *Why one bond is "cheapest":* deliver the barrels of oil sitting in your backyard, not the ones you
  have to ship from overseas. For Treasuries the "shipping cost" is the financing, measured as the
  **implied repo rate**. To compare bonds with different coupons and maturities, each gets a
  **conversion factor**: its price per $1 face if it yielded **6%**. A 5¾% bond trades below par at a 6%
  yield, so its factor is a little under 1 (the video uses **0.99**).
- *Futures DV01* (*How to Calculate Treasury Futures DV01*): start from the CTD's Macaulay duration,
  convert to modified duration, then to dollars using price. Take a CTD DV01 of ~**6.6** (per 100 face)
  and the video computes 6.6 × 0.99 = **6.534**, so 6.534 / 10,000 × **78,000** contracts × $100,000 =
  **~$5.1mm per bp**.
- *The trade that prompted it* (short, Apr 2025): someone sold **78,000** June TY contracts in thin
  London hours, the largest Treasury futures block in at least 12 years. At ~$5.1mm per bp, a
  5–10bp selloff put the seller up **$25–50mm** in a day, plus ~$25mm more on the next 5bp. Jen could
  not tell whether it was an outright short or a hedge against heavy call open interest.
- *Why futures are structurally rich:* real-money buyers (asset managers, pensions, insurers) prefer
  futures and receive-fixed swaps because they need far less cash and balance sheet than physical bonds
  (§10). So futures trade rich to the deliverable cash bonds, and the aged bonds in the basket are
  illiquid ("locked up in the hands of a little retiree here and a pension fund there").
- *The basis trade:* a hedge fund buys the cheap cash bonds, finances them in repo, and sells futures
  against them. Convergence at expiry is near-certain, but the gap is "only a couple of basis points,"
  so it must be levered **~20:1** on average and, per the *Money Stuff* podcast the hosts cite, up to
  **100:1**. Apollo's chief economist Torsten Sløk estimated the trade at **~$800B** (from hedge-fund
  futures shorts and prime-brokerage repo).
- *How it breaks:* the trade needs two things to stay true, futures rich to cash, and the ability to
  hold until convergence. A shock that makes cash Treasuries cheapen sharply *against* futures (a tariff
  announcement, a repo spike) produces mark-to-market losses multiplied by the leverage, margin calls on
  the futures leg, and forced selling of the illiquid cash leg, which cheapens it further. March 2020 was
  the last full blowup; September 2019's repo spike was the funding version (§7).

**Business significance.** The basis trade is how a cash-futures arbitrage becomes a **source of
Treasury market liquidity**: basis funds absorb the cash bonds that real money doesn't want to hold and
supply the futures real money does want. That keeps Treasury yields lower than they would otherwise be,
which matters to every borrower priced off them. The cost is a concentrated, levered, short-volatility
position sitting in the plumbing of the risk-free asset. For a corporate treasurer, futures DV01 is also
the practical hedge unit: pre-hedging a bond issue means shorting the number of contracts whose DV01
matches the planned issue.

**Forces & impact.** Size grows with the structural richness of futures, which grows with
balance-sheet regulation (SLR, Basel endgame) and with real money's preference for derivatives. Risk
rises with leverage, repo volatility and reserve scarcity. Jen's April 2025 list of what the Fed could do
to relieve the pressure, in order of impact: **loosen SLR** so banks can hold Treasuries more cheaply;
reverse QT into **QE**; bid directly at auctions; and only last, cut rates ("filing my nails" to lose
ten pounds). Her central call is that the basis unwind was **a symptom, not the cause**: the reported
blowups (one PM out **$140mm**, another **$30mm**, an unconfirmed **$400mm**) were large for people and
tiny against a $36T market, while the simultaneous collapse in swap spreads pointed to a broad aversion
to cash Treasuries.

**With vs. without.** Without basis traders, futures would trade persistently rich, cash Treasuries
cheap, and the cost of the deficit would be higher. With them, the market works well until a shock
forces them all to sell the same illiquid bonds at once, which is why the Fed ended up buying Treasuries
in size in March 2020. The policy argument that followed (central clearing, SLR reform, a standing repo
facility) is an argument about whether to keep the liquidity and socialize the tail.

**Applies when / Breaks when.** Convergence holds at expiry by construction. The trade breaks when the
path to expiry is intolerable: repo spikes, margin increases, or a sudden repricing of Treasuries as an
asset class rather than of one bond.

**Channel example.** *Bond Market Chaos: Unpacking the Basis Trade Blowup Theory. Cause… or Convenient
Excuse?* (Apr 2025); *Largest 10 Year Treasury Futures Block Trade EVER?* (short, Apr 2025); *How to
Calculate Treasury Futures DV01 (Calculating & Converting DV01 of the Cheapest to Deliver)*; *Head of US
Macro…* (Jan 2026: the trade back to sizes "not seen since… 2019").

**Counterpoint.** **Formula error in the DV01 video:** the futures contract tracks the CTD *divided*
by its conversion factor, so futures DV01 ≈ CTD DV01 **÷** CF, not ×. With CF 0.99 the answer is 6.6 /
0.99 ≈ 6.67, or ~$5.2mm per bp: barely different here, very different for low-coupon CTDs with factors
far below 1. The video's "6½ to just under 8 years" basket is the practical CTD zone; the CME
specification for TY runs from 6½ to 10 years remaining. Jen is careful to say she cannot see the flows
and knew the PMs involved, which is honest, but "symptom not cause" is also the view most comfortable
for someone who thinks the real story is a repricing of US policy. The *Money Stuff* "100:1" is an
upper-tail anecdote, not a market average.

**Links.** [[wss-trading-hedge-funds]] (§9 there treats the same trade as short volatility dressed as
arbitrage, from the hedge-fund seat) · [[canon-perrow-normal-accidents]] (tight coupling: one shock,
many identical positions) · [[canon-taleb-antifragile]] (picking up nickels in front of a steamroller) ·
[[market-structure-24-5-trading]] (central clearing).

---

## 12 · Mortgage-rate drivers and housing policy

**What it is.** A US 30-year fixed mortgage is a risk-free rate plus a spread, and the risk-free rate is
the **10-year Treasury, not the 30-year**. Borrowers move or refinance, so the mortgage's effective life
and rate sensitivity are much shorter than its stated term.

**How it works.**
- Banks originate mortgages, securitize them (with a Fannie/Freddie guarantee taking out most credit
  risk), and sell the MBS so they can lend again.
- MBS investors bear rate risk, (guaranteed-away) credit risk, and **prepayment risk**. US borrowers can
  prepay without penalty, which makes the holder short an option, so MBS have **negative convexity**.
- *Partial durations:* decompose MBS price sensitivity by curve point (2y, 5y, 10y, 30y), measured
  empirically. Hornbach's figures (Sep 2025): only ~**10%** of a secondary-market 30-year mortgage's
  rate sensitivity sits on the 30-year Treasury, ~**40%** on the 10-year, and the remaining ~**50%** on
  the 2- and 5-year. So mortgages trade roughly as **10y + spread**, with real front-end exposure, and
  pushing only the 30-year down 100bp would barely move housing. If Bessent wants cheaper mortgages, he
  wants *all* yields lower, not a flatter curve.
- *Why Fed cuts transmit less than they used to* (Patton, Sep 2024): of an ~$8T agency mortgage market,
  ~35% was adjustable before the GFC (her figure, likely the origination peak), so policy moves hit
  household payments directly; today under 1% floats. TCW estimated **85%** of mortgages in the Bloomberg
  Agg would not be economic to refinance until rates fell another ~100bp. That is lock-in measured.
- *The predatory mechanics of 2006* (Steve Eisman): subprime loans carried a 2–3 year teaser (say 3%)
  resetting to LIBOR + 600 (~9%), underwritten to the teaser the borrower could afford, with ~4 points
  of origination fees rolled into principal against ~1 point on a prime loan. At reset the lender offered
  a refinance into the same structure for another 4 points, so the borrower never escaped and the
  originator earned fees on a loop. Subprime origination went from ~**$50B** (2002) to ~**$500B** (2006),
  2% to 20% of the market. Rising delinquencies in 2006-vintage securitizations were his signal.
- *Iran war, March 2026:* the Fed *held*, yet 30y mortgages rose from **5.75%** (end Feb) to **6.5%**,
  because oil-driven inflation fear lifted the long end. The Fed sets overnight rates. The market sets
  the long end.
- *GSE purchases:* Trump directed Fannie/Freddie to buy **$200B** of MBS. The agency market is **$9T+**,
  and one estimate cited puts the effect at ~**15bp** of spread. The purchases also push the GSEs toward
  post-2008 retained-portfolio caps. Jen reads it as a midterm signal more than a rate fix.
- *50-year mortgage:* roughly **15% lower** annual payment than a 30-year at the then-current curve. In
  an amortizing loan, early payments are almost all interest, so equity barely builds ("almost like
  you're renting"). The *portable* variant breaks the collateral logic of lending (a $1mm loan moving to
  a $500k house) and makes the borrower's option close to certain to be worth exercising, so lenders
  would charge a much higher rate.

**Business significance.** Housing is the largest household asset and a main transmission channel. The
2020 lock-in (2% mortgages nobody will give up) freezes turnover, labor mobility, and the revenue of
brokers, builders and movers. For the Fed, falling mortgage rates now risk re-igniting house prices and
rents, which had been the main source of disinflation. That is why Medeiros says **Treasury and Fed
want opposite things** for mortgage rates in 2026.

**Forces & impact.** Long-end term premium (the dominant 2025–26 driver, more than spreads), MBS
spreads, GSE policy, and lock-in. Every proposal on the table (GSE buying, the 50-year, portability,
banning institutional single-family purchases) is **demand-side**. With supply fixed, more buying power
means higher prices. Housing starts and permits per capita sit near **50-year lows**. Institutional
investors took ~**18%** of single-family purchases (flow, Redfin, ~12 months) but hold only ~**1%** of
the stock.

**With vs. without.** Without GSE guarantees and free prepayment, the US would look like most countries:
shorter fixes, more floating-rate risk on households, and a smaller, more volatile housing market.
Without the 2008 and 2020 QE, the hosts argue, prices would not be where they are. Medeiros: the
proposals make him *more* bullish on house prices troughing in 12–18 months, and no better on
affordability.

**Applies when / Breaks when.** "10y + spread" holds in normal prepayment regimes. It breaks when the
lock-in collapses prepayment speeds (MBS extend toward longer duration), or when spreads, not
Treasuries, drive the move (2008).

**Channel example.** *The best explanation of what drives mortgage rates* (short); *Who controls
mortgage rates?* (short, Mar 2026); *Oracle CDS… plus 50-Year Mortgages* (Nov 2025); *Why 50-year
mortgages won't solve affordability* (short); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep
2025, partial durations); *From Fixed Income Sales to the Buy Side feat. Jamie Patton* (Sep 2024, ARM
share and lock-in); *Steve Eisman… on Tariff Panic and Lessons From the 2008 Crisis* (Apr 2025).

**Counterpoint.** In *Every New Fed Chair…*, Jen says 10–30y yields are what mortgages price off, which
overstates the 30-year's role and contradicts Hornbach's 10% figure. The original version of this note
put the partial-duration hotspot at 7–10y from a short; Hornbach's breakdown gives the front end more
weight than that, and the two are model-dependent estimates that shift with prepayment speeds.
Patton's "under 1% floating" and "85% out of the money" are TCW's claims and unverified; TCW was long
duration at the time, so a story about weak transmission suited its book. The hosts' "let prices
correct" view is easy to hold as homeowners with low leverage. Kristen pushes back that lower rates
could also *unlock supply* by freeing locked-in owners.

**Links.** [[canon-meadows-thinking-in-systems]] (demand subsidies feeding the price loop) ·
[[canon-sterman-business-dynamics]] (supply response delays) · [[canon-taleb-antifragile]] (negative
convexity).

---

## 13 · Inflation measurement and pass-through

**What it is.** Inflation is the *rate of change* in prices, not their level: "the height of each
stair." The US has two baskets. **CPI** (BLS) is household-survey based with fixed annual weights.
**PCE** (BEA) is business-receipts based, its weights shift continuously, and it includes spending made
on consumers' behalf (e.g. employer health care). The Fed targets **PCE**, watches **core** (ex food and
energy) and "supercore" (core services ex housing), and uses CPI for direction.

**How it works.**
- *Substitution:* beef triples in price. CPI still assumes you eat burgers, while PCE registers the
  switch to chicken (or, on Burton's evidence, a husband who has bought pork at Wegmans every week).
- *Receipts vs. survey:* ask three patients what an MRI costs and you hear $300, $1,500 or $0. The
  hospital records $1,500 each time.
- *Base effects:* readings are year-over-year, so a soft print last March makes this March look hot.
  Burton expected a mid-to-high-3s March 2026 CPI partly for that reason. Prices can stay elevated while
  measured inflation reads zero.
- *Tariff pass-through:* inventory days = inventory / COGS × days. Nike: $7.5B / $6.6B × 90 = **~102
  days** of cushion before tariffs hit shelf prices. Munchkin (made in China, 145% tariff): $100k of goods
  now costs **$245k** landed, with the **US importer** paying the tariff. Medeiros estimates **~60%**
  pass-through, a stated rate of ~18% but an effective rate nearer **~10%** after exemptions.
- *Oil:* jet fuel → airfares is the second-round effect the Fed fears when household expectations are
  already elevated. The oil CEO's rule of thumb is transcribed as "every 10 cents ≈ 0.2% of global
  inflation", almost certainly **$10/bbl**, not 10 cents.
- *Nominal vs. real, and what a breakeven is:* John Normand's definition (2024): the nominal rate is
  what you observe; the **real rate** is nominal minus inflation, your gain in purchasing power. In
  2024 the US had positive real rates and Japan negative ones, the widest gap in ~30 years (§15). The
  market's version uses **TIPS**: a 10-year nominal Treasury yield minus the 10-year TIPS real yield is
  the **breakeven**, the inflation rate at which the two pay the same. (The channel's dedicated breakeven
  video is not in the transcript set, so this decomposition is supplied here, not taught on air.) The
  hosts' July 2026 reference to real yields "low-to-mid 2%" is a reading of this market. Hornbach, who
  made markets in cash TIPS in 2005–06, calls it the worst market-making job on the Street: a handful of
  dealers, thin liquidity, and drawdowns management has to stomach.
- *One-time level shift vs. ongoing inflation* (Hornbach, Kristen, Sep 2025): a tariff, like Japan's
  consumption-tax rises, should lift the price *level* once and then drop out of the year-over-year rate
  (base effects again), while cutting real demand. What keeps it inflationary is uncertainty: nobody
  knows the split between exporter, importer and consumer, or whether the rate will change next month.

**Business significance.** The Fed's reaction function runs on these numbers, so every pricing, wage and
debt decision indirectly reads PCE. For operators, inventory days are the lead indicator for when a cost
shock reaches the P&L. They also give you a window to reprice, re-source or pre-buy.

**Forces & impact.** Supply shocks (oil, tariffs), demand (fiscal impulse), expectations, and base
effects. Second order: exogenous shocks the Fed can't control show up in headline inflation, and the
policy question is whether they bleed into core. Since 2019 inflation has been higher everywhere
(Levine), as every government spent and cut rates at once in 2020–21.

**With vs. without.** Without PCE's substitution adjustment, measured inflation overstates the cost of
living and the Fed over-tightens. Without core measures, the Fed would react to every oil spike it can't
control. The cost is that core can look benign while households feel the headline. That is Kristen's
Main Street point: flights she bought for $350 now cost ~$1,000.

**Applies when / Breaks when.** Core is a good guide when shocks are transitory. It fails when shocks
persist long enough to reset expectations ("half a decade of transitory," Medeiros).

**Channel example.** *The truth about inflation: CPI vs PCE* (short); *$53 Billion Hedge Fund Chief
Strategist* (Apr 2026, base effects); *The real pain from tariffs is coming soon: inventory days*
(short, 2025); *Why Stocks Could Drop 10%* (Sep 2026, oil second-round effects); *"Sorry, Mr.
President: that's not how it works"* (short, base effects); *Finance, Philosophy, and the Yen Carry Trade
feat. John Normand* (2024, real vs nominal); *Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025,
TIPS desk, consumption-tax analogy).

**Counterpoint.** The short claims CPI housing at "45%" of the basket. That is an illustrative number;
shelter is ~35% of CPI and ~15% of PCE, which is the bigger and more important difference between the
two. Burton's "inflation will calm down" (Apr 2026) was followed by a September hike.

**Links.** [[canon-mankiw-principles-of-economics]] · [E9 lesson](../lessons/exec-E9-geopolitics-macro.html)
(Hormuz → oil → inflation chain) · [[apply-stock-picking-nke]] (the Nike inventory figures in a filings
context).

---

## 14 · FX and the dollar

**What it is.** An exchange rate is the price of one currency in another. It is driven by growth,
inflation, central-bank policy, fiscal policy, political stability, and above all **rate
differentials**. Raising rates should strengthen a currency.

**How it works.**
- *Rate differential:* the dollar strengthened through the 2022–23 Fed hiking cycle. The yen kept
  weakening even as the BOJ hiked, because the *gap* stayed wide (Adami).
- *Reserve recycling:* decades of US trade deficits shipped dollars abroad, and those dollars were
  recycled into Treasuries. Tariffs that shrink those flows also shrink foreign demand for US debt (Jen,
  Apr 2025).
- *Defending a currency without dumping Treasuries:* Japan, the largest foreign holder, can pledge
  Treasuries in the Fed's foreign repo facility for cash instead of selling them. Jen notes Bessent had
  pushed to expand it. In summer 2026 the US and Japan ran the largest coordinated intervention in
  decades; Bessent's "to-do list: buy 5–10 billion yen" became a meme.
- *Why a weak dollar tempts:* US debt is fixed in nominal dollars, so a weaker dollar transfers value away
  from foreign holders. Officially "we want a strong dollar" (Bessent); unofficially, Jen notes, Trump
  says the quiet part out loud.
- *De-dollarization:* after the 2022 sanctions on Russia's central bank, non-aligned central banks
  bought **gold** instead of Treasuries (Levine). That flow accelerated after April 2 2025. The dollar
  fell ~**10%** in H1 2025.
- *Pegs, crawling pegs and the RMB* (FX101 episode and short, Apr 2025): China's renminbi (units: yuan)
  is not free-floating. From the mid-1990s it was pegged to the dollar at an artificially low rate,
  maintained by buying dollars, which built China into an export power. In 2005 it moved to an
  undisclosed basket within a tight band (a "dirty float" or crawling peg), effectively re-pegged in
  2008, and devalued in 2015 and 2019, each feeding US "currency manipulator" charges. When an
  influencer cited the yuan at an 18-year low as proof the US was "winning" the trade war, Jen's answer
  was that the dollar was falling too: "we are losing together."
- *Who wins from a weak dollar:* a weaker currency helps a country that depends on exports and hurts its
  consumers abroad (Kristen's vacation framing). For a consumption-heavy importer like the US it is a
  strange goal, which is why the hosts read dollar weakness in April 2025 as a warning rather than a win.
- *Hedging costs drive flows* (Hornbach, Sep 2025): a Japanese investor who buys US stocks and sells the
  dollars forward to strip out FX risk pays roughly the rate differential to do so. As the Fed cuts, that
  hedge gets cheaper, foreigners hedge more, and hedging means *selling* dollars forward. Morgan Stanley
  called the dollar down from early 2025 (against consensus) and saw ~10% more to go.
- *Trade construction (FX desk short):* "short cable" means short GBP/USD at ~1.30, target 1.25, stop
  1.35. The trainee is mocked for a symmetric, coin-flip risk/reward with no thesis. Jen's lesson: the
  manager should have coached the inputs and logic rather than hazing her.

**Business significance.** For importers the dollar sets landed cost. For exporters it sets
competitiveness. For the Treasury it sets foreign appetite for its auctions. Medeiros calls the dollar
**the relief valve**: if markets start to believe policy will be set well below where it should be,
the dollar falls first, and then inflation expectations follow.

**Forces & impact.** Policy credibility (§6), rate gaps, capital repatriation (US equities lagged the
rest of the developed world over 12 months to Jan 2026 even with AI), and sanctions risk. Second order:
a weaker dollar helps gold, crypto and (on Jen's speculation) stablecoins, which feeds back into bill
demand (§8).

**With vs. without.** Without the dollar's reserve role, the US would borrow at a higher term premium
and could not run persistent deficits as cheaply. The hosts treat losing it as the tail risk behind
April 2025: "for the first time in my lifetime." Without intervention capacity, Japan's only defense
would be selling Treasuries, which would push US yields up (Adami).

**Applies when / Breaks when.** The rate-differential rule holds in normal regimes. It breaks when
credibility or fiscal fear dominates. In 2025 the dollar fell even as US rates stayed high.

**Channel example.** *I got the chance to ask Scott Bessent* (Sep 2026, intervention and de-dollarization);
*What You Must Know About Commodities feat. Guy Adami* (2024, yen); *Time to Sell? feat. Alicia Levine*
(Jan 2026, gold and central banks); *FX desk hazing rituals* (short); *FX101, Operation Twist and Yale's
$6bn Sale* (Apr 2025); *Essential FX 101 (USD / RMB) for Understanding the US / China Trade War* (short);
*Fixed Income Strategy 101 feat. Matt Hornbach* (Sep 2025).

**Counterpoint.** "A weak dollar means we owe foreigners less" is true of their purchasing power. It also
raises US import prices and future borrowing costs, so it is not a free deleveraging. Lloyd Blankfein's
retort, relayed by Kristen, is the strongest counter to de-dollarization panic: where else would they
put the money? Jen's RMB history is self-described cliff notes ("not an FX expert"); the broad
sequence is right, though the 1994 unification and the 2005–08 managed appreciation (~20%) are
compressed. Hornbach's 2020 short-dollar call took months to work, which he concedes.

**Links.** [E9 lesson](../lessons/exec-E9-geopolitics-macro.html) (tariffs as value swings) ·
[[canon-meadows-thinking-in-systems]] (the dollar → expectations → inflation loop; reflexivity proper,
à la Soros, is not yet in the canon).

---

## 15 · Carry and the yen carry trade

**What it is.** **Carry** is what a position earns (or costs) if nothing moves: the difference between
the rate you receive on what you own and the rate you pay to fund it. Jen's correction of the
private-equity usage: carry here is the gap between where you invest and where you fund, not carried
interest. A **carry trade** borrows in a low-yielding currency and invests in a high-yielding one. The
**yen carry trade** is the canonical version: borrow yen near zero, buy dollars (or Aussie dollars, or
emerging-market currencies) and pocket the differential.

**How it works.**
- *Exchange rate as the price of two monies* (John Normand, ex-JPM head of cross-asset strategy, now
  at AustralianSuper; spring 2024): one money pays X, the other pays Y, and a lot of cash simply moves
  from low yield to high yield. In 2024 US real rates were positive and Japan's negative, a gap near a
  **30-year wide**, and dollar/yen sat near a 30-year high. That is the carry trade showing up in the
  spot rate.
- *Why the yen:* after the Nikkei bubble burst in 1989–90, deflation pinned Japanese rates near zero for
  three decades, so the yen became the safe **funding currency**.
- *The payoff shape:* "up by the stairs, down by the elevator shaft." Long stretches of low-volatility
  gains in the high-yielder, then a macro shock in the high-yield economy (commodities halving in the GFC
  crushed the Brazilian real, Mexican peso, Aussie and Kiwi) wipes out years of carry in weeks. The skill
  is timing the shock, and most people don't.
- *Normand's 2024 forecast:* Fed cuts ~75bp over the cycle, the BOJ hikes ~100bp once a quarter, the
  differential narrows but still favors the dollar, global demand for US AI equities keeps the dollar
  bid, and the yen appreciates **5–10% at most**.
- *Carry elsewhere in this note:* a bond financed in repo (5% coupon − 4% GC = **+1%**, plus roll-down,
  §10); a curve steepener as **negative** carry, paid as rent while you wait (§3); Eisman's 2006 subprime
  short, where shorting New Century stock cost ~**20%** a year in dividends plus borrow while buying
  protection on the BBB− tranche two floors up the "building" cost ~**3%**. Same view, one-seventh the
  carry.
- *2026 coda* (Feb 2026 episode): the BOJ hiking, Japanese underlying inflation near target and a weak
  yen while the Nikkei set records. For Japan, after decades fighting deflation, higher rates read as
  good news, and the summer 2026 joint US–Japan intervention (§14) was the policy response to the yen end
  of the trade.

**Business significance.** Carry trades move trillions across borders, so they set exchange rates for
every importer, exporter and foreign investor. An equity investor who ignores the currency can see a
good stock trade turned into a bad one by a 20% FX gap in a quarter (Normand). For a corporate treasurer,
borrowing in the low-rate currency is the same trade: cheap until the funding currency jumps.

**Forces & impact.** Rate differentials (central-bank paths in both countries), volatility (carry
works when vol is low and dies when it spikes), risk appetite, and capital flows into the high-yielder's
assets. Second order: because everyone is short the same funding currency, an unwind forces simultaneous
buying of it, so the funding currency rallies into a crisis, and the move feeds on itself.

**With vs. without.** Without carry trades, interest-rate gaps would sit unarbitraged and currencies
would track trade flows more closely; high-rate economies would attract less foreign capital. With
them, capital flows to yield in calm times and stampedes back in shocks, which exports one country's
easy money into another's asset prices.

**Applies when / Breaks when.** Works when the differential is wide and stable and volatility is low.
Breaks on a shock to the high-yielder, on a surprise from the funding central bank, or when positioning
gets crowded enough that a small move forces stop-outs.

**Channel example.** *Finance, Philosophy, and the Yen Carry Trade feat. John Normand* (2024); *Tariffs
101* (Apr 2025, carry as the reason a dovish Fed should weaken the dollar); *Steve Eisman, the Real-Life
"Big Short" Investor* (Apr 2025, negative carry of the New Century short); *SaaS-pocalypse, misleading
jobs data, and Japanese equities breaking records* (Feb 2026).

**Counterpoint.** Normand's "5–10% max" was overrun within months: in July–September 2024 dollar/yen fell
from ~161 to ~140, roughly 13%, in a violent carry unwind after a BOJ hike and weak US data, which is
the elevator shaft he described arriving faster than he forecast. Kristen's phrase "intervention from
the Bank of Japan" is loose: Japan's Ministry of Finance decides FX intervention and the BOJ executes it.
Normand works for a pension fund and is selling a long-horizon, stay-invested view; carry is one input
to currencies, not the whole model, as he says himself.

**Links.** [[canon-taleb-black-swan]] (steady gains, rare crushing losses) ·
[[canon-taleb-antifragile]] (carry as short optionality) · [[wss-trading-hedge-funds]] (macro funds and
crowding) · [[canon-perrow-normal-accidents]].

---

## 16 · Tariffs and the April 2025 safe-haven break

**What it is.** A **tariff** is a tax on imports, paid by the *importing business* to its *own*
government. Who ultimately bears it depends on who gives up margin. The April 2025 "reciprocal" tariffs
turned that textbook question into a market event: for the first time in the hosts' careers, US stocks,
Treasuries and the dollar sold off *together*, which is not what a safe haven does.

**How it works.**
- *Incidence, in three branches* (Tariffs 101 and short): a foreign maker sells a microphone to a US
  importer for **$50**; the importer marks it up **$50**; the consumer pays **$100**. Add a **$10**
  tariff, paid to US Customs, and either the foreign maker cuts to $40, or the US importer cuts its markup
  to $40, or the consumer pays **$110** (or buys something else). Most near-term cost was expected to land
  on US firms and consumers, because exporters weren't willing parties and many US firms run thin margins.
- *The reciprocal formula* (Apr 2 2025): take US goods imports from a country minus US exports to it,
  divide by imports, call that the country's "tariff rate," then halve it. Imports $200, exports $100:
  (200 − 100) / 200 = 50%, halved to **25%**. Floor of **10%** on everyone. Results: China **34%** on top
  of an existing 20%, EU **20%**, Japan **24%**, autos **25%**, Canada and Mexico already at **25%**
  (Canadian energy 10%), and an uninhabited penguin island on the list. The formula measures the goods
  trade *deficit*, not any tariff the other country charges, and ignores services, where the US runs a
  surplus.
- *History the hosts used:* the Fordney–McCumber Act (1922) took average import duties to ~40%;
  Smoot–Hawley (1930) added ~20% more on everything, drew retaliation and deepened the Depression; the
  Reciprocal Tariff Act (1934), postwar GATT and the WTO then ran a century of liberalization. Trump's
  first term (2018: washing machines and solar at 30–50%, steel and aluminum 10–25%) was largely kept by
  Biden.
- *The macro read:* tariffs mean slower growth and higher prices, i.e. **stagflation**. Markets priced
  the Fed fighting the growth side (more cuts), and Jen predicted a **steeper curve**: companies would
  "lever their way out" rather than grow out.
- *The break* (Apr 2–11 2025): equities fell, the 10-year rallied briefly to ~**3.9%** and then sold off
  to ~**4.5%**, the dollar hit a 3-year low and gold soared. With a risk-off move, safe-haven demand
  should have strengthened the dollar and pulled yields down. It did neither. The hosts read it as the
  market pricing a real chance that the dollar loses reserve status, plus the auction evidence in §8;
  the 90-day pause came minutes after the 10-year auction.
- *The plumbing link:* the world earns dollars by selling to the US and recycles them into dollar assets,
  mainly Treasuries (foreigners hold ~25–30%). Fewer imports mean fewer recycled dollars, so trade policy
  is also Treasury-demand policy (§14).
- *The "deliberate crash to refinance" theory* (short and Apr 11 episode): ~$9.1T of debt rolls each year
  out of $36.2T, so lower rates would help. But the Fed sets only the front end, the rolling debt is
  mostly bills, and long yields *rose*. The hosts treat the theory as debunked by the price action.
- *GDP fallout* (Apr 30 2025 episode): Q1 GDP contracted (advance −0.3%) as firms pulled imports forward
  ahead of tariffs, with net exports subtracting ~5 points. Jen expected the same next quarter.
- *The fiscal contradiction:* if tariffs are a negotiating tactic ending in a few 5–20% deals, they raise
  too little to dent the deficit; if they are meant to fund tax cuts, they must be high and permanent.
  The equity market was pricing both at once.

**Business significance.** For operators, the questions are incidence and lead time: who in your
supply chain eats the tax, and how many days of inventory you have before it reaches shelf prices (§13).
Small importers are hit hardest because large firms can lobby for carve-outs. For capital markets, the
episode is the clearest live demonstration that the US "risk-free" rate has a credibility component.

**Forces & impact.** Trade balances, retaliation, inventory cycles, the reserve-currency recycling loop,
and political feedback (the administration reversed course when bond and equity markets moved together).
Second order: higher input costs tighten leverage covenants and widen credit spreads (§1), private
equity exits stall, and LPs over-allocated to illiquid assets seek secondaries.

**With vs. without.** Without tariffs since the 1930s, the US built the world's deepest consumer market
and the dollar's reserve role on trade deficits recycled into Treasuries. With sweeping tariffs imposed
at once, that recycling loop is put at risk, and the hosts' fear is a vacuum filled by a basket of
allied currencies or gold.

**Applies when / Breaks when.** Incidence logic always applies; the split depends on pricing power and
substitutes. The safe-haven assumption applies while the US is seen as the safest counterparty; it broke,
briefly, when US policy itself became the shock.

**Channel example.** *Tariffs 101: Why the Markets and U.S. Dollar Are Tanking* (Apr 4 2025); *What are
tariffs and how do they work?* and *Is Trump deliberately trying to crash the U.S. stock markets?*
(shorts); *It Wasn't Equity Turmoil That Spooked Trump — It Was the Bond Market* (Apr 11 2025); *Steve
Eisman, the Real-Life "Big Short" Investor, on Tariff Panic* (Apr 11 2025); *From Intern to Offer…
(Plus Some Markets and Tariff Talk)* (Apr 30 2025).

**Counterpoint.** **Steve Eisman**, recorded the same afternoon, is the strongest counter and the hosts
air him in full. His case: the tariffs answer a real grievance (NAFTA and China's WTO entry grew GDP but
hollowed out towns), and the US holds the cards because exports are only ~**11%** of US GDP versus ~19%
officially for China (he guesses ~30% counting transshipment), 30%+ for Europe, 40%+ for Germany and
~35% for Canada and Mexico, 25 points of it to the US. Partners will negotiate. On the dollar: the global
financial system runs on Treasuries, overnight repo is trillions of dollars collateralized by them, and
"there is no alternative." He told Jen she sounded hysterical, and she owned it ("I'm a bond girl").
The market partly agreed with him: equities recovered to near pre-April levels within weeks. Other
corrections: the GDP discussion leaves investment out of the GDP identity (inventories absorbed
much of the import surge), and Jen's "another hit next quarter" was wrong, as Q2 printed about +3% when
imports collapsed. The 1970s "rates north of 20%" was 1980–81 under Volcker. And the hosts' insistence
that they are apolitical sits awkwardly with episodes that are, by their own account, mostly opinion on
a policy.

**Links.** [E9 lesson](../lessons/exec-E9-geopolitics-macro.html) (tariffs, chokepoints, value
swings) · [[canon-schelling-strategy-of-conflict]] (the "bazooka" as a commitment device) ·
[[canon-dixit-nalebuff-thinking-strategically]] (who saved something for the swim back) ·
[[canon-mankiw-principles-of-economics]] (tax incidence) · [[wss-private-markets-wealth]] (denominator
effect and secondaries).

---

## 17 · Recession indicators

**What it is.** These are signals that the cycle is turning. The serious ones are the inverted yield
curve, labor-market breakevens, and credit and financial conditions. The folklore ones are
consumer-behavior proxies that sometimes rhyme with spending stress.

**How it works.**
- *Curve:* every inversion has preceded a recession by **18–36 months**. Adami's refinement is that the
  *re-steepening* after a long inversion is the danger signal, not the inversion itself. The 2022–24
  inversion was the longest on record, and there was no recession.
- *Labor breakeven:* 90% of labor-force growth since Q3 2023 was foreign-born. With immigration
  reversing, the payroll gain needed to hold unemployment steady falls to ~**40–50k/month** (Medeiros,
  Jan 2026). 75k a month is then *tightening*, not weakness. Payroll headlines must be read against a
  moving breakeven.
- *First prints vs. revisions* (Feb 2026): January payrolls printed **+130k** against ~70k expected and
  the market priced out a March cut. Jen's point was the revisions: 2025's monthly average gain was cut
  from ~49k to ~15k, with Challenger layoffs at post-GFC highs. Discount first prints when the pattern is
  revision after negative revision.
- *How a macro PM trades the print* (Ashish Goyal, ex-BlueCrest/Citadel/Balyasny, early 2024): a
  250k payroll against 200k expected moves front-end yields 5–15bp, about one cut priced out. If the
  broader trend still points to cuts, keep receiving into the move. The hard part is surviving the path:
  stop-losses on a $100mm book shrank from ~$10–12mm fifteen years ago to ~$4–6mm.
- *GDP is backward-looking* (Apr 2025): Q1 2025's contraction was mostly tariff front-running in
  imports, and reversed the next quarter. Confidence surveys and inflation expectations are the
  forward-looking exceptions.
- *Folklore (two shorts):* the hemline index (1926), lipstick (Lauder, 2001), high heels, cardboard-box
  demand ("very real", reportedly watched by the Fed), men's underwear (attributed to Greenspan), plus
  the hosts' own joke "Bravo index" (Real Housewives 2008; Scandoval and SVB 2023).
- *Allocator rule (Levine):* the question is not "will stocks fall?" but "is there a recession?" At
  ≤30% recession probability, stay invested. In 2025 the S&P returned **16.5%** fully invested and
  roughly **−12%** if you missed the 10 best days, all of which followed the worst days in April. Buying
  at all-time highs has historically not lowered 1/3/5-year returns (BNY study).

**Business significance.** Recession probability sets hiring plans, inventory, capex timing and debt
tenor. Getting the *breakeven* wrong means misreading a healthy labor market as weak (or the reverse) and
cutting too early.

**Forces & impact.** Curve signals work through bank margins and credit supply with long lags. In 2023–25
the lag was broken by fiscal support and a private sector that had locked in low rates, which made the
economy less rate-sensitive (§3). AI could change the growth–employment relationship ("a coefficient
shift"), which would make historical breakevens unreliable.

**With vs. without.** Without leading indicators, firms react to recessions after the layoffs. With
overfit indicators, they de-risk into a boom, which is the 2023 "recession that never happened"
(Levine: "we're still waiting for the recession of 2020").

**Applies when / Breaks when.** The curve works when the inversion reflects restrictive policy. It
weakens when the long end is suppressed by QE or flight-to-quality, or when term premium is
structurally changing. The folklore indices are entertainment. The hosts present them that way, and
only cardboard-box demand has a plausible economic mechanism.

**Channel example.** *Top 5 wildest recession indicators* / *Top 10… signs* (shorts); *Every New Fed
Chair…* (curve inversion 2006); *Commodities feat. Guy Adami* (2024); *Time to Sell? feat. Alicia
Levine* (Jan 2026); *SaaS-pocalypse, misleading jobs data…* (Feb 2026); *Portfolio Manager at World's
Top Hedge Funds… Breaks Down Global Macro Trading* (2024); *From Intern to Offer…* (Apr 2025).

**Counterpoint.** Levine runs a wealth-management business whose clients stay invested, so "stay
invested" is good advice *and* good for her business. The 10-best-days stat ignores that you also miss
the worst days, and that the two cluster together. "Every inversion preceded a recession" survives
only if 2022–24 is still "early." Jen's "January is a head fake" was a labeled view, and the
revision arithmetic as transcribed (~43k total) doesn't match a 49k → 15k monthly cut, which implies
~400k over a year; check the BLS benchmark before reusing it.

**Links.** [[canon-taleb-black-swan]] (indicator overfitting) · [[canon-kahneman-thinking-fast-and-slow]]
(narrative fallacy in folklore indices) · [[canon-tetlock-superforecasting]] (base rates for "inversion →
recession").

---

## How the concepts connect

```
Tariffs (§16) / oil shock ──► headline inflation (§13) ──► Fed reaction function (§4, §5)
     │        │                                                   │
     │        │                          front end reprices ◄─────┘  (futures odds, DV01 losses §2)
     │        ▼
     │  inflation expectations ──► long-end term premium (§3) ◄── deficits, long-end supply,
     │        │                         ▲                         hyperscaler issuance, pension unwind
     │        │        credibility / independence (§6) ──► the dollar = relief valve (§14)
     │        │                                                   │
     │        │                    rate gaps ──► carry trades (§15) ──► elevator-shaft unwinds
     ▼        ▼
fewer recycled dollars ──► weaker auction demand (§8) ──► 10-year yield
                                                              │
     ┌────────────────────────────────────────────────────────┤
     ▼                                                        ▼
mortgage = 10y + spread (§12)                corporate yield = 10y + credit spread (§1)
     │                                                        │
housing politics ──► GSE buying               covenant math ──► spreads widen
                                                              │
Treasury response: buybacks + issuance mix (§9) ──► shorter WAM ──► rollover risk
     │                                     │
bill supply ◄── stablecoins, Fed bill      repo / reserves plumbing (§7, §10)
     reinvestment (§7, §8)                       │
                                                 ▼
             cash vs futures vs swaps (§10, §11): balance sheet decides who holds duration
                                                 │
                     levered basis trade (§11) ──► forced selling when repo or cash cheapens
                                                    (2019, Mar 2020, Apr 2025 template)
```

April 2025 ran across the top of this chart: tariffs threatened the dollar-recycling loop, so
Treasuries, the dollar and stocks fell together; swap spreads collapsed and basis trades unwound as
cash Treasuries cheapened against derivatives; and the administration paused within a week. The 2026
sequence ran down the middle. The Iran oil spike lifted 2s and 10s 50–60bp (macro funds lost on DV01 and
crowded steepeners). Mortgages rose 75bp with the Fed on hold. Political pressure to "do something" about
affordability produced GSE buying and Treasury buybacks. The Treasury's issuance choice may have
tightened the front end even as it supported the back. And a balance-sheet-hawk chair hiked because
financial conditions, not the policy rate, were the true measure of tightness. Underneath both, the
question of *who has balance sheet to hold duration* (real money in futures and swaps, levered funds in
cash bonds, dealers forced to take down auctions) decides how violently a shock moves yields. **The
single recurring lesson: the Fed controls one point on the curve. Everything a business actually borrows
at is set by the market, and in 2025–26 by the Treasury, the GSEs and the plumbing as well.**

---

## Retrieval questions

1. **The Fed holds rates steady but mortgage rates jump 75bp. How?** Mortgages price off the 10-year
   plus a spread. An oil shock lifted inflation expectations and term premium at the long end, which the
   Fed doesn't set.
2. **Two traders each lose on a $100mm Treasury position. The 2-year moved 60bp, the 10-year 50bp. Who
   lost more, and why do desks avoid this comparison?** The 10-year trader: duration 8 vs. 1.8, so ~$4mm
   vs. ~$1.1mm. Desks size by DV01, not notional, so risk is comparable across maturities.
3. **Treasury yields fall in a tariff panic. Why might a leveraged company's borrowing cost still
   rise?** Its yield = risk-free + credit spread. Lower EBITDA pushes leverage toward covenant limits
   (4× → 8× on unchanged debt), and spreads widen more than Treasuries fall.
4. **Fed funds futures for a 30-day month price at 96.29, the effective rate is 3.63, and the meeting is
   on day 16. What hike probability is priced?** (30×3.71 − 16×3.63)/14 = 3.80; (3.80−3.63)/0.25 ≈ 68%.
5. **Why is a Fed buying $71B of Treasuries at auction during QT not QE?** It is reinvesting most of $76B
   of maturing SOMA holdings. The balance sheet still shrinks, and no net new reserves are created to
   push long yields down.
6. **The Treasury doubles long-end buybacks. Under which funding choice is this a stealth *tightening*,
   and under which is it QE-like?** Funded with 2s/5s it adds front-end duration supply, which raises
   front yields and flattens the curve. Funded from TGA cash it injects new liquidity, which looks like
   QE.
7. **Why can a dovish appointee not simply cut rates?** The FOMC is a 12-vote majority committee, and the
   chair has no veto. Miran could only dissent.
8. **Medeiros says policy is loose with the 10-year at 4.15%. What is his evidence, and its weakness?**
   10y yields ~300bp below nominal GDP growth, easing financial conditions, IG demand at the tights. The
   weakness: one quarter's 8% NGDP flatters it, and trend nominal growth is lower.
9. **Why would a portable 50-year mortgage carry a much higher rate than a 30-year?** The collateral can
   change, and the borrower's option to keep a low rate becomes near-certain to be valuable, so the
   lender is short a much more expensive option. The DV01 difference between 30 and 50 years is small.
10. **The curve bull-steepens in the US and bear-steepens in Europe in the same year. What different
    stories do they tell?** US: front-end yields fell on expected cuts. Europe: long-end yields rose on
    fiscal-driven term premium despite ~200bp of ECB cuts. The policy rate and the long end decoupled.
11. **Why does the Fed prefer PCE to CPI?** It captures substitution in real time and spending made on
    consumers' behalf, so it describes total consumer spending, the behavior rate policy targets.
12. **A record share of direct bidders at a 7-year auction. What can and can't you infer?** Strong
    demand (it stopped 2.5bp through). Foreign official demand mostly shows up as *indirect* bids via the
    NY Fed, so reading "direct = China" is unreliable.

13. **A real-money manager can get 10-year exposure by paying cash, financing in repo, buying futures or
    receiving fixed in a swap. Why does that choice make futures trade rich to cash bonds?** Futures and
    swaps use far less balance sheet, so real money crowds into them; the deliverable cash bonds are left
    cheap, which is the gap basis traders lever up to capture.
14. **Why can a near-riskless convergence trade blow up a hedge fund?** The gap is a few bp, so it needs
    20:1 or more leverage; a shock that cheapens cash against futures, or a repo spike, produces
    mark-to-market losses and margin calls before expiry, forcing sales of illiquid bonds into a falling
    market.
15. **You are short 78,000 TY contracts; the CTD has DV01 6.6 and conversion factor 0.99. What is your
    risk per bp, and what is wrong with the video's method?** ≈ 6.6 / 0.99 / 10,000 × 78,000 × $100,000
    ≈ $5.2mm. The video multiplies by the factor (≈ $5.1mm); futures track the CTD price divided by its
    factor.
16. **Swap spreads go from −20bp to −30bp. Is that widening or tightening, and what might it say?**
    Tightening, by desk convention inherited from the positive-spread LIBOR era. Treasuries are
    cheapening against swaps: scarce dealer balance sheet, heavy supply, or aversion to holding cash
    Treasuries (April 2025).
17. **Why did SOFR replace LIBOR, and what did the switch remove from the benchmark?** LIBOR was
    self-reported, unsecured and manipulable; SOFR is computed from secured overnight Treasury repo
    trades. The switch removed the bank-credit and term components, which is why legacy loans needed
    credit spread adjustments and term SOFR is thin.
18. **A carry trade has earned steady returns for three years. What does its history say about the next
    month?** Little, except that losses arrive suddenly: carry pays "up by the stairs" and unwinds "down
    the elevator shaft" when the high-yielder suffers a shock or the funding currency's central bank
    surprises (yen, summer 2024).
19. **A $10 tariff lands on a $100 product built from a $50 import. Name the three ways it can be
    absorbed, and say why April 2025 broke a market rule.** Foreign margin, US importer margin, or the
    consumer price. Stocks, Treasuries and the dollar fell together, so the "risk-free" asset behaved like
    a risk asset; the market was pricing US policy credibility.
20. **The reciprocal tariff on a country with $200 of US imports and $100 of US exports?**
    (200 − 100) / 200 = 50%, halved to 25% (floor 10%). It measures the bilateral goods deficit, not the
    country's own tariffs, and ignores services.
21. **Why do Fed cuts move mortgage payments less today than in 2006?** Almost no outstanding mortgages
    float (Patton: under 1% vs ~35% pre-GFC), most borrowers are locked in below market, and only ~10% of
    a mortgage's rate sensitivity sits on the 30-year point, while long yields can rise even as the Fed
    cuts (Sep 2024).

---

## Gaps

Pass 2 recovered nearly every title the first version listed as missing; the dedicated videos on the
basis trade, SOFR, futures DV01/CTD, the yen carry trade, Hornbach, Patton, Operation Twist, tariffs and
the April 2025 bond-market episode are now folded in. **Still missing from the folder** (checked by video
ID against `wss_all_videos.json` / `wss_all_shorts.json`):

- *What are inflation breakevens in bond trading?* (`kkKIq_WxWnU`): §13 supplies the TIPS decomposition
  itself; the channel's explanation and numbers are still unseen
- *How are Trump's reciprocal tariffs calculated?* (`ynHja5RlMN4`): the formula is taught in *Tariffs
  101* (§16), so this short likely adds little
- *Do you know the answer to this bond math 101 question?* (`Zxy3I26G2nI`)
- *Wellington's Head of U.S. Macro with one simple rule for trading the long end* (`ztEWvYczl8w`):
  almost certainly a clip of the Jan 2026 Medeiros episode already used in §5

**Read, little or no change:** *Pete Muller on Building… PDT* and *Quant Investing 101 feat. Stacie
Mintz* (quant equity; only the 2007 quant unwind and Liberation Day as a factor shock); *Who needs karate
when you have the DCF* (no content); *The most underrated show on TV* (prop trading vs client flow,
covered in [[trading-floor-mechanics]]); *Why Jamie Dimon Won't Buy Stocks OR Bonds* (already used);
*Debt Capital Markets 101* and *Fixed Income Sales & Trading 101* (2023 beginner material on the yield
stack and price/yield inversion that §1 already teaches; their 5% Treasury and 98/100 bid-offer figures
are illustrative).

**Concept gaps the transcripts still leave open:** breakeven and real-yield *levels* over the cycle; how
the Taylor rule is computed (inputs named, never shown); the 2026 dot plot's median path; the implied
repo rate and how CTD switches as yields cross 6%; options and swaptions as a way to express rate views
(mentioned by Jen and Goyal, never taught); why foreign official demand shows up as indirect bids (the
hosts treat it as direct).
