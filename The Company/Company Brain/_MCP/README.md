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

**Next Steps:**
1. Upgrade Python to 3.10+
2. Install FastMCP
3. Update Claude Code settings
4. Test with `infrastructure_status()`
