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
6. **Answer the meta-question** — *which canon note, had you actually read it, would have changed this
   memo?* One note. It goes in the Shelf debt table in `JUDGMENT-LEDGER.md`. This is the leg that
   audits the shelf instead of the rep: a book stays unapplied until a rep needs it, and then it jumps
   the queue. Three mentions of the same note promotes it to next-read.
7. **Log** — update `JUDGMENT-LEDGER.md`: the six scores, whether the crux was named unprompted, the
   forecast, and the recurring pattern. This is how it compounds — we watch your soft spots harden
   over cases.

**Cadence — one rep a week, from a menu of three sizes.** The menu exists so the streak survives a bad
week; the mandate is the thing that broke last time (the tool shipped 2026-06-06 and sat unused for 16
weeks because skipping cost nothing).

| Size | Time | Deliverable |
|---|---|---|
| **Full** | ~90 min | The 1-page board memo below |
| **Crux-only** | ~25 min | The crux in two sentences + the one figure proving it + the bear case in one line |
| **Single-figure call** | ~10 min | One figure from the filings, what it decides, your call. Three sentences |

A 10-minute rep scores and counts. A skipped 90-minute rep does not — and gets logged as a `skipped`
row in the ledger, so the gap is visible. Difficulty escalates as scores rise. Full spec of the
mechanism, including the input metrics that actually matter: [MECHANISM.md](MECHANISM.md).

## The deliverable spec — a 1-page board memo
Keep it to one page. Exec altitude. Every claim backed by a real number from the filings.
1. **Recommendation (BLUF)** — one sentence: the call. (Not "it depends.")
2. **The crux** — the single most pivotal, *solvable* challenge the decision turns on (1–2 sentences).
3. **Why — three reasons** — each with a real figure/fact (from the 10-K, the cash flows, the market).
4. **The fatal risk + mitigation** — the one thing that, if wrong, sinks the plan; and what you'd do.
5. **The ask** — what you want the board to approve/decide.

Plus, on every rep regardless of size: **attach one forecast** — a falsifiable statement with a
probability and a resolution date ("70% that gross margin is below X% by FY-end"). That is what makes
calibration measurable rather than a feeling. Then **size it**: pass / probe / commit, in one line, and
why that size fits that probability. Being right about direction and wrong about size is how people
with tomorrow's newspaper still went bust ([bet-sizing-conviction](../notes/bet-sizing-conviction.md)).

## The rubric (how I grade, 1–5 each)
| Dimension | The question a sharp partner asks |
|---|---|
| **Diagnosis** | Did you find the *real* crux, or restate the obvious? |
| **Conviction** | Did you *recommend*, or hide in a tradeoffs matrix? And does the *size* of the commitment match the forecast's probability? |
| **Evidence & execution** | Are the numbers right and the frameworks correctly applied? |
| **Landscape** | Did you read the competitive / market / macro reality? |
| **Communication** | Exec altitude, BLUF, brief — would a CFO buy it in 90 seconds? |
| **Second-order & bear case** | Did you see what happens *next*, and the strongest counter-argument? |

Passing = avg ≥ 3.5; "advise-the-board ready" = ≥ 4.5 with no dimension below 4.
Below-a-masters tells: framework dumping, no recommendation, vanity metrics, ignoring the bear case,
treating a presumption as a fact.

## Files
- `MECHANISM.md` — the mechanism: countable results, controllable input metrics, the three legs, the
  meta-question, and the amendment log. Read this if the gym stops running.
- `CASE-TEMPLATE.md` — skeleton for a new case, so standing one up costs minutes.
- `case-NN-<company>.md` — the case brief + where you paste your memo + my red-team.
- `JUDGMENT-LEDGER.md` — the instrument: rep log (including skipped weeks), scores, input metrics,
  shelf debt, recurring strengths/gaps.
