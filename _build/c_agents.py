from core import add, ICON

C = "agents"

I = {
    "tool": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.8-.7-.7-2.8z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/></svg>',
    "up": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 15l-6-6-6 6"/></svg>',
    "down": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "trash": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
    "pen": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/></svg>',
}

BASE = """.wrap{width:min(100%,620px);display:flex;flex-direction:column;gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px 18px}
.card h2{font-size:15px;margin:0 0 4px;color:var(--ink)}
.muted{color:var(--muted);font-size:13px}
.num{font-variant-numeric:tabular-nums}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.sm{padding:5px 10px;font-size:13px;border-radius:8px}
.ib{width:28px;height:28px;display:grid;place-items:center;border:0;background:none;color:var(--muted);border-radius:7px;cursor:pointer;flex:none}
.ib:hover{background:var(--surface-2);color:var(--ink)}.ib:disabled{opacity:.3;cursor:not-allowed}
.pill{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:600;border-radius:99px;padding:2px 9px;border:1px solid}
.pill.run{color:var(--accent);border-color:color-mix(in srgb,var(--accent) 40%,var(--line))}
.pill.ok{color:var(--good);border-color:color-mix(in srgb,var(--good) 40%,var(--line))}
.pill.bad{color:var(--bad);border-color:color-mix(in srgb,var(--bad) 40%,var(--line))}
.pill.wait{color:var(--muted);border-color:var(--line)}
pre{margin:0;font:12.5px/1.55 var(--mono);background:var(--surface-2);border:1px solid var(--line);border-radius:10px;padding:10px 12px;overflow-x:auto;color:var(--ink)}
.tg{width:40px;height:23px;border-radius:99px;background:var(--line);position:relative;flex:none;border:0;cursor:pointer;padding:0}
.tg::after{content:"";position:absolute;top:3px;left:3px;width:17px;height:17px;border-radius:50%;background:#fff;transition:left .15s}
.tg[aria-checked=true]{background:var(--accent)}.tg[aria-checked=true]::after{left:20px}"""

add(C, "tool-call-card", "Tool Call Card",
    "Shows that the AI used a tool, with its name, status and time. Open it to see the exact input and the result it got back.",
    BASE + """
details.tc{background:var(--surface);border:1px solid var(--line);border-radius:12px;overflow:hidden}
details.tc summary{list-style:none;display:flex;align-items:center;gap:10px;padding:10px 14px;cursor:pointer}
details.tc summary::-webkit-details-marker{display:none}
details.tc summary .ic{width:28px;height:28px;border-radius:8px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;flex:none}
details.tc summary b{color:var(--ink);font-size:14px;font-family:var(--mono);font-weight:600}
details.tc summary .sp{flex:1}
details.tc summary .ch{color:var(--muted);transition:transform .2s;display:grid}details.tc[open] summary .ch{transform:rotate(180deg)}
.io{padding:0 14px 14px;display:flex;flex-direction:column;gap:8px}
.io h3{font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:4px 0 0}""",
    f"""<div class="wrap">
  <details class="tc" id="t1"><summary><span class="ic">{I['tool']}</span><b>get_weather</b><span class="pill ok" id="st">Done</span><span class="sp"></span><span class="muted num">0.8s</span><span class="ch">{ICON['chev']}</span></summary>
    <div class="io"><h3>Input</h3><pre>{{
  "city": "Lisbon",
  "days": 3,
  "units": "celsius"
}}</pre><h3>Result</h3><pre>{{
  "forecast": [
    {{ "day": "Fri", "high": 24, "low": 16, "rain": 0.1 }},
    {{ "day": "Sat", "high": 22, "low": 15, "rain": 0.6 }},
    {{ "day": "Sun", "high": 25, "low": 17, "rain": 0.0 }}
  ]
}}</pre></div></details>
  <details class="tc" id="t2"><summary><span class="ic">{I['tool']}</span><b>search_flights</b><span class="pill run" id="st2">Running</span><span class="sp"></span><span class="muted num" id="tm">0.0s</span><span class="ch">{ICON['chev']}</span></summary>
    <div class="io"><h3>Input</h3><pre>{{ "from": "LHR", "to": "LIS", "date": "2026-10-09" }}</pre><h3>Result</h3><pre id="r2">Waiting for the result...</pre></div></details>
</div>""", """
var st2=document.getElementById('st2'),tm=document.getElementById('tm'),r2=document.getElementById('r2'),start=Date.now();
var tick=setInterval(function(){tm.textContent=((Date.now()-start)/1000).toFixed(1)+'s';},100);
setTimeout(function(){clearInterval(tick);st2.className='pill ok';st2.textContent='Done';r2.textContent='{\\n  "cheapest": { "airline": "Example Air", "price": 89, "depart": "07:15" },\\n  "results": 14\\n}';},2400);""")

add(C, "approval-request", "Action Approval Request",
    "Before an agent does something important, like sending an email, it shows exactly what it will do and waits for Allow or Deny.",
    BASE + """
.ap{border:1.5px solid color-mix(in srgb,var(--warn) 50%,var(--line));background:color-mix(in srgb,var(--warn) 6%,var(--surface));border-radius:var(--radius);padding:16px 18px}
.ap .hd{display:flex;gap:10px;align-items:flex-start;margin-bottom:12px}
.ap .hd svg{color:var(--warn);flex:none;margin-top:1px}
.ap h2{margin:0;font-size:15.5px;color:var(--ink)}.ap .hd p{margin:2px 0 0;font-size:13.5px}
.mail{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:14px;margin-bottom:14px}
.mail dl{display:grid;grid-template-columns:64px 1fr;gap:4px 10px;margin:0 0 10px;font-size:13px}
.mail dt{color:var(--muted)}.mail dd{margin:0;color:var(--ink);overflow-wrap:anywhere}
.mail p{margin:0;line-height:1.6;border-top:1px solid var(--line);padding-top:10px}
.acts{display:flex;gap:8px;flex-wrap:wrap}
.res{display:flex;gap:8px;align-items:center;font-size:14px;font-weight:600;padding:10px 12px;border-radius:10px}
.res.ok{color:var(--good);background:color-mix(in srgb,var(--good) 10%,var(--surface))}.res.no{color:var(--muted);background:var(--surface-2)}""",
    f"""<div class="wrap">
  <section class="ap" id="ap" aria-labelledby="aph">
    <div class="hd">{I['shield']}<div><h2 id="aph">The assistant wants to send an email</h2><p>Check the details. Nothing is sent until you allow it.</p></div></div>
    <div class="mail"><dl><dt>To</dt><dd>sam.porter@example.com</dd><dt>Subject</dt><dd>Moving our meeting to Thursday</dd></dl>
      <p>Hi Sam, could we move our meeting to Thursday at 3pm? Let me know if that works. Thanks, Jo</p></div>
    <div class="acts" id="acts"><button class="btn" type="button" data-a="deny" id="deny">Deny</button><button class="btn" type="button" data-a="edit">Edit first</button><button class="btn pri" type="button" data-a="allow">Allow and send</button></div>
  </section>
  <button class="btn" type="button" id="again" style="align-self:center" hidden>Show the request again</button>
</div>""", """
var acts=document.getElementById('acts'),again=document.getElementById('again'),html=acts.innerHTML;
// Tell your agent the decision here: 'allow', 'deny' or 'edit'.
function decide(a){if(a==='edit'){document.querySelector('.mail p').setAttribute('contenteditable','true');document.querySelector('.mail p').focus();return;}
  acts.innerHTML=a==='allow'?'<div class="res ok" role="status">"""+ICON['check'].replace('"', '\\"')+"""Email sent to sam.porter@example.com</div>':'<div class="res no" role="status">You denied this action. Nothing was sent.</div>';again.hidden=false;}
acts.addEventListener('click',function(e){var b=e.target.closest('button');if(b)decide(b.dataset.a);});
again.addEventListener('click',function(){acts.innerHTML=html;again.hidden=true;document.querySelector('.mail p').removeAttribute('contenteditable');document.getElementById('deny').focus();});
document.getElementById('deny').focus();""")

add(C, "task-plan", "Editable Task Plan",
    "The agent proposes a step by step plan before it starts. People can reorder, edit or remove steps, then approve the plan to run it.",
    BASE + """
ol.plan{list-style:none;margin:12px 0;padding:0;display:flex;flex-direction:column;gap:6px;counter-reset:s}
ol.plan li{display:flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:10px;padding:6px 6px 6px 10px;background:var(--surface);counter-increment:s}
ol.plan li::before{content:counter(s);width:22px;height:22px;border-radius:50%;background:var(--surface-2);color:var(--ink);font-size:12px;font-weight:700;display:grid;place-items:center;flex:none}
ol.plan li.done::before{content:"";background:var(--good)}
ol.plan li.run::before{border:2px solid var(--accent);border-top-color:transparent;background:none;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
ol.plan li span{flex:1;font-size:14px;color:var(--ink);min-width:0;overflow-wrap:anywhere}
ol.plan li input{flex:1;border:1px solid var(--accent);border-radius:7px;padding:5px 8px;background:var(--surface);color:var(--ink);font-size:14px;min-width:0}
.acts{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;align-items:center}
.locked .ib{visibility:hidden}""",
    """<div class="wrap"><div class="card" id="card">
  <h2>Proposed plan</h2><p class="muted" style="margin:0" id="sub">Review the steps before the assistant starts.</p>
  <ol class="plan" id="plan"></ol>
  <div class="acts"><span class="muted" id="st" role="status" aria-live="polite"></span><button class="btn pri" type="button" id="go">Approve and run</button></div>
</div></div>""", """
var steps=['Read the three uploaded sales files','Combine the numbers by month','Make a chart of monthly totals','Write a one page summary'];
var plan=document.getElementById('plan'),go=document.getElementById('go'),st=document.getElementById('st'),card=document.getElementById('card'),locked=false;
var UP='"""+I['up'].replace('"', '\\"')+"""',DN='"""+I['down'].replace('"', '\\"')+"""',PEN='"""+I['pen'].replace('"', '\\"')+"""',DEL='"""+I['trash'].replace('"', '\\"')+"""';
function render(){plan.innerHTML='';steps.forEach(function(s,i){var li=document.createElement('li');li.innerHTML='<span></span><button class="ib" type="button">'+UP+'</button><button class="ib" type="button">'+DN+'</button><button class="ib" type="button">'+PEN+'</button><button class="ib" type="button">'+DEL+'</button>';
  li.querySelector('span').textContent=s;var b=li.querySelectorAll('.ib');
  [['Move up',function(){steps.splice(i-1,0,steps.splice(i,1)[0]);render();plan.children[i-1].querySelectorAll('.ib')[0].focus();},i===0],
   ['Move down',function(){steps.splice(i+1,0,steps.splice(i,1)[0]);render();plan.children[i+1].querySelectorAll('.ib')[1].focus();},i===steps.length-1],
   ['Edit step',function(){var inp=document.createElement('input');inp.value=s;inp.setAttribute('aria-label','Step '+(i+1));li.replaceChild(inp,li.querySelector('span'));inp.focus();inp.select();
      function done(k){if(k&&inp.value.trim())steps[i]=inp.value.trim();render();}inp.onkeydown=function(e){if(e.key==='Enter')done(true);if(e.key==='Escape')done(false);};inp.onblur=function(){done(true);};},false],
   ['Remove step',function(){steps.splice(i,1);render();},steps.length<=1]].forEach(function(o,k){b[k].setAttribute('aria-label',o[0]+': '+s);b[k].onclick=o[1];b[k].disabled=o[2];});
  plan.appendChild(li);});go.disabled=!steps.length||locked;}
go.addEventListener('click',function(){locked=true;card.classList.add('locked');go.disabled=true;document.getElementById('sub').textContent='Running the approved plan.';
  var lis=plan.children;[].forEach.call(lis,function(li,i){setTimeout(function(){if(i>0)lis[i-1].className='done';li.className='run';st.textContent='Step '+(i+1)+' of '+lis.length;},900*i);});
  setTimeout(function(){lis[lis.length-1].className='done';st.textContent='All steps finished';go.textContent='Done';},900*lis.length);});
render();""")

add(C, "agent-timeline", "Agent Activity Timeline",
    "A timeline of everything an agent did: its thinking, tool calls, results and messages, with times and a filter by type.",
    BASE + """
.flt{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}
.flt button{border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:4px 12px;font-size:13px;cursor:pointer}
.flt button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
ol.tl{list-style:none;margin:0;padding:0 0 0 6px;position:relative}
ol.tl::before{content:"";position:absolute;left:15px;top:8px;bottom:8px;width:2px;background:var(--line)}
ol.tl li{position:relative;display:grid;grid-template-columns:22px 1fr auto;gap:12px;padding:7px 0;align-items:start}
ol.tl .dot{width:20px;height:20px;border-radius:50%;border:3px solid var(--surface);position:relative;z-index:1;margin-top:1px}
ol.tl b{display:block;font-size:13px;color:var(--ink)}ol.tl p{margin:1px 0 0;font-size:13.5px;color:var(--text);overflow-wrap:anywhere}
ol.tl time{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.think{background:#8b5cf6}.tool{background:#0ea5e9}.result{background:#16a34a}.msg{background:var(--accent)}""",
    """<div class="wrap"><div class="card">
  <h2>What the agent did</h2><p class="muted" style="margin:0">Research task, 7 steps</p>
  <div class="flt" role="group" aria-label="Filter by type" id="flt"></div>
  <ol class="tl" id="tl"></ol>
</div></div>""", """
var EV=[['think','Thought','I need current prices before I can compare the laptops.','10:02:04'],['tool','Tool call','search_web("lightweight laptop under 1000")','10:02:05'],
['result','Result','Found 8 reviews and 3 price lists.','10:02:07'],['think','Thought','Two models appear in most reviews. I will compare battery life.','10:02:08'],
['tool','Tool call','read_page("review-site.example/laptops-2026")','10:02:09'],['result','Result','Battery: model A 14 hours, model B 11 hours.','10:02:12'],['msg','Message','Model A is the better pick for travel because of the longer battery life.','10:02:14']];
var TYPES=[['all','All'],['think','Thinking'],['tool','Tool calls'],['result','Results'],['msg','Messages']],flt=document.getElementById('flt'),tl=document.getElementById('tl');
function render(f){tl.innerHTML='';EV.filter(function(e){return f==='all'||e[0]===f;}).forEach(function(e){var li=document.createElement('li');
  li.innerHTML='<span class="dot '+e[0]+'" aria-hidden="true"></span><div><b></b><p></p></div><time></time>';li.querySelector('b').textContent=e[1];li.querySelector('p').textContent=e[2];li.querySelector('time').textContent=e[3];tl.appendChild(li);});}
TYPES.forEach(function(t,i){var b=document.createElement('button');b.type='button';b.textContent=t[1];b.setAttribute('aria-pressed',i===0);
  b.onclick=function(){flt.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b);});render(t[0]);};flt.appendChild(b);});
render('all');""")

add(C, "file-diff", "File Change Preview",
    "Shows the changes an AI wants to make to a file, with removed lines in red and added lines in green, and buttons to accept or reject.",
    BASE + """
.wrap{width:min(100%,680px)}
.diff{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--surface)}
.dh{display:flex;align-items:center;gap:10px;padding:9px 12px;border-bottom:1px solid var(--line);background:var(--surface-2);font:13px var(--mono);color:var(--ink);flex-wrap:wrap}
.dh .add{color:color-mix(in srgb,var(--good) 85%,var(--ink))}.dh .del{color:var(--bad)}.dh .sp{flex:1}
.lines{overflow-x:auto;font:12.5px/1.6 var(--mono)}
.ln{display:grid;grid-template-columns:36px 36px 18px 1fr;white-space:pre;min-width:max-content}
.ln span{padding:0 8px;color:var(--muted);text-align:right;user-select:none}
.ln code{padding-right:14px;color:var(--ink)}
.ln.a{background:color-mix(in srgb,var(--good) 12%,transparent)}.ln.a .s{color:var(--good)}
.ln.d{background:color-mix(in srgb,var(--bad) 12%,transparent)}.ln.d .s{color:var(--bad)}
.acts{display:flex;justify-content:flex-end;gap:8px;padding:10px 12px;border-top:1px solid var(--line)}
.res{padding:12px;font-size:14px;font-weight:600;text-align:center}""",
    """<div class="wrap"><div class="diff" id="d">
  <div class="dh"><span>src/utils/price.js</span><span class="add">+3</span><span class="del">-2</span><span class="sp"></span></div>
  <div class="lines" id="lines" role="table" aria-label="Changes to price.js"></div>
  <div class="acts" id="acts"><button class="btn sm" type="button" id="rj">Reject</button><button class="btn sm pri" type="button" id="ac">Accept changes</button></div>
</div></div>""", """
var L=[[' ',1,1,'export function formatPrice(amount) {'],['-',2,null,'  return "$" + amount;'],['+',null,2,'  const value = Number(amount) || 0;'],['+',null,3,'  return value.toLocaleString("en-US", {'],['+',null,4,'    style: "currency", currency: "USD" });'],
[' ',3,5,'}'],[' ',4,6,''],['-',5,null,'// TODO: handle cents'],[' ',6,7,'export const TAX_RATE = 0.2;']];
var lines=document.getElementById('lines'),acts=document.getElementById('acts');
L.forEach(function(l){var d=document.createElement('div');d.className='ln'+(l[0]==='+'?' a':l[0]==='-'?' d':'');d.setAttribute('role','row');
  d.innerHTML='<span role="cell"></span><span role="cell"></span><span class="s" role="cell" aria-label="'+(l[0]==='+'?'added':l[0]==='-'?'removed':'unchanged')+'"></span><code role="cell"></code>';
  var c=d.children;c[0].textContent=l[1]||'';c[1].textContent=l[2]||'';c[2].textContent=l[0].trim();c[3].textContent=l[3];lines.appendChild(d);});
function done(msg,cls){acts.outerHTML='<div class="res" role="status" style="color:var(--'+cls+')">'+msg+'</div>';}
document.getElementById('ac').addEventListener('click',function(){done('Changes applied to price.js','good');});
document.getElementById('rj').addEventListener('click',function(){done('Changes rejected. The file was not changed.','muted');});""")

add(C, "web-results-card", "Web Results Card",
    "A card listing the web pages an AI read, with title, site and a short excerpt. Pages it used in the answer are marked.",
    BASE + """
.res{list-style:none;margin:12px 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.res li{display:flex;gap:12px;align-items:flex-start}
.fav{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;color:#fff;font-size:12px;font-weight:800;flex:none}
.res a{color:var(--ink);font-weight:600;font-size:14px;text-decoration:none}.res a:hover{color:var(--accent);text-decoration:underline}
.res small{display:block;color:var(--muted);font-size:12px}
.res p{margin:3px 0 0;font-size:13px;color:var(--text);line-height:1.5}
.used{font-size:11px;font-weight:700;color:var(--good);border:1px solid color-mix(in srgb,var(--good) 40%,var(--line));border-radius:99px;padding:0 7px;margin-left:6px;white-space:nowrap}
.more{margin-top:10px;border:0;background:none;color:var(--accent);font-weight:600;cursor:pointer;padding:4px 0;font-size:14px}""",
    """<div class="wrap"><div class="card">
  <h2>Sources</h2><p class="muted" style="margin:0" id="sum"></p>
  <ul class="res" id="res"></ul>
  <button class="more" type="button" id="more" aria-expanded="false">Show all sources</button>
</div></div>""", """
var R=[['Sleep Health Guide','sleepguide.example','Adults need 7 to 9 hours of sleep. Keeping a regular schedule matters more than the exact bedtime.','#2563eb',true],
['Better Rest Study','health-journal.example','People who woke at the same time every day reported feeling rested more often.','#0f766e',true],
['Evening Light and Sleep','science-daily.example','Bright screens before bed can delay sleep by up to 30 minutes in some people.','#b45309',true],
['10 Sleep Myths','wellness-blog.example','Napping is not always bad. Short naps before 3pm can help without hurting night sleep.','#7c3aed',false],
['Caffeine Timing','nutrition-facts.example','Caffeine can stay in the body for 5 to 6 hours, so an afternoon coffee may affect sleep.','#be123c',false]];
var res=document.getElementById('res'),more=document.getElementById('more'),all=false;
document.getElementById('sum').textContent='Read '+R.length+' pages, used '+R.filter(function(r){return r[4];}).length+' in the answer';
function render(){res.innerHTML='';(all?R:R.slice(0,3)).forEach(function(r){var li=document.createElement('li');
  li.innerHTML='<span class="fav" aria-hidden="true"></span><div><a href="#"></a>'+(r[4]?'<span class="used">Used</span>':'')+'<small></small><p></p></div>';
  li.querySelector('.fav').style.background=r[3];li.querySelector('.fav').textContent=r[0][0];li.querySelector('a').textContent=r[0];li.querySelector('small').textContent=r[1];li.querySelector('p').textContent=r[2];res.appendChild(li);});
  more.textContent=all?'Show fewer':'Show all '+R.length+' sources';more.setAttribute('aria-expanded',all);}
more.addEventListener('click',function(){all=!all;render();});render();""")

add(C, "run-log-console", "Agent Run Log",
    "A terminal style log that streams what an agent is doing, with colored levels, a pause button, auto scroll and copy.",
    BASE + """
.wrap{width:min(100%,700px)}
.con{border-radius:12px;overflow:hidden;border:1px solid #2a2a33;background:#101015;color:#d9d9e3;box-shadow:var(--shadow)}
.bar{display:flex;align-items:center;gap:8px;padding:8px 10px;background:#18181f;border-bottom:1px solid #2a2a33;flex-wrap:wrap}
.bar b{font-size:13px;color:#fff;margin-right:auto;display:flex;align-items:center;gap:8px}
.live{width:8px;height:8px;border-radius:50%;background:#4ade80;animation:bl 1.2s ease infinite}.paused .live{background:#fbbf24;animation:none}
@keyframes bl{50%{opacity:.3}}
.bar button{border:1px solid #33333d;background:#202029;color:#e5e5ee;border-radius:7px;padding:4px 10px;font-size:12.5px;cursor:pointer}
.bar button:hover{border-color:#8b8bff}.bar button[aria-pressed=true]{background:#2d2d5a;border-color:#8b8bff}
.log{height:260px;overflow-y:auto;padding:10px 12px;font:12.5px/1.65 var(--mono);margin:0;list-style:none}
.log li{white-space:pre-wrap;overflow-wrap:anywhere}.log time{color:#8a8a99;margin-right:8px}
.INFO{color:#7dd3fc}.OK{color:#86efac}.WARN{color:#fcd34d}.ERR{color:#fca5a5}.lv{display:inline-block;width:44px;font-weight:700}""",
    """<div class="wrap"><div class="con" id="con">
  <div class="bar"><b><span class="live" aria-hidden="true"></span><span id="state">Running</span></b>
    <button type="button" id="pause" aria-pressed="false">Pause</button><button type="button" id="auto" aria-pressed="true">Auto scroll</button><button type="button" id="copy">Copy</button><button type="button" id="clr">Clear</button></div>
  <ol class="log" id="log" aria-label="Agent log" aria-live="off"></ol>
</div></div>""", """
var LINES=[['INFO','Starting task: build weekly sales report'],['INFO','Opening sales_week_38.csv'],['OK','Loaded 1,204 rows'],['INFO','Grouping sales by region'],['WARN','3 rows have no region, marking them as Unknown'],
['OK','Created totals for 5 regions'],['INFO','Drawing bar chart'],['OK','Saved chart to report/week38.png'],['INFO','Writing summary'],['ERR','Could not reach email service, will retry in 5 seconds'],['OK','Email service is back'],['OK','Report sent to team@example.com']];
var log=document.getElementById('log'),con=document.getElementById('con'),pause=document.getElementById('pause'),auto=document.getElementById('auto'),state=document.getElementById('state'),i=0,paused=false,timer=null;
function stamp(){var d=new Date();return d.toTimeString().slice(0,8);}
function push(){if(paused)return;if(i>=LINES.length){state.textContent='Finished';clearInterval(timer);con.classList.add('paused');return;}var l=LINES[i++],li=document.createElement('li');
  li.innerHTML='<time></time><span class="lv '+l[0]+'"></span><span></span>';li.children[0].textContent=stamp();li.children[1].textContent=l[0];li.children[2].textContent=l[1];log.appendChild(li);
  if(auto.getAttribute('aria-pressed')==='true')log.scrollTop=log.scrollHeight;}
pause.addEventListener('click',function(){paused=!paused;pause.setAttribute('aria-pressed',paused);pause.textContent=paused?'Resume':'Pause';con.classList.toggle('paused',paused);if(i<LINES.length)state.textContent=paused?'Paused':'Running';});
auto.addEventListener('click',function(){auto.setAttribute('aria-pressed',auto.getAttribute('aria-pressed')!=='true');});
document.getElementById('clr').addEventListener('click',function(){log.innerHTML='';});
document.getElementById('copy').addEventListener('click',function(){var t=log.innerText,b=this;function ok(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy';},1500);}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(t).then(ok,ok);else{var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}ta.remove();ok();}});
push();timer=setInterval(push,700);""")

add(C, "subagent-grid", "Parallel Agents Status",
    "A grid of helper agents working at the same time, each with its own task, progress and status, and a button to stop any one of them.",
    BASE + """
.wrap{width:min(100%,720px)}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:12px}
.ag{border:1px solid var(--line);border-radius:12px;padding:12px;background:var(--surface);display:flex;flex-direction:column;gap:8px}
.ag .t{display:flex;align-items:center;gap:8px;justify-content:space-between}
.ag b{font-size:14px;color:var(--ink)}.ag p{margin:0;font-size:13px;color:var(--text);min-height:2.6em}
.bar{height:6px;border-radius:99px;background:var(--surface-2);overflow:hidden}.bar i{display:block;height:100%;background:var(--accent);transition:width .4s}
.ag.done .bar i{background:var(--good)}.ag.stop .bar i{background:var(--muted)}
.ft{display:flex;justify-content:space-between;align-items:center}
.sum{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
@media(max-width:560px){.grid{grid-template-columns:1fr}}""",
    """<div class="wrap"><div class="card">
  <div class="sum"><div><h2>Research team</h2><p class="muted" style="margin:0" id="sum" role="status" aria-live="polite"></p></div><button class="btn sm" type="button" id="all">Stop all</button></div>
  <div class="grid" id="g"></div>
</div></div>""", """
var A=[['Price finder','Comparing prices on 6 shops'],['Review reader','Reading 12 customer reviews'],['Spec checker','Checking battery and weight'],['Deal watcher','Looking for coupons and sales']];
var g=document.getElementById('g'),sum=document.getElementById('sum'),state=A.map(function(){return {p:0,s:'run'};}),timer;
function paint(){g.innerHTML='';A.forEach(function(a,i){var st=state[i],d=document.createElement('div');d.className='ag'+(st.s==='done'?' done':st.s==='stop'?' stop':'');
  var pill=st.s==='done'?'<span class="pill ok">Done</span>':st.s==='stop'?'<span class="pill wait">Stopped</span>':'<span class="pill run">Working</span>';
  d.innerHTML='<div class="t"><b></b>'+pill+'</div><p></p><div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="'+Math.round(st.p)+'"><i style="width:'+st.p+'%"></i></div><div class="ft"><span class="muted num">'+Math.round(st.p)+'%</span></div>';
  d.querySelector('b').textContent=a[0];d.querySelector('p').textContent=st.s==='done'?'Finished. Results are ready.':a[1];d.querySelector('.bar').setAttribute('aria-label',a[0]+' progress');
  if(st.s==='run'){var b=document.createElement('button');b.className='btn sm';b.type='button';b.textContent='Stop';b.setAttribute('aria-label','Stop '+a[0]);b.onclick=function(){st.s='stop';paint();};d.querySelector('.ft').appendChild(b);}
  g.appendChild(d);});
  var done=state.filter(function(s){return s.s==='done';}).length,run=state.filter(function(s){return s.s==='run';}).length;sum.textContent=run+' working, '+done+' done';document.getElementById('all').disabled=!run;
  if(!run)clearInterval(timer);}
function step(){var changed=false;state.forEach(function(s,i){if(s.s==='run'){s.p=Math.min(100,s.p+4+Math.random()*9+i);if(s.p>=100)s.s='done';changed=true;}});if(changed)paint();}
document.getElementById('all').addEventListener('click',function(){state.forEach(function(s){if(s.s==='run')s.s='stop';});paint();});
paint();timer=setInterval(step,600);""")

add(C, "memory-panel", "AI Memory Manager",
    "A list of things the assistant remembers about someone, with edit and delete for each item, a way to add one, and a switch to turn memory off.",
    BASE + """
.hd{display:flex;justify-content:space-between;align-items:center;gap:12px}
ul.mem{list-style:none;margin:14px 0 10px;padding:0;display:flex;flex-direction:column;gap:6px}
ul.mem li{display:flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:10px;padding:6px 6px 6px 12px;background:var(--surface)}
ul.mem li span{flex:1;font-size:14px;color:var(--ink);min-width:0;overflow-wrap:anywhere}
ul.mem li input{flex:1;border:1px solid var(--accent);border-radius:7px;padding:5px 8px;background:var(--surface);color:var(--ink);font-size:14px;min-width:0}
.off ul.mem{opacity:.45;pointer-events:none}
.add{display:flex;gap:8px}.add input{flex:1;border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--surface);color:var(--ink);min-width:0}
.add input:focus{outline:0;border-color:var(--accent)}
.empty{font-size:14px;color:var(--muted);text-align:center;padding:12px;border:1px dashed var(--line);border-radius:10px}""",
    """<div class="wrap"><div class="card" id="card">
  <div class="hd"><div><h2 id="mh">Memory</h2><p class="muted" style="margin:0">Things the assistant remembers to help you better.</p></div><button class="tg" type="button" role="switch" aria-checked="true" aria-labelledby="mh" id="on"></button></div>
  <ul class="mem" id="mem"></ul>
  <form class="add" id="add"><label class="sr" for="ni">Add something to remember</label><input id="ni" placeholder="Add something to remember"><button class="btn sm" type="submit">Add</button></form>
  <p class="muted" id="st" role="status" aria-live="polite" style="margin:10px 0 0"></p>
</div></div>""", """
var M=['Prefers short answers with bullet points','Is learning Spanish, at a beginner level','Works as a product designer','Is vegetarian'];
var mem=document.getElementById('mem'),st=document.getElementById('st'),card=document.getElementById('card'),on=document.getElementById('on');
var PEN='"""+I['pen'].replace('"', '\\"')+"""',DEL='"""+I['trash'].replace('"', '\\"')+"""';
function render(){mem.innerHTML=M.length?'':'<li class="empty" style="justify-content:center;border-style:dashed">Nothing saved yet.</li>';
  M.forEach(function(m,i){var li=document.createElement('li');li.innerHTML='<span></span><button class="ib" type="button">'+PEN+'</button><button class="ib" type="button">'+DEL+'</button>';li.querySelector('span').textContent=m;
    var b=li.querySelectorAll('.ib');b[0].setAttribute('aria-label','Edit: '+m);b[1].setAttribute('aria-label','Forget: '+m);
    b[1].onclick=function(){M.splice(i,1);render();st.textContent='Forgotten: '+m;};
    b[0].onclick=function(){var inp=document.createElement('input');inp.value=m;inp.setAttribute('aria-label','Edit memory');li.replaceChild(inp,li.querySelector('span'));inp.focus();
      function done(k){if(k&&inp.value.trim()){M[i]=inp.value.trim();st.textContent='Memory updated';}render();}inp.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();done(true);}if(e.key==='Escape')done(false);};inp.onblur=function(){done(true);};};
    mem.appendChild(li);});}
document.getElementById('add').addEventListener('submit',function(e){e.preventDefault();var ni=document.getElementById('ni'),v=ni.value.trim();if(!v)return;M.push(v);ni.value='';render();st.textContent='Saved: '+v;});
on.addEventListener('click',function(){var v=on.getAttribute('aria-checked')!=='true';on.setAttribute('aria-checked',v);card.classList.toggle('off',!v);
  document.getElementById('ni').disabled=!v;st.textContent=v?'Memory is on.':'Memory is off. Nothing new will be saved, and saved items are not used.';});
render();""")

add(C, "connectors-list", "App Connectors List",
    "A list of apps the AI can connect to, like calendar, email and files. Each shows what it can access, with Connect and Disconnect buttons.",
    BASE + """
ul.cx{list-style:none;margin:12px 0 0;padding:0;display:flex;flex-direction:column}
ul.cx li{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:1px solid var(--line)}
ul.cx li:first-child{border-top:0}
.lg{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;color:#fff;flex:none}
.inf{flex:1;min-width:0}.inf b{display:flex;align-items:center;gap:8px;color:var(--ink);font-size:14.5px;flex-wrap:wrap}
.inf p{margin:2px 0 0;font-size:13px;color:var(--muted)}
.scopes{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px}.scopes span{font-size:11.5px;background:var(--surface-2);border:1px solid var(--line);border-radius:6px;padding:1px 7px;color:var(--text)}
.btn.sm{flex:none}""",
    """<div class="wrap"><div class="card">
  <h2>Connected apps</h2><p class="muted" style="margin:0">Let the assistant read and act in your apps. You can disconnect any time.</p>
  <ul class="cx" id="cx"></ul>
  <p class="muted" id="st" role="status" aria-live="polite" style="margin:8px 0 0"></p>
</div></div>""", """
var APPS=[['Calendar','#2563eb','<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>','Find free times and create events.',['Read events','Create events'],true],
['Email','#dc2626','<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>','Search mail and draft replies. Sending always needs your approval.',['Read mail','Create drafts'],false],
['Files','#0f766e','<path d="M3 6h7l2 2h9v11H3z"/>','Find and read documents you choose.',['Read files'],true],
['Notes','#b45309','<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h6M9 16h6"/>','Save summaries and to-do lists.',['Read notes','Create notes'],false]];
var cx=document.getElementById('cx'),st=document.getElementById('st');
function render(){cx.innerHTML='';APPS.forEach(function(a){var li=document.createElement('li');
  li.innerHTML='<span class="lg" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+a[2]+'</svg></span><div class="inf"><b><span></span>'+(a[5]?'<span class="pill ok">Connected</span>':'')+'</b><p></p><div class="scopes"></div></div><button class="btn sm" type="button"></button>';
  li.querySelector('.lg').style.background=a[1];li.querySelector('b span').textContent=a[0];li.querySelector('p').textContent=a[3];
  a[4].forEach(function(s){var sp=document.createElement('span');sp.textContent=s;li.querySelector('.scopes').appendChild(sp);});
  var b=li.querySelector('button');b.textContent=a[5]?'Disconnect':'Connect';b.setAttribute('aria-label',(a[5]?'Disconnect ':'Connect ')+a[0]);if(!a[5])b.classList.add('pri');
  b.onclick=function(){a[5]=!a[5];render();st.textContent=a[0]+(a[5]?' connected':' disconnected');cx.querySelector('[aria-label$="'+a[0]+'"]').focus();};cx.appendChild(li);});}
render();""")
