---
name: TOOL-UTILIZATION-AUDIT
title: Tool Utilization Audit
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Tool Utilization Audit
**Date:** 2026-08-05  
**Scope:** Local development stack + SaaS tools  

---

## Infrastructure Services (Docker)

### Neo4j (Port 7687)
**Status:** ✅ Running  
**Currently Used:** ⚠️ Idle (loaded with 712 ventures, 31 sectors, 500 capabilities, but not connected to VEX API)  
**Should Be:** Relationship graph for venture → capability → repo → agent connections  
**Gap:** No Neo4j queries from vex-api. Graph relationships not exposed via REST API.  
**Phase to Use:** Phase 5 (Knowledge Graph)  
**Action:** Wire vex-api to Neo4j queries. Create capability resolver endpoints.

### Qdrant (Port 6333)
**Status:** ✅ Running  
**Currently Used:** ⚠️ Idle (collection setup but no embeddings loaded)  
**Should Be:** Semantic search for venture descriptions, capabilities, repos  
**Gap:** No embeddings ingestion pipeline. No search endpoints.  
**Phase to Use:** Phase 6 (Semantic Intelligence)  
**Action:** Ingest venture/capability/repo descriptions as embeddings. Wire search to vex-api.

### Redis (Port 6379)
**Status:** ✅ Running  
**Currently Used:** ⚠️ Idle  
**Should Be:** Cache for API responses, session storage, rate limiting  
**Gap:** Not connected to vex-api.  
**Phase to Use:** Phase 4+ (after VEX API exists)  
**Action:** Add Redis client to vex-api. Implement response caching.

### Langfuse (Port 3003)
**Status:** ✅ Running  
**Currently Used:** ⚠️ Idle  
**Should Be:** Agent tracing, LLM observability, token counting  
**Gap:** Not integrated with agents yet.  
**Phase to Use:** Phase 10+ (Agent Execution)  
**Action:** Add Langfuse SDK to agent runners.

### Supabase (Port 5432)
**Status:** ✅ Running  
**Currently Used:** ✅ Connected (ventures, sectors tables exist)  
**Should Be:** Source of truth for all venture data + live updates  
**Gap:** Only ventures/sectors tables populated. Missing: capabilities, agents, skills, action_ledger, policies.  
**Phase to Use:** Phase 3+ (expanding)  
**Action:** Add remaining tables. Create RLS policies.

---

## Deployment Tools (Not Yet Active)

### Trigger.dev (Durable Execution)
**Status:** ❌ Not deployed  
**Currently Used:** ❌ Not integrated  
**Should Be:** Long-running workflows, async task processing, agent jobs  
**Gap:** Platform selected but no account/setup.  
**Phase to Use:** Phase 9 (Trigger.dev Integration)  
**Action:** Create Trigger.dev account, set up local development, wire to vex-engine.

### Vercel (Frontend Deployment)
**Status:** ✅ Deployed (vex-hero-site live)  
**Currently Used:** ✅ Active  
**Should Be:** Frontend CI/CD  
**Gap:** None—working correctly.  

### GitHub (Version Control)
**Status:** ✅ Deployed  
**Currently Used:** ✅ Active  
**Should Be:** Source control  
**Gap:** Some repos missing CLAUDE.md, clear architecture docs.  
**Action:** Add CLAUDE.md to vex, vex-api, vex-engine.

---

## AI/ML Tools (Often Forgotten)

### Ollama (Local LLM)
**Status:** ⚠️ Configured (port 11434 not exposed)  
**Currently Used:** ❌ Idle  
**Should Be:** Local inference for agents when internet-connected LLMs unavailable  
**Gap:** Not exposed to agent runners.  
**Phase to Use:** Phase 10+ (optional for local dev)  
**Action:** Expose port 11434. Register as fallback LLM in agent config.

---

## SaaS Tools (Subscriptions Active)

### Stripe (Payments)
**Status:** ✅ Account active  
**Currently Used:** ⚠️ Minimal (only test mode)  
**Should Be:** Live payment processing for ventures  
**Gap:** No webhook integration with action_ledger yet.  
**Phase to Use:** Phase 12+ (Action Ledger)  
**Action:** Wire Stripe webhooks to Supabase.

### Anthropic API (Claude)
**Status:** ✅ Keys configured  
**Currently Used:** ✅ Active (this conversation)  
**Should Be:** Agent LLM backbone  
**Gap:** Not yet integrated into agents—using manually.  
**Phase to Use:** Phase 10+ (Agent Execution)  
**Action:** Create agent runners using messages_api + tool_use.

### OpenBB (Market Data)
**Status:** ✅ Installed  
**Currently Used:** ❌ Idle  
**Should Be:** Market intelligence for financial ventures  
**Gap:** Not connected to any agent.  
**Phase to Use:** Phase 2+ (Marketing Intelligence) or Phase 10+ (agents)  
**Action:** Create market-research agent using OpenBB SDK.

---

## Development Tools (Often Underutilized)

### ClickUp (Project Management)
**Status:** ✅ Configured  
**Currently Used:** ⚠️ Partial (CRM integrated, not full task tracking)  
**Should Be:** Central task/milestone tracker for all 712 ventures  
**Gap:** Only used for staffing, not VEX phases or other ventures.  
**Action:** Create VEX phase milestones. Add task templates for each phase.

### Notion (Documentation)
**Status:** ✅ Configured  
**Currently Used:** ⚠️ Minimal (some docs, not structured)  
**Should Be:** Shared knowledge base for all ventures + architecture docs  
**Gap:** Not linked to ClickUp or Supabase. Not SOT.  
**Action:** Create Notion doc structure. Link to Supabase via API.

### n8n (Workflow Automation)
**Status:** ✅ Running locally  
**Currently Used:** ⚠️ Active but transitioning  
**Should Be:** Automation layer (will be replaced by Trigger.dev for critical paths)  
**Gap:** Good for simple automation, but not durable enough for production revenue flows.  
**Action:** Keep for simple flows, migrate critical ones to Trigger.dev (Phase 9).

---

## Underutilization Summary

| Tool | Current | Should Be | Gap | Priority |
|------|---------|-----------|-----|----------|
| Neo4j | Idle | Query engine | Not connected | 🔴 P0 |
| Qdrant | Idle | Search index | No embeddings | 🔴 P0 |
| Langfuse | Idle | Agent trace | Not integrated | 🟡 P1 |
| Redis | Idle | Cache layer | Not connected | 🟡 P1 |
| Trigger.dev | Idle | Durable execution | Not deployed | 🔴 P0 |
| Ollama | Idle | Local LLM fallback | Port exposed | 🟢 P2 |
| OpenBB | Idle | Market research | No agent | 🟡 P1 |
| Notion | Minimal | Knowledge base | Not linked | 🟢 P2 |
| Stripe | Minimal | Live payments | No webhooks | 🟡 P1 |
| Anthropic API | Active | Agent backbone | Phase 10 | 🔴 P0 (Phase 10+) |

---

## Quick Wins (This Week)

1. **Neo4j + vex-api integration** (2h) → Graph queries work
2. **CLAUDE.md for vex, vex-api, vex-engine** (30m) → Clear guidance
3. **API.md for vex-api** (1h) → OpenAPI schema
4. **ClickUp VEX phase milestones** (30m) → Track progress
5. **Notion architecture doc** (1h) → Centralized knowledge

---

## Critical Blockers

- **Trigger.dev not deployed** → Phase 9 cannot start
- **Neo4j queries not exposed** → Phase 5 cannot start
- **Qdrant embeddings missing** → Phase 6 cannot start
- **vex-api not connected to Supabase** → Phase 4 foundation weak

---

## Action Plan (Next 24h)

- [ ] Deploy Trigger.dev dev environment
- [ ] Create vex-api/CLAUDE.md
- [ ] Create API.md with Neo4j query endpoints
- [ ] Wire vex-api to Supabase (confirm connection)
- [ ] Create VEX phase milestones in ClickUp

---

## GSD (Get Shit Done) — The Build OS

**Status:** ✅ Concept validated, 🔴 Not yet integrated  
**Purpose:** Software-production methodology for VEX development  
**Use:** Build/modify/verify software artifacts (VEX core, APIs, portals, agents)

### GSD Workflow (per feature)

```
Requirement
    ↓
Research (codebase understanding)
    ↓
Plan (decompose into tasks)
    ↓
Execute (agents build in phases)
    ↓
Verify (test + integration)
    ↓
Commit (to Git)
```

### GSD ≠ Trigger.dev

| What | GSD | Trigger.dev |
|------|-----|-------------|
| **Purpose** | Build software | Run software |
| **When** | Development | Production |
| **Who** | Development agents | Business agents |
| **Where** | `.planning/` + repos | Workflows + jobs |
| **Result** | Code changes | Business results |

### Three Operating Systems

```
                 VEX
                  │
      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼
 BUSINESS       INTEL         BUILD
   OS            OS           OS
   (Agents)   (Graph/RAG)     (GSD)
      │           │            │
      ▼           ▼            ▼
 Customers      Graph       Software
 Employees      Data        Features
 Ventures       Memory      APIs
 Finance        Search      Agents
 Sales          Capabilities
 Operations     Repos
```

### GSD + VEX 15-Phase Roadmap

GSD will be the **build methodology** for Phases 1-15.

Each phase:
```
Phase X Goal
    ↓
GSD Workflow (DISCUSS → RESEARCH → PLAN → EXECUTE → VERIFY → SHIP)
    ↓
Deliverable (code + tests + docs)
    ↓
Next phase unblocked
```

### Action

**Add to .planning/ layer (Phase 0+):**

```
vex/.planning/
├── PROJECT.md
├── ROADMAP.md (15 phases)
├── STATE.md (current phase status)
├── REQUIREMENTS.md
│
├── phases/
│   ├── 01-repo-ingestion/
│   │   ├── brief.md
│   │   ├── research.md
│   │   └── tasks.md
│   ├── 02-architecture-audit/
│   ├── 03-data-source/
│   ├── 04-vex-api/
│   └── ... (15 phases)
│
└── research/
    ├── repos.md
    ├── capabilities.md
    └── dependencies.md
```

**Deploy:** Use GSD Core (https://github.com/open-gsd/gsd-core) as build OS for all software changes.
