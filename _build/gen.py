"""Writes every component to <category>/<slug>/index.html."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import core  # noqa: E402

MODULES = ["c_prompt", "c_thinking", "c_messages", "c_feedback", "c_usage", "c_settings", "c_layout", "c_agents", "c_voice", "c_trust"]
for m in MODULES:
    try:
        __import__(m)
    except ImportError:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    seen = set()
    for c in core.COMPONENTS:
        assert c["slug"] not in seen, "duplicate slug " + c["slug"]
        seen.add(c["slug"])
        d = os.path.join(ROOT, c["category"], c["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "component.html"), "w", encoding="utf-8").write(core.page(c))
    print("wrote", len(core.COMPONENTS), "components")
