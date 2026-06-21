#!/usr/bin/env python3
"""Generate a sacred-geometry montage video (Dearing Wang style) for 2-22 Church.

Opens with the site logo, then fast-cut scenes with text overlays using
Decagon DNA / Tabernacle assets. Output: blog-assets/dna-tabernacle/sacred-geometry-dna.mp4
"""

from __future__ import annotations

import math
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(__file__).resolve().parent / "fonts"
OUT_DIR = ROOT / "blog-assets" / "dna-tabernacle"
BUILD = ROOT / "scripts" / ".video-build"
OUTPUT = OUT_DIR / "sacred-geometry-dna.mp4"

W, H = 1920, 1080
FPS = 30

BG_DARK = (13, 23, 31)       # --gold-dark
BG_NAVY = (23, 42, 54)       # --gold (brand ink)
GOLD = (201, 169, 110)       # readable gold on dark
IVORY = (234, 241, 244)
WHITE = (255, 255, 255)
MUTED = (119, 129, 135)


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    name = {
        "light": "Poppins-Light.ttf",
        "regular": "Poppins-Regular.ttf",
        "medium": "Poppins-Medium.ttf",
        "bold": "Poppins-Bold.ttf",
    }[weight]
    return ImageFont.truetype(str(FONTS / name), size)


def load_image(path: Path) -> Image.Image:
    if path.suffix.lower() == ".svg":
        tmp = BUILD / f"{path.stem}.png"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(path),
                "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white",
                str(tmp),
            ],
            check=True,
            capture_output=True,
        )
        return Image.open(tmp).convert("RGB")
    img = Image.open(path).convert("RGB")
    return ImageOps.fit(img, (W, H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def darken(img: Image.Image, factor: float = 0.55) -> Image.Image:
    overlay = Image.new("RGB", img.size, BG_DARK)
    return Image.blend(img, overlay, factor)


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    y_start: int,
    fnt: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    line_gap: int = 12,
) -> int:
    sizes = [draw.textbbox((0, 0), line, font=fnt) for line in lines]
    heights = [bb[3] - bb[1] for bb in sizes]
    total = sum(heights) + line_gap * (len(lines) - 1)
    y = y_start - total // 2
    for line, h in zip(lines, heights):
        bb = draw.textbbox((0, 0), line, font=fnt)
        tw = bb[2] - bb[0]
        draw.text(((W - tw) // 2, y), line, font=fnt, fill=fill)
        y += h + line_gap
    return y


def wrap_text(text: str, width: int = 28) -> list[str]:
    return textwrap.wrap(text, width=width) or [text]


def make_text_card(
    lines: list[str],
    subtitle: str | None = None,
    bg: tuple[int, int, int] = BG_DARK,
) -> Image.Image:
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    title_font = font(64, "light")
    sub_font = font(28, "regular")
    draw_centered_text(draw, lines, H // 2 - (20 if subtitle else 0), title_font, IVORY)
    if subtitle:
        bb = draw.textbbox((0, 0), subtitle, font=sub_font)
        tw = bb[2] - bb[0]
        draw.text(((W - tw) // 2, H // 2 + 60), subtitle, font=sub_font, fill=GOLD)
    return img


def make_scene(
    background: Image.Image,
    title: str,
    subtitle: str | None = None,
    label: str | None = None,
) -> Image.Image:
    base = darken(background, 0.45)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # bottom gradient scrim
    for i in range(H // 2):
        alpha = int(180 * (i / (H // 2)) ** 1.4)
        draw.line([(0, H - i - 1), (W, H - i - 1)], fill=(13, 23, 31, alpha))

    title_font = font(52, "medium")
    sub_font = font(26, "light")
    label_font = font(18, "regular")

    title_lines = wrap_text(title, 22)
    y = H - 180
    for line in reversed(title_lines):
        bb = draw.textbbox((0, 0), line, font=title_font)
        tw = bb[2] - bb[0]
        th = bb[3] - bb[1]
        draw.text(((W - tw) // 2, y - th), line, font=title_font, fill=(*WHITE, 255))
        y -= th + 8

    if subtitle:
        bb = draw.textbbox((0, 0), subtitle, font=sub_font)
        tw = bb[2] - bb[0]
        draw.text(((W - tw) // 2, H - 110), subtitle, font=sub_font, fill=(*GOLD, 255))

    if label:
        draw.text((48, 48), label, font=label_font, fill=(*IVORY, 200))

    return Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")


def make_logo_intro() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_DARK)
    logo = Image.open(ROOT / "logo-dark-bg.png").convert("RGBA")
    max_w = int(W * 0.62)
    ratio = max_w / logo.width
    logo = logo.resize((max_w, int(logo.height * ratio)), Image.Resampling.LANCZOS)
    x = (W - logo.width) // 2
    y = (H - logo.height) // 2
    img.paste(logo, (x, y), logo)
    return img


def make_end_card() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    logo = Image.open(ROOT / "logo-dark-bg.png").convert("RGBA")
    max_w = int(W * 0.5)
    ratio = max_w / logo.width
    logo = logo.resize((max_w, int(logo.height * ratio)), Image.Resampling.LANCZOS)
    x = (W - logo.width) // 2
    y = H // 2 - logo.height // 2 - 60
    img.paste(logo, (x, y), logo)

    site_font = font(36, "regular")
    study_font = font(24, "light")
    site = "2-22church.com"
    study = "Decagon DNA · The Creator's pattern in Tabernacle and genome"
    for text, fnt, fill, offset in [
        (site, site_font, GOLD, 90),
        (study, study_font, MUTED, 140),
    ]:
        bb = draw.textbbox((0, 0), text, font=fnt)
        tw = bb[2] - bb[0]
        draw.text(((W - tw) // 2, y + logo.height + offset), text, font=fnt, fill=fill)
    return img


def save_frame(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, quality=95)


def render_clip(name: str, img: Image.Image, duration: float, zoom: bool = True) -> Path:
    png = BUILD / f"{name}.png"
    mp4 = BUILD / f"{name}.mp4"
    save_frame(img, png)
    frames = max(1, int(duration * FPS))
    vf = f"scale={W}:{H}"
    if zoom:
        vf = (
            f"zoompan=z='min(zoom+0.0008,1.12)':d={frames}:"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}"
        )
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(png),
        "-vf", vf,
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        str(mp4),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return mp4


def render_logo_fade(duration: float = 4.0) -> Path:
    png = BUILD / "logo_intro.png"
    mp4 = BUILD / "logo_intro.mp4"
    save_frame(make_logo_intro(), png)
    frames = int(duration * FPS)
    fade_in = int(1.2 * FPS)
    fade_out = int(0.8 * FPS)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(png),
        "-vf", (
            f"scale={W}:{H},format=yuv420p,"
            f"fade=t=in:st=0:d={fade_in / FPS:.3f},"
            f"fade=t=out:st={duration - fade_out / FPS:.3f}:d={fade_out / FPS:.3f}"
        ),
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        str(mp4),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return mp4


def build_ambient_audio(duration: float, path: Path) -> None:
    """Soft ambient pad (no copyrighted music)."""
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"sine=frequency=110:duration={duration}:sample_rate=44100",
        "-f", "lavfi", "-i", f"sine=frequency=164.81:duration={duration}:sample_rate=44100",
        "-f", "lavfi", "-i", f"sine=frequency=220:duration={duration}:sample_rate=44100",
        "-f", "lavfi", "-i", f"anoisesrc=d={duration}:c=pink:a=0.012",
        "-filter_complex",
        (
            "[0:a][1:a][2:a]amix=inputs=3:duration=first,volume=0.08[tones];"
            "[3:a]afade=t=in:st=0:d=3,afade=t=out:st={fade_out}:d=4[noise];"
            "[tones][noise]amix=inputs=2:duration=first,"
            "lowpass=f=800,highpass=f=60,volume=0.9[aout]"
        ).format(fade_out=max(0, duration - 4)),
        "-map", "[aout]",
        "-c:a", "aac", "-b:a", "192k",
        str(path),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def concat_with_xfade(clips: list[tuple[Path, float]], xfade: float = 0.45) -> Path:
    """Concatenate clips with crossfades."""
    if len(clips) == 1:
        return clips[0][0]

    # Build filter graph for xfade chain
    inputs = []
    for i, (path, _) in enumerate(clips):
        inputs.extend(["-i", str(path)])

    filters = []
    offset = clips[0][1] - xfade
    prev = "[0:v]"
    for i in range(1, len(clips)):
        nxt = f"[{i}:v]"
        out = f"[v{i}]" if i < len(clips) - 1 else "[vout]"
        filters.append(
            f"{prev}{nxt}xfade=transition=fade:duration={xfade}:offset={offset:.3f}{out}"
        )
        prev = out
        offset += clips[i][1] - xfade

    out_path = BUILD / "montage_noaudio.mp4"
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", ";".join(filters),
        "-map", "[vout]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(out_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return out_path


def mux_audio(video: Path, audio: Path, output: Path) -> None:
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video),
        "-i", str(audio),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(output),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def main() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    assets = ROOT / "blog-assets" / "dna-tabernacle"

    scenes: list[tuple[Image.Image, float, bool]] = []

    # Logo intro handled separately
    scenes.append((
        make_text_card(
            ["This video is about you"],
            subtitle="and your place before the Creator of Scripture",
        ),
        3.2,
        False,
    ))
    scenes.append((
        make_text_card(
            ["A Geometric Code"],
            subtitle="connecting Sinai, the genome, and the God of the Bible",
        ),
        2.8,
        False,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "dna-double-helix-render.jpg"),
            "Golden ratio φ",
            "written into life by the Creator's measure",
            "Genesis 1 · He formed man",
        ),
        3.5,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "tabernacle-decagon-topview-tribes.jpg"),
            "Ten-fold symmetry",
            "the pattern God gave Moses on the mount",
            "~1400 BC · Exodus 25",
        ),
        3.5,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "topview-tabernacle-dna-compare.jpg"),
            "As above · so below",
            "God's dwelling · the cell He formed",
        ),
        4.0,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(ROOT / "dna-tabernacle-pi-314.svg"),
            "314 cubits",
            "π in the curtains the LORD commanded Moses",
            "Exodus 26 · Project314",
        ),
        3.5,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(ROOT / "dna-tabernacle-three-scales.svg"),
            "Pattern · Tent · Helix",
            "one Author · three scales of one dwelling",
        ),
        3.5,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(ROOT / "dna-tabernacle-tenfold.svg"),
            "Ten pentagons about a decagon",
            "design in the molecule that stores life's text",
            "Curtis 1997 · Larsen 2021",
        ),
        3.8,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "dna-cymatics-spectrum.jpg"),
            "Witness the beauty of sound",
            "frequency and form before the Creator",
        ),
        3.5,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "cell-nucleus-cross-section.jpg"),
            "Your body is the temple",
            "of the Holy Spirit · 1 Corinthians 6:19",
        ),
        4.0,
        True,
    ))
    scenes.append((
        make_scene(
            load_image(assets / "tabernacle-wilderness-court.jpg"),
            "The Word tabernacled among us",
            "the Creator drew near · John 1:14",
        ),
        3.5,
        True,
    ))
    scenes.append((make_end_card(), 5.0, False))

    print("Rendering logo intro…")
    logo_clip = render_logo_fade(4.0)

    print("Rendering scene clips…")
    clip_paths: list[tuple[Path, float]] = [(logo_clip, 4.0)]
    for i, (img, dur, zoom) in enumerate(scenes):
        print(f"  scene {i + 1}/{len(scenes)} ({dur}s)")
        clip_paths.append((render_clip(f"scene_{i:02d}", img, dur, zoom=zoom), dur))

    total_dur = sum(d for _, d in clip_paths) - 0.45 * (len(clip_paths) - 1)
    print(f"Concatenating {len(clip_paths)} clips (~{total_dur:.1f}s)…")
    montage = concat_with_xfade(clip_paths, xfade=0.45)

    audio_path = BUILD / "ambient.aac"
    print("Generating ambient audio…")
    build_ambient_audio(total_dur + 0.5, audio_path)

    print(f"Writing {OUTPUT}…")
    mux_audio(montage, audio_path, OUTPUT)

    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"Done: {OUTPUT} ({size_mb:.1f} MB, ~{total_dur:.0f}s)")


if __name__ == "__main__":
    main()
