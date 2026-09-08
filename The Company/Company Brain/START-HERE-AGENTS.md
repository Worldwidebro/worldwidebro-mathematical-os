[[STARTHERE]] | [[REALITY]] | [[00_RESPECT/RESPECT|RESPECT]] | [[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|PROMPTS]] | [[16-AGENTS]] | [[INDEX]]

# AI Agents, Swarms & Model Orchestration

> **Canonical Guide ID:** `GUIDE-AGT-001`  
> **Master Legend:** [[STARTHERE]]  
> **Authority:** Agent Control Plane (CP-006) & Model Control Plane (CP-007)  
> **Status:** ACTIVE ORIENTATION — Updated 2026-09-06

## Purpose
Coordinates the agent personas, prompt stacks, memory architecture, ethical respect boundaries, and multi-model routing across Antigravity IDE and OmniRoute.

## Cognitive & Governance Contracts
- **Universal Agent Operating Contract:** [[AGENTS|AGENTS.md]]
- **Master Orchestration Contract:** [[ANTIGRAVITY|ANTIGRAVITY.md]] (45 Non-Negotiable Operating Rules)
- **Respect Control Layer:** [[00_RESPECT/RESPECT|RESPECT.md]] & [[00_RESPECT/RESPECT-OS|RESPECT-OS.md]] (20 Core Rules, Boundaries, Agency)
- **Memory Operating System:** [[_MEMORY/MEMORY-OS|MEMORY-OS.md]] (Working, Episodic, Semantic, Procedural)
- **Operational Prompt Stack:** [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS.md]] (The Always-On 20-Point Protocol)

## Model Routing & MCP Integration
- **OmniRoute Gateway:** Running on port `:20128` (`http://localhost:20128`), coordinating cloud models (Claude, GPT, Gemini) and local models.
- **FastMCP Adapter:** `/Users/acebless/.omniroute/bin/antigravity-mcp.mjs` exposing 110 OmniRoute tools directly to Antigravity agents.
- **Global Antigravity Skill:** `.gemini/config/skills/omniroute/SKILL.md`
- **Native MLX Model Node:** `mlx-community/Qwen3.6-35B-A3B-5bit` on port `:52415`.
- **Local Ollama Inference:** `qwen2.5-coder:14b`, `llama3.1:8b`, `hermes3:latest` on port `:11434`.

## Subagent Fleet & Personas
- **Domain Subagents:** Defined in `.agents/agents/` (e.g. `@architect`, `@qa`, `@security`).
- **Agents by Sector Registry:** [[_REGISTRIES/agents-by-sector.yaml]]

## Operational Rules for Agents
1. **Always-On Protocol:** Execute [[_PROMPTS/10_PRE-ACTION-AWARENESS]] prior to any modifying action.
2. **Respect Boundaries:** Comply with [[00_RESPECT/RESPECT-BOUNDARIES]] and [[00_RESPECT/RESPECT-AGENCY]].
3. **No Simulated Completion:** Never report "Done" without verified terminal proof (`ANTIGRAVITY.md` Rule #3).
