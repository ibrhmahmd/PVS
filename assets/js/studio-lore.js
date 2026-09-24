// Studio & Lore: contact form feedback only.
(function () {
  var form = document.getElementById('transmission-form');
  var feedback = document.getElementById('form-feedback');
  if (!form || !feedback) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    feedback.classList.remove('hidden');
    feedback.textContent = 'Message received — we will get back to you.';
    var submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sent';
    }
    setTimeout(function () {
      form.reset();
      feedback.classList.add('hidden');
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Send Message';
      }
    }, 4500);
  });
})();