# Architecture Interconnections Map
**Complete Wiki Structure + Relationship Graph**
2026-09-19

---

## Part 1: Document Navigation Graph

```
MASTER ARCHITECTURE
│
├─ [[STARTHERE]] (orientation)
│  └─ This document
│
├─ SOLUTION FINDER SYSTEM
│  ├─ [[SOLUTION-FINDER-SCHEMA.cypher]] (Neo4j constraints)
│  │  └─ Defines: Solution, Problem, SOLVES relationship
│  │     Used by:
│  │      ├─ [[SOLUTION-FINDER-QUERIES.cypher]]
│  │      ├─ [[solution-finder-core.js]]
│  │      └─ [[DATA-ENGINEERING-PLATFORM-DESIGN]]
│  │
│  ├─ [[SOLUTION-FINDER-QUERIES.cypher]] (executable queries)
│  │  └─ Queries defined in: [[SOLUTION-FINDER-SCHEMA.cypher]]
│  │     Implements: 5 discovery queries + 3 registration queries
│  │     Used by: [[solution-finder-core.js]]
│  │
│  ├─ [[QDRANT-SOLUTION-VECTORS.json]] (vector schema)
│  │  └─ Defines: solution embedding space
│  │     Related: [[SOLUTION-FINDER-INTEGRATION-MAP]]
│  │
│  ├─ [[solution-finder-core.js]] (orchestrator)
│  │  └─ Queries:
│  │      ├─ Neo4j via [[SOLUTION-FINDER-QUERIES.cypher]]
│  │      ├─ Qdrant via [[QDRANT-SOLUTION-VECTORS.json]]
│  │      └─ graft (code search)
│  │     Tests: [[solution-finder.test.js]]
│  │     Evals: [[solution-finder-eval.js]]
│  │
│  ├─ [[solution-finder.test.js]] (6 integration tests)
│  │  └─ Tests: [[solution-finder-core.js]]
│  │
│  ├─ [[solution-finder-mcp.py]] (FastMCP server)
│  │  └─ Exposes: [[solution-finder-core.js]] as MCP tools
│  │
│  ├─ [[solution-finder-eval.js]] (8 test cases)
│  │  └─ Evaluates: [[solution-finder-core.js]] quality
│  │
│  └─ [[SOLUTION-FINDER-INTEGRATION-MAP.md]] (master integration doc)
│     └─ Shows:
│         ├─ How SF connects to Neo4j
│         ├─ How SF connects to Qdrant
│         ├─ How SF connects to GitHub repos
│         ├─ How SF connects to VEX
│         └─ How SF enables reuse across 789 ventures
│
├─ PORTFOLIO INTELLIGENCE SYSTEM
│  ├─ [[PORTFOLIO-INTELLIGENCE-LOOP.md]] (master doc)
│  │  └─ Shows:
│  │      ├─ Tabs (local + remote contexts)
│  │      ├─ Loops (revenue, learning, dev, portfolio)
│  │      ├─ Ventures (789 mapped by sector)
│  │      ├─ Repos (177 owned + 618 templates + 1K+ starred)
│  │      ├─ Knowledge graph relationships (Neo4j)
│  │      └─ Interactive queries to see everything
│  │
│  └─ Related: [[VEX-PORTFOLIO-ACCURACY-LOOP]]
│
├─ DATA LOCALITY & ACCURACY SYSTEMS
│  ├─ [[DATA-LOCALITY-MAP.md]] (where data lives)
│  │  └─ Maps:
│  │      ├─ Vercel deployments (7 ventures)
│  │      ├─ Supabase (transactional, source of truth)
│  │      ├─ Mac Studio (Neo4j, Qdrant, Docker)
│  │      ├─ T7 Shield (storage, unknown contents)
│  │      ├─ Lacie (unknown)
│  │      └─ OmniRoute (110 tools, routing)
│  │     References: [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]]
│  │
│  └─ [[VEX-PORTFOLIO-ACCURACY-LOOP.md]] (verification + wiring)
│     └─ Shows:
│         ├─ How to verify VEX data is real
│         ├─ Daily audit checks
│         ├─ Solution Finder metrics wired into VEX tabs
│         └─ API endpoints to implement
│        References: [[DATA-LOCALITY-MAP]], [[SOLUTION-FINDER-INTEGRATION-MAP]]
│
├─ DATA ENGINEERING PLATFORM
│  └─ [[DATA-ENGINEERING-PLATFORM-DESIGN.md]] (modern data stack)
│     └─ Designs:
│         ├─ Fivetran CDC (Supabase → S3)
│         ├─ dbt transformations (staging → marts)
│         ├─ Snowflake/BigQuery warehouse
│         ├─ DataHub catalog
│         ├─ Great Expectations quality checks
│         └─ 4-week implementation roadmap
│        References:
│         ├─ [[DATA-LOCALITY-MAP]] (data sources)
│         ├─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (data contracts)
│         └─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (metrics wiring)
│
└─ WORLDWIDEBRO HOLDINGS OPERATING SYSTEM
   └─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE.md]] (complete OS)
      └─ Defines:
          ├─ Legal entity structure (holding + subsidiaries + IP)
          ├─ Operating org (C-suite + ventures + shared services)
          ├─ Agent organization (orchestrators at every level)
          ├─ Asset & capital graph (who owns what)
          ├─ Governance & authority matrix
          ├─ Data contracts (Venture, Capital, Ownership)
          ├─ VEX as command center
          └─ 8-week implementation roadmap
         References:
          ├─ [[SOLUTION-FINDER-INTEGRATION-MAP]] (solution discovery)
          ├─ [[PORTFOLIO-INTELLIGENCE-LOOP]] (visibility)
          ├─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (data accuracy)
          ├─ [[DATA-LOCALITY-MAP]] (where data lives)
          └─ [[DATA-ENGINEERING-PLATFORM-DESIGN]] (data pipelines)
```

---

## Part 2: System Relationship Graph

```
EXECUTION FLOW

Founder (Human)
    │
    ├─→ VEX Dashboard (visualization)
    │    ├─ Executive view
    │    ├─ Venture deep-dives
    │    ├─ Financial consolidated
    │    ├─ Organization view
    │    ├─ Capital allocation
    │    └─ Governance
    │
    ├─→ Company Brain (data + orchestration)
    │    ├─ Neo4j (relationships)
    │    │  └─ Venture nodes
    │    │  └─ Solution nodes
    │    │  └─ Capability nodes
    │    │  └─ Agent nodes
    │    │  └─ Sector nodes
    │    │  └─ 20,363 edges
    │    │
    │    ├─ Supabase (transactional)
    │    │  ├─ ventures table (789 rows)
    │    │  ├─ metrics table (18K+ rows)
    │    │  ├─ capabilities table (300+ rows)
    │    │  ├─ agents table (318 rows)
    │    │  └─ revenue tracking
    │    │
    │    ├─ Qdrant (semantic)
    │    │  ├─ Solution vectors (17,236)
    │    │  ├─ Pattern vectors
    │    │  └─ Venture vectors
    │    │
    │    └─ Asset Graph (capital)
    │       ├─ Cash positions
    │       ├─ Equity ownership
    │       ├─ IP assets
    │       └─ Obligations
    │
    └─→ Agents (execution)
         ├─ Master Orchestrator
         │  └─ Coordinates all agents
         │
         ├─ Executive Agents
         │  ├─ CEO Agent
         │  ├─ CFO Agent
         │  ├─ COO Agent
         │  └─ CTO Agent
         │
         ├─ Function Orchestrators
         │  ├─ Sales Orchestrator
         │  ├─ Finance Orchestrator
         │  ├─ Ops Orchestrator
         │  ├─ Tech Orchestrator
         │  └─ Marketing Orchestrator
         │
         └─ Venture Orchestrators
            ├─ HealthRoute (LT-005)
            ├─ ACE (CON-001)
            ├─ Staffing (OPS-001)
            ├─ Real Estate (RE-001)
            ├─ Dispatch (LT-011)
            └─ Future ventures
```

**Decision Flow:**
```
Agent needs to decide
    │
    ├─ Query Neo4j (relationships)
    ├─ Query Supabase (transactional state)
    ├─ Query Qdrant (semantic similarity)
    └─ Check Asset Graph (available capital)
    │
    ├─ Run decision logic
    │
    ├─ Query Solution Finder (has this been solved?)
    │  └─ [[SOLUTION-FINDER-INTEGRATION-MAP]]
    │
    ├─ Produce recommendation
    │
    ├─ Check approval matrix
    │  └─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Governance section
    │
    ├─ Submit for approval (if needed)
    │
    └─ Execute → Monitor → Report
```

---

## Part 3: Data Flow Architecture

```
DATA SOURCES
    │
    ├─ Supabase (PostgreSQL)
    │  ├─ ventures table
    │  ├─ metrics table
    │  ├─ capabilities table
    │  └─ agent tracking
    │  └─ Reference: [[DATA-LOCALITY-MAP]]
    │
    ├─ GitHub repositories
    │  ├─ 177 code repos
    │  ├─ 618 template repos
    │  └─ 1K+ starred repos
    │  └─ Reference: [[SOLUTION-FINDER-INTEGRATION-MAP]]
    │
    ├─ Vercel deployments
    │  └─ 7 live ventures
    │  └─ Reference: [[DATA-LOCALITY-MAP]]
    │
    └─ OmniRoute
       └─ 110 tools + routing
       └─ Reference: [[DATA-LOCALITY-MAP]]
    │
    ├─→ INGESTION LAYER
    │   ├─ Fivetran (CDC from Supabase)
    │   └─ Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]]
    │
    ├─→ STORAGE LAYER
    │   ├─ S3 / T7 Shield (data lake)
    │   ├─ Neo4j (graph relationships)
    │   ├─ Qdrant (vectors)
    │   └─ Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]], [[DATA-LOCALITY-MAP]]
    │
    ├─→ TRANSFORMATION LAYER
    │   ├─ dbt (staging → marts)
    │   ├─ Solution Finder (pattern extraction)
    │   └─ Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]], [[SOLUTION-FINDER-INTEGRATION-MAP]]
    │
    ├─→ QUALITY LAYER
    │   ├─ Great Expectations (validation)
    │   ├─ Data contracts (Schema validation)
    │   └─ Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]], [[VEX-PORTFOLIO-ACCURACY-LOOP]]
    │
    ├─→ WAREHOUSE LAYER
    │   ├─ Snowflake / BigQuery
    │   └─ Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]]
    │
    ├─→ ANALYTICS LAYER
    │   ├─ VEX Dashboard
    │   ├─ BI tools
    │   └─ Real-time queries
    │   └─ Reference: [[VEX-PORTFOLIO-ACCURACY-LOOP]]
    │
    └─→ APPLICATION LAYER
        └─ Agents (autonomous execution)
           └─ Reference: [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]]
```

---

## Part 4: System Dependencies

```
DEPENDENCY MAP

[[SOLUTION-FINDER-INTEGRATION-MAP]]
    ↓
Depends on:
├─ [[SOLUTION-FINDER-SCHEMA.cypher]] (Neo4j schema)
├─ [[SOLUTION-FINDER-QUERIES.cypher]] (queries)
├─ [[QDRANT-SOLUTION-VECTORS.json]] (vectors)
├─ [[solution-finder-core.js]] (orchestrator)
└─ [[DATA-LOCALITY-MAP]] (where to query)

Feeds into:
├─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (metrics to show)
├─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (agent decisions)
└─ All ventures (reuse instead of rebuild)

---

[[DATA-ENGINEERING-PLATFORM-DESIGN]]
    ↓
Depends on:
├─ [[DATA-LOCALITY-MAP]] (data sources)
├─ [[SOLUTION-FINDER-INTEGRATION-MAP]] (patterns to extract)
├─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (data contracts)
└─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (metrics to populate)

Feeds into:
├─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (real-time data)
├─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (decision layer)
└─ All 789 ventures (unified data platform)

---

[[VEX-PORTFOLIO-ACCURACY-LOOP]]
    ↓
Depends on:
├─ [[DATA-LOCALITY-MAP]] (where data lives)
├─ [[SOLUTION-FINDER-INTEGRATION-MAP]] (metrics to wire)
├─ [[DATA-ENGINEERING-PLATFORM-DESIGN]] (data freshness)
└─ [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (dashboard structure)

Feeds into:
├─ Founder (visibility)
├─ Agents (context for decisions)
└─ VEX Dashboard (real-time view)

---

[[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]]
    ↓
Depends on:
├─ [[PORTFOLIO-INTELLIGENCE-LOOP]] (visibility requirements)
├─ [[SOLUTION-FINDER-INTEGRATION-MAP]] (agent capabilities)
├─ [[DATA-ENGINEERING-PLATFORM-DESIGN]] (data foundation)
├─ [[VEX-PORTFOLIO-ACCURACY-LOOP]] (command center)
└─ [[DATA-LOCALITY-MAP]] (where everything lives)

Feeds into:
├─ Legal structure (entity formation)
├─ Operating org (human hierarchy)
├─ Agent org (AI execution)
├─ Capital allocation (asset graph)
└─ VEX (command center)
```

---

## Part 5: Quick Reference - "Where Do I Find X?"

### Legal/Governance Questions
- **Legal entity structure?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 1: Legal Entity Structure
- **Approval authority?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 4: Governance & Authority Matrix
- **Data contracts?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 5: Data Contracts
- **Estate planning?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 1: Legal Entity Structure

### Architecture Questions
- **How does Solution Finder work?** → [[SOLUTION-FINDER-INTEGRATION-MAP]]
- **What's running right now?** → [[PORTFOLIO-INTELLIGENCE-LOOP]] → Part 1: Three Questions
- **Where does data live?** → [[DATA-LOCALITY-MAP]]
- **How do systems connect?** → This document ([[ARCHITECTURE-INTERCONNECTIONS]])

### Execution Questions
- **How do agents execute?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 2: Master Orchestrator Logic
- **How do I make a capital decision?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 2: Master Orchestrator Logic
- **How does VEX show everything?** → [[VEX-PORTFOLIO-ACCURACY-LOOP]] → VEX Dashboard visualization

### Data Infrastructure Questions
- **How do I build real-time pipelines?** → [[DATA-ENGINEERING-PLATFORM-DESIGN]] → Part 4-5: Pipeline Design
- **How do I verify data accuracy?** → [[VEX-PORTFOLIO-ACCURACY-LOOP]] → Part 5: Verification Checklist
- **How do I track solutions?** → [[SOLUTION-FINDER-INTEGRATION-MAP]] → Part 4: Eval Strategy

### Implementation Questions
- **What's the roadmap?** → [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 6: Implementation Roadmap (8 weeks)
- **What's the cost?** → [[DATA-ENGINEERING-PLATFORM-DESIGN]] → Part 7: Cost Optimization + [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 8: Cost/Timeline
- **What do I do first?** → This document → Part 6: Implementation Priority Order

---

## Part 6: Implementation Priority Order (with Document References)

### Week 1: Foundation

**Task 1.1:** Load Neo4j Schema
- Reference: [[SOLUTION-FINDER-SCHEMA.cypher]]
- Depends on: Nothing
- Enables: 1.2, 1.3

**Task 1.2:** Execute Cypher Queries
- Reference: [[SOLUTION-FINDER-QUERIES.cypher]]
- Depends on: 1.1
- Enables: 1.3

**Task 1.3:** Run Solution Finder Tests
- Reference: [[solution-finder.test.js]]
- Depends on: 1.1, 1.2
- Outcome: 6/6 PASS

**Task 1.4:** Inventory T7 Shield
- Reference: [[DATA-LOCALITY-MAP]] → T7 Shield section
- Depends on: Nothing
- Enables: 2.1

### Week 2: Verification

**Task 2.1:** Deploy Data Engineering Week 1
- Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]] → Phase 1
- Depends on: 1.4
- Cost: $1.2K

**Task 2.2:** Wire VEX Solutions Tabs
- Reference: [[VEX-PORTFOLIO-ACCURACY-LOOP]] → Part 4: API Endpoints
- Depends on: 1.3
- Enables: 3.1

**Task 2.3:** Meet with Attorney
- Reference: [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 6: Phase 1
- Depends on: Nothing
- Outcome: Operating Agreement drafted

### Week 3: Organization

**Task 3.1:** Implement Hourly Neo4j Sync
- Reference: [[VEX-PORTFOLIO-ACCURACY-LOOP]] → Part 2: Sync Status
- Depends on: 2.1
- Enables: 3.2

**Task 3.2:** Map OmniRoute to Ventures
- Reference: [[DATA-LOCALITY-MAP]] → OmniRoute section
- Depends on: 3.1
- Enables: 4.1

### Month 1: Full Platform

**Task 4.1:** Complete Data Engineering (Weeks 2-4)
- Reference: [[DATA-ENGINEERING-PLATFORM-DESIGN]] → Phases 2-4
- Depends on: 2.1
- Cost: ~$700

**Task 4.2:** Implement Agent Orchestrators
- Reference: [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] → Part 3: Agent Organization
- Depends on: 3.2
- Enables: 4.3

**Task 4.3:** Go-Live: Full Platform
- Reference: [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]]
- Depends on: 4.1, 4.2
- Outcome: Enterprise OS live in VEX

---

## Part 7: Key Interconnections (Detailed)

### Solution Finder Interconnects With

**Neo4j:**
- Reads: [[SOLUTION-FINDER-SCHEMA.cypher]] defines Solution + Problem + SOLVES relationship
- Queries: [[SOLUTION-FINDER-QUERIES.cypher]] searches for solutions by problem name
- Updates: Records solution usage via [[solution-finder-core.js]]

**Qdrant:**
- Vectors: [[QDRANT-SOLUTION-VECTORS.json]] defines embedding space
- Search: [[solution-finder-core.js]] performs semantic search
- Update: New solutions stored via [[solution-finder-mcp.py]]

**Ventures:**
- Discovery: Agents query via [[SOLUTION-FINDER-INTEGRATION-MAP]]
- Reuse: Ventures find existing solutions before building new
- Learning: [[solution-finder-eval.js]] measures effectiveness

**Data Engineering:**
- Vectors: [[DATA-ENGINEERING-PLATFORM-DESIGN]] ingests solution metadata
- Quality: [[Great Expectations]] validates solution integrity
- Warehouse: Solutions queryable from [[Snowflake/BigQuery]]

### VEX Interconnects With

**Company Brain:**
- Neo4j: Real-time queries for relationships
- Supabase: Live venture metrics
- Qdrant: Semantic patterns
- Asset Graph: Capital positions

**Solutions:**
- [[SOLUTION-FINDER-INTEGRATION-MAP]] feeds metrics
- [[VEX-PORTFOLIO-ACCURACY-LOOP]] shows solutions used per venture
- New tabs: Solutions Registry, Venture Solutions, Portfolio Metrics

**Data Platform:**
- [[DATA-ENGINEERING-PLATFORM-DESIGN]] provides real-time data
- [[DATA-LOCALITY-MAP]] shows data sources
- [[Great Expectations]] ensures accuracy

### Worldwidebro Holdings Interconnects With

**Everything:**
- Legal structure enables [[all subsidiaries]]
- Agent org implements [[all orchestrators]]
- Governance matrix enforces [[approval workflows]]
- Data contracts define [[all entities]]
- Asset graph tracks [[all capital]]
- VEX visualizes [[entire OS]]

---

## Summary: The Complete Interconnection

```
FOUNDER
    │
    ├─ APPROVES (via [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] authority matrix)
    │
    ├─ VIEWS (via [[VEX-PORTFOLIO-ACCURACY-LOOP]] dashboard)
    │
    ├─ UNDERSTANDS STRUCTURE (via [[PORTFOLIO-INTELLIGENCE-LOOP]])
    │
    └─ OPERATES (via [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] + [[SOLUTION-FINDER-INTEGRATION-MAP]])
       │
       ├─ Agents query Company Brain:
       │  ├─ Neo4j ([[SOLUTION-FINDER-SCHEMA]])
       │  ├─ Supabase ([[DATA-LOCALITY-MAP]])
       │  ├─ Qdrant ([[QDRANT-SOLUTION-VECTORS]])
       │  └─ Asset Graph ([[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]])
       │
       ├─ Agents execute decisions:
       │  ├─ Via [[SOLUTION-FINDER-INTEGRATION-MAP]] (find existing solutions)
       │  ├─ Via [[WORLDWIDEBRO-HOLDINGS-MASTER-ARCHITECTURE]] (approval gates)
       │  └─ Via [[VEX-PORTFOLIO-ACCURACY-LOOP]] (track + report)
       │
       ├─ Data flows:
       │  ├─ Ingestion: [[DATA-ENGINEERING-PLATFORM-DESIGN]] (Fivetran)
       │  ├─ Processing: [[DATA-ENGINEERING-PLATFORM-DESIGN]] (dbt)
       │  ├─ Quality: [[VEX-PORTFOLIO-ACCURACY-LOOP]] (Great Expectations)
       │  └─ Analytics: [[VEX-PORTFOLIO-ACCURACY-LOOP]] (dashboard)
       │
       └─ 789 ventures execute
           └─ All discoverable via [[SOLUTION-FINDER-INTEGRATION-MAP]]
```

---

**Everything is wired. Everything is connected. Follow the wiki links to understand the full system.**

