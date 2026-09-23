from core import add, ICON

C = "messages"

I = {
    "copy": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 012-2h10"/></svg>',
    "redo": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 11-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg>',
    "speaker": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5L6 9H3v6h3l5 4z"/><path d="M15.5 8.5a5 5 0 010 7M18.5 5.5a9 9 0 010 13"/></svg>',
    "share": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg>',
    "edit": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/></svg>',
    "left": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
    "right": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.5v.5"/></svg>',
    "img": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/></svg>',
}

BASE = """.wrap{width:min(100%,660px);display:flex;flex-direction:column;gap:16px}
.ai,.me{display:flex;gap:12px;align-items:flex-start}
.me{flex-direction:row-reverse}
.av{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;flex:none;font-size:13px;font-weight:700}
.ai .av{background:var(--accent);color:var(--accent-ink)}.me .av{background:var(--surface-2);color:var(--ink);border:1px solid var(--line)}
.col{display:flex;flex-direction:column;gap:6px;min-width:0;max-width:calc(100% - 44px)}
.me .col{align-items:flex-end}
.bubble{background:var(--surface);border:1px solid var(--line);border-radius:4px 16px 16px 16px;padding:11px 15px;color:var(--text);box-shadow:var(--shadow);min-width:0;overflow-wrap:anywhere}
.me .bubble{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);border-radius:16px 4px 16px 16px;box-shadow:none}
.meta{font-size:12px;color:var(--muted)}
.tb{display:flex;gap:2px;align-items:center}
.tb button{display:inline-flex;align-items:center;gap:6px;border:0;background:none;color:var(--muted);height:30px;min-width:30px;padding:0 7px;border-radius:8px;cursor:pointer;font-size:13px}
.tb button:hover{background:var(--surface-2);color:var(--ink)}"""

AV_AI = f'<div class="av" aria-hidden="true">{ICON["spark"]}</div>'
AV_ME = '<div class="av" aria-hidden="true">JL</div>'

# Copy helper with a fallback for pages where the Clipboard API is not allowed
COPY = """function copyText(text){if(navigator.clipboard&&window.isSecureContext){return navigator.clipboard.writeText(text).catch(fallback);}return Promise.resolve(fallback());
  function fallback(){var t=document.createElement('textarea');t.value=text;t.setAttribute('readonly','');t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(t);}}
function flash(btn,label){var span=btn.querySelector('span')||btn,old=span.textContent;span.textContent=label;btn.setAttribute('aria-live','polite');setTimeout(function(){span.textContent=old;},1500);}"""

add(C, "chat-bubbles", "Chat Bubbles",
    "A simple conversation with user and assistant bubbles, avatars and times. The user sits on the right in the brand color.",
    BASE, f"""<div class="wrap" role="log" aria-label="Conversation">
  <div class="me">{AV_ME}<div class="col"><div class="bubble">What should I pack for three days in Edinburgh in October?</div><span class="meta">You, 9:41</span></div></div>
  <div class="ai">{AV_AI}<div class="col"><div class="bubble">Pack layers. October is often 8 to 13 degrees with some rain, so bring a warm sweater, a waterproof jacket and comfortable shoes for the hills.</div><span class="meta">Assistant, 9:41</span></div></div>
  <div class="me">{AV_ME}<div class="col"><div class="bubble">Do I need an umbrella?</div><span class="meta">You, 9:42</span></div></div>
  <div class="ai">{AV_AI}<div class="col"><div class="bubble">A small one helps, but the wind can be strong. A jacket with a hood is often more useful.</div><span class="meta">Assistant, 9:42</span></div></div>
</div>""")

add(C, "formatted-answer", "Formatted Answer",
    "A styled answer with headings, lists, bold text, inline code, a quote and a table, ready for text your AI returns as Markdown.",
    BASE + """
.prose{line-height:1.65}
.prose h3{font-size:16px;color:var(--ink);margin:14px 0 6px}.prose h3:first-child{margin-top:0}
.prose p{margin:0 0 10px}.prose ul,.prose ol{margin:0 0 10px;padding-left:22px}.prose li{margin:3px 0}
.prose strong{color:var(--ink)}
.prose code{font-family:var(--mono);font-size:.88em;background:var(--surface-2);border:1px solid var(--line);border-radius:5px;padding:1px 5px}
.prose blockquote{margin:10px 0;padding:6px 12px;border-left:3px solid var(--accent);color:var(--muted);background:var(--surface-2);border-radius:0 8px 8px 0}
.tw{overflow-x:auto;margin:6px 0 4px}
.prose table{border-collapse:collapse;width:100%;font-size:14px}.prose th,.prose td{border:1px solid var(--line);padding:6px 10px;text-align:left}
.prose th{background:var(--surface-2);color:var(--ink);font-weight:600}""",
    f"""<div class="wrap">
  <div class="ai">{AV_AI}<div class="col" style="flex:1"><div class="bubble prose">
    <h3>A simple weekly budget</h3>
    <p>Split your take-home pay into <strong>three groups</strong>. Move savings first, on payday.</p>
    <ol><li><strong>Needs</strong>: rent, bills, food</li><li><strong>Wants</strong>: eating out, hobbies</li><li><strong>Savings</strong>: emergency fund, goals</li></ol>
    <div class="tw"><table><thead><tr><th>Group</th><th>Share</th><th>On $2,400</th></tr></thead>
    <tbody><tr><td>Needs</td><td>50%</td><td>$1,200</td></tr><tr><td>Wants</td><td>30%</td><td>$720</td></tr><tr><td>Savings</td><td>20%</td><td>$480</td></tr></tbody></table></div>
    <blockquote>Tip: name your savings account after the goal, like <code>Holiday 2027</code>. It makes it harder to spend.</blockquote>
  </div></div></div>
</div>""")

add(C, "code-block-copy", "Code Block with Copy Button",
    "A code block with a language label, a copy button that confirms when done, and a button to wrap long lines.",
    BASE + """
.cb{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--surface-2);margin-top:8px}
.cbh{display:flex;align-items:center;justify-content:space-between;padding:4px 6px 4px 12px;border-bottom:1px solid var(--line);background:var(--surface)}
.lang{font-family:var(--mono);font-size:12px;color:var(--muted)}
.cb pre{margin:0;padding:12px 14px;overflow-x:auto;font:13px/1.6 var(--mono);color:var(--ink);tab-size:2}
.cb.wrapl pre{white-space:pre-wrap;word-break:break-word}
.k{color:#6f3fc9}.s{color:#086a42}.c{color:var(--muted);font-style:italic}.f{color:#0969da}
:root[data-theme=dark] .k{color:#c297ff}:root[data-theme=dark] .s{color:#7ee2a8}:root[data-theme=dark] .f{color:#79b8ff}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .k{color:#c297ff}:root:not([data-theme=light]) .s{color:#7ee2a8}:root:not([data-theme=light]) .f{color:#79b8ff}}""",
    f"""<div class="wrap">
  <div class="ai">{AV_AI}<div class="col" style="flex:1"><div class="bubble">Here is a small function that counts words in a text:
    <div class="cb" id="cb"><div class="cbh"><span class="lang">javascript</span><div class="tb">
      <button type="button" id="wr" aria-pressed="false"><span>Wrap</span></button>
      <button type="button" id="cp">{I['copy']}<span>Copy</span></button></div></div>
<pre id="code"><code><span class="c">// Count the words in a piece of text</span>
<span class="k">function</span> <span class="f">countWords</span>(text) {{
  <span class="k">const</span> words = text.trim().split(<span class="s">/\\s+/</span>).filter(Boolean);
  <span class="k">return</span> words.length;
}}

console.<span class="f">log</span>(<span class="f">countWords</span>(<span class="s">"The quick brown fox jumps over the lazy dog and keeps running"</span>)); <span class="c">// 12</span></code></pre></div>
  </div></div></div>
</div>""", COPY + """
var cp=document.getElementById('cp'),wr=document.getElementById('wr'),cb=document.getElementById('cb');
cp.addEventListener('click',function(){copyText(document.getElementById('code').innerText).then(function(){flash(cp,'Copied');});});
wr.addEventListener('click',function(){var on=cb.classList.toggle('wrapl');wr.setAttribute('aria-pressed',on);});""")

add(C, "message-actions", "Message Action Bar",
    "A row of actions under an answer: copy the text, read it aloud with the browser voice, and share it.",
    BASE + """
.tb{margin-left:-6px}
.tb button[aria-pressed=true]{color:var(--accent);background:var(--accent-soft)}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 16px;border-radius:999px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.on{opacity:1}""",
    f"""<div class="wrap">
  <div class="ai">{AV_AI}<div class="col"><div class="bubble" id="txt">A good first step to learn a language is 15 minutes a day. Short, daily practice builds the habit faster than one long weekly session.</div>
    <div class="tb" role="toolbar" aria-label="Message actions">
      <button type="button" id="cp" aria-label="Copy">{I['copy']}<span class="sr">Copy</span></button>
      <button type="button" id="rd" aria-label="Read aloud" aria-pressed="false">{I['speaker']}</button>
      <button type="button" id="sh" aria-label="Share">{I['share']}</button>
    </div></div></div>
  <div class="toast" id="toast" role="status" aria-live="polite"></div>
</div>""", COPY + """
var txt=document.getElementById('txt'),toast=document.getElementById('toast'),rd=document.getElementById('rd'),tt=null;
function say(m){toast.textContent=m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('on');},1600);}
document.getElementById('cp').addEventListener('click',function(){copyText(txt.textContent).then(function(){say('Copied to clipboard');});});
rd.addEventListener('click',function(){if(!('speechSynthesis' in window)){say('Reading aloud is not supported here');return;}
  if(speechSynthesis.speaking){speechSynthesis.cancel();rd.setAttribute('aria-pressed','false');return;}
  var u=new SpeechSynthesisUtterance(txt.textContent);u.onend=u.onerror=function(){rd.setAttribute('aria-pressed','false');};rd.setAttribute('aria-pressed','true');speechSynthesis.speak(u);});
document.getElementById('sh').addEventListener('click',function(){var data={title:'Answer',text:txt.textContent};
  if(navigator.share){navigator.share(data).catch(function(){});}else{copyText(txt.textContent).then(function(){say('Sharing is not available, so the text was copied');});}});""")

add(C, "answer-versions", "Answer Versions",
    "Regenerate an answer and move between versions with small arrows showing 1 of 3, like popular chat apps do.",
    BASE + """
.nav{display:flex;align-items:center;gap:2px;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.nav button:disabled{opacity:.35;cursor:not-allowed}
.bubble{transition:opacity .2s}.bubble.fade{opacity:.35}""",
    f"""<div class="wrap">
  <div class="me">{AV_ME}<div class="col"><div class="bubble">Give me a name for a small coffee shop by the sea.</div></div></div>
  <div class="ai">{AV_AI}<div class="col"><div class="bubble" id="b" aria-live="polite"></div>
    <div class="tb">
      <div class="nav" role="group" aria-label="Answer versions"><button type="button" id="pv" aria-label="Previous version">{I['left']}</button><span id="pos">1 / 1</span><button type="button" id="nx" aria-label="Next version">{I['right']}</button></div>
      <button type="button" id="re">{I['redo']}<span>Regenerate</span></button>
    </div></div></div>
</div>""", """
var POOL=['How about "Salt and Crema"? It is short and hints at the sea.','Try "Tide Pool Coffee". It sounds friendly and easy to remember.','"The Harbour Cup" feels warm and local.','"Driftwood Beans" has a relaxed beach feel.'];
var versions=[POOL[0]],cur=0,b=document.getElementById('b'),pos=document.getElementById('pos'),pv=document.getElementById('pv'),nx=document.getElementById('nx'),re=document.getElementById('re');
function show(){b.textContent=versions[cur];pos.textContent=(cur+1)+' / '+versions.length;pv.disabled=cur===0;nx.disabled=cur===versions.length-1;}
pv.addEventListener('click',function(){if(cur>0){cur--;show();}});
nx.addEventListener('click',function(){if(cur<versions.length-1){cur++;show();}});
re.addEventListener('click',function(){re.disabled=true;b.classList.add('fade');setTimeout(function(){versions.push(POOL[versions.length%POOL.length]);cur=versions.length-1;b.classList.remove('fade');re.disabled=false;show();},700);});
show();""")

add(C, "inline-citations", "Inline Citations",
    "Numbered source markers inside an answer. Hover or focus a number to see the source, and find the full list below.",
    BASE + """
.cite{position:relative;display:inline-block}
.cite>button{border:0;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;border-radius:6px;padding:0 5px;margin:0 1px;cursor:pointer;vertical-align:super;line-height:1.5}
.pop{position:absolute;left:50%;bottom:calc(100% + 6px);transform:translateX(-50%);width:240px;background:var(--surface);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);padding:10px 12px;font-size:13px;z-index:2;visibility:hidden;opacity:0;transition:opacity .15s}
.cite:hover .pop,.cite:focus-within .pop{visibility:visible;opacity:1}
.pop b{display:block;color:var(--ink)}.pop span{color:var(--muted);font-size:12px}
.srcs{margin:12px 0 0;padding:10px 0 0;border-top:1px solid var(--line);list-style:none;display:flex;flex-direction:column;gap:6px;font-size:13px}
.srcs li{display:flex;gap:8px}.srcs .n{color:var(--accent);font-weight:700;min-width:16px}.srcs a{color:var(--ink)}""",
    f"""<div class="wrap">
  <div class="ai">{AV_AI}<div class="col" style="flex:1"><div class="bubble" style="line-height:1.7">
    Most adults need 7 to 9 hours of sleep a night<span class="cite"><button type="button" aria-describedby="p1">1</button><span class="pop" role="tooltip" id="p1"><b>Sleep Health Guide</b><span>sleepguide.example, updated 2026</span></span></span>.
    Keeping the same wake-up time every day, even on weekends, helps the most<span class="cite"><button type="button" aria-describedby="p2">2</button><span class="pop" role="tooltip" id="p2"><b>Better Rest Study</b><span>health-journal.example, 2025</span></span></span>.
    Screens right before bed can make it harder to fall asleep<span class="cite"><button type="button" aria-describedby="p3">3</button><span class="pop" role="tooltip" id="p3"><b>Evening Light and Sleep</b><span>science-daily.example, 2024</span></span></span>.
    <ol class="srcs" aria-label="Sources">
      <li><span class="n">1</span><a href="#">Sleep Health Guide</a></li>
      <li><span class="n">2</span><a href="#">Better Rest Study</a></li>
      <li><span class="n">3</span><a href="#">Evening Light and Sleep</a></li>
    </ol>
  </div></div></div>
</div>""")

add(C, "edit-message", "Editable User Message",
    "An edit button on the user message turns it into a text box with Save and Cancel, so people can fix a question and ask again.",
    BASE + """
.me .col{width:100%}
.ed{width:min(100%,520px);background:var(--surface);border:1px solid var(--accent);border-radius:14px;padding:10px;box-shadow:var(--shadow)}
.ed textarea{width:100%;border:0;outline:0;resize:vertical;min-height:64px;background:none;color:var(--ink);line-height:1.5}
.ed .row{display:flex;justify-content:flex-end;gap:8px;margin-top:6px}
.btn{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:9px;padding:6px 14px;font-size:14px;cursor:pointer}
.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:600}
.edited{font-size:12px;color:var(--muted)}""",
    f"""<div class="wrap">
  <div class="me">{AV_ME}<div class="col" id="uc">
    <div class="bubble" id="ub">What is the capital of Australia? Is it Sidney?</div>
    <div class="tb"><span class="edited" id="edt" hidden>Edited</span><button type="button" id="eb">{I['edit']}<span>Edit</span></button></div>
  </div></div>
  <div class="ai">{AV_AI}<div class="col"><div class="bubble" id="ab" aria-live="polite">The capital of Australia is Canberra, not Sydney.</div></div></div>
</div>""", """
var uc=document.getElementById('uc'),ub=document.getElementById('ub'),eb=document.getElementById('eb'),ab=document.getElementById('ab'),edt=document.getElementById('edt'),box=null;
function close(){if(box){box.remove();box=null;}ub.hidden=false;eb.parentNode.hidden=false;eb.focus();}
eb.addEventListener('click',function(){if(box)return;box=document.createElement('div');box.className='ed';
  box.innerHTML='<label class="sr" for="et">Edit your message</label><textarea id="et"></textarea><div class="row"><button type="button" class="btn" id="cx">Cancel</button><button type="button" class="btn pri" id="sv">Save and ask again</button></div>';
  var ta=box.querySelector('textarea');ta.value=ub.textContent;ub.hidden=true;eb.parentNode.hidden=true;uc.insertBefore(box,ub);ta.focus();ta.setSelectionRange(ta.value.length,ta.value.length);
  box.querySelector('#cx').onclick=close;
  ta.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  box.querySelector('#sv').onclick=function(){var v=ta.value.trim();if(!v)return;ub.textContent=v;edt.hidden=false;close();ab.textContent='Thinking...';
    setTimeout(function(){ab.textContent='Here is a fresh answer to your edited question: Canberra is the capital. It was chosen as a compromise between Sydney and Melbourne.';},900);};});""")

add(C, "error-retry", "Error Message with Retry",
    "A clear error in the chat when an answer fails, with a Retry button that shows progress and then the answer.",
    BASE + """
.err{display:flex;gap:10px;align-items:flex-start;background:color-mix(in srgb,var(--bad) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--bad) 35%,var(--line));color:var(--ink);border-radius:4px 16px 16px 16px;padding:11px 14px}
.err svg{color:var(--bad);flex:none;margin-top:1px}
.err p{margin:0 0 8px}.err small{color:var(--muted);display:block;margin-bottom:8px}
.btn{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:9px;padding:6px 12px;font-size:14px;font-weight:600;cursor:pointer}
.btn:disabled{opacity:.6;cursor:wait}
.spin{width:14px;height:14px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--accent);animation:sp .8s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}""",
    f"""<div class="wrap">
  <div class="me">{AV_ME}<div class="col"><div class="bubble">Summarize the attached meeting notes.</div></div></div>
  <div class="ai">{AV_AI}<div class="col" id="slot" aria-live="polite"></div></div>
  <button class="btn" id="reset" type="button" style="align-self:center">Show the error again</button>
</div>""", """
var slot=document.getElementById('slot'),tries=0;
function error(){slot.innerHTML='<div class="err" role="alert">"""+I['alert'].replace('"', '\\"')+"""<div><p>Something went wrong while writing this answer.</p><small>The service is busy right now. Your message was not lost.</small><button class="btn" type="button" id="retry">"""+I['redo'].replace('"', '\\"')+"""<span>Retry</span></button></div></div>';
  document.getElementById('retry').onclick=retry;}
function retry(){var b=document.getElementById('retry');b.disabled=true;b.innerHTML='<span class="spin" aria-hidden="true"></span><span>Retrying</span>';tries++;
  setTimeout(function(){slot.innerHTML='<div class="bubble">The meeting agreed on three things: launch moves to May 12, Sara owns the pricing page, and the team meets again on Friday.</div>';},1200);}
document.getElementById('reset').addEventListener('click',error);error();""")

add(C, "file-message", "Message with Attached Files",
    "A user message with attached file cards, showing the file type, name and size, followed by the assistant's reply.",
    BASE + """
.files{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end}
.fc{display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:8px 12px 8px 8px;width:230px;max-width:100%;text-decoration:none;color:inherit}
.fc:hover{border-color:var(--accent)}
.ic{width:38px;height:38px;border-radius:9px;display:grid;place-items:center;color:#fff;font-size:11px;font-weight:800;flex:none}
.ic.pdf{background:#dc2626}.ic.xls{background:#15803d}.ic.img{background:linear-gradient(135deg,#f59e0b,#ec4899)}
.fc b{display:block;color:var(--ink);font-size:13.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.fc div span{font-size:12px;color:var(--muted)}
.fc div{min-width:0}""",
    f"""<div class="wrap">
  <div class="me">{AV_ME}<div class="col">
    <div class="files" aria-label="Attached files">
      <a class="fc" href="#"><span class="ic pdf">PDF</span><div><b>Lease agreement 2026.pdf</b><span>PDF, 1.2 MB</span></div></a>
      <a class="fc" href="#"><span class="ic xls">XLS</span><div><b>Monthly costs.xlsx</b><span>Spreadsheet, 48 KB</span></div></a>
      <a class="fc" href="#"><span class="ic img" aria-hidden="true">{I['img']}</span><div><b>Kitchen photo.jpg</b><span>Image, 2.4 MB</span></div></a>
    </div>
    <div class="bubble">Can you check if the rent in the lease matches my costs sheet?</div>
  </div></div>
  <div class="ai">{AV_AI}<div class="col"><div class="bubble">Yes, they match. The lease says $1,450 a month, and your sheet shows $1,450 for rent from March. The photo shows the dishwasher mentioned on page 3.</div></div></div>
</div>""")

add(C, "long-message-toggle", "Long Answer with Show More",
    "Long answers fold after a few lines with a soft fade and a Show more button, so the chat stays easy to scan.",
    BASE + """
.clip{position:relative;overflow:hidden;transition:max-height .3s ease}
.clip.shut{max-height:7.2em}
.clip.shut::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3em;background:linear-gradient(transparent,var(--surface))}
.clip p{margin:0 0 10px;line-height:1.6}
.more{align-self:flex-start;border:0;background:none;color:var(--accent);font-weight:600;font-size:14px;cursor:pointer;padding:4px 0}""",
    f"""<div class="wrap">
  <div class="ai">{AV_AI}<div class="col"><div class="bubble">
    <div class="clip shut" id="clip">
      <p>Here is a simple plan to run your first 5K in eight weeks.</p>
      <p>Weeks 1 and 2: walk for 5 minutes, then alternate 1 minute of easy running with 2 minutes of walking, eight times. Do this three days a week.</p>
      <p>Weeks 3 and 4: run 2 minutes and walk 1 minute, eight times. Keep the running slow enough that you can still talk.</p>
      <p>Weeks 5 and 6: run 5 minutes and walk 1 minute, five times. Add one longer run on the weekend.</p>
      <p>Weeks 7 and 8: run 10 minutes, walk 1 minute, three times, then try the full 5K at an easy pace. Rest the day before.</p>
    </div>
    <button class="more" id="more" type="button" aria-expanded="false" aria-controls="clip">Show more</button>
  </div></div></div>
</div>""", """
var clip=document.getElementById('clip'),more=document.getElementById('more');
more.addEventListener('click',function(){var open=clip.classList.toggle('shut')===false;more.textContent=open?'Show less':'Show more';more.setAttribute('aria-expanded',open);});""")
