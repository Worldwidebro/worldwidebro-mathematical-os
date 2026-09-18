# 01 — The Company Brain

**Version:** 1.0  
**Status:** Foundation Architecture  
**Authority:** [[REALITY|REALITY.md]] + [[STARTHERE|STARTHERE.md]]  

> **The Company Brain is the organizational intelligence layer.** It knows what the organization knows, remembers what it has learned, and provides context to every decision and work allocation.

---

## What the Company Brain Is

The Company Brain is **not a product.** It is the **unified representation of organizational state, knowledge, relationships, and capabilities** that allows the Master Orchestrator to make intelligent decisions about work distribution.

```text
ORGANIZATIONAL STATE
    ├── What exists (entities: ventures, people, investors, agents, skills, tools)
    ├── How things relate (relationships: ownership, investment, capability, dependency)
    ├── What we know (facts, evidence, research, memory)
    ├── How we got here (provenance, history, decisions, precedent)
    ├── What works (past successful patterns, agent performance, revenue attribution)
    └── What matters (strategic priorities, business objectives, constraints)
```

The Company Brain answers these questions:

| Question | Answer Source |
|----------|---|
| **What do we know?** | Knowledge Graph + Memory System + Registries |
| **Where is knowledge stored?** | Neo4j (relationships), Qdrant (semantic), Supabase (transactional), File System (code/docs) |
| **How do we retrieve it?** | Hybrid search (graph + vector + keyword) + context assembly |
| **Who can do what?** | Agent Registry + Skill Registry + Capability Registry |
| **What have we tried?** | Task Execution History + Revenue Attribution + Evaluation Records |
| **What succeeded?** | Agent Performance Stats + Revenue Logs + Evidence System |
| **What failed?** | Error Logs + Failure Analysis + Prevention Tracking |
| **What matters now?** | Business Objectives + Priorities + Constraints + Policies |

---

## Core Components

### 1. Knowledge Graph (Neo4j)

**What it stores:**
- **Entities:** Ventures (789), People (1200+), Investors (300+), Agents (318), Skills (500+), Tools (1000+), Research (5000+)
- **Relationships:** FOUNDED, INVESTED_IN, USES, MANAGES, DEPENDS_ON, SIMILAR_TO, LEARNED_FROM, etc.
- **Attributes:** revenue, cost, success_rate, capability_score, risk_level, last_updated, evidence_links, etc.

**Example queries:**
```cypher
-- "What agents can execute sales tasks in the LT sector?"
MATCH (agent:Agent)-[:HAS_SKILL]->(skill:Skill {category: "sales"})-[:APPLICABLE_TO]->(sector:Sector {id: "LT"})
RETURN agent, skill, agent.success_rate ORDER BY agent.success_rate DESC

-- "What capabilities does OPS-001 require?"
MATCH (venture:Venture {id: "OPS-001"})-[:REQUIRES]->(cap:Capability)<-[:PROVIDES]-(agent:Agent)
RETURN cap, COLLECT(agent) as available_agents

-- "Which investments have dependencies on agents we already have?"
MATCH (i:Investment)-[:DEPENDS_ON]->(cap:Capability)<-[:PROVIDES]-(agent:Agent)
RETURN i, cap, agent
```

**Refresh Rate:** Real-time (webhooks) + hourly (full sync)

---

### 2. Semantic Memory (Qdrant)

**What it stores:**
- Vector embeddings of all text content (documents, past research, agent memories, task results)
- Metadata: source, timestamp, evidence_score, relevance_to_ventures, etc.

**Use cases:**
- "Find similar past research to this new question"
- "What did we learn about Charlotte market last quarter?"
- "Show me all agent interactions related to revenue attribution"

**Refresh Rate:** On document creation/update + weekly recomputation of old embeddings

---

### 3. Transactional State (Supabase PostgreSQL)

**What it stores:**
- Current task executions (status, assignments, deadlines)
- Revenue logs (every dollar attributed to agent + venture + date)
- Agent stats (success rate, cost per task, ROI, capacity)
- Venture financials (MRR, runway, growth rate, customer count)
- Approvals, decisions, audit trails

**Refresh Rate:** Real-time (inserts/updates as work happens)

---

### 4. Registries (YAML)

**What they store:**
- Static inventories: agents, skills, tools, workflows, research sources, repositories, capabilities

**Registries:**
- `AGENT_REGISTRY.yaml` — 318 agents with capabilities, performance history, autonomy level
- `SKILL_REGISTRY.yaml` — 500+ skills with definitions, prerequisites, cost
- `TOOL_REGISTRY.yaml` — 1000+ tools with APIs, permissions, rate limits
- `WORKFLOW_REGISTRY.yaml` — Repeatable processes and loop patterns
- `RESEARCH_REGISTRY.yaml` — Research sources, quality scores, update frequency
- `REPOSITORY_REGISTRY.yaml` — 1740 repos with dependencies, code status, ownership
- `CAPABILITY_REGISTRY.yaml` — Capability matrix (what agents have, what ventures need, gaps)

**Refresh Rate:** Daily (automated sync from deployment logs) + manual (quarterly review)

---

### 5. Evidence System

**What it stores:**
- Proof that claims are true: test results, verification logs, customer feedback, revenue proof
- Attribution: who verified, when, what was tested, what edge cases, what could still fail
- Confidence scores: how certain we are about this claim

**Structure:**
```yaml
claim: "Agent AGT-042 achieves 96% success rate on sales calls"
evidence:
  - source: "task_executions.success_rate (last 30 days)"
    sample_size: 847
    confidence: 0.96
    verified_date: 2026-09-18
    verified_by: "automated_eval"
  - source: "revenue_attribution"
    total_revenue: 125000
    cost: 2500
    roi: 50
    verified_date: 2026-09-18
edge_cases:
  - "May degrade with new prospect list (untested demographic)"
  - "Performance on email-only prospects lower (no phone): 83%"
  - "Charlotte market performs better than national average"
```

**Refresh Rate:** Continuous (as tasks complete)

---

### 6. Memory System

**What it stores:**
- **Short-term:** Current execution context, active tasks, open decisions (expires: hours)
- **Long-term:** Historical patterns, agent performance trends, venture milestones (expires: never)
- **Episodic:** Specific events (this deal closed, this agent failed, this research found X) (expires: per policy)

**Example episodic memory:**
```yaml
episode: "LT-005 Charlotte Launch Research Sprint"
date: 2026-09-15
agents_involved: ["AGT-107", "AGT-042", "AGT-053"]
research_completed:
  - market_analysis (5000 prospects, $50K TAM)
  - competitor_analysis (3 competitors, pricing: $85-150/delivery)
  - regulatory_analysis (no restrictions, local partner needed)
  - financial_model (breakeven in 4 months, payback in 8)
decision_made: "Launch in Charlotte, Oct 1"
revenue_impact: "+$1.5K/month potential"
agents_learned: "Multi-city market research requires 3 parallel agents"
```

**Refresh Rate:** On event + periodic consolidation

---

## How the Brain Serves the Orchestrator

### Query Pattern 1: "What do I know about this?"
```
QUESTION → SEMANTIC SEARCH (Qdrant) → TOP 10 SIMILAR DOCUMENTS
         → GRAPH QUERY (Neo4j) → RELATED ENTITIES
         → TRANSACTIONAL (Supabase) → CURRENT STATE
         → EVIDENCE → CONFIDENCE SCORE
         → CONTEXT PACKAGE → ORCHESTRATOR
```

### Query Pattern 2: "Can we do this?"
```
OBJECTIVE → REQUIRED CAPABILITIES
         → CAPABILITY REGISTRY → COVERED?
         → AGENT REGISTRY → ASSIGN?
         → PAST PERFORMANCE → CONFIDENCE?
         → BUSINESS IMPACT → PRIORITY?
         → ORCHESTRATOR → DECISION
```

### Query Pattern 3: "What should we do next?"
```
BUSINESS OBJECTIVES → VENTURE FINANCIALS → DISTANCE FROM INCOME
                   → AGENT CAPACITY → UNUSED BANDWIDTH?
                   → RESEARCH BACKLOG → PRIORITY?
                   → MEMORY (past learnings) → PRECEDENT?
                   → ORCHESTRATOR → WORK PLAN
```

---

## Brain Capabilities (Ordered by Maturity)

| Capability | Status | Evidence |
|---|---|---|
| **Store facts** (entities, relationships) | ✅ LIVE | 20,363 edges in Neo4j |
| **Retrieve by keyword** | ✅ LIVE | NAVIGATION_ALIASES.yaml |
| **Retrieve by semantics** | ✅ LIVE | Qdrant + 17,236 vectors |
| **Track performance** | ✅ LIVE | agent_stats + revenue_logs |
| **Remember past work** | ✅ LIVE | task_executions history |
| **Evaluate evidence** | 🟡 PARTIAL | Evidence system scaffolding exists |
| **Synthesize research** | 🟡 PARTIAL | Research registry exists, synthesis missing |
| **Detect conflicts** | ❌ MISSING | No contradiction detection |
| **Predict outcomes** | ❌ MISSING | No forecasting models |
| **Suggest next work** | ❌ MISSING | No planning engine |

---

## What the Brain Does NOT Do

The Brain does not:
- **Make decisions** (Orchestrator does)
- **Execute work** (Agents do)
- **Plan** (Orchestrator + Agents do)
- **Evaluate** (Evaluation System does)
- **Verify** (Verification + Evidence System does)

The Brain **provides context for** all of these, but it doesn't **perform** them.

---

## How Knowledge Enters the Brain

```text
1. OBSERVATION
   └─ Task completed, agent report received, customer feedback, market data

2. CAPTURE
   └─ Webhook → Supabase, Evidence → Evidence System, Research → Knowledge Graph

3. ENRICH
   └─ Extract entities, relationships, confidence scores, temporal data

4. INTEGRATE
   └─ Insert into Neo4j, Qdrant (vector), Memory System

5. VERIFY
   └─ Check for conflicts, validate against constraints, assign evidence score

6. SURFACE
   └─ Available in Orchestrator queries within 5 seconds
```

---

## How Knowledge Becomes Stale

The Brain automatically deprecates knowledge:
- **Stale Task Data:** Older than 90 days, retain only aggregated stats
- **Stale Agent Performance:** Update hourly based on new executions
- **Stale Research:** Mark if source >6 months old without refresh
- **Stale Relationships:** If relationship unused for 12 months, flag for review

---

## The Brain-Orchestrator Contract

### The Brain Promises:
✅ "I know the current state of the organization"  
✅ "I can retrieve any fact you ask for (with confidence score)"  
✅ "I remember what worked before"  
✅ "I track evidence for all claims"  
✅ "I consolidate input from all sources"  

### The Orchestrator Promises:
✅ "I will make decisions based on your context"  
✅ "I will record outcomes back to you"  
✅ "I will verify my work against your evidence"  
✅ "I will update you as the organization changes"  
✅ "I will ask for context I don't have rather than guessing"  

---

## References

- [[REALITY|REALITY.md]] — Current Brain state (What's working? What's missing?)
- [[MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] — How the Brain feeds decisions
- [[AGENT-SYSTEM|03-AGENT-SYSTEM.md]] — How agents report back to the Brain
- [[CAPABILITY-SYSTEM|10-CAPABILITY-SYSTEM.md]] — How the Brain tracks capabilities
- [[EXECUTION-LOOP|05-EXECUTION-LOOP.md]] — How data flows through the entire system

---

**Next:** Read [[MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] to understand how the Brain's knowledge drives work distribution.

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
