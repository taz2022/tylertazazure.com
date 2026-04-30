from flask import Flask
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .backblaze import get_asset_url
    app.jinja_env.globals["asset_url"] = get_asset_url

    from . import press_loader
    app.jinja_env.globals["get_press"] = press_loader.get_press
    app.jinja_env.globals["get_press_for_band"] = press_loader.get_press_for_band
    app.jinja_env.globals["get_band_references"] = press_loader.get_band_references
    app.jinja_env.globals["get_streaming_links"] = press_loader.get_streaming_links

    from datetime import date
    app.jinja_env.globals["current_year"] = date.today().year

    from .routes import main
    app.register_blueprint(main)

    return app
