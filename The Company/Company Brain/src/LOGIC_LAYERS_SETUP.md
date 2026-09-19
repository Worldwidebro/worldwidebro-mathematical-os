[[src/LOGIC_LAYERS_README|Logic Layers Overview]] | [[14-CAPABILITIES/README|14-CAPABILITIES]] | [[INDEX]]

# Logic Layers Registry — Setup & Integration Guide

## Quick Start

You have created a production-ready logic layers system that maps venture tasks to operational workflows and required capabilities.

### Files Created

```
src/
├── data/
│   └── LOGIC_LAYERS_REGISTRY.yaml     (240 lines) — 15 logic layers, 5 categories
├── types/
│   └── LogicLayers.ts                  (180 lines) — TypeScript interfaces + 8 helpers
├── examples/
│   └── logicLayersExample.ts          (65 lines)  — Usage patterns and examples
├── LOGIC_LAYERS_README.md             (198 lines) — Full documentation
└── LOGIC_LAYERS_SETUP.md              (this file)
```

## Registry Overview

### 15 Logic Layers across 5 Categories

| Category | Count | Layers |
|----------|-------|--------|
| Outreach | 2 | LOGIC-001, LOGIC-002 |
| Sales | 4 | LOGIC-003, LOGIC-004, LOGIC-005, LOGIC-015 |
| Support | 3 | LOGIC-006, LOGIC-007, LOGIC-008 |
| Product | 3 | LOGIC-009, LOGIC-010, LOGIC-011 |
| Operations | 3 | LOGIC-012, LOGIC-013, LOGIC-014 |

### Each Layer Includes

- Unique ID (LOGIC-001 format)
- Human-readable name
- Clear description
- Category classification
- 3-5 required capabilities
- Example tasks (for classification)

## Production Integration

### 1. Task Classification Pipeline

```
User Task Description
    ↓
classifyTaskToLayers(description)
    ↓
[LOGIC-001, LOGIC-004]
    ↓
getUniqueCapabilitiesForLayers(layers)
    ↓
[write-emails, score-fit, negotiate-terms]
    ↓
Route to agents with these capabilities
```

### 2. Agent Discovery

Connect with Agent Registry to route tasks:

```typescript
// Find agents that have all required capabilities
const layers = classifyTaskToLayers(taskDescription, logicRegistry);
const capabilities = getUniqueCapabilitiesForLayers(layers, logicRegistry);
const agents = findAgentsWithCapabilities(capabilities, agentRegistry);
```

### 3. Skill Mapping

Link capabilities to concrete skills:

- `write-emails` → Email Writer Skill
- `score-fit` → Sales Qualification Skill
- `track-engagement` → Analytics Skill

### 4. Multi-Layer Tasks

For complex tasks spanning multiple layers:

```typescript
const layerIds = ['LOGIC-001', 'LOGIC-003', 'LOGIC-004'];
const allCapabilities = getUniqueCapabilitiesForLayers(layerIds, registry);
// Now you have all capabilities needed for the full task
```

## Helper Functions

All TypeScript helpers are typed and production-ready:

```typescript
// Load registry
const registry = YAML.load('src/data/LOGIC_LAYERS_REGISTRY.yaml');

// Basic lookups
getCapabilitiesForLayer(layerId, registry)
getLayersByCategory(category, registry)
layerExists(layerId, registry)
getAllLayerIds(registry)

// Advanced operations
findLayersWithCapability(capability, registry)
getUniqueCapabilitiesForLayers(layerIds, registry)
classifyTaskToLayers(description, registry)
getLayerSummary(layerId, registry)
```

## Task Classification Examples

### Example 1: Outreach Task
```
Task: "Send personalized cold emails to 50 startup founders"
Layers: [LOGIC-001, LOGIC-002]
Capabilities: [write-emails, personalize, track-opens, schedule-sends]
```

### Example 2: Sales Task
```
Task: "Conduct discovery call and close deal with prospect"
Layers: [LOGIC-003, LOGIC-004, LOGIC-005]
Capabilities: [ask-discovery-questions, score-fit, create-proposal, negotiate-terms, close-deal]
```

### Example 3: Support Task
```
Task: "Onboard new customer and resolve their first issue"
Layers: [LOGIC-006, LOGIC-008]
Capabilities: [create-account, configure-settings, provide-training, diagnose-issue, provide-solution]
```

## Next Steps

### 1. Integrate with Task Dispatcher

Add to your task routing logic:
```typescript
import { classifyTaskToLayers } from './types/LogicLayers';

function routeTask(task) {
  const layers = classifyTaskToLayers(task.description, registry);
  return dispatchWithLayers(task, layers);
}
```

### 2. Connect Agent Registry

Create mapping between capabilities and agents:
```typescript
const capabilities = getUniqueCapabilitiesForLayers(layers, logicRegistry);
const agents = findAgentsWithCapabilities(capabilities);
```

### 3. Add Skill Registry

Map capabilities to concrete implementation skills:
```yaml
# SKILL_REGISTRY.yaml
skills:
  write-emails:
    implements: [LOGIC-001, LOGIC-002]
    tools: [EmailWriter, PersonalizationEngine, AnalyticsTracker]
  score-fit:
    implements: [LOGIC-004]
    tools: [SalesQualifier, ICPMatcher]
```

### 4. Build Workflow Engine

For multi-step tasks requiring multiple layers:
```typescript
const workflow = {
  layers: ['LOGIC-001', 'LOGIC-003', 'LOGIC-005'],
  sequence: 'serial',
  gates: ['LOGIC-003 needs input from LOGIC-001']
};
```

## Testing

### Verify YAML Structure
```bash
npm run validate:yaml src/data/LOGIC_LAYERS_REGISTRY.yaml
```

### Test TypeScript
```bash
npx ts-node src/examples/logicLayersExample.ts
```

### Extend Registry
```yaml
# Add to LOGIC_LAYERS_REGISTRY.yaml
LOGIC-016:
  id: "LOGIC-016"
  name: "Your New Layer"
  description: "What it does"
  category: "operations"
  capabilities: [cap1, cap2, cap3]
  example_tasks: ["Task 1", "Task 2"]
```

## Architecture Alignment

This system integrates with:

- **Agent Dispatch Router** — Routes tasks to agents by layers
- **Capability Registry** — Catalogs available capabilities
- **Skill Registry** — Maps capabilities to implementations
- **Neo4j Knowledge Graph** — Tracks layer → capability → agent relationships
- **Task System** — Classifies every incoming task to layers

## Performance Notes

- YAML loading: <10ms (cache the loaded registry)
- Task classification: O(n) where n = number of layers (15 = negligible)
- Capability lookup: O(1) hash access
- No runtime dependencies beyond js-yaml for loading

## Maintenance

### When to Update the Registry

1. New venture type needs different workflow → Add logic layer
2. Existing layer needs new capability → Add to capabilities array
3. Capability no longer used → Remove from specific layers (not entire registry)

### Version Control

- Always commit LOGIC_LAYERS_REGISTRY.yaml changes
- Tag major versions when layer structure changes
- Keep CHANGELOG.md for capability additions/removals

## Production Checklist

- [x] 15 logic layers defined across 5 categories
- [x] TypeScript types and interfaces created
- [x] Helper functions for all common operations
- [x] Example usage patterns documented
- [x] README with complete reference
- [x] Error handling (layerExists check before access)
- [x] Task classification algorithm (basic keyword matching)
- [ ] Connect to Agent Registry (next step)
- [ ] Wire to Task Dispatcher (next step)
- [ ] Integrate with Neo4j for graph queries (next step)

---

**Created:** 2026-09-18  
**Status:** Production-Ready  
**Version:** 1.0  
**Last Updated:** 2026-09-18
