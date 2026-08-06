---
name: ARCHITECTURE-CONSOLIDATION-ROADMAP
title: Architecture Consolidation Roadmap
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Architecture Consolidation Roadmap

**Goal**: Build 25 shared architecture documents + TAGGING-STANDARD  
**Timeline**: 5-day sprint  
**Enables**: Hermes agent + 712 venture ecosystem  

---

## Why This Matters

**Without it**: Each venture has custom docs, Hermes asks "which venture? what context?" every time, 40% success rate  
**With it**: Hermes loads CON-042 context instantly, 95% success rate, venture launch in <1 hour  

---

## The 25 Core Documents

### Day 1: Foundation (Executive + System)
1. `ARCHITECTURE.md` — Overall 5-layer system
2. `SYSTEM_OVERVIEW.md` — Ventures → vex → Hermes → Intelligence → Ops
3. `DECISION_LOG.md` — ADRs (T7 Shield, Ollama routing, Git sync)
4. `VISION.md` — 712 ventures as $100M+ platform
5. `NORTH_STAR.md` — Templates → Courses → Community → Agency → IP → Software

### Day 2: Domain + Capability
6. `DOMAIN_MODEL.md` — Venture, Repo, Sector, Capability, Function entities + relationships
7. `CAPABILITY_MAP.md` — All capabilities indexed (lead-capture, invoicing, payments, etc.)
8. `SERVICE_CATALOG.md` — vex-api, vex-engine, vex-hero-site, Neo4j, Qdrant, PostgreSQL, Redis, Ollama
9. `ONTOLOGY.md` — 31-sector taxonomy + Hermes entity types
10. `VENTURE-REGISTRY.md` — Lists all 712 ventures with metadata

### Day 3: Standards (How We Code)
11. `CODING_STANDARDS.md` — Multi-venture rule: 3+ uses = shared library
12. `API_STANDARDS.md` — `/ventures/{ventureId}/resources/{resourceId}`
13. `DATA_MODEL.md` — Venture entity + shared tables
14. `SECURITY.md` — Multi-tenancy, RLS, secrets per venture
15. `REPOSITORY_STANDARD.md` — Folder structure every venture must follow

### Day 4: Intelligence + Operations
16. `AI_ARCHITECTURE.md` — Hermes stack: Ollama → vex-api → Neo4j
17. `AGENT_STANDARD.md` — Hermes capability standard, tool definitions
18. `MODEL_ROUTING.md` — When to use qwen3:8b vs Claude API
19. `KNOWLEDGE_GRAPH.md` — Neo4j schema for Hermes queries
20. `RAG.md` — Qdrant retrieval for venture documentation

### Day 5: Operations + Governance
21. `RUNBOOK.md` — Launch venture, connect to Hermes, debug, scale
22. `PLAYBOOK.md` — Incident response, launch day checklist, quarterly review
23. `INFRASTRUCTURE.md` — Mac Studio, T7 Shield, Vercel, PostgreSQL, Redis, Neo4j, Qdrant
24. `CI_CD.md` — GitHub Actions template every venture inherits
25. `OBSERVABILITY.md` — Langfuse for Hermes traces, Vercel analytics, log aggregation

---

## Document Structure Template

```markdown
# [DOCUMENT_NAME]

[Version]   1.0
[Updated]   2026-07-30
[Owner]     Hermes Agent / Claude Code
[Applies]   All ventures (unless noted)

## Overview
[1-2 sentences]

## Key Concepts
- Concept 1
- Concept 2
- Concept 3

## Standards / Rules
[Bullet list of rules that apply everywhere]

## Venture-Specific Overrides
[How ventures customize if needed]

## Examples
[2-3 real ventures using this standard]

## Related Documents
[Links to related 25 docs]
```

---

## Integration with TAGGING-STANDARD.md

Every document reference must use tags:

```markdown
## See Also

- [ARCHITECTURE.md] (foundation)
- [TAGGING-STANDARD.md] (format for every document)
- [VENTURE-REGISTRY.md] (all 712 ventures)
- [HERMES_ROUTING] ([VENTURE], [ACTION], [PRIORITY] format)
```

Every query to Hermes must include:
```
[VENTURE] CON-042
[ACTION] CONNECT
[OBJECTIVE] Enable lead capture
```

---

## How Hermes Uses All 25 Docs

**Scenario**: Connect CON-042 to lead-capture capability

```
User: "[VENTURE] CON-042 [ACTION] CONNECT [OBJECTIVE] lead-capture"
  ↓
Hermes loads (in order):
  1. ARCHITECTURE.md → System structure
  2. VENTURE-REGISTRY.md → CON-042 metadata (repo, owner, status)
  3. DOMAIN_MODEL.md → Venture → Capability relationship
  4. CAPABILITY_MAP.md → lead-capture definition
  5. REPOSITORY_STANDARD.md → CON-042 folder structure
  6. API_STANDARDS.md → Lead create endpoint format
  7. CODING_STANDARDS.md → Shared function location
  8. RAG.md → Retrieve lead-capture implementation docs
  9. AI_ARCHITECTURE.md → Tool definitions
  10. AGENT_STANDARD.md → Agent reasoning loop
  11. KNOWLEDGE_GRAPH.md → Query Neo4j for venture context
  12. CI_CD.md → Run tests after connecting
  13. RUNBOOK.md → Verification checklist
  ↓
Hermes executes:
  1. Load CON-042 from VENTURE-REGISTRY
  2. Find lead-capture in CAPABILITY_MAP
  3. Generate or copy lead-capture implementation
  4. Register function in Neo4j
  5. Update Qdrant with new capability embedding
  6. Run CI/CD tests
  7. Update VENTURE-REGISTRY.json
  ↓
Result: "CON-042 now captures leads via Jotform webhook. Added to capabilities: [lead-capture]. Tests passing. Deployed. Next: configure Stripe webhooks."
```

---

## Implementation Timeline

**Phase 1 (Days 1-5)**: Write 25 docs  
**Phase 2 (Week 2)**: Test with 5 real ventures  
**Phase 3 (Week 3)**: Train Hermes on all 25 docs  
**Phase 4 (Week 4)**: Rollout to all 712 ventures  
**Phase 5 (Ongoing)**: Update as patterns evolve  

---

## Success Metrics

✅ Hermes success rate 95%+ (vs 40% without standards)  
✅ New venture launches in <1 hour (vs 1 day)  
✅ Every venture references one of 25 shared docs  
✅ Cross-venture features deployed to 10+ ventures using shared standard  
✅ Zero venture-to-venture duplicated documentation  

---

---

## Agent OS Layer (10 Documents — Completed 2026-07-30)

Neo4j knowledge graph wired with 200+ relationships + Agent OS complete.

**Docs**:
1. AGENT-BRACKET-STANDARD.md — Agent bracket language
2. AGENT_SPEC.md — 13 agent types + contracts
3. AGENT_PROTOCOL.md — Multi-agent communication
4. AGENT_MEMORY.md — 5 memory types + storage
5. AGENT_PERMISSIONS.md — Authorization LEVEL_0–5
6. AGENT_LIFECYCLE.md — 7 stages (Creation → Retirement)
7. AGENT_EVALUATION.md — KPI framework (success_rate, latency, cost, accuracy)
8. AGENT_ECONOMICS.md — Cost model + ROI + budget
9. AGENT_ONTOLOGY.md — Neo4j schema + Cypher queries
10. VENTURE-ECOSYSTEM-VOCABULARY.md — 200+ relationships

**Integration**: AGENT_SPEC → AGENT_STANDARD (Day 4 #17), AGENT_ONTOLOGY → KNOWLEDGE_GRAPH (Day 4 #19), VENTURE-ECOSYSTEM-VOCABULARY → ONTOLOGY (Day 2 #9)

**Status**: Neo4j live (5,292 nodes, 14,188 edges), ready for Hermes routing + agent provisioning

---

## Files That Reference These 25 Docs

- Every venture's `.claude/CLAUDE.md` references this set
- VENTURE-REGISTRY.json links to relevant docs per venture
- GitHub issue templates auto-link to relevant docs
- Hermes routing table maps [ACTION] → relevant doc subset
- Deployment scripts validate against REPOSITORY_STANDARD.md
- Agent OS docs integrated for dynamic agent + capability discovery
