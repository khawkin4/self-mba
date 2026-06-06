# Note · Jensen & Meckling — *Theory of the Firm (Agency Theory)*

> Canon · Cluster: Economics & Incentive Design · Maps to **Course 03** (Micro & Strategy Foundations), **E4** (Governance & The Board)

- **Source:** Michael Jensen & William Meckling, *Theory of the Firm: Managerial Behavior, Agency
  Costs and Ownership Structure* (1976)
- **Core claim:** Whenever an **agent acts on behalf of a principal**, their interests diverge — and
  the gap between what the principal wants and what the agent actually does is the **agency cost.**
- **Framework:**
  - **Principal–agent problem** — employees don't automatically optimize for shareholders; managers
    don't for owners; contractors don't for clients. Misaligned incentives + asymmetric information.
  - **Agency costs = monitoring costs + bonding costs + residual loss.**
  - **Three solutions:**
    - **Monitoring** — oversight, audits, boards, reporting.
    - **Bonding** — the agent posts collateral/reputation (skin in the game).
    - **Incentive alignment** — stock options, performance pay, ownership.
  - Every principal-agent problem is at root an **incentive-design** problem.
- **Applies when:** designing compensation, equity, governance, vendor contracts, or any delegation —
  and reading a proxy statement (DEF 14A exec comp) critically.
- **Breaks when:** the cure can be **worse than the disease** — stock-option alignment drove
  short-termism, earnings management, and excessive risk-taking (the 2000s/2008 incentive disasters);
  Goodhart strikes again as agents **game the metric** they're paid on
  ([[canon-doerr-measure-what-matters]]). It also models humans as **purely self-interested**,
  underweighting stewardship, mission, and intrinsic motivation (and over-monitoring signals distrust
  that *reduces* effort — Ariely's norms, [[canon-ariely-predictably-irrational]]). Powerful lens,
  dangerous if taken as the *whole* of human motivation.
- **Practitioner counterpoint:** *(researched 2026-06-05 — r/AskEconomics + agency-theory transcript corpus)*
  The theory's blade is sharpest on **comp structure**: Business School 101's professor walkthrough
  names the exact mechanism the book warns about — *"managers have less to lose because salaries are
  constant and stock option values rise in response to increased volatility,"* so option-heavy pay can
  *manufacture* the risk-taking shareholders fear rather than cure it. The corpus's live debate also
  surfaces the **public-sector variant**: a top r/AskEconomics thread, "**Why can the US government
  successfully run a massive grocery chain for the military (commissaries), but municipal-run grocery
  stores for the public often fail?**" (1,293↑), is at root an argument about *whose* incentives the
  agent (a manager, an agency) is actually answering to. The team-production cousin is Alchian &
  Demsetz ([[canon-alchian-demsetz-firm]]); Bezos's "mechanisms" are alignment by design
  ([[canon-bezos-shareholder-letters]]).
- **Researched layer** *(2026-06-05)*
  - **Canonical explanation (sourced):** Marginal Revolution University reduces the principal–agent
    problem to its bones with the mechanic example — *"you are the principal and the mechanic is your
    agent… he can lie to charge more"* — and ties it to the deeper cost the book emphasizes:
    *"the bigger problem is that the potential for ripoff means that a transaction may be less likely
    to occur in the first place"* (MRU, "What Is the Principal-Agent Problem?"). Agency cost isn't
    just the rip-off; it's the **trade that never happens** because the principal can't trust the
    agent. Ashley Hodgson sharpens the key insight that **the role isn't fixed** — *"it's not that any
    one role is inherently principal inherently agent… it's just who's trying to incentivize who"*
    (voter→representative, manager→worker, coach→athlete).
  - **Real application (mined):** Business School 101 grounds the theory in two real failures —
    **Enron** (management *"hid the losses by misrepresenting them through tricky accounting"* as
    shares fell *"from over 90 to under one dollar"*) and **Bernie Madoff** (*"agency theory claims
    that the lack of oversight and incentive alignment greatly contribute to these problems"*,
    ~$65B lost). Its remedy list maps one-to-one onto Jensen–Meckling's monitoring/bonding/alignment:
    **contracts, restrictions, evaluations, bonuses, transparency.**
  - **Where the corpus pushes back on the book:** the same transcript flags that the standard fix —
    **stock options** — can *create* the misalignment it claims to solve: option value *"rise[s] in
    response to increased volatility which is embedded with risk,"* so the cure feeds short-termism
    (the note's "cure worse than the disease"). And the adjacent lemons material (Akerlof) reframes
    the root cause as **asymmetric information**, not mere greed — markets already evolve private fixes
    (*"inspections, CARFAX reports, and certified pre-owned programs,"* MRU) before any board or
    contract intervenes, which under-cuts a purely monitoring-heavy reading.
  - **Sources in corpus:** Marginal Revolution University — "What Is the Principal-Agent Problem?"
    (youtube.com/watch?v=kd2r3ARB2tk) · Ashley Hodgson — "The Principal-Agent Problem"
    (youtube.com/watch?v=WJ7RDrMx5gM) · Business School 101 — "Agency Theory (With Real World
    Examples)" (youtube.com/watch?v=wdnlvq_sOD4) · Marginal Revolution University — "Asymmetric
    Information and Used Cars" (youtube.com/watch?v=sXPXpJ5vMnU) · r/AskEconomics "Why can the US
    government successfully run a massive grocery chain for the military… but municipal-run grocery
    stores for the public often fail?" (1,293↑).
- **Links:** [[canon-alchian-demsetz-firm]] · [[canon-akerlof-market-for-lemons]] ·
  [[canon-munger-poor-charlies-almanack]] · [[canon-bezos-shareholder-letters]] ·
  [[canon-doerr-measure-what-matters]]

---
### Rep
Pick one delegation or comp arrangement you own. Where do the agent's incentives **diverge** from
yours? Is the lever monitoring, bonding (skin in the game), or alignment — and is it *gameable*?
Pressure-test on a real DEF 14A: `edgar.py filings <TICKER> --form "DEF 14A"`.
