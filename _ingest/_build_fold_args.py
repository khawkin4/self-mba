#!/usr/bin/env python3
"""Build the work-list for the 'fold canon depth into existing course lessons' workflow.
Emits JSON: [{lessonFile, lessonTitle, clusters:[name], notePaths:[...], rawDirs:[...]}]
Each ENRICH-verdict canon cluster contributes its enriched notes to one course lesson.
"""
import glob, json, os, re

ROOT = os.path.expanduser("~/self-mba")
NOTES = os.path.join(ROOT, "notes", "canon")
LESSONS = os.path.join(ROOT, "lessons")
CANON_RAW = os.path.join(ROOT, "_ingest", "raw", "2026-06-05", "canon")

NAME2SLUG = {
    "Strategy": "strategy", "Leadership & Presence": "leadership-presence",
    "Mental Models & Thinking": "mental-models", "Org Design & Mechanisms": "org-design-mechanisms",
    "Landscape & Competitive Awareness": "landscape-competitive", "Negotiation & Influence": "negotiation-influence",
    "Execution & Operations": "execution-operations", "Culture & Change": "culture-change",
    "Product Thinking & Innovation": "product-innovation", "Power & Organizational Politics": "power-politics",
    "Personal Effectiveness": "personal-effectiveness", "Financial Literacy for Operators": "financial-literacy",
    "Economics & Incentive Design": "economics-incentives", "Communication & Storytelling": "communication-storytelling",
    "Design Thinking & Problem-Solving": "design-problem-solving",
}

# course lesson  ->  (title, [contributing canon cluster display-names], one-line focus)
FOLD = {
    "core-02-corporate-finance": ("Corporate Finance & Valuation",
        ["Financial Literacy for Operators"],
        "margin of safety + skill-vs-luck as the operator's lens on valuation under uncertainty"),
    "core-03-micro-strategy": ("Microeconomics & Strategy",
        ["Economics & Incentive Design"],
        "opportunity cost, information asymmetry (lemons), and agency/incentive design"),
    "core-04-competitive-strategy": ("Competitive Strategy",
        ["Strategy", "Landscape & Competitive Awareness", "Design Thinking & Problem-Solving"],
        "the strategy kernel/cascade, the 7 Powers + disruption, and finding the crux"),
    "core-06-operations": ("Operations & Supply Chain",
        ["Execution & Operations"],
        "theory of constraints, lean/TPS, and protecting the wildly important (4DX)"),
    "core-08-negotiation": ("Negotiation",
        ["Negotiation & Influence"],
        "ADD the influence/persuasion layer Voss+Fisher-Ury don't cover: Cialdini's 6 principles and Carnegie"),
    "core-09-leadership-ob": ("Leadership & Org Behavior",
        ["Leadership & Presence", "Org Design & Mechanisms", "Power & Organizational Politics"],
        "managerial leverage, intent-based leadership, mechanisms/OKRs, and the uncomfortable truth of power"),
    "core-10-entrepreneurship": ("Entrepreneurship & Venture",
        ["Product Thinking & Innovation"],
        "build-measure-learn, zero-to-one monopoly, and empowered product teams"),
    "exec-E7-exec-presence-comms": ("Executive Presence & Comms",
        ["Communication & Storytelling"],
        "answer-first (Minto pyramid), story structure (Duarte), and lead-with-why (Sinek)"),
    "exec-E11-operating-system": ("Personal Operating System",
        ["Personal Effectiveness", "Mental Models & Thinking"],
        "deep work + atomic habits as systems, and the cross-disciplinary mental-models latticework"),
    "exec-E12-culture-strategy": ("Culture as Strategy",
        ["Culture & Change"],
        "Schein's three levels, Kotter's 8 steps, Switch's Rider/Elephant/Path, and culture = what you do"),
}

# index canon notes by cluster slug
by_cluster = {}
for p in sorted(glob.glob(os.path.join(NOTES, "canon-*.md"))):
    m = re.search(r"Cluster:\s*(.+?)\s*·", open(p, encoding="utf-8").read())
    slug = NAME2SLUG.get(m.group(1).strip()) if m else None
    if slug:
        by_cluster.setdefault(slug, []).append(p)

out = []
for lf, (title, cnames, focus) in FOLD.items():
    slugs = [NAME2SLUG[c] for c in cnames]
    notes = [n for s in slugs for n in by_cluster.get(s, [])]
    raws = [os.path.join(CANON_RAW, s) for s in slugs]
    out.append({
        "lessonFile": os.path.join(LESSONS, lf + ".html"),
        "lessonTitle": title, "clusters": cnames, "focus": focus,
        "notePaths": notes, "rawDirs": raws,
    })

dest = os.path.join(ROOT, "_ingest", "canon_fold_args.json")
json.dump(out, open(dest, "w"), indent=2)
print(f"fold targets: {len(out)} lessons")
for o in out:
    print(f"  {os.path.basename(o['lessonFile'])}: {len(o['notePaths'])} notes from {o['clusters']}")
print(f"-> {dest}")
