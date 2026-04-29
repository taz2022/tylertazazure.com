"""
press_loader.py — Loads press-inventory.json and exposes filtered views.

The inventory is generated offline by archive_press.py / archive_press_patch.py.
This module is the ONLY place the site reads that file.
"""
import json
from pathlib import Path
from typing import Any

PRESS_TYPES = {
    "Profile", "Review", "Interview", "Feature",
    "Show Review", "Release Coverage", "Video Premiere",
    "Premiere", "News", "Local Press", "Clipping",
}
BAND_REFERENCE_TYPES = {"Band Bio", "Band Site", "Shows", "Reference"}
STREAMING_TYPES = {"Streaming", "Listing"}

_INVENTORY_PATH = Path("press/press-inventory.json")
_cache: list[dict[str, Any]] | None = None


def _load() -> list[dict[str, Any]]:
    global _cache
    if _cache is not None:
        return _cache
    if not _INVENTORY_PATH.exists():
        _cache = []
        return _cache
    try:
        _cache = json.loads(_INVENTORY_PATH.read_text(encoding="utf-8"))
    except Exception:
        _cache = []
    return _cache


def reload() -> None:
    global _cache
    _cache = None
    _load()


def get_press(featured_only: bool = False) -> list[dict[str, Any]]:
    """Public press records — reviews, interviews, profiles. NOT band pages."""
    items = [
        r for r in _load()
        if r.get("type") in PRESS_TYPES
        and r.get("status") != "dead"
    ]
    if featured_only:
        items = [r for r in items if r.get("featured")]
    return items


def get_dead_press() -> list[dict[str, Any]]:
    """Citation-only records — URL is dead."""
    return [r for r in _load() if r.get("status") == "dead" and r.get("type") in PRESS_TYPES]


def get_band_references(band: str) -> list[dict[str, Any]]:
    """Band-page references — official sites, bios, wikis."""
    return [
        r for r in _load()
        if r.get("type") in BAND_REFERENCE_TYPES
        and r.get("band") == band
    ]


def get_streaming_links(band: str) -> list[dict[str, Any]]:
    """Streaming/purchase links for a specific band."""
    return [
        r for r in _load()
        if r.get("type") in STREAMING_TYPES
        and r.get("band") == band
    ]


def get_press_for_band(band: str) -> list[dict[str, Any]]:
    """Public press specifically about a single band."""
    return [
        r for r in _load()
        if r.get("type") in PRESS_TYPES
        and r.get("band") == band
        and r.get("status") != "dead"
    ]
