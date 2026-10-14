"use strict";
const kind=document.querySelector('#kind'),search=document.querySelector('#search'),projects=[...document.querySelectorAll('.project')],routeButtons=[...document.querySelectorAll('[data-route]')];
const routes={product:['market','finddr','policy'],research:['stable','risk','policy'],tools:['invoice','zip']};
let route='';
function apply(updateURL=true){
 const query=search.value.trim().toLocaleLowerCase();let count=0;
 projects.forEach(p=>{p.hidden=(kind.value!=='all'&&p.dataset.kind!==kind.value)||(route&&!routes[route].includes(p.id))||(query&&!p.textContent.toLocaleLowerCase().includes(query));if(!p.hidden)count++});
 document.querySelector('#count').textContent=count+' / '+projects.length+' 项作品';document.querySelector('#no-results').hidden=count>0;
 routeButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.route===route)));
 if(updateURL){const url=new URL(location.href);['kind','q','route'].forEach(k=>url.searchParams.delete(k));if(kind.value!=='all')url.searchParams.set('kind',kind.value);if(query)url.searchParams.set('q',search.value.trim());if(route)url.searchParams.set('route',route);if(projects.some(p=>p.hidden&&'#'+p.id===url.hash))url.hash='projects';history.replaceState(null,'',url)}
}
function restore(){const params=new URL(location.href).searchParams;kind.value=['all','existing','demo'].includes(params.get('kind'))?params.get('kind'):'all';search.value=(params.get('q')||'').slice(0,80);route=Object.hasOwn(routes,params.get('route'))?params.get('route'):'';apply(false);revealTarget()}
function revealTarget(){let id;try{id=decodeURIComponent(location.hash.slice(1))}catch{return}const target=projects.find(p=>p.id===id);if(!target)return;if(target.hidden){kind.value='all';search.value='';route='';apply()}target.querySelector('details').open=true;target.scrollIntoView({block:'start'})}
kind.addEventListener('change',()=>apply());search.addEventListener('input',()=>apply());
routeButtons.forEach(b=>b.addEventListener('click',()=>{route=route===b.dataset.route?'':b.dataset.route;kind.value='all';search.value='';apply()}));
document.querySelector('#clear').addEventListener('click',()=>{kind.value='all';search.value='';route='';apply();search.focus()});
window.addEventListener('popstate',restore);window.addEventListener('hashchange',revealTarget);
document.querySelector('.filter').hidden=false;document.querySelector('.routes').hidden=false;restore();
