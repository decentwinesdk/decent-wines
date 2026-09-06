# -*- coding: utf-8 -*-
"""Bygger Decent Wines-sitet ud fra én skabelon, så header/footer altid er ens."""
import io, os

OUT = "/home/claude/decent-wines"

BREVO = ("https://62e904bf.sibforms.com/serve/MUIFAG2A2gWKubWiqWdExfg6kOr6Wq6eEWOk4"
         "JirmvcQedDVjGHmjH87_S_nf4TB99nz8p_yTzEKbAakLxGEgsClbC5xRG1KDWSuz-IR7HvFkXXA2cKP8D4d_4_"
         "NRy9fJrEfNiZzcUHf4L7oTyGyOHggNbIS1VZ2iAjiGGfV-3I_Qyovolha_K0lVCr4TsNomSwHNfzJsHrQ_dsoBQ==")

IG = "https://www.instagram.com/decentwines_dk/"

IG_SVG = ('<svg viewBox="0 0 24 24"><path d="M12 2c2.7 0 3 0 4.1.1 1 0 1.7.2 2.3.4.6.3 1.1.6 1.6 '
          '1.1s.8 1 1.1 1.6c.2.6.4 1.3.4 2.3.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c0 1-.2 1.7-.4 2.3-.3.6-.6 '
          '1.1-1.1 1.6s-1 .8-1.6 1.1c-.6.2-1.3.4-2.3.4-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-1 0-1.7-.2-2.3-.4-.6-.3-1.1-.6-1.6-1.1'
          's-.8-1-1.1-1.6c-.2-.6-.4-1.3-.4-2.3C2 15 2 14.7 2 12s0-3 .1-4.1c0-1 .2-1.7.4-2.3.3-.6.6-1.1 1.1-1.6s1-.8 '
          '1.6-1.1c.6-.2 1.3-.4 2.3-.4C9 2 9.3 2 12 2Zm0 5a5 5 0 100 10 5 5 0 000-10Zm0 8.2a3.2 3.2 0 110-6.4 3.2 3.2 0 '
          '010 6.4Zm5.2-8.4a1.2 1.2 0 100 2.4 1.2 1.2 0 000-2.4Z"/></svg>')

NAV = [("index.html", "Forside"), ("producenter.html", "Producenter"),
       ("om-os.html", "Om os"), ("kontakt.html", "Kontakt")]


def nav_links(active):
    out = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        out.append('      <a href="%s"%s>%s</a>' % (href, cls, label))
    out.append('      <a class="ig-btn" href="%s" target="_blank" rel="noopener">%s Instagram</a>' % (IG, IG_SVG))
    return "\n".join(out)


def newsletter(heading, text):
    return '''<section id="nyhedsbrev">
  <div class="wrap">
    <div class="news">
      <p class="eyebrow">Nyhedsbrev</p>
      <h2>%s</h2>
      <p>%s</p>
      <form class="news-form" action="%s" method="POST">
        <input type="email" name="EMAIL" placeholder="Din e-mail" aria-label="E-mail" required>
        <button class="btn btn-primary" type="submit">Skriv mig op</button>
        <label class="news-consent">
          <input type="checkbox" name="OPT_IN" value="1" required>
          <span>Ja tak - skriv mig op til nyhedsbrevet. Jeg kan afmelde igen med &eacute;t klik.</span>
        </label>
        <input class="hp" type="text" name="email_address_check" value="" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="locale" value="da">
      </form>
      <div class="form-ok" role="status"></div>
    </div>
  </div>
</section>''' % (heading, text, BREVO)


PAGE = '''<!DOCTYPE html>
<html lang="da">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="da_DK">
<meta property="og:url" content="https://decentwines.dk/%(fname)s">
<meta property="og:image" content="https://decentwines.dk/assets/img/logo.png">
<link rel="canonical" href="https://decentwines.dk/%(fname)s">
<meta name="twitter:card" content="summary">
<link rel="icon" href="assets/img/logo.png">
<link rel="apple-touch-icon" href="assets/img/logo.png">
<link rel="preload" href="assets/fonts/source-serif-4-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>

<header class="site-header">
  <nav class="nav">
    <a class="brand" href="index.html">
      <img src="assets/img/logo.png" alt="Decent Wines">
      <span class="brand-txt"><strong>DECENT WINES</strong><small>K&amp;K Vinimport ApS</small></span>
    </a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg></button>
    <div class="nav-links">
%(nav)s
    </div>
  </nav>
</header>

%(body)s

<footer class="site-footer band-dark">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand" href="index.html">
          <img src="assets/img/logo.png" alt="Decent Wines">
          <span class="brand-txt"><strong>DECENT WINES</strong><small>K&amp;K Vinimport ApS</small></span>
        </a>
        <p>Vin fra f&aring; producenter, vi selv har m&oslash;dt. Catalonien og Piemonte. Etableret 2024.</p>
      </div>
      <div class="foot-col">
        <h4>Site</h4>
        <a href="index.html">Forside</a>
        <a href="producenter.html">Producenter</a>
        <a href="om-os.html">Om os</a>
        <a href="kontakt.html">Kontakt</a>
      </div>
      <div class="foot-col">
        <h4>Producenter</h4>
        <a href="producenter.html#alma">AL-MA &middot; Giribaldi</a>
        <a href="producenter.html#imma">Mas de la Pansa &middot; Imma Soler</a>
        <h4 style="margin-top:22px">F&oslash;lg med</h4>
        <a href="%(ig)s" target="_blank" rel="noopener">@decentwines_dk</a>
        <a href="kontakt.html#nyhedsbrev">Nyhedsbrev</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 K&amp;K Vinimport ApS &middot; CVR 45262464 &middot; K&oslash;benhavn</span>
      <span class="tagline-foot">Ingen st&oslash;j - bare ordentlig vin til anst&aelig;ndige priser.</span>
    </div>
  </div>
</footer>

<script src="assets/main.js"></script>
</body>
</html>
'''


def write(fname, title, desc, active, body):
    # index.html vises som bar rod, de andre med deres filnavn
    canonical = "" if fname == "index.html" else fname
    html = PAGE % {"title": title, "desc": desc, "nav": nav_links(active),
                   "body": body, "ig": IG, "fname": canonical}
    with io.open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("skrev", fname, len(html), "tegn")
