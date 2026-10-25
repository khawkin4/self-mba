# JPMorgan Chase — read-first digest (market-structure lens)

Stage: **read, don't note yet.** This digest covers what was collected and read, what it says, and which notes would earn a place in `notes/`. Built 2026-10-25 in parallel with eight sibling company studies. Format follows the Tradeweb study (`notes/tradeweb-*`, `_ingest/raw/tradeweb/`).

Files in this folder:
- `index.tsv`: 165 in-scope records (date, type, topic, title, url, words).
- `articles.jsonl`: full texts, one JSON object per line (`date, type, topic, title, url, text`). Shareholder letters are their own records.
- `DIGEST.md`: this file.

Quote convention: anything in double quotation marks is verbatim from `articles.jsonl` (or, where marked [TW], from `_ingest/raw/tradeweb/articles-2019-2026.jsonl`). Every quote was checked by script; see §9. Dates are publication dates. *AR2023 letter* means the letter in the 2023 Annual Report, published April 2024.

---

## 1. What the corpus is

**Size: 165 records, ~527,000 words.**

| Type | Records | Words (approx.) | Notes |
|---|---|---|---|
| Dimon shareholder letters, AR2019–AR2025 | 7 | 193k | Read in full. Published Apr 2020 → Apr 2026 |
| Line-of-business CEO letters, AR2019–AR2025 | 7 | 82k | CIB (Pinto → Piepszak/Rohrbaugh → Rohrbaugh/Petno), CCB, CB, AWM, and the COO letter from AR2024 |
| Earnings call transcripts | 10 | 116k | 4Q19, 4Q20, 4Q21, 4Q22, 1Q23 (bank failures), 4Q23, 4Q24, 4Q25, 2Q26, 3Q26 |
| 2025 Investor Day full transcript | 1 | 37k | The only Investor Day transcript JPMC still hosts (2019–2024 PDFs are offline) |
| Newsroom, IR, J.P. Morgan Payments/Kinexys, Markets, Technology, Insights web items | 140 | 92k | 2019-02 → 2026-10-19 |

**Unfiltered universe (what the filter worked from):**
- jpmorganchase.com sitemap: 2,264 URLs. Of these, 481 are press releases (306 since 2019) and 388 are newsroom stories. There are also 13 "From the desk of" op-eds, 594 IR news items since 2013 (307 since 2019) and 124 technology pages. The newsroom listing API reports **468 press releases** in total.
- jpmorgan.com US sitemap: 3,131 URLs. Of these, 111 are Payments newsroom items, 105 corporate news items and 71 technology news items. The rest are Insights sub-sections, Kinexys pages and Markets pages.
- Candidate set fetched: about 1,500 pages. 442 passed a keyword score. **140 were kept** after a hand pass on titles, plus 25 IR documents (letters, transcripts, Investor Day).

**Filter applied (kept):** CIB markets, meaning FICC and equities, e-trading, market-making and JPM's own platforms (Execute, Aqua/JPM-X, DataQuery, Fusion). Also kept: Treasury clearing; payments, blockchain and tokenization (Onyx/Kinexys, JPM Coin/JPMD, stablecoins, Solana CP, Coinbase); AI and technology spend; data; and regulation (stress tests, SCB, Basel III endgame, G-SIB, SLR, open banking, EU equity market structure). Strategy items kept: leadership and succession, First Republic, Apple Card, the $1.5T Security & Resiliency Initiative (SRI), the Trump-lawsuit statement and the "From the desk of" op-eds.

**Skipped (by rule):** consumer product launches, branch openings, philanthropy and community commitments (AdvancingCities, housing, racial equity, workforce), reading lists, recruiting and engineer-culture posts (DEVUP, Ignite), awards-only posts, conference recaps without substance, and most quantum-research posts (four kept as technology-identity signals). Also skipped: card and merchant "tokenization" (a security term, not blockchain), Payments quarterly earnings-highlights pages, dividend, preferred and redemption notices, and *to host / to present at* notices. J.P. Morgan Global Research outlook pieces were skipped except three on AI and stablecoins. That keeps the corpus clear of `notes/jpm-software-sector-spotlight-2026.md`, which is already a research note.

**Gaps and what was blocked:**
- **Nothing was blocked.** jpmorganchase.com and jpmorgan.com answer `curl`, and the sitemaps and the dynamic-grid JSON were enough. The built-in browser was used once, to find the quarterly-earnings JSON endpoint.
- **Investor Day 2019–2024 transcripts are no longer hosted.** The IR notices remain but carry dates only. Only 2025 is available.
- **Earnings releases were not scraped.** Ten of the 31 transcripts available (2019–2026) were taken: each year's Q4 plus 1Q23, 2Q26 and 3Q26.
- **Several events are not on JPMC's own sites:** the original JPM Coin launch (Feb 2019), the Onyx launch (Oct 2020), the May 2021 CCB succession (Smith → Lake/Piepszak) and the 2021 Barnum CFO appointment. They are reconstructed here from the letters and from Kinexys' "About" page.
- **About 35 of the 140 web records are thin** (notice-only, boilerplate, or Markets pages whose pull-quotes the scraper dropped). They stay in the index so the timeline is complete. The thin ones are all IR "Investor Day" and DFAST notices, the 2022-04-13 results page, the 2025-09-19 podcast page and the 2026-07-31 *How are trading platforms evolving?* page.
- **No outside press.** The only outside voices are those JPMC quotes (clients, partners, Risk magazine, Evident), analysts on the calls, and the JPM mentions in the existing Tradeweb corpus.
- **Venue names are almost absent from JPMC's own corpus.** Tradeweb, MarketAxess and Trumid appear **zero** times in 165 records. CME and ICE appear only in the Treasury-clearing explainer, plus one CME aside on a call. This absence is a finding in itself; see §8.

---

## 2. Chronology — 36 events that matter for the lens

| Date | Event | Why it matters |
|---|---|---|
| 2019 (Feb) | JPM Coin launched on a private ledger (later "Kinexys Digital Payments") | First bank-issued deposit token. Not on JPMC sites; dated from the Kinexys "About" page and the AR2025 CIB letter ("launched in 2019") |
| 2019-04-03 | Tradeweb IPO; J.P. Morgan is a joint lead bookrunner [TW] | Founding dealer-owner becomes underwriter while banks sell down. JPM also co-led both follow-ons (Oct 2019, Apr 2020) |
| 2019-04-17 | Piepszak named CFO; Lake moves to CEO of Consumer Lending | First rotation in the bench that produces the 2026 co-presidents |
| 2020-03-05 | Dimon has emergency heart surgery; Board asks Co-Presidents Pinto and Smith to run the firm | Key-person risk becomes real; interim leadership is publicly tested |
| 2020-04-06 | AR2019 letter (COVID): "we will not request any regulatory relief for ourselves." | Sets the "port in the storm" identity used for the next six years |
| 2020-06-29 | First Stress Capital Buffer, 3.3%; buybacks halted under the Fed directive | Start of the capital-rules fight that runs through 2026 |
| 2020 (Oct) | Blockchain units consolidated as **Onyx**; Onyx Digital Assets / intraday repo begin | Institutional on-chain repo starts here; >$300B processed by Jul 2022 |
| 2021-01-15 | 4Q20 call: Dimon, "brutal competition"; investment spend from ~$10B to ~$12.5B | Fintech and Big Tech framed as an existential threat; first sustained analyst pushback on returns (Mayo) |
| 2021-04-07 | AR2020 letter: Treasury repo dislocations "certainly linked" to LCR, SLR and G-SIB "red lines" | Dimon's core market-structure argument: regulation stops dealers from intermediating |
| 2021 (May) | Lake and Piepszak become CCB co-CEOs; Gordon Smith retires; Barnum becomes CFO | Second rotation. No press release on JPMC sites |
| 2021-07-08 | First fully electronic SOFR swap-spread trade on Tradeweb, JPM vs BlackRock; quote from JPM's Thomas Pluta [TW] | JPM as launch dealer on Tradeweb protocols |
| 2022-01-14 | 4Q21 call: 2022 expense guide +$6B, 17% ROTCE "not realistic for 2022"; stock falls | Peak of the investment-versus-returns argument |
| 2022-04-04 | AR2021 letter: "moats... not particularly deep"; JPM Coin and Liink; investment spend from $11.5B to $15B | First letter with tech dollar figures; blockchain called "real" |
| 2022-05-10 | Fusion by J.P. Morgan (buy-side data platform) launched | JPM moves into data and analytics, its own version of the venue-data business |
| 2022-07-13 | JPM's Thomas Pluta named Tradeweb's next President (in office Jan 2023 to Sep 2024) [TW] | Revolving door between JPM and Tradeweb |
| 2022-11 | MAS Project Guardian: tokenized deposits on public Polygon (with DBS, SBI) | First public-chain experiment; JPM later counts Base (2025) as its "first" public-chain use |
| 2023-04-04 | AR2022 letter: Basel III endgame, "we will simply have to adjust"; 300+ AI use cases; ChatGPT named | Acquiescent stance on capital, a year before the reversal |
| 2023-05-01 | JPM acquires First Republic from the FDIC | Consolidation under regulator pressure; capital and integration load |
| 2024-01-25 | Commercial Banking merged with CIB into the Commercial & Investment Bank; Piepszak and Rohrbaugh named co-CEOs; new Markets trading heads | Wholesale franchise restructured around client coverage and payments |
| 2024-04-08 | AR2023 letter: Basel endgame "+25%" capital, "+50%" for market-making; new section on protecting market-making; 400+ AI use cases; Chief Data & Analytics Officer (Heitsenrether) joins the Operating Committee | Endgame fight becomes a defence of the dealer balance sheet |
| 2024-06-27 | JPM publicly disputes the Fed's stress-test treatment of OCI; puts excess capital at ~$54B | Rare public challenge to a supervisor |
| 2024 (summer) | LLM Suite released to employees | Firmwide model-agnostic generative AI platform, built in-house |
| 2024-11-06 | Onyx renamed **Kinexys**; >$1.5T cumulative, >$2B/day | "Multichain" framing begins |
| 2025-01-14 | Pinto to retire end-2026 (Vice Chairman); Piepszak named COO over tech, data and ops; Petno joins Rohrbaugh as CIB co-CEO | Technology, data and AI now report to the COO; Pinto's successors take the CIB |
| 2025-04-07 | AR2024 letter: primary-dealer restrictions will mean "much higher volatility in the treasury markets"; "I underestimated the importance of cloud technology"; AI is nearly absent (3 mentions, versus 22 the year before) | AI detail moves to the new COO letter, which reports LLM Suite at 200k+ users and 10–20% coding productivity |
| 2025-05-19 | Investor Day: Markets fee pool "won't go back" to pre-COVID; cost per trade down 42% in Rates and 23% in Cash Equities since 2019; ~$18B tech spend; Dimon on blockchain: "We spent too much on it." | Clearest single statement of JPM's markets strategy |
| 2025-06-24 | JPMD deposit-token proof of concept on **Base** (Coinbase L2) | Pivot to public chains |
| 2025-10-09 | J.P. Morgan is the **first dealer** to host its U.S. Treasury algos on Tradeweb [TW] | JPM uses the venue as a distribution channel for its own execution |
| 2025-10-13 | $1.5T, 10-year SRI announced; Evident AI Index #1 for the fourth year | Capital redeployment and national-security positioning |
| 2025-11-12 | JPM Coin (JPMD) live for institutional clients on Base | First bank deposit token on a public chain |
| 2025-12-11 | JPM arranges Galaxy Digital commercial paper on **Solana**, settled in USDC | Markets (not Kinexys) uses a stablecoin rail where clients are |
| 2025-12-19 | Treasury clearing explainer: FICC and CME approved, ICE seeking approval; cash clearing Dec 31 2026, repo Jun 30 2027 | JPM's view of the biggest Treasury market-structure change |
| 2026-01-13 | 4Q25 call: 2026 expense ~$105B; stablecoin yield described as a "parallel ecosystem" risk; NBFI exposure ~$160B | Deposit-franchise defence becomes explicit |
| 2026-04-06 | AR2025 letter: names Block, **Citadel Securities**, Revolut and Stripe; "We need to roll out our own blockchain technology"; G-SIB surcharge "un-American"; AI "not a speculative bubble"; 2026 tech budget ~$19.8B (COO letter) | The competitor map now includes market makers and blockchain-native firms |
| 2026-06-25 | **Petno and Rohrbaugh named Co-Presidents**; Petno sole CIB CEO; Rohrbaugh (a trader) takes over CCB; Lake retires | Succession made visible. Dimon says the timetable is unchanged |
| 2026-07-31 | J.P. Morgan e-Trading Survey (10th edition): technology (22%) overtakes liquidity (21%) as traders' top concern for the first time; electronic share expected 60% → 70% by 2027 | The dealer's own read on electronification |
| 2026-10-13 | 3Q26 call: AI spend ~$700M a year with benefits "aren't observable"; buybacks cut to ~$1B; CET1 13.9% | The AI story is reined in; capital goes to organic deployment |
| 2026-10-19 | JPM Coin goes live on Ethereum mainnet (second public chain); Kinexys >$4T cumulative, ~$7B/day | Latest item in the corpus |

Context from sibling studies, not from the JPMC corpus: ICE agreed to buy MarketAxess on 2026-07-30, with **J.P. Morgan advising MarketAxess** (read-ice notes). Tradeweb agreed to buy Trumid on 2026-10-19 (Tradeweb corpus).

---

## 3. People

### Who leads (as of 2026-10)

| Role | Person | Path in the corpus |
|---|---|---|
| Chairman & CEO | Jamie Dimon | Since 2005/06. Heart surgery Mar 2020. "Several years... plus or minus" (2Q26) |
| Co-President; CEO, Commercial & Investment Bank | Doug Petno | CEO Commercial Banking (2019–23) → Co-Head Global Banking (2024) → CIB co-CEO (Jan 2025) → Co-President (Jun 2026) |
| Co-President; CEO, Consumer & Community Banking | Troy Rohrbaugh | Co-head Markets & Securities Services → CIB co-CEO (Jan 2024) → Co-President and CCB CEO (Jun 2026). Barnum: he "was actually an options trader" |
| COO (technology, ops, data & analytics, strategy) | Jennifer Piepszak | CEO Card → CFO (2019) → CCB co-CEO (2021) → CIB co-CEO (2024) → COO (Jan 2025). Dimon: she "does not want to be the CEO" |
| CFO | Jeremy Barnum | CFO since 2021; carries the AI, regulation and capital narrative on calls and at Investor Day |
| CEO, Asset & Wealth Management | Mary Callahan Erdoes | Unchanged throughout |
| Vice Chairman (retiring end-2026) | Daniel Pinto | CIB CEO 2012–2023; Co-President/President & COO 2018–2025 |
| Retired 2026 | Marianne Lake | CFO → Consumer Lending → CCB co-CEO → sole CCB CEO (2024) → left when the co-president plan was made |
| Technology and AI | Lori Beer (Global CIO), Teresa Heitsenrether (Chief Data & Analytics Officer, OpCo since 2023), Derek Waldron (Chief Analytics Officer, LLM Suite), Pat Opet (CISO) | |
| Payments and Kinexys | Umar Farooq and Max Neukirchen (Global Co-Heads of Payments); Naveen Mallela and Kara Kennedy (Kinexys); Oli Harris (Head of Kinexys from Apr 2026, ex-Goldman) | |
| Markets voices | Jason Sippel and Pranav Thakur (Markets trading co-heads 2024); Rachid Alaoui (Equities); Kate Finlayson (FICC market structure); Andrew Cole (Execute); Peter Grant (systematic credit); Liyan Yu (rates automated trading) [TW]; Scott Lucas (Markets digital assets) | |
| Strategic investing | Todd Combs (ex-Berkshire/GEICO; heads the SRI Strategic Investment Group from Jan 2026) | |

### The succession arc
In short: the bench was built by repeated rotations, the date is never named, and the "intent" language is deliberately soft.
- **2020-03-05.** After Dimon's surgery the Board asked "Daniel and Gordon to lead the company during this period". This was the first real test.
- **AR2022 letter (2023-04-04).** This is the only letter with a succession paragraph: "we have multiple successor candidates who are well-known to the board and to the investor community." The AR2023–AR2025 letters say nothing on succession.
- **4Q24 call (2025-01-15).** Dimon gives "four, five years or more". He also says "I think it's wonderful that Jenn Piepszak, who does not want to be the CEO, will be here as Chief Operating Officer".
- **Investor Day (2025-05-19).** "the Board has intent. It's not a promise, it's not a commitment, it's intent". Dimon also floats "four more years and maybe two more" as executive chair.
- **2026-06-25 release.** "The changes announced today mark an important step in our Board’s thoughtful process around succession planning and development of our top leaders"
- **2Q26 call (2026-07-14).** "the Board made a decision to go ahead with making two Co-Presidents, which will be preparing them to do far more at the company". On timing: "Exactly what we said last time. Whatever I said last time, the timetable is essentially the same." Dimon lists the traits he wants: analytics, EQ, "culture carrier", heart, grit. He defends moving a trader into Consumer as cross-firm experience.
- **Inference.** The design gives two candidates each a large business with the other's background: banker Petno runs the wholesale bank and trader Rohrbaugh runs the retail bank. This is the classic horse race. Lake's exit is the cost, admitted plainly ("No mystery.").

### Signature views, dated, and how they shifted

**Dimon on competition: threat → named rivals → market makers and blockchain**
- 2021-04-07 (AR2020): "banks are playing an increasingly smaller role in the financial system."
- 2021-01-15 (4Q20 call): "I expect it to be very, very tough, brutal competition in the next 10 years. I expect to win, so help me God."
- 2022-04-04 (AR2021): "the moats that protect this company are not particularly deep — and we face extraordinary competition."
- 2023-04-04 onward (AR2022–AR2025) the same sentence reads "walls... not particularly high". The metaphor changed but the admission did not.
- 2023-04-04 (AR2022): "many of the new “shadow bank” market makers are fair-weather friends —they do not step in to help clients in tough times."
- 2026-04-06 (AR2025): "The most successful examples of these are Block, Citadel Securities, Revolut and Stripe."
- **Shift:** in 2020–21 the threat is Big Tech and Walmart, met with payments rails and cloud. By 2026 a market maker (Citadel Securities) and blockchain-native rivals are named, and JPM must "roll out our own blockchain technology".

**Dimon on regulation and the dealer balance sheet: no relief → red lines → adjust → fight → "un-American"**
- 2021-04-07: "Over the past two years, we saw significant dislocation in the U.S. Treasury (UST) repo markets, which were certainly linked to these regulations."
- 2021-04-07: "if large players cannot intermediate in markets because of regulatory requirements, the Fed will have to do it"
- 2023-04-04, on Basel endgame: "we will simply have to adjust to them immediately."
- 2024-04-08: "it would increase our firm’s required capital by 25%, making our requirement 30% higher than it would be under the equivalent European Union proposal."
- 2024-04-08: "Some regulators seem to think that market making is a speculative, hedge fund-like activity"
- 2025-04-07: "the restrictions put on market making by primary dealers – will likely lead to much higher volatility in the treasury markets."
- 2026-04-06, on the G-SIB surcharge at ~5.0%: "Frankly, it’s not right, and it’s un-American." He calls the 2026 re-proposals "mixed" and says liquidity rules are the next fight.
- Barnum at Investor Day 2025: "SLR should clearly be fixed, it's a low-hanging fruit, it should be done, and it will certainly bring some benefits somewhere."
- **Shift:** the argument stays the same (capital and liquidity rules push intermediation out of banks and make Treasuries fragile). The posture moves from compliance (2023) to open opposition (2024) to a qualified win (2026).

**AI and technology spend: "spend anything" → use-case counts → "aren't observable"**
- 2021-01-15 (4Q20): "The cloud is real. The cost is real. The speed is real. The security is real. The AI is real. The machine learning is real."
- Mayo's reply on the same call: "spending is certain. Returns are uncertain."
- 2022-01-14 (4Q21), Barnum: "it's impossible to prove, in some narrow financial sense, that there's a tangible return payback from that"
- 2023-04-04: "We already have more than 300 AI use cases in production today for risk, prospecting, marketing, customer experience and fraud prevention"
- 2024-01-12 (4Q23), Barnum: "We're not going to be chasing shiny objects here in AI."
- 2024-04-08: "we are completely convinced the consequences will be extraordinary and possibly as transformational as some of the major technological inventions"
- 2025-04-07 (AR2024, Dimon): AI barely appears, and he admits "I underestimated the importance of cloud technology". The COO letter carries the detail: "We are a technology-driven company as much as we are a bank, and technology is fundamental to everything that we do."
- 2026-04-06: "Overall, the investment in AI is not a speculative bubble; rather, it will deliver significant benefits." Also: "AI will definitely eliminate some jobs, while it enhances others."
- 2026-07-14 (2Q26): "we have had discrete areas where we did reduce jobs by 30% or 40%. And most of those people were offered jobs elsewhere."
- 2026-10-13 (3Q26), Barnum: "the benefits aren't observable in our current quarterly earnings." AI expense is "something like $700 million annually" against a 2026 tech budget of ~$19.8B.
- Numbers trail:
  - Tech budget: ~$12B (2019/2022), $15B investment spend (2022), ~$17B (2024), ~$18B (2025), ~$19.8B (2026 budget).
  - AI use cases: 300+ (2023), 400+ (2024), 500+ (mid-2025), "almost 1,000... the really important ones are 50" (2026).
  - LLM Suite: 0 → 200k users in 8 months.
  - CIB: 175+ use cases; 65k CIB staff on LLM Suite; KYC unit cost down ~40%.
- **Shift:** from unbounded conviction (2021) to disciplined use cases (2023–24) to scale claims (2025) to a deliberately modest, unquantified payoff story (late 2026), while jobs language moves from "augment" to 30–40% cuts in discrete areas.

**Markets: the trading strategy in their own words**
- Pinto, AR2019: "our steadfast pursuit of three strategic goals: being global, complete and at scale."
- Dimon, 4Q20: "we kept our share while things were electronified and digitized"
- Pinto, AR2021: "More and more, participants in trading markets are using digital portals and electronic trading strategies."
- Pinto, AR2022: "the capital required to fuel our global trading desks has risen significantly over the last five years."
- Piepszak and Rohrbaugh, AR2023: "J.P. Morgan launched a new algorithmic trading offering to U.S. Treasury investors to capture share in the world’s most important bond market."
- Petno, Investor Day 2025: "as our overall trading volumes have nearly tripled since 2019, we've seen significant reductions in our cost per trade."
- Rohrbaugh, Investor Day 2025: "I think the broad fee pool in Markets won't go back to those pre-COVID levels." Also: "So in Fixed Income it won't be easy, but I think we can gain share." He admits Rates underperformed.
- Rohrbaugh and Petno, AR2025: "AI became the battleground of competition and the defining market force."
- Dimon, 4Q25: "We have the best FICC business in the world, one of the best equity businesses in the world."
- **Shift:** the growth engine moved from FICC flow to **financing and Prime** (financing up 75% since 2019 at 17% share; Equities +86% in 2Q26, driven by Prime). Markets share is roughly flat at 11.4–11.8%, and Equities rose to co-#1 at 13.2% in 2025. FICC share is below pre-COVID. Electronification is presented as a cost-per-trade story, not a venue story.

**Blockchain and deposits: "real" → "spent too much" → "own the disruption"**
- 2022-04-04: "Decentralized finance and blockchain are real, new technologies that can be deployed in both public and private fashion, permissioned or not."
- Investor Day 2025, Dimon: "We spent too much on it. It doesn't matter as much as you all think."
- 2025-06-24, Mallela: "we are now bringing yield-bearing commercial bank money onto Base, one of the leading public blockchains."
- 2026-01-13 (4Q25), Barnum, on stablecoin rewards: "avoiding the creation of a parallel ecosystem that has all the same economic properties and risks without appropriate regulation."
- 2026-04-06: "We need to roll out our own blockchain technology and continually focus on what our customers want in a very detailed way."
- 2026-05-11, JPM Insights: "The nature of the funds doesn’t change. It’s the same deposit in a different format."
- 2026-08-05, Farooq: "If blockchain is going to disrupt traditional finance, we should own the disruption, rather than be disrupted by others."
- **Shift:** Dimon's own skepticism about the spend sits beside a business that moved from permissioned ledgers to public chains (Base, then Ethereum) in 18 months, driven by stablecoin competition after the GENIUS Act.

---

## 4. Mission and identity, as stated

- **Purpose** (introduced in the AR2022 letter and repeated by the COO): "Make dreams possible for everyone, everywhere, every day." Values: Service, Heart, Curiosity, Courage, Excellence.
- **Steadfast principles** (seven in AR2022, eight from AR2023): fortress balance sheet; "we are not a conglomerate"; the walls "not particularly high". The eighth, added in AR2023: "we must be a source of strength, particularly in tough times, for our clients and the countries in which we operate."
- **CIB identity:** "global, complete and at scale" (Pinto, 2019–20) → "global, diversified, complete and at scale" (2021–22) → "most important financial partner" and "complete counterparty" (Petno and Rohrbaugh, 2025) → "on offense" and "we like our hand" (AR2025).
- **Crisis identity:** "we are a port in the storm" (AR2019). The First Republic purchase is framed as civic duty: "Our government invited us and others to step up, and we did".
- **Tech identity** (new from 2025): a technology-driven company "as much as we are a bank" (COO letters). "JPMorganChase is a powerful neural network." (AR2025).
- **National identity** (new in 2025–26): the $1.5T SRI, defense and critical minerals, Dimon chairing the SRI advisory council, the "From the desk of" policy forum ("Good policy matters. And it’s often free.").
- **How it changed:** 2019–21 is stakeholder language (Business Roundtable purpose, racial-equity commitments). 2022–23 is the codified Purpose plus "guardians of the world’s financial systems". 2025–26 is technology company plus national-security financier. DEI language thins after 2024 ("DEI" becomes "DOI" in the AR2025 LOB letters).

---

## 5. Tailwinds, headwinds, challenges

**A** = the company admits it; **I** = my inference.

**Tailwinds**
- **Rates (A).** NII ex-Markets went from ~$50B (2022 guide) to ~$96.5B (2026) to a $107B 2027 central case. Payments revenue went from $13.9B to $19.3B "due in large part to the effect of higher rates" (Pinto, AR2022).
- **Volatility and a structurally larger Markets wallet (A).** Record Markets revenue was $30B (2024) and $35.8B (2025). The fee pool "won't go back".
- **Financing and Prime (A).** Financing is up 75% since 2019. RWA grew ~$103B in 2Q26, mostly Markets financing.
- **Deregulation (A, 2025–26).** "Positive effects of comprehensive deregulatory policies. This was badly needed and long overdue." Basel and G-SIB re-proposals cut the capital increase. The SLR fix is expected.
- **Consolidation toward scale (A).** Wallet consolidation among the largest institutional clients, with client share up 230bp since 2019. Payments "business gravitates to larger banks". Bank failures brought deposits and clients in 2023.
- **Technology scale (A).** Cost per trade is down 42% in Rates. KYC unit cost is down 40%. Modernization spend is "probably past" its peak (Barnum 2025).
- **Policy support for tokenization (A).** The GENIUS Act, "The new U.S administration has been a huge catalyst" (Lovett), and central-bank pilots (Acacia, Guardian).
- **Excess capital as optionality (A).** It was put at ~$54–60B (2024–25), ~$40B (AR2025) and ~$30B (3Q26). It is now being redeployed organically and through the SRI.

**Headwinds and challenges**
- **Capital rules on market-making (A).** G-SIB at ~5%, SLR, Basel; "un-American"; liquidity rules lock up more than $1T. Trading capital is a headwind (Pinto 2022).
- **Nonbank competition in markets and payments (A).** Citadel Securities and similar firms ("Many large market participants — for example, hedge funds and high-frequency traders, among others — have no obligation to make markets."), Stripe, Block, Revolut, "market infrastructure providers", and private credit, which runs about $1.8T leveraged.
- **FICC share below pre-COVID; Rates underperformance (A).**
- **Stablecoins as a deposit threat (A).** "some version of a threat to the business model" (4Q25). A Treasury estimate puts $6.6T of deposits at risk (analyst-cited).
- **Data access and agentic AI (A).** Screen-scraping is blocked. "we're not going to allow just any outside agents to come in inside the company". The open-banking fight is framed as a "subsidy for data middlemen".
- **Expense growth (A).** Expenses went from ~$68B (2021) to ~$107.5B (2026), with consensus at ~$114B for 2027. Dimon calls perpetual operating leverage a "crazy notion".
- **Succession and key-person risk (A, asked repeatedly by analysts); Lake's departure (A).**
- **Macro (A).** Stagflation odds "two times of what the market thinks" (2025). Deficits, Iran and oil, the "skunk at the party" of rising inflation in 2026, and weak private-credit underwriting (PIK, add-backs).
- **Political and legal exposure (A).** The Trump lawsuit over account closures (Jan 2026), "ping-pong regulations", and Credit Card Competition Act and APR-cap threats.
- **Kinexys is still tiny next to JPM's payment flows (I).** About $7B/day against ~$10–12T/day, or about 0.06%. Cumulative $4T figures flatter it. Dimon's own "We spent too much on it." suggests internal doubt.
- **JPM is both supplier and rival to venues (I).** It needs Tradeweb and MarketAxess liquidity and ships its algos through them. It also pushes clients toward its own channels, internalisation (JPM-X, SI) and data (Fusion). Rising electronic share weakens the relationship premium the CIB sells.
- **AI's payoff narrative is weakening in public (I).** The firm stopped quantifying AI value in late 2026 even as token costs rise. Watch whether 2027 guidance reintroduces numbers.
- **Concentration in the Co-President pair (I).** If the horse race ends badly, the firm loses one of two business heads at once.

---

## 6. Outside voices and skeptics in the corpus

- **Mike Mayo (Wells Fargo)** is the persistent skeptic on expense, technology and AI ROI and on tenure. He spoke in 2020, 2021, 2023, 2025 and 2026. Lines: "spending is certain. Returns are uncertain." (4Q20) and "you're spending the rate hikes for investments over the next 10 years." (4Q21). On the 3Q26 call he got Barnum to cut the AI-spend figure to ~$700M.
- **Other analysts:**
  - Betsy Graseck (Morgan Stanley): investment funding, crypto.
  - Glenn Schorr (Evercore): private credit scale, stablecoin deposit risk.
  - Erika Najarian (UBS): buybacks, succession traits.
  - Ebrahim Poonawala (BofA): agentic AI, "rogue agents".
  - Saul Martinez (HSBC): whether AI benefits are underestimated, citing Block's 40% layoffs.
  - Steven Alexopoulos (TD): "Iron Man never retired".
  - Ken Usdin (Autonomous): what the co-presidents mean for tenure.
  - Jim Mitchell (Seaport): operating leverage.
- **Risk magazine** (quoted by JPM, 2022): the bank "is feverishly remodelling itself for a future that only exists in outline—the giant US bank is a kind of castle-and-laboratory". The flip side: "but these are run-the-bank accomplishments, at a time when change-the-bank has become the priority."
- **Stablecoin and deposit-token debate** (on a JPM page):
  - Amanda Fischer (Better Markets): "Where my confidence in stablecoins collapses is the number of depegging events,"
  - Ran Goldi (Fireblocks), against JPM's thesis: "You cannot send a tokenized deposit to someone who is outside of banking,"
  - JPM's own Teresa Ho: "Overall, while adoption is poised to grow further, it might be at a slower pace than what some might anticipate,"
- **Market-structure voices on Markets pages:** Andrew Morgan (TS Imagine) on EMS adoption, Todd Hohman (SEDA Experts) on agentic-AI operational risk, Ben Hunt (Prescient) on retail volatility selling as an "invisible bubble", and BlackRock's Jason Warr calling ETFs the "poster child of e-trading".
- **Regulators and critics Dimon argues with:** the Fed (CCAR, OCI, G-SIB), the FDIC (handling of SVB and First Republic), proxy advisors ISS and Glass Lewis (JPMAM dropped them), and aggregators and the CFPB (Section 1033).
- **JPM's self-interest is visible.** The open-banking op-ed defends fees JPM earns from aggregators. The EU equities op-ed ("Variety in trading models is a feature – not a flaw – of European market structure.") defends JPM's systematic internaliser and dark pools. The digital-asset op-ed ("payments innovation becomes dangerous when it drifts into shadow banking") defends a deposit-token model that can pay interest against stablecoins that cannot.

---

## 7. Links to the Tradeweb study

1. **Founding owner, then seller.** JPM was among the dealer-owners. At Tradeweb's IPO (Apr 2019) and both follow-ons (Oct 2019, Apr 2020), JPM was a joint lead bookrunner while bank stockholders sold down [TW]. This matches `notes/tradeweb-outside-voices.md` (former owners went from 46% to 17.3% at IPO) and Risk.net's "hostage to the interests of big dealers" framing.
2. **People pipeline.** Thomas Pluta (JPM Global Head of Linear Rates; Tradeweb board from 2017) was Tradeweb President from Jan 2023 to Sep 2024 [TW]. Enrico Bruni (JPM 1995–2002, e-trading strategy) is now Tradeweb Co-Head of Global Markets. Chair Jacques Aigrain and director Daniel Maguire are both ex-JPM. JPMC's corpus mentions none of them.
3. **Launch dealer and liquidity provider.** JPM was counterparty on the first electronic SONIA swap-vs-gilt-future package (2020), the first iBoxx TRS (2021) and the first SOFR swap spread (2021, against BlackRock). In that SOFR release Pluta said "we are encouraging our clients to transition their trading away from LIBOR" [TW]. On portfolio trading, Koo said "we expect this to double in the next couple of years, if not triple" [TW, 2019].
4. **Distribution channel for JPM's own execution.** JPM was "the first dealer to offer algo execution strategies on the Tradeweb platform" (Liyan Yu, 2025-10-09) [TW]. It joined the multi-dealer algo environment with Citi, Morgan Stanley and RBC in 2026 [TW]. JPM's own letter says only that it launched "a new algorithmic trading offering to U.S. Treasury investors" (AR2023), so the venue goes unnamed.
5. **Client.** J.P. Morgan Asset Management routes Treasuries through Tradeweb. Mike McClinchie: "I just started releasing all of my orders from my OMS to Tradeweb" [TW, 2022].
6. **Competitor.** JPM runs single-dealer channels (Execute, J.P. Morgan Markets portal with 90k+ users), internalisation (JPM-X, JPB-X, EU systematic internaliser), algos (Aqua), data (Fusion, DataQuery, JPMaQS, indices: EMBI, GBI) and tokenized repo (Kinexys). JPM's survey finds 40% of traders use both single- and multi-dealer platforms. Andrew Cole describes "a push-pull between the venues that are desperate to implement things that get clients to trade on that platform" (2026-07-31). Peter Grant: "clients are looking at options including reducing the number of dealers and pushing towards this direct connectivity to mitigate the concerns." That is the information-leakage theme of `notes/tradeweb-a2a-information-leakage.md`, seen from the dealer side.
7. **Co-investor.** JPM led a 2021 investment in MAXEX, where Tradeweb invested in 2026 and JPM's Marc Simpson sits on the board. JPM and Tradeweb are both investors in Capitolis (2026) [TW].
8. **Adviser in venue M&A.** JPM was lead financial adviser to Tradeweb on ICD (2024) [TW]. JPM advised MarketAxess on its sale to ICE (2026, per the read-ice sibling).
9. **Index and data provider to venues.** The J.P. Morgan EM bond indices (GBI-EM, EMBI) drive Tradeweb's China and Saudi expansion stories [TW]. JPM is a benchmark owner inside the venue's growth thesis.
10. **The silence.** Across 165 JPMC records, venues are never named, not even at Investor Day. That fits the Tradeweb study's finding that dealers praise "the category" and not the venue. It also fits JPM's preference to describe electronification as its own cost-per-trade and franchise story.

---

## 8. Recommendation — what's worth noting

Ranked by value for the user's time. All avoid `notes/jpm-software-sector-spotlight-2026.md`, which covers J.P. Morgan *research* on software valuation and AI. None of these is about JPM Research.

1. **`jpmc-succession-by-rotation`: *How JPMorganChase built a succession bench without naming a successor (2019–2026)*.**
   - Thesis: Dimon and the Board ran a seven-year rotation (Piepszak CFO → CCB → CIB → COO; Petno CB → CIB; Rohrbaugh Markets → CIB → Consumer). It ended in a banker/trader co-president horse race, kept the date deliberately vague ("intent... not a promise") and accepted losing a contender (Lake).
   - Why: the cleanest primary-source case in the repo of CEO succession at a mega-firm, with dated quotes from both sides of analyst Q&A.
   - Serves E4 (Governance and the Board), E1 (Leading at Scale), 09 (Leadership and OB). Pairs with `tradeweb-people` (Tradeweb abolished its No. 2 seat; JPM doubled it).

2. **`jpmc-dealer-balance-sheet-vs-regulation`: *Dimon's case that capital rules are hollowing out market-making — and the Treasury market*.**
   - Thesis: one argument, made for six years: SLR, G-SIB and Basel push intermediation to nonbanks that are "fair-weather friends", and this makes Treasuries fragile. The posture moved from compliance (2023) to quantified opposition (+25%/+50%, 2024) to a qualified win under deregulation (2026). The Treasury-clearing mandate and primary-dealer limits are the live test.
   - Why: it is the dealer's half of the market-structure story Tradeweb tells from the venue side (all-to-all, clearing, 24/5). The user has no note on the bank-capital side.
   - Serves 11 (Global Strategy and Macro), 03 (Micro and Strategy Foundations: regulation as industry structure), E9. Links to `market-structure-24-5-*` and `tradeweb-rates-em`.

3. **`jpmc-dealer-and-venue`: *JPM as supplier, client, owner and rival of electronic venues*.**
   - Thesis: JPM never names Tradeweb or MarketAxess, yet it underwrote Tradeweb's IPO, staffed its leadership, launched its protocols, distributes its algos through it and advised MarketAxess on its sale. At the same time it builds single-dealer channels, internalisation and data to keep flow. Electronification is pitched as cost-per-trade (Rates down 42%), not as venue share.
   - Why: it closes the loop on the Tradeweb study's *power map* (dealers as a bloc) with the dealer's own words and incentives. Platform co-opetition as a worked example.
   - Serves 04 (Competitive Strategy), Canon: Network Effects and Platform Strategy (Parker et al., Brandenburger and Nalebuff co-opetition), E3 (venue M&A advisory). Pairs with `tradeweb-outside-voices` and `tradeweb-a2a-information-leakage`.

4. **`jpmc-kinexys-deposit-token-bet`: *Bank money on-chain: Kinexys, JPMD and the deposit-token vs stablecoin fight*.**
   - Thesis: JPM's answer to stablecoins is to keep the deposit (with its credit, regulation and interest) and change the rail. It moved from permissioned Onyx (2020) to public Base and Ethereum (2025–26) under GENIUS Act pressure while lobbying to close stablecoin "rewards". Scale is still ~0.06% of daily payment flow.
   - Why: tokenization runs through the Tradeweb, DTCC and ICE sibling studies. JPM is the bank-side protagonist, and the thesis can be tested over the next 12 months.
   - Serves 10 (Entrepreneurship and Venture: incumbent self-disruption), 04, E10. Canon: Christensen.

5. **`jpmc-ai-ledger`: *From 'spend anything' to 'not observable': six years of JPM's AI and tech-spend narrative*.**
   - Thesis: the tech budget rose from ~$12B to ~$19.8B, and AI use cases from 300 to ~1,000 ("the really important ones are 50"). The public payoff story went from unbounded (2021) to measured (2023–25) to deliberately unquantified (3Q26: ~$700M AI spend, benefits "aren't observable"). Jobs language went from "augment" to 30–40% cuts in discrete areas, and the COO says "not fewer headcount".
   - Why: a long-run, dated case of how a mega-firm communicates an AI investment to skeptical investors (Mayo as foil). It complements, and does not repeat, the research-side software note.
   - Serves E10 (Digital and AI Transformation), E8 (Investor Relations), 07 (Data and Decisions).

6. **`jpmc-competitor-map-shift`** (optional; could fold into 3): *From Big Tech to Citadel Securities: how Dimon's named threats changed.*
   - Thesis: the threat list moved from Amazon/Apple/Walmart (2020) to Stripe and shadow banks (2023) to Block, Citadel Securities, Revolut, Stripe, stablecoins and "market infrastructure providers" (2025–26).
   - Why: a compact Grove "only the paranoid" exercise on primary sources. Modest stand-alone value.
   - Serves 04, Canon: Landscape and Competitive (Grove, Christensen).

7. **`jpmc-excess-capital-as-strategy`** (optional): *Fortress balance sheet as an option: buybacks last, ROTCE as an output, SRI as redeployment.*
   - Thesis: the capital hierarchy is buffer → organic growth → dividend → buybacks. Excess went from ~$54–60B to ~$30B as buybacks were cut to ~$1B per quarter for the SRI and financing growth. "you should think of the Firm's ROTCE target as an output, not an input."
   - Why: a clean E2 case with numbers.
   - Serves E2 (Capital Allocation), 02 (Corporate Finance).

**Not worth noting (and why)**
- **Individual Kinexys client-win releases** (BMW, Siemens, Mitsubishi, FirstRand, Arab Bank, KB Kookmin, EBANX): repetitive and promotional. One line each in the chronology of note 4 is enough.
- **Quantum research posts** (QKD, certified randomness, QAOA): technology-identity signals, not market structure.
- **Innovation Week and Tech Week recaps, DEVUP, awards (Evident aside), Risk Awards, Extel sweeps:** the only reusable facts are already captured above.
- **DFAST and Investor Day notices:** dates only.
- **J.P. Morgan Global Research outlook pieces** (AI capex, AI and jobs, generative AI GDP): sell-side research, close to the existing `jpm-software-sector-spotlight-2026` and better sourced from the full reports.
- **Consumer items** (Apple Card, Coinbase consumer link, Chase UK and Germany, Smart Cash, retail execution vs payment for order flow): strategy signals only. The PFOF jab could be one paragraph inside note 3 or 6.
- **SRI and Todd Combs as a stand-alone note:** too early, and mostly political positioning. Fold it into note 7 if written.
- **A Dimon-letters *greatest hits* note:** tempting, but it would duplicate notes 1–5, which already carry the best quotes in a usable structure.

---

## 9. Method and quote verification

- **Sources fetched:**
  - Sitemaps: jpmorganchase.com and jpmorgan.com US.
  - Two JSON endpoints: `/services/json/v1/dynamic-grid.service/...` (IR and newsroom listings) and `/services/json/v1/investor-relations/quarterly-earnings.json` (PDF links).
  - PDFs via `curl -A "Mozilla/5.0"`, with text extracted using `pdftotext`.
  - HTML text from `.cmp-text` and `.cmp-title` blocks, falling back to `<main>` text. Dates come from the page's `alg-search-date` meta.
- **Reading:** nine parallel readers covered the letters (three packets), the LOB letters, the calls (two packets), Investor Day and the web items (two packets), plus my own pass on the Tradeweb corpus' JPM mentions. Scratch findings live outside the repo.
- **Verification:** a script extracted every quoted span of two or more words from this file, normalized whitespace, quotes, dashes and PDF line-break hyphenation, and checked each as a substring of `articles.jsonl` (or the Tradeweb corpus for [TW] quotes). It also checked the ≤25-word limit. Result: recorded at the end of this file.

**Verification result (2026-10-25):** 148 quoted spans of two or more words were checked line by line, with ellipsis fragments checked separately. **0 not found; 0 over 25 words.** Normalization covered curly vs straight quotes, en/em dashes, whitespace and PDF line-break hyphenation. One quote keeps the source's own spacing ("friends —they").
