from core import add, ICON

C = "settings"

BASE = """.wrap{width:min(100%,580px);display:flex;flex-direction:column;gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:18px 20px}
.card h2{font-size:15.5px;margin:0 0 4px;color:var(--ink)}
.muted{color:var(--muted);font-size:13px}
.num{font-variant-numeric:tabular-nums}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.danger{color:var(--bad)}.btn.danger:hover{border-color:var(--bad)}
.tg{width:40px;height:23px;border-radius:99px;background:var(--line);position:relative;flex:none;border:0;cursor:pointer;padding:0;transition:background .15s}
.tg::after{content:"";position:absolute;top:3px;left:3px;width:17px;height:17px;border-radius:50%;background:#fff;transition:left .15s;box-shadow:0 1px 2px rgba(0,0,0,.2)}
.tg[aria-checked=true]{background:var(--accent)}.tg[aria-checked=true]::after{left:20px}
.row{display:flex;justify-content:space-between;align-items:center;gap:14px;padding:12px 0;border-top:1px solid var(--line)}
.row:first-of-type{border-top:0}
.row b{display:block;color:var(--ink);font-size:14px;font-weight:600}.row small{display:block;color:var(--muted);font-size:12.5px;margin-top:1px}
.seg{display:flex;background:var(--surface-2);border-radius:12px;padding:4px;gap:4px}
.seg button{flex:1;border:0;background:none;padding:8px 10px;border-radius:9px;font-size:14px;color:var(--muted);cursor:pointer;font-weight:500}
.seg button[aria-checked=true]{background:var(--surface);color:var(--ink);font-weight:700;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.sample{margin:14px 0 0;padding:12px 14px;border-radius:12px;background:var(--surface-2);font-size:14px;line-height:1.6;color:var(--text);transition:opacity .2s}
.sample small{display:block;color:var(--muted);font-size:12px;margin-bottom:4px}"""

# Radio group helper: arrow keys move, Space or Enter selects (roving tabindex)
RADIO = """function radioGroup(group,onPick){var items=[].slice.call(group.querySelectorAll('[role=radio]'));
  function pick(it,focus){items.forEach(function(x){var on=x===it;x.setAttribute('aria-checked',on);x.tabIndex=on?0:-1;});if(focus)it.focus();onPick(it);}
  items.forEach(function(it,i){it.addEventListener('click',function(){pick(it,false);});
    it.addEventListener('keydown',function(e){var n=null;if(e.key==='ArrowRight'||e.key==='ArrowDown')n=items[(i+1)%items.length];if(e.key==='ArrowLeft'||e.key==='ArrowUp')n=items[(i-1+items.length)%items.length];
      if(n){e.preventDefault();pick(n,true);}});});
  pick(items.filter(function(x){return x.getAttribute('aria-checked')==='true';})[0]||items[0],false);}"""

add(C, "model-cards", "Model Selection Cards",
    "Choose a model from cards that compare speed and quality with small meters. Works with arrow keys like a radio group.",
    BASE + """
.wrap{width:min(100%,720px)}
.mc{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}
.m{text-align:left;border:1.5px solid var(--line);background:var(--surface);border-radius:14px;padding:14px;cursor:pointer;display:flex;flex-direction:column;gap:8px;position:relative}
.m[aria-checked=true]{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 6%,var(--surface))}
.m b{color:var(--ink);font-size:15px}.m p{margin:0;font-size:13px;color:var(--muted);line-height:1.45}
.new{position:absolute;top:10px;right:10px;font-size:11px;font-weight:700;color:var(--accent);background:var(--accent-soft);border-radius:99px;padding:1px 8px}
.mt{display:grid;grid-template-columns:52px 1fr;align-items:center;gap:6px;font-size:12px;color:var(--muted)}
.dots{display:flex;gap:3px}.dots i{width:14px;height:6px;border-radius:3px;background:var(--surface-2)}.dots i.on{background:var(--accent)}
@media(max-width:600px){.mc{grid-template-columns:1fr}}""",
    """<div class="wrap"><div class="card">
  <h2>Choose a model</h2><p class="muted" style="margin:0" id="sel" aria-live="polite"></p>
  <div class="mc" role="radiogroup" aria-label="Model" id="g">
    <button class="m" type="button" role="radio" aria-checked="false" data-n="Fast" data-s="5" data-q="2"><b>Fast</b><p>Quick replies for simple questions and short tasks.</p></button>
    <button class="m" type="button" role="radio" aria-checked="true" data-n="Balanced" data-s="3" data-q="4"><b>Balanced</b><p>A good choice for writing, summaries and everyday work.</p></button>
    <button class="m" type="button" role="radio" aria-checked="false" data-n="Deep" data-s="1" data-q="5"><span class="new">New</span><b>Deep</b><p>Takes longer, but thinks through hard problems and code.</p></button>
  </div>
</div></div>""", RADIO + """
document.querySelectorAll('.m').forEach(function(m){['Speed','Quality'].forEach(function(k){var v=+m.dataset[k==='Speed'?'s':'q'],row=document.createElement('div');row.className='mt';
  row.innerHTML='<span>'+k+'</span><span class="dots" aria-hidden="true">'+[1,2,3,4,5].map(function(i){return '<i'+(i<=v?' class="on"':'')+'></i>';}).join('')+'</span>';m.appendChild(row);});
  m.setAttribute('aria-label',m.dataset.n+'. Speed '+m.dataset.s+' of 5, quality '+m.dataset.q+' of 5');});
radioGroup(document.getElementById('g'),function(it){document.getElementById('sel').textContent='Selected: '+it.dataset.n;});""")

add(C, "temperature-slider", "Creativity Slider",
    "A slider for the model temperature with plain labels from Precise to Creative, a live value, and a sample line that shows the effect.",
    BASE + """
.top{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.val{font-size:22px;font-weight:800;color:var(--ink)}
input[type=range]{width:100%;margin:16px 0 6px;accent-color:var(--accent);height:24px}
.ticks{display:flex;justify-content:space-between;font-size:12.5px;color:var(--muted)}
.ticks span.on{color:var(--ink);font-weight:700}""",
    """<div class="wrap"><div class="card">
  <div class="top"><div><h2 id="lb">Creativity</h2><p class="muted" style="margin:0">Also called temperature</p></div><span class="val num" id="v" aria-hidden="true">0.7</span></div>
  <input id="r" type="range" min="0" max="2" step="0.1" value="0.7" aria-labelledby="lb" aria-describedby="hint">
  <div class="ticks" aria-hidden="true"><span data-z="0">Precise</span><span data-z="1">Balanced</span><span data-z="2">Creative</span></div>
  <p class="sample" id="s" aria-live="polite"></p><p class="sr" id="hint">Lower values give more predictable answers. Higher values give more varied answers.</p>
</div></div>""", """
var r=document.getElementById('r'),v=document.getElementById('v'),s=document.getElementById('s'),ticks=[].slice.call(document.querySelectorAll('.ticks span'));
var SAMPLES=[[0.4,'Precise','A cat is a small, furry animal that people keep as a pet.'],[1.2,'Balanced','A cat is a curious little companion that naps in sunny spots and ignores your calls.'],
[2.01,'Creative','A cat is a velvet philosopher who rules the sofa and judges your life choices at 3am.']];
function render(){var x=+r.value,z=SAMPLES.filter(function(p){return x<p[0];})[0];v.textContent=x.toFixed(1);r.setAttribute('aria-valuetext',x.toFixed(1)+', '+z[1]);
  s.innerHTML='<small>Example answer to "Describe a cat in one sentence"</small>';s.appendChild(document.createTextNode(z[2]));
  ticks.forEach(function(t){t.classList.toggle('on',t.textContent===z[1]);});}
r.addEventListener('input',render);render();""")

add(C, "system-prompt-editor", "System Prompt Editor",
    "Edit the instructions the AI follows in every chat. Includes ready-made starters, a character count, and Save only when something changed.",
    BASE + """
.wrap{width:min(100%,640px)}
.hd{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:10px}
select{border:1px solid var(--line);border-radius:10px;padding:7px 10px;background:var(--surface);color:var(--ink);font-size:13.5px}
textarea{width:100%;min-height:150px;resize:vertical;border:1px solid var(--line);border-radius:12px;padding:12px;background:var(--surface-2);color:var(--ink);font:13.5px/1.6 var(--mono)}
textarea:focus{outline:0;border-color:var(--accent);background:var(--surface)}
.ft{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:10px;flex-wrap:wrap}
.ft div{display:flex;gap:8px}
.dirty{color:var(--warn);font-weight:600}.saved{color:var(--good);font-weight:600}""",
    """<div class="wrap"><div class="card">
  <div class="hd"><div><h2>Custom instructions</h2><p class="muted" style="margin:0">The AI follows these in every new chat.</p></div>
    <label class="sr" for="tpl">Start from a template</label><select id="tpl"><option value="">Start from a template</option><option value="tutor">Patient tutor</option><option value="editor">Strict editor</option><option value="brief">Short answers</option></select></div>
  <label class="sr" for="ta">Instructions</label><textarea id="ta" maxlength="1500" spellcheck="true"></textarea>
  <div class="ft"><span class="muted num" id="st" role="status" aria-live="polite"></span><div><button class="btn" type="button" id="rs">Reset</button><button class="btn pri" type="button" id="sv" disabled>Save</button></div></div>
</div></div>""", """
var T={tutor:'You are a patient tutor. Explain ideas step by step using simple words and one short example. Ask a question at the end to check understanding.',
editor:'You are a strict editor. Point out unclear sentences, repeated words and weak verbs. Suggest a shorter version of each paragraph.',
brief:'Answer in three sentences or fewer. Use plain words. Skip greetings and summaries.'};
var saved='Be friendly and clear. Use short paragraphs. When you are not sure, say so.',ta=document.getElementById('ta'),st=document.getElementById('st'),sv=document.getElementById('sv'),tpl=document.getElementById('tpl');
function showStatus(msg,cls){var n=ta.value.length;st.innerHTML=n.toLocaleString()+' / 1,500'+(msg?' <span class="'+cls+'">'+msg+'</span>':'');}
function check(){var dirty=ta.value!==saved;sv.disabled=!dirty;showStatus(dirty?'Unsaved changes':'','dirty');}
ta.addEventListener('input',check);
tpl.addEventListener('change',function(){if(!tpl.value)return;ta.value=T[tpl.value];tpl.value='';check();ta.focus();});
document.getElementById('rs').addEventListener('click',function(){ta.value=saved;check();});
sv.addEventListener('click',function(){saved=ta.value;sv.disabled=true;showStatus('Saved','saved');});
window.addEventListener('beforeunload',function(e){if(ta.value!==saved){e.preventDefault();e.returnValue='';}});
ta.value=saved;check();""")

add(C, "response-length", "Answer Length Control",
    "A three-way switch for short, medium or long answers, with a preview that shows how much text each choice gives.",
    BASE + ".seg{margin-top:12px}",
    """<div class="wrap"><div class="card">
  <h2 id="lb">Answer length</h2><p class="muted" style="margin:0">How much detail should the AI give?</p>
  <div class="seg" role="radiogroup" aria-labelledby="lb" id="g">
    <button type="button" role="radio" aria-checked="false" data-k="short">Short</button>
    <button type="button" role="radio" aria-checked="true" data-k="medium">Medium</button>
    <button type="button" role="radio" aria-checked="false" data-k="long">Long</button></div>
  <p class="sample" id="s" aria-live="polite"></p>
</div></div>""", RADIO + """
var S={short:['About 1 to 2 sentences','Drink water, sleep well and take short breaks.'],
medium:['About one paragraph','Drink a glass of water when you wake up, try to sleep at the same time each night, and take a five minute break every hour. Small habits like these add up over a week.'],
long:['Several paragraphs with steps','Start with water: keep a bottle on your desk and refill it twice a day. Next, protect your sleep by going to bed at the same time, even on weekends, and keeping screens out of the bedroom. During the day, set a timer to stand up and stretch every hour. After two weeks, check which habit was hardest and adjust it.']};
var s=document.getElementById('s');
radioGroup(document.getElementById('g'),function(it){var v=S[it.dataset.k];s.innerHTML='<small>'+v[0]+'</small>';s.appendChild(document.createTextNode(v[1]));});""")

add(C, "tone-selector", "Tone Selector",
    "Pick how the AI should sound: friendly, professional, casual or direct. A sample reply updates so people can hear the difference.",
    BASE + """
.tones{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.tones button{border:1.5px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:7px 14px;font-size:14px;cursor:pointer}
.tones button[aria-checked=true]{border-color:var(--accent);background:var(--accent-soft);color:var(--ink);font-weight:700}""",
    """<div class="wrap"><div class="card">
  <h2 id="lb">Tone of voice</h2><p class="muted" style="margin:0">Choose how replies should sound.</p>
  <div class="tones" role="radiogroup" aria-labelledby="lb" id="g">
    <button type="button" role="radio" aria-checked="true" data-k="friendly">Friendly</button>
    <button type="button" role="radio" aria-checked="false" data-k="pro">Professional</button>
    <button type="button" role="radio" aria-checked="false" data-k="casual">Casual</button>
    <button type="button" role="radio" aria-checked="false" data-k="direct">Direct</button></div>
  <p class="sample" id="s" aria-live="polite"></p>
</div></div>""", RADIO + """
var S={friendly:'Happy to help! Your order ships tomorrow, and you will get a tracking link by email as soon as it leaves.',
pro:'Thank you for your message. Your order is scheduled to ship tomorrow. A tracking link will be sent to your email address.',
casual:'Good news, your order goes out tomorrow. Keep an eye on your inbox for the tracking link.',
direct:'Ships tomorrow. Tracking link will be emailed.'};
var s=document.getElementById('s');
radioGroup(document.getElementById('g'),function(it){s.innerHTML='<small>Sample reply to "When will my order ship?"</small>';s.appendChild(document.createTextNode(S[it.dataset.k]));});""")

add(C, "feature-toggles", "Feature Toggles",
    "A settings list of switches for AI features like web search, memory and code running, each with a short explanation.",
    BASE + ".card{padding-top:10px;padding-bottom:6px}.ic{width:34px;height:34px;border-radius:10px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;flex:none}.row>div:first-child{display:flex;gap:12px;align-items:center;min-width:0}",
    """<div class="wrap"><div class="card" id="list">
  <h2 style="margin:10px 0 4px">Features</h2><p class="muted" style="margin:0 0 6px">Turn tools on or off for your chats.</p>
</div><p class="muted" id="st" role="status" aria-live="polite" style="text-align:center;margin:0"></p></div>""", """
var ICON={search:'<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',memory:'<path d="M12 3a4 4 0 00-4 4v1a4 4 0 00-2 7.5V17a4 4 0 008 0V7a4 4 0 00-2-4z"/><path d="M12 3a4 4 0 014 4v1a4 4 0 012 7.5V17a4 4 0 01-8 0"/>',
code:'<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',image:'<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>'};
var F=[['search','Web search','Look up current information online when needed.',true],['memory','Memory','Remember details you share across chats.',false],
['code','Code runner','Run small programs to check math and data.',true],['image','Image creation','Create pictures from your descriptions.',false]];
var list=document.getElementById('list'),st=document.getElementById('st');
F.forEach(function(f){var row=document.createElement('div');row.className='row';
  row.innerHTML='<div><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+ICON[f[0]]+'</svg></span><div><b id="l-'+f[0]+'"></b><small></small></div></div><button class="tg" type="button" role="switch" aria-labelledby="l-'+f[0]+'"></button>';
  row.querySelector('b').textContent=f[1];row.querySelector('small').textContent=f[2];var t=row.querySelector('.tg');t.setAttribute('aria-checked',f[3]);
  t.addEventListener('click',function(){f[3]=!f[3];t.setAttribute('aria-checked',f[3]);st.textContent=f[1]+(f[3]?' turned on':' turned off');});list.appendChild(row);});""")

add(C, "persona-cards", "Assistant Persona Cards",
    "Cards for different assistant roles, like tutor, editor or coach. Picking one changes how the assistant greets you.",
    BASE + """
.wrap{width:min(100%,700px)}
.pg{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:14px}
.p{display:flex;gap:12px;align-items:flex-start;text-align:left;border:1.5px solid var(--line);background:var(--surface);border-radius:14px;padding:14px;cursor:pointer}
.p[aria-checked=true]{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 6%,var(--surface))}
.p .a{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;font-weight:800;color:#fff;flex:none}
.p b{display:block;color:var(--ink);font-size:14.5px}.p span{font-size:13px;color:var(--muted);line-height:1.45}
.greet{display:flex;gap:10px;align-items:flex-start;margin-top:14px}
.greet .a{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;color:#fff;font-weight:800;font-size:12px;flex:none}
.greet p{margin:0;background:var(--surface-2);border-radius:4px 14px 14px 14px;padding:10px 13px;font-size:14px}
@media(max-width:560px){.pg{grid-template-columns:1fr}}""",
    """<div class="wrap"><div class="card">
  <h2 id="lb">Choose an assistant</h2><p class="muted" style="margin:0">Each one has its own style and focus.</p>
  <div class="pg" role="radiogroup" aria-labelledby="lb" id="g">
    <button class="p" type="button" role="radio" aria-checked="true" data-c="#4f46e5" data-g="Hi! What would you like to learn today? We can go one step at a time."><span class="a" style="background:#4f46e5">T</span><span><b>Tutor</b><span>Explains ideas slowly with examples.</span></span></button>
    <button class="p" type="button" role="radio" aria-checked="false" data-c="#0f766e" data-g="Paste your text and I will make it clearer and shorter."><span class="a" style="background:#0f766e">E</span><span><b>Editor</b><span>Tightens writing and fixes grammar.</span></span></button>
    <button class="p" type="button" role="radio" aria-checked="false" data-c="#c2410c" data-g="What goal are you working on this week? Let us make a simple plan."><span class="a" style="background:#c2410c">C</span><span><b>Coach</b><span>Helps you set goals and keep going.</span></span></button>
    <button class="p" type="button" role="radio" aria-checked="false" data-c="#1d4ed8" data-g="Share your numbers and I will find the trends that matter."><span class="a" style="background:#1d4ed8">A</span><span><b>Analyst</b><span>Reads data and explains what it means.</span></span></button>
  </div>
  <div class="greet" aria-live="polite"><span class="a" id="ga" aria-hidden="true"></span><p id="gp"></p></div>
</div></div>""", RADIO + """
var ga=document.getElementById('ga'),gp=document.getElementById('gp');
radioGroup(document.getElementById('g'),function(it){ga.style.background=it.dataset.c;ga.textContent=it.querySelector('.a').textContent;gp.textContent=it.dataset.g;});""")

add(C, "advanced-parameters", "Advanced Parameters Panel",
    "A folding panel for power users: maximum answer length, top p, and stop words you can add and remove, with a reset to defaults.",
    BASE + """
details.adv{border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);box-shadow:var(--shadow)}
details.adv summary{list-style:none;display:flex;justify-content:space-between;align-items:center;padding:14px 18px;cursor:pointer;font-weight:700;color:var(--ink)}
details.adv summary::-webkit-details-marker{display:none}
details.adv summary svg{transition:transform .2s;color:var(--muted)}details.adv[open] summary svg{transform:rotate(180deg)}
.body{padding:4px 18px 18px;display:flex;flex-direction:column;gap:16px}
.f label{display:flex;justify-content:space-between;font-size:13.5px;font-weight:600;color:var(--ink);margin-bottom:6px}
.f label span{color:var(--muted);font-weight:500}
.f input[type=number]{width:100%;border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--surface);color:var(--ink)}
.f input[type=range]{width:100%;accent-color:var(--accent)}
.stops{display:flex;flex-wrap:wrap;gap:6px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:6px}
.stops:focus-within{border-color:var(--accent)}
.stop{display:inline-flex;align-items:center;gap:4px;background:var(--surface-2);border-radius:7px;padding:3px 4px 3px 8px;font:12.5px var(--mono);color:var(--ink)}
.stop button{border:0;background:none;color:var(--muted);cursor:pointer;display:grid;place-items:center;width:18px;height:18px;border-radius:5px}
.stops input{flex:1;min-width:120px;border:0;outline:0;background:none;color:var(--ink);padding:4px}
.ft{display:flex;justify-content:flex-end}""",
    f"""<div class="wrap">
  <details class="adv" open><summary>Advanced settings{ICON['chev']}</summary><div class="body">
    <div class="f"><label for="mx">Maximum answer length <span>tokens</span></label><input id="mx" type="number" min="16" max="8192" step="16"></div>
    <div class="f"><label for="tp">Top p <span class="num" id="tpv"></span></label><input id="tp" type="range" min="0" max="1" step="0.05"></div>
    <div class="f"><label for="si">Stop words <span>press Enter to add</span></label><div class="stops" id="stops"><input id="si" placeholder="Add a word"></div></div>
    <div class="ft"><button class="btn" type="button" id="rs">Reset to defaults</button></div>
  </div></details>
</div>""", """
var DEF={max:1024,top:0.9,stops:['###','User:']},st={};
var mx=document.getElementById('mx'),tp=document.getElementById('tp'),tpv=document.getElementById('tpv'),stops=document.getElementById('stops'),si=document.getElementById('si');
function chips(){[].slice.call(stops.querySelectorAll('.stop')).forEach(function(c){c.remove();});
  st.stops.forEach(function(w,i){var c=document.createElement('span');c.className='stop';c.textContent=w;var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Remove '+w);
    b.innerHTML='"""+ICON['x'].replace('"', '\\"')+"""';b.onclick=function(){st.stops.splice(i,1);chips();si.focus();};c.appendChild(b);stops.insertBefore(c,si);});}
function load(o){st={max:o.max,top:o.top,stops:o.stops.slice()};mx.value=st.max;tp.value=st.top;tpv.textContent=(+st.top).toFixed(2);chips();}
mx.addEventListener('change',function(){st.max=Math.min(8192,Math.max(16,+mx.value||DEF.max));mx.value=st.max;});
tp.addEventListener('input',function(){st.top=+tp.value;tpv.textContent=st.top.toFixed(2);});
si.addEventListener('keydown',function(e){var v=si.value.trim();if(e.key==='Enter'){e.preventDefault();if(v&&st.stops.indexOf(v)<0&&st.stops.length<8){st.stops.push(v);chips();}si.value='';}
  if(e.key==='Backspace'&&!si.value&&st.stops.length){st.stops.pop();chips();}});
document.getElementById('rs').addEventListener('click',function(){load(DEF);});
load(DEF);""")

add(C, "language-picker", "Reply Language Picker",
    "A searchable list to choose the language for answers. Shows each language in its own script and supports right-to-left text.",
    BASE + """
.cb{position:relative;margin-top:12px}
.cb input{width:100%;border:1px solid var(--line);border-radius:12px;padding:10px 38px 10px 12px;background:var(--surface);color:var(--ink)}
.cb input:focus{outline:0;border-color:var(--accent)}
.cb>svg{position:absolute;right:12px;top:14px;color:var(--muted);pointer-events:none}
.lb{position:absolute;left:0;right:0;top:calc(100% + 6px);background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);list-style:none;margin:0;padding:6px;max-height:min(230px,40vh);overflow:auto;z-index:2}
.lb li{display:flex;justify-content:space-between;gap:10px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:14px;color:var(--ink)}
.lb li span{color:var(--muted)}
.lb li[aria-selected=true]{background:var(--accent-soft)}
.lb .none{color:var(--muted);cursor:default}
.picked{margin-top:12px;font-size:14px}""",
    f"""<div class="wrap"><div class="card">
  <h2 id="lbl">Reply language</h2><p class="muted" style="margin:0">The AI will answer in this language.</p>
  <div class="cb"><input id="q" role="combobox" aria-labelledby="lbl" aria-controls="lb" aria-expanded="false" aria-autocomplete="list" placeholder="Search languages" autocomplete="off">{ICON['chev']}
    <ul class="lb" id="lb" role="listbox" aria-labelledby="lbl" hidden></ul></div>
  <p class="picked" id="pk" aria-live="polite"></p>
</div></div>""", """
var L=[['English','English','ltr'],['Spanish','Español','ltr'],['French','Français','ltr'],['German','Deutsch','ltr'],['Portuguese','Português','ltr'],['Arabic','العربية','rtl'],
['Hindi','हिन्दी','ltr'],['Bengali','বাংলা','ltr'],['Chinese','中文','ltr'],['Japanese','日本語','ltr'],['Russian','Русский','ltr'],['Turkish','Türkçe','ltr'],['Urdu','اردو','rtl'],['Indonesian','Bahasa Indonesia','ltr']];
var q=document.getElementById('q'),lb=document.getElementById('lb'),pk=document.getElementById('pk'),shown=[],sel=0,cur=L[0];
function open(v){lb.hidden=!v;q.setAttribute('aria-expanded',v);}
function render(){var t=q.value.trim().toLowerCase();shown=L.filter(function(l){return !t||l[0].toLowerCase().indexOf(t)>-1||l[1].toLowerCase().indexOf(t)>-1;});sel=Math.min(sel,Math.max(0,shown.length-1));lb.innerHTML='';
  if(!shown.length){lb.innerHTML='<li class="none">No language found</li>';q.removeAttribute('aria-activedescendant');}
  shown.forEach(function(l,i){var li=document.createElement('li');li.id='lo'+i;li.setAttribute('role','option');li.setAttribute('aria-selected',i===sel);
    li.innerHTML='<b></b><span></span>';li.querySelector('b').textContent=l[0];var s=li.querySelector('span');s.textContent=l[1];s.dir=l[2];s.lang='';
    li.onmousedown=function(e){e.preventDefault();pick(l);};lb.appendChild(li);});
  if(shown.length)q.setAttribute('aria-activedescendant','lo'+sel);}
function pick(l){cur=l;q.value='';open(false);pk.innerHTML='Answers will be in <b></b> <span></span>';pk.querySelector('b').textContent=l[0];var s=pk.querySelector('span');s.textContent='('+l[1]+')';s.dir=l[2];}
q.addEventListener('focus',function(){render();open(true);});
q.addEventListener('input',function(){sel=0;render();open(true);});
q.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){e.preventDefault();open(true);sel=Math.min(sel+1,shown.length-1);render();}
  else if(e.key==='ArrowUp'){e.preventDefault();sel=Math.max(sel-1,0);render();}
  else if(e.key==='Enter'){e.preventDefault();if(shown[sel])pick(shown[sel]);}else if(e.key==='Escape'){open(false);}});
q.addEventListener('blur',function(){open(false);});
pick(L[0]);""")

add(C, "privacy-controls", "Privacy Controls",
    "Clear privacy settings for an AI app: save chat history, allow chats to improve the model, auto-delete, plus export and delete with a confirm step.",
    BASE + """
.card{padding-bottom:10px}
.acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px;padding-top:14px;border-top:1px solid var(--line)}
.sel{border:1px solid var(--line);border-radius:10px;padding:7px 10px;background:var(--surface);color:var(--ink);font-size:13.5px}
.sel:disabled{opacity:.5}
dialog{border:0;border-radius:16px;padding:22px;width:min(92vw,400px);background:var(--surface);color:var(--text);box-shadow:0 30px 80px -20px rgba(0,0,0,.5)}
dialog::backdrop{background:rgba(10,10,20,.45)}
dialog h2{margin:0 0 6px;font-size:17px;color:var(--ink)}dialog p{margin:0 0 16px;font-size:14px}
dialog .f{display:flex;justify-content:flex-end;gap:8px}
.btn.del{background:var(--bad);border-color:var(--bad);color:#fff}""",
    """<div class="wrap"><div class="card">
  <h2>Privacy</h2><p class="muted" style="margin:0 0 6px">You are in control of your data.</p>
  <div class="row"><div><b id="h1">Save chat history</b><small>Keep your chats so you can come back to them.</small></div><button class="tg" type="button" role="switch" aria-checked="true" aria-labelledby="h1" id="hist"></button></div>
  <div class="row"><div><b id="h2">Help improve the model</b><small>Allow your chats to be used for training. Off by default.</small></div><button class="tg" type="button" role="switch" aria-checked="false" aria-labelledby="h2"></button></div>
  <div class="row"><div><b><label for="ad">Delete chats automatically</label></b><small>Old chats are removed after this time.</small></div><select class="sel" id="ad"><option>Never</option><option selected>After 30 days</option><option>After 90 days</option></select></div>
  <div class="acts"><button class="btn" type="button" id="ex">Export my data</button><button class="btn danger" type="button" id="dl">Delete all chats</button></div>
  <p class="muted" id="st" role="status" aria-live="polite" style="margin:10px 0 0"></p>
</div>
<dialog id="dg" aria-labelledby="dgh"><form method="dialog"><h2 id="dgh">Delete all chats?</h2><p>This removes every chat from your account. You cannot undo this.</p>
  <div class="f"><button class="btn" value="cancel" autofocus>Cancel</button><button class="btn del" value="delete">Delete all</button></div></form></dialog>
</div>""", """
var st=document.getElementById('st'),ad=document.getElementById('ad'),hist=document.getElementById('hist'),dg=document.getElementById('dg');
document.querySelectorAll('.tg').forEach(function(t){t.addEventListener('click',function(){var on=t.getAttribute('aria-checked')!=='true';t.setAttribute('aria-checked',on);
  if(t===hist){ad.disabled=!on;st.textContent=on?'Chat history turned on.':'Chat history turned off. New chats will not be saved.';}});});
document.getElementById('ex').addEventListener('click',function(){var data={exported:new Date().toISOString(),settings:{history:hist.getAttribute('aria-checked'),autoDelete:ad.value}};
  var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));a.download='my-data.json';a.click();st.textContent='Your export has started.';});
document.getElementById('dl').addEventListener('click',function(){dg.showModal();});
dg.addEventListener('close',function(){if(dg.returnValue==='delete')st.textContent='All chats were deleted.';document.getElementById('dl').focus();});""")
