# Move 2a: GitHub Repo Institutional Classification

## Overview
Bulk classify 853 owned + 667 starred repos into institutional ontology categories (VCC, CI, EXP, ARC, COMP, TOOL, REF, UNCATEGORIZED) using GitHub API + Claude Opus + Supabase.

**Estimated runtime:** 2 hours  
**Batch size:** 20 repos per LLM call  
**Total batches:** ~74 (1,520 repos ÷ 20)  
**Rate limits:** GitHub API (5000 req/hr), Anthropic API (standard limits)

---

## Prerequisites

### Environment Variables
Add to `.env`:

```bash
# GitHub (user token with repo read access)
GITHUB_TOKEN=github_pat_xxxxx

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Supabase (already configured)
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=eyJhbGc...
```

**Get GitHub Token:**
1. Go to https://github.com/settings/personal-access-tokens/new
2. Select scopes: `read:user`, `public_repo` (minimum)
3. Create and copy token
4. Paste into `.env`

**Anthropic API Key:**
- Available at https://console.anthropic.com/
- Copy and paste into `.env`

### Python Dependencies
```bash
pip install supabase requests anthropic
```

---

## Execution

### Step 1: Run the classification script
```bash
python3 classify_repos_institutional.py
```

**What it does:**
1. Ensures `repo_institutional_index` table exists in Supabase (creates if missing)
2. Fetches all owned repos (paginated, ~15-30s)
3. Fetches all starred repos (paginated, ~15-30s)
4. Batches repos into groups of 20
5. For each batch:
   - Sends to Claude Opus with ontology prompt
   - Parses JSON response
   - Inserts into Supabase (upsert to avoid duplicates)
6. Prints distribution stats (VCC/CI/EXP/ARC/COMP/TOOL/REF/UNCATEGORIZED)

**Output:**
```
=== Summary ===
Owned repos: 853
Starred repos: 667
Total classified: 1520
Total inserted: 1520

=== Classification Distribution ===
  VCC: 42
  CI: 31
  EXP: 18
  ARC: 27
  COMP: 156
  TOOL: 892
  REF: 347
  UNCATEGORIZED: 7
```

### Step 2: Review high-uncertainty classifications
```sql
-- Query Supabase: find repos that need human review
SELECT full_name, institutional_function, confidence, reasoning_keywords
FROM repo_institutional_index
WHERE needs_human_review = true
OR confidence < 0.7
ORDER BY confidence ASC;
```

Expected: ~50-100 repos marked for human review (mostly UNCATEGORIZED or confidence < 0.7)

### Step 3: Trigger deep indexing for VCC repos
Once you've reviewed uncertain classifications, mark validated VCC repos for ingestion:

```sql
-- Mark VCC repos as ready for deep embedding + knowledge graph sync
UPDATE repo_institutional_index
SET ingest_status = 'ingested'
WHERE institutional_function = 'VCC'
AND needs_human_review = false
AND confidence > 0.8;
```

This signals Task 13 (LightRAG) to:
- Fetch repository source code
- Generate semantic embeddings
- Ingest into knowledge graph as "Venture-Critical Core" nodes

---

## Schema Reference

**Columns created by script:**
| Field | Type | Notes |
|-------|------|-------|
| `full_name` | TEXT | Unique identifier (owner/repo) |
| `owner_type` | TEXT | 'owned' or 'starred' |
| `institutional_function` | ENUM | VCC, CI, EXP, ARC, COMP, TOOL, REF, UNCATEGORIZED |
| `confidence` | FLOAT | 0.0-1.0 classification certainty |
| `reasoning_keywords` | TEXT[] | Justification (e.g. ["production", "core", "deployed"]) |
| `suggested_venture` | TEXT | Which venture this repo serves (if applicable) |
| `is_dependency_of` | TEXT[] | List of venture IDs that depend on this repo |
| `needs_human_review` | BOOLEAN | true if confidence < 0.7 or ambiguous |
| `ingest_status` | ENUM | pending → ingested → skipped → quarantined |
| `embedding` | VECTOR(1536) | Semantic embedding (populated by Task 13) |

**Views created:**
- `venture_active_repos`: Filters to VCC + CI repos with ingest_status='pending' (ready for deep indexing)

---

## Troubleshooting

### GitHub API rate limit exceeded
- Reduce batch size to 10 repos/batch
- Reduce concurrent requests (script already rate-limits between batches)
- Wait 1 hour and retry

### Claude API rate limit exceeded
- Script includes 1-second delays between batches
- If still hitting limits, add longer delay: change `time.sleep(1)` to `time.sleep(5)`

### "Table doesn't exist" error
- Script auto-creates table if missing
- If creation fails, ensure pgvector extension is enabled:
  ```sql
  CREATE EXTENSION IF NOT EXISTS vector;
  ```

### JSON parse error from LLM response
- Claude occasionally wraps output in markdown code blocks
- Script handles this, but if it fails, check console output for malformed JSON
- Retry that batch manually (script is idempotent via upsert)

---

## Next Steps (Move 3)

After Move 2a completes:

1. **Move 3 (Week 0, Day 3):** Human Review Interface
   - Query repos with `needs_human_review = true`
   - Manual reclassification for edge cases
   - Set `ingest_status = 'ingested'` for validated repos

2. **Phase 2 (Week 1+):** Knowledge Graph Integration
   - Task 13: Sync VCC repos into LightRAG
   - Task 13.1: Sync COMP/TOOL starred repos into competitive monitoring feeds
   - Task 14: Build Graphify UI with classification coloring + economic topology

3. **Phase 3 (Week 2+):** Agent Integration
   - Agents query institutional index via Graphify
   - Red-team governance: validate agent decisions against institutional taxonomy

---

## Metadata Fields (for reference)

The script also captures from GitHub API:
- `description`: Repo description
- `language`: Primary language (Python, TypeScript, etc.)
- `topics`: GitHub topics/tags
- `last_commit_date`: Last push timestamp
- `stargazers_count`: Star count (as of fetch time)

These are stored in Supabase for historical tracking and can inform confidence scoring in future iterations.
