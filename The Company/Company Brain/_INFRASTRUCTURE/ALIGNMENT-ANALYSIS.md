[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

---
id: INFRA-ALIGNMENT-ANALYSIS
title: "Alignment Analysis: Agency Personas, Homebutton, and Registries"
tags: [infrastructure, alignment, agency, registries]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[CLAUDE]]

# Alignment Analysis: Agency-Agents + Homebutton + Company-Registry + Our Architecture

## The Three Systems

### 1. **Agency-Agents** (Claude Code Personas)
- **Type:** Instruction/persona system for Claude Code
- **What it does:** Manages Claude behavior modes (frontend-dev, backend-engineer, etc.)
- **Location:** `~/.claude/agents/` (markdown files)
- **Activation:** Natural language ("activate Frontend mode")
- **NOT a task runner** — just instruction sets

### 2. **Homebutton** (Dashboard/Interface)
- **Type:** UI/dashboard system
- **What it does:** Home interface for company operations
- **Purpose:** View/manage ventures, sectors, tasks
- **Shows:** Trigger.dev job statuses, sector dashboards

### 3. **worldwidebro-company-registry** ✅ FOUND
- **Type:** Python-based canonical registry
- **Description:** "Canonical company/venture/repository/capability/platform/decision registry"
- **What it does:** Single source of truth for:
  - Ventures (712 entities)
  - Sectors (35 categories)
  - Capabilities (300+)
  - Repositories (1600+)
  - Platforms (infrastructure)
  - Decisions (ADRs)
- **Schemas:** Empty templates for all entities
- **Audit framework:** For validation
- **Architecture decision log:** ADRs

---

## Perfect Alignment: Our Architecture

```
                    CLAUDE CODE
                        ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   AGENCY-AGENTS  COMPANY-REGISTRY  HOMEBUTTON
   (Personas)     (Source of Truth) (Dashboard)
        ↓               ↓               ↓
        └───────────────┼───────────────┘
                        ↓
                    FRACTAL
                (Agent routing)
                        ↓
            ┌───────────┼───────────┐
            ↓           ↓           ↓
       SECTOR-AGENTS  TRIGGER-DEV  MCP-LAYER
       (4 education)  (async jobs) (postgres,
                                    trigger,
                                    memory,
                                    filesystem)
                        ↓
              MAC STUDIO CONTAINERS
            (Neo4j, Qdrant, Postgres)
```

---

## Why This Alignment Is Perfect

### **Company-Registry as Source of Truth**
```yaml
# Registry contains:
ventures:
  - ET-001 (Education sector)
  - FIN-042 (Finance sector)
  - LT-005 (Logistics sector)

sectors:
  - ET: Education (35 ventures)
  - FIN: Finance (42 ventures)
  - LT: Logistics (28 ventures)
  # ...35 sectors total

capabilities:
  - CAP-001: curriculum-planning
  - CAP-002: invoice-generation
  - CAP-003: shipment-tracking
  # ...300+ capabilities

platforms:
  - Fractal (agent routing)
  - Trigger.dev (task orchestration)
  - Neo4j (relationship graph)
  - Qdrant (semantic search)
  - PostgreSQL (operations)
```

### **Fractal Reads Registry**
```python
# fractal/core/agent.py
from company_registry import get_sector, get_capabilities

def route_agent(venture_id: str):
    sector = get_sector(venture_id)  # ET, FIN, LT, etc.
    capabilities = get_capabilities(sector)  # agent routing
    return resolve_agent(capabilities[0]['agent'])  # → education-teacher
```

### **Trigger.dev Tasks Reference Registry**
```ts
// trigger/sector-tasks.ts
import { getVenture, getSectorConfig } from "company-registry";

export const sectorTask = task({
  id: "sector-task",
  run: async ({ ventureId }) => {
    const venture = await getVenture(ventureId);  // ET-001
    const sector = venture.sector;  // ET
    const config = await getSectorConfig(sector);  // 35 sector configs
    const taskType = config.taskTypes[0];  // curriculum-planning
    return await executeTask(taskType, ventureId);
  }
});
```

### **Agency-Agents Provides Claude Personas**
```markdown
# engineering/sector-specialist.md
You are a sector specialist for ${SECTOR}.

Sector: ${SECTOR}
Ventures: ${COUNT}
Capabilities: ${LIST}
MCP Registry: [sector-mcp-registry.yaml]
Trigger.dev Tasks: [/trigger/sector-tasks.ts]

When activated, you help manage ventures in this sector.
```

### **Homebutton Displays Everything**
```
┌─ Homebutton Dashboard ────────────────┐
│  Sectors │ Ventures │ Tasks │ Logs    │
├──────────────────────────────────────┤
│ ET: 35 ventures                       │
│   ├─ curriculum-planning: 3 running   │
│   ├─ course-export: 1 pending         │
│   └─ student-onboarding: 5 completed  │
│                                       │
│ FIN: 42 ventures                      │
│   ├─ invoice-generation: 8 running    │
│   ├─ payment-processing: 2 pending    │
│   └─ revenue-tracking: 12 completed   │
│                                       │
│ LT: 28 ventures                       │
│   ├─ shipment-tracking: 15 running    │
│   ├─ route-optimization: 0 pending    │
│   └─ delivery-confirmation: 28 done   │
└──────────────────────────────────────┘
```

---

## Integration Checklist

- [ ] Clone worldwidebro-company-registry (audit schemas)
- [ ] Sync sector definitions from registry → MCP registry
- [ ] Update Fractal to read from company-registry
- [ ] Create sector-specific agency-agents personas
- [ ] Wire Homebutton to display Trigger.dev task statuses
- [ ] Deploy integrated system to Mac Studio

---

## Why This Matters

**Before:** Scattered sources of truth
- Sector definitions in CLAUDE.md
- MCP registry in sector-mcp-registry.yaml
- Venture data in Supabase
- Agent routing in fractal/core/agent.py

**After:** Single source of truth (company-registry) feeds everything
- Fractal reads registry → agent routing
- Trigger.dev reads registry → task config
- Homebutton reads registry → dashboard data
- Agency-agents read registry → persona config

**Result:** 712 ventures across 35 sectors, fully orchestrated, observable, and manageable.

---

## Infrastructure Context & Links
- **Engineering Hub:** [[56-ENGINEERING/README|56-ENGINEERING]]
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Runtime State:** [[CLAUDE]]
- **Capabilities Matrix:** [[14-CAPABILITIES/CAPABILITIES_INDEX]]
