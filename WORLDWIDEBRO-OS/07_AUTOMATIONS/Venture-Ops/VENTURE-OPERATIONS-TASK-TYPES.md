---
title: Venture Operations Task Types & Skill Mapping
created: 2026-06-01T00:00:00Z
last_edited: 2026-06-02T20:27:23Z
edited_by: Claude Haiku 4.5
version: 1.0
---

# Venture Operations Task Types & Skill Mapping

**Purpose:** Define task types in ClickUp Venture Ops list + map each to executable skills/workflows.

---

## Task Type Definitions (12 Total)

### 1. DEPLOY
**Ventures affected:** All (712)  
**Trigger:** "Venture ready for production"  
**Steps:**
- Read task: venture_id, deployment_target (staging/prod), version
- Load venture context from Supabase
- Invoke deployment skill (build → test → deploy)
- Update task status in ClickUp

**Custom Fields:**
- venture_id (text)
- deployment_target (single select: staging/prod)
- version (text)
- status (single select: pending/in_progress/success/failed)

---

### 2. MIGRATE
**Ventures affected:** Database-heavy (HRMS, CRM, logistics, health)  
**Trigger:** "Schema change or data migration needed"  
**Steps:**
- Read task: venture_id, migration_name, migration_sql
- Validate SQL (security check)
- Run migration against Supabase DB
- Rollback plan ready
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- migration_name (text)
- migration_sql (text, long)
- is_production (checkbox)
- rollback_plan (text)
- status (single select: pending/in_progress/success/failed)

---

### 3. INTEGRATE
**Ventures affected:** All requiring external APIs (payments, email, SMS, etc.)  
**Trigger:** "New API integration needed"  
**Steps:**
- Read task: venture_id, service (Stripe, SendGrid, etc.), credentials_vault_key
- Load credentials from secure vault
- Test API connection
- Deploy integration code
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- service (text: Stripe, SendGrid, Twilio, etc.)
- credentials_vault_key (text)
- status (single select: pending/in_progress/success/failed)

---

### 4. TEST
**Ventures affected:** All  
**Trigger:** "Run E2E tests or QA suite"  
**Steps:**
- Read task: venture_id, test_suite (e2e, unit, integration, smoke)
- Invoke test runner for that venture
- Collect results
- Update ClickUp with pass/fail
- Flag failures for manual investigation

**Custom Fields:**
- venture_id (text)
- test_suite (single select: e2e/unit/integration/smoke)
- status (single select: pending/in_progress/success/failed)
- failures (text, auto-populated)

---

### 5. SYNC
**Ventures affected:** Knowledge-graph heavy (IZA-OS, Graphify, all ventures with KG)  
**Trigger:** "Sync venture data to knowledge graph"  
**Steps:**
- Read task: venture_id, data_source (GitHub, Supabase, Obsidian)
- Export venture data from source
- Upsert into LightRAG graph
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- data_source (single select: GitHub/Supabase/Obsidian)
- status (single select: pending/in_progress/success/failed)

---

### 6. DOCUMENT
**Ventures affected:** All  
**Trigger:** "Update venture documentation"  
**Steps:**
- Read task: venture_id, doc_type (README, API, architecture, etc.)
- Generate or update doc from template
- Validate links/references
- Commit to GitHub
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- doc_type (single select: README/API/architecture/deployment)
- status (single select: pending/in_progress/success/failed)

---

### 7. MONITOR
**Ventures affected:** Production ventures  
**Trigger:** "Check health/metrics for venture"  
**Steps:**
- Read task: venture_id, metric_type (uptime, latency, error_rate, etc.)
- Fetch metrics from monitoring system (Grafana, DataDog, etc.)
- Compare against thresholds
- Alert if critical
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- metric_type (single select: uptime/latency/error_rate/cpu/memory)
- threshold (number)
- status (single select: pending/in_progress/warning/critical)

---

### 8. BACKUP
**Ventures affected:** Database ventures (HRMS, CRM, health records, etc.)  
**Trigger:** "Backup database"  
**Steps:**
- Read task: venture_id, backup_type (full/incremental), target_storage
- Trigger Supabase backup
- Verify backup integrity
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- backup_type (single select: full/incremental)
- target_storage (text: S3/GCS/local)
- status (single select: pending/in_progress/success/failed)

---

### 9. ONBOARD
**Ventures affected:** New ventures (weekly automation)  
**Trigger:** "New venture added to portfolio"  
**Steps:**
- Read task: venture_id
- Create folder structure in WORLDWIDEBRO-OS
- Initialize Supabase table + RLS policies
- Create GitHub repo (if needed)
- Register in knowledge graph
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- folder_created (checkbox)
- db_initialized (checkbox)
- repo_created (checkbox)
- status (single select: pending/in_progress/success/failed)

---

### 10. REPORT
**Ventures affected:** Key metrics ventures  
**Trigger:** "Generate weekly/monthly report"  
**Steps:**
- Read task: venture_id, report_type (weekly/monthly), metrics_list
- Fetch data from Supabase
- Generate report (markdown)
- Post to Slack channel for venture
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- report_type (single select: weekly/monthly)
- metrics_list (text, comma-separated)
- status (single select: pending/in_progress/success/failed)

---

### 11. SCALE
**Ventures affected:** High-growth ventures  
**Trigger:** "Scale infrastructure for demand spike"  
**Steps:**
- Read task: venture_id, scale_target (database/compute/storage), new_capacity
- Provision new resources in Supabase/Vercel
- Run load tests
- Monitor performance
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- scale_target (single select: database/compute/storage)
- new_capacity (text)
- status (single select: pending/in_progress/success/failed)

---

### 12. INCIDENT
**Ventures affected:** Any in production  
**Trigger:** "Production issue detected"  
**Steps:**
- Read task: venture_id, severity (critical/high/medium), description
- Assign to on-call engineer (Slack notification)
- Create incident in monitoring system
- Track resolution
- Post-mortem after close
- Update ClickUp

**Custom Fields:**
- venture_id (text)
- severity (single select: critical/high/medium)
- description (text)
- assigned_to (text)
- status (single select: pending/in_progress/resolved/investigating)

---

## ClickUp List Setup (Venture Ops)

**List Name:** "Venture Operations—Autonomous"  
**Workspace ID:** 9013677375 (same as sales)  
**Status:** 📋 Ready to create  

**Statuses:**
- ⏳ Pending (not started)
- 🔄 In Progress (running)
- ✅ Success (completed)
- ❌ Failed (error, needs manual fix)
- ⚠️ Warning (threshold hit, needs attention)

---

## Skill Mapping Reference

| Task Type | Skill Invoked | MCP Required | Async |
|-----------|---------------|--------------|-------|
| DEPLOY | deployment-workflow | Vercel, GitHub | Yes |
| MIGRATE | supabase-migration | Supabase | Yes |
| INTEGRATE | api-integration | Service-specific | Yes |
| TEST | test-runner | Jest/Playwright | Yes |
| SYNC | kg-sync | LightRAG, Supabase | Yes |
| DOCUMENT | doc-generator | GitHub | No |
| MONITOR | metrics-fetch | Grafana/DataDog | No |
| BACKUP | backup-trigger | Supabase | Yes |
| ONBOARD | venture-setup | All | Yes |
| REPORT | report-generator | Supabase | No |
| SCALE | provision-resources | Vercel, Supabase | Yes |
| INCIDENT | incident-routing | PagerDog, Slack | No |

---

## Next Steps

1. Create ClickUp list "Venture Operations—Autonomous"
2. Add custom fields per task type above
3. Build task watcher (polls every 5 min)
4. Build task executor (invokes skills)
5. Test on HRMS venture first

---

**Status:** ✅ READY  
**Ready by:** 2026-06-01  
**Reviewed by:** —
