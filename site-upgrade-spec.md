# Site Upgrade Spec — Bands, Press, Azure Archives Case Study

**Scope:** Rebuild the Music section around bands (no timeline), add a new Press section, and expand Azure Archives from a single project card into a full case study with its own subpage.

**Target repo:** `tylertazazure.com` (Flask app factory, Jinja2, Railway deploy, Backblaze media)

**Conventions to follow (from existing `CLAUDE.md`):**
- All content lives in `app/content.py` — never hardcode copy in templates
- Never use `items` as a dict key in Jinja2 (Python dict method collision — known bug)
- CSS variables only; no new colors/fonts outside the existing design system
- Test locally with `python app.py` before every push
- Commit in small, focused increments

---

## Prerequisites — confirm before starting

1. `app/content.py` currently uses `PROJECTS["list"]` (not `items`) — verify this is still the case
2. Check that `app/backblaze.py` exposes `get_asset_url(path)` and has a local `/static/images/` fallback
3. Confirm `music.html`, `projects.html`, and `base.html` partials exist in `app/templates/partials/`
4. Verify the navbar is built from a list in `content.py` — any new section added to nav must be registered there

---

## Task 1 — Rebuild Music Section (bands-first, no timeline)

### 1.1 Replace `MUSIC["highlights"]` with `MUSIC["bands"]` in `app/content.py`

Remove the existing `highlights` list. Replace with the structure below. **Do not include years or date ranges on any band** — Tyler has explicitly omitted the timeline.

```python
MUSIC = {
    "headline": "Music",
    "subheadline": "Guitar. Performance. Live rock.",
    "intro": (
        "I started playing guitar at 13 after my dad took me to a Prince concert. "
        "Watching that Purple Rain solo live hooked me for good. Since then I've "
        "played lead guitar across rock, alt-rock, tribute, and live event work — "
        "from Minneapolis rooms to the Las Vegas strip, and every small-town stage in between."
    ),
    "bands": [
        {
            "name": "Code Red Riot",
            "role": "Lead Guitar",
            "description": (
                "Hard rock band based in Las Vegas, signed to Sony RED Music. "
                "Debut album Mask (2018) co-produced by Shawn McGhee "
                "(Disturbed, Five Finger Death Punch, Papa Roach). "
                "Single Bulletproof charted on Billboard Mainstream Rock."
            ),
            "url": "",  # TODO: Tyler to add
            "image": "music/bands/code-red-riot.jpg",  # TODO: upload
            "featured": True,
        },
        {
            "name": "Pandemic",
            "role": "Lead Guitar",
            "description": (
                "Central Minnesota hard rock band active on the regional festival "
                "circuit, including Rock the Riverside at The Clearing in Sauk Rapids."
            ),
            "url": "",  # TODO
            "image": "music/bands/pandemic.jpg",  # TODO
            "featured": True,
        },
        {
            "name": "Hairball",
            "role": "Fill-in Guitar",
            "description": (
                "National-touring rock tribute powerhouse from Minnesota paying homage "
                "to Van Halen, KISS, Mötley Crüe, Queen, Journey, and Aerosmith."
            ),
            "url": "",  # TODO
            "image": "music/bands/hairball.jpg",  # TODO
            "featured": False,
        },
        {
            "name": "Rockstar Bob's Rockshow",
            "role": "Guitar / Vocals",
            "description": "Regional rock act selling out venues across the Midwest.",
            "url": "",  # TODO
            "image": "music/bands/rockshow.jpg",  # TODO
            "featured": False,
        },
        {
            "name": "Raised on Radio",
            "role": "Guest Guitar",
            "description": (
                "Classic rock variety group pulling musicians from Diamondback, "
                "Outside Recess, Pandemic, and Chaser."
            ),
            "url": "",  # TODO
            "image": "music/bands/raised-on-radio.jpg",  # TODO
            "featured": False,
        },
        {
            "name": "La Madness",
            "role": "Lead Guitar, Backing Vocals",
            "description": (
                "Minneapolis-based indie grind blues band. Debut album Chances Are. "
                "Opened for Papa Roach, Fuel, and Tantric; played Whisky A Go Go, "
                "House of Blues San Diego, and First Avenue."
            ),
            "url": "",  # TODO
            "image": "music/bands/la-madness.jpg",  # TODO
            "featured": False,
        },
    ],
    "stages_shared": [
        "Breaking Benjamin",
        "Eagles of Death Metal",
        "Steel Panther",
        "Fozzy",
        "Papa Roach",
        "Fuel",
        "Tantric",
        "Gemini Syndrome",
        "Las Rageous Festival",
        "Whisky A Go Go",
        "House of Blues",
        "First Avenue",
    ],
    "gallery_images": [
        "music/gallery/hairflip-ramones.jpg",
        "music/gallery/goldtop-horns-fire.jpg",
        "music/gallery/stage-teal-lespaul.jpg",
        "music/gallery/brainerd-sunflare.jpg",
        "music/gallery/duo-purple-stage.jpg",
        "music/gallery/gibson-lespaul-bw.jpg",
        "music/gallery/sunburst-daytime.jpg",
        "music/gallery/acoustic-duo-summerfest.jpg",
        "music/gallery/acoustic-hoodie-bw.jpg",
    ],
}
```

### 1.2 Rewrite `app/templates/partials/music.html`

Replace the existing highlights loop with a bands loop. Add the stages-shared marquee and keep the gallery block.

```html
<section class="section music" id="music" aria-labelledby="music-heading">
  <div class="container">
    <div class="section-header scroll-reveal">
      <div class="section-label">Music</div>
      <h2 class="section-heading" id="music-heading">{{ music.headline }}</h2>
      <p class="section-sub">{{ music.subheadline }}</p>
    </div>

    <p class="music__intro scroll-reveal">{{ music.intro }}</p>

    {# ------- Bands grid ------- #}
    <div class="music__bands scroll-reveal" aria-label="Bands">
      {% for band in music.bands %}
      <article class="band-card {% if band.featured %}band-card--featured{% endif %}">
        {% if band.image %}
        <div class="band-card__image">
          <img src="{{ asset_url(band.image) }}" alt="{{ band.name }}" loading="lazy" />
        </div>
        {% else %}
        <div class="band-card__image band-card__image--placeholder" aria-hidden="true">
          <span class="band-card__icon">♪</span>
        </div>
        {% endif %}
        <div class="band-card__body">
          <h3 class="band-card__name">{{ band.name }}</h3>
          <p class="band-card__role">{{ band.role }}</p>
          <p class="band-card__desc">{{ band.description }}</p>
          {% if band.url %}
          <a class="band-card__link" href="{{ band.url }}" target="_blank" rel="noopener">
            Visit {{ band.name }} →
          </a>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>

    {# ------- Stages shared marquee ------- #}
    {% if music.stages_shared %}
    <div class="stages-marquee scroll-reveal" aria-label="Stages shared">
      <div class="stages-marquee__label">Shared stages with</div>
      <div class="stages-marquee__track">
        {% for stage in music.stages_shared %}
        <span class="stages-marquee__item">{{ stage }}</span>
        {% endfor %}
        {# Duplicate for seamless scroll loop #}
        {% for stage in music.stages_shared %}
        <span class="stages-marquee__item" aria-hidden="true">{{ stage }}</span>
        {% endfor %}
      </div>
    </div>
    {% endif %}

    {# ------- Gallery ------- #}
    {% if music.gallery_images %}
    <div class="music__gallery scroll-reveal" aria-label="Music gallery">
      {% for img in music.gallery_images %}
      <div class="music__gallery-item">
        <img src="{{ asset_url(img) }}" alt="Performance photo" loading="lazy" />
      </div>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</section>
```

**Note:** Uses `asset_url()` — confirm this is a Jinja global registered in `app/__init__.py`. If not, register it:

```python
# in app/__init__.py, inside create_app()
from .backblaze import get_asset_url
app.jinja_env.globals["asset_url"] = get_asset_url
```

### 1.3 CSS additions in `app/static/css/styles.css`

Add these rules to the Music section. Use existing CSS variables — do not invent new colors.

```css
/* ============ BAND CARDS ============ */
.music__bands {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--space-lg);
  margin: var(--space-xl) 0;
}

.band-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
  display: flex;
  flex-direction: column;
}

.band-card:hover {
  transform: translateY(-4px);
  border-color: var(--color-accent);
}

.band-card--featured {
  border-color: var(--color-accent);
}

.band-card__image {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: var(--color-surface-alt);
}

.band-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.band-card__image--placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
}

.band-card__icon {
  font-size: 3rem;
  color: var(--color-accent);
  opacity: 0.6;
}

.band-card__body {
  padding: var(--space-md);
  flex: 1;
  display: flex;
  flex-direction: column;
}

.band-card__name {
  font-family: var(--font-serif);
  font-size: 1.5rem;
  color: var(--color-text);
  margin: 0 0 0.25rem 0;
}

.band-card__role {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-accent);
  margin: 0 0 var(--space-sm) 0;
}

.band-card__desc {
  color: var(--color-text-muted);
  line-height: 1.55;
  flex: 1;
}

.band-card__link {
  margin-top: var(--space-sm);
  color: var(--color-accent);
  font-weight: 600;
  text-decoration: none;
}

.band-card__link:hover {
  color: var(--color-accent-hover);
}

/* ============ STAGES MARQUEE ============ */
.stages-marquee {
  margin: var(--space-xl) 0;
  padding: var(--space-md) 0;
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
  overflow: hidden;
}

.stages-marquee__label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-text-muted);
  margin-bottom: var(--space-sm);
}

.stages-marquee__track {
  display: flex;
  gap: var(--space-lg);
  animation: marquee-scroll 40s linear infinite;
  white-space: nowrap;
  width: max-content;
}

.stages-marquee:hover .stages-marquee__track {
  animation-play-state: paused;
}

.stages-marquee__item {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  color: var(--color-text);
  padding: 0 var(--space-md);
  border-right: 1px solid var(--color-border);
}

.stages-marquee__item:last-child {
  border-right: none;
}

@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .stages-marquee__track {
    animation: none;
    flex-wrap: wrap;
    white-space: normal;
    width: auto;
  }
}
```

---

## Task 2 — Add Press Section (new)

The Press section appears **directly below** the Music section on the home page (not a separate route). It shows press coverage as cards with outlet name, article title, short pull-quote, date, and link.

### 2.1 Add `PRESS` dict to `app/content.py`

Place immediately after `MUSIC`:

```python
PRESS = {
    "headline": "Press",
    "subheadline": "Coverage, interviews, and reviews.",
    "intro": "A selection of press from across my music career.",
    "items": [
        {
            "outlet": "WJON",
            "title": "Sauk Rapids Native Making His Mark in the Music Business",
            "date": "February 2020",
            "url": "https://wjon.com/sauk-rapids-native-making-his-mark-in-the-music-business/",
            "pull_quote": "making his mark in the music business",
            "type": "Profile",
            "image": "",
        },
        {
            "outlet": "Sauk Rapids Herald",
            "title": "Pandemic at Rock the Riverside",
            "date": "2024",
            "url": "",  # Not online — print clipping only
            "pull_quote": "lead guitarist with the band Pandemic",
            "type": "Clipping",
            "image": "music/press/pandemic-clipping.jpg",  # TODO: upload
        },
        {
            "outlet": "AudioFuzz",
            "title": "Badass Rock N Roll: Code Red Riot — Living Low",
            "date": "July 2018",
            "url": "https://www.audiofuzz.com/2018/07/08/badass-rock-n-roll-code-red-riot-living-low/",
            "pull_quote": "fantastic guitar slinger",
            "type": "Review",
            "image": "",
        },
        {
            "outlet": "Dangerdog Music Reviews",
            "title": "Code Red Riot: Mask — Album Review",
            "date": "June 2018",
            "url": "https://dangerdog.com/2018-music-reviews/code-red-riot-mask.php",
            "pull_quote": "a heretofore hidden six string talent from Minnesota",
            "type": "Review",
            "image": "",
        },
        {
            "outlet": "Surviving the Golden Age",
            "title": "Code Red Riot: Mask",
            "date": "July 2018",
            "url": "https://survivingthegoldenage.com/code-red-riot-mask/",
            "pull_quote": "heady guitar solos",
            "type": "Review",
            "image": "",
        },
        {
            "outlet": "Indie Music Discovery",
            "title": "Interview with Code Red Riot — Mask",
            "date": "2018",
            "url": "https://www.indiemusicdiscovery.com/interview-code-red-riot/",
            "pull_quote": "",
            "type": "Interview",
            "image": "",
        },
    ],
}
```

**Quote length policy:** Keep all `pull_quote` fields under 15 words. If there's nothing to quote, leave empty — the card will render with outlet, title, date, and type only.

### 2.2 Register `press` in `app/routes.py`

In the route handler that renders the home page, import and pass `PRESS`:

```python
from .content import SITE, HERO, ABOUT, IDENTITY, MUSIC, PRESS, PROJECTS, MUSEUM, TIMELINE, CONTACT, SOCIAL_LINKS, FOOTER

# ...
return render_template(
    "index.html",
    site=SITE,
    hero=HERO,
    about=ABOUT,
    identity=IDENTITY,
    music=MUSIC,
    press=PRESS,  # <-- add
    projects=PROJECTS,
    museum=MUSEUM,
    timeline=TIMELINE,
    contact=CONTACT,
    social_links=SOCIAL_LINKS,
    footer=FOOTER,
)
```

### 2.3 Create `app/templates/partials/press.html`

```html
<section class="section press" id="press" aria-labelledby="press-heading">
  <div class="container">
    <div class="section-header scroll-reveal">
      <div class="section-label">Press</div>
      <h2 class="section-heading" id="press-heading">{{ press.headline }}</h2>
      <p class="section-sub">{{ press.subheadline }}</p>
    </div>

    {% if press.intro %}
    <p class="press__intro scroll-reveal">{{ press.intro }}</p>
    {% endif %}

    <div class="press__grid scroll-reveal">
      {% for item in press.items %}
      <article class="press-card">
        {% if item.image %}
        <div class="press-card__image">
          <img src="{{ asset_url(item.image) }}" alt="{{ item.outlet }} — {{ item.title }}" loading="lazy" />
        </div>
        {% endif %}
        <div class="press-card__body">
          <div class="press-card__meta">
            <span class="press-card__outlet">{{ item.outlet }}</span>
            {% if item.type %}<span class="press-card__type">{{ item.type }}</span>{% endif %}
          </div>
          <h3 class="press-card__title">{{ item.title }}</h3>
          {% if item.pull_quote %}
          <p class="press-card__quote">&ldquo;{{ item.pull_quote }}&rdquo;</p>
          {% endif %}
          <div class="press-card__footer">
            {% if item.date %}<span class="press-card__date">{{ item.date }}</span>{% endif %}
            {% if item.url %}
            <a class="press-card__link" href="{{ item.url }}" target="_blank" rel="noopener">
              Read →
            </a>
            {% endif %}
          </div>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
```

### 2.4 Include `press.html` in `app/templates/index.html`

Add `{% include 'partials/press.html' %}` **immediately after** the music partial include.

### 2.5 Add Press to the navbar

In `app/content.py`, wherever nav items are defined, add Press between Music and Projects. The exact structure depends on the nav data shape — read `app/content.py` first, then mirror the existing pattern. Do **not** add it in two places.

### 2.6 CSS for Press section (add to `styles.css`)

```css
/* ============ PRESS ============ */
.press {
  background: var(--color-surface-alt);
}

.press__intro {
  max-width: 60ch;
  margin: 0 auto var(--space-xl) auto;
  text-align: center;
  color: var(--color-text-muted);
}

.press__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-lg);
}

.press-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.press-card:hover {
  transform: translateY(-3px);
  border-color: var(--color-accent);
}

.press-card__image {
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background: var(--color-surface-alt);
}

.press-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: sepia(0.15) contrast(1.05);
}

.press-card__body {
  padding: var(--space-md);
  flex: 1;
  display: flex;
  flex-direction: column;
}

.press-card__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-xs);
}

.press-card__outlet {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  font-weight: 700;
}

.press-card__type {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  padding: 2px 8px;
  border: 1px solid var(--color-border);
  border-radius: 10px;
}

.press-card__title {
  font-family: var(--font-serif);
  font-size: 1.2rem;
  line-height: 1.35;
  color: var(--color-text);
  margin: 0 0 var(--space-sm) 0;
}

.press-card__quote {
  font-style: italic;
  color: var(--color-text-muted);
  line-height: 1.5;
  margin: 0 0 var(--space-sm) 0;
  flex: 1;
}

.press-card__footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: var(--space-sm);
  border-top: 1px solid var(--color-border);
}

.press-card__date {
  font-size: 0.8rem;
  color: var(--color-text-muted);
}

.press-card__link {
  color: var(--color-accent);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
}

.press-card__link:hover {
  color: var(--color-accent-hover);
}
```

---

## Task 3 — Azure Archives Case Study

Azure Archives is Tyler's flagship SaaS product (Azure Enterprises LLC). Currently it renders as one project card among many. Promote it to a dedicated case study with its own subpage while keeping a teaser card on the main projects list.

### 3.1 Expand the project entry in `app/content.py`

In `PROJECTS["list"]`, locate the existing Azure Archives entry. Replace it with the expanded version below. Keep the overall `PROJECTS` shape intact — only this one entry gets richer fields.

```python
{
    "title": "Azure Archives",
    "slug": "azure-archives",  # NEW — used to route to /projects/azure-archives
    "category": "Web Development",
    "subtitle": "Collections management built for small museums",
    "description": (
        "A full-stack SaaS platform that lets small museums, historical societies, "
        "and archives catalog donations, manage collections, track memberships, and "
        "publish research portals. Simpler than PastPerfect, more powerful than a spreadsheet."
    ),
    "stack": ["Flask", "PostgreSQL", "Jinja2", "Railway", "Backblaze B2", "Stripe", "OpenAI"],
    "status": "Live",
    "url": "https://azurearchives.com",
    "demo_url": "https://demo.azurearchives.com",
    "github": "",
    "featured": True,
    "has_case_study": True,  # NEW — enables "View case study" link

    # --- Case study content ---
    "case_study": {
        "tagline": "Simpler than PastPerfect. More powerful than a spreadsheet.",
        "problem": (
            "Small museums and historical societies are often stuck between two bad options: "
            "legacy desktop software like PastPerfect that's expensive and dated, or a "
            "patchwork of spreadsheets and shared drives that lose data and can't scale. "
            "Neither option gives the public a way to actually see the collection."
        ),
        "approach": (
            "I built Azure Archives as a web-first SaaS with a full audit trail, role-based "
            "approval workflows, DACS-compliant archival fields, and a public-facing research "
            "portal — all on infrastructure that costs pennies per org to run. The AI features "
            "(donation slip scanning, handwritten document transcription, Story Composer) handle "
            "the tedious cataloging work so volunteers can focus on the collection itself."
        ),
        "features": [
            {
                "icon": "📥",
                "title": "Donation Intake",
                "text": "Log donations by hand, import from Excel, or scan physical slips with vision AI.",
            },
            {
                "icon": "🏛",
                "title": "Cataloging",
                "text": "Photos, provenance, condition, location tracking. Role-based approval keeps data clean.",
            },
            {
                "icon": "📂",
                "title": "DACS-Compliant Archives",
                "text": "Finding aids, format tracking, and full-text search across holdings.",
            },
            {
                "icon": "👥",
                "title": "Memberships",
                "text": "Tiers, renewals, payments, and a public signup form. Export for mailing lists.",
            },
            {
                "icon": "🌐",
                "title": "Public Research Portal",
                "text": "Share the collection online. Control per-item visibility. Accept research requests.",
            },
            {
                "icon": "🤖",
                "title": "AI-Powered Tools",
                "text": "Slip scanning, handwritten OCR, and AI-drafted collection stories. Staff reviews every save.",
            },
            {
                "icon": "📊",
                "title": "Board-Ready Reports",
                "text": "Grant-ready collection summaries and board packets generated from live data.",
            },
            {
                "icon": "🔁",
                "title": "No Lock-In",
                "text": "Full CSV/ZIP export at any time. Your data is always yours.",
            },
        ],
        "pricing_tiers": [
            {
                "name": "Free Trial",
                "price": "$0",
                "period": "30 days",
                "note": "All features, 10 GB storage, no credit card required.",
            },
            {
                "name": "Collections",
                "price": "$790",
                "period": "/ year",
                "note": "Everything a small museum needs to catalog, archive, and share.",
            },
            {
                "name": "Collections + Research",
                "price": "$1,190",
                "period": "/ year",
                "note": "Adds genealogy indexes, legacy data crosswalk, and research portal.",
            },
            {
                "name": "Enterprise",
                "price": "from $2,990",
                "period": "/ year",
                "note": "Unlimited storage, custom domain, API access, priority support.",
            },
        ],
        "differentiators": [
            "Grant-fundable: eligible for Minnesota Legacy Grants, IMLS Inspire! Grants for Small Museums, and similar programs.",
            "No per-record fees. No item caps. Unlimited users.",
            "AI tools built in, not bolted on — each action uses one credit with generous monthly allocations.",
            "Staff always reviews before anything saves. AI assists; humans decide.",
        ],
        "tech_notes": (
            "Built with Flask and Jinja2 on Railway, Postgres for relational data, Backblaze B2 "
            "for media storage with presigned URLs for sensitive items, Stripe for subscription "
            "billing, and OpenAI for the vision and language model features. Role-based access "
            "control, full change history, and multi-tenant subdomain routing."
        ),
        "gallery_images": [
            "projects/azure-archives/dashboard.jpg",  # TODO: upload screenshots
            "projects/azure-archives/cataloging.jpg",
            "projects/azure-archives/public-portal.jpg",
            "projects/azure-archives/story-composer.jpg",
        ],
        "cta_text": "Start a free 30-day trial",
        "cta_url": "https://azurearchives.com/signup",
    },
},
```

### 3.2 Add a new route in `app/routes.py`

```python
from flask import abort

@main.route("/projects/<slug>")
def project_detail(slug):
    from .content import PROJECTS, SITE, SOCIAL_LINKS, FOOTER
    project = next((p for p in PROJECTS["list"] if p.get("slug") == slug and p.get("has_case_study")), None)
    if project is None:
        abort(404)
    return render_template(
        "project_detail.html",
        site=SITE,
        project=project,
        social_links=SOCIAL_LINKS,
        footer=FOOTER,
    )
```

### 3.3 Create `app/templates/project_detail.html`

This extends `base.html` but without the full home-page section stack.

```html
{% extends "base.html" %}

{% block title %}{{ project.title }} — {{ site.title }}{% endblock %}

{% block content %}
<article class="project-detail">
  <header class="project-detail__hero">
    <div class="container">
      <a class="project-detail__back" href="/#projects">← Back to projects</a>
      <div class="project-detail__category">{{ project.category }}</div>
      <h1 class="project-detail__title">{{ project.title }}</h1>
      {% if project.subtitle %}
      <p class="project-detail__subtitle">{{ project.subtitle }}</p>
      {% endif %}
      {% if project.case_study.tagline %}
      <p class="project-detail__tagline">{{ project.case_study.tagline }}</p>
      {% endif %}

      <div class="project-detail__actions">
        {% if project.url %}
        <a class="btn btn--primary" href="{{ project.url }}" target="_blank" rel="noopener">
          Visit Live Site →
        </a>
        {% endif %}
        {% if project.demo_url %}
        <a class="btn btn--secondary" href="{{ project.demo_url }}" target="_blank" rel="noopener">
          Try the Demo
        </a>
        {% endif %}
      </div>

      <div class="project-detail__stack">
        {% for tech in project.stack %}
        <span class="stack-tag">{{ tech }}</span>
        {% endfor %}
      </div>
    </div>
  </header>

  <section class="project-detail__section">
    <div class="container container--narrow">
      <h2>The Problem</h2>
      <p>{{ project.case_study.problem }}</p>

      <h2>The Approach</h2>
      <p>{{ project.case_study.approach }}</p>
    </div>
  </section>

  <section class="project-detail__section project-detail__section--alt">
    <div class="container">
      <h2>What It Does</h2>
      <div class="feature-grid">
        {% for feature in project.case_study.features %}
        <div class="feature-card">
          <div class="feature-card__icon" aria-hidden="true">{{ feature.icon }}</div>
          <h3 class="feature-card__title">{{ feature.title }}</h3>
          <p class="feature-card__text">{{ feature.text }}</p>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>

  {% if project.case_study.gallery_images %}
  <section class="project-detail__section">
    <div class="container">
      <h2>Product Screenshots</h2>
      <div class="screenshot-grid">
        {% for img in project.case_study.gallery_images %}
        <div class="screenshot-grid__item">
          <img src="{{ asset_url(img) }}" alt="{{ project.title }} screenshot" loading="lazy" />
        </div>
        {% endfor %}
      </div>
    </div>
  </section>
  {% endif %}

  <section class="project-detail__section project-detail__section--alt">
    <div class="container container--narrow">
      <h2>What Makes It Different</h2>
      <ul class="differentiator-list">
        {% for point in project.case_study.differentiators %}
        <li>{{ point }}</li>
        {% endfor %}
      </ul>
    </div>
  </section>

  {% if project.case_study.pricing_tiers %}
  <section class="project-detail__section">
    <div class="container">
      <h2>Pricing</h2>
      <div class="pricing-grid">
        {% for tier in project.case_study.pricing_tiers %}
        <div class="pricing-card">
          <div class="pricing-card__name">{{ tier.name }}</div>
          <div class="pricing-card__price">
            {{ tier.price }}
            {% if tier.period %}<span class="pricing-card__period">{{ tier.period }}</span>{% endif %}
          </div>
          <p class="pricing-card__note">{{ tier.note }}</p>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>
  {% endif %}

  <section class="project-detail__section project-detail__section--alt">
    <div class="container container--narrow">
      <h2>Technical Notes</h2>
      <p>{{ project.case_study.tech_notes }}</p>
    </div>
  </section>

  <section class="project-detail__cta">
    <div class="container">
      <h2>{{ project.case_study.cta_text or "Ready to get started?" }}</h2>
      {% if project.case_study.cta_url %}
      <a class="btn btn--primary btn--large" href="{{ project.case_study.cta_url }}" target="_blank" rel="noopener">
        {{ project.case_study.cta_text or "Get Started" }} →
      </a>
      {% endif %}
    </div>
  </section>
</article>
{% endblock %}
```

### 3.4 Update the project card on the home page

In `app/templates/partials/projects.html`, for any project with `has_case_study == True`, show an additional "View Case Study" link alongside the existing Live/GitHub links:

```html
{% if project.has_case_study and project.slug %}
<a class="project-card__link project-card__link--case-study" href="/projects/{{ project.slug }}">
  View Case Study →
</a>
{% endif %}
```

### 3.5 CSS for project detail page (add to `styles.css`)

```css
/* ============ PROJECT DETAIL ============ */
.project-detail__hero {
  padding: calc(var(--space-xl) * 2) 0 var(--space-xl) 0;
  background: linear-gradient(180deg, var(--color-surface-alt), var(--color-bg));
  border-bottom: 1px solid var(--color-border);
}

.project-detail__back {
  display: inline-block;
  margin-bottom: var(--space-md);
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: 0.9rem;
}

.project-detail__back:hover { color: var(--color-accent); }

.project-detail__category {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  margin-bottom: var(--space-xs);
}

.project-detail__title {
  font-family: var(--font-serif);
  font-size: clamp(2.5rem, 5vw, 4rem);
  line-height: 1.05;
  margin: 0 0 var(--space-sm) 0;
}

.project-detail__subtitle {
  font-size: 1.3rem;
  color: var(--color-text-muted);
  margin: 0 0 var(--space-md) 0;
}

.project-detail__tagline {
  font-style: italic;
  color: var(--color-text);
  font-size: 1.1rem;
  max-width: 60ch;
  margin: 0 0 var(--space-lg) 0;
}

.project-detail__actions {
  display: flex;
  gap: var(--space-sm);
  flex-wrap: wrap;
  margin: var(--space-lg) 0;
}

.project-detail__stack {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-xs);
}

.stack-tag {
  font-size: 0.8rem;
  padding: 4px 12px;
  border: 1px solid var(--color-border);
  border-radius: 12px;
  color: var(--color-text-muted);
}

.project-detail__section {
  padding: var(--space-xl) 0;
}

.project-detail__section--alt {
  background: var(--color-surface-alt);
}

.container--narrow {
  max-width: 72ch;
}

.project-detail__section h2 {
  font-family: var(--font-serif);
  font-size: 2rem;
  margin: 0 0 var(--space-md) 0;
}

.project-detail__section p {
  color: var(--color-text-muted);
  line-height: 1.7;
  font-size: 1.05rem;
}

/* Feature grid */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--space-md);
  margin-top: var(--space-lg);
}

.feature-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-md);
}

.feature-card__icon { font-size: 2rem; margin-bottom: var(--space-xs); }
.feature-card__title {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  margin: 0 0 var(--space-xs) 0;
}
.feature-card__text { color: var(--color-text-muted); font-size: 0.95rem; line-height: 1.5; margin: 0; }

/* Pricing grid */
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: var(--space-md);
  margin-top: var(--space-lg);
}

.pricing-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-md);
  text-align: center;
}

.pricing-card__name {
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.8rem;
  color: var(--color-accent);
  margin-bottom: var(--space-xs);
}

.pricing-card__price {
  font-family: var(--font-serif);
  font-size: 2rem;
  color: var(--color-text);
}

.pricing-card__period {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-left: 4px;
}

.pricing-card__note {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-top: var(--space-xs);
}

/* Differentiator list */
.differentiator-list {
  list-style: none;
  padding: 0;
}

.differentiator-list li {
  padding: var(--space-sm) 0;
  border-bottom: 1px solid var(--color-border);
  position: relative;
  padding-left: var(--space-md);
  color: var(--color-text);
}

.differentiator-list li:before {
  content: "→";
  color: var(--color-accent);
  position: absolute;
  left: 0;
  font-weight: 700;
}

.differentiator-list li:last-child { border-bottom: none; }

/* Screenshot grid */
.screenshot-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--space-md);
  margin-top: var(--space-lg);
}

.screenshot-grid__item {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  background: var(--color-surface);
}

.screenshot-grid__item img { width: 100%; height: auto; display: block; }

/* Project CTA */
.project-detail__cta {
  padding: calc(var(--space-xl) * 1.5) 0;
  text-align: center;
  background: var(--color-bg);
  border-top: 1px solid var(--color-border);
}

.project-detail__cta h2 {
  font-family: var(--font-serif);
  font-size: 2.2rem;
  margin-bottom: var(--space-md);
}

.btn--large {
  font-size: 1.1rem;
  padding: var(--space-sm) var(--space-lg);
}
```

---

## Task 4 — Backblaze Image Uploads

Tyler needs to upload images before the TODO paths resolve. If `BACKBLAZE_BUCKET_URL` falls back to local, the site still renders — it just won't show the real images.

Folder structure to create in the Backblaze bucket:

```
music/
  bands/
    code-red-riot.jpg
    pandemic.jpg
    hairball.jpg
    rockshow.jpg
    raised-on-radio.jpg
    la-madness.jpg
  gallery/
    hairflip-ramones.jpg
    goldtop-horns-fire.jpg
    stage-teal-lespaul.jpg
    brainerd-sunflare.jpg
    duo-purple-stage.jpg
    gibson-lespaul-bw.jpg
    sunburst-daytime.jpg
    acoustic-duo-summerfest.jpg
    acoustic-hoodie-bw.jpg
  press/
    pandemic-clipping.jpg
projects/
  azure-archives/
    dashboard.jpg
    cataloging.jpg
    public-portal.jpg
    story-composer.jpg
```

Recommended sizing: long edge 1600px, JPG 80% quality. Hero/featured images can go to 2000px.

---

## Task 5 — Update `CLAUDE.md` (the repo's context file)

Add the following sections to the top of `CLAUDE.md` so future Claude Code runs are aware of the new structure:

```markdown
## Music Section — Band-First Structure

The Music section uses `MUSIC["bands"]` (not `highlights`). Each band has:
name, role, description, url, image, featured. **Never add year ranges or timeline data to bands** — Tyler has explicitly omitted this.

Related: `MUSIC["stages_shared"]` (marquee), `MUSIC["gallery_images"]` (photo grid).

## Press Section

Press lives in `content.py` as `PRESS`. Template at `partials/press.html`, included on `index.html` directly after music. Each press item must have: outlet, title, date, url, pull_quote (under 15 words or empty), type, image.

## Project Case Studies

Projects with `has_case_study: True` and a `slug` get their own detail page at `/projects/<slug>`. Case study content lives inside the project dict under a `case_study` key containing: tagline, problem, approach, features, pricing_tiers, differentiators, tech_notes, gallery_images, cta_text, cta_url.

Azure Archives is currently the only project with a case study. Pattern is extensible — other projects can opt in by adding the same fields.
```

---

## Testing Checklist

Before pushing, verify locally with `python app.py`:

1. Home page loads without 500 error
2. Music section shows band cards (placeholder icons ok if images not uploaded yet)
3. Stages marquee scrolls and pauses on hover
4. Press section renders below music with all six cards
5. Press cards link out correctly (target="_blank")
6. Navbar includes Press link and scrolls to `#press`
7. Clicking "View Case Study" on Azure Archives goes to `/projects/azure-archives`
8. Case study page renders all sections: hero, problem, approach, features, pricing, differentiators, tech notes, CTA
9. "Back to projects" link returns to `/#projects` on home
10. Non-existent project slug returns 404 cleanly: `/projects/does-not-exist`
11. Mobile responsive — resize to 375px and confirm no layout breaks
12. `prefers-reduced-motion` disables marquee animation

---

## Deployment

Once local testing passes:

```bash
git add .
git commit -m "Rebuild music section around bands, add press section, add Azure Archives case study"
git push
```

Railway auto-deploys in ~60 seconds. Check Deployments tab for status. If deploy fails, check logs for missing imports or template path issues.

---

## Outstanding TODOs for Tyler (not Claude Code)

These are items Tyler needs to supply manually — Claude Code should not guess:

- [ ] URLs for each band (Code Red Riot, Pandemic, Hairball, Rockstar Bob's Rockshow, Raised on Radio, La Madness)
- [ ] Upload band images to Backblaze `music/bands/`
- [ ] Upload gallery performance photos to Backblaze `music/gallery/`
- [ ] Upload Pandemic newspaper clipping to Backblaze `music/press/`
- [ ] Upload Azure Archives product screenshots to Backblaze `projects/azure-archives/`
- [ ] Confirm or adjust `case_study` copy for Azure Archives (problem, approach, tech_notes)
- [ ] Decide whether to add the 2022 lymphoma story anywhere on the site
