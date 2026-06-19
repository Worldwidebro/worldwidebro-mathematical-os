---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# SkillsLLM Integration — Findings & Research

**Last Updated**: 2026-06-04

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

### Key Characteristics
- Organized by use case (agents, code gen, DevOps, etc.)
- GitHub star counts included
- Security-vetted (open-source only)
- Browser extension available
- Curated by community

---

## API & Data Access (COMPLETE)

### API Status
- ❌ No public API endpoint found
- ❌ No documented API documentation
- ❌ No CSV/JSON export available
- ✅ Public marketplace with browsable skills pages

### Skill Data Structure (Confirmed)
Each skill has these fields:
- **name** - Skill title
- **author** - GitHub username
- **description** - Brief explanation (~120 chars)
- **github_url** - Link to source repository
- **language** - Primary programming language
- **stars** - GitHub star count
- **forks** - GitHub fork count
- **category** - Primary tag (e.g., "AI Agents", "MCP Servers")
- **related_tags** - Secondary tags (e.g., "anthropic", "python")
- **engagement_count** - Numeric counter

### Access Strategy
**Option 1: Web Scraping** (RECOMMENDED)
- Tool: Playwright
- Target: skillsllm.com/skills page (with pagination)
- Rate limit: Respectful delays (1-2 sec per page)
- Estimated time: 30-60 min for 2,800 skills (50 per page = 56 pages)

**Option 2: Contact SkillsLLM**
- Send request via /feedback form
- Ask for: JSON export or API access
- Timeline: Unknown (likely 1-2 weeks)

**Decision**: Build web scraper for Phase 2a

---

## Integration Architecture

### Data Flow
```
SkillsLLM API/Scraper
    ↓ (2,800 skills JSON)
Supabase skills table
    ↓ (title + description)
Chroma embeddings
    ↓ (semantic search)
Matching engine queries
    ↓ (venture_id → recommended skills)
Plane webhook
    ↓ (update custom field)
712 Ventures with skill recommendations
```

### Data Model (DRAFT)

#### Table 1: `skills` (Supabase)
```sql
CREATE TABLE skills (
  id BIGSERIAL PRIMARY KEY,
  skill_id TEXT UNIQUE,
  name TEXT NOT NULL,
  description TEXT,
  category TEXT,
  github_url TEXT,
  github_stars INT,
  url TEXT,
  keywords TEXT[],
  created_at TIMESTAMP DEFAULT NOW(),
  synced_from_skillsllm TIMESTAMP
);
```

#### Table 2: `venture_skills` (Supabase)
```sql
CREATE TABLE venture_skills (
  id BIGSERIAL PRIMARY KEY,
  venture_id BIGINT REFERENCES ventures(id),
  skill_id BIGINT REFERENCES skills(id),
  relevance_score FLOAT,
  recommended_by TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Matching Strategy (DRAFT)

### Logic Options
1. **Rules-based**: Map sector → skill category
2. **Semantic**: Embed venture description + query skill embeddings
3. **Hybrid**: Combine rules + semantic ranking

### Example Matching
- Commerce sector → prioritize "Code Generation", "AI Agents"
- DevOps ventures → prioritize "CLI Tools", "DevOps" skills
- Automation platforms → prioritize "AI Agents", "MCP Servers"

---

## Implementation Blockers (PARALLEL)

### Blocker 2a: Ingest
- Confirm SkillsLLM API/scraping strategy
- Build scraper → Supabase upload
- ~2 hours once API determined

### Blocker 2b: Matching Engine
- Finalize matching rules
- Build script + test with 3 ventures
- ~1 hour

### Blocker 2c: Chroma Indexing
- Verify Chroma running
- Batch embed all 2,800 skills
- ~30 min

---

## Open Questions
- [ ] Is SkillsLLM API public? Where's the API docs?
- [ ] One-time sync or daily cron for skill updates?
- [ ] Should sectors have preferred skills defined manually?
- [ ] How to handle deprecated/renamed skills?
