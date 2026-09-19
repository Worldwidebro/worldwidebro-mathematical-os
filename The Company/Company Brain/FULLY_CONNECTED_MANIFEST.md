# Fully Connected File Base — Execution Manifest

**Goal:** Every core file (800 in Company Brain) discoverable from STARTHERE.md  
**Excluded:** _ENGINE/venv, _EVAL, repos, _TOOLS, external dependencies  
**Connected:** 00-57 domains + infrastructure + root master files  

## Phase 1: Map Core Files (Complete)
✅ Schema created: FILE_GRAPH_SCHEMA.cypher  
✅ Scan completed: FILE_GRAPH_REPORT.json  
✅ Strategy defined: FULLY_CONNECTED_STRATEGY.md  

## Phase 2: Ready to Execute
- [ ] Generate 87 missing domain READMEs (link to STARTHERE + INDEX)
- [ ] Auto-add wiki link headers to disconnected files
- [ ] Repair broken core references (153 valid links)
- [ ] Verify Neo4j graph connectivity

## Success Metric
✅ Start at any file in Company Brain  
✅ Click [[STARTHERE]] → master entry point  
✅ From STARTHERE, reach all other files in <3 clicks  
✅ Neo4j: All 800 files reachable from STARTHERE node

## Execution Pattern (FROM NOW ON)
```bash
# Find scattered file
if scattered_file_found; then
  move_to_proper_domain  # Phase 3 completion
  link_to_starthere      # Auto-add [[STARTHERE]]
  commit_atomically      # One file = one commit
fi
```

## Files Ready for Connection
| Type | Location | Count | Status |
|------|----------|-------|--------|
| Master | root | 6 | ✅ Done |
| Numbered domains | 00-57/ | 72 | 🔄 In progress |
| Infrastructure | _*/ | 8 | 🔄 In progress |
| Ventures | 23-VENTURES/ | 30 | ⏳ Next |
| Business data | BUSINESS-CAPITAL-DATA-ROOM/ | 50 | ⏳ Next |

Total core: ~800 files (ready to fully connect)

---

**Status:** Manifest created Sep 19, 2026  
**Next Action:** Execute Phase 2 (generate READMEs + auto-link)  
**Authority:** Architecture CP-027
