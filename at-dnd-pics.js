/* Active Transport: pictures on drag-and-drop game items.
   Shared file, copied into each site by C:/study-tools/_shared/sync_static.py; do not edit a site's copy.
   The page's <script src="at-dnd-pics.js" data-pics='{"Item name":"pic_img/x.jpg"}'> lists the items
   that have a vetted picture. Each matching item box (.drug-card) gets a thumbnail above its name;
   tapping it opens the full picture. Game data, drag-and-drop and scoring are not touched. */
(function () {
  var me = document.currentScript;
  var pics = {};
  try { pics = JSON.parse(me.getAttribute('data-pics') || '{}'); } catch (e) { return; }
  var keys = {};
  Object.keys(pics).forEach(function (k) { keys[norm(k)] = pics[k]; });
  if (!Object.keys(keys).length) return;

  function norm(s) { return String(s).replace(/\s+/g, ' ').trim(); }

  var css = [
    '.drug-card .at-pic{display:block;box-sizing:border-box;width:100%;max-width:100%;margin:0 0 12px;padding:0;',
    'border:1px solid rgba(255,255,255,.16);border-radius:8px;background:#05080f;cursor:zoom-in;overflow:hidden;',
    'position:relative;font:inherit;color:inherit;-webkit-tap-highlight-color:transparent}',
    '.drug-card .at-pic img{display:block;width:100%;height:180px;object-fit:contain;-webkit-user-drag:none;',
    'user-select:none;-webkit-user-select:none;pointer-events:none}',
    '.drug-card .at-pic:focus-visible{outline:2px solid #22d3ee;outline-offset:2px}',
    '.drug-card .at-pic .at-pic-zoom{position:absolute;right:6px;bottom:6px;width:30px;height:30px;border-radius:8px;',
    'background:rgba(2,6,23,.72);display:flex;align-items:center;justify-content:center;pointer-events:none}',
    '.drug-card .at-pic .at-pic-zoom svg{width:16px;height:16px;stroke:#e2e8f0}',
    '@media (max-width:640px){.drug-card .at-pic img{height:150px}}',
    '.at-pic-lb{position:fixed;inset:0;z-index:2147483000;background:rgba(2,6,23,.94);display:flex;',
    'flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:56px 16px 20px;box-sizing:border-box}',
    '.at-pic-lb[hidden]{display:none}',
    '.at-pic-lb img{display:block;max-width:100%;max-height:calc(100vh - 130px);max-height:calc(100dvh - 130px);',
    'object-fit:contain;border-radius:8px;background:#fff}',
    '.at-pic-lb-cap{color:#e2e8f0;font:600 15px/1.4 Inter,system-ui,sans-serif;text-align:center;max-width:900px;',
    'overflow-wrap:anywhere}',
    '.at-pic-lb-x{position:absolute;top:10px;right:10px;width:44px;height:44px;border-radius:12px;border:1px solid ',
    'rgba(255,255,255,.25);background:rgba(15,23,42,.9);color:#f8fafc;font:600 24px/1 system-ui,sans-serif;cursor:pointer}'
  ].join('');
  var st = document.createElement('style');
  st.setAttribute('data-at-dnd-pics', '');
  st.textContent = css;
  document.head.appendChild(st);

  var ZOOM = '<span class="at-pic-zoom" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M11 8v6M8 11h6"/></svg></span>';

  var lb, lbImg, lbCap, lastFocus;
  function openLb(src, name) {
    if (!lb) {
      lb = document.createElement('div');
      lb.className = 'at-pic-lb';
      lb.setAttribute('role', 'dialog');
      lb.setAttribute('aria-modal', 'true');
      lb.hidden = true;
      lb.innerHTML = '<button type="button" class="at-pic-lb-x" aria-label="Close picture">&times;</button>' +
        '<img alt=""><div class="at-pic-lb-cap"></div>';
      lbImg = lb.querySelector('img');
      lbCap = lb.querySelector('.at-pic-lb-cap');
      lb.addEventListener('click', function (e) { if (e.target !== lbImg) closeLb(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !lb.hidden) closeLb(); });
      document.body.appendChild(lb);
    }
    lastFocus = document.activeElement;
    lbImg.src = src;
    lbImg.alt = name;
    lbCap.textContent = name;
    lb.setAttribute('aria-label', name);
    lb.hidden = false;
    lb.querySelector('.at-pic-lb-x').focus();
  }
  function closeLb() {
    lb.hidden = true;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function decorate(root) {
    var cards = (root || document).querySelectorAll('.drug-card');
    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      if (card.querySelector(':scope > .at-pic')) continue;
      var t = card.querySelector('.drug-card-title');
      if (!t) continue;
      var name = norm(t.textContent);
      var src = keys[name];
      if (!src) continue;
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'at-pic';
      b.setAttribute('aria-label', 'Enlarge picture: ' + name);
      b.innerHTML = '<img decoding="async" draggable="false" alt="">' + ZOOM;
      var img = b.querySelector('img');
      img.src = src;
      img.alt = name;
      b.addEventListener('click', (function (s, n) { return function () { openLb(s, n); }; })(src, name));
      card.insertBefore(b, t);
    }
  }

  function start() {
    decorate(document);
    var box = document.getElementById('cards-container') || document.body;
    new MutationObserver(function () { decorate(box); }).observe(box, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
