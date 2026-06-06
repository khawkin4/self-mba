export const meta = {
  name: 'generate-mba-lessons',
  description: 'Author the remaining 22 MBA lessons as real corpus extractions',
  phases: [
    { title: 'Author', detail: 'one agent per module: read corpus, write grounded interactive lesson' },
    { title: 'Lint', detail: 'grounding check: flag fabricated source URLs' },
  ],
}

const RAW = '/Users/kalvaryhawkins/self-mba/_ingest/raw/2026-06-05'
const OUT = '/Users/kalvaryhawkins/self-mba/lessons'

// Remaining modules (01 Accounting + 02 Corp Finance already authored).
const MODULES = [
  ['core','03-micro-strategy','Microeconomics & Strategy', null],
  ['core','04-competitive-strategy','Competitive Strategy', {t:['NFLX','DIS'], role:'Five Forces backed by real risk factors + segment economics; Netflix vs Disney'}],
  ['core','05-marketing-brand','Marketing & Brand', {t:['NKE'], role:'brand pricing power read in real gross margin'}],
  ['core','06-operations','Operations & Supply Chain', {t:['AMZN','WMT'], role:'margin structure & scale; Amazon (~? margin) vs Walmart (~3% net margin, high turnover)'}],
  ['core','07-data-analytics','Data, Analytics & Decisions', null],
  ['core','08-negotiation','Negotiation', null],
  ['core','09-leadership-ob','Leadership & Org Behavior', null],
  ['core','10-entrepreneurship','Entrepreneurship & Venture', null],
  ['core','11-global-macro','Global Strategy & Macro', null],
  ['core','12-capstone','Capstone', {t:['BRK-B'], role:'full integrative teardown of a real company'}],
  ['exec','E1-leading-at-scale','Leading at Scale', null],
  ['exec','E2-capital-allocation','Capital Allocation', {t:['AAPL','BRK-B'], role:'buybacks vs reinvestment read from real cash-flow statements'}],
  ['exec','E3-mergers-acquisitions','M&A & Restructuring', {t:['MSFT'], role:'acquirer balance-sheet capacity for deals'}],
  ['exec','E4-governance-board','Governance & The Board', {t:['DIS','JPM'], role:'board structure & exec comp via the companies'}],
  ['exec','E5-transformation','Transformation at Scale', null],
  ['exec','E6-crisis-leadership','Crisis Leadership', null],
  ['exec','E7-exec-presence-comms','Executive Presence & Comms', null],
  ['exec','E8-stakeholder-ir','Stakeholder & Investor Relations', null],
  ['exec','E9-geopolitics-macro','Geopolitics & Macro', null],
  ['exec','E10-digital-ai','Digital & AI Transformation', null],
  ['exec','E11-operating-system','Personal Operating System', null],
  ['exec','E12-culture-strategy','Culture as Strategy', null],
]

const COMPONENTS = `
Use ONLY these styled components (no inline styles, no other classes):
- <p class="lead">opening (auto drop-cap)</p>
- <h2>1 · Section</h2> (number sections)
- <div class="reveal"><button class="reveal-q">Prompt</button><div class="reveal-a"><p>Answer</p></div></div>
- Flip-card vocab grid (define 6-8 key terms): <div class="fc-grid"> then repeat
  <button class="fc"><span class="fc-inner"><span class="fc-f"><b>Term</b><span class="hint">tap to flip ↻</span></span><span class="fc-b">Plain-English definition</span></span></button>
- <div class="equation">A short formula or core relationship</div> (optional)
- A custom SVG diagram that TEACHES a core idea, inside:
  <figure class="viz"><svg viewBox="0 0 720 200" role="img" aria-label="..."> ... </svg><figcaption>...</figcaption></figure>
  Use <rect> with classes bar-rev / bar-gross / bar-net (or bar-asset/bar-liab/bar-eq) — widths PROPORTIONAL to real values; add data-tip="explanation" to each rect for hover tooltips; <text class="vlabel">labels</text>, <text class="bar-txt">centered values</text>. For non-financial modules, visualize a framework (a 2x2, a funnel, a spectrum, a process) using the same shapes.
- <div class="example"><p>worked example</p></div>
- <div class="pitfall"><h3>⚠️ Title</h3><p>...</p></div> and one <div class="pitfall subtle"><h3>🔎 Title</h3><p>bridge to next course</p></div>
- Source quotes (REAL): <blockquote class="srcq"><p>"verbatim sentence from a transcript"</p><cite><a href="REAL_URL" target="_blank" rel="noopener">— Channel, "Title"</a> · in your corpus</cite></blockquote>
- Quiz (data-correct = 0-based index): <div class="quizq" data-correct="1"><p class="q">Q?</p><button class="opt">A</button><button class="opt">B</button><button class="opt">C</button><p class="fb">Why the answer is right.</p></div>
- <div class="apply-box"><h3>🎯 Your move</h3><p>a concrete exercise</p></div>
- <div class="src-list"><h4>📚 Taught from these sources in your corpus</h4><ul><li><a href="REAL_URL" target="_blank" rel="noopener">Channel — Title</a></li> ...4-5 real videos... </ul><p style="margin:8px 0 0;color:var(--dim)">Full transcripts of every lecture are below ↓</p></div>`

function prompt([track, id, title, edgar]) {
  const dir = `${RAW}/${track}/${id}`
  const edgarBlock = edgar
    ? `\nREAD the EDGAR financial files in ${dir} (edgar_*.txt) and use the REAL numbers: ${edgar.role}. Build at least one diagram and the worked example from these actual figures (compute real margins/ratios). Tickers: ${edgar.t.join(', ')}.`
    : `\nThis module has NO financial data — do NOT invent any. Teach via frameworks, real examples from the transcripts, and conceptual diagrams (2x2 / funnel / process / spectrum).`
  return `You are authoring ONE interactive lesson for a self-directed MBA web app. This is REAL EXTRACTION: read the actual source corpus and distill it into a TAUGHT lesson (beginner-friendly, correct terminology, visual-first, interactive). The lesson is the takeaway; transcripts are just citations.

MODULE: ${title} (id: ${id})

1) READ THE CORPUS with the Read tool:
- Transcripts: read the JSON files matching ${dir}/yt_*.json — to control time, read the FIRST 5 files only. Each is a list of {id,title,channel,url,transcript,...}. Extract the genuine concepts, terms, frameworks, and examples the lecturers actually teach.
- Curated practitioner discussion: ${dir}/curated_reddit.json (use 1-2 genuinely useful threads if relevant).${edgarBlock}

2) STUDY THE EXEMPLARS for structure & quality bar (read both):
${OUT}/core-01-accounting.html and ${OUT}/core-02-corporate-finance.html
${COMPONENTS}

RULES:
- Ground everything: every <blockquote class="srcq"> must quote a REAL sentence from a transcript with that video's REAL url; the src-list must link REAL videos from the json. NEVER invent sources, quotes, numbers, or URLs.
- Beginner-friendly but precise. Visual-first and interactive: include multiple reveals, a full flip-card grid (6-8 terms), >=2 quizzes, >=1 teaching diagram.
- Output an HTML FRAGMENT ONLY (no <html>/<head>/<body>/<style>) — start with an HTML comment then <p class="lead">.

3) WRITE the fragment to: ${OUT}/${track}-${id}.html

Then return ONE line: the module id + the real video titles you quoted. Do NOT return the HTML.`
}

phase('Author')
log(`Authoring ${MODULES.length} lessons as corpus extractions…`)

const results = await pipeline(
  MODULES,
  (m) => agent(prompt(m), { label: `author:${m[1]}`, phase: 'Author', agentType: 'general-purpose' })
            .then(() => ({ track: m[0], id: m[1], ok: true }))
            .catch(() => ({ track: m[0], id: m[1], ok: false })),
  // Lint stage: verify the written fragment's source URLs actually exist in the corpus json.
  (r, m) => agent(
    `Grounding lint for one MBA lesson. Read the fragment ${OUT}/${m[0]}-${m[1]}.html and the corpus transcripts ${RAW}/${m[0]}/${m[1]}/yt_*.json. ` +
    `Collect every href in the fragment's <blockquote class="srcq"> and <div class="src-list"> that points to youtube. Check each appears as a "url" in the transcript json. ` +
    `If ANY youtube href is fabricated (not in the json), FIX the fragment by replacing it with a real url+title from the json (Write the corrected file). ` +
    `Also confirm the fragment contains: a .lead, a .fc-grid, >=2 .quizq, >=1 <svg>. ` +
    `Return JSON only.`,
    { label: `lint:${m[1]}`, phase: 'Lint', agentType: 'general-purpose',
      schema: { type:'object', required:['id','fabricated_fixed','ok'], properties:{
        id:{type:'string'}, fabricated_fixed:{type:'integer'}, ok:{type:'boolean'}, notes:{type:'string'} } } }
  ).then(v => ({ ...r, lint: v })).catch(() => ({ ...r, lint: null }))
)

const ok = results.filter(r => r && r.ok).length
const fixed = results.reduce((n, r) => n + (r?.lint?.fabricated_fixed || 0), 0)
log(`Done: ${ok}/${MODULES.length} authored, ${fixed} fabricated source URLs auto-fixed.`)
return { authored: ok, total: MODULES.length, fabricated_fixed: fixed,
         results: results.map(r => ({ id: r?.id, ok: r?.ok, lint: r?.lint })) }
