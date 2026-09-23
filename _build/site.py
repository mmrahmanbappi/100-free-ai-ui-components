"""Builds the website: home page, category pages, one detail page per component, README and sitemap."""
import json
import os
import sys
from datetime import date

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402
import gen  # noqa: E402,F401  (loads the component modules)
from core import CATEGORIES, REPO, SITE, esc  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
COMPS = core.COMPONENTS
BUILT = [c for c in CATEGORIES if any(x["category"] == c[0] for x in COMPS)]
PERSON = {"@type": "Person", "@id": SITE + "/#author", "name": "MM Rahman Bappi", "url": "https://mmseo.app/",
          "sameAs": ["https://github.com/mmrahmanbappi"]}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "100 Free AI UI Components",
           "inLanguage": "en", "publisher": {"@id": SITE + "/#author"}}


def cat(cid):
    return next(c for c in CATEGORIES if c[0] == cid)


CSS = """
:root{--bg:#fafafb;--card:#fff;--ink:#17171c;--text:#34343e;--muted:#63636f;--line:#e5e5ea;--acc:#5b5bd6;--acc-soft:#ececfc;--code:#f4f4f7}
@media (prefers-color-scheme:dark){:root{--bg:#111116;--card:#1a1a21;--ink:#f3f3f6;--text:#d6d6de;--muted:#9c9caa;--line:#2d2d37;--acc:#8b8bff;--acc-soft:#25254a;--code:#15151b}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1.05rem/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,sans-serif}
a{color:var(--acc);text-underline-offset:3px}:focus-visible{outline:3px solid var(--acc);outline-offset:3px;border-radius:4px}
img{max-width:100%;height:auto;display:block}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:var(--ink);color:var(--bg);padding:.5rem 1rem;z-index:9}
.wrap{max-width:76rem;margin:0 auto;padding-left:1.25rem;padding-right:1.25rem}.narrow{max-width:48rem}
header.top{border-bottom:1px solid var(--line)}header.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;min-height:4rem}
.brand{font-weight:800;color:var(--ink);text-decoration:none}.brand b{color:var(--acc)}
header nav{display:flex;gap:1.3rem;flex-wrap:wrap;font-size:1rem}header nav a{color:var(--text);text-decoration:none}header nav a:hover{color:var(--acc)}
h1,h2,h3{color:var(--ink);line-height:1.2;letter-spacing:-.015em}h1{font-size:clamp(2.1rem,5vw,3.4rem);margin:.3rem 0 1rem}h2{font-size:clamp(1.4rem,3vw,1.9rem);margin:0 0 1rem}h3{font-size:1.08rem;margin:0 0 .3rem}
p{margin:0 0 1.1rem}.lead{font-size:1.2rem;max-width:44rem}.small{font-size:.95rem;color:var(--muted)}
.hero{padding:3rem 0 2rem}.crumbs{font-size:.95rem;color:var(--muted);padding-top:1.4rem}.crumbs a{color:var(--muted)}
.actions{display:flex;gap:.7rem;flex-wrap:wrap;margin:1.2rem 0 .4rem}
.btn{display:inline-flex;align-items:center;gap:.4rem;padding:.7rem 1.15rem;border-radius:10px;font-weight:700;text-decoration:none;border:2px solid var(--ink);background:none;color:var(--ink);cursor:pointer;font-size:1rem}
.btn.main{background:var(--ink);color:var(--bg)}.btn:hover{border-color:var(--acc)}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.4rem 0}
.chips button,.chips a{font:inherit;font-size:.95rem;padding:.42rem .9rem;border-radius:999px;border:1.5px solid var(--line);background:var(--card);color:var(--text);cursor:pointer;text-decoration:none}
.chips button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.grid{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(17.5rem,1fr));gap:1.3rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;height:100%}
.card img{aspect-ratio:16/10;object-fit:cover;width:100%;border-bottom:1px solid var(--line)}
.card .in{padding:1rem 1.1rem 1.15rem;display:flex;flex-direction:column;gap:.3rem;flex:1}
.card .cat{font-size:.85rem;color:var(--acc);font-weight:600;text-decoration:none}.card h3 a{color:var(--ink);text-decoration:none}.card h3 a:hover{color:var(--acc)}
.card p{font-size:.95rem;color:var(--muted);margin:0;flex:1}
section.band{padding:3rem 0;border-top:1px solid var(--line)}section.band.alt{background:var(--card)}
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:1rem;list-style:none;padding:0;margin:0}
.cats li>*{display:block;padding:1.1rem 1.2rem;border:1px solid var(--line);border-radius:12px;background:var(--bg);text-decoration:none;color:inherit;height:100%}
.cats a:hover{border-color:var(--acc)}.cats b{color:var(--ink)}.cats span{display:block;color:var(--muted);font-size:.95rem}.cats .soon{opacity:.65}
details{border-bottom:1px solid var(--line);padding:1rem 0}summary{font-weight:700;color:var(--ink);cursor:pointer}details p{margin:.7rem 0 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem}ul.ticks{padding-left:1.2rem}ul.ticks li{margin:.35rem 0}
.stage{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--card)}
.stage .bar{display:flex;justify-content:space-between;align-items:center;gap:.6rem;flex-wrap:wrap;padding:.6rem .8rem;border-bottom:1px solid var(--line)}
.seg{display:flex;border:1.5px solid var(--line);border-radius:10px;overflow:hidden}.seg button{border:0;background:none;padding:.35rem .8rem;font:inherit;font-size:.9rem;color:var(--text);cursor:pointer}
.seg button[aria-pressed=true]{background:var(--acc-soft);color:var(--ink);font-weight:700}
.stage iframe{display:block;width:100%;height:480px;border:0;background:#fff}
.code{position:relative;margin:1.2rem 0}.code pre{background:var(--code);border:1px solid var(--line);border-radius:12px;padding:1rem 1.1rem;max-height:420px;overflow:auto;font:13px/1.55 ui-monospace,"Cascadia Code",Menlo,Consolas,monospace;margin:0;white-space:pre}
.code .copy{position:absolute;top:.6rem;right:.8rem}
footer{border-top:1px solid var(--line);padding:2rem 0;color:var(--muted);font-size:.95rem}footer .wrap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}footer p{margin:0}
@media (max-width:860px){.two{grid-template-columns:1fr}.stage iframe{height:520px}}
"""


def shell(title, desc, path, og, schema, body, script="", ogtype="website"):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="MM Rahman Bappi">
<meta name="theme-color" content="#5b5bd6">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="100 Free AI UI Components">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:alt" content="{esc(title)}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
<meta name="twitter:image:alt" content="{esc(title)}">
<link rel="icon" href="{SITE}/_site/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{SITE}/_site/site.css">
<script type="application/ld+json">
{json.dumps(schema, indent=1, ensure_ascii=False)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap"><a class="brand" href="{SITE}/">100 Free <b>AI UI</b> Components</a>
<nav aria-label="Main"><a href="{SITE}/#components">Components</a><a href="{SITE}/#categories">Categories</a><a href="{SITE}/#faq">FAQ</a><a href="{REPO}">GitHub</a></nav></div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap"><p>Made by <a href="https://mmseo.app/">MM Rahman Bappi</a>. Free under the MIT license.</p><p><a href="{REPO}">Source on GitHub</a></p></div></footer>
{('<script>' + script + '</script>') if script else ''}
</body>
</html>
"""


def url_of(c):
    return f"{SITE}/{c['category']}/{c['slug']}/"


def card(c, show_cat=True):
    catl = f'<a class="cat" href="{SITE}/{c["category"]}/">{esc(cat(c["category"])[1])}</a>' if show_cat else ""
    return (f'<li class="card" data-cat="{c["category"]}"><a href="{url_of(c)}" tabindex="-1" aria-hidden="true"><img src="{url_of(c)}thumb.webp" '
            f'alt="{esc(c["name"])} AI UI component preview" width="640" height="400" loading="lazy"></a>'
            f'<div class="in">{catl}<h3><a href="{url_of(c)}">{esc(c["name"])}</a></h3><p>{esc(c["blurb"])}</p></div></li>')


def og_image(name, title, sub, shots):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (250, 250, 251))
    d = ImageDraw.Draw(im)
    bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
    reg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    d.rectangle([0, 0, W, 12], fill=(91, 91, 214))
    d.text((60, 58), title, font=bold, fill=(23, 23, 28))
    d.text((62, 140), sub, font=reg, fill=(99, 99, 111))
    for i, f in enumerate(shots[:6]):
        t = Image.open(f).convert("RGB").resize((340, 212), Image.LANCZOS)
        x, y = 60 + (i % 3) * 370, 210 + (i // 3) * 205
        if y + 212 > H - 8:
            t = t.crop((0, 0, 340, H - 8 - y))
        im.paste(t, (x, y))
        d.rectangle([x, y, x + 339, y + t.size[1] - 1], outline=(222, 222, 228), width=2)
    im.save(os.path.join(ROOT, "_site", f"og-{name}.jpg"), "JPEG", quality=85, optimize=True)


FAQ = [
    ("Are these AI UI components free?", "Yes. Every component is free for personal and commercial projects under the MIT license, including client work."),
    ("Do they need React or a UI library?", "No. Each component is one HTML file with plain CSS and JavaScript. You can paste it into any site, or move the markup into React, Vue or Svelte."),
    ("Do they connect to an AI model?", "No. They are the interface only. The demos use sample text so you can see how they behave, and you connect them to the AI service you use."),
    ("Do they work in dark mode and on phones?", "Yes. Every component follows the light or dark setting of the device and adjusts to small screens."),
    ("Can I change the colors?", "Yes. All colors are CSS variables at the top of the file. Change --accent to your brand color and the component follows."),
]


def build():
    os.makedirs(os.path.join(ROOT, "_site"), exist_ok=True)
    open(os.path.join(ROOT, "_site", "site.css"), "w").write(CSS.strip() + "\n")
    open(os.path.join(ROOT, "_site", "favicon.svg"), "w").write(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#5b5bd6'/>"
        "<path d='M32 12l4.5 15.5L52 32l-15.5 4.5L32 52l-4.5-15.5L12 32l15.5-4.5z' fill='white'/></svg>\n")
    shot = lambda c: os.path.join(ROOT, c["category"], c["slug"], "screenshot.png")
    n = len(COMPS)

    # ---------- detail pages ----------
    for c in COMPS:
        cid, cname, cdesc = cat(c["category"])
        url = url_of(c)
        code = open(os.path.join(ROOT, c["category"], c["slug"], "component.html")).read()
        title = f"{c['name']}: Free AI UI Component (HTML, CSS, JS)"
        if len(title) > 60:
            title = f"{c['name']}: Free AI UI Component"
        if len(title) > 60:
            title = c["name"][:52] + ", Free"
        desc = c["blurb"]
        if len(desc) < 120:
            desc += " Free HTML, CSS and JavaScript."
        if len(desc) > 158:
            desc = desc[:155].rsplit(" ", 1)[0] + "."
        related = [x for x in COMPS if x["category"] == c["category"] and x["slug"] != c["slug"]][:6]
        schema = {"@context": "https://schema.org", "@graph": [WEBSITE, PERSON,
            {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"},
             "breadcrumb": {"@id": url + "#breadcrumb"}, "primaryImageOfPage": url + "screenshot.png", "inLanguage": "en", "dateModified": TODAY},
            {"@type": "SoftwareSourceCode", "@id": url + "#code", "name": c["name"], "description": c["blurb"], "url": url,
             "codeRepository": f"{REPO}/tree/main/{c['category']}/{c['slug']}", "programmingLanguage": ["HTML", "CSS", "JavaScript"],
             "license": "https://opensource.org/licenses/MIT", "isAccessibleForFree": True, "image": url + "screenshot.png",
             "author": {"@id": SITE + "/#author"}, "dateModified": TODAY},
            {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "AI UI components", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": cname, "item": f"{SITE}/{cid}/"},
                {"@type": "ListItem", "position": 3, "name": c["name"], "item": url}]}]}
        body = f"""<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{SITE}/">AI UI components</a> / <a href="{SITE}/{cid}/">{esc(cname)}</a> / <span aria-current="page">{esc(c['name'])}</span></nav></div>
<section class="hero" style="padding-top:1.2rem"><div class="wrap">
<h1>{esc(c['name'])}</h1>
<p class="lead">{esc(c['blurb'])}</p>
<div class="actions"><button class="btn main" type="button" data-copy>Copy the code</button><a class="btn" href="component.html" download="{c['slug']}.html">Download the file</a><a class="btn" href="component.html">Open full screen</a></div>
<p class="small">One HTML file with the CSS and JavaScript inside. No library needed. MIT license.</p>
<div class="stage"><div class="bar"><strong style="color:var(--ink)">Live preview</strong><div class="seg" role="group" aria-label="Preview theme"><button type="button" data-t="light" aria-pressed="true">Light</button><button type="button" data-t="dark" aria-pressed="false">Dark</button></div></div>
<iframe id="pv" src="component.html?theme=light" title="{esc(c['name'])} live preview" loading="lazy"></iframe></div>
</div></section>
<section class="band alt"><div class="wrap two">
<div><h2>How to use it</h2><ol class="ticks">
<li>Click <b>Copy the code</b>, or download the file.</li>
<li>Paste the CSS into your stylesheet, the HTML where you want the component, and the script before the closing body tag.</li>
<li>Change <code>--accent</code> at the top of the CSS to your brand color, then connect the events to your AI service.</li>
</ol></div>
<div><h2>What you get</h2><ul class="ticks">
<li>Works in light and dark mode automatically</li>
<li>Keyboard friendly, with labels for screen readers</li>
<li>Fits phones, tablets and desktops</li>
<li>Respects the reduced motion setting</li>
<li>No framework, so it works with any stack</li>
</ul></div>
</div></section>
<section class="band"><div class="wrap"><h2>The code</h2>
<div class="code"><button class="btn copy" type="button" data-copy>Copy</button><pre id="src"><code>{esc(code)}</code></pre></div>
</div></section>
{f'<section class="band alt"><div class="wrap"><h2>More {esc(cname.lower())} components</h2><ul class="grid">{"".join(card(x, False) for x in related)}</ul></div></section>' if related else ''}"""
        script = """document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){var t=document.getElementById('src').innerText;
navigator.clipboard.writeText(t).then(function(){var o=b.textContent;b.textContent='Copied';setTimeout(function(){b.textContent=o},1500)})})});
var sb=[].slice.call(document.querySelectorAll('.seg button')),pv=document.getElementById('pv');sb.forEach(function(b){b.addEventListener('click',function(){
sb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});pv.src='component.html?theme='+b.dataset.t;})});"""
        open(os.path.join(ROOT, c["category"], c["slug"], "index.html"), "w").write(
            shell(title, desc, f"/{c['category']}/{c['slug']}/", url + "screenshot.png", schema, body, script, "article"))

    # ---------- category pages ----------
    for cid, cname, cdesc in BUILT:
        items = [x for x in COMPS if x["category"] == cid]
        og_image(cid, f"{cname} components", f"{len(items)} free AI UI components in HTML, CSS and JavaScript", [shot(x) for x in items])
        t = f"{len(items)} Free {cname} Components for AI Apps"
        if len(t) > 60:
            t = f"Free {cname} Components for AI Apps"
        d = f"{len(items)} free {cname.lower()} components for AI chat apps. {cdesc} Copy the code or download one file."
        if len(d) > 158:
            d = f"{len(items)} free {cname.lower()} components for AI apps. Live demo, light and dark mode, copy the code or download one file."
        url = f"{SITE}/{cid}/"
        schema = {"@context": "https://schema.org", "@graph": [WEBSITE, PERSON,
            {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": t, "description": d, "isPartOf": {"@id": SITE + "/#website"},
             "breadcrumb": {"@id": url + "#breadcrumb"}, "primaryImageOfPage": f"{SITE}/_site/og-{cid}.jpg", "inLanguage": "en", "dateModified": TODAY,
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "url": url_of(x), "name": x["name"]} for i, x in enumerate(items)]}},
            {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "AI UI components", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": cname, "item": url}]}]}
        body = f"""<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{SITE}/">AI UI components</a> / <span aria-current="page">{esc(cname)}</span></nav></div>
<section class="hero"><div class="wrap"><h1>{esc(cname)} components</h1><p class="lead">{esc(cdesc)} Each one is a single HTML file with a live demo.</p></div></section>
<section class="band alt"><div class="wrap"><ul class="grid">{"".join(card(x, False) for x in items)}</ul></div></section>"""
        os.makedirs(os.path.join(ROOT, cid), exist_ok=True)
        open(os.path.join(ROOT, cid, "index.html"), "w").write(shell(t, d, f"/{cid}/", f"{SITE}/_site/og-{cid}.jpg", schema, body))

    # ---------- home ----------
    og_image("home", "Free AI UI components", "Prompt boxes, thinking states, token meters and more", [shot(x) for x in COMPS[:6]])
    title = "Free AI UI Components: Chat, Prompt and Token UI in HTML"
    desc = "Free AI UI components for chat apps: prompt boxes, thinking animations, token meters and answer ratings. One HTML file each, no library, MIT license."
    schema = {"@context": "https://schema.org", "@graph": [WEBSITE, PERSON,
        {"@type": "CollectionPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"},
         "author": {"@id": SITE + "/#author"}, "dateModified": TODAY, "primaryImageOfPage": SITE + "/_site/og-home.jpg",
         "mainEntity": {"@type": "ItemList", "numberOfItems": n, "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": url_of(x), "name": x["name"]} for i, x in enumerate(COMPS)]}},
        {"@type": "FAQPage", "@id": SITE + "/#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
    chips = '<button type="button" aria-pressed="true" data-f="all">All</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{c[0]}">{esc(c[1])}</button>' for c in BUILT)
    cats = "".join((f'<li><a href="{SITE}/{c[0]}/"><b>{esc(c[1])}</b><span>{esc(c[2])}</span></a></li>' if c in BUILT
                    else f'<li><div class="soon"><b>{esc(c[1])}</b><span>{esc(c[2])} Coming soon.</span></div></li>') for c in CATEGORIES)
    status = "All 100 components are ready." if n >= 100 else f"{n} of 100 components are ready. New ones are added every week."
    body = f"""<section class="hero"><div class="wrap">
<h1>Free AI UI components</h1>
<p class="lead">The parts every AI app needs: a prompt box, a thinking state, a token meter, a way to rate answers. Each component is one HTML file you can copy into any project. No library, no build step.</p>
<div class="actions"><a class="btn main" href="#components">Browse components</a><a class="btn" href="{REPO}">Get the code on GitHub</a></div>
<p class="small">{status} Free for personal and business use.</p>
</div></section>
<section class="band alt" id="components"><div class="wrap"><h2>All components</h2>
<p>Open a component to try the live demo, switch between light and dark mode, and copy the code.</p>
<div class="chips" role="group" aria-label="Filter by category">{chips}</div>
<ul class="grid" id="grid">{"".join(card(x) for x in COMPS)}</ul></div></section>
<section class="band" id="categories"><div class="wrap"><h2>Categories</h2><ul class="cats">{cats}</ul></div></section>
<section class="band alt"><div class="wrap two">
<div><h2>Why these components</h2><p>AI tools are easy to connect, but the interface around them takes time. People expect to paste files, see that the AI is working, know how much a chat costs and tell you when an answer was wrong.</p><p>These components give you those pieces, tested and ready, so you can spend your time on the product.</p></div>
<div><h2>Every component includes</h2><ul class="ticks"><li>Plain HTML, CSS and JavaScript in one file</li><li>Light and dark mode</li><li>Keyboard support and screen reader labels</li><li>A layout that fits phones</li><li>Brand colors you can change in one line</li></ul></div>
</div></section>
<section class="band" id="faq"><div class="wrap narrow"><h2>Questions</h2>{"".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in FAQ)}</div></section>"""
    script = """var b=[].slice.call(document.querySelectorAll('.chips button')),c=[].slice.call(document.querySelectorAll('#grid .card'));
b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.setAttribute('aria-pressed',y===x)});var f=x.dataset.f;c.forEach(function(k){k.hidden=f!=='all'&&k.dataset.cat!==f})})});"""
    open(os.path.join(ROOT, "index.html"), "w").write(shell(title, desc, "/", SITE + "/_site/og-home.jpg", schema, body, script))

    # ---------- 404, sitemap, robots, README ----------
    open(os.path.join(ROOT, "404.html"), "w").write(shell("Page not found | 100 Free AI UI Components", "This page does not exist.", "/404.html", SITE + "/_site/og-home.jpg",
        {"@context": "https://schema.org", "@type": "WebPage", "name": "Page not found"},
        f'<section class="hero"><div class="wrap narrow"><h1>Page not found</h1><p class="lead">This page does not exist or has moved.</p><div class="actions"><a class="btn main" href="{SITE}/">See all components</a></div></div></section>').replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex, follow">'))
    urls = [(SITE + "/", None)] + [(f"{SITE}/{c[0]}/", None) for c in BUILT] + [(url_of(x), url_of(x) + "screenshot.png") for x in COMPS]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        + "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n" + (f"    <image:image><image:loc>{im}</image:loc></image:image>\n" if im else "") + "  </url>\n" for u, im in urls)
        + "</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    rows = []
    for cid, cname, cdesc in BUILT:
        rows.append(f"\n### {cname}\n\n{cdesc}\n\n| Preview | Component |\n|---|---|")
        for x in [c for c in COMPS if c["category"] == cid]:
            rows.append(f"| [![{x['name']}]({cid}/{x['slug']}/thumb.webp)]({url_of(x)}) | **[{x['name']}]({url_of(x)})**<br>{x['blurb']} |")
    coming = [c[1] for c in CATEGORIES if c not in BUILT]
    readme = f"""# 100 Free AI UI Components

![Free AI UI components](_site/og-home.jpg)

The parts every AI app needs: prompt boxes, thinking animations, token meters, answer ratings, agent tool calls and more. Each component is one HTML file with plain CSS and JavaScript. No library, no build step.

**[See every component with a live demo]({SITE}/)**

{status}

## Why use these components

- **One file each.** Copy it into any site, or move the markup into React, Vue or Svelte.
- **Light and dark mode.** Follows the device setting automatically.
- **Accessible.** Keyboard support and labels for screen readers.
- **Works on phones.** Every component fits small screens.
- **Easy to rebrand.** Change `--accent` at the top of the CSS.
- **Free for business use.** MIT license.

## How to use a component

1. Open the [website]({SITE}/) and pick a component.
2. Try the live demo in light and dark mode.
3. Click **Copy the code** or **Download the file**, then connect it to your AI service.

The components are the interface only. They do not call any AI model, so you can use them with any provider.

## Components
{chr(10).join(rows)}
{(chr(10) + "## Coming next" + chr(10) + chr(10) + ", ".join(coming) + "." + chr(10)) if coming else ""}
## License

[MIT](LICENSE). Free for personal and business use.

Made by [MM Rahman Bappi](https://mmseo.app/).
"""
    open(os.path.join(ROOT, "README.md"), "w").write(readme)
    print("site built:", n, "components,", len(BUILT), "categories")


if __name__ == "__main__":
    build()
