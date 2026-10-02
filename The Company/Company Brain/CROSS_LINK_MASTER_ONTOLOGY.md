---
type: master-ontology
canonical: true
authority: semantic-resolution
updated_at: 2026-10-02T19:00:00Z
source_of_truth: true
---

# CROSS_LINK_MASTER_ONTOLOGY — Semantic Grammar

**Master grammar that makes every [[BRACKET]] resolvable. Defines the semantics of links, not just the links themselves.**

This is what lets Claude, Antigravity, agents, and the Company Brain itself traverse the entire knowledge system recursively instead of treating `.md` files as isolated documents.

---

## [PURPOSE]

Turn markdown from **human-readable** into **machine-navigable**.

Transform:
```
[[OMNIROUTE]] is mentioned somewhere
```

Into:
```
[[OMNIROUTE]] = resolvable semantic entity with:
  - Type: service
  - Location: [[MAC_STUDIO]]
  - Runtime: [[DOCKER]]
  - Uses: [[LITELLM]], [[LLM_PROVIDERS]]
  - Used_by: [[CLAUDE_CODE]], [[ANTIGRAVITY]]
  - Provides: [[MODEL_ROUTING]], [[PROVIDER_ROUTING]]
  - Verified_by: [[CONNECTIVITY_TESTS]]
  - State: [[WHERE_WE_ARE#OMNIROUTE]]
```

---

## [LINK_TYPES] — The Relationship Semantics

Every `[[A]] → [[B]]` relationship must have an explicit type:

### [IDENTITY]
```
IS_A           — Type definition (Venture IS_A Company)
INSTANCE_OF    — Instance (VEN-000147 INSTANCE_OF Venture)
REPRESENTS     — Abstraction (OmniRoute REPRESENTS AI_GATEWAY)
ALIAS_OF       — Alternative name
```

### [STRUCTURE]
```
PARENT_OF      — Contains (Sector PARENT_OF Ventures)
CHILD_OF       — Contained by
PART_OF        — Component (Service PART_OF Infrastructure)
CONTAINS       — Has subcomponent
MEMBER_OF      — Group membership
```

### [RELATIONSHIP]
```
RELATED_TO     — General connection
CONNECTED_TO   — Network/system connection
DEPENDS_ON     — Requirement (Agent DEPENDS_ON Capability)
REQUIRES       — Precondition (Action REQUIRES Decision)
ENABLES        — Activation (Capability ENABLES Agent)
BLOCKS         — Prevents (Blocker BLOCKS Action)
CONFLICTS_WITH — Mutually exclusive
```

### [DATA]
```
READS          — Consumes (Agent READS from Database)
WRITES         — Produces (Agent WRITES to Database)
PRODUCES       — Generates output (System PRODUCES Outcome)
CONSUMES       — Accepts input (System CONSUMES Data)
TRANSFORMS     — Changes format/content
SOURCES        — Origin (Data SOURCES from API)
DERIVED_FROM   — Computed (Metric DERIVED_FROM Ventures)
```

### [KNOWLEDGE]
```
DESCRIBES      — Explains (Document DESCRIBES System)
EXPLAINS       — Detailed explanation
EVIDENCES      — Provides proof (Test EVIDENCES Connectivity)
SUPPORTS       — Agrees with (Evidence SUPPORTS Claim)
CONTRADICTS    — Disagrees with
VERIFIES       — Confirms truth (Test VERIFIES Assumption)
REFERENCES     — Cites (Document REFERENCES Ontology)
```

### [EXECUTION]
```
TRIGGERS       — Initiates (Event TRIGGERS Action)
EXECUTES       — Runs (Agent EXECUTES Workflow)
DELEGATES_TO   — Assigns (System DELEGATES_TO Agent)
ASSIGNED_TO    — Owner (Task ASSIGNED_TO Owner)
CREATES        — Makes (Action CREATES Entity)
UPDATES        — Modifies (Action UPDATES Entity)
COMPLETES      — Finishes (Action COMPLETES Goal)
```

### [DECISION]
```
INFORMS        — Provides input (Data INFORMS Decision)
RECOMMENDS     — Suggests (Agent RECOMMENDS Action)
APPROVES       — Authorizes (Authority APPROVES Action)
REJECTS        — Denies (Authority REJECTS Action)
ESCALATES_TO   — Elevates (Blocker ESCALATES_TO Human)
RESULTS_IN     — Outcome (Decision RESULTS_IN Action)
```

### [INFRASTRUCTURE]
```
HOSTED_ON      — Physical location (Service HOSTED_ON Mac_Studio)
RUNS_IN        — Runtime environment (Service RUNS_IN Docker)
MOUNTS         — Storage binding (Container MOUNTS Volume)
EXPOSES        — Makes available (Service EXPOSES API)
CONNECTS_TO    — Network link (Mac_Air CONNECTS_TO Mac_Studio)
ROUTES_THROUGH — Passes via (Traffic ROUTES_THROUGH Tailscale)
MONITORED_BY   — Watched by (Service MONITORED_BY Health_Check)
```

### [BUSINESS]
```
GENERATES      — Creates (Venture GENERATES Revenue)
MONETIZES      — Converts to $ (Feature MONETIZES Usage)
SERVES         — Provides for (Product SERVES Customer)
OPERATES       — Runs (OPC OPERATES Ventures)
OWNS           — Possesses (Founder OWNS Venture)
INVESTS_IN     — Funds (Capital INVESTS_IN Venture)
CREATES_VALUE_FOR — Benefit (System CREATES_VALUE_FOR Business)
```

---

## [CANONICAL_LAYERS]

### Layer 0: Identity & Constitution
```
[[WHOAMI.md]]
├── Defines: [[IDENTITY]], [[AUTHORITY]], [[DECISION_DOCTRINE]]
├── References: [[LEGAL_ENTITIES]], [[ROLES]], [[PEOPLE]]
└── Governs: All downstream decisions
```

### Layer 1: Current Reality
```
[[WHERE_WE_ARE.md]]
├── Describes: [[REALITY]], [[CURRENT_STATE]], [[VERIFIED_FACTS]]
├── References: [[INFRASTRUCTURE]], [[CODEBASE]], [[SERVICES]]
├── Status_of: Every major component
└── Constrains: [[TARGET_STATE]] (must be reachable from here)
```

### Layer 2: Movement & Lifecycle
```
[[DATA_FLOW.md]]
├── Describes: [[DATA]] → [[KNOWLEDGE]] → [[DECISION]] → [[ACTION]] → [[OUTCOME]]
├── Defines: [[LIFECYCLE]], [[TRANSFORMATIONS]], [[PIPELINES]]
├── Connects: All systems via data relationships
└── Traces: Feedback loops
```

### Layer 3: Physical Runtime
```
[[INFRASTRUCTURE.md]]
├── Details: [[MACHINES]], [[DOCKER]], [[SERVICES]], [[NETWORK]]
├── Specifies: [[CONNECTIVITY_TESTS]], [[VERIFICATION_COMMANDS]]
├── Hosts: All executable systems
└── Verified_by: [[CONNECTIVITY_TESTS#Evidence_Registry]]
```

### Layer 4: Semantic Resolution
```
[[CROSS_LINK_MASTER_ONTOLOGY.md]] (this file)
├── Defines: [[LINK_TYPES]], [[RELATIONSHIP_SEMANTICS]]
├── Provides: [[RESOLUTION_RULES]], [[TRAVERSAL_PATHS]]
├── Enables: Machine navigation of knowledge
└── Grammar: For all other documents
```

### Layer 5: Security & Identity
```
[[SECRETS_AND_AUTH_MASTER_ONTOLOGY.md]]
├── Defines: [[IDENTITY]], [[SECRETS]], [[AUTHENTICATION]], [[AUTHORIZATION]]
├── Governs: Credential metadata (not values)
├── Maintains: Secret registry, access control, audit trail
└── Integrates: All secrets and credentials into the graph
```

### Layer 6: Code & Collaboration
```
[[GITHUB_MASTER_ONTOLOGY.md]]
├── Defines: [[GITHUB]], [[REPOSITORY]], [[GIT]], [[CI_CD]], [[EVIDENCE]]
├── Provides: Code source of truth, execution evidence, automation
├── Maintains: Repository intelligence, capability mapping, repo-to-revenue
└── Integrates: All code systems into the graph
```

### Layer 7: Physical Storage & Filesystem
```
[[FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY.md]]
├── Defines: [[FILESYSTEM]], [[DISK_MAP]], [[FILE_TREE]], [[STORAGE_PATH]]
├── Maps: Where all data physically lives (disks, volumes, mounts)
├── Tracks: File lineage, backups, migrations, storage capacity
└── Verifies: Filesystem connectivity, disk health, data integrity
```

---

## [CROSS_LINK_MATRIX] — Canonical Relationships

| From | Relationship | To | Reason |
|------|--------------|----|----|
| [[WHOAMI]] | GOVERNS | [[DECISION_DOCTRINE]] | Constitutional authority |
| [[WHOAMI]] | DEFINES | [[IDENTITY]] | Self-definition |
| [[WHERE_WE_ARE]] | DESCRIBES | [[CURRENT_STATE]] | State registry |
| [[WHERE_WE_ARE]] | VERIFIES | [[ASSERTIONS]] | Evidence-based |
| [[WHERE_WE_ARE]] | REFERENCES | [[INFRASTRUCTURE]] | What's running |
| [[WHERE_WE_ARE]] | REFERENCES | [[CODEBASE]] | What exists |
| [[DATA_FLOW]] | DESCRIBES | [[DATA]] | Movement |
| [[DATA_FLOW]] | CONNECTS | [[SYSTEMS]] | Relationships |
| [[DATA_FLOW]] | DEFINES | [[LIFECYCLE]] | Birth → Death |
| [[INFRASTRUCTURE]] | HOSTS | [[APPLICATIONS]] | Runtime |
| [[INFRASTRUCTURE]] | RUNS | [[CONTAINERS]] | Docker execution |
| [[CONTAINERS]] | RUNS | [[SERVICES]] | Service hosting |
| [[SERVICES]] | EXPOSES | [[APIS]] | Interface |
| [[APIS]] | PROVIDES | [[CAPABILITIES]] | Functionality |
| [[REPOSITORIES]] | IMPLEMENT | [[CAPABILITIES]] | Code base |
| [[CAPABILITIES]] | ENABLE | [[AGENTS]] | Agent resources |
| [[AGENTS]] | EXECUTE | [[WORKFLOWS]] | Automation |
| [[WORKFLOWS]] | PRODUCE | [[OUTCOMES]] | Results |
| [[DATA]] | INFORMS | [[DECISIONS]] | Input to choice |
| [[DECISIONS]] | TRIGGER | [[ACTIONS]] | Execution gate |
| [[ACTIONS]] | PRODUCE | [[OUTCOMES]] | Impact |
| [[OUTCOMES]] | GENERATE | [[FEEDBACK]] | Learning signal |
| [[FEEDBACK]] | UPDATES | [[KNOWLEDGE]] | Learning |
| [[KNOWLEDGE]] | UPDATES | [[KNOWLEDGE_GRAPH]] | Neo4j graph |
| [[KNOWLEDGE_GRAPH]] | INFORMS | [[AGENTS]] | Context for next decision |
| [[SOURCE_OF_TRUTH]] | VERIFIES | [[ASSERTIONS]] | Canonical check |
| [[CONNECTIVITY_TESTS]] | VERIFIES | [[CONNECTIONS]] | Evidence |
| [[AUDIT_LOG]] | RECORDS | [[ACTIONS]] | Immutable trail |
| [[GOVERNANCE]] | CONSTRAINS | [[ACTIONS]] | Policy enforcement |
| [[REAL_ITY]] | CONSTRAINS | [[TARGET_STATE]] | Feasibility |
| [[TAILSCALE]] | CONNECTS | [[MACHINES]] | Network |
| [[DOCKER]] | CONTAINERS | [[MAC_STUDIO]] | Host |

---

## [CROSS_LINKING_RULE]

Every canonical entity MUST be interrogatable via these questions:

```
[[OMNIROUTE]] must answer:

[WHAT_IS_IT]
  → Service, AI Gateway, Model Router

[WHERE_IS_IT]
  → [[MAC_STUDIO]], running in [[DOCKER]], listening on port 3004

[WHO_OWNS_IT]
  → [[DIVINEJOHNS]] (technical owner)

[WHO_USES_IT]
  → [[CLAUDE_CODE]], [[ANTIGRAVITY]], [[CODEX]], [[AGENTS]]

[WHAT_DOES_IT_ENABLE]
  → [[MODEL_ROUTING]], [[PROVIDER_SWITCHING]], [[FALLBACK_LOGIC]]

[WHAT_DOES_IT_DEPEND_ON]
  → [[LITELLM]], [[LLM_PROVIDERS]], [[DOCKER]], [[MAC_STUDIO]]

[WHAT_DEPENDS_ON_IT]
  → [[CLAUDE_CODE]], [[AGENTS]], [[WORKFLOWS]]

[WHAT_DATA_DOES_IT_TOUCH]
  → [[PROMPTS]], [[MODEL_RESPONSES]], [[ROUTING_DECISIONS]]

[WHAT_SYSTEMS_DOES_IT_CONNECT]
  → [[NEO4J]], [[QDRANT]], [[POSTGRESQL]], [[LLM_PROVIDERS]]

[WHAT_REPOSITORY_IMPLEMENTS_IT]
  → github.com/worldwidebro/omniroute (or integration)

[WHAT_AGENT_USES_IT]
  → [[AGENT_ROUTER]], [[MODEL_SELECTION_AGENT]]

[WHAT_WORKFLOW_USES_IT]
  → [[PROMPT_EXECUTION_WORKFLOW]], [[LLM_INFERENCE_WORKFLOW]]

[WHAT_DECISIONS_DOES_IT_INFORM]
  → Which model to use, which provider to call

[WHAT_OUTCOMES_DOES_IT_PRODUCE]
  → [[LLM_RESPONSE]], [[ROUTING_METRICS]], [[COST_TRACKING]]

[HOW_IS_IT_VERIFIED]
  → [[CONNECTIVITY_TEST_2026_10_02#OMNIROUTE]]

[WHAT_EVIDENCE_EXISTS]
  → [[WHERE_WE_ARE#OMNIROUTE]], [[INFRASTRUCTURE#OMNIROUTE]], test results

[WHAT_DOCUMENTS_DESCRIBE_IT]
  → [[INFRASTRUCTURE.md#OMNIROUTE]], [[WHERE_WE_ARE.md#OMNIROUTE]]

[WHAT_IS_ITS_CURRENT_STATE]
  → [[WHERE_WE_ARE#SERVICES#OMNIROUTE]] = [VERIFIED]
```

---

## [RECURSIVE_LOOP] — The Company Brain Heartbeat

Every entity participates in this loop:

```
[[IDENTITY]]
    ↓ (what are we?)
[[INTENT]]
    ↓ (why do we exist?)
[[OBJECTIVE]]
    ↓ (what are we trying to achieve?)
[[REQUIREMENT]]
    ↓ (what do we need?)
[[CAPABILITY]]
    ↓ (what can we do?)
[[RESOURCE]]
    ↓ (what tools/systems?)
[[SYSTEM]]
    ↓ (what runs it?)
[[DATA]]
    ↓ (what flows through?)
[[KNOWLEDGE]]
    ↓ (what do we learn?)
[[AGENT]]
    ↓ (who/what decides?)
[[DECISION]]
    ↓ (what choice?)
[[ACTION]]
    ↓ (what happens?)
[[OUTCOME]]
    ↓ (what results?)
[[FEEDBACK]]
    ↓ (what lesson?)
[[LEARNING]]
    ↓ (how do we improve?)
[[CAPABILITY]] ↺ (what can we do NOW?)
```

---

## [RESOLUTION_RULES]

### Rule 1: Every bracket is a node
```
[[ANYTHING]] = Queryable semantic entity
  → Has type (service, agent, document, concept, entity)
  → Has location (if applicable)
  → Has relationships (inbound + outbound)
  → Has evidence (where it's verified)
  → Has state (current + historical)
```

### Rule 2: Every relationship has semantics
```
[[A]] → [[B]]  is meaningless without type
[[A]] --READS--> [[B]]  is queryable, auditable, executable
```

### Rule 3: No orphan brackets
```
Every [[BRACKET]] must answer: "What does this connect to?"
If it connects to nothing → it's either:
  - Not yet integrated (TODO)
  - Dead/deprecated (remove)
  - Needs documentation (add to ontology)
```

### Rule 4: Bidirectional relationships
```
If [[A]] READS [[B]]
Then [[B]] IS_READ_BY [[A]]

Both directions explicit (or one is derived)
```

### Rule 5: Verification chains
```
[[ASSERTION]] is valid only if:
  → Referenced in [[WHERE_WE_ARE.md]] AND
  → Supported by [[EVIDENCE]] (test, observation, fact) AND
  → Traceable via [[PROVENANCE]]
```

---

## [NAVIGATION_PATTERNS]

### "Trace an action to outcome"
```
[[ACTION]] 
  → TRIGGERS [[EVENT]]
  → EXECUTES [[WORKFLOW]]
  → PRODUCES [[OUTCOME]]
  → GENERATES [[FEEDBACK]]
  → UPDATES [[KNOWLEDGE_GRAPH]]
```

### "Find what breaks if system X fails"
```
[[SYSTEM_X]]
  → IS_REQUIRED_BY [[Y]], [[Z]], ...
  → IMPACTS [[OUTCOMES_1]], [[OUTCOMES_2]], ...
  → AFFECTS [[BUSINESS_VALUES]]
```

### "Verify a claim"
```
[[CLAIM]]
  → REFERENCED_IN [[DOCUMENT]]
  → SUPPORTED_BY [[TEST]], [[OBSERVATION]]
  → VERIFIED_AT [[DATE_TIME]]
  → CURRENT_STATE [[WHERE_WE_ARE]]
```

### "Find who owns something"
```
[[ENTITY]]
  → OWNED_BY [[ROLE]]
  → DELEGATED_TO [[AGENT]]
  → APPROVED_BY [[AUTHORITY]]
  → RESPONSIBLE_FOR [[OUTCOME]]
```

---

## [MASTER_ONTOLOGY_HIERARCHY]

```
                         [[WHOAMI]]
                     (Constitutional)
                            │
                            ▼
                      [[SECRETS_AND_AUTH]]
                    (Identity & Security)
                            │
                            ▼
                      [[WHERE_WE_ARE]]
                     (Current State)
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
[[INFRASTRUCTURE]]   [[DATA_FLOW]]      [[CODEBASE]]
(Physical Layer) (Movement Layer) (Implementation)
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
                    [[KNOWLEDGE_GRAPH]]
                  (Relationship Graph)
                            │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
  [[CAPABILITIES]]     [[AGENTS]]    [[WORKFLOWS]]
         │                 │                 │
         └────────────┬────┴────────────────┘
                      ▼
                 [[DECISIONS]]
                      │
                      ▼
                  [[ACTIONS]]
                      │
                      ▼
                  [[OUTCOMES]]
                      │
                      ▼
                  [[FEEDBACK]]
                      │
                      ▼
                  [[KNOWLEDGE]]
                      │
                      └──────────↺
                   (back to DECISIONS)
```

---

## [IMPLEMENTATION]

This ontology enables:

1. **Automated traversal** — Agent can walk from any [[BRACKET]] to any related concept
2. **Impact analysis** — "What breaks if X fails?" → Follow DEPENDS_ON edges
3. **Provenance tracking** — "Who verified this?" → Follow EVIDENCED_BY edges
4. **Completeness checking** — "Is this entity fully documented?" → Check all questions answered
5. **Consistency validation** — "Does this relationship make sense?" → Type-check against semantics
6. **Recursive learning** — New feedback updates [[KNOWLEDGE_GRAPH]] → improves next [[DECISION]]

---

## [NEXT_ACTIONS]

```
NOW:
  [ ] Map every [[BRACKET]] in existing documents to ontology
  [ ] Identify orphaned brackets (connected to nothing)
  [ ] Classify all relationships by type
  
THIS_WEEK:
  [ ] Create bracket resolution service (Neo4j query engine)
  [ ] Implement bidirectional edge generation
  [ ] Add verification requirement enforcement
  
NEXT_MONTH:
  [ ] Agent navigation of knowledge graph
  [ ] Automated completeness checking
  [ ] Live verification metrics dashboard
```

---

**This is what makes the Company Brain navigable instead of just readable.**

**Every [[BRACKET]] is now a semantic entity. Every relationship is now a queryable arc.**

**The loop is complete: REALITY → DATA → KNOWLEDGE → DECISION → ACTION → OUTCOME → FEEDBACK → LEARNING → IMPROVED CAPABILITY ↺**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]]

**Master grammar: Enables machine navigation of all knowledge.**
