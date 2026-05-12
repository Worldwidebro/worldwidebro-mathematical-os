#!/usr/bin/env bash
# Production OpenBao init checklist (run once per cluster; never commit key material).
set -euo pipefail

export BAO_ADDR="${BAO_ADDR:-http://127.0.0.1:8200}"

echo "=== OpenBao production bootstrap ==="
echo "Prerequisites:"
echo "  - config.hcl has NO dev tokens; storage is PostgreSQL/file as appropriate."
echo "  - TLS enabled or Bao only on loopback / private network."
echo ""

if ! command -v bao >/dev/null 2>&1; then
  echo "Install OpenBao CLI or: docker exec -it openbao bao ..." >&2
  exit 1
fi

echo "1) Initialize (example: 5 shares, threshold 3). Output MUST go to split offline storage:"
echo "     bao operator init -key-shares=5 -key-threshold=3"
echo ""
echo "2) Unseal with at least threshold distinct operators:"
echo "     bao operator unseal"
echo ""
echo "3) Revoke any bootstrap token; use AppRole / OIDC for apps."
echo ""
echo "4) Enable engines (after unseal):"
echo "     bao secrets enable -path=secret kv-v2"
echo "     bao auth enable approle"
echo ""
echo "Do NOT store unseal keys on the same volume as OpenBao data."
echo "=== End checklist ==="
