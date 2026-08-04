# Pilot Deployment Report — venture-template 3-file package

**Date:** 2026-07-29
**Template source:** `/Users/acebless/Documents/venture-template/`
**Target list:** CON-001, FIN-001, RE-001, LT-005, OPS-001, EC-001, TECH-001, COMM-001, EDU-001, FIN-006

## Folder resolution note

None of the venture IDs exist as literal folder names. Resolved actual repo folders via `.planning/VENTURE-READINESS-SCORECARD-V2.csv` `repo_key` column (source of truth per CLAUDE.md). OPS-001 has no matching `repo_key` locally (`ops-001-fractional-cto-agency` and `ops-001-venture-staffing` are both absent) — deployed instead to `ops-staff-001-staffing`, the real staffing-venture repo the user already references as "OPS-001" in memory notes. RE-001's `repo_key` (`re-001-property-holdings`) is a GitHub redirect to `re-001-worldwidebro-holdings` (repo was renamed); push succeeded via the redirect.

## Concurrent run detected

A second instance of this same pilot-deployment task had already run against LT-005, EC-001, and FIN-006 minutes before this run started (commits `7fc6fee`, `f5f17f4`, `f938d9b`, all timestamped ~02:01-02:02am). Those three were verified as already fully deployed and pushed — no duplicate work done except a harmless comment-stripping commit on LT-005's venture.json.

## Results

| Venture ID | Resolved folder | Folder exists | Files deployed | Commit pushed | Status |
|---|---|---|---|---|---|
| CON-001 | con-001-ace-construction | Yes | ONTOLOGY.md (symlink), ontology.ts — venture.json **skipped** (real business data, different schema, preserved) | `6511631` | Deployed |
| FIN-001 | fin-001-genixbank-lite | No | — | — | Not found locally |
| RE-001 | re-001-property-holdings | Yes | ONTOLOGY.md, venture.json, ontology.ts (full deploy — no prior venture.json) | `675efc5` | Deployed |
| LT-005 | lt-005-medical-courier-dispatch | Yes | Already deployed by concurrent run (`7fc6fee`); this run only tidied venture.json comments | `3e08704` | Deployed (pre-existing) |
| OPS-001 | ops-staff-001-staffing | Yes | ONTOLOGY.md, venture.json, ontology.ts (full deploy) | `b828e3a` | Deployed |
| EC-001 | ec-001-angels-in-daylight | Yes | Already deployed by concurrent run — ONTOLOGY.md, ontology.ts; venture.json (real business data) preserved | `f5f17f4` | Deployed (pre-existing) |
| TECH-001 | tech-001-quantum-algorithm-ai | No | — | — | Not found locally |
| COMM-001 | comm-001-luminary-worldwide-events | No | — | — | Not found locally |
| EDU-001 | edu-001-youth-entrepreneurship-curriculum | No | — | — | Not found locally |
| FIN-006 | fin-006-tax-prep-filing-services | Yes | Already deployed by concurrent run — ONTOLOGY.md, ontology.ts; venture.json (real business data) preserved | `f938d9b` | Deployed (pre-existing) |

**Summary: 6/10 ventures successfully deployed. 4/10 not found locally (no clone exists under any known repo_key).**

## Ventures not found locally

These have GitHub-registered `repo_key`s in the CSV but no local clone under `/Users/acebless/Documents/`:
- **FIN-001** — GenixBank Lite (`fin-001-genixbank-lite`)
- **TECH-001** — Quantum Algorithm AI (`tech-001-quantum-algorithm-ai`)
- **COMM-001** — Luminary Worldwide Events (`comm-001-luminary-worldwide-events`)
- **EDU-001** — Youth Entrepreneurship Curriculum (`edu-001-youth-entrepreneurship-curriculum`)

Per scope, no new folders were created — these need `git clone` before the pattern can be deployed.

## venture.json overwrite policy applied

Three ventures (CON-001, EC-001, FIN-006) already had a `venture.json` populated with real business data (revenue targets, entity info, ICP, grants, etc.) using a different schema than the template's ontology-tracking schema (`id`/`agent_id`/`skills`/`ontology_version`). Overwriting these would have destroyed live business data for a cosmetic pattern test, so `venture.json` was left untouched on those three — only `docs/ONTOLOGY.md` and `src/lib/ontology.ts` were added. This is a schema conflict worth resolving before bulk deployment: decide whether `venture.json` should be one unified schema or the ontology fields should be merged into the existing per-venture schema.

## Commit hashes

| Venture | Commit |
|---|---|
| CON-001 | `6511631d29fe527d79520e6d0fb3043278cea795` |
| RE-001 | `675efc52254510485a8310fa8f10597e0daac856` |
| LT-005 | `3e08704c69d9e1bfe00a8f8ed4c464e2c8e7881b` |
| OPS-001 | `b828e3ab87c4280b7b23fb58dd87f12ac3ad2543` |
| EC-001 | `f5f17f4a8d19835b9c74dbf7b5d376eadd9f1288` |
| FIN-006 | `f938d9b` (verified `origin/main` matches `HEAD`, 0 unpushed commits) |

All 6 deployed repos confirmed pushed to `origin/main` with zero unpushed commits as of end of run.
