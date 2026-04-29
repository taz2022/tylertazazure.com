from flask import Blueprint, render_template, abort, request, jsonify, current_app
from . import content as c
from . import press_loader

main = Blueprint("main", __name__)


@main.context_processor
def inject_globals():
    return {
        "site": c.SITE,
        "nav": c.NAV,
        "footer": c.FOOTER,
    }


@main.route("/")
def home():
    return render_template(
        "index.html",
        hub=c.HUB,
        music=c.MUSIC,
        about=c.ABOUT,
        contact=c.CONTACT,
    )


@main.route("/music")
def music():
    return render_template(
        "music.html",
        music=c.MUSIC,
    )


@main.route("/music/<slug>")
def music_band(slug):
    band = next((b for b in c.MUSIC["bands"] if b["slug"] == slug), None)
    if band is None:
        abort(404)
    return render_template(
        "music_band.html",
        band=band,
    )


@main.route("/shows")
def shows():
    return render_template(
        "shows.html",
        shows=c.SHOWS,
    )


@main.route("/press")
def press():
    return render_template(
        "press.html",
        press_items=press_loader.get_press(),
        dead_items=press_loader.get_dead_press(),
    )


@main.route("/contact", methods=["POST"])
def contact_submit():
    data = request.get_json(silent=True) or request.form

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    subject = (data.get("subject") or "Website inquiry").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "Please fill in all required fields."}), 400

    current_app.logger.info(
        f"[Contact Form] From: {name} <{email}> | Subject: {subject}"
    )

    return jsonify({"success": True, "message": "Thanks \u2014 I'll be in touch soon."})


@main.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@main.app_errorhandler(404)
def not_found(e):
    return render_template("404.html", site=c.SITE, nav=c.NAV, footer=c.FOOTER), 404
