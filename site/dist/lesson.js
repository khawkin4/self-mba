
(function(){
  var bar=document.getElementById('progress');
  if(bar){addEventListener('scroll',function(){
    var h=document.documentElement,sc=h.scrollTop,mx=h.scrollHeight-h.clientHeight;
    bar.style.width=(mx>0?100*sc/mx:0)+'%';},{passive:true});}
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
    done.addEventListener('click',function(){done.classList.toggle('checked');
      localStorage.setItem(key,done.classList.contains('checked')?'1':'0');});}
})();
