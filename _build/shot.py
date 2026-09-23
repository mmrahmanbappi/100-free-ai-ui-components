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
