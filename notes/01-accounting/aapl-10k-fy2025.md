# Note · AAPL 10-K FY2025 — reading the scoreboard

> Course 01 · Accounting · Output = "read & annotate one real 10-K"
> This is the **worked template**: every data note in the program looks like this.
> Numbers pulled live from SEC EDGAR via `_ingest/edgar.py` on 2026-06-05.

- **Source:** Apple Inc. Form 10-K, FY ending 2025-09-27 (filed 2025-10-31)
  https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm
- **Core claim:** A 10-K's three statements answer three different questions — *did it sell
  profitably* (income), *what does it own/owe* (balance sheet), *did real cash move* (cash flow).
  You can't read one without the other two.
- **Framework:** The accounting identity + the four ratios that survive contact with reality:

  | Figure (FY2025) | Value | Reading |
  |---|---|---|
  | Revenue | $416.16B | top line |
  | Gross profit | $195.20B | **gross margin 46.9%** — pricing power |
  | Net income | $112.01B | **net margin 26.9%** — exceptional |
  | Assets | $359.24B | what it controls |
  | Liabilities | $285.51B | what it owes |
  | Equity | $73.73B | **the wedge: assets − liabilities** |
  | Operating cash flow | $111.48B | cash earnings ≈ net income → **high earnings quality** |

  - Assets = Liabilities + Equity → 359.24 = 285.51 + 73.73 ✓ (it always balances)
  - **OCF ($111.5B) ≈ Net income ($112.0B)** → profits are backed by real cash, not accruals.
- **Applies when:** any public company — this is the universal first-pass literacy read.
- **Breaks when:** Apple's *equity is artificially low* ($73.7B on $112B income → ROE looks
  >150%) because of years of **buybacks** shrinking equity. Ratios lie without the context;
  this is the bridge to Course 02 (capital allocation) and **E2**.
- **Practitioner counterpoint:** (to fill via `research` → r/SecurityAnalysis / r/FinancialCareers)
  — "what do analysts read FIRST in a 10-K?" Common answer: risk factors + MD&A, then the
  cash flow statement, *before* the income statement headline.
- **Links:** [[02-corporate-finance-dcf]] · [[E2-capital-allocation-buybacks]] · [[04-strategy-five-forces-aapl]]

---
### Do-it-yourself reps
1. `python3 _ingest/edgar.py company MSFT` → fill this same table for Microsoft, compare margins.
2. Open the real 10-K link → read **Item 1A Risk Factors** and **Item 7 MD&A**; note 3 risks.
3. `python3 _ingest/edgar.py search "supplier concentration"` → see who else flags it.
