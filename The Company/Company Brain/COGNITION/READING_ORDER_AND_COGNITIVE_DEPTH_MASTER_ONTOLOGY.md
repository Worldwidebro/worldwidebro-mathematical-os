---
type: master-ontology
status: conceptual
prerequisites: []
requires: []
---

# `READING_ORDER_AND_COGNITIVE_DEPTH_MASTER_ONTOLOGY.md`

```text
[[READING_ORDER]]

├── [[READING_SEQUENCE]]
│   ├── [[START_HERE]]
│   ├── [[PREREQUISITE]]
│   ├── [[FOUNDATION]]
│   ├── [[CONTEXT]]
│   ├── [[CONCEPT]]
│   ├── [[RELATIONSHIP]]
│   ├── [[MECHANISM]]
│   ├── [[APPLICATION]]
│   ├── [[EXECUTION]]
│   ├── [[REFLECTION]]
│   └── [[SYNTHESIS]]
│
├── [[COGNITIVE_PREREQUISITES]]
│   ├── [[KNOW_BEFORE_READING]]
│   ├── [[CONCEPT_DEPENDENCY]]
│   ├── [[CONTEXT_DEPENDENCY]]
│   ├── [[VOCABULARY_DEPENDENCY]]
│   ├── [[SYSTEM_DEPENDENCY]]
│   └── [[KNOWLEDGE_DEPENDENCY]]
│
├── [[AWARENESS]]
│   ├── [[OBSERVATION]]
│   ├── [[RECOGNITION]]
│   ├── [[DISTINCTION]]
│   ├── [[RELATION]]
│   ├── [[PATTERN]]
│   ├── [[STRUCTURE]]
│   ├── [[MECHANISM]]
│   ├── [[SYSTEM]]
│   └── [[META_AWARENESS]]
│
├── [[UNDERSTANDING]]
│   ├── [[DEFINITION]]
│   ├── [[CONTEXT]]
│   ├── [[MEANING]]
│   ├── [[RELATIONSHIPS]]
│   ├── [[CAUSALITY]]
│   ├── [[MECHANISM]]
│   ├── [[APPLICATION]]
│   ├── [[TRANSFER]]
│   └── [[SYNTHESIS]]
│
├── [[DEPTH]]
│   ├── [[SURFACE]]
│   ├── [[STRUCTURAL]]
│   ├── [[MECHANISTIC]]
│   ├── [[CAUSAL]]
│   ├── [[SYSTEMIC]]
│   ├── [[STRATEGIC]]
│   ├── [[META]]
│   └── [[GENERATIVE]]
│
├── [[READING_MODE]]
│   ├── [[SCAN]]
│   ├── [[ORIENT]]
│   ├── [[STUDY]]
│   ├── [[ANALYZE]]
│   ├── [[QUESTION]]
│   ├── [[CONNECT]]
│   ├── [[VERIFY]]
│   ├── [[SYNTHESIZE]]
│   └── [[TEACH]]
│
├── [[COMPREHENSION]]
│   ├── [[RECALL]]
│   ├── [[RECOGNITION]]
│   ├── [[EXPLANATION]]
│   ├── [[APPLICATION]]
│   ├── [[ANALYSIS]]
│   ├── [[SYNTHESIS]]
│   └── [[TRANSFER]]
│
├── [[ULTRATHINKING]]
│   ├── [[SLOW_DOWN]]
│   ├── [[DECOMPOSE]]
│   ├── [[QUESTION_ASSUMPTIONS]]
│   ├── [[MULTI_PERSPECTIVE]]
│   ├── [[CONNECT]]
│   ├── [[TEST]]
│   ├── [[INVERT]]
│   ├── [[SIMULATE]]
│   ├── [[SYNTHESIZE]]
│   └── [[REFLECT]]
│
└── [[META_COGNITION]]
    ├── [[WHAT_DO_I_KNOW]]
    ├── [[HOW_DO_I_KNOW]]
    ├── [[WHAT_AM_I_MISSING]]
    ├── [[WHAT_AM_I_ASSUMING]]
    ├── [[WHAT_CHANGED]]
    ├── [[WHAT_CONNECTS]]
    └── [[WHAT_SHOULD_I_REVISE]]
```

## The most important idea: `[[COGNITIVE_ORDER]]`

Your files should have **two orders**:

### Physical order

Where the file sits:

```text
/KNOWLEDGE/THINKING/SYSTEMS_THINKING.md
```

### Cognitive order

When it should be understood:

```text
[[PREREQUISITE]]
      ↓
[[FOUNDATION]]
      ↓
[[CONCEPT]]
      ↓
[[RELATIONSHIP]]
      ↓
[[MECHANISM]]
      ↓
[[APPLICATION]]
      ↓
[[SYNTHESIS]]
```

Those are **not necessarily the same thing**.

---

# The awareness ladder

I'd explicitly add this to the Company Brain:

```text
[[UNSEEN]]
   ↓
[[OBSERVED]]
   ↓
[[RECOGNIZED]]
   ↓
[[DISTINGUISHED]]
   ↓
[[CONNECTED]]
   ↓
[[UNDERSTOOD]]
   ↓
[[EXPLAINED]]
   ↓
[[MODELED]]
   ↓
[[PREDICTED]]
   ↓
[[APPLIED]]
   ↓
[[VERIFIED]]
   ↓
[[INTEGRATED]]
   ↓
[[TEACHABLE]]
   ↓
[[GENERATIVE]]
```

This is much more useful than simply saying:

> "I read the document."

Because **reading is an event; understanding is a state**.

---

# Reading should generate questions

A sophisticated reading system shouldn't simply consume:

```text
DOCUMENT → SUMMARY
```

It should do:

```text
DOCUMENT
   ↓
[[OBSERVE]]
   ↓
[[IDENTIFY_CONCEPTS]]
   ↓
[[UNKNOWN]]
   ↓
[[QUESTIONS]]
   ↓
[[RESEARCH]]
   ↓
[[CONNECT]]
   ↓
[[VERIFY]]
   ↓
[[UNDERSTAND]]
   ↓
[[UPDATE_KNOWLEDGE_GRAPH]]
```

That connects directly to your existing:

`[[QUESTION_MASTER_ONTOLOGY]]`

and:

`[[KNOWLEDGE_GRAPH]]`

---

# Reading order can be generated automatically

This is where it becomes powerful for your bracketed Markdown architecture.

Every document can declare:

```yaml
---
type: knowledge
cognitive_level: mechanism
prerequisites:
  - "[[SYSTEMS_THINKING]]"
  - "[[FIRST_PRINCIPLES]]"
requires:
  - "[[SYSTEM]]"
  - "[[CAUSALITY]]"
introduces:
  - "[[FEEDBACK_LOOPS]]"
  - "[[SYSTEM_DYNAMICS]]"
deepens:
  - "[[CYBERNETICS]]"
next:
  - "[[CONTROL_THEORY]]"
---
```

Now your system can construct a **reading DAG**:

```text
WHOAMI
   ↓
WORLD MODEL
   ↓
ONTOLOGY
   ↓
SYSTEMS
   ↓
DATA
   ↓
KNOWLEDGE
   ↓
REASONING
   ↓
THINKING
   ↓
DECISION
   ↓
ORCHESTRATION
   ↓
AGENTS
   ↓
EXECUTION
   ↓
FEEDBACK
   ↓
LEARNING
   ↓
AUTONOMY
```

Rather than:

```text
"Here are 900 Markdown files. Good luck."
```

---

# And this is where "ultrathinking" should live

I would **not** define ultrathinking as simply "thinking harder."

Define it as a **deliberate depth protocol**:

```text
[[ULTRATHINKING]]

[1. ORIENT]
      ↓
What am I looking at?

[2. DEFINE]
      ↓
What exactly does each concept mean?

[3. DECOMPOSE]
      ↓
What are its constituent parts?

[4. QUESTION]
      ↓
What assumptions are present?

[5. CONNECT]
      ↓
What does this connect to?

[6. CONTRAST]
      ↓
What is it NOT?

[7. CAUSALIZE]
      ↓
What causes what?

[8. INVERT]
      ↓
How could the model fail?

[9. SIMULATE]
      ↓
What happens if conditions change?

[10. VERIFY]
      ↓
What evidence supports this?

[11. SYNTHESIZE]
      ↓
What larger pattern emerges?

[12. REFLECT]
      ↓
What did I previously misunderstand?

[13. UPDATE]
      ↓
What knowledge should change?

[14. GENERATE]
      ↓
What new questions become possible?
```

That last step is important.

**Deep understanding should produce better questions.**

---

# Recursive reading

Your system can therefore operate like:

```text
READ
 ↓
UNDERSTAND
 ↓
CONNECT
 ↓
QUESTION
 ↓
RESEARCH
 ↓
VERIFY
 ↓
SYNTHESIZE
 ↓
UPDATE GRAPH
 ↓
READ NEW DEPENDENCY
 ↓
DEEPER UNDERSTANDING
 ↺
```

This creates **recursive intelligence** rather than linear document consumption.

---

# The ultimate distinction

I'd put this directly into `REALITY.md` / `KNOWLEDGE.md`:

```text
[[READ]]
    ≠
[[UNDERSTOOD]]

[[UNDERSTOOD]]
    ≠
[[VERIFIED]]

[[VERIFIED]]
    ≠
[[INTEGRATED]]

[[INTEGRATED]]
    ≠
[[MASTERED]]

[[MASTERED]]
    ≠
[[GENERATIVE]]
```

And:

```text
[[KNOWLEDGE]]
→ [[RELATIONSHIPS]]
→ [[MODELS]]
→ [[REASONING]]
→ [[APPLICATION]]
→ [[FEEDBACK]]
→ [[LEARNING]]
→ [NEW KNOWLEDGE]
```

So yes — **reading order, cognitive prerequisites, awareness levels, comprehension states, recursive questioning, and ultrathinking should absolutely become first-class nodes in your Company Brain ontology.**

The bigger architecture becomes:

**`[[READING_ORDER]] → [[AWARENESS]] → [[UNDERSTANDING]] → [[THINKING]] → [[REASONING]] → [[QUESTION]] → [[EVIDENCE]] → [[VERIFICATION]] → [[KNOWLEDGE]] → [[DECISION]] → [[ACTION]] → [[LEARNING]]`**

That gives your Markdown/Wiki-link system not merely a **map of knowledge**, but a **path through knowledge**.


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
