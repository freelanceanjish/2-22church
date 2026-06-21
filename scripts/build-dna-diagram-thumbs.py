#!/usr/bin/env python3
"""Build square DNA diagram thumbs from the canonical double-helix diagram asset."""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "blog-assets" / "dna-tabernacle" / "dna-double-helix-diagram.jpg"
ICON = ROOT / "blog-assets" / "study" / "thumbs" / "dna-double-helix-icon-w480.jpg"
NATURE = ROOT / "blog-assets" / "study" / "thumbs" / "nature" / "dna-double-helix-w480.jpg"


def square_crop(img: Image.Image, keep: float = 0.82) -> Image.Image:
    img = ImageOps.exif_transpose(img.convert("RGB"))
    w, h = img.size
    side = int(min(w, h) * keep)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))


def save_square(src: Path, dst: Path, size: int, keep: float) -> None:
    img = square_crop(Image.open(src), keep=keep)
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(dst, "JPEG", quality=86, optimize=True)
    print(f"wrote {dst} ({size}x{size})")


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"missing source diagram: {SRC}")
    save_square(SRC, ICON, 480, keep=0.82)
    save_square(SRC, NATURE, 480, keep=0.82)


if __name__ == "__main__":
    main()
