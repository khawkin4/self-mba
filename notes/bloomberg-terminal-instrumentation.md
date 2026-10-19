# Bloomberg Terminal — instrumentation, latency, and what the free stack actually costs you

> **Sources:** NYU Law Library *Bloomberg Getting Started* function directory; University of Scranton
> (Kania School) *Bloomberg Training Booklet*, 67pp; `professional.bloomberg.com/support/documentation`
> (hardware/IT specs only — not training); **@ObjectiveTrade**, full channel, 20 transcripts
> (~288k words) — a former options/equity trader screen-recording a live seat, then, after losing
> access, screen-recording the substitutes. **Second pull (workflow-targeted):** Damodaran's own
> *In Practice* webcast on using a Terminal for valuation data; Bloomberg's official *Terminal
> Essentials: Fixed Income*; an `FA`-screen walkthrough; a live pair-trade build; two trading-floor
> documentaries. Synthesized, not reproduced. Raw corpus at `_ingest/raw/2026-09-26/`; searchable
> function index published separately as an artifact (link in §9).
>
> **Why this note exists:** the program has a *data* layer ([[sec-filing-intelligence]], `_ingest/edgar.py`)
> and a *judgment* layer (`acumen/`), but no note on **instrumentation** — the tooling between them, and
> what its absence costs. This matters because [[sec-filing-intelligence]] makes a claim this note
> partially refutes (§3), and because `acumen/MECHANISM.md` needs a way to ask whether a scored call
> depended on data the analyst could not have had. Maps to **Course 01** (Accounting), **Course 02**
> (Corporate Finance & Valuation), **Course 07** (Data & Decision-Making), **Course 11** (Global
> Strategy & Macro), and **E8** (Investor Relations).
>
> **Provenance:** §§1–2 and §5–8 are from the sources. §3 is this note's own argument and is
> *not* in any source — it is a direct disagreement with an existing repo note. §4 is the map, built by
> pairing the function index against `learn/` units and `CURRICULUM.md`; §5 carries its own
> evidence grades. Prices are as captured and
> will drift.

---

## 1 · Three witnesses, opposite ends of a $30,000 gap, same verdict

[[sec-filing-intelligence]] states the program's position on professional terminals in one line:

> *"Proprietary terminals (Bloomberg, FactSet) add analytical layers but the underlying filings are the
> same public data."*

That note reaches this from the outside, reasoning about the corpus. Two further witnesses reach it
from inside a seat. First, ObjectiveTrade, more bluntly:

> *"All the information is available to you elsewhere."* — and, on retail use: *"You don't need it. It
> is complete overkill."*

He is not a free-tools evangelist making a virtue of necessity. He had institutional access at an
options fund, made twenty videos demonstrating the platform, then lost the seat and spent the next
several videos testing what replaces it. His answer, after auditing Refinitiv/XENITH at $150/mo,
Godel at $60, Money.Net Scout at $12–60, OpenBB at zero, and stockanalysis.com at ~$5, was to settle
on the **$5/mo option** for long-horizon equity research — the same tier of tool this repo already
operates above with a free EDGAR CLI.

And then a third witness, who matters more than either — **Aswath Damodaran**, this program's named
source for Course 01 and Course 02, in his own *In Practice* webcast, recorded from a live Terminal:

> *"Almost all of the data here is public data, there's very little private information. You could
> pretty much get the same data elsewhere — it will be a lot more work."* … *"The data that's on
> Bloomberg is available elsewhere for the most part, and you should be able to get that data as
> well."*

**This is convergent validation of the program's core bet.** Three independent parties — one paying
~$30k/yr, one paying nothing, and the academic the curriculum already cites — agree that Layer 1 is a
commodity and that the analytical value sits above it. The EDGAR×event pedagogy in `learn/` is not a
budget approximation of a professional workflow. It is the same Layer 1, read directly instead of
through a vendor.

**Damodaran goes further, and his extra step is the sharpest thing in the whole corpus.** Bloomberg
now computes cost of capital and equity risk premium for you. He refuses to use them:

> *"I don't trust the numbers that Bloomberg comes up with — not because the people behind the numbers
> are not smart people with access to data, but because it's incredibly opaque. You have no idea what
> goes on behind the number… I use Bloomberg to get raw data. I think it's my job in corporate finance
> and valuation to estimate things like equity risk premiums and costs of capital."*

That is [[sec-filing-intelligence]]'s three-layer stack restated by a practitioner: **take Layer 1,
refuse someone else's Layer 3, build your own.** A $30k instrument's most convenient outputs are the
ones the most credible user in the field declines, on explainability grounds — the same grounds that
note calls the deepest structural property of filing-derived intelligence. The convenience is the
trap; the raw data is the product.

---

## 2 · What the $30,000 buys, precisely

A bare-bones seat runs **~$25,000–30,000/yr** (delayed quotes, limited broker research); volume
pricing lands near $26–27k; real-time exchange data and research are extra. Four things justify it,
and only one of them is data.

**1. Aggregation — the purchase is time, not information.** Every item the program pulls from EDGAR,
FRED, and agency sites is one command away instead of one workflow away. This is the honest core of
the value proposition and all three witnesses say so.

**2. Cross-asset grammar.** The yellow-key system (`F2` government, `F3` corporate, `F8` equity,
`F9` commodity, `F11` currency) means *one* syntax covers every asset class. `DES` describes a bond,
a stock, a future or a currency pair depending on which key preceded it. The free stack has no
equivalent: you learn EDGAR for equities, FRED for rates, TRACE for corporate bonds, and a broker
platform for options, each with its own model of the world. **This, not any individual dataset, is
the largest genuine capability gap** — and it is the reason Course 11 (Global Strategy & Macro) and
E9 are the hardest courses to instrument freely.

**3. Data EDGAR genuinely does not contain.** The table below is the honest inventory. "Free
substitute" is graded against what this repo can actually reach today.

| Terminal capability | Fn | Free substitute | Grade |
|---|---|---|---|
| Consensus estimates, per-analyst ratings & price targets | `ANR` `EEO` `EE` | Aggregated consensus on stockanalysis / Yahoo; **Scout (~$60/mo) gives named analysts with individual accuracy records** | Partial |
| Credit ratings with outlook, consolidated | `CRPR` `RATC` | Agency sites + issuer press releases, one at a time | Partial, laborious |
| Modelled default probability | `DRSK` | None. Altman-Z is computable by hand from `edgar.py facts` | Substitutable by work |
| CDS pricing, single-name & sovereign | `CDS` `SOVR` `WCDS` | **None** | No |
| Option volatility surface / term structure | `OVDV` `OMON` | Chains free on thinkorswim; no surface | Partial |
| Short interest & float % | `SI` `SIA` | FINRA biweekly, Finviz | Mostly yes, lagged |
| Block trades, dealer inventory, IOIs | `MBTR` `AQR` `IMGR` | **None** | No |
| Supply-chain graph (suppliers ↔ customers with revenue exposure) | `SPLC` | 10-K Item 1 major-customer disclosure + segment concentration, assembled manually per company | Partial, expensive |
| Bond terms & pricing across ~400k active issues | `SRCH` `YAS` | FINRA TRACE (prices, no analytics) | Partial |
| Real-time quotes, Level II, time & sales | `BQ` | thinkorswim, free with a funded account | **Yes** |
| Physical-flow alt data: tankers, pipelines, refineries, rigs, transmission lines, outages | `BMAP` `MAP` | Scattered, mostly paid | No |
| The messaging network | `IB` | **None at any price** | No |

Note the shape of it: the gaps are concentrated in **credit, derivatives, flow, and physical
commodities** — precisely the domains `learn/` does not cover and `CURRICULUM.md` treats lightly.
For equity fundamentals, which is where this program actually operates, the free stack is close to
complete.

**4. The network.** `IB` (Instant Bloomberg) is an unremarkable chat client containing nearly everyone
in institutional finance. Deals are transacted on it. Both sources identify this — not data quality —
as the reason nobody has displaced Bloomberg. (Compliance note: `IB` and `MSG` traffic is logged in
full and readable by your firm; several banks' group-chat scandals were sourced from it.)

> **Cross-link worth making explicit.** [[sec-filing-intelligence]] closes on the Moat Paradox: the
> raw material is a public good, so the moat migrates upward to *extraction*, then *judgment*, then
> **niche authority** — "when a specific community of decision-makers adopts your judgment framework
> as their standard lens, the framework becomes infrastructure rather than product." That note cites
> Cboe/VIX as the example. **Bloomberg is the same mechanism at full scale, and it landed one layer
> higher still:** not a framework the community adopted, but the *interface* the community adopted.
> The moat is neither the data nor the analytics — it is that the mnemonics, the keyboard, and the
> chat client became the profession's shared vocabulary. Godel's strategy is the tell: it deliberately
> copies Bloomberg's command grammar (`DES`, `FA`, `HDS`, `EQS`) because the switching cost it must
> beat is *muscle memory*, not features. Straight [[canon-helmer-7-powers]] switching costs layered
> on network economies.

---

## 3 · Where this note disagrees with the repo

[[sec-filing-intelligence]] lists "public access" as a compliance property producing this intelligence
capability:

> *"No information-asymmetry barrier — the raw material is free and identical for every analyst, from
> a solo operator to Goldman Sachs."*

**That is true about the corpus and false about the clock, and the distinction is load-bearing.**

Information symmetry is a claim about *content*. It says nothing about *latency*. Consider one fact —
a large institution repositioning out of a name:

| Observer | Sees it via | When |
|---|---|---|
| Bloomberg seat | `MBTR` / `AQR` block print | Seconds |
| Bloomberg seat | `SI` short-interest change | Biweekly |
| This repo | 13F via `FLNG` equivalent / EDGAR | **Up to 45 days after quarter-end** |

Same fact, same legal disclosure regime, same public corpus — a latency spread of roughly seven weeks.
For a compounder holding five years, seven weeks is noise and the symmetry claim holds completely. For
any decision with a clock on it — a credit event, a rate decision, an earnings reaction, a merger
spread — seven weeks is the entire trade, and the playing field is not level in any sense the word
normally carries.

**The corrected formulation: the SEC filing system equalizes access to the historical record and does
nothing to equalize access to the present.** This repo's chosen ground — long-horizon fundamental
analysis, `learn/` through `acumen/` — sits almost entirely in the historical record, which is *why*
the free stack works here and why it would not work on a trading desk. That is a deliberate strategic
position, and it is stronger for being stated rather than assumed. It also draws the boundary of the
program honestly: **this curriculum does not teach, and cannot instrument, anything where latency is
the edge.**

Recommended as an addendum to [[sec-filing-intelligence]]'s "Public access" row rather than a
contradiction of it — the property is real, its scope was overstated.

---

## 4 · The map — every unit's question, both ways

The point of this table is not to make the terminal aspirational. It is to show that **the program's
questions already are the professional questions**, and that the instrument differs while the inquiry
does not.

### `learn/` — the on-ramp

| Unit | The question | This repo | Terminal |
|---|---|---|---|
| [01 Scoreboard](../learn/unit-01-reading-the-scoreboard.md) | Revenue, profit, margin | `edgar.py facts TICKER` | `FA` |
| [02 Cash vs profit](../learn/unit-02-cash-vs-profit.md) | Is profit backed by cash? | Cash-flow facts, computed | `FA` → cash flow |
| [03 Owns & owes](../learn/unit-03-what-a-company-owns-and-owes.md) | Balance sheet, leverage | `edgar.py facts` | `FA`, `CAST`, `DDIS` |
| [04 Health check](../learn/unit-04-is-it-healthy.md) | Margin + cash + leverage | **Computed by hand** | `FA` + `RV` — *see §5* |
| [05 Growth & returns](../learn/unit-05-growth-and-returns.md) | Is the growth worth it? | Multi-year facts | `GF`, `WATC` |
| [06 What's it worth](../learn/unit-06-whats-a-business-worth.md) | DCF | Built in Sheets | `XLTP` DCF template, `WACC`, `EEO` |
| [07 Moats](../learn/unit-07-the-landscape-moats.md) | Durable margin vs peers | Manual peer set | `RV`, `EQRV`, `PPC`, `SPLC` |
| [08 Reading the words](../learn/unit-08-reading-the-words.md) | Risk factors & MD&A drift | `edgar.py search`, filing diff | `CF` (identical filings), `BI` for the analyst read |
| [09 Capital-light](../learn/unit-09-capital-light-businesses.md) | Capex intensity | Capex ÷ revenue from facts | `FA` segments, `RV` |
| [10 Personal finance](../learn/unit-10-personal-finance-operating-system.md) | Your own balance sheet | The whole unit | **Nothing.** The terminal has no view of you |

Unit 10 is worth pausing on. A $30,000 instrument built to price every security on earth has nothing
whatsoever to say about the reader's own 401k match, emergency fund, or savings rate — the decisions
with the largest certain effect on their actual net worth. Keep that next to [[tiger-sisters-wealth-mechanics]].

### Courses & executive modules

| Track | Functions that instrument it |
|---|---|
| **02** Corporate Finance & Valuation | `WACC` `BETA` `EEO` `XLTP` (DCF, 3-statement, sensitivity) |
| **04** Competitive Strategy | `SPLC` `PPC` `RV` `ICS` `MA` — `SPLC` is the standout; nothing free reproduces a supplier↔customer revenue graph |
| **07** Data & Decision-Making | `EQS` `BT` — and `BT` is a trap, see §5 |
| **11** Global Strategy & Macro | `COUN` `ECO` `ECFC` `ECSU` `ECTR` `WB` `BTMM` `BMAP` — **the widest free-stack gap in the curriculum** |
| **E2** Capital Allocation | `CACS` `DVD` `BDVD` `CAST` — dividend/buyback/issuance history in one place |
| **E3** M&A, Deals & Restructuring | `MA` `CAST` `DDIS` `CRPR` — the course `STRUCTURAL-ANALYSIS.md` flags as having *zero* canon notes |
| **E8** Investor Relations | `OWN` `HDS` `FLNG` `ANR` `SI` — who holds it, who's shorting it, what the street says |
| **E9** Geopolitics & Macro | `ECTR` (trade-flow map), `BMAP` (physical chokepoints), `WB` (sovereign curves) |

---

## 5 · Workflows, graded by evidence

**A correction first.** The three desk workflows originally published with this research — equity
analyst, credit, macro-morning — were *my ordering of functions*, not observed practice. The primary
practitioner source is explicit that he had no plan (*"I didn't have a written plan for how I was
going to do this, I just thought I was going to show you some of the functions I use"*), and Parts 2
and 3 are structured as addenda. He closes Part 3 by proposing exactly the missing artifact —

> *"What I might do is sort of take you through flow of what an equity analyst or an equity trader
> might do during a day at work."*

— and never made it. The channel goes on to `PORT`, Launchpad, backtesting, maps and `XLTP` instead.
**The single largest gap in the original corpus was the thing its own author identified and left
open.** A second, workflow-targeted pull closed most of it. Current grades:

| Workflow | Evidence | Source |
|---|---|---|
| Morning market open | Observed, stated as daily habit | ObjectiveTrade Pt 1 / Pt 3 |
| **Valuation data collection** | **Observed end-to-end** | Damodaran, *In Practice* |
| **Credit / fixed income** | **Observed end-to-end** | Bloomberg, *Terminal Essentials* |
| Company financials via `FA` | Observed end-to-end | `FA`-screen walkthrough |
| Backtest + counterfactual | Observed end-to-end | ObjectiveTrade |
| Launchpad build | Observed end-to-end | ObjectiveTrade |
| Custom chart build (`G`) | Observed step-by-step | Scranton booklet |
| Pair-trade construction | Observed, rough | *Pair Trade Workflow* |
| Equity analyst's full day | **Still synthesis** | — |

### 5a · Damodaran's data pull — the one that plugs straight into Course 02

1. `WEI` as the landing page.
2. Type the company name, disambiguate to the **local listing** (`MSFT US Equity`), land on the entry page.
3. `HDS` — largest holders. He flags the provenance himself: sourced from SEC filings, nothing proprietary.
4. `BETA` — **and the point is that it returns the regression, not just a number.** Defaults are parochial: a US stock against the S&P 500, a German one against the DAX, two years of weekly returns. Every amber field is editable — swap the index to MSCI World, weekly → monthly, two years → five, and it re-runs on the spot.
5. `FA` — the statements.
6. `SOVR` — sovereign CDS spreads, which is where his published country-default-spread methodology sources its input.
7. **Stop.** Do not take `WACC` or the computed ERP (§1).

Works on obscure names, which is the part students disbelieve: he demonstrates on Vinamilk
(`VNM Vietnamese Equity`) and gets holders and a beta regression.

### 5b · The credit workflow, corrected

What was published was constructed. The real sequence, from Bloomberg's own training material, routes
through market context first and execution last, and uses six functions the constructed version
lacked entirely:

1. `FICM` — fixed income credit monitor. The dashboard: spreads by instrument and sector, filter to investment grade / high yield / emerging markets, drill into a sector.
2. `WB` — world bonds. Yield and spread **deviation from the average**, to pinpoint anomalies worth investigating. The RMI column flags significant moves in related markets.
3. `BBTI` — commonly traded rates, sorted by category: outright, forwards, curves, butterflies.
4. `SRCH` — and it takes **natural language**. Typing *"US corporate retail amount outstanding greater than 500 million"* is parsed into search parameters.
5. Export → `FIW`, the fixed income worksheet. Subset by asset class, currency, maturity; chart it to surface outliers.
6. `COMB` — comparable bond analysis. Is this issue rich or cheap against similar issuance?
7. `YAS` — yield and spread. The spreads are clickable and adjustable, so yield calculations can be tested live.
8. `ALLQ` — every pricing source and contributing counterparty you are entitled to, aggregated into one relative-value screen.
9. `IMGR` — quotes already received, including over `IB`, consolidated.

`PCS` sets your pricing source once, globally, across all of the above.

### 5c · The detail that should change how this repo teaches

Inside `FA`, clicking any line item drills down — and the drill-down **links back to the original
10-K**, with management's own explanation adjacent. The worked example in the source: Disney's
interest expense falls three straight years; click through; the filing says the decrease was driven
by higher capitalised interest from the Shanghai Disney Resort development.

That is EDGAR × event, inside the Terminal, as a single click. **The program's core pedagogy is a
Bloomberg feature.** Which is the strongest possible argument that `learn/`'s four-pillar model is
aimed correctly — and a reminder that what the Terminal sells here is, again, only the click.

---

## 6 · Breaks when — the terminal is corrosive to this pedagogy if introduced early

The house template demands a failure-mode section. This one is sharp, because the failure is not
technical.

**`learn/README.md` rule 2: "Show every computation as a step, not a result."** The four-pillar model
works because the beginner computes the ugly number themselves — Unit 04 makes you divide $30.9B by
$2.9B and *feel* 10.7× before it tells you the company nearly died. `FA` renders that as a lookup.
The number arrives correct, pre-formatted, and meaningless. **Aggregation removes exactly the friction
that builds the understanding.** A student who learns the health check on a terminal has learned where
a screen is, not what leverage is.

The rule this implies, stated in the same register as the existing one:

> **Keep the core Application terminal-free.** Any Bloomberg function is a clearly-labeled *optional*
> extra, the same way `edgar.py` already is. Arc A must be completed by hand.

**`BT` is the sharper trap.** Backtesting is four clicks and produces a chart of a strategy that
worked. The channel's own worked example is the perfect artifact: a Bollinger mean-reversion rule on
3M, 2010–2021, returned **133%** — which reads as a success until you run `TRA` on the same ticker
over the same window and find that buying at the first entry and never trading again returned **134%**
on price alone and **215%** with dividends. The strategy underperformed doing nothing by 82 points,
and the interface presents it as a win, because the interface has no opinion about the counterfactual.

This is [[canon-mauboussin-success-equation]] (the luck/skill continuum, and the failure to specify a
base rate) and [[canon-kahneman-thinking-fast-and-slow]] (WYSIATI — the result on screen is the whole
world) rendered as a UI affordance. It also belongs with [[canon-taleb-black-swan]] on backfitting a
narrative to a sample. Fold into `quant-backtesting/` as the worked cautionary case; the discipline it
teaches is **always compute the do-nothing counterfactual before reading the strategy result**, which
generalizes far past trading.

**A third, quieter one.** Bloomberg Intelligence (`BI`, `BICO`) hands you a staff analyst's industry
read. It is good. It is also someone else's framing arriving before you have formed your own, which is
the mechanism `acumen/MECHANISM.md` is built to defeat — the "unprompted crux rate" input measures
precisely the ability to name the crux *before* it is handed to you. Read `BI` after your memo, never
before.

---

## 7 · What this gives `acumen/` — a constraint audit, not more corpus

`acumen/MECHANISM.md` is explicit that corpus size is **not** an input metric and names "24 modules,
82 books, 352 cross-links" as vanity measurement. A note contributing 210 function codes would be
exactly that. So the contribution here is a rubric input instead.

**Proposed red-team question, for the case template:**

> *Did this call depend on data the analyst could not have obtained — and if so, was the dependency
> acknowledged?*

Three outcomes, each scoring differently:

| Finding | Reading |
|---|---|
| Call rests only on filing-derivable data | Clean. The historical-record ground this program occupies |
| Call rests on terminal-only data (§2 table) and **says so**, with a stated assumption | Acceptable — the uncertainty is priced |
| Call rests on terminal-only data and **doesn't notice** | **Failure.** A confident memo resting on a number the analyst assumed was knowable |

The third is the valuable catch, and it is invisible without §2's inventory. It is also a specific,
countable version of the calibration-error input the mechanism already tracks: a call that silently
requires CDS spreads or block-trade flow is not an uncertain call, it is an *unfounded* one, and the
distinction should cost different points.

---

## 8 · Access — the cheapest real move

You do not have to decide between $30,000 and nothing.

**University Bloomberg labs.** Most business schools run them; accounts are free, licensed to the
hardware, and require only a mobile number for two-factor at signup. The session does not leave the
building without Bloomberg Anywhere, which is a further charge. On macOS the Terminal runs through
Citrix Workspace, not natively.

**`BESS` — Bloomberg Market Concepts / Essentials.** Free from any terminal: video modules on
equities, fixed income, FX and commodities, an exam per module, 75% earns an Acknowledgement of
Completion. It is the one credential in reach of this program that a recruiter recognizes on sight,
and the program's own rubric treats credential-free self-study as a weakness to manage. `BPS` holds
the cheat sheets, `SMNR` runs daily 20–30 minute webinars, `JOBS` lists roles posted only inside the
Terminal.

**The deliberate buy, if any.** Ranked by marginal value *to this program specifically*:

| Tool | Cost | Buys you | Verdict for this repo |
|---|---|---|---|
| stockanalysis.com Pro | ~$5–8/mo | 270+ screener filters, 10–40yr financials, spreadsheet export | **The rational purchase.** Compresses `edgar.py facts` workflows and adds screening the repo lacks |
| Godel Terminal | ~$60/mo | Bloomberg command grammar, linked panels, Excel export | Buy only to *learn the grammar* cheaply before a lab session |
| Money.Net Scout | ~$12–60/mo | Named analysts with individual accuracy records | The one genuinely distinctive item at this tier |
| MetaStock XENITH | ~$150/mo | Refinitiv, stripped; strong Reuters news | Poor fit — many functions return "not privileged" |
| OpenBB | free | Open-source CLI over third-party APIs | Already duplicated by `_ingest/edgar.py`, and less reliable |

---

## 9 · Links

**Repo:** [[sec-filing-intelligence]] (the Layer 1/2/3 stack this note instruments, and the note §3
disagrees with) · [[tiger-sisters-stock-picking]] and [[apply-stock-picking-nke]] (the analysis loop
these functions would accelerate) · [[market-structure-24-5-trading]] (latency and venue structure —
the §3 clock argument, from the market side) · `quant-backtesting/` (destination for the §6 3M case) ·
`acumen/MECHANISM.md` (§7 rubric input) · [Unit 04](../learn/unit-04-is-it-healthy.md) (§6's worked
example of why aggregation hurts) · [Unit 10](../learn/unit-10-personal-finance-operating-system.md)
(what the instrument cannot see)

**Canon:** [[canon-helmer-7-powers]] (Bloomberg's moat is switching costs + network economies, not
data) · [[canon-mauboussin-success-equation]] and [[canon-kahneman-thinking-fast-and-slow]] (the `BT`
trap) · [[canon-taleb-black-swan]] (backfitting) · [[canon-klarman-margin-of-safety]] (the
long-horizon stance that makes §3's latency gap survivable) · [[canon-shannon-information-theory]]
(symmetry of content vs. symmetry in time)

**Artifact:** the searchable 210-function index, command grammar, five-stage study path and desk
workflows — <https://claude.ai/artifact/Vxdc1owj4zsco7wg3K1mwa>
