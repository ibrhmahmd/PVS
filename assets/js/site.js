// Shared site script — mobile menu, footer newsletter, and screenshot lightbox. Identical on all four pages.
(function () {
  var menuBtn = document.getElementById('mobile-menu-btn');
  var menuIcon = document.getElementById('mobile-menu-icon');
  var mobileNav = document.getElementById('mobile-nav');
  if (!menuBtn || !menuIcon || !mobileNav) return;
  function setMenu(open) {
    mobileNav.classList.toggle('hidden', !open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menuIcon.textContent = open ? 'close' : 'menu';
  }
  menuBtn.addEventListener('click', function () {
    setMenu(mobileNav.classList.contains('hidden'));
  });
  mobileNav.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setMenu(false);
  });
})();

(function () {
  var form = document.getElementById('newsletter-form');
  var confirmation = document.getElementById('newsletter-confirmation');
  if (!form || !confirmation) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    form.classList.add('hidden');
    confirmation.classList.remove('hidden');
  });
})();

// Click-to-enlarge lightbox for every img[data-lightbox].
(function () {
  if (!document.querySelector('img[data-lightbox]')) return;

  var overlay = document.createElement('div');
  overlay.className = 'lightbox';
  overlay.setAttribute('aria-label', 'Image preview');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('role', 'dialog');
  overlay.innerHTML =
    '<button class="lightbox-close" type="button" aria-label="Close image">&#10005;</button>' +
    '<figure class="lightbox-figure">' +
    '<img alt="" />' +
    '<figcaption></figcaption>' +
    '</figure>';
  document.body.appendChild(overlay);

  var overlayImg = overlay.querySelector('img');
  var caption = overlay.querySelector('figcaption');
  var closeBtn = overlay.querySelector('.lightbox-close');
  var lastFocus = null;

  function openLightbox(trigger) {
    lastFocus = trigger.closest('button') || trigger;
    overlayImg.src = trigger.src;
    overlayImg.alt = trigger.alt;
    caption.textContent = trigger.dataset.lightbox || trigger.alt;
    overlay.classList.add('open');
    document.body.classList.add('lightbox-open');
    closeBtn.focus();
  }

  function closeLightbox() {
    if (!overlay.classList.contains('open')) return;
    overlay.classList.remove('open');
    document.body.classList.remove('lightbox-open');
    if (lastFocus) lastFocus.focus();
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    var trigger = e.target.closest('img[data-lightbox]') || (btn && btn.querySelector('img[data-lightbox]'));
    if (trigger && !e.target.closest('.lightbox')) {
      e.preventDefault();
      openLightbox(trigger);
      return;
    }
    if (e.target.closest('.lightbox') && !e.target.closest('.lightbox-figure')) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLightbox();
  });
})();