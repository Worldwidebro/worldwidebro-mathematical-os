---
title: Phase 2 — Repository Authority & Single Source of Truth
date: 2026-07-27
version: 1.0
---

# Phase 2: Repo Authority Matrix

## Problem

Multiple repos claim authority over the same data:
- `worldwidebro-os-knowledge-graph` (was: tree-of-life) — "source of truth"
- `worldwidebro-os-business-engine` — ecosystem logic
- `worldwidebro-os-infrastructure` — bootstrapping + schemas
- Sector-specific repos — their own schemas

**Solution:** Designate canonical layers, make others reference (not copy).

---

## Authority Matrix

| Layer | Canonical Repo | Authority | Other Repos Must |
|-------|---|---|---|
| **Knowledge Graph** | worldwidebro-os-knowledge-graph | Graph schema, entity definitions, relationships | Reference via git submodule or @include |
| **Business Logic** | worldwidebro-os-business-engine | Workflow orchestration, agent patterns, decision logic | Reference via API/import |
| **Infrastructure** | worldwidebro-os-infrastructure | Docker compose, bootstrap scripts, health checks, Makefile | Use as-is (no modifications) |
| **Sector Cores** | worldwidebro-{sector}-os | Sector-specific agents, skills, data models | Extend (don't override) base schemas |
| **Agent Registry** | worldwidebro-os-business-engine/agents/ | 22 agents × 6 OPCOs, decision authority | Reference via JSON API |
| **Skill Registry** | worldwidebro-os-business-engine/skills/ | 296+ skills, tool mappings | Query via endpoint (not copy) |
| **Venture Monorepo** | worldwidebro-ventures | All 712 ventures, venture-specific code | Consume (read-only) from canonical layers |

---

## Enforcement

### What This Means

**✅ DO:** Sector repos can have their own CON-specific agents, but base agent structure comes from worldwidebro-os-business-engine

**❌ DON'T:** Copy ONTOLOGY.md into sector repos; link to canonical version instead

**✅ DO:** Each sector OS can have sector-specific skills, but core 296+ come from worldwidebro-os-business-engine

**❌ DON'T:** Duplicate schemas across repos; reference canonical schema

### Implementation

```bash
# In sector repo (e.g., worldwidebro-construction-os):
# Instead of copying schema.sql, reference it:

# Option A: Git submodule
git submodule add https://github.com/worldwidebro/worldwidebro-os-knowledge-graph.git schemas

# Option B: API-based (cleaner)
# Read from: https://raw.githubusercontent.com/worldwidebro/worldwidebro-os-knowledge-graph/main/schema.sql
```

---

## Cross-Repo Dependencies

```
worldwidebro-ventures (712 ventures)
    ↓ reads
worldwidebro-os-infrastructure (bootstrap + services)
    ↓ uses
worldwidebro-os-business-engine (agents + skills + workflows)
    ↓ reads from
worldwidebro-os-knowledge-graph (canonical schema + ontology)
    ↓ references
worldwidebro-{sector}-os (CON, FIN, STA, EDU, MKTG, etc)
    ↓ uses
(Venture-specific implementations)
```

---

## Migration Path (Immediate)

**Week 1:** Update README in each repo to state its authority level

**Week 2:** Remove duplicate files from sector repos; add references instead

**Week 3:** Test cross-repo references (git submodules + API calls)

**Week 4:** Update CI/CD to validate no duplication

---

## Authority Tiers

### Tier 1 (Canonical)
- worldwidebro-os-knowledge-graph
- worldwidebro-os-business-engine
- worldwidebro-os-infrastructure

→ Other repos reference, never fork

### Tier 2 (Sector Extensions)
- worldwidebro-construction-os
- worldwidebro-finance-os
- worldwidebro-staffing-os
- worldwidebro-education-os
- worldwidebro-marketing-os

→ Can extend base schemas, not override

### Tier 3 (Consumption)
- worldwidebro-ventures (712 ventures)
- worldwidebro-venture-portal (discovery)
- worldwidebro-agent-command-center (operations)

→ Read-only consumers of Tier 1 + Tier 2

---

**Status:** ✅ AUTHORITY DESIGNATED | Next: Phase 3 (Master Blueprint)
