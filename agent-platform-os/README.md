# Agent Platform OS

Agent dispatch engine for task routing, queue management, and real-time coordination (Phase 2).

Tags: [infrastructure, phase-2, agent-dispatch]

## Project Structure

- **agent-registry/** — Agent catalog + capabilities metadata
- **dispatch-engine/** — Task routing and priority queue logic
- **task-queue/** — Async scheduling, retries, and state persistence
- **websocket-handlers/** — Real-time agent status updates and coordination
- **docs/** — Architecture and API documentation
- **tests/** — Test suite
- **.github/workflows/** — CI/CD pipelines

## Workspaces

This is a monorepo using npm workspaces. All packages are defined in `package.json` and linked locally.

```bash
npm install
npm test
```

## Status

Phase 2 — Initial scaffold (folders and configuration only). Implementation pending.
