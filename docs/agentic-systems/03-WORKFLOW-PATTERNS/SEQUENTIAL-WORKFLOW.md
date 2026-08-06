---
name: docs/agentic-systems/03-WORKFLOW-PATTERNS/SEQUENTIAL-WORKFLOW
desc: ...
tags:
  - status/active
  - knowledge/current
id: sequential-workflow
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/03-WORKFLOW-PATTERNS/SEQUENTIAL-WORKFLOW
## Purpose
Detail the sequential workflow pattern where outputs of one step feed directly into the next.

## Core Concept
`Node A -> Node B -> Node C`
A linear pipe where data is refined incrementally, reducing LLM context overhead by scoping each node to a single transformation.

## Technical Details
Ideal for pipeline operations:
1. **Step 1 (Ingest)**: Extract text from PDF.
2. **Step 2 (Analyze)**: Identify compliance violations.
3. **Step 3 (Format)**: Output compliance report.
If Step 2 fails, the system retries Step 2 without needing to repeat the ingestion phase.

## Relations
- Under [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
- Next: [[03-WORKFLOW-PATTERNS/PARALLEL-WORKFLOW.md]]
