#!/usr/bin/env python3
"""Build 2-22 Church logo PNGs and favicon assets."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

BG = (248, 246, 241)
INK = (26, 36, 45)
WHITE = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def draw_mark(draw: ImageDraw.ImageDraw, cx: int, cy: int, radius: int, mark_size: int) -> None:
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=INK)
    font = load_font(FONT_BOLD, mark_size)
    draw.text((cx, cy), "2-22", fill=WHITE, anchor="mm", font=font)


def draw_spaced_text(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    tracking: int,
) -> None:
    for ch in text:
        draw.text((x, y), ch, fill=fill, anchor="lm", font=font)
        x += draw.textlength(ch, font=font) + tracking


def draw_full_logo(
    width: int,
    height: int,
    *,
    background: tuple[int, int, int] | None = BG,
    church_color: tuple[int, int, int] = INK,
) -> Image.Image:
    if background is None:
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    else:
        img = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(img)

    radius = int(height * 0.44)
    cx = radius + int(height * 0.12)
    cy = height // 2
    mark_size = max(12, int(height * 0.22))
    draw_mark(draw, cx, cy, radius, mark_size)

    church_font = load_font(FONT_REG, max(11, int(height * 0.19)))
    church_x = cx + radius + int(height * 0.22)
    draw_spaced_text(draw, church_x, cy, "CHURCH", church_font, church_color, int(height * 0.055))

    return img


def trim_horizontal(img: Image.Image, pad: int = 8) -> Image.Image:
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    bbox = img.getbbox()
    if not bbox:
        return img
    x0, y0, x1, y1 = bbox
    return img.crop((max(0, x0 - pad), max(0, y0 - pad), min(img.width, x1 + pad), min(img.height, y1 + pad)))


def build_mark_png(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.06)
    radius = size // 2 - pad
    draw_mark(draw, size // 2, size // 2, radius, max(10, int(size * 0.22)))
    return img


def save_ico(path: Path, sizes: list[int]) -> None:
    images = [build_mark_png(s) for s in sizes]
    images[0].save(path, format="ICO", sizes=[(s, s) for s in sizes], append_images=images[1:])


def main() -> None:
    full = draw_full_logo(1260, 180)
    full = trim_horizontal(full.convert("RGBA"))
    canvas = Image.new("RGB", (full.width + 80, full.height + 80), BG)
    canvas.paste(full, (40, 40), full)
    canvas.save(ROOT / "logo.png", optimize=True)
    print("wrote logo.png", canvas.size)

    transparent = draw_full_logo(1260, 180, background=None)
    transparent = trim_horizontal(transparent)
    transparent.save(ROOT / "logo-transparent.png", optimize=True)
    print("wrote logo-transparent.png", transparent.size)

    footer_logo = draw_full_logo(1260, 180, background=None, church_color=WHITE)
    footer_logo = trim_horizontal(footer_logo)
    footer_logo.save(ROOT / "logo-footer.png", optimize=True)
    print("wrote logo-footer.png", footer_logo.size)

    dark = draw_full_logo(1260, 180, background=(14, 14, 14), church_color=(234, 241, 244))
    dark = trim_horizontal(dark.convert("RGBA"))
    dark_canvas = Image.new("RGB", (dark.width + 80, dark.height + 80), (14, 14, 14))
    dark_canvas.paste(dark, (40, 40), dark)
    dark_canvas.save(ROOT / "logo-dark-bg.png", optimize=True)
    print("wrote logo-dark-bg.png", dark_canvas.size)

    mark64 = build_mark_png(64)
    mark64.save(ROOT / "favicon.png", optimize=True)
    mark180 = build_mark_png(180)
    mark180.save(ROOT / "apple-touch-icon.png", optimize=True)
    save_ico(ROOT / "favicon.ico", [16, 32, 48, 64])
    print("wrote favicon.png, favicon.ico, apple-touch-icon.png")


if __name__ == "__main__":
    main()
