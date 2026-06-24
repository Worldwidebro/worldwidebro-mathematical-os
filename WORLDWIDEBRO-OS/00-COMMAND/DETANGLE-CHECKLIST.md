# Repo Detangle Checklist (2026-06-24)

Goal: turn the tangled `~/Documents` super-repo into **one company OS repo + many registered
product repos**, with third-party code de-vendored. See
[[REPO-ARCHITECTURE-AND-DETANGLE-PLAN]] for the why.

Legend: `[me]` I can do · `[you]` needs you · `[!]` risk/irreversible · `->` depends on

---

## COMPONENT A — Repo identity (foundational, do FIRST)
*What is `~/Documents`? Until this is decided, everything else is ambiguous.*

- [ ] **A1 [you] DECIDE:** Documents = plain workspace (not git) **and** `WORLDWIDEBRO-OS/` = the
      git repo  ·OR·  Documents stays the repo, stripped to 1 remote. (Recommended: option 1)
- [ ] A2 [me] -> A1: if option 1, `git init` inside `WORLDWIDEBRO-OS/`, set 1 remote
- [ ] A3 [me] move planning files (`task_plan/findings/progress`) + `.gitignore` to the chosen repo root

## COMPONENT B — Remote wiring (untangle the 4 remotes)
*One repo currently cabled to 4 GitHub repos.*

- [ ] B1 [me] document current 4 remotes (DONE in plan: origin=iza-os-financial-core,
      worldwidebro, applyingjobs, clip)
- [ ] B2 [you] CONFIRM the 1 home remote for the OS -> `Worldwidebro/Worldwidebro.git`
- [ ] B3 [me][!] remove the other 3 remotes from the OS repo (they belong to their own products)
- [ ] B4 [me] set branch upstream so commits have ONE push target

## COMPONENT C — The 74 nested repos (sort into 3 buckets)
*This is the bulk. Each repo goes to exactly one bucket.*

### C-own — Your product repos (~17) -> keep independent, REGISTER
ec-051, edu-013, et-001, fin-001(genixbank-lite), genixbank(financial-system),
business-template-marketplace, YES-LLC-CONTRACTOR, pitch-kit, The office, iza-os-marketing-core,
iza-os-rag-system, RE-001-holdings (x2), career-ops, Crucix, design-system
- [ ] C-own-1 [me] gitignore each from the OS repo (so OS doesn't swallow product code)
- [ ] C-own-2 [me] add `remote_url` to `08-DATA/registries/repositories.csv` for each
- [ ] C-own-3 [you][!] reconcile **duplicates**: `design-system` cloned 3x -> keep 1;
      `fin-001` vs `genixbank` (two genixbank repos) -> decide canonical

### C-dep — Third-party tools (~25) -> DE-VENDOR (not your code)
vllm, ComfyUI, langgraph, llama_index, mem0, crewAI, firecrawl, composio, LightRAG, RAG-Anything,
magika, nanoGPT, omi, opensre, Miro-Fish, MoneyPrinterTurbo/V2, dexter, claude-code-proxy,
anthropic-sdk-python, anthropic-skills, claude-quickstarts, awesome-cursorrules, 3 obsidian plugins
- [ ] C-dep-1 [me] gitignore all (already partly done) — never commit borrowed code
- [ ] C-dep-2 [me] record name + URL in `06-TECHNOLOGY` (dependency list), not as tracked code
- [ ] C-dep-3 [you] decide: keep local clones for use, or delete and `pip/clone` on demand

### C-legacy — Superseded/_legacy-os husks
- [ ] C-leg-1 [you] confirm `_legacy-os/*` + `_superseded/*` safe to delete (content migrated)
- [ ] C-leg-2 [me][!] retire husks after confirmation

## COMPONENT D — The registry "wire" (connect OS -> products)
*The single highest-leverage step: make the alignment executable.*

- [ ] D1 [me] add `remote_url` column to `repositories.csv` from the 69 mapped remotes
- [ ] D2 [me] add `local_path` column (where the clone lives) so agents resolve code location
- [ ] D3 [me] regenerate via `build_registries.py`; verify a venture -> repo -> remote traversal

## COMPONENT E — Stop the parallel writer (unblocks everything)
*Folders keep reappearing because a 2nd process commits to the same branch.*

- [ ] E1 [you] find/stop the job-search writer (other Claude tab, `/loop`, or scheduled agent)
- [ ] E2 [me] move my reorg commits onto an isolated branch so they can't be clobbered
- [ ] E3 [you] reload repointed launchd: `launchctl unload/load ~/Library/LaunchAgents/com.izaos.*`
- [ ] E4 [you] clean the 4 dead `Civilization OS` crontab lines (`crontab -e`)

## COMPONENT F — Final cleanup + verify (LAST)
- [ ] F1 [me] -> E1: move the last 3 reappearing root folders into the tree (sticks once writer stopped)
- [ ] F2 [me] confirm root = only `WORLDWIDEBRO-OS/`, `_career/`, `_inbox/` + gitignored artifacts
- [ ] F3 [me] verify CLAUDE.md/script paths still resolve (run one pipeline script dry)
- [ ] F4 [me] final commit + push to the 1 chosen remote

---

## Sequence (what blocks what)
```
A (repo identity) -+-> B (remotes) -> D (registry wire) -+
                   +-> C (sort repos) -------------------+-> F (cleanup+verify)
E (stop writer) -----------------------------------------+   (E must finish before F)
```

## Do-now vs decide-first
- **Safe for me to do now (no decision):** D1, D2, C-own-2, C-dep-1, E2
- **Needs your decision first:** A1, B2, C-own-3, C-dep-3, C-leg-1
- **Needs your hands (system):** E1, E3, E4
