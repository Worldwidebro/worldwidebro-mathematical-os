---
phase: quick-260712-nbx
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql
  - .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/AUDIT-RESULT.md
autonomous: true
requirements: [CLEANUP-01]
must_haves:
  truths:
    - "The 20 confirmed-dead orphaned tables no longer exist in the public schema of Supabase project cyhzilqldouzgynacqpe."
    - "A reversible rollback.sql containing the full CREATE TABLE DDL for all 20 dropped tables exists on disk."
    - "The public schema table count is exactly 251 after the drop (was 271); no other table was touched."
    - "Each of the 20 tables was re-confirmed at 0 live rows immediately before being dropped."
  artifacts:
    - ".planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql"
    - ".planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/AUDIT-RESULT.md"
  key_links:
    - "rollback.sql DDL is captured BEFORE any DROP executes (irreversible-loss guard)."
    - "The 0-row re-verification query runs in the same session, immediately before the DROP calls (race guard)."
    - "DROP scope is limited to the explicit 20-table allowlist — no wildcard/pattern drops against the live DB."
---

<objective>
Drop 20 confirmed-dead, zero-row, zero-code-reference orphaned tables from the CivilizationOS Supabase project (project_id cyhzilqldouzgynacqpe) via the `mcp__claude_ai_Supabase__execute_sql` / `apply_migration` MCP tools, reversibly.

The 20 tables in three clusters:
- joos_* (8): joos_ai_decisions, joos_clients, joos_cost_tracking, joos_job_assignments, joos_job_events, joos_job_stages, joos_jobs, joos_vendors
- folder_* + genius_agents (5): folder_categories, folder_metrics, folder_monetization, folder_value_propositions, genius_agents
- dead per-venture trackers (7): con_001_leads, con_001_outreach, con_001_qualified_leads, fin_001_leads, fin_001_outreach, mc_001_potential_sponsors, mc_001_sponsorships

Purpose: Remove dead schema clutter (audit found 148 zero-code-ref empty tables; these 20 are the confirmed-dead subset) without risking data loss, so the schema reflects only live/intentional structures.
Output: rollback.sql (reversible DDL), the actual DROP executed, and AUDIT-RESULT.md summarizing before/after.
</objective>

<execution_context>
@/Users/acebless/Documents/.claude/gsd-core/workflows/execute-plan.md
@/Users/acebless/Documents/.claude/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/STATE.md

Access model: This plan operates ENTIRELY against a hosted Supabase project via the MCP tools `mcp__claude_ai_Supabase__execute_sql` and `mcp__claude_ai_Supabase__apply_migration` (project_id cyhzilqldouzgynacqpe). There is no local Postgres, no psql, no application source to change. The only local files written are rollback.sql and AUDIT-RESULT.md inside this quick task's own directory.

The 20-table allowlist (use this EXACT set everywhere — never a LIKE/wildcard against the live DB):
joos_ai_decisions, joos_clients, joos_cost_tracking, joos_job_assignments, joos_job_events, joos_job_stages, joos_jobs, joos_vendors, folder_categories, folder_metrics, folder_monetization, folder_value_propositions, genius_agents, con_001_leads, con_001_outreach, con_001_qualified_leads, fin_001_leads, fin_001_outreach, mc_001_potential_sponsors, mc_001_sponsorships
</context>

<tasks>

<task type="auto">
  <name>Task 1: Capture reversible DDL + re-verify 0 rows for all 20 tables</name>
  <files>.planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql</files>
  <action>
Via `mcp__claude_ai_Supabase__execute_sql` against project cyhzilqldouzgynacqpe, run two read-only queries scoped to the 20-table allowlist (pass the list as an explicit IN (...) of the 20 names, schema 'public'):

(1) Row-count re-verification: query pg_stat_user_tables joined to the allowlist returning schemaname, relname, n_live_tup for each of the 20 tables. HARD STOP CONDITION: if any row returns n_live_tup greater than 0, do NOT proceed to Task 2 — record which table(s) gained rows and surface the finding; the audit's confirmed-dead assumption is void for that table. Also confirm the query returns exactly 20 rows (a missing table means it was already dropped — note it and exclude from Task 2).

(2) DDL capture: for each of the 20 tables, reconstruct the full CREATE TABLE statement from pg_catalog / information_schema — column names, data types (format_type on atttypid/atttypmod), NOT NULL, column DEFAULT (pg_get_expr of adbin), plus primary-key / unique / check / foreign-key constraints via pg_get_constraintdef over pg_constraint. Order columns by attnum, exclude dropped/system columns (attnum greater than 0 AND NOT attisdropped).

Assemble the results into rollback.sql: a header comment with project_id, capture timestamp, and the 20-table list; then one `CREATE TABLE IF NOT EXISTS public.<name> (...);` block per table followed by its constraint definitions. Write rollback.sql with the Write tool (this is a LOCAL file — Write is correct here, not the MCP tool). Do not use LIKE/wildcards in any DB query — enumerate the 20 names explicitly.
  </action>
  <verify>
    <automated>test -s .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql && grep -c 'CREATE TABLE IF NOT EXISTS public\.' .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql | grep -qx 20 && echo OK</automated>
  </verify>
  <done>rollback.sql exists and non-empty, contains exactly 20 `CREATE TABLE IF NOT EXISTS public.<name>` blocks with column types/defaults/constraints; the 0-row re-verification returned n_live_tup = 0 for all 20 (or the plan halted with a documented row-gained finding).</done>
</task>

<task type="auto">
  <name>Task 2: Drop the 20 tables, grouped by cluster</name>
  <files>(no local file — remote DB mutation via MCP)</files>
  <action>
Only after Task 1 confirmed rollback.sql holds all 20 DDL blocks AND all 20 tables re-verified at 0 rows. Via `mcp__claude_ai_Supabase__apply_migration` (preferred, so the drop is recorded as a named migration; name it e.g. drop_20_confirmed_dead_orphan_tables), execute the drops grouped by cluster:

Cluster 1 (joos): DROP TABLE IF EXISTS public.joos_ai_decisions, public.joos_clients, public.joos_cost_tracking, public.joos_job_assignments, public.joos_job_events, public.joos_job_stages, public.joos_jobs, public.joos_vendors CASCADE;
Cluster 2 (folder/genius): DROP TABLE IF EXISTS public.folder_categories, public.folder_metrics, public.folder_monetization, public.folder_value_propositions, public.genius_agents CASCADE;
Cluster 3 (dead venture trackers): DROP TABLE IF EXISTS public.con_001_leads, public.con_001_outreach, public.con_001_qualified_leads, public.fin_001_leads, public.fin_001_outreach, public.mc_001_potential_sponsors, public.mc_001_sponsorships CASCADE;

Each DROP names its tables explicitly — never a wildcard. Do NOT touch RLS, any populated table, or any other empty table (agent_*, crm_*, deal_*, financial_*, equity_cap_table, investor_commitments, limited_partners, general_partners are explicitly out of scope). CASCADE is intentional so dependent views/constraints on these dead tables drop cleanly; if CASCADE reports it removed an object owned by a table NOT on the 20-list, capture that in the output for AUDIT-RESULT.md.
  </action>
  <verify>
    <automated>echo "verified in Task 3 via fresh information_schema count"</automated>
  </verify>
  <done>All three DROP statements executed successfully via the MCP tool; migration recorded; any CASCADE side-effects on non-listed objects captured.</done>
</task>

<task type="auto">
  <name>Task 3: Post-drop verification + AUDIT-RESULT.md</name>
  <files>.planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/AUDIT-RESULT.md</files>
  <action>
Via `mcp__claude_ai_Supabase__execute_sql`, run a fresh verification against project cyhzilqldouzgynacqpe:

(1) Confirm absence: query information_schema.tables WHERE table_schema='public' AND table_name IN (the 20 names) — MUST return 0 rows.
(2) Confirm total: SELECT count(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' — MUST equal 251 (was 271, minus 20). If the count differs, investigate and report the discrepancy rather than declaring success.

Write AUDIT-RESULT.md with the Write tool summarizing: the 20 tables dropped (grouped by the 3 clusters), the pre-drop 0-row re-verification result, the rollback file location (absolute path .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/rollback.sql), before count (271), after count (251), any CASCADE side-effects, and a one-line rollback instruction (re-run rollback.sql via the Supabase MCP to recreate the empty structures). Note explicitly that RLS and all out-of-scope tables were untouched.
  </action>
  <verify>
    <automated>test -s .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/AUDIT-RESULT.md && grep -q 251 .planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/AUDIT-RESULT.md && echo OK</automated>
  </verify>
  <done>information_schema shows 0 of the 20 tables remain and public base-table count = 251; AUDIT-RESULT.md documents dropped tables, rollback path, and before/after counts (271 → 251).</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| planner/executor → hosted Supabase (cyhzilqldouzgynacqpe) | Destructive DDL (DROP TABLE CASCADE) crosses into production data store via MCP write access |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-nbx-01 | Denial of Service (data loss) | DROP TABLE on live DB | high | mitigate | Task 1 captures full CREATE TABLE DDL to rollback.sql BEFORE any drop; drops are IF EXISTS and reversible from that file |
| T-nbx-02 | Tampering (race) | table gains rows between audit and drop | high | mitigate | Task 1 re-verifies n_live_tup=0 in the same session immediately before Task 2; hard stop if any table is non-empty |
| T-nbx-03 | Elevation (scope-creep) | wildcard drop hits out-of-scope tables | high | mitigate | Every DROP enumerates the exact 20 names; no LIKE/pattern against live DB; Task 3 asserts exactly 251 tables remain |
| T-nbx-04 | Repudiation | untraceable schema change | low | mitigate | Drops applied via apply_migration (named migration recorded); AUDIT-RESULT.md documents what/when/rollback |
</threat_model>

<verification>
- rollback.sql contains 20 CREATE TABLE blocks with types/defaults/constraints.
- Pre-drop: all 20 tables re-verified at 0 rows (else halt).
- Post-drop: information_schema returns 0 of the 20 names; public base-table count = 251.
- No RLS change; no out-of-scope or populated table touched.
- AUDIT-RESULT.md records dropped tables, rollback path, before/after counts.
</verification>

<success_criteria>
The 20 confirmed-dead orphaned tables are gone from project cyhzilqldouzgynacqpe, the change is reversible via rollback.sql, the public schema holds exactly 251 base tables, and AUDIT-RESULT.md documents the operation.
</success_criteria>

<output>
Create `.planning/quick/260712-nbx-clean-up-confirmed-dead-orphaned-tables-/260712-nbx-SUMMARY.md` when done
</output>
