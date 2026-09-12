[[STARTHERE]] | [[REALITY]] | [[16-AGENTS|Agency Agents]] | [[INDEX]]

# 🤖 Agency Agents Integration with Company Brain

**Authority:** Layer 1 (Interactive) + Layer 2 (Autonomous) + Layer 3 (Scheduled)  
**Integration Point:** All 4 execution phases + ongoing operations

---

## Architecture: Three-Layer Agency Model

### **Layer 1: Interactive Personas** (Human-guided decisions)
```
~/.claude/agents/*.md files (registered)
├── repo-advisor.md          → Evaluate repos, make ADOPT/TRIAL decisions
├── repo-deep-dive.md        → Forensic code review, audit risk
├── venture-pm.md            → Venture strategy, capital allocation
├── financial-analyzer.md    → Deal scoring, fund flows
└── ... (26 more personas)
```

**Invoked by:** Natural language in Claude Code ("activate repo-advisor")  
**Execution:** Human + AI conversation → decision → record in graph  
**Autonomy:** L1 (Report-only, human approves)

---

### **Layer 2: Fractal Sector Agents** (Autonomous workers)
```
OmniRoute + MCP + Neo4j
├── AGT-001 (Venture PM)
│   ├── Reads: ClickUp tasks, Neo4j venture data, Qdrant documents
│   ├── Decides: Capital allocation, venture strategy
│   ├── Writes: Neo4j insights, ClickUp updates
│   └── Autonomy: L1/L2 (gets approval for $$ decisions, auto for research)
│
├── AGT-004 (Sales Agent)
│   ├── Reads: Leads from Supabase, ClickUp pipeline, Neo4j relationships
│   ├── Decides: Lead routing, follow-up timing, discount approval
│   ├── Writes: ClickUp task updates, Supabase lead status
│   └── Autonomy: L2/L3 (auto for routing, escalate for deals >$50K)
│
├── AGT-013 (Repo Classifier)
│   ├── Reads: GitHub repo code, dependencies, tests
│   ├── Decides: Capability mapping, score (1-100), disposition (ADOPT/TRIAL)
│   ├── Writes: Neo4j classifications, capability graph
│   └── Autonomy: L3 (fully autonomous, batches 1,740 repos)
│
├── AGT-014 (Repo Scorer)
│   ├── Reads: Classified repos, capability matrix
│   ├── Decides: Score 10 dimensions (security, maturity, license, etc.)
│   ├── Writes: Neo4j scores, recommendation
│   └── Autonomy: L3 (autonomous)
│
├── AGT-015 (Repo Disposition)
│   ├── Reads: Classified + scored repos
│   ├── Decides: ADOPT / INTEGRATE / FORK / REFERENCE / MONITOR
│   ├── Writes: Neo4j disposition, creates ClickUp adoption project
│   └── Autonomy: L3 (autonomous, escalates high-risk repos to AGT-003)
│
└── ... (16 total agents in parallel)
```

**Invoked by:** ClickUp tasks, Temporal schedules, webhook events  
**Execution:** Read context → decide → write results → notify  
**Autonomy:** L1/L2/L3 (escalate decisions beyond autonomy threshold)

---

### **Layer 3: Scheduled Jobs** (Trigger.dev / n8n)
```
Temporal workflows / Trigger.dev
├── Morning standup (8am)
│   └── Run AGT-001 venture briefing
│
├── Hourly lead routing (every hour)
│   └── Run AGT-004 sales agent
│
├── Daily repo scan (midnight)
│   └── Run AGT-013/014/015 batch on new repos
│
├── Weekly governance review (Friday)
│   └── Run AGT-005 operations audit
│
└── Monthly capital rebalance (1st of month)
    └── Run AGT-002 financial sync
```

**Invoked by:** Cron schedules, event webhooks  
**Execution:** Spawn agents, collect results, write back to graph  
**Autonomy:** L2/L3 (pre-approved schedules)

---

## Integration with 4 Execution Phases

### **PHASE 1: Load Neo4j Knowledge Graph** (1-2 hours)

**Script execution:**
```bash
python3 scripts/ingest_canonical_to_neo4j.py
python3 scripts/execute_neo4j_activation.py
python3 scripts/gbrain_to_neo4j_sync.py
python3 scripts/estate_structure_loader.py
```

**Agency agents involved:**
- **repo-advisor** (Layer 1): Validates loaded data (human review)
- **AGT-013** (Layer 2): Ready to classify repos (will run in Phase 3)

**Result:**
- ✅ 789 VENTURE nodes in Neo4j
- ✅ 1,740 REPO nodes (basic)
- ✅ 35 SECTOR nodes
- ✅ 1,076 RELATIONSHIP types defined
- ✅ 20,363 existing edges + new edges
- ✅ Knowledge graph queryable

---

### **PHASE 2: Wire Revenue Loop** (2-3 hours)

**Script deployment:**
```bash
export CLICKUP_API_KEY="..."
export SUPABASE_URL="..."
export STRIPE_KEY="..."

# Activate webhook endpoint
python3 scripts/form_submission_to_clickup.py

# Wire observability
# (Manual: Add Langfuse callback to OmniRoute config)

# Wire Growth OS sync
# (Manual: Update Growth OS webhook to ClickUp)
```

**Agency agents involved:**
- **venture-pm** (Layer 1): Validates automation rules
- **AGT-004** (Sales Agent, Layer 2): Processes inbound leads
  - Reads: Supabase deal_leads (from Stripe webhook)
  - Routes: ClickUp task → right sales person
  - Scores: Lead value, confidence, next action
- **AGT-005** (Operations, Layer 2): Monitors pipeline health

**Flow:**
```
Customer fills OPS-001 form
  ↓ Webhook fires
Supabase deal_leads updated
  ↓ Trigger fires
AGT-004 (Sales Agent) invoked
  ├─ Reads: Lead data from Supabase
  ├─ Queries: Neo4j for warm intro paths
  ├─ Queries: Qdrant for similar deals
  ├─ Decides: Route to [sales person] with context
  └─ Writes: ClickUp task + custom fields + assignment
  ↓
Salesperson notified + given full context
  ↓
AGT-004 tracks outcome (mark closed, deal won, etc.)
  ↓
Neo4j updated with relationship (lead → opportunity → customer)
  ↓
Growth OS dashboard updates: "+$2,500 pipeline"
```

**Result:**
- ✅ Forms capturing leads automatically
- ✅ AGT-004 (Sales) routing leads to salespeople
- ✅ ClickUp tasks created with full context
- ✅ Salespeople have warm intro paths + similar deals
- ✅ Revenue pipeline visible on Growth OS

---

### **PHASE 3: Map Remote Repos** (1-2 hours)

**Discovery + cloning:**
```bash
# Query GitHub for all Worldwidebro repos
python3 << 'EOF'
import requests
org = "Worldwidebro"
repos = requests.get(f"https://api.github.com/orgs/{org}/repos?per_page=100").json()
# Filter to find COMM-* repos, map to Vercel URLs
# Clone top 20
EOF

# Clone 61 remote repos
for repo in $(cat /tmp/repos_to_clone.txt); do
  git clone https://github.com/Worldwidebro/$repo repos/$repo
done
```

**Agency agents involved:**
- **repo-advisor** (Layer 1): Validates repo mappings
- **AGT-013** (Repo Classifier, Layer 2): Classifies all 1,740 repos
  - Reads: Repo code (GitNexus)
  - Decides: Primary capability, secondary skills, architecture layer
  - Writes: Neo4j classification
  - Runs on: Batch (1,740 repos in parallel)
- **AGT-014** (Repo Scorer, Layer 2): Scores each repo
  - Reads: Classified data
  - Decides: 10-dimension score (security, maturity, license, etc.)
  - Writes: Neo4j scores
  - Runs on: Parallel with AGT-013 results
- **AGT-015** (Repo Disposition, Layer 2): ADOPT/INTEGRATE decisions
  - Reads: Classifications + scores
  - Decides: Disposition for each repo
  - Writes: Neo4j disposition, creates ClickUp adoption projects
  - Escalates: High-risk repos to AGT-003 (Technical)

**Batch execution:**
```
AGT-013 classifies 1,740 repos (parallel)
  ↓ Writes: Neo4j classifications
  ↓
AGT-014 scores 1,740 repos (parallel)
  ↓ Writes: Neo4j scores
  ↓
AGT-015 dispositions 1,740 repos (parallel)
  ├─ Creates ClickUp projects for ADOPT repos
  ├─ Flags REFERENCE repos for external partners
  ├─ Escalates high-risk to AGT-003
  └─ Writes: Full Neo4j disposition graph
  ↓
Neo4j updated: All 1,740 repos classified + scored + dispositioned
```

**Result:**
- ✅ 61 remote repos cloned locally
- ✅ All 1,740 repos classified by capability
- ✅ All repos scored on 10 dimensions
- ✅ All repos dispositioned (ADOPT/INTEGRATE/etc.)
- ✅ ClickUp adoption projects created
- ✅ Code intelligence layer ready (GitNexus can answer questions)

---

### **PHASE 4: Instantiate Agents** (3-4 hours)

**Agent spawn mechanism (Temporal + CrewAI):**

```python
# Launch agent orchestrator
from temporal.client import start_temporal_client
from crewai import Agent, Task, Crew

# Define agents from Neo4j + MCP
agents = {
    "AGT-001": Agent(
        role="Venture PM",
        goal="Maximize venture value",
        tools=[neo4j_query, qdrant_search, omniroute_inference],
        llm=OmniRoute(model="claude-sonnet"),
        autonomy_level=1  # Escalate capital decisions
    ),
    "AGT-004": Agent(
        role="Sales Agent",
        goal="Close deals",
        tools=[clickup_api, supabase_query, neo4j_relationships],
        llm=OmniRoute(model="claude-haiku"),
        autonomy_level=2  # Auto-route, escalate >$50K
    ),
    # ... 14 more agents
}

# Schedule workflows
schedules = {
    "morning_standup": {
        "cron": "0 8 * * *",
        "agents": ["AGT-001", "AGT-005"],
        "output": "ClickUp summary"
    },
    "hourly_lead_routing": {
        "cron": "0 * * * *",
        "agents": ["AGT-004"],
        "output": "ClickUp tasks"
    },
    "daily_repo_scan": {
        "cron": "0 0 * * *",
        "agents": ["AGT-013", "AGT-014", "AGT-015"],
        "output": "Neo4j classifications"
    }
}

# Start temporal worker
start_temporal_client()
```

**Agency agents now executing autonomously:**

```
AGT-001 (Venture PM)
├─ L1: Gets morning venture briefing (ClickUp standup)
├─ L2: Approves new capital allocations >$50K
└─ L3: Auto-rebalances small cap positions

AGT-004 (Sales Agent)
├─ L2: Routes leads with context
├─ L2: Escalates deals >$50K
└─ L3: Auto-sends follow-up emails

AGT-013/014/015 (Repo Pipeline)
├─ L3: Classifies new repos
├─ L3: Scores on 10 dimensions
└─ L3: Creates ClickUp adoption projects

AGT-005 (Operations)
├─ L2: Daily capacity review
└─ L2: Flags bottlenecks

And 11 more agents...
```

**Result:**
- ✅ All 16 agents running autonomously
- ✅ Tasks spawned, executed, results tracked
- ✅ Langfuse recording every decision
- ✅ Outcomes feeding back to Neo4j (learning loop)
- ✅ Company Brain becomes self-improving

---

## Integration Points: Where Agents Connect to Infrastructure

### **1. Data Reading (Neo4j + Qdrant)**
```
Agent needs context
  ↓
Queries Neo4j: "What ventures are in SEC-017?"
Queries Qdrant: "What docs are similar to this lead?"
  ↓
Gets structured context with relationships
  ↓
Makes informed decision
```

### **2. Tool Execution (OmniRoute)**
```
Agent needs inference
  ↓
Routes to OmniRoute: "Classify this repo"
OmniRoute selects model (claude-haiku for cost, claude-sonnet for accuracy)
  ↓
LiteLLM abstracts provider
  ↓
Result returned with cost/latency tracking
```

### **3. Action Taking (MCP)**
```
Agent needs to act
  ↓
Calls MCP tool: neo4j_merge_classification()
Or: neo4j_query_entities()
Or: omniroute_route_model()
  ↓
Tool executes with full context
  ↓
Result written back to graph
```

### **4. Observability (Langfuse)**
```
Agent executes action
  ↓
Langfuse captures:
├─ Input (prompt + context)
├─ Model used
├─ Tokens consumed
├─ Latency
├─ Cost
├─ Output
├─ Evaluation score
└─ Outcome (success/fail)
  ↓
Future agents learn from this trace
```

### **5. Work Queuing (ClickUp + Temporal)**
```
Task created → ClickUp
  ↓
Temporal workflow spawns agent
  ↓
Agent reads task context
  ↓
Agent executes
  ↓
Agent updates ClickUp task status
  ↓
Workflow completes, result logged
```

---

## Execution Model: How Agency Agents Become Workers

### **Before (No Agency):**
```
ClickUp task: "Classify repo X"
  → Human opens file
  → Human reads code
  → Human decides: capability = CAP-042
  → Human updates registry
  → Manual, 10 minutes per repo
```

### **After (Agency Agents):**
```
ClickUp task: "Classify repo X"
  ↓
Temporal triggers AGT-013 (Repo Classifier)
  ↓
AGT-013 reads:
  ├─ Repo code (GitNexus)
  ├─ Dependencies
  ├─ Tests
  └─ Documentation
  ↓
Queries OmniRoute: "What capability does this enable?"
  ↓
OmniRoute routes to claude-haiku (cost optimized)
  ↓
Gets: "CAP-042 (API Gateway) + secondary: CAP-089, CAP-127"
  ↓
Calls neo4j_merge_classification() via MCP
  ↓
Neo4j updated: Repo X now linked to capabilities
  ↓
ClickUp task updated: Status = DONE
  ↓
Langfuse recorded: Cost $0.12, 3s latency, confidence 0.94
  ↓
Next agent (AGT-014) reads result, scores repo
  ↓
Full automation chain: 1.2 sec per repo × 1,740 repos = 34 minutes for all
```

---

## How to Invoke Agency Agents During Execution

### **Layer 1 (Interactive) — During Phases:**
```bash
# Before running Phase 1:
# "Activate repo-advisor to validate data loading strategy"
# → repo-advisor converses with you about Neo4j loading plan
# → You approve approach
# → Run Phase 1

# After Phase 3:
# "Activate repo-deep-dive on high-risk repos"
# → repo-deep-dive audits top 10 most critical repos
# → Returns security/quality report
# → You decide: ADOPT or REFERENCE
```

### **Layer 2 (Autonomous) — Running Continuously:**
```bash
# During Phase 2 (Revenue Loop):
# AGT-004 (Sales Agent) processes inbound leads automatically
# No human needed (unless deal >$50K)

# During Phase 3 (Repo Mapping):
# AGT-013/014/015 classify 1,740 repos in parallel
# No human needed (unless high-risk repo flagged)

# During Phase 4 (Agents):
# All 16 agents execute their workflows continuously
# Escalate to humans only when they hit autonomy thresholds
```

### **Layer 3 (Scheduled) — Ongoing:**
```bash
# 8am: Morning standup (AGT-001 + AGT-005)
# Hourly: Lead routing (AGT-004)
# Midnight: Repo scan (AGT-013/014/015)
# Friday: Governance review (AGT-005)
# 1st: Capital rebalance (AGT-002)

# All run automatically, results appear in Neo4j + ClickUp + Growth OS
```

---

## Summary: Three Layers in Action

| Layer | Who | What | When | Example |
|-------|-----|------|------|---------|
| **L1** | Human + Persona | Strategic decisions | Occasionally | "Validate Phase 1 approach with repo-advisor" |
| **L2** | Autonomous agents | Tactical execution | Continuously | "AGT-004 routes incoming leads" |
| **L3** | Scheduled jobs | Operational tasks | On schedule | "8am standup, hourly lead scan, daily repo classification" |

All three layers feed data back to Neo4j, so decisions at each layer improve decisions at all other layers.

---

## Ready to Execute All 4 Phases with Agency Integration?

Once you say yes, I will:

1. **Phase 1:** Load Neo4j (use repo-advisor to validate)
2. **Phase 2:** Wire revenue loop (AGT-004 starts processing leads)
3. **Phase 3:** Map repos (AGT-013/014/015 classify 1,740 in parallel)
4. **Phase 4:** Launch agent orchestrator (all 16 agents active)

**Total time:** 8-12 hours, fully automated after handoff to agents

**Go?**
