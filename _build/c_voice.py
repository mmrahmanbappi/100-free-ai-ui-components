from core import add, ICON

C = "voice-media"

I = {
    "mic": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></svg>',
    "play": '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>',
    "pause": '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>',
    "cam": '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h4l2-3h6l2 3h4v11H3z"/><circle cx="12" cy="13" r="4"/></svg>',
    "up": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16V4M6 10l6-6 6 6M4 20h16"/></svg>',
    "end": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "mute": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0011.5 5.4M19 11c0 .9-.2 1.8-.5 2.6M12 18v3M3 3l18 18"/></svg>',
    "dl": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
}

BASE = """.wrap{width:min(100%,560px);display:flex;flex-direction:column;gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:18px 20px}
.card h2{font-size:15.5px;margin:0 0 4px;color:var(--ink)}
.muted{color:var(--muted);font-size:13px}
.num{font-variant-numeric:tabular-nums}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer}
.btn:hover{border-color:var(--accent)}.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.sm{padding:5px 10px;font-size:13px;border-radius:8px}
.note{font-size:13px;padding:9px 12px;border-radius:10px;background:var(--surface-2);color:var(--text)}
.note.warn{background:color-mix(in srgb,var(--warn) 10%,var(--surface));border:1px solid color-mix(in srgb,var(--warn) 35%,var(--line))}"""

add(C, "voice-recorder", "Voice Recorder with Waveform",
    "Record a voice message with live bars that follow your voice. Uses the real microphone when allowed, and explains clearly when it is not.",
    BASE + """
.rec{display:flex;align-items:center;gap:14px;margin-top:14px}
.mic{width:56px;height:56px;border-radius:50%;border:0;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;cursor:pointer;flex:none;position:relative}
.mic.on{background:#dc2626;color:#fff}
.mic.on::after{content:"";position:absolute;inset:-5px;border-radius:50%;border:2px solid #dc2626;animation:ring 1.3s ease-out infinite}
@keyframes ring{from{opacity:.8;transform:scale(1)}to{opacity:0;transform:scale(1.3)}}
.wave{flex:1;display:flex;align-items:center;gap:3px;height:48px;min-width:0;overflow:hidden}
.wave i{flex:1;min-width:2px;max-width:5px;height:4px;border-radius:3px;background:var(--line);transition:height .08s}
.wave.live i{background:var(--accent)}
.time{font-size:15px;font-weight:700;color:var(--ink);min-width:44px;text-align:right}
.clips{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:6px}
.clips li{display:flex;align-items:center;gap:10px;background:var(--surface-2);border-radius:10px;padding:8px 12px;font-size:14px;color:var(--ink)}
.clips audio{height:32px;flex:1;min-width:0}""",
    f"""<div class="wrap"><div class="card">
  <h2>Voice message</h2><p class="muted" style="margin:0">Press the button, speak, then press again to stop.</p>
  <div class="rec"><button class="mic" id="mic" type="button" aria-pressed="false" aria-label="Start recording">{I['mic']}</button>
    <div class="wave" id="wave" aria-hidden="true"></div><span class="time num" id="t" role="timer">0:00</span></div>
  <p class="note" id="note" role="status" aria-live="polite" hidden></p>
  <ul class="clips" id="clips" aria-label="Recordings"></ul>
</div></div>""", """
var mic=document.getElementById('mic'),wave=document.getElementById('wave'),t=document.getElementById('t'),note=document.getElementById('note'),clips=document.getElementById('clips');
var N=40,bars=[],stream=null,rec=null,chunks=[],ctx=null,an=null,raf=null,start=0,timer=null,demo=false;
for(var i=0;i<N;i++){var b=document.createElement('i');wave.appendChild(b);bars.push(b);}
function say(m,warn){note.hidden=false;note.textContent=m;note.className='note'+(warn?' warn':'');}
function fmt(ms){var s=Math.floor(ms/1000);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0');}
function draw(){var data=null;if(an){data=new Uint8Array(an.frequencyBinCount);an.getByteFrequencyData(data);}
  bars.forEach(function(b,i){var v=data?data[Math.floor(i*data.length/N/2)]/255:(0.2+0.6*Math.abs(Math.sin(Date.now()/180+i*.7))*Math.random());b.style.height=Math.max(4,v*46)+'px';});raf=requestAnimationFrame(draw);}
function setOn(v){mic.classList.toggle('on',v);wave.classList.toggle('live',v);mic.setAttribute('aria-pressed',v);mic.setAttribute('aria-label',v?'Stop recording':'Start recording');
  if(v){start=Date.now();timer=setInterval(function(){t.textContent=fmt(Date.now()-start);},250);draw();}else{clearInterval(timer);cancelAnimationFrame(raf);bars.forEach(function(b){b.style.height='4px';});}}
function addClip(url,ms){var li=document.createElement('li');li.innerHTML='<span class="num"></span>';li.firstChild.textContent=fmt(ms);
  if(url){var a=document.createElement('audio');a.controls=true;a.src=url;li.appendChild(a);}else{var s=document.createElement('span');s.className='muted';s.textContent='Demo clip (no microphone)';li.appendChild(s);}clips.prepend(li);}
async function begin(){note.hidden=true;
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia||!window.MediaRecorder){demo=true;say('This browser cannot record audio, so this is a demo of the recording screen.',true);setOn(true);return;}
  try{stream=await navigator.mediaDevices.getUserMedia({audio:true});}
  catch(e){demo=true;say(e.name==='NotAllowedError'?'Microphone access was blocked. Allow it in your browser settings to record. Showing a demo instead.':'No microphone was found. Showing a demo of the recording screen.',true);setOn(true);return;}
  demo=false;ctx=new (window.AudioContext||window.webkitAudioContext)();an=ctx.createAnalyser();an.fftSize=256;ctx.createMediaStreamSource(stream).connect(an);
  chunks=[];rec=new MediaRecorder(stream);rec.ondataavailable=function(e){chunks.push(e.data);};
  rec.onstop=function(){addClip(URL.createObjectURL(new Blob(chunks,{type:rec.mimeType})),Date.now()-start);stream.getTracks().forEach(function(tr){tr.stop();});ctx.close();an=null;};rec.start();setOn(true);}
function end(){var ms=Date.now()-start;setOn(false);if(demo){addClip(null,ms);}else if(rec){rec.stop();}t.textContent='0:00';}
mic.addEventListener('click',function(){if(mic.classList.contains('on'))end();else begin();});""")

add(C, "voice-mode", "Voice Mode Screen",
    "A full voice conversation screen with a glowing circle that reacts while the AI speaks, live captions, and mute and end buttons.",
    """.vm{width:min(100%,420px);min-height:min(560px,calc(100vh - 48px));border-radius:28px;background:radial-gradient(circle at 50% 35%,color-mix(in srgb,var(--accent) 22%,var(--surface)),var(--surface) 70%);border:1px solid var(--line);box-shadow:var(--shadow);display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:26px 20px}
.top{font-size:13px;color:var(--muted);display:flex;align-items:center;gap:8px}.top i{width:8px;height:8px;border-radius:50%;background:var(--good)}
.orb{width:170px;height:170px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,var(--accent) 45%,color-mix(in srgb,var(--accent) 55%,#000));box-shadow:0 0 70px -10px var(--accent);transition:transform .12s linear}
.cap{min-height:5.5em;text-align:center;font-size:17px;line-height:1.5;color:var(--ink);max-width:340px}
.cap small{display:block;font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.ctl{display:flex;gap:18px}
.cb{width:60px;height:60px;border-radius:50%;border:1px solid var(--line);background:var(--surface);color:var(--ink);display:grid;place-items:center;cursor:pointer}
.cb[aria-pressed=true]{background:var(--ink);color:var(--bg)}.cb.end{background:#dc2626;border-color:#dc2626;color:#fff}
.done{text-align:center}.done h2{color:var(--ink);font-size:18px;margin:0 0 6px}""",
    f"""<main class="vm" id="vm" aria-label="Voice conversation">
  <div class="top" id="top"><i aria-hidden="true"></i><span id="state">Assistant is speaking</span></div>
  <div class="orb" id="orb" aria-hidden="true"></div>
  <p class="cap" id="cap" aria-live="polite"></p>
  <div class="ctl" id="ctl"><button class="cb" id="mute" type="button" aria-pressed="false" aria-label="Mute microphone">{I['mute']}</button><button class="cb end" id="end" type="button" aria-label="End voice chat">{I['end']}</button></div>
</main>""", """
var LINES=[['Assistant','Sure. A simple way to start running is to walk and jog in turns.'],['You','How long should each part be?'],['Assistant','Try one minute of easy jogging, then two minutes of walking. Repeat that eight times.'],['You','That sounds doable.'],['Assistant','Great. Do it three times this week and we can adjust next week.']];
var orb=document.getElementById('orb'),cap=document.getElementById('cap'),state=document.getElementById('state'),mute=document.getElementById('mute'),i=0,raf,talking=true,muted=false,timer;
function pulse(){var s=talking?1+Math.abs(Math.sin(Date.now()/140))*.12*Math.random()+.03:1+Math.sin(Date.now()/600)*.02;orb.style.transform='scale('+s.toFixed(3)+')';raf=requestAnimationFrame(pulse);}
function next(){var l=LINES[i%LINES.length];i++;talking=l[0]==='Assistant';state.textContent=talking?'Assistant is speaking':(muted?'You are muted':'Listening');
  cap.innerHTML='<small></small>';cap.firstChild.textContent=l[0];cap.appendChild(document.createTextNode(l[1]));}
mute.addEventListener('click',function(){muted=!muted;mute.setAttribute('aria-pressed',muted);mute.setAttribute('aria-label',muted?'Unmute microphone':'Mute microphone');if(!talking)state.textContent=muted?'You are muted':'Listening';});
document.getElementById('end').addEventListener('click',function(){clearInterval(timer);cancelAnimationFrame(raf);document.getElementById('vm').innerHTML='<div></div><div class="done"><h2>Voice chat ended</h2><p class="muted">5 minutes. A transcript was saved to this chat.</p></div><button class="cb" type="button" onclick="location.reload()" aria-label="Start again" style="width:auto;padding:0 20px;border-radius:99px;font-weight:600">Start again</button>';});
next();pulse();timer=setInterval(next,3200);""")

add(C, "audio-answer-player", "Audio Answer Player",
    "A compact player for spoken answers with play and pause, a seek bar, playback speed and the matching text highlighted as it plays.",
    BASE + """
.pl{display:flex;align-items:center;gap:12px;margin-top:14px}
.pp{width:44px;height:44px;border-radius:50%;border:0;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;cursor:pointer;flex:none}
.seek{flex:1;accent-color:var(--accent);min-width:0}
.sp{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:4px 8px;font-size:13px;font-weight:700;cursor:pointer;min-width:48px}
.txt{margin:14px 0 0;line-height:1.7;font-size:15px}
.txt span{transition:background .15s;border-radius:4px}
.txt span.on{background:color-mix(in srgb,var(--accent) 22%,transparent);color:var(--ink)}""",
    f"""<div class="wrap"><div class="card">
  <h2>Listen to the answer</h2><p class="muted" style="margin:0">Connect this to the audio file from your speech service.</p>
  <div class="pl"><button class="pp" id="pp" type="button" aria-label="Play">{I['play']}</button>
    <label class="sr" for="seek">Position</label><input class="seek" id="seek" type="range" min="0" max="1000" value="0">
    <span class="muted num" id="tm">0:00 / 0:18</span><button class="sp" id="sp" type="button" aria-label="Playback speed 1 times">1x</button></div>
  <p class="txt" id="txt"></p>
</div></div>""", """
// Demo timing. With a real file, use an <audio> element and its timeupdate event instead.
var SENT=['Water boils at 100 degrees Celsius at sea level.','At higher places the air pressure is lower,','so water boils at a lower temperature.','In a city at 3,000 metres it boils near 90 degrees.'];
var DUR=18,pos=0,rate=1,playing=false,last=0,raf,pp=document.getElementById('pp'),seek=document.getElementById('seek'),tm=document.getElementById('tm'),sp=document.getElementById('sp'),txt=document.getElementById('txt');
var PLAY='"""+I['play'].replace('"', '\\"')+"""',PAUSE='"""+I['pause'].replace('"', '\\"')+"""';
SENT.forEach(function(s,i){var e=document.createElement('span');e.textContent=s+' ';txt.appendChild(e);});
var spans=[].slice.call(txt.children);
function fmt(s){s=Math.floor(s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0');}
function paint(){seek.value=Math.round(pos/DUR*1000);tm.textContent=fmt(pos)+' / '+fmt(DUR);seek.setAttribute('aria-valuetext',fmt(pos)+' of '+fmt(DUR));
  var k=Math.min(SENT.length-1,Math.floor(pos/DUR*SENT.length));spans.forEach(function(s,i){s.classList.toggle('on',playing&&i===k||(!playing&&pos>0&&i===k));});}
function loop(ts){if(!playing)return;if(last)pos+=(ts-last)/1000*rate;last=ts;if(pos>=DUR){pos=DUR;set(false);}paint();raf=requestAnimationFrame(loop);}
function set(v){playing=v;pp.innerHTML=v?PAUSE:PLAY;pp.setAttribute('aria-label',v?'Pause':'Play');last=0;if(v){if(pos>=DUR)pos=0;raf=requestAnimationFrame(loop);}else cancelAnimationFrame(raf);paint();}
pp.addEventListener('click',function(){set(!playing);});
seek.addEventListener('input',function(){pos=seek.value/1000*DUR;paint();});
sp.addEventListener('click',function(){rate=rate===1?1.5:rate===1.5?2:1;sp.textContent=rate+'x';sp.setAttribute('aria-label','Playback speed '+rate+' times');});
paint();""")

add(C, "image-upload-preview", "Image Upload with Preview",
    "Add images by button or drag and drop and see thumbnails right away. Checks the file type and size and explains any problem.",
    BASE + """
.drop{margin-top:14px;border:2px dashed var(--line);border-radius:14px;padding:22px;text-align:center;color:var(--muted);transition:border-color .15s,background .15s}
.drop.over{border-color:var(--accent);background:var(--accent-soft)}
.drop svg{color:var(--accent);margin-bottom:6px}.drop p{margin:0 0 10px;font-size:14px}
.thumbs{list-style:none;margin:14px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:10px}
.thumbs li{position:relative;aspect-ratio:1;border-radius:12px;overflow:hidden;border:1px solid var(--line);background:var(--surface-2)}
.thumbs img{width:100%;height:100%;object-fit:cover;display:block}
.thumbs button{position:absolute;top:6px;right:6px;width:26px;height:26px;border-radius:50%;border:0;background:rgba(0,0,0,.65);color:#fff;display:grid;place-items:center;cursor:pointer}
.thumbs small{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.7));color:#fff;font-size:11px;padding:12px 6px 4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.errs{margin:10px 0 0;padding:0;list-style:none;font-size:13px;color:var(--bad)}""",
    f"""<div class="wrap"><div class="card">
  <h2>Add images</h2><p class="muted" style="margin:0">PNG, JPG or WebP, up to 5 MB each, 6 images at most.</p>
  <div class="drop" id="drop">{I['up']}<p>Drag images here, or</p><label class="btn">Choose images<input id="inp" type="file" accept="image/png,image/jpeg,image/webp" multiple hidden></label></div>
  <ul class="errs" id="errs" role="alert"></ul>
  <ul class="thumbs" id="thumbs" aria-label="Selected images"></ul>
</div></div>""", """
var MAX=5*1024*1024,LIMIT=6,TYPES=['image/png','image/jpeg','image/webp'],files=[],drop=document.getElementById('drop'),thumbs=document.getElementById('thumbs'),errs=document.getElementById('errs');
var X='"""+ICON['x'].replace('"', '\\"')+"""';
function render(){thumbs.innerHTML='';files.forEach(function(f,i){var li=document.createElement('li'),img=document.createElement('img');img.src=f.url;img.alt=f.file.name;
  li.appendChild(img);li.insertAdjacentHTML('beforeend','<small></small><button type="button">'+X+'</button>');li.querySelector('small').textContent=f.file.name;
  var b=li.querySelector('button');b.setAttribute('aria-label','Remove '+f.file.name);b.onclick=function(){URL.revokeObjectURL(f.url);files.splice(i,1);render();};thumbs.appendChild(li);});}
function addFiles(list){errs.innerHTML='';[].forEach.call(list,function(f){var why=TYPES.indexOf(f.type)<0?'is not a PNG, JPG or WebP image':f.size>MAX?'is larger than 5 MB':files.length>=LIMIT?'was not added because the limit is 6 images':'';
  if(why){var li=document.createElement('li');li.textContent=f.name+' '+why+'.';errs.appendChild(li);return;}files.push({file:f,url:URL.createObjectURL(f)});});render();}
document.getElementById('inp').addEventListener('change',function(e){addFiles(e.target.files);e.target.value='';});
['dragenter','dragover'].forEach(function(n){drop.addEventListener(n,function(e){e.preventDefault();drop.classList.add('over');});});
['dragleave','drop'].forEach(function(n){drop.addEventListener(n,function(e){e.preventDefault();drop.classList.remove('over');});});
drop.addEventListener('drop',function(e){addFiles(e.dataTransfer.files);});""")

add(C, "drop-overlay-upload", "Page Drop Zone with Upload Progress",
    "Drag files anywhere on the page to show a full screen drop area. Each file then uploads with its own progress bar and a cancel button.",
    BASE + """
.ov{position:fixed;inset:0;background:color-mix(in srgb,var(--accent) 18%,rgba(0,0,0,.35));backdrop-filter:blur(2px);display:grid;place-items:center;z-index:9;pointer-events:none}
.ov div{background:var(--surface);border:2px dashed var(--accent);border-radius:20px;padding:34px 44px;text-align:center;color:var(--ink);font-weight:700;font-size:18px}
.ov svg{color:var(--accent);display:block;margin:0 auto 8px}
ul.up{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
ul.up li{display:grid;grid-template-columns:1fr auto auto;gap:4px 10px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:9px 12px}
ul.up b{font-size:14px;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.bar{grid-column:1/-1;height:6px;border-radius:99px;background:var(--surface-2);overflow:hidden}.bar i{display:block;height:100%;background:var(--accent);transition:width .2s}
li.done .bar i{background:var(--good)}li.cancel{opacity:.55}
.empty{border:1px dashed var(--line);border-radius:12px;padding:18px;text-align:center;font-size:14px;color:var(--muted);margin-top:14px}""",
    f"""<div class="wrap"><div class="card">
  <h2>Files for this chat</h2><p class="muted" style="margin:0">Drag files anywhere on this page, or <label style="color:var(--accent);font-weight:600;cursor:pointer">browse<input id="inp" type="file" multiple hidden></label>.</p>
  <div class="empty" id="empty">No files yet</div><ul class="up" id="up" aria-label="Uploads"></ul>
  <button class="btn sm" type="button" id="demo" style="margin-top:12px">Add sample files</button>
</div></div>
<div class="ov" id="ov" hidden><div>{I['up']}Drop files to add them to the chat</div></div>""", """
var up=document.getElementById('up'),ov=document.getElementById('ov'),empty=document.getElementById('empty'),depth=0;
function size(b){return b<1048576?Math.max(1,Math.round(b/1024))+' KB':(b/1048576).toFixed(1)+' MB';}
// Replace this with your real upload (for example fetch with progress). Here progress is simulated.
function upload(name,bytes){empty.hidden=true;var li=document.createElement('li'),p=0,t;li.innerHTML='<b></b><span class="muted num"></span><div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="100"><i></i></div>';
  li.querySelector('b').textContent=name;var info=li.querySelector('span'),bar=li.querySelector('.bar'),fill=li.querySelector('i'),c=document.createElement('button');c.className='btn sm';c.type='button';c.textContent='Cancel';c.setAttribute('aria-label','Cancel '+name);
  info.after(c);bar.setAttribute('aria-label',name+' upload');
  function show(){fill.style.width=p+'%';bar.setAttribute('aria-valuenow',Math.round(p));info.textContent=Math.round(p)+'% of '+size(bytes);}
  t=setInterval(function(){p=Math.min(100,p+6+Math.random()*14);show();if(p>=100){clearInterval(t);li.className='done';info.textContent='Uploaded, '+size(bytes);c.remove();}},250);
  c.onclick=function(){clearInterval(t);li.className='cancel';info.textContent='Cancelled';c.remove();};up.appendChild(li);show();}
function addFiles(list){[].forEach.call(list,function(f){upload(f.name,f.size);});}
window.addEventListener('dragenter',function(e){if(![].slice.call(e.dataTransfer.types).includes('Files'))return;depth++;ov.hidden=false;});
window.addEventListener('dragleave',function(){depth=Math.max(0,depth-1);if(!depth)ov.hidden=true;});
window.addEventListener('dragover',function(e){e.preventDefault();});
window.addEventListener('drop',function(e){e.preventDefault();depth=0;ov.hidden=true;addFiles(e.dataTransfer.files);});
document.getElementById('inp').addEventListener('change',function(e){addFiles(e.target.files);e.target.value='';});
document.getElementById('demo').addEventListener('click',function(){upload('Quarterly report.pdf',2400000);upload('Team photo.jpg',860000);upload('Budget 2026.xlsx',48000);});""")

add(C, "camera-capture", "Camera Photo Capture",
    "Take a photo with the device camera to ask the AI about it. Shows a live preview, a shutter button and retake, with a clear message if there is no camera.",
    BASE + """
.view{margin-top:14px;position:relative;aspect-ratio:16/10;max-height:50vh;width:100%;border-radius:14px;overflow:hidden;background:#111;display:grid;place-items:center;color:#cfcfd8;text-align:center}
.view video,.view img{width:100%;height:100%;object-fit:cover;display:block;position:absolute;inset:0}
.view p{margin:0;padding:0 24px;font-size:14px;position:relative}
.ctl{display:flex;justify-content:center;gap:10px;margin-top:14px;flex-wrap:wrap}
.shot{width:62px;height:62px;border-radius:50%;border:4px solid var(--surface);outline:3px solid var(--accent);background:var(--accent);cursor:pointer}
.shot:disabled{opacity:.4;cursor:not-allowed}""",
    f"""<div class="wrap"><div class="card">
  <h2>Take a photo</h2><p class="muted" style="margin:0">Point your camera at something and ask about it.</p>
  <div class="view" id="view"><p id="msg">Press Start camera to begin.</p></div>
  <div class="ctl" id="ctl"><button class="btn pri" type="button" id="start">{I['cam']}Start camera</button></div>
  <p class="note warn" id="note" role="status" aria-live="polite" hidden></p>
</div></div>""", """
var view=document.getElementById('view'),ctl=document.getElementById('ctl'),note=document.getElementById('note'),stream=null,video=null;
function msg(t){view.innerHTML='<p></p>';view.firstChild.textContent=t;}
function stop(){if(stream){stream.getTracks().forEach(function(t){t.stop();});stream=null;}}
function controls(html){ctl.innerHTML=html;}
async function start(){note.hidden=true;
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia){note.hidden=false;note.textContent='This browser cannot use the camera. You can upload a photo instead.';return;}
  try{stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment'},audio:false});}
  catch(e){note.hidden=false;note.textContent=e.name==='NotAllowedError'?'Camera access was blocked. Allow it in your browser settings, or upload a photo instead.':'No camera was found on this device. You can upload a photo instead.';return;}
  view.innerHTML='';video=document.createElement('video');video.playsInline=true;video.muted=true;video.srcObject=stream;view.appendChild(video);await video.play();
  controls('<button class="shot" type="button" id="snap" aria-label="Take photo"></button><button class="btn" type="button" id="cancel">Cancel</button>');
  document.getElementById('snap').onclick=snap;document.getElementById('cancel').onclick=function(){stop();msg('Camera stopped.');reset();};}
function snap(){var c=document.createElement('canvas');c.width=video.videoWidth;c.height=video.videoHeight;c.getContext('2d').drawImage(video,0,0);stop();
  var img=document.createElement('img');img.src=c.toDataURL('image/jpeg',.9);img.alt='Photo you just took';view.innerHTML='';view.appendChild(img);
  controls('<button class="btn" type="button" id="re">Retake</button><button class="btn pri" type="button" id="use">Use this photo</button>');
  document.getElementById('re').onclick=start;document.getElementById('use').onclick=function(){note.hidden=false;note.className='note';note.textContent='Photo added to your message.';};}
function reset(){controls('<button class="btn pri" type="button" id="start">"""+I['cam'].replace('"', '\\"')+"""Start camera</button>');document.getElementById('start').onclick=start;}
document.getElementById('start').onclick=start;""")

add(C, "live-transcript", "Live Transcript",
    "Captions that appear as people talk, with speaker names and times. The newest line is highlighted, and the full text can be copied.",
    BASE + """
.wrap{width:min(100%,600px)}
.hd{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.live{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;color:var(--bad)}.live i{width:8px;height:8px;border-radius:50%;background:#dc2626;animation:bl 1.2s infinite}
.live.off{color:var(--muted)}.live.off i{background:var(--muted);animation:none}
@keyframes bl{50%{opacity:.3}}
ol.tr{list-style:none;margin:14px 0 0;padding:0;max-height:300px;overflow-y:auto;display:flex;flex-direction:column;gap:10px}
ol.tr li{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;padding:8px 10px;border-radius:10px;transition:background .3s}
ol.tr li.now{background:var(--accent-soft)}
ol.tr b{font-size:13px;color:var(--ink)}ol.tr time{font-size:12px;color:var(--muted);text-align:right}
ol.tr p{grid-column:1/-1;margin:0;font-size:14.5px;line-height:1.55;color:var(--text)}
.ft{display:flex;gap:8px;margin-top:12px}""",
    """<div class="wrap"><div class="card">
  <div class="hd"><div><h2>Meeting transcript</h2><p class="muted" style="margin:0">Weekly planning</p></div><span class="live" id="live"><i aria-hidden="true"></i><span id="lt">Live</span></span></div>
  <ol class="tr" id="tr" aria-live="polite" aria-label="Transcript"></ol>
  <div class="ft"><button class="btn sm" type="button" id="cp">Copy transcript</button><button class="btn sm" type="button" id="stop">Stop</button></div>
</div></div>""", """
var L=[['Maya','Okay, let us start with the launch date.'],['Ben','Design is ready, but we still need the pricing page.'],['Maya','Can we have it by Thursday?'],['Ben','Yes, if copy is final by Tuesday.'],['Assistant','Summary so far: launch depends on the pricing page, due Thursday. Copy is needed by Tuesday.'],['Maya','Great, let us lock that in.']];
var tr=document.getElementById('tr'),i=0,sec=0,timer,live=document.getElementById('live');
function stamp(s){return Math.floor(s/60)+':'+String(s%60).padStart(2,'0');}
function next(){if(i>=L.length){end();return;}var l=L[i++],li=document.createElement('li');sec+=4+Math.floor(Math.random()*5);
  li.innerHTML='<b></b><time></time><p></p>';li.querySelector('b').textContent=l[0];li.querySelector('time').textContent=stamp(sec);li.querySelector('p').textContent=l[1];
  [].forEach.call(tr.children,function(x){x.classList.remove('now');});li.classList.add('now');tr.appendChild(li);tr.scrollTop=tr.scrollHeight;}
function end(){clearInterval(timer);live.classList.add('off');document.getElementById('lt').textContent='Ended';document.getElementById('stop').disabled=true;}
document.getElementById('stop').addEventListener('click',end);
document.getElementById('cp').addEventListener('click',function(){var text=[].map.call(tr.children,function(li){return li.querySelector('time').textContent+' '+li.querySelector('b').textContent+': '+li.querySelector('p').textContent;}).join(String.fromCharCode(10)),b=this;
  function ok(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy transcript';},1500);}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(text).then(ok,ok);else{var ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}ta.remove();ok();}});
next();timer=setInterval(next,1500);""")

add(C, "voice-settings", "Voice and Speech Settings",
    "Pick a reading voice from the ones in the browser, set the speed and pitch, and hear a preview. Shows a notice when no voices are available.",
    BASE + """
.f{display:flex;flex-direction:column;gap:6px;margin-top:14px}
.f label{display:flex;justify-content:space-between;font-size:13.5px;font-weight:600;color:var(--ink)}
.f label span{color:var(--muted);font-weight:500}
select{border:1px solid var(--line);border-radius:10px;padding:8px 10px;background:var(--surface);color:var(--ink);font-size:14px;width:100%}
input[type=range]{width:100%;accent-color:var(--accent)}
.ft{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}""",
    """<div class="wrap"><div class="card">
  <h2>Reading voice</h2><p class="muted" style="margin:0">Used when the assistant reads answers out loud.</p>
  <div class="f"><label for="v">Voice</label><select id="v"></select></div>
  <div class="f"><label for="r">Speed <span class="num" id="rv">1.0x</span></label><input id="r" type="range" min="0.5" max="2" step="0.1" value="1"></div>
  <div class="f"><label for="p">Pitch <span class="num" id="pv">1.0</span></label><input id="p" type="range" min="0.5" max="1.5" step="0.1" value="1"></div>
  <div class="ft"><button class="btn pri" type="button" id="pre">Play preview</button><span class="muted" id="st" role="status" aria-live="polite"></span></div>
</div></div>""", """
var v=document.getElementById('v'),r=document.getElementById('r'),p=document.getElementById('p'),st=document.getElementById('st'),pre=document.getElementById('pre'),has='speechSynthesis' in window,voices=[];
function load(){voices=has?speechSynthesis.getVoices():[];v.innerHTML='';
  if(!voices.length){var o=document.createElement('option');o.textContent=has?'Default voice':'No voices available';v.appendChild(o);v.disabled=!has;if(!has){pre.disabled=true;st.textContent='Speech is not supported in this browser.';}return;}
  v.disabled=false;voices.forEach(function(x,i){var o=document.createElement('option');o.value=i;o.textContent=x.name+' ('+x.lang+')';if(x.default)o.selected=true;v.appendChild(o);});}
if(has){load();speechSynthesis.addEventListener('voiceschanged',load);}else load();
r.addEventListener('input',function(){document.getElementById('rv').textContent=(+r.value).toFixed(1)+'x';});
p.addEventListener('input',function(){document.getElementById('pv').textContent=(+p.value).toFixed(1);});
pre.addEventListener('click',function(){if(!has)return;if(speechSynthesis.speaking){speechSynthesis.cancel();}
  var u=new SpeechSynthesisUtterance('Hello! This is how I will sound when I read answers to you.');if(voices[v.value])u.voice=voices[v.value];u.rate=+r.value;u.pitch=+p.value;
  u.onstart=function(){st.textContent='Playing preview';};u.onend=function(){st.textContent='';};u.onerror=function(){st.textContent='Could not play the preview.';};speechSynthesis.speak(u);});""")

add(C, "image-prompt-editor", "Image Prompt Builder",
    "Write a prompt for an image and pick a style, shape and number of images. A frame shows the chosen shape, and the final prompt updates live.",
    BASE + """
.wrap{width:min(100%,680px)}
textarea{width:100%;min-height:74px;resize:vertical;border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:var(--surface);color:var(--ink);line-height:1.5;margin-top:12px}
textarea:focus{outline:0;border-color:var(--accent)}
.lbl{font-size:13px;font-weight:700;color:var(--ink);margin:14px 0 6px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips button{border:1.5px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:5px 12px;font-size:13px;cursor:pointer}
.chips button[aria-checked=true]{border-color:var(--accent);background:var(--accent-soft);color:var(--ink);font-weight:700}
.grid2{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:end}
.frame{width:120px;height:120px;display:grid;place-items:center}
.frame i{display:block;border:2px dashed var(--accent);border-radius:8px;background:var(--accent-soft);transition:width .2s,height .2s}
.final{margin-top:14px;padding:10px 12px;border-radius:10px;background:var(--surface-2);font:12.5px/1.55 var(--mono);color:var(--ink);overflow-wrap:anywhere}
.ft{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:14px;flex-wrap:wrap}
select{border:1px solid var(--line);border-radius:10px;padding:7px 10px;background:var(--surface);color:var(--ink)}
@media(max-width:520px){.grid2{grid-template-columns:1fr}.frame{justify-self:center}}""",
    """<div class="wrap"><div class="card">
  <h2><label for="pr">Describe your image</label></h2>
  <textarea id="pr">A cozy reading corner by a rainy window, with a cat asleep on a stack of books</textarea>
  <div class="grid2"><div>
    <div class="lbl" id="sl">Style</div><div class="chips" role="radiogroup" aria-labelledby="sl" id="style"></div>
    <div class="lbl" id="al">Shape</div><div class="chips" role="radiogroup" aria-labelledby="al" id="aspect"></div></div>
    <div class="frame" aria-hidden="true"><i id="fr"></i></div></div>
  <div class="final" id="final" aria-live="polite"></div>
  <div class="ft"><label class="muted">Number of images <select id="n"><option>1</option><option>2</option><option selected>4</option></select></label><button class="btn pri" type="button" id="go">Create images</button></div>
</div></div>""", """
var STYLES=['Photo','Watercolor','3D render','Line art','Pixel art'],ASPECTS=[['Square','1:1',1,1],['Wide','16:9',16,9],['Tall','9:16',9,16],['Photo','4:3',4,3]];
var pr=document.getElementById('pr'),fin=document.getElementById('final'),fr=document.getElementById('fr'),style='Watercolor',aspect=ASPECTS[1];
function group(el,items,cur,label,onPick){items.forEach(function(it){var b=document.createElement('button');b.type='button';b.setAttribute('role','radio');var name=label(it);b.textContent=name;b.setAttribute('aria-checked',name===cur);b.tabIndex=name===cur?0:-1;
  b.onclick=function(){el.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-checked',x===b);x.tabIndex=x===b?0:-1;});onPick(it);render();};
  b.onkeydown=function(e){var bs=[].slice.call(el.children),k=bs.indexOf(b),n=e.key==='ArrowRight'||e.key==='ArrowDown'?bs[(k+1)%bs.length]:e.key==='ArrowLeft'||e.key==='ArrowUp'?bs[(k-1+bs.length)%bs.length]:null;if(n){e.preventDefault();n.focus();n.click();}};el.appendChild(b);});}
group(document.getElementById('style'),STYLES,style,function(s){return s;},function(s){style=s;});
group(document.getElementById('aspect'),ASPECTS,aspect[0]+' '+aspect[1],function(a){return a[0]+' '+a[1];},function(a){aspect=a;});
function render(){var w=aspect[2],h=aspect[3],s=100/Math.max(w,h);fr.style.width=(w*s)+'px';fr.style.height=(h*s)+'px';
  fin.textContent=(pr.value.trim()||'Your description')+', '+style.toLowerCase()+' style, aspect ratio '+aspect[1];}
pr.addEventListener('input',render);
document.getElementById('go').addEventListener('click',function(){this.textContent='Creating '+document.getElementById('n').value+' images...';this.disabled=true;var b=this;setTimeout(function(){b.textContent='Create images';b.disabled=false;},1800);});
render();""")

add(C, "image-generation-progress", "Image Generation Progress",
    "Shows images being created: tiles start blurry and sharpen as progress grows, with a cancel button, then download and upscale actions.",
    BASE + """
.wrap{width:min(100%,640px)}
.hd{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px;margin-top:14px}
.tile{position:relative;aspect-ratio:1;border-radius:14px;overflow:hidden;background:var(--surface-2)}
.tile .art{position:absolute;inset:-10%;transition:filter .4s}
.tile .pct{position:absolute;left:10px;bottom:10px;background:rgba(0,0,0,.6);color:#fff;font-size:12px;font-weight:700;border-radius:99px;padding:2px 9px}
.tile .acts{position:absolute;right:8px;bottom:8px;display:flex;gap:6px}
.tile .acts button{border:0;background:rgba(0,0,0,.65);color:#fff;border-radius:8px;padding:5px 9px;font-size:12px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:4px}
.bar{height:6px;border-radius:99px;background:var(--surface-2);overflow:hidden;margin-top:12px}.bar i{display:block;height:100%;background:var(--accent);transition:width .3s}""",
    """<div class="wrap"><div class="card">
  <div class="hd"><div><h2>Creating 4 images</h2><p class="muted" style="margin:0" id="st" role="status" aria-live="polite">Starting</p></div><button class="btn sm" type="button" id="cx">Cancel</button></div>
  <div class="bar" role="progressbar" aria-label="Overall progress" aria-valuemin="0" aria-valuemax="100" id="pb"><i id="bi"></i></div>
  <div class="tiles" id="tiles"></div>
</div></div>""", """
// Placeholder art made with CSS gradients. Replace with your generated image URLs.
var ART=['radial-gradient(circle at 30% 30%,#fde68a,transparent 40%),linear-gradient(160deg,#1e3a8a,#7c3aed 60%,#f472b6)','radial-gradient(circle at 70% 40%,#a7f3d0,transparent 45%),linear-gradient(200deg,#064e3b,#0ea5e9)',
'radial-gradient(circle at 50% 70%,#fecaca,transparent 40%),linear-gradient(120deg,#7c2d12,#f59e0b 55%,#fde68a)','radial-gradient(circle at 40% 50%,#e0e7ff,transparent 35%),linear-gradient(90deg,#111827,#4b5563 50%,#9ca3af)'];
var tiles=document.getElementById('tiles'),st=document.getElementById('st'),bi=document.getElementById('bi'),pb=document.getElementById('pb'),cx=document.getElementById('cx'),p=ART.map(function(){return 0;}),timer;
var DL='"""+I['dl'].replace('"', '\\"')+"""';
ART.forEach(function(a,i){var t=document.createElement('div');t.className='tile';t.setAttribute('role','img');t.setAttribute('aria-label','Image '+(i+1)+' in progress');t.innerHTML='<div class="art"></div><span class="pct">0%</span>';t.querySelector('.art').style.background=a;tiles.appendChild(t);});
var els=[].slice.call(tiles.children);
function paint(){var avg=p.reduce(function(a,b){return a+b;},0)/p.length;bi.style.width=avg+'%';pb.setAttribute('aria-valuenow',Math.round(avg));
  els.forEach(function(t,i){t.querySelector('.art').style.filter='blur('+Math.round((100-p[i])/5)+'px) saturate('+(0.4+p[i]/160)+')';var pc=t.querySelector('.pct');if(pc)pc.textContent=Math.round(p[i])+'%';});
  st.textContent=avg<100?(avg<30?'Sketching shapes':avg<70?'Adding color and light':'Sharpening details')+', '+Math.round(avg)+'%':'Done. Your images are ready.';}
function finish(){clearInterval(timer);cx.hidden=true;els.forEach(function(t,i){t.setAttribute('aria-label','Generated image '+(i+1));var pc=t.querySelector('.pct');if(pc)pc.remove();
  t.insertAdjacentHTML('beforeend','<div class="acts"><button type="button">'+DL+'Save</button><button type="button">Upscale</button></div>');});}
timer=setInterval(function(){p=p.map(function(v,i){return Math.min(100,v+3+Math.random()*7+i*.5);});paint();if(p.every(function(v){return v>=100;}))finish();},300);
cx.addEventListener('click',function(){clearInterval(timer);st.textContent='Cancelled. No images were saved.';cx.hidden=true;});
paint();""")
