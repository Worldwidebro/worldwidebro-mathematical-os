---
id: RECON-DEP-MAP-001
title: "Universal Capability Dependency Map"
aliases: ["Capability Dependency Map", "CAPABILITY_DEPENDENCY_MAP"]
tags: [reconciliation, dependencies, capabilities, ast, supply-chain, graph]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[14-CAPABILITIES/CAPABILITIES_INDEX|Capabilities]] | [[_REGISTRIES/README|Registries Hub]] | [[56-ENGINEERING/README|56-ENGINEERING]]

# Company Brain — Capability Dependency Map
**What 903 starred repos enable in Company Brain**

---

## EXECUTIVE: THE STACK

**31M+ stars** across 903 starred repos. They power:

| Layer | Repos | Stars | Key Tools |
|-------|-------|-------|-----------|
| **AI/Agent Core** | 130 | 3.9M | Claude Code, LangGraph, ponytail, LLM apps |
| **Code Intelligence** | 5 | 314K | Graphify, CodeGraph, LangGraph, graphiti |
| **Orchestration** | 28 | 1.1M | n8n, Dify, MoneyPrinterTurbo |
| **Frontend/UX** | 224 | 7.0M | OpenClaw, Developer Roadmap, ECC, DeepSeek Harness |
| **Knowledge Graphs** | 5 | 314K | LangGraph, Graphify, CodeGraph |
| **Infrastructure** | 7 | 144K | Docker, Terraform, AWS |
| **Observability** | 3 | 228K | Grafana, Prometheus, WorldMonitor |
| **CLI/Tooling** | 19 | 608K | Paperclip, Docling, CLI-Anything |
| **Security** | 2 | 47K | OAuth2, Cybersecurity Skills |
| **Documentation** | 9 | 33K | Wiki, MediaWiki, CodeWiki |

---

## HOW COMPANY BRAIN IS BUILT

### 1. AI/AGENT FOUNDATION (130 repos)
**Purpose:** Core reasoning, model orchestration, RAG

**Top tools:**
- **claude-code** (143K★) — Core IDE integration
- **ponytail** (119K★) — Lazy efficiency patterns (active skill!)
- **awesome-llm-apps** (135K★) — Reference implementations
- **system-prompts-and-models** (143K★) — Model context library
- **LLM frameworks** — OpenAI, Claude SDK, LLaMA

**Enables in CB:**
- CAP-001: Multi-model orchestration
- CAP-002: Prompt engineering & composition
- CAP-003: RAG pipeline construction
- CAP-004: Agent decision logic
- CAP-005: Long-context understanding

---

### 2. CODE INTELLIGENCE (5 repos, but 314K stars)
**Purpose:** Understand, map, analyze codebases

**Top tools:**
- **graphify** (113K★) — Turn code into knowledge graphs (CRITICAL)
- **codegraph** (69K★) — Pre-indexed code knowledge
- **code-review-graph** (31K★) — MCP code intelligence
- **langgraph** (40K★) — Build resilient agent workflows

**Enables in CB:**
- CAP-150: Code-to-graph transformation
- CAP-151: Symbol indexing & search
- CAP-152: Dependency analysis
- CAP-153: Architecture visualization
- CAP-154: Code review automation

**IN USE:** Graft (57-CODE-INTELLIGENCE), graphify integration

---

### 3. ORCHESTRATION & WORKFLOWS (28 repos, 1.1M stars)
**Purpose:** Connect tools, automate flows, manage complexity

**Top tools:**
- **n8n** (203K★) — Workflow automation platform
- **dify** (154K★) — LLM app builder + agentic workflows
- **MoneyPrinterTurbo** (119K★) — Automated content generation
- **MinerU** (78K★) — Document pipeline

**Enables in CB:**
- CAP-200: Multi-agent orchestration
- CAP-201: Loop engineering (L1/L2/L3)
- CAP-202: Task scheduling & distribution
- CAP-203: Data pipeline automation
- CAP-204: Workflow state machines

**IN USE:** Loop Engineering (20-LOOPS), Herdr workflows

---

### 4. FRONTEND & VISUALIZATION (224 repos, 7M stars)
**Purpose:** User interface, dashboards, agent monitoring

**Top tools:**
- **openclaw** (388K★) — Personal AI assistant interface
- **developer-roadmap** (366K★) — Learning/capability maps
- **ECC** (245K★) — Agent harness performance system
- **deepseek-harness** (208K★) — Orchestration UI
- **React/Vue/Next.js** ecosystem

**Enables in CB:**
- CAP-300: VEX Hero dashboard
- CAP-301: Agent monitoring UI
- CAP-302: Real-time collaboration
- CAP-303: Data visualization
- CAP-304: Component libraries

**IN USE:** VEX Hero, venture-hub, Obsidian Vault

---

### 5. KNOWLEDGE GRAPHS & MEMORY (5 repos)
**Purpose:** Store, retrieve, traverse relationships

**Top tools:**
- **LangGraph** (40K★) — Resilient agent memory
- **graphiti** (30K★) — Real-time knowledge graphs
- **graphify** (113K★) — Code-to-graph

**Enables in CB:**
- CAP-400: Neo4j graph queries
- CAP-401: Semantic search (Qdrant)
- CAP-402: Memory systems (episodic, semantic)
- CAP-403: Relationship traversal
- CAP-404: Context assembly

**IN USE:** Neo4j (08-KNOWLEDGE-GRAPH), Qdrant (semantic indexing)

---

### 6. INFRASTRUCTURE & DEVOPS (7 repos)
**Purpose:** Deploy, monitor, scale

**Top tools:**
- **Terraform** (49K★) — IaC automation
- **lazydocker** (52K★) — Docker management
- **ubicloud** (12K★) — AWS alternative

**Enables in CB:**
- CAP-500: Infrastructure-as-code
- CAP-501: Container orchestration
- CAP-502: Cloud operations
- CAP-503: Secret management

**IN USE:** Docker, Vercel, Supabase

---

### 7. OBSERVABILITY (3 repos, 227K stars)
**Purpose:** Monitor, trace, debug

**Top tools:**
- **Grafana** (76K★) — Dashboards
- **Prometheus** (65K★) — Metrics
- **WorldMonitor** (85K★) — Global intelligence

**Enables in CB:**
- CAP-600: SLO/SLI tracking
- CAP-601: Distributed tracing
- CAP-602: Real-time dashboards
- CAP-603: Alert routing

**IN USE:** Langfuse, custom dashboards

---

## DEPENDENCY RISKS

### Single Points of Failure
1. **claude-code** (143K★) — If this breaks, agent IDE breaks
2. **graphify** (113K★) — If indexing breaks, code intelligence breaks
3. **LangGraph** (40K★) — If agent framework breaks, workflows break

### Soft Dependencies (Nice to have)
- ECC (245K★) — Performance optimization, not critical
- Developer Roadmap (366K★) — Educational, not core

### Unmeasured Dependencies
- Custom forks/internal tools
- Private organizational integrations
- T7 Shield tools (archived, not reflected here)

---

## CAPABILITY COVERAGE

**Out of ~300 capabilities in Company Brain:**

| Coverage | Count | Examples |
|----------|-------|----------|
| ✅ Directly enabled | ~120 | Agent reasoning, code analysis, orchestration, visualization |
| ⚠️ Partially enabled | ~80 | Infrastructure, monitoring, auth |
| ❓ Missing | ~100 | Venture-specific logic, domain expertise, business rules |

**Conclusion:** Company Brain is **40% tool-powered**, **60% domain-specific logic**.

---

## NEXT ACTIONS

1. **Map each capability to starred repos** — Create CAP-* → starred-repo links
2. **Identify reuse opportunities** — Which starred tools can solve new problems?
3. **Audit for upgrades** — Are we on latest versions?
4. **Dependency scanning** — Which tools have breaking changes pending?
5. **Build vs. Buy analysis** — Where should we fork vs. depend?

---

## Capability Links & Dependencies
- **Capabilities Hub:** [[14-CAPABILITIES/CAPABILITIES_INDEX|14-CAPABILITIES (300 Solutions)]]
- **Canonical Capability Registry:** [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]]
- **Dependency Management Architecture:** [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/DEPENDENCY-RISK]]
- **Master Registries Portal:** [[_REGISTRIES/README]]
