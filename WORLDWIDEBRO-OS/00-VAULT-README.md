---
name: WORLDWIDEBRO-OS/00-VAULT-README
title: WORLDWIDEBRO OS — Unified Knowledge Vault
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# WORLDWIDEBRO OS — Unified Knowledge Vault

**Purpose:** Single source of truth for 712-venture system, all sectors, all communications, all tasks.

## Folder Structure (Numbered for Priority + Hierarchy)

```
01-STRATEGY/          — Vision, roadmap, decisions (quarterly)
02-INFRASTRUCTURE/    — Tech stack, APIs, databases, deployments (weekly reviews)
03-VENTURES/          — Individual venture configs, status, MRR tracking
04-OPERATIONS/        — Daily ops, checklists, playbooks, team processes
05-COMMUNICATIONS/    — API contracts, event schemas, webhooks, email templates
06-PARTNERS/          — Partner tiers, revenue share, integrations (ServiceNow, etc.)
07-OBSERVABILITY/     — Metrics, dashboards, alerts, incident logs
```

## What Lives Where

### 01-STRATEGY
- `ROADMAP-2026.md` — Annual plan (90 days: foundation → agents → revenue)
- `VEX-EVOLUTION.md` — Marketplace strategy + partners tier model
- `SECTOR-PRIORITIZATION.md` — Which sectors → revenue first

### 02-INFRASTRUCTURE
- `STACK-UNIFIED.md` — Supabase + Hermes + trigger.dev + Graphify
- `SUPABASE-SCHEMA.md` — All tables, relationships, RLS policies
- `HERMES-CONFIG.md` — Agent gateway setup, venture routing logic
- `VERCEL-DEPLOYMENTS.md` — All live ventures + env var status

### 03-VENTURES
- `CON-001/` → status, MRR, email sequences, Stripe webhooks
- `OPS-001/` → dashboard, revenue, Supabase tables
- `VEX-HERO-SITE/` → marketplace, partners, sectors
- `TECH-038/` → voice OS, licensing model

### 04-OPERATIONS
- `DAILY-STANDUP.md` — What's deployed, what's blocking, what's shipping
- `VENTURE-LAUNCH-CHECKLIST.md` — 5-step process per venture
- `INCIDENT-LOGS.md` — Prod issues + resolutions
- `TEAM-PLAYBOOKS/` → onboarding, deployment, debugging

### 05-COMMUNICATIONS
- `EVENTS-SCHEMA.md` — All events (lead.created, venture.deployed, payment.completed)
- `API-CONTRACTS.md` — Hermes ↔ trigger.dev ↔ Supabase ↔ Resend interfaces
- `EMAIL-TEMPLATES/` → CON-001, OPS-001, FIN-037, RE-001 sequences
- `WEBHOOK-REGISTRY.md` — All webhooks (Stripe, form submits, scheduled tasks)

### 06-PARTNERS
- `PARTNER-TIERS.md` — Reseller model, revenue share (30%), onboarding
- `SERVICENOW-INTEGRATION.md` — API contract, incident/change/request workflows
- `INTEGRATION-MARKETPLACE.md` — 3rd party tools (n8n, Make, Zapier, trigger.dev)

### 07-OBSERVABILITY
- `DASHBOARDS.md` — MRR per venture, email metrics, partner performance
- `ALERTS.md` — Deployment failures, payment errors, agent timeouts
- `METRICS-CATALOG.md` — KPIs (lead volume, conversion rate, LTV, CAC)

---

## Graphify Integration

This vault is indexed by Graphify:
- Folders → graph nodes
- Files → knowledge nodes
- Links [[]] → relationships
- Tags #revenue #con #deployment → semantic search

**View graph:** `graphify . --vault /Users/acebless/Documents/WORLDWIDEBRO-OS`

---

## Updating This Vault

**Rules:**
1. One file per topic (no sprawl)
2. Link everything with `[[venture-id]]`, `[[sector]]`, `[[task-id]]`
3. Date files when changed: `UPDATED: 2026-08-05`
4. Run `graphify rebuild` weekly to update graph

**Who writes what:**
- **Claude** — Infrastructure, communications, vendor docs
- **You** — Strategy, operations, decisions, incident logs
- **Agents** — Venture status updates (via webhooks), scheduled nightly

---

**Current status:** Foundation ready. Filling in 02-INFRASTRUCTURE + 05-COMMUNICATIONS this turn.
