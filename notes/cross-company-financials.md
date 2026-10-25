# Note · Cross-company financials — the strategist's numbers: growth came from different engines, and almost every firm's returns depend on whether you count the goodwill it paid for them

> Cross-company analysis note · Maps to **Course 01** (Accounting — goodwill, adjusted vs GAAP), **Course 02** (Corporate Finance & Valuation — ROIC, FCF, capital allocation), **E2** (Capital Allocation), **E3** (M&A — what deals did to returns) · Written 2026-10-25 · Part of the cross-company set: [[cross-company-attention-map]], [[cross-company-say-vs-do]], [[cross-company-capability-matrix]], [[cross-company-narrative-vs-numbers]]

- **Source:** SEC XBRL company facts (the structured data behind every **10-K and 10-Q**), pulled by `_ingest/financials.py` for the eight US-listed firms: Tradeweb, MarketAxess, ICE, S&P Global, Thomson Reuters (40-F, IFRS), BlackRock, Goldman and JPMorgan.
  - **Outputs:** `_ingest/raw/financials/annual.csv` (FY2018–25, every value with its XBRL tag), `derived.csv` (ratios) and `quarterly.csv` (2018–Q2 2026; Q4 derived as full year minus Q1–Q3).
  - **Not covered:** LSEG (UK-listed, not on EDGAR) and Bloomberg (private). LSEG figures come from its annual reports via [[lseg-capital-allocation]].
  - **Cross-checked:** ICE net revenue matches the audited 10-K figures exactly ($5,202M FY19, $9,931M FY25; [[cross-company-say-vs-do]]), and Tradeweb's Q1/Q2 2026 revenue matches [[tradeweb-strategy-financials]].
- **Core claim:** On GAAP numbers, the ten-firm set splits three ways:
  1. **Organic compounders with almost no debt:** Tradeweb (17.6% revenue CAGR, operating margin 24% to 41%, FCF margin 52%) and, until 2021, MarketAxess.
  2. **Acquirers whose reported returns on capital are single digits**, because the price of the deals sits on the balance sheet as goodwill: ICE (ROIC ~8%, ~97% excluding goodwill), S&P after IHS Markit (ROIC fell from ~60% to ~11%), and Tradeweb itself, whose Refinitiv step-up makes ROIC 10% against 27% ex-goodwill.
  3. **Capital returners** that paid out more than their free cash flow: S&P, Thomson Reuters and BlackRock at 112–123% of 2019–25 FCF. The banks bought back 14–15% of their shares.
  
  The question a strategist asks of each firm is how much its returns depend on the price it paid. The answer differs a lot across the set.

---

## 1. The scoreboard, FY2019 → FY2025 (GAAP, as filed)

| | Revenue FY19 → FY25 ($M) | CAGR | Op. margin FY19 → FY25 | FCF margin FY25 | ROIC FY25 | ROIC ex-goodwill | Net debt / EBITDA | Goodwill + intangibles / assets | Diluted shares FY19 → FY25 |
|---|---|---|---|---|---|---|---|---|---|
| **Tradeweb** | 776 → 2,052 | **17.6%** | 24% → **41%** | **52%** | 10% | 27% | net cash (−1.9×) | 52% | +37%* |
| **MarketAxess** | 511 → 846 | 8.8% | 49% → **40%** | 38% | 17% | 23% | net cash | 20% | −2% |
| **ICE** (net) | 5,202 → 9,931 | 11.4% | 51% → 50% | 39% | **8%** | **97%** | **3.1×** | 34% | +2% |
| **S&P Global** | 6,699 → 15,336 | 14.8% | 48% → 42% | 36% | 11% (was 57% in FY19) | n/m | 1.6× | **86%** | **+24%** |
| **Thomson Reuters** | 5,906 → 7,476 | 4.0% | 20% → 29% | 27% | 12% | 45% | 0.8× | 61% | **−11%** |
| **BlackRock** | 14,539 → 24,216 | 8.9% | 38% → **29%** | 15% | 9% | 58% | 0.2× | 37% | +2% |

| Banks | Revenue FY19 → FY25 ($M) | CAGR | ROE FY25 | ROTCE FY25 | Efficiency ratio FY19 → FY25 | Diluted shares FY19 → FY25 |
|---|---|---|---|---|---|---|
| **Goldman** | 36,546 → 58,283 | 8.1% | 14% | **16%** | 68% → 64% | **−15%** |
| **JPMorgan** | 115,720 → 182,447 | 7.9% | 16% | 18%† | 56% → **52%** | **−14%** |

*Notes:*
- **Definitions.** ROIC = NOPAT ÷ average (debt + total equity); cash is not netted, so buyback-heavy filers stay meaningful. "Ex-goodwill" removes goodwill and acquired intangibles from invested capital.
- **\* Tradeweb's share count** rises mainly because pre-IPO LLC units were exchanged into Class A shares, not from new issuance.
- **† JPMorgan's ROTCE** is understated here because its preferred stock isn't tagged in annual XBRL. JPM states 18–23% for 2021–25 itself ([[jpmc-capital-allocation]]).
- **LSEG** (annual reports, £): total income £2,314M (FY19, pre-Refinitiv basis) to £8,986M (FY25). Adjusted EBITDA margin about 50%, leverage under 2× before Octus ([[lseg-capital-allocation]]).

## 2. Five things the numbers say that the narratives don't

1. **Tradeweb is the only compounder that grew *and* expanded margins.** Revenue rose 2.6× while the operating margin went from 24% to 41%, with no debt and FCF above half of revenue. But only 20% of 2019–25 FCF went back to shareholders ($862M of $4.3B). The rest built cash, and that cash now funds Trumid's ~$1.89B ([[tradeweb-strategy-financials]]). The "self-funded" story is real. Trumid is the test of whether the hoard earns its keep.
2. **MarketAxess's decline is visible in every line.** The operating margin fell from 54% (FY20) to 40%, ROIC from 35% to 17%, and in FY25 it paid out **165% of FCF**, the debt-funded buyback seven months before the sale. Growth since FY20 was ~4% a year ([[marketaxess-strategy-financials]]).
3. **Acquisitions turned high-return businesses into average-looking ones on paper.**
   - **S&P:** ROIC ~60% (FY19–21) fell to ~11% after the IHS Markit merger. Goodwill and intangibles are now **86% of assets**, and the share count rose 24% because the deal was paid in stock.
   - **ICE:** ROIC sits at 7–8% every year, against ~100% excluding goodwill.
   - **The underlying franchises earn enormous returns on tangible capital.** Whether the deals created value depends on whether ~8–11% beats the cost of capital (roughly 8–9% for these firms, context). Barely, so far.
4. **BlackRock's GAAP margin fell from 38% to 29%** as GIP/HPS/Preqin brought deal amortisation, integration costs and lower-margin private-markets revenue. FCF margin halved to 15% in FY25, and the 10-K doesn't tag its FY25 buyback cash flow. Its "adjusted" margin is higher. The gap between the two is the price of the private-markets pivot ([[blackrock-private-markets]]).
5. **The banks shrank their share count while growing revenue ~8% a year.** Goldman −15% and JPMorgan −14% of diluted shares, with $67B and $209B returned since 2019. Both improved efficiency. Goldman's ROTCE (16%) is back near JPMorgan's, but by a different route than the 2020 plan ([[goldman-strategy-financials]]).

## 3. Momentum: the last six quarters (revenue YoY, as filed)

| | Q1 25 | Q2 25 | Q3 25 | Q4 25 | Q1 26 | Q2 26 |
|---|---|---|---|---|---|---|
| Tradeweb | +25% | +27% | +13% | +12% | **+21%** | **+9%** |
| MarketAxess | −1% | +11% | +1% | +3% | +12% | **0%** |
| ICE (net) | +8% | +10% | +3% | +8% | **+20%** | +5% |
| S&P Global | +8% | +6% | +9% | +9% | +10% | n/a yet |
| BlackRock | +12% | +13% | +25% | +23% | +27% | **+31%** |
| Goldman | +6% | +15% | +20% | −3% | +14% | **+39%** |
| JPMorgan | +8% | −11%‡ | +9% | +7% | +10% | **+28%** |

‡ Q2 2024 included a one-off Visa share gain, which depresses the Q2 2025 comparison.

**Reading it:**
- **Q1 2026 was a volatility quarter** for the venues (Tradeweb +21%, ICE +20%, MarketAxess +12%). **Q2 normalised fast** (Tradeweb +9%, MarketAxess 0%). That's the volatility beta the narratives play down ([[tradeweb-mission-forces]]).
- **BlackRock's +23–31%** is mostly the GIP/HPS/Preqin consolidation, i.e. acquired growth.
- **The banks' Q2 2026 jumps are as filed.** I haven't decomposed them; check the earnings releases before reading them as trend.
- **Q3 2026 10-Qs** arrive between late October and early November. Re-run `python3 _ingest/financials.py` to extend the series.

## 4. Capital allocation, 2019–2025 (cumulative, $M)

| | FCF | Buybacks + dividends | Paid out / FCF | Cash acquisitions | Big deals (incl. stock) |
|---|---|---|---|---|---|
| Tradeweb | 4,324 | 862 | **20%** | 1,138 | Nasdaq FI, Yieldbroker, r8fin, ICD; Trumid ~$1.97B pending |
| MarketAxess | 1,993 | 1,390 | 70% (165% in FY25) | 115 | small tuck-ins; sold to ICE |
| ICE | 21,349 | 10,872 | 51% | **20,178** | Ellie Mae $11B, Black Knight ~$11.9B; MarketAxess ~$5.7B pending |
| S&P Global | 26,817 | **32,434** | **121%** | 2,805 | IHS Markit (all-stock, ~$44B) |
| Thomson Reuters | 9,708 | 11,989 | **123%** | 4,055 | Casetext etc.; funded partly by the LSEG stake sale |
| BlackRock | 27,279 | 30,645 | **112%** | 9,237 | GIP, HPS, Preqin (largely stock) |
| Goldman | n/m | 66,929 | — | 2,662 | — |
| JPMorgan | n/m | 208,657 | — | 12,282 | First Republic (2023) |

**Read:** payout above 100% of FCF (S&P, Thomson Reuters, BlackRock) means buybacks were funded partly by asset sales (Thomson Reuters' LSEG stake, S&P's post-merger divestitures) or by debt. ICE spent almost as much on acquisitions as it returned, which is the "debt-funded mega-deal, then deleverage" cycle ([[ice-strategy-financials]]). Tradeweb returned the least and is now the buyer.

## 5. Deal multiples on one basis (from the company notes)

| Deal | Price | Implied multiple | Source |
|---|---|---|---|
| ICE ← Ellie Mae (2020) | $11B EV | ~23× EBITDA, ~12× revenue | [[ice-strategy-financials]] |
| ICE ← Black Knight (2023) | ~$16B EV at signing | ~20× unsynergised EBITDA | [[ice-strategy-financials]] |
| ICE ← MarketAxess (2026) | ~$5.7B EV | ~13× EBITDA before synergies (~10.6× after) | [[ice-marketaxess-deal]] |
| Tradeweb ← Trumid (2026) | ~$1.97B (incl. ~$220M tax assets) | ~1.8× *Tradeweb's own* FY25 EBITDA; Trumid's financials undisclosed | [[tradeweb-strategy-financials]] |
| LSEG ← Octus (2026) | $3.535B | ~11–12× revenue, ~29× EBITDA (inference) | [[lseg-capital-allocation]] |
| LSEG ← Refinitiv (2021) | ~$27B EV, all-stock | — | [[lseg-refinitiv-deal]] |

**Read:** the 2026 credit deals were priced very differently. ICE paid ~13× for a slowing but profitable venue. LSEG paid ~29× EBITDA for a fast-growing private-credit data business. Tradeweb didn't disclose what it bought. That's the gap a strategist would press management on.

## 6. What these numbers don't prove

1. **GAAP vs adjusted.** Every firm here runs an "adjusted" story that excludes acquisition amortisation. This note is deliberately GAAP-based, so it shows the cost of deals that adjusted figures hide. Neither view alone is "true".
2. **XBRL gaps.** Thomson Reuters' IFRS tags are sparse (no equity series, so ROE isn't available). BlackRock's FY25 buyback isn't tagged. JPMorgan's preferred stock isn't tagged. These are flagged rather than filled.
3. **ROIC definition choices** (no cash netting, statutory tax rate capped at 35%) change levels, not rankings.
4. **No market data yet.** Without share prices there are no valuation multiples, reverse DCFs or FCF yields. That needs a price source (see §8).

## 7. Canon lenses

- **Capital allocation** ([[canon-bezos-shareholder-letters]], [[canon-munger-poor-charlies-almanack]]): judge per-share FCF and return on capital, not adjusted EPS.
- **Margin of safety** ([[canon-klarman-margin-of-safety]]): paying 20–29× EBITDA (Ellie Mae, Octus) leaves no room for the growth case to slip.
- **Luck vs skill** ([[canon-mauboussin-success-equation]]): the Q1/Q2 2026 swing at the venues shows how much growth is the market.

## 8. Open questions and next data

1. **Valuation:** add share prices to compute EV/EBITDA, P/E, FCF yield and a reverse DCF per firm. That needs a price data source; it's the next decision.
2. **Proxy statements:** what are executives paid on (adjusted EPS, ROIC, TSR)? That predicts deal behaviour.
3. **Trumid's financials** (Tradeweb 8-K / investor deck), so the deal can be put on the same basis as §5.
4. **Q3 2026 10-Qs:** is Q2's normalisation at the venues a trend?

**Links:** [[cross-company-narrative-vs-numbers]] · [[cross-company-say-vs-do]] · [[cross-company-capability-matrix]] · [[cross-company-attention-map]] · [[tradeweb-strategy-financials]] · [[marketaxess-strategy-financials]] · [[ice-strategy-financials]] · [[ice-marketaxess-deal]] · [[spglobal-strategy-financials]] · [[blackrock-strategy-financials]] · [[blackrock-private-markets]] · [[goldman-strategy-financials]] · [[jpmc-capital-allocation]] · [[lseg-capital-allocation]] · [[lseg-refinitiv-deal]] · [[thomsonreuters-capital-allocation]] · [[sec-filing-intelligence]] · [[canon-bezos-shareholder-letters]] · [[canon-munger-poor-charlies-almanack]] · [[canon-klarman-margin-of-safety]] · [[canon-mauboussin-success-equation]]

---
### Rep
1. **Recompute ICE's ROIC both ways.** From `_ingest/raw/financials/annual.csv` take ICE's FY2025 operating income, income tax, pre-tax income, debt, equity, goodwill and intangibles. Compute NOPAT, ROIC on total capital, and ROIC excluding goodwill and intangibles. In one paragraph: which number should the board use to judge the MarketAxess deal, and why?
2. **The Tradeweb cash question.** Tradeweb paid out 20% of its 2019–25 FCF. Suppose instead it had paid out 70% (MarketAxess's ratio). How much cash would it have had for Trumid? What would it have needed to borrow?
3. **Extend the series.** After the Q3 2026 10-Qs are filed, run `python3 _ingest/financials.py` and update §3. Did Q2's slowdown at the venues continue?
