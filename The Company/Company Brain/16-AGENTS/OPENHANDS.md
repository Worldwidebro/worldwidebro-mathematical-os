---
id: AGT-OPENHANDS-001
title: OpenHands — Autonomous Software Development Agent
aliases: ["OpenHands", "openhands", "OpenDevin", "OPENHANDS"]
tags: [agent, openhands, software-engineering, autonomous, swe-agent]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[AGENTS]] | [[START-HERE-AGENTS]] | [[16-AGENTS/README|16-AGENTS]] | [[13_ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# OpenHands (`All-Hands-AI/OpenHands`)

**Authority:** CP-006 (Agents) & CP-027 (Infrastructure)  
**Status:** ✅ `INSTALLED & VERIFIED` (CLI v1.16.0, SDK v1.21.0)  
**Binary Location:** [`/Users/acebless/.local/bin/openhands`](file:///Users/acebless/.local/bin/openhands) (also `openhands-acp`)  
**Package Manager:** Managed via `uv tool` (Python 3.12 isolated runtime)

---

## 1. System Overview
OpenHands (formerly OpenDevin) is an open-source autonomous AI software development agent platform. It executes complex multi-file codebase refactoring, feature implementation, and debugging runs inside secure sandboxes.

## 2. Runtime & Execution Architecture
- **CLI Mode:** Command-line agent interface for automated problem solving and PR generation.
- **GUI Server Mode:** Web-based developer dashboard (`openhands serve`) listening on port `3000`.
- **Sandbox Environment:** Integrates with local Docker daemon for containerized code execution, filesystem isolation, and automated testing.
- **Model Connectivity:** Connects directly to OpenAI, Anthropic, or internal Company Brain routing via OmniRoute (`:20128`) and LiteLLM (`:4000`).

## 3. CLI Invocations
```bash
openhands --version          # Verify OpenHands CLI version (1.16.0)
openhands serve              # Launch local web GUI on port 3000
openhands --mount-cwd        # Start session mounting current workspace
```
