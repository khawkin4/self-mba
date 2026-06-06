#!/usr/bin/env python3
"""Research the 5 benchmark gap domains (MFT-MBA scorecard) — pull lecture transcripts
+ Reddit into raw/2026-06-05/gaps/<area>/ so build.py sees one unified corpus.
Targets the technical/compliance half the great-books canon under-covers.

Run:  python3 _ingest/_research_gaps.py     (writes to the existing date dir)
"""
import os, subprocess, sys, time

HOME = os.path.expanduser("~")
RESEARCH = os.path.join(HOME, "research-kit", ".venv", "bin", "research")
OUT = os.path.join(HOME, "self-mba", "_ingest", "raw", "2026-06-05", "gaps")

# area -> {yt: [...queries], reddit: [{sub, q?}]}
GAPS = {
    "managerial-accounting": {
        "yt": ["Edspira managerial accounting cost behavior CVP analysis",
               "activity based costing explained example",
               "variance analysis standard costing explained",
               "Accounting Stuff managerial accounting basics"],
        "reddit": [{"sub": "Accounting"}],
    },
    "statistics-quant": {
        "yt": ["StatQuest hypothesis testing clearly explained",
               "StatQuest linear regression clearly explained",
               "StatQuest p-values and confidence intervals",
               "business statistics for managers regression forecasting"],
        "reddit": [{"sub": "statistics", "q": "intuition hypothesis testing"}],
    },
    "marketing-strategy": {
        "yt": ["April Dunford positioning obviously awesome",
               "Byron Sharp How Brands Grow laws of growth",
               "segmentation targeting positioning STP marketing explained",
               "customer lifetime value CAC unit economics explained"],
        "reddit": [{"sub": "marketing"}],
    },
    "information-systems": {
        "yt": ["management information systems explained MBA",
               "ERP enterprise systems explained business",
               "relational database fundamentals explained",
               "data governance and data management basics"],
        "reddit": [{"sub": "BusinessIntelligence"}],
    },
    "business-law": {
        "yt": ["business law basics contracts explained",
               "intellectual property law for business explained",
               "employment law basics for managers",
               "antitrust competition law explained"],
        "reddit": [{"sub": "smallbusiness", "q": "legal contracts"}],
    },
}

def slug(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower())[:60].strip("-")

def run(cmd, outfile, timeout=900):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.stdout.strip():
            open(outfile, "w", encoding="utf-8").write(r.stdout); return True
        sys.stderr.write(f"   ! empty: {' '.join(cmd[-3:])}\n")
    except Exception as ex:
        sys.stderr.write(f"   ! {ex}\n")
    return False

def main():
    ok_y = ok_r = 0
    for area, spec in GAPS.items():
        d = os.path.join(OUT, area); os.makedirs(d, exist_ok=True)
        for q in spec["yt"]:
            sys.stderr.write(f"[{area}] yt: {q!r}\n")
            if run([RESEARCH, "yt", q, "-n", "2", "--score", "--transcripts"],
                   os.path.join(d, f"yt_{slug(q)}.json")):
                ok_y += 1
            time.sleep(1.5)
        for rd in spec["reddit"]:
            sub, qq = rd["sub"], rd.get("q")
            if qq:
                cmd = [RESEARCH, "reddit", qq, "--sub", sub, "-n", "12", "--score"]
                label = f"{sub}_{slug(qq)}"
            else:
                cmd = [RESEARCH, "reddit", "--sub", sub, "--listing", "top", "--time", "year", "-n", "12", "--score"]
                label = sub
            sys.stderr.write(f"[{area}] reddit: r/{sub}\n")
            if run(cmd, os.path.join(d, f"reddit_{label}.json"), timeout=300):
                ok_r += 1
            time.sleep(1.0)
    print(f"DONE: {ok_y} yt files, {ok_r} reddit files across {len(GAPS)} gap areas", file=sys.stderr)

if __name__ == "__main__":
    main()
