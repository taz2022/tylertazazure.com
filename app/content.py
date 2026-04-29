"""
content.py — Single source of truth for site content, organized by discipline.

Press content is NOT in this file — it loads from press/press-inventory.json via
press_loader.py and is filtered by type at render time.
"""

# ───────────────────────────────────────────────────────────
# SITE META — global
# ───────────────────────────────────────────────────────────
SITE = {
    "title": "Tyler Azure",
    "tagline": "Guitarist based in Minnesota.",
    "description": (
        "Tyler Azure is a guitarist based in Minnesota. "
        "Lead guitar in Pandemic, Code Red Riot, and more."
    ),
    "contact_email": "azuretaz@gmail.com",  # TODO: confirm
    "base_url": "https://tylertazazure.com",
}

# ───────────────────────────────────────────────────────────
# NAV
# ───────────────────────────────────────────────────────────
NAV = {
    "left": [
        {"label": "Music", "href": "/music"},
        {"label": "Videos", "href": "/videos"},
        {"label": "Shows", "href": "/shows"},
    ],
    "right": [
        {"label": "About",   "href": "/#about"},
        {"label": "Press",   "href": "/press"},
        {"label": "Contact", "href": "/#contact"},
    ],
}

# ───────────────────────────────────────────────────────────
# HUB — homepage
# ───────────────────────────────────────────────────────────
HUB = {
    "hero": {
        "name": "Tyler \u201cTaz\u201d Azure",
        "pill": "Available for booking",
    },
}

# ───────────────────────────────────────────────────────────
# MUSIC — /music discipline page content
# ───────────────────────────────────────────────────────────
MUSIC = {
    "hero": {
        "title": "Music",
        "subtitle": "Guitar. Performance. Live rock.",
        "intro": (
            "I started playing guitar at 13 after watching Prince play Purple Rain "
            "live. Since then I\u2019ve played lead across rock, alt-rock, tribute, and "
            "live-event work \u2014 from Minneapolis rooms to the Las Vegas strip."
        ),
    },
    "bands": [
        {
            "slug": "pandemic",
            "name": "Pandemic",
            "role": "Lead Guitar",
            "status": "Current",
            "short": "Central Minnesota rock band. Active on the regional festival circuit.",
            "url_external": "https://pandemicfever.com",
            "card_image": "music/bands/Pandemic-Header-Logo.png",
            "featured": True,
        },
        {
            "slug": "code-red-riot",
            "name": "Code Red Riot",
            "role": "Lead Guitar",
            "status": "2017\u2013",
            "short": "Hard rock from Las Vegas, signed to Sony RED Music. Debut album Mask (2018).",
            "url_external": "https://linktr.ee/coderedriot",
            "card_image": "music/bands/code red riot.jpg",
            "featured": True,
        },
        {
            "slug": "hairball",
            "name": "Hairball",
            "role": "Fill-in Guitar",
            "status": "Guest",
            "short": "National-touring rock tribute from Minnesota. Van Halen, KISS, M\u00f6tley Cr\u00fce, Queen.",
            "url_external": "https://hairballonline.com",
            "card_image": "music/bands/hairball.webp",
            "featured": False,
        },
        {
            "slug": "rockstar-bobs-rockshow",
            "name": "Rockstar Bob\u2019s Rockshow",
            "role": "Guitar / Vocals",
            "status": "Current",
            "short": "Regional rock act selling out Midwest venues.",
            "url_external": "https://rockstarbob.com",
            "card_image": "music/bands/rockshow.jpg",
            "featured": False,
        },
        {
            "slug": "raised-on-radio",
            "name": "Raised on Radio",
            "role": "Guest Guitar",
            "status": "Occasional",
            "short": "Classic rock variety pulling musicians from Diamondback, Outside Recess, Pandemic, Chaser.",
            "url_external": "",
            "card_image": "music/bands/RaisedOnRadio.webp",
            "featured": False,
        },
        {
            "slug": "la-madness",
            "name": "La Madness",
            "role": "Lead Guitar, Backing Vocals",
            "status": "2013 era",
            "short": "Minneapolis indie grind blues. Debut album Chances Are. Opened for Papa Roach, Fuel, Tantric.",
            "url_external": "",
            "card_image": "music/bands/la madness.jpg",
            "featured": False,
        },
        {
            "slug": "taz-and-t-bone",
            "name": "Taz & T-Bone",
            "role": "Lead Guitar",
            "status": "Current",
            "short": "Acoustic duo playing mostly 80s covers.",
            "url_external": "",
            "card_image": "music/bands/Taz&TBone.png",
            "featured": False,
        },
        {
            "slug": "dirtee-circus",
            "name": "Dirtee Circus",
            "role": "Lead Guitar",
            "status": "Past",
            "short": "The next evolution \u2014 a band born out of L.H.D. in our twenties.",
            "url_external": "https://www.facebook.com/dirteecircusband/",
            "card_image": "music/bands/Dirtee_Circus.jpg",
            "featured": False,
        },
        {
            "slug": "diamondback",
            "name": "Diamondback",
            "role": "Lead Guitar",
            "status": "Past",
            "short": "Fill-in guitar work.",
            "url_external": "https://www.facebook.com/diamondbackbandmn/",
            "card_image": "music/bands/Diamondback.jpg",
            "featured": False,
        },
        {
            "slug": "almost-cooper",
            "name": "Almost Cooper",
            "role": "Lead Guitar",
            "status": "Past",
            "short": "Alice Cooper tribute band.",
            "url_external": "https://almostcooper.com/",
            "card_image": "music/bands/Almost_Cooper.png",
            "featured": False,
        },
    ],
    "stages_shared": [
        "Breaking Benjamin", "Eagles of Death Metal", "Steel Panther", "Fozzy",
        "Papa Roach", "Fuel", "Tantric", "Gemini Syndrome",
        "Las Rageous Festival", "Whisky A Go Go", "House of Blues", "First Avenue",
    ],
    "gallery_images": [
        "music/gallery/preview.webp",
        "music/gallery/preview (1).webp",
        "music/gallery/preview (2).webp",
        "music/gallery/preview (4).webp",
        "music/gallery/preview (5).webp",
        "music/gallery/preview (6).webp",
        "music/gallery/preview (7).webp",
        "music/gallery/preview (8).webp",
        "music/gallery/preview (9).webp",
    ],
}

# ───────────────────────────────────────────────────────────
# VIDEOS — /videos page + band sub-pages
# ───────────────────────────────────────────────────────────
VIDEOS = [
    {"id": "O1O3e3SnuN8", "title": "Bulletproof (Official Video)", "band": "Code Red Riot", "category": "music_video"},
    {"id": "M31OIYEujcA", "title": "Living Low", "band": "Code Red Riot", "category": "music_video"},
    {"id": "w7Qan1Vd8BA", "title": "Slide", "band": "Code Red Riot", "category": "music_video"},
    {"id": "aMLCKKeZDSA", "title": "Killing The Kings (Official Video)", "band": "Code Red Riot", "category": "music_video"},
    {"id": "Bq3AUO0Lk6Q", "title": "Ghost (Lyric Video)", "band": "Code Red Riot", "category": "music_video"},
    {"id": "qrV4VrMph_o", "title": "Handle This (Lyric Video)", "band": "Code Red Riot", "category": "music_video"},
    {"id": "nxKLCgVkv2k", "title": "Bulletproof \u2014 Acoustic Live (Rock 94\u00bd, Spokane)", "band": "Code Red Riot", "category": "live"},
]

# ───────────────────────────────────────────────────────────
# SHOWS — /shows page content
# ───────────────────────────────────────────────────────────
SHOWS = {
    "hero": {
        "title": "Shows",
        "subtitle": "Upcoming dates",
        "intro": "Catch me live. Check back for new dates.",
    },
    "upcoming": [
        {"date": "2026-01-10", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-01-30", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-02-06", "venue": "Stoney\u2019s Bar", "city": "Rockville, MN", "time": "8:30pm\u201312:30am", "band": "Pandemic", "url": ""},
        {"date": "2026-02-07", "venue": "Floyd\u2019s Bar", "city": "Victoria, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-02-27", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-02-28", "venue": "The Park (Celebration of life for Trisha)", "city": "Waite Park, MN", "time": "8pm\u201311pm", "band": "Pandemic", "url": ""},
        {"date": "2026-03-07", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-03-13", "venue": "Pioneer Place", "city": "Saint Cloud, MN", "time": "7:30pm\u201310pm", "band": "Pandemic", "url": ""},
        {"date": "2026-03-14", "venue": "Route 47", "city": "Fridley, MN", "time": "8pm\u201311:30pm", "band": "Pandemic", "url": ""},
        {"date": "2026-03-27", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-03-28", "venue": "Forada Bar and Grill", "city": "Forada, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-04-03", "venue": "Stoney\u2019s Bar", "city": "Rockville, MN", "time": "8:30pm\u201312:30am", "band": "Pandemic", "url": ""},
        {"date": "2026-04-09", "venue": "Arrowwood (Private event)", "city": "Alexandria, MN", "time": "7:30pm\u201311:30pm", "band": "Pandemic", "url": ""},
        {"date": "2026-04-18", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-04-24", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-05-02", "venue": "Pounders Bar and Grill", "city": "Cologne, MN", "time": "8:30pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-05-15", "venue": "La Playette", "city": "Saint Joe, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-05-16", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-05-27", "venue": "Rolling Ridge \u2014 Woodfire Wednesdays", "city": "St. Joe, MN", "time": "6pm\u20139pm", "band": "Taz & T-Bone", "url": ""},
        {"date": "2026-06-11", "venue": "Rock the River", "city": "Sauk Rapids, MN", "time": "7pm\u20139:30pm", "band": "Pandemic", "url": ""},
        {"date": "2026-06-12", "venue": "Onamia Days", "city": "Onamia, MN", "time": "TBD", "band": "Maddie Braun Band", "url": ""},
        {"date": "2026-06-13", "venue": "Fired Up Bar and Grill", "city": "Alexandria, MN", "time": "7pm\u201311pm", "band": "Pandemic", "url": ""},
        {"date": "2026-06-19", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-06-20", "venue": "2 Tall Tavern", "city": "Cushing, MN", "time": "7pm\u201310pm", "band": "Pandemic", "url": ""},
        {"date": "2026-06-25", "venue": "Charlie\u2019s", "city": "Becker, MN", "time": "6pm\u20139pm", "band": "Taz & T-Bone", "url": ""},
        {"date": "2026-06-26", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-07-10", "venue": "Chisago County Fair", "city": "Rush City, MN", "time": "9pm\u20131am", "band": "Pandemic", "url": ""},
        {"date": "2026-07-11", "venue": "Carlos Street Dance", "city": "Carlos, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-07-24", "venue": "Mid Summer Music Fest", "city": "TBD", "time": "TBD", "band": "Pandemic", "url": ""},
        {"date": "2026-07-25", "venue": "Cold Spring Music Festival", "city": "Cold Spring, MN", "time": "8pm\u201311pm", "band": "Pandemic", "url": ""},
        {"date": "2026-07-31", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-08-01", "venue": "Fired Up Bar and Grill", "city": "Alexandria, MN", "time": "7pm\u201311pm", "band": "Pandemic", "url": ""},
        {"date": "2026-08-13", "venue": "MT\u2019s on 8th", "city": "St. Cloud, MN", "time": "6pm\u20139pm", "band": "Taz & T-Bone", "url": ""},
        {"date": "2026-08-15", "venue": "The Outskirts (Outdoor party)", "city": "Forada, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-08-22", "venue": "Ortonville Corn Festival", "city": "Ortonville, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-08-28", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-08-29", "venue": "Hayloft Parking Lot Party", "city": "Luxemburg, MN", "time": "7:30pm\u201311:30pm", "band": "Pandemic", "url": ""},
        {"date": "2026-09-12", "venue": "South Brook Golf Course", "city": "Annandale, MN", "time": "5pm\u20139pm", "band": "Pandemic", "url": ""},
        {"date": "2026-09-19", "venue": "Omni Brewing", "city": "Maple Grove, MN", "time": "7pm\u20139:30pm", "band": "Pandemic", "url": ""},
        {"date": "2026-09-26", "venue": "Legends Bar and Grill", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-10-02", "venue": "Lemusique Room", "city": "Saint Michael, MN", "time": "7:30pm\u201310pm", "band": "Pandemic", "url": ""},
        {"date": "2026-10-03", "venue": "Pounders", "city": "Cologne, MN", "time": "8:30pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-10-24", "venue": "La Playette", "city": "Saint Joe, MN", "time": "8:30pm\u201312:30am", "band": "Pandemic", "url": ""},
        {"date": "2026-10-30", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-10-31", "venue": "Legends Bar and Grill (Halloween Party!)", "city": "Saint Cloud, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-11-27", "venue": "Rollies", "city": "Sauk Rapids, MN", "time": "8pm\u201312am", "band": "Pandemic", "url": ""},
        {"date": "2026-12-05", "venue": "Cuyuna Christmas", "city": "Crosby, MN", "time": "4pm\u20136pm", "band": "Pandemic", "url": ""},
    ],
}

# ───────────────────────────────────────────────────────────
# ABOUT — lives at /#about anchor on homepage
# ───────────────────────────────────────────────────────────
ABOUT = {
    "headline": "About",
    "body_paragraphs": [
        (
            "I grew up in Sauk Rapids, Minnesota. I started playing guitar at 13 after "
            "my dad took me to a Prince concert \u2014 watching Purple Rain live hooked me "
            "for good."
        ),
        (
            "Since then I\u2019ve played lead guitar across rock, alt-rock, tribute, and "
            "live-event work \u2014 from Minneapolis rooms to the Las Vegas strip. "
            "I\u2019ve shared stages with Breaking Benjamin, Steel Panther, Papa Roach, "
            "and more."
        ),
        (
            "Currently playing with Pandemic on the central Minnesota circuit "
            "and Taz & T-Bone as an acoustic duo."
        ),
    ],
}

# ───────────────────────────────────────────────────────────
# CONTACT — lives at /#contact anchor on homepage
# ───────────────────────────────────────────────────────────
CONTACT = {
    "headline": "Let\u2019s Work Together",
    "subheadline": "Booking, session work, or just want to connect \u2014 reach out.",
    "email": SITE["contact_email"],
}

# ───────────────────────────────────────────────────────────
# FOOTER
# ───────────────────────────────────────────────────────────
FOOTER = {
    "tagline": "Guitarist based in Minnesota.",
    "social_links": [
        {"platform": "Facebook", "url": "https://www.facebook.com/TylerAzure/", "icon": "facebook"},
        {"platform": "Instagram", "url": "https://www.instagram.com/azure_tyler/", "icon": "instagram"},
        {"platform": "TikTok", "url": "https://www.tiktok.com/@tyler_taz_azure", "icon": "tiktok"},
    ],
}
