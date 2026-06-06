export const meta = {
  name: 'gap-lessons',
  description: 'Build 5 Ivy & Ink lessons for the benchmark gap domains from the freshly-pulled transcripts',
  phases: [{ title: 'Lessons', detail: 'one lesson per technical-foundations gap domain' }],
}

const RAW = '/Users/kalvaryhawkins/self-mba/_ingest/raw/2026-06-05/gaps'
const LESSONS = '/Users/kalvaryhawkins/self-mba/lessons'

const SPECS = [
  { area: 'managerial-accounting', title: 'Managerial & Cost Accounting',
    focus: 'cost behavior + CVP/break-even, contribution margin, activity-based costing, and standard-cost variance analysis — the decision-support accounting a 10-K never shows you' },
  { area: 'statistics-quant', title: 'Quantitative Methods & Statistics',
    focus: 'linear regression, hypothesis testing, p-values and confidence intervals — turning "decision science" into the actual math, taught StatQuest-style' },
  { area: 'marketing-strategy', title: 'Marketing Strategy & Positioning',
    focus: 'segmentation-targeting-positioning, April Dunford’s positioning method, Byron Sharp’s laws of brand growth, and CAC/LTV unit economics' },
  { area: 'information-systems', title: 'Information Systems & Data',
    focus: 'what an MIS is, ERP/enterprise systems, relational-database fundamentals, and data governance — the IT backbone of a modern firm' },
  { area: 'business-law', title: 'The Legal Environment of Business',
    focus: 'contracts, intellectual property (copyright/trademark/patent), employment law, and antitrust basics every manager must know' },
]

const LESSON_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['area', 'status', 'sections', 'sourcesCited'],
  properties: {
    area: { type: 'string' }, status: { type: 'string', enum: ['written', 'error'] },
    sections: { type: 'integer' }, sourcesCited: { type: 'integer' }, lessonPath: { type: 'string' },
  },
}

phase('Lessons')
const INSTRUCTIONS = (s) => `You are authoring ONE net-new "Ivy & Ink" lesson for The Compounding MBA, teaching "${s.title}". This is a BENCHMARK-GAP domain — the technical content a great-books canon under-covers — so be concrete and practical. Ground it ONLY in the real transcripts/threads in the corpus dir; never invent a citation.

OUTPUT FILE (write it): ${LESSONS}/gap-${s.area}.html
CORPUS DIR: ${RAW}/${s.area}
FOCUS: ${s.focus}

STEPS:
1. Read TWO format exemplars and copy their structure + CSS classes EXACTLY (partial HTML body, NO <html>/<head>/<body> wrapper — build.py wraps it):
   - ${LESSONS}/canon-game-theory.html
   - ${LESSONS}/canon-behavioral-decision.html
   Required elements/classes IN ORDER: <p class="lead">; several numbered <h2> sections; <blockquote class="srcq"><p>…real quote…</p><cite><a href=REAL_CORPUS_URL …>— Source</a> · in your corpus</cite></blockquote>; at least one <figure class="viz"> with an inline <svg viewBox…> diagram using classes vlabel/bar-rev/bar-gross/bar-net/bar-txt/bar-txt-sm and data-tip tooltips (e.g. a break-even chart, a regression line, an STP funnel, a 3-tier data/ERP stack, a contract-formation flow); one <div class="reveal"> q/a; one <div class="fc-grid"> of flashcards; one <div class="example"> worked example with real numbers where apt; a "Check yourself" block of 3 <div class="quizq" data-correct="N"> with <button class="opt"> + <p class="fb">; a <div class="pitfall"> and a <div class="pitfall subtle"> (bridge to the rest of the MBA); a <div class="apply-box"> ("🎯 Your move"); a final <div class="src-list"> listing the REAL corpus YouTube URLs taught from.
2. Mine the corpus: run \`ls ${RAW}/${s.area}\`, then extract transcript titles/ids/quotable lines with python, e.g.:
   \`python3 -c "import json,glob; [print(v.get('title'),'|',v.get('id'),'|',(v.get('transcript') or '')[:3500]) for f in glob.glob('${RAW}/${s.area}/yt_*.json') for v in json.load(open(f))]"\`
   and the reddit_*.json titles + top selftext for a practitioner reality-check.
3. Teach the FOCUS concretely — real formulas/definitions/worked numbers where the domain calls for it (e.g. break-even = fixed / contribution margin; a variance split; a regression slope; CAC payback; a contract's required elements). Use REAL quotes with REAL youtube.com/watch?v=<id> links found in the corpus. Start the file with an HTML comment naming the domain + the sources used.
4. Write a complete, polished lesson (~120–170 lines) to ${LESSONS}/gap-${s.area}.html.

Return: {area:"${s.area}", status:"written", sections:<# h2>, sourcesCited:<# real cite links>, lessonPath:"${LESSONS}/gap-${s.area}.html"}.`

const out = await parallel(
  SPECS.map((s) => () => agent(INSTRUCTIONS(s), { label: `gap:${s.area}`, phase: 'Lessons', schema: LESSON_SCHEMA }))
)
const ok = out.filter(Boolean)
log(`wrote ${ok.filter(x => x.status === 'written').length}/${SPECS.length} gap lessons`)
return { written: ok.filter(x => x.status === 'written').map(x => ({ area: x.area, sections: x.sections, cites: x.sourcesCited })) }
