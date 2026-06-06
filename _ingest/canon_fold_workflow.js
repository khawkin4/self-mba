export const meta = {
  name: 'canon-fold-into-lessons',
  description: 'Append a cited "From the Canon" section to each of 10 existing course lessons, grounded in the enriched canon notes',
  phases: [
    { title: 'Plan', detail: 'build the lesson -> clusters -> notes work-list' },
    { title: 'Fold', detail: 'append a From the Canon section to each course lesson' },
  ],
}

const PLAN_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['targets'],
  properties: {
    targets: { type: 'array', items: { type: 'object', additionalProperties: true,
      required: ['lessonFile', 'lessonTitle', 'clusters', 'focus', 'notePaths'],
      properties: {
        lessonFile: { type: 'string' }, lessonTitle: { type: 'string' },
        clusters: { type: 'array', items: { type: 'string' } },
        focus: { type: 'string' },
        notePaths: { type: 'array', items: { type: 'string' } },
        rawDirs: { type: 'array', items: { type: 'string' } },
      } } },
  },
}

const FOLD_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['lessonFile', 'status', 'booksAdded', 'sourcesCited'],
  properties: {
    lessonFile: { type: 'string' },
    status: { type: 'string', enum: ['folded', 'replaced', 'error'] },
    booksAdded: { type: 'integer' },
    sourcesCited: { type: 'integer' },
  },
}

phase('Plan')
const plan = await agent(
  `Run this and return its output as structured data:
\`\`\`
python3 ~/self-mba/_ingest/_build_fold_args.py >/dev/null 2>&1; cat ~/self-mba/_ingest/canon_fold_args.json
\`\`\`
It's a JSON array of fold targets (course lessons that should gain a "From the Canon" section). Return it verbatim under key "targets".`,
  { label: 'plan:fold-worklist', phase: 'Plan', schema: PLAN_SCHEMA }
)
log(`fold targets: ${plan.targets.length} course lessons`)

phase('Fold')
const FOLD_INSTRUCTIONS = (t) => `You are enriching ONE existing "Ivy & Ink" course lesson by APPENDING a cited "From the Canon" section that folds in the relevant canon books. This is NON-DESTRUCTIVE: do not rewrite or delete any existing content. Cite ONLY real sources that already appear in the enriched canon notes (never invent a URL).

COURSE LESSON FILE (edit in place): ${t.lessonFile}
LESSON TOPIC: ${t.lessonTitle}
WHAT TO ADD (focus): ${t.focus}
CANON NOTES TO DRAW FROM (already enriched — they contain real quotes + "Sources in corpus" URLs):
${t.notePaths.map((p) => '  - ' + p).join('\n')}

STEPS:
1. Read the existing lesson file ${t.lessonFile} to learn its voice, structure, and CSS classes (lead, h2, srcq/cite, fc-grid, pitfall, apply-box, src-list). Note how it already teaches the topic — your section COMPLEMENTS it, no repetition.
2. IDEMPOTENCY: if the file already contains the marker "<!-- CANON-FOLD -->", you are REPLACING the old fold. Remove everything from "<!-- CANON-FOLD -->" to just before the file's final source-list (or EOF) and regenerate. Otherwise you're adding it fresh. Set status accordingly ("replaced" vs "folded").
3. Read the canon notes listed. From each book pull: its one-line core claim + ONE genuinely useful framework or insight the existing lesson lacks, and (where the note's "Researched layer" has one) a REAL quoted line with its real youtube.com/watch?v=<id> source.
4. Write a new section and INSERT it immediately BEFORE the lesson's final <div class="src-list"> (so the source list stays last). If there is no src-list, append at end. The section must be:
   - Open with the exact HTML comment: <!-- CANON-FOLD -->
   - <h2>📚 From the Canon — <name the books, e.g. "Cialdini &amp; Carnegie on influence"></h2>
   - A <p> that frames how these books deepen THIS lesson's topic (use the focus above).
   - For each book: a short punchy treatment — a <p> or a <div class="fc-grid"> of flashcards (one per book: <button class="fc"><span class="fc-inner"><span class="fc-f"><b>Book — Author</b><span class="hint">tap to flip ↻</span></span><span class="fc-b">the one idea</span></span></button>), OR a few <blockquote class="srcq"><p>real quote</p><cite><a href=REAL_URL …>— Source</a> · in your corpus</cite></blockquote> where a real cite exists in the notes.
   - Include at least ONE real <blockquote class="srcq"> with a real corpus URL if any of the notes has one (the non-corpus-thin ones do).
   - End the section with a <p class="loop-line"> pointing readers to the canon cluster page(s) for deeper sourcing, e.g. linking to the cluster's site page(s) like <a href="${(t.clusters && t.clusters.length ? 'canon-' : '')}…">. (Use the canon cluster site pages named canon-<slug>.html — derive the slug from the cluster; if unsure, just name the books in prose.)
5. Keep it tight and high-signal (roughly 20–45 lines). Match the lesson's existing tone exactly. Do NOT touch any pre-existing section.

Return: {lessonFile:"${t.lessonFile}", status:"folded"|"replaced", booksAdded:<int>, sourcesCited:<# real cite links you added>}.`

const folded = await parallel(
  plan.targets.map((t) => () =>
    agent(FOLD_INSTRUCTIONS(t), { label: `fold:${t.lessonFile.split('/').pop().replace('.html', '')}`, phase: 'Fold', schema: FOLD_SCHEMA })
  )
)
const ok = folded.filter(Boolean)
log(`folded ${ok.filter(f => f.status !== 'error').length}/${plan.targets.length} lessons · ${ok.reduce((s, f) => s + (f.sourcesCited || 0), 0)} cites added`)

return {
  folded: ok.filter(f => f.status !== 'error').map(f => ({ lesson: f.lessonFile.split('/').pop(), books: f.booksAdded, cites: f.sourcesCited })),
}
