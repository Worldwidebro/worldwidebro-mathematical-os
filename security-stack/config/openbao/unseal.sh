#!/usr/bin/env bash
# Run on a host with `bao` CLI and network access to OpenBao (after operator init).
# Never store unseal keys on the same disk as production data without offline splits.

set -euo pipefail

export BAO_ADDR="${BAO_ADDR:-http://127.0.0.1:8200}"

if ! command -v bao >/dev/null 2>&1; then
  echo "bao CLI not found. Install OpenBao client or use: docker exec -it openbao bao ..." >&2
  exit 1
fi

status="$(bao status -format=json 2>/dev/null || true)"
sealed="$(echo "$status" | sed -n 's/.*"sealed":\([a-z]*\).*/\1/p' | head -1)"

if [[ "$sealed" != "true" ]]; then
  echo "OpenBao is not sealed (or not initialized yet). status:"
  bao status || true
  exit 0
fi

if [[ -f "${UNSEAL_KEY_FILE:-}" ]]; then
  echo "Unsealing with key file (single-key dev pattern — use Shamir shards in prod)..."
  bao operator unseal "$(cat "$UNSEAL_KEY_FILE")"
else
  echo "Set UNSEAL_KEY_FILE to a file containing one unseal key, or run:" >&2
  echo "  bao operator unseal" >&2
  exit 1
fi

echo "Post-unseal bootstrap (idempotent — ignore errors if already enabled):"
bao secrets enable -path=secret kv-v2 2>/dev/null || true
bao auth enable approle 2>/dev/null || true

echo "Done. bao status:"
bao status
