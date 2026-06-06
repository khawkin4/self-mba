export const meta = {
  name: 'learn-validate',
  description: 'Validate the learn/ units: accuracy + objective-alignment (expert) and beginner-clarity (naive reader), per unit',
  phases: [{ title: 'Validate', detail: 'expert auditor + naive-beginner reader per unit' }],
}

const DIR = '/Users/kalvaryhawkins/self-mba/learn'
const UNITS = [
  'unit-01-reading-the-scoreboard.md',
  'unit-02-cash-vs-profit.md',
  'unit-03-what-a-company-owns-and-owes.md',
  'unit-04-is-it-healthy.md',
]

const AUDIT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['unit', 'accuracyClean', 'accuracyIssues', 'objectivesCovered', 'objectiveIssues'],
  properties: {
    unit: { type: 'string' },
    accuracyClean: { type: 'boolean' },
    accuracyIssues: { type: 'array', items: { type: 'string' } },
    objectivesCovered: { type: 'boolean' },
    objectiveIssues: { type: 'array', items: { type: 'string' } },
  },
}
const BEGINNER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['unit', 'clarity', 'exampleLanded', 'findings'],
  properties: {
    unit: { type: 'string' },
    clarity: { type: 'integer' }, // 1-5
    exampleLanded: { type: 'boolean' },
    findings: { type: 'array', items: {
      type: 'object', additionalProperties: false,
      required: ['issue', 'severity'],
      properties: {
        issue: { type: 'string' },
        severity: { type: 'string', enum: ['blocking', 'minor', 'cosmetic'] },
      } } },
  },
}

phase('Validate')
const results = await pipeline(
  UNITS,
  (u) => parallel([
    () => agent(
      `You are an EXPERT finance/accounting exam auditor. Read this beginner teaching unit and validate it on two things — be a skeptic, recompute everything.
FILE: ${DIR}/${u}
1. ACCURACY: re-derive every numeric figure and every answer given in "Check yourself" and "Application" (margins, leverage = liabilities/equity, the equation A=L+E, cash gaps, etc.). Flag any wrong number, wrong computed answer, or internally inconsistent figure. Do the arithmetic yourself.
2. OBJECTIVE ALIGNMENT: identify the unit's learning objectives (stated or implied). Does its assessment (Check yourself + Application) actually test each objective? Flag any objective taught-but-not-tested, or any question testing something never taught.
Return {unit:"${u}", accuracyClean, accuracyIssues:[...], objectivesCovered, objectiveIssues:[...]}.`,
      { label: `audit:${u.slice(5, 7)}`, phase: 'Validate', schema: AUDIT_SCHEMA }
    ),
    () => agent(
      `Adopt the persona of a SMART ADULT WITH ZERO BUSINESS OR FINANCE BACKGROUND. You have never heard of revenue, margin, a balance sheet, depreciation, leverage, or a 10-K. Read this unit as that person and report honestly where it fails you.
FILE: ${DIR}/${u}
List each problem as a finding with a SEVERITY — and be disciplined about severity, this is the most important part:
- **blocking**: a true beginner genuinely CANNOT understand the unit's core concept here, or would get a wrong mental model (e.g. a computation stated as a result they can't follow; a key idea tested but never taught). These are the only things that should fail a unit.
- **minor**: a term you could infer from context but that really should be glossed (e.g. "public company", "top line"). Worth fixing eventually; not a blocker.
- **cosmetic**: idioms/style a novice can ride past ("turned the corner", "threw off"). Nice-to-have.
Do NOT inflate severity. A unit with only minor/cosmetic findings is GOOD ENOUGH for a learner. Reserve 'blocking' for genuine comprehension breakers.
Also give: exampleLanded (did the real example make the concept click?) and clarity 1–5 (5 = a total beginner would understand and could do the Application).
Return {unit:"${u}", clarity, exampleLanded, findings:[{issue, severity}]}.`,
      { label: `beginner:${u.slice(5, 7)}`, phase: 'Validate', schema: BEGINNER_SCHEMA }
    ),
  ])
)

const byUnit = results.map((pair, i) => {
  const [audit, beg] = pair
  const findings = (beg && beg.findings) || []
  const blocking = findings.filter(f => f.severity === 'blocking')
  // gate: accuracy clean + objectives covered + clarity>=4 + NO blocking comprehension breakers.
  // minor/cosmetic findings are backlog, not gate-failers.
  const pass = !!(audit && beg && audit.accuracyClean && audit.objectivesCovered && beg.clarity >= 4 && blocking.length === 0)
  return { unit: UNITS[i], pass, audit, beginner: beg, blocking, findings }
})
const passed = byUnit.filter(u => u.pass).length
log(`validated ${UNITS.length} units · ${passed} pass · blocking issues: ${byUnit.reduce((a, u) => a + u.blocking.length, 0)}`)
return {
  passed, total: UNITS.length,
  units: byUnit.map(u => ({
    unit: u.unit, pass: u.pass,
    clarity: u.beginner?.clarity,
    accuracyClean: u.audit?.accuracyClean,
    blocking: u.blocking.map(f => f.issue),
    minor: u.findings.filter(f => f.severity === 'minor').map(f => f.issue),
    cosmetic: u.findings.filter(f => f.severity === 'cosmetic').length,
    accuracyIssues: u.audit?.accuracyIssues || [],
    objectiveIssues: u.audit?.objectiveIssues || [],
    exampleLanded: u.beginner?.exampleLanded,
  })),
}
