# Note · Aladdin and the data push — BlackRock's software arm grew from an internal risk system into the operating layer of other firms, and it is now reaching for the private-markets index

> Technology / data-strategy note · Maps to **E10** (Digital & AI Transformation), **Course 10** (Entrepreneurship & Venture: platforms), **Course 07** (Data, Analytics & Decision-Making), **Course 04** (Competitive Strategy: switching costs, cornered resources) · Written 2026-10-25 · Companion to [[blackrock-hub]], [[blackrock-anchor-client]], [[blackrock-private-markets]]

- **Source:**
  - Aladdin-related releases in `_ingest/raw/blackrock/articles.jsonl`: eFront (2019), Azure (2020), Clarity AI (2021), Snowflake (2021), Baringa (2021), Avaloq (2023), Preqin (2024–25).
  - The 2023 and 2025 Investor Day decks (Aladdin sections presented by Sudhir Nair, later with Tarek Chouman).
  - Annual earnings narratives and the Fink letters.
  - Technology revenue figures come from earnings releases. Where marked *parsed*, the figure was reconstructed from flattened tables.
- **Core claim:** Aladdin went through five stages:
  1. **an internal risk system** that BlackRock still runs on ("both a user and a provider");
  2. **a cloud SaaS product** (Azure 2020, Snowflake 2021);
  3. **a whole-portfolio workflow**, from eFront in 2019 to Preqin in 2025;
  4. **a connectivity layer** that venues plug into ([[blackrock-anchor-client]]);
  5. **a data and benchmark business** for private markets, with an AI copilot on top.

  **Technology revenue roughly doubled**, from $785M (2018) to about $1.5B (2023, parsed), with annual contract value (ACV) growing 11–16% a year. It is still under 10% of BlackRock's revenue. Its strategic value is larger than its revenue: it makes BlackRock the default **language** of other firms' portfolios. That creates switching costs, and since Preqin it also creates a neutrality problem. **What isn't proven:** client counts and growth are self-reported, and there is no independent evidence on retention or margins.

---

## 1. Chronology

| Date | Step | Source | Number |
|---|---|---|---|
| 2018 | Tech services revenue +19% | FY2018 release | $785M |
| 2019-03 | **eFront** acquired: private-markets software | Release | $1.3B; eFront 700+ clients in 48 countries |
| 2019-04 | Fink: Aladdin to become "the language of portfolio construction" for wealth managers | 2019 letter | 200+ clients, "over a dozen operational APIs" |
| 2020-04-07 | **Aladdin on Microsoft Azure** | Release | — |
| 2020-12-01 | Aladdin Climate; Sustainalytics/Refinitiv ESG data | Release | 1,200 KPIs |
| 2021-01-14 | **Clarity AI** stake (ML-driven ESG data) | Release | — |
| 2021-02-22 | **Aladdin Data Cloud on Snowflake**; Aladdin Studio for developers | Newsroom | — |
| 2021-04 | "Aladdin enabled us to rebuild BlackRock beyond its walls" (Fink) | 2021 letter | 250+ third-party clients |
| 2021-06 | Baringa climate scenario model bought and embedded | Release | Used on $15T+ assets |
| FY2021 | Revenue $1.3B; ACV +13% | Earnings | — |
| FY2022 | "record net new sales of Aladdin" in a down year | Earnings | Revenue $1.4B (deck); 98% 3-yr retention |
| 2023-03 | SVB week: Aladdin usage spikes; Aladdin Wealth usage "more than doubled" | 2023 AGM | — |
| 2023-06-14 | Investor Day: "Platform as a Service"; "Low to mid–teen long–term growth target"; ~$12.5B addressable market | 2023 deck | 130,000+ users |
| 2023-06-14 | **Avaloq** minority stake: core banking + Aladdin Wealth | Release | — |
| 2024-03 | "Aladdin AI copilots" and "openness supporting ecosystem partnerships" | 2024 letter | $1.5B 2023 revenue (letter) |
| 2024-06-30 | **Preqin** to be bought: data, benchmarks, indices | Release and deck | ~$240M recurring revenue; private-markets data TAM $18B by 2030 |
| 2025-03-03 | Preqin closes; Preqin benchmarks inside Aladdin | Release | — |
| 2025-06-12 | Investor Day: "The language of the whole portfolio"; Aladdin Copilot; addressable market $20B+ | 2025 deck | 360,000+ Aladdin and Preqin users; API calls 17x since 2023 |
| 2026-03 | Preqin data "unified" on Aladdin; 16% organic ACV growth in 2025 | 2026 letter | — |
| Q3 2026 | Tech services and subscription revenue +14% year on year | Earnings | Nine months: $1,684M vs $1,450M (parsed) |

## 2. How BlackRock describes Aladdin

- "As both a user and a provider of Aladdin, this decision reflects BlackRock’s ongoing commitment to continuous innovation and scalable operating solutions," (Rob Goldstein, Azure, 2020-04-07)
- "Aladdin has been on a journey for three decades to put data at the heart of the investment process." (Goldstein, Snowflake, 2021-02-22)
- "asset managers have to be as good at using technology as anything else they do – and as good at it as any tech firm." (Fink, 2020-03-30)
- "It remains the language of portfolios, uniting all of BlackRock" (Fink, 2024-03-26)
- "This presents a substantial opportunity for Aladdin to bridge the transparency gap between public and private markets through data and analytics," (Sudhir Nair, Preqin, 2024-06-30)
- "In other words, Preqin effectively does for private markets what Zillow did for housing." (Fink, 2025-03-31)
- "With clearer, more timely data, it becomes possible to index private markets just like we do now with the S&P 500." (Fink, 2025-03-31)
- "AI can be a powerful business accelerator for Aladdin, amplifying the strengths of its scale, deep resources, proprietary data, and extensive embedded network" (Fink, 2026-03)
- On private assets in 401(k)s: "we are going to be the engine that powers that data and analytics." (Fink, CNBC 2025-10-17)

## 3. The economics (BlackRock figures)

| Metric | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Tech services revenue | $785M | $974M (parsed) | $1,139M (parsed) | ~$1.3B | $1.4B (deck) | ~$1.5B | >$1.6B (letter) | n/a in text |
| ACV growth | — | — | — | +13% | — | — | +12% | +16% organic (2026 letter) |
| Clients / users | 200+ clients | — | — | 250+ third-party | — | 130,000+ users | 1,000+ clients (Preqin release) | 360,000+ Aladdin and Preqin users |

*Read:* this is software-grade growth (low to mid teens) on a small base relative to ~$20B+ firm revenue. Investor Day 2025 targets **private markets plus technology at ≥30% of revenue by 2030**, so Aladdin and Preqin are half of the re-rating story told in [[blackrock-private-markets]] §3.

## 4. What the claims don't prove

1. **User counts change definition.** *Clients* (2019), *third-party clients* (2021), *users* (2023) and *Aladdin and Preqin users* (2025) are different units. The "~3x" user growth since 2023 is mostly Preqin seats being added.
2. **The 98% 3-year average retention (2023 deck)** slips to 97% in 2025. Both figures are self-reported, with no cohort data.
3. **Margins are not disclosed.** Technology is not reported as a segment with operating income.
4. **AI benefits are asserted.** Systematic's LLM beat GPT-4o (61% vs 55% accuracy on 40-day forward returns, 2025 deck) on BlackRock's own test. Copilot productivity is unquantified.
5. **The "transparency gap" claim cuts both ways.** Preqin's data comes from GP and LP reporting. BlackRock is a large GP. The deck promises "safeguarding GP/LP data through information barriers", but nothing in the corpus shows how that is audited.

## 5. Strategic read (inference — not BlackRock's words)

- **Being the user sells the product.** Clients buy Aladdin partly because BlackRock trusts it with $10–15T. That same fact is the main objection from rival managers, who must hand portfolio data to a competitor's software.
- **The moat is the book of record, not the analytics.** Once Aladdin holds positions, trades, accounting and now private-markets cash flows, it becomes very costly to replace. APIs (17x usage growth) and venue integrations make it the hub other systems attach to. See [[canon-shapiro-varian-information-rules]].
- **The Preqin bet is an index-provider bet.** Public-markets index providers (S&P Dow Jones, MSCI, FTSE Russell) earn rents from being the reference. BlackRock pays those rents on iShares. Owning the reference for private assets reverses the flow, and puts BlackRock against MSCI (Burgiss), S&P, LSEG and Bloomberg. See [[spglobal-hub]], [[lseg-hub]], [[bloomberg-hub]].
- **AI favours whoever holds the labelled data.** Aladdin's portfolio, trade and private-markets records form a training set no external AI vendor has. That is Fink's 2026 argument, and it echoes Tradeweb's point about its own data ([[tradeweb-tech-ai-data]]).

## 6. Canon lenses

- **Platforms** ([[canon-cusumano-business-of-platforms]], [[canon-parker-platform-revolution]]): Aladdin is an industry platform (the hub) and also a transaction platform (venue connectivity). Watch for the classic risk of the platform owner competing with its complementors.
- **7 Powers** ([[canon-helmer-7-powers]]): switching costs (book of record), cornered resource (Preqin data), scale economies (fixed-cost software).
- **Innovator's dilemma** ([[canon-christensen-innovators-dilemma]]): an asset manager that builds software sold to its own competitors is a deliberate self-cannibalization.
- **Information theory** ([[canon-shannon-information-theory]]): "language of portfolios" as an analogy. A common encoding lowers transmission cost between systems, and whoever sets the code captures value.

## 7. Practitioner counterpoint

- **For:** Aladdin survives repeated stress tests: COVID, the 2022 rates shock, SVB week. Clients use it for exposure and broker restrictions ("Aladdin was built for times of market dislocation", Fink, 2023 AGM). The 2025 deck footnote benchmarks Aladdin's growth against State Street's Charles River, Clearwater, S&P, Morningstar, MSCI, Enfusion, Broadridge and Temenos. So there are alternatives, and clients choose Aladdin anyway.
- **Against:** concentration risk at the system level. Much of global asset management running on one vendor's risk models is a common-mode failure point ([[canon-perrow-normal-accidents]]). The corpus contains no regulator view on this.
- **Both:** if you are evaluating Aladdin as a client, ask for data portability terms and an exit plan before signing, because the switching cost is the product.

## 8. Open questions to track

1. Does BlackRock launch Preqin-branded **private-markets indices** licensed to third parties?
2. Do other managers publicly drop or adopt Aladdin after the Preqin purchase?
3. Is technology ever reported as a segment with margins?
4. Does the Aladdin–Tradeweb integration reach direct RFQ and AiEX? See [[blackrock-anchor-client]] §9.

**Links:** [[blackrock-hub]] · [[blackrock-anchor-client]] · [[blackrock-private-markets]] · [[blackrock-strategy-financials]] · [[tradeweb-tech-ai-data]] · [[tradeweb-ai-price]] · [[bloomberg-terminal-instrumentation]] · [[wss-ai-economics]] · [[bloomberg-hub]] · [[spglobal-hub]] · [[lseg-hub]] · [[canon-cusumano-business-of-platforms]] · [[canon-helmer-7-powers]] · [[canon-shapiro-varian-information-rules]] · [[canon-perrow-normal-accidents]]

---
### Rep
**Value Aladdin as a standalone software business.**

**(a)** Take ~$1.6B of 2024 technology revenue and ~12% ACV growth. Apply a software multiple of 10x revenue. What is Aladdin worth, and what share of BlackRock's ~$280B 2030 market-cap ambition (2025 deck) does that represent today?
*Answer:* ≈ **$16B**, about 6% of $280B.

**(b)** Grow revenue at 12% to 2030. What is 2030 revenue, and the value at the same multiple?
*Answer:* $1.6B × 1.12⁶ ≈ **$3.2B**, so ≈ **$32B**.

**(c)** Argue in one paragraph whether the larger value is the software itself or its effect on BlackRock's asset-management flows (the *user and provider* loop). Which number would you need from BlackRock to settle it?

---
**Sources:**
- [FY2018 earnings, 2019-01-16](https://ir.blackrock.com/files/doc_news/archive/1e73cdf2-0a27-4c3c-8ab1-04fd74fd8ec0.pdf)
- [eFront, 2019-03-22](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2019/BlackRock-to-Acquire-eFront----Industry-Leading-Alternatives-Investment-Software-Provider/default.aspx)
- [2019 Chairman's letter, 2019-04-08](https://www.sec.gov/Archives/edgar/data/1364742/000119312519099885/d642785ddefa14a.htm)
- [Aladdin on Azure, 2020-04-07](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2020/BlackRock-and-Microsoft-Form-Strategic-Partnership-to-Host-Aladdin-on-Azure-as-BlackRock-Readies-Aladdin-for-Next-Chapter-of-Innovation/default.aspx)
- [Aladdin Climate, 2020-12-01](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2020/BlackRock-Unveils-New-Offering-to-Power-Investors-Transition-to-Net-Zero-Emissions/default.aspx)
- [Clarity AI, 2021-01-14](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2021/BlackRock-Boosts-Aladdins-Forward-Looking-Sustainability-Analytics-and-Reporting-Capabilities-Through-Strategic-Partnership-with-Clarity-AI/default.aspx)
- [Snowflake, 2021-02-22](https://www.blackrock.com/corporate/newsroom/media/press-releases/aladdin-data-cloud-powered-by-snowflake)
- [2021 Chairman's letter, 2021-04](https://www.blackrock.com/corporate/investor-relations/2021-larry-fink-chairmans-letter)
- [AGM 2023, 2023-05-24](https://s24.q4cdn.com/856567660/files/doc_downloads/2023/05/2023-blk-annual-shareholder-meeting-transcript.pdf)
- [Investor Day 2023, 2023-06-14](https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BlackRock-2023-Investor-Day.pdf)
- [Avaloq, 2023-06-14](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2023/BlackRock-and-Avaloq-Unveil-Strategic-Partnership-to-Provide-Integrated-Technology-Solutions-Meeting-Evolving-Needs-of-Wealth-Managers/default.aspx)
- [Preqin, 2024-06-30](https://ir.blackrock.com/files/doc_events/2024/BLK-Preqin-Press-Release.pdf)
- [Preqin close, 2025-03-03](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2025/BlackRock-Establishes-Preeminent-Private-Markets-Technology-and-Data-Provider-with-Close-of-Preqin-Acquisition/default.aspx)
- [2025 letter, 2025-03-31](https://www.blackrock.com/corporate/investor-relations/2025-larry-fink-annual-chairmans-letter)
- [Investor Day 2025, 2025-06-12](https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf)
- [2026 letter, 2026-03](https://www.blackrock.com/corporate/investor-relations/larry-fink-annual-chairmans-letter)
- [Q3 2026 earnings, 2026-10-14](https://ir.blackrock.com/files/doc_financials/2026/Q3/BLK-3Q26-Earnings-Release.pdf)
