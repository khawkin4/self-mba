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
- **Practitioner counterpoint:** *(researched 2026-06-05 — TOC walkthrough transcripts; r/operations
  re-pull pending)* A live shop-floor demo nails the killer insight: in Shrinivas Gondhalekar's
  ball-pen line, the team cut a 15-unit build from **9:20 down to 66 seconds with zero added
  resources** — *"no increase in resources… only redistribution of the work."* The non-obvious part
  practitioners stress is **subordination, not speed**: *"if the previous operations work faster it
  is of no use because the output does not go up and only WIP builds up in between."* They signal the
  bottleneck's pace literally by **tapping the table** — *"indication from a central planner is no
  use"* — i.e. the system follows the constraint, not the plan. The killer line in summary form
  (Corporate Stickman): *"it doesn't matter how fast cars are moving everywhere else"* if there's a
  jam at one exit.
- **Researched layer** *(2026-06-05)* *(corpus thin — no Reddit in pull; flagged for re-pull)*
  - **Canonical explanation (sourced):** The mechanism is that a system's output is governed by one
    constraint, so non-bottleneck effort is wasted motion. As one TOC walkthrough puts it,
    *"the bottleneck is the limiting operation — you cannot work faster than the bottleneck, and if
    the previous operations work faster it is of no use because the output does not go up and only
    WIP builds up in between"* (Shrinivas Gondhalekar — *TOC Theory of Constraints & De-bottlenecking*).
    The book's three metrics anchor this: *"throughput is the rate at which the system generates
    money, inventory is the money tied up in the system, operating expense is the money spent to turn
    inventory into throughput"* (Corporate Stickman — *The Goal* summary).
  - **Real application (mined):** A 15-unit ball-pen assembly line, four operators. **Step 1** identify
    the bottleneck (the operator who hits max WIP first). **Step 2** subordinate — the previous stations
    *synchronize to the bottleneck's pace* via a tapped signal, killing inter-station WIP while output
    holds. **Step 3** elevate without spend — redistribute the idle operator's slack so the constraint
    operator gets help. Result: build time fell from **9:20 to 66 seconds (~7x), no resources added** —
    a clean physical proof of "exploit + subordinate before you elevate."
  - **Where the corpus pushes back on the book:** The transcripts faithfully evangelize TOC but expose
    its scope limit by example — every demo is a **physical, serial line** where the constraint is
    visible and stationary (an oven baking 10 pizzas/hour, a slow relay runner, a ball-pen station).
    None model knowledge work, shifting human-attention constraints, or demand-limited systems where
    "elevate the constraint" adds capacity nobody needs — exactly the *breaks-when* cases. The
    community/ops practitioner voice (r/operations, r/supplychain) is **absent from this pull** and
    should be re-pulled to stress-test TOC against messy real deployments.
  - **Sources in corpus:** Shrinivas Gondhalekar — "TOC Theory of Constraints & De bottlenecking"
    (youtube.com/watch?v=Lorz-tRYwTQ) · Corporate Stickman — "Fix Bottlenecks & Boost Productivity |
    The Goal by Eliyahu Goldratt (Book Summary)" (youtube.com/watch?v=_M00FIFLDUw). *(No Reddit threads
    in this pull.)*
- **Links:** [[canon-meadows-thinking-in-systems]] · [[canon-ohno-toyota-production-system]] ·
  [[canon-larson-elegant-puzzle]]

---
### Rep
Map one real process you touch (`_ingest`-style: inputs → steps → output). Find the single step
where work piles up — that's your constraint. What would *exploiting* it (not improving the rest)
look like?
