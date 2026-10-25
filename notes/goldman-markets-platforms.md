# Note · Goldman Sachs markets platforms — the dealer answers electronification by becoming broker, venue, principal and data distributor at once, then moves its moat to the balance sheet

> Practitioner / market-structure note · Maps to **Course 04** (Competitive Strategy — coopetition with venues, platform positioning, buyer power), **Course 10** (Entrepreneurship & Venture — building platforms inside an incumbent: Marquee, ETF Accelerator), **Course 11** (Global Strategy, Macro & Responsible Business — EU market structure, the consolidated tape, CCP policy), **Course 07** (Data, Analytics & Decision-Making — whose denominator: tickets, TRACE prints, "addressable" liquidity), **E10** (Digital & AI Transformation for Leaders — SecDB to Marquee AI) · Written 2026-10-25 · Part of [[goldman-hub]]; the dealer-side counterpart to [[tradeweb-tech-ai-data]], [[tradeweb-credit]] and [[tradeweb-equities-retail]]; companions [[goldman-strategy-financials]], [[goldman-digital-assets]], [[goldman-ai]]

- **Source:** `_ingest/raw/goldman/articles.jsonl`, **~33 items**, Apr 2019 – Oct 2026, plus five undated business pages:
  - GSET, Connectivity, Systematic Trading Strategies and the credit portfolio-trading (PT) article (undated, scraped Oct 2026).
  - The Marquee history page (2019) and 14 platform releases: AWS (2021), MSCI (2021, one-line stub), Visual Structuring (2022, 2023), MarketView (2023), ETF Accelerator (four, 2023–24), Marquee for e-Quality (2022).
  - The Investor Day 2020 deck, including the *Future of Market Structure* breakout, and the Investor Day 2023 GBM deck.
  - Five *Exchanges* transcripts: Varadhan (Apr 2020), the GameStop special (Feb 2021), the retail panel (**filed 2020-06-14 but recorded 2 and 10 June 2022**; URL slug 06-14-22), the GBM co-heads (Nov 2023), Churchman on AI (Aug 2026).
  - Two CCP releases (Oct 2019, Mar 2020), four Insights articles (Beasley 2025 and 2026, McCarthy 2026, Campbell/Isaacs 2026), the 2019 and 2025 letters (dated to fiscal year-end, published the following spring), and the Q4-2025 and Q3-2026 earnings releases.

  **Missing:** the CCP paper itself, the credit-PT report, the MSCI release body, the FICC & Equities and Prime Services pages (scraped empty), any Marquee user, revenue or pricing figure, and any Sigma X volume. **Goldman's site never names Trumid, MarketAxess or ICE, and names Tradeweb only in an ID20 footnote and the DAP release.** Everything is Goldman's own channel.
- **Core claim:** Goldman did not fight electronification; it occupied every seat around it. By 2019 it was booking **~99.9% of its US cash-equity tickets, ~75% of US credit and ~80% of energy/metals delta-one** electronically (ID20). It sells algos and smart order routing (**broker**), runs its own ATS/MTF pools, Sigma X2 and Sigma X MTF (**venue operator**), sells "GS Principal Liquidity" into those flows (**principal**), and since 2014 has pushed its pricing, risk models and third-party data to clients' desktops through Marquee (**pre-trade data distributor**). Its policy positions fit that portfolio. It co-wrote the 2019 CCP paper asking clearing houses to put up more of their own capital. Its strats called PFOF retail flow "non-participable". It wants a "modest" TRACE fix for PT prints. And it champions an EU consolidated tape that counts its **€1tn a year of off-book principal liquidity** as real liquidity. The letters stopped citing electronic share after 2020. The economic moat moved to **financing**: **19% of markets revenue in 2018 → 37% in 2025 → ~46% in Q3 2026** *(derived)*. That is the opposite bet to Tradeweb's, where the venue's automation and the data it throws off are the product.

---

## 1. Chronology — the dealer's platform spine

| Date | Event | Terms / numbers (as Goldman states them) |
|---|---|---|
| Early 1990s | **SecDB** (Securities Database): firm-wide risk aggregation built by strats | — |
| 1995 | **GS Financial Workbench**: client and employee website for research, models, trades, derivative pricing | — |
| **Jun 30 2014** | **Marquee** launched with APIs into clients' systems | "more than 20 years of historical data for select asset classes" |
| 2019-10-24 | **CCP resilience paper** with BlackRock, JPM, Allianz, Citi, SocGen, State Street, T. Rowe, Vanguard | Own-capital tranches, member ballot, assessments capped at 1x default-fund contribution, bail-in debt for resolution |
| **2020-01-29** | **Investor Day**: GM deck plus *Future of Market Structure* breakout (Nahum, Martin, Hong) | Electronic tickets ~99.9% US cash equities / ~75% US credit / ~80% energy & metals delta-one. PT "$120bn+ executed since inception". ">$2tn of liquidity supplied in 2019" (FINRA OTC blocks). Financing 19% of GS markets revenue vs 32% peer average; $1.4bn FICC financing gap |
| 2020-03-10 | Ten more firms sign the CCP paper (Barclays, Deutsche, UBS, Guardian Life, TIAA, Franklin Templeton…) | — |
| 2020-04-16 | Varadhan: FX and equities already electronic; COVID shows voice credit and derivatives can be booked electronically from home | GM printed **19.7%** in Q1 2020 vs an 11% threshold |
| 2021-02-04 | GameStop special (Marshall, Mahajan, Tuorto, Reed) | 24bn shares on US exchanges in one day; Jan 2021 equity-linked issuance $129bn (+150% YoY) |
| 2021-05-17 | GS–MSCI risk-analytics collaboration | Stub only |
| **2021-11-30** | **GS Financial Cloud for Data with AWS** (re:Invent): PlotTool Pro, GS Quant, AWS Data Exchange | Wellington, Millennium, MSCI quoted; access via GS Developer Console or AWS Marketplace |
| 2022-02-03 | Marquee for e-Quality, year 2: donation tied to FX & commodities volume on **Marquee Trader** | 2021 campaign raised $1.1m |
| 2022-06 (filed as 2020-06-14) | Retail panel: Jeria on non-participable volume; Gensler's order-by-order competition idea | Retail ~10% → 13% (zero commissions) → ~20% (summer 2020); off-exchange 35% → 45% → >50% on some days (Dec 2020–Jan 2021); steady state ~15% |
| 2022-06-02 | *(context, [[tradeweb-derivatives-regulation]])* First electronic SOFR swaption: **Goldman ↔ CDPQ** on TW SEF | — |
| **2022-09-27** | **Visual Structuring** (FX options, mobile-first, patent-pending), Amsterdam | — |
| 2022-11 | **ETF Accelerator** introduced (date per the Oct 2023 release) | — |
| 2023-04-17 | Visual Structuring adds equities, crypto, precious metals; web and Android | — |
| 2023-10-05 → 2024-06-27 | Accelerator listings: Brandes ×3 (Cboe), GMO QLTY (NYSE), Eagle EAGL (NYSE Arca; first SMA conversion, 5th fund), Ultramarin/Baader UCITS (XETRA; 6th fund, first EMEA) | ETFs "with assets over $3 billion" launched to Jun 2024 |
| **2023-11-14** | **Marquee MarketView**: dashboards with LSEG, FactSet, MSCI, Axioma, Wolfe data | Widget authoring needs a PlotTool Pro subscription |
| 2023-11-21 | Varadhan: biggest fear is automation going wrong, found "after the fact" | — |
| Undated (2026 scrape) | **GSET** page: algos, SOR, low-latency DMA, sponsored access, Sigma X2 (US ATS, Form ATS-N), Sigma X MTF, Sigma X Japan/HK/Australia; **Atlas** equities platform rebuild | No volumes |
| Undated | *Where Next for Credit Portfolio Trading?* (unnamed Co-Head of US Credit Trading) | "less than 1% of TRACE prints" to be adjusted |
| **2025-10-24** | Beasley with New Financial: UK & EU market structure | Lit primary ~30% of reported volume; addressable liquidity >2x primary; €1tn principal liquidity in 2024; 17 CCPs / 31 CSDs; post-trade costs 50–100% higher than US |
| 2025 (FY) | Letter: financing businesses **37%** of FICC+Equities revenue, 17% CAGR since 2021 | — |
| 2026-03-10 | McCarthy (GSAM): bond ETFs forced dealers to build basket technology | Active ETFs ~$1.8tn, 53% organic growth (2025) |
| **2026-07-27** | Beasley/Whitehead: EU consolidated tape due "in the coming weeks"; UK next year, interim daily feed first | Off-book = 40% of addressable liquidity; EU tape free for retail |
| 2026-08-18 | Campbell/Isaacs: US ETFs | >$1tn inflows H1 2026, >$2tn expected (+40%); $16.1tn AUM; GS ETF trading volumes +50% on 2025 |
| 2026-08-24 | Churchman: **Marquee AI**, "only available internally right now" | — |
| 2026-10-13 | Q3 2026: Equities financing **$3.37bn** > intermediation **$3.08bn** | — |
| 2026-10-19 | *(context, [[tradeweb-strategy-financials]])* Tradeweb agrees to buy Trumid (~$1.97B); **Goldman advises Trumid** | — |

## 2. The numbers

**Electronic share, 2019 (ID20, slide 11 footnote).** These are Goldman's *own* "electronic tickets as a percentage of total", not market shares:

| Business | Electronic share of GS tickets | Claim attached |
|---|---|---|
| US cash equities | ~99.9% | *#1 provider of institutional principal liquidity* (>$2tn supplied in 2019; FINRA OTC trades of 10,000+ shares and $200k+, Oct–Nov 2019) |
| US credit | ~75% | "#1 IG Systematic"; PT "$120bn+ executed since inception" |
| Energy & metals delta-one | ~80% | Commodities via eAron |

**Market-structure breakout (ID20).** Catalysts: regulation (Reg NMS, Dodd-Frank, Volcker, MiFID II, MAR, margin and stay rules, MMF reform, Brexit), technology (data to 175 ZB by 2025E; internal US cash-equity execution down to 0.35 micros by 2019) and passive growth. Its swap example routes a GS entity through a SEF and a CCP, the dealer-on-venue model. The credit "ecosystem" slide lists single-bond, algo, PT and bond ETFs delivered via multilateral venues, bilateral APIs, EMS and Marquee. It cites >6m daily price updates, 32,000 CUSIPs priced, GS liquidity in >15,000 CUSIPs and >10,000 inquiries a day. *(The slide text is jumbled in extraction, so these pairings follow the reader notes.)* Systematic equities wallet: $1.8bn (2012) → $3.6bn (2018), with a ~$1bn revenue gap to close.

**Financing, the moat that grew** (ID20; L25; Q4-25 and Q3-26 releases):

| Period | FICC fin. | Equities fin. | FICC + Equities | Financing share |
|---|---|---|---|---|
| 2018 | — | — | — | **19%** (US peers 32%) |
| 2022 | — | — | — | $7.1bn total financing (ID23 GBM) |
| FY2025 | $4.25bn | $7.20bn | $31.06bn | **36.9%** *(derived; the letter says 37%)* |
| Q3 2026 | $1.207bn | $3.365bn | $9.912bn | **46.1%** *(derived)* |

**Platforms with numbers:** Marquee Trader volumes funded $1.1m of donations (2021). ETF Accelerator: 6 funds, >$3bn, in ~19 months. That is the full public tally. **No Marquee user count, revenue or price appears anywhere in the corpus.**

**ETF plumbing (Aug 2026):** "in times of market stress, ETFs are accounting for 40% of the tape at times." The industry trades ~$320bn notional a day. There are >6,000 US ETFs, more than single stocks. Model-portfolio ETF assets are up 46% to $950bn.

## 3. The five seats, and how each one was narrated

1. **Broker (GSET, Connectivity).** Algos, SOR to "exchanges and a majority of non-displayed venues", DMA, sponsored access, FIX into "all major EMS/OMS platforms". Distribution runs through other people's workflow, not a proprietary terminal. **Atlas** is the multi-year rebuild, "designed for lower latency, increased capacity and support for new workflows and client customizations".
2. **Venue operator (Sigma X).** Sigma X2 (US ATS, with Form ATS-N and monthly metrics linked but not scraped), Sigma X MTF (Europe), and pools in Japan, Hong Kong and Australia. Its algorithms "may access unique off-exchange GS Principal Liquidity and potentially receive performance benefits including price or size improvement". The same firm routes the order, runs the pool and can take the other side.
3. **Principal liquidity provider.** ">$2tn" in US equities (2019). "In 2024 alone we provided over €1 trillion of principal liquidity in European equities to our clients" (Beasley). It is pitched as protection from leakage: "the more information you put into the marketplace, the more you're going to show your intentions and the worse your performance will be."
4. **Pre-trade data distributor (Marquee).**
   - **2014:** clients get "the same pricing data, risk models, and proprietary datasets used by Goldman Sachs traders and risk managers".
   - **2020:** Marquee is "Goldman Sachs' digital storefront for institutional client services" (ID20).
   - **2021:** the AWS cloud lets clients put their own data next to GS's.
   - **2022:** Visual Structuring targets the step *before* execution: "the vast majority of a trader's time is spent during the ideation process".
   - **2023:** MarketView makes GS a redistributor of rivals' content ("partner vendors… in an open ecosystem").
   - **2026:** Marquee AI, internal only, tries to "attribute everything to a source, a specific line in each source".
5. **Rule-shaper.** CCPs (2019–20), PFOF and auctions (2022), TRACE (undated), the EU tape and post-trade consolidation (2025–26). Each is covered in §4.

**How the story shifted.** In **2019–20** the firm sold electronic share and platform *("a once-in-a-generation period of significant regulatory and technological change"*, 2019 letter). In **2021–23** the vocabulary was products and partners (AWS, MSCI, Visual Structuring, MarketView, the Accelerator). In **2023–26** it was durability: GBM "raising the floor", financing as "a ballast to our results" (2025 letter), and operational risk from automation (Varadhan: "so much of our workflow has migrated through technological automation"). Electronic share disappears from the letters after the 2020 deck, which suggests it became table stakes. *(Inference.)*

## 4. Market-structure positions, read as a portfolio

| Issue | Goldman's position (verbatim where quoted) | Which seat it protects *(inference)* |
|---|---|---|
| **CCP resilience** (Oct 2019, Mar 2020) | CCPs should make "material contributions of their own capital to the default waterfall in two separate tranches"; member assessments "capped at one times each clearing member's default fund contribution"; bail-in debt for resolution. Guardian Life: clearing "has also increased dependence on central clearing counterparties and created a concentration of risk." | The clearing member's balance sheet. Shift tail loss from members to CCP owners (exchanges) |
| **Clearing in GameStop** (Feb 2021) | Marshall: "Clearinghouses help to ensure that brokers and clients have enough collateral to cover their trades in stock and options." Declines to opine on regulating retail apps | Neutral on rules that hurt retail brokers, not GS |
| **Retail/PFOF** (Jun 2022) | Jeria: "Because these trades happen on a bilateral basis, they are non-participable from other market participants." "Trading costs skyrocketed across the broad spectrum of all stocks that our clients were trading." On Gensler's auctions: "the devil will be in the details." | The institutional agency algo business (POV/VWAP clients), whose cost rose when wholesalers internalized retail |
| **Credit PT and TRACE** (undated) | "A modest adjustment to less than 1% of TRACE prints could improve execution quality in even the most illiquid bonds and through market cycles." | The PT principal desk ($120bn+ by 2020). Presumably less information leakage from basket prints *(the report isn't in the corpus)* |
| **EU consolidated tape** (2025–26) | "This transparency will show that our markets are far more liquid than people realize, encouraging greater global investment in the region." The tapes "could also make market data cheaper to access". | The systematic internalizer: off-book flow gets *counted* as liquidity without being pushed back to lit books; exchange data fees fall |
| **Supervision & stability** (2025) | Wants "participants who are conducting like-for-like businesses are supervised in the same way"; "my hope is that European regulators recognize the value of stability." | Status quo for SIs; a level field against exchanges and PTFs |
| **Post-trade** (2025) | "Europe has 17 central counterparties for clearing and 31 central securities depositaries for settlement across 31 different countries." | Lower operating cost for a pan-European dealer |

The common thread: **Goldman backs transparency and mutualized infrastructure where it lowers its costs or legitimizes its off-exchange role, and keeps proprietary the seats that need a balance sheet.** *(Inference; the same pattern appears in [[goldman-digital-assets]].)*

## 5. Against Tradeweb's thesis: who owns the data?

| | Tradeweb (venue) | Goldman (dealer) |
|---|---|---|
| **Thesis** | Automation is the product; the flow's data is the business ([[tradeweb-tech-ai-data]]) | Own the client's *pre-trade* workflow and the balance sheet behind execution |
| **Reference price** | Ai-Price, Tradeweb FTSE closing prices (WGBI source); market-data revenue $76.5M (FY20) → $133.7M (FY25) ([[tradeweb-ai-price]] §6) | Marquee pricing and risk models from SecDB; revenue never disclosed |
| **Credit PT** | Sells PT as a protocol; argues the TRACE *denominator* is inflated by affiliate prints (>9% of IG TRACE, Q1 2026) ([[tradeweb-credit]]) | Is the PT principal; asks to change how <1% of TRACE *prints* are treated |
| **ETFs** | US ETF RFQ $930bn in 2025 ([[tradeweb-equities-retail]]) | Issuer (GSAM), AP, market maker, launch platform (Accelerator), and the trading desk that sees "40% of the tape" in stress |
| **Tapes** | With Bloomberg and MarketAxess, tried to *run* the EU bond tape; JV abandoned Dec 8 2023 ([[tradeweb-derivatives-regulation]]) | Wants the equity tape to *count* off-book liquidity |
| **Ownership** | Dealers' stake fell from 46% to 17.3% at the 2019 IPO. ID20 strips "Tradeweb gains" from peer revenue (JPM ~$335mm, Citi $355mm, UBS $38mm, DB €101mm, Barclays £126mm) and lists none for GS *(whether GS booked one isn't stated)* | Launch dealer on venues (SOFR swaption, 2022), adviser to Trumid (2026), co-investor in Digital Asset ([[goldman-digital-assets]]) |

**Reading.** The venue wants to own the data exhaust. The dealer wants to own the ideation screen upstream and the risk downstream, and is content for venues to own the middle as long as it keeps quoting there. Consolidation in that middle (ICE–MarketAxess, Jul 30 2026; Tradeweb–Trumid, Oct 19 2026) raises venue bargaining power over dealers. Goldman's hedges are principal liquidity, its own pools and Marquee. *(Inference.)* Bloomberg ([[bloomberg-hub]]) and LSEG Workspace ([[lseg-hub]]) are the desktops Marquee competes with, though no release says so; ICE ([[ice-hub]]) and MarketAxess ([[marketaxess-hub]]) are the venues Goldman never names.

## 6. What the claims don't prove

1. **"Electronic share" is a ticket count, not a dollar share or a market share.** ~99.9% of tickets says nothing about how much *notional* trades electronically, and large blocks are the voice tail.
2. **Rankings are self-selected.** *#1 provider of institutional principal liquidity* uses a FINRA block filter (10,000+ shares and $200k+) over two months. "#1 IG Systematic" has no stated source.
3. **Marquee economics are invisible.** There are no users, revenue, pricing or retention figures. PlotTool Pro is the only paid tier named. The e-Quality donation implies Marquee Trader volume, but the rate isn't given.
4. **"Addressable liquidity" is GS's co-authored measure.** The New Financial report was produced "in partnership with Goldman Sachs". Counting SI and off-book flow as addressable is exactly the definition that flatters an internalizer.
5. **The €1tn has no denominator.** No total European volume is given, so GS's share can't be computed from the corpus.
6. **The TRACE proposal is unread.** The article is undated and its author unnamed, and the report is not in the corpus. We don't know whether it predates the May 15 2023 FINRA PT flag ([[tradeweb-credit]]).
7. **The retail numbers are strats' estimates on a podcast.** "Other market participants" cited 30% retail. The 2022 recording date is mislabelled as 2020 in the corpus.
8. **The ETF Accelerator tally stops in mid-2024.** No later release appears, so scale after six funds is unknown.
9. **No outside critic appears.** No exchange, venue, regulator or retail broker answers Goldman on PFOF, the tape or CCPs anywhere in the corpus.

## 7. Strategic read *(inference throughout)*

- **Electronification compresses the flow spread, so the dealer monetizes the balance sheet.** Financing went from 19% to 37% to ~46% of markets revenue. Prime, repo and structured lending need capital and credit judgement, which venues can't copy. This is the strategic answer to Tradeweb's automation-is-the-product thesis.
- **Sigma X plus principal liquidity is the internalizer's flywheel.** More client algo flow gives more internal crossing, less leakage, better fills and then more flow. The EU tape helps this flywheel by making off-book volume visible, so investors size up in Europe without the flow moving back to lit books.
- **Marquee is a move upstream of the RFQ.** If ideas are priced in a Goldman tool (Visual Structuring, MarketView), the trade is more likely to land at Goldman, whatever venue prints it. Redistributing LSEG, FactSet and MSCI data makes Marquee a *place*, not a feed. But the tool lacks the network effect of a multi-dealer venue: clients use Marquee for Goldman, not for the market.
- **CCP and post-trade positions reduce the dealer's tail and operating cost.** Members want owners' skin in the game and fewer European plumbing silos.
- **Coopetition with venues is the steady state.** Goldman is launch dealer, co-investor (Digital Asset) and banker (Trumid) to the venues that compress its spreads.
- **Automation risk replaced market risk** (Varadhan, 2023). That is the cost of the ~99.9%.

## 8. Canon lenses

- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): venues are complementors for distribution and competitors for data. Goldman quotes on Tradeweb, advises Trumid and co-funds Digital Asset.
- **Multi-sided platforms** ([[canon-hagiu-wright-multi-sided-platforms]], [[canon-parker-platform-revolution]]): Sigma X is a two-sided pool with the operator as a possible counterparty. That is the conflict the ATS-N form exists to disclose.
- **Information rules** ([[canon-shapiro-varian-information-rules]]): MarketView's "open ecosystem" lowers switching costs to attract users, then builds lock-in through client-authored widgets and PlotTool history.
- **Power** ([[canon-helmer-7-powers]]): the balance sheet is a cornered resource with scale economies. Marquee shows little network power.
- **Adverse selection** ([[canon-akerlof-market-for-lemons]]): wholesalers internalize uninformed retail flow and leave institutions trading against what remains. "Non-participable" names that cost.
- **Normal accidents** ([[canon-perrow-normal-accidents]]): tightly coupled automation ("the proliferation that can transpire") and concentrated CCPs are the system risks the firm itself names.
- **Sustaining innovation** ([[canon-christensen-innovators-dilemma]]): every platform here sustains the dealer franchise; none cannibalizes it.

## 9. Practitioner counterpoint

- **Bull:** Goldman occupies every profitable seat. It is in the agency, venue, principal, data and financing seats, plus the advisory seat when venues sell. Financing at ~46% of markets revenue in Q3 2026 and record ETF volumes (+50%) show the model working. Its policy stances are publicly reasoned and broadly shared (nine CCP co-authors, ten more signers).
- **Skeptic:** the seats conflict. The broker routes to its own pool, where its principal desk may trade against the order. Its strats lament non-participable retail flow while it internalizes €1tn of European flow. Its tape advocacy is built on a measure it co-defined. Marquee has run for twelve years with no disclosed economics, which suggests it is a cost of sales, not a business.
- **Synthesis:** judge the model by *client* TCA, not by Goldman's tallies. Ask for Sigma X fill quality versus lit venues (ATS-N metrics), Marquee-originated flow share, and the financing mix through a deleveraging. Read every position paper as a statement of which seat it protects.

## 10. Open questions to track

1. Does the 10-K or any IR deck ever size Marquee: users, revenue, or flow it originates?
2. Sigma X2 monthly metrics: what volume and fill rate does the pool post against peers?
3. The EU tape went live in 2026. Do European order sizes and foreign allocations actually rise, as Beasley predicts, and does SI share hold?
4. Does FINRA adopt a PT-print change matching Goldman's "<1% of prints" ask, alongside SR-FINRA-2026-009 ([[tradeweb-credit]])?
5. Does financing hold above 40% of markets revenue when volatility and prime balances fall?
6. Does ICE–MarketAxess plus Tradeweb–Trumid change dealer economics in US credit, and does Goldman respond via its own pools or PT?
7. Does Marquee AI go client-facing, and is it priced?
8. Does the ETF Accelerator publish anything after 2024 (fund count, AUM), and how does it fit with the Innovator and NEOS acquisitions ([[goldman-awm-private-credit]])?

**Links:** [[goldman-hub]] · [[goldman-strategy-financials]] (financing table) · [[goldman-digital-assets]] (the same mutualize-or-own pattern) · [[goldman-ai]] (Marquee AI) · [[goldman-awm-private-credit]] · [[goldman-people]] · [[tradeweb-hub]] · [[tradeweb-tech-ai-data]] · [[tradeweb-credit]] · [[tradeweb-equities-retail]] · [[tradeweb-derivatives-regulation]] · [[tradeweb-ai-price]] · [[tradeweb-strategy-financials]] · [[bloomberg-hub]] · [[lseg-hub]] · [[marketaxess-hub]] · [[ice-hub]] · [[market-structure-24-5-trading]] · [[trading-floor-mechanics]] · [[wss-trading-hedge-funds]] · [[wss-credit-distressed]] · [[bloomberg-terminal-instrumentation]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-hagiu-wright-multi-sided-platforms]] · [[canon-shapiro-varian-information-rules]] · [[canon-helmer-7-powers]] · [[canon-akerlof-market-for-lemons]] · [[canon-perrow-normal-accidents]]

---
### Rep
Three computations with this note's numbers, then a one-paragraph judgement.

**(a) The moat moved.** From the Q4-2025 and Q3-2026 releases, compute financing as a share of FICC+Equities revenue. *(Answer: FY2025 (4.25 + 7.20) / (14.52 + 16.54) = 11.45 / 31.06 = **36.9%**. Q3 2026 (1.207 + 3.365) / (3.471 + 6.441) = 4.572 / 9.912 = **46.1%**.)* Against 19% in 2018, how many percentage points did financing's share rise in under eight years? *(+27pp.)* Name one reason the quarterly figure may overstate the trend.

**(b) Non-participable volume.** A client sends a POV algo at 10% of a stock's *total* volume, but only lit and participable venues can be accessed. Compute the share of *participable* volume the algo must take when off-exchange is 35% (pre-COVID) and >50% (Jan 2021 peak days). *(Answer: 0.10 / 0.65 = **15.4%**; 0.10 / 0.50 = **20%**, a 30% jump in footprint.)* Explain in two sentences why Jeria's "trading costs skyrocketed" follows from this.

**(c) The tape and order sizing.** A global PM caps European orders at 10% of *visible* daily volume and today sees only the lit primary market (~30% of reported volume). By what factor can the cap grow if the tape shows all reported volume? *(1 / 0.30 = **3.3×**.)* Beasley's report puts *addressable* liquidity at >2× primary. Recompute on that basis *(≥**2×**)* and say which number Goldman's internalizer business needs investors to believe, and why.

**Judgement:** in one paragraph, decide whether Goldman should spin Marquee out as an industry-owned data platform, the way it did GS DAP. Use §5 and the absence of disclosed Marquee economics.

---
**Sources:** [GSET electronic trading, undated](https://www.goldmansachs.com/what-we-do/ficc-and-equities/gset-equities) · [Connectivity, undated](https://www.goldmansachs.com/what-we-do/ficc-and-equities/connectivity) · [Systematic Trading Strategies, undated](https://www.goldmansachs.com/what-we-do/ficc-and-equities/systematic-trading-strategies) · [Credit portfolio trading, undated](https://www.goldmansachs.com/what-we-do/ficc-and-equities/insights/articles/where-next-for-credit-portfolio-trading) · [Marquee history, Apr 18 2019](https://www.goldmansachs.com/our-firm/history/moments/2014-marquee) · [CCP paper, Oct 24 2019](https://www.goldmansachs.com/pressroom/press-releases/2019/safety-soundness-clearing-houses) · [2019 letter, Dec 31 2019](https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2019-annual-report/letter-to-shareholders-2019.pdf) · [Investor Day 2020 deck, Jan 29 2020](https://www.goldmansachs.com/investor-relations/investor-day-2020/presentations/consolidated-presentations.pdf) · [CCP signatories, Mar 10 2020](https://www.goldmansachs.com/pressroom/press-releases/2020/clearinghouses-march-2020) · [Varadhan, Apr 16 2020](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/04-16-2020-ashok-varadhan) · [Retail special, Feb 4 2021](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-04-2021-the-rise-of-retail-investing-and-its-impact) · [GS–MSCI, May 17 2021](https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-and-msci-announcement) · [AWS Financial Cloud, Nov 30 2021](https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-aws-announcement-30-nov-2021) · [Marquee for e-Quality, Feb 3 2022](https://www.goldmansachs.com/pressroom/press-releases/2022/marquee-for-e-quality) · [Retail panel, Jun 14 2022](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/06-14-22-marshall-tuorto-jeria) · [Visual Structuring, Sep 27 2022](https://www.goldmansachs.com/pressroom/press-releases/2022/goldman-sachs-announces-launch-of-visual-structuring) · [Investor Day 2023 GBM, Feb 28 2023](https://www.goldmansachs.com/investor-relations/investor-day-2023/multimedia/presentations/pdfs/global-banking-and-markets.pdf) · [Visual Structuring expands, Apr 17 2023](https://www.goldmansachs.com/pressroom/press-releases/2023/gs-expands-visual-structuring-into-equities-crypto-and-precious-metals) · [ETF Accelerator first funds, Oct 5 2023](https://www.goldmansachs.com/pressroom/press-releases/2023/goldman-sachs-launch-of-first-funds-through-etf-accelerator) · [MarketView, Nov 14 2023](https://www.goldmansachs.com/pressroom/press-releases/2023/goldman-sachs-launches-marquee-marketview) · [GMO ETF, Nov 15 2023](https://www.goldmansachs.com/pressroom/press-releases/2023/gs-etf-accelerator-gmo-launch) · [GBM co-heads, Nov 21 2023](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/11-21-23-esposito-dees-varadhan) · [Eagle ETF, Mar 25 2024](https://www.goldmansachs.com/pressroom/press-releases/2024/gs-etf-accelerator-new-fund-launched) · [First EMEA ETF, Jun 27 2024](https://www.goldmansachs.com/pressroom/press-releases/2024/etf-accelerator-announces-first-fund-launched-in-emea) · [UK & EU markets, Oct 24 2025](https://www.goldmansachs.com/insights/articles/how-well-are-uk-eu-stock-markets-working) · [2025 letter, Dec 31 2025](https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2025/letter-to-shareholders.pdf) · [Active ETFs, Mar 10 2026](https://www.goldmansachs.com/insights/articles/why-active-etfs-are-gaining-momentum-as-investors-seek-new-solutions) · [EU consolidated tape, Jul 27 2026](https://www.goldmansachs.com/insights/articles/europes-consolidated-stock-market-tape-could-invigorate-and-boost-investment) · [ETFs $2T, Aug 18 2026](https://www.goldmansachs.com/insights/articles/why-etfs-are-expected-to-draw-2-trillion-in-investments-in-2026) · [Churchman on AI, Aug 24 2026](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/building-ai-systems-for-capital-markets)
