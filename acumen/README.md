# The Acumen Gym — a judgment regimen

> **Goal:** build credible business acumen at a masters level *and beyond* — to communicate and
> advise executives, read the landscape, and execute. Not a credential, not an exam score: **judgment.**
>
> **Premise:** judgment isn't transferred by reading summaries. It's built by making real calls on
> real situations with no answer key, then having them torn apart by someone playing a sharp
> partner/CFO/board member. The corpus (`notes/canon`, `lessons/`) is the reference shelf behind this;
> the reps happen here.

## Roles
- **You** make the call. You produce the deliverable — the diagnosis, the position, the memo. The
  judgment is yours; that's the whole point.
- **Me (the red team)** set real cases, then adversarially critique your thinking the way a skeptical
  board member would: *where's the crux you missed, where's your conviction, what would the bear say,
  you gave me a matrix — give me a recommendation.* I do not write your memo.

## The loop (one case ≈ one rep)
> Knowledge and reps interleave — you need a *floor* to start, then the rep itself tells you what to
> learn next. Knowledge serves the rep; the rep directs the knowledge.

0. **Prime** — before each rep, pull the *case-specific* knowledge from the shelf (`notes/canon`,
   `lessons/`): the 3–5 frameworks the call actually needs + the figures to extract. Enough to make
   the call competently — **not** everything. (`case-NN-prime.md`.)
1. **Case set** — I give you a real company + a live, contestable decision. No fabricated numbers;
   you pull real data (EDGAR via `_ingest/edgar.py`).
2. **You diagnose + decide** — name the *crux*, take a position, do the actual analysis.
3. **You write the memo** — the 1-page exec deliverable (spec below). Take a stance; no hedging.
4. **I red-team** — score on the rubric, then attack: the bear case, the hole, the question that
   sinks you in the boardroom.
5. **Learn the exposed gap** — the red-team surfaces exactly what you didn't understand. *That* is the
   next study target — just-in-time, motivated, retained. This is how knowledge → understanding.
6. **Log** — update `JUDGMENT-LEDGER.md` with the score + the recurring pattern. This is how it
   compounds — we watch your soft spots harden over cases.

**Cadence:** ~1 case/week (or as fast as you want the reps). Difficulty escalates as scores rise.

## The deliverable spec — a 1-page board memo
Keep it to one page. Exec altitude. Every claim backed by a real number from the filings.
1. **Recommendation (BLUF)** — one sentence: the call. (Not "it depends.")
2. **The crux** — the single most pivotal, *solvable* challenge the decision turns on (1–2 sentences).
3. **Why — three reasons** — each with a real figure/fact (from the 10-K, the cash flows, the market).
4. **The fatal risk + mitigation** — the one thing that, if wrong, sinks the plan; and what you'd do.
5. **The ask** — what you want the board to approve/decide.

## The rubric (how I grade, 1–5 each)
| Dimension | The question a sharp partner asks |
|---|---|
| **Diagnosis** | Did you find the *real* crux, or restate the obvious? |
| **Conviction** | Did you *recommend*, or hide in a tradeoffs matrix? |
| **Evidence & execution** | Are the numbers right and the frameworks correctly applied? |
| **Landscape** | Did you read the competitive / market / macro reality? |
| **Communication** | Exec altitude, BLUF, brief — would a CFO buy it in 90 seconds? |
| **Second-order & bear case** | Did you see what happens *next*, and the strongest counter-argument? |

Passing = avg ≥ 3.5; "advise-the-board ready" = ≥ 4.5 with no dimension below 4.
Below-a-masters tells: framework dumping, no recommendation, vanity metrics, ignoring the bear case,
treating a presumption as a fact.

## Files
- `case-NN-<company>.md` — the case brief + where you paste your memo + my red-team.
- `JUDGMENT-LEDGER.md` — running scorecard + recurring strengths/gaps across cases.
