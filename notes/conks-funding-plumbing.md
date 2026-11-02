# Conks (Concoda): the money-market plumbing, gauge by gauge

> **Sources:** *Conks* (conks.plumbing, Substack, pseudonymous author "C."), pulled 2026-11-01. The archive lists
> 150+ posts back to 2021; most long-form pieces since late 2023 are **paid (Conks Pro) and were skipped**,
> including the Oct 31 2026 *Primer: The Cross-Currency Basis* and both parts of *The Repo Dark Spot*. Pulled:
> **28 free posts**: the *Primer: The SOFR/FF Basis* (Jun 2026), two *Plumbing Feed* roundups (Apr and Sep 2026),
> two free *Plumbing Notes* (Sep and Oct 2025), seven free long-form essays from 2022–23 (Eurodollar system,
> Treasury market, liquidity squeeze), and 16 infographic posts whose content is images. Fourteen infographic images
> were downloaded and three were read visually for this note: the G-SIB surcharge, the Fed's repo-rate "sweet
> spot", and banks' intraday liquidity requirements. The rest (rate and repo hierarchies, key repo spreads,
> dealers under Basel III) are saved but **not yet read**. Raw corpus,
> archive index and downloaded images are local-only in `_ingest/raw/2026-11-01/conks-funding-plumbing/`
> (gitignored). Summarized in own words; the infographics are copyrighted and are not reproduced.
>
> **What it adds:** [[rodrigues-derivatives-problem-map]] explains *how instruments are priced*; Conks explains
> *where the cash comes from* and which rules decide whether it moves: reserves, repo, the Fed's facilities, and
> bank capital and liquidity constraints. It is the closest match in format to Rodrigues (one mechanism per
> visual), on the funding side of the book.
>
> **Maps to:** **Course 11** (macro: transmission), **E6** (crisis: funding spirals), **E9** (FX and global
> dollar), with links to the market-infrastructure studies ([[ice-clearing-treasury]], [[jpmc-capital-regulation]]).
>
> **Lens:** **Run** (how dealers and banks fund and constrain a book), with **Understand** for regime reading.
> **Steps served:** none directly. Serves *regime awareness* for `_ingest/regimes.py` (below).
>
> ⚠ **Bias and verification.** Pseudonymous author; sells a paid tier, so free posts are partly marketing for it
> and the full reasoning sits behind the paywall. Trade calls ("wideners to keep widening", "fade three cuts")
> are opinions, not scored here. Infographics carry Conks's own disclaimer that figures are illustrative (the
> G-SIB example's 850-point score is a worked example, not a named bank). 2026 policy events (a Warsh-led Fed,
> reserve-management purchases, expanded Treasury buybacks, an SLR rework) are **as reported** by Conks and not
> verified here.

---

- **Core claim:** Short-term dollar funding is a set of linked markets (reserves, fed funds, repo, FX swaps)
  bounded by Fed facilities and bank rules. Liquidity is "plentiful" or "scarce" not by the size of the Fed's
  balance sheet alone but by whether **the banks that hold reserves are willing and allowed to lend them**. A
  handful of spreads tells you which state you're in, usually before the headlines.

## Framework

### 1. The gauges, and how to read them
| Gauge | What it measures | Reads "tight" when |
|---|---|---|
| **SOFR minus EFFR** ("SOFR-FF basis", ticker SERFF) | Repo rate vs the near-dead unsecured interbank rate | The basis widens (more positive). EFFR barely moves (~$100bn a day, mostly an arbitrage), so SOFR does the moving |
| **SOFR vs IORB** | Repo rate vs what the Fed pays banks on reserves | SOFR trades **above** IORB: banks need a premium to move reserves into repo |
| **SOFR vs the standing repo facility (SRF) rate** | Whether the Fed's ceiling is binding | Dealer repo trades at or above the SRF rate, and the SRF is actually tapped |
| **Overnight RRP balance** | Spare cash parked at the Fed by money funds | Near zero: the shock absorber is empty, so cash leaves repo before it leaves the RRP |
| **Swap spreads** (Treasury yield vs SOFR swap) | Dealers' ability to warehouse Treasuries | More negative. Conks calls this the best single friction gauge |
| **Cross-currency basis** | The cost of borrowing dollars via FX swaps | More negative (dollar scarcity offshore). Primer paywalled; mechanics from the free 2023 Eurodollar essay and swap-line infographics |

- Futures quirk worth learning once: fed funds and SOFR futures are priced as 100 minus the rate, so a *wider*
  SOFR-FF basis shows up as the futures spread "selling off" (more negative). Analysts don't agree on the words
  "tighten" and "widen" here; check which one they mean.
- Calendar spreads of the basis (e.g. July vs September) show the market's expected *change* in funding
  conditions, for instance around tax dates, quarter-ends, or when Fed purchases begin.

### 2. The Fed's "sweet spot" and what pushes repo out of it
- The Fed wants overnight repo (SOFR, TGCR, BGCR) **just below IORB**, between the RRP floor and the SRF ceiling.
- Pushing repo **up**: rate cuts that banks front-run by buying Treasuries with reserves; banks holding reserves
  against unrealized securities losses instead of lending them; dealers funding record Treasury inventories in
  repo; hedge-fund basis-trade leverage demand.
- Pulling repo **down**: Fed reserve-management purchases of bills (Conks insists "QE is QE and everything else
  is not QE"); technical cuts to IORB or the SRF rate; more central clearing, which shrinks bank balance-sheet cost.
- The Fed is (per Conks, Oct 2025) informally moving its target from the unsecured fed funds rate to a **secured
  repo rate (TGCR)**, finishing the LIBOR-to-SOFR shift on the policy side.

### 3. Rules set the price of balance sheet
- **G-SIB surcharge:** a bank's score is the higher of two methods. Both score size, interconnectedness,
  complexity and cross-border activity; Method 1 adds substitutability, the Fed's Method 2 adds **short-term
  wholesale funding**. Scores fall into 100-point bands, each band adding about 0.5 points of extra CET1 capital.
  Because the scores are measured at **year-end**, banks shrink repo and other wholesale activity into December,
  which is a cause of recurring year-end funding spikes.
- **Liquidity requirements:** the LCR is an end-of-day test, but internal stress tests and resolution-planning
  rules (RLAP/RLEN) bind **intraday** and are stricter. Banks add self-imposed buffers on top. So "excess
  reserves" are much smaller than the headline: a bank can hold many reserves and still have none to lend.
- **Leverage ratio (SLR)** taxes every asset, including safe Treasuries and repo. Easing it ("relief valve")
  frees dealers to warehouse more bonds, which shows up in swap spreads.

### 4. Who holds the bonds now
- Primary dealers held a record net long Treasury position (over $500bn, per Conks, Apr 2026) that they fund in
  repo and hedge with swaps. The **"Great Balance Sheet Congestion"**: large deficits, foreign buyers facing
  negative FX-hedged carry, and dealer constraints.
- Private, price-sensitive holders now own about three-quarters of Treasuries (Conks citing Fed data), so yields
  clear on macro views more than on central-bank buying.
- Sovereign offsets (Treasury cash-management and liquidity buybacks, Fed bill purchases) dampen volatility.
  Conks's view: buybacks move **swap spreads** more than yield levels.
- Foreign official access: the Fed's FIMA repo facility lets foreign central banks raise dollars against
  Treasuries without selling them, which makes swap-line requests mostly signalling.

## How it informs regime awareness (`regimes.py`)
- `regimes.py`'s "cash stuck" axis uses credit spreads, NFCI, SLOOS and VIX. Conks's gauges are **upstream** of
  those: funding friction appears in repo and swap spreads days or weeks before it widens credit spreads or
  moves NFCI.
- Reading for Q4 2026 from the free posts (as of Sep 2026): front-end funding calm (SOFR-FF tight, swap spreads
  widening on buybacks and SLR relief), so the **money-market channel is open** even with rates high. That fits
  **B (Lender's market)**, not C, on this channel; Wang's AI-financing concern is a credit-channel signal
  ([[fedguy-liquidity-plumbing]]). The two can disagree, which is why the script already has two channels.
- Candidate additions to test, not adopted: SOFR minus IORB, SOFR minus EFFR, and RRP balance as a third
  "plumbing" channel, with a stuck threshold such as SOFR > IORB for most of a quarter. Must pass the `--sweep`
  sensitivity check. The data begin in 2018 (SOFR), so the backtest is short.
- Seasonal false alarms to filter: quarter-ends, mid-month Treasury settlements, tax dates, and especially
  **year-end** (G-SIB window dressing).

## Applies when
- You need to know whether a rate move is *policy* or *plumbing* (a funding squeeze can lift short rates without
  any change in the Fed's stance).
- Studying dealers, clearing houses and venues ([[ice-clearing-treasury]], [[tradeweb-rates-em]],
  [[trading-floor-mechanics]]): their volumes and margins move with these constraints.

## Breaks when
- **The paywall.** The free sample is mostly diagrams and roundups; the argued theses (cross-currency basis, repo
  dark spot) are paid. This note sees the toolkit, not the full case.
- **Rule changes.** SLR, G-SIB and central-clearing rules were all moving in 2025–26; any threshold learned
  today can shift with the next rule.
- **Personal use.** None of this tells an individual what to buy. It tells you when "cash is trash" headlines
  or a funding scare are noise versus a regime turn.

## Practitioner counterpoint
- Wang ([[fedguy-liquidity-plumbing]]) ex-NY Fed desk, uses the same swap-spread gauge but argues from a slower,
  macro vantage. They agree that buybacks are small and swap spreads are the price signal to watch.
- [[wss-rates-macro]] (sell-side seat) covers the basis trade and negative swap spreads; Conks adds the
  regulatory machinery that sets their size.
- [[apply-six-problems-to-market-infrastructure]] maps funding and capital problems to the venues; Conks
  explains why those problems spike at year-end.

## Links
[[fedguy-liquidity-plumbing]] · [[wss-scenario-map]] · [[wss-rates-macro]] · [[rodrigues-derivatives-problem-map]]
(XVA and funding cost) · [[jpmc-capital-regulation]] · [[ice-clearing-treasury]] · [[tradeweb-rates-em]] ·
[[trading-floor-mechanics]] · [[apply-six-problems-to-market-infrastructure]] · [[canon-perrow-normal-accidents]] ·
[[canon-meadows-thinking-in-systems]] · [[portfolio-methodology-educators]]
