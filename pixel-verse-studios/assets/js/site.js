// The only script on the site: click a screenshot to see it big.
// Every screenshot in the pages is an <img data-lightbox="caption text">.

// Build the dark overlay once and hide it until someone clicks a screenshot.
var overlay = document.createElement('div');
overlay.className = 'lightbox';
overlay.setAttribute('role', 'dialog');
overlay.setAttribute('aria-modal', 'true');
overlay.setAttribute('aria-label', 'Image preview');
overlay.innerHTML =
  '<button class="lightbox-close" type="button" aria-label="Close image">&#10005;</button>' +
  '<figure class="lightbox-figure"><img alt="" /><figcaption></figcaption></figure>';
document.body.appendChild(overlay);

var bigImage = overlay.querySelector('img');
var caption = overlay.querySelector('figcaption');
var closeButton = overlay.querySelector('.lightbox-close');

// Remember what was clicked, so the keyboard focus goes back there when we close.
var clickedThing = null;

function open_lightbox(picture) {
  clickedThing = picture.closest('button') || picture;
  bigImage.src = picture.src;
  bigImage.alt = picture.alt;
  caption.textContent = picture.dataset.lightbox || picture.alt;
  overlay.classList.add('open');
  document.body.classList.add('lightbox-open');
  closeButton.focus();
}

function close_lightbox() {
  overlay.classList.remove('open');
  document.body.classList.remove('lightbox-open');
  if (clickedThing) clickedThing.focus();
}

document.addEventListener('click', function (event) {
  // Clicked inside the overlay: the close button or the dark background closes it,
  // but clicking the picture itself does not.
  if (event.target.closest('.lightbox')) {
    if (!event.target.closest('.lightbox-figure')) close_lightbox();
    return;
  }

  // Clicked a screenshot (or the button around it): open it.
  var button = event.target.closest('button');
  var picture = event.target.closest('img[data-lightbox]');
  if (!picture && button) picture = button.querySelector('img[data-lightbox]');
  if (picture) open_lightbox(picture);
});

// Escape closes it too.
document.addEventListener('keydown', function (event) {
  if (event.key === 'Escape' && overlay.classList.contains('open')) close_lightbox();
});
