# Note · Kinexys and the deposit-token bet — JPM's answer to stablecoins is to keep the deposit and change the rail; it went from private ledgers to public chains in 18 months, at ~0.06% of its daily payment flow

> Payments / tokenization note · Maps to **Course 10** (Entrepreneurship & Venture — incumbent self-disruption, an internal startup), **Course 04** (Competitive Strategy — defending a deposit franchise), **E10** (Digital & AI Transformation), **Course 11** (regulation as market design: the GENIUS Act) · Written 2026-10-25 · Companion to [[jpmc-markets-venues]] and [[tradeweb-tech-ai-data]]

- **Source:** 53 JPMC payments, blockchain and tokenization items 2021–2026 (`_ingest/raw/jpmc/articles.jsonl`, topic `payments-blockchain`): the J.P. Morgan Payments newsroom, Kinexys insights, the Kinexys landing and "About" pages (accessed 2026-10-25), J.P. Morgan Global Research on stablecoins (2025-09-04), and the Farooq/Muriungi op-ed (2026-06-29). Also Dimon's letters AR2021 and AR2025, the 2025 Investor Day, the 4Q25 call and the AR2022–AR2025 CIB letters. **All volumes are JPM's own, self-reported and undefined (notional vs value).** Pages dated 2021–22 already say "Kinexys" because the site was renamed retroactively. At the time the unit was **Onyx**.
- **Core claim:** JPM's thesis is that institutions want **bank money on-chain**: a deposit with the bank's credit, regulation and ability to pay interest, moved on a blockchain rail. Stablecoins are the alternative it argues against. From 2019 to 2024 it built that on **private, permissioned ledgers** (JPM Coin, now Kinexys Digital Payments; Onyx Digital Assets; Liink). From 2025, under stablecoin pressure after the GENIUS Act, it moved to **public chains**: a Chainlink/Ondo cross-chain test (May 2025), the JPMD deposit token on Coinbase's **Base** (proof of concept Jun 2025, live Nov 2025), Galaxy commercial paper on **Solana** settled in USDC (Dec 2025), tokenized money-market funds on **Ethereum** (May 2026) and JPM Coin on Ethereum mainnet (Oct 2026). Reported volume grew from >$2B/day (Nov 2024) to ~$7B/day (May 2026). That is still about **0.06%** of the ~$10–12T a day JPM Payments moves. Dimon's own verdict: "We spent too much on it. It doesn't matter as much as you all think." The product is a hedge against deposit disintermediation more than a profit line.

---

## 1. Chronology

| Date | Milestone (JPM's description) | Chain / scale |
|---|---|---|
| 2015–17 | Blockchain Center of Excellence; Quorum (open-source, bank-built); Interbank Information Network (later Liink) | Private, permissioned (per "About" page) |
| 2019 | **JPM Coin** launched (later Kinexys Digital Payments) | Private ledger |
| 2020 | Blockchain units consolidated as **Onyx**; Onyx Digital Assets and intraday repo begin | Permissioned EVM chain |
| 2021 | Partior co-founded with DBS and Temasek; Siemens becomes the first blockchain deposit-account client; satellites test (2021-10-04) | Private |
| 2022-04-04 | Dimon (AR2021): "Decentralized finance and blockchain are real, new technologies that can be deployed in both public and private fashion, permissioned or not." Also: "we also use a blockchain to move tokenized U.S. dollar deposits with JPM Coin." | — |
| 2022-07-15 | Tokenized Collateral Network first trade; intraday repo >$300B processed | Private |
| 2022-11 | MAS Project Guardian: tokenized deposits used in an FX trade on **Polygon** (with DBS, SBI) | First public-chain pilot |
| 2023 | Programmable payments live (Siemens); euro added | Private |
| **2024-11-06** | **Onyx renamed Kinexys**; >$1.5T cumulative, >$2B/day; "payments transactions have grown by 10x year-over-year" | "Multichain" framing |
| 2024-11-12 | Digital Debt Service: City of Quincy ~$10M muni bond, DvP to a blockchain deposit account | "private and permissioned" |
| 2025-04-14 | GBP blockchain deposit accounts; first clients LSEG's SwapAgent and Trafigura | Private |
| 2025-05-17 | First settlement **beyond private chains**: Ondo tokenized Treasuries vs KDP cash, via Chainlink | Cross-chain test |
| 2025-05-19 | Investor Day. Farooq: "Kinexys is one of the largest and leading institutional blockchain platforms". Nearly $2T processed. Dimon: "We spent too much on it." | — |
| **2025-06-24** | **JPMD** proof of concept on **Base**: "This marks the first time Kinexys is leveraging a public blockchain" | Public L2 |
| 2025-07 | GENIUS Act signed (per Global Research, 2025-09-04) | Stablecoin yield ban |
| 2025-07-30 | JPMC–Coinbase consumer partnership (bank-to-wallet links, card funding) | Not Kinexys |
| 2025-10-31 | Kinexys Fund Flow first trade (JPMAM / Private Bank with Citco) | Private |
| **2025-11-12** | **JPM Coin (JPMD) live** for institutional clients on Base; B2C2, Coinbase and Mastercard in the pilot | First bank deposit token on a public chain (JPM's claim) |
| 2025-12-11 | J.P. Morgan arranges Galaxy Digital US commercial paper on **Solana**, settled in **USDC**; buyers Coinbase and Franklin Templeton | Markets (not Kinexys); a third-party stablecoin as the cash leg |
| 2026-01-13 | 4Q25 call: stablecoin yield and a "parallel" system called a risk; Treasury estimate of $6.6T deposits at risk raised by Schorr | — |
| 2026-04-06 | Dimon (AR2025): "We need to roll out our own blockchain technology and continually focus on what our customers want in a very detailed way." | — |
| 2026-04-28 | **Oli Harris** (ex-Goldman Digital Assets) becomes Head of Kinexys; Kara Kennedy becomes Global Head of Market Development | Commercialisation hire |
| 2026-05-14 | Kinexys underpins JPMAM tokenized money-market funds on **public Ethereum** | Public L1 |
| 2026-05-18 | Project Acacia (RBA): repo settled with a CBA deposit token and wholesale AUD CBDC; >$4T cumulative, ~$7B/day | Interoperability |
| 2026-06-29 | Blockchain deposit accounts reach **eight currencies** (adds AUD, HKD, JPY, RMB, SGD) | Private |
| 2026-08-05 | HBS case. Farooq: "If blockchain is going to disrupt traditional finance, we should own the disruption, rather than be disrupted by others." | — |
| **2026-10-19** | **JPM Coin live on Ethereum mainnet**, the "second public blockchain" | Public L1 |

## 2. The thesis in JPM's own words

| Claim | Verbatim (speaker, date) |
|---|---|
| Bank money on a public rail | "we are now bringing yield-bearing commercial bank money onto Base, one of the leading public blockchains." (Naveen Mallela, 2025-06-24) |
| Same deposit, new format | "The nature of the funds doesn’t change. It’s the same deposit in a different format." (JPM Insights, 2026-05-11) |
| The treasurer's question about stablecoins | "For a treasurer, that raises real questions: what credit risk am I taking on, how does this sit on my balance sheet" (2026-05-11) |
| Deposit tokens as collateral | "deposit tokens, like JPM Coin, can serve as collateral, giving counterparties confidence that is not available with other on-chain instruments today." (2026-05-11) |
| Both chain types | "Private and public chains solve distinct problems, and their value compounds when they share a common infrastructure layer" (2026-05-11) |
| Interoperability | "Together with our clients, we aim to move beyond the limitations of legacy technology and realize the promise of a multichain world," (Farooq, 2024-11-06) |
| Regulation: same activity, same rules | "Whether an asset is issued or traded on a blockchain does not change its economic function." And: "payments innovation becomes dangerous when it drifts into shadow banking" (Farooq and Muriungi, 2026-06-29) |
| The stablecoin threat (CFO) | "avoiding the creation of a parallel ecosystem that has all the same economic properties and risks without appropriate regulation." (Barnum, 4Q25 call) |
| Self-disruption | "we should own the disruption, rather than be disrupted by others." (Farooq, 2026-08-05) |
| Scale claim in the CIB letter | "we launched JPM Coin on a public blockchain, marking a new era in digital money" (Rohrbaugh and Petno, AR2025) |

## 3. Metrics as reported

| Measure | Value (record date) |
|---|---|
| Cumulative volume | >$1.5T (Nov 2024) → "nearly $2 trillion" (May 2025) → >$3T (Mar 2026) → >$4T (May 2026 onward) |
| Average daily volume | >$2B (Nov 2024) → >$5B (Mar–Apr 2026) → ~$7B (May 2026 onward) |
| Transaction growth | "10x year-over-year" (2024–25); "thirtyfold" since 2023 across blockchain platforms (AR2025 CIB letter) |
| Currencies | USD → EUR → GBP (2025) → eight (Jun 2026) |
| Intraday repo | >$300B by Jul 2022 |
| JPM Payments for scale | ~$10T a day (2025), "nearly $12 trillion" a day (AR2025 letter) |
| Context | US stablecoins $225B, projected $500–750B (Global Research, Sep 2025); tokenized real-world assets on public chains >$29B (Apr 2026, cited by JPM) |

**Derived:** ~$7B ÷ ~$11T ≈ **0.06%** of daily payment value.

## 4. What the claims don't prove

1. **Volumes are undefined and unaudited.** "Notional", "transactions" and "processed" are used interchangeably. The Kinexys landing page (accessed Oct 2026) still shows ">$3 trillion" next to ">$7 billion" daily, behind the press releases.
2. **The claim to be first on a public chain depends on what counts.** Project Guardian (2022) used Polygon. JPM counts Base (2025) as first, presumably treating Guardian as an experiment.
3. **Client wins are mostly one-corridor pilots.** Siemens, BMW, Mitsubishi, FirstRand, Arab Bank and KB Kookmin each describe one intragroup or one-corridor flow. No client discloses what share of its treasury runs on Kinexys.
4. **The Canton story conflicts.** One undated JPM-hosted article says JPM Coin launched on Base and Canton in 2025. The May 2026 piece says Canton is "planned". The Oct 2026 release calls Ethereum the "second" public chain. Treat Canton as not live.
5. **Revenue is never disclosed.** Neither Kinexys revenue nor its cost appears. Dimon's "spent too much" is the only cost signal.

## 5. Strategic read (inference — not JPMC's words)

- **This is a deposit-defence product.** Stablecoins that pay "rewards" pull deposits out of banks; the Treasury estimate on the 4Q25 call is $6.6T at risk. A deposit token that stays on JPM's balance sheet and can pay interest keeps the money inside, while GENIUS-regulated stablecoins can't pay yield. The op-ed's push against yield-like "rewards" protects that asymmetry. *(Inference.)*
- **The pivot to public chains was forced by distribution.** On private ledgers JPM could only reach its own clients. On Base and Ethereum it can meet crypto-native counterparties (Coinbase, B2C2) and tokenized funds. Using USDC for the Galaxy CP shows the market pulled JPM onto stablecoin rails first.
- **Kinexys is a classic internal venture with a new commercial boss.** It was a decade of R&D (Quorum, Liink, Onyx), then a rebrand (2024), an HBS case and awards (2026), and an outside commercial hire (Harris, 2026). The Investor Day aside about overspending suggests a management team that wants revenue, not milestones.
- **It links to the venue fight.** Tokenized repo and collateral (TCN, Acacia, HQLAx) compete with venue on-chain repo (Tradeweb's Canton pilots, [[tradeweb-tech-ai-data]]) and with DTCC's tokenization service. Whoever holds the cash leg (a bank deposit token, a stablecoin, or a CBDC) has leverage over settlement venues.

## 6. Canon lenses

- **Incumbent's dilemma** ([[canon-christensen-innovators-dilemma]]): stablecoins start as low-end, retail and crypto rails. JPM's response is classic: build a separate unit (Onyx/Kinexys), move upmarket, keep the core economics (the deposit). Christensen would ask whether the unit can cannibalise wire and correspondent revenue.
- **Owning the disruption** ([[canon-grove-only-the-paranoid-survive]]): Farooq's line is Grove's strategic inflection point turned into a mandate.
- **Lemons and trust** ([[canon-akerlof-market-for-lemons]]): JPM's pitch to treasurers is quality uncertainty. A dollar token's issuer, reserves and redeemability vary, and a bank deposit removes the doubt. Depegs (Fischer's point, [[jpmc-outside-voices]]) are the lemon risk.
- **Network effects** ([[canon-shapiro-varian-information-rules]]): a deposit token is worth more the more counterparties accept it. Mastercard's token network and Coinbase are distribution, and Canton and Ethereum are reach.

## 7. Practitioner counterpoint

- **For JPM:** institutions need credit-safe, regulated cash for tokenized assets. Deposit tokens can be collateral and earn interest. Eight currencies, programmable FX and 24/7 settlement solve real treasury problems (EBANX: from 24+ hours to minutes).
- **Against:** "You cannot send a tokenized deposit to someone who is outside of banking," (Ran Goldi, Fireblocks, on a JPM page). Stablecoins are open, deposit tokens are closed. JPM's own research expects slower stablecoin adoption ("it might be at a slower pace than what some might anticipate,", Teresa Ho). That also means less pressure to scale deposit tokens.
- **Synthesis:** for now the two coexist. Stablecoins serve the open, retail and crypto edge; deposit tokens serve bank-to-bank and treasury flows. The test is whether tokenized-asset settlement on public chains chooses one cash leg.

## 8. Open questions

1. Does JPM disclose Kinexys revenue or JPMD balances outstanding?
2. Does JPMD pay interest in production, and to whom?
3. Does Canton go live, and does Kinexys connect to DTCC's or Tradeweb's tokenized collateral networks?
4. Do other banks issue interoperable deposit tokens (CBA appears in Acacia), or does JPM remain alone?
5. Do regulators extend GENIUS-style yield bans to deposit tokens, or leave the asymmetry in place?

**Links:** [[jpmc-hub]] · [[jpmc-markets-venues]] · [[jpmc-capital-regulation]] · [[jpmc-outside-voices]] · [[jpmc-mission-forces]] · [[tradeweb-tech-ai-data]] · [[tradeweb-rates-em]] · [[ice-hub]] · [[lseg-hub]] · [[blackrock-hub]] · [[goldman-hub]] · [[canon-christensen-innovators-dilemma]] · [[canon-grove-only-the-paranoid-survive]] · [[canon-akerlof-market-for-lemons]] · [[canon-shapiro-varian-information-rules]]

---
### Rep
Using only §3: (a) Compute Kinexys's daily volume as a share of JPM's daily payments at $10T and at $12T. (b) If daily volume grows from $2B (Nov 2024) to $7B (May 2026), what is the implied annual growth rate, and how many years at that rate to reach 1% of $12T a day? (c) Write a 120-word memo to JPM's CFO arguing for or against disclosing Kinexys revenue at the 2027 Investor Day.

*Answers:* (a) $7B / $10T = 0.07%; $7B / $12T ≈ 0.058%. (b) That is 3.5× in 1.5 years, ≈ **130% a year**. 1% of $12T is $120B a day, ~17× $7B: ln 17 / ln 2.3 ≈ **3.4 years** if that growth held, which it rarely does.

**Sources:** [Blockchain asset tokenization, 2022-07-15](https://www.jpmorgan.com/insights/payments/blockchain-digital-assets/blockchain-kinexys-asset-tokenization) · [Institutional DeFi (Guardian), 2022-11-24](https://www.jpmorgan.com/insights/payments/blockchain-digital-assets/institutional-defi) · [Introducing Kinexys, 2024-11-07](https://www.jpmorgan.com/insights/payments/blockchain-digital-assets/introducing-kinexys) · [Quincy muni bond, 2024-11-12](https://www.jpmorganchase.com/about/technology/blog/first-live-municipal-blockchain-based-bond-issuance-in-US) · [GBP BDAs, 2025-04-14](https://www.jpmorgan.com/payments/newsroom/gbp-blockchain-deposit-accounts-kinexys) · [Chainlink/Ondo cross-chain, 2025-05-17](https://www.jpmorgan.com/payments/newsroom/kinexys-chainlink-ondo-tokenized-asset-test) · [JPMD on Base pilot, 2025-06-24](https://www.jpmorgan.com/payments/newsroom/kinexys-usd-digital-deposit-tokens) · [Stablecoin primer, 2025-09-04](https://www.jpmorgan.com/insights/global-research/currencies/stablecoins) · [JPMD live, 2025-11-12](https://www.jpmorgan.com/payments/newsroom/jpm-coin-usd-deposit-token-institutional-clients) · [Solana CP, 2025-12-11](https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-commercial-paper-issuance-solana-blockchain) · [Kinexys 2026 milestones, 2026-04-28](https://www.jpmorgan.com/payments/newsroom/kinexys-milestones-2026) · [Public and private chains, 2026-05-11](https://www.jpmorgan.com/insights/payments/blockchain-digital-assets/kinexys-powers-finance-public-private) · [Tokenized MMFs, 2026-05-14](https://www.jpmorgan.com/payments/newsroom/kinexys-tokenized-money-market-funds) · [Project Acacia, 2026-05-18](https://www.jpmorgan.com/payments/newsroom/kinexys-project-acacia-tokenization-trial-australia) · [Farooq/Muriungi op-ed, 2026-06-29](https://www.jpmorganchase.com/newsroom/from-the-desk-of/getting-the-framework-right-for-digital-assets-in-the-us) · [APAC BDAs, 2026-06-29](https://www.jpmorgan.com/payments/newsroom/kinexys-apac-blockchain-deposit-accounts) · [HBS case, 2026-08-05](https://www.jpmorgan.com/payments/newsroom/harvard-business-school-case-study-kinexys) · [JPM Coin on Ethereum, 2026-10-19](https://www.jpmorgan.com/payments/newsroom/jpm-coin-live-on-ethereum) · [About Kinexys (accessed 2026-10-25)](https://www.jpmorgan.com/kinexys/about) · [Stablecoins and deposit tokens (undated)](https://www.jpmorgan.com/payments/payments-unbound/magazine/articles/stablecoins-deposit-tokens-reshaping-payments)
