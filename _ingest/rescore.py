#!/usr/bin/env python3
"""
Educational re-scorer for the Reddit corpus.

The `research` kit ships a PAIN scorer (built to surface customer complaints for
product research) — exactly the wrong objective for a learning corpus, so it
flags venting/drama as "signal". This re-scores every Reddit post for EDUCATIONAL
value instead, writes a curated, filtered set, and reports the signal lift.

Reads:  _ingest/raw/<latest>/<track>/<module>/reddit_*.json
Writes: _ingest/raw/<latest>/<track>/<module>/curated_reddit.json  (kept posts, ranked)
        per-post "edu_score" + "edu_reasons"

Usage: python3 _ingest/rescore.py [--keep 8] [--min 3]
"""
import argparse, glob, json, os, re

HOME = os.path.expanduser("~")
INGEST = os.path.join(HOME, "self-mba", "_ingest")

LEARN = re.compile(r"\b(how (do|does|to|did)|why (is|are|does|do|did)|what(?:'s| is| are)|explain|"
                   r"framework|guide|walkthrough|breakdown|difference between|when (to|should)|"
                   r"best way|lessons? (learned|from)|case study|mental model|rule of thumb|"
                   r"deep dive|understand|intuition|first principles|playbook)\b", re.I)
VENT = re.compile(r"\b(toxic|i hate|hate my|quit|got fired|getting fired|cooked|fuck|fucking|stupid|"
                  r"rant|vent|burnout|burnt out|wtf|scam|nightmare|miserable|underpaid|layoff|laid off|"
                  r"drama|aita|am i the|circlejerk|meme|shitpost|depressed|crying)\b", re.I)
MEH = re.compile(r"\b(weekly thread|daily thread|megathread|moronic monday|stupid question|"
                 r"who's hiring|resume review|salary sharing|rate my)\b", re.I)

def score(p):
    title = p.get("title", "") or ""
    body = (p.get("selftext", "") or "")
    ups = int(float(p.get("ups", 0) or 0))
    comments = int(float(p.get("comments", 0) or 0))
    s, why = 0, []
    if LEARN.search(title): s += 3; why.append("teaches/explains")
    if LEARN.search(body): s += 1
    if len(body) > 1200: s += 2; why.append("substantive write-up")
    elif len(body) > 400: s += 1
    if ups >= 100 and comments >= 30: s += 2; why.append("high engagement")
    elif ups >= 30 and comments >= 10: s += 1
    if comments >= 80: s += 1; why.append("rich discussion")
    if VENT.search(title): s -= 3; why.append("venting/drama (penalized)")
    if MEH.search(title): s -= 2; why.append("low-content thread")
    if len(title) < 25 and not LEARN.search(title): s -= 1
    return max(s, 0), why

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", type=int, default=8, help="max curated posts per module")
    ap.add_argument("--min", type=int, default=3, help="min edu_score to keep")
    a = ap.parse_args()
    raw = sorted(glob.glob(os.path.join(INGEST, "raw", "*")))[-1]

    tot = kept = 0
    lift_rows = []
    for mdir in sorted(glob.glob(os.path.join(raw, "*", "*"))):
        posts = []
        for f in glob.glob(os.path.join(mdir, "reddit_*.json")):
            try: posts += json.load(open(f))
            except Exception: pass
        if not posts: continue
        for p in posts:
            p["edu_score"], p["edu_reasons"] = score(p)
        tot += len(posts)
        good = sorted([p for p in posts if p["edu_score"] >= a.min],
                      key=lambda p: p["edu_score"], reverse=True)[:a.keep]
        kept += len(good)
        mod = os.path.basename(mdir)
        lift_rows.append((mod, len(posts), len(good)))
        json.dump(good, open(os.path.join(mdir, "curated_reddit.json"), "w"), indent=2)

    print(f"=== EDUCATIONAL RE-SCORE ===")
    print(f"  {tot} posts in -> {kept} curated kept ({100*kept//max(tot,1)}% — the rest was noise)")
    print(f"  modules with ZERO educational posts (Reddit should be cut there):")
    for mod, n, k in lift_rows:
        if k == 0: print(f"    {mod}  ({n} posts, none qualified)")
    print(f"  strongest Reddit modules:")
    for mod, n, k in sorted(lift_rows, key=lambda x: -x[2])[:6]:
        print(f"    {mod}: {k} kept / {n}")

if __name__ == "__main__":
    main()
