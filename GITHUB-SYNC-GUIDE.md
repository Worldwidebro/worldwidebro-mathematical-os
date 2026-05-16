# GitHub Repos Sync — Setup & Usage

The Dexter Dashboard now sources repo metadata directly from GitHub instead of hardcoded Supabase entries.

## How It Works

```
GitHub API (repos, README, topics, package.json)
    ↓
github_repos_sync.py (extracts metadata, infers capabilities)
    ↓
Supabase repos table (source of truth)
    ↓
dexter_dashboard.py (fetches + capability-matches to ventures)
    ↓
Dashboard: Per-venture recommended repos
```

## Setup

### 1. Set GitHub Token (Recommended)

```bash
export GITHUB_TOKEN="ghp_YOUR_TOKEN_HERE"
export GITHUB_ORG="Worldwidebro"
```

Get token: https://github.com/settings/tokens (Personal access tokens → Tokens (classic))
- Scopes needed: `public_repo`, `read:org`
- Without token: 60 req/hr. With token: 5000 req/hr.

### 2. Ensure Supabase Connection

```bash
export SUPABASE_URL="https://cyhzilqldouzgynacqpe.supabase.co"
export SUPABASE_KEY="your_service_role_key"
```

### 3. Run Initial Sync

```bash
python3 github_repos_sync.py
```

**Output:**
```
================================================================================
GITHUB REPOS SYNC — Sync GitHub repos to Supabase
================================================================================

⚠️  GITHUB_TOKEN not set. Using unauthenticated requests (rate limited).

📡 Fetching repos from Worldwidebro...
✅ Found 42 repos in Worldwidebro

🔍 Extracting metadata from 42 repos...
  🔵 OWNED venture-hub           | portfolio, cap-table, fundraising
  🔵 OWNED mission-control       | authentication, oauth, oidc
  🔵 OWNED pitch-kit             | pitch, deck, presentation
  ⭐ STARRED some-reference      | api, integration
  ...

================================================================================
📊 SYNC SUMMARY
================================================================================
  Total repos:    42
  Owned:          18
  Starred:        24
  Timestamp:      2026-05-16T15:30:45.123456
================================================================================
```

## How Repos Are Classified

### Owned Repos (Internal Products)
- Hardcoded canonical list of 18 known internal products
- Synced with full metadata from GitHub
- Recommended to ventures based on **capability matching**
- Shown in dashboard with blue badges

### Starred Repos (External References)
- All repos in Worldwidebro org NOT in owned list
- Represent ecosystem of external tools
- Can be linked to ventures for research/reference
- Currently not displayed in dashboard (planned for Phase 2)

## Capability Inference

Repos automatically get capabilities extracted from:

1. **GitHub Topics** (highest priority)
   - mission-control repo topic: `authentication` → capability: authentication
   - venture-hub repo topic: `portfolio` → capability: portfolio

2. **package.json keywords** (if Node.js project)
   - `"keywords": ["oauth", "sessions"]` → capabilities: oauth, sessions

3. **README/description** (keyword matching)
   - "financial" → capability: finance
   - "authentication" → capability: authentication

## Venture-to-Repo Matching

Dashboard matches repos to ventures in order:

1. **Primary:** `ventures.required_capabilities` field
   - If venture has `required_capabilities = ['authentication', 'oauth']`
   - Recommends repos with matching capabilities

2. **Secondary:** Sector-based matching
   - If venture has no required_capabilities
   - Recommends repos whose capabilities match venture.sector

3. **Top 3 repos** by capability match score
   - Sorted by relevance
   - Displayed as inline blue badges with tooltips

## Automation (Optional)

To keep repos in sync with GitHub automatically:

```bash
# Run daily sync (cron)
0 9 * * * cd /Users/acebless/Documents && python3 github_repos_sync.py >> /tmp/github_sync.log 2>&1
```

Or use Make:
```bash
# Add to Makefile
.PHONY: sync-repos
sync-repos:
	python3 github_repos_sync.py
```

## Dashboard Integration

The dashboard now:
- ✅ Fetches repos from Supabase (GitHub-sourced)
- ✅ Matches repos to ventures by capabilities
- ✅ Shows top 3 repos per venture as badges
- ✅ Displays repo purpose on hover
- ✅ Shows integration effort (low/medium/high)

### Next Phase Features
- Starred repos display (external references)
- Click-to-view repo details modal
- Integration effort filtering (show only "low" effort)
- Team recommendations (repos used by similar ventures)

## Troubleshooting

### "No repos found"
- Check GITHUB_ORG is correct (default: "Worldwidebro")
- Verify org is public or GITHUB_TOKEN has access
- Run with verbose: add `print(repos)` after fetch

### "Sync failed: 401"
- Set GITHUB_TOKEN (unauthenticated hits rate limit)
- For Supabase: SUPABASE_KEY must be service_role (not anon)

### Repos not appearing in dashboard
- Run sync: `python3 github_repos_sync.py`
- Check Supabase repos table: `select count(*) from repos where repo_type='owned'`
- Verify venture `required_capabilities` is set or sector matches

## Files

- **github_repos_sync.py** — Main sync script (run manually or via cron)
- **dexter_dashboard.py** — Updated to use GitHub-sourced repos
- **GITHUB-SYNC-GUIDE.md** — This file
