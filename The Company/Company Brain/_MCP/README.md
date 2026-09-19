---
id: PORTAL-MCP-SERVER-001
title: "Company Brain FastMCP Server Gateway"
aliases: ["_MCP", "_MCP/README", "FastMCP Server", "Company Brain MCP"]
tags: ["mcp", "fastmcp", "tools", "infrastructure", "api"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_INFRASTRUCTURE/README|Operational Infrastructure]] | [[18-TOOLS/README|18-TOOLS]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[CLAUDE]]

# Company Brain FastMCP Server

> **Framework:** [FastMCP](https://github.com/PrefectHQ/fastmcp) (Official MCP framework)  
> **Authority:** Infrastructure Control Plane ([[CP-027]])  
> **Connected Registry:** [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]] & [[_REGISTRIES/tools/README|Tools Registry]]  
> **Status:** 🟢 ACTIVE — Ready for Python 3.10+ upgrade

---

## What is FastMCP?

FastMCP is the standard MCP (Model Context Protocol) framework. It powers 70% of MCP servers globally and handles:
- **Servers** — Expose tools, resources, and prompts to LLMs
- **Clients** — Connect to any MCP server with full protocol support
- **Apps** — Interactive UIs rendered in the conversation

---

## Company Brain MCP Server

This server exposes Company Brain infrastructure as MCP tools, allowing Claude Code and other LLM clients to directly control:
- Infrastructure deployment (phases 1-4)
- Service health monitoring
- Knowledge graph wiring
- Control plane synchronization
- Sector information queries

### Available Tools

| Tool | Purpose |
|------|---------|
| `infrastructure_status()` | Check all service health (OmniRoute, Neo4j, Qdrant, Ollama) |
| `infrastructure_deploy(phase)` | Deploy databases, models, exo, or observability |
| `omniroute_status()` | Check AI gateway |
| `neo4j_status()` | Check knowledge graph |
| `neo4j_wire_ontology()` | Wire ontology relationships |
| `test_e2e()` | Run integration tests |
| `test_models()` | List available models |
| `control_planes_sync()` | Synchronize all 6 control planes |
| `get_sector_info(sector_id)` | Get sector details |

### Available Resources

- `company_brain_status` — Current activation status

### Available Prompts

- `setup_company_brain` — Guided setup prompt

---

## Installation

### Step 1: Upgrade Python (REQUIRED)

FastMCP requires Python ≥ 3.10. Current environment is 3.9.6.

**Option A: Use pyenv (Recommended)**
```bash
# Install Python 3.12 (latest stable)
pyenv install 3.12.0
pyenv local 3.12.0
python3 --version  # Should show 3.12.0

# Create a venv for Company Brain
python3 -m venv /Users/acebless/.venv/company-brain
source /Users/acebless/.venv/company-brain/bin/activate
```

**Option B: Use Homebrew**
```bash
brew install python@3.12
/usr/local/opt/python@3.12/bin/python3 -m venv /Users/acebless/.venv/company-brain
source /Users/acebless/.venv/company-brain/bin/activate
```

**Option C: Use Conda**
```bash
conda create -n company-brain python=3.12
conda activate company-brain
```

### Step 2: Install FastMCP

```bash
# Activate the venv (if not already)
source /Users/acebless/.venv/company-brain/bin/activate

# Install FastMCP
pip install fastmcp

# Verify installation
python3 -c "import fastmcp; print(f'FastMCP {fastmcp.__version__} ready')"
```

### Step 3: Configure Claude Code

Add this to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "company-brain": {
      "command": "/Users/acebless/.venv/company-brain/bin/python3",
      "args": [
        "_MCP/fastmcp_server.py"
      ],
      "cwd": "/Users/acebless/Documents/The Company/Company Brain"
    }
  }
}
```

Then restart Claude Code to load the server.

### Step 4: Verify Installation

In Claude Code, try:
```
infrastructure_status()
```

Should return JSON with OmniRoute, Neo4j, Qdrant, Ollama status.

---

## Usage Examples

### Check Infrastructure Health
```python
result = infrastructure_status()
print(result["output"])
```

### Deploy Phase 1 (Databases)
```python
result = infrastructure_deploy(phase="1")
# Wait for Neo4j, Qdrant, PostgreSQL, Redis to start
```

### Wire Neo4j Ontology
```python
result = neo4j_wire_ontology()
# Creates relationships between control planes
```

### Run E2E Tests
```python
result = test_e2e()
# Verifies all services respond correctly
```

### Synchronize Control Planes
```python
result = control_planes_sync()
# Updates all 6 control planes in Neo4j
```

---

## Architecture

```
Claude Code / LLM Client
        ↓
   FastMCP Server (stdio transport)
        ↓
   Company Brain Tools
        ↓
   CLI (_CLI/bin/cb)
        ↓
   Docker Services (OmniRoute, Neo4j, Qdrant, etc.)
```

---

## Files

- `fastmcp_server.py` — MCP server implementation (10 tools, 1 resource, 1 prompt)
- `mcp-config.json` — Configuration template for Claude Code
- `README.md` — This file

---

## Requirements

| Component | Version | Status |
|-----------|---------|--------|
| Python | ≥3.10 | ⏳ Upgrade needed |
| FastMCP | Latest | ⏳ Install after upgrade |
| Company Brain CLI | Latest | ✅ Ready |
| Docker | Latest | ✅ Running |

---

## Authority

Infrastructure Control Plane (CP-027)

**Related Control Planes:**
- CP-006: Agent Routing
- CP-007: Model Selection
- CP-013: Knowledge Graph
- CP-020: Financial Tracking
- CP-029: Observability

---

## References

- [FastMCP Documentation](https://gofastmcp.com)
- [Model Context Protocol Spec](https://modelcontextprotocol.io)
- [Company Brain CLAUDE.md](../CLAUDE.md)
- [Company Brain CLI](../README.md)

---

## Documentation & Specification Matrix

### Core Specifications & Integration Protocols
- [[_MCP/AAS_CORE_MCP_SPEC|AAS Core MCP Spec]] — Autonomous Agent System core MCP specification.
- [[_MCP/AGENT_QUICK_REFERENCE|Agent Quick Reference]] — Fast reference for tool invocation and schema mapping.
- [[_MCP/CLAUDE-CODE-OMNIROUTE-INTEGRATION|Claude Code OmniRoute Integration]] — Direct Claude Code connection to OmniRoute.
- [[_MCP/CODE-SEARCH-STRATEGY|Code Search Strategy]] — Hybrid lexical and AST search architecture.
- [[_MCP/CONVERSION_DECISION_TREE|Conversion Decision Tree]] — Decision logic for data and format conversions.
- [[_MCP/DEALFLOW_NEO4J_API|DealFlow Neo4j API]] — Neo4j endpoints and Cypher schemas for DealFlow.
- [[_MCP/DEALFLOW_POSTGRES_SETUP|DealFlow Postgres Setup]] — PostgreSQL relational schema and indexing.
- [[_MCP/EXECUTE-ON-MAC-AIR|Execute on Mac Air]] — Field execution runbook for mobile engineering node.
- [[_MCP/FILE_CONVERSION_SERVICE|File Conversion Service]] — Document parsing and Markdown compilation pipeline.
- [[_MCP/OMNIROUTE-CLAUDE-CODE-ARCHITECTURE|OmniRoute Claude Code Architecture]] — Dual-plane proxy architecture.
- [[_MCP/OMNIROUTE-MCP-WIRING|OmniRoute MCP Wiring]] — FastMCP socket configuration and server startup.
- [[_MCP/OMNIROUTE_A2A_AGENT_FLOW|OmniRoute A2A Agent Flow]] — Agent-to-Agent message passing and task delegation.
- [[_MCP/OMNIROUTE_AGENT_HOOKUP_SUMMARY|OmniRoute Agent Hookup Summary]] — Swarm activation summary.
- [[_MCP/OMNIROUTE_DEALFLOW_INTEGRATION|OmniRoute DealFlow Integration]] — CRM pipeline synchronization via MCP.
- [[_MCP/PHASE3_IMPLEMENTATION|Phase 3 Implementation]] — Long-term MCP tool rollout and lifecycle.
- [[_MCP/PHASE_1_EXECUTION_PLAN|Phase 1 Execution Plan]] — Phase 1 deployment and validation checklist.
- [[_MCP/QDRANT_DEAL_DISCOVERY_SETUP|Qdrant Deal Discovery Setup]] — Vector similarity search for opportunities.
- [[_MCP/QUICK-START-OMNIROUTE|Quick Start OmniRoute]] — Rapid onboarding and test commands.
- [[_MCP/REAL-AGENT-BLUEPRINT|Real Agent Blueprint]] — Production agent specification with strict grounding.
- [[_MCP/SESSION-SUMMARY-2026-09-17|Session Summary (2026-09-17)]] — Architecture decision checkpoint.
- [[_MCP/SYSTEMS-INTEGRATION-MASTER|Systems Integration Master]] — Ecosystem-wide integration topology.

### Capability Units 10–17 Specifications
- [[_MCP/UNIT-10-SEARCH-CAPABILITIES-SPEC|Unit 10: Search Capabilities]] — Dynamic registry query protocol.
- [[_MCP/UNIT-11-EXECUTE-CAPABILITY-SPEC|Unit 11: Execute Capability]] — Execution engine and parameter passing.
- [[_MCP/UNIT-12-ANTHROPIC-PLUGIN-WIRING-SPEC|Unit 12: Anthropic Plugin Wiring]] — Claude tool use mapping.
- [[_MCP/UNIT-13-ORCHESTRATOR-SPEC|Unit 13: Orchestrator Spec]] — Master workflow coordination specification.
- [[_MCP/UNIT-14-E2E-TEST-SPEC|Unit 14: E2E Test Spec]] — Automated testing framework for tool interfaces.
- [[_MCP/UNIT-15-ERROR-RECOVERY-SPEC|Unit 15: Error Recovery Spec]] — Fallback logic, circuit breakers, and retries.
- [[_MCP/UNIT-16-PERFORMANCE-BASELINE|Unit 16: Performance Baseline]] — Latency targets and throughput thresholds.
- [[_MCP/UNIT-17-PRODUCTION-DEPLOYMENT|Unit 17: Production Deployment]] — Final deployment and monitoring checklist.

---

**Next Steps:**
1. Upgrade Python to 3.10+
2. Install FastMCP
3. Update Claude Code settings
4. Test with `infrastructure_status()`
