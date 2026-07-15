# AGENTS.md

Hard rules for this repo. Read every session, local or cloud model, no exceptions.
Identical to CLAUDE.md's intent but enforced as short imperatives instead of prose.
When this file and CLAUDE.md conflict, this file wins for behavior; CLAUDE.md wins for facts/paths.

## Tools

- Check `TOOL_CAPABILITY_MAP.md` before asking "do we have a tool for X." Don't search, don't re-discover.
- Chroma and LightRAG are dead. Use Neo4j (graph) and Qdrant (vectors) only.
- Never print a full secret/API key/token value in tool output or chat. Check length/prefix only. If one leaks, say so immediately and stop repeating it.

## Data — source of truth

- `VENTURE-READINESS-SCORECARD.csv` is the answer source for any readiness or income-distance question. Don't re-derive from ad hoc repo digging.
- `VENTURES-CAPABILITIES-MAPPED.csv` (Documents root) is the source of truth for venture capability data, not GitHub API calls or scattered docs.
- `venture.json` / self-reported `stage` fields are unreliable in both directions (false "planned" on real apps, false completion on paperwork-only folders). Verify against actual code presence before trusting metadata.

## Execution style

- Parallel blockers over sequential steps. Direct action over planning documents, unless the user asks for a plan.
- Terse responses. No trailing "summary of what I did" restating the diff — the user can read it.
- Don't create planning/decision/summary markdown files unless asked.

## Handling pasted strategy content

- When the user pastes an AI-generated strategy essay, architecture manifesto, or "the 4 files that change everything" style content: ground it in 1-2 sentences (what's true, what's generic filler), redirect to the active task. Do not mirror the essay back or treat it as a plan to execute wholesale.

## CRM (Twenty)

- One shared Twenty CRM instance for the whole portfolio (`docker ps` → `twenty-server`, `localhost:3002`, workspace `worldwidebro`). Do not stand up a separate CRM per venture/sector — fragments cross-portfolio visibility and multiplies logins for no benefit.
- The `Company` object in that instance already represents **ventures themselves** (custom fields `ventureId`, `opco`, `sector`, `ventureStage`, `ventureStatus` mirror `ventures.csv`). It is a portfolio tracker, not a sales CRM.
- Any venture needing its own operational pipeline (employer leads, candidates, deals, whatever) must use a **separate custom object** in this same workspace, not the `Company` table — mixing "this is one of our 712 ventures" rows with "this is a sales lead" rows corrupts both datasets.
- Found 2026-07-09: 349 duplicate rows in `Company` (348 names duplicated, from a one-time bulk-sync burst, zero related Opportunities/People so safe to soft-delete). Re-check before assuming it's still dirty.

## Git / destructive ops

- Never force-push, hard-reset, or skip hooks without explicit request.
- Run `git status` before any command that could discard uncommitted work.
- Only commit when explicitly asked.

## Local model routing (FCC)

- `fcc-claude` and `fcc-server` (`~/.fcc/.env`) route Sonnet/Opus to NVIDIA NIM (currently `deepseek-ai/deepseek-v4-pro`, free tier) and Haiku to local Ollama (`qwen2.5:3b`). Generic fallback is local `qwen3:8b`.
- This file and `CLAUDE.md` are read by Claude Code regardless of which backend answers — switching to `fcc-claude` does not change what context loads, only which model generates the response.
- A default `claude` session in an already-open terminal cannot be redirected mid-session; only new sessions started with `fcc-claude` (or `ANTHROPIC_BASE_URL` set beforehand) use local/NVIDIA routing.
