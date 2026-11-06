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
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
  }

  // Görseller: data-bg ile tembel yükleme. Görsel yüklenemezse koyu degrade kalır.
  function loadBg(el) {
    var src = el.getAttribute("data-bg");
    if (!src) return;
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

  // Yıl
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
