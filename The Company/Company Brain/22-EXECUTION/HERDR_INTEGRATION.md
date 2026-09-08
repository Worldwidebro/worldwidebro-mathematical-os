# herdr Integration (TOL-000003)

**Status:** ✅ Registered  
**Version:** Current  
**Company Brain Base:** 22-EXECUTION, 49-SYSTEM  
**Related:** [[EXECUTION_STACK]] | [[GRAFT_INTEGRATION]] | [[FRACTAL_INTEGRATION]]

---

## What herdr Does

Persistent agent runtime. Owns terminal sessions/workspaces where agents execute.

**Key feature:** Agents don't lose state if connection drops.

```
Before herdr:
Agent starts → "SSH connection lost" → All work lost → Restart

With herdr:
Agent starts → "SSH connection lost" → Reconnect → Continue working
```

---

## Capabilities

- Persistent terminal sessions
- Terminal pane management
- Session reattachment (e.g., `herdr attach agent-001`)
- Agent-to-agent interaction (tmux escape sequences)
- Runtime visibility (which agent is blocked?)
- Status tracking (working/blocked/idle)

---

## Relationship to Other Systems

**NOT** the same as:
- **Fractal** — herdr doesn't create hierarchy. Fractal does.
- **Graft** — herdr doesn't understand code. Graft does.
- **Loop Engine** — herdr doesn't discover work. Loop Engine does.

**IS:**
- Where agents literally run
- Terminal ownership
- Session persistence
- Runtime substrate

---

## Architecture Position

```
Fractal (WHO/HOW: agent hierarchy)
    │
herdr (WHERE: persistent runtime)
    │
Claude / Codex / Agents (WHAT: reasoning)
```

---

## Object Types Involved

- RUNTIME — herdr instance
- RUNTIME_SESSION — persistent session
- RUNTIME_PANE — terminal pane within session
- PROCESS — running subprocess

---

## Key Relationships

```
AGENT RUNS_IN RUNTIME       (which runtime owns this agent)
RUNTIME HOSTS AGENT_RUN     (which runs are executing)
RUNTIME_SESSION PERSISTS    (survives disconnect)
RUNTIME_SESSION REATTACHABLE (can reconnect)
```

---

## Setup

```bash
herdr server &
herdr create-session my-agent
herdr attach my-agent
```

---

## Deployment Checklist

- [ ] herdr installed
- [ ] Server running as background service
- [ ] Sessions persist across SSH disconnect
- [ ] Reattachment works
- [ ] Pane management works
- [ ] Agent visibility in `herdr status`
- [ ] Cost/resource tracking operational

---

**See also:** [[EXECUTION_STACK]] | [[FRACTAL_INTEGRATION]] | [[22-EXECUTION]]
