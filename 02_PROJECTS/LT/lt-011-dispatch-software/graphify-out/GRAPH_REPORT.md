---
name: 02_PROJECTS/LT/lt-011-dispatch-software/graphify-out/GRAPH_REPORT
title: Graph Report - lt-011-dispatch-software  (2026-08-05)
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Graph Report - lt-011-dispatch-software  (2026-08-05)

## Corpus Check
- 20 files · ~12,790 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 270 nodes · 318 edges · 26 communities (24 shown, 2 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 5 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9821deb9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]

## God Nodes (most connected - your core abstractions)
1. `WorkflowState` - 12 edges
2. `8. Core Pages` - 12 edges
3. `str` - 11 edges
4. `compilerOptions` - 11 edges
5. `Any` - 10 edges
6. `5. User Personas` - 9 edges
7. `13. Agent Responsibilities` - 9 edges
8. `36. Phase Roadmap` - 9 edges
9. `37. North-Star Metrics` - 9 edges
10. `LLMGateway` - 7 edges

## Surprising Connections (you probably didn't know these)
- `test_llm_gateway_structured_generation_and_fallback()` --calls--> `LLMGateway`  [INFERRED]
  agents/test_llm_gateway.py → agents/llm_gateway.py
- `test_end_to_end_dispatch_workflow()` --calls--> `Location`  [INFERRED]
  agents/test_dispatch_engine.py → agents/dispatch_engine.py
- `test_end_to_end_dispatch_workflow()` --calls--> `Load`  [INFERRED]
  agents/test_dispatch_engine.py → agents/dispatch_engine.py
- `test_end_to_end_dispatch_workflow()` --calls--> `WorkflowEngine`  [INFERRED]
  agents/test_dispatch_engine.py → agents/dispatch_engine.py
- `CarrierMatchDecision` --uses--> `LLMGateway`  [INFERRED]
  agents/test_llm_gateway.py → agents/llm_gateway.py

## Import Cycles
- None detected.

## Communities (26 total, 2 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (40): 10. Order Model, 11. Freight Model, 12. Agent Architecture, 14. Agentic Workflow Architecture, 15. Core Workflow: Order to Delivery, 16. Exception Workflow, 18. Skills Architecture, 19. MCP Architecture (+32 more)

### Community 1 - "Community 1"
Cohesion: 0.12
Nodes (20): BillingAgent, Carrier, CarrierMatcherAgent, ConfirmationAgent, DispatchAgent, EvaluatorAgent, ExceptionHandlerAgent, Load (+12 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (20): dependencies, axios, cors, dotenv, express, @supabase/supabase-js, description, devDependencies (+12 more)

### Community 3 - "Community 3"
Cohesion: 0.23
Nodes (10): LLMExecutionTrace, LLMGateway, float, str, Simulates LLM API call, returning json matching the Pydantic schema structure., CarrierMatchDecision, test_llm_gateway_structured_generation_and_fallback(), BaseModel (+2 more)

### Community 4 - "Community 4"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, module, moduleResolution, outDir, resolveJsonModule, rootDir (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.17
Nodes (12): 8. Core Pages, Agent Control, Customer, Dispatch, Driver, Executive, Finance, Fleet (+4 more)

### Community 6 - "Community 6"
Cohesion: 0.20
Nodes (9): 1. Where to Bid on Freight Loads, 2. Where to Source and Dispatch Owner-Operators, 3. The Bidding & Dispatching SOP, A. Carrier Directories, A. High-Volume Commercial Load Boards (Spot Market), B. Brokerage Directories & Portals (Contract & Route Bidding), B. Fleet & Truck Rentals (For Short-Term Dispatch), C. Government & Institutional Bidding (High-Value / Low-Risk) (+1 more)

### Community 7 - "Community 7"
Cohesion: 0.22
Nodes (9): 13. Agent Responsibilities, BILLING_AGENT, DISPATCH_AGENT, EXCEPTION_AGENT, FREIGHT_AGENT, MATCHING_AGENT, ORDER_AGENT, ROUTING_AGENT (+1 more)

### Community 8 - "Community 8"
Cohesion: 0.22
Nodes (9): 36. Phase Roadmap, Phase 0 — Foundation, Phase 1 — Dispatch MVP, Phase 2 — Tracking, Phase 3 — Documents & Billing, Phase 4 — Agentic Operations, Phase 5 — Freight, Phase 6 — Intelligence (+1 more)

### Community 9 - "Community 9"
Cohesion: 0.22
Nodes (9): 37. North-Star Metrics, Agentic, Automation, Customer, Efficiency, Financial, Operational, Reliability (+1 more)

### Community 10 - "Community 10"
Cohesion: 0.22
Nodes (9): 5. User Personas, Carrier, Customer, Dispatcher, Driver, Executive, Fleet Manager, Freight Broker (+1 more)

### Community 11 - "Community 11"
Cohesion: 0.25
Nodes (7): 1. System Topology, 2. MCP Layer Contracts, 3. Capability Graph Integration, DispatchOS System Architecture, Documents MCP (`mcp/documents`), GPS MCP (`mcp/gps`), Maps MCP (`mcp/maps`)

### Community 12 - "Community 12"
Cohesion: 0.25
Nodes (7): 1. Target Customer Profile (SaaS & Brokerage), 2. Prospect List (High-Priority North Carolina Targets), 3. Call Scripts (Outbound Outreach), 4. Daily Outreach Rhythm (Schedule to Revenue), DispatchOS Sales Leads & Outreach Guide, Script A: Target is a Trucking Fleet (Selling SaaS), Script B: Target is a Freight Brokerage (Selling automation & integrations)

### Community 13 - "Community 13"
Cohesion: 0.25
Nodes (6): axios, path, server, serverPath, { spawn }, tsNodePath

### Community 14 - "Community 14"
Cohesion: 0.29
Nodes (6): 1. State Transitions, 2. Entity Database Schema Mapping, 3. Financial Settlement Formula, A. Load State Machine, B. Tender State Machine, DispatchOS Domain Model Specifications

### Community 15 - "Community 15"
Cohesion: 0.33
Nodes (6): 17. Agent Permissions, Level 0 — Observe, Level 1 — Low-risk execution, Level 2 — Operational execution, Level 3 — Financial actions, Level 4 — Restricted

### Community 16 - "Community 16"
Cohesion: 0.33
Nodes (6): 26. Analytics, Agents, Customers, Fleet, Freight, Operations

### Community 17 - "Community 17"
Cohesion: 0.33
Nodes (6): 33. Non-Functional Requirements, Auditability, Availability, Observability, Performance, Recoverability

### Community 18 - "Community 18"
Cohesion: 0.33
Nodes (6): 4. Target Customers, Freight companies, Logistics companies, Primary customers, Specialized transportation, Transportation companies

### Community 19 - "Community 19"
Cohesion: 0.40
Nodes (5): 7. MVP Scope, Deferred, MVP modules, MVP workflow, Required

### Community 20 - "Community 20"
Cohesion: 0.40
Nodes (4): 1. Order-to-Delivery Workflow (Logistics Core), 2. Freight Tendering Workflow (Carrier/Broker Integration), 3. Exception Resolution Workflow (Durable Agent Recovery), DispatchOS Agentic Workflows

### Community 21 - "Community 21"
Cohesion: 0.50
Nodes (3): Architecture, LT-011: DispatchOS — Dispatch, Logistics & Freight Core, System Positioning

### Community 23 - "Community 23"
Cohesion: 0.50
Nodes (3): builds, routes, version

### Community 24 - "Community 24"
Cohesion: 0.50
Nodes (3): orgId, projectId, projectName

## Knowledge Gaps
- **169 isolated node(s):** `projectId`, `orgId`, `projectName`, `float`, `float` (+164 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `8. Core Pages` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `5. User Personas` connect `Community 10` to `Community 0`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `13. Agent Responsibilities` connect `Community 7` to `Community 0`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **What connects `projectId`, `orgId`, `projectName` to the rest of the system?**
  _170 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.04878048780487805 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.12312312312312312 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._