from core import add, ICON

C = "prompt-input"

# Shared look for the prompt boxes in this category
BOX = """.pb{width:min(100%,680px);background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:10px 10px 10px 14px;transition:border-color .15s}
.pb:focus-within{border-color:var(--accent)}
.pb textarea{width:100%;border:0;outline:0;resize:none;background:none;min-height:24px;max-height:200px;line-height:1.5;padding:6px 0;color:var(--ink)}
.pb textarea::placeholder{color:var(--muted)}
.row{display:flex;align-items:center;gap:8px;min-width:0}
.row>span{min-width:0}
.sp{flex:1}
.ib{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;border:0;background:none;color:var(--muted);cursor:pointer}
.ib:hover{background:var(--surface-2);color:var(--ink)}
.send{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;border:0;background:var(--accent);color:var(--accent-ink);cursor:pointer;transition:opacity .15s,transform .1s}
.send:disabled{opacity:.35;cursor:not-allowed}
.send:not(:disabled):active{transform:scale(.94)}
.log{width:min(100%,680px);margin-bottom:12px;display:flex;flex-direction:column;gap:8px}
.msg{align-self:flex-end;max-width:85%;background:var(--accent-soft);color:var(--ink);padding:9px 13px;border-radius:14px 14px 4px 14px;white-space:pre-wrap;word-wrap:break-word;animation:pop .2s ease}
@keyframes pop{from{opacity:0;transform:translateY(6px)}}
.wrap{width:min(100%,680px);display:flex;flex-direction:column;align-items:stretch}"""

# Shared helper: grow a textarea with its content
GROW = """function grow(t){t.style.height='auto';t.style.height=Math.min(t.scrollHeight,200)+'px'}
function post(log,text){var m=document.createElement('div');m.className='msg';m.textContent=text;log.appendChild(m);}"""

add(C, "basic-prompt-box", "Basic Prompt Box",
    "A clean prompt box. Enter sends, Shift and Enter adds a new line, and the send button stays off until there is text.",
    BOX, f"""<div class="wrap">
  <div class="log" id="log" aria-live="polite"></div>
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Ask anything"></textarea>
    <div class="row"><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
</div>""", GROW + """
var f=document.getElementById('f'),q=document.getElementById('q'),s=document.getElementById('s'),log=document.getElementById('log');
q.addEventListener('input',function(){grow(q);s.disabled=!q.value.trim();});
q.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();f.requestSubmit();}});
f.addEventListener('submit',function(e){e.preventDefault();var t=q.value.trim();if(!t)return;post(log,t);q.value='';grow(q);s.disabled=true;q.focus();});""")

add(C, "auto-grow-prompt", "Auto-Growing Prompt",
    "A prompt that grows as people type, stops at a set height and then scrolls. Shows a live character count.",
    BOX + """
.count{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.count.near{color:var(--warn)}.count.over{color:var(--bad);font-weight:600}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" maxlength="2000" placeholder="Write a long message. The box grows with you."></textarea>
    <div class="row"><span class="count" id="c" aria-live="polite">0 / 2000</span><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
</div>""", GROW + """
var q=document.getElementById('q'),c=document.getElementById('c'),s=document.getElementById('s'),MAX=2000;
q.addEventListener('input',function(){grow(q);var n=q.value.length;c.textContent=n.toLocaleString()+' / '+MAX.toLocaleString();c.className='count'+(n>=MAX?' over':n>MAX*.9?' near':'');s.disabled=!q.value.trim();});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';q.dispatchEvent(new Event('input'));});""")

add(C, "prompt-with-attachments", "Prompt with File Attachments",
    "Attach files with a button or by dragging them onto the box. Each file shows as a chip with its size and a remove button.",
    BOX + """
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px}
.chips:empty{display:none}
.chip{display:flex;align-items:center;gap:8px;background:var(--surface-2);border:1px solid var(--line);border-radius:10px;padding:6px 6px 6px 10px;font-size:13px;max-width:240px}
.chip .n{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--ink)}
.chip .z{color:var(--muted);font-size:12px;flex:none}
.chip button{border:0;background:none;color:var(--muted);cursor:pointer;display:grid;place-items:center;width:22px;height:22px;border-radius:6px;flex:none}
.chip button:hover{background:var(--line);color:var(--ink)}
.pb.drag{border-style:dashed;border-color:var(--accent);background:var(--accent-soft)}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <div class="chips" id="chips" aria-live="polite"></div>
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Ask about your files, or drop them here"></textarea>
    <div class="row">
      <label class="ib" title="Attach files">{ICON['clip']}<span class="sr">Attach files</span><input id="file" type="file" multiple hidden></label>
      <span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button>
    </div>
  </form>
</div>""", GROW + """
var f=document.getElementById('f'),q=document.getElementById('q'),s=document.getElementById('s'),chips=document.getElementById('chips'),inp=document.getElementById('file'),files=[];
function size(b){return b<1024?b+' B':b<1048576?(b/1024).toFixed(0)+' KB':(b/1048576).toFixed(1)+' MB'}
function draw(){chips.innerHTML='';files.forEach(function(file,i){var c=document.createElement('div');c.className='chip';
  c.innerHTML='<span class="n"></span><span class="z"></span><button type="button" aria-label="Remove file">"""+ICON['x']+"""</button>';
  c.querySelector('.n').textContent=file.name;c.querySelector('.z').textContent=size(file.size);
  c.querySelector('button').onclick=function(){files.splice(i,1);draw();};chips.appendChild(c);});
  s.disabled=!q.value.trim()&&!files.length;}
function addFiles(list){for(var i=0;i<list.length;i++)files.push(list[i]);draw();}
inp.addEventListener('change',function(){addFiles(inp.files);inp.value='';});
q.addEventListener('input',function(){grow(q);draw();});
['dragenter','dragover'].forEach(function(ev){f.addEventListener(ev,function(e){e.preventDefault();f.classList.add('drag');});});
['dragleave','drop'].forEach(function(ev){f.addEventListener(ev,function(e){e.preventDefault();f.classList.remove('drag');});});
f.addEventListener('drop',function(e){if(e.dataTransfer.files.length)addFiles(e.dataTransfer.files);});
f.addEventListener('submit',function(e){e.preventDefault();files=[];q.value='';grow(q);draw();});""")

add(C, "voice-input-prompt", "Prompt with Voice Input",
    "A microphone button that turns speech into text when the browser supports it, with a pulsing record state and a timer.",
    BOX + """
.mic{position:relative}
.mic.on{background:var(--bad);color:#fff}
.mic.on::after{content:"";position:absolute;inset:-4px;border-radius:13px;border:2px solid var(--bad);animation:ring 1.2s ease-out infinite}
@keyframes ring{from{opacity:.8;transform:scale(1)}to{opacity:0;transform:scale(1.35)}}
.rec{display:none;align-items:center;gap:8px;font-size:13px;color:var(--bad);font-variant-numeric:tabular-nums}
.rec.on{display:flex}
.dot{width:8px;height:8px;border-radius:50%;background:var(--bad);animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:.2}}
.note{font-size:12px;color:var(--muted);margin-top:8px;text-align:center}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Type, or press the microphone and speak"></textarea>
    <div class="row">
      <button class="ib mic" id="mic" type="button" aria-pressed="false" aria-label="Start voice input">{ICON['mic']}</button>
      <span class="rec" id="rec" aria-live="polite"><span class="dot"></span><span id="t">0:00</span> Listening</span>
      <span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button>
    </div>
  </form>
  <p class="note" id="note"></p>
</div>""", GROW + """
var q=document.getElementById('q'),s=document.getElementById('s'),mic=document.getElementById('mic'),rec=document.getElementById('rec'),t=document.getElementById('t'),note=document.getElementById('note');
var SR=window.SpeechRecognition||window.webkitSpeechRecognition,r=null,on=false,timer=null,start=0,base='';
note.textContent=SR?'Voice input uses your browser speech service.':'Voice input is not supported in this browser, so this is a demo of the recording state.';
function tick(){var sec=Math.floor((Date.now()-start)/1000);t.textContent=Math.floor(sec/60)+':'+String(sec%60).padStart(2,'0');}
function set(v){on=v;mic.classList.toggle('on',v);rec.classList.toggle('on',v);mic.setAttribute('aria-pressed',v);mic.setAttribute('aria-label',v?'Stop voice input':'Start voice input');
  if(v){start=Date.now();tick();timer=setInterval(tick,500);}else clearInterval(timer);}
mic.addEventListener('click',function(){
  if(on){if(r)r.stop();set(false);return;}
  set(true);if(!SR)return;
  r=new SR();r.interimResults=true;r.continuous=true;base=q.value?q.value+' ':'';
  r.onresult=function(e){var txt='';for(var i=0;i<e.results.length;i++)txt+=e.results[i][0].transcript;q.value=base+txt;grow(q);s.disabled=!q.value.trim();};
  r.onend=function(){set(false);};r.onerror=function(){set(false);};r.start();});
q.addEventListener('input',function(){grow(q);s.disabled=!q.value.trim();});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';grow(q);s.disabled=true;});""")

add(C, "slash-commands-prompt", "Prompt with Slash Commands",
    "Type a slash to open a command menu. Use the arrow keys to move, Enter to pick, and Escape to close.",
    BOX + """
.pb{position:relative}
.menu{position:absolute;left:10px;right:10px;bottom:calc(100% + 8px);background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:6px;list-style:none;margin:0;max-height:min(210px,40vh);overflow:auto}
.menu[hidden]{display:none}
.menu li{display:flex;gap:10px;align-items:baseline;padding:8px 10px;border-radius:8px;cursor:pointer}
.menu li b{color:var(--ink);font-family:var(--mono);font-size:13px;min-width:92px}
.menu li span{color:var(--muted);font-size:13px}
.menu li[aria-selected=true]{background:var(--accent-soft)}
.menu .empty{color:var(--muted);font-size:13px;cursor:default}
.hint{font-size:12px;color:var(--muted)}
.hint kbd{font-family:var(--mono);background:var(--surface-2);border:1px solid var(--line);border-radius:5px;padding:0 5px}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <ul class="menu" id="menu" role="listbox" aria-label="Commands" hidden></ul>
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Type / for commands" role="combobox" aria-controls="menu" aria-expanded="false" aria-autocomplete="list"></textarea>
    <div class="row"><span class="hint">Press <kbd>/</kbd> for commands</span><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
</div>""", GROW + """
var CMDS=[['/summarize','Make a short summary'],['/translate','Translate to another language'],['/explain','Explain in simple words'],['/rewrite','Rewrite in a different tone'],['/table','Turn the answer into a table'],['/code','Answer with code only'],['/shorter','Make it shorter']];
var q=document.getElementById('q'),menu=document.getElementById('menu'),s=document.getElementById('s'),sel=0,shown=[];
function word(){var v=q.value.slice(0,q.selectionStart);var m=v.match(/(^|\\s)(\\/\\w*)$/);return m?m[2]:null;}
function render(){var w=word();if(w===null){menu.hidden=true;q.setAttribute('aria-expanded','false');return;}
  shown=CMDS.filter(function(c){return c[0].indexOf(w.toLowerCase())===0;});sel=Math.min(sel,Math.max(shown.length-1,0));menu.innerHTML='';
  if(!shown.length){menu.innerHTML='<li class="empty">No matching command</li>';}
  shown.forEach(function(c,i){var li=document.createElement('li');li.setAttribute('role','option');li.id='o'+i;li.setAttribute('aria-selected',i===sel);
    li.innerHTML='<b></b><span></span>';li.querySelector('b').textContent=c[0];li.querySelector('span').textContent=c[1];
    li.onmousedown=function(e){e.preventDefault();pick(i);};menu.appendChild(li);});
  menu.hidden=false;q.setAttribute('aria-expanded','true');if(shown.length)q.setAttribute('aria-activedescendant','o'+sel);}
function pick(i){var c=shown[i];if(!c)return;var pos=q.selectionStart,before=q.value.slice(0,pos).replace(/\\/\\w*$/,c[0]+' ');q.value=before+q.value.slice(pos);q.selectionStart=q.selectionEnd=before.length;menu.hidden=true;q.setAttribute('aria-expanded','false');grow(q);s.disabled=!q.value.trim();q.focus();}
q.addEventListener('input',function(){sel=0;grow(q);s.disabled=!q.value.trim();render();});
q.addEventListener('keydown',function(e){if(!menu.hidden&&shown.length){
  if(e.key==='ArrowDown'){e.preventDefault();sel=(sel+1)%shown.length;render();return;}
  if(e.key==='ArrowUp'){e.preventDefault();sel=(sel-1+shown.length)%shown.length;render();return;}
  if(e.key==='Enter'||e.key==='Tab'){e.preventDefault();pick(sel);return;}}
  if(e.key==='Escape'){menu.hidden=true;q.setAttribute('aria-expanded','false');}});
q.addEventListener('blur',function(){menu.hidden=true;});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';grow(q);s.disabled=true;});""")

add(C, "model-picker-prompt", "Prompt with Model Picker",
    "A prompt box with a small menu to choose how the AI should answer: fast, balanced or deep thinking.",
    BOX + """
.pick{position:relative}
.pbtn{display:flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);border-radius:999px;padding:5px 10px 5px 12px;font-size:13px;font-weight:600;cursor:pointer}
.pbtn:hover{border-color:var(--accent)}
.plist{position:absolute;left:0;bottom:calc(100% + 8px);width:260px;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:6px;list-style:none;margin:0;z-index:2}
.plist[hidden]{display:none}
.plist li{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:9px 10px;border-radius:8px;cursor:pointer}
.plist li:hover,.plist li:focus{background:var(--surface-2);outline:0}
.plist li b{color:var(--ink);font-size:14px}.plist li span{grid-column:1;color:var(--muted);font-size:12.5px}
.plist li i{grid-row:1/3;grid-column:2;align-self:center;color:var(--accent);visibility:hidden}
.plist li[aria-selected=true] i{visibility:visible}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Ask anything"></textarea>
    <div class="row">
      <div class="pick">
        <button class="pbtn" id="pb" type="button" aria-haspopup="listbox" aria-expanded="false"><span id="cur">Balanced</span>{ICON['chev']}</button>
        <ul class="plist" id="pl" role="listbox" aria-label="Answer mode" hidden>
          <li role="option" tabindex="-1" data-v="Fast" aria-selected="false"><b>Fast</b><span>Quick answers for simple questions</span><i>{ICON['check']}</i></li>
          <li role="option" tabindex="-1" data-v="Balanced" aria-selected="true"><b>Balanced</b><span>Good for most everyday tasks</span><i>{ICON['check']}</i></li>
          <li role="option" tabindex="-1" data-v="Deep thinking" aria-selected="false"><b>Deep thinking</b><span>Slower, better for hard problems</span><i>{ICON['check']}</i></li>
        </ul>
      </div>
      <span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button>
    </div>
  </form>
</div>""", GROW + """
var pb=document.getElementById('pb'),pl=document.getElementById('pl'),cur=document.getElementById('cur'),q=document.getElementById('q'),s=document.getElementById('s'),items=[].slice.call(pl.querySelectorAll('li'));
function open(v){pl.hidden=!v;pb.setAttribute('aria-expanded',v);if(v){var a=pl.querySelector('[aria-selected=true]')||items[0];a.focus();}}
function choose(li){items.forEach(function(x){x.setAttribute('aria-selected',x===li);});cur.textContent=li.dataset.v;open(false);pb.focus();}
pb.addEventListener('click',function(){open(pl.hidden);});
items.forEach(function(li,i){li.addEventListener('click',function(){choose(li);});
  li.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){e.preventDefault();items[(i+1)%items.length].focus();}
    if(e.key==='ArrowUp'){e.preventDefault();items[(i-1+items.length)%items.length].focus();}
    if(e.key==='Enter'||e.key===' '){e.preventDefault();choose(li);}if(e.key==='Escape'){open(false);pb.focus();}});});
document.addEventListener('click',function(e){if(!e.target.closest('.pick'))open(false);});
q.addEventListener('input',function(){grow(q);s.disabled=!q.value.trim();});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';grow(q);s.disabled=true;});""")

add(C, "prompt-suggestions", "Prompt Suggestions",
    "Starter ideas shown as buttons above an empty prompt. Clicking one fills the box so people can edit it before sending.",
    BOX + """
.hi{font-size:22px;font-weight:700;color:var(--ink);margin:0 0 6px;text-align:center}
.sub{color:var(--muted);text-align:center;margin:0 0 18px}
.sugs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-bottom:12px}
.sug{text-align:left;border:1px solid var(--line);background:var(--surface);border-radius:12px;padding:10px 12px;cursor:pointer;transition:border-color .15s,background .15s}
.sug:hover{border-color:var(--accent);background:var(--accent-soft)}
.sug b{display:block;color:var(--ink);font-size:14px}.sug span{color:var(--muted);font-size:13px}
@media(max-width:520px){.sugs{grid-template-columns:1fr}}""",
    f"""<div class="wrap">
  <p class="hi">What can I help with?</p>
  <p class="sub">Pick an idea to start, or write your own.</p>
  <div class="sugs" id="sugs">
    <button class="sug" type="button" data-p="Plan a 3 day trip to Lisbon on a small budget, with one day of food markets."><b>Plan a trip</b><span>3 days in Lisbon on a budget</span></button>
    <button class="sug" type="button" data-p="Explain how compound interest works using a simple example with real numbers."><b>Explain an idea</b><span>How compound interest works</span></button>
    <button class="sug" type="button" data-p="Write a short, friendly email asking my manager to move our meeting to Thursday."><b>Write an email</b><span>Move a meeting politely</span></button>
    <button class="sug" type="button" data-p="Give me 5 healthy dinner ideas I can cook in 20 minutes with basic ingredients."><b>Get ideas</b><span>Quick healthy dinners</span></button>
  </div>
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Ask anything"></textarea>
    <div class="row"><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
</div>""", GROW + """
var q=document.getElementById('q'),s=document.getElementById('s');
document.querySelectorAll('.sug').forEach(function(b){b.addEventListener('click',function(){q.value=b.dataset.p;grow(q);s.disabled=false;q.focus();q.setSelectionRange(q.value.length,q.value.length);});});
q.addEventListener('input',function(){grow(q);s.disabled=!q.value.trim();});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';grow(q);s.disabled=true;});""")

add(C, "prompt-token-counter", "Prompt with Token Counter",
    "Estimates how many tokens a prompt will use as people type, with a bar that turns orange and then red near the limit.",
    BOX + """
.meter{display:flex;align-items:center;gap:10px;font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums}
.bar{width:110px;height:6px;border-radius:99px;background:var(--surface-2);overflow:hidden}
.bar i{display:block;height:100%;width:0;background:var(--accent);border-radius:99px;transition:width .15s,background .15s}
.meter.near .bar i{background:var(--warn)}.meter.over .bar i{background:var(--bad)}.meter.over{color:var(--bad);font-weight:600}
.tip{font-size:12px;color:var(--muted);margin:8px 0 0;text-align:center}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="3" placeholder="Paste a long text to see how many tokens it uses"></textarea>
    <div class="row">
      <div class="meter" id="m" aria-live="polite"><span class="bar"><i id="b"></i></span><span id="n">0 / 1,000 tokens</span></div>
      <span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button>
    </div>
  </form>
  <p class="tip">The count is an estimate: about 4 characters per token for English text.</p>
</div>""", GROW + """
var q=document.getElementById('q'),m=document.getElementById('m'),b=document.getElementById('b'),n=document.getElementById('n'),s=document.getElementById('s'),LIMIT=1000;
function est(t){if(!t.trim())return 0;var words=t.trim().split(/\\s+/).length;return Math.max(Math.ceil(t.length/4),Math.ceil(words*1.3));}
q.addEventListener('input',function(){grow(q);var k=est(q.value),p=Math.min(k/LIMIT,1);b.style.width=(p*100)+'%';
  n.textContent=k.toLocaleString()+' / '+LIMIT.toLocaleString()+' tokens';m.className='meter'+(k>LIMIT?' over':k>LIMIT*.8?' near':'');
  s.disabled=!q.value.trim()||k>LIMIT;});
document.getElementById('f').addEventListener('submit',function(e){e.preventDefault();q.value='';q.dispatchEvent(new Event('input'));});""")

add(C, "send-shortcut-prompt", "Prompt with Send Shortcut Setting",
    "Lets people choose whether Enter sends the message or adds a new line, with a keyboard hint that updates to match.",
    BOX + """
.hint{font-size:12px;color:var(--muted)}
kbd{font-family:var(--mono);font-size:11.5px;background:var(--surface-2);border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:0 5px;color:var(--ink)}
.opt{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);margin:10px 4px 0;cursor:pointer;user-select:none}
.tg{width:34px;height:20px;border-radius:99px;background:var(--line);position:relative;flex:none;border:0;cursor:pointer;padding:0}
.tg::after{content:"";position:absolute;top:3px;left:3px;width:14px;height:14px;border-radius:50%;background:#fff;transition:left .15s}
.tg[aria-checked=true]{background:var(--accent)}.tg[aria-checked=true]::after{left:17px}""",
    f"""<div class="wrap">
  <div class="log" id="log" aria-live="polite"></div>
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Write a message"></textarea>
    <div class="row"><span class="hint" id="hint"></span><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
  <div class="opt"><button class="tg" id="tg" type="button" role="switch" aria-checked="true" aria-labelledby="tgl"></button><span id="tgl">Press Enter to send</span></div>
</div>""", GROW + """
var f=document.getElementById('f'),q=document.getElementById('q'),s=document.getElementById('s'),tg=document.getElementById('tg'),hint=document.getElementById('hint'),log=document.getElementById('log');
var mac=/Mac|iPhone|iPad/.test(navigator.platform),mod=mac?'Cmd':'Ctrl',enterSends=true;
function paint(){hint.innerHTML=enterSends?'<kbd>Enter</kbd> to send, <kbd>Shift</kbd> + <kbd>Enter</kbd> for a new line':'<kbd>'+mod+'</kbd> + <kbd>Enter</kbd> to send';tg.setAttribute('aria-checked',enterSends);}
tg.addEventListener('click',function(){enterSends=!enterSends;paint();q.focus();});
q.addEventListener('keydown',function(e){if(e.key!=='Enter'||e.isComposing)return;var modKey=e.metaKey||e.ctrlKey;
  if((enterSends&&!e.shiftKey&&!modKey)||(!enterSends&&modKey)){e.preventDefault();f.requestSubmit();}});
q.addEventListener('input',function(){grow(q);s.disabled=!q.value.trim();});
f.addEventListener('submit',function(e){e.preventDefault();var t=q.value.trim();if(!t)return;post(log,t);q.value='';grow(q);s.disabled=true;});
paint();""")

add(C, "prompt-history", "Prompt with History",
    "Press the Up arrow in an empty box to bring back earlier prompts, like a terminal. Recent prompts also appear as a list.",
    BOX + """
.recent{width:min(100%,680px);margin-top:12px}
.recent h2{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:0 0 6px 4px}
.recent ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:4px}
.recent button{width:100%;display:flex;align-items:center;gap:10px;text-align:left;border:0;background:none;padding:8px 10px;border-radius:10px;color:var(--text);cursor:pointer}
.recent button:hover{background:var(--surface-2);color:var(--ink)}
.recent button svg{color:var(--muted);flex:none}
.recent button span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.hint{font-size:12px;color:var(--muted)}
kbd{font-family:var(--mono);font-size:11.5px;background:var(--surface-2);border:1px solid var(--line);border-radius:5px;padding:0 5px}""",
    f"""<div class="wrap">
  <form class="pb" id="f">
    <label class="sr" for="q">Message</label>
    <textarea id="q" rows="1" placeholder="Ask anything. Press the Up arrow for earlier prompts."></textarea>
    <div class="row"><span class="hint"><kbd>Up</kbd> and <kbd>Down</kbd> to browse history</span><span class="sp"></span><button class="send" id="s" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></div>
  </form>
  <div class="recent"><h2>Recent prompts</h2><ul id="list"></ul></div>
</div>""", GROW + """
var HIST=['Summarize this article in 5 bullet points','Write a polite reminder about an unpaid invoice','Explain the difference between RAM and storage'];
var f=document.getElementById('f'),q=document.getElementById('q'),s=document.getElementById('s'),list=document.getElementById('list'),idx=-1,draft='';
function render(){list.innerHTML='';HIST.slice().reverse().slice(0,5).forEach(function(p){var li=document.createElement('li'),b=document.createElement('button');b.type='button';
  b.innerHTML='"""+ICON['history']+"""<span></span>';b.querySelector('span').textContent=p;b.onclick=function(){q.value=p;grow(q);s.disabled=false;q.focus();};li.appendChild(b);list.appendChild(li);});}
q.addEventListener('keydown',function(e){var atStart=q.selectionStart===0&&q.selectionEnd===0,atEnd=q.selectionStart===q.value.length;
  if(e.key==='ArrowUp'&&atStart){if(!HIST.length)return;e.preventDefault();if(idx===-1){draft=q.value;idx=HIST.length;}idx=Math.max(0,idx-1);q.value=HIST[idx];grow(q);s.disabled=false;}
  else if(e.key==='ArrowDown'&&idx>-1&&atEnd){e.preventDefault();idx++;if(idx>=HIST.length){idx=-1;q.value=draft;}else q.value=HIST[idx];grow(q);s.disabled=!q.value.trim();}
  else if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();f.requestSubmit();}});
q.addEventListener('input',function(){idx=-1;grow(q);s.disabled=!q.value.trim();});
f.addEventListener('submit',function(e){e.preventDefault();var t=q.value.trim();if(!t)return;HIST=HIST.filter(function(h){return h!==t;});HIST.push(t);idx=-1;q.value='';grow(q);s.disabled=true;render();});
render();""")
