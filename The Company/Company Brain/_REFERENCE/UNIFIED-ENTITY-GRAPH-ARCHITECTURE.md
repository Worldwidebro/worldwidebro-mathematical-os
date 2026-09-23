# Unified Entity Graph Architecture (Phase 4 Integration)

**Authority:** CP-001 (Sovereign Operator)  
**Generated:** 2026-09-25  
**Phase:** 4 (Oct 15-21) — Observability & Pre-flight  
**Status:** SPECIFICATION (ready for Phase 4 integration)

---

## Core Principle

> A starred repository is not valuable because it is starred. Its value comes from what capability it provides, what it connects to, and **how close that use is to execution and revenue**.

---

## 1. The Unified Entity Model

```
                    COMPANY BRAIN
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     KNOWLEDGE        EXECUTION       GOVERNANCE
        │                │                │
    ┌───┴───┐       ┌───┴───┐       ┌───┴───┐
    │       │       │       │       │       │
  BASES  REGISTERS AGENTS  WORKFLOWS  DECISIONS
    │       │       │       │       │       │
    └───┬───┘       └───┬───┘       └───┬───┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                  KNOWLEDGE GRAPH
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    REPOSITORIES    MCPs              SKILLS
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
                    CAPABILITIES
                        │
                        ▼
                      TOOLS
                        │
                        ▼
                      VENTURES
                        │
                        ▼
                    CUSTOMERS
                        │
                        ▼
                    REVENUE
```

---

## 2. Entity Types & Lifecycle

### Repository Lifecycle
```
STARRED → DISCOVERED → CLASSIFIED → VERIFIED → MAPPED → TESTED → WATCH → PILOT → ADOPTED → INTEGRATED → PRODUCTION → REVENUE
```

| State       | Meaning                                      |
| ----------- | -------------------------------------------- |
| STARRED     | Found and saved                              |
| DISCOVERED  | Entered Company Brain registry               |
| CLASSIFIED  | Capability identified                        |
| VERIFIED    | Repository/source checked & working          |
| MAPPED      | Relationships to bases/ventures identified   |
| TESTED      | Pilot tested or evaluation complete          |
| WATCH       | Interesting, not yet tested                  |
| PILOT       | Currently being tested                       |
| ADOPTED     | Chosen for use in production                 |
| INTEGRATED  | Connected to system/workflow                 |
| PRODUCTION  | Operating in live system                     |
| RETIRED     | No longer used                               |

### Entity Representations

Each entity has **two canonical representations**:

1. **Markdown + WikiLinks** (human navigation)
2. **XML** (machine consumption)

Example:

```markdown
---
id: REPO-0042
type: repository
canonical_name: browser-use/jev-ultrafast
status: watch
---

# browser-use/jev-ultrafast

## Identity
- **Type:** Repository
- **ID:** REPO-0042
- **Status:** WATCH

## Capability
[[Browser Automation]]

## Company Brain Relationships
- Implements → [[CAP-001]]
- Enables → [[Skill — Browser Control]]
- Supports → [[MCP-0009]]
- Powers → [[LT-005 Medical Courier]]

## Revenue Path
Evaluation → Browser Automation Capability → Dispatch Workflow → HealthRoute Venture → Customer Delivery → Revenue

## Adoption Status
**Status:** WATCH (not tested)  
**Next:** Evaluation phase
```

Corresponding XML:

```xml
<repository id="REPO-0042">
    <name>browser-use/jev-ultrafast</name>
    <status>watch</status>
    <lifecycle_stage>tested</lifecycle_stage>
    <capabilities>
        <capability ref="CAP-001"/>
    </capabilities>
    <relationships>
        <relationship type="enables" ref="SKILL-0042"/>
        <relationship type="supports" ref="MCP-0009"/>
        <relationship type="powers" ref="VENTURE-LT-005"/>
    </relationships>
    <revenue_path>
        <step sequence="1">evaluation</step>
        <step sequence="2" ref="CAP-001">browser-automation</step>
        <step sequence="3" ref="WORKFLOW-001">dispatch</step>
        <step sequence="4" ref="VENTURE-LT-005">healthroute</step>
        <step sequence="5">customer-delivery</step>
        <step sequence="6">revenue</step>
    </revenue_path>
</repository>
```

---

## 3. Entity Types in Company Brain

### Tier 1: Strategy & Domains
- **Base** (B001-B500) — 50 control domains
- **Sector** (SEC-001-035) — Business domains
- **Venture** — Operating companies

### Tier 2: Capability Layer
- **Repository** — GitHub/external code
- **Capability** — What something enables
- **MCP** — Machine context protocol
- **Tool** — Discrete function
- **Skill** — Procedure/operational expertise

### Tier 3: Execution Layer
- **Agent** — Autonomous executor
- **Workflow** — Multi-step process
- **Task** — Discrete work unit
- **Decision** — Control point

### Tier 4: Outcome Layer
- **Customer** — Who we serve
- **Revenue** — Income attribution
- **Metric** — Measurement

---

## 4. Registry Family (Oct 15-21)

Create explicit registries by entity type:

```
_REGISTRIES/CANONICAL/
├── CBP-REGISTRY.yaml                   (500 bases, ACTIVE)
├── SECTOR-REGISTRY.yaml                (35 sectors)
├── VENTURE-REGISTRY.yaml               (789 ventures)
├── CAPABILITY-REGISTRY.yaml            (300+ capabilities)
├── REPOSITORY-REGISTRY.yaml            (starred repos)
├── MCP-REGISTRY.yaml                   (tools/MCPs)
├── SKILL-REGISTRY.yaml                 (procedures)
├── AGENT-REGISTRY.yaml                 (autonomous agents)
├── WORKFLOW-REGISTRY.yaml              (processes)
├── TOOL-REGISTRY.yaml                  (discrete functions)
├── CUSTOMER-REGISTRY.yaml              (buyers/users)
├── DECISION-REGISTRY.yaml              (control points)
└── RELATIONSHIP-REGISTRY.yaml          (graph edges)
```

---

## 5. Distance-to-Income Classification

Every repository, MCP, skill, and tool must answer:

```
Does this:
A. Directly produce revenue?
B. Enable a revenue-producing workflow?
C. Reduce operating cost?
D. Reduce execution time?
E. Improve reliability?
F. Provide strategic capability?
G. Merely provide interesting technology?
```

Example classification:

```yaml
REPO-0042:
  name: browser-use/jev-ultrafast
  economic_role: "enablement"
  revenue_path:
    - venture: LT-005
      workflow: dispatch
      capability: route-optimization
      service: delivery
      mechanism: per-delivery-fee
  distance_to_income: "3 steps" (repo → capability → workflow → revenue)
  revenue_multiplier: "high" (applies to all deliveries)
  confidence: "unverified" (requires testing)
```

This allows queries like:

> Show me technologies that can be deployed into revenue workflows this quarter.

Instead of:

> Show me my starred repositories.

---

## 6. Technology-to-Revenue Graph (Go-Live Roadmap)

```
                    STARRED REPOSITORY
                           │
                           ▼
                       CAPABILITY
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
           SKILL          MCP           TOOL
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                          AGENT
                           │
                           ▼
                        WORKFLOW
                           │
                           ▼
                         SYSTEM
                           │
                           ▼
                         VENTURE
                           │
                           ▼
                     PRODUCT/SERVICE
                           │
                           ▼
                        CUSTOMER
                           │
                           ▼
                       TRANSACTION
                           │
                           ▼
                         REVENUE
```

**Phase 4 Task:** Wire Phase 1-3 foundations into this graph so repositories → capabilities → workflows → ventures → revenue is fully connected.

---

## 7. Entity Card Representations

### Repository Card
```
┌─────────────────────────────────────┐
│ browser-use/jev-ultrafast           │
│ REPO-0042                           │
├─────────────────────────────────────┤
│ Capability                          │
│ [[CAP-001 | Browser Automation]]    │
│                                     │
│ Status: WATCH                       │
│ Adoption: Not Tested                │
│                                     │
│ Skills: 2                           │
│ MCPs: 1                             │
│ Tools: 5                            │
│                                     │
│ Revenue Distance: 3 steps           │
│ Distance: Evaluation Required       │
│                                     │
│ [Open] [Evaluate] [Test] [Adopt]    │
└─────────────────────────────────────┘
```

### Capability Card
```
┌─────────────────────────────────────┐
│ Browser Automation                  │
│ CAP-001                             │
├─────────────────────────────────────┤
│ Status: AVAILABLE                   │
│ Implementation: EXTERNAL (repo)     │
│                                     │
│ Used By: 3 Skills                   │
│ Powers: 2 MCPs                      │
│ Enables: 4 Workflows                │
│                                     │
│ Ventures:                           │
│ • [[LT-005 | HealthRoute]]          │
│ • [[OPS-001 | Staffing]]            │
│                                     │
│ Revenue: $4,500/mo                  │
│ (verified live)                     │
└─────────────────────────────────────┘
```

### Venture Card (Revenue)
```
┌─────────────────────────────────────┐
│ LT-005 | HealthRoute Courier        │
│ VENTURE-LT-005                      │
├─────────────────────────────────────┤
│ Base: [[B581 | Logistics]]          │
│ Agent: [[Dispatch Agent]]           │
│                                     │
│ Status: ACTIVE                      │
│ Revenue: $1,800/mo (verified)       │
│                                     │
│ Capabilities:                       │
│ • [[Route Optimization]]            │
│ • [[GPS Tracking]]                  │
│ • [[Driver Management]]             │
│                                     │
│ Technologies:                       │
│ ✓ [[REPO-0042]]                    │
│ ✓ [[MCP-0009]]                     │
│                                     │
│ Workflow: [[Dispatch Workflow]]     │
│ Customers: Healthcare Providers     │
└─────────────────────────────────────┘
```

---

## 8. Phase 4 Integration Tasks (Oct 15-21)

### Task 1: Create Registries (Oct 15-16)
- [ ] REPOSITORY-REGISTRY.yaml (map starred repos)
- [ ] MCP-REGISTRY.yaml (active MCPs)
- [ ] SKILL-REGISTRY.yaml (procedures)
- [ ] TOOL-REGISTRY.yaml (discrete tools)
- [ ] CAPABILITY-REGISTRY.yaml (expand: 300+ → map to repos)

### Task 2: Establish Relationships (Oct 17-18)
- [ ] RELATIONSHIP-REGISTRY.yaml (all edges)
- [ ] Map Repository → Capability
- [ ] Map Capability → Skill → MCP → Tool
- [ ] Map Tool → Agent → Workflow → Venture

### Task 3: Distance-to-Income Classification (Oct 19)
- [ ] Classify all 300+ capabilities by economic role
- [ ] Classify all starred repos by revenue path
- [ ] Identify quick wins (short distance → revenue)
- [ ] Prioritize evaluation/adoption queue

### Task 4: Dashboard Creation (Oct 20)
- [ ] Entity card templates (repo, capability, MCP, skill, venture, customer)
- [ ] Real-time registry indexes
- [ ] Revenue attribution (from Phase 2) + technology stack visualization
- [ ] "Distance to Income" heat map

### Task 5: Pre-flight Verification (Oct 21)
- [ ] All entities have ID + type + status
- [ ] All relationships bidirectional in graph
- [ ] Revenue paths traceable (venture → capabilities → repos)
- [ ] Dashboards showing live metrics
- [ ] Stakeholder sign-off

---

## 9. WikiLink Conventions (Standardized)

### Entity Links
```
[[REPO-0042]]           Entity by ID
[[CAP-001]]            Capability by ID
[[VENTURE-LT-005]]     Venture by ID
[[SKILL-0042]]         Skill by ID
[[MCP-0009]]           MCP by ID
[[BASE-251]]           Base by ID
[[AGENT-Dispatch]]     Agent by name
[[WORKFLOW-001]]       Workflow by ID
```

### Human-Readable Aliases
```
[[REPO-0042|browser-use JEV]]
[[VENTURE-LT-005|HealthRoute Courier]]
[[CAP-001|Browser Automation]]
[[BASE-251|Sales Pipeline]]
```

**Rule:** ID is canonical. Display name can change.

---

## 10. XML Schema Structure

Consistent structure across all entity types:

```xml
<entity type="[repository|mcp|skill|capability|...]" id="[ID]">
    <identity>
        <id>[canonical id]</id>
        <name>[human name]</name>
        <status>[lifecycle state]</status>
    </identity>
    
    <purpose>
        [What this entity does]
    </purpose>
    
    <relationships>
        <relationship type="implements" ref="[CAP-001]"/>
        <relationship type="enables" ref="[SKILL-042]"/>
        <relationship type="powers" ref="[VENTURE-LT-005]"/>
    </relationships>
    
    <revenue_path>
        [Steps from this entity to customer revenue]
    </revenue_path>
    
    <metrics>
        [Key performance indicators]
    </metrics>
    
    <lifecycle_evidence>
        [What proves this entity's status]
    </lifecycle_evidence>
</entity>
```

---

## 11. Expected Outcome (Oct 22 Go-Live)

**What's Connected:**
- ✅ 500 Bases (B001-B500) — control domains
- ✅ 50 Domain Agents — autonomous executors
- ✅ 789 Ventures — revenue-generating companies
- 🔄 300+ Capabilities — what we can do
- 🔄 300+ Repositories — how we do it
- 🔄 20+ MCPs — tools that enable execution
- 🔄 50+ Skills — procedures
- 🔄 200+ Tools — discrete functions

**What's Visible:**
- Entity dashboards (repo → capability → venture → revenue)
- Distance-to-income heat map
- Real-time revenue attribution
- Technology adoption pipeline
- Capability-to-venture mapping

**What's Executable:**
- All repositories classified by economic role
- Starred repos mapped to revenue workflows
- MCPs wired to capabilities and agents
- Skills assigned to workflows
- Full technology stack → customer revenue path visible

---

## 12. Success Criteria (Oct 22)

- ✅ 100% of bases wired to agents + workflows
- ✅ 100% of ventures connected to capabilities + repositories
- ✅ All repositories classified (lifecycle state + economic role)
- ✅ Revenue path traceable: repo → capability → workflow → customer → $
- ✅ Live dashboard showing technology → revenue pipeline
- ✅ Automated distance-to-income scoring
- ✅ Stakeholder sign-off on unified graph

---

**Reference:** [[BASE-WORKFLOW-WIRING|_REFERENCE/BASE-WORKFLOW-WIRING.md]]  
**Execution:** Phase 4 (Oct 15-21) — Observability & Pre-flight  
**Go-Live:** October 22, 2026 ✅
