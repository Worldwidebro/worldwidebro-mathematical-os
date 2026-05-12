#!/usr/bin/env bash
# T06 — Wazuh agent install (Ubuntu/Debian). Set WAZUH_MANAGER_IP before running.
set -euo pipefail

WAZUH_MANAGER_IP="${WAZUH_MANAGER_IP:?export WAZUH_MANAGER_IP}"

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y curl gnupg

install -d -m 0755 /usr/share/keyrings
curl -sSL https://packages.wazuh.com/key/GPG-KEY-WAZUH |
  gpg --dearmor -o /usr/share/keyrings/wazuh.gpg
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" \
  >/etc/apt/sources.list.d/wazuh.list

apt-get update -y
apt-get install -y wazuh-agent

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONF_SRC="${REPO_ROOT}/config/wazuh/ossec.conf"
CONF_DST="/var/ossec/etc/ossec.conf"

if [[ ! -f "$CONF_SRC" ]]; then
  echo "Missing $CONF_SRC" >&2
  exit 1
fi

sed "s/WAZUH_MANAGER_IP/${WAZUH_MANAGER_IP}/g" "$CONF_SRC" >"$CONF_DST"

systemctl enable --now wazuh-agent
systemctl restart wazuh-agent

echo "Wazuh agent configured against ${WAZUH_MANAGER_IP}"
