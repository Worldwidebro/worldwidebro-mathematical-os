---
title: System Topology — Ports, Routing, Inference, & Dependencies
date: 2026-07-21
version: 1.0
status: ACTIVE
---

# System Topology — Ports, Routing, Inference, & Dependencies

**Master reference for all ports, services, network connections, and what's wired vs. broken.**

---

## Machine Map (Tailscale Network)

```
MacBook Air (this machine)          Mac Studio (100.87.214.70)
├─ 11434: Ollama (0 models) ❌      ├─ 11434: Ollama (qwen2.5:32b, qwen3:8b) ✅
├─ 20128: OmniRoute ✅              ├─ 3004: TwentyHQ
├─ 7474: Neo4j (container)          ├─ 8091: Infisical
├─ 6333: Qdrant (container) ✅      ├─ 6333: Qdrant (separate)
├─ 5432: PostgreSQL (native) ✅     ├─ 6380: Redis
├─ 3001: Grafana ✅                 ├─ 5678: n8n ✅
├─ 80: Caddy ✅                     ├─ 3010: Open WebUI (Ollama UI)
└─ 3100: Loki (logging)             ├─ 8787: MCP Jungle
                                     └─ Docker compose: civos_* stack
```

---

## Port Inventory

### This Machine (MacBook Air — 100.121.17.63)

| Port | Service | Status | Purpose |
|------|---------|--------|---------|
| **20128** | OmniRoute | ✅ LIVE | Central routing layer — Anthropic, Ollama fallback, LiteLLM |
| **11434** | Ollama | ✅ RUNNING | LLM inference — **0 models loaded** ❌ DEAD END |
| **7474** | Neo4j UI | ✅ LIVE | Graph database console (Docker container) |
| **7687** | Neo4j Bolt | ✅ LIVE | Graph queries (bolt://localhost:7687) |
| **6333** | Qdrant | ✅ LIVE | Vector embeddings (Docker container) |
| **5432** | PostgreSQL | ✅ LIVE | Transactional data (native, not Docker) |
| **3001** | Grafana | ✅ LIVE | Dashboards (login broken — creds unknown) |
| **3100** | Loki | ✅ LIVE | Log aggregation (Docker container) |
| **80** | Caddy | ✅ LIVE | Reverse proxy |
| **4000** | LiteLLM | ⏳ DOWN | Model routing (config present, service stopped) |

### Mac Studio (100.87.214.70)

| Port | Service | Status | Notes |
|------|---------|--------|-------|
| **11434** | Ollama | ✅ LIVE | **REAL MODELS:** qwen2.5:32b, qwen3:8b |
| **3004** | TwentyHQ | ✅ LIVE | CRM instance |
| **8091** | Infisical | ✅ LIVE | Secrets management |
| **6333** | Qdrant | ✅ LIVE | Separate vector store |
| **5678** | n8n | ✅ LIVE | Automation workflows |
| **3010** | Open WebUI | ✅ LIVE | Ollama web interface |

---

## Critical Wiring Problem

### Current State (BROKEN)

```
Claude Code / Hermes / Codex
    ↓
OmniRoute (localhost:20128)
    ├─ Ollama backend: localhost:11434 ❌ 0 models
    ├─ Anthropic: configured ✅
    └─ LiteLLM: localhost:4000 ❌ SERVICE DOWN

Hermes Agent (~/.hermes/config.yaml)
    ↓ model.base_url: http://localhost:20128/v1 (points to OmniRoute)
    ↓ fallback: Ollama → localhost:11434 ❌ 0 models

FCC (Free Claude Code)
    ↓ Routes to: localhost:11434 ❌ 0 models
```

### Required State (MUST WIRE)

```
Claude Code / Hermes / Codex / FCC
    ↓
OmniRoute (localhost:20128)
    ├─ Ollama: 100.87.214.70:11434 ✅ [qwen2.5, qwen3]
    ├─ Anthropic fallback: ✅
    └─ exo (distributed): ⏳ pending
```

---

## Wiring Checklist

### TIER 1 — BLOCKS INFERENCE (DO FIRST)
- [ ] **OmniRoute Ollama target** — Change from `localhost:11434` to `100.87.214.70:11434`
  - File: `~/.omniroute/config.json` or `~/.omniroute/.env`
  - Test: `curl http://localhost:20128/health`
  - Verify: `curl -X POST http://localhost:20128/v1/chat/completions -d '{"model":"qwen2.5:32b",...}'` returns response

- [ ] **Hermes → OmniRoute confirmation**
  - File: `~/.hermes/config.yaml`
  - Verify `model.base_url: http://localhost:20128/v1` is set
  - Test: `hermes -c "test" --debug` shows OmniRoute in logs

- [ ] **FCC routing** — Configure to use OmniRoute or Mac Studio Ollama directly
  - Directory: `/Users/acebless/free-claude-code-eval/`
  - Identify: Where does fcc-server load config?
  - Wire: Point to `100.87.214.70:11434` or `localhost:20128`

### TIER 2 — ENABLES SCALE (NEXT 2 WEEKS)
- [ ] **exo clustering** — Activate distributed inference
  - Status: Installed but idle on Mac Studio
  - Setup: `cd ~/exo && source .venv/bin/activate && exo start`
  - Wire: OmniRoute should route to exo cluster

- [ ] **Mac Studio → PostgreSQL sync** — Log inference calls back to database
  - Status: No bidirectional sync yet
  - Add: Inference metrics table + n8n workflow

- [ ] **Prometheus scraping** — Currently only scrapes self
  - Missing targets: LiteLLM (4000), otel-collector, app metrics
  - Add: Prometheus job for each service

- [ ] **Grafana login** — Fix broken authentication
  - Issue: Admin credentials unknown
  - Fix: `docker exec grafana grafana-cli admin reset-admin-password`

### TIER 3 — OBSERVABILITY (LATER)
- [ ] **LiteLLM health** — Restart service, verify in fallback chain
- [ ] **otel-collector** — Add to Prometheus targets
- [ ] **Langfuse wiring** — Instrument apps to export traces

---

## File Dependencies

| File | Depends On | Purpose |
|------|------------|---------|
| `~/.omniroute/config.json` | Mac Studio Ollama IP | OmniRoute routes to correct inference |
| `~/.hermes/config.yaml` | OmniRoute endpoint | Hermes delegates to router |
| `litellm_config.yaml` | Mac Studio Ollama IP | LiteLLM model routing (if restarted) |
| `docker-compose.yml` | Colima Docker, Mac IPs | Container services (Neo4j, Qdrant, etc.) |
| `prometheus.yml` | All service IPs/ports | Metrics collection targets |

---

## Quick Reference: What to Check First

```bash
# 1. Is OmniRoute pointing to Mac Studio?
grep -i "ollama\|11434" ~/.omniroute/config.json ~/.omniroute/.env 2>/dev/null | grep -v localhost

# 2. Is Hermes wired to OmniRoute?
grep "base_url\|provider" ~/.hermes/config.yaml | grep omniroute

# 3. Does OmniRoute respond?
curl http://localhost:20128/health

# 4. Can OmniRoute reach Mac Studio Ollama?
curl http://100.87.214.70:11434/api/tags

# 5. Are all containers running?
docker-compose ps
```

---

## Status Summary

| Layer | Component | Status | Issue |
|-------|-----------|--------|-------|
| **Routing** | OmniRoute | ✅ Running | Points to wrong Ollama |
| **Routing** | Hermes | ✅ Wired to OmniRoute | Good, but OmniRoute broken |
| **Routing** | FCC | ✅ Installed | Unconfigured |
| **Inference** | Mac Studio Ollama | ✅ Live + Models | **Primary source** |
| **Inference** | This machine Ollama | ✅ Running | **No models** |
| **Data** | PostgreSQL | ✅ Live | Transactional store |
| **Graph** | Neo4j | ✅ Live | Knowledge graph |
| **Vector** | Qdrant | ✅ Live | Embeddings |
| **Observability** | Prometheus | ✅ Live | Only scraping self |
| **Observability** | Grafana | ✅ Running | Login broken |

---

## Next Step

1. **Today:** Fix OmniRoute → Mac Studio Ollama IP (TIER 1.1)
2. **Verify Hermes connection** (TIER 1.2)
3. **Configure FCC** (TIER 1.3)
4. **Run end-to-end test:** Ask a question via Claude Code, watch it route through OmniRoute to Mac Studio and return
