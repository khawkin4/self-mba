# Feroldi's Stock Screening: Quality Checklist, Moat Sources, Earnings-vs-Cash Traps

> **Sources:** Brian Feroldi, *Long-Term Mindset* (brianferoldi.substack.com). Pulled 2026-11-01 via the
> Substack archive: **418 posts, 404 paid-only, 14 free**. All 14 free posts were pulled (2026-09-02 to
> 2026-10-31), including four "Is X a Buy at $Y?" teardowns (Broadcom, Visa, Meta, Microsoft), one on Nvidia,
> a five-part moat series, Nike's moats, MercadoLibre, share count and market efficiency. Paid posts were
> skipped, among them "When is a valuation too high to buy?" and "The 4 Value Traps". Public product
> listings were recorded as metadata only (Gumroad storefront, brianferoldi.com). Summarized in own words;
> raw text stays in `_ingest/raw/2026-11-01/feroldi/`.
>
> **What it adds:** a repeatable *screen-and-thesis* front end for step 5, which the repo lacked. It gives
> a fixed scorecard, a named moat source, and a handful of forensic checks that catch "cheap" stocks which
> aren't. Each teardown ends with an explicit **move-to-Buy** and **walk-away** trigger, which is a ready
> template for kill criteria.
>
> **Lens:** Decide. **Serves methodology steps:** 5 (screen, thesis, kill criteria, review). Light on
> valuation. Step 7 only via his "most people should index" caveat.
>
> **Maps to:** Course 02 (valuation inputs), Unit 07 (moats), E2 (capital allocation).
>
> ⚠ **Bias:**
> - Every free post now ends with an ad for **Stock Simplifier**, his own scoring app (free tier, paid
>   upgrades), and the slides in the teardowns are that app's output. The method is partly a sales funnel
>   for it.
> - The **Feroldi Quality Score** (with Brian Stoffel) is sold on Gumroad as "Investing Checklists" for
>   **$9.99** (54 ratings, avg 4.9). The listing says only that these are the checklists the two Brians use
>   to judge a company's quality. **Its criteria were not pulled and are not described here.**
> - Optimistic about compounders. All share prices, multiples and company figures are his, as of each
>   post's date, and were **not re-verified against filings** [unverified].
> - Not advice.

---

## Core claim

Focus on the business, not the stock. Run every company through the same fixed checklist, name the one moat
source the thesis rests on, and check that reported earnings are really cash before trusting any
multiple. Then write down, *before buying*, the one number that would change your mind.

## Framework

### 1. The 8-step scorecard (as publicly described in the posts)
Every "Is X a Buy" post runs the same sequence: **business → phase → moat → growth → management → risk →
valuation → verdict**. The output is a composite score out of 5 and one of three verdicts: **Buy / Watch /
(Avoid)**.
- **Business quality** checks: predictable revenue, pricing power, recession resistance, dominant position.
- **Phase:** each company goes into one of five lifecycle phases: **Startup → Hyper-growth → Operating
  leverage → Capital return → Decline.** Which metrics matter depends on the phase. A company changes
  phase when its financing flows change, whatever it calls itself (see Meta below).
- **Moat:** rated by width *and direction* (for example "Wide and Growing").
- **Risk:** includes customer and supplier concentration, disruption, and "outside management's control"
  (FX, regulation).
- **Verdicts seen:**

| Company | Score | Verdict | Why |
|---|---|---|---|
| Nvidia | 5/5 on quality, moat, growth, management; risk 2/5 | Watch | Lumpy demand; 2 customers ≈36% of revenue |
| MercadoLibre | 4.6 | Buy (with a watch metric) | |
| Meta | 4.5 | Watch | FCF collapsed under capex |
| Broadcom | 4.3 | Watch | "great business, bad valuation" |
| Visa | 4.2 | Buy | |
| Microsoft | not stated | Buy, "eyes open" | |
| Nike | not scored | "Too hard" pile | |

Takeaway: **a high quality score does not give a Buy.** Risk and valuation can each veto it.

### 2. Name the moat source (five types)
His list, close to Helmer's: **network effects, switching costs, cost advantages, intangibles (brand,
patents), counter-positioning.** You should be able to state which one you rely on in one sentence, and
whether it is widening or narrowing.
- **Network effects:** direct (phone, social) vs indirect, two-sided (Visa and Mastercard). They run in
  reverse when users leave (Myspace).
- **Switching costs:** measured in money, time and hassle. US checking accounts are kept about 17 years
  (2021 Bankrate survey, as he cites it). Enterprise databases: Amazon's migration off Oracle took 100+
  teams and 7,500 databases, which few companies could do.
- **Cost advantages:** scale (financing, marketing, R&D, specialist managers, purchasing) and **location**
  (Compass Minerals' salt mines near winter markets; Casey's in towns of <5,000, too small for a second
  store).
- **Moat test in the numbers:** pricing power shows up as margins rising *while* input costs rise (Broadcom
  passing on foundry price increases) or as volume and price rising together (Meta: +14% ad impressions
  and +12% price per ad in one quarter).
- **Nike case (Sep 2026):** Nike had two moats, brand and wholesale shelf space. Going direct-to-consumer
  gave the shelf space away (On and Hoka took it). Moving spend to measurable performance marketing
  starved the brand. His lesson from his own Under Armour loss: he couldn't tell a durable brand from a
  company that was temporarily good at marketing. Test: if the moat is "the brand", write down what would
  make it stop working, then check whether that is already happening. Compare with
  [[apply-stock-picking-nke]].

### 3. Forensic checks before trusting a multiple
These are the most reusable part.
1. **Put P/E next to P/FCF.** If they are close, earnings are mostly cash (Visa 33.1 vs 34.6). If one is
   about double the other, find out why before buying (Microsoft 28.6 vs 56.9; Meta 28.0 vs 46.3).
2. **Capex vs depreciation gap.** Heavy building makes earnings look better than cash. Microsoft FY26:
   $115.9B capex vs $34.3B depreciation, so about $81.6B of cost still to reach the income statement,
   plus $24.6B in finance leases outside the capex line. Watch operating margin. If it slides as
   depreciation arrives, the spending isn't paying for itself.
3. **Halve the E for cyclicals.** A cheap P/E can be the top of a wave (the Lynch point). Nvidia at 28.4×:
   a repeat of FY23's −55% earnings would make it about 63× at the same price. If it is still cheap on
   bad-year earnings, it may be a bargain.
4. **Throw out a distorted historical average.** Acquisition amortization can make trailing P/E spike and
   make today's multiple look "below average". Broadcom FY24: amortization went from $3.2B to $9.3B after
   VMware, net income was $5.9B against FCF of $19.4B. Judge today's P/E on its own.
5. **Recurring "one-time" charges.** Look back 5–10 years. If a charge appears in about 4 of 5 years, put
   it back into earnings permanently. Visa litigation: $4.8B over 4 years, ≈$1.2B/yr ≈ 5% of operating
   profit. Real, but not a thesis breaker. At about 30% it would be one.
6. **Lenders look worse the faster they grow** (loss provisions are booked up front), and their cash flow
   statements mix in deposits and funding flows. MercadoLibre showed P/E 50.2 vs P/FCF 9.3. **A cheap
   P/FCF screen keeps turning up financial companies** for this reason.
7. **Share count.** Track diluted shares from the 10-Q cover. There are seven events that move it (IPO,
   secondary, convertibles, SBC, splits, stock M&A, buybacks). When buybacks stop, SBC dilution shows up
   (Meta's basic share count up for the first time in years).
8. **Financing section = the real phase.** If buybacks fell to zero and borrowing rose in the same year,
   the company changed phase. Meta: no buybacks in H1 2026, +$24.9B of debt, shareholder yield −2.4%.

### 4. Kill criteria as a written trigger pair
Each teardown ends with two lines. They are directly usable as a step-5 template:
- **Move to Buy if…** For example: Broadcom's customer concentration falls, or its P/E looks reasonable on
  today's earnings. Nvidia's revenue spreads beyond a few hyperscalers, or it looks cheap on bad-year
  earnings.
- **Walk away if…** For example: Broadcom's top customer passes ⅓ of revenue (it was 32%, up from 21% two
  years earlier) while the multiple stays high. Meta's or Microsoft's operating margin keeps sliding
  (Meta 42% → 41% → 38.1%). Visa's incentives to banks grow faster than gross revenue (they were $15.75B,
  ≈28% of gross revenue), which would mean the moat is narrowing.
- **One watch metric per business,** written down before buying and checked every quarter. MercadoLibre:
  the 15–90-day NPL ratio (7.0%) must hold or improve as the loan book matures. Software: net revenue
  retention. Retail: same-store sales.

### 5. Base-rate humility
- The best US stock of 1995–2015 (Monster Beverage, per Housel) fell 50%+ four times. Holding through
  drawdowns is the price of the return.
- He says most people should index. DIY active investors fail on time, interest and temperament.
- He keeps a **"too hard" pile** (Buffett's box) for honest bull-and-bear stand-offs.

## Applies when
- Building a watchlist for the satellite slice: filter on quality and moat first, then run the forensic
  checks, then hand the survivors to a real valuation ([[damodaran-valuation-method]]).
- Writing the thesis and kill-criteria lines for a position: one moat sentence, one watch metric, one
  walk-away trigger.
- Large, well-covered compounders where the risk is paying too much or misreading accounting, not fraud.

## Breaks when
- **Valuation is thin.** Verdicts rest on P/E and P/FCF against the stock's own history and an app's
  "expensive band". There is no DCF and no implied-expectations step. A stock can be "Attractive" on its
  own average and still be priced for heroic growth.
- **Scorecards miss context.** He admits it himself: the app scored MercadoLibre's CEO ownership as 0%
  while the founder-chairman holds a large stake. A score shows where to look, not the answer.
- **Survivorship and selection.** The teardowns are mega-cap winners that have already had big runs. The
  free archive is only two months deep. The paid archive (404 posts) holds most of the method.
- **Product incentive.** A free method that ends in an app subscription will lean on whatever the app
  measures.

## Practitioner counterpoint
- **Damodaran** would move moats and management out of the discount rate and into margins and
  reinvestment, and would demand an explicit value, not a multiple compared with its own past
  ([[damodaran-valuation-method]]).
- **Mauboussin / Dorsey:** a moat should show up as ROIC above the cost of capital for years. Feroldi
  quotes ROIC (Nvidia's 135%) but doesn't make it a gate. Damodaran's data says only about 28% of global
  firms clear that bar, so "wide moat" should be rare in any honest screen.
- **Khan's framework** ([[tiger-sisters-stock-picking]]) covers similar ground (understand, read the 10-K,
  ask why) and adds an explicit circle-of-competence step.

## Links
[[unit-07-the-landscape-moats]] · [[canon-helmer-7-powers]] (the source of counter-positioning) ·
[[unit-02-cash-vs-profit]] (P/E vs P/FCF) · [[unit-05-growth-and-returns]] · [[unit-09-capital-light-businesses]]
(Buffett's great/good/gruesome split, which he applies to Microsoft) · [[apply-stock-picking-nke]] ·
[[tiger-sisters-stock-picking]] · [[sec-filing-intelligence]] (where share count and charges live) ·
[[bet-sizing-conviction]] · [[damodaran-valuation-method]] · [[portfolio-methodology-educators]]

## The one-line habit
For every holding, keep three lines: **moat source (one sentence)**, **watch metric with today's value**, and
**walk-away trigger**. Before quoting any P/E, write the P/FCF next to it.
