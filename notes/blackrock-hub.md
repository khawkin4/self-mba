# Note · BlackRock hub — the largest buy-side order book and its software became the platform others plug into; then it bought its way into private markets while its CEO's public voice retreated from climate

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy), **Course 02** (Corporate Finance & Valuation), **Course 11** (Global Strategy, Macro & Responsible Business), **E2** (Capital Allocation), **E3** (M&A), **E7** (High-Stakes Communication), **E8** (Stakeholder & Investor Relations), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Entry point for the ten BlackRock notes

- **Source:** a filtered BlackRock corpus of **103 records, 2019-01 → 2026-10** (`_ingest/raw/blackrock/index.tsv`, full texts in `articles.jsonl`, about 1.7M characters). It covers:
  - 13 Fink letters, read in full;
  - 51 investor-relations releases, filtered from 164;
  - 25 newsroom items, filtered from 112;
  - 3 AGM transcripts (2021–23);
  - the 2023 and 2025 Investor Day decks, plus the GIP, Preqin and HPS deal decks;
  - the BUIDL launch release, the Fink–Goldstein Economist op-ed, and 4 cross-references from the Tradeweb corpus.

  The filter and the gaps are documented in `_ingest/raw/blackrock/DIGEST.md`; the main gaps are no earnings-call transcripts and no AGM transcripts after 2023. Reader notes A–F are in `_ingest/raw/blackrock/reading-notes/`.
- **Core claim:** BlackRock in 2019–2026 is three stories stacked on one engine.
  - **The engine:** record flows, from $124B to $698B a year, led by iShares, plus Aladdin.
  - **Story 1, market structure.** The largest buy-side client turns its software into the hub that venues, data vendors and custodians plug into. Then it multi-sources or internalizes around every concentrated supplier.
  - **Story 2, strategy.** In 2024–25 it spends ~$27B on GIP, Preqin and HPS to become "a scale operator across public and private markets and technology". This is a bet on a higher multiple.
  - **Story 3, voice.** Larry Fink's letters retreat in stages, from "a fundamental reshaping of finance" (2020) to "energy abundance" (2026), under a two-front political attack, while the fiduciary line (*not our money*) stays the constant.
  - **What is never named:** Tradeweb, despite being BlackRock's integrated credit venue. Also missing from the documents: a successor to Fink, and any metric for its own systemic weight.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[blackrock-anchor-client]] | Venues plug into Aladdin, not the other way round; BlackRock multi-sources every concentrated supplier | Tradeweb × Aladdin phases, bond ETFs as plumbing, custodian split, TXSE, internalization |
| [[blackrock-fink-letters]] | The CEO's public voice retreated in five stages; fiduciary duty was the hinge | All 13 letters as a sequence, phrase-by-phrase tracking, what replaced climate |
| [[blackrock-private-markets]] | GIP + HPS + Preqin is the BGI playbook rerun | Deal terms, multiples, IRRs, 50/30/20, 401(k), AI infrastructure |
| [[blackrock-aladdin-data]] | Aladdin grew from an internal system into others' operating layer and is reaching for the private-markets index | Tech revenue, eFront to Preqin, AI, neutrality risk |
| [[blackrock-digital-assets]] | The incumbent tokenizes the rails but keeps the regulated wrapper | BUIDL structure, Securitize conflict, IBIT, stablecoin reserves, the Economist op-ed |
| [[blackrock-stewardship-backlash]] | Attacked from both sides: exit, settle, fight, and hand the choice back to clients | CA100+, NZAM, the AG suits, DOJ/FTC, Lander, Voting Choice, AGM votes |
| [[blackrock-strategy-financials]] | A flow machine whose margin follows markets; the deals bet on a re-rating | FY2018–Q3 2026 table, 2030 targets, GAAP vs adjusted, bear-case arithmetic |
| [[blackrock-people]] | A founder-CEO with no named heir; power spreading to the CFO, COO and acquired founders | Org chart, profiles with dated quotes, board, succession signals |
| [[blackrock-outside-voices]] | Critics appear only where BlackRock can't edit them | Every AGM proponent, the officials, partners' revealing quotes, vote scoreboard |
| [[blackrock-mission-forces]] | Purpose never changed; identity did, and the risks moved to politics, antitrust and illiquidity | Purpose and boilerplate, strategy pillars, tailwinds and headwinds, five forces, crisis tests, scenarios |

**Suggested order:** people → fink-letters → mission-forces → strategy-financials → anchor-client → aladdin-data → private-markets → digital-assets → stewardship-backlash → outside-voices.

## 2. Timeline, 2019–2026

| Date | Event | Note |
|---|---|---|
| 2019-01 | *Purpose & Profit* CEO letter | [[blackrock-fink-letters]] |
| 2019-03 | eFront ($1.3B), private-markets software | [[blackrock-aladdin-data]] |
| 2020-01 | *Fundamental reshaping of finance*; sustainability as the "new standard" | [[blackrock-fink-letters]] |
| 2020-03 | COVID letter: bond ETFs modernizing the "$100 trillion bond market" | [[blackrock-anchor-client]] |
| 2020-04 | Aladdin on Azure | [[blackrock-aladdin-data]] |
| 2020-05 | PNC exits its 22% stake; $1.1B buyback | [[blackrock-strategy-financials]] |
| 2021-01 | Net zero; "sustainability premium" | [[blackrock-fink-letters]] |
| 2021-12 | iShares post-trade: one custodian becomes four | [[blackrock-anchor-client]] |
| 2022-01 | *Not woke* CEO letter; Voting Choice | [[blackrock-stewardship-backlash]] |
| 2022-03 | Russia "has put an end to the globalization"; first stablecoin mention | [[blackrock-fink-letters]] |
| 2022-05 | AGM: the "tactical" pullback on climate proposals; first anti-ESG questions | [[blackrock-outside-voices]] |
| 2022-10 | Martin Small named CFO | [[blackrock-people]] |
| 2022-12 | **Tradeweb credit integrated into the Aladdin OEMS** | [[blackrock-anchor-client]] |
| 2023-03 | First combined letter after SVB; *not… environmental police* | [[blackrock-fink-letters]] |
| 2023-06 | Investor Day: "Platform as a Service"; 5% organic target | [[blackrock-strategy-financials]] |
| 2023-12 | Tradeweb AllTrade inside Aladdin | [[blackrock-anchor-client]] |
| 2024-01 | **GIP**; "strategic re-architecture" | [[blackrock-private-markets]] |
| 2024-02 | Exit from CA100+ (Inc. level) | [[blackrock-stewardship-backlash]] |
| 2024-03 | **BUIDL** on Ethereum; "energy pragmatism" letter | [[blackrock-digital-assets]] |
| 2024-05 | Securitize round led by BlackRock, with Tradeweb co-investing | [[blackrock-digital-assets]] |
| 2024-06 | TXSE founding stake; **Preqin** | [[blackrock-anchor-client]], [[blackrock-aladdin-data]] |
| 2024-09 | AI Infrastructure Partnership | [[blackrock-private-markets]] |
| 2024-12 | **HPS** | [[blackrock-private-markets]] |
| 2025-01 | NZAM exit; Tennessee case resolved | [[blackrock-stewardship-backlash]] |
| 2025-03 | *Not who we are anymore*; 50/30/20; *every asset can be tokenized* | [[blackrock-fink-letters]] |
| 2025-05 | DOJ/FTC back the coal antitrust suit; BlackRock calls it "baseless" | [[blackrock-stewardship-backlash]] |
| 2025-06 | Investor Day: 2030 targets; internalization | [[blackrock-strategy-financials]] |
| 2025-11 | Mexican repo on Tradeweb via Aladdin; NYC Comptroller rebuttal | [[blackrock-anchor-client]], [[blackrock-outside-voices]] |
| 2025-12 | Fink–Goldstein Economist op-ed | [[blackrock-digital-assets]] |
| 2026-01 | FY2025: $14T AUM, record $698B inflows | [[blackrock-strategy-financials]] |
| 2026-03 | "Growing with your country" letter | [[blackrock-fink-letters]] |
| 2026-10 | Q3 2026: $15.49T AUM; "investing, financing, and technology" | [[blackrock-mission-forces]] |

## 3. Five patterns across the notes

1. **Multi-source the supplier, own the workflow.**
   - Custodians (four), proxy advisers (Egan-Jones), exchanges (TXSE), dealers ("multiple intermediaries") and venues (internal crossing) are all treated the same way.
   - Aladdin is the workflow everyone plugs into. Venues court it.
   - This is the other side of [[tradeweb-outside-voices]] and [[tradeweb-mission-forces]] (buyer power), and of the coming venue consolidation ([[ice-hub]], [[marketaxess-hub]]).
2. **Wrap the new thing in an old wrapper.**
   - ETFs for bonds (2002 onward), ETPs for bitcoin (2024), money-market structures for tokenized cash (BUIDL) and SMAs or target-date funds for private markets (2025–26).
   - BlackRock monetizes innovations others built by packaging them for its distribution ([[blackrock-digital-assets]], [[blackrock-private-markets]]).
3. **Buy the data layer, then the index.**
   - The sequence runs from eFront (2019) to Clarity AI and Baringa (2021) to Preqin (2024).
   - The aim is to "index private markets just like we do now with the S&P 500" (Fink, 2025), moving BlackRock from index licensee to index owner ([[blackrock-aladdin-data]]). That puts it up against [[spglobal-hub]], [[lseg-hub]] and [[bloomberg-hub]].
4. **The fiduciary hinge.** *Not our money* is the argument for activism (2020), for neutrality (2023), against the right (DOJ/FTC) and against the left (Lander). The principle stays constant while the policy swings ([[blackrock-fink-letters]], [[blackrock-stewardship-backlash]]).
5. **Self-measured scorecards.** These are the BlackRock counterpart of the Tradeweb study's pattern 4 ([[tradeweb-hub]] §3). All are BlackRock's own benchmarks:
   - execution savings ("25%" in 2023, "~$600 million" in 2024);
   - deal IRRs (15–18%);
   - the private-asset uplift in target-date funds (+50bp);
   - the "sustainability premium" (2021);
   - user counts whose definitions keep changing.

## 4. Who holds power over whom (summary)

| Relationship | Direction | Evidence |
|---|---|---|
| BlackRock → venues (Tradeweb, MarketAxess) | BlackRock stronger | Venues integrate into Aladdin; BlackRock never names Tradeweb; internalization ([[blackrock-anchor-client]]) |
| BlackRock → custodians, proxy advisers | BlackRock stronger | Four-way custody split; third proxy adviser |
| Index providers (S&P, MSCI, FTSE Russell) → BlackRock | Providers stronger today | "BlackRock does not choose the components of the index" (2021 AGM); Preqin is the hedge |
| State officials and DOJ/FTC → BlackRock | Officials stronger in 2022–25 | Pledge exits, settlements ([[blackrock-stewardship-backlash]]) |
| Hyperscalers ↔ BlackRock/GIP | Mutual | Capex "beyond what any single company or government can finance" (Microsoft) |
| Acquired founders ↔ BlackRock | Founders gaining | Board and GEC seats, deferred stock ([[blackrock-people]]) |

## 5. Cross-note open questions

1. **Succession:** does a co-signatory, President or co-CEO appear by the 2027 letter? ([[blackrock-people]])
2. **Coal antitrust ruling:** what does it mean for common ownership? ([[blackrock-stewardship-backlash]])
3. **Private-markets scorecard:** fundraising against ~$67B a year toward $400B; private markets plus technology against 30% of revenue. ([[blackrock-private-markets]], [[blackrock-strategy-financials]])
4. **Aladdin–venue terms** after ICE–MarketAxess and Tradeweb–Trumid. ([[blackrock-anchor-client]])
5. **Preqin indices:** licensed to third parties? ([[blackrock-aladdin-data]])
6. **BUIDL as collateral** at venues or clearing houses. ([[blackrock-digital-assets]])

**Links:** [[blackrock-anchor-client]] · [[blackrock-fink-letters]] · [[blackrock-private-markets]] · [[blackrock-aladdin-data]] · [[blackrock-digital-assets]] · [[blackrock-stewardship-backlash]] · [[blackrock-strategy-financials]] · [[blackrock-people]] · [[blackrock-outside-voices]] · [[blackrock-mission-forces]] · [[tradeweb-hub]] · [[tradeweb-credit]] · [[tradeweb-outside-voices]] · [[tradeweb-mission-forces]] · [[ice-hub]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[lseg-hub]] · [[thomsonreuters-hub]] · [[goldman-hub]] · [[jpmc-hub]] · [[market-structure-24-5-trading]] · [[wss-private-markets-wealth]] · [[sec-filing-intelligence]] · [[canon-porter-competitive-strategy]] · [[canon-helmer-7-powers]] · [[canon-pfeffer-power]]

---
### Rep
**Write a one-page memo as a Tradeweb board member: *How dependent are we on BlackRock, and what do we do about it?*** Use only numbers from these notes and the Tradeweb notes.

1. Size BlackRock's credit flow, using the [[blackrock-anchor-client]] Rep (≈277 AllTrade trades a day from Aladdin).
2. Name BlackRock's three outside options: other venues, internalization, and Aladdin's integrations with rivals.
3. Name Tradeweb's three counter-moves: Trumid, curated *select smart* RFQ, and co-investing in rails (Securitize).
4. State the one number you would ask BlackRock for, and the one you would never get.

Then compare your memo with how Tradeweb's own releases describe the partnership ([[tradeweb-credit]] §1).

**Corpus refresh:** blackrock.com and q4cdn PDFs download with `curl -A "Mozilla/5.0"`. ir.blackrock.com needs the browser: use same-origin `fetch` against the Q4 feeds `/feed/PressRelease.svc/GetPressReleaseList?…&bodyType=2&year=YYYY` and `/feed/Event.svc/GetEventList?…`. The method is documented in `_ingest/raw/blackrock/DIGEST.md` and in the shared session notes. Add new Fink letters as their own records.
