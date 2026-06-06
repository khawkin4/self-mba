# Unit 02 — Cash vs. Profit: why a "profitable" company can still run out of money

> **For a beginner.** Builds on Unit 01. Same company (Royal Caribbean), same event (COVID), one new
> idea: **profit and cash are not the same thing** — and confusing them is how people get fooled.

---

## ① Material — what we're learning, and where it lives
Unit 01 used the **income statement** (revenue → profit). Now meet the second scoreboard: the
**cash flow statement**, which answers a different question — *did real money actually come in?* The
top of it we care about is **operating cash flow (OCF)**: the cash the core business threw off this
year. It sits in every 10-K, right after the income statement, free on EDGAR.

---

## ② Understanding — the idea in plain language
**Profit is an opinion; cash is a fact.** Profit follows accounting *rules* that include things where
no money moved this year. The big one is **depreciation**:

> Your lemonade stand buys a **$12,000 delivery van**. Accounting won't subtract all $12,000 from this
> year's profit — it spreads it as a ~$2,000/year "expense" over the van's life. So in *years 2–6* your
> profit shows a $2,000 cost, but **zero cash leaves** (you already paid for the van in year 1). Result:
> your **cash is higher than your profit** by that $2,000.

It runs the other way too: if a customer *promises* to pay (sale booked, cash not yet in your hand),
profit goes up but no cash arrived. So:

- **Profit can be higher than cash** (e.g., booking sales customers haven't paid yet).
- **Cash can be higher than profit** (e.g., depreciation — a paper cost, no cash out).

Why it matters, bluntly: **companies don't die from low profit; they die from running out of cash.**
You must watch both lines.

---

## ③ Example — Royal Caribbean's real numbers (the two come apart)
From RCL's actual filings (USD):

| Year | Profit (net income) | Operating cash flow | What it shows |
|---|---|---|---|
| **2019** | **+$1.9 B** | **+$3.7 B** | Cash was *nearly double* profit — because ships **depreciate** (a paper cost, no cash out). |
| **2020** | **−$5.8 B** | **−$3.7 B** | COVID: the loss was *real in cash too* — the business bled billions. |
| **2022** | **−$2.2 B** | **+$0.5 B** | **The punchline:** a net **loss**, but cash flow turned **positive**. Profit and cash had *opposite signs.* |

Read it:
- **2019** is pillar ②'s "cash > profit" lesson, live: $3.7B of cash vs. $1.9B of profit — the ~$1.8B
  gap is mostly depreciation on those giant ships (a real expense, no cash leaving).
- **2020** shows the other truth: when the event hit, the loss was *cash-real* — they actually drained
  billions, which is why they had to borrow to survive (that's Unit 03).
- **2022** is the one to remember: the income statement said "still losing money" (−$2.2B), but the cash
  flow said "the boats are sailing and cash is coming in again" (+$0.5B). **If you only watched profit,
  you'd have missed that the business had already turned the corner on cash.**

---

## ④ Application — your turn
**A. Compute.** In 2019, profit was $1.9B and operating cash flow was $3.7B. How big was the gap, and
what mostly explains it? *(≈ $1.8B; mostly depreciation — a non-cash expense.)*

**B. Explain.** In 2022 the company reported a loss but positive operating cash flow. In one sentence,
why is that possible? *(Profit includes non-cash charges and prior write-offs; the actual cash the
sailings generated was positive even though the accounting bottom line was still negative.)*

**C. Stretch — real tool.** Pick any company and compare its profit to its operating cash flow:
```
python3 _ingest/edgar.py facts COST     # Costco
```
Ask: is cash bigger or smaller than profit, and what would explain the gap?

### Check yourself
1. A company reports a $50M profit but *negative* operating cash flow. Name one way that happens.
   *(e.g., it booked sales customers haven't paid for yet — profit up, cash not in.)*
2. Which line tells you whether a company can *survive* next month — profit or cash? *(Cash.)*

### What's next
**Unit 03 — What a Company Owns and Owes (the Balance Sheet):** where the money to *survive* 2020 came
from, and the one number that acts as a company's shock absorber.
