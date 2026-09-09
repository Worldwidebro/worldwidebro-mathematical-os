# Wiki Link Updates — Agent OS Business Responsibility Framework

**Authority:** CP-006 (Agents) + CP-027 (Infrastructure)  
**Scope:** Map new Agent OS business function architecture to existing wiki structure  
**Action:** Update 40+ docs to reflect 33-function business responsibility model

---

## CRITICAL PATH UPDATES (Sep 12-19)

### 🔴 TIER 1: Foundation Docs (MUST UPDATE)

#### 1. **START-HERE-AGENTS.md**
**Current:** Lists 16 agents individually  
**Update:** Add new framework: "Agents organized by Business Responsibility, not agent type"

Add section:
```markdown
## Agent OS Business Responsibility Framework

Rather than "16 agents," think: "33 business functions + 1 orchestrator"

### 1. Strategy & Leadership (CEO, Strategy, Research, Decision agents)
- Analyze markets
- Identify opportunities
- OKR planning
- Strategic planning
- Decision support

### 2. Research & Intelligence (Digital Librarian + Research agents)
- Web research
- Competitor research
- Market research
- Source verification
- Evidence extraction

### 3. Product (Product agents)
...
```

---

#### 2. **AGENTS.md**
**Current:** "16 agents listed by ID"  
**Update:** Reorganize by business function first, then agent

```markdown
# AGENTS — Business Responsibility Framework

## Strategy & Leadership Layer
- **AGT-001** (Venture PM) → Provides: Strategic planning, capital decisions, risk analysis
- **CEO Agent** (future) → Provides: Quarterly planning, board reporting, M&A strategy

## Sales Layer
- **AGT-004** (Sales Agent) → Provides: Lead qualification, account research, proposal generation
- **SDR Agent** (future) → Provides: Outreach personalization, email generation, follow-up
- **AE Agent** (future) → Provides: Deal management, objection handling, forecasting

## Research & Intelligence Layer
- **AGT-020** (Research Librarian) → Provides: Market research, source verification, knowledge synthesis
- **AGT-021** (Venture Librarian) → Provides: Venture research, capability gap analysis
- **AGT-022** (Integration Librarian) → Provides: Integration scoring, recommendations

## Operations Layer
- **AGT-005** (Operations) → Provides: Process workflows, dispatch, resource allocation
...
```

---

#### 3. **14-CAPABILITIES/README.md**
**Current:** Lists capabilities by ID  
**Update:** Add business function mapping

Add section after capabilities list:
```markdown
## Capabilities → Business Functions Mapping

Each capability supports specific business functions:

CAP-042 (Market Research)
  ├─ Supports: Strategy & Leadership → Market analysis
  ├─ Supports: Sales → Account research
  ├─ Supports: Product → Market opportunity identification
  └─ Provided by: AGT-020, AGT-021, external research tools

CAP-043 (Lead Qualification)
  ├─ Supports: Sales → Lead scoring
  ├─ Supports: Operations → Lead routing
  └─ Provided by: AGT-004, Callcenter OS
```

---

#### 4. **19-ORCHESTRATION/README.md**
**Current:** "Orchestration infrastructure"  
**Update:** Add business function routing diagram

```markdown
# Orchestration — Business Function Router

The orchestrator maps Business Function → Responsibility → Capability → Agent:

## Examples

### Function: Sales
Responsibilities:
  - find_prospects
  - qualify_leads
  - generate_proposals
  - close_deals
  
Capabilities Required:
  - Lead research
  - Lead scoring
  - Communication
  - Deal management

Agents:
  - AGT-020 (research)
  - AGT-004 (sales)
  - Future: SDR Agent, AE Agent

### Function: Operations
Responsibilities:
  - process_workflows
  - schedule_work
  - dispatch
  - route_optimization

Capabilities Required:
  - Scheduling
  - Route optimization
  - Resource allocation

Agents:
  - AGT-005 (operations)
  - Future: Dispatcher Agent, Scheduler Agent
```

---

### 🟡 TIER 2: Domain READMEs (UPDATE WITH SECTIONS)

Each domain 00-50 needs a new section: "**Business Functions This Domain Supports**"

#### 00-CONSTITUTION/README.md
Add:
```markdown
## Business Functions This Domain Supports

- Strategy & Leadership (defines constitution)
- Compliance (governance framework)
- HR (policies and principles)
- Executive reporting (mission, vision)
```

#### 01-IDENTITY/README.md
Add:
```markdown
## Business Functions This Domain Supports

- Strategy & Leadership (company identity)
- Sales (brand positioning)
- Marketing (brand narrative)
- HR (culture and values)
- Fundraising (investor narrative)
```

#### 04-DATA/README.md
Add:
```markdown
## Business Functions This Domain Supports

- All 33 business functions (data is foundational)
- Specifically critical for:
  - Finance (transaction data)
  - Operations (workflow data)
  - Sales (pipeline data)
  - Analytics (reporting)
```

#### 14-CAPABILITIES/README.md
Add:
```markdown
## Business Functions Depend on Capabilities

[Detailed mapping of all 300 capabilities to the 33 functions]

Example:
  - Market Research (CAP-042) → Supports Strategy, Sales, Product
  - Lead Scoring (CAP-043) → Supports Sales only
  - Process Workflow (CAP-044) → Supports Operations, Project Management
```

#### 16-AGENTS/README.md
Add:
```markdown
## Agents Organized by Business Function

### Strategy & Leadership
- AGT-001 (Venture PM)
- [CEO Agent] (future)
- [Strategy Agent] (future)

### Sales
- AGT-004 (Sales Agent)
- [SDR Agent] (future)
- [AE Agent] (future)

### Research & Intelligence
- AGT-020 (Research Librarian)
- AGT-021 (Venture Librarian)
- AGT-022 (Integration Librarian)

### Operations
- AGT-005 (Operations)
- [Dispatcher Agent] (future)
- [Scheduler Agent] (future)

...
```

---

### 🟢 TIER 3: Reference Docs (ADD NEW SECTIONS)

#### **STARTHERE.md**
Add new section after current content:
```markdown
## The 33 Business Functions (New Framework)

Your Agent OS will eventually support 33 business functions:

1. Strategy & Leadership → CEO, Strategic planning, Decision support
2. Research & Intelligence → Digital Librarian, Market research, Competitive intelligence
3. Product → Product strategy, Requirements, Roadmap
4. Software Engineering → Code, Testing, Deployment
5. Sales → Prospecting, Lead qualification, Closing
6. Marketing → Content, Campaigns, Analytics
...through...
33. Corporate Intelligence → Market monitoring, Risk detection

Each function decomposes into Responsibilities → Capabilities → Agents.
```

---

#### **INDEX.md**
Add:
```markdown
## Agent OS Business Function Map

See: [[14-CAPABILITIES/README.md]] for full capability-to-function mapping
See: [[16-AGENTS/README.md]] for agent assignments by function
See: [[19-ORCHESTRATION/README.md]] for how responsibilities route to agents
```

---

#### **INDEX-DOMAINS-COMPLETE.md**
Add:
```markdown
## Business Functions Per Domain

| Domain | Functions Supported | Critical Agent |
|--------|-------------------|-----------------|
| 00-CONSTITUTION | Compliance, HR, Leadership | N/A (framework) |
| 01-IDENTITY | Strategy, Sales, Marketing, HR | Brand Agent (future) |
| 14-CAPABILITIES | All 33 functions | Capability Router (orchestrator) |
| 16-AGENTS | All 33 functions | Orchestrator |
| 19-ORCHESTRATION | All 33 functions | Orchestrator kernel |
```

---

### 🔵 TIER 4: New Docs (CREATE)

#### **BUSINESS_FUNCTIONS_DIRECTORY.md** (NEW)
Create comprehensive reference for all 33 business functions:

```markdown
# Business Functions Directory

Complete mapping of 33 business functions to Company Brain Agent OS.

## Format for Each Function

```yaml
function_id: BF-001
name: Strategy & Leadership
agents:
  - AGT-001 (Venture PM)
  - [CEO Agent] (future)
  - [Strategy Agent] (future)
responsibilities:
  - RESP-001: Strategic planning
  - RESP-002: Market analysis
  - RESP-003: Capital allocation
capabilities_required:
  - CAP-001: Market analysis
  - CAP-002: Financial forecasting
  - CAP-003: Risk assessment
domains_involved:
  - 00-CONSTITUTION
  - 20-DECISIONS
  - 21-CAPITAL
wikis:
  - [[STARTHERE.md]]
  - [[00-CONSTITUTION/README.md]]
```

Then document all 33...
```

---

#### **RESPONSIBILITY_INDEX.md** (NEW)
Create master reference of all responsibilities:

```markdown
# Responsibility Index

Maps every responsibility to its business function, required capabilities, and assigned agents.

## Sales Responsibilities

RESP-001: identify_prospects
  ├─ Function: Sales
  ├─ Capabilities: Market research, Lead research
  ├─ Agents: AGT-020, AGT-004, [SDR Agent]
  └─ Workflow: Market → Prospects → Qualification

RESP-002: qualify_leads
  ├─ Function: Sales
  ├─ Capabilities: Lead scoring, Account enrichment
  ├─ Agents: AGT-004, [Lead Scorer Agent]
  └─ Workflow: Prospects → Qualified leads → Proposals

...
```

---

## WIKI LINK UPDATES BY SECTION

### Navigation Layer Updates

**_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml**

Add new aliases:
```yaml
Agent Operating System:
  - Agent OS
  - Agent index
  - Business function framework
  - Orchestrator control plane

Business Functions:
  - 33 functions
  - Business OS
  - Responsibility-driven architecture
  - Function-first design

Each of 33 functions:
  - Strategy & Leadership
  - Research & Intelligence
  - Product
  - Software Engineering
  - Sales
  - ... through ...
  - Corporate Intelligence
```

---

## IMPLEMENTATION TIMELINE

| Phase | Dates | Action | Status |
|-------|-------|--------|--------|
| **Phase 1** | Sep 12-14 | Update TIER 1 docs (4 docs) | 🔴 Pending |
| **Phase 2** | Sep 14-16 | Update TIER 2 domain READMEs (20+ docs) | 🟡 Pending |
| **Phase 3** | Sep 16-17 | Create TIER 4 new docs (2 docs) | 🟢 Pending |
| **Phase 4** | Sep 17-18 | Update TIER 3 reference docs (5 docs) | 🔵 Pending |
| **Phase 5** | Sep 18-19 | Update navigation aliases + cross-links | 🟣 Pending |

---

## CRITICAL CROSS-LINKS TO ADD

After updates, add these wiki links:

**In AGENTS.md:**
- Link each agent to its business function doc
- Link each agent's responsibilities to RESPONSIBILITY_INDEX.md
- Link each agent's capabilities to CAPABILITY_INDEX.md

**In 14-CAPABILITIES/README.md:**
- Link each capability to which functions use it
- Link each capability to which agents provide it
- Link each capability to required business functions

**In 16-AGENTS/README.md:**
- Link to Business Functions Directory
- Link to Responsibility Index
- Link to Orchestration layer

**In 19-ORCHESTRATION/README.md:**
- Link to Business Functions Directory
- Link examples to specific responsibilities
- Link to Agent assignments

---

## SUCCESS CRITERIA

✅ Every agent has a "Business Function" label  
✅ Every responsibility maps to a business function  
✅ Every capability maps to which functions use it  
✅ Every domain README has "Functions Supported" section  
✅ New docs created: Business Functions Directory + Responsibility Index  
✅ Navigation layer updated with business function aliases  
✅ All cross-links bidirectional (agent ↔ function ↔ responsibility ↔ capability)

---

**Authority:** CP-006 (Agents) + Navigation Layer (CP-013)  
**Owner:** Navigation & Documentation  
**Blocker:** None (documentation-only, no code changes)  
**Timeline:** Complete by Sep 19 to support Path B launch

