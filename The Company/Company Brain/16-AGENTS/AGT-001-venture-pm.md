# AGT-001: Venture PM Agent

**Agent ID:** AGT-001  
**Fractal Agent:** `venture-pm`  
**Status:** 🟢 ACTIVE  
**Updated:** 2026-09-02

---

## Overview

Venture Project Management routing agent. Routes project orchestration tasks to Claude backend via Fractal loop orchestration.

**Purpose:** Project setup, milestone tracking, delivery coordination

---

## Integration

### Fractal
- **Class:** `company_brain.VenturePMAgent`
- **Command:** `venture-pm`
- **Backend:** Claude (Claude Opus 5)
- **File:** `/fractal/fractal/impl/company_brain.py:VenturePMAgent`

### Company Brain Registry
- **Metadata:** `/_REGISTRIES/agents/AGT-001-venture-pm.yaml`
- **Linked to:** [[SECTOR-TAXONOMY-MASTER]]

### Neo4j
- **Node:** `Agent {id: 'AGT-001', name: 'Venture PM'}`
- **Relationships:** SERVES → [[Sectors]], EXECUTES → [[Control Planes]]

---

## Sectors Served

- [[SEC-002-Construction]]
- [[SEC-005-Education]]
- [[SEC-008-Financial]]
- [[SEC-017-Logistics]]
- [[SEC-024-Technology]]
- All others (cross-cutting)

---

## Control Planes

- [[CP-001-Strategic-Planning]]
- [[CP-012-Project-Execution]]
- [[CP-023-Governance]]
- [[CP-026-Delivery]]

---

## Capabilities

- [[CAP-001-API-Design]]
- [[CAP-012-Project-Management]]
- [[CAP-055-Milestone-Tracking]]

---

## Autonomy Levels (L1/L2/L3)

| Level | Budget | Behavior | Approval |
|-------|--------|----------|----------|
| **L1** | $0.50/step | Report & plan | Requires human approval |
| **L2** | $2.00/step | Execute with monitoring | Automatic (after 10+ L1 successes) |
| **L3** | $10.00/run | Autonomous execution | Automatic (after 10+ L2 successes) |

---

## ClickUp Integration

**Task Types Routed to This Agent:**
- "Project setup"
- "Milestone tracking"
- "Delivery coordination"
- "Sprint planning"

**Trigger:** Tasks containing `@[VENTURE-ID]` in description

---

## Related Agents

- [[AGT-002-financial]] — coordinates revenue tracking
- [[AGT-003-technical]] — coordinates infrastructure
- [[AGT-004-sales]] — coordinates lead qualification

---

## Status

- [x] Fractal implementation
- [x] Registry metadata
- [x] Obsidian vault entry
- [ ] Neo4j wiring (pending auth)
- [ ] End-to-end test

---

**See also:** [[16-AGENTS]] | [[\\\_REGISTRIES/agents/AGT-001-venture-pm.yaml]]
