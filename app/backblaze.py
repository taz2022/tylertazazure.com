"""
backblaze.py — Lightweight helper for resolving media asset URLs.

Strategy:
  - If BACKBLAZE_BUCKET_URL is set in the environment, assets are served from
    Backblaze B2 public URLs.
  - If it is not set (local dev or misconfigured), assets fall back to the
    local /static/images/ path so the site never breaks.

Upload workflow (manual, no dashboard needed for v1):
  1. Upload files to your Backblaze B2 bucket via the B2 web console or CLI.
  2. Make the bucket/files public (or use a signed URL if private).
  3. Set BACKBLAZE_BUCKET_URL in your Railway environment variables.
  4. Reference assets in content.py using just their filename or relative path
     within the bucket, e.g. "hero/background.jpg".

For private bucket uploads via boto3, see the commented section below.
"""

import os
from flask import current_app, url_for


def get_asset_url(path: str) -> str:
    """
    Return a fully-qualified URL for a media asset.

    Args:
        path: Relative path to the asset, e.g. "hero/background.jpg"
              or "music/performance.jpg". This should match the path
              within your B2 bucket AND within /static/images/ locally.

    Returns:
        A public URL string (Backblaze CDN or local static fallback).
    """
    bucket_url = current_app.config.get("BACKBLAZE_BUCKET_URL", "").rstrip("/")

    if bucket_url:
        return f"{bucket_url}/{path.lstrip('/')}"

    # Local fallback — expects file at app/static/images/<path>
    return url_for("static", filename=f"images/{path}")


def b2_is_configured() -> bool:
    """Return True if Backblaze B2 credentials are present."""
    return bool(
        current_app.config.get("BACKBLAZE_KEY_ID")
        and current_app.config.get("BACKBLAZE_APPLICATION_KEY")
        and current_app.config.get("BACKBLAZE_BUCKET_NAME")
    )


# ---------------------------------------------------------------------------
# Optional: boto3 upload helper (not needed for v1 display-only usage)
# ---------------------------------------------------------------------------
# Uncomment and install boto3 if you want server-side upload capability.
#
# import boto3
# from botocore.client import Config as BotocoreConfig
#
# def get_b2_client():
#     return boto3.client(
#         "s3",
#         endpoint_url=current_app.config["BACKBLAZE_ENDPOINT"],
#         aws_access_key_id=current_app.config["BACKBLAZE_KEY_ID"],
#         aws_secret_access_key=current_app.config["BACKBLAZE_APPLICATION_KEY"],
#         config=BotocoreConfig(signature_version="s3v4"),
#         region_name=current_app.config["BACKBLAZE_REGION"],
#     )
#
# def upload_file(local_path, b2_key):
#     client = get_b2_client()
#     bucket = current_app.config["BACKBLAZE_BUCKET_NAME"]
#     client.upload_file(local_path, bucket, b2_key)
#     return get_asset_url(b2_key)
