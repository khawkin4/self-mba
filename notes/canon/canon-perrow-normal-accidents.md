# Note · Perrow — *Normal Accidents*

> Canon · Cluster: Systems Thinking & Complexity · Maps to **Course 06** (Operations), **E6** (Crisis Leadership)

- **Source:** Charles Perrow, *Normal Accidents* (1984)
- **Core claim:** Some systems are **both tightly coupled and interactively complex** — and in those
  systems, serious accidents aren't anomalies, they're **inevitable** ("normal"). You can't engineer
  them away.
- **Framework:**
  - **Tight coupling** — events propagate fast with little slack; no time to intervene.
  - **Interactive complexity** — components interact in unexpected, non-linear ways the designers
    didn't foresee.
  - When a system has **both**, multiple small failures combine in ways no operator can anticipate →
    catastrophe (nuclear plants, financial markets, air traffic, chemical plants).
  - **The fork:** you can't safely maintain *both* tight coupling and high complexity. To reduce
    accidents you must **reduce coupling** (add buffers, slack, redundancy) *or* **reduce complexity**
    (simplify interactions). Adding more automation/safety can *increase* complexity and backfire.
- **Applies when:** assessing systemic/operational risk in complex, fast, interdependent systems —
  and questioning whether a "safety" feature actually adds complexity.
- **Breaks when:** Perrow is **near-fatalistic** ("accidents are inevitable, stop trying"), and the
  **High Reliability Organization** school (aircraft carriers, nuclear navy) shows some complex
  tightly-coupled systems achieve remarkable safety through culture, redundancy, and "stop the line"
  ([[canon-ohno-toyota-production-system]]). The truth is contested: structure makes accidents
  *likely*, not *certain*. Classifying real systems as "tightly coupled / complex" is also fuzzier
  than the 2×2 suggests.
- **Practitioner counterpoint:** (fill via `research` → r/sysadmin, r/devops, SRE threads) — the
  living version is **complex systems failure** (Cook's "How Complex Systems Fail"): incidents are
  multiple latent faults aligning. The lesson SREs take: **add slack/buffers and reduce coupling**;
  more dashboards (complexity) can make it worse. Taleb's fragility is the risk cousin
  ([[canon-taleb-black-swan]]).
- **Links:** [[canon-taleb-black-swan]] · [[canon-sterman-business-dynamics]] ·
  [[canon-jervis-system-effects]] · [[canon-ohno-toyota-production-system]]

---
### Rep
Take one system you depend on. Is it **tightly coupled** (no slack)? **Interactively complex**
(surprising interactions)? If both, add a buffer or simplify one interaction — don't just add a
monitor.
