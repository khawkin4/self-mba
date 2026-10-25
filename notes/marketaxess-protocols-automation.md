# Note · MarketAxess protocols & automation — Concannon imported equity microstructure into bonds; every protocol shipped, adoption was the constraint

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — protocol breadth vs workflow depth, imitation vs fit), **Course 06** (Operations — automation, platform rebuilds, throughput), **Course 03** (Microeconomics — auctions, two-sided liquidity, dealer economics), **E5** (Transformation & Change Management at Scale — the five-year rebuild), **E10** (Digital & AI Transformation — algos, AI dealer selection), **E1** (Leading at Scale — an operator-CEO's playbook) · Written 2026-10-25 · Part of [[marketaxess-hub]]; companions [[marketaxess-open-trading]], [[marketaxess-strategy-financials]], [[tradeweb-credit]]

- **Source:** MarketAxess corpus (`_ingest/raw/marketaxess/articles.jsonl`), about **45 items** used: 12 product and partner news releases (Live Markets 2019 → Mid-X 2025 → auctions 2025), 14 earnings releases (2021–3Q26, narrative only), the FY2020–FY2025 letters, the 2021 Investor Day and Dec 2025 Goldman Sachs decks, and about 15 Knowledge Center pieces on automation, blocks, PT, Mid-X and auctions (including Bloomberg, The TRADE, Markets Media and WatersTechnology reprints). Range **May 2019 – Oct 2026**. Caveats: there are **no standalone releases for the X-Pro launch (2023) or the PT launch (2019)**; they appear only in letters and earnings text. Several Knowledge Center dates are estimates. **No volumes are ever disclosed for Live Markets, Adaptive Auto-X or the auctions.** No call transcripts.
- **Core claim:** Chris Concannon (ex-Bats/Cboe; President & COO from Jan 2019, CEO from Apr 2023) brought exchange and ETF microstructure to an RFQ venue: a **central limit order book** (Live Markets, announced May 2019 for 2H19, launched summer 2020), **portfolio trading** (announced for autumn 2019; only *more than 50* trades by Jun 2021; **$92B** in 2022), **algorithmic execution** (Adaptive Auto-X 2023, **Pragma** bought Oct 2023), **mid-point matching** for dealers (Mid-X, relaunched in US credit Sep 2025), **targeted block RFQ** (late 2024) and **opening & closing auctions** (Nov 2025). Every one of them shipped. Most shipped late, and the ones with disclosed adoption grew mainly where **dealers** wanted them (Mid-X, dealer RFQ) or where they rode existing RFQ flow (Auto-X: **28%** of credit trade count but only **11%** of volume in FY25). The rebuild behind it, promised as a *fully redesigned trading experience* for **1Q22**, became X-Pro (2023), a *build* year (2024) and *still have work to do* (FY25), and needed a new CTO (2026). Meanwhile the GS deck admits US credit revenue shrank **2% a year** over 2020–24. Tradeweb took share by wiring the workflow around the existing RFQ (net spotting, early PT; [[tradeweb-credit]]) rather than by adding protocols.

---

## 1. Chronology — protocol by protocol: promised vs delivered vs adopted

Figures as MarketAxess states them unless marked *derived*.

| Protocol (import from) | Announced / promised | Actually live | Adoption metric MKTX discloses | Volume disclosed? |
|---|---|---|---|---|
| **Live Markets CLOB** (equity order book) | 2019-05-09: "expected to launch in the second half of 2019" | "Launched in the summer of 2020" (~1 year late); UST version later; *Live Markets Match* (CP+-range matching) | Market makers: **Goldman** (Oct 2020), **Barclays** (May 2021), one unnamed systematic firm, **Flow Traders** (HY, Dec 2021). Hedge fund interactions +275% since launch. Embedded in **BlackRock Aladdin** (Sep 2024) | **Never** |
| **Portfolio trading** (ETF-style basket risk transfer) | 2019-06-19: "expected to launch in the Autumn of 2019" | Real release "late-May" 2021 | Jun 2021: "more than 50 portfolio trades" (17 investors, 9 dealers). $29B (2021) → **$92B** (2022, ~31% of e-traded PT in 4Q22). Share of US HG+HY PT: **20.0%** (3Q24) → **16.2%** (4Q24) → **19.0%** (FY25) → **21%** (4Q25). PT ADV $1.4B (FY25), record **$2.0B** (2Q26) | Yes, from 2021 |
| **Auto-X RFQ** (rules-based auto-execution) | 2018 launch | 2018 | 17% of tickets (Q2 2021); ~20% of credit trade count (2022); "nearly 10%" of volume (2023 YTD); **28% of trade count / 11% of volume** (FY25); 261 clients; power users at **92%** (HG) / **74%** (HY), vs 32% / 9% in 2018 | Partly (shares, cumulative $) |
| **Adaptive Auto-X** (smart order router / parent order) | 2021 Investor Day: "Encouraging clients to leave the parent order with MarketAxess" | Pilot Q1 2023 (CP+ Peg); first client algo trade Jun 2023; Europe pilot 2026 | None beyond *first trade*; in Aladdin Sep 2024 | **Never** |
| **Pragma** (equity/FX algo engine) | Agreed 2023-08-07 | Closed 2023-10-02 | $31.7M of revenue in 2024 (its commissions are driven by equities, per 1Q25); becomes "the backbone of our entire system" (Tait, 2025) | n/a |
| **Mid-X** (IDB-style mid-point matching) | Launched 2020 (FY20 letter); relaunch on Pragma promised for 2Q25 (FY24 letter) | EM/Eurobonds 2024; **US credit Sep 2025** | EM/Euro 2Q25 +70% YoY; US "exceeded 2bn printed" (Dec 2025); >**$3B** in Dec 2025 alone; ADV **+168%** (Q1 2026); 60+ dealer firms, up to 6 sessions a day | Partly |
| **Dealer RFQ / DealerAxess** (dealer-to-dealer via OT) | — | DealerAxess late Q1 2024 | Dealer RFQ ADV $1.2B (2024), $1.8B (1Q25); dealer-initiated ADV **$1.7B** (FY25, +33%), record $1.9B (1Q26) | Yes |
| **Targeted block RFQ** (block desks, curated) | *Block Trading* on the 2021 Investor Day slide | Oct–Nov 2024 (EM/Euro); US credit 2Q25 | Block ADV **$5B** (FY25, +24%), record **$6.6B** (1Q26, +35%), $5.4B (3Q26); US block e-penetration est. **10–20%** (GS deck) | Yes |
| **Targeted Axes** (disclosed axe distribution) | — | Pilot Nov 2025 | "strong feedback" | No |
| **Opening & Closing Auctions** (exchange closing cross) | 2025-11-05: available "in the coming weeks" | Nov 2025, US HG/HY on X-Pro | 600+ webinar attendees; still advertising "as participation continues to grow" (May 2026) | **Never** |
| **X-Pro** (platform rebuild) | 2021 Investor Day: "Fully redesigned trading experience being rolled out starting 1Q22" | 2023 (PT first); international 3Q24; Dealer RFQ + Mid-X on Pragma 2H25; enhanced X-Pro RFQ for US credit **3Q26** | Share of PT on X-Pro: 18.2% (3Q23) → 30.3% (4Q23) → 56% (2Q24) → 59% (3Q24) → 71% (4Q24) → **85%** (1Q25) | n/a |

**Pattern.** The protocols aimed at the buy side as a new way to trade (CLOB, Adaptive Auto-X, auctions) have no disclosed volumes. The protocols with disclosed growth either serve dealers' risk recycling (Mid-X, dealer RFQ, DealerAxess), sit on top of the existing RFQ (Auto-X, targeted block RFQ), or followed the market rather than led it (PT, once X-Pro could carry it).

## 2. The three-channel framework (Feb 2025 →) with the GS deck's market map

Concannon's FY24 letter: "We have a clear strategy to return to market share growth in U.S. credit across these three channels". The Dec 2025 Goldman Sachs deck sizes them:

| Channel | Market ADV (Nov 2025 TTM) | Est. e-penetration | MKTX's tools | MKTX's own metric (FY25 unless noted) |
|---|---|---|---|---|
| **Client-initiated RFQ** | **$11.6bn** | ~40–45% | RFQ, OT, Auto-X, AI dealer selection | Automation 28% of trade count |
| — of which **high-touch / block** | **$19.4bn** (block trade size) | est. **10–20%** | Targeted RFQ, Smart Select, Targeted Axes | Block ADV $5B (all regions) |
| **Portfolio trading** | **$6.1bn** | **~80%** | X-Pro PT, CP+ in PT, ETF overlays | US PT share 19.0% → US PT ADV $1.1B |
| **Dealer-initiated** | **$14.5** (unit missing in the deck; $bn assumed) | ~25% | Dealer RFQ, Mid-X, DealerAxess | Dealer-initiated ADV $1.7B |

- **Derived:** the four rows sum to about **$51.6bn** of US credit ADV. Roughly **$34bn** of it (blocks + dealer-initiated) is less than a quarter electronic, which is where the deck says the growth is. US PT share × market PT ADV = 19% × $6.1bn ≈ **$1.16bn**, which matches the $1.1B reported (consistency check, *derived*).
- **The deck's own verdict:** "A return to U.S. credit revenue growth is fundamental to our future success". US credit revenue CAGR **(2%)** over 2020–24, against **+15%** outside US credit.
- **Read:** the channel frame moves the scoreboard from *share of TRACE* (falling) to *ADV per channel* (rising). It is also honest about the opportunity. The underpenetrated pools are blocks and dealer-to-dealer, which are exactly where a buy-side RFQ venue has least natural access and where IDBs and Tradeweb are strong.

## 3. Dealer algos — the liquidity the protocols run on

| Metric (MKTX says) | Value | Source |
|---|---|---|
| Share of client RFQs that algos respond to (US/EUR HG & HY) | **96%** | *Algos in block trading* (2025) |
| Algo counterparty share of US HG trades | **88%** (Q1 2025), +21pp vs Q1 2021; 11 responses per inquiry | same |
| Algo share of US HG responses, $5–10mm | 12% → 37% | same |
| Dealer algo win rate on credit blocks | 10% (2023) → 25% (2025) | *From fringe to familiar* |
| Algo share of prices, April 2025 tariff shock | ~**80%**, vs a fall from 60% to 50% in COVID | *April volatility* AxessPoint |
| EUR HG responses from algos | 65% (2025); responses per RFQ 5.4 → 7.1; €3–5mm algo responses 10% → 22% | *European credit automation* (2026) |
| Dealer algo responses | 23.7M in 2022 (+29.2%) | FY22 letter |

"It is becoming clear that algos are dominating the liquidity pool". **Inference:** every new protocol (Auto-X, Mid-X, auctions, PT) depends on the same small set of bank pricing engines. That makes the platform more resilient in a tariff-style shock (algos stayed on) and more concentrated in a deeper one.

## 4. Automation economics — what MarketAxess says it saves

- **Time.** In Q2 2021, Auto-X RFQ saved "approximately 131 seconds per inquiry", "over 3600 hours" and 410,000 clicks in the quarter (about 400 trading days), assuming 60 seconds of trader validation per trade.
- **Persistence in stress.** The *no-touch* rate was 7% in COVID and 36% during SVB/Credit Suisse (2023). Override rates fell from 50% to 21%.
- **Speed.** Median time to trade is 43 seconds in EUR IG vs 10 minutes in USD IG (2023): "There is little benefit to delay the timers as similar trading outcomes can be obtained with shorter timers."
- **Scale.** Auto-X passed $1tn cumulative (2024). Some clients use the strategies for "over 90% of their trading volumes" (Schiffman, Sep 2024). In Europe the largest clients automated 75% of tickets up to €5m in Q1 2026, and "Automation in European credit trading is no longer experimental, it’s becoming the norm."
- **The gap that matters (derived):** automation is 28% of credit trade count but 11% of volume (FY25), so the average automated ticket is about a third the size of the average ticket ((11/28) ÷ (89/72) ≈ 0.32). Automation has electronified the small tickets the platform already had. It has not yet won the blocks, which is why blocks became a separate channel.

## 5. Opening & Closing Auctions — the cleanest import, and its adoption test

- **Design (MKTX says).** Book-building and imbalance phases; pegged, limit and *offsetting-only* orders. It "clears at the price that maximizes total trading volume". Pegged orders fill first, then limit, then offsetting. Built on the Pragma engine in X-Pro, the *first front-to-back implementation* of X-Pro and Pragma (GS deck, paraphrased). Advisory group: **AllianceBernstein, BlackRock, DWS, State Street Investment Management** ([[blackrock-hub]]).
- **The case.** "31% of U.S. high-grade TRACE is executed between 4 – 5 PM ET on month-ends" (GS deck). Concannon: 25% of a month-end day's IG volume trades in the last hour, and "almost 15%" on a normal day. CP+ bid-ask "collapses by 35% between the first and last hour of the trading day". ETF trading is over $10bn a day, ten times a decade ago. Sweeney: the equity closing auction is "about 10% of total trading volume".
- **The claims.** Concannon: "There’s no tradeable true auctions. This is the first." Sweeney: "Within the next couple of years, this could be the dominant protocol in the market" and "we’re now in the beginning of the snowball phase." BlackRock's Veiner says it "represents a meaningful advancement in the modernisation of the bond market."
- **The cautions, from inside the same coverage.** Bloomberg: "the worry is there’s a tradeoff if it squeezes dealer profits tied to the very inefficiencies it would eliminate." Concannon himself: "success will depend on adoption" without deep dealer and buy-side participation. Sweeney: "We have to make sure the auction is a liquid event". Concannon's answer to dealers: "Dealers can exit inventory on an auction or they can be a liquidity provider in an auction".
- **Read:** this is the import with the strongest structural logic, because indexation and ETFs really do concentrate flow at the close. It is also the most exposed to the CLOB problem. A single clearing price helps whoever is on the wrong side of the information gap, and it takes away dealers' end-of-day pricing edge. Six months after launch the company was still running ads asking people to join a Wednesday auction. No volume has been published.

## 6. The X-Pro rebuild — five years in five quotes

| Date | Statement | Reading |
|---|---|---|
| Sep 2021 (Investor Day) | "Fully redesigned trading experience being rolled out starting 1Q22" | The promise |
| Apr 2024 (FY23 letter) | "order-centric trading platform, MarketAxess X-Pro" launched in 2023; PT first | ~1.5 years late, and only PT at first |
| Apr 2025 (FY24 letter) | "2024 was primarily a “build” year in our technology transformation" | Year three |
| Dec 2025 (Mid-X interview) | "we’re integrating Pragma technology as the backbone of our entire system" | A second re-architecture inside the first |
| Apr 2026 (FY25 letter) | "We still have work to do"; new CTO William Quan to "strengthen technology execution across the enterprise" | Year five, new technology leadership reporting to the COO |
| Oct 2026 (3Q26) | Enhanced X-Pro RFQ brings "AI-powered dealer selection into a single modern interface" | The core US credit RFQ, the biggest franchise, migrates last |

**Inference:** the sequencing put the new protocols (PT, then dealer tools, then auctions) on the new stack before the core client RFQ. That made sense for share recovery in PT, where X-Pro share rose from 18% to 85% of MKTX PT and PT share recovered to 21%. But the highest-revenue workflow ran on the legacy UI until late 2026, while Tradeweb took IG share (context, from [[tradeweb-ai-price]] §6: The DESK, Jun 2026, Tradeweb 18.0% vs MKTX 16.0% of IG+HY TRACE).

## 7. Why each import worked technically but adoption was the constraint (inference — not stated by MarketAxess)

1. **Order books need committed liquidity providers, and corporate bonds do not have them by default.** Schiffman said so in 2021: "a streaming order book requires commitment from all participants to succeed." Three or four dedicated market makers on the most active IG names is a showcase, not a market. No volume was ever published.
2. **The imports took dealer edge away.** Auctions (a single closing price), Live Markets (pre-trade transparency) and OT (anonymity) all make the market fairer for the buy side and cost dealers information rents. Dealers adopted what helped them (Mid-X to recycle PT risk, dealer RFQ into OT, algos that answer at scale) and were slow on what didn't. The 2025–26 product list, with DealerAxess, Mid-X, Targeted Axes and the curation tools, reads as MKTX bargaining for dealer participation.
3. **The buy side is already on the RFQ, so new protocols compete with a habit.** Adaptive Auto-X needs clients to "leave the parent order" with the venue. Block desks needed "a more contained environment" (Burke, EM TRFQ). In practice traders add a protocol only when it is in the same ticket and the same OMS, hence the push into Aladdin, the IMTC OMS and X-Pro as *one container*.
4. **Technology was the binding constraint on the ones clients did want.** PT was announced in 2019 but stalled until a real release in 2021 and X-Pro in 2023–24. Tradeweb launched PT in Jan 2019 and did **$43bn** that year and **$123bn** in 2020 (context, from [[tradeweb-credit]] §1), while MKTX had done *more than 50* trades by mid-2021.
5. **Low-fee protocols dilute the fee line.** PT, blocks, Mid-X and auctions all carry lower fees per million than single-name RFQ. Credit FPM fell from $184.78 (FY21) to $127 (3Q26) ([[marketaxess-strategy-financials]]). So even the protocols that won adoption grew ADV faster than revenue.

## 8. Compared with Tradeweb's workflow wiring

| | MarketAxess (this note) | Tradeweb (context, from [[tradeweb-credit]]) |
|---|---|---|
| Strategy | Add **new protocols** from equities and ETFs (CLOB, auctions, algos, matching) | Electronify the **work around the existing RFQ** (Treasury spotting → Net Spotting → MCNS; voice processing; PT; AiEX) |
| PT | Announced Jun 2019; scaled 2022 ($92B); X-Pro-dependent; share 16–21% (2024–25) | First mover Jan 2019; $43bn (2019) → $123bn (2020) → >$270bn (2022); >$1tn market PT by 2024 |
| Hedging | Net spotting via LiquidityEdge (bought 2019), integrated in PT 2021 | Net Spotting **$818bn** submitted (2020); the *rates adjacency* moat |
| Auto-execution | Auto-X 17% of tickets (2021), 28% of trade count (FY25) | AiEX ≈ **54%** of IG RFQ tickets (Nov 2021) |
| A2A | OT, the brand | AllTrade, added *without changing anyone's workflow* |
| Price ruler | CP+ | Ai-Price |
| Result | Protocol breadth; US HG share 22.8% (4Q20) → 18.4% (4Q24) | HG TRACE share 11.8% (2019) → 22.5% (Q1 2022); fully electronic HG record 19.7% (Apr 2024) |

**Read:** in Goldratt's terms ([[canon-goldratt-the-goal]]), Tradeweb attacked the binding constraint in IG execution, the Treasury hedge and its phone delay, inside the trader's existing ticket. MarketAxess opened new channels next to the ticket. Both approaches are rational. In a relationship market the one that changes the fewest habits wins first.

## 9. What the claims don't prove

1. **Launch ≠ adoption.** Live Markets, Adaptive Auto-X and the auctions are described in launch releases and features, never in volumes. *First* claims ("fixed income's first", "first standardized market-wide auction protocol") are unverified inside the corpus.
2. **Records in low-fee channels.** Record block, PT and Mid-X ADV comes with a falling credit FPM. ADV growth by channel is not revenue growth, and the deck says US credit revenue shrank.
3. **The denominators move.** PT share is quoted as *% of e-traded PT* (~31%, 4Q22), as *% of HG+HY TRACE PT* (20.0%/16.2%, 2024), and as *US credit PT* (19.0%, FY25). The April 2025 letter said PT share was "tracking 320 basis points above" FY24, and the year closed at +270bp. From 2024 the releases also footnote the effect of single-dealer PT on reported share.
4. **Automation is measured by ticket.** Trade-count shares (17%, 20%, 28%) flatter automation against volume share (10%, 11%).
5. **Self-measured TCA.** Block TCA (*Blockbusting* Part 4: 26% at CP+ mid or better) and PT precision (HY median absolute deviation to CP+ $0.17 → $0.10) are scored on CP+ (see [[marketaxess-open-trading]] §5).

## 10. Canon lenses

- **Sustaining vs disruptive** ([[canon-christensen-innovators-dilemma]]): CLOBs and auctions are *disruptive* to dealer economics and were sold to the dealers they disrupt. Auto-X and dealer RFQ are *sustaining*, and they are the ones that grew.
- **Multi-sided platforms and chicken-and-egg** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): an order book or auction is worth joining only if the other side is there. MKTX seeded with named market makers (Goldman, Barclays, Flow Traders) and an advisory group (BlackRock et al.), the textbook subsidy-the-hard-side move, without disclosed results.
- **Transformation at scale** ([[canon-kotter-leading-change]], E5): a five-year platform rebuild with a re-architecture in the middle (Pragma), two CFO changes and a new CTO shows how execution risk compounds when the rebuild and the strategy change at once.
- **Theory of the constraint** ([[canon-goldratt-the-goal]]): see §8.
- **Power** ([[canon-helmer-7-powers]]): protocols are copyable. Durable power comes from switching costs (TCA history on CP+, OMS integration) and from scale in liquidity, which neither the CLOB nor the auctions reached.

## 11. Practitioner counterpoint

- **For MarketAxess:** the imports were the right bets on where credit is going. Indexation, ETFs, algos and systematic funds are real, and MKTX built the plumbing early. Automation numbers (92% power-user Auto-X, algos at 80% of prices in April 2025, 36% no-touch through SVB) show a platform that holds up in stress. Mid-X and dealer-initiated ADV (+33%) show dealers *will* adopt tools that help them recycle risk.
- **Against:** a venue cannot import a market structure that the participants with the information advantage don't want. The undisclosed CLOB and auction volumes, the five-year rebuild and the 2% annual US credit revenue decline say the portfolio of protocols did not move the core. The equity analogy is weak: bonds have thousands of CUSIPs per issuer and no natural continuous two-sided interest.
- **Both:** judge each protocol by **disclosed volume and fee per million**, not by launch. For auctions, the test is whether S&P or other evaluators adopt the closing print as a mark, as Sweeney hopes. That would make it a benchmark, not just a protocol.

## 12. Open questions to track

1. Will ICE publish closing-auction, Live Markets and Adaptive Auto-X volumes, or fold them into ICE Bonds' protocols? ([[marketaxess-ice-deal]], [[ice-hub]])
2. Does the auction close become an evaluated-pricing input (S&P, [[marketaxess-data-cp-plus]])?
3. Does the enhanced X-Pro RFQ (3Q26) stop US HG share falling?
4. Blocks: does US block e-penetration move from 10–20% toward the ~40–45% of client RFQ?
5. What happens to Mid-X and DealerAxess if ICE's own dealer and retail networks overlap them?

**Links:** [[marketaxess-hub]] · [[marketaxess-open-trading]] · [[marketaxess-strategy-financials]] · [[marketaxess-data-cp-plus]] · [[marketaxess-ice-deal]] · [[marketaxess-people]] · [[tradeweb-credit]] · [[tradeweb-ai-price]] · [[tradeweb-a2a-information-leakage]] · [[tradeweb-hub]] · [[blackrock-hub]] · [[ice-hub]] · [[goldman-hub]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[canon-christensen-innovators-dilemma]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-parker-platform-revolution]] · [[canon-goldratt-the-goal]] · [[canon-kotter-leading-change]] · [[canon-helmer-7-powers]]

---
### Rep
**Closing-auction economics.** Use the GS deck sum of US credit ADV (~$51.6bn, *derived*), Concannon's "almost 15%" of a normal day's volume in the last hour, and FY25 credit FPM of **$139**.
(a) How much US credit ADV trades in the last hour on a normal day? (b) If the auction captures 5% of that last-hour flow, what annual volume (252 days) and revenue does that imply at the FY25 FPM? Compare it with FY25 revenue of $846M. (c) A client trades $10mm of a bond with spread duration 7 whose CP+ bid-ask is 2bp in the first hour. Using the "collapses by 35%" claim, what does trading at the close save in half-spread cost? (d) One paragraph: why (b) is probably an upper bound on revenue but (c) is why the buy side, and BlackRock, want the auction anyway.

*(a) 15% × $51.6bn ≈ **$7.7bn**. (b) 5% × $7.7bn ≈ $387m a day × 252 ≈ **$97.5bn** a year × $139/mm ≈ **$13.6M**, about **1.6%** of FY25 revenue. (c) First-hour half-spread 1bp → $10,000,000 × 7 × 0.0001 = **$7,000**. Close half-spread 0.65bp → **$4,550**. Saving ≈ **$2,450** per trade (all derived). (d) Auction fees are unlikely to match single-name RFQ FPM, and auction volume partly cannibalises close-of-day RFQ and PT already on the platform. The value goes to the buy side as tighter spreads and less tracking error, and to MKTX as a benchmark and data product (a closing mark for S&P and ETFs). That is why "success will depend on adoption" is the real test, not fee revenue.*

---
**Sources (MarketAxess corpus, `_ingest/raw/marketaxess/articles.jsonl`, accessed 2026-10-25):**
- [Live Markets announced, 2019-05-09](https://investor.marketaxess.com/news/news-details/2019/MarketAxess-Developing-Live-Order-Book-for-Institutional-Fixed-Income-Market-05-09-2019/default.aspx) · [PT announced, 2019-06-19](https://investor.marketaxess.com/news/news-details/2019/MarketAxess-Brings-Efficiency-to-Portfolio-Trading-Protocols-06-19-2019/default.aspx) · [Goldman Sachs on Live Markets, 2020-10-21](https://investor.marketaxess.com/news/news-details/2020/Goldman-Sachs-Adds-Streaming-Firm-Pricing-to-MarketAxess-Live-Markets-Order-Book-10-21-2020/default.aspx) · [Barclays on Live Markets, 2021-05-27](https://investor.marketaxess.com/news/news-details/2021/Barclays-Adds-Streaming-Firm-Pricing-To-MarketAxess-Live-Markets-Order-Book-05-27-2021/default.aspx) · [PT enhancements, 2021-06-23](https://investor.marketaxess.com/news/news-details/2021/MarketAxess-Adds-New-Efficiency-and-Cost-Saving-Enhancements-to-Portfolio-Trading-Capabilities-06-23-2021/default.aspx) · [Flow Traders, 2021-12-07](https://investor.marketaxess.com/news/news-details/2021/Flow-Traders-Takes-a-New-Market-Position-as-an-Active-Liquidity-Provider-on-MarketAxess-12-07-2021/default.aspx)
- [2021 Investor Day, 2021-09-14](https://s201.q4cdn.com/767283836/files/doc_presentation/2021/09/2021-Investor-Day-Presentation.pdf) · [GS Financial Services Conference deck, 2025-12-09](https://s201.q4cdn.com/767283836/files/doc_downloads/2025/12/11/Goldman-Sachs-Financial-Services-Conference-Final.pdf)
- [2020 letter, 2021-04-28](https://s201.q4cdn.com/767283836/files/doc_financials/2020/ar/MKTX_Annual-Report_2020.pdf.pdf) · [2022 letter, 2023-04-26](https://s201.q4cdn.com/767283836/files/doc_financials/2022/ar/Posting-179619_MarketAxess-Holdings_COMBO-PRoxy-AR_WEB-HOSTING_rev2_MS.pdf) · [2023 letter, 2024-04-24](https://s201.q4cdn.com/767283836/files/doc_financials/2023/ar/327161_MARKETAXESS-HOLDINGS-INC-_10K_2024_V1_PWO-34656_PROOF_rev3_MS_DY.pdf) · [2024 letter, 2025-04-23](https://s201.q4cdn.com/767283836/files/doc_financials/2024/ar/388651_P20013_MKTX_2025-Proxy_PROOF_MS_COLOR.pdf) · [2025 letter, 2026-04-29](https://s201.q4cdn.com/767283836/files/doc_financials/2025/ar/MarketAxess-Holdings-Inc-2025-10-K-ARS.pdf)
- [Adaptive Auto-X first trade, 2023-06-22](https://investor.marketaxess.com/news/news-details/2023/MarketAxess-Announces-First-Client-Algo-Trade-Using-Adaptive-Auto-X/default.aspx) · [Pragma agreement, 2023-08-07](https://investor.marketaxess.com/news/news-details/2023/MarketAxess-to-Acquire-Algorithmic-Trading-Provider-Pragma/default.aspx) · [Pragma close, 2023-10-02](https://investor.marketaxess.com/news/news-details/2023/MarketAxess-Completes-Acquisition-of-Pragma/default.aspx) · [BlackRock Aladdin, 2024-09-09](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Announces-Expanded-Partnership-with-BlackRock-to-Deliver-Enhanced-Connectivity-and-Efficiency-to-Global-Credit-Markets/default.aspx) · [Mid-X in US credit, 2025-08-05](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Announces-the-Launch-of-Mid-X-in-US-Credit/default.aspx) · [William Quan CTO, 2026-02-25](https://investor.marketaxess.com/news/news-details/2026/William-Quan-to-Join-MarketAxess-as-Chief-Technology-Officer/default.aspx)
- Earnings: [1Q24](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-First-Quarter-2024-Financial-Results/default.aspx) · [2Q24](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-Second-Quarter-2024-Financial-Results/default.aspx) · [3Q24](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-Third-Quarter-2024-Financial-Results/default.aspx) · [4Q24](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx) · [3Q25](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Reports-Third-Quarter-2025-Financial-Results/default.aspx) · [4Q25](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx) · [1Q26](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-First-Quarter-2026-Financial-Results/default.aspx) · [2Q26](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Second-Quarter-2026-Financial-Results/default.aspx) · [3Q26](https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Third-Quarter-2026-Financial-Results/default.aspx) · [4Q23](https://investor.marketaxess.com/news/news-details/2024/MarketAxess-Reports-Fourth-Quarter-and-Full-Year-2023-Results/default.aspx)
- Auctions: [release, 2025-11-05](https://investor.marketaxess.com/news/news-details/2025/MarketAxess-Unveils-Fixed-Incomes-First-Opening--Closing-Auctions-Designed-to-Improve-Pricing-and-Liquidity/default.aspx) · [Bloomberg reprint, 2025-11-05](https://www.marketaxess.com/articles/corporate-bond-world-set-to-get-first-daily-closing-auction) · [Unlocking liquidity, 2025-11](https://www.marketaxess.com/articles/unlocking-liquidity-how-marketaxess-opening-and-closing-auctions-are-reshaping-bond-trading) · [The TRADE, 2025-12-15](https://www.marketaxess.com/articles/history-in-the-making-a-closer-look-at-marketaxess-newly-launched-opening-and-closing-auctions) · [Closing Auction ad, 2026](https://www.marketaxess.com/whats-new/whats-new-closing-auction)
- Automation & dealers: [Quantifying the efficiency opportunity, 2021](https://www.marketaxess.com/articles/axesspoint_quantifying-the-efficiency-opportunity-for-automation) · [Persistence of automation, 2023](https://www.marketaxess.com/articles/persistence-of-automation-through-volatility) · [Speed of trading, 2023](https://www.marketaxess.com/articles/axesspoint-speed-of-trading-algos-and-velocity) · [Intelligent Automation, 2024-05](https://www.marketaxess.com/articles/the-future-of-fixed-income-trading-is-intelligent-automation) · [Algos in block trading, 2025](https://www.marketaxess.com/articles/axesspoint-the-expanding-role-of-algos-in-block-trading-and-market-liquidity) · [From fringe to familiar, 2025](https://www.marketaxess.com/articles/from-fringe-to-familiar-the-automation-frontier-in-trading) · [European credit automation, 2026](https://www.marketaxess.com/articles/the-rise-of-european-credit-automation) · [DealerAxess (WatersTechnology), 2025-09-16](https://www.marketaxess.com/articles/marketaxess-enhances-dealer-value-through-its-new-dealeraxess-service) · [Mid-X expands (Markets Media), 2025-12-03](https://www.marketaxess.com/articles/marketaxess-expands-mid-x-protocol) · [More block trades are going electronic, ~2026](https://www.marketaxess.com/articles/more-block-trades-are-going-electronic) · [Targeted axes, 2026-02](https://www.marketaxess.com/articles/targeted-axes-precision-control-and-efficiency) · [Live Markets and hedge funds, undated](https://www.marketaxess.com/articles/live-markets-and-the-innovative-hedge-funds-using-it)
