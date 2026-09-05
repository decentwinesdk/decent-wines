/* Decent Wines — mobilmenu + nyhedsbrev (Brevo) */
(function () {
  // Mobilmenu
  var burger = document.querySelector('.burger');
  var links = document.querySelector('.nav-links');
  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  // Kontaktformular — sender til Web3Forms, men brugeren bliver paa siden.
  // Gaar det galt, falder vi tilbage til almindelig afsendelse, og saa sender
  // Web3Forms folk tilbage hertil med ?sendt=1, som vi kvitterer for nedenfor.
  document.querySelectorAll('.kontakt-form').forEach(function (form) {
    var box = form.parentElement.querySelector('.form-ok');
    var btn = form.querySelector('button[type="submit"]');
    var btnText = btn ? btn.textContent : '';

    function kvitter() {
      if (!box) return;
      box.textContent = 'Tak. Beskeden er sendt, og vi vender tilbage.';
      box.classList.remove('error');
      box.classList.add('show');
    }

    if (location.search.indexOf('sendt=1') > -1) kvitter();

    form.addEventListener('submit', function (e) {
      if (typeof form.checkValidity === 'function' && !form.checkValidity()) return;
      e.preventDefault();
      var sendt = false;

      function nulstil() {
        if (btn) { btn.disabled = false; btn.textContent = btnText; }
      }

      if (btn) { btn.disabled = true; btn.textContent = 'Sender…'; }

      fetch(form.action, { method: 'POST', body: new FormData(form) })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (!data || data.success !== true) throw new Error('afvist');
          sendt = true;
          kvitter();
          form.reset();
        })
        .catch(function () {
          if (!sendt) { form.submit(); }  // almindelig afsendelse som reserveplan
        })
        .then(nulstil, nulstil);
    });
  });

  // Nyhedsbrev — sender rigtigt til Brevo.
  // Vi sender i baggrunden, så brugeren bliver på siden og får vores egen kvittering.
  // Går det galt (netværk, blokeret CORS), falder vi tilbage til en almindelig
  // afsendelse, hvor Brevo selv viser en kvitteringsside. Så mister vi aldrig en tilmelding.
  document.querySelectorAll('.news-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      // Lad browseren selv fange tomme felter og manglende samtykke
      if (typeof form.checkValidity === 'function' && !form.checkValidity()) return;
      e.preventDefault();

      var box = form.parentElement.querySelector('.form-ok');
      var btn = form.querySelector('button[type="submit"]');
      var btnText = btn ? btn.textContent : '';
      var sent = false;

      function show(msg, isError) {
        if (!box) return;
        box.textContent = msg;
        box.classList.toggle('error', !!isError);
        box.classList.add('show');
      }
      function reset() {
        if (btn) { btn.disabled = false; btn.textContent = btnText; }
      }

      if (btn) { btn.disabled = true; btn.textContent = 'Sender…'; }

      fetch(form.action + '?isAjax=1', {
        method: 'POST',
        body: new FormData(form),
        mode: 'cors'
      })
        .then(function (r) {
          if (!r.ok) throw new Error('Brevo svarede ' + r.status);
          sent = true;
          show('Tak — du er nu tilmeldt. Vi skriver, når der er nyt i kælderen. 🍷', false);
          form.reset();
        })
        .catch(function () {
          if (!sent) { form.submit(); }  // almindelig afsendelse som reserveplan
        })
        .then(reset, reset);
    });
  });
})();
