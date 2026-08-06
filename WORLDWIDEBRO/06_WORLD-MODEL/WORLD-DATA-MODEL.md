---
name: WORLDWIDEBRO/06_WORLD-MODEL/WORLD-DATA-MODEL
title: WORLDWIDEBRO WORLD DATA MODEL
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# WORLDWIDEBRO WORLD DATA MODEL
## 24 domains, structured for decision → action → outcome → learning

**Status:** Architecture (implementing incrementally)  
**Purpose:** Enable OS to observe → understand → decide → act → verify → learn

---

## THE DECISION LOOP (why this matters)

```
WORLD STATE (reality)
    ↓
OBSERVATION (what is real?)
    ↓
DATA (facts with metadata)
    ↓
KNOWLEDGE (connections + meaning)
    ↓
CONTEXT (what matters for this goal?)
    ↓
GOAL (what are we trying to accomplish?)
    ↓
DECISION (what should we do?)
    ↓
ACTION (execute)
    ↓
OUTCOME (did we achieve the goal?)
    ↓
REVENUE (economic value created?)
    ↓
LEARNING (what did we learn?)
    ↓
UPDATED WORLD MODEL
    ↓
NEXT DECISION (repeat)
```

**Every step requires authoritative, fresh, connected data.**

---

## 24 DATA DOMAINS

| # | Domain | Purpose | Current status |
|---|--------|---------|-----------------|
| 1 | Identity | Who/what is this entity? | 🟢 Partial (Neo4j) |
| 2 | Organization | Company structure, legal entities | 🟡 Minimal |
| 3 | Ventures | Business models, stage, lifecycle | 🟢 Exists (CSV) |
| 4 | Customers | Lead → payment → retention pipeline | 🟡 Partial (CRM) |
| 5 | Markets | Geography, industry, demand, trends | 🟡 Minimal |
| 6 | Competitive | Who competes? Their products/pricing | 🔴 Missing |
| 7 | Capital | Cash, credit, equity, runway | 🟡 Partial |
| 8 | Financial | Revenue, expense, profit, MRR | 🟡 Blocked (Postgres) |
| 9 | Transactions | Quotes, sales, invoices, payments | 🟡 Partial (Stripe) |
| 10 | Repositories | Code, dependencies, capabilities | 🟢 Exists (237 repos) |
| 11 | Files | Metadata: path, type, owner, hash | 🟡 Partial (328K files) |
| 12 | Agents | Purpose, skills, tools, performance | 🟢 Exists (486) |
| 13 | Skills | Definition, inputs, outputs, cost | 🟢 Exists (1,965) |
| 14 | Capabilities | What can be done, who can do it | 🟡 Partial |
| 15 | Tools/MCPs | Contract, version, health, cost | 🟡 Partial |
| 16 | Workflows | Trigger, actions, agents, outcomes | 🟡 Partial (Make) |
| 17 | Decisions | Goal, options, choice, reason, result | 🔴 Missing |
| 18 | Knowledge | Documents, facts, sources, proof | 🟢 Qdrant + Neo4j |
| 19 | Memory | Working, episodic, semantic, org | 🟡 Partial |
| 20 | Infrastructure | Devices, servers, containers, networks | 🟢 Docker visible |
| 21 | Observability | Logs, metrics, traces, errors, latency | 🟡 Langfuse partial |
| 22 | Security | Users, roles, permissions, audit | 🟡 Partial |
| 23 | Governance | Policies, authority, approval, rules | 🟡 CLAUDE.md only |
| 24 | Talent | People, roles, skills, performance | 🟡 Minimal |

---

## ESSENTIAL METADATA ON EVERY ENTITY

```yaml
# Canonical identity
id:                    # Unique ID (e.g., "customer-001", "venture-lt-005")
canonical_name:        # Authority name
type:                  # From ontology (person, venture, repo, etc.)

# Ownership & status
owner:                 # Person/entity responsible
status:                # active / deprecated / archived / unknown
created_at:            # When added to system
updated_at:            # When last modified
verified_at:           # When last confirmed TRUE ← CRITICAL

# Quality & trust
confidence:            # 0.0–1.0 (how certain?)
freshness:             # current / stale / unknown
provenance:            # "from GitHub", "from CSV", "from Stripe", etc.
sensitivity:           # public / internal / confidential

# Connectivity
relationships:         # What connects to this?
```

**This metadata prevents garbage from corrupting your model.**

---

## MINIMUM REGISTRIES FOR 30-DAY EXECUTION

Create these in `WORLDWIDEBRO/06_WORLD-MODEL/REGISTRY/` (CSV format):

### PEOPLE.csv
```
id | name | email | role | organization | status | verified_at
antwuan-johns | Antwuan Johns | [...] | CEO | Worldwidebro | active | 2026-08-04
```

### VENTURES.csv (from existing CSV)
```
venture_id | name | sector | stage | owner | readiness_pct | verified_at
LT-005 | Medical Courier | logistics | validation | ... | 68.0 | 2026-08-04
```

### CUSTOMERS.csv
```
customer_id | name | company | contact_email | status | ltv | acquisition_date | verified_at
cust-001 | John Doe | ABC Corp | [...] | active | 25000 | 2026-07-15 | 2026-08-04
```

### TRANSACTIONS.csv
```
transaction_id | date | type | venture_id | customer_id | amount | status | verified_at
txn-001 | 2026-07-20 | sale | LT-005 | cust-001 | 5000 | completed | 2026-08-04
```

### REVENUE.csv
```
period | venture_id | mrr | arr | customer_count | churn_rate | verified_at
2026-08 | LT-005 | 12000 | 144000 | 8 | 0.05 | 2026-08-04
```

### AGENTS.csv
```
agent_id | name | purpose | skills | status | success_rate | verified_at
agent-dispatch | Dispatch Agent | Route optimization | routing,scheduling | active | 0.92 | 2026-08-04
```

### CAPABILITIES.csv
```
capability_id | name | agents_capable | cost | latency_ms | status | verified_at
cap-dispatch | Logistics Dispatch | agent-dispatch | 100 | 250 | active | 2026-08-04
```

### DECISIONS.csv
```
decision_id | date | goal | chosen_action | expected_outcome | actual_outcome | revenue_created | verified_at
dec-001 | 2026-08-04 | Acquire customer | Outreach to ABC Corp | 1 customer | 1 customer acquired | 5000 | 2026-08-04
```

### LESSONS.csv
```
lesson_id | source_decision | insight | action_taken | status | verified_at
les-001 | dec-001 | Cold outreach to SMBs works | Allocate 50% of sales time to outreach | applied | 2026-08-10
```

---

## WHERE DATA LIVES

| Domain | Primary | Secondary | Query method |
|--------|---------|-----------|--------------|
| Identity | Neo4j | PostgreSQL | Cypher / SQL |
| Ventures | CSV → Neo4j | PostgreSQL | SQL |
| Customers | PostgreSQL | Stripe | SQL |
| Revenue | Stripe / PostgreSQL | Ledger | SQL |
| Repositories | GitHub API → Neo4j | Git | Cypher |
| Agents | Registry → Neo4j | Langfuse | Cypher |
| Workflows | Make / Neo4j | Langfuse traces | Cypher / SQL |
| Decisions | PostgreSQL | Neo4j | SQL |
| Outcomes | PostgreSQL | Neo4j | SQL |
| Knowledge | Qdrant (semantic) + Neo4j (graph) | Obsidian | Vector search / Cypher |
| Infrastructure | Docker + Prometheus | — | Metrics API |
| Observability | Langfuse + Prometheus | Time-series | Query API |

---

## CRITICAL QUERIES YOUR OS MUST ANSWER

### TRACK 1: TRUTH
```sql
-- What is our actual MRR?
SELECT SUM(amount) FROM transactions 
WHERE date >= DATE_TRUNC('month', NOW())
  AND status = 'completed'
  AND verified_at > DATE_SUB(NOW(), INTERVAL 7 DAY);

-- How many active customers?
SELECT COUNT(DISTINCT customer_id) FROM transactions
WHERE status = 'active'
  AND verified_at > DATE_SUB(NOW(), INTERVAL 7 DAY);

-- What ventures are operational?
SELECT venture_id, readiness_pct FROM ventures
WHERE stage IN ('validation', 'growth')
  AND verified_at > DATE_SUB(NOW(), INTERVAL 30 DAY);

-- What is our runway?
SELECT 
  (SELECT SUM(amount) FROM transactions WHERE status = 'active') as cash
  / (SELECT SUM(expense) FROM expenses WHERE month = CURRENT_MONTH) as runway_months;
```

### TRACK 2: CASH
```cypher
-- What can we sell?
MATCH (c:Capability)-[:MONETIZED_AS]->(s:Service)
RETURN c.name, s.price, s.delivery_time;

-- Who should we contact?
MATCH (opp:Opportunity)-[:FOR]->(c:Capability)
WHERE opp.status = 'qualified'
  AND opp.probability > 0.3
RETURN opp.customer, opp.value, opp.deadline;

-- Did we convert?
MATCH (d:Decision)-[:FOR]->(opp:Opportunity)-[:CONVERTED_TO]->(t:Transaction)
RETURN d.date, opp.customer, t.amount, d.reason;
```

### TRACK 3: PLATFORM
```cypher
-- What workflows exist?
MATCH (w:Workflow)-[:USES]->(a:Agent)-[:HAS_SKILL]->(s:Skill)
RETURN w.name, a.name, s.name, w.success_rate;

-- Which agents should handle this task?
MATCH (cap:Capability)-[:IMPLEMENTED_BY]->(a:Agent)
WHERE cap.name = 'Customer Acquisition'
RETURN a.name, a.success_rate, a.cost_per_execution;

-- What did we learn?
MATCH (l:Lesson)<-[:PRODUCES]-(o:Outcome)<-[:RESULTS_IN]-(d:Decision)
WHERE d.date > DATE_SUB(NOW(), INTERVAL 30 DAY)
RETURN l.insight, l.action_taken, COUNT(d) frequency;
```

---

## HOW THIS ENABLES THE 30-DAY PLAN

### TRACK 1: TRUTH (Days 1–7)
- **Registries fill with actual data** (not assumptions)
- **Verified_at shows staleness** (don't trust data older than 7 days)
- **Confidence scores prevent garbage** (only use 0.9+ data for decisions)
- **Revenue registry proves MRR exists** (or doesn't)

### TRACK 2: CASH (Days 1–30)
- **Customers registry** tracks every prospect → customer journey
- **Transactions registry** logs every dollar
- **Decisions registry** explains why we chose each customer
- **Outcomes registry** proves ROI
- Example: "3 outreach decisions → 1 converted → $5K revenue → 20% CAC"

### TRACK 3: PLATFORM (Days 1–30)
- **Capabilities registry** maps offerings → agents → cost
- **Workflows registry** shows execution chains
- **Lessons registry** captures improvements
- **Decisions registry** trains autonomy
- Example: "Outreach works → apply lesson → increase outreach → more customers"

---

## THE PAYOFF (Day 30)

After 30 days of collecting authoritative data:

```
BUSINESS REALITY
├── MRR: $X (from transactions)
├── Customers: X (from customer registry)
├── Runway: X months (from cash / burn)
├── CAC: $X (from decisions + outcomes)
└── Margin: X% (from revenue - cost)

OPERATIONAL REALITY
├── Operational ventures: X (verified stage)
├── Stalled: X (no activity > 30 days)
├── Paperware: X (no code)
└── Health: X/100 (calculated from components)

DECISION QUALITY
├── Decisions made: X
├── Successful: X% (outcomes = goal achieved)
├── Lessons learned: X
├── Lessons applied: X
└── Revenue impact: $X (from applied lessons)

SYSTEM AUTONOMY
├── Automated decisions: X
├── Autonomous workflows: X
├── No human intervention needed: X%
└── Autonomy level: X/12
```

**That is a World Data Model in action:**

Not "we have all the data."

But: **"We observe reality, decide based on evidence, execute, measure outcomes, learn, and improve."**

That transforms from an AI project into an **economic machine**.
