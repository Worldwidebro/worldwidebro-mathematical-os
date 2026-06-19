---
name: skillsllm-integration-task-plan
version: 1.0
created: 2026-06-04 22:43
updated: 2026-06-05 00:15
phase: "1-4 (1: ✅ Complete, 2a-3: ✅ Ready, 2c: 🔮 Planned, 4: 🔮 Planned)"
status: ready_for_security_review
author: Claude Haiku 4.5
objective: Track SkillsLLM integration phases through deployment
next_action: Apply security fixes (2-3 hours) before testing
---

# SkillsLLM Integration — Task Plan v1.0

**Status**: Initiated 2026-06-04  
**Goal**: Integrate 2,800+ SkillsLLM skills into Plane/OS ecosystem  
**Outcome**: Ventures get skill recommendations; agents suggest skills autonomously

---

## Phase 1: Schema & Research (COMPLETE ✅)
**Status**: `complete`  
**Goal**: Define data model, understand SkillsLLM API, assess integration points

- [x] Research SkillsLLM API → No public API; decided on Playwright web scraping
- [x] Discover skill fields → 11 fields
- [x] Design Supabase schemas (skills, venture_skills tables)
- [x] Design Chroma embedding strategy (name + description fields)
- [x] Create Supabase migration
- [x] Create Playwright scraper skeleton

**Decisions Made**:
- Supabase as canonical store
- Chroma for semantic search
- Playwright for web scraping
- Three parallel blockers in Phase 2

---

## Phase 2a: Ingest Script (READY ✅)
**Status**: `ready_for_execution`  
**Goal**: Pull SkillsLLM data → Supabase

- [x] Build SkillsLLM scraper (Playwright)
- [x] Map SkillsLLM fields → Supabase schema
- [x] Handle 2,800 skills with pagination + batching
- [x] Implement --sample flag for testing

---

## Phase 2b: Matching Engine (READY ✅)
**Status**: `ready_for_execution`  
**Goal**: Build venture-type → skills recommender

- [x] Defined sector → skill category mapping
- [x] Implemented rules-based matching logic
- [x] Created batch insert with upsert

---

## Phase 2c: Chroma Indexing (PLANNED)
**Status**: `planned`  
**Goal**: Build semantic search for skills

- [ ] Start Chroma server
- [ ] Create `skills_semantic` collection
- [ ] Batch embed all 2,800 skills
- [ ] Test semantic queries

---

## Phase 3: Plane Webhook (READY ✅)
**Status**: `ready_for_execution`  
**Dependencies**: Phase 2a ✅ + Phase 2b ✅
**Goal**: Wire skill recommendations into Plane custom fields

- [x] Designed webhook handler
- [x] Implemented venture_skills → Plane mapping
- [x] Created batch update

---

## Phase 4: Agent Integration (QUEUED)
**Status**: `queued`  
**Goal**: Agents can query & suggest skills

- [ ] Create agent query function
- [ ] Create agent action function
- [ ] Test with Claude agent

---

## Blockers (v1.1 required)
| Severity | Issue | Phase | Status |
|----------|-------|-------|--------|
| 🔴 CRITICAL | Missing RLS policies | Foundation | BLOCKING |
| 🔴 CRITICAL | Admin API keys in scripts | All | BLOCKING |
| 🔴 CRITICAL | Plane API key in logs | Phase 3 | BLOCKING |
| 🟠 HIGH | No page input validation | Phase 2a | TODO |
| 🟠 HIGH | No Plane rate limiting | Phase 3 | TODO |
| 🟡 MEDIUM | No input validation | Phase 2a | TODO |
| 🟡 MEDIUM | N+1 query problem | Phase 2b | TODO |
| 🟡 MEDIUM | No audit logging | Database | TODO |

See: `RED-TEAM-REPORT-v1.0.md`

---

## Files Created ✅
- [x] `001_create_skills_tables-v1.0.sql`
- [x] `populate_skillsllm_skills-v1.0.py`
- [x] `match_ventures_to_skills-v1.0.py`
- [x] `plane_webhook_skills-v1.0.py`

---

## Execution Sequence (v1.1+)
1. Apply security fixes (2-3 hours)
2. Apply Supabase migration
3. Test ingest: `--sample` mode
4. Test matching: `--dry-run` mode
5. Test webhook: `--dry-run` mode
6. Full run: all data (2,800 skills, 712 ventures)

---

## Next Action
→ Apply security fixes before deployment (see `RED-TEAM-REPORT-v1.0.md`)
