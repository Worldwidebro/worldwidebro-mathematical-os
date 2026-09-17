---
title: Autonomous Loop Specification
id: AUTONOMOUS-LOOP-SPEC
phase: Phase 2 (Local Autonomy)
updated: 2026-09-17
---

# Autonomous Loop Specification

**Goal:** Define the exact steps every autonomous agent loop executes.

## Loop Anatomy (7 Steps)

### 1. OBSERVE (5 min heartbeat)
- Poll event queue
- Read current system state
- Check agent health

### 2. UNDERSTAND
- Classify event type (via Model Router)
- Retrieve context from Neo4j
- Load venture/agent/tool registries

### 3. PLAN
- Route task: Local Ollama or Cloud Claude?
- Generate action plan
- Check permissions via Tool Gateway

### 4. EXECUTE
- Call tool via MCP
- Log all inputs/outputs
- Stream status

### 5. VERIFY
- Eval: Did action succeed?
- Compare before/after state
- If failed: retry with alternative tool

### 6. RECORD
- Update system state (Postgres)
- Create event (for next loop)
- Add to audit log (Neo4j)

### 7. LEARN
- Store outcome as Neo4j edge
- Update agent metrics
- Adjust future decisions

## State Model

```yaml
venture_id: VEN-000001
current_gaps:
  - gap_id: GAP-LOOP-001
    status: in_progress
    last_action: 2026-09-17 16:30:00
    iterations: 2
last_successful_action: 2026-09-17 16:25:00
next_scheduled_action: 2026-09-17 17:00:00
metric_delta: +15% revenue (since last cycle)
```

## Heartbeat Schedule

```
Every 1 min    → event monitor
Every 5 min    → operational monitor
Every 15 min   → sales pipeline monitor
Every hour     → agent health check
Every 4 hours  → revenue opportunity scan
Every night    → system reconciliation
Every week     → strategic review
```

