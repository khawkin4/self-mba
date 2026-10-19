# Judgment Ledger

> The instrument. Not a report card — the point is the *pattern*: where judgment is consistently sharp
> versus soft, so the soft spots get drilled until they harden. Mechanism spec: [MECHANISM.md](MECHANISM.md).
>
> **Two rules.** Every rep gets scored, even a bad one. Every *skipped* week gets a row, so the gap is
> visible instead of invisible.

## Status

| | |
|---|---|
| **Baseline** | **Not yet measured.** No rep has been scored |
| Tool complete since | 2026-06-06 |
| Mechanism live since | 2026-09-26 |
| Weeks elapsed before the mechanism | 16 |
| Reps scored in those weeks | 0 |
| Open cases | 5 briefed, 0 scored — see the menu below |

The first scored rep — whatever it scores — is the baseline. A measured bad number is worth more than
no number, because it is the only thing that makes later improvement visible.

## The menu

Pick one a week. The sizes exist so a bad week still produces a scored rep.

| Case | Company | Size | Time | Exercises |
|---|---|---|---|---|
| [case-01-intel](case-01-intel.md) | Intel | full | ~90 min | Grove (inflection), Christensen, Helmer, Rumelt, Klarman |
| [case-02-boeing](case-02-boeing.md) | Boeing | crux-only | ~25 min | Goldratt (the constraint), Ohno, Perrow, Bungay |
| [case-03-carvana](case-03-carvana.md) | Carvana | single-figure | ~10 min | Akerlof (lemons), Klarman |
| [case-04-disney](case-04-disney.md) | Disney | full | ~90 min | Lafley-Martin, Brandenburger-Nalebuff, Schelling, Helmer |
| [case-05-seed-fund-2022](case-05-seed-fund-2022.md) | Hypothetical $150M seed fund (June 2022) | full, **sealed key** | ~90 min | Klarman, Taleb, Tetlock (base rates), Mauboussin; WSS regime map |

Each case's "Canon to bring to bear" list *is* its prime — three to five frameworks, no more. Cases
02–04 deliberately pull canon notes that `STRUCTURAL-ANALYSIS.md` flagged as never applied.

## Rep log

One row per week. `done` = a scored memo. `skipped` = no rep; say why in one honest clause.

| Week of | Case | Size | Status | Forecast made | Notes |
|---|---|---|---|---|---|
| 2026-06-08 → 2026-09-21 | case-01-intel | full | **skipped** (16 wks) | — | Tool built, no adoption or inspection leg; nothing made the rep happen |
| 2026-09-26 | case-03-carvana + case-02-boeing | single-figure + crux-only | **demo** (Claude wrote both) | yes, both | First run of the harness. Both failed — 3.17 and 3.00. Not the baseline |
| 2026-09-28 | *pick from the menu* | — | open | — | First rep under the mechanism |

## Scores

Six dimensions, 1–5. Passing = avg ≥ 3.5. Advise-the-board ready = ≥ 4.5 with nothing below 4.

| # | Case | Date | Diagnosis | Conviction | Evidence | Landscape | Comms | 2nd-order | Avg | Crux unprompted? |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Intel — capital allocation | — | — | — | — | — | — | — | — | — |

### Demo reps — memos written by Claude, NOT the baseline

These measure Claude's judgment, not yours. They exist as worked examples and as the first proof the
harness runs. Your baseline is still unmeasured.

| # | Case | Date | Diagnosis | Conviction | Evidence | Landscape | Comms | 2nd-order | Avg | Crux unprompted? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03 | carvana (demo) | 2026-09-26 | 3 | 4 | 4 | 2 | 4 | 2 | 3.17 | yes |
| 02 | boeing (demo) | 2026-09-26 | 3 | 4 | 2 | 2 | 4 | 3 | 3.00 | yes |

Both **failed** (pass is ≥ 3.5). The red-teams in the case files are a better guide to what the rubric
actually rewards than the rubric is.

## Input metrics

Read these, not the corpus counts. Definitions in [MECHANISM.md](MECHANISM.md).

| Metric | Yours | Demo (Claude) | Target |
|---|---|---|---|
| Reps scored / week (4-week rolling) | 0.0 | 2 in one day | 1.0 |
| Unprompted crux rate | — | 100% (2/2) | ≥ 60% |
| Rubric dimensions below 4 (latest rep) | — | 4 (boeing) | 0 |
| Shelf debt open | 2 | — | ≤ 3 |
| Weeks skipped (rolling 8) | 8 | — | ≤ 1 |
| Calibration error (mean, resolved forecasts) | — | unresolved until 2027 | ≤ 0.15 |
| Sizing coherence (size fits probability) | — | not scored (predates the rule) | ≥ 80% |

## Shelf debt

The evidence-ranked reading list. One row per red team, answering: *which canon note, had I actually
read it, would have changed this memo?* Three mentions of the same note promotes it to the front of the
queue **and** earns it a practitioner application note.

| Rep | Note the red team named | Mentions | Read? | Application note written? |
|---|---|---|---|---|
| 03 carvana (demo) | `canon-helmer-7-powers` — a 100%-margin line with no named barrier is a price, not a moat | 1 | no | no |
| 02 boeing (demo) | `canon-taleb-black-swan` — operating losses within ~3% of book equity; survivability beats average unit economics | 1 | no | no |
| 03 runner-up | `canon-perrow-normal-accidents` — tight coupling from origination to the ABS bid | 1 | no | no |
| 02 runner-up | `canon-mankiw-principles-of-economics` — marginal vs average cost | 1 | no | no |
| 02 third | `canon-sterman-business-dynamics` — an inventory drawdown can be a de-stocking echelon | 1 | no | no |

Four of the five sit on `STRUCTURAL-ANALYSIS.md`'s never-applied list. The meta-question surfaced them
in two reps; sixteen weeks of coverage-driven planning had not.

## Recurring strengths

- *(populated after reps — needs at least 3 to be a pattern, not a fluke)*

## Recurring gaps — the drill list

From two demo reps only, so a hypothesis rather than a pattern — the mechanism says three before it
counts. These are Claude's gaps; whether they are yours is unmeasured.

- **Landscape scored 2 on both.** Both memos stayed entirely inside the 10-K: no comparables, no funding
  or credit-market read, no competitive response. A thesis that depends on an external market — ABS
  demand for Carvana, certification and supplier capacity for Boeing — cannot be built from the filing
  alone.
- **A ratio whose construction was never interrogated.** Carvana: divided a gross-profit line by a net
  income produced by a $2.8B tax benefit on a pre-tax *loss*. Boeing: divided a segment loss
  substantially composed of reach-forward charges on undelivered aircraft by current-year deliveries.
  The same error twice — each figure was verified against the filing, but what it was *made of* was not.
- **Second-order weak exactly where the counter-argument is management's own.** Both filings state the
  opposing case explicitly; neither memo engaged it.

## Trajectory notes

- *(e.g. "conviction 2 → 4 over cases 1–4; second-order still soft")*
