#!/usr/bin/env python3
"""Assemble the generated exam-calibrated question bank (_ingest/benchmark/*.json)
into a self-scoring BENCHMARK exam -> site/dist/benchmark-exam.html.
Harder than the recall self-diagnostic; calibrated to CFA/GMAT/CLEP/MFT-MBA and
linked to their official free practice. Run after benchmark_gen_workflow.js.
"""
import glob, html, json, os

ROOT = os.path.expanduser("~/self-mba")
SRC = os.path.join(ROOT, "_ingest", "benchmark")
DIST = os.path.join(ROOT, "site", "dist")

bank = []
for f in sorted(glob.glob(os.path.join(SRC, "*.json"))):
    try:
        for q in json.load(open(f, encoding="utf-8")):
            if q.get("q") and isinstance(q.get("opts"), list) and len(q["opts"]) >= 2 \
               and isinstance(q.get("correct"), int) and 0 <= q["correct"] < len(q["opts"]):
                bank.append({"domain": q.get("domain", "?"), "emulates": q.get("emulates", ""),
                             "q": q["q"], "opts": q["opts"], "correct": q["correct"],
                             "rationale": q.get("rationale", "")})
    except Exception as ex:
        print(f"  ! {os.path.basename(f)}: {ex}")

from collections import Counter
dist = Counter(q["domain"] for q in bank)
print(f"benchmark bank: {len(bank)} original calibrated questions")
for d, n in sorted(dist.items(), key=lambda x: -x[1]):
    print(f"  {d:28} {n}")

LINKS = ('<div class="note"><b>Sit the real thing.</b> This is an original, exam-calibrated proxy — '
         'for a true external score take an official free practice exam and bring it back: '
         '<a href="https://www.mba.com/exams/gmat-exam/about/exam-content" target="_blank" rel="noopener">GMAT Focus Official Starter Kit</a> · '
         '<a href="https://clep.collegeboard.org/prepare-for-an-exam/practice-questions-study-guides" target="_blank" rel="noopener">CLEP sample questions</a> · '
         '<a href="https://www.cfainstitute.org/programs/cfa-program/candidate-resources/level-i-exam" target="_blank" rel="noopener">CFA Level I practice</a>. '
         'See <code>notes/canon/BENCHMARK-EXTERNAL.md</code> for the full mapping.</div>')

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Calibrated Benchmark Exam · The Compounding MBA</title>
<link rel="stylesheet" href="style.css">
<style>
.exam-wrap{max-width:780px;margin:0 auto;padding:26px 24px 120px}
.exam-q{border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 14px;background:var(--surface)}
.exam-q .dtag{font:600 .62rem/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass);margin-bottom:8px;display:flex;justify-content:space-between;gap:10px}
.exam-q .dtag .emu{color:var(--exec)}
.exam-q .qn{font:600 1.02rem/1.55 var(--read);color:var(--ink);margin:0 0 12px;white-space:pre-wrap}
.exam-opt{display:block;width:100%;text-align:left;padding:11px 14px;margin:6px 0;border:1px solid var(--line2);border-radius:7px;background:var(--bg2);color:var(--ink2);font:.96rem var(--read);cursor:pointer;transition:.15s}
.exam-opt:hover{border-color:var(--brass)}
.exam-opt.sel{border-color:var(--brass);background:rgba(203,162,79,.12);color:var(--ink)}
.exam-opt.correct{border-color:var(--core);background:rgba(132,173,138,.16);color:var(--ink)}
.exam-opt.wrong{border-color:var(--wrong);background:rgba(207,106,90,.14)}
.exam-fb{margin:10px 0 0;font:.9rem/1.55 var(--read);color:var(--dim);display:none}
.exam-fb.show{display:block}
#scorebar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:14px 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.bigbtn{padding:13px 26px;border:0;border-radius:8px;background:var(--brass);color:#0c100e;font:600 .95rem var(--mono);letter-spacing:.04em;cursor:pointer}
.result{border:1px solid var(--brass);border-radius:12px;padding:24px;margin:0 0 22px;background:var(--surface2);display:none}
.result.show{display:block;animation:rise .5s both}
.result h2{margin:0 0 6px;font:300 2.6rem/1 var(--serif);color:var(--ink)}
.result .band{font:600 .8rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brass)}
.dom-row{display:grid;grid-template-columns:210px 1fr 64px;gap:12px;align-items:center;margin:9px 0;font:.9rem var(--read)}
.dom-bar{height:9px;border-radius:5px;background:var(--line);overflow:hidden}.dom-bar>i{display:block;height:100%;background:linear-gradient(90deg,var(--core),var(--brass2))}
.note{font:.84rem/1.65 var(--read);color:var(--dim);border-left:2px solid var(--line2);padding-left:14px;margin:18px 0}
@media(max-width:560px){.dom-row{grid-template-columns:120px 1fr 50px}}
</style></head><body>
<div class="grain"></div><div class="atmos"></div>
<div id="scorebar">
<a href="index.html" style="font:.8rem var(--mono);color:var(--dim);text-decoration:none">&larr; Index</a>
<span style="font:600 .8rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink)">Calibrated Benchmark Exam</span>
<span id="prog" style="font:.82rem var(--mono);color:var(--dim)"></span>
<button id="submit" class="bigbtn" style="margin-left:auto">Submit &amp; Score</button>
<button id="retake" class="bigbtn" style="display:none;background:var(--surface2);color:var(--ink);border:1px solid var(--line2)">Retake</button>
</div>
<div class="exam-wrap">
<div class="result" id="result"></div>
<p class="note" id="introNote"></p>
__LINKS__
<div id="questions"></div>
</div>
<script>
const BANK = __BANK__;
let order=[], answers={};
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function render(){
  order=BANK.map((q,i)=>i); shuffle(order); answers={};
  const wrap=document.getElementById('questions'); wrap.innerHTML='';
  order.forEach((qi,n)=>{const q=BANK[qi];
    const div=document.createElement('div'); div.className='exam-q'; div.id='q'+qi;
    div.innerHTML='<div class="dtag"><span>'+(n+1)+' &middot; '+q.domain+'</span><span class="emu">'+(q.emulates||'')+'</span></div>'+
      '<p class="qn">'+q.q+'</p>'+
      q.opts.map((o,oi)=>'<button class="exam-opt" data-q="'+qi+'" data-o="'+oi+'">'+o+'</button>').join('')+
      '<p class="exam-fb">'+(q.rationale||'')+'</p>';
    wrap.appendChild(div);});
  document.querySelectorAll('.exam-opt').forEach(b=>b.addEventListener('click',function(){
    if(document.getElementById('result').classList.contains('show'))return;
    const qi=this.dataset.q;
    document.querySelectorAll('.exam-opt[data-q="'+qi+'"]').forEach(x=>x.classList.remove('sel'));
    this.classList.add('sel'); answers[qi]=+this.dataset.o; prog();}));
  document.getElementById('result').classList.remove('show'); document.getElementById('result').innerHTML='';
  document.getElementById('submit').style.display=''; document.getElementById('retake').style.display='none'; prog(); window.scrollTo(0,0);
}
function prog(){document.getElementById('prog').textContent=Object.keys(answers).length+' / '+BANK.length+' answered';}
function band(p){return p>=80?'Strong — exam-ready':p>=65?'Competent':p>=50?'Developing':'Needs work';}
function grade(){
  const byDom={}; let correct=0;
  BANK.forEach((q,qi)=>{const d=q.domain; byDom[d]=byDom[d]||{c:0,t:0}; byDom[d].t++;
    const a=answers[qi]; const opts=document.querySelectorAll('.exam-opt[data-q="'+qi+'"]');
    opts.forEach((o,oi)=>{if(oi===q.correct)o.classList.add('correct'); if(oi===a&&a!==q.correct)o.classList.add('wrong');});
    document.querySelector('#q'+qi+' .exam-fb').classList.add('show');
    if(a===q.correct){correct++; byDom[d].c++;}});
  const pct=Math.round(100*correct/BANK.length);
  const rows=Object.keys(byDom).sort().map(d=>{const o=byDom[d],p=Math.round(100*o.c/o.t);
    return '<div class="dom-row"><span>'+d+'</span><span class="dom-bar"><i style="width:'+p+'%"></i></span><span style="text-align:right;color:var(--dim)">'+o.c+'/'+o.t+'</span></div>';}).join('');
  const r=document.getElementById('result');
  r.innerHTML='<div class="band">'+band(pct)+'</div><h2>'+pct+'%</h2>'+
    '<p style="color:var(--dim);margin:.2em 0 16px">'+correct+' of '+BANK.length+' correct &middot; original questions calibrated to CFA / GMAT / CLEP / MFT-MBA difficulty</p>'+
    '<div style="border-top:1px solid var(--line);padding-top:14px">'+rows+'</div>'+
    '<p class="note" style="margin-top:18px">Weak domains are your study targets. This is a calibrated <b>proxy</b> — for a true external score, sit an official practice exam (links at top). Unanswered count as wrong.</p>';
  r.classList.add('show');
  document.getElementById('submit').style.display='none'; document.getElementById('retake').style.display='';
  window.scrollTo({top:0,behavior:'smooth'});
}
document.getElementById('submit').addEventListener('click',grade);
document.getElementById('retake').addEventListener('click',render);
document.getElementById('introNote').textContent=BANK.length+' original, application-level questions across '+new Set(BANK.map(q=>q.domain)).size+
  ' MBA domains, written to real-exam difficulty (not recall). Answer what you can, then Submit & Score.';
render();
</script></body></html>"""

out = PAGE.replace("__BANK__", json.dumps(bank, ensure_ascii=False)).replace("__LINKS__", LINKS)
os.makedirs(DIST, exist_ok=True)
open(os.path.join(DIST, "benchmark-exam.html"), "w", encoding="utf-8").write(out)
print(f"\nwrote {os.path.join(DIST, 'benchmark-exam.html')} ({len(bank)} questions)")
