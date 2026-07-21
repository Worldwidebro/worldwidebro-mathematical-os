# Registries Mapping: How All Registries Connect to OS & Ventures

**Date:** 2026-07-20  
**Purpose:** Show how all registries (tools, MCPs, capabilities, ventures, repos) fit into WORLDWIDEBRO-OS

---

## Registry Hierarchy

```
REGISTRIES/ (Single Source of Truth)
├── tools-registry.yaml (22 tools + services + agents)
├── mcp-servers/ (25+ MCPs: Stripe, GitHub, Slack, etc.)
├── capability_vocabulary.json (25 canonical capabilities)
├── ventures.yaml (712 ventures + status + revenue)
├── organizations.yaml (Holding + 6 OPCOs)
├── agents.yaml (3 core + 50+ specialized agents)
├── repositories.yaml (1,639 repos + capabilities)
├── models.yaml (Claude, Ollama, Colibri, exo)
├── prompts.yaml (all system prompts)
├── workflows.yaml (n8n + Zapier automations)
└── data-sources.yaml (all integrations)

        ↓ FEEDS INTO ↓

AI-PLATFORM/
├── Uses: agents.yaml → agent instantiation
├── Uses: models.yaml → LiteLLM routing
├── Uses: prompts.yaml → agent instructions

KNOWLEDGE-OS/
├── Uses: capability_vocabulary.json → capability graph
├── Uses: repositories.yaml → repo matching

VENTURE-FACTORY/
├── Uses: ventures.yaml → spawn new ventures
├── Uses: organizations.yaml → set org structure
├── Uses: agents.yaml → assign CEO, CTO, CFO
├── Uses: capabilities → new venture needs
├── Uses: repositories.yaml → assign repos

GROWTH-OS/
├── Uses: ventures.yaml → portfolio dashboard
├── Uses: workflows.yaml → lead capture + customer flows
├── Uses: data-sources.yaml → integrations

TECHNOLOGY/
├── Uses: tools-registry.yaml → health monitoring
├── Uses: mcp-servers/ → integration management
├── Uses: workflows.yaml → automation pipelines

        ↓ ALL 712 VENTURES INHERIT ↓

Each Venture Gets
├── Status + MRR + runway (from ventures.yaml)
├── Assigned agents (from agents.yaml)
├── Assigned repos (from repositories.yaml)
├── Available capabilities (from capability_vocabulary.json)
├── Access to all tools (from tools-registry.yaml)
├── Access to all MCPs (from mcp-servers/)
├── Assigned workflows (from workflows.yaml)
└── Model access (from models.yaml)
```

---

## Registry 1: tools-registry.yaml

**What:** 22 tools + services (Repomix, Serena, LiteLLM, Ollama, Prometheus, Grafana, etc.)  
**Who uses:** All ventures, Hermes, health checker  
**Updates:** Weekly

**How it flows:**
```
tools-registry.yaml
    ↓
check-tools.sh reads it
    ↓
"Is repomix installed? Is Ollama running?"
    ↓
All ventures inherit: "We can use these 22 tools"
```

---

## Registry 2: mcp-servers/

**What:** 25+ MCP integrations (Stripe, GitHub, Slack, Supabase, etc.)  
**Who uses:** All ventures (for third-party APIs), agents  
**Updates:** When new MCP added

**How it flows:**
```
mcp-servers/stripe.mcp.json
    ↓
Venture CFO agent needs to process payment
    ↓
Hermes says: "Use Stripe MCP"
    ↓
Venture calls Stripe → creates charge
```

---

## Registry 3: capability_vocabulary.json

**What:** 25 canonical capabilities (Estimation, Risk Score, Payment, Invoicing, etc.)  
**Who uses:** Venture requirements, repo matching, agent assignments  
**Updates:** Quarterly

**How it flows:**
```
capability_vocabulary.json
├── CON (Construction) needs: Estimation, Lead Capture, Invoicing
├── STA (Staffing) needs: Candidate Matching, Placement, Availability
├── FIN (Finance) needs: Risk Score, Position Sizing, Reconciliation
    ↓
Each venture looks up: "What capabilities do I need?"
    ↓
VENTURE-FACTORY assigns repos + agents to match
```

---

## Registry 4: ventures.yaml

**What:** 712 ventures (status, stage, sector, MRR, runway, assigned agents)  
**Who uses:** Dashboard, decision-making, resource allocation  
**Updates:** Real-time (status changes constantly)

**How it flows:**
```
ventures.yaml
├── CON-001: Active, MRR=$5K, runway=12 months
├── CON-002: Building, MRR=$0, runway=8 months
└── ... (710 more)
    ↓
CEO dashboard reads it
    ↓
"Which 9 ventures are active? What's revenue? Who's at risk?"
    ↓
Hermes reads it
    ↓
"Allocate capital per priority + runway"
```

---

## Registry 5: organizations.yaml

**What:** Holding + 6 OPCOs + org hierarchy  
**Who uses:** Governance, reporting, authority structure  
**Updates:** Rarely (quarterly org changes)

**How it flows:**
```
organizations.yaml
├── Worldwidebro Holdings
    ├── CON (Construction, 120 ventures)
    ├── STA (Staffing, 95 ventures)
    ├── RE (Real Estate, 110 ventures)
    └── ... (3 more OPCOs)
    ↓
Decision authority flows down
    ↓
"This decision affects STA → route through STA head"
```

---

## Registry 6: agents.yaml

**What:** 3 core agents + 50+ specialized (CEO, CTO, CFO, Hermes, etc.)  
**Who uses:** VENTURE-FACTORY, task routing, decision authority  
**Updates:** Weekly (new agents rare)

**How it flows:**
```
agents.yaml
├── AG-CEO: decision-making, strategy
├── AG-CTO: architecture, technology
├── AG-CFO: finance, capital allocation
├── HERMES: decision routing by amount + irreversibility
    ↓
New venture created
    ↓
VENTURE-FACTORY assigns: CEO, CTO, CFO to this venture
    ↓
Venture inherits these 3 agents automatically
```

---

## Registry 7: repositories.yaml

**What:** 1,639 repositories + what capabilities they implement  
**Who uses:** Code reuse, venture capability matching, Repomix packaging  
**Updates:** Weekly (new repos, capability updates)

**How it flows:**
```
repositories.yaml
├── stripe-integration: implements Payment, Invoicing
├── candidate-matcher: implements Candidate Matching
├── risk-model: implements Risk Score
    ↓
New venture: "I need Estimation capability"
    ↓
VENTURE-FACTORY queries repositories.yaml
    ↓
"stripe-integration implements Payment → assign it"
    ↓
Venture gets repo access + Repomix packages it
```

---

## Registry 8: models.yaml

**What:** All LLMs available (Claude Opus, Ollama qwen2.5, Colibri, exo)  
**Who uses:** LiteLLM router, agent model selection  
**Updates:** When new model added

**How it flows:**
```
models.yaml
├── claude-opus-4-8: cloud, $0.015/1K, reasoning
├── qwen2.5:32b: local, $0, reasoning
├── qwen3:8b: local, $0, reasoning
    ↓
Agent needs to reason about venture strategy
    ↓
LiteLLM reads models.yaml
    ↓
"Which model? Claude is best but expensive"
    ↓
"Can use local qwen2.5 first, fallback to Claude"
```

---

## Registry 9: prompts.yaml

**What:** All system prompts (CEO prompt, Hermes reasoning, task instructions)  
**Who uses:** Agents when executing work  
**Updates:** Weekly (prompt optimization)

**How it flows:**
```
prompts.yaml
├── CEO Agent System Prompt
├── Hermes Decision Router Prompt
├── Task: estimate-job Prompt
    ↓
Agent AG-CEO starts executing
    ↓
reads: prompts.yaml[CEO-001]
    ↓
Follows instructions in prompt
    ↓
Makes strategic decision
```

---

## Registry 10: workflows.yaml

**What:** n8n + Zapier automations (venture provisioning, payment processing, lead capture)  
**Who uses:** Task automation, event triggering  
**Updates:** Weekly (new workflows)

**How it flows:**
```
workflows.yaml
├── Venture Provisioning: triggers on new_venture_created
├── Payment Processing: triggers on payment_received
├── Lead Capture: triggers on form_submission
    ↓
Event happens: "New venture created"
    ↓
VENTURE-FACTORY reads workflows.yaml[provisioning]
    ↓
Executes: create_supabase_project + create_n8n_workflow + assign_agents
```

---

## Registry 11: data-sources.yaml

**What:** All external integrations (Google Sheets, Supabase, n8n, Salesforce, etc.)  
**Who uses:** Data pipelines, integrations, dashboard data sources  
**Updates:** When new integration added

**How it flows:**
```
data-sources.yaml
├── supabase: operational database
├── qdrant: vector search
├── stripe: payment data
├── salesforce: CRM data
    ↓
Dashboard needs: "Show revenue this week"
    ↓
Queries data-sources.yaml[stripe]
    ↓
Fetches: all transactions from Stripe
    ↓
Renders: revenue metric
```

---

## The Complete Flow

```
EXECUTIVE SETS PRIORITY
    ↓
"Prioritize revenue ventures this quarter"
    ↓
DIRECTIVE CREATED
    ↓
"Update REVENUE-PRIORITY-DIRECTIVE"
    ↓
REGISTRY UPDATED
    ↓
ventures.yaml: mark high-revenue as P0
    ↓
ALL 712 VENTURES INHERIT
    ↓
Each venture reads: "I'm priority" or "I'm secondary"
    ↓
Agents execute accordingly
```

---

## How to Add to a Registry

### Add a new tool:
1. Edit: `registries/tools-registry.yaml`
2. Add entry with tool_id, name, health_check, used_by
3. Test: `./scripts/check-tools.sh --category <category>`
4. Done: all ventures inherit it

### Add a new capability:
1. Edit: `registries/capability_vocabulary.json`
2. Add with name, domain, repos that implement it
3. Test: Query knowledge graph for coverage
4. Done: ventures can see it in their requirements

### Create new workflow:
1. Edit: `registries/workflows.yaml`
2. Add workflow with trigger + actions
3. Import to n8n
4. Done: automation runs

---

## Navigation

| Need | Registry | Location |
|---|---|---|
| List all tools? | tools-registry.yaml | `registries/` |
| Check MCP availability? | mcp-servers/ | `registries/` |
| See all capabilities? | capability_vocabulary.json | `registries/` |
| Check venture health? | ventures.yaml | `registries/` |
| See agent assignments? | agents.yaml | `registries/` |
| Which repo implements X? | repositories.yaml | `registries/` |
| Pick best model? | models.yaml | `registries/` |
| What prompts exist? | prompts.yaml | `registries/` |
| What workflows run? | workflows.yaml | `registries/` |

---

*All registries live in `WORLDWIDEBRO-OS/08-DATA/registries/`. Each registry feeds into specific OS layers. All 712 ventures inherit changes to any registry.*
