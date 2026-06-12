#!/usr/bin/env python3
"""Generate SVG diagrams for the Vedic-Hebrew zodiac calendar article."""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
INK = "#172A36"
BG = "#EEF4F7"
MUTED = "#47545B"
GOLD = "#2A4A5E"
WHITE = "#FFFFFF"
FONT = "'Noto Sans Devanagari', 'Arial Unicode MS', sans-serif"


def wrap(title, body, w=680, h=320):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>{title}</title>
  <rect width="{w}" height="{h}" fill="{BG}"/>
  {body}
</svg>
'''


def write(name, content):
    path = OUT / name
    path.write_text(content, encoding="utf-8")
    print("wrote", path.name)


def wheel(cx, cy, r, labels, title, subtitle):
    segs = len(labels)
    import math
    parts = [f'<text x="{cx}" y="22" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="0.1em" fill="{INK}">{title}</text>']
    if subtitle:
        parts.append(f'<text x="{cx}" y="38" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">{subtitle}</text>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.4" opacity="0.35"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.55}" fill="rgba(23,42,54,0.06)" stroke="{INK}" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{INK}"/>')
    parts.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{WHITE}">12</text>')
    for i, label in enumerate(labels):
        ang = math.radians(-90 + (360 / segs) * i + (360 / segs) / 2)
        x1 = cx + (r * 0.55) * math.cos(ang)
        y1 = cy + (r * 0.55) * math.sin(ang)
        x2 = cx + (r * 0.82) * math.cos(ang)
        y2 = cy + (r * 0.82) * math.sin(ang)
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="0.6" opacity="0.25"/>')
        tx = cx + (r * 0.92) * math.cos(ang)
        ty = cy + (r * 0.92) * math.sin(ang)
        parts.append(
            f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="6.5" fill="{INK}">{label}</text>'
        )
    return "\n  ".join(parts)


def svg_wheel():
    rashi = ["Mesha", "Vrish", "Mith", "Kark", "Simh", "Kany", "Tula", "Vris", "Dhan", "Makr", "Kumb", "Meen"]
    mazzal = ["T'leh", "Shor", "T'um", "Sart", "Arye", "Betu", "Mozn", "Akra", "Kesh", "Gedi", "D'li", "Dagi"]
    body = f'''
  <line x1="340" y1="48" x2="340" y2="300" stroke="{INK}" stroke-width="1" opacity="0.15"/>
  {wheel(170, 175, 95, rashi, "RASHI CHAKRA", "वैदिक · 12 signs")}
  {wheel(510, 175, 95, mazzal, "MAZZAROTH", "עברי · 12 signs")}
  <text x="340" y="305" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Same belt of constellations · different names · one sky</text>
'''
    write("astro-12-sign-wheel.svg", wrap("Twelve sign wheels: Rashi Chakra and Mazzaroth", body, h=320))


def svg_drift():
    body = f'''
  <text x="340" y="24" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="0.1em" fill="{INK}">LUNI-SOLAR DRIFT (WHY A 13TH MONTH EXISTS)</text>
  <text x="340" y="42" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">12 lunar months ≈ 354 days · solar year ≈ 365 days · gap ≈ 11 days per year</text>
  <rect x="60" y="70" width="560" height="36" rx="4" fill="#FFF" stroke="{INK}" stroke-width="1"/>
  <rect x="60" y="70" width="420" height="36" rx="4" fill="rgba(23,42,54,0.12)"/>
  <text x="80" y="93" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">Solar year (seasons / festivals)</text>
  <text x="500" y="93" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">365 d</text>
  <rect x="60" y="120" width="560" height="36" rx="4" fill="#FFF" stroke="{INK}" stroke-width="1"/>
  <rect x="60" y="120" width="408" height="36" rx="4" fill="rgba(23,42,54,0.08)"/>
  <text x="80" y="143" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">12 lunar months (Molad / Chandramana)</text>
  <text x="500" y="143" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{INK}">354 d</text>
  <path d="M 340 170 L 340 200" stroke="{GOLD}" stroke-width="1.5" marker-end="url(#arr)"/>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{GOLD}"/></marker></defs>
  <rect x="220" y="205" width="240" height="52" rx="6" fill="{INK}"/>
  <text x="340" y="228" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="600" fill="{WHITE}">~11 day drift each year</text>
  <text x="340" y="244" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="#A8C4DC">Corrected by leap month · not a 13th sign</text>
  <text x="120" y="285" font-family="{FONT}" font-size="10" fill="{INK}">अधिक मास</text>
  <text x="120" y="300" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Adhika Masa (Vedic)</text>
  <text x="480" y="285" font-family="{FONT}" font-size="10" fill="{INK}">אדר א׳</text>
  <text x="480" y="300" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Adar I (Jewish)</text>
'''
    write("astro-lunar-solar-drift.svg", wrap("Lunar-solar drift and leap month correction", body, h=320))


def svg_leap():
    body = f'''
  <text x="340" y="24" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="0.1em" fill="{INK}">THE 13TH MONTH: REPEAT A SIGN, DO NOT INVENT ONE</text>
  <line x1="340" y1="40" x2="340" y2="300" stroke="{INK}" stroke-width="1" opacity="0.15"/>
  <text x="170" y="58" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">अधिक मास</text>
  <text x="510" y="58" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{INK}">אדר ראשון</text>
  <text x="170" y="74" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-weight="700" fill="{MUTED}">VEDIC MECHANISM</text>
  <text x="510" y="74" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-weight="700" fill="{MUTED}">JEWISH MECHANISM</text>
  <rect x="50" y="95" width="240" height="180" rx="6" fill="#FFF" stroke="{INK}" stroke-width="1"/>
  <text x="170" y="118" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{INK}">Lunar month with NO new Sankranti</text>
  <rect x="70" y="130" width="200" height="28" rx="3" fill="rgba(23,42,54,0.1)" stroke="{INK}" stroke-width="0.8"/>
  <text x="170" y="148" text-anchor="middle" font-size="8" fill="{INK}">Month N (regular)</text>
  <rect x="70" y="168" width="200" height="28" rx="3" fill="{INK}"/>
  <text x="170" y="186" text-anchor="middle" font-size="8" fill="{WHITE}">Adhika · shares next Rashi</text>
  <rect x="70" y="206" width="200" height="28" rx="3" fill="rgba(23,42,54,0.1)" stroke="{INK}" stroke-width="0.8"/>
  <text x="170" y="224" text-anchor="middle" font-size="8" fill="{INK}">Month N+1 (named twice that year)</text>
  <text x="170" y="258" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">Astronomy flags the extra month</text>
  <rect x="390" y="95" width="240" height="180" rx="6" fill="#FFF" stroke="{INK}" stroke-width="1"/>
  <text x="510" y="118" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{INK}">Metonic cycle · 7 leap years / 19 years</text>
  <rect x="410" y="130" width="200" height="28" rx="3" fill="rgba(23,42,54,0.1)" stroke="{INK}" stroke-width="0.8"/>
  <text x="510" y="148" text-anchor="middle" font-size="8" fill="{INK}">Shevat · Adar I · Adar II</text>
  <rect x="410" y="168" width="200" height="28" rx="3" fill="{INK}"/>
  <text x="510" y="186" text-anchor="middle" font-size="8" fill="{WHITE}">Both Adars = Dagim (Pisces)</text>
  <rect x="410" y="206" width="200" height="28" rx="3" fill="rgba(23,42,54,0.1)" stroke="{INK}" stroke-width="0.8"/>
  <text x="510" y="224" text-anchor="middle" font-size="8" fill="{INK}">Passover stays in spring</text>
  <text x="510" y="258" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">Mathematics schedules the extra month</text>
  <text x="340" y="300" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">12 signs remain · 13th month doubles one window</text>
'''
    write("astro-leap-month-mechanism.svg", wrap("Adhika Masa and Adar Rishon compared", body, h=320))


def svg_moon():
    body = f'''
  <text x="340" y="24" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="0.1em" fill="{INK}">MOON BEFORE SUN (BOTH TRADITIONS)</text>
  <text x="340" y="42" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Western horoscope emphasises Sun sign · Vedic &amp; Hebrew calendars centre the Moon</text>
  <circle cx="170" cy="155" r="48" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1.2"/>
  <circle cx="155" cy="140" r="22" fill="#D8E4EC" stroke="{INK}" stroke-width="0.8"/>
  <text x="170" y="220" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{INK}">जन्म राशि</text>
  <text x="170" y="238" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Janma Rashi · Moon sign</text>
  <text x="170" y="256" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">Nakshatra · lunar mansion</text>
  <circle cx="510" cy="155" r="48" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1.2"/>
  <circle cx="495" cy="140" r="22" fill="#D8E4EC" stroke="{INK}" stroke-width="0.8"/>
  <text x="510" y="220" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{INK}">ראש חודש</text>
  <text x="510" y="238" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Rosh Chodesh · new moon</text>
  <text x="510" y="256" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="{MUTED}">Molad · festival rhythm</text>
  <text x="340" y="290" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="{MUTED}">Renewal, seasons, and identity tied to lunar light</text>
'''
    write("astro-moon-primacy.svg", wrap("Moon primacy in Vedic and Jewish calendars", body, h=300))


if __name__ == "__main__":
    svg_wheel()
    svg_drift()
    svg_leap()
    svg_moon()
