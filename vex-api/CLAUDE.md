# CLAUDE.md — VEX API

**Scope:** REST API for vex-hero-site frontend and agent orchestration  
**Updated:** 2026-08-05  
**Phase:** 3-4 (Data Source → API)  
**Framework:** Node.js/Express or FastAPI (TBD)

---

## What This Repo Does

VEX API provides:
- REST endpoints for venture/capability/sector queries
- Supabase → Neo4j → Qdrant integration
- Graph queries (find ventures by capability)
- Semantic search (find similar ventures)
- Agent dispatch endpoints

---

## Environment Variables

```env
SUPABASE_URL=http://localhost:5432
SUPABASE_ANON_KEY=<from Supabase>
NEO4J_URL=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ventures2026
QDRANT_URL=http://localhost:6333
REDIS_URL=redis://localhost:6379
```

---

## Endpoints (Phase 4+)

```
# Ventures
GET    /api/ventures
GET    /api/ventures/:id
POST   /api/ventures/search

# Capabilities
GET    /api/capabilities
GET    /api/capabilities/:id

# Graph Queries
POST   /api/graph/ventures-by-capability
POST   /api/graph/agents-for-capability
POST   /api/graph/repos-for-capability

# Search (Qdrant)
POST   /api/search
```

---

## Phase Gates

| Phase | Deliverable |
|-------|-------------|
| **3** | Supabase connection verified |
| **4** | /api/ventures, /api/capabilities live |
| **5** | Neo4j graph queries wired |
| **6** | Qdrant semantic search working |

---

## Commands

```bash
npm install
npm run dev          # Start :3000
npm run build
npm run test
npm run docs         # Generate OpenAPI docs
```

---

## Critical Rules

1. **Supabase is SOT** — Never cache venture data longer than 5 min.
2. **Neo4j queries must be fast** — Use indexes, avoid full scans.
3. **All responses must validate** — Use Zod or Pydantic.
4. **Rate limit all endpoints** — 100 req/min default, 1000 authenticated.

---

## Related

- Root CLAUDE.md: `~/.claude/CLAUDE.md`
- VEX Core: `/Users/acebless/Documents/vex`
- VEX Engine: `/Users/acebless/Documents/vex-engine`
