# Credit, private credit & distressed — how lenders get paid, and how they get taken (Wall Street Skinny)

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-capital-markets-ma]] [[wss-private-markets-wealth]] [[wss-rates-macro]] [[wss-technicals-career]] [[wss-trading-hedge-funds]]

> **Sources — 34 transcripts (17 long-form, 17 shorts)** from The Wall Street Skinny (Kristen Kelly,
> ex-Morgan Stanley financial sponsors and 2007 CLO desk; Jen Saarbach, ex-Lehman / Morgan Stanley rates
> S&T). Anchors: the three-part **Caesars** series (Pt 1 LBO, Pt 2 distressed, Pt 3 with FT reporter
> **Sujeet Indap**, co-author of *Caesars Palace Coup*); the full **Distressed Debt 101** interview with
> **Michael Gatto** (head of private-side investing at Silver Point, ~$41bn; author of *The Credit
> Investor's Handbook*); **Direct Lending Explained** with **Alona Gornick** (Churchill Asset Management,
> a TIAA affiliate); **Credit Trading 101** with ex-Goldman credit trader **Carissa Jordan**; **DCM 101**;
> two 2026 private-credit deep dives (the second with **Fabian Kroboth**, CIO of Northwall Capital, ~$3bn,
> transcribed as "Krobog"/"Croxbach"); **Keri Findley** (Tacora Capital) on asset-based lending; the
> **PIK** episode; **EA vs TXU**; two **First Brands** episodes; **Oracle CDS**; the **Lakers /
> Guggenheim** insurer story; live from **Global Alts Miami**; shorts with Gatto, Kroboth, the
> $53bn-fund strategist and a Carlyle wealth head. Pass 2 also read gap-list shorts routed to other
> clusters (Skechers rollover equity, a corporate-bond explainer). Raw at
> `_ingest/raw/2026-10-04/media/wall-street-skinny/` (cluster key `credit-distressed`).
>
> **Scope note:** three files in this cluster are mostly about something else. The First Brands/Apollo
> episode (`O4ayidFGsGM`) is ~80% an operations interview (Don Kieffer, MIT Sloan, *There's Got to Be a
> Better Way*); the EA episode and the First Brands bankruptcy episode spend half their time on Fed
> funds vs SOFR, gold, and a naked-short Treasury trader. Those parts are left to the ops and
> rates-macro notes. Only the credit material is distilled here.
>
> **Maps to:** Course **02** (Corporate Finance & Valuation: capital structure, cost of debt), Course
> **11** (Macro: spreads, cycles, 2008), **E2** (Capital Allocation), **E3** (M&A, Deals & Restructuring,
> the primary home), **E4** (Governance: boards owe duties to equity, lenders get only their contract),
> **E6** (Crisis Leadership), **E9** (Macro for Decision-Makers).
>
> ⚠ **Bias.** The hosts are ex-sell-side and came up in the 2007 CLO and rates world. Kristen defends
> CLOs hard, and her own data point for that defense ("defaults were like 2%", repeated in two
> episodes) is wrong (see §18). Guests are often selling an asset class. Findley is raising a fund and
> quotes her own returns. Gatto runs Silver Point's private credit and is "100%" sure private credit is
> good for society, while plugging his book throughout. Gornick's current job is selling Churchill's
> funds to the wealth channel, and her "remarkably low loss rates" claim predates a real cycle. Kroboth
> jokes about fundraising and frames his smaller AUM as discipline. Two bond shorts are paid ads for
> Public.com's bond account. The Global Alts host runs the conference whose meeting counts he quotes.
> Indap and Carissa Jordan (no longer at a bank) are the most neutral voices. Several figures are
> misspoken on air ("$30 million" for the $30bn Caesars LBO, "$6 million" for First Brands' $6bn
> refinancing, VICI as a "$50 million company", the Gatto episode "filmed in November of 2020" when
> First Brands and Tricolor date it to late 2025). Each is flagged where it appears. The hosts also cite
> ChatGPT and Claude as sources for BDC leverage and Affinity's AUM, so treat those numbers as
> unverified.

---

## What this adds to the program

- **The lender's side of every deal.** The repo teaches the LBO from the equity seat
  ([[tiger-sisters-private-capital-101]]: house analogy, Toys R Us) and leverage as a balance-sheet ratio
  (`learn/unit-04-is-it-healthy.md`). Nothing here covers how debt is priced, layered, documented,
  traded, or taken away. This note adds credit spreads, seniority and structural subordination,
  covenants, recovery rates, and the playbook equity uses against debt.
- **Agency cost of debt, made concrete.** [[canon-jensen-meckling-agency-theory]] covers managers versus
  shareholders. The 1976 paper's *other* half, where equity expropriates creditors once leverage is
  high, is missing from the repo. Caesars is that half acted out in full: asset transfers to an affiliate,
  guarantee stripping, conflicted fairness opinions.
- **Private credit as a structure, not a buzzword.** Direct lending as it is actually built (middle-market
  tiers, unitranche, delayed-draw loans, the 150–250bp premium and what it buys), asset-based lending,
  the three kinds of semi-liquid retail vehicle and why each gates differently, insurer balance sheets,
  and why the 2026 stress looks like "2008 with the leverage moved". None of it is in the repo.
- **The plumbing of a bond.** How a bond is born (syndicate, book, Treasury plus spread) and how it then
  trades (OTC dealers, spread vs price quoting, agency trading, portfolio trades, CDS indices). The repo's
  [[trading-floor-mechanics]] covers the floor; this adds the credit product itself.
- **Why the bottom of a capital structure is a negotiation, not a formula.** Distressed strategies (pull
  to par, distress for control, capital-structure relative value), valuation fights, liability management
  exercises with a worked uptier, capital-solutions lending, CDS as a weapon as well as a hedge, and the
  reason a 2026 first-lien loan recovers about 60 cents where it once recovered about 80.
- **A direct challenge to the accounting core.** Course 01 material (`summaries/core-01-accounting.json`)
  teaches the current ratio as a liquidity measure. Gatto, who teaches credit at Columbia and Fordham,
  calls it analytically useless. §5 sets out why a lender looks elsewhere.
- **A judgment hook for `acumen/`.** Every concept below gives a falsifiable question to ask of a live
  credit: who controls the documents, who can be layered, and who is forced to sell.

## Concept map

| # | Concept | One-line definition | Why it matters | In repo? |
|---|---|---|---|---|
| 1 | Credit asymmetry & expected loss | Lenders' upside stops at par; loss = default rate × (1 − recovery) | Sets the whole mindset: avoid losers, don't pick winners | n |
| 2 | Credit spreads | Borrowing cost = risk-free base + a premium for default risk | Spreads, not rates, decide whether a leveraged company can refinance | n |
| 3 | Bond issuance: DCM, syndicates & ratings | Banks underwrite, build a book and price a new bond at Treasury + spread | Where corporate debt is born, and who bears the risk until it's sold | partial ([[wss-capital-markets-ma]] §2 has the equity bookbuild) |
| 4 | Credit trading & market structure | OTC dealers quoting spread (IG) or price (HY), now mostly as agents | Liquidity is conditional on a dealer's balance sheet, which shrank after 2008 | partial (trading-floor-mechanics, generic) |
| 5 | Leverage, coverage, covenants & liquidity | Debt/EBITDA, EBITDA/interest, the tripwires written on them, and real liquidity | How lenders see trouble early, and why cov-lite blinds them | partial (unit-04; core-01 current ratio) |
| 6 | Capital structure, security & structural subordination | Who gets paid first, against what assets, at which legal entity | Where you sit decides what you recover | partial (LBO stack only) |
| 7 | Public vs private credit | Syndicated loans, HY bonds, bridges and CLOs vs one-lender direct loans | Explains the decade's migration of lending out of banks | n |
| 8 | Direct lending mechanics | Unitranche, revolvers, delayed-draw loans, covenants and the life of a loan | What the borrower buys with a 150–250bp premium | n |
| 9 | Asset-based lending | Lending against pools of loans, leases or receivables, not company earnings | A different underwriting model, and the one First Brands defrauded | n |
| 10 | PIK interest | Interest added to principal instead of paid in cash | The cleanest early warning of private-credit stress | n |
| 11 | LBO leverage then vs now | Caesars and TXU (≈8x, <20% equity) vs EA (7.5x, ~65% equity) | The equity cushion, not the multiple, sets who absorbs the first loss | partial |
| 12 | BDCs, semi-liquid vehicles & gating | Public BDCs, non-traded BDCs and interval funds that borrow at fund level and cap redemptions | The liquidity mismatch behind the 2026 headlines | n |
| 13 | Insurer balance-sheet model | Asset managers buying insurers to hold their own originated credit | Lowest-cost funding for private credit, and where related-party risk hides | n |
| 14 | Liability management & creditor-on-creditor violence | Uptiers, drop-downs, guarantee releases and roll-ups that reorder the stack | Why "senior secured" no longer means safe | n |
| 15 | Distressed investing, valuation fights & bankruptcy | Buying debt cheap to recover par or take control; Ch. 11 vs Ch. 7 | Where credit cycles turn into ownership changes | n |
| 16 | Capital solutions / special situations | Senior lending into complex or urgent situations other lenders can't touch | "Cap solutions is the new distressed": where distressed capital went | n |
| 17 | Credit default swaps | Insurance on a borrower's default, tradable without owning the debt | Hedge, short, and lever that changes creditors' incentives | partial (Bloomberg CDS screen; 2008 mention) |
| 18 | Private credit vs 2008 | What's the same (lax standards, opacity) and what's different (less bank leverage, no housing) | The systemic-risk call every allocator is being asked to make | n |

---

## 1 · Credit asymmetry & expected loss

**What it is.** A lender's best case is fixed: collect the coupons and get the face value ("par") back.
The worst case is losing most of the principal. So credit investing is about avoiding the bad outcome
rather than finding the great one. The hosts' version: equity has to pick winners, credit just has to
avoid losers. Gatto's version is about temperament. A venture investor can take zeros on six deals out
of ten as long as it doesn't miss the next Facebook; a lender's job is to never make the mistake, so the
credit analyst is professionally glass-half-empty.

**How it works.** Any pool of loans comes down to two assumptions: what share **defaults**, and how much
you **recover** on the ones that do. Expected loss = default rate × (1 − recovery rate). The channel's
stress case (Kristen recalling a Blackstone executive, *Private Credit: The Best Explanation*): even at a
**15%** cumulative default rate and **50%** recovery, the book loses 15% × 0.5 = **7.5%** of principal.
Painful, and it ends the 10–12% return story, but it is nowhere near the 100-to-zero of an equity wipeout.
Annualized illustration (not from the channel): 3% default × (1 − 0.70) = 0.9% a year of loss, which a
10% coupon easily covers; at 8% defaults and 60% recovery the loss is 3.2% a year, and the coupon carries
a levered fund only if nothing else goes wrong. Anchor recoveries on air: CLO models assumed about 70
cents on senior loans (Kristen, in three episodes). In the financial crisis you expected about 70 on
senior debt and about 40 on bonds (Caesars Pt 2). Moody's now shows first-lien recoveries near 60 cents,
down from about 80 (Indap, Pt 3).

**Business significance / value.** This is why lenders charge a spread, demand collateral and write
covenants: every tool exists to push recovery up or default down. It is also why credit funds lever
up. A 10% asset with a capped upside only reaches equity-like returns if you borrow against it (§12).
Gatto says every Silver Point credit memo now carries a section on AI vulnerability: a borrower that
covers its coupon easily today may not in four years, and the analyst who says "we're not worried about
that" is the one he expects to blow up.

**Forces & impact.** Recoveries depend on what sits *below* you in the structure (§6), on how much
leverage the deal carries, on what is left to sell (a pipe-fittings maker leaves more residual value than
a SaaS wrapper, Jen's point in the 2008 deep dive), and on whether other creditors can jump ahead of you
(§14). All of these have moved against lenders since 2015, and that is the core of the "it's worse than
2008" argument.

**With vs. without.** Without the asymmetry framing, investors read a 10–11% yield on "senior secured"
loans as low risk and high reward, which is how BCRED was sold (shorts, `lAF2ujd64GU`). With it, you
ask what the yield pays you for, and the answer is default and recovery risk plus illiquidity.

**Applies when / Breaks when.** Applies to every performing loan. Breaks when the instrument has hidden
upside, as in distressed debt bought at 10–40 cents (§15), where returns look like equity. Findley's
re-REMIC mezzanine bonds bought at about 10 cents are the extreme case.

**Channel example.** *The BEST EXPLAINER you'll get on Private Credit Funds like Blackstone's BCRED or
Blue Owl's OBDC* (short). The 15/50 stress case from *Private Credit: The Best Explanation of Exactly
What's Happening*. Gatto's memo discipline from *Distressed Debt 101 with the GOAT*. Recovery data from
*Financial Times Reporter TELLS ALL: Why Private Credit is Worse than Credit in 2008*.

**Counterpoint.** The short's "low risk, high reward" framing of BCRED is a straw man. Nobody serious
priced it that way, since the yield was mostly SOFR plus an illiquidity premium during a high-rate
period. The 15/50 stress case comes secondhand from a manager defending its own fund, and it ignores
fund leverage: a 7.5% principal loss on a book levered 1:1 is roughly 15% of investor equity. The 70/40
GFC recovery numbers are roughly right for loans and bonds respectively, though dated: they predate
cov-lite and loan-only structures.

**Links.** [[canon-klarman-margin-of-safety]] (lender's margin of safety = recovery cushion),
[[canon-taleb-black-swan]] (capped upside, fat left tail), [[canon-grove-only-the-paranoid-survive]]
(Gatto's credit temperament).

---

## 2 · Credit spreads

**What it is.** A company's borrowing rate has two parts: a **base rate** (Treasury yield or SOFR) that
everyone pays, and a **credit spread** that pays the lender for this borrower's default risk. Spreads
are quoted in basis points (bp; 100bp = 1%).

**How it works.** The tariff short's arithmetic: Treasuries at 4% plus a 150bp spread gives a 5.5%
all-in cost. When tariffs hit, the base rate *fell* (money fled into Treasuries) but spreads *widened*,
because default risk rose through three channels: higher input costs, weaker demand at higher prices,
and retaliation abroad. So the US government's borrowing got cheaper while leveraged companies'
borrowing got dearer. The Oracle episode shows the market-level gauge: **CDX IG**, the index of CDS on
investment-grade names, widened to roughly 40bp while Oracle's own spread widened by about 95bp. The
investor's side of the same arithmetic (a sponsored corporate-bond short): a 5% five-year Treasury plus a
170bp spread locks in 6.7%. If Treasuries don't move but the spread tightens to 150bp, new bonds yield
6.5% and the 6.7% bond rises in price. A bondholder earns from falling rates *or* tightening spreads,
and loses on either moving the other way.

**Business significance / value.** The spread is the price of access to capital. It decides whether a
maturity can be refinanced (First Brands could not), whether an LBO pencils out, and whether a
hyperscaler can keep funding capex with debt. Indap's note on the record investment-grade week (Amazon,
Honeywell) shows the other side: treasurers rush to issue when spreads are tight and windows open.

**Forces & impact.** Spreads compress when investors hunt for yield. Jen's "cash trap" argument: front-end
investors pre-buy Fed cuts, then stretch further out the curve and down the credit spectrum, and spreads
reach all-time tights. *Credit Trading 101* gives the mechanism. With Treasury yields high, "yield-based
buyers" buy corporate bonds outright for the all-in yield instead of hedging out the rate component, so
their demand lands on the spread. On air, IG spreads were at their tightest since 2007 while default
rates sat around a historically normal 3% (Carissa, citing a Barclays credit strategist). Spreads widen
on defaults, fraud headlines and recession signals. Second-order
effect: tight spreads loosen terms (cov-lite, PIK toggles), and loose terms make the next widening
worse.

**With vs. without.** If spreads did not move with risk, risky borrowers would fund at the government's
rate and lenders would be paid nothing for default, which was roughly the 2006–07 condition. When spreads
stay tight for too long, everyone short credit is "dying" (Jen on First Brands): the negative carry of
being right too early kills the position before the event arrives.

**Applies when / Breaks when.** Applies to traded credit. It breaks in private credit, where a loan
"identifies as par" (Jen) because it is marked to model, not to market. Spread widening shows up late
there, as markdowns and dividend cuts (§12).

**Channel example.** *Tariff Fallout: Why Are Credit Spreads Widening?* (short). *Oracle CDS: the
"Anti-AI Trade"*. *Why Apollo Was Blacklisted By First Brands*, where First Brands broke and spreads
"didn't budge". *Credit Trading 101* (tights with 3% defaults). *How does investing in corporate bonds
work?* (short, a Public.com ad).

**Counterpoint.** The tariff short treats spreads as a pure function of fundamentals. In practice
technical demand matters as much: insurer and retail inflows can hold spreads tight through real
deterioration, which is the hosts' own point elsewhere and the Barclays strategist's whole argument.
Jen's cash-trap thesis is her hypothesis, not consensus. The corporate-bond short is an ad promising
to "lock in" 6.7%; that yield is locked only if you hold to maturity and nothing defaults, and a blend
of IG and high yield at 170bp is a portfolio average, not a risk level.

**Links.** [[bloomberg-terminal-instrumentation]] (`CDS`, `WB` spread screens the program cannot
reproduce for free), [[trading-floor-mechanics]].

---

## 3 · Where bonds come from: DCM, syndicates & ratings

**What it is.** A bond is a tradable slice of a loan. The **debt capital markets (DCM)** group sits
between investment banking and sales & trading: it helps a company decide what debt to issue, then a
**syndicate** of banks **underwrites** it (commits to buy the whole issue if investors don't) and sells
it on to investors. Investment-grade issuers are covered by DCM proper; high-yield issuers, often LBO
companies, by **leveraged finance** (levfin).

**How it works.** The hosts' worked example (*DCM 101*): Amazon borrowing about **$13.7bn** to buy Whole
Foods, with Goldman, Bank of America and JPMorgan as the syndicate and maturities out to 40 years.
1. **Underwriting spread.** If the syndicate commits at 98 and sells to investors at 100, the 2 points
   are its fee and its cushion against the market moving before the bonds are placed.
2. **Pricing = risk-free + spread.** Take the on-the-run Treasury of the same tenor (say 5% for 10
   years), add the issuer's credit spread (say 100bp for Amazon), and the coupon is **6%**. Longer tenor
   costs more (the hosts' 6% for 10 years vs 8% for 40), and weaker credit costs more.
3. **Building the book.** Fixed-income salespeople collect orders from Fidelity, BlackRock, Vanguard and
   the like. A hot book (the hosts' hypothetical: $45bn of orders for $13.7bn of bonds) lets the
   syndicate tighten "price talk", so the issuer pays a lower yield. In 2026, Amazon's record issuance day
   was about **3.5x** oversubscribed (Jen, *Private Credit Deep Dive*), and she warns books are padded.
4. **Pricing call and allocation.** On pricing day a trader calls the Treasury level, the spread is
   added, and the bond is born. The lead underwriter decides allocations; per Carissa, its traders weigh
   in on who is "real money" and who will flip. The bond then "breaks" and the trader sends the first
   two-way market, sometimes minutes after allocation.

**Ratings** set the boundary. S&P, Moody's and Fitch run AAA, AA, A, BBB (investment grade, down to
BBB−), then BB, B, CCC (high yield, BB+ and below), then default. High-yield issues need size to trade:
Kristen's rule of thumb was at least about $200M, and the smallest issue Carissa ever traded was about
$150M, which "you never see again" once placed.

**Business significance / value.** DCM turns a company's need for long-term money into securities that
thousands of investors can hold in small pieces, so no single bank has to carry Amazon for 40 years. The
bank earns the underwriting spread and the relationship. The issuer gets price discovery; the investor
gets a liquid claim.

**Forces & impact.** Issuance windows open and shut with rates and sentiment, which is why treasurers rush
to issue when spreads are tight (Amazon and Honeywell in 2026). Ratings are partly backward-looking:
Carissa notes that in 2008 many companies trading like junk were still rated investment grade. The US
itself lost its AAA, and on air only Microsoft and Johnson & Johnson (plus Apple at one agency) are
named as AAA corporates. Second-order: the BBB−/BB+ line drives forced selling when a "fallen angel" is
downgraded, because many IG mandates cannot hold high yield.

**With vs. without.** Without an underwritten syndicate, every large borrower would have to find its own
lenders, and market moves during the sale would land on the issuer. With it, the bank absorbs that
risk, which is exactly what goes wrong in a "hung" deal such as the Twitter buyout debt banks were stuck
with in 2022–23 (Gatto).

**Applies when / Breaks when.** Works for rated issuers in open markets. Breaks for small or complex
borrowers that can't be rated or syndicated, which is the opening for direct lending (§8), and when
markets shut between commitment and sale. Gornick's point: a bank can give price talk, but on pricing day
the terms can "flex" wider or the deal can die.

**Channel example.** *5. Debt Capital Markets 101: Where Do Bonds Come From?*. *Credit Trading 101*
(syndicate desk and allocation). *Private Credit Deep Dive* (Amazon's 2026 deal).

**Counterpoint.** The Amazon walkthrough is simplified to the point of error. Amazon's 2017 Whole Foods
financing was a **$16bn** multi-tranche bond, not $13.7bn, and a 2-point underwriting spread is a
high-yield number; investment-grade gross spreads run well under 1% of face. Kristen's mortgage aside says
the 10-year "went down 3.25%" in a day; a move of that size never happened, and she probably means
basis points or a yield level. The hosts admit the episode is outside their seat ("go easy on us").

**Links.** [[wss-capital-markets-ma]] (§2, the equity bookbuild, same syndicate mechanics),
[[trading-floor-mechanics]] (where the syndicate desk sits).

---

## 4 · How credit trades: dealers, quotes and the shrinking risk book

**What it is.** After issuance, corporate bonds trade **over the counter (OTC)**: no exchange, just
investors asking dealers (Goldman, JPMorgan, BofA) for a two-way price. "Credit" in trading means
corporate bonds and corporate CDS, split into leveraged loans, investment grade, high yield and
distressed, with converts and preferreds as hybrids (*Credit Trading 101*).

**How it works.** Carissa's mechanics:
- **Quoting.** IG trades as a **spread over Treasuries** in basis points; HY and distressed trade in
  **dollar price** (99 bid, 99.5 offered). Because price and yield move inversely, an IG dealer's *bid*
  spread is the higher number. Distressed paper is quoted in price because a 40,000bp spread means
  nothing; "call it 60" does.
- **Size.** Standard markets are about **$5M** in IG and about **$2M** in HY. A standard Treasury
  ticket is about $100M, so credit is a much thinner market.
- **Hedging.** An IG buyer usually sells Treasuries against the bond, weighted by DV01 (the dollar change
  per 1bp move), to isolate the spread. If the client doesn't, the dealer hedges through its rates desk.
- **Agency vs risk.** Dealers once bought bonds into inventory and worked out of them. Since Volcker
  they mostly match a buyer and seller at the same time. HY bid-ask is about half a point, but a matched
  agency trade may earn only 1/8 or 1/16.
- **Portfolio trading.** Instead of bid-wanted lists (BWICs) priced bond by bond, managers send a whole
  portfolio for one price, built off third-party pricing. Portfolio trades are about **10%** of TRACE
  volume (TRACE is the public tape of bond trades).
- **Desks.** Distressed has its own desk, staffed with lawyers reading documents, and is dominated by
  hedge funds; real money appears when it has to work out of a position.

**Business significance / value.** Market-making is what makes a bond worth more than a loan: you can
sell it. Dealers earn the bid-ask; investors pay it as the cost of exit. For issuers, secondary prices set
the level of the next deal, so traders and syndicate desks constantly compare notes on where existing
bonds trade and who holds them.

**Forces & impact.** Post-crisis capital rules and Volcker shrank dealer balance sheets. Banks that once
let a trader be long or short $50M of one bond now balk, desks are staffed by "junior risk takers" who
never traded through 2008, and the job shifted to agency matching. Electronic and algorithmic trading
make IG "more equity-like". Second-order: liquidity is now conditional. In calm markets it's cheap; in
stress, nobody warehouses risk, so prices gap. Funding costs matter again with rates high: a dealer long
a bond is borrowing to hold it.

**With vs. without.** Without dealers willing to hold inventory, bonds behave more like private loans,
easy to buy and hard to sell. With agency-only dealers, the buyer of last resort is missing exactly when
needed, which is the opening distressed and capital-solutions funds fill (§15, §16).

**Applies when / Breaks when.** The two-way market works for large, liquid issues and index names.
It breaks for small issues ($150M), off-index names, and anything in distress, where the trade happens
only at a price someone with a legal edge will pay.

**Channel example.** *Credit Trading 101* (Carissa Jordan, ex-Goldman, started on the IG desk in July
2008).

**Counterpoint.** Jen calls TRACE a post-crisis requirement; TRACE actually launched in **2002**, and
post-crisis rules expanded it and shortened reporting lags. The "tightest since 2007 with 3% defaults"
data point was true when recorded but is a snapshot. Carissa is candid that she left trading years ago
and some current-practice figures are secondhand.

**Links.** [[trading-floor-mechanics]] (desk roles, sales vs trading), [[wss-trading-hedge-funds]]
(fast money, basis trades), [[bloomberg-terminal-instrumentation]] (`ALLQ`-style dealer quotes the
program cannot see for free).

---

## 5 · Leverage, coverage, covenants & liquidity

**What it is.** **Leverage** = debt / EBITDA (EBITDA is earnings before interest, taxes, depreciation and
amortization, a rough proxy for operating cash flow). It roughly says how many years of current cash flow
it would take to repay the debt. **Coverage** = EBITDA / interest: how many times over the company can pay
a year's interest. **Covenants** are contract terms that trip when these ratios cross a line.

**How it works.** The tariff short's example: $400M debt / $100M EBITDA = 4.0x against a 6.0x covenant,
so the company is fine. EBITDA falls to $50M and leverage becomes 8.0x, a breach without borrowing a
dollar more. Caesars: $24bn / $3bn = **8x at inception**, coverage **1.5x**. By 2014 EBITDA was about
$1.5bn, $300M *below* OpCo interest alone. OpCo leverage reached 14–16x and then **18x**, coverage about
**0.5x**, free cash flow about **−$1bn** a year. Kristen's conservative variant is (EBITDA − capex) /
interest, because capex is real cash. Two covenant styles: **maintenance** covenants are tested every
quarter; **incurrence** covenants are tested only when the company acts (borrows more, pays a
dividend). Cov-lite loans carry only incurrence tests.

Who gets which: in the middle market, direct lenders insist on quarterly **financial maintenance
covenants** that the syndicated market dropped (Gornick, counterintuitively: the borrower pays a premium
*and* accepts tighter terms), though in the competitive upper middle market some direct deals now carry
none. Kroboth's non-negotiables as a special-situations lender are a covenant, downside protection, and
limits on **EBITDA add-backs** (the "adjustments" that inflate the EBITDA the ratios are tested on).

**Liquidity, not the current ratio.** Gatto's book calls the current ratio (current assets ÷ current
liabilities), standard in accounting courses, analytically meaningless as a liquidity measure; Jen reads
the passage on air. His reasons and his multi-step replacement are left as a spoiler. The usual lender
objections (not from the channel): inventory and receivables are not cash, and the ratio ignores revolver
availability, cash burn and debt maturities. A working version: cash plus undrawn committed revolver,
less minimum operating cash, set against the next 12–24 months of burn, interest and maturities.

**Business significance / value.** Covenants are the lender's early-warning system and seat at the table.
A breach forces a negotiation while value still exists, and that is the whole point. Caesars had
effectively *one* covenant that mattered (senior secured debt/EBITDA), breached in 2014.

**Forces & impact.** Competition among lenders trades covenants away for yield. Kristen ties the shift
from maintenance to incurrence covenants directly to investors reaching for spread. Gatto sorts current
deals into good, fine and bad (bad meaning the lender is not paid for the risk). In a normal market the
bad ones fail to raise money; he now sees all three getting done, his marker of the overheated phase of
the cycle. The second-order effect: without tripwires, the first sign of trouble is a missed payment or a
fraud discovery, by which point recoveries have already fallen.

**With vs. without.** With maintenance covenants, Caesars' lenders would have had leverage over Apollo
years before the asset transfers. Without them (and with the $4.5bn of old Harrah's bonds that carried
no change-of-control protection), lenders learned their position was being reshaped only after the fact.

**Applies when / Breaks when.** EBITDA-based ratios apply to steady cash-flow businesses. They break for
asset-light software where "adjusted EBITDA" is negotiable, and wherever EBITDA itself is fraudulent
(First Brands).

**Channel example.** *Tariff Fallout* (short). *Private Equity's Blueprint For Legally Stealing From its
Creditors | Caesars LBO (Pt 1/3)*. *Distressed Debt 102 (Pt 2/3)*. *What is Private Credit? | Direct
Lending Explained* (maintenance covenants). *Distressed Debt 101 with the GOAT* (current ratio, deal
tiers). *Private Credit: The Best Explanation* (Kroboth's non-negotiables).

**Counterpoint.** Kristen says a post-2008 rule capped LBOs at 6x and attributes it to "when Obama came
in" or "the SEC". It was the **2013 interagency leveraged-lending guidance** (Fed, OCC, FDIC), which
applied to banks, not to private lenders, and was softened in 2018. That is precisely why the risk
migrated to non-banks. The "years to repay" reading of leverage ignores interest and capex, so it
overstates repayment capacity. Gatto's "the current ratio is a joke" is deliberately provocative; the
ratio is crude rather than useless for a trade creditor screening thousands of small accounts.

**Links.** `learn/unit-04-is-it-healthy.md` (balance-sheet leverage),
[[canon-jensen-meckling-agency-theory]] (covenants as bonding devices).

---

## 6 · Capital structure, security & structural subordination

**What it is.** The **capital structure** ranks claims: senior secured loans, then junior/second-lien
debt, then unsecured bonds, then equity. **Senior** means first in line; **secured** means a claim on
specific assets or cash flows (Jen: security need not be a building; it can be the business's cash
flows). **Structural subordination** means a lender to a parent ranks behind lenders to the subsidiary
that actually owns the assets, because it is "further from the cash". Equity at the bottom is, in her
words, a hope that something is left.

**How it works.** Jen's image is a cereal dispenser: losses empty from the bottom up. Every bond is a
contract, and its **indenture** sets which entities guarantee it and what it is secured by (Gatto), which
is why two bonds of the same company can be worth very different amounts in default (§15). Caesars added a
legal-entity layer: a **parent** over an **OpCo** (runs the casinos) and a **PropCo** (owns the
buildings, leased back to the OpCo). The PropCo carried $6.5bn of CMBS, mortgage debt the OpCo lenders
could not touch. Kristen's Kim Kardashian analogy: a lender to the Skims business cannot foreclose on the
Calabasas house, because the mortgage lender holds it. The OpCo debt was **guaranteed by the parent**,
which gave OpCo creditors a claim on parent value. Apollo later attacked exactly that link (§14).
**Special-purpose vehicles (SPVs)** are the hidden version. Gatto: a company that pledges receivables and
inventory for a $100M revolver shows $100M of debt. Move those assets into a separate legal entity,
structure the borrowing so the accountants allow both assets and debt off the balance sheet, and the same
economic loan disappears from view. How much debt sat in SPVs was his headline First Brands red flag, and
it was Enron's.

**Business significance / value.** OpCo/PropCo splits let a sponsor borrow cheaply against real estate
(subsidized mortgage markets, a REIT's tax advantage) on top of cash-flow debt. Caesars got about two
extra turns of leverage this way. The PropCo later emerged from bankruptcy as **VICI**, a REIT that
Caesars pays more than $1bn a year in rent (Indap).

**Forces & impact.** Every new entity is a seam where value can be moved. Indap adds a modern point:
lease payments to VICI are "effectively debt", so Caesars' roughly $15bn of debt understates its real
fixed claims. The same applies to any sale-leaseback.

**With vs. without.** A single-entity borrower gives all lenders one pool to fight over. Multi-entity
structures give the equity sponsor a map of where to relocate assets. That map is the precondition for
drop-downs.

**Applies when / Breaks when.** Seniority holds in a clean bankruptcy. It breaks when documents permit
priming, layering or entity transfers (§14), when a court values the company low enough to wipe a class
out (§15), and when lease and off-balance-sheet obligations (First Brands' $10–11bn included
off-balance-sheet financing) are counted as something other than debt. Project-finance SPVs (Meta's
Hyperion data center, §18) are the legitimate use: lenders deliberately sit closer to one asset's cash
flows.

**Channel example.** *Caesars LBO (Pt 1/3)*. Indap on VICI and the lease-as-debt point in Pt 3. *Private
Equity vs. Private Credit Explained in less than 90 seconds* (short). Gatto on SPVs in *Distressed Debt
101*.

**Counterpoint.** The hosts report VICI as a "$50 million" company. They mean billions, and even then
the figure is closer to enterprise value than market cap. Kristen also says lenders "typically" take
ownership in a bankruptcy. That is true for the fulcrum class only, not senior lenders who are paid in
full. Gatto says SPVs are designed "for the most part" to hide debt; securitization SPVs also exist to
isolate assets and lower funding costs, and most are disclosed in footnotes, which is his real point:
read them.

**Links.** [[tiger-sisters-private-capital-101]] (equity view of the same stack),
`acumen/case-03-carvana.md` (ABS subordinate tranches, the securitization version of the same
logic).

---

## 7 · Public vs private credit: syndicated loans, HY bonds, bridges, CLOs, direct lending

**What it is.** **Public credit** is debt with a CUSIP (a tradable identifier) and a visible price. Findley:
if it is CUSIP'd it's public, otherwise it's private. **Private credit** is a privately negotiated loan
between a borrower (usually a small or mid-size private company) and a capital provider (an insurer, an
alternative manager's fund, or a BDC) with no intermediary in between (Gornick). It is a catch-all:
direct lending, opportunistic and special-situations credit, mezzanine, infrastructure, real estate and
venture debt, and asset-based finance all qualify, with very different risk. And it is old: insurers
were making private placements to mid-size companies in the 1980s. Traditionally a bank arranged a
**syndicated loan** and parcelled it out to other banks and to **CLOs** (collateralized loan
obligations, vehicles that pool about 200 leveraged loans and sell tranches against them). Big deals
added **high-yield (junk) bonds** for issues above roughly $200–250M, with a **bridge loan** from the
banks covering the gap until the bonds sold. **Direct lending** replaces all of that with one lender, or
a small club, that originates and holds the loan.

**How it works.** Gatto lays out the three ways Silver Point earns from loans. In the **broadly
syndicated loan (BSL)** market a bank finds, structures and sells the deal and you buy a small piece,
mostly through CLOs, which buy **60–70%** of every BSL. In **private credit** you do all of it yourself,
take an upfront fee and coupons, and need to write $200–500M checks, because the borrower's reason for
coming to you is not dealing with a hundred lenders (about $16–17bn of Silver Point's $41bn). And
**distressed** (§15). The borrower's trade-off (Jen's short): direct lenders close in days rather than
weeks, and if things go wrong you renegotiate with one counterparty instead of thousands of bondholders.
In exchange you pay more: Gornick puts the premium at **150–250bp**, narrowing to about 500bp versus
325–350bp in the upper middle market (§8). Loans float at SOFR (formerly
LIBOR) plus a spread; HY bonds are usually fixed. The **CLO warehouse**: banks fund the purchase of loans
for a CLO manager before the CLO prices, earning a markup and fees, and are stuck with the "parts" if
buyers vanish (Jen's car-factory analogy). That happened in 2007–08. **EA, 2025**: JPMorgan alone
committed the **$20bn** debt package ($18bn funded at close), the largest single-bank buyout underwrite
on record. It can syndicate, issue bonds, or hold the loan on a roughly **$50bn direct-lending
balance sheet**. In 2007 TXU's $24bn of senior loans came from a dozen banks, plus $11bn of HY via
bridges.

**Business significance / value.** Value migrated from bank underwriting fees to asset managers' spread
income. Indap's point is that the labels are dissolving: Apollo-type funds buy and hold billions of
"public" deal debt, which is private credit by behaviour. Banks have come back in through direct-lending
arms and by lending *to* private credit funds.

**Forces & impact.** Post-2008 capital rules and leveraged-lending guidance pushed risk out of banks. Jen
in the 2008 deep dive: the risk-taking moved to what was called shadow banking, which "got a facelift"
and was rebranded private credit. Zero rates and then high floating rates made private loans attractive
to insurers and retail. The second-order effect is concentration. Syndication spreads one borrower across many balance sheets; a
single direct lender (or JPM on EA) holds a concentrated position. Jen: securitization exists to *reduce*
bank risk, and holding is the opposite.

**With vs. without.** Without the syndicated or CLO machine, banks could make each loan only once
(Jen: securitization is "where bonds come from"). Without direct lending, the 2023 freeze, when banks
were hung on the Twitter buyout debt and SVB failed, would have cut off credit entirely. Gatto calls
private credit the lender that steps in when banks step back.

**Applies when / Breaks when.** Direct lending wins in mid-market deals (too small for HY) and in speed-
or confidentiality-sensitive situations. It breaks when one-lender opacity hides stress (Jen: the market
is designed to obscure trouble) and when too much capital chases too few deals, compressing spreads and
diligence.

**Channel example.** *Eerie Similarities Between Record Setting 2025 LBO (EA) and 2007 TXU LBO*. *The
best explanation of why everyone is worried about Private Credit* (short). *Distressed Debt 101 with the
GOAT* and its short *Is Private Credit about to Blow Up the Economy? Michael Gatto's Honest Take*. *What
is Private Credit? | Direct Lending Explained*. *Private Credit Deep Dive: Is this 2008 all over again?*.

**Counterpoint.** Gatto's case, that private credit is countercyclical and uses moderate 60% LTV with
1:1 to 2:1 fund leverage, comes from the head of a private credit business. LTV is computed on sponsor
valuations at 20x EBITDA, so 60% LTV can still mean 7x+ leverage. Kristen guesses JPM won't hold all
$20bn, but nobody on the episode knows the structure. In the 2008 deep dive Kristen cites Gornick as
saying direct lending costs "around 100 basis points" more; Gornick's own figure was 150–250bp.

**Links.** [[trading-floor-mechanics]] (who on the floor syndicates and distributes).

---

## 8 · Direct lending mechanics: unitranche, revolvers, delayed draws and the life of a loan

**What it is.** How a direct loan to a private-equity-owned company is actually built. A **unitranche**
is a single loan, one credit agreement and one blended price, that replaces a senior loan plus a junior
loan from different lenders. Around it sit a **revolver** (a credit line the borrower draws and repays)
and often a **delayed-draw term loan (DDTL)**, committed now and drawn later.

**How it works.** Gornick (Churchill, *Direct Lending Explained*):
- **Market tiers** by EBITDA: lower middle market below about **$15M** (some say $10M), core
  **$15–75M** (or $10–100M), upper middle market above about **$75–100M**. Borrowers in each tier look
  alike, so structure follows size. The big managers' books skew larger: on air, typical BCRED-type
  borrowers had about $250M of EBITDA (Kristen).
- **Classic core structure:** senior debt to about **4x** EBITDA, junior debt another **1–2x**, so
  5–5.5x total, and the rest of the price is sponsor equity. That is a three-party negotiation.
- **Unitranche:** one lender goes from dollar one to about **5.5–7x** at a blended price, so the deal
  is two-party (lender and sponsor). It emerged around 2018–19 and became mainstream in the 2021 boom.
  The edge is speed in auctions with 20–50 sponsors bidding: a committed one-lender package lets a
  sponsor pre-empt. "Stretch senior" sits in between.
- **Revolver:** hard for non-banks, which have no deposits to fund a draw within 24 hours, so lenders
  must reserve liquidity for it.
- **DDTL:** committed for 18–24 months for bolt-on acquisitions in buy-and-build strategies; the sponsor
  pays a **ticking fee** on the unused amount and loses it if not drawn.
- **Terms:** 5–7 year maturity, about **1%** a year amortization, a small call premium early (101–102)
  and freely prepayable after. Loans are usually refinanced or repaid around **year 3–4**, mostly on a
  sale, and about **20%** of the portfolio repays each year, so origination has to keep running just to
  stay invested. A "portable" loan that follows the company to a new owner is rare and very
  borrower-friendly.
- **Price:** the premium over syndicated debt is 150–250bp. Gornick's arithmetic: on a $1bn loan, 200bp
  is **$20M** a year, real money at scale. In the upper middle market it narrows to about 500bp spread
  versus 325–350bp in an open BSL market, so large borrowers flip back to syndicated when it reopens.
- **Allocation:** Churchill splits each deal pro rata across about **50** vehicles (dedicated senior,
  dedicated junior funds that "signed up" for 100–300bp more, equity co-invest), so a $300M deal becomes
  many small positions and no fund cherry-picks. It turns down **80–90%** of what originators source.

**Business significance / value.** The sponsor buys certainty: no rating process, no syndication flex,
one price that holds, and a lender who can approve another $50–150M in two weeks. The lender captures
spread, upfront fees and covenant control. Churchill's sourcing edge is that it is often an LP in the
sponsor's funds, so the sponsor keeps calling even after being turned down; its parent TIAA supplies
"permanent capital".

**Forces & impact.** Competition from new entrants ("on fund one") and the reopening BSL market compress
spreads and loosen terms at the top end. Longer PE hold periods (now above six years versus a historical
four or five, per Gornick) slow repayments and push lenders into "amend and extend" or dividend
recaps. Regional banks were constrained after SVB, ceding the lower tiers. Second-order: scale wins.
A lender that can offer more than today's need signals it can fund the next five years of growth.

**With vs. without.** Without unitranche, a sponsor in an auction must coordinate two lenders who disagree
on price and intercreditor terms, and loses to a rival with a cleaner package. With it, one lender holds
5.5–7x of leverage, so its recovery depends entirely on its own underwriting; there is no junior lender
below it to absorb the first loss.

**Applies when / Breaks when.** Works for PE-backed, cash-generative middle-market companies where speed
and flexibility are worth 150–250bp. Breaks when the lender "taps out" and can't fund the next draw (the
borrower's risk), when the next owner asks for a more aggressive structure and the incumbent declines,
and when competition strips covenants in the upper tier.

**Channel example.** *What is Private Credit? | Direct Lending Explained* (Alona Gornick, ex-Bank of
America gaming banker and Oaktree high-yield analyst, now Churchill).

**Counterpoint.** Gornick is pitching her firm to wealth clients, and "low loss rates" describe a
market that has not been through a full default cycle at its current size. Being an LP in the sponsor's
funds is a sourcing edge and a conflict: a lender courting the next fund allocation may be slow to
enforce against that sponsor. Unitranche "efficiency" also concentrates 5.5–7x in one lender, and her own
earlier career story (Oaktree's Harrah's bonds primed by an LBO, §14) is what happens when documents are
loose.

**Links.** [[tiger-sisters-private-capital-101]] (the sponsor's side of the same deal),
[[canon-brandenburger-nalebuff-coopetition]] (direct lenders compete for deals but need each other in
clubs).

---

## 9 · Asset-based lending (and the double-pledge failure)

**What it is.** In **asset-based lending (ABL)** the lender is repaid by a pool of assets (consumer
loans, leases, invoices, purchase orders, receivables) rather than by the borrower's overall earnings.
Direct lending to a company relies on "the good faith and credit" of that company; ABL relies on the
collateral pool (Findley). Gornick draws the same line from the other side: a direct lender's "security"
is the enterprise value of the whole business, which can be mostly goodwill, while ABL has hard
collateral.

**How it works.** Findley's underwriting is a **transition matrix**. Of current loans, how many go 30
days delinquent; of those, how many cure, stay, or roll to 60. Iterate to a lifetime default estimate,
set the loan-to-value and rate off that estimate times a safety multiple, and lend where you get your
money back even under stress. She did this as a stochastic process at Morgan Stanley ABS-CDO research
and now does it on $10–40M loans. Her formative trade (Third Point, 2009): take a $100M Alt-A mortgage
bond downgraded to D, have a rating agency re-tranche it into a 60% AAA senior piece and a 40%
mezzanine piece, keep the mezz at about **10 cents** with a 5% coupon on par. Two years of coupons (5 +
5 = 10 cents) returned the purchase price, and anything after was profit. She sanity-checked the dealer's
deeply pessimistic assumptions against a chart showing 97% of mortgage defaulters default by month 60,
so a pool that had paid for five years was unlikely to default en masse.

**Business significance / value.** ABL finances fintechs, auto lenders and specialty finance companies
that are too volatile for cash-flow lending but hold predictable asset pools. Findley's further point is
that returns and AUM are inversely correlated. A $500M fund can live on $20–40M deals that the $100bn
managers cannot staff, which is her pitch for small managers.

**Forces & impact.** Collateral illiquidity forces long lockups. Findley left Third Point because 90-day
investor liquidity could not hold illiquid loans, which is the same mismatch that later hit BDCs (§12). The
failure mode is collateral that does not exist. **First Brands** (Gatto's summary): a founder-owned
(100%) auto aftermarket parts maker (wipers and the like) built by acquisitions funded in the
syndicated loan market. A routine refinancing asked for *more* debt than it had; existing holders were
positive, but new, more sophisticated eyes stalled the process, the loans fell from about 96–100 into
the 30s, and it filed. The same receivables had been pledged to several lenders ("hidden factoring"),
about **$2.3bn** of assets "evaporated", and total liabilities including off-balance-sheet financing ran
to roughly **$10–11bn**. Exposure surfaced at Jefferies' Point Bonita fund and UBS O'Connor (reportedly
about 30% of one portfolio). Lenders requested a Deloitte quality-of-earnings report, the $6bn
refinancing failed, and the company filed Chapter 11 on Sept. 28. Gatto expects hundreds of millions in
bankruptcy costs. Tricolor, a subprime used-car lender, filed Chapter 7. Zions ($50M write-off) and
Western Alliance disclosed fraud-linked loans the same week. Gatto's lesson is procedural: a red flag
(debt sitting in SPVs, §6) doesn't mean a bad deal, it means ask more questions. Silver Point analyzed
the loans and had no exposure.

**With vs. without.** ABL works only if the lender verifies and controls the collateral: lockboxes, UCC
filings, field audits. Without verification it becomes unsecured lending at secured spreads. Jen's
analogy: one house, two mortgages, two banks.

**Applies when / Breaks when.** Applies to granular, data-rich pools with long performance histories.
Breaks under correlated defaults (the CDO lesson Findley lived through, where pooled assets were not
independent) and under fraud, which surfaces "when something goes wrong" (§18).

**Channel example.** *Private Credit 101: Asset-Based Lending feat. Keri Findley*. *First Brands
Bankruptcy, Gold at Record Highs*. *The best explanation of why everyone is worried about Private
Credit* (short). Gatto's First Brands account in *Distressed Debt 101 with the GOAT*.

**Counterpoint.** Findley's returns (mid-20s unlevered IRR at Third Point, "30s" net in one quarter at
Tacora) are self-reported, and a single strong quarter says little about risk. One video says First
Brands failed to refinance "$6 million"; it was $6bn. The hosts frame First Brands as possible fraud, and
on air it was still alleged. Gatto's "you could have spotted it" is hindsight from a firm that passed;
the lenders who stayed in also had the documents.

**Links.** [[canon-akerlof-market-for-lemons]] (lenders can't see collateral quality, so the bad
borrowers self-select), `acumen/case-03-carvana.md` (auto-loan securitization).

---

## 10 · PIK (payment-in-kind) interest

**What it is.** PIK lets a borrower pay interest by adding it to the loan balance instead of paying cash.
Kristen calls it the buy-now-pay-later of interest. A **PIK toggle** lets the borrower choose cash or PIK
period by period.

**How it works.** $100 at 10% means $10 cash a year. PIK it once and you owe $110; next year's interest is
$11, then $12.10, compounding the principal. The Bloomberg data (four years of tracking, so the "four-year
high" is a since-records-began high) shows PIK use in private credit rising from about **7.7% to almost
12%**. The share of that which is **"bad PIK"** rose from about **18% to roughly 50%**. Bad PIK means the
borrower elected it after the deal closed, rather than it being structured in at signing. "Good PIK" is
lender-dictated structure: senior lenders cap cash interest to juniors, so a junior tranche might be 10%
cash plus 5% PIK.

**Business significance / value.** For the borrower, PIK conserves cash in a squeeze. For a BDC, PIK
counts as *income* but brings in no cash, so it inflates reported earnings and can fund dividends that
are not covered by cash (Indap: analysts back it out). For the sponsor, PIK buys time for the equity
option. **Medallia** shows the limit. A Thoma Bravo 2021 LBO had been PIKing; its lenders (Apollo,
Blackstone and others) refused to allow more and demanded new equity or the keys. Thoma Bravo handed
over the company.

**Forces & impact.** Rate rises on floating-rate debt raise cash interest exactly when EBITDA is under
pressure, and PIK is the release valve. Second-order: PIK delays defaults (smoothing reported default
rates), raises the eventual loss given default, because the claim has grown while the asset hasn't, and
makes BDC NAVs lag reality. Gatto's view of the accommodation game: experienced lenders give
"tender loving care" (amendments, PIK, more sponsor equity) to deals they believe in, but get paid for
it in fees and a higher rate, and move fast to de-risk the ones they don't. The question for any PIK
election is which of those two the lender thinks it is.

**With vs. without.** Without PIK, stressed borrowers default sooner and lenders take control earlier,
with more value left. With unlimited PIK, a zombie borrower compounds its debt until there is nothing
left to recover. The canary in the coal mine that Kristen remembers from 2006–07 is back.

**Applies when / Breaks when.** PIK is benign when structured in at signing for a growth company
expected to refinance. It is a distress signal when borrower-elected after closing on a no-growth
business.

**Channel example.** *What does the rise in PIK loans mean for Private Credit?* (podcast). *Why a SaaS
Company Default (Medalla) is actually a WIN for Private Credit* (short). Indap in Pt 3. Gatto on
paid accommodation in *Distressed Debt 101*.

**Counterpoint.** The Medallia short calls the default a "win" for private credit because big lenders
took control. That is spin. A default the lender forces is still a loss against par, and the short
admits that smaller managers without restructuring teams or "fancy lawyers" are the worry. The PIK
statistics' denominator (which deals, whose dataset) isn't given on air. The tracker is likely Lincoln
International via Bloomberg, which should be checked before reuse.

**Links.** [[canon-sterman-business-dynamics]] (stock-and-flow: PIK is an unpaid flow accumulating into
the debt stock).

---

## 11 · LBO leverage then vs now: Caesars, TXU, EA

**What it is.** A leveraged buyout (LBO) funds an acquisition mostly with debt borrowed *by the target*
and repaid from its cash flows. The repo has the mechanics
([[tiger-sisters-private-capital-101]]). The channel adds the cross-cycle comparison and the
sponsor-side economics.

**How it works.**

| | Caesars (2006–08) | TXU (2007) | EA (2025) |
|---|---|---|---|
| Enterprise value | $30bn | ~$45bn | $55bn |
| Equity | ~$6bn (Apollo 1.325 + TPG 1.325 + ~30 co-investors ~3.5) | ~$8bn (KKR, TPG, GS Capital) | ~$36bn (Silver Lake, PIF, Affinity) |
| Equity % | ~20% | <20% | ~65% |
| Debt | $24bn: $7bn bank loans, $6bn bridge-to-HY, $6.5bn CMBS, $4.5bn legacy Harrah's | ~$36bn ($24bn senior loans, $11bn HY) | $20bn, one bank (JPM) |
| Leverage | ~8x ($24bn / $3bn EBITDA) | ~8.5x LTM | ~7.5x |
| Outcome | Bankrupt 2015 | Bankrupt (Energy Future Holdings) | — |

Why EA needs so much equity: at **20x EBITDA** purchase price and banks lending **7–8x**, debt covers at
most 7.5/20 ≈ 37.5% of the price. The rest, roughly 62.5%, *must* be equity, which matches the 65%
reported. That is also why PE historically avoided tech: high multiples break the math. For scale, a
core middle-market buyout today runs about 5–5.5x (4x senior plus 1–2x junior), or up to about 7x in a
unitranche (Gornick, §8), so these mega-deals sit at the top of the range. Sponsor fee
extraction at Caesars: **$100M each** to Apollo and TPG as "consulting" at close, plus about **1% of
EBITDA (~$30M/yr)** in monitoring fees, typically followed by a termination fee at exit.

**Business significance / value.** Equity returns (targeted at 22–27% IRR at Caesars) come from three
levers: EBITDA growth, multiple expansion, and debt paydown. Caesars paid down only **$185M** from
2014–16 because it kept borrowing to stay alive, so the third lever ran backwards. Co-invest beat club
deals after Caesars because Apollo and TPG fought over control. One sponsor now runs the company and LPs
co-invest without paying 2-and-20 (EA has one operator, Silver Lake).

**Forces & impact.** Cheap debt and fundraising surges push deal size (2005: Toys R Us $7bn, SunGard
$11.4bn; 2007: TXU). Today the drivers are sovereign wealth equity and single-bank or private-credit
commitments. Second-order: a large equity cushion protects lenders, but it also lowers sponsor IRR, which
invites PIK, preferred structures, or fee layering to rebuild returns. Kristen suspects Silver Lake has a
preferential slice.

**With vs. without.** Thin equity (TXU, Caesars) means any shock (energy prices, 2008) wipes out equity
and moves straight into creditor fights. A 65% cushion means the equity takes the first $36bn of losses.
That's why "same leverage multiple" does not mean "same risk".

**Applies when / Breaks when.** Debt/EBITDA comparisons apply when EBITDA is stable. They break when
the purchase multiple is the risk: at 20x, a fall to 12x erases about 40% of enterprise value, which
still sits inside EA's equity. The same fall at 8x equity would not.

**Channel example.** *Eerie Similarities Between Record Setting 2025 LBO (EA) and 2007 TXU LBO*.
*Largest LBO EVER!!! Harbinger of another 2008?* (short). *Caesars LBO (Pt 1/3)*. *Skechers' $9B deal
shows why in LBOs, cash isn't always king... A Primer on Rollover Equity* (short).

**Counterpoint.** The hosts compare a regulated utility with a commodity hedge (TXU) to a gaming
franchise (EA) as if leverage meant the same thing in both. It doesn't. They also do not ask whether
EA's $36bn includes rolled-over existing stakes (PIF was already an EA shareholder), which would mean
less new cash than headlined. The Skechers short shows how common that is: 3G offered holders **$63**
cash or **$57** plus one unlisted equity unit, with rollover capped at **20%** so 3G keeps 80%. Rolled
equity counts toward the cushion but is not new money. Paramount/WBD ("$25bn buying $110bn", about 7x) is called an LBO in
substance. That's fair, but it's an analogy, not a classification.

**Links.** [[tiger-sisters-private-capital-101]], [[canon-jensen-meckling-agency-theory]] (fees paid
by the company to its owners).

---

## 12 · BDCs, semi-liquid vehicles & gating

**What it is.** Retail investors want liquidity; direct loans have none. Three wrappers bridge the gap
(*Private Credit: The Best Explanation*):
- A **public BDC** (business development company, a regulated vehicle lending to mid-size companies)
  lists on an exchange. Investors exit by selling shares to each other; the fund's cash is untouched, and
  the share price can sit far from NAV.
- A **non-traded BDC** (Blackstone's BCRED, Blue Owl's private sister fund) is bought at NAV and redeemed
  through quarterly windows, typically capped around **5%** of the fund. The manager *may* stop
  redemptions altogether.
- An **interval fund** (Cliffwater is the example) is legally required to offer to repurchase a set slice
  of shares each period, so it cannot simply shut the door.

**Gating** means limiting or suspending redemptions when requests exceed the cap.

**How it works.** Leverage arithmetic (gating short; Kristen's version in the explainer): investors put in
$100, the fund borrows $100, and it makes $200 of loans yielding about 8–9%. Illustration (not from the
channel): loans at 10%, borrowing at 6%, gives 20 − 6 = **$14, a 14% return on equity** before fees. A 5%
loss on the loan book is $10, or **10% of equity**. Indap: public BDCs run roughly 1:1 debt to equity,
non-traded ones no more than 2:1. What's in the big funds, per the hosts' reading of filings: borrowers
with around $250M of EBITDA, and **~80%** senior secured at Blue Owl versus **~95%** at Blackstone and
BlackRock.

The 2026 sequence on air, in order:
- Blue Owl turned its non-traded BDC into a **drawdown fund** in February, returning cash only as assets
  are sold. The hosts read it partly as closing an arbitrage: redeem the private fund at par, buy the
  public sister at a **~20%** discount to NAV.
- Blackstone's BCRED received about **$3.8bn** of redemption requests; senior partners put in **$155M**
  of their own money and the fund met everything.
- Oaktree also paid above its cap (about **8.5%**), backed by parent Brookfield. BlackRock and Ares
  enforced their caps. Apollo capped redemptions on its **$25bn** BDC, and the hosts report Moody's
  stripped a KKR credit fund of its investment-grade rating.
- A **$25M** BlackRock loan went from par to zero in three months, a "hangnail" against a multi-billion
  book (Jen) that still became a headline.
- **Boaz Weinstein** (Saba Capital, the activist) bid **65–80 cents** for the gated Blue Owl shares,
  which Kristen reads as a floor.

Kroboth adds two mechanics that shrink the scary numbers. First, investors over-request. If requests are
pro-rated at 7%, asking for 100% returns seven times what asking for 20% does, so headline request
figures overstate real demand for cash. Second, people redeem from the *best* funds first, the ones still
paying out at or above NAV, which he calls everybody running for the cash machine.

**Business significance / value.** BDCs are how alternative asset managers reach retail, the "only real
untapped market" (Indap). Institutions are near peak allocation, and public alt managers traded at about
**40x forward earnings** (Blackstone above $200bn market cap) on a story of growing from about $500bn to
$1–1.5trn AUM each. Fees stack: the manager's cut plus the wealth adviser's, against 5–10bp at Vanguard or
Fidelity. Jen frames the two readings: the cynic's (institutional money ran out, so retail backfills)
and the fair one (private markets were the path to wealth for the connected, and access is overdue).

**Forces & impact.** Rates, software-sector stress (heavy BDC concentration in SaaS) and fraud headlines
drive redemptions. Redemptions force gates, gates cause panic, and panic drives more requests. Kristen was
gated in Blackstone's BREIT in 2022 while moving and buying a house: wet-signature letters by mail, and a
year to get out. Second-order: the gate protects remaining holders from fire sales (the SVB lesson:
depositors ran Friday and the bank was gone by Sunday), but it breaks the retail expectation of
liquidity, which threatens the 401(k) channel. Kristen's counter: a 401(k) is the right home, because
it's the money nobody touches. The mismatch was obvious years ago, Kroboth says, and well-run managers
hold cash buffers, credit lines and a map of what takes 24 months versus five years to liquidate.

**With vs. without.** Without a gate, the first redeemers are paid at stale NAV and the last are left
holding the worst loans, a classic run. With a gate, everyone shares the illiquidity, which is what the
documents said all along. The interval fund is the uncomfortable middle: by law it must keep paying
out, so in a rush it may have to sell loans when locking the door would serve holders better.

**Applies when / Breaks when.** Works for long-horizon investors who never need the money (Harvard,
CalSTRS). Breaks for doctors and dentists sold "low risk, great returns", and whenever NAV lags secondary
prices enough that redeeming at NAV is a free option (the public-private discount). Kroboth doubts that
arbitrage works at scale, and secondary buyers stand ready to buy stakes in gated funds at a discount.

**Channel example.** *Private Credit: The Best Explanation of Exactly What's Happening* (structures,
caps, Kroboth). *Private Credit Deep Dive: Is this 2008 all over again?* (BCRED, BREIT, Weinstein).
*Private Credit GATING?!….WTF is Happening with Blue Owl, Blackstone, BlackRock and Morgan Stanley?*
(short). *The BEST EXPLAINER... BCRED or OBDC* (short). Indap in Pt 3.

**Counterpoint.** The leverage figures came partly from the hosts asking an AI. The legal cap for all BDCs
has been 2:1 debt/equity since 2018, so the 1:1 public figure is practice, not a rule. The hosts say
interval funds must allow "5 to 7%"; under the SEC's interval-fund rule the required periodic repurchase
offer is **5–25%** of shares, set by the fund. The "40%" Blue Owl redemption figure from the gating
short was flagged on air as "something like that", and the KKR downgrade is reported, not shown. Pass 1
of this note carried the bidder as "Eisenberg"; the full episode names Boaz Weinstein. Indap's view
(correction, not catastrophe) is the more defensible one: fund leverage of 1–2x is modest next to 2008
bank and CDO leverage.

**Links.** [[canon-perrow-normal-accidents]] (tight coupling: redemption terms tied to illiquid assets),
[[canon-thaler-sunstein-nudge]] (Indap: gates as a forced nudge against selling at the bottom),
[[wss-private-markets-wealth]] (the wealth-channel distribution side).

---

## 13 · The insurer balance-sheet model (and related-party risk)

**What it is.** Asset managers buy or build life insurers because insurers collect premiums today against
payouts decades away and need long-dated, yield-paying assets. The manager can originate those assets
itself: a private equity deal, financed by its own private credit, sold to its own insurer, earning fees
at every step. Apollo/Athene is the template.

**How it works.** Capital charges (Jen's figures): investment-grade bonds about **1–2%** (about 50x
leverage on the insurer's capital), riskier loans **6–7%**, common equity about **30%**. Investments in
**related parties** require more capital and disclosure, and they are capped. **Delaware Life**, an
insurer tied to Mark Walter's TWG and managed by Guggenheim, reported **$1.4bn** of related-party
investments, then after a DOJ probe revised the figure to **$17bn**, about **39%** of its portfolio and
well above the cap. Walter bought the Lakers at a **$10bn** valuation in October and agreed to sell
within the year at **$12.5bn** to Josh Kushner (Thrive) and Bob Iger. The market inferred a forced unwind
to repay insurer loans. Jen also reports a related insurer group restructuring away its voting stake 18
months before the subpoenas, which reclassified about $2.5bn as unaffiliated, and political donations
tied to a Kansas insurance-regulation delay. All of this is reported, not charged.

**Business significance / value.** This model is the cheapest, stickiest funding source in private credit
and a large part of the post-2008 growth of alt managers. Value is captured three times: origination fees
(the bank arm), management fees (the asset manager), and spread (the insurer).

**Forces & impact.** State-level insurance regulation, capital-charge arbitrage, and the
illiquidity of what the insurer holds. Second-order: the insurer's policyholders become unknowing
lenders to the manager's own deals, and risk becomes *concentrated* in correlated counterparties. Kristen
draws the CDO parallel of assumed zero correlation.

**With vs. without.** Without captive insurers, private credit would have to raise every dollar from
third parties at market terms. With undisclosed related-party lending, the insurer "really just owned
Mark Walter" (FT reader comment quoted by Jen), so policyholder security depends on trophy-asset values.

**Applies when / Breaks when.** Works with arm's-length assets and honest disclosure. Breaks when assets
are related-party, illiquid, and must be sold in a down market, and when the regulator is captured.

**Channel example.** *Why the Lakers Sale to Kushner & Iger is ACTUALLY the Craziest Private Credit
Scandal of the Year*. *The TRUTH about the LA Lakers $12.5Bn Sale* (short).

**Counterpoint.** Jen labels the episode "conspiracy corner" herself. The forced-sale thesis is inference:
a 25% markup in a year on a scarce NBA franchise also fits an opportunistic seller. No charges had been
filed on air. The Madoff framing is clickbait, and the hosts concede no Ponzi is alleged.

**Links.** [[canon-akerlof-market-for-lemons]], [[canon-jensen-meckling-agency-theory]] (manager vs
policyholder).

---

## 14 · Liability management & creditor-on-creditor violence

**What it is.** **Liability management exercises (LMEs)** are out-of-court transactions in which a
distressed company and some creditors restructure debt in ways that leave other creditors worse off.
Three names for one thing (Gatto): LME is the lawyers' term, **creditor-on-creditor violence** the
press's, and "position enhancing transactions" a law firm's attempt at spin that never caught on.
Lenders hold only contractual rights; the board's fiduciary duty runs to shareholders. So anything the
documents don't forbid is fair game (*Caesars Palace Coup*, read on air).

**How it works.** Gatto's worked **uptier** (*Distressed Debt 101*). A sponsor buys a company for **$3bn**:
$1bn equity, **$2bn** broadly syndicated senior secured loan, held mostly by CLOs. In the old mindset
every holder of that loan was a musketeer, one for all. The document says no new debt can rank ahead
of or alongside it, but like most loan documents it can be amended by a simple majority (sometimes
two-thirds).
1. The company underperforms and needs **$200M** of new money.
2. A majority of lenders votes to amend the document to allow **$1.2bn** of new debt *senior* to the
   existing loan. So far everyone is diluted equally.
3. The same majority provides the $1.2bn. **$200M** goes to the company; the other **$1bn** buys back the
   majority's own old loans at a small discount (say 95).
4. Result: the majority now holds $1.2bn of super-senior debt. The minority holds the remaining **$1bn**
   of old loan, now *junior* to $1.2bn, and its price drops from about **85 to 30**. Same company, same
   cash flows; only the ranking changed.

For a distressed fund on the winning side the arithmetic is better still: buy the loan at 60, exchange
it at a discount into 85 of new money that ranks ahead of everyone, and that 85 behaves like par.

The **Caesars** playbook, the template, in order:
1. **Open-market buybacks** of bonds at discount (50 cents retires $1). Efficient, but it creates
   **cancellation-of-debt income**, taxable, which the company could not pay. The 2009 stimulus let it be
   deferred (the hosts say "got rid of"; it was a deferral).
2. **Uptier exchange**: offer holders of $100 of later-maturing debt about $80 of new debt that is
   *senior*, with a higher coupon and a later maturity. Participants move up; non-participants are
   pushed down.
3. **Drop-down to a clean affiliate**: Apollo and TPG created **Caesars Growth Partners (CGP)**, which
   had no legacy debt, and had it buy assets from the OpCo. Planet Hollywood plus one other casino went
   for **$350M**, with a stated value of $360M that management projected to reach **$830M** within three
   years. The online gaming business went for **$525M**, projected at **$820M**. The projected gain was
   about **$775M** (470 + 295 ≈ 765, close enough), and the projections were shown to the board **one
   month after** closing. Evercore's fairness opinion did not update for Britney Spears' residency. A later
   four-property sale targeted **$2bn** cash and cost the OpCo **$3bn** of revenue and **$700M** of EBITDA.
   Junior bonds fell to **12 cents**.
4. **Guarantee release**: OpCo debt was guaranteed by the parent only while the OpCo was wholly owned.
   Apollo sold a minority stake (options on OpCo shares) to friendly investors, so the OpCo was no longer
   wholly owned, and argued the guarantee fell away.

Gornick saw the precursor from inside Oaktree: it bought newly issued Harrah's bonds, and shortly after,
the buyout put "a massive amount" of new debt ahead of them through an opening in the documents.

Later variants: **J.Crew** (a provision let the company move valuable assets, its intellectual property,
away from lenders' collateral) and **Serta** (a non-pro-rata uptier). Indap's modern form: in a cov-lite
loan-only structure, two groups of *equal* first-lien lenders bid to provide rescue financing; the winner
**rolls up** its old debt into a new super-senior class and the losers drop "four steps" back.

**Business significance / value.** LMEs transfer value from non-participating creditors to equity and to
participating creditors, legally if the documents allow and short of **fraudulent conveyance**. Value is
captured by whoever has the best lawyers, the most capital to fund the new money, and the earliest seat
at the table. Funds on the right side post "supercharged" returns; the cost is paid by passive holders:
CLOs, small managers, retail BDCs. Gatto's blunt advice to the losers is "Know what you agree to."
LMEs also create trades: when Bausch Health's secured bonds sold off on fear of being LME'd behind the
term loan, Silver Point bought them, judging the feared transaction would not happen.

**Forces & impact.** Gatto gives three causes. A cultural change after 2008: sponsors used to boast that
no senior secured lender lost money with them, and after 2008 protecting their own LPs came first.
Sponsors also hired the best lawyers to build borrower-friendly escape hatches into documents. And
small lenders couldn't push back: a CLO taking $5–10M of a $1bn deal won't read a 300-page agreement
or demand changes, because it is being "done a favor" by getting any allocation. Add cov-lite documents,
loan-only stacks, and big managers on every side of every deal (Oaktree was there to "drink the blood
of Apollo" and is also a PE firm). Second-order effects: first-lien recoveries fall (about 80 to about
60 cents, Moody's via Indap); borrowers put aggressive funds on **disqualified-lender lists** (First
Brands blacklisted Apollo, partly for its LME reputation and partly because Apollo owns rival Tenneco and
would have seen the data room); lenders now negotiate anti-LME "blockers". Gatto expects LMEs to stay
"part of the docs" as long as capital chases deals, and says it is much more a syndicated-loan problem
than a private-credit one.

**With vs. without.** Without LMEs, a distressed company files and the absolute priority rule
distributes value by rank. With them, rank is renegotiated before court, and seniority becomes a
starting position rather than an entitlement. In 2008 CLOs survived because they were senior secured and
everything below took the pain first (Gatto); a "senior secured" lender who wakes up behind $1.2bn of new
debt has no such cushion. In Caesars, the courts and an involuntary filing by junior creditors ultimately
reversed much of it.

**Applies when / Breaks when.** LMEs work when documents are loose, a majority can be co-opted, and the
lender group is large and anonymous (syndicated loans, bonds). They break in court when the transfer
looks like fraudulent conveyance, when the fairness process is visibly conflicted, or when excluded
creditors band together, as Oaktree and others did with an involuntary petition. Serta shows how
fragile the legal ground is. Judge Jones (Southern District of Texas) approved the uptier and the
company emerged on that basis. Jones later resigned over an undisclosed relationship with a lawyer who
appeared before him. Then the Fifth Circuit ruled on New Year's Eve (2024) that the deal did not fit the
document's open-market-purchase exception. They also break in small private clubs: Gornick and Kroboth
argue that two to eight like-minded lenders who will meet again rarely turn on each other, and Kroboth
avoids the issue by being sole lender. His reasoning: LMEs are common "because it's possible".

**Channel example.** *Distressed Debt 101 with the GOAT* (Gatto's uptier, Serta, J.Crew, Bausch).
*Distressed Debt 102: When Debt Investors Turn On Each Other | Caesars Pt 2/3*. *What is Private Credit?
| Direct Lending Explained* (Harrah's priming). *Why did First Brands BLACKLIST Apollo from its list of
lenders?* (short). *Financial Times reporter: How Private Credit Has Changed Since 2008…and Gotten
Riskier* (short). Indap in Pt 3.

**Counterpoint.** The hosts treat Apollo as a near-cartoon villain while admitting it was
"vindicated": Caesars did recover once the debt was gone, and the recovery went to the creditors. LMEs
can also preserve going-concern value that a premature filing would destroy, part of why Gatto calls
them a fascinating subject rather than an evil. Indap calls true creditor-on-creditor fights "still relatively
limited". The bigger driver of lower recoveries is simply that loans now form more of the stack.
Kroboth's claim that Apollo is now "much more boring" comes from a peer, not an audit, and the club
argument is untested in a deep downturn.

**Links.** [[canon-jensen-meckling-agency-theory]] (asset substitution and claim dilution, the
debt-side agency costs), [[canon-schelling-strategy-of-conflict]] (coalitions and commitment among
creditors), [[canon-axelrod-evolution-of-cooperation]] (why cooperation holds in repeated private
clubs and unravels among anonymous syndicate holders).

---

## 15 · Distressed investing, valuation fights & bankruptcy

**What it is.** Three different things (Caesars Pt 2). **Distressed investing** is a strategy: buy debt
someone else lent, now trading at a material discount (80, 70, even 10 cents), and profit either when it
recovers toward par or by converting it into control. **Restructuring** is the negotiation to save a
struggling company: asset sales, exchanges, LMEs. **Bankruptcy** is court: **Chapter 11** reorganizes and
keeps the company running; **Chapter 7** liquidates it (First Brands filed 11; Tricolor filed 7). Gatto's
framing: about 80% of the skill set is ordinary corporate investing (industry, business, model); the
other 20% is the bankruptcy code, documents and negotiation.

**How it works.** Gatto's strategy spectrum (*Distressed Debt 101*):
- **Pull to par.** Buy at 82, clip the coupon, get repaid at 100 because the company never files. The
  return beats a loan bought at 98 for the same credit.
- **Distress for control.** Buy debt you expect to become the equity. Men's Wearhouse (Gatto groups it
  with Jos. A. Bank; both sat under Tailored Brands) in COVID: senior secured debt at **30–50 cents**, below what Silver Point thought liquidating
  inventory and owned real estate would return. Downside: cost back plus a little. Upside: convert to
  equity, inject liquidity, and ride the pent-up demand for weddings, tux rentals and new work clothes.
  It worked.
- **Capital-structure relative value.** Two bonds of one company trade together, but the documents make
  one better. Lehman had bonds with a **double-dip** claim (two recoveries from the estate). The dispute
  settled at **1.8x** the normal bonds' recovery without a trial, and the other side agreeing to 1.8
  told you who would have won. The edge is finding a lawyer who isn't conflicted, since every big firm
  represents someone in the case.
- **LME plays.** Position for, or against, a feared transaction (§14).

Apollo and TPG at Caesars ran distress for control too: about **$70M** for **$300M** face of Planet
Hollywood's junior mortgage debt, converted into a controlling equity stake by early 2010. **Debt as
quasi-equity**: Paulson bought Caesars unsecured bonds at about **66 cents** and swapped about **$1.1bn**
face for **16%** of the parent at a **$4.5bn** equity value. Check: 0.16 × $4.5bn = $720M, against a cost
of about 0.66 × $1.1bn ≈ $726M, so he swapped at almost exactly his cost basis.

**Valuation fights.** Gatto's example: $500M of secured debt, $200M of unsecured bonds you bought at 40,
betting the bonds get a recovery, probably in equity. The judge values the company at **$400M**. That is
less than the $500M secured claim, so secured lenders get 100% of the new equity and the bonds get
**zero**. Two years later the company sells for **$800M**, enough to have covered all $700M of debt. You
were right on value and still got nothing. Most fights settle (say 90/10) before a judge rules.

**The bankruptcy toolkit.** In Chapter 11 a company can reject or assume leases, renegotiate union
contracts, and emerge with much less debt, often with some creditors as the new owners, effectively the
new private equity sponsor. Filing also freezes maneuvering, like someone shouting "Uno". At Caesars,
junior creditors (Oaktree et al.) filed an **involuntary** petition to freeze Apollo's moves. Outcome:
about two years of litigation, **$273M** in estate fees ($79M to Kirkland & Ellis alone), emergence
October 2017. Second-lien bonds went from cents to **65** at emergence to about **100** as Caesars and
VICI stock rallied, roughly $5bn of value. Elliott made about **$1bn**.

**Business significance / value.** Distressed funds supply liquidity to forced sellers (hung bridges
bought at about 80 cents in 2008; Third Point buying forced-sold paper in 2009) and are often the
eventual owners. Gatto's defense against the "vulture" label: distressed funds fund rescues that avoid
bankruptcy (capital solutions, §16), bring in restructuring advisers, and use the code to cut debt so the
business can hire and grow again. The **holding period** is the edge. Private equity's 7–10 year lockups
let it wait; hedge funds with short redemption terms may be forced to sell at the bottom. Blackstone held
Hilton through the crisis and made about $10bn.

**Forces & impact.** Kroboth (Northwall; the "three rules" short is his, not Gatto's): big managers now
raise **dislocation funds** that can only be drawn after preset market triggers, so risk reprices fast
and the chance to deploy a lot at 70 is brief. A good distress cycle needs a *sudden, unexpected*
shock; a foreseeable maturity wall gets refinanced, extended and nibbled away by credit funds,
capital-solutions funds and credit-secondaries funds. He waited 15 years for one. When a real
dislocation comes, LPs struggle to allocate new money because their other holdings are falling (the
denominator problem), so committed capital wins. Europe's distressed market is too small to be an asset
class, and the famous US distressed shops (Oaktree among them) have become broad credit platforms.
Gatto's forecast for the turn sorts lenders into three groups. Cycle-tested funds with workout teams
will keep lending when others stop and outperform. Decent underwriters without workout staff will
pause. Funds run by people who never saw a cycle will fail to raise again and disappear.

**With vs. without.** Without distressed buyers, forced sellers' prices fall further and companies are
liquidated instead of reorganized. With them, a default is "the beginning of a potential restructuring"
(Medallia short), not the end. Without a valuation process, the senior class would simply take the
company; with one, junior classes get a forum, and a costly fight.

**Applies when / Breaks when.** Works when you have capital, legal resources, and time. Breaks when you
are on the wrong side of the documents or the valuation ruling, when your own liquidity is short, or when
you are too early, paying carry while waiting for a cycle that is being refinanced away.

**Channel example.** *Distressed Debt 101 with the GOAT: Michael Gatto* (strategies, Men's Wearhouse,
Lehman double dip, valuation fights). *Distressed Debt 102 (Pt 2/3)*. *Private Credit: The Best
Explanation of Exactly What's Happening* and its clip *CIO of $3Bn Private Credit Firm on THREE RULES for
Making Money in Distressed Investing* (Kroboth). *Private Equity's Blueprint... (Pt 1/3)* (hung bridges,
the Rowan "you want chaos" ethos).

**Counterpoint.** Pass 1 of this note attributed the dislocation-fund argument to Gatto; the full
episode shows it is Kroboth's. The Planet Hollywood figures don't reconcile: the hosts say "50 cents on
the dollar" but also $70M for $300M face, which is about 23 cents. One number is wrong. Gatto's
heroes-not-vultures pitch is self-description, and the valuation-fight example cuts both ways: secured
holders who win a low valuation capture the later upside. The "blood in the streets" career lesson is
survivorship-biased; the hedge funds forced to sell at the bottom are the other half of the story. Kristen
argues lawyers are well placed to move into distressed; Gatto, who has no law degree, says you can learn
the legal side on the job.

**Links.** [[canon-klarman-margin-of-safety]] (forced selling creates price ≠ value; Klarman's Baupost is
a distressed shop), [[canon-mauboussin-success-equation]] (luck of timing in distressed returns),
[[canon-fisher-ury-getting-to-yes]] (most valuation fights end in negotiated splits; know your
alternative to a ruling).

---

## 16 · Capital solutions / special situations ("credit opportunities")

**What it is.** Lending into situations too complex, urgent or unusual for a bank, a direct lender or a
mezzanine lender. Kroboth places it on a ladder: plain direct lending (reasonable leverage), unitranche
(more), mezzanine (closer to equity), then special situations, which his firm rebrands "credit
opportunities". The defining feature is **situational complexity**, usually with urgency. Distressed
buys someone else's debt in the secondary market; capital solutions originates new senior debt.

**How it works.** Kroboth's examples (Northwall, ~$3bn):
- **Project North.** A UK industrial company. A PE buyer had chased it for 18 months; one of its high
  street lenders dropped out **four weeks** before closing. Northwall decided fast and closed on time, for
  extra economics. The risk was low; the price was for speed and certainty.
- **Consumer tail portfolios.** Hundreds of millions of defaulted, already worked-out bank receivables
  (overdrafts and similar) where the customer is on a ten-year payment plan. The hard work is done; what
  is left is a long annuity that the owner sells for liquidity.
- **Legal assets.** Not single-case litigation funding, which is venture-like (some zeros, some 5x), but
  loans to law firms secured on their whole case portfolio, structured as credit: downside protection,
  contractual return, fixed maturity. Last money in, first money out of any case revenue, repaid in about
  five years. One loan of about **$186M** against a book that could produce **$1–2bn** if every case won.
  The firm claims its book is worth 800, he thinks 200, he lends 30. The risk isn't losing cases (the
  portfolio diversifies that) but that lawyers are poor at running a business and run out of money. One
  case in that portfolio was the Mariana dam disaster in Brazil, which brought claims against BHP and
  Vale in English courts.
- **Terms.** The borrower trades **price and structure for speed and certainty**. Pay more, fine, but no
  compromise on covenants, downside protection or EBITDA add-back limits. Northwall lost a deal two weeks
  before the episode because the intermediary called its terms "not market"; his reply was that the only
  willing lender *is* the market.

**Business significance / value.** This is where distressed expertise went in a decade without much
distress. Kroboth's line, "Cap Solutions is the new distressed", and Gatto's description of capital
solutions lending as being welcomed by the company and sponsor because it solves a problem, say the same
thing. Returns come from complexity premia and fees, not from betting on default. Goldman closed its
famous special situations group in favor of more scalable direct lending.

**Forces & impact.** Complex deals need closed-end, locked-up funds: a tariff-refund monetization or a
law-firm loan can take 12–24 months and can never be traded out of. Legal-asset returns are uncorrelated
with markets, which is the allocation pitch (0–10% of his fund). Second-order: as plain private credit
gets crowded, borrowers who want plain-market loose terms at slightly higher prices drift into this
niche; disciplined lenders wait them out, which caps fund size (his "why we're $3bn, not $10bn").

**With vs. without.** Without this capital, a PE deal dies when a bank drops out, and a law firm or a
holder of a defaulted-loan tail has nowhere to turn. With it, those situations close, at a price, and the
lender controls the outcome as sole lender rather than hoping a syndicate behaves (§14).

**Applies when / Breaks when.** Works when complexity, not credit quality, is what keeps other lenders
away, and when the lender can hold to maturity. Breaks when "special situations" becomes a license to do
anything, which Kroboth admits is why the label got a bad name, and when complexity hides plain bad
credit.

**Channel example.** *Private Credit: The Best Explanation of Exactly What's Happening* (Fabian Kroboth,
Northwall Capital). Gatto on capital solutions in *Distressed Debt 101*.

**Counterpoint.** Every example is a winner told by the manager, and "we turn down loose deals" is
standard marketing. Legal-asset lending carries duration and ethics risk (financiers' influence over
claims) that the episode doesn't discuss. His claim that big managers have planned for every liquidity
scenario is reassurance from a peer, not evidence.

**Links.** [[professional-services-leverage]] (why law firms are cash-hungry partnerships),
[[canon-klarman-margin-of-safety]] (lending 30 against an asset you value at 200).

---

## 17 · Credit default swaps (CDS)

**What it is.** A CDS is insurance on a borrower's default. The buyer pays a running premium (the CDS
spread); the seller pays out if the borrower defaults. You don't need to own the bonds to buy
protection, so CDS can be a hedge or an outright short on a company's credit. Carissa's origin story:
CDS was built to make bondholders whole. If a bond recovers 40 in bankruptcy, protection pays the other
60, so the holder gets back par. It is now mostly a tool for views on credit and spread momentum.

**How it works.** **Elliott at Caesars** owned the debt and bought CDS against it. Sellers of short-dated
protection reasoned a fresh cash infusion made bankruptcy impossible, which amounted to doubling down on
their long. As bankruptcy approached, the protection rose in value. **Apollo at First Brands** was
blacklisted as a lender (it owns rival Tenneco and has an LME reputation), bought CDS about a year
early, and profited. **Oracle**: the OpenAI deal headlined at $300bn against OpenAI revenue of about
$13bn (Jen's figure). Oracle's operating cash flow is about a quarter to a fifth of other hyperscalers',
and its capex is debt-funded. Oracle lost about $315bn of market value from the peak, and its CDS became
the market's "anti-AI trade": a liquid, cheap way to bet against AI capex, widening about 95bp against
about 40bp for CDX IG.

**Market structure** (*Credit Trading 101*). The five-year contract is the liquid, "on-the-run" point.
When Carissa traded (Frontier Communications bonds and CDS together), hundreds of single names traded,
quoted from 1 to 10 years. Now the liquid products are the **indices** (CDX IG, CDX HY, a financials
index coming), and single names trade only if they sit in an index. Prop desks and bond-vs-CDS basis
traders have largely gone, bank CVA desks (which hedge the bank's own counterparty risk) remain, and some
dealers have stopped making markets in single-name CDS altogether.

**Business significance / value.** CDS let banks and funds hedge concentrated loans and let skeptics
express a view. Wider CDS feeds back into borrowing cost. Kristen notes Oracle can route around it
through **project finance**, where a data center's own cash flows support the debt rather than Oracle's
credit (the reverse of Meta, which borrows more cheaply as a corporate).

**Forces & impact.** CDS changes creditor incentives. A bondholder hedged with more protection than bonds
is a net-short "empty creditor" who gains from default, which reshapes restructuring alliances (Caesars
Pt 2). Reflexivity: buying a company's CDS widens its spreads and makes refinancing harder, so it is
unclear which came first, the CDS or the egg. Kristen likens it to insuring a neighbour's house and then
driving into it.

**With vs. without.** Without CDS, lenders could only hedge by selling the loan, and skeptics could
only short equity. With CDS, credit risk is priced continuously, but someone with no economic interest in
the company's survival can sit at the restructuring table.

**Applies when / Breaks when.** Works for liquid names with standardized contracts. Breaks in private
credit (no CDS on a direct loan, hence the hunt for proxies like Oracle), for off-index single names
where nobody makes a market, and when protection sellers cannot pay (AIG, 2008). The irony Kristen
notes: a product invented so bondholders could protect a specific name now barely trades by name.

**Channel example.** *Oracle CDS: the "Anti-AI Trade"*. *Why Apollo Was Blacklisted By First Brands*.
*Distressed Debt 102 (Pt 2/3)*. *Credit Trading 101* (index vs single name). Related: *The TRUTH about
AI Data Centers* (short): Nvidia backstopping
about $250bn of a $527bn OpenAI build that sends it about $400bn of revenue, vendor credit that a CDS
skeptic would price.

**Counterpoint.** Oracle CDS widening is partly hedging demand, so it measures how many people want an AI
hedge as much as Oracle's default risk. The hosts say this, which is to their credit. The "$300bn"
contract is multi-year and conditional, so set against one year of OpenAI revenue it overstates the
mismatch. The data-center short's cost build is a creator's estimate.

**Links.** [[bloomberg-terminal-instrumentation]] (`CDS`, `SOVR`, `WCDS`, with no free equivalent),
[[tiger-sisters-stock-picking]] (2008 CDS), [[canon-taleb-black-swan]].

---

## 18 · Private credit vs 2008: same song, different instruments

**What it is.** The systemic question: is private credit's stress (gates, PIK, fraud, markdowns) a repeat
of 2007–08 or a contained correction?

**How it works.** **What rhymes.** Too much money chasing too few deals, looser covenants, PIK toggles
(back from 2006), opaque marks, retail distribution, and correlation assumed away (Kristen on CDOs: when
it goes bad, it goes bad everywhere). Fraud surfaces when the cycle turns: Madoff, First Brands, Tricolor,
the $2.6bn naked-short Treasury trader whose trade cost dealers about $250M when COVID moved rates 50bp
against him (≈ $4.2M DV01 × 50bp ≈ $210M by Kristen's estimate). Indap: first lien means something
"a lot different" now. **What differs** (Indap). Banks matter less and asset managers more. BDC leverage
is 1–2x, not 30x. Corporate leverage in software is nothing like the 2006 housing bubble. In 2008 the
*underlying* assets (subprime mortgages) were bad, re-levered through MBS, CDOs and CDO-squared. Kristen's
2007 CLO loans were mostly fine. The question is whether today's corporate loans resemble the loans of
2008 or the mortgages. Kristen's chain for 2008: "NINJA" loans (no income, job or assets) with
adjustable rates, pooled into MBS, re-pooled into CDOs and CDO-squared, much of it held by the same banks
that made the loans. Jen's: one web of institutions doing lending, liquidity and risk-taking at once.
Today's equivalent sits in pensions, endowments, insurers and other funds with long horizons, so
direct household exposure is small; the channels are pensions' marks, banks lending to funds, and
sentiment spreading to public spreads. **The new inversion**: high-yield bonds (unsecured, larger BB issuers) yield about
6–8%, while "senior secured" leveraged and private loans yield 9–11%. That is not an arbitrage if the
loan borrowers are worse companies, and they are. Smaller funds are easier to raise, so more money now
flows to the *lowest* credit quality.

**Business significance / value.** For allocators: Global Alts private-credit meetings fell from
**3,200 to 3,000**, cooling rather than an exodus. Public credit meanwhile boomed: the record 2026
investment-grade issuance day (Amazon, Honeywell) was oversubscribed while BDCs were gating. Kristen's
read is a flight to quality *within* credit. Amazon won't be "SaaS'd away"; a middle-market software
borrower might. Data-center finance shows the same split: CoreWeave and Oracle reportedly couldn't fund
one project, while Meta's Hyperion raised money against Meta's lease payments plus the building itself. Interest is shifting to long/short, relative value and
macro. For the big alt managers: their valuations assumed the model survives a real credit cycle, which
it hasn't faced since 2009. Indap's summary: correction, not catastrophe, but real pain for the sector.

**Forces & impact.** Retail and 401(k) access push supply. Sticky rates and SaaS disruption (AI) press on
the software-heavy loan book. Gates educate investors the hard way. The $53bn-fund strategist's quip:
private equity praising private credit is like Chick-fil-A's cows, because if you're in the credit, your
equity has already been wiped out. Kroboth's diagnosis: a liquidity crisis set off by real but
limited credit worries. The software scare triggered it, though some of the worst markdowns (the
BlackRock fund) were old non-software loans. Jen adds the cynic's label for private marks, "volatility
laundering", and the counter that patient capital sometimes really does work a loan out.

**With vs. without.** Without private credit, Gatto argues, bank pullbacks cascade into deeper
downturns. His 2023 case: banks were stuck with the Twitter buyout debt they couldn't sell near par, SVB
and other regional banks failed, and the Fed was raising rates into inflation; the large private lenders
kept doing good deals, and nobody would bail out the ones that did bad deals. Without regulatory reach into private credit, the risk the 2008 reforms pushed out of
banks sits with insurers and retail, and nobody has watched it through a downturn.

**Applies when / Breaks when.** The "contained" view holds if losses stay in software and mid-market
loans and fund leverage stays modest. It breaks if insurer balance sheets (§13) or bank lending *to*
private credit funds transmit losses, which is the inter-connection Indap says nobody yet knows. Both
hosts end on the same split verdict in the deep dive: private credit probably isn't the domino, but oil,
unemployment and a shakier property market could still produce a 2008-scale downturn around it.

**Channel example.** *Private Credit Deep Dive: Is this 2008 all over again?*. *Private Credit: The Best
Explanation of Exactly What's Happening*. *Distressed Debt 101 with the GOAT* (Gatto's 2023 case).
*Financial Times Reporter TELLS ALL: Why Private Credit is Worse than Credit in 2008*. *Is Private Credit
Fundraising OVER? We're LIVE from MIAMI!*. *Private Credit GATING?!* (short). *Chief Strategist of $53
Billion Hedge Fund* (short).

**Counterpoint.** Kristen says 2008 corporate defaults "peaked at like 2%" and CLO investors did fine,
and repeats it to Gatto, who doesn't correct her.
Spec-grade defaults actually peaked near **10–14%** in 2009 (Moody's/S&P loan and HY series). CLO
*senior* tranches survived; equity and mezzanine took real losses, and the "investors made out like
bandits" story applies to those who bought at the bottom. The Carlyle short's claim that "alternatives" is
an archaic word, because listed US companies shrank from about 5,000 to about 3,500, is a sales pitch for
retail allocation.

**Links.** [[canon-perrow-normal-accidents]], [[canon-taleb-black-swan]], [[canon-akerlof-market-for-lemons]].

---

## How the concepts connect

```
 DCM: Treasury + spread → bond born (3) ──► dealers make markets, now as agents (4)
        │                                        │ (thin balance sheets: liquidity is conditional)
        ▼                                        ▼
cheap money / yield-based buyers ──► spreads compress (2) ──► lenders compete on terms
        │                                                     │
        ▼                                                     ▼
 LBOs at 7–8x on 20x multiples (11);        cov-lite + add-backs + PIK toggles + unitranche /
 middle-market unitranche to ~7x (8)        loan-only stacks; "bad deals" get done (5,10,6,8)
        │                                                     │
        └──────────► rates rise / EBITDA falls / AI scare ◄───┘
                              │
          ┌───────────────────┼────────────────────┐
          ▼                   ▼                    ▼
  PIK elected (10)    covenant tripwires absent   fraud / SPV debt surfaces (6, 9: First Brands)
          │                   │                    │
          ▼                   ▼                    ▼
  BDC income ≠ cash;   LMEs: majority uptiers,      spreads/CDS widen (2,17)
  NAV lags (12)        drop-downs, roll-ups (14)     │
          │                   │                    ▼
          ▼                   ▼             refinancing fails → Ch.11/Ch.7 (15)
  redemptions > cap     first-lien recovery          │
  (over-requested)      ~80→~60c (1)                 ▼
  → gate / drawdown /         │             valuation fight decides who owns it (15)
  forced interval-fund        ▼
  sales (12) ──────► forced sellers ──► distressed buyers, dislocation funds,
                                         capital-solutions lenders (15,16)
                              │
                              ▼
     transmission risk: insurer balance sheets (13), bank loans to funds, pension marks (18)
```

The loop that matters most: **loose terms during tight spreads decide the recovery during wide
spreads.** Everything from PIK to LMEs is a cheap-money-era clause being exercised in a squeeze. Pass 2
adds a second loop: **the size of the lender group decides how violent the squeeze gets.** Anonymous
syndicated holders (CLOs taking $5–10M of a $1bn loan) get uptiered; a sole lender or a small repeat
club with maintenance covenants negotiates early (§8, §14, §16). And a third: **whoever has committed,
locked-up capital when sellers are forced sets the price**, which is why dislocation funds and gates
both exist (§12, §15).

---

## Retrieval questions

1. **A company's 10-year Treasury rate falls 50bp after a tariff shock, but its own borrowing cost rises.
   How?** *The base rate fell on flight to safety, but the credit spread widened by more because default
   risk rose through input costs, demand and retaliation.*
2. **Leverage is 4x against a 6x covenant. Without borrowing more, what EBITDA decline breaches it?**
   *A one-third decline: debt/EBITDA = 6 at EBITDA = 4/6 of the original. Breaches come from earnings,
   not just borrowing.*
3. **Why does EA's 7.5x leverage carry less lender risk than TXU's 8.5x, beyond the 1-turn gap?** *A 65%
   equity cushion versus under 20%: equity absorbs the first ~$36bn of value loss. At 20x purchase and
   7.5x debt, the math forces the cushion.*
4. **A BDC reports rising net investment income while its cash interest receipts are flat. What do you
   suspect, and why does it matter for the dividend?** *PIK income is booked but not received, so the
   dividend may be funded by non-cash income and NAV may be overstated.*
5. **Distinguish "good PIK" from "bad PIK".** *Good PIK is structured in at signing (often to fit
   seniors' cash caps). Bad PIK is elected by the borrower after closing to conserve cash, and it signals
   stress. The bad share rose from ~18% to ~50%.*
6. **Why did Caesars' parent guarantee matter, and how did Apollo attack it?** *It gave OpCo creditors a
   claim on parent value. Selling a minority OpCo stake broke "wholly owned" status, which Apollo argued
   released the guarantee.*
7. **You hold first-lien debt in a cov-lite, loan-only structure. Name two reasons your expected recovery
   is lower than a 2008 first-lien holder's.** *No junior bonds below to absorb losses, so recoveries are
   shared across a larger first-lien class; and uptier/roll-up LMEs can push non-participants behind a new
   super-senior class.*
8. **Why can a gate be in the remaining investors' interest?** *It prevents fire-sale liquidation of
   illiquid loans to pay early redeemers at stale NAV. It shares the illiquidity instead of transferring
   losses to those who stay.*
9. **Why might an investor buy a company's CDS rather than lend to it, and how can that change the
   company's fate?** *To short credit or hedge without exposure. Wider CDS raises refinancing costs
   (reflexivity), and net-short holders gain from default, which changes restructuring alliances.*
10. **Paulson swapped $1.1bn face of Caesars bonds for 16% of a $4.5bn equity value. Was the swap rich or
    fair to him at the time?** *About fair at cost: 16% × 4.5 = $720M versus ~$726M paid (66c). He was
    buying optionality on a recovery, not a discount.*
11. **Kroboth says a known maturity wall is a poor distressed setup. Why?** *A foreseeable problem gets
    refinanced, extended and nibbled by capital-solutions, secondaries and dislocation funds. Only a sudden
    shock forces real fire sales.*
12. **Why is the insurer-owned asset manager model both private credit's best funding source and its
    likeliest transmission channel?** *Low capital charges (~1–2% on IG) and long-dated liabilities make
    it cheap, sticky funding. Related-party, illiquid assets concentrate policyholder risk in the
    manager's own deals (Delaware Life: $1.4bn → $17bn, 39%).*
13. **A sponsor pays a direct lender 150–250bp more than syndicated debt and accepts quarterly
    maintenance covenants. What is it buying?** *Certainty and speed: no rating process, no syndication
    flex, one committed price that can pre-empt an auction, and a small lender group that can approve
    add-on money or an amendment in days. The covenants are the price of that relationship.*
14. **An IG dealer quotes a bond at 118/115. Which side is the bid, and why does the HY desk quote 99/99.5
    instead?** *118 is the bid: a higher spread means a lower price, which is where a dealer buys. HY and
    distressed trade on dollar price because credit risk, not rates, drives the value, and huge spreads
    are meaningless as quotes.*
15. **In Gatto's uptier, the minority's loan falls from 85 to 30 though the company's cash flows haven't
    changed. What changed, and what document feature allowed it?** *Its rank: $1.2bn of new debt now
    sits ahead of it. A simple-majority amendment right let the majority permit senior debt and then use
    the new money to retire its own old loans.*
16. **You bought unsecured bonds at 40, the company later sells for $800M against $700M of debt, and you
    got zero. How?** *A judge valued it at $400M in bankruptcy, below the $500M secured claim, so secured
    lenders took all the new equity. Being right on value isn't enough; the valuation ruling decides.*
17. **Why can an interval fund suffer worse fire sales in a rush than a non-traded BDC?** *It is legally
    required to make periodic repurchase offers, so it must keep paying out, while a non-traded BDC can
    suspend redemptions or convert to a drawdown fund and sell assets on its own schedule.*
18. **A fund announces redemption requests equal to 30% of NAV with a 7% cap. Why might real demand for
    cash be lower, and why might the *better* funds see the most requests?** *Investors over-request,
    since pro-rated payouts are a share of what they ask for. And in a scramble people pull from funds still
    paying at or above NAV (Kroboth's cash machine), not the worst ones.*
19. **Kroboth lends $30M against a law firm's case book the firm values at $800M. What is he actually
    underwriting?** *Not the cases (diversification handles that) but the firm as a business: will it
    overspend and run out of money before cases pay, and is he first money out with a fixed maturity?*

---

## Gaps (what is still missing)

Pass 2 recovered all six priority long-form episodes (Gatto, the two 2026 deep dives, Direct Lending,
Credit Trading 101, DCM 101) and the two missing shorts (PE vs private credit; the Apollo blacklist), plus
the Skechers rollover short from the old gap list. Checked against `/Users/kalvaryhawkins/wss_all_videos.json`
and `wss_all_shorts.json`, these credit-relevant items still have no transcript:

**Shorts**
- *Largest Debt Commitment in History for LBO by ONE BANK. 2008 All Over Again?* (`fZQP_mQ_2sg`), part 2
  of the EA short, on what "underwriting" JPMorgan's $20bn means (§11)
- *Paper LBO must know for PE interviews* (`J9xh-sNosSM`), LBO return arithmetic

**Referenced on air but not in the YouTube catalog** (likely podcast-only)
- The promised **part 2 of the gating short** (whether the underlying loans are toxic)
- The **2023 original Indap interview** referenced in the Caesars series
- The **Barclays credit strategist** interview Carissa and Jen cite for the "wall of cash" spread argument (§2)
- The **Goldman perpetual/evergreen funds** episode (Chris Nelson) cited in the BDC discussion (§12)
- The upcoming **fixed-income replacement** conversation (Brian Weinstein), on what's actually inside
  "IG-replacement" private credit portfolios
- Gatto's **First Brands red-flags paper**, offered via the hosts' newsletter (an external document, not a
  transcript)

**Routed elsewhere, read for pass 2, belongs in sibling notes:** *Cash Free Debt Free* (`rtU0nzvHDno`)
and *LBO in Under 3 Minutes* (`QFD4WRoax2g`) are LBO interview mechanics for
[[wss-private-markets-wealth]] / [[wss-technicals-career]]; *How do bonds work?* (`NpaENGQk18M`,
duration and DV01) is rates material for [[wss-rates-macro]]. The basis-trade and bond-market episodes
(`BDzC3h0vgwA`, `zCC7YTQ3b-M`) are in the rates-macro cluster.
