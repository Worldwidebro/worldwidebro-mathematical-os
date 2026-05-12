#!/usr/bin/env bash
# T05 — Ubuntu 22.04/24.04 host hardening (run as root). Review AllowUsers.
set -euo pipefail

echo "=== Host hardening (SSH drop-in, fail2ban, auditd, sysctl) ==="

ALLOW_USER="${SUDO_USER:-${ADMIN_USER:-}}"
if [[ -z "$ALLOW_USER" ]]; then
  echo "Set SUDO_USER by running with sudo, or export ADMIN_USER=your_linux_username" >&2
  exit 1
fi

install -d -m 0755 /etc/ssh/sshd_config.d
cat >/etc/ssh/sshd_config.d/99-security-stack.conf <<EOF
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
MaxSessions 5
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers ${ALLOW_USER}
Protocol 2
X11Forwarding no
AllowTcpForwarding no
EOF

if sshd -t; then
  systemctl reload ssh || systemctl reload sshd
else
  echo "sshd -t failed; not reloading ssh" >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y fail2ban auditd audispd-plugins lynis

install -d -m 0755 /etc/fail2ban/jail.d
cat >/etc/fail2ban/jail.d/security-stack.local <<'EOF'
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true
port = ssh
logpath = %(sshd_log)s
maxretry = 3
EOF

systemctl enable --now fail2ban

auditctl -w /etc/passwd -p wa -k identity || true
auditctl -w /etc/shadow -p wa -k identity || true
auditctl -w /etc/sudoers -p wa -k privilege || true
auditctl -w /opt/openclaw -p wa -k openclaw || true

SYSCTL_FILE=/etc/sysctl.d/99-security-stack.conf
cat >"$SYSCTL_FILE" <<'EOF'
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.tcp_timestamps = 0
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
kernel.randomize_va_space = 2
# Reduce swap pressure (does not remove secrets already in swap; consider encrypted swap or swapoff)
vm.swappiness = 10
EOF
sysctl --system

if [[ "${DISABLE_SWAP:-0}" == "1" ]]; then
  echo "DISABLE_SWAP=1: running swapoff -a (review OOM risk)"
  swapoff -a || true
fi

lynis audit system --quick || true

echo "=== Done. Review /etc/ssh/sshd_config.d/99-security-stack.conf and Lynis report ==="
