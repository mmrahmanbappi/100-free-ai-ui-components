"""Screenshots of every component, with a short set-up so the picture shows it in use."""
import glob
import os
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGE = {
    "basic-prompt-box": "q=document.getElementById('q');q.value='Write a short thank you note to my team for finishing the project early';q.dispatchEvent(new Event('input'))",
    "auto-grow-prompt": "q=document.getElementById('q');q.value='Here is my plan for the launch:\\n1. Finish the landing page\\n2. Record a short demo video\\n3. Email the waiting list';q.dispatchEvent(new Event('input'))",
    "prompt-with-attachments": "var dt=new DataTransfer();dt.items.add(new File([new Uint8Array(248000)],'q3-report.pdf'));dt.items.add(new File([new Uint8Array(12000)],'sales.csv'));var i=document.getElementById('file');i.files=dt.files;i.dispatchEvent(new Event('change'));q=document.getElementById('q');q.value='Compare these two files and list the main differences';q.dispatchEvent(new Event('input'))",
    "voice-input-prompt": "document.getElementById('mic').click()",
    "slash-commands-prompt": "q=document.getElementById('q');q.focus();q.value='/';q.selectionStart=q.selectionEnd=1;q.dispatchEvent(new Event('input'))",
    "model-picker-prompt": "document.getElementById('pb').click()",
    "prompt-token-counter": "q=document.getElementById('q');q.value='Please review this contract and point out anything unusual. '.repeat(40);q.dispatchEvent(new Event('input'))",
    "send-shortcut-prompt": "q=document.getElementById('q');q.value='Can you help me plan a birthday party for 20 people?';q.dispatchEvent(new Event('input'))",
}


# How long to wait before the picture, so animated components are caught mid-way
WAIT = {"streaming-text": 1900, "reasoning-panel": 2300, "agent-progress-steps": 2500, "status-spinner": 1700,
        "tool-call-indicator": 2100, "stop-generating": 2000, "thinking-shimmer": 700}
STAGE["inline-citations"] = "document.querySelector('.cite button[aria-describedby=p2]').focus()"
STAGE["edit-message"] = "document.getElementById('eb').click()"
STAGE["answer-versions"] = "document.getElementById('re').click()"
WAIT["answer-versions"] = 1000
STAGE["thumbs-feedback"] = "document.querySelector('[data-v=up]').click()"
STAGE["thumbs-down-reasons"] = "document.getElementById('dn').click();document.querySelectorAll('.chip')[0].click();document.querySelectorAll('.chip')[2].click();document.activeElement.blur()"
STAGE["star-rating"] = "var i=document.getElementById('s4');i.checked=true;i.dispatchEvent(new Event('change'))"
STAGE["compare-answers"] = "document.querySelector('.choices [data-v=A]').click()"
STAGE["report-dialog"] = "document.getElementById('open').click();document.querySelector('input[value=wrong]').checked=true;document.activeElement.blur()"
STAGE["satisfaction-scale"] = "var i=document.getElementById('f4');i.checked=true;i.dispatchEvent(new Event('change'))"
STAGE["rewrite-options"] = "document.getElementById('tg').click();document.activeElement.blur()"
STAGE["feedback-toast"] = "document.querySelector('[data-v=up]').click()"
WAIT["feedback-toast"] = 700
STAGE["usage-chart"] = "document.querySelectorAll('.chart button')[10].focus()"
STAGE["message-cost"] = "document.querySelector('details.cost').open=true"
STAGE["language-picker"] = "var q=document.getElementById('q');q.focus();q.value='a';q.dispatchEvent(new Event('input'))"
STAGE["system-prompt-editor"] = "var t=document.getElementById('ta');t.value+=' Use examples from everyday life.';t.dispatchEvent(new Event('input'))"
STAGE["floating-chat-widget"] = "document.getElementById('fab').click();document.activeElement.blur()"
STAGE["chat-item-menu"] = "document.querySelectorAll('#list .ib')[1].click()"
STAGE["share-dialog"] = "document.getElementById('open').click();var r=document.querySelector('input[value=link]');r.checked=true;r.dispatchEvent(new Event('change'));document.activeElement.blur()"
STAGE["conversation-search"] = "var q=document.getElementById('q');q.value='plan';q.dispatchEvent(new Event('input'))"
STAGE["tool-call-card"] = "document.getElementById('t1').open=true"
STAGE["task-plan"] = "document.getElementById('go').click()"
WAIT["task-plan"] = 1500
WAIT["run-log-console"] = 3200
WAIT["subagent-grid"] = 2200
STAGE["voice-recorder"] = "document.getElementById('mic').click()"
WAIT["voice-recorder"] = 1400
WAIT["voice-mode"] = 900
STAGE["audio-answer-player"] = "document.getElementById('pp').click()"
WAIT["audio-answer-player"] = 6500
STAGE["image-upload-preview"] = "var dt=new DataTransfer();[['#f59e0b','#be123c','Sunset.png'],['#0ea5e9','#1e3a8a','Lake.png'],['#84cc16','#166534','Forest.png']].forEach(function(c){var cv=document.createElement('canvas');cv.width=cv.height=120;var g=cv.getContext('2d'),gr=g.createLinearGradient(0,0,120,120);gr.addColorStop(0,c[0]);gr.addColorStop(1,c[1]);g.fillStyle=gr;g.fillRect(0,0,120,120);var b=atob(cv.toDataURL('image/png').split(',')[1]),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);dt.items.add(new File([u],c[2],{type:'image/png'}));});var inp=document.getElementById('inp');inp.files=dt.files;inp.dispatchEvent(new Event('change'))"
STAGE["drop-overlay-upload"] = "document.getElementById('demo').click()"
WAIT["drop-overlay-upload"] = 1000
WAIT["live-transcript"] = 4700
WAIT["image-generation-progress"] = 2600
STAGE["onboarding-tour"] = "document.getElementById('start').click()"
WAIT["onboarding-tour"] = 600
STAGE["keyboard-shortcuts"] = "document.getElementById('open').click();document.activeElement.blur()"
STAGE["whats-new-dialog"] = "document.getElementById('open').click();document.activeElement.blur()"
STAGE["fact-check-panel"] = "document.querySelectorAll('details')[2].open=true"
STAGE["ai-generated-label"] = "document.querySelector('.lab button').focus()"
STAGE["ai-orb"] = "document.querySelector('[data-s=listen]').click()"


def main(only=None):
    files = sorted(glob.glob(os.path.join(ROOT, "*", "*", "component.html")))
    if only:
        files = [f for f in files if os.path.basename(os.path.dirname(f)) in only or f.split(os.sep)[-3] in only]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for theme in ("light", "dark"):
            pg = b.new_page(viewport={"width": 760, "height": 475}, color_scheme=theme)
            for f in files:
                d = os.path.dirname(f)
                slug = os.path.basename(d)
                pg.goto("file://" + f, wait_until="load")
                if slug in STAGE:
                    pg.evaluate("(()=>{var q;" + STAGE[slug] + "})()")
                pg.wait_for_timeout(WAIT.get(slug, 450))
                out = os.path.join(d, "screenshot.png" if theme == "light" else "screenshot-dark.png")
                pg.screenshot(path=out)
                im = Image.open(out).convert("RGB")
                im.save(out, optimize=True)
                if theme == "light":
                    im.resize((640, 400), Image.LANCZOS).save(os.path.join(d, "thumb.webp"), "WEBP", quality=82, method=6)
            pg.close()
        b.close()
    print("screenshots:", len(files))


if __name__ == "__main__":
    main(sys.argv[1:] or None)
