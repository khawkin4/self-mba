# Note · Fourier / frequency-domain use cases across the Compounding MBA

> Cross-cutting tool note · Maps to **Course 06** (Operations), **07** (Data & Decisions), **11** / **E9** (Macro), **E8** (IR), gaps **Statistics & Quant**, canon **Systems Thinking**, `quant-backtesting/`

- **Source:** repo-wide sweep (CURRICULUM, lessons/, learn/, notes/, notes/canon/, acumen/, quant-backtesting/, _ingest/) + live tests on the cached FRED series, 2026-10-24
- **Core claim:** Fourier is a tool for *when* and *how regularly*, not *what* or *why*. It earns its place where a **numeric series** has a **stable cause** and **many cycles** of data — calendars, seasons, delays in feedback loops. Everywhere else in an MBA ("credit cycles", "VC cycles", "debt cycles") it is most useful as a **debunking tool**.
- **Framework — sort every "cycle" first:**
  1. **Deadline, not a cycle** (patent expiry, statute of limitations) → event/cohort study, not Fourier.
  2. **Known schedule** (FOMC, auctions, earnings season, month-end, payday, fiscal year-end) → you already know the period: **fold the data on the calendar** (event study). More powerful than scanning a spectrum.
  3. **Stable natural/structural rhythm** (seasons, 24h, 7-day week, supply-chain delays) → periodogram, seasonal adjustment, Fourier-term forecasting.
  4. **Quasi-cycle** (business cycle, bullwhip in real chains, default cycles) → broad hump, not a line; band-pass to *describe*, never to *time*.
- **Applies when:** sampling is faster than 2× the rhythm (Nyquist); ≥ several full cycles; the cause doesn't move; you test peaks against a **red-noise null** with a **multiple-testing** correction.
- **Breaks when:** few cycles; persistence (AR(1) / random-walk) masquerading as cycles; fat tails (variance — and so the power spectrum — may not exist; characteristic functions still do); two-sided filters used "as of" today (endpoint look-ahead); scanning hundreds of frequencies and keeping the best one (de Prado's seasonal-overfitting example).
- **Practitioner counterpoint:** quants use calendar effects heavily but treat spectral "peak-hunting" in prices as data-snooping; macro shops use band-pass filters for description only.
- **Links:** [[canon-sterman-business-dynamics]] [[canon-meadows-leverage-points]] [[canon-shannon-information-theory]] [[canon-kahneman-sibony-sunstein-noise]] [[canon-taleb-black-swan]] [[wss-rates-macro]] [[wss-trading-hedge-funds]] [[sec-filing-intelligence]] [[lopez-de-prado]] [[factor-models-regime-detection]]

---

## 1. What the tests on our own data showed

Script: `python3 quant-backtesting/rhythm_fred_check.py _ingest/raw/2026-10-04/data/fred`
(periodogram vs. a smoothed-background null, 1% family-wise threshold across all frequencies; plus direct calendar folds)

| Series | Naive test (AR(1) null, 99% per frequency) | Corrected test | Verdict |
|---|---|---|---|
| Fed funds (level / change) | "Cycles" at 8.6, 4.5 months | Nothing significant | No rate cycle |
| NFCI financial conditions | "Cycle" at ~31 weeks | Nothing significant | No cycle — persistence |
| 30y mortgage, Baa–10y, SLOOS | Short-period "peaks" | Nothing significant | Noise |
| **VIX daily change** | Smeared | Fold by weekday: **Mon +1.5–2.2%, Fri −1.0%**, same in 1990–2007 and 2008–2026 | **Real** — mechanical weekend effect in implied-vol calculation |
| **Core PCE m/m (already SA)** | — | Fold by month: **January +0.6–0.8 ann. pts** above average since 1990; first month of quarter high | **Real** — residual seasonality survives official adjustment |

**Lessons:** (a) the naive test finds "cycles" everywhere — the correction kills all of them in rates/conditions; (b) when you know the period, fold on it directly; (c) "seasonally adjusted" ≠ seasonality-free.

Beer Game sim (`python3 quant-backtesting/rhythm_beer_game.py`, 4 stages, white-noise demand):

| Shipping delay | Factory/retail variance | Peak gain by frequency |
|---|---|---|
| 1 week | 1.0× | 10× at ~27-week period |
| 2 weeks | 2.1× | 20× |
| 4 weeks | 7.0× | 72× at ~24-week period |

Random demand comes out as a ~6-month oscillation at the factory — **structure creates the cycle**. In this parameterization the period is set mostly by forecast smoothing; the delay sets the *size*. That is Meadows' leverage points #9 (delays) and #8 (balancing-loop strength) as a two-knob experiment.

## 2. Strong use cases (do these)

1. **Bullwhip in the frequency domain** — `lessons/canon-systems-complexity.html` (L14–43, 130), `canon-sterman-business-dynamics.md` (L13–16, 72), `canon-meadows-leverage-points.md` (L12). Spectrum of orders per stage, gain by frequency, cross-spectral phase = measured delay. Real data: FRED RSXFS vs AMTMNO, ISRATIO.
2. **FOMC / Treasury-auction / month-end calendars** — `wss-rates-macro.md` L358–364 (event-day variance weighting), L594 (FF–SOFR −30bp at month-end), `wss-technicals-career.md` L634–650 (auctions as scheduled supply shocks). Fold daily yields/repo spreads on the calendar; Lomb–Scargle for uneven FOMC spacing. Data: FRED DGS2, SOFR, EFFR, RRPONTSYD; TreasuryDirect.
3. **Seasonal adjustment before anomaly flags** — `sec-filing-intelligence.md` L13, 32: the quarterly anomaly flagger compares to trailing history, so retail Q4 will throw false alarms. Remove the 4-per-year seasonal (STL or seasonal indices) first. *Most directly useful code change.* Needs a quarterly mode in `_ingest/edgar.py` (currently `latest_facts` keeps only the latest annual value; Q4 = FY − Q1..Q3).
4. **Operations forecasting** — `lessons/core-06-operations.html` has no demand forecasting or seasonality. Add STL / Fourier-term (Prophet-style) forecasts; 24h + 7-day arrival spectra for queue staffing. Data: FRED RSAFSNA vs RSAFS; AMZN/WMT 10-Q revenue; M5 Walmart.
5. **A/B tests and regressions** — `lessons/gaps-statistics-quant.html` L72 ("4.6% over a week"), L98–104; `core-07-data-analytics.html`. Day-of-week cycle → test in whole weeks; deseasonalize before regressing trending series.
6. **Raw vs adjusted macro** — `core-11-global-macro.html`, `exec-E9` L79, `wss-ai-economics.md` L1181–1186 (January payrolls head fake). Compare PAYNSA vs PAYEMS, CPIAUCNS vs CPIAUCSL; add the residual-January PCE finding above.
7. **Calendar effects in market structure** — `wss-trading-hedge-funds.md` L484–487 (monthly → weekly → 0DTE expiries), `market-structure-24-5-trading.md` L27–31 (overnight returns; does the daily cycle split under 24/5?). Spectrogram of volume over 2010–2026. Needs intraday/expiry data not in the repo.

## 3. Moderate use cases

8. **Review cadence = sampling rate (Nyquist)** — `canon-shannon-information-theory.md`, `canon-aws-mechanisms-orr.md` L37, `canon-4dx…` L15/73, `canon-doerr…` L12. A monthly board deck can't see anything faster than ~2 months and aliases weekly swings. Lead-vs-lag measure: coherence + phase lag = true lead time.
9. **Personal cash rhythms** — `learn/unit-10-personal-finance-operating-system.md` L15, 67. Lomb–Scargle on bank-transaction dates finds biweekly pay, monthly rent, annual lumps; shows why "6× average monthly expenses" understates lumpy months.
10. **Working-capital swings** — `learn/unit-02-cash-vs-profit.md` L55, `core-01-accounting.html`. Quarterly inventory/OCF for WMT, TGT, NKE: Q3 build, Q4 release.
11. **Energy demand** — `wss-trading-hedge-funds.md` L1151, L680 ("seasonal build" vs glut). EIA storage + heating degree days.
12. **Noise audits** — `canon-kahneman-sibony-sunstein-noise.md`. If repeated over many periods, split variance into drift (low frequency) vs scatter (white).
13. **Acumen cases** — none mention seasonality today. Carvana (`case-03` L99, 208, 307: loan-sale spread "cyclical") — test against BAA10Y / MORTGAGE30US (both showed *no* cycle above). Seed fund 2022 — pair `regimes.py --asof` with the red-noise lesson. Boeing L335 ("bullwhip two to four quarters").
14. **Personal OS** — `exec-E11-operating-system.html` L30–50 energy audit; habit logs (`canon-clear-atomic-habits`) show the 7-day line.

## 4. Cautionary / "breaks when" material

15. **Debt cycles** — `quant-backtesting/research/bridgewater.md` L12–13, field guide L383: 75–100-year cycles have 2–3 observations. Unconfirmable.
16. **Yield-curve → recession** — `wss-rates-macro.md` L1381–1392: ~8 events; count them, don't spectrum them.
17. **VC / exit / M&A / credit "cycles"** — `harlem-capital-vc-insights.md` L122–132, `wss-private-markets-wealth.md` L264–296, `wss-credit-distressed.md` L1090–1107. Red-noise null exercise — our NFCI/Baa tests are the template.
18. **Regimes don't cycle** — `wss-scenario-map.md` L108 already says it; `regimes.py` and the HMM/change-point notes are the right tools. A band-pass "cycle phase" would break the `--asof` no-hindsight rule.
19. **Fat tails** — `canon-taleb-black-swan.md`: spectral tools assume finite variance; the option-pricing demos (`fourier_pricing_demo.py`) show where Fourier *does* still work — via characteristic functions.
20. **Seasonal overfitting** — de Prado transcript ("my favorite examples come from the area of seasonal patterns"); `academic-frameworks-multiple-testing.md`. A periodogram peak is a selected trial out of hundreds.

## 5. Gaps found in the repo

- No lesson, learn unit or GLOSSARY entry covers seasonality, seasonal adjustment, periodograms, coherence or Nyquist (GLOSSARY has only "bullwhip effect", L481).
- `fourier_pricing_demo.py` / `fourier_variations.py` are **uncommitted** and not linked from the site (`site/library.py:28` publishes only `quant-backtesting/research/*.md`).
- `edgar.py` has no quarterly time-series mode.
- `canon-ohno-toyota-production-system.md` lacks heijunka (production levelling = a low-pass filter on demand).

## Rep

Pick one strong case. State the suspected cause and its exact period *before* looking. Fold the data on that period, then run the corrected periodogram. If the peak only appears in the uncorrected test, write it up as a "breaks when".
