
(function(){
  var COLORS={core:[45,122,74],exec:[184,110,26],canon:[154,123,46],gaps:[122,97,33]};
  var BG=[250,247,242];

  // ====== WORD CLOUD — canvas spiral packing, 0° + 90° ======
  var wcCvs=document.getElementById('wc-canvas');
  if(wcCvs && typeof WC_DATA!=='undefined' && WC_DATA.length){
    var panel=wcCvs.parentElement;
    var pw=panel.clientWidth-56;
    var W=Math.max(pw,260),H=Math.round(W*1.1);
    var dpr=window.devicePixelRatio||1;
    wcCvs.width=W*dpr;wcCvs.height=H*dpr;
    wcCvs.style.width=W+'px';wcCvs.style.height=H+'px';
    var ctx=wcCvs.getContext('2d');
    ctx.scale(dpr,dpr);
    var placed=[];
    var sorted=WC_DATA.slice().sort(function(a,b){return b.s-a.s;});
    var ck=['core','exec','canon','gaps','core'];
    function colorFor(i){var c=COLORS[ck[i%5]]||COLORS.core;return 'rgb('+c[0]+','+c[1]+','+c[2]+')';}
    function measure(word,size,rot){
      ctx.font=(size>18?'600 ':'500 ')+size+'px Lexend,system-ui,sans-serif';
      var m=ctx.measureText(word);
      var tw=m.width+4,th=size*1.1+2;
      return rot?{w:th,h:tw,tw:tw,th:th}:{w:tw,h:th,tw:tw,th:th};
    }
    function overlaps(x,y,w,h){
      for(var i=0;i<placed.length;i++){
        var p=placed[i];
        if(x<p.x+p.w&&x+w>p.x&&y<p.y+p.h&&y+h>p.y)return true;
      }
      return false;
    }
    sorted.forEach(function(d,i){
      var size=Math.round(13+d.s*22);
      var rot=i>2&&Math.random()<0.3;
      var m=measure(d.w,size,rot);
      var cx=W/2,cy=H/2;
      var step=3,angle=0,r=0,found=false;
      for(var tries=0;tries<800;tries++){
        var px=cx+Math.cos(angle)*r-m.w/2;
        var py=cy+Math.sin(angle)*r-m.h/2;
        if(px>=0&&py>=0&&px+m.w<=W&&py+m.h<=H&&!overlaps(px,py,m.w,m.h)){
          placed.push({x:px,y:py,w:m.w,h:m.h,word:d.w,size:size,rot:rot,color:colorFor(i),s:d.s});
          found=true;break;
        }
        angle+=0.6;r+=step*0.12;
      }
    });
    function drawCloud(){
      ctx.clearRect(0,0,W,H);
      placed.forEach(function(p){
        ctx.save();
        ctx.font=((p.size>18?'600 ':'500 ')+p.size+'px Lexend,system-ui,sans-serif');
        ctx.fillStyle=p.color;
        ctx.globalAlpha=0.5+p.s*0.5;
        if(p.rot){
          ctx.translate(p.x+p.w/2,p.y+p.h/2);
          ctx.rotate(-Math.PI/2);
          ctx.textAlign='center';ctx.textBaseline='middle';
          ctx.fillText(p.word,0,0);
        }else{
          ctx.textAlign='left';ctx.textBaseline='top';
          ctx.fillText(p.word,p.x+2,p.y+1);
        }
        ctx.restore();
      });
    }
    var wcObs=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){drawCloud();wcObs.unobserve(e.target);}});
    },{threshold:0.1});
    wcObs.observe(wcCvs);
  }

  // ====== 3D KNOWLEDGE GRAPH (Three.js) ======
  var mount=document.getElementById('kg-mount');
  var tip=document.getElementById('kg-tip');
  if(!mount||typeof THREE==='undefined'||typeof KG_DATA==='undefined'||!KG_DATA.nodes.length)return;

  var rect=mount.getBoundingClientRect();
  var W3=Math.round(rect.width)||500,H3=Math.round(W3*10/16);
  var scene=new THREE.Scene();
  scene.background=new THREE.Color(BG[0]/255,BG[1]/255,BG[2]/255);
  var camera=new THREE.PerspectiveCamera(50,W3/H3,1,2000);
  camera.position.set(0,0,220);
  var renderer=new THREE.WebGLRenderer({antialias:true});
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(W3,H3);
  mount.appendChild(renderer.domElement);

  var ambient=new THREE.AmbientLight(0xffffff,0.6);
  scene.add(ambient);
  var dir=new THREE.DirectionalLight(0xffffff,0.8);
  dir.position.set(100,200,150);scene.add(dir);

  var tcHex={core:0x2d7a4a,exec:0xb86e1a,canon:0x9a7b2e,gaps:0x7a6121};
  var maxW=Math.max.apply(null,KG_DATA.edges.map(function(e){return e.w;}))||1;
  var nodeObjs=[],nodeMap={},edgeLines=[];

  KG_DATA.nodes.forEach(function(n,i){
    var phi=Math.acos(-1+2*i/KG_DATA.nodes.length);
    var theta=Math.sqrt(KG_DATA.nodes.length*Math.PI)*phi;
    var R=60+Math.random()*20;
    var geo=new THREE.SphereGeometry(2.5,16,12);
    var mat=new THREE.MeshPhongMaterial({color:tcHex[n.track]||0x8a837a,shininess:80});
    var mesh=new THREE.Mesh(geo,mat);
    mesh.position.set(R*Math.sin(phi)*Math.cos(theta),R*Math.sin(phi)*Math.sin(theta),R*Math.cos(phi));
    mesh.userData={id:n.id,label:n.label,track:n.track,vx:0,vy:0,vz:0};
    scene.add(mesh);
    nodeObjs.push(mesh);
    nodeMap[n.id]=mesh;
  });

  KG_DATA.edges.forEach(function(e){
    var s=nodeMap[e.s],t=nodeMap[e.t];
    if(!s||!t)return;
    var geo=new THREE.BufferGeometry().setFromPoints([s.position,t.position]);
    var op=0.06+0.14*(e.w/maxW);
    var mat=new THREE.LineBasicMaterial({color:0x9a7b2e,transparent:true,opacity:op});
    var line=new THREE.Line(geo,mat);
    line.userData={s:s,t:t,w:e.w,baseOp:op};
    scene.add(line);
    edgeLines.push(line);
  });

  // 3D force simulation
  function tick3D(){
    var damp=0.9,rep=800,k=0.006;
    for(var i=0;i<nodeObjs.length;i++){
      var n=nodeObjs[i],p=n.position,d=n.userData;
      d.vx-=p.x*0.0008;d.vy-=p.y*0.0008;d.vz-=p.z*0.0008;
      for(var j=i+1;j<nodeObjs.length;j++){
        var m=nodeObjs[j],q=m.position,md=m.userData;
        var dx=p.x-q.x,dy=p.y-q.y,dz=p.z-q.z;
        var d2=dx*dx+dy*dy+dz*dz+1;
        var f=rep/d2,dist=Math.sqrt(d2);
        var fx=dx/dist*f,fy=dy/dist*f,fz=dz/dist*f;
        d.vx+=fx;d.vy+=fy;d.vz+=fz;
        md.vx-=fx;md.vy-=fy;md.vz-=fz;
      }
    }
    for(var i=0;i<edgeLines.length;i++){
      var e=edgeLines[i],sp=e.userData.s.position,tp=e.userData.t.position;
      var dx=tp.x-sp.x,dy=tp.y-sp.y,dz=tp.z-sp.z;
      var dist=Math.sqrt(dx*dx+dy*dy+dz*dz)||1;
      var ideal=25+15*(1-e.userData.w/maxW);
      var f=(dist-ideal)*k;
      var fx=dx/dist*f,fy=dy/dist*f,fz=dz/dist*f;
      e.userData.s.userData.vx+=fx;e.userData.s.userData.vy+=fy;e.userData.s.userData.vz+=fz;
      e.userData.t.userData.vx-=fx;e.userData.t.userData.vy-=fy;e.userData.t.userData.vz-=fz;
    }
    for(var i=0;i<nodeObjs.length;i++){
      var n=nodeObjs[i],d=n.userData;
      d.vx*=damp;d.vy*=damp;d.vz*=damp;
      n.position.x+=d.vx;n.position.y+=d.vy;n.position.z+=d.vz;
    }
    edgeLines.forEach(function(line){
      var pts=[line.userData.s.position,line.userData.t.position];
      line.geometry.setFromPoints(pts);
    });
  }

  // Manual orbit controls
  var isDrag=false,prevX=0,prevY=0;
  var spherical={theta:0,phi:Math.PI/2,r:220};
  function updateCam(){
    camera.position.set(
      spherical.r*Math.sin(spherical.phi)*Math.cos(spherical.theta),
      spherical.r*Math.cos(spherical.phi),
      spherical.r*Math.sin(spherical.phi)*Math.sin(spherical.theta));
    camera.lookAt(0,0,0);
  }
  mount.addEventListener('pointerdown',function(e){isDrag=true;prevX=e.clientX;prevY=e.clientY;mount.setPointerCapture(e.pointerId);});
  mount.addEventListener('pointermove',function(e){
    if(!isDrag)return;
    spherical.theta-=(e.clientX-prevX)*0.008;
    spherical.phi=Math.max(0.1,Math.min(Math.PI-0.1,spherical.phi-(e.clientY-prevY)*0.008));
    prevX=e.clientX;prevY=e.clientY;
    updateCam();
  });
  mount.addEventListener('pointerup',function(){isDrag=false;});
  mount.addEventListener('wheel',function(e){
    e.preventDefault();
    spherical.r=Math.max(80,Math.min(500,spherical.r+e.deltaY*0.3));
    updateCam();
  },{passive:false});

  // Raycaster for hover
  var raycaster=new THREE.Raycaster();
  raycaster.params.Points={threshold:5};
  var mouse=new THREE.Vector2();
  var hovMesh=null;
  mount.addEventListener('mousemove',function(e){
    if(isDrag)return;
    var r=mount.getBoundingClientRect();
    mouse.x=((e.clientX-r.left)/r.width)*2-1;
    mouse.y=-((e.clientY-r.top)/r.height)*2+1;
    raycaster.setFromCamera(mouse,camera);
    var hits=raycaster.intersectObjects(nodeObjs);
    var newHov=hits.length?hits[0].object:null;
    if(newHov!==hovMesh){
      if(hovMesh)hovMesh.scale.set(1,1,1);
      hovMesh=newHov;
      if(hovMesh){
        hovMesh.scale.set(1.8,1.8,1.8);
        edgeLines.forEach(function(l){
          var conn=l.userData.s===hovMesh||l.userData.t===hovMesh;
          l.material.opacity=conn?0.6:0.03;
        });
        nodeObjs.forEach(function(n){
          if(n===hovMesh){n.material.emissive.setHex(0x333300);return;}
          var conn=false;
          edgeLines.forEach(function(l){if((l.userData.s===hovMesh&&l.userData.t===n)||(l.userData.t===hovMesh&&l.userData.s===n))conn=true;});
          n.material.opacity=conn?1:0.15;n.material.transparent=!conn&&n!==hovMesh;
        });
        if(tip){
          var conns=edgeLines.filter(function(l){return l.userData.s===hovMesh||l.userData.t===hovMesh;}).length;
          tip.innerHTML='<b>'+hovMesh.userData.label+'</b><br><span style="color:var(--dim);font-size:.72rem">'+conns+' connections · '+hovMesh.userData.track+'</span>';
          tip.classList.add('show');
          tip.style.left=(e.clientX-mount.getBoundingClientRect().left+14)+'px';
          tip.style.top=(e.clientY-mount.getBoundingClientRect().top-36)+'px';
        }
      }else{
        edgeLines.forEach(function(l){l.material.opacity=l.userData.baseOp;});
        nodeObjs.forEach(function(n){n.material.opacity=1;n.material.transparent=false;n.material.emissive.setHex(0);});
        if(tip)tip.classList.remove('show');
      }
    }
  });
  mount.addEventListener('click',function(){
    if(hovMesh)window.location.href=hovMesh.userData.id+'.html';
  });

  var simSteps=0,maxSim=200;
  function animate(){
    requestAnimationFrame(animate);
    if(simSteps<maxSim){tick3D();simSteps++;}
    renderer.render(scene,camera);
  }
  var kgObs=new IntersectionObserver(function(es){
    es.forEach(function(e){if(e.isIntersecting){animate();kgObs.unobserve(e.target);}});
  },{threshold:0.05});
  kgObs.observe(mount);
})();
