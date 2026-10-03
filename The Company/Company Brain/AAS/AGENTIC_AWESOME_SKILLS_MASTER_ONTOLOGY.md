---
type: capability-supply-chain
status: conceptual
prerequisites: []
requires: []
---
# `AGENTIC_AWESOME_SKILLS_MASTER_ONTOLOGY.md`

[[AGENTIC_AWESOME_SKILLS]]
├── [[IDENTITY]]
│   ├── [[AAS]]
│   ├── [[AAS_CORE]]
│   ├── [[SKILL_LIBRARY]]
│   ├── [[SKILL_CATALOG]]
│   └── [[AGENTIC_CAPABILITY_SUPPLY_CHAIN]]
│
├── [[SKILLS]]
│   ├── [[SKILL]]
│   ├── [[SKILL_MD]]
│   ├── [[SKILL_ID]]
│   ├── [[SKILL_NAME]]
│   ├── [[SKILL_DESCRIPTION]]
│   ├── [[SKILL_CATEGORY]]
│   ├── [[SKILL_TAGS]]
│   ├── [[SKILL_RISK]]
│   ├── [[SKILL_VERSION]]
│   ├── [[SKILL_SOURCE]]
│   ├── [[SKILL_DEPENDENCIES]]
│   ├── [[SKILL_TOOLS]]
│   ├── [[SKILL_MCP]]
│   ├── [[SKILL_INPUTS]]
│   ├── [[SKILL_OUTPUTS]]
│   ├── [[SKILL_PROCEDURE]]
│   └── [[SKILL_VERIFICATION]]
│
├── [[DISCOVERY]]
│   ├── [[SEARCH]]
│   ├── [[CATALOG]]
│   ├── [[INDEX]]
│   ├── [[MACHINE_READABLE_INDEX]]
│   ├── [[FILTER]]
│   ├── [[CATEGORY_FILTER]]
│   ├── [[TAG_FILTER]]
│   ├── [[RISK_FILTER]]
│   ├── [[HOST_FILTER]]
│   └── [[CAPABILITY_SEARCH]]
│
├── [[SELECTION]]
│   ├── [[AGENT_SELECTION]]
│   ├── [[SKILL_SELECTION]]
│   ├── [[EXACT_ID_SELECTION]]
│   ├── [[STACK_COMPOSITION]]
│   ├── [[BUNDLE]]
│   ├── [[WORKFLOW]]
│   └── [[SELECTION_EVIDENCE]]
│
├── [[AAS_CORE]]
│   ├── [[LOCAL_CATALOG]]
│   ├── [[MCP]]
│   ├── [[COMPOSE_STACK]]
│   ├── [[STACK_MANIFEST]]
│   ├── [[STACK_VALIDATION]]
│   ├── [[PLAN]]
│   ├── [[PLAN_PREVIEW]]
│   ├── [[APPROVAL]]
│   └── [[TRUST_BOUNDARY]]
│
├── [[INSTALLATION]]
│   ├── [[DIRECT_INSTALL]]
│   ├── [[INSTALL_PREVIEW]]
│   ├── [[DRY_RUN]]
│   ├── [[HOST_TARGET]]
│   ├── [[SKILL_DIRECTORY]]
│   ├── [[USER_SCOPE]]
│   ├── [[PROJECT_SCOPE]]
│   └── [[INSTALL_VERIFICATION]]
│
├── [[HOSTS]]
│   ├── [[CLAUDE_CODE]]
│   ├── [[CODEX]]
│   ├── [[ANTIGRAVITY]]
│   ├── [[ANTIGRAVITY_CLI]]
│   ├── [[GEMINI_CLI]]
│   ├── [[CURSOR]]
│   ├── [[KIRO]]
│   ├── [[COPILOT]]
│   ├── [[OPENCODE]]
│   └── [[CUSTOM_HOST]]
│
├── [[PLUGINS]]
│   ├── [[PLUGIN]]
│   ├── [[PLUGIN_MANIFEST]]
│   ├── [[PLUGIN_SKILLS]]
│   ├── [[SPECIALIZED_PLUGIN]]
│   ├── [[PLUGIN_COMPATIBILITY]]
│   └── [[PLUGIN_INSTALLATION]]
│
├── [[BUNDLES]]
│   ├── [[ROLE_BUNDLE]]
│   ├── [[DOMAIN_BUNDLE]]
│   ├── [[GOAL_BUNDLE]]
│   ├── [[SKILL_GROUP]]
│   └── [[BUNDLE_METADATA]]
│
├── [[WORKFLOWS]]
│   ├── [[WORKFLOW]]
│   ├── [[WORKFLOW_STEPS]]
│   ├── [[WORKFLOW_METADATA]]
│   ├── [[WORKFLOW_ORDER]]
│   ├── [[PREREQUISITES]]
│   ├── [[HANDOFFS]]
│   └── [[WORKFLOW_OUTCOME]]
│
├── [[REGISTRIES]]
│   ├── [[SKILL_REGISTRY]]
│   ├── [[SKILL_INDEX]]
│   ├── [[CATEGORY_REGISTRY]]
│   ├── [[TAG_REGISTRY]]
│   ├── [[RISK_REGISTRY]]
│   ├── [[PLUGIN_REGISTRY]]
│   ├── [[BUNDLE_REGISTRY]]
│   ├── [[WORKFLOW_REGISTRY]]
│   ├── [[HOST_REGISTRY]]
│   └── [[SOURCE_REGISTRY]]
│
├── [[VALIDATION]]
│   ├── [[STRUCTURAL_VALIDATION]]
│   ├── [[IDENTITY_VALIDATION]]
│   ├── [[SCHEMA_VALIDATION]]
│   ├── [[STACK_VALIDATION]]
│   ├── [[COMPATIBILITY_VALIDATION]]
│   ├── [[SECURITY_REVIEW]]
│   ├── [[SEMANTIC_FIT]]
│   └── [[OPERATIONAL_SAFETY]]
│
├── [[VERIFICATION]]
│   ├── [[SKILL_VERIFICATION]]
│   ├── [[INSTALL_VERIFICATION]]
│   ├── [[EXECUTION_VERIFICATION]]
│   ├── [[OUTPUT_VERIFICATION]]
│   ├── [[EVIDENCE]]
│   └── [[AUDIT]]
│
├── [[SECURITY]]
│   ├── [[RISK]]
│   ├── [[RISK_LEVEL]]
│   ├── [[TRUST_BOUNDARY]]
│   ├── [[CONTENT_REVIEW]]
│   ├── [[DEPENDENCY_REVIEW]]
│   ├── [[INSTALL_SAFETY]]
│   └── [[EXECUTION_SAFETY]]
│
├── [[LIFECYCLE]]
│   ├── [[DISCOVER]]
│   ├── [[INSPECT]]
│   ├── [[SELECT]]
│   ├── [[COMPOSE]]
│   ├── [[VALIDATE]]
│   ├── [[PREVIEW]]
│   ├── [[APPROVE]]
│   ├── [[INSTALL]]
│   ├── [[EXECUTE]]
│   ├── [[VERIFY]]
│   ├── [[UPDATE]]
│   ├── [[DEPRECATE]]
│   └── [[RETIRE]]
│
└── [[KNOWLEDGE_GRAPH]]
    ├── [[SKILL_NODE]]
    ├── [[CAPABILITY_NODE]]
    ├── [[AGENT_NODE]]
    ├── [[TOOL_NODE]]
    ├── [[MCP_NODE]]
    ├── [[WORKFLOW_NODE]]
    ├── [[REPOSITORY_NODE]]
    ├── [[HOST_NODE]]
    └── [[RELATIONSHIP_GRAPH]]

---

# 1. What this repository actually is

AAS is not the Agent. AAS is a capability/skill supply chain that lets agents discover, select, inspect, compose, validate, install, and use reusable procedures.

```text
       [[AAS]]
          │
  ┌───────┼───────┐
  ↓       ↓       ↓
[[SKILLS]] [[CATALOG]] [[DISCOVERY]]
  │       │       │
  └───────┼───────┘
          ↓
   [[SELECTION]]
          ↓
 [[STACK_COMPOSITION]]
          ↓
   [[VALIDATION]]
          ↓
   [[PLAN_PREVIEW]]
          ↓
   [[INSTALLATION]]
          ↓
       [[HOST]]
          ↓
      [[AGENT]]
          ↓
    [[EXECUTION]]
          ↓
   [[VERIFICATION]]
```

---

# 2. The fundamental ontology

```text
[[REQUIREMENT]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_COMPOSITION]]
       ↓
    [[AGENT]]
```
AAS becomes a capability acquisition mechanism.

---

# 3. The SKILL.md becomes a first-class object

```text
[[SKILL]]
├── [[SKILL_ID]]
├── [[SKILL_NAME]]
├── [[DESCRIPTION]]
├── [[PURPOSE]]
├── [[CAPABILITY]]
├── [[DOMAIN]]
├── [[CATEGORY]]
├── [[TAGS]]
├── [[RISK]]
├── [[VERSION]]
├── [[SOURCE]]
├── [[LICENSE]]
│
├── [[PREREQUISITES]]
├── [[DEPENDENCIES]]
├── [[REQUIRED_TOOLS]]
├── [[REQUIRED_MCP]]
├── [[REQUIRED_FILES]]
├── [[REQUIRED_DATA]]
│
├── [[INPUTS]]
├── [[PROCEDURE]]
├── [[DECISION_RULES]]
├── [[OUTPUTS]]
│
├── [[VALIDATION]]
├── [[FAILURE_MODES]]
├── [[SAFETY]]
├── [[EVALUATION]]
└── [[EVIDENCE]]
```

---

# 4. SKILLS_INDEX is a major Company Brain asset

```text
[[SKILLS]]
      ↓
[[SKILLS_INDEX]]
      ↓
[[MACHINE_READABLE_DISCOVERY]]
      ↓
[[CAPABILITY_REGISTRY]]
```

For your Company Brain:
```text
AAS skills_index.json
      ↓
  INGESTOR
      ↓
NORMALIZATION
      ↓
ENTITY_RESOLUTION
      ↓
CAPABILITY_MAPPING
      ↓
SKILL_REGISTRY
      ↓
   NEO4J
```

---

# 5. Catalog ≠ Registry ≠ Index

```text
CATALOG
   ↓
 INDEX
   ↓
REGISTRY
   ↓
 SCHEMA
   ↓
 SKILL
   ↓
WORKFLOW
```

---

# 6. AAS Core

```text
DISCOVERED
      ↓
  SELECTED
      ↓
  COMPOSED
      ↓
  VALIDATED
      ↓
   PLANNED
      ↓
  REVIEWED
      ↓
  APPROVED
      ↓
 INSTALLED
      ↓
  EXECUTED
      ↓
  VERIFIED
```

Not: `FOUND = INSTALLED = WORKING`

---

# 7. Skill stack ontology

```text
[[SKILL_STACK]]
├── [[STACK_ID]]
├── [[STACK_NAME]]
├── [[PURPOSE]]
├── [[OBJECTIVE]]
├── [[SKILLS]]
├── [[ORDER]]
├── [[DEPENDENCIES]]
├── [[HOST]]
├── [[COMPATIBILITY]]
├── [[VALIDATION]]
├── [[PLAN]]
├── [[APPROVAL]]
├── [[INSTALLATION]]
└── [[EVIDENCE]]
```

---

# 8. Bundles

```text
BUNDLE
   ↓
CANDIDATE SKILLS
   ↓
SELECTION
   ↓
 STACK
   ↓
ORDERING
   ↓
WORKFLOW
```

---

# 9. AAS + Antigravity

```text
[[ANTIGRAVITY]]
       ↓
[[PROJECT]]
       ↓
[[OBJECTIVE]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[AAS_DISCOVERY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_STACK]]
       ↓
[[VALIDATION]]
       ↓
[[PLAN]]
       ↓
[[ANTIGRAVITY_AGENT]]
       ↓
[[EXECUTION]]
```

---

# 10. AAS + Claude

```text
[[CLAUDE]]
       ↓
[[PROJECT_CONTEXT]]
       ↓
[[QUESTION]]
       ↓
[[REQUIREMENT]]
       ↓
[[AAS_MCP]]
       ↓
[[SKILL_SEARCH]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_STACK]]
       ↓
[[PLAN]]
       ↓
[[CLAUDE_CODE]]
       ↓
[[EXECUTION]]
```

---

# 11. AAS + Codex

```text
[[CODEX]]
       ↓
[[AAS_CORE]]
       ↓
[[MCP]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[STACK]]
       ↓
[[VALIDATION]]
       ↓
[[PLAN]]
       ↓
[[CODEX_EXECUTION]]
```

---

# 12. AAS + MCP

```text
[[AAS]]
       ↓
[[MCP_SERVER]]
       ↓
[[MCP_TOOL]]
├── [[SEARCH_SKILLS]]
├── [[READ_SKILL]]
├── [[COMPOSE_STACK]]
├── [[VALIDATE_STACK]]
└── [[PLAN]]
```

---

# 13. The recursive intelligence loop

```text
[[TASK]]
       ↓
[[REQUIREMENTS]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_COMPOSITION]]
       ↓
[[AGENT_EXECUTION]]
       ↓
[[RESULT]]
       ↓
[[VERIFICATION]]
       ↓
[[LESSON]]
       ↓
[[NEW_CAPABILITY]]
       ↓
[[NEW_SKILL]]
       ↓
[[SKILL_REGISTRY]]
       ↓
[[CAPABILITY_GRAPH]]
       ↺
```

---

# 14. AAS security ontology

```text
[[SKILL_TRUST]]
├── [[SOURCE_TRUST]]
├── [[CONTENT_TRUST]]
├── [[STRUCTURAL_VALIDITY]]
├── [[IDENTITY_VALIDITY]]
├── [[SEMANTIC_FIT]]
├── [[COMPATIBILITY]]
├── [[DEPENDENCY_SAFETY]]
├── [[INSTALL_SAFETY]]
├── [[EXECUTION_SAFETY]]
├── [[OPERATIONAL_SAFETY]]
└── [[VERIFIED_BEHAVIOR]]
```

VALID_SKILL ≠ SAFE_SKILL ≠ COMPATIBLE_SKILL ≠ APPROPRIATE_SKILL ≠ WORKING_SKILL

---

# 15. Skill provenance

```text
SKILL
   ↓
DERIVED_FROM
   ↓
SOURCE_REPOSITORY
```

---

# 16. AAS ↔ Company Brain graph

```text
[[COMPANY_BRAIN]]
       │
[[CAPABILITIES]]
       │
[[CAPABILITY_REGISTRY]]
       │
[[AAS_DISCOVERY]]
       │
   ┌───┴───┐
   ↓       ↓
[[SKILL_INDEX]] [[CATALOG]]
   │       │
   └───┬───┘
       ↓
[[SKILL_REGISTRY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_STACK]]
       ↓
[[WORKFLOW]]
       ↓
[[AGENT]]
       ↓
   ┌───┼───┐
   ↓   ↓   ↓
[[CLAUDE]] [[ANTIGRAVITY]] [[CODEX]]
   │   │   │
   └───┼───┘
       ↓
[[MCP]]
       ↓
[[TOOLS / APIs]]
       ↓
[[EXECUTION]]
       ↓
[[VERIFICATION]]
       ↓
[[EVIDENCE]]
       ↓
[[KNOWLEDGE_GRAPH]]
       ↺
```

---

# 17. The skill supply chain

```text
[[SKILL_SUPPLY_CHAIN]]
DISCOVER
   ↓
INGEST
   ↓
NORMALIZE
   ↓
IDENTIFY
   ↓
CLASSIFY
   ↓
TAG
   ↓
MAP_TO_CAPABILITY
   ↓
MAP_TO_AGENT
   ↓
MAP_TO_TOOL
   ↓
MAP_TO_MCP
   ↓
MAP_TO_WORKFLOW
   ↓
VALIDATE
   ↓
VERSION
   ↓
INSTALL
   ↓
EXECUTE
   ↓
VERIFY
   ↓
EVALUATE
   ↓
LEARN
   ↓
UPDATE_REGISTRY
   ↓
UPDATE_GRAPH
```

---

# 18. This changes your existing Company Brain ontology

```text
[[CAPABILITY]]
       ↓
[[CAPABILITY_DISCOVERY]]
       ↓
[[SKILL_CATALOG]]
       ↓
[[SKILL_MATCHING]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_STACK]]
       ↓
[[AGENT]]
       ↓
[[EXECUTION]]
```

---

# 21. The most powerful connection: Repo → Skill → Capability

```text
[[STARRED_REPOSITORY]]
       ↓
[[REPOSITORY_INTELLIGENCE]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_EXTRACTION]]
       ↓
[[SKILL_NORMALIZATION]]
       ↓
[[CAPABILITY_MAPPING]]
       ↓
[[CAPABILITY_REGISTRY]]
       ↓
[[AGENT_MATCHING]]
       ↓
[[WORKFLOW_COMPOSITION]]
       ↓
[[TASK_EXECUTION]]
       ↓
[[VERIFICATION]]
       ↓
[[OUTCOME]]
```

---

# 22. The final unified architecture

```text
[[REALITY]]
       ↓
[[OBSERVATION]]
       ↓
[[KNOWLEDGE]]
       ↓
[[QUESTION]]
       ↓
[[THINKING_FRAMEWORK]]
       ↓
[[REQUIREMENT]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[CAPABILITY_DISCOVERY]]
       ↓
[[AAS / SKILL DISCOVERY]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_COMPOSITION]]
       ↓
[[DIRECTIVE]]
       ↓
[[EXECUTIVE]]
       ↓
[[ORCHESTRATOR]]
       ↓
[[AGENT]]
       ↓
[[SKILL]]
       ↓
[[TOOL / MCP / CLI]]
       ↓
[[ACTION]]
       ↓
[[OUTCOME]]
       ↓
[[OBSERVABILITY]]
       ↓
[[SELF_HEALING]]
       ↓
[[VERIFICATION]]
       ↓
[[EVIDENCE]]
       ↓
[[KNOWLEDGE_GRAPH]]
       ↓
[[REGISTRIES]]
       ↓
[[CAPABILITY_GROWTH]]
       ↺
```

The key architectural distinction:
```text
[[ANTIGRAVITY]] = execution / agent environment
[[CLAUDE]] = intelligence / reasoning environment
[[CODEX]] = coding / reasoning environment
[[AAS]] = reusable skill + capability supply chain
[[MCP]] = tool/context connection protocol
[[OMNIROUTE]] = model/provider routing fabric
[[NEO4J]] = relationship fabric
[[QDRANT]] = semantic retrieval fabric
[[OBSIDIAN]] = human knowledge/context fabric
[[COMPANY_BRAIN]] = governance + knowledge + orchestration + execution + learning system
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
