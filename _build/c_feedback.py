from core import add, ICON

C = "feedback"

I = {
    "up": '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 10v11H3V10z"/><path d="M7 10l4-7a2.5 2.5 0 012.9 3L13 10h6.2a2 2 0 012 2.3l-1.3 7A2 2 0 0117.9 21H7"/></svg>',
    "down": '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 14V3h4v11z"/><path d="M17 14l-4 7a2.5 2.5 0 01-2.9-3L11 14H4.8a2 2 0 01-2-2.3l1.3-7A2 2 0 016.1 3H17"/></svg>',
    "star": '<svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z"/></svg>',
    "flag": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V4M4 4h12l-2 4 2 4H4"/></svg>',
    "redo": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 11-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg>',
    "info": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></svg>',
}


def face(mouth, eyes="normal"):
    """Simple SVG faces for the satisfaction scale (not emoji)."""
    m = {"sad": "M8 16.5q4-4 8 0", "meh": "M8.5 15.5h7", "ok": "M8 15q4 2 8 0", "happy": "M7.5 14q4.5 4.5 9 0", "very": "M7 13.5q5 6 10 0z"}[mouth]
    fill = ' fill="currentColor"' if mouth == "very" else ' fill="none"'
    return (f'<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
            f'<circle cx="12" cy="12" r="9.5"/><circle cx="9" cy="10" r=".9" fill="currentColor"/><circle cx="15" cy="10" r=".9" fill="currentColor"/><path d="{m}"{fill}/></svg>')


BASE = """.wrap{width:min(100%,640px);display:flex;flex-direction:column;gap:14px}
.ai{display:flex;gap:12px;align-items:flex-start}
.av{width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.col{display:flex;flex-direction:column;gap:8px;min-width:0;flex:1}
.bubble{background:var(--surface);border:1px solid var(--line);border-radius:4px 16px 16px 16px;padding:11px 15px;box-shadow:var(--shadow);color:var(--text);overflow-wrap:anywhere}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px 18px}
.card h2{font-size:15px;margin:0 0 4px;color:var(--ink)}.card p{margin:0 0 12px;color:var(--muted);font-size:14px}
.ib{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:0;background:none;color:var(--muted);height:32px;min-width:32px;padding:0 8px;border-radius:8px;cursor:pointer;font-size:13px}
.ib:hover{background:var(--surface-2);color:var(--ink)}
.ib[aria-pressed=true]{color:var(--accent);background:var(--accent-soft)}
.btn{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:9px;padding:7px 14px;font-size:14px;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:600}
.btn:disabled{opacity:.45;cursor:not-allowed}
.thanks{font-size:13.5px;color:var(--good);display:flex;align-items:center;gap:6px;animation:in .25s ease}
@keyframes in{from{opacity:0;transform:translateY(3px)}}"""

AV = f'<div class="av" aria-hidden="true">{ICON["spark"]}</div>'
ANSWER = "To remove a red wine stain, blot it right away, then cover it with salt or baking soda for 10 minutes. Rinse with cold water, not hot, and wash as usual."

add(C, "thumbs-feedback", "Thumbs Up and Down",
    "Two small buttons under an answer. Pick one to rate it, pick it again to undo, and see a short thank you.",
    BASE + """.tb{display:flex;align-items:center;gap:2px;margin-left:-6px}.msg{font-size:13px;color:var(--muted);margin-left:8px}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col"><div class="bubble">{ANSWER}</div>
  <div class="tb" role="group" aria-label="Rate this answer">
    <button class="ib" type="button" data-v="up" aria-pressed="false" aria-label="Good answer">{I['up']}</button>
    <button class="ib" type="button" data-v="down" aria-pressed="false" aria-label="Bad answer">{I['down']}</button>
    <span class="msg" id="m" role="status" aria-live="polite"></span>
  </div></div></div></div>""", """
var bs=[].slice.call(document.querySelectorAll('.tb .ib')),m=document.getElementById('m'),val=null;
// Send val ('up', 'down' or null) to your analytics here.
bs.forEach(function(b){b.addEventListener('click',function(){val=val===b.dataset.v?null:b.dataset.v;
  bs.forEach(function(x){x.setAttribute('aria-pressed',x.dataset.v===val);});
  m.textContent=val==='up'?'Thanks, glad it helped.':val==='down'?'Thanks. We will use this to improve.':'';});});""")

add(C, "thumbs-down-reasons", "Thumbs Down with Reasons",
    "When someone marks an answer as bad, a small panel asks why, with quick reason buttons and an optional comment.",
    BASE + """.tb{display:flex;align-items:center;gap:2px;margin-left:-6px}
.panel{animation:in .2s ease}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.chip{border:1px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:5px 12px;font-size:13px;cursor:pointer}
.chip[aria-pressed=true]{border-color:var(--accent);background:var(--accent-soft);color:var(--ink);font-weight:600}
textarea{width:100%;border:1px solid var(--line);border-radius:10px;background:var(--surface);padding:8px 10px;min-height:64px;resize:vertical;color:var(--ink)}
textarea:focus{outline:0;border-color:var(--accent)}
.row{display:flex;justify-content:flex-end;gap:8px;margin-top:10px}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col"><div class="bubble">{ANSWER}</div>
  <div class="tb" role="group" aria-label="Rate this answer">
    <button class="ib" type="button" id="up" aria-pressed="false" aria-label="Good answer">{I['up']}</button>
    <button class="ib" type="button" id="dn" aria-pressed="false" aria-label="Bad answer" aria-expanded="false" aria-controls="panel">{I['down']}</button>
  </div>
  <div id="slot" aria-live="polite"></div>
  <form class="card panel" id="panel" hidden>
    <h2 id="ph">What was wrong with this answer?</h2><p>Pick any that apply. This helps us improve.</p>
    <div class="chips" role="group" aria-labelledby="ph">
      <button class="chip" type="button" aria-pressed="false">Not correct</button><button class="chip" type="button" aria-pressed="false">Not helpful</button>
      <button class="chip" type="button" aria-pressed="false">Too long</button><button class="chip" type="button" aria-pressed="false">Did not follow my request</button>
      <button class="chip" type="button" aria-pressed="false">Unsafe or harmful</button><button class="chip" type="button" aria-pressed="false">Something else</button>
    </div>
    <label class="sr" for="cm">More details</label><textarea id="cm" placeholder="Tell us more (optional)"></textarea>
    <div class="row"><button class="btn" type="button" id="cx">Cancel</button><button class="btn pri" type="submit" id="send" disabled>Send feedback</button></div>
  </form></div></div></div>""", """
var up=document.getElementById('up'),dn=document.getElementById('dn'),panel=document.getElementById('panel'),slot=document.getElementById('slot'),send=document.getElementById('send'),cm=document.getElementById('cm'),chips=[].slice.call(document.querySelectorAll('.chip'));
function reset(){chips.forEach(function(c){c.setAttribute('aria-pressed','false');});cm.value='';send.disabled=true;}
function openPanel(v){panel.hidden=!v;dn.setAttribute('aria-expanded',v);if(v){reset();chips[0].focus();}}
function check(){send.disabled=!chips.some(function(c){return c.getAttribute('aria-pressed')==='true';})&&!cm.value.trim();}
up.addEventListener('click',function(){var on=up.getAttribute('aria-pressed')!=='true';up.setAttribute('aria-pressed',on);dn.setAttribute('aria-pressed','false');openPanel(false);slot.innerHTML=on?'<div class="thanks">Thanks for letting us know.</div>':'';});
dn.addEventListener('click',function(){var on=dn.getAttribute('aria-pressed')!=='true';dn.setAttribute('aria-pressed',on);up.setAttribute('aria-pressed','false');slot.innerHTML='';openPanel(on);});
chips.forEach(function(c){c.addEventListener('click',function(){c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')!=='true');check();});});
cm.addEventListener('input',check);
document.getElementById('cx').addEventListener('click',function(){dn.setAttribute('aria-pressed','false');openPanel(false);dn.focus();});
panel.addEventListener('submit',function(e){e.preventDefault();var picked=chips.filter(function(c){return c.getAttribute('aria-pressed')==='true';}).map(function(c){return c.textContent;});
  // Send {reasons: picked, comment: cm.value} to your server here.
  openPanel(false);slot.innerHTML='<div class="thanks">Thanks. Your feedback was sent.</div>';dn.focus();});""")

add(C, "star-rating", "Star Rating",
    "Rate an answer from one to five stars with the mouse or keyboard. Each level shows a word, like Good or Excellent.",
    BASE + """.stars{display:flex;gap:2px;border:0;padding:0;margin:0}
.stars input{position:absolute;opacity:0;width:1px;height:1px}
.stars label{cursor:pointer;color:var(--line);transition:color .1s,transform .1s;display:grid;place-items:center;padding:2px}
.stars label svg{fill:currentColor}
.stars label.on{color:#f5a524}.stars label:hover{transform:scale(1.12)}
.stars input:focus-visible+label{outline:2px solid var(--accent);outline-offset:1px;border-radius:6px}
.lbl{font-weight:600;color:var(--ink);min-height:1.5em;font-size:14px}
.card{display:flex;flex-direction:column;align-items:center;text-align:center;gap:6px}""",
    f"""<div class="wrap"><div class="card">
  <h2 id="h">How good was this answer?</h2>
  <fieldset class="stars" id="stars" aria-labelledby="h">
    {''.join(f'<input type="radio" name="r" id="s{i}" value="{i}"><label for="s{i}" data-v="{i}">{I["star"]}<span class="sr">{i} star{"s" if i > 1 else ""}</span></label>' for i in range(1, 6))}
  </fieldset>
  <div class="lbl" id="lbl" aria-live="polite">Pick a rating</div>
</div></div>""", """
var WORDS=['','Poor','Fair','Good','Very good','Excellent'],labels=[].slice.call(document.querySelectorAll('.stars label')),lbl=document.getElementById('lbl'),val=0;
function paint(n){labels.forEach(function(l){l.classList.toggle('on',+l.dataset.v<=n);});}
labels.forEach(function(l){l.addEventListener('mouseenter',function(){paint(+l.dataset.v);lbl.textContent=WORDS[+l.dataset.v];});});
document.getElementById('stars').addEventListener('mouseleave',function(){paint(val);lbl.textContent=val?WORDS[val]:'Pick a rating';});
document.querySelectorAll('.stars input').forEach(function(i){i.addEventListener('change',function(){val=+i.value;paint(val);lbl.textContent=WORDS[val]+'. Thanks for rating.';});});""")

add(C, "helpful-bar", "Was This Helpful Bar",
    "A short question at the end of an answer with Yes and No buttons. It turns into a thank you once someone answers.",
    BASE + """.hb{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:var(--surface-2);border:1px solid var(--line);border-radius:12px;padding:8px 10px 8px 14px;font-size:14px}
.hb span{color:var(--text);margin-right:auto}
.hb .btn{padding:5px 14px}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col"><div class="bubble">{ANSWER}</div>
  <div class="hb" id="hb" aria-live="polite"><span>Was this answer helpful?</span><button class="btn" type="button" data-v="yes">Yes</button><button class="btn" type="button" data-v="no">No</button></div>
</div></div></div>""", """
var hb=document.getElementById('hb');
hb.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
  hb.innerHTML='<span class="thanks">'+(b.dataset.v==='yes'?'Great, thanks for telling us.':'Sorry about that. Thanks for telling us.')+'</span>';});""")

add(C, "compare-answers", "Compare Two Answers",
    "Two answers side by side so people can pick the better one, or say both are good or both are bad. Useful for testing models.",
    BASE + """.wrap{width:min(100%,860px)}
.q{font-weight:600;color:var(--ink);margin:0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.opt{background:var(--surface);border:2px solid var(--line);border-radius:14px;padding:12px 14px;font-size:14px;line-height:1.6;transition:border-color .15s}
.opt b{display:block;font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.opt.win{border-color:var(--good)}.opt.lose{opacity:.55}
.choices{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.choices .btn[aria-pressed=true]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:600}
@media(max-width:620px){.pair{grid-template-columns:1fr}}""",
    """<div class="wrap">
  <p class="q">Which answer is better?</p>
  <div class="pair">
    <div class="opt" id="A"><b>Answer A</b>Water boils at 100 degrees Celsius at sea level. On a high mountain the air pressure is lower, so it boils at a lower temperature, around 90 degrees at 3,000 metres.</div>
    <div class="opt" id="B"><b>Answer B</b>Water boils at 100 degrees Celsius.</div>
  </div>
  <div class="choices" role="group" aria-label="Your choice">
    <button class="btn" type="button" data-v="A" aria-pressed="false">A is better</button>
    <button class="btn" type="button" data-v="B" aria-pressed="false">B is better</button>
    <button class="btn" type="button" data-v="tie" aria-pressed="false">Both are good</button>
    <button class="btn" type="button" data-v="bad" aria-pressed="false">Both are bad</button>
  </div>
  <p class="thanks" id="t" role="status" aria-live="polite" style="justify-content:center;min-height:1.4em;margin:0"></p>
</div>""", """
var bs=[].slice.call(document.querySelectorAll('.choices .btn')),A=document.getElementById('A'),B=document.getElementById('B'),t=document.getElementById('t');
bs.forEach(function(b){b.addEventListener('click',function(){var v=b.dataset.v;bs.forEach(function(x){x.setAttribute('aria-pressed',x===b);});
  A.className='opt'+(v==='A'?' win':v==='B'?' lose':'');B.className='opt'+(v==='B'?' win':v==='A'?' lose':'');
  t.textContent='Thanks. Your choice was saved.';});});""")

add(C, "report-dialog", "Report a Problem Dialog",
    "A report button opens a dialog to flag an answer, with categories and details. It traps focus and closes with Escape.",
    BASE + """dialog{border:0;border-radius:16px;padding:0;width:min(92vw,440px);background:var(--surface);color:var(--text);box-shadow:0 20px 60px -10px rgba(0,0,0,.4)}
dialog::backdrop{background:rgba(10,10,20,.45)}
.dh{display:flex;justify-content:space-between;align-items:center;padding:16px 18px 4px}
.dh h2{margin:0;font-size:17px;color:var(--ink)}
.db{padding:4px 18px 18px}
.opts{display:flex;flex-direction:column;gap:6px;margin:10px 0 12px;border:0;padding:0}
.opts label{display:flex;gap:10px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:9px 12px;cursor:pointer;font-size:14px}
.opts label:has(input:checked){border-color:var(--accent);background:var(--accent-soft);color:var(--ink)}
.opts input{accent-color:var(--accent)}
textarea{width:100%;border:1px solid var(--line);border-radius:10px;background:var(--surface);padding:8px 10px;min-height:70px;resize:vertical;color:var(--ink)}
textarea:focus{outline:0;border-color:var(--accent)}
.row{display:flex;justify-content:flex-end;gap:8px;margin-top:12px}
.tb{display:flex;gap:2px;margin-left:-6px}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col"><div class="bubble">{ANSWER}</div>
  <div class="tb"><button class="ib" type="button" id="open">{I['flag']}<span>Report</span></button><span id="done" role="status" aria-live="polite"></span></div>
</div></div></div>
<dialog id="dlg" aria-labelledby="dt">
  <form method="dialog" id="f">
    <div class="dh"><h2 id="dt">Report this answer</h2><button class="ib" type="button" id="close" aria-label="Close">{ICON['x']}</button></div>
    <div class="db">
      <fieldset class="opts"><legend class="sr">What is the problem?</legend>
        <label><input type="radio" name="k" value="wrong" required>It is wrong or misleading</label>
        <label><input type="radio" name="k" value="harm">It is harmful or unsafe</label>
        <label><input type="radio" name="k" value="private">It shares private information</label>
        <label><input type="radio" name="k" value="other">Something else</label>
      </fieldset>
      <label class="sr" for="d">Details</label><textarea id="d" placeholder="What happened? (optional)"></textarea>
      <div class="row"><button class="btn" type="button" id="cancel">Cancel</button><button class="btn pri" type="submit" value="send">Send report</button></div>
    </div>
  </form>
</dialog>""", """
var dlg=document.getElementById('dlg'),open=document.getElementById('open'),f=document.getElementById('f'),done=document.getElementById('done');
open.addEventListener('click',function(){f.reset();dlg.showModal();});
document.getElementById('close').addEventListener('click',function(){dlg.close('cancel');});
document.getElementById('cancel').addEventListener('click',function(){dlg.close('cancel');});
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close('cancel');});
dlg.addEventListener('close',function(){if(dlg.returnValue==='send'){done.innerHTML='<span class="thanks">Thanks. We will review this answer.</span>';}open.focus();});""")

add(C, "satisfaction-scale", "Satisfaction Scale",
    "Five faces from very unhappy to very happy. A quick way to ask how a chat went, drawn in SVG so it looks the same everywhere.",
    BASE + """.card{text-align:center}
.faces{display:flex;justify-content:center;gap:6px;margin:10px 0 6px;border:0;padding:0}
.faces input{position:absolute;opacity:0;width:1px;height:1px}
.faces label{display:flex;flex-direction:column;align-items:center;gap:4px;cursor:pointer;color:var(--muted);padding:8px 6px;border-radius:12px;min-width:62px;font-size:12px;transition:transform .1s,color .1s}
.faces label:hover{transform:translateY(-2px);color:var(--ink)}
.faces input:checked+label{color:var(--accent);background:var(--accent-soft);font-weight:600}
.faces input:focus-visible+label{outline:2px solid var(--accent);outline-offset:2px}
@media(max-width:420px){.faces label{min-width:52px;font-size:11px}}""",
    f"""<div class="wrap"><div class="card">
  <h2 id="h">How was your chat today?</h2><p>Your answer helps us make the assistant better.</p>
  <fieldset class="faces" aria-labelledby="h">
    {''.join(f'<input type="radio" name="s" id="f{i}" value="{i}"><label for="f{i}">{face(m)}<span>{w}</span></label>' for i, (m, w) in enumerate([("sad", "Very unhappy"), ("meh", "Unhappy"), ("ok", "Okay"), ("happy", "Happy"), ("very", "Very happy")], 1))}
  </fieldset>
  <p class="thanks" id="t" role="status" aria-live="polite" style="justify-content:center;min-height:1.4em;margin:0"></p>
</div></div>""", """
document.querySelectorAll('.faces input').forEach(function(i){i.addEventListener('change',function(){document.getElementById('t').textContent='Thanks for sharing how it went.';});});""")

add(C, "rewrite-options", "Rewrite Options Menu",
    "A Try again button with a menu to change the answer: shorter, longer, simpler or more formal. The answer updates in place.",
    BASE + """.tb{display:flex;gap:2px;margin-left:-6px;position:relative}
.menu{position:absolute;top:calc(100% + 4px);left:0;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:6px;list-style:none;margin:0;min-width:200px;z-index:2}
.menu li button{width:100%;text-align:left;border:0;background:none;padding:8px 10px;border-radius:8px;font-size:14px;color:var(--text);cursor:pointer}
.menu li button:hover,.menu li button:focus{background:var(--surface-2);color:var(--ink);outline:0}
.bubble{transition:opacity .2s}.bubble.fade{opacity:.35}
.tag{font-size:12px;color:var(--muted)}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col">
  <div class="bubble" id="b" aria-live="polite">Compound interest means you earn interest on your savings and also on the interest you already earned. Over many years this makes your money grow faster, like a snowball rolling downhill and picking up more snow.</div>
  <div class="tb"><button class="ib" type="button" id="tg" aria-haspopup="menu" aria-expanded="false">{I['redo']}<span>Try again</span></button><span class="tag" id="tag"></span>
    <ul class="menu" id="menu" role="menu" hidden>
      <li role="none"><button role="menuitem" type="button" data-k="short">Make it shorter</button></li>
      <li role="none"><button role="menuitem" type="button" data-k="long">Make it longer</button></li>
      <li role="none"><button role="menuitem" type="button" data-k="simple">Make it simpler</button></li>
      <li role="none"><button role="menuitem" type="button" data-k="formal">Make it more formal</button></li>
    </ul></div>
</div></div></div>""", """
var V={short:['Shorter','You earn interest on your interest, so savings grow faster over time.'],
  long:['Longer','Compound interest means you earn interest on your savings and also on the interest you already earned. If you save $1,000 at 5 percent a year, you have $1,050 after one year. In year two you earn 5 percent on $1,050, not $1,000. After 20 years you would have about $2,650 without adding anything. The longer you leave it, the faster it grows.'],
  simple:['Simpler','Your money makes money, and then that money makes money too.'],
  formal:['More formal','Compound interest is interest calculated on both the initial principal and the interest accumulated in previous periods, which accelerates growth over time.']};
var tg=document.getElementById('tg'),menu=document.getElementById('menu'),b=document.getElementById('b'),tag=document.getElementById('tag'),items=[].slice.call(menu.querySelectorAll('button'));
function show(v){menu.hidden=!v;tg.setAttribute('aria-expanded',v);if(v)items[0].focus();}
tg.addEventListener('click',function(){show(menu.hidden);});
items.forEach(function(it,i){it.addEventListener('click',function(){show(false);b.classList.add('fade');var k=it.dataset.k;
    setTimeout(function(){b.textContent=V[k][1];tag.textContent=V[k][0];b.classList.remove('fade');tg.focus();},600);});
  it.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){e.preventDefault();items[(i+1)%items.length].focus();}if(e.key==='ArrowUp'){e.preventDefault();items[(i-1+items.length)%items.length].focus();}if(e.key==='Escape'){show(false);tg.focus();}});});
document.addEventListener('click',function(e){if(!e.target.closest('.tb'))show(false);});""")

add(C, "confidence-badge", "Confidence Badge",
    "A small badge that tells people how sure the AI is about an answer, with a short explanation and a reminder to check sources.",
    BASE + """.badges{display:flex;flex-wrap:wrap;gap:8px}
.bd{position:relative;display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:4px 10px 4px 8px;font-size:12.5px;font-weight:600;border:1px solid;cursor:help;background:none;font-family:inherit}
.bd i{width:8px;height:8px;border-radius:50%;background:currentColor}
.hi{color:var(--good);border-color:color-mix(in srgb,var(--good) 40%,var(--line))}
.md{color:var(--warn);border-color:color-mix(in srgb,var(--warn) 40%,var(--line))}
.lo{color:var(--bad);border-color:color-mix(in srgb,var(--bad) 40%,var(--line))}
.tip{position:absolute;left:0;top:calc(100% + 6px);width:min(250px,75vw);background:var(--surface);color:var(--text);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);padding:9px 11px;font-weight:400;font-size:12.5px;line-height:1.5;visibility:hidden;opacity:0;transition:opacity .15s;z-index:2;text-align:left}
.bd:hover .tip,.bd:focus .tip{visibility:visible;opacity:1}""",
    f"""<div class="wrap">
  <div class="ai">{AV}<div class="col"><div class="bubble">The Eiffel Tower is about 330 metres tall, including its antennas.</div>
    <div class="badges"><button class="bd hi" type="button" aria-describedby="t1"><i></i>High confidence<span class="tip" role="tooltip" id="t1">This is a well known fact that many trusted sources agree on.</span></button></div></div></div>
  <div class="ai">{AV}<div class="col"><div class="bubble">Your plant likely needs more light. The yellow lower leaves are a common sign.</div>
    <div class="badges"><button class="bd md" type="button" aria-describedby="t2"><i></i>Medium confidence<span class="tip" role="tooltip" id="t2">Several causes are possible. A photo or more details would help.</span></button></div></div></div>
  <div class="ai">{AV}<div class="col"><div class="bubble">The shop may open at 9am on public holidays, but this can change.</div>
    <div class="badges"><button class="bd lo" type="button" aria-describedby="t3"><i></i>Low confidence<span class="tip" role="tooltip" id="t3">This could be out of date. Please check the shop's website before you go.</span></button></div></div></div>
</div>""")

add(C, "feedback-toast", "Feedback Toast with Undo",
    "After someone rates an answer, a small message slides up to confirm it, with an Undo button for a few seconds.",
    BASE + """.tb{display:flex;align-items:center;gap:2px;margin-left:-6px}
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,120%);display:flex;align-items:center;gap:14px;background:var(--ink);color:var(--bg);padding:10px 10px 10px 16px;border-radius:12px;font-size:14px;box-shadow:0 12px 30px -8px rgba(0,0,0,.4);transition:transform .25s ease;max-width:calc(100vw - 32px)}
.toast.on{transform:translate(-50%,0)}
.toast button{border:0;background:none;color:var(--accent-soft);font-weight:700;padding:6px 10px;border-radius:8px;cursor:pointer;font-size:14px}
.toast button:hover{background:rgba(255,255,255,.12)}
.bar{position:absolute;left:0;bottom:0;height:3px;background:var(--accent);border-radius:0 0 12px 12px;width:100%}
.toast.on .bar{animation:shrink 4s linear forwards}@keyframes shrink{to{width:0}}""",
    f"""<div class="wrap"><div class="ai">{AV}<div class="col"><div class="bubble">{ANSWER}</div>
  <div class="tb" role="group" aria-label="Rate this answer">
    <button class="ib" type="button" data-v="up" aria-pressed="false" aria-label="Good answer">{I['up']}</button>
    <button class="ib" type="button" data-v="down" aria-pressed="false" aria-label="Bad answer">{I['down']}</button>
  </div></div></div></div>
<div class="toast" id="toast" role="status" aria-live="polite"><span id="tm">Thanks for your feedback</span><button type="button" id="undo">Undo</button><span class="bar" aria-hidden="true"></span></div>""", """
var bs=[].slice.call(document.querySelectorAll('.tb .ib')),toast=document.getElementById('toast'),undo=document.getElementById('undo'),prev=null,val=null,t=null;
function set(v){val=v;bs.forEach(function(x){x.setAttribute('aria-pressed',x.dataset.v===v);});}
function hide(){toast.classList.remove('on');}
bs.forEach(function(b){b.addEventListener('click',function(){prev=val;set(val===b.dataset.v?null:b.dataset.v);if(val===null)return hide();
  toast.classList.remove('on');void toast.offsetWidth;toast.classList.add('on');clearTimeout(t);t=setTimeout(hide,4000);});});
undo.addEventListener('click',function(){set(prev);clearTimeout(t);hide();});""")
