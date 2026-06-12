#!/usr/bin/env python3
"""Restore dropdown nav (no carets) across site HTML files."""
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

STUDY_LINKS = [
    ("Biblical Cosmology", "cosmology.html"),
    ("God of Pi", "project314.html"),
    ("Noah's Ark", "noahs-ark.html"),
    ("Solomon's Temple", "solomons-temple.html"),
    ("Heavenly Jerusalem", "heavenly-jerusalem.html"),
    ("Old Maps", "old-maps.html"),
]

RESOURCE_LINKS = [
    ("One God", "references.html#one-god"),
    ("Short Season", "references.html#short-season"),
    ("Biblical Earth", "references.html#biblical-earth"),
    ("Podcasts", "references.html#podcasts"),
    ("Debates", "references.html#debates"),
    ("Articles", "references.html#articles"),
    ("Archives", "references.html#archives"),
    ("Documentaries", "references.html#documentaries"),
]


def active_class(label: str, active_label: str) -> str:
    return ' class="active"' if label == active_label else ""


def desktop_nav(active_label: str) -> str:
    lines = ["  <ul class=\"nav-links\">"]
    lines.append(
        f'    <li><a href="index.html#about"{active_class("Home", active_label)}>Home</a></li>'
    )
    lines.append(
        f'    <li><a href="articles.html"{active_class("Articles", active_label)}>Articles</a></li>'
    )
    lines.append(
        f'    <li><a href="blogs.html"{active_class("Blogs", active_label)}>Blogs</a></li>'
    )

    study_cls = active_class("Study", active_label)
    lines.append(f'    <li class="nav-item">')
    lines.append(f'      <a href="study.html"{study_cls}>Study</a>')
    lines.append('      <div class="nav-dropdown">')
    for label, href in STUDY_LINKS:
        lines.append(f'        <a href="{href}">{label}</a>')
    lines.append("      </div>")
    lines.append("    </li>")

    res_cls = active_class("Resources", active_label)
    lines.append(f'    <li class="nav-item">')
    lines.append(f'      <a href="references.html"{res_cls}>Resources</a>')
    lines.append('      <div class="nav-dropdown">')
    for label, href in RESOURCE_LINKS:
        lines.append(f'        <a href="{href}">{label}</a>')
    lines.append("      </div>")
    lines.append("    </li>")

    lines.append(
        f'    <li><a href="qa.html"{active_class("Q&A", active_label)}>Q&amp;A</a></li>'
    )
    lines.append(
        f'    <li><a href="our-story.html"{active_class("Our Story", active_label)}>Our Story</a></li>'
    )
    lines.append("  </ul>")
    return "\n".join(lines)


def mobile_nav() -> str:
    lines = [
        '  <a href="index.html#about" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Home</a>',
        '  <a href="articles.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Articles</a>',
        '  <a href="blogs.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Blogs</a>',
        '  <a href="study.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Study</a>',
    ]
    for label, href in STUDY_LINKS:
        lines.append(
            f'  <a href="{href}" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">{label}</a>'
        )
    lines.append(
        '  <a href="references.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Resources</a>'
    )
    lines.append(
        '  <a href="qa.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Q&amp;A</a>'
    )
    lines.append(
        '  <a href="our-story.html" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Our Story</a>'
    )
    lines.append(
        '  <a href="index.html#join" style="color:var(--text-secondary);" onclick="this.closest(\'.mobile-menu\').classList.remove(\'open\')">Connect</a>'
    )
    return "\n".join(lines)


def patch_file(path: Path):
    text = path.read_text(encoding="utf-8")
    active = ACTIVE.get(path.name, "")
    new_desktop = desktop_nav(active)
    new_mobile = mobile_nav()

    text2 = re.sub(
        r"<ul class=\"nav-links\">.*?</ul>",
        new_desktop,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if text2 == text:
        return False

    text3 = re.sub(
        r"<div class=\"mobile-menu\" id=\"mobile-menu\">.*?<button class=\"mobile-close\"[^>]*>.*?</button>\s*(.*?)\s*</div>",
        lambda m: (
            '<div class="mobile-menu" id="mobile-menu">\n'
            '  <button class="mobile-close" onclick="document.getElementById(\'mobile-menu\').classList.remove(\'open\')">&times;</button>\n'
            + new_mobile
            + "\n</div>"
        ),
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
