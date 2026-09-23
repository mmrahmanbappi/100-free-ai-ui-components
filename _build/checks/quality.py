"""Quality checks for every component: hidden elements, text contrast (WCAG AA) and phone width.
Run: python3 _build/checks/quality.py"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HIDDEN = "[...document.querySelectorAll('[hidden]')].filter(e=>e.getBoundingClientRect().height>0).map(e=>e.id||e.className)"
CONTRAST = r"""(()=>{
function rgb(s){const m=s.match(/[\d.]+/g);if(!m)return null;let v=m.map(Number);
  if(s.startsWith('color('))v=v.slice(0,3).map(x=>x*255).concat(v.length>3?[v[3]]:[1]);return v}
function lum(c){const a=c.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
function bg(e){while(e){const c=getComputedStyle(e).backgroundColor,r=rgb(c);if(r&&(r.length<4||r[3]>0.5))return r;e=e.parentElement}return[255,255,255]}
const bad=[];for(const e of document.querySelectorAll('body *')){
  if(e.closest('.sr'))continue;if(![...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))continue;
  const cs=getComputedStyle(e),box=e.getBoundingClientRect();if(cs.visibility==='hidden'||box.height===0||box.width<=1||+cs.opacity<.5)continue;
  if(cs.webkitTextFillColor&&cs.webkitTextFillColor.includes('0)'))continue;
  const f=rgb(cs.color),b=bg(e),r=(Math.max(lum(f),lum(b))+.05)/(Math.min(lum(f),lum(b))+.05);
  const big=parseFloat(cs.fontSize)>=18.5||(parseFloat(cs.fontSize)>=14&&+cs.fontWeight>=700);
  if(r<(big?3:4.5))bad.push((e.className||e.tagName)+' '+r.toFixed(2)+' "'+e.textContent.trim().slice(0,24)+'"')}
return bad.slice(0,4)})()"""


def run():
    files = sorted(glob.glob(os.path.join(ROOT, "*", "*", "component.html")))
    problems = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        for theme in ("light", "dark"):
            pg = b.new_page(color_scheme=theme)
            for f in files:
                pg.goto("file://" + f, wait_until="load")
                pg.wait_for_timeout(80)
                h, c = pg.evaluate(HIDDEN), pg.evaluate(CONTRAST)
                if h or c:
                    problems += 1
                    print(theme, f.split(os.sep)[-2], "| shown but hidden:", h, "| low contrast:", c)
            pg.close()
        m = b.new_page(viewport={"width": 390, "height": 844})
        for f in files:
            m.goto("file://" + f, wait_until="load")
            if m.evaluate("document.documentElement.scrollWidth") > 392:
                problems += 1
                print("phone: too wide", f.split(os.sep)[-2])
        b.close()
    print(f"checked {len(files)} components in light, dark and phone width: {problems} problems")
    return problems


if __name__ == "__main__":
    sys.exit(1 if run() else 0)
