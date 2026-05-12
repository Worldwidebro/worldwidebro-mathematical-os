#!/usr/bin/env bash
# Host-side exposure sweep (Linux). Run with sudo for netstat/ss and log greps.
set -u

echo "=== OPENCLAW / SECURITY-STACK AUDIT ==="

echo "[1] Listening sockets (non-loopback on sensitive ports):"
if command -v ss >/dev/null 2>&1; then
  sudo ss -tulpn 2>/dev/null | grep -E ':(3000|8200|5432|6379|9443|80|443)\b' || true
else
  sudo netstat -tulpn 2>/dev/null | grep -E ':(3000|8200|5432|6379|9443|80|443)' || true
fi

echo ""
echo "[2] Dotenv / key material under /opt /home /root (sample):"
sudo find /opt /home /root -maxdepth 5 \( -name '.env' -o -name '*.pem' -o -name 'id_rsa' \) 2>/dev/null | head -20

echo ""
echo "[3] Docker: openclaw-core capabilities (if exists):"
if docker inspect openclaw-core >/dev/null 2>&1; then
  docker inspect openclaw-core --format '{{json .HostConfig.CapAdd}} {{json .HostConfig.CapDrop}}'
else
  echo "(container not found)"
fi

echo ""
echo "[4] OpenBao seal status:"
if command -v curl >/dev/null 2>&1; then
  curl -fsS --max-time 2 "http://127.0.0.1:8200/v1/sys/seal-status" 2>/dev/null | head -c 400 || echo "(unreachable or not JSON)"
  echo ""
else
  echo "(curl missing)"
fi

echo ""
echo "[5] Metadata endpoint from host (should fail if egress filtered):"
if command -v curl >/dev/null 2>&1; then
  if timeout 2 curl -fsS "http://169.254.169.254/latest/meta-data/" 2>/dev/null; then
    echo "VULNERABLE: metadata reachable from this host"
  else
    echo "OK or blocked (curl failed/timeout)"
  fi
else
  echo "(curl missing)"
fi

echo ""
echo "[6] Possible API keys in OpenClaw logs (sample):"
if [[ -d /var/log/openclaw ]]; then
  sudo grep -R "sk-" /var/log/openclaw/ 2>/dev/null | head -5 || echo "(no matches or empty)"
else
  echo "(no /var/log/openclaw)"
fi

echo ""
echo "=== AUDIT COMPLETE ==="
