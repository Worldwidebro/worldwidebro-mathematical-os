# DealFlowOS PostgreSQL Persistence

**Authority:** DealFlowOS Engine  
**Status:** ✅ Wired (2026-09-08)  
**Database:** PostgreSQL at localhost:5433  
**API Server:** Python HTTP server at 127.0.0.1:5432

---

## Overview

DealFlowOS now has persistent deal storage via PostgreSQL. All deals created through the dealflow-os.html UI are automatically persisted to the database and survive page reloads.

### Three-Table Schema

**`deals`** — Core deal records
- `id` (SERIAL PRIMARY KEY)
- `company_id` (VARCHAR 100, UNIQUE) — Machine-readable identifier
- `company_name` (VARCHAR 255) — Display name
- `stage` (VARCHAR 50) — Pipeline stage (discovered, researched, qualified, contacted, negotiating, closed)
- `value` (DECIMAL 15,2) — Deal value in currency
- `structure_type` (VARCHAR 100) — Deal structure (equity, debt, grant, etc.)
- `industry`, `location` — Enrichment fields
- `contact_email`, `contact_phone` — Contact info
- `notes` (TEXT) — Internal notes
- `score` (DECIMAL 5,2) — Deal quality score (0-100)
- `created_at`, `updated_at` (TIMESTAMP) — Audit timestamps
- `created_by`, `source` (VARCHAR) — Origin tracking
- **Indexes:** stage, created_at

**`deal_notes`** — Deal collaboration & notes
- `id` (SERIAL PRIMARY KEY)
- `deal_id` (INTEGER FK → deals.id, CASCADE) — Which deal
- `content` (TEXT) — Note text
- `note_type` (VARCHAR 50) — general, update, decision, etc.
- `created_by`, `created_at`, `updated_at` (TIMESTAMP) — Audit
- `is_pinned` (BOOLEAN) — Pin important notes to top
- **Index:** deal_id

**`agent_runs`** — Agent execution tracking
- `id` (SERIAL PRIMARY KEY)
- `deal_id` (INTEGER FK → deals.id, CASCADE) — Which deal
- `agent_type` (VARCHAR 100) — Type of agent (research, qualify, enrich, etc.)
- `agent_name` (VARCHAR 255) — Specific agent instance
- `status` (VARCHAR 50) — pending, running, completed, failed
- `input_data`, `results_json` (JSONB) — Structured data for the run
- `error_message` (TEXT) — Failure details
- `execution_time_ms` (INTEGER) — Runtime
- `started_at`, `completed_at` (TIMESTAMP) — Precise timing
- **Index:** deal_id

---

## Installation

### 1. Install PostgreSQL Driver

```bash
pip install psycopg2-binary
```

### 2. Verify PostgreSQL is Running

```bash
psql -h localhost -p 5433 -U admin -d company_brain -c "SELECT 1;"
```

**Output should show:** `?column?` / `1`

### 3. Start the API Server

```bash
cd "/Users/acebless/Documents/The Company/Company Brain"
python3 _MCP/dealflow_postgres_api.py
```

**Expected output:**
```
✓ PostgreSQL schema initialized successfully
✓ DealFlowOS PostgreSQL API Server running on http://127.0.0.1:5432

Endpoints:
  POST   /api/deals                 — Create new deal
  GET    /api/deals                 — List all deals
  GET    /api/deals/:id             — Get deal details
  PUT    /api/deals/:id             — Update deal
  POST   /api/deals/:id/notes       — Add deal note
  GET    /api/deals/:id/notes       — Get deal notes
  POST   /api/deals/:id/agent-runs  — Log agent run
  GET    /api/deals/:id/agent-runs  — Get agent runs
  GET    /health                    — Health check
```

### 4. Test Health

```bash
curl http://127.0.0.1:5432/health
```

**Expected response:**
```json
{"status": "healthy", "service": "dealflow-postgres-api"}
```

---

## API Endpoints

### Create Deal (POST)

```bash
curl -X POST http://127.0.0.1:5432/api/deals \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "BuildRight Construction",
    "value": 500000,
    "industry": "Construction",
    "location": "North Carolina",
    "stage": "discovered",
    "source": "dealflow-os"
  }'
```

**Response (201 Created):**
```json
{
  "success": true,
  "deal_id": 1,
  "company_id": "...",
  "company_name": "BuildRight Construction",
  "created_at": "2026-09-08T14:30:22.123456"
}
```

### Get All Deals (GET)

```bash
curl http://127.0.0.1:5432/api/deals?limit=50&stage=discovered
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "company_id": "...",
      "company_name": "BuildRight",
      "stage": "discovered",
      "value": 500000,
      "score": 75,
      "created_at": "2026-09-08T14:30:22"
    }
  ],
  "count": 1
}
```

### Get Deal Details (GET)

```bash
curl http://127.0.0.1:5432/api/deals/1
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "company_id": "...",
    "company_name": "BuildRight",
    "stage": "discovered",
    "value": 500000,
    "score": 75,
    "created_at": "2026-09-08T14:30:22",
    "notes_list": [...],
    "agent_runs": [...]
  }
}
```

### Update Deal (PUT)

Move deal through pipeline by updating stage:

```bash
curl -X PUT http://127.0.0.1:5432/api/deals/1 \
  -H "Content-Type: application/json" \
  -d '{
    "stage": "qualified",
    "score": 85
  }'
```

**Response (200 OK):**
```json
{
  "success": true,
  "deal_id": 1,
  "updated_at": "2026-09-08T15:45:00.123456",
  "fields_updated": ["stage", "score"]
}
```

### Add Deal Note (POST)

```bash
curl -X POST http://127.0.0.1:5432/api/deals/1/notes \
  -H "Content-Type: application/json" \
  -d '{
    "content": "CEO interested in H2 2026 expansion",
    "note_type": "update",
    "created_by": "sarah"
  }'
```

**Response (201 Created):**
```json
{
  "success": true,
  "note_id": 42,
  "deal_id": 1,
  "created_at": "2026-09-08T14:35:00.123456"
}
```

### Log Agent Run (POST)

```bash
curl -X POST http://127.0.0.1:5432/api/deals/1/agent-runs \
  -H "Content-Type: application/json" \
  -d '{
    "agent_type": "research",
    "agent_name": "Research Agent v2.1",
    "status": "completed",
    "input_data": {"company_id": "...", "depth": "deep"},
    "results_json": {"found_contacts": 5, "score_delta": 10}
  }'
```

**Response (201 Created):**
```json
{
  "success": true,
  "run_id": 23,
  "deal_id": 1,
  "created_at": "2026-09-08T14:40:00.123456"
}
```

---

## UI Integration

The `dealflow-os.html` "New Deal" button now:

1. Captures form inputs (company_name, value, industry, location)
2. POSTs to `/api/deals` with `API_POSTGRES` base URL
3. Displays success/error feedback
4. Clears form on success
5. Refreshes pipeline view (if loaded)

### Form Fields

```html
<input id="dealName" type="text" placeholder="Company name" />
<input id="dealValue" type="number" placeholder="Deal value ($)" />
<input id="dealIndustry" type="text" placeholder="Industry" />
<input id="dealLocation" type="text" placeholder="Location" />
```

All fields except `dealName` are optional.

---

## Verification Checklist

✅ **Schema created:** Run `psql -h localhost -p 5433 -U admin -d company_brain -c "\dt;"` to list tables  
✅ **API server running:** `curl http://127.0.0.1:5432/health` returns healthy  
✅ **Create deal:** Use dealflow-os.html "New Deal" button or curl POST  
✅ **Check persistence:** Page reload → deals still visible  
✅ **Update deal:** PUT request moves deal through pipeline  
✅ **Add notes:** POST to `/api/deals/:id/notes` creates note  
✅ **Agent tracking:** POST to `/api/deals/:id/agent-runs` logs execution  

---

## Configuration

### Environment Variables

```bash
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5433
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=changeme
export POSTGRES_DB=company_brain
```

Default values match above — only override if your setup differs.

### API Server Port

The API server runs on `127.0.0.1:5432` by default. To use a different port:

```bash
python3 _MCP/dealflow_postgres_api.py 9999
```

Then update `API_POSTGRES` in dealflow-os.html:

```javascript
const API_POSTGRES = "http://127.0.0.1:9999";
```

---

## Database Queries (Reference)

### Count all deals

```sql
SELECT COUNT(*) FROM deals;
```

### View deals by stage

```sql
SELECT stage, COUNT(*) FROM deals GROUP BY stage ORDER BY COUNT(*) DESC;
```

### Get deal with all notes and agent runs

```sql
SELECT d.*, 
       (SELECT COUNT(*) FROM deal_notes WHERE deal_id = d.id) as note_count,
       (SELECT COUNT(*) FROM agent_runs WHERE deal_id = d.id) as run_count
FROM deals d
WHERE d.id = 1;
```

### Find high-value deals (>$1M)

```sql
SELECT id, company_name, value, stage, created_at 
FROM deals 
WHERE value > 1000000 
ORDER BY value DESC;
```

### Recent agent activity

```sql
SELECT ar.deal_id, ar.agent_type, ar.status, ar.execution_time_ms, d.company_name
FROM agent_runs ar
JOIN deals d ON ar.deal_id = d.id
ORDER BY ar.created_at DESC
LIMIT 20;
```

---

## Troubleshooting

### "Database connection failed"

**Check:** PostgreSQL is running on port 5433

```bash
docker ps | grep postgres
# or
lsof -i :5433
```

**Fix:** Start PostgreSQL or update POSTGRES_PORT

### "Deal already exists" (duplicate company_id)

**Issue:** company_id is UNIQUE. If you create two deals with the same company_id, the second fails.

**Fix:** Use different company_id or clear the deals table:

```sql
TRUNCATE TABLE deals CASCADE;
```

### API returns 500 error

**Check:** Server logs in terminal window where dealflow_postgres_api.py is running

**Common causes:**
- PostgreSQL connection refused
- Invalid JSON in POST body
- Missing required fields

### Page reload loses new deals

**Check:** Confirm the API server is still running

**Issue:** If the server was stopped, newly created deals exist in PostgreSQL but the page reload will load fresh data from the Neo4j API. Restart the server to persist new deals going forward.

---

## Authority & Next Steps

- **Control Plane:** DealFlowOS Engine (CP-028 Collaboration)
- **Layer:** Execution (Layer 11)
- **Status:** ✅ Ready for production use

**Next:**
1. Wire agent execution to log agent runs via API
2. Build deal analytics dashboard from PostgreSQL
3. Sync deal stage changes back to Neo4j for knowledge graph integration
4. Set up automated backups of deals table
