# VAGMER Oto Servis — Web Sitesi

Apple tasarım prensipleriyle hazırlanmış, çok sayfalı statik tanıtım sitesi.

**Sayfalar:** Ana Sayfa (`index.html`), Hizmetler (`hizmetler.html`), Hakkımızda (`hakkimizda.html`), İletişim & Randevu (`iletisim.html`), 404.

## Sunucuya kurulum (Ubuntu)

Sunucuda root olarak:

```bash
curl -fsSL https://raw.githubusercontent.com/DenizAtikkk/vagmer-website/claude/vagmer-auto-service-website-mxdwfq/deploy/install.sh | bash
```

Site nginx ile **8090 portunda** yayınlanır (sunucudaki diğer projelere dokunmaz): `http://SUNUCU_IP:8090`. Farklı port için: `PORT=8095 bash deploy/install.sh`. Güncellemek için aynı komutu tekrar çalıştırın.

## Düzenlenecek bilgiler

- Telefon, e-posta, adres: `index.html`, `hizmetler.html`, `hakkimizda.html`, `iletisim.html` (alt bilgi ve iletişim sayfası)
- WhatsApp numarası: `assets/js/main.js` içindeki `CONFIG.whatsapp`
- Harita: `iletisim.html` içindeki iframe `q=` parametresi
- Görseller: Unsplash stok fotoğrafları (yüklenemezse koyu degrade gösterilir)
