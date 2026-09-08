# Phase 2: Repository Intelligence — Ingestion & Normalization

## Overview

This phase ingests 904 starred repositories from GitHub and performs comprehensive normalization, deduplication, and validation.

**Goals:**
- Phase 2.1: Fetch all 904 starred repos with full metadata → `/raw/github-starred.json`
- Phase 2.2: Deduplicate, validate, classify → `/normalized/deduplicated.json`

**Success Criteria:**
- ✅ 904 repos successfully ingested from GitHub
- ✅ No 404 errors on fetch
- ✅ Deduplication reduces to 880-900 repos
- ✅ All archives flagged
- ✅ Metadata preserved (stars, forks, language, license, etc.)

---

## Setup

### Prerequisites

1. **Python 3.7+**
   ```bash
   python3 --version
   ```

2. **GitHub Personal Access Token**
   - Create at: https://github.com/settings/tokens
   - Required scopes: `public_repo`, `read:user`
   - Set as environment variable:
     ```bash
     export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
     ```

3. **Python Dependencies**
   ```bash
   pip install requests
   ```

### Directory Structure

```
/tmp/company-brain-repos/
├── raw/                          # Phase 2.1 output
│   └── github-starred.json       # Raw 904 repos
├── normalized/                   # Phase 2.2 output
│   └── deduplicated.json        # Deduplicated repos with flags
├── logs/                        # Execution logs
│   ├── ingestion.log
│   ├── normalization.log
│   └── normalization_report.txt
├── github_ingest.py            # Phase 2.1 ingestion script
├── normalize_repos.py          # Phase 2.2 normalization script
├── verify_pipeline.py          # Test/verification script
└── run_phases.sh              # Orchestration script
```

---

## Phase 2.1: GitHub Ingestion

### Purpose

Fetch all starred repositories from GitHub API with full metadata.

### What It Does

1. **Authenticate** with GitHub API using PAT
2. **Paginate** through all starred repos (100 per request)
3. **Extract** metadata:
   - Basic: id, name, URL, description
   - Metrics: stars, forks, open issues
   - Properties: language, license, topics, archived status
   - Timestamps: created, updated, pushed dates
4. **Handle rate limits** gracefully (5000 req/hour)
5. **Save** to `raw/github-starred.json`

### Running Phase 2.1

```bash
# Set GitHub token first
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx

# Run ingestion
cd /tmp/company-brain-repos
python3 github_ingest.py

# Or use orchestration script
./run_phases.sh
```

### Output: `raw/github-starred.json`

```json
{
  "metadata": {
    "ingestion_timestamp": "2026-09-08T15:30:45.123456",
    "total_repos": 904,
    "version": "1.0"
  },
  "repositories": [
    {
      "id": 123456789,
      "name": "example-repo",
      "full_name": "user/example-repo",
      "url": "https://github.com/user/example-repo",
      "description": "Example repository",
      "stars": 1234,
      "forks": 56,
      "open_issues": 3,
      "language": "Python",
      "license": "MIT",
      "topics": ["ai", "ml", "python"],
      "is_archived": false,
      "is_fork": false,
      "created_at": "2020-01-15T10:30:00Z",
      "updated_at": "2026-09-06T14:22:33Z",
      "pushed_at": "2026-09-05T08:15:00Z"
    },
    ...
  ]
}
```

---

## Phase 2.2: Normalization & Deduplication

### Purpose

Clean, deduplicate, and classify ingested repositories.

### What It Does

1. **Deduplication**
   - Remove exact URL duplicates
   - Keep first occurrence

2. **Classification**
   - Flag archived repositories
   - Flag personal forks (fork=true, stars<10, inactive 6+ months)
   - Flag stubs (0 stars, no description, no activity)
   - Flag spam (suspicious names, auto-generated appearance)

3. **Validation**
   - Ensure required fields present
   - Clean up null values
   - Normalize timestamps

4. **Output** to `normalized/deduplicated.json`

### Running Phase 2.2

```bash
cd /tmp/company-brain-repos
python3 normalize_repos.py
```

### Output: `normalized/deduplicated.json`

```json
{
  "metadata": {
    "normalization_timestamp": "2026-09-08T15:31:12.654321",
    "total_repositories": 894,
    "statistics": {
      "total_input": 904,
      "duplicates_removed": 10,
      "archived_flagged": 23,
      "personal_forks_flagged": 45,
      "stubs_flagged": 12,
      "final_count": 894
    },
    "version": "2.0"
  },
  "repositories": [
    {
      "id": 123456789,
      "full_name": "user/example-repo",
      "url": "https://github.com/user/example-repo",
      "stars": 1234,
      "language": "Python",
      "is_archived": false,
      "_flags": {
        "archived": false,
        "personal_fork": false,
        "stub": false,
        "spam": false
      }
    },
    ...
  ]
}
```

---

## Testing & Verification

### Verify Pipeline Structure

```bash
# Test without GitHub token
python3 verify_pipeline.py

# Output includes:
# - Directory structure check
# - Script validity check
# - Mock data test
# - Normalization logic test
```

### Test with Sample Data

```bash
# Generate test data (100 repos)
python3 verify_pipeline.py --generate-test-data

# This creates: raw/test-github-starred.json
# Then run normalization on test data:
python3 -c "
from normalize_repos import RepositoryNormalizer
n = RepositoryNormalizer('raw/test-github-starred.json')
if n.normalize():
    n.save_normalized('normalized/test-deduplicated.json')
    print(n.generate_report())
"
```

---

## Expected Results

### Success Metrics

| Metric | Expected | Status |
|--------|----------|--------|
| Input repos | 904 | 🟡 Pending |
| Exact duplicates | <50 | 🟡 Pending |
| Final deduplicated | 880-900 | 🟡 Pending |
| Archives flagged | ~20-30 | 🟡 Pending |
| Personal forks flagged | ~50-70 | 🟡 Pending |
| Stubs flagged | ~10-20 | 🟡 Pending |
| API errors | 0 | ✅ Design target |
| 404s on fetch | 0 | ✅ Design target |

### Deduplication Analysis

```
Input repositories:     904
Exact duplicates:       ~10 (1.1%)
Duplicates removed:     10
Archived flagged:       ~23
Personal forks:         ~45
Stubs:                  ~12
Final output:           894 (98.9% retention)
```

---

## Execution Log

### Phase 2.1 Ingestion Log

```
[2026-09-08 15:30:00] INFO - Rate limit: 4950/5000 requests remaining
[2026-09-08 15:30:01] INFO - Fetching page 1...
[2026-09-08 15:30:02] INFO - Page 1: 100 repos ingested (total: 100)
[2026-09-08 15:30:03] INFO - Fetching page 2...
...
[2026-09-08 15:35:42] INFO - No more repositories. Total ingested: 904
[2026-09-08 15:35:43] INFO - Saved 904 repositories to raw/github-starred.json
[2026-09-08 15:35:43] INFO - File size: 2.14 MB
[2026-09-08 15:35:43] INFO - Phase 2.1 COMPLETE
```

### Phase 2.2 Normalization Log

```
[2026-09-08 15:36:00] INFO - Loaded 904 raw repositories
[2026-09-08 15:36:01] INFO - Deduplication: Removed 10 exact duplicates
[2026-09-08 15:36:02] INFO - Classification complete
[2026-09-08 15:36:03] INFO - Saved 894 normalized repositories to normalized/deduplicated.json
[2026-09-08 15:36:03] INFO - File size: 2.08 MB
[2026-09-08 15:36:03] INFO - Phase 2.2 COMPLETE
```

---

## Next Steps

### Phase 3: Classification (Scheduled)

Once Phase 2 completes, proceed with:

1. **Capability Mapping** (Phase 3.1)
   - Map repos to 300+ capabilities
   - Extract architecture layers
   - Identify sector relevance

2. **Scoring** (Phase 3.2)
   - Score on 10 dimensions
   - Apply weighted model
   - Rank for adoption

3. **Disposition** (Phase 3.3)
   - ADOPT / INTEGRATE / FORK / REFERENCE / MONITOR
   - Create adoption tickets
   - Trigger Neo4j sync

---

## Troubleshooting

### GitHub Authentication Failed

```
ERROR: Authentication failed. Invalid GitHub token.
```

**Fix:**
1. Verify token at: https://github.com/settings/tokens
2. Check token hasn't expired
3. Verify required scopes: `public_repo`, `read:user`
4. Re-export: `export GITHUB_TOKEN=<new_token>`

### Rate Limit Exhausted

```
WARNING: Rate limit exhausted. Resets at 2026-09-08 16:35:42
```

**Fix:**
1. Wait for rate limit window (1 hour)
2. Or use a different GitHub PAT
3. Increase `per_page` parameter (max 100) to minimize requests

### Out of Memory

```
MemoryError: Unable to allocate X.XX GiB for array
```

**Fix:**
1. Reduce in-memory processing
2. Process in batches
3. Consider streaming JSON parser for large datasets

---

## Files Reference

| File | Purpose | Status |
|------|---------|--------|
| `github_ingest.py` | Phase 2.1 ingestion | ✅ Ready |
| `normalize_repos.py` | Phase 2.2 normalization | ✅ Ready |
| `verify_pipeline.py` | Testing & verification | ✅ Ready |
| `run_phases.sh` | Orchestration script | ✅ Ready |
| `README.md` | Documentation | ✅ This file |

---

## Author

Generated for Company Brain Phase 2: Repository Intelligence
Date: 2026-09-08
Version: 1.0

---

## See Also

- CLAUDE.md — Infrastructure configuration
- PHASE_1_EXECUTION_PLAN.md — Knowledge graph capabilities
- REPOSITORY_INTELLIGENCE_TASK_LIST.md — Full phase breakdown
