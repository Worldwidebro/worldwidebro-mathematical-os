---
title: Agent Memory Architecture
version: 1.0
date: 2026-07-30
companion: [[AGENT-BRACKET-STANDARD.md]], [[AGENT_SPEC.md]]
---

# Agent Memory Architecture

**Purpose**: 5 memory types enable agents to learn, improve, and share knowledge.

---

## Memory Types

### EPISODIC (What happened)
- Storage: Supabase + Redis
- TTL: 30 days
- Use: Recent decisions, outcomes

### SEMANTIC (What is known)
- Storage: Neo4j
- TTL: Indefinite
- Use: Facts, relationships, patterns

### PROCEDURAL (How to do)
- Storage: Git + PLAYBOOK.md
- TTL: Indefinite
- Use: Workflows, algorithms

### WORKING (Current state)
- Storage: Redis
- TTL: Session duration
- Use: Active task, progress, blockers

### REFLECTIVE (Lessons learned)
- Storage: Supabase learning_log
- TTL: 180 days
- Use: Pattern recognition, confidence

---

## Learning Loop

Execute → Measure → Evaluate → Reflect → Improve → Deploy → Repeat (weekly)

---

## Version History
- **v1.0 (2026-07-30)**: Agent memory architecture.
