#!/usr/bin/env python3
"""Download Wikimedia Commons photos for temple-parallels blog (CC-licensed)."""
import json
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "blog-assets" / "temple-parallel-photos"
UA = "2-22church-blog/1.0 (educational; contact: 2-22church.com)"

# (local_slug, commons_filename, max_width_thumb or 0 for full)
FILES = [
    # 01 Architecture
    ("01-garbhagriha-interior", "Inside_the_Garbhagriha_of_Shri_Ananthashayana_Temple.jpg", 1280),
    ("01-temple-mandapa-khajuraho", "01022_Lakshmana_temple,_Khajuraho_Madhya_Pradesh_007.jpg", 1280),
    ("01-tabernacle-timna-court", "Tabernacle_timna.jpg", 1280),
    ("01-ark-timna-replica", "Timna_Tabernacle_inside_Ark_of_the_Covenant.jpg", 1280),
    # 02 Purity
    ("02-ganges-ritual-bath", "Bathing_in_the_Ganges_During_Kumbh_Mela.jpg", 1280),
    ("02-mikveh-qumran", "Ancient_mikveh_in_Qumran.jpg", 1280),
    # 03 Incense
    ("03-temple-incense-india", "Incense_offering_at_a_Hindu_temple.jpg", 1280),
    ("03-altar-of-incense-model", "Altar_of_incense_Timna_tabernacle.jpg", 1280),
    # 04 Prostration
    ("04-sashtanga-pranam", "Prostration_in_Hindu_temple.jpg", 1280),
    ("04-jewish-prayer-western-wall", "Jews_praying_at_Western_Wall.jpg", 1280),
    # 05 Lamp
    ("05-akhanda-deepam-lamps", "Oil_lamps_at_Hindu_temple.jpg", 1280),
    ("05-menorah-tabernacle", "Menorah_in_Timna_tabernacle.jpg", 1280),
    # 06 Food
    ("06-naivedyam-offering", "Food_offering_in_Hindu_temple.jpg", 1280),
    ("06-showbread-tabernacle", "Table_of_showbread_Timna.jpg", 1280),
    # 07 Thread
    ("07-upanayana-thread-ceremony", "Upanayana_ceremony.jpg", 1280),
    ("07-tzitzit-tallit", "Tzitzit_closeup.jpg", 1280),
    # 08 Anointing
    ("08-abhishekam-shiva", "Abhisheka_of_Shiva_Lingam.jpg", 1280),
    ("08-anointing-oil-bible", "The_Phillip_Medhurst_Picture_Torah_472._Building_the_ark_of_the_covenant._Exodus_cap_37._Mortier.jpg", 960),
    # 09 First fruits
    ("09-india-harvest-festival", "Pongal_festival_offerings.jpg", 1280),
    ("09-bikkurim-first-fruits", "Bikkurim.jpg", 1280),
    # 10 Holika / fire
    ("10-holi-bonfire", "Holi_bonfire.jpg", 1280),
    ("10-bronze-altar-timna", "Tabernacle_brazen_altar_Timna.jpg", 1280),
    # 11 Palkhi / Ark
    ("11-dnyaneshwar-palkhi", "Dnyaneshwar_Maharaj_Palkhi_(Dindi_or_Wari).jpg", 1280),
    ("11-ark-carrying-illustration", "The_Ark_of_the_Covenant_carried.jpg", 1280),
    # Hero extras
    ("hero-meenakshi-gopuram", "Meenakshi_Amman_Temple_gopuram.jpg", 1600),
    ("hero-rath-yatra", "Rath_Yatra_Puri.jpg", 1280),
]

FALLBACK = {
    "03-temple-incense-india": "Incense_sticks_in_India.jpg",
    "03-altar-of-incense-model": "Tabernacle_timna.jpg",
    "04-sashtanga-pranam": "Hindu_devotees_at_temple.jpg",
    "04-jewish-prayer-western-wall": "Western_Wall_Jerusalem.JPG",
    "05-akhanda-deepam-lamps": "Deepam.jpg",
    "05-menorah-tabernacle": "Golden_menorah_Jerusalem.jpg",
    "06-naivedyam-offering": "Prasadam.jpg",
    "06-showbread-tabernacle": "Tabernacle_timna.jpg",
    "07-upanayana-thread-ceremony": "Yajnopavita.jpg",
    "07-tzitzit-tallit": "Tallit.jpg",
    "08-abhishekam-shiva": "Abhishekam.jpg",
    "08-anointing-oil-bible": "Anointing.jpg",
    "09-india-harvest-festival": "Onam_festival_pookkalam_and_feast.jpg",
    "09-bikkurim-first-fruits": "First_fruits.jpg",
    "10-bronze-altar-timna": "Tabernacle_timna.jpg",
    "11-ark-carrying-illustration": "Joshua_passing_the_River_Jordan_with_the_Ark_of_the_Covenant.jpg",
    "hero-meenakshi-gopuram": "Sri_Meenakshi_Temple.jpg",
    "hero-rath-yatra": "Jagannath_Temple_Rath_Yatra.jpg",
}


def resolve_url(filename: str) -> str | None:
    import urllib.parse
    q = urllib.parse.quote(filename.replace(" ", "_"))
    api = f"https://commons.wikimedia.org/w/api.php?action=query&titles=File:{q}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for p in pages.values():
            if "imageinfo" in p:
                ii = p["imageinfo"][0]
                return ii.get("thumburl") or ii.get("url")
    except Exception as e:
        print("  api fail", filename, e)
    # redirect fallback
    path_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(filename)}"
    req2 = urllib.request.Request(path_url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req2, timeout=30) as r:
            final = r.geturl()
            if "upload.wikimedia.org" in final and not final.endswith(".php"):
                return final
    except Exception as e:
        print("  redirect fail", filename, e)
    return None


def download(slug: str, filename: str, width: int) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    url = resolve_url(filename)
    tried = [filename]
    if not url and slug in FALLBACK:
        fb = FALLBACK[slug]
        tried.append(fb)
        url = resolve_url(fb)
    if not url:
        return {"slug": slug, "ok": False, "tried": tried}

    ext = ".jpg"
    if url.lower().endswith(".png"):
        ext = ".png"
    dest = OUT / f"{slug}{ext}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if len(data) < 5000 or data[:15].startswith(b"<!DOCTYPE") or data[:5] == b"<?xml":
        return {"slug": slug, "ok": False, "tried": tried, "reason": "not image"}
    dest.write_bytes(data)
    return {"slug": slug, "ok": True, "file": dest.name, "bytes": len(data), "source": url, "commons": tried[-1]}


def main():
    manifest = []
    for slug, name, w in FILES:
        print("fetch", slug, "...", end=" ")
        m = download(slug, name, w)
        manifest.append(m)
        print("OK" if m.get("ok") else "FAIL")
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    ok = sum(1 for m in manifest if m.get("ok"))
    print(f"\n{ok}/{len(manifest)} images saved to {OUT}")


if __name__ == "__main__":
    main()
