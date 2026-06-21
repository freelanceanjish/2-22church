#!/usr/bin/env python3
"""Download real CC/public-domain nature photos for Study hub divine geometry."""

import json
import shutil
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "nature"
THUMBS = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "thumbs" / "nature"
HERO = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "thumbs"
UA = "2-22church-study/1.0 (educational; contact: 2-22church.com)"

# (local_slug, commons_filename)
FILES = [
    ("sunflower", "Sunflower Helianthus annuus.jpg"),
    ("pinecone", "Pine cone - geograph.org.uk - 1308648.jpg"),
    ("fern-frond", "Fern frond - geograph.org.uk - 1308648.jpg"),
    ("nautilus-shell", "Nautilus_pompilius.jpg"),
    ("honeycomb", "Honey_comb.jpg"),
    ("snowflake", "Snowflake_300um_LTSEM.jpg"),
    ("galaxy-spiral", "Messier_51_Hubble_Wiki.jpg"),
    ("human-eye", "Iris Macro, Eye close-up (11622304153).jpg"),
]

FALLBACK = {
    "sunflower": "Sunflower from Silesia2.jpg",
    "pinecone": "Pine cones.jpg",
    "fern-frond": "Tree fern frond.jpg",
    "nautilus-shell": "Chambered Nautilus.jpg",
    "honeycomb": "Closeup_honeycomb.jpg",
    "snowflake": "Snowflake macro photography - Patagonia - Argentina.jpg",
    "galaxy-spiral": "Andromeda Galaxy (with h-alpha).jpg",
    "human-eye": "Human eye.jpg",
}


def resolve_url(filename: str) -> str | None:
    q = urllib.parse.quote(filename.replace(" ", "_"))
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&titles=File:"
        + q
        + "&prop=imageinfo&iiprop=url&iiurlwidth=960&format=json"
    )
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        for p in data.get("query", {}).get("pages", {}).values():
            if "imageinfo" in p:
                ii = p["imageinfo"][0]
                return ii.get("thumburl") or ii.get("url")
    except Exception as e:
        print("  api fail", filename, e)
    path_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(filename)}"
    req2 = urllib.request.Request(path_url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req2, timeout=30) as r:
            final = r.geturl()
            if "upload.wikimedia.org" in final and not final.endswith(".php"):
                return final
    except Exception as e:
        print("  redirect fail", filename, e)
    return None


def download(slug: str, filename: str) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    url = resolve_url(filename)
    tried = [filename]
    if not url and slug in FALLBACK:
        fb = FALLBACK[slug]
        tried.append(fb)
        url = resolve_url(fb)
    if not url:
        return {"slug": slug, "ok": False, "tried": tried}

    ext = ".jpg"
    if url.lower().endswith(".png"):
        ext = ".png"
    dest = OUT / f"{slug}{ext}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if len(data) < 5000 or data[:15].startswith(b"<!DOCTYPE") or data[:5] == b"<?xml":
        return {"slug": slug, "ok": False, "tried": tried, "reason": "not image"}
    dest.write_bytes(data)
    return {"slug": slug, "ok": True, "file": dest.name, "bytes": len(data), "source": url}


def resize_thumb(src: Path, dst: Path, max_width: int = 480, max_height: int = 320) -> None:
    img = Image.open(src)
    w, h = img.size
    scale = min(max_width / w, max_height / h, 1.0)
    if scale < 1.0:
        w = int(w * scale)
        h = int(h * scale)
        img = img.resize((w, h), Image.Resampling.LANCZOS)
    THUMBS.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(dst, "JPEG", quality=82, optimize=True)
    print(f"  thumb {dst.name} ({w}x{h})")


def main() -> None:
    manifest = []
    for slug, name in FILES:
        print("fetch", slug, "...", end=" ")
        m = download(slug, name)
        manifest.append(m)
        print("OK" if m.get("ok") else "FAIL", m.get("tried", m.get("reason")))

    # NIH public-domain DNA photograph (real molecule, not illustration)
    dna_src = Path(__file__).resolve().parent.parent / "blog-assets" / "dna-tabernacle" / "dna-double-helix-nhgri.jpg"
    dna_dest = OUT / "dna-double-helix.jpg"
    if dna_src.exists():
        shutil.copy2(dna_src, dna_dest)
        manifest.append({"slug": "dna-double-helix", "ok": True, "file": dna_dest.name, "source": "NIH/NHGRI public domain"})
        print("copy dna-double-helix OK")
    else:
        manifest.append({"slug": "dna-double-helix", "ok": False})
        print("copy dna-double-helix FAIL missing source")

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    ok = sum(1 for m in manifest if m.get("ok"))
    print(f"\n{ok}/{len(manifest)} saved to {OUT}")

    print("\nBuilding thumbs...")
    for path in sorted(OUT.glob("*.*")):
        if path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        slug = path.stem
        thumb = THUMBS / f"{slug}-w480.jpg"
        resize_thumb(path, thumb)

    sunflower = OUT / "sunflower.jpg"
    if sunflower.exists():
        hero_dst = HERO / "geometry-sunflower-hero-w1200.jpg"
        img = Image.open(sunflower)
        w, h = img.size
        scale = min(1200 / w, 800 / h, 1.0)
        if scale < 1.0:
            w = int(w * scale)
            h = int(h * scale)
            img = img.resize((w, h), Image.Resampling.LANCZOS)
        img.convert("RGB").save(hero_dst, "JPEG", quality=85, optimize=True)
        print(f"  hero {hero_dst.name} ({w}x{h})")


if __name__ == "__main__":
    main()
