---
name: system-taxonomy
description: VEX Operating System - Complete taxonomy mapping (8 layers × 50 capabilities × 12 domains) with audit and task prioritization
metadata:
  type: reference
  version: 1.0
  status: active
  last_updated: 2026-08-07
  incomplete_tasks: 90
  completed_percentage: 30
---

# VEX Operating System — Complete Taxonomy & Audit

**Purpose:** Unified capability-based architecture for 712-venture autonomous operating system.  
**Current State:** 30% complete (15/50 capabilities, 5/8 layers at 50%+)  
**Incomplete Tasks:** 90 documents with TODO/WIP/BLOCKED  
**Next:** Deploy missing layers systematically by capability, not by venture.

---

## 📊 THE 8-LAYER ARCHITECTURE

### Layer 1: Compute & Runtime (40% complete)
**What:** CPU, containers, serverless, edge compute  
**Status:** Docker running (11 containers) ✅; Ollama needed ❌

### Layer 2: Operating System (80% complete)
**What:** Filesystem, processes, memory, permissions, services  
**Status:** macOS stable ✅; Tailscale pending ❌

### Layer 3: Developer Runtime (75% complete)
**What:** Python, Node, Go, Rust, Java, .NET; package managers  
**Status:** Python 3.12 ✅; Node ✅; Go ✅; Rust needed ❌

### Layer 4: Developer Toolchain (85% complete)
**What:** Git, SDK, CLI, Framework, API, MCP  
**Status:** Toolchain solid ✅; **MCP servers critical gap** ❌

### Layer 5: Agent Tooling (50% complete)
**What:** Planner, memory, reasoner, evaluator, reflection, critic  
**Status:** Core loop ✅; Reflection/Critic needed ❌

### Layer 6: MCP Ecosystem (0% complete) ⚠️ **CRITICAL GAP**
**What:** Filesystem MCP, GitHub MCP, Neo4j MCP, Postgres MCP, Browser MCP  
**Status:** ZERO deployed ❌ BLOCKING all agent-to-service communication

### Layer 7: AI Infrastructure (30% complete)
**What:** LLMs, embeddings, RAG, rerankers, vision, OCR, TTS/STT  
**Status:** Text-only ✅; Multimodal needed ❌

### Layer 8: Business Systems (25% complete)
**What:** CRM, Projects, Scheduling, Analytics, Support  
**Status:** TwentyHQ CRM ✅; Vikunja/Chatwoot/Cal.com/PostHog needed ❌

---

## 🗺️ THE 50-DOMAIN CAPABILITY MAP

### Deployed (15/50 - 30%)
✅ Identity, Knowledge, Data, Storage, Development, AI, Analytics, Knowledge Graph, Vector DB, Event Bus, Agent Platform, Observability, Integration, APIs

### Critical Missing (12/50)
❌ Communication (Chatwoot), Automation, Workflow, Projects (Vikunja), CRM (partial), Security, Scheduling (Cal.com), Decision Engine, Testing, Compliance, Reporting, Business Intelligence

### Not Started (23/50)
ERP, Finance, HR, Marketing, Sales, Support, Infrastructure, DevOps, Monitoring, Design, Content, Media, Documents, Commerce, Search, Rules, Simulation, Mobile, IoT, GIS, Collaboration, Learning, Research, Governance

---

## 🎯 CATEGORIZED INCOMPLETE TASKS (90 Total)

### TIER 0: CRITICAL PATH (Deploy First)
- MCP deployment (Filesystem, GitHub, Neo4j, Postgres, Browser)
- Ollama/Tailscale infrastructure
- Event bus wiring (Redis → Neo4j)

### TIER 1: FOUNDATION (Week 1-2)
- Agent autonomy pipeline
- Business systems (Vikunja, Chatwoot, Cal.com)
- Langfuse evaluator wiring

### TIER 2: VENTURE OPERATIONS (Week 3+)
- Revenue tracking (CON-001, LT-005)
- Sector readiness
- Portfolio management

### TIER 3: PLANNING & STRATEGY
- System audits
- Skills inventory
- Org structure

### TIER 4-5: DASHBOARDS & LEGACY
- Graph dashboards
- Older planning docs

---

## 🚀 EXECUTION ROADMAP

### **THIS WEEK: MCP + Services**
```
Parallel Track 1: Deploy 5 critical MCPs
├── Filesystem MCP (file agent)
├── GitHub MCP (code agent)
├── Neo4j MCP (graph agent)
├── Postgres MCP (data agent)
└── Browser MCP (web agent)

Parallel Track 2: Deploy business systems
├── Vikunja (tasks)
├── Chatwoot (comms)
├── Cal.com (scheduling)
└── PostHog (analytics)

Result: Unblock all agent-to-service communication + enable autonomous loops
```

### **WEEK 2: Foundation**
- Wire MCP servers → event bus
- Wire business systems → Neo4j
- Deploy Langfuse evaluator

### **WEEK 3: Intelligence**
- Add reranker
- Add vision model
- Add OCR/TTS/STT

### **WEEK 4: Autonomy**
- First complete autonomous loop
- Goal/time/event-based loops
- Multi-loop orchestration

---

## 📌 NEXT ACTIONS

1. ✅ Create this file (system taxonomy)
2. Update MASTER-INDEX.md with layer/domain links
3. Categorize 2,000 repos by 50-domain taxonomy
4. Create DEPLOYMENT-CHECKLIST.md (week-by-week)
5. Archive/consolidate 90 incomplete tasks into taxonomy

**This file is your single source of truth for system completeness.**

