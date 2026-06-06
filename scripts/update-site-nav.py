#!/usr/bin/env python3
"""Replace dropdown nav with flat menu across site HTML files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ACTIVE = {
    "index.html": "Home",
    "articles.html": "Articles",
    "blogs.html": "Blogs",
    "blog.html": "Blogs",
    "testimonies.html": "Blogs",
    "study.html": "Study",
    "cosmology.html": "Study",
    "project314.html": "Study",
    "old-maps.html": "Study",
    "noahs-ark.html": "Study",
    "solomons-temple.html": "Study",
    "heavenly-jerusalem.html": "Study",
    "references.html": "Resources",
    "qa.html": "Q&A",
    "our-story.html": "Our Story",
    "gatherings.html": "Our Story",
    "scripturalism.html": "Articles",
    "post.html": "Articles",
}

ITEMS = [
    ("Home", "index.html#about"),
    ("Articles", "articles.html"),
    ("Blogs", "blogs.html"),
    ("Study", "study.html"),
    ("Resources", "references.html"),
    ("Q&A", "qa.html"),
    ("Our Story", "our-story.html"),
]


def desktop_nav(active_label: str) -> str:
    lines = ['  <ul class="nav-links">']
    for label, href in ITEMS:
        cls = ' class="active"' if label == active_label else ""
        lines.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')
    lines.append("  </ul>")
    return "\n".join(lines)


def mobile_nav(active_label: str) -> str:
    lines = []
    for label, href in ITEMS:
        lines.append(
            f'  <a href="{href}" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">{label}</a>'
        )
    lines.append(
        '  <a href="index.html#join" style="color:var(--text-secondary);" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Connect</a>'
    )
    return "\n".join(lines)


def patch_file(path: Path):
    text = path.read_text(encoding="utf-8")
    active = ACTIVE.get(path.name, "")
    new_desktop = desktop_nav(active)
    new_mobile = mobile_nav(active)

    # Replace desktop nav block
    text2 = re.sub(
        r"<ul class=\"nav-links\">.*?</ul>",
        new_desktop,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if text2 == text:
        return False

    # Replace mobile menu links (between close button and Connect)
    text3 = re.sub(
        r"(<div class=\"mobile-menu\" id=\"mobile-menu\">.*?<button class=\"mobile-close\"[^>]*>.*?</button>\n)(.*?)(\n</div>)",
        lambda m: m.group(1) + new_mobile + m.group(3),
        text2,
        count=1,
        flags=re.DOTALL,
    )

    path.write_text(text3, encoding="utf-8")
    print("updated", path.name)
    return True


def main():
    for html in sorted(ROOT.glob("*.html")):
        if html.name.endswith(".bak") or "preview" in html.name or html.name == "subscribers.html":
            continue
        patch_file(html)


if __name__ == "__main__":
    main()
