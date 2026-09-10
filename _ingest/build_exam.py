#!/usr/bin/env python3
"""Harvest the quiz questions baked into every lesson, tag each to an MFT-MBA domain,
and emit a self-contained, self-scoring diagnostic exam -> site/dist/exam.html.

Run:  python3 _ingest/build_exam.py     (after site is built; reuses style.css)
"""
import glob, html, json, os, re

ROOT = os.path.expanduser("~/self-mba")
LESSONS = os.path.join(ROOT, "lessons")
DIST = os.path.join(ROOT, "site", "dist")

# lesson-file stem -> MFT-MBA / CPC domain
DOMAIN = {
    # core
    "core-01-accounting": "Accounting", "core-02-corporate-finance": "Finance",
    "core-03-micro-strategy": "Economics", "core-04-competitive-strategy": "Strategy",
    "core-05-marketing-brand": "Marketing", "core-06-operations": "Operations",
    "core-07-data-analytics": "Quantitative & Statistics", "core-08-negotiation": "Management & OB",
    "core-09-leadership-ob": "Management & OB", "core-10-entrepreneurship": "Strategy",
    "core-11-global-macro": "International Business", "core-12-capstone": "Integration",
    # exec
    "exec-E1-leading-at-scale": "Management & OB", "exec-E2-capital-allocation": "Finance",
    "exec-E3-mergers-acquisitions": "Finance", "exec-E4-governance-board": "Legal & Ethical",
    "exec-E5-transformation": "Management & OB", "exec-E6-crisis-leadership": "Management & OB",
    "exec-E7-exec-presence-comms": "Communication", "exec-E8-stakeholder-ir": "Communication",
    "exec-E9-geopolitics-macro": "International Business", "exec-E10-digital-ai": "Information Systems",
    "exec-E11-operating-system": "Management & OB", "exec-E12-culture-strategy": "Management & OB",
    # canon
    "canon-game-theory": "Economics", "canon-behavioral-decision": "Quantitative & Statistics",
    "canon-risk-fragility": "Quantitative & Statistics", "canon-systems-complexity": "Operations",
    "canon-platform-strategy": "Strategy", "canon-history-judgment": "Strategy",
    "canon-power-politics": "Management & OB", "canon-information-communication": "Communication",
    "canon-ethics-judgment": "Legal & Ethical",
    # gaps (Technical Foundations)
    "gaps-managerial-accounting": "Accounting", "gaps-statistics-quant": "Quantitative & Statistics",
    "gaps-marketing-strategy": "Marketing", "gaps-information-systems": "Information Systems",
    "gaps-business-law": "Legal & Ethical",
}

def clean(s):
    s = re.sub(r"<[^>]+>", "", s)             # strip inner tags
    s = html.unescape(s).replace("\n", " ")
    return re.sub(r"\s+", " ", s).strip()

QUIZ = re.compile(r'<div class="quizq"\s+data-correct="(\d+)"\s*>(.*?)</div>', re.S)
QTEXT = re.compile(r'<p class="q">(.*?)</p>', re.S)
OPT = re.compile(r'<button class="opt">(.*?)</button>', re.S)
FB = re.compile(r'<p class="fb">(.*?)</p>', re.S)

bank = []
for path in sorted(glob.glob(os.path.join(LESSONS, "*.html"))):
    stem = os.path.basename(path)[:-5]
    domain = DOMAIN.get(stem)
    if not domain:
        continue
    txt = open(path, encoding="utf-8").read()
    for i, (correct, body) in enumerate(QUIZ.findall(txt)):
        qm, opts, fbm = QTEXT.search(body), OPT.findall(body), FB.search(body)
        if not qm or len(opts) < 2:
            continue
        bank.append({
            "id": f"{stem}-{i}", "domain": domain,
            "q": clean(qm.group(1)), "opts": [clean(o) for o in opts],
            "correct": int(correct), "fb": clean(fbm.group(1)) if fbm else "",
            "src": stem,
        })

# distribution report
from collections import Counter
dist = Counter(q["domain"] for q in bank)
print(f"harvested {len(bank)} questions from {len({q['src'] for q in bank})} lessons")
for d, n in sorted(dist.items(), key=lambda x: -x[1]):
    print(f"  {d:28} {n}")

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diagnostic Exam · The Compounding MBA</title>
<link rel="stylesheet" href="style.css">
<style>
.exam-wrap{max-width:760px;margin:0 auto;padding:30px 24px 120px}
.exam-q{border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 14px;background:var(--surface)}
.exam-q .dtag{font:600 .62rem/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--brass);margin-bottom:8px;display:inline-block}
.exam-q .qn{font:600 1.02rem/1.5 var(--read);color:var(--ink);margin:0 0 12px}
.exam-opt{display:block;width:100%;text-align:left;padding:11px 14px;margin:6px 0;border:1px solid var(--line2);border-radius:7px;background:var(--bg2);color:var(--ink2);font:.96rem var(--read);cursor:pointer;transition:.15s}
.exam-opt:hover{border-color:var(--brass)}
.exam-opt.sel{border-color:var(--brass);background:rgba(203,162,79,.12);color:var(--ink)}
.exam-opt.correct{border-color:var(--core);background:rgba(132,173,138,.16);color:var(--ink)}
.exam-opt.wrong{border-color:var(--wrong);background:rgba(207,106,90,.14)}
.exam-fb{margin:10px 0 0;font:.9rem/1.55 var(--read);color:var(--dim);display:none}
.exam-fb.show{display:block}
#scorebar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:14px 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
#scorebar b{color:var(--brass2)}
.bigbtn{padding:13px 26px;border:0;border-radius:8px;background:var(--brass);color:#0c100e;font:600 .95rem var(--mono);letter-spacing:.04em;cursor:pointer}
.bigbtn:disabled{opacity:.4;cursor:default}
.result{border:1px solid var(--brass);border-radius:12px;padding:24px;margin:0 0 22px;background:var(--surface2);display:none}
.result.show{display:block;animation:rise .5s both}
.result h2{margin:0 0 6px;font:300 2.4rem/1 var(--serif);color:var(--ink)}
.result .band{font:600 .8rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass)}
.dom-row{display:grid;grid-template-columns:200px 1fr 64px;gap:12px;align-items:center;margin:9px 0;font:.9rem var(--read)}
.dom-bar{height:9px;border-radius:5px;background:var(--line);overflow:hidden}
.dom-bar > i{display:block;height:100%;background:linear-gradient(90deg,var(--core),var(--brass2))}
.note{font:.84rem/1.6 var(--read);color:var(--dim);border-left:2px solid var(--line2);padding-left:14px;margin:18px 0}
@media(max-width:560px){.dom-row{grid-template-columns:120px 1fr 50px}}
</style></head><body>
<div id="scorebar">
<a href="index.html" class="home" style="font:.8rem var(--mono);color:var(--dim)">&larr; Index</a>
<span style="font:600 .8rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink)">Diagnostic Exam</span>
<span id="prog" style="font:.82rem var(--mono);color:var(--dim)"></span>
<button id="submit" class="bigbtn" style="margin-left:auto">Submit &amp; Score</button>
<button id="retake" class="bigbtn" style="display:none;background:var(--surface2);color:var(--ink);border:1px solid var(--line2)">Retake</button>
</div>
<div class="exam-wrap">
<div class="result" id="result"></div>
<p class="note" id="introNote"></p>
<div id="questions"></div>
</div>
<script>
const BANK = __BANK__;
const BLUEPRINT = __BLUEPRINT__;  // MFT-MBA relative emphasis
let order=[], answers={};
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function render(){
  order = BANK.map((q,i)=>i); shuffle(order); answers={};
  const wrap=document.getElementById('questions'); wrap.innerHTML='';
  order.forEach((qi,n)=>{
    const q=BANK[qi];
    const div=document.createElement('div'); div.className='exam-q'; div.id='q'+qi;
    div.innerHTML='<span class="dtag">'+(n+1)+' &middot; '+q.domain+'</span><p class="qn">'+q.q+'</p>'+
      q.opts.map((o,oi)=>'<button class="exam-opt" data-q="'+qi+'" data-o="'+oi+'">'+o+'</button>').join('')+
      '<p class="exam-fb">'+q.fb+'</p>';
    wrap.appendChild(div);
  });
  document.querySelectorAll('.exam-opt').forEach(b=>b.addEventListener('click',function(){
    const qi=this.dataset.q;
    const qDiv=document.getElementById('q'+qi);
    if(qDiv.classList.contains('done'))return;
    qDiv.classList.add('done');
    const q=BANK[qi], chosen=+this.dataset.o;
    answers[qi]=chosen;
    const opts=qDiv.querySelectorAll('.exam-opt');
    opts.forEach((o,oi)=>{
      o.style.pointerEvents='none';
      if(oi===q.correct)o.classList.add('correct');
      if(oi===chosen&&chosen!==q.correct)o.classList.add('wrong');
    });
    const fb=qDiv.querySelector('.exam-fb');
    if(fb)fb.classList.add('show');
    updateProg();
  }));
  document.getElementById('result').classList.remove('show');
  document.getElementById('result').innerHTML='';
  document.getElementById('submit').style.display=''; document.getElementById('retake').style.display='none';
  updateProg(); window.scrollTo(0,0);
}
function updateProg(){
  const n=Object.keys(answers).length;
  const c=Object.keys(answers).filter(qi=>answers[qi]===BANK[qi].correct).length;
  document.getElementById('prog').textContent=c+' correct · '+n+' / '+BANK.length+' answered';
}
function band(p){return p>=85?'Distinction':p>=70?'Pass (solid)':p>=55?'Marginal pass':'Below pass — review';}
function grade(){
  const byDom={}; let correct=0;
  BANK.forEach((q,qi)=>{
    const d=q.domain; byDom[d]=byDom[d]||{c:0,t:0};
    byDom[d].t++; const a=answers[qi];
    const opts=document.querySelectorAll('.exam-opt[data-q="'+qi+'"]');
    opts.forEach((o,oi)=>{if(oi===q.correct)o.classList.add('correct'); if(oi===a&&a!==q.correct)o.classList.add('wrong');});
    document.querySelector('#q'+qi+' .exam-fb').classList.add('show');
    if(a===q.correct){correct++; byDom[d].c++;}
  });
  const pct=Math.round(100*correct/BANK.length);
  const rows=Object.keys(byDom).sort().map(d=>{
    const o=byDom[d], p=Math.round(100*o.c/o.t);
    return '<div class="dom-row"><span>'+d+'</span><span class="dom-bar"><i style="width:'+p+'%"></i></span><span style="text-align:right;color:var(--dim)">'+o.c+'/'+o.t+'</span></div>';
  }).join('');
  const r=document.getElementById('result');
  r.innerHTML='<div class="band">'+band(pct)+'</div><h2>'+pct+'%</h2>'+
    '<p style="color:var(--dim);margin:.2em 0 16px">'+correct+' of '+BANK.length+' correct &middot; self-diagnostic, blueprinted to MFT-MBA domains</p>'+
    '<div style="border-top:1px solid var(--line);padding-top:14px">'+rows+'</div>'+
    '<p class="note" style="margin-top:18px">Indicative only: this scores <b>recall of the taught material</b>, not full MBA mastery. '+
    'Weak domains above are your study targets — open the matching lesson from the Index. Unanswered count as wrong.</p>';
  r.classList.add('show');
  document.getElementById('submit').style.display='none'; document.getElementById('retake').style.display='';
  window.scrollTo({top:0,behavior:'smooth'});
}
document.getElementById('submit').addEventListener('click',grade);
document.getElementById('retake').addEventListener('click',render);
document.getElementById('introNote').textContent=
  BANK.length+' questions across '+new Set(BANK.map(q=>q.domain)).size+' MBA domains, drawn from every lesson\\'s comprehension checks. '+
  'Answer what you can, then Submit & Score for an overall result and a per-domain breakdown.';
render();
</script></body></html>"""

blueprint = {  # directional MFT-MBA emphasis (High/Med) for the report note
    "Strategy": "High", "Finance": "High", "Marketing": "High", "Accounting": "High",
    "Quantitative & Statistics": "High", "Management & OB": "High", "Economics": "Med",
    "Operations": "Med", "Information Systems": "Med", "Legal & Ethical": "Med",
    "International Business": "Med", "Communication": "Med", "Integration": "Med",
}
out = PAGE.replace("__BANK__", json.dumps(bank, ensure_ascii=False)).replace("__BLUEPRINT__", json.dumps(blueprint))
os.makedirs(DIST, exist_ok=True)
open(os.path.join(DIST, "exam.html"), "w", encoding="utf-8").write(out)
print(f"\nwrote {os.path.join(DIST, 'exam.html')} ({len(bank)} questions)")
