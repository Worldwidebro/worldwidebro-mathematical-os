---
name: AI-BRAIN/ONTOLOGY
title: WORLDWIDEBRO SEMANTIC ONTOLOGY v1.0
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# WORLDWIDEBRO SEMANTIC ONTOLOGY v1.0

**Purpose:** Canonical vocabulary for Obsidian, Neo4j, agents, and all systems.  
**Status:** Active  
**Last Updated:** 2026-08-04  
**Scope:** All entities, relationships, tags, and properties

---

## CORE PRINCIPLE

- **Folders** → human navigation
- **Type** → what something *is*
- **Tags** → state/lifecycle/classification
- **Wiki-links** → relationships (DO NOT use tags for relationships)
- **Properties** → structured facts
- **Neo4j** → machine-readable relationship graph

---

## 1. CANONICAL TYPES

```yaml
# Business/Economic
asset
venture
company
brand
product
service
market
customer
person
organization

# Software/Technology
software
repository
application
api
library
database
infrastructure
device

# Knowledge/Intelligence
knowledge
document
research
concept
methodology
playbook
policy
procedure
dataset
model

# AI/Execution
capability
skill
agent
workflow
tool
mcp
prompt

# Management
project
task
decision
directive
objective
experiment

# Opportunity/Risk
opportunity
problem
risk
dependency
synergy

# Financial
transaction
lead
deal
contract
order
revenue
expense
investment

# Event/Source
event
meeting
communication
source
claim
```

---

## 2. RELATIONSHIP FAMILIES (10 canonical types)

### IDENTITY
```
same-as
alias-of
duplicate-of
version-of
derived-from
replaced-by
supersedes
```

### OWNERSHIP
```
owned-by
managed-by
created-by
maintained-by
licensed-by
licensed-to
operated-by
```

### STRUCTURE
```
part-of
contains
component-of
parent
child
sibling
```

### DEPENDENCY
```
requires
depends-on
enables
prerequisite-for
blocked-by
```

### CAPABILITY
```
has-capability
implements
provides
exposes
uses
fulfills
```

### EXECUTION
```
executes
orchestrates
delegates-to
routes-to
triggers
verifies
recovers-with
completes
```

### KNOWLEDGE
```
explains
supports
contradicts
evidence-for
evidence-against
references
summarizes
related-to
example-of
instance-of
```

### BUSINESS
```
serves
sells-to
sold-by
competes-with
partners-with
supplies
purchases-from
supports
operates-in
targets
belongs-to-market
belongs-to-sector
```

### ECONOMIC
```
monetizes
monetized-by
generates-revenue
generates-cost
creates-value
unlocks
cross-sells
upsells
bundles-with
increases-margin
reduces-cost
```

### EVOLUTION
```
improves
optimizes
learns-from
replaces
evolves-into
deprecates
```

---

## 3. LIFECYCLE TAGS (use exactly one)

```yaml
#status/idea
#status/research
#status/planned
#status/building
#status/testing
#status/staged
#status/active
#status/paused
#status/deprecated
#status/archived
#status/failed
```

---

## 4. PRIORITY TAGS

```yaml
#priority/p0        # Critical blocker
#priority/p1        # High impact
#priority/p2        # Normal
#priority/p3        # Low/future
```

---

## 5. HEALTH TAGS

```yaml
#health/healthy
#health/degraded
#health/blocked
#health/broken
#health/unknown
```

---

## 6. KNOWLEDGE QUALITY TAGS

```yaml
#knowledge/current         # Recently verified
#knowledge/stale           # Not verified in 30+ days
#knowledge/unverified      # Never verified
#knowledge/conflicted      # Contradicts another source
#knowledge/incomplete      # Missing key information
#knowledge/obsolete        # Known to be outdated
```

---

## 7. CANONICAL PROPERTIES

Every important note should have:

```yaml
---
id: unique-identifier
type: venture|software|capability|agent|etc
name: human-readable name
status: active|paused|archived
owner: "[[Worldwidebro]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: github|planning|discovery|etc
observed_at: YYYY-MM-DD
verified_at: YYYY-MM-DD
confidence: 0.0-1.0
freshness: current|stale|unknown
---
```

---

## 8. STANDARD NOTE TEMPLATE

Use for any important entity:

```markdown
# [Entity Name]

## Identity
What is this thing?

## Type
`venture` (from canonical types)

## Status
#status/active

## Owner
- [[Worldwidebro]]

## Portfolio
- [[VEX]] or [[IZA OS]] or [[AI-BOSS]]

## Purpose
Why does it exist?

## Capabilities
- [[Capability 1]]
- [[Capability 2]]

## Dependencies
- [[Dependency 1]]
- [[Dependency 2]]

## Used By
- [[User 1]]

## Enables
- [[Enabled Thing]]

## Synergies
- [[Related Entity]]

## Monetization
How does this create value?

## Evidence
- [[Supporting Document]]

## Related
- [[Related Entity]]

## Provenance
Source: [[GitHub]] or [[Planning]]
Observed: YYYY-MM-DD
Verified: YYYY-MM-DD
Confidence: 0.92
```

---

## 9. WIKI-LINK EXAMPLES

Use in markdown; they generate Neo4j relationships:

```markdown
## Capabilities
- [[Dispatch]]
- [[Routing]]

## Dependencies
- [[STA-001]]
- [[Healthcare Compliance]]

## Synergies
- [[STA-001]] (shares staffing)
- [[LT-011]] (shares dispatch)

## Monetization
- [[Courier Service Revenue]]
```

Each link + context → Neo4j relationship:
- Context `## Capabilities` + `[[Dispatch]]` → `has-capability`
- Context `## Dependencies` + `[[STA-001]]` → `depends-on`
- Context `## Synergies` + `[[STA-001]]` → `synergy-with`

---

## 10. FOLDER STRUCTURE (human navigation only)

```
DIRECTIVES/
├── mission/
├── goals/
├── objectives/
├── principles/
├── constraints/
└── economic-model/

EXECUTIVES/
├── decisions/
├── policies/
├── priorities/
├── strategies/
└── control-loops/

PROJECTS/
├── ventures/
├── software/
├── products/
├── research/
├── infrastructure/
└── experiments/

AI-BRAIN/
├── knowledge/
├── capabilities/
├── agents/
├── skills/
├── mcp/
├── workflows/
├── graph/
├── memory/
└── provenance/
```

**DO NOT** create `CUSTOMERS/`, `MARKETS/`, `CAPABILITIES/`, etc. as parallel trees. Those entities live in the **graph**, accessed via queries.

---

## 11. VALIDATION RULES

Before creating any new entity:

1. Does it already exist in Neo4j?
2. Is the type from CANONICAL TYPES?
3. Does it have an owner?
4. Can you verify it (verified_at, confidence)?
5. Is it worth a new entity or should it be a relationship to existing entity?

---

## 12. ENFORCEMENT

This ontology is **not optional**. All entities must:

- Have `type` from canonical list
- Have `id`, `name`, `status`, `owner`
- Have `verified_at`, `confidence`
- Use wiki-links for relationships (not tags)
- Use tags only for lifecycle/priority/health/knowledge-quality
- Follow standard template

Violations flag as **identity resolution tasks** in the decision engine.

---

**Version:** 1.0  
**Effective:** 2026-08-04  
**Authority:** CLAUDE.md  
**Next Review:** 2026-09-04
