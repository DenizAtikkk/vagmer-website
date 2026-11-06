#!/usr/bin/env bash
# VAGMER web sitesi kurulum / güncelleme (Ubuntu)
# Sunucudaki diğer projelere dokunmaz: kendi portunda (varsayılan 8090) yayınlar.
# Kullanım:  bash install.sh            (port 8090)
#            PORT=8095 bash install.sh  (başka port)
set -euo pipefail

PORT="${PORT:-8090}"
REPO="https://github.com/DenizAtikkk/vagmer-website.git"
BRANCH="claude/vagmer-auto-service-website-mxdwfq"
SRC="/opt/vagmer-website"
WEB="/var/www/vagmer"

export DEBIAN_FRONTEND=noninteractive
command -v nginx >/dev/null 2>&1 || { apt-get update -y; apt-get install -y nginx; }
command -v git   >/dev/null 2>&1 || apt-get install -y git
command -v rsync >/dev/null 2>&1 || apt-get install -y rsync

# Kaynak kodu al / güncelle
if [ -d "$SRC/.git" ]; then
  git -C "$SRC" fetch --depth 1 origin "$BRANCH"
  git -C "$SRC" reset --hard FETCH_HEAD
else
  git clone --branch "$BRANCH" --depth 1 "$REPO" "$SRC"
fi

# Port başka bir uygulama tarafından kullanılıyor mu? (bizim nginx hariç)
if ss -ltnp "( sport = :$PORT )" | grep -v nginx | grep -q LISTEN; then
  echo "HATA: $PORT portu başka bir uygulama tarafından kullanılıyor."
  ss -ltnp "( sport = :$PORT )"
  echo "Başka port deneyin, örn:  PORT=8095 bash $SRC/deploy/install.sh"
  exit 1
fi

# 80 portu nginx dışında bir uygulamadaysa, nginx'in varsayılan sitesi açılamaz -> sadece onu devre dışı bırak
if ss -ltnp '( sport = :80 )' | grep LISTEN | grep -vq nginx; then
  if [ -L /etc/nginx/sites-enabled/default ]; then
    echo "Not: 80 portu başka bir uygulamada; nginx'in boş varsayılan sitesi devre dışı bırakılıyor."
    rm -f /etc/nginx/sites-enabled/default
  fi
fi

# Dosyaları yayın klasörüne kopyala
mkdir -p "$WEB"
rsync -a --delete --exclude ".git" --exclude "deploy" --exclude "README.md" "$SRC/" "$WEB/"
chown -R www-data:www-data "$WEB"

# nginx site ayarı
sed "s/__PORT__/$PORT/g" "$SRC/deploy/nginx-vagmer.conf" > /etc/nginx/sites-available/vagmer
ln -sf /etc/nginx/sites-available/vagmer /etc/nginx/sites-enabled/vagmer

nginx -t
systemctl enable nginx >/dev/null 2>&1 || true
if systemctl is-active --quiet nginx; then
  systemctl reload nginx
else
  systemctl restart nginx || { journalctl -u nginx --no-pager -n 20; exit 1; }
fi

# Güvenlik duvarı açıksa portu aç
if command -v ufw >/dev/null 2>&1 && ufw status | grep -q "Status: active"; then
  ufw allow "$PORT"/tcp
fi

IP=$(curl -s -4 --max-time 5 https://ifconfig.me || hostname -I | awk '{print $1}')
echo
echo "=============================================="
echo " VAGMER sitesi yayında:  http://$IP:$PORT"
echo "=============================================="
