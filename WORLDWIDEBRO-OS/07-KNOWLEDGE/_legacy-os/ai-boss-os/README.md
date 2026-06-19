# AI Boss OS — CivilizationOS Operating System

**Autonomous Intelligence Operating System for 712 Ventures Across 31 Sectors**

This is a **production-ready, multi-agent system** designed to:
- Autonomously manage 712+ ventures
- Make data-driven capital allocation decisions
- Monitor risk + ROI in real-time
- Scale from startup to 10,000+ ventures

**Tech Stack:** Kafka + Temporal + LangGraph + Neo4j + Postgres + Grafana

### Bootstrap (Week 1)

```bash
# 1. Load 712 ventures → entity registry
python3 scripts/load_entity_registry.py

# 2. Dry-run (default) — validates config, lists SQL + Kafka topics
python3 core/bootstrap/init_system.py

# 3. Apply when Postgres + Kafka are running
python3 core/bootstrap/init_system.py --apply
```

**Config:** `core/config/system_config.yaml` · **Contracts:** `../agents-os/shared/CONTRACTS-SUMMARY.md`

### Cursor / Claude entry points

| File | Purpose |
|------|---------|
| `.cursor/instructions.md` | Implementation guide for Cursor agents |
| `.claude/cursor.md` | Cursor-specific rules (boundaries, style) |
| `CURSOR-TASKS.md` | Phased checklist — **start here for builds** |
| `../SESSION-HANDOFF-2026-06-05.md` | Full session pickup (all workstreams) |

---

## 🧠 System Architecture (13 Layers)

```
┌─────────────────────────────────────────────────────┐
│  HUMAN LAYER (Obsidian Knowledge Vault)             │
├─────────────────────────────────────────────────────┤
│  MCP API GATEWAY (FastAPI + Tool Registry)          │
├─────────────────────────────────────────────────────┤
│  SECURITY LAYER (Vault + Keycloak + OPA)            │
├─────────────────────────────────────────────────────┤
│  ECONOMIC LAYER (Revenue, Capital, ROI)            │
├─────────────────────────────────────────────────────┤
│  OBSERVABILITY (Grafana + Prometheus + Logs)        │
├─────────────────────────────────────────────────────┤
│  EVENT SYSTEM (Kafka + Consumers + Schemas)         │
├─────────────────────────────────────────────────────┤
│  MEMORY + DATA (Postgres + Neo4j + Vector DB)       │
├─────────────────────────────────────────────────────┤
│  EXECUTION (Temporal Workflows + n8n Flows)         │
├─────────────────────────────────────────────────────┤
│  AGENTS (6 Agent Types Coordinated)                 │
├─────────────────────────────────────────────────────┤
│  REGISTRIES (System Governance + Metadata)          │
├─────────────────────────────────────────────────────┤
│  BOOTSTRAP (System Init + Runtime + Scheduler)      │
├─────────────────────────────────────────────────────┤
│  CORE CONFIG (Environment + Feature Flags)          │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Folder Structure

### **Core System** (`core/`)
- System initialization, bootstrap, event loop, scheduler

### **Registries** (`registries/`)
13 registries that govern the system (entities, agents, workflows, capital, risk, etc.)

### **Agents** (`agents/`)
6 agent archetypes + multi-agent coordination

### **Execution** (`execution/`)
Temporal workflows, n8n flows, job runners, schedulers

### **Memory** (`memory/`)
Postgres (truth), Neo4j (graph), Qdrant (vector search), Redis (cache)

### **Events** (`events/`)
Kafka producers/consumers, event schemas, 25 event types

### **Observability** (`observability/`)
Grafana dashboards, Prometheus metrics, structured logging, tracing

### **Economy** (`economy/`)
Capital allocation, revenue tracking, ROI calculations, pricing logic

### **Security** (`security/`)
Vault (secrets), Keycloak (auth), OPA (policies), roles + permissions

### **Knowledge Vault** (`knowledge_vault/`)
Obsidian integration, venture logs, decision history, system maps

### **MCP** (`mcp/`)
FastAPI gateway, tool registry, agent bridge for Claude + other LLM agents

### **Ventures** (`ventures/`)
Active/testing/failed/scaled venture folders

### **Docker/K8s** (`docker/`, `k8s/`)
Container definitions, Kubernetes manifests

---

## 🚀 Quick Start

### 1. Setup Environment
```bash
cd ai-boss-os
cp core/config/system_config.yaml.example core/config/system_config.yaml
# Edit with your Kafka, Postgres, Neo4j connection strings
```

### 2. Initialize System
```bash
python3 core/bootstrap/init_system.py
# Creates database schemas, Neo4j ontology, Kafka topics
```

### 3. Start Services
```bash
bash core/bootstrap/start_services.sh
# Starts: Kafka, Postgres, Neo4j, Redis, Temporal, Grafana
```

### 4. Boot Orchestrator
```bash
python3 agents/orchestration_agents/master_orchestrator.py
# Loads 712 ventures, spawns venture agents, starts risk monitor
```

### 5. Monitor Dashboard
```
Open http://localhost:3000 (Grafana)
Watch real-time agent decisions, risk alerts, capital allocation
```

---

## 🧭 Implementation Phases

### Phase 1: Registries + Bootstrap (Week 1)
- [ ] Load all entity data from CSV → entity_registry/
- [ ] Define all 6 agent types in agent_registry/
- [ ] Define 25 event types in event_registry/
- [ ] Create Kafka topics + Postgres schema

### Phase 2: Core Infrastructure (Week 2)
- [ ] Bootstrap system init
- [ ] Event bus integration (Kafka)
- [ ] State persistence (Postgres + Redis)
- [ ] Graph seeding (Neo4j)

### Phase 3: Master Orchestrator (Week 2-3)
- [ ] Build orchestrator agent (LangGraph)
- [ ] Venture agent spawning (Temporal)
- [ ] Risk agent monitor

### Phase 4: Venture Agent Template (Week 3-4)
- [ ] Single venture agent (state machine)
- [ ] Decision loop + execution
- [ ] Risk integration

### Phase 5: Integration (Week 4-5)
- [ ] Grafana dashboards
- [ ] Prometheus metrics
- [ ] Slack notifications
- [ ] Obsidian export

### Phase 6: Production (Week 5-6)
- [ ] Docker/Kubernetes deployment
- [ ] Load testing
- [ ] Failure recovery
- [ ] Go/no-go decision

---

## 📊 Key Concepts

### **Registries = System Governance**
Instead of hardcoded configs, everything is metadata-driven.

### **Events = State Mutations**
No direct DB writes. All changes flow through Kafka.

### **Agents = Autonomous Decisions**
6 agent types coordinate to manage system.

### **Memory = 3 Layers**
- Postgres (truth) + Neo4j (relationships) + Qdrant (semantic search)

---

## 🚀 Next Steps

1. Check `BUILD-STATUS.md` for what's been created vs. what remains
2. Start with Phase 1 in `registries/`
3. Follow agent development guide in `agents/README.md`

