from core import add, ICON

C = "trust"

I = {
    "info": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.5v.5"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17v.5"/></svg>',
    "wifi": '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M2 8.5a15 15 0 0120 0M5 12a10 10 0 0114 0M8.5 15.5a5 5 0 017 0M12 19h.01M3 3l18 18"/></svg>',
    "busy": '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "long": '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 4h10l4 4v12H5z"/><path d="M9 12h6M9 16h4"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "key": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7 14h10"/></svg>',
}

BASE = """a{color:var(--ink);font-weight:600}
.wrap{width:min(100%,600px);display:flex;flex-direction:column;gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:18px 20px}
.card h2{font-size:15.5px;margin:0 0 4px;color:var(--ink)}
.muted{color:var(--muted);font-size:13px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}.btn:disabled{opacity:.45;cursor:not-allowed}
.ib{width:30px;height:30px;display:grid;place-items:center;border:0;background:none;color:var(--muted);border-radius:8px;cursor:pointer}.ib:hover{background:var(--surface-2);color:var(--ink)}
kbd{font:600 12px var(--mono);background:var(--surface-2);border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 7px;color:var(--ink)}
dialog{border:0;border-radius:18px;padding:0;background:var(--surface);color:var(--text);box-shadow:0 30px 80px -20px rgba(0,0,0,.5);width:min(92vw,460px)}
dialog::backdrop{background:rgba(10,10,20,.45)}"""

add(C, "ai-generated-label", "AI-Generated Label",
    "A clear label that marks text or images made by AI. Hover or focus it to see how it was made and what to check.",
    BASE + """
.post{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow)}
.art{height:170px;background:radial-gradient(circle at 30% 30%,#fde68a,transparent 40%),linear-gradient(135deg,#1e3a8a,#7c3aed 60%,#f472b6);position:relative}
.post .in{padding:14px 16px}.post h3{margin:0 0 4px;font-size:15px;color:var(--ink)}.post p{margin:0;font-size:14px}
.lab{position:relative;display:inline-flex}
.lab>button{display:inline-flex;align-items:center;gap:5px;font:600 12px var(--font);border-radius:999px;padding:3px 9px;cursor:help;border:1px solid var(--line);background:var(--surface);color:var(--ink)}
.lab>button b{width:7px;height:7px;border-radius:50%;background:var(--accent)}
.lab.on-img{position:absolute;left:10px;top:10px}.lab.on-img>button{background:rgba(0,0,0,.62);color:#fff;border-color:transparent}
.tip{position:absolute;top:calc(100% + 6px);left:0;width:min(260px,80vw);background:var(--surface);color:var(--text);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);padding:10px 12px;font-size:12.5px;line-height:1.5;z-index:3;display:none}
.lab:hover .tip,.lab:focus-within .tip{display:block}
.tip b{display:block;color:var(--ink);margin-bottom:2px}""",
    f"""<div class="wrap">
  <article class="post">
    <div class="art" role="img" aria-label="Abstract illustration of a sunrise over a city">
      <span class="lab on-img"><button type="button" aria-describedby="t1"><b></b>AI image</button><span class="tip" role="tooltip" id="t1"><b>Made with an image model</b>From the prompt "sunrise over a quiet city, soft colors". It is not a photo of a real place.</span></span>
    </div>
    <div class="in"><h3>Five quiet places to watch the sunrise</h3>
      <p style="margin-bottom:10px">A short guide to early morning walks, with tips on when to arrive and what to bring.</p>
      <span class="lab"><button type="button" aria-describedby="t2"><b></b>AI-assisted text</button><span class="tip" role="tooltip" id="t2"><b>Written with AI help</b>A person reviewed and edited this text. Check opening times before you go.</span></span>
    </div>
  </article>
</div>""")

add(C, "ai-disclaimer-banner", "AI Disclaimer Banner",
    "A short, honest notice that the assistant can make mistakes, with a link to learn more. It can be closed and remembers that choice.",
    BASE + """
.ban{display:flex;gap:12px;align-items:flex-start;background:var(--surface-2);border:1px solid var(--line);border-radius:12px;padding:11px 12px 11px 14px;font-size:14px;color:var(--text)}
.ban svg{color:var(--accent);flex:none;margin-top:2px}.ban p{margin:0;flex:1}.ban a{color:var(--ink);font-weight:600}
.foot{text-align:center;font-size:12px;color:var(--muted);margin:0}
.pb{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:12px 14px;color:var(--muted);box-shadow:var(--shadow)}""",
    f"""<div class="wrap">
  <div class="ban" id="ban" role="note"><span>{I['info']}</span><p>The assistant can make mistakes. Check important information, like dates, prices and medical or legal advice. <a href="#">How we use AI</a></p><button class="ib" id="x" type="button" aria-label="Close notice">{ICON['x']}</button></div>
  <div class="pb">Ask anything</div>
  <p class="foot">Answers are generated by AI and may be inaccurate.</p>
  <button class="btn" id="again" type="button" style="align-self:center" hidden>Show the notice again</button>
</div>""", """
var ban=document.getElementById('ban'),again=document.getElementById('again'),KEY='ai-notice-closed',wasClosed=false;
// Remember the choice for this visit. Use localStorage in your app to keep it longer.
try{wasClosed=sessionStorage.getItem(KEY)==='1';}catch(e){}
function show(v){ban.hidden=!v;again.hidden=v;}
document.getElementById('x').addEventListener('click',function(){show(false);try{sessionStorage.setItem(KEY,'1');}catch(e){}again.focus();});
again.addEventListener('click',function(){show(true);try{sessionStorage.removeItem(KEY);}catch(e){}});
show(!wasClosed);""")

add(C, "onboarding-tour", "Onboarding Tour",
    "A step by step tour that points at parts of the app with short tips. People can go back, skip, or use the arrow keys.",
    BASE + """
.app{width:min(100%,640px);position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:visible}
.bar{display:flex;align-items:center;gap:10px;padding:10px 12px;border-bottom:1px solid var(--line)}
.bar b{color:var(--ink);font-size:14px;flex:1}.chip{font-size:12.5px;border:1px solid var(--line);border-radius:999px;padding:4px 10px;color:var(--ink)}
.body{height:150px;padding:14px;color:var(--muted);font-size:14px}
.pb{margin:0 12px 12px;border:1px solid var(--line);border-radius:12px;padding:10px 12px;color:var(--muted);font-size:14px}
[data-tour]{position:relative;border-radius:10px;transition:box-shadow .2s}
[data-tour].hl{box-shadow:0 0 0 3px var(--accent),0 0 0 8px color-mix(in srgb,var(--accent) 22%,transparent);z-index:2}
.pop{position:absolute;width:min(280px,86vw);background:var(--ink);color:var(--bg);border-radius:14px;padding:14px 16px;box-shadow:var(--shadow);z-index:5}
.pop h3{margin:0 0 4px;font-size:15px;color:inherit}.pop p{margin:0 0 12px;font-size:13.5px;opacity:.9}
.pop .row{display:flex;align-items:center;gap:8px}.pop .dots{display:flex;gap:5px;flex:1}.pop .dots i{width:7px;height:7px;border-radius:50%;background:currentColor;opacity:.3}.pop .dots i.on{opacity:1}
.pop button{border:0;border-radius:8px;padding:6px 11px;font:600 13px var(--font);cursor:pointer}
.pop .nx{background:var(--bg);color:var(--ink)}.pop .bk,.pop .sk{background:transparent;color:inherit;opacity:.8}
.start{align-self:center}""",
    """<div class="wrap" style="width:min(100%,640px)">
  <div class="app" id="app">
    <div class="bar"><b data-tour="1">New chat</b><span class="chip" data-tour="2">Balanced</span></div>
    <div class="body" data-tour="3">Your conversation will appear here.</div>
    <div class="pb" data-tour="4">Ask anything</div>
    <div class="pop" id="pop" role="dialog" aria-labelledby="ph" hidden></div>
  </div>
  <button class="btn start" id="start" type="button">Start the tour</button>
</div>""", """
var STEPS=[['Start a new chat','Every new chat starts fresh. Old chats stay in your history.'],['Pick a mode','Balanced works for most tasks. Choose Deep thinking for hard problems.'],
['Read the answer here','Answers appear in this area. You can copy, rate or ask for a new version.'],['Ask your question','Type here and press Enter. Shift and Enter adds a new line.']];
var app=document.getElementById('app'),pop=document.getElementById('pop'),start=document.getElementById('start'),i=0;
function place(el){var a=app.getBoundingClientRect(),r=el.getBoundingClientRect(),top=r.bottom-a.top+12,left=Math.max(0,Math.min(r.left-a.left,a.width-pop.offsetWidth));
  if(top+pop.offsetHeight>a.height+140)top=r.top-a.top-pop.offsetHeight-12;pop.style.top=top+'px';pop.style.left=left+'px';}
function show(k){i=k;document.querySelectorAll('[data-tour]').forEach(function(x){x.classList.toggle('hl',+x.dataset.tour===k+1);});var el=document.querySelector('[data-tour="'+(k+1)+'"]');
  pop.innerHTML='<h3 id="ph"></h3><p></p><div class="row"><span class="dots" aria-label="Step '+(k+1)+' of '+STEPS.length+'">'+STEPS.map(function(_,j){return '<i class="'+(j===k?'on':'')+'"></i>';}).join('')+'</span>'
    +(k>0?'<button class="bk" type="button">Back</button>':'<button class="sk" type="button">Skip</button>')+'<button class="nx" type="button">'+(k===STEPS.length-1?'Done':'Next')+'</button></div>';
  pop.querySelector('h3').textContent=STEPS[k][0];pop.querySelector('p').textContent=STEPS[k][1];pop.hidden=false;place(el);pop.querySelector('.nx').focus();
  pop.querySelector('.nx').onclick=function(){k===STEPS.length-1?end():show(k+1);};var b=pop.querySelector('.bk,.sk');b.onclick=function(){b.className==='bk'?show(k-1):end();};}
function end(){pop.hidden=true;document.querySelectorAll('.hl').forEach(function(x){x.classList.remove('hl');});start.textContent='Take the tour again';start.focus();}
pop.addEventListener('keydown',function(e){if(e.key==='Escape')end();if(e.key==='ArrowRight'&&i<STEPS.length-1)show(i+1);if(e.key==='ArrowLeft'&&i>0)show(i-1);});
start.addEventListener('click',function(){show(0);});
window.addEventListener('resize',function(){if(!pop.hidden)place(document.querySelector('[data-tour="'+(i+1)+'"]'));});""")

add(C, "prompt-tips", "Prompt Tips Card",
    "Tips for writing better prompts, each with a weak and a stronger example side by side. Flip through them with the arrows.",
    BASE + """
.top{display:flex;justify-content:space-between;align-items:center;gap:10px}
.nav{display:flex;align-items:center;gap:4px;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.tip h3{margin:14px 0 10px;font-size:17px;color:var(--ink)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ex{border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.5;border:1px solid var(--line)}
.ex small{display:block;font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.ex.weak{background:var(--surface-2)}.ex.weak small{color:var(--muted)}
.ex.good{background:color-mix(in srgb,var(--good) 8%,var(--surface));border-color:color-mix(in srgb,var(--good) 35%,var(--line))}.ex.good small{color:var(--good)}
.use{margin-top:12px}
@media(max-width:520px){.pair{grid-template-columns:1fr}}""",
    f"""<div class="wrap"><div class="card">
  <div class="top"><h2>Write better prompts</h2><div class="nav"><button class="ib" id="pv" type="button" aria-label="Previous tip">&#8249;</button><span id="pos" aria-live="polite">1 / 4</span><button class="ib" id="nx" type="button" aria-label="Next tip">&#8250;</button></div></div>
  <div class="tip" id="tip"></div>
  <button class="btn use" id="use" type="button">Try the stronger prompt</button>
  <p class="muted" id="st" role="status" aria-live="polite" style="margin:8px 0 0"></p>
</div></div>""", """
var T=[['Say who it is for','Explain photosynthesis.','Explain photosynthesis to a 10 year old in 3 short sentences.'],
['Give the format you want','Compare these two phones.','Compare these two phones in a table with price, battery and camera.'],
['Share the context','Write an email to my landlord.','Write a polite email to my landlord asking to fix the kitchen heater this week.'],
['Ask for one step at a time','Plan my wedding.','List the first 5 things to decide when planning a small wedding for 40 people.']];
var i=0,tip=document.getElementById('tip'),pos=document.getElementById('pos');
function show(){var t=T[i];tip.innerHTML='<h3></h3><div class="pair"><div class="ex weak"><small>Weak</small><span></span></div><div class="ex good"><small>Stronger</small><span></span></div></div>';
  tip.querySelector('h3').textContent=t[0];var s=tip.querySelectorAll('.ex span');s[0].textContent=t[1];s[1].textContent=t[2];pos.textContent=(i+1)+' / '+T.length;}
document.getElementById('pv').addEventListener('click',function(){i=(i-1+T.length)%T.length;show();});
document.getElementById('nx').addEventListener('click',function(){i=(i+1)%T.length;show();});
document.getElementById('use').addEventListener('click',function(){document.getElementById('st').textContent='Added to the prompt box: "'+T[i][2]+'"';});
show();""")

add(C, "keyboard-shortcuts", "Keyboard Shortcuts Panel",
    "A panel of keyboard shortcuts that opens with the question mark key, with a search box and keys grouped by task.",
    BASE + """
.hint{text-align:center;color:var(--muted);font-size:14px;margin:0}
dialog{width:min(92vw,520px)}
.hd{display:flex;align-items:center;gap:10px;padding:16px 18px 10px}.hd h2{margin:0;font-size:17px;color:var(--ink);flex:1}
.srch{margin:0 18px 8px;width:calc(100% - 36px);border:1px solid var(--line);border-radius:10px;padding:8px 11px;background:var(--surface);color:var(--ink);font-size:14px}
.srch:focus{outline:0;border-color:var(--accent)}
.list{max-height:min(360px,60vh);overflow-y:auto;padding:0 18px 16px}
.list h3{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:12px 0 6px}
.list dl{margin:0}.list .r{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:7px 0;border-bottom:1px solid var(--line);font-size:14px}
.list dt{color:var(--text)}.list dd{margin:0;display:flex;gap:4px;flex:none}
.none{color:var(--muted);font-size:14px;padding:14px 0}""",
    f"""<p class="hint">Press <kbd>?</kbd> to see keyboard shortcuts, or <button class="btn" id="open" type="button" style="margin-left:6px">{I['key']}Show shortcuts</button></p>
<dialog id="dlg" aria-labelledby="kh"><div class="hd"><h2 id="kh">Keyboard shortcuts</h2><button class="ib" id="x" type="button" aria-label="Close">{ICON['x']}</button></div>
  <label class="sr" for="q">Search shortcuts</label><input class="srch" id="q" type="search" placeholder="Search shortcuts" autocomplete="off">
  <div class="list" id="list"></div></dialog>""", """
var mac=/Mac|iPhone|iPad/.test(navigator.platform),M=mac?'Cmd':'Ctrl';
var G=[['Chat',[['Send message',['Enter']],['New line',['Shift','Enter']],['Stop the answer',['Esc']],['Edit last message',['Up']]]],
['Navigation',[['New chat',[M,'Shift','O']],['Search chats',[M,'K']],['Toggle sidebar',[M,'B']]]],
['Answers',[['Copy last answer',[M,'Shift','C']],['Read aloud',[M,'Shift','R']],['Show shortcuts',['?']]]]];
var dlg=document.getElementById('dlg'),q=document.getElementById('q'),list=document.getElementById('list');
function render(){var t=q.value.trim().toLowerCase(),html='';G.forEach(function(g){var rows=g[1].filter(function(r){return !t||r[0].toLowerCase().indexOf(t)>-1||r[1].join(' ').toLowerCase().indexOf(t)>-1;});
  if(!rows.length)return;html+='<h3>'+g[0]+'</h3><dl>'+rows.map(function(r){return '<div class="r"><dt>'+r[0]+'</dt><dd>'+r[1].map(function(k){return '<kbd>'+k+'</kbd>';}).join('')+'</dd></div>';}).join('')+'</dl>';});
  list.innerHTML=html||'<p class="none">No shortcut matches your search.</p>';}
function open(){q.value='';render();dlg.showModal();q.focus();}
document.getElementById('open').addEventListener('click',open);document.getElementById('x').addEventListener('click',function(){dlg.close();});
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close();});q.addEventListener('input',render);
document.addEventListener('keydown',function(e){var typing=/input|textarea|select/i.test(e.target.tagName)||e.target.isContentEditable;if(e.key==='?'&&!typing&&!dlg.open){e.preventDefault();open();}});""")

add(C, "error-states", "AI Error States",
    "Friendly error screens for common AI problems: no internet, the service is busy, and a message that is too long. Each says what to do next.",
    BASE + """
.tabs{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}
.tabs button{border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:5px 12px;font-size:13px;cursor:pointer}
.tabs button[aria-selected=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.st{text-align:center;padding:26px 22px}
.st .ic{width:60px;height:60px;border-radius:50%;margin:0 auto 12px;display:grid;place-items:center;background:var(--surface-2);color:var(--ink)}
.st h2{font-size:18px}.st p{margin:6px auto 16px;max-width:380px;font-size:14px}
.st .acts{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.spin{width:14px;height:14px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--accent);animation:sp .8s linear infinite}@keyframes sp{to{transform:rotate(360deg)}}""",
    """<div class="wrap">
  <div class="tabs" role="tablist" aria-label="Error type"><button role="tab" aria-selected="true" data-k="offline">Offline</button><button role="tab" aria-selected="false" data-k="busy">Service busy</button><button role="tab" aria-selected="false" data-k="long">Message too long</button></div>
  <div class="card st" id="st" role="tabpanel" aria-live="polite"></div>
</div>""", """
var S={offline:['""" + I['wifi'].replace("'", "\\'") + """','You are offline','Your message is saved. It will send as soon as you are back online.','Try again','View saved message'],
busy:['""" + I['busy'].replace("'", "\\'") + """','The service is busy right now','Many people are using the assistant. Please wait a moment and try again.','Try again','Check service status'],
long:['""" + I['long'].replace("'", "\\'") + """','Your message is too long','Your message is about 14,000 words. Shorten it, or split it into parts and send them one by one.','Shorten it for me','Split into parts']};
var st=document.getElementById('st'),tabs=[].slice.call(document.querySelectorAll('.tabs button'));
function show(k){var s=S[k];tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.k===k);});
  st.innerHTML='<div class="ic">'+s[0]+'</div><h2></h2><p class="muted"></p><div class="acts"><button class="btn pri" type="button" id="a1"></button><button class="btn" type="button"></button></div>';
  st.querySelector('h2').textContent=s[1];st.querySelector('p').textContent=s[2];var b=st.querySelectorAll('button');b[0].textContent=s[3];b[1].textContent=s[4];
  b[0].onclick=function(){b[0].disabled=true;b[0].innerHTML='<span class="spin" aria-hidden="true"></span>Working';setTimeout(function(){st.innerHTML='<h2>All set</h2><p class="muted">That worked. You can keep chatting.</p>';},1100);};}
tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.k);});});show('offline');""")

add(C, "content-warning", "Sensitive Content Notice",
    "Hides an answer about a sensitive topic behind a calm notice, with a clear choice to show it and a link to real help.",
    BASE + """
.bubble{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:4px 16px 16px 16px;box-shadow:var(--shadow);overflow:hidden;min-height:210px}
.txt{padding:14px 16px;line-height:1.6;filter:blur(7px);user-select:none;transition:filter .25s}
.bubble.open .txt{filter:none;user-select:auto}
.cover{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;padding:16px;background:color-mix(in srgb,var(--surface) 70%,transparent)}
.bubble.open .cover{display:none}
.cover b{color:var(--ink);font-size:15px}.cover p{margin:0 0 4px;font-size:13.5px;max-width:360px}
.cover svg{color:var(--warn)}
.help{font-size:13px;margin:0}.help a{color:var(--ink);font-weight:600}""",
    f"""<div class="wrap">
  <div class="bubble" id="b">
    <div class="txt" id="txt" aria-hidden="true">Grief can show up as tiredness, trouble sleeping and a hard time focusing. These are common reactions. Small routines, like a short daily walk and regular meals, can help. Talking with someone you trust, or a counselor, can make a real difference.</div>
    <div class="cover" id="cover"><span>{I['alert']}</span><b>This answer talks about grief and loss</b><p class="muted">You can choose whether to read it now.</p><button class="btn pri" id="show" type="button">{I['eye']}Show the answer</button></div>
  </div>
  <p class="help muted">If you are struggling, you can reach a local support line any time. <a href="#">Find help near you</a></p>
  <button class="btn" id="hide" type="button" style="align-self:center" hidden>Hide it again</button>
</div>""", """
var b=document.getElementById('b'),txt=document.getElementById('txt'),hide=document.getElementById('hide');
document.getElementById('show').addEventListener('click',function(){b.classList.add('open');txt.setAttribute('aria-hidden','false');hide.hidden=false;txt.setAttribute('tabindex','-1');txt.focus();});
hide.addEventListener('click',function(){b.classList.remove('open');txt.setAttribute('aria-hidden','true');hide.hidden=true;document.getElementById('show').focus();});""")

add(C, "fact-check-panel", "Fact Check Panel",
    "Shows how each claim in an answer was checked: supported by sources, not found, or conflicting. Open a claim to see the sources.",
    BASE + """
.sum{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0 12px}
.pill{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:600;border-radius:999px;padding:3px 10px;border:1px solid var(--line);color:var(--ink)}
.pill i{width:8px;height:8px;border-radius:50%}
.ok i{background:var(--good)}.no i{background:var(--muted)}.mix i{background:var(--warn)}
details{border:1px solid var(--line);border-radius:12px;padding:0;margin-bottom:8px;background:var(--surface)}
details summary{list-style:none;cursor:pointer;display:flex;gap:10px;align-items:flex-start;padding:10px 12px;font-size:14px;color:var(--ink)}
details summary::-webkit-details-marker{display:none}
details summary .pill{margin-left:auto;flex:none}
details ul{margin:0;padding:0 12px 12px 30px;font-size:13px;color:var(--text)}details li{margin:3px 0}""",
    """<div class="wrap"><div class="card">
  <h2>How this answer was checked</h2>
  <div class="sum" id="sum"></div>
  <div id="claims"></div>
  <p class="muted" style="margin:6px 0 0">Checks look for sources that say the same thing. They do not prove a claim is true.</p>
</div></div>""", """
var CL=[['The Eiffel Tower is about 330 metres tall.','ok','Supported',['Official tower website','City tourism guide','Encyclopedia entry']],
['It was finished in 1889.','ok','Supported',['Official tower website','History magazine article']],
['It gets about 7 million visitors a year.','mix','Sources differ',['One source says 6.2 million (2023)','Another says 7 million (2019)']],
['It is repainted every 5 years.','no','Not found',['No source found. The official site says about every 7 years.']]];
var LAB={ok:'Supported',mix:'Sources differ',no:'Not found'},sum=document.getElementById('sum'),claims=document.getElementById('claims');
var WORD={ok:['supported','supported'],mix:['source differs','sources differ'],no:['not found','not found']};
['ok','mix','no'].forEach(function(k){var n=CL.filter(function(c){return c[1]===k;}).length;sum.insertAdjacentHTML('beforeend','<span class="pill '+k+'"><i></i>'+n+' '+WORD[k][n===1?0:1]+'</span>');});
CL.forEach(function(c){var d=document.createElement('details');d.innerHTML='<summary><span></span><span class="pill '+c[1]+'"><i></i>'+c[2]+'</span></summary><ul></ul>';
  d.querySelector('summary span').textContent=c[0];c[3].forEach(function(s){var li=document.createElement('li');li.textContent=s;d.querySelector('ul').appendChild(li);});claims.appendChild(d);});""")

add(C, "whats-new-dialog", "What's New Dialog",
    "A short dialog that introduces new features, with a few slides, Beta labels and a way to send feedback. It shows once per version.",
    BASE + """
.slide{padding:22px 22px 8px}
.pic{height:140px;border-radius:14px;margin-bottom:16px;display:grid;place-items:center;color:#fff;font-weight:800;font-size:22px}
.slide h2{margin:0 0 6px;font-size:18px;color:var(--ink);display:flex;align-items:center;gap:8px}
.beta{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;border:1px solid var(--accent);color:var(--accent);border-radius:999px;padding:1px 8px}
.slide p{margin:0;font-size:14px}
.ft{display:flex;align-items:center;gap:8px;padding:14px 22px 18px}
.dots{display:flex;gap:6px;flex:1}.dots i{width:8px;height:8px;border-radius:50%;background:var(--line)}.dots i.on{background:var(--accent)}
.fb{font-size:13px;color:var(--muted);padding:0 22px 16px;margin:0}.fb a{color:var(--ink);font-weight:600}""",
    """<button class="btn" id="open" type="button">See what is new</button>
<dialog id="dlg" aria-labelledby="wh"><div id="slide" class="slide" aria-live="polite"></div>
  <div class="ft"><span class="dots" id="dots" aria-hidden="true"></span><button class="btn" id="bk" type="button">Back</button><button class="btn pri" id="nx" type="button">Next</button></div>
  <p class="fb">Have thoughts on these features? <a href="#">Send feedback</a></p></dialog>""", """
var V='2.4',S=[['Voice chats','Talk to the assistant hands free, with live captions.',false,'#4f46e5'],['Projects','Keep chats, files and notes for one goal in a single place.',true,'#0f766e'],['Longer files','Upload documents up to 300 pages and ask questions about them.',false,'#b45309']];
var dlg=document.getElementById('dlg'),slide=document.getElementById('slide'),dots=document.getElementById('dots'),bk=document.getElementById('bk'),nx=document.getElementById('nx'),i=0;
function show(k){i=k;var s=S[k];slide.innerHTML='<div class="pic" aria-hidden="true"></div><h2 id="wh"></h2><p class="muted"></p>';slide.querySelector('.pic').style.background=s[3];slide.querySelector('.pic').textContent=s[0];
  var h=slide.querySelector('h2');h.textContent=s[0];if(s[2])h.insertAdjacentHTML('beforeend','<span class="beta">Beta</span>');slide.querySelector('p').textContent=s[1];
  dots.innerHTML=S.map(function(_,j){return '<i class="'+(j===k?'on':'')+'"></i>';}).join('');bk.disabled=k===0;nx.textContent=k===S.length-1?'Got it':'Next';}
function open(){show(0);dlg.showModal();nx.focus();}
// Show once per version: remember the version you last showed, for example in localStorage.
document.getElementById('open').addEventListener('click',open);
bk.addEventListener('click',function(){if(i>0)show(i-1);});nx.addEventListener('click',function(){if(i<S.length-1)show(i+1);else dlg.close();});
dlg.addEventListener('keydown',function(e){if(e.key==='ArrowRight'&&i<S.length-1)show(i+1);if(e.key==='ArrowLeft'&&i>0)show(i-1);});
dlg.addEventListener('close',function(){document.getElementById('open').focus();});""")

add(C, "first-run-consent", "First Run Consent",
    "A clear welcome step before first use that explains how data is used in plain words. People must agree to the terms, and training is a separate, optional choice.",
    BASE + """
.wrap{width:min(100%,520px)}
.card h2{font-size:19px;margin-bottom:6px}
.pts{list-style:none;margin:14px 0;padding:0;display:flex;flex-direction:column;gap:10px}
.pts li{display:flex;gap:10px;font-size:14px;line-height:1.5}
.pts li span:first-child{width:24px;height:24px;border-radius:50%;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;flex:none;font-weight:700;font-size:12px}
.chk{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line);border-radius:12px;margin-bottom:8px;cursor:pointer;font-size:14px}
.chk input{margin-top:3px;accent-color:var(--accent);width:16px;height:16px;flex:none}
.chk small{display:block;color:var(--muted);font-size:12.5px}
.ft{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:14px;flex-wrap:wrap}
.done{text-align:center}.done h2{color:var(--ink)}""",
    """<div class="wrap"><form class="card" id="f">
  <h2>Before you start</h2><p class="muted" style="margin:0">A quick summary of how the assistant works with your data.</p>
  <ul class="pts">
    <li><span>1</span><span>Your chats are saved to your account so you can come back to them. You can delete them at any time.</span></li>
    <li><span>2</span><span>The assistant can make mistakes. Check important facts before you rely on them.</span></li>
    <li><span>3</span><span>Do not share passwords, bank details or other private information in chats.</span></li>
  </ul>
  <label class="chk"><input type="checkbox" id="terms" required><span>I agree to the <a href="#">Terms</a> and <a href="#">Privacy Policy</a><small>Required to use the assistant.</small></span></label>
  <label class="chk"><input type="checkbox" id="train"><span>Allow my chats to help improve the model<small>Optional. You can change this later in settings.</small></span></label>
  <div class="ft"><span class="muted" id="hint" aria-live="polite">Please agree to the terms to continue.</span><button class="btn pri" id="go" type="submit" disabled>Continue</button></div>
</form></div>""", """
var f=document.getElementById('f'),terms=document.getElementById('terms'),train=document.getElementById('train'),go=document.getElementById('go'),hint=document.getElementById('hint');
terms.addEventListener('change',function(){go.disabled=!terms.checked;hint.textContent=terms.checked?'Ready when you are.':'Please agree to the terms to continue.';});
f.addEventListener('submit',function(e){e.preventDefault();if(!terms.checked)return;
  // Save { terms: true, training: train.checked } with the date and your policy version.
  f.innerHTML='<div class="done"><h2>You are all set</h2><p class="muted">Model training is <b>'+(train.checked?'on':'off')+'</b>. You can change it any time in settings.</p></div>';});""")
