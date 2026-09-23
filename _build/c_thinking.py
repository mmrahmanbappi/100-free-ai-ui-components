from core import add, ICON

C = "thinking"

# Shared look: an assistant row with an avatar and a bubble, plus a small replay button
BASE = """.wrap{width:min(100%,640px);display:flex;flex-direction:column;gap:14px}
.ai{display:flex;gap:12px;align-items:flex-start}
.av{width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.bubble{background:var(--surface);border:1px solid var(--line);border-radius:4px 16px 16px 16px;padding:12px 15px;box-shadow:var(--shadow);color:var(--text);min-width:0;max-width:100%}
.meta{font-size:12px;color:var(--muted)}
.replay{align-self:center;border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:6px 14px;font-size:13px;cursor:pointer}
.replay:hover{border-color:var(--accent);color:var(--ink)}"""

AV = f'<div class="av" aria-hidden="true">{ICON["spark"]}</div>'

add(C, "typing-dots", "Typing Dots",
    "Three bouncing dots inside an answer bubble, the classic sign that the AI is writing a reply.",
    BASE + """
.dots{display:flex;gap:5px;padding:4px 2px}
.dots i{width:8px;height:8px;border-radius:50%;background:var(--muted);animation:b 1.2s ease-in-out infinite}
.dots i:nth-child(2){animation-delay:.15s}.dots i:nth-child(3){animation-delay:.3s}
@keyframes b{0%,60%,100%{transform:translateY(0);opacity:.45}30%{transform:translateY(-6px);opacity:1}}
.done{animation:fade .25s ease}@keyframes fade{from{opacity:0}}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble" id="b" role="status" aria-live="polite"><span class="sr">The assistant is typing</span><div class="dots" aria-hidden="true"><i></i><i></i><i></i></div></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var b=document.getElementById('b'),t=null,DOTS=b.innerHTML;
function run(){clearTimeout(t);b.innerHTML=DOTS;t=setTimeout(function(){b.innerHTML='<div class="done">Sure. Here is a short plan you can follow this week.</div>';},2600);}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "thinking-shimmer", "Thinking Shimmer",
    "A soft light moves across the word Thinking while the AI works, then it changes to how long the thinking took.",
    BASE + """
.shim{font-weight:600;background:linear-gradient(90deg,var(--muted) 0%,var(--muted) 40%,var(--ink) 50%,var(--muted) 60%,var(--muted) 100%);background-size:250% 100%;
-webkit-background-clip:text;background-clip:text;color:transparent;animation:s 1.6s linear infinite}
@keyframes s{from{background-position:100% 0}to{background-position:-50% 0}}
.took{color:var(--muted);font-size:14px;display:flex;align-items:center;gap:6px}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble" id="b" role="status" aria-live="polite"></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var b=document.getElementById('b'),t=null,start=0;
function run(){clearTimeout(t);start=Date.now();b.innerHTML='<span class="shim">Thinking</span>';
  t=setTimeout(function(){var s=Math.round((Date.now()-start)/1000);b.innerHTML='<div class="took">"""+ICON['check']+"""Thought for '+s+' seconds</div><div style="margin-top:8px">The best time to post is Tuesday morning, based on your past results.</div>';},3200);}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "streaming-text", "Streaming Text",
    "The answer appears word by word with a blinking cursor, the way most AI chat apps show a reply as it is written.",
    BASE + """
.out{white-space:pre-wrap;line-height:1.65}
.cur{display:inline-block;width:8px;height:1.1em;background:var(--accent);vertical-align:text-bottom;margin-left:2px;border-radius:2px;animation:bl 1s steps(1) infinite}
@keyframes bl{50%{opacity:0}}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble"><span class="out" id="o" aria-live="polite"></span><span class="cur" id="c" aria-hidden="true"></span></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var TEXT="Good question. A budget works best when it is simple. Start with three groups: needs, wants and savings. Put fixed bills in needs, fun spending in wants, and move savings on payday so it happens first.";
var o=document.getElementById('o'),c=document.getElementById('c'),t=null;
function run(){clearTimeout(t);o.textContent='';c.hidden=false;var words=TEXT.split(' '),i=0;
  (function next(){if(i>=words.length){c.hidden=true;return;}o.textContent+=(i?' ':'')+words[i++];t=setTimeout(next,45+Math.random()*70);})();}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "reasoning-panel", "Reasoning Panel",
    "A panel that shows each thinking step while the AI works, then folds itself away with a summary you can open again.",
    BASE + """
.rp{border:1px solid var(--line);border-radius:12px;background:var(--surface-2);margin-bottom:10px;overflow:hidden}
.rp summary{list-style:none;display:flex;align-items:center;gap:8px;padding:9px 12px;cursor:pointer;font-size:14px;color:var(--muted);font-weight:600}
.rp summary::-webkit-details-marker{display:none}
.rp summary .ch{margin-left:auto;transition:transform .2s}.rp[open] summary .ch{transform:rotate(180deg)}
.rp ol{margin:0;padding:0 14px 12px 32px;font-size:14px;color:var(--text)}
.rp li{margin:4px 0;animation:in .25s ease}@keyframes in{from{opacity:0;transform:translateY(4px)}}
.live{background:linear-gradient(90deg,var(--muted),var(--ink),var(--muted));background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:s 1.5s linear infinite}
@keyframes s{from{background-position:100% 0}to{background-position:-100% 0}}
.ans{animation:in .3s ease}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble" style="flex:1">
    <details class="rp" id="rp" open><summary><span id="lab" class="live">Thinking</span><span class="ch">{ICON['chev']}</span></summary><ol id="steps" aria-live="polite"></ol></details>
    <div id="ans"></div>
  </div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var STEPS=['Reading the question about moving the meeting','Checking which days both people are free','Thursday afternoon works for everyone','Writing a short, polite message'];
var rp=document.getElementById('rp'),lab=document.getElementById('lab'),steps=document.getElementById('steps'),ans=document.getElementById('ans'),timers=[];
function run(){timers.forEach(clearTimeout);timers=[];steps.innerHTML='';ans.innerHTML='';rp.open=true;lab.className='live';lab.textContent='Thinking';var start=Date.now();
  STEPS.forEach(function(s,i){timers.push(setTimeout(function(){var li=document.createElement('li');li.textContent=s;steps.appendChild(li);},700*(i+1)));});
  timers.push(setTimeout(function(){rp.open=false;lab.className='';lab.textContent='Thought for '+Math.round((Date.now()-start)/1000)+' seconds';
    ans.innerHTML='<div class="ans">Here is a message you can send: "Hi Sam, could we move our meeting to Thursday at 3pm? Thanks!"</div>';},700*(STEPS.length+1)+300));}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "agent-progress-steps", "Agent Progress Steps",
    "A checklist of what an AI agent is doing right now. Each step shows a spinner while it runs and a tick when it is done.",
    BASE + """
.card{width:100%;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px 18px}
.card h2{font-size:15px;margin:0 0 12px;color:var(--ink)}
.steps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.steps li{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--muted)}
.st{width:20px;height:20px;border-radius:50%;border:2px solid var(--line);display:grid;place-items:center;flex:none}
li.run{color:var(--ink);font-weight:600}li.run .st{border-color:var(--accent);border-right-color:transparent;animation:spin .8s linear infinite}
li.done{color:var(--text)}li.done .st{background:var(--good);border-color:var(--good);color:#fff}
@keyframes spin{to{transform:rotate(360deg)}}
.bar{height:6px;background:var(--surface-2);border-radius:99px;margin-top:14px;overflow:hidden}.bar i{display:block;height:100%;width:0;background:var(--accent);transition:width .4s}""",
    f"""<div class="wrap">
  <div class="card"><h2 id="h" aria-live="polite">Working on your report</h2>
    <ol class="steps" id="s">
      <li><span class="st"></span>Reading 3 uploaded files</li>
      <li><span class="st"></span>Finding sales numbers for each month</li>
      <li><span class="st"></span>Building a summary table</li>
      <li><span class="st"></span>Writing the key points</li>
    </ol><div class="bar" aria-hidden="true"><i id="bar"></i></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var li=[].slice.call(document.querySelectorAll('#s li')),bar=document.getElementById('bar'),h=document.getElementById('h'),timers=[];
function mark(i){li.forEach(function(x,j){x.className=j<i?'done':j===i?'run':'';x.querySelector('.st').innerHTML=j<i?'"""+ICON['check'].replace("'", "\\'")+"""':'';});bar.style.width=(i/li.length*100)+'%';}
function run(){timers.forEach(clearTimeout);timers=[];h.textContent='Working on your report';mark(0);
  li.forEach(function(_,i){timers.push(setTimeout(function(){mark(i+1);if(i===li.length-1)h.textContent='Your report is ready';},1100*(i+1)));});}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "skeleton-message", "Skeleton Message",
    "Grey placeholder lines with a moving shine that hold the space of the answer while it loads, so the page does not jump.",
    BASE + """
.sk{display:flex;flex-direction:column;gap:9px;width:100%}
.sk i{height:12px;border-radius:6px;background:linear-gradient(90deg,var(--surface-2) 25%,var(--line) 50%,var(--surface-2) 75%);background-size:300% 100%;animation:sh 1.4s ease infinite}
.sk i:nth-child(1){width:92%}.sk i:nth-child(2){width:100%}.sk i:nth-child(3){width:78%}.sk i:nth-child(4){width:55%}
@keyframes sh{from{background-position:100% 0}to{background-position:0 0}}
.bubble{flex:1}.txt{animation:f .3s ease}@keyframes f{from{opacity:0}}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble" id="b" role="status" aria-live="polite"></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var b=document.getElementById('b'),t=null;
function run(){clearTimeout(t);b.innerHTML='<span class="sr">Loading the answer</span><div class="sk" aria-hidden="true"><i></i><i></i><i></i><i></i></div>';
  t=setTimeout(function(){b.innerHTML='<div class="txt">Your trip costs about $640 in total: $380 for the hotel, $160 for food and $100 for trains and museum tickets.</div>';},2600);}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "ai-orb", "AI Orb",
    "A glowing orb that shows what the assistant is doing: resting, listening or thinking. Great for voice and assistant screens.",
    """.wrap{display:flex;flex-direction:column;align-items:center;gap:22px}
.orb{width:150px;height:150px;border-radius:50%;position:relative;background:radial-gradient(circle at 35% 30%,#fff 0,var(--accent) 38%,color-mix(in srgb,var(--accent) 60%,#000) 100%);box-shadow:0 0 60px -10px var(--accent);transition:transform .4s}
.orb::after{content:"";position:absolute;inset:-14px;border-radius:50%;border:2px solid var(--accent);opacity:0}
.orb.idle{animation:breathe 4s ease-in-out infinite}
.orb.listen{animation:breathe 1.2s ease-in-out infinite}.orb.listen::after{animation:ring 1.4s ease-out infinite}
.orb.think{animation:wobble 2.2s ease-in-out infinite;filter:saturate(1.3)}
@keyframes breathe{50%{transform:scale(1.06)}}
@keyframes ring{from{opacity:.7;transform:scale(.95)}to{opacity:0;transform:scale(1.35)}}
@keyframes wobble{0%,100%{border-radius:50%;transform:rotate(0)}25%{border-radius:46% 54% 52% 48%}50%{border-radius:53% 47% 45% 55%;transform:rotate(12deg)}75%{border-radius:48% 52% 55% 45%}}
.lab{font-weight:600;color:var(--ink);min-height:1.5em}
.seg{display:flex;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:4px;gap:4px}
.seg button{border:0;background:none;padding:7px 14px;border-radius:9px;font-size:14px;color:var(--muted);cursor:pointer}
.seg button[aria-pressed=true]{background:var(--accent-soft);color:var(--ink);font-weight:600}""",
    """<div class="wrap">
  <div class="orb idle" id="orb" aria-hidden="true"></div>
  <div class="lab" id="lab" role="status" aria-live="polite">Ready when you are</div>
  <div class="seg" role="group" aria-label="Assistant state">
    <button type="button" data-s="idle" aria-pressed="true">Resting</button>
    <button type="button" data-s="listen" aria-pressed="false">Listening</button>
    <button type="button" data-s="think" aria-pressed="false">Thinking</button>
  </div>
</div>""", """
var orb=document.getElementById('orb'),lab=document.getElementById('lab'),bs=[].slice.call(document.querySelectorAll('.seg button'));
var LAB={idle:'Ready when you are',listen:'Listening...',think:'Thinking about your question'};
// Call setState('idle' | 'listen' | 'think') from your app.
function setState(s){orb.className='orb '+s;lab.textContent=LAB[s];bs.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.s===s);});}
bs.forEach(function(b){b.addEventListener('click',function(){setState(b.dataset.s);});});""")

add(C, "status-spinner", "Spinner with Status Text",
    "A small spinner with a line of text that changes as the work moves forward, so people know the AI has not frozen.",
    BASE + """
.stat{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:10px 18px 10px 12px;box-shadow:var(--shadow);align-self:flex-start;max-width:100%}
.sp{width:22px;height:22px;border-radius:50%;border:3px solid var(--accent-soft);border-top-color:var(--accent);animation:spin .75s linear infinite;flex:none}
@keyframes spin{to{transform:rotate(360deg)}}
.st{font-size:14px;color:var(--ink);transition:opacity .25s}.st.out{opacity:0}
.stat.ok .sp{animation:none;border-color:var(--good);background:var(--good)}
.el{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums;margin-left:4px}""",
    f"""<div class="wrap">
  <div class="stat" id="box"><span class="sp" aria-hidden="true"></span><span class="st" id="st" role="status" aria-live="polite">Starting</span><span class="el" id="el">0s</span></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var MSGS=['Reading your document','Finding the main ideas','Checking the numbers','Writing the summary','Done'];
var st=document.getElementById('st'),el=document.getElementById('el'),box=document.getElementById('box'),timers=[],tick=null;
function say(m){st.classList.add('out');setTimeout(function(){st.textContent=m;st.classList.remove('out');},250);}
function run(){timers.forEach(clearTimeout);clearInterval(tick);timers=[];box.classList.remove('ok');st.textContent=MSGS[0];var start=Date.now();
  tick=setInterval(function(){el.textContent=Math.floor((Date.now()-start)/1000)+'s';},250);
  MSGS.slice(1).forEach(function(m,i){timers.push(setTimeout(function(){say(m);if(m==='Done'){box.classList.add('ok');clearInterval(tick);}},1300*(i+1)));});}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "tool-call-indicator", "Web Search Indicator",
    "Shows that the AI is searching the web, with sources popping in one by one, then a short summary of how many it found.",
    BASE + """
.tool{display:flex;flex-direction:column;gap:10px;width:100%}
.pill{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;background:var(--surface-2);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13.5px;color:var(--text)}
.pill .sp{width:14px;height:14px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--accent);animation:spin .8s linear infinite}
.pill.ok .sp{animation:none;border-color:var(--good);background:var(--good)}
@keyframes spin{to{transform:rotate(360deg)}}
.srcs{display:flex;flex-wrap:wrap;gap:6px}
.src{display:flex;align-items:center;gap:7px;border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:5px 10px 5px 6px;font-size:13px;animation:pop .25s ease}
.src b{width:18px;height:18px;border-radius:5px;display:grid;place-items:center;color:#fff;font-size:10px}
@keyframes pop{from{opacity:0;transform:scale(.9)}}
.bubble{flex:1}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble"><div class="tool">
    <span class="pill" id="p" role="status" aria-live="polite"><span class="sp" aria-hidden="true"></span><span id="pt">Searching the web</span></span>
    <div class="srcs" id="srcs" aria-label="Sources"></div><div id="ans"></div></div></div></div>
  <button class="replay" id="r" type="button">Run again</button>
</div>""", """
var SRC=[['Weather Service','#2563eb'],['City Guide','#0f766e'],['Travel Forum','#b45309'],['News Daily','#be123c'],['Trip Blog','#7c3aed']];
var p=document.getElementById('p'),pt=document.getElementById('pt'),srcs=document.getElementById('srcs'),ans=document.getElementById('ans'),timers=[];
function run(){timers.forEach(clearTimeout);timers=[];srcs.innerHTML='';ans.textContent='';p.classList.remove('ok');pt.textContent='Searching the web';
  SRC.forEach(function(s,i){timers.push(setTimeout(function(){var d=document.createElement('span');d.className='src';d.innerHTML='<b></b><span></span>';
    d.querySelector('b').style.background=s[1];d.querySelector('b').textContent=s[0][0];d.querySelector('span').textContent=s[0];srcs.appendChild(d);},600*(i+1)));});
  timers.push(setTimeout(function(){p.classList.add('ok');pt.textContent='Searched 5 sources';ans.textContent='Expect light rain on Saturday morning, then clear skies. Pack a thin jacket.';},600*(SRC.length+1)));}
document.getElementById('r').addEventListener('click',run);run();""")

add(C, "stop-generating", "Stop Generating Button",
    "A stop button that appears while the answer is being written. Stopping keeps what was written and offers to continue or try again.",
    BASE + """
.out{white-space:pre-wrap;line-height:1.65}
.cur{display:inline-block;width:7px;height:1.05em;background:var(--accent);vertical-align:text-bottom;margin-left:2px;border-radius:2px;animation:bl 1s steps(1) infinite}
@keyframes bl{50%{opacity:0}}
.note{display:block;margin-top:8px;font-size:12.5px;color:var(--muted)}
.bar{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:8px 16px;font-size:14px;font-weight:600;cursor:pointer;box-shadow:var(--shadow)}
.btn:hover{border-color:var(--accent)}.btn[hidden]{display:none}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="bubble" style="flex:1"><span class="out" id="o" aria-live="polite"></span><span class="cur" id="c" aria-hidden="true"></span><span class="note" id="n" hidden>You stopped this answer.</span></div></div>
  <div class="bar">
    <button class="btn" id="stop" type="button">{ICON['stop']}Stop generating</button>
    <button class="btn" id="cont" type="button" hidden>Continue</button>
    <button class="btn" id="again" type="button" hidden>Try again</button>
  </div>
</div>""", """
var TEXT="Here are five ways to save on groceries. First, plan meals for the week before you shop. Second, buy store brands for basics like rice, flour and pasta. Third, check the reduced shelf in the evening. Fourth, cook bigger batches and freeze portions. Fifth, keep a running list on your phone so you only buy what you need.";
var o=document.getElementById('o'),c=document.getElementById('c'),n=document.getElementById('n'),stopBtn=document.getElementById('stop'),cont=document.getElementById('cont'),again=document.getElementById('again');
var words=TEXT.split(' '),i=0,t=null;
function ui(state){stopBtn.hidden=state!=='run';cont.hidden=state!=='stopped';again.hidden=state==='run';c.hidden=state!=='run';n.hidden=state!=='stopped';}
function step(){if(i>=words.length){ui('done');return;}o.textContent+=(i?' ':'')+words[i++];t=setTimeout(step,55+Math.random()*60);}
function start(reset,byUser){clearTimeout(t);if(reset){o.textContent='';i=0;}ui('run');step();if(byUser)stopBtn.focus();}
stopBtn.addEventListener('click',function(){clearTimeout(t);ui('stopped');cont.focus();});
cont.addEventListener('click',function(){start(false,true);});
again.addEventListener('click',function(){start(true,true);});
start(true);""")
