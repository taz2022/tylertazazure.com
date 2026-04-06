"""
content.py — Single source of truth for all site content.

Edit this file to update copy, projects, music highlights, museum work,
social links, and contact info without touching templates.

Placeholder values are marked with: # TODO: update
"""

# ---------------------------------------------------------------------------
# SITE META
# ---------------------------------------------------------------------------
SITE = {
    "title": "Tyler Azure",
    "tagline": "Musician. Builder. Museum Modernizer.",
    "description": (
        "Tyler Azure is a musician, web developer, and museum professional "
        "who works across performance, software, and preservation."
    ),
    "contact_email": "tyler@tylerazu.re",  # TODO: update
    "contact_email_label": "tyler@tylerazu.re",  # display text
}

# ---------------------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------------------
NAV_LINKS = [
    {"label": "About", "href": "#about"},
    {"label": "Music", "href": "#music"},
    {"label": "Projects", "href": "#projects"},
    {"label": "Museum Work", "href": "#museum"},
    {"label": "Journey", "href": "#timeline"},
    {"label": "Contact", "href": "#contact"},
]

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
HERO = {
    "name": "Tyler Azure",
    "headline": "Musician. Builder. Museum Modernizer.",
    "subheadline": (
        "I perform on stage, build digital tools, and bring modern thinking "
        "to archives, collections, and history."
    ),
    "cta_primary": {"label": "View My Work", "href": "#projects"},
    "cta_secondary": {"label": "Get in Touch", "href": "#contact"},
    # Set these to Backblaze paths once uploaded, e.g. "hero/background.jpg"
    "background_image": "",  # TODO: update — leave blank for CSS gradient fallback
}

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
ABOUT = {
    "intro": (
        "I've spent years moving between worlds that most people keep separate — "
        "the stage, the codebase, and the archive. Each one has shaped how I think "
        "and what I build."
    ),
    "body": (
        "Music gave me discipline, creative range, and the ability to read a room. "
        "Development gave me systems thinking and the satisfaction of solving real problems. "
        "Museum and archival work gave me a respect for story, structure, and the long view. "
        "Together, they make me a different kind of professional — one who can perform, "
        "build, and preserve with equal seriousness."
    ),
    "portrait_image": "",  # TODO: update — Backblaze path or local filename
    "stats": [
        {"label": "Years in Music", "value": "10+"},           # TODO: update
        {"label": "Projects Built", "value": "20+"},           # TODO: update
        {"label": "Museum Roles", "value": "3+"},              # TODO: update
        {"label": "Disciplines Combined", "value": "One"},
    ],
}

# ---------------------------------------------------------------------------
# IDENTITY (Three Pillars)
# ---------------------------------------------------------------------------
IDENTITY = {
    "headline": "Three worlds. One approach.",
    "subheadline": (
        "The things that seem unrelated are usually the most connected. "
        "Here's how music, code, and history feed each other."
    ),
    "pillars": [
        {
            "icon": "♩",
            "title": "Music",
            "description": (
                "Performance taught me creative discipline, stage presence, and how to "
                "connect with an audience — skills that transfer directly into every client "
                "interaction and public-facing project I take on."
            ),
        },
        {
            "icon": "⌨",
            "title": "Development",
            "description": (
                "Building software taught me to think in systems — to ask not just "
                "\"does this work?\" but \"will this still work in two years?\" I build "
                "things that are useful, maintainable, and built to last."
            ),
        },
        {
            "icon": "🏛",
            "title": "Museum Work",
            "description": (
                "Archives and preservation taught me that how you steward information "
                "matters as much as the information itself. I bring that same care to "
                "every project, whether it's a digital system or a historical collection."
            ),
        },
    ],
    "synthesis": (
        "Most people specialize in one lane. I've always worked across them — "
        "and I've found that the unexpected connections between music, technology, "
        "and history are exactly where the most interesting work happens."
    ),
}

# ---------------------------------------------------------------------------
# MUSIC
# ---------------------------------------------------------------------------
MUSIC = {
    "headline": "Music",
    "subheadline": "Guitar. Performance. Live events. This is where it all started.",
    "intro": (
        "Music isn't a side project. It's been a central part of my professional "
        "life for over a decade — performing live, working events, and developing "
        "a creative foundation that informs everything else I do."
    ),
    "highlights": [
        {
            "title": "Live Performance",
            "description": (
                "Experienced performer across venues and event formats — "
                "from intimate sets to large live events."
            ),
            "image": "",  # TODO: update
        },
        {
            "title": "Guitar",
            "description": (
                "Guitar is my primary instrument. I play across genres and bring "
                "technical ability and musical feel to every performance."
            ),
            "image": "",  # TODO: update
        },
        {
            "title": "Events & Entertainment",
            "description": (
                "Wedding performer, DJ, and MC work. I know how to read a room, "
                "keep energy up, and make events memorable."
            ),
            "image": "",  # TODO: update
        },
    ],
    "gallery_images": [],  # TODO: add Backblaze paths, e.g. ["music/show1.jpg", ...]
}

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
PROJECTS = {
    "headline": "Projects",
    "subheadline": "Things I've designed, built, and shipped.",
    "intro": (
        "I build practical digital tools — websites, systems, and applications "
        "that solve real problems cleanly. Here's a selection of recent work."
    ),
    "list": [
        {
            "title": "Azure Archives",
            "category": "Web Development",
            "description": (
                "A digital archive and research platform for historical records and "
                "collections. Built with Flask, Railway, and Backblaze B2."
            ),
            "stack": ["Flask", "Jinja2", "Railway", "Backblaze B2"],
            "status": "Live",
            "url": "https://azurearchives.com",
            "github": "",
            "featured": True,
        },
        {
            "title": "Personal Website",
            "category": "Web Development",
            "description": "This site. Built with Flask, deployed on Railway.",
            "stack": ["Flask", "Jinja2", "Railway"],
            "status": "Live",
            "url": "#",
            "github": "",
            "featured": False,
        },
        # TODO: Add more projects following this structure
    ],
    "categories": [
        "All",
        "Web Development",
        "App Development",
        "Automation / Tools",
        "Museum Technology",
        "AI-Assisted Systems",
    ],
}

# ---------------------------------------------------------------------------
# MUSEUM / ARCHIVES
# ---------------------------------------------------------------------------
MUSEUM = {
    "headline": "Museum & Archival Work",
    "subheadline": "Preservation, digitization, and systems modernization.",
    "intro": (
        "I've worked with museums, historical societies, and archival collections — "
        "bringing modern tools and workflows to institutions that have long histories "
        "worth protecting and sharing."
    ),
    "cards": [
        {
            "icon": "📦",
            "title": "Archives & Digitization",
            "description": (
                "Converting physical records and collections into accessible, "
                "searchable digital formats. Making history findable."
            ),
        },
        {
            "icon": "⚙",
            "title": "Systems Modernization",
            "description": (
                "Updating legacy workflows with tools that actually work — "
                "databases, collection management, and digital infrastructure."
            ),
        },
        {
            "icon": "📖",
            "title": "Historical Storytelling",
            "description": (
                "Helping institutions share their collections with the public "
                "through thoughtful digital experiences and web presence."
            ),
        },
        {
            "icon": "🗂",
            "title": "Collections Support",
            "description": (
                "Organizing, cataloging, and maintaining collections — "
                "with an eye toward long-term usability and access."
            ),
        },
    ],
    "quote": (
        "Good archives don't just store the past. They make it usable."
    ),
}

# ---------------------------------------------------------------------------
# TIMELINE / JOURNEY
# ---------------------------------------------------------------------------
TIMELINE = {
    "headline": "The Journey",
    "subheadline": "Music, code, and history — in roughly the order they happened.",
    "events": [
        {
            "period": "Early Years",          # TODO: add approximate dates
            "category": "Music",
            "title": "Started Playing Guitar",
            "description": "Picked up guitar and began performing — what became a decade-long career in live music.",
        },
        {
            "period": "Mid Career",           # TODO: update
            "category": "Music",
            "title": "Live Performance & Events",
            "description": "Built a professional presence in live music, events, weddings, and entertainment.",
        },
        {
            "period": "Transition",           # TODO: update
            "category": "Development",
            "title": "Started Building for the Web",
            "description": "Began learning software development and building practical tools and websites.",
        },
        {
            "period": "Recent",               # TODO: update
            "category": "Museum",
            "title": "Museum & Archival Work",
            "description": "Joined museum and historical society projects, bringing digital tools to preservation work.",
        },
        {
            "period": "Now",
            "category": "All Three",
            "title": "Music + Code + History",
            "description": "Working across all three disciplines — performing, building, and preserving.",
        },
    ],
}

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
CONTACT = {
    "headline": "Let's Work Together",
    "subheadline": (
        "Whether it's a web project, a music event, or museum technology work — "
        "I'd like to hear what you're building."
    ),
    "email": SITE["contact_email"],
    "email_label": SITE["contact_email_label"],
}

# ---------------------------------------------------------------------------
# SOCIAL LINKS
# ---------------------------------------------------------------------------
SOCIAL_LINKS = [
    {"platform": "GitHub", "url": "#", "icon": "github"},      # TODO: update
    {"platform": "LinkedIn", "url": "#", "icon": "linkedin"},  # TODO: update
    # {"platform": "Instagram", "url": "#", "icon": "instagram"},
    # {"platform": "Twitter", "url": "#", "icon": "twitter"},
]

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
FOOTER = {
    "tagline": "Musician. Builder. Museum Modernizer.",
    "copyright": "Tyler Azure",
}
