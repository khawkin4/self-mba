# Unit 03 — What a Company Owns and Owes: the Balance Sheet

> **For a beginner.** Builds on Units 01–02. Same company, same event. New idea: the **balance sheet**,
> and the one number that absorbs the shock when things go wrong.

---

## Plain words first (read once)
- **Debt** — money the company **borrowed and must repay**, plus **interest** (the fee a lender charges
  for the loan), whatever happens.
- **Revenue / profit** — *revenue* = money in from customers; *profit* = what's left after all costs (Unit 01).
- **Creditors** — the people/banks the company **owes** (the lenders behind its debt).
- **Income statement / cash flow statement** — the first two scoreboards (Units 01–02): *did it make a
  profit?* and *did real cash come in?* This unit adds the third: *what does it own and owe?*
- **Snapshot** — a balance sheet is measured **at one date** (e.g. Dec 31), not over a year.
- **10-K / SEC / EDGAR** — a company's annual report, filed with the U.S. regulator (SEC) and free on its
  EDGAR website. · **$X B** = X billion dollars.

*(Assets, liabilities, and equity are the lesson itself — taught below.)*

## ① Material — what we're learning, and where it lives
The third scoreboard is the **balance sheet** — a *snapshot* (at one date) of everything a company
**owns** and **owes**. It's built on the one equation all of business accounting rests on:

> **Assets = Liabilities + Equity**

It's in every 10-K, free on EDGAR. (Income statement = "did it make money?"; cash flow = "did cash come
in?"; balance sheet = "what does it *have*, and who has a claim on it?")

---

## ② Understanding — the idea in plain language
- **Assets** — everything the company owns or controls (cash, ships, buildings, what customers owe it).
- **Liabilities** — everything it *owes* others (loans, bills, debt).
- **Equity** — what's left for the owners after the debts: **Equity = Assets − Liabilities.**

> A **house** worth **$400k** (asset) with a **$300k mortgage** (liability) → your **equity is $100k**.
> If the house value falls to $350k, your equity drops to $50k — *the equity takes the hit first.*

That's the key intuition: **equity is the shock absorber (the cushion).** Losses come out of equity.
Debt, by contrast, must be repaid no matter what. So when a shock hits, watch two things: liabilities
*rising* (borrowing to survive) and equity *shrinking* (losses eating the cushion). If equity gets thin,
the company is fragile — one more bad year and the debts could exceed what it owns.

---

## ③ Example — Royal Caribbean's balance sheet through COVID (real figures, USD)
*(Equity shown as Assets − Liabilities — exactly what "what's left for owners" means.)*

| Year | Assets | Liabilities (owes) | Equity (cushion) | What happened |
|---|---|---|---|---|
| **2019** | $30.3 B | $17.6 B | **$12.7 B** | Healthy: owners' cushion ≈ **42%** of assets. |
| **2020** | $32.5 B | $23.7 B | **$8.8 B** | COVID: revenue gone, so they **borrowed billions to survive** → liabilities jump ~$6B; losses eat the cushion. |
| **2022** | $33.8 B | $30.9 B | **$2.9 B** | Survived — but the cushion is nearly gone (**~8%** of assets). Debts almost as big as everything owned. |
| **2025** | $41.6 B | $31.4 B | **$10.2 B** | Recovered: profits rebuilt the cushion. |

Read the story the snapshot tells:
- **2019** — a sturdy balance sheet: for every $100 of stuff owned, only ~$58 was owed; ~$42 was the
  owners' cushion.
- **2020–2022 — the event in the balance sheet.** With sailings stopped, the only way to survive was to
  **borrow** — liabilities climbed from $17.6B to $30.9B. Meanwhile each year's loss came *out of equity*,
  shrinking the cushion from $12.7B to **$2.9B**. By 2022 the company owned $33.8B but owed $30.9B — it
  survived, but barely; the shock absorber was almost fully compressed.
- **2025 — recovery.** Profits flowed back into equity, rebuilding the cushion to $10.2B.

This is the **EDGAR × event** bridge again: the snapshot numbers (filing) only make sense once you know
*why* (COVID forced debt-fueled survival). A beginner can now *see* how a shock transmits through a
balance sheet: **liabilities up, equity down, fragility up.**

---

## ④ Application — your turn
**A. Verify the equation.** Take 2020: Assets $32.5B, Liabilities $23.7B. What's equity? *(≈ $8.8B —
and notice $23.7B + $8.8B = $32.5B. It always balances.)*

**B. Read the cushion.** Equity ÷ Assets went from ~42% (2019) to ~8% (2022). In one sentence, what does
that tell you about how risky the company was in 2022? *(Very — almost everything it owned was owed to
creditors; one more bad year could have pushed debts past assets.)*

**C. Reason it out (no computer needed).** A company has $200B of assets and $100B of liabilities. What
is its equity, and what % of its assets is that cushion? Is it sturdier or shakier than Royal Caribbean
in 2022 (~8%)? *(Equity = $100B; that's 50% of assets — far sturdier than RCL's 8%.)*

**D. Optional — pull it yourself (only if you have this project set up).** With the repo running:
`python3 _ingest/edgar.py facts AAPL` — then size its equity cushion against its assets. No setup? Skip it.

### Check yourself
1. Equity = Assets − ______ ? *(Liabilities.)*
2. When a company loses money, which part of the balance sheet shrinks first? *(Equity — the cushion.)*
3. Why is a thin equity cushion dangerous even if the company is still alive? *(Little margin for the
   next shock; debts could exceed assets, and creditors must still be paid.)*
4. True or false: a balance sheet shows what happened *over the whole year*. *(False — it's a
   **snapshot at one date** (e.g. Dec 31). The income statement covers the year; the balance sheet is
   the photo of what's owned and owed at that instant.)*
5. Of the three scoreboards — income statement, cash flow statement, balance sheet — which one tells you
   what a company **owns and owes**? *(The balance sheet.)*

### What's next
**Unit 04 — Is It Healthy?** Put all three statements together into a 3-minute health check anyone can
run — and watch the danger signal flash on Royal Caribbean in 2022.
