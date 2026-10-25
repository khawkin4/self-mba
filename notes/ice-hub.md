# Note · ICE hub — one founder's "analog to digital" playbook run across energy, clearing, the NYSE, mortgages and bonds, paid for by futures volatility and now buying the execution it couldn't build

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy — platform roll-ups, vertical integration), **Course 02** (Corporate Finance & Valuation — debt-funded M&A, adjusted vs GAAP), **Course 07** (Data, Analytics & Decision-Making — evaluated prices, benchmarks, self-graded accuracy), **Course 11** (Global Strategy & Macro — energy geopolitics, mandates), **E2** (Capital Allocation), **E3** (M&A), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Entry point for the eleven ICE notes; peer study to [[tradeweb-hub]]

- **Source:** ICE's investor-relations newsroom, **1,689 items from Jan 2 2019 to Oct 22 2026**, pulled through the Q4 JSON press feed from the browser, because ir.theice.com blocks `curl` with a Cloudflare challenge. Also used: **133 ice.com Insights / ICE Vox articles** (lens-filtered from ~770 in the sitemap), **29 "Inside the ICE House" podcast transcripts** (2018–2026), and the **seven Letters to Shareholders (2019–2025)**. **783 substantive items** were read in full (`_ingest/raw/ice/articles.jsonl`; index and skip reasons in `index.tsv`; corpus digest in `_ingest/raw/ice/DIGEST.md`). Excluded: 681 NYSE delisting notices, 151 statistics and volume releases, 72 monthly mortgage-data reports, and dividend, event, award and holiday items. Everything comes from ICE's own channels. The corpus has no sell-side research, press coverage or critics.
- **Core claim:** ICE runs one playbook, and Sprecher states it in so many words. Find a large, opaque, analog market. Give customers a stake or make them anchors. Buy into it during a crisis ("I've never been the low bidder"). Put it on ICE's technology and clearing. Then sell the data it throws off. The playbook was applied to OTC energy (2000), CDS clearing (2009), the NYSE (2013), mortgages (MERS → Simplifile → Ellie Mae → Black Knight, ~$25B, 2016–2023), and now fixed income. Between 2019 and 2026 the self-description dropped "exchange" (2021) and "market infrastructure" (2024) in favour of "technology and data". Revenue rose from $5.2B to $9.9B, the 20th straight record year in 2025. The record years still come mostly from futures and clearing volatility. The pattern breaks at bond execution: after seven years of building ICE Bonds, ICE agreed on **2026-07-30 to buy MarketAxess (~$5.7B EV, all debt)**. Tradeweb answered 81 days later with Trumid. As with Tradeweb, nearly every quality metric is ICE grading itself, here with its own evaluated price.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[ice-strategy-financials]] | A 20-year record-revenue compounder that alternates debt-funded mega-deals with deleveraging; adjusted metrics carry the "all-weather" story | FY18–1H26 financials, every deal and divestiture with price and multiple, buyback cycles, GAAP vs adjusted |
| [[ice-marketaxess-deal]] | The evaluator buys the flow: seven years of ICE Bonds, then $5.7B for the institutional network | Deal terms, ICE Bonds build history, CLOB vs RFQ, the Tradeweb–Trumid mirror deal, deal math |
| [[ice-fixed-income-data]] | An evaluated-pricing incumbency that grades the market, then sells the grade as execution, indices and AI feeds | CEP, Best Ex, indices/ETF stack, the "data-centric" thesis, accuracy claims, Compass and MCP |
| [[ice-benchmarks-iba]] | From LIBOR administrator to replacement-rate builder whose key inputs come from rivals' platforms | LIBOR wind-down, Term SONIA/SOFR waterfalls, Tradeweb data, Bank Yield Index, AMERIBOR, LBMA |
| [[ice-mortgage-technology]] | ~$25B for a life-of-loan chain bought at the top of the rate cycle, a bet on refi plus a data flywheel | Ellie Mae, Black Knight and the FTC, GAAP vs adjusted margins, rate-lock data → futures |
| [[ice-clearing-treasury]] | Clearing is where the franchise sits, and mandates are the entry wedge | CDS clearing, margin offsets, the FTX fight, U.S. Treasury clearing as challenger to FICC |
| [[ice-energy-benchmarks]] | The "technology and data" company still earns its record years from energy volatility, and wins benchmarks by moving the delivery point | Brent/Midland, HOU vs Cushing, Murban, TTF/JKM, carbon, GPU-compute futures |
| [[ice-nyse-listings-digital]] | The NYSE is ~10% of revenue but the brand and political front door; it carried ICE from "regulated-only" crypto to on-chain markets | Pillar, the floor, 22-hour trading, NYSE Texas, Bakkt → Polymarket/OKX/tokenized NYSE |
| [[ice-people]] | A founder-led bench that speaks the founder's script; 26 years at the top, no named successor | Org chart over time, dated quotes, view shifts, succession |
| [[ice-outside-voices]] | Friendly rivals, regulators and deal counterparties on ICE's own stage; the useful lines are the few that push back | Duffy, Behnam, Broeksmit, Wigglesworth, Lutnick; who holds power over ICE |
| [[ice-mission-forces]] | The playbook never changed; the noun did (exchange → data → technology), while volatility, mandates and the rate cycle did the work | Mission lines, boilerplate drift, tailwinds and headwinds, forces map, crisis tests, 2030 scenarios |

**Suggested order:** people → mission-forces → strategy-financials → marketaxess-deal → fixed-income-data → benchmarks-iba → clearing-treasury → mortgage-technology → energy-benchmarks → nyse-listings-digital → outside-voices. Read it alongside [[tradeweb-hub]]. The two companies meet in credit, Treasuries, benchmarks and reference prices.

## 2. Timeline, 2000 → 2026

*Pre-2019 events come from ICE's own retellings: podcasts, the letters and release backgrounders. They were not checked against contemporaneous sources. 2019–2026 events come from the theme notes, which cite the articles.*

| Year | Event | Why it matters |
|---|---|---|
| 2000 | ICE founded in Atlanta as an electronic OTC energy market. Per Sprecher, about 80% of the equity was given to customers in exchange for order flow ([[ice-people]]). | Customer ownership as the bootstrap. The model was reused in clearing and with Bakkt. |
| 2001–02 | Enron Online collapses, and ICE becomes the "neutral counterparty". It buys the IPE (Brent) "for double". | Luck plus readiness. Brent becomes the franchise. |
| 2005 | IPO. Market cap about $1B (2024 letter). | — |
| 2007 | Loses the Chicago Board of Trade bidding war to CME (Sprecher had the offer "slip under the door" of the CBOT CEO). | Duffy says the bid made CME pay more ([[ice-outside-voices]]). |
| 2009 | CDS clearing, after Geithner's "big barn" invitation ([[ice-clearing-treasury]]). | Mandates as the entry wedge. |
| 2013 | Buys NYSE Euronext and later spins off Euronext (the spin-off is context, not from ICE corpus). The NYSE is rebuilt on Pillar. | The brand, and a "mess" rebuilt from scratch. |
| 2015–17 | Interactive Data (IDC), S&P securities evaluations, the BofA indices, MERS. | The fixed-income data and mortgage beachheads. |
| 2018 | BondPoint and TMC acquired. Bakkt founded. | The execution and crypto bets begin. |
| **2019** | ICE Bonds launched. Simplifile ($335M). MOVE index. **Tradeweb ICE Treasury Closing Prices.** Bakkt bitcoin futures. ETF Hub. ICE Futures Abu Dhabi announced. | The building year. |
| 2020 | eBay approach dropped within 48 hours. COVID floor closure. **Ellie Mae, $11B.** Record Q1. | Mortgage becomes a segment. |
| 2021 | "Exchange" drops out of the descriptor (first seen Mar 29). Gardiner becomes CFO. Bakkt is SPAC'd and deconsolidated. The Coinbase stake is sold. LIBOR end dates are set. Term SONIA launches with Tradeweb data. Leadership reshuffle in December. | The identity pivot. |
| 2022 | **Black Knight agreed at $13.1B**, and buybacks are suspended. ICE Term SOFR launches with Tradeweb as its first input. The FTX clearing fight at the CFTC. | The biggest bet. |
| 2023 | The FTC sues. Black Knight is repriced and closes at ~$11.9B, with two divestitures to Constellation. Edmonds is named to run FIDS. | Antitrust cost. |
| 2024 | "Market infrastructure" drops out of the descriptor. **ICE Bonds–MarketAxess network link.** USD LIBOR ends. The AI Center of Excellence is ICE creating "an R&D department for the first time". | Prelude to the deal. |
| 2025 | AFX/AMERIBOR. NYSE Texas. Buybacks resume. Treasury clearing rulebook published. **Polymarket, up to $2B.** FY revenue $9.9B, the 20th straight record. | The crypto reversal begins. |
| H1 2026 | **Treasury clearing live (Feb 3).** NYSE tokenized platform. OKX stake. Record January (245.8M contracts). Compass (AI pre-trade analytics). GPU-compute futures. Bond data delivered over MCP. | "On-chain" and AI narratives. |
| **Jul 30 2026** | **ICE agrees to buy MarketAxess**: $167/sh cash, ~$5.7B EV, close expected H1 2027 ([[ice-marketaxess-deal]]). | The evaluator buys the flow. |
| Oct 19 2026 | (Tradeweb corpus) Tradeweb agrees to buy Trumid for ~$1.97B ([[tradeweb-hub]]). | Credit e-trading consolidates into two vertical stacks. |

## 3. Five patterns across the notes

1. **One playbook, stated by the CEO.** The pattern is analog market → anchor customers → crisis-timed purchase → ICE tech and clearing → data. It appears in energy (IPE, Murban/ADNOC, HOU), clearing (CDS, then Treasuries), the NYSE (an acqui-hire rebuild), mortgages (the robo-signing-era MERS, then the high-rate-trough Black Knight) and fixed income. Sprecher's rule: “it's easier to start a new initiative and have market acceptance of your initiative during periods of stress.” (2024-08-12). **Where it failed:** Bakkt's futures, the CBOT bid, the eBay idea, the ICE Bank Yield Index, organic bond execution. See [[ice-people]] and [[ice-strategy-financials]].
2. **Regulation is the door, and ICE says so.** CDS clearing came from Geithner's "barn". Treasury clearing came from the SEC mandate; Edmonds: “I don't believe without the regulatory catalyst that we would have made the decision to enter that.” (2026-01-14). LIBOR's death created the IBA replacement-rate line, and best-execution and liquidity rules generate data products. ICE also lobbies against rules that would shrink its markets: EU gas price caps, position limits, parts of the SEC equity package. See [[ice-clearing-treasury]], [[ice-benchmarks-iba]], [[ice-energy-benchmarks]]. Compare Tradeweb's same pattern in [[tradeweb-derivatives-regulation]].
3. **The evaluator grades the market.** ICE's Continuous Evaluated Pricing is the yardstick for its own portfolio-trade studies, its best-execution product, its ETF fair-value claims and its auction prices. ICE says its accuracy improved (38% IG / 79% HY "closer to the next trade" since 2018) but publishes no absolute error, and its disclaimer admits it lacks some trade data and dealer quotes. Tradeweb does the same with Ai-Price ([[tradeweb-ai-price]]). Before quoting any ICE number, ask "measured how, against whose price?" See [[ice-fixed-income-data]].
4. **The noun drifts; the cash engine doesn't.**
   - The descriptor runs "operator of global exchanges and clearing houses" (2019) → "data, technology and market infrastructure" (2021) → "technology and data" (2024) → "financial market technology and data powering global capital markets" (2026).
   - ESG rises (2019–22) and vanishes (2024–25 letters).
   - Crypto flips from "regulated-only" to OKX and tokenized NYSE equities.
   - The quarters that set records are energy and rates volatility (energy revenue +46% in 1Q26, −13% in 2Q26). See [[ice-mission-forces]], [[ice-energy-benchmarks]], [[ice-nyse-listings-digital]].
5. **Adjusted metrics carry the "all-weather" story.**
   - Twenty straight record-revenue years and 58–61% adjusted operating margins.
   - FY22 GAAP EPS fell 64% on Bakkt.
   - Mortgage Technology posted GAAP segment losses in many post-Black Knight quarters against 35–43% adjusted margins; the gap is acquired-intangible amortization.
   - Each mega-deal is debt-funded, and buybacks pause until leverage returns. For MarketAxess the leverage path is 3.4x → ≤3.0x. See [[ice-strategy-financials]], [[ice-mortgage-technology]].

## 4. ICE and Tradeweb: where the two studies meet

| Topic | ICE side | Tradeweb side |
|---|---|---|
| Reference prices | CEP plus evaluations (an SEC-registered RIA). Relative accuracy claim. Buying MarketAxess CP+ | Ai-Price, a ~30% improvement over last print ([[tradeweb-ai-price]]) |
| Benchmarks | IBA's Term SONIA and Term SOFR, Treasury closing prices, CMT and inflation ICE Swap Rate all **use Tradeweb data** ([[ice-benchmarks-iba]]) | Tradeweb data became a benchmark input after the March 2020 ICE Swap Rate failure ([[tradeweb-derivatives-regulation]]) |
| Credit protocol | CLOB, click-to-trade and sessions. RFQ "leaks" (Jackson, 2018; ICE Bonds, 2025) | All-to-all broadcast leaks; "select smart" ([[tradeweb-a2a-information-leakage]]) |
| Consolidation | MarketAxess, Jul 30 2026 | Trumid, Oct 19 2026 ([[tradeweb-strategy-financials]]) |
| Treasury clearing | The CCP: ICE Clear Credit, live Feb 2026 | The venue: execution flow pushed by the mandate |
| Shared people | Michael Blaugrund (ex-Tradeweb), NYSE COO 2019 and ICE tokenization lead 2026 | Lee Olesky and Lisa Schirf quoted in ICE releases (2019–20) |

**Correction flagged, not applied:** [[tradeweb-ai-price]] says ICE "publishes no figure" for CEP accuracy. ICE does publish a relative improvement figure ([[ice-fixed-income-data]]). It publishes no absolute error.

## 5. Cross-note open questions

1. **MarketAxess close:** the shareholder vote, antitrust review alongside Tradeweb–Trumid, and whether S&P's CP+ licence survives the change of control ([[ice-marketaxess-deal]]).
2. **Mortgage payoff:** does Mortgage Technology's GAAP margin turn durably positive as prepayments rise (a four-year high in 2026), or does credit stress (foreclosure inventory at a six-year high) arrive first ([[ice-mortgage-technology]])?
3. **Treasury clearing share:** how much cash and repo flow does ICE Clear Credit win before the Dec 31 2026 and Jun 30 2027 mandates, and do the deadlines slip ([[ice-clearing-treasury]])?
4. **On-chain execution:** does the NYSE tokenized venue launch in H2 2026 as promised? Does OKX distribution of NYSE tokenized equities get regulatory approval ([[ice-nyse-listings-digital]])?
5. **Independent rulers:** will ICE or anyone else publish CEP's absolute error against a third-party price, side-matched and out of sample ([[ice-fixed-income-data]])?
6. **Succession:** Sprecher is in year 26, with no named successor ([[ice-people]]).
7. **Q3 2026 results:** is the 2Q26 energy decline (−13%) a blip, and what pro-forma leverage does ICE report?

**Links:** [[ice-strategy-financials]] · [[ice-marketaxess-deal]] · [[ice-fixed-income-data]] · [[ice-benchmarks-iba]] · [[ice-mortgage-technology]] · [[ice-clearing-treasury]] · [[ice-energy-benchmarks]] · [[ice-nyse-listings-digital]] · [[ice-people]] · [[ice-outside-voices]] · [[ice-mission-forces]] · [[tradeweb-hub]] · [[tradeweb-ai-price]] · [[tradeweb-credit]] · [[tradeweb-derivatives-regulation]] · [[marketaxess-hub]] · [[spglobal-hub]] · [[bloomberg-hub]] · [[lseg-hub]] · [[market-structure-24-5-trading]] · [[wss-capital-markets-ma]] · [[wss-rates-macro]] · [[canon-helmer-7-powers]] · [[canon-porter-competitive-strategy]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-shapiro-varian-information-rules]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
**(a) Two credit deals side by side.**
- ICE pays ~$5.7B EV for MarketAxess at ~10.6x LTM EBITDA, pro forma for full synergies.
- Tradeweb pays ~$1.97B for Trumid ([[tradeweb-hub]]).
- Compute ICE's price as a share of its own FY25 net revenue ($9.9B) and of FY25 adjusted free cash flow ($4.2B).
- *(Answer: 5.7/9.9 ≈ **58%** of a year's revenue; 5.7/4.2 ≈ **1.36 years** of adjusted FCF.)*
- In one paragraph, say which buyer is taking more balance-sheet risk relative to size, and what that implies about how badly each wanted the asset.

**(b) The descriptor test.**
- List ICE's five self-descriptions (§3, pattern 4) with dates.
- For each, name the acquisition or strategic move that preceded it within 12 months.
- *(Answer sketch: Ellie Mae → "mortgage technology" (Aug 2020); Ellie Mae and the Bakkt deconsolidation → "data, technology and market infrastructure" (Mar 2021); the Black Knight close → "technology and data" (first seen 2024-01-16); Polymarket and the tokenized NYSE → "financial market technology and data powering global capital markets" (first seen 2026-03-05, the OKX release). Earnings releases were still using "technology and data" on 2026-07-30; see [[ice-mission-forces]].)*
- Then argue whether the label drives the valuation multiple ICE wants, or follows the business mix.

**(c) Board memo.**
- Write one page as an ICE independent director, on whether to approve MarketAxess.
- Use pattern 1 for the logic and pattern 5 for the financing risk, plus the three facts from §5 you would require.
- Compare your memo with what ICE discloses in its Q3 2026 results and the merger proxy.

**Corpus refresh:** ir.theice.com blocks `curl`. Load any IR page in the browser and run `fetch('/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=2&pressReleaseDateFilter=3&categoryId=00000000-0000-0000-0000-000000000000&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=YYYY&excludeSelection=1')`. ice.com pages and `sitemap.xml` download fine with `curl`.
