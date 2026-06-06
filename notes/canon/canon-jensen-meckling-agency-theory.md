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
- **Practitioner counterpoint:** (fill via `research` → r/SecurityAnalysis, r/FinancialCareers) —
  investors read proxies through this lens: **is management's comp aligned with long-term value, or
  with gaming a metric?** The team-production cousin is Alchian & Demsetz
  ([[canon-alchian-demsetz-firm]]); Bezos's "mechanisms" are alignment by design
  ([[canon-bezos-shareholder-letters]]).
- **Links:** [[canon-alchian-demsetz-firm]] · [[canon-akerlof-market-for-lemons]] ·
  [[canon-munger-poor-charlies-almanack]] · [[canon-bezos-shareholder-letters]] ·
  [[canon-doerr-measure-what-matters]]

---
### Rep
Pick one delegation or comp arrangement you own. Where do the agent's incentives **diverge** from
yours? Is the lever monitoring, bonding (skin in the game), or alignment — and is it *gameable*?
Pressure-test on a real DEF 14A: `edgar.py filings <TICKER> --form "DEF 14A"`.
