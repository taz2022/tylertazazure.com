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
        {"label": "About",   "href": "/#about"},
        {"label": "Music",   "href": "/music"},
        {"label": "Videos",  "href": "/videos"},
        {"label": "Shows",   "href": "/shows"},
    ],
    "right": [
        {"label": "Press",   "href": "/press"},
        {"label": "Gallery", "href": "/gallery"},
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
    "streaming": {
        "spotify_embed_url": "https://open.spotify.com/embed/artist/5rak7UsAIT3HqwMtXE5IFQ",
        "platforms": [
            {"name": "Spotify",       "url": "", "icon": "spotify"},       # TODO: fill in
            {"name": "Apple Music",   "url": "", "icon": "apple-music"},   # TODO: fill in
            {"name": "YouTube Music", "url": "", "icon": "youtube-music"}, # TODO: fill in
            {"name": "Amazon Music",  "url": "", "icon": "amazon-music"},  # TODO: fill in
        ],
    },
    "press_quotes": [
        {"quote": "", "source": "", "author": "", "url": ""},  # TODO: fill in
        {"quote": "", "source": "", "author": "", "url": ""},  # TODO: fill in
    ],
    "photo_strip": [
        "gallery/taz_live.jpg",
        "gallery/taz_CRR.jpg",
        "gallery/taz_hairball.jpg",
        "gallery/tazbenefit.jpg",
        "gallery/tazriver.jpg",
        "gallery/Taz&treybenefit.jpg",
    ],
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
            "gallery": [
                "music/bands/gallery/pandemic/preview.webp",
            ],
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
            "gallery": [
                "music/bands/gallery/code-red-riot/505777708_4024309347841809_7715807865004723605_n.jpg",
                "music/bands/gallery/code-red-riot/506016432_4024309127841831_8059111995896846116_n.jpg",
                "music/bands/gallery/code-red-riot/506020850_4024310144508396_1834922089331998896_n.jpg",
                "music/bands/gallery/code-red-riot/506031621_4024310097841734_7849437605715721410_n.jpg",
                "music/bands/gallery/code-red-riot/506044601_4024310451175032_7627880900340003804_n.jpg",
                "music/bands/gallery/code-red-riot/506139464_4024309331175144_3822868570484021526_n.jpg",
                "music/bands/gallery/code-red-riot/506304675_4024310191175058_4090827974887735242_n.jpg",
                "music/bands/gallery/code-red-riot/506306983_4024310511175026_6035343872043475420_n.jpg",
                "music/bands/gallery/code-red-riot/35121257_10155447714842611_6718863850780753920_n.jpg",
                "music/bands/gallery/code-red-riot/35225891_10155447712072611_3520799917637369856_n.jpg",
                "music/bands/gallery/code-red-riot/35226892_10155447712217611_2180349137180950528_n.jpg",
                "music/bands/gallery/code-red-riot/37114278_2130443827203953_6981752085935030272_n.jpg",
                "music/bands/gallery/code-red-riot/42549020_10155688262572611_5304401184562348032_n.jpg",
                "music/bands/gallery/code-red-riot/42649442_10155688262522611_8122381265291706368_n.jpg",
                "music/bands/gallery/code-red-riot/468665372_10162660583708453_4531454331984620010_n.jpg",
                "music/bands/gallery/code-red-riot/472064041_10170898577895727_558813032380923173_n.jpg",
                "music/bands/gallery/code-red-riot/472135450_10170884042205727_7737665537774350069_n.jpg",
                "music/bands/gallery/code-red-riot/taz_CRR.jpg",
                "music/bands/gallery/code-red-riot/coderedriot.jpg",
                "music/bands/gallery/code-red-riot/code red riot.jpg",
            ],
            "streaming": {
                "spotify_embed_url": "https://open.spotify.com/embed/album/0tNXIO6ME8rtFcRUIak0uV",
                "platforms": [
                    {"name": "Spotify",     "url": "https://open.spotify.com/album/0tNXIO6ME8rtFcRUIak0uV", "icon": "spotify"},
                    {"name": "Apple Music", "url": "", "icon": "apple-music"},   # TODO: fill in
                    {"name": "YouTube",     "url": "https://www.youtube.com/@coderedriot", "icon": "youtube"},  # TODO: confirm
                ],
            },
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
            "gallery": [
                "music/bands/gallery/hairball/119193857_10164487445105727_221552235811410408_n.jpg",
                "music/bands/gallery/hairball/34863416_1766961096673953_8437915882415456256_n.jpg",
                "music/bands/gallery/hairball/35489487_1290677257732268_1353844777702916096_n.jpg",
                "music/bands/gallery/hairball/40684140_10161118588950727_143010840314904576_n.jpg",
                "music/bands/gallery/hairball/46035964_1987192098026984_8104118179585851392_n.jpg",
                "music/bands/gallery/hairball/472267974_10170670695425274_7763462850468380618_n.jpg",
                "music/bands/gallery/hairball/472559185_10170926532830727_9063704705337378678_n.jpg",
                "music/bands/gallery/hairball/taz_hairball.jpg",
                "music/bands/gallery/hairball/preview (7).webp",
            ],
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
            "url_external": "https://lamadnessmusic.com/",
            "card_image": "music/bands/la madness.jpg",
            "featured": False,
            "gallery": [
                "music/bands/gallery/la-madness/472758715_10170964672090727_9038602632989929997_n.jpg",
                "music/bands/gallery/la-madness/la madness.jpg",
                "music/bands/gallery/la-madness/preview (6).webp",
            ],
            "streaming": {
                "spotify_embed_url": "https://open.spotify.com/embed/album/196mEUJI4c9tuLGvwm5WGs",
                "platforms": [
                    {"name": "Spotify", "url": "https://open.spotify.com/album/196mEUJI4c9tuLGvwm5WGs", "icon": "spotify"},
                ],
            },
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
            "gallery": [
                "music/bands/gallery/taz-and-t-bone/Taz&Tbone1.jpg",
            ],
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
            "gallery": [
                "music/bands/gallery/dirtee-circus/470214961_10170566029660727_6984243041806106190_n.jpg",
                "music/bands/gallery/dirtee-circus/472886551_10170954795720727_1439670497971905408_n.jpg",
                "music/bands/gallery/dirtee-circus/648812422_10174259783150727_8819566306982505118_n.jpg",
            ],
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
            "gallery": [
                "music/bands/gallery/almost-cooper/469899750_10236021580018505_6991603722219923685_n.jpg",
                "music/bands/gallery/almost-cooper/472685727_10170968705590727_1261297078651282226_n.jpg",
                "music/bands/gallery/almost-cooper/56835736_10218975146872358_3068247657563553792_n.jpg",
                "music/bands/gallery/almost-cooper/56968271_10218995695026049_4896611962705674240_n.jpg",
                "music/bands/gallery/almost-cooper/57052263_10157067863523187_4867868418063204352_n.jpg",
                "music/bands/gallery/almost-cooper/preview (8).webp",
            ],
        },
    ],
    "stages_shared": [
        "Breaking Benjamin", "Eagles of Death Metal", "Steel Panther", "Fozzy",
        "Papa Roach", "Fuel", "Tantric", "Gemini Syndrome",
        "Las Rageous Festival", "Whisky A Go Go", "House of Blues", "First Avenue",
    ],
    "gallery_images": [
        "music/gallery/preview.webp",
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
# GALLERY — /gallery page
# ───────────────────────────────────────────────────────────
GALLERY = {
    "hero": {
        "title": "Gallery",
        "subtitle": "Live photos",
    },
    "images": [
        "gallery/taz_live.jpg",
        "gallery/taz_live_2.jpg",
        "gallery/taz_CRR.jpg",
        "gallery/coderedriot.jpg",
        "gallery/taz_hairball.jpg",
        "gallery/tazbenefit.jpg",
        "gallery/tazriver.jpg",
        "gallery/Taz&Tbone1.jpg",
        "gallery/Taz&treybenefit.jpg",
        "music/gallery/preview.webp",
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
            "Tyler \u201cTaz\u201d Azure is a self-taught guitarist, songwriter, and performer "
            "from Sauk Rapids, Minnesota. He first picked up the guitar at age 13, "
            "inspired by the sound, style, and stage presence of artists like Prince, "
            "Slash, Joe Perry, and Jimmy Page. What started as a teenage obsession "
            "quickly became a lifelong pursuit, shaped by countless hours of learning "
            "by ear, chasing tone, and studying the players who made the guitar feel "
            "larger than life."
        ),
        (
            "At just 14 years old, Tyler found himself onstage for the first time "
            "during an impromptu jam in North Dakota. That moment lit the fuse. From "
            "there, he began forming bands, writing music, and playing shows across "
            "the Midwest, steadily building a reputation as a high-energy guitarist "
            "with a natural feel for rock, blues, and live performance."
        ),
        (
            "In 2016, Tyler moved to Las Vegas to join drummer Corky Gainsford in the "
            "original rock band Code Red Riot. The band signed with Sony Red and toured "
            "nationally, giving Tyler the chance to perform across the country and "
            "sharpen his craft on bigger stages. During that time, he continued to grow "
            "as both a performer and songwriter, blending raw rock influence with a "
            "modern, hard-hitting edge."
        ),
        (
            "Over the years, Tyler has performed with and filled in for a wide range "
            "of acts, from original projects to major tribute and cover bands. His "
            "experience includes playing with bands such as Dirtee Circus, Hairball, "
            "Code Red Riot, La Madness, Almost Cooper, and Pandemic. Whether stepping "
            "into a high-pressure fill-in role or leading a project of his own, Tyler "
            "brings preparation, grit, instinct, and stage presence to every performance."
        ),
        (
            "His playing blends classic rock swagger, blues-based phrasing, melodic "
            "leads, and a stage-first approach built from years of live experience. "
            "While his influences can be heard in the fire of his solos and the attitude "
            "of his rhythm playing, Tyler has developed a voice of his own: loud, "
            "melodic, restless, and built for the stage."
        ),
        (
            "Today, Tyler continues to write, record, and perform throughout Minnesota "
            "and the Midwest, playing solo acoustic shows, duo performances, full-band "
            "gigs, tribute acts, and fill-in guitar work. Whether performing in an "
            "intimate acoustic room or on a full-scale rock stage, Tyler brings the "
            "same fire, feel, and commitment to every show."
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
    "copyright": "Tyler Azure",
    "tagline": "Guitarist based in Minnesota.",
    "social_links": [
        {"platform": "Facebook", "url": "https://www.facebook.com/TylerAzure/", "icon": "facebook"},
        {"platform": "Instagram", "url": "https://www.instagram.com/azure_tyler/", "icon": "instagram"},
        {"platform": "TikTok", "url": "https://www.tiktok.com/@tyler_taz_azure", "icon": "tiktok"},
    ],
}
