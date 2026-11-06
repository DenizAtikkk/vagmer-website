#!/usr/bin/env bash
# VAGMER web sitesi kurulum / güncelleme scripti (Ubuntu)
# Kullanım (sunucuda root olarak):  bash install.sh
set -euo pipefail

REPO="https://github.com/DenizAtikkk/vagmer-website.git"
BRANCH="claude/vagmer-auto-service-website-mxdwfq"
SRC="/opt/vagmer-website"
WEB="/var/www/vagmer"

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y nginx git rsync

if [ -d "$SRC/.git" ]; then
  git -C "$SRC" fetch origin "$BRANCH"
  git -C "$SRC" checkout -B "$BRANCH" "origin/$BRANCH"
else
  git clone --branch "$BRANCH" --depth 1 "$REPO" "$SRC"
fi

mkdir -p "$WEB"
rsync -a --delete --exclude ".git" --exclude "deploy" --exclude "README.md" "$SRC/" "$WEB/"
chown -R www-data:www-data "$WEB"

cp "$SRC/deploy/nginx-vagmer.conf" /etc/nginx/sites-available/vagmer
ln -sf /etc/nginx/sites-available/vagmer /etc/nginx/sites-enabled/vagmer
rm -f /etc/nginx/sites-enabled/default

nginx -t
systemctl enable nginx
systemctl restart nginx

if command -v ufw >/dev/null 2>&1 && ufw status | grep -q "Status: active"; then
  ufw allow 80/tcp
  ufw allow OpenSSH
fi

IP=$(hostname -I | awk '{print $1}')
echo
echo "VAGMER sitesi yayında:  http://$IP  (port 80)"
