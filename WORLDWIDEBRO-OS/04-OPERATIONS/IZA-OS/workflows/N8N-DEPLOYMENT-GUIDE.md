# IZA OS Phase 3: n8n Workflow Deployment Guide

## Overview

Three production-ready n8n workflows automate IZA OS capability routing, decision-making, and escalation systems. These workflows route requests through departments to agents, decisions through authority hierarchies, and escalate when thresholds are exceeded.

**Files:**
1. `CAPABILITY-REQUEST-FLOW.json` — Routes capability requests → departments → agents
2. `DECISION-ROUTING-FLOW.json` — Routes decisions by amount/type through authority chain
3. `ESCALATION-FLOW.json` — Handles escalations with 4-hour timeout and fallback chain

---

## Pre-Deployment Checklist

### Credentials Required

Configure these credentials in n8n before importing:

| Credential | Type | Details |
|---|---|---|
| `supabase-prod` | PostgreSQL | Host: `db.supabase.xyz`, Port: 5432, User: `postgres` |
| `neo4j-local` | Neo4j | URI: `bolt://localhost:7687`, User: `neo4j`, Password: (set in CLAUDE.md) |
| `slack-bot` | Slack | OAuth token with `chat:write`, `chat:read` permissions |

### Database Tables Required

**Supabase (PostgreSQL):**

```sql
-- ventures_requesting table
CREATE TABLE ventures_requesting (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  capability_required TEXT NOT NULL,
  priority TEXT DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
  context JSONB,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'assigned', 'escalation_pending', 'completed')),
  assigned_agent_id UUID,
  assigned_department_id UUID,
  escalation_reason TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- decisions table
CREATE TABLE decisions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  decision_type TEXT NOT NULL,
  amount NUMERIC(15,2) DEFAULT 0,
  venture_id TEXT NOT NULL,
  context JSONB,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'awaiting_director', 'awaiting_hermes', 'awaiting_human')),
  authority_routed_to TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- escalations table
CREATE TABLE escalations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escalation_type TEXT NOT NULL CHECK (escalation_type IN ('no_available_agents', 'capability_not_found', 'large_amount', 'irreversible')),
  request_id UUID REFERENCES ventures_requesting(id),
  decision_id UUID REFERENCES decisions(id),
  department_id UUID,
  venture_id TEXT NOT NULL,
  current_holder TEXT,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'awaiting_director', 'awaiting_hermes', 'awaiting_human', 'timeout_expired', 'resolved')),
  escalation_chain JSONB DEFAULT '["venture", "department", "hermes", "human"]',
  escalation_reason TEXT,
  next_escalation_time TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### Neo4j Graph Nodes Required

```cypher
-- Department node
CREATE (d:Department {
  id: 'DEPT-001',
  name: 'Operations',
  director_id: 'AGENT-001'
});

-- Agent nodes
CREATE (a:Agent {
  id: 'AGENT-001',
  name: 'Director Smith',
  status: 'available',
  role: 'director',
  email: 'smith@iza-os.local'
});

CREATE (a2:Agent {
  id: 'AGENT-002',
  name: 'Agent Jones',
  status: 'available',
  expertise: 'scheduling,logistics',
  email: 'jones@iza-os.local'
});

-- Capability node
CREATE (c:Capability {
  name: 'scheduling'
});

-- Relationships
CREATE (d)-[:PROVIDES_CAPABILITY]->(c);
CREATE (d)-[:HAS_AGENT]->(a2);
CREATE (d)-[:LED_BY]->(a);

-- Hermes node
CREATE (h:Hermes {
  id: 'hermes-001',
  name: 'Hermes Coordination Engine',
  status: 'available',
  channel: '#iza-os-hermes'
});

-- Human approver node
CREATE (human:Human {
  id: 'human-001',
  name: 'Human Approver',
  role: 'approver',
  status: 'available',
  email: 'approver@iza-os.local'
});
```

---

## Workflow 1: Capability Request Flow

**Purpose:** Route capability requests from ventures to appropriate departments and agents.

**Flow:**
1. **Webhook Receive** — Listen for POST at `/webhook/capability-request`
2. **Log to Supabase** — Insert into `ventures_requesting` table
3. **Query Neo4j** — Find department providing the capability
4. **Check Department** — If found, continue; if not, escalate
5. **Find Available Agent** — Query for available agents in department
6. **Check Agent** — If found, assign; if not, escalate
7. **Update Assignment** — Write agent assignment to Supabase
8. **Update Dashboard** — HTTP POST to `/api/dashboard/request/update`
9. **Notify Agent** — Slack message to agent's channel
10. **Return Success** — Webhook response with request ID

**Input Payload:**
```json
{
  "venture_id": "VENT-001",
  "capability_required": "scheduling",
  "priority": "high",
  "context": {
    "deadline": "2026-07-20",
    "budget": 50000
  }
}
```

**Output:**
```json
{
  "request_id": "uuid",
  "assigned_agent_id": "AGENT-002",
  "status": "assigned",
  "timestamp": "2026-07-16T18:00:00Z"
}
```

**Error Handling:**
- **No Department Found** → Escalation Flow (capability_not_found)
- **No Agents Available** → Escalation Flow (no_available_agents)
- **Database Error** → Log error to Slack #iza-os-errors

---

## Workflow 2: Decision Routing Flow

**Purpose:** Route decisions through authority hierarchy based on amount and type.

**Flow:**
1. **Webhook Receive** — Listen for POST at `/webhook/decision-submit`
2. **Log Decision** — Insert into `decisions` table with status='pending'
3. **Check Irreversible** — If decision_type='irreversible', escalate to human
4. **Check Amount > $25K** — If yes, escalate to Hermes
5. **Check Amount $5K-$25K** — If in range, route to department director
6. **Amount < $5K** — Auto-approve
7. **Execute Decision** — HTTP POST to `/api/decision/execute`
8. **Update Status** — Set status='approved' in Supabase
9. **Notify** — Slack message to appropriate authority

**Authority Hierarchy:**
- `amount < $5K` → **Auto-approve** (venture lead can decide)
- `$5K ≤ amount ≤ $25K` → **Department Director** (4-hour timeout)
- `amount > $25K` → **Hermes System** (4-hour timeout)
- `decision_type = 'irreversible'` → **Human Approver** (4-hour timeout)

**Input Payload:**
```json
{
  "venture_id": "VENT-001",
  "decision_type": "budget_allocation",
  "amount": 15000,
  "context": {
    "justification": "Q3 hiring budget",
    "team": "operations"
  }
}
```

**Output:**
```json
{
  "decision_id": "uuid",
  "status": "awaiting_director",
  "authority_routed_to": "AGENT-001",
  "timestamp": "2026-07-16T18:00:00Z"
}
```

---

## Workflow 3: Escalation & Fallback Flow

**Purpose:** Handle escalations and enforce 4-hour timeout with automatic escalation.

**Escalation Chain:**
```
Venture → Department Director → Hermes System → Human Approver
  ↓          (4h timeout)        (4h timeout)    (FINAL)
  └→ If no response within 4h, auto-escalate to next level
```

**Features:**
- 4-hour timeout per authority level
- Automatic escalation to next level on timeout
- Audit trail in Supabase for all escalations
- Slack alerts to #iza-os-critical on timeout

---

## Deployment Steps

### 1. Configure Credentials (n8n UI)

Go to Credentials and create:
- PostgreSQL for Supabase
- Neo4j for local instance
- Slack for bot

### 2. Import Workflows

**Via n8n UI:**
1. Go to Workflows > Import
2. Upload each JSON file
3. Confirm credentials
4. Activate workflows

**Via CLI:**
```bash
npx n8n import:workflow --input CAPABILITY-REQUEST-FLOW.json
npx n8n import:workflow --input DECISION-ROUTING-FLOW.json
npx n8n import:workflow --input ESCALATION-FLOW.json
```

### 3. Test Endpoints

```bash
# Test capability request
curl -X POST http://localhost:5678/webhook/capability-request \
  -H "Content-Type: application/json" \
  -d '{"venture_id": "VENT-001", "capability_required": "scheduling", "priority": "high"}'

# Test decision submit
curl -X POST http://localhost:5678/webhook/decision-submit \
  -H "Content-Type: application/json" \
  -d '{"venture_id": "VENT-001", "decision_type": "budget_allocation", "amount": 15000}'

# Test escalation
curl -X POST http://localhost:5678/webhook/escalation-flow \
  -H "Content-Type: application/json" \
  -d '{"escalation_type": "no_available_agents", "venture_id": "VENT-001", "department_id": "DEPT-001"}'
```

### 4. Verify Database

```sql
SELECT * FROM ventures_requesting ORDER BY created_at DESC LIMIT 5;
SELECT * FROM decisions ORDER BY created_at DESC LIMIT 5;
SELECT * FROM escalations ORDER BY created_at DESC LIMIT 5;
```

---

## Production Checklist

- [ ] Database tables created
- [ ] Neo4j nodes created
- [ ] n8n credentials configured
- [ ] All workflows imported and activated
- [ ] Webhook endpoints tested
- [ ] Slack channels created
- [ ] Monitoring set up
- [ ] 4-hour timeout tested
- [ ] Escalation chain tested end-to-end

---

## Error Response Protocol

| Issue | Check | Fix |
|---|---|---|
| Workflow not triggering | Workflow is active; webhook path correct | Activate workflow; verify payload |
| Database write error | Credentials correct; tables exist | Recreate tables; test Supabase connection |
| Neo4j query error | Neo4j running; nodes exist | Start Neo4j; create nodes via Cypher |
| Slack not sending | Bot token valid; channel access | Refresh token; add bot to channels |

---

## Maintenance

**Daily:** Monitor pending escalations and decisions  
**Weekly:** Review escalation patterns and approval times  
**Monthly:** Audit timeout frequency; verify agent availability accuracy

---

## Support & Integration

These workflows integrate with:
- **Supabase** for audit trails
- **Neo4j** for entity resolution
- **Slack** for notifications
- **Dashboard API** for real-time status updates
- **Hermes Coordination Engine** for high-level decisions

---

Version: Wave 1, Task 3 | Updated: 2026-07-16
