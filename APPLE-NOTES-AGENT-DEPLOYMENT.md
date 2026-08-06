---
name: APPLE-NOTES-AGENT-DEPLOYMENT
title: Apple Notes Ingestion Agent — Deployment Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Apple Notes Ingestion Agent — Deployment Guide

**Status:** Production-ready  
**Components:** 3 files (Python agent, TypeScript webhook handler, unit tests)  
**Last Updated:** 2026-08-05  

---

## Overview

The Apple Notes ingestion agent automatically:
1. Receives notes from Apple Notes via Zapier/Trigger.dev webhook
2. Classifies using Claude (venture, type: strategic/operational/learning, entities, actions)
3. Stores in Supabase operational table (`apple_notes_inbox`)
4. Updates Neo4j knowledge graph (Note → Venture, Note → Entity relationships)
5. Embeds semantically in Qdrant for vector search
6. Routes to specialized agents (ArchitectureAgent, ExecutionAgent, ResearchAgent, etc.)
7. Syncs back to Obsidian vault
8. Logs outcomes to learning table for improvement

**Pipeline:** Ingest → Classify → Supabase → Neo4j → Qdrant → Dispatch → Obsidian → Learning

---

## Prerequisites

- **Python 3.12+** with uv package manager
- **Node.js 18+** (for TypeScript webhook handler)
- **Local services running:**
  - Supabase (port 54321)
  - Neo4j (port 7687)
  - Qdrant (port 6333)
  - Claude API key (`ANTHROPIC_API_KEY`)

Verify:
```bash
# Supabase
psql -h localhost -U postgres -d ventures -c "SELECT COUNT(*) FROM apple_notes_inbox;"

# Neo4j
curl http://localhost:7474 -u neo4j:ventures2026

# Qdrant
curl http://localhost:6333/health

# Claude API
echo $ANTHROPIC_API_KEY | wc -c  # Should be >50
```

---

## Installation

### 1. Python Agent Setup

```bash
cd ~/Documents

# Create venv
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install \
  langgraph \
  anthropic \
  supabase \
  neo4j \
  qdrant-client \
  pydantic

# Set environment variables
export ANTHROPIC_API_KEY="sk-..."
export SUPABASE_URL="http://localhost:54321"
export SUPABASE_KEY="eyJhbGciOiJIUzI1NiIs..."
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="ventures2026"
export QDRANT_URL="http://localhost:6333"

# Test agent
python -m apple_notes_agent  # Should see: "✓ Processed note"
```

### 2. Webhook Handler Setup (TypeScript)

```bash
# Install dependencies
npm install zod node-fetch

# Create Next.js API route
mkdir -p pages/api/webhooks
cp trigger_webhook_handler.ts pages/api/webhooks/apple-notes.ts

# Or use Express.js
npm install express
# See Express example at end of trigger_webhook_handler.ts
```

### 3. Database Schema

**Supabase:**
```sql
-- Create tables
CREATE TABLE apple_notes_inbox (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT NOT NULL,
  venture_id TEXT,
  note_type TEXT,
  entities JSONB DEFAULT '[]',
  actions JSONB DEFAULT '[]',
  created_at TIMESTAMP DEFAULT NOW(),
  processed BOOLEAN DEFAULT FALSE
);

CREATE TABLE apple_notes_learning (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  note_id TEXT NOT NULL,
  venture_predicted TEXT,
  note_type_predicted TEXT,
  agents_dispatched JSONB DEFAULT '[]',
  entities_extracted INT,
  actions_identified INT,
  error_count INT,
  processing_time TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_apple_notes_venture ON apple_notes_inbox(venture_id);
CREATE INDEX idx_apple_notes_type ON apple_notes_inbox(note_type);
CREATE INDEX idx_learning_venture ON apple_notes_learning(venture_predicted);
```

**Neo4j:**
```cypher
CREATE CONSTRAINT note_id_unique IF NOT EXISTS
FOR (n:Note) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT venture_id_unique IF NOT EXISTS
FOR (v:Venture) REQUIRE v.id IS UNIQUE;

CREATE CONSTRAINT entity_name_unique IF NOT EXISTS
FOR (e:Entity) REQUIRE e.name IS UNIQUE;
```

**Qdrant:**
```bash
curl -X PUT http://localhost:6333/collections/apple_notes \
  -H "Content-Type: application/json" \
  -d '{
    "vectors": {
      "size": 1536,
      "distance": "Cosine"
    }
  }'
```

---

## Configuration

### Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=sk-...
SUPABASE_URL=http://localhost:54321
SUPABASE_KEY=eyJh...
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ventures2026
QDRANT_URL=http://localhost:6333

# Optional (webhook handler)
AGENT_API_URL=http://localhost:8000
AGENT_API_KEY=...  # For authentication
WEBHOOK_PORT=3000
TRIGGER_SIGNING_SECRET=...  # From Trigger.dev
```

### OmniRoute Integration (LLM Dispatch)

The agent currently uses Claude via Anthropic API. To integrate OmniRoute for dynamic LLM routing:

1. **Check OmniRoute capabilities** in your repos:
   ```bash
   ls ~/Documents/OmniRoute
   ```

2. **Replace Claude calls** in `apple_notes_agent.py` line ~81:
   ```python
   # Current (static):
   from anthropic import Anthropic
   response = claude_client.messages.create(model="claude-opus-5", ...)

   # With OmniRoute (dynamic routing):
   from omniroute import OmniRoute
   router = OmniRoute()
   response = router.query(prompt, task="reasoning")
   ```

3. **Configure OmniRoute** in `.env`:
   ```bash
   OMNIROUTE_API_KEY=...
   OMNIROUTE_MODELS=claude-opus-5,gpt-4,command-r-plus
   ```

---

## Running the Agent

### Manual Processing

```python
import asyncio
from apple_notes_agent import process_note

result = asyncio.run(process_note(
    "LT-005 dispatch needs API wiring by Friday",
    note_id="note-2026-08-05-001"
))

print(f"Venture: {result.venture_id}")
print(f"Type: {result.note_type}")
print(f"Actions: {result.actions}")
```

### Via Webhook (Trigger.dev/Zapier)

1. **Configure Trigger.dev:**
   - Create workflow: "Apple Notes → Webhook"
   - Webhook URL: `https://your-domain.com/webhook/apple-notes`
   - Payload: `{ "note_content": "...", "note_id": "...", "source": "apple_notes" }`

2. **Test webhook:**
   ```bash
   curl -X POST http://localhost:3000/webhook/apple-notes \
     -H "Content-Type: application/json" \
     -d '{
       "note_content": "LT-005 needs dispatch platform",
       "note_id": "test-001",
       "source": "apple_notes"
     }'
   # Expect: 202 Accepted
   ```

---

## Testing

### Unit Tests

```bash
# Run all tests
pytest test_apple_notes_agent.py -v

# Run specific test class
pytest test_apple_notes_agent.py::TestClassification -v

# Run with coverage
pytest test_apple_notes_agent.py --cov=apple_notes_agent
```

### Integration Test

```python
# test_apple_notes_agent.py::TestIntegration::test_full_pipeline
# Processes a note through entire pipeline with mocked services
pytest test_apple_notes_agent.py::TestIntegration -v
```

### End-to-End Test

```bash
# 1. Start all services
docker-compose up -d

# 2. Populate test note
python -c "
import asyncio
from apple_notes_agent import process_note
asyncio.run(process_note('Test note for E2E validation'))
"

# 3. Verify in Supabase
psql -h localhost -U postgres -d ventures -c \
  "SELECT id, venture_id, note_type FROM apple_notes_inbox ORDER BY created_at DESC LIMIT 1;"

# 4. Verify in Neo4j
curl -s http://localhost:7474/db/neo4j/cypher \
  -u neo4j:ventures2026 \
  -d "MATCH (n:Note) RETURN COUNT(n);"

# 5. Verify in Qdrant
curl -s http://localhost:6333/collections/apple_notes/points | jq '.result.points | length'
```

---

## Deployment

### To Vercel (Next.js)

```bash
# 1. Copy webhook handler
cp trigger_webhook_handler.ts pages/api/webhooks/apple-notes.ts

# 2. Set environment variables in Vercel dashboard:
# - AGENT_API_URL (your Python API endpoint)
# - AGENT_API_KEY
# - TRIGGER_SIGNING_SECRET

# 3. Deploy
vercel deploy
```

### To Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN pip install langgraph anthropic supabase neo4j qdrant-client pydantic

COPY apple_notes_agent.py .

EXPOSE 8000

CMD ["python", "-m", "apple_notes_agent"]
```

### To Railway

```bash
railway add python
railway up
# Set env vars in dashboard
```

---

## API Integration

### Python API Wrapper

```python
# api_wrapper.py
from fastapi import FastAPI
from apple_notes_agent import process_note

app = FastAPI()

@app.post("/process-note")
async def api_process_note(content: str, note_id: str = None):
    result = await process_note(content, note_id)
    return {
        "note_id": result.note_id,
        "venture_id": result.venture_id,
        "note_type": result.note_type,
        "entities": result.entities,
        "actions": result.actions,
        "errors": result.errors,
    }
```

Run:
```bash
pip install fastapi uvicorn
uvicorn api_wrapper:app --reload
```

---

## Monitoring

### Log Output

```bash
# Check logs in real-time
tail -f /tmp/apple_notes_agent.log
```

### Processing Status

```bash
# Count notes processed today
psql -h localhost -U postgres -d ventures -c \
  "SELECT COUNT(*), note_type FROM apple_notes_inbox \
   WHERE created_at > NOW() - INTERVAL '24 hours' \
   GROUP BY note_type;"

# Check errors
psql -h localhost -U postgres -d ventures -c \
  "SELECT note_id, error_count FROM apple_notes_learning \
   WHERE error_count > 0 ORDER BY processing_time DESC LIMIT 10;"
```

### Learning Loop Metrics

```bash
# Extract accuracy metrics
psql -h localhost -U postgres -d ventures -c \
  "SELECT 
     COUNT(*) as total_processed,
     ROUND(100.0 * COUNT(CASE WHEN error_count = 0 THEN 1 END) / COUNT(*), 1) as success_rate,
     AVG(entities_extracted) as avg_entities,
     AVG(actions_identified) as avg_actions
   FROM apple_notes_learning
   WHERE processing_time > NOW() - INTERVAL '7 days';"
```

---

## Troubleshooting

### Agent Not Processing Notes

Check services and env vars:
```bash
docker ps | grep neo4j  # Should show running
echo $ANTHROPIC_API_KEY  # Should not be empty
python apple_notes_agent.py  # Test run
```

### Webhook Timeout

Agent returns 202 Accepted immediately; processing happens async. Check if backend is running:
```bash
curl http://localhost:8000/health
```

### Database Connection Errors

Verify services:
```bash
docker-compose restart neo4j supabase qdrant
```

---

## Files

| File | Purpose |
|------|---------|
| `apple_notes_agent.py` | Core LangGraph agent (8 nodes, 8 edges) |
| `trigger_webhook_handler.ts` | Webhook endpoint for Trigger.dev |
| `test_apple_notes_agent.py` | 30+ unit tests with mocks |
| This guide | Deployment reference |

---

**Ready to deploy.** Follow "Installation" section, then test with the included unit tests.
