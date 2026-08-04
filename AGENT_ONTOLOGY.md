---
title: Agent Ontology & Neo4j Schema
version: 1.0
date: 2026-07-30
companion: [[AGENT_SPEC.md]], [[ONTOLOGY.md]], [[VENTURE-ECOSYSTEM-VOCABULARY.md]]
---

# Agent Ontology & Neo4j Schema

**Purpose**: Define Neo4j node and relationship types for agent discovery, routing, and orchestration. Enable Hermes to dynamically route tasks via graph traversal.

---

## Node Types

### Agent

```cypher
(:Agent {
  agent_id: "SA-CON-001-v1",
  name: "SalesAgent",
  type: "SALES_AGENT",
  venture_id: "CON-001",
  status: "LIVE",
  autonomy_level: "LEVEL_3",
  version: "1.0",
  created_at: "2026-07-15",
  confidence_threshold: 0.75,
  budget_monthly: 200,
  cost_ytd: 514
})
```

### Task

```cypher
(:Task {
  task_id: "T-2026-07-30-001",
  venture_id: "CON-001",
  type: "LEAD_QUALIFICATION",
  status: "PENDING",
  priority: "P1",
  assigned_at: "2026-07-30",
  required_capabilities: ["lead_scoring", "crm"],
  deadline: "2026-07-31"
})
```

### Capability

```cypher
(:Capability {
  capability_id: "cap_lead_scoring",
  name: "lead_scoring",
  category: "SALES",
  success_rate: 0.94,
  cost_per_use: 0.05
})
```

### Tool

```cypher
(:Tool {
  tool_id: "tool_crm_api",
  name: "CRM API",
  provider: "Salesforce",
  cost_per_call: 0.01,
  rate_limit: 1000,
  timeout_seconds: 30
})
```

### Venture

```cypher
(:Venture {
  venture_id: "CON-001",
  name: "ACE Construction",
  sector: "construction",
  stage: "MVP",
  monthly_revenue: 15000
})
```

---

## Relationship Types

### Agent Relationships

```
[EXECUTES] Agent → Task (assigned_at, deadline)
[SPAWNED_BY] Agent → Venture (created_at)
[USES] Agent → Tool (since, permission_level)
[PROVIDES] Agent → Capability (success_rate, cost_per_use)
[ROUTED_TO] Agent → Agent (reason, timestamp)
[COMMUNICATES_WITH] Agent → Agent (message_count)
[APPROVED_BY] Agent → Director (timestamp, scope)
[DEPLOYED_TO] Agent → Environment (version, timestamp)
[LIFECYCLE_STATE] Agent → LifecycleStage (stage, started_at)
```

### Task Relationships

```
[REQUIRES] Task → Capability (essential, fallback_available)
[ASSIGNED_TO] Task → Agent (assigned_at, deadline)
[BELONGS_TO] Task → Venture (created_at)
[DEPENDS_ON] Task → Task (order, blocking)
[ESCALATED_TO] Task → Director (reason, timestamp)
```

### Capability Relationships

```
[COMPOSED_OF] Capability → Capability (weight, required)
[REQUIRES] Capability → Tool (essential)
[CONFLICTS_WITH] Capability → Capability (reason)
[PRECEDES] Capability → Capability (order)
```

### Venture Relationships

```
[SPAWNS_AGENT] Venture → Agent (created_at)
[HAS_CAPABILITY] Venture → Capability (coverage, maturity)
[USES] Venture → Tool (since, usage_level)
[NEEDS] Venture → Capability (priority, urgency)
[REFERS_CLIENTS] Venture → Venture (from ONTOLOGY)
```

---

## Graph Query Patterns

### Find Best Agents for Task

```cypher
MATCH (t:Task {task_id: 'T-2026-07-30-001'})
  -[:REQUIRES]->(req:Capability)
MATCH (a:Agent)-[:PROVIDES]->(req)
WHERE a.status = 'LIVE'
  AND a.autonomy_level IN ['LEVEL_3','LEVEL_4','LEVEL_5']
RETURN a ORDER BY a.success_rate DESC LIMIT 3
```

### Agent Capability Discovery

```cypher
MATCH (v:Venture {venture_id: 'CON-001'})
  -[:SPAWNS_AGENT]->(a:Agent)
MATCH (a)-[:PROVIDES]->(c:Capability)-[:REQUIRES]->(t:Tool)
RETURN a.name, COLLECT(c.name), COLLECT(t.name)
```

### Capability Gaps

```cypher
MATCH (v:Venture {venture_id: 'CON-001'})
  -[:NEEDS]->(gap:Capability)
WHERE NOT (v)-[:HAS_CAPABILITY]->(gap)
MATCH (a:Agent)-[:PROVIDES]->(gap)
WHERE a.status = 'LIVE'
RETURN gap.name, a.name, a.autonomy_level
```

### Agent Performance Trend

```cypher
MATCH (a:Agent {agent_id: 'SA-CON-001'})
  -[:EXECUTES]->(t:Task)
WHERE t.completed_at > datetime('2026-07-01')
RETURN COUNT(t), AVG(t.success), SUM(t.cost)
```

---

## Neo4j Indexes

```cypher
CREATE INDEX agent_id ON :Agent(agent_id);
CREATE INDEX agent_status ON :Agent(status);
CREATE INDEX task_id ON :Task(task_id);
CREATE INDEX capability_name ON :Capability(name);
CREATE INDEX venture_id ON :Venture(venture_id);
```

Latency target: < 100ms for routing decisions.

---

## vex-api Integration

```yaml
GET /agents/for-task/{task_id}
  → Neo4j: Find agents for task
  → Response: [{agent_id, success_rate}, ...]
  → SLA: < 500ms

GET /ventures/{venture_id}/agents
  → Neo4j: Agents by venture
  → Response: [{agent_id, type, status}, ...]
  → SLA: < 500ms

POST /tasks/{task_id}/assign
  → Neo4j: Create ASSIGNED_TO relationship
  → Response: {assigned_agent_id, cost_estimate}
  → SLA: < 1s

GET /capabilities/for-venture/{venture_id}
  → Neo4j: Capability coverage + gaps
  → Response: [{capability, coverage, gaps}, ...]
  → SLA: < 1s
```

---

## Integration with ONTOLOGY.md

Agent relationships map to venture ecosystem:

```
Agent [COMMUNICATES_WITH] Agent
  ↓ corresponds to ↓
Venture [REFERS_CLIENTS | CREATES_REVENUE_SYNERGY] Venture

Example: Sales agents coordinate → ventures exchange referrals
```

---

## Version History

- **v1.0 (2026-07-30)**: Agent ontology with Neo4j schema and query patterns.

