export const meta = {
  name: 'acumen-redteam',
  description: 'Red-team a submitted acumen memo: rubric scores, bear case, the boardroom question, and the shelf-debt meta-question',
  phases: [
    { title: 'Red-team', detail: 'rubric scorer + bear case + boardroom question + shelf-debt, per case' },
    { title: 'Ledger', detail: 'assemble the ledger rows' },
  ],
}

// Usage: Workflow({ scriptPath: '_ingest/acumen_redteam_workflow.js',
//                   args: ['2026-09-26', 'case-02-boeing.md'] })   // leading date optional
// Cases: case-01-intel.md (full) · case-02-boeing.md (crux-only) · case-03-carvana.md (single-figure)
//        case-04-disney.md (full). Menu and sizes: acumen/JUDGMENT-LEDGER.md
// The memo must already be pasted under "## YOUR MEMO" in the case file. This workflow never writes
// the memo — it only attacks it. See acumen/MECHANISM.md.

const DIR = '/Users/kalvaryhawkins/self-mba/acumen'
const CANON = '/Users/kalvaryhawkins/self-mba/notes/canon/CANON.md'
// args: an optional leading YYYY-MM-DD (the run date, since Date.now() is unavailable in
// workflow scripts — it breaks resume), then the case filenames.
const ARGV = Array.isArray(args) && args.length ? args : ['case-01-intel.md']
const RUN_DATE = /^\d{4}-\d{2}-\d{2}$/.test(ARGV[0]) ? ARGV[0] : ''
const CASES = RUN_DATE ? ARGV.slice(1) : ARGV

const DIMENSIONS = ['diagnosis', 'conviction', 'evidence', 'landscape', 'comms', 'secondOrder']

const SCORE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['case', 'memoPresent', 'scores', 'cruxUnprompted', 'cruxStated', 'justification'],
  properties: {
    case: { type: 'string' },
    memoPresent: { type: 'boolean' },
    scores: {
      type: 'object', additionalProperties: false,
      required: DIMENSIONS,
      properties: Object.fromEntries(DIMENSIONS.map(d => [d, { type: 'integer' }])), // 1-5
    },
    cruxStated: { type: 'string' },
    cruxUnprompted: { type: 'boolean' },
    justification: { type: 'array', items: { type: 'string' } },
  },
}
const BEAR_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['case', 'bearCase', 'unsupportedClaims', 'presumptionsTreatedAsFact'],
  properties: {
    case: { type: 'string' },
    bearCase: { type: 'string' },
    unsupportedClaims: { type: 'array', items: { type: 'string' } },
    presumptionsTreatedAsFact: { type: 'array', items: { type: 'string' } },
  },
}
const BOARD_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['case', 'question', 'whyItSinks', 'bestAnswerAvailable'],
  properties: {
    case: { type: 'string' },
    question: { type: 'string' },
    whyItSinks: { type: 'string' },
    bestAnswerAvailable: { type: 'string' },
  },
}
const SHELF_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['case', 'note', 'whatItWouldHaveChanged', 'runnerUp'],
  properties: {
    case: { type: 'string' },
    note: { type: 'string' },            // a canon-*.md slug
    whatItWouldHaveChanged: { type: 'string' },
    runnerUp: { type: 'string' },
  },
}

phase('Red-team')
const results = await pipeline(
  CASES,
  (c) => parallel([
    () => agent(
      `You are a SKEPTICAL MANAGING PARTNER grading a board memo. Read the case brief and the memo pasted under "## YOUR MEMO".
FILE: ${DIR}/${c}
RUBRIC in ${DIR}/README.md — score each 1-5, and be hard. 3 = competent, 4 = would survive a real board, 5 = rare.
- diagnosis: did they find the real crux, or restate the obvious?
- conviction: did they RECOMMEND, or hide in a tradeoffs matrix? "It depends" = 1.
- evidence: are the numbers right and the frameworks correctly applied? Verify the figures against the filings yourself where you can; a wrong or unsourced number caps this at 2.
- landscape: did they read the competitive / market / macro reality?
- comms: exec altitude, BLUF, brief — would a CFO buy it in 90 seconds?
- secondOrder: did they see what happens next, and the strongest counter-argument?
Below-a-masters tells that must pull scores down: framework dumping, no recommendation, vanity metrics, ignoring the bear case, treating a presumption as fact.
Also report cruxStated (their crux, verbatim-ish) and cruxUnprompted: TRUE only if the crux they named is NOT simply one of the frameworks listed in the case's own "Canon to bring to bear" section handed to them — i.e. they did the diagnosis rather than picking from the menu.
If no memo has been pasted, set memoPresent false and all scores to 1.
Return {case:"${c}", memoPresent, scores:{...}, cruxStated, cruxUnprompted, justification:[one line per dimension]}.`,
      { label: `score:${c.slice(5, 7)}`, phase: 'Red-team', schema: SCORE_SCHEMA }
    ),
    () => agent(
      `You are the BEAR. Your job is to make the memo's recommendation look naive.
FILE: ${DIR}/${c}
Build the strongest honest case that the recommendation is wrong — not a list of risks, an argument. Use real figures where you can pull them.
Then list: unsupportedClaims (assertions with no figure behind them) and presumptionsTreatedAsFact (things the memo assumes are settled that are actually contested).
Do NOT rewrite their memo or tell them what to recommend instead.
Return {case:"${c}", bearCase, unsupportedClaims:[...], presumptionsTreatedAsFact:[...]}.`,
      { label: `bear:${c.slice(5, 7)}`, phase: 'Red-team', schema: BEAR_SCHEMA }
    ),
    () => agent(
      `You are a BOARD MEMBER with 30 seconds and no patience. Read the memo.
FILE: ${DIR}/${c}
Produce the ONE question that would sink this memo in the room — the question whose answer the author clearly does not have. Not a generic "what about competition"; the specific question this specific memo is defenceless against.
Then: whyItSinks (one sentence), and bestAnswerAvailable — the best answer a well-prepared author COULD have given from the filings, so the author can see the gap.
Return {case:"${c}", question, whyItSinks, bestAnswerAvailable}.`,
      { label: `board:${c.slice(5, 7)}`, phase: 'Red-team', schema: BOARD_SCHEMA }
    ),
    () => agent(
      `You audit the SHELF, not the memo. This is the meta-inspection question from acumen/MECHANISM.md.
MEMO: ${DIR}/${c}
CANON INDEX: ${CANON} (82 notes across 23 clusters; each entry has a one-line core claim)
Read the memo's reasoning and its gaps. Then name the ONE canon note that, had the author actually read it, would have MATERIALLY CHANGED this memo — a different crux, a different call, or a risk they missed. Be specific about what would have changed.
Rules: name a note that exists in the index, by its canon-*.md slug. Prefer a note the case brief did NOT already hand them in its "Canon to bring to bear" list — the point is to find the shelf they didn't reach for. If the honest answer is one the brief listed, say so anyway.
Return {case:"${c}", note, whatItWouldHaveChanged, runnerUp}.`,
      { label: `shelf:${c.slice(5, 7)}`, phase: 'Red-team', schema: SHELF_SCHEMA }
    ),
  ])
)

phase('Ledger')
const reps = results.map((quad, i) => {
  const [score, bear, board, shelf] = quad
  const s = score?.scores || {}
  const vals = DIMENSIONS.map(d => s[d]).filter(v => typeof v === 'number')
  const avg = vals.length ? vals.reduce((a, b) => a + b, 0) / vals.length : null
  const below4 = DIMENSIONS.filter(d => typeof s[d] === 'number' && s[d] < 4)
  const pass = avg !== null && avg >= 3.5
  const boardReady = avg !== null && avg >= 4.5 && below4.length === 0
  return {
    case: CASES[i],
    memoPresent: !!score?.memoPresent,
    scores: s,
    avg: avg === null ? null : Math.round(avg * 100) / 100,
    pass, boardReady,
    dimensionsBelow4: below4,
    cruxStated: score?.cruxStated,
    cruxUnprompted: !!score?.cruxUnprompted,
    justification: score?.justification || [],
    bearCase: bear?.bearCase,
    unsupportedClaims: bear?.unsupportedClaims || [],
    presumptionsTreatedAsFact: bear?.presumptionsTreatedAsFact || [],
    boardroomQuestion: board?.question,
    whyItSinks: board?.whyItSinks,
    bestAnswerAvailable: board?.bestAnswerAvailable,
    shelfDebt: shelf?.note,
    shelfDebtWhy: shelf?.whatItWouldHaveChanged,
    shelfDebtRunnerUp: shelf?.runnerUp,
    // paste-ready row for the Scores table in acumen/JUDGMENT-LEDGER.md
    ledgerRow: `| ${CASES[i].slice(5, 7)} | ${CASES[i].replace(/^case-\d+-/, '').replace(/\.md$/, '')} | ${RUN_DATE || '—'} | ${DIMENSIONS.map(d => s[d] ?? '—').join(' | ')} | ${avg === null ? '—' : avg.toFixed(2)} | ${score?.cruxUnprompted ? 'yes' : 'no'} |`,
    shelfRow: `| ${CASES[i].slice(5, 7)} | ${shelf?.note || '—'} | 1 | no | no |`,
  }
})

const scored = reps.filter(r => r.memoPresent).length
log(`red-teamed ${CASES.length} case(s) · ${scored} with a memo present · ${reps.filter(r => r.pass).length} pass (avg >= 3.5)`)
if (scored < CASES.length) log('NOTE: a case with no memo pasted scores 1s by design — that is a skipped rep, log it as `skipped` in the ledger rather than as a score.')
return { reps, updateLedger: 'acumen/JUDGMENT-LEDGER.md — paste ledgerRow into Scores, shelfRow into Shelf debt, and set the input metrics' }
