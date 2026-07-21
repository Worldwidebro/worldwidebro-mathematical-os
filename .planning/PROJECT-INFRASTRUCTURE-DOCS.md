---
name: Infrastructure Documentation & 100-Map Atlas
date: 2026-07-21
status: Ready for Wave 3
part_of: 5-Wave Execution Plan
---

# Infrastructure Documentation & 100-Map Atlas

**Purpose:** Create the architecture atlas — 5 comprehensive topology documents + Neo4j schema enhancements that enable 100+ dynamic Cypher views on demand (CEO view, CTO view, Finance view, etc.).

## Core Value

A single source of truth for infrastructure state. Neo4j becomes the query engine; the 5 docs are the reference views that prove the model works. Future "maps" (compliance view, cost view, vendor view, threat model view) query the same graph without new documents.

## Requirements

### Active — Documentation (Wave 3, Task 4)

- [ ] **INFRA-01**: Create `NETWORK_TOPOLOGY.md` (Tailscale network map, all ports, service endpoints, device addressing)
- [ ] **INFRA-02**: Create `SERVICE_TOPOLOGY.md` (Docker services, ports, health status, dependencies)
- [ ] **INFRA-03**: Create `DATA_FLOW_MAP.md` (Supabase → PostgreSQL → Neo4j → Qdrant → Ollama → Hermes agents → Audit trail)
- [ ] **INFRA-04**: Create `AGENT_COMMUNICATION_MAP.md` (Hermes CEO agent orchestrating 232 Agency Agents, skill framework hierarchy)
- [ ] **INFRA-05**: Create `SECURITY_ACCESS_MAP.md` (Permission hierarchy, approval thresholds, audit matrix)

### Active — Topology Rewrites (Wave 3, Task 5)

- [ ] **INFRA-06**: Rewrite `TOPOLOGY.md` (v1.0 → v2.0) to operational state with cross-references to 5 new docs
- [ ] **INFRA-07**: Rewrite `TOPOLOGY-WITH-EXO-AND-T7.md` (v2.0 → v3.0) with T7 storage + Ollama + Mac Studio integration

### Active — Reference Rules (Wave 3, Task 6)

- [ ] **INFRA-08**: Create `.claude/rules/graphify.md` (graph reference usage, best practices)
- [ ] **INFRA-09**: Create `.claude/rules/ollama-topology.md` (Ollama network/storage topology for agent routing)

### Active — Neo4j Schema (Wave 4, Task 8)

- [ ] **INFRA-10**: Add 9 new entity labels: `Hardware`, `Storage`, `Application`, `Service`, `Process`, `Team`, `Decision`, `DataSource`, `Pipeline`
- [ ] **INFRA-11**: Add relationships: `RUNS_ON`, `STORED_ON`, `DEPENDS_ON`, `BELONGS_TO`, `APPROVES`, `FOLLOWS`, `FLOWS_TO`, `PRODUCES`
- [ ] **INFRA-12**: Seed with real current data (2 Hardware, 1 Storage, live services)
- [ ] **INFRA-13**: Write 3-4 example Cypher queries (CEO, CTO, Finance views) proving on-demand generation works
- [ ] **INFRA-14**: Document Neo4j query patterns in `.claude/rules/neo4j-views.md`

### Out of Scope

- Building all 100 maps (only 3-4 examples + framework)
- Migrating existing data to new schema (additive only)
- Rewriting infrastructure (docs describe current state only)

## Deliverables

1. **5 new topology docs** — `NETWORK_TOPOLOGY.md`, `SERVICE_TOPOLOGY.md`, `DATA_FLOW_MAP.md`, `AGENT_COMMUNICATION_MAP.md`, `SECURITY_ACCESS_MAP.md`
2. **2 rewritten topology docs** — `TOPOLOGY.md` (v2.0), `TOPOLOGY-WITH-EXO-AND-T7.md` (v3.0)
3. **2 rules files** — `.claude/rules/graphify.md`, `.claude/rules/ollama-topology.md`
4. **Neo4j schema extension** — 9 entity types, 8 relationship types, seeded with real data
5. **Example Cypher views** — 3-4 working queries proving CEO/CTO/Finance views work

## Timeline

Wave 3 (Parallel with Wave 2 code consolidation).

**Estimated effort:** 4-5 hours (mostly writing + Neo4j schema modeling).

---

## Related Files

- Existing TOPOLOGY.md: Foundation for v2.0 rewrite
- Neo4j current state: 1394 entities, 1376 relationships (ready for expansion)
- Docker services status: All healthy (from S632 infrastructure audit)

## Status

🟡 Planned. Depends on Wave 0 disk cleanup.
