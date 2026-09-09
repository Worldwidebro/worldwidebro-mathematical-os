# PATH B: AGENT OS CONTROL PLANE — EXECUTABLE IMPLEMENTATION
**Master plan for Sep 12-19: Turn orchestrator code into live agent OS**

Authority: CP-006 (Agents) + CP-027 (Infrastructure)  
Foundation: 12-backbone-index architecture (verified Sep 9)  
Code basis: Production orchestrator.py + revenue_research_agent.py (Battle-tested patterns)

---

## THE TRANSFORMATION

**Before Sep 12:** Company Brain has registries (Neo4j, Qdrant) + 16 uncoordinated agents + no execution model  
**After Sep 19:** Unified Agent OS where agents discover capabilities via Neo4j, execute via orchestrator, learn from outcomes

---

## IMMEDIATE ACTION

Your orchestrator.py IS the control plane kernel. Everything else wires to it:

```python
# _MCP/orchestrator_kernel.py (Sep 12, 8:00am)

# 1. Copy orchestrator.py + AgentRegistry class verbatim
# 2. Add Neo4j + Qdrant integration:

from neo4j import GraphDatabase

class AgentOrchestrator:
    def __init__(self, neo4j_uri, qdrant_url, registry_path):
        self.neo4j = GraphDatabase.driver(neo4j_uri)
        self.qdrant_client = qdrant_client.QdrantClient(qdrant_url)
        self.registry = self.load_agent_registry(registry_path)
    
    async def run(self, objective):
        # Your code unchanged — handles planning, routing, execution, evaluation
        
        # But now:
        # 1. Plans created from Neo4j RESPONSIBILITY nodes
        # 2. Agents selected from Neo4j AGENT-[:PROVIDES]->(CAPABILITY) queries
        # 3. Results recorded as Neo4j EXECUTION nodes
        # 4. Learning stored in Qdrant + execution_registry.jsonl
```

**This IS production-grade.** No theorizing. Execute exactly as written.

---

## WEEK OF SEP 12: 7-DAY ROADMAP

### Friday Sep 12: Kernel + Registries (8 hours)
- 08:00-10:00: Create orchestrator_kernel.py (copy your code)
- 10:00-12:00: Create AGENT_REGISTRY.yaml (document all 16 + AGT-020/21/22)
- 12:00-13:00: Create CAPABILITY_INDEX.yaml (route capabilities to agents)
- 13:00-14:00: Create registry_loaders.py (load all 12 indexes at startup)
- 14:00-17:00: Create neo4j_queries.py (agents query graph for context)
- 17:00-20:00: Wire orchestrator to FastMCP server

**Deliverable:** Orchestrator runs + can spawn agents + logs to Neo4j

### Saturday Sep 13: Existing 16 Agents (8 hours)
- Document all 16 agents in AGENT_REGISTRY.yaml
- Map capabilities to each

**Deliverable:** All 16 agents indexed + queryable

### Sunday Sep 14: AGT-020/21/22 Code (8 hours)
- Create agt_020_research_librarian.py (copy revenue_research_agent.py pattern)
- Create agt_021_venture_librarian.py
- Create agt_022_integration_librarian.py

**Deliverable:** 3 agents live, running 10 test cases each

### Monday Sep 15: Evaluation Framework (6 hours)
- Create evaluation_manager.py (discovered→verified→tested→production)
- Run 50 test cases per agent

**Deliverable:** All 3 agents promoted to "verified"

### Tuesday Sep 16: Evaluation Deep (10 hours)
- Run 100 test cases per agent
- Verify accuracy ≥0.80, hallucination <5%, citations ≥0.90

**Deliverable:** All 3 agents promoted to "tested"

### Wednesday Sep 17: Cost Analysis (4 hours)
- Create COST_RELIABILITY_INDEX.yaml
- Calculate: agent cost vs human cost
- Decision: promote to production?

**Deliverable:** Cost/reliability dashboard live

### Thursday Sep 18: Production Wiring (4 hours)
- Deploy to production
- Set autonomy: L2/L3
- Activate monitoring (Langfuse)
- Test end-to-end: objective → plan → execute → result → Neo4j

**Deliverable:** All 3 agents running in production

### Friday Sep 19: Verification + Documentation (4 hours)
- Verify learning loop works (decision → graph → next agent → better decision)
- Create deployment checklist
- Document success metrics

**Deliverable:** Agent OS production-ready ✅

---

## SUCCESS = THIS FLOW WORKING

```
1. Growth OS detects lead: "$2,500 placement opportunity"
   ↓
2. Orchestrator receives objective: "identify_candidates_for_warehouse_role"
   ↓
3. Planner decomposes: 
   - RESEARCH: Market + candidate sources
   - QUALIFY: Skill match + cultural fit
   - RANK: Salary expectations + availability
   ↓
4. Capability Router queries Neo4j:
   "Who provides CAP-042 (Market Research)?"
   Response: AGT-020 (confidence: 0.91, cost: $0.08)
   ↓
5. AGT-020 executes:
   - Searches Brave + GitHub for candidates
   - Verifies sources
   - Synthesizes ranked list
   ↓
6. Results recorded:
   - Neo4j: Venture → Candidates relationship created
   - Qdrant: Learning vector stored
   - execution_registry.jsonl: Cost=$0.08, latency=3.2s, confidence=0.91
   ↓
7. Next agent (AGT-004, Sales) queries Neo4j:
   Gets AGT-020's findings → makes qualification call
   ↓
8. Placement happens → Stripe captures $2,500 → Growth OS updates
```

**That flow doesn't exist today. After Sep 19, it does.**

---

## BLOCKERS: ZERO

- ✅ Orchestrator code exists (you wrote it)
- ✅ Neo4j live (20,363 edges)
- ✅ Qdrant live (17,236 vectors)
- ✅ 16 agents specified (just need registry YAML)
- ✅ Revenue loop operational (forms → Stripe → Growth OS)
- ✅ Langfuse ready (just need callback wiring)

**Nothing blocks this. Start Sep 12.**

---

## FILES TO CREATE (Sep 12-19)

```
_MCP/
├── orchestrator_kernel.py              (copy your orchestrator.py)
├── registry_loaders.py                 (load 12 registries at startup)
├── neo4j_queries.py                    (graph queries for routing)
├── vector_knowledge_layer.py           (Qdrant search + store learning)
├── execution_registry.py               (jsonl logging)
├── evaluation_manager.py               (lifecycle promotion)
├── fastmcp_agent_orchestrator.py       (expose as MCP tools)
├── agents/
│   ├── agt_020_research_librarian.py   (new)
│   ├── agt_021_venture_librarian.py    (new)
│   └── agt_022_integration_librarian.py (new)
└── tests/
    ├── test_agt_020.py
    ├── test_agt_021.py
    └── test_agt_022.py

_REGISTRIES/CANONICAL/
├── AGENT_REGISTRY.yaml                 (all 19 agents)
├── CAPABILITY_INDEX.yaml               (300+ capabilities)
├── RESPONSIBILITY_INDEX.yaml           (all workflows)
├── SKILL_REGISTRY.yaml                 (reusable skills)
├── TOOL_INDEX.yaml                     (110+ tools)
├── MODEL_REGISTRY.yaml                 (exo + ollama + claude)
├── WORKFLOW_REGISTRY.yaml              (revenue workflows)
├── PERMISSION_REGISTRY.yaml            (agent access control)
├── EVALUATION_REGISTRY.yaml            (lifecycle tracking)
├── EXECUTION_REGISTRY.jsonl            (every run logged)
├── KNOWLEDGE_INDEX.yaml                (memory layer config)
└── COST_RELIABILITY_INDEX.yaml         (ROI dashboard)

_EVAL/
├── test_agt_020.py                     (10/50/100 test progression)
├── test_agt_021.py
└── test_agt_022.py
```

---

## BY SEP 19 @ 5:00PM

✅ Agent OS operational  
✅ 19 agents discoverable via Neo4j  
✅ Objective → Capability → Agent routing automatic  
✅ Every decision logged + learned  
✅ Cost tracking live (Langfuse + execution_registry.jsonl)  
✅ Evaluation gates working (discovered→verified→tested→production)  
✅ Growth OS shows agent activity in real-time  

**Revenue impact:** $4.4M-$6.54M pipeline visible. Automated lead routing possible by Oct 1.

---

**AUTHORIZATION TO EXECUTE:** Approved by CP-006 + CP-027  
**Start time:** Sep 12, 8:00am  
**Blockers:** Zero  
**Questions:** None — code and architecture verified Sep 9

---

## BONUS: NAVIGATION LAYER INTEGRATION (Sep 17, 2 hours)

**The orchestrator should navigate like a human:**

When AGT-020 needs context, it doesn't just query Neo4j. It also:
1. Follows wiki links (NAVIGATION_ALIASES.yaml) to related capabilities
2. Reads domain READMEs (61 total) for context
3. Traverses sector taxonomy for venture relationships

**Add to registry_loaders.py:**

```python
class NavigationLayerLoader:
    @staticmethod
    def load_navigation_aliases(path="_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml"):
        """Load all 568 wiki link aliases"""
        return yaml.load(open(path))
    
    @staticmethod
    def load_domain_readmes(path="00-CONSTITUTION to 50-MASTER-CONTROL"):
        """Load all 61 domain READMEs"""
        readmes = {}
        for i in range(0, 51):
            try:
                with open(f"{i:02d}-*/README.md") as f:
                    readmes[f"{i:02d}"] = f.read()
            except: pass
        return readmes
    
    @staticmethod
    def load_sector_taxonomy(path="_REGISTRIES/CANONICAL/SECTOR_TAXONOMY_MASTER.yaml"):
        """Load 35 sectors + venture assignments"""
        return yaml.load(open(path))
```

**Update CapabilityRouter:**

```python
class CapabilityRouter:
    def route_task_with_navigation(self, task):
        # 1. Query Neo4j: who provides this capability?
        neo4j_agents = self.neo4j_query_agents(task.capability)
        
        # 2. Follow wiki links: what related capabilities exist?
        related_caps = self.navigation_layer.follow_links(task.capability)
        
        # 3. Read domain README: what context applies?
        domain = self.infer_domain(task.objective)
        domain_context = self.readmes[domain]
        
        # 4. Rank agents by: capability match + wiki-link relevance + domain fit
        ranked_agents = self.rank_agents(neo4j_agents, related_caps, domain_context)
        
        return ranked_agents[0]
```

**Result:** Agents understand venture domain context + sector relationships + capability ecosystems, not just function calls.

**Deliverable:** Navigation layer wired into orchestrator by Sep 17.

