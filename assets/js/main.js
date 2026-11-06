/* VAGMER — site interactions */
(function () {
  // İşletme bilgileri — tek yerden güncelleyin
  var CONFIG = {
    whatsapp: "905000000000" // Başında + olmadan, ülke koduyla (örn. 905321234567)
  };

  // Mobil menü
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      setMenu(!nav.classList.contains("open"));
    });
    nav.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    window.addEventListener("resize", function () { if (window.innerWidth > 820) setMenu(false); });
  }
  function setMenu(open) {
    nav.classList.toggle("open", open);
    document.body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
  }

  // Görseller: data-bg ile tembel yükleme. Görsel yüklenemezse koyu degrade kalır.
  function loadBg(el) {
    var src = el.getAttribute("data-bg");
    if (!src) return;
    // Ekran genişliği ve piksel yoğunluğuna göre uygun boyutta görsel iste
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = Math.ceil((el.clientWidth || window.innerWidth) * dpr / 200) * 200;
    w = Math.max(400, Math.min(w, 2400));
    if (el.classList.contains("hero-media")) w = window.innerWidth < 735 ? 800 : 1600; // <head> preload ile aynı
    src = src.replace(/([?&])w=\d+/, "$1w=" + w);
    if (window.innerWidth < 735) src = src.replace(/q=\d+/, "q=70");
    var img = new Image();
    img.onload = function () { el.style.backgroundImage = "url('" + src + "')"; };
    img.src = src;
    el.removeAttribute("data-bg");
  }
  var bgs = document.querySelectorAll("[data-bg]");
  if ("IntersectionObserver" in window) {
    var bgObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { loadBg(e.target); bgObs.unobserve(e.target); }
      });
    }, { rootMargin: "400px" });
    bgs.forEach(function (el) { bgObs.observe(el); });
  } else {
    bgs.forEach(loadBg);
  }

  // Kaydırınca beliren içerik
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var rObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); rObs.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { rObs.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // WhatsApp bağlantıları
  document.querySelectorAll("[data-wa]").forEach(function (a) {
    var text = a.getAttribute("data-wa") || "Merhaba VAGMER, bilgi almak istiyorum.";
    a.href = "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(text);
    a.target = "_blank";
    a.rel = "noopener";
  });

  // Randevu formu -> WhatsApp mesajı
  var form = document.getElementById("randevu-form");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var d = new FormData(form);
      var lines = [
        "Merhaba VAGMER, randevu talebim:",
        "Ad Soyad: " + (d.get("ad") || ""),
        "Telefon: " + (d.get("telefon") || ""),
        "Araç: " + (d.get("marka") || "") + " " + (d.get("model") || ""),
        "Hizmet: " + (d.get("hizmet") || ""),
        "Tercih edilen tarih: " + (d.get("tarih") || "-"),
        "Not: " + (d.get("mesaj") || "-")
      ];
      var url = "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(lines.join("\n"));
      var status = document.getElementById("form-status");
      if (status) status.textContent = "Talebiniz WhatsApp üzerinden iletilmek üzere hazırlandı.";
      window.open(url, "_blank", "noopener");
    });
  }

  // Mobil alt çubuk: form görünürken veya klavye açıkken gizle
  var bar = document.querySelector(".action-bar");
  if (bar) {
    var hideFor = document.querySelectorAll("#randevu-form, .footer");
    var visible = new Set();
    if ("IntersectionObserver" in window && hideFor.length) {
      var bObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { e.isIntersecting ? visible.add(e.target) : visible.delete(e.target); });
        bar.classList.toggle("hide", visible.size > 0);
      });
      hideFor.forEach(function (el) { bObs.observe(el); });
    }
    document.addEventListener("focusin", function (e) {
      if (e.target.matches("input, textarea, select")) bar.classList.add("hide");
    });
    document.addEventListener("focusout", function () {
      if (!visible.size) bar.classList.remove("hide");
    });
  }

  // Yıl
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
