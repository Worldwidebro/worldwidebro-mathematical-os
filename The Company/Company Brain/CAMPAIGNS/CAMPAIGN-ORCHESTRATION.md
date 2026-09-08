# CAMPAIGN-ORCHESTRATION — Routing, Scheduling & Task Decomposition

> **Canonical Document ID:** `DOC-ORC-CAM-001`  
> **Authority:** Orchestration (CP-019)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. Orchestration Engine Principles

The **Campaign Orchestrator** evaluates active campaign states on an hourly cron:
1. Queries Prometheus and Postgres for current spend and event telemetry.
2. Checks active experiments for statistical significance.
3. Evaluates [[CAMPAIGNS/STOP-RULES]]; if any threshold is violated, triggers immediate pause.
4. Generates daily operational digests for the Sovereign Operator.

---

## 2. Master Links

- Automation: [[CAMPAIGNS/CAMPAIGN-AUTOMATION]]
- Governance: [[CAMPAIGNS/GOVERNANCE]]
