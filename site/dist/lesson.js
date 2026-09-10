
(function(){
  var bar=document.getElementById('progress');
  if(bar){addEventListener('scroll',function(){
    var h=document.documentElement,sc=h.scrollTop,mx=h.scrollHeight-h.clientHeight;
    bar.style.width=(mx>0?100*sc/mx:0)+'%';},{passive:true});}
  // keyboard nav: ← → for prev/next
  var prevLink=document.querySelector('.pn:not(.next)');
  var nextLink=document.querySelector('.pn.next');
  document.addEventListener('keydown',function(e){
    if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'||e.target.isContentEditable)return;
    if(e.key==='ArrowLeft'&&prevLink){prevLink.click();}
    if(e.key==='ArrowRight'&&nextLink){nextLink.click();}
  });
  // flip cards
  document.querySelectorAll('.fc').forEach(function(c){
    c.addEventListener('click',function(){c.classList.toggle('flipped');});});
  // click-to-reveal
  document.querySelectorAll('.reveal .reveal-q').forEach(function(q){
    q.addEventListener('click',function(){q.parentNode.classList.toggle('open');});});
  // MCQ quiz w/ instant feedback
  document.querySelectorAll('.quizq').forEach(function(q){
    var correct=+q.dataset.correct, opts=q.querySelectorAll('.opt');
    opts.forEach(function(b,i){b.addEventListener('click',function(){
      if(q.classList.contains('done'))return; q.classList.add('done');
      b.classList.add(i===correct?'right':'wrong');
      if(i!==correct)opts[correct].classList.add('right');
      var fb=q.querySelector('.fb'); if(fb)fb.classList.add('show');});});});
  // SVG / element hotspots -> floating tooltip
  var tip=document.createElement('div'); tip.className='tip'; document.body.appendChild(tip);
  function place(e){var t=e.touches?e.touches[0]:e; tip.style.left=t.clientX+'px';
    tip.style.top=(t.clientY+window.scrollY-12)+'px';}
  document.querySelectorAll('[data-tip]').forEach(function(el){
    el.classList.add('hot');
    function show(e){tip.textContent=el.dataset.tip; tip.classList.add('show'); place(e);}
    el.addEventListener('mouseenter',show); el.addEventListener('mousemove',place);
    el.addEventListener('mouseleave',function(){tip.classList.remove('show');});
    el.addEventListener('click',function(e){show(e);
      document.querySelectorAll('[data-tip].active').forEach(function(o){if(o!==el)o.classList.remove('active');});
      el.classList.toggle('active');});});
  document.addEventListener('click',function(e){
    if(!e.target.closest('[data-tip]'))tip.classList.remove('show');});
  // module completion (persisted; surfaced on index)
  var done=document.getElementById('mark-done');
  if(done){var key='mba-done-'+(done.dataset.mod||location.pathname.split('/').pop());
    if(localStorage.getItem(key)==='1')done.classList.add('checked');
    done.addEventListener('click',function(){
      done.classList.toggle('checked');
      localStorage.setItem(key,done.classList.contains('checked')?'1':'0');
      if(done.classList.contains('checked')){
        done.classList.add('just-checked');
        setTimeout(function(){done.classList.remove('just-checked');},600);
        // update streak
        try{
          var today=new Date().toISOString().slice(0,10);
          var sk=JSON.parse(localStorage.getItem('mba-streak')||'{"d":0,"last":""}');
          var yesterday=new Date(Date.now()-864e5).toISOString().slice(0,10);
          if(sk.last!==today){
            sk.d=(sk.last===yesterday)?sk.d+1:1;
            sk.last=today;
            localStorage.setItem('mba-streak',JSON.stringify(sk));}
        }catch(e){}
        // toast
        var toast=document.getElementById('toast');
        if(toast){
          var track=(done.dataset.mod||'').split('-')[0];
          var xpVal={core:100,exec:120,canon:80,gaps:90}[track]||80;
          toast.innerHTML='Module complete! <span class="xp-plus">+'+xpVal+' XP</span>';
          toast.classList.add('show');
          setTimeout(function(){toast.classList.remove('show');},2800);
          // confetti burst
          for(var i=0;i<24;i++){
            var c=document.createElement('div');c.className='confetti';
            c.style.left=Math.random()*100+'vw';
            c.style.background=['#9a7b2e','#2d7a4a','#b86e1a','#c4372a','#4a90d9'][i%5];
            c.style.animationDelay=Math.random()*0.8+'s';
            c.style.animationDuration=(2+Math.random()*1.5)+'s';
            c.style.width=(6+Math.random()*6)+'px';
            c.style.height=(6+Math.random()*6)+'px';
            document.body.appendChild(c);
            setTimeout(function(el){el.remove();},(4000),c);}
        }
      }
    });}
  // ====== Chart.js auto-init ======
  if(typeof Chart!=='undefined'){
    var COLORS={brass:'#9a7b2e',core:'#84ad8a',exec:'#b86e1a',dim:'#7a7568',ink:'#2c2a25',
      line:'#d9d4cb',surface:'#f2ede6',red:'#cf6a5a',blue:'#4a90d9',teal:'#2d8a7a',
      purple:'#7a5fa0',orange:'#d4842a'};
    Chart.defaults.font.family="'Lexend',sans-serif";
    Chart.defaults.color=COLORS.dim;
    Chart.defaults.plugins.legend.labels.usePointStyle=true;
    Chart.defaults.plugins.legend.labels.boxWidth=8;
    Chart.defaults.elements.bar.borderRadius=4;
    Chart.defaults.elements.bar.borderSkipped=false;
    Chart.defaults.scale.grid={color:'rgba(0,0,0,.06)'};
    Chart.defaults.scale.border={display:false};
    function patchCallbacks(obj){
      if(!obj||typeof obj!=='object')return;
      Object.keys(obj).forEach(function(k){
        if(k==='callback'&&obj[k]==='PERCENT'){obj[k]=function(v){return v+'%'};}
        else if(k==='callback'&&obj[k]==='DOLLAR'){obj[k]=function(v){return '$'+v+'B'};}
        else if(k==='callback'&&obj[k]==='DOLLAR_PLAIN'){obj[k]=function(v){return '$'+v};}
        else if(k==='callback'&&obj[k]==='PLAIN'){obj[k]=function(v){return v.toLocaleString()};}
        else patchCallbacks(obj[k]);
      });
    }
    document.querySelectorAll('canvas[data-chart]').forEach(function(cvs){
      try{
        var cfg=JSON.parse(cvs.dataset.chart);
        patchCallbacks(cfg);
        if(!cfg.options)cfg.options={};
        if(cfg.options.animation===undefined){
          cfg.options.animation={duration:800,easing:'easeOutQuart'};
        }
        if(!cfg.options.plugins)cfg.options.plugins={};
        if(!cfg.options.plugins.tooltip)cfg.options.plugins.tooltip={};
        cfg.options.plugins.tooltip.backgroundColor='rgba(44,42,37,.92)';
        cfg.options.plugins.tooltip.cornerRadius=6;
        cfg.options.plugins.tooltip.padding=10;
        new Chart(cvs,cfg);
      }catch(e){console.warn('Chart init error:',e);}
    });
  }
})();
