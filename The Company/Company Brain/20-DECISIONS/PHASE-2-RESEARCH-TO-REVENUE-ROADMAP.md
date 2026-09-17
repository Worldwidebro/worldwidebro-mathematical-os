# Phase 2: Research-to-Revenue Engine Roadmap

**Document ID:** PHASE-2-ROADMAP-001  
**Updated:** 2026-09-17  
**Authority:** CP-001 (Strategic), CP-065 (Knowledge Logic)  
**Phase:** 2026-10-01 → 2027-03-31  
**Objective:** Build the complete Research-to-Revenue Engine connecting global research to Company Brain capabilities to business outcomes

---

## Executive Summary

Phase 1 (Sep 2026) built the **logic and knowledge infrastructure**:
- 72 logic layers with 72 control points
- Typed wikilinks and RDF/XML ontology
- Graph ingestion pipeline (markdown → Neo4j)
- Research Intelligence Base (20 sections)

Phase 2 (Oct 2026 - Mar 2027) builds the **operational engine**:
- Autonomous research discovery and verification
- Experiment sandbox for validation
- Adoption decision recorder
- Revenue attribution system
- Complete research-to-revenue loop

**Result:** Every academic paper, GitHub repo, technique, and benchmark becomes automatically discoverable, testable, and connected to ventures and revenue.

---

## Architecture Overview

```
EXTERNAL RESEARCH ECOSYSTEM
├─ arXiv (2M+ papers)
├─ OpenAlex (250M+ papers)
├─ Semantic Scholar (200M+ papers)
├─ Papers With Code (60K+ papers)
├─ GitHub (100M+ repos)
├─ Hugging Face (250K+ models)
└─ Standards, patents, industry blogs
    │
    ▼
RESEARCH INGESTION ENGINE
├─ Fetch (10+ sources)
├─ Normalize (deduplicate)
├─ Extract (claims, methods, code)
└─ Provenance (source, confidence)
    │
    ▼
KNOWLEDGE GRAPH
├─ Neo4j (entities, relationships)
├─ Postgres (authoritative state)
└─ Qdrant (semantic search)
    │
    ▼
RESEARCH AGENTS
├─ Discovery (find relevant papers)
├─ Verification (validate claims)
├─ Synthesis (connect multiple papers)
└─ Adoption (decide WATCH/PILOT/ADOPTED)
    │
    ▼
EXPERIMENT SANDBOX
├─ Reproduce findings
├─ Benchmark against baselines
├─ Measure cost/accuracy/speed
└─ Evaluate adoption viability
    │
    ▼
ADOPTION DECISION SYSTEM
├─ Record evidence
├─ Track confidence
├─ Manage conflicts
└─ Emit adoption event
    │
    ▼
CAPABILITY GRAPH
├─ New capabilities from research
├─ New agents and tools
├─ New workflows
└─ New repositories
    │
    ▼
VENTURE DEPLOYMENT
├─ Integrate into workflows
├─ Measure business impact
├─ Track cost and revenue
└─ Attribute to research
    │
    ▼
ECONOMIC OUTCOME
├─ Cost reduction
├─ Speed improvement
├─ Quality increase
└─ Revenue growth
    │
    ▼
COMPANY BRAIN LEARNS
├─ Record what worked
├─ Update adoption strategy
├─ Reinvest in research
└─ Continuous improvement
```

---

## Two Major Loops

### Knowledge Loop (Discovery → Learning)

```
RESEARCH (papers, code, benchmarks)
    ↓
INGEST (fetch + normalize)
    ↓
EXTRACT (claims, methods, evidence)
    ↓
VERIFY (replicate, validate locally)
    ↓
GRAPH (store relationships)
    ↓
RETRIEVE (query by agents)
    ↓
LEARN (update adoption strategy)
```

### Economic Loop (Research → Revenue)

```
RESEARCH (capability opportunity)
    ↓
CAPABILITY (technique/method/model)
    ↓
EXPERIMENT (test in sandbox)
    ↓
ADOPTION (WATCH → PILOT → ADOPTED)
    ↓
IMPLEMENTATION (code + workflow)
    ↓
WORKFLOW (integrated with agents)
    ↓
PRODUCT (customer-facing feature)
    ↓
CUSTOMER (transaction, revenue)
    ↓
MEASURE (cost/revenue/impact)
    ↓
REINVEST (repeat)
```

---

## 6 Major Systems

### 1. Graph Infrastructure

**Goal:** Queryable, versionable, conflict-aware knowledge graph

**Components:**
- Schema versioning (who changed what, when, why)
- Event log (every mutation is an event)
- Conflict resolution (support competing assertions)
- Query builder (safe API for agents)
- Provenance tracking (every fact has a source)

**Deliverables:**
- Graph versioning system
- Event log schema
- Conflict resolver
- Agent query API
- Provenance recorder

**Timeline:** Oct 1-31, 2026

---

### 2. Knowledge Publishing

**Goal:** Reliable markdown → XML → validation → Neo4j pipeline

**Components:**
- Frontmatter validator
- Named wikilink resolver
- Entity relationship extractor
- Schema validator
- Neo4j transaction engine
- Semantic embedder

**Deliverables:**
- Markdown validator
- XML/RDF generator
- Entity resolver
- Relationship validator
- Neo4j upserter
- Qdrant embedder

**Timeline:** Nov 1-30, 2026

---

### 3. Research Intelligence Engine

**Goal:** Autonomous discovery and ingestion from 20+ research sources

**Components:**
- arXiv API integration
- OpenAlex integration
- Semantic Scholar integration
- Papers With Code scraper
- GitHub code finder
- Hugging Face model fetcher
- Metadata normalizer
- Deduplicator

**Deliverables:**
- `research-ingestion` repository
- Source-specific scrapers
- Normalization engine
- Deduplication system
- XML/RDF output
- Provenance recorder

**Timeline:** Dec 1-31, 2026

---

### 4. Research Agent System

**Goal:** Specialized agents for discovery, verification, synthesis, adoption

**Components:**

**Discovery Agent**
- Search arXiv, OpenAlex, Semantic Scholar, GitHub, Papers With Code
- Filter by relevance to Company Brain domains
- Alert on high-confidence matches
- Track top authors and institutions

**Verification Agent**
- Extract claims from papers
- Find supporting evidence and experiments
- Check for code availability
- Identify limitations and contradictions
- Run reproducibility checks

**Synthesis Agent**
- Connect related papers
- Track research lineage (prior work → new work)
- Build capability chains
- Identify gaps in knowledge
- Propose integration points

**Adoption Agent**
- Assess technical compatibility
- Evaluate hardware/dependency requirements
- Check license compatibility
- Measure implementation complexity
- Decide WATCH/PILOT/ADOPTED

**Deliverables:**
- 4 specialized agents
- Agent task definitions
- Agent decision frameworks
- Agent query templates

**Timeline:** Jan 1-31, 2027

---

### 5. Experiment Sandbox

**Goal:** Safe testing environment for research before production deployment

**Components:**
- Experiment definition schema
- Sandbox environment setup
- Baseline measurement system
- Hypothesis validation
- Metrics collection
- Cost tracking
- Success criteria checker
- Result recorder

**Deliverables:**
- Experiment platform
- Sandbox configuration
- Baseline runner
- Metrics collector
- Cost accountant
- Result recorder

**Timeline:** Feb 1-28, 2027

---

### 6. Adoption Decision System

**Goal:** Formalize research adoption decisions with evidence tracking

**Components:**
- Decision schema (WATCH/PILOT/ADOPTED/REJECTED/SUPERSEDED)
- Evidence recorder
- Confidence scorer
- Decision owner tracking
- Review scheduler
- Conflict handler

**Deliverables:**
- Adoption decision schema
- Decision recorder
- Evidence tracker
- Conflict resolver
- Review scheduler

**Timeline:** Mar 1-15, 2027

---

## 12-Item Build Sequence

**No dependencies between items** → can build in parallel or any order

### Infrastructure Items (Oct-Nov)

1. **Graph Schema + Versioning** (Oct 1-15)
   - Version tracking
   - Event log
   - Conflict resolution model

2. **Publishing Pipeline** (Oct 16-31)
   - Markdown → XML/RDF
   - Entity/relationship extraction
   - Neo4j upserter

3. **Query Builder** (Nov 1-15)
   - Safe agent API
   - Query templates
   - Permission checking

### Research Items (Dec-Jan)

4. **Research Ingestion Engine** (Dec 1-20)
   - arXiv integration
   - OpenAlex integration
   - Metadata normalization

5. **Research Entity Extraction** (Dec 21-31)
   - Claim extraction
   - Method/model extraction
   - Evidence identification

6. **Discovery Agent** (Jan 1-15)
   - Multi-source search
   - Relevance filtering
   - Author/institution tracking

7. **Verification Agent** (Jan 16-31)
   - Claim validation
   - Code availability check
   - Reproducibility assessment

### Operational Items (Feb-Mar)

8. **Experiment Sandbox** (Feb 1-14)
   - Environment setup
   - Baseline measurement
   - Cost tracking

9. **Adoption Decision Recorder** (Feb 15-28)
   - Decision schema
   - Evidence tracking
   - Conflict resolution

10. **Synthesis Agent** (Mar 1-7)
    - Connect related papers
    - Build capability chains
    - Propose integrations

11. **Adoption Agent** (Mar 8-15)
    - Compatibility assessment
    - Cost/benefit analysis
    - Decision recommendation

12. **Revenue Attribution** (Mar 16-31)
    - Research-to-revenue chain
    - Impact measurement
    - ROI calculation

---

## Milestones & Checkpoints

### Oct 2026: Infrastructure Foundation
- [ ] Graph versioning system live
- [ ] Publishing pipeline functional
- [ ] Markdown files successfully ingesting to Neo4j

### Nov 2026: Knowledge Publishing
- [ ] 100+ research papers in graph
- [ ] Entity relationships validated
- [ ] Qdrant semantic indexing working

### Dec 2026: Research Discovery
- [ ] Daily arXiv ingestion live
- [ ] OpenAlex integration complete
- [ ] 1,000+ papers indexed

### Jan 2027: Agent Autonomy
- [ ] Discovery agent finding relevant papers
- [ ] Verification agent validating claims
- [ ] Adoption agent recommending decisions

### Feb 2027: Experimentation
- [ ] Experiment sandbox operational
- [ ] 5+ successful local reproductions
- [ ] Cost tracking accurate

### Mar 2027: Revenue Attribution
- [ ] 3+ research-enabled capabilities deployed
- [ ] Revenue attribution working
- [ ] Phase 2 complete

---

## Success Criteria

### Knowledge Loop
- [ ] Ingest 10K+ papers per month
- [ ] Extract 95%+ of claims/methods/code correctly
- [ ] Verify 80%+ of papers locally
- [ ] Query latency < 100ms
- [ ] Graph consistency 99.9%+

### Economic Loop
- [ ] Identify 5+ revenue-generating research opportunities
- [ ] Deploy 3+ research-enabled capabilities to production
- [ ] Measure $100K+ attributed revenue from research
- [ ] ROI on research investment > 5x

### Operational
- [ ] 100% of adoptions tracked and documented
- [ ] 0 unattributed research-to-revenue claims
- [ ] Zero conflicts in adoption records
- [ ] Agent decisions 90%+ accurate

---

## Connected to Phase 1

```
PHASE 1 (Complete)
├─ 72 Logic Layers (organized in 12 domains)
├─ 72 Control Planes (decision authorities)
├─ Typed Wikilinks (relationship semantics)
├─ RDF/XML Ontology (machine interchange)
├─ Graph Ingestion Pipeline (markdown → Neo4j)
├─ Research Intelligence Base (20 sections)
└─ Logic Architecture Framework (complete guide)
    │
    ▼
PHASE 2 (This Roadmap)
├─ Graph Infrastructure (versioning, events, conflicts)
├─ Knowledge Publishing (markdown → production)
├─ Research Intelligence Engine (20+ sources)
├─ Research Agent System (discovery → adoption)
├─ Experiment Sandbox (safe testing)
├─ Adoption Decision System (evidence tracking)
├─ Revenue Attribution (research → money)
└─ Continuous Improvement Loop (learn & reinvest)
    │
    ▼
RESULT
├─ Autonomous research discovery
├─ Autonomous experimentation
├─ Autonomous adoption decisions
├─ Measurable business impact
└─ Self-improving research-to-revenue engine
```

---

## Budget Estimate

| System | Engineering Effort | Research Effort | Total |
|--------|-------------------|-----------------|-------|
| Graph Infrastructure | 120h | 20h | 140h |
| Knowledge Publishing | 100h | 20h | 120h |
| Research Intelligence | 200h | 50h | 250h |
| Research Agents | 240h | 60h | 300h |
| Experiment Sandbox | 160h | 80h | 240h |
| Adoption System | 120h | 40h | 160h |
| **TOTAL** | **940h** | **270h** | **1,210h** |

**Timeline:** 6 months (Oct 2026 - Mar 2027)  
**Team:** 2-3 engineers + 1 researcher

---

## Critical Dependencies

### Must-Have Before Phase 2 Starts
- ✅ Phase 1 complete (logic layers, ontology, typed wikilinks)
- ✅ Neo4j running and queryable
- ✅ Postgres for authoritative state
- ✅ Qdrant for semantic search

### External Dependencies
- arXiv API (stable, free)
- OpenAlex API (stable, free)
- Semantic Scholar API (stable, free)
- GitHub API (rate limits, requires auth)
- Hugging Face API (stable, free)

### No Blockers Identified

All Phase 2 work is independent. No research is required. Architecture is clear. Implementation is straightforward engineering.

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| API rate limits | Implement caching, queuing, backoff strategy |
| Research source instability | Multiple sources, fallback mechanism |
| Experiment sandbox cost | Local-first, cloud overflow only |
| Large graph performance | Neo4j tuning, query optimization, caching |
| Adoption decision conflicts | Conflict resolution system, confidence scores |
| Revenue attribution complexity | Start simple (direct attribution), add complexity later |

---

## Post-Phase-2 (Phase 3 & Beyond)

Once Phase 2 is operational, Phase 3 becomes possible:

- **Cross-venture capability sharing** (capability proven in one venture → scale to others)
- **Research portfolio optimization** (which research areas generate most revenue?)
- **Predictive research scouting** (what research will matter in 6 months?)
- **Competitor intelligence** (who implemented what, when?)
- **Trend detection** (emerging topics → emerging opportunities)

---

## Master References

- **Phase 1 Complete:** [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md]]
- **Logic Layers:** [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]]
- **Typed Wikilinks:** [[_DOCS/TYPED-WIKILINKS-GUIDE.md]]
- **Graph Ingestion:** [[_PIPELINES/GRAPH-INGESTION-PIPELINE.md]]
- **Research Intelligence:** [[42-RESEARCH-INTELLIGENCE/README.md]]
- **Research Ontology:** [[_ONTOLOGY/RESEARCH-INTELLIGENCE-LAYER.xml]]
- **Research Sources:** [[_REGISTRIES/CANONICAL/RESEARCH-SOURCE-REGISTRY.yaml]]

---

## One Sentence

**By Mar 2027, Company Brain transforms global research into autonomous experiments, validated capabilities, and measurable revenue impact.**

