# Note · LSEG hub — a European exchange group that bought its way into data, then spent five years proving the purchase while its best growth came from things it does not fully own (Tradeweb) or cannot control (volatility)

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy), **Course 02** (Corporate Finance & Valuation), **Course 03** (Microeconomics — clearing incentives), **Course 07** (Data, Analytics & Decision-Making), **Course 11** (Global Strategy & Macro), **E2** (Capital Allocation), **E3** (M&A), **E4** (Governance), **E8** (Investor Relations), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Entry point for the eleven LSEG notes

- **Source:** the LSEG corpus at `_ingest/raw/lseg/`.
  - **Index** (`index.tsv`): 1,027 items.
  - **Fetched** (`articles.jsonl`): 804 items, about 8.9M characters:
    - **Press releases:** the full lseg.com archive from 2019 (887 items; the sitemap and the site search agree). This includes Refinitiv, FTSE Russell and LCH sub-feeds.
    - **42 call and event transcripts**, Jul 2021 → Oct 2026.
    - **Annual reports 2019–2025**, filtered to the strategic report plus principal risks.
    - **35 *New at LSEG* posts.**
  - **Excluded:** 223 items (167 routine index reviews, investor-site shells, single-issuer listings, AGM vote results).
  - **Digest:** `_ingest/raw/lseg/DIGEST.md`.
  - **Caveats:** there are no transcripts before Jul 2021. Everything is company-published.
- **Core claim:** In 2019 LSEG paid ~US$27bn in shares for Refinitiv. It turned an exchange, index and clearing group (£1.9bn revenue) into a ~£9bn "financial markets infrastructure and data provider." The deal worked on its own terms: synergies beat targets, leverage fell a year early, and the sellers were bought out. It did not lift the core data business above ~5% growth.
  - **Where growth came from.** Mostly three places: Tradeweb (majority-owned, never in the synergy case), LCH's SwapClear (a customer-mutualised utility whose economics LSEG bought back in 2025), and FTSE Russell (riding passive and gatekeeping the WGBI).
  - **2025–26.** The AI narrative de-rated the stock. Management answered with "LSEG Everywhere" (licensed data inside every LLM), record buybacks (~10% of market cap a year), and Octus, the first large deal since Refinitiv.
  - **Constant underneath.** One CEO, one Chair, and one word: *open*.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[lseg-refinitiv-deal]] | The $27bn all-share bet beat every synergy target and still did not change the growth rate of what it bought | Deal terms, HKEX counter-bid, Borsa remedy, synergy scorecard, the 37% seller overhang |
| [[lseg-tradeweb-control]] | Owner, distributor, benchmark administrator and index rule-setter at once | 50.9% economic / 89.9% voting, the data licence, Tradeweb FTSE closing prices in WGBI, interlocks, conflicts |
| [[lseg-ai-everywhere]] | From Workspace-in-Teams to the licensed data layer for other people's agents, before the money shows up | Microsoft 2022 terms and delays, MCP/LLM partnerships, the 90% claim, AI monetisation |
| [[lseg-workspace-data]] | Five division heads, a ~30% price discount, Eikon sunset done, Workflows still ~3% | Workspace vs Bloomberg, LDAs, HSBC/Barclays displacements, ASV's retirement |
| [[lseg-post-trade-clearing]] | LSEG keeps buying back the clearing economics it shared with its bank members | SwapClear >90%, the 2025 PTS deal (£1.15bn), Euronext's exit, EU equivalence |
| [[lseg-ftse-russell-indices]] | The #3 index provider whose real power is gatekeeping WGBI membership and pricing | Country classification (China, Korea, India), Tradeweb price switch, mandate loss, ESG fade |
| [[lseg-capital-allocation]] | From *why no buyback?* to ~10% of market cap a year, then a $3.5bn debt-funded deal | Leverage bands, directed buybacks, Octus maths |
| [[lseg-digital-markets]] | A shrinking UK listings franchise answered with private markets, 24/5 and tokenisation, with no revenue yet | PISCES, DMI, DiSH, DSD, LSE 24, xStocks |
| [[lseg-people]] | One CEO and Chair for seven years, a revolving door everywhere else | Org chart, profiles with dated quotes, where views shifted |
| [[lseg-outside-voices]] | Analysts are the only real skeptics; banks are customers *and* co-owners | The sell-side bench by era, banks, partners, regulators, missing voices |
| [[lseg-mission-forces]] | Purpose fixed, identity moved three times, the main threat moved from regulators to the AI narrative | Mission lines, boilerplate drift, tailwinds/headwinds, risk register, crisis tests, scenarios |

**Suggested order:** people → mission-forces → refinitiv-deal → tradeweb-control → workspace-data → ai-everywhere → capital-allocation → post-trade-clearing → ftse-russell-indices → digital-markets → outside-voices. *If you came from the Tradeweb study*, start with [[lseg-tradeweb-control]].

## 2. Timeline, 2019–2026

| Year | Event | Why it matters |
|---|---|---|
| 2018 | David Schwimmer (ex-Goldman) becomes CEO | — |
| Jan 2019 | 4.92% of Euroclear bought | Open-access post-trade ties (sold Dec 2024 for €455m) |
| **Aug 2019** | **Refinitiv agreed**: all-share, EV ≈ US$27bn; sellers ~37% economic | From exchange group to data company ([[lseg-refinitiv-deal]]) |
| Sep–Oct 2019 | HKEX unsolicited bid, rejected and withdrawn | The strategic fork: regional exchange merger vs multi-asset data |
| 2020 | COVID records; EC Phase II; Borsa Italiana sold to Euronext (€4.325bn) | The remedy that later costs LCH SA clearing flow |
| **Jan 2021** | **Refinitiv completes**; Tradeweb consolidated (49% minority) | ~25,000 staff |
| 2021 | China into WGBI (phased over 36 months); Euronext to leave LCH SA | Index as capital-flow gatekeeper |
| 2022 | First buyback (£750m); Microsoft 10-year deal + ~4% stake; D&A head leaves | Overhang management begins; cloud/AI bet |
| 2023 | "Integration to transformation"; FTSE Russell–Tradeweb partnership; CMD; CFO change | Tradeweb prices as benchmarks |
| 2024 | Consortium <2% ("overhang eliminated"); WGBI to Tradeweb FTSE closes (from Mar 2025); LCH 94.2% | — |
| 2025 | Eikon retired; PTS deal (£1.15bn); "LSEG Everywhere" + MCP (Microsoft, Anthropic, OpenAI); margin >50% | AI-defence year |
| 2026 | £3bn buyback; ASV retired from 2027; DiSH/DSD; LSE 24; tokenised equities; **Octus ($3.535bn)** alongside Tradeweb–Trumid | "Global leader in fixed income data and trading" |

## 3. Five patterns across the notes

1. **Growth arrives through assets LSEG doesn't fully control.**
   - Tradeweb (50.9% economic, excluded from synergies) drives about two-thirds of the old Capital Markets segment.
   - SwapClear's economics were shared with banks until 2025.
   - FTSE Russell's asset fees follow markets.
   - The acquired desktop, which LSEG fully controls, grows ~3%. ([[lseg-tradeweb-control]], [[lseg-post-trade-clearing]], [[lseg-workspace-data]])
2. **"Open" is the constant identity, and its meaning keeps moving.**
   - 2019: open access in clearing.
   - 2021: Workspace as "not a closed box".
   - 2024: FTSE as the "open meadow" against Bloomberg's walled garden.
   - 2025–26: LLM-agnostic MCP ("closed box mentality" is the rivals').
   - Meanwhile LSEG builds an integrated credit stack (Octus + Tradeweb + Workspace + FTSE prices) that resembles the vertical models it criticises. ([[lseg-mission-forces]])
3. **Customers are counterparties on four fronts at once.** The same dozen banks buy data (and consolidate vendors to cut price), co-own clearing (and sold back their SwapClear share for £1.15bn), sit on PTS's board, and endorse tokenisation. LSEG's buyer power problem is concentrated and sophisticated. ([[lseg-outside-voices]])
4. **Capital return as narrative management.** Buybacks first absorbed a 37% seller and then answered an AI de-rating. Each step-up matches a share-price dip, and management says so ("dislocation"). ([[lseg-capital-allocation]])
5. **Self-scored KPIs, then a KPI change.** Synergies, the 90% claim, MCP adoption and the #3-in-pricing-and-reference-data claim are all LSEG-stated. ASV, the one external-facing subscription metric, was demoted in 2024 and retired from 2027 after slowing. Same lesson as the Tradeweb study ([[tradeweb-hub]] pattern 4): ask *measured how, against what?* ([[lseg-ai-everywhere]])

## 4. How LSEG connects to the other company studies

- **Tradeweb:** controlled subsidiary, data source and benchmark price source. See [[tradeweb-hub]], [[tradeweb-strategy-financials]], [[tradeweb-rates-em]], [[tradeweb-ai-price]].
- **ICE / MarketAxess:** the vertically integrated rival in pricing and fixed-income data, now buying MarketAxess. Octus + Trumid is LSEG–Tradeweb's answer. See [[ice-hub]], [[marketaxess-hub]].
- **Bloomberg:** the desktop and fixed-income-index rival LSEG defines itself against. It is never quoted in LSEG's record. See [[bloomberg-hub]], [[bloomberg-terminal-instrumentation]].
- **S&P Global:** index (S&P DJI) and data rival. Source of the D&A co-head (Biagini). See [[spglobal-hub]].
- **Thomson Reuters:** Refinitiv seller (~15% of LSEG via the consortium) and Reuters news supplier under a 30-year contract. See [[thomsonreuters-hub]].
- **Goldman Sachs / JPMorgan:** SwapClear and PTS co-owners, data customers, and the source of LSEG's CEO and CIO. See [[goldman-hub]], [[jpmc-hub]].
- **BlackRock:** iShares index licensee (>$430bn on FTSE Russell products), Aladdin data partner, Preqin supplier. See [[blackrock-hub]].

## 5. Cross-note open questions

1. **AI revenue:** when does LSEG disclose MCP/AI revenue, and does D&A growth exceed 6% in 2027? ([[lseg-ai-everywhere]])
2. **Tradeweb licence terms:** what is the arm's-length price of Tradeweb data sold through its parent, and who on Tradeweb's board signs it off? ([[lseg-tradeweb-control]])
3. **Octus integration:** does "light integration" keep the founder and team, and does the EPS-neutral-in-2028 maths hold? ([[lseg-capital-allocation]])
4. **EU clearing after 2028:** does EMIR 3 or a new equivalence cliff move euro swaps toward Eurex? ([[lseg-post-trade-clearing]])
5. **WGBI governance:** any challenge to Tradeweb-derived prices in the flagship index? ([[lseg-ftse-russell-indices]])
6. **Succession:** who follows Schwimmer, and does the D&A co-head structure last? ([[lseg-people]])

**Links:** [[lseg-refinitiv-deal]] · [[lseg-tradeweb-control]] · [[lseg-ai-everywhere]] · [[lseg-workspace-data]] · [[lseg-post-trade-clearing]] · [[lseg-ftse-russell-indices]] · [[lseg-capital-allocation]] · [[lseg-digital-markets]] · [[lseg-people]] · [[lseg-outside-voices]] · [[lseg-mission-forces]] · [[tradeweb-hub]] · [[ice-hub]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[thomsonreuters-hub]] · [[goldman-hub]] · [[jpmc-hub]] · [[blackrock-hub]] · [[market-structure-24-5-trading]] · [[wss-capital-markets-ma]] · [[canon-helmer-7-powers]] · [[canon-porter-competitive-strategy]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
**Sum-of-the-parts, on one page.** Use FY25 divisional revenue (AR 2025): D&A £3,978m, FTSE Russell £954m, Risk Intelligence £579m, Markets £3,467m (of which Fixed Income, Derivatives & Other, mostly Tradeweb, £1,539m).
- (a) Apply rough peer EV/revenue multiples: D&A 6x, FTSE Russell 15x, Risk Intelligence 9x, Tradeweb line 12x (then × 50.9% for LSEG's economic share), rest of Markets 8x.
  *(Answer: D&A ≈ £23.9bn; FTSE ≈ £14.3bn; RI ≈ £5.2bn; Tradeweb share ≈ 1,539 × 12 × 0.509 ≈ £9.4bn; rest of Markets ≈ 1,928 × 8 ≈ £15.4bn; total ≈ **£68bn** before net debt of ~£9–10bn and the LCH minority.)*
- (b) Which line carries the most valuation risk if the AI bear case is right? Which if volatility falls?
- (c) State the one disclosure (from §5) that would most change your multiple on D&A.

**Corpus refresh:** lseg.com serves plain curl. Re-pull the press-release list from `https://www.lseg.com/en/sitemap-index.xml` (paths `/en/media-centre/press-releases/`). Transcripts are PDFs under `/content/dam/lseg/en_us/documents/investor-relations/…/transcripts/`. Add new items to `articles.jsonl` and re-run the quote check against it.
