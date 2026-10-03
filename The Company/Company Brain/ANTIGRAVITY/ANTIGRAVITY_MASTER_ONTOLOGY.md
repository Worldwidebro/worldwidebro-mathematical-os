---
type: execution-substrate
status: conceptual
prerequisites: []
requires: []
---

# `ANTIGRAVITY_MASTER_ONTOLOGY.md`

[[ANTIGRAVITY]]
├── [[IDENTITY]]
│   ├── [[ANTIGRAVITY_PLATFORM]]
│   ├── [[AGENTIC_DEVELOPMENT]]
│   ├── [[AGENT_HARNESS]]
│   ├── [[EXECUTION_ENVIRONMENT]]
│   └── [[ORCHESTRATION_SURFACE]]
│
├── [[SURFACES]]
│   ├── [[ANTIGRAVITY_2]]
│   ├── [[ANTIGRAVITY_CLI]]
│   ├── [[ANTIGRAVITY_IDE]]
│   ├── [[IDE_EXTENSIONS]]
│   └── [[ANTIGRAVITY_SDK]]
│
├── [[AGENTS]]
│   ├── [[PRIMARY_AGENT]]
│   ├── [[SUBAGENTS]]
│   ├── [[PARALLEL_AGENTS]]
│   ├── [[ASYNC_AGENTS]]
│   ├── [[LOCAL_AGENTS]]
│   ├── [[SPECIALIST_AGENTS]]
│   └── [[AGENT_SESSIONS]]
│
├── [[AGENT_MANAGEMENT]]
│   ├── [[SPAWN]]
│   ├── [[DELEGATE]]
│   ├── [[PARALLELIZE]]
│   ├── [[MONITOR]]
│   ├── [[PAUSE]]
│   ├── [[RESUME]]
│   ├── [[HANDOFF]]
│   ├── [[CANCEL]]
│   └── [[TERMINATE]]
│
├── [[WORKSPACE]]
│   ├── [[PROJECT]]
│   ├── [[MULTI_ROOT]]
│   ├── [[REPOSITORY]]
│   ├── [[FOLDER]]
│   ├── [[WORKTREE]]
│   ├── [[BRANCH]]
│   └── [[WORKSPACE_CONTEXT]]
│
├── [[TOOLS]]
│   ├── [[EDITOR]]
│   ├── [[TERMINAL]]
│   ├── [[BROWSER]]
│   ├── [[FILESYSTEM]]
│   ├── [[GIT]]
│   ├── [[SHELL]]
│   ├── [[WEB]]
│   └── [[EXTERNAL_TOOLS]]
│
├── [[KNOWLEDGE]]
│   ├── [[CODE_CONTEXT]]
│   ├── [[PROJECT_CONTEXT]]
│   ├── [[KNOWLEDGE_BASE]]
│   ├── [[DOCUMENTS]]
│   ├── [[REPOSITORIES]]
│   ├── [[MEMORY]]
│   └── [[AGENT_CONTEXT]]
│
├── [[MCP]]
│   ├── [[MCP_SERVERS]]
│   ├── [[MCP_TOOLS]]
│   ├── [[MCP_RESOURCES]]
│   └── [[MCP_CONNECTIONS]]
│
├── [[SKILLS]]
│   ├── [[SKILL_REGISTRY]]
│   ├── [[PROJECT_SKILLS]]
│   ├── [[DOMAIN_SKILLS]]
│   └── [[CUSTOM_SKILLS]]
│
├── [[RULES]]
│   ├── [[GLOBAL_RULES]]
│   ├── [[PROJECT_RULES]]
│   ├── [[WORKFLOW_RULES]]
│   ├── [[SECURITY_RULES]]
│   └── [[AGENT_RULES]]
│
├── [[EXECUTION]]
│   ├── [[TASK]]
│   ├── [[PLAN]]
│   ├── [[ACTION]]
│   ├── [[COMMAND]]
│   ├── [[TOOL_CALL]]
│   ├── [[ARTIFACT]]
│   └── [[RESULT]]
│
├── [[ARTIFACTS]]
│   ├── [[PLAN]]
│   ├── [[TASK_LIST]]
│   ├── [[CODE_DIFF]]
│   ├── [[DIAGRAM]]
│   ├── [[SCREENSHOT]]
│   ├── [[BROWSER_RECORDING]]
│   ├── [[REPORT]]
│   └── [[VERIFICATION_ARTIFACT]]
│
├── [[VERIFICATION]]
│   ├── [[TEST]]
│   ├── [[BUILD]]
│   ├── [[LINT]]
│   ├── [[TYPECHECK]]
│   ├── [[BROWSER_TEST]]
│   ├── [[DIFF_REVIEW]]
│   ├── [[ARTIFACT_REVIEW]]
│   └── [[EVIDENCE]]
│
├── [[AUTOMATION]]
│   ├── [[SCHEDULED_TASK]]
│   ├── [[CRON]]
│   ├── [[BACKGROUND_AGENT]]
│   ├── [[MAINTENANCE]]
│   └── [[MONITORING]]
│
├── [[CLI]]
│   ├── [[AGY]]
│   ├── [[COMMANDS]]
│   ├── [[PROMPTS]]
│   ├── [[SLASH_COMMANDS]]
│   ├── [[TUI]]
│   └── [[SSH_EXECUTION]]
│
├── [[SDK]]
│   ├── [[CUSTOM_AGENT]]
│   ├── [[CUSTOM_TOOL]]
│   ├── [[LIFECYCLE_HOOK]]
│   ├── [[SAFETY_POLICY]]
│   ├── [[INSPECT]]
│   ├── [[DECIDE]]
│   ├── [[TRANSFORM]]
│   └── [[SUBAGENT_SPAWNING]]
│
├── [[SECURITY]]
│   ├── [[PERMISSIONS]]
│   ├── [[APPROVAL_GATES]]
│   ├── [[SANDBOX]]
│   ├── [[CREDENTIAL_MASKING]]
│   ├── [[GIT_POLICIES]]
│   └── [[WORKSPACE_BOUNDARIES]]
│
└── [[ORCHESTRATION]]
    ├── [[TASK_ROUTING]]
    ├── [[AGENT_ROUTING]]
    ├── [[SKILL_ROUTING]]
    ├── [[TOOL_ROUTING]]
    ├── [[MCP_ROUTING]]
    ├── [[MODEL_ROUTING]]
    ├── [[PARALLEL_EXECUTION]]
    ├── [[DEPENDENCY_MANAGEMENT]]
    ├── [[HANDOFF]]
    ├── [[VERIFICATION]]
    └── [[RECOVERY]]

---

# 1. Antigravity's place in Company Brain

The cleanest model is:

```text
       [[COMPANY_BRAIN]]
               │
    [[DIRECTIVES / OBJECTIVES]]
               │
        [[EXECUTIVES]]
               │
       [[ORCHESTRATOR]]
               │
       ┌───────────┴───────────┐
       ↓                       ↓
[[ANTIGRAVITY]]         [[OTHER_AGENTS]]
       │
   ┌─────────┼─────────┐
   ↓         ↓         ↓
[[AGENT]] [[SKILLS]] [[TOOLS]]
   │         │         │
   └─────────┼─────────┘
             ↓
        [[EXECUTION]]
             │
   ┌───────────┼────────────┐
   ↓           ↓            ↓
[[EDITOR]] [[TERMINAL]] [[BROWSER]]
   │           │            │
   └───────────┼────────────┘
               ↓
         [[ARTIFACTS]]
               ↓
        [[VERIFICATION]]
               ↓
           [[RESULT]]
```

Antigravity itself therefore becomes an execution substrate for your broader Company Brain.

---

# 2. Antigravity's actual surfaces

[[ANTIGRAVITY_2]]
The standalone command center designed to launch, monitor, and orchestrate agents.

[[ANTIGRAVITY_CLI]]
The terminal-native surface (agy).

[[ANTIGRAVITY_IDE]]
The editor-centered surface (EDITOR + AGENT + TERMINAL + BROWSER + MCP + SKILLS + ARTIFACTS).

[[ANTIGRAVITY_SDK]]
The programmable layer (CUSTOM AGENT + CUSTOM TOOLS + LIFECYCLE HOOKS + SAFETY POLICIES + SUBAGENTS).

[[IDE_EXTENSIONS]]
Antigravity extensions into VS Code, Visual Studio, JetBrains, Zed, and Xcode.

---

# 3. Antigravity Agent Ontology

The agent itself should be represented as:

```text
[[ANTIGRAVITY_AGENT]]
├── [[IDENTITY]]
├── [[MISSION]]
├── [[OBJECTIVE]]
├── [[CONTEXT]]
├── [[KNOWLEDGE]]
├── [[MODEL]]
├── [[TOOLS]]
├── [[SKILLS]]
├── [[MCP]]
├── [[RULES]]
├── [[PERMISSIONS]]
├── [[PLAN]]
├── [[TASKS]]
├── [[SUBAGENTS]]
├── [[ACTIONS]]
├── [[ARTIFACTS]]
├── [[VERIFICATION]]
├── [[RESULTS]]
├── [[FEEDBACK]]
└── [[MEMORY]]
```

---

# 4. Parallel agent architecture

```text
        [[MASTER_AGENT]]
               │
    [[TASK_DECOMPOSITION]]
               │
   ┌───────────────┼────────────────┐
   ↓               ↓                ↓
[[RESEARCH]]   [[CODING]]      [[TESTING]]
   AGENT          AGENT            AGENT
   │               │                │
   ↓               ↓                ↓
 REPORT           CODE           RESULTS
   │               │                │
   └───────────────┼────────────────┘
                   ↓
         [[SYNTHESIS_AGENT]]
                   ↓
           [[VERIFICATION]]
```

---

# 5. Antigravity as your coding workforce

Canonical roles:
```text
[[ANTIGRAVITY_CEO_AGENT]]
[[ANTIGRAVITY_ARCHITECT_AGENT]]
[[ANTIGRAVITY_RESEARCH_AGENT]]
[[ANTIGRAVITY_REPOSITORY_AGENT]]
[[ANTIGRAVITY_CODING_AGENT]]
[[ANTIGRAVITY_DEBUG_AGENT]]
[[ANTIGRAVITY_TEST_AGENT]]
[[ANTIGRAVITY_UI_AGENT]]
[[ANTIGRAVITY_BROWSER_AGENT]]
[[ANTIGRAVITY_DATABASE_AGENT]]
[[ANTIGRAVITY_DEVOPS_AGENT]]
[[ANTIGRAVITY_SECURITY_AGENT]]
[[ANTIGRAVITY_DOCUMENTATION_AGENT]]
[[ANTIGRAVITY_AUDIT_AGENT]]
[[ANTIGRAVITY_VERIFICATION_AGENT]]
```

---

# 6. Antigravity + MCP

```text
    [[COMPANY_BRAIN]]
           ↓
    [[ANTIGRAVITY]]
           ↓
     [[MCP_CLIENT]]
           ↓
┌───────┼────────┬────────┬─────────┐
↓       ↓        ↓        ↓         ↓
GitHub  Neo4j   Qdrant  Docker  OpenObserve
```

---

# 7. Antigravity + CLI

```text
[[MAC_AIR]]
      ↓
[[TAILSCALE]]
      ↓
[[MAC_STUDIO]]
      ↓
[[SSH]]
      ↓
[[ANTIGRAVITY_CLI]]
      ↓
[[AGY]]
      ↓
[[COMPANY_BRAIN_REPOSITORY]]
```

---

# 8. Antigravity + OmniRoute

```text
[[COMPANY_BRAIN]]
      ↓
[[ANTIGRAVITY]]
      ↓
[[AGENT]]
      ↓
[[MODEL_REQUEST]]
      ↓
[[OMNIROUTE]]
      ↓
[[MODEL / PROVIDER]]
      ↓
[[RESPONSE]]
      ↓
[[ANTIGRAVITY]]
```

---

# 9. Antigravity + your filesystem

```text
[[ANTIGRAVITY_PROJECT]]
      ↓
[[WORKSPACE]]
      ↓
┌──────┼────────┬──────────┐
↓      ↓        ↓          ↓
Repo A Repo B  Docs     Config
```

---

# 10. Antigravity artifacts

```text
TASK
  ↓
PLAN
  ↓
EXECUTION
  ↓
ARTIFACT
  ↓
TEST
  ↓
EVIDENCE
  ↓
VERIFIED_RESULT
```

---

# 11. Antigravity self-healing

```text
[[ANTIGRAVITY_AGENT]]
      ↓
    ACTION
      ↓
    TEST
      ↓
   FAILURE?
   /      \
 NO       YES
 ↓          ↓
VERIFY   [[DIAGNOSE]]
            ↓
         [[RECOVERY]]
            ↓
         [[RETEST]]
            ↓
         [[VERIFICATION]]
            ↓
       ┌─────┴─────┐
       ↓           ↓
      PASS       FAIL
       ↓           ↓
    COMPLETE   ESCALATE
```

---

# 12. Antigravity directives (Constitutional layer)

```text
[[ANTIGRAVITY_DIRECTIVES]]
1.  [[REALITY_FIRST]]
2.  [[NO_FAKE_COMPLETION]]
3.  [[VERIFY_BEFORE_CLAIMING]]
4.  [[SOURCE_OF_TRUTH_FIRST]]
5.  [[READ_BEFORE_MODIFY]]
6.  [[UNDERSTAND_DEPENDENCIES]]
7.  [[PRESERVE_EXISTING_FUNCTIONALITY]]
8.  [[MINIMIZE_UNNECESSARY_CHANGE]]
9.  [[TEST_AFTER_CHANGE]]
10. [[DOCUMENT_MATERIAL_CHANGES]]
11. [[CREATE_EVIDENCE]]
12. [[ESCALATE_UNCERTAINTY]]
13. [[NEVER_HIDE_FAILURE]]
14. [[UPDATE_REGISTRIES]]
15. [[UPDATE_KNOWLEDGE_GRAPH]]
16. [[HANDOFF_COMPLETE_CONTEXT]]
```

---

# 13. The Final Company Brain Relationship

This is the canonical graph for the entire system:

```text
                       [[WHOAMI]]
                           ↓
                       [[MISSION]]
                           ↓
                      [[PRINCIPLES]]
                           ↓
                     [[DIRECTIVES]]
                           ↓
                    [[EXECUTIVES]]
                           ↓
                     [[OBJECTIVES]]
                           ↓
                    [[QUESTIONS]]
                           ↓
               [[THINKING_FRAMEWORKS]]
                           ↓
                   [[REQUIREMENTS]]
                           ↓
                  [[CAPABILITIES]]
                           ↓
                  [[ANTIGRAVITY]]
                           ↓
                  [[ORCHESTRATOR]]
                           ↓
        ┌─────────────────────────────────────┐
        │                                     │
        │             [[AGENTS]]              │
        │                 │                   │
        │                 ↓                   │
        │             [[SKILLS]]              │
        │                 │                   │
        │                 ↓                   │
        │             [[TOOLS]]               │
        │                 │                   │
        │                 ↓                   │
        │  [[MCP]] ←→ [[CLI]] ←→ [[API]]      │
        │                 │                   │
        │                 ↓                   │
        │             [[MODELS]]              │
        │                                     │
        └─────────────────────────────────────┘
                           ↓
                     [[EXECUTION]]
                           ↓
                     [[ARTIFACTS]]
                           ↓
                      [[TESTING]]
                           ↓
                   [[VERIFICATION]]
                           ↓
                      [[REALITY]]
                           ↓
                      [[OUTCOME]]
                           ↓
                   [[OBSERVABILITY]]
                           ↓
                   [[SELF_HEALING]]
                           ↓
                      [[LEARNING]]
                           ↓
                  [[KNOWLEDGE_GRAPH]]
                           ↓
                     [[REGISTRIES]]
                           ↓
                    [[NEW_CONTEXT]]
                           ↺
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
