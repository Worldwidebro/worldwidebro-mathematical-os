---
id: INFRA-CRM-EVAL-001
title: "Three CRM Systems: Evaluation Summary"
aliases: ["CRM Evaluation", "Twenty CRM vs Comp AI", "CRM Integration"]
tags: ["crm", "evaluation", "twenty", "clickup", "comp-ai", "intelligence-layer"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[23-VENTURES/23-VENTURES|Ventures Ecosystem]] | [[16-AGENTS/README|16-AGENTS Fleet]] | [[54-FINANCIAL/README|54-FINANCIAL]]

# Three CRM Systems: Evaluation Summary

**Date:** 2026-09-06  
**Status:** Phase 2 Planning  
**Purpose:** Understand how Comp AI CRM, Twenty, and ClickUp map to [[50-MASTER-CONTROL/50-MASTER-CONTROL|Company Brain layers]]

---

## THE THREE SYSTEMS

### 1. Comp AI CRM — Intelligence Layer ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-031]])

**Philosophy:** "The agent is not a feature of the CRM; the CRM is where the agent keeps its notes."

**Architecture:**
```
Agent Layer (Eve framework)
  ├── Tools: research_person, enrich_company, record_fact, schedule_recheck
  ├── Skills: Autonomous execution on own schedule
  ├── Sandbox: No network access, no DB credentials
  └── Evidence Ledger: Never guess, only record observed facts

API Layer (NestJS + tRPC)
  └── Type-safe, authenticated endpoints

Frontend (Next.js)
  └── Agent monitoring tab (reasoning, discarded leads, open questions)

Database (PostgreSQL + Prisma ORM)
  └── Immutable evidence log
```

**What makes it unique:**
- Agent operates autonomously while humans sleep
- Rejects confidence scores entirely
- Records only observed facts (evidence-based)
- Human reviews only when evidence quality is ambiguous
- Durable agent sessions (resume mid-research)

**Role in Company Brain:**
- Discovers facts about companies/people/markets
- Records evidence (timestamped, sourced, verifiable)
- Schedules rechecks (stay current over time)
- Feeds Neo4j with discovered relationships
- Triggers Twenty updates automatically

**Example workflow:**
```
Comp AI Agent
  ↓ "Company X expanded into healthcare"
  ↓ [records evidence: source, date, confidence]
Neo4j Update
  ↓ Company -[EXPANDED_INTO {evidence_id}]-> Healthcare
Twenty Update
  ↓ Company.industries += "Healthcare"
ClickUp Task
  ↓ "Research healthcare opportunity for X"
Buzz Notification
  ↓ @sales-team "New opportunity discovered"
```

**Integration Points:**
- Input: Market data, company lists, person lists
- Output: Discovered facts → Neo4j
- Trigger: Entity updates in Neo4j → Twenty
- Monitoring: Agent activity visible in Buzz

**Risk/Opportunity:**
- ✅ Perfectly aligned with Company Brain intelligence layer
- ✅ Evidence-first philosophy matches Neo4j knowledge graph
- ⚠️ Requires defining what to research (agent jobs queue)
- ⚠️ Needs scheduling + maintenance (rechecks)

---

### 2. Twenty CRM — Business Operations Layer (CP-032)

**Philosophy:** "Technical teams defining business objects as code, not clicking forms."

**Architecture:**
```
Objects & Fields (Code-First)
  ├── Standard: Company, Person, Deal, Opportunity
  ├── Custom: Any business entity (Venture, Market, Product)
  └── Relations: Foreign keys, linked objects

Views & Customization
  ├── Table views
  ├── Kanban views
  ├── Calendar views
  └── Custom layouts

Workflows & Automation
  ├── Triggers (on create, update, delete)
  ├── Actions (send email, create task, webhook)
  ├── Conditions (if/then logic)
  └── Schedules (recurring)

AI Agents (Native Integration)
  └── Conversational + autonomous

Database (PostgreSQL + Redis + BullMQ)
  └── ACID transactions + job queue

APIs (GraphQL + REST)
  └── Webhooks for external systems
```

**What makes it unique:**
- Define business objects as code (version control compatible)
- Multi-tenant ready (workspace isolation)
- RBAC built-in (role-based access control)
- Audit logs for compliance
- Workflow automation without coding
- Native agent integration points

**Role in Company Brain:**
- System of record for business entities
- Companies, people, deals, opportunities
- Venture-specific custom objects
- Workflow automation (deal won → onboarding)
- Audit trail (compliance + reporting)

**Example workflow:**
```
Comp AI discovers fact
  ↓ Webhook to Twenty
Company record updated
  ↓ industries: ["Healthcare"]
Workflow trigger
  ↓ "Healthcare industry" → create opportunity
Opportunity created
  ↓ Webhook to ClickUp
ClickUp project auto-created
  ↓ "Evaluate healthcare market for LT-005"
```

**Integration Points:**
- Input: Comp AI discoveries (webhooks)
- Input: ClickUp task completions (webhooks)
- Output: Deal updates → ClickUp projects
- Output: Company/person changes → Neo4j
- Monitoring: Dashboard showing pipeline health

**Risk/Opportunity:**
- ✅ Programmable objects match venture customization needs
- ✅ Workflow automation can create work
- ✅ GraphQL API integrates cleanly with Neo4j
- ⚠️ RBAC complexity (who sees what data)
- ⚠️ Requires defining data model for each venture type

---

### 3. ClickUp (Existing) — Execution Layer (CP-033)

**Philosophy:** "Everything is a task with relationships, priorities, and accountability."

**Architecture:**
```
Hierarchy
  Workspace
    └── Space
         └── Folder
              └── List
                   └── Task
                        ├── Subtask
                        ├── Checklists
                        └── Dependencies

Metadata
  ├── Assignee (person or agent)
  ├── Status (Backlog → Todo → In Progress → Review → Done)
  ├── Priority (Urgent, High, Normal, Low)
  ├── Due Date & Time Tracking
  ├── Custom Fields
  ├── Relationships (blocks, blocked_by, related_to)
  └── Comments & Attachments

Automation
  ├── Workflows (if/then rules)
  ├── Automations (on trigger, do action)
  ├── Recurring tasks
  └── Forms (for intake)

APIs
  ├── REST
  ├── Webhooks (2-way sync)
  └── Custom fields
```

**What makes it unique:**
- Hierarchical structure (space → folder → list → task)
- Flexible custom fields (per list or global)
- Time tracking built-in
- Dependency tracking (task B blocks task A)
- Automation without code
- 2-way webhooks (accepts + sends events)

**Role in Company Brain:**
- Accountability surface (who does what by when)
- Work generation (from ClickUp, Twenty, Buzz)
- Progress tracking (venture readiness, adoption pipeline)
- Dependency management (what blocks what)
- Team visibility (dashboard, workload, deadlines)

**Example workflow:**
```
Twenty deal won
  ↓ Webhook to ClickUp
Onboarding project auto-created
  ├── Task: Implementation planning
  ├── Task: Training schedule
  ├── Task: Deployment
  └── Task: Follow-up (dependent on Deployment)

Repository evaluated as TRIAL
  ↓ ClickUp project auto-created
  ├── Sandbox testing (Week 1)
  ├── Benchmark performance (Week 2)
  ├── Security review (Week 3)
  ├── Team evaluation (Week 4)
  └── Decision (dependent on all reviews)

Agent assigned to task
  ↓ Executes work
  ↓ Updates ClickUp with results
  ↓ Marks task complete
  ↓ Triggers next phase
```

**Integration Points:**
- Input: Twenty automations (new deals → projects)
- Input: Repository Intelligence (disposition → adoption project)
- Input: Buzz decisions (action items → tasks)
- Output: Task completion → Neo4j (venture progress)
- Output: Assignments → Agent task queue
- Monitoring: Dashboard (velocity, blockers, workload)

**Risk/Opportunity:**
- ✅ Already deployed and operational
- ✅ Excellent for human accountability
- ✅ Strong webhook system for 2-way sync
- ⚠️ Not a knowledge graph (don't use for business logic)
- ⚠️ Needs clear task → capability mapping

---

## COMPARISON TABLE

| Aspect | Comp AI CRM | Twenty | ClickUp |
|--------|------------|--------|---------|
| **Purpose** | Research + Evidence | Business Entities | Work Execution |
| **Owner** | Intelligence | Business Ops | Execution |
| **Primary User** | Agents | Business teams | Everyone (execution) |
| **Data Model** | Evidence ledger | Custom objects | Tasks + hierarchy |
| **Customization** | Tool definitions | Code-first objects | Custom fields |
| **Automation** | Agent jobs | Workflows | Automations |
| **Real-time** | No (batch agent runs) | Yes (webhooks) | Yes (webhooks) |
| **Scalability** | 100K records | 1M+ records | 100K+ tasks |
| **Cost** | Open-source | Open-source | SaaS (paid) |

---

## INTEGRATION PATTERNS

### Pattern 1: Discovery → Operations → Execution

```
Comp AI discovers fact
  ↓ (evidence recorded in PostgreSQL)
Neo4j webhook receives update
  ↓ (relationship added)
Twenty webhook receives update
  ↓ (company custom field updated)
Twenty workflow triggered
  ↓ (if new industry, create opportunity)
ClickUp webhook receives new deal
  ↓ (create onboarding project)
Team sees work
  ↓ (assigned to sales agent)
```

### Pattern 2: Repository Intelligence → Adoption Project

```
Repo disposition decided in Buzz
  ↓ (humans + repo-advisor approve)
Automation creates ClickUp project
  ├── Sandbox test task (due Sep 13)
  ├── Benchmark task (due Sep 15)
  ├── Security review (due Sep 17)
  ├── Team evaluation (due Sep 19)
  └── Final decision (due Sep 20)

Each task:
  ├── Assigned to appropriate agent/person
  ├── Relates to Neo4j repo entity
  ├── Updates ClickUp with results
  └── Triggers next phase

Result:
  ├── Full audit trail in ClickUp
  ├── Decisions traceable in Neo4j
  ├── Work tracked in real-time
  └── Can pause/resume adoption
```

### Pattern 3: Agents Operating Across Systems

```
repo-adoption-agent
  ├── Reads ClickUp task: "Sandbox test trycompai/crm"
  ├── Reads Neo4j context: repo capabilities, venue needs
  ├── Reads Twenty: relevant deals in progress
  ├── Executes sandbox setup
  ├── Posts progress to Buzz #repo-adoption-pipeline
  ├── Uploads benchmark report to ClickUp
  ├── Updates ClickUp task status
  └── Triggers next phase automation
```

---

## PHASE 2 DEPLOYMENT ORDER

**Why this sequence:**

1. **Comp AI CRM first** (simpler, isolated agent)
   - Deploy in Week 1 (Oct 1-7)
   - Configure research jobs
   - Wire webhooks to Twenty
   - Verify evidence recording

2. **Twenty second** (builds on Comp AI)
   - Deploy in Week 2 (Oct 8-14)
   - Create objects + custom fields
   - Wire Twenty ↔ ClickUp sync
   - Test deal workflows

3. **Full integration third** (requires both)
   - Week 3 (Oct 15-21)
   - Cross-system automations
   - Agent task queues
   - Unified dashboards

---

## EVALUATION CHECKLIST (Before Phase 2)

### Comp AI CRM
- [ ] Clone + explore architecture
- [ ] Understand agent job queue model
- [ ] Define what to research (companies? people? markets?)
- [ ] Review evidence ledger schema
- [ ] Plan webhook integration to Twenty
- [ ] Decide: self-hosted or managed?

### Twenty
- [ ] Clone + explore object model
- [ ] Define custom objects for ventures
- [ ] Plan automation workflows
- [ ] Review API + webhook capabilities
- [ ] Decide: Vercel hosting or self-hosted?
- [ ] Plan RBAC strategy

### Integration Points
- [ ] Comp AI → Twenty webhooks
- [ ] Twenty → ClickUp webhooks
- [ ] Twenty ↔ Neo4j sync
- [ ] Repository Intelligence → ClickUp projects
- [ ] Buzz → Task creation automation

---

## DECISION: NEXT STEPS

**Immediate (This Week):**
1. Clone both repositories
2. Run locally to see UI/UX
3. Identify deployment blockers
4. Assign Phase 2 team

**Week of Oct 1:**
1. Deploy Comp AI CRM
2. Deploy Twenty
3. Wire first webhook
4. Test end-to-end flow on 1 example

**Status:** Ready to proceed with Phase 2

---

**This is not a CRM comparison. This is architectural integration planning.**

Each system serves a specific purpose in Company Brain. The magic is in how they synchronize.

