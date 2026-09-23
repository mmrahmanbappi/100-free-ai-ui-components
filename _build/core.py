"""Shared helpers for the AI UI component files."""
import html

SITE = "https://mmrahmanbappi.github.io/100-free-ai-ui-components"
REPO = "https://github.com/mmrahmanbappi/100-free-ai-ui-components"

CATEGORIES = [
    ("prompt-input", "Prompt Input", "Boxes where people type to the AI, from a simple field to slash commands and history."),
    ("thinking", "Thinking and Loading", "Animations and states that show the AI is working, streaming or using a tool."),
    ("messages", "Chat Messages", "Message bubbles, code blocks, sources and actions for AI answers."),
    ("feedback", "Answer Feedback", "Ratings, thumbs, comparisons and forms that tell you if an answer helped."),
    ("usage", "Tokens and Usage", "Token meters, context bars, credits and limits that show what each chat costs."),
    ("settings", "Model and Settings", "Model pickers, sliders and toggles that control how the AI answers."),
    ("chat-layout", "Chat Layouts", "Full chat windows, sidebars, widgets and empty states."),
    ("agents", "Agents and Tools", "Tool calls, approvals, task plans and logs for AI agents."),
    ("voice-media", "Voice and Media", "Voice input, audio answers, image upload and generation progress."),
    ("trust", "Trust and Onboarding", "Labels, notices, tips and error states that help people trust the AI."),
]

COMPONENTS = []

# Design tokens shared by every component. Change --accent to rebrand.
TOKENS = """:root{
  --accent:#5b5bd6; --accent-ink:#fff; --accent-soft:#ececfc;
  --bg:#f7f7f8; --surface:#fff; --surface-2:#f1f1f4; --ink:#17171c; --text:#3a3a44; --muted:#6c6c78;
  --line:#e3e3e8; --good:#15803d; --warn:#b45309; --bad:#c62828;
  --radius:14px; --shadow:0 1px 2px rgba(20,20,30,.06),0 8px 24px -12px rgba(20,20,30,.18);
  --font:system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,sans-serif; --mono:ui-monospace,"Cascadia Code",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){
  --accent:#8b8bff; --accent-ink:#0f0f16; --accent-soft:#25254a;
  --bg:#0f0f13; --surface:#18181f; --surface-2:#212129; --ink:#f3f3f6; --text:#d4d4dc; --muted:#9a9aa8;
  --line:#2c2c36; --good:#4ade80; --warn:#fbbf24; --bad:#f87171; --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -12px rgba(0,0,0,.6);
}}
:root[data-theme=dark]{
  --accent:#8b8bff; --accent-ink:#0f0f16; --accent-soft:#25254a;
  --bg:#0f0f13; --surface:#18181f; --surface-2:#212129; --ink:#f3f3f6; --text:#d4d4dc; --muted:#9a9aa8;
  --line:#2c2c36; --good:#4ade80; --warn:#fbbf24; --bad:#f87171; --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -12px rgba(0,0,0,.6);
}
*{box-sizing:border-box}
html,body{margin:0}
body{min-height:100vh;display:grid;grid-template-columns:minmax(0,1fr);place-items:center;padding:24px;background:var(--bg);color:var(--text);font:15px/1.5 var(--font);-webkit-font-smoothing:antialiased}
button,input,textarea,select{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
[hidden]{display:none!important}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition:none!important}}"""

# Small SVG icons used inside components
ICON = {
    "send": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    "clip": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5l-8.6 8.6a5 5 0 01-7.1-7.1l8.6-8.6a3.5 3.5 0 015 5l-8.6 8.6a2 2 0 01-2.8-2.8l7.9-7.9"/></svg>',
    "mic": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></svg>',
    "stop": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>',
    "x": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "file": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/></svg>',
    "history": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 109-9 9 9 0 00-7 3.4"/><path d="M3 4v4h4M12 7v5l3 2"/></svg>',
    "check": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12l5 5L20 6"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true"><path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8z"/></svg>',
}


def esc(s):
    return html.escape(str(s), quote=True)


def page(c):
    return f"""<!DOCTYPE html>
<!--
  {c['name']}: a free AI UI component
  From 100 Free AI UI Components by MM Rahman Bappi, MIT license
  {SITE}/

  How to use: copy the CSS, HTML and JavaScript below into your page.
  Colors are CSS variables at the top. Change --accent to match your brand.
  Light and dark themes follow the visitor's system setting, or set
  data-theme="dark" or data-theme="light" on the html element.
-->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(c['name'])} | Free AI UI Component</title>
<meta name="description" content="{esc(c['blurb'])}">
<meta name="robots" content="noindex, follow">
<style>
{TOKENS}
/* ---- component ---- */
{c['css'].strip()}
</style>
</head>
<body>
{c['html'].strip()}
<script>
// Demo helper: add ?theme=dark or ?theme=light to the address to preview a theme.
(function(){{var t=new URLSearchParams(location.search).get('theme');if(t)document.documentElement.dataset.theme=t;}})();
{c['js'].strip()}
</script>
</body>
</html>
"""


def add(category, slug, name, blurb, css, html_, js=""):
    COMPONENTS.append(dict(category=category, slug=slug, name=name, blurb=blurb, css=css, html=html_, js=js))
