#!/usr/bin/env python3
"""
Market-regime classifier for the Compounding MBA — places each quarter since 1990 in the
four-regime map from notes/wss-scenario-map.md, using public FRED data.

Stdlib only (no pip). Pulls FRED's keyless CSV endpoint:
  https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>

The two axes:
  rates   price of money.   HIGH if the quarter-end effective fed funds rate >= RATE_HIGH (2.5%).
  cash    is money coming back?  STUCK if EITHER channel is stressed:
          market channel  the mean z-score (vs. 1990Q2 onward) of Baa-Treasury spread, Chicago Fed
                          NFCI, net % of banks tightening C&I standards (SLOOS) and VIX is
                          >= STRESS_STUCK (0.5); or
          bank channel    SLOOS net tightening >= BANK_STUCK (30%).
          The bank channel was added after the first run: in 2023 public gauges were calm (VIX ~15-20,
          normal spreads) while 45-51% of banks were net tightening, a level seen only in 1990, 2001
          and 2008. The composite averaged that away. Private exits and fund distributions, the core
          of the "drought", are not on FRED at all, so this axis is still a proxy.

  A Boom            low rates,  cash flowing
  B Lender's market high rates, cash flowing
  C Drought         high rates, cash stuck
  D Shock           low rates,  cash stuck

The thresholds are judgment calls and are printed with every run; `--sweep` shows how many
quarters change regime if they move. This is a heuristic, not a model.

Usage:
  python3 regimes.py                 # fetch (cached), classify, print annual table
  python3 regimes.py --refresh       # re-download every series
  python3 regimes.py --sweep         # threshold sensitivity
  python3 regimes.py --md            # write the markdown history table to the data folder
  python3 regimes.py --asof 2022-06-30   # only data observed by that date (no hindsight; for acumen cases)
"""
import argparse, csv, io, json, os, statistics, sys, time, urllib.request
from collections import defaultdict
from datetime import date

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw", "2026-10-04", "data", "fred")

# Series used to classify, plus context columns shown in the table.
STRESS = ["BAA10Y", "NFCI", "DRTSCILM", "VIXCLS"]
CONTEXT = ["FEDFUNDS", "T10Y3M", "PCEPILFE", "MORTGAGE30US"]
SERIES = {
    "FEDFUNDS": "Effective fed funds rate, monthly (%)",
    "BAA10Y": "Moody's Baa corporate yield minus 10y Treasury (pp)",
    "NFCI": "Chicago Fed National Financial Conditions Index (0 = average; + = tighter)",
    "DRTSCILM": "SLOOS: net % of banks tightening C&I standards, large/mid firms",
    "VIXCLS": "CBOE VIX",
    "T10Y3M": "10y minus 3m Treasury (pp); negative = inverted",
    "PCEPILFE": "Core PCE price index (for real fed funds)",
    "MORTGAGE30US": "30y fixed mortgage rate (%)",
}
RATE_HIGH = 2.5
STRESS_STUCK = 0.5
BANK_STUCK = 30.0
START = (1990, 2)
NAMES = {"A": "Boom", "B": "Lender's market", "C": "Drought", "D": "Shock"}


def fetch(sid, refresh=False):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{sid}.csv")
    if refresh or not os.path.exists(path):
        for attempt in range(4):
            try:
                with urllib.request.urlopen(FRED.format(sid), timeout=60) as r:
                    open(path, "wb").write(r.read())
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(2 ** attempt)
    rows = []
    with open(path) as f:
        for d, v in csv.reader(f):
            if d == "observation_date" or v in ("", "."):
                continue
            rows.append((date.fromisoformat(d), float(v)))
    return rows


def quarterly(rows, how="mean"):
    """Collapse observations to {(year, q): value} by mean or last observation."""
    buckets = defaultdict(list)
    for d, v in rows:
        buckets[(d.year, (d.month - 1) // 3 + 1)].append((d, v))
    out = {}
    for k, obs in buckets.items():
        obs.sort()
        out[k] = obs[-1][1] if how == "last" else statistics.fmean(v for _, v in obs)
    return out


def build(refresh=False, asof=None):
    raw = {s: fetch(s, refresh) for s in SERIES}
    if asof:
        raw = {s: [(d, v) for d, v in rows if d <= asof] for s, rows in raw.items()}
    q = {s: quarterly(raw[s]) for s in SERIES}
    q["FF_END"] = quarterly(raw["FEDFUNDS"], "last")
    core = quarterly(raw["PCEPILFE"], "last")
    q["CORE_PCE_YOY"] = {(y, k): 100 * (v / core[(y - 1, k)] - 1) for (y, k), v in core.items()
                         if (y - 1, k) in core}

    quarters = sorted(k for k in q["FF_END"] if k >= START and all(k in q[s] for s in STRESS))
    # z-scores vs. the full sample, so "stress" means stressed relative to 1990-today
    z = {}
    for s in STRESS:
        vals = [q[s][k] for k in quarters]
        mu, sd = statistics.fmean(vals), statistics.pstdev(vals)
        z[s] = {k: (q[s][k] - mu) / sd for k in quarters}

    table = []
    for k in quarters:
        comp = statistics.fmean(z[s][k] for s in STRESS)
        ff = q["FF_END"][k]
        table.append({
            "q": f"{k[0]}Q{k[1]}", "year": k[0], "ff_end": ff,
            "real_ff": ff - q["CORE_PCE_YOY"].get(k, float("nan")),
            "stress": comp, **{s: q[s][k] for s in STRESS},
            "curve": q["T10Y3M"].get(k), "mortgage": q["MORTGAGE30US"].get(k),
        })
    return table


def classify(table, rate_high=RATE_HIGH, stuck=STRESS_STUCK, bank=BANK_STUCK):
    for r in table:
        hi = r["ff_end"] >= rate_high
        r["channel"] = "market" if r["stress"] >= stuck else ("bank" if r["DRTSCILM"] >= bank else "")
        st = bool(r["channel"])
        r["regime"] = {(False, False): "A", (True, False): "B", (True, True): "C", (False, True): "D"}[(hi, st)]
    return table


def annual(table):
    by = defaultdict(list)
    for r in table:
        by[r["year"]].append(r)
    out = []
    for y, rs in sorted(by.items()):
        regs = "".join(r["regime"] for r in rs)
        dom = max("ABCD", key=regs.count)
        out.append({
            "year": y, "quarters": regs, "dominant": dom,
            "ff_end": rs[-1]["ff_end"], "real_ff": rs[-1]["real_ff"],
            "stress": statistics.fmean(r["stress"] for r in rs),
            "baa": statistics.fmean(r["BAA10Y"] for r in rs),
            "nfci": statistics.fmean(r["NFCI"] for r in rs),
            "sloos": statistics.fmean(r["DRTSCILM"] for r in rs),
            "vix": statistics.fmean(r["VIXCLS"] for r in rs),
            "curve": statistics.fmean(r["curve"] for r in rs if r["curve"] is not None),
        })
    return out


def fmt(v, p=2):
    return "n/a" if v is None or v != v else f"{v:.{p}f}"


def markdown(years, since=2005):
    lines = ["| Year | Quarters | Regime | FF end % | Real FF | Stress z | Baa spread | NFCI | SLOOS net % | VIX | 10y-3m |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for a in years:
        if a["year"] < since:
            continue
        lines.append(f"| {a['year']} | `{a['quarters']}` | {a['dominant']} {NAMES[a['dominant']]} | {fmt(a['ff_end'])} | "
                     f"{fmt(a['real_ff'])} | {fmt(a['stress'])} | {fmt(a['baa'])} | {fmt(a['nfci'])} | "
                     f"{fmt(a['sloos'], 1)} | {fmt(a['vix'], 1)} | {fmt(a['curve'])} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--md", action="store_true")
    ap.add_argument("--since", type=int, default=2005)
    ap.add_argument("--asof", type=date.fromisoformat, help="ignore observations after this date (YYYY-MM-DD)")
    a = ap.parse_args()

    table = classify(build(a.refresh, a.asof))
    years = annual(table)
    print(f"# thresholds: HIGH rates if quarter-end fed funds >= {RATE_HIGH}%; "
          f"STUCK if stress composite >= {STRESS_STUCK} (mean z of {', '.join(STRESS)}) "
          f"OR SLOOS net tightening >= {BANK_STUCK}%")
    print(f"# sample {table[0]['q']}..{table[-1]['q']} ({len(table)} quarters)"
          + (f"; as of {a.asof} (z-scores use only data to that date)" if a.asof else "") + "\n")
    print(markdown(years, a.since))

    if a.sweep:
        base = {r["q"]: r["regime"] for r in table}
        print("\n# sensitivity: quarters (since 1990) whose regime changes vs. base")
        for rh in (2.0, 2.5, 3.0):
            for st in (0.25, 0.5, 0.75):
                for bk in (20.0, 30.0, 40.0, 999.0):
                    alt = classify([dict(r) for r in table], rh, st, bk)
                    n = sum(r["regime"] != base[r["q"]] for r in alt)
                    lbl = "off" if bk > 100 else f">={bk:.0f}%"
                    print(f"  rates>={rh}%  stress>={st}  bank {lbl:5s}: {n:3d} of {len(table)} quarters change")
        classify(table)

    if a.asof:
        return
    os.makedirs(OUT, exist_ok=True)
    json.dump({"thresholds": {"rate_high": RATE_HIGH, "stress_stuck": STRESS_STUCK, "bank_stuck": BANK_STUCK, "stress_series": STRESS},
               "series": SERIES, "quarters": table, "years": years},
              open(os.path.join(OUT, "regimes.json"), "w"), indent=1, default=str)
    if a.md:
        open(os.path.join(OUT, "regime_history.md"), "w").write(markdown(years, a.since) + "\n")
        print(f"\nwrote {OUT}/regime_history.md")


if __name__ == "__main__":
    main()
