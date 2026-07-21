# A2: Hermes Supabase Schema Reconciliation

This document tracks changes to align Hermes queries with the current database schema structure.

## 1. Schema Discrepancy
The local client was querying `public.ventures` whereas the database table schema is mapped under `core.ventures` or `tenant.ventures` dynamically.

## 2. Fix Mappings
Update API router endpoints in `src/lib/supabase.ts`:

```typescript
// Replace:
const { data } = await supabase.from('ventures').select('*');

// With:
const { data } = await supabase.rpc('get_tenant_ventures');
```

## 3. Verification
Ensure that the CEO Dashboard loads the list of active ventures without returning empty arrays or database syntax errors.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Supabase database active with ventures populated; tenant RPC function `get_tenant_ventures` deployed.
    *   **Dependencies:** Blocks Hermes Dashboard visual verification of venture health and MRR.
*   **Verification Gate:**
    *   **Success Criteria:** Running `npm run dev` in the Hermes Next.js repository compiles cleanly and loads the ventures list from the database without crashes.
    *   **Blockers:** CEO dashboard will crash on load with 500 database exceptions when querying outdated schema references.
