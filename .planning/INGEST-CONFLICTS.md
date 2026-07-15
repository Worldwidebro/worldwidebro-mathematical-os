## Conflict Detection Report

### BLOCKERS (0)

None.

Cross-reference cycle detection was re-run (this is a re-run after a prior BLOCKER) and the previously reported 2-node cycle is confirmed resolved — see INFO below for details. No LOCKED ADR contradictions exist (0 ADRs in this batch). No UNKNOWN-confidence-low classifications exist (all 8 docs classified high-confidence). MODE=new, so no existing-CONTEXT.md-locked-decision check applies.

### WARNINGS (1)

[WARNING] SPEC-precedence Governance Charter sourced from a `_superseded` path
  Found: `GOVERNANCE-CHARTER.md` (classified as SPEC, precedence 2, feeding constraints.md) lives at `/Users/acebless/Documents/WORLDWIDEBRO-OS/02-GOVERNANCE/holdings/_superseded/Worldwidebro-Holdings/GOVERNANCE-CHARTER.md` — the `_superseded/` segment is the user's own archival convention. A second reference to a `GOVERNANCE-CHARTER.md` exists at `/Users/acebless/Documents/Worldwidebro-Holdings/GOVERNANCE-CHARTER.md` (cited as required reading by README-START-HERE.md, a non-superseded, actively-maintained folder), but that copy was not part of this ingest and was not classified.
  Impact: if the non-superseded copy differs from the ingested one, downstream synthesis (constraints.md, and anything gsd-roadmapper derives from it) will enshrine potentially-stale governance rules as authoritative without the user knowing a newer version exists.
  → Confirm whether `/Users/acebless/Documents/Worldwidebro-Holdings/GOVERNANCE-CHARTER.md` is the live canonical charter; if so, re-ingest it (with precedence set appropriately) before routing, or explicitly confirm the `_superseded` copy is intentionally still canonical.

### INFO (3)

[INFO] Cross-reference cycle from prior run confirmed resolved
  Note: the prior ingest run hit a BLOCKER on a 2-node cycle between two files both named `MASTER-INDEX.md` — `/Users/acebless/Documents/MASTER-INDEX.md` and `WORLDWIDEBRO-OS/08-DATA/.../01_CEO_COMMAND_CENTER/Indexes/MASTER-INDEX.md`. The latter has since been renamed to `CEO-COMMAND-CENTER-SALES-OPS-INDEX.md`, and its own classification's cross_refs now correctly resolves to `/Users/acebless/Documents/MASTER-INDEX.md` by full path (a genuine one-way "see also" reference, not a cycle). Re-running DFS cycle detection over all 8 docs' cross_refs in this batch found zero cycles. One stale artifact remains: `/Users/acebless/Documents/MASTER-INDEX.md`'s own classification JSON still lists the pre-rename path ending in `.../Indexes/MASTER-INDEX.md` in its `cross_refs` array (its source document's prose text was correctly updated to reference the new filename — only the classification metadata lagged). Because that stale path no longer matches any node's `source_path` in this batch, it resolves to nothing and does not reconstitute the cycle. Recommend re-running the classifier on `/Users/acebless/Documents/MASTER-INDEX.md` to refresh its `cross_refs` metadata, but this is not blocking.

[INFO] Auto-resolved: venture-count figures differ across DOC sources
  Note: ventures counts vary across the DOC-type sources in this batch — `/Users/acebless/Documents/MASTER-INDEX.md` (precedence 0) and `WORLDWIDEBRO-OS/08-DATA/portfolio-reports/README.md` (precedence 0) both cite 712; `GOVERNANCE-CHARTER.md` (precedence 2) and `Worldwidebro-Holdings/README-START-HERE.md` (precedence 4) both cite 704; `CEO-COMMAND-CENTER-SALES-OPS-INDEX.md` (precedence 3, dated 2026-05-10) cites 687; `00-MASTER-INDEX.md` (precedence 3) cites 1,504 "in graph." These read as different snapshots/measures (pipeline total vs Supabase count vs in-graph count) taken at different dates rather than a substantive decision conflict. Per precedence, 712 (the precedence-0 sources) is treated as the canonical figure carried into context.md; the other figures are preserved verbatim in their respective topic entries in context.md for traceability, not deleted.

[INFO] PRD requirement appears only partially executed
  Note: `MASTER-INDEX-CONSOLIDATION-PLAN.md` (PRD, precedence 1, dated 2026-06-13) instructs archiving/deleting `00-MASTER-INDEX.md` by Week 2 as part of consolidating index masters down to 3. `00-MASTER-INDEX.md` (`WORLDWIDEBRO-OS/07-KNOWLEDGE/research/00-MASTER-INDEX.md`) is nonetheless present and was classified as a live DOC in this same ingest batch, with no archive marker. `/Users/acebless/Documents/MASTER-INDEX.md` does now serve as a single broad entry point, consistent with this PRD's overall intent. Recorded in requirements.md under REQ-consolidate-index-masters for the roadmapper's awareness — not gating, since it does not require picking between competing variants.
