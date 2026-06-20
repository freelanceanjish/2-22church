#!/usr/bin/env python3
"""Generate Decagon DNA / Tabernacle comparison SVGs (UTF-8 XML)."""

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


def three_scales():
    w, h = 960, 520
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Three scales of dwelling: heavenly pattern, Tabernacle, DNA decagon</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="16" y="16" width="{w-32}" height="{h-32}" rx="10" fill="{BG}" stroke="{INK}" stroke-width="2"/>
  <text x="{w//2}" y="48" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" letter-spacing="0.12em" fill="{INK}">THREE SCALES OF DWELLING</text>
  <text x="{w//2}" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10" fill="{MUTED}">Same grammar at heaven, tent, and genome</text>

  <!-- Outer ring: heavenly pattern -->
  <circle cx="480" cy="280" r="210" fill="none" stroke="{INK}" stroke-width="1.5" opacity="0.25" stroke-dasharray="8 6"/>
  <text x="480" y="78" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{MUTED}">HEAVENLY PATTERN</text>
  <text x="480" y="92" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">shown to Moses on the mount · before ~1400 BC</text>

  <!-- Middle ring: tabernacle decagon -->
  <polygon points="480,110 598,145 633,263 598,381 480,416 362,381 327,263 362,145" fill="rgba(139,105,20,0.08)" stroke="{GOLD}" stroke-width="2"/>
  <text x="480" y="128" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">WILDERNESS TABERNACLE</text>
  <text x="480" y="142" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">decagon dome · π-scaled court · ~1400 BC Sinai</text>

  <!-- Inner: DNA decagon axial -->
  <polygon points="480,175 545,195 565,260 545,325 480,345 415,325 395,260 415,195" fill="rgba(91,141,184,0.12)" stroke="{ACCENT}" stroke-width="2"/>
  <circle cx="480" cy="260" r="28" fill="none" stroke="{ACCENT}" stroke-width="1.2" opacity="0.6"/>
  <text x="480" y="252" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="22" font-weight="700" fill="{ACCENT}">10</text>
  <text x="480" y="272" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">bases / turn</text>
  <text x="480" y="368" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">B-DNA AXIAL DECAGON</text>
  <text x="480" y="382" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">36° per base · φ ratios · creation / described 1953–2021</text>

  <!-- Arrows inward -->
  <path d="M480 200 L480 218" stroke="{INK}" stroke-width="1" marker-end="url(#arr)"/>
  <path d="M480 330 L480 348" stroke="{INK}" stroke-width="1" opacity="0.5"/>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{INK}"/></marker></defs>

  <text x="480" y="455" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-style="italic" fill="{MUTED}">Hebrews 8:5 shadow · Exodus copy · genome as living text</text>
  <text x="480" y="478" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">1 Corinthians 6:19 · your body is the temple of the Holy Spirit</text>
</svg>'''
    write("dna-tabernacle-three-scales.svg", body)


def tenfold():
    w, h = 960, 420
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Ten-fold symmetry: Tabernacle decagon and DNA axial decagon</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" letter-spacing="0.1em" fill="{INK}">TEN AS STRUCTURAL GRAMMAR</text>
  <line x1="{w//2}" y1="52" x2="{w//2}" y2="{h-40}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <!-- Left: tabernacle decagon top view -->
  <text x="240" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">TABERNACLE DECAGON (~1400 BC)</text>
  <polygon points="240,100 310,118 328,188 310,258 240,276 170,258 152,188 170,118" fill="rgba(139,105,20,0.1)" stroke="{GOLD}" stroke-width="2"/>
  <circle cx="240" cy="188" r="18" fill="none" stroke="{INK}" stroke-width="1"/>
  <text x="240" cy="188" y="192" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{INK}">Ark</text>
  <text x="240" y="300" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Andrew Hoy · Project314 · yurt dome</text>
  <text x="240" y="314" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">ten-sided dwelling · six stories (model)</text>

  <!-- Right: DNA axial -->
  <text x="720" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">B-DNA AXIAL VIEW</text>
  <polygon points="720,100 790,118 808,188 790,258 720,276 650,258 632,188 650,118" fill="rgba(91,141,184,0.1)" stroke="{ACCENT}" stroke-width="2"/>
  <g stroke="{ACCENT}" stroke-width="1.2" fill="none" opacity="0.7">
    <line x1="720" y1="188" x2="808" y2="188"/>
    <line x1="744" y1="112" x2="696" y2="264"/>
    <line x1="696" y1="112" x2="744" y2="264"/>
  </g>
  <text x="720" y="192" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="18" font-weight="700" fill="{ACCENT}">10</text>
  <text x="720" y="300" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">10 base pairs · 36° rotation each</text>
  <text x="720" y="314" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Curtis 1997 · Larsen Symmetry 2021</text>

  <text x="{w//2}" y="360" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">360° ÷ 10 = 36° · π/5 radians · golden-triangle angle</text>
  <text x="{w//2}" y="378" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-style="italic" fill="{MUTED}">Sinai precedes the laboratory by more than three millennia</text>
</svg>'''
    write("dna-tabernacle-tenfold.svg", body)


def pi_314():
    w, h = 960, 380
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>314 cubits and helical circle: pi in Tabernacle curtains and DNA turn</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" fill="{INK}">π AND CIRCULAR MEASURE</text>
  <line x1="{w//2}" y1="52" x2="{w//2}" y2="{h-36}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <!-- Left: cylinder 314 -->
  <text x="240" y="72" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">EXODUS CURTAIN CYLINDER</text>
  <ellipse cx="240" cy="200" rx="90" ry="28" fill="none" stroke="{GOLD}" stroke-width="2"/>
  <line x1="150" y1="200" x2="150" y2="280" stroke="{GOLD}" stroke-width="1.5"/>
  <line x1="330" y1="200" x2="330" y2="280" stroke="{GOLD}" stroke-width="1.5"/>
  <ellipse cx="240" cy="280" rx="90" ry="28" fill="rgba(139,105,20,0.06)" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="240" y="205" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="{GOLD}">314</text>
  <text x="240" y="222" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">cubits circumference</text>
  <text x="240" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">(30×11) − (30÷2) − 1 = 314</text>
  <text x="240" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">π × 100 · court diameter 100 cubits</text>

  <!-- Right: helix turn -->
  <text x="720" y="72" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">DNA HELICAL TURN</text>
  <path d="M640 280 Q680 120 720 200 T800 280" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
  <path d="M640 300 Q680 140 720 220 T800 300" fill="none" stroke="{ACCENT}" stroke-width="2.5" opacity="0.5"/>
  <text x="720" y="200" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">pitch ~34Å</text>
  <text x="720" y="214" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">width ~21Å</text>
  <text x="720" y="310" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">10 bases per 360° turn</text>
  <text x="720" y="324" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">φ ratio length:width (Larsen 2021)</text>

  <text x="{w//2}" y="358" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-style="italic" fill="{MUTED}">Circle encoded in linen before Greece named π · circle encoded in the information molecule</text>
</svg>'''
    write("dna-tabernacle-pi-314.svg", body)


def zones():
    w, h = 960, 520
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>Three zones: Tabernacle graded sanctity and cell structure</title>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>
  <text x="{w//2}" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700" fill="{INK}">THREE ZONES INWARD</text>
  <line x1="{w//2}" y1="52" x2="{w//2}" y2="{h-40}" stroke="{INK}" stroke-width="1" opacity="0.2"/>

  <!-- Tabernacle nested -->
  <text x="240" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{GOLD}">TABERNACLE (~1400 BC)</text>
  <rect x="60" y="85" width="360" height="300" fill="#FFF" stroke="{INK}" stroke-width="1" opacity="0.4"/>
  <text x="240" y="102" text-anchor="middle" font-size="7" fill="{MUTED}">Outer Court</text>
  <rect x="100" y="115" width="280" height="220" fill="rgba(139,105,20,0.06)" stroke="{GOLD}" stroke-width="1.2"/>
  <text x="240" y="132" text-anchor="middle" font-size="7" fill="{MUTED}">Holy Place</text>
  <rect x="160" y="165" width="160" height="120" fill="rgba(139,105,20,0.12)" stroke="{GOLD}" stroke-width="1.5"/>
  <text x="240" y="182" text-anchor="middle" font-size="7" fill="{MUTED}">Holy of Holies</text>
  <rect x="200" y="200" width="80" height="50" fill="{GOLD}" opacity="0.25" stroke="{INK}" stroke-width="1"/>
  <text x="240" y="228" text-anchor="middle" font-size="7" font-weight="700" fill="{INK}">Ark</text>
  <text x="240" y="400" text-anchor="middle" font-size="8" fill="{MUTED}">altar · laver → lamp · bread · incense → Ark</text>

  <!-- Cell nested -->
  <text x="720" y="68" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{ACCENT}">LIVING CELL</text>
  <circle cx="720" cy="235" r="150" fill="#FFF" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="720" y="100" text-anchor="middle" font-size="7" fill="{MUTED}">cell membrane (Outer Court)</text>
  <circle cx="720" cy="235" r="95" fill="rgba(91,141,184,0.08)" stroke="{ACCENT}" stroke-width="1.2"/>
  <text x="720" y="155" text-anchor="middle" font-size="7" fill="{MUTED}">cytoplasm · organelles (Holy Place)</text>
  <circle cx="720" cy="235" r="45" fill="rgba(91,141,184,0.18)" stroke="{INK}" stroke-width="1.5"/>
  <text x="720" y="232" text-anchor="middle" font-size="7" font-weight="700" fill="{INK}">nucleus</text>
  <text x="720" y="244" text-anchor="middle" font-size="6" fill="{MUTED}">DNA · chromatin</text>
  <text x="720" y="400" text-anchor="middle" font-size="8" fill="{MUTED}">membrane → metabolism → genome at centre</text>

  <text x="{w//2}" y="455" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">Paul: your body is the temple of the Holy Spirit (1 Corinthians 6:19)</text>
  <text x="{w//2}" y="478" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-style="italic" fill="{MUTED}">graded access · information guarded at the centre · Spirit as indwelling Glory</text>
</svg>'''
    write("dna-tabernacle-zones.svg", body)


if __name__ == "__main__":
    three_scales()
    tenfold()
    pi_314()
    zones()
    print("done")
