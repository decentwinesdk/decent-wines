Sitet skrives ikke i haanden. Det bygges af de to scripter her.

build_site.py er rammen om alle sider: header, footer, nav, nyhedsbrev, head-tags.
pages.py er alt indholdet paa de fire sider.

Saadan bygger man: laeg begge filer ved siden af mappen med sitet, ret OUT i
build_site.py saa den peger paa den mappe, og koer "python3 pages.py".

Den skriver index.html, producenter.html, om-os.html og kontakt.html.
Ret aldrig i HTML-filerne direkte. De bliver overskrevet ved naeste build.
