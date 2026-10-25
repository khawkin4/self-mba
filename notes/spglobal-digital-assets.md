# Note · S&P Global in digital assets — selling the "trusted" label to on-chain markets, one non-rating and one licence at a time

> Market-structure / innovation note · Maps to **Course 04** (Competitive Strategy: extending a brand into an adjacent market, partner-led entry), **Course 11** (Global Strategy & Responsible Business: regulation, GENIUS Act, reputational risk), **E9** (Geopolitics & Macro: stablecoins, 24/7 offshore venues), **E10** (Digital & AI Transformation: tokenization, smart contracts, oracles) · Written 2026-10-25 · Part of [[spglobal-hub]]; companions [[spglobal-indices-benchmarks]], [[spglobal-ai-data-layer]], [[tradeweb-tech-ai-data]]

- **Source:** S&P Global press and IR corpus, `_ingest/raw/spglobal/articles.jsonl`. About 25 items from Dec 2020 to Oct 2026 cover crypto indices, Ratings' DeFi group, stablecoin and vault assessments, tokenization licences, the Kaiko partnership and investment, and the OpenZeppelin deal. Several 2025–26 releases carry an S&P-written *digital-assets timeline*, which is used for dates. Tradeweb overlap comes from `_ingest/raw/tradeweb/articles-2019-2026.jsonl`. No trade volumes, fees or revenue for any digital-asset product are disclosed anywhere in the corpus.
- **Core claim:** S&P is not building crypto infrastructure. It rents out its **brand and governance** to people who do:
  - Index licences: Lukka, Centrifuge, Dinari, Trade[XYZ] on Hyperliquid, Kaiko and Pantera.
  - Ratings-style *opinions* that are explicitly **not credit ratings**: stablecoin assessments (2023), vault risk assessments (2026).
  - Distribution through crypto plumbing: Chainlink, Base, Canton.

  From 2025 it also started **buying in and investing**: it led Kaiko's Series B-2 and agreed to buy OpenZeppelin, placed under the Ratings president. In S&P's own words the strategy is "bringing trusted data, benchmarks and transparent risk assessment to markets as they move onchain" (Le Pallec, 2026-09-17). Two tensions run through the file:
  1. Ratings uses the credibility of its rating franchise while labelling each product *not a rating*.
  2. The index business guards S&P 500 rules strictly (the 2026 MegaCap refusal) but licenses the same index for **leveraged 24/7 perpetuals** offshore.

---

## 1. Chronology — the spine

All figures are as S&P states them ("S&P says"), unless another source is named.

| Date | Event | Numbers stated / note |
|---|---|---|
| **2020-12-03** | S&P DJI builds crypto index capability with **Lukka** pricing data (Lukka Prime fair-value method) | Custom indices first (IDX Insights, Q1 2021) |
| 2021-05-04 | S&P Digital Market Indices: Bitcoin, Ethereum, MegaCap | Lukka prices; the S&P DJI Index Committee administers |
| 2021-07-13 | S&P Cryptocurrency Broad Digital Market Index | 240+ coins at launch |
| **2022-05-17** | **Ratings forms a DeFi group.** Chuck Mounts is Chief DeFi Officer; Charles Jansen is Head of DeFi Transformation | The first dedicated digital-assets organisation |
| 2022-06-17 | Ratings research says stablecoins will compete with CBDCs or tokenized bank deposits | Early tokenization framing |
| Jan 2023 | S&P Cryptocurrency DeFi Index (S&P timeline) | — |
| **2023-12-12** | **Stablecoin Stability Assessments (SSAs).** Scale of 1 (very strong) to 5 (weak). USDC, USDP and GUSD **2**; USDT, DAI and FDUSD **4**; FRAX and TUSD **5** | The release ends: "This report does not constitute a rating action." |
| Feb–Sep 2025 | First *ratings* of tokenized treasury funds: Janus Henderson Anemoy, Delta Wellington, OpenEden TBILL | Proper ratings, on tokenized wrappers of ordinary assets |
| **2025-07-01** | S&P 500 licensed to **Centrifuge / Anemoy** (with Janus Henderson as sub-advisor) for a tokenized index fund | The SPXA token launched Sep 2025 (S&P timeline) |
| Aug 2025 | **Sky Protocol rated B-** (Stable), the first credit rating of a DeFi protocol | S&P timeline |
| 2025-10-07 | S&P Digital Markets 50 planned: 35 crypto-linked stocks plus 15 coins. **Dinari** issues a tracking token (dShares) | Hybrid equity-and-crypto benchmark |
| **2025-10-14** | **SSAs published on-chain via Chainlink DataLink**, starting on Base (Coinbase's L2) | Stablecoins "$301bn", up from "$173bn" a year earlier; the GENIUS Act is cited |
| 2025-11-13 | Investor Day lists DeFi, stablecoins and tokenization as Ratings growth drivers | The 2025 CEO letter says SSAs cover "more than 90 percent of stablecoins in circulation" |
| Feb 2026 | First rating of a bitcoin-backed structured finance deal (*Ledn*) | S&P timeline |
| Mar 2026 | S&P DJI and Kaiko tokenize the **iBoxx U.S. Treasuries Index** | S&P calls it "the first time a major index provider has made a financial benchmark available as a native digital asset" |
| **2026-03-18** | **S&P 500 licensed to Trade[XYZ] for perpetual contracts on Hyperliquid** | "first and only officially licensed" S&P 500 perpetual. For eligible **non-US** investors, leveraged, 24/7. XYZ cites $100B+ volume since Oct 2025 |
| 2026-07-21 | S&P Pantera Digital Asset Index (Artemis data): fundamentals-based, excludes "meme coins or Bitcoin" | A second, competing crypto index philosophy under the S&P name |
| **2026-09-01** | **S&P Kaiko Digital Asset Indices**: S&P DJI's and Kaiko's crypto indices rebranded onto Kaiko's technology stack | 4,000+ rates and indices; Kaiko connects to 150+ exchanges. Kaiko keeps its own BMR registration |
| **2026-09-14** | **S&P Global Ventures leads Kaiko's Series B-2** | Terms not disclosed |
| **2026-09-17** | **Agreement to acquire OpenZeppelin** (smart-contract security). It reports to Ratings President Yann Le Pallec | Its contracts "underpin over $37 trillion in value transferred"; 900+ security engagements; terms not disclosed; not material |
| **2026-10-04** | **Vault Risk Assessment (VRA)** for DeFi lending vaults: six risk factors, a letter scale | Vault deposits $1.5B (Sep 2024) → $10B (Sep 2026). "A VRA is not a credit rating" |
| **2026-10-13** | **First on-chain OTC swap on a tokenized benchmark**: a TRS on the tokenized iBoxx USD Liquid IG index, executed by DRW vs Marex on **Derivnex (Canton)** | Kaiko distributes the signed official index values |

**The Tradeweb thread (from the Tradeweb corpus):**
- **2026-06-11:** S&P Global and Tradeweb are both named among investors in Digital Asset's **$355M** raise. Digital Asset is the builder of Canton.
- **2026-07-15:** S&P Dow Jones Indices and Tradeweb are both named participants in DTCC's tokenized-collateral demonstration.
- Tradeweb's own on-chain work (Canton Treasury financing, 2025) is in [[tradeweb-tech-ai-data]]. Both firms sit on the same rail, Canton. S&P's product there is the benchmark; Tradeweb's is the trade.

## 2. Three businesses under one "digital assets" label

| Line | Division | What S&P sells | What the counterparty brings | S&P's risk |
|---|---|---|---|---|
| **Crypto and tokenized indices** | S&P DJI | Brand, administration, licensing, BMR/IOSCO governance | Data and calculation (Lukka → Kaiko), the venue (Hyperliquid, Canton, Centrifuge) | Index-brand reputation if a leveraged venue fails |
| **Risk opinions** | Ratings | SSAs, VRAs, protocol and fund ratings, on-chain delivery | Oracles (Chainlink), chains (Base), now OpenZeppelin's audit capability | The "not a rating" line blurs; NRSRO and CRA regulators look on |
| **Strategic stakes** | Corporate / Ventures | Capital and brand | Kaiko, OpenZeppelin, Digital Asset (Canton) | Venture risk; conflicts when the investee is also the calculation agent |

## 3. How the narrative moved

1. **2020–2021: bring transparency to a speculative market.** Roffman (2020): "the time is right for independent, reliable and user-friendly benchmarks." Roffman (2021): "Traditional financial markets and digital assets are no longer mutually exclusive markets." The releases still call the market "traditionally speculative".
2. **2022: Ratings sees both disruption and risk.** Elizabeth Mann, Ratings CFO: "there are both significant opportunities and risks." The DeFi group's remit is to explain the market to clients, not yet to rate it.
3. **2023: assessments, carefully labelled.** SSAs launch with the Tether score of 4 (*constrained*), and every SSA release repeats that these are not ratings. Analyst Lapo Guadagnuolo: "stablecoins are not immune to factors such as asset quality, governance, and liquidity."
4. **2025: from print to protocol.** Chainlink puts SSAs inside smart contracts. Mounts uses the house AI phrase: "meeting our clients where they are". Index licences move from data products to tradable tokens (Centrifuge, Dinari).
5. **2026: S&P invests and owns.** Kaiko stake, the OpenZeppelin acquisition, VRA, and the Canton swap. Clay (S&P DJI CEO) writes digital assets into the mission: "our mission to advance essential intelligence by bridging traditional and decentralized finance". Drinkwater on Canton: the deal "extends our credit franchise into on-chain finance".

## 4. What the claims don't prove

1. **"First" is the only metric.** The corpus has no revenue, no licence fees, no AUM for SPXA or dShares, and no open interest for the S&P 500 perpetual. "First and only officially licensed", "first OTC swap on Canton" and "first credit rating of a DeFi protocol" are milestones, not traction.
2. **The Canton swap is a single sample trade.** The release itself calls it "The sample transaction". The future steps (digital cash, collateral, margin on Canton) are described as "expected".
3. **"Not a rating" carries the rating brand without the rating rules.** SSAs and VRAs use a rating-like scale and the Ratings division name, but each release disclaims them as ratings. *Inference:* that avoids NRSRO and EU CRA obligations while still lending the brand's credibility. Clients may not read the difference.
4. **The volumes quoted are partners' numbers.** "Over $1 trillion traded daily in linked exposures" describes the S&P 500 ecosystem, not the perpetual. XYZ's $100B volume and $600B+ annualized run rate are XYZ's own figures for all its markets. Chainlink's "$25 trillion in transaction value" is Chainlink's.
5. **The calculation is now outsourced.** In the S&P Kaiko suite, Kaiko does "data sourcing and calculation". S&P DJI provides "licensing, distribution and benchmark administration". S&P owns part of Kaiko. The governance claim depends on administration controls the corpus does not describe.
6. **Two crypto index philosophies under one brand.** The S&P Kaiko suite includes bitcoin reference rates. The S&P Pantera index is pitched against "momentum or popular tokens (including meme coins or Bitcoin)". Both carry the S&P name.
7. **Rules on one side, licences on the other.** S&P DJI refused MegaCap IPO exceptions to protect "core index principles" (Jun 2026, [[spglobal-indices-benchmarks]]). Three months earlier it licensed the same index for leveraged perpetuals on a decentralised chain for non-US users. Both decisions can be defended, but they apply different appetites for risk to the same brand.

## 5. Strategic read (inference — not stated by S&P Global)

- **Entry by licence is cheap optionality.** Every product here except OpenZeppelin and the Kaiko stake is a licence or an opinion: low capital, undisclosed and probably small revenue, high signalling value. If tokenized markets scale, S&P is already the default benchmark and risk label. If they don't, little is lost except reputational exposure.
- **Ratings is becoming the digital-assets hub.** The DeFi group, SSAs, VRA, protocol ratings and now OpenZeppelin all sit under Ratings. Index tokenization sits in S&P DJI. *Inference:* the long game is a *risk layer for on-chain finance*, where smart-contract audit (OpenZeppelin) + stablecoin and vault scores + benchmark prices = a composite trust stamp. That also adds conflict questions, because a rater would own the auditor.
- **Kaiko echoes the CRISIL pattern.** S&P takes a stake in a specialist, co-brands it, and lets the specialist run the engine. This is how S&P has handled new geographies and data niches before (CRISIL in India; Lukka, then Kaiko, in crypto).
- **Same rail as Tradeweb, different layer.** Both firms invested in Digital Asset. Tradeweb runs repo and Treasury financing on Canton; S&P puts its iBoxx index there. *Inference:* if Canton becomes the institutional OTC rail, S&P's index licence and Tradeweb's execution meet again, as they did on Tradeweb's SEF for iBoxx TRS in 2021. Watch for a Tradeweb-executed trade on a tokenized S&P index.
- **The bank and asset-manager angle.** Janus Henderson (SPXA sub-advisor), JPMorgan (a Chainlink client per the release), Goldman and BlackRock appear only at the edges of this corpus. Whether the large incumbents adopt S&P-stamped tokens is the real test. See [[jpmc-hub]], [[goldman-hub]], [[blackrock-hub]].

## 6. Canon lenses

- **Innovator's dilemma** ([[canon-christensen-innovators-dilemma]]): S&P enters a low-end, unregulated market *with partners* rather than through its core products. That is the textbook way for an incumbent to hedge disruption without cannibalising itself.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Kaiko was a competing crypto-index provider. It is now co-brand, calculation agent and investee.
- **Lemons and certification** ([[canon-akerlof-market-for-lemons]]): stablecoins and vaults are a classic quality-uncertainty market. S&P sells the certificate. The certificate's value depends on the certifier not being captured, which the "not a rating" line and the OpenZeppelin ownership both complicate.
- **Antifragility and optionality** ([[canon-taleb-antifragile]]): many small, cheap bets with capped downside (licences, assessments) and uncapped upside if tokenization scales.
- **Normal accidents** ([[canon-perrow-normal-accidents]]): smart contracts, oracles, leveraged perpetuals and 24/7 venues make a tightly coupled system. An S&P-branded score inside an automated liquidation rule spreads S&P's errors at machine speed.

## 7. Practitioner counterpoint

- **For S&P:** institutions moving on-chain need the same risk tools they use off-chain. A familiar scale from a regulated rater is useful, even with caveats. Licensing the S&P 500 to a decentralised venue at least brings official data and governance to a market that would otherwise trade an unofficial clone.
- **Against:** offshore leveraged perpetuals are a reputational risk with little visible revenue. A depeg or an exploit at an S&P-assessed protocol would be front-page news. "Not a rating" will not protect the brand in that headline.
- **Both:** judge the strategy by what is *paid for*. Until S&P discloses licence or assessment revenue, treat the activity as option value plus marketing.

## 8. Open questions to track

1. **Revenue.** Does S&P ever break out digital-asset revenue (Ratings or Indices), or name it in earnings PDFs?
2. **OpenZeppelin close.** How will S&P handle conflicts when Ratings assesses protocols that OpenZeppelin audits?
3. **Perpetual volume.** What is the open interest in the S&P 500 perpetual on Hyperliquid, and does a US-regulated venue follow?
4. **Canton follow-through.** Is there a second Derivnex trade, a dealer beyond DRW and Marex, or a Tradeweb-executed trade on a tokenized S&P index?
5. **SSA regulation.** Do the GENIUS Act or EU MiCA push SSAs toward formal rating status, or force more disclaimers?
6. **Kaiko governance.** As S&P owns more of Kaiko, who governs the S&P Kaiko indices day to day?

**Links:** [[spglobal-hub]] · [[spglobal-indices-benchmarks]] (licensing model; the MegaCap contrast) · [[spglobal-ai-data-layer]] (the same *meet clients where they are* distribution logic) · [[spglobal-people]] (Clay, Le Pallec, Mounts, Drinkwater) · [[spglobal-outside-voices]] · [[tradeweb-tech-ai-data]] (Canton, on-chain repo, Tradeweb's frontier bets) · [[tradeweb-hub]] · [[jpmc-hub]] · [[goldman-hub]] · [[blackrock-hub]] · [[market-structure-24-5-trading]] (24/7 venues) · [[canon-christensen-innovators-dilemma]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-akerlof-market-for-lemons]] · [[canon-taleb-antifragile]] · [[canon-perrow-normal-accidents]]

---
### Rep
Three exercises with numbers from this note.

**(a) Vault growth.** S&P says vault deposits went from $1.5B (Sep 2024) to $10B (Sep 2026). Compute the annual growth rate. *(Answer: (10/1.5)^(1/2) − 1 ≈ **158%** a year.)* If a VRA earned an assumed 1bp a year on rated deposits, and S&P rated half the market, what is the revenue? *(Answer: $5B × 0.0001 = **$500k**.)* In two sentences, say why S&P would launch a product this small.

**(b) Stablecoin coverage.** Stablecoins were $301bn in Oct 2025 (Coingecko, per S&P). S&P says SSAs cover "more than 90 percent" of circulating stablecoins. How many dollars of stablecoins carry an S&P assessment? *(Answer: ≥ **$271bn**.)* USDT scores 4 (*constrained*). Explain why an S&P 4 on the largest coin could be good for S&P's credibility but awkward for a DeFi protocol that wires SSAs into its collateral rules via Chainlink.

**(c) The brand-risk trade.** Build a one-line expected-value comparison for the Hyperliquid licence. Assume licence revenue of $5M a year (an assumption; nothing is disclosed) against a 2% annual chance of a reputational event that costs S&P DJI 0.5% of its ~$1.8B revenue (S&P's TTM figure). *(Answer: expected cost = 0.02 × $9M = **$0.18M**; the licence looks positive.)* Now name two reasons this simple EV understates the downside: fat tails, and spillover to Ratings.

---
**Sources (S&P Global press/IR, accessed via `articles.jsonl` 2026-10-25; Tradeweb newsroom via its corpus):**
- [Lukka crypto indexing, 2020-12-03](https://press.spglobal.com/2020-12-03-S-P-Dow-Jones-Indices-Builds-Crypto-Indexing-Capabilities-with-Lukka)
- [Digital Market Indices, 2021-05-04](https://press.spglobal.com/2021-05-04-S-P-Dow-Jones-Indices-Launches-Cryptocurrency-Index-Series-Including-S-P-Bitcoin-Index)
- [Broad Digital Market Index, 2021-07-13](https://press.spglobal.com/2021-07-13-S-P-Dow-Jones-Indices-Launches-S-P-Cryptocurrency-Broad-Digital-Market-Index)
- [Ratings DeFi group, 2022-05-17](https://press.spglobal.com/2022-05-17-S-P-Global-Ratings-Establishes-Decentralized-Finance-DeFi-Group-Amidst-Heightened-Investor-Interest)
- [Stablecoin Stability Assessment, 2023-12-12](https://press.spglobal.com/2023-12-12-S-P-Global-Ratings-Launches-Stablecoin-Stability-Assessment)
- [Centrifuge S&P 500 tokenization, 2025-07-01](https://press.spglobal.com/2025-07-01-S-P-Dow-Jones-Indices-Collaborates-with-Centrifuge-to-Bring-the-S-P-500-Index-Onchain,-Expanding-Access-to-the-Worlds-Most-Widely-Recognized-Benchmark)
- [Digital Markets 50 / Dinari, 2025-10-07](https://press.spglobal.com/2025-10-07-S-P-Global-to-Launch-Innovative-Crypto-Ecosystem-Index,-a-New-Way-to-Combine-Cryptocurrencies-and-Crypto-Linked-Equities)
- [SSAs on-chain via Chainlink, 2025-10-14](https://press.spglobal.com/2025-10-14-S-P-Global-Ratings-and-Chainlink-Collaboration-Brings-S-Ps-Stablecoin-Stability-Assessments-On-Chain)
- [2025 CEO letter, published 2026](https://www.spglobal.com/en/annual-reports/2025/ceo-letter)
- [S&P 500 perpetual on Hyperliquid, 2026-03-18](https://press.spglobal.com/2026-03-18-S-P-Dow-Jones-Indices-Licenses-S-P-500-R-to-Trade-XYZ-for-Perpetual-Contracts-on-Hyperliquid)
- [S&P Pantera index, 2026-07-21](https://press.spglobal.com/2026-07-21-S-P-Dow-Jones-Indices-and-Pantera-Capital-Launch-New-Index-for-Digital-Assets)
- [S&P Kaiko Digital Asset Indices, 2026-09-01](https://press.spglobal.com/2026-09-01-S-P-Dow-Jones-Indices-and-Kaiko-Introduce-S-P-Kaiko-Digital-Asset-Indices)
- [Kaiko Series B-2 investment, 2026-09-14](https://press.spglobal.com/2026-09-14-S-P-Global-Leads-Strategic-Investment-in-Kaiko,-Deepening-Commitment-to-Digital-Assets-and-On-chain-Markets)
- [OpenZeppelin acquisition, 2026-09-17](https://investor.spglobal.com/news-releases/news-details/2026/SP-Global-Announces-Agreement-to-Acquire-OpenZeppelin/default.aspx)
- [Vault Risk Assessment, 2026-10-04](https://press.spglobal.com/2026-10-04-S-P-Global-Ratings-launches-Vault-Risk-Assessment-for-digital-asset-markets)
- [Tokenized iBoxx TRS on Canton, 2026-10-13](https://press.spglobal.com/2026-10-13-S-P-Dow-Jones-Indices-and-Kaiko-Enable-First-On-chain-OTC-Swap-Referencing-a-Tokenized-Benchmark,-Executed-by-DRW-and-Marex-on-Derivnex)
- Tradeweb corpus: [Digital Asset $355M raise, 2026-06-11](https://www.tradeweb.com/newsroom/media-center/in-the-news/digital-asset-raises-$355-million-to-accelerate-cantons-role-as-onchain-infrastructure-for-capital-markets/) · [DTCC tokenized collateral, 2026-07-15](https://www.tradeweb.com/newsroom/media-center/in-the-news/dtcc-turns-tokenization-into-reality-u.s.-trades-successfully-processed-using-dtc-tokenized-assets)
