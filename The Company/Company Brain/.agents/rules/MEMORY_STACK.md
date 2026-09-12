# AGENT MEMORY & AWARENESS STACK

> **Scope:** 20-Prompt Architecture for Agent Memory and Continuity
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

Modern agent-memory architectures separate working, episodic, semantic, and procedural memory. This stack ensures continuity, connection, awareness, retrieval, consolidation, and self-correction.

## The 20-Prompt Framework

1. **Identity Awareness**: Who am I, what system am I operating within, and what is my role?
2. **Current-State Awareness**: What is happening right now?
3. **Historical Context**: What has happened previously in this context?
4. **Goal Alignment**: Does the current action align with the master goals?
5. **Procedural Memory Retrieval**: How do I perform this specific task based on past experiences?
6. **Semantic Memory Retrieval**: What are the canonical definitions and facts related to this topic?
7. **Episodic Memory Retrieval**: What were the exact events of the last similar execution?
8. **Dependency Mapping**: What other systems or artifacts are affected by this action?
9. **Constraint Checking**: What are the limits and rules I must follow here?
10. **Validation Strategy**: How will I prove this action was successful?
11. **Execution Phase**: (The actual generation/action)
12. **Self-Correction Check**: Did the execution meet the constraints and goals?
13. **Error Handling**: If a failure occurred, what is the recovery path?
14. **State Transition**: How do I update the system state post-execution?
15. **Consolidation Trigger**: What new knowledge needs to be saved to semantic/procedural memory?
16. **Graph Association**: How does this new information link to existing nodes in the knowledge graph?
17. **Pruning Strategy**: What temporary or outdated context can be discarded?
18. **User Communication**: What does the user need to know about this action?
19. **Next-Action Prediction**: What is the logical next step for the user or system?
20. **Sleep/Idle State Prep**: How do I safely suspend state until the next activation?

## Implementation

This stack should be loaded into the agent's context during initialization and referenced at each step of the OODA loop (Observe, Orient, Decide, Act).

[[STARTHERE]] | [[ANTIGRAVITY]] | [[CLAUDE]]
