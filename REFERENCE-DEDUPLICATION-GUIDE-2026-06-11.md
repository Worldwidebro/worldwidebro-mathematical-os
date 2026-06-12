# Reference Deduplication Guide
## 10,846 Markdown Files — Inconsistent Naming Resolution

**Issue:** Same concepts referenced with 5-10 different naming conventions  
**Impact:** Broken cross-file linking, fragmented search, context loss  
**Solution:** Establish canonical naming standard + batch deduplication  
**Status:** Plan documented, ready to execute next session

---

## ❌ THE PROBLEM (Examples)

### CON-011 (Electrical Services)
```
❌ con-011-electrical-services/     (lowercase)
❌ CON-011-Electrical-Services/     (mixed case)
❌ CON-011-Electrical/              (abbreviated)
❌ electrical-services/             (no ID)
❌ Electrical/                      (wrong structure)
❌ ops-venture-002-electrical/      (legacy)
```

**Result:** Same venture, 6+ reference formats → broken links

---

## ✅ CANONICAL STANDARD (NEXT SESSION)

### Venture ID
```
Format:   CON-###
Example:  CON-011
Use:      Master references
```

### Directory
```
Format:   con-###-venture-name-lowercase/
Example:  con-011-electrical-services/
Use:      Folder structure
```

### Files
```
Format:   CON-###-VENTURE-NAME-UPPERCASE-TYPE.md
Example:  CON-011-ELECTRICAL-SERVICES-BANKABILITY-ROADMAP.md
Use:      Documentation
```

### WikiLinks
```
Format:   [[CON-### | Venture Name]]
Example:  [[CON-011 | Electrical Services]]
Use:      Cross-file references
```

---

## 📋 NEXT SESSION TASKS (READY TO EXECUTE)

### Task A1: Audit References (4 hours)
**Input:** All 10,846 markdown files  
**Process:** Find all CON-### variations  
**Output:** REFERENCE-RESOLUTION-MAP.csv

```
concept,canonical_id,canonical_name,variations_found,files_affected
Electrical,CON-011,Electrical Services,"con-011, electrical, Electrical",47
HVAC,CON-012,HVAC Services,"con-012, hvac, HVAC",52
... (712 ventures)
```

**Script:** Bash find + grep + sort -u

### Task A2: Standardize (8 hours)
**Process:** Batch sed/replace using CSV mapping  
**Output:** 10,846 files with consistent naming  
**Automation:** 90% scriptable

```bash
find . -name "*.md" -type f \
  -exec sed -i 's/con-011-electrical/CON-011-Electrical-Services/g' {} \; \
  -exec sed -i 's/\[\[electrical\]\]/[[CON-011 | Electrical]]/g' {} \;
```

### Task A3: Validate (2 hours)
**Check:** All references resolve, no orphans  
**Output:** Validation report + metrics  
**Automation:** Script + manual spot-check

---

## 🔗 WIKILINKS STRUCTURE

### Currently ✅ Created
```
CON-011 → CON-011-ELECTRICAL-SERVICES-BANKABILITY-ROADMAP.md
CON-012 → CON-012-HVAC-SERVICES-BANKABILITY-ROADMAP.md
(2/20 manual, 18 auto-created but need linking)
```

### Ready to Wire (Task B)
```
[[CON-011 | Electrical Services]]
  ├─ [[Bankability Roadmap]]
  ├─ [[Week-1 Execution Plan]]
  ├─ [[Skill Framework Integration]]
  └─ [[Awesome Library Links]]
```

---

## ✅ WHAT'S READY

**Deduplication Plan:** ✅ Documented above  
**Task Breakdown:** ✅ Time-estimated (14 hours for A tasks)  
**Naming Standard:** ✅ Defined (canonical forms)  
**Scripts Outline:** ✅ Provided (ready to code)  
**Execution Order:** ✅ Clear (A → B → C → D)

---

## 🚀 READY FOR NEXT SESSION?

**Start with:** Task A1 (audit references)  
**Timeline:** All A tasks complete in 14 hours  
**Then:** Tasks B, C, D follow directly  
**Payoff:** 10,846 files deduplicated + wikilinked

---

**Date:** 2026-06-11  
**Status:** Plan ready ✅ | Execution pending  
**Next Step:** Task A1
