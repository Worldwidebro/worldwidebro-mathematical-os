# Chat2DB Deployment Guide

**Status:** Ready to deploy  
**Target:** Mac Studio (100.87.214.70) via Tailscale  
**Access:** http://100.87.214.70:8080  
**Config:** See docker-compose.yml (scratchpad)

---

## Quick Start (5 minutes)

### 1. Copy docker-compose to Mac Studio

```bash
scp /private/tmp/claude-501/-Volumes-LaCie/7f55f05f-c069-4a7b-83c7-bcd128f72795/scratchpad/chat2db-docker-compose.yml macstudio:~/chat2db-docker-compose.yml
```

### 2. Start services

```bash
ssh macstudio
docker-compose -f ~/chat2db-docker-compose.yml up -d
```

### 3. Verify health

```bash
docker-compose ps
# Should show: chat2db, postgres HEALTHY
```

### 4. Access Chat2DB

**From this machine (via Tailscale):**
```bash
open http://100.87.214.70:8080
```

**Login:**
- User: `admin`
- Password: `ventures2026`

---

## Database Connections (Pre-configured)

### PostgreSQL (TwentyHQ)
- Host: `postgres` (Docker internal)
- Port: 5432
- Database: `twenty`
- User: `postgres`
- Password: `postgres`

### DuckDB (Analytics)
- Path: `/data/worldwidebro_os.duckdb`
- Mount: `/Volumes/T7 Shield/.../databases/` (read-only)

### MySQL (Optional)
- Pre-configured in Chat2DB, not yet wired

---

## LLM Configuration

**Provider:** FreeLLMAPI (your local free-tier aggregator)  
**Endpoint:** http://100.121.17.63:8000  
**Model:** gpt-3.5-turbo  
**Cost:** FREE (Gemini, Groq, Mistral, Cerebras, GitHub Models)

Chat2DB will use FreeLLMAPI for all SQL generation, optimization, and explanations.

---

## Features Enabled

- ✅ Natural language → SQL generation
- ✅ SQL optimization suggestions
- ✅ Schema visualization
- ✅ Query explanations
- ✅ Data export (CSV, Excel, JSON)
- ✅ ERD diagrams
- ✅ Team collaboration

---

## Example Queries

Once deployed, you can ask Chat2DB:

**Venture Analytics:**
> "Show all construction ventures with revenue > $50K in the last month"

**Staffing:**
> "Which recruiters have the highest placement rate?"

**Pipeline:**
> "Generate SQL for MRR by sector"

**Real Estate:**
> "Find properties that haven't been updated in 90 days"

Chat2DB generates the SQL automatically.

---

## Troubleshooting

### Chat2DB won't start

```bash
ssh macstudio
docker-compose logs chat2db
# Check for port conflicts (8080 in use) or volume mounts
```

### Can't connect to PostgreSQL

```bash
# Verify postgres is running
docker-compose ps postgres

# Test connection from Chat2DB container
docker exec civos_chat2db psql -h postgres -U postgres -d twenty -c "SELECT 1"
```

### DuckDB mount failing

Ensure `/Volumes/T7 Shield/.../databases/worldwidebro_os.duckdb` exists on Mac Studio with correct permissions.

```bash
ssh macstudio
ls -la /Volumes/T7\ Shield/.../databases/worldwidebro_os.duckdb
```

### FreeLLMAPI not responding

Verify FreeLLMAPI is running on MacBook Air:

```bash
curl http://100.121.17.63:8000/health
# Should return 200 OK
```

---

## Monitoring

**View logs:**
```bash
ssh macstudio
docker-compose logs -f chat2db
```

**Check health:**
```bash
curl http://100.87.214.70:8080/api/health
```

**Monitor resources:**
```bash
ssh macstudio
docker stats civos_chat2db
```

---

## Next Steps

1. **Deploy** (5 min) — Run docker-compose up
2. **Test** (5 min) — Login and run a simple query
3. **Integrate** — Wire Chat2DB to venture agents
4. **Fractal Skills** — Create Chat2DB skills for each sector

---

## Integration with AI Boss OS

Chat2DB becomes the **Database Intelligence Layer** in your OS:

```
Venture Agent
    ↓
"Query construction ventures"
    ↓
Chat2DB (NL → SQL)
    ↓
PostgreSQL / DuckDB
    ↓
Results + Visualization
```

All without manual SQL writing.

---

**Created:** 2026-07-25  
**Status:** Ready for deployment  
**Owner:** You (via Tailscale)
