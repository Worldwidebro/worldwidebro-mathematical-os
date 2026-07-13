---
status: complete
---

# Quick Task 260712-nbx: Clean up confirmed-dead orphaned tables — Summary

**Completed:** 2026-07-13
**Executor note:** The original executor agent hit a session API limit mid-run after completing all 3 planned tasks and writing AUDIT-RESULT.md, but before writing this SUMMARY.md or its final commit. The orchestrator (this session) independently re-verified the live database state before closing out the task, rather than trusting the executor's self-report alone.

## What happened

Dropped 20 confirmed-dead tables from the CivilizationOS Supabase project (`cyhzilqldouzgynacqpe`), in 3 clusters:
- `joos_*` (8 tables) — had a design doc, zero implementing code
- `folder_*` + `genius_agents` (5 tables) — tied to an abandoned "101 Genius Folders" concept
- Dead per-venture trackers (7 tables) — `con_001_*`, `fin_001_*`, `mc_001_*` — real ventures, but these specific tracking tables had zero code writing to them

All 20 were re-verified at 0 rows immediately before dropping (race guard), full DDL was captured to `rollback.sql` first, and CASCADE side-effects (5 dependent views, 14 foreign-key constraints on out-of-scope tables) were documented — all confirmed safe since every affected table was independently at 0 rows.

## Deviation from plan

The executor used the Supabase CLI (`supabase db query --linked`) instead of the planned `mcp__claude_ai_Supabase__execute_sql`/`apply_migration` MCP tools, reporting the MCP tools were not exposed in its tool-restricted subagent context. This was not independently verified, but the outcome was verified independently regardless (see below), so the deviation doesn't affect the correctness of the result.

## Independent verification (orchestrator, post-hoc)

Because the executor's report contained an unexplained count discrepancy (266→246 instead of the plan's expected 271→251) and used a fallback tool path, the orchestrator re-verified directly via its own `mcp__claude_ai_Supabase__execute_sql` access before accepting the result:

- `SELECT count(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' AND table_name IN (<20 names>)` → **0** (all 20 confirmed gone)
- `SELECT count(*) FROM pg_stat_user_tables WHERE schemaname='public'` → **251** (exact match to the plan's expected 271 → 251, using the plan's original counting method)

The count discrepancy in the executor's AUDIT-RESULT.md was resolved: it used a different counting method (`information_schema.tables`) than the plan (`pg_stat_user_tables`), which counts 5 fewer relations in this database for unrelated reasons — not data loss, not drift between sessions.

## Artifacts

- Plan: `260712-nbx-PLAN.md`
- Rollback (reversible DDL for all 20 tables): `rollback.sql`
- Full audit trail: `AUDIT-RESULT.md` (corrected with independent verification)
- This summary: `260712-nbx-SUMMARY.md`

## Out of scope (untouched, confirmed)

The other ~128 zero-code-reference empty tables from the original audit (agent_*, crm_*, deal_*, financial_*, equity_cap_table, investor_commitments, limited_partners, general_partners, etc.) were explicitly out of scope for this pass and were not touched. The 197-table RLS-disabled issue found during the original audit is also untouched — separate, undecided issue.
