export const meta = {
  name: 'benchmark-verify',
  description: 'Adversarially verify the 104 calibrated benchmark answer keys: independent re-solve per domain, flag wrong/ambiguous keys',
  phases: [{ title: 'Verify', detail: 'one solver per domain re-works every question and flags issues' }],
}

const SRC = '/Users/kalvaryhawkins/self-mba/_ingest/benchmark'
const SLUGS = ['finance', 'accounting', 'economics', 'quant-stats', 'strategy', 'marketing',
  'management-ob', 'operations', 'information-systems', 'legal-ethical', 'international', 'communication']

const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['slug', 'total', 'flagged'],
  properties: {
    slug: { type: 'string' }, total: { type: 'integer' },
    flagged: { type: 'array', items: {
      type: 'object', additionalProperties: false,
      required: ['idx', 'issue', 'markedCorrect', 'shouldBe', 'note'],
      properties: {
        idx: { type: 'integer' },
        issue: { type: 'string', enum: ['wrong_key', 'multiple_correct', 'ambiguous', 'factual_error', 'weak_distractor', 'none_correct'] },
        markedCorrect: { type: 'integer' },
        shouldBe: { type: 'integer', description: 'the index you believe is correct; -1 if no single option is correct' },
        note: { type: 'string' },
      } } },
  },
}

phase('Verify')
const INSTRUCTIONS = (slug) => `You are an exam answer-key auditor. Independently re-solve every question in this domain file and flag any whose marked answer is wrong, ambiguous, or has a second defensible answer. Be a skeptic: SOLVE the question yourself FIRST (show the math for computational ones in your reasoning), THEN compare to the marked key. Do not rubber-stamp.

FILE: ${SRC}/${slug}.json  (a JSON array; each item has q, opts, correct (0-based), rationale)

For EACH question:
1. Read q + opts. Work out the correct answer yourself from first principles — recompute every number, check every claimed fact. For finance/quant/accounting, actually do the arithmetic (you may use \`python3 -c\` via Bash to check a calculation).
2. Compare your answer to the marked "correct" index.
3. Flag it ONLY if there's a real problem:
   - wrong_key: the marked answer is incorrect; another option is right.
   - multiple_correct: two+ options are defensibly correct.
   - none_correct: no option is correct (shouldBe = -1).
   - ambiguous: question is unclear/underspecified enough that the key is debatable.
   - factual_error: a stated fact/number in the stem or options is wrong.
   - weak_distractor: technically keyed right but a distractor is so close it's unfair (low priority — only if notable).
Do NOT flag questions that are fine.

Return: {slug:"${slug}", total:<#questions in file>, flagged:[{idx, issue, markedCorrect, shouldBe, note}]}.
- idx = 0-based position in the file. shouldBe = the index YOU believe correct (or -1). note = one sentence: the error + your reasoning (with the number if computational).`

const res = await parallel(
  SLUGS.map((slug) => () => agent(INSTRUCTIONS(slug), { label: `verify:${slug}`, phase: 'Verify', schema: VERIFY_SCHEMA }))
)
const ok = res.filter(Boolean)
const allFlags = ok.flatMap(r => (r.flagged || []).map(f => ({ slug: r.slug, ...f })))
log(`verified ${ok.reduce((a, b) => a + (b.total || 0), 0)} questions · ${allFlags.length} flagged`)
return {
  totalVerified: ok.reduce((a, b) => a + (b.total || 0), 0),
  flagCount: allFlags.length,
  byIssue: allFlags.reduce((m, f) => { m[f.issue] = (m[f.issue] || 0) + 1; return m }, {}),
  flags: allFlags,
}
