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
- **Practitioner counterpoint:** *(researched 2026-06-06 — book-specific re-pull: Elite Compass *The
  Goal* summary + a TOC constraint-vs-bottleneck walkthrough)* The sharpest practitioner correction to
  a casual reading of the book is that **a bottleneck is not the same thing as the constraint** —
  *"a bottleneck is a resource with capacity less or equal to the demand put upon it, while a
  constraint is a limiting factor of the organisation's performance… a constraint can be called a
  bottleneck but the bottleneck is not always a constraint"* (Theory of Constraints walkthrough,
  6UT1EnL7nOc). In the worked plant example there are *two* bottlenecks (resources B and E) but only
  one is the system constraint: *"working to improve the throughput on B is of little interest as long
  as it keeps being the limiting factor… all attention must be focused on the constraint."* Speeding up
  the wrong bottleneck just *"extend[s] the queue of working progress"* — the exact local-optimization
  trap the book warns against.
- **Researched layer** *(updated 2026-06-06)*
  - **Canonical explanation (sourced):** A system's output is governed by one constraint, so
    non-bottleneck effort is wasted motion that only piles up WIP. The book frames profitability around
    three interlocking metrics: *"throughput measures how much revenue the system generates from sales,
    inventory reflects money tied up in raw materials and unsold products, operational expenses
    encompass the costs of turning inventory into throughput… these three metrics are interconnected
    and provide a clear framework for decision-making"* (Elite Compass — *Book Summary of The Goal*,
    y7ORK5qIbOw). The summary also stresses that fixing one constraint surfaces the next: *"fixing one
    bottleneck often reveals another, which means that monitoring and addressing constraints must
    become an ongoing practice"* — i.e. step 5, "repeat," is the real lesson, not a one-time fix.
  - **Real application (mined):** A 15-unit ball-pen assembly line, four operators. **Step 1** identify
    the bottleneck — *"why is it the bottleneck? It's because I have maximum WIP, it's already reached
    three pieces."* **Step 2** subordinate — *"if the previous operations work faster it is of no use
    because the output does not go up and only WIP builds up in between,"* so upstream stations
    synchronize to the bottleneck's pace via a tapped-table signal. **Step 3** elevate without spend —
    redistribute slack toward the constraint. Result: a clean physical proof of "exploit + subordinate
    before you elevate" (Shrinivas Gondhalekar — *TOC Theory of Constraints & De-bottlenecking*,
    Lorz-tRYwTQ). The Corporate Stickman summary gives the one-line mental model: *"if there's a
    traffic jam at one exit, it doesn't matter how fast cars are moving everywhere else"* (_M00FIFLDUw).
  - **Where the corpus pushes back on the book:** The constraint-vs-bottleneck transcript exposes a
    real subtlety the novel glosses — once you elevate the binding constraint past the next bottleneck,
    *"B will become the system's constraint and E will remain the bottleneck"*: the constraint **moves**,
    and a static read of "find the bottleneck" misleads. And every demo is a **physical, serial line**
    where the constraint is visible and stationary; none model knowledge work, shifting human-attention
    constraints, or demand-limited systems where "elevate the constraint" adds capacity nobody needs —
    exactly the *breaks-when* cases. (No Reddit threads surfaced in this pull, so the messy-real-world
    deployment voice is still under-sampled.)
  - **Sources in corpus:** Elite Compass — "Book Summary of The Goal | Eliyahu Goldratt & Jeff Cox"
    (youtube.com/watch?v=y7ORK5qIbOw) · "The subtle difference between a constraint and a bottleneck
    (Theory of Constraints)" (youtube.com/watch?v=6UT1EnL7nOc) · Shrinivas Gondhalekar — "TOC Theory of
    Constraints & De bottlenecking" (youtube.com/watch?v=Lorz-tRYwTQ) · Corporate Stickman — "Fix
    Bottlenecks & Boost Productivity | The Goal by Eliyahu Goldratt (Book Summary)"
    (youtube.com/watch?v=_M00FIFLDUw). *(No Reddit threads in this pull.)*
- **Links:** [[canon-meadows-thinking-in-systems]] · [[canon-ohno-toyota-production-system]] ·
  [[canon-larson-elegant-puzzle]]

---
### Rep
Map one real process you touch (`_ingest`-style: inputs → steps → output). Find the single step
where work piles up — that's your constraint. What would *exploiting* it (not improving the rest)
look like?
