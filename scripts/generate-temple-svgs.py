#!/usr/bin/env python3
# Generates temple comparison SVGs as valid UTF-8 XML (Devanagari + floor plans).

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
FONT = "'Noto Sans Devanagari', 'Arial Unicode MS', sans-serif"
INK = "#172A36"
BG = "#EEF4F7"
MUTED = "#47545B"
WHITE = "#FFFFFF"


def wrap(title, body, w=680, h=260):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <title>{title}</title>
  <rect width="{w}" height="{h}" fill="{BG}"/>
  {body}
</svg>
'''


def header(num, en_title, y=28):
    return f'''<text x="{680//2}" y="{y}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="0.12em" fill="{INK}">{num} - {en_title}</text>
  <line x1="{680//2}" y1="40" x2="{680//2}" y2="230" stroke="{INK}" stroke-width="1" opacity="0.18"/>'''


def col_labels(left, right, dev_left="", dev_right=""):
    d1 = f'''<text x="170" y="62" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{INK}">{dev_left}</text>''' if dev_left else ""
    d2 = f'''<text x="510" y="62" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{INK}">{dev_right}</text>''' if dev_right else ""
    return f'''{d1}{d2}
  <text x="170" y="78" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-weight="700" letter-spacing="0.1em" fill="{MUTED}">{left}</text>
  <text x="510" y="78" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" font-weight="700" letter-spacing="0.1em" fill="{MUTED}">{right}</text>'''


def write(name, content):
    path = OUT / name
    path.write_text(content, encoding="utf-8")
    print("wrote", path.name)


def svg_01_floorplan():
    body = f'''
  <text x="340" y="24" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" font-weight="700" fill="{INK}">01 - TEMPLE FLOOR PLAN (GRADED SANCTITY)</text>
  <line x1="340" y1="36" x2="340" y2="400" stroke="{INK}" stroke-width="1" opacity="0.15"/>
  <text x="170" y="48" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{INK}">दक्षिण भारतीय मंदिर</text>
  <text x="510" y="48" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="{MUTED}">TABERNACLE / TEMPLE</text>
  <!-- Hindu plan -->
  <rect x="40" y="60" width="260" height="320" fill="#FFF" stroke="{INK}" stroke-width="1.2"/>
  <rect x="55" y="75" width="230" height="50" fill="rgba(23,42,54,0.05)" stroke="{INK}" stroke-width="0.8"/>
  <text x="170" y="105" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{MUTED}">गोपुरम् · प्राकार</text>
  <rect x="70" y="140" width="200" height="90" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="170" y="168" text-anchor="middle" font-family="{FONT}" font-size="10" fill="{MUTED}">प्रदक्षिणा पथ</text>
  <rect x="95" y="200" width="150" height="70" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1"/>
  <text x="170" y="232" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{INK}">मण्डप</text>
  <rect x="125" y="285" width="90" height="70" fill="{INK}"/>
  <text x="170" y="318" text-anchor="middle" font-family="{FONT}" font-size="12" fill="#FFF">गर्भगृह</text>
  <text x="170" y="336" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="7" fill="#EAF1F4">one pujari</text>
  <!-- Hebrew plan -->
  <rect x="380" y="60" width="260" height="320" fill="#FFF" stroke="{INK}" stroke-width="1.2"/>
  <rect x="395" y="75" width="230" height="120" fill="rgba(23,42,54,0.04)" stroke="{INK}" stroke-width="0.8"/>
  <text x="510" y="100" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="9" fill="{MUTED}">OUTER COURT</text>
  <rect x="430" y="115" width="50" height="35" fill="{INK}" opacity="0.85"/>
  <text x="455" y="136" text-anchor="middle" font-size="7" fill="#FFF">altar</text>
  <ellipse cx="560" cy="132" rx="22" ry="14" fill="none" stroke="{INK}" stroke-width="1"/>
  <text x="560" y="136" text-anchor="middle" font-size="7" fill="{MUTED}">laver</text>
  <rect x="420" y="210" width="180" height="100" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1"/>
  <text x="510" y="238" text-anchor="middle" font-size="8" fill="{MUTED}">HOLY PLACE · menorah · bread</text>
  <line x1="500" y1="210" x2="500" y2="310" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="492" y="265" font-size="7" fill="{INK}">veil</text>
  <rect x="465" y="285" width="90" height="55" fill="{INK}"/>
  <text x="510" y="312" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="8" fill="#FFF">ARK</text>
  <text x="340" y="398" text-anchor="middle" font-size="10" fill="{INK}">Public → priestly → single minister at centre</text>
'''
    write("temple-compare-01-floorplan.svg", wrap("Temple floor plans", body, 680, 420))


def svg_01_zones():
    body = header("01", "GRADED SANCTITY (OVERVIEW)") + col_labels(
        "HINDU ZONES", "HEBREW ZONES", "वैदिक मंदिर", "מִשְׁכָּן"
    ) + f'''
  <circle cx="170" cy="155" r="68" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.35"/>
  <circle cx="170" cy="155" r="44" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1.2"/>
  <circle cx="170" cy="155" r="18" fill="{INK}"/>
  <text x="170" y="159" text-anchor="middle" font-family="{FONT}" font-size="9" fill="#FFF">गर्भगृह</text>
  <rect x="430" y="95" width="160" height="150" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.35"/>
  <rect x="450" y="115" width="120" height="110" fill="rgba(23,42,54,0.08)" stroke="{INK}" stroke-width="1.2"/>
  <rect x="478" y="143" width="64" height="54" fill="{INK}"/>
  <text x="510" y="175" text-anchor="middle" font-size="8" fill="#FFF">Holy of Holies</text>
'''
    write("temple-compare-01-zones.svg", wrap("Graded sanctity", body))


def svg_10_holika():
    body = header("10", "SACRED FIRE · BURNT OFFERING") + col_labels(
        "HOLIKA DAHAN / HAVAN", "OLAH · MIZBEACH", "होलिका दहन", "עֹלָה"
    ) + f'''
  <!-- Bonfire -->
  <ellipse cx="170" cy="200" rx="55" ry="12" fill="rgba(23,42,54,0.12)"/>
  <path d="M140 200 Q150 150 165 120 Q170 95 175 120 Q190 155 200 200 Z" fill="{INK}" opacity="0.75"/>
  <path d="M155 200 Q165 160 170 135 Q175 110 180 140 Q188 170 195 200 Z" fill="{INK}" opacity="0.5"/>
  <rect x="158" y="175" width="24" height="28" rx="2" fill="none" stroke="{INK}" stroke-width="1.2"/>
  <text x="170" y="228" text-anchor="middle" font-family="{FONT}" font-size="9" fill="{MUTED}">अग्नि · पाप दहन</text>
  <text x="170" y="242" text-anchor="middle" font-size="7" fill="{MUTED}">Havan kunda · spring Holi rite</text>
  <!-- Bronze altar -->
  <rect x="468" y="175" width="84" height="28" fill="{INK}"/>
  <rect x="448" y="168" width="124" height="8" fill="{INK}" opacity="0.5"/>
  <path d="M500 168 Q505 130 510 95 Q515 125 520 168" fill="none" stroke="{INK}" stroke-width="1.5" opacity="0.45"/>
  <path d="M488 168 Q492 125 496 100" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.35"/>
  <path d="M524 168 Q528 125 532 100" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.35"/>
  <text x="510" y="228" text-anchor="middle" font-size="8" fill="{MUTED}">Burnt offering ascends</text>
  <text x="510" y="242" text-anchor="middle" font-family="{FONT}" font-size="9" fill="{INK}">यज्ञ वेदी · לְעוֹלָם</text>
'''
    write("temple-compare-10-holika.svg", wrap("Holika Dahan and burnt offerings", body))


def svg_11_palkhi():
    body = header("11", "PROCESSION OF PRESENCE") + col_labels(
        "PALKHI / RATH YATRA", "ARK OF THE COVENANT", "पालखी", "אָרוֹן הַבְּרִית"
    ) + f'''
  <!-- Palanquin -->
  <rect x="115" y="155" width="110" height="48" rx="4" fill="#FFF" stroke="{INK}" stroke-width="1.5"/>
  <path d="M125 155 Q170 125 215 155" fill="none" stroke="{INK}" stroke-width="1.5"/>
  <line x1="130" y1="203" x2="130" y2="218" stroke="{INK}" stroke-width="3"/>
  <line x1="210" y1="203" x2="210" y2="218" stroke="{INK}" stroke-width="3"/>
  <circle cx="130" cy="222" r="6" fill="{INK}"/><circle cx="210" cy="222" r="6" fill="{INK}"/>
  <line x1="145" y1="218" x2="145" y2="200" stroke="{INK}" stroke-width="2"/>
  <line x1="195" y1="218" x2="195" y2="200" stroke="{INK}" stroke-width="2"/>
  <text x="170" y="182" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{INK}">उत्सव मूर्ति</text>
  <text x="170" y="238" text-anchor="middle" font-size="7" fill="{MUTED}">Shoulders of devotees · pradakshina</text>
  <!-- Ark -->
  <rect x="455" y="148" width="110" height="58" rx="3" fill="#FFF" stroke="{INK}" stroke-width="1.5"/>
  <circle cx="510" cy="172" r="14" fill="rgba(23,42,54,0.15)" stroke="{INK}"/>
  <line x1="468" y1="206" x2="468" y2="222" stroke="{INK}" stroke-width="4"/>
  <line x1="552" y1="206" x2="552" y2="222" stroke="{INK}" stroke-width="4"/>
  <text x="510" y="178" text-anchor="middle" font-size="8" fill="{INK}">mercy seat</text>
  <text x="510" y="238" text-anchor="middle" font-size="7" fill="{MUTED}">Levites · poles · must not touch</text>
  <text x="510" y="250" text-anchor="middle" font-family="{FONT}" font-size="8" fill="{MUTED}">Numbers 4:15</text>
'''
    write("temple-compare-11-palkhi.svg", wrap("Palkhi and Ark of the Covenant", body))


def svg_ritual_grid():
    rows = [
        ("Incense", "धूप", "Dhupa", "Ketoret"),
        ("Eternal lamp", "अखण्ड दीप", "Akhanda Deepa", "Ner Tamid"),
        ("Holy food", "नैवेद्यम्", "Naivedyam", "Showbread"),
        ("Ritual bath", "स्नान", "Snana", "Mikveh"),
        ("Sacred fire", "होलिका / हवन", "Holika / Havan", "Olah / Mizbeach"),
        ("Procession", "पालखी", "Palkhi", "Aron HaBrit"),
        ("Sacred veil", "पर्दा", "Parochet path", "Parochet"),
        ("Anointing", "अभिषेक", "Abhishekam", "Shemen Mishchah"),
        ("First fruits", "अग्र पूजा", "Agra-Puja", "Bikkurim"),
        ("Death impurity", "सूतक", "Sutak", "Tumah / Red Heifer"),
        ("Sacred thread", "यज्ञोपवीत", "Yajnopavita", "Tzitzit"),
    ]
    parts = [
        f'<text x="360" y="32" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="600" fill="{INK}">ELEVEN PARALLEL RITUAL ELEMENTS</text>',
        f'<line x1="48" y1="48" x2="672" y2="48" stroke="{INK}" stroke-width="1" opacity="0.2"/>',
        f'<text x="200" y="68" text-anchor="middle" font-size="9" font-weight="700" fill="{INK}">VEDIC / HINDU</text>',
        f'<text x="520" y="68" text-anchor="middle" font-size="9" font-weight="700" fill="{INK}">HEBREW</text>',
    ]
    y = 88
    for i, (label, dev, ind, heb) in enumerate(rows):
        fill = "#FFFFFF" if i % 2 == 0 else "rgba(23,42,54,0.04)"
        parts.append(f'<rect x="48" y="{y}" width="624" height="34" fill="{fill}" stroke="{INK}" stroke-width="0.6"/>')
        parts.append(f'<text x="72" y="{y+20}" font-family="Arial,sans-serif" font-size="8" font-weight="600" fill="{INK}">{label}</text>')
        parts.append(f'<text x="200" y="{y+14}" text-anchor="middle" font-family="{FONT}" font-size="10" fill="{INK}">{dev}</text>')
        parts.append(f'<text x="200" y="{y+26}" text-anchor="middle" font-size="7" fill="{MUTED}">{ind}</text>')
        parts.append(f'<text x="520" y="{y+20}" text-anchor="middle" font-size="8" fill="{MUTED}">{heb}</text>')
        y += 34
    parts.append(f'<text x="360" y="{y+20}" text-anchor="middle" font-size="10" fill="{MUTED}">Structural parallels — study Scripture with humility</text>')
    write("temple-ritual-parallels.svg", wrap("Ritual parallels grid", "\n  ".join(parts), 720, y + 40))


NAMES = {
    2: "temple-compare-02-purity.svg",
    3: "temple-compare-03-incense.svg",
    4: "temple-compare-04-prostration.svg",
    5: "temple-compare-05-lamp.svg",
    6: "temple-compare-06-food.svg",
    7: "temple-compare-07-thread.svg",
    8: "temple-compare-08-anointing.svg",
    9: "temple-compare-09-tithing.svg",
}


def svg_simple(num, title, left, right, dev_l, dev_r, draw_fn):
    body = header(f"{num:02d}", title) + col_labels(left, right, dev_l, dev_r) + draw_fn()
    write(NAMES[num], wrap(title, body))


# Regenerate 02-09 with Devanagari labels
def gen_all():
    svg_01_floorplan()
    svg_01_zones()

    svg_simple(2, "RITUAL IMPURITY", "SUTAK · ASAUCHAM", "TUMAH · MIKVEH", "अशौचम्", "טומאה", lambda: f'''
  <rect x="88" y="95" width="164" height="85" fill="#FFF" stroke="{INK}"/><line x1="108" y1="110" x2="232" y2="165" stroke="{INK}" stroke-width="2"/>
  <text x="170" y="200" text-anchor="middle" font-family="{FONT}" font-size="10" fill="{INK}">स्नान</text>
  <rect x="428" y="95" width="164" height="85" fill="#FFF" stroke="{INK}"/>
  <text x="510" y="200" text-anchor="middle" font-size="8" fill="{MUTED}">Red heifer · mikveh</text>''')

    svg_simple(3, "INCENSE", "DHUPA", "KETORET", "धूप", "קטורת", lambda: f'''
  <path d="M155 200 Q170 120 185 200" fill="none" stroke="{INK}" opacity="0.5"/><rect x="158" y="198" width="24" height="8" fill="{INK}"/>
  <path d="M495 200 Q510 115 525 200" fill="none" stroke="{INK}" opacity="0.5"/><rect x="498" y="198" width="24" height="8" fill="{INK}"/>''')

    svg_simple(4, "PROSTRATION", "DANDAVAT", "FACE BEFORE ARK", "दण्डवत् प्रणाम", "השתחוו", lambda: f'''
  <circle cx="118" cy="165" r="9" fill="{INK}"/><rect x="128" y="170" width="84" height="7" fill="{INK}"/>
  <circle cx="458" cy="165" r="9" fill="{INK}"/><rect x="468" y="170" width="84" height="7" fill="{INK}"/>''')

    svg_simple(5, "ETERNAL LAMP", "AKHANDA DIPA", "MENORAH", "अखण्ड दीप", "נר תמיד", lambda: f'''
  <ellipse cx="170" cy="155" rx="10" ry="18" fill="{INK}"/><rect x="162" y="175" width="16" height="25" fill="{INK}"/>
  <line x1="510" y1="195" x2="510" y2="115" stroke="{INK}" stroke-width="3"/><line x1="460" y1="155" x2="560" y2="155" stroke="{INK}" stroke-width="2"/>
  <circle cx="510" cy="110" r="6" fill="{INK}"/>''')

    svg_simple(6, "HOLY FOOD", "NAIVEDYAM", "SHOWBREAD", "नैवेद्यम्", "לחם פנים", lambda: f'''
  <ellipse cx="170" cy="170" rx="48" ry="10" fill="#FFF" stroke="{INK}"/><circle cx="155" cy="165" r="10" fill="rgba(23,42,54,0.12)"/>
  <rect x="468" y="160" width="84" height="6" fill="{INK}"/><rect x="475" y="150" width="14" height="12" fill="#FFF" stroke="{INK}"/>''')

    svg_simple(7, "SACRED THREAD", "YAJNOPAVITA", "TZITZIT · AVNET", "यज्ञोपवीत", "ציצית", lambda: f'''
  <line x1="160" y1="110" x2="180" y2="195" stroke="{INK}" stroke-width="2"/><ellipse cx="170" cy="130" rx="22" ry="28" fill="#FFF" stroke="{INK}"/>
  <rect x="468" y="150" width="84" height="50" fill="#FFF" stroke="{INK}"/><rect x="468" y="175" width="84" height="10" fill="{INK}"/>''')

    svg_simple(8, "ANOINTING", "ABHISHEKAM", "HOLY OIL", "अभिषेक", "שמן משחה", lambda: f'''
  <line x1="165" y1="95" x2="175" y2="140" stroke="{INK}" opacity="0.5"/><ellipse cx="170" cy="175" rx="20" ry="35" fill="rgba(23,42,54,0.15)"/>
  <rect x="498" y="165" width="24" height="40" fill="#FFF" stroke="{INK}"/><line x1="510" y1="125" x2="510" y2="165" stroke="{INK}" stroke-width="2"/>''')

    svg_simple(9, "FIRST FRUITS", "AGRA-PUJA", "BIKKURIM", "अग्र पूजा", "ביכורים", lambda: f'''
  <path d="M130 195 L205 195 L195 155 L140 155 Z" fill="#FFF" stroke="{INK}"/>
  <rect x="440" y="175" width="140" height="22" fill="#FFF" stroke="{INK}"/><circle cx="470" cy="168" r="10" fill="rgba(23,42,54,0.1)"/>''')

    svg_10_holika()
    svg_11_palkhi()
    svg_ritual_grid()

    # Hero composite
    write("temple-hero-eleven-parallels.svg", wrap("Eleven temple parallels", f'''
  <text x="340" y="32" text-anchor="middle" font-size="12" font-weight="600" fill="{INK}">VEDIC TEMPLE · HEBREW SANCTUARY</text>
  <text x="340" y="52" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK}">गर्भगृह  ·  קֹדֶשׁ הַקֳּדָשִׁים</text>
  <rect x="60" y="75" width="260" height="150" fill="#FFF" stroke="{INK}"/>
  <text x="190" y="120" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{INK}">होलिका · पालखी</text>
  <text x="190" y="145" text-anchor="middle" font-size="9" fill="{MUTED}">fire · procession · food · lamp</text>
  <rect x="360" y="75" width="260" height="150" fill="#FFF" stroke="{INK}"/>
  <text x="490" y="120" text-anchor="middle" font-size="11" fill="{INK}">Olah · Aron · Ketoret</text>
  <text x="490" y="145" text-anchor="middle" font-size="9" fill="{MUTED}">burnt offering · ark · incense</text>
  <text x="340" y="250" text-anchor="middle" font-size="10" fill="{MUTED}">11 structural parallels — sample artwork</text>
''', 680, 280))


if __name__ == "__main__":
    gen_all()
    print("done")
