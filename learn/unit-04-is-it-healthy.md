# Unit 04 — Is It Healthy? A 3-minute health check

> **For a beginner — the capstone of the literacy arc.** You now know the three scoreboards (income,
> cash, balance sheet). This unit puts them together into a quick read of whether a company is *healthy*
> — and you'll watch the danger signal flash on Royal Caribbean in 2022.

---

## ① Material — what we're learning
No single number tells you if a business is healthy — you **triangulate** across the three statements.
Here's the beginner's 3-minute check, one number from each:

| From the… | Number | Question it answers |
|---|---|---|
| Income statement | **Net margin** = profit ÷ revenue | Does it keep money on each sale? |
| Cash flow statement | **Cash check** = is operating cash flow positive (and vs. profit)? | Is real cash coming in? |
| Balance sheet | **Leverage** = liabilities ÷ equity | How much does it owe vs. its cushion? |

---

## ② Understanding — what "good" and "bad" look like
- **Net margin** — higher and *stable* is better. Negative means it loses money on operations.
- **Cash check** — operating cash flow should be **positive**; if profit is positive but cash isn't
  (or vice-versa), find out why (Unit 02). Cash is survival.
- **Leverage (liabilities ÷ equity)** — how many dollars owed per dollar of cushion. **~1–2× is
  comfortable** for most businesses; **the higher it climbs, the more fragile** — a highly levered
  company has little room for a bad year before creditors are at the door. (Capital-heavy industries
  like cruise lines and airlines run higher naturally, but there's a level that screams danger.)

The skill: read all three *together*. One bad number can be a blip; **all three flashing at once is a
company fighting for survival.**

---

## ③ Example — run the check on Royal Caribbean (real figures)
| | 2019 (normal) | 2022 (post-shock) | 2025 (recovered) |
|---|---|---|---|
| **Net margin** | +17% | **−24%** | positive again |
| **Operating cash flow** | +$3.7 B | +$0.5 B | +$6.5 B |
| **Leverage** (Liab ÷ Equity) | **1.4×** | **10.7×** | 3.1× |
| **Read** | healthy | **alarm** | repaired |

What the check tells a beginner, instantly:
- **2019** — margin positive, cash strong, leverage a comfortable 1.4×. **Healthy.**
- **2022** — margin deeply negative (−24%), cash barely positive, and **leverage explodes to ~10.7×** —
  it owed nearly *eleven dollars for every dollar* of owners' cushion. That leverage number is the
  alarm bell: you can now *read*, in one ratio, that this company was fighting for its life — exactly
  what the COVID story (Units 01–03) told you in words. The numbers and the event agree.
- **2025** — margin positive, cash gushing ($6.5B), leverage back to a sane 3.1×. **Repaired.**

You just diagnosed a real company's rise, near-death, and recovery from three numbers — the same first
pass a professional analyst makes. That's financial literacy.

---

## ④ Application — your turn
**A. Compute the alarm.** 2022: Liabilities $30.9B, Equity $2.9B. What's leverage? *(≈ 10.7× — the
danger signal.)*

**B. Make the call.** Given 2022's three numbers (−24% margin, barely-positive cash, 10.7× leverage),
write one sentence a beginner could hand a friend: *is this company healthy, and why?* *(No — it's
losing money and dangerously indebted; it's surviving, not thriving.)*

**C. Stretch — your first real diagnosis.** Pick a company you know and run the full 3-minute check:
```
python3 _ingest/edgar.py facts <TICKER>     # e.g. SBUX, NKE, F
```
Pull revenue/profit (margin), operating cash flow, and liabilities÷equity. Write a two-line verdict.
*This is the literacy you came for — you can now open any public company and form a first opinion.*

### Check yourself
1. Which three numbers make the beginner's health check, and which statement does each come from?
2. A company has +20% margins and strong cash but **8× leverage**. Healthy or risky — and why the
   nuance? *(Profitable and cash-generative, but fragile to a downturn because of heavy debt — watch it.)*

### You've finished the literacy arc
You can now read the scoreboard (01), tell cash from profit (02), read what a company owns and owes
(03), and judge basic health (04) — on **real companies**, grounded in **real filings**, made vivid by
**real events**.

### What's next — climbing the ladder
- **Unit 05 — Growth & Returns:** why growth isn't always good (does the company earn more than its
  money costs?).
- **Unit 06 — What's a Business Worth?** the intuition behind valuation (a company = its future cash).
- **Unit 07 — The Landscape:** why some businesses are just *better* (intro to moats / competitive
  advantage) — your bridge to `notes/canon` and `lessons/`.
- **Then → `acumen/`:** you're ready to start making real calls and getting red-teamed (the case method).
