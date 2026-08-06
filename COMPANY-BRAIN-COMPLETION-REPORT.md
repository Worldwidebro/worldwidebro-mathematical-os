---
name: COMPANY-BRAIN-COMPLETION-REPORT
title: Company Brain Completion Report
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Company Brain Completion Report

**Completed:** 2026-05-09  
**Project:** CivilizationOS / `cyhzilqldouzgynacqpe`

---

## What Was Completed

The company-brain spine is now live in Supabase and populated from local files, ClickUp mappings, and context events.

## Live Supabase Tables Created

- `external_system_links`
- `company_files`
- `file_task_links`
- `venture_context_events`

Migration applied from:

- `/Users/acebless/Documents/venture-hub/supabase/migrations/202605020001_create_company_file_registry.sql`

## Live Row Counts

| Table | Rows |
|---|---:|
| `company_files` | 749 |
| `external_system_links` | 682 |
| `file_task_links` | 616 |
| `venture_context_events` | 55 |

## File Scan

Broad scan root:

- `/Users/acebless/Documents`

Scan result before explicit VAPI registration:

- 6,681 candidate files scanned
- 735 files mapped
- 54 venture IDs covered

Inventory snapshot:

- `/Users/acebless/Documents/venture-hub/data/company_files_inventory.json`

## VAPI Calling System Registered

The VAPI AI calling system was explicitly registered because root-level files do not all contain venture IDs.

Registered module:

- `SALES-001-AI-CALLING-SYSTEM`

Registered files:

- `.env.example`
- `CONTACTS-INITIAL.csv`
- `OUTREACH-EXECUTION-GUIDE.md`
- `PHASE-1-CHECKLIST.md`
- `PHASE-1-READY-TO-DEPLOY.md`
- `VAPI-API-USAGE.md`
- `package.json`
- `rag-venture-context.js`
- `vapi-agent-bella-config.json`
- `vapi-agent-echo-config.json`
- `vapi-agent-swift-config.json`
- `vapi-api-integration.js`
- `webhook-call-complete.js`
- `webhook-server.js`

Support script added:

- `/Users/acebless/Documents/venture-hub/scripts/register-vapi-calling-files.js`

## Support Script Added

- `/Users/acebless/Documents/venture-hub/scripts/generate-company-brain-upsert.js`

This generates a Supabase SQL upsert from `data/company_files_inventory.json` so the brain can be reloaded through the Supabase management connection without disabling RLS.

## Current Data Flow

```text
Local files
  -> company_files_inventory.json
  -> Supabase company_files
  -> file_task_links
  -> external_system_links
  -> venture_context_events
  -> RAG / LlamaIndex / agent context
```

## Notes

- Public REST reads may show zero rows for the new tables because RLS is enabled.
- Supabase management queries confirm the actual counts above.
- `business_ventures_master` is not present in the live schema. The canonical live venture table remains `business_ventures`.
