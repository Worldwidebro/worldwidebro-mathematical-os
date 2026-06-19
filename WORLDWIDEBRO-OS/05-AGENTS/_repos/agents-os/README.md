# CivilizationOS Agent Operating System

**Production-ready multi-agent system** for managing 712 ventures across 31 sectors.

Three coordinated agent types running on unified OS infrastructure.

---

## 📁 Structure

```
agents-os/
├── shared/                      # Contracts, schemas, common code
│   ├── schemas/                 # Data contracts (JSON Schema)
│   ├── registries/              # OS entity registries (entities, relationships, capabilities)
│   ├── config/                  # Shared configuration
│   └── utils/                   # Common libraries
│
├── orchestrator/                # Master Orchestrator Agent
│   ├── config/                  # Agent config + capabilities
│   ├── workflows/               # Orchestration flows
│   ├── decision-engine/         # Capital allocation + flow control
│   └── integration/             # OS <-> Orchestrator contracts
│
├── venture-agent/               # Venture Agent (1 per venture)
│   ├── config/                  # Template config (instantiated per venture)
│   ├── workflows/               # Venture execution flows
│   ├── state-management/        # Venture state machine
│   └── integration/             # Venture OS contracts
│
├── risk-agent/                  # Risk/Capital Monitor Agent
│   ├── config/                  # Risk engine config
│   ├── rules-engine/            # Kill/scale logic
│   ├── constraints/             # System boundaries
│   └── integration/             # Risk OS contracts
│
├── event-system/                # Central event bus + schemas
│   ├── topics/                  # Event type definitions
│   ├── handlers/                # Event processors
│   └── routing/                 # Event routing rules
│
├── state-model/                 # Source-of-truth state definitions
│   ├── venture-state.md         # Venture state machine
│   ├── agent-state.md           # Agent execution state
│   └── system-state.md          # Global system state
│
├── integrations/                # External system contracts
│   ├── supabase/                # Database integration
│   ├── chroma/                  # Vector search integration
│   └── webhooks/                # Event webhooks
│
└── deployment/                  # Production deployment
    ├── docker/                  # Container definitions
    ├── kubernetes/              # K8s manifests
    └── monitoring/              # Observability configs
```

---

## 🚀 Quick Start

### 1. **Define Data Contracts**
```bash
cd shared/schemas
# Review all JSON Schema definitions for agents, events, state
```

### 2. **Load OS Knowledge**
```bash
cd shared/registries
# Load venture registry, sector taxonomy, capabilities mapping
```

### 3. **Run Master Orchestrator**
```bash
cd orchestrator
# Orchestrator is the entry point—it spawns venture agents + risk agent
```

### 4. **Monitor via Events**
```bash
cd event-system
# All agent actions → events → Obsidian/Grafana dashboards
```

---

## 📊 System Architecture (Contracts-First View)

### Three Agent Types (State Machine Perspective)

```
┌─────────────────────────────────────────────────────────────┐
│                  MASTER ORCHESTRATOR                         │
│  (Startup) → Load ventures → Spawn agents → Event loop      │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Venture Agent│  │ Venture Agent│  │  Risk Agent  │
│   Venture 1  │  │  Venture N   │  │   Monitor    │
│ (Running)    │  │  (Running)   │  │  (Continuous)│
└──────────────┘  └──────────────┘  └──────────────┘
      │                  │                  │
      └──────────────────┼──────────────────┘
                         │
                    Event Bus
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
         Obsidian            Grafana Dashboards
        (Dataview)          (Real-time KPIs)
```

### Event Flow

```
Agent Decision → Event Emitted → Bus → Risk Engine → Validation
                                         ↓
                                   OK? → Update State
                                   ✗? → Escalate/Rollback
```

---

## 🔑 Key Design Principles

### 1. **Data Contracts Over Code**
Every system interaction has a **JSON Schema contract**. No ambiguity.

### 2. **Event-Driven State**
No direct DB writes. All mutations via events → state transitions.

### 3. **Risk Engine First**
Every decision validated against constraints before execution.

### 4. **Deterministic Agent Loops**
Agents are state machines, not black boxes. Every step logged.

### 5. **Economic Awareness**
Every agent decision tracks cost + ROI impact.

---

## 📈 Files to Read First (Order Matters)

1. **shared/contracts-summary.md** — All system boundaries in one place
2. **shared/schemas/agent.schema.json** — Agent structure contract
3. **orchestrator/config/orchestrator.yaml** — Master agent config
4. **event-system/event-taxonomy.md** — All 25 event types
5. **state-model/venture-state.md** — Venture state machine
6. **risk-agent/rules-engine/constraints.json** — Kill/scale rules

---

## 🧭 Implementation Sequence

### Phase 1: Contracts (Week 1)
- [ ] Define all 10 schemas
- [ ] Define all 25 event types
- [ ] Define venture state machine
- [ ] Define agent execution model

### Phase 2: Orchestrator (Week 2)
- [ ] Build orchestrator agent
- [ ] Event bus integration
- [ ] Venture agent spawning

### Phase 3: Venture Agent (Week 3)
- [ ] Build single venture agent template
- [ ] State machine implementation
- [ ] Workflow engine

### Phase 4: Risk Agent (Week 3)
- [ ] Build risk monitor
- [ ] Constraint validation
- [ ] Escalation logic

### Phase 5: Integration (Week 4)
- [ ] Supabase sync
- [ ] Event logging
- [ ] Obsidian + Grafana dashboards

### Phase 6: Production (Week 5)
- [ ] Docker / Kubernetes
- [ ] Load testing
- [ ] Go/no-go decision

---

## 🧠 For Engineers Implementing This

1. **Don't implement without reading the schemas first**
2. **Every agent method = one state transition**
3. **Every mutation = one event**
4. **Every event = one dashboard metric**

Start with `shared/contracts-summary.md`. Everything else flows from there.

---

## 📞 Questions?

- **"What's the API contract between orchestrator + venture agent?"** → See `shared/schemas/`
- **"What happens when a venture hits risk threshold?"** → See `risk-agent/rules-engine/constraints.json`
- **"How do I add a new agent type?"** → Follow the Venture Agent template in `venture-agent/config/`
- **"What events exist?"** → See `event-system/event-taxonomy.md`
