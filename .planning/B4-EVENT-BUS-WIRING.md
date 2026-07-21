# B4: Redis Event Bus Wiring Guide

Explains step-by-step setup to route events across active agent runtimes.

## 1. Setup Redis Connection
Initialize connection in your script:

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

## 2. Publish Events
```python
r.publish('agent_channel', '{"event": "VENTURE_LAUNCHED", "id": "CON-001"}')
```

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Redis service active; B2 and B3A operational.
    *   **Dependencies:** Blocks n8n event workflows (D1) and real-time agent coordination.
*   **Verification Gate:**
    *   **Success Criteria:** Running a subscriber captures a published `VENTURE_LAUNCHED` event in under 100ms.
    *   **Blockers:** Agents must poll database tables continuously, causing high API costs and latency.
