/* ============================================================
   Tyler Azure — main.js
   Vanilla JS only. No dependencies.
   ============================================================ */

'use strict';

// ── Navbar: scroll state + active link ─────────────────────
(function initNavbar() {
  const navbar  = document.getElementById('navbar');
  const links   = document.querySelectorAll('.navbar__link');
  const sections = document.querySelectorAll('section[id]');

  if (!navbar) return;

  function onScroll() {
    // Scrolled state
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Active link highlighting
    let current = '';
    sections.forEach(section => {
      const top = section.offsetTop - 96;
      if (window.scrollY >= top) {
        current = section.getAttribute('id');
      }
    });

    links.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // run once on load
})();

// ── Mobile Menu ─────────────────────────────────────────────
(function initMobileMenu() {
  const toggle     = document.getElementById('navToggle');
  const menu       = document.getElementById('mobileMenu');
  const menuLinks  = document.querySelectorAll('.mobile-menu__link, .mobile-menu__cta');

  if (!toggle || !menu) return;

  function openMenu() {
    toggle.classList.add('open');
    menu.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    menu.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    toggle.classList.remove('open');
    menu.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', () => {
    if (menu.classList.contains('open')) closeMenu();
    else openMenu();
  });

  menuLinks.forEach(link => link.addEventListener('click', closeMenu));

  // Close on Escape
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && menu.classList.contains('open')) closeMenu();
  });
})();

// ── Scroll Reveal (Intersection Observer) ──────────────────
(function initScrollReveal() {
  const elements = document.querySelectorAll('.scroll-reveal');
  if (!elements.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger children slightly
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, i * 60);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  elements.forEach(el => observer.observe(el));
})();

// ── Project Category Filter ─────────────────────────────────
(function initProjectFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards      = document.querySelectorAll('.project-card');

  if (!filterBtns.length || !cards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      // Update active state
      filterBtns.forEach(b => {
        b.classList.remove('filter-btn--active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('filter-btn--active');
      btn.setAttribute('aria-pressed', 'true');

      // Filter cards
      cards.forEach(card => {
        const category = card.dataset.category;
        if (filter === 'All' || category === filter) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
})();

// ── Contact Form ────────────────────────────────────────────
(function initContactForm() {
  const submitBtn  = document.getElementById('contactSubmit');
  const formWrap   = document.getElementById('contactFormWrap');
  const successEl  = document.getElementById('formSuccess');
  const errorEl    = document.getElementById('formError');

  if (!submitBtn) return;

  function getField(name) {
    const el = document.querySelector(`[name="${name}"]`);
    return el ? el.value.trim() : '';
  }

  function showMessage(el, message) {
    el.textContent = message || el.textContent;
    el.hidden = false;
  }

  function hideMessages() {
    successEl.hidden = true;
    errorEl.hidden   = true;
  }

  submitBtn.addEventListener('click', async () => {
    hideMessages();

    const name    = getField('name');
    const email   = getField('email');
    const subject = getField('subject');
    const message = getField('message');

    // Basic client-side validation
    if (!name || !email || !message) {
      showMessage(errorEl, 'Please fill in your name, email, and message.');
      return;
    }

    submitBtn.disabled    = true;
    submitBtn.textContent = 'Sending…';

    try {
      const response = await fetch('/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, subject, message }),
      });

      const data = await response.json();

      if (data.success) {
        formWrap.style.display = 'none';
        showMessage(successEl, data.message);
        successEl.focus();
      } else {
        showMessage(errorEl, data.error || 'Something went wrong. Please try again.');
        submitBtn.disabled    = false;
        submitBtn.textContent = 'Send Message';
      }
    } catch (err) {
      showMessage(errorEl, 'Network error. Please email directly or try again.');
      submitBtn.disabled    = false;
      submitBtn.textContent = 'Send Message';
    }
  });
})();

// ── Smooth scroll for anchor links ─────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
