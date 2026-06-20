#!/usr/bin/env python3
"""Generate Decagon DNA / Tabernacle comparison SVGs (UTF-8 XML)."""

import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
INK = "#172A36"
BG = "#EEF4F7"
MUTED = "#47545B"
GOLD = "#8B6914"
ACCENT = "#5B8DB8"


def write(name, content):
    path = OUT / name
    path.write_text(content, encoding="utf-8")
    print("wrote", path.name)


def decagon_points(cx, cy, radius, start_deg=-90):
    """Return SVG polygon points string for a regular decagon (10 sides)."""
    pts = []
    for i in range(10):
        ang = math.radians(start_deg + i * 36)
        x = cx + radius * math.cos(ang)
        y = cy + radius * math.sin(ang)
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def decagon_vertices(cx, cy, radius, start_deg=-90):
    """Return list of (x, y) vertex coordinates for a regular decagon."""
    verts = []
    for i in range(10):
        ang = math.radians(start_deg + i * 36)
        verts.append((cx + radius * math.cos(ang), cy + radius * math.sin(ang)))
    return verts


def decagon_svg(cx, cy, radius, stroke, fill, stroke_width=2, start_deg=-90, show_vertices=False, vertex_fill=INK):
    points = decagon_points(cx, cy, radius, start_deg)
    parts = [f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round"/>']
    if show_vertices:
        for i, (x, y) in enumerate(decagon_vertices(cx, cy, radius, start_deg), start=1):
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{vertex_fill}" opacity="0.85"/>')
            if i in (1, 4, 7, 10):
                parts.append(
                    f'<text x="{x:.1f}" y="{y - 8:.1f}" text-anchor="middle" '
                    f'font-family="Arial,Helvetica,sans-serif" font-size="6" fill="{MUTED}">{i}</text>'
                )
    return "\n  ".join(parts)


def radial_spokes(cx, cy, radius, stroke, start_deg=-90):
    lines = []
    for x, y in decagon_vertices(cx, cy, radius, start_deg):
        lines.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{stroke}" stroke-width="0.8" opacity="0.35"/>')
    return "\n  ".join(lines)


def three_scales():
    w, h = 960, 520
    tab_dec = decagon_svg(480, 268, 158, GOLD, "rgba(139,105,20,0.08)", show_vertices=True, vertex_fill=GOLD)
    dna_dec = decagon_svg(480, 268, 72, ACCENT, "rgba(91,141,184,0.12)", show_vertices=True, vertex_fill=ACCENT)
    dna_spokes = radial_spokes(480, 268, 72, ACCENT)
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Three scales of dwelling: heavenly pattern, Tabernacle, DNA decagon</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="10" fill="{BG}" stroke="{INK}" stroke-width="2"/>
  <text x="{w//2}" y="48" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{INK}">THREE SCALES OF DWELLING</text>
  <text x="{w//2}" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10" fill="{MUTED}">Regular decagons · 10 sides · 36° between vertices</text>

  <circle cx="480" cy="268" r="210" fill="none" stroke="{INK}" stroke-width="1.5" opacity="0.25" stroke-dasharray="8 6"/>
  <text x="480" y="88" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{MUTED}">HEAVENLY PATTERN · before ~1400 BC</text>

  {tab_dec}
  <text x="480" y="118" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">WILDERNESS TABERNACLE DECAGON · ~1400 BC</text>

  {dna_dec}
  {dna_spokes}
  <circle cx="480" cy="268" r="22" fill="none" stroke="{ACCENT}" stroke-width="1.2" opacity="0.6"/>
  <text x="480" y="262" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="{ACCENT}">10</text>
  <text x="480" y="278" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">bases / turn</text>
  <text x="480" y="368" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">B-DNA AXIAL DECAGON</text>
  <text x="480" y="382" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">10 vertices · 36° per base · φ ratios · 1953–2021</text>

  <text x="480" y="455" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-style="italic" fill="{MUTED}">Hebrews 8:5 shadow · Exodus copy · genome as living text</text>
  <text x="480" y="478" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">1 Corinthians 6:19 · your body is the temple of the Holy Spirit</text>
</svg>'''
    write("dna-tabernacle-three-scales.svg", body)


def tenfold():
    w, h = 960, 420
    left_dec = decagon_svg(240, 195, 92, GOLD, "rgba(139,105,20,0.1)", show_vertices=True, vertex_fill=GOLD)
    left_spokes = radial_spokes(240, 195, 92, GOLD)
    right_dec = decagon_svg(720, 195, 92, ACCENT, "rgba(91,141,184,0.1)", show_vertices=True, vertex_fill=ACCENT)
    right_spokes = radial_spokes(720, 195, 92, ACCENT)
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Ten-fold symmetry: Tabernacle decagon and DNA axial decagon</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" letter-spacing="0.1em" fill="{INK}">TEN AS STRUCTURAL GRAMMAR</text>
  <text x="{w//2}" y="56" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{MUTED}">Each shape is a regular decagon · 10 sides · 10 vertices</text>
  <line x1="{w//2}" y1="64" x2="{w//2}" y2="{h-40}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <text x="240" y="82" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">TABERNACLE DECAGON (~1400 BC)</text>
  {left_dec}
  {left_spokes}
  <circle cx="240" cy="195" r="16" fill="none" stroke="{INK}" stroke-width="1"/>
  <text x="240" y="199" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{INK}">Ark</text>
  <text x="240" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Andrew Hoy · Project314 · yurt dome</text>
  <text x="240" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">ten-sided dwelling · six stories (model)</text>

  <text x="720" y="82" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">B-DNA AXIAL DECAGON</text>
  {right_dec}
  {right_spokes}
  <text x="720" y="199" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="18" font-weight="700" fill="{ACCENT}">10</text>
  <text x="720" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">10 base pairs · 36° rotation each</text>
  <text x="720" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Curtis 1997 · Larsen Symmetry 2021</text>

  <text x="{w//2}" y="360" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">360° ÷ 10 = 36° · π/5 radians · golden-triangle angle</text>
  <text x="{w//2}" y="378" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-style="italic" fill="{MUTED}">Sinai precedes the laboratory by more than three millennia</text>
</svg>'''
    write("dna-tabernacle-tenfold.svg", body)


def pi_314():
    w, h = 960, 380
    # Decagon cross-section hint on helix side
    helix_dec = decagon_svg(720, 215, 48, ACCENT, "rgba(91,141,184,0.08)", stroke_width=1.5)
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>314 cubits and helical circle: pi in Tabernacle curtains and DNA turn</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" fill="{INK}">π AND CIRCULAR MEASURE</text>
  <line x1="{w//2}" y1="52" x2="{w//2}" y2="{h-36}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <text x="240" y="72" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">EXODUS CURTAIN CYLINDER</text>
  <ellipse cx="240" cy="200" rx="90" ry="28" fill="none" stroke="{GOLD}" stroke-width="2"/>
  <line x1="150" y1="200" x2="150" y2="280" stroke="{GOLD}" stroke-width="1.5"/>
  <line x1="330" y1="200" x2="330" y2="280" stroke="{GOLD}" stroke-width="1.5"/>
  <ellipse cx="240" cy="280" rx="90" ry="28" fill="rgba(139,105,20,0.06)" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="240" y="205" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="{GOLD}">314</text>
  <text x="240" y="222" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">cubits circumference</text>
  <text x="240" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">(30×11) − (30÷2) − 1 = 314</text>
  <text x="240" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">π × 100 · court diameter 100 cubits</text>

  <text x="720" y="72" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">DNA HELICAL TURN</text>
  <path d="M640 280 Q680 120 720 200 T800 280" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
  <path d="M640 300 Q680 140 720 220 T800 300" fill="none" stroke="{ACCENT}" stroke-width="2.5" opacity="0.5"/>
  {helix_dec}
  <text x="720" y="200" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">pitch ~34Å · axial decagon</text>
  <text x="720" y="214" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">width ~21Å</text>
  <text x="720" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">10 bases per 360° turn</text>
  <text x="720" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">φ ratio length:width (Larsen 2021)</text>

  <text x="{w//2}" y="358" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-style="italic" fill="{MUTED}">Circle encoded in linen before Greece named π · circle encoded in the information molecule</text>
</svg>'''
    write("dna-tabernacle-pi-314.svg", body)


def zones():
    w, h = 960, 520
    # Tabernacle as decagon outer court with nested zones
    outer_pts = decagon_points(240, 245, 165)
    holy_pts = decagon_points(240, 245, 115)
    inner_pts = decagon_points(240, 245, 62)
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Three zones: Tabernacle graded sanctity and cell structure</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" fill="{INK}">THREE ZONES INWARD</text>
  <line x1="{w//2}" y1="52" x2="{w//2}" y2="{h-40}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <text x="240" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">TABERNACLE DECAGON (~1400 BC)</text>
  <polygon points="{outer_pts}" fill="#FFF" stroke="{INK}" stroke-width="1" opacity="0.5"/>
  <text x="240" y="92" text-anchor="middle" font-size="7" fill="{MUTED}">Outer Court</text>
  <polygon points="{holy_pts}" fill="rgba(139,105,20,0.06)" stroke="{GOLD}" stroke-width="1.2"/>
  <text x="240" y="148" text-anchor="middle" font-size="7" fill="{MUTED}">Holy Place</text>
  <polygon points="{inner_pts}" fill="rgba(139,105,20,0.14)" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="240" y="198" text-anchor="middle" font-size="7" fill="{MUTED}">Holy of Holies</text>
  <circle cx="240" cy="245" r="22" fill="{GOLD}" opacity="0.3" stroke="{INK}" stroke-width="1"/>
  <text x="240" y="249" text-anchor="middle" font-size="7" font-weight="700" fill="{INK}">Ark</text>
  <text x="240" y="430" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">decagon court → priestly hall → Ark at centre</text>

  <text x="720" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">LIVING CELL</text>
  <circle cx="720" cy="245" r="150" fill="#FFF" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="720" y="108" text-anchor="middle" font-size="7" fill="{MUTED}">cell membrane (Outer Court)</text>
  <circle cx="720" cy="245" r="95" fill="rgba(91,141,184,0.08)" stroke="{ACCENT}" stroke-width="1.2"/>
  <text x="720" y="168" text-anchor="middle" font-size="7" fill="{MUTED}">cytoplasm · organelles (Holy Place)</text>
  <circle cx="720" cy="245" r="45" fill="rgba(91,141,184,0.18)" stroke="{INK}" stroke-width="1.5"/>
  <text x="720" y="242" text-anchor="middle" font-size="7" font-weight="700" fill="{INK}">nucleus</text>
  <text x="720" y="254" text-anchor="middle" font-size="6" fill="{MUTED}">DNA · chromatin</text>
  <text x="720" y="430" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">membrane → metabolism → genome at centre</text>

  <text x="{w//2}" y="475" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">Paul: your body is the temple of the Holy Spirit (1 Corinthians 6:19)</text>
  <text x="{w//2}" y="494" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-style="italic" fill="{MUTED}">graded access · information guarded at the centre · Spirit as indwelling Glory</text>
</svg>'''
    write("dna-tabernacle-zones.svg", body)


if __name__ == "__main__":
    three_scales()
    tenfold()
    pi_314()
    zones()
    print("done")
