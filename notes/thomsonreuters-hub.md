# Note · Thomson Reuters hub — the company that owned Tradeweb sold the trading floor, gave most of the money back, and bet the rest on "trust" as the moat in professional AI

> Hub / company-study note · Maps to **E2** (Capital Allocation), **E3** (M&A, Deals & Restructuring), **E5** (Transformation), **E10** (Digital & AI Transformation), **Course 02** (Corporate Finance & Valuation), **Course 04** (Competitive Strategy), **E4** (Corporate Governance), **E1** (Leading at Scale) · Written 2026-10-25 · Entry point for the seven Thomson Reuters notes

- **Source:**
  - Thomson Reuters press releases, **2019-01 → 2026-10**. All **527** URLs in the thomsonreuters.com sitemap for the period, plus the Q3 2025 results release from the IR site, which the sitemap omits. Index: `_ingest/raw/thomsonreuters/index.tsv`, 533 rows.
  - **293 substantive items** were read in full (`articles.jsonl`).
  - IR documents fetched through the browser, because the IR site blocks scripts: the **2019 AGM transcript**, the **2021 Investor Day transcript** (~29k words with analyst Q&A), the 2021 CEO slides and the Casetext call slides.
  - Excluded, each with a reason in the index: 240 routine items (date/webcast notices, AGM and filing notices, awards, minor product and partnership items).
  - Not read: Reuters News articles (by design), annual reports, earnings-call transcripts, the 2024 Investor Day (no transcript; the deck is image-only).
  - Reading digest: `_ingest/raw/thomsonreuters/DIGEST.md`.
- **Core claim:** TR in 2019–2026 is a **capital-allocation and transformation case**, not a market-structure peer. Its market-structure relevance is mostly historical:
  - It owned Tradeweb from 2004 through Financial & Risk (F&R).
  - It sold 55% of F&R to Blackstone in 2018. F&R became Refinitiv and held ~54% of Tradeweb at the 2019 IPO.
  - It swapped its 45% for LSEG shares in 2021 and sold them by **May 2024**.
  - What remains is **Reuters News, distributed to financial professionals only through LSEG until 2048**.

  The money (~$17B in 2018, ≈$8.3B in 2021–24) mostly went back to shareholders. The rest bought tax software and legal AI at ~8–10× revenue. Meanwhile an outside CEO ran a pre-registered **Change Program** that hit its 2023 targets. That operating-company platform let TR ship generative AI fast, starting with **Casetext** in 2023. By 2026 it had **one million CoCounsel users**, the **"fiduciary-grade AI"** standard and its own **$40M "Thomson" LLM**. The open question is whether "trust", the word carried from the 1941 Reuters Trust Principles into the AI pitch, is a moat against frontier labs that both supply TR's models and could sell around it.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[thomsonreuters-refinitiv-lseg-exit]] | Sold the trading floor in three steps and kept one wire into it (Reuters via LSEG to 2048) | Lineage to Tradeweb and LSEG; every LSEG tranche and price; realized ≈$8.3B vs a $9.8B mark; the news contract |
| [[thomsonreuters-capital-allocation]] | A controlled company that returned most of the windfall, bought revenue at ~8–10×, and now funds returns with debt | Sources and uses; buyback prices $49 → $166; deal prices; the KKR print JV; Woodbridge's float cap; leverage 0.4× → 0.9× |
| [[thomsonreuters-change-program]] | Hard targets, candid diagnosis, mostly hit; capex the chosen miss | 2021 design, quarterly progress, scorecard, launch-day quotes |
| [[thomsonreuters-ai-strategy]] | Rents the labs' models, sells content and editors as the trust layer, built a $40M model as a hedge | 2019–2026 AI chronology; the moat claim evolving; economics; what the claims don't prove |
| [[thomsonreuters-people]] | Family board → outside CEO → outside change team → product and AI voices | Org chart over time; profiles with dated quotes; how views shifted |
| [[thomsonreuters-outside-voices]] | Counterparties praise what they buy; AI suppliers praise TR's content; doubt comes only from analysts and academics | Stakeholder map; 2021 analyst Q&A; missing competitors |
| [[thomsonreuters-mission-forces]] | "Trust" survived every identity rewrite; the danger is good-enough AI from TR's own suppliers | Mission statements by date; tailwinds T1–T8, headwinds H1–H10; crisis tests; 2030 scenarios |

**Suggested order:** refinitiv-lseg-exit (the Tradeweb link) → capital-allocation → change-program → ai-strategy → people → mission-forces → outside-voices.

## 2. Timeline

| Date | Event | Why it matters |
|---|---|---|
| 2004–05 (context) | Thomson acquires Tradeweb ([[tradeweb-hub]]) | Media and data parent owns a venue |
| 2008 (context) | Thomson + Reuters merge | The F&R terminal business vs. Bloomberg |
| **Oct 2018** | 55% of F&R to Blackstone → **Refinitiv**; ~$17B cash; $10B returned; Reuters 30-year news contract | The exit from markets begins |
| Apr 2019 (context) | Tradeweb IPO; Refinitiv keeps ~54% | Smith later credits "the IPO of Tradeweb" for Refinitiv's value creation |
| **Aug 2019** | LSEG agrees to buy Refinitiv, ~$27B EV, all in shares; TR → ~15% of LSEG | Market-infrastructure consolidation, seen from the seller's side |
| **Mar 2020** | **Steve Hasker** CEO; Mike Eastwood CFO | Outside operator |
| 2020 | COVID: guidance cut, revolver drawn; Big 3 still +4% | Subscription content proves resilient |
| **Jan 2021** | LSEG deal closes: 82.5M LSEG shares ≈ $9.8B; lock-ups to 2025; Reuters contract to 2048 | TR becomes a financial investor in LSEG |
| **Feb–Mar 2021** | **Change Program** ($500–600M) + Investor Day: 2023 targets; "$15 billion" capacity; "rigor" | Holding company → operating company; content → content-driven technology company |
| Dec 2022 | Change Program completed ($540M run-rate savings); Westlaw Precision (Sep); SurePrep ($500M) | Platform ready months before ChatGPT |
| **2023** | LSEG sales of ~$5.5B (Microsoft + three placements); **$2.2B return of capital**; **Casetext $650M**; Elite to TPG; GenAI strategy ($100M+ a year) | The windfall gets spent, mostly returned |
| 2024 | **Pagero** (~$800M) after a bidding war; brand refresh; CoCounsel 2.0 multi-model; Safe Sign, Materia; **LSEG exit (May 15)**; FindLaw sold | Clean exit from markets; AI platform |
| 2025 | SafeSend ($600M); Nasdaq listing; agentic AI; $200M+ a year on AI; organic 7% | Growth at a decade high |
| **2026** | 1M CoCounsel users; $1.2B returns (debt-funded in substance); CFO → Bischoping; Anthropic SDK + MCP; **"Fiduciary-Grade AI"**; KKR print JV (Oct 1); **Thomson LLM ($40M)**; Q3 2026 results due Nov 3 | Trust as product; own model as a hedge |

## 3. Five patterns across the notes

1. **Sell the volatile, keep the recurring.** Markets (2018–24), Spain (2021), Elite (2023), FindLaw (2024) and Print (2026) all left. Each sale raised the share of ~90%-retention subscription revenue (Big 3: ~80% → 83–85%). See [[thomsonreuters-capital-allocation]] and [[thomsonreuters-refinitiv-lseg-exit]].
2. **Windfalls go back pro-rata.** A family controller with a float cap means big returns take the form of **return of capital plus share consolidation** (2018, 2023, 2026), not open-market buybacks. Acquisitions stay small: the largest is ~$800M.
3. **Candor buys credibility, once.** The 2021 launch admitted below-average NPS and being "late to the game". That credibility carried the Change Program. By 2026 the only admitted weakness is Hron's "table stakes". See [[thomsonreuters-change-program]] and [[thomsonreuters-people]].
4. **The moat claim narrows as the technology widens.** Data (2021) → content plus talent plus distribution (2023) → agentic workflow (2025) → verification and liability (2026) → owning the model (Aug 2026). Each step answers the same unnamed threat. See [[thomsonreuters-ai-strategy]].
5. **Self-graded scorecards.** Run-rate savings, one million users, "on par with the latest frontier models", "fiduciary-grade" and the adoption surveys are all TR's own rulers. That is the same problem as the [[tradeweb-hub]] pattern 4. The independent checks in the corpus are a handful of analyst questions (2021) and academic testers TR selected.

## 4. Links to the other company studies

- **Tradeweb:** ownership lineage (Thomson → F&R → Refinitiv → LSEG). Tradeweb's IPO value helped fund TR's pivot. Reuters news sits in the same LSEG Workspace channel as Tradeweb data and Ai-Price ([[tradeweb-ai-price]], [[tradeweb-strategy-financials]]).
- **LSEG** ([[lseg-hub]]): the buyer of Refinitiv, TR's exclusive Reuters distributor to finance, and a buyer of its own shares from TR (2023–24).
- **Bloomberg** ([[bloomberg-hub]]): the terminal rival the F&R business faced. Bloomberg Law was named as a Practical Law challenger (2021).
- **S&P Global** ([[spglobal-hub]]): a contrasting information-services path. It kept and bought market data and indices while TR exited them.
- **Goldman, JPMorgan, BlackRock** ([[goldman-hub]], [[jpmc-hub]], [[blackrock-hub]]): no direct link in the TR corpus beyond TR's legal and tax customers and the analysts at the 2021 Investor Day (JPMorgan's Steinerman).

## 5. Cross-note open questions

1. **CoCounsel economics:** revenue, ARPU and gross margin after model costs ([[thomsonreuters-ai-strategy]] §8).
2. **Seat-based pricing vs. fewer junior lawyers:** the inferred H3 in [[thomsonreuters-mission-forces]].
3. **Deal grading:** post-close revenue of Casetext, Pagero and SafeSend ([[thomsonreuters-capital-allocation]] §10).
4. **The Reuters–LSEG contract:** escalator, minimums, exit rights before 2048 ([[thomsonreuters-refinitiv-lseg-exit]] §9).
5. **Q3 2026 results (Nov 3 2026):** the first quarter with Print as a discontinued operation. Is ~8% organic real at ~35–36% margin?

**Links:** [[thomsonreuters-refinitiv-lseg-exit]] · [[thomsonreuters-capital-allocation]] · [[thomsonreuters-change-program]] · [[thomsonreuters-ai-strategy]] · [[thomsonreuters-people]] · [[thomsonreuters-outside-voices]] · [[thomsonreuters-mission-forces]] · [[tradeweb-hub]] · [[tradeweb-strategy-financials]] · [[tradeweb-ai-price]] · [[lseg-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[ice-hub]] · [[marketaxess-hub]] · [[goldman-hub]] · [[jpmc-hub]] · [[blackrock-hub]] · [[wss-capital-markets-ma]] · [[wss-ai-economics]] · [[canon-rumelt-good-strategy]] · [[canon-christensen-innovators-dilemma]] · [[canon-helmer-7-powers]]

---
### Rep
Write a one-page **memo to a TR board member** on whether TR should make a $3B+ AI acquisition in 2027. Use only numbers from these notes.
1. **Funding:** state the capacity. Leverage was 0.9× in mid-2026 and TR's 2020 target was 2.5×. FCF is ~$2.1B (2026 guide). Dividends cost ~$1.0B a year ([[thomsonreuters-capital-allocation]]).
2. **Strategic case:** name the threat in one sentence, using H1–H3 in [[thomsonreuters-mission-forces]].
3. **Precedent:** compare the price with Casetext ($650M) and with the $40M Thomson model ([[thomsonreuters-ai-strategy]]).
4. **Governance:** state what Woodbridge's ~66–70% stake implies for an equity-funded deal.
5. **Decision:** recommend yes or no, and name the one disclosure you would demand first.

**Corpus refresh:**
- thomsonreuters.com press pages download fine with `curl` and a browser user agent. Use `/en/sitemap.xml` as the index.
- ir.thomsonreuters.com returns 403 to scripts. Open it in the browser and use same-origin `fetch()`, which returns PDFs as base64 and release text.
- Rebuild with the scripts noted in `_ingest/raw/thomsonreuters/DIGEST.md` §1. The Q3 2026 results release (Nov 3) is the next item to add.
