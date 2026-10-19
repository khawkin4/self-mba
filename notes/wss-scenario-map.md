# The WSS scenario map — the seven concept notes reorganized by market regime

> **What this is.** The seven Wall Street Skinny notes are organized by *concept* (rates, credit, deals, private
> markets, AI, hedge funds, technicals). Each concept carries an "Applies when / Breaks when" and a "With vs. without"
> paragraph, but those conditions are scattered across ~10,000 lines. This note answers one question: **do we
> understand ideal vs. non-ideal scenarios?** It re-sorts every mechanism by the market regime it thrives or fails in,
> names who wins and loses in each regime, and asks what structures survive the bad ones.
>
> **Sources.** The hub [[wall-street-skinny-insights]]; the seven concept notes [[wss-rates-macro]] (**R**),
> [[wss-credit-distressed]] (**Cr**), [[wss-capital-markets-ma]] (**CM**), [[wss-private-markets-wealth]] (**PM**),
> [[wss-ai-economics]] (**AI**), [[wss-trading-hedge-funds]] (**HF**), [[wss-technicals-career]] (**TC**); and the
> venture applications [[apply-wss-to-venture]] (**AV**), [[primary-venture-partners-insights]] (**PVP**) and
> [[harlem-capital-vc-insights]] (**HC**). The bold letters are the keys used in every "Note §" column below
> (TC sections are numbered 4.x in that note).
>
> **Provenance:** the regime framework is this note's synthesis, not the channel's. The channel teaches mechanisms
> and their failure conditions; it never sorts them into a 2×2. Every mechanism, figure and example below is from the
> notes (and inherits their flags: 2026 events as reported on air, guests talking their book). The placement of each
> mechanism in a regime, the seat verdicts and the transition logic are this note's judgment.
>
> **Data.** A FRED-based regime history (which quarters sat in which cell, from spreads, curve, financial conditions
> and policy rates) is maintained separately and populated into the **Regime history (data)** section near the end.
> Signals that are on FRED are tagged with their series IDs in the dashboard so that section and this one line up.
>
> Maps to **Course 11** (Macro: regimes and transmission), **E2** (Capital Allocation: structure under uncertainty),
> **E6** (Crisis Leadership: forced sellers and who sets the price), **Course 10** (venture fund timing).

---

## The framework, and where the notes push back on it

**Two axes.** The vertical axis is the **price of money** (low vs. high). The horizontal axis is **cash return**: can
capital come *back* to the people who supplied it, through exits, distributions, refinancing and new issuance (open),
or is it trapped (stuck)?

```
                              CASH RETURN
                    open (exits, refis, issuance)      stuck (no exits, no refis)
                 ┌───────────────────────────────┬───────────────────────────────┐
   PRICE    low  │  A · BOOM                     │  D · SHOCK                    │
   OF            │  2019–21 (and 2010–15)        │  2008–09, Mar 2020            │
   MONEY         │  everything refinances        │  rates cut to zero, but no    │
                 │  and everything sells         │  one can sell anything        │
                 ├───────────────────────────────┼───────────────────────────────┤
            high │  B · LENDER'S MARKET          │  C · DROUGHT                  │
                 │  2024–26 (and 2006–07)        │  2022–23                      │
                 │  money is dear, but windows   │  money is dear and the        │
                 │  are open; coupons are king   │  windows are shut             │
                 └───────────────────────────────┴───────────────────────────────┘
```

**Four refinements the notes justify** (the agreed framework is kept; these sharpen it):

1. **The cash axis runs at two speeds.** Public channels (IG bond issuance, IPOs, strategic M&A, BSL refinancing)
   reopen first; private realizations (PE distributions, venture DPI) lag by years. In 2024–26 public cash was
   flowing hard (record IG issuance, Figma and SpaceX IPOs, "the year of the banker" in 2025, TC §4.19) while PE
   distributions as a share of NAV sat at a post-GFC low (PM §6). The channel's own period is therefore a **split
   B: B for public markets, C-like for private books.** Many seat verdicts below differ depending on which speed a
   seat lives on.
2. **The rate axis means restrictiveness, not level.** Medeiros's point (R §5): a 4.15% 10-year against ~8% nominal
   GDP growth is *loose*, and the policy rate sat ~150–200bp below the Taylor rule in 2026. "Rates are high" and
   "rates are restrictive" are different claims; the 2023–25 recession calls failed on exactly that confusion. Read
   the vertical axis as **financial conditions** (the price of money relative to growth), with the policy-rate level
   as shorthand. That is why the dashboard leans on spreads and NFCI, not on fed funds alone.
3. **D has a variant in which the risk-free asset breaks.** April 2025: tariffs, and stocks, Treasuries and the dollar
   fell *together*; the 10-year went from ~3.9% to ~4.5%, 30-year swap spreads neared −100bp, basis trades unwound,
   and the administration paused within a week (R §16, HF §15). Gilts in 2022 are the same template. Call it **D′**:
   cash stuck suddenly, but long rates *rise* because the "safe" asset is part of the problem. Who wins in D (long
   Treasuries) loses in D′.
4. **The transition the channel actually lived, C → B, is missing from the original four arrows.** It is added below.

**Four cross-regime laws.** The first three were agreed; the fourth is added because the notes keep arriving at it
independently (HF §14, Cr §7, the hub's system-level "with vs. without").

1. **Ideal for whom.** Every price in finance has two sides, so one seat's ideal regime is its counterparty's
   non-ideal one. B's 9–11% contractual coupon is the floating-rate borrower's PIK election (Cr §10). Figma's ~$3B
   day-one pop is the selling VCs' loss and the allocated buyers' gain (CM §5). A gate protects stayers and traps
   redeemers (Cr §12). A CV crystallizes the GP's carry and asks LPs to sell or roll (PM §5). A majority uptier takes
   the minority's loan from 85 to 30 (Cr §14). "Is this a good regime?" has no answer until you name the seat.
2. **Ideal conditions breed non-ideal structures.** Cheap money writes the documents that expensive money
   enforces. The credit note's master loop: *loose terms during tight spreads decide the recovery during wide
   spreads* (Cr "How the concepts connect"). Cov-lite, PIK toggles, 7x unitranche, 20x software LBOs, sub lines,
   SPACs, the 1.375% 2050 Treasury, 2–3% mortgages and SVB's securities book were all A-regime choices; their bills
   came due in C. B is now writing its own (the AI funding ladder, retail evergreen money, IG at 30-year tights).
3. **Structure beats conditions.** What survives a bad regime was built in a good one: EA's 65% equity check, PDT's
   seven-year lockup, a sole lender's maintenance covenant, ABG Print's permanent capital, Sixth Street's overlay fund.
   The holding period belongs to whoever funds you (HF "How the concepts connect"), and the holding period is set at
   the moment of funding, not at the moment of stress.
4. **Risk relocates; it does not leave.** Every constraint on banks moved the activity somewhere less regulated:
   prop trading to hedge funds, market making to Citadel and Jane Street, LBO lending to private credit, liquidity
   transformation into BDCs and evergreens (HF §14, hub). Regulation chooses *where* C and D bite, not whether. The
   2008 D hit bank balance sheets; the next one is more likely to surface in BDC gates, insurer related-party books
   (Cr §13), NAV loans and SPV debt (AI §7).

---

## How regimes move: transitions and their triggers

| From → to | Trigger (per the notes) | What moves first | What moves last | Channel evidence |
|---|---|---|---|---|
| **A → C** | Inflation forces the central bank off zero. QE during real inflation is "gasoline on the fire" (R §7); 9% CPI, then hikes plus QT | Longest-duration assets: XBI fell in Feb 2021 on rate expectations right after the vaccine (CM §18); Bitcoin topped as the Fed abandoned zero (HF §18); SPACs | Private marks: VC marks lagged public tech in 2022, then the denominator effect hit (PM §6) | R §7, §17; CM §11, §18; PM §6 |
| **C → B** | Rates stay high, but demand for income reopens windows: money pre-buys cuts, then reaches down the credit curve (Jen's "cash trap", R §1, Cr §2) | IG bonds at 30-year tights; record issuance days 3.5x covered (Cr §3) | PE distributions; GPs "grow into the entry multiple" and use CVs instead (PM §5) | R §1; Cr §2–3; CM §4–5; PM §5–6 |
| **B → C** | Windows shut while rates stay high. Five candidate triggers in the notes: a hike into loose conditions (Warsh, Sep 2026; Medeiros maps one more hike to 5–10% lower S&P, R §5); a long-end shock (Mar 2026 oil; auctions tailing, dealer takedown ~24% vs ~10% norm, R §8); a credit event at the weakest link (First Brands, BDC gating, Cr §9, §12); mega-IPOs trading poorly (Svrluga, PVP §8); a break in the AI funding ladder ("chips, China, credit", July 2026, AI §13) | Spreads on the weakest credits: Oracle 215bp, Nvidia 40→80bp, new 30-year hyperscaler paper +40–60bp in a month (AI §6) | Private loan marks, which "identify as par" until markdowns and dividend cuts (Cr §2) | R §5, §8; Cr §2, §12; AI §6, §13 |
| **C → D** | A *sudden, unexpected* shock hitting a tightly coupled position. Kroboth's rule: a foreseeable maturity wall gets refinanced, extended and nibbled away, so **C usually ends without D** (Cr §15). The D-makers in the notes are plumbing events (Sep 2019 repo spike, Mar 2020 basis unwind, R §7, §11) and runs (SVB 2023 was the near miss, TC §4.22) | Repo/GC, swap spreads, ETF discounts to NAV (HF §4) | Default statistics, smoothed by PIK and amend-and-extend (Cr §10) | R §7, §10–11; Cr §15; HF §4 |
| **D → A** | Policy floods the system: zero rates, QE across the curve, facilities. The hosts concede that without 2008–09 QE "the bottom would have fallen out" (R §7) | Buyers with committed capital set prices at the bottom (Cr §15); bond ETFs flipped from discount to premium when the Fed said it would buy IG (HF §4) | Risk appetite becomes mania: ZIRP fed SPACs and meme stocks (CM §11) | R §7; Cr §15; CM §11 |
| **B → D′** | Policy itself becomes the shock, so the safe asset sells off with risk assets (Apr 2025 tariffs, R §16) | Swap spreads (~−100bp on 30s), basis unwinds, the dollar | Equities recovered within weeks once the shock was reversed (R §16 counterpoint) | R §10, §16; HF §15 |

Two things the table says that the 2×2 alone does not. **First, regimes do not cycle in a fixed order:** A went to C in
2022 without a D, C went back to B in 2024 without a D, and D′ in April 2025 reverted to B inside a month. **Second, the
slowest-moving variable is always private realization.** Whatever regime public markets are in, private books are
one or two cells behind, which is the mechanical reason the distribution drought outlived the 2022–23 drought itself.

---

## Regime A · Boom (low rates, cash flowing)

**Defining conditions.** Policy rate near zero, QE holding down the whole curve (R §7), IG spreads tight because
"money has nowhere to go" (R §1), IPO and SPAC windows wide open, distributions recycling into record commitments
(2021 distributions were an all-time record, PM §6), subscription lines at a third to half of commitments on
revolver-like terms (PM §3). Episodes: 2019–21 most cleanly; 2010–15 in a milder form.

| Mechanism | Ideal for (who, why) | Non-ideal for (who, why) | Note § |
|---|---|---|---|
| Rates, curve, duration | Issuers terming out cheap long debt; homeowners locking 2–3% fixed; long-duration equity (VC, biotech, SaaS), because the discount rate is near zero | Savers and money funds earning nothing (TINA); buyers of 2020 long bonds (the 1.375% Aug-2050 later traded near 46 cents); banks loading deposits into duration (SVB's later failure) | R §2, §9, §12; CM §18 |
| Credit spreads, private credit | Borrowers and sponsors: spreads at the tights, cov-lite, unitranche to 5.5–7x that pre-empts auctions | Lenders: paid little for default risk; Gatto's marker of overheating is that "bad deals" (lender not paid for the risk) still get done | Cr §2, §5, §8 |
| PIK and LME documents | Sponsors writing escape hatches into documents (J.Crew-style asset moves, open-market-purchase exceptions, PIK toggles as a free option) | CLOs taking $5–10M of a $1bn loan who won't read a 300-page agreement; harmless now, enforced in C | Cr §10, §14 |
| BDC and evergreen wrappers | Managers: inflows exceed redemptions; evergreens grew ~$50bn → ~$500bn in about five years. Investors see smooth quarterly marks | Late entrants buying at a NAV that lags reality ("volatility laundering"); constant inflows force deployment into an overheated market | PM §8; Cr §12 |
| IPO window and pop | Issuers at rich multiples; pre-profit biotech (~75 IPOs of $50M+ a year in 2020–21); SPAC sponsors collecting a ~20–32% promote | SPAC public holders (2020–21 SPACs down 65–90%); selling holders who leave a pop on the table | CM §5, §11, §18 |
| M&A, cash vs. stock | Acquirers with high P/E stock (cheap currency) *and* cheap debt: both currencies are cheap at once | Sellers paid in bubble-priced stock (AOL/Time Warner, ~$100bn destroyed) | CM §13, §15; TC §4.22 |
| PE exits, secondaries, CVs | GPs: exits at high multiples; sub lines manufacture early IRR (a day-one markup gives "an infinite IRR"); leverage is cheap for everyone | Buyers of 2019–22 vintages at peak multiples, later told to "grow into the entry multiple"; LPs who judged on IRR rather than DPI | PM §3, §5 |
| Endowments, denominator | Endowments: a public rally leaves them *under*-allocated, driving record commitments; distributions fund the next fund | Every pool that over-commits on that basis; the NAV balloon becomes the drought's denominator later | PM §6 |
| Hedge fund leverage, basis, pods | Levered beta (PE, effectively levered long the market); basis traders on cheap repo with ample reserves | Hedge funds "paid not to be correlated," which lagged the zero-rate bull and cut fees; short sellers earning no rebate on proceeds | HF §1, §9, §15 |
| AI capex funding ladder | Only rung one exists: hyperscalers fund capex from cash flow, sit on net cash and buy back stock; asset-light compounders win | Credit investors starved of high-grade supply ("we'll never get another bond" scarcity keeps IG tight) | AI §6 |
| SaaS | Software founders and sponsors: sticky seat-based annuities, lent to at high leverage at 2019–21 prices | Lenders underwriting a perpetuity at a 2021 multiple; Shah's point is that later SaaS fears are about *those vintages and prices* | AI §17; PM §2 |
| VC fundraising and exits | Emerging managers ("anyone with a pulse" raises a fund); founders raising at markups; Harlem raised Fund II ($134M) in six months in 2021 | Late-round investors (round-by-round returns fell, last rounds negative, per the Instacart chart); 2021–22 vintages, which Harlem's Henri says "won't" outperform | PM §14b; HC §5, §7 |
| Bank capital, repo | Banks flush with QE reserves and deposits; ample reserves keep repo calm | Banks that put deposit inflows into long securities (SVB's bill arrives in 2023) | R §7; TC §4.22 |
| Comp, careers | Juniors: on-cycle recruiting pulled ever earlier; buy-side seats plentiful; "everyone wished they were a SPAC person" (Bok) | Careers built on a ladder that is about to drop (SPACs, crossover growth) | TC §4.21; CM §11 |
| Mortgages, CRE | Buyers locking 2–3% fixed; CRE bought at ~65% LTV "when money was practically free" | The next cohort: lock-in freezes turnover later; short 3–5-year CRE loans become the refinancing wall | R §12; PM §10–11 |

**What gets planted here** (the seeds of C and D). Cov-lite and incurrence-only documents; PIK toggles; unitranche at
7x with no junior cushion beneath it (Cr §8); 20x software LBOs; ~$900bn of subscription lines (2023) and the IRR
habits they formed (PM §3); NAV loans and recaps layered on levered companies (PM §7); duration on bank balance sheets;
2–3% mortgages (the lock-in that later freezes housing); 3–5-year floating CRE loans at 65% LTV; record LP
commitments that swell unrealized NAV (the drought's denominator); first-time VC funds raised on markups; SPAC
promotes. The hub's chain starts here: rates set the price of money, and the price set in A is the one every
structure was underwritten at.

**The winning structure in A.** Lock long, cheap, fixed-rate liabilities and keep the asset side flexible (Adelman's
fixed-rate 10-year debt as a "one-way option", PM §10; Bessent's criticism that Yellen did not term out the Treasury
at 1%, R §9). *Sell into the window* rather than holding for more: take exits and IPOs while the book is deep. And
refuse the loose deal: Kroboth caps Northwall at ~$3bn rather than ~$10bn because disciplined lenders sit out the
plain-market deals (Cr §16). The seat that loses least in the next regime is the one that declined to write A's
documents.

---

## Regime B · Lender's market (high rates, cash flowing)

**Defining conditions.** Policy rate between ~5.5% (before the Sep 2024 first cut) and ~3.5–4% (2026), with the long end above it (US 30-year yields above 5% for the
longest stretch since 2007, R §3); IG spreads at 30-year tights despite tariffs and war (R §1, Cr §2); record IG
issuance; IPOs back (Figma, SpaceX), M&A back, 2025 "the year of the banker"; secondaries ~$160bn in 2024 (PM §5).
But PE distributions/NAV at a post-GFC low (PM §6), so this is the **split B** of refinement 1. The historical analog
is 2006–07: fed funds ~5.25%, spreads near tights, TXU and Caesars (TC §4.7). The channel's 2024–26 is that regime
again, with the leverage moved from banks to funds (Cr §18).

| Mechanism | Ideal for (who, why) | Non-ideal for (who, why) | Note § |
|---|---|---|---|
| Rates, curve, duration | Savers, money funds and bill buyers (stablecoins add a structural bid, R §8); short sellers, whose rebate now exceeds most borrow fees (HF §9) | Long-duration holders: the Mar 2026 oil shock repriced 10s ~50bp and "carted everybody out" of steepeners (Caxton ~$1.3bn, R §3); the Treasury's interest bill; homeowners who would like to move | R §2–3, §8; HF §9 |
| Credit spreads, private credit | Direct lenders: ~9–11% contractual, a 150–250bp premium over syndicated, quarterly maintenance covenants in the core middle market; insurers buying long paper | Floating-rate borrowers (cash interest rises as EBITDA strains); upper-middle-market lenders who lose borrowers back to the reopened BSL market (~500bp vs 325–350bp) | Cr §7–8, §18 |
| PIK and LMEs | Sponsors buying time with PIK; funds on the winning side of an uptier (buy at 60, exchange into 85 of super-senior new money) | BDC holders (PIK is booked income but no cash, so dividends can be uncovered); minority and CLO lenders (85 → 30). PIK use ~7.7% → ~12%, "bad PIK" ~18% → ~50% | Cr §10, §14 |
| BDC and evergreen gating | Managers still raising through the wealth channel and the 2025 401(k) order; stayers, whom the gate protects; secondary buyers (Saba bid 65–80 cents for gated Blue Owl shares) | Redeemers: 5% caps, Blue Owl's conversion to a drawdown fund, BCRED's ~$3.8bn of requests met only with $155M of partners' money; retail sold "low risk, high reward" | Cr §12; PM §8 |
| IPO window and pop | Mega-issuers who can dictate (SpaceX: a take-it-or-leave-it $135, ~75bp fee, 4.9% float, index rules rewritten); underwriters (greenshoe, "perfect 20% pop") | Passive holders as exit liquidity for unlocking VCs; incumbents sold to fund new issues (Tesla in "the Elon trade"); Figma's selling holders (~$3bn) | CM §4–8 |
| M&A, cash vs. stock | High-P/E acquirers paying in stock (at 37x, stock costs ~2.7% vs ~4.1% after-tax debt); existential bidders backed by sovereign or billionaire equity (Paramount's ~$110bn stack); target shareholders under Revlon | Disciplined strategics paying cash (Netflix fell on its all-cash switch; Google/Wiz forgoes ~$1.2bn a year after tax); targets left holding the leverage; financial co-investors whose IRR breaks on each bump (Affinity walked) | CM §12–15 |
| PE exits, secondaries, CVs | GPs who crystallize carry in a CV and earn tiered carry on the same asset; secondary buyers (an "undercapitalized" buyer base, good buyout funds at mid-to-high 90s, 20–40% exit pops); the advisors | LPs who roll, or who must commit to the next fund to be allowed to sell (paying to leave); small LPs without negotiating weight | PM §5–6 |
| Endowments, denominator | Large endowments selling at strong prices (Yale's ~$6bn LP-led sale, framed as opportunistic) | Small and newly taxed endowments (the 2025 excise tax tiers); every LP waiting on DPI to recommit | PM §6 |
| Hedge fund leverage, basis, pods | Pods (dispersion high, rebate pays the shorts, $100m sign-on packages); basis traders (heavy Treasury supply, the trade back to "sizes not seen since 2019", ~$800bn by Slok's estimate); L/S and macro funds getting the meetings | Single, concentrated levered books: Situational Awareness at ~4:1, margin-called into a forced sale to Citadel while still up ~80% on the year; crowded curve trades | HF §1, §10, §12, §15; R §11 |
| AI capex funding ladder | Chip and power rent-holders (PJM capacity ~10x); private credit and insurers buying long-dated paper (PIMCO's ~10-point gain on Hyperion); banks underwriting record IG and equity (Google ~$85bn); infra funds with 20-year hyperscaler leases | Hyperscaler shareholders (Meta FCF $8.5bn → $784m; Google's first negative-FCF quarter); ratepayers; Nvidia's own credit (40 → 80bp); Oracle at 215bp; neoclouds borrowing against GPUs | AI §4–8 |
| SaaS | Lenders on short paybacks (at ~2–3x, debt can be money-good while equity reprices); AI-native challengers | SaaS equity (a perpetuity reprices on a year-8 threat); PIK-heavy 6–7x LBO lenders (Medallia's keys went to Apollo and Blackstone); BDCs concentrated in software (~$17.7bn of SaaS loans into distress in two weeks) | AI §17; Cr §10, §12 |
| VC fundraising and exits | Scaled brand managers (~58% of VC dollars to nine firms; Primary closed $625M in Feb 2026); AI-infrastructure seed bets riding the capex cycle | Emerging managers: a 3x net fund over 12 years earns ~9.6% a year, about private credit's yield, so LPs keep only managers they believe can do 5x+; first-time funds fell ~60%; app-layer seed exposed to the SaaS-pocalypse | AV §2, §6; PVP §1 |
| Bank capital, repo | Non-bank dealers (Citadel Securities' possible white-label S&T, HFT market makers); banks lending *to* private credit funds; underwriting desks | Banks rationing balance sheet under SLR/Basel endgame, so swap spreads stay negative and auction takedowns rise; reserve scarcity (the tell before QT ended: fed funds minus SOFR went from ~−6bp to ~−30bp, R §7) | R §7, §10; HF §14 |
| Comp, careers | Bankers (deal volume back); 2024–25 exits into private credit; S&T traders moving to hedge funds | PE juniors facing "top-heavy" seat freezes as fundraising tightens; private credit comp plateauing as PE refugees fill seats | TC §4.19–4.21 |
| Mortgages, CRE | Owners with 2–3% fixed debt; rescue capital (pref and mezz at high-single to low-double-digit yields, senior to old equity) | 2021-vintage CRE equity (a $100M deal at 65% LTV, revalued to $85M and refinanced at 55%, leaves an ~$18M gap); first-time buyers (the Fed held in Mar 2026 and 30-year mortgages still rose 75bp) | R §12; PM §10–11 |

**What gets planted here.** The AI funding ladder descends past cash flow into bonds, off-balance-sheet SPVs (Hyperion:
~92% debt, a four-year lease break), vendor guarantees (Nvidia backstopping ~$250bn of a ~$527bn build) and
GPU-collateralized neocloud debt (AI §7–8); five hyperscalers' 2026 capex near ~$800bn. Bad PIK at half of all PIK.
Retail and 401(k) money moving into vehicles that hold 5–7-year assets against quarterly redemption promises (PM §8).
IG spreads with no cushion left ("up by the stairs, down by the elevator shaft", R §1). The basis trade back at 2019
size; pods all running similar factor-neutral books, so stop-losses become the contagion mechanism (HF §10). Mega-IPOs
with ~95% of shares locked, which become supply on unlock (CM §8). CVs postponing price discovery on the best assets
(PM §5). JPMorgan's $20bn sole LBO underwrite concentrating what syndication used to spread (TC §4.10). Insurer books
with related-party concentration (Delaware Life's $1.4bn → $17bn revision, Cr §13). A Treasury that shortens its
average maturity, swapping term risk for rollover risk (R §9). Loan-only stacks that have already pushed first-lien
recoveries from ~80 to ~60 cents (Cr §1). Every item is a funding arrangement that works while the windows stay open.

**The winning structure in B.** Be the senior, floating-rate, covenanted lender, ideally the *only* one (Kroboth's sole
lender with non-negotiable covenants and add-back limits, Cr §16; Churchill's maintenance covenants and TIAA's
permanent capital, Cr §8). On the equity side, carry a fat equity check (EA's ~65% means equity absorbs the first ~$36bn
of loss, Cr §11). If you issue, sell what is rich: Google sold stock, a mandatory convertible and upside calls when
equity, vol and call skew were all expensive (CM §9). And hold liabilities locked in during A. The seat that does best
in B is the one *supplying* liquidity (secondary buyers, rescue capital, sole lenders), because B is the regime in which
everyone else is paying for it.

---

## Regime C · Drought (high rates, cash stuck)

**Defining conditions.** Fast hikes into inflation, QT, the 2022–24 curve inversion (the longest on record, R §17); the
IPO window shut, SPAC trusts drained by redemptions, biotech forced into reverse mergers and licensing (CM §11, §18);
banks hung on the Twitter buyout debt (Cr §7); BREIT gating from Dec 2022 (PM §8); the 2022 denominator effect in
venture (PM §6); SVB in Mar 2023, a duration mismatch (R §2); negative leverage in CRE (3–3.5 caps against a 4.2–4.3%
10-year froze transactions, PM §10). Episode: 2022–23.

| Mechanism | Ideal for (who, why) | Non-ideal for (who, why) | Note § |
|---|---|---|---|
| Rates, curve, duration | Front-end savers; short sellers (rebate); dollar holders (the dollar rose through the hiking cycle) | Duration holders (SVB; the 2050 bond at ~46 cents); long-duration equity (XBI, VC marks); 60/40 portfolios when stocks and bonds fall together | R §2, §9, §14; CM §18 |
| Credit spreads, private credit | Large direct lenders that step in as banks step back: in 2023 banks were hung on Twitter debt and regional banks pulled back after SVB, and Gatto's large private lenders kept doing good deals | Floating-rate LBO borrowers (coverage collapses; tariffs or input costs push 4x leverage toward an 8x covenant breach without new borrowing, R §1); banks holding hung bridges | Cr §5, §7, §18; R §1 |
| PIK and LMEs | Funds with lawyers and new-money capacity (the best lawyers, the most capital and the earliest seat capture the transfer); sponsors using PIK to keep the equity option alive | Anonymous CLO holders uptiered behind new super-senior debt; lenders without anti-LME blockers; eventually the sponsor (lenders refuse more PIK and take the keys) | Cr §10, §14 |
| BDC and evergreen gating | Holders who stay (the gate shares illiquidity instead of handing the worst loans to the last out); buyers of public BDCs at deep discounts to NAV | Redeemers (Kristen's year-long BREIT exit by wet-signature letter); interval funds that by law must keep repurchasing and so sell into the rush | Cr §12; PM §8 |
| IPO window and pop | The few buyers of the few deals; private lenders financing companies that cannot list | Issuers and founders (window shut, down rounds, flat rounds); SPAC holders; VCs and PE needing exits | CM §4, §11, §18 |
| M&A, cash vs. stock | Cash-rich strategics and patient firms ("downturns are when patient firms move up", Bok); boutiques with restructuring desks (the countercyclical hedge Greenhill added in 2001) | Levered buyers (cash deals more dilutive as rates rise; debt capacity shrinks); advice-only firms with no restructuring revenue | CM §2, §13 |
| PE exits, secondaries, CVs | Secondary buyers (step changes in the market followed the dot-com bust and the GFC, when LPs suddenly needed cash); GPs able to move winners into CVs | GPs who need realized exits to show DPI before the next raise; holders of 2021 vintages with stale marks; LPs who cannot recommit | PM §5–6 |
| Endowments, denominator | Pools that entered under-allocated, or with cash to buy LP stakes at discounts | Endowments overweight privates (in 2022 VC LPs "freaked out" and trimmed managers as public tech fell and venture marks lagged); small endowments that cannot earn without risking principal | PM §6 |
| Hedge fund leverage, basis, pods | Pods and macro funds (strong 2022 returns brought huge 2023–24 inflows); short books earning the rebate; anyone selling volatility to the panicked at good prices | Levered long beta; crypto (its first top coincided with the Fed abandoning zero); funds whose investors redeem into the drawdown (a run on the bank) | HF §1, §10, §18 |
| AI capex funding ladder (if B breaks into C) | Cash-funded hyperscalers that can keep building and buy distressed capacity; owners of powered shells; buyers of Oracle CDS if the downturn is credit-led | The lower rungs lose funding first: neoclouds with chip-backed debt, SPV lenders facing a lease break ("a data center in the middle of a field without a customer"), Nvidia's guarantee and the revenue it bought; equity-funded capex is self-limiting, credit-funded capex propagates | AI §6–8, §11 |
| SaaS | Lenders at 2–3x whose loans repay before the threat arrives; acquirers of cheap software | Zero-rate software vintages bought at 2019–21 prices; PIK-heavy 6–7x LBOs, where the payback window is long enough for the threat to land | PM §2; AI §17 |
| VC fundraising and exits | Scaled firms with deep LP relationships (Primary closed $275M + $150M Select in Sept 2022, as C began); new vintages buying at reset prices ("post-crash vintages historically outperform", HC §7) | Emerging managers (LPs cut first-time relationships first; Harlem did zero deals in one Q4 after SVB); seed companies needing an A ("downstream-capital risk is the killer"); 2021 vintages | HC §7; AV §1; PVP §8 |
| Bank capital, repo | Banks with short assets and sticky deposits; money funds paid 5% on cash | Banks with duration (SVB); regional banks, which ceded lower-middle-market lending; banks carrying hung LBO debt they cannot sell near par | R §2; Cr §7–8; TC §4.22 |
| Comp, careers | Restructuring bankers; distressed and credit hiring | Juniors (bottom-bucket "donut" bonuses of zero or $15–25k); the "+2" buy-side step vanishes as fundraising stalls and senior seats freeze | TC §4.19, §4.21 |
| Mortgages, CRE | Locked-in homeowners (moving from 2% to 7% roughly triples the payment, so nobody sells); gap-capital funds; debt funds and insurers replacing banks | CRE equity in 2021 office deals (wiped out even if office "always bounces back"); movers, brokers and builders whose revenue depends on turnover | R §12; PM §10–11 |

**What gets planted here.** Extend-and-pretend: PIK, amend-and-extend, CVs and gap capital spread losses over time
instead of crystallizing them (PM §11, Cr §10). That keeps C from becoming D, but it also keeps marks above clearing
prices and stretches the drought. Private credit grows into the space banks vacate, which becomes B's lender's market
(Cr §7). Managers, unable to get institutions to recommit, build the retail evergreen channel, planting B's liquidity
mismatch (PM §6, §8). Record LP-led secondaries build the buyer base that later prices CVs. Emerging managers who fail
to raise in C are missing from the next bottom. And pent-up issuance waits for the window, which is why B opens with
record bond days and a mega-IPO queue.

**The winning structure in C.** Committed, locked-up capital with cash still to deploy: secondary funds, dislocation
funds that draw only after preset market triggers (Cr §15), scaled VC firms with a separate opportunity fund. Sole or
small-club lending with maintenance covenants, which forces the negotiation early, "while value still exists" (Cr §5).
Short-duration, floating-rate assets; fixed-rate liabilities locked in A. Permanent capital (PM §14). And for advisers,
a countercyclical line: restructuring peaks when M&A dies (CM §2).

---

## Regime D · Shock (low or falling rates, cash stuck)

**Defining conditions.** A sudden shock nobody refinanced in advance; correlations jump toward one (HF §5); funding
plumbing seizes (repo, the basis trade, bond ETFs at deep discounts, HF §4, §15); distributions *stop* (in the GFC the
numerator went to zero, PM §6); the central bank cuts to zero and buys assets. Episodes: 2008–09; March 2020. Variant
D′ (April 2025, 2022 gilts): same frozen cash, but long rates rise.

| Mechanism | Ideal for (who, why) | Non-ideal for (who, why) | Note § |
|---|---|---|---|
| Rates, curve, duration | Long Treasury holders and receivers as the long end rallies (except in D′); positive convexity pays | Anyone short duration in the rally: dealers who hedged an undelivered $2.6bn long-bond sale lost ~$210–250M when COVID moved yields ~50bp the wrong way; in D′ even Treasuries fail as a hedge | R §2, §16; TC §4.13 |
| Credit spreads, private credit | Committed capital buying at 70: the chance to deploy a lot is brief because dislocation funds reprice risk fast | Levered credit funds; holders forced to sell fallen angels (many IG mandates cannot hold high yield after a BBB−/BB+ downgrade); lenders without workout teams, which Gatto expects to "fail to raise again and disappear" | Cr §3, §15 |
| PIK and LMEs, bankruptcy | Senior lenders with control; distress-for-control buyers (Men's Wearhouse senior debt at 30–50 cents in COVID, converted to equity, "it worked") | Equity; junior and minority creditors; the losing side of a valuation fight (right on value at $800M, zero at a $400M ruling) | Cr §15 |
| BDC and evergreen gating | Stayers protected by the gate; secondary buyers of gated stakes | Redeemers, trapped at a NAV "nobody will pay"; interval funds forced to sell; the 401(k) channel, which relies on a liquidity expectation the gate breaks | Cr §12; PM §8 |
| IPO window and pop | Almost nobody; biotechs with creative fixes (reverse merger into a cash-rich shell, sell the lead asset) | Issuers; VCs needing exits; underwriters with a broken deal on the books | CM §18 |
| M&A, cash vs. stock | Cash-rich buyers and PE with dry powder (Blackstone held Hilton through the crisis for ~$10bn; Sixth Street wrote a $1bn package for Airbnb in under seven days in COVID); advice-only boutiques (Greenhill's stock hit an all-time high the week Lehman failed) | Forced sellers; acquirers whose stock currency collapsed; deals with soft financing commitments ("up to") | Cr §15; PM §2b; CM §2, §14 |
| PE exits, secondaries, CVs | Secondary buyers with capital (the market's step changes follow crises); locked-up PE, which "doesn't go bankrupt" for lack of margin calls (AI §13) | GPs with thinly capitalized, levered portfolio companies (TXU's ~18% equity check, Caesars); funds with NAV loans against already-levered companies; LPs selling at deep discounts | PM §5, §7; TC §4.7 |
| Endowments, denominator | Liquid pools able to rebalance in a day; secondary buyers | Endowments: public −25% pushes a 20% private target to ~24%, capital calls continue, and spending needs may spike just as private assets become unsellable | PM §6 |
| Hedge fund leverage, basis, pods | Patient balance sheets that buy forced sellers' books at a discount (Citadel taking Situational Awareness's public book at a discount); tail-hedgers | Basis traders (March 2020 was the last full blowup); crowded quant books (Aug 2007: PDT "lost our entire year in a week"); convert-arb funds when the 2008 short ban removed their hedge; pod PMs stopped out together | HF §2, §11–12, §15 |
| AI capex funding ladder | Cash-funded builders who can keep spending through the shock | Neoclouds with GPU-collateralized debt; SPV lenders whose offtaker walks at a lease break; leveraged holders of concentrated AI exposure (≈1.2m Korean accounts margin-called as the KOSPI fell 38% from highs) | AI §7–8, §13 |
| SaaS | Lenders with short paybacks, still money-good | Levered, PIK-funded software borrowers; BDCs with heavy software concentration, whose redemptions and markdowns arrive together | AI §17; Cr §12 |
| VC fundraising and exits | Firms with fresh capital and reserves, buying at the lowest entry prices of the cycle | Emerging managers trying to raise (fund timing); founders who need downstream capital; vintages deployed at peak prices | HC §7; AV §9 |
| Bank capital, repo | Survivors who get capital injections on terms (MUFG's $9bn convertible preferred into Morgan Stanley); dealers once the Fed backstops markets | Dealers with full balance sheets and bilateral exposures (pre-clearing, Lehman's failure left counterparties unhedged); bank employees holding deferred stock (Lehman colleagues' locked-up net worth went to zero) | TC §4.22 |
| Comp, careers | Distressed investors and restructuring advisers ("blood in the streets", with the survivorship caveat) | Juniors (Barclays kept Lehman's banking business but cut FICC, and everyone reinterviewed for their own job); anyone with wealth in employer stock | TC §4.22; Cr §15 |
| Mortgages, CRE | 2020: borrowers who refinanced into 2–3% fixed as the long end fell | 2008: subprime borrowers on teaser ARMs resetting to LIBOR + 600, refinanced in a loop for fees; CRE owners on short floating loans | R §12; Cr §18 |

**What gets planted here.** QE, zero rates and an embedded central-bank put (R §7) that become A's cash trap; ZIRP-era
SPAC and meme manias (CM §11). Post-crisis rules that push risk out of banks: 2013 leveraged-lending guidance (6x),
Volcker, Basel III, central clearing, which create private credit, non-bank dealing and the future D's location
(law 4; Cr §5, HF §14). Regulators' plumbing fixes (the Standing Repo Facility in 2021, the Treasury clearing mandate,
R §7, §10). Distressed specialists who survive become broad credit platforms (Cr §15). And the vintages that buy the
bottom, which become the best-performing funds of the cycle.

**The winning structure in D.** Committed, locked-up capital with dry powder; low or no leverage; liquidity-matched
vehicles (closed-end over open-end, because whoever can be redeemed becomes a forced seller); senior, secured,
covenanted claims with control; permanent capital that can draw its revolver and wait (ABG Print, PM §14); hedges that
match the risk actually held (index puts do not hedge single names under dispersion, AI §11). The credit note's third
loop, built on Kroboth: **when sellers are forced, whoever has committed, locked-up capital sets the price** (Cr "How
the concepts connect").

---

## Seat-by-seat matrix

Verdicts: **thrives** (the regime pays this seat), **fine** (works, nothing special), **squeezed** (returns or access
compressed, survivable), **forced out** (made to sell, exit, close or stop). Each reason is a compressed pointer to the
regime tables above.

| Seat | A · Boom | B · Lender's market | C · Drought | D · Shock |
|---|---|---|---|---|
| LP / endowment | **thrives**: distributions recycle into commitments | **squeezed**: DPI lags; sells secondaries at par | **squeezed**: denominator binds; trims managers | **forced out**: calls continue; sells at discounts |
| PE GP | **thrives**: cheap debt, multiples, open exits | **squeezed**: leverage no edge; CVs replace exits | **squeezed**: exits shut; marks stale; DPI pressure | **squeezed**: levered portcos; dry powder helps |
| VC GP (scaled) | **thrives**: markups and IPO window | **fine**: brand raises; needs IPO window | **squeezed**: exits shut, but still raising | **fine**: reserves and Select buy bottom |
| VC GP (emerging) | **thrives**: "anyone with a pulse" raises | **squeezed**: 3x net ≈ private credit | **squeezed**: LPs cut first-time managers first | **forced out**: cannot raise at the bottom |
| Direct lender | **fine**: spreads thin, terms loosening | **thrives**: 9–11% coupons, covenants, banks retreat | **fine**: high coupons, PIK and amendments rising | **squeezed**: defaults; workout teams decide survival |
| Syndicated-loan / CLO holder | **fine**: cov-lite documents, harmless for now | **squeezed**: LME risk; recoveries ~60 cents | **squeezed**: uptiered behind new super-senior debt | **squeezed**: primed; downgrades force selling |
| Distressed / cap solutions | **squeezed**: no distress; capital waits idle | **fine**: "cap solutions is the new distressed" | **thrives**: LMEs, rescue loans, gap capital | **thrives**: forced sellers; committed capital sets price |
| Multi-manager PM | **fine**: low dispersion; hedging out beta lags | **thrives**: dispersion, short rebate, talent war | **thrives**: volatility and dispersion pay pods | **squeezed**: correlated stops fire PMs together |
| Basis trader | **fine**: cheap repo, ample reserves | **thrives**: heavy supply keeps futures rich | **fine**: QT supply grows; repo risk rises | **forced out**: repo spikes, margin, forced sales |
| IPO issuer / founder | **thrives**: rich multiples; SPACs as backdoor | **fine**: selective window; ~15–20% designed pops | **squeezed**: window shut; down rounds | **forced out**: no window; recap, license, sell |
| Strategic acquirer | **thrives**: stock and debt both cheap | **fine**: stock cheap; cash deals dilutive | **fine**: targets cheap; own currency weaker | **thrives** (if cash-rich): buys forced sellers |
| Bank dealer | **fine**: QE reserves, thin spreads, calm repo | **thrives**: "year of the banker"; record issuance | **squeezed**: hung bridges; advisory fees fall | **squeezed**: balance sheet full; warehouses hung |
| Individual in evergreen funds | **fine**: inflows exceed redemptions; smooth marks | **squeezed**: annual carry on marks; caps bind | **squeezed**: gated; a year to exit | **squeezed**: trapped; NAV is not a price |
| Junior banker | **thrives**: deal volume; on-cycle recruiting earlier | **fine**: deals back; buy-side seats tight | **squeezed**: donut bonuses; "+2" step vanishes | **forced out**: layoffs; reinterview for own job |

How to read it: **no seat thrives in all four columns.** The only seat that never drops below "fine" is the
*cash-rich* strategic acquirer, and "cash-rich" is itself a structure chosen in advance (law 3). Distressed/cap
solutions and the pod shop are the next closest to all-weather, and both earn it by being *liquidity providers* in C
and D. The direct lender's best column is B and its worst is D; the emerging VC's
best is A and its worst is D; the LP's verdicts move with the slowest variable (private realizations). The matrix is
law 1 in grid form: the B column's "thrives" (direct lender, basis trader, bank dealer) are paid by the B column's
"squeezed" (borrowers, LPs, evergreen holders).

---

## Structure beats conditions: what protects each seat in bad regimes

Each entry is a choice made *before* the stress, so it can be checked in documents, not predicted from markets.

| Structural choice | What it protects against | Seats it protects | Where it is taught | Channel example |
|---|---|---|---|---|
| **Liquidity matching** (assets no less liquid than the redemption promise) | Runs: redemptions force fire sales that kill a fund whose thesis is right | Evergreen managers and holders, hedge funds, BDCs | Cr §12; PM §8; HF §1; TC §4.22 (Industry S4E1) | BREIT gated Dec 2022 to early 2024; an interval fund must keep paying out in a rush; Findley left Third Point because 90-day liquidity could not hold illiquid loans (Cr §9) |
| **Maintenance covenants** (tested quarterly, not only on action) | Discovering trouble at a missed refinancing, after the collateral is gone | Direct lenders, CLO holders, any senior creditor | Cr §5, §8; R §1; TC §4.12 | Caesars had effectively one covenant that mattered; Churchill insists on quarterly maintenance tests in the core middle market |
| **Equity check size** | A modest fall in enterprise value wiping out equity and moving straight into creditor fights | LBO lenders, sponsors, rollover holders | TC §4.7–4.8; Cr §11 | EA ~65% equity (a 10% EV rise is only a 15% equity gain, but equity eats the first ~$36bn) vs TXU ~18% (bankrupt) |
| **Lockups and permanent capital** | A funder deciding your holding period: margin, redemption, recall, fund-life deadlines | Hedge funds, PE, small-business owners, distressed buyers | HF §1, §12; Cr §15; CM §19; PM §14 | PDT's seven-year lockup; Citadel survived 2008 on term financing and two-year capital locks; ABG Print's revenue fell 95% in March 2020 and permanent capital kept it alive (2024 revenue beat 2019) |
| **Reserves and dry powder** | Missing the bottom because new capital cannot be raised then | VC, PE, distressed, secondaries | Cr §15; PM §2b; PVP §3; AV §9 | Dislocation funds that draw after preset triggers; Sixth Street's overlay fund wrote Airbnb's $1bn in under seven days; Primary Select as reserves carved into their own vehicle |
| **Sole-lender or small-club positions** | Being uptiered or rolled up by a co-opted majority of anonymous holders | Private lenders | Cr §14, §16 | Kroboth avoids LMEs by being sole lender; two to eight repeat lenders "rarely turn on each other"; CLOs with $5–10M slices get primed |
| **Anti-LME blockers and disqualified-lender lists** | Documents that let a simple majority subordinate you | Syndicated lenders; borrowers | Cr §14 | First Brands blacklisted Apollo; lenders now negotiate blockers after Serta and J.Crew |
| **Fund timing** (close before the downturn, deploy through it) | Raising into a drought and slowing exactly when entry prices are best | Emerging VC and PE managers | AV §9; HC §7, §10 | Primary closed Fund IV + Select in Sept 2022 as C began; Harlem did zero deals in one Q4 after SVB |
| **Fixed-rate, long-dated liabilities locked in A** | Refinancing at the regime's price instead of the old one | Homeowners, real estate owners, issuers, the Treasury | PM §10; R §9, §12 | Adelman's ~4% 10-year debt vs 6.5–7% now ("one-way option"); US borrowers locked at 2–3% |
| **Distribute rather than hold** | One balance sheet carrying a concentrated position into a freeze | Banks, underwriters | TC §4.10; Cr §7 | TXU's loans syndicated across a dozen banks vs JPMorgan's $20bn sole EA commitment (backed by ~$50bn of direct-lending capacity) |
| **Hedges that match the held risk** | A hedge that does not pay in the scenario that hurts you | Concentrated equity books, credit-led hedges | AI §11; HF §7 | Situational Awareness's index puts barely moved while its single names fell ~50%; Oracle CDS pays only if the AI downturn is credit-led |
| **DPI discipline over marks** | Raising the next fund on paper returns that "can evaporate 70%" | VC and PE GPs, LPs | PM §3; HC §1, §13 | Lerer's three-fund hump; a sub-line-flattered J-curve; Shah: DPI moved from afterthought to central after ZIRP |
| **A countercyclical business line** | Revenue that disappears with the deal cycle | Advisory boutiques, banks | CM §2; TC §4.18 | Greenhill added restructuring in 2001; a multi-product bank's trading desk offsets M&A droughts (why Bok sold to Mizuho) |
| **A diversified, pre-briefed investor base** | One LP's redemption forcing a liquidation | Hedge funds, emerging managers | HF §19 | Bauman: diversify by size, type and region, and call investors *before* bad news |

---

## Signal dashboard: telling which regime you are in

The channel teaches most of these as mechanisms rather than as a dashboard; where a series choice is this note's
operationalization of a concept the channel teaches, the "Taught in" column says so. FRED series IDs are given for
those on FRED; otherwise the real source is named. **Read the two axes separately:** spreads, curve, NFCI and real
yields locate the price-of-money axis; IPO pops, DPI, BDC requests and auction takedowns locate the cash axis.

| Indicator | What it measures | A/B reading (windows open) | C/D reading (windows shut) | Taught in | Source |
|---|---|---|---|---|---|
| IG credit spread | Price of default risk for high-grade borrowers | Tight: Aug 2025 IG at 30-year tights, "cash trap" | Gaps wider "down the elevator shaft"; weakest names first (Oracle 215bp; new 30s +40–60bp) | R §1; Cr §2; AI §6 | FRED: BAA10Y |
| High-yield spread (OAS) | Price of default risk for leveraged borrowers; whether refinancing windows are open | Compressed; "bad deals get done" | Wide; refinancing shut; the companies that most need to roll are shut out first | R §1; Cr §2, §5 | FRED: BAMLH0A0HYM2 |
| IPO day-one pops and pricing vs range | Equity window and allocation demand | ~15–20% designed pops (SpaceX +19.2%); in froth, blowouts (Figma +250%, CXMT +466%) | Deals pulled, priced below range, or broken through issue (Facebook); biotech reverse mergers | CM §4–5, §18 | Not on FRED: Jay Ritter's IPO statistics (Univ. of Florida), Renaissance Capital |
| Distributions / NAV and fund DPI | Whether private capital is coming back | Distributions recycling; 2021 an all-time record | Distributions/NAV at post-GFC low (2024–26); in the GFC the numerator went to zero | PM §3, §6; HC §13 | Not on FRED: GP reports, Cambridge Associates and MSCI-Burgiss benchmarks, PitchBook |
| BDC / evergreen redemption requests vs the ~5% quarterly cap | Retail liquidity demand against illiquid assets | Requests under the cap; inflows exceed outflows | Requests above the cap (BCRED ~$3.8bn; Oaktree paid ~8.5%); gates, drawdown conversions; read over-requesting as inflation of the headline | Cr §12; PM §8 | Not on FRED: fund 8-Ks and tender-offer filings (Schedule TO) on SEC EDGAR, manager letters |
| PIK share of private-credit income, and the "bad PIK" share | Borrowers converting cash interest into principal | Low and mostly structured at signing (~7.7%) | Rising and borrower-elected (~12%, with bad PIK ~50%); notably the 2026 reading is already C-like inside a B | Cr §10; AI §17 | Not on FRED: Lincoln International private-market data (via Bloomberg; the note flags this attribution for checking), BDC 10-Q schedules of investments |
| Treasury auction tails and dealer takedown | End demand for duration; dealer balance-sheet strain | Stop-throughs; dealer takedown near ~10% | Tails; dealer takedown ~24% (Mar 2026 2-year); dealers "puke" paper. Read *indirect* bids, not directs, for foreign official demand | R §8; TC §4.14 | Not on FRED: TreasuryDirect auction results |
| Fed funds minus SOFR | Reserve scarcity and repo stress | Small negative (~−6bp): reserves ample | Deeply negative (~−30bp at Oct 2025 month-end) or SOFR spiking above the range (Sep 2019) | R §7, §10 | FRED: EFFR, SOFR (FEDFUNDS for the monthly series) |
| Equity put/call ratio | Positioning and complacency | ~0.6–0.7 normal; ~0.44 is crowded bullishness, a late-A/B warning | Elevated; hedging demand | CM §8; HF §7 | Not on FRED: CBOE equity put/call ratio |
| Curve shape (10s–2s, 10s–3m) | Policy stance vs growth expectations | Steep in A (bull steepening after cuts); flattening or inverted late in B | Deep inversion in C (2022–24, longest on record); re-steepening after a long inversion is Adami's danger signal for D | R §3, §17 | FRED: T10Y2Y, T10Y3M |
| Financial conditions index | The channel through which the policy rate reaches the economy | Loose (Warsh said three times conditions were too loose; ~200bp below Taylor) | Tightening fast | R §5 (taught as a concept; the NFCI series is this note's choice) | FRED: NFCI |
| Senior loan officer standards (C&I) | Whether banks are tightening credit supply | Easing or neutral | Net tightening; regional banks pulling back (post-SVB) | R §17; PM §11; Cr §8 (taught as "tighter credit standards"; the SLOOS series is this note's choice) | FRED: DRTSCILM |
| VIX (and single-name vs index vol) | Equity volatility; dispersion | Low teens to ~16; single-name IV far above index IV means dispersion, so index hedges fail | Spikes; correlations toward one | CM §8; HF §7; AI §12 | FRED: VIXCLS (single-name IV: not on FRED, CBOE/OptionMetrics) |
| 10-year real yield | Real price of money; Hornbach's R − G for risk assets | Low or falling real rates with rising growth expectations support equities | Real rates rising faster than growth expectations | R §5, §13 | FRED: DFII10 |
| 10-year breakeven inflation | Market inflation expectations; whether "transitory" has reset | Anchored | Unanchored (the A → C trigger) | R §13 (the channel's breakeven video is missing; decomposition supplied in R) | FRED: T10YIE |
| 30-year mortgage rate | Long-end transmission to households; lock-in | Falling with the long end (2020 refinancing wave) | Rising even with the Fed on hold (Mar 2026: +75bp) | R §12 | FRED: MORTGAGE30US |
| Fed balance sheet | QE vs QT vs reserve management | Expanding (QE) or reserve-management bill purchases | QT, then the point where reserves turn scarce; emergency expansion in D | R §7 | FRED: WALCL |
| Swap spreads (30-year) | Dealer balance sheet and appetite for cash Treasuries | Mildly negative (structural since 2008) | Collapse toward −100bp (Apr 2025): "nobody wants" cash Treasuries | R §10; HF §15 | Not on FRED: Bloomberg/Tradeweb swap curves |
| Weakest-AI-builder CDS (Oracle) | The market's chosen hedge against the AI ladder breaking | Modest (CDX IG ~40bp) | Oracle protection ~130bp/yr and widening ~95bp vs index; a crowded hedge | AI §11; Cr §17 | Not on FRED: CDS dealers, Bloomberg `CDS` |

**One combined reading the channel's own period supports.** In 2025–26, spreads were tight, auctions mostly cleared,
the IPO window was open and NFCI-style conditions were loose (the B column), while DPI was at a post-GFC low, PIK and
bad PIK were at record shares and BDC requests ran over caps (the C column). That is refinement 1 on a dashboard:
**public signals read B, private signals read C.** A regime call from either half alone would be wrong.

---

## Primary vs Harlem through all four regimes

Figures from [[apply-wss-to-venture]], [[primary-venture-partners-insights]] and [[harlem-capital-vc-insights]].
Arithmetic as in AV (10% exit ownership, fees ignored). The two firms share a 2015 NYC starting line and take opposite
bets on the management fee, which is why they sort so differently across regimes.

**In A (boom), both raise fast and the gap is size.** Harlem raised Fund II ($134M) in six months in 2021 on a
post-George-Floyd tailwind; Primary closed Fund III ($150M) in February 2021. At near-zero rates, private credit
yields 5–6%, so a 3x venture fund is a wide premium and LP money flows to emerging managers first, as the higher-beta
bet (AV §2, "with vs. without"). Both firms' A-vintage funds deployed at peak seed prices: in mid-2022 Svrluga said seed
"hasn't gotten the memo" (PVP §8), and Henri says the 2021–22 vintages "won't" outperform (HC §7). A is where both
firms plant their weakest vintages.

**In B (lender's market), the regime splits the firms on both speeds.** On *fundraising*, the opportunity-cost math
bites: 3x net over 12 years is ~9.6% a year against 9–11% contractual credit, so LPs underwrite only 5x+ candidates and
judge that from brand and history (AV §2). Primary pitches each partner book as "eight 5x funds" and closed $625M in
February 2026, during the drought; Harlem's Fund III (target $150M, SEC filing 2024) had no close found, raising
into an anti-DEI backlash. On *exits*, B's open public window is Primary's: at 10% exit ownership Fund V needs ~$6.3B of
aggregate exit value to return 1x and ~$19B for 3x gross, which requires IPOs or mega-acquisitions, and Svrluga says
the OpenAI, Anthropic and SpaceX IPOs will cool or heat the market (AV §3). B also lets Primary work through Fund I's
tail (~11.7 years old, past a 10-year term): the ~$800M sale at 20-something times invested capital and the pending
Alma sale arrive in early 2026 (PVP §8). Harlem's path (~$1.5B of exit value returns Fund III, through $300M–$1B
strategic acquisitions) faces B's affordability problem: at high rates, cash deals are dilutive and buyers lean on
stock, so strategic bids depend on acquirers' P/Es (CM §13, AV §3). AI cuts the same way: Primary's most valuable mark is
a chip company that thrives while hyperscaler capex climbs, while Harlem's likely app-layer exposure sits in the
SaaS-pocalypse (AV §6; Harlem's sector mix is n/d).

**In C (drought), the risks swap seats.** Primary's fund-level math stalls when the IPO window shuts: multi-billion
outcomes cannot clear, Fund I's tail needs extensions or secondaries (venture secondary discounts are not covered by the
channel, n/d), and Select's role in insider rounds becomes an LP-vs-LP marking question (AV §4). But Primary keeps
raising: it closed $275M + $150M Select in September 2022, months into C, because $100B+ LPs underwriting 15–20-year
relationships pay for brand (PVP §8). Harlem is the manager the drought hits by design: LPs cut first-time and small
relationships first, its LP base leans on individuals and family offices with less pacing discipline, and it did zero
deals in one Q4 after SVB (HC §7). Its consolation is the exit side: the $300M–$1B M&A market "stays open in most
cycles," and its 12 exits on 80+ investments, if mostly small M&A, produce DPI, which is the right currency for C (AV §1).
**C hits Harlem through fundraising and Primary through exits.**

**In D (shock), fund timing decides everything, and here it is concrete.** Entry prices are lowest in D, and
post-crash vintages historically outperform (HC §7). The investors who profit are the ones still writing checks, which
is a fundraising question, not a picking question (AV §9). Sun's own deployment math assumes a fund puts its capital to
work over about three years (PVP §1). So:
- *Primary Fund V* closed in **February 2026** with $625M. A D arriving anywhere in 2026–28 lands **inside its
  investment period**: the firm buys the bottom with capital raised at the top, plus a separate Select pool for
  follow-ons. The same thing happened, in milder form, with Fund IV + Select closed in September 2022 and deployed
  through the 2022–25 reset.
- *Harlem Fund II* (2021) would be largely deployed by 2026, at A prices. *Fund III*, unclosed as of the sources, is
  the fund that would need to be raised **during** D, when the denominator effect freezes LP commitments and emerging
  managers are cut first. Harlem would be slowing down exactly when entry prices are best.
- The exit side reverses the B picture: in D neither IPOs nor strategic M&A clear, Primary's compute and semis marks are
  the most cyclical in the portfolio if the AI funding ladder breaks (AV §6), and Primary's Fund I tail would face
  secondaries at the widest discounts of the cycle.

**One line.** Primary's structure (scale, brand, multi-fund LP relationships, a separate reserves vehicle) is built
for C and D on the capital side and depends on A and B on the exit side; Harlem's structure (lean, M&A-sized exits)
is resilient on the exit side in every regime and exposed on the capital side in every regime but A. Law 3 applies:
neither firm chose its regime, and both chose their structure.

---

## Regime history (data)

_Generated by `_ingest/regimes.py` from FRED (keyless CSV; cached in `_ingest/raw/2026-10-04/data/fred/`). Re-run with
`python3 _ingest/regimes.py --refresh --md --since 1990`._

**Rules (transparent, judgment-set).** *Rates* are HIGH when the quarter-end effective fed funds rate is at least 2.5%.
*Cash* is STUCK when either channel is stressed:
- **Market channel:** the mean z-score (vs. 1990 onward) of the Baa–Treasury spread, Chicago Fed NFCI, net % of banks
  tightening C&I standards (SLOOS) and VIX is at least 0.5.
- **Bank channel:** SLOOS net tightening is at least 30%.

Across 36 threshold combinations (rates 2.0/2.5/3.0%, stress 0.25/0.5/0.75, bank 20/30/40%/off), at most 17 of 146
quarters change regime, so the history below is not an artifact of one cut-off.

| Year | Quarters | Regime | FF end % | Real FF | Stress z | Baa spread | NFCI | SLOOS net % | VIX | 10y-3m |
|---|---|---|---|---|---|---|---|---|---|---|
| 1990 | `CCC` | C Drought | 7.31 | 3.28 | 0.79 | 1.85 | 0.19 | 51.8 | 23.3 | 0.94 |
| 1991 | `CBBB` | B Lender's market | 4.43 | 0.95 | 0.09 | 1.94 | -0.28 | 23.5 | 18.4 | 2.32 |
| 1992 | `BBBB` | B Lender's market | 2.92 | 0.12 | -0.49 | 1.96 | -0.78 | 3.8 | 15.5 | 3.49 |
| 1993 | `BBBB` | B Lender's market | 2.96 | 0.50 | -0.85 | 2.06 | -1.00 | -13.4 | 12.7 | 2.80 |
| 1994 | `BBBB` | B Lender's market | 5.45 | 3.27 | -0.89 | 1.54 | -0.74 | -16.7 | 13.9 | 2.71 |
| 1995 | `BBBB` | B Lender's market | 5.60 | 3.46 | -0.78 | 1.62 | -0.67 | -7.7 | 12.4 | 0.91 |
| 1996 | `BBBB` | B Lender's market | 5.29 | 3.43 | -0.62 | 1.62 | -0.74 | -2.7 | 16.4 | 1.29 |
| 1997 | `BBBB` | B Lender's market | 5.50 | 4.05 | -0.44 | 1.51 | -0.62 | -8.0 | 22.3 | 1.15 |
| 1998 | `BBBC` | B Lender's market | 4.68 | 3.33 | 0.12 | 1.96 | -0.41 | 7.8 | 25.5 | 0.36 |
| 1999 | `BBBB` | B Lender's market | 5.30 | 3.86 | 0.26 | 2.23 | -0.25 | 8.0 | 24.4 | 0.86 |
| 2000 | `BCCC` | C Drought | 6.40 | 4.53 | 0.55 | 2.34 | -0.11 | 28.3 | 23.3 | 0.03 |
| 2001 | `CCCD` | C Drought | 1.82 | 0.08 | 0.96 | 2.93 | -0.35 | 50.5 | 25.7 | 1.54 |
| 2002 | `DADD` | D Shock | 1.24 | -0.53 | 0.81 | 3.19 | -0.46 | 28.0 | 27.2 | 2.98 |
| 2003 | `DAAA` | A Boom | 0.98 | -0.66 | 0.17 | 2.75 | -0.63 | 8.6 | 22.1 | 2.98 |
| 2004 | `AAAA` | A Boom | 2.16 | 0.09 | -0.65 | 2.12 | -0.70 | -20.4 | 15.5 | 2.87 |
| 2005 | `BBBB` | B Lender's market | 4.16 | 1.88 | -0.79 | 1.77 | -0.59 | -18.3 | 12.8 | 1.07 |
| 2006 | `BBBB` | B Lender's market | 5.24 | 2.92 | -0.69 | 1.69 | -0.56 | -8.0 | 12.8 | -0.06 |
| 2007 | `BBBC` | B Lender's market | 4.24 | 1.84 | -0.14 | 1.85 | -0.21 | 5.7 | 17.5 | 0.15 |
| 2008 | `CDDD` | D Shock | 0.16 | -0.98 | 2.44 | 3.78 | 1.27 | 57.2 | 32.6 | 2.26 |
| 2009 | `DDDD` | D Shock | 0.12 | -1.39 | 2.10 | 4.04 | 0.91 | 37.3 | 31.6 | 3.11 |
| 2010 | `AAAA` | A Boom | 0.18 | -0.88 | 0.20 | 2.82 | -0.31 | -8.0 | 22.5 | 3.08 |
| 2011 | `AAAD` | A Boom | 0.07 | -1.90 | 0.17 | 2.88 | -0.41 | -13.7 | 24.2 | 2.73 |
| 2012 | `AAAA` | A Boom | 0.16 | -1.53 | 0.10 | 3.13 | -0.46 | -4.7 | 17.8 | 1.72 |
| 2013 | `AAAA` | A Boom | 0.09 | -1.46 | -0.40 | 2.75 | -0.71 | -13.2 | 14.2 | 2.29 |
| 2014 | `AAAA` | A Boom | 0.12 | -1.24 | -0.55 | 2.31 | -0.74 | -11.5 | 14.2 | 2.51 |
| 2015 | `AAAA` | A Boom | 0.24 | -0.95 | -0.04 | 2.86 | -0.50 | -2.6 | 16.7 | 2.08 |
| 2016 | `AAAA` | A Boom | 0.54 | -1.23 | 0.11 | 2.87 | -0.37 | 7.4 | 15.9 | 1.52 |
| 2017 | `AAAA` | A Boom | 1.30 | -0.28 | -0.55 | 2.11 | -0.55 | -3.5 | 11.1 | 1.38 |
| 2018 | `AAAA` | A Boom | 2.27 | 0.23 | -0.53 | 1.89 | -0.55 | -13.3 | 16.7 | 0.94 |
| 2019 | `AAAA` | A Boom | 1.55 | 0.01 | -0.32 | 2.23 | -0.56 | 0.3 | 15.4 | 0.04 |
| 2020 | `ADDD` | D Shock | 0.09 | -1.42 | 0.87 | 2.71 | -0.36 | 37.6 | 29.3 | 0.53 |
| 2021 | `AAAA` | A Boom | 0.08 | -5.00 | -0.47 | 1.95 | -0.64 | -15.0 | 19.7 | 1.40 |
| 2022 | `AABC` | A Boom | 4.10 | -0.97 | 0.30 | 2.12 | -0.27 | 11.8 | 25.6 | 0.86 |
| 2023 | `CCCC` | C Drought | 5.33 | 2.10 | 0.25 | 1.91 | -0.27 | 43.9 | 16.9 | -1.32 |
| 2024 | `BBBB` | B Lender's market | 4.48 | 1.58 | -0.38 | 1.55 | -0.42 | 9.5 | 15.5 | -0.97 |
| 2025 | `BBBB` | B Lender's market | 3.72 | 0.85 | -0.23 | 1.70 | -0.49 | 10.2 | 19.0 | 0.09 |
| 2026 | `BBB` | B Lender's market | 3.75 | 0.98 | -0.36 | 1.63 | -0.52 | 4.5 | 18.3 | 0.67 |

### What the data says about the framework

1. **Bad regimes are the minority, but not rare.** Since 1990Q2: Lender's market 58 quarters (40%), Boom 54 (37%),
   Drought 18 (12%), Shock 16 (11%). Roughly **one quarter in four** is a regime where cash is stuck. A fund with a
   10-year life should expect to live through at least one.
2. **Booms do not turn straight into droughts. They go through a hiking cycle.** There is no direct A → C transition
   in 35 years. The observed path is **A → B → C**: 2004 → 2005–07 → 2007Q4, and 2021 → 2022Q3 → 2022Q4. Law 2 ("ideal
   conditions breed non-ideal structures") holds, but the mechanism is the rate rise exposing what the boom built: thin
   equity checks, floating-rate debt and marks nobody tested. That matches the spine in [[wall-street-skinny-insights]].
3. **A drought ends one of two ways, and history splits.** C → B (soft landing) three times: 1991, 1999, 2024.
   C → D (break) twice: 2001 and 2008. 2023 resolved to B: bank tightening eased from ~51% to ~0 while the Fed held at
   5.33%. This is exactly what the private-credit notes describe. Non-bank lenders filled the gap banks left
   ([[wss-credit-distressed]]), so cash stopped being stuck without rates falling.
4. **Every Shock has ended in a Boom** (D → A in all 5 cases), because the policy response to a shock is cutting to
   near zero. Shocks are short (1–7 quarters); booms are long (33 quarters from 2012Q1 to 2020Q1). The structural
   lesson for seats that survive D: the prize is entering A with capital (Law 3, and the fund-timing argument for
   Primary vs. Harlem above).
5. **Droughts start in bank credit before public markets notice.** In four quarters cash was stuck *only* through the
   bank channel, with calm VIX and spreads: 1990Q2, 2000Q3 and all of 2023. Public stress gauges missed the start of
   the 1990 and 2000 droughts and all of 2023. **On the signal dashboard, the Senior Loan Officer Survey (FRED:
   DRTSCILM) is the early warning; VIX and spreads confirm late.**
6. **Rates alone do not make equity non-ideal.** 1992–99 is classified Lender's market (fed funds ~3–6%, real ~3–4%),
   yet it hosted the dot-com IPO boom. Strong growth and a re-rating can overpower the rate axis. The 2×2 has no growth
   axis, which is its biggest blind spot (see *Limits*).
7. **Where we are: 2026Q3 = Lender's market, low stress.** Fed funds 3.75%, stress composite −0.52, SLOOS net
   tightening 0%, curve positive again (+0.67). The nearest boundary is A: if the Fed cuts below 2.5% while stress stays
   low, the map flips to Boom, with everything Law 2 says about what gets planted there.

**Caveats specific to the data.** The bank channel was added *after* the first run missed 2023, so it is partly fitted
to history the framework already expected. It is plausible (bank credit is the channel the notes describe) but not
independently validated. Private exits and fund distributions, the literal "cash coming back", are not on FRED. Adding
IPO counts (Ritter) and distribution yields (Cambridge Associates, PitchBook) would replace the proxy with the real
thing. The ICE high-yield spread on FRED only goes back to 2023 under its licence, so the long history uses Baa.

### How the data squares with the refinements above

- **Split B.** The classifier sees 2024–26 as a clean Lender's market because every public and bank gauge is calm.
  The private signals that make it "C-like for private books" (distributions/NAV, PIK share, BDC redemption requests)
  are not on FRED, so the data **cannot confirm or refute** the split. It is consistent with finding 5: public gauges
  are the last to see private stress.
- **Rates relative to growth.** The classifier uses the nominal policy-rate level. Finding 6 (1992–99 classified B
  while hosting an equity boom) is the data's own evidence for the refinement that the vertical axis should be tightness
  *relative to growth*. A real-rate-minus-growth axis is the obvious next version of `regimes.py`.
- **D′.** April 2025 does not register: 2025Q2 is B, because the stress lasted weeks and quarterly averages smooth it
  away. D′ episodes need daily data (swap spreads, the 10y vs. the dollar) to see.

---

## Retrieval questions

1. **It's 2022 and you run an endowment with a 20% private-equity target. Public equities fall 25% and private marks
   barely move. What happens, and to whom does it spread?** Private is now ~24% of the portfolio, above target (the
   denominator effect, PM §6). You stop recommitting, trim managers or sell LP stakes in the secondary market. The
   managers cut first are emerging ones, which is how a public-market drawdown becomes a venture fundraising drought.
2. **It's 2021 and you are a CLO manager taking $8M of a $1bn cov-lite, loan-only first-lien deal. What happens to you
   in C?** You never read the 300-page document, so a simple-majority amendment can let a co-opted group put $1.2bn of
   new money ahead of you and buy back its own old loans; your price goes from ~85 to ~30 (Cr §14). With no junior
   bonds beneath the loan, recoveries are ~60 cents, not ~80 (Cr §1). A's terms, C's bill.
3. **It's 2026 and you hold a non-traded BDC. Requests hit 30% of NAV against a ~5% quarterly cap. What happens and
   why might it be better than it looks?** The manager pro-rates or gates; you get a fraction of what you asked for.
   Headline requests overstate real demand because investors over-request, and people redeem from the *best* funds
   first (Kroboth, Cr §12). The gate protects you from the worst loans being left to the last holders; a secondary
   buyer may bid 65–80 cents.
4. **It's March 2020 and you run a Treasury basis trade at 20:1. What happens and why?** Cash Treasuries cheapen
   against futures in a dash for cash; the cash leg marks down, futures margin is due, repo haircuts rise, and you sell
   illiquid bonds into a falling market (R §11, HF §15). Convergence at expiry is certain; surviving the path is not.
   The Fed ends up buying Treasuries in size. Regime D: the short-vol position dressed as arbitrage fails.
5. **It's 2025, you are a strategic acquirer at 37x P/E, and you have bid for a target with cash and stock. A rival
   forces you to go all-cash. What does the market do and why?** Your stock falls: at 37x, stock costs ~2.7% of
   earnings while 5.5% debt costs ~4.1% after tax, so all-cash is more dilutive, and it pauses buybacks (CM §13). In B,
   high rates make cash the expensive currency for rich-P/E buyers.
6. **It's 2026 and you bought the bonds of a hyperscaler data-center SPV (A+, ~100bp over the sponsor's curve, a
   four-year lease). What is your scenario map?** In B you are paid for the cancellation option and may flip for gains
   (PIMCO's ~10 points). In C or D the sponsor can walk at a lease break, and you own "a data center in the middle of a
   field without a customer" (AI §7). The spread was the price of a put you wrote on the AI regime.
7. **It's 2023 and you are a regional bank that put 2021 deposit inflows into long Treasuries. What happens?** Rates rose
   ~400bp; duration turns that into large mark-to-market losses (the 1.375% 2050 traded near 46 cents, R §9). If
   depositors run, the losses crystallize (SVB). An A-regime asset choice meeting a C-regime liability run.
8. **It's late 2008. A PE fund with a 10-year lock and a hedge fund with quarterly redemptions own the same distressed
   bond at 40. Who keeps it, and why?** The PE fund: its holding period is set by its lockup, while the hedge fund's is
   set by redemptions and margin, so it may be forced to sell at the bottom (Cr §15, HF "How the concepts connect").
   Same asset, same thesis, different structure. Law 3.
9. **It's 2026 and you are an emerging VC manager raising a $150M Fund III. What regime change helps you most, and what
   hurts most?** A move back toward A (credit at 5–6%) reopens the venture premium and sends LP money to emerging
   managers first (AV §2). A D during the raise hurts most: the denominator effect freezes commitments just as entry
   prices hit their low, so the fund that most needs to exist at the bottom cannot close (AV §9).
10. **It's 2021 and you are a sponsor buying a SaaS company at 20x EBITDA with a 7x unitranche and a PIK toggle. Walk it
    through B and C.** In B, floating-rate interest rises as the SaaS-pocalypse caps growth; you elect PIK, and the
    claim compounds while the asset does not (Cr §10). In C, lenders refuse more PIK and ask for new equity or the keys
    (Medallia, AI §17). The equity check was ~65% by arithmetic (Cr §11), and that cushion is what decides whether the
    lenders or you absorb the first loss.

---

## Limits: what this synthesis cannot tell you

- **Two axes are a compression.** The 2×2 leaves out inflation regime (an oil shock is stagflationary and fits no cell
  cleanly; March 2026 raised rates with windows still open), fiscal term premium and central-bank credibility (R §6),
  geopolitics, and sector-specific cycles such as AI or office. Refinements 1–3 patch the worst gaps; they do not
  remove them.
- **Regimes are labelled after the fact.** Private marks lag public prices by quarters and DPI by years, so a real-time
  call is always partly stale, and the dashboard's most diagnostic private signals (DPI, PIK share, BDC requests) are
  self-reported by interested parties and not on FRED.
- **The sample is tiny.** The modern record has roughly two clean D episodes, one or two C's, and a B that is still
  running. Base rates for "how long C lasts" or "how often C becomes D" cannot be computed from this many cases.
- **The channel mostly saw one regime.** Nearly all transcripts date from 2024–26 (split B, with one D′ in April 2025).
  The A, C and D cells lean on the hosts' retrospective stories (2007 CLOs, 2008 plumbing, 2020 SPACs, BREIT in 2022),
  which carry their sell-side bias and their misremembered figures (e.g. 2008 defaults "peaked at 2%"; actually ~10–14%,
  Cr §18).
- **Seats are not homogeneous.** Each verdict describes the median occupant of a seat. Law 3 means a well-structured
  direct lender in D can beat a badly structured one in B; the matrix cannot see structure, only the seat.
- **The map does not time anything.** It says what each regime rewards, not when the next transition comes or which
  trigger fires. The B → C table lists five candidate triggers from the notes; it does not rank them.
- **US-centric.** European real estate is bank-dominated (PM §11), the ECB's 2025 cuts came with a *bear* steepener
  (R §3), and Japan's rate regime runs the other way (R §15). The cells do not transfer without adjustment.
- **2026 facts are as reported on air.** SpaceX, Anthropic, Situational Awareness and the Warsh hike are unverified in
  the source notes, and this note inherits that status.
- **This is a map for reading mechanisms, not a positioning tool.** It is built to answer "who is paying whom in this
  regime, and what structure survives the next one," not "what to buy."
