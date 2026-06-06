#!/usr/bin/env python3
"""Build the args array for the canon enrichment workflow.
Emits JSON: [{note, book, clusterName, clusterSlug, rawDir, rawFiles, enriched}]
Reads each note's `Cluster:` header, maps to its raw folder, lists available raw.
"""
import glob, json, os, re

ROOT = os.path.expanduser("~/self-mba")
NOTES = os.path.join(ROOT, "notes", "canon")
RAW = os.path.join(ROOT, "_ingest", "raw", "2026-06-05", "canon")
# also allow reuse of overlapping course raw for ENRICH clusters
COURSE_RAW = os.path.join(ROOT, "_ingest", "raw", "2026-06-05")

NAME2SLUG = {
    "Strategy": "strategy",
    "Leadership & Presence": "leadership-presence",
    "Mental Models & Thinking": "mental-models",
    "Org Design & Mechanisms": "org-design-mechanisms",
    "Landscape & Competitive Awareness": "landscape-competitive",
    "Negotiation & Influence": "negotiation-influence",
    "Execution & Operations": "execution-operations",
    "Culture & Change": "culture-change",
    "Risk, Uncertainty & Fragility": "risk-fragility",
    "Product Thinking & Innovation": "product-innovation",
    "Power & Organizational Politics": "power-politics",
    "Personal Effectiveness": "personal-effectiveness",
    "Financial Literacy for Operators": "financial-literacy",
    "Behavioral Design & Decision Science": "behavioral-decision",
    "Game Theory & Strategic Interaction": "game-theory",
    "Network Effects & Platform Strategy": "platform-strategy",
    "Systems Thinking & Complexity": "systems-complexity",
    "Information & Communication": "information-communication",
    "Economics & Incentive Design": "economics-incentives",
    "History & Judgment": "history-judgment",
    "Communication & Storytelling": "communication-storytelling",
    "Design Thinking & Problem-Solving": "design-problem-solving",
    "Ethics & Judgment": "ethics-judgment",
}

out, unmapped = [], set()
for p in sorted(glob.glob(os.path.join(NOTES, "canon-*.md"))):
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"Cluster:\s*(.+?)\s*·", txt)
    cname = m.group(1).strip() if m else "?"
    slug = NAME2SLUG.get(cname)
    if not slug:
        unmapped.add(cname); continue
    rawdir = os.path.join(RAW, slug)
    rawfiles = sorted(os.path.basename(f) for f in glob.glob(os.path.join(rawdir, "*"))) if os.path.isdir(rawdir) else []
    out.append({
        "note": p,
        "book": os.path.basename(p)[:-3],
        "clusterName": cname,
        "clusterSlug": slug,
        "rawDir": rawdir,
        "rawFiles": rawfiles,
        "enriched": "Researched layer" in txt,
    })

# Net-new lessons: homeless clusters that merit their own lesson (game-theory already built).
NET_NEW = {
    "behavioral-decision": "Behavioral Design & Decision Science",
    "risk-fragility": "Risk, Uncertainty & Fragility",
    "systems-complexity": "Systems Thinking & Complexity",
    "platform-strategy": "Network Effects & Platform Strategy",
    "history-judgment": "History & Judgment",
    "power-politics": "Power & Organizational Politics",
    "information-communication": "Information & Communication",
    "ethics-judgment": "Ethics & Judgment",
}
lessons = []
for slug, title in NET_NEW.items():
    lesson_path = os.path.join(ROOT, "lessons", f"canon-{slug}.html")
    notes_in = [o["note"] for o in out if o["clusterSlug"] == slug]
    rawdir = os.path.join(RAW, slug)
    rawfiles = sorted(os.path.basename(f) for f in glob.glob(os.path.join(rawdir, "*"))) if os.path.isdir(rawdir) else []
    lessons.append({"clusterSlug": slug, "clusterName": title, "lessonPath": lesson_path,
                    "rawDir": rawdir, "rawFiles": rawfiles, "notePaths": notes_in,
                    "exists": os.path.exists(lesson_path)})

todo = [o for o in out if not o["enriched"]]
payload = {"notes": todo, "lessons": lessons}
dest = os.path.join(ROOT, "_ingest", "canon_workflow_args.json")
json.dump(payload, open(dest, "w"), indent=2)
print(f"notes total: {len(out)} · already enriched: {sum(o['enriched'] for o in out)} · to enrich: {len(todo)}")
print(f"net-new lessons to draft: {len(lessons)} ({', '.join(l['clusterSlug'] for l in lessons)})")
print(f"unmapped clusters: {sorted(unmapped) or 'none'}")
print(f"clusters MISSING raw: {sorted({o['clusterSlug'] for o in out if not o['rawFiles']})}")
print(f"-> {dest}")
