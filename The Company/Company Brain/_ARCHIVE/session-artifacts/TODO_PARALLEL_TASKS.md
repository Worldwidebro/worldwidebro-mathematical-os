# Company Brain — Parallel Task Breakdown

[[00-CONSTITUTION]] | [[INDEX-DOMAINS-COMPLETE]]

**Goal:** Complete Company Brain framework and implement first revenue loop  
**Model:** 36-sector taxonomy grounded in VEX venture data + federated knowledge graph  
**Execution:** Loop Engineering (L1 report-only, graduate to L2/L3 after validation)

---

## PHASE 2: VEX CROSSWALK (Blocking for Phases 3+)

**Objective:** Map 500+ ventures to canonical 36-sector taxonomy; identify gaps; validate sector assignments.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 2.1: Audit VEX venture registry schema | Data Engineer | None | ✓ | 2h |
| 2.2: Extract venture list + current sector assignments | Data Engineer | 2.1 | ✓ | 1h |
| 2.3: Map 14 existing sectors to canonical 36 | Analyst | 2.2 | ✓ | 2h |
| 2.4: Classify 22 gap sectors (ventures with no assignment) | Analyst | 2.2 | ✓ | 3h |
| 2.5: Identify ventures not fitting 36-sector model | Analyst | 2.4 | ✓ | 1h |
| 2.6: Validate consolidation of TC (21 + 30 → single sector) | Analyst | 2.3 | - | 1h |
| 2.7: Publish canonical 36-sector-to-venture mapping | Data Engineer | 2.3-2.6 | - | 1h |

**Parallel groups:** 2.1-2.2 (2 eng), 2.3-2.5 (2 analyst). 2.6-2.7 sequential.

---

## PHASE 3A: REGISTRY HIERARCHY (Parallel after 2.7)

**Objective:** Create authoritative source of truth: Sector → Industry → Market → OpCo → Venture.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 3A.1: Design registry schema (5-level hierarchy) | Architect | Phase 2.7 | - | 2h |
| 3A.2: Create PostgreSQL `registry_sector` | DBA | 3A.1 | ✓ | 1h |
| 3A.3: Create PostgreSQL `registry_industry` | DBA | 3A.1 | ✓ | 1h |
| 3A.4: Create PostgreSQL `registry_market` | DBA | 3A.1 | ✓ | 1h |
| 3A.5: Create PostgreSQL `registry_opco` | DBA | 3A.1 | ✓ | 1h |
| 3A.6: Populate `registry_sector` (36 sectors) | Data Eng | 3A.2 + 2.7 | - | 1h |
| 3A.7: Populate `registry_industry` from VEX | Data Eng | 3A.3 + 2.2 | - | 2h |
| 3A.8: Populate `registry_market` (infer from ventures) | Data Eng | 3A.4 | - | 3h |
| 3A.9: Populate `registry_opco` (existing assignments) | Data Eng | 3A.5 + 2.7 | - | 2h |
| 3A.10: Create validation views | DBA | 3A.6-3A.9 | ✓ | 1h |
| 3A.11: Audit: Verify venture counts match VEX | QA | 3A.6-3A.10 | - | 1h |

**Parallel groups:** 3A.2-3A.5 (4 DBA), 3A.6-3A.9 (2 eng, mostly seq), 3A.10-3A.11.

---

## PHASE 3B: SECTOR WIKI PAGES (Parallel after 3A.6)

**Objective:** Create 36 wiki pages (one per sector) + index + navigation.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 3B.1: Create `SECTOR_TAXONOMY.md` (canonical ref) | Writer | Phase 2.7 | - | 2h |
| 3B.2: Create sector template (OpCo, Industries, Ventures, etc.) | Writer | 3B.1 | - | 1h |
| 3B.3: Generate 36 sector markdown files (SEC-001.md through SEC-036.md) | Automation | 3B.2 | ✓ | 2h |
| 3B.4: Populate sectors with data from registries (bulk) | Automation | 3B.3 + 3A.6-3A.9 | ✓ | 3h |
| 3B.5: Wire sector pages into Obsidian wiki (verify links) | Dev | 3B.4 | - | 1h |
| 3B.6: Add sector links to INDEX.md | Writer | 3B.5 | - | 0.5h |

**Parallel groups:** 3B.3-3B.4 (2 automation), 3B.5-3B.6.

---

## PHASE 4: VISUAL LAYER & NAVIGATION (Parallel with Phase 3)

**Objective:** Color coding, reading guides, visual hierarchy.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 4.1: Design color scheme (domains, sectors, types, status) | Designer | Ontology files | ✓ | 1.5h |
| 4.2: Create NAVIGATION_GUIDE.md (how to read CB) | Writer | INDEX.md | ✓ | 2h |
| 4.3: Create QUICK_START.md (new user entry) | Writer | 4.2 | ✓ | 1h |
| 4.4: Create GLOSSARY.md (types, rels, abbreviations) | Writer | Ontology | ✓ | 2h |
| 4.5: Apply color tags to domain README files | Dev | 4.1 | ✓ | 1h |
| 4.6: Apply color tags to sector pages | Dev | 4.1 + 3B.5 | ✓ | 1h |
| 4.7: Create visual hierarchy diagram | Designer | All | - | 1.5h |

**Parallel groups:** 4.1-4.3-4.4 (2 writers, 1 designer), 4.5-4.6 (2 dev).

---

## PHASE 5: GRAPH INTEGRATION (Parallel with Phases 3-4)

**Objective:** Wire all entities and relationships into Neo4j knowledge graph.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 5.1: Design Neo4j schema (60 node types, 25 rels) | Architect | Ontology | - | 2h |
| 5.2: Create Neo4j node definitions (60 types) | DBA | 5.1 | ✓ | 1h |
| 5.3: Create Neo4j relationship definitions (25 types) | DBA | 5.1 | ✓ | 1h |
| 5.4: Ingest Sector nodes (36) | Data Eng | 5.2 + 3A.6 | ✓ | 1h |
| 5.5: Ingest Domain nodes (50) | Data Eng | 5.2 + domains | ✓ | 1h |
| 5.6: Ingest Venture nodes (500+) | Data Eng | 5.2 + 2.7 | ✓ | 2h |
| 5.7: Ingest Capability/Agent/Skill nodes | Data Eng | 5.2 | ✓ | 2h |
| 5.8: Wire Sector → Venture relationships (500+) | Data Eng | 5.4 + 5.6 + 2.7 | - | 1h |
| 5.9: Wire Domain → Sector relationships | Data Eng | 5.4 + 5.5 | - | 1h |
| 5.10: Ingest EVIDENCED_BY relationships (proofs) | Data Eng | 5.3 | ✓ | 2h |
| 5.11: Validate graph completeness (no orphans) | QA | 5.4-5.10 | - | 1h |

**Parallel groups:** 5.2-5.3 (2 DBA), 5.4-5.7, 5.10 (3 eng), 5.8-5.9, 5.11.

---

## PHASE 6: CLAUDE.MD UPDATES (Parallel with Phases 3-5)

**Objective:** Update CLAUDE.md with complete ontology + validation rules.

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 6.1: Add OBJECT_TYPES section | Writer | OBJECT_TYPES.yaml | ✓ | 1h |
| 6.2: Add RELATIONSHIPS section | Writer | RELATIONSHIPS.yaml | ✓ | 1h |
| 6.3: Add EVIDENCE_STANDARDS section | Writer | EVIDENCE_STANDARDS.md | ✓ | 1h |
| 6.4: Add STATUS_LIFECYCLE section | Writer | STATUS_LIFECYCLE.md | ✓ | 1h |
| 6.5: Add REGISTRY_HIERARCHY section | Writer | 3A.1 | ✓ | 1h |
| 6.6: Add SECTOR_TAXONOMY section (36 + gaps) | Writer | 2.7 | ✓ | 1.5h |
| 6.7: Add VALIDATION_RULES section | Architect | All above | - | 1h |
| 6.8: Add DISCOVERY_ORDER section (updated) | Writer | All above | - | 0.5h |

**Parallel groups:** 6.1-6.6 (1 writer, all parallel), 6.7-6.8.

---

## PHASE 7: REVENUE LOOP L1 (Parallel with Phase 6)

**Objective:** Implement first revenue loop at L1 (report-only).

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 7.1: Define Lead Discovery loop spec (LOP-000001) | PM | Framework | - | 2h |
| 7.2: Spec: inputs, outputs, decision points | PM | 7.1 | - | 1h |
| 7.3: Implement step 1: Scan prospects (read-only) | Dev | 7.2 | ✓ | 3h |
| 7.4: Implement step 2: Classify quality (scoring) | Dev | 7.2 | ✓ | 3h |
| 7.5: Implement step 3: Propose (report, no action) | Dev | 7.3 + 7.4 | - | 2h |
| 7.6: Implement metrics: accuracy tracking | Dev | 7.5 | ✓ | 2h |
| 7.7: Test L1 end-to-end (propose 10 leads, audit) | QA | 7.5 | - | 2h |
| 7.8: Document loop operation (runbook) | Writer | 7.7 | ✓ | 1h |
| 7.9: Extract lesson (accuracy tells us about model) | Analyst | 7.7 | ✓ | 1h |
| 7.10: Declare loop ACTIVE (SLA: ≥95% accuracy) | PM | 7.7-7.9 | - | 0.5h |

**Parallel groups:** 7.3-7.4, 7.6, 7.8-7.9. 7.5 blocks 7.6-7.7. 7.10 is gate.

---

## PHASE 8: LOOP GRADUATION L1 → L2 (After 7.10)

**Objective:** Graduate loop from L1 (report) to L2 (assisted execution).

| Task | Owner | Dependencies | Parallel | Est. Time |
|------|-------|--------------|----------|-----------|
| 8.1: Audit L1 results (manual review of 100 leads) | Analyst | 7.10 | - | 3h |
| 8.2: Calculate accuracy vs. 95% SLA | Analyst | 8.1 | - | 1h |
| 8.3: Decision: approve L2 or iterate | PM | 8.2 | - | 1h |
| 8.4: Design L2 assisted execution (approval gate) | PM | 8.3 | - | 1h |
| 8.5: Implement approval gate (human review) | Dev | 8.4 | ✓ | 2h |
| 8.6: Test L2 with real lead actions | QA | 8.5 | - | 2h |
| 8.7: Measure conversion on L2-generated leads | Analyst | 8.6 | - | 2h |
| 8.8: Decision: proceed to L3 or stabilize at L2 | PM | 8.7 | - | 1h |

---

## READY NOW (Parallel from day 1)

**Phase 2: VEX Crosswalk**
- Task 2.1-2.2: Audit + extract (2 data engineers) ✓
- Task 2.3-2.5: Classify + gaps (2 analysts) ✓
- Task 2.6-2.7: Validate + publish (sequential)

**Start after 2.7:**

**Phase 3A: Registries** (4-5 people, 2-3 days)
- 3A.2-3A.5: Create tables (4 DBAs in parallel)
- 3A.6-3A.9: Populate (2 data engineers, mostly seq)

**Phase 3B: Wiki** (2-3 people, 1-2 days)
- 3B.2-3B.4: Template + generate (automation)
- 3B.5-3B.6: Wire into wiki (1 developer)

**Phase 4: Visual** (3-4 people, 1 day, can start Day 2)
- 4.1-4.4: Design + docs (2 writers, 1 designer in parallel)
- 4.5-4.6: Apply tags (2 developers in parallel)

**Phase 5: Graph** (3-4 people, 2-3 days, can start Day 2)
- 5.2-5.3: Schema + node/rel defs (2 DBAs)
- 5.4-5.7, 5.10: Ingest nodes (3 engineers in parallel)
- 5.8-5.9: Wire relationships (1 engineer)

**Phase 6: CLAUDE.md** (1-2 people, 1 day, can start Day 3)
- 6.1-6.6: Sections (1 writer, all parallel)
- 6.7-6.8: Synthesis (1 architect)

**Phase 7: L1 Loop** (3-4 people, 2-3 days, start Day 4)
- 7.1-7.2: Spec (1 PM)
- 7.3-7.4: Implement steps (2 developers in parallel)
- 7.6, 7.8-7.9: Metrics + docs (2 people in parallel)
- 7.7: Test (1 QA)

**Phase 8: L2 Loop** (3-4 people, 2-3 days, start Day 7)

---

## CRITICAL PATH

```
Day 1: Phase 2 (VEX crosswalk) blocks everything
Day 2: Phase 2.7 complete → Phases 3A/3B/4/5 start in parallel
Day 3: Phase 3A complete → Phase 6 starts
Day 4: Phase 5 complete → Phase 7 (L1 loop) starts
Day 6-7: Phase 7 complete (L1 running) → Phase 8 (L2 loop) starts
Day 9-10: Phase 8 complete (L2 generating leads)
```

---

## SUCCESS CRITERIA

✓ **Phase 2:** All 500+ ventures mapped to sectors, 0 unassigned  
✓ **Phase 3A:** Registry authoritative, <0.1% drift vs. VEX  
✓ **Phase 3B:** All 36 sector wiki pages created & linked  
✓ **Phase 4:** New user can navigate CB in <5 min (QUICK_START works)  
✓ **Phase 5:** Neo4j graph queryable by sector/domain/venture/capability  
✓ **Phase 6:** CLAUDE.md fully updated with ontology  
✓ **Phase 7:** L1 loop running, ≥95% accuracy on manual audit of 100 leads  
✓ **Phase 8:** L2 loop in production, generating 10+ qualified leads/week  

---

## TEAM SIZE & DURATION

| Phase | People | Duration | Start | End |
|-------|--------|----------|-------|-----|
| 2 | 4 | 1-2 days | Day 1 | Day 2 |
| 3A | 7 | 2-3 days | Day 2 | Day 4 |
| 3B | 3 | 1-2 days | Day 2 | Day 3 |
| 4 | 4 | 1 day | Day 2 | Day 3 |
| 5 | 4 | 2-3 days | Day 2 | Day 5 |
| 6 | 2 | 1 day | Day 3 | Day 4 |
| 7 | 4 | 2-3 days | Day 4 | Day 7 |
| 8 | 4 | 2-3 days | Day 7 | Day 10 |

**Peak parallelism:** Day 2-3 (up to 15 people)  
**Total duration:** ~10 days with parallel execution

**Status:** Ready to execute | **Updated:** 2026-09-01
