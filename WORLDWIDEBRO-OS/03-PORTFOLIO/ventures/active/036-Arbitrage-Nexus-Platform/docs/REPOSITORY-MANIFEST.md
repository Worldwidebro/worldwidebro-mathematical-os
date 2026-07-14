# Repository Manifest — Arbitrage Nexus Platform

## Mapped repositories

| Repo | Role | Stack | Status |
|------|------|-------|--------|
| [`fin-036-arbitrage-nexus-platform`](https://github.com/Worldwidebro/fin-036-arbitrage-nexus-platform) | Canonical venture repo — strategy, VENTURE.json, `lib/shared` submodule | Shell + Markdown | Docs complete, no execution code. |
| [`arbitrage-nexus`](https://github.com/Worldwidebro/arbitrage-nexus) | Frontend MVP — multi-vertical marketplace | React + TS + Vite + Supabase + shadcn/ui | Live and deployed at https://arbitrage-nexus.vercel.app (2026-07-13): listing creation, messaging, admin approval, test-mode Stripe payment links all working. Backend migrated to `arbitrage_nexus` schema in the CivilizationOS Supabase project. |

## Source records

- `08-DATA/registries/venture_repo_map.csv`
- `08-DATA/registries/venture_capability_map.csv`
- `REGISTRIES/repository_registry_pilot.json`
- **Not** `repo_venture_mapping.json` — its FIN-036 entry is score-based noise (unrelated repos like `documenso` outscore the real `arbitrage-nexus` repo, and `fin-036-arbitrage-nexus-platform` isn't listed at all). Manually verified mapping above supersedes it for this venture.

## Notes

Use this manifest to assign repos to venture workstreams, owner agents, and CI/CD clusters.

**2026-07-13 revert incident:** this file was found reverted to a blank
"*(none mapped)*" stub after having been manually corrected on 2026-07-11 —
part of a mass event that touched 715 VENTURE.md files across the portfolio
in the same ~30 minute window. Root cause not yet identified (ruled out the
three scheduled `com.izaos.*` launchd jobs — none were due to fire). If this
file reverts again, that confirms an active, unidentified regeneration
process is overwriting manually-edited venture docs, and the durable fix
needs to happen upstream in the registry/VENTURE.json source data, not in
this generated output file.