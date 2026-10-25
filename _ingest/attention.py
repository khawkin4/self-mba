#!/usr/bin/env python3
"""Cross-company attention map: tag every newsroom article with shared topics.

Reads each company's scraped corpus (_ingest/raw/<company>/articles*.jsonl),
scores every article against the regex keywords in attention_taxonomy.json,
and writes per-article tags plus company x topic and company x year x topic
share-of-voice tables to _ingest/raw/attention/.

Scoring: a keyword hit in the title counts TITLE_WEIGHT; hits in the first
BODY_WINDOW characters of the body count 1 each. A topic is tagged when its
score reaches the threshold. Long documents (letters, transcripts) are scored
on the window only, so they don't tag every topic.

    python3 _ingest/attention.py               # tag + aggregate
    python3 _ingest/attention.py --validate    # compare with blind labels
"""
import argparse, collections, csv, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(RAW, "attention")
COMPANIES = ["tradeweb", "ice", "marketaxess", "bloomberg", "spglobal", "lseg",
             "thomsonreuters", "goldman", "jpmc", "blackrock"]
FILTERED = {"goldman", "jpmc", "blackrock"}  # corpora pre-filtered to the market-structure lens
TITLE_WEIGHT = 3
BODY_WINDOW = 6000
THRESHOLD = 3
# Per-topic thresholds, tuned against 160 blind-labelled articles (validation_labels.jsonl).
# Topics with <5 gold examples (mortgage, listings, payments, private markets, fees, risk)
# use moderate values rather than the in-sample optimum.
TOPIC_THRESHOLD = {"credit": 6, "rates": 5, "derivs_clearing": 8, "equities_etf": 7,
                   "commodities_energy": 5, "mortgage_lending": 6, "listings_ipo": 6,
                   "indices_benchmarks": 8, "pricing_data": 8, "workflow_desktop": 3,
                   "electronification": 6, "ai": 4, "digital_assets": 3, "private_markets": 5,
                   "esg_climate": 3, "regulation_policy": 5, "deals_capital": 3,
                   "people_culture": 3, "fees_pricing_power": 2, "risk_resilience": 3,
                   "international": 6, "retail_wealth": 6, "payments_banking": 5,
                   "ratings_research": 3}


def load_taxonomy():
    tax = json.load(open(os.path.join(HERE, "attention_taxonomy.json")))["topics"]
    return {k: [re.compile(p, re.I) for p in v["keywords"]] for k, v in tax.items()}, tax


def year_of(rec):
    m = re.search(r"(20[012]\d)", str(rec.get("date", "")))
    if m:
        return int(m.group(1))
    m = re.search(r"(January|February|March|April|May|June|July|August|September|October|"
                  r"November|December) \d{1,2},? (20[12]\d)", rec.get("text", "")[:3000])
    return int(m.group(2)) if m else None


BOILERPLATE = re.compile(r"\bAbout (Tradeweb|Intercontinental Exchange|ICE\b|MarketAxess|Bloomberg|S&P Global|"
                         r"London Stock Exchange|LSEG|Thomson Reuters|Goldman Sachs|JPMorgan|J\.P\. Morgan|BlackRock)")


def body_of(rec):
    """Body text up to the corporate 'About us' boilerplate, capped at BODY_WINDOW."""
    text = rec.get("text", "") or ""
    m = BOILERPLATE.search(text, 200)
    return text[:m.start()][:BODY_WINDOW] if m else text[:BODY_WINDOW]


def score(rec, pats, thresholds=None):
    th = thresholds or TOPIC_THRESHOLD
    title, body = rec.get("title", "") or "", body_of(rec)
    out = {}
    for topic, rx in pats.items():
        s = sum(TITLE_WEIGHT * len(p.findall(title)) + len(p.findall(body)) for p in rx)
        if s >= th.get(topic, THRESHOLD):
            out[topic] = s
    return out


def corpus(company):
    path = sorted(glob.glob(os.path.join(RAW, company, "articles*.jsonl")))[0]
    for i, line in enumerate(open(path)):
        if line.strip():
            yield i, json.loads(line)


def run():
    pats, tax = load_taxonomy()
    os.makedirs(OUT, exist_ok=True)
    topics = list(pats)
    rows, by_co, by_year = [], collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    n_co, n_year = collections.Counter(), collections.Counter()
    for c in COMPANIES:
        for i, r in corpus(c):
            tags = score(r, pats)
            y = year_of(r)
            rows.append({"id": f"{c}:{i}", "company": c, "year": y or "", "type": r.get("type", ""),
                         "title": (r.get("title") or "")[:160], "topics": ";".join(sorted(tags))})
            n_co[c] += 1
            by_co[c].update(tags.keys())
            if y and 2019 <= y <= 2026:
                n_year[(c, y)] += 1
                by_year[(c, y)].update(tags.keys())
    with open(os.path.join(OUT, "article_tags.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(OUT, "share_by_company.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["company", "articles", "filtered_corpus"] + topics)
        for c in COMPANIES:
            w.writerow([c, n_co[c], c in FILTERED] + [round(100 * by_co[c][t] / n_co[c], 1) for t in topics])
    with open(os.path.join(OUT, "share_by_year.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["company", "year", "articles"] + topics)
        for (c, y) in sorted(n_year):
            n = n_year[(c, y)]
            w.writerow([c, y, n] + [round(100 * by_year[(c, y)][t] / n, 1) for t in topics])
    print(f"tagged {len(rows)} articles; untagged {sum(1 for r in rows if not r['topics'])}")
    print(f"wrote {OUT}/article_tags.csv, share_by_company.csv, share_by_year.csv")


def validate():
    pats, _ = load_taxonomy()
    gold = {json.loads(l)["id"]: set(json.loads(l)["topics"]) for l in open(os.path.join(OUT, "validation_labels.jsonl"))}
    recs = {}
    for c in COMPANIES:
        for i, r in corpus(c):
            if f"{c}:{i}" in gold:
                recs[f"{c}:{i}"] = r
    tp, fp, fn = collections.Counter(), collections.Counter(), collections.Counter()
    for aid, g in gold.items():
        p = set(score(recs[aid], pats))
        for t in p & g: tp[t] += 1
        for t in p - g: fp[t] += 1
        for t in g - p: fn[t] += 1
    print(f"{'topic':22} {'prec':>5} {'rec':>5} {'f1':>5}  tp fp fn")
    T = P = R = 0
    for t in sorted(pats):
        pr = tp[t] / (tp[t] + fp[t]) if tp[t] + fp[t] else 0
        rc = tp[t] / (tp[t] + fn[t]) if tp[t] + fn[t] else 0
        f1 = 2 * pr * rc / (pr + rc) if pr + rc else 0
        print(f"{t:22} {pr:5.2f} {rc:5.2f} {f1:5.2f}  {tp[t]:2} {fp[t]:2} {fn[t]:2}")
    a, b, c_ = sum(tp.values()), sum(fp.values()), sum(fn.values())
    pr, rc = a / (a + b), a / (a + c_)
    print(f"{'MICRO':22} {pr:5.2f} {rc:5.2f} {2*pr*rc/(pr+rc):5.2f}  {a} {b} {c_}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--validate", action="store_true")
    validate() if ap.parse_args().validate else run()
