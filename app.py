"""
app.py — Local development entry point.

Run with:
    python app.py

For production (Railway), Gunicorn uses wsgi.py via the Procfile.
"""
from app import create_app
from app.config import Config
import os


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
