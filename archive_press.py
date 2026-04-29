"""
archive_press.py — One-shot press archiver for tylertazazure.com

Does three things in a single run:
  1. Submits every press URL to the Wayback Machine (permanent external archive)
  2. Downloads a local HTML copy of each page
  3. Writes press-inventory.json — the single source of truth for the
     site's Press section, consumable directly by content.py

Run:   python archive_press.py
Time:  ~3 minutes
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path


# ─────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("press")
HTML_DIR = OUTPUT_DIR / "html"
MANIFEST_PATH = OUTPUT_DIR / "press-inventory.json"

WAYBACK_SAVE = "https://web.archive.org/save/"
USER_AGENT = "Mozilla/5.0 (press-archiver; tylertazazure.com)"
DELAY_SECONDS = 6  # stay under Wayback's rate limit


# ─────────────────────────────────────────────────────────────
# THE PRESS INVENTORY
# ─────────────────────────────────────────────────────────────
# Each entry: a record ready to drop into the site's PRESS dict.
# Empty pull_quote / image means the card will render without that element.
# ─────────────────────────────────────────────────────────────
ARTICLES = [
    {
        "id": "wjon-2020-hometown",
        "outlet": "WJON",
        "title": "Sauk Rapids Native Making His Mark in the Music Business",
        "date": "February 2020",
        "url": "https://wjon.com/sauk-rapids-native-making-his-mark-in-the-music-business/",
        "pull_quote": "making his mark in the music business",
        "type": "Profile",
        "band": "Code Red Riot",
        "featured": True,
    },
    {
        "id": "coderedriot-about",
        "outlet": "Code Red Riot",
        "title": "Band Biography",
        "date": "2018",
        "url": "https://coderedriot.com/about/",
        "pull_quote": "a fantastic guitar slinger from Minnesota",
        "type": "Band Bio",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "audiofuzz-2018-living-low",
        "outlet": "AudioFuzz",
        "title": "Badass Rock N Roll: Code Red Riot — Living Low",
        "date": "July 2018",
        "url": "https://www.audiofuzz.com/2018/07/08/badass-rock-n-roll-code-red-riot-living-low/",
        "pull_quote": "fantastic guitar slinger",
        "type": "Review",
        "band": "Code Red Riot",
        "featured": True,
    },
    {
        "id": "dangerdog-2018-mask",
        "outlet": "Dangerdog Music Reviews",
        "title": "Code Red Riot: Mask",
        "date": "June 2018",
        "url": "https://dangerdog.com/2018-music-reviews/code-red-riot-mask.php",
        "pull_quote": "a heretofore hidden six string talent from Minnesota",
        "type": "Review",
        "band": "Code Red Riot",
        "featured": True,
    },
    {
        "id": "stga-2018-mask",
        "outlet": "Surviving the Golden Age",
        "title": "Code Red Riot: Mask",
        "date": "July 2018",
        "url": "https://survivingthegoldenage.com/code-red-riot-mask/",
        "pull_quote": "heady guitar solos",
        "type": "Review",
        "band": "Code Red Riot",
        "featured": True,
    },
    {
        "id": "imd-interview",
        "outlet": "Indie Music Discovery",
        "title": "Interview with Code Red Riot — Mask",
        "date": "2018",
        "url": "https://www.indiemusicdiscovery.com/interview-code-red-riot/",
        "pull_quote": "",
        "type": "Interview",
        "band": "Code Red Riot",
        "featured": True,
    },
    {
        "id": "frr-2018-mask",
        "outlet": "Front Row Report",
        "title": "Review: Code Red Riot — Mask",
        "date": "June 2018",
        "url": "http://thefrontrowreport.com/review-code-red-riot-mask/",
        "pull_quote": "",
        "type": "Review",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "everybodywiki",
        "outlet": "EverybodyWiki",
        "title": "Code Red Riot — Encyclopedia Entry",
        "date": "2018",
        "url": "https://en.everybodywiki.com/Code_Red_Riot",
        "pull_quote": "",
        "type": "Reference",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "allmusic-mask",
        "outlet": "AllMusic",
        "title": "Code Red Riot — Mask (Album)",
        "date": "2018",
        "url": "https://www.allmusic.com/album/mask-mw0003185930",
        "pull_quote": "",
        "type": "Listing",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "bandsintown-crr",
        "outlet": "Bandsintown",
        "title": "Code Red Riot — Artist Page",
        "date": "",
        "url": "https://www.bandsintown.com/a/13686848-code-red-riot",
        "pull_quote": "",
        "type": "Listing",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "knsi-2024-riverside",
        "outlet": "KNSI Radio",
        "title": "Rock the Riverside Returns to The Clearing Thursday",
        "date": "July 2024",
        "url": "https://knsiradio.com/2024/07/11/628777/",
        "pull_quote": "",
        "type": "Local Press",
        "band": "Pandemic",
        "featured": True,
    },
    {
        "id": "pandemicfever-home",
        "outlet": "Pandemic Fever",
        "title": "Pandemic — Official Band Site",
        "date": "Current",
        "url": "https://pandemicfever.com/",
        "pull_quote": "",
        "type": "Band Site",
        "band": "Pandemic",
        "featured": False,
    },
    {
        "id": "pandemicfever-shows",
        "outlet": "Pandemic Fever",
        "title": "Pandemic — Show Dates",
        "date": "Current",
        "url": "https://pandemicfever.com/show-dates",
        "pull_quote": "",
        "type": "Shows",
        "band": "Pandemic",
        "featured": False,
    },
    {
        "id": "do512-lamadness",
        "outlet": "Do512",
        "title": "La Madness — Artist Page",
        "date": "2013",
        "url": "https://do512.com/artists/la-madness",
        "pull_quote": "",
        "type": "Listing",
        "band": "La Madness",
        "featured": False,
    },
    {
        "id": "rockstarbob-band",
        "outlet": "Rockstar Bob's Rockshow",
        "title": "The Band",
        "date": "Current",
        "url": "https://rockstarbob.com/the-band",
        "pull_quote": "",
        "type": "Band Site",
        "band": "Rockstar Bob's Rockshow",
        "featured": False,
    },
    {
        "id": "apple-music-crr",
        "outlet": "Apple Music",
        "title": "Code Red Riot — Artist Page",
        "date": "2018",
        "url": "https://music.apple.com/us/artist/code-red-riot/1198765344",
        "pull_quote": "",
        "type": "Streaming",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "amazon-mask",
        "outlet": "Amazon Music",
        "title": "Code Red Riot — Mask",
        "date": "2018",
        "url": "https://www.amazon.com/Mask-Explicit-Code-Red-Riot/dp/B07DFBBLDN",
        "pull_quote": "",
        "type": "Listing",
        "band": "Code Red Riot",
        "featured": False,
    },
    # These three are best-guess URLs constructed from citations.
    # If they 404, the script will log it; find the real URL and update here.
    {
        "id": "highwiredaze-2018-unmasked",
        "outlet": "Highwire Daze",
        "title": "Code Red Riot: Unmasked!",
        "date": "August 2018",
        "url": "https://www.highwiredaze.com/2018/08/08/code-red-riot-unmasked/",
        "pull_quote": "",
        "type": "Interview",
        "band": "Code Red Riot",
        "featured": False,
        "verify_url": True,
    },
    {
        "id": "bravewords-2018-livinglow",
        "outlet": "Bravewords",
        "title": "Code Red Riot To Release Debut Album; Living Low Video Streaming",
        "date": "June 2018",
        "url": "https://bravewords.com/news/code-red-riot-to-release-debut-album-this-month-living-low-music-video-streaming",
        "pull_quote": "",
        "type": "News",
        "band": "Code Red Riot",
        "featured": False,
        "verify_url": True,
    },
    {
        "id": "puregrainaudio-2018-premiere",
        "outlet": "PureGrainAudio",
        "title": "Las Vegas Rockers Code Red Riot Get Heavy on 'Mask' [Exclusive Premiere]",
        "date": "June 2018",
        "url": "https://puregrainaudio.com/features/las-vegas-rockers-code-red-riot-get-heavy-on-their-debut-album-mask-exclusive-premiere",
        "pull_quote": "",
        "type": "Premiere",
        "band": "Code Red Riot",
        "featured": False,
        "verify_url": True,
    },
]


# ─────────────────────────────────────────────────────────────
# WORKERS
# ─────────────────────────────────────────────────────────────

def fetch(url: str, timeout: int = 60) -> tuple[int | None, bytes | None]:
    """Fetch a URL. Returns (status_code, body_bytes) or (None, None) on error."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return None, None


def submit_to_wayback(url: str) -> str | None:
    """Submit URL to Wayback Machine. Returns the archive URL if confirmable."""
    status, _ = fetch(WAYBACK_SAVE + url, timeout=90)
    if status and 200 <= status < 400:
        # Wayback returns a redirect to the snapshot; we'll note the latest-snapshot URL
        return f"https://web.archive.org/web/*/{url}"
    return None


def save_html_copy(article: dict) -> str | None:
    """Download a local HTML copy. Returns the local path as a string."""
    status, body = fetch(article["url"])
    if not body:
        return None
    out_path = HTML_DIR / f"{article['id']}.html"
    out_path.write_bytes(body)
    return str(out_path.as_posix())


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    HTML_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    total = len(ARTICLES)

    print(f"\nArchiving {total} press articles...\n")

    for i, article in enumerate(ARTICLES, 1):
        print(f"[{i:2}/{total}] {article['outlet']}: {article['title'][:55]}")

        # 1. Wayback submission
        wayback_url = submit_to_wayback(article["url"])
        if wayback_url:
            print("           wayback: submitted")
        else:
            print("           wayback: FAILED (site may be down or URL 404)")

        # 2. Local HTML copy
        local_path = save_html_copy(article)
        if local_path:
            size_kb = Path(local_path).stat().st_size // 1024
            print(f"           local:   saved ({size_kb} KB)")
        else:
            print("           local:   FAILED")

        # 3. Consolidate result
        results.append({
            **article,
            "wayback_url": wayback_url,
            "local_html": local_path,
            "archived_at": time.strftime("%Y-%m-%d"),
        })

        # Be kind to servers
        if i < total:
            time.sleep(DELAY_SECONDS)

    # 4. Write the manifest
    MANIFEST_PATH.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # 5. Summary
    succeeded = sum(1 for r in results if r["local_html"])
    archived = sum(1 for r in results if r["wayback_url"])

    print(f"\n{'─' * 60}")
    print(f"  Local HTML saves:  {succeeded}/{total}")
    print(f"  Wayback submits:   {archived}/{total}")
    print(f"  Manifest:          {MANIFEST_PATH}")
    print(f"{'─' * 60}\n")

    failed = [r for r in results if not r["local_html"]]
    if failed:
        print("Failed fetches (verify URLs manually):")
        for r in failed:
            print(f"  - {r['outlet']}: {r['url']}")
        print()


if __name__ == "__main__":
    main()
