---
type: execution-node
status: conceptual
prerequisites: []
requires: []
---

# `COMPANY_BRAIN_AGENTS_TOOLS_SKILLS_MASTER_ONTOLOGY.md`

```text id="3k8wq1"
[[COMPANY_BRAIN_EXECUTION]]

├── [[ORGANIZATION]]
│   ├── [[COMPANY_BRAIN]]
│   ├── [[EXECUTIVE_LAYER]]
│   ├── [[DEPARTMENT_LAYER]]
│   ├── [[SPECIALIST_LAYER]]
│   ├── [[EXECUTION_LAYER]]
│   ├── [[SUPPORT_LAYER]]
│   └── [[HUMAN_LAYER]]
│
├── [[AGENTS]]
│   ├── [[ORCHESTRATOR_AGENTS]]
│   ├── [[EXECUTIVE_AGENTS]]
│   ├── [[DEPARTMENT_AGENTS]]
│   ├── [[MANAGER_AGENTS]]
│   ├── [[SPECIALIST_AGENTS]]
│   ├── [[RESEARCH_AGENTS]]
│   ├── [[ANALYSIS_AGENTS]]
│   ├── [[CODING_AGENTS]]
│   ├── [[DESIGN_AGENTS]]
│   ├── [[DATA_AGENTS]]
│   ├── [[OPERATIONS_AGENTS]]
│   ├── [[SALES_AGENTS]]
│   ├── [[FINANCE_AGENTS]]
│   ├── [[LEGAL_AGENTS]]
│   ├── [[SECURITY_AGENTS]]
│   ├── [[QA_AGENTS]]
│   ├── [[AUDIT_AGENTS]]
│   ├── [[MONITORING_AGENTS]]
│   └── [[LEARNING_AGENTS]]
│
├── [[CAPABILITIES]]
│   ├── [[BUSINESS_CAPABILITIES]]
│   ├── [[TECHNICAL_CAPABILITIES]]
│   ├── [[COGNITIVE_CAPABILITIES]]
│   ├── [[OPERATIONAL_CAPABILITIES]]
│   ├── [[DATA_CAPABILITIES]]
│   ├── [[RESEARCH_CAPABILITIES]]
│   ├── [[CREATIVE_CAPABILITIES]]
│   ├── [[COMMUNICATION_CAPABILITIES]]
│   └── [[AUTOMATION_CAPABILITIES]]
│
├── [[SKILLS]]
│   ├── [[RESEARCH_SKILLS]]
│   ├── [[WRITING_SKILLS]]
│   ├── [[CODING_SKILLS]]
│   ├── [[DATA_SKILLS]]
│   ├── [[ANALYSIS_SKILLS]]
│   ├── [[DESIGN_SKILLS]]
│   ├── [[SALES_SKILLS]]
│   ├── [[FINANCE_SKILLS]]
│   ├── [[OPERATIONS_SKILLS]]
│   ├── [[ORCHESTRATION_SKILLS]]
│   ├── [[DELEGATION_SKILLS]]
│   ├── [[VERIFICATION_SKILLS]]
│   └── [[META_SKILLS]]
│
├── [[TOOLS]]
│   ├── [[LOCAL_TOOLS]]
│   ├── [[REMOTE_TOOLS]]
│   ├── [[SOFTWARE]]
│   ├── [[APIS]]
│   ├── [[DATABASES]]
│   ├── [[BROWSERS]]
│   ├── [[FILESYSTEM_TOOLS]]
│   ├── [[DEVELOPER_TOOLS]]
│   ├── [[DESIGN_TOOLS]]
│   └── [[BUSINESS_TOOLS]]
│
├── [[MCP]]
│   ├── [[MCP_SERVER]]
│   ├── [[MCP_CLIENT]]
│   ├── [[MCP_TOOL]]
│   ├── [[MCP_RESOURCE]]
│   ├── [[MCP_PROMPT]]
│   ├── [[LOCAL_MCP]]
│   ├── [[REMOTE_MCP]]
│   └── [[MCP_REGISTRY]]
│
├── [[CLI]]
│   ├── [[CLI]]
│   ├── [[CLI_COMMAND]]
│   ├── [[CLI_SUBCOMMAND]]
│   ├── [[CLI_ARGUMENT]]
│   ├── [[CLI_FLAG]]
│   ├── [[CLI_OUTPUT]]
│   ├── [[CLI_HARNESS]]
│   ├── [[CLI_INSTALLATION]]
│   ├── [[CLI_PREFLIGHT]]
│   └── [[CLI_VERIFICATION]]
│
├── [[MODELS]]
│   ├── [[LLM]]
│   ├── [[LOCAL_MODEL]]
│   ├── [[REMOTE_MODEL]]
│   ├── [[EMBEDDING_MODEL]]
│   ├── [[VISION_MODEL]]
│   └── [[MODEL_ROUTER]]
│
├── [[CONTEXT]]
│   ├── [[KNOWLEDGE]]
│   ├── [[MEMORY]]
│   ├── [[DOCUMENTS]]
│   ├── [[REPOSITORIES]]
│   ├── [[DATABASES]]
│   ├── [[GRAPH]]
│   └── [[RUNTIME_CONTEXT]]
│
├── [[WORK]]
│   ├── [[OBJECTIVE]]
│   ├── [[PROJECT]]
│   ├── [[TASK]]
│   ├── [[SUBTASK]]
│   ├── [[ACTION]]
│   └── [[DELIVERABLE]]
│
├── [[ORCHESTRATION]]
│   ├── [[ROUTING]]
│   ├── [[PLANNING]]
│   ├── [[DECOMPOSITION]]
│   ├── [[SCHEDULING]]
│   ├── [[PRIORITIZATION]]
│   ├── [[DELEGATION]]
│   ├── [[PARALLELIZATION]]
│   ├── [[SEQUENCING]]
│   ├── [[HANDOFF]]
│   ├── [[ROTATION]]
│   ├── [[ESCALATION]]
│   └── [[COORDINATION]]
│
├── [[EXECUTION]]
│   ├── [[CLAIM]]
│   ├── [[START]]
│   ├── [[EXECUTE]]
│   ├── [[CHECKPOINT]]
│   ├── [[RECOVER]]
│   ├── [[HANDOFF]]
│   ├── [[COMPLETE]]
│   └── [[VERIFY]]
│
├── [[GOVERNANCE]]
│   ├── [[AUTHORITY]]
│   ├── [[PERMISSIONS]]
│   ├── [[POLICIES]]
│   ├── [[APPROVALS]]
│   ├── [[GUARDRAILS]]
│   ├── [[AUDIT]]
│   └── [[HUMAN_ESCALATION]]
│
└── [[LEARNING]]
    ├── [[FEEDBACK]]
    ├── [[EVALUATION]]
    ├── [[TELEMETRY]]
    ├── [[LESSONS]]
    ├── [[ERROR_PATTERNS]]
    ├── [[CAPABILITY_GAPS]]
    ├── [[SKILL_IMPROVEMENTS]]
    └── [[SYSTEM_IMPROVEMENT]]
```

# 1. The fundamental execution equation

This should become one of the core laws of the Company Brain:

```text
[[OBJECTIVE]]
      ↓
[[REQUIREMENT]]
      ↓
[[CAPABILITY]]
      ↓
[[AGENT]]
      ↓
[[SKILL]]
      ↓
[[TOOL]]
      ↓
[MCP / API / CLI]
      ↓
[[WORKFLOW]]
      ↓
[[ACTION]]
      ↓
[[OUTPUT]]
      ↓
[[VERIFICATION]]
      ↓
[[OUTCOME]]
      ↓
[[FEEDBACK]]
```

Or more compactly:

```text
GOAL
→ CAPABILITY
→ AGENT
→ SKILL
→ TOOL
→ EXECUTION
→ VERIFICATION
→ OUTCOME
→ LEARNING
```

This is the backbone of the entire agent registry.

---

# 2. The agent hierarchy

I would organize agents into **organizational roles**, not merely technical functions.

```text
[[COMPANY_BRAIN]]
│
├── [[ORCHESTRATOR]]
│
├── [[CEO_AGENT]]
│
├── [[CHIEF_OF_STAFF_AGENT]]
│
├── [[DEPARTMENT_AGENTS]]
│   ├── [[FINANCE_AGENT]]
│   ├── [[SALES_AGENT]]
│   ├── [[MARKETING_AGENT]]
│   ├── [[OPERATIONS_AGENT]]
│   ├── [[TECHNOLOGY_AGENT]]
│   ├── [[PRODUCT_AGENT]]
│   ├── [[DATA_AGENT]]
│   ├── [[LEGAL_AGENT]]
│   ├── [[SECURITY_AGENT]]
│   ├── [[HR_AGENT]]
│   └── [[STRATEGY_AGENT]]
│
├── [[SPECIALIST_AGENTS]]
│
├── [[EXECUTION_AGENTS]]
│
├── [[QA_AGENTS]]
│
└── [[AUDIT_AGENTS]]
```

But then add **cross-cutting agents**.

### Intelligence

```text
[[RESEARCH_AGENT]]
[[WEB_RESEARCH_AGENT]]
[[REPOSITORY_INTELLIGENCE_AGENT]]
[[KNOWLEDGE_AGENT]]
[[QUESTION_AGENT]]
[[THINKING_AGENT]]
[[SYNTHESIS_AGENT]]
[[ENTITY_RESOLUTION_AGENT]]
```

### Engineering

```text
[[ARCHITECTURE_AGENT]]
[[CODING_AGENT]]
[[DEBUGGING_AGENT]]
[[TESTING_AGENT]]
[[DEPLOYMENT_AGENT]]
[[DEVOPS_AGENT]]
[[INFRASTRUCTURE_AGENT]]
[[DATABASE_AGENT]]
```

### Company operations

```text
[[CRM_AGENT]]
[[SALES_AGENT]]
[[CUSTOMER_AGENT]]
[[PIPELINE_AGENT]]
[[FINANCE_AGENT]]
[[ACCOUNTING_AGENT]]
[[PROCUREMENT_AGENT]]
[[OPERATIONS_AGENT]]
[[PROJECT_AGENT]]
```

### Control

```text
[[SECURITY_AGENT]]
[[COMPLIANCE_AGENT]]
[[POLICY_AGENT]]
[[PERMISSIONS_AGENT]]
[[AUDIT_AGENT]]
[[RISK_AGENT]]
[[VERIFICATION_AGENT]]
```

---

# 3. The most important agent: `[[ORCHESTRATOR]]`

The orchestrator shouldn't perform every task.

Its primary job is:

> **Determine what needs to happen and construct the execution system that makes it happen.**

```text
[[ORCHESTRATOR]]

├── [[UNDERSTAND_OBJECTIVE]]
├── [[LOAD_CONTEXT]]
├── [[CLASSIFY_WORK]]
├── [[DECOMPOSE_WORK]]
├── [[IDENTIFY_CAPABILITIES]]
├── [[SELECT_AGENTS]]
├── [[SELECT_SKILLS]]
├── [[SELECT_TOOLS]]
├── [[SELECT_MCP]]
├── [[SELECT_CLI]]
├── [[SELECT_MODEL]]
├── [[CHECK_PERMISSIONS]]
├── [[BUILD_PLAN]]
├── [[DELEGATE]]
├── [[SCHEDULE]]
├── [[MONITOR]]
├── [[HANDLE_FAILURE]]
├── [[REQUEST_HANDOFF]]
├── [[ESCALATE]]
├── [[VERIFY]]
├── [[CLOSE]]
└── [[LEARN]]
```

---

# 4. Capability registry

This should sit **above agents**.

Why?

Because you don't want:

> "Which agent should I use?"

You want:

> **"What capability is actually required?"**

Then discover the implementation.

```text
[[CAPABILITY]]
      │
      ├── [[IMPLEMENTED_BY]] → [[AGENT]]
      ├── [[IMPLEMENTED_BY]] → [[SKILL]]
      ├── [[IMPLEMENTED_BY]] → [[TOOL]]
      ├── [[IMPLEMENTED_BY]] → [[MCP]]
      ├── [[IMPLEMENTED_BY]] → [[CLI]]
      └── [[IMPLEMENTED_BY]] → [[SOFTWARE]]
```

Example:

```text
[[REPOSITORY_ANALYSIS]]
       │
       ├── [[REPOSITORY_INTELLIGENCE_AGENT]]
       ├── [[GITHUB]]
       ├── [[GIT]]
       ├── [[SERENA]]
       ├── [[SOURCEGRAPH]]
       ├── [[GITNEXUS]]
       └── [[REPOSITORY_ANALYSIS_SKILL]]
```

This prevents tool-first architecture.

---

# 5. Skills

A skill is **repeatable procedural knowledge**.

```text
[[SKILL]]

├── [[SKILL_ID]]
├── [[NAME]]
├── [[DESCRIPTION]]
├── [[CAPABILITY]]
├── [[PREREQUISITES]]
├── [[INPUTS]]
├── [[OUTPUTS]]
├── [[TOOLS_REQUIRED]]
├── [[MCP_REQUIRED]]
├── [[CLI_REQUIRED]]
├── [[MODEL_REQUIREMENTS]]
├── [[PERMISSIONS]]
├── [[PROCEDURE]]
├── [[VALIDATION]]
├── [[FAILURE_MODES]]
├── [[VERSION]]
└── [[EVALUATION]]
```

Examples:

```text
[[GITHUB_REPOSITORY_AUDIT]]
[[CODEBASE_SEARCH]]
[[DOCUMENT_INGESTION]]
[[ENTITY_RESOLUTION]]
[[KNOWLEDGE_GRAPH_UPDATE]]
[[WEB_RESEARCH]]
[[COMPETITIVE_RESEARCH]]
[[DATABASE_MIGRATION]]
[[API_TESTING]]
[[DEPLOYMENT]]
[[SALES_PROSPECTING]]
[[TASK_DECOMPOSITION]]
[[AGENT_DELEGATION]]
[[HANDOFF_GENERATION]]
[[OUTPUT_VERIFICATION]]
```

---

# 6. Tools

Tools are the **action interfaces**.

```text
[[TOOL]]

├── [[TOOL_ID]]
├── [[NAME]]
├── [[TYPE]]
├── [[PROVIDER]]
├── [[CAPABILITIES]]
├── [[INPUT_SCHEMA]]
├── [[OUTPUT_SCHEMA]]
├── [[AUTH]]
├── [[PERMISSIONS]]
├── [[NETWORK]]
├── [[LATENCY]]
├── [[COST]]
├── [[LIMITS]]
├── [[FAILURE_MODES]]
├── [[HEALTH]]
└── [[VERIFICATION]]
```

Types:

```text
[[WEB_TOOL]]
[[FILE_TOOL]]
[[DATABASE_TOOL]]
[[GIT_TOOL]]
[[GITHUB_TOOL]]
[[SHELL_TOOL]]
[[BROWSER_TOOL]]
[[API_TOOL]]
[[COMMUNICATION_TOOL]]
[[DESIGN_TOOL]]
[[ANALYTICS_TOOL]]
[[FINANCE_TOOL]]
[[CRM_TOOL]]
[[DEPLOYMENT_TOOL]]
```

---

# 7. MCP layer

MCP becomes the **tool/context interoperability layer**.

```text
[[MCP]]

├── [[MCP_SERVER]]
│
├── [[MCP_CLIENT]]
│
├── [[MCP_TOOL]]
│
├── [[MCP_RESOURCE]]
│
├── [[MCP_PROMPT]]
│
├── [[LOCAL_MCP]]
│
├── [[REMOTE_MCP]]
│
├── [[MCP_AUTH]]
│
├── [[MCP_PERMISSIONS]]
│
├── [[MCP_HEALTH]]
│
└── [[MCP_REGISTRY]]
```

Relationship:

```text
AGENT
 ↓
SKILL
 ↓
MCP
 ↓
MCP_TOOL
 ↓
REAL_SYSTEM
```

For example:

```text
[[RESEARCH_AGENT]]
       ↓
[[WEB_RESEARCH_SKILL]]
       ↓
[[MCP]]
       ↓
[[SEARCH_TOOL]]
       ↓
[[WEB]]
```

---

# 8. CLI layer

CLIs are different from MCP.

A CLI is an **executable interface to a system**.

```text
[[CLI]]

├── [[DISCOVER]]
├── [[INSTALL]]
├── [[PREFLIGHT]]
├── [[AUTHENTICATE]]
├── [[EXECUTE]]
├── [[CAPTURE_OUTPUT]]
├── [[PARSE_OUTPUT]]
├── [[VALIDATE]]
├── [[LOG]]
└── [[AUDIT]]
```

Your CLI ecosystem should therefore contain:

```text
[[CLI_REGISTRY]]
[[CLI_HUB]]
[[CLI_DISCOVERY]]
[[CLI_INSTALLATION]]
[[CLI_PREFLIGHT]]
[[CLI_EXECUTION]]
[[CLI_OUTPUT]]
[[CLI_HARNESS]]
[[CLI_VERIFICATION]]
```

And the relationship:

```text
[[CAPABILITY]]
       ↓
[[CLI]]
       ↓
[[COMMAND]]
       ↓
[[SOFTWARE]]
       ↓
[[ARTIFACT]]
       ↓
[[VALIDATION]]
```

This fits your earlier **CLI-Hub / CLI-Anything** architecture.

---

# 9. Model layer

Don't confuse the **agent** with the **model**.

```text
[[AGENT]]
      ↓
[[USES]]
      ↓
[[MODEL]]
```

An agent might use:

```text
[[CLAUDE]]
[[CODEX]]
[[LOCAL_MODEL]]
[[VISION_MODEL]]
[[EMBEDDING_MODEL]]
```

And:

```text
[[OMNIROUTE]]
```

can sit between agent/application and model/provider infrastructure:

```text
AGENT
 ↓
MODEL_REQUEST
 ↓
[[OMNIROUTE]]
 ↓
PROVIDER
 ↓
MODEL
 ↓
RESPONSE
```

---

# 10. Context and memory

Agents need more than tools.

```text
[[AGENT]]
   │
   ├── [[CONTEXT]]
   ├── [[MEMORY]]
   ├── [[KNOWLEDGE]]
   ├── [[DOCUMENTS]]
   ├── [[KNOWLEDGE_GRAPH]]
   ├── [[REPOSITORIES]]
   └── [[CURRENT_STATE]]
```

Your existing stack maps naturally:

```text
[[OBSIDIAN]]
      ↓
Human knowledge/context

[[NEO4J]]
      ↓
Relationships

[[QDRANT]]
      ↓
Semantic retrieval

[[GITHUB]]
      ↓
Code/repository reality

[[POSTGRES]]
      ↓
Operational state

[[OPENOBSERVE]]
      ↓
Observability
```

---

# 11. Delegation ontology

This deserves its own layer.

```text
[[DELEGATION]]

├── [[DELEGATE]]
├── [[ASSIGN]]
├── [[CLAIM]]
├── [[ACCEPT]]
├── [[REJECT]]
├── [[REASSIGN]]
├── [[DECOMPOSE]]
├── [[PARALLELIZE]]
├── [[SEQUENCE]]
├── [[HANDOFF]]
├── [[ROTATE]]
├── [[ESCALATE]]
└── [[RECALL]]
```

The decision:

```text
[[WORK]]
 ↓
[WHO CAN DO THIS?]
 ↓
[CAPABILITY MATCH]
 ↓
[AGENT MATCH]
 ↓
[SKILL MATCH]
 ↓
[TOOL ACCESS]
 ↓
[[PERMISSION]]
 ↓
[[CAPACITY]]
 ↓
[[ASSIGNMENT]]
```

---

# 12. Agent matching

Create:

```text
[[AGENT_MATCHING_ENGINE]]
```

It evaluates:

```text
[[CAPABILITY_MATCH]]
[[SKILL_MATCH]]
[[TOOL_ACCESS]]
[[MCP_ACCESS]]
[[CLI_ACCESS]]
[[MODEL_CAPABILITY]]
[[CONTEXT_ACCESS]]
[[PERMISSION]]
[[AVAILABILITY]]
[[CAPACITY]]
[[COST]]
[[LATENCY]]
[[RELIABILITY]]
[[PRIOR_PERFORMANCE]]
```

Then:

```text
WORK
 ↓
CANDIDATE AGENTS
 ↓
CAPABILITY MATCH
 ↓
RESOURCE MATCH
 ↓
AUTHORITY CHECK
 ↓
ASSIGNMENT
```

---

# 13. Organization becomes a graph

Instead of:

```text
CEO
 ↓
Department
 ↓
Employee
```

Company Brain becomes:

```text
                    [[COMPANY_BRAIN]]
                           │
                      [[ORCHESTRATOR]]
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        [[AGENT]]      [[AGENT]]      [[AGENT]]
             │             │             │
        [[SKILLS]]     [[SKILLS]]     [[SKILLS]]
             │             │             │
        [[TOOLS]]      [[MCP]]        [[CLI]]
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                       [[WORKFLOW]]
                           ↓
                         [[TASK]]
                           ↓
                        [[ACTION]]
                           ↓
                       [[OUTCOME]]
```

---

# 14. The master execution loop

This should probably become the **canonical Company Brain agent loop**:

```text
[[OBJECTIVE]]
      ↓
[[QUESTION]]
      ↓
[[CONTEXT]]
      ↓
[[DECOMPOSITION]]
      ↓
[[REQUIREMENTS]]
      ↓
[[CAPABILITY_DISCOVERY]]
      ↓
[[AGENT_SELECTION]]
      ↓
[[SKILL_SELECTION]]
      ↓
[[TOOL_SELECTION]]
      ↓
[[MCP_SELECTION]]
      ↓
[[CLI_SELECTION]]
      ↓
[[MODEL_SELECTION]]
      ↓
[[PERMISSION_CHECK]]
      ↓
[[PLAN]]
      ↓
[[DELEGATION]]
      ↓
[[EXECUTION]]
      ↓
[[OBSERVATION]]
      ↓
[[VERIFICATION]]
      ↓
[[RESULT]]
      ↓
[[OUTCOME]]
      ↓
[[AUDIT]]
      ↓
[[LEARNING]]
      ↓
[[REGISTRY_UPDATE]]
      ↓
[[KNOWLEDGE_GRAPH_UPDATE]]
      ↺
```

---

# 15. The self-organizing layer

This is where your system moves beyond a static "agent list."

Create:

```text
[[AGENT_ECOSYSTEM]]
```

It continuously discovers:

```text
NEW REPOSITORY
      ↓
NEW CAPABILITY
      ↓
NEW SKILL
      ↓
NEW TOOL
      ↓
NEW MCP
      ↓
NEW CLI
      ↓
NEW AGENT POSSIBILITY
      ↓
NEW WORKFLOW
      ↓
NEW BUSINESS CAPABILITY
```

Your repository intelligence system can therefore feed:

```text
[[REPOSITORY_INTELLIGENCE]]
        ↓
[[CAPABILITY_REGISTRY]]
        ↓
[[SKILL_REGISTRY]]
        ↓
[[TOOL_REGISTRY]]
        ↓
[[MCP_REGISTRY]]
        ↓
[[CLI_REGISTRY]]
        ↓
[[AGENT_REGISTRY]]
        ↓
[[WORKFLOW_REGISTRY]]
```

That is the **compounding loop** you've been describing.

---

# 16. Registries you should have

I'd make these first-class:

```text
[[AGENT_REGISTRY]]
[[CAPABILITY_REGISTRY]]
[[SKILL_REGISTRY]]
[[TOOL_REGISTRY]]
[[MCP_REGISTRY]]
[[CLI_REGISTRY]]
[[API_REGISTRY]]
[[MODEL_REGISTRY]]
[[PROVIDER_REGISTRY]]
[[WORKFLOW_REGISTRY]]
[[LOOP_REGISTRY]]
[[TASK_REGISTRY]]
[[AGENT_PERMISSION_REGISTRY]]
[[AGENT_PERFORMANCE_REGISTRY]]
[[AGENT_EVALUATION_REGISTRY]]
[[DELEGATION_REGISTRY]]
[[HANDOFF_REGISTRY]]
[[ORCHESTRATION_REGISTRY]]
[[INTEGRATION_REGISTRY]]
[[DEPENDENCY_REGISTRY]]
[[ERROR_REGISTRY]]
[[EVIDENCE_REGISTRY]]
[[ARTIFACT_REGISTRY]]
```

---

# 17. The most important graph relationships

Your Neo4j ontology can use relationships such as:

```text
[[AGENT]]
    [[HAS_CAPABILITY]]
    [[HAS_SKILL]]
    [[USES_TOOL]]
    [[USES_MCP]]
    [[USES_CLI]]
    [[USES_MODEL]]
    [[READS]]
    [[WRITES]]
    [[KNOWS]]
    [[EXECUTES]]
    [[DELEGATES_TO]]
    [[REPORTS_TO]]
    [[SUPERVISES]]
    [[HANDOFFS_TO]]
    [[ESCALATES_TO]]
    [[REQUIRES]]
    [[DEPENDS_ON]]
    [[PRODUCES]]
    [[VERIFIED_BY]]
    [[EVALUATED_BY]]
```

And:

```text
[[CAPABILITY]]
    [[IMPLEMENTED_BY]] → [[AGENT]]
    [[ENABLED_BY]] → [[SKILL]]
    [[EXECUTED_WITH]] → [[TOOL]]
    [[CONNECTED_BY]] → [[MCP]]
    [[EXPOSED_BY]] → [[CLI]]
    [[POWERED_BY]] → [[MODEL]]
```

---

# 18. The complete Company Brain stack

This gives you a very clean ontology:

```text
                         [[MISSION]]
                             ↓
                         [[OBJECTIVE]]
                             ↓
                         [[QUESTION]]
                             ↓
                        [[REQUIREMENT]]
                             ↓
                        [[CAPABILITY]]
                             ↓
                    [[CAPABILITY_REGISTRY]]
                             ↓
                         [[AGENT]]
                             ↓
                          [[SKILL]]
                             ↓
                  ┌──────────┼──────────┐
                  ↓          ↓          ↓
                [[MCP]]    [[CLI]]    [[API]]
                  │          │          │
                  └──────────┼──────────┘
                             ↓
                          [[TOOL]]
                             ↓
                          [[MODEL]]
                             ↓
                        [[EXECUTION]]
                             ↓
                         [[RESULT]]
                             ↓
                       [[VERIFICATION]]
                             ↓
                         [[OUTCOME]]
                             ↓
                         [[FEEDBACK]]
                             ↓
                         [[LEARNING]]
                             ↓
                  [[CAPABILITY_REGISTRY]]
                             ↺
```

And surrounding the whole thing:

```text
                 [[KNOWLEDGE]]
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   [[OBSIDIAN]]   [[NEO4J]]     [[QDRANT]]
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                  [[CONTEXT]]
                      ↓
                   [[AGENT]]
```

while infrastructure supports it:

```text
[[MAC_STUDIO]]
      ↓
[[DOCKER]]
      ↓
[[SERVICES]]
      ↓
[[OMNIROUTE]]
      ↓
[[MODELS]]
```

and:

```text
[[MAC_AIR]]
      ↓
[[TAILSCALE]]
      ↓
[[MAC_STUDIO]]
```

## The key architectural rule

I'd make this explicit:

```text
[DO NOT START WITH AGENTS]

START WITH:

[[OBJECTIVE]]
      ↓
[[REQUIREMENT]]
      ↓
[[CAPABILITY]]
      ↓
[AVAILABLE IMPLEMENTATIONS]
      ↓
[AGENT + SKILL + TOOL + MCP + CLI]
```

That means your Company Brain doesn't become **"318 agents trying to find work."**

It becomes a **capability operating system** that dynamically assembles the right execution team for the work.

And that fits the architecture you've already been building:

**`[[QUESTION]] → [[THINKING]] → [[CAPABILITY]] → [[AGENT]] → [[SKILL]] → [[TOOL]] → [[MCP]] / [[CLI]] → [[WORKFLOW]] → [[ACTION]] → [[VERIFICATION]] → [[OUTCOME]] → [[LEARNING]]`**


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
