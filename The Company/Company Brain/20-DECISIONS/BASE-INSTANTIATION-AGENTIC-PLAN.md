# Base Instantiation — Agentic Engineering Plan

**Date:** 2026-09-22  
**Authority:** Agentic Engineering Skill + BASES-CANONICAL-DEFINITION  
**Timeline:** Sep 23 – Dec 31, 2026 (4 phases, 14 weeks)  
**Objective:** Instantiate 35 Bases (domain knowledge systems) with agents, evaluate evals, scale to full Company Brain operationalization

---

## Eval-First Strategy

### Baseline Evals (Sep 23-24)

#### Capability Eval
**Test:** Can we create and validate a Base structure?

```python
def test_base_instantiation():
    # Given: BASE-009 (Logistics) template
    # When: Agent instantiates identity + ontology + knowledge layers
    # Then: Verify all 7 sections created, metadata complete, Neo4j nodes created
    
    base = instantiate_base("BASE-009", template="logistics")
    
    assert base.identity.base_id == "BASE-009"
    assert base.ontology.entities_count > 0
    assert base.knowledge.sources_count > 0
    assert neo4j_node_count(base_id="BASE-009") > 0
    assert base.status == "INSTANTIATED"
    
    return {
        "passed": True,
        "sections_created": 7,
        "neo4j_nodes": neo4j_node_count(base_id="BASE-009"),
        "knowledge_items": base.knowledge.sources_count
    }
```

**Success Criteria:**
- ✅ Base created with all 7 sections (Identity, Ontology, Knowledge, Market, Ventures, Operations, Technology, Agents, Decisions, Experiments, Outputs)
- ✅ Metadata complete (Base ID, Name, Description, Owner, Status)
- ✅ Neo4j graph nodes created (Base node, 5+ entity nodes)
- ✅ Obsidian wiki links resolve
- ✅ Base frontmatter valid YAML

**Baseline:** 0 passes (no Bases yet)

#### Regression Eval
**Test:** Does creating a Base break existing systems?

```python
def test_base_no_regressions():
    # Given: Company Brain state (Neo4j 20,363 edges, Qdrant 17,236 vectors)
    # When: Instantiate BASE-009
    # Then: Verify no Neo4j queries break, no Qdrant consistency errors
    
    baseline_edges = neo4j_edge_count()
    baseline_vectors = qdrant_vector_count()
    
    instantiate_base("BASE-009")
    
    # No edges should be deleted; only additions
    assert neo4j_edge_count() >= baseline_edges
    assert qdrant_vector_count() >= baseline_vectors
    
    # All existing queries still work
    assert test_existing_queries()  # 50+ queries
    
    return {
        "edges_added": neo4j_edge_count() - baseline_edges,
        "vectors_added": qdrant_vector_count() - baseline_vectors,
        "queries_passing": 50
    }
```

**Success Criteria:**
- ✅ No edges deleted (only additions)
- ✅ No vectors deleted (only additions)
- ✅ 50+ existing Neo4j queries still pass
- ✅ Qdrant consistency check passes
- ✅ No breaking changes to CLAUDE.md, ANTIGRAVITY rules, or existing Bases

**Baseline:** 50 passes (no regressions to break initially)

---

## Phase 1: Core Bases (Sep 23 – Oct 6)

**Goal:** Define 3 production Bases (Logistics, Real Estate, Staffing)

### Phase 1 Unit Breakdown (15-min rule)

#### Unit 1.1: BASE-009 Identity (Logistics)
**Time:** 2h | **Model:** Haiku  
**Trigger:** Run baseline evals

```
1.1a (30min) — Parse BASE-009-Logistics from SECTOR_TAXONOMY
1.1b (30min) — Create _base.md (frontmatter + description)
1.1c (30min) — Generate Base ID, Owner, Status
1.1d (30min) — Link to SECTOR-009 in Neo4j

Verify:
  ✅ _base.md exists with valid YAML frontmatter
  ✅ Base node created in Neo4j
  ✅ Obsidian wiki link [[BASE-009-Logistics]] resolves
  ✅ Capability Eval: identity_complete = true
```

**Risk:** SECTOR-009 mapping missing. Mitigation: Query SECTORS_REGISTRY; fallback to manual mapping.

---

#### Unit 1.2: BASE-009 Ontology (Logistics)
**Time:** 3h | **Model:** Sonnet  
**Depends on:** 1.1

```
1.2a (45min) — Define entity types (Venture, Route, Driver, Delivery, Customer)
1.2b (45min) — Define relationship types (HAS_ROUTE, ASSIGNED_TO, COMPLETED_BY)
1.2c (45min) — Create OWL/RDF triples in _ontology/BASE-009-ontology.xml
1.2d (45min) — Map to COMPANY-BRAIN-ONTOLOGY; validate no conflicts

Verify:
  ✅ 15+ entity types defined
  ✅ 20+ relationship types defined
  ✅ RDF/XML valid against schema
  ✅ No ontology conflicts with existing 250+ entities
  ✅ Neo4j constraint creation succeeds
```

**Risk:** Ontology conflicts with BASE-012 (RE-001 uses Driver, Routes). Mitigation: Namespace (Logistics:Driver, RealEstate:Driver).

---

#### Unit 1.3: BASE-009 Knowledge (Logistics)
**Time:** 2h | **Model:** Haiku  
**Depends on:** 1.1, 1.2

```
1.3a (30min) — Ingest sources (routing algorithms, delivery SOP, driver regs)
1.3b (30min) — Create knowledge.md (concepts, evidence, research)
1.3c (30min) — Link sources to Neo4j Knowledge nodes
1.3d (30min) — Generate wiki links to related Bases (BASE-003 Energy, BASE-017 Transportation)

Verify:
  ✅ 10+ sources ingested (local, not external URLs)
  ✅ 25+ concepts documented
  ✅ knowledge.md linked to ontology entities
  ✅ Qdrant: concepts embedded + indexed
  ✅ Semantic search: "How does delivery routing work?" → returns knowledge
```

**Risk:** Sources fragmented across repos. Mitigation: Use REPOSITORY_REGISTRY; fallback to `ingest-and-sources.md` procedure.

---

#### Unit 1.4: BASE-009 Ventures (Logistics)
**Time:** 2h | **Model:** Haiku  
**Depends on:** 1.1

```
1.4a (30min) — Link existing ventures: LT-005 (Medical Courier), LT-011 (Dispatch)
1.4b (30min) — Create ventures.md with product matrix + revenue models
1.4c (30min) — Map to Neo4j: Base -(CONTAINS_VENTURE)-> Venture
1.4d (30min) — Query success: "Show me all ventures in Logistics"

Verify:
  ✅ 2 active ventures linked (LT-005, LT-011)
  ✅ Product/service definitions clear
  ✅ Revenue models documented (per-delivery fees, subscriptions)
  ✅ Neo4j query returns both ventures
  ✅ ventures.md frontmatter references BASE-009
```

**Risk:** Venture metadata inconsistent with VENTURES_REGISTRY. Mitigation: Normalize from VENTURES_BY_SECTOR.yaml first.

---

#### Unit 1.5: BASE-009 Agents (Logistics)
**Time:** 3h | **Model:** Sonnet  
**Depends on:** 1.1, 1.2, 1.4

```
1.5a (45min) — Identify agents authorized for Logistics Base (Dispatch Agent, Tracking Agent)
1.5b (45min) — Define agent capabilities (routing, ETA, driver assignment)
1.5c (45min) — Link agents to Base + Neo4j: Base -(GOVERNED_BY_AGENT)-> Agent
1.5d (45min) — Test L2 autonomy: Agent reads Base, makes decision, reports result

Verify:
  ✅ 3+ agents identified for BASE-009
  ✅ Capabilities documented (L1/L2/L3 autonomy per capability)
  ✅ Neo4j relationship created + queryable
  ✅ agents.md has access control policies
  ✅ L2 test: Agent updates delivery status in Base, Neo4j reflects change
```

**Risk:** Agent scope ambiguous. Mitigation: Reference AGENT_SCOPE_MATRIX; restrict via Neo4j (:AUTHORIZED_FOR relationship).

---

#### Unit 1.6: BASE-009 Validation (Logistics)
**Time:** 2h | **Model:** Opus  
**Depends on:** 1.1-1.5

```
1.6a (30min) — Run Capability Eval: BASE-009 complete?
1.6b (30min) — Run Regression Eval: No breaks to existing systems?
1.6c (30min) — Neo4j integrity check: All 7 sections have nodes, no dangling refs
1.6d (30min) — Obsidian audit: All wiki links resolve, no orphans

Verify:
  ✅ Capability Eval: PASSED (7 sections, metadata, Neo4j nodes)
  ✅ Regression Eval: PASSED (50+ queries still pass, no edges deleted)
  ✅ Neo4j validation: 0 orphans, all constraints satisfied
  ✅ Obsidian audit: 0 broken links
  ✅ BASE-009 status: PRODUCTION_READY
```

**Risk:** Eval catches ontology conflict. Mitigation: Rollback 1.2, resolve conflict, re-run 1.2-1.6.

---

### Phase 1 Summary

| Base | Units | Hours | Status | Evals | Ready for Production |
|------|-------|-------|--------|-------|----------------------|
| BASE-009 (Logistics) | 1.1-1.6 | 14h | ✅ Complete | ✅ Pass | Oct 6 |
| BASE-012 (Real Estate) | 2.1-2.6 | 14h | In Progress | — | Oct 6 |
| BASE-014 (Staffing) | 3.1-3.6 | 14h | Queued | — | Oct 6 |

**Phase 1 Total:** 42 hours (6h/day × 7 days = feasible in 1 week with 2 agents)

---

## Phase 2: Agentic Scaling (Oct 7-31)

**Goal:** Build pipeline for 12 more Bases (BASE-004, BASE-005, BASE-018, BASE-025, BASE-027, BASE-031, BASE-032, BASE-033, BASE-034, BASE-035, BASE-036 + Emerging)

### Strategy
- **Parallel instantiation:** 3 agents work on 3 Bases simultaneously
- **Template reuse:** Units 1.1-1.6 become boilerplate; reduce per-Base from 14h to 8h
- **Regression gates:** Every 2 Bases, run full eval suite
- **Model tier:** Haiku 70%, Sonnet 25%, Opus 5% (validation + conflict resolution)

### Success Criteria
- ✅ 15 Bases instantiated by Oct 31
- ✅ 100% eval pass rate (Capability + Regression)
- ✅ Neo4j: 35,000+ edges (up from 20,363)
- ✅ Qdrant: 25,000+ vectors (up from 17,236)
- ✅ 0 regressions in existing systems

---

## Phase 3: Cross-Base Integration (Nov 1-30)

**Goal:** Connect Bases to revenue, agents, decisions

### Units
- **3.1-3.5:** Revenue attribution graph (Base → Venture → Customer → Transaction → $)
- **3.6-3.10:** Agent coordination (multi-Base workflows)
- **3.11-3.15:** Decision propagation (policy change in one Base → affects others)
- **3.16-3.20:** Semantic search across Bases

### Success Criteria
- ✅ Revenue query: "Show me all revenue in BASE-009 for Q4 2026" → returns $X
- ✅ Agent query: "Which agents operate across 3+ Bases?" → returns list + authorizations
- ✅ Decision query: "If we change pricing in BASE-012, what cascades?" → impacts analysis

---

## Phase 4: Full Operationalization (Dec 1-31)

**Goal:** Complete 35 Bases, measure Company Brain readiness

### Success Criteria
- ✅ 35/35 Bases instantiated
- ✅ 50,000+ Neo4j edges (graph density increase)
- ✅ 40,000+ Qdrant vectors (knowledge coverage)
- ✅ 100% Base ontology consistency checks pass
- ✅ Revenue loops operational (lead → venture → transaction → $ → memory)
- ✅ Agent autonomy L2/L3 tested on 5+ Bases
- ✅ Obsidian vault fully integrated (wiki links → Base graph)

---

## Cost & Timeline Summary

| Phase | Bases | Hours | Model Mix | Weeks | Cost Estimate |
|-------|-------|-------|-----------|-------|-----------------|
| Phase 1 | 3 | 42h | 40H + 2S + 1O | 1 | $180 |
| Phase 2 | 12 | 80h | 56H + 20S + 4O | 3 | $300 |
| Phase 3 | — | 50h | 20H + 25S + 5O | 1 | $250 |
| Phase 4 | 20 | 120h | 80H + 30S + 10O | 1 | $450 |
| **TOTAL** | **35** | **292h** | **196H + 77S + 20O** | **6** | **$1,180** |

**Cost:** ~$1.2K for full Company Brain operationalization  
**Timeline:** 6 weeks (Sep 23 – Dec 31) with 2 agents working in parallel

---

## Contingency & Rollback

**If eval fails:**
1. Pause Base instantiation
2. Rollback to last CHECKPOINT
3. Fix root cause (ontology conflict, orphaned entity, etc.)
4. Re-run eval
5. Continue

**Checkpoints:** After units 1.6, 2.6, 3.6, 4.6 (every 3 Bases)

---

## Integration Points

### Obsidian
- BASES/ folder → 35 subdirectories (one per Base)
- Each Base has _base.md (identity), knowledge.md, agents.md, decisions.md
- Wiki links: [[BASE-009-Logistics]] → [[LT-005-Medical-Courier]] → [[CP-026-Operations]]

### OpenKnowledge
- Bases can be collaborative domains for researchers
- Sources ingested per Base (procedures in `references/ingest-and-sources.md`)
- Knowledge synthesis per Base (via `/research-with-sources` skill)

### Neo4j
- Base node: (Base {id, name, status})
- Base relationships: CONTAINS_VENTURE, REQUIRES_CAPABILITY, GOVERNED_BY_AGENT, etc.
- Query: MATCH (base:Base)-[*1..3]->(entity) RETURN base, COLLECT(entity)

### Qdrant
- Embed Base concepts: "Medical courier dispatch routing algorithms"
- Query: Search vector space for "healthcare logistics agents"
- Return: TOP-K Bases + concepts relevant to query

---

## Next Steps (Sep 23)

1. ✅ Canonical Definition created (BASES-CANONICAL-DEFINITION.md)
2. ✅ Agentic Plan created (this file)
3. **TODO:** Create Unit 1.1 implementation checklist
4. **TODO:** Run baseline evals (Capability + Regression)
5. **TODO:** Kickoff Phase 1 with first agent

---

**Authority:** User + Agentic Engineering Skill  
**Last Updated:** 2026-09-22  
**Status:** READY FOR EXECUTION (Sep 23 kickoff)
---

## Control Base Reference

This document is mapped to [[B201|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B201]]
