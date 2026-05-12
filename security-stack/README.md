# Security stack (T01–T17 templates)

**Task status:** see **[TASKS.md](TASKS.md)** for T01–T17 and exposure-audit checklist.

Production-oriented **templates** for defense-in-depth around OpenClaw-class agents. Paths match:

```text
security-stack/
├── docker/
├── config/
├── scripts/
├── monitoring/
├── docs/
└── safeline/          # created by scripts/bootstrap-safeline.sh
```

## Quick start (OpenBao + Postgres + Redis)

```bash
cd docker
cp .env.example .env
# Edit .env — use URL-safe DB password for OpenBao’s Postgres URL

cd ..
chmod +x scripts/*.sh
./scripts/render-openbao-config.sh   # requires envsubst (brew install gettext)
cd docker
docker compose up -d
```

Initialize / unseal OpenBao:

```bash
docker exec -it openbao bao operator init
docker exec -it openbao bao operator unseal
# See config/openbao/unseal.sh for key-file pattern
```

## SafeLine WAF

Do **not** rely on a single `chaitin/safeline-ce` image. Install vendor compose:

```bash
./scripts/bootstrap-safeline.sh
```

## Nginx

Include `config/nginx/http_snippets/01-openclaw-rate-limit.conf` inside `http {}`, then enable `config/nginx/openclaw.conf` (adjust `server_name` + TLS paths).

## Linux-only scripts

`scripts/iptables_rules.sh` and `scripts/secure_host.sh` target **Linux** hosts (not macOS).

## Paste status

Your message truncated **T11** mid-line and did not include **full T12–T17** prose. This repo still contains:

- T12: `scripts/deploy_infisical.sh` (pointer stub)
- T13: `scripts/migrate_secrets.py` (API stub — verify Infisical version)
- T14: AES memory encryption is referenced in `config/openclaw/config.yaml` (runtime-specific)
- T15: Wazuh manager + TheHive — not bundled (deploy separately)
- T16: `docker/docker-compose.monitoring.yml` + `monitoring/loki-config.yaml`
- T17: `monitoring/alert_rules.yaml` (example LogQL)

Send the remaining paste to replace stubs / extend rules.

## Exposure audit & remediation

See [docs/EXPOSURE_AUDIT.md](docs/EXPOSURE_AUDIT.md). Quick checks:

```bash
chmod +x scripts/security_audit.sh scripts/remediate_audit.sh scripts/openbao_production.sh
sudo ./scripts/security_audit.sh
./scripts/remediate_audit.sh   # prints checklist + stack reload hints
```

After changing Postgres/Redis exposure, recreate containers:

```bash
cd docker && docker compose up -d --force-recreate
```
