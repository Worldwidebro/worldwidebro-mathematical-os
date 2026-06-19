---
name: skillsllm-integration-findings
version: 1.0
created: 2026-06-04 22:40
updated: 2026-06-05 00:15
phase: "1 (Research)"
status: complete
author: Claude Haiku 4.5
objective: Document SkillsLLM platform research and data model design
references: ["skillsllm-integration-task-plan", "RED-TEAM-REPORT-v1.0"]
---

# SkillsLLM Integration — Findings & Research v1.0

**Last Updated**: 2026-06-05

---

## SkillsLLM Platform Overview

### What It Is
- **Name**: SkillsLLM (skillsllm.com)
- **Purpose**: AI Skills Marketplace for Claude Code, Codex CLI, ChatGPT
- **Scale**: 2,800+ skills across 10 categories
- **License**: Open-source (GitHub-verified)

### Skill Categories
| Category | Count | Notes |
|----------|-------|-------|
| AI Agents | 2,157 | Largest category |
| MCP Servers | 469 | Data integration |
| Code Generation | ~150 | Estimated |
| CLI Tools | ~100 | Estimated |
| IDE Extensions | ~100 | Estimated |
| DevOps | ~150 | Estimated |
| Others | ~75 | Various |

---

## API & Data Access (COMPLETE)

### API Status
- ❌ No public API endpoint found
- ❌ No documented API documentation
- ❌ No CSV/JSON export available
- ✅ Public marketplace with browsable skills pages

### Skill Data Structure (Confirmed)
Each skill has 11 fields:
- **name** - Skill title
- **author** - GitHub username
- **description** - Brief explanation (~120 chars)
- **github_url** - Link to source repository
- **language** - Primary programming language
- **stars** - GitHub star count
- **forks** - GitHub fork count
- **category** - Primary tag
- **related_tags** - Secondary tags
- **engagement_count** - Numeric counter

### Access Strategy
**Option 1: Web Scraping** (CHOSEN)
- Tool: Playwright
- Target: skillsllm.com/skills with pagination
- Rate limit: 1-2 sec per page
- Time estimate: 30-60 min for 2,800 skills

**Status**: Implemented in `populate_skillsllm_skills-v1.0.py`

---

## Matching Strategy

### Logic (Implemented)
**Rules-based**: Sector → skill category mapping

Examples:
- Commerce → "Code Generation", "AI Agents"
- DevOps → "CLI Tools", "DevOps"
- Automation → "AI Agents", "MCP Servers"

### Future (Phase 2c)
Semantic matching via Chroma embeddings (optional enhancement)

---

## Data Model (Confirmed)

### Table 1: `skills`
- id, skill_id (unique), name, description, category
- github_url, github_stars, github_forks, language
- related_tags (array), engagement_count
- embedding_status, created_at, updated_at, synced_from_skillsllm_at

### Table 2: `venture_skills`
- id, venture_id, skill_id (unique together)
- relevance_score (0.0-1.0)
- recommended_by ("rules", "semantic", "manual", "agent")
- created_at, updated_at

---

## Architecture

### Data Flow
```
SkillsLLM → Scraper → Supabase → Matching Engine → Plane Webhook → 712 Ventures
```

### Files
- `populate_skillsllm_skills-v1.0.py` — Ingest (Playwright scraper)
- `match_ventures_to_skills-v1.0.py` — Matching (rules-based)
- `plane_webhook_skills-v1.0.py` — Webhook (Plane API)
- `001_create_skills_tables-v1.0.sql` — Schema

---

## Known Issues (See RED-TEAM-REPORT-v1.0.md)

### Critical
- Missing RLS policies on tables
- Admin API keys in scripts
- Plane API key in logs

### High
- No page input validation
- No Plane rate limiting
- ToS compliance (no robots.txt check)

### Medium
- No input validation on scraped data
- N+1 query problem
- No audit logging

---

## Next Steps
1. Apply security fixes (see RED-TEAM-REPORT-v1.0.md)
2. Run tests with --sample and --dry-run flags
3. Full deployment (2,800 skills, 712 ventures)
