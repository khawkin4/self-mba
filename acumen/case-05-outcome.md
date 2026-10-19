# Case 05 — SEALED OUTCOME: what happened after June 30, 2022

> **Stop.** Open this only after your memo and three forecasts for [case-05-seed-fund-2022](case-05-seed-fund-2022.md)
> are written into that file. Reading it first spends the rep.
>
> **Provenance.** Market path: FRED via `_ingest/regimes.py` (full-sample run, same rules). Venture facts: the firm
> notes [[primary-venture-partners-insights]] and [[harlem-capital-vc-insights]] (press and transcripts), plus
> [[wss-private-markets-wealth]]. Nothing here is a judgment on which plan was *right*. A plan can be sound and
> unlucky. This file resolves the forecasts and shows what each plan ran into.

## The regime path, quarter by quarter

| Quarter | Regime | Channel | Fed funds (end) | SLOOS net % | Stress z | VIX | 10y−3m |
|---|---|---|---|---|---|---|---|
| 2022Q2 *(decision)* | A Boom | — | 1.21 | −1.5 | 0.20 | 27.4 | +1.83 |
| 2022Q3 | B Lender's market | — | 2.56 | 24.2 | 0.49 | 24.8 | +0.35 |
| 2022Q4 | **C Drought** | market | 4.10 | 39.1 | 0.64 | 25.0 | −0.36 |
| 2023Q1 | **C Drought** | bank | 4.65 | 44.8 | 0.43 | 20.7 | −1.14 |
| 2023Q2 | **C Drought** | bank | 5.08 | 46.0 | 0.36 | 16.4 | −1.67 |
| 2023Q3 | **C Drought** | bank | 5.33 | 50.8 | 0.21 | 15.0 | −1.39 |
| 2023Q4 | **C Drought** | bank | 5.33 | 33.9 | −0.00 | 15.3 | −1.08 |
| 2024Q1 | B Lender's market | — | 5.33 | 14.5 | −0.38 | 13.7 | −1.30 |
| 2024Q4 | B Lender's market | — | 4.48 | 0.0 | −0.47 | 17.4 | −0.30 |

**How fast it turned.**
- The 10y−2y curve inverted on **July 6, 2022**, four trading days after the decision date.
- The first SLOOS reading after the decision jumped from easing to **+24% net tightening**, and it stayed above 30%
  for five straight quarters.
- The fed funds rate went from 1.21% to 5.33% in twelve months.

**How it ended.** There was no Shock. Lending standards normalized in 2024 while the Fed held at 5.33%, a soft
landing. The scenario map reads this as non-bank lenders filling the gap the banks left ([[wss-scenario-map]],
data finding 3).

**The lesson about the dashboard.** On the decision date every lagging gauge said Boom. Public stress gauges went on
to read *calm* through most of the drought (VIX at 15–16 in 2023Q2–Q4). Only the bank channel stayed lit. A plan
that waited for public confirmation would have waited through the whole drought.

## Resolving your forecasts

| # | Forecast | Resolution |
|---|---|---|
| 1 | Regime in 2023Q2 | **C Drought** (bank channel). Score 1 if you said Drought. |
| 2 | SLOOS > 30% in some 2023 quarter | **Yes.** All four quarters: 44.8, 46.0, 50.8, 33.9. |
| 3 | Fund II first close ≥ X% of target by your date | Score against the evidence below. If your date was before 2024 and your plan was *Hold* (launch mid-2023), the evidence says the odds were poor for an emerging manager. |

**Calibration score.** For forecasts 1 and 2, compute |p − outcome|, where outcome is 1 if it happened and 0 if not.
Log both in [JUDGMENT-LEDGER.md](JUDGMENT-LEDGER.md). For forecast 3, write one sentence on whether the evidence
supports your number.

## What real seed managers ran into (the evidence for forecast 3)

- **The scaled manager ran for the window, and made it.** Primary closed **$425M** in **September 2022** ($275M
  Fund IV plus a $150M Select opportunity fund), one quarter into the turn. That is plan 3 executed by a firm with
  institutional LPs and a brand. It went on to raise **$625M** for Fund V in February 2026, after the drought.
  ([[primary-venture-partners-insights]].)
- **The emerging manager raised before the turn, then met it on the next fund.** Harlem closed Fund II ($134M) in
  2021, at the top. Its Fund III, targeting $150M, appears in an SEC filing in **2024**, and the sources found no
  announced close. It raised into the post-drought LP squeeze plus a backlash against diversity-focused funds.
  ([[harlem-capital-vc-insights]] and press.)
- **Why LPs froze.** Fund distributions fell to post-GFC lows relative to NAV, and the denominator effect pushed
  institutions to pause new commitments. Seed managers also sat behind multi-stage firms in LP budgets.
  ([[wss-private-markets-wealth]] §6; [[primary-venture-partners-insights]] §8.)
- **The peer's call.** The mid-2022 prediction that seed would reprice within about six months fits the regime turn
  that followed. No transcript gives a dated seed-valuation series, so this is directionally confirmed, not
  measured.

## What each plan ran into

| Plan | Market it met | What went right | What went wrong |
|---|---|---|---|
| **1. Hold** | Fund II launch in mid-2023 landed in the middle of the drought | Fund I kept deploying through 2022–23 at reset prices, the strongest entry window in the cycle | The mid-2023 raise met LPs with no distributions and full allocations. This is the fund-timing risk in [[apply-wss-to-venture]] Concept 9. |
| **2. Brace** | Same raise problem; Fund I slowed into the best prices | Reserves defended winners through the A-round squeeze; no portfolio was forced into a down round | Slowing deployment during a drought buys at the bottom *less*, the opposite of Law 3's prize. And the raise problem wasn't solved. |
| **3. Run for the window** | Q3 2022 launch, one quarter before the Drought quarters | Primary shows it could work for a manager LPs already knew | For a $150M emerging manager, a smaller-target raise in Q3 2022 meant pitching LPs who were already watching the denominator. The plan works only if you can *close* in a quarter or two. |

The pattern the data supports: **the decision was really about the raise, not the pace.** Deployment through the
drought was the opportunity. Fundraising through it was the threat. The plans that separated those two did best.
For example, run for the window **and** keep deploying Fund I at pace, with an LP-approved extension as the backstop.

## Red-team prompts for your memo

- Did you name the **bank channel** (or any leading indicator) as the one to trust, or did you reason from VIX and
  spreads?
- Did you use a **base rate**? Both times since 1990 that a Boom gave way to high rates (2005, 2022), a Drought
  followed: about three years later in 2007Q4, and immediately in 2022Q4 ([[wss-scenario-map]], data finding 2).
  That is n = 2, a thin base rate, so a calibrated memo should say so rather than treat it as a law.
- Did your fatal risk name the **LP side** (distributions, the denominator effect), or only the portfolio side?
- Meta-question: which note, had you read it, would have changed the memo? Likely candidates:
  [[canon-tetlock-superforecasting]] (base rates) or [[wss-private-markets-wealth]] §6 (the distribution clock).
