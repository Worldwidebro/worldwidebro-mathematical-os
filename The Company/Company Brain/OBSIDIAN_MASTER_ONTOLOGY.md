---
type: knowledge-interface-ontology
canonical: true
authority: semantic-source-layer
updated_at: 2026-10-02T21:00:00Z
source_of_truth: true
---

# OBSIDIAN_MASTER_ONTOLOGY — Semantic Source Layer

**Obsidian is not a notes app. It is the human-readable semantic interface through which the Company Brain describes, reasons about, updates, and verifies itself.**

This is the bridge between reality (what actually exists and changes) and the machine systems (graph, registries, agents, automations) that govern the organization.

---

## [OBSIDIAN_ROLE]

Obsidian serves four critical functions:

1. **Human Interface** — Where humans read, write, and reason about the system
2. **Semantic Layer** — Where reality becomes metadata (brackets, wiki links, frontmatter)
3. **Knowledge Source** — Where facts are captured before they become graph edges
4. **Feedback Loop** — Where outcomes are recorded and learning is captured

```
[REALITY]
    ↓
[HUMAN_OBSERVATION]
    ↓
[MARKDOWN_CAPTURE]
    ↓
[BRACKETED_SEMANTICS]
    ↓
[WIKI_LINKS]
    ↓
[KNOWLEDGE_GRAPH]
    ↓
[MACHINE_REASONING]
    ↓
[AGENT_EXECUTION]
    ↓
[NEW_REALITY]
    ↓
[OBSIDIAN_UPDATE] ↺
```

---

## [OBSIDIAN_ARCHITECTURE] — Three Semantic Layers

### Layer 1: Human Layer
```
[NOTES]         — Freeform thoughts
[DOCUMENTS]     — Structured writing
[RESEARCH]      — Exploratory investigation
[MEETINGS]      — Sync notes + decisions
[IDEAS]         — Brainstorms + concepts
[PLANS]         — Strategies + roadmaps
[DECISIONS]     — Choices + rationale
[WRITING]       — Formal communication
```

### Layer 2: Semantic Layer
```
[FRONTMATTER]   — Metadata (type, status, owner, date)
[BRACKETS]      — Ontology terms ([AGENT], [TASK], [BLOCKED], [VERIFIED])
[WIKI_LINKS]    — Entity references ([[OMNIROUTE]], [[VENTURE_001]])
[TAGS]          — Searchable labels (#urgent, #architecture)
[PROPERTIES]    — Structured fields (status: complete, owner: X)
[ENTITY_IDS]    — Machine identifiers (VEN-000147, CAP-000082)
[RELATIONSHIPS] — Connections ([DEPENDS_ON], [EXECUTES], [PRODUCES])
[STATES]        — Current condition ([IN_PROGRESS], [BLOCKED], [VERIFIED])
[EVENTS]        — What happened (created, updated, deployed)
```

### Layer 3: Machine Layer
```
[INDEX]                 — Full-text search + entity index
[GRAPH]                 — Wiki link graph visualization
[REGISTRIES]            — Synchronized to git registries
[EMBEDDINGS]            — Vector representations for semantic search
[ENTITY_RESOLUTION]     — Duplicate detection + consolidation
[LINEAGE]               — Who references whom
[PROVENANCE]            — Where facts came from
[QUERIES]               — Datalog-style questions
[VALIDATION]            — Drift + consistency checks
[AUTOMATIONS]           — Triggers that run agents
```

---

## [WIKI_LINKS] vs [BRACKETS]

**Critical distinction: Use them for different jobs.**

### `[[Wiki Links]]` — Objects That Exist as Notes

Use for any entity that has a dedicated markdown file and represents something that exists or could exist:

```
[[WHOAMI]]                  — Identity document
[[MAC_STUDIO]]              — Physical device
[[OMNIROUTE]]               — Infrastructure service
[[REPOSITORY_INTELLIGENCE]] — Capability/system
[[TASK_001]]                — Work item
[[VENTURE_001]]             — Business entity
[[AGENT_001]]               — Autonomous entity
[[DECISION_001]]            — Recorded choice
[[EVIDENCE_001]]            — Proof/test result
```

### `[BRACKETS]` — Semantic Concepts / Ontology / States / Relationships

Use for abstract concepts, ontology terms, states, and relationship types:

```
[AGENT]             — Type classification
[TASK]              — Work unit
[BLOCKED]           — Current state
[VERIFIED]          — Verification status
[DEPENDS_ON]        — Relationship type
[EXECUTES]          — Execution relationship
[PRODUCES]          — Output relationship
[MONETIZES]         — Business relationship
[HOSTED_ON]         — Infrastructure relationship
[READS]             — Data flow
[WRITES]            — Data production
[TRANSFORMS]        — Transformation operation
```

### Combined: Complete Entity Description

```markdown
# [[REPOSITORY_INTELLIGENCE]]

[AGENT]
[CAPABILITY]
[EXECUTION_SYSTEM]

## Identity
- Type: [[CAPABILITY]]
- Purpose: Automated analysis of external repositories
- Owner: [[DIVINEJOHNS]]
- Status: [PRODUCTION]

## Execution
- [EXECUTES] [[REPOSITORY_SCAN_WORKFLOW]]
- [READS] [[REPOSITORY_REGISTRY]]
- [WRITES] [[KNOWLEDGE_GRAPH]]
- [PRODUCES] [[CAPABILITY_SUMMARY]]

## Impact
- [MONETIZES] [[OPPORTUNITY_DETECTION]]
- [ENABLES] [[VENTURE_READINESS_ASSESSMENT]]
- [HOSTED_ON] [[MAC_STUDIO]]

## Verification
- [TESTED] against 147 repositories
- [VERIFIED] by [[DIVINEJOHNS]] (Sep 29, 2026)
- Last run: [EXECUTED] [[DATE_TIMESTAMP]]
```

---

## [CANONICAL_VAULT_STRUCTURE] — 14 Knowledge Domains

```
/vault
├── 00_START_HERE/
│   ├── START_HERE.md
│   ├── [[WHOAMI]].md
│   ├── [[WHERE_WE_ARE]].md
│   ├── [[WHERE_WE_ARE_GOING]].md
│   ├── [[HOW_WE_GET_THERE]].md
│   ├── [[REALITY]].md
│   └── [[SOURCE_OF_TRUTH]].md
│
├── 01_CONSTITUTION/
│   ├── VALUES.md
│   ├── PRINCIPLES.md
│   ├── INTENTIONS.md
│   ├── [[DECISION_DOCTRINE]].md
│   ├── AUTHORITY.md
│   └── GOVERNANCE.md
│
├── 02_ONTOLOGY/
│   ├── ONTOLOGY.md
│   ├── [[BRACKETED_TERMS]].md
│   ├── [[ENTITY_TYPES]].md
│   ├── [[RELATIONSHIP_TYPES]].md
│   ├── [[STATES]].md
│   └── [[CONTROL_POINTS]].md
│
├── 03_GRAPH/
│   ├── [[KNOWLEDGE_GRAPH]].md
│   ├── [[ENTITY_GRAPH]].md
│   ├── [[DEPENDENCY_GRAPH]].md
│   ├── [[TASK_GRAPH]].md
│   ├── [[AGENT_GRAPH]].md
│   └── [[REVENUE_GRAPH]].md
│
├── 04_ORGANIZATION/
│   ├── [[ORGANIZATION]].md
│   ├── [[HOLDING_COMPANY]].md
│   ├── [[ENTITIES]].md
│   ├── [[OPCOS]].md
│   ├── [[SPVS]].md
│   ├── [[VENTURES]].md
│   ├── [[DEPARTMENTS]].md
│   └── [[ROLES]].md
│
├── 05_INFRASTRUCTURE/
│   ├── [[INFRASTRUCTURE]].md
│   ├── [[MAC_STUDIO]].md
│   ├── [[MAC_AIR]].md
│   ├── [[STORAGE]].md
│   ├── [[DOCKER]].md
│   ├── [[CONTAINERS]].md
│   ├── [[TAILSCALE]].md
│   ├── [[NETWORK]].md
│   ├── [[PORTS]].md
│   └── [[CONNECTIVITY_TESTS]].md
│
├── 06_AI/
│   ├── [[AI_SYSTEM]].md
│   ├── [[MODELS]].md
│   ├── [[PROVIDERS]].md
│   ├── [[OMNIROUTE]].md
│   ├── [[CLAUDE]].md
│   ├── [[CLAUDE_CODE]].md
│   ├── [[ANTIGRAVITY]].md
│   ├── [[AGENTS]].md
│   ├── [[SKILLS]].md
│   ├── [[CAPABILITIES]].md
│   ├── [[MCP]].md
│   ├── [[A2A]].md
│   └── [[AUTONOMY]].md
│
├── 07_DATA/
│   ├── [[DATA_FLOW]].md
│   ├── [[DATA_SOURCES]].md
│   ├── [[DATA_MODEL]].md
│   ├── [[DATA_SCHEMA]].md
│   ├── [[DATA_LINEAGE]].md
│   ├── [[DATA_PROVENANCE]].md
│   ├── [[DATA_VALIDATION]].md
│   └── [[REGISTRIES]].md
│
├── 08_CODE/
│   ├── [[CODEBASE]].md
│   ├── [[REPOSITORIES]].md
│   ├── [[SERVICES]].md
│   ├── [[APIS]].md
│   ├── [[DEPENDENCIES]].md
│   └── [[DEPLOYMENTS]].md
│
├── 09_WORK/
│   ├── [[TASKS]].md
│   ├── [[UNCOMPLETED_TASKS]].md
│   ├── [[BLOCKERS]].md
│   ├── [[DEPENDENCIES]].md
│   ├── [[HANDOFFS]].md
│   ├── [[ROTATIONS]].md
│   ├── [[WORK_QUEUES]].md
│   └── [[UPDATES]].md
│
├── 10_DECISIONS/
│   ├── [[DECISIONS]].md
│   ├── [[APPROVALS]].md
│   ├── [[ASSUMPTIONS]].md
│   └── [[DECISION_HISTORY]].md
│
├── 11_BUSINESS/
│   ├── [[BUSINESS_MODEL]].md
│   ├── [[MARKETS]].md
│   ├── [[PRODUCTS]].md
│   ├── [[SERVICES]].md
│   ├── [[CUSTOMERS]].md
│   ├── [[SALES]].md
│   ├── [[REVENUE]].md
│   ├── [[CAPITAL]].md
│   └── [[OUTCOMES]].md
│
├── 12_VERIFICATION/
│   ├── [[EVIDENCE]].md
│   ├── [[TESTS]].md
│   ├── [[HEALTH_CHECKS]].md
│   ├── [[ASSERTIONS]].md
│   ├── [[DRIFT]].md
│   └── [[AUDIT_LOG]].md
│
├── 13_RESEARCH/
│   ├── [[RESEARCH]].md
│   ├── [[SOURCES]].md
│   ├── [[QUESTIONS]].md
│   ├── [[HYPOTHESES]].md
│   └── [[INSIGHTS]].md
│
└── 99_SYSTEM/
    ├── [[OBSIDIAN]].md
    ├── [[VAULT_STRUCTURE]].md
    ├── [[INGESTION]].md
    ├── [[INDEXING]].md
    ├── [[LINKING]].md
    ├── [[AUTOMATION]].md
    ├── [[GRAPH_SYNC]].md
    └── [[VAULT_HEALTH]].md
```

---

## [MASTER_SEMANTIC_LOOP]

This is the loop that makes Obsidian an **active part** of the system, not a downstream artifact:

```
[REALITY]           ← What actually exists/changes
    ↓
[OBSERVATION]       ← Human or system observes it
    ↓
[CAPTURE]           ← Record in markdown note
    ↓
[FRONTMATTER]       ← Add metadata (type, owner, date, status)
    ↓
[BRACKET_EXTRACTION]  ← Extract [ONTOLOGY_TERMS]
    ↓
[WIKI_LINK_RESOLUTION]  ← Resolve [[ENTITY_REFERENCES]]
    ↓
[ENTITY_RESOLUTION]   ← Deduplicate, consolidate
    ↓
[RELATIONSHIP_EXTRACTION]  ← Extract [DEPENDS_ON], [PRODUCES], etc.
    ↓
[GRAPH_UPDATE]      ← Write to Neo4j
    ↓
[KNOWLEDGE_UPDATE]  ← Indexed, queryable
    ↓
[WHERE_WE_ARE_UPDATE] ← Refresh current state
    ↓
[IMPACT_ANALYSIS]   ← What changed? What's affected?
    ↓
[TASK_GENERATION]   ← Create work items for changes
    ↓
[AGENT_DELEGATION]  ← Route to appropriate agents
    ↓
[EXECUTION]         ← Agents act
    ↓
[VERIFICATION]      ← Test, check, validate
    ↓
[EVIDENCE]          ← Gather proof
    ↓
[OBSIDIAN_UPDATE]   ← Record result back in vault
    ↺
```

---

## [ENTITY_INTERROGATION] — Every Entity Must Answer

Every meaningful Obsidian object (`[[ENTITY]]`) must be interrogatable:

```
[WHAT_IS_IT]
  → Type, classification, purpose

[WHY_DOES_IT_EXIST]
  → Strategic context, motivation

[WHO_OWNS_IT]
  → Accountable party, decision authority

[WHO_USES_IT]
  → Consumers, dependents, downstream systems

[WHERE_IS_IT]
  → Physical location, system location, repository

[WHAT_DOES_IT_DEPEND_ON]
  → Upstream systems, prerequisites, blockers

[WHAT_DEPENDS_ON_IT]
  → Downstream impacts, who needs this

[WHAT_DATA_DOES_IT_USE]
  → Inputs, data sources, feeds

[WHAT_DOES_IT_PRODUCE]
  → Outputs, results, side effects

[WHAT_DOES_IT_ENABLE]
  → Capabilities it unlocks

[WHAT_REPOSITORY_IMPLEMENTS_IT]
  → GitHub repo, file path, codebase

[WHAT_AGENT_OPERATES_IT]
  → Which AI agent manages/executes

[WHAT_TASKS_USE_IT]
  → Which work items depend on this

[WHAT_DECISIONS_USE_IT]
  → What choices rely on this

[WHAT_OUTCOMES_RESULT]
  → Business impact, revenue, learning

[HOW_IS_IT_VERIFIED]
  → Test, observation, approval method

[WHAT_EVIDENCE_EXISTS]
  → Proof, screenshots, logs, metrics

[WHAT_IS_THE_CURRENT_STATE]
  → Live status, health, last updated

[WHEN_WAS_IT_LAST_UPDATED]
  → Timestamp, change frequency

[WHAT_CHANGED]
  → Recent modifications, delta

[WHAT_IS_NOW_REQUIRED]
  → Next action, dependency, blocker
```

---

## [COMPLETE_ENTITY_TRAVERSAL]

Every [[ENTITY]] should be reachable via this path:

```
[[ENTITY]]
    ↓ [WHAT_IS_IT]
[[PURPOSE]]
    ↓ [WHY_DOES_IT_EXIST]
[[OBJECTIVE]]
    ↓ [WHAT_IS_REQUIRED]
[[REQUIREMENT]]
    ↓ [WHAT_ENABLES_THIS]
[[CAPABILITY]]
    ↓ [WHO_PROVIDES_THIS]
[[AGENT]]
    ↓ [HOW_IS_THIS_BUILT]
[[REPOSITORY]]
    ↓ [WHERE_IS_THIS_HOSTED]
[[INFRASTRUCTURE]]
    ↓ [WHAT_DATA_FLOWS]
[[DATA_FLOW]]
    ↓ [WHAT_DOES_THIS_PRODUCE]
[[KNOWLEDGE]]
    ↓ [HOW_IS_THIS_USED]
[[DECISION]]
    ↓ [WHAT_ACTION_RESULTS]
[[TASK]]
    ↓ [WHO_EXECUTES_THIS]
[[ACTION]]
    ↓ [WHAT_IS_THE_RESULT]
[[OUTCOME]]
    ↓ [WHAT_VALUE_IS_CREATED]
[[REVENUE]]
    ↓ [HOW_IS_THIS_PROVEN]
[[EVIDENCE]]
    ↓ [WHERE_IS_THIS_RECORDED]
[[WHERE_WE_ARE]]
    ↓ [WHAT_IS_THE_STATE_NOW]
[[ENTITY]]
```

---

## [OBSIDIAN_FRONTMATTER_STANDARD]

Every note should have canonical metadata:

```yaml
---
type: agent | capability | task | decision | entity | evidence | infrastructure | outcome

status: idea | draft | active | verified | completed | archived

owner: [[ENTITY]]

created_at: 2026-10-02
updated_at: 2026-10-02

relates_to:
  - [[ENTITY_1]]
  - [[ENTITY_2]]

depends_on:
  - [[DEPENDENCY_1]]

blocks:
  - [[TASK_1]]

verified_by: [[APPROVER]]

evidence:
  - [[TEST_1]]
  - [[OBSERVATION_1]]

state: [ACTIVE] | [BLOCKED] | [VERIFIED] | [FAILED]

tags:
  - architecture
  - urgent
  - infrastructure

---
```

---

## [BRACKETED_ONTOLOGY] — Standard Terms

Every bracket term should be defined in `[[BRACKETED_TERMS]]`:

```
[AGENT]             — Autonomous entity capable of decisions and actions
[TASK]              — Discrete unit of work
[BLOCKED]           — Cannot proceed; external blocker
[VERIFIED]          — Evidence confirms state/completion
[EXECUTED]          — Action completed
[DEPENDS_ON]        — Requires another entity
[EXECUTES]          — Runs, operates, implements
[PRODUCES]          — Creates output/result
[READS]             — Consumes data from
[WRITES]            — Produces data to
[MONETIZES]         — Converts to revenue
[HOSTED_ON]         — Physical/logical location
[ENABLES]           — Makes possible
[TRIGGERS]          — Initiates
[TRANSFORMS]        — Changes form/content
[VERIFIES]          — Confirms truth of
[ESCALATES_TO]      — Moves to higher authority
[ROTATES_TO]        — Reassigns to
[HANDOFFS_TO]       — Transfers to
[REQUIRES_APPROVAL] — Needs authorization
[FAILED]            — Did not succeed
[PENDING]           — Waiting for something
[STALE]             → Potentially out of date
```

---

## [VAULT_AUTOMATION]

Obsidian should trigger automations:

```
[ON_NOTE_CREATE]
  → Extract brackets, wiki links
  → Generate frontmatter template
  → Run entity resolution
  → Update graph

[ON_NOTE_UPDATE]
  → Detect changes
  → Extract new brackets/links
  → Check for drift
  → Cascade updates to related entities
  → Flag if current state differs from [[WHERE_WE_ARE]]

[ON_LINK_CREATE]
  → Validate [[TARGET]] exists
  → Check for circular dependencies
  → Update backlinks
  → Alert if creating breaking change

[ON_STATE_CHANGE]
  → Log state transition
  → Trigger dependent tasks
  → Update WHERE_WE_ARE
  → Alert affected parties
  → Generate next-action suggestions

[ON_VERIFICATION]
  → Mark verified with timestamp
  → Archive evidence
  → Unlock dependent tasks
  → Update knowledge graph
  → Close associated tasks
```

---

## Implementation: Making Obsidian the Semantic Source

To make this real:

1. **Create canonical vault structure** — 14 domains, all cross-linked
2. **Define bracketed ontology** — 50+ terms with consistent meaning
3. **Wire frontmatter validation** — Enforce standard metadata on all notes
4. **Implement bracket extraction** — Scanner that finds [TERMS] and creates graph edges
5. **Implement wiki-link validation** — Checks that [[LINKS]] point to real files
6. **Create entity resolution** — Deduplicates entities, consolidates definitions
7. **Build graph sync** — Exports Obsidian entities to Neo4j daily
8. **Create verification workflow** — Enforces evidence before [VERIFIED] state
9. **Implement cascading updates** — When one entity changes, what else must update?
10. **Build vault health dashboard** — Shows drift, missing evidence, broken links

---

**Obsidian is not where you keep notes. It is where the Company Brain continuously explains itself, and where humans keep it honest.**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[TASK_EXECUTION_MASTER_ONTOLOGY.md]]

**Human-readable semantic source layer: The bridge between reality and machine reasoning.**
