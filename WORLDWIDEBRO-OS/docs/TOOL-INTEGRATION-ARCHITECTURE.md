# AI Boss OS Tool Integration Architecture

**Date:** 2026-07-20  
**Purpose:** Complete nervous system map for all tools, MCPs, services, agents in the 712-venture OS

---

## Overview: The Nervous System

AI Boss OS integrates 22+ tools across 7 layers:

```
VENTURES (712) → AGENTS → TASKS → TOOLS → MEMORY → OBSERVABILITY
```

All connected via tool registries and health checks.

---

## Tool Registries

| Registry | Purpose | Location |
|---|---|---|
| tools-registry.yaml | Master tool inventory + health checks | `WORLDWIDEBRO-OS/08-DATA/registries/` |
| MCP_REGISTRY.json | All available MCPs | `/Documents/` |
| TOOL_CAPABILITY_MAP.md | Business goals → MCPs | `/Documents/` |
| REPOSITORY-REGISTRY.json | 1,639 repos + capabilities | `WORLDWIDEBRO-OS/08-DATA/` |

---

## Layer 1: Repository Intelligence

Convert codebases into structured knowledge:

| Tool | Input | Output | Used By |
|---|---|---|---|
| Repomix | Git repo | XML context | Coding agent |
| Serena | Codebase | Symbol index | Symbol resolver |
| SocratiCode | Repository | Neo4j + vectors | Semantic search |
| GitNexus | Repo | Dependency graph | Impact analyzer |

---

## Layer 2: AI Model Routing

| Component | Purpose | Config |
|---|---|---|
| LiteLLM | Route requests to best model | litellm_config.yaml |
| Ollama | Run local LLMs | Mac Studio:11434 |
| Claude API | Cloud fallback | ANTHROPIC_API_KEY |

---

## Layer 3: Agents & Tasks

### Core Agents (LIVE)

| Agent | Purpose | Status |
|---|---|---|
| Agent Factory | Spawn ventures | Live |
| Hermes | Route decisions | Live |
| Orchestrator | Execute tasks | Live |

### Task Types

| Task | Agent | Status |
|---|---|---|
| compile-outreach | AG-CEO | ✅ Wired |
| db-dedupe | AG-CAO | ✅ Wired |
| repo-scan | AG-CTO | ✅ Wired |
| estimate-job | AG-CEO | ❌ Needs wiring |
| risk-score | AG-CFO | ❌ Needs wiring |
| dispatch-job | AG-LOG | ❌ Needs wiring |

**Path to 50 tasks:** 40 hours wiring.

---

## Layer 4: Observability

| Service | Purpose | Port | Status |
|---|---|---|---|
| Langfuse | Trace LLM calls | 3003 | Running |
| Prometheus | Metrics | 9090 | Running (1 target) |
| Grafana | Dashboards | 3001 | Running (login issue) |
| OpenTelemetry | Trace collection | 4317 | Running (not wired) |

---

## Layer 5: Memory

### Vector Search (Qdrant)

| Collection | Size | Purpose |
|---|---|---|
| repositories | 1,648 vectors | Find repos by meaning |
| notes | 15,558 vectors | Find knowledge |
| capabilities | 250 vectors | Find features |

### Knowledge Graph (Neo4j)

| Entity | Count |
|---|---|
| Ventures | 712 |
| Repositories | 1,639 |
| Capabilities | 25 |
| Relationships | 10,000+ |

---

## Layer 6: Data

| Database | Purpose | Records |
|---|---|---|
| Supabase | Operational data | 712 ventures + logs |
| DuckDB | Analytics | Fast queries |

---

## Layer 7: Automation

| Platform | Purpose | Status |
|---|---|---|
| n8n | Workflow orchestration | Running |
| Zapier | Cloud integration | Available |

---

## Data Flow Example: Construction Estimate

```
1. Inquiry received → n8n webhook
2. Classify: Hermes routes to "construction_estimate"
3. Authority: $1000 estimate = "auto_approve"
4. Execute: Task "estimate-job"
   - Repomix packages past estimates
   - Serena loads pricing logic
   - SocratiCode queries: "Similar jobs"
   - LiteLLM routes to qwen2.5
   - Output: "$3,500 estimate"
5. Trace: Langfuse logs (tokens, cost, latency)
6. Log: Supabase records decision + execution
7. Dashboard: Grafana updates (tasks completed, avg time, revenue)
```

---

## Health Check

Run daily:

```bash
./WORLDWIDEBRO-OS/scripts/check-tools.sh
```

Shows:
- ✓ Healthy tools
- ⚠ Warnings (not running)
- ✗ Critical (not installed)

---

## Next 30 Days

- Week 1: Fix observability wiring (Prometheus, Grafana, OTEL)
- Week 2: Wire 10+ task types
- Week 3: Validate data integrity
- Week 4: Build CEO dashboard

**Total effort:** ~60 hours

---

## Summary

✅ 22 tools integrated  
✅ 3 agents live  
✅ 4 memory systems running  
✅ 1,639 repos indexed  
✅ 712 ventures ready  

⏳ 47 task types need wiring (40 hours)  
⏳ Observability not fully wired (20 hours)  

*This is the nervous system that keeps AI Boss OS aware and responsive.*
