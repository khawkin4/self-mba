# Note · Goldratt — *The Goal*

> Canon · Cluster: Execution & Operations · Maps to **Course 06** (Operations & Supply Chain)

- **Source:** Eliyahu Goldratt, *The Goal* (1984) — Theory of Constraints, as a novel
- **Core claim:** Every system has **one constraint** — a single bottleneck that limits total
  throughput. **Optimizing anything that isn't the bottleneck is an illusion of progress.**
- **Framework — the five focusing steps:**
  1. **Identify** the system's constraint.
  2. **Exploit** it — squeeze maximum output from it (never let the bottleneck idle).
  3. **Subordinate** everything else to that decision — the whole system serves the bottleneck.
  4. **Elevate** the constraint — add capacity to it.
  5. **Repeat** — the constraint *moves*; go back to step 1 (don't let inertia become the new
     constraint).
  - Reframes efficiency: **local optimization of a non-constraint is waste** (it just builds
    inventory in front of the bottleneck).
- **Applies when:** any flow system with a measurable throughput — a factory, a sales pipeline, a
  CI/CD chain, a hospital, an org's decision flow.
- **Breaks when:** the single-bottleneck model is cleanest in **physical, serial** systems — in
  knowledge work the constraint is often invisible, shifting, or *human attention*, which resists
  the "subordinate everything to it" prescription. Some systems have *multiple* binding constraints
  at once. And "elevate the constraint" can be the wrong move if demand itself is the real limit
  (you'd be adding capacity nobody needs). Deep kinship with Meadows' leverage points
  ([[canon-meadows-thinking-in-systems]]) and Larson's throughput framing
  ([[canon-larson-elegant-puzzle]]).
- **Practitioner counterpoint:** (fill via `research` → r/operations, r/supplychain) — ops folks
  say the killer insight is "an hour lost at the bottleneck is an hour lost for the whole system;
  an hour saved at a non-bottleneck is a mirage."
- **Links:** [[canon-meadows-thinking-in-systems]] · [[canon-ohno-toyota-production-system]] ·
  [[canon-larson-elegant-puzzle]]

---
### Rep
Map one real process you touch (`_ingest`-style: inputs → steps → output). Find the single step
where work piles up — that's your constraint. What would *exploiting* it (not improving the rest)
look like?
