(function () {
  if (document.getElementById('diagram-lightbox')) return;

  var box = document.createElement('div');
  box.id = 'diagram-lightbox';
  box.className = 'diagram-lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Enlarged diagram');
  box.innerHTML = '<button type="button" class="diagram-lightbox-close" aria-label="Close">&times;</button><img alt="">';
  document.body.appendChild(box);

  var img = box.querySelector('img');
  var closeBtn = box.querySelector('.diagram-lightbox-close');

  function open(src, alt) {
    img.src = src;
    img.alt = alt || '';
    box.classList.add('open');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  function close() {
    box.classList.remove('open');
    img.removeAttribute('src');
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', close);
  box.addEventListener('click', function (e) {
    if (e.target === box || e.target === img) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && box.classList.contains('open')) close();
  });

  document.querySelectorAll('.diagram-block img').forEach(function (diagram) {
    diagram.setAttribute('tabindex', '0');
    diagram.setAttribute('role', 'button');
    diagram.setAttribute('aria-label', (diagram.alt || 'Diagram') + '. Click to enlarge.');

    function zoom() {
      open(diagram.currentSrc || diagram.src, diagram.alt);
    }

    diagram.addEventListener('click', zoom);
    diagram.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        zoom();
      }
    });

    var hint = document.createElement('span');
    hint.className = 'diagram-zoom-hint';
    hint.textContent = 'Click to view full size';
    diagram.parentNode.appendChild(hint);
  });
})();
