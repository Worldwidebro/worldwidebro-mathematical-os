---
title: Venture Operations—Autonomous System Setup Guide
created: 2026-06-01T00:00:00Z
last_edited: 2026-06-02T20:27:23Z
edited_by: Claude Haiku 4.5
version: 1.0
---

# Venture Operations—Autonomous System Setup

**Goal:** Enable 712 ventures to auto-execute operational tasks (deploy, migrate, sync, test, etc.) via ClickUp + skill-based execution.

---

## System Architecture

```
ClickUp Task Created
        ↓
Task Watcher (polls every 5 min)
        ↓
Task Parser (extracts venture_id, task_type, custom fields)
        ↓
Task Executor (routes to skill)
        ↓
Skill Invoked (deploy, migrate, test, sync, etc.)
        ↓
ClickUp Updated (status + results)
```

---

## Files in This System

| File | Purpose | Created | Last Edited | Editor |
|------|---------|---------|-------------|--------|
| VENTURE-OPERATIONS-TASK-TYPES.md | Defines 12 task types & skill mappings | 2026-06-01 | 2026-06-01 | Claude Haiku 4.5 |
| task-watcher.py | Polls ClickUp, parses tasks, invokes executor | 2026-06-01 | 2026-06-01 | Claude Haiku 4.5 |
| task-executor.py | Routes tasks to appropriate skills | 2026-06-01 | 2026-06-01 | Claude Haiku 4.5 |
| VENTURE-OPS-AUTONOMOUS-SETUP.md | Setup guide & edit tracking | 2026-06-01 | 2026-06-01 | Claude Haiku 4.5 |

**File Metadata Key:**
- `created`: When the file was first written
- `last_edited`: Most recent edit timestamp
- `edited_by`: Who made the last edit (Claude Haiku 4.5 or team member)
- `version`: Semantic versioning (major.minor.patch)

---

## Setup Steps (5 min each)

### Step 1: Create ClickUp List "Venture Operations—Autonomous"

1. Go to ClickUp workspace: **9013677375**
2. Click **+ List**
3. Name: `Venture Operations—Autonomous`
4. Add statuses:
   - ⏳ Pending
   - 🔄 In Progress
   - ✅ Success
   - ❌ Failed
   - ⚠️ Warning

---

### Step 2: Add Custom Fields to List

For each task type, add custom fields (see VENTURE-OPERATIONS-TASK-TYPES.md for full spec):

**Global fields:**
- `venture_id` (Text)
- `task_type` (Single Select)

**Task-specific fields:**
- DEPLOY: deployment_target, version
- MIGRATE: migration_name, migration_sql, is_production, rollback_plan
- INTEGRATE: service, credentials_vault_key
- TEST: test_suite, failures
- SYNC: data_source
- DOCUMENT: doc_type
- MONITOR: metric_type, threshold
- BACKUP: backup_type, target_storage
- ONBOARD: folder_created, db_initialized, repo_created
- REPORT: report_type, metrics_list
- SCALE: scale_target, new_capacity
- INCIDENT: severity, description, assigned_to

**Save field IDs** for .env configuration.

---

### Step 3: Configure .env

```bash
# ClickUp API
CLICKUP_API_KEY=your_token_here
CLICKUP_WORKSPACE=9013677375
CLICKUP_LIST_VENTURE_OPS=901003877

# Polling
POLL_INTERVAL=300  # 5 minutes
LOG_LEVEL=INFO
```

---

### Step 4: Start Task Watcher

```bash
# Test run
python task-watcher.py

# Background
systemctl start venture-ops-watcher
systemctl enable venture-ops-watcher

# Docker
docker-compose up -d task-watcher
```

---

### Step 5: Create Test Task

In ClickUp:
1. New task: `DEPLOY HRMS-001 to staging`
2. Custom fields:
   - venture_id: `HRMS-001`
   - deployment_target: `staging`
   - version: `1.0.0`
3. Status: ⏳ Pending
4. Save

Watcher picks up in 5 min → updates status → posts result comment.

---

## Scaling to 712 Ventures

Once HRMS works:

1. **Batch tasks:**
   ```python
   for v_id in ventures:
       create_task(name=f"ONBOARD {v_id}", venture_id=v_id)
   ```

2. **Schedule recurring:**
   - MONITOR: Daily
   - REPORT: Weekly
   - BACKUP: Nightly

3. **Automate creation:**
   - Supabase trigger → ONBOARD task
   - GitHub webhook → TEST task
   - Cron job → BACKUP tasks

---

## Edit Tracking & Handoff

When modifying files:

1. **Update YAML frontmatter:**
   ```yaml
   last_edited: 2026-06-02T20:27:23Z
   edited_by: Claude Haiku 4.5
   version: 1.1
   ```

2. **Add change log entry:**
   ```markdown
   - **v1.1** (2026-06-01, Your Name): Description of changes
   ```

3. **Commit with context:**
   ```
   Update task-watcher.py: Add retry logic
   
   - 3 retries with exponential backoff
   - Updated YAML metadata
   ```

**Result:** Everyone knows who changed what, when, and why.

---

## Troubleshooting

**Tasks not picked up?**
- Verify CLICKUP_API_KEY in .env
- Check list ID matches config
- Review logs: `tail -f /var/log/venture-ops/task-watcher.log`

**Tasks stuck in progress?**
- Check executor logs for errors
- Verify MCP/skill connection
- Manually retry task

**Fields not syncing?**
- Verify field IDs
- Check field types (Single Select vs Text)
- Clear cache

---

**Status:** ✅ READY  
**Test Venture:** HRMS (pending)  
**Reviewed:** —
