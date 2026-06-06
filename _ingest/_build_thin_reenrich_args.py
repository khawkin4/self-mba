#!/usr/bin/env python3
"""Work-list for re-enriching the corpus-thin canon notes after the targeted re-pull.
Selects notes still flagged 'corpus thin' and points each at its cluster raw dir
(which now also holds yt_fix_*.json from _repull_thin.py).
Emits JSON: {notes:[{note, book, clusterName, clusterSlug, rawDir, fixFiles}]}
"""
import glob, json, os, re

ROOT = os.path.expanduser("~/self-mba")
NOTES = os.path.join(ROOT, "notes", "canon")
RAW = os.path.join(ROOT, "_ingest", "raw", "2026-06-05", "canon")
NAME2SLUG = {
    "Strategy": "strategy", "Leadership & Presence": "leadership-presence",
    "Mental Models & Thinking": "mental-models", "Org Design & Mechanisms": "org-design-mechanisms",
    "Landscape & Competitive Awareness": "landscape-competitive", "Negotiation & Influence": "negotiation-influence",
    "Execution & Operations": "execution-operations", "Culture & Change": "culture-change",
    "Risk, Uncertainty & Fragility": "risk-fragility", "Product Thinking & Innovation": "product-innovation",
    "Power & Organizational Politics": "power-politics", "Personal Effectiveness": "personal-effectiveness",
    "Financial Literacy for Operators": "financial-literacy", "Behavioral Design & Decision Science": "behavioral-decision",
    "Game Theory & Strategic Interaction": "game-theory", "Network Effects & Platform Strategy": "platform-strategy",
    "Systems Thinking & Complexity": "systems-complexity", "Information & Communication": "information-communication",
    "Economics & Incentive Design": "economics-incentives", "History & Judgment": "history-judgment",
    "Communication & Storytelling": "communication-storytelling", "Design Thinking & Problem-Solving": "design-problem-solving",
    "Ethics & Judgment": "ethics-judgment",
}
out = []
for p in sorted(glob.glob(os.path.join(NOTES, "canon-*.md"))):
    txt = open(p, encoding="utf-8").read()
    if "corpus thin" not in txt:
        continue
    m = re.search(r"Cluster:\s*(.+?)\s*·", txt)
    slug = NAME2SLUG.get(m.group(1).strip()) if m else None
    rawdir = os.path.join(RAW, slug) if slug else ""
    book = os.path.basename(p)[:-3]
    fix = os.path.join(rawdir, f"yt_fix_{book.replace('canon-', '')}.json")
    out.append({"note": p, "book": book, "clusterName": m.group(1).strip() if m else "?",
                "clusterSlug": slug, "rawDir": rawdir,
                "fixFile": fix if os.path.exists(fix) else "", "hasFix": os.path.exists(fix)})

dest = os.path.join(ROOT, "_ingest", "canon_reenrich_args.json")
json.dump({"notes": out}, open(dest, "w"), indent=2)
print(f"thin notes to re-enrich: {len(out)} · with new yt_fix transcript: {sum(o['hasFix'] for o in out)}")
print(f"-> {dest}")
