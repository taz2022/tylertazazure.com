# Tyler Azure — Claude Code Build Instructions

This file is the single source of truth for Claude Code when working on
`tylertazazure.com`. Read this fully before making any changes.

---

## Architecture — hub + spokes

- `/` — editorial scroll hub. Music → Tech → Museum bands.
- `/music`, `/tech`, `/museum` — discipline sub-pages, each with its own CSS file and visual language.
- `/music/<slug>` — band sub-pages. Template is parameterized. One band = one entry in `content.MUSIC.bands`.
- `/press` — standalone filtered listing. Press content does NOT appear on the homepage.

## Content source of truth

- `app/content.py` — all editorial copy and structured data, organized by discipline (`SITE`, `NAV`, `HUB`, `MUSIC`, `TECH`, `MUSEUM`, `ABOUT`, `CONTACT`, `FOOTER`).
- `press/press-inventory.json` — all press records, generated offline by `archive_press.py`. The site reads it via `app/press_loader.py`.

## Press classification

Every record in `press-inventory.json` has a `type` field. The loader buckets them:
- PRESS_TYPES → `/press` + band sub-page press sections
- BAND_REFERENCE_TYPES → band sub-page "Official" sections
- STREAMING_TYPES → band sub-page "Where to listen"

Never hardcode press in `content.py`. Always use the loader.

## CSS architecture

- `styles.css` — base + navbar only
- `page-hub.css` — homepage + press page
- `page-music.css` — /music and /music/<slug>
- `page-tech.css` — /tech
- `page-museum.css` — /museum

Each page loads only its own CSS file. No cross-contamination.

## Navbar

- Simplified: Music · Tech · Museum | LOGO | About · Press · Contact
- Nav items driven by `content.NAV`, not hardcoded
- Existing navbar-v2 styling (mix-blend-mode logo, uppercase letterspaced links) preserved

## Music bands

**Never add year ranges or timeline data to bands** — Tyler has explicitly omitted this.
Each band has: slug, name, role, status, short, url_external, card_image, featured.

---

## Stack

- **Python 3.12** + **Flask 3.1** + **Jinja2**
- **Gunicorn** for production (Railway)
- **Backblaze B2** for media (public bucket URL, no boto3 needed for v1)
- **Vanilla CSS + JS** — no React, no Vite, no Node build step
- **Railway** for hosting and CI/CD via GitHub push

---

## Project Structure

```
/
├── app.py                  # Local dev entry (python app.py)
├── wsgi.py                 # Gunicorn entry (Railway uses this)
├── Procfile                # web: gunicorn wsgi:app --bind 0.0.0.0:$PORT
├── .python-version         # 3.12
├── requirements.txt        # Flask, gunicorn, python-dotenv
├── .env.example
└── app/
    ├── __init__.py         # create_app() factory
    ├── config.py           # All config from env vars
    ├── routes.py           # URL routes + /contact POST endpoint
    ├── backblaze.py        # get_asset_url() helper
    ├── content.py          # ← ALL site copy and data lives here
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   └── partials/
    │       ├── navbar.html
    │       ├── hero.html
    │       ├── about.html
    │       ├── identity.html
    │       ├── music.html
    │       ├── projects.html
    │       ├── museum.html
    │       ├── timeline.html
    │       ├── contact.html
    │       └── footer.html
    └── static/
        ├── css/styles.css
        ├── js/main.js
        └── images/
```

---

## Known Bugs — Fix These First

### BUG 1 — CRITICAL — Site crashes on every page load

**File:** `app/templates/partials/projects.html` line 26
**File:** `app/content.py`

**Root cause:** Python dicts have a built-in `.items()` method. When Jinja2
sees `projects.items` it calls the dict method instead of getting the key,
returning a dict_items iterator that breaks the for loop.

**Fix in `app/content.py`:**
```python
# WRONG
PROJECTS = {
    ...
    "items": [ ... ]
}

# CORRECT
PROJECTS = {
    ...
    "list": [ ... ]
}
```

**Fix in `app/templates/partials/projects.html`:**
```html
<!-- WRONG -->
{% for project in projects.items %}

<!-- CORRECT -->
{% for project in projects.list %}
```

Apply this fix before anything else. Verify locally with `python app.py`
and confirm the home page loads at `http://localhost:5000`.

---

## Content To Update (app/content.py)

All content lives in `app/content.py`. Every field marked `# TODO: update`
needs real information. Work through them in this order:

### Priority 1 — Required for site to look complete

```python
SITE = {
    "contact_email": "YOUR REAL EMAIL",
    "contact_email_label": "YOUR REAL EMAIL",
}

HERO = {
    # Update headline and subheadline to feel personal and specific
    # Tyler's real voice — not generic portfolio copy
}

ABOUT = {
    # Real bio copy — confident, specific, human
    # Real stat numbers where known
    # portrait_image: set to Backblaze path once uploaded, e.g. "about/tyler.jpg"
}

SOCIAL_LINKS = [
    {"platform": "GitHub", "url": "https://github.com/taz2022"},
    {"platform": "LinkedIn", "url": "YOUR LINKEDIN URL"},
]
```

### Priority 2 — Projects list

Add real projects to `PROJECTS["list"]`. Each project follows this exact schema:

```python
{
    "title": "Project Name",
    "category": "Web Development",  # Must match a value in PROJECTS["categories"]
    "description": "One or two sentence description.",
    "stack": ["Flask", "PostgreSQL", "Railway"],
    "status": "Live",               # Live | In Progress | Archived
    "url": "https://...",           # or "" if none
    "github": "https://...",        # or "" if none
    "featured": True,               # True for top projects, False otherwise
}
```

**Important:** The category must exactly match one of the strings in
`PROJECTS["categories"]` or the filter buttons won't work.

### Priority 3 — Timeline

Update `TIMELINE["events"]` with real approximate dates/periods.
Replace placeholder period strings like "Early Years" with real ranges
like "2014 – 2016". Tyler knows his own timeline — fill these in.

### Priority 4 — Music section

Add real performance photos to Backblaze and set paths in:
```python
MUSIC = {
    "gallery_images": ["music/show1.jpg", "music/show2.jpg"],
    "highlights": [
        {"title": "...", "image": "music/highlight1.jpg"},
    ]
}
```

---

## Images — Backblaze B2 Workflow

1. Upload images to the B2 bucket via the Backblaze web console
2. Organize into folders: `about/`, `music/`, `hero/`, `projects/`
3. In `content.py`, set the image field to the path within the bucket:
   ```python
   "portrait_image": "about/tyler-portrait.jpg"
   ```
4. The `get_asset_url()` helper in `backblaze.py` constructs the full URL
   using `BACKBLAZE_BUCKET_URL` from Railway's environment variables
5. If `BACKBLAZE_BUCKET_URL` is not set, the site falls back to
   `/static/images/` automatically — it never crashes

**Environment variable in Railway:**
```
BACKBLAZE_BUCKET_URL = https://f005.backblazeb2.com/file/your-bucket-name
```

---

## Environment Variables (Railway → Variables tab)

All of these must be set in Railway for production:

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Flask session security — generate with `python -c "import secrets; print(secrets.token_hex(32))"` |
| `FLASK_ENV` | Set to `production` |
| `PUBLIC_SITE_URL` | `https://tylertazazure.com` |
| `CONTACT_EMAIL` | Where contact form submissions are logged |
| `BACKBLAZE_BUCKET_URL` | Public CDN prefix for media |
| `BACKBLAZE_BUCKET_NAME` | Bucket name |
| `BACKBLAZE_KEY_ID` | B2 App Key ID |
| `BACKBLAZE_APPLICATION_KEY` | B2 App Key secret |
| `BACKBLAZE_ENDPOINT` | `https://s3.us-west-004.backblazeb2.com` |
| `BACKBLAZE_REGION` | `us-west-004` |

---

## Deployment Workflow

Every change follows this pattern:

```bash
# 1. Make changes locally
# 2. Test locally
python app.py
# visit http://localhost:5000

# 3. Commit and push
git add .
git commit -m "describe what you changed"
git push

# 4. Railway auto-deploys in ~60 seconds
# Check Railway → Deployments for status
```

**Never push broken code.** Always test locally first with `python app.py`.

---

## CSS Design System (app/static/css/styles.css)

All CSS variables are defined at the top of `styles.css`. Use only these —
do not introduce new colors or fonts.

```css
/* Colors */
--color-bg:         #0d1117   /* Main background */
--color-bg-2:       #111827   /* Alternate section background */
--color-surface:    #1a2236   /* Card backgrounds */
--color-text:       #f0ede6   /* Primary text */
--color-text-muted: #8a96b0   /* Secondary text */
--color-blue:       #1e7ed4   /* Primary accent — matches logo */
--color-blue-light: #4da3f0   /* Hover states */
--color-gold:       #c8941a   /* Secondary accent — matches logo */
--color-gold-light: #e8b44a   /* Gold hover states */

/* Fonts */
--font-display: 'Cormorant Garamond'  /* Headlines only */
--font-body:    'Outfit'              /* All body text */
```

When adding new sections or components, follow the existing pattern:
- Section wrapper: `<section class="section [name]" id="[name]">`
- Use `scroll-reveal` class for scroll animations
- Use `container` class for max-width centering

---

## JavaScript (app/static/js/main.js)

Current features — do not duplicate these:
- Navbar scroll state (`scrolled` class added after 40px)
- Active nav link highlighting based on scroll position
- Mobile menu toggle
- `scroll-reveal` Intersection Observer
- Project category filter buttons
- Contact form fetch POST to `/contact`
- Smooth scroll for anchor links

When adding new JS features, append to `main.js` inside a self-invoking
function `(function initFeatureName() { ... })();` to avoid global scope
pollution.

---

## Flask Routes (app/routes.py)

Current routes:
- `GET /` → renders `index.html` with all section data from `content.py`
- `POST /contact` → validates form, logs submission, returns JSON
- `GET /health` → returns `{"status": "ok"}` — used by Railway health checks

When adding new pages (e.g. `/music`, `/projects`):
1. Add the route to `routes.py`
2. Create the template in `app/templates/`
3. Add the nav link to `NAV_LINKS` in `content.py`

---

## What's Left To Build

Work through these in order. Each item is self-contained.

### Phase 1 — Fix and stabilize (do first)
- [ ] Fix `projects.items` → `projects.list` bug (see BUG 1 above)
- [ ] Confirm site loads at Railway URL
- [ ] Set all required Railway environment variables

### Phase 2 — Real content
- [ ] Update `content.py` with real email, bio, social links
- [ ] Add real projects to `PROJECTS["list"]`
- [ ] Fill in real timeline dates in `TIMELINE["events"]`
- [ ] Update hero headline/subheadline to final copy

### Phase 3 — Media
- [ ] Upload portrait photo to Backblaze → set `ABOUT["portrait_image"]`
- [ ] Upload hero background image → set `HERO["background_image"]`
- [ ] Upload music photos → set `MUSIC["gallery_images"]`
- [ ] Verify all images display correctly in production

### Phase 4 — Custom domain
- [ ] In Railway → Settings → Networking → Generate Domain (if not done)
- [ ] Add Custom Domain → `tylertazazure.com`
- [ ] Copy the CNAME record Railway provides
- [ ] Add CNAME to DNS at your domain registrar
- [ ] Wait for DNS propagation (5 min to 48 hrs)
- [ ] Verify `https://tylertazazure.com` loads

### Phase 5 — Polish
- [ ] Add a favicon (`app/static/images/favicon.ico`)
  - Add to `base.html`: `<link rel="icon" href="{{ url_for('static', filename='images/favicon.ico') }}">`
- [ ] Add Open Graph meta tags to `base.html` for social sharing previews
- [ ] Wire up contact form email sending via Flask-Mail (optional)
- [ ] Add Google Analytics or Plausible (optional, privacy-respecting)
- [ ] Final responsive check on mobile

---

## Open Graph Meta Tags (for Phase 5)

Add inside `<head>` in `base.html`:

```html
<meta property="og:title" content="{{ site.title }} — {{ site.tagline }}" />
<meta property="og:description" content="{{ site.description }}" />
<meta property="og:url" content="{{ site.public_url | default('') }}" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
```

---

## Contact Form — Email Wiring (optional Phase 5)

To actually send emails from the contact form:

1. Add to `requirements.txt`:
   ```
   Flask-Mail==0.10.0
   ```

2. Add to Railway environment variables:
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=true
   MAIL_USERNAME=your@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your@gmail.com
   ```

3. Uncomment the Flask-Mail block in `app/routes.py`

---

## Notes for Claude Code

- **Always read `content.py` before editing templates** — the data
  structure drives the template rendering
- **Never hardcode content in templates** — it belongs in `content.py`
- **Test every change locally before pushing** — `python app.py`
- **Keep CSS variables consistent** — use the defined variables, no new colors
- **One commit per logical change** — makes Railway deploys easy to roll back
- **The `# TODO: update` comments in `content.py` are your checklist**

---

## Quick Commands Reference

```bash
# Run locally
python app.py

# Install dependencies
pip install -r requirements.txt

# Generate a SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"

# Push changes
git add .
git commit -m "your message"
git push

# Check Railway logs
# Railway dashboard → your service → Deployments → active deployment → logs
```
