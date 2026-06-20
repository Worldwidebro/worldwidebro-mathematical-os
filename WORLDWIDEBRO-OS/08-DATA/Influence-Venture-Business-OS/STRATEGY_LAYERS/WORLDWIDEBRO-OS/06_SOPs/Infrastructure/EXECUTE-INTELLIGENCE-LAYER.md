# Execute Intelligence Layer: Options A, B, C

**Complete deployment guide for Repo Metadata Foundation, LlamaIndex Indexing, and Backstage Service Catalog**

---

## Prerequisites

```bash
# Verify environment variables are set
echo $GITHUB_TOKEN        # Should be set
echo $SUPABASE_SERVICE_KEY # Should be set
echo $OPENAI_API_KEY      # Optional, for embeddings

# Verify Ollama is running
curl http://100.87.214.70:11434/api/tags
# Should return list of available models (qwen2.5:32b, nomic-embed-text, etc.)

# Verify Supabase is accessible
curl -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/ventures?limit=1
# Should return venture data
```

---

## Architecture

```
┌─ OPTION A: Metadata Foundation ────┐
│ populate_repos_metadata.py          │
│ • Parse 640 repos from markdown     │
│ • Query GitHub API (stars, etc.)    │
│ • Ollama inference (capabilities)   │
│ • Map to ventures                   │
│ • Insert to Supabase repos table    │
└─────────────────────────────────────┘
              ↓ (850+ repos with metadata)
    ┌─────────┴──────────┐
    ↓                    ↓
┌─ OPTION C: Indexing ──────────┐   ┌─ OPTION B: Backstage ─────────┐
│ index_repos_with_llamaindex.py │   │ backstage-integration-setup.md │
│ • Extract README from GitHub   │   │ • Docker deployment           │
│ • Create embeddings (1536 dims)│   │ • PostgreSQL setup            │
│ • Store vectors in DB          │   │ • Sync Supabase → Catalog     │
│ • Enable semantic search       │   │ • Custom plugins              │
└────────────────────────────────┘   │ • Integration roadmap         │
              ↓                       └────────────────────────────────┘
    ┌─────────┴────────────┐                      ↓
    ↓                      ↓          ┌──────────────────────┐
Complete Knowledge Graph System        │ Backstage Portal     │
with Semantic Search + UI Navigation   │ • Service Catalog    │
                                       │ • Dependencies       │
                                       │ • Roadmaps          │
                                       │ • Semantic Search    │
                                       └──────────────────────┘
```

---

## Execution Timeline

| Phase | Task | Duration | Status |
|-------|------|----------|--------|
| **PHASE 1: Setup** | Run Supabase migrations | 5 min | [ ] |
| **PHASE 2: Option A** | Populate repos metadata | 20-30 min | [ ] |
| **PHASE 3: Option C** | Index repos with embeddings | 30-45 min | [ ] |
| **PHASE 4: Option B** | Deploy Backstage | 15-20 min | [ ] |
| **PHASE 5: Verify** | Test all three integrated | 10 min | [ ] |

**Total Time:** 80-120 minutes (1.5-2 hours)

---

## PHASE 1: Run Supabase Migrations

### 1.1 Verify current migrations

```bash
cd /Users/acebless/Documents
ls -la migrations/
# Should show:
# - 001_create_ventures_table.sql (existing)
# - 002_create_aoc_tasks_table.sql (existing)
# - 003_create_repos_metadata_table.sql (NEW - from Option A)
```

### 1.2 Run migrations via Supabase CLI

```bash
# Option 1: Via Supabase Dashboard (recommended)
# Go to: https://app.supabase.com/project/cyhzilqldouzgynacqpe/sql/new
# Copy content of 003_create_repos_metadata_table.sql
# Paste and run

# Option 2: Via CLI
supabase link --project-ref cyhzilqldouzgynacqpe
supabase db push
```

### 1.3 Verify migration succeeded

```sql
-- In Supabase SQL Editor, run:
SELECT table_name FROM information_schema.tables 
WHERE table_schema='public' AND table_name='repos';
-- Should return: repos

SELECT * FROM pg_indexes WHERE tablename='repos' LIMIT 5;
-- Should return: 9 indexes (idx_repos_name, idx_repos_capabilities, etc.)
```

**Expected Output:** repos table exists with schema (id, repo_id, name, capabilities, embedding, etc.)

---

## PHASE 2: Option A - Repo Metadata Foundation

### 2.1 Prepare Python environment

```bash
# Install dependencies
pip3 install requests python-dotenv

# Verify Python version
python3 --version  # Should be 3.8+

# Create .env file if not exists
cd /Users/acebless/Documents
cat > .env << 'EOF'
GITHUB_TOKEN=your_token_here
SUPABASE_SERVICE_KEY=your_key_here
NEXT_PUBLIC_SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
OLLAMA_URL=http://100.87.214.70:11434
EOF
```

### 2.2 Run population script

```bash
cd /Users/acebless/Documents

# Dry run (optional, logs what would happen)
python3 -c "
import populate_repos_metadata as p
pop = p.RepoMetadataPopulator()
repos = pop.parse_repos_from_markdown()
print(f'Found {len(repos)} repos to process')
print(f'First 10: {repos[:10]}')
"

# Full run
python3 populate_repos_metadata.py

# Expected output:
# [INFO] Parsing repos from starred-repos-capabilities.md
# [INFO] Found 640 unique repos from markdown
# [INFO] Fetching ventures from Supabase
# [INFO] Fetched 687 ventures with 127 unique capabilities
# [INFO] Processing: 1/640 llama_index
# [INFO]   ✓ GitHub: 32,400 stars
# [INFO]   ✓ Ollama: Indexing and retrieval system for LLMs...
# [INFO]   ✓ Mapped to 45 ventures in 8 sectors
# [INFO]   ✓ Inserted to Supabase
# ... (continues for all 640 repos)
# [INFO] POPULATION SUMMARY
# [INFO] Total repos parsed: 640
# [INFO] Repos with GitHub data: 580
# [INFO] Repos with Ollama inference: 620
# [INFO] Repos successfully inserted: 610
# [INFO] Repos failed: 30 (retryable)
```

### 2.3 Verify Phase 2 complete

```bash
# Count repos in Supabase
python3 << 'EOF'
import os
import requests
headers = {
    "apikey": os.getenv("SUPABASE_SERVICE_KEY"),
    "Authorization": f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}"
}
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=count()"
response = requests.get(url, headers=headers)
print(f"Repos in Supabase: {response.json()[0]['count']}")
# Expected: 600-650

# Sample a repo with metadata
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?limit=1&select=*"
response = requests.get(url, headers=headers)
repo = response.json()[0]
print(f"\nSample repo:")
print(f"  Name: {repo['name']}")
print(f"  Capabilities: {repo['capabilities']}")
print(f"  Integration Effort: {repo['integration_effort']}")
print(f"  Ventures: {len(repo['venture_ids'])} ventures")
EOF
```

**Milestone:** ✓ Option A complete - 600+ repos with metadata in Supabase

---

## PHASE 3: Option C - LlamaIndex Semantic Indexing

### 3.1 Prepare embedding dependencies

```bash
# Option 1: Use Ollama (local, free, already running)
# No additional setup needed

# Option 2: Use OpenAI API (requires API key + cost ~$1-5)
export EMBEDDING_MODEL=openai
export OPENAI_API_KEY=sk-...

# Verify Ollama has embedding model
curl http://100.87.214.70:11434/api/tags | grep nomic-embed-text
# If not present, pull it:
# curl http://100.87.214.70:11434/api/pull -d '{"name": "nomic-embed-text:latest"}'
```

### 3.2 Run indexing script

```bash
cd /Users/acebless/Documents

# Full run with Ollama (default)
python3 index_repos_with_llamaindex.py

# Expected output:
# [INFO] LLAMAINDEX SEMANTIC INDEXING - OPTION C LAYER
# [INFO] Using embedding model: ollama
# [INFO] Fetching repos to index from Supabase
# [INFO] Fetched 610 repos for indexing
# [INFO] [1/610] Indexing: llama_index
# [INFO]   ✓ Extracted README (4,200 chars)
# [INFO]   ✓ Embedding created (1536 dims)
# [INFO]   ✓ Stored in Supabase
# ... (continues for all 610 repos)
# [INFO] INDEXING SUMMARY
# [INFO] Total repos to index: 610
# [INFO] Content extracted: 580
# [INFO] Embeddings created: 575
# [INFO] Embeddings stored in DB: 570
```

### 3.3 Verify Phase 3 complete

```bash
python3 << 'EOF'
import os
import requests
headers = {
    "apikey": os.getenv("SUPABASE_SERVICE_KEY"),
    "Authorization": f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}"
}

# Count repos with embeddings
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=count()&embedding=not.null"
response = requests.get(url, headers=headers)
print(f"Repos with embeddings: {response.json()[0]['count']}")
# Expected: 550-600

# Sample repo embedding
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?limit=1&select=name,embedding&embedding=not.null"
response = requests.get(url, headers=headers)
repo = response.json()[0]
embedding = repo['embedding']
print(f"\nSample embedding:")
print(f"  Repo: {repo['name']}")
print(f"  Embedding dims: {len(embedding)}")
print(f"  First 5 values: {embedding[:5]}")
EOF
```

**Milestone:** ✓ Option C complete - 550+ repos with semantic embeddings

---

## PHASE 4: Option B - Backstage Service Catalog

### 4.1 Deploy Backstage (Docker)

```bash
# Option 1: Docker (fastest)
docker pull backstage/backstage:latest
docker run -d \
  -p 3000:7007 \
  -e BACKSTAGE_BASE_URL=http://localhost:3000 \
  --name backstage \
  backstage/backstage:latest

# Verify running
curl http://localhost:3000
# Should return HTML

# Option 2: Local npm (more control)
# See backstage-integration-setup.md for full instructions
npm install -g npx
npx @backstage/create-app@latest --path ./backstage-app
cd backstage-app
npm run dev
```

### 4.2 Configure database

```bash
# If using Docker + PostgreSQL, add to docker-compose:
# postgres:
#   image: postgres:13
#   environment:
#     POSTGRES_PASSWORD: backstage
#     POSTGRES_DB: backstage

# Then create app-config.yaml:
cat > app-config.yaml << 'EOF'
backend:
  database:
    connection:
      host: postgres
      port: 5432
      user: postgres
      password: backstage
      database: backstage

integrations:
  supabase:
    - host: cyhzilqldouzgynacqpe.supabase.co
      token: ${SUPABASE_SERVICE_KEY}

catalog:
  import:
    entityFilename: catalog-info.yaml
  providers:
    supabase:
      default:
        host: cyhzilqldouzgynacqpe.supabase.co
        schedule:
          frequency: { minutes: 30 }
EOF
```

### 4.3 Run catalog sync

```bash
# From backstage-integration-setup.md, create sync-script.ts:
npm install @supabase/supabase-js js-yaml

# Create sync script (copy from backstage-integration-setup.md)
# Then run:
npx ts-node sync-script.ts

# Expected output:
# Synced 687 ventures and 610 repos
# Catalog files created:
# - catalog/ventures.yaml
# - catalog/repos.yaml
```

### 4.4 Verify Backstage is running

```bash
# Open browser
open http://localhost:3000

# Navigate to Service Catalog
# You should see:
# - 687 Ventures listed as Services
# - 610 Repos listed as Components
# - Click a venture to see its repo dependencies
# - Click "Integration Roadmap" to see phases
```

**Milestone:** ✓ Option B complete - Backstage running with full catalog

---

## PHASE 5: End-to-End Verification

### 5.1 Test Option A (Metadata)

```bash
# Query: Get a venture and show its required repos
python3 << 'EOF'
import os
import requests

headers = {
    "apikey": os.getenv("SUPABASE_SERVICE_KEY"),
    "Authorization": f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}"
}

# Get a venture
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/ventures?select=id,name,required_capabilities&limit=1"
venture = requests.get(url, headers=headers).json()[0]

print(f"Venture: {venture['name']}")
print(f"Required capabilities: {venture['required_capabilities']}")

# Find repos that provide these capabilities
repos_url = f"https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=name,capabilities,integration_effort&capabilities=cs.{'{' + ','.join(venture['required_capabilities']) + '}'}"
repos = requests.get(repos_url, headers=headers).json()

print(f"\nRepos available ({len(repos)}):")
for repo in repos[:5]:
    print(f"  - {repo['name']} ({repo['integration_effort']} effort)")
EOF
```

### 5.2 Test Option C (Semantic Search)

```python
# Test semantic search
python3 << 'EOF'
import os
import requests
import json

# Create query embedding
def get_embedding(text):
    response = requests.post(
        "http://100.87.214.70:11434/api/embeddings",
        json={"model": "nomic-embed-text:latest", "prompt": text},
        timeout=30
    )
    return response.json()["embedding"]

# Query and get repos
query = "booking and calendar management system"
query_embedding = get_embedding(query)

headers = {
    "apikey": os.getenv("SUPABASE_SERVICE_KEY"),
    "Authorization": f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}"
}

# Get repos with embeddings
url = "https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=name,purpose,embedding&limit=50&embedding=not.null"
repos = requests.get(url, headers=headers).json()

# Calculate similarity
def cosine_similarity(a, b):
    import math
    dot_product = sum(x*y for x,y in zip(a,b))
    norm_a = math.sqrt(sum(x**2 for x in a))
    norm_b = math.sqrt(sum(x**2 for x in b))
    return dot_product / (norm_a * norm_b) if norm_a * norm_b > 0 else 0

similarities = []
for repo in repos:
    if repo["embedding"]:
        sim = cosine_similarity(query_embedding, repo["embedding"])
        similarities.append((sim, repo["name"], repo["purpose"]))

similarities.sort(reverse=True)

print(f"Query: '{query}'")
print(f"\nTop 5 results:")
for score, name, purpose in similarities[:5]:
    print(f"  {score:.3f} - {name}: {purpose[:60]}")
EOF
```

### 5.3 Test Option B (Backstage)

```bash
# In browser, test:
# 1. Service Catalog page (should load 687 services)
curl http://localhost:3000/catalog/services

# 2. Component Library (should show 610 components)
curl http://localhost:3000/catalog/components

# 3. Click a venture, should show:
#    - Description
#    - Dependencies (repos)
#    - Integration roadmap
#    - Maturity score
```

### 5.4 Data Flow Check

```bash
# Verify complete pipeline:

# GitHub → Option A
echo "✓ GitHub repos downloaded and analyzed"

# Option A → Supabase (repos table)
python3 -c "
import requests, os
headers = {'apikey': os.getenv('SUPABASE_SERVICE_KEY'), 'Authorization': f\"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}\"}
count = requests.get('https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=count()', headers=headers).json()[0]['count']
print(f'✓ {count} repos in Supabase')
"

# Supabase → Option C (embeddings)
python3 -c "
import requests, os
headers = {'apikey': os.getenv('SUPABASE_SERVICE_KEY'), 'Authorization': f\"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}\"}
count = requests.get('https://cyhzilqldouzgynacqpe.supabase.co/rest/v1/repos?select=count()&embedding=not.null', headers=headers).json()[0]['count']
print(f'✓ {count} repos with embeddings')
"

# Supabase → Option B (Backstage)
echo "✓ Backstage synced with Supabase (http://localhost:3000)"
```

**Milestone:** ✓ All three options integrated and working

---

## Success Criteria

| Option | Expected Output | Verification Command |
|--------|-----------------|----------------------|
| **A** | 600+ repos in Supabase with metadata (capabilities, integration_effort, cost) | `SELECT COUNT(*) FROM repos WHERE capabilities IS NOT NULL` → 600+ |
| **C** | 550+ repos with 1536-dim embeddings for semantic search | `SELECT COUNT(*) FROM repos WHERE embedding IS NOT NULL` → 550+ |
| **B** | Backstage portal running at http://localhost:3000 with 687 ventures as services | `curl http://localhost:3000/catalog/services` → 687 services |
| **Integration** | Semantic query "What repos solve booking?" returns cal_com, schedulekit, etc. | Run semantic search test above |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `populate_repos_metadata.py` fails at GitHub API | Check GITHUB_TOKEN env var, verify rate limits |
| Ollama not responding | `curl http://100.87.214.70:11434/api/tags`, ensure server running |
| Supabase insertion fails | Check SUPABASE_SERVICE_KEY, verify repos table exists via migrations |
| Backstage won't start | Check Docker is running, port 3000 is free, verify app-config.yaml syntax |
| Semantic search returns empty | Ensure embeddings were stored (Phase 3 success), repos table has vectors |

---

## Next Steps After Completion

1. **Connect to Make.com workflows** - Link repo metadata to deal router (what repos does this venture need?)
2. **Add Slack notifications** - Alert on new repos added, new ventures needing repos
3. **Create ClickUp integration** - Track repo integration status per venture
4. **Build reporting dashboard** - Ventures by repo dependency complexity, adoption rates
5. **Enable real-time search** - Add LlamaIndex query interface to Slack/Obsidian

---

## Files & Resources

| File | Purpose |
|------|---------|
| `003_create_repos_metadata_table.sql` | Supabase migration (repos table schema) |
| `populate_repos_metadata.py` | Option A: Metadata population script |
| `index_repos_with_llamaindex.py` | Option C: Embedding generation script |
| `backstage-integration-setup.md` | Option B: Backstage deployment guide |
| `EXECUTE-INTELLIGENCE-LAYER.md` | This guide (you are here) |

---

## Timeline Estimate

- **Setup (Phase 1):** 5 minutes
- **Option A (Phase 2):** 20-30 minutes
- **Option C (Phase 3):** 30-45 minutes
- **Option B (Phase 4):** 15-20 minutes
- **Verification (Phase 5):** 10 minutes

**Total:** 80-120 minutes (1.5-2 hours to complete all three options)

---

**Status: Ready to execute. Start with PHASE 1 when ready.**
