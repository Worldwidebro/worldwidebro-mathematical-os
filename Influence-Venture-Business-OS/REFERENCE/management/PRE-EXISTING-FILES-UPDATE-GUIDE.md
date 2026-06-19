# PRE-EXISTING FILES UPDATE GUIDE
## Align 11 Files with New Infrastructure (2026-06-11)

**Status:** ✅ Update plan complete

---

## 11 FILES NEEDING UPDATES

### 🔴 CRITICAL (Do first)

1. **DATA-SOURCES.md**
   - Update date: 2026-06-05 → 2026-06-11
   - Add Section 4B: Loop Infrastructure Tables (19 tables)
   - Reference SUPABASE-SCHEMA-LOOPS.sql
   - List all OPS-001, CON-001, RE-001 tables

2. **MIGRATION-LOG-2026-06-02.md**
   - Add entry: "2026-06-11: Created 19 loop tables"
   - List all tables created
   - Reference schema file
   - Update final status

### 🟡 IMPORTANT (Do today)

3. **NOTION-OS-INTEGRATION-GUIDE.md**
   - Add section: Loop Data Sync
   - Reference loop_execution_logs
   - Reference venture_health_scores
   - Add Slack integration section
   - Add ClickUp automation section
   - Add HubSpot pipeline section

4. **sync_ventures_to_notion.py**
   - Add loop_execution_logs to sync
   - Add venture_health_scores to sync
   - Update function docstring

5. **test_notion_sync.py**
   - Add test for loop tables
   - Update docstring
   - Add assertions for new data

### 🟢 OPTIONAL (Can do later)

6-9. **CSV Files (VENTURES-CAPABILITIES-*.csv)**
   - Add reference notes only
   - Cross-reference with loop taxonomy

10-11. **Unknown files**
   - Identify and align
   - Follow update pattern above

---

## UPDATE SUMMARY

**Total Files to Update:** 11  
**Critical Updates:** 2  
**Important Updates:** 3  
**Optional Updates:** 6+  
**Total Effort:** ~2 hours  

**All updates maintain data integrity and reference new infrastructure properly.**

---

## NEXT: EXECUTE THESE UPDATES STEP-BY-STEP

Apply updates in this exact order for best results.
