from core import add, ICON

C = "usage"

BASE = """.wrap{width:min(100%,560px);display:flex;flex-direction:column;gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:18px 20px}
.card h2{font-size:15px;margin:0 0 4px;color:var(--ink)}
.muted{color:var(--muted);font-size:13px}
.num{font-variant-numeric:tabular-nums}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer;text-decoration:none}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.bar{height:8px;border-radius:99px;background:var(--surface-2);overflow:hidden}
.bar i{display:block;height:100%;border-radius:99px;background:var(--accent);transition:width .3s,background .3s}
.ok{--lvl:var(--accent)}.warn{--lvl:var(--warn)}.full{--lvl:var(--bad)}
.tg{width:38px;height:22px;border-radius:99px;background:var(--line);position:relative;flex:none;border:0;cursor:pointer;padding:0}
.tg::after{content:"";position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:#fff;transition:left .15s}
.tg[aria-checked=true]{background:var(--accent)}.tg[aria-checked=true]::after{left:19px}"""

# Shared: number formatting and level class
FMT = """function fmt(n){return n>=1e6?(n/1e6).toFixed(n>=1e7?0:1)+'M':n>=1e3?(n/1e3).toFixed(n>=1e4?0:1)+'k':String(n)}
function level(p){return p>=1?'full':p>=.8?'warn':'ok'}"""

add(C, "token-ring", "Token Ring Meter",
    "A small ring that fills as a chat uses up its token budget. It turns orange near the limit and red when full, with an exact count on hover.",
    BASE + """
.tr{display:flex;align-items:center;gap:16px}
.ring{position:relative;width:64px;height:64px;flex:none}
.ring svg{width:64px;height:64px;transform:rotate(-90deg)}
.ring circle{fill:none;stroke-width:7}
.ring .bg{stroke:var(--surface-2)}.ring .fg{stroke:var(--lvl);stroke-linecap:round;transition:stroke-dashoffset .4s,stroke .3s}
.ring b{position:absolute;inset:0;display:grid;place-items:center;font-size:13px;color:var(--ink)}
.ctl{display:flex;gap:8px;margin-top:14px}""",
    """<div class="wrap"><div class="card">
  <div class="tr ok" id="w"><div class="ring" title="" id="ring"><svg viewBox="0 0 64 64" aria-hidden="true"><circle class="bg" cx="32" cy="32" r="27"/><circle class="fg" id="fg" cx="32" cy="32" r="27"/></svg><b class="num" id="pct">0%</b></div>
    <div><h2>Tokens used in this chat</h2><p class="muted num" id="txt" role="status" aria-live="polite"></p></div></div>
  <div class="ctl"><button class="btn" type="button" id="add">Send a message</button><button class="btn" type="button" id="clr">New chat</button></div>
</div></div>""", FMT + """
var LIMIT=128000,used=38400,fg=document.getElementById('fg'),w=document.getElementById('w'),pct=document.getElementById('pct'),txt=document.getElementById('txt'),ring=document.getElementById('ring'),C=2*Math.PI*27;
fg.style.strokeDasharray=C;
// Call render(tokensUsed) whenever your API reports usage.
function render(n){used=Math.min(n,LIMIT);var p=used/LIMIT;fg.style.strokeDashoffset=C*(1-p);pct.textContent=Math.round(p*100)+'%';w.className='tr '+level(p);
  txt.textContent=fmt(used)+' of '+fmt(LIMIT)+' tokens'+(p>=1?'. Start a new chat to continue.':p>=.8?'. Close to the limit.':'');ring.title=used.toLocaleString()+' of '+LIMIT.toLocaleString()+' tokens';}
document.getElementById('add').addEventListener('click',function(){render(used+Math.round(9000+Math.random()*9000));});
document.getElementById('clr').addEventListener('click',function(){render(0);});
render(used);""")

add(C, "context-window-bar", "Context Window Bar",
    "A bar that shows what fills the AI's memory for this chat: instructions, files, chat history and room left for the reply.",
    BASE + """
.stack{display:flex;height:14px;border-radius:99px;overflow:hidden;background:var(--surface-2);margin:12px 0 10px}
.stack i{display:block;height:100%;transition:width .35s}
.leg{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;font-size:13px;list-style:none;margin:0;padding:0}
.leg li{display:flex;align-items:center;gap:8px;min-width:0}.leg b{margin-left:auto;color:var(--ink);font-weight:600}
.sw{width:10px;height:10px;border-radius:3px;flex:none}
.tip{display:flex;gap:10px;align-items:center;justify-content:space-between;margin-top:14px;padding:10px 12px;border-radius:10px;background:color-mix(in srgb,var(--warn) 10%,var(--surface));border:1px solid color-mix(in srgb,var(--warn) 35%,var(--line));font-size:13.5px;color:var(--ink);flex-wrap:wrap}
@media(max-width:480px){.leg{grid-template-columns:1fr}}""",
    """<div class="wrap"><div class="card">
  <h2>Context window</h2><p class="muted num" id="tot" aria-live="polite"></p>
  <div class="stack" id="stack" role="img" aria-label="Context window usage"></div>
  <ul class="leg" id="leg"></ul>
  <div class="tip" id="tip" hidden><span>The chat is getting long. Older messages may be forgotten.</span><button class="btn" type="button" id="sum">Summarize older messages</button></div>
</div></div>""", FMT + """
var LIMIT=200000,COL=['#6366f1','#0ea5e9','#f59e0b','var(--line)'];
var parts=[['Instructions',4200],['Files',61000],['Chat history',104000],['Reserved for the reply',8000]];
var stack=document.getElementById('stack'),leg=document.getElementById('leg'),tot=document.getElementById('tot'),tip=document.getElementById('tip');
function render(){var used=parts.reduce(function(a,p){return a+p[1];},0);stack.innerHTML='';leg.innerHTML='';
  parts.forEach(function(p,i){var s=document.createElement('i');s.style.width=(p[1]/LIMIT*100)+'%';s.style.background=COL[i];s.title=p[0]+': '+p[1].toLocaleString()+' tokens';stack.appendChild(s);
    var li=document.createElement('li');li.innerHTML='<span class="sw"></span><span></span><b class="num"></b>';li.querySelector('.sw').style.background=COL[i];li.children[1].textContent=p[0];li.querySelector('b').textContent=fmt(p[1]);leg.appendChild(li);});
  var p=used/LIMIT;tot.textContent=fmt(used)+' of '+fmt(LIMIT)+' tokens used ('+Math.round(p*100)+'%)';stack.setAttribute('aria-label','Context window '+Math.round(p*100)+' percent full');tip.hidden=p<.8;}
document.getElementById('sum').addEventListener('click',function(){parts[2][1]=Math.round(parts[2][1]*.2);render();});
render();""")

add(C, "credits-card", "Credits Remaining Card",
    "Shows how many credits are left this month, when they reset, and a button to buy more. The bar changes color as credits run low.",
    BASE + """
.big{font-size:34px;font-weight:800;color:var(--ink);letter-spacing:-.02em;line-height:1.1;margin:8px 0 2px}
.big span{font-size:15px;font-weight:600;color:var(--muted);letter-spacing:0}
.card .bar{margin:14px 0 8px}.card .bar i{background:var(--lvl)}
.row{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-top:14px}""",
    """<div class="wrap"><div class="card ok" id="c">
  <h2>Credits</h2>
  <p class="big num" id="left">0 <span>left</span></p>
  <p class="muted num" id="of"></p>
  <div class="bar" role="progressbar" aria-label="Credits used" aria-valuemin="0" aria-valuemax="100" id="pb"><i id="bi"></i></div>
  <div class="row"><span class="muted">Resets on October 1</span><div style="display:flex;gap:8px"><button class="btn" type="button" id="use">Use 150</button><button class="btn pri" type="button" id="buy">Buy more</button></div></div>
</div></div>""", FMT + """
var TOTAL=2000,left=640,c=document.getElementById('c'),lf=document.getElementById('left'),of=document.getElementById('of'),bi=document.getElementById('bi'),pb=document.getElementById('pb');
function render(){var used=TOTAL-left,p=used/TOTAL;lf.innerHTML=left.toLocaleString()+' <span>left</span>';of.textContent=used.toLocaleString()+' of '+TOTAL.toLocaleString()+' credits used this month';
  bi.style.width=(p*100)+'%';pb.setAttribute('aria-valuenow',Math.round(p*100));c.className='card '+level(p);}
document.getElementById('use').addEventListener('click',function(){left=Math.max(0,left-150);render();});
document.getElementById('buy').addEventListener('click',function(){TOTAL+=1000;left+=1000;render();});
render();""")

add(C, "rate-limit-banner", "Rate Limit Banner",
    "A clear banner when someone hits their message limit, with a live countdown to when they can send again and the prompt box turned off.",
    BASE + """
.ban{display:flex;gap:12px;align-items:flex-start;padding:12px 14px;border-radius:12px;background:color-mix(in srgb,var(--warn) 10%,var(--surface));border:1px solid color-mix(in srgb,var(--warn) 40%,var(--line));color:var(--ink)}
.ban svg{color:var(--warn);flex:none;margin-top:2px}
.ban b{display:block}.ban p{margin:2px 0 0;font-size:13.5px;color:var(--text)}
.ban.ready{background:color-mix(in srgb,var(--good) 10%,var(--surface));border-color:color-mix(in srgb,var(--good) 40%,var(--line))}.ban.ready svg{color:var(--good)}
.pb{display:flex;gap:8px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:8px 8px 8px 14px;box-shadow:var(--shadow)}
.pb input{flex:1;border:0;outline:0;background:none;color:var(--ink);min-width:0;padding:6px 0}
.pb input:disabled{cursor:not-allowed}
.send{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;border:0;background:var(--accent);color:var(--accent-ink);cursor:pointer}
.send:disabled{opacity:.35;cursor:not-allowed}""",
    f"""<div class="wrap">
  <div class="ban" id="ban" role="status" aria-live="polite"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
    <div><b id="bt">You have reached your message limit</b><p id="bp">You can send more messages in <span class="num" id="cd">2:00</span>. Upgrade for a higher limit.</p></div></div>
  <form class="pb" id="f"><label class="sr" for="q">Message</label><input id="q" placeholder="Please wait until your limit resets" disabled><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></form>
  <button class="btn" type="button" id="again" style="align-self:center">Show the limit again</button>
</div>""", """
var cd=document.getElementById('cd'),ban=document.getElementById('ban'),bt=document.getElementById('bt'),bp=document.getElementById('bp'),q=document.getElementById('q'),s=document.getElementById('s'),t=null;
// Start the countdown with the number of seconds your API returns (for example the Retry-After header).
function limit(sec){clearInterval(t);var end=Date.now()+sec*1000;ban.className='ban';bt.textContent='You have reached your message limit';
  bp.innerHTML='You can send more messages in <span class="num" id="cd"></span>. Upgrade for a higher limit.';cd=document.getElementById('cd');q.disabled=true;s.disabled=true;q.placeholder='Please wait until your limit resets';
  function tick(){var left=Math.max(0,Math.round((end-Date.now())/1000));cd.textContent=Math.floor(left/60)+':'+String(left%60).padStart(2,'0');
    if(!left){clearInterval(t);ban.className='ban ready';bt.textContent='You can send messages again';bp.textContent='Your limit has reset.';q.disabled=false;s.disabled=false;q.placeholder='Ask anything';}}
  tick();t=setInterval(tick,1000);}
document.getElementById('again').addEventListener('click',function(){limit(120);});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';});
limit(120);""")

add(C, "message-cost", "Cost per Message",
    "A small line under each answer showing tokens in and out and what the message cost. Click it to see the full breakdown.",
    BASE + """
.ai{display:flex;gap:12px;align-items:flex-start}
.av{width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.col{display:flex;flex-direction:column;gap:6px;min-width:0;flex:1}
.bubble{background:var(--surface);border:1px solid var(--line);border-radius:4px 16px 16px 16px;padding:11px 15px;box-shadow:var(--shadow);line-height:1.6}
details.cost{font-size:12.5px;color:var(--muted)}
details.cost summary{cursor:pointer;list-style:none;display:inline-flex;gap:10px;align-items:center;padding:2px 6px;margin-left:-6px;border-radius:6px}
details.cost summary::-webkit-details-marker{display:none}
details.cost summary:hover{background:var(--surface-2);color:var(--ink)}
.bd{margin-top:6px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--surface);max-width:320px}
.bd table{width:100%;border-collapse:collapse}.bd td{padding:6px 10px;border-bottom:1px solid var(--line)}.bd tr:last-child td{border:0;font-weight:700;color:var(--ink)}
.bd td:last-child{text-align:right}""",
    f"""<div class="wrap">
  <div class="ai"><div class="av" aria-hidden="true">{ICON['spark']}</div><div class="col">
    <div class="bubble">Your trip budget comes to about $640 for three days: hotel $380, food $160 and transport $100.</div>
    <details class="cost"><summary class="num" id="sum"></summary><div class="bd"><table><tbody id="tb"></tbody></table></div></details>
    <p class="muted" style="margin:0;font-size:12px">Example prices for illustration only.</p>
  </div></div>
</div>""", FMT + """
// Example prices per million tokens. Replace with your provider's real prices.
var PRICE={input:3,output:15},usage={input:1840,output:420};
function money(n){return n<0.01?'$'+n.toFixed(4):'$'+n.toFixed(3)}
var ci=usage.input/1e6*PRICE.input,co=usage.output/1e6*PRICE.output;
document.getElementById('sum').textContent=fmt(usage.input)+' in, '+fmt(usage.output)+' out, '+money(ci+co);
document.getElementById('tb').innerHTML='<tr><td>Input, '+usage.input.toLocaleString()+' tokens</td><td>'+money(ci)+'</td></tr><tr><td>Output, '+usage.output.toLocaleString()+' tokens</td><td>'+money(co)+'</td></tr><tr><td>Total</td><td>'+money(ci+co)+'</td></tr>';""")

add(C, "usage-chart", "Daily Usage Chart",
    "A small bar chart of tokens used each day for two weeks. Hover or use the Tab key to read each day's exact number.",
    BASE + """
.wrap{width:min(100%,620px)}
.hd{display:flex;justify-content:space-between;align-items:flex-end;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.big{font-size:26px;font-weight:800;color:var(--ink);line-height:1}
.chart{position:relative;display:flex;align-items:flex-end;gap:5px;height:150px;padding-top:24px;border-bottom:1px solid var(--line)}
.chart button{flex:1;border:0;padding:0;background:var(--accent);opacity:.75;border-radius:5px 5px 0 0;cursor:pointer;min-width:0;transition:opacity .15s}
.chart button:hover,.chart button:focus-visible{opacity:1}
.chart button.today{background:var(--ink)}
.days{display:flex;gap:5px;margin-top:6px}.days span{flex:1;text-align:center;font-size:11px;color:var(--muted)}
.pop{position:absolute;top:-4px;transform:translateX(-50%);background:var(--ink);color:var(--bg);font-size:12px;padding:3px 8px;border-radius:6px;white-space:nowrap;pointer-events:none}
.pop[hidden]{display:none}""",
    """<div class="wrap"><div class="card">
  <div class="hd"><div><h2>Tokens per day</h2><p class="muted" style="margin:0">Last 14 days</p></div><div style="text-align:right"><div class="big num" id="tot"></div><span class="muted">total</span></div></div>
  <div class="chart" id="ch" role="list" aria-label="Tokens used per day"><div class="pop num" id="pop" hidden></div></div>
  <div class="days" id="days" aria-hidden="true"></div>
</div></div>""", FMT + """
var DATA=[42,51,38,66,72,24,18,55,61,70,84,79,31,58].map(function(k){return k*1000;});
var ch=document.getElementById('ch'),pop=document.getElementById('pop'),days=document.getElementById('days'),max=Math.max.apply(null,DATA),today=new Date();
document.getElementById('tot').textContent=fmt(DATA.reduce(function(a,b){return a+b;},0));
DATA.forEach(function(v,i){var d=new Date(today);d.setDate(today.getDate()-(DATA.length-1-i));var label=d.toLocaleDateString(undefined,{month:'short',day:'numeric'});
  var b=document.createElement('button');b.type='button';b.setAttribute('role','listitem');b.style.height=(v/max*100)+'%';if(i===DATA.length-1)b.className='today';
  b.setAttribute('aria-label',label+': '+v.toLocaleString()+' tokens');
  function show(){pop.hidden=false;pop.textContent=label+': '+fmt(v);pop.style.left=(b.offsetLeft+b.offsetWidth/2)+'px';}
  b.addEventListener('mouseenter',show);b.addEventListener('focus',show);b.addEventListener('mouseleave',function(){pop.hidden=true;});b.addEventListener('blur',function(){pop.hidden=true;});
  ch.appendChild(b);var s=document.createElement('span');s.textContent=i%2?'':d.getDate();days.appendChild(s);});""")

add(C, "upgrade-banner", "Upgrade Plan Banner",
    "A friendly banner that appears when someone is close to their free limit, comparing free and paid limits. It can be closed.",
    BASE + """
.up{position:relative;border-radius:var(--radius);padding:18px 20px;background:linear-gradient(135deg,color-mix(in srgb,var(--accent) 16%,var(--surface)),var(--surface));border:1px solid color-mix(in srgb,var(--accent) 35%,var(--line));box-shadow:var(--shadow)}
.up h2{font-size:16px;margin:0 0 4px;color:var(--ink);padding-right:30px}
.up p{margin:0 0 14px;font-size:14px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}
.pl{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 12px;font-size:13.5px}
.pl b{display:block;color:var(--ink);font-size:14px;margin-bottom:4px}.pl.pro{border-color:var(--accent)}
.pl ul{margin:0;padding-left:18px}.pl li{margin:2px 0}
.x{position:absolute;top:10px;right:10px;width:30px;height:30px;border:0;background:none;color:var(--muted);border-radius:8px;cursor:pointer;display:grid;place-items:center}
.x:hover{background:var(--surface-2);color:var(--ink)}
.acts{display:flex;gap:8px;flex-wrap:wrap}
@media(max-width:460px){.cmp{grid-template-columns:1fr}}""",
    f"""<div class="wrap">
  <section class="up" id="up" aria-labelledby="uh">
    <button class="x" id="x" type="button" aria-label="Close">{ICON['x']}</button>
    <h2 id="uh">You have used 90% of your free messages</h2>
    <p>Upgrade to keep chatting today and get longer answers.</p>
    <div class="cmp"><div class="pl"><b>Free</b><ul><li>40 messages a day</li><li>Short files</li><li>Standard speed</li></ul></div>
      <div class="pl pro"><b>Plus</b><ul><li>Unlimited messages</li><li>Files up to 100 pages</li><li>Faster answers</li></ul></div></div>
    <div class="acts"><a class="btn pri" href="#">Upgrade to Plus</a><button class="btn" type="button" id="later">Maybe later</button></div>
  </section>
  <button class="btn" type="button" id="show" style="align-self:center" hidden>Show the banner again</button>
</div>""", """
var up=document.getElementById('up'),show=document.getElementById('show');
function hideBanner(){up.hidden=true;show.hidden=false;show.focus();}
document.getElementById('x').addEventListener('click',hideBanner);document.getElementById('later').addEventListener('click',hideBanner);
show.addEventListener('click',function(){up.hidden=false;show.hidden=true;document.getElementById('x').focus();});""")

add(C, "price-calculator", "Model Price Calculator",
    "Pick a model and enter expected tokens to estimate the monthly cost. Uses example prices that you replace with your own.",
    BASE + """
.wrap{width:min(100%,600px)}
.models{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0 16px;border:0;padding:0}
.models label{border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;cursor:pointer;font-size:13px;display:flex;flex-direction:column;gap:2px}
.models label b{color:var(--ink);font-size:14px}
.models label:has(input:checked){border-color:var(--accent);background:var(--accent-soft)}
.models input{position:absolute;opacity:0;width:1px;height:1px}
.models label:has(input:focus-visible){outline:2px solid var(--accent);outline-offset:2px}
.fields{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.fields label{display:flex;flex-direction:column;gap:4px;font-size:13px;font-weight:600;color:var(--ink)}
.fields input{border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--surface);color:var(--ink);font-variant-numeric:tabular-nums}
.res{margin-top:16px;padding:14px;border-radius:12px;background:var(--surface-2);display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.res b{font-size:28px;color:var(--ink)}
@media(max-width:500px){.models,.fields{grid-template-columns:1fr}}""",
    """<div class="wrap"><div class="card">
  <h2>Estimate your monthly cost</h2><p class="muted" style="margin:0">Example prices per million tokens.</p>
  <fieldset class="models" id="models"><legend class="sr">Model</legend>
    <label><input type="radio" name="m" value="fast"><b>Fast</b><span>$0.25 in, $1.25 out</span></label>
    <label><input type="radio" name="m" value="balanced" checked><b>Balanced</b><span>$3 in, $15 out</span></label>
    <label><input type="radio" name="m" value="deep"><b>Deep</b><span>$15 in, $75 out</span></label></fieldset>
  <div class="fields"><label>Input tokens per month<input id="in" type="number" min="0" step="100000" value="20000000"></label>
    <label>Output tokens per month<input id="out" type="number" min="0" step="100000" value="4000000"></label></div>
  <div class="res" aria-live="polite"><span class="muted">Estimated cost per month</span><b class="num" id="res">$0</b></div>
</div></div>""", """
var P={fast:[0.25,1.25],balanced:[3,15],deep:[15,75]},inp=document.getElementById('in'),out=document.getElementById('out'),res=document.getElementById('res');
function calc(){var m=document.querySelector('input[name=m]:checked').value,i=Math.max(0,+inp.value||0),o=Math.max(0,+out.value||0);
  var cost=i/1e6*P[m][0]+o/1e6*P[m][1];res.textContent='$'+cost.toLocaleString(undefined,{minimumFractionDigits:2,maximumFractionDigits:2});}
document.querySelectorAll('input').forEach(function(x){x.addEventListener('input',calc);x.addEventListener('change',calc);});calc();""")

add(C, "daily-limit-ring", "Messages Left Today",
    "A ring that counts down the messages left today, with the reset time. Useful for free plans with a daily limit.",
    BASE + """
.wrap{width:min(100%,360px)}
.card{text-align:center}
.ring{position:relative;width:150px;height:150px;margin:6px auto 10px}
.ring svg{width:150px;height:150px;transform:rotate(-90deg)}
.ring circle{fill:none;stroke-width:12}.ring .bg{stroke:var(--surface-2)}.ring .fg{stroke:var(--lvl);stroke-linecap:round;transition:stroke-dashoffset .4s}
.ring div{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring b{font-size:38px;color:var(--ink);line-height:1}.ring span{font-size:13px;color:var(--muted)}
.card .btn{margin-top:12px}""",
    """<div class="wrap"><div class="card ok" id="c">
  <h2>Messages left today</h2>
  <div class="ring"><svg viewBox="0 0 150 150" aria-hidden="true"><circle class="bg" cx="75" cy="75" r="64"/><circle class="fg" id="fg" cx="75" cy="75" r="64"/></svg>
    <div role="status" aria-live="polite"><b class="num" id="n">0</b><span id="of">of 40</span></div></div>
  <p class="muted" id="reset" style="margin:0"></p>
  <button class="btn" type="button" id="send">Send a message</button>
</div></div>""", """
var LIMIT=40,left=12,fg=document.getElementById('fg'),n=document.getElementById('n'),c=document.getElementById('c'),send=document.getElementById('send'),C=2*Math.PI*64;
fg.style.strokeDasharray=C;
var mid=new Date();mid.setHours(24,0,0,0);var hrs=Math.max(1,Math.round((mid-new Date())/36e5));
document.getElementById('reset').textContent='Resets at midnight, in about '+hrs+(hrs===1?' hour':' hours');
function render(){var p=left/LIMIT;fg.style.strokeDashoffset=C*(1-p);n.textContent=left;c.className='card '+(left===0?'full':p<=.2?'warn':'ok');send.disabled=left===0;send.textContent=left===0?'Limit reached':'Send a message';}
send.addEventListener('click',function(){if(left>0){left--;render();}});render();""")

add(C, "spend-alerts", "Spending Alerts",
    "Set a monthly budget and choose when to get an email: at half, most or all of the budget. Shows spend so far and a forecast.",
    BASE + """
.wrap{width:min(100%,560px)}
.budget{display:flex;align-items:center;gap:10px;margin:14px 0}
.budget label{font-weight:600;color:var(--ink);font-size:14px}
.money{display:flex;align-items:center;border:1px solid var(--line);border-radius:10px;padding:0 10px;background:var(--surface)}
.money span{color:var(--muted)}.money input{border:0;outline:0;background:none;width:90px;padding:8px 4px;color:var(--ink);font-variant-numeric:tabular-nums}
.money:focus-within{border-color:var(--accent)}
.track{position:relative;height:12px;border-radius:99px;background:var(--surface-2);margin:18px 0 6px}
.track .sp{position:absolute;left:0;top:0;bottom:0;border-radius:99px;background:var(--accent)}
.track .fc{position:absolute;left:0;top:0;bottom:0;border-radius:99px;background:repeating-linear-gradient(45deg,color-mix(in srgb,var(--accent) 35%,transparent) 0 6px,transparent 6px 12px)}
.track .mk{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--muted)}
.legend{display:flex;justify-content:space-between;font-size:12.5px;color:var(--muted);gap:10px;flex-wrap:wrap}
.alerts{list-style:none;margin:16px 0 0;padding:0}
.alerts li{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 0;border-top:1px solid var(--line);font-size:14px;color:var(--ink)}
.alerts small{display:block;color:var(--muted);font-size:12.5px}
.over{color:var(--bad);font-weight:600}""",
    """<div class="wrap"><div class="card">
  <h2>Monthly budget</h2><p class="muted" style="margin:0">Get an email before costs get out of hand.</p>
  <div class="budget"><label for="b">Budget</label><div class="money"><span>$</span><input id="b" type="number" min="1" value="500"></div></div>
  <div class="track" aria-hidden="true"><div class="fc" id="fc"></div><div class="sp" id="sp"></div><div class="mk" style="left:50%"></div><div class="mk" style="left:80%"></div></div>
  <div class="legend num" aria-live="polite"><span id="spent"></span><span id="fore"></span></div>
  <ul class="alerts" id="al"></ul>
</div></div>""", """
var SPENT=212,DAY=19,DAYS=30,b=document.getElementById('b'),sp=document.getElementById('sp'),fc=document.getElementById('fc'),al=document.getElementById('al');
var LEVELS=[[50,'At 50% of budget',true],[80,'At 80% of budget',true],[100,'When the budget is used up',true]];
function render(){var bud=Math.max(1,+b.value||1),fore=Math.round(SPENT/DAY*DAYS);
  sp.style.width=Math.min(100,SPENT/bud*100)+'%';fc.style.width=Math.min(100,fore/bud*100)+'%';
  document.getElementById('spent').textContent='Spent so far: $'+SPENT;var f=document.getElementById('fore');f.textContent='Forecast this month: $'+fore;f.className=fore>bud?'over':'';
  al.innerHTML='';LEVELS.forEach(function(l,i){var li=document.createElement('li');li.innerHTML='<span></span><button class="tg" type="button" role="switch"></button>';
    li.firstChild.innerHTML=l[1]+'<small>Email when spend reaches $'+Math.round(bud*l[0]/100)+'</small>';var t=li.querySelector('.tg');t.setAttribute('aria-checked',l[2]);t.setAttribute('aria-label',l[1]);
    t.onclick=function(){l[2]=!l[2];t.setAttribute('aria-checked',l[2]);};al.appendChild(li);});}
b.addEventListener('input',render);render();""")
