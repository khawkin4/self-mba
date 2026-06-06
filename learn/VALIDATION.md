# Validation & the teaching flywheel

> A unit isn't "done" because I wrote it — it's done when it's *validated to teach*. This is the
> feedback loop that makes the curriculum improve instead of just grow.

## The flywheel
```
   write/​revise a unit
          │
          ▼
   VALIDATE  ──►  measure where it fails  ──►  fix list  ──►  revise  ─┐
          │                                                            │
          └──────────────── re-validate ◄─────────────────────────────┘
```
Each turn: the failures tell us exactly what to fix in *this* unit, and the patterns tell us how to
fix the *template* for every future unit. Validation data is the steering, not a report card.

## What "validated" means — three automated checks + one human gold standard

**Automated (fast, cheap, every revision):**
1. **Accuracy audit** *(expert agent)* — re-derive every figure and every "Check yourself"/Application
   answer; flag any wrong number or wrong computed answer. (Numbers are real SEC data; the answers must
   actually be correct.) **Hard gate: zero accuracy errors.**
2. **Beginner-clarity review** *(agent role-playing a true novice, no outside knowledge)* — flag every
   term used-before-defined, every logical leap, every place a beginner gets lost, and whether the
   example actually made the concept click. **Gate: clarity ≥ 4/5, no undefined-jargon blockers.**
3. **Objective alignment** *(expert agent)* — does the unit have clear learning objectives, and does its
   assessment test each one? Flag taught-but-not-tested and tested-but-not-taught. **Gate: full coverage.**

**Human gold standard (periodic, the real proof):** a real beginner reads the unit and takes the
held-out application. Agent-as-beginner is a *proxy* — it knows too much — so it can only catch
clarity/leap failures, not prove a human learned. The human test is ground truth; the automated loop
just lets us iterate fast between human checks.

## Thresholds — severity-gated (so the loop actually converges)
A naive-reader proxy will *always* find one more nit, so a "zero findings" gate is a hamster wheel, not
a flywheel. Findings are therefore graded by **severity**, and only real comprehension-breakers gate:
- **blocking** — a beginner genuinely can't understand the core idea here, or it's tested-but-untaught.
- **minor** — a term inferable from context that should still be glossed (backlog, doesn't gate).
- **cosmetic** — idiom/style a novice rides past (nice-to-have).

A unit **passes** when: **accuracy clean · objectives covered · clarity ≥ 4 · zero *blocking* findings.**
Minor/cosmetic items are logged as backlog, not failures. This converges — and it's honest about the
fact that the agent-beginner has a pedantry ceiling; the **real human read is the ground truth** that
catches what the proxy can't, and resolves whether the remaining minors actually matter.

## The loop in practice
- Harness: `_ingest/learn_validate_workflow.js` (per unit: an expert auditor for checks 1+3, a
  naive-beginner for check 2; runs across all units in parallel).
- Results + fix lists logged in `VALIDATION-LOG.md` (dated, so we see units improve over turns).
- Fix → re-run → log. When a fix pattern repeats, fold it into the unit template in `README.md`.
