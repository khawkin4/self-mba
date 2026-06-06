# Note · Ohno — *Toyota Production System*

> Canon · Cluster: Execution & Operations · Maps to **Course 06** (Operations & Supply Chain)

- **Source:** Taiichi Ohno, *Toyota Production System* (1978) — the origin of lean
- **Core claim:** Relentlessly **eliminate waste (*muda*)** and build quality into the process, so
  problems surface and get fixed at the source rather than hidden by inventory.
- **Framework:**
  - **The seven wastes:** overproduction · waiting · unnecessary transport · overprocessing · excess
    inventory · unnecessary motion · defects. (Overproduction is the worst — it hides the others.)
  - **Pull, not push** — produce only what's needed, when it's needed (just-in-time / *kanban*).
  - **Kaizen** — continuous improvement as a *cultural practice*, not a project with an end date.
  - **Jidoka / "stop the line"** — any worker can halt production on a defect. Short-term cost,
    massive long-term quality gain. Migrated far beyond cars (software, healthcare, ops).
- **Applies when:** any repeatable process where flow, quality, and inventory matter — and where the
  culture can support workers *stopping* the line.
- **Breaks when:** **JIT trades resilience for efficiency** — zero inventory shatters under supply
  shocks (COVID, the chip shortage made this vivid); it's *fragile* in Taleb's sense
  ([[canon-taleb-antifragile]]). "Stop the line" only works with real psychological safety and
  worker competence — bolted onto a blame culture it's dead on arrival. And lean tools copied
  without the *culture* (the most common failure) produce cargo-cult kaizen — checklists, no
  improvement.
- **Practitioner counterpoint:** *(researched 2026-06-05 — r/supplychain corpus)* The corpus is a live
  case study in JIT's fragility thesis: when an upstream shock hits, lean inventory has no cushion. A
  r/supplychain thread "**Shipping costs from suppliers in china are exploding. $200 → $1200**" (549↑)
  has a buyer whose *"parts that's supposed to cost $150 [are] now costing us close to $1800"* after a
  carrier change plus tariffs — with zero buffer, every shock lands instantly on the line. "**The first
  shortages due to the Gulf of Hormuz are beginning to arrive**" (240↑) and JP Morgan's Persian-Gulf
  oil-arrival map (408↑) show the same "**canary in the coal mine**" dynamic at macro scale. Post-2020
  consensus: pure JIT was over-optimized; the swing is to "just-in-case" buffers on critical inputs —
  Goldratt's "elevate vs. demand" tension ([[canon-goldratt-the-goal]]) in the wild.
- **Researched layer** *(2026-06-05)*
  - **Canonical explanation (sourced):** TPS rests on **two pillars over a goal** — *"the goal of lean…
    is to create the highest quality products at the lowest cost with the shortest lead time… These
    goals are upheld by two pillars. The first pillar is just-in-time… The next pillar is quality at the
    source — we never knowingly pass a defective product to our next downstream customer"* (EMS
    Consulting Group). The JIT insight came not from a factory but a supermarket: Ohno *"was struck by
    the way customers could choose exactly what they wanted, when they wanted… With a 'supermarket
    formula,' only enough parts were produced in the first phase to replace what was used in the second"*
    (Bloomberg Originals) — the seed of *kanban*.
  - **Real application (mined):** Toyota's own training video makes "stop the line" concrete: *"if an
    irregularity occurs… the worker presses the call button, then a yellow lamp is displayed… if the
    issue is not resolved within a set distance, the assembly line will stop and the andon lamp will turn
    from yellow to red… the problem is solved even if it means stopping production"* (Toyota Motor
    Corporation). Bloomberg confirms the payoff: as Ohno's cord let *"the whole team work on it, to
    prevent it from happening again… the number of errors began to drop dramatically."*
  - **Where the corpus pushes back on the book:** the r/supplychain threads show the JIT pillar is only
    as strong as the supply network feeding it — buffer-less lean turns a "$150" part into "$1800" the
    instant a carrier or tariff regime shifts (549↑), and macro shocks (Hormuz, Persian-Gulf oil, 408↑)
    propagate with no slack to absorb them. The practitioner swing is explicit: re-introduce
    "just-in-case" inventory on critical, single-sourced inputs even at the cost of textbook leanness.
  - **Sources in corpus:** EMS Consulting Group — "Lean Manufacturing: What is Lean and the Toyota
    Production System?" (youtube.com/watch?v=sUtmosujXVE) · Bloomberg Originals — "How Toyota Changed The
    Way We Make Things" (youtube.com/watch?v=F5vtCRFRAK0) · Toyota Motor Corporation — "The Toyota
    Production System as Taught by Toyota - Episode 01" (youtube.com/watch?v=TUKpxjAftnk) · E-Concepts —
    "13 Pillars of Toyota Production System" (youtube.com/watch?v=pzuUqzUM0YY) · r/supplychain "Shipping
    costs from suppliers in china are exploding. $200 → $1200" (549↑), "The first shortages due to the
    Gulf of Hormuz are beginning to arrive" (240↑), "JP Morgan have mapped out when the last of the
    Persian gulf oil will arrive" (408↑).
- **Links:** [[canon-goldratt-the-goal]] · [[canon-meadows-thinking-in-systems]] ·
  [[canon-walsh-score-takes-care-of-itself]] · [[canon-taleb-antifragile]]

---
### Rep
Pick a process you run. Find one of the seven wastes in it (usually waiting or overprocessing).
Remove it — and notice whether you had inventory hiding the real problem.
