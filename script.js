let rows=[],sortKey='company',ascending=true;
const tbody=document.querySelector('#jobs tbody');
const search=document.querySelector('#search');
function dateVal(v){if(v==='Rolling')return 8640000000000000;const d=Date.parse(v);return Number.isNaN(d)?8640000000000000:d}
function moneyVal(v){const m=String(v).replace(/,/g,'').match(/\$([0-9.]+)/);return m?Number(m[1]):-1}
function value(r,k){if(k.includes('date'))return dateVal(r[k]);if(k.includes('rate')||k.includes('compensation'))return moneyVal(r[k]);return String(r[k]||'').toLowerCase()}
function render(){
 const q=search.value.trim().toLowerCase();
 const filtered=rows.filter(r=>Object.values(r).join(' ').toLowerCase().includes(q));
 filtered.sort((a,b)=>{const x=value(a,sortKey),y=value(b,sortKey);return(x<y?-1:x>y?1:0)*(ascending?1:-1)});
 tbody.innerHTML=filtered.map(r=>`<tr>
 <td>${r.company}</td>
 <td><a href="${r.application_url}" target="_blank" rel="noopener">${r.role}</a></td>
 <td>${r.location}</td><td>${r.work}</td><td>${r.open_date}</td><td>${r.close_date}</td>
 <td>${r.hourly_rate}</td><td>${r.total_compensation}</td></tr>`).join('');
}
fetch('data/opportunities.json').then(r=>r.json()).then(d=>{rows=d;render()});
document.querySelectorAll('th').forEach(th=>th.addEventListener('click',()=>{const key=th.dataset.key;if(sortKey===key)ascending=!ascending;else{sortKey=key;ascending=true}render()}));
search.addEventListener('input',render);
