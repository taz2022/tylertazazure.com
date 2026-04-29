# Navbar Redesign Spec — v2 (corrected)

**Goal:** Fix the current navbar which has three visible problems in the live preview:

1. The logo image has a black rectangular background baked into the PNG, making it look like a "billboard" floating above the nav instead of a logo mark.
2. The logo is rendering at roughly 300px tall — way larger than the navbar itself — because nothing in CSS is constraining its height.
3. Nav links are still title-case with default spacing, which reads as a generic template nav.

**Scope:** `app/templates/partials/navbar.html`, the navbar section of `app/static/css/styles.css`, and small checks in `main.js` and `base.html`. Do **not** modify the hero or any other section — those look fine and stay as-is.

---

## Pre-flight audit (do this first)

Before making any edits, scan the existing codebase for CSS rules that could override the new navbar styles:

```bash
grep -n "img\s*{" app/static/css/styles.css
grep -n ".navbar" app/static/css/styles.css
grep -n "\.navbar__" app/static/css/styles.css
```

**What to look for:**

- Any global `img { width: 100%; }` or `img { max-width: 100%; height: auto; }` rules — these will override logo sizing if the logo selector isn't specific enough.
- Any **existing `.navbar` rules** that weren't removed in a prior redesign attempt. If found, the old rules need to be fully removed, not layered on top of the new ones.
- Any `.navbar__logo` rule without an explicit height. That's why the logo is blowing out to 300px — the image is rendering at its natural pixel dimensions.

**Report what was found** before proceeding to Task 2, so I (Tyler) know what conflicts existed.

---

## Task 1 — Replace `app/templates/partials/navbar.html`

Full file replacement. Do not merge — overwrite.

```html
<header class="navbar" id="navbar" role="banner">
  <div class="navbar__inner">

    <!-- Left nav -->
    <nav class="navbar__group navbar__group--left" aria-label="Primary navigation (left)">
      <ul class="navbar__links" role="list">
        <li><a href="#about"    class="navbar__link">About</a></li>
        <li><a href="#music"    class="navbar__link">Music</a></li>
        <li><a href="#press"    class="navbar__link">Press</a></li>
      </ul>
    </nav>

    <!-- Center logo -->
    <a href="/" class="navbar__brand" aria-label="Tyler Azure — Home">
      <img
        src="{{ url_for('static', filename='images/logo.png') }}"
        alt="Tyler Azure"
        class="navbar__logo"
      />
    </a>

    <!-- Right nav -->
    <nav class="navbar__group navbar__group--right" aria-label="Primary navigation (right)">
      <ul class="navbar__links" role="list">
        <li><a href="#projects" class="navbar__link">Projects</a></li>
        <li><a href="#museum"   class="navbar__link">Museum</a></li>
        <li><a href="#contact"  class="navbar__link">Contact</a></li>
      </ul>
    </nav>

    <!-- Mobile hamburger -->
    <button
      class="navbar__toggle"
      id="navToggle"
      aria-label="Toggle navigation"
      aria-expanded="false"
      aria-controls="mobileMenu"
    >
      <span></span><span></span><span></span>
    </button>
  </div>

  <!-- Mobile menu -->
  <div class="mobile-menu" id="mobileMenu" aria-hidden="true">
    <nav aria-label="Mobile navigation">
      <ul class="mobile-menu__links" role="list">
        <li><a href="#about"    class="mobile-menu__link">About</a></li>
        <li><a href="#music"    class="mobile-menu__link">Music</a></li>
        <li><a href="#press"    class="mobile-menu__link">Press</a></li>
        <li><a href="#projects" class="mobile-menu__link">Projects</a></li>
        <li><a href="#museum"   class="mobile-menu__link">Museum</a></li>
        <li><a href="#contact"  class="mobile-menu__link">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
```

**Note:** "Journey" was replaced by "Press" to match the main site upgrade spec. If the Press section hasn't been built yet, leave the Press link in place — it'll fall through to a broken anchor harmlessly until that section exists.

---

## Task 2 — Replace the navbar CSS block in `styles.css`

**Process:** Locate any existing block starting with something like `/* ── Navbar ── */` or `.navbar {` and delete the **entire block** down through the last navbar/mobile-menu media query. Then paste the block below in its place. If the audit in the pre-flight step found multiple navbar blocks scattered around the file, remove all of them.

```css
/* ─────────────────────────────────────────────────────────── */
/* NAVBAR v2 — center logo with mix-blend-mode, tight proportions */
/* ─────────────────────────────────────────────────────────── */

:root {
  --navbar-h: 104px;
  --navbar-h-scrolled: 72px;
  --navbar-logo-h: 68px;
  --navbar-logo-h-scrolled: 44px;
}

.navbar {
  position: fixed;
  inset: 0 0 auto 0;
  z-index: 100;
  height: var(--navbar-h);
  background: rgba(13, 17, 23, 0.0); /* start transparent */
  transition:
    height var(--duration, 0.3s) var(--ease, ease),
    background var(--duration, 0.3s) var(--ease, ease),
    backdrop-filter var(--duration, 0.3s) var(--ease, ease),
    border-color var(--duration, 0.3s) var(--ease, ease);
  border-bottom: 1px solid transparent;
}

.navbar.scrolled {
  height: var(--navbar-h-scrolled);
  background: rgba(13, 17, 23, 0.88);
  backdrop-filter: blur(24px) saturate(1.2);
  -webkit-backdrop-filter: blur(24px) saturate(1.2);
  border-bottom-color: var(--color-border);
}

/* Inner container — single flex row with logo as an inline item */
.navbar__inner {
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 clamp(1rem, 3vw, 2.5rem);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(1rem, 3vw, 2.5rem);
}

/* Nav groups — flex to fill sides, contents pulled toward the logo */
.navbar__group {
  flex: 1 1 0;
  display: flex;
  align-items: center;
  min-width: 0;
}

.navbar__group--left  { justify-content: flex-end; }
.navbar__group--right { justify-content: flex-start; }

/* Link list */
.navbar__links {
  display: flex;
  align-items: center;
  gap: clamp(1rem, 2.2vw, 2.25rem);
  margin: 0;
  padding: 0;
  list-style: none;
}

/* Link styling — uppercase, letterspaced, small */
.navbar__link {
  font-family: var(--font-sans, 'Outfit', sans-serif);
  font-size: 0.78rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--color-text-muted, #9ba3af);
  text-decoration: none;
  padding: 0.5rem 0;
  position: relative;
  white-space: nowrap;
  transition: color var(--duration, 0.3s) var(--ease, ease);
}

.navbar__link:hover,
.navbar__link.active {
  color: var(--color-text, #f3f4f6);
}

/* Underline that animates from center */
.navbar__link::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -2px;
  width: 0;
  height: 1px;
  background: var(--color-accent, #1e7ed4);
  transition: width var(--duration, 0.3s) var(--ease, ease),
              left var(--duration, 0.3s) var(--ease, ease);
}

.navbar__link:hover::after,
.navbar__link.active::after {
  width: 100%;
  left: 0;
}

/* Brand — logo wrapper, fixed width so it doesn't flex */
.navbar__brand {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  line-height: 0; /* prevents inline baseline gap below image */
  transition: opacity var(--duration, 0.3s) var(--ease, ease),
              transform var(--duration, 0.3s) var(--ease, ease);
}

.navbar__brand:hover { opacity: 0.92; }
.navbar__brand:active { transform: scale(0.98); }

/* Logo — STRICTLY CONSTRAINED so no global img rule can blow it out */
.navbar__logo,
.navbar img.navbar__logo {
  display: block;
  height: var(--navbar-logo-h);
  max-height: var(--navbar-logo-h);
  width: auto;
  max-width: clamp(140px, 22vw, 260px);
  object-fit: contain;

  /* KEY TRICK: screen blend mode makes the logo's black background
     blend into the dark navbar, effectively turning black pixels
     transparent. Works because the navbar sits over dark content.
     Remove this line once the logo PNG has true transparency. */
  mix-blend-mode: screen;

  /* Keeps highlights looking crisp against the navbar's scroll-state background */
  filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.3));

  transition:
    height var(--duration, 0.3s) var(--ease, ease),
    filter var(--duration, 0.3s) var(--ease, ease);
}

.navbar.scrolled .navbar__logo {
  height: var(--navbar-logo-h-scrolled);
  max-height: var(--navbar-logo-h-scrolled);
}

.navbar__brand:hover .navbar__logo {
  filter: drop-shadow(0 2px 14px rgba(30, 126, 212, 0.5));
}

/* ── Mobile hamburger ──────────────────────────────────────── */
.navbar__toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: 0.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.navbar__toggle:hover { background: rgba(255, 255, 255, 0.06); }

.navbar__toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--color-text, #f3f4f6);
  border-radius: 2px;
  transition: transform var(--duration, 0.3s) var(--ease, ease),
              opacity var(--duration, 0.3s);
}

.navbar__toggle.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.navbar__toggle.open span:nth-child(2) { opacity: 0; }
.navbar__toggle.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* ── Mobile menu ───────────────────────────────────────────── */
.mobile-menu {
  position: absolute;
  top: var(--navbar-h);
  left: 0;
  right: 0;
  background: rgba(13, 17, 23, 0.97);
  backdrop-filter: blur(24px);
  border-bottom: 1px solid var(--color-border, #1f2937);
  padding: 2rem clamp(1rem, 3vw, 2rem);
  display: none;
}

.navbar.scrolled .mobile-menu { top: var(--navbar-h-scrolled); }

.mobile-menu.open {
  display: block;
  animation: menuSlide 0.28s ease;
}

@keyframes menuSlide {
  from { opacity: 0; transform: translateY(-10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.mobile-menu__links {
  display: flex;
  flex-direction: column;
  gap: 0;
  list-style: none;
  margin: 0;
  padding: 0;
}

.mobile-menu__link {
  display: block;
  padding: 1.1rem 0;
  font-family: var(--font-sans, 'Outfit', sans-serif);
  font-size: 1.05rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--color-text-muted, #9ba3af);
  text-decoration: none;
  border-bottom: 1px solid var(--color-border, #1f2937);
  transition: color var(--duration, 0.3s) ease,
              padding-left var(--duration, 0.3s) ease;
}

.mobile-menu__link:hover {
  color: var(--color-accent, #1e7ed4);
  padding-left: 0.5rem;
}

.mobile-menu__link:last-child { border-bottom: none; }

/* ── Responsive ────────────────────────────────────────────── */
@media (max-width: 900px) {
  :root {
    --navbar-h: 76px;
    --navbar-h-scrolled: 60px;
    --navbar-logo-h: 46px;
    --navbar-logo-h-scrolled: 34px;
  }

  .navbar__group { display: none; }

  .navbar__inner {
    justify-content: space-between;
    padding: 0 1rem;
  }

  .navbar__brand {
    flex: 1;
    justify-content: center;
  }

  .navbar__toggle { display: flex; }

  /* Visual counterweight to the hamburger so the logo reads centered */
  .navbar__inner::before {
    content: "";
    flex: 0 0 40px;
  }
}
```

**Why `mix-blend-mode: screen` works:**

Screen blend mode combines each pixel with what's behind it using the inverse-multiply formula. The practical result: **pure black pixels become fully transparent**, while colored/light pixels composite on top. Your logo has a black background and bright chrome/blue/gold artwork — screen mode will drop the black and keep everything else visible. The navbar sits over dark content (hero background and scrolled dark navbar), so the math works out cleanly in both states.

The tradeoff: screen mode is only correct when the backdrop is dark. If Tyler ever puts the logo on a light background, the blend will look wrong — so when he gets a properly transparent PNG, just delete the `mix-blend-mode: screen;` line and everything else stays the same.

---

## Task 3 — Verify `main.js` has scroll-state and toggle wiring

Open `app/static/js/main.js`. Search for `'scrolled'` and `'navToggle'`. If either is missing, add:

```javascript
// Navbar scroll state
(function () {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const onScroll = () => {
    if (window.scrollY > 40) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// Mobile menu toggle
(function () {
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('mobileMenu');
  if (!toggle || !menu) return;

  const setOpen = (open) => {
    menu.classList.toggle('open', open);
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-hidden', String(!open));
  };

  toggle.addEventListener('click', () => {
    setOpen(!menu.classList.contains('open'));
  });

  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => setOpen(false));
  });
})();
```

If both blocks already exist and are functional, leave them alone.

---

## Task 4 — Check `base.html` for navbar offset

Search `app/templates/base.html` (or wherever the `<main>` wrapper lives) and confirm the content does not sit under the fixed navbar. One of these needs to be true:

- **Option A (content starts below navbar):** `<main>` has `padding-top: var(--navbar-h);` or equivalent.
- **Option B (hero bleeds under navbar):** The first section (hero) has enough top padding of its own so nothing important sits under the nav.

**Current screenshots suggest Option B is active.** The hero looks fine with the title/tagline positioned well clear of the nav. Leave as-is unless something visually shifts.

---

## Task 5 — Specificity sanity check

After applying all changes, run:

```bash
grep -n "img" app/static/css/styles.css | head -30
```

If you find any rule like `img { width: 100%; height: auto; }` that's higher up in the file than the navbar block, the navbar's `.navbar__logo` rule will still win **because of the combined selector** (`.navbar img.navbar__logo`) — but if you see anything that looks like `body img { ... }` or `.container img { ... }` that could fight specificity, flag it for Tyler to review.

---

## Testing checklist

Run `python app.py` and open `http://localhost:5000/`. Verify:

1. **Logo no longer has a black rectangle around it** — the black should blend invisibly into the navbar area.
2. Logo is ~68px tall at the top of the page (not 300px). Proportional to the nav text.
3. Nav links read as uppercase, letterspaced (ABOUT · MUSIC · PRESS — not About Music Press).
4. Links have a thin blue underline that animates from the center on hover.
5. Scroll down 50px — navbar shrinks smoothly, gains a blurred dark background, logo scales to 44px.
6. Scroll back up — navbar expands and fades background back to transparent.
7. Resize to <900px — desktop nav disappears, hamburger appears on the right, logo centers.
8. Tap hamburger → mobile menu slides down with uppercase letterspaced links.
9. Tap a mobile link → menu closes.
10. Keyboard Tab navigation reaches each link; focus ring visible on each.
11. Zero horizontal scroll at any viewport width between 320px and 1920px.

---

## Optional fallback — text wordmark if the logo still feels too heavy

If the logo image still visually dominates even after the blend-mode fix, Tyler may want to swap it temporarily for a clean text wordmark. To do that, replace the `<a class="navbar__brand">` block in `navbar.html` with:

```html
<a href="/" class="navbar__brand navbar__brand--text" aria-label="Tyler Azure — Home">
  <span class="navbar__wordmark">Tyler<span class="navbar__wordmark-accent">Azure</span></span>
</a>
```

And add this CSS at the bottom of the navbar block:

```css
.navbar__wordmark {
  font-family: var(--font-serif, 'Cormorant Garamond', serif);
  font-size: 1.75rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: var(--color-text, #f3f4f6);
  line-height: 1;
}

.navbar__wordmark-accent {
  color: var(--color-accent, #1e7ed4);
  margin-left: 0.3em;
  font-style: italic;
}

.navbar.scrolled .navbar__wordmark {
  font-size: 1.35rem;
}
```

This keeps all the layout logic identical — only the center element changes. Tyler can switch back to the image logo at any time by reverting that single block.
