# Bucket G — Markets platforms, electronic trading, retail flows, market structure (notes)

Source: `G-markets-platforms.jsonl`, 77 items. Every item was read in full. Quotes were checked by script against the source text. Transcript quotes marked † cross a PDF line break in the source; the only change is that each newline was replaced by a single space.

## 1. Items read

**77 items in all.** About 45 are IR-event stubs: a speaker, a date, and forward-looking boilerplate. The decks themselves are *not* in the corpus. Three business pages are **empty**: FICC and Equities (#6), **Our Purpose and Values (#7)** and Prime Services (#8). There is also **no 2019 CCP / clearing-house letter in this bucket.** I grepped for "clearing" and "CCP" and found only the 2021 Marshall remark and the 2025 Beasley post-trade remarks. So the "clearing-house safety (2019 CCP letter)" focus can't be served from G. Check other buckets.

Notable items:
- (undated) **GSET Electronic Trading page.** Algos, SOR, low-latency DMA, sponsored access, "GS Principal Liquidity", the SIGMA X pools, and the new **Atlas** equities platform.
- (undated) **Systematic Trading Strategies.** QIS indices, i-Select on Marquee, the Developer API.
- (undated) **Connectivity.** FIX into every major EMS/OMS across equities, futures, options and synthetics.
- (undated) **Where Next for Credit Portfolio Trading?** Proposes a TRACE reform. The author is identified only as "Co-Head of U.S. Credit Trading".
- (undated) **Custody Solutions.** An RIA custodian sponsored by GBM. Two pages, both thin.
- 2019-04-18 **"With Marquee, Institutions Access Data…"** History of SecDB, then Financial Workbench (1995), then Marquee (30 Jun 2014).
- 2020-03-01 **Solomon all-staff COVID email.**
- 2020-04-16 **Exchanges: Ashok Varadhan, "How Markets Have 'Changed Forever'".** Full transcript.
- 2020-06-14 **Exchanges: "How Retail Investors Are Shaping Markets"** (Marshall, Tuorto, Jeria). **Date flag:** the file says 2020-06-14, but the transcript was recorded **2 and 10 June 2022** and the URL slug is 06-14-22. Treat it as **2022-06-14**.
- 2020-06-18 / 2020-07-17 **Markets Update** blurbs: Berlinski on retail and day trading; Esposito on a "gritty" Q2. Blurbs only, no transcript.
- 2021-02-04 **Special episode: Rise of Retail Investing** (Marshall, Mahajan, Tuorto, Reed). Recorded during the GameStop week.
- 2021-05-17 **GS–MSCI collaboration** (one-line stub; the PDF is not included).
- 2021-07-02 **Hari Moorthy on Transaction Banking** (UK launch).
- 2021-10-17 **Full ownership of the China JV** (GSGH).
- 2021-10-20 **AmEx × GS TxB** B2B payments.
- 2021-11-30 **GS Financial Cloud for Data with AWS.**
- 2022-02-03 **Marquee for e-Quality.** A charity donation tied to FX and commodities volumes on Marquee Trader.
- 2022-09-27 **Visual Structuring** launch (FX options, mobile-first).
- 2022-10-18 Carey Halio on Q3 2022 and the "purposeful business realignment".
- 2023-10-05 / 2023-11-15 / 2024-03-25 / 2024-06-27 **ETF Accelerator.** Launches for Brandes, GMO, Eagle, and Ultramarin/Baader.
- 2023-11-14 **Marquee MarketView** launch.
- 2023-11-21 **Exchanges: the GBM co-heads** (Dees, Esposito, Varadhan).
- 2024-01-10 **Solomon at the Global Affairs Summit** (geopolitics and AI).
- 2025-02-26 **KC McClure and John Waldron join the Board.**
- 2025-06-25 **Solomon in Les Echos:** "Europe Has an Opportunity to Seize".
- 2025-08-14 **Waldron in the FT:** "Strategic Interdependence".
- 2025-10-24 **"How Well Are UK & EU Stock Markets Working?"** (Eleanor Beasley; New Financial report).
- 2026-02-12 **Exchanges Great Investors: David Craver (Lone Pine)**, hosted by Tony Pasquariello.
- 2026-03-10 **Active ETFs** (Brendan McCarthy, GSAM).
- 2026-07-27 **Europe's consolidated tape** (Beasley, Bertie Whitehead).
- 2026-08-18 **ETFs on track for $2T of flows in 2026** (Tom Campbell, Jackson Isaacs).
- 2019-02-12 → 2026-09-16: **IR conference stubs** (Credit Suisse, Bernstein, BofA, Wolfe FinTech, Barclays, UBS, GS US Financials, fixed-income calls). The texts are boilerplate only. The *changing* boilerplate is still informative; see §8. **Date flag:** #12 is dated 2019-11-05 but describes Waldron's Bernstein talk on 31 May 2019.

## 2. Key events

- 2014-06-30: Marquee launched, giving clients API access to "the same pricing data, risk models, and proprietary datasets" used by GS traders. https://www.goldmansachs.com/our-firm/history/moments/2014-marquee
- 2020-03-01: Solomon's COVID email to staff restricts non-essential international travel. https://www.goldmansachs.com/pressroom/announcements/2020/03-01-2020-sharing-thoughts
- 2020-04-15: Varadhan says Global Markets printed a **19.7%** return in Q1 2020, against the 11% threshold set at Investor Day. https://www.goldmansachs.com/insights/goldman-sachs-exchanges/04-16-2020-ashok-varadhan
- 2021-02-01/02: Retail special recorded. **24bn shares** traded on US exchanges in one day, beating the October 2008 record. Jan 2021 equity-linked issuance was **$129bn** globally (+150% YoY). https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-04-2021-the-rise-of-retail-investing-and-its-impact
- 2021-05-17: GS–MSCI risk-analytics collaboration. https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-and-msci-announcement
- 2021-07-02: Transaction Banking launches in the UK, one year after the US launch. Moorthy sizes the UK wallet at $20–30bn. https://www.goldmansachs.com/insights/articles/from_briefings_02-july-2021
- 2021-10-17: CSRC approves full ownership of GSGH, to be renamed Goldman Sachs (China) Securities. https://www.goldmansachs.com/pressroom/press-releases/2021/announcement-17-oct-2021
- 2021-10-20: AmEx virtual cards are embedded in the GS TxB platform. General availability is planned for early 2022. https://www.goldmansachs.com/pressroom/press-releases/2021/integrated-digital-payments-20-Oct-2021
- 2021-11-30: GS Financial Cloud for Data with AWS announced at re:Invent. It covers PlotTool Pro, GS Quant and AWS Data Exchange, with Wellington, Millennium and MSCI quoted. https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-aws-announcement-30-nov-2021
- 2022-02-03: Marquee for e-Quality runs for a second year. The 2021 campaign raised $1.1m. https://www.goldmansachs.com/pressroom/press-releases/2022/marquee-for-e-quality
- 2022-09-27: Visual Structuring launched in Amsterdam: FX options first, patent-pending, mobile-first. https://www.goldmansachs.com/pressroom/press-releases/2022/goldman-sachs-announces-launch-of-visual-structuring
- 2022-10-18: Q3 2022 results and the announcement of a "purposeful business realignment". https://www.goldmansachs.com/investor-relations/presentations/2022/2022-10-18-q3-results-video
- 2022-11: ETF Accelerator introduced (date per the 2023 release).
- 2023-10-05: First ETF Accelerator funds list: three Brandes active ETFs on Cboe. https://www.goldmansachs.com/pressroom/press-releases/2023/goldman-sachs-launch-of-first-funds-through-etf-accelerator
- 2023-11-14: Marquee MarketView launched, with data partners LSEG, FactSet, MSCI, Axioma and Wolfe. https://www.goldmansachs.com/pressroom/press-releases/2023/goldman-sachs-launches-marquee-marketview
- 2023-11-15: GMO's first ETF (QLTY, NYSE) lists through the Accelerator. https://www.goldmansachs.com/pressroom/press-releases/2023/gs-etf-accelerator-gmo-launch
- 2024-03-25: Eagle Capital's EAGL is the 5th Accelerator ETF and the first SMA conversion. https://www.goldmansachs.com/pressroom/press-releases/2024/gs-etf-accelerator-new-fund-launched
- 2024-06-27: The first EMEA Accelerator fund (Ultramarin/Baader, an AI-driven UCITS ETF on XETRA) is the 6th fund. Funds launched through the platform total more than **$3bn**. https://www.goldmansachs.com/pressroom/press-releases/2024/etf-accelerator-announces-first-fund-launched-in-emea
- 2025-02-26: Waldron joins the Board (non-independent), alongside KC McClure. https://www.goldmansachs.com/pressroom/press-releases/2025/kc-mcclure-and-john-waldron-join-goldman-sachs-board-of-directors
- 2025-10-24: GS and New Financial report that European "addressable liquidity" is more than 2x primary-exchange volume. GS provided more than **€1tn** of principal liquidity in European equities in 2024. https://www.goldmansachs.com/insights/articles/how-well-are-uk-eu-stock-markets-working
- 2026-07-27: The EU consolidated tape is due "in the coming weeks". The UK follows the next year, with an interim daily-activity feed first. https://www.goldmansachs.com/insights/articles/europes-consolidated-stock-market-tape-could-invigorate-and-boost-investment
- 2026-08-18: US ETF inflows top **$1tn in H1 2026**, with more than $2tn expected for the year (+40%). GS ETF trading volumes are up 50% on 2025. https://www.goldmansachs.com/insights/articles/why-etfs-are-expected-to-draw-2-trillion-in-investments-in-2026

## 3. People & views

**Ashok Varadhan** (co-head of Global Markets, later co-head of GBM). In 2020 he frames markets as a relay and stresses humility about a strong quarter. Electronification was already complete in FX, equities and some government bonds, and COVID showed that voice-traded credit and derivatives could also be booked electronically from home. In 2023 his biggest fear has moved from market risk to *operational risk from automation*.
> "Global Markets is the transmission mechanism for all of these things." — Ashok Varadhan, Global Co-Head, Global Markets (2020-04-16, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/04-16-2020-ashok-varadhan)

> "returns will be an output, not an input." — Ashok Varadhan, Global Co-Head, Global Markets (2020-04-16, same URL)

> "there's always a newspaper article about the person that left not a newspaper article about the quality of the team that stays behind." † — Ashok Varadhan (2020-04-16, same URL)

> "so much of our workflow has migrated through technological automation" † — Ashok Varadhan, Co-Head, GBM (2023-11-21, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/11-21-23-esposito-dees-varadhan)

> "the pandemic, subsequent to the financial crisis, frankly, from, like, a markets perspective felt like nothing." † — Ashok Varadhan (2023-11-21, same URL)

**David Jeria** (Head of Electronic Trading Strats). This is the clearest market-structure voice in the bucket. Retail flow is internalized off-exchange through PFOF, which makes it "non-participable" for institutional algos and raised their trading costs. His figures: off-exchange share went from 35% to 45% (summer 2020) to above 50% on some days in Dec 2020 and Jan 2021. Retail share went from about 10% to about 13% after zero commissions, to about 20% during COVID, with a forecast steady state near 15%. He gives Gensler's 2022 order-by-order competition and auction idea a cautious welcome ("devil will be in the details").
> "Because these trades happen on a bilateral basis, they are non-participable from other market participants." † — David Jeria, Head of Electronic Trading Strats (2022-06, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/06-14-22-marshall-tuorto-jeria)

> "Trading costs skyrocketed across the broad spectrum of all stocks that our clients were trading." † — David Jeria (2022-06, same URL)

> "Because of the gameification aspect that's here to stay." † — David Jeria (2022-06, same URL)

**John Marshall** (Head of Derivatives Research). His data: retail went from 10–15% to 20–30% of share volume, and is about 50% of single-stock options. Single-stock options grew 4x from 2019 to 2021. In 2021 he declined to opine on regulating retail apps and defended clearing-house collateral rules and trading halts.
> "This blended makes about 40 percent of all risk in single stocks being traded by retail." † — John Marshall, Head of Derivatives Research (2022-06, same URL)

> "Clearinghouses help to ensure that brokers and clients have enough collateral to cover their trades in stock and options." † — John Marshall (2021-02-04, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-04-2021-the-rise-of-retail-investing-and-its-impact)

**Raj Mahajan** (Global Head of Systematic Trading). Explains internalization, PFOF and price improvement. After GameStop he says hedge-fund short-risk models must be rebuilt.
> "the risk models didn't contemplate a 10x move in the short against you or a 20x move in the short against you." † — Raj Mahajan, Global Head of Systematic Trading (2021-02-04, same URL)

**Chris Churchman** (Head of Marquee). Marquee is positioned as an *open ecosystem*: third-party data, client-authored widgets, mobile.
> "Visual Structuring aims to create a new paradigm in options trade idea generation; a new language of derivatives trading," — Chris Churchman, Head of GS Marquee (2022-09-27, https://www.goldmansachs.com/pressroom/press-releases/2022/goldman-sachs-announces-launch-of-visual-structuring)

> "Clients can leverage the best insights and data that Goldman Sachs and our partner vendors have to offer in an open ecosystem," — Chris Churchman (2023-11-14, https://www.goldmansachs.com/pressroom/press-releases/2023/goldman-sachs-launches-marquee-marketview)

**David Solomon** (CEO). In 2021 he frames GS as a technology supplier to institutions. On AI in 2024 his line is that GS doesn't have to be first. In Europe in 2025 he praises the region's equity market structure and attacks its regulation.
> "Goldman Sachs has always led by building technology to serve the most sophisticated financial institutions," — David Solomon, Chairman & CEO (2021-11-30, https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-aws-announcement-30-nov-2021)

> "This is not a place where you necessarily have to be first, which is generally true with all these big technologies," — David Solomon (2024-01-10, https://www.goldmansachs.com/insights/articles/geopolitical-competition-is-sending-shockwaves-through-the-global-economy)

> "an internationally regarded equity market structure that has seen it weather recent episodes of volatility effectively." — David Solomon, Les Echos op-ed (2025-06-25, https://www.goldmansachs.com/insights/articles/les-echos-europe-has-an-opportunity-to-seize)

**Eleanor Beasley** (Head of Equity Market Structure; COO, EMEA Equities). Defends fragmentation and internalization (GS as a systematic internalizer) and pushes for the consolidated tape and post-trade consolidation.
> "you're now only going to see 30% of reported trading volume, and you're therefore going to massively underestimate what is available," — Eleanor Beasley (2025-10-24, https://www.goldmansachs.com/insights/articles/how-well-are-uk-eu-stock-markets-working)

> "in 2024 alone we provided over €1 trillion of principal liquidity in European equities to our clients." — Eleanor Beasley (2025-10-24, same URL)

> "Europe has 17 central counterparties for clearing and 31 central securities depositaries for settlement across 31 different countries." — Eleanor Beasley (2025-10-24, same URL)

> "This transparency will show that our markets are far more liquid than people realize, encouraging greater global investment in the region," — Eleanor Beasley (2026-07-27, https://www.goldmansachs.com/insights/articles/europes-consolidated-stock-market-tape-could-invigorate-and-boost-investment)

**Bertie Whitehead** (Head of Corporate Broking). Says Europe-vs-US liquidity is comparable after adjusting for free float.
> "Global market capital is like air: It flows everywhere." — Bertie Whitehead (2026-07-27, same URL)

**Brendan McCarthy** (GSAM, Global Head of ETF Distribution). Argues that bond ETFs forced dealers to build portfolio-trading technology.
> "this has forced dealers to build the technology and connectivity required to buy and sell hundreds or thousands of bonds at once." — Brendan McCarthy (2026-03-10, https://www.goldmansachs.com/insights/articles/why-active-etfs-are-gaining-momentum-as-investors-seek-new-solutions)

**Tom Campbell / Jackson Isaacs** (GBM ETF distribution and trading).
> "in times of market stress, ETFs are accounting for 40% of the tape at times." — Tom Campbell, Head of Americas ETF Distribution (2026-08-18, https://www.goldmansachs.com/insights/articles/why-etfs-are-expected-to-draw-2-trillion-in-investments-in-2026)

**Credit trading** (unnamed Co-Head of US Credit Trading):
> "A modest adjustment to less than 1% of TRACE prints could improve execution quality in even the most illiquid bonds and through market cycles." — Co-Head of U.S. Credit Trading (undated, https://www.goldmansachs.com/what-we-do/ficc-and-equities/insights/articles/where-next-for-credit-portfolio-trading)

**Hari Moorthy** (Global Head of Transaction Banking):
> "transaction banking can be viewed as a stabilizing anchor for banks, with revenue volatility generally lower than capital markets products." — Hari Moorthy (2021-07-02, https://www.goldmansachs.com/insights/articles/from_briefings_02-july-2021)

**Other voices:**
- **Dan Dees** argues against negativity bias: since LTCM, US GDP is up about 3x and markets are up more than 500%. His top worry is the US fiscal position.
- **Jim Esposito** sees weak demand for long Treasuries (QT, regional banks, China). He notes private equity's share of M&A rose from about 20% to about 40% of volume.
- **John Waldron** (FT, 2025) describes "strategic interdependence" with China: China's share of US imports fell from 22% to 13.4%, and FDI into China is down more than 90%.

## 4. Mission / identity statements (as stated)

- The **Purpose and Values page (#7) is empty** in the scrape. No formal purpose statement is available from this bucket.
- **Marquee lineage as identity.** The story runs from SecDB (early 1990s) to GS Financial Workbench (1995) to Marquee (2014). GS describes giving clients "the same pricing data, risk models, and proprietary datasets used by Goldman Sachs traders and risk managers". Marquee is "one manifestation of how Goldman Sachs drives client impact through leading-edge technology."
- **TxB self-description:** "the strength, heritage, and expertise of a 150-year-old firm with the agility and entrepreneurial spirit of a tech start-up."
- **ETF Accelerator** (Mantil) cites "Goldman Sachs’ commitment to excellence, client service, innovation, and partnership". These are the core values in shorthand.
- **Solomon (2024):** "Our job is to have an understanding of those impacts in a way that’s going to be helpful to our clients." He also calls GS "US, first and foremost".
- **Partnership culture.** In 2020 Varadhan cites the firm's "spirit of partnership". In 2023 he invokes the flat, accessible culture of the 1998 partnership (Corzine walking the floor). Dees describes the banking "true north" as client relationships.
- **Solomon, March 2020:** "We have managed through volatile markets before – it’s core to what we do."

## 5. Tailwinds / headwinds / challenges

- **Tailwind: volatility and client activity drive markets revenue** (ADMITTED). Q1 2020 GM return was 19.7% against the 11% threshold. Varadhan warns that "one quarter is just a quarter".
- **Tailwind: the ETF boom** (ADMITTED). It feeds GS's ETF trading and authorized-participant role, ETF Accelerator, and model-portfolio rebalancing flow. US ETF AUM is $16.1tn, active ETFs are 13% of AUM but more than 35% of 2026 flows, and model portfolios hold $950bn (+46%).
- **Tailwind: electronification and fragmentation favour scaled internalizers** (INFERRED from Beasley's €1tn principal-liquidity figure and from GSET advertising "unique access to GS Principal Liquidity").
- **Headwind: retail internalization off-exchange made institutional execution costlier** (ADMITTED by Jeria). Trading costs "skyrocketed".
- **Headwind: operational and automation risk** (ADMITTED, Varadhan 2023): errors "proliferate" and are found only after the fact.
- **Headwind: talent attrition perception** (ADMITTED, 2020). Varadhan pushes back on press coverage of partner departures.
- **Headwind: US fiscal trajectory and weak Treasury demand** (ADMITTED, Dees and Esposito 2023).
- **Headwind: geopolitics and fragmentation** (ADMITTED, Solomon 2024, Waldron 2025).
- **Headwind: European regulatory burden and post-trade fragmentation** (ADMITTED). Solomon cites Draghi's estimate that internal barriers equal a 110% tariff on services. Beasley says post-trade costs are 50–100% higher than in the US.
- **Challenge: the consumer retreat, shown in the boilerplate** (ADMITTED in IR forward-looking statements). The sequence runs: sale of GreenSky and Marcus loans (Jun 2023), then "Personal Financial Management" (Sep 2023), then "strategic alternatives for credit card partnerships" (Dec 2023), then the GM card transition (2024–25), then "transition the Apple credit card program to another issuer" (Feb 2026 onward).
- **Challenge: Marquee monetization is opaque** (INFERRED). Every release describes products and entitlements. None gives users, revenue or a pricing model, apart from the PlotTool Pro subscription needed to create widgets.

## 6. Outside voices / skeptics

- **David Craver (Lone Pine, 2026).** Passive flows and levered multi-strats have hollowed out fundamental price discovery. Event volatility no longer tracks news, and he can no longer read a press release and predict the move. He sees this as an *opportunity* for duration-oriented investors. On AI he is bullish ("third or fourth inning"; "revenge of the dinosaurs").
> "I used to be able to read a press release and tell you what the stock was going to do the next day." † — David Craver, Co-CIO Lone Pine (2026-02-12, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/fundamentals-still-matter-lone-pines-david-craver)

> "The passive flows, by definition, are not taking a view on valuation." † — David Craver (2026-02-12, same URL)

> "it's not a bubble when everybody thinks it's a bubble." † — David Craver (2026-02-12, same URL)

- **Press-release partners** endorse rather than criticize. They include Adam Selipsky (AWS CEO), Justin Stephan (Wellington), Vlad Torgovnik (Millennium CIO), Jorge Mina (MSCI), Richard Benson (Millennium Global, praising Visual Structuring "on the sofa"), Dean Henry (AmEx) and Leila Thomas (Urban Synergy).
- **Gary Gensler** (SEC), paraphrased by Jeria: order-by-order competition for retail and auctions. This is the regulatory challenge to the PFOF and internalization model.
- **Mario Draghi**, cited by Solomon on EU internal barriers.
- **Genuine skeptics are absent.** None of the outside voices criticize GS itself. The closest are the "doubters" Siewert mentions in 2020 and the press coverage of partner departures.

## 7. Market-structure links

- **GS as a dealer that is also venue and infrastructure.** GSET sells algos, SOR, DMA and sponsored access. It runs its own ATS/MTF pools: **Sigma X2** (US ATS, with Form ATS-N filed), **Sigma X MTF** (Europe), and Sigma X Japan, HK and Australia. It offers "GS Principal Liquidity" with possible "price or size improvement". So GS is broker, venue operator and principal at once. **Atlas** is a multi-year rebuild of the equities trading stack.
- **Connectivity.** FIX into all major EMS/OMS, plus pre- and post-trade allocations via FIX. Distribution runs through third-party workflow rather than a proprietary terminal.
- **Marquee as a data, API and distribution business.** It started in 2014 with APIs, then grew into Marquee Trader (electronic FX and commodities execution, with volumes large enough to fund $1.1m in donations), GS Quant (Python), PlotTool Pro (time series), the Developer API, i-Select (client-built indices), Visual Structuring (2022) and MarketView (2023). The **AWS Financial Cloud for Data** (2021) and the **MSCI** tie-up (2021) push GS into data infrastructure, sold through AWS Marketplace and Data Exchange. MarketView redistributes **LSEG, FactSet, MSCI, Axioma and Wolfe** data, so GS acts as an aggregator and distributor of other vendors' content as well as its own. This competes with Bloomberg and LSEG Workspace for the buy-side desktop, though no release says so.
- **Credit portfolio trading.** GS calls PT "a critical tool" for executing large bond baskets and argues for a "modest" TRACE reform covering less than 1% of prints. That is presumably the dissemination and reporting treatment of PT prints, but the full report isn't in the corpus. McCarthy (2026) links this to bond ETFs, which "forced dealers to build" basket technology. **Venues (Tradeweb, MarketAxess, Trumid) are never named in this bucket.**
- **Retail flow and PFOF** (2021–22): retail orders go to market makers that internalize or route to exchanges. Off-exchange volume reached more than 50% on some days. "Non-participable" volume raises costs for institutions. Gensler's auction idea was the possible fix.
- **Clearing.** Marshall (2021) defends CCP collateral rules during GameStop. Beasley (2025) contrasts Europe's 17 CCPs and 31 CSDs with the US's one CCP (for equities) and one CSD, and calls for consolidation. The **2019 CCP letter is not in this bucket.**
- **Consolidated tape** (2025–26): GS strongly supports it, and the EU tape will be free for retail. GS uses it to argue that Europe's liquidity is underestimated, since lit primary venues carry less than 30% of volume and off-book trading is 40% of addressable liquidity. It would also lower market-data costs, which implicitly hits the exchanges' data revenue.
- **MiFID II** (2018) is credited with boosting venue competition and innovation. Beasley asks for like-for-like supervision of like-for-like businesses, which reads as a dig at exchanges or PTFs, and for regulatory "stability".
- **ETF plumbing.** GS is an ETF issuer (GSAM), authorized participant and market maker. The Accelerator offers launch-and-list as a service (Cboe, NYSE, NYSE Arca, XETRA listings). Model-portfolio rebalancing is a new flow source.
- **No digital-asset or tokenization content** appears in this bucket. The custody page mentions "digital-forward", but in the sense of a digital UX, not crypto.

## 8. Surprises / note-worthy theses

1. **GS argues *for* fragmentation and *for* transparency at the same time, and the two fit its business.** It provides €1tn a year of off-book principal liquidity as a systematic internalizer, and it wants a consolidated tape that makes that off-book liquidity *visible and counted*. The tape helps a fragmented market look deep without pushing flow back onto lit exchanges. Study note: incumbent dealers can embrace transparency regimes that legitimize their off-exchange role.
2. **Marquee is a platform strategy, not a single product.** Its path runs SecDB → Workbench → Marquee APIs → Trader → GS Quant/PlotTool → AWS cloud → MarketView, where third-party vendors' data is redistributed. GS is trying to own the buy-side *pre-trade* workflow. The Visual Structuring release says outright that technology has optimized execution while "the vast majority of a trader’s time is spent during the ideation process". The aim is to move upstream of the trade so the flow lands at GS. Revenue is never disclosed, so platform economics can't be assessed.
3. **IR boilerplate works as a strategy timeline.** The forward-looking disclaimers in the empty IR stubs chart the consumer exit precisely: Marcus loans and GreenSky in 2023, then card partnerships, then GM, then Apple in 2026. They also mark the arrival of "the opportunities presented by AI" (Sep 2025) and "OneGS 3.0" (May 2026). This makes a cheap, reliable dating tool for other buckets.
4. **The retail cycle in numbers, told by the dealer's own strats.** Retail went from about 10% to 20–25% of volume and then to an expected ~15% steady state. Off-exchange share went from 35% to above 50%. Retail made up about 50% of single-stock options and about 40% of single-stock risk, and 80% of retail notional sat in about 100 names each week. Jeria's "non-participable" concept is a strong study note: retail internalization creates a hidden cost for institutional VWAP and POV algos.
5. **The ETF as a market-structure force.** GS argues that bond ETFs drove the basket and portfolio-trading technology (McCarthy). ETFs now reach 40% of the tape in stress, and there are more US ETFs (6,000+) than single stocks. GS earns on every layer: issuer, AP, market maker, launch platform (Accelerator), and distribution to model portfolios.
6. **Varadhan's shift in what he fears.** In 2020 COVID markets were a "30-second reel" he had seen before. By 2023 his main fear was failure in automation, not market risk. That is an admission that electronification moves dealer risk from price risk to operational and tail technology risk.

Ambiguities and gaps:
- The retail podcast is dated 2020 in the file but recorded in 2022.
- The Bernstein 2019 stub date is inconsistent.
- The purpose, values, FICC and Prime pages are empty.
- The MSCI release body and all IR decks are absent.
- The credit-PT article doesn't name its author.
- The requested 2019 CCP letter is not present.
