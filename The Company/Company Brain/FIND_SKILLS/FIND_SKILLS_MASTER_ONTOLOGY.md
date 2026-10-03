---
type: meta-skill
status: conceptual
prerequisites: []
requires: []
---
# `FIND_SKILLS_MASTER_ONTOLOGY.md`

[[FIND_SKILLS]]
├── [[IDENTITY]]
│   ├── [[FIND_SKILLS_SKILL]]
│   ├── [[META_SKILL]]
│   ├── [[SKILL_DISCOVERY_AGENT]]
│   ├── [[CAPABILITY_DISCOVERY]]
│   └── [[SKILL_SUPPLY_CHAIN_ENTRYPOINT]]
│
├── [[TRIGGER]]
│   ├── [[HOW_DO_I]]
│   ├── [[FIND_A_SKILL]]
│   ├── [[IS_THERE_A_SKILL]]
│   ├── [[CAN_YOU_DO]]
│   ├── [[EXTEND_CAPABILITIES]]
│   ├── [[FIND_TOOLS]]
│   ├── [[FIND_TEMPLATES]]
│   └── [[FIND_WORKFLOWS]]
│
├── [[REQUEST_UNDERSTANDING]]
│   ├── [[DOMAIN]]
│   ├── [[TASK]]
│   ├── [[SPECIALIZED_CAPABILITY]]
│   ├── [[USER_INTENT]]
│   ├── [[CONSTRAINTS]]
│   └── [[SKILL_LIKELIHOOD]]
│
├── [[DISCOVERY]]
│   ├── [[SKILLS_SH]]
│   ├── [[LEADERBOARD]]
│   ├── [[SEARCH_STRATEGY]]
│   ├── [[KEYWORDS]]
│   ├── [[ALTERNATIVE_TERMS]]
│   ├── [[OWNER_FILTER]]
│   └── [[REPOSITORY_SEARCH]]
│
├── [[CLI_SEARCH]]
│   ├── [[NPM_SKILLS_CLI]]
│   ├── [[NPM_SKILLS_FIND]]
│   ├── [[QUERY]]
│   ├── [[OWNER]]
│   ├── [[RESULTS]]
│   └── [[CANDIDATES]]
│
├── [[QUALITY]]
│   ├── [[INSTALL_COUNT]]
│   ├── [[SOURCE_REPUTATION]]
│   ├── [[GITHUB_STARS]]
│   ├── [[AUTHOR]]
│   ├── [[REPOSITORY]]
│   ├── [[RECENCY]]
│   ├── [[MAINTENANCE]]
│   └── [[EVIDENCE]]
│
├── [[EVALUATION]]
│   ├── [[RELEVANCE]]
│   ├── [[CAPABILITY_MATCH]]
│   ├── [[DOMAIN_MATCH]]
│   ├── [[TASK_MATCH]]
│   ├── [[QUALITY_ASSESSMENT]]
│   ├── [[TRUST]]
│   ├── [[COMPATIBILITY]]
│   └── [[RISK]]
│
├── [[RECOMMENDATION]]
│   ├── [[SKILL_NAME]]
│   ├── [[PURPOSE]]
│   ├── [[INSTALL_COUNT_METRIC]]
│   ├── [[SOURCE]]
│   ├── [[INSTALL_COMMAND]]
│   ├── [[SKILLS_SH_URL]]
│   └── [[ALTERNATIVES]]
│
├── [[INSTALLATION]]
│   ├── [[SKILLS_ADD]]
│   ├── [[PACKAGE]]
│   ├── [[GLOBAL]]
│   ├── [[PROJECT]]
│   ├── [[CONFIRMATION]]
│   └── [[INSTALL_VERIFICATION]]
│
├── [[NO_RESULT]]
│   ├── [[NO_MATCH]]
│   ├── [[DIRECT_EXECUTION]]
│   ├── [[CREATE_NEW_SKILL]]
│   └── [[SKILLS_INIT]]
│
└── [[LEARNING]]
    ├── [[DISCOVERY_RESULT]]
    ├── [[SKILL_USAGE]]
    ├── [[SUCCESS]]
    ├── [[FAILURE]]
    ├── [[RATING]]
    ├── [[PERFORMANCE]]
    └── [[REGISTRY_UPDATE]]

---

# 1. The crucial distinction

The normal skill architecture is:
```text
[[TASK]] ↓ [[SKILL]] ↓ [[EXECUTION]]
```

find-skills inserts a meta-layer:
```text
[[TASK]] ↓ [[CAPABILITY_GAP]] ↓ [[FIND_SKILLS]] ↓ [[SKILL_DISCOVERY]] ↓ [[SKILL_SELECTION]] ↓ [[SKILL]] ↓ [[EXECUTION]]
```

find-skills is a capability-discovery mechanism, not merely a task-execution skill.

---

# 2. find-skills is a meta-skill

```text
[[FIND_SKILLS]]
├── [[META_SKILL]]
├── [[DISCOVERY_SKILL]]
├── [[ROUTING_SKILL]]
├── [[CAPABILITY_MAPPING_SKILL]]
├── [[RECOMMENDATION_SKILL]]
└── [[INSTALLATION_GATEWAY]]
```

It doesn't primarily teach an agent how to perform the task. It teaches the agent **how to determine whether another reusable capability exists for the task**.

---

# 3. Its trigger ontology

```text
[[USER_REQUEST]]
 │
 ├── "How do I X?"
 │       ↓
 │ [[CAPABILITY_DISCOVERY]]
 │
 ├── "Find a skill for X"
 │       ↓
 │ [[SKILL_SEARCH]]
 │
 ├── "Is there a skill that can X?"
 │       ↓
 │ [[SKILL_EXISTENCE_QUERY]]
 │
 ├── "Can you X?"
 │       ↓
 │ [[CAPABILITY_GAP_ANALYSIS]]
 │
 ├── "Find a tool for X"
 │       ↓
 │ [[TOOL_DISCOVERY]]
 │
 └── "Find a workflow for X"
         ↓
   [[WORKFLOW_DISCOVERY]]
```

---

# 4. Question → skill discovery

This is the connection I'd make canonical:

```text
[[QUESTION]]
       ↓
[[QUESTION_INTENT]]
       ↓
[[CAPABILITY_REQUIRED]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[FIND_SKILLS]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_CANDIDATES]]
       ↓
[[SKILL_EVALUATION]]
       ↓
[[SKILL_SELECTION]]
```

---

# 5. The discovery pipeline

```text
[[REQUEST]]
       ↓
[[UNDERSTAND]]
       ↓
[[DOMAIN]]
       ↓
[[TASK]]
       ↓
[[CAPABILITY]]
       ↓
[[SEARCH_LEADERBOARD]]
       ↓
[[SEARCH_SKILLS]]
       ↓
[[COLLECT_CANDIDATES]]
       ↓
[[FILTER]]
       ↓
[[EVALUATE]]
       ↓
[[COMPARE]]
       ↓
[[SELECT]]
       ↓
[[INSTALL_OR_USE]]
       ↓
[[VERIFY]]
```

---

# 6. Leaderboard as discovery intelligence

```text
[[SKILLS_SH]]
       ↓
[[LEADERBOARD]]
       ↓
[[POPULARITY_SIGNAL]]
       ↓
[[CANDIDATE_DISCOVERY]]
```

But your Company Brain distinguishes:
```text
[[POPULAR]] ≠ [[RELEVANT]]
[[POPULAR]] ≠ [[HIGH_QUALITY]]
[[HIGH_INSTALL_COUNT]] ≠ [[VERIFIED_FOR_THIS_TASK]]
```

Expanded signal ontology:
```text
[[DISCOVERY_SIGNAL]]
├── [[INSTALL_COUNT]]
├── [[GITHUB_STARS]]
├── [[SOURCE_REPUTATION]]
├── [[RECENCY]]
├── [[MAINTENANCE]]
├── [[DOCUMENTATION]]
├── [[COMPATIBILITY]]
├── [[TASK_RELEVANCE]]
└── [[VERIFIED_PERFORMANCE]]
```

---

# 7. The skill evaluator

```text
[[SKILL_EVALUATION_AGENT]]

CANDIDATE
       ↓
RELEVANCE CHECK
       ↓
SOURCE CHECK
       ↓
QUALITY CHECK
       ↓
COMPATIBILITY CHECK
       ↓
SECURITY CHECK
       ↓
TASK FIT
       ↓
EVIDENCE
       ↓
RECOMMENDATION
```

And importantly: `SEARCH_RESULT ≠ EVALUATED_SKILL`

---

# 8. Skill selection scoring

Use dimensions rather than one opaque number:

```text
[[SKILL_FIT]]
├── [[TASK_RELEVANCE]]
├── [[DOMAIN_RELEVANCE]]
├── [[CAPABILITY_MATCH]]
├── [[SOURCE_TRUST]]
├── [[COMMUNITY_SIGNAL]]
├── [[MAINTENANCE]]
├── [[COMPATIBILITY]]
├── [[SECURITY]]
├── [[DEPENDENCIES]]
├── [[INSTALLABILITY]]
└── [[VERIFICATION_STATUS]]
```

---

# 9. npx skills becomes a capability package manager

```text
[[SKILLS_CLI]]
├── [[FIND]]
├── [[ADD]]
├── [[UPDATE]]
├── [[USE]]
├── [[LIST]]
├── [[REMOVE]]
└── [[INIT]]
```

This makes the CLI: **package-management infrastructure for agent capabilities**.

---

# 10. The really important command: skills use

```text
[[SKILL_LIFECYCLE]]
DISCOVER
       ↓
INSPECT
       ↓
USE ├── temporary capability
       ↓
INSTALL ├── persistent capability
       ↓
UPDATE
       ↓
REMOVE
```

This separates `[[EXPERIMENTAL_CAPABILITY]]` from `[[APPROVED_INSTALLED_CAPABILITY]]`.

---

# 11. find-skills + AAS

```text
       [[AAS]]
          │
  [[SKILL_LIBRARY]]
          │
  [[SKILL_CATALOG]]
          │
          ↓
   [[FIND_SKILLS]]
          │
  ┌───────┼───────┐
  ↓       ↓       ↓
[[SEARCH]] [[LEADERBOARD]] [[FILTER]]
  │       │       │
  └───────┼───────┘
          ↓
   [[CANDIDATES]]
          ↓
   [[EVALUATION]]
          ↓
   [[SELECTION]]
          ↓
  [[SKILL_STACK]]
          ↓
      [[AGENT]]
```
AAS = capability universe
find-skills = capability discovery/routing mechanism

---

# 12. find-skills + Antigravity

```text
[[ANTIGRAVITY]]
       ↓
[[TASK]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[FIND_SKILLS]]
       ↓
[[SKILLS_SH]]
       ↓
[[SKILL_DISCOVERY]]
       ↓
[[SKILL_EVALUATION]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[ANTIGRAVITY_SKILL]]
       ↓
[[AGENT_EXECUTION]]
```

---

# 13. The recursive capability loop

```text
[[AGENT]]
       ↓
"CAN I DO THIS?"
       ↓
[[CAPABILITY_CHECK]]
       ↓
┌──────┴──────┐
│             │
↓             ↓
[[YES]]         [[NO]]
│             │
↓             ↓
EXECUTE [[FIND_SKILLS]]
              ↓
      [[DISCOVER_SKILLS]]
              ↓
         [[EVALUATE]]
              ↓
          [[SELECT]]
              ↓
        [[INSTALL/USE]]
              ↓
          [[AGENT]]
              ↓
         [[EXECUTE]]
```

This gives your agents capability self-expansion.

---

# 14. Governance gate

```text
[[FIND_SKILLS]]
       ↓
[[CANDIDATE]]
       ↓
[[INSPECT]]
       ↓
[[TRUST]]
       ↓
[[COMPATIBILITY]]
       ↓
[[SECURITY]]
       ↓
[[APPROVAL]]
       ↓
[[INSTALL]]
```

---

# 15. No-result behavior

```text
[[CAPABILITY_GAP]]
       ↓
[[FIND_SKILLS]]
       ↓
     FOUND?
     /    \
  YES      NO
   ↓        ↓
SELECT   [[CREATE_SKILL]]
   ↓        ↓
INSTALL  [[SKILLS_INIT]]
   ↓        ↓
EXECUTE  [[NEW_SKILL]]
   ↓        ↓
      [[SKILL_REGISTRY]]
```

That creates a capability-compounding loop.

---

# 16. The real relationship to your Company Brain

```text
[[REALITY]]
       ↓
[[QUESTION]]
       ↓
[[REQUIREMENT]]
       ↓
[[CAPABILITY]]
       ↓
[[CAPABILITY_GAP]]
       ↓
[[FIND_SKILLS]]
       ↓
[[SKILL_SEARCH]]
       ↓
[[SKILL_CANDIDATES]]
       ↓
[[SKILL_EVALUATION]]
       ↓
[[SKILL_SELECTION]]
       ↓
[[SKILL_STACK]]
       ↓
[[AGENT]]
       ↓
[[EXECUTION]]
       ↓
[[OUTCOME]]
       ↓
[[VERIFICATION]]
       ↓
[[EVIDENCE]]
       ↓
[[KNOWLEDGE_GRAPH]]
       ↓
[[CAPABILITY_REGISTRY]]
       ↺
```

The three-layer canonical model:
```text
[[AAS]] "Where capabilities live."
       ↓
[[FIND_SKILLS]] "How agents discover capabilities."
       ↓
[[ANTIGRAVITY / CLAUDE / CODEX / OTHER HOST]] "Where agents use capabilities."
```

And underneath all three:
```text
[[COMPANY_BRAIN]]
       ↓
[[CAPABILITY_GRAPH]]
       ↓
[[SKILL_REGISTRY]]
       ↓
[[AGENT_REGISTRY]]
       ↓
[[TOOL_REGISTRY]]
       ↓
[[WORKFLOW_REGISTRY]]
       ↓
[[EVIDENCE_REGISTRY]]
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
