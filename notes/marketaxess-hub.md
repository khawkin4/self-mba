# Note · MarketAxess hub — the all-to-all pioneer that taught bonds to trade electronically, then sold itself to an exchange group when its home market stopped compounding

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy — platform share, counter-positioning against Tradeweb), **Course 02** (Corporate Finance & Valuation — the ICE premium vs standalone targets), **Course 07** (Data, Analytics & Decision-Making — self-measured KPIs, shifting denominators), **Course 01** (Accounting — reading "record" headlines against segment data), **E3** (M&A), **E4** (Corporate Governance — founder succession, chair split, board reshaping), **E8** (Stakeholder & Investor Relations), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Entry point for the nine MarketAxess notes; sister study [[tradeweb-hub]]

- **Source:** MarketAxess corpus as of 2026-10-25 at `_ingest/raw/marketaxess/`. The **index** (`index.tsv`, 710 rows) covers every investor-relations press release from 2019-01-01 to 2026-10-23 (296, pulled from the Q4 IR feed in the browser because `curl` is Cloudflare-blocked) plus the marketaxess.com Knowledge Center (research, media reprints, What's New). The **359 full-text items** (`articles.jsonl`) are 86 news releases, 32 earnings releases (narrative only), 7 annual letters to stockholders (FY2019–FY2025), the 2021 Investor Day and Dec 2025 Goldman Sachs decks, 230 research/insight pieces and 1 ICE release. Skipped: 91 volume releases, 65 event notices, promos, foreign-language duplicates and gated pages (reasons in the index). No earnings-call transcripts. Knowledge Center dates are mostly estimates. Read-first digest: `_ingest/raw/marketaxess/DIGEST.md`.
- **Core claim:** MarketAxess built the US corporate-bond e-trading category (founded 2000) and made **anonymous all-to-all trading** ("Open Trading") its identity. Open Trading was **27%** of credit volume in 2019 and a record **37%** in 3Q22, and its estimated client savings of over **$1B** in 2020 exceeded company revenue (MKTX's figures). That model peaked in 2020 (revenue $689M, operating margin 54.4%). After that, US high-grade share slid from a **22.8%** record (4Q20) to **18.4%** (4Q24). Credit fee per million fell from **$184.78** (FY21) to **$127** (3Q26), and by MKTX's own Dec 2025 deck US credit revenue shrank about **2% a year** over 2020–24, while every annual letter reported a "record". An exchange operator, Chris Concannon (CEO from April 2023), rebuilt the platform to trade like equities: order book, algorithms (Pragma), mid-point matching, closing auctions, indices and data (CP+ into S&P Global's pricing). That grew the business outside US credit to about half of revenue, but it did not repair the core. Seven and a half months after publishing standalone 2026–28 targets, the board agreed to sell to **ICE for $167 a share in cash** (about $5.7B EV, Jul 30 2026, close expected 1H 2027). Along the way the company's own research and products moved from *send to everyone* toward *select smart*, the same turn Tradeweb made in 2026.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[marketaxess-strategy-financials]] | A high-margin compounder whose core stopped compounding while the headlines kept saying "record" | FY19–3Q26 numbers, fee capture, KPI drift and the disclosure retreat, every deal, buybacks and the ASR, 2021 TAM vs 2025 targets |
| [[marketaxess-ice-deal]] | Targets in December, a sale in July: the standalone plan lost to a 33% cash premium | Deal terms, the road to the sale, valuation arithmetic, what ICE gets, the S&P-feed and antitrust angles, the Tradeweb–Trumid mirror |
| [[marketaxess-open-trading]] | All-to-all won the crisis argument and lost the routing argument; both venues now sell curation | Open Trading share and savings, how savings are defined, the no-leakage research, Targeted RFQ / AI Select / axes, vs Tradeweb's leakage paper |
| [[marketaxess-protocols-automation]] | Equity microstructure imported into bonds: every protocol shipped, adoption was the constraint | Live Markets, PT and X-Pro, Auto-X and Pragma, dealer algos, Mid-X, blocks, closing auctions, the five-year rebuild |
| [[marketaxess-data-cp-plus]] | Inquiry exhaust, including trades that never happened, turned into prices, tapes and indices — but the data line stayed small (~6% of FY25 revenue) and the accuracy evidence self-graded | CP+, Axess All, TraX and TraX Tape, the consolidated-tape JV, S&P / MSCI / Refinitiv / Arcesium, accuracy claims |
| [[marketaxess-international-rates]] | The half of the business that kept growing, on index inclusion, mandates and all-to-all in EM; Treasuries stayed a $4-a-million challenger | EM hard and local currency, Asia/China/India, LatAm, MENA, Eurobonds, Treasuries, munis, private banks and retail |
| [[marketaxess-people]] | A founder's all-to-all conviction handed to an exchange operator, a churned C-suite and a re-made board | Who ran MarketAxess, profiles with dated quotes, where views shifted |
| [[marketaxess-outside-voices]] | A chorus that praises all-to-all in a crisis and automation in calm, a few independents who name the tradeoff, and competitors never in the room | Clients, dealers, non-bank liquidity, partners, official sector, skeptics, the competitors it never names |
| [[marketaxess-mission-forces]] | The identity line never moved; the mission went from *open* to *intelligent*; calm markets, curated rivals and fee mix did the damage until ICE bid | Mission and boilerplate drift, tailwinds and headwinds, forces map, crisis tests, scenarios after ICE |

**Companion notes from the sibling studies:** [[ice-marketaxess-deal]] (the same deal from ICE's side — *the evaluator buys the flow*) and [[spglobal-pricing-fixed-income]] (S&P's evaluated pricing, which rents CP+).

**Suggested order:** people → mission-forces → strategy-financials → open-trading → protocols-automation → data-cp-plus → international-rates → ice-deal → outside-voices. If you've just read the Tradeweb study, start with open-trading next to [[tradeweb-a2a-information-leakage]], then ice-deal.

## 2. Timeline, 2019 → 2026

*Pre-2019 context is from boilerplate and later letters only. Figures as MarketAxess states them unless marked.*

| Year | Event | Why it matters |
|---|---|---|
| 2000 / pre-2019 | Founded; US corporate-bond RFQ. Open Trading built out in the 2010s (2016 releases on record Open Trading volume; Composite+ introduced 2017) | The category creator; all-to-all as the brand |
| Jan 2019 | Chris Concannon hired as President & COO from Cboe/Bats | Exchange DNA enters |
| 2019 | Live Markets order book and portfolio trading announced; Refinitiv redistributes CP+; IG indexes; joins the S&P 500; **LiquidityEdge** (Treasuries, about $150M) | Diversification starts |
| 2020 | COVID: Open Trading 35% of credit volume in March; NY Fed SMCCF eligible seller; Regulatory Reporting Hub bought from Deutsche Börse; FY revenue **$689M**, operating margin 54.4% | Peak year |
| 2021 | Low volatility: 2Q21 EPS −20%; MuniBrokers; China CIBM; Investor Day TAM of $5B rising to an *aspirational* $11B | The volatility dependence shows |
| 2022 | Rate shock brings record composite share and Open Trading at 37% (3Q22); MKTX 400 index and SSGA LQIG ETF; MSCI; EU consolidated-tape bid explored with **Bloomberg and Tradeweb** | Last share-gain year |
| 2023 | **Concannon CEO** (Apr 3), McVey Executive Chairman; Adaptive Auto-X; **Pragma**; X-Pro; the CT JV signed (May) and abandoned (Dec) | The rebuild begins |
| 2024 | EM and Eurobond share disclosure dropped; **ICE Bonds** liquidity link (Aug); BlackRock Aladdin (Sep); **S&P Global** data partnership (Oct); McVey retires; Hernandez becomes Chair | Partners line up; founder exits |
| 2025 | Three-channel strategy (Feb); RFQ-hub majority; India IGBs; Mid-X; **closing auctions** (Nov); medium-term targets and $300M ASR (Dec) | Last standalone plan |
| 2026 | Cifu (Virtu) and Schiciano (PE) join the board (Mar); TraX Tape (Jun); **ICE agrees to acquire MKTX** (Jul 30, $167/share, about $5.7B EV); 3Q26 revenue +1%, credit FPM $127 | The end of independence |

## 3. Six patterns across the notes

1. **A volatility derivative dressed as a growth stock.** Records come in stress years (2020, 2022, April 2025) and slumps in calm ones (2021, 2023, 2025 *continued tight credit spreads*). Open Trading's value is highest exactly when dealers step back, so the business sells insurance whose premium is set by volatility. See [[marketaxess-open-trading]], [[marketaxess-mission-forces]].
2. **The metric moves when the number stalls.** US high-grade share became HG+HY, then *composite* (Eurobond share against MKTX's own Trax denominator), then *three channels*. Open Trading penetration and savings stopped being reported after FY22/FY23, and EM, Eurobond and PT share disclosures were paused in 2024. The Tradeweb study found the same habit on the other side ([[tradeweb-credit]] §4.5). See [[marketaxess-strategy-financials]].
3. **Every venue grades itself with its own ruler.** Open Trading savings are measured against best dealer cover and CP+. Impact studies use CP+. CP+ accuracy is shown against on-platform trades. No head-to-head against Ai-Price, BVAL or ICE is published, which mirrors [[tradeweb-ai-price]]. See [[marketaxess-data-cp-plus]].
4. **Convergence on curation.** Tradeweb's 2026 *blast all → select smart* ([[tradeweb-a2a-information-leakage]]) has a MarketAxess twin: Targeted RFQ, Smart Dealer Select, AI Select, Targeted Axes and Disclosed Open Trading, all 2024–26. Both venues now argue about *which* trades go wide, not *whether* all-to-all works.
5. **Imports worked, adoption decided.** Order book, portfolio trading, algorithms, mid-point matching and auctions all shipped, usually late (Live Markets about a year, the redesign about five years). Each was judged by whether dealers and the buy side moved flow, and Concannon said so himself about auctions. See [[marketaxess-protocols-automation]], [[marketaxess-people]].
6. **Partners became the buyer.** Refinitiv (LSEG) redistributed CP+ in 2019; Bloomberg and Tradeweb were consortium partners in 2022–23; ICE linked its retail bond ATS to Open Trading in 2024 in the same *complementary* language it used for the takeover in 2026. S&P built its corporate evaluated pricing on CP+ and, after closing, will buy it from ICE. See [[marketaxess-ice-deal]], [[marketaxess-outside-voices]].

## 4. Where MarketAxess and Tradeweb meet

| Topic | MarketAxess side | Tradeweb side |
|---|---|---|
| All-to-all | The brand since the 2010s; research says it doesn't leak; products drift to curation 2024–26 | AllTrade praised as a *#4 dealer* (2021); leakage paper and SNAP+ (2026) — [[tradeweb-a2a-information-leakage]] |
| Share | HG share 22.8% (4Q20) → 18.4% (4Q24); headline share dropped | (context) The DESK, Jun 2026: Tradeweb 18.0% vs MKTX 16.0% of IG+HY TRACE — [[tradeweb-ai-price]] §6 |
| How share was won | Anonymous liquidity, HY and EM strength | Workflow around the trade: net spotting, PT, voice processing — [[tradeweb-credit]] |
| Reference price | CP+, into S&P Global | Ai-Price, distributed by LSEG — [[tradeweb-ai-price]] |
| Consolidation | Sold to ICE (Jul 2026) | Bought Trumid (Oct 2026) — [[tradeweb-strategy-financials]] |
| Cooperation | EU consolidated-tape JV with Bloomberg and Tradeweb (2022–23), abandoned | Same JV |
| Naming rivals | Never names Tradeweb, Trumid or Bloomberg as competitors | Stopped naming MarketAxess after 2019 — [[tradeweb-people]] |

## 5. Cross-note open questions

1. **Stockholder vote and regulatory review** of ICE–MKTX, alongside Tradeweb–Trumid: does anyone challenge two simultaneous credit-venue consolidations? ([[marketaxess-ice-deal]])
2. **What happens to Open Trading under ICE:** kept as the institutional all-to-all pool, merged with ICE's retail ATS, or curated further? ([[marketaxess-open-trading]])
3. **The S&P feed:** does S&P keep CP+ inside its evaluated pricing once a direct competitor owns it? ([[marketaxess-data-cp-plus]], [[spglobal-hub]])
4. **Fee per million:** is the decline mix (PT, blocks, Mid-X) or price? A clean US-credit fee series by protocol would settle it. ([[marketaxess-strategy-financials]])
5. **Closing auctions:** does participation grow into a benchmark, as Sweeney predicted, or stay a niche? ([[marketaxess-protocols-automation]])
6. **Earnings-call transcripts** (not in this corpus) for 2024–26: how did analysts press on share loss, and what did management concede live?

**Links:** [[marketaxess-strategy-financials]] · [[marketaxess-ice-deal]] · [[marketaxess-open-trading]] · [[marketaxess-protocols-automation]] · [[marketaxess-data-cp-plus]] · [[marketaxess-international-rates]] · [[marketaxess-people]] · [[marketaxess-outside-voices]] · [[marketaxess-mission-forces]] · [[tradeweb-hub]] · [[tradeweb-credit]] · [[tradeweb-a2a-information-leakage]] · [[tradeweb-ai-price]] · [[tradeweb-strategy-financials]] · [[ice-hub]] · [[ice-marketaxess-deal]] · [[spglobal-pricing-fixed-income]] · [[spglobal-hub]] · [[lseg-hub]] · [[bloomberg-hub]] · [[blackrock-hub]] · [[jpmc-hub]] · [[market-structure-24-5-trading]] · [[wss-capital-markets-ma]] · [[canon-helmer-7-powers]] · [[canon-christensen-innovators-dilemma]] · [[canon-porter-competitive-strategy]] · [[canon-hagiu-wright-multi-sided-platforms]]

---
### Rep
Write a one-page **memo as a MarketAxess stockholder deciding how to vote** on the ICE offer. Use only numbers from these notes. (1) Back out the unaffected share price from the $167 offer and the 33% premium. *(Answer: 167 / 1.33 ≈ **$125.6**.)* (2) Using the Dec 2025 targets (8–9% revenue growth a year, +75–125bp margin a year), say in one paragraph what the standalone stock needed to be worth by 2028 to beat $167, and which assumption (US credit ADV growth of at least ~6% a year) carries the most risk given 2Q26 US credit commissions fell 9%. (3) Name one thing ICE gets that a financial buyer would not (pattern 6). (4) Name the strongest reason to vote no. Then check your answer against [[marketaxess-ice-deal]].

**Corpus refresh:** the IR site blocks scripted requests. Open `investor.marketaxess.com` in the browser and call `/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=2&pressReleaseDateFilter=3&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=-1&excludeSelection=1` with same-origin `fetch()`. marketaxess.com pages and q4cdn PDFs download with `curl` with a browser user-agent. Rebuild with the scratch build script, then append new items to the relevant note.
