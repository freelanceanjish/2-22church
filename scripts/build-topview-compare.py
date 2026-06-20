#!/usr/bin/env python3
"""Build Tabernacle top view + B-DNA helix comparison figure with safe margins."""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "blog-assets" / "dna-tabernacle"
HELIX = OUT_DIR / "dna-double-helix-nhgri.jpg"

W, H = 1200, 820
PAD = 40
DIVX = W // 2
CONTENT_TOP = 82
CONTENT_BOTTOM = 620
FOOTER_TOP = 648

INK = (23, 42, 54)
MUTED = (71, 84, 91)
GOLD = (139, 105, 20)
ACCENT = (91, 141, 184)
BG = (238, 244, 247)


def load_fonts():
    bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
    sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    xs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    micro = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    return bold, sm, xs, micro, label


def fits_in_box(bbox, box, margin=4):
    x0, y0, x1, y1 = box
    return (
        bbox[0] >= x0 + margin
        and bbox[1] >= y0 + margin
        and bbox[2] <= x1 - margin
        and bbox[3] <= y1 - margin
    )


def draw_tabernacle_topview(draw, box, label_font):
    """Draw Project314-style decagon top view; tribe labels stay inside safe margins."""
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    inset = 52
    max_r = min(x1 - x0, y1 - y0) // 2 - inset

    court_r = int(max_r * 0.90)
    draw.ellipse([cx - court_r, cy - court_r, cx + court_r, cy + court_r], outline=(101, 67, 33), width=3)
    for i in range(24):
        ang = math.radians(-90 + i * (360 / 24))
        px = cx + court_r * math.cos(ang)
        py = cy + court_r * math.sin(ang)
        draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(101, 67, 33))

    roof_r = int(max_r * 0.52)
    verts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        verts.append((cx + roof_r * math.cos(ang), cy + roof_r * math.sin(ang)))
    for i in range(10):
        nxt = (i + 1) % 10
        draw.polygon([cx, cy, verts[i][0], verts[i][1], verts[nxt][0], verts[nxt][1]], fill=(176, 32, 45))
        draw.line([verts[i], verts[nxt]], fill=(120, 18, 28), width=2)

    cap_r = int(max_r * 0.11)
    draw.ellipse(
        [cx - cap_r, cy - cap_r, cx + cap_r, cy + cap_r],
        fill=(230, 225, 210),
        outline=(120, 110, 95),
        width=2,
    )

    tribes = [
        "Benjamin",
        "Reuben",
        "Levi",
        "Judah",
        "Issachar",
        "Dan",
        "Gad",
        "Asher",
        "Naphtali",
        "Joseph",
    ]

    for i, name in enumerate(tribes):
        ang = math.radians(-90 + i * 36)
        for scale in (0.74, 0.68, 0.62, 0.56):
            label_r = int(max_r * scale)
            lx = cx + label_r * math.cos(ang)
            ly = cy + label_r * math.sin(ang)
            bbox = draw.textbbox((lx, ly - 12), name, font=label_font, anchor="mm")
            dot_y = ly - 22 if ly < cy else ly + 22
            dot_x = lx
            if fits_in_box(bbox, box, margin=6):
                draw.ellipse([dot_x - 5, dot_y - 5, dot_x + 5, dot_y + 5], fill=GOLD)
                draw.text((lx, ly), name, fill=INK, anchor="mm", font=label_font)
                break


def paste_helix(canvas, box):
    x0, y0, x1, y1 = box
    helix = Image.open(HELIX).convert("RGB")
    target_w = x1 - x0 - 12
    target_h = y1 - y0 - 28
    scale = min(target_w / helix.width, target_h / helix.height)
    new_size = (max(1, int(helix.width * scale)), max(1, int(helix.height * scale)))
    helix = helix.resize(new_size, Image.LANCZOS)
    panel = Image.new("RGB", (x1 - x0, y1 - y0), (255, 255, 255))
    ox = (x1 - x0 - helix.width) // 2
    oy = (y1 - y0 - helix.height) // 2 + 6
    panel.paste(helix, (ox, oy))
    canvas.paste(panel, (x0, y0))


def draw_dna_axial(draw, box):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    max_r = min(x1 - x0, y1 - y0) // 2 - 22
    r_outer, r_backbone, r_inner = int(max_r * 0.92), int(max_r * 0.68), int(max_r * 0.34)

    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        pts.append((cx + r_outer * math.cos(ang), cy + r_outer * math.sin(ang)))
    draw.polygon(pts, fill=(214, 228, 240), outline=ACCENT, width=2)
    draw.ellipse([cx - r_backbone, cy - r_backbone, cx + r_backbone, cy + r_backbone], outline=ACCENT, width=2)
    draw.ellipse([cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner], outline=ACCENT, width=1)

    for i in range(10):
        ang = math.radians(-90 + i * 36)
        x1p = cx + r_inner * math.cos(ang)
        y1p = cy + r_inner * math.sin(ang)
        x2p = cx + r_backbone * math.cos(ang)
        y2p = cy + r_backbone * math.sin(ang)
        draw.line([(x1p, y1p), (x2p, y2p)], fill=GOLD, width=3)
        draw.ellipse([x1p - 4, y1p - 4, x1p + 4, y1p + 4], fill=ACCENT)
        draw.ellipse([x2p - 4, y2p - 4, x2p + 4, y2p + 4], fill=ACCENT)

    bold = load_fonts()[0]
    micro = load_fonts()[3]
    draw.text((cx, cy - 6), "10", fill=INK, anchor="mm", font=bold)
    draw.text((cx, y1 - 18), "Axial view · 36° per base pair", fill=MUTED, anchor="mm", font=micro)


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bold, sm, xs, micro, label_font = load_fonts()

    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([PAD, PAD, W - PAD, H - PAD], radius=10, fill=BG, outline=INK, width=2)
    draw.text((W // 2, 54), "Top view: decagon Tabernacle camp and B-DNA double helix", fill=INK, anchor="mm", font=bold)
    draw.text((W // 4, 74), "~1400 BC · Project314 decagon model (top view)", fill=GOLD, anchor="mm", font=sm)
    draw.text((3 * W // 4, 74), "B-DNA · side view and axial turn", fill=ACCENT, anchor="mm", font=sm)
    draw.line([(DIVX, CONTENT_TOP - 6), (DIVX, CONTENT_BOTTOM + 6)], fill=(180, 188, 194), width=1)

    left_box = (PAD + 28, CONTENT_TOP, DIVX - 28, CONTENT_BOTTOM)
    right_h = CONTENT_BOTTOM - CONTENT_TOP
    helix_h = int(right_h * 0.58)
    right_top = (DIVX + 24, CONTENT_TOP, W - PAD - 24, CONTENT_TOP + helix_h - 4)
    right_bottom = (DIVX + 24, CONTENT_TOP + helix_h + 4, W - PAD - 24, CONTENT_BOTTOM)

    for b in (left_box, right_top, right_bottom):
        draw.rounded_rectangle(b, radius=8, fill=(255, 255, 255), outline=(210, 218, 224), width=1)

    draw_tabernacle_topview(draw, left_box, label_font)
    paste_helix(img, right_top)
    draw = ImageDraw.Draw(img)
    draw.text(
        ((right_top[0] + right_top[2]) // 2, right_top[1] + 14),
        "Double helix · NIH public domain",
        fill=ACCENT,
        anchor="mm",
        font=micro,
    )
    draw_dna_axial(draw, right_bottom)

    draw.text(
        (W // 4, FOOTER_TOP),
        "Andrew Hoy · Project314 · project314.org · decagon roof · ten camp positions",
        fill=MUTED,
        anchor="mm",
        font=xs,
    )
    draw.text(
        (W // 4, FOOTER_TOP + 18),
        "Numbers 2 camp order around the dwelling (model kit top view)",
        fill=MUTED,
        anchor="mm",
        font=xs,
    )
    draw.text(
        (3 * W // 4, FOOTER_TOP),
        "NIH B-DNA helix photograph (side) + axial decagon (top)",
        fill=MUTED,
        anchor="mm",
        font=xs,
    )
    draw.text(
        (3 * W // 4, FOOTER_TOP + 18),
        "10 base pairs · 36° per step · Curtis 1997 · Larsen Symmetry 2021",
        fill=MUTED,
        anchor="mm",
        font=xs,
    )
    draw.text(
        (W // 2, FOOTER_TOP + 44),
        "360° ÷ 10 = 36° (π/5 radians) · same count on the tent and in one helix turn",
        fill=INK,
        anchor="mm",
        font=xs,
    )
    draw.text(
        (W // 2, H - PAD - 14),
        "Left: physical decagon layout. Right: molecule side view and looking down the helix axis.",
        fill=MUTED,
        anchor="mm",
        font=micro,
    )

    out = OUT_DIR / "topview-tabernacle-dna-compare.jpg"
    img.save(out, quality=93)
    print("wrote", out)

    solo_pad = 72
    solo_size = 720
    solo = Image.new("RGB", (solo_size, solo_size), (255, 255, 255))
    sdraw = ImageDraw.Draw(solo)
    draw_tabernacle_topview(sdraw, (solo_pad, solo_pad, solo_size - solo_pad, solo_size - solo_pad), label_font)
    solo_path = OUT_DIR / "tabernacle-decagon-topview-tribes.jpg"
    solo.save(solo_path, quality=93)
    print("wrote", solo_path)


if __name__ == "__main__":
    build()
