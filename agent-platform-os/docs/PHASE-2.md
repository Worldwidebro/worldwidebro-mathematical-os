---
name: agent-platform-os/docs/PHASE-2
title: Agent Platform OS — Phase 2 Documentation
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Platform OS — Phase 2 Documentation

**Status:** Ready for Round 3 integration  
**Generated:** 2026-07-29  
**Tags:** [infrastructure, phase-2, agent-dispatch]

---

## Overview

Agent Platform OS is a lightweight, minimal infrastructure for:
1. **Agent Registry** — In-memory store of agent metadata (capabilities, cost, availability)
2. **Dispatch Engine** — Route tasks to best agent using capability + load + cost scoring
3. **Task Queue** — Async task scheduling with priority ordering and retry logic (max 3 retries)
4. **WebSocket Event Bus** — Real-time status broadcasts (agent events, task events, queue stats)

All components are currently in-memory. **Round 3** wires Supabase storage, vex-hero-site dashboard subscription, and feedback loop integration.

---

## Architecture

```
Task Enqueue
     ↓
[TaskQueue] ← Sorted by: priority → deadline → cost
     ↓
Dequeue → [TaskDispatcher]
              ↓
              Score candidates (capability 50% + availability 30% + cost 20%)
              ↓
              Select best agent
              ↓
          Log [DispatchDecision] → WebSocket broadcast
              ↓
          [WebSocketEventBus] → Dashboard subscribers
              ↓
          Agent executes task
              ↓
          mark_completed() or mark_failed()
              ↓
          Retry if needed (< 3 attempts)
```

---

## Component Details

### 1. AgentRegistry (`agent-registry/registry.ts`)

**Purpose:** Store and query agent metadata.

**Interface:**
```typescript
interface AgentMetadata {
  id: string;                    // e.g., "OPCO_001_Agent"
  name: string;                  // display name
  capabilities: string[];        // e.g., ["deployment_approval", "roi_tracking"]
  cost_per_hour: number;         // $0.03 for Haiku
  available: boolean;            // current availability
  last_heartbeat: Date;          // last seen timestamp
  max_concurrent_tasks: number;  // capacity limit
  opco?: string;                 // optional OPCO reference
}
```

**Key Methods:**
- `register_agent(metadata)` — Add or update agent
- `list_agents(available_only?)` — Get all agents
- `get_agent(id)` — Get agent by ID
- `update_availability(id, available)` — Update status + heartbeat
- `has_capability(id, capability)` — Check agent capability
- `agents_with_capability(capability)` — Find agents with specific capability
- `get_agent_load(id)` — Estimate agent load (30% baseline if available, 100% if not)

**Storage (Round 3):** Supabase `agents` table

---

### 2. TaskDispatcher (`dispatch-engine/dispatcher.ts`)

**Purpose:** Route tasks to best-fit agent.

**Dispatch Algorithm:**
```
Score = 0.5 × capability_score + 0.3 × availability_score + 0.2 × cost_score

capability_score:   % of required capabilities agent has (0–100)
availability_score: 100 - agent_load% (0–100)
cost_score:         Inverse of estimated cost; logarithmic decay (0–100)
```

**Task Interface:**
```typescript
interface Task {
  id: string;                       // unique task ID
  priority: 'critical'|'high'|'normal'|'low';
  required_capabilities: string[];  // capabilities needed
  deadline?: Date;                  // optional deadline
  estimated_cost_hours: number;     // estimated hours to completion
}
```

**Dispatch Decision:**
```typescript
interface DispatchDecision {
  task_id: string;
  agent_id: string;
  agent_name: string;
  reason: string;  // e.g., "Score 87.50: capability_match 100.00 + availability 70.00 + cost_efficiency 50.00"
  score: number;   // 0–100
  timestamp: Date;
}
```

**Key Methods:**
- `dispatch(task)` → `DispatchDecision | null` — Route task; return best agent or null if no match
- `get_decisions()` — Audit trail of all dispatch decisions
- `get_task_decisions(task_id)` — Decisions for a specific task

**Storage (Round 3):** Supabase `capital_decisions` table (dispatch decisions logged here)

---

### 3. TaskQueue (`task-queue/queue.ts`)

**Purpose:** Async scheduling with priority ordering and retry logic.

**Queued Task:**
```typescript
interface QueuedTask {
  id: string;
  task: Task;                   // full task object
  state: 'pending'|'in_progress'|'completed'|'failed';
  dispatch_decision?: DispatchDecision;
  retry_count: number;          // 0–3
  max_retries: number;          // default 3
  created_at: Date;
  started_at?: Date;
  completed_at?: Date;
  error?: string;               // e.g., "agent_timeout"
}
```

**Priority Ordering:**
1. **Priority:** critical → high → normal → low
2. **Deadline:** earliest first (or `Infinity` if no deadline)
3. **Cost:** lowest cost first

**Key Methods:**
- `enqueue(task, max_retries?)` → `QueuedTask` — Add task to queue
- `dequeue()` → `QueuedTask | null` — Next task by priority + deadline + cost
- `mark_completed(task_id)` → `QueuedTask | null` — Task succeeded; reset retry count
- `mark_failed(task_id, error)` → `QueuedTask | null` — Task failed; requeue or mark failed if max retries exceeded
- `get_task(task_id)` — Get task state by ID
- `get_tasks_by_state(state)` — Get all tasks in a state
- `stats()` — Queue statistics: total, pending, in_progress, completed, failed
- `retry_failed()` → `number` — Manual retry all failed tasks; return count

**Retry Logic:**
- Exponential backoff not yet implemented (queued for Round 3); retries happen immediately
- Max 3 retries by default
- On final failure, state → `failed`; task stays in queue for audit

**Storage (Round 3):** Supabase `task_queue` table

---

### 4. WebSocketEventBus (`websocket-handlers/handlers.ts`)

**Purpose:** Real-time status broadcasts for dashboard + monitoring.

**WebSocket Event:**
```typescript
interface WebSocketEvent {
  event: string;                // event type
  agent_id?: string;            // agent involved
  task_id?: string;             // task involved
  timestamp: Date;              // when it happened
  status?: string;              // current status
  payload?: Record<string, any>;// event-specific data
}
```

**Events:**
| Event | Payload | Usage |
|-------|---------|-------|
| `agent_online` | `{ agent_name }` | Agent heartbeat received |
| `agent_offline` | `{ agent_name }` | Agent missed heartbeat deadline |
| `task_dispatched` | `{ agent_name, dispatch_score }` | Task routed to agent |
| `task_completed` | `{ duration_ms }` | Task finished successfully |
| `task_failed` | `{ error, retry_count, max_retries }` | Task failed; retrying if < max |
| `agent_availability_changed` | `{ agent_name, available }` | Availability status changed |
| `queue_stats_update` | `{ total, pending, in_progress, completed, failed }` | Periodic stats (every 5s) |

**Key Methods:**
- `subscribe(callback)` → `() => void` — Subscribe to all events; returns unsubscribe function
- `emit_agent_online(agent_id, agent_name)` — Agent came online
- `emit_agent_offline(agent_id, agent_name)` — Agent went offline
- `emit_task_dispatched(task_id, agent_id, agent_name, dispatch_score)` — Task routed
- `emit_task_completed(task_id, agent_id, duration_ms)` — Task succeeded
- `emit_task_failed(task_id, agent_id, error, retry_count, max_retries)` — Task failed
- `emit_agent_availability_changed(agent_id, agent_name, available)` — Availability changed
- `emit_queue_stats_update()` — Broadcast queue stats
- `get_subscriber_count()` → `number` — Monitoring: how many subscribers

**Stats Broadcaster:**
```typescript
setup_stats_broadcaster(bus, interval_ms?) → () => void
```
Periodically broadcasts queue stats every 5 seconds (or custom interval). Returns unsubscribe function.

**Storage (Round 3):** WebSocket connections to vex-hero-site dashboard

---

## Integration Points

### Current (Phase 2)

1. **AgentRegistry** reads from `family-office-os/AGENTS.md` (manual bootstrap)
2. **TaskDispatcher** uses `AgentRegistry` to find + score agents
3. **TaskQueue** calls `TaskDispatcher.dispatch()` on dequeue
4. **WebSocketEventBus** broadcasts to in-memory subscribers

### Round 3

1. **Supabase**
   - `agents` table: Live agent registry (replaces in-memory)
   - `capital_decisions` table: Dispatch decisions audit trail
   - `task_queue` table: Queue state persistence
   - Triggers: Auto-update `agents.last_heartbeat` on heartbeat webhook

2. **vex-hero-site Dashboard**
   - Subscribes to WebSocket events
   - Real-time agent status panel
   - Task queue visualization
   - Dispatch decision audit trail

3. **Feedback Loop**
   - `01_loop_feedback_collector.py` reads completed tasks from WebSocket
   - Logs ROI, cost, duration for OPCO agent scoring
   - Feeds back to `capital_decisions` → agent learning

---

## Usage Example

```typescript
import { AgentRegistry } from './agent-registry/registry';
import { TaskDispatcher } from './dispatch-engine/dispatcher';
import { TaskQueue } from './task-queue/queue';
import { WebSocketEventBus, setup_stats_broadcaster } from './websocket-handlers/handlers';

// 1. Initialize
const registry = new AgentRegistry();
const dispatcher = new TaskDispatcher(registry);
const queue = new TaskQueue(dispatcher);
const bus = new WebSocketEventBus(registry, queue, dispatcher);

// 2. Register agents (bootstrapped from family-office-os)
registry.register_agent({
  id: 'OPCO_001_Agent',
  name: 'OPCO_001_Agent',
  capabilities: ['deployment_approval', 'roi_tracking'],
  cost_per_hour: 0.03,
  available: true,
  last_heartbeat: new Date(),
  max_concurrent_tasks: 5,
  opco: 'OPCO_001',
});

// 3. Subscribe to events
bus.subscribe((event) => {
  console.log(`[Dashboard] ${event.event} at ${event.timestamp}`);
});

// 4. Start stats broadcaster
const stop_broadcaster = setup_stats_broadcaster(bus, 5000);

// 5. Enqueue a task
const task = queue.enqueue({
  id: 'task-001',
  priority: 'high',
  required_capabilities: ['deployment_approval'],
  estimated_cost_hours: 0.5,
});

// 6. Process tasks
const next = queue.dequeue();
if (next && next.dispatch_decision) {
  bus.emit_task_dispatched(
    next.task.id,
    next.dispatch_decision.agent_id,
    next.dispatch_decision.agent_name,
    next.dispatch_decision.score
  );
  // → Agent processes task
  queue.mark_completed(next.task.id);
  bus.emit_task_completed(next.task.id, next.dispatch_decision.agent_id, 500);
}

// 7. Monitor
console.log(queue.stats()); // { total: 1, pending: 0, in_progress: 0, completed: 1, failed: 0 }

// 8. Stop broadcaster when done
stop_broadcaster();
```

---

## Constraints & Limitations (Round 2)

1. **In-memory only** — No persistence on restart
2. **No exponential backoff** — Retries happen immediately (upgrade path: exponential delays if queue congestion observed)
3. **Naive load estimation** — 30% baseline for available agents (upgrade path: per-agent task counter)
4. **No task isolation** — All tasks share global queue; no per-agent queues (upgrade path: if dispatch becomes contention hotspot)
5. **No dashboard yet** — WebSocket events go to subscribers, but no browser UI (built in Round 3)

---

## Testing

Basic smoke tests for dispatch correctness:

```typescript
// Test: Highest-capability agent wins
const task = { id: 'test-1', priority: 'normal', required_capabilities: ['roi_tracking'], estimated_cost_hours: 1 };
const decision = dispatcher.dispatch(task);
assert(decision?.agent_id === 'OPCO_001_Agent', 'Wrong agent selected');
assert(decision.score >= 70, 'Score too low for perfect match');

// Test: Queue priority ordering
queue.enqueue({ ...task, priority: 'low', id: 'low-1' });
queue.enqueue({ ...task, priority: 'critical', id: 'crit-1' });
const first = queue.dequeue();
assert(first?.id === 'crit-1', 'Priority not respected');

// Test: Retry on failure
queue.enqueue(task);
queue.mark_failed(task.id, 'test error');
assert(queue.get_task(task.id)?.state === 'pending', 'Failed task not requeued');
```

---

## References

- **family-office-os/AGENTS.md** — Agent bootstrap configuration (manual read in Round 2; Supabase sync in Round 3)
- **01_loop_feedback_collector.py** — Feedback loop; consumes completed tasks
- **vex-hero-site** — Dashboard consumer (Round 3)
- **Supabase** — Live storage backend (Round 3)

---

**Next Steps (Round 3):**
1. Supabase schema + integration
2. vex-hero-site WebSocket subscription
3. Feedback loop wiring
4. Exponential backoff retry logic
5. Per-agent task counter load estimation
