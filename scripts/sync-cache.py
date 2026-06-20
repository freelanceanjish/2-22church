#!/usr/bin/env python3
"""Sync posts.js and style.css cache-bust query strings across HTML files."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_VERSION = "46"
STYLE_VERSION = "7"

SKIP = {"subscribers.html", "birth-preparation.html", "blog-preview-temple-parallels.html", "index.html.bak"}


def sync_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = re.sub(r"posts\.js\?v=\d+", f"posts.js?v={POSTS_VERSION}", text)
    text = re.sub(r'style\.css\?v=\d+', f"style.css?v={STYLE_VERSION}", text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for html in sorted(ROOT.rglob("*.html")):
        if html.name in SKIP or "blog-preview" in html.name:
            continue
        if sync_file(html):
            print("synced", html.relative_to(ROOT))
            changed += 1
    print(f"done: {changed} file(s) updated to posts.js?v={POSTS_VERSION}, style.css?v={STYLE_VERSION}")


if __name__ == "__main__":
    main()
