---
name: System Verification & End-to-End Integration
date: 2026-07-21
status: Ready for Wave 5
part_of: 5-Wave Execution Plan
---

# System Verification & End-to-End Integration

**Purpose:** Rebuild vex-hero-site (npm install/build), wire MCP Ollama config, and prove the entire Neo4j Cypher view system works end-to-end with real query results.

## Core Value

Proof that the 100-map atlas architecture actually works. Real queries return real data. All dependencies resolve and build cleanly. Ready for production scale-out.

## Requirements

### Active — vex-hero-site Rebuild (Wave 5, Task 9)

- [ ] **VERIFY-01**: Run `cd vex-hero-site && npm install` (regenerates node_modules from package-lock.json)
- [ ] **VERIFY-02**: Run `npm run build` (compiles all 16 sector pages + portfolio data)
- [ ] **VERIFY-03**: Verify build succeeds with no errors or warnings
- [ ] **VERIFY-04**: Run `npm run preview` and test in browser: all sector pages render, no console errors
- [ ] **VERIFY-05**: Verify no regressions from disk cleanup or consolidation work

### Active — MCP Ollama Config (Wave 4, Task 7)

- [ ] **VERIFY-06**: Create `~/Iza-OS-Tree-of-Life/agents-global/ollama-mcp/config.json` with live model list
- [ ] **VERIFY-07**: Verify curl `http://localhost:11434/api/tags` returns 3 models (qwen2.5:32b, qwen3:8b, nomic-embed-text)
- [ ] **VERIFY-08**: Wire config into agent routing (Hermes uses Ollama for inference, falls back to Mac Studio if needed)

### Active — Neo4j View Queries (Wave 4, Task 8)

- [ ] **VERIFY-09**: Test CEO view query: aggregate venture MRR + runway across sectors
- [ ] **VERIFY-10**: Test CTO view query: find services by hardware node, dependencies, SLA criticality
- [ ] **VERIFY-11**: Test Finance view query: trace decision approval chains, amounts, thresholds
- [ ] **VERIFY-12**: Verify each query returns non-empty results from live Neo4j data
- [ ] **VERIFY-13**: Document query response times (target: <500ms per view)

### Out of Scope

- Building all 100 views (framework proven with 3-4 examples)
- Updating existing ventures (vex rebuild verifies all data integrates cleanly)
- Tuning Ollama inference performance (baseline only)

## Deliverables

1. **Rebuilt vex-hero-site** — Clean npm build, all pages render in browser
2. **MCP Ollama config** — `config.json` wired and verified with live models
3. **Proof-of-concept Neo4j views** — 3-4 working Cypher queries returning live data
4. **End-to-end integration test report** — All systems verified talking to each other

## Timeline

Wave 5 (Depends on Waves 2, 3, 4 completion).

**Estimated effort:** 2-3 hours (mostly build + query testing, minimal new code).

---

## Related Files

- vex-hero-site: `/Users/acebless/Documents/vex-hero-site`
- Neo4j state: Healthy with 1394 entities ready for querying
- Ollama on Mac Studio: Models confirmed loaded (qwen2.5:32b, qwen3:8b, nomic-embed-text)
- Docker services: All running (Neo4j, Qdrant, LiteLLM, Langfuse, Prometheus, otel-collector)

## Status

🟡 Planned. Depends on Waves 2-4 completion.
