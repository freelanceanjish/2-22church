#!/usr/bin/env python3
"""Remove preventDefault on Study/Resources nav links so click goes to hub page."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(
    r"<script>\s*document\.querySelectorAll\('\.nav-item'\)\.forEach\(function\(item\)\{.*?\}\);\s*</script>",
    re.DOTALL,
)

for html in ROOT.glob("*.html"):
    if "preview" in html.name or html.name == "subscribers.html":
        continue
    text = html.read_text(encoding="utf-8")
    new_text = BLOCK.sub("", text)
    if new_text != text:
        html.write_text(new_text, encoding="utf-8")
        print("fixed", html.name)
