#!/usr/bin/env python3
"""
EDGAR fetcher for the Compounding MBA — primary-source financials from the SEC.

Stdlib only (no pip). Hits the public SEC EDGAR APIs:
  - ticker -> CIK map:   https://www.sec.gov/files/company_tickers.json
  - filing index:        https://data.sec.gov/submissions/CIK##########.json
  - XBRL company facts:  https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
  - full-text search:    https://efts.sec.gov/LATEST/search-index?q=...

SEC requires a descriptive User-Agent with contact info (their fair-access rule).
Set EDGAR_UA env var to "Name email@example.com", or it falls back to a generic one.

Usage:
  python3 edgar.py company AAPL          # overview + latest filings + key financials
  python3 edgar.py filings AAPL --form 10-K --n 5
  python3 edgar.py facts AAPL            # dump selected XBRL fundamentals as JSON
  python3 edgar.py search "going concern" --n 10   # full-text search across filings
"""
import json, os, sys, time, urllib.request, urllib.parse, argparse

UA = os.environ.get("EDGAR_UA", "Compounding-MBA research self-mba@example.com")
HEADERS = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate", "Host": None}

def _get(url, host=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if host:
        req.add_header("Host", host)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                enc = r.headers.get("Content-Encoding", "")
                if enc == "gzip":
                    import gzip; raw = gzip.decompress(raw)
                return raw.decode("utf-8", "replace")
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(0.6 * (attempt + 1))  # SEC rate limit ~10 req/s; back off politely

_TICKERS = None
def cik_for(ticker):
    global _TICKERS
    if _TICKERS is None:
        data = json.loads(_get("https://www.sec.gov/files/company_tickers.json"))
        _TICKERS = {v["ticker"].upper(): (v["cik_str"], v["title"]) for v in data.values()}
    t = ticker.upper()
    if t.isdigit():
        return int(t), None
    if t not in _TICKERS:
        sys.exit(f"Unknown ticker: {ticker}")
    return _TICKERS[t]

def submissions(cik):
    cik10 = str(cik).zfill(10)
    return json.loads(_get(f"https://data.sec.gov/submissions/CIK{cik10}.json"))

def company_facts(cik):
    cik10 = str(cik).zfill(10)
    return json.loads(_get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json"))

def full_text_search(q, n=10):
    url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode({"q": q})
    data = json.loads(_get(url))
    hits = data.get("hits", {}).get("hits", [])[:n]
    out = []
    for h in hits:
        s = h.get("_source", {})
        out.append({
            "form": s.get("file_type") or s.get("root_form"),
            "company": (s.get("display_names") or ["?"])[0],
            "date": s.get("file_date"),
            "id": h.get("_id"),
        })
    return out

# A small, high-signal set of XBRL tags for a first-pass fundamentals read.
KEY_TAGS = {
    "Revenues": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"],
    "NetIncome": ["NetIncomeLoss"],
    "Assets": ["Assets"],
    "Liabilities": ["Liabilities"],
    "Equity": ["StockholdersEquity"],
    "OperatingCashFlow": ["NetCashProvidedByUsedInOperatingActivities"],
    "GrossProfit": ["GrossProfit"],
}

def latest_facts(facts):
    us = facts.get("facts", {}).get("us-gaap", {})
    out = {}
    for label, tags in KEY_TAGS.items():
        # Companies switch XBRL tags over time, so pool ALL candidate tags and pick the
        # single most-recent annual figure across them (not the first tag that has data).
        pooled = []
        for tag in tags:
            node = us.get(tag)
            if not node:
                continue
            for x in node.get("units", {}).get("USD", []):
                pooled.append((tag, x))
        if not pooled:
            continue
        annual = [(t, x) for (t, x) in pooled if x.get("fp") == "FY" and x.get("form", "").startswith("10-K")]
        chosen = annual or pooled
        tag, last = max(chosen, key=lambda tx: tx[1].get("end", ""))
        out[label] = {"value": last.get("val"), "end": last.get("end"), "tag": tag}
    return out

def cmd_company(args):
    cik, title = cik_for(args.ticker)
    sub = submissions(cik)
    name = sub.get("name", title)
    print(f"# {name}  (CIK {cik})")
    print(f"  SIC: {sub.get('sicDescription')}  ·  Exchange: {', '.join(sub.get('exchanges', []) or [])}")
    recent = sub.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accs = recent.get("accessionNumber", [])
    print("\n## Recent key filings")
    wanted = {"10-K", "10-Q", "8-K", "DEF 14A"}
    shown = 0
    for f, d, a in zip(forms, dates, accs):
        if f in wanted:
            acc = a.replace("-", "")
            url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={urllib.parse.quote(f)}"
            print(f"  {d}  {f:8s}  acc:{a}")
            shown += 1
            if shown >= 12:
                break
    print("\n## Key financials (latest annual, XBRL)")
    try:
        lf = latest_facts(company_facts(cik))
        for k, v in lf.items():
            val = v["value"]
            disp = f"${val/1e9:,.2f}B" if isinstance(val, (int, float)) and abs(val) >= 1e8 else f"{val:,}"
            print(f"  {k:18s} {disp:>14s}   (FY end {v['end']})")
    except Exception as e:
        print(f"  (facts unavailable: {e})")

def cmd_filings(args):
    cik, _ = cik_for(args.ticker)
    sub = submissions(cik)
    recent = sub.get("filings", {}).get("recent", {})
    rows = list(zip(recent.get("form", []), recent.get("filingDate", []),
                    recent.get("accessionNumber", []), recent.get("primaryDocument", [])))
    rows = [r for r in rows if (not args.form or r[0] == args.form)][:args.n]
    for form, date, acc, doc in rows:
        accn = acc.replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/{doc}"
        print(f"{date}  {form:8s}  {url}")

def cmd_facts(args):
    cik, _ = cik_for(args.ticker)
    print(json.dumps(latest_facts(company_facts(cik)), indent=2))

def cmd_search(args):
    for h in full_text_search(args.query, args.n):
        print(f"{h['date']}  {str(h['form']):8s}  {h['company']}")

def main():
    p = argparse.ArgumentParser(description="SEC EDGAR fetcher for the Compounding MBA")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("company"); c.add_argument("ticker"); c.set_defaults(fn=cmd_company)
    f = sub.add_parser("filings"); f.add_argument("ticker"); f.add_argument("--form"); f.add_argument("--n", type=int, default=10); f.set_defaults(fn=cmd_filings)
    x = sub.add_parser("facts"); x.add_argument("ticker"); x.set_defaults(fn=cmd_facts)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--n", type=int, default=10); s.set_defaults(fn=cmd_search)
    args = p.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()
