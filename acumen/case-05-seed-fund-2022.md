# Case 05 — A $150M seed fund, June 30, 2022: hold or brace?

> **Status:** OPEN — awaiting your memo.
> **Rep type:** capital allocation under regime uncertainty + fund strategy (Exec E2; Course 10).
> **Size:** full (~90 min) — see the menu in [MECHANISM.md](MECHANISM.md).
> **Historical rep with a sealed key.** Unlike cases 01–04 this decision has resolved. What happened is in
> [case-05-outcome.md](case-05-outcome.md). **Do not open it until your memo and forecasts are written.** The
> outcome scores your forecasts (calibration), not your memo; the memo is still red-teamed on the rubric.

## The brief

It is **Thursday, June 30, 2022.** You are the managing partner of a seed fund. The fund is hypothetical; the market
is not.

**Your fund (hypothetical parameters; the ranges come from the two real firms in the notes):**
- **Fund I:** $150M, 2021 vintage, ~45% of investable capital called. Planned 3-year investment period, ending
  mid-2024.
- **Checks and ownership:** first checks of $1.5–3.5M for 10–15% ownership. Reserves at about 1:1, so roughly half
  of each fund is held back for follow-ons.
- **Portfolio:** about 18 companies. Most raised at 2021 prices, and roughly a third will need a Series A within
  18 months.
- **LPs:** two endowments, a fund-of-funds, a corporate, and about 30 family offices and individuals.
- **Plan of record:** launch Fund II in **mid-2023**, targeting $200M.

**What you can see today (verify every figure; none of it should be taken from this brief on trust):**
- **Rates:** the Fed has hiked three times since March. Effective fed funds is ~1.2% at quarter-end, and core PCE
  inflation is running ~4–5% above it. The policy rate is still well below inflation.
- **The yield curve:** 10y minus 2y is **+0.06**, a few basis points from inverting.
- **Public markets:** growth stocks have repriced sharply and the IPO window has been shut for months. VIX averaged
  ~27 in the quarter.
- **Credit and banks:** the Baa spread is ~2.1, not alarming. Banks are still net *easing* C&I lending standards
  (SLOOS about −1.5% to −8% across the latest readings).
- **The regime classifier, as of today** (`_ingest/regimes.py --asof 2022-06-30`), reads **Boom** for 2022Q1
  and Q2.
- **A peer's read:** a respected NYC seed GP says public markets and growth investors have repriced, but seed
  "hasn't gotten the memo." He expects seed pricing to reset within about six months.
  ([[primary-venture-partners-insights]] §8, mid-2022 interview.)

**The tension.** The lagging gauges say Boom. The leading ones (hikes, curve, the dead IPO window, growth-stage
repricing) say the money is about to get more expensive and stop coming back. Your Fund II plan assumes LPs who are
still writing checks in mid-2023.

**The decision:** pick one of three plans, and state what's the single thing that, if wrong, sinks it:

1. **Hold:** keep Fund I's 3-year deployment pace and the mid-2023 Fund II launch.
2. **Brace:** slow Fund I to a 4–5 year pace, raise reserves for the portfolio, and keep the Fund II date.
3. **Run for the window:** launch Fund II **now** (Q3 2022) at a smaller target to close before LPs freeze, and
   slow Fund I.

(A fourth plan is allowed if you can defend it.)

## Pull the real data (as of the decision date — no hindsight)

```
python3 _ingest/regimes.py --asof 2022-06-30 --since 2000     # regime history using only data to that date
```
FRED series (stop reading at 2022-06-30): `FEDFUNDS`, `T10Y2Y`, `T10Y3M`, `BAA10Y`, `DRTSCILM` (SLOOS), `NFCI`,
`VIXCLS`, `PCEPILFE`. Name the indicator you trust most and say why it beats the others *for this decision*.

## Hindsight firewall

**Allowed before the memo:** the *concept* sections of the WSS notes:
- [[wss-rates-macro]]: curve, FOMC, financial conditions
- [[wss-private-markets-wealth]]: the distribution clock, denominator effect, LP behavior
- [[wss-credit-distressed]]
- [[wss-capital-markets-ma]]: IPO window
- [[harlem-capital-vc-insights]]: fund math
- [[primary-venture-partners-insights]] §§2–3: ownership, reserves, the opportunity fund

**Not until after the memo:** [[wss-scenario-map]] (its data section narrates 2022–23), [[apply-wss-to-venture]],
and [case-05-outcome.md](case-05-outcome.md). Several WSS notes also mention 2023–26 events in passing. If you hit
one, note it in the memo, so the red team can discount for leakage.

## Canon to bring to bear

`canon-klarman-margin-of-safety` (dry powder; don't need the good case) · `canon-taleb-antifragile` (who is the
forced seller when funding is pulled) · `canon-tetlock-superforecasting` (base rates and calibrated updating) ·
`canon-mauboussin-success-equation` (vintage luck vs. skill in fund returns)

> Four, deliberately. The case is built to test whether you **use base rates** (how often does a hiking cycle with a
> flattening curve end in a credit crunch?) rather than narrate.

## Your deliverable

**Full memo** (one page, spec in [README.md](README.md)), written to your LP advisory committee:
- **BLUF:** which plan.
- **The crux:** what you believe about the next 18 months that your plan depends on.
- **Three reasons,** each with a real, dated figure.
- **The fatal risk and its mitigation.**
- **The ask:** what you need from LPs (e.g. an extension of the investment period, approval to reallocate reserves).

**Attach three forecasts,** each with a probability, resolving by **2023-12-31**:
1. **Market:** the quarterly regime per `regimes.py` (Boom / Lender's market / Drought / Shock) will be ______ in
   2023Q2. *(p = __%)*
2. **Bank credit:** SLOOS net tightening (`DRTSCILM`) will exceed 30% in at least one quarter of 2023. *(p = __%)*
3. **Your own:** under your plan, Fund II reaches a first close of at least ___% of target by ______. *(p = __%)*
   This one is about *seed fundraising in general*. The outcome file scores it against what real seed managers in
   the notes actually achieved.

---
## YOUR MEMO
*(paste here)*

## YOUR FORECASTS
1. ...
2. ...
3. ...

---
## RED-TEAM (after you submit)
*(six-dimension scores · the bear case · the boardroom question that sinks you · calibration from the outcome file ·
and the meta-question: which canon note, had you read it, would have changed this memo?)*
