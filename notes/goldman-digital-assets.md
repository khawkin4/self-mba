# Note · Goldman Sachs digital assets — from a crypto access desk to permissioned collateral plumbing, ending in giving away the rail

> Practitioner / strategy note · Maps to **Course 04** (Competitive Strategy — network adoption, why rails get mutualized, coopetition), **Course 10** (Entrepreneurship & Venture — incubating a platform inside a bank, then spinning it out), **Course 11** (Global Strategy, Macro & Responsible Business — stablecoin regulation, singleness of money, contagion), **E10** (Digital & AI Transformation for Leaders — pilots vs production, tokenization as plumbing) · Written 2026-10-25 · Part of [[goldman-hub]]; companions [[goldman-markets-platforms]], [[goldman-outside-voices]]; the venue-side mirror is [[tradeweb-tech-ai-data]] and [[tradeweb-outside-voices]]

- **Source:** `_ingest/raw/goldman/articles.jsonl`, the **15 digital-asset items** (Mar 2021 – Sep 2025), plus every other item that mentions crypto, blockchain or tokenization (Solomon Jan 2022, Covello Jun/Jul 2024, Cohen Sep 2025). Coverage caveats:
  - The Dec 2022 Top of Mind (*The Winter of Crypto's Discontents*) and its podcast are **redacted scrapes**: cover pull-quotes and chart captions only.
  - The *Stablecoin summer* page (Aug 20 2025) captured the Brooks/Eichengreen podcast, not the report.
  - *Blockchain + The Capital Markets* (Jun 2021) is an empty stub.
  - The GS DAP launch release, any DAP volume, the Digital Asset investment and Canton do **not** appear. Canton facts come from the Tradeweb study.

  **No shareholder letter (FY2019–FY2025) and neither Investor Day deck mentions crypto, blockchain or tokenization** (regex check of the corpus). All voices appear on Goldman's own channels.
- **Core claim:** Goldman's digital-asset story has three acts.
  - **2021:** a **crypto access desk** justified by "client demand, pure and simple": cash-settled CME futures and NDFs, because US banks couldn't trade the physical.
  - **2022, after Terra and FTX:** "digital assets" redefined as **tokenized traditional assets and digital money**, anchored in the 2021 EIB digital bond and pitched on settlement precision, risk reduction and efficiency.
  - **2024–25: permissioned collateral plumbing.** GS DAP is to be **spun out as "industry-owned"** with **Tradeweb as first strategic partner**, and BNY uses it for **mirror tokens of MMF shares** "as a form of collateral".

  Between Act 2 and Act 3 there are **18 months of near-silence** (Apr 2023 – Nov 2024), during which Goldman's own head of equity research lists blockchain among hyped technologies with "few—if any—real world applications". The end state is a bank that **mutualizes the ledger and keeps the trading, collateral and banking fees** around it. Its invited skeptics frame the open risks: Roubini's *BINO* (Blockchain In Name Only) critique of exactly this kind of permissioned chain, Gorton's warning that interoperability imports contagion, and Eichengreen's singleness-of-money objection to stablecoins.

---

## 1. Chronology

| Date | Event | Terms / numbers (as stated) |
|---|---|---|
| 2017–18 | GS explores digital custody and a crypto desk, then shelves both | Market was "almost exclusively retail led" (McDermott, 2021) |
| Early 2021 (described Jun 10 2021) | **EIB first digital bond**: GS co-leads with SocGen and Santander | €100mn, 2-year, public Ethereum, French law, no CSD or custodian; **T+1 vs the usual T+5**; debt and cash as ERC-20 tokens |
| 2021-03-03 (aired Mar 5) | **Crypto desk goes live**, "quite narrow initially": CME futures and NDFs; bitcoin content on Marquee | >300 client conversations; survey of ~300: 40% have exposure, 61% expect holdings to rise, 76% see BTC at $40–100k by year-end, 22% >$100k |
| 2021-05-24 | Top of Mind #98, *Crypto: A New Asset Class?* | NDFs cash-settled; CME BTC and ETH futures (ETH agency only); principal BTC futures next; synthetic BTC ETNs via European prime; lending, structured notes, wealth access. Apr 2020 → Apr 2021: BTC spot ~$300mn → ~$1.5bn/day; CME BTC futures ~$200mn → ~$2bn/day |
| 2022-01 | Solomon: CEOs ask about "technology, crypto" | Only CEO mention in the corpus |
| 2022-05-18 | McDermott after TerraUSD: "not to group all stable coins in the same bucket"; welcomes regulation "as a regulated bank" | EIB bond settled on-chain DvP against a *synthetic CBDC* (tokenized cash at the central bank); >87 countries exploring CBDCs |
| **2022-11-03** | **Datonomy** with MSCI and Coin Metrics: a GICS-style taxonomy for coins | MSCI is "owner and sole administrator"; sold as a data feed via developer.gs.com |
| 2022-12-13 | Top of Mind #114 (redacted): FTX, Luna, Celsius | Market cap down ~70% from May 2021 peak to below $900bn; BTC/ETH volumes down ~65%; DeFi TVL down ~80% to ~$42bn; "~$1.5tn" decline, ~$500bn hit to US investors |
| **2023-04-17** | **Visual Structuring** extends to crypto options (plus equities, metals) | Last digital-asset item for 19 months |
| 2024-06-27 / 07-16 | Covello (GS Research): blockchain is a failed hype cycle | — |
| **2024-11-18** | **GS DAP spin-out** planned into "an industry-owned distributed technology solution", subject to regulatory approval; **Tradeweb first strategic partner** | DAP "leverages solutions developed by Digital Asset"; no terms, no volumes |
| 2025-06-10 | IB Insights (Coupal, McDermott): the US regulatory pivot | Digital-asset M&A $15.8B (2024) vs $1B (2019), $6.4B YTD 2025; stablecoins ~$220bn, ~1% of US M2; BCG/Ripple: tokenized RWA $18.9tn by 2033 |
| 2025 (Jun or Jul) | *(context, [[tradeweb-outside-voices]])* **Goldman joins Digital Asset's $135M round**, co-led by Tradeweb and DRW | Stake undisclosed; the Tradeweb notes date the round Jun 24 or Jul 9 2025 |
| **2025-07-23** | **BNY × GS tokenized MMFs**: mirror tokens of MMF shares on GS DAP via BNY LiquidityDirect | BlackRock, BNY Dreyfus, Federated Hermes, Fidelity, GSAM; BNY keeps "the official books, records, and settlements" |
| Summer 2025 | **GENIUS Act** becomes law, the first federal stablecoin framework | Podcast recorded Jul 14, Jul 18, Aug 7; aired Sep 2 |
| *(context)* Aug 12 2025 | First on-chain UST financing on Canton, executed on Tradeweb ([[tradeweb-tech-ai-data]]) | Roles not disclosed |

## 2. The three acts, in Goldman's words

**Act 1 — access desk (2021).**
- The justification was "Client demand, pure and simple." Institutional demand showed "no signs of that abating", and "we've crossed the Rubicon in terms of institutional buy-in".
- The constraint was regulatory: for US banks, "the inability to trade the physical". The workaround was derivatives "where we cash settle, so we don't trade the physical."
- McDermott named the tail risk himself: "we're only one big fraud away from a very negative impact on the market".
- The house view was split. Pandl saw bitcoin as a macro asset akin to gold. Currie and Sprogis saw "a high likelihood that bitcoin will eventually lose its crown" to a more useful coin.

**Act 2 — redefinition (2021–23).**
- The EIB bond was "democratization in action", and Le Moine called it the "first proper validation of the use of this technology".
- After Terra, McDermott conceded crypto behaved as risk-on, "a little less than the inflationary hedge". He moved the frame from price to infrastructure: "It's not too grandiose to say digital assets will bring about a paradigm shift in the financial markets and beyond."
- Investment focus moved to "the blockchain infra". He was positive on public and private chains "with various safeguards".
- Datonomy (2022) and Visual Structuring for crypto (2023) are Marquee products, extending the dealer's data business ([[goldman-markets-platforms]]). In Darling's words, data services for digital assets are "a strategic focus and natural extension to our existing business".

**Act 3 — permissioned plumbing, given away (2024–25).**
- "We view permissioned distributed technologies as the next structural change to financial markets" (McDermott, Nov 2024).
- The spin-out rationale is "a new, standalone company independent of Goldman Sachs" to "provide the future runway for digital financial services".
- Tradeweb's Bruner: "a new wave of access, liquidity, and interoperability".
- By 2025 the strategy is "client-led tokenization activities to crypto-linked product offerings and blockchain investments", plus traditional banking to the sector. The DAP ambition is now "a fully mutualized, distributed technology solution".
- On MMF tokens: "would enable us to unlock their utility as a form of collateral and open up more seamless transferability in the future."

## 3. The silence, Apr 2023 – Nov 2024

From the Visual Structuring crypto release (Apr 17 2023) to the DAP spin-out (Nov 18 2024), the corpus holds **no Goldman digital-asset strategy statement at all**. That window covers *(context, not in the corpus)* the Gensler-era SEC enforcement wave, and SAB 121, which per McDermott's 2025 account put custodied crypto on custodians' balance sheets. The only digital-asset mentions in it come from Goldman's AI skeptic, Jim Covello:
- *Top of Mind*, Jun 2024: "virtual reality, the metaverse, and blockchain are prime examples of technologies that saw substantial spend but have few—if any—real world applications today."
- *Exchanges*, Jul 2024: "Blockchain was supposed to be a big technology."

Read with the regulation, the silence looks like a deliberate hold, not a retreat *(inference)*. The desk kept trading, and the corpus shows no unwind. The re-entry came after the Nov 2024 US election, with a structure (spin-out, partners) that lowers single-bank exposure. McDermott's 2025 account credits the change in tone directly: SAB 121 rescinded "to give a potential path for banks to facilitate custody", with SAB 122 "lowering the onerous regulatory capital requirements that stemmed from SAB 121".

## 4. Why give away the rail? The Tradeweb / Canton / Digital Asset link

| Layer | Who | Evidence |
|---|---|---|
| Ledger technology | **Digital Asset** (developer of Canton) | DAP "leverages solutions developed by Digital Asset" (2024, 2025 releases). Canton is never named on goldmansachs.com |
| Ledger capital | Digital Asset $135M round, **co-led by Tradeweb and DRW, with Goldman**, Citadel Securities, DTCC, Virtu ([[tradeweb-outside-voices]]) | 2025; GS stake undisclosed |
| Platform | **GS DAP**, built in-house, to be spun out "industry-owned" | Nov 2024; regulatory approval pending; no completion in the corpus |
| Execution / liquidity | **Tradeweb**, first DAP partner, bringing "trading and liquidity capabilities across the fixed income spectrum" | Tradeweb also runs Canton "firsts": UST financing (Aug 2025), tokenized-Gilt repo (Feb 2026), tokenized UST vs USDCx (Jul 2026) ([[tradeweb-tech-ai-data]]) |
| Cash / collateral asset | **BNY** mirror tokens of MMF shares; five fund managers | Jul 2025; BNY remains record-keeper |

**Strategic read** *(inference)*:
1. **A single-bank ledger can't win network adoption.** Competing dealers and clients won't onboard to a Goldman-owned rail that sees their positions. Mutualizing it follows the path of DTCC, SWIFT and, ironically, Tradeweb itself, whose dealer owners went from 46% to 17.3% at the 2019 IPO.
2. **Goldman keeps the fees that need a balance sheet or a franchise:** crypto-linked trading, collateral services, IB advice to the sector (M&A volumes up 16x 2019–24), and GSAM as one of the MMF issuers. This is the same mutualize-the-network, own-the-balance-sheet pattern as the CCP paper and the EU tape ([[goldman-markets-platforms]] §4).
3. **Goldman and Tradeweb are hedged with each other.** Goldman is a co-investor in the rail Tradeweb trades on. Tradeweb is the venue on Goldman's platform. Both appear in each other's "firsts". Tradeweb's tech note calls its own stance "rail-agnostic execution". Goldman's is rail-agnostic ownership.
4. **Mirror tokens are additive, not substitutive.** BNY keeps the books, so the token rides on existing transfer-agent infrastructure. That is good for adoption and weak evidence that DLT replaces anything yet.

## 5. The skeptics Goldman invited

| Voice | Date | Argument | Hits which part of the strategy |
|---|---|---|---|
| **Nouriel Roubini** (NYU) | May 2021 | Most enterprise DLT is "BINO", because experiments are "private, centralized and permissioned". "The idea that technology can resolve the question of trust is delusional." "Any treasurer who invests in something that falls 15% in value overnight will be fired." | Act 3 exactly: GS DAP is permissioned by design |
| **Alan Cohen** (ex-SEC, ex-GS compliance) | May 2021 | "the anonymity promised by some crypto assets will inevitably meet intense regulatory opposition" | Explains why the bank route is permissioned |
| **Dan Guido** (Trail of Bits) | May 2021 | "It's a wild west out there for developers building applications on the blockchain." | Smart-contract risk on public chains (the EIB bond ran on Ethereum) |
| **Jay Clayton** (ex-SEC) | Dec 2022 | "The collapse of FTX is firstly an age-old lesson that unregulated markets are dangerous." | Supports the regulated-bank moat |
| **Timothy Massad** (ex-CFTC) | Dec 2022 | "Saying that US crypto entities are well-regulated by state laws" equals pre-1929 blue-sky laws | Same |
| **Gary Gorton** (Yale) | Dec 2022 | Contagion was contained because "blockchain technology isn't currently interoperable with the real world… But that lack of interoperability will eventually change." | DAP, BNY MMF tokens and Tradeweb on Canton *are* the interoperability |
| **Barry Eichengreen** (Berkeley) | Sep 2025 | "So, what's at risk is what economists refer to as a singleness of money." "There is nothing like a deposit insurance fund for stablecoins." Treasury demand: "marginal is the right word here." | Stablecoins as the cash leg; MMF tokens are the bank-side alternative |
| **Brian Brooks** (ex-acting OCC) | Sep 2025 | GENIUS mirrors bank supervision: "There's just a sense that supervision equals safety." | Bull case for regulated issuers |
| **Jim Covello** (GS Research) | Jun–Jul 2024 | Blockchain as a failed hype cycle | The firm's own strategy, during its silence |

The bulls are also on the record: Novogratz in 2021 called crypto an "official asset class" and predicted that "Uniswap could become a bigger exchange than the CME or the NYSE". His forecast of a clear Gensler framework "within his first nine months" proved wrong.

## 6. The numbers, and what they don't prove

1. **The 2021 liquidity numbers are ratios of a boom.** CME BTC futures volume rose ~10x and spot ~5x in a year (Apr 2020 → Apr 2021) *(derived)*. TOM cites "almost 900%" CME growth in April. None of it tells you Goldman's share or revenue.
2. **Client surveys aren't demand.** About 300 respondents, self-selected from GS clients. The 76% who expected $40–100k was a range, not a forecast. Siewert said on air they "are not Goldman Sachs predictions".
3. **The winter numbers don't reconcile.** A ~70% fall to below $900bn implies a peak near $3tn and a ~$2.1tn decline *(derived)*, against the "~$1.5tn" decline in the same report. A ~$1.5tn decline to $900bn would be a ~62% fall *(derived)*. The redacted scrape hides which chart each figure belongs to.
4. **The forward market sizes are vendors'.** The $18.9tn tokenized-RWA figure is BCG/Ripple's (Ripple sells the rails). Goldman cites it approvingly but doesn't adopt it.
5. **There is no DAP volume, user count or revenue,** and no completion date for the spin-out. The BNY launch is "a first step", with the official record off-chain.
6. **Firsts are unsized.** The EIB bond was €100mn. No notional is given for the MMF tokens or for the Tradeweb Canton trades ([[tradeweb-tech-ai-data]] §4).
7. **Survivorship and selection.** Goldman published nothing during the 2023–24 drawdown in sentiment. The skeptics are framed inside Goldman's own research product, and the redacted 2022 interviews leave the regulators' full arguments unread.

## 7. Canon lenses

- **Platform adoption and neutrality** ([[canon-parker-platform-revolution]], [[canon-hagiu-wright-multi-sided-platforms]]): a rail owned by one participant faces a chicken-and-egg problem made worse by distrust. Spinning it out is the classic neutrality fix.
- **Coopetition** ([[canon-brandenburger-nalebuff-coopetition]]): Goldman, Tradeweb, BNY, Citadel Securities and DTCC cooperate on the ledger and compete on everything that runs over it.
- **Disruption** ([[canon-christensen-innovators-dilemma]]): permissioned DLT is incumbent-shaped *sustaining* technology. Roubini's BINO critique is the disruptor's reply: if it's permissioned, why is it a blockchain?
- **Contagion and coupling** ([[canon-perrow-normal-accidents]]): Gorton's point in systems terms. Atomic, 24/7 settlement tightens coupling, and tightly coupled systems with complex interactions fail in surprising ways.
- **Lemons** ([[canon-akerlof-market-for-lemons]]): Eichengreen's singleness of money is a lemons problem. If every dollar token must be inspected, private money trades at a discount (free-banking notes, the 2008 MMF that "broke the buck").
- **Betting under uncertainty** ([[canon-duke-thinking-in-bets]]): the 2021 desk was a small, cash-settled option on a contested asset, and the 2023–24 silence a refusal to add to a losing hand in a hostile regime.

## 8. Practitioner counterpoint

- **Bull:** the sequence is disciplined. Goldman entered narrowly (cash-settled, regulated venues), built reusable infrastructure (EIB, DAP), stayed quiet when the regime was hostile, and re-entered with partners when it turned. Collateral mobility is a real problem: MMF shares that move as collateral 24/7 save margin and funding at scale. And giving away the rail is the only way it gets adopted.
- **Skeptic:** five years in, the public evidence is one €100mn bond, a taxonomy owned by MSCI, an options pricer, a planned spin-out with no closing, and mirror tokens over BNY's legacy books. That is Roubini's BINO in practice: a permissioned database with a blockchain label, sold to the same incumbents. And the moment it works, Gorton's channel opens.
- **Synthesis:** score it on production metrics, not "firsts". Ask for DAP notional and participants after spin-out, the share of MMF-token collateral accepted by third parties, and whether DAP interoperates with Canton and DTCC's tokenization service. Treat each new partner announcement as an option, not a result.

## 9. Open questions to track

1. Does the GS DAP spin-out close? Who owns it, and does Goldman keep a stake or a board seat?
2. Do DAP and Canton converge, given that DAP already runs on Digital Asset technology and Goldman holds a Digital Asset stake?
3. Do BNY mirror tokens become *legal* records (on-chain transfer-agent books), and are they accepted as margin at a CCP?
4. Does Goldman issue or custody a bank stablecoin or deposit token under GENIUS, given Brooks's point that banks issue tokens to cut funding costs?
5. With SAB 121 gone, does Goldman add spot crypto custody or principal spot trading, and does any letter finally mention digital assets?
6. Does Tradeweb's fixed-income liquidity show up on DAP in a volume number?
7. Stress test: in the next crypto drawdown, do tokenized MMF or Treasury positions transmit losses (Gorton) or stay ring-fenced?

**Links:** [[goldman-hub]] · [[goldman-markets-platforms]] (Marquee products, the mutualize-or-own pattern) · [[goldman-outside-voices]] (the skeptics) · [[goldman-ai]] (Covello) · [[goldman-mission-forces]] · [[tradeweb-tech-ai-data]] (Canton chronology) · [[tradeweb-outside-voices]] (Digital Asset round) · [[tradeweb-mission-forces]] (T10 tokenization) · [[tradeweb-strategy-financials]] · [[wss-rates-macro]] (Treasuries as stablecoin reserves) · [[market-structure-24-5-trading]] (24/7 collateral) · [[canon-parker-platform-revolution]] · [[canon-brandenburger-nalebuff-coopetition]] · [[canon-christensen-innovators-dilemma]] · [[canon-perrow-normal-accidents]] · [[canon-akerlof-market-for-lemons]]

---
### Rep
Four short computations, then a decision.

**(a) Settlement risk.** The EIB bond was €100mn and settled T+1 instead of T+5. If counterparty exposure during settlement scales with days outstanding, by how much does T+1 cut exposure-days? *(Answer: from 5 × €100mn = €500mn-days to €100mn-days, **−80%**; T+0 would remove it entirely.)* Name one risk the faster cycle *adds*.

**(b) Reconcile the winter.** Top of Mind #114 says market cap fell ~70% to below $900bn, and also that it fell "~$1.5tn from its peak". Compute the peak implied by each statement. *(Answer: 900 / 0.30 ≈ **$3.0tn**, a $2.1tn fall; or 900 + 1,500 = **$2.4tn**, a 62.5% fall.)* Which would you check first, and where?

**(c) Stablecoins and Treasuries.** Stablecoins are ~$220bn, "roughly 1% of M2" (Jun 2025). What M2 does that imply? *(~$22tn.)* Eichengreen cites a $2tn stablecoin scenario against "some $30 trillion" of Treasuries. What share of Treasuries would reserves hold if fully backed one-for-one? *(2 / 30 ≈ **6.7%**.)* Is "marginal" fair?

**(d) The vendor forecast.** BCG/Ripple's chart runs from ~$0.6tn (2025) to $18.9tn (2033). *(The year pairing is inferred from jumbled chart text.)* Compute the implied CAGR. *(Answer: (18.9 / 0.6)^(1/8) − 1 = 31.5^0.125 − 1 ≈ **54% a year**.)* Compare it with the 16x rise in digital-asset M&A over 2019–24 *(≈74% a year, derived)* and say which is the better base rate.

**Decision:** as head of Digital Assets, write three sentences on whether Goldman should keep a **controlling** stake in spun-out DAP. Address Roubini's trust objection and Gorton's contagion objection explicitly.

---
**Sources:** [Crypto desk podcast, Mar 5 2021](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/03-05-2021-mathew-mcdermott) · [TOM #98 Crypto, May 24 2021](https://www.goldmansachs.com/insights/top-of-mind/crypto-a-new-asset-class) · [Crypto podcast, Jun 1 2021](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/06-01-2021-crypto-a-new-asset-class) · [EIB digital bond, Jun 10 2021](https://www.goldmansachs.com/insights/articles/from_briefings_10-june-2021) · [McDermott after Terra, May 18 2022](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/05-18-22-mathew-mcdermott) · [Datonomy, Nov 3 2022](https://www.goldmansachs.com/pressroom/press-releases/2022/introducing-datonomy-11-03-2022) · [TOM #114 Crypto winter, Dec 13 2022](https://www.goldmansachs.com/insights/top-of-mind/the-winter-of-cryptos-discontents) · [Visual Structuring crypto, Apr 17 2023](https://www.goldmansachs.com/pressroom/press-releases/2023/gs-expands-visual-structuring-into-equities-crypto-and-precious-metals) · [TOM Gen AI (Covello), Jun 27 2024](https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too-much-spend-too-little-benefit) · [GS DAP spin-out, Nov 18 2024](https://www.goldmansachs.com/pressroom/press-releases/2024/announcement-18-nov-2024) · [Digital asset adoption, Jun 10 2025](https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/why-digital-asset-adoption-is-accelerating) · [BNY tokenized MMFs, Jul 23 2025](https://www.goldmansachs.com/pressroom/press-releases/2025/bny-goldman-sachs-launch-tokenized-money-market-funds-solution) · [Stablecoins podcast, Sep 2 2025](https://www.goldmansachs.com/insights/goldman-sachs-exchanges/after-a-summer-of-stablecoins-whats-next) · [Digital Asset $135M (Tradeweb newsroom), Jul 9 2025](https://www.tradeweb.com/newsroom/media-center/in-the-news/digital-asset-raises-$135-million-to-accelerate-adoption-of-canton-network/)
