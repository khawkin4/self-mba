export const meta = {
  name: 'benchmark-gen',
  description: 'Generate an original, exam-calibrated question bank (~104 Qs) blueprinted to the real MBA exams (CFA/GMAT/CLEP/MFT-MBA)',
  phases: [{ title: 'Generate', detail: 'one agent per domain writes original exam-difficulty questions' }],
}

const OUT = '/Users/kalvaryhawkins/self-mba/_ingest/benchmark'
const LESSONS = '/Users/kalvaryhawkins/self-mba/lessons'

const SPECS = [
  { slug: 'finance', domain: 'Finance', n: 10, emulates: 'CFA Level 1 (3-option, computational + concept: time value, ratios, valuation, WACC)', grounding: `${LESSONS}/core-02-corporate-finance.html` },
  { slug: 'accounting', domain: 'Accounting', n: 8, emulates: 'CLEP Financial Accounting + managerial (debits/credits, statements, CVP/break-even, variance)', grounding: `${LESSONS}/gaps-managerial-accounting.html, ${LESSONS}/core-01-accounting.html` },
  { slug: 'economics', domain: 'Economics', n: 8, emulates: 'CLEP Micro/Macro + CFA Econ (elasticity, marginal analysis, supply/demand, opportunity cost)', grounding: `${LESSONS}/core-03-micro-strategy.html` },
  { slug: 'quant-stats', domain: 'Quantitative & Statistics', n: 12, emulates: 'GMAT Quant (5-option problem solving) + Data Insights/Data Sufficiency + StatQuest-level stats (regression, hypothesis tests, p-values, expected value)', grounding: `${LESSONS}/gaps-statistics-quant.html, ${LESSONS}/core-07-data-analytics.html` },
  { slug: 'strategy', domain: 'Strategy', n: 12, emulates: 'MFT-MBA strategic integration + GMAT Critical Reasoning (scenario/argument analysis: five forces, moats, disruption, game theory)', grounding: `${LESSONS}/core-04-competitive-strategy.html, ${LESSONS}/canon-game-theory.html` },
  { slug: 'marketing', domain: 'Marketing', n: 8, emulates: 'CLEP Principles of Marketing (STP, 4Ps, positioning, CAC/LTV unit economics)', grounding: `${LESSONS}/gaps-marketing-strategy.html, ${LESSONS}/core-05-marketing-brand.html` },
  { slug: 'management-ob', domain: 'Management & OB', n: 12, emulates: 'CLEP Principles of Management + MFT-MBA (applied leadership/OB judgment, motivation, org design, negotiation)', grounding: `${LESSONS}/core-09-leadership-ob.html, ${LESSONS}/core-08-negotiation.html` },
  { slug: 'operations', domain: 'Operations', n: 8, emulates: 'MFT-MBA + GMAT Data Insights (theory of constraints, lean, little\'s law, bottleneck/throughput scenarios)', grounding: `${LESSONS}/core-06-operations.html, ${LESSONS}/canon-systems-complexity.html` },
  { slug: 'information-systems', domain: 'Information Systems', n: 6, emulates: 'CLEP Information Systems (MIS concepts, databases, ERP, data governance)', grounding: `${LESSONS}/gaps-information-systems.html` },
  { slug: 'legal-ethical', domain: 'Legal & Ethical', n: 8, emulates: 'CLEP Introductory Business Law + CFA Ethics (contracts, IP, employment, standards-application scenarios)', grounding: `${LESSONS}/gaps-business-law.html, ${LESSONS}/canon-ethics-judgment.html` },
  { slug: 'international', domain: 'International Business', n: 6, emulates: 'MFT-MBA international (trade, FX, entry modes, country risk scenarios)', grounding: `${LESSONS}/core-11-global-macro.html` },
  { slug: 'communication', domain: 'Communication', n: 6, emulates: 'applied business communication judgment (pyramid principle, audience, data viz integrity)', grounding: `${LESSONS}/exec-E7-exec-presence-comms.html` },
]

const GEN_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['slug', 'count', 'file'],
  properties: { slug: { type: 'string' }, count: { type: 'integer' }, file: { type: 'string' } },
}

phase('Generate')
const INSTRUCTIONS = (s) => `You are writing an ORIGINAL, exam-calibrated question set for a self-MBA benchmark. These must read like a real standardized exam — APPLICATION and COMPUTATION difficulty, NOT simple recall.

DOMAIN: ${s.domain}
WRITE: ${s.n} questions
CALIBRATE TO: ${s.emulates}

CRITICAL INTEGRITY RULES:
- Write 100% ORIGINAL questions. Do NOT copy, paraphrase, or lightly edit any real CFA/GMAT/CLEP/MFT-MBA question. Invent your own scenarios, companies, and numbers.
- Match the *difficulty, format, and cognitive style* of the named exam — not its content verbatim.
- Prefer scenario/word-problem/computation over "define X". For quant/finance/accounting, include real numbers the test-taker must work. For strategy/management/ethics, use short scenarios requiring judgment.
- Each question must have ONE unambiguously best answer and plausible distractors.

OPTIONAL GROUNDING (for accuracy/level, not copying): you may skim ${s.grounding} to match the concepts our curriculum teaches.

OUTPUT: write a JSON array to ${OUT}/${s.slug}.json — each element:
{ "domain": "${s.domain}", "emulates": "<short exam tag e.g. 'CFA L1' / 'GMAT Quant' / 'CLEP'>",
  "q": "<question, include any numbers/scenario>", "opts": ["...", "...", "...", "..."],
  "correct": <0-based index>, "rationale": "<1-2 sentences why correct + why others fail>" }
Use 3 options for CFA-style, 5 for GMAT-quant-style, else 4. Make the JSON valid (escape quotes). Create the ${OUT} dir if needed (\`mkdir -p ${OUT}\`).

Return: {slug:"${s.slug}", count:${s.n}, file:"${OUT}/${s.slug}.json"}.`

const res = await parallel(
  SPECS.map((s) => () => agent(INSTRUCTIONS(s), { label: `gen:${s.slug}`, phase: 'Generate', schema: GEN_SCHEMA }))
)
const ok = res.filter(Boolean)
log(`generated ${ok.reduce((a, b) => a + (b.count || 0), 0)} questions across ${ok.length} domains`)
return { domains: ok.map(x => ({ d: x.slug, n: x.count })) }
