# The Wall Street Skinny — Insight Extraction (the capital-markets plumbing layer)

> Distilled from **The Wall Street Skinny** (YouTube `@TheWallStreetSkinny`, 174 long-form videos + 275 shorts,
> catalog pulled 2026-10-04). Hosts: **Kristen Kelly** (ex-Morgan Stanley investment banking) and **Jen Saarbach**
> (ex-Morgan Stanley sales & trading), plus guests from JPMorgan, Goldman, Morgan Stanley, Carlyle, Bridgewater,
> Wellington, PGIM, the FT and others. Raw transcripts at `_ingest/raw/2026-10-04/media/wall-street-skinny/{videos,shorts}/`;
> topic routing in `_clusters.json`; analyst brief in `_BRIEF.md`. Summarized in own words with brief attributed quotes,
> not reproductions.
>
> **Coverage:** 392 of 449 transcripts (169/174 long-form, 223/275 shorts). Notes were drafted from ~247 and then
> revised in a second pass once the backfill finished; each note's *Gaps* section lists only what is still missing
> (mostly music-only shorts and a handful of episodes YouTube never served).
>
> ⚠ **Bias.** Both hosts are ex-sell-side and sell courses (M&A, Excel); many guests run the asset class they are
> explaining (private credit, evergreen PE, infrastructure, home equity). Several shorts are machine-translated
> round trips with garbled units ("$3 billion" meaning trillion). Every note flags corrected figures inline.

## What this channel adds over the rest of the program

The canon owns strategy theory; [[trading-floor-mechanics]] owns how a bank floor is organized; the Tiger Sisters notes
own accessible PE/VC 101. Before this batch the program had **essentially nothing** on four layers this channel teaches well:

1. **Rates and the Fed's machinery**: bond math, duration/DV01, auctions, QE vs. Treasury buybacks, CPI vs. PCE. (Course 11, E9)
2. **Credit from the lender's side**: private credit, PIK, BDC gating, liability-management fights, recoveries. (Course 02, E2/E3)
3. **Deal and offering mechanics**: IPO pricing vs. valuation, greenshoe, accretion/dilution, financing commitments. (Course 02, E3)
4. **How the money is actually raised and held**: evergreen funds, secondaries, pod shops, and who controls the holding period. (E2, E8)

Plus a fifth, timely layer: **the financing of the AI build-out**, which links all four.

## The seven teaching notes

| Note | Concepts | The one idea to keep |
|---|---|---|
| [[wss-rates-macro]] | 17: bond yield stack, DV01/convexity, curve trades, FOMC odds, neutral rate, Fed independence, QE/QT, auctions, buybacks, repo/SOFR/swaps, Treasury futures and the basis trade, mortgages, CPI/PCE and breakevens, FX, carry and the yen carry trade, tariffs and the April 2025 safe-haven break, recession signals | Three separate levers move long rates (Fed QE, Treasury issuance and buybacks, agency MBS buying), and how a buyback is *funded* decides whether it eases or tightens. Second-pass addition: "who has balance sheet to hold duration" ties April 2025, the basis trade, negative swap spreads and dealer auction takedowns together. |
| [[wss-credit-distressed]] | 18: credit asymmetry, spreads, covenants, structural subordination, DCM and ratings, credit trading, public vs. private credit, direct lending mechanics, ABL, PIK, LBO leverage, BDCs and gating, insurer balance sheets, liability management, distressed/bankruptcy, capital solutions, CDS, private credit vs. 2008 | The agency problem has a debt side. Caesars is Jensen-Meckling played by creditors. First-lien recoveries fell from ~80 to ~60 cents mostly because loan-only structures removed the junior cushion. Lender concentration decides who gets uptiered: anonymous CLO syndicates get primed; sole lenders with maintenance covenants negotiate early. |
| [[wss-capital-markets-ma]] | 19: EV vs. equity value, bulge bracket vs. boutique, DCM (how a bond is born), IPO process, the pop, direct listings, greenshoe, float/index rules, follow-ons, block trades, SPACs, cash vs. stock, accretion/dilution, sources and uses, contested deals, spin-offs and split-offs, rollover, biotech, small-deal financing | Valuation, pricing and affordability are three different questions. Netflix walked from WBD on affordability: at a 37x P/E, stock costs ~2.7% earnings yield vs. ~4.1% after-tax debt. |
| [[wss-private-markets-wealth]] | 18: blind pools and the deployment clock, megafund vs. LMM, operating value creation, TVPI/DPI, co-invest, secondaries/continuation funds ($160bn in 2024), the distribution drought and endowment model (Yale), leverage at every layer, evergreen funds, the wealth distribution chain, the advisor (wirehouse vs. RIA vs. MFO), real estate, infrastructure and project finance, home equity, VC from the outside in, ETA, sports | The retail push is a liquidity problem: distributions are at a post-GFC low, institutions can't recommit, so managers need individual investors, and the evergreen wrapper hides costs (annual carry on unrealized marks). |
| [[wss-ai-economics]] | 17: the AI stack, chips, open vs. closed weights, power prices, grid queues, hyperscalers turning net borrowers, project finance/SPVs (Meta Hyperion terms), vendor guarantees, depreciation lives, data-center subsidies, Oracle CDS, index concentration, Situational Awareness, AI IPOs, IP, jobs, the SaaS-pocalypse | The build-out is descending a funding ladder (cash flow → bonds → off-balance-sheet SPVs → vendor guarantees → chip-backed debt). Each rung adds reach and couples risk; the binding constraint is the grid, not capital. |
| [[wss-trading-hedge-funds]] | 20: 2-and-20 on runnable capital, strategy taxonomy, indices and benchmarks, ETFs, beta/alpha, Sharpe and information ratio, pod shops, fundamental long/short, short selling and squeezes, quant, leverage spirals, DV01, repo and bank capital rules, basis trade, options and put/call, reading rates, Soros/BoE, commodities and physical oil, fundraising, Moneyball | The holding period belongs to whoever funds you. Redemptions, margin calls and pod stop-losses kill correct theses (Situational Awareness was reportedly +80% when its book was sold). |
| [[wss-technicals-career]] | 22: three-statement model, EV vs. equity, DCF, WACC and how debt changes it, EBIT/EBITDA and the interest cap, the equity check, paper LBO/IRR, sources and uses and cash-free debt-free, boutique vs. bulge bracket, who funds LBO debt, club deals, collateral and Chapter 7/11, repo fails, auctions, IPO pop, interested-party marks, research economics, comp and deferrals, carry by fund size, recruiting pipeline, finance embedded in *Industry* recaps | The equity check is the real risk dial. It sets first loss in an LBO, a first-loss hedge fund seat, and a senior banker's deferred comp; it is why 20x tech LBOs need sovereign equity. |

## The spine: one causal story across all seven notes

```
Rates set the price of money                                  [[wss-rates-macro]]
  → floating-rate borrowers squeezed; PIK toggles; covenant-lite loans
    defer the reckoning; recoveries fall                       [[wss-credit-distressed]]
  → PE exits stall; distributions dry up; the denominator binds;
    secondaries and continuation funds manufacture liquidity    [[wss-private-markets-wealth]]
  → managers turn to individual investors via evergreen funds;
    the same liquidity mismatch reappears as gating             [[wss-private-markets-wealth]] · [[wss-credit-distressed]]
  → meanwhile AI capex outgrows cash flow and walks down the
    funding ladder into exactly these private-credit and SPV pools [[wss-ai-economics]]
  → equity markets price it through mega-IPOs, follow-ons and
    deal math where affordability, not value, decides           [[wss-capital-markets-ma]]
  → and leveraged holders get forced out on the funder's clock,
    not the thesis's                                            [[wss-trading-hedge-funds]]
Underneath every link: who writes the equity check takes the first loss  [[wss-technicals-career]]
```

**With vs. without, at system level:** private credit, evergreen funds and SPVs are all *liquidity and maturity
transformation outside the banks*. With them, capital reaches borrowers banks won't fund (AI data centers, 20x LBOs,
mid-market companies) and investors get yield. Without them, that activity shrinks or returns to bank balance sheets,
where capital rules make it costlier. The cost of having them is that the run risk moves to places with slower marks
and fewer backstops. That is the 2008 comparison the channel keeps circling, and [[wss-credit-distressed]] scores it.

## Connections to the existing program

- **Canon:** [[canon-jensen-meckling-agency-theory]] (creditor and LP agency), [[canon-taleb-antifragile]] (leverage and forced
  sellers), [[canon-klarman-margin-of-safety]] (distressed buying), [[canon-mauboussin-success-equation]] (alpha vs. beta, Sharpe).
- **Practitioner notes:** [[trading-floor-mechanics]], [[bloomberg-terminal-instrumentation]], [[tiger-sisters-private-capital-101]],
  [[harlem-capital-vc-insights]], [[professional-services-leverage]], [[market-structure-24-5-trading]].
- **learn/:** [[unit-06-whats-a-business-worth]] needs enterprise value (absent until now; taught in [[wss-capital-markets-ma]]
  and [[wss-technicals-career]]). [[unit-09-capital-light-businesses]] needs a footnote: Google and Meta are turning capital-heavy
  (Google's first negative-FCF quarter; Meta FCF $8.5bn → $784m, per [[wss-ai-economics]]).
- **Scenarios:** [[wss-scenario-map]] reorganizes all seven notes by market regime (Boom, Lender's market, Drought, Shock): who wins and loses in each, which structures survive, the signal dashboard, and a FRED-based regime history since 1990 (`_ingest/regimes.py`).
- **Applied to venture:** [[apply-wss-to-venture]] runs these concepts against [[primary-venture-partners-insights]] and [[harlem-capital-vc-insights]]: the layer reaches seed VC through LPs and exits, and scale shifts the risk from fundraising to exit-window and liquidity.
- **acumen/:** candidate cases. *Caesars 2008–2017* (LBO → liability management → bankruptcy) and *Netflix vs. Paramount for WBD*
  (affordability vs. value) are both fully sourced in the notes above.

## Correction log (selected; full lists in each note)

| Claim on air | Correction | Note |
|---|---|---|
| 2008 corporate defaults "peaked at 2%" | Spec-grade defaults peaked ~10–14% | credit |
| 6x LBO leverage cap was SEC rule | 2013 interagency bank guidance | credit |
| 11 FOMC voters | 12; the NY Fed president always votes | rates |
| Foreign central banks bid "direct" at auctions | They usually show as "indirect" via the NY Fed | rates |
| Black Monday ~26% | S&P ~−20.5% | rates |
| "10 cents of oil ≈ 0.2% inflation" | Almost certainly $10/bbl | rates, trading |
| Hormuz ~10m bbl/day | ~20m | trading |
| Black-Litterman is a Black-Scholes tweak | It is a portfolio-allocation model | trading |
| "$17T private credit" | ~$1.5–2T | private markets |
| Disney/Fox ~$85bn | ~$71bn | technicals |
| UK bonus cap still binding | Scrapped 2023 | technicals |
| Credit-spread default math | Must divide by loss-given-default | AI |
| Futures DV01 = CTD DV01 × conversion factor | Divide by the conversion factor | rates, trading |
| Foreign buyers struck at April 2025 auctions | Indirect bidding was near record (~88%) | rates |
| Direct-lending premium ~100bp (quoted) | Guest said 150–250bp | credit |
| Interval funds repurchase "5–7% by law" | SEC rule allows 5–25% | credit |
| "Three rules of distressed" credited to Gatto | They are Kroboth's (Northwall); pass 1 had this wrong too | credit |
| Google raise was a $17bn convert | ~$85bn package | AI |
| Modigliani and Miller shared a Nobel | 1985 and 1990, separately | technicals |
| Continuation vehicles "50%+" of secondaries | All GP-led ~44% on the guest's own split | private markets |

Figures for 2026 events (SpaceX and Anthropic IPOs, Warsh hike, Situational Awareness) are as reported on the channel and not
independently verified. [[wss-ai-economics]] discusses Anthropic and was drafted with an Anthropic model; it says so.

## Status and remaining work

- **Two passes complete.** All seven notes were revised against the full backfill; reconstructions were replaced with
  the channel's own teaching wherever a transcript existed, and remaining self-derived arithmetic is labelled in place.
- **Still missing** (listed per note): Industry S2E2 "Giant Squid" (block trades, PWM perception), the inflation-breakevens
  explainer, Paper LBO and Rule of 72 shorts, and assorted music-only shorts.
- **Never taught by the channel** (needs another source): NAV loans, implied repo and CTD switching, swaptions,
  advisor payout grids and Reg BI, venture secondary discounts, boutique fee economics.
- **Glossary:** *Capital Markets, Credit & Rates* section in `GLOSSARY.md`.
