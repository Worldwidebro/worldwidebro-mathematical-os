---
name: deployment
description: Orchestrates service deployments, container lifecycle, and infrastructure updates across the Mac Studio and local network. Use when deploying Docker services, updating CLI tools, or modifying system daemons.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Deployment Skill

This skill coordinates infrastructure deployments across Company Brain nodes according to `CLAUDE.md` and `_INFRASTRUCTURE/DEPLOYMENT_PHASES.md`.

## Node Targets

- **Mac Studio** (`100.87.214.70` via Tailscale):
  - Primary Docker host (reached via `docker --context macstudio`)
  - Runs Neo4j (`civos_neo4j`), Qdrant, PostgreSQL, Redis, OmniRoute, LiteLLM, Grafana, Langfuse, and `exo`.
- **MacBook Air** (`100.121.17.63` via Tailscale):
  - Client and mobile development node.

## Deployment Checklist

1. Pre-flight checks: confirm container health and disk space on LaCie 4TB.
2. Rollback readiness: ensure previous configuration files are backed up.
3. Health check: verify port responsiveness and API status endpoints post-deployment.
