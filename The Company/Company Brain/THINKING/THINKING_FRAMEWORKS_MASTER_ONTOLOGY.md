---
type: master-ontology
status: conceptual
prerequisites: []
requires: []
---

# `THINKING_FRAMEWORKS_MASTER_ONTOLOGY.md`

```text
[[THINKING_FRAMEWORKS]]

├── [[SYSTEMS_THINKING]]
│   ├── [[SYSTEM]]
│   ├── [[COMPONENTS]]
│   ├── [[BOUNDARIES]]
│   ├── [[RELATIONSHIPS]]
│   ├── [[INTERACTIONS]]
│   ├── [[FEEDBACK]]
│   ├── [[EMERGENCE]]
│   └── [[SYSTEM_STATE]]
│
├── [[FIRST_PRINCIPLES]]
│   ├── [[ASSUMPTIONS]]
│   ├── [[FACTS]]
│   ├── [[CONSTRAINTS]]
│   ├── [[FUNDAMENTALS]]
│   ├── [[DERIVATION]]
│   └── [[RECONSTRUCTION]]
│
├── [[SECOND_ORDER_THINKING]]
│   ├── [[DIRECT_EFFECT]]
│   ├── [[SECOND_ORDER_EFFECT]]
│   ├── [[THIRD_ORDER_EFFECT]]
│   ├── [[CONSEQUENCE]]
│   ├── [[REACTION]]
│   └── [[LONG_TERM_EFFECT]]
│
├── [[PROBABILISTIC_THINKING]]
│   ├── [[HYPOTHESIS]]
│   ├── [[PRIOR]]
│   ├── [[EVIDENCE]]
│   ├── [[LIKELIHOOD]]
│   ├── [[POSTERIOR]]
│   ├── [[UNCERTAINTY]]
│   └── [[CONFIDENCE]]
│
├── [[INVERSION]]
│   ├── [[DESIRED_OUTCOME]]
│   ├── [[FAILURE_MODE]]
│   ├── [[OPPOSITE]]
│   ├── [[ANTI_GOAL]]
│   ├── [[PREVENTION]]
│   └── [[REVERSAL]]
│
├── [[SCENARIO_THINKING]]
│   ├── [[BASELINE]]
│   ├── [[BEST_CASE]]
│   ├── [[WORST_CASE]]
│   ├── [[LIKELY_CASE]]
│   ├── [[SCENARIO]]
│   ├── [[TRIGGER]]
│   └── [[RESPONSE]]
│
├── [[CONSTRAINT_THINKING]]
│   ├── [[OBJECTIVE]]
│   ├── [[CONSTRAINT]]
│   ├── [[BOTTLENECK]]
│   ├── [[CAPACITY]]
│   ├── [[THROUGHPUT]]
│   └── [[SYSTEM_LIMIT]]
│
├── [[OPPORTUNITY_COST_THINKING]]
│   ├── [[CHOICE]]
│   ├── [[ALTERNATIVE]]
│   ├── [[TRADEOFF]]
│   ├── [[RESOURCE]]
│   ├── [[FOREGONE_OPTION]]
│   └── [[VALUE_OF_ALTERNATIVE]]
│
├── [[OODA_LOOP]]
│   ├── [[OBSERVE]]
│   ├── [[ORIENT]]
│   ├── [[DECIDE]]
│   ├── [[ACT]]
│   ├── [[FEEDBACK]]
│   └── [[LOOP_SPEED]]
│
├── [[MECHANISM_DESIGN]]
│   ├── [[ACTORS]]
│   ├── [[INCENTIVES]]
│   ├── [[RULES]]
│   ├── [[INFORMATION]]
│   ├── [[STRATEGY]]
│   ├── [[BEHAVIOR]]
│   └── [[OUTCOME]]
│
├── [[ROOT_CAUSE_THINKING]]
│   ├── [[SYMPTOM]]
│   ├── [[EVENT]]
│   ├── [[CAUSE]]
│   ├── [[CONTRIBUTING_FACTOR]]
│   ├── [[ROOT_CAUSE]]
│   ├── [[5_WHYS]]
│   └── [[CORRECTIVE_ACTION]]
│
└── [[DECOMPOSITION_THINKING]]
    ├── [[WHOLE]]
    ├── [[SUBSYSTEM]]
    ├── [[COMPONENT]]
    ├── [[SUBPROBLEM]]
    ├── [[DEPENDENCY]]
    ├── [[SEQUENCE]]
    └── [[RECOMPOSITION]]
```

These 12 form a **thinking toolkit**, rather than a rigid hierarchy.

---

# 1. `[[SYSTEMS_THINKING]]`

Ask:

> **What system am I actually looking at, and how do its parts interact?**

```text
[[WHOLE]]
   ↓
[[SYSTEM]]
   ├── [[COMPONENTS]]
   ├── [[RELATIONSHIPS]]
   ├── [[INPUTS]]
   ├── [[PROCESSES]]
   ├── [[OUTPUTS]]
   ├── [[FEEDBACK]]
   └── [[ENVIRONMENT]]
```

For Company Brain:

```text
[[USER]]
 ↓
[[QUESTION]]
 ↓
[[CLAUDE]]
 ↓
[[MCP]]
 ↓
[[OMNIROUTE]]
 ↓
[[MODEL]]
 ↓
[[TOOL]]
 ↓
[[ACTION]]
 ↓
[[OUTCOME]]
```

Systems thinking asks what happens **across the whole chain**, not merely at one node.

---

# 2. `[[FIRST_PRINCIPLES]]`

Ask:

> **What is actually true underneath the assumptions?**

```text
[[PROBLEM]]
 ↓
[[ASSUMPTIONS]]
 ↓
[[FACTS]]
 ↓
[[CONSTRAINTS]]
 ↓
[[FUNDAMENTALS]]
 ↓
[[DERIVATION]]
 ↓
[[SOLUTION]]
```

For example:

```text
"We need another AI agent."
          ↓
What capability is missing?
          ↓
What task must be performed?
          ↓
What inputs are required?
          ↓
What outputs are required?
          ↓
Can an existing capability already do it?
```

This prevents **architecture-by-assumption**.

---

# 3. `[[SECOND_ORDER_THINKING]]`

Ask:

> **What happens after the immediate result?**

```text
[[ACTION]]
   ↓
[DIRECT EFFECT]
   ↓
[SECOND_ORDER EFFECT]
   ↓
[THIRD_ORDER EFFECT]
   ↓
[LONG_TERM EFFECT]
```

Example:

```text
Automate task
    ↓
Task gets faster
    ↓
More tasks can be processed
    ↓
Capacity changes
    ↓
Work allocation changes
    ↓
Infrastructure requirements change
```

This connects directly to:

```text
[[FEEDBACK_LOOPS]]
[[SYSTEMS_THINKING]]
[[SCENARIO_THINKING]]
```

---

# 4. `[[PROBABILISTIC_THINKING]]`

Ask:

> **Given the evidence, what hypotheses remain plausible and how uncertain are they?**

```text
[[HYPOTHESIS]]
      ↓
[[PRIOR]]
      ↓
[[EVIDENCE]]
      ↓
[[LIKELIHOOD]]
      ↓
[UPDATED BELIEF]
      ↓
[[UNCERTAINTY]]
```

Important Company Brain distinction:

```text
[[CONFIDENCE]]
≠
[[TRUTH]]

[[MODEL_BELIEF]]
≠
[[VERIFIED_REALITY]]
```

Therefore:

```text
[[CLAUDE_CLAIM]]
      ↓
[[EVIDENCE]]
      ↓
[[VERIFICATION]]
      ↓
[[REALITY]]
```

---

# 5. `[[INVERSION]]`

Instead of asking only:

> How do we succeed?

ask:

> **How could this fail?**

```text
[DESIRED OUTCOME]
       ↓
[[INVERT]]
       ↓
[FAILURE CONDITIONS]
       ↓
[FAILURE MODES]
       ↓
[[PREVENTION]]
       ↓
[[RESILIENCE]]
```

For infrastructure:

```text
"How do we keep Company Brain available?"

invert:

"What would make Company Brain unavailable?"
```

Potential categories:

```text
[[NETWORK_FAILURE]]
[[STORAGE_FAILURE]]
[[AUTH_FAILURE]]
[[PROVIDER_FAILURE]]
[[DATABASE_FAILURE]]
[[CONFIGURATION_DRIFT]]
[[DATA_CORRUPTION]]
[[DEPENDENCY_FAILURE]]
```

---

# 6. `[[SCENARIO_THINKING]]`

Ask:

> **What different futures should the system be prepared for?**

```text
                    [[CURRENT_STATE]]
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
     [BEST CASE]      [BASE CASE]     [WORST CASE]
          │               │               │
          ↓               ↓               ↓
      [[RESPONSE]]       [[RESPONSE]]       [[RESPONSE]]
```

Extend this into:

```text
[[SCENARIO]]
[[TRIGGER]]
[[ASSUMPTION]]
[[CONDITION]]
[[RESPONSE]]
[[CONTINGENCY]]
[[RECOVERY]]
```

This becomes particularly useful for autonomous systems.

---

# 7. `[[CONSTRAINT_THINKING]]`

Ask:

> **What is actually limiting throughput?**

```text
[[GOAL]]
  ↓
[[SYSTEM]]
  ↓
[[CONSTRAINTS]]
  ↓
[[BOTTLENECK]]
  ↓
[[EXPLOIT]]
  ↓
[[SUBORDINATE]]
  ↓
[[ELEVATE]]
  ↓
[[REPEAT]]
```

For Company Brain:

```text
Revenue objective
      ↓
Customer acquisition
      ↓
Sales capacity
      ↓
Lead volume
      ↓
Qualified leads
      ↓
Calls
      ↓
Appointments
      ↓
Closing
```

The constraint might be somewhere completely different from where the team initially looks.

---

# 8. `[[OPPORTUNITY_COST_THINKING]]`

Every resource allocation implies:

```text
[CHOICE A]
   +
[NOT CHOOSING B]
```

Therefore:

```text
[[RESOURCE]]
    ↓
[OPTION A]
    ↓
[FOREGO B]
    ↓
[OPPORTUNITY COST]
```

Resources include:

```text
[[TIME]]
[[MONEY]]
[[COMPUTE]]
[[ATTENTION]]
[[ENGINEERING]]
[[CAPITAL]]
[[STORAGE]]
[[AGENT_CAPACITY]]
```

This is important because an enormous repository inventory creates an enormous **selection problem**.

---

# 9. `[[OODA_LOOP]]`

The operational cognition loop:

```text
[[OBSERVE]]
    ↓
[[ORIENT]]
    ↓
[[DECIDE]]
    ↓
[[ACT]]
    ↓
[[OBSERVE]]
    ↺
```

Map it directly to Company Brain:

```text
[[OBSERVABILITY]]
       ↓
[[CONTEXT]]
       ↓
[[DECISION_ENGINE]]
       ↓
[[ACTION_ENGINE]]
       ↓
[[OUTCOME]]
       ↓
[[OBSERVABILITY]]
```

This is one of the cleanest bridges between **thinking and execution**.

---

# 10. `[[MECHANISM_DESIGN]]`

Ask:

> **If I construct the rules and incentives differently, how will behavior change?**

```text
[[ACTORS]]
   ↓
[[INFORMATION]]
   ↓
[[INCENTIVES]]
   ↓
[[RULES]]
   ↓
[[AVAILABLE_STRATEGIES]]
   ↓
[[BEHAVIOR]]
   ↓
[[OUTCOME]]
```

For an agent organization:

```text
[[AGENT]]
 ↓
[[AUTHORITY]]
 ↓
[[INCENTIVE]]
 ↓
[[REWARD]]
 ↓
[[PERMISSION]]
 ↓
[[BEHAVIOR]]
```

This connects directly to:

```text
[[GOVERNANCE]]
[[AUTHORITY]]
[[PERMISSIONS]]
[[DELEGATION]]
[[AGENTS]]
[[AUTONOMY]]
```

---

# 11. `[[ROOT_CAUSE_THINKING]]`

Do not stop at symptoms.

```text
[[SYMPTOM]]
   ↓
[[EVENT]]
   ↓
[[CAUSE]]
   ↓
[CONTRIBUTING FACTORS]
   ↓
[ROOT CAUSE]
   ↓
[CORRECTIVE ACTION]
   ↓
[[VERIFICATION]]
```

Useful methods:

```text
[[5_WHYS]]
[[FISHBONE]]
[[FAULT_TREE]]
[[CAUSE_EFFECT]]
[[FAILURE_MODE_ANALYSIS]]
```

And:

```text
[[SYMPTOM]]
≠
[[ROOT_CAUSE]]
```

---

# 12. `[[DECOMPOSITION_THINKING]]`

Ask:

> **What smaller problems make up the larger problem?**

```text
[[WHOLE]]
   ↓
[[SUBSYSTEMS]]
   ↓
[[COMPONENTS]]
   ↓
[[SUBPROBLEMS]]
   ↓
[[TASKS]]
   ↓
[[ACTIONS]]
```

Example:

```text
[BUILD COMPANY BRAIN]
        ↓
├── [[IDENTITY]]
├── [[KNOWLEDGE]]
├── [[DATA]]
├── [[INFRASTRUCTURE]]
├── [[AGENTS]]
├── [[TOOLS]]
├── [[ORCHESTRATION]]
├── [[SECURITY]]
├── [[GOVERNANCE]]
├── [[OBSERVABILITY]]
└── [[EXECUTION]]
```

Then each branch decomposes recursively.

---

# The 12-framework thinking matrix

| Framework                       | Primary question                     | Main object  |
| ------------------------------- | ------------------------------------ | ------------ |
| `[[SYSTEMS_THINKING]]`          | How do the parts interact?           | System       |
| `[[FIRST_PRINCIPLES]]`          | What is fundamentally true?          | Assumptions  |
| `[[SECOND_ORDER_THINKING]]`     | What happens afterward?              | Consequences |
| `[[PROBABILISTIC_THINKING]]`    | What does the evidence imply?        | Uncertainty  |
| `[[INVERSION]]`                 | How could this fail?                 | Failure      |
| `[[SCENARIO_THINKING]]`         | What futures are possible?           | Scenarios    |
| `[[CONSTRAINT_THINKING]]`       | What limits the system?              | Bottleneck   |
| `[[OPPORTUNITY_COST_THINKING]]` | What are we giving up?               | Tradeoff     |
| `[[OODA_LOOP]]`                 | How do we continuously adapt?        | Action loop  |
| `[[MECHANISM_DESIGN]]`          | How do rules shape behavior?         | Incentives   |
| `[[ROOT_CAUSE_THINKING]]`       | Why did this actually happen?        | Causality    |
| `[[DECOMPOSITION_THINKING]]`    | What smaller problems comprise this? | Structure    |

---

# The deeper ontology

These frameworks operate on different dimensions:

```text
                         [[PROBLEM]]
                              │
          ┌───────────────────┼────────────────────┐
          ↓                   ↓                    ↓
     [[STRUCTURE]]       [[CAUSALITY]]        [[UNCERTAINTY]]
          │                   │                    │
   SYSTEMS THINKING      ROOT CAUSE          PROBABILISTIC
   DECOMPOSITION         SECOND ORDER         SCENARIOS
                              │
                              ↓
                         [[FAILURE]]
                              │
                         INVERSION
                              │
                              ↓
                         [[LIMITS]]
                              │
                      CONSTRAINT THINKING
                              │
                              ↓
                         [[CHOICES]]
                              │
                     OPPORTUNITY COST
                              │
                              ↓
                         [[BEHAVIOR]]
                              │
                      MECHANISM DESIGN
                              │
                              ↓
                         [[EXECUTION]]
                              │
                           OODA
                              │
                              ↓
                           OUTCOME
```

---

# Thinking Framework Router

This is where it becomes useful for your agents.

Create:

```text
[[THINKING_FRAMEWORK_ROUTER]]
```

Its job:

```text
[[QUESTION]]
     ↓
[[PROBLEM_CLASSIFICATION]]
     ↓
[SELECT THINKING FRAMEWORK]
     ↓
[APPLY FRAMEWORK]
     ↓
[GENERATE INSIGHTS]
     ↓
[COMPARE PERSPECTIVES]
     ↓
[[SYNTHESIZE]]
     ↓
[ANSWER / DECISION / ACTION]
```

For example:

```text
"Why is this system failing?"
        ↓
[[ROOT_CAUSE_THINKING]]
        +
[[SYSTEMS_THINKING]]
        +
[[INVERSION]]
```

Or:

```text
"Should we build this?"
        ↓
[[FIRST_PRINCIPLES]]
        +
[[OPPORTUNITY_COST_THINKING]]
        +
[[CONSTRAINT_THINKING]]
        +
[[SCENARIO_THINKING]]
```

Or:

```text
"Can this run autonomously?"
        ↓
[[SYSTEMS_THINKING]]
        +
[[DECOMPOSITION_THINKING]]
        +
[[INVERSION]]
        +
[[SCENARIO_THINKING]]
        +
[[OODA_LOOP]]
```

---

# Thinking as a graph

The important part for your Company Brain is that **frameworks should themselves be graph nodes**.

```text
[[QUESTION]]
      ↓
[[PROBLEM]]
      ↓
[[THINKING_FRAMEWORK]]
      ↓
[[REASONING_PROCESS]]
      ↓
[[INSIGHT]]
      ↓
[[EVIDENCE]]
      ↓
[[ANSWER]]
      ↓
[[DECISION]]
      ↓
[[ACTION]]
      ↓
[[OUTCOME]]
      ↓
[[FEEDBACK]]
      ↺
```

Relationships:

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

---

# Recursive thinking

This is the part that fits your larger architecture particularly well.

An agent shouldn't necessarily use **one** framework.

It can recursively compose them:

```text
[[QUESTION]]
    ↓
[[SYSTEMS_THINKING]]
    ↓
[[DECOMPOSITION]]
    ↓
[[ROOT_CAUSE]]
    ↓
[[FIRST_PRINCIPLES]]
    ↓
[[CONSTRAINT]]
    ↓
[[INVERSION]]
    ↓
[[SECOND_ORDER]]
    ↓
[[SCENARIOS]]
    ↓
[[PROBABILISTIC]]
    ↓
[[OPPORTUNITY_COST]]
    ↓
[[OODA]]
    ↓
[[DECISION]]
```

This creates a:

```text
[[THINKING_PIPELINE]]
```

rather than a static list of frameworks.

---

# Master bracket vocabulary

```text
[[THINKING]]
[[THINKING_FRAMEWORKS]]
[[REASONING]]
[[REASONING_ENGINE]]
[[COGNITION]]
[[COGNITIVE_PROCESS]]
[[PROBLEM_SOLVING]]
[[DECISION_MAKING]]

[[SYSTEMS_THINKING]]
[[FIRST_PRINCIPLES]]
[[SECOND_ORDER_THINKING]]
[[PROBABILISTIC_THINKING]]
[[INVERSION]]
[[SCENARIO_THINKING]]
[[CONSTRAINT_THINKING]]
[[OPPORTUNITY_COST_THINKING]]
[[OODA_LOOP]]
[[MECHANISM_DESIGN]]
[[ROOT_CAUSE_THINKING]]
[[DECOMPOSITION_THINKING]]

[[ASSUMPTION]]
[[FACT]]
[[EVIDENCE]]
[[HYPOTHESIS]]
[[CAUSALITY]]
[[CONSEQUENCE]]
[[UNCERTAINTY]]
[[RISK]]
[[SCENARIO]]
[[CONSTRAINT]]
[[BOTTLENECK]]
[[TRADEOFF]]
[[INCENTIVE]]
[[FAILURE_MODE]]
[[ROOT_CAUSE]]
[[SUBPROBLEM]]
[[DEPENDENCY]]

[[OBSERVE]]
[[ORIENT]]
[[DECIDE]]
[[ACT]]

[[INSIGHT]]
[[SYNTHESIS]]
[[DECISION]]
[[ACTION]]
[[OUTCOME]]
[[FEEDBACK]]
[[LEARNING]]

[[THINKING_FRAMEWORK_ROUTER]]
[[THINKING_PIPELINE]]
[[REASONING_GRAPH]]
[[REASONING_CHAIN]]
[[REASONING_TRACE]]
[[REASONING_CONTEXT]]
[[REASONING_EVIDENCE]]
[[REASONING_VERIFICATION]]
```

## The ultimate Company Brain relationship

Your **Question Ontology** and **Thinking Ontology** should connect directly:

```text
[[REALITY]]
      ↓
[[UNKNOWN]]
      ↓
[[QUESTION]]
      ↓
[[KNOWLEDGE_GAP]]
      ↓
[[QUESTION_CLASSIFICATION]]
      ↓
[[THINKING_FRAMEWORK_ROUTER]]
      ↓
┌──────────────────────────────────────┐
│  [[SYSTEMS_THINKING]]                │
│  [[FIRST_PRINCIPLES]]                │
│  [[SECOND_ORDER_THINKING]]           │
│  [[PROBABILISTIC_THINKING]]          │
│  [[INVERSION]]                       │
│  [[SCENARIO_THINKING]]               │
│  [[CONSTRAINT_THINKING]]             │
│  [[OPPORTUNITY_COST_THINKING]]       │
│  [[OODA_LOOP]]                       │
│  [[MECHANISM_DESIGN]]                │
│  [[ROOT_CAUSE_THINKING]]             │
│  [[DECOMPOSITION_THINKING]]          │
└──────────────────────────────────────┘
      ↓
[[REASONING]]
      ↓
[[INSIGHT]]
      ↓
[[EVIDENCE]]
      ↓
[[VERIFICATION]]
      ↓
[[KNOWLEDGE]]
      ↓
[[DECISION]]
      ↓
[[TASK]]
      ↓
[[AGENT]]
      ↓
[[ACTION]]
      ↓
[[OUTCOME]]
      ↓
[[FEEDBACK]]
      ↺
```

So the architecture becomes:

**Questions determine what needs to be known.
Thinking frameworks determine how to investigate it.
Evidence determines what can be supported.
Verification determines what can be trusted.
Decisions determine what should happen.
Agents and workflows determine how it happens.
Outcomes determine what the system learns.**


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
