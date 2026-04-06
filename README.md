# Tyler Azure — Personal Website

A polished, responsive personal brand site built with Flask, deployed on Railway, and media-ready for Backblaze B2.

**Stack:** Python 3 · Flask · Jinja2 · Vanilla CSS/JS · Gunicorn · Railway · Backblaze B2

---

## Project Structure

```
/
├── app.py                  # Local dev entry point
├── wsgi.py                 # Gunicorn / production entry point
├── Procfile                # Railway start command
├── .python-version         # Python version pin (Railway uses this)
├── requirements.txt
├── .env.example            # Copy this to .env for local dev
└── app/
    ├── __init__.py         # Flask app factory
    ├── config.py           # Environment variable config
    ├── routes.py           # URL routes + contact form endpoint
    ├── backblaze.py        # Asset URL helper (B2 or local fallback)
    ├── content.py          # ← EDIT THIS to update all site content
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   └── partials/       # One file per section
    └── static/
        ├── css/styles.css
        ├── js/main.js
        └── images/         # Local image fallbacks
```

---

## Local Development

### 1. Clone and set up a virtual environment

```bash
git clone <your-repo-url>
cd tyler-azure-site

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your values (see the comments in `.env.example`).

For local dev with no Backblaze configured, you can leave the B2 fields blank —
the site will fall back to local images automatically.

### 4. Run locally

```bash
python app.py
```

Visit `http://localhost:5000`

---

## Updating Content

**All site copy, project data, music highlights, and contact info live in one file:**

```
app/content.py
```

Edit that file — no template digging required. Values marked with `# TODO: update`
are placeholders waiting for your real information.

### Key sections to update first:
- `SITE` — title, email, description
- `HERO` — headline, subheadline
- `ABOUT` — bio copy, stats
- `PROJECTS` → `items` — your actual projects
- `SOCIAL_LINKS` — GitHub, LinkedIn URLs
- `CONTACT` — email address

---

## Adding / Replacing Images

### Option A: Local images (development / simple deployments)

Drop images into `app/static/images/` using whatever folder structure you prefer,
then reference them in `content.py` like this:

```python
"portrait_image": "your-photo.jpg"   # → app/static/images/your-photo.jpg
```

The `get_asset_url()` helper in `backblaze.py` will serve them via Flask's
static file handler automatically.

### Option B: Backblaze B2 (recommended for production)

1. Upload your images to your B2 bucket using the Backblaze web console or CLI.
2. Make the files/bucket public (or configure a CDN rule).
3. Set `BACKBLAZE_BUCKET_URL` in your Railway environment variables
   (e.g. `https://f005.backblazeb2.com/file/your-bucket-name`).
4. In `content.py`, set image values to the path within your bucket:

```python
"portrait_image": "about/tyler-portrait.jpg"
# → resolves to https://f005.backblazeb2.com/file/your-bucket-name/about/tyler-portrait.jpg
```

If `BACKBLAZE_BUCKET_URL` is not set, the site falls back to local images
and never crashes.

---

## Deployment on Railway

### First deploy

1. Push your code to a GitHub repository.
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub.
3. Select your repo. Railway will detect Python automatically via `.python-version`.
4. Railway will use the `Procfile` to start the app:
   ```
   gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
   ```

### Environment variables on Railway

In your Railway project → **Variables**, add:

| Variable                  | Value                                               |
|---------------------------|-----------------------------------------------------|
| `SECRET_KEY`              | A long random string (generate one below)           |
| `FLASK_ENV`               | `production`                                        |
| `PUBLIC_SITE_URL`         | `https://yourdomain.com`                            |
| `CONTACT_EMAIL`           | `tyler@yourdomain.com`                              |
| `BACKBLAZE_BUCKET_URL`    | `https://f005.backblazeb2.com/file/your-bucket`     |
| `BACKBLAZE_BUCKET_NAME`   | `your-bucket-name`                                  |
| `BACKBLAZE_KEY_ID`        | Your B2 Key ID                                      |
| `BACKBLAZE_APPLICATION_KEY` | Your B2 Application Key                           |
| `BACKBLAZE_ENDPOINT`      | `https://s3.us-west-004.backblazeb2.com`            |
| `BACKBLAZE_REGION`        | `us-west-004`                                       |

**Generate a SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Custom domain
In Railway → your service → **Settings → Networking** → add your custom domain.
Point your DNS CNAME to the Railway-provided address.

---

## Configuring Backblaze B2

### What you need from Backblaze

1. **Create a bucket** in your Backblaze account.
   - Set it to **Public** if you want direct CDN URLs.
   - Note the bucket name and region (shown on the bucket page).

2. **Get your public bucket URL.**
   - Go to your bucket → click any file → copy the URL up to `.../file/bucket-name/`
   - That prefix is your `BACKBLAZE_BUCKET_URL`.

3. **Create an Application Key** (for optional server-side upload support).
   - Backblaze console → App Keys → Add a New Application Key.
   - Restrict it to your bucket if possible.
   - Copy the **Key ID** and **Application Key** — you only see the key once.

4. **Get your S3-compatible endpoint.**
   - Format: `https://s3.<region>.backblazeb2.com`
   - Example: `https://s3.us-west-004.backblazeb2.com`
   - Your region is shown on the bucket details page.

### For v1 (display only — no uploads from the server)
You only need `BACKBLAZE_BUCKET_URL`. The app constructs public URLs from it
without needing API credentials. Set just that one variable and you're done.

---

## Contact Form

The contact form submits to `/contact` (POST) via JavaScript fetch.
In v1, submissions are logged to Railway's stdout (visible in Railway logs).

To add email sending later:
1. Install `Flask-Mail`: add `Flask-Mail` to `requirements.txt`
2. Configure SMTP env vars (`MAIL_SERVER`, `MAIL_USERNAME`, `MAIL_PASSWORD`, etc.)
3. Uncomment the Flask-Mail block in `app/routes.py`

---

## Expanding the Site Later

The architecture is designed to grow cleanly:

- Add new pages by creating routes in `routes.py` and templates in `templates/`
- Add new sections by creating partials and including them in `index.html`
- Add a database by integrating Flask-SQLAlchemy (keep it out of v1)
- Add an upload panel by building on the commented `upload_file()` in `backblaze.py`
- Add email via Flask-Mail (instructions above)

---

## Tech Stack Details

| Tool           | Version  | Purpose                              |
|----------------|----------|--------------------------------------|
| Python         | 3.12     | Language                             |
| Flask          | 3.1.0    | Web framework                        |
| Gunicorn       | 23.0.0   | Production WSGI server               |
| python-dotenv  | 1.0.1    | Local `.env` loading                 |
| Jinja2         | (Flask)  | Server-side templating               |
| Railway        | —        | Hosting + CI/CD                      |
| Backblaze B2   | —        | Media / asset storage                |

---

## License

Personal use. All rights reserved — Tyler Azure.
