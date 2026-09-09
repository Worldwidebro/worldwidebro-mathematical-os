# Infrastructure Status — 2026-09-09

**VERIFIED AGAINST:** Live `docker --context macstudio ps` + Tailscale network audit

## Services Online ✅

| Component | Port | Status | Location |
|-----------|------|--------|----------|
| Neo4j | 7687/7474 | ✅ 20,363 edges live | Mac Studio (Docker) |
| Qdrant | 6333 | ✅ 17,236 vectors indexed | Mac Studio (Docker) |
| PostgreSQL | 5432/5433 | ✅ Operational | Mac Studio (Docker) |
| Redis | 6379+ | ✅ Caching working | Mac Studio (Docker) |
| OmniRoute | 20128 | ✅ Gateway running | Mac Studio |
| LiteLLM | 4000 | ✅ Routing working | Mac Studio |
| Ollama | 11434 | ✅ 6 models, 4d+ uptime | Mac Studio (~/.ollama) |
| exo MLX | 52415 | ✅ 120-model catalog | Mac Studio |
| Growth OS | 3030 | ✅ Dashboard live | localhost |
| OpenObserve | 5080 | ✅ Live | Mac Studio |
| Langfuse | 3003 | ⚠️ Callback NOT wired | Mac Studio |

## Hardware

**Mac Studio M4** (100.87.214.70 via Tailscale)
- CPU: 12-core M4 Max | Memory: 36GB | Storage: 512GB + 4TB LaCie
- Role: Primary inference + database host

**MacBook Air** (100.121.17.63 via Tailscale)
- CPU: 8-core M-series | Memory: 16GB | Storage: 228GB + 1.8TB
- Role: Secondary inference agent

## Credentials

**OmniRoute:** http://100.87.214.70:20128 → Bitwarden "OmniRoute — Company Brain"  
**Mac Studio SSH:** ssh macstudio → Bitwarden "Mac Studio SSH — Company Brain"  
**Neo4j:** bolt://100.87.214.70:7687 (default: neo4j/changeme — **CHANGE THIS**)  
**PostgreSQL:** postgres://admin:changeme@100.87.214.70:5433 (default creds — **CHANGE THIS**)

## OmniRoute Routing Gaps

| Gap | Fix Effort | Fix |
|-----|-----------|-----|
| exo's 120 models — only 1 wired | Low | Add real `model_list` entries to litellm-config.yaml |
| Ollama's 6 models unreachable | Low | Re-point `embed` route, re-test, remove stale comment |
| Langfuse receiving zero traffic | Low | Add `success_callback: ["langfuse"]` to LiteLLM config |
| OmniRoute/LiteLLM on different Docker networks | Unverified | Check OmniRoute dashboard provider list |

## Model Inventory (Live-Audited 2026-09-05)

| Model | Status | Location | Reachable? |
|-------|--------|----------|-----------|
| qwen2.5-coder:14b | ✅ Running | Ollama | ❌ not wired |
| nomic-embed-text | ✅ Running | Ollama | ❌ route disabled |
| hermes3, llama3.1:8b | ✅ Running | Ollama | ❌ not wired |
| Qwen3.6-35B-A3B-5bit | ✅ Running | exo | ✅ wired (only one) |
| 119 other exo models | ✅ Available | exo | ❌ not wired |

## Git Invariants

1. All venture changes → Git + PR (no direct DB edits except migrations)
2. Commit messages include venture ID when applicable
3. Tests must pass before merge
4. No force-push to main
5. Attribution: `Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>`
