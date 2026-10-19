# Note · 24/5 Trading — how institutions are handling it, and the architecture pattern underneath

> Practitioner / operations note · Companion to [[market-structure-24-5-trading]] · Maps to **Course 06** (Operations), **E-track** (systems, org design) · Written 2026-09-21

- **Source:** SEC — Commissioner Peirce, *Stock Around the Clock*, remarks at the SEC Roundtable on Preparations for 24-Hour Trading (Sept 17, 2026); Exegy — *23x5 Trading: The Operational Reality of No Maintenance Windows*; Adaptive — *Architecting 24/7 capital markets with high-availability sequencer designs*; AWS for Industries — *Cloud Adoption Update for FMI Providers 1H26*; Markets Media — *Cboe's "Follow the Sun" model*; DTCC — *The Shift to 24x5 Trading*; Capco — *Are You Ready for 24x5 in 2026?*; FinanceFeeds / FOW on OCC Ovation.
- **Core claim:** Institutions are splitting into three camps — **rebuild** (the FMIs, on multi-year cloud programs that predate 24/5 but are what make it possible), **squeeze** (broker-dealers and clearing firms compressing a 12-hour batch cycle into ~1 hour), and **opt out** (most of the buy side, hiding behind "selective participation"). The technical crux across all three is the same: **the business date is an implicit global variable in every post-trade system, and 24/5 makes it explicit, multi-valued, and event-driven.** That is a refactor pattern, not a rewrite — and it's the AWS-shaped, repeatable piece.

---

## 1. How institutions are actually handling it (Sept 2026)

| Camp | Who | What they're doing | Tell |
|---|---|---|---|
| **Rebuild** | DTCC, OCC, ASX, Nasdaq, BYMA | Multi-year mainframe → cloud microservices. OCC **Ovation** (single mainframe → microservices, Vermiculus risk engine). DTCC core clearing/settlement/risk to cloud **by 2030**. ASX's new CHESS on AWS: 21M trades/day vs 7M on the old system. Nasdaq migrating its U.S. options markets to AWS one exchange at a time (MRX, GEMX, next one queued). | NSCC delivered 24x5 clearing on June 29, 2026 *because* the modernization was already underway. |
| **Squeeze** | Broker-dealers, clearing firms, custodians, fund admins | Compress "overnight batch processing cycles or critical IT maintenance into a single hour" (Peirce). Shift ledgers, margin/buying power, recon and reporting from end-of-day jobs to rolling incremental processes. Staff a follow-the-sun desk or outsource one. | The complaint at the SEC roundtable was *back-office compression*, not liquidity. |
| **Opt out** | Asset managers, pension/insurance | "Selective participation and robust safeguards"; governance and compliance memos explaining why they *won't* trade overnight. | Peirce's own question — *is choosing not to trade overnight still an acceptable fiduciary decision?* — is the tell that most of the buy side wants the answer to be yes. |
| **Vendors** | Adaptive, Exegy, Capco, ViewTrade, Duco, Broadridge, FIS | Selling readiness assessments, sequencer architectures, streaming recon, follow-the-sun runbooks. | The market for the *fix* is forming faster than the market for the *trading*. |

**Operating-model responses now visible:**
- **Follow-the-sun support** (Cboe explicitly; OCC "evaluating"): regional teams with seamless handoff and full operational context. Exegy's framing: staffing 24/5 is expensive, but "staffing without consistent processes and shared tooling is even more expensive, because it introduces risk without absorbing it."
- **Event-driven workflows replacing batch** (OCC): the day-roll becomes an event, not a cron.
- **Change management inversion**: progressive/blue-green rollout, automated regression, fast rollback with end-to-end observability — "no longer optional."
- **Load profile change**: no single predictable peak; bursts off overnight news and Asia macro; "liquidity pockets that ebb and flow unpredictably."
- **Human factors**: supervision with limited humans overnight, "sleep," social-media rumors hitting a live market at 2am with a skeleton crew.

## 2. The architecture pattern — "business date as a first-class event"

**The diagnostic that finds every problem:** `grep` the codebase for the business date. Every hardcoded `T+1`, every `if hour < 16`, every cron at 16:15, every job named `EOD_*`, every table keyed on `trade_date` populated by `CURRENT_DATE`. Each one is a latent bug under 24/5, because the trade date now rolls at **8:00pm ET**, the protected session runs **9pm–4am**, the band reference is struck at **7:45pm**, and the official close is still **4:00pm**. Four clocks where there used to be one.

**The pattern** (Adaptive's sequencer control-message model, generalized from the matching engine to the *whole* post-trade stack):

```
┌──────────────────────────────────────────────────────────────────────┐
│  SESSION LIFECYCLE SERVICE  (single authoritative emitter)            │
│  events: session.open · session.close · tradeDate.roll@20:00 ·        │
│          bandRef.snapshot@19:45 · clearing.cutoff · weekend.open      │
└──────────────┬───────────────────────────────────────────────────────┘
               │ control messages on the ordered log (not cron)
               ▼
┌──────────────────────────────────────────────────────────────────────┐
│  ORDERED LOG / SPINE   (MSK or Kinesis; partition by symbol/account)  │
│  trades · fills · allocations · lifecycle markers · corporate actions │
└───┬──────────────┬──────────────┬──────────────┬─────────────────────┘
    ▼              ▼              ▼              ▼
 Positions      Cash/Margin    Recon (stream   Reporting / CAT /
 (Flink,        (Flink,        join vs DTCC/   surveillance
  running)       running)       custodian)      (rolling windows)
    │              │              │              │
    └──── every consumer subscribes to lifecycle events; none owns a clock ────┘
```

**The seven decisions that follow from it:**

1. **One clock owner.** A Session Lifecycle Service (EventBridge + Step Functions or a small DynamoDB-backed state machine) is the *only* thing that decides what "today" is. It emits lifecycle events onto the log. Everything downstream is a state machine that consumes them. This is how you kill the implicit global.
2. **The log is the spine; the day-roll is a record in it.** Kinesis or MSK with per-symbol / per-account partitioning, exactly-once semantics on the ledgers. Replay = recovery. Snapshot at marker boundaries; log truncation only at snapshots (Adaptive's asynchronous-snapshot rule: one replica snapshots while the others keep processing — synchronous snapshots cause "systemic jitter").
3. **Reconciliation becomes a streaming join, not a job.** Managed Flink computing running positions and cash; breaks detected as they occur against the DTCC/custodian feed. This is the single highest-value piece — **T0 break detection** — and it's what T+1 already demanded; 24/5 just removes the last excuse.
4. **Cells, not a monolith, because you can't take *the system* down.** AWS cell-based architecture + shuffle sharding: partition by symbol range / clearing account / region. Maintenance = drain a cell. Canary = deploy to the low-volume cell first (Adaptive's "canary by partition" is the same idea). Blast radius becomes a design parameter.
5. **Two versions live at once, always.** Protocol versioning (`protocolId`, `protocolVersion`, `messageType`) with control-message handover; schema changes as expand/contract only — no breaking DDL, ever, because there's no window to run it in. Blue/green on ECS/EKS with connection draining; feature flags; automated rollback as a first-class path.
6. **Test in production, continuously.** You lost the window to test in staging then cut over — so AWS Fault Injection Service game-days become the regression suite. Predictive scaling keyed to the macro/earnings calendar with a *floor* (you cannot cold-start into a BoJ headline).
7. **The weekend is the only irreversible window — enforce it in CI/CD.** Fri 8pm → Sun 8pm ET is the last genuine pause. Deployment guardrails by time-of-week: irreversible operations (data migrations, cutovers) are only allowed then; everything else must be reversible. Policy as code, not a wiki page.

**Plus the org half** (the roundtable said this is as much organizational as technical): runbooks as code (Systems Manager / Incident Manager), trace context that travels with the incident so the Singapore engineer has what the New York engineer had, and an on-call model that treats 2am ET as a *shift*, not an exception.

## 3. Is there a scalable resource here? An honest assessment

**Where the gap actually is.** AWS's own 1H26 FMI cloud-adoption report **does not mention 24x5 or extended hours at all.** The Well-Architected Financial Services Lens is generic. The matching-engine problem (sequencers, RAFT, state-machine replication) is *solved* and owned by specialists — Adaptive, Aeron, LMAX, Vermiculus, Nasdaq's own Eqlipse. Don't compete there. The **post-trade / back-office** problem is the unserved one, and it's the bigger population.

**Who has the pain and no capability.** Not the top five (they have armies). The middle: regional broker-dealers, correspondent clearing firms, fund administrators, RIA/wealth platforms, the OMS/PMS vendors that sell to them — and **non-U.S. brokers wanting to offer U.S. overnight to Asian retail**, which is the actual growth segment (75–80% of overnight flow). Hundreds of entities, identical problem, hard deadline, no in-house streaming/cloud depth.

**Why now is defensible.** Three dated forcing functions: SIP + LULD overnight go live **Dec 6, 2026**; NYSE Arca "late 2026"; Nasdaq H2 2026. The SEC is holding roundtables. Deadline-driven, compliance-adjacent work is the most reliably funded category in financial services.

**The asset, in layers of increasing willingness-to-pay:**

| Layer | What it is | Economics |
|---|---|---|
| **Reference architecture** (public) | The diagram above + the seven decisions, published as a lens/whitepaper | Low WTP; it's the *marketing* for the next two layers. Credibility asset. |
| **24/5 Readiness Assessment** (the wedge) | 2–3 week diagnostic: business-date grep, batch-job inventory, clock-dependency map, blast-radius map, gap report against the five-layer stack in [[market-structure-24-5-trading]] | Cheap, repeatable, fixed-price. Sells the migration. |
| **Migration engagement** | Batch → streaming for recon/positions/cash on the pattern; cell partitioning; deploy-pipeline guardrails | The money. Unglamorous data-model surgery, not greenfield. |
| **Managed service** (the product) | Session Lifecycle Service + continuous recon as a service, sold to the firms that own a recon vendor already and need the *migration path* | Highest leverage, hardest to build; crowded adjacent space (Duco, Gresham, FIS). |

**Breaks when:**
- Overnight volume stays <2% and budgets get cut — then this is a compliance checkbox, not a transformation, and the assessment layer is all that sells.
- Capco/Accenture/Broadridge/FIS and the OMS vendors productize the same thing with distribution you don't have. (They will. Speed and specificity are the only edge.)
- The real blocker at a given client is the mainframe, not the cloud — then the pattern is right but the engagement is a five-year modernization you don't want to own.
- Phase 2 of the LULD plan or a post-incident rule change re-batches the overnight (auctions, mandatory pauses). Then some of the "no window" urgency evaporates.

**Practitioner counterpoint:** the vendors selling readiness (Exegy, Capco, Adaptive) all agree on the *engineering* and all quietly admit the *org* is the harder half — handoffs, runbooks, who's awake. A pattern that ships only the architecture will be judged on the outage that happened at 2:40am on a Tuesday when the runbook assumed a New York engineer. The differentiated version of this offering ships the operating model with the diagram.

- **Links:** [[market-structure-24-5-trading]] · [[canon-goldratt-the-goal]] (the constraint moved to layers 4–5) · [[canon-perrow-normal-accidents]] (removing slack from a coupled system) · [[canon-ohno-toyota-production-system]] (batch → flow, and when *not* to) · [[canon-bezos-shareholder-letters]] (two-way doors — the weekend is the only one-way door left) · [[canon-larson-elegant-puzzle]] (org as a throughput system; follow-the-sun) · [[canon-helmer-7-powers]] (which layer of the asset has a barrier)

---
### Rep
Take one system you know well (or one client's). Run the diagnostic: list every place the business date is *assumed* rather than *received*. Sort into three buckets — (a) would produce a wrong number at 9pm ET, (b) would produce a wrong number at 8pm–9pm ET only (the seam), (c) is fine. Estimate how many are bucket (a). That number is the assessment's headline, and the pitch.

**Sources used (2026-09-21):** [SEC — Peirce, *Stock Around the Clock* (Sept 17, 2026)](https://www.sec.gov/newsroom/speeches-statements/peirce-remarks-sec-roundtable-091726) · [Exegy — 23x5 Trading: no maintenance windows](https://www.exegy.com/23x5-trading/) · [Adaptive — 24/7 sequencer architectures](https://weareadaptive.com/trading-resources/24-7-sequencer-architectures-capital-markets/) · [AWS — FMI cloud adoption update 1H26](https://aws.amazon.com/blogs/industries/financial-market-infrastructure-providers-cloud-adoption-update-for-1h26/) · [Markets Media — Cboe follow-the-sun](https://www.marketsmedia.com/cboes-follow-the-sun-model-will-help-24x5-us-equities-trading/) · [DTCC — The Shift to 24x5 Trading](https://www.dtcc.com/-/media/Files/Downloads/Transformation/theshiftto24x5trading.pdf) · [Capco — Ready for 24x5 in 2026?](https://www.capco.com/intelligence/capco-intelligence/us-equities-extended-trading-hours) · [FinanceFeeds — OCC Ovation](https://financefeeds.com/occ-taps-vermiculus-microservice-based-solution-for-new-platform-ovation/) · [ViewTrade — infrastructure for 24/7 markets](https://www.viewtrade.com/blog/designing-scalable-trading-infrastructure-for-24-7-and-overnight-markets/) · [AWS Well-Architected FSI Lens](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/financial-services-industry-lens/wellarchitected-financial-services-industry-lens.pdf)
