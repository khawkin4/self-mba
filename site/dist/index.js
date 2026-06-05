
(function(){document.querySelectorAll('.mcard[data-mod]').forEach(function(c){
  if(localStorage.getItem('mba-done-'+c.dataset.mod+'.html')==='1')c.classList.add('completed');});})();
