#!/usr/bin/env python3
"""Remove duplicate inline nav-dropdown CSS so style.css controls hover behavior."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BLOCK = re.compile(
    r"\n?/\* NAV DROPDOWN[S]?[^*]*\*/\s*"
    r"(?:\.nav-item\.open\s*)?"
    r"\.nav-item\{[^}]+\}\s*"
    r"\.nav-item>a\{[^}]+\}\s*"
    r"(?:\.nav-item \.caret\{[^}]+\}\s*)?"
    r"(?:\.nav-item\.open[^}]+\}\s*)*"
    r"\.nav-dropdown\{[^}]+\}\s*"
    r"\.nav-item\.open \.nav-dropdown\{[^}]+\}\s*"
    r"\.nav-dropdown a\{[^}]+\}\s*"
    r"\.nav-dropdown a:hover\{[^}]+\}\s*",
    re.DOTALL,
)

for path in ROOT.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    new_text, n = BLOCK.subn("\n", text)
    if n:
        path.write_text(new_text, encoding="utf-8")
        print(f"cleaned {path.name} ({n} block(s))")

# bump style.css cache buster
for path in ROOT.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    updated = re.sub(r'style\.css\?v=\d+', "style.css?v=5", text)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        print(f"bumped cache on {path.name}")
