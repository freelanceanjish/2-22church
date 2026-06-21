#!/usr/bin/env python3
"""Generate web-sized study images that fit hub cards and diagram frames."""

from pathlib import Path

from PIL import Image

ROOT = Path("blog-assets/study")
THUMBS = ROOT / "thumbs"


def resize_to(
    src: Path,
    dst: Path,
    max_width: int | None = None,
    max_height: int | None = None,
    jpeg: bool = False,
) -> None:
    img = Image.open(src)
    w, h = img.size
    scale = 1.0
    if max_width and w > max_width:
        scale = min(scale, max_width / w)
    if max_height and h > max_height:
        scale = min(scale, max_height / h)
    if scale < 1.0:
        w = int(w * scale)
        h = int(h * scale)
        img = img.resize((w, h), Image.Resampling.LANCZOS)

    dst.parent.mkdir(parents=True, exist_ok=True)
    if jpeg:
        img.convert("RGB").save(dst, "JPEG", quality=82, optimize=True)
    else:
        img.save(dst, "PNG", optimize=True)

    print(f"{src.name} -> {dst.name} ({w}x{h})")


def main() -> None:
    jobs = [
        # Study hub cards
        (ROOT / "ark-traditional-vs-contextual.png", THUMBS / "ark-traditional-vs-contextual-w640.png", 640, None, False),
        (ROOT / "temple-traditional-vs-contextual.png", THUMBS / "temple-traditional-vs-contextual-w640.png", 640, None, False),
        (ROOT / "jerusalem-traditional-vs-contextual.png", THUMBS / "jerusalem-traditional-vs-contextual-w640.png", 640, None, False),
        (ROOT / "renformation/ark/shoebox-vs-round.png", THUMBS / "shoebox-vs-round-w640.png", 640, None, False),
        # Study page diagrams (readable in ~1120px column)
        (ROOT / "jerusalem-traditional-vs-contextual.png", THUMBS / "jerusalem-traditional-vs-contextual-w960.png", 960, None, False),
        (ROOT / "jerusalem-contextual-elevation.png", THUMBS / "jerusalem-contextual-elevation-w960.png", 960, None, False),
        (ROOT / "jerusalem-pi-footprint.png", THUMBS / "jerusalem-pi-footprint-w960.png", 960, None, False),
    ]

    renformation = ROOT / "renformation"
    for path in sorted(renformation.rglob("*.png")):
        rel = path.relative_to(renformation)
        jobs.append(
            (path, THUMBS / "diagrams" / f"{rel.parent}-{path.stem}-w960.png".replace("/", "-"), 960, None, False)
        )

    jobs.append(
        (
            renformation / "research/rectangular-depiction.jpg",
            THUMBS / "diagrams/research-rectangular-depiction-w960.jpg",
            960,
            None,
            True,
        )
    )

    for src, dst, width, height, jpeg in jobs:
        if src.exists():
            resize_to(src, dst, width, height, jpeg)
        else:
            print(f"skip missing {src}")


if __name__ == "__main__":
    main()
