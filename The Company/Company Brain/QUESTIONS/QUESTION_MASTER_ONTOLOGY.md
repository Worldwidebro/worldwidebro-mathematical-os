---
type: master-ontology
status: conceptual
prerequisites: []
requires: []
---

# `QUESTION_MASTER_ONTOLOGY.md`

```text
[[QUESTION]]

├── [[QUESTION_IDENTITY]]
│   ├── [[QUESTION_ID]]
│   ├── [[QUESTION_TEXT]]
│   ├── [[QUESTION_TYPE]]
│   ├── [[QUESTION_CLASS]]
│   ├── [[QUESTION_STATUS]]
│   ├── [[QUESTION_VERSION]]
│   ├── [[QUESTION_ORIGIN]]
│   └── [[QUESTION_PARENT]]
│
├── [[QUESTION_ACTOR]]
│   ├── [[ASKER]]
│   ├── [[AUDIENCE]]
│   ├── [[OWNER]]
│   ├── [[DECISION_MAKER]]
│   ├── [[ANSWERER]]
│   ├── [[AGENT]]
│   ├── [[SYSTEM]]
│   └── [[STAKEHOLDER]]
│
├── [[QUESTION_INTENT]]
│   ├── [[UNDERSTAND]]
│   ├── [[DISCOVER]]
│   ├── [[VERIFY]]
│   ├── [[DIAGNOSE]]
│   ├── [[COMPARE]]
│   ├── [[EVALUATE]]
│   ├── [[PREDICT]]
│   ├── [[EXPLAIN]]
│   ├── [[CLASSIFY]]
│   ├── [[LOCATE]]
│   ├── [[IDENTIFY]]
│   ├── [[QUANTIFY]]
│   ├── [[OPTIMIZE]]
│   ├── [[DECIDE]]
│   ├── [[PLAN]]
│   ├── [[CREATE]]
│   ├── [[CONTROL]]
│   ├── [[MONITOR]]
│   └── [[LEARN]]
│
├── [[QUESTION_TARGET]]
│   ├── [[ENTITY]]
│   ├── [[OBJECT]]
│   ├── [[SYSTEM]]
│   ├── [[PROCESS]]
│   ├── [[EVENT]]
│   ├── [[STATE]]
│   ├── [[RELATIONSHIP]]
│   ├── [[DATA]]
│   ├── [[DOCUMENT]]
│   ├── [[FILE]]
│   ├── [[REPOSITORY]]
│   ├── [[AGENT]]
│   ├── [[TASK]]
│   ├── [[PERSON]]
│   ├── [[ORGANIZATION]]
│   ├── [[MARKET]]
│   ├── [[CUSTOMER]]
│   └── [[ENVIRONMENT]]
│
├── [[QUESTION_DIMENSIONS]]
│   ├── [[WHO]]
│   ├── [[WHAT]]
│   ├── [[WHY]]
│   ├── [[WHEN]]
│   ├── [[WHERE]]
│   ├── [[HOW]]
│   ├── [[HOW_MUCH]]
│   ├── [[HOW_MANY]]
│   ├── [[WHICH]]
│   ├── [[WHETHER]]
│   └── [[WHAT_IF]]
│
├── [[QUESTION_SCOPE]]
│   ├── [[TIME_SCOPE]]
│   ├── [[GEOGRAPHIC_SCOPE]]
│   ├── [[ENTITY_SCOPE]]
│   ├── [[SYSTEM_SCOPE]]
│   ├── [[DATA_SCOPE]]
│   ├── [[ENVIRONMENT_SCOPE]]
│   ├── [[DEPARTMENT_SCOPE]]
│   └── [[BUSINESS_SCOPE]]
│
├── [[QUESTION_CONTEXT]]
│   ├── [[BACKGROUND]]
│   ├── [[CURRENT_STATE]]
│   ├── [[KNOWN_FACTS]]
│   ├── [[UNKNOWN_FACTS]]
│   ├── [[ASSUMPTIONS]]
│   ├── [[CONSTRAINTS]]
│   ├── [[DEPENDENCIES]]
│   ├── [[PRIOR_ANSWERS]]
│   └── [[RELATED_QUESTIONS]]
│
├── [[QUESTION_EPISTEMOLOGY]]
│   ├── [[KNOWN]]
│   ├── [[UNKNOWN]]
│   ├── [[UNCERTAIN]]
│   ├── [[AMBIGUOUS]]
│   ├── [[CONTESTED]]
│   ├── [[UNVERIFIED]]
│   ├── [[MISSING_DATA]]
│   ├── [[MISSING_CONTEXT]]
│   └── [[KNOWLEDGE_GAP]]
│
├── [[EVIDENCE_REQUIREMENTS]]
│   ├── [[EVIDENCE]]
│   ├── [[SOURCE]]
│   ├── [[SOURCE_OF_TRUTH]]
│   ├── [[PRIMARY_SOURCE]]
│   ├── [[SECONDARY_SOURCE]]
│   ├── [[OBSERVATION]]
│   ├── [[DOCUMENT]]
│   ├── [[DATASET]]
│   ├── [[CODE]]
│   ├── [[LOG]]
│   ├── [[TEST]]
│   ├── [[EXPERIMENT]]
│   └── [[WITNESS]]
│
├── [[RESEARCH]]
│   ├── [[SEARCH]]
│   ├── [[RETRIEVAL]]
│   ├── [[BROWSING]]
│   ├── [[DOCUMENT_REVIEW]]
│   ├── [[DATA_ANALYSIS]]
│   ├── [[CODE_ANALYSIS]]
│   ├── [[INTERVIEW]]
│   ├── [[EXPERIMENT]]
│   └── [[INVESTIGATION]]
│
├── [[ANSWER]]
│   ├── [[ANSWER]]
│   ├── [[ANSWER_TYPE]]
│   ├── [[ANSWER_STATUS]]
│   ├── [[ANSWER_CONFIDENCE]]
│   ├── [[ANSWER_SCOPE]]
│   ├── [[ANSWER_EVIDENCE]]
│   ├── [[ANSWER_LIMITATIONS]]
│   ├── [[ANSWER_ASSUMPTIONS]]
│   └── [[ANSWER_PROVENANCE]]
│
├── [[VERIFICATION]]
│   ├── [[ANSWER_VERIFICATION]]
│   ├── [[FACT_CHECK]]
│   ├── [[CROSS_CHECK]]
│   ├── [[REPRODUCTION]]
│   ├── [[TEST]]
│   ├── [[VALIDATION]]
│   └── [[AUDIT]]
│
├── [[DECISION]]
│   ├── [[DECISION_REQUIRED]]
│   ├── [[DECISION_INFORMED]]
│   ├── [[OPTIONS]]
│   ├── [[CRITERIA]]
│   ├── [[TRADEOFFS]]
│   ├── [[RISK]]
│   └── [[DECISION_OUTCOME]]
│
├── [[ACTION]]
│   ├── [[TASK_CREATED]]
│   ├── [[ACTION_TRIGGERED]]
│   ├── [[AGENT_ASSIGNED]]
│   ├── [[WORKFLOW_TRIGGERED]]
│   ├── [[IMPLEMENTATION]]
│   └── [[FOLLOW_UP]]
│
├── [[QUESTION_GRAPH]]
│   ├── [[PARENT_QUESTION]]
│   ├── [[CHILD_QUESTION]]
│   ├── [[RELATED_QUESTION]]
│   ├── [[DUPLICATE_QUESTION]]
│   ├── [[PREREQUISITE_QUESTION]]
│   ├── [[FOLLOW_UP_QUESTION]]
│   ├── [[CONDITIONAL_QUESTION]]
│   ├── [[CONTRADICTORY_QUESTION]]
│   └── [[SUPERSEDING_QUESTION]]
│
├── [[QUESTION_LIFECYCLE]]
│   ├── [[CREATED]]
│   ├── [[CAPTURED]]
│   ├── [[CLASSIFIED]]
│   ├── [[REFINED]]
│   ├── [[QUEUED]]
│   ├── [[RESEARCHING]]
│   ├── [[ANSWERED]]
│   ├── [[VERIFIED]]
│   ├── [[PARTIALLY_ANSWERED]]
│   ├── [[BLOCKED]]
│   ├── [[UNRESOLVED]]
│   ├── [[SUPERSEDED]]
│   └── [[CLOSED]]
│
└── [[QUESTION_REALITY]]
    ├── [[QUESTION_VALID]]
    ├── [[QUESTION_ANSWERABLE]]
    ├── [[QUESTION_VERIFIED]]
    ├── [[ANSWER_VERIFIED]]
    ├── [[EVIDENCE_SUFFICIENT]]
    ├── [[EVIDENCE_INSUFFICIENT]]
    └── [[UNKNOWN_REMAINS]]
```

# 1. The fundamental question loop

This should become one of the core Company Brain loops:

```text
[[UNKNOWN]]
    ↓
[[QUESTION]]
    ↓
[[QUESTION_INTENT]]
    ↓
[[QUESTION_SCOPE]]
    ↓
[[KNOWLEDGE_GAP]]
    ↓
[[EVIDENCE_REQUIREMENT]]
    ↓
[[RESEARCH]]
    ↓
[[ANSWER]]
    ↓
[[VERIFICATION]]
    ↓
[[KNOWLEDGE]]
    ↓
[[DECISION]]
    ↓
[[ACTION]]
    ↓
[[OUTCOME]]
    ↓
[[NEW_EVIDENCE]]
    ↓
[[NEW_QUESTION]]
    ↺
```

That means **questions become the entry point to the intelligence loop**.

---

# 2. The universal question grammar

Every question can be decomposed into:

```text
[[ASKER]]
+
[[INTENT]]
+
[[TARGET]]
+
[[DIMENSION]]
+
[[SCOPE]]
+
[[CONTEXT]]
+
[[CONSTRAINTS]]
+
[[EVIDENCE_REQUIREMENT]]
+
[[ANSWER_CRITERIA]]
```

For example:

> “Where is the actual OmniRoute data stored?”

becomes:

```yaml
question_id: Q-0001

intent: LOCATE

target: [[OMNIROUTE_DATA]]

dimension: WHERE

scope:
  system: [[OMNIROUTE]]

context:
  environment: [[MAC_STUDIO]]

evidence_required:
  - filesystem_observation
  - mount_information

answer_criteria:
  - actual_path
  - mounted_volume
  - verification_status
```

---

# 3. The 12 fundamental question dimensions

Your ontology should normalize natural-language questions into these primitives:

```text
[[WHO]]
[[WHAT]]
[[WHY]]
[[WHEN]]
[[WHERE]]
[[HOW]]
[[HOW_MUCH]]
[[HOW_MANY]]
[[WHICH]]
[[WHETHER]]
[[WHAT_IF]]
[[WHAT_NEXT]]
```

Then compound questions become compositions.

### WHO

```text
Who owns this?
Who operates this?
Who has access?
Who created it?
Who should act?
```

### WHAT

```text
What is this?
What happened?
What exists?
What changed?
What does it do?
```

### WHY

```text
Why does this exist?
Why did this fail?
Why was this decision made?
Why is this dependency required?
```

### WHEN

```text
When was it created?
When did it fail?
When does it expire?
When should it run?
```

### WHERE

```text
Where is it stored?
Where is it deployed?
Where did the event occur?
Where is the source of truth?
```

### HOW

```text
How does it work?
How is it connected?
How do we implement it?
How do we verify it?
```

### HOW_MUCH

```text
How much does it cost?
How much storage does it consume?
How much revenue does it produce?
```

### HOW_MANY

```text
How many repositories?
How many agents?
How many customers?
How many dependencies?
```

### WHICH

```text
Which repository?
Which provider?
Which agent?
Which implementation?
```

### WHETHER

```text
Is it working?
Does it exist?
Can it connect?
Should it be deployed?
```

### WHAT_IF

```text
What happens if this fails?
What happens if the credential expires?
What happens if the disk disappears?
```

### WHAT_NEXT

```text
What should happen next?
What is blocked?
What action follows?
```

---

# 4. Question classes

I'd create these major classes:

```text
[[FACTUAL]]
[[DEFINITIONAL]]
[[DESCRIPTIVE]]
[[LOCATIONAL]]
[[IDENTIFICATION]]
[[EXPLANATORY]]
[[CAUSAL]]
[[DIAGNOSTIC]]
[[COMPARATIVE]]
[[QUANTITATIVE]]
[[VERIFICATION]]
[[VALIDATION]]
[[CLASSIFICATION]]
[[RELATIONAL]]
[[DEPENDENCY]]
[[PROCEDURAL]]
[[STRATEGIC]]
[[OPERATIONAL]]
[[PREDICTIVE]]
[[SCENARIO]]
[[OPTIMIZATION]]
[[DECISION]]
[[PLANNING]]
[[RESEARCH]]
[[DISCOVERY]]
[[CREATIVE]]
[[GENERATIVE]]
[[REFLECTIVE]]
[[METACOGNITIVE]]
```

---

# 5. Factual questions

```text
[Factual Question]
      ↓
[Known/Unknown Fact]
      ↓
[[Source]]
      ↓
[[Evidence]]
      ↓
[[Answer]]
```

Example:

```text
How many repositories exist?
```

The answer should ideally come from an authoritative repository inventory, not an old conversation.

---

# 6. Definition questions

```text
WHAT_IS_X?
WHAT_DOES_X_MEAN?
WHAT_COUNTS_AS_X?
WHAT_IS_THE_BOUNDARY_OF_X?
```

These are important for ontology construction.

Example:

```text
What exactly counts as a [[VENTURE]]?
```

---

# 7. Diagnostic questions

These are particularly important for infrastructure.

```text
[[SYMPTOM]]
   ↓
[[QUESTION]]
   ↓
[[HYPOTHESIS]]
   ↓
[[TEST]]
   ↓
[[OBSERVATION]]
   ↓
[[ROOT_CAUSE]]
```

Example:

```text
Why can't Claude Code reach OmniRoute?
```

Break into:

```text
Is Claude Code running?
        ↓
Can DNS resolve?
        ↓
Can the host be reached?
        ↓
Is the port open?
        ↓
Is the service listening?
        ↓
Is authentication valid?
        ↓
Is authorization valid?
        ↓
Does the provider respond?
```

One human question becomes a **question tree**.

---

# 8. Question decomposition

This is one of the most powerful parts.

```text
[MASTER QUESTION]
       │
       ├── [SUBQUESTION A]
       │      ├── [SUBQUESTION A1]
       │      └── [SUBQUESTION A2]
       │
       ├── [SUBQUESTION B]
       │      ├── [SUBQUESTION B1]
       │      └── [SUBQUESTION B2]
       │
       └── [SUBQUESTION C]
```

Example:

```text
[Can the Company Brain autonomously operate a repository?]
                │
                ├── Does it know the repository exists?
                │
                ├── Can it authenticate?
                │
                ├── Can it read the repository?
                │
                ├── Can it understand the code?
                │
                ├── Can it create a task?
                │
                ├── Can it modify code?
                │
                ├── Can it run tests?
                │
                ├── Can it create a PR?
                │
                ├── Can it verify CI?
                │
                ├── Can it deploy?
                │
                └── Can it verify the outcome?
```

That is a **question DAG**, not merely a list.

---

# 9. Question dependencies

Add:

```text
[[REQUIRES_ANSWER_TO]]
[[DEPENDS_ON]]
[[BLOCKED_BY]]
[[ENABLES]]
[[RESOLVES]]
[[REFINES]]
[[EXPANDS]]
[[CONTRADICTS]]
[[FOLLOWS]]
[[SUPERSEDES]]
```

Example:

```text
Q1: Does OmniRoute exist?
        ↓
Q2: Is OmniRoute running?
        ↓
Q3: Is OmniRoute reachable?
        ↓
Q4: Can Claude authenticate?
        ↓
Q5: Can Claude invoke a model?
```

Therefore:

```text
Q5 [[DEPENDS_ON]] Q4
Q4 [[DEPENDS_ON]] Q3
Q3 [[DEPENDS_ON]] Q2
Q2 [[DEPENDS_ON]] Q1
```

---

# 10. Questions and knowledge gaps

This is the bridge into your knowledge graph:

```text
[[QUESTION]]
      ↓
[[UNKNOWN]]
      ↓
[[KNOWLEDGE_GAP]]
      ↓
[[RESEARCH]]
      ↓
[[KNOWLEDGE]]
```

A knowledge gap should itself become an entity:

```yaml
gap_id: GAP-001

question: Q-001

unknown:
  - actual_omniroute_host

impact:
  - connectivity
  - Claude integration

required_evidence:
  - infrastructure_scan
  - Docker inspection

status: OPEN
```

---

# 11. Question → source selection

The question itself should determine where to look.

```text
QUESTION
   ↓
QUESTION_TYPE
   ↓
SOURCE_SELECTION
```

Example:

```text
"What is the actual file path?"
        ↓
[[FILESYSTEM]]

"Does this repository contain X?"
        ↓
[[GITHUB]]

"What does this document say?"
        ↓
[[DOCUMENT]]

"Is the service running?"
        ↓
[[INFRASTRUCTURE]]

"What relationships exist?"
        ↓
[[NEO4J]]

"What similar concepts exist?"
        ↓
[[QDRANT]]

"What does current external documentation say?"
        ↓
[[WEB_RESEARCH]]
```

This creates a **question routing engine**.

---

# 12. Question routing ontology

```text
[[QUESTION]]
     ↓
[[CLASSIFY]]
     ↓
[[ROUTE]]
     │
     ├── [[FILESYSTEM_AGENT]]
     ├── [[GITHUB_AGENT]]
     ├── [[WEB_RESEARCH_AGENT]]
     ├── [[DATABASE_AGENT]]
     ├── [[KNOWLEDGE_AGENT]]
     ├── [[INFRASTRUCTURE_AGENT]]
     ├── [[SECURITY_AGENT]]
     ├── [[FINANCE_AGENT]]
     ├── [[SALES_AGENT]]
     └── [[GENERAL_REASONING_AGENT]]
```

Then:

```text
[[QUESTION]]
     ↓
[[ROUTER]]
     ↓
[[AGENT]]
     ↓
[[TOOL]]
     ↓
[[SOURCE]]
     ↓
[[EVIDENCE]]
     ↓
[[ANSWER]]
```

---

# 13. Question → evidence → answer

This distinction should be hard-coded:

```text
[[QUESTION]]
     ↓
[[CLAIM]]
     ↓
[[EVIDENCE]]
     ↓
[[ANSWER]]
```

And:

```text
[[ANSWER]]
≠
[[TRUTH]]
```

Instead:

```text
[[ANSWER]]
     ↓
[[VERIFICATION]]
     ↓
[[VERIFIED_KNOWLEDGE]]
```

This fits perfectly with your:

```text
[[REALITY]]
[[SOURCE_OF_TRUTH]]
[[EVIDENCE]]
[[VERIFICATION]]
```

---

# 14. Answer states

```text
[[ANSWERED]]
[[VERIFIED]]
[[PARTIALLY_ANSWERED]]
[[UNVERIFIED]]
[[UNCERTAIN]]
[[CONTESTED]]
[[INSUFFICIENT_EVIDENCE]]
[[UNKNOWN]]
[[NOT_ANSWERABLE]]
[[BLOCKED]]
[[SUPERSEDED]]
```

Important:

```text
[[ANSWERED]]
≠
[[VERIFIED]]
```

And:

```text
[[NO_ANSWER]]
≠
[[NOT_ANSWERABLE]]
```

---

# 15. Question confidence

Avoid treating confidence as truth.

Use separate dimensions:

```text
[[ANSWER_CONFIDENCE]]
[[EVIDENCE_STRENGTH]]
[[SOURCE_AUTHORITY]]
[[VERIFICATION_STATUS]]
[[UNCERTAINTY]]
[[AMBIGUITY]]
```

For example:

```yaml
answer:
  confidence: medium

evidence:
  strength: high

source:
  authority: primary

verification:
  status: verified
```

Those are different properties.

---

# 16. Question → decision

Some questions exist because a decision must be made.

```text
[[DECISION]]
      ↓
[[DECISION_QUESTIONS]]
      ↓
[[RESEARCH]]
      ↓
[[OPTIONS]]
      ↓
[[TRADEOFFS]]
      ↓
[[DECISION]]
```

Example:

```text
Should this repository become a production service?
```

Break into:

```text
What does it do?
What dependencies does it have?
Is it maintained?
Is it secure?
Does it work?
What infrastructure does it require?
What does deployment require?
What does it cost?
What business capability does it provide?
What revenue opportunity does it support?
What risks exist?
```

The system then supplies information to the human decision-maker or authorized decision process.

---

# 17. Question → task

Questions that cannot be answered immediately become work.

```text
[[QUESTION]]
     ↓
[[UNANSWERED]]
     ↓
[[RESEARCH_TASK]]
     ↓
[[AGENT]]
     ↓
[[INVESTIGATION]]
     ↓
[[EVIDENCE]]
     ↓
[[ANSWER]]
```

This means your task system can contain:

```text
[[QUESTION_TASK]]
[[RESEARCH_TASK]]
[[VERIFICATION_TASK]]
[[INVESTIGATION_TASK]]
[[DIAGNOSTIC_TASK]]
[[DATA_COLLECTION_TASK]]
```

---

# 18. Questions that create other questions

Questions recursively generate questions:

```text
Q0
│
├── Q1
│   ├── Q1.1
│   └── Q1.2
│
├── Q2
│   ├── Q2.1
│   └── Q2.2
│
└── Q3
```

Then:

```text
Q0
 ↓
Q1 + Q2 + Q3
 ↓
Answers
 ↓
Synthesis
 ↓
Q0 Answer
```

This is the basis of **recursive research**.

---

# 19. Question graph

Add a dedicated graph:

```text
[[QUESTION_GRAPH]]

QUESTION
 ├── [[PARENT_OF]]
 ├── [[CHILD_OF]]
 ├── [[DEPENDS_ON]]
 ├── [[REQUIRES]]
 ├── [[REFINES]]
 ├── [[EXPANDS]]
 ├── [[CONTRADICTS]]
 ├── [[DUPLICATES]]
 ├── [[FOLLOWS]]
 ├── [[ANSWERS]]
 ├── [[GENERATES]]
 ├── [[BLOCKS]]
 └── [[SUPERSEDES]]
```

Now questions themselves become graph nodes.

---

# 20. Question registry

Create:

```text
QUESTION_REGISTRY.md
```

Example:

```yaml
question_id: Q-2026-0001

text: "Where is the actual OmniRoute data stored?"

type: LOCATIONAL

intent: LOCATE

actor:
  asker: USER
  owner: INFRASTRUCTURE_AGENT

target:
  - [[OMNIROUTE]]
  - [[OMNIROUTE_DATA]]

dimensions:
  - [[WHERE]]

scope:
  system: [[MAC_STUDIO]]

status: ANSWERED

answer:
  status: VERIFIED
  evidence:
    - [[FILESYSTEM_SCAN]]
    - [[MOUNT_INSPECTION]]

dependencies: []

follow_up_questions:
  - Q-2026-0002

created_at: ...
answered_at: ...
verified_at: ...
```

---

# 21. Question lifecycle

```text
[[QUESTION_CAPTURED]]
        ↓
[[CLASSIFIED]]
        ↓
[[CONTEXTUALIZED]]
        ↓
[[SCOPED]]
        ↓
[[DECOMPOSED]]
        ↓
[[ROUTED]]
        ↓
[[RESEARCHING]]
        ↓
[[EVIDENCE_COLLECTED]]
        ↓
[[ANSWER_DRAFTED]]
        ↓
[[VERIFIED]]
        ↓
[[KNOWLEDGE_UPDATED]]
        ↓
[DECISION/ACTION]
        ↓
[[CLOSED]]
```

But it can branch:

```text
                    ┌→ [[BLOCKED]]
                    │
[[RESEARCHING]] ──────┼→ [[PARTIAL]]
                    │
                    ├→ [[UNRESOLVED]]
                    │
                    └→ [[ANSWERED]]
```

---

# 22. Question automation agent

I would create:

```text
[[QUESTION_ORCHESTRATOR]]
```

with capabilities:

```text
[[CAPTURE_QUESTION]]
[[CLASSIFY_QUESTION]]
[[DETECT_AMBIGUITY]]
[[RESOLVE_CONTEXT]]
[[IDENTIFY_TARGET]]
[[IDENTIFY_INTENT]]
[[DETERMINE_SCOPE]]
[[DETECT_DUPLICATES]]
[[DECOMPOSE_QUESTION]]
[[BUILD_QUESTION_GRAPH]]
[[SELECT_SOURCE]]
[[SELECT_AGENT]]
[[SELECT_TOOL]]
[[RESEARCH]]
[[COLLECT_EVIDENCE]]
[[SYNTHESIZE]]
[[ANSWER]]
[[VERIFY]]
[[UPDATE_KNOWLEDGE]]
[[CREATE_FOLLOWUP]]
[[CREATE_TASK]]
[[TRIGGER_DECISION]]
[[CLOSE_QUESTION]]
```

---

# 23. Ambiguity detection

This should be a first-class capability.

```text
[[QUESTION]]
     ↓
[[AMBIGUITY_DETECTION]]
     ├── ambiguous_entity
     ├── ambiguous_time
     ├── ambiguous_scope
     ├── ambiguous_intent
     ├── ambiguous_reference
     ├── missing_context
     └── undefined_term
```

Example:

> “Is it working?”

The system should ask:

```text
What is "it"?
Working in what sense?
At what layer?
Against what expected result?
In which environment?
When was it last tested?
```

So:

```text
AMBIGUOUS QUESTION
        ↓
QUESTION REFINEMENT
        ↓
ANSWERABLE QUESTION
```

---

# 24. Question quality ontology

A question can be evaluated structurally:

```text
[[QUESTION_QUALITY]]

├── [[CLARITY]]
├── [[SPECIFICITY]]
├── [[SCOPE]]
├── [[CONTEXT]]
├── [[ANSWERABILITY]]
├── [[EVIDENCEABILITY]]
├── [[RELEVANCE]]
├── [[ACTIONABILITY]]
├── [[NON_DUPLICATION]]
└── [[DECISION_RELEVANCE]]
```

Not as a generic “good/bad” score, but as diagnostic dimensions.

---

# 25. Questions and the entire Company Brain

This is the deeper architecture:

```text
                         [[REALITY]]
                             ↓
                       [[OBSERVATION]]
                             ↓
                           [[DATA]]
                             ↓
                         [[UNKNOWN]]
                             ↓
                        [[QUESTION]]
                             ↓
                     [[QUESTION_GRAPH]]
                             ↓
                       [[RESEARCH]]
                             ↓
                         [[EVIDENCE]]
                             ↓
                         [[ANSWER]]
                             ↓
                       [[VERIFICATION]]
                             ↓
                        [[KNOWLEDGE]]
                             ↓
                         [[CONTEXT]]
                             ↓
                        [[REASONING]]
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
                         [[OBSERVATION]]
                             ↓
                         [[EVIDENCE]]
                             ↓
                        [[LEARNING]]
                             ↓
                       [[NEW QUESTION]]
                             ↺
```

That gives you a much deeper interpretation of the Company Brain:

> **The system is not primarily an answer machine. It is a question-management and reality-resolution system.**

---

# 26. Master question vocabulary

```text
[[QUESTION]]
[[QUESTIONS]]
[[QUESTION_ID]]
[[QUESTION_TEXT]]
[[QUESTION_TYPE]]
[[QUESTION_CLASS]]
[[QUESTION_STATUS]]
[[QUESTION_INTENT]]
[[QUESTION_TARGET]]
[[QUESTION_SCOPE]]
[[QUESTION_CONTEXT]]

[[WHO]]
[[WHAT]]
[[WHY]]
[[WHEN]]
[[WHERE]]
[[HOW]]
[[HOW_MUCH]]
[[HOW_MANY]]
[[WHICH]]
[[WHETHER]]
[[WHAT_IF]]
[[WHAT_NEXT]]

[[ASKER]]
[[ANSWERER]]
[[OWNER]]
[[STAKEHOLDER]]
[[DECISION_MAKER]]

[[UNKNOWN]]
[[KNOWN]]
[[UNCERTAINTY]]
[[AMBIGUITY]]
[[KNOWLEDGE_GAP]]
[[MISSING_DATA]]
[[MISSING_CONTEXT]]
[[ASSUMPTION]]
[[CONSTRAINT]]

[[FACTUAL_QUESTION]]
[[DEFINITION_QUESTION]]
[[DIAGNOSTIC_QUESTION]]
[[CAUSAL_QUESTION]]
[[COMPARATIVE_QUESTION]]
[[VERIFICATION_QUESTION]]
[[PREDICTIVE_QUESTION]]
[[SCENARIO_QUESTION]]
[[OPTIMIZATION_QUESTION]]
[[DECISION_QUESTION]]
[[RESEARCH_QUESTION]]
[[DISCOVERY_QUESTION]]
[[PROCEDURAL_QUESTION]]

[[SUBQUESTION]]
[[PARENT_QUESTION]]
[[CHILD_QUESTION]]
[[FOLLOWUP_QUESTION]]
[[PREREQUISITE_QUESTION]]
[[RELATED_QUESTION]]
[[DUPLICATE_QUESTION]]
[[CONTRADICTORY_QUESTION]]
[[SUPERSEDING_QUESTION]]

[[QUESTION_GRAPH]]
[[QUESTION_DECOMPOSITION]]
[[QUESTION_ROUTING]]
[[QUESTION_ORCHESTRATION]]
[[QUESTION_QUEUE]]
[[QUESTION_REGISTRY]]

[[RESEARCH]]
[[INVESTIGATION]]
[[SEARCH]]
[[RETRIEVAL]]
[[EVIDENCE]]
[[SOURCE]]
[[SOURCE_OF_TRUTH]]
[[PROVENANCE]]

[[ANSWER]]
[[ANSWER_STATUS]]
[[ANSWER_CONFIDENCE]]
[[ANSWER_EVIDENCE]]
[[ANSWER_LIMITATIONS]]
[[ANSWER_PROVENANCE]]

[[VERIFICATION]]
[[VALIDATION]]
[[FACT_CHECK]]
[[CROSS_CHECK]]
[[REPRODUCTION]]
[[AUDIT]]

[[DECISION]]
[[DECISION_SUPPORT]]
[[OPTIONS]]
[[TRADEOFFS]]
[[RISK]]

[[QUESTION_TASK]]
[[RESEARCH_TASK]]
[[INVESTIGATION_TASK]]
[[VERIFICATION_TASK]]

[[QUESTION_ORCHESTRATOR]]
[[QUESTION_AGENT]]
[[RESEARCH_AGENT]]
[[ANSWER_AGENT]]
[[VERIFICATION_AGENT]]

[[QUESTION_REALITY]]
[[ANSWER_REALITY]]
[[QUESTION_SOURCE_OF_TRUTH]]
```

---

# 28. The ultimate relationship

I would add this to your **Cross-Link Master Ontology**:

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

And the **Company Brain master loop** becomes:

```text
[[REALITY]]
   ↓
[[UNKNOWN]]
   ↓
[[QUESTION]]
   ↓
[[KNOWLEDGE_GAP]]
   ↓
[[QUESTION_DECOMPOSITION]]
   ↓
[[QUESTION_ROUTING]]
   ↓
[[AGENT]]
   ↓
[[TOOLS]]
   ↓
[[EVIDENCE]]
   ↓
[[ANSWER]]
   ↓
[[VERIFICATION]]
   ↓
[[KNOWLEDGE]]
   ↓
[[DECISION]]
   ↓
[[TASK]]
   ↓
[[ACTION]]
   ↓
[[OUTCOME]]
   ↓
[[NEW_REALITY]]
   ↓
[[NEW_UNKNOWN]]
   ↓
[[NEW_QUESTION]]
   ↺
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
