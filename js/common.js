jQuery(function() {
  var windowWidth = $(window).width();
  var windowSm = 767;
  if (windowSm >= windowWidth) {
    var headerHeight = 90;
  } else {
    var headerHeight = 120;
  }
  var documentUrl = location.origin + location.pathname + location.search;
  jQuery(document).on('click', 'a[href*="#"]', function(event) {
    var anchor = event.currentTarget;
    var anchorUrl = anchor.protocol + '//' + anchor.host + anchor.pathname + anchor.search;
    if (documentUrl !== anchorUrl) {
      return true;
    }

    var speed = 500;
    var position = $(anchor.hash).offset().top - headerHeight;
    jQuery('body,html').animate({
      scrollTop: position
    }, speed, 'swing');
    event.preventDefault();
    return false;
  });
});

// ハンバーガーメニュー実装
const checkbox = document.getElementById('menubtn');
const navmenu = document.getElementById('navmenu');
function openMenu() {
  if (navmenu.className == '') {
    navmenu.classList.add('checked');
  } else {
    navmenu.classList.remove('checked');
  }
}
checkbox.addEventListener('click', openMenu);

function closeMenu() {
  if (navmenu.className == 'checked') {
    navmenu.classList.remove('checked');
  }
}
const main = document.querySelector('main');
const footer = document.querySelector('footer');
main.addEventListener('click', closeMenu);
footer.addEventListener('click', closeMenu);
