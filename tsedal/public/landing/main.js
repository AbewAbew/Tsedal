/** Tsedal landing interactions. Navigation works without JavaScript. */
(() => {
  'use strict';
  const language = document.documentElement.lang;
  document.querySelectorAll('[data-language]').forEach(link => {
    if (link.dataset.language === language) link.setAttribute('aria-current', 'page');
  });
  document.querySelectorAll('.focus-row-item').forEach(row => {
    row.addEventListener('pointerenter', () => row.classList.add('active'));
    row.addEventListener('pointerleave', () => row.classList.remove('active'));
  });
})();
