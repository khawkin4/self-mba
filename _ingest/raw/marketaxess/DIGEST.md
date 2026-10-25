# MarketAxess (MKTX) — corpus digest, 2019 → Oct 2026

> Read-first stage. Nothing here has been written to `notes/` yet. This file says what was collected, what it says, and what is worth turning into notes.
> Built 2026-10-25. Everything in straight double quotes below is a verbatim quote of 25 words or fewer, checked by script against `articles.jsonl` (whitespace-normalised). The method is at the end.

---

## 1. What the corpus is

**Files**
- `index.tsv` has **710 rows**: every item found from 2019-01-01 to 2026-10-23, plus undated Knowledge Center items. Columns are date, type, topic, title, url, fetched (Y/N) and skip_reason. Estimated dates also carry their basis.
- `articles.jsonl` has **359 full-text items**, about 1.87M characters. Fields: date, type, topic, title, url, source, text. Knowledge Center items also have date_basis and keywords.

**Sources**

| Source | How it was obtained | Items |
|---|---|---|
| investor.marketaxess.com press releases (Q4 platform) | Cloudflare blocks `curl`. I used the site's own JSON feed (`/feed/PressRelease.svc`) via same-origin `fetch()` in the built-in browser. The feed holds 625 releases back to 2009; **296 are dated 2019 or later**. | 296 indexed, 119 fetched |
| Earnings releases (in the above) | Narrative only. Text is cut at the conference-call or financial-table section, capped at 20k characters. | 32 |
| Annual reports, FY2019–FY2025 | PDFs from q4cdn. Only the **CEO *Letter to Stockholders and Clients*** was kept. | 7 |
| Investor decks | 2021 Virtual Investor Day; Goldman Sachs conference, Dec 9 2025 (medium-term targets) | 2 |
| marketaxess.com Knowledge Center: AxessPoint research, thought leadership, media reprints, What's New | Sitemap (287 URLs) plus the 240-card `/knowledge` listing, fetched with `curl` | 236 fetched |
| ICE releases naming MarketAxess | Copied from the sibling ICE corpus (`_ingest/raw/ice/articles.jsonl`). The ICE deal release came from there too, because the MKTX PDF copy lost its "fi"/"ff" ligatures in extraction. | 1 (+ deal text) |

**Fetched items by year and type** (*undated* means no usable date clue):

| Type | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | undated / pre-2019 |
|---|---|---|---|---|---|---|---|---|---|
| News release (IR) | 18 | 12 | 11 | 6 | 11 | 9 | 12 | 8 | – |
| Earnings release | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | – |
| Shareholder letter / deck | – | 1 | 2 | 1 | 1 | 1 | 2 | 1 | – |
| AxessPoint research | 3 | 7 | 12 | 8 | 2 | 1 | 9 | 2 | 5 + 1 |
| Research / insight | 1 | 7 | 7 | 11 | 20 | 15 | 11 | 18 | 33 + 2 |
| Media reprint (*In the News*) | – | – | – | – | – | – | 11 | 3 | – |
| What's New | – | 1 | 1 | 1 | – | 2 | 4 | 1 | 31 |

**Skipped, and why** (all recorded in `index.tsv`):

| Count | Reason |
|---|---|
| 91 | Monthly or quarterly volume statistics. Routine, and the same numbers appear in the earnings releases. |
| 65 | Conference-call, investor-conference and updated-time notices |
| 14 | Duplicate releases |
| 5 | Philanthropy and office PR (Trading for Trees and Turkeys, EMpower, Spacesmith) |
| 42 | What's New promos: monthly dealer rankings, charity days, *cast your vote* |
| 13 | Foreign-language duplicates (FR, DE, JP) |
| 16 | Pages with no article text (video or form landing pages) |
| 102 | Knowledge Center cards with no fetchable page (gated whitepapers, videos, SSRN academic papers, legacy MiFID cards, PDFs) |
| 2 | Bodies not retrievable: the Virtu RFQ-hub consortium release (ir.virtu.com returns 403) and the SSGA LQIG ETF release (no body) |

**Gaps and caveats**
- **No earnings-call transcripts.** They are not on the IR site, so live Q&A with analysts is missing. This is the biggest gap for *views under pressure*.
- **No standalone product press releases for X-Pro (2023), CP+ launches or Adaptive Auto-X GA.** MarketAxess announced these on calls or the corporate site, not the IR feed. They are covered through earnings releases and letters.
- **Knowledge Center dates are weak.** Only about 18 cards carry a stated date. Others are estimated from the latest year cited in the text, asset upload paths or card order, and 69 fetched items are undated. Readers found misdated items: *Brazil's fixed income market turns electronic* is about May 2026; *Fed-day dynamics* is 2026; *More block trades are going electronic* is about Q2 2026; *Bringing transparency to the muni marketplace* is about 2024–25, not 2017. Treat any date with `date_basis` ≠ `stated` as approximate.
- **Selection bias.** Every outside voice here was chosen by MarketAxess, apart from the few media reprints (Bloomberg, The TRADE, The DESK, GlobalCapital, WatersTechnology), and even those were reposted by MarketAxess. The corpus **never names a competitor** except in the Bloomberg/Tradeweb consolidated-tape releases and in Bloomberg's own competitor disclosure.

---

## 2. Chronology: 36 events that matter

| Date | Event | Why it matters |
|---|---|---|
| 2019-01-07 | **Chris Concannon** (ex-Bats CEO, Cboe President, Virtu, Nasdaq, SEC) is hired as President & COO | Exchange and ETF microstructure DNA arrives. He is the strategy owner from here on. |
| 2019-04-04 | Virtu partnership (RFQ-hub ETF trading, eNAV) | First ETF move. It reappears in 2022 as the RFQ-hub consortium and in 2026 as a board seat for Virtu co-founder Doug Cifu. |
| 2019-04-11 | Refinitiv agrees to redistribute Composite+ (CP+) and Axess All | Data distribution starts, ironically through Tradeweb's controlling shareholder. |
| 2019-05-09 | Live Markets all-to-all order book announced for 2H19 | It actually launched in summer 2020, and its volume is never disclosed. |
| 2019-06-19 | Portfolio-trading protocol announced for "Autumn of 2019" | By June 2021 only "more than 50" trades had been done. PT is where MKTX fell behind Tradeweb. |
| 2019-07-01 | Joins the S&P 500 | Peak of the growth-stock era |
| 2019-11-01 | LiquidityEdge (US Treasuries) closes, about $150M | Rates entry. It stays a 2–3.7% share and about $4/million fee business. |
| 2020-03/04 | COVID: Open Trading reaches 35% of credit volume in March 2020; McVey says it was "essential" | All-to-all proves itself as crisis liquidity. This is the core of the brand. |
| 2020-09-09 | NY Fed names MarketAxess an eligible seller for the SMCCF | Official-sector endorsement of the venue |
| 2020-11-30 | Deutsche Börse Regulatory Reporting Hub acquired | Post-trade (Trax) scale in the EU |
| 2021-01-27 | FY20: revenue $689M (+35%), operating margin 54.4%, Open Trading savings above $1B (more than revenue) | **High-water mark** |
| 2021-04-09 | MuniBrokers closes | Muni inter-dealer entry |
| 2021-07-21 | 2Q21 revenue −5%, EPS −20%, blamed on low volatility | End of the *record earnings* streak. It shows the business is a volatility derivative. |
| 2021-09-14 | Investor Day: a $5B to *aspirational* $11B revenue opportunity; target of 50% international revenue | Peak ambition. No financial targets. |
| 2021-09-27 | China CIBM access via CFETS / Bond Connect | International expansion |
| 2022-03-16 | MKTX US IG 400 tradable index; SSGA's LQIG ETF launched on it | Venue becomes index provider |
| 2022-06-22 | **Bloomberg, MarketAxess and Tradeweb explore a joint EU consolidated-tape bid** | Rivals cooperate on infrastructure |
| 2022 | Rate shock: composite share hits a record, Open Trading 37% of credit volume (3Q22), PT $25B a quarter | Last share-gain year |
| 2023-01-09 | **Concannon named CEO** (from Apr 3, 2023). McVey becomes Executive Chairman. | Founder-to-operator succession |
| 2023-05-23 → 2023-12-08 | CT JV signed with Bloomberg and Tradeweb, then **abandoned** over "risk and complexity" | MKTX later sells its own TraX Tape into the same reform (2026). |
| 2023-06-22 | First client algo trade on **Adaptive Auto-X** | Shift from RFQ venue toward smart order routing |
| 2023-10-02 | **Pragma** (algorithmic trading) acquisition closes | Its execution technology becomes "the backbone". Mid-X and auctions run on it. |
| 2023 (FY) | X-Pro "order-centric" platform rolls out. The FY23 letter has **no market-share numbers at all**. | The disclosure retreat begins. |
| 2024-01-31 | MKTX stops publishing EM and Eurobond market share (methodology review) | Disclosure retreat, continued |
| 2024-08-05 | **ICE Bonds and MarketAxess connect liquidity networks** (munis and corporates, retail plus institutional) | Commercial precursor to the takeover, in the same "complementary strengths" language |
| 2024-09-09 | Expanded **BlackRock Aladdin** integration | Distribution through the largest buy-side OEMS |
| 2024-10-31 | **S&P Global MI data partnership**: CP+ feeds S&P Evaluated Bond Pricing, and S&P reference data feeds MKTX | CP+ becomes a valuation input. After ICE closes, S&P's corporate pricing rests on an ICE-owned feed. |
| 2024-11-06 | **McVey to retire** end-2024. Carlos Hernandez (ex-JPMorgan) becomes Chair, splitting the roles for the first time. | Founder exits |
| 2025-02-06 | FY24: HG share 18.4% in 4Q24 (vs 20.9%), HY 13.4% (vs 17.2%). Concannon unveils the **"three channels"** plan. | Share erosion is admitted and reframed. |
| 2025-05-12 | Majority (~90%) of **RFQ-hub** (ETFs, derivatives) | Multi-asset RFQ |
| 2025-06/07 | First fully electronic Indian Government Bond workflow for foreign investors (first trade: BlackRock–StanChart) | EM local-markets growth |
| 2025-08-05 | **Mid-X** launched in US credit (anonymous mid-matching priced off CP+) | Goes after dealer-to-dealer flow |
| 2025-11-05 | **Opening and Closing Auctions** for US HG/HY (advisory group: BlackRock, DWS, State Street, AB) | Imports equity closing-auction microstructure into bonds |
| 2025-12-09 | **Medium-term targets** for 2026–28: 8–9% revenue growth, +75–125bp margin a year, plus a $300M ASR | A standalone plan, abandoned within about 7.5 months |
| 2026-01-26 | Doug Cifu (Virtu co-founder) and Ken Schiciano (TA Associates PE) elected to the board, effective March 1 | Board reshaped (the significance is inference) |
| 2026-06-18 | **TraX Tape** launched in London (consolidated, de-duplicated, CP+-enriched) | A commercial play on the EU/UK tape |
| 2026-07-30 | **ICE agrees to acquire MarketAxess** for $167 a share in cash: 33% premium, about $6.0B equity value, about $5.7B EV, about 10.6x LTM EBITDA with synergies. All-debt financed, $100M of cost synergies, close expected 1H 2027. | The end of independent MKTX |
| 2026-10-23 | 3Q26: revenue +1%, credit fee per million $127 (−9%), $13.1M of merger costs; 1Q26 "other legal expenses" are reclassified as merger-related | The sale process was running by Q1 2026. |

---

## 3. People

### Rick McVey: founder (2000), Chair & CEO to April 2023, Executive Chair, retired end-2024
- **Signature view: all-to-all is the moat.** Price improvement for clients is the proof, and volatility is the swing factor.
  - "We believe Open Trading liquidity was essential to the functioning of credit markets during the quarter" (1Q20, 2020-04-29)
  - "Second quarter results were heavily impacted by low levels of credit market volatility in a very tough year over year comparison for MarketAxess" (2021-07-21)
  - "reflecting the powerful benefits of Open Trading, our unique all-to-all liquidity pool" (4Q22, 2023-01-25)
  - "Without the open market — with its large, diverse pool of different types of participants" (FY19 letter)
- **Shift.** His language moves from automation (2019) to crisis resilience and savings above revenue (2020) to defence, citing low volatility and a "broader foundation" (2021), and finally to a higher-rate "long runway" (2022). Handing over: "we believe that it is now the right time for the leadership transition" (2023-01-25).

### Chris Concannon: President & COO 2019–23, CEO from April 2023
- **2019–22: exchange and ETF logic applied to bonds**, with data as a product.
  - "MarketAxess continues to digitize the credit markets and build on its record of innovation and growth." (2019-01-07)
  - "We are still in the early days of the indexation of the fixed income markets" (2021-10-18)
- **2023: automation, AI, Pragma.**
  - "quantitative, AI-powered technology solutions powered by proprietary data designed to simplify and enhance their workflows" (2023-08-07)
- **2024–25: share recovery, then open admission.**
  - "We have a clear strategy to return to market share growth in U.S. credit across these three channels" (FY24 letter)
  - "To address our challenges in U.S. credit, we are focused on growing our targeted block trading solution in the client-initiated channel." (3Q25)
  - "We still have work to do" (FY25 letter, on the technology transformation)
- **Dec 2025: stockholder value.**
  - "Our announcements today reflect the Board’s confidence in our long-term strategy and our commitment to driving stockholder value creation." (2025-12-09)
- **Jul 2026: scale.**
  - "Together, we will have the scale to invest more deeply in the areas that matter most to our customers." (2026-07-30)
- **On auctions:** "There’s no tradeable true auctions. This is the first." (Bloomberg reprint, 2025-11-05)
- **Read.** He arrived to make bonds trade like equities: order books, ETFs, indices, algos, auctions. Each of those got built. None of them repaired US-credit share or fee capture, and the strategy ended in a sale to an exchange group. (Inference.)

### The bench (selected)
- **Kat Sweeney**, Head of Index & ETF, later Data & ETF Solutions, ex-SSGA and Goldman ETF market-making. She is the ETF/auction/data voice.
  - "Within the next couple of years, this could be the dominant protocol in the market." (The TRADE, 2025-12-15, on the closing auction)
  - "we’re now in the beginning of the snowball phase." (same piece)
- **Richard Schiffman**, Head of Open Trading, later Global Head of Trading Solutions.
  - "a streaming order book requires commitment from all participants to succeed." (2021-05-27). This is an early admission of why Live Markets stayed small.
- **Spencer Lee**, Head of Client Product, Americas (2025). He was quoted as an Agilon Capital client in the 2021 deck before he was hired.
  - "Our goal isn’t more tools, it’s better orchestration of them." (The DESK, 2026-06-15)
- **Dean Berry**, Group COO and CEO EMEA/APAC (2025), ex-LSEG/BGC.
  - "The data tells you what happened, and TraX Tape tells you what it means." (2026-06-18)
- **Others:**
  - Ilene Fiszel Bieler: CFO from 2024, after Gerosa (2021–24) and DeLise (to 2021).
  - William Quan: CTO from 2026, reporting to Berry rather than the CEO.
  - Dan Burke: Global Head of EM.
  - Riad Chowdhury: Head of APAC.
  - Steve Tait: US dealer execution and Mid-X, ex-JPMorgan.
  - Julien Alexandre: research.
  - Gareth Coltman: automation product.
  - Daniel Kelly: munis.
- **Board arc.**
  - 2019–21 additions map to strategy: Prager (ex-BlackRock trading), Gmelich (ex-Goldman FICC), Gibson (Loop, diversity dealers), Charles Li (ex-HKEX, China).
  - 2023–26 additions map to the endgame: Hernandez (JPMorgan banker, Chair 2025), Hoornweg (StanChart), Cifu (Virtu) and Schiciano (PE).
- **Churn (admitted in numbers, read as inference).** Two CFO changes in three years. New COO, CTO and Americas product head. Severance for "changes in management structure" in three quarters, 2025–26.
- **A small fact.** Concannon's 2019 bio lists him as a former attorney at Morgan, Lewis & Bockius, which is ICE's co-counsel on the deal.

### ICE side (deal release)
- **Jeff Sprecher**, ICE Chair & CEO.
  - "take the largest, least-efficient corners of global finance and apply technology and network effects to improve transparency"
  - "That is what we did in energy, in credit default swaps, and in mortgage technology."
- **Warren Gardiner**, ICE CFO: "We are acquiring a high-quality, cash-generative business"

---

## 4. Mission and identity: as stated, and how it changed

- **2019, open access.** The purpose is "our purpose is to open global markets to create" more opportunity (FY19 letter). The boilerplate rewrite of April 2019 makes Open Trading the identity: "MarketAxess’ award-winning Open Trading™ marketplace is regarded as the preferred all-to-all trading solution in the global credit markets". That sentence then survives in every release through 2026.
- **2021–22, full lifecycle.** Trax drops out of the boilerplate. "intelligent data products" and the "full trading lifecycle" come in.
- **2023, transformation.** "transform the way fixed-income is traded, making it easier for institutions to invest in and trade bonds" (FY23 letter).
- **2024–25, intelligence.** "mission of creating an intelligent, global, electronic fixed-income marketplace that works better for everyone" (FY24 letter). Then the "MarketAxess advantage", meaning network, differentiated liquidity and AI data. Open Trading is recast as one plank of "differentiated liquidity".
- **2026, ICE's description.** ICE describes MKTX as "a preeminent electronic trading platform for global institutional fixed income markets". The word *institutional* matters: retail and wealth is ICE's side of the story.
- **What disappeared.** Open Trading penetration % (last given as 36% in FY22) and Open Trading savings dollars (last about $470M in FY23). ESG, which was one of six 2021 progress areas, is gone after 2023. So are the HG market-share headline and any *record share* language.

---

## 5. Tailwinds, headwinds, challenges

**A** = the company admits it; **I** = my inference from its numbers.

**Headwinds and challenges**
- **US credit share erosion (A from 2024, I before).**
  - HG share was 22.8% at the 4Q20 record and 21.3% in FY22. It fell to 18.4% in 4Q24. HY fell from 20.5% (4Q22) to about 13%.
  - The headline metric moved as share stalled: HG, then HG+HY, then "composite" (with Eurobond share measured against MKTX's own Trax data), then "channels".
  - 3Q25: "dampened our market share and revenue growth in U.S. credit".
- **US credit revenue shrinking (A, Dec 2025 deck).** US credit revenue had a **(2%)** CAGR over 2020–24, against +15% outside US credit. Operating margin was 46% in 2022 and 42% in 2024. The deck says: "A return to U.S. credit revenue growth is fundamental to our future success".
- **Fee compression (A, but explained as mix and duration).** Credit fee per million went $184.78 (FY21), $166.96 (FY22), $139 (FY25), $127 (3Q26). Growth came in low-fee protocols: PT, blocks, Mid-X, RFQ-hub. Dealers migrating to fixed-distribution plans is another quiet price concession (A, 2022).
- **Volatility dependence (A).** 2020 and 2022 were records and 2021 slumped. The FY25 letter blames "continued tight credit spreads and low credit spread volatility".
- **Technology execution (A).** The 2021 deck promised a "Fully redesigned trading experience" for 1Q22. It became X-Pro (2023), a "build" year (2024), "still have work to do" (2025) and a new CTO (2026). That is roughly five years of rebuilding while Tradeweb took share.
- **Competition (I).** Tradeweb and Trumid are never named. Competition appears only in the risk-factor boilerplate.
- **Information leakage and the winner's curse in anonymous pools (A, in research).** "Given the risk of the winner’s curse, sell side dealers could adopt a more defensive strategy when pricing bonds in anonymous liquidity pools." (Asia blocks, 2025)
- **Concentration in dealer algos (I).** Algos are the counterparty on 88% of US HG trades and answer 96% of RFQs. They do keep quoting in stress: about 80% of prices in the April 2025 shock, against 50% in COVID.

**Tailwinds**
- **Outside US credit (A).** $406M of revenue in FY25 (+10%), about 50% of the total. EM topped $1T in 2025. The platform covers 100% of the GBI-EM index, and index inclusion (India, China, later Korea and Saudi) brings demand. Brazil's 2026 accreditation mandate.
- **Data and services (A).** Services revenue was a record $112M in FY25. The S&P, MSCI, Arcesium and Refinitiv deals; TraX Tape; CP+ in munis and ETFs.
- **ETF and passive growth (A).** Index products, PT, closing auctions and RFQ-hub are all bets that bond trading follows the index.
- **Automation (A).** 28% of credit trade count and 11% of credit volume (FY25). Power users automate 92% of HG.
- **Regulation (A).** The EU/UK transparency reforms (TraX), MiFID, SFTR and CSDR post-trade, and US all-to-all advocacy in Treasuries.
- **Why sell (A + I).** The admitted case is scale and complementarity: ICE brings retail/wealth, data, indices and connectivity. The inferred case is that the standalone plan needed US credit to recover and it wasn't (2Q26 US credit commissions −9%), so a 33% cash premium beat waiting.

---

## 6. Outside voices and skeptics (all inside the corpus)

**Skeptics and cautions**
- **Bloomberg News** (reprint, 2025-11-05), on auctions: "the worry is there’s a tradeoff if it squeezes dealer profits tied to the very inefficiencies it would eliminate." The article also discloses that Bloomberg competes with MarketAxess and Tradeweb.
- **Paulo Costa** (MKTX, Fireside Friday, 2025-07-11), on Asia: "our clients have an absolute craving for transparency but potentially not their own." A wry admission of the data business's tension.
- **Aberdeen, Russell Beer** (FIX axe panel): "It’s a data war out there". Buy-siders complain dealers don't update axes, and MKTX concedes "there is real work to do on measurement, transparency, and incentive design".
- **DWS, Jeff Lenamon**, hedging even while endorsing: CP+ is "a great tool to help us potentially minimize tracking error".

**Allies and validators**
- BlackRock (Prager on the board; Veiner on auctions; Aladdin; first IGB trade).
- Goldman Sachs: Amy Hong backs Live Markets for "pre-trade price transparency and execution certainty".
- MSCI: Henry Fernandez, "As bond markets continue to evolve beyond over-the-counter trading coupled with compressed management fees".
- S&P Global: Laura Misher and Tasha Gonska. Coalition Greenwich (Kevin McPartland) on all-to-all Treasuries. The PIMCO all-to-all paper. The NY Fed (SMCCF).

**Non-bank liquidity**
- Virtu (Cifu, 2019 partner and 2026 director), Citadel Securities, Flow Traders and Jane Street via the RFQ-hub consortium.
- Flow Traders' Pereira: "market participants are looking to connect with alternative liquidity providers like Flow Traders."

**Missing**
- Analysts, activists, regulators critical of MKTX, and competitors speaking for themselves.

---

## 7. Links to the Tradeweb study (`notes/tradeweb-*.md`)

1. **The same turn, from the other side.** Tradeweb's 2026 *blast all → select smart* turn (SNAP+, the A2A-leakage whitepaper, see [[tradeweb-a2a-information-leakage]]) has a MarketAxess twin. In 2024–26 MKTX's own products moved toward curation: Targeted RFQ (hit ratios about 13% above average), AI Select, Smart Dealer Select, Targeted Axes, Disclosed Open Trading. Its research says it plainly: "Instead of “blasting” inquiries broadly, traders can engage a curated set of counterparties".
2. **The contradiction is in the research.** MKTX's research says all-to-all does not leak. Its impact study finds a median post-trade impact of about 13% of bid-ask in US HG, with Open Trading adding about zero: "access to all-to-all liquidity is not the market impact penalty box." Yet it hedges: "Larger and less liquid trades may still call for more selective distribution." Both venues grade themselves with their own reference price (CP+ vs Ai-Price). The convergence suggests the debate is about *which* trades go wide, not whether all-to-all works.
3. **The CP+ vs Ai-Price contest** ([[tradeweb-ai-price]]). MKTX sells CP+ as the data moat: "sets CP+ apart from pricing solutions that rely solely on public trade tapes." It never publishes an error statistic against a rival, which matches the Tradeweb note's critique. S&P ↔ MKTX (soon ICE) against LSEG/FTSE ↔ Tradeweb is confirmed from the MKTX side. Twist: Refinitiv (LSEG) was CP+'s first redistributor in 2019.
4. **Partners on infrastructure, silent rivals on product.** The 2022–23 EU consolidated-tape JV with Bloomberg and Tradeweb is the only time MKTX names either. Neither company names the other as a competitor in its own newsroom. A shared communications norm.
5. **Consolidation in parallel.** ICE–MKTX (Jul 2026) and Tradeweb–Trumid (Oct 2026) both target close in H1 2027. Trumid never appears anywhere in the MKTX corpus. The share flip is in the Tradeweb notes, not here (The DESK, June 2026: Tradeweb 18.0% vs MKTX 16.0% of IG+HY TRACE). MKTX stopped headlining share as that happened.
6. **Shared people and ties.** Dean Berry (MKTX COO 2025) came from LSEG, Tradeweb's controlling shareholder. Richard Prager (ex-BlackRock) sits on the MKTX board; BlackRock is a client and partner of both venues. Concannon and Tradeweb's Hult are both exchange-style operators who succeeded founders (McVey; Olesky).
7. **Different moats.** The Tradeweb note argues Tradeweb won by wiring the workflow around the trade: spotting, voice processing, PT. MKTX's admitted laggards are exactly PT (an X-Pro feature only from 2023) and blocks ("principally done over the phone", 2024). MKTX's edge stayed in HY, EM and anonymous all-to-all.

---

## 8. Recommendation: what's worth noting

Ranked by value for your time. Course codes refer to `CURRICULUM.md`.

1. ***ICE buys MarketAxess: how the all-to-all pioneer ended up for sale***
   - **Thesis:** a 25-year category creator sold at about 10.6x synergised EBITDA, 7.5 months after publishing standalone targets. US credit revenue had shrunk 2% a year (2020–24) while every letter reported a "record".
   - **Why it's worth it:** a complete, documented arc in one place: founder succession, KPI drift, disclosure retreat, a debt-funded ASR, board reshaping, then the sale. Pair it with Tradeweb–Trumid as the mirror deal.
   - **Serves:** E3 (M&A), 02 (valuation: price the premium vs the targets), E4 (governance: Chair split, new directors), 04.
2. ***Open Trading vs 'select smart': both venues converged on curation***
   - **Thesis:** all-to-all wins in stress and in small or liquid tickets. Large illiquid trades get routed to curated dealers. Each venue's research proves whatever its product needs, measured against its own reference price.
   - **Why it's worth it:** it directly extends [[tradeweb-a2a-information-leakage]] with the opposing study (MKTX's *How trades move markets*, *Blockbusting* Part 2) plus the algo data: 88% of HG trades have an algo counterparty.
   - **Serves:** 07 (selection bias, self-benchmarking), 04 (counter-positioning), 03 (adverse selection, winner's curse).
3. ***Moving the goalposts: how MarketAxess reframed its KPIs as the core stalled***
   - **Thesis:** HG share became composite, then channels. Open Trading savings and penetration vanished. The "record" streak continued as fee per million fell 31%.
   - **Why it's worth it:** a reusable investor-relations lesson on reading a 10-K and letters skeptically, with every number traceable in this corpus.
   - **Serves:** 01 (read the scoreboard), E8 (investor relations), E7.
4. ***CP+ and TraX: the venue as data vendor, and why ICE wanted the flow***
   - **Thesis:** proprietary inquiry data, including quotes that did not trade, is the moat. S&P built its evaluated pricing on it, and ICE is the evaluator buying the flow.
   - **Why it's worth it:** strong, but it overlaps [[tradeweb-ai-price]] §4–5. **Recommend merging it as a section into that note** rather than writing a new one.
   - **Serves:** 07, E10 (AI and data strategy).
5. ***Concannon's experiment: importing equity microstructure into bonds***
   - **Thesis:** order book (2020), algos and Pragma (2023), Mid-X (2025), closing auctions (2025). Each import worked technically, adoption was the constraint, and the operator-CEO ended up selling.
   - **Why it's worth it:** a clean leadership-plus-strategy case. The auctions material has unusually candid quotes ("success will depend on adoption") and a Bloomberg skeptic.
   - **Serves:** E1, E5 (transformation at scale), 04, 09.
6. **Optional: *EM and international as the growth engine***
   - **Thesis:** half of revenue and +15% a year, driven by index inclusion, mandates (Brazil, India) and Open Trading at 40%+ in EM hard currency.
   - **Why it's worth it:** only if you want a Course 11 (Global strategy and macro) case. Otherwise one paragraph inside note 1 is enough.

**Not worth noting**
- **Regional AxessPoints and media reprints** (Argentina, MENA, Malaysia, Korea, Mexico): marketing color with event-volume numbers. One or two data points can feed note 6 or note 1. They are not standalone notes.
- **Monthly volume releases and routine earnings detail:** already summarised in the chronology and §5.
- **Munis, private banking (Axess IQ), repo and post-trade reporting (Sonar, SensAI):** real businesses, but peripheral to the market-structure lens. The *243 days late* reporting stat is a fun fact, not a note.
- **ESG, Trading for Trees, Diversity Dealer Initiative:** dropped by the company itself after 2023.
- **People profiles beyond McVey and Concannon:** fold the bench into note 1 or note 5. A standalone *MarketAxess people* note would mostly repeat titles.

---

## Method and verification

- **Reading.** Six parallel readers each read one slice in full: IR 2019–22, IR 2023–26, letters and decks, two research halves, and regional research. Their notes are in the scratchpad, not the repo. This digest was written from those notes plus spot checks.
- **Quote check.** Every string in straight double quotes in this file was checked by a script as a whitespace-normalised substring of `articles.jsonl` texts, and is 25 words or fewer. The result is appended below.
- **Data correction.** The ICE deal text was taken from the sibling ICE corpus because PDF extraction lost ligatures.

**Verification result (2026-10-25):** 70 straight-quoted strings checked, 70 found verbatim (whitespace-normalised) in `articles.jsonl`, all ≤25 words. Labels and note titles are in *italics*, not quotes.
