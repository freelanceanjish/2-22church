#!/usr/bin/env python3
"""Generate landing-page OG thumbnail samples for approval."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "blog-assets" / "og-samples"
W, H = 1200, 630

INK = (23, 42, 54)
MUTED = (71, 84, 91)
GOLD = (201, 168, 76)
BG = (244, 247, 245)
WHITE = (255, 255, 255)


def fonts():
    bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46)
    headline = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 54)
    reg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    micro = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    return bold, headline, reg, sm, micro


def paste_logo(canvas, logo_path, box, max_h=110):
    logo = Image.open(logo_path).convert("RGBA")
    scale = min((box[2] - box[0]) / logo.width, max_h / logo.height)
    size = (max(1, int(logo.width * scale)), max(1, int(logo.height * scale)))
    logo = logo.resize(size, Image.LANCZOS)
    x = box[0] + (box[2] - box[0] - logo.width) // 2
    y = box[1] + (box[3] - box[1] - logo.height) // 2
    canvas.paste(logo, (x, y), logo)


def sample_a_light_band():
    """Light canvas, dark top band, gold logo, landing tagline below."""
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 150], fill=INK)
    draw.rectangle([0, 560, W, H], fill=(238, 244, 247))

    _, headline, reg, sm, micro = fonts()
    paste_logo(img, ROOT / "logo.png", (120, 24, W - 120, 126), max_h=88)

    draw.text((W // 2, 250), "Built on the Living Word", fill=INK, anchor="mm", font=headline)
    draw.text((W // 2, 330), "A house church movement", fill=INK, anchor="mm", font=reg)
    draw.multiline_text(
        (W // 2, 395),
        "Teaching · fellowship · breaking bread · prayer\nin homes, backyards, and parks",
        fill=MUTED,
        anchor="mm",
        font=sm,
        align="center",
        spacing=8,
    )
    draw.text((W // 2, 590), "2-22church.com", fill=MUTED, anchor="mm", font=micro)
    return img


def sample_b_dark_hero():
    """Full dark hero like logo-dark-bg, logo centered, tagline in white/gold."""
    img = Image.new("RGB", (W, H), INK)
    draw = ImageDraw.Draw(img)

    # soft glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([300, 40, 900, 420], fill=(201, 168, 76, 28))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"))

    _, headline, reg, sm, micro = fonts()
    paste_logo(img, ROOT / "logo.png", (180, 90, W - 180, 190), max_h=92)

    draw.text((W // 2, 285), "Built on the Living Word", fill=GOLD, anchor="mm", font=headline)
    draw.text((W // 2, 365), "A house church movement", fill=WHITE, anchor="mm", font=reg)
    draw.multiline_text(
        (W // 2, 430),
        "Apostolic foundation in homes where people actually gather",
        fill=(190, 198, 204),
        anchor="mm",
        font=sm,
        align="center",
    )
    draw.text((W // 2, 585), "2-22church.com", fill=(130, 145, 155), anchor="mm", font=micro)
    return img


def sample_c_mark_and_type():
    """Circle mark left, logo wordmark + tagline right."""
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 430, H], fill=INK)

    mark = None  # draw circle mark manually below
    cx, cy = 215, H // 2 - 30
    draw.ellipse([cx - 92, cy - 92, cx + 92, cy + 92], fill=INK, outline=GOLD, width=3)
    bold = fonts()[0]
    draw.text((cx, cy), "2-22", fill=WHITE, anchor="mm", font=ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42
    ))

    paste_logo(img, ROOT / "logo.png", (470, 70, W - 50, 155), max_h=72)

    _, headline, reg, sm, micro = fonts()
    draw.text((720, 230), "Built on the Living Word", fill=INK, anchor="mm", font=ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44
    ))
    draw.text((720, 305), "A house church movement", fill=INK, anchor="mm", font=reg)
    draw.multiline_text(
        (720, 390),
        "We are a community built on the apostolic\nfoundation of teaching, fellowship,\nbreaking bread, and prayer.",
        fill=MUTED,
        anchor="mm",
        font=sm,
        align="center",
        spacing=6,
    )
    draw.line([(470, 520), (W - 50, 520)], fill=(220, 228, 232), width=1)
    draw.text((720, 575), "2-22church.com", fill=MUTED, anchor="mm", font=micro)
    return img


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    samples = [
        ("sample-a-light-band.jpg", sample_a_light_band, "Sample A · light canvas, dark band, gold logo"),
        ("sample-b-dark-hero.jpg", sample_b_dark_hero, "Sample B · dark hero, gold headline"),
        ("sample-c-mark-type.jpg", sample_c_mark_and_type, "Sample C · circle mark + wordmark split"),
    ]
    for name, fn, label in samples:
        path = OUT / name
        fn().save(path, quality=92)
        print(label, "->", path)


if __name__ == "__main__":
    main()
