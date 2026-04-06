from flask import Blueprint, render_template, request, jsonify, current_app
from . import content as c

main = Blueprint("main", __name__)


@main.context_processor
def inject_globals():
    """Inject site-wide content into every template context."""
    return {
        "site": c.SITE,
        "nav_links": c.NAV_LINKS,
        "social_links": c.SOCIAL_LINKS,
        "footer": c.FOOTER,
    }


@main.route("/")
def index():
    return render_template(
        "index.html",
        hero=c.HERO,
        about=c.ABOUT,
        identity=c.IDENTITY,
        music=c.MUSIC,
        projects=c.PROJECTS,
        museum=c.MUSEUM,
        timeline=c.TIMELINE,
        contact=c.CONTACT,
    )


@main.route("/contact", methods=["POST"])
def contact():
    """
    Simple contact form endpoint.

    For v1 this logs the submission and returns a JSON response.
    To wire up email sending, install Flask-Mail and configure MAIL_* env vars.
    See README for instructions.
    """
    data = request.get_json(silent=True) or request.form

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    subject = (data.get("subject") or "Website inquiry").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "Please fill in all required fields."}), 400

    # Log submission (Railway captures stdout in logs)
    current_app.logger.info(
        f"[Contact Form] From: {name} <{email}> | Subject: {subject}"
    )

    # ---------------------------------------------------------------------------
    # Optional: Flask-Mail integration (uncomment when ready)
    # ---------------------------------------------------------------------------
    # from flask_mail import Mail, Message
    # mail = Mail(current_app)
    # msg = Message(
    #     subject=f"[Tyler Azure Website] {subject}",
    #     sender=current_app.config["MAIL_DEFAULT_SENDER"],
    #     recipients=[current_app.config["CONTACT_EMAIL"]],
    #     reply_to=email,
    #     body=f"From: {name} <{email}>\n\n{message}",
    # )
    # mail.send(msg)
    # ---------------------------------------------------------------------------

    return jsonify({"success": True, "message": "Thanks — I'll be in touch soon."})


@main.route("/health")
def health():
    """Health check endpoint for Railway."""
    return jsonify({"status": "ok"}), 200
