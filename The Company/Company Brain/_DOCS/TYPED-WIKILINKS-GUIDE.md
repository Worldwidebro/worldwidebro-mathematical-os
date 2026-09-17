# Typed Wiki Links Guide

**Document ID:** TYPED-WIKILINKS-001  
**Updated:** 2026-09-17  
**Purpose:** Human-readable authoring layer for Company Brain knowledge graph  
**Canonical Format:** [[_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml]] (RDF/XML)

---

## Overview

The Company Brain uses **typed wiki links** to make relationship semantics explicit instead of leaving every link unlabeled.

Instead of:
```markdown
[[Some Page]]
```

Use:
```markdown
relationship::[[Some Page]]
```

This makes edges in the knowledge graph **named and queryable**.

---

## Relationship Vocabulary (15 Families)

### 1. ORGANIZATION RELATIONSHIPS

```markdown
belongs-to-domain::[[Purpose Domain]]
governed-by-control-plane::[[CP-001: Identity Control Plane]]
belongs-to::[[Worldwidebro Holdings]]
```

### 2. BUSINESS RELATIONSHIPS

```markdown
enables-venture::[[LT-005: Medical Courier]]
offers::[[Product: Delivery Service]]
targets::[[Customer Segment: Healthcare Facilities]]
generates-revenue::[[Revenue Stream: Delivery Fees]]
```

### 3. AGENT RELATIONSHIPS

```markdown
executes-logic::[[Logic-031: Agent Logic]]
governed-by-agent::[[Operations Agent]]
capable-of::[[Capability: Workflow Orchestration]]
uses-tool::[[Tool: ClickUp API]]
uses-model::[[Model: Claude Haiku 4.5]]
uses-prompt::[[Prompt: Agent Directive for Operations]]
reads-knowledge::[[Knowledge: Current Inventory State]]
writes-knowledge::[[Knowledge: Order Fulfillment Status]]
delegates-to-agent::[[Research Agent]]
escalates-to-agent::[[Strategic Agent]]
collaborates-with-agent::[[Finance Agent]]
supervised-by-agent::[[Orchestrator Agent]]
```

### 4. CAPABILITY RELATIONSHIPS

```markdown
implemented-by-repository::[[Repository: worldwidebro-dispatch]]
requires-capability::[[Capability: Real-time Tracking]]
enables-venture::[[LT-005]]
depends-on-capability::[[Capability: Customer Authentication]]
```

### 5. SOFTWARE RELATIONSHIPS

```markdown
powers-venture::[[LT-005: Medical Courier]]
contains-code-for::[[Application: Courier Dispatch API]]
depends-on-repository::[[Repository: worldwidebro-routing]]
tested-by-evaluation::[[Evaluation: E2E Courier Tests]]
exposes::[[API: /v1/dispatch]]
calls::[[API: Google Maps Routing]]
deployed-to::[[Infrastructure: Vercel Production]]
```

### 6. WORKFLOW RELATIONSHIPS

```markdown
triggered-by-event::[[Event: New Order Received]]
has-step::[[Workflow: Validate Order Details]]
has-step::[[Workflow: Assign Driver]]
has-step::[[Workflow: Track Delivery]]
produces-output::[[Knowledge: Delivery Confirmation]]
executes-workflow::[[Workflow: Order Fulfillment]]
orchestrates::[[Workflow: Multi-Stop Delivery]]
```

### 7. BUSINESS LOGIC RELATIONSHIPS

```markdown
constrained-by-policy::[[Policy: Maximum Delivery Distance]]
constrained-by-policy::[[Policy: Driver Safety Requirements]]
requires-approval::[[CP-021: Revenue Control Plane]]
applies-to-venture::[[LT-005]]
determined-by::[[Rule: Dynamic Pricing Algorithm]]
```

### 8. DECISION RELATIONSHIPS

```markdown
made-by-agent::[[Operations Agent]]
based-on-logic::[[Logic-026: Routing Logic]]
supported-by-knowledge::[[Knowledge: Current Capacity]]
results-in-action::[[Workflow: Dispatch Assignment]]
approved-by::[[CP-027: Dispatch Control Plane]]
```

### 9. KNOWLEDGE RELATIONSHIPS

```markdown
documents::[[Logic-006: Revenue Logic]]
references::[[Venture: LT-005]]
derived-from::[[Evaluation: Q3 Performance Review]]
supports-decision::[[Decision: Price Adjustment]]
verified-by::[[Evaluation: Data Validation Report]]
contradicts::[[Knowledge: Previous Market Assumption]]
```

### 10. STATE & EVENT RELATIONSHIPS

```markdown
has-state::[[State: Order Pending]]
triggered-by-event::[[Event: Driver Accepted]]
changes-state::[[State: In Transit]]
caused-by::[[Action: Driver Location Update]]
observed-by::[[Agent: Tracking Agent]]
produces-event::[[Event: Delivery Completed]]
```

### 11. EVALUATION RELATIONSHIPS

```markdown
evaluated-by::[[Evaluation: Agent Performance Report]]
measures::[[Metric: Average Delivery Time]]
validated-by::[[Evaluation: Customer Satisfaction Survey]]
tested-by-evaluation::[[Evaluation: Integration Tests]]
learned-from::[[Result: High Cancellation Rate]]
```

### 12. DEPENDENCY RELATIONSHIPS

```markdown
depends-on::[[Repository: worldwidebro-auth]]
requires::[[Tool: Stripe Payment API]]
enabled-by::[[Infrastructure: Docker Cluster]]
extends::[[Capability: Basic Delivery]]
replaces::[[Legacy System: Manual Dispatch]]
supersedes::[[Version 1.0 API]]
```

### 13. TEMPORAL RELATIONSHIPS

```markdown
created-from::[[Template: Venture Template v2]]
version-of::[[Product: Courier v2.1]]
superseded-by::[[Policy v2: Updated Safety Requirements]]
deprecated-by::[[Tool: Mapbox (switched to Google Maps)]]
```

### 14. GOVERNANCE RELATIONSHIPS

```markdown
governed-by::[[Policy: Data Privacy]]
authorized-by::[[Permission: Admin Dashboard Access]]
overrides::[[Previous Rule: Delivery Distance Limit]]
follows::[[Process: Standard QA Checklist]]
```

### 15. LEARNING RELATIONSHIPS

```markdown
learned-from::[[Result: A/B Test Showed 15% Improvement]]
improved-by::[[Experiment: New Pricing Model]]
iterated-from::[[Version 1: Initial Release]]
informed-by::[[Research: Market Analysis 2026]]
```

---

## Example: Logic Layer Markdown

```markdown
---
id: logic-006
type: logic-layer
name: Revenue Logic
layer-number: 6
control-plane: CP-006
domain: Business Domain
---

# Logic-006: Revenue Logic

**Core Question:** How do we turn activity into revenue?

## Domain

belongs-to-domain::[[Business Domain]]

## Governance

governed-by-control-plane::[[CP-006: Revenue Control Plane]]

## Execution

governs::[[Agent: Revenue Loop Agent]]

## Related Logics

depends-on-logic::[[Logic-008: Customer Logic]]
depends-on-logic::[[Logic-009: Sales Logic]]
depends-on-logic::[[Logic-007: Pricing Logic]]

## Constraints

constrained-by-policy::[[Policy: Revenue Recognition Standards]]
constrained-by-policy::[[Policy: Financial Reporting Requirements]]

## Knowledge Base

uses-knowledge::[[Knowledge: Customer Acquisition Costs]]
uses-knowledge::[[Knowledge: Lifetime Value Models]]
produces-knowledge::[[Knowledge: Revenue Forecasts]]

## Workflows

controls::[[Workflow: Lead to Cash]]
controls::[[Workflow: Subscription Renewal]]
controls::[[Workflow: Upsell Detection]]

## Measurements

measured-by::[[Metric: MRR (Monthly Recurring Revenue)]]
measured-by::[[Metric: Customer Acquisition Cost]]
measured-by::[[Metric: Churn Rate]]
measured-by::[[Metric: Lifetime Value]]

## Evaluation

evaluated-by::[[Evaluation: Revenue Model Validation]]
validated-by::[[Evaluation: Financial Audit]]

## Implementation

implemented-by-agent::[[Agent: Revenue Loop Agent]]

## Related Ventures

enables-venture::[[LT-005: Medical Courier]]
enables-venture::[[OPS-001: Staffing]]
enables-venture::[[RE-001: Real Estate Investment]]

## References

documents::[[Document: Revenue Playbook]]
references::[[Document: Pricing Strategy Guide]]

---

## How Revenue Happens

1. **Customer enters funnel** (Logic-008: Customer Logic)
2. **Sales process begins** (Logic-009: Sales Logic)
3. **Price is calculated** (Logic-007: Pricing Logic)
4. **Revenue is recognized** (Logic-006: Revenue Logic) ← YOU ARE HERE
5. **Payment is collected** (Logic-021: Financial Logic)
6. **Customer is retained** (Logic-010: Customer Success Logic)

## Agents Responsible

- operates::[[Agent: Revenue Loop Agent]] — Primary executor
- supervised-by::[[Agent: Finance Control Agent]] — Oversight
- escalates-to::[[Agent: CFO Agent]] — Decision exceptions

## Policies Governing

- Policy: Revenue Recognition Standards (GAAP compliance)
- Policy: Pricing Transparency (FTC regulations)
- Policy: Payment Processing Security (PCI-DSS)

## Tools Used

- uses-tool::[[CRM: Salesforce or Supabase]]
- uses-tool::[[Billing: Stripe or custom billing engine]]
- uses-tool::[[Analytics: Mixpanel or custom dashboard]]

## What Breaks

If this logic fails:
- depends-on-logic::[[Logic-008]] → Ventures have no customers
- depends-on-logic::[[Logic-009]] → Sales process breaks
- depends-on-logic::[[Logic-007]] → Pricing undefined
- depends-on-logic::[[Logic-021]] → Payments not collected

## Last Updated

verified-by::[[Evaluation: Q3 Revenue Audit]]
updated-at::2026-09-17
updated-by::Finance Agent
confidence::0.98
```

---

## Example: Agent Markdown

```markdown
---
id: agent-revenue-loop
type: agent
name: Revenue Loop Agent
domain: Business Domain
control-plane: CP-006
---

# Revenue Loop Agent

**Purpose:** Ensure revenue moves from opportunity to cash and retention.

## Relations

### Logic Execution
executes-logic::[[Logic-006: Revenue Logic]]
governed-by-control-plane::[[CP-006: Revenue Control Plane]]

### Capabilities
capable-of::[[Capability: Lead Scoring]]
capable-of::[[Capability: Revenue Forecasting]]
capable-of::[[Capability: Customer Segmentation]]

### Tools
uses-tool::[[Stripe API]]
uses-tool::[[Salesforce CRM]]
uses-tool::[[Mixpanel Analytics]]

### Model & Prompts
uses-model::[[Model: Claude Sonnet 5]]
uses-prompt::[[Prompt: Revenue Forecasting Directive]]

### Knowledge
reads-knowledge::[[Knowledge: Customer Acquisition Costs]]
reads-knowledge::[[Knowledge: Pricing Tiers]]
writes-knowledge::[[Knowledge: Revenue Forecasts]]

### Workflows
executes-workflow::[[Workflow: Lead to Cash]]
executes-workflow::[[Workflow: Subscription Renewal]]
orchestrates::[[Workflow: Upsell Detection]]

### Escalation
escalates-to-agent::[[Agent: Finance Control Agent]]
delegates-to-agent::[[Agent: Payment Processing Agent]]

### Evaluation
evaluated-by::[[Evaluation: Revenue Agent Performance]]
validated-by::[[Evaluation: Revenue Projection Accuracy]]

### Ventures
serves::[[LT-005: Medical Courier]]
serves::[[OPS-001: Staffing]]
serves::[[RE-001: Real Estate]]

## Workflow

1. **Monitor** → reads-knowledge::[[Knowledge: New Opportunities]]
2. **Analyze** → capable-of::[[Capability: Lead Scoring]]
3. **Forecast** → produces-knowledge::[[Knowledge: Revenue Forecast]]
4. **Process** → uses-tool::[[Stripe API]]
5. **Track** → writes-knowledge::[[Knowledge: Payment Status]]
6. **Report** → evaluated-by::[[Evaluation: Monthly Revenue Report]]

## What This Agent Does (In Plain English)

The Revenue Loop Agent is responsible for ensuring that customer interest turns into committed cash flow. It:

- **Scores leads** to identify high-probability sales
- **Forecasts revenue** to inform strategy and capital decisions
- **Processes payments** via Stripe or alternative gateways
- **Tracks collections** and flags at-risk payments
- **Segments customers** by value and retention risk
- **Detects upsell opportunities** to grow customer value
- **Reports** monthly, quarterly, and annually to finance

## Decision Authority

This agent has autonomous authority (L2-L3) to:
- ✅ Approve discounts up to 15%
- ✅ Retry failed payments (up to 3 attempts)
- ✅ Segment customers and create cohorts
- ❓ Pricing changes > 10% (requires CP-006 approval)
- ❌ Write-off unpaid invoices (requires CP-021 approval)

## Control Plane

governed-by-control-plane::[[CP-006: Revenue Control Plane]]

**CP-006 responsibilities:**
- Approves pricing policies
- Monitors revenue accuracy
- Authorizes revenue recognition policy changes
- Handles escalated payment exceptions

## Testing & Validation

tested-by-evaluation::[[Evaluation: Revenue Agent E2E Tests]]
- Revenue projection accuracy: 95%+
- Payment success rate: 99.5%+
- Customer segmentation consistency: 98%+

---

Last updated: 2026-09-17 | Confidence: 0.98 | Verified by: Finance Control Agent
```

---

## How to Use This in Your Wiki

1. **In Markdown frontmatter**, declare the entity type:
   ```yaml
   ---
   id: logic-006
   type: logic-layer
   wiki: true
   ---
   ```

2. **Use typed wikilinks throughout** the document:
   ```markdown
   belongs-to-domain::[[Business Domain]]
   governs::[[Agent: Revenue Loop Agent]]
   constrained-by-policy::[[Policy: GAAP Revenue Recognition]]
   ```

3. **Graph importer parses** the Markdown:
   - Extracts `subject-id` (frontmatter `id`)
   - Extracts `predicate` (relationship type before `::`)
   - Extracts `object-id` (entity in `[[...]]`)
   - Creates RDF triple: `(subject, predicate, object)`

4. **Triple flows to Neo4j**:
   ```cypher
   CREATE (logic006:LogicLayer {id: "logic-006", name: "Revenue Logic"})
   CREATE (cp006:ControlPlane {id: "cp-006"})
   CREATE (logic006)-[:GOVERNED_BY_CONTROL_PLANE]->(cp006)
   ```

---

## Ingestion Pipeline

```
MARKDOWN FILES
    ↓
EXTRACT FRONTMATTER (id, type)
    ↓
PARSE TYPED WIKILINKS (relationship::[[target]])
    ↓
BUILD TUPLES (subject, predicate, object)
    ↓
RESOLVE REFERENCES (find target by name/wiki-link)
    ↓
CREATE RDF TRIPLES
    ↓
VALIDATE AGAINST ONTOLOGY
    ↓
WRITE TO NEO4J
    ↓
OPTIONAL: INDEX IN QDRANT (semantic search)
```

---

## Benefits

✅ **Human-readable** — Markdown is easy to author and review  
✅ **Machine-queryable** — Typed edges create explicit graph semantics  
✅ **Version-controlled** — Lives in Git alongside code  
✅ **Decentralized** — Markdown files can be authored anywhere  
✅ **Canonical** — XML/RDF is the source of truth for imports  
✅ **Auditable** — Every relationship has provenance metadata  

---

## References

- Master Ontology: [[_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml]]
- Logic Layers Registry: [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]]
- Agent Definitions: [[16-AGENTS/AGENT-DIRECTIVES.yaml]]
- Graph Ingestion: [[_PIPELINES/GRAPH-INGESTION-PIPELINE.md]]

