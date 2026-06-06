export const meta = {
  name: 'canon-enrich-and-teach',
  description: 'Enrich 80 canon notes with cited Researched layers from on-disk corpus, then draft 8 net-new Ivy & Ink cluster lessons',
  phases: [
    { title: 'Plan', detail: 'build the work-list from disk (notes to enrich + lessons to draft)' },
    { title: 'Enrich', detail: 'fill each note\'s research layer from its cluster raw transcripts + reddit' },
    { title: 'Lessons', detail: 'draft net-new lessons for the homeless clusters' },
  ],
}

const PLAN_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['notes', 'lessons'],
  properties: {
    notes: { type: 'array', items: { type: 'object', additionalProperties: true,
      required: ['note', 'book', 'clusterName', 'clusterSlug', 'rawDir'],
      properties: {
        note: { type: 'string' }, book: { type: 'string' },
        clusterName: { type: 'string' }, clusterSlug: { type: 'string' },
        rawDir: { type: 'string' }, rawFiles: { type: 'array', items: { type: 'string' } },
      } } },
    lessons: { type: 'array', items: { type: 'object', additionalProperties: true,
      required: ['clusterSlug', 'clusterName', 'lessonPath', 'rawDir', 'notePaths'],
      properties: {
        clusterSlug: { type: 'string' }, clusterName: { type: 'string' },
        lessonPath: { type: 'string' }, rawDir: { type: 'string' },
        rawFiles: { type: 'array', items: { type: 'string' } },
        notePaths: { type: 'array', items: { type: 'string' } },
      } } },
  },
}

const ENRICH_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['book', 'status', 'sourcesCited', 'corpusThin'],
  properties: {
    book: { type: 'string' },
    status: { type: 'string', enum: ['enriched', 'skipped', 'error'] },
    sourcesCited: { type: 'integer' },
    corpusThin: { type: 'boolean' },
    note: { type: 'string' },
  },
}

const LESSON_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['clusterSlug', 'status', 'sections', 'sourcesCited'],
  properties: {
    clusterSlug: { type: 'string' },
    status: { type: 'string', enum: ['written', 'error'] },
    sections: { type: 'integer' },
    sourcesCited: { type: 'integer' },
    lessonPath: { type: 'string' },
  },
}

// ---- Phase 1: build the work-list from disk ----
phase('Plan')
const plan = await agent(
  `Run this exact command and return its output as structured data:
\`\`\`
python3 ~/self-mba/_ingest/_build_canon_workflow_args.py >/dev/null 2>&1; cat ~/self-mba/_ingest/canon_workflow_args.json
\`\`\`
The file is JSON with keys "notes" (array of notes still needing enrichment) and "lessons" (net-new lessons to draft). Return it verbatim as the structured object — do not invent or drop entries.`,
  { label: 'plan:build-worklist', phase: 'Plan', schema: PLAN_SCHEMA }
)

log(`work-list: ${plan.notes.length} notes to enrich, ${plan.lessons.length} net-new lessons to draft`)

// ---- Phase 2: enrich every note in parallel (each edits a DISTINCT file) ----
phase('Enrich')
const ENRICH_INSTRUCTIONS = (t) => `You are enriching ONE canon book-note in The Compounding MBA with a real, cited "Researched layer" mined from the on-disk corpus. Integrity is paramount: cite ONLY sources that actually exist in the raw files. Never invent a URL, video ID, channel, or Reddit thread.

NOTE TO ENRICH: ${t.note}
BOOK: ${t.book}   CLUSTER: ${t.clusterName}
RAW CORPUS DIR: ${t.rawDir}

STEPS:
1. Read the format exemplar so you match it EXACTLY: ~/self-mba/notes/canon/canon-voss-never-split-the-difference.md (see its "Practitioner counterpoint" line + "Researched layer" block + "Sources in corpus" line).
2. Read the note you must enrich: ${t.note}
3. Mine the corpus. List the raw files: \`ls "${t.rawDir}"\`. For yt_*.json (YouTube transcripts) and reddit_*.json, extract titles, ids/urls, and key passages WITHOUT reading entire huge files — use python, e.g.:
   \`python3 -c "import json,glob; [print(v.get('title'),'|',v.get('id'),'|',(v.get('transcript') or '')[:2500]) for f in glob.glob('${t.rawDir}/yt_*.json') for v in json.load(open(f))]"\`
   and similarly print reddit titles + ups + selftext[:400]. Also, if this cluster maps onto an existing course pull, you MAY additionally read ~/self-mba/_ingest/raw/2026-06-05/core/ or /exec/ folders that clearly cover this book (optional).
4. EDIT the note in place with two changes, matching the exemplar's markdown style precisely:
   a. REPLACE the line that begins "- **Practitioner counterpoint:** (fill via \`research\`" with a real, sourced practitioner finding (label it "*(researched 2026-06-05 — <subreddit/transcript> corpus)*"). Quote real Reddit thread titles + upvote counts and/or real transcript lines.
   b. INSERT, immediately BEFORE the line that begins "- **Links:**", a new block exactly like the exemplar's:
      "- **Researched layer** *(2026-06-05)*" followed by indented bullets:
        - **Canonical explanation (sourced):** the book's core mechanism, with a real quoted line + (channel/title) from a transcript in the corpus.
        - **Real application (mined):** a concrete case/example from the corpus (a Reddit story or a transcript example).
        - **Where the corpus pushes back on the book:** the practitioner reality-check / critique.
        - **Sources in corpus:** a real list — "<Channel> — <title> (youtube.com/watch?v=<id>)" for each transcript you used, and "r/<sub> '<thread title>' (<ups>↑)" for reddit. Only list what you actually opened.
5. Do NOT alter the note's existing core claim, framework, applies/breaks-when, cross-links ([[...]]), or the Rep. Only add the two pieces above.

IF THE RAW DIR IS EMPTY OR THIN: do not fabricate. Write a lighter "Researched layer" grounded in well-established knowledge of the book, clearly add "*(corpus thin — flagged for re-pull)*", and set corpusThin=true. Cite only what genuinely exists.

Return: {book, status:"enriched", sourcesCited:<count of real sources you listed>, corpusThin:<bool>, note:"${t.note}"}.`

const enriched = await parallel(
  plan.notes.map((t) => () =>
    agent(ENRICH_INSTRUCTIONS(t), { label: `enrich:${t.book.replace(/^canon-/, '')}`, phase: 'Enrich', schema: ENRICH_SCHEMA })
  )
)
const ok = enriched.filter(Boolean)
log(`enriched ${ok.filter(e => e.status === 'enriched').length}/${plan.notes.length} notes · ${ok.filter(e => e.corpusThin).length} flagged corpus-thin`)

// ---- Phase 3: draft net-new lessons (after enrichment barrier; lessons read enriched notes) ----
phase('Lessons')
const LESSON_INSTRUCTIONS = (l) => `You are authoring ONE net-new "Ivy & Ink" lesson for The Compounding MBA, teaching the canon cluster "${l.clusterName}". It must be visual-first, interactive, and grounded ONLY in real sources from the corpus. Never invent a citation.

OUTPUT FILE (write it): ${l.lessonPath}
CLUSTER RAW CORPUS: ${l.rawDir}
ENRICHED CANON NOTES for this cluster (read them — they hold the synthesized content + cited sources):
${l.notePaths.map((p) => '  - ' + p).join('\n')}

STEPS:
1. Read TWO format exemplars and copy their structure/CSS classes EXACTLY (this is a partial HTML body — NO <html>/<head>/<body> wrapper; build.py wraps it):
   - ~/self-mba/lessons/canon-game-theory.html  (the canon-lesson exemplar)
   - ~/self-mba/lessons/core-08-negotiation.html (the original style reference)
   Required elements & classes, in this order: opening <p class="lead">; several <h2> numbered sections; <blockquote class="srcq"><p>…quote…</p><cite><a href=REAL_CORPUS_URL …>— Source</a> · in your corpus</cite></blockquote>; at least one <figure class="viz"> with an inline <svg viewBox…> diagram using the existing classes (vlabel, bar-rev, bar-gross, bar-net, bar-txt, bar-txt-sm, data-tip tooltips); one <div class="reveal"> q/a; one <div class="fc-grid"> of flashcards (<button class="fc"><span class="fc-inner"><span class="fc-f">…<span class="hint">tap to flip ↻</span></span><span class="fc-b">…</span></span></button>); one <div class="example">; a "Check yourself" section of 3 <div class="quizq" data-correct="N"> with <button class="opt"> options + <p class="fb"> feedback; a <div class="pitfall"> and a <div class="pitfall subtle"> (bridge to the rest of the shelf); a <div class="apply-box"> ("🎯 Your move"); and a final <div class="src-list"> listing the REAL corpus YouTube URLs you taught from, plus a line naming the [[canon-...]] notes behind the lesson.
2. Mine the cluster raw (ls "${l.rawDir}"; extract transcript titles, ids, and quotable lines via python as needed) and the enriched notes. Teach the cluster's marquee books and their key frameworks. Use REAL quotes with REAL youtube.com/watch?v=<id> links found in the corpus. If the raw is thin, lean on the enriched notes' content and cite only the real sources that exist; keep every <cite> link real.
3. Write a complete, polished lesson body to ${l.lessonPath}. Aim for the depth/length of the two exemplars (~120–180 lines). Start the file with an HTML comment naming the cluster + the books + the corpus sources used.

Return: {clusterSlug:"${l.clusterSlug}", status:"written", sections:<# of h2>, sourcesCited:<# of real cite links>, lessonPath:"${l.lessonPath}"}.`

const lessons = await parallel(
  plan.lessons.map((l) => () =>
    agent(LESSON_INSTRUCTIONS(l), { label: `lesson:${l.clusterSlug}`, phase: 'Lessons', schema: LESSON_SCHEMA })
  )
)
const lok = lessons.filter(Boolean)
log(`drafted ${lok.filter(x => x.status === 'written').length}/${plan.lessons.length} lessons`)

return {
  enriched: ok.filter(e => e.status === 'enriched').length,
  corpusThin: ok.filter(e => e.corpusThin).map(e => e.book),
  lessonsWritten: lok.filter(x => x.status === 'written').map(x => x.clusterSlug),
  lessonsCited: lok.map(x => ({ c: x.clusterSlug, src: x.sourcesCited })),
}
