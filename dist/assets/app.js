(function () {
  'use strict';
  var doc = document;
  doc.documentElement.classList.add('js');

  // ---- analytics: dataLayer only; no wallet addresses, card data or amounts are ever collected ----
  window.dataLayer = window.dataLayer || [];
  function track(name, params) {
    var payload = { event: name };
    for (var k in params) payload[k] = params[k];
    window.dataLayer.push(payload);
  }

  // ---- CTA clicks ----
  doc.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-cta]') : null;
    if (el) track('cta_click', { location: el.getAttribute('data-cta'), target: 'changenow' });
  });

  // ---- FAQ accordion (all text is in the HTML; JS only collapses it) ----
  var buttons = doc.querySelectorAll('.faq-q');
  function setOpen(btn, open) {
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    var panel = doc.getElementById(btn.getAttribute('aria-controls'));
    if (panel) panel.hidden = !open;
  }
  Array.prototype.forEach.call(buttons, function (btn, i) {
    setOpen(btn, i === 0);
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      setOpen(btn, open);
      if (open) track('faq_open', { question: btn.textContent.trim() });
    });
  });

  // ---- one-time view events ----
  if ('IntersectionObserver' in window) {
    var once = function (selector, threshold, eventName) {
      var node = doc.querySelector(selector);
      if (!node) return;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { track(eventName, {}); io.disconnect(); }
        });
      }, { threshold: threshold });
      io.observe(node);
    };
    once('[data-track="comparison"]', 0.5, 'comparison_view');
    once('#methodology', 0.15, 'methodology_view');
  }

  // ---- mobile sticky CTA: shown once the hero CTA has scrolled above the viewport;
  // hidden while the FAQ, the final CTA or the footer is on screen. Position-based, so anchor jumps work too. ----
  var sticky = doc.getElementById('sticky-cta');
  var heroCta = doc.querySelector('.hero-cta');
  if (sticky && heroCta) {
    var stickyLink = sticky.querySelector('a');
    var guards = [doc.getElementById('faq'), doc.querySelector('.sec-final'), doc.querySelector('.site-footer')];
    var updateSticky = function () {
      var vh = window.innerHeight || doc.documentElement.clientHeight;
      var passed = heroCta.getBoundingClientRect().bottom < 0;
      var blocked = guards.some(function (n) {
        if (!n) return false;
        var r = n.getBoundingClientRect();
        return r.top < vh && r.bottom > 0;
      });
      var show = passed && !blocked;
      sticky.classList.toggle('show', show);
      sticky.setAttribute('aria-hidden', show ? 'false' : 'true');
      if (stickyLink) stickyLink.tabIndex = show ? 0 : -1;
    };
    window.addEventListener('scroll', updateSticky, { passive: true });
    window.addEventListener('resize', updateSticky);
    updateSticky();
  }

  // ---- scroll depth 25/50/75/90 ----
  var marks = [25, 50, 75, 90];
  var sent = {};
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      ticking = false;
      var h = doc.documentElement;
      var total = h.scrollHeight - h.clientHeight;
      if (total <= 0) return;
      var pct = (window.pageYOffset / total) * 100;
      marks.forEach(function (m) {
        if (pct >= m && !sent[m]) { sent[m] = true; track('scroll_depth', { percent: m }); }
      });
    });
  }, { passive: true });

  // ---- close mobile menu after choosing a link ----
  var menu = doc.querySelector('.menu');
  if (menu) {
    menu.addEventListener('click', function (ev) {
      if (ev.target.closest && ev.target.closest('a')) menu.removeAttribute('open');
    });
  }
})();
