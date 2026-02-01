#!/bin/bash
set -e

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <domain> <email>"
    echo "Example: $0 xyz.com admin@xyz.com"
    exit 1
fi

DOMAIN=$1
EMAIL=$2

echo "==> Installing Certbot"
sudo apt-get update
sudo apt-get install -y certbot

echo "==> Obtaining SSL certificate for $DOMAIN"
sudo certbot certonly --standalone -d $DOMAIN --email $EMAIL --agree-tos --non-interactive

echo "==> SSL certificate installed successfully"
sudo ls -la /etc/letsencrypt/live/$DOMAIN/

echo "==> Setting up auto-renewal"
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer

echo "==> Done! Certificate will auto-renew before expiration"