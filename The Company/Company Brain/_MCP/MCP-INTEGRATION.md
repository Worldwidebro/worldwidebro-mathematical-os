[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[ANTIGRAVITY]]

# MCP-INTEGRATION.md — Model Context Protocol Architecture & Contracts

**Authority:** Infrastructure & AI Tooling Control Plane (CP-027)  
**Standard:** Model Context Protocol (MCP) v1.0  
**Status:** `VERIFIED_LIVE`  

---

## 1. MCP Topology Overview

Company Brain acts as both an **MCP Consumer** (calling external tools, browsers, routers) and an **MCP Provider** (exposing corporate memory, sector ontologies, deployment triggers, and vector search).

```text
┌────────────────────────────────────────────────────────────────────────┐
│                          ANTIGRAVITY IDE                               │
│                   Workspace & Global Client                            │
└───────────────┬────────────────────────────────────────┬───────────────┘
                │                                        │
      Local Stdio Processes                     Remote HTTP Transport
                │                                        │
 ┌──────────────┴──────────────┐          ┌──────────────┴──────────────┐
 │ - company-brain (FastMCP)   │          │ - browseros-neo (:9012/mcp) │
 │ - omniroute (Bridge stdio)  │          │ - n8n-mcp (Bridge HTTP)     │
 │ - open-knowledge (CLI)      │          │                             │
 └─────────────────────────────┘          └─────────────────────────────┘
```

---

## 2. Server Inventory & Configurations

### 2.1 Core Server: `company-brain` (FastMCP)
- **Path:** `_MCP/fastmcp_server.py`
- **Execution Command:**  
  `/opt/homebrew/bin/uv run --with fastmcp --with pyyaml python3 "/Users/acebless/Documents/The Company/Company Brain/_MCP/fastmcp_server.py"`
- **Health Check Command:**  
  `uv run --with fastmcp --with pyyaml python3 _MCP/fastmcp_server.py --help`
- **Category:** Infrastructure & Corporate Memory
- **Tools Inventory:**
  - `infrastructure_status()`: Queries Tailscale mesh, Mac Studio Docker containers, and core port health. (Read-Only)
  - `infrastructure_deploy(phase)`: Deploys core infrastructure phases (Docker, Neo4j, Qdrant). (Mutating)
  - `omniroute_status()`: Returns live routing stats and active provider endpoints. (Read-Only)
  - `neo4j_status()`: Verifies Bolt connection and node counts. (Read-Only)
  - `neo4j_wire_ontology()`: Synchronizes `SECTOR-TAXONOMY-MASTER.md` into Neo4j graph nodes. (Mutating)
  - `qdrant_search_similar_deals(query, limit)`: Performs vector similarity search over venture prospectus deals. (Read-Only)
  - `test_e2e()`: Executes system-wide connectivity test suite. (Read-Only)

### 2.2 Inference & Model Server: `omniroute`
- **Path:** `/Users/acebless/.omniroute/bin/antigravity-mcp.mjs`
- **Execution Command:**  
  `/opt/homebrew/bin/node /Users/acebless/.omniroute/bin/antigravity-mcp.mjs`
- **Configuration Environment:**
  - `OMNIROUTE_BASE_URL`: `http://100.87.214.70:20128` (or local `http://localhost:20128`)
  - `OMNIROUTE_API_KEY`: `sk-30c31902dc868c0d-9d94e1-e953ae37`
- **Tools Inventory:**
  - `omniroute_get_health()`: Circuit breaker and provider status. (Read-Only)
  - `omniroute_list_combos()`: Failover combinations and weighting policies. (Read-Only)
  - `omniroute_route_request(prompt, model)`: Dispatches prompt through optimal cost/latency combo. (Mutating/Execution)
  - `omniroute_best_combo_for_task(task)`: Recommends cheapest and fastest combo. (Read-Only)
  - `omniroute_cache_stats()`: Context compression and token savings ledger. (Read-Only)

### 2.3 Workflow Automation Server: `n8n-mcp`
- **Path:** `_MCP/n8n_mcp_bridge.py`
- **Execution Command:**  
  `/usr/bin/python3 "/Users/acebless/Documents/The Company/Company Brain/_MCP/n8n_mcp_bridge.py"`
- **Target URL:** `http://100.87.214.70:5678/mcp-server/http`
- **Permissions:** Restricted execution token for automated business workflows.

---

## 3. Security & Permission Boundaries

| Operation Tier | Operations | Tool Examples | Audit Requirements |
|---|---|---|---|
| **Tier 1: Safe Read-Only** | Inspecting status, vector searches, reading nodes, querying telemetry | `infrastructure_status`, `qdrant_search_similar_deals`, `omniroute_get_health` | Logged to `.gemini/antigravity/brain/.../transcript.jsonl` |
| **Tier 2: Non-Destructive Mutating** | Generating vector PDFs, routing chat requests, updating knowledge indices | `scripts/make-pdf`, `omniroute_route_request`, `graphify update` | Git diff / commit check before and after |
| **Tier 3: Destructive / Critical** | Deploying containers, restarting core daemons, overwriting registries | `infrastructure_deploy`, database drops, git push force | **STRICT USER CONFIRMATION REQUIRED** |

---

## 4. Verification Test Commands

```bash
# 1. Test company-brain FastMCP server tool discovery
/opt/homebrew/bin/uv run --with fastmcp --with pyyaml python3 "_MCP/fastmcp_server.py" --help

# 2. Test live infrastructure status via Antigravity native MCP tool invocation
# Tool: company-brain -> infrastructure_status
# Result: Tailscale mesh live (100.87.214.70), Neo4j (:7474), Qdrant (:6333), Exo (:52415) all verified.
```
