# Case 02 — Boeing (BA): the rate-ramp crux

> **Status:** OPEN — awaiting your call.
> **Rep type:** operations + constraint diagnosis.
> **Size:** **crux-only** (~25 min) — see the menu in [MECHANISM.md](MECHANISM.md).
> No answer key. Take a position.

## The brief

Boeing's commercial recovery depends on getting narrowbody deliveries up, and every quarter of delay
compounds: customers hold slots, penalties accrue, and the cash conversion cycle stays stretched while
inventory sits as work-in-progress. The pressure is to raise the production rate. The counter-pressure
is that the quality escapes that caused the crisis were themselves produced by ramping a system whose
upstream suppliers and inspection processes could not hold the rate.

**Verify before you reason:** whether a regulator-imposed production-rate cap is currently in force,
what rate Boeing is actually achieving, and what management says the binding limit is. Do not take the
paragraph above as current fact.

**The decision:** Is Boeing's binding constraint **inside the factory** (labour, traveled work,
inspection throughput) or **upstream in the supply chain** (structures, engines, castings) — and
therefore, should the next increment of capital and management attention go to the line or to the
suppliers?

## Pull the real data

```
python3 _ingest/edgar.py company BA
python3 _ingest/edgar.py filings BA --form 10-K     # Item 1A + MD&A; read the segment discussion
python3 _ingest/edgar.py facts BA                   # inventory, advances, FCF, contract liabilities
python3 _ingest/edgar.py search "production rate"   # what Boeing and its suppliers each say
```

The tell is in inventory and advances: work-in-progress that will not convert looks different from a
system starved upstream. Check at least one supplier's filings too — a constraint you cannot see in
Boeing's numbers may be visible in theirs.

## Canon to bring to bear

`canon-goldratt-the-goal` (one constraint; optimising a non-constraint is an illusion of progress) ·
`canon-ohno-toyota-production-system` (stop the line; quality built in, not inspected in) ·
`canon-perrow-normal-accidents` (tight coupling + complexity makes failures systemic, not personal) ·
`canon-bungay-art-of-action` (the plan→outcome gap closes with intent, not more detail)

> Anything you reach for that is **not** on this list is exactly what the meta-question is hunting for.

## Your deliverable — crux-only

1. **The crux** in two sentences — the single pivotal, *solvable* challenge, stated so that fixing it
   would actually change the outcome. "Quality culture" is not solvable at this altitude; name
   something a board can fund.
2. **The one figure that proves it** — a real number from the filings, with its source.
3. **The bear case in one line** — the strongest reason your crux is the wrong one.

**Attach a forecast.** One falsifiable statement with a probability and a resolution date.

---
## YOUR CALL

> **Written by Claude, 2026-09-26, at the user's request — a worked example, not the user's baseline.**
> Log as a demo row. All figures from the FY2025 10-K filed 2026-01-30.

**The crux.** The brief's question is the wrong one: Boeing's binding constraint is neither the factory
nor the supply chain, because it has already demonstrated it can move units — **600 total deliveries in
2025 versus 348 in 2024 and 528 in 2023, with 447 737s against 396 in 2023** — while commercial aircraft
programs inventory *fell* $4,407M to $70,785M, which is a system converting work-in-progress, not one
starved upstream or clogged. The solvable, pivotal challenge is **cost per delivered unit**: BCA lost
**$7,079M on 600 deliveries, or $11.8M per aircraft, against $1,635M on 528 deliveries in 2023, or
$3.1M** — so at higher volume than the pre-crisis year, Boeing is losing **3.8x more per airplane.**

**The one figure that proves it.** BCA loss from operations per delivery: **$11.8M in 2025 vs $3.1M in
2023** (loss from operations $7,079M / 600 deliveries, and $1,635M / 528; 10-K segment table and
deliveries table). Raising the rate against this is Goldratt's error in its purest form — adding
throughput at a station that is not the constraint, where every incremental unit *enlarges* the loss.

**The bear case in one line.** Rate *is* the constraint and the loss per unit is simply fixed cost
spread over too few units — absorption improves mechanically as rate rises, and the 2025 number is
already $11.1M/unit better than 2024's $22.9M, so the cure for the loss is precisely the volume I am
telling the board to stop chasing.

**Why I still hold the crux.** The 2025 improvement came with $1,377M of net unfavourable cumulative
catch-up adjustments and higher 777X and 767 reach-forward losses — costs that grow with commitments,
not ones that dilute with volume. And the company's reported $2,235M of net earnings is not operational:
earnings from operations of $4,281M includes a **$9,566M gain** on the October 2025 sale of Digital
Aviation Solutions to Thoma Bravo for $10,550M. Strip it and Boeing's operations lost roughly $5.3
billion in its best delivery year since the crisis, against $5,454M of total shareholders' equity and
$8.5B of debt due within twelve months. The board is funding rate out of a divestiture.

**Forecast.** 70% that BCA reports another full-year loss from operations in FY2026, and 60% that BCA's
loss per delivery remains above $5M. Resolves with the FY2026 10-K, expected January 2027.

---
## RED-TEAM — run 2026-09-26

> Four agents: rubric scorer, bear, board member, shelf auditor.
> Harness: `_ingest/acumen_redteam_workflow.js`. Memo written by Claude, so this is a **demo row**.

**Result: FAIL — average 3.00** (pass is >= 3.5). Crux named unprompted: yes.
Dimensions below 4: Diagnosis, Evidence, Landscape, 2nd-order & bear case.

| Dimension | Score |
|---|---|
| Diagnosis | 3 |
| Conviction | 4 |
| Evidence | 2 |
| Landscape | 2 |
| Communication | 4 |
| 2nd-order & bear case | 3 |

### Scorer's justification

- DIAGNOSIS 3 — Real credit for refusing the brief's factory-vs-supplier binary and going at unit economics instead; that is diagnosis, not menu-picking. But 'cost per delivered unit' is an outcome metric off the segment table, not a mechanism a board can fund (the brief explicitly demanded the latter), and the memo ignored the brief's standing instruction to verify the rate cap: the 10-K (p.33) says the 737 rate recovered from below 38/mo to 42/mo, that the FAA and Boeing *jointly agreed* the KPI/rate-readiness process supported 42 in Oct 2025, and that 47 in 2026 requires 'the concurrence of the FAA.' A per-increment regulatory gate is in force and management names rate readiness as the binding limit; the memo dismisses rate using full-year delivery counts, which is the wrong denominator for a monthly-rate-gated question.
- CONVICTION 4 — Genuinely recommends and takes the risk: stop chasing rate, holds the crux explicitly against its own stated bear case, and attaches a dated probabilistic forecast. No matrix, no hedging, no 'it depends.' Held back from 5 because the case asked where the *next increment of capital* should go and the memo only says where it should not — it never names the alternative claim on the dollar, so the board leaves with a veto instead of an allocation.
- EVIDENCE 2 — Every raw figure checks out exactly against the FY2025 10-K filed 2026-01-30 (deliveries 600/348/528 and 447 vs 396; BCA loss $7,079M/$7,969M/$1,635M; inventory $70,785M from $75,192M, a $4,407M fall; $9,566M gain on $10,550M Thoma Bravo proceeds, closed 10/31/25; earnings from operations $4,281M, net $2,235M; equity $5,454M; $8.5B short-term debt) — that arithmetic discipline is rare. But the 'one figure that proves it' is an artifact: $5,283M of the $7,079M loss is 777X/767 reach-forward charges, non-recurring program development losses that do not belong in a per-unit denominator. Net them out and BCA is at $1,796M/600 = $2.99M per delivery versus $3.10M in 2023 — per-unit economics are FLAT, not 3.8x worse, and the headline claim collapses. Second error: the $1,377M catch-up cited to rebut the bear case actually *improved* ~$5.2B YoY (from $6,562M unfavourable in 2024) and the filing attributes it primarily to BDS fixed-price development programs (KC-46A, VC-25B, T-7A, MQ-25, Commercial Crew), not BCA — right number, wrong direction, wrong segment. Worse for the thesis: the filing says the 777X reach-forward was 'partially attributable to higher estimated supplier costs' and 'due to increases in supplier costs,' so the memo's own proof figure is filing-attributed to the upstream constraint it declared irrelevant.
- LANDSCAPE 2 — Near-total blindness to the rest of the same filing. The Spirit AeroSystems acquisition closed 12/8/25 for ~$4.7B in Boeing stock, ~15,000 employees, and in-sources 737/P-8/KC-46 fuselages plus 767/777/787 structures — Boeing already answered the case's exact question by buying its critical upstream supplier, and the memo does not mention it once. It also misses BCA backlog at $567,290M (up from $435,175M), which is demand confirmation that would have *strengthened* the cost-not-demand argument; and there is no Airbus, no engine/CFM supply, no FAA posture. The memo reads the segment table, not the landscape.
- COMMS 4 — Exec altitude and genuinely tight: reframes in the first sentence, figures bolded and sourced, bear case stated rather than buried, forecast attached, comfortably one page. A CFO buys it in 90 seconds — which is exactly the hazard, because what they would buy is the 3.8x. Not a 5: the divestiture-funded-operations point (strip the $9,566M gain and operations lost ~$5.3B against $5,454M of equity) is the strongest line in the memo and it is stranded in a subordinate 'why I still hold the crux' paragraph instead of leading.
- SECOND-ORDER 3 — Credit for self-attacking unprompted and for naming a real bear case (fixed-cost absorption). But it picked the second-strongest counter and missed the one that ends the meeting: decompose your own loss figure and the 3.8x is reach-forward contamination. It also misses Spirit's 2026 cost consequence, which both threatens the crux and would have made the forecast far better-reasoned. And the forecast is low-information — 70% on another FY2026 BCA operating loss is close to a gimme given 777X reach-forward dynamics, so it tests almost nothing; the $5M/unit leg is the only part carrying calibration risk, and it inherits the contaminated metric.

### The bear case

THE BEAR CASE: the crux is a divisor error, and the memo's own one-line bear case has already won
in filings that were on the wire before the memo was written.

**1. The numerator belongs to aircraft that do not exist.**
The crux is "cost per delivered unit," proven by BCA's $7,079M FY2025 loss divided by 600
deliveries. But $5,283M of that $7,079M is reach-forward losses on the 777X and 767 (10-K: "higher
combined reach-forward losses of $5,283 million on the 777X and 767 programs in 2025"), of which
$4,899M is 777X alone. The 777X delivered zero aircraft in 2025, has 560 undelivered units under
firm orders, an accounting quantity of 650, and a first delivery "expected in 2027." A reach-
forward loss is the one-time recognition of the *entire* projected program loss across an
accounting quantity that is almost all undelivered. Dividing it by 600 delivered 737s, 767s, 777s
and 787s does not measure the cost of building those aircraft. It measures nothing.

Strip it and the memo's own metric inverts: $1,796M / 600 = **$2.99M per delivery in 2025 against
$3.10M in 2023** ($1,635M / 528, and 2023 carried no 777X/767 reach-forward loss). Not 3.8x worse.
About 4% better, at 14% higher volume.

**2. The whole charge landed in one quarter, and the memo smeared it across four.**
BCA loss from operations by period: 1H25 −$1,094M on 280 deliveries ($3.91M/unit); Q3-25 −$5,353M
on 160 deliveries ($33.5M/unit — the 777X quarter, and the Q3 10-Q says so: "an incremental reach-
forward loss of $4,899 million during the third quarter of 2025"); Q4-25 −$632M on 160 deliveries
($3.95M/unit). Three of the four quarters of the "3.8x worse" year ran at roughly the 2023 rate.
The headline is one Tuesday in October.

**3. The memo's bear case is not a hypothetical. It is reported.**
Two FY2026 10-Qs were on file before 2026-09-26 (filed 2026-04-22 and 2026-07-28). 1H26: BCA loss
from operations **−$885M on 314 deliveries = $2.82M per unit**, margin (4.2)% against (5.8)% in
1H25. Q2-26 alone: **−$322M on 171 deliveries = $1.88M per unit**, margin (2.7)% — against 2023's
(4.8)%, the year the memo holds up as the healthy benchmark.

The ex-charge series reads $11.18M (FY24) → $2.99M (FY25) → $2.82M (1H26) → $1.88M (Q2-26). That
is an absorption curve. It is the memo's own bear line — "fixed cost spread over too few units" —
playing out in four consecutive data points, three of which were published and available.

**4. The evidence used to dismiss absorption is from the wrong segment.**
The memo rejects absorption because the 2025 improvement "came with $1,377M of net unfavourable
cumulative catch-up adjustments... costs that grow with commitments, not ones that dilute with
volume." The 10-K attributes that $1,377M "primarily due to losses recognized on the KC-46A
Tanker, VC-25B, T-7A Red Hawk, MQ-25, and Commercial Crew programs" — every one a BDS fixed-price
development program. A defense-segment charge is being used to argue that commercial narrowbody
unit costs do not dilute with volume. And it fell from $6,562M in 2024 to $1,377M in 2025, a 79%
reduction.

**5. The inventory proof is the same $4.9B charge, counted a second time, pointing the other
way.**
The memo says commercial aircraft programs inventory "*fell* $4,407M to $70,785M, which is a
system converting work-in-progress." But the 10-K states the 777X reach-forward loss "was recorded
as a reduction of deferred production costs, unamortized tooling and other non-recurring costs" —
booked directly into that inventory line. 777X unamortized tooling fell $4,122M → $1,816M while
777X work-in-process *rose* $3,476M → $4,313M. On the programs that actually deliver, deferred
production costs went **up**: 737 from $9,679M to $11,777M, 787 from $13,178M to $13,859M. The
$4.9B write-off is simultaneously the memo's proof that unit cost is broken and its proof that
conversion is healthy. It cannot be both, and on the delivering programs it is neither.

**6. "The board is funding rate out of a divestiture" is contradicted by where the money went.**
The memo cites "$8.5B of debt due within twelve months" against "$5,454M of total shareholders'
equity." The same 10-K page says Boeing held **$10.9B of cash and $18.5B of short-term
investments** plus $10.0B of undrawn revolvers — $29.4B against $8.5B, 3.5x coverage. Boeing then
paid it: 1H26 financing outflow $8,513M, total debt **$54.1B → $45.9B**, short-term debt down to
$4.6B, still holding $7.2B cash + $12.8B short-term investments + $10.0B undrawn. Investment grade
at all three agencies; **Fitch revised its BBB− outlook to positive in June 2026**. The DAS
proceeds went to deleveraging. Equity of $5,454M is also a poor solvency read for a firm carrying
$64,059M of customer advances as a liability — that is prepaid revenue, not distress.

**7. Cash answers the absorption question directly, and it answers for rate.**
Operating cash flow: −$12,080M (2024, 348 deliveries) → +$1,065M (2025, 600) → +$1,185M in 1H26
versus −$1,389M in 1H25. A $13.1B swing arriving alongside a 72% delivery increase. In 1H26,
inventories were a $3.5B unfavourable working-capital swing "reflect[ing] increased production,"
and Boeing still generated positive OCF because Advances and progress billings rose $59,404M →
$64,059M. Customers are prefunding the ramp faster than WIP accumulates. That is precisely the
stretched cash conversion cycle in the brief, closing — and it closes *because* of rate, not
despite it.

**8. Rate is not merely available. The regulator is granting it and Boeing is spending into it.**
Q2-26 10-Q: the 737 program "began to transition from a production rate of 42 to 47 per month with
the concurrence of the Federal Aviation Administration," is "planning for additional production
rate increases beyond 47 per month," and "began low-rate production on a new 737 production line
in July 2026." The 787 has "stabilized at eight per month." Capex was $2.0B in 1H26 against $1.1B
in 1H25, with 2026 expected higher still. BCA backlog: $435,175M (12/31/24) → $567,290M (12/31/25)
→ **$596,724M (6/30/26)**, up $29.4B in six months. Telling this board to defund rate means
slowing the conversion of a $597B backlog, in a duopoly, using a metric that has improved
monotonically every period rate has risen.

**9. The crux is not a crux, and the memo's own framework says so.**
Goldratt's instruction is to find the constraint and elevate it. "Cost per delivered unit" is not
a constraint; it is a quotient — an outcome with no station, no queue and no capacity. Meanwhile
the filings name a dated, fundable blocker the memo never reaches for: as of 6/30/26 Boeing had
"approximately 40 737-7 and 737-10 aircraft in inventory" that cannot be delivered until the FAA
certifies the engine anti-ice solution, with the −10 at 31% of undelivered 737 orders. Forty
finished airplanes that cannot convert is a constraint with a location. A crux that leaves it
outside the frame fails its own pivotality test.

**10. And the memo already decided the brief's question for management, after management had spent
$4.7B answering it.**
The memo declares the factory-versus-supply-chain question "the wrong one." Boeing closed the
acquisition of Spirit AeroSystems on 2025-12-08, exchanging approximately $4.7B of stock, with
$10,278M of provisional goodwill "provisionally assigned to our Commercial Airplanes (BCA)
segment." The next increment of capital already went upstream. The brief's dichotomy was live
enough to buy the supplier.

**11. The forecast is close to unfalsifiable on one leg and already losing on the other.**
"70% that BCA reports another full-year loss from operations in FY2026" — BCA is already at −$885M
through June with the 10-K warning that further reach-forward losses are possible. A full-year
profit would require +$885M in 2H26 from a segment that has not earned a full-year profit since
2018. Assigning 70% to that is not a prediction. The testable leg — "60% that BCA's loss per
delivery remains above $5M" — reads $2.82M at the halfway mark and $1.88M in the most recent
quarter. The memo gave 60% odds to the side of its own bear case that the published data already
contradicts by a factor of two and a half.

**The bear's summary.** Every figure in the memo is real. The inference is not. A single Q3-2025
charge against airplanes scheduled for 2027 was divided by 2025's delivered fleet, called a
production cost, and then used a second time — as an inventory decline — to argue the factory is
healthy. The absorption explanation was dismissed with a defense-segment number. And the two 10-Qs
that settle the question were already on file, saying $2.82M and $1.88M per unit while the rate
went from 42 to 47 a month with the regulator's blessing. Recommending that the board stop chasing
rate is not the contrarian read here. It is the one the data most recently available had already
falsified.

**Unsupported claims:** "Cost per delivered unit" is named as the pivotal solvable challenge, but the $11.8M quotient is never decomposed — no figure for labour hours per unit, traveled work, rework, supplier price inflation, or learning-curve position. The memo produces a ratio and calls it a cost driver without identifying a single component of it a board could fund.; "Every incremental unit *enlarges* the loss" — no marginal cost figure appears anywhere. Under program accounting, reported cost of sales per delivery is revenue times an estimated cost-of-sales percentage for the total remaining program, which is an average, not a marginal cost. The 1H26 margin improvement from (5.8)% to (4.2)% at higher volume is direct evidence against the claim, and it is unaddressed.; "Costs that grow with commitments, not ones that dilute with volume" — asserted about the $1,377M of catch-up adjustments and the 777X/767 losses with no fixed/variable decomposition and no figure showing which cost component scales with which variable.; "The board is funding rate out of a divestiture" — no figure traces the $10,550M of DAS proceeds to any rate-related use. No capex number, no tooling or new-line investment figure, no rate-readiness spend. The traceable 1H26 use was $8,513M of net financing outflow reducing total debt from $54.1B to $45.9B.; "A system converting work-in-progress, not one starved upstream or clogged" — no conversion metric is offered: no inventory turns, no days of WIP, no deferred production cost per unit, no supplier delivery performance figure. The single inventory delta cited ($4,407M) is not shown to be conversion rather than write-down, and the 10-K says the write-down was booked into that line.; "It has already demonstrated it can move units" is used to declare the factory-versus-supply-chain question moot, yet the memo never states an achieved monthly production rate for any program — 737, 787 or 767. The brief explicitly instructed: verify "what rate Boeing is actually achieving, and what management says the binding limit is." No rate figure appears in the call.; The $8.5B of 12-month debt maturities is presented as a stressor with no offsetting liquidity figure and no maturity schedule. The same 10-K page discloses $10.9B cash, $18.5B short-term investments and $10.0B undrawn revolvers.; "Roughly $5.3 billion" of operating loss is presented as the true operational result with no reconciliation to the $5,283M of 777X/767 reach-forward losses disclosed in the same filing — two figures that are the same number to within $2M.; "$5,454M of total shareholders' equity" is invoked as a measure of financial capacity with no adjustment for, or mention of, the $59,404M of Advances and progress billings sitting on the other side of the balance sheet as prepaid customer cash.; The forecast's second leg ("60% that BCA's loss per delivery remains above $5M") is stated with no reference to the 1H26 figure of $2.82M that was already published in the 2026-07-28 10-Q, and no figure establishing what 2H26 would have to do to reach $5M.

**Presumptions treated as fact:** That BCA's FY2025 loss from operations is a per-delivered-unit production cost. Contested by program accounting: $5,283M of the $7,079M is reach-forward loss on the 777X and 767, recognized against an accounting quantity of 650 units for a program with 560 undelivered firm orders, zero 2025 deliveries and first delivery expected 2027.; That FY2025 is the latest evidence available. Two FY2026 10-Qs were on file before the memo's date (filed 2026-04-22 and 2026-07-28). Both cut against the crux: 1H26 BCA −$885M on 314 deliveries ($2.82M/unit), Q2-26 −$322M on 171 ($1.88M/unit).; That the $1,377M of net unfavourable cumulative catch-up adjustments bears on BCA's unit economics. The 10-K attributes it "primarily due to losses recognized on the KC-46A Tanker, VC-25B, T-7A Red Hawk, MQ-25, and Commercial Crew programs" — all BDS fixed-price development. Segment attribution is not settled in the memo's favour; it is settled against it.; That the absorption explanation has been ruled out. The memo states it as its own bear line, then rejects it on non-BCA evidence without testing the loss-per-unit series ex-reach-forward-charge, which reads $11.18M (FY24) → $2.99M (FY25) → $2.82M (1H26) → $1.88M (Q2-26).; That the $4,407M decline in commercial aircraft programs inventory is evidence of work-in-progress conversion. The 10-K states the $4,899M 777X reach-forward loss "was recorded as a reduction of deferred production costs, unamortized tooling and other non-recurring costs." On the delivering programs, deferred production costs rose: 737 $9,679M → $11,777M, 787 $13,178M → $13,859M.; That a regulator-imposed rate ceiling is the operative constraint. As of 1H26 the 737 program "began to transition from a production rate of 42 to 47 per month with the concurrence of the Federal Aviation Administration," is planning increases beyond 47, and began low-rate production on a new line in July 2026. The condition the brief asked to verify had already moved.; That the balance sheet cannot support a ramp. At 6/30/26: total debt down $8.2B to $45.9B, short-term debt $4.6B, $7.2B cash plus $12.8B short-term investments plus $10.0B undrawn revolvers, investment grade at all three agencies, and Fitch's outlook revised to positive in June 2026.; That stripping the $9,566M DAS gain isolates "operations." Strip it and FY2025 operations show −$5,285M; strip the $5,283M of 777X/767 reach-forward losses as well and the figure is approximately −$2M. Which of those describes operations is the contested question, and the memo treats its own answer as given.; That a single year's BCA segment loss is a stable per-unit cost signal at all. Under program accounting, cost of sales per delivery is a function of the estimated cost percentage for the total remaining program and the accounting quantity — which Boeing raised by 400 units on the 737 and 100 on the 787 in 1H26 alone (737: 11,600 → 12,000 → 12,400 → 12,800). The headline metric is partly an artifact of estimate and quantity revisions, not a measured production cost.; That management has not already answered the brief's factory-versus-supply-chain question. Boeing closed the Spirit AeroSystems acquisition on 2025-12-08 for approximately $4.7B in stock, with $10,278M of provisional goodwill assigned to BCA. The next increment of capital went upstream before the memo declared the question the wrong one.; That demand and backlog are settled and therefore irrelevant to the crux. BCA backlog went $435,175M (12/31/24) → $567,290M (12/31/25) → $596,724M (6/30/26), and the 10-K warns of "reductions to backlog and/or significant order cancellations due to... delivery delays." Whether slowing conversion is costless to a $597B backlog in a duopoly is contested, not given.; That further 777X reach-forward losses are the expected case rather than an open question. The filings state only that the listed factors "could result in additional reach-forward losses in future periods," and the 767 charge fell to $40M in 1H26 from $191M in 1H25. The memo treats recurrence as settled in order to argue the losses grow with commitments.; That "cost per delivered unit" satisfies Goldratt's definition of a constraint. It is a quotient with no station, queue or capacity. The memo invokes Goldratt to argue against elevating throughput while naming as the constraint the one thing in the frame that cannot be a constraint — and leaves outside the frame a dated, located blocker: approximately 40 737-7 and 737-10 aircraft in inventory at 6/30/26 awaiting FAA certification of the engine anti-ice solution, with the −10 at 31% of undelivered 737 orders.

### The boardroom question

> You're telling us to stop funding rate because we lose $11.8M per airplane — so tell me how much
> of that $7,079M BCA loss is 777X and 767 reach-forward charges, which are losses recognised on
> airplanes we have not delivered and in the 777X's case will not deliver until 2027. Net those out
> and give me the operating margin on the 600 airplanes we actually shipped, because if the answer
> is roughly break-even your 3.8x-worse-per-airplane number is an accounting artifact, not a unit
> cost.

**Why it sinks:** The memo's single load-bearing figure divides a segment loss that is substantially composed of
forward-looking program charges on undelivered aircraft by current-year deliveries, and the
author's own paragraph proves he read the disclosure ($1,377M cumulative catch-up, "higher 777X
and 767 reach-forward losses") yet never quantified it or removed it from the numerator — so the
board can see he knows the denominator doesn't match the numerator and chose not to look.

**Best answer available:** The prepared answer decomposes the $7,079M before dividing: strip the 777X and 767 reach-forward
losses and the $1,377M net unfavourable cumulative catch-up out of the numerator, and separately
strip the abnormal production costs Boeing expenses rather than capitalises, to produce a clean
delivered-unit result — on the disclosed pieces the residual is roughly $2B on 600 deliveries,
near the $3.1M/unit of 2023, so the honest claim is not "3.8x worse per airplane" but "per-unit
economics have recovered to pre-crisis while the loss migrated into development commitments." That
reframes the crux correctly and more defensibly: the board's problem is not rate and not
delivered-unit cost but unpriced development exposure — 777X, whose charge scales with schedule
slip and order-book pricing struck years ago, not with volume — and the right funding question is
whether to keep buying schedule on 777X or cap it, while letting 737 rate rise because at
recovered unit margin each incremental narrowbody now absorbs fixed cost instead of enlarging the
loss. The author should then anchor it in the 737 program's own numbers — unit cost trend,
deferred production balance, abnormal costs expensed — rather than a segment aggregate, keep the
genuinely strong solvency point (operations lost money in the best delivery year since the crisis
only after removing the $9,566M Digital Aviation gain, against $5,454M of equity and $8.5B of
current debt), and restate the forecast on the decomposed metric: probability that BCA's ex-reach-
forward loss per delivery stays above $5M in FY2026, which is falsifiable and actually tests the
crux.

### Shelf debt — the meta-question

**Note named: `canon-taleb-black-swan`**

Not on the brief's canon list — this is shelf the author never reached for, and it would have
changed the call, not just added a caveat.

The memo does the hard work and then throws away its own best finding. It discovers, in the "Why I
still hold the crux" paragraph, that (a) reported net earnings of $2,235M is an artifact of a
$9,566M one-time gain on the Digital Aviation Solutions sale, (b) stripped of it, operations lost
roughly $5.3B, and (c) that sits against $5,454M of total shareholders' equity and $8.5B of debt
due within twelve months. Those three facts are filed as supporting colour for a cost-per-unit
thesis. Read against Taleb, they ARE the thesis: annual operating losses are within ~3% of total
book equity, and the near-term maturity wall exceeds equity outright. Boeing's outcome
distribution is not set by the average unit economics; it is set by one tail draw — another
quality escape, a grounding, a 777X certification slip triggering fresh reach-forward charges. The
note's operative rule is exactly the one the memo violates: don't anchor on the felt-likelihood of
the rare event, anchor on whether the exposure is survivable.

Three specific changes:

1. A different crux. The brief asked where the next increment of capital and management attention
should go — line or suppliers. The memo refuses both, names cost per delivered unit, and then
never answers the allocation question at all. Taleb's frame answers it: the next increment goes to
survivability. The pivotal, board-fundable, solvable challenge is removing the single-point
exposures that convert a bad year into insolvency — equity/liquidity capacity ahead of the $8.5B
wall, and de-risking or de-scoping the reach-forward programs (777X, 767) whose charges scale with
commitments. That is a crux a board can fund; "cost per delivered unit" is a diagnosis, not an
action.

2. A different reading of the divestiture. The memo's own line — "The board is funding rate out of
a divestiture" — is stated as an indictment and then dropped. Taleb makes it the mechanism:
selling a cash-generative, capital-light asset to fund a fat-tailed manufacturing ramp is trading
tail protection for throughput. That is the decision to attack, and it reframes the 2025 "best
delivery year since the crisis" as consumption of the buffer rather than recovery.

3. A materially better forecast. The memo forecasts 70% that BCA reports another full-year
operating loss — near-certain and therefore near-information-free, and it resolves on a metric no
board decision hinges on. The survivability frame yields a falsifiable statement with actual
stakes: a probability on an equity raise or dilutive capital event, a credit downgrade, or fresh
reach-forward charges above a stated threshold before the $8.5B matures. Same resolution date, far
more skin in the game.

It also closes a hole the memo leaves open: the bear case it wrote (fixed-cost absorption improves
with volume) is the only bear case it entertains. Taleb supplies the one that actually sinks the
memo — the crux is aimed at the mean in a business decided by the tail.

**Runner-up:** canon-mankiw-principles-of-economics — marginal thinking would have attacked the memo's central
metric rather than its conclusion. "$11.8M loss per aircraft" divides a total segment loss that
includes reach-forward losses on units not yet built and $1,377M of cumulative catch-up on units
already delivered by the current year's delivery count; that is not a per-unit cost, and the
marginal cash cost of the next 737 versus its contracted price may well be positive while the
average accounting loss stays ugly. The memo half-anticipates this in its own bear case and rebuts
it ("costs that grow with commitments, not ones that dilute with volume") — a fair answer on
reach-forward charges, which is why this ranks second rather than first, but it never separates
the average from the marginal explicitly, and if the marginal unit contributes, the crux collapses
and the brief's original rate question comes back. (Third: canon-sterman-business-dynamics — the
$4,407M inventory drawdown the memo reads as proof of healthy conversion is also what a de-
stocking echelon looks like two to four quarters before the bullwhip starves the line again.)
