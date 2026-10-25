# Note · BlackRock as the anchor client — venues plug into Aladdin, not the other way round; the buy side's biggest order book now sets the terms of electronification

> Market-structure / power note · Maps to **Course 04** (Competitive Strategy: buyer power, five forces), **Course 03** (Microeconomics & Strategy Foundations: coopetition, bargaining), **Course 06** (Operations: post-trade, execution cost), **Course 10** (platforms), **E10** (Digital & AI Transformation) · Written 2026-10-25 · Companion to [[blackrock-hub]], [[blackrock-aladdin-data]], [[tradeweb-credit]], [[tradeweb-outside-voices]]

- **Source:** `_ingest/raw/blackrock/articles.jsonl`, read in full. Used here:
  - the 2020 and 2022 Fink shareholder letters (the bond-ETF and intermediary passages);
  - the 2021 ETF post-trade release and the 2022 bond-ETF forecast release;
  - the 2023 and 2025 Investor Day decks (execution and internalization slides);
  - the Texas Stock Exchange statement (2024);
  - four Tradeweb releases copied from the Tradeweb corpus: Aladdin phase 1 (2022-12) and phase 2 (2023-12), the Securitize round (2024-05), and Mexican repo (2025-11).
- **Core claim:**
  - **Who adapts to whom.** BlackRock is the largest buy-side user of every bond and ETF venue, but the integration runs one way. Tradeweb wires its protocols into **Aladdin's order and execution management system (OEMS)**, and BlackRock's own documents never name Tradeweb.
  - **One repeated move.** Over 2021–2025 BlackRock does the same thing to every concentrated supplier: it splits the supplier, multi-sources, funds an alternative, or internalizes the flow. That covers ETF custodians (one bank became four), proxy advisers (Egan-Jones added), exchanges (a founding stake in TXSE), dealers (*multiple intermediaries*) and venues (internal crossing).
  - **Bond ETFs are the demand-side engine.** They create the baskets that pushed dealers into algorithmic pricing and portfolio trading, the business Tradeweb and MarketAxess monetize.
  - **Evidence quality.** The direction is well evidenced. How much BlackRock's leverage is worth in fees or terms is *never disclosed*.

---

## 1. Chronology: BlackRock and market plumbing

| Date | Event | Source | Read |
|---|---|---|---|
| 2019-04-08 | Fink: Aladdin to be "the language of portfolio construction" for wealth managers. A Trading and Liquidity Strategies team lobbies on market structure | 2019 shareholder letter | Aladdin positioned as a standard, not a product |
| 2020-03-30 | During the COVID crash, Fink writes the bond-ETF passage (§2): ETFs as price discovery for frozen bonds | 2020 shareholder letter | Demand-side case for electronification |
| 2020-05-11 | PNC sells its 22% stake; BlackRock buys back $1.1B | IR release | Ends bank-affiliate ownership; nothing ties BlackRock to one dealer group |
| 2021-12-07 | **US iShares post-trade servicing split**: State Street alone → State Street, BNY Mellon, Citi, JPMorgan ($2.3T; ~2-year RFP; 18-month transition) | IR release | Buyer power over custodians, framed as "concentration risk" |
| 2022-03-24 | Scale lets BlackRock "diversify our service providers" across "multiple intermediaries" | 2022 shareholder letter | The same move, stated for dealers |
| 2022-05-18 | Forecast: global bond ETFs **$5T by 2030** (from $1.7T, ~2% of a $124T bond market); IG e-trading share 36% (Mar 2022) vs 21% (early 2019) | Newsroom | ETFs tied explicitly to electronification |
| 2022-12-06 | **Tradeweb × Aladdin phase 1**: multi-year integration of Tradeweb credit trading and data into the Aladdin OEMS. Ai-Price (~25k bonds), Liquidity Score and dealer axes appear inside Aladdin | Tradeweb release | The venue enters BlackRock's workflow |
| 2023-06-14 | Investor Day: *25% savings in execution costs* vs a market average (slide caption, reassembled from fragmented slide text); 6,600 fixed income trades a day; target to triple iShares fixed income ETFs to $2.5T by 2030 | 2023 deck | Execution scale sold as a client benefit |
| 2023-12-11 | **Phase 2**: Aladdin credit users get **AllTrade** all-to-all, Rematch and Tradeweb Direct; RFQ and AiEX "next" | Tradeweb release | Tradeweb's anonymous liquidity is reachable from Aladdin |
| 2024-05-01 | BlackRock leads Securitize's $47M round; **Tradeweb co-invests** | Tradeweb release | Venue and anchor client share a tokenization rail ([[blackrock-digital-assets]]) |
| 2024-06-05 | **Founding investor in the Texas Stock Exchange** | Newsroom statement | The buy side funds a new exchange |
| 2024-06-11 | Egan-Jones added to Voting Choice as a third proxy adviser | Newsroom | Multi-sourcing for governance plumbing ([[blackrock-stewardship-backlash]]) |
| 2025-06-12 | Investor Day: *25% of equity trades offset in 2024 for clients* (slide text, reassembled); "~$600 million in transaction costs saved for clients in 2024 via internalization"; Systematic: "Decrease reliance on external liquidity providers" | 2025 deck | Internalization is the counter-signal for venues |
| 2025-11-12 | First electronic **Mexican repo** market on Tradeweb: BlackRock is the first client (via Aladdin), Santander the first dealer | Tradeweb release | The anchor-client template exported to EM repo |

## 2. Bond ETFs as plumbing, in BlackRock's words

- 2020-03-30 (Fink): "The biggest transformation we have seen so far is in fixed income, where ETFs are transforming and modernizing the $100 trillion bond market itself."
- 2020-03-30 (Fink): "The need to price and trade large baskets of bonds has pushed the industry to develop algorithms that can price thousands of bonds simultaneously"
- 2020-03-30 (Fink): "ETFs are serving as tools for price discovery and delivering incremental liquidity and value."
- 2021 shareholder letter (Fink): bond ETFs let investors avoid "a legacy marketplace that remains fragmented and comparatively difficult to access."
- 2022-05-18 (newsroom): "the growth of bond ETFs and their ecosystem has helped drive advances in electronic trading and algorithmic pricing of individual bonds"
- 2022-05-18 (Salim Ramji): bond ETFs "have become the catalyst of a more modern, more digital and more transparent bond market."
- 2023-03-15 (Fink): "We believe that bond ETFs will continue to catalyze advances in fixed income market structure"

**The mechanism** (ties to [[tradeweb-credit]] §5 and [[tradeweb-equities-retail]]):
- ETF creation and redemption needs dealers to price *baskets*. Baskets reward algorithmic pricing and the portfolio-trading protocol.
- PT rose from ~1% of TRACE in early 2019 to 11.4% by Dec 2024 (figures from the Tradeweb notes).
- iShares is the largest issuer: 8 of the 10 most liquid fixed income ETFs (2023 and 2025 decks, Bloomberg data). So BlackRock's product line produces much of the order flow the venues compete for.

## 3. Aladdin as the distribution chokepoint

What the integration gives each side, using only the releases:

| Party | Gets | In their words |
|---|---|---|
| Tradeweb | Distribution to Aladdin's institutional users without a separate front end | Elisabeth Kirby (2023-12-11): "leveraging the Aladdin platform’s extensive OEMS capabilities and broad institutional client base to create greater liquidity, connectivity and transparency across our markets." Chris Bruner (2022-12-06): "this integration will provide its users with more efficient access to our suite of protocols." |
| Aladdin / BlackRock | Venue data (Ai-Price, liquidity scores, axes) and A2A liquidity inside its own screen; a richer OEMS to sell to third parties | Kamya Somasundaram (2022-12-06): "Credit markets have grown increasingly electronic in recent years, but significant opportunities still exist to accelerate this trend" |
| Common clients | Fewer screens; Tradeweb's "AllTrade made up 32% of in-comp RFQ for High Grade credit and 44% for High Yield credit" (2023-12-11) | — |

**Asymmetry:**
- The Tradeweb releases cite Aladdin's "client base". BlackRock's 13 Fink letters, 3 AGM transcripts and 5 decks **never name Tradeweb**.
- Only one trading venue is named anywhere in BlackRock's own documents, and only as an identity-checking example: "Trade venues like NYSE and MarketAxess manage to do the same for buying and selling securities." (2025-03-31)
- *Inference:* each venue needs Aladdin more than Aladdin needs that venue, because Aladdin can multi-home across venues. In Pfeffer's terms, dependence equals importance times the lack of alternatives ([[tradeweb-outside-voices]] §5 scores BlackRock high on both).

## 4. The multi-sourcing pattern

| Supplier market | Concentration before | BlackRock's move | Stated reason |
|---|---|---|---|
| ETF custody / fund admin | State Street, sole provider for US iShares | Four providers (2021) | Derek Stein: "which will help us scale the iShares franchise and mitigate concentration risk." |
| Dealers | Bank balance sheets shrinking (2020 letter) | "multiple intermediaries and better technology" (2022) | Efficiency |
| Proxy advice | ISS / Glass Lewis duopoly (context) | Egan-Jones as third adviser (2024); 2023 letter calls for "more proxy advisors" | Client choice |
| Exchanges | NYSE / Nasdaq duopoly (context) | Founding stake in TXSE (2024) | "to increase liquidity and improve market efficiency for BlackRock’s clients and other investors in the U.S. capital markets." |
| External liquidity | Dealers and venues | Internal crossing: 25% of equity trades offset (2024) | "Decrease reliance on external liquidity providers, reduce information leakage, and lower trading costs" (2025 deck) |

## 5. What the claims don't prove

1. **The 25% execution-cost saving (2023) is self-measured.** The benchmark is "previous day’s closing price" plus a half-spread from "a consensus opinion of BlackRock traders as well as a set of over 10 broker dealers" (2023 deck footnote). No third-party TCA is in the corpus.
2. **The ~$600M saved through internalization (2024)** is unbenchmarked. There is no method, no split between equity and fixed income, and no estimate of information-leakage avoided.
3. **No economics for the Tradeweb deal.** Neither side discloses fees, exclusivity or volume routed. "Multi-year partnership" is the only term.
4. **Post-trade split outcomes are absent.** There are no later releases on cost or service-level results.
5. **The TXSE stake's size is not disclosed.** Nor is any order-routing commitment.
6. **Bond-ETF forecasts are the issuer talking its book.** BlackRock forecasts $5T in industry bond-ETF AUM (2022) and a $2.5T iShares target (2023, set from $1.6T at the time, roughly a tripling). By 2025 the deck instead projects *2x+* growth in global fixed income ETF AUM to 2030, and does not restate the $2.5T iShares target.

## 6. Strategic read (inference — not BlackRock's words)

- **The OEMS is a toll road the venues pave.** Tradeweb pays in integration work and data (Ai-Price on Aladdin screens). That makes Aladdin more valuable to its 1,000+ clients (Preqin release, 2024), which raises Aladdin's leverage over the *next* venue negotiation.
- **The same flywheel as Bloomberg's terminal, from the other side.** Bloomberg owns the screen and runs a venue. BlackRock owns the screen and is the largest order book. Expect venues to court Aladdin the way dealers court Bloomberg. See [[bloomberg-hub]].
- **Internalization squeezes venues from below.** As BlackRock crosses more flow internally (equities first, "electronic credit" next in the Systematic slide), the external flow that remains is the harder, more information-sensitive part. That is good for curated RFQ (Tradeweb's *select smart* turn) and bad for broadcast.
- **Consolidation changes the bargaining.** Tradeweb buying Trumid and ICE buying MarketAxess (context from [[tradeweb-hub]]) reduces BlackRock's outside options in US credit. That is the first shift in a decade that strengthens venues against the anchor client. See [[ice-hub]], [[marketaxess-hub]].

## 7. Canon lenses

- **Five forces** ([[canon-porter-competitive-strategy]]): textbook buyer power. BlackRock is concentrated, its purchases are large relative to each supplier, switching costs are low (multi-homing), and it can credibly integrate backward (internalization, TXSE).
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Tradeweb is complementor (Aladdin integration), co-investor (Securitize) and, through internalization, a potential competitor for the same flow.
- **Power** ([[canon-pfeffer-power]]): dependence = importance × lack of alternatives. Multi-sourcing deliberately lowers BlackRock's own dependence on every supplier.
- **Platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): Aladdin becomes a multi-sided platform once venues, data vendors (Preqin, Clarity AI) and custodians plug in. Whoever owns the workflow captures the network value.
- **Information goods** ([[canon-shapiro-varian-information-rules]]): putting venue data inside the OEMS raises switching costs for *clients* while lowering them for BlackRock.

## 8. Practitioner counterpoint

- **For BlackRock:** multi-sourcing is ordinary vendor risk management, and the regulators' worry about single points of failure in ETF servicing is real. Tradeweb chose the integration, and phase 2 widened it, so Tradeweb must see net value. Clients get fewer screens.
- **Against:** a manager with this much flow that also owns the workflow software and crosses trades internally can tilt routing toward whichever venue gives better data terms. That is a quiet conflict inside the Aladdin user/provider model. The corpus has no disclosure on how Aladdin routes orders for third-party clients versus BlackRock's own.
- **Both:** a credit desk deciding venue share should measure fill rates and slippage by venue *through* the OEMS, with a third-party mid. It should not assume an integrated venue is the cheapest.

## 9. Open questions to track

1. Did the "next" phase, direct RFQ and AiEX from Aladdin (promised 2023-12), go live? Check Tradeweb releases 2024–26.
2. Does Aladdin integrate MarketAxess, Bloomberg or Trumid protocols on similar terms? Search the sibling studies ([[marketaxess-hub]], [[bloomberg-hub]]).
3. What share of BlackRock's credit flow is internally crossed by 2027? Watch whether "electronic credit" internalization appears in the next Investor Day.
4. Does BlackRock route flow to TXSE after its 2026 launch?
5. Do the ICE–MarketAxess and Tradeweb–Trumid deals change Aladdin's integration terms?

**Links:** [[blackrock-hub]] · [[blackrock-aladdin-data]] · [[blackrock-digital-assets]] · [[blackrock-mission-forces]] · [[blackrock-outside-voices]] · [[tradeweb-hub]] · [[tradeweb-credit]] · [[tradeweb-equities-retail]] · [[tradeweb-ai-price]] · [[tradeweb-outside-voices]] · [[tradeweb-mission-forces]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[bloomberg-hub]] · [[marketaxess-hub]] · [[ice-hub]] · [[canon-porter-competitive-strategy]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-pfeffer-power]]

---
### Rep
**You are BlackRock's global head of credit trading.**

**(a)** Use the Tradeweb phase-2 figures (AllTrade = 32% of in-comp HG RFQ, 44% of HY) and BlackRock's 6,600 fixed income trades a day (2023 deck). Assume 40% of those are credit and 30% of credit trades are routed to Tradeweb. How many trades a day reach AllTrade if Tradeweb's in-comp mix holds for BlackRock (HG:HY = 3:1)?
*Answer:* 6,600 × 0.4 × 0.3 = 792 credit trades to Tradeweb. Of those, 594 are HG × 0.32 ≈ 190 and 198 are HY × 0.44 ≈ 87. That is **≈277 a day**.

**(b)** You can internalize 10% more of credit flow, saving 2bp per trade on a $5mm average ticket. What is the annual saving, over 250 days?
*Answer:* 6,600 × 0.4 × 0.10 = 264 trades. 264 × $5mm × 0.0002 = $264k a day, so **≈$66M a year**.

**(c)** In one paragraph, weigh that against the information Tradeweb loses, and explain what you would ask Tradeweb for in the next integration phase.

---
**Sources:**
- [2020 Chairman's letter (SEC DEFA14A), 2020-03-30](https://www.sec.gov/Archives/edgar/data/1364742/000119312520091041/d902903ddefa14a.htm)
- [2021 Chairman's letter, 2021-04](https://www.blackrock.com/corporate/investor-relations/2021-larry-fink-chairmans-letter)
- [ETF post-trade diversification, 2021-12-07](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2021/BlackRock-Strengthens-ETF-Operating-Platform-by-Diversifying-Post-Trade-Service-Providers/default.aspx)
- [2022 Chairman's letter, 2022-03-24](https://www.blackrock.com/corporate/investor-relations/2022-larry-fink-chairmans-letter)
- [Bond ETFs to $5T, 2022-05-18](https://www.blackrock.com/corporate/newsroom/media/press-releases/blackrock-projects-global-bond-etf-assets-to-reach)
- [Tradeweb × Aladdin phase 1, 2022-12-06](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-announces-partnership-with-blackrock-to-further-electronify-corporate-bond-market/)
- [2023 letter, 2023-03-15](https://www.blackrock.com/corporate/investor-relations/2023-larry-fink-annual-chairmans-letter)
- [Investor Day 2023, 2023-06-14](https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BlackRock-2023-Investor-Day.pdf)
- [Tradeweb × Aladdin phase 2, 2023-12-11](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-enters-next-phase-of-partnership-with-blackrock/)
- [Securitize round, 2024-05-01](https://www.tradeweb.com/newsroom/media-center/news-releases/securitize-announces-$47-million-strategic-funding-round-led-by-blackrock/)
- [TXSE investment, 2024-06-05](https://www.blackrock.com/corporate/newsroom/announcement/investment-in-texas-stock-exchange)
- [2025 letter, 2025-03-31](https://www.blackrock.com/corporate/investor-relations/2025-larry-fink-annual-chairmans-letter)
- [Investor Day 2025, 2025-06-12](https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf)
- [Mexican repo, 2025-11-12](https://www.tradeweb.com/newsroom/media-center/in-the-news/santander-and-blackrock-launch-the-first-electronic-market-for-mexican-repo-in-collaboration-with-tradeweb/)
