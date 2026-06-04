#!/usr/bin/env python3
import json, time, urllib.request, urllib.parse
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "blog-assets" / "temple-parallel-photos"
UA = "2-22church-blog/1.0"

# slug -> list of commons filenames to try
EXTRA = {
    "02-ganges-ritual-bath": ["Ganga_Aarti_at_Dashaswamedh_Ghat,_Varanasi.jpg", "Ganges_in_Varanasi.jpg"],
    "02-mikveh-qumran": ["Mikveh_at_Masada.jpg", "Mikveh_in_the_City_of_David.jpg"],
    "03-temple-incense-india": ["Incense_in_a_Hindu_temple,_India.jpg", "Incense_sticks_India.jpg"],
    "04-sashtanga-pranam": ["Devotees_doing_Sashtanga_Dandavat_Pranam.jpg", "Hindu_pilgrims_at_Vaishno_Devi.jpg"],
    "04-jewish-prayer-western-wall": ["Westernwall_jerusalem.jpg", "The_Western_Wall.jpg"],
    "05-menorah-tabernacle": ["Menorah,_Israel_Museum,_Jerusalem.jpg", "Golden_menorah_in_front_of_the_Knesset,_Jerusalem.jpg"],
    "07-upanayana-thread-ceremony": ["Upanayana.jpg", "Sacred_Thread_Ceremony.jpg"],
    "08-abhishekam-shiva": ["Abhishekam_performed_on_Shiva_Lingam.jpg", "Abhishekam.jpg"],
    "09-india-harvest-festival": ["Pongal_festival.jpg", "Onam_feast.jpg"],
    "11-ark-carrying-illustration": ["The_Ark_of_the_Covenant_(James_Tissot).jpg", "Joshua_crossing_the_Jordan_with_the_Ark.jpg"],
    "hero-meenakshi-gopuram": ["Madurai_Meenakshi_Amman_Temple_Gopuram.jpg", "Meenakshi_Temple,_Madurai.jpg"],
    "hero-rath-yatra": ["Jagannath_Temple,_Puri,_Rath_Yatra.jpg", "Rath_Yatra_in_Puri.jpg"],
}


def resolve(filename):
    q = urllib.parse.quote(filename.replace(" ", "_"))
    api = f"https://commons.wikimedia.org/w/api.php?action=query&titles=File:{q}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
    for p in data["query"]["pages"].values():
        if "imageinfo" in p:
            return p["imageinfo"][0].get("thumburl") or p["imageinfo"][0]["url"]
    return None


def save(slug, url):
    dest = OUT / f"{slug}.jpg"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        b = r.read()
    if len(b) > 8000 and not b[:20].strip().startswith(b"<"):
        dest.write_bytes(b)
        print(f"OK {slug} {len(b)}")
        return True
    print(f"bad data {slug}")
    return False


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, names in EXTRA.items():
        if (OUT / f"{slug}.jpg").exists():
            print(f"skip {slug}")
            continue
        for name in names:
            time.sleep(3)
            try:
                url = resolve(name)
                if url and save(slug, url):
                    break
            except Exception as e:
                print(slug, name, e)


if __name__ == "__main__":
    main()
