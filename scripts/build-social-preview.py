#!/usr/bin/env python3
"""Build og-image.jpg, inject social meta tags, and generate post share pages."""

import html
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
POSTS_JS = ROOT / "posts.js"
POST_DIR = ROOT / "post"
SITE = "https://2-22church.com"
OG_IMAGE = ROOT / "og-image.jpg"
OG_VERSION = "4"
CROPS_DIR = ROOT / "blog-assets" / "og-crops"
MARKER_START = "<!-- social-meta:start -->"
MARKER_END = "<!-- social-meta:end -->"

SKIP_HTML = {
    "subscribers.html",
    "birth-preparation.html",
    "blog-preview-temple-parallels.html",
    "index.html.bak",
}

PAGE_META = {
    "index.html": {
        "title": "2:22 Church, Built on the Living Word",
        "description": "A community rooted in the living Word, gathered around Jesus Christ, built on apostolic teaching, with no walls and no hierarchy, just people.",
        "path": "/index.html",
        "type": "website",
    },
    "articles.html": {
        "title": "Articles, 2:22 Church",
        "description": "Reflections on Scripture, community, service, and the living faith we are still learning to walk.",
        "path": "/articles.html",
        "type": "website",
    },
    "blogs.html": {
        "title": "Blogs, 2:22 Church",
        "description": "Personal testimony, reflection, and honest writing from the 2:22 Church community.",
        "path": "/blogs.html",
        "type": "website",
    },
    "blog.html": {
        "title": "Blog, 2:22 Church",
        "description": "Weekly word and teaching from 2:22 Church.",
        "path": "/blog.html",
        "type": "website",
    },
    "testimonies.html": {
        "title": "Testimonies, 2:22 Church",
        "description": "Personal stories of faith, struggle, and following Jesus.",
        "path": "/testimonies.html",
        "type": "website",
    },
    "qa.html": {
        "title": "Questions and Answers, 2:22 Church",
        "description": "Honest questions answered from Scripture, with links to in-depth articles and studies.",
        "path": "/qa.html",
        "type": "website",
    },
    "study.html": {
        "title": "Study Hub, 2:22 Church",
        "description": "Promoted research on biblical cosmology, Project314, Renformation, and original 2:22 Church studies.",
        "path": "/study.html",
        "type": "website",
    },
    "our-story.html": {
        "title": "Our Story, 2:22 Church",
        "description": "How 2:22 Church began and why we carry a burden for truth outside institutional religion.",
        "path": "/our-story.html",
        "type": "website",
    },
    "gatherings.html": {
        "title": "Gatherings, 2:22 Church",
        "description": "How we gather in homes and open places, the apostolic pattern without buildings or hierarchy.",
        "path": "/gatherings.html",
        "type": "website",
    },
    "cosmology.html": {
        "title": "Biblical Cosmology, 2:22 Church",
        "description": "Study of the firmament, the circle of the earth, and what Scripture says about creation.",
        "path": "/cosmology.html",
        "type": "website",
    },
    "project314.html": {
        "title": "God of Pi, 2:22 Church",
        "description": "Andrew Hoy and Project314: pi in Exodus curtains and the recovered Tabernacle pattern.",
        "path": "/project314.html",
        "type": "website",
    },
    "noahs-ark.html": {
        "title": "Noah's Ark, 2:22 Church",
        "description": "Renformation Project Arc and the curved-vessel reading of Genesis 6.",
        "path": "/noahs-ark.html",
        "type": "website",
    },
    "solomons-temple.html": {
        "title": "Solomon's Temple, 2:22 Church",
        "description": "The stone enlargement of Moses' Tabernacle blueprint.",
        "path": "/solomons-temple.html",
        "type": "website",
    },
    "heavenly-jerusalem.html": {
        "title": "Heavenly Jerusalem, 2:22 Church",
        "description": "The city-dwelling pattern from Ezekiel to Revelation.",
        "path": "/heavenly-jerusalem.html",
        "type": "website",
    },
    "old-maps.html": {
        "title": "Old Maps, 2:22 Church",
        "description": "Historical maps and the biblical earth.",
        "path": "/old-maps.html",
        "type": "website",
    },
    "references.html": {
        "title": "Resources, 2:22 Church",
        "description": "Podcasts, debates, articles, and archives for studying Scripture and history.",
        "path": "/references.html",
        "type": "website",
    },
    "scripturalism.html": {
        "title": "Scripturalism, 2:22 Church",
        "description": "The Word judges history, not the other way around.",
        "path": "/scripturalism.html",
        "type": "article",
    },
    "post.html": {
        "title": "Articles, 2:22 Church",
        "description": "Teaching, testimony, and study articles from 2:22 Church.",
        "path": "/post.html",
        "type": "website",
    },
}


def load_posts():
    text = POSTS_JS.read_text(encoding="utf-8")
    posts = []
    start = text.find("const POSTS = [")
    if start == -1:
        return posts
    chunk = text[start:]
    for m in re.finditer(r'\n  \{\n    id: "([^"]+)"', chunk):
        block_start = m.start()
        next_post = chunk.find("\n  {", block_start + 1)
        block = chunk[block_start:next_post if next_post != -1 else len(chunk)]

        def grab(name):
            fm = re.search(rf'{name}: "((?:\\.|[^"\\])*)"', block)
            return fm.group(1).replace('\\"', '"') if fm else ""

        linkm = re.search(r'link: "([^"]+)"', block)
        image = grab("image")
        posts.append(
            {
                "id": m.group(1),
                "title": grab("title"),
                "date": grab("date"),
                "category": grab("category"),
                "image": image,
                "excerpt": grab("excerpt"),
                "link": linkm.group(1) if linkm else None,
            }
        )
    return posts


def abs_image(path: str) -> str:
    if not path or path.startswith("data:"):
        return f"{SITE}/og-image.jpg?v={OG_VERSION}"
    path = path.split("?", 1)[0]
    if path.startswith("http"):
        return path
    return f"{SITE}/{path.lstrip('/')}"


def cover_crop(im, target_w, target_h):
    scale = max(target_w / im.width, target_h / im.height)
    resized = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def hero_gradient_overlay(w, h):
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = overlay.load()
    for x in range(w):
        t = x / w
        if t <= 0.44:
            alpha = 0.92 - (t / 0.44) * 0.14
        else:
            alpha = 0.78 - ((t - 0.44) / 0.56) * 0.42
        a = int(255 * max(0.0, min(1.0, alpha)))
        for y in range(h):
            px[x, y] = (255, 255, 255, a)
    return overlay


def crop_width_from_meta(meta, margin=64):
    """Right edge of OG content: logo/tagline bounds plus margin."""
    lb = meta["logo"]
    tb = meta["tagline"]
    right = max(lb["x"] + lb["width"], tb["x"] + tb["width"])
    return int(min(1200, right + margin))


def build_og_image():
    """Compose OG thumbnail from hero background plus live logo/tagline screenshots."""
    import json

    w, h = 1200, 630
    hero = Image.open(ROOT / "hero-bg.jpg").convert("RGB")
    base = cover_crop(hero, w, h)
    base = Image.alpha_composite(base.convert("RGBA"), hero_gradient_overlay(w, h)).convert("RGB")

    logo_path = CROPS_DIR / "logo-crop.png"
    tagline_path = CROPS_DIR / "hero-tagline-crop.png"
    meta_path = CROPS_DIR / "meta.json"

    if logo_path.exists() and tagline_path.exists() and meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        logo = Image.open(logo_path).convert("RGBA")
        tagline = Image.open(tagline_path).convert("RGBA")
        lb = meta["logo"]
        tb = meta["tagline"]
        base = base.convert("RGBA")
        base.alpha_composite(logo, (int(lb["x"]), int(lb["y"])))
        base.alpha_composite(tagline, (int(tb["x"]), int(tb["y"])))

        crop_w = crop_width_from_meta(meta)
        cropped = base.crop((0, 0, crop_w, h))
        base = cropped.resize((w, h), Image.LANCZOS).convert("RGB")
    else:
        raise FileNotFoundError(
            "Missing OG crops. Run: node scripts/capture-og-crops.mjs"
        )

    out = ROOT / "og-image.jpg"
    base.save(out, quality=92, optimize=True)
    samples = ROOT / "blog-assets" / "og-samples"
    samples.mkdir(parents=True, exist_ok=True)
    base.save(samples / "live-home-hero.jpg", quality=92)
    print("wrote", out)


def meta_block(title, description, url, image, page_type="website"):
    title_e = html.escape(title, quote=True)
    desc_e = html.escape(description, quote=True)
    url_e = html.escape(url, quote=True)
    image_e = html.escape(image, quote=True)
    return f"""{MARKER_START}
<meta name="description" content="{desc_e}">
<link rel="canonical" href="{url_e}">
<meta property="og:type" content="{page_type}">
<meta property="og:site_name" content="2:22 Church">
<meta property="og:title" content="{title_e}">
<meta property="og:description" content="{desc_e}">
<meta property="og:url" content="{url_e}">
<meta property="og:image" content="{image_e}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_e}">
<meta name="twitter:description" content="{desc_e}">
<meta name="twitter:image" content="{image_e}">
{MARKER_END}"""


def inject_page_meta():
    default_image = f"{SITE}/og-image.jpg?v={OG_VERSION}"
    for filename, meta in PAGE_META.items():
        path = ROOT / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        block = meta_block(
            meta["title"],
            meta["description"],
            f"{SITE}{meta['path']}",
            default_image,
            meta.get("type", "website"),
        )
        if MARKER_START in text:
            text = re.sub(
                re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
                block,
                text,
                flags=re.S,
            )
        else:
            text = text.replace(
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + block,
                1,
            )
        path.write_text(text, encoding="utf-8")
        print("meta", filename)


def generate_post_share_pages(posts):
    POST_DIR.mkdir(exist_ok=True)
    template_path = ROOT / "post.html"
    template = template_path.read_text(encoding="utf-8")

    for post in posts:
        if post.get("link"):
            continue
        slug = post["id"]
        url = f"{SITE}/post/{slug}.html"
        image = abs_image(post.get("image", ""))
        title = f"{post['title']}, 2:22 Church"
        description = post["excerpt"]
        block = meta_block(title, description, url, image, "article")

        page = re.sub(
            r"<!-- social-meta:start -->.*?<!-- social-meta:end -->",
            block,
            template,
            count=1,
            flags=re.S,
        )
        page = page.replace("<title>Post, 2:22 Church</title>", f"<title>{html.escape(title)}</title>")
        if '<base href="' not in page:
            page = page.replace(
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<base href="https://2-22church.com/">',
                1,
            )
        page = page.replace(
            "var params = new URLSearchParams(window.location.search);\nvar postId = params.get('id');",
            f'var postId = "{slug}";',
        )

        out = POST_DIR / f"{slug}.html"
        out.write_text(page, encoding="utf-8")
        print("share", out.relative_to(ROOT))

    valid = {f"{p['id']}.html" for p in posts if not p.get("link")}
    for old in POST_DIR.glob("*.html"):
        if old.name not in valid:
            old.unlink()
            print("removed stale", old.relative_to(ROOT))


def post_href(post_id: str) -> str:
    return f"post/{post_id}.html"


def update_links():
    replacements = [
        (r'href="post\.html\?id=([^"]+)"', r'href="post/\1.html"'),
        (r"href='post\.html\?id=([^']+)'", r"href='post/\1.html'"),
        (r"'post\.html\?id=' \+ p\.id", r"'post/' + p.id + '.html'"),
        (r"'post\.html\?id=' \+ post\.id", r"'post/' + post.id + '.html'"),
        (r"postHref = post\.link \? post\.link : 'post\.html\?id=' \+ post\.id", r"postHref = post.link ? post.link : 'post/' + post.id + '.html'"),
        (r"var fHref = f\.link \? f\.link : 'post\.html\?id=' \+ f\.id", r"var fHref = f.link ? f.link : 'post/' + f.id + '.html'"),
        (r"var postHref = post\.link \? post\.link : 'post\.html\?id=' \+ post\.id", r"var postHref = post.link ? post.link : 'post/' + post.id + '.html'"),
        (r'href="post\.html\?id=\' \+ p\.id \+ \'"', r'href="post/\' + p.id + \'.html"'),
    ]

    patterns = [
        (r'href="post\.html\?id=([^"]+)"', r'href="post/\1.html"'),
        (r"href='post\.html\?id=([^']+)'", r"href='post/\1.html'"),
        (r"<a href=\"post\.html\?id=([^\"]+)\"", r'<a href="post/\1.html"'),
        (r"'post\.html\?id=' \+ p\.id \+", r"'post/' + p.id + '.html' +"),
        (r"'post\.html\?id=' \+ p\.id", r"'post/' + p.id + '.html'"),
        (r"'post\.html\?id=' \+ post\.id", r"'post/' + post.id + '.html'"),
        (r"'post\.html\?id=' \+ f\.id", r"'post/' + f.id + '.html'"),
        (r"post\.link \? post\.link : 'post\.html\?id=' \+ post\.id", r"post.link ? post.link : 'post/' + post.id + '.html'"),
        (r"f\.link \? f\.link : 'post\.html\?id=' \+ f\.id", r"f.link ? f.link : 'post/' + f.id + '.html'"),
        (r'return \'<a href="post\.html\?id=', r'return \'<a href="post/'),
        (r'post\.html\?id=\' \+ p\.id \+ \'"', r'post/\' + p.id + \'.html"'),
    ]

    for path in list(ROOT.glob("*.html")) + [POSTS_JS]:
        if path.name in SKIP_HTML or path.suffix != ".html" and path.name != "posts.js":
            if path.name != "posts.js":
                continue
        text = path.read_text(encoding="utf-8")
        original = text

        text = re.sub(r'href="post\.html\?id=([^"]+)"', r'href="post/\1.html"', text)
        text = re.sub(r"href='post\.html\?id=([^']+)'", r"href='post/\1.html'", text)
        text = re.sub(r"<a href=\"post\.html\?id=([^\"]+)\"", r'<a href="post/\1.html"', text)
        text = re.sub(
            r"post\.link \? post\.link : 'post\.html\?id=' \+ post\.id",
            r"post.link ? post.link : 'post/' + post.id + '.html'",
            text,
        )
        text = re.sub(
            r"f\.link \? f\.link : 'post\.html\?id=' \+ f\.id",
            r"f.link ? f.link : 'post/' + f.id + '.html'",
            text,
        )
        text = re.sub(
            r"return '<a href=\"post\.html\?id=' \+ p\.id \+ '\"",
            r"return '<a href=\"post/' + p.id + '.html\"'",
            text,
        )

        if text != original:
            path.write_text(text, encoding="utf-8")
            print("links", path.name)


def main():
    build_og_image()
    inject_page_meta()
    posts = load_posts()
    generate_post_share_pages(posts)
    update_links()


if __name__ == "__main__":
    main()
