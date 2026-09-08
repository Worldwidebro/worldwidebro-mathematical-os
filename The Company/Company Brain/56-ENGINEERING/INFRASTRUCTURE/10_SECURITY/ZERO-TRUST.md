---
id: DOC-10-SEC-016
aliases: ['ZERO-TRUST']
tags: ['security', 'zero-trust', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE]] | [[_REGISTRIES/infrastructure_risk_registry.json]]

# Zero Trust Architecture (NIST SP 800-207)

> **Authority:** CP-027 | **Standard:** NIST SP 800-207 | **Status:** ENFORCED

## NIST SP 800-207 Multi-Subject Model
NIST Zero Trust Architecture explicitly models all entities accessing resources as subjects:
1. **Humans:** Sovereign Operator / Founder.
2. **Devices:** Mac Studio M4 Max, MacBook Air.
3. **Applications:** FastMCP, Vercel frontends, Open WebUI.
4. **Servers & Containers:** `civos_neo4j`, `civos_qdrant`, `civos_litellm`.
5. **Autonomous AI Agents:** OmniRoute, Antigravity, domain subagents.

Every subject access request must be authenticated, authorized, and encrypted regardless of physical location.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/infrastructure_risk_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/TAILSCALE|TAILSCALE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/FIREWALL|FIREWALL]]
- [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/POLICY-AS-CODE|POLICY-AS-CODE]]
- [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]]
