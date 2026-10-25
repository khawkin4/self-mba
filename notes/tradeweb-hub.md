# Note · Tradeweb hub — one playbook run across every OTC market for 25 years, now bought rather than built

> Hub / company-study note · Maps to **Course 04** (Competitive Strategy), **Course 02** (Corporate Finance & Valuation), **Course 07** (Data, Analytics & Decision-Making), **Course 11** (Global Strategy & Macro), **E2** (Capital Allocation), **E3** (M&A), **E10** (Digital & AI Transformation) · Written 2026-10-24 · Entry point for the eight Tradeweb notes

- **Source:** the full Tradeweb newsroom as of 2026-10-24: **2,149 items, Feb 2001 – Oct 22 2026** (index: `_ingest/raw/tradeweb/newsroom-index.tsv`). The **481 substantive text items from 2019–2026** were read in full (`_ingest/raw/tradeweb/articles-2019-2026.jsonl`, split into six theme buckets `bucket-*.jsonl`). Excluded: monthly volume releases, monthly ETF / government-bond update blogs, date notices, video and podcast pages. 2001–2018 is covered from **release titles only** (§2).
- **Core claim:** Tradeweb does one thing over and over. It takes an over-the-counter market that trades by phone, puts **multi-dealer RFQ** on it, adds automation around the trade, turns the resulting flow into **data and reference prices**, and then repeats in the next asset class or country. Treasuries (1998) → mortgages and euro govvies (2001) → swaps and CDS (2005) → ETFs (2012) → US credit (2014) → China (2017) → corporates' cash (2024). Regulation sped it up twice (swap mandates 2013, Treasury clearing 2026). Since 2021 the growth engine has added **acquisitions** that grow in size, ending with the **~$1.97B Trumid deal** (Oct 19 2026). Almost every quality metric along the way is Tradeweb measuring itself.

---

## 1. Map of the notes

| Note | Thesis in one line | Read it for |
|---|---|---|
| [[tradeweb-strategy-financials]] | A self-funded compounder now buying its way up the credit stack | FY19–H1 26 financials, IPO mechanics, every deal, LSEG control, Trumid at ~1.8× FY25 adj. EBITDA |
| [[tradeweb-credit]] | Credit share won by wiring the workflow around the trade, graded with its own rulers | Portfolio trading, net spotting, TRACE share 2019–26, the "select smart" turn, the TRACE-denominator fight |
| [[tradeweb-rates-em]] | The moat is the plumbing; the next leg is benchmarks and new countries | Treasuries, govvies, repo, Bond Connect, Saudi, Korea WGBI, closing-price benchmarks |
| [[tradeweb-derivatives-regulation]] | Mandates built the swaps franchise; now the same playbook goes to unmandated markets | SEF share, LIBOR→SOFR, Treasury clearing, UK/EU transparency, uncleared swap unwinds |
| [[tradeweb-equities-retail]] | The fixed-income RFQ playbook exported to ETFs and turned into a data business | ETF RFQ in Europe, the US and Asia; iNAV; Plato eBlock |
| [[tradeweb-tech-ai-data]] | Automation is the product; the data it throws off is the business | AiEX adoption, SNAP+, TARA, Kalshi, Canton and on-chain repo, corporate-VC stakes |
| [[tradeweb-people]] | Founder-era search-engine thinking handed to a CEO betting on frontier markets; the President role didn't stick | Who runs Tradeweb, profiles with dated quotes, where leaders' views shifted |
| [[tradeweb-outside-voices]] | A curated chorus; the few independent voices are the useful ones | Clients, dealers, non-banks, partners, skeptics, who holds power over Tradeweb |
| [[tradeweb-mission-forces]] | No formal mission; tailwinds are mandates and debt supply, the risk is venues becoming stacks | Mission lines, boilerplate drift, tailwinds and headwinds, five forces, crisis tests, 2030 scenarios |
| [[tradeweb-ai-price]] | A "30% better" pricing claim proves the floor, not the ceiling | The model price everything else is measured against; competitor landscape |
| [[tradeweb-a2a-information-leakage]] | A real but tiny leakage effect, measured with the vendor's own ruler | The May 2026 whitepaper; A2A vs voice vs SNAP+ |

**Suggested order:** people → mission-forces → outside-voices → strategy-financials → credit → a2a-leakage → ai-price → tech-ai-data → rates-em → derivatives-regulation → equities-retail.

## 2. Twenty-five-year timeline

*2001–2018 from newsroom release titles only (not read in full). 2019–2026 from the theme notes, which cite the articles.*

| Year | Event | Why it matters |
|---|---|---|
| 1996 / 1998 | Founded; dealer-to-client RFQ for US Treasuries (per later boilerplate and [[tradeweb-equities-retail]]) | The original protocol, cloned into every later market |
| 2001 | Euro sovereign market makers added; **TBA-MBS** launched; 9/11 outage, then "Resumes trading of U.S.-based products"; Moneyline Telerate licenses its data | Multi-asset and data licensing from year 5 |
| 2002 | JP Morgan takes an equity stake; **Lee Olesky** named President | Dealer ownership, the founding tension of the model |
| 2004–05 | **Thomson acquires Tradeweb**; corporate bond marketplace; **euro and USD swaps**; **CDS** platform; repo | Media-data parent, a pattern repeated with Refinitiv and LSEG |
| 2006 | Retail via LeverTrade (rebranded **Tradeweb Retail**) | Second client channel |
| 2007–08 | **Nine dealers + Thomson form a consortium** around Tradeweb; Citi joins; **Hilliard Farber** buys entry into inter-dealer (later **Dealerweb**); new CEO | Third channel (wholesale); dealers as owners *and* customers |
| 2009–10 | Barclays stake; Thomson Reuters distributes data; first fully electronic swap trade executed **and cleared** in the US | Pre-positioning for Dodd-Frank |
| 2011–12 | First electronic cleared CDS; hires SEF compliance head; European ETF platform (Oct 2012) | ETFs, the first non-fixed-income adjacency |
| 2013 | **CFTC approves TW SEF**; live SEF trading; buys **BondDesk** (retail bonds) | Regulation creates the swaps franchise ([[tradeweb-derivatives-regulation]]) |
| 2014 | **US corporate bond trading** launched (again, after the 2004 marketplace); BlackRock integrated-rates deal | The market it wins share in after 2019 |
| 2016 | **US ETF platform**; CodeStreet acquired; UK Treasury names Tradeweb and FTSE Russell as gilt and T-bill end-of-day reference price providers | First official benchmark role |
| 2017 | **All-to-all corporate trading**; Citadel Securities joins Treasuries; first offshore **Bond Connect** link; MiFID II APA | Non-bank liquidity; China |
| 2018 | Refinitiv data redistribution extended; options RFQ; Plato eBlock (European equities) | — |
| **Apr 2019** | **IPO at $27**, 40M shares (46M with greenshoe), all proceeds used to buy out banks; follow-on Oct 2019 at $42 | Banks 46% → 17.3%; Refinitiv ~54% |
| 2019 | Portfolio trading for US credit; multi-dealer PT; Tradeweb ICE UST closing prices | The PT wave |
| Mar 2020 | Platform volume >$1tn/day in COVID; follow-on at $50.25 | Electronic proven under stress |
| 2020–21 | ICE Swap Rate fallback uses Tradeweb quotes; Multi-Client Net Spotting; **"SOFR First"**; (context) LSEG completes its Refinitiv purchase | Benchmarks + rate transition |
| Jun 2021 | **Nasdaq US fixed-income platform (ex-eSpeed)**, $190M | First acquisition as a public company |
| 2023 | **Billy Hult CEO** (Jan 1); **Yieldbroker** A$125M; new LSEG data licence | — |
| 2024 | r8fin; **ICD $785M** (corporate treasurers, the fourth channel); FTSE Russell to use Tradeweb closing prices for **WGBI** | Revenue +29% |
| 2025 | FY revenue **~$2.05B (+18.9%)**, adj. EBITDA margin ~54%; SNAP+ pilot; first on-chain Treasury financing (Canton); TW SEF single-name CDS | — |
| H1 2026 | Kalshi stake and data; Crossover (crypto) round; **"Blast all → select smart"** (Mar 31); **A2A leakage whitepaper** (May 13); TARA (Jun 15); Korea joins WGBI | AI and "frontier markets" narrative |
| Jul 2026 | (context) **ICE agrees to buy MarketAxess**, ~$5.7B EV, close H1 2027 ([[tradeweb-ai-price]]) | Credit-venue consolidation begins |
| **Oct 19 2026** | **Trumid**: ~$1.97B ($1.75B business + ~$220M tax assets), ~$1.89B cash + $82M equity, close H1 2027 | Largest deal ever; first aimed at the competitive front |

## 3. Five patterns across the notes

1. **Same playbook, new market.** RFQ → automation (AiEX, 2012) → data and benchmarks → next market. Each theme note finds the same sequence in a different asset class. The cleanest examples: closing prices (gilts 2016 → UST 2019 → EGB 2023 → WGBI 2025) and ETF RFQ (EU → US → Asia).
2. **Regulation is the accelerant, and Tradeweb lobbies for more of it.** Swap mandates (2013), MiFID II (2018), LIBOR transition (2021), the Treasury clearing mandate (cash Dec 31 2026, repo Jun 30 2027) and UK/EU bond transparency (2025–26) each pushed flow onto venues. See [[tradeweb-derivatives-regulation]].
3. **Automation → data → models → more automation.** AiEX is 58% of tickets by Q1 2026 (Tradeweb's figure); each automated RFQ is a labelled training record for Ai-Price, SNAP+ and TARA. The moat is that labelled history, not the rules engine. See [[tradeweb-tech-ai-data]].
4. **Self-measured scorecards.** Ai-Price measures itself against last print; the leakage paper measures A2A with Ai-Price; SNAP+ savings are "estimated"; TRACE share uses Tradeweb's own definition, and in 2026 Tradeweb argued the denominator is inflated. Independent checks exist only for share (The DESK, Coalition Greenwich), and there they broadly agree on direction. Before quoting any Tradeweb number, ask "measured how, against what?"
5. **From builder to buyer, and from broad to selective.** 2019–2021 messaging: electronification and breadth (A2A as a "top-4 dealer"). 2026 messaging: curated dealer lists (SNAP+) and consolidation (Trumid). The two shifts fit together: a venue whose franchise is dealer relationships, facing an ICE–MarketAxess combination built on A2A, sells selectivity and buys the third credit venue. *(Inference.)*

## 4. Cross-note open questions

1. **Trumid financials**: revenue, EBITDA and the implied multiple (8-K / Oct 20 2026 investor deck), the tax assets, funding, and the antitrust read alongside ICE–MarketAxess. ([[tradeweb-strategy-financials]] §8)
2. **Independent rulers**: will Tradeweb re-run Ai-Price, leakage or SNAP+ results on a price it doesn't build? ([[tradeweb-ai-price]] §9, [[tradeweb-a2a-information-leakage]] §8)
3. **Fee capture vs volume**: revenue per $1bn ADV fell from ~$1.07M to ~$0.78M (2019→2025, derived). Mix shift or price cuts?
4. **Treasury clearing** (Dec 2026 / Jun 2027): does the mandate move dealer-to-client Treasury flow onto venues the way the swap mandate did in 2013?
5. **Frontier options**: do Kalshi, Canton/on-chain repo and Crossover move past single-trade demos by 2027?
6. **Q3 2026 results (Oct 29 2026)**: was Q2's +9.0% growth a blip?

**Links:** [[tradeweb-people]] · [[tradeweb-outside-voices]] · [[tradeweb-mission-forces]] · [[tradeweb-strategy-financials]] · [[tradeweb-credit]] · [[tradeweb-rates-em]] · [[tradeweb-derivatives-regulation]] · [[tradeweb-equities-retail]] · [[tradeweb-tech-ai-data]] · [[tradeweb-ai-price]] · [[tradeweb-a2a-information-leakage]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[wss-capital-markets-ma]] · [[wss-rates-macro]] · [[wss-credit-distressed]] · [[sec-filing-intelligence]] · [[canon-helmer-7-powers]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-porter-competitive-strategy]] · [[canon-christensen-innovators-dilemma]]

---
### Rep
Write a one-page **board memo as a Tradeweb independent director** on the Trumid deal. Use only numbers from these notes. (1) State the price as multiples of Tradeweb's FY25 adjusted EBITDA and revenue ([[tradeweb-strategy-financials]] §5). (2) Name the strategic logic in one sentence, using pattern 5 above. (3) List the three facts you would require before voting yes, drawn from §4 above. (4) Name one way the deal fails. Then compare your memo with what Tradeweb actually discloses when the 8-K and Q3 2026 results come out.

**Corpus refresh:** to update, re-run the newsroom scrape from the browser (the site blocks scripted requests; `curl` gets a Cloudflare challenge, but same-origin `fetch` from a loaded page works), then add new items to the relevant bucket and note.
