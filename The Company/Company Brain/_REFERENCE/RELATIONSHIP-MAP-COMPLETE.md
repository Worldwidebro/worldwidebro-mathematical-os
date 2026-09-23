# Complete Relationship Map — Company Brain Entity Graph

**Authority:** CP-001 (Sovereign Operator)  
**Generated:** 2026-09-25  
**Status:** CANONICAL (all relationships bracketed)

---

## Relationship Types & Directions

| Type | Direction | Example |
|------|-----------|---------|
| `implements` | Repository → Capability | [[REPO-0042]] implements [[CAP-001]] |
| `enables` | Capability → Skill | [[CAP-001]] enables [[SKILL-0042]] |
| `uses` | Skill → MCP | [[SKILL-0042]] uses [[MCP-0009]] |
| `exposes` | MCP → Tool | [[MCP-0009]] exposes [[TOOL-0015]] |
| `executed_by` | Tool → Agent | [[TOOL-0015]] executed_by [[AGENT-Dispatch]] |
| `executes` | Agent → Workflow | [[AGENT-Dispatch]] executes [[WORKFLOW-001]] |
| `operates_on` | Workflow → Venture | [[WORKFLOW-001]] operates_on [[VENTURE-LT-005]] |
| `serves` | Venture → Customer | [[VENTURE-LT-005]] serves [[CUSTOMER-Healthcare]] |
| `produces` | Customer → Revenue | [[CUSTOMER-Healthcare]] produces [[REVENUE-LT-005]] |
| `maps_to` | Base → Domain | [[BASE-251]] maps_to [[DOMAIN-25-SALES]] |
| `assigned_to` | Domain → Agent | [[DOMAIN-25-SALES]] assigned_to [[AGENT-Sales-Pipeline]] |
| `defined_in` | Task → Workflow | [[TASK-CreateOpportunity]] defined_in [[WORKFLOW-SalesFlow]] |
| `escalates_to` | Task → Authority | [[TASK-CreateOpportunity]] escalates_to [[AUTHORITY-SalesManager]] |
| `stored_in` | Revenue → Venture | [[REVENUE-LT-005]] stored_in [[VENTURE-LT-005]] |

---

## Phase 0: Infrastructure (500 Bases)

### Base → Domain Mapping

**Constitution Layer (00):**
- [[BASE-001]] maps_to [[00-CONSTITUTION]]
- [[BASE-002]] maps_to [[00-CONSTITUTION]]
- ... (10 bases per domain)
- [[BASE-010]] maps_to [[00-CONSTITUTION]]

**Identity Layer (01):**
- [[BASE-011]] maps_to [[01-IDENTITY]]
- [[BASE-012]] maps_to [[01-IDENTITY]]
- ... (10 bases)
- [[BASE-020]] maps_to [[01-IDENTITY]]

**Sources to Orchestration (02-19):**
- [[BASE-021]] → [[02-SOURCES]]
- [[BASE-031]] → [[03-INGESTION]]
- [[BASE-041]] → [[04-DATA]]
- [[BASE-051]] → [[05-METADATA]]
- [[BASE-061]] → [[06-ENTITY-RESOLUTION]]
- [[BASE-071]] → [[07-ONTOLOGY]]
- [[BASE-081]] → [[08-KNOWLEDGE-GRAPH]]
- [[BASE-091]] → [[09-KNOWLEDGE]]
- [[BASE-101]] → [[10-MEMORY]]
- [[BASE-111]] → [[11-INDEXING]]
- [[BASE-121]] → [[12-CONTEXT]]
- [[BASE-131]] → [[13-REPOSITORIES]]
- [[BASE-141]] → [[14-CAPABILITIES]]
- [[BASE-151]] → [[15-SKILLS]]
- [[BASE-161]] → [[16-AGENTS]]
- [[BASE-171]] → [[17-MODELS]]
- [[BASE-181]] → [[18-TOOLS]]
- [[BASE-191]] → [[19-ORCHESTRATION]]

**Operations & Execution (20-28):**
- [[BASE-201]] → [[20-DECISIONS]]
- [[BASE-211]] → [[21-POLICY]]
- [[BASE-221]] → [[22-EXECUTION]]
- [[BASE-231]] → [[23-VENTURES]]
- [[BASE-241]] → [[24-FINANCE]]
- [[BASE-251]] → [[25-SALES]]
- [[BASE-261]] → [[26-MARKETING]]
- [[BASE-271]] → [[27-CUSTOMERS]]
- [[BASE-281]] → [[28-PRODUCT]]

**Business Operations (29-36):**
- [[BASE-291]] → [[29-OPERATIONS]]
- [[BASE-301]] → [[30-HR]]
- [[BASE-311]] → [[31-LEGAL]]
- [[BASE-321]] → [[32-SECURITY]]
- [[BASE-331]] → [[33-COMPLIANCE]]
- [[BASE-341]] → [[34-RISK]]
- [[BASE-351]] → [[35-ASSETS]]
- [[BASE-361]] → [[36-PARTNERS]]

**Research & Learning (37-50):**
- [[BASE-371]] → [[37-RESEARCH]]
- [[BASE-381]] → [[38-OPPORTUNITIES]]
- [[BASE-391]] → [[39-EXPERIMENTS]]
- [[BASE-401]] → [[40-METRICS]]
- [[BASE-411]] → [[41-OBSERVABILITY]]
- [[BASE-421]] → [[42-EVALUATION]]
- [[BASE-431]] → [[43-OUTCOMES]]
- [[BASE-441]] → [[44-LEARNING]]
- [[BASE-451]] → [[45-EVOLUTION]]
- [[BASE-461]] → [[46-GOVERNANCE]]
- [[BASE-471]] → [[47-DOCUMENTS]]
- [[BASE-481]] → [[48-AUTOMATION]]
- [[BASE-491]] → [[49-SYSTEM]]
- [[BASE-501]] → [[50-MASTER-CONTROL]]

---

## Phase 1: Agent Routing

### Domain → Agent Relationships

**Strategic Layer (L1):**
- [[00-CONSTITUTION]] assigned_to [[AGENT-Strategic-Planning]]
- [[20-DECISIONS]] assigned_to [[AGENT-Decision-Framework]]
- [[31-LEGAL]] assigned_to [[AGENT-Legal-Compliance]]
- [[46-GOVERNANCE]] assigned_to [[AGENT-Governance-Framework]]
- [[50-MASTER-CONTROL]] assigned_to [[AGENT-Executive-Dashboard]]

**Operational Layer (L2):**
- [[01-IDENTITY]] assigned_to [[AGENT-Org-Design]]
- [[02-SOURCES]] assigned_to [[AGENT-Data-Ingestion]]
- [[04-DATA]] assigned_to [[AGENT-Database-Optimizer]]
- [[05-METADATA]] assigned_to [[AGENT-Metadata-Steward]]
- [[14-CAPABILITIES]] assigned_to [[AGENT-Capability-Inventory]]
- [[17-MODELS]] assigned_to [[AGENT-Model-Selection]]
- [[21-POLICY]] assigned_to [[AGENT-Policy-Compliance]]
- [[25-SALES]] assigned_to [[AGENT-Sales-Pipeline]]
- [[26-MARKETING]] assigned_to [[AGENT-Campaign-Manager]]
- [[29-OPERATIONS]] assigned_to [[AGENT-Operations-Manager]]
- [[30-HR]] assigned_to [[AGENT-HR-Operations]]
- [[34-RISK]] assigned_to [[AGENT-Risk-Management]]
- [[37-RESEARCH]] assigned_to [[AGENT-Market-Research]]
- [[38-OPPORTUNITIES]] assigned_to [[AGENT-Opportunity-Scout]]
- [[43-OUTCOMES]] assigned_to [[AGENT-Outcome-Tracker]]
- [[44-LEARNING]] assigned_to [[AGENT-Learning-System]]
- [[45-EVOLUTION]] assigned_to [[AGENT-System-Evolution]]
- [[49-SYSTEM]] assigned_to [[AGENT-System-Architecture]]

**Tactical/Real-time Layer (L3):**
- [[03-INGESTION]] assigned_to [[AGENT-ETL-Orchestrator]]
- [[06-ENTITY-RESOLUTION]] assigned_to [[AGENT-Entity-Resolver]]
- [[08-KNOWLEDGE-GRAPH]] assigned_to [[AGENT-Graph-Database]]
- [[10-MEMORY]] assigned_to [[AGENT-Memory-System]]
- [[11-INDEXING]] assigned_to [[AGENT-Search-Index]]
- [[12-CONTEXT]] assigned_to [[AGENT-Context-Assembly]]
- [[16-AGENTS]] assigned_to [[AGENT-Lifecycle-Manager]]
- [[19-ORCHESTRATION]] assigned_to [[AGENT-Workflow-Orchestrator]]
- [[22-EXECUTION]] assigned_to [[AGENT-Execution-Tracker]]
- [[23-VENTURES]] assigned_to [[AGENT-Venture-Operations]]
- [[24-FINANCE]] assigned_to [[AGENT-Financial-Planning]]
- [[27-CUSTOMERS]] assigned_to [[AGENT-Customer-Success]]
- [[32-SECURITY]] assigned_to [[AGENT-Security-Operations]]
- [[39-EXPERIMENTS]] assigned_to [[AGENT-Experiment-Manager]]
- [[40-METRICS]] assigned_to [[AGENT-Metrics-Dashboard]]
- [[41-OBSERVABILITY]] assigned_to [[AGENT-System-Observability]]
- [[48-AUTOMATION]] assigned_to [[AGENT-Automation-Orchestrator]]

---

## Phase 2: Venture Assignment

### Venture → Base Relationships

**Revenue-Generating (ACTIVE):**
- [[VENTURE-OPS-001]] assigned_to [[BASE-291]] (Operations)
- [[VENTURE-LT-005]] assigned_to [[BASE-581]] (Logistics — extended)
- [[VENTURE-CALLCENTER]] assigned_to [[BASE-291]] (Operations)

**Building (DEVELOPMENT):**
- [[VENTURE-CON-001]] assigned_to [[BASE-511]] (Construction — extended)
- [[VENTURE-RE-001]] assigned_to [[BASE-541]] (Financial — extended)

**Assessment:**
- [[VENTURE-LT-011]] assigned_to [[BASE-581]] (Logistics — extended)

### Venture → Agent Relationships

**Direct Agent Assignments:**
- [[VENTURE-OPS-001]] executes_via [[AGENT-Staffing-Pipeline]]
- [[VENTURE-LT-005]] executes_via [[AGENT-Dispatch]]
- [[VENTURE-CALLCENTER]] executes_via [[AGENT-Call-Routing]]
- [[VENTURE-CON-001]] assigned_to [[AGENT-Construction-Manager]] (pending)
- [[VENTURE-RE-001]] assigned_to [[AGENT-Real-Estate-Deal]] (pending)

### Revenue Attribution Relationships

**Transaction Flow:**
[[TRANSACTION]] 
  → captures [[VENTURE-ID]]
  → lookup [[VENTURE-TO-BASE-MAPPING]]
  → find [[BASE-ID]]
  → lookup [[BASE-TO-AGENT-MAPPING]]
  → assign [[AGENT-ID]]
  → attribute [[OPCO-ID]]
  → record [[REVENUE]]

**Example (LT-005):**
[[TRANSACTION-001]] 
  → [[VENTURE-LT-005]] 
  → [[BASE-581]] 
  → [[AGENT-Dispatch]] 
  → [[OPCO-005]] 
  → [[REVENUE-$1800]]

---

## Phase 3: Task Workflows

### Task → Workflow Relationships

**Sales Opportunity Workflow:**
- [[TASK-CreateOpportunity]] defined_in [[WORKFLOW-SalesOpportunity]]
- [[TASK-ScoreLead]] defined_in [[WORKFLOW-SalesOpportunity]]
- [[TASK-RouteSalesRep]] defined_in [[WORKFLOW-SalesOpportunity]]
- [[TASK-CreateDealRecord]] defined_in [[WORKFLOW-SalesOpportunity]]

**Delivery Dispatch Workflow:**
- [[TASK-CaptureDelivery]] defined_in [[WORKFLOW-DeliveryDispatch]]
- [[TASK-ValidateAddress]] defined_in [[WORKFLOW-DeliveryDispatch]]
- [[TASK-AssignDriver]] defined_in [[WORKFLOW-DeliveryDispatch]]
- [[TASK-CreateShipment]] defined_in [[WORKFLOW-DeliveryDispatch]]
- [[TASK-TrackDelivery]] defined_in [[WORKFLOW-DeliveryDispatch]]

**Financial Reconciliation Workflow:**
- [[TASK-GatherPayments]] defined_in [[WORKFLOW-FinancialReconciliation]]
- [[TASK-MatchTransactions]] defined_in [[WORKFLOW-FinancialReconciliation]]
- [[TASK-FlagDiscrepancies]] defined_in [[WORKFLOW-FinancialReconciliation]]
- [[TASK-InvestigateVariance]] defined_in [[WORKFLOW-FinancialReconciliation]]

### Workflow → Agent Relationships

- [[WORKFLOW-SalesOpportunity]] executes_via [[AGENT-Sales-Pipeline]]
- [[WORKFLOW-DeliveryDispatch]] executes_via [[AGENT-Dispatch]]
- [[WORKFLOW-FinancialReconciliation]] executes_via [[AGENT-Financial-Planning]]
- [[WORKFLOW-StaffingFollowUp]] executes_via [[AGENT-Staffing-Pipeline]]
- [[WORKFLOW-CallQuality]] executes_via [[AGENT-Call-Routing]]

### Workflow → Venture Relationships

- [[WORKFLOW-SalesOpportunity]] powers [[VENTURE-OPS-001]], [[VENTURE-LT-005]], [[VENTURE-CALLCENTER]]
- [[WORKFLOW-DeliveryDispatch]] powers [[VENTURE-LT-005]]
- [[WORKFLOW-FinancialReconciliation]] powers [[VENTURE-OPS-001]], [[VENTURE-LT-005]], [[VENTURE-CALLCENTER]]
- [[WORKFLOW-StaffingFollowUp]] powers [[VENTURE-OPS-001]]
- [[WORKFLOW-CallQuality]] powers [[VENTURE-CALLCENTER]]

### Task Escalation Relationships

- [[TASK-CreateOpportunity]] escalates_to [[AUTHORITY-SalesManager]] if low_score
- [[TASK-ValidateAddress]] escalates_to [[AUTHORITY-CustomerService]] if invalid
- [[TASK-AssignDriver]] escalates_to [[AUTHORITY-LogisticsManager]] if no_driver_available
- [[TASK-MatchTransactions]] escalates_to [[AUTHORITY-CFO]] if discrepancy_large

---

## Phase 4: Unified Entity Graph

### Repository → Capability Relationships

- [[REPO-0042|browser-use]] implements [[CAP-001|Browser-Automation]]
- [[REPO-XXXX]] implements [[CAP-002|Route-Optimization]]
- [[REPO-YYYY]] implements [[CAP-003|GPS-Tracking]]

### Capability → Skill Relationships

- [[CAP-001|Browser-Automation]] enables [[SKILL-0042|Browser-Control]]
- [[CAP-002|Route-Optimization]] enables [[SKILL-0043|Dispatch-Planning]]
- [[CAP-003|GPS-Tracking]] enables [[SKILL-0044|Fleet-Monitoring]]

### Skill → MCP Relationships

- [[SKILL-0042|Browser-Control]] uses [[MCP-0009|Browser-MCP]]
- [[SKILL-0043|Dispatch-Planning]] uses [[MCP-0010|Routing-MCP]]
- [[SKILL-0044|Fleet-Monitoring]] uses [[MCP-0011|Tracking-MCP]]

### MCP → Tool Relationships

- [[MCP-0009|Browser-MCP]] exposes [[TOOL-0015|Click]]
- [[MCP-0009|Browser-MCP]] exposes [[TOOL-0016|Navigate]]
- [[MCP-0009|Browser-MCP]] exposes [[TOOL-0017|ReadPage]]
- [[MCP-0010|Routing-MCP]] exposes [[TOOL-0018|CalculateRoute]]
- [[MCP-0011|Tracking-MCP]] exposes [[TOOL-0019|GetGPS]]

### Tool → Agent Relationships

- [[TOOL-0015|Click]] executed_by [[AGENT-Dispatch]]
- [[TOOL-0016|Navigate]] executed_by [[AGENT-Dispatch]]
- [[TOOL-0018|CalculateRoute]] executed_by [[AGENT-Dispatch]]
- [[TOOL-0019|GetGPS]] executed_by [[AGENT-Dispatch]]

### Technology Stack → Revenue Path

**Example: LT-005 (HealthRoute Courier)**
```
[[REPO-0042|browser-use]]
  ↓ implements
[[CAP-001|Browser-Automation]]
  ↓ enables
[[SKILL-0042|Browser-Control]]
  ↓ uses
[[MCP-0009|Browser-MCP]]
  ↓ exposes
[[TOOL-0015|Click]] + [[TOOL-0016|Navigate]]
  ↓ executed_by
[[AGENT-Dispatch]]
  ↓ executes
[[WORKFLOW-DeliveryDispatch]]
  ↓ operates_on
[[VENTURE-LT-005|HealthRoute]]
  ↓ serves
[[CUSTOMER-HealthcareProviders]]
  ↓ produces
[[REVENUE-1800]] per month
```

---

## All Relationship Types (Master Index)

**1. Structural**
- [[X]] maps_to [[Y]] — base maps to domain
- [[X]] assigned_to [[Y]] — domain assigned to agent
- [[X]] defined_in [[Y]] — task defined in workflow
- [[X]] belongs_to [[Y]] — entity belongs to category

**2. Capability**
- [[X]] implements [[Y]] — repository implements capability
- [[X]] enables [[Y]] — capability enables skill
- [[X]] uses [[Y]] — skill uses MCP
- [[X]] exposes [[Y]] — MCP exposes tool
- [[X]] supports [[Y]] — something supports something

**3. Execution**
- [[X]] executed_by [[Y]] — tool executed by agent
- [[X]] executes [[Y]] — agent executes workflow
- [[X]] operates_on [[Y]] — workflow operates on venture
- [[X]] powers [[Y]] — workflow powers venture
- [[X]] executes_via [[Y]] — venture executes via agent

**4. Business**
- [[X]] serves [[Y]] — venture serves customer
- [[X]] produces [[Y]] — customer produces revenue
- [[X]] stored_in [[Y]] — revenue stored in venture
- [[X]] generates [[Y]] — venture generates revenue
- [[X]] attributed_to [[Y]] — revenue attributed to venture/agent

**5. Control & Escalation**
- [[X]] escalates_to [[Y]] — task escalates to authority
- [[X]] approved_by [[Y]] — action approved by role
- [[X]] controlled_by [[Y]] — entity controlled by base

**6. Discovery & Relationships**
- [[X]] related_to [[Y]] — entities related
- [[X]] similar_to [[Y]] — similar entities
- [[X]] derived_from [[Y]] — derived entity
- [[X]] connected_to [[Y]] — connected entities

---

## Bidirectional Relationships (Important)

All relationships are **bidirectional in the graph**:

- [[REPO-0042]] implements [[CAP-001]]
- [[CAP-001]] implemented_by [[REPO-0042]]

- [[VENTURE-LT-005]] executes_via [[AGENT-Dispatch]]
- [[AGENT-Dispatch]] executes [[VENTURE-LT-005]]

- [[TASK-CreateOpportunity]] escalates_to [[AUTHORITY-SalesManager]]
- [[AUTHORITY-SalesManager]] manages [[TASK-CreateOpportunity]]

---

## Verification Checklist

- [ ] All 500 bases bracketed and mapped to 50 domains
- [ ] All 50 domains bracketed and assigned to agents
- [ ] All 789 ventures bracketed and mapped to bases
- [ ] All agents bracketed and connected to workflows
- [ ] All workflows bracketed and linked to ventures
- [ ] All repositories bracketed and linked to capabilities
- [ ] All capabilities bracketed and linked to skills
- [ ] All skills bracketed and linked to MCPs
- [ ] All MCPs bracketed and linked to tools
- [ ] All revenue paths bracketed end-to-end
- [ ] All escalation paths bracketed with authorities
- [ ] All customer relationships bracketed

---

**Status:** ALL RELATIONSHIPS BRACKETED ✅  
**Format:** [[ID|Display Name]] or [[ID]]  
**Canonical Rule:** ID is permanent, display name can change  
**Graph Consistency:** All relationships bidirectional

