#!/usr/bin/env bash
# T12 — Stub: deploy Infisical per official self-host guide (Docker/K8s).
# https://infisical.com/docs/self-hosting/overview
set -euo pipefail

cat <<'EOF'
Infisical is not bundled here (image + migrations change frequently).

Recommended:
  1. Follow Infisical self-host docs; use a dedicated compose or Helm chart.
  2. Store connection URL + service token in OpenBao.
  3. Run scripts/migrate_secrets.py to import existing .env keys.

EOF
exit 0
