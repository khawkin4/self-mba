# Case 01 — Prime (the knowledge this call needs)

> Pulled from the shelf so you can rep competently. This gives you the **lenses and the figures to
> extract** — not the diagnosis or the recommendation. Naming the crux and taking the position is
> your rep. Go deeper on any lens via the linked notes/lessons.

## 1. The decision frame — capital allocation
A capital-allocation call is "where does the next dollar go," judged on **return on incremental
capital vs. cost of capital**. The five uses: reinvest in the business · M&A · dividends · buybacks ·
pay down debt. Two tests that decide this case:
- **One-way vs. two-way door** (Bezos): building leading-edge fabs is a multi-year, ~irreversible
  one-way door — it demands deliberation and a higher bar than a reversible bet.
- **Margin of safety** (Klarman): don't size the bet so large that one bad surprise (a node slip, a
  demand air-pocket) is fatal to the balance sheet.
- *Go deeper:* `notes/canon/canon-bezos-shareholder-letters`, `canon-klarman-margin-of-safety`,
  `lessons/exec-E2-capital-allocation.html`.

## 2. The landscape lens — is the moat gone, and is this an inflection?
- **7 Powers** (Helmer): name Intel's *actual* remaining power, if any — **process power / scale /
  cornered resource** — and ask whether TSMC has taken it. "Strong brand" is not a power; be precise.
- **Strategic inflection point** (Grove, *his own company*): is this a **10×** force (process
  leadership lost; compute demand shifting from CPU to accelerators), where the old strategy stops
  working?
- **Disruption** (Christensen): Intel pressured from *below* (good-enough efficiency/ARM) and from
  the *side* (GPU/accelerators it doesn't lead). Which is the binding one?
- *Go deeper:* `canon-helmer-7-powers`, `canon-grove-only-the-paranoid-survive`,
  `canon-christensen-innovators-dilemma`.

## 3. The crux discipline (this is the rep)
Rumelt: the call turns on **one pivotal, *solvable* challenge** — your job is to *name it*, not list
all of Intel's problems. A strong memo's crux looks like *"whether Intel can reach process parity with
TSMC before the foundry capex exhausts its balance-sheet runway — everything else is downstream."*
A weak one restates the obvious ("Intel faces intense competition"). *Go deeper:* `canon-rumelt-the-crux`.

## 4. The numbers to pull and the test (execution/literacy)
From `edgar.py facts INTC` + the 10-K, extract and *interpret*:
| Figure | Why it decides the call |
|---|---|
| **Capex vs. operating cash flow** | Is the foundry bet outrunning internally generated cash? Gap = financing/dilution risk. |
| **Gross-margin trend** | Proxy for process competitiveness; falling margin = losing the manufacturing edge. |
| **Cash & total debt** | The runway / margin of safety for a multi-year bet. |
| **Segment mix & trend** | Is the cash-cow core (CPU) eroding faster than the bet can mature? |
| **R&D + the ROIC vs. WACC test** | Is reinvested capital earning *above* its cost? If ROIC < WACC, reinvestment destroys value. |

The core test: **does the incremental capital earn its cost of capital, and can the balance sheet
survive if it doesn't for 2–3 more years?** *Go deeper:* `lessons/core-02-corporate-finance.html`,
`lessons/gaps-managerial-accounting.html`, the AAPL 10-K worked note in `notes/01-accounting`.

## 5. Communication (so it lands)
Minto: **answer first.** Open with the call, then the crux, then three evidenced reasons. A CFO
should get your recommendation in the first sentence and the *why* in 90 seconds. *Go deeper:*
`canon-minto-pyramid-principle`, `lessons/exec-E7-exec-presence-comms.html`.

---
**You now have the floor.** Pull the real INTC numbers, name the crux, take the side, write the
1-page memo (spec in `README.md`), and bring it back. Where this prime falls short is exactly what
the red-team will expose — and that gap becomes your next study target.
