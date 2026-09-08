---
id: CTRL-INST-001
title: Company Brain — Installation Phases
aliases: ["INSTALLATION_PHASES", "Company Brain Installation Phases", "Rollout Phases"]
tags: ["installation", "phases", "rollout", "neo4j", "qdrant", "capabilities", "automation"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[50-MASTER-CONTROL/DEPLOYMENT_CHECKLIST|DEPLOYMENT_CHECKLIST]] | [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX]] | [[REALITY]]

# Company Brain — Installation Phases
**Framework for deploying the reconciled system**

---

## PHASE 1: DISCOVERY (✅ COMPLETE — CB-RECON-2026-09-01)

**What we discovered:**
- 789 ventures ([[SECTOR_INDEX|SEC-001 through SEC-035]])
- 893 repositories (`CB-REPO-000001` to `CB-REPO-000893`, see [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml|REPOSITORY_REGISTRY]])
- 903 starred dependencies (31M+ stars, 10 capability layers, see [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE]])
- 22 Vercel deployments
- Neo4j graph schema ready ([[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]])

**Outputs:** `[[_REGISTRIES/RECONCILIATION_2026_09_01/]]`
- `CANONICAL_REGISTRY_DRAFT.json`
- `UNIFIED_VENTURE_REGISTRY.json`
- `GITHUB_INVENTORY_MASTER.json`
- `STARRED_REPOS_DEPENDENCY_ANALYSIS.json`
- `COMPANY_BRAIN_NEO4J_IMPORT.cypher`

**Status:** Ready for Phase 2

---

## PHASE 2: FOUNDATION (NEXT)

**Build the knowledge graph foundation.**

**Step 2.1: Load [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|Neo4j]]**
```bash
cat _REGISTRIES/RECONCILIATION_2026_09_01/COMPANY_BRAIN_NEO4J_IMPORT.cypher \
  | cypher-shell -u neo4j -p <password>
```
**Success:** COMPANY node + 789 VENTURE nodes + 893 REPOSITORY nodes queryable

**Step 2.2: Index [[10-MEMORY/10-MEMORY|Qdrant]] (semantic search)**
- Embed 893 README files → vectors
- Embed 789 venture descriptions → vectors
- Embed 903 starred repo descriptions → vectors

**Step 2.3: Wire [[09-KNOWLEDGE/Awesome-Lists|Awesome Lists]]**
- Index sindresorhus/awesome (58K★) as solution search layer
- Create CAP-* → awesome-list links for every capability
- Build "find similar tools" query engine

**Deliverables:**
- [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|Neo4j]] queries returning results
- [[10-MEMORY/10-MEMORY|Qdrant]] vectors indexed (300K+)
- [[09-KNOWLEDGE/Awesome-Lists|Awesome lists]] searchable via Company Brain

---

## PHASE 3: CAPABILITY MAPPING (FOLLOW-UP)

**Map every starred repo to a capability.**

**Step 3.1: Create CAP-* → STARRED-REPO links**
- 300 capabilities × dependencies = capability matrix ([[14-CAPABILITIES/CAPABILITIES_INDEX|Capabilities Index]])
- Identify gaps (missing tools for each capability)
- Flag single points of failure

**Step 3.2: Build solution search**
- Query: "How do I X?" → Check [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|Neo4j]] for existing solutions
- Fallback: "Not found → search awesome lists"
- Result: Tool recommendation + integration guide

**Step 3.3: Venture gap analysis**
- 678 ventures without repos
- Use awesome lists to find candidate tools
- Suggest "build vs. buy" decisions

**Deliverables:**
- [[14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json|CAPABILITY_SOLUTION_MATRIX.json]] (CAP-* → tools)
- `VENTURE_GAP_ANALYSIS.json` (678 unimplemented ventures)
- `AWESOME_LISTS_INDEX.json` (searchable awesome ecosystem)

---

## PHASE 4: AUTOMATION (ONGOING)

**Make Company Brain self-healing.**

**Step 4.1: Dependency monitoring**
- Alert when starred repos have breaking changes
- Auto-flag single points of failure (claude-code, graphify, LangGraph)
- Suggest alternatives from awesome lists

**Step 4.2: Venture-to-repo linkage**
- Auto-discover repos matching venture names
- Suggest repo assignments to orphaned ventures
- Flag duplicates

**Step 4.3: Gap filling**
- Monthly scan: "What's missing from our stack?"
- Query awesome lists: "What's trending in AI/ops/frontends?"
- Recommend new starred repos to watch

**Deliverables:**
- Scheduled crawlers (Temporal workflows)
- Dependency alert system
- Auto-gap detector

---

## FILE ORGANIZATION (WHERE THINGS LIVE)

```
Company Brain/
├── 50-MASTER-CONTROL/
│   ├── INSTALLATION_PHASES.md (THIS FILE)
│   ├── EXECUTION_STACK.md
│   └── LOOP_ENGINEERING.md
│
├── _REGISTRIES/
│   ├── RECONCILIATION_2026_09_01/ (CANONICAL DATA)
│   │   ├── CANONICAL_REGISTRY_DRAFT.json ........... 893 repos (CB-REPO-*)
│   │   ├── UNIFIED_VENTURE_REGISTRY.json ......... 789 ventures (SEC-NNN)
│   │   ├── GITHUB_INVENTORY_MASTER.json ........ Complete GitHub state
│   │   ├── STARRED_REPOS_DEPENDENCY_ANALYSIS.json  903 dependencies
│   │   ├── AWESOME_LISTS_INDEX.json (phase 3) ... Awesome ecosystem
│   │   ├── CAPABILITY_SOLUTION_MATRIX.json (phase 3) CAP-* → tools
│   │   ├── VENTURE_GAP_ANALYSIS.json (phase 3) .. Unimplemented ventures
│   │   ├── COMPANY_BRAIN_NEO4J_IMPORT.cypher .... Ready to load
│   │   ├── COMPANY_BRAIN_AUDIT_REPORT.md ....... Discovery report
│   │   ├── CAPABILITY_DEPENDENCY_MAP.md ........ How tools power CB
│   │   └── DELIVERY_SUMMARY.md ................. Integration overview
│   │
│   ├── REPOSITORY_REGISTRY.yaml ................ All repos (permanent)
│   ├── VENTURE_REGISTRY.yaml .................. All ventures (permanent)
│   └── ID_REGISTRY.yaml ....................... ID mappings (permanent)
│
├── 14-CAPABILITIES/
│   ├── _registry/
│   │   └── capabilities.json ................. CAP-001 to CAP-300
│   └── solutions/ (phase 3)
│       ├── CAP-001-multi-model-orchestration.md
│       ├── CAP-150-code-intelligence.md
│       └── ...
│
├── 57-CODE-INTELLIGENCE/
│   └── GRAFT_INTEGRATION.md ................... Graphify + code graphs
│
├── 20-LOOPS/
│   └── LOOP_ENGINEERING.md .................... Revenue loops (L1/L2/L3)
│
└── INDEX.md .................................. Master hub (updated with reconciliation links)
```

---

## HOW COMPANY BRAIN SEARCHES AWESOME LISTS TO SOLVE GAPS

### Query Pattern 1: "Find tools for capability X"

```cypher
MATCH (cap:CAPABILITY {id: "CAP-150"})
MATCH (cap)-[:POWERED_BY]->(starred:STARRED_REPO)
RETURN starred.name, starred.description, starred.stars
ORDER BY starred.stars DESC;
```

**Fallback if not found:**
```
Query awesome lists: "code intelligence" OR "AST" OR "dependency analysis"
→ Recommend: new tools to star or build
```

### Query Pattern 2: "What tools exist for venture sector X?"

```cypher
MATCH (v:VENTURE {sector: "SEC-008"})
MATCH (v)-[:NEEDS]->(cap:CAPABILITY)
MATCH (cap)-[:POWERED_BY]->(starred:STARRED_REPO)
RETURN DISTINCT starred.name, cap.id
ORDER BY starred.stars DESC;
```

### Query Pattern 3: "What's missing in our stack?"

```cypher
MATCH (cap:CAPABILITY)
WHERE NOT (cap)-[:POWERED_BY]->()
RETURN cap.id, cap.name, cap.description;
```

**Action:** Search awesome lists for matches

### Query Pattern 4: "What can solve this problem?"

```
User: "We need to process documents at scale"
↓
Query Neo4j: MATCH ()-[:SOLVES]->(requirement) WHERE requirement = "document processing"
↓
If no match:
  1. Parse requirement → search awesome lists
  2. Return: "We don't have this. Awesome suggests: X, Y, Z"
  3. Recommend: star repo, integrate, or build
```

---

## AWESOME LISTS AS CAPABILITY DISCOVERY

**Master link:** https://github.com/sindresorhus/awesome (58K★)

Company Brain uses awesome as a **capability discovery layer:**

| Awesome Category | Company Brain Layer | Query |
|------------------|-------------------|-------|
| awesome-ai | CAP-001 to CAP-100 (AI/Agent core) | "Which AI tools aren't we watching?" |
| awesome-react | CAP-300 to CAP-305 (Frontend) | "React ecosystem gaps?" |
| awesome-kubernetes | CAP-500 to CAP-503 (Infrastructure) | "K8s tools missing?" |
| awesome-python | Language layer | "Python tools for ventures?" |
| awesome-databases | CAP-400 to CAP-405 (Knowledge graphs) | "DB alternatives?" |
| awesome-node | Backend frameworks | "Node.js tools?" |
| awesome-cli | CAP-600 (CLI tools) | "CLI gaps?" |

**Process:**
1. Quarterly: Crawl awesome-* repos
2. Extract tools + descriptions
3. Cross-reference with starred repos
4. Identify gaps (trending tools not in our stack)
5. Recommend additions or alternatives

---

## SUCCESS METRICS

| Phase | Metric | Target |
|-------|--------|--------|
| Phase 1 (Discovery) | All ventures + repos catalogued | ✅ 789 + 893 |
| Phase 2 (Foundation) | Neo4j queries returning results | ✅ Ready to load |
| Phase 3 (Mapping) | CAP-* → tool links complete | 300/300 |
| Phase 4 (Automation) | Dependency alerts working | Daily |
| Awesome integration | Gaps automatically detected | Weekly |

---

## NEXT IMMEDIATE ACTIONS

1. **Phase 2 start:** Load Neo4j (next session)
2. **Index Qdrant:** Embed all descriptions
3. **Wire awesome lists:** Make them searchable
4. **Create solution search:** "How do I solve X?"

---

**This is Company Brain's installation roadmap. All files are permanent, tracked in Git, and integrated into the knowledge graph.**

---

## Connected Navigation
- Master Control Gateway: [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- Deployment Checklist: [[50-MASTER-CONTROL/DEPLOYMENT_CHECKLIST|DEPLOYMENT_CHECKLIST]]
- Execution Stack: [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]]
- Capabilities Index: [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX]]
- Canonical Registries: [[_REGISTRIES/README|Registries Hub]]
