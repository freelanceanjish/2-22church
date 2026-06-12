#!/usr/bin/env python3
"""Replace em/en dashes used as punctuation in site prose."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"blog-preview-temple-parallels.html"}
FOOTER_OLD = "built on apostolic teaching — no walls, no hierarchy, just people."
FOOTER_NEW = "built on apostolic teaching, with no walls, no hierarchy, just people."

for path in sorted(ROOT.glob("*.html")):
    if path.name in SKIP:
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace(FOOTER_OLD, FOOTER_NEW)
    # em dash and en dash as clause separators
    text = text.replace(" — ", ", ")
    text = text.replace(" – ", ", ")
    text = text.replace("—", ", ")
    text = text.replace("–", ", ")
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"updated {path.name}")

# posts.js excerpts we touched
posts = ROOT / "posts.js"
if posts.exists():
    t = posts.read_text(encoding="utf-8")
    o = t
    t = t.replace(" — ", ", ")
    t = t.replace("—", ", ")
    if t != o:
        posts.write_text(t, encoding="utf-8")
        print("updated posts.js")
