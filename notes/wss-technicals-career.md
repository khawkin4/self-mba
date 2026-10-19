# Wall Street Skinny — technicals & career: how deals are priced, financed, and paid for

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-capital-markets-ma]] [[wss-credit-distressed]] [[wss-private-markets-wealth]] [[wss-rates-macro]] [[wss-trading-hedge-funds]]

> **Sources:** Pass 1: 29 items in the `technicals-career` cluster (5 long videos, 24 shorts) + the High
> Yield Harry compensation episode (`FErYd8yHf18`) + a keyword scan of `culture-other`. **Pass 2:** the 30
> newly recovered `technicals-career` files (11 long videos, 19 shorts; 11 shorts are music-only), four
> gap titles routed elsewhere (*Elite Boutique vs. Bulge Bracket* `zEnUJLR29OE`, *Industry S2E7*
> `5yDEBpGLofI`, *Bankers vs. Lawyers* `4K9ZjBkSTT4`, *#1 of Top 5 Technical Questions* `NTF9MY-817E`), and
> a full read of the second half of `culture-other` (10 long videos, 23 shorts). Roughly 95 transcripts
> in total. Raw: `_ingest/raw/2026-10-04/media/wall-street-skinny/`.
>
> **Maps to:** Course **01** (the three statements, as a model), Course **02** (Corporate Finance &
> Valuation: DCF, WACC, capital structure, EV, LBO arithmetic, IRR), Course **03** (incentive design:
> deferral, clawbacks, bonus caps), Course **09** (career/org: the 2+2+2 pipeline, golden handcuffs,
> boutique vs. bulge bracket), Course **11** (credit cycles, rates plumbing), **E2** (Capital Allocation),
> **E3** (M&A, Deals & Restructuring: LBO structure, sources & uses, rollover, Chapter 7 vs. 11, IPO vs.
> direct listing), **E4** (Governance: related-party marks, research conflicts, audit), **E8** (Investor
> Relations).
>
> **Pass 2 replaced the reconstructions.** The DCF, WACC (cost of debt, cost of equity, beta choice, how
> debt changes WACC), three-statement build, LBO and cash-free/debt-free sections are now taught from the
> channel's own dedicated videos, with the hosts' numbers. Still self-derived and labeled as such: the
> WACC weighting example (Part 1 of the WACC series has no transcript), the rule-of-72 cross-check, and
> the EA paper-LBO extension in §4.8. The *Top 8 Technicals* shorts exist but are music-only.
>
> ⚠ **Bias:** both hosts are ex-Morgan Stanley sell side (Kristen: IBD / financial sponsors / CLO desk;
> Jen: rates S&T) and sell courses and boot camps in nearly every episode. Watch for: (1) instinctive
> defense of the bank-intermediated system (CLOs "are not 2008", the Centerview analyst is probably in
> "the wrong job"); (2) guests talking their book — Spotify's SVP on Spotify's model, Citi's head of
> research on why research still matters, High Yield Harry selling a comp-data platform; (3) comp data
> that is self-reported and anonymous (Buyside Hub), so it skews toward people proud of their number.

---

## What this adds to the program

- **The valuation toolkit, from the channel's own interview series.** The repo builds a DCF from scratch
  ([[unit-06-whats-a-business-worth]]) but has no WACC, CAPM or beta anywhere. New here: the channel's
  worked cost of debt (7% × 0.75 = 5.25%) and cost of equity (4.25% + 1.25 × 5.5% = 11.125%), the
  theory-vs-practice split on beta (forward Barra vs. Bloomberg adjusted, and why the sell side
  standardizes for litigation), the U-shaped answer to "how does debt change WACC," and the earnings-yield
  vs. cost-of-equity confusion that conflates EPS accretion with valuation.
- **Enterprise value has no home in the repo.** `GLOSSARY.md` and `learn/unit-06` teach DCF as
  "discount the cash" but never separate *equity* value from *firm* value. The channel's X/xAI
  short is the cleanest demonstration available: a "$33B" deal and a "$44B" deal that are the
  **same price**. This note adds EV, and why every LBO/M&A headline must be decoded through it.
- **The LBO is in the repo only as a house analogy** ([[tiger-sisters-private-capital-101]], Toys "R"
  Us). New here: Kristen's worked LBO ($3M equity → $9M, 3.0x, ~25% IRR, decomposed into EBITDA growth
  vs. debt paydown), the **equity check as the real risk dial** (TXU ~18% vs. EA ~65%), sources & uses,
  cash-free/debt-free and rollover equity (Skechers), and who actually funds the debt.
- **How finance people are paid, with numbers.** [[trading-floor-mechanics]] says entry pay is
  "roughly six figures" and stops. New here: the base/bonus split by level (IB vs. PE/private credit),
  the **one-third cash / one-third deferred cash / one-third deferred stock** structure, why deferral
  makes seniors expensive to poach, how the EU bonus cap *raised* fixed pay, and carry economics by
  fund size. This is applied agency theory ([[canon-jensen-meckling-agency-theory]]).
- **Failure modes and firm models**: First Brands (double-pledged receivables), the "11,000-to-1"
  Treasury short, JPMorgan's $20B sole underwrite, 2008's bilateral-swap contagion; the IPO pop as a
  transfer to allocated investors (Figma ≈ $3B); and Scott Bok on why advice-only boutiques exist and
  why he sold Greenhill into Mizuho anyway.

---

## Concept map

| # | Concept | One line | Why it matters | In repo? |
|---|---|---|---|---|
| 1 | Three-statement model | IS → CFS → BS, linked so every assumption balances | Base of every DCF/LBO; you don't always need it | partial |
| 2 | Equity value vs. enterprise value | Equity + net debt = the price of the whole business | Headline deal prices are usually the wrong number | **n** |
| 3 | The DCF | Project unlevered FCF, add terminal value, discount at WACC | The intrinsic valuation; the #1 interview question | partial |
| 4 | The WACC and beta | Weighted after-tax cost of debt and CAPM cost of equity | The discount rate is where judgment hides | **n** |
| 5 | Capital structure and WACC | Debt lowers WACC until distress risk raises it | Interview staple; CFO financing choice | **n** |
| 6 | EBIT vs. EBITDA & the interest cap | Tax law lets you deduct interest up to 30% of one of them | Decides the size of the debt tax shield | **n** |
| 7 | The LBO and the equity check | Buy with debt; the equity share sets who eats the first loss | The dial behind TXU's bankruptcy and EA's cushion | partial |
| 8 | Paper LBO, IRR, rule of 72 | Back-of-envelope return math in your head | How PE screens a deal in 3 minutes | **n** |
| 9 | Sources & uses, CFDF, rollover | The buyout budget; cash and debt settled at close | Where fees and the equity check are computed | **n** |
| 10 | Who funds the debt: syndication → CLO → private credit | Banks originate risk and then distribute or hold it | Determines where losses land in a downturn | partial |
| 11 | Club deals vs. co-invest | Many sponsors vs. one sponsor plus LPs | Governance of the buyer, and fee economics for LPs | **n** |
| 12 | Collateral, covenants, recovery, bankruptcy chapters | What lenders hold and when they can act | Why loans recover ~70c and fraud surfaces late | partial |
| 13 | Shorting bonds, repo haircuts, settlement fails | Borrow, sell, return; the haircut prices the client | Where a tiny fund put $250M of loss on the street | partial |
| 14 | Treasury auctions | Single-price (Dutch) auction; WI, tail, stop-through | The supply events that move the rates market | **n** |
| 15 | IPO pricing, the pop, lockups, direct listings | Banks underprice ~15%; anything above is a transfer | Figma's ~$3B gift to allocated buyers | **n** |
| 16 | Private marks & related-party valuation | A private price set by an interested party | xAI/X; also how private credit "marks at par" | partial |
| 17 | Sell-side research economics | Analysts sell insight to investors and access to companies | Why coverage stops when a bank is mandated | partial |
| 18 | Elite boutique vs. bulge bracket | Advice-only vs. advice plus balance sheet | Conflicts, cyclicality, where juniors learn | **n** |
| 19 | Banker & buy-side comp structure | Base fixed, bonus variable, seniors deferred | Incentives, retention, poaching costs | **n** |
| 20 | Carry economics by fund size | 20% of profits split in basis points | Why small funds hand out carry and megafunds don't | partial |
| 21 | The career pipeline (2+2+2, on-cycle) | IB as PE's outsourced training program | Explains recruiting games and the "last chopper" at ~30 | partial |
| 22 | Culture-other teaching | Mechanisms embedded in TV recaps | Axes, 2008 plumbing, fraud patterns, gating | partial |

---

## 4 · Concepts

### 4.1 The three-statement model, and when you don't need one

- **What it is:** A linked projection of a company's income statement, cash flow statement and balance
  sheet in Excel, so that one assumption change (say, revenue growth) flows through profit, cash and
  the balance sheet at once. It is the "language" Kristen says bankers speak; the DCF, the LBO and the
  merger model are all built on top of its outputs.
- **How it works (Kristen, *ESSENTIALS for Building a 3 Statement Financial Model*):** She orders the
  statements **income statement → cash flow statement → balance sheet**, not the textbook IS → BS → CFS,
  because that is the path one dollar takes: net income closes the income statement and opens the cash
  flow statement (the *indirect method*); the cash flow statement converts it to a change in cash; that
  cash lands on the balance sheet. Her build sequence:
  1. Income statement from sales down to net income, **leaving holes** for interest expense and interest
     income (they need the debt and cash balances, which don't exist yet) and for D&A (needs capex).
  2. Balance sheet line by line through **supporting schedules** (working capital, PP&E, debt), top to
     bottom, with cash left for last.
  3. Every balance sheet projection has a twin on the cash flow statement (more PP&E is capex; more
     receivables is a cash outflow). "You can't do one without the other": if a line moves on one
     statement and not the other, the model won't balance, and you lose hours finding it.
  Once the schedules exist the holes fill and the model closes (interest depends on cash, which depends
  on interest: the circularity analysts switch on iterative calculation for, which the hosts don't
  name).
- **Business significance:** A **DCF does not need the full linked model**: it uses only unlevered
  cash flows, so you can pull EBITDA, D&A, capex and the change in working capital into an output tab and
  skip the debt and the balance sheet. Some LBOs on the sponsors desk were run on cash flows plus a debt
  schedule only. But a PE modeling test will expect the full three statements. And her teaching
  observation: students say two days building one taught them more accounting than a semester of class.
- **Forces & impact (the *Financial Modeling & Excel MUST KNOWS* episode):** Banking models are valued
  because they are a **transferable representation of a business**, unlike trading-desk models
  (convertible pricing with Monte Carlo engines, CDO models) that programmers build, nobody formats
  because no client sees them, and whose skill doesn't travel. Conventions are near-universal: **blue
  inputs, black formulas, green links to other sheets**. Keyboard over mouse because a model is thousands
  of formulas; Windows over Mac Excel; learn native shortcuts for interviews (you won't have your add-ins
  on someone else's machine), then load productivity add-ins on the job. Excel inertia is structural:
  Morgan Stanley was still on Excel 2003 in 2010 because the ribbon broke everyone's key sequences.
  The model's output is a *conversation with a CEO*, not a P&L position, so presentation is part of the
  substance.
- **With vs. without:** With linked statements, every assumption is forced to be internally consistent
  (growth needs working capital and capex, which need funding). Without them, a cash-flow-only model can
  assume growth for free; the balance sheet is the check that catches it.
- **Applies when** you need debt capacity, credit stats, or EPS (LBO, merger, restructuring). **Breaks
  when** it's overkill: a quick DCF or a screening valuation.
- **Channel example:** *ESSENTIALS for Building a 3 Statement Financial Model*; *Financial Modeling &
  Excel MUST KNOWS for Investment Banking x Macabacus* (with Macabacus founder Ryan McGregor, ex-Lehman,
  who built the tool in 2008 after being laid off; acquired by CFI in 2021).
- **Counterpoint:** The modeling episode is partly an ad (Macabacus is a sponsor; the hosts were
  launching their own modeling course). The craft claims hold, but "you can knock out a model in 20
  minutes to an hour" is Kristen-speed, not analyst-speed.
- **Links:** [[unit-02-cash-vs-profit]] (why net income isn't cash); [[unit-03-what-a-company-owns-and-owes]]
  (the balance sheet); [[aapl-10k-fy2025]] (a real set of statements to model).

### 4.2 Equity value vs. enterprise value

- **What it is:** *Equity value* is what the shares are worth. *Enterprise value* (EV) is what the
  whole operating business is worth: equity plus debt (strictly, plus debt and preferred, minus
  cash). Buying a company means buying the equity *and* taking on its debt, so EV is the real price.
- **How it works:** The hosts' house analogy (*#1 Top 5 Technical Questions*): a $5M house bought with
  $1M down and a $4M mortgage. You didn't buy a $1M house; you bought a $5M one, financed 20/80. The
  X/xAI short applies it: xAI bought X in an all-stock deal at **$33B equity value**, but X carried
  **~$12B of debt** (mostly from Musk's 2022 buyout), so EV ≈ **$45B**. In 2022 Musk paid **$44B**
  when X had **~$0.6B** of debt, EV ≈ $44.6B. Arithmetic: 33 + 12 = 45 vs. 44 + 0.6 = 44.6. Same price;
  the "markdown" was a financing change, not a valuation change.
- **Business significance:** Every multiple that matters to a buyer (EV/EBITDA, the LBO's 20x for EA)
  is EV-based, because EBITDA is earned for *all* capital providers. Equity multiples (P/E) belong to
  shareholders only. Mixing them is the commonest error in deal headlines, and the hosts note that
  TXU is reported as both a "$30B" and a "$45B" LBO for exactly this reason.
- **Forces & impact:** Leverage moves value between the two lines. Pile on debt and, for the same EV,
  equity shrinks; this is the whole engine of §4.7. Second-order: a falling "valuation" can be pure
  re-leveraging, and a rising one can be debt paydown.
- **With vs. without:** Without EV, a company with $40B of debt and $5B of market cap looks "cheap"
  next to a debt-free $20B one. With it you see the first costs $45B.
- **Applies when** comparing businesses with different capital structures, or acquisitions. **Breaks
  when** "debt" is ambiguous: leases, pensions, off-balance-sheet obligations (First Brands, §4.12),
  minority interests. EV is only as honest as the debt list.
- **Channel example:** *The Truth About the $33Bn Elon Musk's xAI Paid for X*; *#1 of Top 5 Technical
  Questions*.
- **Counterpoint:** The short says "true value is EV." Value to *whom* matters: xAI's outside
  shareholders paid in stock, so their question is the relative value of two private stocks, both
  marked by a party on both sides (§4.16). EV arithmetic doesn't fix a soft mark.
- **Links:** [[unit-06-whats-a-business-worth]] (cash-flow logic this sits on); GLOSSARY "Leverage".

### 4.3 The DCF: intrinsic value, and the interview answer

- **What it is:** One of the three standard ways to value a company, alongside public comparables
  (what similar listed companies trade at) and precedent transactions (what similar companies were
  bought for). The discounted cash flow analysis is the **intrinsic** one: value comes from the cash
  this business will produce, not from what other businesses fetch.
- **How it works (Kristen, *Walk Me Through the DCF in Under 3 Minutes*):** Three steps.
  1. Project **unlevered free cash flow** (cash generated for all capital providers, before interest)
     for 5, 10 or 15 years. Academically you project until the company reaches steady state; in
     practice you stop at 5–15.
  2. Add a **terminal value** for everything after the projection: either the **perpetuity growth
     method** (grow the last year's cash flow forever at a constant rate) or the **exit multiple
     method** (assume the business is sold at a multiple, usually of EBITDA). Academics dislike the
     second, she notes; banks use it routinely.
  3. Discount every cash flow and the terminal value back at the **WACC** (§4.4) and add them up. The
     sum is **enterprise value** (§4.2), not equity value.
  Why discount (*DCF in Investment Banking: Theory vs. Reality*): inflation, the risk the cash never
  arrives, and opportunity cost (money today could sit in a ~5% Treasury). Kristen's point on effort:
  she could explain the DCF in one three-minute video; the WACC took three.
- **Business significance:** The DCF is the methodology that answers "what is this worth to *anyone*,"
  which is why it anchors fairness opinions and buy-side underwriting. For a banker it is one bar on the
  football field next to comps and precedents; the episode on modeling stresses it's part of a
  *holistic* picture shown to a CEO, not a trading model.
- **Forces & impact:** Rates move the discount rate; the terminal value usually carries most of the
  value, so the exit multiple quietly imports market pricing back into an "intrinsic" method. The
  hosts' recurring *Industry* joke makes the second-order point: lower the WACC and the valuation goes
  up, so a DCF can be tuned toward the answer the client wants to hear (§4.4 on why banks standardize
  inputs).
- **With vs. without:** With a DCF, a buyer has a value independent of a frothy comp set. Without it,
  every valuation is relative, and a sector-wide bubble looks "fairly priced" against itself.
- **Applies when** cash flows are forecastable (mature, positive FCF). **Breaks when** the terminal
  value is most of the answer, cash flows are negative for years (early-stage), or the exit multiple
  method turns it back into a comps analysis.
- **Channel example:** *Walk Me Through the DCF in Under 3 Minutes*; *DCF in Investment Banking:
  Theory vs. Reality*.
- **Counterpoint:** The three-minute answer is an interview script; it doesn't say how sensitive the
  output is. A 1-point change in WACC or terminal growth can move value 15–25% on a typical model,
  which is why the football field shows ranges, not points (standard practice, not stated by the hosts).
- **Links:** [[unit-06-whats-a-business-worth]] (the repo's DCF built from scratch);
  [[bloomberg-terminal-instrumentation]] (`XLTP` DCF template).

### 4.4 The WACC: cost of debt, cost of equity, and choosing a beta

- **What it is:** The **weighted average cost of capital** is the DCF's discount rate: the blended
  return that lenders and shareholders require, weighted by how much of the business each funds.
  WACC = %debt × after-tax cost of debt + %equity × cost of equity.
- **How it works (the channel's three-part WACC series plus the beta segment of *Theory vs. Reality*):**
  - **Cost of debt.** Use what the company would pay to borrow **today**: the **yield to maturity** on
    its long-dated bonds, not the coupon. A bond issued in 2020 with a 3% coupon may now yield 7%,
    because its price fell when rates rose. Interest is tax-deductible, so multiply by (1 − t). Tax
    rate: 21% US federal plus 1–5% state and local, so ~**25%** is the standard assumption (use local
    rates for a foreign company). **7% × (1 − 25%) = 5.25%.**
  - **Cost of equity** isn't observable, so banks use **CAPM**: risk-free rate + levered beta × market
    risk premium. Risk-free = 10- or 20-year Treasury yield (for euro cash flows, the safest euro
    sovereign: the German Bund). **Beta** = how much the stock moves per 1% move in the market (β 1.25
    → +1.25% when the S&P rises 1%). **Market risk premium** comes from the Duff & Phelps (now Kroll)
    valuation handbook, typically **3–7%**, or from NYU's Aswath Damodaran, who publishes his free.
    Channel numbers: **4.25% + 1.25 × 5.5% = 11.125%.**
  - **Weighting** (illustration, not the channel's): at 30% debt / 70% equity,
    0.3 × 5.25% + 0.7 × 11.125% = 1.58% + 7.79% ≈ **9.4%**. The series ends with Kristen's joke that
    after all this the MD says the rate looks high and to use equity research's number.
  - **Which beta (Theory vs. Reality).** Academics say use a **forward-looking (predicted) beta**,
    because you are discounting future cash flows; Barra publishes them, but they are a black box.
    Sell-side bankers mostly use **historical** beta from Bloomberg's `BETA` screen: two years of weekly
    returns regressed against the S&P; the slope is **raw beta**, and **R²** says how much of the stock's
    movement the market explains. Most banks then use **adjusted beta = ⅔ × raw + ⅓ × 1.0** (Blume's
    observation that betas drift toward 1). Low R², a short trading history, or a private company →
    use peers: **unlever** each peer's beta to an asset beta (stripping out their leverage), take the
    mean or median, **relever** at your company's capital structure. (The standard formula, which the
    hosts reference but don't state: βL = βU × [1 + (1 − t) × D/E].)
- **Business significance:** The WACC is where judgment hides inside a "mechanical" valuation. The
  sell side standardizes inputs for liability reasons: a bank writing a fairness opinion may have to
  defend its beta under oath, and Kristen cites a figure that **75%** of acquisitions end in lawsuits.
  The buy side, not defending anything in court, can use R² and judgment to pick the beta that best
  describes the business. Same formula, different incentives.
- **Forces & impact:** Rates feed in twice (risk-free rate and cost of debt), so a rising-rate
  environment lowers every DCF value even if the business is unchanged. Tax policy feeds the debt leg
  (§4.6). Bloomberg access itself is a barrier: the hosts put a terminal at ~$28k a year.
- **With vs. without:** With a defensible WACC, two banks valuing the same company land in a similar
  range. Without standard inputs, the discount rate becomes the dial that delivers the client's number.
- **Applies when** the company's risk resembles its history or its peers'. **Breaks when** the capital
  structure is about to change (an LBO: the historical beta describes a different company), or when
  peers aren't really peers.
- **Channel example:** *Breaking Down the Cost of Equity in the WACC for a DCF*; *#1 Top Technical
  Finance Concept…WACC Part 3* (cost of debt); *DCF in Investment Banking: Theory vs. Reality*. Part 1
  (the weighting) has no transcript.
- **Counterpoint / check:** The 75% lawsuit figure fits *public-company* deals in the 2010s merger
  litigation wave, not acquisitions generally. The 3–7% MRP range is wide enough that the "source"
  barely constrains you: 3% vs. 7% on β 1.25 is a 5-point swing in cost of equity. And a 25% tax rate
  in the cost of debt assumes the interest is fully deductible, which §4.6's cap can deny.
- **Links:** [[bloomberg-terminal-instrumentation]] (`BETA` returns the regression, not just a
  number; why not to take the terminal's `WACC`); [[unit-06-whats-a-business-worth]].

### 4.5 Capital structure: how adding debt changes the WACC

- **What it is:** The interview question *"How does increasing debt impact the WACC?"* The channel's
  answer: debt is cheaper than equity, so adding it **lowers** the WACC (and raises value) up to a
  point, after which rising default risk makes both debt and equity more expensive and the WACC
  **rises**.
- **How it works (Kristen, *How Does Increasing Debt Impact the WACC*):**
  - **Why debt is cheaper.** Lenders are paid before shareholders and stand first in bankruptcy. She
    cites Fitch data: average recovery ~**76%** for first-lien loans, ~**40%** for bonds; equity in
    Bed Bath & Beyond was essentially wiped out. Lower risk, lower required return, plus the tax
    deduction.
  - **The deduction has limits** since the 2017 tax law (§4.6).
  - **Three theories.** *Trade-off/traditional*: an optimal mix exists. *Pecking order*: fund from
    retained earnings first, then debt, then new equity as a last resort, because issuing stock signals
    management thinks it's overvalued (she saw this on the converts desk). *Modigliani–Miller*: with no
    taxes, more debt raises the cost of equity exactly enough that value can't change; with taxes,
    debt adds value through the tax shield, which she reframes as a **transfer from taxpayers** to the
    company, not value creation.
  - **What MM leaves out:** bankruptcy costs; issuance costs (IPO fees ~**6–7%** vs. **12–40bp** on
    Meta's 2023 bond deal, per the underwriting discount she looked up); the discipline debt imposes;
    and the fact that borrowing costs rise in **steps** at rating thresholds, not smoothly.
  - **The converts-desk chart.** For CFOs she drew cost of capital (y) against the stock's expected
    five-year CAGR (x). Debt is a flat line: its cost doesn't depend on the share price. Equity is a 45°
    line: if your stock compounds 20% a year, that is what selling stock cost you. A convertible is debt
    below some growth rate and equity issued at a premium above it. Moral: if you expect your stock to
    do badly, issue equity; if you expect it to soar, issue debt, which is exactly the signal the
    pecking order says investors read.
  - **The commenter's error.** A viewer argued cost of equity is now *below* cost of debt for
    investment-grade firms, using earnings ÷ price. That's the **earnings yield** (1/PE), not a cost of
    equity: it ignores growth and payout. It is a legitimate **accretion/dilution** tool: at PE 20 the
    earnings yield is 5%, below a 5.25% after-tax cost of debt, so funding a deal with stock dilutes EPS
    less than funding it with debt. EPS is an accounting, equity-only metric; WACC is a valuation input.
- **Business significance:** Capital structure is a CFO's main financial lever and the whole premise of
  the LBO (§4.7). The EPS-vs-WACC confusion is common in boardrooms too: a deal can be accretive and
  still destroy value.
- **Forces & impact:** Tax rates and the interest cap set the size of the shield; rates and spreads set
  the cost of debt; the stock's valuation sets the attractiveness of equity (a high PE makes stock cheap
  currency for acquisitions, §4.22 on AOL/Time Warner).
- **With vs. without:** With a tax shield, leverage is subsidized and companies carry more debt than MM
  alone predicts. Without it (pure MM), financing is irrelevant and only operations create value.
- **Applies when** the firm has taxable profits to shield and stable cash flow. **Breaks when** distress
  costs bite: past the optimum, each turn of leverage adds more expected bankruptcy cost than shield.
- **Channel example:** *CRITICAL Investment Banking Interview Question: How Does Increasing Debt Impact
  the WACC*.
- **Counterpoint / corrections:** Kristen says Modigliani and Miller won the Nobel together in 1985;
  Modigliani won in 1985, Miller in 1990. She describes the 30%-of-EBITDA cap as running 2018–2021 with
  EBIT from 2022, while the channel's interest-deductibility short says 2018–2022 and 2023; the statute
  switched to EBIT for tax years beginning in **2022**. Her worked number is also off: 30% of a $150
  EBITDA is $45, not $50. The "debt is cheaper" line is right on a required-return basis but says
  nothing about *total* cost once distress risk is priced into equity.
- **Links:** [[canon-jensen-meckling-agency-theory]] (debt as discipline on managers);
  [[wss-capital-markets-ma]] (converts, accretion/dilution in live deals).

### 4.6 EBIT vs. EBITDA, and the interest-deductibility cap

- **What it is:** EBIT is operating profit. EBITDA adds back depreciation and amortization (D&A),
  non-cash charges, so it approximates operating cash flow and is always ≥ EBIT. US tax law (since
  2017) caps how much interest a company may deduct at **30% of a profit measure**, and *which*
  measure it is matters a lot to anyone running a leveraged balance sheet.
- **How it works (the short's numbers):** EBIT $100, D&A $50, so EBITDA $150; interest expense $100.
  - Pre-2018: deduct all $100 → taxable income **$0**.
  - EBITDA era (cap = 30% × EBITDA = $45): taxable = 100 − 45 = **$55**.
  - EBIT era (cap = 30% × EBIT = $30): taxable = 100 − 30 = **$70**.
  The channel dates the switch two ways: the short says 2018–2022 then 2023; Kristen's WACC video says
  2018–2021 then 2022. The statute moved to EBIT for tax years beginning in **2022**; the video is right.
  Same company, same debt, taxable income up 27% from a definitional change, while rates were rising
  so interest bills grew too. PE lobbied to restore D&A; the short cites a Treasury estimate of
  roughly **$180B** of added deficit over ten years.
- **Business significance:** The tax shield on interest is one of the reasons debt is "cheaper" than
  equity in the WACC (after-tax cost of debt = rate × (1 − t); the channel's 7% × 0.75 = 5.25%, §4.4). Cap the deduction and the effective
  cost of debt rises, the optimal leverage falls, and LBO returns fall. The cap hits capital-intensive,
  high-D&A businesses hardest under the EBIT version.
- **Forces & impact:** Tax policy and rates compound: higher coupons × lower cap = shrinking shield.
  The companion short (*Real Reason AI Companies are Rushing to Raise*) makes the mirror-image point
  on the asset side: 100% immediate expensing of capex pulls spending forward while the rule lasts.
- **With vs. without:** With an unlimited deduction, the tax code subsidizes leverage, and the
  marginal LBO is partly a tax trade. With a tight cap, deals must earn their return operationally.
- **Applies when** the borrower's interest exceeds the cap (high-leverage, high-rate). **Breaks when**
  the company has little taxable income anyway (losses, NOLs): the cap then costs nothing today.
- **Channel example:** *Private Equity LBO Modeling Basics: Changes to Interest Deductibility Rules*;
  *How Does Increasing Debt Impact the WACC* (same mechanics, 150/100 example).
- **Counterpoint / dated:** The short was recorded while the restoration was still being lobbied.
  The 2025 tax law (OBBBA) restored the EBITDA-based cap and 100% bonus depreciation — verify the
  current Section 163(j) text before using either figure. The short also frames this as PE's issue;
  the cap binds any leveraged company, including utilities and telecoms.
- **Links:** GLOSSARY "Leverage"; §4.4–4.5 (where the shield enters the WACC).

### 4.7 The LBO and the equity check

- **What it is:** A leveraged buyout buys a company with a small slice of sponsor equity and a large
  slice of debt that the target's own cash flow must service. The **equity check** (equity ÷ total
  price) is the dial: it decides how much the sponsor's return is magnified and how much room there
  is before lenders lose money.
- **How it works.** The channel's definition (*LBO in Under 3 Minutes*): buying a company financed
  mostly with debt, like buying an investment house with a mortgage, renovating it, and selling it.
  The sponsor raises value by growing sales and cutting costs, which lifts **EBITDA**; the company's
  cash flow pays down debt meanwhile; the sponsor cares about return on *its own* cash, not the rise in
  the house's price (worked numbers in §4.8). The live-deal version (hosts' figures, *Eerie
  Similarities…EA and 2007 TXU*):

  | | TXU (2007) | Electronic Arts (2025) |
  |---|---|---|
  | Sponsors | KKR, TPG, Goldman Sachs Capital Partners (club) | Silver Lake + Saudi PIF + Affinity Partners (co-invest) |
  | Enterprise value | ~$45B | ~$55B |
  | Sponsor equity | ~$8B (**~17–20%**) | ~$36B (**~65%**) |
  | Debt | ~$36B (24B senior secured loans syndicated; ~11B high yield via bridge) | ~$20B (≈$18B funded at close), **JPMorgan sole underwriter** |
  | Leverage (debt / LTM EBITDA) | ~8.5x | ~7.5x |
  | Purchase multiple | utility-low | **~20x EBITDA** |
  | Outcome | one of the largest bankruptcies ever | TBD |

  Why tech used to be un-LBO-able, in the hosts' arithmetic: if a company costs **20x** EBITDA and
  banks lend only **7–8x**, the other **12–13 turns (60–65%) must be equity**, but sponsors dislike
  going above ~30% equity because it dilutes returns. EA's 65% equity is that math forced through.
  Silver Lake's 2013 Dell buyout is the precedent they cite for tech LBOs working.
- **Business significance:** Lenders get paid first; equity absorbs the first loss. A thin check
  (TXU) means a modest fall in enterprise value wipes out the sponsor and hits lenders; a fat one
  (EA) protects banks but makes sponsor returns hard to hit (see §4.8). Value is created by EBITDA
  growth, debt paydown, and multiple expansion; it is *captured* by whoever holds the levered slice.
- **Forces & impact:** Credit appetite (spreads near all-time tights per the hosts), rates (Fed funds
  ~5.25% in 2007 vs. ~4–4.25% at recording), regulatory leverage guidance (~6x), and the multiple
  paid. Second-order: when purchase multiples outrun what lenders will fund, equity checks balloon
  and the "LBO" becomes a levered growth-equity deal.
- **With vs. without:** Without leverage, a sponsor buying at 20x earns roughly the business's
  unlevered return. With TXU-style leverage, small changes in value swing equity by multiples
  (energy prices fell, the equity was gone).
- **Applies when** cash flow is stable and predictable enough to service fixed claims. **Breaks when**
  cash flow is cyclical or commodity-linked (TXU: natural gas collapsed), or when the multiple paid
  needs growth the debt schedule can't wait for.
- **Channel example:** *LBO in Under 3 Minutes*; *Eerie Similarities Between Record Setting 2025 LBO (EA)
  and 2007 TXU LBO*; *Largest LBO EVER!!! Harbinger of another 2008?*
- **Counterpoint:** Kristen's heuristic that 8.5x leverage means "about 8.5 years to repay" uses
  EBITDA as if it were all free cash flow. After interest, tax, and capex, payback is far longer, and
  at TXU-era rates interest alone ate much of the EBITDA. The "under 6x" benchmark she attributes
  vaguely ("SEC?") is the 2013 US bank regulators' leveraged-lending guidance (Fed/OCC/FDIC), relaxed
  after 2018. And the PIF's motive (influence, not IRR, per the hosts) means EA's equity may accept
  returns a pure financial buyer wouldn't; the 65% check is partly a strategic subsidy.
- **Links:** [[tiger-sisters-private-capital-101]] (LBO intro, Toys "R" Us); GLOSSARY "LBO".

### 4.8 Paper LBO, IRR and the rule of 72

- **What it is:** A paper LBO is the mental-math version of a buyout model used in PE interviews:
  entry price, debt, exit price, and the resulting multiple of money (MOIC) and internal rate of
  return (IRR). The **rule of 72** says money doubles in ~72 ÷ r years at r% a year.
- **How it works (Kristen's numbers, *LBO in Under 3 Minutes*):**

  | | Entry | Exit (year 5) |
  |---|---|---|
  | EBITDA | $1.0M | $1.5M (sales up, costs cut) |
  | Multiple | 10x | 10x (held flat) |
  | Enterprise value | **$10M** | **$15M** |
  | Debt | $7M | $6M ($1M of cumulative cash flow repaid) |
  | Sponsor equity | **$3M** | **$9M** (15 − 6) |

  $3M → $9M is a **3.0x** in five years, which she calls a **25% IRR** (exactly: 3^(1/5) − 1 = 24.6%).
  Decompose the $6M equity gain: **$5M from EBITDA growth** at a constant multiple (83%) and **$1M from
  debt paydown** (17%); multiple expansion contributed nothing. Note the leverage effect: the business
  rose 50% in value; the equity tripled.
  *Rule-of-72 check (this note's):* a 3.0x is ~1.6 doublings; five years ÷ 1.6 ≈ 3.2 years per doubling;
  72 ÷ 3.2 ≈ **23%**, close to the true 24.6% (the rule understates at high rates). Shortcuts worth
  memorizing: 2.0x in 5 years ≈ 15%, 2.0x in 3 ≈ 26%, 3.0x in 5 ≈ 25%.
  *Applied to the hosts' EA figures (this note's arithmetic):* EV $55B at ~20x → EBITDA ≈ $2.75B; debt
  $20B; equity $36B. A 2.0x in five years needs exit equity $72B → EV $92B (debt held flat), so EBITDA
  must reach $4.6B at 20x (~11% a year) or ~$6.1B if the multiple falls to 15x (~17% a year). And
  leverage cuts both ways: on TXU's $8B equity / $45B EV, a 10% rise in EV is a 56% equity gain; on EA's
  $36B / $55B, only 15%. That is why a 65% check is a return problem: "harder to make the math work."
- **Business significance:** IRR is how sponsors are judged and paid (carry hurdles, §4.20). Paper-LBO
  math lets you sanity-check a pitch instantly: a sponsor promising 25% on a 65%-equity deal must be
  assuming heroic growth, multiple expansion, or a dividend recap.
- **Forces & impact:** Time is in the denominator. IRR rewards fast exits, which encourages early
  recaps and quick flips; MOIC rewards actual value created. Slow exit markets (the hosts' "exits are
  taking longer", continuation vehicles) crush IRR even when MOIC holds.
- **With vs. without:** Without leverage, Kristen's deal is $10M → $15M, a 1.5x (~8.4% IRR). With 70%
  debt, the same operating result is a 3.0x. Without IRR discipline, a 2x over ten years (~7%) looks
  like a win; with it, that's below the long-run equity market.
- **Applies when** cash flows are lumpy (in at entry, out at exit). **Breaks when** interim
  distributions and recycling make IRR gameable (early dividends inflate it), or when comparing deals
  of different durations, where MOIC and IRR disagree.
- **Channel example:** *LBO in Under 3 Minutes* (the worked deal); EA/TXU figures from *Eerie
  Similarities…*. The dedicated *Paper LBO* and *Rule of 72* shorts still have no transcript (§7).
- **Counterpoint:** Her example ignores fees (§4.9), interest cost, and taxes, and $1M of cash flow over
  five years is conservative for a business earning $1–1.5M of EBITDA a year; real debt paydown would
  usually be larger and returns higher. The flat 10x multiple is the honest assumption; sponsors'
  models often quietly assume expansion.
- **Links:** GLOSSARY "IRR"; [[tiger-sisters-private-capital-101]].

### 4.9 Sources & uses, cash-free debt-free, and rollover equity

- **What it is:** The **sources and uses table** is the one-page budget of a buyout: where every dollar
  comes from (debt tranches, sponsor equity, the target's own cash) and where it goes (buying the
  business, refinancing its debt, fees). **Cash-free, debt-free** is the convention for buying a
  private company: the buyer pays for the business as if it had no cash and no debt; the seller keeps
  its cash and pays off its own debt. **Rollover equity** is when sellers take part of their price as
  equity in the new private company instead of cash.
- **How it works (Kristen, *Cash Free Debt Free EXPLAINED*):** The house again: you buy the whole house;
  if the seller has a mortgage, it gets paid off at closing; a safe full of cash in the living room
  leaves with the seller.
  - *Private target (cash-free, debt-free).* **Uses:** purchase of the enterprise + transaction fees
    (bankers, lawyers) + financing fees (cost of raising the debt) + **minimum cash** the business needs
    to operate. **Sources:** senior debt + subordinated debt + sponsor equity.
  - *Public target.* **Uses:** buy every share, usually at a **premium** + **refinance** the existing
    debt + transaction and financing fees. There is no minimum-cash line: the cash comes with the shares
    you bought. So it shows up on the **sources** side as **excess cash**: everything on the balance
    sheet above what the business needs (she uses ~$10–25M as the keep-back) helps fund the deal,
    alongside senior debt, sub debt and sponsor equity.
  - The two framings reconcile to the same economics "99% of the time."
  **Rollover (Skechers, *Skechers' $9B deal…A Primer on Rollover Equity*):** 3G Capital offered
  shareholders either **$63 cash** or **$57 cash + one equity unit** in the private company (unlisted,
  untradeable). Rollover is capped at **20%** of the equity so 3G owns at least **80%**. Anyone electing
  the unit is implicitly valuing it above **$6**. Normally rollover is reserved for management; offering
  it to all holders lets those sitting on a ~20% loss (tariff uncertainty) keep upside instead of
  crystallizing it. Jen's analogy: selling your house to a flipper for $450k instead of $500k in
  exchange for a share of the $1M resale.
- **Business significance:** S&U is where the equity check (§4.7) is actually computed, and fees are
  visible as a cost the sponsor must earn back. Rollover reduces the cash the sponsor must raise,
  aligns sellers with the buyer, and signals the seller's confidence; for the buyer it is cheaper
  equity with no fee load.
- **Forces & impact:** In public-to-private deals, the premium is the price of control; excess cash
  on the target's balance sheet is free financing, which makes cash-rich public companies attractive
  targets. Going private also removes quarterly disclosure, which is the management-side reason
  (Skechers working through tariffs out of public view).
- **With vs. without:** Without the cash-free, debt-free convention, every private deal would argue over
  how much the seller's cash and debt are "worth"; with it, price is set on the business and the balance
  sheet is settled mechanically (in practice via a working-capital adjustment at close). Without
  rollover, sellers must choose between full exit and no deal.
- **Applies when** buying a whole business whose capital structure will be replaced. **Breaks when**
  "debt-like items" are contested (deferred revenue, unfunded pensions, accrued bonuses), which is where
  real-world CFDF disputes live, and for rollover when minority holders end up locked in a private
  company with no liquidity and no control.
- **Channel example:** *Cash Free Debt Free EXPLAINED*; *Skechers' $9B deal shows why in LBOs, cash isn't
  always king*.
- **Counterpoint:** The short treats the private-company case as the "cleanest" and skips the
  working-capital peg and debt-like-item fights that actually consume the negotiation. On Skechers, the
  hosts frame the unit as upside participation; it is also illiquid, subordinated to a large new debt
  load, and controlled by 3G.
- **Links:** [[tiger-sisters-private-capital-101]] (LBO structure); §4.2 (EV: what the "uses" buy).

### 4.10 Who funds the debt: syndication → CLO → private credit

- **What it is:** A bank that "underwrites" an LBO commits to provide the money, but traditionally it
  doesn't keep it. It **syndicates** term loans to other banks and institutional buyers (the broadly
  syndicated loan, BSL, market), bridges the high-yield bonds until they can be sold, and sells loan
  pieces into **CLOs** (collateralized loan obligations: pools of senior secured loans financed by
  tranches of debt plus an equity slice). Private credit is the alternative: one lender, holding.
- **How it works:** TXU: Citi, JPMorgan, Goldman structured ~$24B of senior secured loans and
  syndicated them across Credit Suisse, Morgan Stanley and others; ~$11B was to be high-yield bonds,
  bridged by the banks. CLO managers bought loans first into a bank-financed **warehouse**, then the
  CLO priced and took the loans off bank balance sheets. Jen's analogy: a car maker stockpiling parts
  for orders that may be cancelled; the bank earns the markup and carry, until buyers vanish and it is
  left with "8,000 steering wheels" (2007–08, hung deals, fire sales). EA: JPMorgan alone committed
  **$20B**, the largest single-bank buyout underwrite ever per the hosts, backed by ~**$50B** of its
  own direct-lending capacity as a fallback if it can't syndicate.
- **Business significance:** Distribution is what lets a bank lend again; Jen's point is that
  securitization exists so lenders don't "face" one borrower forever. Fees accrue at each handoff
  (underwriting, warehouse carry, CLO structuring). Private credit charges more (one lender, more
  customization) but offers certainty and privacy.
- **Forces & impact:** Rates and spreads (floating-rate loans get cheaper as rates fall), bank capital
  rules, and investor demand for yield. When demand is strong, concentration feels safe; when it
  turns, concentrated holders are forced sellers.
- **With vs. without:** Without syndication, the largest deals can't be done by any one bank, and each
  bank carries undiversified risk. With it, risk is spread, but in 2007 it was spread into buyers who
  were simultaneously exposed to mortgage CDOs, so they all disappeared at once.
- **Applies when** the risk can be sold to diversified holders. **Breaks when** the distribution
  channel freezes (2007–08) or when the originator chooses to hold (EA), concentrating risk in one
  balance sheet.
- **Channel example:** *Eerie Similarities…*; *Largest LBO EVER!!!* (Part 2 on what "underwriting"
  means is in the missing short *Largest Debt Commitment in History for LBO by ONE BANK*).
- **Counterpoint:** Kristen defends CLOs hard: underlying loans are senior secured with covenants,
  ~70c recovery, managers often hold the equity tranche, and corporate defaults were modest even in
  2008. That's largely right historically, but she concedes covenant protection has eroded
  (covenant-lite, incurrence-only tests, §4.12), which weakens exactly the protection she relies on.
  Jen's counter is the fair one: a private-credit book can't be checked from outside ("okay, you say
  so").
- **Links:** GLOSSARY "CLO"; [[market-structure-24-5-institutional-response]].

### 4.11 Club deals vs. co-invest

- **What it is:** A **club deal** pools several PE firms as co-sponsors. A **co-invest** has one lead
  sponsor that runs the business while its limited partners (LPs) or strategic investors put extra
  equity directly into the deal alongside the fund.
- **How it works:** TXU was a classic club (KKR + TPG + GSCP, $8B). EA looks like a club but the hosts
  read it as co-invest: Silver Lake is the operator; PIF (>$1T AUM) supplies most of the $36B;
  Affinity Partners (~$5B AUM, founded 2021) is the puzzle. Even a large sponsor fund (~$25B, the
  rough ceiling they cite) won't put $36B, or even a big fraction of its fund, into one deal. The LP
  gets exposure **without paying 2-and-20** on that capital.
- **Business significance:** Clubs blurred accountability; the hosts point to Caesars (Apollo and
  TPG), where sponsors fought over direction and litigation followed. Co-invest keeps one decision
  maker and gives big LPs cheaper exposure, which is why it displaced clubs.
- **Forces & impact:** Sovereign wealth with non-financial goals (PIF's image-building, LIV Golf) is
  now a major equity source; its return hurdle may be lower, which lets prices rise.
- **With vs. without:** Without co-invest, $50B+ buyouts require multiple sponsors and their
  governance friction; with it, one sponsor can do a deal several times its own appetite.
- **Applies when** a trusted operator and deep-pocketed LPs coexist. **Breaks when** the co-investor's
  goals diverge (influence vs. IRR), or the lead gets preferential economics that misalign it with
  co-investors (the hosts speculate Silver Lake may get a sweetened structure).
- **Channel example:** *Eerie Similarities…*
- **Counterpoint:** The Affinity/PIF roles are speculation on air ("according to ChatGPT" for the AUM
  figure). Treat the motive analysis as opinion.
- **Links:** [[tiger-sisters-wealth-mechanics]] (club deals in family-office context).

### 4.12 Collateral, covenants, recovery, and the bankruptcy chapters

- **What it is:** Secured lenders lend against **collateral** (receivables, inventory, buildings) and
  protect themselves with **covenants**: *maintenance* covenants are tested every quarter (e.g.,
  leverage below X), *incurrence* covenants only bite when the borrower takes an action (new debt,
  dividends). In distress, **Chapter 11** reorganizes the company so it continues; **Chapter 7**
  liquidates it and pays lenders from the proceeds.
- **How it works:** First Brands (auto parts) filed Chapter 11 on Sept 28 after failing to refinance
  ~**$6B** of maturing debt (the transcript says "$6 million" once, then "$6 billion"; billions is
  right). Investigators found roughly **$2.3B of assets** that "evaporated": receivables apparently
  pledged to more than one financier (invoice factoring done off the books, "hidden factoring"),
  plus off-balance-sheet liabilities, for **~$10–11B** of total liabilities. Exposed: Jefferies'
  Point Bonita private-credit fund and UBS O'Connor (reportedly **~30%** of one portfolio). Tricolor
  (subprime auto lending) went straight to Chapter 7. The same short set: Bed Bath & Beyond liquidated
  in bankruptcy, sold its brand to Overstock, and the renamed Overstock is now bidding **$150M** for The
  Container Store; the "company" is a brand bought at auction, not a revived business.
- **Business significance:** Collateral is why a CLO model assumes **~70c on the dollar** recovery
  for senior loans vs. ~0 for equity. But collateral is a claim on a document; if the same invoice
  backs three loans, two lenders hold nothing.
- **Forces & impact:** In a yield-hungry market, lenders trade protections for spread (maintenance →
  incurrence), so problems surface later. Kristen: fraud is easy to hide when things go well and
  hard when they don't. Jen: private credit is "designed in a way that obfuscates stress" because a
  single lender can quietly renegotiate.
- **With vs. without:** With maintenance covenants, a lender sees trouble at the first bad quarter and
  can renegotiate from strength. Without them, the first signal is a missed refinancing, when the
  collateral may already be gone.
- **Applies when** collateral is verifiable and uniquely pledged. **Breaks when** receivables are
  double-pledged, off-balance-sheet obligations are hidden, or covenants are light enough that no one
  is looking.
- **Channel example:** *First Brands Bankruptcy, Gold at Record Highs & Banking Analyst Suing Over
  Sleep*; *How can Bed Bath & Beyond…bid $150M for The Container Store?*
- **Counterpoint:** Both hosts say outright they're not distressed experts. "History rhymes" with
  2007 is suggestive; First Brands is so far an alleged fraud, not evidence of a systemic private
  credit failure. Two auto names don't make a cycle.
- **Links:** [[trading-floor-mechanics]] (risk vs. client split); GLOSSARY "CLO".

### 4.13 Shorting bonds, repo haircuts, and settlement fails

- **What it is:** To short a bond you borrow it (via a reverse repo with a dealer), sell it, and hope
  to buy it back cheaper. The dealer lends against collateral with a **haircut** sized to the client's
  creditworthiness, e.g., lend $95, $90, or $80 of bonds per $100. **DV01** is the dollar change in a
  position per one-basis-point move in yield.
- **How it works:** In Feb 2020 a small fund (the hosts call it a parody name; Black Brook) sold short
  **$2.6B** of 30-year Treasuries, "spraying the street" in clips across several dealers so none saw
  the full size. Jen's DV01: ~**$4.2M per bp**. The fund never sourced the borrow, failed to deliver,
  and COVID triggered a rally: 30-year yields fell from ~3.7% to ~3.2%, about **50bp**. 50 × $4.2M ≈
  **$210M** (the reported street loss was **~$250M**), borne by dealers who had hedged by going short
  themselves and then were never delivered the bonds. "11,000-to-1": $2.6B ÷ 11,000 ≈ $240k of
  actual capital.
- **Business significance:** Dealers make markets on trust and post-trade controls. The salesperson
  doesn't check a BlackRock's balance sheet per trade; onboarding, credit limits and settlement
  monitoring do that "behind the scenes." When those controls miss, the dealer is the one who is
  short.
- **Forces & impact:** Electronic trading and fragmented execution make "spraying" easy and the
  aggregate invisible. Settlement (T+1) gives a one-day window where an unfunded sale looks normal.
- **With vs. without:** With haircuts sized to credit, a client can't take more risk than its capital
  supports; without enforcement, leverage is whatever the counterparty forgets to check.
- **Applies when** controls are applied at onboarding and settlement. **Breaks when** a client splits
  orders across dealers and no one aggregates exposure; when an exogenous shock moves the market
  before the fail is resolved.
- **Channel example:** *First Brands Bankruptcy…* (the "Ferrari-loving trader" segment).
- **Counterpoint:** The transcript gives the fund's size as "less than $250 million" and "$2.5
  million" in different breaths; the 11,000:1 headline only works with the smaller figure. Jen also
  frames the story as boring incompetence; the more interesting lesson is that four or five dealers'
  controls each passed a trade that was only dangerous in aggregate.
- **Links:** [[trading-floor-mechanics]] (risk controllers, middle office); [[market-structure-24-5-trading]].

### 4.14 Treasury auctions

- **What it is:** The Treasury sells new debt on a fixed calendar through a **single-price (Dutch)
  auction**: everyone who is filled pays the same clearing yield, set by the last bid needed to fill
  the size.
- **How it works:** Before the auction, the new bond trades **when-issued** (WI) as a yield spread to
  the current on-the-run, so the market prices the expected clearing level. Bidders: **direct**
  (needs a Treasury account), **indirect** (often via a bank), and **dealers** (the remainder).
  Non-competitive bids max out at **$10M** (retail); a competitive bidder can take up to **35%** of the
  auction. If $25B of 10s are offered, the yield of the bid that fills the 25th billion clears the
  whole issue. Bids close 12:59, results just after 1pm. Clears **above** the WI yield → "tailed"
  (weak); **at** → "on the screws"; **below** → "stopped through" (strong).
- **Business significance:** Auctions are scheduled supply shocks to the world's benchmark asset; a
  tail can trigger a sell-off, a stop-through a scramble rally. Dealers are obliged to absorb what
  others don't, which ties dealer balance sheets to fiscal deficits.
- **Forces & impact:** Deficit size sets auction sizes; foreign and domestic demand sets the clearing
  yield. The paired short on mortgage rates adds the transmission: the Fed sets overnight rates, but
  30-year mortgages price off the long end, which the market sets (and which QE can push down). The
  administration's directive for Fannie/Freddie to buy **$200B** of MBS is small against a **~$9T**
  agency MBS market; Kristen calls it a signal more than a lever.
- **With vs. without:** A discriminatory auction (each pays their own bid) pushes bidders to shade
  bids and favors insiders; the single price draws more aggressive, honest bidding.
- **Applies when** the market is deep and the calendar predictable. **Breaks when** dealer balance
  sheets are constrained, so tails widen.
- **Channel example:** *The best explanation of Treasury auctions you'll find on the internet*;
  *Who Controls Mortgage Rates?*
- **Counterpoint:** The rates side is covered more deeply in the rates-macro cluster; this is the
  minimum a deal person needs.
- **Links:** [[market-structure-24-5-institutional-response]]; [[bloomberg-terminal-instrumentation]].

### 4.15 IPO pricing, the pop, lockups, and the direct listing

- **What it is:** In an IPO, underwriting banks build a book of investor demand, set a price, buy
  the shares from the issuer and resell them. **Primary** shares raise money for the company;
  **secondary** shares let existing holders sell. A **direct listing** skips the underwritten offering:
  existing shares simply begin trading, priced by an opening auction.
- **How it works (Figma short):** **12.5M primary + 24.5M secondary = 37M** shares sold, against
  **585M** fully diluted shares (~**6%** float, ignoring the greenshoe). Priced at **$33** (→ **$19.3B**
  valuation). Banks aim for a ~**15%** first-day pop, i.e., price ~15% below expected trading value.
  Figma closed day one near **$115**: +$82/share × 37M ≈ **$3B** that went to the allocated buyers
  instead of Figma and its selling VCs (proceeds were ~$1.2B). Holders who didn't sell enjoy the
  markup but face a **~180-day lockup**. Spotify (2018) instead did a direct listing: no new shares,
  secondary only; it had a public investor day anyone could watch; opening was delayed about half a day
  while the exchange found the clearing price. Its SVP's critique of IPOs: allocations favor bank
  relationships, middlemen arbitrage the price, retail is shut out.
- **Business significance:** The pop is a cost of capital paid to allocated investors (largely the
  bank's best clients). Banks benefit both ways: fees from the issuer and goodwill from the buyers
  who get the cheap shares.
- **Forces & impact:** Banks are paid by the issuer but repeat-play with buyers, so they lean toward
  underpricing. Brand-strong companies that don't need cash (Spotify) can skip them. The hosts also
  note the SEC review step means a government shutdown can stall the IPO pipeline.
- **With vs. without:** Without the underwritten process, price discovery happens live, which works
  for well-known names and is risky for obscure ones; the company raises no new money in a pure
  direct listing.
- **Applies when** there's real uncertainty about demand (bookbuilding reveals it). **Breaks when**
  demand is so lopsided that the "discount" becomes a 250% gift.
- **Channel example:** *Why Figma's stock price tripling the day of its IPO [is] a BAD THING*; *How
  Spotify Turned a Free Product into a $100 Billion Company*.
- **Counterpoint:** Figma's sellers sold ~6% of the company; the pop re-marked the other ~94% at ~3.5x
  overnight, which helps follow-on raises and employee equity. And Spotify's SVP is describing his
  own company's choice; few have copied it, which suggests the underwritten IPO solves problems
  (stabilization, a committed buyer base) he doesn't mention.
- **Links:** [[sec-filing-intelligence]] (S-1 reading).

### 4.16 Private marks and related-party valuation

- **What it is:** A private company has no market price; its "valuation" is the last price at which
  someone bought shares. If an interested party sets that price, the mark is only as good as the
  independence of the buyer.
- **How it works:** X raised equity at a **$33B** valuation weeks before xAI bought it at the same
  figure in stock. Musk participated in that round and controls both companies, so he helped set the
  price at which one of his companies bought the other. Outside xAI shareholders bear the
  consequence of that exchange ratio. Same pattern in private credit: loans "marked at par" by the
  manager who earns fees on the NAV (Jen's "it's marked par, we say it is").
- **Business significance:** Fees, carry, and fund performance are computed on marks. Citi's head of
  research describes the information gap: privates have no audited quarterly filings, and coverage
  is moving there anyway because the investable universe has "de-equitized" (fewer listed stocks,
  more value in a handful of megacaps and in large private unicorns).
- **Forces & impact:** Longer private holding periods → more value sits at marks → more pressure to
  democratize access to private assets (retail products), which raises the cost of a bad mark.
- **With vs. without:** With independent price setters and audits, the mark approximates a market.
  Without them, it can be the controlling party's number.
- **Applies when** there's a real arm's-length round. **Breaks when** insiders lead the round or the
  manager marks its own book.
- **Channel example:** *The Truth About the $33Bn Elon Musk's xAI Paid for X*; *Citi's Global Head of
  Research…Covering Private Companies*.
- **Counterpoint:** The short says "who cares" if one person owns most of both. The answer is the
  minority holders, and they presumably priced the governance risk when they invested.
- **Links:** [[canon-akerlof-market-for-lemons]]; [[tiger-sisters-private-capital-101]].

### 4.17 Sell-side research economics

- **What it is:** Sell-side analysts build forecasts and ratings, and sell two things: insight to
  investors ("where is consensus wrong?") and access/judgment to companies. They work behind
  information barriers from bankers.
- **How it works (Lucy Baldwin, Citi):** ~**800** research staff cover ~**3,500** listed equities
  plus rates, FX, commodities, credit (as baskets, not single names), and lately crypto and large
  private companies. Rule: once the bank is **mandated** on a transaction, its analysts stop
  publishing on that company. Her claim: commodity coverage is now table stakes (an LLM can produce
  it); value has shifted to star analysts that C-suites call. Research → banking used to be a
  common senior path; regulation made it harder; juniors now exit directly to PE and, in 2024–25,
  private credit.
- **Business significance:** Research is a cost center that supports trading flow and banking
  relationships. Regulation (the 2003 Global Settlement in the US; MiFID II unbundling in Europe) cut
  the direct link between research and banking fees, which is why coverage shrank and why the
  survivors push into new areas.
- **Forces & impact:** AI raises capacity per analyst; de-equitization shrinks the public universe;
  the growth of sponsors (PE/private credit owning IPO candidates) changes who research serves.
- **With vs. without:** With independent research, investors get a dissenting voice on company
  narratives. Without the barrier, research becomes marketing for the bank's deals (the pre-2003
  problem).
- **Applies when** analysts can publish freely. **Breaks when** the bank is mandated (silence) or when
  coverage of private targets drifts into pre-IPO marketing.
- **Channel example:** *Citi's Global Head of Research…*
- **Counterpoint:** A head of research arguing the value of human analysts is talking her book. She
  dismisses the conflict in covering private IPO candidates as "easily mitigated." The pre-2003
  history suggests otherwise.
- **Links:** [[trading-floor-mechanics]] §3c (buy-side vs. sell-side research), §4 (information
  barriers).

### 4.18 Elite boutique vs. bulge bracket: two business models for selling advice

- **What it is:** A **bulge bracket** is a universal bank (Morgan Stanley, Goldman, JPMorgan) that sells
  advice *and* lends, underwrites, trades and holds a balance sheet. An **elite boutique** (Greenhill,
  Lazard, Evercore, Centerview) sells only advice (M&A, restructuring) and has no balance sheet.
- **How it works (Scott Bok, Greenhill chairman, *Elite Boutique vs. Bulge Bracket*):**
  - *History.* Charging for M&A advice is recent: Wall Street once earned its money underwriting and gave
    merger advice away; Bob Greenhill built Morgan Stanley's M&A department with about four people. In
    the 1980s–90s consolidation (Glass-Steagall erosion; the British merchant banks absorbed; tech
    specialists like Robertson Stephens and Alex. Brown bought) left roughly **nine** firms owning
    investment banking. Boutiques were the backlash: clients began to doubt that a bank selling them
    loans, bonds and hedges was purely on their side. The boutique sells **conflict-free advice**. Bok's
    mentor's image of advice inside a trading firm: the hot dog stand in front of the casino, which has a
    bad day whenever the traders do.
  - *Risk.* With no balance sheet or trading book, the firm was "our phones and our desks": the worst case
    is less work, not losses. Scale matters for firms holding volatile assets or deposits (he cites SVB),
    not for advisers.
  - *Diversifying within advice.* Greenhill added **restructuring in 2001** as a countercyclical hedge
    (bankruptcy work peaks when M&A dies); most boutiques followed. Geography is the other hedge
    (Australia held up while Europe's banks sank after 2008).
  - *Greenhill's IPO.* Founded 1996, ~$100M revenue for several years; IPO in 2004 at ~100 people, ~**16x**
    oversubscribed, ~**$500M** value at the end of day one, ~**$2B** within 18 months for ~125 people.
    Lazard and Evercore listed in the next two years. During 2008 its stock hit an all-time high the week
    Lehman failed: "best house in a bad neighborhood."
  - *The reversal.* After 25 years many firms looked like Greenhill; Bok sold to **Mizuho** (2023) because
    inside a multi-product bank, trading does well in volatility while M&A clients freeze, which smooths
    the cycle. The episode gives no price (outside sources: ~$550M including debt).
  - *Today.* The industry has "refragmented": elite boutiques, single-industry or single-country
    specialists, and foreign banks (Mizuho, RBC, Nomura) building US advisory.
- **Business significance:** The two models capture value differently. The bulge bracket can bundle a
  financing commitment with the advice (JPMorgan's $20B on EA, §4.10), which wins mandates and earns
  fees on several products, at the cost of conflicts and capital. The boutique earns on reputation and
  senior attention alone, so its pitch is independence, and its value is concentrated in a few rainmakers.
  For juniors: entry pay is nearly identical (§4.22: boutiques maybe ~$10k more), but the experience
  differs. Bok's test is to join a "Navy SEALs" unit, not a "General Motors factory," which can be a
  small group inside a mega-bank, and never to choose on brand or an extra $5,000 of base.
- **Forces & impact:** M&A cycles hit pure advisers hardest; restructuring and geography are their only
  hedges. Regulation since 2008 (bank capital rules Bok calls "generals fighting the last war") raised
  the cost of the universal model and helped boutiques win share. The cycle can also run the other way:
  public boutiques face quarterly scrutiny, and the halving of US listed companies (take-privates,
  mergers) shrinks the client base.
- **With vs. without:** Without boutiques, every major board's adviser would also want to lend to,
  underwrite and trade against it. With them, boards hire a boutique for the opinion and a bulge bracket
  for the money, which is now common on large deals.
- **Applies when** a client values independence and senior attention (boards, special committees,
  restructurings). **Breaks when** the deal needs a financing commitment, or a downturn hits a firm with
  no other revenue.
- **Channel example:** *Elite Boutique vs. Bulge Bracket Investment Banks feat. Greenhill Chairman, Scott
  Bok*.
- **Counterpoint:** Bok sold his boutique into a bank, which is itself a verdict on the pure model at
  subscale. The episode never covers fees (retainer vs. success), deal-size bands, or analyst pay, so the
  title promises more comparison than it delivers. "Conflict-free" is also relative: boutiques have
  conflicts of their own (success fees reward getting *a* deal done).
- **Links:** [[professional-services-leverage]] (partner-driven firms); [[trading-floor-mechanics]]
  (the trading side of the universal bank); [[canon-jensen-meckling-agency-theory]] (adviser incentives).

### 4.19 Banker and buy-side comp structure

- **What it is:** Wall Street pay = **base salary** (fixed, bi-weekly, roughly standardized across firms
  and cities at junior levels) + **bonus** (performance-based, discretionary, and the part that grows
  with seniority). Senior bonuses are partly **deferred** and subject to **clawback**.
- **How it works (Buyside Hub data via High Yield Harry; hosts read averages):**

  | Level | IB base | IB bonus | IB total (avg / 75th pct) | PE/private credit total (avg / 75th) |
  |---|---|---|---|---|
  | Analyst | $111k | $52k | $163k / $185k | $165k / $191k |
  | Senior analyst (3rd yr) | — | — | $202k / $217.5k | $182.5k / $196k |
  | Associate | $165k | $114k | $280k / $328k | $251k / $291k |
  | Senior associate | — | — | — / $430k | $309k / ~$350k |
  | VP | $257k | $150k | $409k / $500k | $423k / $485k (ex-carry) |

  Hosts' starting base in 2006–07: ~$55–60k. Bottom-bucket juniors may get a "donut" (zero bonus, a
  signal to leave without severance) or more often **$15–25k**. MDs: base perhaps ~$200k, total in
  the millions; cash comp often >$1M.
  **Deferral:** a VP's ~$500k bonus might pay **one-third cash, one-third deferred cash** (invested but
  inaccessible), **one-third deferred stock** vesting over **3–5 years**. Unvested deferrals are
  forfeited on leaving, so a new employer must "buy out" the deferred balance. By ~30 that balance is
  large enough to make you an expensive hire, hence the "last chopper out" window. Jefferies is cited
  for clawback periods.
  **EU bonus cap** (*How a law capping Wall Street bonuses RAISED their pay*): post-crisis rules limited
  bonuses to 2x base (1x without shareholder approval); European banks raised bases to stay
  competitive, so total pay held, fixed pay rose, and a bad actor now got paid *more* for doing
  nothing, because the base is guaranteed. Jen's verdict: a rule meant to rein in risk-takers ended up
  guaranteeing their pay.
  **How bonuses are set and told (Industry S1E6, S1E7, S1E3 recaps):** numbers are fixed in December
  and paid January–March depending on the firm. Analysts start in July, so their first payout is a
  pro-rated **stub**, and they stay on a summer cycle for about two years before a stub catches them
  up to the winter cycle at promotion (Jen's 2008 Barclays stub was "little more than a cup of
  coffee"). Analyst bonuses are **tiered** (Kristen guesses ~five buckets), and juniors now learn the
  tiers through anonymous polls. Senior variable pay is a function of personal, desk, division and firm
  results against the desk **budget**; the range widens from ~$200k to $2M+ with seniority. "Don't talk
  about your comp" survives as policy, and the hosts call it a control tool: without comparisons you
  can't tell you're underpaid. Kristen calls VP pay of ~$500k "public domain." Clawbacks at banks are
  rare in practice: deferred pay is forfeited if you're fired for cause, kept if you resign; the
  realistic punishment is a donut next year. MDs may not top up juniors from their own pockets; excess
  pay must come from the pool. Hedge funds are different: clawbacks can be contractual (Jen's
  illustration: paid $80M, asked for $79M back after a down year).
  **Guarantees when switching (Industry S2E7):** a trader moving firms typically asks for a **two-year
  guarantee**; all-cash with no deferral is "not happening" today. A guarantee borrows from future pay:
  when it expires you are almost always "paid down," because the new bank stretched to hire you.
  Battlefield promotions (more responsibility without the title or pay) are why switching is often the
  only way to reset comp.
- **Business significance:** Deferral aligns senior pay with multi-year outcomes and creates
  retention ("golden" or, for mid-levels, "silver handcuffs"). Bonus pools flex with revenue, so the
  bank's cost base flexes too. Desks cross-subsidize: a star on a bad-year desk is paid less, and a
  weak performer on a good-year desk is carried.
- **Forces & impact:** Deal volume (2025 was "the year of the banker": IPOs and M&A back), buy-side
  fundraising (tight, so the sell side is more competitive than in the ZIRP years), regulation.
  Second-order: buy-side comp at junior levels is roughly *equal to or below* IB before carry, which
  undercuts the old "exit ASAP" logic.
- **With vs. without:** Without deferral, a trader can take risk that pays this year and blows up
  next, then leave; clawbacks plus deferral make him wear the tail. Without a bonus cap, pay flexes
  with performance; the cap's unintended effect was guaranteed pay, the opposite of its aim.
- **Applies when** comparing like-for-like (an MBA associate vs. a first-year big-law lawyer at
  ~$250–400k, per the hosts). **Breaks when** carry enters (§4.20) or for top-bucket outliers.
- **Channel example:** *EXACTLY How Much Investment Bankers & Private Equity Get Paid feat. High Yield
  Harry*; *Why I walked away from over $200k of my bonus at Morgan Stanley*; *How a law capping Wall
  Street bonuses RAISED their pay*; *Industry S1E6 "Nutcracker"…Bonus Season*; *Industry S1E7 "Pre Crisis
  Activity"…Bonus Clawbacks*; *Industry S2E7 "Lone Wolf and Cub"…How Investment Bankers Get Paid*.
- **Counterpoint / dated:** Survey data is self-reported. The hosts flag the VP figure as low versus
  their anecdotal S&T experience (+$100–200k). The UK scrapped the cap in late 2023; the EU's remains.
  The hosts' framing ("bonus is a misnomer, it's performance pay") is accurate but also defends
  their old industry from a public perception problem. In S2E7 the team-pricing arithmetic doesn't
  close (half of 4 × $1M is $2M, not the "$4–8M" Jen lands on). Jen's FTC non-compete point (S1E7) is
  dated: the 2024 ban was struck down and later abandoned. TARP is the Troubled Asset *Relief*
  Program, not "Recovery" (S1E7).
- **Links:** [[canon-jensen-meckling-agency-theory]]; [[professional-services-leverage]] (fixed
  associate pay at law firms, the comparison case).

### 4.20 Carry economics by fund size

- **What it is:** PE and credit funds charge **"2 and 20"**: ~2% a year of assets as a management fee
  and ~20% of profits as **carried interest** (carry), usually after a return hurdle. Individuals get
  slices of the carry pool, quoted in basis points (bips) of the fund's carry, vesting over ~5 years.
- **How it works (hosts' arithmetic):** A **$10B** fund earns **$200M** a year in fees; a **$1B** fund
  earns **$20M**. If each doubles its money, carry is **$2B** vs. **$200M**. Buyside Hub: at
  ~$4–5B funds, mid-levels get ~**20–40bps** of carry; at ~$8–10B, ~**30–50bps** starting at senior
  associate; at **$200–500M** lower-middle-market funds, **100–500bps** (1–5%), and a junior associate
  may get a point or more. Megafunds (Apollo, Thoma Bravo) give associates **no** carry. Sub-$5B funds
  may add **$50–500k** of other equity incentives. Hours: private credit ~55–60/wk, PE ~65–70,
  megafund PE can match banking.
- **Business significance:** 100% of zero is zero (Jen). A big carry percentage at a small fund can
  be worth less than a small slice at a megafund, and carry is paid years later if at all. Small funds
  substitute carry for cash because they can't match the fee-funded salaries.
- **Forces & impact:** Exit slowdowns and continuation vehicles stretch the carry timeline; fundraising
  difficulty makes senior seats sticky ("top-heavy"), so juniors stall. Private credit comp has
  plateaued, per Harry, as seats fill with PE refugees.
- **With vs. without:** Without carry, buy-side pay is IB-like or lower. With it, the payoff is a
  call option on fund performance, which is the real reason to move.
- **Applies when** the fund performs and you stay through vesting. **Breaks when** the fund
  underperforms the hurdle, or you leave before vesting.
- **Channel example:** *EXACTLY How Much Investment Bankers & Private Equity Get Paid*.
- **Counterpoint:** Harry runs a comp-data platform; "you can go to the table on carry" is also his
  product's pitch. The 2x-in-a-period illustration ignores hurdles and the time value of carry.
- **Links:** [[tiger-sisters-private-capital-101]] (2 and 20); [[harlem-capital-vc-insights]]
  (European vs. American waterfalls, clawbacks to LPs).

### 4.21 The career pipeline: 2+2+2, on-cycle recruiting, and the MBA

- **What it is:** The traditional elite path was **2 years** as an IB analyst → **2 years** at a PE
  firm → **2 years** of MBA → back to PE. **On-cycle recruiting** is the compressed, megafund-led window
  in which PE firms interview first-year analysts for associate jobs starting ~18 months out.
- **How it works:** In 2006–07 on-cycle came about six months into the job, after a first review.
  Game theory pushed it earlier ("if Apollo does it, we must"), until firms interviewed analysts
  before they'd started work, effectively hiring on school pedigree. JPMorgan responded by requiring
  new analysts to attest they wouldn't recruit elsewhere in their first months. PE firms began hiring
  straight from undergrad to stop paying banks' recruiting premium (banks spend heavily to train
  analysts), and per the hosts some are unhappy with results. Banks now try to *keep* analysts. The MBA
  as a career-switch tool: High Yield Harry calls it "LBOing yourself" (borrowing to buy an option on
  a better career), worth it mainly if you lack the network.
  **The undergrad funnel (*From Intern to Offer*):** applications for a junior-summer internship now
  open as early as January of sophomore year, a rolling ~16–18-month window; sophomore internships
  almost never convert, and the junior internship is the real 10-week interview. Offers are a ranking
  market: at a ~150-person bulge-bracket S&T program, interns rank desks and desks rank interns, and
  "if no desk ranks you first" an offer is hard to justify. Programs hire more summers than full-time
  seats, then attrition (firings, quits, visa failures) reopens seats for the senior-fall cycle. Offers
  are rarely rescinded, Jen argues, because juniors are cheap options: firms "overhire and overfire"
  (Lehman honored incoming offers through bankruptcy). Training then takes 2–3 months, including a
  two-week modeling bootcamp (Mindy Kaling reaction episode); interview technicals have inflated from
  "how do you value a company" (Kristen, 2007) to deferred taxes. The PE conveyor (sophomore PE,
  junior IB, PE offer starting two years later) selects on resumes, not observed work; Kristen on her
  own early hire: "on paper though, I looked great."
  **Other doors:** alumni outreach beats cold LinkedIn (*Our Number One Tip*); the MBA is the main reset
  for career switchers because associate classes have hundreds of seats built for non-finance people;
  sector expertise can enter via equity research. Licensing: the **SIE** ($80, no sponsor needed, often
  expected before day one), then Series 7/79/63; the **CFA** (three levels, ~40% average Level I pass
  rate, ~$1,000 registration) fits asset management and S&T better than IBD, where modeling is a
  footnote (*CFA for Investment Banking*). S&T is more a career than a two-year program: banks barely
  recruit S&T from MBAs, and it has become a talent farm for hedge funds, where a senior bank trader's
  "couple million" can become tens of millions. Trading interviews test thinking under adverse
  selection: a counterparty offering you a bet is itself information (*Sneak peek into the interview
  for one of Wall Street's highest-paid jobs*).
- **Business significance:** IB is PE's outsourced training and screening program; on-cycle is PE
  free-riding on that screen. Deferral (§4.19) makes the window close around 30.
- **Forces & impact:** Hours (Centerview analyst lawsuit over a sleep accommodation, not dismissed;
  the hosts doubt it changes practice), AI threat to junior work, and buy-side fundraising.
- **With vs. without:** Without the analyst program, PE would have to train and screen itself (it's
  trying); without on-cycle, PE would hire on observed performance instead of pedigree.
- **Applies when** buy-side seats are plentiful. **Breaks when** fundraising stalls, so senior seats
  freeze and the "+2" step vanishes.
- **Channel example:** *EXACTLY How Much…*; *Is an MBA worth it?*; *First Brands…* (Centerview
  segment); *Citi's Global Head of Research* (research exits); *From Intern to Offer: The Unwritten Rules
  of Wall Street Success*; *Our Number One Tip to Break Into Investment Banking*; *CFA for Investment
  Banking* (with Kaplan's Joyce Schnur); *How to Network Like a Pro feat. Jen Prosek* (networking as
  "giving to receive": make introductions and ask nothing; judge conferences by meetings that convert
  within six months).
- **Counterpoint:** The hosts' Centerview take ("wrong job") is the generation that survived the
  system judging it. They acknowledge deaths from overwork and still frame an 8-hour sleep request as
  9-to-5 entitlement; reasonable people disagree. Their own suggestion (follow-the-sun global teams,
  AI) is the more useful idea. Kaplan's guest is selling exam prep and misstates details: CFA Level I
  has 180 questions, not 150; the SIE launched in 2018; the charter also needs ~4,000 hours of work
  experience; licenses lapse after two years out of the industry (extendable), not immediately.
- **Links:** [[trading-floor-mechanics]] (seat comparison); [[professional-services-leverage]]
  (Cravath tournament: the same pyramid logic).

### 4.22 Folded in from the culture-other recaps (Industry / Succession / Strangers)

The TV recaps hold more real teaching than their titles suggest. Only the mechanisms not already
covered above are listed here, compressed. Source episodes: Succession S3 Part 1 (`E-wsDCA0I5I`) and
Part 2 (`2aT4Mofm8ho`); Strangers (`3fbWStK44P0`, `I3XGEgKGDLI`); Industry S3E6 (`H2jaqoTmfzY`), S3E8,
S4 premiere, S4E4, S4E5, S4E8. Pass 2 read the second half in full: the Mindy Kaling reaction
(`RFFok3hycaQ`), Bankers vs. Doctors (`Yc25Hc4AeaY`), Industry S1E3 (`xYByha9veu0`), S3E1 (`XYoNNAlefC8`),
S3E7 (`WaQm3U-mjwM`), S4E1 (`n7YeX2tgykQ`), S4E2 (`Rig7FMhill8`), S4E6 (`YXfRCC0il58`), S4E7
(`bywWURDpNWI`), *Uppity Working Women* (`jjH3Wtiz9EE`) and the remaining culture shorts. S1E3 and
*Uppity Working Women* are garbled machine translations (S1E3 also cuts off mid-sentence), so check
their figures; *Uppity Working Women* and S4E2 contain almost no finance. The bulge-bracket vs.
boutique teardown now has its own section (§4.18).

- **Deferred stock is a bet on your employer (Industry S3E6).** Juniors are paid mostly in cash. The
  stock share and the deferral length both grew after 2008. Jen watched Lehman colleagues' locked-up net
  worth go to zero, so her rule is to take as much cash as possible if you work at a bank. That's the
  employee's view of §4.19: deferral aligns you with the firm, and it also concentrates your wealth in
  the firm.
- **Hedge fund clawbacks and crystallization (Strangers; Industry S4E8).** Hedge funds claw back pay
  more than banks do. At pod shops (Millennium, Citadel, Point72) a PM can have one great year, blow up
  the next, and be clawed back and out. Performance fees usually crystallize in December, but fund
  documents can allow earlier payouts. Worked example on $250M AUM: 2% fee ≈ $5M, plus 20% of $110M
  profit = $22M, so ≈ $27M earned. "Points" (1% of firm profits) are the hedge fund version of carry.
- **Fee compression (Strangers).** Their 2-and-20 example: $100M AUM pays a $2M management fee. Grow it
  to $150M and 20% of the $50M gain is $10M. Fund-of-funds fees fell from 1-and-10 to roughly 50bp
  flat once allocators did manager diligence themselves. The average hedge fund fee is ~1.67%,
  citing a Goldman prime-brokerage report. Long-only managers earn ~50–75bp. The fee you can charge
  tracks how much alpha you deliver that clients can't replicate themselves.
- **First-loss structures (Industry S4E4).** The manager absorbs the first losses in exchange for a
  larger share of upside (a friend's fund gets ~50% of the upside). Used for market-neutral funds.
  This is §4.7's equity check applied to a fund: whoever takes the first loss is paid for leverage.
- **Gross leverage and the margin spiral (Industry S4E4–S4E5).** Gross leverage = (|longs| + |shorts|)
  ÷ NAV. On a 2x short, a 7% rise in the stock costs 14% of NAV (~$35M on $250M), which wipes out a
  $10M first-loss tranche. The prime broker then sells other positions to meet margin. Shorting
  requires a located borrow, a borrow fee, restricted proceeds and extra collateral (cf. §4.13 for
  bonds). Their line: the market can stay irrational longer than you can stay solvent.
- **Total return swaps and Archegos (Industry S4E5).** Post ~10–20% margin for 5–10x synthetic
  exposure: pay SOFR plus a spread, receive the stock's return. The bank holds the shares, so nothing
  is publicly disclosed. Archegos spread the same bet across several prime brokers, the §4.13 "spraying"
  problem at equity scale. A 2021 Viacom share issuance triggered margin calls. Morgan Stanley and
  Goldman sold first; Credit Suisse lost ~$5B. Wirecard (€1.9B of nonexistent cash, forged bank
  confirmations) is their template for fraud found late, cf. §4.12.
- **M&A consideration and control (Succession S3).** Offer premiums run ~20–40%. Merger-arb funds
  buy the gap between the trading price and the offer, while long-only "real money" sells. All-stock
  deals need no financing, but the seller is paid in the buyer's currency. AOL/Time Warner is the
  warning: AOL paid in bubble-priced stock. A cash mix is capped by debt capacity: ~6–7x EBITDA even
  for a stable company, less for a weaker one. Termination fees compensate the counterparty for
  diligence and financing costs. Twitter's was ~$1B on $44B. In the proxy fight each side spent
  ~$100M, and the settlement took the form of board seats plus a standstill (no takeover attempt).
  Valuing a company from a stake: a $350M loss is 10% of a 4% stake, so the stake is $3.5B and the
  company ~$87.5B. *Flag:* the hosts call Disney/Fox an "$85B" deal; the final price was ~$71B.
- **Convertible vs. CoCo (Industry S4E4).** A convertible is debt if the stock falls and equity if it
  rises, which protects the investor. A CoCo (contingent convertible) converts or is written off when
  the issuer is under stress, which protects the issuing bank's capital (Credit Suisse AT1s were wiped
  out). An outside investor would demand the convertible, not the CoCo.
- **Big Law vs. banking pay (Strangers).** Bulge-bracket entry pay is nearly identical across firms,
  and elite boutiques pay perhaps ~$10k more. Law adds ~$250k of tuition and three years of lost
  earnings. Profits per equity partner in 2025, per the hosts: Wachtell over $12M, Kirkland ~$11M,
  Davis Polk ~$9.8M. Their thesis is that elite firms became "alpha providers" by finding the loopholes
  behind liability-management exercises, so they are now paid like risk-takers. This extends
  [[professional-services-leverage]].
- **S&T pay runs on budgets and sales credits (Industry S1E3; short k7ZuBMq2Sl4).** Salespeople are not
  on commission. They earn internal "sales credits" set by a grid of product × size × trade type. Desks
  can double the credits on trades they want done (axes), and some banks (not all: Jen's first had
  none, her next did) charge negative credits, e.g. when a client "showers the street." Figures: ~2,000 credits for
  $100M of 5-year Treasuries vs. $0.5–1M for one structured cross-asset trade. The bonus pool depends on
  results against the desk budget. Making $120M on a $100M budget pays well; making $60M hands rivals
  ammunition to take pool for their own division. Sales and trading fight every year over whether the
  revenue came from bringing in the risk or taking it.
- **What an axe really is, at three levels (Industry S1E3, Jen).** A desk is axed when client flow
  leaves it with more risk than it wants or can cheaply hedge. *Inventory:* bonds quoted 99/101 offered
  at 100 to move them, like a grocer marking down bananas. *Derivative risk:* a 2-year swap hedges with
  2-year Treasuries plus a spread, but an 8-year point has no Treasury (only 7s and 10s), so it needs a
  5-7-10 butterfly; quietly offering the risk to clients is cheaper than paying spreads on three
  illiquid hedges. *Information:* traders post axes just to learn what clients are doing, which is
  worth paying up for. Electronic trading compresses spreads on plain products, so desks push
  **correlation trades** (e.g., a payer swaption, effectively a put on bonds, that pays only if gold and
  the S&P behave a certain way): conditional exposure the client buys more cheaply than the legs, with
  wide bid-offer because there's no liquid market. Jen's critique of Harper's "structure" (index put +
  gold call + builder CDS) is that the put and the CDS are the same bet at two points in the capital
  structure: a portfolio, not a structure.
- **Deferred pay when switching firms (Industry S3E7).** The new firm usually pays a guarantee and buys
  out the deferred cash and stock left behind. When the old employer's stock crashes, the deferred
  balance shrinks and the person becomes cheaper to hire. This is the §4.19 "expensive by 30" logic run
  in reverse. Options in a takeover: assume they all vest; in a stock deal they convert at the exchange
  ratio, in a cash deal you exercise at the strike. Goldman keeps a partner tier above MD, and because
  part of bank pay is stock, bankers own equity from associate level "whether you want to or not."
- **IPO mechanics, the full version (Industry S3E1, "Lumi is WeWork 2.0").** Typical float is 10–20%.
  Price comes from bookbuilding, not a model. The target discount is ~15%, and the pop follows from
  oversubscription (e.g., $200 of orders for $100 of shares), because partially filled buyers then buy
  in the market. The **greenshoe**: the bank sells ~15% more than the deal size and buys shares back in
  the market if the price weakens, which supports trading for the first weeks. The 180-day lockup is
  often followed by a follow-on offering. The bank's real stake is reputation: a broken first deal
  costs fees on the rest of its pipeline (they cite Facebook's IPO). Lumi itself priced at 430 against an
  expected ~480 close, only a ~10% discount. Banks' bake-off valuations give way to research analysts'
  models once they're wall-crossed, and investor orders set the final price; the S3E1 funding ladder
  runs friends and family ($5–25k checks) → angels → VC → growth equity → IPO, with secondary anywhere
  from 0% to 100% of the offering. Wall crossing: an S&T person brought over the information barrier
  can be frozen in personal positions. Kristen puts Volcker's limit on banks' fund investing at ~1% of
  Tier 1; the rule is 3% of any one fund and 3% of Tier 1 in aggregate. Adds to §4.15.
- **Net vs. gross leverage, and EBITDA games (Industry S3E1).** Net debt = debt minus cash. Lumi made
  its net debt look smaller by counting uncollectable receivables as cash. EBITDA isn't GAAP, so it can
  be massaged, as with WeWork's "community-adjusted EBITDA." LBO practice quotes gross leverage because
  lenders want the worst case. What counts as cash: money-market funds yes (cash equivalents are
  instruments under ~3 months at purchase); receivables never, since net-30 terms can stretch to 60–90
  days. $100M of debt with $10M of cash ≈ $90M of debt and none. Ties to §4.2's caveat that EV is only
  as honest as the debt list. Kristen's power-stack aside (same episode): nuclear and coal run
  constantly, wind and solar when they can, and gas plants are the flexible marginal unit, so **gas sets
  the power price**, and a gas spike *raises* a solar generator's margin (the show has it backwards).
- **Valuation hygiene (Industry S3E7, S4E6–S4E7).** Match numerator to denominator: equity value with
  net income / EPS, EV with sales / EBITDA / EBIT ("EV per share" doesn't exist). Banks trade on
  price-to-book because their balance sheets are marked to market. Equity can be worth zero, but the
  whole firm cannot. Accretion/dilution refers to the *buyer's* EPS. Stock consideration exposes the
  seller to the buyer's share price before closing; Netflix–Warner Bros is cited as moving to all-cash
  to speed the deal up (S4E7: from roughly 90% cash to all cash; reported terms were nearer 84/16).
  Disclosure thresholds: 5% in the US, 3% in the UK. Porsche/VW 2008 combined ~42% of the shares with
  31.5% in cash-settled options; the counterparty banks delta-hedged by buying real shares, each just
  under 3%, and "cash-settled" could be switched to physical by agreement. Synthetic positions carry no
  vote or dividend but leave a paper trail (collateral, ISDAs, confirmations), which is how a fake stake
  gets exposed. A bid turns **hostile** only after the board rejects it and the bidder goes to
  shareholders (bear-hug letter). The house version of equity-vs-firm (S4E6): $1M house, $800k mortgage,
  $200k equity; sell at $750k and the equity is zero while lenders still recover most of their money.
  Hence Kristen's sum-of-the-parts correction: a £12/share base case built on £2–3B of legitimate EV
  stays £12 when the fake acquisitions are valued at zero; it doesn't fall to zero.
- **Bank capital stacks (Industry S3E7, S4E6).** Preferred equity has no principal to repay and is
  subordinated. TARP and Buffett's Goldman investment were structured this way, hence the hosts' "a
  capital injection, not a bailout." In 2008 MUFG put $9B into Morgan Stanley, mostly convertible
  preferred with a 10% dividend and a ~$31.25 conversion price, for 21%. Basel III minimums: 4.5% CET1,
  6% Tier 1, 8% total capital; big banks run 10–14%. The show repeatedly confuses four instruments:
  putable bonds (investor's trigger), callable bonds (issuer's option), convertibles and CoCos.
- **2008 plumbing and rescues (Industry S3E7).** Pre-2008 swaps were bilateral under a CSA (Credit
  Support Annex; Jen calls it a "collateral services agreement"). If Lehman owed MS $10M and failed, MS
  lost the $10M *and* its offsetting hedge was suddenly unhedged, so losses chained bank to bank; that is
  why most derivatives are now centrally cleared. Lehman's 2008 was a run on **liquidity** (clearing banks
  and repo counterparties demanding collateral), not deposits, after ~$10B of capital raises (a $4B
  convertible preferred in April, $6B after a $2.8B Q2 loss) failed to restore confidence. Barclays
  bought the US business for its IBD/ECM and the 745 Seventh Ave building, not its FICC, so FICC staff
  were cut and everyone reinterviewed for their own jobs. The 2008 short-sale ban covered *all* shorting
  of financials, which blew up convertible-arb funds that hedge by shorting stock. Morgan Stanley stayed
  independent on CIC's $5B mandatory convertible (Dec 2007) plus MUFG's $9B. Kristen's TARP case: three
  programs, below-market preferred dividends, and MS/GS forced to take it for system confidence; TARP
  is often confused with QE, which is what actually drove 2009–10 bank profits. SVB (Treasuries marked
  down as rates rose) and Credit Suisse (a 2022 Saudi/QIA raise, then a refusal of more support, then a
  forced weekend sale to UBS with AT1s wiped) are her modern rhymes. Distress is defined as **inability
  to refinance**, not a falling share price. *Flags:* the TARP disbursed figure is ~$443B (authority cut
  from $700B to $475B), not her "60%" or "50% untouched"; the equity-method threshold is 20%, not 21%.
- **Liquidity matching and gating (Industry S4E1).** PE locks capital up 5–7 years to match illiquid
  assets; hedge funds offer monthly or quarterly liquidity (multi-manager platforms lock up 3+ years).
  Redemptions force fire sales that can kill a fund whose thesis is right. **Gating** suspends outflows
  so stayers aren't hurt by forced selling, and it wrecks future fundraising. Allocators on the Yale
  model buy market beta cheaply and use hedge funds for uncorrelated absolute return, so a short-only
  fund is a hedge, not a market-beater; an SMA runs the client's constraints while a fund pools capital
  behind the manager's view. Shorting stock: locate a borrow through prime brokerage, pay the borrow fee
  plus any dividends owed to the lender; illiquid mid-caps are expensive to borrow. Cover in small clips
  across dealers so you don't squeeze yourself (S4E7). Ties to the private-credit gating discussion in
  [[wss-credit-distressed]].
- **Fraud patterns and audit (Industry S4E6).** Kristen's taxonomy. *Enron* (~$70B peak cap): booked a
  10–15-year contract's full value on day one, hid debt and losses in SPEs, round-tripped trades to
  inflate revenue; Arthur Andersen died with it, and Sarbanes-Oxley (2002) created the PCAOB, CEO/CFO
  certification and auditor-independence rules. *Valeant*: R&D ~3% of sales vs. a 15–20% industry norm;
  bought drugs and raised prices (one +525%, another +2,700%); channel stuffing through Philidor; Ackman
  lost ~$4B. *Luckin*: simply fabricated sales, caught by store-traffic video and receipts. Lesson:
  complexity is cover; "the cash flow statement tells the truth." A legitimate SPV for contrast: Meta's
  Hyperion data center, owned and controlled by Blue Owl with Meta holding ~20% and leasing it, which
  keeps the debt off Meta's balance sheet. Audit outcomes: clean, qualified, adverse (and disclaimer,
  which she omits). *Flags:* Luckin's video evidence was ~11,000 hours, not "92,000"; Liberation Day
  was April 2, 2025, not April 9.
- **Bankruptcy waterfall and UK regulators (Industry S4E7).** Senior secured → senior unsecured →
  subordinated → equity; Kristen's training firm recovered ~12c on the dollar on unpaid Lehman invoices,
  trickling in over ~10 years (the unsecured-creditor reality behind §4.12's ~70c secured figure). Bank
  M&A priced at ~1.2x book with a 90-day clawback works like an earn-out. UK map: the SFO prosecutes
  fraud (LIBOR), the FCA is roughly SEC plus CFPB, the PRA licenses banks, and a Section 166
  "skilled person review" lets the regulator compel an outside firm to review governance and controls.
- **Insurance as tail-risk pricing (shorts).** A-Rod's 2001 10-year, $252M contract was spread across 17
  insurers; nobody would cover the last three years (performance falls after ~34), so Buffett did:
  the back-end years carry the risk, and the premium is the price of a tail. War-risk marine cover is
  priced per transit at roughly 0.25–0.30% of hull value (~$250–300k on a $100M ship), lower with armed
  guards, and insurers can simply withdraw cover.
- **Sell company stock when it vests (Industry S4E7).** Your salary already makes you long your
  employer, so holding its stock as well doubles the risk. This is blanket advice; the hosts don't
  mention taxes. Taylor Swift masters (short): Scooter Braun bought for ~$140M and sold 17 months later
  for $300M. Shamrock held from 2020 to 2025, putting in $300M and selling for $360M while collecting
  ~$30M a year of income, about 12% a year before financing.
- **Doctors vs. bankers (Yc25Hc4AeaY).** No lifetime-earnings model, but the shape is clear: residents
  earn ~$50–60k (NYC is now nearer $70–90k), a general pediatrician posting paid $125k, and "real money"
  arrives around 31–32. NYC academic medicine pays around the national median, a prestige discount.
  Pediatric emergency medicine pays in the low-to-mid $200ks, **$50–100k less** than adult EM despite
  more training, because insurers set pediatric reimbursement lower decades ago; incentives follow
  reimbursement, so cash-pay, 9-to-5 specialties (sleep, allergy) are now the competitive ones. A few
  surgical services subsidize the rest of the hospital. Insurers can pay up to a year late, claw back,
  or downcode (one paid ~$200 for a breast reduction that includes three months of post-op care), which
  pushes surgeons to cash pay, collected before surgery. Surgery is compared to project-based IBD and
  the ER to reactive S&T. *Flag:* $80k a year of college is $320k over four years, not the "$240k" said.
  Household math (short): $1M a year in NYC with three kids leaves ~$100–200k after ~$350k federal plus
  ~$100k state, city and payroll tax, $25–40k of health premiums, ~$200k of housing on a $2.5M apartment,
  and $40–72k per child of preschool plus a nanny.
- **Bankers vs. lawyers (`4K9ZjBkSTT4`, with a Wachtell M&A partner and a Davis Polk capital-markets
  partner).** M&A law covers *control* transactions; capital markets covers raising money without
  selling control, and is collegial because issuer and underwriter want the same outcome, while M&A
  risk allocation is zero-sum. Bankers set price and consideration; lawyers set structure (direct vs.
  reverse triangular merger), shareholder-vote consequences, termination and reverse termination fees,
  and antitrust efforts covenants. Big Law first-years earn ~**$225k** base with a small bonus (pay
  weighted to base, consistent with more risk-averse people); banking pays a lower base and larger
  bonus, with MDs at $1–5M. Partnership takes ~8–10 years by qualitative vote, and partners buy in with
  capital. Most contracts are never re-read; the ones that are (a buyer trying to walk) are why the best
  drafters are hired up front. *Flag:* the vote trigger he simplifies as the cash/stock mix is really
  the exchange rule on issuing ≥20% of the acquirer's shares.
- **Sports franchises as assets (`0Un7W_aL1H4`, Eli Manning and David Adelman; routed to this cluster).**
  Valuation tracks how much revenue is shared nationally. NFL: a ~$110B, 11-year national TV deal split
  equally across 32 teams plus a hard cap, so big- and small-market teams converge in value. NBA: ~60/40
  national/local with a soft cap, a luxury tax and two "aprons" that add penalties and roster limits.
  MLB: mostly local revenue and no cap, so value depends on market and only a handful of teams make real
  money. The NFL now admits an approved list of PE funds (Arctos, Ares, Sixth Street, a Blackstone/Carlyle
  consortium) for minority stakes, which pushed money down into smaller sports assets. Adelman's point:
  owning the arena captures building revenue and the fan experience (the 76ers' 50/50 arena with Comcast,
  ~$1.5B, opening 2031), and the surrounding real estate counts toward team value. *Flags:* $110B/11/32 is
  ~$312M a team a year from TV alone, not "$400M"; Kristen's 4.2x apron "fine" is invented (the tax is
  tiered ~1.5–4.75x on the overage); the NBA deal is ~$76B over 11 years; Packers shares carry no
  economic rights, so "publicly traded" is wrong.
- **One-sidedness flags (culture-other).** The two Strangers episodes contradict each other on AUM,
  fee terms and roles. Their claim that a short over 5% becomes public is wrong: 13D/G covers long
  positions, and EU/UK net-short disclosure starts at 0.1–0.5%. Their "~57% NY marginal tax" is high;
  the top combined federal/state/city rate is ~52%. Jen's "TARP wasn't technically a bailout" is
  opinion stated as fact.

---

## 5 · How the concepts connect

```
 three statements (§4.1) ──► unlevered FCF ──► DCF (§4.3) ──► ENTERPRISE VALUE (§4.2) ◄── comps / precedents
                                                  ▲
               WACC (§4.4): rf + β × MRP for equity; YTM × (1 − t) for debt
                                                  ▲
         tax shield, capped at 30% of EBIT(DA) (§4.6) ──► capital structure (§4.5): debt cheap until distress
                                                  │
 purchase multiple ──► debt capacity (turns of EBITDA) ──► EQUITY CHECK (§4.7) ──► sources & uses (§4.9)
                                                  │                   │
         who holds the debt: syndicate → CLO → private credit (§4.10)  ▼
                    │                                     paper LBO: IRR / MOIC (§4.8)
       covenants, collateral, recovery (§4.12)                        │
       yield-hungry market → covenant-lite → fraud found late         ▼
                                                     carry (§4.20) ──► comp: base, bonus, deferral (§4.19)
 exit: IPO (pop = transfer, §4.15) / sale / continuation;                  │
 private marks (§4.16) bridge the years with no price                       ▼
                                          who sells the advice: boutique vs. bulge bracket (§4.18)
                                          and who climbs the ladder: career pipeline (§4.21)
```

The causal spine: **the three statements produce the cash flows; the WACC prices them, and the tax
treatment of debt bends the WACC; the price paid and debt capacity set the equity check; the equity
check decides both the return and who eats the first loss; the holder of the debt decides where that
loss lands; and the return decides carry, which is what the whole career ladder is climbing toward.**
Two recurring tensions run across the chain. First, every "mechanical" step hides a judgment the seat
shapes: the sell side standardizes beta and the MRP to survive a lawsuit, the buy side uses judgment,
and an *Industry* banker lowers the WACC to please a client. Second, controls at every link
(covenants, haircuts, research barriers, central clearing, deferral, clawbacks) each exist because a
past failure at that link was expensive: TXU and hung bridges, Lehman's bilateral swaps, the pre-2003
research scandals, the 2008 bonus-for-blowup problem.

---

## 6 · Retrieval questions

1. **A headline says Company A was "sold for $20B less" than two years ago. What two numbers do you
   ask for before believing it?** — Debt (and cash) at both dates. The price of the business is EV;
   an equity-value drop can be pure added leverage (X/xAI: 33+12 ≈ 44+0.6).
2. **Why does Kristen put the cash flow statement in the middle of a three-statement model, and why
   can a DCF skip the balance sheet?** — It follows one dollar: net income opens the CFS, which ends in
   the change in cash that lands on the balance sheet. A DCF needs only unlevered cash flows (EBITDA,
   D&A, capex, ΔNWC), not debt or a balancing balance sheet.
3. **A company's 2020 bonds carry a 3% coupon but yield 7% today; the tax rate is 25%. What is its
   cost of debt for the WACC, and why not 3%?** — 7% × 0.75 = 5.25%. The WACC needs today's marginal
   cost of borrowing; the coupon reflects 2020 rates.
4. **A sell-side banker and a buy-side investor value the same company. Why might they choose different
   betas?** — The banker may defend a fairness opinion in court, so uses a standard (Bloomberg adjusted
   beta, ⅔ raw + ⅓ × 1); the investor can weigh R², use peer asset betas relevered, or a forward beta.
5. **A viewer says cost of equity is 5% because the stock trades at 20x earnings. What is right and
   wrong about that?** — 1/PE is the earnings yield, useful for EPS accretion (stock at 5% vs. debt at
   5.25% after tax), but it ignores growth and payout and is not a required return. Equity is junior to
   debt (loan recoveries ~76%, equity often zero), so it must cost more.
6. **Under Modigliani–Miller with taxes, adding debt raises firm value. Where does the value come from,
   per Kristen?** — From taxpayers, through the interest deduction; it's a transfer, not created value.
   Bankruptcy and issuance costs (IPO fees 6–7% vs. bond fees 12–40bp) are what MM leaves out.
7. **In Kristen's LBO ($10M at 10x, $3M equity, EBITDA $1M → $1.5M, $1M of debt repaid), how much of the
   equity gain came from operations vs. debt paydown, and what would the unlevered return be?** — $5M of
   the $6M gain from EBITDA growth, $1M from paydown; 3.0x ≈ 25% IRR levered vs. 1.5x ≈ 8% unlevered.
8. **Why could PE not LBO most tech companies in 2007, in one sentence of arithmetic?** — At ~20x
   EBITDA with lenders funding 7–8x, equity must fill 60–65%, far above the ~30% that makes LBO returns
   work.
9. **In a public-to-private LBO, why is there no "minimum cash" line in uses, and where does the
   target's cash go?** — Buying the shares buys the cash; excess cash above the operating keep-back
   appears as a *source* funding the deal. In a private cash-free/debt-free deal, the seller keeps its
   cash and repays its debt.
10. **Skechers holders could take $63 cash or $57 + one private unit. What are electors betting, and
    what are they giving up?** — That the unit is worth more than $6 after 3G's turnaround; they give up
    liquidity, control and seniority (the unit sits under the new debt), within a 20% rollover cap.
11. **Why did JPMorgan's sole $20B commitment worry Jen more than TXU's syndicate did?** — Distribution
    spreads risk; a single holder concentrates it on one systemically important balance sheet.
12. **Why does a boutique add restructuring, and why did Greenhill still sell to Mizuho?** — Restructuring
    peaks when M&A dies, the only hedge an advice-only firm has; inside a universal bank, trading's
    volatility profits offset M&A droughts, and the boutique model had been widely copied.
13. **Why did the EU bonus cap increase guaranteed pay, and what does a two-year switching guarantee do
    to pay in year three?** — Banks raised bases to hold total comp, so less pay was at risk. Guarantees
    borrow from the future: after they expire you are usually "paid down."
14. **How did Lehman's failure hurt Morgan Stanley even on a swap where MS was owed money?** — MS lost
    the receivable *and* its offsetting hedge with another party was suddenly unhedged; bilateral
    exposure chained losses across banks, which is why most swaps are now centrally cleared.

---

## 7 · Gaps — titles to fold in later

Still missing after pass 2 (catalog `wss_all_videos.json` / `wss_all_shorts.json` vs. files present):

- **Technicals:** *Paper LBO must know for PE interviews* (`J9xh-sNosSM`) · *Private Equity Interview MUST
  KNOW: The Rule of 72* (`h57N5mP-qn8`) · *8 must know technicals for sales and trading interviews*
  (`AjVQNEWc5pc`) · *Largest Debt Commitment in History for LBO by ONE BANK* (`fZQP_mQ_2sg`, EA Part 2) ·
  WACC Part 1 (the weighting video; no catalog match found). *Top 8 Technicals* (`qAzAguiaTJ0`,
  `VXrEMy8w83M`) exist but are music-only, so their content is unrecoverable from transcripts.
- **Industry & equity offerings:** *S2E2 "Giant Squid": Block Trades, IPOs vs. Other Equity Offerings*
  (`beSAafxvKn0`) · *How Lumi's IPO was Saved By Shady Tricks (Industry S3E2)* (`HHHy4hPhDG0`) ·
  *Investment banking vs. Private equity* (`6kiO6Tc1Qf8`) · *Doctors vs. Investment bankers*
  (`nSm30CMe2Hg`) · *Investment Banking vs. Sales and Trading Lifestyle* (`IZJjGRQqm4E`) · several Excel
  shortcut shorts (`Y3FC14q5-OI`, `QR7T5q4bt34`, `XmmJ6VXft7Q`, `pp8BOfKkZxQ`, `ogGE4l4H2Mw`,
  `9JSFOpy1zOU`).
- **Present but owned by sibling notes** (not folded here to avoid duplication): *Private Equity 102*,
  *PE Secondaries 101/201*, *Private Equity vs. Private Credit in 90 seconds* → [[wss-private-markets-wealth]];
  *The HIDDEN Cost of SPACs*, *Industry S2E3: Block Trades* → [[wss-capital-markets-ma]]. *PE Associate
  Tell-All* (`8W5DEMasd3k`), *Growth Equity Value Creation w/ Sixth Street* (`EY3HcYOB2No`) and *The One
  Fatal Flaw with Private Equity* (`vy6iPkxcBFM`) now have transcripts and are candidates for §4.21 or
  the private-markets note on a later pass.
- **Content the episodes didn't deliver:** the Bok interview never covers boutique fee structures
  (retainer vs. success fee), deal-size bands or analyst pay, and gives no Mizuho price; those need a
  non-channel source.
