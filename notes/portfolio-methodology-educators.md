# Personal portfolio methodology, and who teaches each step

> **Sources:** web research on 2026-11-01 across ~30 educators (creator sites, Substack archives, podcast
> feeds, papers, SEC 13F). Each creator's latest dated output was checked on their own archive where the
> site allowed it; Bogleheads.org, morningstar.com, pwlcapital.com and LinkedIn/X blocked scripted access, so
> claims from those are marked **[unverified]**. Summarized in own words, not reproduced.
>
> **Why this note exists:** the repo had the *pieces* of an investor's toolkit (EDGAR, the Nike stock-picking
> rep, bet sizing, the backtesting field guide) but no end-to-end method for building a personal portfolio, and
> no map of who teaches it. [[rodrigues-derivatives-problem-map]] prompted the search for "people like him";
> most of them turned out to be **Run** content, so this note sorts everyone by lens.
>
> **Maps to:** **Course 02** (valuation), **Course 07** (decisions under uncertainty), **E2** (capital
> allocation), **E11** (personal operating system). Extends [[unit-10-personal-finance-operating-system]].
>
> ⚠ **Not advice.** Educational framework. US account types; contribution limits change yearly. Several
> educators below sell funds or brokerage services whose sales depend on the views they teach. Incentives are
> listed for every creator.

---

## The lens tags

| Lens | Question it answers | Use it for |
|---|---|---|
| **Understand** | How do businesses, markets and financial firms work? | Thinking; inputs to any decision |
| **Decide** | What do I buy, how much, when do I sell, in my own accounts? | Your own portfolio |
| **Run** | How is a large book priced, hedged, funded and risk-managed? | Understanding institutions and careers. Rarely actionable personally |

---

## The methodology: eight steps

The core move: **write the rules before picking the investments.** Professionals call the written rules an
Investment Policy Statement (IPS).

### 1. Objectives and constraints (the IPS)
- One page: goal and target number, horizon, liquidity needs, tax situation, and risk.
- **Risk capacity ≠ risk tolerance.** Capacity is how much loss you can afford. At 30 with stable income it's
  high, because future earnings act like a large bond holding (Bernstein; Ayres & Nalebuff's "human capital"
  framing). Tolerance is what you can sit through without selling. Judge it from your behaviour in a real
  drawdown, not a questionnaire.
- Bernstein separates **deep risk** (permanent loss of real wealth: inflation, confiscation, devastation) from
  **shallow risk** (a temporary price fall). His maxim: once your goals are funded, stop taking risk you no
  longer need.
- **Target number:** ~25× annual spending (the 4% rule). ERN's 1871–2016 data, for a 50/50 portfolio: 4%
  succeeds ~95% of the time over 30 years and only ~65% over 60. His headline: **"3.5% is the new 4%"** for
  early retirees. Verified on the post.
- Teachers: **Bernstein**, **Bogleheads wiki** (IPS page [unverified]), **Big ERN**, **Christine Benz**.

### 2. Strategic asset allocation (the decision that matters most)
- Choose the stock/bond mix and the US/international split. Write the target weights into the IPS.
- **Three-fund portfolio** (Larimore / Bogleheads): total US stock, total international stock, total US bond.
- **Glide paths:**
  - Standard target-date funds de-risk with age.
  - **Ayres & Nalebuff** argue the opposite for the young: ~2:1 leverage (200% stocks) through the 20s–30s,
    stepping down to ~50% by retirement. Critiques:
    - Investors capitulate in the first bear market.
    - It depends on uncertain future savings.
    - CXO Advisory estimates ~25% of followers would have seen a 40%+ one-month drop.
  - **Cederburg et al.** ("Beyond the Status Quo", SSRN 4590406) challenge standard lifecycle glidepaths from a
    different angle. Read both before deciding.
  - In retirement, **ERN** and **Pfau/Kitces** both favour *rising* equity glidepaths, because sequence risk
    is worst early. They disagree on the specifics: ERN (SWR Part 20) rejects the Pfau/Kitces glidepaths
    because they did poorly on historical data, and prefers a fast rise (e.g. 60%→100%) used only when CAPE
    starts above ~20. See [[ern-safe-withdrawal-series]].
  - While still saving, ERN (Part 43) finds ~100% equities defensible until the last 2.5–5 years before
    retirement. Cederburg's result (Rational Reminder eps 284, 350) points the same way: an all-equity,
    one-third US / two-thirds international mix beat target-date funds. See
    [[rational-reminder-portfolio-evidence]].
- **Faber** (*Global Asset Allocation*): the famous portfolios (Dalio, Swensen, Arnott…) end up closer to each
  other than their marketing suggests. Sticking with a reasonable mix matters more than which one you pick.
- **Factor tilts** (size/value/profitability) on top of market-cap indexing: **Ben Felix**, **Swedroe**,
  **Merriman** (heavy small-value). Felix's own firm debated tilts vs plain cap-weight in 2025, so this is
  contested even among its advocates.

### 3. Cheap implementation and asset location
- Lowest-cost broad index funds or ETFs available in each account.
- **Funding order** (Bogleheads, via a Bogle Center chapter talk):
  1. 401(k) to the employer match
  2. HSA, if on a high-deductible plan
  3. IRA (Roth or traditional)
  4. Max the 401(k)
  5. Mega-backdoor Roth or taxable
  - Put the IRA ahead of the 401(k) if plan fees are high.
- **Asset location:** highest expected growth in the Roth; bonds in tax-deferred where possible; tax-efficient
  equity index funds in taxable. ⚠ Ben Felix's asset-location research is **Canadian** (RRSP/TFSA). Use
  Bogleheads/Kitces for US rules.
- ⚠ **Section 351 ETF exchanges:** Faber/Cambria promote them; Kitces (Oct 28, 2026) covers IRS guidance
  limiting some of them. Check current rules before acting on either.
- Teachers: **Bogleheads**, **Kitces**, **Benz**.

### 4. Rebalancing: set the rule before you need it
- **Calendar:** once a year (Carlson's default for most people).
- **Bands, the 5/25 rule** (Swedroe, via *Think, Act, and Invest Like Warren Buffett*): rebalance when an asset
  class drifts outside the **smaller** of ±5 percentage points or ±25% of its target.
  - 70/30 portfolio: act when stocks hit 65% or 75%.
  - 10% small-cap sleeve: band is 7.5–12.5%.
  - Verified on Carlson's post.
- **Kitces** research supports tolerance bands of ~±20% relative for advisors.
- **Rebalance timing luck** (Hoffstein, Faber & Braun, 2020): identical strategies diverge just because they
  rebalance on different dates, often by >100bp/yr for factor indices.
  - The fix is **tranching**: split into N sleeves rebalanced on staggered dates. Noise falls roughly 1/N and
    average returns are unchanged.
  - Matters more for factor/trend strategies than for a three-fund portfolio.
- **Faber's trend rule** (GTAA, 2007 paper): hold each asset class while its monthly price is above its
  10-month moving average, otherwise hold cash. Backtests exclude taxes and costs, so treat it as a rule to
  study, not a free lunch. Check against the backtesting field guide's failure modes.

### 5. Satellite stocks: one process per position
| Stage | What to do | Teachers |
|---|---|---|
| Screen | Start from a defined filter, not tips | **Feroldi** (Quality Score checklist, sold for $9.99), `_ingest/financials.py` |
| Thesis | What must be true; read the 10-K | [[apply-stock-picking-nke]], [[tiger-sisters-stock-picking]], **Dorsey** (moat sources: intangibles, switching costs, network effects, cost advantage, efficient scale; a moat shows up as ROIC > cost of capital for years) |
| Valuation | What does the price already assume? | **Mauboussin** (*Expectations Investing*: reverse-DCF the price → find where expectations are wrong → buy/sell/hold), **Damodaran** (narrative → numbers → value → feed back into the story) |
| Sizing | Starter ~1–2%, per-stock cap, slice cap | [[bet-sizing-conviction]] |
| Kill criteria | Specific facts that make you sell | Nike rep's disconfirming checklist |
| Review | Quarterly, against the thesis, not the price | **Mauboussin** |

Sector depth: **Rubinstein** (banks and fintech), **App Economy Insights** (visual quarterly results; data,
not a process).

### 6. Options: only with a stated purpose
- Purpose first: **income** (covered calls), **cheaper entry** (cash-secured puts), **protection** (buying
  puts). Defined risk only; a fixed maximum loss per trade.
- **The core skill is implied vs realized volatility** (Sinclair, Natenberg). Sinclair's edge has two sources:
  - Durable risk premia, chiefly the volatility risk premium: implied usually exceeds realized.
  - Anomalies that fade once found.
- Sinclair's sizing: fractional Kelly; judge risk by the worst case, not the probability; expect occasional
  losses ~20× the typical win. That last point is why premium-selling "income" is less safe than its win rate
  suggests (Moontower's long-running theme too).
- **tastytrade mechanics:** sell premium at high IV rank, ~45 days to expiry, take profit at 50%, manage at ~21
  days.
  - Evidence is mostly their own studies.
  - ⚠ tastytrade is owned by IG Group (2021, ~$1B), and tastylive is paid to promote the brokerage, so the
    content favours trading frequently.
  - Independent critics say early exits hide tail risk.
- Teachers: **Sinclair** (*Retail Options Trading*, 2024, with Andrew Mack), **Natenberg** (*Option
  Volatility and Pricing*), **Moontower**, **Colin Bennett** (*Trading Volatility*).

### 7. Measurement, the step most people skip
- Benchmark every active slice against **the index you would otherwise hold**, after costs and taxes.
- Keep a decision journal: probability of being right, the size chosen, the outcome. Separate skill from luck
  before scaling a slice up.
- Teachers: **Mauboussin** ("Probabilities and Payoffs"; skill vs luck, [[canon-mauboussin-success-equation]]),
  [[canon-duke-thinking-in-bets]], [[canon-tetlock-superforecasting]].
- **Repo gap:** no scorecard or IPS template exists yet.

### 8. Review cadence
- Quarterly look; annual IPS review or after a life change. Never rewrite the IPS because of what markets did.
- Benz's annual portfolio checkups; Bernstein's "stop playing once you've won".

---

## Creator registry

Status = the latest dated output found on 2026-11-01. "Pull" = how the content could be ingested via `_ingest/`.

### Decide: for your own portfolio
| Creator | Status | Steps | Pull | Incentive / bias |
|---|---|---|---|---|
| **Ben Felix**, Rational Reminder | Ep #433, Oct 29 2026 | 1–3 | ★★★ episode transcripts on rationalreminder.ca | PWL Capital AUM; PWL bought by OneDigital (Jan 2025). Factor-tilt advocate. Canadian tax lens |
| **Bogleheads** (wiki, forum, Rick Ferri's podcast) | Podcast Ep 99, Oct 20 2026 | 1–4, 8 | ★★ podcast RSS; wiki/forum block scripts (read manually) | Nonprofit, low conflict. Index orthodoxy, US-centric |
| **Christine Benz**, Morningstar | Active mid-2026; Oct [unverified] | 1, 2, 4, 8 | ★★ podcast; site blocks scripts | Morningstar employee (ratings business). Bucket approach (from Evensky) |
| **Karsten Jeske**, Big ERN | SWR Part 66, Oct 19 2026 | 1, 2, 8 | ★★★ blog RSS + free SWR spreadsheet | No products. US historical data only |
| **Paul Merriman** | 2026 Bainbridge series; Ultimate Buy & Hold 2026 | 2, 4 | ★★ podcast + site | Retired adviser, nonprofit. Heavy small-value bias; states a 5% withdrawal rule (vs ERN's 3.5%) |
| **Ayres & Nalebuff** | Nothing on leverage since 2013 | 1, 2 | ★ book, NBER w14094 | Academics. Contested leverage thesis |
| **Brian Feroldi** | Oct 31 2026 | 5 (screen, thesis) | ★★★ Substack RSS, YouTube | Paid templates and courses. Optimistic about compounders; light on valuation |
| **Euan Sinclair** | AD Derivs podcast, 2026 | 6 | ★ books, podcasts | Books, teaching. Low conflict |
| **Moontower** (Kris Abdelmessih) | Oct 29 & Nov 1 2026 | 6, sizing | ★★★ Substack RSS | Ex-SIG options trader. Sells moontower.ai analytics |
| **tastytrade / tastylive** | Show ongoing; Sosnoff left Sep 2025 (per Wikipedia) | 6 mechanics | ★★★ YouTube volume | ⚠ Broker-owned (IG Group); pushes high activity |

### Understand: thinking and inputs
| Creator | Status | Steps | Pull | Incentive / bias |
|---|---|---|---|---|
| **Michael Mauboussin**, Counterpoint Global | Paper Sep 17 2026 | 5, 7 | ★★ free PDFs, but morganstanley.com returned 403 on 2026-11-01; 2001–24 papers came via michaelmauboussin.com links, mid-2024 onward missing | Effectively MSIM marketing; sells nothing directly |
| **Aswath Damodaran** | Anthropic IPO valuation, Oct 28 2026 | 5, 2 (market assumptions) | ★★★ Substack RSS, free datasets | Academic. Books and paid certificates |
| **William Bernstein** | ~May 2026 Merriman talk; site dormant | 1, 2 | ★ books | Books, advisory firm. Low conflict |
| **Ben Carlson & Michael Batnick** | Both Oct 30 2026 | 2, 4, 8 | ★★★ blog RSS, podcasts | Ritholtz AUM; Talk Your Book is sponsored fund pitches |
| **Meb Faber** | "How I Invest 2026", Oct 30 2026 | 2, 4, 5 | ★★★ podcast, blog, SSRN | ⚠ Cambria CEO; research often lines up with Cambria funds |
| **Joseph Wang**, Fed Guy | Markets Weekly ~Sep 2026; blog Feb 2026 | Regime awareness (feeds `regimes.py`) | ★★ blog (direct fetch blocked) | Runs money at Monetary Macro; sells courses |
| **Marc Rubinstein**, Net Interest | Oct 30 2026 | 5 (financials sector) | ★★ RSS; half of each issue paywalled | Fintech consultant and angel |
| **App Economy Insights** | ~Nov 1 2026 | 5 inputs | ★★ RSS; PRO paywalled | Subscriptions; big-tech tilt |
| **Pat Dorsey** | Fund active (13F Aug 2026); no talks found | 5 (moats) | ★ books, podcasts | Institutional fund. Concentrated (~11 names) |
| **Sheldon Natenberg** | Not current (latest 2023) | 6 mechanics | ★ book | Textbook standard |
| **Scott Cederburg** | Rational Reminder #350 | 2 (lifecycle critique) | ★★ papers, podcast | Academic |

### Run: institutions, like Rodrigues
| Creator | Status | Closest to Rodrigues in | Pull | Notes |
|---|---|---|---|---|
| **Conks / Concoda** | Oct 31 2026 | **Format**: infographic plumbing primers | ★★★ Substack RSS | Repo, cross-currency basis, G-SIB. Paid Pro tier |
| **Joseph Wang** | (above) | **Format**: one mechanism per post | ★★ | Also Understand |
| **Jon Gregory** | *The xVA Challenge* 5th ed., mid-2026 | **Topic**: XVA | ★ books, paid courses | Vendor-adjacent panels |
| **Antoine Savine** | Moved to Barclays (Global Head of Rates Quants), late 2025 | **Topic**: AAD, rates | ★★ GitHub lecture notes, code | Long-form, code-first |
| **Larry Swedroe** | Substack ~daily, Oct 30 2026 | n/a | ★★★ Substack RSS | Left Buckingham Jun 2024. ⚠ A critic alleges undisclosed promotion of a private-credit fund |
| **Corey Hoffstein** | Flirting with Models, Oct 12 2026 | n/a | ★★★ podcast, blog | ⚠ PM of Return Stacked ETFs; the stacking advocacy sells them, the timing-luck research doesn't |
| **Michael Kitces** | Oct 26–30 2026 | n/a | ★★★ RSS | Advisor audience. Bond tent, rising glidepath |
| **Paul Wilmott** | Mar 2025 article | n/a | ★★ blog, QuantSpeak podcast | Sells CQF. Model skepticism is useful to anyone |
| **Damiano Brigo** | Papers to Nov 2024 | **Topic**: rates, CVA | ★ papers | Academic |
| **Riccardo Rebonato** | Shifted to climate finance (EDHEC) | **Topic**: rates | ★ books, Coursera | Term-premium material is useful to bond investors |
| **Colin Bennett** | No output 2024–26; role unclear | **Topic**: vol | ★ book | Not an active creator |

---

## Distilled notes (pulled 2026-11-01)

Raw corpora for all of these are under `_ingest/raw/2026-11-01/` (gitignored).

| Step | Note | Source pulled | Gaps |
|---|---|---|---|
| 1, 2, 4, 8 | [[ern-safe-withdrawal-series]] | All 66 parts + the case-studies post | None |
| 1–4, 8 | [[rational-reminder-portfolio-evidence]] | 26 methodology episodes | No dedicated rebalancing episode; the 2025 PWL tilts debate wasn't found |
| 5, 7 | [[mauboussin-counterpoint-methods]] | 20 papers, 2001–24 | morganstanley.com returned 403, so mid-2024 onward is missing, including all 2026 papers |
| 5 | [[damodaran-valuation-method]] | 48 posts (last 12 months + methodology) | None |
| 5 | [[feroldi-stock-screening]] | 14 free posts | 404 of 418 are paid; Quality Score criteria not pulled |
| 6 | [[moontower-options-intuition]] | 107 free posts | Paid posts skipped, incl. the tail-hedge piece |
| 2, 4 | [[swedroe-factors-rebalancing]] | 99 free posts + the critique | 5/25 rule not in his recent posts (secondary source only) |
| 3, 4, 8 | [[kitces-planning-methods]] | 9 core posts + feed | None |
| Regimes | [[fedguy-liquidity-plumbing]] | 8 YouTube transcripts | fedguy.com refused connections |
| Regimes | [[conks-funding-plumbing]] | 28 free posts | Paid primers skipped; 11 of 14 infographics unread |
| 2, 4, 7 | Own backtest (kept private) | Baseline + 11 mutations, 1990–2026 | One history; taxes ignored |
| 6 | Own backtest (kept private) | Covered calls, put-writes, protective puts, collars, condors vs the market; implied vs realized vol, 1986–2026 | Costs, spreads and taxes not deducted |
| 2, 5 | Own backtest (kept private) | Sectors, commodities, bitcoin; decade persistence; momentum vs past-winner rules, 1937–2026 | Industry portfolios aren't funds pre-1998; bitcoin is a survivor |

## Pull queue (suggested order)

Ranked by Decide value × pullability. All are RSS or transcript sources that `_ingest/` can handle without a
logged-in browser.
1. **Big ERN**: SWR series (66 parts) → steps 1, 2, 8
2. **Rational Reminder**: transcripts → steps 1–3
3. **Mauboussin**: Counterpoint PDFs → steps 5, 7
4. **Damodaran**: Substack + data updates → step 5
5. **Moontower**: Substack → step 6
6. **Swedroe**: Substack → steps 2, 4 (read with the disclosure caveat)
7. **Feroldi**: Substack → step 5
8. **Kitces**: RSS → steps 3, 8
9. **Wang** and **Conks**: Understand / Run, the closest Rodrigues-style feeds

Manual-only:
- Bogleheads wiki (IPS, three-fund and funding-order pages)
- Morningstar (Benz)
- LinkedIn (Savine and Gregory, if they post)
- Books: Bernstein, Sinclair, Natenberg, Dorsey

Raw corpora go under `_ingest/raw/` (gitignored), as with Rodrigues.

## Open questions [unverified]
- The Bogleheads IPS wiki page contents
- Benz's October 2026 output
- Ben Felix's current title
- Swedroe's current employer
- Colin Bennett's current role
- Natenberg's employment status
- Euan Sinclair at Hull Tactical
- Whether Cederburg et al. test leverage

## Links
[[unit-10-personal-finance-operating-system]] · [[bet-sizing-conviction]] · [[apply-stock-picking-nke]] ·
[[tiger-sisters-stock-picking]] · [[rodrigues-derivatives-problem-map]] · [[wss-scenario-map]] ·
[[canon-mauboussin-success-equation]] · [[canon-klarman-margin-of-safety]] · [[canon-taleb-black-swan]] ·
[[canon-duke-thinking-in-bets]] · [[canon-tetlock-superforecasting]] ·
[[harvey-liu-zhu-backtesting-pitfalls]]
