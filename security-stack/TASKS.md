# Security stack — task tracker

The numbered tasks (**T01–T17**) came from the chat backlog (defense-in-depth / OpenClaw hardening). This file is the **authoritative status** for what is in-repo vs still manual.

Legend: **Done** = implemented in this repo · **Stub** = placeholder / needs your env · **Manual** = runbooks only · **Out of scope** = not bundled here

| ID | Task | Status | Location / notes |
|----|------|--------|-------------------|
| T01 | Docker foundation (Postgres, Redis, OpenBao) | **Done** | `docker/docker-compose.yml` — Postgres/Redis **no host ports**; SafeLine via `scripts/bootstrap-safeline.sh` |
| T02 | OpenBao config + unseal | **Done** | `config/openbao/config.hcl.template`, `scripts/render-openbao-config.sh`, `config/openbao/unseal.sh`, `scripts/openbao_production.sh` |
| T03 | Nginx TLS reverse proxy | **Done** | `config/nginx/openclaw.conf`, `config/nginx/http_snippets/01-openclaw-rate-limit.conf` |
| T04 | iptables / firewall baseline | **Done** | `scripts/iptables_rules.sh` (+ metadata egress drop, optional `ALLOW_PUBLIC_HTTP`) |
| T05 | Host hardening (SSH, fail2ban, sysctl) | **Done** | `scripts/secure_host.sh` |
| T06 | Wazuh agent | **Done** | `config/wazuh/ossec.conf`, `scripts/install_wazuh_agent.sh` |
| T07 | OpenClaw Docker sandbox | **Done** | `docker/docker-compose.openclaw.yml` (no `DAC_OVERRIDE`) |
| T08 | OpenClaw security config | **Done** | `config/openclaw/config.yaml` |
| T09 | Rules of the Claw | **Done** | `config/openclaw/rules_of_the_claw.yaml` (+ awk/sed/openssl/git patterns) |
| T10 | AgentWard / prompt guards | **Done** | `config/openclaw/agentward_plugin.py`, `config/agentward/guardrails.yaml` (+ `SSRFProtection`) |
| T11 | Memory guard / RAG poisoning | **Done** | `config/openclaw/memory_guard.py` (user isolation, TTL, cleanup) |
| T12 | Deploy Infisical | **Stub** | `scripts/deploy_infisical.sh` — points to upstream docs |
| T13 | Migrate secrets off `.env` | **Stub** | `scripts/migrate_secrets.py` — verify Infisical API for your version |
| T14 | Encrypt memory / keys via OpenBao | **Partial** | Declared in `config/openclaw/config.yaml`; **wire in your OpenClaw runtime** |
| T15 | Wazuh manager + TheHive IR | **Out of scope** | Deploy separately; agent side only in-repo |
| T16 | Log aggregation (Loki) | **Done (minimal)** | `docker/docker-compose.monitoring.yml`, `monitoring/loki-config.yaml` |
| T17 | Alert rules | **Done (example)** | `monitoring/alert_rules.yaml` — tune LogQL + labels |

## Exposure audit (post-chat)

| Item | Status |
|------|--------|
| Remove Postgres/Redis host ports | **Done** |
| Block cloud metadata egress | **Done** (iptables) |
| Security audit script | **Done** | `scripts/security_audit.sh` |
| Remediation checklist | **Done** | `scripts/remediate_audit.sh`, `docs/EXPOSURE_AUDIT.md` |
| Illustrative air-gap compose | **Done** | `docker/docker-compose.secure-minimal.yml` |

## What’s left for you (can’t be “finished” without your environment)

1. **Run** `render-openbao-config.sh`, `docker compose up`, **init/unseal OpenBao** on a real host.  
2. **T12–T13**: Replace stubs with your Infisical deployment + verified API migration.  
3. **T15**: If required, add Wazuh manager + TheHive (or SIEM of choice) — separate compose/ops.  
4. **T14**: Connect memory encryption and dynamic secrets to **actual** OpenClaw / Infisical / OpenBao.  
5. **Git remote**: `git remote add origin …` and push when you create the GitHub/GitLab repo.

## Optional next session

- [ ] CI workflow: `docker compose -f docker/docker-compose.yml config` + shellcheck on `scripts/*.sh`  
- [ ] Replace `migrate_secrets.py` with Infisical SDK version you run in prod  
- [ ] Add TheHive / Wazuh manager reference compose (if you standardize on one stack)
