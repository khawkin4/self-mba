export const meta = {
  name: 'canon-reenrich-thin',
  description: 'Re-enrich the corpus-thin canon notes using the newly re-pulled book-specific transcripts',
  phases: [
    { title: 'Plan', detail: 'list thin notes + their new yt_fix transcripts' },
    { title: 'Reenrich', detail: 'replace each thin research layer with a fuller cited one' },
  ],
}

const PLAN_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['notes'],
  properties: {
    notes: { type: 'array', items: { type: 'object', additionalProperties: true,
      required: ['note', 'book', 'clusterName', 'rawDir'],
      properties: {
        note: { type: 'string' }, book: { type: 'string' }, clusterName: { type: 'string' },
        clusterSlug: { type: 'string' }, rawDir: { type: 'string' },
        fixFile: { type: 'string' }, hasFix: { type: 'boolean' },
      } } },
  },
}
const RE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['book', 'status', 'sourcesCited', 'stillThin'],
  properties: {
    book: { type: 'string' },
    status: { type: 'string', enum: ['reenriched', 'unchanged', 'error'] },
    sourcesCited: { type: 'integer' }, stillThin: { type: 'boolean' },
  },
}

phase('Plan')
const plan = await agent(
  `Run and return as structured data under "notes":
\`\`\`
python3 ~/self-mba/_ingest/_build_thin_reenrich_args.py >/dev/null 2>&1; cat ~/self-mba/_ingest/canon_reenrich_args.json
\`\`\``,
  { label: 'plan:thin-worklist', phase: 'Plan', schema: PLAN_SCHEMA }
)
log(`re-enrich: ${plan.notes.length} thin notes (${plan.notes.filter(n => n.hasFix).length} have new transcript)`)

phase('Reenrich')
const RE = (t) => `You are RE-ENRICHING one canon note that was previously flagged "corpus thin". A targeted re-pull has now fetched a book-specific transcript for it. Replace the thin research layer with a fuller, properly-sourced one. Integrity: cite ONLY sources that actually exist in the raw files; never invent a URL.

NOTE: ${t.note}
BOOK: ${t.book}   CLUSTER: ${t.clusterName}
NEW book-specific transcript (primary source): ${t.fixFile || '(none landed — see rawDir)'}
CLUSTER RAW DIR (other transcripts + reddit): ${t.rawDir}

STEPS:
1. Read the new transcript first (if present): \`python3 -c "import json; [print(v.get('title'),'|',v.get('id'),'|',(v.get('transcript') or '')[:4000]) for v in json.load(open('${t.fixFile}'))]"\` (skip if path empty). Also skim the other yt_*.json + reddit_*.json in ${t.rawDir} for anything book-relevant.
2. Read the note ${t.note}. Read ~/self-mba/notes/canon/canon-voss-never-split-the-difference.md as the format exemplar.
3. REPLACE the existing block that runs FROM the line beginning "- **Practitioner counterpoint:**" UP TO (but NOT including) the line beginning "- **Links:**". Regenerate both pieces from the new sources:
   a. "- **Practitioner counterpoint:** *(researched 2026-06-06 — <real source>)*" + a real, sourced finding (quote a real transcript line or a real reddit thread title + ups).
   b. A blank line, then "- **Researched layer** *(updated 2026-06-06)*" with indented bullets: Canonical explanation (sourced, with a real quoted line + channel/title), Real application (mined), Where the corpus pushes back, and "Sources in corpus:" listing ONLY the real youtube.com/watch?v=<id> + r/<sub> sources you actually used.
   - If the new transcript genuinely covers the book, DROP all "corpus thin / flagged for re-pull" wording and set stillThin=false. If it's still weak, keep an honest brief flag and set stillThin=true.
4. Do NOT alter the note's core claim, framework, applies/breaks-when, the "- **Links:**" line, cross-links, or the Rep. Only replace the practitioner + researched-layer block.

Return: {book:"${t.book}", status:"reenriched"|"unchanged", sourcesCited:<int>, stillThin:<bool>}.`

const res = await parallel(
  plan.notes.map((t) => () =>
    agent(RE(t), { label: `reenrich:${t.book.replace(/^canon-/, '')}`, phase: 'Reenrich', schema: RE_SCHEMA })
  )
)
const ok = res.filter(Boolean)
log(`re-enriched ${ok.filter(r => r.status === 'reenriched').length}/${plan.notes.length} · still thin: ${ok.filter(r => r.stillThin).length}`)
return {
  reenriched: ok.filter(r => r.status === 'reenriched').length,
  stillThin: ok.filter(r => r.stillThin).map(r => r.book),
}
