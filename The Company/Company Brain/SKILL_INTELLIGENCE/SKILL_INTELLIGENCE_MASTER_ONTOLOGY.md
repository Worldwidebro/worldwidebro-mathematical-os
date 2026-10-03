---
type: intelligence-node
status: conceptual
prerequisites: []
requires: []
---
# `SKILL_INTELLIGENCE_MASTER_ONTOLOGY.md`

[[SKILL_INTELLIGENCE]]
├── [[IDENTITY]]
│   ├── [[SKILL_INTELLIGENCE_ENGINE]]
│   ├── [[INGESTION_SYSTEM]]
│   ├── [[NORMALIZATION_SYSTEM]]
│   └── [[CAPABILITY_GRAPH_BUILDER]]
│
├── [[INGESTION_SOURCES]]
│   ├── [[STARRED_REPOSITORIES]]
│   ├── [[AAS_INDEX]]
│   ├── [[ANTIGRAVITY_SKILLS]]
│   ├── [[CLAUDE_SKILLS]]
│   ├── [[CODEX_SKILLS]]
│   ├── [[MCP_SERVERS]]
│   └── [[LOCAL_WORKFLOWS]]
│
├── [[NORMALIZATION]]
│   ├── [[FORMAT_ALIGNMENT]]
│   ├── [[SCHEMA_VALIDATION]]
│   ├── [[METADATA_EXTRACTION]]
│   ├── [[AUTHOR_RESOLUTION]]
│   └── [[DEPENDENCY_MAPPING]]
│
├── [[DEDUPLICATION]]
│   ├── [[EXACT_MATCH_DETECTION]]
│   ├── [[SEMANTIC_SIMILARITY]]
│   ├── [[CAPABILITY_COLLISION]]
│   ├── [[CANONICAL_SELECTION]]
│   └── [[ALIAS_MAPPING]]
│
├── [[CAPABILITY_MAPPING]]
│   ├── [[DOMAIN_CLASSIFICATION]]
│   ├── [[TASK_IDENTIFICATION]]
│   ├── [[WORKFLOW_ATTACHMENT]]
│   ├── [[AGENT_MATCHING]]
│   └── [[TOOL_REQUIREMENTS]]
│
├── [[GRAPH_ASSEMBLY]]
│   ├── [[NODE_CREATION]]
│   ├── [[RELATIONSHIP_CREATION]]
│   ├── [[PREREQUISITE_LINKING]]
│   └── [[GRAPH_VALIDATION]]
│
├── [[INTELLIGENCE_ROUTING]]
│   ├── [[AGENT_CAPABILITY_UPDATE]]
│   ├── [[REGISTRY_SYNC]]
│   ├── [[FIND_SKILLS_INDEX_UPDATE]]
│   └── [[ORCHESTRATOR_NOTIFICATION]]
│
└── [[BUSINESS_ALIGNMENT]]
    ├── [[REVENUE_ATTRIBUTION]]
    ├── [[COST_ANALYSIS]]
    ├── [[ROI_TRACKING]]
    └── [[STRATEGIC_FIT]]

---

# 1. The Skill Intelligence Engine

This is the system that continuously surveys the landscape of available tools, repositories, and playbooks, and translates them into executable capability nodes for the Company Brain.

It answers the question:
> "Given everything we have starred, installed, or discovered, what is the Company Brain actually capable of doing right now?"

---

# 2. The Ingestion Pipeline

```text
[[SOURCES]]
 ├── [[STARRED_REPOSITORIES]]
 ├── [[AAS_SKILLS_INDEX]]
 ├── [[ANTIGRAVITY_SKILL_DIR]]
 ├── [[CLAUDE_PLUGIN_DIR]]
 └── [[MCP_REGISTRY]]
       ↓
[[INGESTION_ENGINE]]
       ↓
[[RAW_SKILL_DATA]]
```

---

# 3. Normalization and Deduplication

Skills come in many formats (SKILL.md, MCP JSON, Python scripts). They must be normalized.

```text
[[RAW_SKILL_DATA]]
       ↓
[[NORMALIZATION]]
       ↓
[[SEMANTIC_ANALYSIS]]
       ↓
[[DEDUPLICATION_ENGINE]]
       ↓
   COLLISION?
   /        \
 YES         NO
  ↓          ↓
MERGE    REGISTER_NEW
  ↓          ↓
[[CANONICAL_SKILL_NODE]]
```

---

# 4. Capability Mapping

A skill is just a file until it is mapped to a capability.

```text
[[CANONICAL_SKILL_NODE]]
       ↓
WHAT DOES IT DO?
       ↓
[[CAPABILITY_MAPPING]]
       ↓
WHICH AGENT CAN USE IT?
       ↓
[[AGENT_MATCHING]]
       ↓
WHAT DOES IT REQUIRE?
       ↓
[[TOOL_DEPENDENCY_MAPPING]]
```

---

# 5. The Ultimate Value Chain

This pipeline finally bridges the gap between a developer starring a GitHub repository and the company generating revenue:

```text
[[GITHUB_STAR]]
       ↓
[[SKILL_INTELLIGENCE]]
       ↓
[[CAPABILITY_NODE]]
       ↓
[[FIND_SKILLS]]
       ↓
[[ORCHESTRATOR]]
       ↓
[[AGENT]]
       ↓
[[EXECUTION]]
       ↓
[[BUSINESS_VALUE]]
       ↓
[[REVENUE_ATTRIBUTION]]
```

---

# 6. Graph Synchronization

Once a skill is normalized and mapped, it must be pushed into the global knowledge graph:

```text
[[SKILL_INTELLIGENCE]]
       ↓
[[NEO4J_UPDATE]]
       ↓
[[SKILL_REGISTRY_UPDATE]]
       ↓
[[CAPABILITY_REGISTRY_UPDATE]]
       ↓
[[COMPANY_BRAIN_AWARENESS]]
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
