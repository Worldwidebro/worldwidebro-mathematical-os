[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Company Brain Architecture — Multi-Layer Platform Design

[[CLAUDE.md]] | [[STARTHERE]] | [[REALITY]]

**Scope:** Unified architecture integrating knowledge, intelligence, business operations, execution, and collaboration layers  
**Updated:** 2026-09-06  
**Authority:** CP-027 (Infrastructure Control Plane)  
**Vision:** Build a genuine agentic operating system, not a collection of tools

---

## ARCHITECTURE OVERVIEW

### The Five-Layer Model

```
                         COMPANY BRAIN PLATFORM
                              │
                   ┌──────────┴──────────┐
                   │                     │
              KNOWLEDGE               ACTION
                   │                     │
             ┌─────┴─────┐        ┌────┴─────┐
             ↓           ↓        ↓          ↓
           Neo4j       Qdrant   ClickUp     Buzz
             │           │        │          │
        Relationships  Semantic   Work      Collaboration
        Ontology       Search     Tasks     Agents
        Entities       RAG        Projects  Events
        Evidence       Memory     Goals     Rooms
             │           │        │          │
             └───────────┼────────┴──────────┘
                         ↓
                     AGENTS
                         │
                ┌────────┼────────┐
                ↓        ↓        ↓
             Comp AI   Twenty   GitHub
                │        │        │
             Research   CRM      Code
```

### The Six Systems

| Layer | System | Role | Authority |
|-------|--------|------|-----------|
| **Knowledge** | Neo4j + Qdrant | Relationships, entities, facts, semantic search, organizational knowledge | CP-013 (Knowledge Control Plane) |
| **Intelligence** | Comp AI CRM | Research, evidence, enrichment, identity resolution, agent memory | CP-031 (Intelligence Control Plane) — NEW |
| **Business** | Twenty | Companies, people, deals, custom objects, workflows, RBAC, dashboards | CP-032 (Business Operations Control Plane) — NEW |
| **Execution** | ClickUp | Goals, objectives, projects, tasks, dependencies, accountability, automation | CP-033 (Execution Control Plane) — NEW |
| **Collaboration** | Buzz | Rooms, agents, events, artifacts, automation, shared workspace, relay infrastructure | CP-028 (Collaboration Control Plane) |
| **Engineering** | GitHub | Source code, repositories, issues, pull requests, CI/CD | CP-034 (Engineering Control Plane) — NEW |

---

## SYSTEM RESPONSIBILITIES

### 1. KNOWLEDGE LAYER (Neo4j + Qdrant)

**What it holds:**
- Entity relationships (venture → capability → repository → technology)
- Organizational ontology (45+ relationship types)
- Evidence ledger (why facts are believed)
- Semantic embeddings (what concepts mean, in context)

**Who reads it:**
- All agents (for context assembly)
- All systems (for entity lookups)
- ClickUp (for understanding why tasks exist)
- Comp AI (for enrichment context)

**Who writes it:**
- Comp AI CRM (evidence + discovery)
- Twenty (company/person/deal updates)
- ClickUp (task → capability relationships)
- Buzz (event-based updates from collaboration)

**Example:** 
```
Company
  ├── NAME → "Acme Corp"
  ├── HEADQUARTER → San Francisco
  ├── EXPANDED_INTO → Healthcare (evidence: Comp AI research)
  ├── USES_TECH → Kubernetes (evidence: GitHub crawl)
  └── IS_OPPORTUNITY_FOR → LT-005 (Medical Courier venture)
```

### 2. INTELLIGENCE LAYER (Comp AI CRM)

**What it does:**
- Research companies, people, markets
- Maintain evidence ledger (not confidence scores, but actual evidence)
- Enrich entities with discovered facts
- Schedule rechecks for stale information
- Maintain durable agent sessions

**Agent pattern:**
```
research_agent
  ├── read_crm_history (what do we know)
  ├── search_crm (find related companies/people)
  ├── identify_contact (resolve entity)
  ├── research_person (discover new facts)
  ├── enrich_company (add evidence)
  ├── record_fact (evidence + recheck schedule)
  └── schedule_recheck (stay current)
```

**Canonical structure:**
- Research tasks (ongoing)
- Evidence records (immutable log)
- Entities (person, company, market, opportunity)
- Relationships (discovered through research)
- Rechecks (scheduled audits)

**Produces:**
- Discovered opportunities → Twenty
- Evidence → Neo4j
- Work → ClickUp
- Notifications → Buzz

**Example flow:**
```
Comp AI discovers:
"Company X expanded into healthcare"
  ↓
Record evidence:
timestamp, source, confidence (based on sources, not speculation)
  ↓
Neo4j update:
X -[EXPANDED_INTO {evidence_id}]-> Healthcare
  ↓
Twenty update:
Company.custom_field_industries += "Healthcare"
  ↓
ClickUp:
Create "Research healthcare opportunity for X" task
  ↓
Buzz notification:
@sales-team "Opportunity: X entering healthcare"
```

### 3. BUSINESS LAYER (Twenty)

**What it holds:**
- Companies (with custom fields for each venture type)
- People (contacts, hiring, partnerships)
- Deals (opportunities, pipeline stages)
- Custom objects (ventures, markets, products)
- Relationships (through foreign keys + workflow automation)
- Activities (calls, emails, meetings)

**Standard objects:**
```
Company
  ├── name
  ├── industry
  ├── size
  ├── headquarters
  ├── website
  ├── custom fields (venture-specific)
  └── relationships to people, deals, opportunities

Person
  ├── name, email, phone
  ├── company
  ├── role
  ├── custom fields
  └── relationships

Deal
  ├── name
  ├── amount
  ├── stage (prospecting, qualified, proposal, negotiating, won, lost)
  ├── company
  ├── contact
  ├── close date
  └── custom fields
```

**Canonical source of truth for:**
- Who we're talking to (people)
- Who we're selling to (companies)
- What we're selling (deals/opportunities)
- Custom business objects (ventures, markets, products)
- Workflow automation (triggers, actions)
- Permissions (who can see what)

**APIs:**
- GraphQL (primary)
- REST (webhooks for events)

**Produces:**
- ClickUp tasks (for every deal won, create onboarding project)
- Buzz notifications (deal updates)
- Neo4j relationships (company → industry, person → company)

### 4. EXECUTION LAYER (ClickUp)

**What it represents:**
```
GOAL
 ↓
OBJECTIVE
 ↓
PROJECT
 ↓
TASK
 ↓
SUBTASK
 ↓
ACTION
 ↓
RESULT
```

**Canonical structure:**
```
Workspace
 └── Space
      └── Folder
           └── List
                └── Task
                     ├── Subtask
                     ├── Assignee (Person or Agent)
                     ├── Status (Backlog, Todo, In Progress, Review, Done)
                     ├── Priority (Urgent, High, Normal, Low)
                     ├── Dependency (blocked_by, blocks, related_to)
                     ├── Custom Fields
                     ├── Checklist (for subtasks)
                     ├── Comments (decisions, context)
                     ├── Attachments (evidence, artifacts)
                     ├── Time Tracking (actual vs. estimated)
                     └── **Relationships** (to Neo4j entities)
                          ├── IMPLEMENTS → Capability
                          ├── BELONGS_TO → Venture
                          ├── PRODUCES → Artifact
                          ├── RELATES_TO → Repository
                          ├── RELATES_TO → Customer
                          └── ACHIEVES → Goal
```

**Key distinction:** ClickUp is NOT the knowledge source. ClickUp is the accountability/execution surface.

Every task should answer:
- **What?** (title + description)
- **Why?** (related Neo4j entities)
- **Who?** (assignee, team)
- **When?** (due date, timeline)
- **How?** (checklist, subtasks, attachments)
- **Status?** (current state)

**Task creation triggers:**
- Repository Intelligence: adoption project created
- Comp AI: research opportunity → sales task
- Twenty: deal won → onboarding project
- Buzz: team discussion → tracked action item
- Agent: discovers issue → remediation task

**Example task hierarchy:**

```
PROJECT: LT-005 Medical Courier MVP
├── FOLDER: Infrastructure
│   ├── LIST: Supabase Setup
│   │   ├── TASK: Wire Supabase
│   │   │   ├── SUBTASK: Create project
│   │   │   ├── SUBTASK: Configure auth
│   │   │   └── SUBTASK: Set up RLS
│   │   ├── TASK: Configure Stripe
│   │   │   ├── SUBTASK: API keys
│   │   │   └── SUBTASK: Webhook setup
│   │   └── [+] related Neo4j: LT-005 -REQUIRES-> Supabase
│   │                                              -REQUIRES-> Stripe
│
├── FOLDER: Deployment
│   ├── LIST: Production
│   │   ├── TASK: HTTPS + SSL
│   │   ├── TASK: Monitoring
│   │   └── TASK: Backup/restore
│
└── FOLDER: Quality
    ├── LIST: Testing
    ├── LIST: Security review
    └── LIST: Production validation
```

### 5. COLLABORATION LAYER (Buzz)

**What it enables:**
```
HUMAN ──┐
        ├──→ ROOM ──→ EVENTS ──→ RELAY ──→ EVENT STORE
AGENT ──┘           (published to channels/search)
```

**Key entities:**
- **Room:** Shared workspace (venture, project, team, agent)
- **Event:** Any action (message, decision, artifact, automation)
- **Agent:** First-class room member (has Nostr key, audit trail)
- **Artifact:** Attached files, decisions, code, proposals
- **Automation:** Triggered workflows

**Rooms for Company Brain:**
```
#company-brain-general        (meta-discussions)
#ventures                     (venture updates)
#repository-intelligence      (repo adoption pipeline)
#research-<venture>           (venture-specific research)
#sales-operations             (ClickUp + Twenty integration)
#engineering                  (GitHub + code discussions)
#agent-coordination           (agents coordinating on tasks)
#decisions                    (captured decision threads)
#learning                     (knowledge shared)
```

**Agent participation:**
```
Agent joins room
  ↓
Reads recent events (context assembly)
  ↓
Processes (reads messages, tasks, decisions)
  ↓
Executes (may call other systems)
  ↓
Publishes event (result, question, decision)
  ↓
Humans see in real-time
  ↓
Humans provide feedback in same thread
  ↓
Agent responds
  ↓
Full audit trail preserved
```

**Example: Repository adoption workflow in Buzz**

```
#repository-intelligence

Event 1: repo-adoption-agent
"Evaluating trycompai/crm for adoption
 Disposition: TRIAL
 Recommendation: Sandbox test
 Timeline: 2 weeks"

Event 2: repo-advisor persona
"Question: How does this compare to Twenty?
Both are CRM-adjacent but very different patterns."

Event 3: repo-adoption-agent
"Good question. Comp AI is agent-first with evidence ledger.
Twenty is programmable CRM with custom objects.
Actually complementary, not competitive.
Recommendation: TRIAL both independently, then decide overlap."

Event 4: human review
"Agreed. Creating ClickUp adoption projects for both."

Event 5: automation
"ClickUp project created: trycompai/crm adoption
ClickUp project created: twenty adoption
@repo-adoption-agent assigned to both"

[All events in Buzz, full thread history, linked to Neo4j decisions]
```

---

## SYSTEM SYNCHRONIZATION

### Knowledge Graph ↔ Business Operations

**Direction: Comp AI → Twenty**
```
Comp AI discovers fact
  ↓
Evidence recorded
  ↓
Neo4j updated
  ↓
Webhook to Twenty
  ↓
Company/person custom field updated
  ↓
(e.g., "Company X expanded into healthcare")
```

**Direction: Twenty → Neo4j**
```
Deal created in Twenty
  ↓
ClickUp project auto-created
  ↓
Neo4j relationship created
  ↓
(Deal connects Company → Opportunity → Venture)
```

### Business Operations ↔ Execution

**Direction: Twenty → ClickUp**
```
Deal won in Twenty
  ↓
Webhook to ClickUp
  ↓
Auto-create "Onboarding" project with:
  ├── Implementation tasks
  ├── Training schedule
  ├── Deployment checklist
  ├── Follow-up schedule
  └── (custom fields from Twenty)
```

**Direction: ClickUp → Twenty**
```
ClickUp task completed
  ↓
Deal stage updated
  ↓
(e.g., Onboarding complete → move to Active customer)
```

### Execution ↔ Collaboration

**Direction: ClickUp → Buzz**
```
New task assigned
  ↓
Buzz notification
  ↓
Agent joins room
  ↓
Agent discusses approach
  ↓
Human approves plan
  ↓
Agent executes
  ↓
Results posted to Buzz
  ↓
ClickUp task updated
```

**Direction: Buzz → ClickUp**
```
Team discussion in Buzz
  ↓
Consensus on action item
  ↓
"Create ClickUp task" automation
  ↓
Task created with discussion context
  ↓
Assigned to owner
```

### Collaboration ↔ Intelligence

**Direction: Buzz → Comp AI**
```
Research question in #research-venture
  ↓
Research agent reads thread
  ↓
Runs discovery
  ↓
Posts findings
  ↓
Evidence recorded in Comp AI
  ↓
Neo4j updated
```

### Repository Intelligence → Work

**Direction: Phase 4-6 dispositions → ClickUp projects**

```
Repository Intelligence identifies repo for adoption
  ↓
AGT-014 scores it (10 dimensions)
  ↓
AGT-015 recommends disposition (TRIAL/ADOPT/FORK/etc.)
  ↓
Buzz channel: #repository-intelligence
  ├─ Posts findings
  ├─ repo-advisor reviews
  ├─ repo-deep-dive deep-dives
  ├─ Humans approve
  ↓
Automation: Create ClickUp adoption project
  ├─ TRIAL phase:
  │   ├─ Sandbox environment
  │   ├─ Benchmark performance
  │   ├─ Security review
  │   ├─ Architecture assessment
  │   └─ Team evaluation
  ├─ ADOPT phase:
  │   ├─ Integration tasks
  │   ├─ Documentation
  │   ├─ Training
  │   └─ Production deployment
  ├─ FORK phase:
  │   ├─ Clone repository
  │   ├─ Customize for needs
  │   ├─ Internal security review
  │   └─ Deploy on infrastructure
  └─ Monitoring:
      └─ Weekly health checks (AGT-018)
```

---

## EXAMPLE: COMPLETE FLOW

### Scenario: Medical Courier Venture Opportunity Discovery

**Step 1: Research (Comp AI)**
```
Research Agent runs in background
  ↓
Discovers: "Healthcare dispatching market growing 15% YoY"
  ↓
Discovers: "Company X entering healthcare logistics"
  ↓
Records evidence:
  - Source: Crunchbase + their blog
  - Date: 2026-09-06
  - Confidence: High (multiple sources)
  ↓
Comp AI records facts:
  - Company X
  - ├── EXPANDED_INTO → Healthcare
  - └── USES_MARKET → Logistics Dispatching
```

**Step 2: Intelligence Update (Neo4j)**
```
Neo4j updates:
  Company X
  ├── INDUSTRY → Healthcare
  ├── MARKET → Logistics Dispatching (15% growth)
  ├── EXPANSION_DATE → 2026-09-06
  └── POTENTIAL_FOR → LT-005 Medical Courier
```

**Step 3: Business Operations (Twenty)**
```
Twenty webhook triggered
  ↓
Company X custom field updated:
  - industries: [Healthcare]
  - markets: [Logistics Dispatching]
  - growth_rate: [15% YoY]
```

**Step 4: Opportunity Creation (Twenty)**
```
Sales agent reviews findings
  ↓
Creates Deal in Twenty:
  - Company: Company X
  - Opportunity: "Logistics dispatching software"
  - Amount: $TBD
  - Stage: Prospecting
  - Next Step: Contact CTO
```

**Step 5: Execution Planning (ClickUp)**
```
Twenty webhook to ClickUp
  ↓
Auto-create project: "Company X - Dispatching Opportunity"
  ├── Sales Task: Contact CTO
  │   ├── RELATES_TO → Company (Twenty)
  │   ├── ACHIEVES → LT-005 validation
  │   └── Custom field: discovery_source = Comp AI
  ├── Research Task: Market analysis
  │   ├── Due date: Sep 13
  │   └── Assignee: market-research-agent
  ├── Product Task: Evaluate fit
  │   ├── Checklist: feature gap analysis
  │   └── Dependencies: market analysis
  └── Revenue tracking: potential $XXX
```

**Step 6: Collaboration (Buzz)**
```
#research-ventures channel

Message 1: research-agent
"Opportunity identified: Company X healthcare entry
Found via Crunchbase, confirmed via blog + LinkedIn
Market growth 15% YoY in healthcare logistics"

Message 2: sales-team
"Company X is already a customer? Let me check Twenty..."

Message 3: sales-agent
"Confirmed: Company X is existing customer (Small license)
CTO is John Doe (john@companyx.com)
Previous engagement: Jan 2026 trial"

Message 4: sales-team
"Perfect. I'll reach out about expansion. Creating ClickUp task."

Message 5: automation
"ClickUp task created: Reach out to Company X CTO about logistics
Assigned to @sales-team, due Sep 8"

Message 6: sales-team
"Done. Moving to #company-x-dispatching-opportunity"

```

**Step 7: Execution & Feedback (ClickUp + Buzz)**
```
ClickUp task "Evaluate fit for LT-005"
  ↓
market-research-agent runs analysis
  ↓
Uploads report to ClickUp
  ↓
Posts findings to #research-ventures:
  "Market analysis complete: 12 competitors, 60% TAM underserved"
  ↓
Team approves prioritization
  ↓
Task moves to "Done"
  ↓
Next project phase: "Product evaluation"
```

**Step 8: Knowledge Update**
```
All findings synced back to Neo4j:
  
Company X
  ├── MARKET_ANALYSIS → [report_artifact]
  ├── COMPETITIVE_INTENSITY → 12 competitors
  ├── TAM_ADDRESSABLE → 60%
  ├── OPPORTUNITY_STATUS → Qualified
  └── OPPORTUNITY_ASSIGNED_TO → LT-005 Medical Courier

LT-005
  ├── QUALIFIED_OPPORTUNITY → Company X
  ├── REVENUE_POTENTIAL → $XXX
  └── NEXT_ACTION → Product evaluation (due Sep 15)
```

**Result:** Complete closed-loop system
- Intelligence (Comp AI) → discovered opportunity
- Knowledge (Neo4j) → connected to venture
- Business (Twenty) → tracked as opportunity
- Execution (ClickUp) → scheduled work
- Collaboration (Buzz) → human-agent coordination

---

## CONTROL PLANES (UPDATED)

| CP # | Name | Systems | Authority |
|------|------|---------|-----------|
| CP-006 | Agent Control Plane | All agents + orchestration | [[Agents]] |
| CP-007 | Model Control Plane | OmniRoute + LiteLLM + model routing | [[Models]] |
| CP-013 | Knowledge Control Plane | Neo4j + Qdrant | [[Knowledge]] |
| CP-020 | Financial Control Plane | Cost tracking by model/provider | [[Finance]] |
| CP-027 | Infrastructure Control Plane | Databases, services, deployment | [[Infrastructure]] |
| CP-028 | Collaboration Control Plane | Buzz relay + rooms + events | [[Buzz]] |
| **CP-031** | **Intelligence Control Plane** | **Comp AI CRM** | **NEW: Research + evidence** |
| **CP-032** | **Business Operations Control Plane** | **Twenty** | **NEW: CRM + business entities** |
| **CP-033** | **Execution Control Plane** | **ClickUp** | **NEW: Tasks + projects + accountability** |
| **CP-034** | **Engineering Control Plane** | **GitHub** | **NEW: Repositories + code** |
| CP-029 | Observability | Langfuse + dashboards | [[Observability]] |

---

## REPOSITORY INTELLIGENCE INTEGRATION

### Phase 9 Output (Awesome Lists) → New Architecture

Instead of:
```
"904 repos analyzed, top 50 listed in Awesome registry"
```

Now:
```
904 repos analyzed
  ↓
Phase 4-6: Classified/scored/dispositioned
  ↓
Buzz collaboration with repo-advisor/repo-deep-dive
  ↓
Final dispositions reviewed
  ↓
[For each repo with disposition TRIAL/ADOPT/FORK]
  ├── Create ClickUp adoption project
  ├── Notify relevant team in Buzz
  ├── Record decision in Neo4j
  ├── Create company-brain/adoption/<repo-name> branch
  ├── Schedule weekly health check (AGT-018)
  └── [And this produces actual work, not just reports]
```

---

## IMPLEMENTATION ROADMAP

### Phase 1: Knowledge + Collaboration (Sep 6-26)
- ✅ Deploy Buzz (Week 1)
- ✅ Repository Intelligence System phases 4-6 with Buzz collaboration (Week 2-3)
- ✅ Connect Neo4j to Buzz (event sync)

### Phase 2: Intelligence (Oct 1-31)
- Deploy Comp AI CRM
- Wire research agents to feed Neo4j + Twenty
- Create research dashboards

### Phase 3: Business Operations (Nov 1-30)
- Deploy Twenty
- Set up company/person/deal objects
- Create Twenty ↔ ClickUp sync
- Set up RBAC + permissions

### Phase 4: Full Integration (Dec 1-31)
- Wire all 6 systems together
- Create cross-system automations
- Build unified dashboard
- Deploy to production

---

## SUCCESS CRITERIA

**You'll know it's working when:**

1. ✅ Comp AI discovers a fact → appears in Twenty within 15 minutes
2. ✅ Deal won in Twenty → ClickUp project auto-created
3. ✅ ClickUp task created → Buzz notification + agent joins room
4. ✅ Repo disposition decided in Buzz → ClickUp adoption project created automatically
5. ✅ Neo4j query returns context from all 5 systems (Twenty + Comp AI + ClickUp + Buzz + GitHub)
6. ✅ Agent reads ClickUp task, understands business context (via Neo4j), executes, updates task + Buzz
7. ✅ No duplicate effort: all 5 systems sync automatically, source of truth is clear

---

## KEY PRINCIPLES

1. **Boundaries Preserved**
   - Each system owns its domain
   - No monolithic mega-app
   - Sync through APIs + events

2. **ClickUp is NOT the Knowledge Graph**
   - ClickUp is the accountability surface
   - Neo4j is the relationship surface
   - Comp AI is the research surface

3. **Every System Feeds Neo4j**
   - Twenty company updates → Neo4j entity updates
   - Comp AI evidence → Neo4j relationships
   - ClickUp task completion → Neo4j fact: venture progress

4. **Agents Operate at the Sync Layer**
   - Not in one system exclusively
   - They read from all systems via APIs
   - They update multiple systems in one workflow

5. **Humans Use the System They Know Best**
   - Sales team works in Twenty/ClickUp/Buzz
   - Engineers work in GitHub/ClickUp/Buzz
   - Management reads dashboards (Neo4j + ClickUp)
   - All synchronized underneath

---

**This is Company Brain. Not a tool collection. A platform.**

