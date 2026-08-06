---
name: security-stack/docs/EXPOSURE_AUDIT
title: Exposure audit & remediation
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Exposure audit & remediation

## Already addressed in-repo

| Finding | Mitigation |
|---------|------------|
| Postgres/Redis published on loopback | **Removed** `ports:` from `docker/docker-compose.yml`; only the Docker bridge can reach them |
| Cloud metadata SSRF from host | **iptables OUTPUT** drop to `169.254.169.254` / `169.254.170.2` in `scripts/iptables_rules.sh` |
| Public HTTP fingerprint | **Optional** `ALLOW_PUBLIC_HTTP=0` drops inbound TCP/80 (use DNS ACME or internal-only redirect) |
| OpenBao dev token | **Commented guidance** only; never set `BAO_DEV_*` in production — use `scripts/openbao_production.sh` |
| OpenClaw `DAC_OVERRIDE` | **Not present** in `docker-compose.openclaw.yml` (only `NET_BIND_SERVICE` after `cap_drop: ALL`) |
| Tool bypasses (awk/sed/openssl/git) | **Expanded** `rules_of_the_claw.yaml` tier1 |
| SSRF in fetched URLs | **`SSRFProtection`** in `agentward_plugin.py` |
| Logs leaking secrets | **`log_redactor.py`** `RedactingFilter` |
| Memory isolation / TTL | **`user_id`**, **`expires_at`**, **`get_memories`** in `memory_guard.py` |

## Still your responsibility

- **AppArmor/SELinux** profiles for Docker and nginx (distribution-specific).
- **Swap**: secrets can land in swap. Options: encrypted swap, `swapoff -a` (impacts memory pressure), or `vm.swappiness=0` (hint in `secure_host.sh`).
- **TLS inside Docker network** (mTLS between OpenClaw ↔ OpenBao) if threat model includes local attackers.
- **LUKS** (or cloud volume encryption) for `/var/lib/docker` and DB volumes.
- **SafeLine console (9443)**: bind to VPN or SSH tunnel; strong auth; IP allowlist at nginx or firewall.

## Minimal “air-gap style” OpenClaw

`docker/docker-compose.secure-minimal.yml` is an **illustrative** pattern (`network_mode: none`). Most real OpenClaw deployments need outbound network for LLM APIs; treat that file as a thought experiment unless you proxy via a sidecar.
