# Note · Cross-company executive pay — what nine boards pay their CEOs for predicts how each firm behaves, and the deal-makers are the ones paid on total, not organic, growth

> Governance / incentives note · Maps to **E4** (Corporate Governance — pay design, say-on-pay, controlled companies), **E2** (Capital Allocation — how incentives steer M&A and buybacks), **Course 09** (Leadership & Org Behavior — incentives), **Course 03** (Microeconomics — principal–agent) · Written 2026-10-25 · Part of the cross-company set: [[cross-company-financials]], [[cross-company-narrative-vs-numbers]], [[cross-company-say-vs-do]]

- **Source:** each firm's latest annual proxy:
  - **US filers (2026 DEF 14A):** Tradeweb, MarketAxess, ICE, S&P Global, BlackRock, Goldman, JPMorgan.
  - **Thomson Reuters:** 2026 Management Proxy Circular (6-K, 2026-04-15).
  - **LSEG:** Directors' Remuneration Report in its 2025 Annual Report.
  - Extracted to `_ingest/raw/audit/pay/<ticker>.json`, with verbatim quotes script-checked. Each company's people note now has a "How they're paid" section.
  - **Not covered:** Bloomberg (private).
- **Core claim:** **Pay design predicts behaviour better than strategy statements do.**
  - **Tradeweb pays on *total* revenue growth and on EBITDA excluding deal costs**, so acquisitions help both of its pay metrics. It then made its largest acquisition (Trumid).
  - **Thomson Reuters pays only on *organic* growth and neutralises unplanned buybacks**, so neither buying growth nor shrinking the share count lifts pay. It returned capital instead.
  - **JPMorgan pays on unadjusted reported ROTCE** and won 91% shareholder support.
  - **The four boards that lost a third of their shareholders** on say-on-pay (BlackRock 67%, Goldman ~66%, S&P 68.8%, LSEG 69.6%) all relied on discretion, special awards, severance or adjusted EPS.

---

## 1. The pay map

| Firm | CEO, FY2025 pay | Annual bonus metrics | Long-term metrics | Basis | Say-on-pay |
|---|---|---|---|---|---|
| **Tradeweb** | Hult, **$20.6M** (from $16.7M) | 50% constant-currency revenue growth, 50% adjusted EBITDA margin (paid at max) | ⅓ RSU; ⅓ revenue and EBITDA growth PRSUs; ⅓ **absolute** TSR | Non-GAAP; **total** (not organic) revenue | ~99% |
| **MarketAxess** | Concannon, **$7.1M** | 75% adjusted operating income, 25% individual | PSUs: ⅓ **US credit market share**, ⅓ revenue growth outside US credit, ⅓ operating margin | Operating KPIs; unplanned M&A excluded | 98% |
| **ICE** | Sprecher, **$22.1M** | 70% adjusted operating income, 30% net revenue | 30% relative TSR vs S&P 500, 40% year-3 EBITDA, 30% RSU | Non-GAAP; **mid-period M&A excluded** | 94% (79% in 2024) |
| **S&P Global** | Cheung, **$12.8M** | Adjusted revenue and EBITA margin plus scorecard (70%), individual (30%) | **70% three-year cumulative adjusted EPS**, 30% RSU | All "ICP adjusted"; pro forma for divestitures | **68.8%** |
| **LSEG** | Schwimmer, **£6.4M** (UK basis, at vesting) | 60% organic adjusted operating profit, plus ASV, strategy, personal | **60% adjusted EPS growth**, 40% relative TSR (sector and FTSE 100) | AEPS not organic, so deals and buybacks can lift it | **69.6%** |
| **Thomson Reuters** | Hasker, **US$11.7M** | ⅓ organic revenue, ⅓ organic recurring contract value, ⅓ adjusted EBITDA less capex | 50% organic revenue growth, 50% FCF per share | Non-IFRS, **organic by construction**; excess buybacks neutralised | ~99% |
| **BlackRock** | Fink, **$45.0M** board-framed ($37.7M SCT) | Scorecard: 50% financial, 25% business, 25% organisational, then "context-informed judgment" | BPIP: organic revenue growth × adjusted operating margin (target 44%), pays 0–165% | Non-GAAP; plus CEO **carried interest** | **67%** |
| **Goldman** | Solomon, **$47.0M** board-framed ($118.9M SCT incl. retention grant) | Holistic, no weights, a formula explicitly rejected | 3-year average **reported ROE**, absolute and vs peers (<5% pays 0, ≥16% pays 150%) | GAAP ROE | **~66%** |
| **JPMorgan** | Dimon, **$43.0M** board-framed ($40.6M SCT) | ~50% results, ~50% "how"; cuts for shortcomings "without limits" | 3-year average **unadjusted ROTCE** (≥18% max, <6% zero) and relative to 10 peers; CET1 hurdle | Reported | **91%** |

*Comparability: US totals value equity at grant. LSEG's UK "single figure" counts long-term awards at vesting (its 2023 award vested at 46%). "Board-framed" is how BlackRock, Goldman and JPMorgan describe the annual decision; the Summary Compensation Table follows SEC rules.*

## 2. Four patterns

**1. M&A treatment predicts M&A behaviour.**

| Pay treats acquisitions as… | Firms | What they did 2019–26 ([[cross-company-financials]] §4) |
|---|---|---|
| **Helpful.** Total revenue counts; deal costs stripped from EBITDA | **Tradeweb** | Nasdaq FI, Yieldbroker, r8fin, ICD, then **Trumid ~$1.97B** (all cash) |
| **Helpful via adjusted EPS.** Not organic; accretive deals and buybacks lift it | **LSEG**, **S&P** (S&P neutralises divestitures) | LSEG: Refinitiv, PTS, **Octus ~29× EBITDA**. S&P: IHS Markit, then a 121% payout of FCF |
| **Neutral.** Mid-period deals excluded from targets | **ICE**, **MarketAxess** | ICE still did Ellie Mae and Black Knight; deal management is rewarded through individual objectives instead |
| **Excluded by design.** Organic only; excess buybacks neutralised | **Thomson Reuters** | Returned 123% of FCF; small AI tuck-ins only |
| **Judgement or returns-based** | **Goldman**, **JPMorgan**, **BlackRock** | Banks: buybacks and reported returns. BlackRock: GIP, HPS, Preqin (BPIP's *organic* growth leg doesn't reward acquired revenue directly; the carry plan rewards private-markets fundraising) |

*Inference, not proof:* incentives don't cause deals by themselves. But the one venue paid on total growth is the one now making its biggest acquisition, and the one firm paid purely on organic growth is the one that returned the most cash.

**2. Adjusted metrics are nearly universal; the exceptions are the banks.**
- **Seven of nine** pay on non-GAAP measures (adjusted EBITDA, operating income or EPS).
- **Only Goldman and JPMorgan** pay long-term awards on *reported* ROE/ROTCE. JPMorgan explicitly uses "unadjusted" figures and can cancel up to half of unvested awards if three-year ROTCE falls below 15%.
- This ties back to the GAAP-vs-adjusted gaps in [[cross-company-financials]], such as ICE's mortgage margin (1% GAAP vs 41% adjusted). Where pay is adjusted, the adjusted story is the one management is paid to defend.

**3. When adjusted EPS pays and TSR doesn't, shareholders notice.**
- **LSEG's 2023–25 award:** adjusted EPS vested at 77%, while relative TSR paid **0%** (33rd percentile against peers). Say-on-pay was 69.6%.
- **S&P** puts 70% of long-term pay on one adjusted-EPS number and got 68.8%, after a predecessor's severance package.
- **BlackRock (67%) and Goldman (~66%)** drew dissent over discretion and special awards. Goldman's **$80M retention grants each to Solomon and Waldron** have no performance condition and cliff-vest in January 2030.

**4. MarketAxess: the incentives were set for a business that was being sold.**
- **The grant:** in **February 2026**, the same month J.P. Morgan began advising on a sale ([[marketaxess-ice-deal]]), MarketAxess granted PSUs measured one-third on **US credit market share**, the metric that had been falling since 2020.
- **The payout terms:** the merger converts unfinished awards at the **higher of target or actual performance**. The proxy shows no retention or transaction bonuses. Concannon's estimated change-of-control payout is **$14.6M** (cash $5.3M, equity $9.2M), and the merger itself counts as "good reason" for him to leave on those terms.
- **The read:** pay targeted the right problem, but the sale took the metric off the scoreboard before it could be measured.

## 3. Controlled companies

- **Tradeweb (LSEG controls 89.9% of the votes)** doesn't use Nasdaq's controlled-company exemptions for pay governance, according to its proxy. Its say-on-pay (~99%) is mostly a vote by the controller.
- **Thomson Reuters (Woodbridge, the Thomson family's holding company)** has Woodbridge-affiliated directors on its pay committee. Its ~99% approval reflects that.
- **The read:** where one holder controls the vote, say-on-pay tells you about the controller's satisfaction, not the minority's.

## 4. What this doesn't prove

1. **Pay is one input among many.** Strategy, opportunity and balance sheets matter more for any single deal. The M&A pattern in §2 is a correlation across nine firms.
2. **Headline totals aren't comparable** across the US, Canadian and UK disclosure regimes, or between "board-framed" and Summary Compensation Table figures.
3. **Proxies describe design, not outcomes.** Whether the metrics were set hard enough needs several years of target-vs-actual history. Only some proxies disclose it.

## 5. Canon lenses

- **Agency** ([[canon-jensen-meckling-agency-theory]]): pay is the board's main lever on the agent. Adjusted metrics move the agent's attention away from the cost of capital paid for acquisitions.
- **Incentives** ([[canon-munger-poor-charlies-almanack]]): "Show me the incentive and I'll show you the outcome." The Tradeweb and Thomson Reuters contrast is the cleanest example in the set.
- **Goodhart's law** ([[canon-kahneman-sibony-sunstein-noise]], [[canon-doerr-measure-what-matters]]): when adjusted EPS becomes the target, it stops measuring value (LSEG: EPS paid, TSR didn't).
- **Power** ([[canon-pfeffer-power]]): controlled companies and retention grants show who can set their own terms.

## 6. Open questions

1. Will Tradeweb's 2027 proxy count Trumid's revenue toward pay targets, or exclude it?
2. Will LSEG move long-term pay off adjusted EPS after two years of ~70% say-on-pay?
3. Do Goldman's retention grants hold the leadership pair through 2030, and what happens to the succession signal if either leaves?
4. Does ICE carry MarketAxess's US-credit-share metric into its own plans after closing, or drop it?

**Links:** [[cross-company-financials]] · [[cross-company-narrative-vs-numbers]] · [[cross-company-say-vs-do]] · [[cross-company-capability-matrix]] · [[tradeweb-people]] · [[marketaxess-people]] · [[marketaxess-ice-deal]] · [[ice-people]] · [[spglobal-people]] · [[lseg-people]] · [[thomsonreuters-people]] · [[blackrock-people]] · [[goldman-people]] · [[jpmc-people]] · [[canon-jensen-meckling-agency-theory]] · [[canon-munger-poor-charlies-almanack]] · [[canon-kahneman-sibony-sunstein-noise]] · [[canon-doerr-measure-what-matters]] · [[canon-pfeffer-power]]

---
### Rep
1. **Predict from pay.** Using only §1, predict how each firm responds to a $2B acquisition opportunity that is accretive to adjusted EPS but dilutive to return on capital. Then check against what each did 2019–26.
2. **Redesign one plan.** Rewrite LSEG's long-term plan so that a deal like Octus (~29× EBITDA) only pays out if it earns its cost of capital. Which metric would you use, and how would you treat acquired amortisation?
3. **The MarketAxess grant.** In one paragraph: was granting US-credit-share PSUs in February 2026, while sale talks were starting, a governance problem? Use the merger-proxy timeline in [[marketaxess-ice-deal]].
