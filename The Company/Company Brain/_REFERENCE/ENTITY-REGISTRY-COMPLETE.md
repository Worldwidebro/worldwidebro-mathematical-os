# Complete Entity Registry — All Entity Types Bracketed

**Authority:** CP-001 (Sovereign Operator)  
**Generated:** 2026-09-25  
**Status:** COMPREHENSIVE (all 16 entity types mapped)

---

## Entity Types Coverage Matrix

| Entity Type | Count | Bracketed | Registered | Status |
|---|---|---|---|---|
| **Bases** | 500 | ✅ B001-B500 | CBP_REGISTRY.yaml | COMPLETE |
| **Domains** | 50 | ✅ 00-CONSTITUTION through 50-MASTER-CONTROL | DOMAIN-MAP.md | COMPLETE |
| **Agents** | 50 | ✅ AGENT-[Name] | AGENT_DISPATCH_ROUTING.yaml | COMPLETE |
| **Ventures** | 789 | ✅ VENTURE-[ID] | VENTURE_TO_BASE_MAPPING.yaml | COMPLETE |
| **Workflows** | 5+ | ✅ WORKFLOW-[N] | TASK_WORKFLOW_DEFINITIONS.yaml | COMPLETE |
| **Tasks** | 20+ | ✅ TASK-[Name] | TASK_WORKFLOW_DEFINITIONS.yaml | COMPLETE |
| **Sectors** | 35 | ⚠️ SEC-001 to SEC-035 | SECTOR-REGISTRY.yaml | PENDING |
| **Operating Companies** | 36 | ⚠️ OPCO-001 to OPCO-036 | OPCO-REGISTRY.yaml | PENDING |
| **Legal Entities** | 150 | ❌ UNBRACKETED | LEGAL-ENTITY-REGISTRY.yaml | MISSING |
| **Customers** | 500+ | ⚠️ CUSTOMER-[Category] | CUSTOMER-REGISTRY.yaml | PENDING |
| **Repositories** | 1,740 | ⚠️ REPO-[ID] | REPOSITORY-REGISTRY.yaml | PENDING |
| **Capabilities** | 300+ | ⚠️ CAP-[ID] | CAPABILITY-REGISTRY.yaml | PENDING |
| **Skills** | 50+ | ⚠️ SKILL-[ID] | SKILL-REGISTRY.yaml | PENDING |
| **MCPs** | 20+ | ⚠️ MCP-[ID] | MCP-REGISTRY.yaml | PENDING |
| **Tools** | 200+ | ⚠️ TOOL-[ID] | TOOL-REGISTRY.yaml | PENDING |
| **Stakeholders/People** | 100+ | ❌ UNBRACKETED | PERSON-REGISTRY.yaml | MISSING |

---

## 🔴 CRITICAL: Legal Entity Structure (UNBRACKETED)

### Family Office Hierarchy

```
[[FAMILY-TRUST]]  (Principal)
    ↓
[[HOLDING-COMPANY-PARENT]]  (Asset/IP/Admin LLCs)
    ├── [[TRUST-Asset-001]]
    ├── [[TRUST-IP-001]]
    └── [[TRUST-Admin-001]]
    ↓
[[OPCO-001]] through [[OPCO-036]]  (Operating Companies)
    ↓
[[VENTURE-001]] through [[VENTURE-789]]  (Ventures)
```

### 150 Legal Entities (Need Bracketing)

**From CLAUDE.md:**
- 1 Family Trust (Principal)
- 150 Legal Entities total:
  - Asset management LLCs (30-50)
  - IP holding trusts (20-30)
  - Administrative trusts (10-15)
  - Operating company structures (50-60)

**Current Status:** NOT BRACKETED

**Needed:**
```
[[LE-001]] through [[LE-150]] 
with relationships:
  - controlled_by → [[FAMILY-TRUST]]
  - holds → [[VENTURE-X]]
  - operated_by → [[OPCO-Y]]
  - manages → [[ASSET-Z]]
```

---

## 🟡 PENDING: Sectors & Operating Companies

### Sectors (35 Total)

**Currently:** SEC-001 to SEC-035 (defined in SECTOR-TAXONOMY-MASTER.md)

**Needed Bracketing:**
```
[[SEC-001|Operations]]
[[SEC-002|Logistics]] 
[[SEC-003|Technology]]
...
[[SEC-035|Master Control]]
```

**Relationships to bracket:**
- [[SEC-N]] contains [[VENTURE-X]], [[VENTURE-Y]]
- [[SEC-N]] managed_by [[OPCO-M]]
- [[SEC-N]] mapped_to [[BASE-N]]
- [[SEC-N]] employs [[AGENT-Name]]

### Operating Companies (36 Total)

**Currently:** OPCO-001 to OPCO-036 (in org structure)

**Needed Bracketing:**
```
[[OPCO-001|Operations Company]]
[[OPCO-005|Logistics Company]]
[[OPCO-010|Technology Company]]
...
[[OPCO-036|Master Control Company]]
```

**Relationships to bracket:**
- [[OPCO-N]] operates [[VENTURE-X]], [[VENTURE-Y]]
- [[OPCO-N]] assigned_to [[SEC-M]]
- [[OPCO-N]] controlled_by [[LE-K]]
- [[OPCO-N]] managed_by [[EXECUTIVE-Role]]

---

## ✅ COMPLETE: Currently Bracketed Entities

### Core Infrastructure (500 Bases + 50 Domains + 50 Agents)
```
[[BASE-001]] → [[00-CONSTITUTION]] → [[AGENT-Strategic-Planning]]
[[BASE-251]] → [[25-SALES]] → [[AGENT-Sales-Pipeline]]
[[BASE-581]] → [[58-LOGISTICS]] → [[AGENT-Dispatch]]
... (all 500 wired)
```

### Ventures (789 Total)
```
[[VENTURE-OPS-001]] assigned_to [[BASE-291]] via [[OPCO-001]] in [[SEC-010|Operations]]
[[VENTURE-LT-005]] assigned_to [[BASE-581]] via [[OPCO-005]] in [[SEC-004|Logistics]]
[[VENTURE-CALLCENTER]] assigned_to [[BASE-291]] via [[OPCO-001]] in [[SEC-010|Operations]]
... (789 wired)
```

### Workflows (5+ Core)
```
[[WORKFLOW-SalesOpportunity]] 
  executes_via [[AGENT-Sales-Pipeline]]
  operates_on [[VENTURE-OPS-001]], [[VENTURE-LT-005]]
  
[[WORKFLOW-DeliveryDispatch]]
  executes_via [[AGENT-Dispatch]]
  operates_on [[VENTURE-LT-005]]
  
[[WORKFLOW-FinancialReconciliation]]
  executes_via [[AGENT-Financial-Planning]]
  operates_on all ventures
```

### Tasks (20+ Core)
```
[[TASK-CreateOpportunity]] defined_in [[WORKFLOW-SalesOpportunity]]
[[TASK-ValidateAddress]] defined_in [[WORKFLOW-DeliveryDispatch]]
[[TASK-MatchTransactions]] defined_in [[WORKFLOW-FinancialReconciliation]]
... (all workflow steps wired)
```

### Technology Stack (Partial)
```
[[REPO-0042]] implements [[CAP-001]] 
  enables [[SKILL-0042]] 
  uses [[MCP-0009]] 
  exposes [[TOOL-0015]]
```

---

## ❌ MISSING: Stakeholders & Legal Details

### 21 Core Stakeholders (Need Bracketing)

**From PEOPLE-ROLES-INFRASTRUCTURE-BRIDGE.md:**
- Founder: Antwuan Johns
- Executives (5-7)
- Operational leads (8-10)
- Support staff (3-5)

**Needed:**
```
[[PERSON-AntwuanJohns|Founder/CEO]]
  has_authority [[CP-001]]
  signs_off_on [[DECISION-Type-A]]
  owns [[OPCO-All]]

[[PERSON-ChiefOfStaff|Chief of Staff]]
  manages [[ORG-Structure]]
  approves [[VENTURE-Create]]

[[PERSON-VPSales|VP Sales]]
  leads [[BASE-251]]
  manages [[AGENT-Sales-Pipeline]]
  approves [[TASK-HighValue]]
```

### Approval Authorities (Need Bracketing)

**Strategic Approvers:**
- [[AUTHORITY-Founder]] → All strategic decisions
- [[AUTHORITY-CFO]] → Financial decisions > $10K
- [[AUTHORITY-VPOps]] → Operational decisions
- [[AUTHORITY-ChiefLegal]] → Legal/compliance

**Operational Approvers:**
- [[AUTHORITY-DepartmentHead]] → Daily operations
- [[AUTHORITY-TeamLead]] → Task escalations
- [[AUTHORITY-OnCall]] → Emergency decisions

---

## 🔧 MISSING: External Entities

### Partners & Integrations
```
[[PARTNER-AWS]]
[[PARTNER-Supabase]]
[[PARTNER-Make.com]]
[[PARTNER-OpenAI]]
[[PARTNER-Anthropic]]
```

### External Systems
```
[[SYSTEM-GitHub]]
[[SYSTEM-Supabase]]
[[SYSTEM-Neo4j]]
[[SYSTEM-Qdrant]]
[[SYSTEM-OmniRoute]]
```

### Government & Regulatory
```
[[REGULATOR-SEC]] (if applicable)
[[JURISDICTION-US]]
[[TAX-ENTITY-EIN]]
```

---

## Complete Bracketing Roadmap (Oct 22-30)

### Oct 22 (Launch Day)
✅ **Already Bracketed:**
- 500 Bases (B001-B500)
- 50 Domains (00-CONSTITUTION → 50-MASTER-CONTROL)
- 50 Agents (AGENT-Name)
- 789 Ventures (VENTURE-ID)
- 5+ Workflows (WORKFLOW-Name)
- 20+ Tasks (TASK-Name)

### Oct 23-25 (Extended Entities)
🔄 **Must Bracket:**
- [[SEC-001]] through [[SEC-035]] — Sectors
- [[OPCO-001]] through [[OPCO-036]] — Operating Companies
- [[REPO-XXXX]] through [[REPO-XXXX]] — Repositories (1,740)
- [[CAP-XXXX]] through [[CAP-XXXX]] — Capabilities (300+)
- [[SKILL-XXXX]] through [[SKILL-XXXX]] — Skills (50+)
- [[MCP-XXXX]] through [[MCP-XXXX]] — MCPs (20+)
- [[TOOL-XXXX]] through [[TOOL-XXXX]] — Tools (200+)
- [[CUSTOMER-XXXX]] — Customers (500+)

### Oct 26-28 (Critical Missing)
🔴 **CRITICAL - Must Complete:**
- [[LE-001]] through [[LE-150]] — Legal Entities
- [[PERSON-Name]] — All stakeholders (21 core + extended)
- [[AUTHORITY-Role]] — All approval authorities
- [[PARTNER-Name]] — External partners
- [[SYSTEM-Name]] — External systems

### Oct 29-30 (Verification)
✅ **Final Verification:**
- All relationships bidirectional
- All entities have ID + type + status
- Revenue path fully traceable
- Legal structure clearly mapped
- Stakeholder approvals wired

---

## Entity Bracketing Convention

### Format
```
[[ENTITY-TYPE-ID|Display Name]]
or
[[ENTITY-TYPE-ID]] (if unambiguous)
```

### Examples
```
Base:      [[BASE-251|Sales Control Base]]
Domain:    [[25-SALES]]
Agent:     [[AGENT-Sales-Pipeline]]
Venture:   [[VENTURE-LT-005|HealthRoute]]
Sector:    [[SEC-004|Logistics]]
OpCo:      [[OPCO-005|Logistics Company]]
Legal:     [[LE-042|Logistics OpCo Trust]]
Person:    [[PERSON-AntwuanJohns|Founder]]
Authority: [[AUTHORITY-CFO]]
Repository: [[REPO-0042|browser-use]]
Capability: [[CAP-001|Browser Automation]]
Customer:  [[CUSTOMER-Healthcare]]
Partner:   [[PARTNER-AWS]]
System:    [[SYSTEM-Supabase]]
```

### Registry Files (All Needed)
- CBP_REGISTRY.yaml ✅ (LIVE)
- DOMAIN-MAP.md ✅ (LIVE)
- AGENT_DISPATCH_ROUTING.yaml ✅ (LIVE)
- VENTURE_TO_BASE_MAPPING.yaml ✅ (LIVE)
- TASK_WORKFLOW_DEFINITIONS.yaml ✅ (LIVE)
- SECTOR-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- OPCO-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- **LEGAL-ENTITY-REGISTRY.yaml** 🔴 (CRITICAL - MISSING)
- CUSTOMER-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- REPOSITORY-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- CAPABILITY-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- SKILL-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- MCP-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- TOOL-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- **PERSON-REGISTRY.yaml** 🔴 (CRITICAL - MISSING)
- AUTHORITY-REGISTRY.yaml 🔴 (CRITICAL - MISSING)
- PARTNER-REGISTRY.yaml 🔄 (NEEDS BRACKETING)
- SYSTEM-REGISTRY.yaml 🔄 (NEEDS BRACKETING)

---

## 🔴 CRITICAL GAP: Legal Entities (150 Unbracketed)

**Problem:** We know from CLAUDE.md that there are 150 legal entities controlling ventures and capital, but:
- No entity IDs defined (LE-001 through LE-150)
- No relationships to ventures bracketed
- No ownership structure wired in graph
- No control points marked

**Impact:** 
- Revenue attribution incomplete (can't trace $ to legal entity)
- Compliance untracked (entity responsibility unmapped)
- Capital allocation unmapped (can't query who owns what)
- Governance broken (control authority undefined)

**Solution:** Create LEGAL-ENTITY-REGISTRY.yaml with:
```
[[LE-001]] through [[LE-150]]
  └── relationships:
      - controlled_by → [[FAMILY-TRUST]]
      - operates → [[VENTURE-X]]
      - contains → [[OPCO-Y]]
      - holds → [[ASSET-Z]]
      - reports_to → [[AUTHORITY-CFO]]
```

---

## Status Summary

| Category | Complete | Bracketed | Registered | Next |
|---|---|---|---|---|
| **Core Infrastructure** | ✅ 100% | ✅ 100% | ✅ 100% | Live |
| **Ventures & Workflows** | ✅ 100% | ✅ 100% | ✅ 100% | Live |
| **Sectors & OpCos** | ⚠️ 80% | ❌ 0% | ⚠️ 50% | Bracket & link |
| **Legal Entities** | ❌ 0% | ❌ 0% | ❌ 0% | CREATE IMMEDIATELY |
| **People & Roles** | ⚠️ 50% | ❌ 0% | ⚠️ 30% | Bracket & link |
| **Technology Stack** | ⚠️ 60% | ⚠️ 20% | ⚠️ 40% | Bracket all |

**CRITICAL MISSING:** Legal entities must be bracketed and linked before Oct 22 go-live to ensure governance is operational.

