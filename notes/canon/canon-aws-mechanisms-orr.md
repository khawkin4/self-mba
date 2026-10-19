# Note · AWS — *Building Mechanisms & the Operational Readiness Review*

> Canon · Cluster: Org Design & Mechanisms · Maps to **E11** (Personal Operating System), **E5**
> (Transformation), **Course 06** (Operations), **E1** (Leading at Scale)
>
> **Primary-source method note, not a book.** The cluster already holds the *assertion* that
> mechanisms beat intentions ([[canon-bezos-shareholder-letters]]) and a *goal-setting* tool
> ([[canon-doerr-measure-what-matters]]). Neither tells you how to build one. This note is the
> construction method, taken from the only place AWS publishes it in full.

- **Source:** AWS Well-Architected, *Building mechanisms* + *The ORR mechanism* (tool / adoption /
  inspection / iteration / Appendix A) · AWS Enterprise Strategy, *Strategy is a winding road;
  mechanisms keep you on track* · AWS Prescriptive Guidance, *Theme 8: Implement mechanisms for manual
  processes* · *Elements of Amazon's Day 1 Culture* (Daniel Slater, AWS, 2023) · Amazon Science, *How
  mechanism design theory helps optimize Amazon vendor collaboration*
- **Core claim:** A mechanism is not a process or a policy. Verbatim: *"A mechanism is a complete
  process where you create a **tool**, drive **adoption** of the tool, and **inspect** the results in
  order to make course corrections… It takes controllable **inputs** and transforms them into ongoing
  **outputs** to address a recurring business challenge."* Drop any one of the three legs and what you
  have is a good intention with paperwork.

- **Framework — the seven steps, as AWS actually built the ORR:**
  1. **Work backwards from the challenge** and state the outputs as *countable* results. AWS wanted
     availability, so it named three: incidents that are **fewer, shorter, smaller**. Not a vision
     statement — three things you can count, or you cannot inspect later.
  2. **Name the controllable inputs.** For the ORR, *"the design and operations of those services are
     the inputs."* Skipping this step is the usual reason a mechanism never moves anything.
  3. **Build the smallest tool.** The ORR's tool is a *checklist of questions* — each one a question, a
     paragraph of guidance, and answers carrying a risk rating (*"Do any of your hosts pin
     certificates?"* → ☐ Yes | High Risk, ☐ No | No Risk). The web service came years later.
  4. **Source the content from your own failures.** Appendix A walks a real incident (a manual IAM
     change never written back into the CloudFormation template) into one checklist question. A mature
     mechanism is a compiled history of your own outages.
  5. **Get adoption by embedding in a lifecycle that already exists.** Despite the name, the ORR is not
     a pre-launch gate — it is *"built into the entire Software Development Lifecycle."* New gates get
     routed around.
  6. **Inspect at three altitudes.** *Cadence*: a weekly ops metrics meeting up to SVP level, where one
     inspected number is when a team last ran an ORR and how many action items are open. *Per instance*:
     a written narrative reviewed with leadership; high-criticality findings escalate into a go / no-go.
     *Meta*: the correction-of-error template asks *"When was your last ORR performed?"* and *"Would any
     ORR recommendations have reduced or avoided the impact of this event?"* — every failure audits the
     mechanism meant to prevent it.
  7. **Iterate, with a standing owner.** *"It's unlikely that a mechanism will operate as designed from
     day one."* A specialist community ("Operational Champions") both challenges answers during reviews
     and curates the question list — checking each question asks the right thing and that its result can
     be measured.

- **Second framework — mechanism vs. guardrail:** a guardrail is a wall that engages only in an
  emergency; a mechanism is a slope that re-centres you continuously. The image is a train wheel: the
  flange touches the rail only in a crisis, while the sloped tread quietly re-centres the train on
  every rotation. **Design the slope.** The cleanest example is a cloud migration run with *no
  deadline*: remaining on-premises costs were allocated across whatever applications stayed, so each
  team's bill rose as its neighbours left. Nobody was ordered to migrate; migrating became cheaper.

- **Third framework — when incentives are in play** (Amazon Science): if the mechanism spans parties
  with private information, you need **incentive compatibility** — truthful reporting must be each
  party's best strategy *"regardless of what the other side does"* — and **information privacy**: the
  vendor *"never reveals its cost structure, only its responses to iterative queries."* The transferable
  moves are: price the deviation and charge it to whoever causes it; iterate proposals instead of
  demanding disclosure; **offer a menu, not a mandate**.

- **Applies when:** the problem **recurs**, you have a countable output, and the behaviour you want
  currently depends on someone remembering. Also the diagnostic use: given anything called a process,
  name its tool, its adoption route, and its inspection — the missing leg is the answer.

- **Breaks when:**
  - **The problem is one-off.** A mechanism on a non-recurring problem is pure overhead; that is a
    project. AWS is explicit that the cyclic form *"is best suited for solving recurring problems."*
  - **Inspection has no gravity.** The guide's own warning: *"you will need to create an inspection
    process that has the gravity to drive both cultural change and adoption of the mechanism's tool."*
    Without a forum senior people already attend, steps 1–5 decay into paperwork. Theme 8 makes the same
    point from the other side, naming executive sponsorship and named owners as prerequisites.
  - **The process becomes the thing.** Bezos, 2016: *"You stop looking at outcomes and just make sure
    you're doing the process right… do we own the process or does the process own us?"* This is the
    mechanism's own Day-2 failure, and the meta-inspection question in step 6 is the only defence in the
    material.
  - **Aggregate reporting hides the tail.** The Day 1 whitepaper: average growth *"may mask underlying
    trends and drivers that affect a meaningful number of customers."* A single contradicting anecdote is
    data about the tail. Pairs with [[canon-tufte-visual-display]] and
    [[canon-kahneman-thinking-fast-and-slow]] on what a summary statistic destroys.
  - **The metric is self-reported by someone it judges.** Then you have built a machine that rewards
    misreporting — see the incentive-compatibility framework above.

- **Practitioner counterpoint:** *(not yet mined from the Reddit / YouTube corpus — run
  `python3 _ingest/pull.py` before claiming an outside practitioner read.)* Two counterpoints are
  available honestly without it. First, the mined corpus already in
  [[canon-bezos-shareholder-letters]] shows the *dissent* mechanism is the one that reliably rots:
  r/ExperiencedDevs *"I'm giving up; becoming a yes man"* (1,668↑) and r/managers *"the 'silent
  resignation' nobody notices"* (9,401↑) document Day-2 stasis arriving not from bad mechanisms but from
  **misaligned rewards underneath good ones**. Second, and more usefully, **this repository is itself a
  failed-mechanism case study**: `acumen/` shipped a complete tool on 2026-06-06 — six-dimension rubric,
  red-team protocol, memo spec, pass thresholds — and produced zero scored reps in sixteen weeks,
  because nothing cost anything when a week was skipped. `learn/VALIDATION.md`, which has all three
  legs, produced five documented turns of improvement in the same period. Same author, same repo; the
  difference is adoption and inspection. Written up in `acumen/MECHANISM.md`.

- **Shelf gap (deliberate, do not fake it):** Bryar & Carr's *Working Backwards* is the book-length
  treatment of this material and the source of the PR/FAQ mechanism. It is cited *inside*
  [[canon-bezos-shareholder-letters]] but has no note of its own. It should get one — from an actual
  read, not from summaries.

- **Links:** [[canon-bezos-shareholder-letters]] · [[canon-doerr-measure-what-matters]] ·
  [[canon-4dx-four-disciplines-execution]] (lead measures = controllable inputs) ·
  [[canon-walsh-score-takes-care-of-itself]] (the standard of performance is the input; results lag) ·
  [[canon-grove-high-output-management]] (indicator pairing, leading indicators) ·
  [[canon-goldratt-the-goal]] (build the mechanism at the constraint, nowhere else) ·
  [[canon-meadows-leverage-points]] (inspection is a feedback loop; which loop you add is the leverage
  choice) · [[canon-thaler-sunstein-nudge]] (the slope, not the wall — defaults over mandates) ·
  [[canon-jensen-meckling-agency-theory]] (why self-reported metrics fail) ·
  [[canon-clear-atomic-habits]] (the one-person version: systems over willpower)

---
### Rep
Take one thing you call a process. Write down its tool, who actually adopts it, and who inspects the
result — with a date for the last inspection. Whichever of the three you cannot fill in is why it isn't
working. Then add the meta-question to whatever template records your failures: *would this mechanism
have prevented the last one?*
