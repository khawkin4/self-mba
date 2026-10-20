/* Shared chrome: theme toggle, nav state, ⌘K palette, reading progress, TOC scroll-spy, "continue" memory. */
(function(){
  var root=document.documentElement;
  // ---- theme (mba-theme: 'light' | 'dark' | unset = follow OS) ----
  try{var t=localStorage.getItem('mba-theme');if(t)root.setAttribute('data-theme',t);}catch(e){}
  var tbtn=document.getElementById('theme-toggle');
  if(tbtn){tbtn.addEventListener('click',function(){
    var dark=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
    var next=dark?'light':'dark';root.setAttribute('data-theme',next);
    try{localStorage.setItem('mba-theme',next);}catch(e){}
    document.dispatchEvent(new CustomEvent('mba-theme',{detail:next}));
  });}

  // ---- nav active state ----
  var page=location.pathname.split('/').pop()||'index.html';
  var navKey='path';
  if(/^(lib|doc)-/.test(page))navKey='library';
  else if(/exam/.test(page))navKey='exam';
  else if(page==='index.html'){navKey=location.hash==='#t-library'?'library':location.hash==='#t-explore'?'explore':'path';}
  function paintNav(k){document.querySelectorAll('.sn-links a[data-nav]').forEach(function(a){var on=a.dataset.nav===k;a.classList.toggle('active',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});}
  paintNav(navKey);
  if(page==='index.html'){addEventListener('hashchange',function(){
    var k=location.hash==='#t-library'?'library':location.hash==='#t-explore'?'explore':'path';
    paintNav(k);});}

  // ---- reading progress (docs + module pages) ----
  var bar=document.getElementById('progress');
  if(bar){var h=document.documentElement;
    var tick=function(){var mx=h.scrollHeight-h.clientHeight;bar.style.width=(mx>0?100*h.scrollTop/mx:0)+'%';};
    addEventListener('scroll',tick,{passive:true});tick();}

  // ---- remember last-opened lesson or document for the home "Continue" card ----
  var title=document.querySelector('.mod-header h1,.doc-title');
  if(title&&page!=='index.html'){try{
    var crumb=document.querySelector('.breadcrumb a:nth-of-type(2),.crumbs a:nth-of-type(2)');
    localStorage.setItem('mba-last',JSON.stringify({h:page,t:title.textContent.trim(),c:crumb?crumb.textContent.trim():''}));
  }catch(e){}}

  // ---- read tracking (mba-read-<href>) ----
  function isRead(h){try{return localStorage.getItem('mba-read-'+h)==='1';}catch(e){return false;}}
  function setRead(h,v){try{if(v)localStorage.setItem('mba-read-'+h,'1');else localStorage.removeItem('mba-read-'+h);}catch(e){}}
  window.mbaIsRead=isRead;
  var mr=document.querySelector('.mark-read');
  if(mr){
    var href=mr.dataset.href;
    function paint(){mr.classList.toggle('checked',isRead(href));mr.setAttribute('aria-pressed',isRead(href)?'true':'false');}
    paint();
    mr.addEventListener('click',function(){setRead(href,!isRead(href));paint();
      var t=document.getElementById('toast');if(t){t.textContent=isRead(href)?'Marked as read':'Marked unread';t.classList.add('show');setTimeout(function(){t.classList.remove('show');},1800);}});
    // auto-mark once the reader has scrolled ≥90% of the document
    var autoDone=isRead(href);
    var auto=function(){if(autoDone)return;var h=document.documentElement,mx=h.scrollHeight-h.clientHeight;
      if(mx>0&&h.scrollTop/mx>=0.9){autoDone=true;setRead(href,true);paint();}};
    addEventListener('scroll',auto,{passive:true});
  }
  // collection index rows: tick the ones already read + count
  var libRows=document.querySelectorAll('.lib-row[data-href]');
  if(libRows.length){var n=0;libRows.forEach(function(r){if(isRead(r.dataset.href)){r.classList.add('read');n++;}});
    var rc=document.querySelector('.lib-readcount');if(rc){rc.textContent=n?n+' read':'';}}
  // home library cards: "n/total read"
  document.querySelectorAll('.lcard-read[data-docs]').forEach(function(el){try{
    var docs=JSON.parse(el.dataset.docs),n=docs.filter(isRead).length;
    el.textContent=n?n+' read · ':'';}catch(e){}});

  // ---- document TOC: open on desktop, scroll-spy ----
  var toc=document.querySelector('.doc-toc');
  if(toc){
    var det=toc.querySelector('details');
    var wide=matchMedia('(min-width:1000px)');
    function sync(){if(det){if(wide.matches)det.open=true;}}
    sync();wide.addEventListener?wide.addEventListener('change',sync):wide.addListener(sync);
    var links=[].slice.call(toc.querySelectorAll('a[href^="#"]'));
    var heads=links.map(function(a){return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));});
    var spy=function(){
      var y=scrollY+120,cur=-1;
      heads.forEach(function(el,i){if(el&&el.offsetTop<=y)cur=i;});
      links.forEach(function(a,i){a.classList.toggle('cur',i===cur);});
    };
    addEventListener('scroll',spy,{passive:true});spy();
    // on narrow screens, collapse after choosing a section
    links.forEach(function(a){a.addEventListener('click',function(){if(det&&!wide.matches)det.open=false;});});
  }

  // ---- ⌘K command palette over search-index.json ----
  var ICON='<svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14"/></svg>';
  var box=document.createElement('div');box.className='cmdk';box.id='cmdk';box.setAttribute('role','dialog');box.setAttribute('aria-label','Search');
  box.innerHTML='<div class="cmdk-box"><div class="cmdk-in">'+ICON+'<input type="text" placeholder="Search modules, notes, glossary…" autocomplete="off" spellcheck="false"></div><div class="cmdk-list"></div><div class="cmdk-foot"><span><kbd>↑↓</kbd>navigate</span><span><kbd>↵</kbd>open</span><span><kbd>esc</kbd>close</span></div></div>';
  document.body.appendChild(box);
  var input=box.querySelector('input'),list=box.querySelector('.cmdk-list');
  var INDEX=null,sel=0,rows=[];
  var ORDER={'Core':0,'Executive':1,'Canon':2,'Foundations':3,'On-ramp':4,'Acumen Gym':5,'Field Notes':6,'Canon Notes':7,'Quant Lab':8,'Reference':9,'Exams':10};
  function load(cb){
    if(INDEX)return cb(INDEX);
    fetch('search-index.json').then(function(r){return r.json();}).then(function(j){INDEX=j;cb(j);}).catch(function(){
      // offline / file:// fallback: index whatever this page links to
      INDEX=[].slice.call(document.querySelectorAll('.mcard[href],.lib-row[href],.latest-list a')).map(function(a){
        var t=a.querySelector('h3,.lib-title,.lt-title');return {t:t?t.textContent.trim():a.textContent.trim(),h:a.getAttribute('href'),c:'',k:''};});
      cb(INDEX);});
  }
  function score(item,q){
    var t=item.t.toLowerCase(),k=(item.k||'').toLowerCase(),p=(item.p||'').toLowerCase();
    if(!q)return item.p?0:1;
    var bonus=item.p?0:5;
    if(k&&k===q)return 100;
    if(t.indexOf(q)===0)return 50+bonus;
    var words=q.split(/\s+/),s=0;
    for(var i=0;i<words.length;i++){if(!words[i])continue;
      if(t.indexOf(words[i])<0&&p.indexOf(words[i])<0&&(item.c||'').toLowerCase().indexOf(words[i])<0)return 0;
      s+=t.indexOf(words[i])>=0?10:4;}
    return s+bonus;
  }
  function render(q){
    q=(q||'').trim().toLowerCase();
    var hits=INDEX.map(function(it){return [score(it,q),it];}).filter(function(x){return x[0]>0;});
    hits.sort(function(a,b){return b[0]-a[0]||((a[1].c in ORDER)?ORDER[a[1].c]:50)-((b[1].c in ORDER)?ORDER[b[1].c]:50)||a[1].t.localeCompare(b[1].t);});
    hits=hits.slice(0,q?40:24);
    rows=[];list.innerHTML='';
    if(!hits.length){list.innerHTML='<div class="cmdk-empty">Nothing matches “'+q.replace(/</g,'&lt;')+'”.</div>';return;}
    var lastGroup=null;
    hits.forEach(function(x){var it=x[1];
      if(it.c!==lastGroup){var g=document.createElement('div');g.className='cmdk-group';g.textContent=it.c||'Pages';list.appendChild(g);lastGroup=it.c;}
      var a=document.createElement('a');a.className='cmdk-item';a.href=it.h;
      a.innerHTML='<span class="cmdk-code">'+(it.k||'')+'</span><span class="cmdk-t"></span><span class="cmdk-c"></span>';
      a.querySelector('.cmdk-t').textContent=it.t;a.querySelector('.cmdk-c').textContent=it.c||'';
      if(it.p){a.classList.add('cmdk-sub');var pe=document.createElement('span');pe.className='cmdk-p';pe.textContent=it.p;a.querySelector('.cmdk-t').appendChild(pe);}
      a.addEventListener('mousemove',function(){setSel(rows.indexOf(a));});
      a.addEventListener('click',function(e){e.preventDefault();go(a.href);});
      list.appendChild(a);rows.push(a);});
    setSel(0);
  }
  function go(h){close();var u=new URL(h,location.href);
    if(u.pathname===location.pathname&&u.hash){var el=document.getElementById(decodeURIComponent(u.hash.slice(1)));if(el){history.pushState(null,'',u.hash);el.scrollIntoView();return;}}
    location.href=h;}
  function setSel(i){sel=Math.max(0,Math.min(i,rows.length-1));rows.forEach(function(r,j){r.classList.toggle('sel',j===sel);});
    if(rows[sel])rows[sel].scrollIntoView({block:'nearest'});}
  function open(){box.classList.add('open');input.value='';load(function(){render('');});setTimeout(function(){input.focus();},10);}
  function close(){box.classList.remove('open');}
  var openBtn=document.getElementById('open-search');if(openBtn)openBtn.addEventListener('click',open);
  box.addEventListener('click',function(e){if(e.target===box)close();});
  input.addEventListener('input',function(){render(input.value);});
  document.addEventListener('keydown',function(e){
    if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();box.classList.contains('open')?close():open();return;}
    if(e.key==='/'&&!box.classList.contains('open')&&!/INPUT|TEXTAREA/.test(e.target.tagName)&&!e.target.isContentEditable){e.preventDefault();open();return;}
    if(!box.classList.contains('open'))return;
    if(e.key==='Escape'){close();}
    else if(e.key==='ArrowDown'){e.preventDefault();setSel(sel+1);}
    else if(e.key==='ArrowUp'){e.preventDefault();setSel(sel-1);}
    else if(e.key==='Enter'){if(rows[sel]){e.preventDefault();go(rows[sel].href);}}
  });
})();
