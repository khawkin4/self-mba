#!/usr/bin/env python3
"""Say-vs-do audit: newsroom attention vs FY2025 revenue mix, and 10-K risks vs newsroom silence.

Inputs:  raw/attention/article_tags.csv  (from attention.py)
         raw/audit/<ticker>.json          (FY2019/FY2025 revenue lines + FY2025 risk factors)
         raw/<company>/articles*.jsonl    (for the silence keyword scan)
Outputs: raw/audit/revenue_by_topic.csv, attention_vs_revenue.csv, silence.csv

The line -> topic map below is explicit so every revenue number can be traced to a
filing line. Lines mapped to "other" (news, FX, investment-banking advisory, corporate
treasury, eliminations) are excluded from the comparison and reported as such.
Bloomberg is private and discloses no revenue, so it has no say-vs-do row.
"""
import collections, csv, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
AUD = os.path.join(RAW, "audit")
RECENT = (2023, 2026)  # attention window compared with FY2025 revenue
BUSINESS_TOPICS = ["credit", "rates", "derivs_clearing", "equities_etf", "commodities_energy",
                   "mortgage_lending", "listings_ipo", "indices_benchmarks", "pricing_data",
                   "workflow_desktop", "ratings_research", "private_markets", "retail_wealth",
                   "payments_banking", "ai", "digital_assets"]

# company -> (audit file, {line-prefix: topic}); only FY2025 leaf lines that sum to the total.
REVENUE_MAP = {
    "tradeweb": ("tw", {"Rates –": "rates", "Money Markets –": "rates", "Credit –": "credit",
                        "Equities –": "equities_etf", "Market Data –": "pricing_data", "Other –": "other"}),
    "marketaxess": ("mktx", {"Commissions – variable transaction fees – Credit": "credit",
                             "Commissions – fixed distribution fees – Credit": "credit",
                             "Commissions – variable transaction fees – Rates": "rates",
                             "Commissions – fixed distribution fees – Rates": "rates",
                             "Commissions – variable transaction fees – Other": "other",
                             "Information services": "pricing_data", "Post-trade services": "other",
                             "Technology services": "workflow_desktop"}),
    "ice": ("ice", {"Exchanges – Energy": "commodities_energy", "Exchanges – Agricultural": "commodities_energy",
                    "Exchanges – Financial futures": "derivs_clearing", "Exchanges – OTC": "derivs_clearing",
                    "Exchanges – Cash equities": "equities_etf", "Exchanges – Data and connectivity": "pricing_data",
                    "Exchanges – Listings": "listings_ipo", "Fixed Income and Data Services – Fixed income execution": "credit",
                    "Fixed Income and Data Services – CDS clearing": "derivs_clearing",
                    "Fixed Income and Data Services – Fixed income data": "pricing_data",
                    "Fixed Income and Data Services – Data and network": "workflow_desktop",
                    "Mortgage Technology –": "mortgage_lending"}),
    "spglobal": ("spgi", {"Ratings": "ratings_research", "Market Intelligence": "pricing_data",
                          "Platts (FY2019) / Energy": "commodities_energy", "Mobility": "other",
                          "Indices (S&P Dow Jones Indices)": "indices_benchmarks",
                          "Intersegment elimination": "other"}),
    "blackrock": ("blk", {"Base fees – Equity: iShares": "equities_etf", "Base fees – Fixed income: iShares": "equities_etf",
                          "Base fees – Equity: Active": "equities_etf", "Base fees – Fixed income: Active": "credit",
                          "Base fees – Non-ETF index": "equities_etf", "Base fees – Multi-asset": "retail_wealth",
                          "Base fees – Alternatives": "private_markets", "Base fees – Currency": "commodities_energy",
                          "Base fees – Cash management": "rates", "Investment advisory performance fees": "private_markets",
                          "Technology services": "workflow_desktop", "Distribution fees": "retail_wealth",
                          "Advisory and other": "other"}),
    "thomsonreuters": ("tri", {"Legal Professionals": "workflow_desktop", "Corporates": "workflow_desktop",
                               "Tax & Accounting": "workflow_desktop", "Reuters News": "other",
                               "Global Print": "other", "Eliminations": "other"}),
    "lseg": ("lseg", {"Data & Analytics – Workflows": "workflow_desktop", "Data & Analytics – Data & Feeds": "pricing_data",
                      "Data & Analytics – Analytics": "pricing_data", "FTSE Russell": "indices_benchmarks",
                      "Risk Intelligence": "other", "Secondary Markets – Fixed income": "rates",
                      "Markets – Equities": "equities_etf", "Markets – FX": "other",
                      "LCH – OTC": "derivs_clearing", "Net Treasury Income": "derivs_clearing",
                      "Markets – Securities": "derivs_clearing", "Markets – Non-Cash": "derivs_clearing",
                      "Other": "other"}),
    "goldman": ("gs", {"Advisory": "other", "Equity underwriting": "listings_ipo", "Debt underwriting": "credit",
                       "FICC": "rates", "Equities": "equities_etf", "Other": "other",
                       "Management and other fees": "retail_wealth", "Incentive fees": "private_markets",
                       "Private banking": "retail_wealth", "Investments": "private_markets",
                       "Platform Solutions": "retail_wealth"}),
    "jpmc": ("jpm", {"Banking & Wealth": "retail_wealth", "Home Lending": "mortgage_lending",
                     "Card Services": "retail_wealth", "Investment Banking": "other", "Payments": "payments_banking",
                     "Lending": "credit", "Other": "other", "Fixed Income Markets": "rates",
                     "Equity Markets": "equities_etf", "Securities Services": "payments_banking",
                     "Credit Adjustments": "other", "Asset Management": "retail_wealth",
                     "Global Private Bank": "retail_wealth", "Corporate": "other"}),
}
# ICE line items are gross; subtract transaction-based expenses (mostly cash-equity rebates
# and Section 31 fees) from cash equities so the mix reflects net revenue.
ICE_TBE_FY25 = 12640 - 9931
# LSEG Markets segment total and the D&A segment total double-count their sub-lines.
SKIP_LINES = {"lseg": ["Markets (total income", "Data & Analytics (excl", "Recoveries"],
              "spglobal": [], "blackrock": ["Total base fees"], "thomsonreuters": []}

# Risk themes for the silence audit: 10-K theme -> newsroom keyword pattern (any mention counts).
SILENCE = {
    "cyber": r"cyber|ransomware|data breach|hack",
    "operational_outage": r"outage|downtime|disruption to (our|the) (platform|service)|operational resilien|business continuity",
    "competition": r"\bcompetit(or|ion|ive pressure)",
    "fee_pressure": r"fee (pressure|compression|cut)|pricing pressure|price (cut|reduction)|lower fees|fee per million|take rate",
    "controlling_shareholder_related_party": r"controlling (shareholder|stake|interest)|majority[- ]owned|related[- ]party",
    "key_clients_concentration": r"largest (clients|customers)|client concentration|customer concentration",
    "market_volatility_dependence": r"\bvolatil",
    "regulation": r"regulat",
    "technology_change_ai": r"disrupt|artificial intelligence|\bAI\b",
    "litigation": r"litigation|lawsuit|settlement with|\bfined?\b|penalt",
    "talent_key_people": r"talent|key (personnel|people|employees)|retain (our )?(people|employees)",
    "debt_leverage": r"\bleverage\b|debt|senior notes|credit rating of (the company|ICE|LSEG)",
    "international_fx_geopolitics": r"geopolit|sanction|exchange rate|currency (risk|fluctuation)|tariff",
    "climate_esg": r"climate|\bESG\b",
    "acquisitions_integration": r"integration|acqui",
    "data_ip_licensing": r"intellectual property|licen[cs]",
}
CORPUS = {"tradeweb": "tw", "ice": "ice", "marketaxess": "mktx", "spglobal": "spgi", "lseg": "lseg",
          "thomsonreuters": "tri", "goldman": "gs", "jpmc": "jpm", "blackrock": "blk"}


def revenue_by_topic(company):
    ticker, mapping = REVENUE_MAP[company]
    d = json.load(open(os.path.join(AUD, f"{ticker}.json")))
    out, unmatched = collections.Counter(), []
    for ln in d["revenue_lines"]:
        name, v = ln["line"], ln.get("fy2025")
        if v is None or ln.get("level") in ("subtotal", "memo") or any(name.startswith(s) for s in SKIP_LINES.get(company, [])):
            continue
        if company in ("spglobal", "thomsonreuters") and ln.get("level") == "sub":
            continue  # use segment totals
        if company == "lseg" and ln.get("level") == "segment" and not name.startswith(("FTSE Russell", "Risk Intelligence", "Other")):
            continue  # LSEG FY25 detail lives in sub-lines
        if company == "lseg" and name.startswith("FTSE Russell –"):
            continue
        if company == "blackrock" and ln.get("level") == "sub":
            continue
        topic = next((t for p, t in mapping.items() if name.startswith(p)), None)
        if topic is None:
            unmatched.append(name); continue
        if company == "ice" and name.startswith("Exchanges – Cash equities"):
            v -= ICE_TBE_FY25
        out[topic] += v
    total = d["total_revenue"]["fy2025"]
    if company == "ice":
        total = d["total_revenue"]["net_of_transaction_based_expenses"]["fy2025"]
    return out, total, unmatched


def attention_share(company):
    tags = collections.Counter()
    for r in csv.DictReader(open(os.path.join(RAW, "attention", "article_tags.csv"))):
        if r["company"] == company and r["year"] and RECENT[0] <= int(r["year"]) <= RECENT[1]:
            tags.update(t for t in r["topics"].split(";") if t in BUSINESS_TOPICS)
    n = sum(tags.values())
    return {t: 100 * tags[t] / n for t in BUSINESS_TOPICS} if n else {}


def silence(company):
    path = sorted(glob.glob(os.path.join(RAW, company, "articles*.jsonl")))[0]
    texts = [json.loads(l).get("text", "") for l in open(path) if l.strip()]
    d = json.load(open(os.path.join(AUD, f"{CORPUS[company]}.json")))
    risk = collections.Counter(r["theme"] for r in d["risk_factors"])
    rows = []
    for theme, pat in SILENCE.items():
        rx = re.compile(pat, re.I)
        pct = 100 * sum(1 for t in texts if rx.search(t)) / len(texts)
        rows.append((theme, risk.get(theme, 0), round(pct, 1)))
    return rows, len(d["risk_factors"])


def main():
    with open(os.path.join(AUD, "revenue_by_topic.csv"), "w", newline="") as f, \
         open(os.path.join(AUD, "attention_vs_revenue.csv"), "w", newline="") as g:
        wf, wg = csv.writer(f), csv.writer(g)
        wf.writerow(["company", "topic", "fy2025_revenue_m", "share_of_total_pct"])
        wg.writerow(["company", "topic", "attention_pct_2023_26", "revenue_pct_fy25", "gap_pp", "excluded_revenue_pct"])
        for c in REVENUE_MAP:
            rev, total, unmatched = revenue_by_topic(c)
            if unmatched:
                print(f"  {c}: unmatched lines {unmatched}")
            mapped = sum(v for t, v in rev.items() if t != "other")
            excl = round(100 * rev.get("other", 0) / total, 1)
            for t, v in sorted(rev.items(), key=lambda kv: -kv[1]):
                wf.writerow([c, t, round(v, 1), round(100 * v / total, 1)])
            att = attention_share(c)
            for t in BUSINESS_TOPICS:
                a, r = att.get(t, 0), 100 * rev.get(t, 0) / mapped
                if a >= 1 or r >= 1:
                    wg.writerow([c, t, round(a, 1), round(r, 1), round(a - r, 1), excl])
            print(f"{c:15} total {total:>9,.0f}  mapped {mapped:>9,.0f}  check {sum(rev.values()):>9,.0f}  excluded {excl}%")
    with open(os.path.join(AUD, "silence.csv"), "w", newline="") as h:
        w = csv.writer(h)
        w.writerow(["company", "risk_theme", "risk_factors_in_filing", "newsroom_mention_pct"])
        for c in CORPUS:
            rows, n = silence(c)
            for theme, k, pct in rows:
                w.writerow([c, theme, k, pct])
    print("wrote revenue_by_topic.csv, attention_vs_revenue.csv, silence.csv")


if __name__ == "__main__":
    main()
