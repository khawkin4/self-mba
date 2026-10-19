# The Acumen Mechanism

> A tool with no adoption and no inspection is a good intention. This file is the mechanism that
> makes the gym actually run: what it is for, the countable results, the inputs it moves, and how it
> gets inspected. Companion to `learn/VALIDATION.md` — same shape, one layer up. That flywheel guards
> whether a *unit teaches*; this one guards whether *judgment improves*.

## The challenge, worked backwards

**Recurring challenge:** judgment does not build from reading. The corpus grows every month; the
ability to make a defensible call on a live decision does not follow it.

**Three countable results** (the ORR pattern — AWS named *fewer, shorter, smaller* incidents):

| Result | Counted as |
|---|---|
| **More** reps | Cases *scored*, not briefed |
| **Sharper** diagnosis | Share of reps where you named the crux before the red team named it |
| **Fewer** soft spots | Rubric dimensions scoring below 4 |

## The controllable inputs

| Input metric | Definition | Source | Why it's controllable |
|---|---|---|---|
| **Reps / week** | A scored memo landed in the ledger. Target: 1 | Rep log | You decide whether to sit down |
| **Unprompted crux rate** | Did your stated crux survive the red team, without it being handed to you from the case's canon list? | Red-team output | Improves with reps and with reading the right thing |
| **Dimensions below 4** | Count of the six rubric dimensions under 4 on the latest rep | Scores table | Each one names a specific drill |
| **Shelf debt closed** | Canon notes the red team flagged as *would have changed this memo*, that you then actually read | Shelf debt table | A short, evidence-ranked list |
| **Calibration error** | \|stated probability − outcome\| on the forecast attached to each call | Rep log, scored when resolvable | Forces a number instead of a hedge |
| **Sizing coherence** | Share of reps where the red team judged the pass / probe / commit size consistent with the stated probability | Red-team output, scored immediately | Calibration alone doesn't pay; the size you attach to it does. Unlike calibration, it needs no resolution date |

**Explicitly not inputs.** 24 modules, 82 books, 352 cross-links, 55 site pages, ~1.5M words
ingested. These measure corpus *size*. They are outputs of a production mechanism that already works
well, and none of them moves judgment. The rubric in `README.md` lists "vanity metrics" as a
below-a-masters tell — that applies to this repo's own dashboard.

## The three legs

| Leg | What it is | Lives in |
|---|---|---|
| **Tool** | Six-dimension rubric, one-page memo spec, case template | `README.md`, `CASE-TEMPLATE.md` |
| **Adoption** | One rep a week, chosen from a menu of three sizes; the rep is scheduled, and a skipped week is logged as a row | `JUDGMENT-LEDGER.md` |
| **Inspection** | Every rep scored on the rubric; monthly read of the ledger for the pattern; the meta-question after every red team | `JUDGMENT-LEDGER.md` |

## Adoption: why this failed once, and the fix

Honest record. The tool was complete on **2026-06-06**. Case 01 was briefed the same day and the memo
was never written. Sixteen weeks against a stated cadence of one case a week: **zero scored reps.**

Nothing in the loop cost anything when a week was skipped, so skipping was the dominant strategy.
This is the failure the Bezos canon note already predicts — *"the mechanism is only as live as the
incentives underneath it."* Three changes, each borrowed from mechanism design:

1. **Log the deviation; don't leave a hole.** A missed week gets a row in the rep log with reason
   `skipped`. An absence you can see is a cost; an absence you can't is free.
2. **A menu, not a mandate.** Every week offers three sizes — **full memo** (~90 min), **crux-only**
   (~25 min), **single-figure call** (~10 min). The small option exists so the streak survives a bad
   week. A 10-minute rep scores and counts; a skipped 90-minute rep does not.
3. **Reps are the allocated resource.** Treat them like budget or headcount: 52 a year, spent or
   forfeited, tracked in one place. This is the cycle-time-as-finite-resource idea applied to a
   system of one.

## Inspection: three altitudes

- **Per rep** — the red team scores all six dimensions, names the bear case, and names the boardroom
  question that sinks you. No rep closes unscored.
- **Per month** — read the ledger for the *pattern*, not the score: which dimension is consistently
  soft, whether the crux rate is moving, how many weeks were skipped.
- **Meta** — the question below, which inspects the corpus rather than the rep.

## The meta-question

After every red team, answer exactly one question:

> **Which canon note, had I actually read it, would have changed this memo?**

The answer goes in the **Shelf debt** table in the ledger. This is the correction-of-error move: AWS's
incident template asks *"would any ORR recommendations have reduced or avoided the impact of this
event?"*, so every failure audits the mechanism meant to prevent it. Here, every rep audits the shelf.

Three effects:

- It produces a reading list ranked by **evidence** instead of by coverage.
- It is the only honest test of whether the 82 notes earn their keep.
- It collapses two of the repo's named structural gaps — 33 unapplied books, 14 sources-only clusters
  — into one queue. A book stays unapplied until a rep needs it, and then it jumps the line.

**Rule:** if three consecutive reps name the same note, that note is the next thing you read *and* the
next practitioner application note you write.

## Iteration

When the red team repeats the same critique across three cases, the fix belongs in the **tool**, not in
the next rep — amend the memo spec or the rubric in `README.md` and log it below. Same rule as the
`learn/` flywheel: a repeated fix becomes a template change.

## Amendment log

| Date | Change | Why |
|---|---|---|
| 2026-09-26 | Mechanism written: deviation logging, case-size menu, meta-question, input metrics | The tool had existed since 2026-06-06 with no adoption and no inspection — 16 weeks, 0 scored reps |
| 2026-10-04 | Added a one-line size (pass / probe / commit) to every forecast; Conviction now scores size-vs-probability fit; new input metric *sizing coherence* | Elm Wealth experiment ([bet-sizing-conviction](../notes/bet-sizing-conviction.md)): with tomorrow's news, laypeople and AI models still lost on sizing, while pros won by matching size to confidence. The gym measured confidence but never the commitment attached to it |
