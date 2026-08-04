let rows=[],sortKey='company',asc=true;
const body=document.querySelector('#jobs tbody');
const search=document.querySelector('#search');
function parseValue(row,key){
  const v=row[key]||'';
  if(key.includes('date')){const d=Date.parse(v);return Number.isNaN(d)?Infinity:d;}
  if(key.includes('rate')||key.includes('compensation')){
    const m=String(v).replace(/,/g,'').match(/\$([0-9.]+)/);return m?Number(m[1]):-1;
  }
  return String(v).toLowerCase();
}
function render(){
  const q=search.value.toLowerCase();
  const filtered=rows.filter(r=>Object.values(r).join(' ').toLowerCase().includes(q));
  filtered.sort((a,b)=>{const x=parseValue(a,sortKey),y=parseValue(b,sortKey);return (x<y?-1:x>y?1:0)*(asc?1:-1)});
  body.innerHTML=filtered.map(r=>`<tr>
  <td>${r.company}</td>
  <td><a href="${r.application_url}" target="_blank" rel="noopener">${r.role}</a></td>
  <td>${r.location}</td><td>${r.work_arrangement}</td>
  <td>${r.open_date}</td><td>${r.close_date}</td>
  <td>${r.hourly_rate}</td><td>${r.estimated_total_compensation}</td>
  </tr>`).join('');
}
fetch('data/opportunities.json').then(r=>r.json()).then(d=>{rows=d;render()});
document.querySelectorAll('th').forEach(th=>th.addEventListener('click',()=>{
 const k=th.dataset.key;if(sortKey===k)asc=!asc;else{sortKey=k;asc=true}render();
}));
search.addEventListener('input',render);
