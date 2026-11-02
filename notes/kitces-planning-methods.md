# Kitces planning methods: rebalancing bands, asset location, the bond tent, and tax risk

> **Sources:** Michael Kitces, *Nerd's Eye View* (kitces.com). Pulled 2026-11-01. Nine full posts: tolerance-band
> rebalancing (2016), two asset-location posts (2013, 2015), yield-split asset location (2022, Kitces team), the
> portfolio size effect and bond tent (2016), three rising-equity-glidepath posts with Wade Pfau's research (2013,
> 2014, 2014), and the IRS Section 351 / ETF tax-risk post (Oct 28 2026). Plus the 11-item RSS feed (Oct 15 to
> Oct 30 2026), which is mostly practice-management content for advisors. Raw corpus is local-only in
> `_ingest/raw/2026-11-01/kitces-planning-methods/` (gitignored). Summarized in own words.
>
> **What it adds:** [[portfolio-methodology-educators]] names Kitces as a teacher for steps 3, 4 and 8 but cites
> him in one line each. This note records the actual rules, the numbers behind them, and the conditions where they
> stop working.
>
> **Maps to:** **E11** (personal operating system), **Course 07** (decisions under uncertainty), extends
> [[unit-10-personal-finance-operating-system]].
>
> **Lens:** **Decide**. **Steps served:** 3 (implementation and asset location), 4 (rebalancing), 8 (review
> cadence). Also touches 2 (the glidepath around retirement).
>
> ⚠ **Bias.** Written for financial advisors, not individuals; much of the value framing is "how an advisor shows
> value" (tax alpha, rebalancing software). Kitces is Head of Planning Strategy at Focus Partners Wealth and
> co-founded several advisor-tech businesses. The core research posts are 10+ years old and many of their numbers
> assumed the 2013–2016 low-rate world. US tax rules only. Not advice.

---

- **Core claim:** Most of what an individual can control after picking the asset mix is *process*: when to
  rebalance, which account holds what, and how much risk to carry in the decade either side of retirement. Each
  has a rule that beats the folk default (calendar rebalancing, "bonds in the IRA", a steadily falling equity
  share), and each rule depends on a condition worth writing into the IPS.

## Framework

### 1. Rebalance on bands, not on the calendar (step 4)
- Frequent calendar rebalancing (monthly, quarterly) barely lowers risk, adds almost nothing to return, and
  racks up costs. It also cuts winners short in a trend and buys too early into a slide.
- Better: let weights drift, check often, and trade **only the holding that breaches its band**.
- Use **relative** bands, not absolute ones. An absolute ±10-point band on a 10% sleeve almost never triggers;
  on a 50% core it triggers often. A relative band scales with the position.
- Evidence cited: Gobind Daryanani's 2007 *Journal of Financial Planning* study ("Opportunistic Rebalancing",
  rolling 5-year periods, 1992–2004) found a **±20% relative band** worked best; 10–15% traded too much and 25%
  missed opportunities.
  - 60% stock target: act at 48% or 72%. 10% sleeve: act at 8% or 12%.
- Cost of the method: it needs frequent *looking* (or software), even though trades are rare.
- ⚠ The 20% figure comes from one 13-year window. Treat it as a reasonable range (15–25%), not an optimum.
  Compare Swedroe's 5/25 rule in [[portfolio-methodology-educators]], which is tighter on large sleeves.

### 2. Asset location depends on horizon and expected return, not just "tax efficiency" (step 3)
- The rule of thumb puts tax-inefficient bonds in tax-deferred accounts and stocks in taxable. Kitces argues it
  is often wrong:
  - When bond yields are low, there is little to shelter, and the high-growth asset gains more from deferral.
  - Over a long enough horizon, dividends plus **any** turnover create a yearly tax drag that can make holding
    stocks in the IRA better, even though IRA withdrawals are taxed as income.
- So location is a function of three things: tax drag, expected return, and **time horizon**.
- Size of the prize: research he cites puts good location at **20–50+ bp a year** (2013 post); the 2022 post
  estimates ~10 bp a year from location and another ~10 bp from **yield-splitting** (replace a total-market fund
  with a low-yield growth fund in taxable plus a high-yield value or bond fund in tax-deferred), compounding to
  roughly **6% more wealth** over several decades.
- Teaching point for the IPS: list each holding's yield and turnover, rank by tax drag, fill the most sheltered
  account with the worst offender. Re-run when rates change, because the ranking flips with yields.

### 3. The retirement red zone, the bond tent, and the rising glidepath (steps 2 and 8)
- **Portfolio size effect:** in the ~10 years before and after retirement, the portfolio is at its largest and
  new contributions are tiny next to market moves. Sequence risk peaks here.
- **Bond tent / V-shaped glidepath:** equity share starts high, falls into retirement (build a bond reserve),
  then **rises again** in the first half of retirement as the bonds are spent.
- Kitces and Pfau's simulations (4% withdrawal, assumed real returns 6.5% stocks / 2.4% bonds): starting at 30%
  equities and gliding to 70% had a **95.1%** success rate versus **93.2%** for a static 60/40, with a *lower*
  average equity share. The logic: bad early markets mean you buy equities cheaply as you glide up; good early
  markets mean you are already safe.
- Refinements:
  - **Accelerate:** reach the target equity share in ~15 years, then hold it; the late-life increase adds little.
  - **Use T-bills as ballast** if bond-heavy early years carry rate risk.
  - **Valuation overlay:** a high Shiller CAPE at retirement predicts when the rising path matters; a low CAPE
    means a static or even declining path does fine. Kitces frames this as risk management, not market timing.
- Bucket strategies (cash / bonds / stocks pools) quietly *are* a rising glidepath once the safe buckets are spent
  and not refilled. Much of their benefit comes from that, not from the mental accounting.

### 4. Tax risk is a second risk axis (step 3, Oct 2026)
- **Revenue Ruling 2026-20:** the IRS ruled that one variant of a **Section 351 ETF conversion** is taxable: when
  securities that don't fit the ETF's mandate are swapped out through an Authorized Participant as part of the
  same plan, the ETF is not treated as an independent intermediary. It did **not** restrict 351 conversions in
  general, which leaves a large gray zone.
- **Notice 2026-62** (comment period; guidance could be retroactive) flags: an exchange-fund/partnership variant
  of 351, box-spread ETFs that turn interest-like income into deferred gains, ETFs that rotate around dividend
  record dates, ETFs that bend the RIC qualifying-income rules, and some offsetting-character trades.
- Kitces's method, which ports well to any tax-motivated product:
  1. **Investment case first:** would you still own it if the tax benefit came in far smaller?
  2. Net benefit if it works (after fees, financing, and the fact that much of the "saving" is deferral).
  3. Total cost if it fails (tax, interest, penalties, professional fees).
  4. Strength of the position (independent tax adviser; is any legal opinion updated for the new guidance?).
  5. Separate **tax-risk tolerance** (will you accept an audit or a Tax Court fight?) from **tax-risk capacity**
     (could you pay a large bill plus penalties?). It mirrors the risk tolerance vs capacity split in step 1.
- ⚠ Faber/Cambria promote 351 exchanges commercially ([[portfolio-methodology-educators]]); check the current IRS
  position and get independent advice before acting. Not verified against the IRS text itself, only Kitces's
  summary.

## Applies when
- US investor with a mix of taxable, tax-deferred and Roth accounts (location only matters with more than one).
- A written target allocation exists (bands need a target).
- Within ~10 years of a planned retirement or drawdown (bond tent, glidepath).

## Breaks when
- **One account only** (all in a 401(k) or all in taxable): location is moot, and yield-splitting just adds funds.
- **Taxable rebalancing:** selling the breaching holding realizes gains. Rebalance with new contributions,
  withdrawals and dividends first; bands interact with tax-loss harvesting.
- **Rates regime change.** The location and T-bill-ballast arguments were built when bond yields were near zero.
  With 4–5% yields, the case for sheltering bonds is stronger again, so the ranking can flip. Re-run the math.
- **Assumed returns.** The glidepath success rates come from simulations with fixed real returns and a 4% rule;
  they are sensitive to both. ERN's historical work reaches similar conclusions but different numbers.
- **Behaviour.** A rising equity share at 75 needs a retiree who can watch a larger equity drawdown late in life.
  The research shows the path works; it does not show people stick to it.

## Practitioner counterpoint
- Big ERN and Pfau broadly agree on rising glidepaths in retirement; Ayres & Nalebuff and Cederburg et al. argue
  about the *accumulation* glidepath instead, which Kitces doesn't address.
- Rebalancing-timing luck (Hoffstein) says the *date* you rebalance matters more for factor strategies than
  the band width. Bands partly fix this because they trigger on drift, not on a date.
- Much of the "tax alpha" story is advisor marketing: 10–20 bp a year is real but small next to fees. An investor
  paying a 1% advisory fee to capture 20 bp of location alpha has lost the trade.

## What to put in the IPS (from this note)
- `Rebalance: check monthly; trade a sleeve only if it drifts beyond ±20% of its target weight (relative). Use
  cash flows before sales in taxable.`
- `Location: rank holdings by yield × turnover; re-rank whenever 10y yields move ±1 point.`
- `Pre-retirement: from T–10 years, build a bond reserve to N years of spending; spend it first; let equity share
  rise back to target by T+15.`
- `Tax-motivated products: investment case first; record tolerance and capacity for tax risk.`

## Links
[[portfolio-methodology-educators]] (steps 3, 4, 8) · [[unit-10-personal-finance-operating-system]] ·
[[bet-sizing-conviction]] (sizing under estimated, not known, odds) · [[canon-taleb-black-swan]] (sequence risk is
a tail-timing problem) · [[canon-thaler-sunstein-nudge]] (pre-committed rules beat in-the-moment choices) ·
[[canon-kahneman-thinking-fast-and-slow]] (why calendar or band rules protect against panic selling)
