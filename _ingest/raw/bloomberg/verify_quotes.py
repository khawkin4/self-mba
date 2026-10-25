# usage: verify_quotes.py DIGEST.md articles.jsonl [extra.jsonl...]
# Checks every double-quoted span of >=3 words (paired within a line) in the digest appears verbatim in some article text.
import sys, re, json
md = open(sys.argv[1]).read()
texts = []
for fn in sys.argv[2:]:
    for l in open(fn):
        a = json.loads(l); texts.append((a["url"], a["text"]))
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()
ntexts = [(u, norm(t)) for u, t in texts]
# quotes: straight or curly double quotes; skip code spans
body = re.sub(r"`[^`\n]*`", "", md)
qs = []
for line in body.split("\n"):
    parts = line.split('"')
    qs += [parts[i] for i in range(1, len(parts) - 1, 2)]   # straight quotes, paired within the line
    qs += re.findall(r"\u201c([^\u201d]+)\u201d", line)        # curly double quotes
bad, exact, normed = [], 0, 0
for q in qs:
    if len(q.split()) < 3: continue
    core = q.strip().strip(".,;:…").replace("…", "...")
    pieces = [p.strip() for p in re.split(r"\s*\.\.\.\s*|\s*\[…\]\s*", core) if p.strip()]
    hit_exact = all(any(p in t for _, t in texts) for p in pieces)
    hit_norm = all(any(norm(p) in t for _, t in ntexts) for p in pieces)
    if hit_exact: exact += 1
    elif hit_norm: normed += 1
    else: bad.append(q)
    if len(q.split()) > 25: print("LONG(>25w):", q[:100])
print(f"quotes checked: {exact+normed+len(bad)}  exact: {exact}  match-after-quote-style-normalisation: {normed}  NOT FOUND: {len(bad)}")
for q in bad: print("NOT FOUND:", q)
