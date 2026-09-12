---
id: AGT-HERMES-001
title: Hermes Agent — Autonomous Agent Operating System
aliases: ["Hermes", "Hermes Agent", "hermes-agent", "HERMES"]
tags: [agent, hermes, nous-research, execution, autonomous]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[AGENTS]] | [[START-HERE-AGENTS]] | [[16-AGENTS/README|16-AGENTS]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# Hermes Agent (`NousResearch/hermes-agent`)

**Authority:** CP-006 (Agents) & CP-027 (Infrastructure)  
**Status:** ✅ `LIVE & RUNNING` (Verified local runtime v0.21.0, launchd daemon PID 974)  
**Install Directory:** [`/Users/acebless/.hermes/hermes-agent`](file:///Users/acebless/.hermes/hermes-agent)  
**CLI Binaries:** [`/Users/acebless/.local/bin/hermes`](file:///Users/acebless/.local/bin/hermes), [`/Users/acebless/.local/bin/hermes-acp`](file:///Users/acebless/.local/bin/hermes-acp)

---

## 1. System Overview
Hermes Agent is the autonomous agent framework created by Nous Research. In Company Brain, Hermes serves as a multi-channel autonomous worker capable of executing tasks across Telegram, WhatsApp, Slack, terminal sessions, and background cron schedules.

## 2. Live Runtime & Infrastructure
- **Process Manager:** `launchd` service running `python -m hermes_cli.main gateway run --replace` (PID `974`).
- **MCP Integration:** Active OpenKnowledge MCP watchdog daemon (`tools/mcp_stdio_watchdog.py`, PID `1504`).
- **Primary Model Provider:** Nous Portal (`upstage/solar-pro4:free` via `https://inference-api.nousresearch.com/v1`).
- **Local Inference Fallback 1:** Mac Studio Ollama (`http://100.87.214.70:11434/v1` serving `qwen3:8b` and `hermes3:latest`).
- **Local Inference Fallback 2:** LiteLLM Gateway (`http://localhost:4000/v1` serving `coder`).

## 3. Storage & Capabilities
- **Skills Registry:** 1,964 modular skills loaded in `~/.hermes/skills/`.
- **State & Kanban DBs:** SQLite databases `state.db` (17.9 MB) and `kanban.db` tracking agent memory, sessions, and task boards.
- **Messaging Surfaces:** Active Telegram integration (`8267837521`), WhatsApp, and Slack.

## 4. CLI Commands
```bash
hermes status     # View live gateway status, auth providers, and messaging links
hermes doctor     # Comprehensive diagnostics and health check
hermes chat       # Launch interactive CLI terminal session
```
