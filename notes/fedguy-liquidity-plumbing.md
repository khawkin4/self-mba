# Fed Guy (Joseph Wang): reading the Fed, swap spreads, and the funding side of the AI boom

> **Sources:** Joseph Wang, former senior trader on the New York Fed's open markets desk, now CIO of Monetary
> Macro; author of *Central Banking 101*. **The blog (fedguy.com) could not be pulled:** the RSS feed was tried
> once on 2026-11-01 and the server reset the TLS connection (same for the home page), so no blog posts are in
> this note. In their place: transcripts of 8 videos from his own YouTube channel, *Markets Weekly* (Sep 12,
> 19, 26; Oct 3, 10, 17, 24, 2026) and his **October 2026 FOMC debrief** (Oct 28). Auto-generated captions, so
> names and numbers may be garbled. Raw corpus is local-only in
> `_ingest/raw/2026-11-01/fedguy-liquidity-plumbing/` (gitignored), with a `BLOCKED.md` fetch log. Summarized in
> own words.
>
> **What it adds:** [[wss-scenario-map]] and `_ingest/regimes.py` classify regimes from *slow* public gauges
> (fed funds, credit spreads, NFCI, SLOOS, VIX). Wang reads the *fast* gauges a former Fed desk trader watches:
> swap spreads, the Fed's own framing of financial conditions, and who is funding the marginal borrower. That
> gives the regime map a "what would flip it" layer.
>
> **Maps to:** **Course 11** (macro: regimes and transmission), **E6** (crisis: forced sellers), **E2** (capital
> allocation: when financing becomes the constraint).
>
> **Lens:** **Understand** (inputs to decisions), with **Run** content on Treasury-market plumbing. **Steps
> served:** none directly; it serves *regime awareness*, the context around steps 2 (allocation), 4
> (rebalancing into stress) and 8 (review). Not a portfolio method.
>
> ⚠ **Bias and verification.** Wang runs money and sells macro courses (centralbanking101.com, linked in every
> video description). Weekly videos are commentary, not research, and the political asides are opinion. **The
> 2026 events below are as he reported them on air and are unverified here:** a Warsh-led Fed starting a hiking
> cycle in September 2026, the 10-year above 5.3% and 30-year above 5.7%, a US–Iran conflict pushing Brent up,
> Treasury buyback sizes, and two FOMC dissents in October. The blog's longer, mechanism-per-post archive
> (scarce reserves, RRP draining, TGA) is the better source and is **not** reflected here.

---

- **Core claim:** The level of rates tells you less than whether the system can still *carry* the debt being
  issued. Watch the gauges of warehousing capacity (swap spreads), the central bank's own words on whether
  conditions are "tight", and whether the marginal borrower (now AI capex) can still raise money. When those turn,
  the regime turns, often before the slow indicators move.

## Framework

### 1. Swap spreads are the best price signal for "too many Treasuries"
- If Treasury supply outruns demand, Treasury yields rise relative to the expected path of policy (the swap
  rate), so **swap spreads go more negative**.
- Mechanism: leveraged buyers (relative-value funds, dealers) buy Treasuries with repo money, hedge the rate risk
  with a swap, and earn the spread. A more negative spread is the higher fee they demand to warehouse more bonds.
  When their balance sheets are full, the spread blows out (he cites April 2025 "Liberation Day").
- Use: he rejected the "AI bond issuance is crowding out Treasuries" story in late September 2026 because swap
  spreads showed no stress. **Check quantity stories against the price.**
- Same tool across countries: French 10-year swap spreads going more negative means France is being priced as a
  credit, not as a risk-free rate (Oct 3 and Oct 24 episodes).

### 2. The Fed's word for financial conditions tells you the next move
- The Fed fights inflation by tightening financial conditions; how tight is "enough" is subjective.
- Per Wang, the switch from Powell (conditions judged restrictive, so no hikes) to Warsh (judged not
  restrictive) is what started the 2026 hikes. After the October 2026 meeting he read Warsh's line that he was
  "unwilling and unable to call them tight" (as quoted on air) as "still in hiking mode."
- Wang's December 2026 call: hike, **unless** an AI-led equity correction intervenes. That is a falsifiable test
  to check after the meeting.
- Calendar change (reported): 2027 keeps eight FOMC meetings but only seven "live"; 2028 maybe six. Fewer live
  meetings make the front end jumpier.

### 3. Financing has become the constraint on the AI build-out
- Hyperscalers spent their free cash flow on capex, then borrowed (including off-balance-sheet SPVs and
  guarantees). CDS on AI-linked issuers is rising; neoclouds (heavily levered compute lessors) are the weakest
  link.
- His framing: data-centre builders **borrow long and lend short**, financing long-lived assets with compute
  contracts of 1–5 years whose renewal price is uncertain. That is the reverse of a bank's mismatch, and it is
  exposed to the spot price of compute (cheaper chips, better algorithms, VCs tiring of subsidising demand).
- Rates "get in the cracks": the Fed chair argued higher rates are slowing parts of the AI and commercial real
  estate complex, and Wang agreed.
- Read-through: if AI capex slows and it has been a large share of GDP growth, recession odds rise, and that pulls
  the Fed off its hiking path.

### 4. Supply tricks move less than headlines say
- Treasury **buybacks** at the long end: a larger programme was announced and then under-executed in September
  2026, and the 30-year kept rising. Small relative to fundamentals. (Conks reached the same view: buybacks move
  swap spreads more than yields; see [[conks-funding-plumbing]].)
- **Bank of England QT tweak** (Sep 2026, as reported): slower active gilt sales, sold to the government rather
  than the market. A sign central banks will bend QT when long yields become unstable.
- **Oil:** rising oil is inflationary (yields up) up to a point, then recessionary (yields down). He doesn't
  know where the turn is, but noted yields were no longer rising with oil in late October.

## How it informs regime awareness (`regimes.py`)
- **Rates axis:** a hiking cycle with the 10-year above 5% (if accurate) puts late 2026 firmly in **HIGH** price of
  money. The open question is the cash axis.
- **Cash axis, where Wang adds signal:** `regimes.py` reads BAA10Y, NFCI, SLOOS and VIX. Wang's late-2026 picture
  (VIX just under 20, skew steepening, AI CDS widening, financing harder to raise) is the pattern the script's
  docstring warns about for 2023: stress showing in one funding channel while the broad composites stay calm.
  His reading implies **B (Lender's market) drifting toward C (Drought)**, with the AI financing channel as the
  stuck pipe.
- **Candidate fast gauges** to test, not adopted: 10-year Treasury minus SOFR swap rate (swap spread; not on
  FRED, needs another source), SOFR minus IORB (both on FRED as `SOFR` and `IORB`), Fed reverse repo
  (`RRPONTSYD`), bank reserves (`WRESBAL`) and the TGA (`WTREGEN`). Series IDs are from memory; confirm on FRED
  before wiring anything in. Any addition should go through the `--sweep` sensitivity check.
- **Transition triggers to watch:** an AI-led equity correction (Fed pauses: B→C or C→D), oil past the recession
  inflection (yields fall: toward D), French spreads widening into the 2027 election (euro risk-off, deflationary).

## Applies when
- Reading the current regime between FOMC meetings, before slow indicators update.
- Testing a popular macro story ("AI bonds crowd out Treasuries", "buybacks will cap yields") against a price.

## Breaks when
- **Swap spreads have more than one driver.** Bank capital rules (SLR), dealer balance-sheet relief and hedging
  flows move them too, so a calm spread can hide stress elsewhere.
- **Weekly commentary drifts with the news.** Single-episode calls are not a track record; score them.
- **Politics.** He mixes market reads with strong political opinion; separate the two before using either.
- **Caption errors.** Auto-captions mangle names ("Wars"/"Walsh" for Warsh) and figures. Verify any number
  before citing it.

## Practitioner counterpoint
- Conks ([[conks-funding-plumbing]]) reads the same plumbing at higher resolution (SOFR-FF basis, the Fed's repo
  "sweet spot", G-SIB year-end effects) and agrees that swap spreads are the best friction gauge.
- [[wss-rates-macro]] covers the same instruments from the sell-side seat (basis trade, negative swap spreads,
  LIBOR to SOFR).
- A personal investor can rarely act on any of this directly. Its value is knowing which regime you are in
  before you rebalance or add risk.

## Links
[[wss-scenario-map]] (the regime 2×2) · [[wss-rates-macro]] · [[conks-funding-plumbing]] ·
[[rodrigues-derivatives-problem-map]] (funding cost and swaps from the quant side) · [[jpmc-capital-regulation]]
(SLR and capital rules that set dealer capacity) · [[portfolio-methodology-educators]] ·
[[canon-perrow-normal-accidents]] (tightly coupled funding chains) · [[canon-meadows-thinking-in-systems]] (stocks,
flows and delays in liquidity)
