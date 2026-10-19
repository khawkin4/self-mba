#!/usr/bin/env python3
"""Build a decision-sampled backtest population from SEC XBRL frames.

The point: sample on the DECISION, not on the outcome. This enumerates every filer that
reported a qualifying decision in a period (a business combination above a pre-declared
threshold), then looks up an outcome label afterwards. No hand-picking, so no survivorship
bias — see the "Backtesting the engine" section of the mechanisms doc.

  python3 _ingest/backtest_population.py --year 2021 --min-usd 2e9 --out acq2021.json

Caveat you must not forget: goodwill impairment is a COMPANY-level fact. It is not
necessarily attributable to the deal in question, and it has low sensitivity — plenty of
failed acquisitions are never impaired. Treat the label as a screen for cases worth
reconstructing by hand, never as ground truth.
"""
import argparse, json, sys, time, urllib.request

UA = {"User-Agent": "self-mba techforge8yte@gmail.com"}
DECISION_TAGS = ["BusinessCombinationConsiderationTransferred1",
                 "PaymentsToAcquireBusinessesNetOfCashAcquired"]
OUTCOME_TAGS = ["GoodwillImpairmentLoss", "GoodwillAndIntangibleAssetImpairment"]


def frame(tag, period, unit="USD"):
    url = f"https://data.sec.gov/api/xbrl/frames/us-gaap/{tag}/{unit}/{period}.json"
    try:
        req = urllib.request.Request(url, headers=UA)
        data = json.loads(urllib.request.urlopen(req, timeout=60).read())
        return {int(x["cik"]): x for x in data.get("data", [])}
    except Exception as exc:
        print(f"  ! {tag} {period}: {exc}", file=sys.stderr)
        return {}
    finally:
        time.sleep(0.25)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2021, help="decision year")
    ap.add_argument("--min-usd", type=float, default=2e9, help="pre-declare this BEFORE looking")
    ap.add_argument("--horizon", type=int, default=4, help="years of outcome to look up")
    ap.add_argument("--out")
    a = ap.parse_args()

    decisions = {}
    for tag in DECISION_TAGS:
        f = frame(tag, f"CY{a.year}")
        print(f"{tag} CY{a.year}: {len(f)} filers", file=sys.stderr)
        for cik, r in f.items():
            if r["val"] > decisions.get(cik, {}).get("val", 0):
                decisions[cik] = {**r, "tag": tag}

    pop = {c: r for c, r in decisions.items() if r["val"] >= a.min_usd}
    print(f"population: {len(pop)} of {len(decisions)} at >= ${a.min_usd/1e9:g}B", file=sys.stderr)

    impair = {}
    for yr in range(a.year + 1, a.year + 1 + a.horizon):
        for tag in OUTCOME_TAGS:
            for cik, r in frame(tag, f"CY{yr}").items():
                impair.setdefault(cik, {})
                impair[cik][yr] = max(impair[cik].get(yr, 0), r["val"])

    rows = []
    for cik, d in pop.items():
        years = impair.get(cik, {})
        total = sum(years.values())
        ratio = total / d["val"] if d["val"] else 0.0
        label = ("failed" if ratio >= 0.50 else "partial" if ratio >= 0.10 else "no-signal")
        rows.append({"cik": cik, "company": d["entityName"], "decision_usd": d["val"],
                     "impairment_usd": total, "ratio": round(ratio, 3), "label": label,
                     "impairment_years": sorted(years), "decision_tag": d["tag"],
                     "attributable": None})   # <- fill by hand; see the caveat above
    rows.sort(key=lambda r: -r["ratio"])

    counts = {}
    for r in rows:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    print("labels:", counts, file=sys.stderr)

    out = {"decision_year": a.year, "min_usd": a.min_usd, "horizon_years": a.horizon,
           "population_size": len(rows), "label_counts": counts, "cases": rows}
    text = json.dumps(out, indent=1)
    if a.out:
        open(a.out, "w").write(text)
        print(f"wrote {a.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
