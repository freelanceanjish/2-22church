#!/usr/bin/env python3
"""Build side-by-side decagon template + B-DNA axial top view comparison figure."""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "blog-assets" / "dna-tabernacle" / "larsen-dna-decagon-cross-section.png"
OUT = ROOT / "blog-assets" / "dna-tabernacle" / "dna-quantum-tabernacle-compare.jpg"
THUMB = ROOT / "blog-assets" / "study" / "thumbs" / "nature" / "dna-quantum-tabernacle-w480.jpg"
ICON = ROOT / "blog-assets" / "study" / "thumbs" / "dna-quantum-tabernacle-icon-w480.jpg"

W, H = 1200, 760
PAD = 36
SPLIT = W // 2


def crop_panel(img: Image.Image, index: int) -> Image.Image:
    w, h = img.size
    panel_w = w // 3
    return img.crop((index * panel_w, 0, (index + 1) * panel_w, h))


def paper_bg(size: tuple[int, int]) -> Image.Image:
    bg = Image.new("RGB", size, (244, 238, 228))
    noise = Image.effect_noise(size, 18).convert("L")
    noise = ImageEnhance.Contrast(noise).enhance(0.35)
    tint = Image.new("RGB", size, (236, 228, 214))
    return Image.composite(tint, bg, noise)


def colorize_dna(panel: Image.Image) -> Image.Image:
    gray = panel.convert("L")
    gray = ImageOps.autocontrast(gray, cutoff=1)
    gray = ImageEnhance.Contrast(gray).enhance(1.35)
    w, h = gray.size
    out = Image.new("RGB", (w, h), (0, 0, 0))
    px = out.load()
    gpx = gray.load()
    cx, cy = w / 2, h / 2
    max_r = math.hypot(cx, cy)
    for y in range(h):
        for x in range(w):
            g = gpx[x, y]
            if g > 235:
                continue
            r = math.hypot(x - cx, y - cy) / max_r
            if g < 40:
                color = (20, 60, 180)
            elif g < 90:
                color = (0, 170, 210)
            elif g < 140:
                color = (40, 210, 120)
            elif g < 190:
                color = (230, 210, 40)
            else:
                color = (240, 90, 30)
            strength = min(1.0, (255 - g) / 180)
            mix = 0.35 + 0.65 * strength
            px[x, y] = tuple(int(c * mix * (0.75 + 0.25 * (1 - r))) for c in color)
    return out.filter(ImageFilter.GaussianBlur(radius=0.4))


def fit_panel(panel: Image.Image, box: tuple[int, int, int, int], bg: Image.Image) -> None:
    x0, y0, x1, y1 = box
    target_w, target_h = x1 - x0, y1 - y0
    scale = min(target_w / panel.width, target_h / panel.height) * 0.92
    new_size = (max(1, int(panel.width * scale)), max(1, int(panel.height * scale)))
    panel = panel.resize(new_size, Image.Resampling.LANCZOS)
    ox = x0 + (target_w - panel.width) // 2
    oy = y0 + (target_h - panel.height) // 2
    bg.paste(panel, (ox, oy), panel if panel.mode == "RGBA" else None)


def build() -> None:
    src = Image.open(SRC).convert("RGB")
    panel_a = crop_panel(src, 0)
    panel_b = crop_panel(src, 1)

    canvas = Image.new("RGB", (W, H), (18, 18, 22))
    left = paper_bg((SPLIT - PAD, H - PAD * 2))
    right = Image.new("RGB", (SPLIT - PAD, H - PAD * 2), (8, 8, 12))
    canvas.paste(left, (PAD, PAD))
    canvas.paste(right, (SPLIT, PAD))

    content_top, content_bottom = PAD + 48, H - PAD - 36
    left_box = (PAD + 24, content_top, SPLIT - 24, content_bottom)
    right_box = (SPLIT + 24, content_top, W - PAD - 24, content_bottom)

    decagon = panel_b.convert("RGBA")
    dna = colorize_dna(panel_a)
    fit_panel(decagon, left_box, canvas)
    fit_panel(dna, right_box, canvas)

    draw = ImageDraw.Draw(canvas)
    draw.line([(SPLIT, PAD + 20), (SPLIT, H - PAD - 20)], fill=(120, 128, 136), width=1)
    draw.text((SPLIT // 2, PAD + 18), "Decagon template · ten golden triangles", fill=(90, 70, 40), anchor="mm")
    draw.text((SPLIT + (SPLIT - PAD) // 2, PAD + 18), "B-DNA axial view · top of the helix", fill=(180, 210, 230), anchor="mm")
    draw.text(
        (W // 2, H - PAD - 10),
        "Larsen 2021 · Symmetry · decagon overlay on B-DNA cross-section (panels B and A)",
        fill=(170, 176, 182),
        anchor="mm",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, quality=93)
    print("wrote", OUT)

    thumb_w = 480
    scale = thumb_w / W
    thumb = canvas.resize((thumb_w, int(H * scale)), Image.Resampling.LANCZOS)
    THUMB.parent.mkdir(parents=True, exist_ok=True)
    thumb.save(THUMB, quality=85)
    print("wrote", THUMB)

    icon_size = 480
    scale = min(icon_size / W, icon_size / H)
    fitted = canvas.resize((int(W * scale), int(H * scale)), Image.Resampling.LANCZOS)
    square = Image.new("RGB", (icon_size, icon_size), (18, 18, 22))
    ox = (icon_size - fitted.width) // 2
    oy = (icon_size - fitted.height) // 2
    square.paste(fitted, (ox, oy))
    ICON.parent.mkdir(parents=True, exist_ok=True)
    square.save(ICON, quality=86, optimize=True)
    print("wrote", ICON, f"({icon_size}x{icon_size})")


if __name__ == "__main__":
    build()
