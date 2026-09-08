---
id: INFRA-SUB-CONFIG
title: "System Configuration & Environment Variables Infrastructure"
aliases: ["_INFRASTRUCTURE/config", "Config Infrastructure"]
tags: [infrastructure, config, environment, secrets, tailscale]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[CLAUDE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]]

# System Configuration & Environment Variables Infrastructure

Canonical management of `.env.local` bindings, Tailscale node variables, and daemon service configurations.

## Architecture & Security
- **Secrets Architecture:** [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECRETS|Secrets Management]]
- **Infrastructure Registry:** [[_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml]]
- **Runtime Environment:** [[CLAUDE.md]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
