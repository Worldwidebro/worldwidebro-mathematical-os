#!/usr/bin/env bash
# T04 — Linux iptables baseline (run as root). Review before production.
set -euo pipefail

ADMIN_SSH_SOURCE="${ADMIN_SSH_SOURCE:?set ADMIN_SSH_SOURCE to your admin IPv4/32 or CIDR}"

iptables -F
iptables -X
iptables -t nat -F
iptables -t mangle -F

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Cloud metadata / link-local SSRF hardening (host + containers using host net)
iptables -A OUTPUT -d 169.254.169.254 -j DROP
iptables -A OUTPUT -d 169.254.170.2 -j DROP

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# SSH: prefer locking to admin source; fallback accepts from anywhere if you set 0.0.0.0/0 (not recommended)
if [[ "$ADMIN_SSH_SOURCE" != "0.0.0.0/0" ]]; then
  iptables -A INPUT -p tcp --dport 22 -s "$ADMIN_SSH_SOURCE" -m conntrack --ctstate NEW -j ACCEPT
else
  iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --set
  iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
  iptables -A INPUT -p tcp --dport 22 -j ACCEPT
fi

iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW -m limit --limit 50/minute --limit-burst 100 -j ACCEPT
# Set ALLOW_PUBLIC_HTTP=0 to drop inbound 80 (e.g. ACME DNS-only). Default allows HTTP→HTTPS redirect.
if [[ "${ALLOW_PUBLIC_HTTP:-1}" == "1" ]]; then
  iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
else
  iptables -A INPUT -p tcp --dport 80 -j DROP
fi

iptables -A INPUT -p tcp --dport 3000 -s 127.0.0.1 -j ACCEPT
iptables -A INPUT -p tcp --dport 3000 -j DROP

iptables -A INPUT -p tcp --dport 9443 -s 127.0.0.1 -j ACCEPT

iptables -A INPUT -p tcp --dport 3306 -j DROP
iptables -A INPUT -p tcp --dport 5432 -j DROP
iptables -A INPUT -p tcp --dport 6379 -j DROP
iptables -A INPUT -p tcp --dport 27017 -j DROP

iptables -A INPUT -p icmp -m limit --limit 1/second -j ACCEPT

iptables -A INPUT -m limit --limit 5/min -j LOG --log-prefix "IPTABLES-DROP: " --log-level 4
iptables -A INPUT -j DROP

if command -v iptables-save >/dev/null; then
  mkdir -p /etc/iptables
  iptables-save > /etc/iptables/rules.v4
fi

echo "iptables rules applied. Persist with iptables-persistent (Debian/Ubuntu) or distro equivalent."
