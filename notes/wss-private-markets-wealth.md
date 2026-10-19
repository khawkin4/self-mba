# Private markets & the wealth channel: how the money is pooled, priced, levered and sold (Wall Street Skinny)

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-capital-markets-ma]] [[wss-credit-distressed]] [[wss-rates-macro]] [[wss-technicals-career]] [[wss-trading-hedge-funds]]

> **Sources:** 49 files: 32 long-form videos and 17 shorts. Pass 1 used 22 (15 videos, 7 shorts). Pass 2 added 26 cluster files (17 videos, 9
> shorts) plus the Skechers rollover short routed elsewhere. Three shorts have no usable speech ("In Private Equity it's called Leverage", "Step by
> Step: How to Break into PE", "Working Backwards"), and four pass-2 videos were read with little or no change (PE Associate Tell-All, the contrarian
> long/short PM episode, the real-estate-news episode, Project Finance 101, which is mostly a career story). Raw at
> `_ingest/raw/2026-10-04/media/wall-street-skinny/` (cluster `private-markets-wealth`). Guests: Neha Shah (Head of PE Solutions, Morgan Stanley
> Investment Management), Kristen Olson (Head of Alternatives for Wealth, Goldman Sachs), AJ Tracy (lower-middle-market PE, ex-Canaccord/CIC),
> Mike Dorrell (CEO, Stonepeak), Lauren Hochfelder (co-CEO, Morgan Stanley Real Estate Investing), Deborah Smith (CEO, CenterCap), Keri Findley
> (founder, Tacora Capital), Jesse Sapphire (owner of ABG Print, self-funded searcher), Alicia Levine (BNY Wealth), Alex Cavalier (CAIS).
> Pass 2 adds: Justin Resnick (MD, Evercore Private Capital Advisory; secondaries ×2), Paul Dodd (Head of Go-to-Market Operations, Sixth Street),
> a Bain Capital Portfolio Group SVP (PE 102), Shane Clifford (Global Head of Wealth, Carlyle), Tony Abatti (CEO, SCS Financial, an RIA), Susan
> Moffett (co-founder, Curated Wealth Partners, a multi-family office), Camilo Acosta (pre-seed AI fund manager), the FareHarbor founder (Mark Cuban
> episode), Eli Manning and David Adelman (Sixers/Devils/Crystal Palace co-owner, FS Investments co-founder), and the ex-Morgan Stanley/Carlyle energy
> team (project finance). Plus the hosts' Caesars LBO, FT-leverage, comp, Yale-sale and endowment episodes. Paraphrased in my own words. Quotes are
> brief and attributed. Several pass-2 transcripts are machine-translated or poorly captioned; names are given as best reconstructed.
>
> **Maps to:** Course **02** (Corporate Finance & Valuation: fund math, IRR versus multiple, cap rates), **06** (Operations: PE value creation),
> **10** (Entrepreneurship: ETA/search), **11** (Macro: rates, permitting, the power grid); Exec **E2** (Capital Allocation), **E3** (Deals &
> Restructuring), **E8** (Investor Relations: fundraising, platforms, LP reporting). The personal-finance angle extends
> [[unit-10-personal-finance-operating-system]].
>
> ⚠ **Bias:** the hosts are ex-Morgan Stanley sell-side (IBD and rates S&T) and openly sell courses. Almost every guest runs a product in the asset
> class they explain. The Goldman, Morgan Stanley and Carlyle guests distribute private funds to wealthy individuals. Shah runs a fund-of-funds and
> defends its fees. Dorrell raises infrastructure money. Findley owns the home-equity contracts she describes. The hosts were attending the CAIS
> summit while interviewing CAIS. Resnick is a sell-side secondaries advisor who earns fees on every continuation vehicle and cites his own firm's
> study. Clifford runs Carlyle's retail distribution. Both RIA guests pitch independence against the banks that compete with them. Adelman co-owns
> the teams whose record prices he defends and co-founded a retail alternatives manager. No guest makes the case *against* opening private markets
> to individuals. The hosts also get several numbers wrong, and those are flagged inline. Treat the mechanics as reliable and the sales pitches as
> advocacy.

---

## What this adds to the program

- **Repo baseline.** [[tiger-sisters-private-capital-101]] covers 2-and-20, the LBO-as-mortgage analogy and PE's bad reputation.
  [[harlem-capital-vc-insights]] covers the VC waterfall, DPI/TVPI and the J-curve. [[tiger-sisters-wealth-mechanics]] covers ETA with seller
  financing. **No note covers** secondaries, continuation vehicles, evergreen/semi-liquid funds, fund-of-funds, co-investment, subscription lines,
  NAV loans, real estate PE, infrastructure or home-equity investments. This note fills those gaps.
- **The new frame is the plumbing.** How a private fund's clock, fees, leverage and liquidity actually work explains *why* the industry is now
  courting individual investors: LP distributions are at a post-GFC low, institutions are at their target allocations, and individuals are the
  next pool of capital.
- **It teaches the measurement traps:** IRR can be manufactured with a credit line, quartile rankings are meaningless early in a fund's life,
  evergreen fees look cheaper than they are, and private marks dampen reported volatility. These map directly to `acumen/` judgment work.
- **Two real-asset classes get mechanics, not slogans.** Real estate (cap rate as an inverted multiple, and why US office's true yield is below
  its advertised cap rate). Infrastructure (assets bad management can't kill, the muni-bond tax hurdle, 20-year compounding, and the PJM power
  squeeze from AI data centers).
- **It sharpens the small-business ETA material** with search-fund economics, the SBA personal-guarantee constraint, seller notes as quasi-equity,
  and permanent capital as a survival trait.
- **Pass 2 adds the channel's own detail on four things the first pass reconstructed:** continuation-vehicle pricing and tiered carry (Evercore),
  the Yale sale as a live denominator-effect case, the RIA-versus-wirehouse conflict map, and sports-league revenue design. Venture fund math is
  taught from the LP and founder side here. The firm-level application lives in [[apply-wss-to-venture]], [[primary-venture-partners-insights]] and
  [[harlem-capital-vc-insights]]; this note does not repeat it.

## Concept map

| # | Concept | One-line definition | Why it matters | In repo? |
|---|---|---|---|---|
| 1 | Blind-pool fund mechanics | LPs commit; GP calls capital as it finds deals, charges fees on commitments | Creates the deployment clock that drives most GP behavior | partial (2&20, waterfall) |
| 2 | Megafund vs lower-middle-market (LMM) | Same strategy label, different return engine | Where value is *created* (operations) vs *engineered* (leverage, multiples) | partial |
| 2b | Operating value creation | Portfolio groups and operating partners who work the EBITDA lever after close | The only return source that isn't a commodity once debt is cheap for everyone | partial ([[canon-sterman-business-dynamics]]) |
| 3 | Measuring a fund | Net IRR, TVPI, DPI, vintage quartiles; credit lines bend IRR | You can't pick managers or judge PE without it | partial (VC only) |
| 4 | Co-investment & fund-of-funds | Fee-free side-by-side deals; pooled manager selection | How large LPs cut fees; how small ones get access | n |
| 5 | Secondaries (LP-led, GP-led) | Selling fund stakes, or moving assets into continuation vehicles; priced off NAV | The industry's liquidity valve when exits stall (~$160B in 2024) | partial ([[apply-wss-to-venture]] §4) |
| 6 | Distribution drought, the denominator & the endowment model | Distributions/NAV at GFC lows; public falls push privates over target; Yale sells | Why fundraising slowed, why endowments sell, why wealth is courted | partial ([[apply-wss-to-venture]] §1) |
| 7 | Leverage stacked on leverage | Debt at company, GP, fund and NAV level, plus tax rules | Hidden systemic coupling | n |
| 8 | Evergreen/semi-liquid wrappers | Perpetual funds with liquidity sleeves, quarterly redemptions, gates | The product that brings private assets to individuals | n |
| 9 | The wealth distribution chain | Manufacturer → platform → advisor → client | Who earns what, and why platforms became gatekeepers | n |
| 9b | The advisor: wirehouse/private bank vs RIA vs multi-family office | Who the advisor works for and who else pays them | The conflict map for every product in concept 8 | n |
| 10 | Real estate PE | Core / value-add / opportunistic; cap rates; true yield | The third-largest asset class, with its own math | n |
| 11 | CRE refinancing wall & gap capital | 2021-vintage loans rolling into higher rates and lower LTVs | Where equity gets wiped and rescue capital earns its returns | n |
| 12 | Infrastructure | Essential, high-barrier hard assets held for decades | Bond-like durability, equity-like compounding; AI power demand | n |
| 13 | Home-equity investments (HEI) | Selling a share of your home's future equity for cash, with no payments | A lock-in-era product; the cost is hidden in the haircut | n |
| 14 | ETA / search funds | Buying and running a small business instead of founding one | A real alternative career path, with specific capital structures | partial |
| 14b | Venture capital from the outside in | Fund math, stages, SAFEs, preferences, and when not to raise | VC capital raises the exit bar; it is a choice, not a default | y (VC notes) / n (founder side) |
| 15 | Sports franchises: league design and scarcity | National vs local revenue, caps, ownership rules, arena control | Why NFL teams trade like annuities and Premier League clubs like options | n |

---

## 1. Blind-pool fund mechanics and the deployment clock

**What it is:** A traditional PE fund is a **blind pool**. LPs sign a legal commitment (say $100M of a $900M fund) without knowing what will be
bought. The GP sends **capital calls** as it finds deals, and the LP must wire its pro-rata share whether or not it likes the deal.

**How it works:** AJ Tracy walked through his old fund's mechanics:
- **Calls.** A $90M investment equals 10% of a $900M fund, so every LP gets a call for 10% of its commitment.
- **Fees.** The ~2% management fee is charged on *commitments*, not on invested capital, because it pays salaries, travel and overhead.
- **Deployment and re-raise.** Funds rarely deploy 100%. About 15% is held back for add-ons. At roughly **70% deployed** the GP goes back to
  placement agents to raise the next fund, ideally with early exits as proof.
- **Fee offsets.** LPs often require monitoring and transaction fees charged to portfolio companies to be credited against the 2%, so the GP
  doesn't get paid twice.
- **Catch-up arithmetic** (his example, my totals). Call $100M with an 8% compounding preferred return, so LPs must get $108M back first. Sell for
  $150M, a $50M profit. With a full GP catch-up, the GP takes 100% of the next dollars until it holds 20% of profits distributed so far. Solve
  X = 0.2 × (8 + X), so X = $2M. The remaining $40M splits 80/20: GP $8M, LP $32M. **Totals: LP $140M (profit $40M, i.e. 80%), GP $10M
  (20% of $50M).** Without a catch-up, the 80/20 split applies only to the $42M above $108M: GP $8.4M, LP $141.6M. The catch-up is worth $1.6M to
  the GP here.
- **The alternative: independent ("fundless") sponsors.** They raise deal by deal. Each deal must be pitched to investors, who can say no. Carry is
  earned per deal, so a 10x and a zero don't net out the way they do in a pooled fund.

**Business significance / value:** The blind pool hands the GP discretion and a guaranteed fee stream. In exchange, LPs get scope controls through
an **LPAC** (limited partner advisory committee). Tracy's example: "you're a food fund, don't start doing tech." LPs build their allocations from
specialists, so style drift breaks *their* portfolio construction.

**Forces & impact:** The investment period and the fee clock create **pressure to deploy**. Tracy notes that winning a broad auction means you
paid more than everyone else willing to bid, so "either you're really smart or really dumb." The independent sponsor trades certainty of capital
for patience: there's no clock forcing it to buy at the top.

**With vs. without:** Without blind pools, every deal needs fresh LP consent. Closing is slower, certainty of funds is lower, and sellers favor
committed-capital bidders. With them, LPs give up selection, accept fees on idle money, and are exposed to deployment-driven overpaying late in
the investment period.

**Applies when / Breaks when:** Works when the GP has a long track record and a narrow mandate. Breaks when fund size jumps faster than the team,
or when a hot market meets an expiring investment period.

**Channel example:** "Private Equity 101: Lower Middle Market PE Deep Dive" (AJ Tracy). His $900M fund II at Canaccord, and his current fundless
sponsor, Cardus.

**Counterpoint:** Tracy presents fee offsets and LPAC scope limits as robust. In practice both are negotiated, and smaller LPs get weaker terms. The
fundless model's "patience" is partly a virtue made of necessity: he admits deal-by-deal capital is much harder to raise in uncertain markets.

**Links:** [[harlem-capital-vc-insights]] (waterfall, European vs American), [[tiger-sisters-private-capital-101]] (2-and-20 basics),
[[canon-jensen-meckling-agency-theory]] (fees on commitments as an agency cost).

## 2. Megafund vs lower-middle-market: where PE returns actually come from

**What it is:** "Private equity" covers multi-billion-dollar buyouts and family-business recapitalizations alike. The return engines differ.
Tracy names two value levers: lower the discount rate (multiple expansion) or **grow cash flow** (cost cuts *or* reinvestment). Alongside them sits
**financial engineering**: minimum equity, maximum debt.

**How it works:**
- **Depth of the target pool** (Shah). The US has roughly 70,000-80,000 companies with $10-100M of revenue, versus 5,000-10,000 above $100M.
  Fundraising concentrates in the megafunds, so **less capital chases far more companies**.
- **What that buys an LMM investor.** Lower entry EV/EBITDA, and less debt needed because growth can produce the return. Shah says her portfolio
  runs at about **half the market's median leverage**.
- **Alignment.** LMM GPs get rich from carry, which requires selling, rather than "stacking management fees from fund to fund." Shah wants them to
  earn carry because carry means distributions.
- **The LMM reality** (Tracy). The CEO is often the owner. One target had 26 family members working everywhere from the C-suite to the forklift.
  After a $500M payout, do they still show up? EBITDA often **dips right after purchase** while the sponsor invests in talent and systems.
- **Leverage norms.** When Tracy started, light-industrial deals paid 6-8x EBITDA with 3.5-4x leverage. Today 6x leverage is "easy," stacked with
  holdco PIK (payment-in-kind) layers.
- **Strategy archetypes:**
  - Playbook firms (Vista).
  - Roll-ups buying small players cheaply for **multiple arbitrage** (Riverside, Align).
  - Zero-based budgeting (3G).
  - Loan-to-own distressed (Apollo at Caesars).
- **Carry by fund size** (comp episode, Buyside Hub data via "High Yield Harry"):
  - $4-5B funds: 20-40 bps of carry for mid-level staff.
  - $8-10B funds: 30-50 bps.
  - $200-500M funds: **1-5%**, because a small pool needs a bigger slice to pay the same.
  - On paper, 20% carry on a $10B fund that doubles is $2B of carry to split.
  - Cash comp barely beats banking until associate level: senior analysts average about $182.5k total.
- **Operating lift.** AI call-recording lets a sponsor train reps on the best calls and score 100% of calls to find "100 basis points" of
  improvement (Sixth Street short). Don Kieffer's operations episode adds the **capability trap**: cutting 50% of maintenance staff gives
  "better before worse." Private ownership can absorb a "worse before better" investment dip that quarterly reporting punishes.

**Business significance / value:** At megafund scale, returns lean more on leverage, multiples and scale. In the LMM, the classic professionalizing
work is still available: upgrading the CFO, adding M&A, building systems. Whoever does the operational work captures the **multiple step-up**
when a small, messy company becomes a larger, professional one that a bigger sponsor will pay more for.

**Forces & impact:**
- Zero rates (2019-21) inflated software buyout prices. Shah says the AI-disrupts-SaaS headlines are about *those vintages and prices*, not all
  PE software.
- Rising rates turn high-leverage capital structures into refinancing problems. Tracy expects sponsors to put in more equity, and lenders to
  prefer workouts over foreclosure on asset-light businesses that have nothing to seize.
- Hot themes as of 2026: residential and commercial services beyond HVAC ("can't be disrupted by AI"), pharma services and healthcare.
- **Who's in the equity changes the price you can pay** (Paramount/WBD short). A strategic buyer pays for what it can't build. A sovereign
  fund may accept a low return for influence. A PE-style sponsor paid on fees and deal-level carry walks once a higher bid pushes expected IRR below
  its hurdle. Kristen's reading is that Affinity Partners left the Paramount consortium on that math, not on politics.

**With vs. without:** Without a functioning LMM buyer base, founder-owned companies can only sell to strategics or to family. Many would stay
under-professionalized. When the engine breaks, through overpaying plus too much leverage, cost cuts replace investment and the "corporate raider"
headline becomes true.

**Applies when / Breaks when:** LMM works with real operating support, modest leverage and an exit path to a larger buyer. It breaks on key-person
risk, hidden concentration, or a sponsor who is really running a megafund leverage playbook on a small company.

**Channel example:** "Morgan Stanley's Head of PE Solutions" (Shah). "PE 101: Lower Middle Market" (Tracy: a QSR paper converter sold to a
strategic at **3.2x**, the same month he married the CEO's daughter). "Exactly How Much Investment Bankers & PE Get Paid." "How PE is Actually
Using AI" (short).

**Counterpoint:** Every LMM GP says it creates value through operations. Tracy concedes the stereotype exists for a reason (Toys "R" Us) and that
some firms just lever up. The claim that small deals deliver comparable or higher returns with half the leverage comes from a fund-of-funds that
sells LMM exposure. Return dispersion is also wider in the LMM. The hosts' own PE-vs-hedge-fund episode is blunter: if you didn't make money in PE
over the last 15 years, "you're doing it wrong." That is an admission that beta and cheap debt did much of the work.

**Links:** [[unit-06-whats-a-business-worth]] (multiples), [[canon-sterman-business-dynamics]] (capability trap), [[canon-goldratt-the-goal]]
(flow and firefighting), [[canon-porter-competitive-strategy]].

## 2b. Operating value creation: portfolio groups and operating partners

**What it is:** The staff and process a PE firm uses to raise a company's cash flow *after* buying it. A megafund keeps a dedicated
**portfolio group** (Bain Capital) or a bench of **operating partners** (Sixth Street) beside the deal team. A small fund's deal team does the same
work itself.

**How it works:**
- **The returns bridge** (Kristen, PE 102). An LBO return has three sources:
  - EBITDA growth, which raises exit EV at a constant multiple.
  - Debt paydown from the extra cash, which shifts EV from lenders to equity.
  - Possible multiple expansion if margins and growth are better at exit.
  Her point is that the first two can't be bought: in the zero-rate years anyone could lever up, so financial engineering became a commodity.
  "Without operational performance, you're not special." The transcript has her saying returns come from "the transaction"; context makes clear
  she meant operations.
- **The LBO-in-three-minutes arithmetic** (short), as the baseline the bridge decomposes. Buy at 10x $1M EBITDA = $10M with $3M equity and $7M
  debt. Grow EBITDA to $1.5M over 5 years and sell at the same 10x for $15M. Pay down $1M of debt from cash flow, so $6M is owed. Equity is
  $15M − $6M = $9M, 3x on $3M, about a 25% IRR. Of the $6M gain, $5M came from EBITDA growth and $1M from paydown, with no multiple expansion.
- **How Bain Capital's portfolio group works** (PE 102). The thesis at purchase names "three or four" growth levers, and the group's job is to help
  management execute them fast. Generalists cover one or two companies and specialists cover more. The group meets the deal team weekly. It hires
  only people with long consulting *and* operating careers, never straight from school or an MBA. Members work with the CEO, CHRO, CIO and head
  of sales but hold no title inside the company.
- **Sixth Street's model** (Paul Dodd). The operator is in the room at every stage:
  - Before investment, sizing the value opportunity and risk alongside the deal team.
  - During the hold, driving it while the deal team keeps it "on the rails."
  - At exit, building the narrative so the improvement is paid for.
  The partners measured him on how the CEOs rate Sixth Street. He refuses to write playbooks ("guides and frameworks" instead), because you can't
  have the answer before you understand the business.
- **The go-to-market lever with AI** (Dodd's worked example).
  - Record 100% of sales calls.
  - Mine the best reps' calls from discovery to close and build an onboarding agent from them.
  - Score every new rep's calls against that standard and coach the gaps.
  - Score every call in the company to find 50-200 bps of win-rate improvement.
  The payoff is shorter ramp time. A second example is using LLMs to build ideal-customer-profile lists ("every company hiring 10+ people in
  Nebraska") and back-test which attributes predict a sale.
- **AI cost reality.** Dodd expects tech budgets to *rise* in 2026, with payoff in 2027-28. AI tools are workflows rather than tools you build
  workflows around, so each choice is a change-management project. A wrong pick gets redone in 6-12 months. Pick the use with the most impact and
  the least process change. AI on a bad forecasting process just makes the bad forecast faster.

**Business significance / value:** At constant multiples, EBITDA is the lever that compounds through both the exit value and the paydown.
Operating capability is how a firm can win an auction without overpaying: it can underwrite growth that other bidders can't deliver. It is also
a fundraising story, which is why every firm claims it.

**Forces & impact:**
- The end of cheap debt. Dodd: "Free money is gone and gravity is now real again." Growth at any cost is over, so unit economics decide.
- AI-native competitors with no legacy tech, against incumbents with distribution. Dodd expects the shakeout over 12-24 months.
- "Stroke of the pen" policy risk (tariffs, executive orders) that wasn't in models three years ago.
- **Fund size.** Dodd's "curse of capital": a fund that must deploy loses discipline. Sixth Street keeps each growth fund at "billions, not hundreds
  of billions" and pairs it with an overlay fund. That is how it wrote a $1B debt-and-equity package for Airbnb, alongside Silver Lake, in under
  seven days during COVID.

**With vs. without:** Without an operating function, returns depend on buying cheap, leverage and the exit market, and all three were gone by
2023. With it, a firm can hold through a weak exit window while EBITDA grows into the entry price. That is Resnick's "grow into the multiple"
argument for 2018-22 vintages (concept 5).

**Applies when / Breaks when:** Works when the company has product-market fit and a scale problem, and when management trusts the operator. It
breaks when the "operating partner" is a marketing title, when the playbook is imposed before the business is understood, or when cost cuts are
labeled value creation.

**Channel example:** "Private Equity 102: Value Creation at a Megafund" (Bain Capital Portfolio Group). "PE | Growth Equity Value Creation w Sixth
Street's Paul Dodd." "LBO in Under 3 Minutes" (short). "How PE is Actually Using AI" (short).

**Counterpoint:** Neither episode gives a single number on how much of a fund's return came from operations versus leverage and multiples, or a
named portfolio company. Neither discusses who pays the operating team. When operating partners bill portfolio companies instead of the
management company, LPs bear the cost indirectly. Dodd calls Sixth Street "not an LBO strategy company" and warns that debt raises risk, though
the firm began as TPG's lending arm and lends to the same kind of company. Read that as instrument choice, not a stance against leverage. PE 102
is mostly a career story; its value-creation content is thin.

**Links:** [[canon-sterman-business-dynamics]] (worse-before-better), [[canon-goldratt-the-goal]], [[unit-05-growth-and-returns]],
[[wss-ai-economics]] (AI capex and adoption), [[canon-grove-high-output-management]].

## 3. Measuring a fund: net IRR, TVPI, DPI, quartiles, and the manufactured J-curve

**What it is:** **Net IRR** is the time-weighted return after fees. **TVPI** is total value (realized plus unrealized) per dollar called.
**DPI** is cash actually distributed per dollar called. Funds are compared within a **vintage year** and ranked into quartiles.

**How it works:**
- **Benchmarks** (Shah). For a mature buyout fund: above 20% net IRR, above 2x net multiple, and DPI "as close to two as possible." The best venture
  funds reach 5-10x, but very few do, and fame often rests on one vintage.
- **Quartile claims.** "I have never had a fund come into my office" that didn't claim top quartile. Slice the data differently and anyone ranks
  first, like bookrunner league tables.
- **Quartiles mature too late.** Rankings mean little until years 5-6, by which point the LP has already faced one or two re-up decisions. So
  selection relies on other tools, including whether a $1B top-quartile team can repeat with a $2.5B fund.
- **Subscription credit lines.** These are loans secured by LPs' uncalled commitments. They were originally 60-90-day cash bridges. At zero rates,
  banks offered lines worth a third to half of commitments, with revolver-like terms.
  - Normally a new fund shows negative IRR at first, because fees push NAV below cost (the J-curve).
  - Fund a deal on the line, draw LP money a year later after a mark-up to 1.2x, and the negative IRR disappears.
  - A day-one mark-up gives "an infinite IRR."
  - Lines now show up in secondaries too. In a continuation vehicle the sub line stays in place 12-24 months and can fund part of the purchase:
    selling LPs get 75 cents on day one instead of 50, with 25 of those cents borrowed (Resnick, Secondaries 201). He concedes LPs have "mixed
    receptivity" to the IRR effect.
- **Worked example (mine).** Exit at 2.0x after 5 years:
  - Capital drawn at t=0: IRR = 2^(1/5) − 1 ≈ **14.9%**.
  - Capital drawn at t=1 because a line funded year one: IRR = 2^(1/4) − 1 ≈ **18.9%**.
  - **TVPI is unchanged, slightly lower after line interest.** IRR measures timing; the multiple measures money.

**Business significance / value:** IRR drives marketing and carry hurdles, so GPs have an incentive to manage it. DPI is the only metric that is
cash. It moved from afterthought to central in the post-ZIRP drought (Shah: much less of a focus five to ten years ago).

**Forces & impact:** The FT figures the hosts cite put subscription lines at roughly **$900B in 2023**. Higher rates made the lines costlier, so
some GPs moderated their use. LPs still *expect* lines to be used to soften the J-curve. Second-order effect: an industry of earlier, flatter
J-curves makes young funds look better than they are, and selection by early IRR gets worse.

**With vs. without:** Without DPI discipline, a fund can raise its next vehicle on marks alone ("hanging skins on the wall," in Tracy's phrase).
When marks turn out optimistic, LPs find out a fundraise too late.

**Applies when / Breaks when:** Net IRR plus DPI comparisons work within a vintage, between mature funds. They break when comparing across vintages,
across funds with different credit-line policies, or a young fund's IRR against a mature fund's.

**Channel example:** "Morgan Stanley's Head of PE Solutions" (Shah on quartiles and credit lines). "Will Private Equity Take Down the Global
Economy" (the hosts admit they didn't understand subscription lines; Shah's episode later explains them).

**Counterpoint:** Shah calls J-curve mitigation "generally good for everyone." But the borrowing cost is real and comes out of LP returns, and the
benefit lands mostly on reported IRR and on GPs' hurdle math. IRR also overstates how much wealth is created when early distributions can't be
reinvested at the same rate. The program should default to multiples and DPI.

**Links:** [[harlem-capital-vc-insights]] (DPI as truth, the 3-fund hump), [[canon-mauboussin-success-equation]] (separating skill from vintage
luck), [[canon-akerlof-market-for-lemons]] (every pitch claims top quartile, an information-asymmetry market).

## 4. Co-investment and fund-of-funds: buying down the fee load

**What it is:**
- **Co-investment** means investing *next to* a GP in a specific deal, usually at **zero management fee and zero carry**.
- A **fund-of-funds (multi-manager)** pools many LPs' money to select, diligence and access many GP funds.

**How it works:**
- **Blended fees.** Put $1 in a 2-and-20 fund and $1 in a 0/0 co-invest, and you're effectively paying **"one and ten"** (Shah). Nobody knows
  how much PE capital is unpromoted co-invest, so headline 2-and-20 overstates what large LPs actually pay. Megafund carry holds at 20%, but
  institutions negotiate fees below 2%.
- **Two co-invest models:**
  - **Post-close syndication**, pro rata to fund commitments, as passive capital in a GP-controlled vehicle.
  - **Pre-signing co-underwriting.** MS commits before the LOI or bid so the GP can credibly say where the money is coming from. MS sometimes
    writes a bigger check than the GP and takes a board observer seat.
  - Either way, investors want the same valuation and security as the GP, plus **drag-along** and **tag-along** rights.
  - Shah's co-invest close rate is **under 5%**. Mostly she says no, politely.
- **Fund-of-funds evolution.**
  - Twenty years ago FoFs charged **1% plus 5% carry**. "That is gone."
  - The case today: aggregation gives negotiating weight (a $50-100M commitment instead of an LP's $2M), plus diligence coverage. Commitments are
    locked for ~10 years, so a bad manager pick is expensive.
  - FoF sourcing at MS includes **15,000 financial advisors** whose clients run or own PE funds, a sourcing angle the hosts had never considered.
- **The club-deal-to-co-invest shift.** Caesars (2006-08, $30B LBO) was co-sponsored by Apollo and TPG, about $1.325B of equity each, with
  ~30 co-investors adding ~$3.5B (Michael J. Fox Foundation, Bob Kraft, banks). Club deals with shared control fell out of favor afterward: one
  sponsor decides, and co-investors ride along.

**Business significance / value:** Co-invest lets big LPs build concentrated, cheaper exposure. GPs gain deal capacity without breaching the
per-deal concentration limits of their own fund (e.g. no more than 20% in one deal). FoFs earn a fee for access and selection, a business that
only survives if net returns beat what clients could get alone.

**Forces & impact:** Fee pressure from LPs, larger deal sizes, and GPs needing equity certainty in competitive auctions. Second-order effect:
co-invest flow goes to the biggest, most trusted LPs, which widens the gap between them and small LPs.

**With vs. without:** Without co-invest, deals above a fund's concentration limit need club structures with messy shared control (Caesars), and
LP fees stay higher. Without FoFs, small institutions and individuals can't build diversified PE exposure at all.

**Applies when / Breaks when:** Co-invest works with high alignment and a long relationship. It breaks through adverse selection: the GP
syndicates the deals it doesn't want to hold. FoFs work when selection skill is real. They break when the second fee layer meets average managers.

**Channel example:** "Morgan Stanley's Head of PE Solutions" (Shah). "Private Equity's Blueprint for Legally Stealing from its Creditors | Caesars
LBO (Pt 1/3)."

**Counterpoint:** Kristen Kelly's instinct that FoF means "fees upon fees" is softened, not refuted. Shah is the seller here. The adverse-selection
risk in syndicated co-invest goes unexamined. Shah's pre-signing model mitigates it, but most LPs get the post-close syndication flavor.

**Links:** [[canon-akerlof-market-for-lemons]], [[canon-jensen-meckling-agency-theory]], [[tiger-sisters-private-capital-101]].

## 5. Secondaries: LP-led sales and GP-led continuation vehicles

**What it is:** The market for buying existing private-fund exposure. A **primary** is an LP's original 10-year commitment to a new fund. A
**secondary** is any later transfer of that exposure.
- **LP-led:** an LP sells its fund interests, usually a portfolio of many, to a secondary buyer, who takes over the position including any
  unfunded commitments.
- **GP-led:** the sponsor starts the deal. The two forms are:
  - A **tender offer**: every LP in a fund gets a 10-20 business-day window to sell at a price set by outside buyers.
  - A **continuation vehicle (CV)**: one or more assets move into a new vehicle, and each LP chooses to sell or roll.

**How it works** (Justin Resnick, Evercore, across two episodes):
- **Size and growth.**
  - About $20-30B a year when he started in 2012-13.
  - About **$160B in 2024**: roughly $90B LP-led and $70B GP-led.
  - He'd "be surprised" if 2025 didn't reach $200B.
  - Pass 1 had Shah's "about half and half"; Resnick's split is 50/50 to 60/40.
  - Buyout is still 80%+ of volume. Credit, infrastructure and venture secondaries are growing.
  - Step changes in the market followed the dot-com bust and the GFC, when LPs suddenly needed cash.
- **Pricing is quoted against NAV,** the GP's quarterly reference-date mark. A stake goes at 75, 100 or 110 cents on the dollar depending on assets
  and outlook. In 2024-25, recent-vintage funds from brand-name GPs traded in the mid-to-high 90s, sometimes at par. Buyers can pay a higher
  headline price with **deferred payment**: 50 cents now and 50 in a year, part funded by the portfolio's own distributions.
- **Why LPs sell now.** Resnick frames it as portfolio management rather than distress:
  - Rebalance an allocation that is "out of whack" (the denominator, concept 6).
  - Recycle old exposure into new vintages so as not to miss one with core GPs.
  - Take strong pricing while buyers compete.
  - A typical case: a pension needing $1B sells 100 fund interests at once.
- **The single-asset CV, step by step:**
  1. A sponsor's crown jewel has tripled or quadrupled over 3-5 years.
  2. The old route was to sell it to another sponsor, lock in the multiple for the track record, and watch the buyer make another 3-5x.
  3. Instead, the advisor runs an M&A-style auction among secondary buyers, who underwrite the company like a PE buyer would.
  4. The winning price goes to the old fund's LPs. Each sells (in his processes over 12-24 months, 80-99% did) or rolls.
  5. The company moves into a new vehicle capitalized by new secondary money, rolling LPs and the GP.
  6. Debt is usually refinanced at the same time to suit the new hold period. Attractive existing debt can stay if the deal is structured as a
     transfer to an affiliate.
- **The use case flipped.** In the early 2010s CVs were mostly for tail-end funds that had done "just okay": the GP couldn't raise again, so the
  restructuring swapped out LPs and reset its economics. Today the same structure is for winners that need more time or capital. "End of fund
  life is not necessarily a bad thing anymore" (Resnick).
- **CV economics** (Resnick's worked example). Invested 100, now worth 400, transferred at 400.
  - **Fee.** A 2% fee on 100 is 2. On 400 it would be 8 for managing the same company. So CVs charge **50-100 bps (up to ~125)**, which keeps
    dollar fees "neutral to slightly accretive."
  - **Carry is where the GP earns.** It crystallizes carry on the old fund at the 400 price, rolls that carry into the CV, and earns new carry on
    a tiered waterfall instead of a flat 20%:

| Tier | Carry | Hurdle |
|---|---|---|
| 1 | 10% | 8% IRR |
| 2 | 15% | 15% IRR **and** ~1.5x MOIC |
| 3 | 20% | 20% IRR **and** 2.0x MOIC |

  Some deals use 15/20/25. Single-asset buyers expect LBO-style returns (20%+ IRR, 2x+). Multi-asset CVs are diversified, take bigger checks
  and accept a slightly lower return. By volume, single- and multi-asset are about 50/50. By count, single-asset deals are 60-70%.
- **Managing the conflict.** The GP is seller (for the old fund) and buyer/manager (of the CV). The safeguards are:
  - LPAC approval.
  - A third-party auction.
  - A fairness opinion.
  - The LP's option to sell.
  - The GP rolling *all* its crystallized carry into the CV, so its look-through stake in the company rises.
- **The buyer universe.** About 15-25 firms can write multi-hundred-million checks. Flagship secondary funds now rank among the largest PE funds:
  Blackstone Strategic Partners ~$25B, Lexington ~$23B, Ardian ~$30B (his figures, approximate). Direct sponsors (Apollo, TPG, Leonard Green,
  A&M Capital) are launching single-asset CV funds. Their reasoning: if rivals keep their best companies in CVs instead of selling them, this is
  the only way to buy them.
- **Collateralized fund obligations (CFOs).** Instead of selling at a discount, an LP tranches a seasoned portfolio's cash flows. The rated senior
  notes go to insurers, and the LP keeps the equity tranche. CFOs work best on credit portfolios, which pay current interest. GPs use the same
  technique to raise flagship money.
- **Credit CVs** exist because loan repayment often depends on the borrower being sold. Slow M&A delays that even for performing loans.

**Business significance / value:**
- Secondaries give liquidity to LPs locked for 10+ years.
- They give GPs DPI without selling into a weak exit market. Resnick says 12%+ of PE exits in 2023 went through CVs.
- Buyers earn returns from seasoned, known assets bought near NAV, from conservative GP marks, and from a typical "pop" at exit of 20-40% over
  the mark.
- The advisor earns fees on both the M&A-style auction and the fund overlay. Resnick calls the job "part M&A, part fundraising."
- **Secondaries are ideal for evergreen funds** (concept 8): already invested, diversified at once, and mature enough to distribute cash for
  redemptions. Most secondary firms have launched a '40 Act fund with monthly inflows, where institutional fundraising takes 6-18 months.

**Forces & impact:**
- Weak M&A and IPO markets; the drought (concept 6); evergreen demand for seasoned assets.
- A buyer base Resnick calls "drastically undercapitalized." In 2024 dry powder of $166B covered only 1-2 years of deals, so pricing stays strong.
- **Second-order:**
  - CVs postpone true price discovery on the best assets.
  - The fee and carry reset gives GPs a new reason to keep winners.
  - Secondaries feed the leverage stack: sub lines, deferred payments, refinancings (concept 7).

**With vs. without:** Without secondaries, an LP needing cash in a drought can only default on capital calls or wait. The denominator problem would
freeze allocations harder, and every end of fund life would force a sale into whatever market exists. With them, liquidity exists at a price, and
the GP gains a way to sell to itself.

**Applies when / Breaks when:** Works when buyers have real pricing information, many LPs sell (a market test), and the GP's whole economics roll.
It breaks when a CV marks up and re-fees an asset nobody else would buy, when "roll" is the only practical option, or when deferred payments and
sub lines push hidden leverage into the new vehicle.

**Channel example:** "Private Equity Secondaries 101" and "Secondaries 201" (Resnick). "Morgan Stanley's Head of PE Solutions" (the evergreen fit).
"Will Private Equity Take Down the Global Economy" (CVs levered again). "FX101… Yale's $6bn Sale" (an LP-led sale, concept 6).

**Counterpoint:**
- Resnick is the advisor paid to run these deals, and the CV performance study he cites ("in line with PE, narrower dispersion, winners keep
  winning") is Evercore-sponsored and mostly unrealized.
- His 101 claim that CVs are "50% plus" of the market conflicts with his own 2024 split, where all GP-led deals were ~44%.
- A high sell rate partly shows that pricing was full. It isn't proof that LPs endorse the structure.
- "Mid-to-high 90s" applies only to good recent buyout funds. Venture, older and tail-end portfolios trade at much wider discounts, which he
  never mentions.
- Asked about 2018-22 vintages bought at peak multiples, he answered that the companies need time to "grow into their entry valuation
  multiple." Kristen called it "word salad." It is an admission that some marks hold stale enterprise values.

**Links:** [[canon-jensen-meckling-agency-theory]] (GP on both sides), [[harlem-capital-vc-insights]] (DPI pressure), [[apply-wss-to-venture]]
(secondaries vs an opportunity fund for seed winners), [[primary-venture-partners-insights]] (Select as the non-CV answer),
[[wss-capital-markets-ma]] (SpaceX holders' liquidity), [[wss-credit-distressed]] (credit secondaries).

## 6. The distribution drought, the denominator, and the endowment model

**What it is:**
- PE distributions *as a share of unrealized value* fell to a level last seen after Lehman, even as IPOs reopened and secondaries set records.
- The **denominator effect** is the mechanism that turns that drought into forced selling. When public assets fall, slow-marked private holdings
  become a larger share of the portfolio than the target, so new commitments freeze or stakes get sold.
- The **endowment (Yale/Swensen) model** is the allocation philosophy that made universities the largest holders of exactly these assets.

**How it works:**
- **Shah's decomposition of the ratio:**
  - **Numerator.** Absolute distributions set a record in 2021, an anomaly. Excluding 2021, they've risen every year, including 2025.
  - **Denominator, part one.** Unrealized NAV ballooned: record inflows from 2018-21.
  - **Denominator, part two.** Marks above cost that some suspect are optimistic.
  - **The GFC was different:** distributions simply stopped.
- **The denominator effect, mechanically** (VC 101 and the Powell/endowment episode). Take a $100 portfolio at target 60 public / 20 private
  equity / 20 other. Public equity falls 25% to 45, and the private marks barely move. The total is now about $85, and private is 20/85 ≈ 24%,
  above target (my illustration). Public assets rebalance in a day. Private funds can't, so the LP stops recommitting, cuts managers, or sells in
  the secondary market. In 2022 venture marks lagged while public tech fell, so VC LPs "freaked out" and trimmed managers. The pass-1 reverse
  case still holds: a public rally leaves LPs *under*-allocated and drives record commitments.
- **Yale's sale** (FX101 episode, April 2025):
  - Yale ($41B endowment) hired Evercore to sell about **$6B of LBO fund interests**, roughly 15% of the endowment (my arithmetic), in an LP-led
    secondary.
  - Kristen's reasons LBO exposure is under pressure:
    - Tariffs squeeze portfolio margins.
    - Lower, less certain profits make the debt riskier and dearer.
    - Exits are shut, so distributions stall.
    - Equities and bonds are both down, so the denominator effect bites.
  - The irony she flags is that Yale's late CIO David Swensen invented the model being unwound.
  - Bloomberg reported Yale had been exploring the sale for months, so it predates the federal funding fight.
  - Resnick, asked a year later, declines to discuss Yale and calls such sales opportunistic portfolio management at strong prices.
- **Why endowments can't just spend their way out** (Harvard funding episode):
  - Much of an endowment is restricted by donors to specific uses.
  - The average endowment spends **48.1%** of its payout on financial aid (the annual NACUBO-type study the hosts cite).
  - It aims to live off returns in perpetuity and preserve principal.
  - **Size is a feedback loop** (Jen). Harvard (~$52B) can absorb a $2B grant cut. The average endowment (~$230M) can't generate meaningful income
    without risking principal, so small endowments must run more conservatively and earn less. "The bigger you are, the more of a buffer you
    have."
- **The tax shock.** The hosts report the 2025 tax bill's endowment excise tax: floated at 22% (the House draft was actually 21%), enacted as a
  tier by endowment per student. They cite the 4% and 8% tiers and omit the 1.4% bottom tier. The foundation tax was dropped. Endowments expecting
  the hit looked to exit illiquid positions in the first half of 2025.
- **GP leverage over exits.** Per a Bloomberg piece the hosts cite, some GPs approve an LP's transfer (required for any secondary sale) only if the
  seller commits to the GP's next fund. In effect you pay to leave. Yale is big enough to refuse; a small LP that needs cash isn't.
- **Feedback loop.** No distributions, so LPs can't recommit, so GP fundraising slows, so managers turn to new LPs.

**Business significance / value:**
- This is the macro reason for the wealth push. Goldman's Olson concedes the cynic's point that managers "need to find a new LP." Institutions over
  the last 30 years have reached their target allocations.
- Endowments are the most prestigious LPs because they have the longest horizon. Pensions and insurers have liabilities and must plan for
  withdrawals.
- When an endowment sells, the secondary buyer captures the discount, or, at strong prices, the seller captures liquidity cheaply.

**Forces & impact:**
- Rates (slower exits, dearer debt), tariffs, buyer-seller valuation gaps, the exit-market cycle, and now policy toward universities (the excise
  tax, frozen research grants, foreign-student limits).
- **Second-order:**
  - Secondaries boom.
  - CVs proliferate.
  - NAV loans grow.
  - Managers push into 401(k)s and wealth channels.
  - The model's prestige erodes when its inventor's own endowment sells.

**With vs. without:**
- In a normal cycle, distributions recycle into new commitments and fundraising funds itself.
- When the cycle stalls, the industry needs liquidity engineering (concepts 5 and 7) or new capital (concept 8).
- Without the endowment model, universities would hold liquid 60/40 portfolios: lower expected return, but no forced sellers in a drawdown.

**Applies when / Breaks when:** The ratio diagnosis works when marks are honest. If marks are inflated, the real denominator is smaller and the
drought is partly a hidden write-down. The endowment model works for large, perpetual, untaxed pools with patient governance. It breaks for small
endowments, for taxed ones, and for any pool whose spending needs spike just as private assets become unsellable.

**Channel example:** "Morgan Stanley's Head of PE Solutions" (the distributions framing). "FX101, Operation Twist and Yale's $6bn Sale of Their
ENTIRE PE Portfolio." "Jerome Powell Isn't Coming to Save Us Plus Endowment Talk…" (Harvard, endowment spending). "Venture Capital 101" (the 2022
denominator effect in VC). "Secondaries 201" (endowment tax, Yale).

**Counterpoint:**
- Shah's decomposition is right but generous. "Some skepticism that marks are optimistic" carries a lot of weight. If exits clear below marks,
  the ratio and reported returns get worse together.
- The episode title says Yale sold its "ENTIRE" PE portfolio. The reported deal was about $6B of LBO interests, not everything.
- The hosts' endowment sizes are loose: Princeton is closer to $34B than $38B, and Brown closer to $7B than $5B.
- "48.1% spent on aid" is a share of endowment *spending*, not of assets.

**Links:** [[canon-meadows-thinking-in-systems]] (a reinforcing loop with a delay), [[canon-sterman-business-dynamics]], [[apply-wss-to-venture]]
(how the drought reaches seed funds), [[harlem-capital-vc-insights]] (the LP's view), [[wss-rates-macro]] (rates and the April 2025 drawdown).

## 7. Leverage stacked on leverage across the fund stack

**What it is:** Debt now sits at every layer of a private-equity structure, not just inside the bought company. The layers are often lent by
different teams or institutions that can't see each other's exposure.

**How it works:**

*Layer zero: why leverage cuts both ways* (shorts).
- **The fatal flaw.** Buy a $10M "house" with $3M equity and a $7M mortgage. If it's worth $15M, equity goes from 3 to 8, a 2.7x gain on a 50%
  asset gain. If it falls to $6M, the asset is down 40% and the equity is gone, below zero. The debt that juiced the upside works "like a noose."
- **Cash-free, debt-free.** In a private-company LBO the buyer pays for the whole enterprise. The seller repays its own debt and keeps its excess
  cash, and the buyer funds a minimum operating cash balance as a *use*. In a public take-private the buyer must buy every share, at a premium,
  and refinance the debt. The target's cash sits inside the equity it buys, so excess cash above the operating minimum becomes a *source*. Both
  sources-and-uses tables end up equivalent.
- **Rollover equity** (Skechers short). 3G offered Skechers holders $63 cash, or $57 cash plus one unlisted equity unit in the private company.
  Rollover was capped at 20% so 3G keeps 80%. Rolling sellers accept less cash now in exchange for a share of the upside. That aligns them with
  the buyer and lowers the cash the sponsor must raise.

*The fund stack* (the hosts' walk-through of an FT piece):
1. **Company-level LBO debt.** On Caesars: $24B of debt on ~$3B EBITDA, about **8x leverage** and about **1.5x interest coverage** at inception.
   An OpCo/PropCo split added CMBS (commercial mortgage-backed securities) debt on the casinos, worth roughly two extra turns.
2. **Private-credit lenders that are themselves borrowing** from banks, often affiliated with the same PE firms.
3. **GP co-investment financed by bank loans.**
4. **Subscription lines:** about $900B (2023).
5. **NAV loans:** the fund borrows against its stakes in already-levered portfolio companies, about **$100B** last year.
6. **Dividend recaps**, and **continuation vehicles levered again**.

**Tax layer** (LBO-modeling short):
- EBIT 100, D&A 50, EBITDA 150, interest 100.
- 2018-22: the deduction cap was 30% of EBITDA = 45, so taxable income was 55.
- From 2023: the cap became 30% of EBIT = 30, so taxable income rose to 70.
- PE lobbied to restore the EBITDA basis, which Treasury scored at almost $180B over 10 years. *Update the short predates: the 2025 tax act
  restored the EBITDA basis. Verify before relying on it.* The Adelman episode (March 2025) repeats the lobbying story and Bloomberg's
  ~$180B deficit estimate, and notes the cap hits any borrower, not just PE-backed ones.

**Business significance / value:** Each layer raises equity IRR or eases liquidity. Each layer also earns a lender a fee. The hosts' point is about
who carries the risk: non-bank lenders face lighter supervision than banks.

**Forces & impact:**
- Cheap money built the stack.
- Rising rates raise interest costs while the deduction cap shrinks.
- Covenant-lite documents let sponsors move assets away from creditors (the Caesars "creditor-on-creditor violence" lineage). That is why First
  Brands kept Apollo off its lender list: it didn't want Apollo's tactics in a future restructuring, or a competitor's owner (Apollo backs Tenneco)
  in its data room.

**With vs. without:** Without layered leverage, PE returns are lower, but failures stay at the company. With it, stress transmits: a bad mark
triggers NAV-loan pressure, then forced sales, then a lender's loss. A reasonable reading of the FT is that the system is more tightly coupled
than anyone's single exposure suggests.

**Applies when / Breaks when:** Works when cash flows grow and refinancing markets stay open. Breaks on fraud or double-pledged collateral
(First Brands, Tricolor), a jump in rates, or a sudden stop in credit.

**Channel example:** "Will Private Equity Take Down the Global Economy." "Private Equity LBO Modeling Basics: Changes to Interest Deductibility"
(short). "Caesars LBO (Pt 1/3)." "Why Apollo Was Blacklisted by First Brands." "The One Fatal Flaw with Private Equity…", "Cash Free Debt Free
EXPLAINED", "Skechers' $9B deal… Rollover Equity", "Private Equity vs. Private Credit in 90 seconds" (shorts; the last pictures the capital
structure as a cereal bin: senior secured debt comes out first from the top, and equity at the bottom gets the crumbs).

**Counterpoint:**
- The hosts say private credit is "on the order of $17 trillion" against $8T of PE AUM. **That is wrong.** Private credit AUM is roughly
  $1.5-2T. They probably confused it with a broader debt aggregate.
- They also concede credit spreads "didn't budge" through the First Brands scare.
- Tracy's counter: lenders to asset-light businesses have nothing to foreclose on, so they cooperate in workouts, which can make leverage less
  explosive than the layer count implies.

**Links:** [[canon-perrow-normal-accidents]] (tight coupling plus complexity), [[canon-taleb-black-swan]], [[unit-04-is-it-healthy]] (leverage and
coverage ratios).

## 8. Evergreen and semi-liquid wrappers: private assets for individuals

**What it is:** Perpetual vehicles (non-traded BDCs and REITs, interval funds, tender-offer funds, private evergreen funds) that hold the *same*
illiquid assets as 10-year drawdown funds. They accept money continuously and offer **limited periodic redemptions**.

**How it works:**
- **Liquidity sleeve.** Olson: 10-20% sits in liquid, yielding, stable assets to meet redemptions. That drags returns ("single digits on the
  sleeve"); there's "no free lunch."
- **Redemption limit.** Typically **up to 5% of assets per quarter** (Shah). Beyond that the manager can **gate**. Olson calls gates "a feature,
  not a bug": they prevent fire-selling assets at a discount to fund redemptions. The hosts were gated by a big private REIT in 2022.
- **Advantage: fully invested on day one.** No blind-pool risk, no capital-call admin. A drawdown program takes **5-6 years** to reach a target
  exposure.
- **Fee illusion** (Olson's example). The per-year arithmetic is mine, and it assumes a full catch-up:

| | Drawdown fund | Evergreen |
|---|---|---|
| Management fee | 1.5% on commitment | 1.25% on NAV |
| Carry | 20% over an 8% hurdle | 12.5-15% over a ~5% hurdle |
| When carry is taken | After capital is returned, often years 4-6 | **Every year, on realized and unrealized gains** |
| Year-one carry on $1M at a 12% gain | $0 | ~$15k (12.5% of $120k) |

  The evergreen looks cheaper on paper and is "in most years more expensive" in practice.
- **Temporary relief:** large early-mover fee concessions while managers race for platform scale.
- **Deployment pressure.** Evergreens grew from **~$50B to almost $500B** in about 5 years (Olson). Constant inflows must be deployed or the cash
  drag shows up in returns. So pick managers with deep deal origination.
- **Allocation policy is the key diligence question.** Same team? Yes, usually. Same deals? Ask. Pro rata across all funds is the right answer.
  "Except in this case" exceptions deserve scrutiny. Olson frames the risk as A deals versus B deals, not A team versus B team.
- **Drawdown versus evergreen, in Carlyle's terms** (Shane Clifford). On a $100 drawdown commitment, the GP calls $15 here and $23 there over 3-4
  years, and returns come back over a 10-plus-year life. An evergreen takes the full $100 up front, accepts subscriptions monthly, and redeems
  quarterly up to about 5% of fund value. He wants the industry to say "semi-liquid," and treats evergreen and perpetual as the same thing.
- **The legal wrappers are different machines** (Clifford names them; the distinctions are mine):
  - An **interval fund** must repurchase a set percentage at set intervals.
  - A **tender-offer fund** repurchases only when its board decides to.
  - A **BDC** is a lending vehicle that elects '40 Act treatment.
  - A **non-traded REIT** is a tax election that must pay out 90% of income.
  Outside the US, Carlyle uses European fund regimes. "Liquidity" means something different in each wrapper.
- **The BDC as the original retail private-credit wrapper.** David Adelman co-founded FS Investments in 2007 after seeing non-traded REITs sold to
  "middle America" through small broker-dealers. He applied the same wrapper to private credit for PE-backed companies. FS now has about $83B,
  with two BDCs listed on the NYSE. His case for illiquidity is behavioral: it stops retail investors selling at the low, and it lets the fund buy
  in a downturn. Jen agrees it "takes away your worst instinct."
- **The model portfolio being sold.** Clifford proposes replacing 60/40 with **50/30/20**, the 20 in private markets. He argues "alternatives" is
  an archaic label: the choice is private versus public capital, because the Wilshire 5000 has shrunk from ~7,000 names to ~3,500. (It peaked
  nearer 7,500, and the shrinkage also reflects M&A and fewer IPOs, not just companies going private.)
- **Retirement is "the 800-pound gorilla"** (Clifford). The summer-2025 executive order on 401(k) access, with Labor Department guidance expected
  afterward, would let defined-contribution savers do what defined-benefit pensions have done for 40 years. His irony: teachers and firefighters
  already own PE through their pensions without knowing it, while the 30-40-year DC saver, who fits illiquidity best, can't. Jen asked directly
  whether retail is being opened because institutional money is tapped out. He answered with diversification and fairness, not data.
- **Disclosure.** Registered evergreen funds publish holdings and net-of-fee performance on public websites, which institutions used to get
  privately. That is fund-level disclosure. It doesn't answer Kristen's worry, which was about the companies underneath reporting less often.

**Business significance / value:** Managers get a new, sticky capital base. Advisors get a product that behaves like normal investing. The
investor gets access to the "87% of US companies above $100M revenue" that are private. Olson also cites 40% fewer public companies than a decade
ago; Carlyle's head of wealth says the Wilshire 5000 now holds about 3,500 stocks.

**Forces & impact:**
- Institutional saturation, product innovation in older wrappers, and the August 2025 executive order opening 401(k)s.
- More bidders could compress returns by bidding up entry prices. Olson's partial answer: they also bid up exit prices.
- **Volatility laundering** (Shah, concept 3's sibling): marked quarterly, so reported volatility is lower. Shah argues the real reasons to own PE
  are alignment and control, not smoothness. The hosts admit public-market people are partly "jealous."

**With vs. without:** Without wrappers, private markets stay limited to roughly $5M-plus investors and institutions. Retirement savers lose the
illiquidity premium that defined-benefit pensions used to capture for them. Shah's fairness point: the same retirement money moved from pensions
to individuals and lost the asset class along the way. With wrappers, individuals get access along with gating risk, opaque marks and fee
complexity they mostly don't understand ("I guarantee you nobody understands this").

**Applies when / Breaks when:** Works when inflows exceed redemptions, assets are seasoned and cash-generative (secondaries, credit), and investors
truly have long horizons; 401(k)s fit by design. Breaks in a run: redemptions above the cap, gates, investors discovering that the NAV they bought
at isn't a price anyone will pay, and the manager forced to deploy into an overheated market.

**Channel example:** "Goldman Sachs' Head of Alts for Wealth" (Olson). "Morgan Stanley's Head of PE Solutions" (Shah). "Inside Carlyle: How the
$470B+ Private Markets Giant Is Changing the Game" (Clifford; the short "Carlyle's Head of Global Wealth" is clipped from it). "Co-Owner of Philly
76ers David Adelman…" (FS Investments). "Secondaries 201" (secondary firms' '40 Act funds). "PE vs Hedge Funds March Madness Bracket" (short:
Blackstone employees "pitched in to cover redemptions" from a private credit fund).

**Counterpoint:** All three architects of this market (GS, MS, Carlyle) were on camera, and nobody from the skeptical side was. Annual carry
crystallization usually comes with a high-water mark, which tempers Olson's "more expensive" claim somewhat. On the other side, quarterly NAV marks
mean investors entering and exiting transfer value between each other whenever marks lag reality. That issue was never raised. Adelman
praises illiquidity while selling it, and nobody mentions that BREIT gated in 2022-23. Resnick concedes retail buyers face "the same kind of risks"
after Kristen notes the average retail investor spends about six minutes researching a stock.

**The manufacturer's own pitch (primary source).** Blackstone University, *Essentials of Private Markets: Americas* (2025 brochure,
blackstone.com). The guests above describe the pitch; this is the pitch itself, in writing, from the largest manager.
- **Headline exhibit (2016-2024, quarterly index returns).** A 60/40 portfolio returned 9.4% a year with 10.6% volatility and a 2.2% yield. A
  45/10 PE/25/10 private credit/10 real assets portfolio returned 10.4% with 8.8% volatility and a 3.4% yield.
- **Supporting claims.** Stocks and bonds were positively correlated in 66% of calendar years since 1974, so the 60/40 hedge is unreliable.
  Pensions and family offices hold ~30% in private markets, endowments ~50%, and individuals far less. Evergreen funds are presented as the
  "middle path": invested from day one, with NAV subscriptions and redemptions "subject to limits."
- **What the footnotes undercut:**
  - *Fees.* Returns "do not necessarily consider fees and expenses." NFI-ODCE is gross of fees, and the Cliffwater index is gross and unlevered.
    The 1-point edge sits inside a normal private-fund fee load.
  - *Smoothing.* The private legs are appraisal or IRR-based indices, so the 1.8-point volatility "improvement" is partly volatility laundering
    (above).
  - *Apples to oranges.* Cambridge PE and infrastructure figures are pooled horizon IRRs, set against time-weighted public returns.
  - *Window.* Nine years, chosen as the "earliest common available data." Mostly zero rates, plus a 2022 where public marks fell and private
    marks lagged.
  - *Silence.* Gates appear only as "subject to limits." The brochure doesn't mention that Blackstone's own BREIT limited redemptions from December
    2022 into early 2024.
- **The tell:** manager selection is framed as the critical decision, and the criteria named (scale, staying power, track record) describe the
  author.

**Links:** [[unit-10-personal-finance-operating-system]], [[canon-taleb-black-swan]] (smoothness is not safety), [[trading-floor-mechanics]],
[[canon-klarman-margin-of-safety]] (who is selling, and why).

## 9. The wealth distribution chain: manufacturer → platform → advisor → client

**What it is:** The value chain that sells private funds to individuals. The hosts use a **pharma analogy**:
- **GPs are drug makers**: they do the R&D, buying and fixing companies.
- **Wealth advisors are doctors**: they know the patient's risk tolerance and horizon.
- **The platform is the pharmacy formulary**: advisors can only prescribe what the firm's curators put on the shelf.

**How it works:**
- **Goldman's three layers** (Olson):
  - Investing experts, both proprietary and external manager selection. GS has **$540B+ in alternatives** and has been at it since its late-1980s
    merchant bank.
  - Platform curation.
  - Advisors working the whole client relationship. The **average GS wealth client has $75M** there, as close to institutional as individuals
    get. GS's moderate-risk model allocation went from **20% to 27% alternatives** over 25 years.
- **CAIS** puts the process "on digital rails": discovery, a 60-page subscription doc digitized, transaction, reporting and custody links. Founded
  in 2009, it pairs ~600 advisors with 50+ managers at its summit.
- **Wealth versus asset management** (Levine, BNY Wealth). Same investing skill, different client: individuals instead of institutions. That
  makes the business personal, built on legacy and family, and **tax-driven**. A tactical shift must pay over 12-18 months to justify the tax
  bill. Many alternatives throw off **ordinary income** instead of long-term capital gains, which matters to taxable clients.
- **The manufacturer's sale, institutional versus wealth** (Clifford, Carlyle). "Global Wealth" isn't wealth management. It is selling Carlyle funds
  *through* wirehouses and private banks to end clients like "my father-in-law, a retired dentist." That is business to business to consumer.
  - **Institutional finals:** about 30 minutes before trustees, the CIO's staff and an investment consultant, with an 80-page deck of which you
    reach 20 slides.
  - **Wealth:** 5-6 minutes with an advisor ("10 max on a good day"), a 3-page deck, and a story the advisor can retell to the client in under
    two minutes. A real-estate fund sells itself ("you'll own part of One Vanderbilt"); managed futures don't.
  - **Scale math:** about 300,000 US advisors; reaching 75-100k is "a really good job." That can't be done in person, hence video under five
    minutes and social media. This is also why Carlyle sponsors Red Bull's F1 team: the audience is global and "40 plus %" female, per Clifford.
- **Industry shape: the dumbbell** (Clifford). Large multi-strategy platforms at one end, niche specialists at the other, and the middle squeezed,
  because sovereigns and big wealth platforms want "more things with less partners."

**Business significance / value:** Platforms become **gatekeepers**. A smaller GP that wins a spot on Goldman's shelf has effectively outsourced
its fundraising. Ten to fifteen years ago, managers said "thanks but no thanks" to wealth capital. Now they call asking how it works. Capital from
individuals is expensive to serve: lots of small tickets, quarterly transparency, education, and staff to cover advisors. That's why managers
waited until they had to.

**Forces & impact:** Shrinking public markets, institutional saturation, millennials' interest in private tech (90%-plus "know about alts" per a GS
survey), and regulation. Second-order effects: wealth roles gain prestige and pay, and IR and marketing at small GPs are rebuilt around getting on
platforms.

**With vs. without:** Without platforms, each GP must build its own retail distribution, so only megafunds can do it. With them, distribution power
concentrates in a few banks and fintechs, which earn fees on access.

**Applies when / Breaks when:** Works when the curator's diligence is independent. It breaks when the platform has its own funds on the shelf,
which is the conflict Goldman's dual role raises. Olson says GS also builds pure third-party portfolios on request.

**Channel example:** "Goldman Sachs' Head of Alts for Wealth." "Apollo's Quest to Double AUM… and the CAIS Summit." "Time to Sell? feat. Alicia
Levine of BNY Wealth." Apollo targets doubling from about $700B AUM in five years, and it marketed to younger investors with memes and holiday
videos.

**Counterpoint:**
- The pharma analogy cuts both ways. Formularies are shaped by rebates, and pharmacies by what pays.
- The hosts also mock "democratization." The products reach accredited investors ($1-2M), not everyone, though some interval funds carry no
  minimum and no carry.
- Levine adds a sober note: her firm holds **no crypto allocation**, because risk-adjusted returns matter more than absolute ones.

**Links:** [[canon-jensen-meckling-agency-theory]] (Bessemer's "same side of the table" contrast in [[tiger-sisters-private-capital-101]]),
[[unit-10-personal-finance-operating-system]].

## 9b. The advisor: wirehouse and private bank vs RIA vs multi-family office

**What it is:** The last link in concept 9, the person who actually puts the client into a product. Three models compete:
- **Wirehouse / broker** (Merrill, Morgan Stanley, UBS) and **private bank / trust company** (JPMorgan Private Bank, Goldman PWM, Northern Trust,
  Bessemer). Advisors work inside a firm with a product platform and its own balance sheet.
- **Independent RIA** (Registered Investment Adviser, SEC-regulated). Wealth management is the whole business, and there is no proprietary product
  shelf.
- **Multi-family office (MFO).** An RIA serving a few very large families with investment advice plus bill pay, household payroll and estate work.

**How it works:**
- **Client tiers** (Tony Abatti, SCS Financial).
  - McKinsey's ultra-high-net-worth line is $25M. SCS's floor is $50M, its average client about $150M, and retention 98%.
  - It needs 10-12 new clients a year, about $1.5-1.8B of new relationships (my arithmetic).
  - At $1M, planning means budgeting and college savings. At $200M it means gifting, estate insurance, philanthropy, jets, and an "outsourced
    CFO": one sheet consolidating every trust, GRAT, policy, loan to a friend, and the $50k "scars" in friends' restaurants.
- **How the money is made.**
  - Brokers earn commissions or a share when they sell a product, such as the firm's real-estate fund.
  - RIAs charge a fee on assets. Abatti cites ~1% as the industry norm and the industry's reputation as overpriced, watered-down product.
  - At a wirehouse, pay is "you eat what you kill": no reviews, MD on hitting a revenue formula, and the formula renegotiated in bad years.
- **The shelf conflict** (Susan Moffett, Curated Wealth Partners). A platform approves 20-40 managers per category, and managers often share fees
  with the bank to get on the list. Her test for a cheap big-bank quote: "they're not earning less, they're just getting paid by somebody else."
  Her RIA "only gets paid by my client." She says banks have settled lawsuits over this in the last decade (none named).
- **Why RIAs "caught fire" about 15 years ago** (Moffett). The bank bundle came apart:
  - Independent research became buyable.
  - Reporting and tech tools reached scale, so a two-person RIA is viable.
  - Brokers broke away from Merrill and Morgan Stanley, and assets followed.
  - Custody moved to Schwab and Fidelity.
  - Asset managers (KKR, Apollo, even JPMorgan Asset Management) built sales forces to sell to RIAs, so independents now get the same products.
- **Pooling versus segregation for private funds.**
  - SCS pools clients into one LP line. Going to Andreessen Horowitz with $100M made of $1M tickets gets "no thanks"; one SCS line gets a
    yes. SCS leaned into private allocations in 2008-09, when institutions were overallocated, and kept that access.
  - Curated keeps each family's portfolio segregated, built around its illiquid "rocks" such as a family business or the principal's own fund.
- **The tax lens** (Abatti). A 9% private-credit yield is about 4% to a top-bracket Californian. That is consistent with ~37% federal + 3.8% NIIT +
  13.3% state ≈ 54% (my arithmetic). Rebalancing is free for an endowment and a taxable event for a family. Judge managers after tax and after
  fees.
- **Single- versus multi-family office** (Moffett). Below roughly $2.5-3B of net worth, a family can't pay enough to keep top staff in its own
  office, so turnover follows and an MFO is cheaper.
- **What stays at the banks:**
  - Balance sheet and lending. A Curated client keeps a $10M relationship at JPMorgan to get a good credit line.
  - Brand and perceived safety.
  - For a family office, execution and access. Family offices use banks "as a counterparty and not as a partner."

**Business significance / value:**
- In the bank model, the firm captures the advisory fee plus product revenue on the other side, and wins the lending.
- In the RIA model, the advisory fee is the main revenue, so value shifts to the advisor-owners and to custodians.
- For a GP, the RIA channel is a second route to wealth capital that bypasses the wirehouse formulary.

**Forces & impact:**
- Unbundled technology, the breakaway movement, and asset managers selling direct to RIAs.
- Reputation spillover from scandals elsewhere in the bank. Moffett became a "professional apologist" for the London Whale.
- Taxes (New York and California top brackets).
- **Second-order:** the advisor who sells alternatives is now often independent. That raises the stakes on independent diligence (concept 8) and
  on how GPs reach 300,000 advisors (concept 9).

**With vs. without:** Without RIAs, private-fund access for individuals runs only through bank shelves with embedded revenue sharing. With them,
clients get conflict-lighter advice, but lose a balance sheet, a training pipeline and some scale, and still have to bank somewhere.

**Applies when / Breaks when:** The RIA model works when the client values independence and planning over trading ideas. Abatti says clients who
want to trade daily belong at JPMorgan, Goldman or Morgan Stanley. It breaks when an RIA is too small to diligence private managers, or when its
asset fee quietly discourages paying down debt or spending.

**Channel example:** "Private Wealth Management 'PWM' 101 (for the Ultra Rich)" (Abatti). "PWM 102: RIAs vs. PWM at a Big Bank ('Wirehouses')"
(Moffett).

**Counterpoint:**
- Both guests run RIAs and pitch independence against the firms they compete with.
- Neither names RIA conflicts: asset fees reward gathering assets, custodians earn on client cash sweeps, and private equity has been rolling RIAs
  up, which brings back the shelf pressure.
- No grid percentages, recruiting loans, Broker Protocol mechanics or the fiduciary versus Reg BI standard are discussed.
- Moffett's definition implies wirehouse advisors are independent; most are employees.
- Her claim that Schwab "takes no risk" ignores its 2023 deposit stress. The real protection is that client securities are segregated.
- Abatti's "$25M is top 2%" is wrong. The top 1% of US households starts around $10-14M of net worth, so $25M is rarer still.
- His Massachusetts-versus-Florida estate example ($16M state tax on $100M vs zero) uses the top marginal rate and omits the federal estate tax,
  which applies in both states.

**Links:** [[canon-jensen-meckling-agency-theory]] (who pays the agent), [[unit-10-personal-finance-operating-system]],
[[tiger-sisters-wealth-mechanics]], [[tiger-sisters-private-capital-101]] (Bessemer, "same side of the table").

## 10. Real estate PE: risk buckets, cap rates and true yield

**What it is:** Institutional investing in physical property (multifamily, industrial, office, retail, student and senior housing, data centers).
It's organized by **risk bucket** and valued by **cap rate**, not EV/EBITDA.

**How it works:**
- **Risk buckets** (Deborah Smith):
  - **Core:** stabilized, cash-yielding, the REIT-like model.
  - **Value-add:** returns from cash plus appreciation earned through capex (new kitchens, landscaping).
  - **Opportunistic:** new development, land, speculative projects with no cash flow yet.
- **Vehicles** (Hochfelder). MS's business started in the early-1990s S&L-crisis era with closed-end opportunistic funds targeting about **20%
  returns**: 4-year investment period, 10-year life. Open-ended core funds have quarterly, semi-liquid redemptions.
- **Cap rate = NOI / value**, the inverse of a multiple. A **lower cap rate means a higher price.**
  - $5M NOI at a 4 cap is worth $125M. At a 6 cap it's worth $83.3M, a 33% drop from a two-point move (my arithmetic).
  - **Negative leverage:** core multifamily in DC traded at 3-3.5 caps while the 10-year sat at 4.2-4.3%. Financing a 4% yield with 6% debt
    *lowers* the equity return, so transactions froze.
- **True yield versus advertised cap rate.** In US office, landlords pay for tenant buildout and big leasing commissions every time a lease rolls.
  That recurring capital sits "below the line," so the cash an owner collects is far below the quoted cap rate. MS pulled back from US office
  *before* COVID for this reason. In Japan, tenants pay for their own buildout.
- **Net lease** (tenant pays taxes, insurance and roof) protects landlords through cycles.
- **Flight to quality.** San Francisco office is about **37% vacant**, yet MS's best buildings get record rents. Demand consolidates into an "oasis
  in the office desert." NYC office utilization went from ~5% at the COVID trough to the 70s.
- **Deal terms:** about **60% LTV** is standard, often a floating-rate 3+1+1-year loan for transitional assets. Value-add commonly runs about 65%
  leverage.
- **Theses ride demographics:** e-commerce drove industrial, an aging population drives senior housing, and millennials now want larger suburban
  homes. Developers "develop to the rearview mirror," building what tenants wanted last cycle.
- **The owner-operator's version** (David Adelman, Campus Apartments, ~25,000 student beds in 23-24 states).
  - **Leverage worked example.** Buy at $1M with $700k debt and $300k equity; the tenants' rent services the debt.
    - At ~3% appreciation the building reaches ~$1.45M while the loan amortizes to ~$450k, so equity is ~$1.0M on $300k.
    - That implies a 12-14-year hold (1.03^12 ≈ 1.43), and his numbers ignore capex and vacancy.
    - A cash-out refinance then returns the original equity to fund the next deal.
    - He calls real estate "a get-rich slow business."
  - **Fixed-rate debt as a "one-way option."** 10-year money locked at ~4% a few years ago against 6.5-7% now. It isn't free: prepayment
    penalties lock you in if rates fall.
  - **Pricing rule** from his mentor: "if you're full, 100% full, your rents are too low."
  - **Location rule:** avoid schools with capped enrollment. A captive audience that refills every year beats equilibrium.
  - **Hotels:** the brand on the building takes ~9% off the top with no capital committed. In his view the franchisor has the best business in real
    estate (see [[unit-09-capital-light-businesses]]).
  - **Net lease** is only as good as the tenant. CVS, Walgreens and Rite Aid leases looked like annuities until those tenants' credit fell.
- **Housing lock-in, in payments** (real-estate news episode). Moving from a 2% to a 7% mortgage roughly triples the monthly payment, which is
  why owners don't sell. Three to four months of inventory or less marks a seller's market. The mortgage-interest deduction cap fell from $1M to
  $750k of principal in 2017.

**Business significance / value:** Real estate offers both current cash flow and appreciation, an inflation hedge (rents tend to track or beat
inflation, and the asset reprices with it), and efficient financing. Hochfelder calls it arguably the third-largest asset class. Banks advise the
*managers* of capital: the top 10 control $1.5-2T and the top 20 control $2.5-3T, with Blackstone first and Brookfield second (Smith). Boutiques
without balance sheets compete on advice in the $2-15B-manager middle market.

**Forces & impact:**
- Base rates feed directly into cap rates, though Hochfelder says less tightly than people assume, because income growth drives much of the value.
- Supply chain shifts move industrial demand: India-sourced goods land at East Coast ports, China-sourced at West Coast ones.
- Tariffs and onshoring.
- Housing affordability. Hochfelder's answer is new supply, including build-to-rent communities.
- A related policy short: a proposal to eliminate capital-gains tax on primary residences. The exclusion has been **$250k/$500k since 1997**, when
  the median home cost about $145k versus about $417k now. It targets the "stay-put penalty," but mostly helps wealthier owners.

**With vs. without:** Without institutional capital, large-scale new supply, professional management and purpose-built niches like student and
senior housing don't get financed at scale. Single-family "PE buys up the neighborhood" is the backlash case. MS says it never played there.

**Applies when / Breaks when:** Works when NOI grows and cap rates sit sensibly above debt costs. Breaks with negative leverage, capex-heavy
sectors priced on headline cap rates, or obsolete stock that can't be converted. 1980s office towers have sealed windows and too few bathrooms for
residential use.

**Channel example:** "Real Estate Private Equity 101 feat. Lauren Hochfelder." "Real Estate Investment Banking" (Deborah Smith). "Co-Owner of Philly
76ers David Adelman on Sports Investing, Real Estate and Early Stage Investing." "Real Estate News, Meme Stocks…" (housing).

**Counterpoint:** Hochfelder says real estate values rose in seven of the last eight S&P downturns. Private real estate is **appraisal-marked**,
so that is partly volatility laundering (concept 8): REIT prices, marked daily, fall with stocks. "Cash flows tend to grow faster than inflation"
also depends on lease structure. Long fixed leases lag.

**Links:** [[unit-06-whats-a-business-worth]] (multiples versus yields), [[unit-09-capital-light-businesses]] (the opposite of capex-heavy office),
[[canon-klarman-margin-of-safety]].

## 11. The CRE refinancing wall and gap capital

**What it is:** Commercial real estate loans are short (3-5 years, often floating). Properties bought with cheap 2020-21 debt must refinance at
higher rates and **lower loan-to-value**, which opens a funding hole that equity holders must fill or lose the asset.

**How it works:**
- **Smith's sequence.** Bought at 65% debt "when money was practically free." The refinance now costs 5-6%, and the lender will only lend 50-55%.
- **Illustration (mine).** A $100M purchase with $65M debt and $35M equity. The value falls to $85M as cap rates widen. A 55% refinance yields
  $46.75M, leaving an **$18.25M gap**, while the equity is now worth $20M instead of $35M.
- **Three outcomes:**
  - **Extend** ("kick the can," common if NOI is still growing).
  - **Hand back the keys.** Lenders often don't want them: "what do you want me to do with it?"
  - **Fill the gap with preferred equity or mezzanine debt** at higher cost, from funds formed for exactly this. Smith notes the same thing
    happened after the GFC.

**Business significance / value:** Rescue capital earns high single- to low double-digit yields, senior to the old equity. Banks avoid
crystallizing losses on properties they hold at above-market marks. Owners of buildings with rising NOI can grow into the old debt.

**Forces & impact:** Rates, tighter credit standards, sector-specific obsolescence (office, empty big boxes), and the rise of debt funds,
insurance-company lending and CMBS as alternatives to banks in the US. Europe and Asia remain bank-dominated.

**With vs. without:** Without gap capital, more forced sales, a faster price reset, and bigger bank losses. With extend-and-pretend plus mezzanine,
price discovery is slower and losses are spread over time. Smith notes that after the GFC everyone expected repricing, "and here we are down at 3%
cap rates again."

**Applies when / Breaks when:** Extension works when assets perform and rates are expected to fall. It breaks for structurally impaired assets,
like the downtown San Francisco office the hosts say "you can't even give away."

**Channel example:** "Real Estate Investment Banking" (Smith, recorded around March 27).

**Counterpoint:** Smith's optimism is that "the real estate markets always bounce back." That holds for the sector, not for individual capital
stacks. Equity in a 2021 office deal can be wiped out even if office eventually recovers.

**Links:** [[canon-klarman-margin-of-safety]], [[unit-04-is-it-healthy]].

## 12. Infrastructure: essential assets bad management can't kill

**What it is:** Private equity-style ownership of airports, toll roads, utilities, pipelines, fiber, towers, data centers and LNG terminals. These
are **essential services with very high barriers to entry**, held for 20-30 years.

**How it works:**
- **The defining insight** (Dorrell). Most businesses die if mismanaged. A badly run airport or utility doesn't, because nobody can build a rival.
  That reliability supports very favorable financing. His comparison: Buffett's ideal-business checklist reads like a description of
  infrastructure (BNSF railroad, utilities).
- **Origin story:**
  - Macquarie's tax group, experts in cross-border leasing (depreciating one $100M jet in two countries), saw Australian states privatizing toll
    roads and airports in the mid-1990s.
  - With no balance sheet and no local PE industry, they **listed a vehicle on the ASX to raise retail money purely to bid**. Macquarie earned
    management fees, carry *and* M&A advisory fees on it.
  - The US came late because **muni bonds** gave public owners a tax-advantaged cost of capital: a 6% taxable yield is roughly a 4% muni yield.
  - The US industry launched around 2006 out of investment banks, staffed by energy, transport, muni and project-finance bankers rather than
    seasoned PE teams. MS raised about $3B and GS about $5B for first funds, versus the $2B that would count as a triumph for a famous PE spinout.
- **Allocations:** US pensions run about 3-4% to infrastructure. Canada, Australia, Europe and the UK went from 1% to 10%-plus, mostly equity.
- **Risk and return:** between private credit and PE on both risk and return, but with **duration** as the differentiator. 15% a year for 5
  years ≈ 2.0x; 15% a year for 20 years ≈ **16.4x** (my arithmetic). Dorrell compares it to sprinting a marathon.
- **Three buckets, about 90% of Stonepeak's deals:**
  - **Digital:** data growth, plus AI raising capital needs about 10x.
  - **Energy:** both transition and traditional. **PJM** (the eastern and Midwestern grid, including Northern Virginia) has **~8% annual load
    growth** after 20 flat years. Capacity prices, set three years ahead by auction, rose roughly **tenfold** in the latest auction.
  - **Transport and logistics:** reshoring, friend-shoring, resiliency.
- **The data-center split.** A 20-year contract with Google, Microsoft or Amazon isn't speculative. A field-sited training center leased to a
  cash-burning AI startup that can't self-fund is. The test: if everything goes wrong, do we get our money back plus a modest return?

**Business significance / value:**
- Investors buy low-volatility, inflation-linked cash flows and pay for them with lower returns ("no free lunches").
- Governments get capital and operating skill. Privately run airports (the LaGuardia rebuild, Sydney) are measurably better, and governments can
  collect more tax from increased traffic.
- **Regulation is the price of monopoly:** a utility can't charge what it likes.

**Forces & impact:**
- **Permitting** is the binding constraint, federal and local. Dorrell sees a possible "grand bargain": permitting reform for Republicans, green
  energy support for Democrats.
- **Rule changes mid-project** destroy investability. The Dakota Access pipeline was stopped *while operating*. Solar projects were stranded by the
  2025 tax changes.
- Power prices will rise as data-center demand hits capacity prices, and Dorrell expects big tech to collide with local governments over who pays.
- NIMBY opposition and eminent domain explain why US high-speed rail stalls.

**With vs. without:** Without private infrastructure capital, rebuilding depends on government budgets and muni debt, so assets age. Dorrell's
Sydney example: toll roads people resent are options that wouldn't exist otherwise, because the free back roads remain. With it, users pay tolls
and parking fees ("you'll pay a fortune to park") and political backlash follows.

**Project finance, the debt underneath** (Project Finance 101, ex-Morgan Stanley/Carlyle energy team).
- A project (power plant, toll road, refinery, wind farm) sits in its own entity, and the lenders' only recourse is that asset's forecast cash
  flows.
- So a single-B utility can build a plant without its corporate rating taking the debt. In exchange the lenders demand far stricter covenants.
- Compared with munis: a muni toll road is backed by a government sponsor. A project-financed one must repay entirely from its own tolls over
  the asset's life.
- **A closed system.** There is a construction period with no cash flow, and contractor terms decide who bears construction risk. Then comes a
  fixed operating business. You can't grow a toll road the way you sell more widgets.
- **The buyer's lever is re-risking.** Hedge a power plant's gas input and power output with a bank commodities desk for 5-7 years and it becomes
  almost an annuity, which supports more debt and a schedule to pay it down.
- The team's Carlyle energy fund launched as "mezzanine" because 2009 was a record mezz fundraising year. LPs called it "so 2009," so it
  invested across the capital structure (a 14% first-lien loan, sub debt, a refinery bought outright). They put the platform at "$45 billion";
  that is almost certainly ~$4.5B misheard.
- The mechanics are taught in depth in [[wss-ai-economics]] §7 (data-center SPVs). They are not repeated here.

**Applies when / Breaks when:** Works with stable rules, a contracted or regulated revenue base and creditworthy counterparties. Breaks with
regulatory reversals, speculative counterparties, or a utility regulator that takes the investor's side of the bargain away.

**Channel example:** "Move Over Private Equity. Private Infrastructure Investing: AI Boom Beneficiary? feat. Mike Dorrell" (Stonepeak, about $80B
AUM). "49. Project Finance 101 & Infrastructure Investing Basics."

**Counterpoint:**
- "Private operators will do a better job every single time" is a fundraiser's line. Thames Water is the standard counterexample: privatized,
  over-levered, under-invested.
- The "70% of internet traffic goes through Northern Virginia" figure is a widely repeated but unsupported statistic. Treat it as "largest
  data-center market," nothing more precise.
- His claim that finance-trained investors beat operators at investment decisions is candid but self-serving.

**Links:** [[canon-helmer-7-powers]] (cornered resource and barriers), [[canon-klarman-margin-of-safety]] (the "get our money back" test),
[[canon-porter-competitive-strategy]].

## 13. Home-equity investments (HEIs): selling a slice of your house

**What it is:** A homeowner sells a percentage of the home's equity to an investor for an upfront cash payment, with **no monthly payments and no
interest**. They settle when the home is sold or refinanced, or at term (typically 3-5 years in Findley's framing).

**How it works:**
- **Findley's example.**
  - Bought in 2020 for $800k with a $600k mortgage at about 3%. The house is now worth about $1M.
  - The originator haircuts the value 25% for local price volatility: $750k − $600k = $150k of "adjusted" equity.
  - It pays **$50k for one-third of the equity.**
  - Sell tomorrow and you owe ($1M − $600k)/3 = **$133k**.
  - Later, you owe a third of whatever the equity turns out to be, so the originator shares the downside too. It lost money on San Francisco
    condos during COVID.
- **Why borrowers use it:**
  - A HELOC requires roughly a 750-780 FICO, and is hard to get for 1099/K-1 earners and investors.
  - Refinancing means giving up a 2-3% mortgage for 6-plus%.
  - Findley pitches it as **credit-curing**: pay off about $50k of credit cards at 18-26%, rebuild the FICO, graduate to a HELOC.
- **Market context** (Jen's Fed and ICE data): household debt $18.8T (Q1 2026, +$4.6T since 2019), credit cards $1.25T, and $17.8T of home equity
  of which $11.6T is "tappable."
- **Returns and pipeline:** about **17% average returns** since 2015 (Bloomberg, via Jen). Tacora buys from originator Point (a16z- and
  WestCap-backed), which is licensed state by state in ~40 states. **Not in Texas**, which limits corporations on title.

**Business significance / value:** It turns illiquid, locked-in home equity into cash without debt service. The investor buys diversified,
housing-linked, long-duration equity with no coupon, an asset "without a natural buyer." That is Tacora's role: asset-based capital for
venture-backed originators. Tacora grew from a $350M fund I (2022) to $700M at fund II's hard cap, about $1.5-1.6B in total.

**Forces & impact:** The **mortgage lock-in effect** (2-3% legacy rates versus about 6.4% today), the K-shaped consumer (wages up 2-3% in real
terms while housing, cars, insurance and groceries are up 60-80%), tight post-GFC credit standards, and a housing undersupply that should support
prices for 5-10 years.

**With vs. without:** Without HEIs, a house-rich, cash-poor owner can only sell, refinance at a high rate, or borrow on cards. With them, liquidity
comes at the price of giving up upside, with the investor absorbing some downside.

**Applies when / Breaks when:** Works with rising or stable local prices and a borrower who would otherwise pay 20%-plus. It breaks in a 2008-style
national decline (Findley concedes this) and for borrowers who misunderstand the cost.

**Channel example:** "Hedge Funds Want the Equity in Your Home, feat. Tacora Capital Founder Keri Findley."

**Counterpoint (the most important one in this note):** Run Findley's own numbers. Settling immediately turns $50k into $133k for the investor,
about **2.7x on day one**, because the 25% haircut is a discount the homeowner pays up front. Flat prices over 5 years still leave the owner owing
at least $133k. A $50k loan at about 9% for 5 years costs roughly $77k in total. Real contracts include caps that limit this, but the product's
"no payments" framing hides a high implied cost of capital. The haircut is also the investor's margin of safety: the home can fall 25% before the
investor loses a dollar. The ~17% investor return is the homeowner's cost. The hosts, both CDO alumnae, didn't press the point.

**Links:** [[canon-klarman-margin-of-safety]] (the haircut as margin of safety), [[unit-10-personal-finance-operating-system]] (debt versus
equity for a household).

## 14. Entrepreneurship through acquisition (ETA) and search funds

**What it is:** Becoming a CEO by **buying** an existing profitable small business rather than founding one. There are two main models: the
**search fund** (investors pay you to search, then fund the deal) and the **self-funded search** (your own savings, raising only once you find
the deal).

**How it works** (Jesse Sapphire):
- **Search-fund economics.** Search capital converts into deal equity with a step-up. The searcher holds no common equity up front but receives
  about **25% of the gain above purchase price plus a hurdle**. That's a carry-like option, which suits fast growers (home-health staffing, SaaS)
  and argues for the biggest deal you can run. It fits poorly with slow, single-digit businesses whose equity is built mostly by paying down debt.
  Typical real-world structures vest that roughly 25% in tranches: at acquisition, over time, and on IRR hurdles.
- **Self-funded.** You own the equity outright (Sapphire owns 100%). So target a "**cockroach**": single-digit growth, a long profitable record
  (ABG has operated since 1992 and survived 9/11 and the GFC), an explainable business, and a sector where you're the ideal customer.
- **Size bands** (rough):
  - SDE (seller's discretionary earnings, which adds back the owner's pay) of $0-1M: main-street buyers.
  - About $0.5-3.5M EBITDA: self-funded searchers. ABG was about $1.3-1.5M. His search box was $0.75-2.5M.
  - Larger: search funds.
  - About $5-20M EBITDA: LMM PE.
- **Sourcing.** Brokers take about **10%** of price. Sapphire mailed a brochure to roughly 250 brokers. One called 18 months later, and the deal
  fell apart twice in a two-year process. You're "the worst kind of buyer": little money, not strategic, no industry experience, risky to lend to.
- **Debt stack** (example: $10M price):
  - About $6M bank or **SBA** debt. SBA loans run 10 years; **anyone owning more than 20% must personally guarantee**, which rules SBA out for
    funded search.
  - About $2M equity.
  - About **$2M seller note**: second lien, sometimes on standby, sometimes forgivable instead of an earnout. Banks treat it almost as equity
    because it keeps the old owner invested in the transition.
  - Classic trade-off: price *or* liquidity. A seller who wants top dollar finances part of it.
  - These are **"airball" loans** against cash flow with no hard collateral. His borrowing rate is **11.5%**.
- **Asset deal versus stock deal.** In an asset deal the buyer leaves past liabilities behind and gets a stepped-up tax basis. He used a
  **338(h)(10)** election: legally a stock deal, taxed as an asset deal.

**Business significance / value:** The seller (often around 75 years old, without a successor) gets liquidity and legacy. Many sell to "the next
version of them" rather than to PE. The buyer gets revenue, profit and staff from day one. Sapphire's short puts the comparison plainly:
starting a company takes irrational exuberance, while buying one means revenue, profit and good people on day one. Sapphire argues W-2 careers carry under-appreciated
risk. He lost five CEOs and the clients he printed for included Signature, SVB and Credit Suisse.

**Forces & impact:** The boomer business-succession wave, interest rates (debt service on an 11.5% airball), and SBA program rules.
**Time horizon** turns out to be decisive. In COVID, ABG's revenue fell **95%** and staff went from 24 to 4. A 3-5-year search-fund clock would
have shut it in April 2020. Permanent capital, PPP and a fully drawn revolver kept it alive. **2024 revenue beat 2019.**

**With vs. without:** Without ETA, many founder-owned firms close or sell to consolidators when the owner retires. When it breaks, the buyer over-
"strategizes." Sapphire tells the story of a snowplow-company buyer whose real problem was afternoon Wi-Fi dropping a third of orders. Or the deal
dies on hidden concentration, such as five "separate" top clients all referred by one person who golfs with the owner.

**Applies when / Breaks when:** Works with patient capital, humility ("you are the only thing that changed"), and diligence into concentrations.
Breaks with leverage plus a shock under a forced-exit timeline.

**Channel example:** "Entrepreneurship Through Acquisition 101" (Jesse Sapphire, ABG Print).

**Counterpoint:** One survivor's story. His "75% of searchers find a deal" is above the Stanford search-fund study's roughly 60-65%. The 25%
carry-like structure he described (he didn't take that route) simplifies the tranche vesting. Repo baseline: [[tiger-sisters-wealth-mechanics]]
claims about 60% of small-business sales include seller financing. This note adds why banks *want* the seller note and where SBA's
guarantee rule bites.

**Links:** [[tiger-sisters-wealth-mechanics]], [[entrepreneurship-operator-playbook]], [[canon-akerlof-market-for-lemons]] (seller information
advantage, reps and warranties).

## 14b. Venture capital from the outside in: fund math, the founder's terms, and when not to raise

**What it is:** VC is equity for young, unproven companies, raised from LPs into a fund that must return multiples of itself. This section covers
what the channel adds from two outside views: the LP's (how the fund math constrains every check) and the founder's (what taking the money
commits you to). The firm-level view of seed funds is in [[primary-venture-partners-insights]], [[harlem-capital-vc-insights]] and
[[apply-wss-to-venture]].

**How it works:**
- **Angel versus fund** (Camilo Acosta, VC 101, Sept 2023).
  - An angel's $25k check only has to come back 2-3x.
  - A $100M fund has to return $300-500M to be good, so each winner must be enormous. Camilo: it's "much easier to make money as an angel."
  - The LP ladder runs from high-net-worth individuals and family offices to funds of funds, then endowments, foundations and pensions.
- **Stages keep moving.**
  - Pre-seed: idea, team, maybe an MVP.
  - Seed: product in market, roughly $10k MRR, under $1M ARR.
  - Series A at $1-2M ARR. A story alone no longer raises an A.
  - B onward are growth rounds judged on unit economics and a path to a $5-10B company.
  - Crossover funds (Tiger, Coatue) pushed down into the A, blurring late VC into growth equity.
- **Fees and carry.**
  - 2 and 20 is the norm. First-time funds often charge 2.5%, and Sequoia and Founders Fund-tier firms 3 and 30.
  - Carry arithmetic (his example, my completion): a $20M fund grows to $100M, profit $80M, GP carry $16M, LPs $64M plus their $20M back.
  - Carry is paid only on realization, which is why skill takes about a decade to judge.
  - The GP commit is ~1% of the fund, sometimes "cashless": management fees are waived and diverted into the commitment.
  - The firm usually sits in three entities: the LP fund, the management company and the general partner.
- **Returns are bimodal.** VC is "the highest returning asset class" only in its top quartile. Camilo says the average fund returns about 1x, and he
  expects many firms to be wiped out. UTIMCO's $129M across Union Square Ventures funds returned $1.18B, about 9.1x (my arithmetic).
- **SAFEs and pre/post-money.** A SAFE (Y Combinator) is a right to future equity that converts at the first priced round. Camilo calls it an
  interest-free note, which is wrong: it is not debt. A "$2M on $10M" raise matters by definition:
  - $10M pre-money means a $12M post, so the investor owns 16.7%.
  - $10M post-money means the investor owns 20%.
  His fund targets 5% ownership at entry. A Series A lead wants 10-20%.
- **Liquidation preference** (FareHarbor founder, "Mark Cuban told him not to take VC"). Teach it correctly, because the guest's version was
  wrong:
  - **1x non-participating.** $50k for 0.5% at $10M. On a $20M sale the investor takes the greater of $50k back or 0.5% × $20M = $100k, so $100k,
    2x. On a $4M sale it takes $50k back if the preference stack fits under the price, versus $20k pro rata.
  - **Participating.** The investor takes $50k *and then* $100k, $150k in all. That "double dip" is what the guest described as normal. It isn't
    standard in modern VC.
  - His practical rule is sound: before writing a check, get in writing whether the valuation is pre or post, what percentage the money buys, what
    you receive at a $100M exit, and the preference terms.
- **Why not raise** (FareHarbor: booking software for tour operators, sold to Booking Holdings).
  - About 300 staff and $30-50M of revenue in three years, funded by $5M of venture debt with an equity kicker to buy a competitor. No VC equity.
  - About to raise $100M, they met Mark Cuban, who called it "vulture capital" and said to take it only if you have a "slot machine": a known CAC
    and LTV where $100M in reliably becomes $200M out.
  - The founder's arithmetic: with $100M of preferred on top, a $250M sale stops working for the investors. You need $1B or more, and to get there
    you hire 700 people, add legal and HR, and lose the lean "local maximum" when profit peaks and an acquirer pays most.
  - They sold for about $250M a year later. The episode title says $300M; the guest says $250M, matching public reports.
- **Angel discipline** (same guest).
  - Open with "not investing right now, but I'd love to look," which protects the friendship.
  - Invest only when founders have put in their own money and sold something.
  - Distinguish a good *business* from a good *investment*: an investment needs a buyer and a timeline.
  - Prefer bottom-up evidence (1,000 units sold out from one influencer post) to "0.5% of a $1B market." He garbled that as $50M; it is $5M.

**Business significance / value:**
- VC turns founder risk into a portfolio bet in which a few winners pay for everything. The fund captures value through ownership in the winners.
- Late entrants capture less. Damodaran's Instacart chart, which Kristen cites, showed returns falling round by round, with the last rounds
  negative.
- For founders, VC buys speed at the price of a higher exit bar and loss of control. Board seats usually arrive at the Series A.

**Forces & impact:**
- Rates: "TINA" became "TARA" (there are reasonable alternatives) at 5.5-6% risk-free, so LPs demand more of risky funds.
- The 2022 denominator effect (concept 6).
- Exits stuck behind private giants such as Stripe, so funds run to year 12 and beyond (one cited in year 17).
- AI: "wrapper" startups have no moat and turn capital-intensive. Camilo prefers the infrastructure layer: "we're still in the 80s and 90s of AI."

**With vs. without:** Without VC, companies with expensive, uncertain paths (deep tech, network effects) don't get built, and founders grow on
debt and cash flow as FareHarbor did. With it, the preference stack and fund math decide which exits count as success. A $250M sale can be a
triumph for a bootstrapped founder and a failure for a $100M fund.

**Applies when / Breaks when:** VC fits when growth really converts capital into durable value at scale (the slot machine) and the outcome can be
large enough to return a fund. It breaks when the company is a good business with a natural $250M exit, or when a crowded market lets "anyone with
a pulse" raise a fund.

**Channel example:** "27. Venture Capital 101" (Camilo Acosta). "He Sold His Business for $300mm. Why Mark Cuban Told Him Not to Take Venture
Capital."

**Counterpoint:**
- Both guests talk their book: an emerging AI pre-seed manager raising money ("former founders make the best VCs"), and a bootstrapped survivor
  ("vulture capital"). The second is survivorship: the companies that needed VC and died without it aren't on the show.
- Camilo dates and figures several facts loosely. Thiel's Facebook check was at about a $5M valuation, not $2.5M. Sequoia had already split off
  its China and India arms before the recording. VC fund commitments aren't "redeemed"; LPs stop re-upping or sell in secondaries.
- The angel guest's "up to 10%" of wealth in angel deals is aggressive by most planners' norms, and Kristen pushed back.

**Links:** [[harlem-capital-vc-insights]] (waterfall, DPI, J-curve), [[primary-venture-partners-insights]] (fund size → ownership → return the
fund), [[apply-wss-to-venture]] (the WSS layer applied to two seed firms), [[canon-ries-lean-startup]], [[canon-mauboussin-success-equation]]
(power laws and luck).

## 15. Sports franchises: league design, scarcity, and arena control

**What it is:** Major-league teams priced as **un-replicable franchises**. Each league is a cartel that fixes the number of teams, pools some
revenue and may cap costs. That design decides whether a team behaves like an annuity or an option.

**How it works:**
- **Revenue mix plus a cost cap is the whole model** (the hosts' Sports Investing 101). Split revenue into national (shared media, divided
  equally) and local (tickets, local TV, sponsorship, arena), then ask whether payroll is capped:

| League | National / local | Payroll | Consequence |
|---|---|---|---|
| NFL | ~80 / 20 | Hard cap (~$255M in 2024, ~$279M in 2025) | Small and big markets converge; a half-empty stadium "almost doesn't matter" |
| NBA | ~60 / 40 | Soft cap: luxury tax plus first and second "aprons" | Overspending is punished; playoff runs add revenue each round |
| MLB | ~20 / 80 | No cap | Market size rules: Soto's $765M/15-year Mets deal; "maybe six of 30" teams make real money |

- **The NFL TV arithmetic.** $110B over 11 years is $10B a year, or ~$312M per team. Kristen's "~$400M a year" per team is closer to *total*
  national revenue.
- **The NBA tax.** The 2024-25 aprons were ~$178M and ~$189M. The hosts illustrated a single "4.2x" penalty on dollars over the second apron.
  The real tax is bracketed from the tax line, steps up every $5M, and is steeper for repeat offenders. The aprons mainly bite as roster-building
  restrictions.
- **Comps:**
  - Lakers: **$10B** for a majority stake (2025).
  - Celtics: about $6.1B, structured as 51% now and the rest in 2028.
  - Washington Commanders: $6B (2023).
  - Denver Broncos: $4.7B (2022).
  - Mets: Steve Cohen paid $2.4B for 95% in 2020.
- **Who may own a team.** Historically an NFL team needed one billionaire paying cash (David Tepper, Panthers). In 2024 the NFL approved a list of
  PE funds for minority stakes: Arctos, Ares, Sixth Street, and a consortium including Blackstone and Carlyle. Per public reports, the cap is 10%
  per fund per team, with a minimum hold. Sixth Street then bought into the Patriots and Celtics, built Bay FC (NWSL) from rights to the field in
  14 months, and financed Real Madrid's stadium renovation against future stadium revenue rights. Leagues police conflicts too: Michael Rubin had
  to sell his Sixers stake when Fanatics entered sports betting, and Adelman bought it to become the third-largest partner in HBSE.
- **The trickle-down** (hosts). Family offices shut out of the big funds chase "micro-sports" (smaller leagues, women's teams, adjacencies). Eli
  Manning's Brand Velocity Group invests around teams (media, equipment, collectibles, gaming) rather than in them.
- **Arena control is a second asset** (Adelman).
  - The Sixers rent from the Flyers and Comcast, so they miss building revenue and don't control the fan experience.
  - The new ~$1.5B South Philadelphia arena (opening 2030, or 2031 in the earlier clip) is a 50/50 partnership. Retail, food and the district's
    apartments and hotel feed the team's value: team and arena are "hand and glove."
  - HBSE's Prudential Center in Newark runs 240+ events a year with one pro tenant.
  - When a tenant team's lease expires, either the landlord makes "a great offer to stay" or the team must raise $1.5B for its own building.
- **The Premier League contrast** (Crystal Palace). No salary cap. Rivals include sovereign wealth funds that can spend $300M on one player.
  **Relegation** drops the bottom three clubs a division, and revenue collapses. Adelman said "bottom two"; it is three. The realistic owner goal
  is "keep me in the middle of the pack."

**Business significance / value:**
- US closed leagues with pooled national media and caps turn teams into **contracted, monopoly-like media annuities**, structurally close to
  infrastructure (concept 12).
- Sellers capture the scarcity premium. The league protects it by limiting supply ("It's 30 teams. That's it," Adelman). Owners who control the
  arena capture building revenue; tenants don't.
- Open, relegation-based leagues add binary downside and an arms race against state money.

**Forces & impact:**
- Media-rights inflation. The NBA's new deal is ~$76B over 11 years; the hosts said 10.
- Leagues admitting institutional capital, which widens the buyer pool and lifts every owner's mark.
- Billionaires and sovereign funds set the marginal price.
- **Second-order:** each record sale re-marks every other team. Adelman doesn't think any NBA owner was upset by the Celtics price. Comps set by
  hometown-pride buyers become everyone's valuation, which is circular.

**With vs. without:** Without closed leagues, teams behave like Premier League clubs: high variance, owners as patrons, frequent losses. With them,
trophy pricing keeps setting records, and the risk shifts to whether media rights keep compounding.

**Applies when / Breaks when:** Works while national media rights keep growing and leagues keep supply fixed. It would break if streaming-era rights
stopped escalating, or in MLB-style leagues where local revenue and no cap let a few rich markets outspend the rest.

**Channel example:** "Sports Investing Basics & Interview with Eli Manning and David Adelman." "Co-Owner of Philly 76ers David Adelman on Sports
Investing, Real Estate and Early Stage Investing." "PE | Growth Equity Value Creation w Sixth Street's Paul Dodd" (Bay FC, Real Madrid). "Real
Estate PE 101" (intro segment). "Why Owning a Soccer Team in the Premier League is WILD" (short).

**Counterpoint:**
- Adelman's "scarcity justifies the price" is the view of an owner whose stake is re-marked by every record sale.
- Kristen's claim that the Giants and Chiefs are worth "roughly the same" overstates the NFL's parity. A high national share narrows the gap
  between markets; it doesn't erase it.
- The Packers are not "publicly traded": their shares can't be transferred and pay no dividends.
- MLB's national media income is roughly $1.5-2B *a year*, not the "$1B" the hosts said.
- The **Millennium** aside from the same Real Estate PE intro still stands as illustrative only: ~12x "operating cash flow" ($14B / $1.125B)
  versus 4-6x for hedge funds and 15-20x for PE managers. Its fee math slips: 20% × 20% × $75B is $3B, not "$2-2.25B."
- The Lakers deal structure is in [[wss-credit-distressed]].

**Links:** [[canon-helmer-7-powers]] (scarcity as cornered resource), [[wss-credit-distressed]] (Lakers financing), [[unit-09-capital-light-businesses]]
(the league office as asset-light franchisor).

---

## How the concepts connect

```
ZIRP 2019-21 ─► record LP commitments + high entry multiples + cheap layered debt (7) ─► "anyone with a pulse" raises a VC fund (14b)
     │                                   │
     ▼                                   ▼
NAV swells, marks optimistic (6)    sub lines flatter early IRR (3)
     │
rates ↑ ─► leverage is no longer an edge ─► returns must come from EBITDA: operating partners, AI in go-to-market (2b)
     │
     ├─► exits stall ─► distributions/NAV at GFC low (6) ─► LPs can't recommit ─► fundraising slows
     │        │
     │        └─► public drawdown (Apr 2025) + endowment tax ─► denominator effect ─► Yale sells ~$6B LP-led (6)
     │
     ├─► liquidity engineering: LP-led & GP-led secondaries (5) ─► CVs re-fee winners (tiered carry), sub lines + deferred payments,
     │   NAV loans, CFOs, div recaps (7)
     │
     └─► new LP needed ─► wealth channel (9) ─► advisor choice: wirehouse shelf vs RIA (9b) ─► evergreen wrappers (8)
                                               │                                           ─► best-fit assets = secondaries (5) & co-invest (4)
                     constant inflows ─► deployment pressure ─► entry prices ↑ ─► future returns ↓ (2)
                     quarterly marks ─► "volatility laundering" ─► gates if redemptions > 5%/qtr
                     401(k) executive order ─► the largest pool yet, sold in 5-minute advisor pitches (8, 9)

Same rate shock in real assets: cap rates ↑ ─► negative leverage ─► CRE refi gap (11) ─► pref/mezz rescue capital
                                 and households: 2% → 7% mortgage lock-in ─► home-equity investments (13)
Duration as the antidote: infrastructure and project finance (12), permanent-capital ETA (14), closed-league franchises (15)
Scarcity as the antidote: fixed league supply + pooled media + caps ─► record comps ─► PE whitelisted into the NFL (15)
```

The single idea underneath: **private markets trade liquidity and price transparency for control and an illiquidity premium.** Every product in
this note is a way to re-sell some liquidity (secondaries, evergreens, HEIs), borrow against illiquidity (sub lines, NAV loans), or exploit
someone else's need for it (gap capital, distressed debt).

## Retrieval questions

1. **A fund shows 35% IRR and 1.15x TVPI in year two. What two questions do you ask?**
   How much was funded on a subscription line before capital was called, and what DPI does it have? Early IRR is timing-sensitive and can be
   manufactured. The multiple and cash distributed are not.
2. **Why can distributions hit a record and still be at a GFC-low as a share of NAV?**
   The denominator (unrealized NAV) ballooned from 2018-21 inflows and optimistic marks. In 2008, by contrast, the numerator went to zero.
3. **An evergreen fund charges 1.25% and 12.5% over a 5% hurdle. A drawdown fund charges 1.5% and 20% over 8%. Why might the evergreen cost more?**
   Its carry crystallizes every year on unrealized gains, over a lower hurdle. Drawdown carry waits until capital and pref are returned, often in
   years 4-6.
4. **Why are secondaries the natural core of semi-liquid funds?**
   They're already invested (no blind-pool cash drag), diversified at once, and mature enough to distribute cash for redemptions.
5. **Shah wants her LMM GPs to earn carry. Why is that an alignment argument, not a generosity one?**
   Carry requires selling, which produces distributions. Fee income from ever-larger funds rewards asset gathering instead.
6. **An office building quotes a 6 cap. Why might an investor's true yield be closer to 4?**
   Recurring tenant buildouts and leasing commissions are capital spent below the NOI line every time leases roll.
7. **Why did infrastructure investing start in Australia, not the US?**
   Australian states privatized assets in the 1990s and Macquarie raised listed retail capital to bid. US public owners already had cheap,
   tax-exempt muni financing (6% taxable ≈ 4% muni).
8. **Same 15% annual return: why does Dorrell prize it over 20 years far more than over 5?**
   Compounding. 2.0x versus about 16.4x. Duration, not the rate, is infrastructure's edge.
9. **Using Findley's numbers, what does a homeowner who sells immediately pay for $50k of HEI cash?**
   $133k, about 2.7x. The 25% volatility haircut is a discount transferred to the investor up front and doubles as the investor's margin of
   safety.
10. **Why can't a classic search-fund deal use SBA debt?**
    SBA requires a personal guarantee from anyone holding more than 20% of the equity, which search-fund investors won't give.
11. **Why did First Brands put Apollo on its disqualified-lender list?**
    Apollo's Caesars-era reputation for aggressive restructuring tactics, and its ownership of competitor Tenneco, which would have given it data
    room access.
12. **What makes an infrastructure asset different from Walmart, in Dorrell's framing?**
    Mismanagement doesn't kill it, because nobody can build a competing airport or utility. That earns cheap financing and lower returns, and
    invites regulation.
13. **Blackstone shows a private-markets portfolio beating 60/40 by 1 point a year with 1.8 points less volatility (2016-24). Name three reasons
    an individual investor wouldn't capture that.**
    Fees (the indices are largely gross), appraisal smoothing (the volatility gap is partly measurement), and mismatched return types (pooled
    IRRs against time-weighted returns). Bonus: a short, low-rate window, and redemption gates that the backtest never had to face.
14. **A GP moves a 4x winner into a continuation vehicle at 400 and charges 75 bps instead of 2%. Why is the GP still better off than selling?**
    It crystallizes carry on the old fund at 400, rolls that carry into the CV to keep compounding, and earns new tiered carry (10/15/20 over
    rising IRR and MOIC hurdles). 75 bps on 400 is 3, more than 2% on the original 100.
15. **Why do 80-99% of LPs choosing to sell in a CV not prove the deal was fair to them?**
    A high sell rate mostly shows the price was full relative to NAV. The test of fairness is the third-party auction plus the GP rolling all its
    economics. And the sponsor's own advisor ran the process.
16. **Public equities drop 25% and private marks barely move. Walk through why a long-horizon endowment might sell PE stakes anyway.**
    Private becomes overweight against target (the denominator effect), distributions have stalled so no cash is coming in, and new commitments
    to core GPs still need funding. Selling on the secondary market at strong prices rebalances and recycles. Yale's ~$6B sale is the case.
17. **Why can Harvard absorb a $2B funding cut that would break a $230M endowment, beyond the obvious size difference?**
    Endowments spend from returns and much of the money is donor-restricted. A small endowment can't earn much without risking principal, so it
    runs conservatively and earns less. Size buys both buffer and return.
18. **A big bank quotes a lower advisory fee than an RIA. What's the first question?**
    Who else pays the bank? Shelf-space revenue sharing from product managers and lending economics can subsidize the quoted fee (Moffett).
19. **In Kristen's returns bridge, why is operating improvement worth more than its EBITDA effect alone?**
    Higher EBITDA raises exit EV at a constant multiple *and* produces cash that pays down debt, moving value from lenders to equity. It may also
    earn a higher multiple at exit. Leverage alone stopped being an edge once everyone could borrow cheaply.
20. **$2M on a "$10M" SAFE: what's the investor's ownership if $10M is pre-money, and if it's post-money?**
    16.7% ($2M of $12M) versus 20% ($2M of $10M).
21. **A founder takes $100M of VC and later gets a $250M offer. Why might the deal no longer work?**
    The fund needs a multiple on $100M of preferred, so a $250M exit barely returns the preference and fails the fund math. The company now has to
    chase $1B+, which changes hiring, burn and risk. That was Cuban's "slot machine" test.
22. **Why does an NFL team in Kansas City trade at a value closer to a New York team than an MLB team in a small market does to the Yankees?**
    About 80% of NFL revenue is pooled national media split equally, under a hard cap. MLB is about 80% local with no cap, so market size drives
    revenue and payroll.
23. **Why did the Sixers' new arena deal matter for team valuation?**
    As a tenant they missed building revenue and control of the fan experience. As a 50/50 owner they share retail, food and district income,
    and a buyer of the team gets both.

## Gaps (what is still missing after pass 2)

Every pass-1 gap title now has a transcript and has been folded in (Secondaries 101/201, Yale, endowment talk, PE 102, Sixth Street, Carlyle,
PWM 101/102, both sports episodes, Project Finance 101, PE Associate Tell-All, VC 101, the Mark Cuban episode, and the LBO shorts).

Catalog titles still without a usable transcript:
- Videos: **S2E2 "Giant Squid" | Block Trades, IPOs vs. Other Equity Offerings, Perception of PWM & More!** (beSAafxvKn0): the PWM-perception
  segment.
- Shorts: "Paper LBO…" (J9xh-sNosSM), "Private Equity Associates rely on this one simple Excel trick" (XmmJ6VXft7Q), "3 Secrets from senior women
  in PE and PWM" (BpYtJ1pw0M8), "Largest Debt Commitment in History for LBO by ONE BANK" (fZQP_mQ_2sg), "The Rule of 72" (h57N5mP-qn8), and the
  IBD-vs-PE / PE-vs-hedge-fund career shorts (AvYJQ1wyw9I, -Hf6aYdtdfE, YYZIMxyok9w, 6kiO6Tc1Qf8, Z5_KV5NsKso). The career shorts belong in
  [[wss-technicals-career]].
- Present but empty: "Step by Step: How to Break into PE" (BIPgf2Im740) and "Working Backwards" (VELp2jJxEu0) have no usable speech.

Topics the channel never teaches, even with the full transcript set (fill from other sources if needed):
- **Wealth advisor plumbing:** grid payout percentages, recruiting loans, the Broker Protocol, fiduciary duty versus Reg BI, custody rules, and
  PE roll-ups of RIAs.
- **Value creation evidence:** any split of PE returns between operations, leverage and multiples, and who pays operating-partner costs.
- **Sports structure:** NBA/MLB/NHL institutional-ownership rules, league debt limits, and minority-stake liquidity and discounts.
- **Secondaries pricing:** discounts on venture and tail-end portfolios (only strong pricing on good buyout funds is discussed), and NAV loans,
  which are named but never defined.

Cross-cluster: the Lakers financing and Caesars/First Brands distressed mechanics are in [[wss-credit-distressed]]. Project finance and data-center
SPVs are in [[wss-ai-economics]]. Paramount/WBD affordability is in [[wss-capital-markets-ma]].
