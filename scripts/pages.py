# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude")
from build_site import write, newsletter, IG

# ---------------------------------------------------------------- byggeklodser

def wine(wid, name, meta, pull, img, img_alt, specs, taste, prices, fill=False, extra=""):
    spec_rows = "".join(
        "\n          <dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in specs)
    price_html = ""
    for b, note in prices:
        if b is None:
            if note:
                price_html += '\n          <p class="price-ask">%s</p>' % note
        elif b.startswith("~"):
            price_html += '\n          <p class="price-single">%s</p>' % b[1:]
        else:
            price_html += '\n          <div class="price"><b>%s</b><span>%s</span></div>' % (b, note)
    if img is None:
        # Ingen flaske til denne vin - vi viser markens navn i stedet for at laane en anden flaske.
        photo = ('<div class="wine-photo plate"><div class="plate-in">'
                 '<span class="plate-eyebrow">Enkeltmark</span>'
                 '<span class="plate-name">%s</span>'
                 '<span class="plate-meta">%s</span>'
                 '</div></div>' % (img_alt[0], img_alt[1]))
        return '''
      <article class="wine" id="%s">
        %s''' % (wid, photo) + '''
        <div>
          <h3>%s</h3>
          <p class="wine-meta">%s</p>
          <p class="pull">%s</p>
          <dl class="spec">%s
          </dl>
          <p class="taste">%s</p>
          %s
          <div class="prices">%s
          </div>
        </div>
      </article>''' % (name, meta, pull, spec_rows, taste, extra, price_html)
    return '''
      <article class="wine" id="%s">
        <div class="wine-photo%s"><img src="assets/img/%s" alt="%s"></div>
        <div>
          <h3>%s</h3>
          <p class="wine-meta">%s</p>
          <p class="pull">%s</p>
          <dl class="spec">%s
          </dl>
          <p class="taste">%s</p>
          %s
          <div class="prices">%s
          </div>
        </div>
      </article>''' % (wid, " fill" if fill else "", img, img_alt, name, meta, pull,
                       spec_rows, taste, extra, price_html)


# ---------------------------------------------------------------- FORSIDE

forside = '''<section class="hero hero-dark band-dark">
  <div class="wrap">
    <img class="hero-bottle" src="assets/img/bakuretsu-fl.png" alt="Bakuretsu Cava Ros&eacute;">
    <p class="eyebrow">Vinimport &middot; K&oslash;benhavn &middot; Est. 2024</p>
    <h1>Ingen st&oslash;j - bare ordentlig vin til anst&aelig;ndige priser.</h1>
    <div class="hero-lines" style="margin-top:30px">
      <p>Vi er to, der importerer vin.</p>
      <p>Ikke mange - f&aring;, og kun dem vi selv ville s&aelig;tte p&aring; bordet.</p>
      <p>Vi henter dem hjem fra folk, vi har m&oslash;dt.</p>
      <p>Og vi kan fortælle dig, hvem de er.</p>
    </div>
    <div class="cta-row">
      <a class="btn btn-primary" href="producenter.html">Se producenterne</a>
      <a class="btn btn-ghost" href="om-os.html">Vores historie</a>
    </div>
  </div>
</section>

<section class="after-hero">
  <div class="wrap">
    <p class="eyebrow">Navnet</p>
    <h2>Decent er ikke et beskedent ord</h2>
    <p class="lede" style="margin:18px 0 40px">Det betyder anst&aelig;ndig. Ordentlig. Uden armbev&aelig;gelser. Vi tog det som navn,
      fordi det skal kunne forsvares - b&aring;de om vinen og om m&aring;den, vi handler p&aring;.</p>
    <div class="pillars">
      <div class="pillar">
        <h3>F&aring; producenter</h3>
        <p>Vi vil hellere kende to godt end tredive overfladisk. Sortimentet vokser kun,
          n&aring;r vi har m&oslash;dt nogen, vi vil st&aring; inde for.</p>
      </div>
      <div class="pillar">
        <h3>Relationen f&oslash;r prisen</h3>
        <p>Vi handler ikke p&aring; pris alene. En relation, der holder, er mere v&aelig;rd
          end en forhandling, der blev vundet.</p>
      </div>
      <div class="pillar">
        <h3>Balance frem for power</h3>
        <p>Vine, der l&oslash;fter uden at fylde. Terroir og enkeltmarker frem for
          teknik for teknikkens skyld.</p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Fra vores eget bord</p>
    <h2>Vi drikker det, vi s&aelig;lger</h2>
    <p class="lede" style="margin:16px 0 2px">Ingen studieopstilling. Det er flaskerne,
      som de ser ud hjemme hos os, p&aring; en helt almindelig aften.</p>
    <div class="strip">
      <figure><img src="assets/img/nebbiolo-glas.jpg" alt="Flaske Nebbiolo d&rsquo;Alba fra AL-MA med prop og fyldt glas p&aring; en k&oslash;kkenbordplade"><figcaption>Nebbiolo d&rsquo;Alba</figcaption></figure>
      <figure><img src="assets/img/bakuretsu-rogn.jpg" alt="Bakuretsu Cava Ros&eacute; sk&aelig;nket op ved siden af en sk&aring;l rogn og cr&egrave;me fraiche"><figcaption>Bakuretsu til rognen</figcaption></figure>
      <figure><img src="assets/img/trepat-bord.jpg" alt="Flaske Mas de la Pansa Trepat 2020 p&aring; et egetr&aelig;sbord"><figcaption>Mas de la Pansa Trepat</figcaption></figure>
      <figure><img src="assets/img/arawaru-glas.jpg" alt="Flaske Arawaru med sk&aelig;nket glas og t&aelig;ndte lys"><figcaption>Arawaru</figcaption></figure>
    </div>
  </div>
</section>

<section class="band-soft">
  <div class="wrap">
    <p class="eyebrow">Producenterne</p>
    <h2>To huse. Samme m&aring;lestok.</h2>
    <p class="lede" style="margin:18px 0 10px">Vi begyndte i Catalonien og fortsatte i Piemonte.
      R&aelig;kkef&oslash;lgen betyder ikke s&aring; meget - begge steder handlede det om at m&oslash;de nogen,
      vi kunne st&aring; inde for.</p>

    <div class="entrances">
      <div class="entrance">
        <a class="entrance-img contain" href="producenter.html#alma" tabindex="-1" aria-hidden="true"><img src="assets/img/barolo.png" alt="Barolo fra AL-MA / Giribaldi"></a>
        <div>
          <h2><a class="entrance-title" href="producenter.html#alma">AL-MA &middot; Giribaldi</a></h2>
          <p class="where">Rodello &middot; Piemonte &middot; Italien</p>
          <p>Fjerde generation i Langhe. Ti mennesker, &eacute;n mark, samme arbejde hver dag.
            AL-MA er Alessandras og Matteos eget navn - samme ving&aring;rde som Giribaldi,
            men en yngre stemme. Og &oslash;kologisk Barolo, hvilket i Piemonte stadig er undtagelsen.</p>
          <a class="arrow" href="producenter.html#alma">Nebbiolo, Barolo og Ravera</a>
        </div>
      </div>

      <div class="entrance">
        <a class="entrance-img contain" href="producenter.html#imma" tabindex="-1" aria-hidden="true"><img src="assets/img/bakuretsu-fl.png" alt="Bakuretsu Cava Ros&eacute; fra Mas de la Pansa"></a>
        <div>
          <h2><a class="entrance-title" href="producenter.html#imma">Mas de la Pansa &middot; Imma Soler</a></h2>
          <p class="where">Conca de Barber&agrave; &middot; Catalonien &middot; Spanien</p>
          <p>Imma begyndte med at s&aelig;lge familiens druer. I dag laver hun kun den vin, hun selv
            har lyst til at drikke: fem hektar, &oslash;kologisk, minimal indgriben - og &eacute;n drue,
            Trepat, i tre vidt forskellige udtryk. Vores allerf&oslash;rste palle var hendes cava.</p>
          <a class="arrow" href="producenter.html#imma">Tre udtryk p&aring; Trepat</a>
        </div>
      </div>
    </div>
  </div>
</section>

''' + newsletter(
    "V&aelig;r f&oslash;rst, n&aring;r nye flasker lander",
    "Vi skriver, n&aring;r vi henter nyt hjem, holder smagninger eller l&oslash;fter sl&oslash;ret for n&aelig;ste parti. Ingen spam - kun vin.")


# ---------------------------------------------------------------- PRODUCENTER

alma_wines = (
    wine("nebbiolo", "Nebbiolo d'Alba",
         "Montelupo Albese &middot; &Aring;rgang 2022 &middot; &Oslash;kologisk",
         "Ren Nebbiolo - 40 dage p&aring; st&aring;l, f&oslash;r den overhovedet ser et fad. Det tager tid, men ingen genveje.",
         "nebbiolo.png", "Nebbiolo d'Alba fra AL-MA",
         [("Drue", "100 % Nebbiolo"),
          ("Appellation", "D.O.C. Nebbiolo d'Alba, Montelupo Albese (480 moh., syd)"),
          ("Metode", "16 dages skalmaceration ved ca. 28 &deg;C, 40 dage p&aring; st&aring;l. Derefter ca. 15 mdr. p&aring; barrique, min. 6 mdr. p&aring; flaske")],
         "Intens rubinr&oslash;d med orange sk&aelig;r. Rose, hindb&aelig;r, vanilje og balsamiske toner. T&oslash;r, fyldig og rund, med unge tanniner, syltede r&oslash;de b&aelig;r og et strejf kanel.",
         [("165 kr./fl.", "ved 6 stk. &middot; 990 kr. i alt"), ("~Enkeltflaske: 189 kr.", "")]) +
    wine("barolo", "Barolo",
         "Novello &middot; &Aring;rgang 2022 &middot; &Oslash;kologisk",
         "En rigtig god Barolo, uden at ville v&aelig;re mere, end den er.",
         "barolo.png", "Barolo fra AL-MA",
         [("Drue", "100 % Nebbiolo (Michet, Lampia, Ros&eacute;)"),
          ("Appellation", "D.O.C.G. Barolo, Novello (350&ndash;400 moh., syd)"),
          ("Metode", "20 dages traditionel maceration ved 30&ndash;35 &deg;C. 4 mdr. p&aring; st&aring;l, derefter 2 &aring;r p&aring; fransk eg. Flaskelagret i ving&aring;rdens underjordiske k&aelig;lder ved 16 &deg;C")],
         "Intens rubinr&oslash;d, med murstensr&oslash;de nuancer efter lagring. R&oslash;de b&aelig;r, kirseb&aelig;r, et strejf hvid peber. Varm og bl&oslash;d, med indpakkende tanniner og en krydret afslutning.",
         [("250 kr./fl.", "ved 3 stk. &middot; 750 kr. i alt"),
          ("235 kr./fl.", "ved 6 stk. &middot; 1.410 kr. i alt"),
          ("~Enkeltflaske: 279 kr.", "")]) +
    wine("ravera", "Barolo Ravera",
         "Enkeltmark (MGA) &middot; &Aring;rgang 2020 &middot; &Oslash;kologisk",
         "Ravera regnes blandt Barolos mest anerkendte marker. Her taler jorden for sig selv.",
         "barolo.png", "Barolo Ravera fra AL-MA",
         [("Drue", "100 % Nebbiolo (Michet, Lampia, Ros&eacute;)"),
          ("Appellation", "D.O.C.G. Barolo, MGA Ravera, Novello (ca. 360 moh., syd)"),
          ("Metode", "Traditionel maceration. L&aelig;ngere fadlagring end husets almindelige Barolo")],
         "Rubinr&oslash;d med murstensr&oslash;de reflekser. S&oslash;d duft af kirseb&aelig;r, syltede b&aelig;r og et strejf hvid peber - karakteristisk for Novello. Varm og bl&oslash;d, med kompleks krydderi i eftersmagen.",
         [("365 kr./fl.", "ved 3 stk. &middot; 1.095 kr. i alt"),
          ("350 kr./fl.", "ved 6 stk. &middot; 2.100 kr. i alt"),
          ("~Enkeltflaske: 399 kr.", "")])
)

imma_wines = (
    wine("bakuretsu", "Bakuretsu",
         "Cava Ros&eacute; &middot; Trepat 2023 &middot; &Oslash;kologisk",
         "&raquo;Stille-elegant.&laquo; Friskere og frugtigere, fordi den bevidst er holdt p&aring; st&aring;ltank - aldrig fad.",
         "bakuretsu-fl.png", "Bakuretsu Cava Ros&eacute;",
         [("Drue", "100 % Trepat"),
          ("Appellation", "D.O. Conca de Barber&agrave;, Catalonien"),
          ("Dosage", "Brut &middot; 11,5 %"),
          ("Metode", "Traditionel metode, 18 mdr. p&aring; b&aelig;rmen. St&aring;ltank, ingen fadlagring")],
         "Lys laksefarve. Jordb&aelig;r og kirseb&aelig;r, et strejf brioche. Fin syre, hindb&aelig;r, citron, lang frisk eftersmag. "
         "Til aperitif, friske skaldyr og &oslash;sters, bl&oslash;de oste, let charcuteri.",
         [("149 kr./fl.", "750 kr. pr. kasse (6 fl.)")],
         extra='<p class="etiket"><b>Etiketten</b>Bakuretsu og Arawaru er malet af den japanske kunstner '
               'Wataru Koike (f.&nbsp;1978, Nagoya) - tidligere marketingdirekt&oslash;r, i dag billedkunstner. '
               'Samarbejdet med Mas de la Pansa er en del af hans udforskning af vin som spejl af landskab og tid.</p>') +
    wine("trepat", "Mas de la Pansa &middot; Trepat",
         "Enkeltmark &middot; &Aring;rgang 2020 &middot; &Oslash;kologisk",
         "Husets seri&oslash;se, terroir-drevne Trepat. Finesse fremfor power - energi, friskhed, r&oslash;de b&aelig;r og friske urter.",
         "mdlp-trepat.png", "Mas de la Pansa Trepat, enkeltmark",
         [("Drue", "100 % Trepat"),
          ("Appellation", "D.O. Conca de Barber&agrave;, Catalonien (enkeltmark)"),
          ("Alkohol", "13 %"),
          ("Metode", "29 dages maceration i st&aring;ltank, bl&oslash;d presning. Derefter 5 mdr. p&aring; fransk eg (2. brug)"),
          ("P&aring; flaske", "Uden fining eller filtrering")],
         "Fra marken familien plantede i 1957 p&aring; en nordvendt skr&aring;ning. Tres &aring;r gamle stokke, lavt udbytte, dybere koncentration.",
         [("269 kr./fl.", "1.350 kr. pr. kasse (6 fl.)")],
         extra='<p class="etiket"><b>Etiketten</b>Hesten hedder Vermell. Han reddede livet for Immas far, dengang '
               'han var tre &aring;r gammel: bedstefaren pl&oslash;jede marken, hesten n&aelig;gtede pludselig at g&aring; videre '
               '- for ved hans f&oslash;dder l&aring; den lille dreng. Et familie-skr&aelig;mmebillede, der er blevet en '
               'historie, de gerne fort&aelig;ller videre.</p>') +
    wine("arawaru", "Arawaru",
         "Trepat 2024 &middot; Det lettere spor",
         "&raquo;Pinot Noir m&oslash;der Gamay&hellip; med spansk middelhavsst&oslash;v.&laquo; Ikke power og m&oslash;rk tyngde.",
         "arawaru-fl.png", "Arawaru, Trepat 2024",
         [("Drue", "100 % Trepat"),
          ("Appellation", "D.O. Conca de Barber&agrave;, Catalonien"),
          ("Alkohol", "12 %"),
          ("Metode", "Koldmaceration, derefter kort lagring i st&aring;ltank")],
         "Lys, saftig, frisk, med krydret kant: jordb&aelig;r, ribs, granat&aelig;ble, t&oslash;rrede urter, hvid peber, lidt blomster.",
         [("139 kr./fl.", "700 kr. pr. kasse (6 fl.)")],
         extra='<p class="etiket"><b>Etiketten</b>Malet af Wataru Koike - samme kunstner som Bakuretsu.</p>')
)

smagekasse = '''
      <div class="smagekasse">
        <p class="eyebrow">Smagekasse</p>
        <h3>Trepat 3-pak</h3>
        <p>&Eacute;n af hver: Bakuretsu, Mas de la Pansa Trepat og Arawaru. Samme drue, samme
          k&aelig;lder, tre helt forskellige udtryk - bobler, seri&oslash;s enkeltmark og let og frisk.</p>
        <div class="price"><b>495 kr.</b><span>for alle tre</span></div>
      </div>'''

producenter = '''<section class="hero band-dark" style="padding:58px 0 52px">
  <div class="wrap">
    <p class="eyebrow">Producenterne</p>
    <h1 style="font-size:clamp(2.2rem,5vw,3.4rem)">Dem vi henter hjem fra</h1>
    <p class="lede" style="margin-top:22px">To huse, to lande. Historien f&oslash;rst - vinene nedenunder,
      der hvor de h&oslash;rer til.</p>
  </div>
</section>

<section class="producer" id="alma" style="padding-bottom:20px">
  <div class="wrap">
    <div class="producer-head">
      <p class="eyebrow">Producent</p>
      <h2>AL-MA &middot; Giribaldi</h2>
      <p class="where">Rodello &middot; Piemonte &middot; Italien</p>
      <p class="pull" style="margin-bottom:0">To navne. &Eacute;n ving&aring;rd.</p>
    </div>
    <div class="producer-body">
      <div>
        <p>Giribaldi er en familieving&aring;rd i Rodello, i hjertet af Langhe. Grundlagt i starten
          af 1900-tallet, drevet af samme familie i tre generationer siden.</p>
        <p>I dag st&aring;r Mario og Giovanna Giribaldi i spidsen sammen med deres b&oslash;rn
          Alessandra og Matteo - fjerde generation. Ti mennesker, &eacute;n mark, samme arbejde hver dag.</p>
        <p>AL-MA er Alessandras og Matteos eget navn: deres to forbogstaver, sat sammen. Samme
          ving&aring;rde, samme druer, samme k&aelig;lder som Giribaldi - men en yngre stemme og en
          mere nutidig stil. Hvor de klassiske Giribaldi-vine er t&aelig;nkt til at ligge i &aring;revis,
          er AL-MA&rsquo;erne lavet til at v&aelig;re klar, n&aring;r de lander i glasset. Vi har valgt at
          arbejde med AL-MA, fordi det er dem, vi har m&oslash;dt - og fordi navnet fort&aelig;ller,
          hvem der reelt st&aring;r bag vinen i dag.</p>
        <p>Giribaldi er blandt de f&aring; certificeret &oslash;kologiske Barolo-producenter i Piemonte
          - en region, hvor &oslash;kologisk dyrkning stadig er undtagelsen snarere end reglen.</p>
      </div>
      <figure class="producer-photo">
        <img src="assets/img/alessandra-kasper.jpg" alt="Alessandra Giribaldi og Kasper foran de store fade i Rodello">
        <figcaption>Alessandra og Kasper i k&aelig;lderen i Rodello.</figcaption>
      </figure>
    </div>


    <div class="wines-head" style="margin-top:44px">
      <p class="eyebrow">Bes&oslash;get</p>
      <p>Rodello, en eftermiddag i juli.</p>
    </div>
    <div class="strip">
      <figure><img src="assets/img/giribaldi-indgang.jpg" alt="Indgangen til Giribaldi med familiev&aring;benet over porten"><figcaption>Porten, med v&aring;benet over</figcaption></figure>
      <figure><img src="assets/img/giribaldi-tanke.jpg" alt="Ståltanke hos Giribaldi"><figcaption>St&aring;ltankene</figcaption></figure>
      <figure><img src="assets/img/giribaldi-kaelder.jpg" alt="Store egefade i k&aelig;lderen"><figcaption>De store fade</figcaption></figure>
      <figure><img src="assets/img/giribaldi-fad.jpg" alt="Fadbund med Azienda Agricola Mario Giribaldi br&aelig;ndt i tr&aelig;et"><figcaption>Azienda Agricola Mario Giribaldi</figcaption></figure>
      <figure><img src="assets/img/langhe-besog.jpg" alt="Udsigt over Langhe fra smagerummet"><figcaption>Udsigten er Langhe</figcaption></figure>
      <figure><img src="assets/img/giribaldi-udsigt.jpg" alt="Barolo MGA-bogen p&aring; bordet i smagerummet"><figcaption>Barolo MGA p&aring; bordet</figcaption></figure>
    </div>

    <div class="wines-head">
      <p class="eyebrow">Tre vine fra Langhe</p>
      <p>Fra en hverdags-Nebbiolo til Barolos mest anerkendte enkeltmark.</p>
    </div>
''' + alma_wines + '''
  </div>
</section>

<section class="producer" id="imma" style="border-top:1px solid var(--rule)">
  <div class="wrap">
    <div class="producer-head">
      <p class="eyebrow">Producent</p>
      <h2>Mas de la Pansa &middot; Imma Soler</h2>
      <p class="where">Conca de Barber&agrave; &middot; Catalonien &middot; Spanien</p>
      <p class="pull" style="margin-bottom:0">&Eacute;n kvinde. &Eacute;n drue. Conca de Barber&agrave;.</p>
    </div>
    <div class="producer-body">
      <div>
        <p>Imma Soler startede med at s&aelig;lge familiens druer. Nu laver hun sin egen vin
          - og kun den, hun selv har lyst til at drikke.</p>
        <p>Hun er uddannet i PR og marketing, sidenhen sommelier fra CETT i Barcelona og videre
          med WSET. Projektet startede i Viver de Celleristes i Barber&agrave; de la Conca - en
          vin-inkubator i det gamle andelskooperativ fra 1894, den f&oslash;rste af sin slags i
          Catalonien. F&oslash;rste &aring;rgang var 2016.</p>
        <p>I dag arbejder hun med &eacute;t ben i Alt Camp, hvor de gamle Macabeu- og
          Parellada-marker st&aring;r, og &eacute;t i Conca de Barber&agrave;, hjemsted for Trepat.
          Cirka fem hektar, certificeret &oslash;kologisk, minimal indgriben. Ingen masker -
          vinen skal spejle stedet, som det er.</p>
        <p>Familien plantede Trepat-marken i 1957, p&aring; en nordvendt skr&aring;ning. Vinstokkene er
          i dag tres &aring;r gamle - gamle nok til lavt udbytte og dybere koncentration i druerne.</p>
        <p class="pull" style="margin:26px 0 0">Trepat er ikke en drue med power og m&oslash;rk tyngde.
          Den er lys, elegant, lav i alkohol, med god syre og en krydret kant af r&oslash;de b&aelig;r.</p>
        <p style="margin-top:16px">Trepat er en gammel drue i Conca de Barber&agrave;, men en ung
          r&oslash;dvin. I &aring;rtier blev den kun brugt til ros&eacute; og cava - den f&oslash;rste
          t&oslash;rre, r&oslash;de udgave kom f&oslash;rst p&aring; markedet i 2004, lavet af en anden
          producent i omr&aring;det. Alt, hvad Imma laver, kommer fra den samme drue, i den samme
          k&aelig;lder. Forskellen mellem hendes to spor er intentionen: det stille og traditionelle
          - og det, der t&oslash;r lidt mere.</p>
        <p>Det var hendes cava, der stod p&aring; vores allerf&oslash;rste palle. Vi baksede med den
          i frostvejr - og s&aring; var K&amp;K Vinimport pludselig en realitet.</p>
      </div>
      <figure class="producer-photo">
        <img src="assets/img/imma-fad.jpg" alt="Imma Soler ved et fad med en flaske Mas de la Pansa Trepat">
        <figcaption>Imma Soler, Conca de Barber&agrave;.</figcaption>
      </figure>
    </div>


    <div class="wines-head" style="margin-top:44px">
      <p class="eyebrow">Hos Imma</p>
      <p>Marken, k&aelig;lderen og bordet.</p>
    </div>
    <div class="strip">
      <figure><img src="assets/img/imma-mark.jpg" alt="Imma Soler &aring;bner en flaske ude i vinmarken"><figcaption>Flasken &aring;bnet i marken</figcaption></figure>
      <figure><img src="assets/img/imma-vinstokke.jpg" alt="Imma Soler mellem gamle vinstokke"><figcaption>De gamle stokke</figcaption></figure>
      <figure><img src="assets/img/imma-smagning.jpg" alt="Imma Soler med en flaske Mas de la Pansa til smagning"><figcaption>Til smagning</figcaption></figure>
      <figure><img src="assets/img/cava.jpg" alt="Den f&oslash;rste palle cava, leveret i frostvejr"><figcaption>Vores f&oslash;rste palle, i frostvejr</figcaption></figure>
    </div>

    <div class="wines-head">
      <p class="eyebrow">Tre udtryk. Samme drue.</p>
      <p>Bobler, seri&oslash;s enkeltmark og let, frisk r&oslash;dvin - alt sammen 100&nbsp;% Trepat.</p>
    </div>
''' + imma_wines + smagekasse + '''
  </div>
</section>

''' + newsletter(
    "F&oslash;lg med, n&aring;r der kommer nyt hjem",
    "Vi skriver, n&aring;r vi henter nyt hjem, holder smagninger eller l&oslash;fter sl&oslash;ret for n&aelig;ste parti.")


# ---------------------------------------------------------------- OM OS

om_os = '''<section class="hero band-dark" style="padding:58px 0 52px">
  <div class="wrap">
    <p class="eyebrow">Om os</p>
    <h1 style="font-size:clamp(2.2rem,5vw,3.4rem)">Det begyndte med en palle i frostvejr</h1>
    <p class="lede" style="margin-top:22px">K&amp;K Vinimport er Kasper og Kim. Der er ikke flere af os 
      - og ikke flere producenter, end vi kan n&aring; at bes&oslash;ge.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="producer-body" style="padding-top:0">
      <div>
        <p>Vi startede i 2024 med det enkleste, vi kunne komme p&aring;: hente vin hjem fra folk,
          vi selv havde m&oslash;dt, og som vi kunne st&aring; inde for.</p>
        <p>Den f&oslash;rste palle var cava fra Catalonien. Vi pakkede den ud i bidende kulde,
          solgte den til glade kunder - og s&aring; var virksomheden en realitet.</p>
        <p>Siden er Piemonte kommet til: Nebbiolo d&rsquo;Alba, Barolo og Barolo Ravera fra
          Giribaldi i Rodello. To producenter, to lande, samme m&aring;lestok.</p>
        <p>Vi har ingen ambition om et katalog p&aring; hundrede vine. Vi vil bygge et lille
          importhus med f&aring; producenter, t&aelig;tte relationer og faglig trov&aelig;rdighed.
          Det tager l&aelig;ngere tid. Det er ogs&aring; meningen.</p>
      </div>
      <div class="producer-photo"><img src="assets/img/smagning-alma.jpg" alt="Fire flasker fra AL-MA stillet op til smagning, med skinke og parmesan p&aring; br&aelig;ttet"></div>
    </div>
  </div>
</section>

<section class="band-soft">
  <div class="wrap midtstillet">
    <p class="eyebrow">Os to</p>
    <h2>Kasper &amp; Kim</h2>
    <p class="lede intro">Der er ikke andre. Vi k&oslash;ber ind, k&oslash;rer paller,
      skriver mails til Italien og Spanien - og vi har smagt hver eneste flaske, vi s&aelig;lger.</p>
    <div class="portraits">
      <figure>
        <img src="assets/img/portraet-kasper.jpg" alt="Kasper hos Giribaldi i Rodello">
        <figcaption>Kasper</figcaption>
      </figure>
      <figure>
        <img src="assets/img/portraet-kim.jpg" alt="Kim">
        <figcaption>Kim</figcaption>
      </figure>
    </div>
    <p class="lede udtro">Producenterne skal kunne bes&oslash;ges. Det er ikke en talem&aring;de
      - det er den eneste m&aring;de, vi ved, hvad vi s&aelig;lger.</p>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">N&aring;r det lander</p>
    <h2>Fra kasse til bord</h2>
    <p class="lede" style="margin:16px 0 2px">F&aring; paller ad gangen. Kassen bliver pakket ud,
      flaskerne stillet op - og vi har smagt p&aring; alt det, vi s&aelig;lger.</p>
    <div class="strip">
      <figure><img src="assets/img/parellada-kasse.jpg" alt="&Aring;ben papkasse med flasker fra Mas de la Pansa, pakket i silkepapir"><figcaption>Ud af kassen</figcaption></figure>
      <figure><img src="assets/img/alma-tre.jpg" alt="Nebbiolo d&rsquo;Alba, Barolo og Barolo Ravera fra AL-MA side om side"><figcaption>Nebbiolo, Barolo, Ravera</figcaption></figure>
      <figure><img src="assets/img/bakuretsu-etiket.jpg" alt="N&aelig;rbillede af Wataru Koikes maleri p&aring; etiketten til Bakuretsu"><figcaption>Wataru Koikes etiket</figcaption></figure>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Det vi g&aring;r efter</p>
    <h2 style="margin-bottom:34px">Tre ting, vi ikke g&aring;r p&aring; kompromis med</h2>
    <div class="pillars">
      <div class="pillar">
        <h3>Kurateret, ikke bredt</h3>
        <p>F&aring; og rigtige frem for bred distribution. Kvalitetsrestauranter, vinbarer og folk,
          der gider bruge tid p&aring;, hvad der st&aring;r i glasset.</p>
      </div>
      <div class="pillar">
        <h3>Producenten skal kunne bes&oslash;ges</h3>
        <p>Vi repr&aelig;senterer kun huse, vi kan m&oslash;de i &oslash;jenh&oslash;jde - og helst f&aring; en tur
          med ud i markerne. Relationen er en del af produktet.</p>
      </div>
      <div class="pillar">
        <h3>Historien vejer lige s&aring; meget</h3>
        <p>Tekniske fakta skal v&aelig;re i orden. Men hvem der har lavet vinen, og hvorfor,
          er ikke en tilf&oslash;jelse - det er hele pointen.</p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Det uglamour&oslash;se</p>
    <h2>EMCS, proformafakturaer og punktafgifter</h2>
    <p class="lede" style="margin-top:18px">Det fylder mere, end nogen fort&aelig;ller p&aring; forh&aring;nd.
      Men det er ogs&aring; der, forskellen ligger mellem at ville importere vin og at g&oslash;re det.</p>
  </div>
</section>

''' + newsletter(
    "F&oslash;lg rejsen",
    "Vi er lige begyndt. Skriv dig op og v&aelig;r med fra de tidlige paller til de n&aelig;ste flasker, der lander.")


# ---------------------------------------------------------------- KONTAKT

W3F = "6583e329-993d-40b0-a9e0-df22db576019"

kontakt = '''<section class="hero band-dark" style="padding:58px 0 52px">
  <div class="wrap">
    <p class="eyebrow">Kontakt</p>
    <h1 style="font-size:clamp(2.2rem,5vw,3.4rem)">Sig hej</h1>
    <p class="lede" style="margin-top:22px">Der sidder ikke en kundeservice i den anden ende.
      Der sidder os to.</p>
  </div>
</section>

<section>
  <div class="wrap contact-grid">
    <div>
      <p class="eyebrow">Skriv til os</p>
      <h2 style="font-size:clamp(1.6rem,3vw,2.15rem);margin:0 0 10px">Send en besked</h2>
      <p style="color:var(--ink-soft);max-width:52ch;margin:0">Bestilling, sp&oslash;rgsm&aring;l til en
        vin, eller om vi kan skaffe noget hjem, vi ikke f&oslash;rer. Det hele m&aring; komme her.</p>

      <form class="kontakt-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="%(w3f)s">
        <input type="hidden" name="subject" value="Ny besked fra decentwines.dk">
        <input type="hidden" name="from_name" value="Decent Wines">
        <input type="hidden" name="redirect" value="https://decentwines.dk/kontakt.html?sendt=1">

        <div class="par">
          <label>
            <span class="lab">Navn</span>
            <input type="text" name="navn" required autocomplete="name">
          </label>
          <label>
            <span class="lab">E-mail</span>
            <input type="email" name="email" required autocomplete="email">
          </label>
        </div>

        <label>
          <span class="lab">Restaurant eller firma <i>(valgfrit)</i></span>
          <input type="text" name="firma" autocomplete="organization">
        </label>

        <label>
          <span class="lab">Besked</span>
          <textarea name="besked" required placeholder="Skriv l&oslash;s."></textarea>
        </label>

        <input class="hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="btn btn-primary" type="submit">Send</button>
      </form>
      <div class="form-ok" role="status"></div>
      <p class="kontakt-note">Vi bruger kun det, du skriver, til at svare dig.
        Beskeden sendes gennem Web3Forms og lander i vores indbakke.</p>
    </div>

    <div>
      <p class="eyebrow">Eller find os her</p>
      <div class="info-line">
        <svg viewBox="0 0 24 24"><path d="M12 2c2.7 0 3 0 4.1.1 1 0 1.7.2 2.3.4.6.3 1.1.6 1.6 1.1s.8 1 1.1 1.6c.2.6.4 1.3.4 2.3.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c0 1-.2 1.7-.4 2.3-.3.6-.6 1.1-1.1 1.6s-1 .8-1.6 1.1c-.6.2-1.3.4-2.3.4-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-1 0-1.7-.2-2.3-.4-.6-.3-1.1-.6-1.6-1.1s-.8-1-1.1-1.6c-.2-.6-.4-1.3-.4-2.3C2 15 2 14.7 2 12s0-3 .1-4.1c0-1 .2-1.7.4-2.3.3-.6.6-1.1 1.1-1.6s1-.8 1.6-1.1c.6-.2 1.3-.4 2.3-.4C9 2 9.3 2 12 2Z" stroke-linejoin="round"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1"/></svg>
        <span><b>Instagram</b><a href="%(ig)s" target="_blank" rel="noopener">@decentwines_dk</a></span>
      </div>
      <div class="info-line">
        <svg viewBox="0 0 24 24"><path d="M8 3h8l-1 8a4 4 0 01-3 4v4m-3 0h6M8 3l1 8a4 4 0 003 4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span><b>Bestilling</b>Skriv i formularen, s&aring; vender vi tilbage med m&aelig;ngder og levering.</span>
      </div>
      <div class="info-line">
        <svg viewBox="0 0 24 24"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 9h.01M15 9h.01M9 13h.01M15 13h.01M9 17h6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span><b>Virksomhed</b>K&amp;K Vinimport ApS &middot; CVR 45262464 &middot; K&oslash;benhavn</span>
      </div>
      <div class="info-line">
        <svg viewBox="0 0 24 24"><path d="M4 21c4-2 5-8 4-12M20 21c-4-2-5-8-4-12M8 5c1.5 1.5 6.5 1.5 8 0" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span><b>Vi s&aelig;lger til</b>Restauranter, vinbarer og kvalitetsbevidste privatkunder.</span>
      </div>
    </div>
  </div>
</section>

''' % {"ig": IG, "w3f": W3F} + newsletter(
    "F&aring; besked, n&aring;r vi henter nyt hjem",
    "Vi skriver, n&aring;r der lander nye flasker, n&aring;r vi holder smagninger, eller n&aring;r vi l&oslash;fter sl&oslash;ret for n&aelig;ste parti. Ingen spam - kun vin.")

# ---------------------------------------------------------------- skriv

write("index.html", "Decent Wines - K&K Vinimport ApS",
      "Vinimport fra få producenter i Catalonien og Piemonte. Ingen støj – bare ordentlig vin til anstændige priser.",
      "index.html", forside)

write("producenter.html", "Producenterne - Decent Wines",
      "AL-MA / Giribaldi i Piemonte og Imma Soler / Mas de la Pansa i Catalonien - historien først, vinene under.",
      "producenter.html", producenter)

write("om-os.html", "Om os - Decent Wines",
      "K&K Vinimport er Kasper og Kim. Et lille importhus med få producenter, tætte relationer og faglig troværdighed.",
      "om-os.html", om_os)

write("kontakt.html", "Kontakt & nyhedsbrev - Decent Wines",
      "Skriv til Decent Wines om bestilling, en bestemt vin eller noget vi kan skaffe hjem. Eller skriv dig op til nyhedsbrevet.",
      "kontakt.html", kontakt)
