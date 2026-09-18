# Logic Layers Registry

The Logic Layers Registry maps venture tasks to operational workflows and required capabilities.

## Files

- **`src/data/LOGIC_LAYERS_REGISTRY.yaml`** — The authoritative registry (15 logic layers across 5 categories)
- **`src/types/LogicLayers.ts`** — TypeScript interfaces and helper functions
- **`src/examples/logicLayersExample.ts`** — Example usage patterns

## What are Logic Layers?

Logic Layers represent the core operational workflows that run your ventures:

| Category | Layers | Purpose |
|----------|--------|---------|
| **Outreach** | LOGIC-001, LOGIC-002 | Finding and contacting prospects |
| **Sales** | LOGIC-003, LOGIC-004, LOGIC-005, LOGIC-015 | Qualifying and closing deals |
| **Support** | LOGIC-006, LOGIC-007, LOGIC-008 | Customer success and retention |
| **Product** | LOGIC-009, LOGIC-010, LOGIC-011 | Feedback, prioritization, analytics |
| **Operations** | LOGIC-012, LOGIC-013, LOGIC-014 | Automation, reporting, optimization |

## How to Use

### 1. Load the Registry

```typescript
import yaml from 'js-yaml';
import fs from 'fs';

const registryYaml = fs.readFileSync('src/data/LOGIC_LAYERS_REGISTRY.yaml', 'utf-8');
const registry = yaml.load(registryYaml) as LogicLayersRegistry;
```

### 2. Get Capabilities for a Layer

```typescript
import { getCapabilitiesForLayer } from 'src/types/LogicLayers';

const capabilities = getCapabilitiesForLayer('LOGIC-001', registry);
// Returns: ['write-emails', 'personalize', 'track-opens', ...]
```

### 3. Classify a Task

```typescript
import { classifyTaskToLayers } from 'src/types/LogicLayers';

const task = "Send cold email to startup founders";
const layers = classifyTaskToLayers(task, registry);
// Returns: ['LOGIC-001', 'LOGIC-002']
```

### 4. Get All Layers in a Category

```typescript
import { getLayersByCategory } from 'src/types/LogicLayers';

const salesLayers = getLayersByCategory('sales', registry);
// Returns array of all sales-related layers
```

### 5. Find Layers with a Specific Capability

```typescript
import { findLayersWithCapability } from 'src/types/LogicLayers';

const layers = findLayersWithCapability('write-emails', registry);
// Returns all layers that require email writing
```

## Task Classification Pipeline

The typical workflow integrates logic layers into your task system:

```
Task Description
    ↓
classifyTaskToLayers() → [LOGIC-001, LOGIC-002]
    ↓
getUniqueCapabilitiesForLayers() → [write-emails, personalize, track-engagement]
    ↓
Dispatch to agents with required capabilities
```

## Logic Layers Reference

### Outreach (2 layers)

- **LOGIC-001: Cold Outreach** — Initial contact with prospects
  - Capabilities: write-emails, personalize, track-opens, handle-unsubscribes, find-contact-info

- **LOGIC-002: Email Sequencing** — Multi-touch campaigns and follow-ups
  - Capabilities: write-emails, schedule-sends, personalize, track-engagement, handle-bounces

### Sales (4 layers)

- **LOGIC-003: Sales Discovery** — Uncover prospect needs
  - Capabilities: ask-discovery-questions, listen-actively, map-current-state, identify-pain-points, qualify-budget

- **LOGIC-004: Sales Qualification** — Determine if prospect is qualified
  - Capabilities: score-fit, evaluate-budget, assess-authority, check-timeline, handle-objections

- **LOGIC-005: Proposal & Closing** — Create solutions and close deals
  - Capabilities: design-solution, create-proposal, handle-objections, negotiate-terms, close-deal

- **LOGIC-015: Customer Retention & Expansion** — Grow existing customer relationships
  - Capabilities: monitor-health, identify-expansion-opportunities, conduct-qbr, create-growth-plan, track-renewals

### Support (3 layers)

- **LOGIC-006: Customer Onboarding** — Set up new customers
  - Capabilities: create-account, configure-settings, provide-training, assign-resources, track-adoption

- **LOGIC-007: Support Ticketing** — Create and route support tickets
  - Capabilities: create-ticket, categorize-issue, assign-priority, route-to-team, track-status

- **LOGIC-008: Issue Resolution** — Troubleshoot and fix problems
  - Capabilities: diagnose-issue, provide-solution, test-fix, document-resolution, follow-up

### Product (3 layers)

- **LOGIC-009: Product Feedback Collection** — Gather customer feedback
  - Capabilities: ask-feedback-questions, record-feedback, categorize-feedback, identify-patterns, route-to-team

- **LOGIC-010: Feature Prioritization** — Rank feature requests
  - Capabilities: evaluate-impact, estimate-effort, score-priority, communicate-decisions, track-roadmap

- **LOGIC-011: Usage Analytics** — Track product usage
  - Capabilities: track-events, analyze-usage, identify-trends, detect-churn-risk, create-dashboards

### Operations (3 layers)

- **LOGIC-012: Data Extraction & Reporting** — Extract and report metrics
  - Capabilities: extract-data, consolidate-sources, format-reports, visualize-metrics, schedule-reports

- **LOGIC-013: Process Automation** — Automate workflows
  - Capabilities: build-workflow, integrate-systems, handle-errors, log-activity, monitor-status

- **LOGIC-014: Performance Optimization** — Improve efficiency
  - Capabilities: measure-performance, identify-bottlenecks, test-improvements, track-impact, document-changes

## Helper Functions

All exported from `src/types/LogicLayers.ts`:

| Function | Purpose |
|----------|---------|
| `getCapabilitiesForLayer(layerId, registry)` | Get capabilities for one layer |
| `getLayersByCategory(category, registry)` | Get all layers in a category |
| `findLayersWithCapability(capability, registry)` | Find layers with a capability |
| `getUniqueCapabilitiesForLayers(layerIds, registry)` | Get all capabilities across multiple layers |
| `layerExists(layerId, registry)` | Check if a layer exists |
| `getAllLayerIds(registry)` | Get all layer IDs |
| `classifyTaskToLayers(taskDescription, registry)` | Map a task to layers (basic implementation) |
| `getLayerSummary(layerId, registry)` | Get formatted layer description |

## Extending the Registry

To add a new logic layer:

1. Add entry to `LOGIC_LAYERS_REGISTRY.yaml`:
```yaml
  LOGIC-016:
    id: "LOGIC-016"
    name: "New Layer"
    description: "Description"
    category: "operations"
    capabilities:
      - capability-1
      - capability-2
    example_tasks:
      - "Example task 1"
```

2. Types automatically support any layer ID (no code change needed)

3. Test with `classifyTaskToLayers()` to verify task matching

## Best Practices

1. **Task Classification** — Always classify before dispatching
2. **Capability Checking** — Verify agents have required capabilities before assignment
3. **Category Grouping** — Use category filters for high-level task organization
4. **Documentation** — Keep example_tasks up-to-date for accurate classification

## Integration Points

- **Task Dispatch** — Use `classifyTaskToLayers()` to route tasks to agents
- **Agent Registry** — Cross-reference with agent capabilities
- **Skill Registry** — Map capabilities to specific skills
- **Workflow Engine** — Use for multi-step task orchestration

---

Last updated: 2026-09-18
Status: Production-ready
Version: 1.0
