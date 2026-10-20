
(function(){
  // --- Completion state ---
  document.querySelectorAll('.mcard[data-mod]').forEach(function(c){
    if(localStorage.getItem('mba-done-'+c.dataset.mod+'.html')==='1')c.classList.add('completed');
  });

  // --- XP + Level system ---
  var XP={core:100,exec:120,canon:80,gaps:90};
  var LVL=[[0,'Analyst'],[300,'Associate'],[700,'Senior Associate'],[1200,'VP'],
    [2000,'Director'],[3000,'SVP'],[4200,'Managing Director'],[5000,'C-Suite']];
  function calcXP(){
    var xp=0;
    document.querySelectorAll('.mcard.completed').forEach(function(c){
      xp+=(XP[c.dataset.track]||80);});
    return xp;}
  function getLevel(xp){
    var lv=LVL[0];
    for(var i=0;i<LVL.length;i++){if(xp>=LVL[i][0])lv=LVL[i];}
    return lv;}
  var xp=calcXP(),lv=getLevel(xp);
  var xpEl=document.getElementById('xp-count');
  var lvlEl=document.getElementById('level-badge');
  if(xpEl){
    var cur=0,target=xp,dur=800,st=null;
    function stepXP(ts){
      if(!st)st=ts;var p=Math.min((ts-st)/dur,1);
      var e=1-Math.pow(1-p,3);
      xpEl.textContent=Math.floor(target*e);
      if(p<1)requestAnimationFrame(stepXP);}
    requestAnimationFrame(stepXP);}
  if(lvlEl)lvlEl.textContent=lv[1];

  // --- Streak ---
  try{
    var today=new Date().toISOString().slice(0,10);
    var sk=JSON.parse(localStorage.getItem('mba-streak')||'{"d":0,"last":""}');
    var sEl=document.getElementById('streak-num');
    if(sEl){
      var yesterday=new Date(Date.now()-864e5).toISOString().slice(0,10);
      if(sk.last===today)sEl.textContent=sk.d;
      else if(sk.last===yesterday)sEl.textContent=sk.d;
      else sEl.textContent=0;
    }
  }catch(e){}

  // --- Animated stat counters ---
  function animNum(el){
    var raw=el.dataset.target;if(!raw)return;
    var t=parseInt(raw.replace(/,/g,''),10);
    if(isNaN(t)){el.textContent=raw;return;}
    var dur=1400,st=null;
    function step(ts){
      if(!st)st=ts;var p=Math.min((ts-st)/dur,1);
      el.textContent=Math.floor(t*(1-Math.pow(1-p,3))).toLocaleString();
      if(p<1)requestAnimationFrame(step);
      else{el.textContent=t.toLocaleString();el.classList.add('counted');}
    }
    requestAnimationFrame(step);
  }
  var sObs=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){animNum(e.target);sObs.unobserve(e.target);}
    });},{threshold:0.3});
  document.querySelectorAll('.stat-num[data-target]').forEach(function(el){sObs.observe(el);});

  // --- Animate bar fills (hero coverage + path stage bars) ---
  var bObs=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){
        e.target.style.width=e.target.dataset.width+'%';
        bObs.unobserve(e.target);}
    });},{threshold:0.3});
  document.querySelectorAll('.stat-bar-fill[data-width],.stage-bar i[data-width]').forEach(function(el){bObs.observe(el);});

  // --- Hero CTA: first visit → start the On-ramp; returning → continue the last item ---
  try{
    var last=JSON.parse(localStorage.getItem('mba-last')||'null');
    var cta=document.getElementById('hero-cta');
    if(last&&last.h&&cta){
      cta.href=last.h;cta.classList.add('is-continue');
      document.getElementById('cta-label').textContent='Continue: '+last.t;
      document.getElementById('cta-sub').textContent=(last.c||'Where you left off');
    }
  }catch(e){}

  // --- Path stages: the reader's own progress (modules from mba-done-*, docs from mba-read-*) ---
  function isRead(h){try{return localStorage.getItem('mba-read-'+h)==='1';}catch(e){return false;}}
  document.querySelectorAll('.stage').forEach(function(st){
    var done=0,total=0;
    if(st.dataset.track){var cs=document.querySelectorAll('.mcard[data-track="'+st.dataset.track+'"]');total=cs.length;
      cs.forEach(function(c){if(c.classList.contains('completed'))done++;});}
    else if(st.dataset.docs){try{var docs=JSON.parse(st.dataset.docs);total=docs.length;done=docs.filter(isRead).length;}catch(e){}}
    var pct=total?Math.round(100*done/total):0;
    var lbl=st.querySelector('.stage-prog'),bar=st.querySelector('.stage-bar i');
    if(lbl)lbl.textContent=done===0?'Not started':(done===total?'Complete':done+'/'+total+' done');
    if(bar)bar.dataset.width=pct;
    st.classList.toggle('started',done>0);st.classList.toggle('complete',total>0&&done===total);
  });

  // --- Long sections collapsed behind "Show all" ---
  document.querySelectorAll('.show-all').forEach(function(btn){
    var grid=document.querySelector('#'+btn.dataset.for+' .grid');
    btn.addEventListener('click',function(){grid.classList.remove('trunc');btn.remove();});
  });
  function untrunc(){document.querySelectorAll('.grid.trunc').forEach(function(g){g.classList.remove('trunc');});document.querySelectorAll('.show-all').forEach(function(b){b.remove();});}
  var qEl=document.getElementById('q');if(qEl)qEl.addEventListener('input',untrunc,{once:true});
  document.querySelectorAll('.chip:not([data-filter="all"])').forEach(function(c){c.addEventListener('click',untrunc,{once:true});});

  // --- Card entrance stagger (per-section, Material deceleration) ---
  var sections=document.querySelectorAll('.track-section');
  sections.forEach(function(sec){
    var idx=0;
    var obs=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          e.target.style.animationDelay=(idx%12)*0.04+'s';
          e.target.classList.add('card-enter');
          idx++;obs.unobserve(e.target);}
      });},{threshold:0.05,rootMargin:'40px'});
    sec.querySelectorAll('.mcard').forEach(function(c){obs.observe(c);});
  });

  // --- Container transform: card click animation ---
  document.querySelectorAll('.mcard[href]').forEach(function(c){
    c.addEventListener('click',function(e){
      e.preventDefault();
      try{sessionStorage.setItem('mba-scroll',window.scrollY);
        var active=document.querySelector('.tt.active');
        if(active)sessionStorage.setItem('mba-tab',active.getAttribute('data-track'));
      }catch(x){}
      c.classList.add('navigating');
      var href=c.getAttribute('href');
      setTimeout(function(){window.location.href=href;},180);
    });
  });

  // --- Scroll + tab restoration on return ---
  try{
    var savedScroll=sessionStorage.getItem('mba-scroll');
    if(savedScroll!==null){
      window.scrollTo(0,parseInt(savedScroll,10));
      sessionStorage.removeItem('mba-scroll');
      document.querySelectorAll('.mcard').forEach(function(c){c.style.animation='none';c.style.opacity='1';});
    }
    var savedTab=sessionStorage.getItem('mba-tab');
    if(savedTab){sessionStorage.removeItem('mba-tab');}
  }catch(x){}

  // --- Sticky tabs scroll spy ---
  var tabs=document.querySelectorAll('.tt');
  var secs=document.querySelectorAll('.track-section');
  if(tabs.length&&secs.length){
    var spy=function(){
      var pos=window.scrollY+140,act=0;
      secs.forEach(function(s,i){if(s.offsetTop<=pos)act=i;});
      tabs.forEach(function(t,i){t.classList.toggle('active',i===act);});};
    window.addEventListener('scroll',spy,{passive:true});
    tabs.forEach(function(t){
      t.addEventListener('click',function(e){
        e.preventDefault();
        var sec=document.querySelector(t.getAttribute('href'));
        if(sec){
          window.scrollTo({top:sec.offsetTop-60,behavior:'smooth'});
          sec.classList.remove('landing');
          void sec.offsetWidth;
          sec.classList.add('landing');
        }
      });
    });
  }

  // --- Filter chips ---
  document.querySelectorAll('.chip').forEach(function(chip){
    chip.addEventListener('click',function(){
      document.querySelectorAll('.chip').forEach(function(c){c.classList.remove('active');});
      chip.classList.add('active');
      var f=chip.dataset.filter;
      document.querySelectorAll('.mcard').forEach(function(c){
        var show=true;
        if(f==='lesson')show=c.classList.contains('ready');
        else if(f==='completed')show=c.classList.contains('completed');
        else if(f==='not-started')show=!c.classList.contains('completed');
        c.style.display=show?'':'none';
      });
      document.getElementById('q').value='';
    });
  });
  // --- Track section collapse/expand ---
  document.querySelectorAll('.th-toggle').forEach(function(btn){
    btn.addEventListener('click',function(e){
      e.preventDefault();
      var sec=btn.closest('.track-section');
      sec.classList.toggle('collapsed');
      var track=btn.closest('.track-head').dataset.collapse;
      if(track){
        try{
          var st=JSON.parse(localStorage.getItem('mba-collapsed')||'{}');
          st[track]=sec.classList.contains('collapsed');
          localStorage.setItem('mba-collapsed',JSON.stringify(st));
        }catch(e){}
      }
    });
  });
  try{
    var cst=JSON.parse(localStorage.getItem('mba-collapsed')||'{}');
    Object.keys(cst).forEach(function(track){
      if(cst[track]){
        var head=document.querySelector('.track-head[data-collapse="'+track+'"]');
        if(head)head.closest('.track-section').classList.add('collapsed');
      }
    });
  }catch(e){}
})();
