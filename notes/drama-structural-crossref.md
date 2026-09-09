# DRAMA Platform: Structural Cross-Reference

Cross-reference of [sec-filing-intelligence.md](sec-filing-intelligence.md) against the actual DRAMA platform (`~/edgar-ingest`). The first document theorizes why SEC filings work as intelligence infrastructure. This one maps where the platform exploits that structure, where it doesn't, and what the gaps mean.

---

## Architecture Correspondence

The SEC intelligence analysis proposes a three-layer stack: Fact → Assurance → Judgment. The platform implements a three-layer architecture that maps cleanly but not identically:

| Theory Layer | Platform Layer | Implementation | Status |
|---|---|---|---|
| **Fact** (commodity, identical for all) | **Layer 1 + Layer 2** (bronze index + silver XBRL) | 1.18M filings indexed, 122.5M facts landed, 2.58M facts in silver, 100% faithfulness verified | Live on R2 |
| **Assurance** (nothing silently dropped) | **Quarantine + verify.py + golden signals** | Failed records quarantined with reason, faithfulness hard-gate (exit 1), identity soft-checks, golden signal per output | Live |
| **Judgment** (derived intelligence, the product) | **conditions/** directory | Comparability rules (R1-R11), clean financials (754K values), revenue corrections (10.7K), industry bounds (18.9K flags), diligence scanner, delta, sector map | Live (bounds local-only) |

The theory calls Layer 1 a commodity. The platform confirms this: the bronze data is public XBRL, identical for everyone. The theory calls Layer 3 the moat. The platform's conditions/ directory is additive-only and confidence-scored — every judgment traces back through the assurance layer to source facts. This is the provenance chain, implemented as a verified architectural invariant rather than a claimed property.

The one divergence: the theory treats Assurance as a distinct value layer ("most platforms silently drop ambiguous data"). The platform's quarantine-not-drop principle maps to this, but GAP-C (the coverage mart, not yet built) means an unmapped tag still vanishes silently. Assurance is load-bearing but incomplete — the platform can prove faithfulness of what it mapped, but cannot yet prove that it mapped everything.

---

## Consumer Typology vs. Platform Capabilities

The intelligence analysis identifies five consumer archetypes. Here's what the platform can actually deliver for each today, and where it falls short.

### The Compounder — Strong

The platform's strongest alignment. The serial-acquirer scorecard (`scorecard.py`) directly answers "is this growth earned or bought?" — M&A intensity metric, trailing-window analysis, earned/mixed/bought verdict. The three UI lenses (Compounder, Activist, Credit) present the same scorecard data with different emphasis, which is exactly the consumer-typology insight operationalized: same facts, different decision context.

**What's built:** R1 acquisition-masked growth detection. Multi-year cash flow trajectory. Revenue CAGR with acquisition adjustment. Peer comparison within niche. Object surface composing scorecard + snapshot into a finding-led workspace.

**What's missing:** No segment decomposition — can't isolate which business lines are growing organically vs. via acquisition when a company has multiple segments. No valuation data — can answer "is the growth real?" but not "is it priced in?"

### The Activist — Strong

The comparability engine was built for this consumer. R7 (accruals/proof-of-cash), R8 (non-recurring earnings load), R5 (goodwill concentration), R10 (intangibles exceeding equity) are directly the questions an activist or short thesis starts with. Filing delta (`delta.py`) surfaces narrative shifts — added/removed risk factor sentences year-over-year.

**What's built:** All 11 comparability rules with confidence scoring. On-demand filing delta across risk factors, MD&A, business sections. Industry bounds for peer-relative outlier detection. Diligence phrase scanner for going-concern language, material weaknesses, restatements.

**What's missing:** Narrative-quantitative cross-reference (see below — the platform analyzes numbers and narrative separately, but doesn't systematically flag when they contradict each other). No price data means no short-setup signals (overvaluation relative to earnings quality).

### The Acquirer — Strong

The diligence red-flag scanner and niche scorecard were built for pre-data-room assessment. The building-products niche — 31 companies with M&A counts, serial-acquirer scores, capex and buyback patterns — is an acquirer's target-screening tool.

**What's built:** Diligence phrase scanning (11 categories, negation-guarded, confidence-tiered). Leverage capacity assessment (R4, R6). Quarterly investment anomaly detection (de-cumulated from 10-Q YTD). Acquisition market dynamics — who else is buying, at what cadence, at what implied multiples (goodwill/intangible balances).

**What's missing:** No DCF or comparable-company valuation (no price data). No segment-level analysis for synergy assessment. Text corpus is Q1 2025 only — can't scan historical filings for diligence patterns across time.

### The Venture Investor — Partial

This is the weakest consumer alignment. The SEC intelligence analysis argues that incumbents' segment revenue is "the most defensible market-sizing data available." The platform has no segment mapping. Industry bounds provide sector-level benchmarks (what margins look like in building products), but can't decompose a conglomerate into addressable markets.

**What's built:** Industry bounds for sector-level unit-economics benchmarks. Risk factor text search (finding where incumbents mention disruptive threats). Serial-acquirer tracking for M&A market dynamics (predicting exit environments).

**What's missing:** No segment data — the primary market-sizing use case is unserved. Risk factor search is limited to the Q1 2025 text slice. No startup-comparable pipeline (the platform is designed around public filers, not private company benchmarking).

### The Competitor — Moderate

Quarterly investment anomaly detection reveals capex and R&D trends. Filing delta surfaces strategic narrative shifts. Industry bounds position a company against peers. But competitive intelligence often requires the most granular data — segment-level, geography-level, product-level — which the platform doesn't break down.

**What's built:** Quarterly capex/R&D/M&A spending patterns with anomaly detection. Filing delta across all narrative sections. Peer-relative positioning on margins and leverage.

**What's missing:** No segment or geographic breakdowns. No executive-movement tracking (proxy analysis limited to niche scorecard). No supply-chain or customer-concentration analysis beyond the diligence-flag level.

---

## Emergent Properties vs. Platform Exploitation

The intelligence analysis names four emergent properties of the filing system. The platform exploits three well and one poorly.

### Temporal Compulsion — Exploited

`quarterly_investment.py` directly leverages mandatory quarterly cadence: it de-cumulates 10-Q year-to-date figures into discrete quarters and flags statistical anomalies against the company's own trailing history. The comparability engine runs on annual (10-K) data, creating longitudinal trend detection. Filing delta compares consecutive annual filings. The platform treats time series as first-class objects — the "readings" feature in `chat.py` generates analyst-style narrative of CAGR, regime contrast, down years, and record highs from the temporal structure.

### Comprehensive Coverage — Exploited

17,891 CIKs ingested. Industry bounds computed across 30 sectors using the full population (Tukey fences over median/IQR per sector-year, min 8 peers). The platform takes advantage of population-level analysis — these aren't sample statistics. However, GAP-C means coverage is not provably complete at the concept level: if a filer's revenue tag doesn't match the concept map, that filer silently lacks revenue data without any alert.

### Provenance Chain — Architecturally Embodied

This is the platform's strongest structural alignment with the theory. The faithful-source firewall isn't a feature — it's an architectural invariant verified at 100% by `verify.py`. Every Layer 3 judgment traces through the assurance layer to a source XBRL fact. The additive-only principle (conditions/ never mutate silver) means the provenance chain is mechanically enforced, not just promised. The "flag, never fail" principle means every comparability flag carries a confidence score and evidence trail. This is the "check me" intelligence property made concrete.

### Narrative-Quantitative Duality — Underexploited

This is the gap. The theory doc identifies "the gap between narrative and numbers" as the richest intelligence signal — when MD&A tells one story and the cash flow statement tells another. The platform has both capabilities: `delta.py` analyzes narrative, `comparability.py` analyzes numbers. But they operate independently. No module systematically cross-references them.

Example of what's missing: R1 flags acquisition-masked organic decline (revenue grew 1.5% despite $1.9B in acquisition spend). Delta might show that the same filing's MD&A added language about "strong organic demand." These two signals together — quantitative evidence of bought growth plus narrative claiming organic growth — are more informative than either alone. But the platform surfaces them as separate findings that the human analyst must juxtapose.

This is a design opportunity, not a bug. A cross-reference module that matches comparability flags against narrative claims for the same (cik, year) would be a new kind of Layer 3 output — one that no other platform produces because it requires both structured financial analysis AND filing text analysis running against the same entity in the same period.

---

## The Moat Paradox, Applied

The intelligence analysis identifies three moat-eligible layers: extraction infrastructure, judgment framework, and niche authority. Map each to the platform's actual position.

### Extraction Infrastructure — Built, Not a Moat

The bronze-to-silver pipeline, XBRL concept mapping (46 concepts), DuckDB-over-R2, and the faithfulness verification are solid engineering. But they are reproducible. The benchmark report explicitly notes that `edgartools` already ships a free 234-concept standardizer. The pipeline is necessary infrastructure — without it, nothing downstream works. But possession of a working XBRL pipeline is not a durable competitive advantage. The platform invests heavily here (100% faithfulness is overkill for most use cases), which serves reliability but not differentiation.

### Judgment Framework — Built, Differentiated, Unvalidated by Market

The 11 comparability rules, serial-acquirer scorecard, industry bounds, and diligence scanner collectively represent a judgment framework that encodes domain expertise into repeatable analysis. This is genuine differentiation — Bloomberg doesn't run these specific heuristics, and the confidence-scored, evidence-traced format is distinct from sell-side analysis.

But the ARCHITECTURE.md flags the central risk: the premise that this judgment layer is what Bloomberg/FactSet's customers actually pay for "was never confirmed." Their moat might be distribution, terminal lock-in, or licensed data (price feeds, reference data), not the quality of financial-ratio analysis. This is a customer-discovery question, and no customer has been asked.

### Niche Authority — Not Started

The building-products niche (31 companies) is defined as the go-deep target. The DRAMA Score concept — a diagnostic that a specific M&A community adopts as their standard lens — is articulated but unbuilt. No mechanism exists for distribution: no API, no embeddable widget, no content channel, no niche community engagement. The platform is an analyst's private tool, not a product with adoption dynamics.

This is the bottleneck the memory notes flag: "ZERO customer contact = the real bottleneck." The moat paradox resolves only when the judgment framework migrates from private tool to community standard. Everything between here and there is distribution, not engineering.

---

## What the Cross-Reference Reveals

Three structural findings emerge.

**1. The platform is strongest where the theory is most concrete.**

The Compounder and Activist archetypes map to built, tested, confidence-scored capabilities (scorecard, comparability rules, delta). The Venture and Competitor archetypes — where the theory relies on segment data and cross-company strategic inference — have thin coverage. The platform's investment followed the most operationalizable intelligence questions, which is defensible prioritization but leaves the broadest market-sizing and strategic-intelligence use cases unserved.

**2. The narrative-quantitative cross-reference is the highest-value unbuilt capability.**

The theory doc identifies this as the defining property of SEC filings vs. all other intelligence sources. The platform has both analytical engines (narrative and quantitative) running independently. Wiring them together — matching comparability flags against narrative claims for the same filer and period — would produce a signal that is genuinely novel, hard to replicate, and directly actionable for every consumer archetype. It would also exercise both the structured XBRL pipeline and the text corpus simultaneously, which would justify the full text backfill that's currently on hold.

**3. The gap between judgment framework and niche authority is not an engineering problem.**

The platform's engineering is mature: 100% faithfulness, 11 validated rules, confidence scoring, provenance tracing. The gap is that no external decision-maker has used it, validated it, or adopted it. The Cboe analogy from the theory doc makes this precise: the VIX methodology didn't become a moat because it was correct — it became a moat because a community adopted it as their standard. The platform has the methodology. The community adoption is a zero.

---

## Structural Summary

| Dimension | Theory Position | Platform Reality | Gap |
|---|---|---|---|
| Fact layer | Commodity, no moat | Built, 100% faithful, live on R2 | None (over-invested if anything) |
| Assurance layer | Reliability moat | Quarantine + verify, but GAP-C missing | Coverage signal incomplete |
| Judgment layer | The product, the moat | 11 rules, scorecard, bounds, scanner, delta | Narrative-quantitative cross-ref unbuilt |
| Compounder use case | Earned vs. bought | Strong (scorecard, R1, lenses) | No segment data |
| Activist use case | Accounting divergence | Strong (R7-R11, delta, diligence) | No narrative-quantitative cross-ref |
| Acquirer use case | Diligence + capacity | Strong (scanner, R4, quarterly anomaly) | Text limited to Q1 2025 slice |
| Venture use case | Market sizing + disruption | Partial (bounds, risk search) | No segment mapping |
| Competitor use case | Investment + exposure | Moderate (quarterly anomaly, delta) | No segment/geography breakdown |
| Temporal compulsion | Observe on the calendar's schedule | Exploited (quarterly de-cumulation, readings) | — |
| Comprehensive coverage | Population, not sample | Exploited (17.9K CIKs, 30 sectors) | GAP-C: silent unmapped CIKs |
| Provenance chain | "Check me" intelligence | Architecturally embodied (100% faithfulness) | — |
| Narrative-quantitative duality | The richest signal | Underexploited (separate engines, no cross-ref) | Highest-value unbuilt module |
| Extraction infrastructure | Necessary, not sufficient | Built, solid, reproducible | Not a moat (edgartools exists) |
| Judgment framework | Differentiated, the product | Built, differentiated, market-unvalidated | No customer has been asked |
| Niche authority | Hardest, most durable moat | Articulated (DRAMA Score), unbuilt | ZERO distribution, ZERO community |
