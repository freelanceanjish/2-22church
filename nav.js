(function () {
  var hamburger = document.querySelector('.nav-hamburger');
  var mobileMenu = document.getElementById('mobile-menu');
  if (!hamburger || !mobileMenu) return;

  var mobileClose = mobileMenu.querySelector('.mobile-close');

  function setOpen(open) {
    hamburger.classList.toggle('open', open);
    mobileMenu.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }

  hamburger.addEventListener('click', function () {
    setOpen(!mobileMenu.classList.contains('open'));
  });

  if (mobileClose) {
    mobileClose.addEventListener('click', function () {
      setOpen(false);
    });
  }

  mobileMenu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      setOpen(false);
    });
  });

  document.addEventListener('click', function (e) {
    if (!mobileMenu.classList.contains('open')) return;
    if (!mobileMenu.contains(e.target) && !hamburger.contains(e.target)) {
      setOpen(false);
    }
  });
})();
