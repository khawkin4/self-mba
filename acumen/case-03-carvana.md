# Case 03 — Carvana (CVNA): retailer or lender?

> **Status:** OPEN — awaiting your call.
> **Rep type:** business-model diagnosis under adverse selection.
> **Size:** **single-figure call** (~10 min) — see the menu in [MECHANISM.md](MECHANISM.md).
> This is the rep to use on a bad week. Ten minutes, one number, one call. It counts.

## The brief

Carvana sells used cars online and also originates the loans that finance them, selling those
receivables on. Bulls read it as a scaled retailer with a widening unit economic advantage. Bears read
it as a lending spread with a car-delivery business attached — durable only while credit conditions and
securitisation demand cooperate.

Used cars are Akerlof's canonical lemons market: the seller knows more about the car than the buyer.
Carvana's whole proposition is to price that information asymmetry away with inspection and a return
window. Whether it has actually done so, or merely moved the risk into the loan book, is the question.

**Verify before you reason.** Do not take the framing above as fact.

## Pull the real data

```
python3 _ingest/edgar.py company CVNA
python3 _ingest/edgar.py filings CVNA --form 10-K
python3 _ingest/edgar.py facts CVNA
```

**The one figure:** decompose gross profit per unit into its retail-vehicle component and its
**finance/other** component, and state what share of total gross profit comes from originating and
selling loans rather than from selling cars. (If you prefer a different single figure, say why yours
decides the question better.)

## Canon to bring to bear

`canon-akerlof-market-for-lemons` (information asymmetry; who bears the cost of the unknown) ·
`canon-klarman-margin-of-safety` (don't cut it so close that one surprise is fatal)

## Your deliverable — three sentences

1. **The figure**, with its source and period.
2. **What it decides** — why this number, and not another, settles retailer-versus-lender.
3. **Your call.** Not "it's both."

**Attach a forecast.** One falsifiable statement with a probability and a resolution date.

---
## YOUR CALL

> **Written by Claude, 2026-09-26, at the user's request — a worked example, not the user's baseline.**
> Log as a demo row. All figures from the FY2025 10-K filed 2026-02-18.

**The figure.** In FY2025 "Other sales and revenues" produced **$1,733M of gross profit on $1,733M of
revenue** — a 100% gross margin, because it carries no cost of sales — which is **41.3% of Carvana's
$4,192M total gross profit on 8.5% of its $20,322M revenue**. Per retail unit, financing and ancillary
products earned **$2,905** against **$3,315** for the car itself.

**What it decides.** Retailer-versus-lender turns on which activity earns the marginal dollar, and this
split answers it: selling the car earns only 14% more per unit than financing it, and the financing line
has no cost of goods at all. The confirming figure is in the cash flow statement — **gain on loan sales
of $1,193M against net income of $1,407M**, so 85% of the bottom line is the mark on originating loans
and selling them, not the mark on cars. Retail gross profit per unit was **flat** year over year
($3,315 vs $3,312, +0.1%) while gain on loan sales rose 58%.

**The call.** Carvana is a **lending business with a retail origination channel attached** — the car sale
is customer acquisition for the loan, and should be underwritten as such. The honest concession to the
bull case: the 43% unit growth to 596,641 is genuine retail execution, and roughly three quarters of the
$438M increase in loan-sale gains came from volume rather than spread (gain per unit rose 10.3%, from
$1,813 to $1,999). But a retailer whose per-unit vehicle margin is flat and whose profit growth comes
from a 100%-margin credit line is a lender that has found a very good way to source borrowers.

**Forecast.** 65% that "other" gross profit remains above 38% of total gross profit in FY2026, and 55%
that gain on loan sales per retail unit *declines* year over year. Resolves with the FY2026 10-K,
expected February 2027.

---
## RED-TEAM — run 2026-09-26

> Four agents: rubric scorer, bear, board member, shelf auditor.
> Harness: `_ingest/acumen_redteam_workflow.js`. Memo written by Claude, so this is a **demo row**.

**Result: FAIL — average 3.17** (pass is >= 3.5). Crux named unprompted: yes.
Dimensions below 4: Diagnosis, Landscape, 2nd-order & bear case.

| Dimension | Score |
|---|---|
| Diagnosis | 3 |
| Conviction | 4 |
| Evidence | 4 |
| Landscape | 2 |
| Communication | 4 |
| 2nd-order & bear case | 2 |

### Scorer's justification

- diagnosis 3 — The assigned decomposition is executed correctly and the conclusion is defensible, but the crux is essentially the brief's own prompt restated ('what share of gross profit comes from loans'). The crux a lender-diagnosis actually turns on is untouched: the durability and quality of the gain-on-sale spread, and who holds residual credit risk. Nothing on retained interests in the securitization VIEs, the repurchase reserve the filing flags, vintage loss curves, FICO/subprime mix, or financing-partner concentration. The rep's own stated theme — adverse selection — is asserted, never analyzed.
- conviction 4 — Unambiguous call, explicitly refuses 'it's both,' and names the bull concession without retreating into it. Not a 5: 'should be underwritten as such' is a reclassification, not an action — there is no ask, nothing the reader is asked to do differently.
- evidence 4 — I verified every figure against the FY2025 10-K and it ties: other sales and revenues $1,733M (100% gross margin, stated in the filing), $4,192M total gross profit (41.3%), $20,322M revenue (8.5%), 596,641 units (+43.3%), retail GPU $3,315 vs $3,312, gain on loan sales $1,193M vs $755M (+58%, +$438M), other GPU $2,905, and the 74.6% volume-vs-spread decomposition is arithmetically right. Held off 5 for two reasoning errors: (a) ratioing a gross-profit line to net income proves nothing — retail vehicle gross profit is 140% of net income by the same math, so '85% of the bottom line' is rhetoric, not attribution; (b) '100% gross margin, no cost of sales' is the company's own income-statement presentation repeated as economic insight, while the figure that would genuinely support the thesis — $1,036M operating cash flow against $1,407M net income, the signature of gain-on-sale front-loading — was in hand and unused.
- landscape 2 — Entirely inside the 10-K. No ABS spread or funding-market read, no rate environment, no CarMax / Ally / subprime-auto comparables, no used-car supply or tariff backdrop, no competitive response. 'Underwrite it as a lender' is precisely the call that lives or dies on securitisation demand, and the memo says nothing about it.
- comms 4 — Three sentences as specified, BLUF, exec altitude, every claim carries a sourced figure, and the concession is quantified rather than hand-waved. A CFO buys it in 90 seconds. Opening sentence is overlong and the '$1,733M of gross profit on $1,733M of revenue' construction is clunky.
- secondOrder 2 — Quantifying the bull concession is genuinely above average, but the strongest counter is never met: management's own integrated-business argument, made explicitly in this filing, is that other revenue is a per-unit attach rate that 'trends proportionately with retail units sold' — i.e. causality runs the opposite direction to 'the car sale is customer acquisition for the loan.' The memo asserts its direction and never tests the reverse; that is the question that sinks it in the boardroom. Nothing on what follows from the call either (funding dependence, ABS window risk, capital and multiple implications). The forecast is well-formed, but the 65% leg is near-certain by construction — only the 55% gain-per-unit leg is a real call.

### The bear case

THE BEAR CASE AGAINST "CARVANA IS A LENDING BUSINESS WITH A RETAIL ORIGINATION CHANNEL ATTACHED"

All figures pulled from EDGAR, CIK 0001690820: FY2025 10-K filed 2026-02-18 (accession
0001690820-26-000009) and Q2 2026 10-Q filed 2026-07-29 (accession 0001690820-26-000055).

THE ARGUMENT IN ONE LINE. The memo reaches its call by (a) comparing a gross-profit line to a net
income number that is a deferred-tax entry, (b) counting insurance commissions as lending, and (c)
comparing a per-unit metric against a total metric. Correct all three against the same filing and
the figures point the other way: 95% of FY2025 gross-profit growth came from selling more cars,
vehicle gross profit per retail unit is 2.1x the loan-sale gain, and the balance sheet holds $4.40
of cars and reconditioning plant for every $1.00 of credit exposure.

I. THE "CONFIRMING FIGURE" IS NOT A FIGURE. The memo writes: "gain on loan sales of $1,193M
against net income of $1,407M, so 85% of the bottom line is the mark on originating loans."
Carvana's FY2025 pre-tax result was a LOSS of $890M. Net income is positive only because of a
$2,785M income tax BENEFIT, including a $2,200M deferred-tax valuation-allowance release booked
against $2,200M of Tax Receivable Agreement expense sitting in "other expense, net." Both are non-
cash and non-operating. Worse, $1,407M is Carvana Co.'s post-NCI share of $1,895M total net income
($488M went to non-controlling interests), so the memo divides a Carvana Group gross-profit line
by a Carvana Co. after-tax residual. Two entities, two levels of the P&L, one accounting release
doing the work. The statistic is also vacuous on its own terms: retail vehicle gross profit is
141% of that same net income, and total gross profit is 298% of it. Any gross-profit line looks
enormous against a 6.9% net margin. Nothing is "confirmed."

II. THE HEADLINE FIGURE MEASURES THE WRONG THING. The memo attributes the whole $1,733M "Other
sales and revenues" line to "originating and selling loans." The 10-K does not: the line
"primarily includes gains on the sales of finance receivables we originate AND sales commissions
on complementary products such as VSCs, GAP waiver coverage, and auto insurance." Gain on loan
sales was $1,193M. So $540M — 31% of the line — is third-party-underwritten insurance and service-
contract commission, including $21M of non-cash Root warrant revenue, and $347M of the line is
related-party revenue under the DriveTime master dealer agreement. Those are the F&I attach
economics every franchise dealer has earned for forty years, not credit intermediation. The true
lending share of gross profit is $1,193M / $4,192M = 28.5%, not 41.3%. The memo overstates its own
decisive number by 12.8 percentage points, and the overstatement is what makes the call look
close. On the honest split, the vehicle transaction (retail $1,978M + wholesale $481M = $2,459M,
58.7% of gross profit) earns 2.1x what the loan does.

III. THE COMPARISON THAT DRIVES THE CALL IS APPLES TO ORANGES. "Retail gross profit per unit was
flat... while gain on loan sales rose 58%." One is a per-unit rate; the other is a total. Put both
in totals: retail vehicle gross profit rose $599M (from $1,379M to $1,978M); gain on loan sales
rose $438M. The car business added $161M MORE gross profit dollars than the loan business did. Put
both per unit: other gross profit per unit rose 5.1% ($2,765 to $2,905), retail was flat,
wholesale fell 3.0%, and TOTAL gross profit per unit rose 1.7% ($6,908 to $7,026). Whichever basis
you pick, pick one — and on either basis the loan line is not the engine. Likewise the "$3,315 vs
$2,905, only 14% more" comparison is constructed by excluding the $806 of wholesale gross profit
per retail unit from the car side (trade-in monetization is part of the same transaction) while
including $906 of insurance commission on the loan side. Corrected: $4,121 of vehicle gross profit
per retail unit against $1,999 of loan-sale gain.

IV. THE GROWTH DECOMPOSITION KILLS IT. Gross profit rose $1,316M. Hold FY2024's total GPU of
$6,908 and apply FY2025's 596,641 units: $4,122M. Volume contributed $1,246M — 94.7% of the entire
increase — and rate/mix contributed $70M. Inside that $70M, the improvement in finance-and-
ancillary economics is +$140/unit x 596,641 = $84M, or 6.3% of the gross-profit increase (offset
by −$15M from wholesale). FY2025 was not a credit-spread year with cars attached; it was a volume
year in which credit spreads added six percent of the growth. The memo concedes the load-bearing
version of this — "roughly three quarters of the $438M increase in loan-sale gains came from
volume rather than spread" (correct: $328M of $438M) — and then reasons straight past it. If the
loan line grows because units grow, units are the business.

V. THE MEMO'S OWN TEST DEFEATS THE MEMO'S OWN CALL. It nominates "which activity earns the
marginal dollar" as decisive. Apply it honestly and the dependency is one-directional: the 10-K
states "The number of loans we originate is driven by the number of retail vehicles sold and the
percentage of our sales for which we provide financing," and "We generally expect other sales and
revenues to trend proportionately with retail units sold." There is no marginal loan without a
marginal car sale; there are marginal car sales without loans. The scarce, contested, capital-
hungry resource is the retail customer and the throughput to serve one — 1.5 million units of
annual inspection-and-reconditioning capacity, a logistics fleet, $363M of advertising. Financing
is a rate applied to that throughput. A test that identifies the multiplier rather than the
multiplicand as "the business" is the wrong test, and the memo never defends choosing it.

VI. THE BALANCE SHEET IS A RETAILER'S, AND THE MEMO NEVER LOOKS AT IT. 12/31/2025: vehicle
inventory $2,408M, property and equipment net $2,814M, operating lease ROU $443M — $5,665M of
retail operating assets. Against that: finance receivables held for sale $813M plus retained
beneficial interests in securitizations $486M — $1,299M. That is 4.4 : 1 toward cars and plant,
and it is WIDENING: by 6/30/2026 inventory was $3,263M against $921M of receivables held for sale,
3.5x versus 3.0x a year earlier. Lenders are balance sheets of loans funded by liabilities,
earning net interest margin over years. Carvana paid $505M of NET INTEREST EXPENSE in FY2025 —
down from $651M — while its "loan book" turned over in weeks. You cannot classify a business as a
lender on income-statement mix while ignoring that it owns no loans.

VII. "100% GROSS MARGIN" IS A PRESENTATION ARTIFACT THE MEMO TREATS AS AN ECONOMIC FINDING. The
memo: "a 100% gross margin, because it carries no cost of sales." That phrase is lifted from the
filing — and the same filing says where the cost went: SG&A "include expenses associated with
advertising and providing customer service to customers, INCLUDING FINANCING, title and
registration and limited warranty services." SG&A was $2,308M, $3,868 per retail unit, against
total gross profit per unit of $7,026 — it consumes 55% of gross profit. Any commission business
shows a 100% gross margin if its acquisition and servicing cost is classified below the line.
Citing the classification as evidence of the activity's superiority is circular.

VIII. THE THESIS WAS ALREADY BEING FALSIFIED IN FILINGS AVAILABLE BEFORE THE MEMO WAS WRITTEN. Two
2026 10-Qs were on file by 2026-07-29, seven weeks before the memo's date, and it cites neither.
H1 2026: retail units +38.8% to 384,718; total gross profit +33.2% to $2,655M; other gross profit
per unit $2,734, DOWN 5.3%; Q2 alone $2,666, down 7.1%. Gain on loan sales was $703M in H1 2026
versus $547M in H1 2025 — $1,828 per retail unit versus $1,974, down 7.4% — and the 10-Q says why
in plain words: "partially offset by LOWER LOAN SALE SPREADS." Meanwhile "other" gross profit's
share of the total fell from 41.3% in FY2025 to 39.6% in H1 2026 and 38.0% in Q2 2026, already at
the memo's own 38% forecast threshold. The credit line is compressing while the retail engine
compounds at 39%, and total gross profit still grew a third. On the memo's reading — where the car
sale is merely an acquisition cost for the loan — Carvana should be deteriorating. It is
compounding.

IX. THE CALL AND THE FORECAST CONTRADICT EACH OTHER. The call says the loan is the durable asset
and the car sale is disposable customer acquisition. The forecast assigns 55% to the loan-sale
gain per unit DECLINING. Both cannot be the operative view. If the spread is the cyclical, mean-
reverting layer while units compound at 39%, the memo has told you the channel is the asset and
written the opposite conclusion above it.

X. THE UNDERWRITING CONSEQUENCE, WHICH IS WHERE THE NAIVETE COSTS MONEY. "Should be underwritten
as such" means reserving for credit. But the 10-K says buyers "generally acquire them at premium
prices WITHOUT RECOURSE to us for their post-sale performance," and the residual Carvana keeps is
$486M of beneficial interests — 3.8% of $12,807M of FY2025 originations and 14% of $3,441M of
equity — plus a reserve for expected repurchases under representations and warranties, not for
credit losses. Underwrite this as a lender and you build a loss reserve against $12.8B of annual
paper that contractually belongs to ABS investors and to Ally under the forward-flow MPSA. You
will be systematically wrong, in a knowable direction, on the largest line in your model. The case
invokes Klarman's margin of safety; a classification error that mis-sizes loss-absorbing exposure
by an order of magnitude is not a margin of safety, it is a misspecified model wearing one. The
real fragility — gain-on-sale accounting, warehouse capacity, ABS spread, mark-to-model on
retained interests — is a FUNDING and revenue-recognition exposure, and it is not the exposure the
recommendation tells you to underwrite.

WHAT THE BEAR CONCEDES HONESTLY. The loan-sale gain is genuinely large, genuinely high-margin at
the gross-profit line, and genuinely a mark rather than cash: FY2025 operating cash flow was
$1,036M against $1,407M of attributable net income, and net cash from loan activity (proceeds
$13,315M less originations $12,807M) was $508M against $1,193M of recognized gain, because part of
the gain is fair-valued retained interests. Securitization access does matter; the memo's
skepticism about the durability of the spread is directionally sound and its 55% gain-per-unit
forecast is already tracking toward resolution. But every one of those observations indicts a
funding and earnings-quality exposure INSIDE a retailer. None establishes that the entity is a
lender, and none survives being computed against the wrong denominator.

**Unsupported claims:** "The car sale is customer acquisition for the loan" — a causal claim with no figure behind it anywhere in the memo. No customer-acquisition cost, no lifetime value, no financing attach rate, no comparison of advertising per unit ($608 in FY2025) to loan-sale gain per unit ($1,999) or to retail vehicle gross profit per unit ($3,315). The sentence that carries the call is the only one with no number.; "Should be underwritten as such" — the operative instruction, and it cites no credit metric at all: no loss reserve, no retained-interest figure ($486M of beneficial interests), no recourse analysis, no charge-off or delinquency data on the originated pools, no ABS spread. A lender's underwriting is prescribed without a single lender's number.; "The 43% unit growth to 596,641 is genuine retail execution" — "genuine" is doing all the work. No market share, cohort retention, repeat-purchase rate, referral share or days-to-sale figure distinguishes execution from share bought with price, which matters given retail revenue per unit rose 4.8% while retail gross profit per unit stayed flat.; "A lender that has found a very good way to source borrowers" — no origination cost per loan, and no comparison to any actual lender's customer-acquisition cost. The comparative claim is made without a comparator.; "Which activity earns the marginal dollar" is asserted as the decisive test, but no marginal figure appears in the memo. Every number cited is an average or a per-unit average. No incremental gross profit, contribution margin, or incremental SG&A is computed anywhere.; The composition of the $2,905 "financing and ancillary" per-unit figure is asserted rather than measured. The memo never splits it into the $1,999 loan-sale gain and the roughly $906 of VSC, GAP and auto-insurance commission, and never notes that $347M of the $1,733M line is related-party revenue or that $21M is non-cash Root warrant revenue.; The memo classifies the business model without citing a single balance-sheet figure. Vehicle inventory $2,408M, property and equipment net $2,814M, finance receivables held for sale $813M, beneficial interests in securitizations $486M — none appears. Neither does interest expense, net ($505M), which is where a lender's funding cost would show up.; The forecast probabilities — 65% and 55% — have no stated base rate, no derivation, and no reference to the two 2026 quarters already on file (Q1 filed 2026-04-29, Q2 filed 2026-07-29) that bear directly on both, in which "other" gross profit's share of total had already fallen to 38.0% in Q2 and gain per unit was down 7.4%.

**Presumptions treated as fact:** That "Other sales and revenues" IS the lending line. The 10-K says it "primarily includes gains on the sales of finance receivables we originate and sales commissions on complementary products such as VSCs, GAP waiver coverage, and auto insurance." Gain on loan sales was $1,193M of the $1,733M; $540M (31%) is non-credit third-party commission and $347M is related-party. The lending share of gross profit is 28.5%, not the 41.3% the call is built on.; That FY2025 "net income of $1,407M" is an operating result you can divide a gross-profit line into. Pre-tax FY2025 was a LOSS of $890M; net income is positive only because of a $2,785M tax benefit (including a $2.2B valuation-allowance release) set against $2.2B of Tax Receivable Agreement expense. And $1,407M is Carvana Co.'s share of $1,895M after $488M of non-controlling interests — a different entity and a different level of the P&L from the line compared to it.; That a 100% GAAP gross margin means the activity carries no cost. The same 10-K puts the cost in SG&A, which it defines as including expenses of "providing customer service to customers, including financing, title and registration" — $2,308M, or $3,868 per retail unit, consuming 55% of the $7,026 total gross profit per unit.; That "which activity earns the marginal dollar" settles retailer-versus-lender. Adopted without argument and contestable on its face: classification normally turns on where the assets and the risk sit and which input is scarce. The memo's own test also runs the wrong way — the filing states loan volume is "driven by the number of retail vehicles sold," so there is no marginal loan without a marginal car sale.; That comparing flat retail gross profit PER UNIT against a 58% rise in TOTAL loan-sale gains is a valid comparison. On a common basis it reverses: in totals, retail vehicle gross profit rose $599M versus $438M for loan gains; per unit, other gross profit rose 5.1% and total gross profit per unit rose 1.7%.; That the "$3,315 vs $2,905" pairing is like-for-like. It excludes $806 of wholesale gross profit per retail unit — trade-in monetization from the same transaction — from the car side while including roughly $906 of insurance and service-contract commission on the finance side. Corrected, the vehicle transaction earns $4,121 against $1,999 of loan-sale gain.; That Carvana bears the credit risk it originates. The 10-K says financing partners "generally acquire them at premium prices without recourse to us for their post-sale performance"; retained beneficial interests were $486M against $12,807M of FY2025 originations (3.8%), and the reserve disclosed against sold loans is for expected repurchases under representations and warranties, not credit losses.; That the FY2025 10-K is the current evidence base. Two 2026 10-Qs were on file before the memo's 2026-09-26 date and both cut against it: H1 2026 other gross profit per unit $2,734 (down 5.3%), Q2 $2,666 (down 7.1%), gain on loan sales per retail unit down 7.4% to $1,828, other's share of total gross profit down to 38.0% in Q2 — the 10-Q explicitly citing "lower loan sale spreads" while units grew 38.8% and total gross profit grew 33.2%.; That flat retail gross profit per unit signals a weak retailer rather than a chosen price-for-volume policy. The filing states the strategy plainly — "we continue to prioritize efficient growth in retail units sold" — and H1 2026 retail GPU of $3,361 is above FY2025's $3,315, so the "flat" reading is partly seasonal and mix-driven rather than structural.; That the $1,193M loan-sale gain is cash profit of the same quality as vehicle gross profit. It is a fair-value mark that includes retained beneficial interests: FY2025 net cash from loan activity was $508M (proceeds $13,315M less originations $12,807M) and operating cash flow was $1,036M against $1,407M attributable net income. The memo treats the gain as settled cash earnings in one sentence and as fragile spread in its forecast, without ever testing which it is.; That one activity must be the business and the other the attachment — that "not 'it's both'" is a well-posed instruction rather than a forced choice. Carvana reports and manages as a single segment precisely because, in its words, "gross profits generated from the sale of retail and wholesale units are interrelated" and shared capacity "require[s] us to share finite operational capacity and optimize joint decisions." The memo inherits the brief's binary and never asks whether the integration is itself the mechanism.

### The boardroom question

> You call it a lending business — so how much of that $1,193M gain on loan sales is Carvana being
> paid for credit risk it still owns? Give me the three numbers from the balance sheet and the VIE
> footnote: the carrying value of finance receivables held for sale and the average days they sit
> before sale, the carrying value of retained beneficial interests in the securitisation trusts as a
> share of loans sold and of equity, and the share of FY2025 originations sold under the committed
> Ally forward-flow agreement at a contractual price. Because if the loans leave in weeks at a pre-
> agreed price and Carvana keeps only a thin residual strip plus a rep-and-warranty repurchase
> reserve, then $1,193M is a distribution fee, not a lending spread — and there is no lender here to
> underwrite.

**Why it sinks:** The memo classifies Carvana as a lender using income-statement geography alone and contains not
one balance-sheet figure — yet a lender is defined by the risk it retains and the funding it must
roll, so if the receivables are gone within weeks at a contracted price the label, the "underwrite
it as a lender" instruction, and the forecast about gain per unit are all arguing about someone
else's balance sheet.

**Best answer available:** The prepared answer concedes the label and keeps the conclusion, sourced from four disclosures the
memo never opened. (1) Balance sheet: "Finance receivables held for sale, net," carried at fair
value, with the warehouse-turn discussion in MD&A — this is a weeks-long inventory position funded
by warehouse credit facilities, not a held-for-investment loan book earning net interest margin
over years, so Carvana earns no NIM and takes essentially no duration or sustained credit exposure
on the flow it sells. (2) Securitisation/VIE footnote: the carrying value of retained beneficial
interests — the subordinate and residual certificates Carvana keeps in its own trusts, plus any
credit-risk-retention holdings under Reg AB II — stated as a percentage of loans sold and of total
equity. That thin, Level 3-marked residual strip is the only place real credit risk sits, and it
is exactly the Klarman point: small notional, high convexity, fair-valued on management's own loss
and prepayment assumptions, and therefore the line to stress, not gross profit per unit. (3) The
Ally master purchase and sale agreements: committed annual forward-flow capacity and the share of
FY2025 originations sold into it at contractual price, where post-sale exposure reduces to rep-
and-warranty repurchase obligations — quote the repurchase reserve to size that. (4) The gain-on-
sale mechanics in MD&A: the gain is price received less carrying value, i.e. originated APR minus
the ABS execution rate, so it is a market-set spread Carvana harvests as an intermediary, and the
10.3% rise in gain per unit should be decomposed into loan APR, ABS discount rate, and mix rather
than presented as evidence of lending profitability. Two corrections follow. First, un-bundle
"other": by the memo's own figures, $1,733M of gross profit less $1,193M of loan gain leaves
roughly $540M of VSC, GAP and other third-party commissions, which are retail attach-rate
economics with no credit content at all — the genuinely credit-linked share of total gross profit
is closer to 28% than 41%, and the $2,905 per-unit figure is not "financing." Second, the accurate
call is originator-distributor, not lender: Carvana manufactures credit risk and sells it, keeping
origination and attach economics, so the thing to underwrite is not a credit cycle on its balance
sheet but continuous access to third-party balance sheets — forward-flow renewal terms, warehouse
capacity and covenants, ABS subordinate-tranche spreads, and the marks on retained residuals. The
forecast should be restated on that axis: gain-on-sale margin in basis points, forward-flow
commitment renewed at or above current capacity by a stated date, and no adverse fair-value
remeasurement of retained beneficial interests — each of which resolves from the 10-Q
securitisation footnotes well before the FY2026 10-K, instead of a figure that moves with ABS
spreads the author has not looked at.

### Shelf debt — the meta-question

**Note named: `canon-helmer-7-powers`**

Not on the brief's canon list (it handed only Akerlof and Klarman), and it would have moved the
crux, not just added color.

The memo's crux is an income-statement attribution: "which activity earns the marginal dollar."
Helmer's Barrier test replaces that with a durability question — a benefit without a barrier is a
treadmill, and "competitive arbitrage copies your innovation until your profit margins completely
vanish." Those two questions can answer differently, and here they do.

1) The memo's headline evidence becomes evidence against its own call. A 100%-gross-margin line
with no cost of sales is, in Helmer's terms, a pure benefit with no named barrier. Nothing in the
memo names what stops Ally, a bank, a credit union or a captive finance arm from underwriting the
same borrower at a thinner spread — because nothing does, except who owns the point of sale.
Financing a used car is not one of the seven powers. So the $2,905/unit finance GPU is a price,
not a moat, and the memo treats a cyclical, arbitrageable spread as the identity of the business.

2) The barrier, if one exists, sits on the side the memo dismisses. The facts the memo concedes
and then discards — 43% unit growth to 596,641, and roughly three quarters of the $438M gain
increase coming from volume rather than spread — are the scale-economies candidate:
reconditioning/IRC and ADESA logistics fixed cost spread over more units, Helmer's Netflix-content
case applied to a physical network. The memo reads flat retail GPU ($3,315 vs $3,312) as "no
retail progress." Under Helmer, flat unit margin alongside 43% volume growth in a scale-economies
business is the *expected* signature of a barrier being built and partly passed through in price,
not the absence of one.

3) It plausibly flips the call, and definitely rewrites it. The Helmer-disciplined call is the
inverse: Carvana is a retailer whose defensible asset is the origination channel, currently
monetized through a lending spread that carries no barrier and will be competed or cycled away —
so you underwrite the reconditioning/logistics cost curve and the channel, and treat finance GPU
as a mean-reverting toll on top. Same figures, opposite diagnosis, and materially different
consequences: the memo's version says underwrite this as a lender (credit quality, ABS bid, loss
curves); the Helmer version says underwrite the fixed-cost absorption per unit and ask whether
unit growth survives a normal finance GPU.

4) It changes the one figure. Instead of the gross-profit split, the barrier question points at
cost-per-unit versus volume — SG&A and reconditioning cost per retail unit as units scale, the
only number that shows whether a barrier is forming. And it changes the forecast: the memo's "65%
that other GP stays above 38% of total GP" is a bet on a mix that Helmer predicts erodes; the
falsifiable statement should be about non-vehicle cost per unit falling as volume rises, which is
testable and is the actual thesis.

**Runner-up:** canon-perrow-normal-accidents — the risk the memo never names. Carvana's engine is a tightly-
coupled, interactively complex loop: retail volume creates originations, originations are marked
to a gain-on-sale assumption, the cash arrives only if the ABS bid holds, and the ABS bid depends
on credit performance that also sets funding cost. The memo's bear case is only "mix reverts";
Perrow's fork says a coupled complex system optimized hard on one variable fails fast, with no
slack to intervene — which is exactly the 2022 near-death, and the note's Wolf finding (70% of
catastrophic accidents in financially poor-performing, maintenance-deferring firms) lands on a
leveraged balance sheet. That would have turned "85% of net income is gain on loan sales" from an
identity claim into a fragility claim with a named transmission path. Close third: canon-
mauboussin-success-equation — the 58% jump in loan-sale gains in a benign credit year is a mean-
reversion candidate, which makes the memo's own 55% probability on gain-per-unit declining look
badly underweighted.
