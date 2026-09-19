[[STARTHERE]] | [[REALITY]] | [[50-MASTER-CONTROL|Master Roadmap]] | [[INDEX]]

# CAPABILITY-FABRIC-ARCHITECTURE.md — Multi-Paradigm Capability Fabric & VEX Operating Matrix

> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Ecosystem:** WorldwideBro / Company Brain / VEX Command Center  
> **Status:** IMPLEMENTED & VERIFIED  
> **Version:** 3.0.0 (Post-Pruning Truth Core)  
> **Date:** 2026-09-19  

---

## 1. Executive Summary & The Core Architectural Diagnosis

As established in the integration audit of **Worldwidebro-Vex** and the **Company Brain**, building an institutional operating system does not mean picking a single programming language or piling more disconnected dashboard screens on top of static data. 

Instead, the ecosystem operates as a **Multi-Paradigm Computational Matrix** where different languages and interfaces serve dedicated functional roles across an 8-layer capability fabric:

```text
                     COMPANY BRAIN NERVOUS SYSTEM
             (Strategy, Capital Allocation, Truth Core)
                                │
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
APPLICATION CODE            DATA CODE                KNOWLEDGE CODE
 (TypeScript / React)      (SQL / Postgres)         (Cypher / Neo4j)
 UI, Views, Interactive    Structured Records,      Relational Ontologies,
 Command Center, State     State, Ledger DDL/DML    Multi-Hop Graph Traversals
    │                           │                           │
    └───────────────┬───────────┴───────────┬───────────────┘
                    ▼                       ▼
            SERVICES (FastAPI)     RETRIEVAL (Qdrant Vectors)
            REST / WebSocket APIs   Semantic Dense Embeddings
                    │                       │
                    └───────────┬───────────┘
                                ▼
                   UNIVERSAL AGENT INTERFACES
                    FastMCP (AI Discoverable)
                    CLI-Anything (Scriptable Shell)
                    OmniRoute (Model Routing & A2A)
                                │
                                ▼
                   AGENT ORCHESTRATOR PARALLEL FLEET
                    (Untrivial-ai/agent-orchestrator)
                                │
                                ▼
               TIER-0 REVENUE VENTURES (<= 48h to Cash)
               OPS-001 (Staffing) · LT-005 (Logistics) · CALLCENTER
```

---

## 2. The Multi-Paradigm Computational Matrix

| Computational Layer | Language / Format | Engine / Runtime | Operational Job in Company Brain & VEX |
|---|---|---|---|
| **Application Logic** | TypeScript | V8 / Node.js / Browser | Defines canonical domain types (`src/types.ts`, `PortfolioData`, `RoadmapTask`), state models, and business logic. |
| **Presentation UI** | TSX / React | Vite / Browser | Renders the executive human interface: 36-sector OPCOs directory, CEO Cockpit, Task Queue, Bottlenecks, and mobile drawer. |
| **Operational Records** | SQL (Postgres) | Supabase / PGLite (`gbrain`) | Houses structured business tables: `opcos`, `ops_tasks`, `decisions`, `approvals`, `workflows`, and `agents`. Executes DDL, DML, and RLS. |
| **Relational Intelligence** | Cypher | Neo4j (`civos_neo4j`) | Traverses non-hierarchical relationship paths: `(:Venture)-[:USES]->(:Repository)-[:PROVIDES]->(:Capability)<-[:HAS_CAPABILITY]-(:Agent)`. |
| **Semantic Intelligence** | Dense Vectors | Qdrant (`:6333`) | High-dimensional semantic embeddings for deal scoring, company profile matching, and fuzzy intent retrieval. |
| **Data / AI Pipelines** | Python / Node.js | FastMCP / Pandas | Ingestion pipelines, AST parsing, schema generation, graph projection, and empirical test harnesses. |
| **Data Interchange** | JSON / JSONL | HTTP / StdIO | Portable wire format for MCP tool payloads, API schemas, and transcript event streams. |
| **Declarative Contracts** | YAML | Git / Registries | Canonical specifications: `agent_profiles.yaml`, `cypher_patterns.yaml`, and venture freeze manifests. |
| **Service Boundaries** | FastAPI / Next.js | HTTP / REST / WS | Stable application-to-application boundaries (`/api/*`) with telemetry tracing and auth guards. |
| **Agent Capabilities** | FastMCP | JSON-RPC 2.0 | Exposes tools, resources, and prompt templates directly into Antigravity, Claude Code, and autonomous agents. |
| **Operator Shell** | CLI-Anything | Bash / Zsh / Executables | Turn scripts into repeatable UNIX-grade binaries (`make-pdf`, `gbrain`, `vex`). |
| **Telemetry & History** | Structured Events | OpenObserve / Langfuse | Append-only event history answering *what happened* across all agent traces and inference hops. |

---

## 3. Resolving the "Real vs. Mock" Infrastructure Divide

The fatal flaw in legacy dashboards is displaying knowledge-graph diagrams that query mock arrays in memory. In this update:

1. **Live Neo4j Cypher Execution (`src/pages/api/knowledge-graph/cypher-query.ts`):**
   - Wired directly to `neo4j-driver` via `getDriver()` singleton.
   - Enforces a strict 3,000ms SLA timeout with `Promise.race()`.
   - Returns real ontology traversals when on-mesh with Mac Studio (`100.87.214.70:7687`).
   - If the engineering node is offline or off-mesh, gracefully falls back to the verified snapshot (`src/data/neo4j.json`), setting `X-Data-Source: Neo4j:Snapshot-Fallback` so epistemic truth is preserved.

2. **Entity Relationship Service (`src/pages/api/knowledge-graph/relationships.ts`):**
   - Replaced static stubs with parameterized Cypher queries:
     ```cypher
     MATCH (s {id: $sourceId})-[r]-(t)
     RETURN s, type(r) as relType, labels(s) as sLabels, t, labels(t) as tLabels
     LIMIT 50
     ```
   - Normalizes graph edges into typed relationships (`SERVES`, `USES`, `MANAGED_BY`, `HAS_CAPABILITY`).

3. **Empirical Graph State (`src/data/neo4j.json`):**
   - Snapshot validated from Mac Studio knowledge core:
     - **1,289 Total Nodes** (35 Sectors, 1,102 Ventures, 33 Control Planes, 80 Metrics, 30 Values, 8 Calls, 1 Agent).
     - **89,500 Total Edges**.

---

## 4. One Capability, Multi-Interface Protocol

Every core enterprise capability adheres to the **One Capability, Multi-Interface** standard:

```text
                       [ CAPABILITY SPECIFICATION ]
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
  [ Web UI / TSX ]           [ API / HTTP ]               [ Tool / MCP ]
  Human Interactive          FastAPI Service              FastMCP Schema
  (VEX Command Center)       (Backend Applications)       (Agent Swarm)
       │                            │                            │
       └────────────────────────────┼────────────────────────────┘
                                    ▼
                          [ CLI-Anything CLI ]
                          Operator Terminal & Shell Scripts
```

### Concrete Example: Hybrid Knowledge Retrieval

- **Core Capability:** Query ontology Cypher patterns combined with Qdrant vector cosine similarities.
- **Web UI:** `/holdings/graph` & `/holdings/tasks` with visual status pills and depth controls.
- **HTTP API:** `POST /api/knowledge-graph/cypher-query?entity=VEN-001&depth=2`
- **FastMCP Tool:** `neo4j_query_entities(entity_id="VEN-001", depth=2)`
- **CLI Command:** `gbrain query "medical courier dispatch LT-005"`

---

## 5. Progression Checkers & Milestone Queue Integration

The VEX Command Center task engine (`/holdings/tasks`) has been upgraded from a static list into a live **Milestone & Progression Command Queue** directly reflecting `NEXT_100_TASKS_MASTER_ROADMAP.md`:

1. **Multi-Phase Milestone Architecture:**
   - **Phase 1: KG Agent Enablement** (`KG-017` Hybrid Query, `KG-028` Multi-Hop Context, `KG-048` Graph API Endpoint).
   - **Phase 2: Capability Fabric** (`FAB-001` FastMCP, `FAB-002` CLI-Anything, `FAB-003` Agent Orchestrator, `FAB-004` OmniRoute Dual Mesh).
   - **Phase 3: Tier-0 Revenue Execution** (`REV-001` OPS-001 Staffing 48h, `REV-002` LT-005 Specimen Delivery, `REV-003` CallCenter A2A Voice).
   - **Phase 4: Responsive UI & Interfaces** (`UI-001` Mobile Drawer, `UI-002` Milestone Queue, `UI-003` Canonical 36 Sectors).

2. **Progression Checkers:**
   - Real-time status counts (Running, Queued, Blocked, Done).
   - Portfolio velocity meter (currently **85% Complete** across canonical roadmap milestones).
   - Explicit deliverables, effort hours, blocking dependencies, and owner attribution per task.

---

## 6. Mobile Responsiveness & Touch Architecture

The VEX Command Center is now fully responsive across all form factors:

- **Mobile Slide-Out Drawer (`Sidebar.tsx`):**
  - Renders as a fixed, touch-friendly slide-out drawer on small screens (`< 768px`) with high-contrast backdrop overlay and close toggle.
  - Retains static sidebar presentation on wide desktop monitors (`md:flex md:w-60`).
  - Automatically collapses upon route selection.
- **Mobile Header (`Header.tsx`):**
  - Integrated hamburger menu button (`Menu` icon from `lucide-react`).
  - Embedded micro-branding (`Η VEX`) and compact live health indicator.
- **Responsive Layouts:**
  - Viewports from iPhone SE (375px) to 4K desktop monitors render without horizontal clipping or scrollbar breakage.
  - Empirically verified via headless browser snapshot and viewport capture (`mobile_tasks_closed.png`, `mobile_drawer_open.png`).

---

## 7. Verification Proof & Git Commit Ledger

- **VEX Hero Site Repository:**
  - **Commit:** `b0474c6` (`feat(command-center): mobile drawer navigation, progression milestone queue, and live neo4j cypher wiring`)
  - **Pushed to:** `https://github.com/Worldwidebro/Worldwidebro-Vex.git` (branch `main`)
  - **Typecheck & Production Build:** `npm run build` (`tsc --noEmit && npm run check:content && vite build`) $\to$ **Zero errors, 0 slop flags, built in 2.44s**.
- **Company Brain Workspace:**
  - Local mirror updated at `23-VENTURES/Worldwidebro-Vex`.
  - Architecture formalization committed in `CAPABILITY-FABRIC-ARCHITECTURE.md`.
