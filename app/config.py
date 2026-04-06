import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask core
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = FLASK_ENV == "development"

    # Site
    PUBLIC_SITE_URL = os.environ.get("PUBLIC_SITE_URL", "http://localhost:5000")

    # Backblaze B2
    BACKBLAZE_BUCKET_NAME = os.environ.get("BACKBLAZE_BUCKET_NAME", "")
    BACKBLAZE_BUCKET_URL = os.environ.get("BACKBLAZE_BUCKET_URL", "")
    # e.g. https://f005.backblazeb2.com/file/your-bucket-name
    # Used to construct public CDN URLs without needing boto3 for reads.
    # For uploads/private access, use KEY_ID + APPLICATION_KEY via boto3.
    BACKBLAZE_KEY_ID = os.environ.get("BACKBLAZE_KEY_ID", "")
    BACKBLAZE_APPLICATION_KEY = os.environ.get("BACKBLAZE_APPLICATION_KEY", "")
    BACKBLAZE_ENDPOINT = os.environ.get(
        "BACKBLAZE_ENDPOINT", "https://s3.us-west-004.backblazeb2.com"
    )
    BACKBLAZE_REGION = os.environ.get("BACKBLAZE_REGION", "us-west-004")

    # Contact
    CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "tyler@example.com")
