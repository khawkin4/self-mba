# Goldman Sachs: read-first digest (2019-01-01 → 2026-10-25)

Stage: **read, not note.** This file describes the corpus, says what's in it, and recommends which notes are worth writing. Nothing has been written to `notes/` yet.
Files: `index.tsv` (262 rows: date, type, topic, title, url, words) · `articles.jsonl` (262 items with full text; `pdfs` lists the PDF each text came from) · this digest.

---

## 1. What the corpus is

**Source universe (unfiltered).** goldmansachs.com publishes one sitemap with **6,996 URLs**. Relevant sections:
- **Pressroom 2019–2026:** 458 items (430 press releases plus 28 announcements). Per year: 37 / 60 / 66 / 52 / 58 / 53 / 55 / 49.
- **Insights (all years):** Articles 632, *Exchanges* podcast pages 620, Talks at GS 613, GS Research pages 217, The Markets 261, Top of Mind 64, plus ~1,175 insight PDFs (podcast transcripts and reports).
- **Investor Relations:** 142 presentation/event pages for 2019–2026, annual reports 2019–2025, and Investor Day 2020 and 2023.

**How it was collected.** `curl` worked with no bot challenge. Each page's `__NEXT_DATA__` JSON yielded title, publishDate and rich-text body. PDFs came straight from the site.
- I downloaded all 458 pressroom items for 2019–2026, plus 1,316 Insights/Exchanges/Top of Mind pages and 142 IR pages.
- I screened them by title, then a keyword pass over the opening text, then hand curation.
- For the kept items I added the PDF text: 50 podcast transcripts or Top of Mind reports, 32 earnings releases (pages 1–4: highlights plus the CEO quote), 7 shareholder letters, and the Investor Day decks (2020 consolidated, eight from 2023).

**What's in it (262 items, ~512k words):**

| Type | n | Notes |
|---|---|---|
| Press release / announcement | 110 | 32 earnings releases (with PDF), M&A, leadership, platforms/digital, capital/SCB, 1MDB, consumer |
| IR event | 54 | Conference talks (Solomon, Waldron, Coleman) and quarterly IR videos. **Stubs only:** webcast audio, no transcript (see gaps) |
| *Exchanges* podcast | 44 | 38 with full transcript PDFs: Solomon ×6, Waldron ×2, Varadhan, Esposito/Dees, McDermott ×2, Argenti, Lee/Posnett, Churchman, Osman Ali, Ken Griffin, Marks/Arougheti, Zelter, Rowan, etc. |
| Insights article | 24 | Argenti pieces, market structure (EU tape, UK/EU equity liquidity, active ETFs, credit PT), CEO op-eds |
| Shareholder letter | 7 | Solomon, FY2019–FY2025 (dated to fiscal year-end; published ~Mar–Apr of the following year) |
| Investor Day deck | 9 | 2020 consolidated (~22k words); 2023: eight decks |
| Top of Mind (Research) | 5 | Crypto 2021, crypto winter 2022 (redacted scrape), gen-AI skeptic 2024, stablecoins 2025, private credit 2026 |
| Business page | 9 | GSET, connectivity, systematic strategies, custody, Marquee history. **Purpose & Values, FICC & Equities and Prime pages scraped empty** |

**Filter applied.** I **kept** items on:
- Global Banking & Markets: FICC/equities, electronic trading, financing/prime, market structure.
- Marquee and the data/platform products: Visual Structuring, MarketView, AWS/MSCI, ETF Accelerator.
- Digital assets: GS DAP, BNY tokenized MMFs, Datonomy, crypto desk.
- AI: hires, GS AI Assistant, OneGS 3.0, Marquee AI.
- Strategy: segments, Investor Days, the consumer build and exit, the AWM/alternatives pivot, Capital Solutions.
- All AWM M&A.
- Leadership and CEO/President/CFO voices.
- Capital and regulation: SCB, CCP paper, Basel.
- 1MDB, as a culture/controls signal.
- Outside skeptics hosted on GS channels.

I **skipped**:
- **Philanthropy:** 10,000 Small Businesses/Women, One Million Black Women, Launch With GS, Market Madness, the Fund for Racial Equity.
- **Sponsorships and NIL deals.**
- **Routine items:** preferred dividends, redemptions, conference-call notices, MD/partner-class lists, banker hires (M&A/IB partners), senior advisers (Sunak, Frydenberg), office openings (except Bellevue engineering), J.D. Power awards.
- **ESG and climate releases.**
- **COVID logistics.**
- **Index methodology notices.**
- **Most GS Research macro:** the ~150 AI-capex, power, equity-strategy and economics articles. I kept only the skeptic debates.
- **Whole sections:** Talks at GS and the investment-banking sector outlooks.

**Gaps and what was blocked or absent:**
- **Earnings-call transcripts aren't public.** The IR site offers them only through a transcript-request form, which I didn't submit. Conference talks are webcast audio only. Quarterly *results presentation* PDFs exist but weren't pulled. So the *analyst Q&A voice is missing*; quarterly management views come from the release quotes, the letters and the podcasts.
- **10-K/10-Q and proxy filings weren't used.** EDGAR would fill the segment, comp and governance detail.
- **Empty scrapes (client-rendered pages):** Purpose & Values, FICC & Equities, and Prime Services. Mission language therefore comes from the letters, releases and podcasts.
- **The Dec-2022 Top of Mind ("Winter of Crypto's Discontents") and its podcast are redacted scrapes** with cover quotes only. The Lemkau (2020) and Solomon COVID (2020-04) episodes have no transcript. The "Stablecoin summer" page captured the podcast transcript, not the report.
- **robots.txt.** `/materials/` is disallowed for all agents and I didn't fetch it. `/insights` is disallowed only for GPTBot/ChatGPT-User. I signed in nowhere, submitted no forms and accepted no terms.
- **Date quirks** (all in `index.tsv` as scraped):
  - The retail podcast filed as 2020-06-14 was recorded **June 2022** (URL slug 06-14-22).
  - Bernstein "2019-11-05" describes the 31 May 2019 talk.
  - Two 2020 earnings releases had wrong CMS dates; I fixed them from the URL.
  - The NEOS release is dated 2026-09-03 but its dateline is 12 Aug 2026.
  - The Solomon Jan-2024 episode page says "2023".
- **The GS site never names Trumid, MarketAxess, ICE or Canton,** and names Tradeweb only twice. Venue relationships have to come from the Tradeweb study and from filings (§7).

---

## 2. Chronology: the 36 events that matter for the lens

| Date | Event | Source |
|---|---|---|
| 2018-10-01 | Solomon becomes CEO. The same-day "One Goldman Sachs" memo with Waldron and Scherr starts a cross-divisional client pilot | Exchanges 2019-10-01 |
| 2019-05-16 | **United Capital** acquired (~$750M): an RIA channel and the first acquisition under Solomon | PR |
| 2019-08 | **Apple Card** launches. GS "had no legacy business", so it built a greenfield stack | Exchanges 2019-10-01 |
| 2019-09-12 | **Marco Argenti** (from AWS) joins as co-CIO, with Atte Lahtiranta as CTO | PR |
| 2019-10-24 | GS co-authors the buy-side/sell-side paper on **CCP resilience** (skin in the game, assessment caps) with BlackRock, JPM and Vanguard | PR (+2020-03-10 follow-up) |
| 2020-01-07 | New segments: IB, Global Markets, Asset Management, **Consumer & Wealth Management** | PR |
| 2020-01-29 | **First-ever Investor Day.** Targets: ROE >13%, efficiency ~60%, $1.3bn of expense saves. Four growth bets: Transaction Banking, consumer, alts, wealth. GM deck: electronic share ~99.9% of US cash-equity tickets, ~75% of US credit | ID20 deck |
| 2020-03 | COVID. Buybacks suspended and the discount window drawn. Q2 2020 brings the best FICC quarter in 9 years | PRs |
| 2020-06 | **Transaction Banking** launches in the US (~$25bn deposits by Q2) | Q2-20 release |
| 2020-06-29 | First **stress capital buffer, 6.7%**, later revised to 6.6% after a Fed calculation error | PR |
| 2020-09-18 | **Folio Financial** acquired: RIA custody and a "durable revenue" platform | PR |
| 2020-10-22 | **1MDB** settled: $3.42bn of 2020 provisions and ~$174m of clawbacks. The Board calls it "an institutional failure" | PR |
| 2021-03 | **Crypto desk** goes live (CME futures, NDFs), led by Mathew McDermott | Exchanges 2021-03-05 |
| 2021-06 | Co-leads the **EIB €100mn digital bond** on public Ethereum, settled T+1 | Insights 2021-06-10 |
| 2021-08-19 | **NN Investment Partners** (~€1.6–1.7bn), adding ~$305bn of AUS. Closed 2022-04-11 | PR |
| 2021-09-14 | **Denis Coleman** is named CFO from 2022. Stephen Scherr, who built Consumer and TxB, retires | PR |
| 2021-09-15 | **GreenSky** deal: Marcus is to "become the consumer banking platform of the future". Closed 2022-03-29 | PR |
| 2021-11-30 | **GS Financial Cloud for Data with AWS** launched at re:Invent | PR |
| 2022 (FY) | 2021 ROE was 23.0%. Targets raised to ROE 14–16% and $225bn of alts fundraising for 2020–24 | L21 |
| 2022-09-27 | **Marquee Visual Structuring** launched (FX options; expanded to equities, crypto and metals 2023-04-17) | PR |
| 2022-10-18 | **Realignment** into Global Banking & Markets, Asset & Wealth Management and Platform Solutions. 2022 letter: "significantly narrow our ambitions for our consumer strategy" | Q3-22 release, L22 |
| 2022-11-03 | **Datonomy** (with MSCI and Coin Metrics), a digital-asset taxonomy distributed via Marquee | PR |
| 2023-02-28 | **Investor Day 2023.** Platform Solutions targets breakeven by 2025, AWM a mid-20s margin, GBM "raising the floor" (financing $2.0bn in 2013 → $7.1bn in 2022) | ID23 decks |
| 2023-Q1→Q4 | Consumer unwind: Marcus loan-book sale (~$470m loss), GreenSky goodwill impairment ($504m) then sale to Sixth Street (2023-10-11), PFM sold to Creative Planning (2023-08-28) | Releases |
| 2023-11-14 | **Marquee MarketView** redistributes LSEG, FactSet, MSCI, Axioma and Wolfe data | PR |
| 2024-06-25 | Top of Mind #129, "Gen AI: too much spend, too little benefit?": in-house skeptic **Jim Covello** alongside **Daron Acemoglu** | ToM |
| 2024-06-28 | Solomon **publicly disputes** a 6.4% SCB. The Fed reconsiders to 6.2% on 2024-08-28 | PRs |
| 2024-11-18 | **GS DAP spin-out** planned into an "industry-owned" entity. **Tradeweb is the first strategic partner**; the platform is built on Digital Asset tech | PR |
| 2025-01-13 | **Capital Solutions Group** formed in GBM to sit at the "fulcrum" of private credit (~$145bn of GS private credit) | PR |
| 2025-01-21 | Leadership reshuffle: triumvirate co-heads of IB, FICC and Equities; Gutman and Shah become GSI co-CEOs; Pasquariello and Storey co-head One GS | PR |
| 2025-01 (late) | **GS AI Assistant** rolled out firmwide. Solomon: engineering productivity on ~12,000 engineers is the "most obvious" use | Exchanges 2025-01-29 |
| 2025-07-23 | **BNY × GS tokenized MMFs**: mirror tokens on GS DAP, with BlackRock, Fidelity, Federated Hermes, Dreyfus and GSAM | PR |
| 2025-09-04 / 10-13 / 12-01 | **AWM deal spree:** T. Rowe Price tie-up (up to $1bn, ~3.5% stake), **Industry Ventures** (VC secondaries; closed 2026-01-05), **Innovator** (buffer ETFs; closed 2026-04-02) | PRs |
| 2025 (FY) | ROE **15.0%**, the 2020 target finally met. **OneGS 3.0** ("operating model propelled by AI") launched. FICC+Equities financing $11.4bn, **37% of markets revenue**. SCB down to 3.4% | L25, Q4-25 release |
| 2026-01-07 | **Apple Card goes to JPMorgan Chase** (>$20bn book, +$0.46 EPS): "substantially completes the narrowing of our focus in our consumer business" | PR |
| 2026-03→05 | Private-credit stress. BDC redemptions and AI-exposed software loans dominate; GS voices insist the stress is not systemic | Exchanges / ToM |
| 2026-Q3 | Record run: Q2 revenue $20.34bn and ROE 23.5%. In Q3 **Equities financing ($3.37bn) exceeds Equities intermediation ($3.08bn)**. More AWM deals: LCN (Aug), NEOS (Sep) | Releases |

---

## 3. People: who leads, who speaks, what they believe

**David Solomon (Chairman & CEO since Oct 2018).** He carries the firm's narrative almost alone: every earnings quote, every letter, and six podcasts. His arc runs in three phases:
- **Builder (2019–21):** diversify, open new businesses, a "digital consumer bank".
- **Refocus (2022–23):** "two core businesses", "no ambiguity".
- **Scale and efficiency (2024–26):** One GS, durable revenues, private credit, OneGS 3.0, AI.

The constants are One GS, client-centricity, plan-plus-KPIs (unusual for an ex-partnership), and impatience with regulators (SCB, Basel III).

> "We are building the digital consumer bank of the future." — David Solomon, CEO (2019-12-31, 2019 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2019-annual-report/letter-to-shareholders-2019.pdf)

> "And capital is a commodity." — David Solomon, CEO (2019-10-01, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/09-23-2019-david-solomon-first-year)

> "one of the things that, as an organization, we still excel at, is bespoke risk intermediation." — David Solomon, CEO (2019-10-01, same URL)

> "They did not want to jump inside the financial moat, the financial regulatory moat." — David Solomon, on Apple (2019-10-01, same URL)

> "there were calls to downsize our Global Markets business, but we believe its performance in 2020 shows it was wise to stay the course" — David Solomon (2020-12-31, 2020 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2020-annual-report/multimedia/2020/letter-to-shareholders.pdf)

> "We have been clear in our aspiration for Marcus to become the consumer banking platform of the future" — David Solomon, on GreenSky (2021-09-15, https://www.goldmansachs.com/pressroom/press-releases/2021/goldman-sachs-to-acquire-greensky)

> "In 2022, we decided to significantly narrow our ambitions for our consumer strategy." — David Solomon (2022-12-31, 2022 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2022-annual-report/multimedia/letter-to-shareholders.pdf)

> "We haven't executed perfectly on all of them. And there are places where we certainly could have executed better." — David Solomon (2023-02-24, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/02-24-2023-david-solomon)

> "There’s no ambiguity about who we are — a preeminent global investment bank, serving the most important companies, institutions and individuals in the world" — David Solomon (2023-12-31, 2023 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2023-annual-report/multimedia/letter-to-shareholders.pdf)

> "Our consumer ambitions we narrowed materially, and then we went and we executed on those decisions very effectively." — David Solomon (2024-01-23, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/01-23-24-solomon)

> "This increase does not seem to reflect the strategic evolution of our business and the continuous progress we’ve made to reduce our stress loss intensity" — David Solomon, on the SCB (2024-06-28, https://www.goldmansachs.com/pressroom/press-releases/2024/goldman-sachs-statement-on-stress-capital-buffer)

> "we are operating at the fulcrum of one of the most important structural trends in finance today: the emergence and growth of private credit" — David Solomon (2024-12-31, 2024 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2024-annual-report/multimedia/letter-to-shareholders.pdf)

> "In 2025, we announced the launch of One Goldman Sachs 3.0, our new operating model propelled by AI." — David Solomon (2025-12-31, 2025 letter, https://www.goldmansachs.com/investor-relations/financials/current/annual-reports/2025/letter-to-shareholders.pdf)

> "the reality of it is that it's narrower than that grand vision of reimagining the firm." — David Solomon, on OneGS 3.0 (2026-01-23, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/goldman-sachs-chairman-and-ceo-david-solomon-on-ai-m-and-a-and-markets)

> "I'm not in the job apocalypse camp." — David Solomon (2026-01-23, same URL)

> "This transaction substantially completes the narrowing of our focus in our consumer business" — David Solomon, on Apple Card (2026-01-07, https://www.goldmansachs.com/pressroom/press-releases/2026/goldman-sachs-announces-agreement-to-transition-apple-card-program-to-chase)

> "are a reminder that the credit cycle has not been repealed." — David Solomon, on private-credit/software stress (2025-12-31, 2025 letter, URL above)

**How Solomon's views shifted:**
- **Consumer:** "open field" (2019) → GreenSky's network bought to save 7–10 years (2021) → provisions named as a drag (2023) → "narrowed materially", presented as nimbleness rather than error (2024) → Apple footnote (2025 letter).
- **AI:** "early stage of testing" (2023) → "Euphoria cools" and a "narrow set of use cases" (2024) → engineering productivity (2025) → OneGS 3.0, with expectations deliberately reset (2026).
- **Regulation:** adversary (Basel III, SCB 2023–24) → "more balanced regulatory regime" (2025).

**John Waldron (President & COO; joined the Board Feb 2025).** He is the operator and the clear heir. He diagnosed One GS as a repair job, and he is now the person who quantifies "durability".

> "we have gotten more Balkanized. We do operate in more individual units." — John Waldron (2019-09-13, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/09-09-2019-john-waldron)

> "the organizational structure of the firm was getting in the way of the ethos of the firm" — John Waldron (2019-09-13, same URL)

> "In the last five years, the standard deviation of our results is 6%. In the prior 10 years, it was 24%." — John Waldron, on Global Markets (2025-06-05, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/how-goldman-sachs-john-waldron-is-navigating-a-more-uncertain-time)

> "We kind of obsess over those rankings. We're not obsessing over revenue." — John Waldron, on client wallet share (2025-06-05, same URL)

> "I think the definitional success of our firm over time will be how well do we deploy technology to make us better." — John Waldron (2025-06-05, same URL)

**Denis Coleman (CFO from 2022).** A leveraged-finance banker who replaced the consumer architect Scherr. He is the technocrat of the ROE bridge (~150bp from fees, ~150bp from alts balance-sheet reduction, the Platform Solutions loss reversed) and of SCB "transparency".

**GBM leaders:**
- **Ashok Varadhan** (co-head GM/GBM) moves from market risk to automation risk:
  > "so much of our workflow has migrated through technological automation" — Ashok Varadhan, GBM co-head (2023-11-21, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/11-21-23-esposito-dees-varadhan)
- **Dan Dees** (GBM co-head; "raising the floor").
- **Jim Esposito.**
- **2025 co-heads:** FICC Brauth/Shah/Sehgal, Equities Potishko/Goddeeris/Hoxha.

**Platform and tech voices:**
- **Chris Churchman** (Head of Marquee).
- **Marco Argenti** (CIO).
- **George Lee** (ex-CIO; co-head GS Global Institute; AI Exchanges host).
- **Mathew McDermott** (Global Head of Digital Assets).
- **Eleanor Beasley** (Head of Equity Market Structure, EMEA).
- **David Jeria** (Electronic Trading Strats).

> "We view permissioned distributed technologies as the next structural change to financial markets" — Mathew McDermott (2024-11-18, https://www.goldmansachs.com/pressroom/press-releases/2024/announcement-18-nov-2024)

> "Client demand, pure and simple." — Mathew McDermott, on the 2021 crypto desk (2021-05-24, https://www.goldmansachs.com/insights/top-of-mind/crypto-a-new-asset-class)

> "The failure mode here is not technological, it’s organizational." — Marco Argenti, CIO (2025-07-09, https://www.goldmansachs.com/insights/articles/fortune-we-must-prepare-ai-natives-to-shape-the-future-of-work)

> "We launched our GS AI Assistant which allows more people across the firm to get access to leading-edge models" — George Lee (2025-02-04, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/ai-exchanges-will-falling-costs-drive-new-opportunities)

> "But like a demo is judged on its best day, whereas a product is judged on its worst day, right?" — Chris Churchman, Head of Marquee (2026-08-24, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/building-ai-systems-for-capital-markets)

> "in 2024 alone we provided over €1 trillion of principal liquidity in European equities to our clients." — Eleanor Beasley (2025-10-24, https://www.goldmansachs.com/insights/articles/how-well-are-uk-eu-stock-markets-working)

> "Because these trades happen on a bilateral basis, they are non-participable from other market participants." — David Jeria, on retail internalization (2022-06-14, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/06-14-22-marshall-tuorto-jeria)

**AWM and alternatives voices:**
- **Marc Nachmann** (Global Head of AWM).
- **Julian Salisbury** (CIO).
- **Vivek Bantwal and James Reynolds** (private credit).
- **Michael Brandmeyer** (XIG CIO).
- **Pete Lyon** (Capital Solutions Group).
- **Darren Cohen** (Growth Equity).
- **Hans Swildens** (Industry Ventures, now a GS partner).

> "But the reality is that it's not semiliquid, it's illiquid." — Vivek Bantwal, GSAM private credit (2026-03-23, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/private-credit-concerns-in-context)

> "private equity has actually gone negative in terms of alpha to the public markets for the first time over the last two years." — Michael Brandmeyer, GSAM XIG CIO (2026-06-08, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/private-markets-at-an-inflection-point)

> "I think we're in the middle of a market structure change." — Pete Lyon, Capital Solutions Group (2026-06-08, same URL)

> "there's one asset class in the world that hasn't gone through a digital transformation, and that's alternatives." — Darren Cohen, GSAM Growth Equity (2025-09-09, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/the-growth-playbook-goldman-sachs-darren-cohen-on-building-a-growth-investing-platform)

---

## 4. Mission and identity, as stated, and how it changed

| Period | Stated purpose / identity | Source |
|---|---|---|
| 2019–20 | Purpose: *"advance sustainable economic growth and financial opportunity."* Values cut to four: partnership, client service, integrity, excellence. Boilerplate: "a leading global investment banking, securities and investment management firm" | L19, L20, ID20 |
| 2021–22 | Boilerplate adds **"and consumer banking"**. The 2021 letter replaces the purpose box with "Our Strategy to Produce Higher, More Consistent Returns" | releases, L21 |
| 2022–23 | Purpose rewritten: *"world’s most exceptional financial institution."* The societal language disappears. "Preeminent global investment bank", "two core businesses" | L22, L23 |
| Late 2023 → | "Consumer banking" **dropped** from the boilerplate (from the GreenSky-sale release on). Becomes "a leading global financial institution" | releases |
| 2024–26 | One GS, "world-class, interconnected franchises", "durable". The 2025 letter anchors values in **John Whitehead's 14 Business Principles (1979)** | L24, L25 |

> "Goldman Sachs’ mission is to advance sustainable economic growth and financial opportunity across the globe." — David Solomon (2019-12-31, 2019 letter, URL above)

> "We are resolute in fulfilling our purpose of putting capital and ideas to work to evolve organizations, accelerate global economies and amplify personal prosperity." — David Solomon (2020-01-29, https://www.goldmansachs.com/pressroom/press-releases/2020/announcement-01-29-2020)

**Reading.** The identity statements track the strategy:
- The societal purpose arrived with diversification.
- "Consumer banking" entered the legal self-description during the build and left during the exit.
- Heritage and excellence replaced purpose once the firm returned to being an investment bank plus asset manager.

Sustainability and D&I content fades from the letters after 2022. *(Inference: nothing is formally retracted.)*

---

## 5. Tailwinds, headwinds, challenges

A = admitted by GS in the corpus · I = my inference from the corpus.

**Tailwinds:**
1. **Volatility plus financing (A).** The FICC/Equities path:
   - Equities $7.4bn (2019) → record $13.4bn (2024) → $16.5bn (2025) → $19.2bn in 9M-2026.
   - Financing grew from 19% of markets revenue (vs 32% for peers, ID20) to **37%** in 2025.
   - In Q3-2026 Equities financing exceeds intermediation.
   - Waldron: the standard deviation of results fell from 24% to 6%.
2. **AWM fee build (A).**
   - Management fees: $6.1bn (2019) → $10.4bn (2024) → $11.5bn (2025).
   - Alts raised: $438bn since ID20.
   - New goals: $75–100bn a year, and $750bn of fee-paying alts AUS by 2030.
3. **Capital relief (A).** SCB 6.7% → 3.4% (2025). The dividend rose from $0.85 to $5.00.
4. **M&A/IPO rebound and AI as a fee engine (A).** "Technology and AI-led innovation should be a catalyst" (2026). AI debt was ~18% of IG supply in 2026 (Research).
5. **Private credit's structural growth (A).** Capital Solutions Group plus AWM private credit.
6. **ETF boom (A).** GS acts as issuer, AP, market maker and launch platform (ETF Accelerator, Innovator, NEOS).
7. **US regulatory pivot on digital assets (A, McDermott 2025).** SAB 121 rescinded, the GENIUS Act.

**Headwinds and challenges:**
1. **The failed consumer diversification (A, minimally).**
   - Losses ran in sequence: Marcus loans, a $504m GreenSky impairment, PFM, the GM card, then Apple Card.
   - The 2020 >13% ROE target was missed in 2022–23 (10.2%, ~7.5%) and met only in 2025, through financing and fees, not through TxB or consumer.
   - **Admitted in one sentence across seven letters** (2022).
2. **Capital-markets-heavy mix and cyclicality (A).** "We have a mix of businesses that is very capital markets heavy" (Solomon 2023).
3. **Balance-sheet investing drag (A).** A ~$10bn revenue swing in 2022 was the "biggest drag", bigger than consumer. Principal investments ran down from $64bn to ~$6bn.
4. **Regulation (A).** SCB fights (2020 error, 2024 dispute) and Basel III endgame lobbying.
5. **1MDB (A).** $3.42bn, clawbacks, and a compliance function that "nearly doubled".
6. **Private-credit stress, 2026 (A, framed by GS as technical rather than fundamental).** BDC outflows, AI risk to software borrowers (~25% of direct lending), and GS on both the origination and asset-management sides. (I: a conflict-of-interest question in allocation.)
7. **AI execution (A).** "Changing processes in a big enterprise is hard work". Covello's "six times the cost". Churchman warns of junior-pipeline "cognitive atrophy". (I: AI gains may be competed away across banks.)
8. **Operational/automation risk (A, Varadhan).**
9. **Talent competition with Big Tech (I).** Senior hires from AWS, Google and Amazon AGI, and an office in Bellevue.
10. **Marquee monetization is undisclosed (I).** No users, revenue or pricing appear anywhere.
11. **Moving goalposts (I).**
    - The alts target switched from $100bn *net* to $150bn *gross* (2019 → 2020).
    - The top-client metric moved from top-100 to top-150 with a restated base.
    - Returns became "through the cycle" once 2022–23 fell short.

---

## 6. Outside voices and skeptics in the corpus

GS curates every voice here: these are its own podcasts and research, with internal hosts. The sharpest skeptics are **GS's own researchers** or academics it invited.

| Voice | Topic | Line |
|---|---|---|
| **Jim Covello** (GS Head of Global Equity Research) | Gen-AI ROI | "So, the crucial question is: What $1tn problem will AI solve?" (2024-06-25) |
| **Daron Acemoglu** (MIT) | AI productivity | ~0.5% productivity and ~1% GDP gain over a decade, vs GS's own 9%/6.1% |
| **Nouriel Roubini** (NYU) | Crypto/permissioned DLT | "The idea that technology can resolve the question of trust is delusional." (2021-05-24); enterprise chains are "Blockchain In Name Only", which pre-critiques GS DAP |
| **Barry Eichengreen** (Berkeley) | Stablecoins | singleness of money; "There is nothing like a deposit insurance fund for stablecoins." (2025-09-02) |
| **Gary Gorton** (Yale) | Contagion | crypto didn't spread *because* it isn't wired into TradFi yet, which implies tokenization bridges carry future contagion |
| **Howard Marks** (Oaktree) | Private credit | "So everybody hangs up a shingle as a direct lender. That's a gold rush." (2026-05-11) |
| **Michael Arougheti** (Ares), **Jim Zelter** (Apollo), **Marc Rowan** (Apollo) | Private credit | defenders: "not really a gate", "headlines are a lot louder than the spreads"; investors as "the new banks" |
| **Ken Griffin** (Citadel) | AI, market making | agents cut a 6–8 week task to hours, yet CEOs' AI success stories "Not one involved AI" |
| **David Craver** (Lone Pine) | Passive/multi-strat market structure | "The passive flows, by definition, are not taking a view on valuation." (2026-02-12) |
| CCP paper co-signers (BlackRock, JPM, Vanguard, Guardian Life) | Clearing | users skeptical of CCPs' own skin in the game |
| Alan Waxman (Sixth Street) | GreenSky | the implicit counter-view: a specialty-finance owner fits better than a G-SIB |

> "So, the crucial question is: What $1tn problem will AI solve?" — Jim Covello, GS Head of Global Equity Research (2024-06-25, https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too-much-spend-too-little-benefit)

> "The idea that technology can resolve the question of trust is delusional." — Nouriel Roubini, NYU Stern (2021-05-24, https://www.goldmansachs.com/insights/top-of-mind/crypto-a-new-asset-class)

> "There is nothing like a deposit insurance fund for stablecoins." — Barry Eichengreen, UC Berkeley (2025-09-02, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/after-a-summer-of-stablecoins-whats-next)

> "So everybody hangs up a shingle as a direct lender. That's a gold rush." — Howard Marks, Oaktree (2026-05-11, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/cracks-in-private-credit)

> "these models, again, in the hands of the average person will create herd behavior" — Osman Ali, GS QIS co-head, on AI making markets less efficient (2026-05-06, https://www.goldmansachs.com/insights/goldman-sachs-exchanges/will-ai-make-markets-less-efficient)

**Absent:** any regulator speaking in its own voice, any unhappy client, any Marcus customer, any competing dealer, and any venue operator criticizing GS.

---

## 7. Links to the Tradeweb study

| Link | What GS's corpus says | What the Tradeweb study adds |
|---|---|---|
| **GS DAP × Tradeweb** | Nov 2024: Tradeweb is the *first strategic partner* in spinning DAP into an "industry-owned" ledger, bringing "trading and liquidity capabilities across the fixed income spectrum". DAP runs on **Digital Asset** tech (Canton is never named) | Tradeweb co-led Digital Asset's $135M round with DRW, alongside **Goldman**, Citadel Securities, DTCC and Virtu (2025-07). Tradeweb ran the first on-chain UST financing on **Canton** (2025-08). GS and Tradeweb are co-investors and co-builders on the same tokenization rail (`notes/tradeweb-outside-voices.md`, `tradeweb-mission-forces.md` T10) |
| **Tradeweb IPO gains** | ID20 GM deck strips 2019 "Tradeweb gains" out of peer revenues (JPM ~$335mm, Citi $355mm…) | Dealers' stake went from 46% to 17.3% at IPO. GS was one of the founding dealer-owners; the GS corpus doesn't say what it held or sold *(gap: check 10-K)* |
| **GS as dealer on venues** | No venue is named. GS stresses electronic share (75% of US credit tickets in 2019), portfolio trading (>$120bn executed by 2020) and a proposed **TRACE reform for PT prints** | Tradeweb's study lists GS's Anshul Sehgal (now FICC co-head) and McDermott as launch-dealer voices. First electronic SOFR swaption: **Goldman ↔ CDPQ** on Tradeweb SEF (2022-06-02). GS is a dedicated market maker on MarketAxess Live Markets (Bloomberg 2021, via the TW study) |
| **GS as venue/competitor** | GS runs its own ATS/MTFs (Sigma X2, Sigma X MTF), sells "GS Principal Liquidity", and built **Marquee** as a pre-trade data/API storefront that redistributes LSEG/FactSet/MSCI data | Tradeweb's thesis is that the venue owns data and reference prices. Marquee is the dealer's attempt to own the *pre-trade* workflow instead. Both compete for the buy-side desktop with Bloomberg and LSEG Workspace *(I)* |
| **EU consolidated tape** | GS strongly supports it; it shows off-book liquidity (where GS internalizes) as real liquidity | The Tradeweb/MarketAxess/Bloomberg tape JV ended 2023-12. The same issue, seen from the venue side |
| **Financing over flow** | Financing reached 37% of markets revenue, and Equities financing exceeds intermediation in Q3-26 | Explains why dealers can live with spread compression from electronification: the moat moved to balance sheet (prime, repo). This is the strategic counterpart to Tradeweb's automation-is-the-product thesis |
| **Trumid / ICE–MarketAxess** | **Never mentioned** in GS's own channels | Tradeweb buying Trumid (2026-10-19) and ICE buying MarketAxess (2026-07-30) consolidate the venues GS quotes on. GS's sell-side position, and any Trumid shareholding, have to come from filings and press *(gap)* |

---

## 8. Recommendation: what's worth noting

Ranked by value for the user's time and how well they connect to existing notes.

1. **"Durable revenues: how Goldman turned a trading house into a financing-and-fees franchise (2019–2026)"**
   - **Thesis:** the 2020 plan said durability would come from new businesses. It actually came from the old dealer's balance sheet (prime, repo, structured lending: 37% of markets revenue) plus AWM fees, while consumer was written off. ROE met target five years late, through a different mix.
   - **Why:** the cleanest numbers series in the corpus (targets vs actuals table, financing path, SCB path, Waldron's 24%→6%). It also pairs directly with Tradeweb's electronification story.
   - **Serves:** 02 Corporate Finance & Valuation, E2 Capital Allocation, E8 Investor Relations.
2. **"The consumer round trip: Marcus, Apple Card, GreenSky (2016–2026) as a case in strategic reversal"**
   - **Thesis:** an investment bank tried to build a mass-market bank on a greenfield stack ("no legacy business"). Rising credit costs, capital intensity and the absence of distribution economics forced a five-step exit, narrated through one letter sentence and a boilerplate edit.
   - **Why:** a dated and quantified reversal case, with leadership changes (Scherr out, Coleman in) and narrative management. Rare material.
   - **Serves:** 04 Competitive Strategy, E5 Transformation & Change, E3 M&A (buy GreenSky, sell GreenSky), E8.
3. **"The dealer as platform: Marquee, Sigma X, ETF Accelerator and the consolidated tape"**
   - **Thesis:** GS answers electronification by being broker, venue operator, principal liquidity provider and pre-trade data distributor at once. It backs transparency (tape) that legitimizes its off-exchange role.
   - **Why:** this is the market-structure counterpart to the Tradeweb hub, and it tests Tradeweb's venue-owns-the-data thesis from the dealer side. Caveat: Marquee economics are undisclosed.
   - **Serves:** 04, 10 Entrepreneurship & Venture (platform), E10 Digital & AI; Canon: Network Effects & Platform Strategy, Coopetition.
4. **"Giving away the rail: GS DAP, Tradeweb, BNY and why tokenization gets mutualized"**
   - **Thesis:** GS built a permissioned ledger, then chose to spin it out as "industry-owned" with Tradeweb. Rails only get adoption when no single dealer owns them. The skeptics (Roubini's "BINO", Gorton on contagion) frame the risk.
   - **Why:** it ties directly to Tradeweb's Canton/Digital Asset work. The arc from crypto desk (2021) to collateral plumbing (2025) is clean.
   - **Serves:** 04, E10, 10; Canon: Network Effects, Game Theory (Brandenburger & Nalebuff).
5. **"Private credit: the bank on both sides of the boom and the 2026 stress"**
   - **Thesis:** GBM originates through Capital Solutions and AWM invests through $145bn+ of private credit. The 2026 BDC redemptions and AI-software exposure test whether the house line (not systemic; redemption limits are "a feature, not a bug") holds.
   - **Why:** live and important; it has strong outside voices (Marks, Arougheti, Zelter) and an internal admission (PE alpha turned negative).
   - **Serves:** E2, E3, E6 Crisis & Resilience, 11 Macro; Canon: Risk & Fragility.
6. **"One Goldman Sachs: from a 'Balkanized' diagnosis to a wallet-share metric"**
   - **Thesis:** a culture and org redesign that started as an admitted failure (2019), was hard-wired by the 2022 GBM merger, and became a measurable KPI (client rankings, wallet share +390bp), plus OneGS 3.0 extending it to operations.
   - **Why:** a leadership and org-design case with direct quotes from both principals. The 1MDB clawbacks and controls fit as a sidebar.
   - **Serves:** 09 Leadership & OB, E1 Leading at Scale, E12 Culture as Strategy, E4 Governance (1MDB sidebar).
7. **"AI inside a bank: OneGS 3.0, the GS AI Assistant, and the house skeptic"** *(optional; overlaps with existing AI notes)*
   - **Thesis:** GS deployed AI first to developers and KYC/onboarding, promises flat headcount rather than cuts, and stages its own bull-vs-bear debate (Lee vs Covello) while earning fees from the capex boom.
   - **Serves:** E10, 07 Data & Decisions.

**Not worth noting, and why:**
- **GS Research macro and AI-capex pieces (~150 screened).** Forecasts with short shelf lives. They are already covered by better canon, or by the WSS notes for rates and credit.
- **IR event stubs (54).** Boilerplate only. One curiosity: the forward-looking disclaimers date the consumer exit and the first mention of "AI"/"OneGS 3.0". That fits as a footnote in note 2, not a note of its own.
- **Leadership-appointment releases.** Useful as a chronology inside note 6, not on their own.
- **1MDB as a standalone note.** Strong governance material, but it's mostly a legal settlement. Write it only if the user is doing E4/E6 and wants a culture-and-controls case.
- **Crypto price and trading content (2021–22).** Dated. Keep only the McDermott tone shift and the skeptic quotes, for note 4.
- **Stress-test statements beyond the SCB path table.** Repetitive.
- **ETF Accelerator individual launches.** One line in note 3 covers them.

**Before writing any of these, fill:**
1. The earnings-call Q&A, from transcripts via another source; it's needed for notes 1–2.
2. The 10-K, for segment financials, the Tradeweb/venue stakes and Marquee disclosure.
3. Press coverage of the Trumid and ICE–MarketAxess deals from the dealer side.

*Quote check:* every `>` quote above was verified verbatim against `articles.jsonl` by script (whitespace and curly-quote normalized; PDF line breaks treated as spaces).
