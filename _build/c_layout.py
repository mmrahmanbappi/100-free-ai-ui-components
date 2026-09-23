from core import add, ICON

C = "chat-layout"

I = {
    "menu": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 01-11.6 7.1L4 20l1-4.5A8 8 0 1121 12z"/></svg>',
    "dots": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true"><circle cx="5" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="19" cy="12" r="1.8"/></svg>',
    "search": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "back": '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 17v5M9 3h6l-1 6 4 4H6l4-4z"/></svg>',
    "folder": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h7l2 2h9v11H3z"/></svg>',
    "link": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M10 14a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1M14 10a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1"/></svg>',
}

# A shared chat core: message list, prompt box, and a fake streaming reply
CHAT_CSS = """.msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px;scroll-behavior:smooth}
.m{max-width:80%;padding:9px 13px;border-radius:14px;line-height:1.55;font-size:14px;overflow-wrap:anywhere;animation:pop .2s ease}
.m.u{align-self:flex-end;background:var(--accent);color:var(--accent-ink);border-bottom-right-radius:4px}
.m.a{align-self:flex-start;background:var(--surface-2);color:var(--text);border-bottom-left-radius:4px}
@keyframes pop{from{opacity:0;transform:translateY(5px)}}
.pb{display:flex;gap:8px;align-items:flex-end;padding:10px;border-top:1px solid var(--line);background:var(--surface)}
.pb textarea{flex:1;border:1px solid var(--line);border-radius:12px;padding:9px 12px;resize:none;background:var(--surface);color:var(--ink);max-height:120px;line-height:1.45;min-width:0}
.pb textarea:focus{outline:0;border-color:var(--accent)}
.send{width:38px;height:38px;border-radius:11px;border:0;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;cursor:pointer;flex:none}
.send:disabled{opacity:.35;cursor:not-allowed}
.ib{width:34px;height:34px;display:grid;place-items:center;border:0;background:none;color:var(--muted);border-radius:9px;cursor:pointer;flex:none}
.ib:hover{background:var(--surface-2);color:var(--ink)}"""

CHAT_HTML = f"""<div class="msgs" id="msgs" role="log" aria-live="polite" aria-label="Messages"></div>
<form class="pb" id="pf"><label class="sr" for="pq">Message</label><textarea id="pq" rows="1" placeholder="Message the assistant"></textarea><button class="send" id="ps" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></form>"""

CHAT_JS = """var REPLIES=['Good question. Here is a short answer you can use right away.','Sure. I would start with the simplest option and adjust from there.','Here is a quick plan: first list what you need, then pick one small step for today.'];
function chat(root,seed){var msgs=root.querySelector('#msgs'),f=root.querySelector('#pf'),q=root.querySelector('#pq'),s=root.querySelector('#ps'),busy=false,n=0;
  function add(role,text){var d=document.createElement('div');d.className='m '+role;d.textContent=text;msgs.appendChild(d);msgs.scrollTop=msgs.scrollHeight;return d;}
  function grow(){q.style.height='auto';q.style.height=Math.min(q.scrollHeight,120)+'px';}
  (seed||[]).forEach(function(p){add(p[0],p[1]);});
  q.addEventListener('input',function(){grow();s.disabled=!q.value.trim()||busy;});
  q.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();f.requestSubmit();}});
  f.addEventListener('submit',function(e){e.preventDefault();var t=q.value.trim();if(!t||busy)return;add('u',t);q.value='';grow();s.disabled=true;busy=true;
    var d=add('a',''),words=REPLIES[n++%REPLIES.length].split(' '),i=0;
    (function tick(){if(i<words.length){d.textContent+=(i?' ':'')+words[i++];msgs.scrollTop=msgs.scrollHeight;setTimeout(tick,60);}else{busy=false;s.disabled=!q.value.trim();}})();});
  return {add:add};}"""

SEED = [["u", "Can you help me plan a small birthday party?"], ["a", "Of course. How many guests, and is it indoors or outdoors?"], ["u", "About 12 people, in my apartment."], ["a", "Nice. Plan finger food, one simple game and a playlist. Want a shopping list?"]]
SEED_JS = str(SEED).replace("'", '"')

add(C, "full-chat-window", "Full Chat Window",
    "A complete chat screen with a header, scrolling messages and a prompt box at the bottom. Replies stream in, and the view follows along.",
    CHAT_CSS + """
.win{width:min(100%,720px);height:min(560px,calc(100vh - 48px));display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
.hd{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line)}
.hd h1{font-size:15px;margin:0;color:var(--ink)}.hd span{font-size:12.5px;color:var(--muted)}
.hd .sp{flex:1}""",
    f"""<main class="win" id="w">
  <header class="hd"><div><h1>Party planning</h1><span>Balanced model</span></div><span class="sp"></span><button class="ib" type="button" aria-label="New chat">{I['plus']}</button></header>
  {CHAT_HTML}
</main>""", CHAT_JS + f"""
chat(document.getElementById('w'),{SEED_JS});""")

add(C, "chat-sidebar", "Chat Sidebar",
    "A sidebar with past chats grouped by date, a New chat button and the current chat highlighted. On phones it slides in from a menu button.",
    CHAT_CSS + """
body{padding:0;place-items:stretch}
.app{display:grid;grid-template-columns:260px 1fr;height:100vh;width:100%}
.side{background:var(--surface-2);border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0}
.side .top{padding:12px}
.new{width:100%;display:flex;align-items:center;gap:8px;justify-content:center;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:9px;font-weight:600;cursor:pointer}
.new:hover{border-color:var(--accent)}
nav{overflow-y:auto;padding:0 8px 12px}
nav h2{font-size:11.5px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:14px 8px 6px}
nav a{display:block;padding:8px 10px;border-radius:9px;color:var(--text);text-decoration:none;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
nav a:hover{background:var(--surface)}nav a[aria-current=page]{background:var(--surface);color:var(--ink);font-weight:600;box-shadow:0 1px 2px rgba(0,0,0,.08)}
.main{display:flex;flex-direction:column;min-width:0;min-height:0;background:var(--surface)}
.bar{display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid var(--line)}
.bar h1{font-size:15px;margin:0;color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.burger{display:none}.scrim{display:none}
@media(max-width:700px){.app{grid-template-columns:1fr}.burger{display:grid}
  .side{position:fixed;inset:0 auto 0 0;width:min(280px,85vw);z-index:5;transform:translateX(-100%);transition:transform .2s}
  .app.open .side{transform:none}.app.open .scrim{display:block;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:4}}""",
    f"""<div class="app" id="app">
  <aside class="side" id="side" aria-label="Chats"><div class="top"><button class="new" type="button" id="new">{I['plus']}New chat</button></div>
    <nav id="nav"></nav></aside>
  <div class="scrim" id="scrim"></div>
  <main class="main" id="w"><div class="bar"><button class="ib burger" id="bg" type="button" aria-label="Open chat list" aria-expanded="false" aria-controls="side">{I['menu']}</button><h1 id="title"></h1></div>
    {CHAT_HTML}</main>
</div>""", CHAT_JS + """
var GROUPS=[['Today',['Party planning','Email to my landlord']],['Yesterday',['Explain compound interest','Fix my CSS grid']],['Previous 7 days',['Trip to Lisbon','Birthday gift ideas','Weekly meal plan','Resume feedback']]];
var nav=document.getElementById('nav'),title=document.getElementById('title'),app=document.getElementById('app'),bg=document.getElementById('bg'),c=chat(document.getElementById('w'),""" + SEED_JS + """);
function menu(v){app.classList.toggle('open',v);bg.setAttribute('aria-expanded',v);}
function select(a){nav.querySelectorAll('a').forEach(function(x){x.removeAttribute('aria-current');});a.setAttribute('aria-current','page');title.textContent=a.textContent;menu(false);}
GROUPS.forEach(function(g){var h=document.createElement('h2');h.textContent=g[0];nav.appendChild(h);g[1].forEach(function(t){var a=document.createElement('a');a.href='#';a.textContent=t;
  a.addEventListener('click',function(e){e.preventDefault();select(a);});nav.appendChild(a);});});
select(nav.querySelector('a'));
bg.addEventListener('click',function(){menu(!app.classList.contains('open'));});
document.getElementById('scrim').addEventListener('click',function(){menu(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false);});
document.getElementById('new').addEventListener('click',function(){var a=document.createElement('a');a.href='#';a.textContent='New chat';a.addEventListener('click',function(e){e.preventDefault();select(a);});
  nav.insertBefore(a,nav.children[1]);select(a);document.getElementById('msgs').innerHTML='';document.getElementById('pq').focus();});""")

add(C, "empty-chat-state", "Empty Chat Welcome Screen",
    "The first screen of a new chat: a greeting, example prompts, what the assistant can do and its limits, with the prompt box ready below.",
    CHAT_CSS + """
.win{width:min(100%,760px);display:flex;flex-direction:column;gap:18px}
.hi{text-align:center}.logo{width:48px;height:48px;border-radius:14px;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;margin:0 auto 10px}
.hi h1{font-size:24px;margin:0;color:var(--ink)}.hi p{margin:4px 0 0;color:var(--muted)}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.col h2{font-size:13px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:0 0 8px;text-align:center}
.col ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.col li{background:var(--surface);border:1px solid var(--line);border-radius:11px;padding:9px 11px;font-size:13.5px;line-height:1.4}
.col button{width:100%;text-align:left;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:11px;padding:9px 11px;font-size:13.5px;cursor:pointer;line-height:1.4}
.col button:hover{border-color:var(--accent);background:var(--accent-soft)}
.box{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow)}
.box .pb{border-top:0}
@media(max-width:640px){.cols{grid-template-columns:1fr}}""",
    f"""<main class="win">
  <div class="hi"><div class="logo" aria-hidden="true">{ICON['spark']}</div><h1>How can I help today?</h1><p>Ask a question or pick an example to start.</p></div>
  <div class="cols">
    <section class="col"><h2>Examples</h2><ul>
      <li style="padding:0;border:0"><button type="button">Explain quantum computing in simple words</button></li>
      <li style="padding:0;border:0"><button type="button">Write a thank you note to a teacher</button></li>
      <li style="padding:0;border:0"><button type="button">Plan a week of easy dinners</button></li></ul></section>
    <section class="col"><h2>What I can do</h2><ul><li>Remember what you said earlier in this chat</li><li>Let you correct me and try again</li><li>Summarize files you upload</li></ul></section>
    <section class="col"><h2>Limits</h2><ul><li>I can make mistakes, so check important facts</li><li>I may not know very recent events</li><li>I do not give medical or legal decisions</li></ul></section>
  </div>
  <div class="box"><form class="pb" id="pf"><label class="sr" for="pq">Message</label><textarea id="pq" rows="1" placeholder="Message the assistant"></textarea><button class="send" id="ps" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></form></div>
</main>""", """
var q=document.getElementById('pq'),s=document.getElementById('ps');
document.querySelectorAll('.col button').forEach(function(b){b.addEventListener('click',function(){q.value=b.textContent;s.disabled=false;q.focus();});});
q.addEventListener('input',function(){s.disabled=!q.value.trim();});
document.getElementById('pf').addEventListener('submit',function(e){e.preventDefault();q.value='';s.disabled=true;});""")

add(C, "floating-chat-widget", "Floating Chat Widget",
    "A round chat button in the corner that opens a small chat panel, with an unread badge. Escape or the close button hides it again.",
    CHAT_CSS + """
.page{width:min(100%,640px);color:var(--muted);text-align:center}
.page h1{color:var(--ink);font-size:22px;margin:0 0 6px}
.fab{position:fixed;right:22px;bottom:22px;width:56px;height:56px;border-radius:50%;border:0;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;cursor:pointer;box-shadow:0 10px 30px -8px color-mix(in srgb,var(--accent) 70%,transparent);z-index:3;transition:transform .15s}
.fab:hover{transform:scale(1.05)}
.badge{position:absolute;top:-2px;right:-2px;min-width:20px;height:20px;border-radius:99px;background:#dc2626;color:#fff;font-size:11.5px;font-weight:700;display:grid;place-items:center;padding:0 5px;border:2px solid var(--bg)}
.panel{position:fixed;right:22px;bottom:90px;width:min(360px,calc(100vw - 32px));height:min(460px,calc(100vh - 120px));background:var(--surface);border:1px solid var(--line);border-radius:18px;box-shadow:0 24px 60px -20px rgba(0,0,0,.45);display:flex;flex-direction:column;overflow:hidden;z-index:3;transform-origin:bottom right;animation:open .18s ease}
@keyframes open{from{opacity:0;transform:scale(.9)}}
.ph{display:flex;align-items:center;gap:10px;padding:12px 14px;background:var(--accent);color:var(--accent-ink)}
.ph b{display:block;font-size:14.5px}.ph small{opacity:.85;font-size:12px}.ph .sp{flex:1}
.ph .ib{color:inherit}.ph .ib:hover{background:rgba(255,255,255,.15);color:inherit}""",
    f"""<div class="page"><h1>Your website</h1><p>The chat button sits in the bottom right corner.</p></div>
<button class="fab" id="fab" type="button" aria-label="Open chat" aria-expanded="false" aria-controls="panel">{I['chat']}<span class="badge" id="badge">1</span></button>
<section class="panel" id="panel" role="dialog" aria-labelledby="pt" hidden>
  <div class="ph"><div><b id="pt">Help assistant</b><small>Usually replies in a few seconds</small></div><span class="sp"></span><button class="ib" id="cls" type="button" aria-label="Close chat">{ICON['x']}</button></div>
  {CHAT_HTML}
</section>""", CHAT_JS + """
var fab=document.getElementById('fab'),panel=document.getElementById('panel'),badge=document.getElementById('badge');
var c=chat(panel,[['a','Hi! Looking for something? I can help you find it.']]);
function open(v){panel.hidden=!v;fab.setAttribute('aria-expanded',v);fab.setAttribute('aria-label',v?'Close chat':'Open chat');if(v){badge.hidden=true;document.getElementById('pq').focus();}else fab.focus();}
fab.addEventListener('click',function(){open(panel.hidden);});
document.getElementById('cls').addEventListener('click',function(){open(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!panel.hidden)open(false);});""")

add(C, "split-view-chat", "Split View: Chat and Document",
    "Chat on one side and a live document on the other, the layout used by AI writing tools. On phones it switches to two tabs.",
    CHAT_CSS + """
body{padding:0;place-items:stretch}
.app{display:grid;grid-template-columns:minmax(300px,2fr) 3fr;height:100vh;width:100%}
.chatp{display:flex;flex-direction:column;border-right:1px solid var(--line);background:var(--surface);min-width:0;min-height:0}
.doc{overflow-y:auto;background:var(--surface-2);padding:28px;min-width:0}
.paper{max-width:620px;margin:0 auto;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:28px 32px;box-shadow:var(--shadow)}
.paper h1{font-size:22px;color:var(--ink);margin:0 0 12px}.paper p{line-height:1.7;margin:0 0 12px}
.paper mark{background:color-mix(in srgb,var(--accent) 22%,transparent);color:inherit;border-radius:3px;padding:0 2px;animation:hl 1.5s ease}
@keyframes hl{from{background:color-mix(in srgb,var(--accent) 55%,transparent)}}
.tabs{display:none}
@media(max-width:700px){.app{grid-template-columns:1fr;grid-template-rows:auto 1fr}.tabs{display:flex;border-bottom:1px solid var(--line);background:var(--surface)}
  .tabs button{flex:1;border:0;background:none;padding:12px;font-weight:600;color:var(--muted);cursor:pointer;border-bottom:2px solid transparent}
  .tabs button[aria-selected=true]{color:var(--ink);border-color:var(--accent)}
  .chatp,.doc{grid-row:2;grid-column:1}.app[data-tab=doc] .chatp,.app[data-tab=chat] .doc{display:none}.doc{padding:14px}.paper{padding:20px}}""",
    f"""<div class="app" id="app" data-tab="chat">
  <div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-t="chat" aria-controls="cp">Chat</button><button role="tab" aria-selected="false" data-t="doc" aria-controls="dp">Document</button></div>
  <section class="chatp" id="cp" role="tabpanel" aria-label="Chat">{CHAT_HTML}</section>
  <section class="doc" id="dp" role="tabpanel" aria-label="Document"><article class="paper"><h1>Welcome email</h1>
    <p id="p1">Hi Sam, welcome to the team! We are so glad you are here.</p>
    <p id="p2">Your first week will be about meeting people and getting set up. On Monday you will have lunch with the design team.</p>
    <p id="p3">If you have questions, just reply to this email.</p></article></section>
</div>""", CHAT_JS + """
var app=document.getElementById('app'),tabs=[].slice.call(document.querySelectorAll('.tabs button'));
var c=chat(document.getElementById('cp'),[['u','Write a short welcome email for a new designer named Sam.'],['a','Done. I wrote it in the document on the right. Want it warmer or shorter?']]);
tabs.forEach(function(t){t.addEventListener('click',function(){app.dataset.tab=t.dataset.t;tabs.forEach(function(x){x.setAttribute('aria-selected',x===t);});});});
// When a new message is sent, pretend the AI edits the document
document.getElementById('pf').addEventListener('submit',function(){setTimeout(function(){var p=document.getElementById('p2');
  p.innerHTML='Your first week will be about meeting people and getting set up. <mark>We have planned a relaxed lunch on Monday so you can meet the design team.</mark>';},800);});""")

add(C, "mobile-chat", "Mobile Chat Screen",
    "A phone-sized chat with a back button, assistant name and status, messages, and a prompt bar with an attach button, sized for thumbs.",
    CHAT_CSS + """
.phone{width:min(100%,390px);height:min(720px,calc(100vh - 48px));display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:28px;overflow:hidden;box-shadow:var(--shadow)}
.top{display:flex;align-items:center;gap:8px;padding:12px 10px;border-bottom:1px solid var(--line)}
.who{display:flex;align-items:center;gap:10px;flex:1;min-width:0}
.av{width:36px;height:36px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.who b{display:block;color:var(--ink);font-size:15px}.who small{display:flex;align-items:center;gap:5px;color:var(--muted);font-size:12px}
.who small i{width:7px;height:7px;border-radius:50%;background:var(--good)}
.m{max-width:85%;font-size:15px}
.pb{padding:8px 10px 12px}.pb textarea{border-radius:20px;padding:10px 14px}.send{border-radius:50%;width:42px;height:42px}
.ib{width:42px;height:42px}""",
    f"""<main class="phone" id="w">
  <header class="top"><button class="ib" type="button" aria-label="Back">{I['back']}</button>
    <div class="who"><span class="av" aria-hidden="true">{ICON['spark']}</span><div><b>Assistant</b><small><i aria-hidden="true"></i>Online</small></div></div>
    <button class="ib" type="button" aria-label="More options">{I['dots']}</button></header>
  <div class="msgs" id="msgs" role="log" aria-live="polite" aria-label="Messages"></div>
  <form class="pb" id="pf"><button class="ib" type="button" aria-label="Attach a file">{ICON['clip']}</button><label class="sr" for="pq">Message</label><textarea id="pq" rows="1" placeholder="Message"></textarea><button class="send" id="ps" type="submit" aria-label="Send message" disabled>{ICON['send']}</button></form>
</main>""", CHAT_JS + f"""
chat(document.getElementById('w'),{SEED_JS});""")

add(C, "conversation-search", "Conversation Search",
    "Search through past chats as you type. Matching words are highlighted, and a friendly message appears when nothing is found.",
    """.wrap{width:min(100%,560px);background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
.sb{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--line);color:var(--muted)}
.sb input{flex:1;border:0;outline:0;background:none;color:var(--ink);font-size:15px;min-width:0}
.sb kbd{font:11.5px var(--mono);border:1px solid var(--line);border-radius:5px;padding:1px 6px;color:var(--muted)}
ul{list-style:none;margin:0;padding:6px;max-height:340px;overflow-y:auto}
li a{display:block;padding:10px 12px;border-radius:10px;text-decoration:none;color:inherit}
li a:hover,li a:focus{background:var(--surface-2);outline:0}
li b{display:block;color:var(--ink);font-size:14px}li span{display:block;color:var(--muted);font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
li small{color:var(--muted);font-size:12px}
mark{background:color-mix(in srgb,var(--accent) 25%,transparent);color:inherit;border-radius:3px;padding:0 1px}
.empty{padding:28px 16px;text-align:center;color:var(--muted);font-size:14px}
.count{padding:8px 16px;font-size:12px;color:var(--muted);border-top:1px solid var(--line)}""",
    f"""<div class="wrap" role="search">
  <div class="sb">{I['search']}<label class="sr" for="q">Search chats</label><input id="q" type="search" placeholder="Search your chats" autocomplete="off"><kbd>Esc</kbd></div>
  <ul id="res"></ul>
  <div class="count" id="cnt" role="status" aria-live="polite"></div>
</div>""", """
var CHATS=[['Trip to Lisbon','Day 2: visit the tram 28 route and the castle before lunch.','Mon'],['Email to my landlord','Write a polite email about the broken heater in the kitchen.','Mon'],
['Explain compound interest','Interest on your interest makes savings grow faster over time.','Sun'],['Fix my CSS grid','Use minmax(0, 1fr) so long words do not break the layout.','Sat'],
['Birthday gift ideas','A cooking class, a plant, or a photo book from your trip.','Sep 12'],['Weekly meal plan','Monday: lentil soup. Tuesday: tacos. Wednesday: pasta with greens.','Sep 10'],['Resume feedback','Move your strongest project to the top and cut the summary to two lines.','Sep 8']];
var q=document.getElementById('q'),res=document.getElementById('res'),cnt=document.getElementById('cnt');
function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function hl(text,t){var e=esc(text);if(!t)return e;var re=new RegExp('('+t.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&')+')','ig');return e.replace(re,'<mark>$1</mark>');}
function render(){var t=q.value.trim(),list=CHATS.filter(function(c){return !t||(c[0]+' '+c[1]).toLowerCase().indexOf(t.toLowerCase())>-1;});
  res.innerHTML=list.length?'':'<li class="empty">No chats match "'+esc(t)+'". Try a different word.</li>';
  list.forEach(function(c){var li=document.createElement('li');li.innerHTML='<a href="#"><b>'+hl(c[0],t)+'</b><span>'+hl(c[1],t)+'</span><small>'+c[2]+'</small></a>';res.appendChild(li);});
  cnt.textContent=t?list.length+(list.length===1?' chat found':' chats found'):CHATS.length+' chats';}
q.addEventListener('input',render);q.addEventListener('keydown',function(e){if(e.key==='Escape'){q.value='';render();}});render();""")

add(C, "chat-item-menu", "Chat List Item Menu",
    "Each chat in the list has a menu to rename it in place, pin it to the top, or delete it with an undo option.",
    """.wrap{width:min(100%,380px);background:var(--surface-2);border:1px solid var(--line);border-radius:var(--radius);padding:10px}
.wrap h2{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:6px 8px}
ul{list-style:none;margin:0;padding:0}
li{position:relative;display:flex;align-items:center;gap:6px;border-radius:9px;padding:0 4px 0 10px}
li:hover,li:focus-within{background:var(--surface)}
li a{flex:1;padding:9px 0;color:var(--text);text-decoration:none;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
li .pin{color:var(--accent);display:grid}
li input{flex:1;border:1px solid var(--accent);border-radius:7px;padding:6px 8px;background:var(--surface);color:var(--ink);font-size:14px;margin:4px 0;min-width:0}
.ib{width:28px;height:28px;display:grid;place-items:center;border:0;background:none;color:var(--muted);border-radius:7px;cursor:pointer;flex:none}
.ib:hover{background:var(--surface-2);color:var(--ink)}
.menu{position:absolute;right:4px;top:100%;background:var(--surface);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);padding:4px;min-width:150px;z-index:3;list-style:none;margin:0}
.menu button{width:100%;text-align:left;border:0;background:none;padding:8px 10px;border-radius:7px;font-size:13.5px;color:var(--ink);cursor:pointer}
.menu button:hover,.menu button:focus{background:var(--surface-2);outline:0}.menu .del{color:var(--bad)}
.undo{display:flex;justify-content:space-between;align-items:center;margin-top:8px;background:var(--ink);color:var(--bg);border-radius:10px;padding:8px 8px 8px 12px;font-size:13.5px}
.undo button{border:0;background:none;color:var(--bg);font-weight:700;cursor:pointer;padding:4px 8px;text-decoration:underline}""",
    """<div class="wrap"><h2>Your chats</h2><ul id="list"></ul><div class="undo" id="undo" role="status" aria-live="polite" hidden><span id="ut"></span><button type="button" id="ub">Undo</button></div></div>""", """
var items=[{t:'Party planning',p:false},{t:'Email to my landlord',p:false},{t:'Explain compound interest',p:false},{t:'Trip to Lisbon',p:true},{t:'Weekly meal plan',p:false}];
var list=document.getElementById('list'),undo=document.getElementById('undo'),ut=document.getElementById('ut'),last=null,timer=null,openMenu=null;
var PIN='"""+I['pin'].replace('"', '\\"')+"""',DOTS='"""+I['dots'].replace('"', '\\"')+"""';
function closeMenu(){if(openMenu){openMenu.remove();openMenu=null;}}
function render(){closeMenu();list.innerHTML='';items.slice().sort(function(a,b){return b.p-a.p;}).forEach(function(it){var li=document.createElement('li');
  li.innerHTML=(it.p?'<span class="pin" title="Pinned">'+PIN+'</span>':'')+'<a href="#"></a><button class="ib" type="button" aria-haspopup="menu" aria-expanded="false">'+DOTS+'</button>';
  li.querySelector('a').textContent=it.t;var mb=li.querySelector('.ib');mb.setAttribute('aria-label','Options for '+it.t);
  mb.addEventListener('click',function(e){e.stopPropagation();var was=openMenu&&openMenu.parentNode===li;closeMenu();if(was)return;
    var m=document.createElement('ul');m.className='menu';m.setAttribute('role','menu');
    [['Rename',rename],[it.p?'Unpin':'Pin to top',function(){it.p=!it.p;render();}],['Delete',del]].forEach(function(o,i){var b=document.createElement('button');b.type='button';b.setAttribute('role','menuitem');b.textContent=o[0];if(o[0]==='Delete')b.className='del';
      b.addEventListener('click',function(){closeMenu();o[1]();});var l=document.createElement('li');l.setAttribute('role','none');l.appendChild(b);m.appendChild(l);});
    li.appendChild(m);openMenu=m;mb.setAttribute('aria-expanded','true');m.querySelector('button').focus();
    m.addEventListener('keydown',function(ev){var bs=[].slice.call(m.querySelectorAll('button')),k=bs.indexOf(document.activeElement);
      if(ev.key==='ArrowDown'){ev.preventDefault();bs[(k+1)%bs.length].focus();}if(ev.key==='ArrowUp'){ev.preventDefault();bs[(k-1+bs.length)%bs.length].focus();}if(ev.key==='Escape'){closeMenu();mb.setAttribute('aria-expanded','false');mb.focus();}});});
  function rename(){var a=li.querySelector('a'),inp=document.createElement('input');inp.value=it.t;inp.setAttribute('aria-label','Chat name');li.replaceChild(inp,a);inp.focus();inp.select();
    function done(save){if(save&&inp.value.trim())it.t=inp.value.trim();render();}
    inp.addEventListener('keydown',function(ev){if(ev.key==='Enter')done(true);if(ev.key==='Escape')done(false);});inp.addEventListener('blur',function(){done(true);});}
  function del(){var i=items.indexOf(it);last={it:it,i:i};items.splice(i,1);render();ut.textContent='"'+it.t+'" deleted';undo.hidden=false;clearTimeout(timer);timer=setTimeout(function(){undo.hidden=true;last=null;},5000);}
  list.appendChild(li);});}
document.getElementById('ub').addEventListener('click',function(){if(!last)return;items.splice(last.i,0,last.it);last=null;undo.hidden=true;render();});
document.addEventListener('click',closeMenu);render();""")

add(C, "sidebar-folders", "Sidebar with Pinned Chats and Folders",
    "A chat sidebar with a pinned section and folders you can open and close, like projects. It remembers which folders are open.",
    """.side{width:min(100%,300px);background:var(--surface-2);border:1px solid var(--line);border-radius:var(--radius);padding:10px;max-height:calc(100vh - 48px);overflow-y:auto}
h2{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:8px 8px 6px;display:flex;align-items:center;gap:6px}
ul{list-style:none;margin:0;padding:0}
a.c{display:block;padding:7px 10px;border-radius:8px;color:var(--text);text-decoration:none;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
a.c:hover{background:var(--surface)}a.c[aria-current=page]{background:var(--surface);color:var(--ink);font-weight:600}
.fold{width:100%;display:flex;align-items:center;gap:8px;border:0;background:none;padding:8px 10px;border-radius:8px;color:var(--ink);font-size:14px;font-weight:600;cursor:pointer;text-align:left}
.fold:hover{background:var(--surface)}
.fold .n{margin-left:auto;font-size:12px;color:var(--muted);font-weight:500}
.fold .ch{transition:transform .15s;color:var(--muted);display:grid}.fold[aria-expanded=false] .ch{transform:rotate(-90deg)}
.fold+ul{padding-left:22px}
.pinned a.c{display:flex;gap:8px;align-items:center}.pinned svg{color:var(--accent);flex:none}""",
    f"""<nav class="side" aria-label="Chats" id="side">
  <h2>{I['pin']}Pinned</h2><ul class="pinned" id="pinned"></ul>
  <h2>Folders</h2><ul id="folders"></ul>
</nav>""", """
var PINNED=['Company handbook questions','Quarterly report draft'];
var FOLDERS=[['Website redesign',['Homepage copy','Color ideas','Launch checklist']],['Spanish practice',['Ordering food','Past tense drills']],['Home',['Kitchen renovation budget','Garden plan for spring','Moving checklist']]];
var PIN='"""+I['pin'].replace('"', '\\"')+"""',FOLD='"""+I['folder'].replace('"', '\\"')+"""',CH='"""+ICON['chev'].replace('"', '\\"')+"""';
var openState={0:true};  // Replace with saved state from your app, for example localStorage.
function link(t){var a=document.createElement('a');a.className='c';a.href='#';a.textContent=t;a.addEventListener('click',function(e){e.preventDefault();document.querySelectorAll('a.c').forEach(function(x){x.removeAttribute('aria-current');});a.setAttribute('aria-current','page');});return a;}
PINNED.forEach(function(t){var li=document.createElement('li'),a=link(t);a.insertAdjacentHTML('afterbegin',PIN);li.appendChild(a);document.getElementById('pinned').appendChild(li);});
FOLDERS.forEach(function(f,i){var li=document.createElement('li'),b=document.createElement('button'),ul=document.createElement('ul');b.type='button';b.className='fold';ul.id='fo'+i;
  b.innerHTML='<span class="ch">'+CH+'</span>'+FOLD+'<span></span><span class="n">'+f[1].length+'</span>';b.children[2].textContent=f[0];b.setAttribute('aria-controls',ul.id);
  f[1].forEach(function(t){var l=document.createElement('li');l.appendChild(link(t));ul.appendChild(l);});
  function set(v){b.setAttribute('aria-expanded',v);ul.hidden=!v;openState[i]=v;}
  b.addEventListener('click',function(){set(ul.hidden);});set(!!openState[i]);li.appendChild(b);li.appendChild(ul);document.getElementById('folders').appendChild(li);});
document.querySelector('#fo0 a.c').setAttribute('aria-current','page');""")

add(C, "share-dialog", "Share Conversation Dialog",
    "Share a chat with a link. Choose who can see it, whether to show your name, then copy the link with one click.",
    """.btn{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:9px 16px;font-size:14px;font-weight:600;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
dialog{border:0;border-radius:18px;padding:0;width:min(92vw,460px);background:var(--surface);color:var(--text);box-shadow:0 30px 80px -20px rgba(0,0,0,.5)}
dialog::backdrop{background:rgba(10,10,20,.45)}
.dg{padding:20px 22px}.dg h2{margin:0 0 4px;font-size:18px;color:var(--ink)}.dg>p{margin:0 0 16px;color:var(--muted);font-size:14px}
.opt{display:flex;flex-direction:column;gap:8px;margin-bottom:14px;border:0;padding:0}
.opt label{display:flex;gap:10px;align-items:flex-start;border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;cursor:pointer}
.opt label:has(input:checked){border-color:var(--accent);background:var(--accent-soft)}
.opt input{accent-color:var(--accent);margin-top:3px}
.opt b{display:block;color:var(--ink);font-size:14px}.opt small{color:var(--muted);font-size:12.5px}
.chk{display:flex;gap:8px;align-items:center;font-size:14px;margin-bottom:14px;color:var(--ink)}.chk input{accent-color:var(--accent);width:16px;height:16px}
.link{display:flex;gap:8px;align-items:center;border:1px solid var(--line);border-radius:12px;padding:6px 6px 6px 12px;background:var(--surface-2)}
.link input{flex:1;border:0;outline:0;background:none;color:var(--text);font:13px var(--mono);min-width:0}
.link.off{opacity:.5}
.x{position:absolute;top:12px;right:12px;width:32px;height:32px;border:0;background:none;color:var(--muted);border-radius:8px;cursor:pointer;display:grid;place-items:center}
.x:hover{background:var(--surface-2);color:var(--ink)}""",
    f"""<button class="btn" id="open" type="button" aria-haspopup="dialog">{I['link']}Share chat</button>
<dialog id="dlg" aria-labelledby="dh"><div class="dg" style="position:relative">
  <button class="x" id="x" type="button" aria-label="Close">{ICON['x']}</button>
  <h2 id="dh">Share this chat</h2><p>People with the link can read the chat. New messages you send later are not shared.</p>
  <fieldset class="opt"><legend class="sr">Who can see it</legend>
    <label><input type="radio" name="v" value="private" checked><span><b>Only me</b><small>The link will not work for anyone else.</small></span></label>
    <label><input type="radio" name="v" value="link"><span><b>Anyone with the link</b><small>They do not need an account.</small></span></label></fieldset>
  <label class="chk"><input type="checkbox" id="nm"> Show my name on the shared page</label>
  <div class="link off" id="lk"><label class="sr" for="url">Share link</label><input id="url" readonly value="https://example.com/share/party-planning-7f3k"><button class="btn pri" type="button" id="cp" disabled>Copy link</button></div>
</div></dialog>""", """
var dlg=document.getElementById('dlg'),lk=document.getElementById('lk'),cp=document.getElementById('cp'),url=document.getElementById('url');
function update(){var pub=document.querySelector('input[name=v]:checked').value==='link';lk.classList.toggle('off',!pub);cp.disabled=!pub;}
document.querySelectorAll('input[name=v]').forEach(function(r){r.addEventListener('change',update);});
document.getElementById('open').addEventListener('click',function(){dlg.showModal();});
document.getElementById('x').addEventListener('click',function(){dlg.close();});
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close();});
dlg.addEventListener('close',function(){document.getElementById('open').focus();});
cp.addEventListener('click',function(){url.select();var done=function(){cp.textContent='Copied';setTimeout(function(){cp.textContent='Copy link';},1500);};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(url.value).then(done,function(){document.execCommand('copy');done();});else{document.execCommand('copy');done();}});
update();""")
