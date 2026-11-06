import os, sys

ROOT = sys.argv[1]
U = "https://images.unsplash.com/photo-{}?auto=format&fit=crop&w={}&q=80"
IMG = {
    "hero": "1486262715619-67b85e0b08d3",
    "engine": "1487754180451-c456f719a1fc",
    "dark": "1503376780353-7e6692767b70",
    "car1": "1492144534655-ae79c964c9d7",
    "car2": "1580273916550-e323be2ae537",
    "car3": "1552519507-da3b142c6e3d",
    "car4": "1494976388531-d1058494cdd8",
    "car5": "1568605117036-5fe5e7bab0b7",
    "tools": "1530046339160-ce3e530c7d2f",
    "mech": "1619642751034-765dfdf7c58e",
    "mech2": "1625047509248-ec889cbff17f",
}
def img(k, w=1600):
    return U.format(IMG[k], w)

PHONE = "+90 (5XX) XXX XX XX"
PHONE_HREF = "+905000000000"
EMAIL = "info@vagmer.com.tr"
ADDRESS = "İstanbul, Türkiye"

ICONS = {
    "phone": '<svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24"><path d="M21 12a8.5 8.5 0 0 1-12.6 7.4L3 21l1.6-5.2A8.5 8.5 0 1 1 21 12z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "engine": '<svg viewBox="0 0 24 24"><path d="M4 10h2V8h3V6h6v2h2l2 3h2v5h-2l-2 3H8l-2-3H4z"/><path d="M9 6V4h6v2"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>',
    "gear": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
    "drop": '<svg viewBox="0 0 24 24"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>',
    "chain": '<svg viewBox="0 0 24 24"><circle cx="7" cy="12" r="4"/><circle cx="17" cy="12" r="4"/><path d="M7 8h10M7 16h10"/></svg>',
    "disc": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>',
    "fan": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-7 4-7s3 4-2 7M14 12c4 0 7 1 7 4s-4 3-7-2M12 14c0 4-1 7-4 7s-3-4 2-7M10 12c-4 0-7-1-7-4s4-3 7 2"/></svg>',
    "chip": '<svg viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "tag": '<svg viewBox="0 0 24 24"><path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/></svg>',
    "eye": '<svg viewBox="0 0 24 24"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
}

NAV = [("index.html", "Ana Sayfa"), ("hizmetler.html", "Hizmetler"), ("hakkimizda.html", "Hakkımızda"), ("iletisim.html", "İletişim")]
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.4-1.5-.9-.8-1.5-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4C2.7 15.6 2.2 13.8 2.2 12 2.2 6.6 6.6 2.2 12 2.2S21.8 6.6 21.8 12 17.4 21.8 12 21.8zM12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6c1.8 1 3.8 1.5 5.8 1.5 6.6 0 12-5.4 12-12S18.6 0 12 0z"/></svg>'


def page(fname, title, desc, body):
    import re
    m = re.search(r'class="hero-media" data-bg="([^"]+)"', body)
    preload = ""
    if m:
        u = m.group(1)
        preload = (f'\n<link rel="preload" as="image" href="{u.replace("w=2200","w=800").replace("q=80","q=70")}" media="(max-width: 734px)" fetchpriority="high">'
                   f'\n<link rel="preload" as="image" href="{u.replace("w=2200","w=1600")}" media="(min-width: 735px)" fetchpriority="high">')
    links = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV
    )
    html = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#161617">
<meta name="format-detection" content="telephone=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="VAGMER">
<link rel="manifest" href="manifest.webmanifest">{preload}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/logo.svg">
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="nav" role="navigation" aria-label="Ana menü">
  <div class="container">
    <a class="brand" href="index.html"><img src="assets/img/logo.svg" alt="" width="28" height="28">VAGMER</a>
    <button class="nav-toggle" aria-label="Menüyü aç" aria-expanded="false"><span></span><span></span></button>
    <ul class="nav-links">{links}<li><a class="nav-cta" href="iletisim.html#randevu">Randevu Al</a></li></ul>
  </div>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html"><img src="assets/img/logo.svg" alt="" width="24" height="24">VAGMER</a>
        <p>Motor mekanik ve VAG grubu araçlarda uzman oto servis. Doğru teşhis, şeffaf fiyat, garantili işçilik.</p>
      </div>
      <div><h5>Site</h5><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}</ul></div>
      <div><h5>Hizmetler</h5><ul>
        <li><a href="hizmetler.html#motor">Motor Revizyonu</a></li>
        <li><a href="hizmetler.html#triger">Triger Seti</a></li>
        <li><a href="hizmetler.html#sanziman">DSG Şanzıman</a></li>
        <li><a href="hizmetler.html#diagnostik">Arıza Tespit</a></li>
      </ul></div>
      <div><h5>İletişim</h5><ul>
        <li><a href="tel:{PHONE_HREF}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ADDRESS}</li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>Copyright © <span id="year">2026</span> VAGMER Oto Servis. Tüm hakları saklıdır.</span>
      <span>Volkswagen, Audi, Seat, Škoda ve Porsche ilgili sahiplerinin tescilli markalarıdır.</span>
    </div>
  </div>
</footer>
<nav class="action-bar" aria-label="Hızlı işlemler">
  <a class="ab-call" href="tel:{PHONE_HREF}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>Ara</a>
  <a class="ab-wa" data-wa="Merhaba VAGMER, bilgi almak istiyorum." href="iletisim.html">{WA_SVG}WhatsApp</a>
  <a class="ab-cta" href="iletisim.html#randevu">Randevu al</a>
</nav>
<a class="fab" data-wa="Merhaba VAGMER, bilgi almak istiyorum." href="iletisim.html" aria-label="WhatsApp ile yazın">{WA_SVG}</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(html)


def svc_card(icon, title, text, anchor):
    return f'''<a class="card reveal" href="hizmetler.html#{anchor}" style="color:inherit;text-decoration:none">
  <div class="icon">{ICONS[icon]}</div><h3>{title}</h3><p>{text}</p><span class="link-arrow" style="color:var(--link)">Daha fazla bilgi</span></a>'''

# ---------------- Ana Sayfa ----------------
home = f'''
<section class="hero">
  <div class="hero-media" data-bg="{img('hero', 2200)}"></div>
  <div class="container">
    <p class="eyebrow">VAGMER Oto Servis</p>
    <h1 class="display">Motorunuz.<br>Bizim uzmanlığımız.</h1>
    <p class="lead">Motor mekanikten şanzımana, arıza tespitten periyodik bakıma. Aracınıza fabrika standartlarında, şeffaf ve garantili servis.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="iletisim.html#randevu">Randevu al</a>
      <a class="link-arrow" style="color:var(--link-dark)" href="hizmetler.html">Hizmetleri keşfedin</a>
    </div>
  </div>
</section>

<section class="section center">
  <div class="container narrow reveal">
    <h2 class="headline">Her ses bir şey anlatır.<br><span class="gradient-text">Biz dinlemeyi biliyoruz.</span></h2>
    <p class="lead">VAGMER, Volkswagen grubu araçlarda uzmanlaşmış ekibi ve güncel teşhis cihazlarıyla, sorunun kaynağını ilk seferde bulur. Tahmin yok, gereksiz parça değişimi yok.</p>
  </div>
</section>

<section class="section-sm" style="padding-top:0">
  <div class="container grid grid-2">
    <div class="tile reveal">
      <div class="media" data-bg="{img('engine', 1400)}"></div>
      <h3>Motor Mekanik</h3>
      <p>Revizyon, conta, segman ve silindir kapağı.</p>
      <div class="cta-row"><a class="btn btn-primary" href="hizmetler.html#motor">Daha fazla bilgi</a><a class="btn btn-ghost" href="iletisim.html#randevu">Randevu al</a></div>
    </div>
    <div class="tile reveal">
      <div class="media" data-bg="{img('dark', 1400)}"></div>
      <h3>Arıza Tespit</h3>
      <p>Bilgisayarlı diagnostik, tek seferde doğru teşhis.</p>
      <div class="cta-row"><a class="btn btn-primary" href="hizmetler.html#diagnostik">Daha fazla bilgi</a><a class="btn btn-ghost" href="iletisim.html#randevu">Randevu al</a></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="center reveal">
      <h2 class="headline">Hizmetlerimiz</h2>
      <p class="lead narrow">Aracınızın kalbinden yürüyen aksamına kadar, ihtiyaç duyduğu her şey tek çatı altında.</p>
    </div>
    <div class="grid grid-3" style="margin-top:56px">
      {svc_card("engine", "Motor Revizyonu", "Komple ya da üst/alt revizyon, ölçümlü ve dokümante işçilik.", "motor")}
      {svc_card("chain", "Triger & Zincir", "Triger seti, zincir uzaması ve gergi değişimleri.", "triger")}
      {svc_card("gear", "DSG Şanzıman", "Mekatronik, kavrama seti ve şanzıman yağı değişimi.", "sanziman")}
      {svc_card("pulse", "Arıza Tespit", "Orijinal seviye diagnostik ve canlı veri analizi.", "diagnostik")}
      {svc_card("fan", "Turbo & Enjektör", "Turbo bakımı, enjektör testi ve kalibrasyonu.", "turbo")}
      {svc_card("drop", "Periyodik Bakım", "Üretici onaylı yağ ve filtrelerle bakım.", "bakim")}
    </div>
  </div>
</section>


<section class="section">
  <div class="container split">
    <div class="media ratio-4x3 reveal" data-bg="{img('mech', 1400)}"></div>
    <div class="reveal">
      <p class="eyebrow">Neden VAGMER?</p>
      <h2 class="headline">Şeffaflık,<br>standart donanım.</h2>
      <p class="lead">İşe başlamadan önce net teşhis ve yazılı fiyat. Değişen her parçayı size teslim ederiz.</p>
      <ul class="check-list">
        <li>Uzman ve sertifikalı motor ustaları</li>
        <li>Orijinal ve OEM kalite yedek parça</li>
        <li>Fotoğraflı ve dokümante işlem raporu</li>
        <li>Tüm işçiliklerde 12 ay garanti</li>
      </ul>
    </div>
  </div>
</section>

<section class="section alt center">
  <div class="container reveal">
    <h2 class="headline">VAG grubunda uzman.</h2>
    <p class="lead narrow">Grubun motor ve şanzıman mimarisini yakından tanıyoruz. Diğer marka ve modeller için de hizmet veriyoruz.</p>
    <div class="brands">
      <span class="chip">Volkswagen</span><span class="chip">Audi</span><span class="chip">Seat</span><span class="chip">Škoda</span><span class="chip">Cupra</span><span class="chip">Porsche</span><span class="chip">Diğer markalar</span>
    </div>
  </div>
</section>

<section class="section dark center">
  <div class="container narrow reveal">
    <h2 class="display" style="font-size:clamp(40px,6vw,72px)">Aracınız hazır olduğunda,<br>biz de hazırız.</h2>
    <p class="lead">Online randevu alın, aracınızı zamanında ve eksiksiz teslim alın.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="iletisim.html#randevu">Randevu al</a>
      <a class="btn btn-ghost" data-wa="Merhaba VAGMER, aracım için bilgi almak istiyorum." href="iletisim.html">WhatsApp’tan yazın</a>
    </div>
  </div>
</section>
'''
page("index.html", "VAGMER Oto Servis — Motor Mekanik ve VAG Uzmanı", "VAGMER Oto Servis: motor mekanik, motor revizyonu, triger, DSG şanzıman, arıza tespit ve periyodik bakım. Volkswagen, Audi, Seat, Škoda uzmanı.", home)

# ---------------- Hizmetler ----------------
def svc_section(anchor, eyebrow, title, text, items, key, reverse=False, alt=False):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'''<section id="{anchor}" class="section{' alt' if alt else ''}" style="scroll-margin-top:var(--nav-h)">
  <div class="container split{' reverse' if reverse else ''}">
    <div class="media ratio-4x3 reveal" data-bg="{img(key, 1400)}"></div>
    <div class="reveal">
      <p class="eyebrow">{eyebrow}</p>
      <h2 class="headline">{title}</h2>
      <p class="lead">{text}</p>
      <ul class="check-list">{lis}</ul>
      <div class="cta-row" style="justify-content:flex-start"><a class="btn btn-primary" href="iletisim.html#randevu">Randevu al</a></div>
    </div>
  </div>
</section>'''

services = f'''
<section class="page-hero dark">
  <div class="container narrow reveal">
    <p class="eyebrow">Hizmetler</p>
    <h1 class="display">Hassas işçilik.<br>Her parçada.</h1>
    <p class="lead">Motor mekanikten elektroniğe, aracınızın ihtiyaç duyduğu her şey için uzman ekip ve doğru ekipman.</p>
  </div>
</section>

<section class="section-sm alt">
  <div class="container grid grid-4">
    <a class="card reveal" href="#motor" style="color:inherit;text-decoration:none"><div class="icon">{ICONS['engine']}</div><h3>Motor</h3></a>
    <a class="card reveal" href="#triger" style="color:inherit;text-decoration:none"><div class="icon">{ICONS['chain']}</div><h3>Triger</h3></a>
    <a class="card reveal" href="#sanziman" style="color:inherit;text-decoration:none"><div class="icon">{ICONS['gear']}</div><h3>Şanzıman</h3></a>
    <a class="card reveal" href="#diagnostik" style="color:inherit;text-decoration:none"><div class="icon">{ICONS['pulse']}</div><h3>Diagnostik</h3></a>
  </div>
</section>

{svc_section("motor", "Motor Mekanik", "Motor revizyonu.", "Yağ yakma, kompresyon kaybı, conta yakma veya yüksek kilometre. Motorunuzu söküp ölçerek, ihtiyaç kadar müdahale ediyoruz.", ["Komple, üst ve alt motor revizyonu", "Silindir kapağı planyası ve conta değişimi", "Segman, piston, kol yatağı ve ana yatak", "Supap, supap lastiği ve kam mili işlemleri", "Yağ ve su kaçağı tespiti ve onarımı"], "engine")}
{svc_section("triger", "Zamanlama Sistemi", "Triger seti ve zincir.", "Zamanında yapılmayan triger değişimi motorun en pahalı arızasına dönüşebilir. Kayış ya da zincir, doğru aparat ve doğru tork ile.", ["Triger kayışı, gergi ve devirdaim seti", "Triger zinciri uzama ölçümü ve değişimi", "Eksantrik ayar ve faz kontrolü", "Orijinal zamanlama aparatlarıyla montaj"], "tools", reverse=True, alt=True)}
{svc_section("sanziman", "Şanzıman", "DSG ve otomatik şanzıman.", "Vuruntu, titreme, geç vites geçişi veya uyarı lambası. DSG ve otomatik şanzımanlarda teşhisten onarıma çözüm.", ["DSG kavrama (debriyaj) seti değişimi", "Mekatronik ünite arıza tespiti ve onarımı", "Şanzıman yağı ve filtre değişimi", "Adaptasyon ve temel ayar işlemleri"], "car2")}
{svc_section("diagnostik", "Elektronik", "Bilgisayarlı arıza tespit.", "Güncel diagnostik yazılımları ve canlı veri analizi ile arızanın kaynağına ilk seferde ulaşıyoruz.", ["Tüm modüllerde arıza kodu okuma ve silme", "Canlı veri ve sensör analizi", "Kodlama, adaptasyon ve servis sıfırlama", "Elektrik ve kablo tesisatı arızaları"], "dark", reverse=True, alt=True)}
{svc_section("turbo", "Performans & Verim", "Turbo ve enjektör.", "Güç kaybı, siyah duman, ıslık sesi ya da yüksek yakıt tüketimi. Turbo ve yakıt sistemini test ederek çözüyoruz.", ["Turbo kontrolü, bakımı ve değişimi", "Enjektör testi, temizliği ve kodlaması", "EGR ve DPF temizliği", "Emme ve egzoz sistemi kontrolleri"], "car3")}
{svc_section("bakim", "Bakım", "Periyodik bakım.", "Üretici bakım takvimine uygun, onaylı yağ ve filtrelerle. Aracınızın değerini ve garantisini koruyun.", ["Üretici onaylı motor yağı ve filtre değişimi", "Hava, polen ve yakıt filtreleri", "Fren sistemi ve balata kontrolü", "Süspansiyon ve yürüyen aksam kontrolü", "Antifriz, fren hidroliği ve sıvı seviyeleri"], "car1", reverse=True, alt=True)}

<section class="section dark">
  <div class="container">
    <div class="center reveal"><h2 class="headline">Nasıl çalışıyoruz?</h2><p class="lead narrow">Basit, şeffaf ve öngörülebilir bir süreç.</p></div>
    <div class="grid grid-4 steps" style="margin-top:64px">
      <div class="step reveal"><h3>Randevu</h3><p>Online ya da telefonla size uygun zamanı seçin.</p></div>
      <div class="step reveal"><h3>Teşhis</h3><p>Aracınızı inceler, sorunu ve çözümünü açıkça anlatırız.</p></div>
      <div class="step reveal"><h3>Onay</h3><p>Yazılı fiyat teklifiniz onaylanmadan işleme başlamayız.</p></div>
      <div class="step reveal"><h3>Teslim</h3><p>Test sürüşü sonrası, değişen parçalarla birlikte teslim.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container narrow">
    <h2 class="headline center reveal">Sıkça sorulan sorular</h2>
    <div class="faq reveal">
      <details><summary>Triger setini ne zaman değiştirmeliyim?</summary><p>Motor tipine göre genellikle 60.000–120.000 km veya 4–5 yıl aralığındadır. Aracınızın şasi numarasıyla üretici takvimini kontrol edip size net bilgi veririz.</p></details>
      <details><summary>Arıza tespiti ne kadar sürer?</summary><p>Standart bilgisayarlı arıza tespiti çoğunlukla 30–60 dakika sürer. Detaylı mekanik inceleme gerekiyorsa süreyi önceden bildiririz.</p></details>
      <details><summary>Orijinal parça mı kullanıyorsunuz?</summary><p>Tercihinize göre orijinal (OE) ya da OEM kalite parça kullanıyoruz. Her iki seçeneğin fiyatını da teklifimizde ayrı ayrı belirtiyoruz.</p></details>
      <details><summary>İşçiliğe garanti veriyor musunuz?</summary><p>Evet. Yaptığımız tüm işçiliklere 12 ay garanti veriyoruz. Parça garantisi üretici koşullarına tabidir.</p></details>
      <details><summary>Sadece VAG grubu araçlara mı bakıyorsunuz?</summary><p>Uzmanlık alanımız Volkswagen, Audi, Seat, Škoda ve Porsche olsa da, diğer marka araçlara da motor mekanik ve bakım hizmeti veriyoruz.</p></details>
    </div>
  </div>
</section>
'''
page("hizmetler.html", "Hizmetler — VAGMER Oto Servis", "Motor revizyonu, triger seti, DSG şanzıman, bilgisayarlı arıza tespit, turbo, enjektör ve periyodik bakım hizmetleri.", services)

# ---------------- Hakkımızda ----------------
about = f'''
<section class="hero" style="min-height:78vh">
  <div class="hero-media" data-bg="{img('mech2', 2200)}"></div>
  <div class="container">
    <p class="eyebrow">Hakkımızda</p>
    <h1 class="display">Ustalık,<br>tutkuyla başlar.</h1>
    <p class="lead">Motorlara olan merakla başlayan yolculuğumuz, bugün binlerce aracın güvenle yola devam etmesini sağlıyor.</p>
  </div>
</section>

<section class="section center">
  <div class="container narrow reveal">
    <h2 class="headline">Bizim hikâyemiz.</h2>
    <p class="lead">VAGMER, Volkswagen grubu araçlara duyulan tutkuyla kuruldu. Amacımız basitti: Aracını bize emanet eden herkese, yetkili servis kalitesini daha ulaşılabilir ve daha şeffaf bir deneyimle sunmak.</p>
    <p class="lead">Bugün deneyimli usta kadromuz, güncel teşhis donanımımız ve titiz çalışma prensiplerimizle, her aracı kendi aracımız gibi ele alıyoruz.</p>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="center reveal"><h2 class="headline">Değerlerimiz</h2></div>
    <div class="grid grid-3" style="margin-top:56px">
      <div class="card reveal"><div class="icon">{ICONS['eye']}</div><h3>Şeffaflık</h3><p>Ne yaptığımızı, neden yaptığımızı ve ne kadar tuttuğunu işe başlamadan önce açıkça paylaşırız.</p></div>
      <div class="card reveal"><div class="icon">{ICONS['shield']}</div><h3>Güven</h3><p>Değişen parçaları size teslim eder, tüm işçiliklerimizi 12 ay garanti altına alırız.</p></div>
      <div class="card reveal"><div class="icon">{ICONS['chip']}</div><h3>Teknoloji</h3><p>Güncel diagnostik yazılımları ve özel servis aparatlarıyla, fabrika standartlarında çalışırız.</p></div>
      <div class="card reveal"><div class="icon">{ICONS['clock']}</div><h3>Zamanında teslim</h3><p>Verdiğimiz teslim süresine sadık kalır, gecikme durumunda sizi önceden bilgilendiririz.</p></div>
      <div class="card reveal"><div class="icon">{ICONS['tag']}</div><h3>Adil fiyat</h3><p>Gereksiz parça değişimi önermeyiz. Sadece ihtiyacınız olanı, doğru fiyata yaparız.</p></div>
      <div class="card reveal"><div class="icon">{ICONS['disc']}</div><h3>Titizlik</h3><p>Her işlemi ölçer, kontrol eder ve test sürüşüyle doğrulayarak tamamlarız.</p></div>
    </div>
  </div>
</section>


<section class="section">
  <div class="container">
    <div class="center reveal"><h2 class="headline">Atölyemizden.</h2><p class="lead narrow">Temiz, düzenli ve donanımlı bir çalışma ortamı.</p></div>
    <div class="gallery" style="margin-top:56px">
      <div class="media ratio-16x9 wide reveal" data-bg="{img('engine', 1600)}"></div>
      <div class="media ratio-3x4 reveal" style="aspect-ratio:auto" data-bg="{img('tools', 900)}"></div>
      <div class="media ratio-1x1 reveal" data-bg="{img('car4', 900)}"></div>
      <div class="media ratio-1x1 reveal" data-bg="{img('car5', 900)}"></div>
      <div class="media ratio-1x1 reveal" data-bg="{img('car1', 900)}"></div>
    </div>
  </div>
</section>

<section class="section alt center">
  <div class="container narrow reveal">
    <h2 class="headline">Tanışmaya hazır mısınız?</h2>
    <p class="lead">Atölyemize uğrayın, bir çay eşliğinde aracınızı birlikte değerlendirelim.</p>
    <div class="cta-row"><a class="btn btn-primary" href="iletisim.html#randevu">Randevu al</a><a class="link-arrow" href="iletisim.html">Yol tarifi</a></div>
  </div>
</section>
'''
page("hakkimizda.html", "Hakkımızda — VAGMER Oto Servis", "VAGMER Oto Servis'in hikâyesi, değerleri ve atölyesi. Şeffaf, güvenilir ve garantili motor mekanik servisi.", about)

# ---------------- İletişim ----------------
contact = f'''
<section class="page-hero alt">
  <div class="container narrow reveal">
    <p class="eyebrow">İletişim</p>
    <h1 class="display">Bize ulaşın.</h1>
    <p class="lead">Sorularınız, fiyat teklifi veya randevu için buradayız.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-3">
    <a class="card card-dark reveal" href="tel:{PHONE_HREF}" style="text-decoration:none"><div class="icon">{ICONS['phone']}</div><h3>Telefon</h3><p>{PHONE}</p></a>
    <a class="card card-dark reveal" data-wa="Merhaba VAGMER, bilgi almak istiyorum." href="#" style="text-decoration:none"><div class="icon">{ICONS['chat']}</div><h3>WhatsApp</h3><p>Hızlı yanıt için mesaj gönderin.</p></a>
    <a class="card card-dark reveal" href="mailto:{EMAIL}" style="text-decoration:none"><div class="icon">{ICONS['mail']}</div><h3>E-posta</h3><p>{EMAIL}</p></a>
  </div>
</section>

<section id="randevu" class="section alt" style="scroll-margin-top:var(--nav-h)">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <p class="eyebrow">Online Randevu</p>
      <h2 class="headline">Randevunuzu<br>şimdi oluşturun.</h2>
      <p class="lead">Formu doldurun, talebiniz WhatsApp üzerinden bize ulaşsın. En kısa sürede dönüş yapıp randevunuzu onaylayalım.</p>
      <table class="hours" aria-label="Çalışma saatleri">
        <tr><td>Pazartesi – Cuma</td><td>08:30 – 19:00</td></tr>
        <tr><td>Cumartesi</td><td>09:00 – 17:00</td></tr>
        <tr><td>Pazar</td><td>Kapalı</td></tr>
      </table>
    </div>
    <form id="randevu-form" class="form reveal" autocomplete="on">
      <div class="row">
        <div class="field"><label for="ad">Ad Soyad</label><input id="ad" name="ad" autocomplete="name" autocapitalize="words" enterkeyhint="next" required></div>
        <div class="field"><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" inputmode="tel" autocomplete="tel" enterkeyhint="next" required></div>
      </div>
      <div class="row">
        <div class="field"><label for="marka">Marka</label>
          <select id="marka" name="marka" required>
            <option>Volkswagen</option><option>Audi</option><option>Seat</option><option>Škoda</option><option>Cupra</option><option>Porsche</option><option>Diğer</option>
          </select></div>
        <div class="field"><label for="model">Model / Yıl</label><input id="model" name="model" autocomplete="off" enterkeyhint="next"></div>
      </div>
      <div class="row">
        <div class="field"><label for="hizmet">Hizmet</label>
          <select id="hizmet" name="hizmet">
            <option>Arıza Tespit</option><option>Motor Revizyonu</option><option>Triger Seti</option><option>DSG / Şanzıman</option><option>Turbo / Enjektör</option><option>Periyodik Bakım</option><option>Diğer</option>
          </select></div>
        <div class="field"><label for="tarih">Tercih edilen tarih</label><input id="tarih" name="tarih" type="date"></div>
      </div>
      <div class="field"><label for="mesaj">Aracınızdaki sorun</label><textarea id="mesaj" name="mesaj" enterkeyhint="send"></textarea></div>
      <button class="btn btn-primary" type="submit">Randevu talebi gönder</button>
      <p id="form-status" class="form-status" role="status"></p>
      <p class="form-note">Gönder’e bastığınızda talebiniz WhatsApp’ta hazır bir mesaj olarak açılır.</p>
    </form>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Konum</p>
      <h2 class="headline">Atölyemiz.</h2>
      <div class="info" style="margin-top:28px">
        <div class="info-item"><div><h4>Adres</h4><p>{ADDRESS}</p></div></div>
        <div class="info-item"><div><h4>Telefon</h4><a href="tel:{PHONE_HREF}">{PHONE}</a></div></div>
        <div class="info-item"><div><h4>E-posta</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      </div>
    </div>
    <iframe class="map reveal" title="VAGMER konum" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://www.google.com/maps?q=Istanbul&z=11&output=embed"></iframe>
  </div>
</section>
'''
page("iletisim.html", "İletişim ve Randevu — VAGMER Oto Servis", "VAGMER Oto Servis iletişim bilgileri, çalışma saatleri ve online randevu formu.", contact)

notfound = '''
<section class="page-hero dark" style="min-height:70vh;display:flex;align-items:center">
  <div class="container narrow center">
    <p class="eyebrow">404</p>
    <h1 class="display">Bu sayfa yolda kaldı.</h1>
    <p class="lead">Aradığınız sayfa bulunamadı. Ama aracınızı yolda bırakmayız.</p>
    <div class="cta-row"><a class="btn btn-primary" href="index.html">Ana sayfaya dön</a></div>
  </div>
</section>'''
page("404.html", "Sayfa bulunamadı — VAGMER", "Sayfa bulunamadı.", notfound)
print("ok")
