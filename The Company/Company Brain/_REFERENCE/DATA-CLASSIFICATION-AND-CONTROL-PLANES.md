# Data Classification & Control Planes

**Date:** 2026-09-22  
**Authority:** [[RESPECT|00_RESPECT/RESPECT.md]] (governance) + [[ANTIGRAVITY|ANTIGRAVITY.md]] (zero fake completion)  
**Purpose:** Define what's public, private, and how control planes govern access across Bases

---

## Data Classification Matrix

| Layer | Data | Classification | Access | Storage | Governance |
|-------|------|-----------------|--------|---------|------------|
| **VEX Portal** | Venture showcase, hero video, founder path | **PUBLIC** | World-wide | Vercel (vex-hero-site-sigma.vercel.app) | CP-006 (Revenue) |
| **VEX Dashboard** | Portfolio metrics, revenue, agent count | **PUBLIC (Aggregate)** | Founders, investors | Supabase (public schema) | CP-027 (Infrastructure) |
| **portfolio.public.json** | Sanitized venture list (names, URLs, archetypes) | **PUBLIC (Filtered)** | CDN, clients | Vercel static files | CP-001 (Enterprise) |
| **Company Brain Registries** | ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv | **PRIVATE** | Internal only (Claude, agents) | Git (Company Brain repo) | CP-001 (Enterprise) + CP-021 (Revenue) |
| **Neo4j Graph** | Relationships, entity metadata, decision logic | **PRIVATE** | Agents + authorized operators | On-premise Mac Studio | CP-027 (Infrastructure) |
| **Qdrant Vectors** | Semantic embeddings of knowledge, concepts | **PRIVATE** | Agents (semantic search only) | On-premise Mac Studio | CP-027 (Infrastructure) |
| **Supabase (Private)** | Venture financials, agent performance, internal metrics | **PRIVATE** | Agents, finance team, founders | Hosted (encrypted) | CP-021 (Revenue) + CP-027 (Infra) |
| **Obsidian Vault** | Base knowledge, operational decisions, research | **PRIVATE** | Founders, internal operators | Local encrypted disk | CP-001 (Enterprise) |
| **Base Ontologies** | Entities, relationships, domain models | **PRIVATE** | Agents scoped to Base | Neo4j + Git | CP-027 (Infra) |
| **Agent Internals** | Reasoning, logs, tool invocations, decisions | **PRIVATE** | Agents, operators (debugging) | Supabase logs (encrypted) | CP-033 (Execution) |
| **Control Plane Decisions** | Approval logs, escalations, policy changes | **PRIVATE (Audit)** | CP members only | Neo4j + audit logs | CP-001 (Enterprise) |
| **Legal/Tax Docs** | OpCo structures, trust documents, IP vaults | **CONFIDENTIAL** | Founders, attorneys | Secure data room | CP-001 (Enterprise) |

---

## Public Layer (VEX → World)

### What VEX Shows (portfolio.public.json)

```json
{
  "ventures": [
    {
      "id": "LT-005",
      "name": "Medical Courier",
      "sector": "Logistics & Healthcare",
      "archetype": "Contract Cash Flow",
      "status": "live",
      "url": "https://healthroute-courier.vercel.app",
      "github": "https://github.com/Worldwidebro/lt-005-medical-courier-dispatch"
    },
    // ... sanitized entries only
  ],
  "metrics": {
    "total_ventures": 789,
    "live": 15,
    "in_development": 200,
    "sectors": 36
  }
}
```

**Excluded from portfolio.public.json:**
- ❌ Financial metrics (revenue, costs, margins)
- ❌ Venture readiness scores (internal planning)
- ❌ OpCo mappings (legal structure)
- ❌ Agent assignments (operations)
- ❌ Decision histories (governance)
- ❌ Any PII or proprietary data

### VEX Dashboard (Aggregate Metrics)

**Public to Founders/Investors:**
- ✅ Total active ventures (count)
- ✅ Revenue (company total, not per-venture)
- ✅ Active agents (count)
- ✅ Recent deployments (timestamps, not details)
- ✅ Portfolio health score (aggregate)

**NOT Public:**
- ❌ Per-venture revenue breakdown
- ❌ Agent locations, assignments, credentials
- ❌ Control plane decisions
- ❌ Venture financial details
- ❌ Market analysis, strategy

**Query Control:**
- VEX dashboard reads from `supabase_public_schema` (filtered views)
- No direct Neo4j access (graph remains private)
- No access to venture_financials or agent_performance tables

---

## Private Layer (Company Brain → Agents + Operators)

### Neo4j Graph (Private)

**What's Stored:**
- Base nodes (35), Venture nodes (789), Agent nodes (318)
- Relationships: (Base)-[:CONTAINS_VENTURE]->(Venture)
- Entity metadata: venture readiness, financial projections, agent capabilities
- Decision history: "CP-021 approved pricing change on 2026-09-15"

**Access:**
- Only Claude Code + authorized agents read Neo4j
- Never exposed to internet (localhost:7687, Tailscale VPN only)
- Queries run from Mac Studio only
- Query logs stored with approval chain

**Example Query (Private):**
```cypher
// Finance agent queries (sensitive)
MATCH (base:Base {id: "BASE-009"})
  -[:CONTAINS_VENTURE]->(v:Venture)
  -[:HAS_FORECAST]->(f:Forecast)
RETURN v.name, f.revenue_forecast, f.confidence
// Returns: LT-005, $85K, 0.92 (PRIVATE)
```

### Qdrant (Vector Store, Private)

**What's Stored:**
- Semantic embeddings of Base concepts ("Medical courier dispatch routing")
- Knowledge documents (SOPs, research, market analysis)
- Agent reasoning chains (for audit trail)

**Access:**
- Agents query for semantic search (hidden vectors, only results shown)
- Not exposed to VEX or public
- Cannot reverse-engineer embedding → original text

**Example Search (Private):**
```
Agent Query: "What are the constraints for Logistics dispatch?"
Qdrant Returns: TOP-3 concepts
  1. "Driver safety regulations" (conf=0.94)
  2. "Maximum delivery distance" (conf=0.91)
  3. "Vehicle maintenance schedule" (conf=0.87)
# Used to inform agent decisions; never shown publicly
```

### Registries (Git, Private)

**Private Files:**
- VENTURE_PORTFOLIO_MASTER_INVENTORY.md (all 789 ventures with internal notes)
- BUSINESS-METRIC-REGISTRY.yaml (financial models, CLV, CAC by venture)
- CONTROL_DOMAINS_250.yaml (all control plane decisions)
- AGENTS_REGISTRY.yaml (agent capabilities, autonomy levels, performance)
- CAPABILITY_GAP_MATRIX.yaml (what we can't do yet)
- LIVING_INVENTORY_VENTURES.csv (active venture status, not sanitized)

**Access:**
- Claude Code (this session) can read all registries
- Agents query via Neo4j + capability checks
- Never sent to VEX or public APIs

**Excluded from Public:**
- venture_readiness_scores.csv (not published)
- venture_financials.yaml (not published)
- agent_performance_metrics.csv (not published)

---

## Control Planes: Governance Layer

**Purpose:** Control planes are decision-makers that govern data access, Base operations, and agent autonomy.

### The 30 Control Planes (CP-001 to CP-030+)

| CP | Name | Authority | What They Govern |
|----|------|-----------|------------------|
| **CP-001** | Enterprise | Founder/sovereign operator | Venture creation, legal structure, strategic direction |
| **CP-006** | Revenue | CFO / finance team | Pricing, revenue recognition, financial reporting |
| **CP-021** | Revenue (Venture-level) | Revenue operations | Deal approvals, revenue attribution, forecasts |
| **CP-023** | Sales | Sales lead | Lead qualification, commission, forecasting |
| **CP-025** | People | HR / operations | Agent assignments, capacity planning, team structure |
| **CP-026** | Operations | Operations lead | Workflow approvals, SOP changes, incident response |
| **CP-027** | Infrastructure | Tech lead | System design, database access, deployment |
| **CP-031** | Marketing | Marketing lead | Campaign approvals, spend, content strategy |
| **CP-033** | Execution | COO / project mgmt | Task routing, deadline enforcement, escalation |
| **CP-041** | Data Security | CISO / security | Data classification, encryption, access controls |

(20+ more specialized control planes mapped to Bases, sectors, functions)

### How Control Planes Govern Bases

**Example: BASE-009 (Logistics)**

```
Base Governance:

CP-026 (Operations)
  ├─ Approves new workflows in BASE-009
  ├─ Reviews delivery SOP changes
  └─ Escalates incidents (e.g., "No drivers available")

CP-021 (Revenue)
  ├─ Sets pricing in BASE-009 (per-delivery fee)
  ├─ Approves discounts > 15%
  └─ Forecasts revenue from LT-005, LT-011

CP-027 (Infrastructure)
  ├─ Manages Neo4j access (who reads BASE-009)
  ├─ Oversees Qdrant indexing (semantic search for BASE-009)
  └─ Audits agent tool usage (OmniRoute API calls)

CP-033 (Execution)
  ├─ Routes tasks to Dispatch Agent (BASE-009 scoped)
  ├─ Sets SLA (delivery within 4 hours)
  └─ Triggers escalation to CP-026 if SLA breached

Decision Chain:
  Founder (CP-001) sets strategy
    ↓
  Revenue (CP-021) sets pricing
    ↓
  Operations (CP-026) designs workflow
    ↓
  Execution (CP-033) assigns tasks
    ↓
  Dispatch Agent executes (scoped to BASE-009)
    ↓
  Results logged + fed back to all CPs
```

### Control Plane + Data Classification

**Rule 1: CP Authority Determines Data Access**
```
Agent (Dispatch)
  ├─ Scoped to: BASE-009
  ├─ CP Authority: CP-026, CP-033
  ├─ Can Read: BASE-009 ontology, operational state
  └─ Cannot Read: BASE-012 (Real Estate), financial forecasts
```

**Rule 2: Escalation Changes Data Visibility**
```
Normal Flow:
  Agent (Dispatch) → [Can't approve discount > 15%]
                   → Escalate to CP-021 (Revenue)
                   → CP-021 Reviews: financial model + impact
                   → CP-021 Approves or Denies
                   → Decision logged (audit trail)
```

**Rule 3: CPs Make Public/Private Decisions**
```
Example: Should LT-005 metrics be public?
  
  Founder (CP-001): "Show revenue in VEX dashboard"
  
  Revenue (CP-021): "Approve public aggregate only (total logistics revenue)"
  
  Infrastructure (CP-027): "Filter Supabase query - show sector total, not per-venture"
  
  VEX Updates: Portfolio shows "$120K logistics revenue" (aggregate, safe)
  
  Audit Trail: Decision logged with CP approvals
```

---

## Data Flow with Governance

```
EXTERNAL (PUBLIC)
├── VEX Portal (hero experience, founder path)
│   └── portfolio.public.json (sanitized venture list)
│       └── Queries: portfolio metrics aggregate only
│           └── CP-001/CP-006 approve what's public
│
INTERNAL (PRIVATE)
├── Company Brain (Neo4j, Qdrant, Registries)
│   └── Agents + operators query via:
│       ├── Neo4j (graph, relationship queries)
│       ├── Qdrant (semantic search)
│       └── Registries (YAML/CSV lookups)
│
├── Control Planes (Governance Layer)
│   ├── CP-001 → Enterprise decisions (venture creation)
│   ├── CP-006 → Revenue decisions (pricing, forecasting)
│   ├── CP-021 → Venture-level revenue
│   ├── CP-026 → Operations (workflows, SOPs)
│   ├── CP-027 → Infrastructure (data access, Neo4j)
│   ├── CP-033 → Execution (task routing, escalation)
│   └── CP-041 → Security (data classification)
│
└── Agent Execution (Private)
    ├── Agent reads Base knowledge (private)
    ├── Agent queries Neo4j (private)
    ├── Agent executes within CP authority
    ├── Agent logs results (audit trail)
    └── Results feed back to CPs + memory

VEX Dashboard (Semi-Public)
├── Aggregate metrics only
├── CP approval for each metric
├── No per-venture breakdowns
└── Sanitized view of Company Brain
```

---

## Security & Audit

### What Gets Logged (Audit Trail)

**Always Logged:**
- ✅ Who queried what (agent ID, query type)
- ✅ What was returned (data accessed)
- ✅ When (timestamp)
- ✅ Why (task context, CP approval)
- ✅ Result (decision made, action taken)

**Stored in:**
- Neo4j: audit nodes with (User)-[:EXECUTED]->(Query)-[:RETURNED]->(Result)
- Supabase: audit_logs table (encrypted)
- Obsidian: Decision logs per CP

### Access Control Enforcement

**Network:**
- ❌ Neo4j (localhost:7687) — never public, Tailscale VPN only
- ❌ Qdrant (localhost:6333) — never public, internal Docker only
- ❌ Supabase private schema — credentials in Bitwarden, not in code
- ✅ VEX (Vercel) — public, but queries filtered public schema only

**Code:**
- Agent scope checked on every query (Base authorization)
- CP approval required for sensitive operations (pricing changes > 15%)
- OmniRoute gateway filters tool access (who can call which APIs)

**Data:**
- Sensitive fields masked in logs (revenue → "***")
- PII encrypted (names → hashed when logged)
- Audit trail immutable (append-only)

---

## Public/Private Decision Flowchart

```
Should this data be in VEX dashboard?

START
  │
  ├─ Contains PII or sensitive financial data?
  │  └─ YES → PRIVATE (stay in Company Brain)
  │  └─ NO → Continue
  │
  ├─ Is it competitive/strategic intelligence?
  │  └─ YES → PRIVATE (only for founders)
  │  └─ NO → Continue
  │
  ├─ Would public disclosure harm negotiating position?
  │  └─ YES → PRIVATE
  │  └─ NO → Continue
  │
  ├─ Is it aggregate (sector-level, not per-venture)?
  │  └─ NO → PRIVATE (break down to aggregate)
  │  └─ YES → Continue
  │
  ├─ Get CP approval (CP-001 + CP-006)
  │  └─ NO → PRIVATE
  │  └─ YES → Continue
  │
  └─ PUBLISH to VEX (portfolio.public.json or dashboard)
     └─ Implement Supabase filtering (public schema view)
     └─ Audit log: who approved, when
```

---

## Current State (Sep 22, 2026)

| Component | Public | Private | CP Governance |
|-----------|--------|---------|---|
| **VEX Portal** | ✅ Live | — | CP-001 / CP-006 approve content |
| **portfolio.public.json** | ✅ Published | — | Sanitized list only |
| **VEX Dashboard** | ✅ Aggregate metrics | — | CP approval per metric |
| **Neo4j Graph** | — | ✅ Private (Tailscale) | CP-027 governs access |
| **Qdrant Vectors** | — | ✅ Private (internal) | CP-027 governs access |
| **Registries (Git)** | — | ✅ Private (internal) | CP-001 / CP-006 |
| **Supabase Public Schema** | ✅ VEX queries only | — | CP-027 enforces filtering |
| **Supabase Private Schema** | — | ✅ Agents only | CP-021 / CP-041 |
| **Obsidian Vault** | — | ✅ Local encrypted | CP-001 (founders only) |
| **Audit Logs** | — | ✅ Encrypted | CP-001 / CP-041 |

---

## Bases + Data Classification

### Per-Base Classification

**BASE-009 (Logistics) Classification:**
- **Public:** "Logistics sector: 2 active ventures, live service"
- **Semi-Public:** "Logistics revenue: $X this month" (aggregate only)
- **Private:** "LT-005 revenue $Y, LT-011 revenue $Z" (per-venture)
- **Private:** "Driver roster, delivery logs, customer data" (PII)

**Per-Base CP Governance:**
- CP-026 (Operations) → operations.md changes
- CP-021 (Revenue) → pricing, revenue forecasts
- CP-033 (Execution) → task routing, escalation
- CP-027 (Infrastructure) → Neo4j access for BASE-009 agents

---

## Next Steps

1. **Supabase Schema:** Create public_schema view (filtered metrics only)
2. **VEX Integration:** Query public_schema for dashboard data
3. **Audit Trail:** Log all CP approvals for public data decisions
4. **Per-Base Policies:** Define classification for each of 35 Bases
5. **Security Review:** Verify no sensitive data leaks via VEX

---

**Authority:** [[RESPECT|RESPECT.md]] (governance) + [[ANTIGRAVITY|ANTIGRAVITY.md]] (zero fake completion) + CP decisions  
**Updated:** 2026-09-22  
**Status:** GOVERNANCE FRAMEWORK READY

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]