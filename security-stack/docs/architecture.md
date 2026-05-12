# Security stack architecture

Defense-in-depth layers referenced by this repo:

| Layer | Controls in this repo |
|-------|------------------------|
| Physical / Host | `scripts/secure_host.sh`, `scripts/iptables_rules.sh` (Linux) |
| Network | Nginx TLS termination, SafeLine CE (vendor compose), firewall |
| Identity | OpenBao (AppRole/KV patterns in docs; configure in your environment) |
| Compute | Docker hardening, Wazuh syscheck, resource limits |
| Application | OpenClaw config, Rules of the Claw, AgentWard-style guardrails |
| Data | PostgreSQL for OpenBao storage, Infisical migration script (stub) |
| Tooling | Disabled tools / command blocklists in `config/openclaw/config.yaml` |
| Memory | `memory_guard.py` + vector write validation |

## SafeLine WAF

Chaitin publishes **multi-service** SafeLine CE (`compose.yaml` + `.env`), not a single `chaitin/safeline-ce` container. Use:

```bash
./scripts/bootstrap-safeline.sh
```

Then deploy from `./safeline/` per [SafeLine deploy docs](https://docs.waf.chaitin.com/en/GetStarted/Deploy).

## OpenBao

- Prefer **Shamir** unseal for air-gapped or generic servers. **AWS KMS auto-unseal** is optional; enable only when you have a real KMS key and IAM role/instance profile.
- Inside Docker, bind OpenBao’s listener to `0.0.0.0:8200` and restrict exposure with **host** `ports: 127.0.0.1:8200:8200`.

## Nginx

`limit_req_zone` must appear in the **`http` context**. This repo ships `config/nginx/http_snippets/01-openclaw-rate-limit.conf` for `include` from your main `nginx.conf`. Site-only directives live in `openclaw.conf`.

## OpenClaw / AgentWard

Example configs and Python helpers are **templates**. Wire them into your actual OpenClaw runtime (hooks, plugins, or middleware) per upstream OpenClaw documentation.
