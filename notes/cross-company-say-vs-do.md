# Note · Cross-company say-vs-do audit — newsrooms talk about the next business and stay quiet about the current one, and every firm's 10-K worries about what its press office never mentions

> Cross-company analysis note · Maps to **Course 01** (Accounting — segment reporting, revenue recognition), **Course 07** (Data, Analytics & Decision-Making — triangulating sources), **E8** (Stakeholder & Investor Relations — disclosure vs messaging), **E4** (Corporate Governance — controlled companies, risk oversight), **E6** (Crisis Leadership — operational risk) · Written 2026-10-25 · Part of the cross-company set: [[cross-company-attention-map]], [[cross-company-capability-matrix]]

- **Source:** two independent sources set against each other.
  - **Newsroom attention, 2023–2026:** from [[cross-company-attention-map]].
  - **FY2025 revenue by line, and FY2025 risk factors:** from each company's own filing. 10-Ks for Tradeweb, MarketAxess, ICE, S&P Global, BlackRock, Goldman and JPMorgan; Thomson Reuters' 40-F annual report; LSEG's 2025 annual report. Extracted to `_ingest/raw/audit/<ticker>.json` (raw filings in `_ingest/raw/audit/edgar/`).
  - **Computed by** `_ingest/say_vs_do.py`, with an explicit filing-line to topic map in the script. Outputs: `revenue_by_topic.csv`, `attention_vs_revenue.csv`, `silence.csv`.
  - **Bloomberg** is private and discloses no revenue or risk factors, so it isn't in this audit.
- **Core claim:** Set side by side, the two sources show the same pattern at nine firms. **The newsroom over-represents what the company wants to become and under-represents what pays the bills today**, by 30–70 percentage points for the core business. The 10-K is where the company is most candid, about outages, concentration and control. Those same risks appear in under 3% of its press output. None of this is deception, since both documents are public. But someone who reads only the newsroom would misjudge where each firm's money and fragility sit.

---

## 1. How the comparison works

- **Revenue side:** every FY2025 revenue line in the filing is mapped to one topic in the shared taxonomy. The mapped lines reconcile exactly to the reported totals:

  | Company | FY2025 total |
  |---|---|
  | Tradeweb | $2,052M |
  | MarketAxess | $846M |
  | ICE | $9,931M net |
  | S&P Global | $15,336M |
  | BlackRock | $24,216M |
  | Thomson Reuters | $7,476M |
  | LSEG | £8,986M total income |
  | Goldman | $58,283M |
  | JPMorgan | $185,581M managed basis ($182,447M reported) |

  - **Excluded as "other"** (no taxonomy home): news, FX, investment-banking advisory, corporate treasury, Mobility, Risk Intelligence. That's 0–18% of revenue per company, shown in each table.
  - **ICE:** line items are gross, so ICE's $2,709M of transaction-based expenses (mostly equity rebates and regulatory fees) is netted against cash equities.
- **Attention side:** share of business-topic tags in 2023–2026 newsroom items, normalised to 100% over the 16 business topics. AI and digital assets are included as "topics with no revenue line".
- **Gap = attention share − revenue share, in percentage points.** A large negative gap means a business that's under-talked; a large positive one means a topic that's over-talked.
- **Caveats:**
  - Goldman, JPMorgan and BlackRock corpora were **filtered to the market-structure lens** when collected, so their consumer/retail under-talk is partly built in. Weight their rows lightly on retail.
  - The mapping is approximate where filings bundle businesses. For example, Goldman's FICC is mapped wholly to rates, though it includes credit, FX and commodities. LSEG's "Fixed Income, Derivatives & Other" (mostly Tradeweb) is mapped to rates.

## 2. Say vs do, company by company (attention 2023–26 vs FY2025 revenue)

| Company | Most **under-talked** (revenue share → attention share) | Most **over-talked** (attention, with little or no revenue) | Read |
|---|---|---|---|
| **Tradeweb** | Rates **63% → 22%** (−41pp); credit 24% → 13% | Workflow 14%, derivatives 11%, tokens 9%, indices 5%, AI 4% | Rates (Treasuries, swaps, repo; $1.27B, 62% of revenue) pays for the company. The newsroom leads with credit, workflow and new markets. Tokenization is ~$12M of "other" revenue at most |
| **MarketAxess** | Credit **88% → 33%** (−54pp) | Pricing/data 26% (vs 7% of revenue), workflow 15% (vs 2%), AI 8% | Its whole revenue base is credit commissions. Its newsroom keeps pivoting to data (CP+), automation and AI: the diversification story while US credit shrank ([[marketaxess-strategy-financials]]) |
| **ICE** | Energy **24% → 12%**; mortgages **21% → 9%**; data 23% → 15% | Indices 8% (inside the data line), rates 5%, credit 5% (vs 1%), listings 9% (vs 5%) | The two biggest swing factors, energy futures and Black Knight/Ellie Mae, are under-told. Listings and fixed income get more attention than their revenue justifies |
| **S&P Global** | Ratings **34% → 4%** (−30pp); data 36% → 24% | **AI 19%**, workflow 10%, private markets 7%, tokens 3% | Ratings, a third of revenue and the most regulated, highest-margin franchise, barely appears. AI is the most-published topic with no separate revenue line ([[spglobal-ai-data-layer]]) |
| **BlackRock** | ETFs and index **46% → 13%** (−34pp); fixed-income active 8% → 1% | **Private markets 33% (vs 18%)**, AI 5%, tokens 5% | iShares pays; private markets is the story. That's consistent with the 2024 GIP/HPS/Preqin bet ([[blackrock-private-markets]]). The private-markets revenue share is real and rising, but the newsroom runs ahead of it |
| **Thomson Reuters** | Professional software **100% → 30%** of mapped revenue | **AI 59%** | Legal, tax and corporates software is all the mapped revenue. The newsroom is mostly AI. The AI is embedded in those products (CoCounsel), so this is the "same revenue, new story" case ([[thomsonreuters-ai-strategy]]) |
| **LSEG** | Tradeweb line (mapped to rates) **19% → 5%**; workflows 24% → 15% | AI 11%, indices 16% (vs 12%) | The fastest-growing line is a subsidiary it talks about least. Pattern 1 of [[lseg-hub]] confirmed numerically |
| **Goldman** | FICC **28% → 1%**; wealth 29% → 11% (filtered corpus) | **AI 20%**, private markets 17% (vs 3%), tokens 5% | Trading revenue ($31B across FICC and equities, ~53%) is nearly invisible in the newsroom. The story is AI and alternatives fundraising ([[goldman-awm-private-credit]]) |
| **JPMorgan** | Consumer/wealth 57% → 9% (largely a filter effect); markets 21% → 9% | **Tokens 26%**, AI 13% | Kinexys is the most-published market-structure topic. Its revenue isn't broken out, and payments as a whole is 14% of revenue ([[jpmc-kinexys-deposit-tokens]]) |

### The pattern in one line
Every firm's largest negative gap is its **core cash generator**: rates, credit, energy, ratings, ETFs, legal software, trading. Every firm's largest positive gap is a **bet with no revenue line yet**: AI, tokens, private markets. That's rational IR: investors already price the core, so management sells the option value. But it means **newsroom reading systematically overweights optionality**, and readers should correct for it.

## 3. The silence audit: risks the filing names that the newsroom never mentions

Each cell is the number of FY2025 risk factors in the filing on that theme / the share of all newsroom articles (2019–26) that mention it at all. "Silence" means the filing lists at least one risk factor but fewer than 3% of articles mention the theme.

| Theme | TW | ICE | MKTX | SPGI | LSEG | TRI | GS | JPM | BLK |
|---|---|---|---|---|---|---|---|---|---|
| Operational outage | **5 / 0.8%** | 2 / 0.6% | **4 / 0.3%** | **4 / 1.8%** | 3 / 4.0% | 1 / 0.7% | **4 / 1.9%** | 5 / 5.5% | **8 / 1.0%** |
| Cyber | 1 / **0.0%** | 2 / 1.4% | 1 / 12.8% | 1 / 7.7% | 1 / 2.7% | 1 / 4.8% | 1 / 3.1% | 1 / 15.2% | 1 / 14.6% |
| Client concentration | **3 / 0.2%** | 0 / 0.1% | 2 / 1.4% | 1 / 0.0% | 0 / 1.7% | 1 / 0.3% | 1 / 0.0% | 1 / 0.6% | 2 / 1.9% |
| Controlling holder / related party | **9 / 2.3%** | — | — | — | — | **2 / 0.7%** | — | — | — |
| Fee pressure | 0 / 0.2% | 1 / 0.3% | 1 / **13.9%** | 0 / 1.2% | 0 / 1.1% | 0 / 0.3% | 1 / 0.0% | 0 / 1.8% | 0 / 3.9% |

*(Mention rates use broad keyword patterns over full texts, which is reliable for "almost never" but noisy above ~10%. Full table: `_ingest/raw/audit/silence.csv`.)*

**What it shows:**

1. **Operational fragility is the universal silence.** Seven of nine firms list 2–8 outage or systems-failure risk factors. Fewer than 2% of their articles mention outages, downtime or continuity.
   - **BlackRock** has 8 such factors, several specifically about Aladdin's scale: "Continuing enhancements to Aladdin's capabilities… have led to significant growth in Aladdin's processing scale". Its newsroom presents Aladdin purely as a growth platform ([[blackrock-aladdin-data]]).
   - **Tradeweb's** filing says "Systems failures, interruptions, delays in service… could materially harm our business". Its newsroom has never covered an outage, and **0.0%** of its articles mention cyber.
   - Since Tradeweb FTSE closing prices now set the WGBI ([[lseg-tradeweb-control]]), a Tradeweb outage at the close is a market-wide event. Neither firm discusses that.
2. **Control is disclosed, never discussed.**
   - **Tradeweb:** two filing headings say it plainly: "LSEG controls us and its interests may conflict with ours or yours in the future", and Tradeweb is a "controlled company" exempt from some Nasdaq governance rules. A third covers Refinitiv's right to require new share issuance. The other six are about the tax-receivable agreement and holding-company structure, which pay benefits to its pre-IPO owners. 2.3% of articles mention control at all, mostly boilerplate.
   - **Thomson Reuters:** "Woodbridge controls our company and is in a position to affect our governance and operations." 0.7% of its articles mention it.
3. **Client concentration lives only in the 10-K.** Tradeweb: "We are dependent on our dealer clients to support our marketplaces". MarketAxess: it "could lose significant sources of revenue and trading volume if we lose any of our significant institutional investor clients". Its newsroom celebrates the same clients as partners ([[tradeweb-outside-voices]], [[blackrock-anchor-client]]).
4. **Fee pressure: the honest outlier is the weak one.** MarketAxess is the only firm whose newsroom discusses fees (13.9% of articles), because its fee-per-million decline *is* its earnings story. Its filing adds: "past trends in commissions are not necessarily indicative of future commissions". Everyone else's fee rates appear in tables, not narrative.
5. **The reverse also happens.** Regulation, AI/technology change, acquisitions and volatility are discussed *more* in newsrooms than in filings. The newsroom frames them as opportunity: "the transparency machine", "AI everywhere", "volatility drives volume".

## 4. Revenue growth vs attention growth (FY2019 → FY2025)

Where comparable bases exist:

| Company | Revenue FY19 → FY25 | Fastest-growing line (comparable basis) | Did attention follow? |
|---|---|---|---|
| Tradeweb | $776M → $2,052M (+165%) | Money markets variable fees $26M → $156M (×6); rates variable $232M → $813M (×3.5) | **No.** Repo and money markets are barely covered. Rates attention is flat at ~30% |
| MarketAxess | $511M → $846M (+65%) | Rates variable $5M → $28M; information services $31M → $53M | Partly: data and automation attention rose as credit share fell |
| ICE (net) | $5,202M → $9,931M (+91%) | Mortgage tech $139M → $2,101M (acquired); energy $992M → $2,182M (×2.2) | **No.** Energy attention is flat to down. Mortgage coverage spiked only at deal times |
| S&P Global | $6,699M → $15,336M (+129%) | Market Intelligence $1,959M → $4,916M (IHS Markit); Indices $918M → $1,850M (×2) | Indices yes. Ratings growth (+52%) is invisible |
| BlackRock | $14,539M → $24,216M (+67%) | Illiquid alternatives base fees $488M → $2,350M (×4.8) | **Yes.** Private-markets attention rose ahead of the revenue |
| Thomson Reuters | $5,906M → $7,476M (+27%) | Corporates $1,321M → $1,987M (+50%); Tax & Accounting +54% | The narrative moved to AI. Growth came from the existing professional franchises |
| Goldman | $36,546M → $58,283M (+59%) | FICC financing $1,379M → $4,251M (×3); equities financing $3,017M → $7,195M (×2.4) | **No.** Prime and financing growth, the "durable" revenue ([[goldman-markets-platforms]]), is almost absent from the newsroom |
| JPMorgan | $115,627M → $182,447M (+58%) | Payments $4,565M → $19,331M (partly a re-segmentation) | Partly: payments and Kinexys get heavy coverage |

**Second pattern:** the fastest-*growing* revenue is often as under-covered as the core. Tradeweb's money markets/repo, ICE's energy, and Goldman's financing book are all unglamorous balance-sheet or plumbing businesses that newsrooms don't tell stories about.

## 5. What this does not prove

1. **Newsroom ≠ IR.** Earnings calls and investor days do discuss the core (the LSEG corpus includes them, and its gaps are smaller). This audit compares *press* output with filings, which is the right comparison for what the public and clients hear.
2. **Topic mapping is lossy.** For example, Thomson Reuters' AI *is* its workflow software, and Goldman's FICC includes credit. Gaps of under ~10pp shouldn't be read as meaningful.
3. **Risk-factor counts measure lawyerly granularity, not risk size.** Tradeweb's 9 control-related factors partly reflect its Up-C structure.
4. **Filtered corpora** make Goldman's, JPMorgan's and BlackRock's retail gaps partly artificial.

## 6. Strategic read (inference)

- **For an analyst:** use the newsroom to see where management wants to go, and the filing to see where the money and the fragility are. The gap between them is a map of **management's option bets**: AI at S&P, Thomson Reuters and Goldman; tokens at JPMorgan and Tradeweb; private markets at BlackRock and Goldman.
- **For a competitor:** the under-covered core is where an incumbent is least likely to be innovating in public. Tradeweb's repo and money-market growth and ICE's energy dominance are quiet strengths. MarketAxess's US credit decline was quiet weakness until the ICE deal.
- **For a board:** silence on operational risk is defensible in marketing but dangerous in a crisis, because there is no prior public narrative to fall back on. The firms with a **benchmark role** (Tradeweb/LSEG closing prices, ICE's benchmark administration, S&P indices) have the most to lose from that silence.

## 7. Canon lenses

- **Agency and disclosure** ([[canon-jensen-meckling-agency-theory]]): the 10-K is written for liability; the newsroom is written for valuation. The difference is information about what management fears.
- **Normal accidents** ([[canon-perrow-normal-accidents]]): tightly coupled infrastructure (closing prices into indices, Aladdin into the buy-side) makes the never-mentioned outage the highest-consequence event.
- **Luck vs skill** ([[canon-mauboussin-success-equation]]): the under-covered growth lines (repo, energy, financing) are the most rate- and volatility-driven. The newsroom gives the credit to strategy.
- **Pre-mortem thinking** ([[canon-klein-sources-of-power]]): the risk-factor section is a pre-mortem the company already wrote. Read it first.

## 8. Open questions

1. Has any of these firms ever published a post-incident report on its own outage? Search each corpus for "incident", "outage" and "restored".
2. If ICE keeps MarketAxess's disclosure habits, does the fee-per-million table survive? If not, credit fee pressure becomes invisible industry-wide.
3. Tradeweb's money-markets line grew ×6. Does management start telling a repo/Treasury-clearing story ahead of the Dec 2026 and Jun 2027 deadlines ([[tradeweb-derivatives-regulation]])?
4. Will S&P ever narrate ratings again, or only through AI and data?

**Links:** [[cross-company-attention-map]] · [[cross-company-capability-matrix]] · [[tradeweb-hub]] · [[tradeweb-strategy-financials]] · [[tradeweb-outside-voices]] · [[tradeweb-derivatives-regulation]] · [[lseg-tradeweb-control]] · [[lseg-hub]] · [[ice-strategy-financials]] · [[marketaxess-strategy-financials]] · [[spglobal-ai-data-layer]] · [[blackrock-private-markets]] · [[blackrock-aladdin-data]] · [[blackrock-anchor-client]] · [[thomsonreuters-ai-strategy]] · [[goldman-awm-private-credit]] · [[goldman-markets-platforms]] · [[jpmc-kinexys-deposit-tokens]] · [[sec-filing-intelligence]] · [[canon-jensen-meckling-agency-theory]] · [[canon-perrow-normal-accidents]] · [[canon-mauboussin-success-equation]] · [[canon-klein-sources-of-power]]

---
### Rep
1. **Recompute one row.** Open `_ingest/raw/audit/tw.json`. Sum the FY2025 rates and money-markets lines (variable + fixed) and divide by $2,052.4M. *(Answer: (813.2 + 280.3 + 156.2 + 17.6) / 2,052.4 ≈ **61.7%**.)* Then count Tradeweb's 2023–26 articles tagged `rates` in `_ingest/raw/attention/article_tags.csv`.
2. **Silence test.** Pick one company. Read its five operational-risk headings in its audit file, then search its `articles.jsonl` for "outage", "incident" and "restored". Write one paragraph: is the silence because nothing happened, or because nothing was said?
3. **Analyst memo.** For S&P Global, write three sentences an analyst would add to a newsroom-based summary to correct the ratings under-weighting, using the FY2019 → FY2025 ratings growth in §4.
