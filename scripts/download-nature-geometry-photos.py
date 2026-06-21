#!/usr/bin/env python3
"""Download geometry-focused CC nature photos and crop to pattern for Study hub."""

import json
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps

OUT = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "nature"
THUMBS = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "thumbs" / "nature"
HERO = Path(__file__).resolve().parent.parent / "blog-assets" / "study" / "thumbs"
UA = "2-22church-study/1.0 (educational; contact: 2-22church.com)"

# (slug, commons filename, geometry crop spec)
# keep: center fraction to retain before aspect crop (lower = tighter zoom on pattern)
FILES = [
    ("sunflower", "Pflanze-Sonnenblume1-Asio (cropped).JPG", {"keep": 0.92, "aspect": (3, 2)}),
    ("pinecone", "Scrub Pine Pinus virginiana Cone Closeup 2000px.jpg", {"keep": 0.78, "aspect": (3, 2)}),
    ("fern-frond", "Southern Wood Fern Dryopteris ludoviciana Frond Closeup 2000px.jpg", {"keep": 0.72, "aspect": (3, 2)}),
    ("nautilus-shell", "Inside Nautilus Pompilius.jpg", {"keep": 0.68, "aspect": (3, 2)}),
    ("honeycomb", "Wax foundation - Flickr - conall...jpg", {"keep": 0.62, "aspect": (3, 2)}),
    ("snowflake", "Real snowflake - Flickr - Alexey Kljatov (6).jpg", {"keep": 0.52, "aspect": (3, 2)}),
    ("galaxy-spiral", "Messier51 sRGB.jpg", {"keep": 0.42, "aspect": (3, 2)}),
    ("human-eye", "Iris Macro, Eye close-up (11622304153).jpg", {"keep": 0.85, "aspect": (3, 2)}),
]

FALLBACK = {
    "sunflower": "Sunflower macro wide.jpg",
    "pinecone": "Pine Cone (124362815).jpeg",
    "fern-frond": "Christmas Fern Polystichum acrostichoides Curl Closeup 2000px.jpg",
    "nautilus-shell": "Nautilus_pompilius.jpg",
    "honeycomb": "Honey_comb.jpg",
    "snowflake": "Snowflake_300um_LTSEM.jpg",
    "galaxy-spiral": "Young, Hot Stars in a Spiral Arm of the Whirlpool Galaxy (M51) (2005-12-1695).jpg",
    "human-eye": "Human eye.jpg",
}

FALLBACK_CROP = {
    "sunflower": {"keep": 0.55, "aspect": (3, 2)},
    "pinecone": {"keep": 0.65, "aspect": (3, 2)},
    "fern-frond": {"keep": 0.7, "aspect": (3, 2)},
    "nautilus-shell": {"keep": 0.55, "aspect": (3, 2)},
    "honeycomb": {"keep": 0.55, "aspect": (3, 2)},
    "snowflake": {"keep": 0.75, "aspect": (3, 2)},
    "galaxy-spiral": {"keep": 0.55, "aspect": (3, 2)},
    "human-eye": {"keep": 0.85, "aspect": (3, 2)},
}


def resolve_url(filename: str) -> str | None:
    q = urllib.parse.quote(filename.replace(" ", "_"))
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&titles=File:"
        + q
        + "&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 ** attempt + 2)
                continue
            raise
    if len(data) < 5000 or data[:15].startswith(b"<!DOCTYPE") or data[:5] == b"<?xml":
        return {"slug": slug, "ok": False, "tried": tried, "reason": "not image"}
    dest.write_bytes(data)
    return {"slug": slug, "ok": True, "file": dest.name, "bytes": len(data), "source": url}


def crop_geometry(img: Image.Image, spec: dict) -> Image.Image:
    img = ImageOps.exif_transpose(img.convert("RGB"))
    keep = spec.get("keep", 0.75)
    aw, ah = spec.get("aspect", (3, 2))
    target_ratio = aw / ah

    w, h = img.size
    side = int(min(w, h) * keep)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))

    w, h = img.size
    current = w / h
    if current > target_ratio:
        new_w = int(h * target_ratio)
        x0 = (w - new_w) // 2
        img = img.crop((x0, 0, x0 + new_w, h))
    else:
        new_h = int(w / target_ratio)
        y0 = (h - new_h) // 2
        img = img.crop((0, y0, w, y0 + new_h))
    return img


def save_thumb(src: Path, dst: Path, spec: dict, width: int = 480) -> None:
    img = crop_geometry(Image.open(src), spec)
    height = int(width * spec.get("aspect", (3, 2))[1] / spec.get("aspect", (3, 2))[0])
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    THUMBS.mkdir(parents=True, exist_ok=True)
    img.save(dst, "JPEG", quality=84, optimize=True)
    print(f"  thumb {dst.name} ({width}x{height})")


def main() -> None:
    manifest = []
    crop_specs: dict[str, dict] = {}

    for slug, name, spec in FILES:
        print("fetch", slug, "...", end=" ")
        dest = OUT / f"{slug}.jpg"
        if dest.exists() and dest.stat().st_size > 5000:
            m = {"slug": slug, "ok": True, "file": dest.name, "bytes": dest.stat().st_size, "source": "cached"}
            print("cached", end=" ")
        else:
            m = download(slug, name)
            if not m.get("ok") and slug in FALLBACK:
                time.sleep(1)
                m = download(slug, FALLBACK[slug])
                spec = FALLBACK_CROP.get(slug, spec)
        manifest.append(m)
        crop_specs[slug] = spec
        print("OK" if m.get("ok") else "FAIL", m.get("source", m.get("tried")))

    dna_src = Path(__file__).resolve().parent.parent / "blog-assets" / "dna-tabernacle" / "dna-double-helix-nhgri.jpg"
    dna_dest = OUT / "dna-double-helix.jpg"
    if dna_src.exists():
        shutil.copy2(dna_src, dna_dest)
        manifest.append({"slug": "dna-double-helix", "ok": True, "file": dna_dest.name, "source": "NIH/NHGRI public domain"})
        crop_specs["dna-double-helix"] = {"keep": 0.55, "aspect": (3, 2)}
        print("copy dna-double-helix OK")
    else:
        manifest.append({"slug": "dna-double-helix", "ok": False})

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    ok = sum(1 for m in manifest if m.get("ok"))
    print(f"\n{ok}/{len(manifest)} saved to {OUT}")

    print("\nBuilding geometry-focused thumbs...")
    for path in sorted(OUT.glob("*.*")):
        if path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        slug = path.stem
        spec = crop_specs.get(slug, {"keep": 0.7, "aspect": (3, 2)})
        save_thumb(path, THUMBS / f"{slug}-w480.jpg", spec)

    sunflower = OUT / "sunflower.jpg"
    if sunflower.exists():
        hero_dst = HERO / "geometry-sunflower-hero-w1200.jpg"
        img = crop_geometry(Image.open(sunflower), crop_specs.get("sunflower", {"keep": 0.9, "aspect": (3, 2)}))
        w, h = img.size
        scale = min(1200 / w, 800 / h, 1.0)
        if scale < 1.0:
            w = int(w * scale)
            h = int(h * scale)
            img = img.resize((w, h), Image.Resampling.LANCZOS)
        img.save(hero_dst, "JPEG", quality=86, optimize=True)
        print(f"  hero {hero_dst.name} ({w}x{h})")


if __name__ == "__main__":
    main()
