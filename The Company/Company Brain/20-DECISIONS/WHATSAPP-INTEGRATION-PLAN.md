---
title: WhatsApp Integration Plan — Company Brain Mobile Control Layer
authority: CP-027 (Infrastructure), CP-033 (Execution), CP-021 (Revenue)
status: PLANNED (Phase 2b, Oct 2026)
version: 1.0
created: 2026-09-19
---

# WhatsApp Integration Plan — Company Brain Mobile Control Layer

**Objective:** Enable remote mobile control of Company Brain (ventures, agents, approvals) via WhatsApp while preserving Claude as reasoning engine and Company Brain as state owner.

**Timeline:** Phase 2b (Oct 2026), 3 weeks, 30-40 hours
**Teams:** DevOps (1), Backend (1), Security (1), QA (1)
**Budget:** $2K (Meta infrastructure), $1.5K (development)

---

## 1. Architecture Decision

**NOT:** WhatsApp → Claude

**YES:** WhatsApp → Company Brain API → Master Orchestrator → Claude + MCP + Neo4j

**Why:** Preserves Company Brain as state owner; Claude is reasoning engine only; WhatsApp is one of N control planes.

---

## 2. Phase 1: Foundation (Week 1, Oct 1-7)

### 2.1 WhatsApp Business Platform Setup

1. Create Meta Business Account
2. Configure WhatsApp Business Cloud API
3. Register phone number (+1 XXX-XXX-XXXX)
4. Configure webhook: `whatsapp-gateway.company-brain.ai`
5. Set webhook events: `messages`, `message_status`

**Credentials:** Store in Bitwarden under "WhatsApp Business Platform"
- META_ACCESS_TOKEN
- BUSINESS_ACCOUNT_ID
- PHONE_NUMBER_ID
- WEBHOOK_VERIFY_TOKEN

### 2.2 Database Schema (Supabase)

Core tables:

```sql
CREATE TABLE whatsapp_contacts (
  id UUID PRIMARY KEY,
  phone_number TEXT UNIQUE NOT NULL,
  display_name TEXT,
  user_id UUID REFERENCES users(id),
  first_message_at TIMESTAMPTZ,
  last_message_at TIMESTAMPTZ,
  status TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE whatsapp_conversations (
  id UUID PRIMARY KEY,
  contact_id UUID REFERENCES whatsapp_contacts(id),
  user_id UUID REFERENCES users(id),
  topic TEXT,
  context JSONB,
  status TEXT,
  created_at TIMESTAMPTZ,
  updated_at TIMESTAMPTZ
);

CREATE TABLE whatsapp_messages (
  id UUID PRIMARY KEY,
  conversation_id UUID REFERENCES whatsapp_conversations(id),
  direction TEXT,
  message_type TEXT,
  external_message_id TEXT UNIQUE,
  sender_type TEXT,
  content TEXT,
  status TEXT,
  created_at TIMESTAMPTZ,
  processed_at TIMESTAMPTZ
);

CREATE TABLE whatsapp_tasks (
  id UUID PRIMARY KEY,
  conversation_id UUID REFERENCES whatsapp_conversations(id),
  intent TEXT,
  orchestrator_task_id UUID REFERENCES tasks(id),
  status TEXT,
  result JSONB,
  created_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ
);

CREATE TABLE whatsapp_approvals (
  id UUID PRIMARY KEY,
  conversation_id UUID REFERENCES whatsapp_conversations(id),
  approval_request_id UUID REFERENCES approval_requests(id),
  action_summary TEXT,
  status TEXT,
  decision_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ
);

CREATE TABLE whatsapp_events (
  id UUID PRIMARY KEY,
  event_type TEXT,
  contact_id UUID REFERENCES whatsapp_contacts(id),
  payload JSONB,
  created_at TIMESTAMPTZ
);
```

---

## 3. Phase 2: Gateway & API (Week 2, Oct 8-14)

### 3.1 WhatsApp Gateway (FastAPI)

**Key endpoints:**

```
GET  /webhooks/whatsapp    → Meta verification
POST /webhooks/whatsapp    → Receive messages
POST /whatsapp/send        → Send messages
GET  /health               → Health check
```

**Workflow:**
1. Receive message from Meta
2. Validate signature
3. Deduplicate (prevent replays)
4. Normalize & store in Supabase
5. Enqueue to orchestrator
6. Get response
7. Send back via Meta API

### 3.2 Company Brain API Endpoints

Add to existing API:

```
POST   /api/v1/orchestrator/classify     → Classify intent
POST   /api/v1/orchestrator/plan         → Plan execution
POST   /api/v1/orchestrator/execute      → Execute task
GET    /api/v1/whatsapp/contacts         → List contacts
GET    /api/v1/whatsapp/conversations    → List conversations
```

---

## 4. Phase 3: Orchestrator Integration (Week 2-3, Oct 8-21)

### 4.1 Intent Classification

```yaml
INTENTS:
  status:
    patterns: ["what's blocking", "status", "update", "progress"]
    agents: ["SALES-001", "OPS-001", "RESEARCH-001"]
    
  agent_run:
    patterns: ["run", "execute", "start", "audit"]
    agents: ["any"]
    
  approval:
    patterns: ["approve", "deny", "confirm", "yes", "no"]
    agents: ["none"]
    
  research:
    patterns: ["research", "find", "investigate"]
    agents: ["RESEARCH-001"]
```

---

## 5. Initial Commands (MVP)

### 5.1 System
- `/help` → List all commands
- `/status` → Company-wide status
- `/whoami` → Show identity + permissions
- `/agents` → List active agents
- `/tasks` → Show active tasks

### 5.2 Business
- `/status lt-005` → HealthRoute metrics
- `/revenue` → Week/month/YTD revenue
- `/pipeline` → Sales pipeline by venture
- `/bottlenecks` → What's blocking each venture

### 5.3 Agent Control
- `/agent status SALES-001` → Is agent running?
- `/agent run RESEARCH-001` → Start research task
- `/agent logs AGENT-RUN-123` → Show execution logs

### 5.4 Approvals
- `/approvals` → Show pending
- `/approve AR-123` → Approve action
- `/deny AR-123` → Deny action

### 5.5 Natural Language (Claude-powered)
```
"What's blocking HealthRoute from its first customer?"
→ Dispatch SALES-001 + OPS-001 + RESEARCH-001
→ Return: "Sales: 26 leads. Ops: 1 issue. Research: Competitor pricing."

"Research 20 Charlotte medical practices for LT-005"
→ Dispatch RESEARCH-001
→ Return: "Found 23 matches. 18 verified. Draft email ready."
```

---

## 6. Security & Permissions

### 6.1 Authentication Layers

1. **Meta → Webhook:** Validate signature/token per Meta spec
2. **Phone → User:** Phone number → user_id → role
3. **Action → Permission:** User role determines what agents/tools are available

### 6.2 Tool Permissions (by agent)

```yaml
SALES-001:
  CRM.search_leads    ✅ ALLOW
  Email.send          ⚠️ APPROVAL
  CRM.delete_lead     ❌ DENY
  Finance.transfer    ❌ DENY

RESEARCH-001:
  Web.search          ✅ ALLOW
  GitHub.read         ✅ ALLOW
  Supabase.query      ✅ ALLOW
  Email.send          ❌ DENY
```

---

## 7. Monitoring & Observability

### 7.1 Metrics
- `whatsapp_messages_received_total` (counter)
- `whatsapp_messages_sent_total` (counter)
- `whatsapp_message_latency_ms` (histogram)
- `orchestrator_tasks_created` (counter)
- `approval_requests_pending` (gauge)

### 7.2 Audit Trail
`whatsapp_events` table tracks:
- User sends message
- Orchestrator classifies intent
- Agent starts execution
- Agent completes
- Approval request created/approved
- Action executes

---

## 8. Rollout Plan

### Phase 1: Closed Beta (Oct 15-21)
- 2 users (owner + ops manager)
- Real ventures only
- Approval workflows mandatory

### Phase 2: Limited Release (Oct 22-31)
- 5 users (executives + lead agents)
- All 6 Tier-0 ventures
- Natural language enabled

### Phase 3: General Availability (Nov 1+)
- All team members
- Full agent registry
- Historical queries

---

## 9. Success Criteria (By Nov 15)

- [ ] 10+ conversations per week via WhatsApp
- [ ] 3+ approval requests executed per week
- [ ] <500ms latency (message → response start)
- [ ] Zero security incidents
- [ ] 95%+ webhook delivery success
- [ ] All 6 Tier-0 ventures queryable
- [ ] 90%+ natural language classification accuracy

---

## 10. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Meta API rate limiting | Exponential backoff + queue |
| Phone spoofing | Verify every request + log numbers |
| Agent runaway costs | max_concurrency=1, approval gate |
| Message loss | Webhook retry, Supabase SoT |
| Timezone confusion | Always UTC, user locale in profile |

---

## 11. Files to Create

- `_MCP/whatsapp_gateway.py` — Gateway server
- `_REGISTRIES/CANONICAL/WHATSAPP_INTENTS.yaml` — Intent definitions
- Supabase schema migrations
- Docker compose update
- E2E tests (Meta webhook simulator)

---

## 12. Next Steps (Immediate)

1. **Sep 19-20:** Create Meta Business Account + webhook URL
2. **Sep 21-22:** Implement WhatsApp Gateway
3. **Sep 23-24:** Create Supabase schema
4. **Sep 25-27:** Wire orchestrator endpoints
5. **Sep 28-30:** End-to-end testing
6. **Oct 1-7:** Beta rollout

---

**Owner:** CP-027 (Infrastructure)
**Stakeholders:** CP-006 (Operations), CP-021 (Revenue), CP-033 (Execution)
**Budget:** $3.5K (Meta API, development)
**Expected ROI:** 30% faster approvals, 40% faster status checks, mobile portfolio control
