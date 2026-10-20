"""Library layer: renders the repo's markdown corpus (learn/, acumen/, notes/, canon,
quant research, glossary, curriculum) into static pages next to the module pages.

Called from build.py main(). Each collection gets an index page (lib-<slug>.html) and one
page per document (doc-<collection>-<stem>.html). Relative .md links and [[wiki]] links are
rewritten to the generated pages so the corpus stays cross-linked on the site.
"""
import datetime, glob, html, json, os, re, subprocess

import markdown

COLLECTIONS = [
    # slug, label, kicker, description, glob patterns (relative to ROOT)
    ("learn", "On-ramp", "Zero → financial literacy",
     "Ten four-pillar units: concept, plain language, a real EDGAR example, an exercise.",
     ["learn/unit-*.md", "learn/README.md"]),
    ("acumen", "Acumen Gym", "Judgment reps",
     "Real companies, live decisions, no answer key — memos that get red-teamed.",
     ["acumen/*.md"]),
    ("notes", "Field Notes", "Practitioner intelligence",
     "Market structure, capital markets, venture and operator playbooks distilled from practitioners.",
     ["notes/*.md", "notes/01-accounting/*.md"]),
    ("canon", "Canon Notes", "The reading backbone",
     "Book-by-book distillations: core claim, framework, applies when, breaks when.",
     ["notes/canon/*.md"]),
    ("quant", "Quant Lab", "Backtesting research",
     "How systematic shops test ideas — and how backtests lie.",
     ["quant-backtesting/research/*.md"]),
    ("reference", "Reference", "Maps of the program",
     "The curriculum, the glossary and the structural analysis that tie the layers together.",
     ["CURRICULUM.md", "GLOSSARY.md", "STRUCTURAL-ANALYSIS.md"]),
]

PIN_FIRST = {"README", "CANON", "MECHANISM", "JUDGMENT-LEDGER", "main-compilation", "CURRICULUM"}


def _git_dates(root, relpath):
    """(first-added, last-modified) ISO dates from git; falls back to mtime."""
    try:
        out = subprocess.run(["git", "-C", root, "log", "--follow", "--format=%cs", "--", relpath],
                             capture_output=True, text=True, timeout=10).stdout.split()
        if out:
            return out[-1], out[0]
    except Exception:
        pass
    d = datetime.date.fromtimestamp(os.path.getmtime(os.path.join(root, relpath))).isoformat()
    return d, d


def _title_and_lede(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = m.group(1).strip() if m else fallback
    title = re.sub(r"[*_`]", "", title)
    lede = ""
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("---") or s.startswith("|"):
            continue
        s = s.lstrip("> ").strip()
        s = re.sub(r"\*\*Status:\*\*.*", "", s)
        if len(s) < 40:
            continue
        lede = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
        lede = re.sub(r"[*_`]|\[\[|\]\]", "", lede)
        break
    return title, (lede[:220] + "…") if len(lede) > 220 else lede


def _doc_id(coll, stem):
    return f"doc-{coll}-{re.sub(r'[^A-Za-z0-9_-]+', '-', stem).lower()}.html"


def collect(root):
    """Return {slug: [doc,...]} plus a path->href map for link rewriting."""
    docs, by_path, by_stem = {}, {}, {}
    for slug, label, kicker, desc, pats in COLLECTIONS:
        items = []
        seen = set()
        for pat in pats:
            for p in sorted(glob.glob(os.path.join(root, pat))):
                rel = os.path.relpath(p, root)
                if rel in seen:
                    continue
                seen.add(rel)
                stem = os.path.splitext(os.path.basename(p))[0]
                text = open(p, encoding="utf-8").read()
                title, lede = _title_and_lede(text, stem)
                added, updated = _git_dates(root, rel)
                parent = os.path.basename(os.path.dirname(rel))
                nested = os.path.dirname(rel) != os.path.dirname(pats[0])
                href = _doc_id(slug, f"{parent}-{stem}" if nested else stem)
                d = dict(coll=slug, rel=rel, stem=stem, title=title, lede=lede, text=text,
                         href=href, added=added, updated=updated,
                         words=len(re.findall(r"\w+", text)))
                items.append(d)
                by_path[os.path.normpath(rel)] = href
                by_stem.setdefault(stem, href)
        items.sort(key=lambda d: (d["stem"] not in PIN_FIRST, d["stem"]))
        docs[slug] = items
    return docs, by_path, by_stem


def _rewrite_links(text, rel, by_path, by_stem):
    base = os.path.dirname(rel)

    def md_link(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, frag = target.partition("#")
        key = os.path.normpath(os.path.join(base, path))
        href = by_path.get(key) or by_stem.get(os.path.splitext(os.path.basename(path))[0])
        if href:
            return f"[{label}]({href}{'#' + frag if frag else ''})"
        return label  # local file the site doesn't publish: keep the text only

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", md_link, text)

    def wiki(m):
        stem = m.group(1).split("|")[0].strip()
        href = by_stem.get(stem)
        lab = stem.replace("-", " ")
        return f'<a class="wiki" href="{href}">{html.escape(lab)}</a>' if href else f'<span class="wiki dead">{html.escape(lab)}</span>'

    return re.sub(r"\[\[([^\]]+)\]\]", wiki, text)


_MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
                        extension_configs={"toc": {"permalink": False, "toc_depth": "2-3"}})


def render_markdown(text):
    _MD.reset()
    body = _MD.convert(text)
    return body, getattr(_MD, "toc_tokens", [])


def _toc_html(tokens):
    if not tokens:
        return ""
    items = []

    def walk(nodes, depth):
        for c in nodes:
            if c["level"] > 3:
                continue
            items.append(f'<li class="l{c["level"]}"><a href="#{c["id"]}">{c["name"]}</a></li>')
            if c["level"] == 2 and c.get("children"):
                walk(c["children"], depth + 1)

    for t in tokens:
        # docs put the title in h1; walk its children
        walk(t.get("children") or [] if t["level"] == 1 else [t], 0)
    if len(items) < 2:
        return ""
    return (f'<nav class="doc-toc" aria-label="On this page"><details><summary>On this page</summary>'
            f'<ol>{"".join(items)}</ol></details></nav>')


def _meta_for(slug):
    return next(c for c in COLLECTIONS if c[0] == slug)


HEADINGS = {}  # href -> [(text, id)] gathered while rendering, for the search index


def render_doc(d, docs, by_path, by_stem, head, foot):
    slug, label, kicker, _, _ = _meta_for(d["coll"])
    body, toc = render_markdown(_rewrite_links(d["text"], d["rel"], by_path, by_stem))
    hs = []
    def _walk(nodes):
        for c in nodes:
            if c["level"] in (2, 3):
                hs.append((re.sub(r"<[^>]+>", "", c["name"]).strip(), c["id"]))
            if c.get("children"): _walk(c["children"])
    _walk(toc)
    HEADINGS[d["href"]] = hs[:60]
    # strip the leading h1: the page header carries the title
    body = re.sub(r"^\s*<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)
    # tables scroll horizontally on narrow screens instead of breaking the page
    body = re.sub(r"<table>(.*?)</table>", r'<div class="tbl"><table>\1</table></div>', body, flags=re.S)
    siblings = docs[slug]
    i = siblings.index(d)
    prev = siblings[i - 1] if i > 0 else None
    nxt = siblings[i + 1] if i < len(siblings) - 1 else None
    pn = '<nav class="doc-pn">'
    pn += f'<a class="doc-prev" href="{prev["href"]}"><span>Previous</span>{html.escape(prev["title"])}</a>' if prev else "<span></span>"
    pn += f'<a class="doc-next" href="{nxt["href"]}"><span>Next</span>{html.escape(nxt["title"])}</a>' if nxt else "<span></span>"
    pn += "</nav>"
    mins = max(1, round(d["words"] / 230))
    return head.format(title=html.escape(d["title"]) + " · The Compounding MBA", css="style.css") + f"""
<div id="progress"></div>
<div class="doc-shell" data-coll="{slug}">
<header class="doc-head">
<nav class="crumbs"><a href="index.html">Home</a><span>/</span><a href="index.html#t-library">Library</a><span>/</span><a href="lib-{slug}.html">{html.escape(label)}</a></nav>
<div class="doc-kicker">{html.escape(kicker)}</div>
<h1 class="doc-title">{html.escape(d["title"])}</h1>
<div class="doc-meta"><span>{mins} min read</span><span>{d["words"]:,} words</span><span>Updated {d["updated"]}</span><span class="doc-src">{html.escape(d["rel"])}</span></div>
</header>
<div class="doc-layout">
{_toc_html(toc)}
<article class="prose">{body}</article>
</div>
<div class="doc-end"><button class="mark-read" type="button" data-href="{d['href']}"><span class="mr-tick">✓</span><span class="mr-off">Mark as read</span><span class="mr-on">Read</span></button><span class="doc-end-hint">Marks itself read when you reach the end.</span></div>
{pn}
</div>{foot}"""


def render_collection(slug, docs, head, foot):
    _, label, kicker, desc, _ = _meta_for(slug)
    rows = []
    for i, d in enumerate(docs[slug], 1):
        rows.append(f"""<a class="lib-row" href="{d['href']}" data-updated="{d['updated']}" data-href="{d['href']}">
<span class="lib-n">{i:02d}</span><span class="lib-tick" aria-label="Read">✓</span>
<span class="lib-main"><span class="lib-title">{html.escape(d['title'])}</span><span class="lib-lede">{html.escape(d['lede'])}</span></span>
<span class="lib-date">{d['updated']}</span></a>""")
    total = sum(d["words"] for d in docs[slug])
    others = "".join(f'<a href="lib-{s}.html"{" class=cur" if s == slug else ""}>{html.escape(l)}</a>'
                     for s, l, *_ in COLLECTIONS)
    return head.format(title=f"{html.escape(label)} · The Compounding MBA", css="style.css") + f"""
<div class="lib-shell" data-coll="{slug}">
<header class="lib-head">
<nav class="crumbs"><a href="index.html">Home</a><span>/</span><a href="index.html#t-library">Library</a><span>/</span><span class="current">{html.escape(label)}</span></nav>
<div class="doc-kicker">{html.escape(kicker)}</div>
<h1 class="lib-h1">{html.escape(label)}</h1>
<p class="lib-desc">{html.escape(desc)}</p>
<div class="doc-meta"><span>{len(docs[slug])} documents</span><span>{total:,} words</span><span class="lib-readcount" data-total="{len(docs[slug])}"></span></div>
<input class="lib-filter" aria-label="Filter {html.escape(label.lower())}" placeholder="Filter {html.escape(label.lower())}…" oninput="var q=this.value.toLowerCase();document.querySelectorAll('.lib-row').forEach(function(r){{r.style.display=r.textContent.toLowerCase().includes(q)?'':'none'}})">
</header>
<div class="lib-list">{''.join(rows)}</div>
<nav class="lib-foot" aria-label="Collections">{others}</nav>
</div>{foot}"""


def build(root, dist, head, foot="</body></html>"):
    """Render every collection. Returns summary data for the home page."""
    docs, by_path, by_stem = collect(root)
    for slug, items in docs.items():
        open(os.path.join(dist, f"lib-{slug}.html"), "w", encoding="utf-8").write(render_collection(slug, docs, head, foot))
        for d in items:
            open(os.path.join(dist, d["href"]), "w", encoding="utf-8").write(render_doc(d, docs, by_path, by_stem, head, foot))
    summary = []
    for slug, label, kicker, desc, _ in COLLECTIONS:
        items = docs[slug]
        summary.append(dict(slug=slug, label=label, kicker=kicker, desc=desc, count=len(items),
                            words=sum(d["words"] for d in items), hrefs=[d["href"] for d in items],
                            updated=max((d["updated"] for d in items), default="")))
    latest = sorted((d for items in docs.values() for d in items), key=lambda d: (d["updated"], d["added"]), reverse=True)[:8]
    latest = [dict(title=d["title"], href=d["href"], updated=d["updated"], coll=_meta_for(d["coll"])[1], lede=d["lede"]) for d in latest]
    search = [dict(t=d["title"], h=d["href"], c=_meta_for(d["coll"])[1], k="") for items in docs.values() for d in items]
    for items in docs.values():
        for d in items:
            for txt, hid in HEADINGS.get(d["href"], []):
                if len(txt) < 4: continue
                search.append(dict(t=txt, h=f"{d['href']}#{hid}", c=_meta_for(d["coll"])[1], k="", p=d["title"]))
    n = sum(len(v) for v in docs.values())
    print(f"  library: {n} documents across {len(docs)} collections")
    return dict(collections=summary, latest=latest, doc_count=n, doc_words=sum(s["words"] for s in summary), search=search)
