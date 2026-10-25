# Note · JPMorganChase Markets and the venues — the world's biggest dealer underwrote, staffed, launched and now ships its algos through Tradeweb, yet never names a venue; electronification is told as a cost-per-trade story

> Market-structure / competitive-strategy note · Maps to **Course 04** (Competitive Strategy — co-opetition, platform power), **Course 06** (Operations — cost per trade, automation), **E3** (M&A — the bank as venue adviser and investor), **E10** (Digital & AI Transformation) · Canon: Network Effects & Platform Strategy · Written 2026-10-25 · Companion to [[tradeweb-outside-voices]] and [[tradeweb-a2a-information-leakage]]

- **Source:** `_ingest/raw/jpmc/articles.jsonl`: the CIB letters AR2019–AR2025 (Pinto; then Piepszak and Rohrbaugh; then Rohrbaugh and Petno), the CIB segment of the 2025 Investor Day, the Markets lines of ten earnings calls, J.P. Markets pages (Execute, Aqua and JPM-X, DataQuery, JPMaQS, FICC market structure, the e-Trading Survey report) and the five 2026 Markets articles (Jul 31 and Aug 28). The Tradeweb side comes from `_ingest/raw/tradeweb/articles-2019-2026.jsonl`, marked [TW]. **JPMC's 165 records name Tradeweb, MarketAxess and Trumid zero times.** Some 2026 Markets pages lost their pull-quotes in scraping.
- **Core claim:** J.P. Morgan is #1 in Markets revenue (~11.4–12.9% share, 2019–2025) and grew Markets revenue from ~$21B (2019) to a record **$35.8B (2025)**. The growth came from **financing and Prime** and from a structurally bigger wallet, not from FICC share, which Rohrbaugh admits is below pre-COVID. Electronification shows up in JPMC's telling only as **operating leverage**: volumes "nearly tripled since 2019" while cost per trade fell 42% in Rates and 23% in Cash Equities. Toward venues JPM plays **every role at once**: founding owner and IPO bookrunner, people supplier (Pluta, Bruni), launch counterparty, the first dealer whose algos Tradeweb hosted, client (JPMAM), co-investor (MAXEX, Capitolis), M&A adviser (ICD; MarketAxess's sale to ICE), index owner (EMBI, GBI), and competitor through its own single-dealer platform, dark pool, systematic internaliser and data products. The silence about venues is the strategy. The client relationship is the product; the venue is plumbing.

---

## 1. Markets by the numbers (JPMC's figures)

| Year (letter date) | Markets revenue | Markets share (Coalition) | FICC / Equities | Signal in the text |
|---|---|---|---|---|
| 2019 (AR2019) | ~$21B (+7%) | #1, 12.0% | FI $14.4B; Eq $6.5B, 11.3% share (from 8.4% in 2015) | "global, complete and at scale" |
| 2020 | **$29.5B (+41%)** | #1, 12.9% | FI $20.9B; Eq $8.6B | FX "730 trades per second" at peak; multi-dealer platforms named |
| 2021 | $27B | #1, 12.2% | Eq record $10.5B | "digital portals and electronic trading strategies" |
| 2022 | $29B | #1 (~11.7%, chart) | FI $18.6B; Eq $10.4B | trading capital "a headwind"; credit e-trading |
| 2023 | $28B | #1, 11.4% | institutional-client share 11.1% (2018) → 13.9% | algorithmic Treasury offering |
| 2024 | **$30B (record)** | #1, 11.4% | Eq +13%, FI +5% | financing up 75% since 2019 at 17% share |
| 2025 (AR2025) | **$35.8B (+19%)** | #1, 11.8%; Equities co-#1 13.2% | FI $22.5B; Eq record $13.3B | "AI became the battleground" |
| 2026 YTD (calls) | n/r in $ | — | Equities +86% (2Q26), +49% (3Q26); FICC −4% (3Q26) | Prime and financing; RWA +$103B in 2Q26 |

Other markers: >90,000 active users on the J.P. Morgan Markets portal and a $340B single-day FX record (Investor Day 2025). The April 2025 tariff shock produced 29 billion equity trades in a single day (Risk Awards page, 2025-12-18) and 3.2B order and execution messages on the worst day (AR2025 CIB letter). Equity derivatives house and QIS house of the year at the 2026 Risk Awards.

## 2. What the CIB leaders say about electronification

| Date | Speaker | Line (verbatim) |
|---|---|---|
| 2020-04-06 | Pinto | "our steadfast pursuit of three strategic goals: being global, complete and at scale." |
| 2021-01-15 | Dimon (4Q20) | "we kept our share while things were electronified and digitized" |
| 2021-04-07 | Pinto | "The trend in electronification continues in market trading" and JPM is "more effectively participating in multi-dealer platforms." |
| 2022-04-04 | Pinto | "More and more, participants in trading markets are using digital portals and electronic trading strategies." JPM is "building out our own proprietary channels that connect to others in order to streamline the experience from pre-trade to post-trade." |
| 2023-04-04 | Pinto | "the capital required to fuel our global trading desks has risen significantly over the last five years." |
| 2024-04-08 | Piepszak & Rohrbaugh | "We are investing heavily in the electronification of our credit business, bringing across some of the technology and approach behind our Equities business." And: "J.P. Morgan launched a new algorithmic trading offering to U.S. Treasury investors to capture share in the world’s most important bond market." |
| 2025-05-19 | Petno | "as our overall trading volumes have nearly tripled since 2019, we've seen significant reductions in our cost per trade." |
| 2025-05-19 | Rohrbaugh | "I think the broad fee pool in Markets won't go back to those pre-COVID levels." FICC share is lower because of wallet mix "plus certain areas of underperformance, such as Rates". "So in Fixed Income it won't be easy, but I think we can gain share." |
| 2026-01-13 | Dimon (4Q25) | "We have the best FICC business in the world, one of the best equity businesses in the world." |
| 2026-04-06 | Rohrbaugh & Petno | "AI became the battleground of competition and the defining market force." Nonbanks "are scaling into areas once considered the preserve of universal banks" |

**Reading the arc:** 2020–21 treats electronification as a trend to *participate in* (multi-dealer platforms). 2022–24 shifts to *own channels* and capital cost. 2025–26 treats it as *operating leverage* (cost per trade, AI) and a contest with nonbanks. At no point is a venue named.

## 3. JPM's own trading surface (from the Markets pages)

| Product | What it is (JPMC description) | Venue analogue |
|---|---|---|
| **Execute** | FX and commodities single-dealer platform; Execute Analytics; Execute for Private Bank | Competes with multi-dealer FX platforms |
| **Aqua** + **JPM-X / JPB-X** | Liquidity-seeking equity algo with six urgency levels; JPM-X a "fully dark, continuous crossing platform" ATS; JPB-X a second ATS | Internalisation versus lit exchanges |
| EU/UK **systematic internaliser** | Defended in Rachid Alaoui's op-ed (2026-09-08) | Competes with MTFs and exchanges |
| **Rates algos** | Hosted on Tradeweb from 2025 [TW]; "algorithmic trading offering" (AR2023) | Distribution through the venue |
| **Vida Beta One** | Portfolio-trading platform (Risk Awards 2026) | Competes with venue PT protocols |
| **DataQuery, JPMaQS, Fusion** | Market data, 20+ years of vol history, macro quant data, buy-side data platform | Competes with venue and LSEG data businesses |
| **Indices** | EMBI, CEMBI, GBI-EM, JESG | Drive venue EM growth stories [TW] |
| **Kinexys tokenized repo** | Intraday repo with tokenized collateral, ">$300 billion" processed by 2022-07 | Competes with on-chain repo pilots |

## 4. The e-Trading Survey: the dealer's read on the market (J.P. Morgan Markets, 2026, 10th edition)

| Measure | 2026 result (JPM's survey) | Earlier |
|---|---|---|
| Top market-structure concern | **Technology developments 22%**, access to liquidity 21%, regulation 18% | Liquidity was top for ten years (25% in 2022) |
| Electronic share of trading | 60% in 2026 → **70% expected in 2027** | 2022: 78% of traders planned to use e-trading more |
| Biggest daily challenge | Volatile markets, 43% (fourth year running) | — |
| Platform use | 40% use both single-dealer and multi-dealer platforms | — |
| Most influential technology (3 years) | Generative AI 43% | Machine learning/NLP ranked first in 2024 and 2025 |
| Biggest digital-asset opportunity | Tokenization, 40% | — |
| Next product to electronify | ETFs 18%; equity derivatives 15%; corporate bonds 15% | — |
| Asset-class levels (2026 articles) | FX about 95% electronic; credit about 40% (Andrew Cole) | — |

Voices from the 2026 articles:
- **Andrew Cole** (Head of Execute product): "there’s a push-pull between the venues that are desperate to implement things that get clients to trade on that platform". He also says "For every electronification that enables traders to do good things, there’s a counter way where we educate them".
- **Peter Grant** (systematic credit): "clients are looking at options including reducing the number of dealers and pushing towards this direct connectivity to mitigate the concerns."

That is the leakage worry of [[tradeweb-a2a-information-leakage]], seen from the dealer side.

## 5. The nine roles JPM plays toward Tradeweb and other venues

| # | Role | Evidence |
|---|---|---|
| 1 | Founding owner, then seller | Joint lead bookrunner on Tradeweb's IPO (Apr 2019) and follow-ons (Oct 2019, Apr 2020), all used to buy out bank holders [TW]; bank ownership fell from 46% to 17.3% ([[tradeweb-strategy-financials]]) |
| 2 | People pipeline | Thomas Pluta (JPM Global Head of Linear Rates; Tradeweb director from 2017) was Tradeweb President Jan 2023–Sep 2024. Enrico Bruni (JPM 1995–2002, e-trading strategy) is a Tradeweb co-head of Global Markets. Chair Jacques Aigrain and director Daniel Maguire also have JPM stints [TW] |
| 3 | Launch counterparty | First electronic SONIA swap-vs-gilt-future package (2020); first iBoxx TRS (2021); first fully electronic SOFR swap spread (2021, vs BlackRock). In that SOFR release Pluta said "we are encouraging our clients to transition their trading away from LIBOR" [TW] |
| 4 | Algo distribution | Liyan Yu (2025-10-09): "As the first dealer to offer algo execution strategies on the Tradeweb platform" JPM is "providing broader investor access to our leading U.S. Treasury algo strategies" [TW]. Joined multi-dealer algo workflows with Citi, Morgan Stanley and RBC (2026) [TW] |
| 5 | Client | JPMAM's Mike McClinchie: "I just started releasing all of my orders from my OMS to Tradeweb" [TW, 2022-02-10] |
| 6 | Co-investor | JPM led a 2021 investment in MAXEX, where Tradeweb invested in 2026 and JPM's Marc Simpson sits on the board. Both invested in Capitolis (2026) [TW] |
| 7 | Venue M&A adviser | JPM was lead financial adviser to Tradeweb on ICD ($785M, 2024) [TW]. JPM advised MarketAxess on its sale to ICE (Jul 2026; per the ICE sibling study, [[ice-hub]], [[marketaxess-hub]]) |
| 8 | Index owner | J.P. Morgan GBI-EM and EMBI inclusion drives Tradeweb's China and Saudi stories [TW] |
| 9 | Competitor | §3 above. Portfolio trading: Koo (JPM, 2019) said "we expect this to double in the next couple of years, if not triple" [TW] |

## 6. What the claims don't prove

1. **Cost per trade isn't margin.** The 42% and 23% falls come with "nearly tripled" volumes. JPMC doesn't give revenue per trade, so whether automation kept or gave away economics can't be checked.
2. **Share is Coalition's, on JPMC's peer set.** Coalition Greenwich ranks banks against banks. Nonbank market makers (Citadel Securities, Jane Street) are outside the peer set, so "#1" can coexist with share loss to nonbanks.
3. **The survey is JPM's own, sample size not given.** Respondents are J.P. Morgan clients. Technology overtaking liquidity may say as much about who answers as about the market.
4. **Electronic share figures disagree.** Cole's "about 40%" for credit and ICMA's ~60% for European credit (quoted on the same page) use different scopes. Neither matches Tradeweb's TRACE-share definitions ([[tradeweb-credit]]).
5. **Financing growth is balance-sheet growth.** The financing and Prime engine (17% share, RWA +$103B in one quarter) is exactly what capital rules price ([[jpmc-capital-regulation]]). Its returns depend on the rules outcome and on hedge-fund leverage, which Barnum calls "known unknowns".

## 7. Strategic read (inference — not JPMC's words)

- **Silence is positioning.** A dealer that names Tradeweb in its shareholder letter endorses a channel that commoditises dealers. JPM instead describes "our own proprietary channels that connect to others". The venues are the "others".
- **Ship your algos through the venue; keep the client in your channel.** Putting Treasury algos on Tradeweb gives JPM distribution to clients it doesn't cover, at the cost of the venue's toll. Execute, JPM-X and Vida keep the direct relationship and the data. Expect JPM to push venues toward "dealer-in-the-loop" protocols (SNAP+, curated RFQ) and away from anonymous all-to-all.
- **Consolidation helps the bank's bargaining power.** ICE–MarketAxess and Tradeweb–Trumid mean fewer, bigger venues. JPM advised on one side of that. With fewer venues, each dealer matters more to each venue. With bigger venues, each venue matters more to each dealer. JPM's index, data and algo assets are levers in that negotiation.
- **The nonbank threat is the real competitive axis.** Dimon's AR2025 list names Citadel Securities ([[jpmc-mission-forces]]). In 2025–26 the Rohrbaugh and Petno letter adds "market infrastructure providers" as competitors. That likely means venues and data vendors bundling execution, data and post-trade.
- **Treasury clearing and all-to-all are the swing events** ([[jpmc-capital-regulation]], [[tradeweb-derivatives-regulation]]). If clearing releases balance sheet, JPM can stream more in all-to-all. If it doesn't, nonbanks gain.

## 8. Canon lenses

- **Co-opetition** ([[canon-brandenburger-nalebuff-coopetition]]): JPM is a complementor (liquidity, algos, indices) and a substitute (single-dealer, internalisation) to every venue. Its value net includes Tradeweb as supplier, customer and competitor at once.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): venues need dealers on one side to attract clients on the other. The largest dealer has the most leverage over the platform's pricing and protocol choices.
- **Information economics** ([[canon-shapiro-varian-information-rules]]): DataQuery, JPMaQS, Fusion and the indices turn trading exhaust into licensable data, the same move venues make.
- **Disruption from below** ([[canon-christensen-innovators-dilemma]]): principal trading firms entered at the low-margin, high-volume end (streaming, ETFs, Treasuries). Dimon's 2026 naming of Citadel Securities is the moment an incumbent admits the entrant has moved upmarket.

## 9. Practitioner counterpoint

- **Bank view:** venues are useful pipes. The client relationship, research and balance sheet decide who wins the trade, especially in size and in stress. That is why JPM can be #1 while venues grow.
- **Venue view** ([[tradeweb-outside-voices]]): dealers praise "the category" and hedge on the venue. Automation and A2A erode the relationship premium one protocol at a time, and every AiEX ticket makes the dealer more interchangeable.
- **Synthesis:** both are true in different segments. In FX (about 95% electronic) the bank is a price stream. In credit (about 40%) and derivatives ("a third-party platform at any level is just a technology vendor", Cole) the relationship still counts.

## 10. Open questions

1. Does JPM's Markets share hold at ~11–12% if Treasury clearing and SLR relief lift nonbank capacity in 2027?
2. Does JPM put more algos or streams on Tradeweb or Bloomberg after the Trumid and MarketAxess deals close (H1 2027)?
3. Does JPM disclose any electronic-share or revenue-per-trade metric at the 2027 Investor Day?
4. Does Fusion or DataQuery compete head-on with venue data (Tradeweb Ai-Price, ICE pricing, LSEG)?
5. What did JPM earn as adviser on MarketAxess, and does it advise on other venue consolidations?

**Links:** [[jpmc-hub]] · [[jpmc-capital-regulation]] · [[jpmc-kinexys-deposit-tokens]] · [[jpmc-ai-tech-spend]] · [[jpmc-mission-forces]] · [[tradeweb-hub]] · [[tradeweb-outside-voices]] · [[tradeweb-people]] · [[tradeweb-credit]] · [[tradeweb-a2a-information-leakage]] · [[tradeweb-strategy-financials]] · [[tradeweb-derivatives-regulation]] · [[trading-floor-mechanics]] · [[market-structure-24-5-trading]] · [[wss-trading-hedge-funds]] · [[ice-hub]] · [[marketaxess-hub]] · [[bloomberg-hub]] · [[lseg-hub]] · [[blackrock-hub]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-parker-platform-revolution]] · [[canon-shapiro-varian-information-rules]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
Using only §1 and §4: (a) Compute Markets revenue CAGR from 2019 (~$21B) to 2025 ($35.8B). (b) If electronic share rises from 60% to 70% and JPM's revenue per electronic trade is half its revenue per voice trade at constant volume, what happens to revenue from the shift alone? (c) In five bullets, advise Tradeweb's head of rates on what to offer JPM in return for streaming more Treasury liquidity into all-to-all, using the roles in §5.

*Answer for (a):* (35.8 / 21)^(1/6) − 1 ≈ **9.3% a year**. *(b):* Normalise revenue per voice trade to 1 and per electronic trade to 0.5, with 100 trades. Before: 40 + 30 = 70. After: 30 + 35 = 65. That is **−7%** from mix alone, which is why the bank talks about cost per trade.

**Sources:** [AR2019 LOB letters, 2020-04-06](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2019.pdf) · [AR2020 LOB letters, 2021-04-07](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2020.pdf) · [AR2021 LOB letters, 2022-04-04](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2021.pdf) · [AR2022 LOB letters, 2023-04-04](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2022.pdf) · [AR2023 LOB letters, 2024-04-08](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2023.pdf) · [AR2025 LOB letters, 2026-04-06](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/line-of-business-ceo-letters-to-shareholders-2025.pdf) · [2025 Investor Day, 2025-05-19](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/events/2025/jpmc-2025-investor-day/full-transcript.pdf) · [Risk Awards 2026, 2025-12-18](https://www.jpmorgan.com/insights/markets-and-economy/markets/risk-awards) · [e-Trading Survey (accessed 2026-10-25)](https://www.jpmorgan.com/markets/etrading-trends) · [Digital Trading Desk, 2026-07-31](https://www.jpmorgan.com/insights/markets-and-economy/markets/digital-trading-desk-human-touch) · [Technology overtakes liquidity, 2026-07-31](https://www.jpmorgan.com/insights/markets-and-economy/markets/technology-overtakes-liquidity-market-structure) · [E-trading & ETFs, 2026-07-31](https://www.jpmorgan.com/insights/markets-and-economy/markets/etfs-trading-institutional-liquidity) · [Alaoui op-ed, 2026-09-08](https://www.jpmorganchase.com/newsroom/from-the-desk-of/trading-choice-is-a-feature-not-a-flaw-in-europes-equity-markets) · [Aqua/JPM-X (accessed)](https://www.jpmorgan.com/markets/aqua) · [Tradeweb: JPM algos on Tradeweb, 2025-10-09](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-expands-algorithmic-execution-capabilities-for-u.s.-treasuries) · [Tradeweb: first SOFR swap spread, 2021-07-08](https://www.tradeweb.com/newsroom/media-center/news-releases/tradeweb-announces-first-fully-electronic-sofr-swap-spread-trade/) · [Tradeweb: Pluta named President, 2022-07-13](https://www.tradeweb.com/newsroom/media-center/news-releases/thomas-pluta-appointed-next-president-of-tradeweb/)
