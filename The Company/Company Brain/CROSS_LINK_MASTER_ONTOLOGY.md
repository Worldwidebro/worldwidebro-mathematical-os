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

## [[PURPOSE]]

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

## [[LINK_TYPES]] — The Relationship Semantics

Every `[[A]] → [[B]]` relationship must have an explicit type:

### [[IDENTITY]]
```
IS_A           — Type definition (Venture IS_A Company)
INSTANCE_OF    — Instance (VEN-000147 INSTANCE_OF Venture)
REPRESENTS     — Abstraction (OmniRoute REPRESENTS AI_GATEWAY)
ALIAS_OF       — Alternative name
```

### [[STRUCTURE]]
```
PARENT_OF      — Contains (Sector PARENT_OF Ventures)
CHILD_OF       — Contained by
PART_OF        — Component (Service PART_OF Infrastructure)
CONTAINS       — Has subcomponent
MEMBER_OF      — Group membership
```

### [[RELATIONSHIP]]
```
RELATED_TO     — General connection
CONNECTED_TO   — Network/system connection
DEPENDS_ON     — Requirement (Agent DEPENDS_ON Capability)
REQUIRES       — Precondition (Action REQUIRES Decision)
ENABLES        — Activation (Capability ENABLES Agent)
BLOCKS         — Prevents (Blocker BLOCKS Action)
CONFLICTS_WITH — Mutually exclusive
```

### [[DATA]]
```
READS          — Consumes (Agent READS from Database)
WRITES         — Produces (Agent WRITES to Database)
PRODUCES       — Generates output (System PRODUCES Outcome)
CONSUMES       — Accepts input (System CONSUMES Data)
TRANSFORMS     — Changes format/content
SOURCES        — Origin (Data SOURCES from API)
DERIVED_FROM   — Computed (Metric DERIVED_FROM Ventures)
```

### [[KNOWLEDGE]]
```
DESCRIBES      — Explains (Document DESCRIBES System)
EXPLAINS       — Detailed explanation
EVIDENCES      — Provides proof (Test EVIDENCES Connectivity)
SUPPORTS       — Agrees with (Evidence SUPPORTS Claim)
CONTRADICTS    — Disagrees with
VERIFIES       — Confirms truth (Test VERIFIES Assumption)
REFERENCES     — Cites (Document REFERENCES Ontology)
```

### [[EXECUTION]]
```
TRIGGERS       — Initiates (Event TRIGGERS Action)
EXECUTES       — Runs (Agent EXECUTES Workflow)
DELEGATES_TO   — Assigns (System DELEGATES_TO Agent)
ASSIGNED_TO    — Owner (Task ASSIGNED_TO Owner)
CREATES        — Makes (Action CREATES Entity)
UPDATES        — Modifies (Action UPDATES Entity)
COMPLETES      — Finishes (Action COMPLETES Goal)
```

### [[DECISION]]
```
INFORMS        — Provides input (Data INFORMS Decision)
RECOMMENDS     — Suggests (Agent RECOMMENDS Action)
APPROVES       — Authorizes (Authority APPROVES Action)
REJECTS        — Denies (Authority REJECTS Action)
ESCALATES_TO   — Elevates (Blocker ESCALATES_TO Human)
RESULTS_IN     — Outcome (Decision RESULTS_IN Action)
```

### [[INFRASTRUCTURE]]
```
HOSTED_ON      — Physical location (Service HOSTED_ON Mac_Studio)
RUNS_IN        — Runtime environment (Service RUNS_IN Docker)
MOUNTS         — Storage binding (Container MOUNTS Volume)
EXPOSES        — Makes available (Service EXPOSES API)
CONNECTS_TO    — Network link (Mac_Air CONNECTS_TO Mac_Studio)
ROUTES_THROUGH — Passes via (Traffic ROUTES_THROUGH Tailscale)
MONITORED_BY   — Watched by (Service MONITORED_BY Health_Check)
```

### [[BUSINESS]]
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

## [[CANONICAL_LAYERS]]

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

## [[CROSS_LINK_MATRIX]] — Canonical Relationships

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

## [[CROSS_LINKING_RULE]]

Every canonical entity MUST be interrogatable via these questions:

```
[[OMNIROUTE]] must answer:

[[WHAT_IS_IT]]
  → Service, AI Gateway, Model Router

[[WHERE_IS_IT]]
  → [[MAC_STUDIO]], running in [[DOCKER]], listening on port 3004

[[WHO_OWNS_IT]]
  → [[DIVINEJOHNS]] (technical owner)

[[WHO_USES_IT]]
  → [[CLAUDE_CODE]], [[ANTIGRAVITY]], [[CODEX]], [[AGENTS]]

[[WHAT_DOES_IT_ENABLE]]
  → [[MODEL_ROUTING]], [[PROVIDER_SWITCHING]], [[FALLBACK_LOGIC]]

[[WHAT_DOES_IT_DEPEND_ON]]
  → [[LITELLM]], [[LLM_PROVIDERS]], [[DOCKER]], [[MAC_STUDIO]]

[[WHAT_DEPENDS_ON_IT]]
  → [[CLAUDE_CODE]], [[AGENTS]], [[WORKFLOWS]]

[[WHAT_DATA_DOES_IT_TOUCH]]
  → [[PROMPTS]], [[MODEL_RESPONSES]], [[ROUTING_DECISIONS]]

[[WHAT_SYSTEMS_DOES_IT_CONNECT]]
  → [[NEO4J]], [[QDRANT]], [[POSTGRESQL]], [[LLM_PROVIDERS]]

[[WHAT_REPOSITORY_IMPLEMENTS_IT]]
  → github.com/worldwidebro/omniroute (or integration)

[[WHAT_AGENT_USES_IT]]
  → [[AGENT_ROUTER]], [[MODEL_SELECTION_AGENT]]

[[WHAT_WORKFLOW_USES_IT]]
  → [[PROMPT_EXECUTION_WORKFLOW]], [[LLM_INFERENCE_WORKFLOW]]

[[WHAT_DECISIONS_DOES_IT_INFORM]]
  → Which model to use, which provider to call

[[WHAT_OUTCOMES_DOES_IT_PRODUCE]]
  → [[LLM_RESPONSE]], [[ROUTING_METRICS]], [[COST_TRACKING]]

[[HOW_IS_IT_VERIFIED]]
  → [[CONNECTIVITY_TEST_2026_10_02#OMNIROUTE]]

[[WHAT_EVIDENCE_EXISTS]]
  → [[WHERE_WE_ARE#OMNIROUTE]], [[INFRASTRUCTURE#OMNIROUTE]], test results

[[WHAT_DOCUMENTS_DESCRIBE_IT]]
  → [[INFRASTRUCTURE.md#OMNIROUTE]], [[WHERE_WE_ARE.md#OMNIROUTE]]

[[WHAT_IS_ITS_CURRENT_STATE]]
  → [[WHERE_WE_ARE#SERVICES#OMNIROUTE]] = [[VERIFIED]]
```

---

## [[RECURSIVE_LOOP]] — The Company Brain Heartbeat

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

## [[RESOLUTION_RULES]]

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

## [[NAVIGATION_PATTERNS]]

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

## [[MASTER_ONTOLOGY_HIERARCHY]]

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

## [[IMPLEMENTATION]]

This ontology enables:

1. **Automated traversal** — Agent can walk from any [[BRACKET]] to any related concept
2. **Impact analysis** — "What breaks if X fails?" → Follow DEPENDS_ON edges
3. **Provenance tracking** — "Who verified this?" → Follow EVIDENCED_BY edges
4. **Completeness checking** — "Is this entity fully documented?" → Check all questions answered
5. **Consistency validation** — "Does this relationship make sense?" → Type-check against semantics
6. **Recursive learning** — New feedback updates [[KNOWLEDGE_GRAPH]] → improves next [[DECISION]]

---

## [[NEXT_ACTIONS]]

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

---

## [[EXTENDED_RELATIONSHIP_TYPES]] — 12 Additional Semantics (Unit 8)

### [[STORAGE_RELATIONSHIPS]]
```
STORED_IN      — Data location (File STORED_IN Folder)
MOUNTED_ON     — Volume binding (Folder MOUNTED_ON Filesystem)
RESIDES_ON     — Physical location (Filesystem RESIDES_ON Device)
BACKED_UP_TO   — Replica location (Data BACKED_UP_TO ExternalDrive)
MIGRATED_TO    — Movement (Data MIGRATED_TO NewLocation)
```

### [[EXECUTION_RELATIONSHIPS]]
```
EXECUTES       — Agent action (Agent EXECUTES Task)
DELEGATES_TO   — Reassignment (Manager DELEGATES_TO Agent)
CHAINS_TO      — Sequential (Task CHAINS_TO NextTask)
LOOPS_OVER     — Iteration (Workflow LOOPS_OVER DataSet)
ABORTS_ON      — Failure handling (Task ABORTS_ON Error)
```

### [[LINEAGE_RELATIONSHIPS]]
```
TRANSFORMS     — Data change (RawData TRANSFORMS to CleanData)
DERIVED_FROM   — Computation (Metric DERIVED_FROM Ventures)
AGGREGATES     — Combination (Report AGGREGATES Metrics)
FILTERS        — Selection (Subset FILTERS from FullSet)
LINEAGE_CHAIN  — Full ancestry (CurrentData LINEAGE_CHAIN SourceData)
```

### [[DEPENDENCY_RELATIONSHIPS]]
```
SOFT_DEPENDS   — Recommended (Service SOFT_DEPENDS on Cache)
HARD_DEPENDS   — Required (Agent HARD_DEPENDS on Capability)
CIRCULAR_WITH  — Mutual dependency (A CIRCULAR_WITH B)
BLOCKS_UNTIL   — Blocker (Task BLOCKS_UNTIL Condition)
WAITS_FOR      — Synchronization (Agent WAITS_FOR Signal)
```

### [[ANNOTATION_RELATIONSHIPS]]
```
COMMENTED_BY   — Discussion (Document COMMENTED_BY Reviewer)
FLAGGED_BY     — Marking (Entity FLAGGED_BY QA)
APPROVED_BY    — Authorization (Change APPROVED_BY Authority)
REJECTED_BY    — Denial (Change REJECTED_BY Authority)
REVISED_BY     — Editing (Document REVISED_BY Author)
```

### [[EVIDENCE_RELATIONSHIPS]]
```
EVIDENCE_LOG   — Proof collection (Claim EVIDENCE_LOG [Test1, Test2])
VERIFIED_AT    — Timestamp (Evidence VERIFIED_AT DateTime)
CONFIDENCE     — Certainty metric (Assertion CONFIDENCE 0.95)
SUPERSEDED_BY  — Obsolescence (OldData SUPERSEDED_BY NewData)
CONTRADICTED   — Conflict (Claim1 CONTRADICTED Claim2)
```

### [[TEMPORAL_RELATIONSHIPS]]
```
CREATED_AT     — Birth timestamp (Entity CREATED_AT DateTime)
MODIFIED_AT    — Last change (Entity MODIFIED_AT DateTime)
DEPRECATED_AT  — Expiry (Service DEPRECATED_AT DateTime)
ARCHIVED_AT    — Historical (Document ARCHIVED_AT DateTime)
VALID_UNTIL    — Expiration (Credential VALID_UNTIL DateTime)
```

### [[AUTHORITY_RELATIONSHIPS]]
```
OWNED_BY       — Owner (Resource OWNED_BY Organization)
MANAGED_BY     — Manager (Service MANAGED_BY Team)
GOVERNED_BY    — Policy (Action GOVERNED_BY Policy)
AUDITED_BY     — Oversight (Account AUDITED_BY Auditor)
AUTHORIZED_BY  — Permission (Access AUTHORIZED_BY SecOps)
```

### [[COMPOSITION_RELATIONSHIPS]]
```
COMPOSED_OF    — Parts (System COMPOSED_OF Subsystems)
EMBEDDED_IN    — Nesting (Component EMBEDDED_IN Container)
LAYER_IN       — Stratification (Feature LAYER_IN Application)
EXTENDS        — Inheritance (SpecializedClass EXTENDS BaseClass)
IMPLEMENTS     — Interface (Concrete IMPLEMENTS Interface)
```

### [[MAPPING_RELATIONSHIPS]]
```
ALIAS_FOR      — Name variant (Nickname ALIAS_FOR RealName)
EQUIVALENT_TO  — Semantic match (Term1 EQUIVALENT_TO Term2)
MAPS_TO        — Translation (SourceID MAPS_TO TargetID)
RESOLVES_TO    — Final reference (Bracket RESOLVES_TO Entity)
NORMALIZED_AS  — Canonical form (VariantForm NORMALIZED_AS StandardForm)
```

### [[MEASUREMENT_RELATIONSHIPS]]
```
MEASURES       — Metric (SLA MEASURES Availability)
THRESHOLD_SET  — Limit (Metric THRESHOLD_SET 99.9%)
TRIGGERS_ALERT — Action (Metric TRIGGERS_ALERT OnFailure)
TRACKED_BY     — Monitoring (Service TRACKED_BY Dashboard)
REPORTED_IN    — Aggregation (Metric REPORTED_IN Report)
```

### [[FALLBACK_RELATIONSHIPS]]
```
PRIMARY_IS     — First choice (Service PRIMARY_IS MainServer)
FALLBACK_TO    — Backup (MainServer FALLBACK_TO ReplicaServer)
FAILOVER_TO    — Emergency (FailedService FAILOVER_TO Backup)
CASCADES_TO    — Propagation (Failure CASCADES_TO DependentSystems)
RECOVERY_FROM  — Restoration (System RECOVERY_FROM Backup)
```

**Relationship Coverage: 45+ types total (7 original categories + 12 new = complete semantic grammar)**

---

## [[COMPLETE_TRAVERSAL_PATHS]] — End-to-End Navigation (Unit 9)

### Path 1: User → Ventures They Control
```
[[WHOAMI#Person]]
  ↓ [[OWNS]] 
[[OPERATING_COMPANY]]
  ↓ [[OPERATES_IN]]
[[SECTOR]]
  ↓ [[CONTAINS]]
[[VENTURE]]
  ↓ [[GENERATES]]
[[REVENUE_STREAM]]
  ↓ [[ATTRIBUTED_TO]]
[[FINANCIAL_PROFILE]]
  → Result: Map person → company ownership → sector scope → ventures → revenue
```

### Path 2: Venture → Revenue Loops
```
[[VENTURE]]
  ↓ [[EXECUTES]]
[[WORKFLOW]]
  ↓ [[INCLUDES]]
[[REVENUE_LOOP]]  (lead-gen → sales → delivery → collection → retention)
  ↓ [[TRACKS]]
[[METRIC]]
  ↓ [[INFORMS]]
[[DECISION]]
  ↓ [[RESULTS_IN]]
[[ACTION]]
  → Result: From venture through full revenue cycle to decisions and actions
```

### Path 3: Repository → Deployed Ventures
```
[[REPOSITORY]]
  ↓ [[IMPLEMENTS]]
[[CAPABILITY]]
  ↓ [[ENABLES]]
[[AGENT]]
  ↓ [[EXECUTES]]
[[DEPLOYMENT]]
  ↓ [[RUNS_ON]]
[[VENTURE]]
  ↓ [[GENERATES]]
[[OUTCOME]]
  → Result: Code lineage from repository through execution to business outcome
```

### Path 4: Agent → Decisions It Made
```
[[AGENT]]
  ↓ [[EXECUTES]]
[[TASK]]
  ↓ [[BASED_ON]]
[[CONTEXT_DATA]]
  ↓ [[INFORMS]]
[[LAYA_DECISION]]  (confidence-gated L1/L2/L3)
  ↓ [[LOGGED_IN]]
[[NEO4J_GRAPH]]
  ↓ [[REFERENCES]]
[[DECISION_AUTHORITY]]
  → Result: Agent decision trail from task through reasoning to authority approval
```

### Path 5: Capability → Ventures Using It
```
[[CAPABILITY]]
  ↓ [[MAPPED_TO]]
[[SKILL_REGISTRY]]
  ↓ [[AVAILABLE_TO]]
[[AGENT]]
  ↓ [[EXECUTES]]
[[WORKFLOW]]
  ↓ [[USED_BY]]
[[VENTURE]]
  ↓ [[CREATES_VALUE_FOR]]
[[STAKEHOLDER]]
  → Result: Capability discovery from registry through execution to business value
```

### Path 6: File → Storage → Mount → Device
```
[[FILE]]
  ↓ [[STORED_IN]]
[[FOLDER]]
  ↓ [[MOUNTED_ON]]
[[FILESYSTEM]]
  ↓ [[RESIDES_ON]]
[[VOLUME]]
  ↓ [[ATTACHED_TO]]
[[DEVICE]]
  ↓ [[CONNECTIVITY]]
[[NETWORK]]
  → Result: Complete data lineage from logical file to physical hardware and network
```

### Path 7: Obsidian Document → Neo4j Entity
```
[[MARKDOWN_FILE]]
  ↓ [[CONTAINS]]
[[WIKI_LINK]]
  ↓ [[REFERENCES]]
[[BRACKET_ENTITY]]
  ↓ [[RESOLVES_TO]]
[[MASTER_ONTOLOGY_ENTITY]]
  ↓ [[REPRESENTS]]
[[NEO4J_NODE]]
  ↓ [[CONNECTED_VIA]]
[[NEO4J_EDGE]]
  → Result: Knowledge source bridge from human-readable markdown to machine graph
```

### Path 8: Decision → Evidence → Reality → Action
```
[[DECISION]]
  ↓ [[BASED_ON]]
[[EVIDENCE]]
  ↓ [[VALIDATES]]
[[ASSERTION]]
  ↓ [[STATUS]]
[[WHERE_WE_ARE#Current_State]]
  ↓ [[INFORMS]]
[[ACTION_PLAN]]
  ↓ [[EXECUTES_TO]]
[[OUTCOME]]
  → Result: Fully validated decision-to-action chain with evidence and reality checks
```

### Path 9: Task Blocker → Resolution → Unblocking
```
[[TASK]]
  ↓ [[BLOCKED_BY]]
[[BLOCKER]]
  ↓ [[ESCALATES_TO]]
[[DECISION_AUTHORITY]]
  ↓ [[APPROVES]]
[[RESOLUTION]]
  ↓ [[REMOVES]]
[[BLOCKER_CLEARED]]
  ↓ [[UNBLOCKS]]
[[TASK]]  (now executable)
  → Result: Complete blocker lifecycle from identification through resolution
```

**Traversal Coverage: 9 complete end-to-end paths showing full navigation from any starting point**

---

**This is what makes the Company Brain navigable instead of just readable.**

**Every [[BRACKET]] is now a semantic entity. Every relationship is now a queryable arc.**

**The loop is complete: REALITY → DATA → KNOWLEDGE → DECISION → ACTION → OUTCOME → FEEDBACK → LEARNING → IMPROVED CAPABILITY ↺**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[OBSIDIAN_MASTER_ONTOLOGY.md]]

**Master grammar v1.1: 45+ relationship types, 9 complete traversal paths, machine navigation enabled.**

# Appendix: Cognition, Thinking, and Question Cross-Links

## 10. The Reality Resolution Loop (Questions)

```text
[[QUESTION]]
    [[TARGETS]] → [[ENTITY]]

[[QUESTION]]
    [[SEEKS]] → [[KNOWLEDGE]]

[[QUESTION]]
    [[IDENTIFIES]] → [[KNOWLEDGE_GAP]]

[[QUESTION]]
    [[REQUIRES]] → [[EVIDENCE]]

[[QUESTION]]
    [[ROUTES_TO]] → [[AGENT]]

[[QUESTION]]
    [[USES]] → [[TOOL]]

[[QUESTION]]
    [[SEARCHES]] → [[SOURCE]]

[[QUESTION]]
    [[GENERATES]] → [[TASK]]

[[QUESTION]]
    [[INFORMS]] → [[DECISION]]

[[QUESTION]]
    [[TRIGGERS]] → [[ACTION]]

[[ANSWER]]
    [[ANSWERS]] → [[QUESTION]]

[[EVIDENCE]]
    [[SUPPORTS]] → [[ANSWER]]

[[VERIFICATION]]
    [[VERIFIES]] → [[ANSWER]]

[[ANSWER]]
    [[UPDATES]] → [[KNOWLEDGE]]

[[FOLLOWUP_QUESTION]]
    [[FOLLOWS]] → [[ANSWER]]
```

## 11. The Reasoning Loop (Thinking Frameworks)

```text
[[QUESTION]]
    [[REQUIRES]] → [[THINKING_FRAMEWORK]]

[[THINKING_FRAMEWORK]]
    [[OPERATES_ON]] → [[PROBLEM]]

[[THINKING_FRAMEWORK]]
    [[USES]] → [[EVIDENCE]]

[[THINKING_FRAMEWORK]]
    [[GENERATES]] → [[INSIGHT]]

[[INSIGHT]]
    [[INFORMS]] → [[DECISION]]

[[DECISION]]
    [[TRIGGERS]] → [[ACTION]]

[[ACTION]]
    [[PRODUCES]] → [[OUTCOME]]

[[OUTCOME]]
    [[GENERATES]] → [[FEEDBACK]]

[[FEEDBACK]]
    [[UPDATES]] → [[KNOWLEDGE]]
```

## 12. The Learning Path (Cognitive Reading Order)

```text
[[READING_ORDER]]
    [[DEFINES]] → [[AWARENESS]]

[[AWARENESS]]
    [[ENABLES]] → [[UNDERSTANDING]]

[[UNDERSTANDING]]
    [[EMPOWERS]] → [[THINKING]]

[[THINKING]]
    [[PRODUCES]] → [[REASONING]]

[[REASONING]]
    [[GENERATES]] → [[QUESTION]]

[[QUESTION]]
    [[DEMANDS]] → [[EVIDENCE]]

[[EVIDENCE]]
    [[REQUIRES]] → [[VERIFICATION]]

[[VERIFICATION]]
    [[FORMS]] → [[KNOWLEDGE]]

[[KNOWLEDGE]]
    [[INFORMS]] → [[DECISION]]

[[DECISION]]
    [[TRIGGERS]] → [[ACTION]]

[[ACTION]]
    [[YIELDS]] → [[LEARNING]]
```

## 13. The Knowledge Artifact Lifecycle

```text
[[OBSERVATION]]
    [[BECOMES]] → [[NOTE]]

[[DOCUMENT]]
    [[EXTRACTED_TO]] → [[INDEX]]

[[INDEX]]
    [[ORGANIZED_BY]] → [[CATALOG]]

[[CATALOG]]
    [[STRUCTURED_BY]] → [[ONTOLOGY]]

[[ONTOLOGY]]
    [[FEEDS]] → [[KNOWLEDGE_GRAPH]]

[[KNOWLEDGE_GRAPH]]
    [[GUIDES]] → [[READING_PATH]]

[[READING_PATH]]
    [[BUILDS]] → [[UNDERSTANDING]]
```

## 14. The Capability and Execution Loop

```text
[[CAPABILITY]]
    [[IMPLEMENTED_BY]] → [[AGENT]]
    [[ENABLED_BY]] → [[SKILL]]
    [[EXECUTED_WITH]] → [[TOOL]]
    [[CONNECTED_BY]] → [[MCP]]
    [[EXPOSED_BY]] → [[CLI]]
    [[POWERED_BY]] → [[MODEL]]

[[AGENT]]
    [[HAS_CAPABILITY]] → [[CAPABILITY]]
    [[HAS_SKILL]] → [[SKILL]]
    [[USES_TOOL]] → [[TOOL]]
    [[USES_MCP]] → [[MCP]]
    [[USES_CLI]] → [[CLI]]
    [[USES_MODEL]] → [[MODEL]]
    [[EXECUTES]] → [[TASK]]
    [[DELEGATES_TO]] → [[AGENT]]
    [[REPORTS_TO]] → [[AGENT]]
    [[SUPERVISES]] → [[AGENT]]
    [[HANDOFFS_TO]] → [[AGENT]]
    [[ESCALATES_TO]] → [[AGENT]]
    [[PRODUCES]] → [[ARTIFACT]]
```

## 15. The Company Brain Control Architecture

```text
[[WHOAMI]]
    [[GUIDED_BY]] → [[MISSION]]

[[MISSION]]
    [[ENFORCED_BY]] → [[DIRECTIVES]]

[[DIRECTIVES]]
    [[COORDINATED_BY]] → [[EXECUTIVES]]

[[EXECUTIVES]]
    [[PRIORITIZE]] → [[OBJECTIVES]]

[[OBJECTIVES]]
    [[DECOMPOSED_BY]] → [[ORCHESTRATOR]]

[[ORCHESTRATOR]]
    [[DELEGATES_TO]] → [[AGENTS]]

[[AGENTS]]
    [[PRODUCE]] → [[OUTCOMES]]

[[OUTCOMES]]
    [[MONITORED_BY]] → [[OBSERVABILITY]]

[[OBSERVABILITY]]
    [[TRIGGERS]] → [[SELF_HEALING]]

[[SELF_HEALING]]
    [[REQUIRES]] → [[VERIFICATION]]

[[VERIFICATION]]
    [[UPDATES]] → [[LEARNING]]

[[LEARNING]]
    [[INFORMS]] → [[KNOWLEDGE_GRAPH]]

[[KNOWLEDGE_GRAPH]]
    [[PROVIDES]] → [[NEW_CONTEXT]]
```

## 16. The Full Company Brain Global Graph

```text
[[WHOAMI]] → [[MISSION]] → [[PRINCIPLES]] → [[DIRECTIVES]] → [[EXECUTIVES]] → [[OBJECTIVES]] → [[QUESTIONS]] → [[THINKING_FRAMEWORKS]] → [[REQUIREMENTS]] → [[CAPABILITIES]] → [[ANTIGRAVITY]] → [[ORCHESTRATOR]]

[[ORCHESTRATOR]]
    [[EXECUTES_VIA]] → [[AGENTS]]

[[AGENTS]]
    [[USES_SKILLS]] → [[SKILLS]]
    [[USES_TOOLS]] → [[TOOLS]]
    [[CONNECTS_VIA]] → [[MCP]]
    [[CONNECTS_VIA]] → [[CLI]]
    [[CONNECTS_VIA]] → [[API]]
    [[REASONS_VIA]] → [[MODELS]]

[[MODELS]] → [[EXECUTION]] → [[ARTIFACTS]] → [[TESTING]] → [[VERIFICATION]] → [[REALITY]] → [[OUTCOME]] → [[OBSERVABILITY]] → [[SELF_HEALING]] → [[LEARNING]] → [[KNOWLEDGE_GRAPH]] → [[REGISTRIES]] → [[NEW_CONTEXT]]
```

## 17. The Capability Supply Chain (AAS)

```text
[[REQUIREMENT]] → [[CAPABILITY_GAP]] → [[SKILL_DISCOVERY]] → [[SKILL_SELECTION]] → [[SKILL_COMPOSITION]] → [[AGENT]]

[[STARRED_REPOSITORY]]
    [[ANALYZED_BY]] → [[REPOSITORY_INTELLIGENCE]]
    [[EXTRACTS]] → [[SKILL]]
    [[MAPS_TO]] → [[CAPABILITY]]
    [[MATCHES_TO]] → [[AGENT]]
    [[EXECUTES]] → [[TASK]]
    [[PRODUCES]] → [[OUTCOME]]

[[REALITY]] → [[OBSERVATION]] → [[KNOWLEDGE]] → [[QUESTION]] → [[THINKING_FRAMEWORK]] → [[REQUIREMENT]] → [[CAPABILITY_GAP]] → [[CAPABILITY_DISCOVERY]] → [[AAS]] → [[SKILL_SELECTION]] → [[SKILL_COMPOSITION]] → [[DIRECTIVE]] → [[EXECUTIVE]] → [[ORCHESTRATOR]] → [[AGENT]] → [[SKILL]] → [[TOOL]] → [[ACTION]] → [[OUTCOME]] → [[OBSERVABILITY]] → [[SELF_HEALING]] → [[VERIFICATION]] → [[EVIDENCE]] → [[KNOWLEDGE_GRAPH]] → [[REGISTRIES]] → [[CAPABILITY_GROWTH]]
```

## 18. The Recursive Capability Loop (FIND-SKILLS)

```text
[[CAPABILITY_GAP]]
    [[RESOLVED_BY]] → [[FIND_SKILLS]]

[[FIND_SKILLS]]
    [[SEARCHES]] → [[AAS]]
    [[EVALUATES]] → [[SKILL_CANDIDATES]]
    [[PRODUCES]] → [[SKILL_SELECTION]]

[[NO_RESULT]]
    [[TRIGGERS]] → [[CREATE_NEW_SKILL]]
    [[UPDATES]] → [[SKILL_REGISTRY]]
```

## 19. The Skill Intelligence Value Chain

```text
[[GITHUB_STAR]]
    [[INGESTED_BY]] → [[SKILL_INTELLIGENCE]]
    [[NORMALIZED_INTO]] → [[CANONICAL_SKILL_NODE]]
    [[MAPPED_TO]] → [[CAPABILITY]]
    [[DISCOVERED_BY]] → [[FIND_SKILLS]]
    [[EXECUTED_BY]] → [[AGENT]]
    [[GENERATES]] → [[BUSINESS_VALUE]]
    [[ATTRIBUTED_TO]] → [[REVENUE_ATTRIBUTION]]
```
