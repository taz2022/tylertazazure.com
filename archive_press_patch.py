"""
archive_press_patch.py — Delta archiver for URL fixes and new articles.

Run this AFTER archive_press.py has finished. It will:
  1. Fix broken URLs (Highwire Daze had wrong slug pattern)
  2. Mark dead URLs (PureGrainAudio was absorbed into V13.net)
  3. Add newly discovered articles (Vents, New Noise, Scary Monsters, Metal Temple, Highwire Daze Las Rageous)

The script is idempotent — running it twice is safe. It reads the existing
press/press-inventory.json, applies deltas, and writes the merged result back.

Run:   python archive_press_patch.py
Time:  ~1 minute
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path


# ─────────────────────────────────────────────────────────────
# CONFIG (mirrors archive_press.py)
# ─────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("press")
HTML_DIR = OUTPUT_DIR / "html"
MANIFEST_PATH = OUTPUT_DIR / "press-inventory.json"

WAYBACK_SAVE = "https://web.archive.org/save/"
USER_AGENT = "Mozilla/5.0 (press-archiver; tylertazazure.com)"
DELAY_SECONDS = 6


# ─────────────────────────────────────────────────────────────
# 1. URL FIXES — update existing records with correct URLs + re-archive
# ─────────────────────────────────────────────────────────────
URL_FIXES = [
    {
        "id": "highwiredaze-2018-unmasked",
        "new_url": "https://highwiredaze.com/2018/08/08/coderedriotunmasked/",
        # The original slug used dashes (code-red-riot-unmasked) but the
        # real URL concatenates the band name (coderedriotunmasked)
    },
]


# ─────────────────────────────────────────────────────────────
# 2. DEAD URLS — mark as dead in manifest, do not re-archive
# ─────────────────────────────────────────────────────────────
DEAD_URLS = [
    {
        "id": "puregrainaudio-2018-premiere",
        "note": (
            "PureGrainAudio was absorbed into V13.net in the company's rebrand. "
            "The original article URL is dead. Check archive.org manually for a "
            "preserved snapshot; otherwise cite as 'PureGrainAudio, June 2018 (archived)'."
        ),
    },
]


# ─────────────────────────────────────────────────────────────
# 3. NEW ARTICLES — append to manifest if not already present
# ─────────────────────────────────────────────────────────────
NEW_ARTICLES = [
    {
        "id": "highwiredaze-2017-lasrageous",
        "outlet": "Highwire Daze",
        "title": "Meet The Local Bands of Las Rageous — Code Red Riot, A Friend A Foe, NATIONS, and We Gave It Hell",
        "date": "April 2017",
        "url": "https://highwiredaze.com/2017/04/17/lasrageous1/",
        "pull_quote": "",
        "type": "Feature",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "vents-2018-mask-release",
        "outlet": "Vents Magazine",
        "title": "Code Red Riot Releases Debut Album Mask",
        "date": "June 2018",
        "url": "https://ventsmagazine.com/2018/06/29/code-red-riot-releases-debut-album-mask/",
        "pull_quote": "heavy, really heavy",
        "type": "Release Coverage",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "newnoise-2018-slide",
        "outlet": "New Noise Magazine",
        "title": "Music Video Premiere: Code Red Riot — Slide",
        "date": "September 2018",
        "url": "https://newnoisemagazine.com/music-video-premiere-code-red-riot-slide/",
        "pull_quote": "",
        "type": "Video Premiere",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "scarymonsters-2019-komp",
        "outlet": "Scary Monsters Music",
        "title": "KOMP 92.3 Vegas Homegrown Series with Code Red Riot, The Dirty Hooks and More!",
        "date": "January 2019",
        "url": "https://www.scarymonstersmusic.com/single-post/2019/01/18/KOMP-923-Vegas-Homegrown-Series-with-Code-ReD-Riot-The-Dirty-Hooks-and-More",
        "pull_quote": "",
        "type": "Show Review",
        "band": "Code Red Riot",
        "featured": False,
    },
    {
        "id": "metaltemple-2018-mask",
        "outlet": "Metal Temple",
        "title": "Code Red Riot — Mask",
        "date": "August 2018",
        "url": "https://metal-temple.com/review/code-red-riot-mask/",
        "pull_quote": "deserves our attention",
        "type": "Review",
        "band": "Code Red Riot",
        "featured": False,
    },
]


# ─────────────────────────────────────────────────────────────
# WORKERS
# ─────────────────────────────────────────────────────────────

def fetch(url: str, timeout: int = 60):
    """Returns (status_code, body_bytes) or (None, None) on error."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return None, None


def submit_to_wayback(url: str):
    status, _ = fetch(WAYBACK_SAVE + url, timeout=90)
    if status and 200 <= status < 400:
        return f"https://web.archive.org/web/*/{url}"
    return None


def save_html_copy(article: dict):
    status, body = fetch(article["url"])
    if not body:
        return None
    out_path = HTML_DIR / f"{article['id']}.html"
    out_path.write_bytes(body)
    return str(out_path.as_posix())


def load_manifest():
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    print(f"WARNING: {MANIFEST_PATH} doesn't exist. Run archive_press.py first.")
    return []


def save_manifest(records):
    MANIFEST_PATH.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def find_record(records, article_id):
    return next((r for r in records if r.get("id") == article_id), None)


def archive_and_record(article: dict, records: list, label: str):
    """Wayback + local HTML + upsert into records."""
    print(f"  {label}: {article['outlet']}: {article['title'][:55]}")

    wayback = submit_to_wayback(article["url"])
    print(f"         wayback: {'submitted' if wayback else 'FAILED'}")

    local = save_html_copy(article)
    if local:
        size_kb = Path(local).stat().st_size // 1024
        print(f"         local:   saved ({size_kb} KB)")
    else:
        print(f"         local:   FAILED")

    record = {
        **article,
        "wayback_url": wayback,
        "local_html": local,
        "archived_at": time.strftime("%Y-%m-%d"),
    }

    existing = find_record(records, article["id"])
    if existing:
        existing.update(record)
    else:
        records.append(record)


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    records = load_manifest()

    print(f"\nLoaded {len(records)} existing records from manifest.")
    print(f"Applying patch: {len(URL_FIXES)} fix(es), {len(DEAD_URLS)} dead URL(s), {len(NEW_ARTICLES)} new article(s).\n")

    # 1. Apply URL fixes
    if URL_FIXES:
        print("─── Fixing broken URLs ──────────────────────────────")
        for fix in URL_FIXES:
            existing = find_record(records, fix["id"])
            if not existing:
                print(f"  skip: {fix['id']} (not in manifest)")
                continue
            old_url = existing.get("url", "")
            print(f"  fix:  {fix['id']}")
            print(f"        old: {old_url}")
            print(f"        new: {fix['new_url']}")
            existing["url"] = fix["new_url"]
            archive_and_record(existing, records, "re-archive")
            time.sleep(DELAY_SECONDS)

    # 2. Mark dead URLs
    if DEAD_URLS:
        print("\n─── Marking dead URLs ───────────────────────────────")
        for dead in DEAD_URLS:
            existing = find_record(records, dead["id"])
            if not existing:
                print(f"  skip: {dead['id']} (not in manifest)")
                continue
            existing["status"] = "dead"
            existing["note"] = dead["note"]
            print(f"  dead: {dead['id']}")
            print(f"        note: {dead['note'][:60]}...")

    # 3. Add new articles
    if NEW_ARTICLES:
        print("\n─── Adding new articles ─────────────────────────────")
        for article in NEW_ARTICLES:
            if find_record(records, article["id"]):
                print(f"  skip: {article['id']} (already in manifest)")
                continue
            archive_and_record(article, records, "add")
            time.sleep(DELAY_SECONDS)

    # 4. Save manifest
    save_manifest(records)

    # 5. Summary
    featured = sum(1 for r in records if r.get("featured"))
    dead = sum(1 for r in records if r.get("status") == "dead")

    print(f"\n{'─' * 60}")
    print(f"  Total records:     {len(records)}")
    print(f"  Featured on site:  {featured}")
    print(f"  Dead URLs:         {dead}")
    print(f"  Manifest written:  {MANIFEST_PATH}")
    print(f"{'─' * 60}\n")


if __name__ == "__main__":
    main()
