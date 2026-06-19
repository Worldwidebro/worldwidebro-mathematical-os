# SkillsLLM Integration Task Plan

**Status**: Initiated 2026-06-04  
**Goal**: Integrate 2,800+ SkillsLLM skills into Plane/OS ecosystem  
**Outcome**: Ventures get skill recommendations; agents suggest skills autonomously

---

## Phase 1: Schema & Research (COMPLETE ✅)
**Status**: `complete`  
**Goal**: Define data model, understand SkillsLLM API, assess integration points

- [x] Research SkillsLLM API → No public API; decided on Playwright web scraping
- [x] Discover skill fields → 11 fields (name, author, description, github_url, language, stars, forks, category, related_tags, engagement_count)
- [x] Design Supabase schemas (skills, venture_skills tables)
- [x] Design Chroma embedding strategy (name + description fields)
- [x] Create Supabase migration: `PLANE/01_SCHEMAS/001_create_skills_tables.sql`
- [x] Create Playwright scraper skeleton: `populate_skillsllm_skills.py`

**Decisions Made**:
- Supabase as canonical store (not local CSV)
- Chroma for semantic search (name + description)
- Playwright for web scraping (respectful rate limiting: 1-2 sec/page)
- Three parallel blockers in Phase 2

---

## Phase 2a: Ingest Script (READY ✅)
**Status**: `ready_for_execution`  
**Goal**: Pull SkillsLLM data → Supabase

**Tasks**:
- [x] Build SkillsLLM scraper (Playwright)
- [x] Map SkillsLLM fields → Supabase schema
- [x] Handle 2,800 skills with pagination + batching
- [x] Implement --sample flag for testing
- [x] Ready to execute: `python3 populate_skillsllm_skills.py --sample`

**Output**: `PLANE/05_SCRIPTS/populate_skillsllm_skills.py` (ready to run)

---

## Phase 2b: Matching Engine (READY ✅)
**Status**: `ready_for_execution`  
**Goal**: Build venture-type → skills recommender

**Tasks**:
- [x] Defined sector → skill category mapping (SECTOR_SKILL_MAPPING dict)
- [x] Implemented rules-based matching logic
- [x] Created batch insert with upsert
- [x] Ready to execute: `python3 match_ventures_to_skills.py --dry-run`
- [ ] (After Phase 2a) Run on all ventures

**Output**: `PLANE/05_SCRIPTS/match_ventures_to_skills.py` (ready to run)

---

## Phase 2c: Chroma Indexing (PLANNED)
**Status**: `planned`  
**Goal**: Build semantic search for skills

**Tasks**:
- [ ] Start Chroma server (if not running)
- [ ] Create `skills_semantic` collection
- [ ] Batch embed all 2,800 skills (name + description)
- [ ] Test query: "code generation" → top 5 skills
- [ ] Integrate embeddings into matching engine

**Output**: Chroma collection ready for semantic queries

---

## Phase 3: Plane Webhook (READY ✅)
**Status**: `ready_for_execution`  
**Dependencies**: Phase 2a ✅ + Phase 2b ✅
**Goal**: Wire skill recommendations into Plane custom fields

**Tasks**:
- [x] Designed webhook handler with Plane API integration
- [x] Implemented venture_skills → Plane custom field mapping
- [x] Created batch update with error handling
- [x] Ready to execute: `python3 plane_webhook_skills.py --dry-run`
- [ ] (After Phase 2a+2b) Run on all 712 ventures

**Output**: `PLANE/04_AUTOMATION/plane_webhook_skills.py` (ready to run)

---

## Phase 4: Agent Integration (DEPENDS ON Phase 3)
**Status**: `queued`  
**Goal**: Agents can query & suggest skills

**Tasks**:
- [ ] Create agent query function: `get_venture_recommended_skills(venture_id)`
- [ ] Create agent action: `suggest_skill(venture_id, skill_id, rationale)`
- [ ] Test with Claude agent on sample venture
- [ ] Document for future agent builds

**Output**: Agents can autonomously recommend skills

---

## Errors Encountered
| Error | Phase | Attempt | Resolution |
|-------|-------|---------|------------|
| (none yet) | — | — | — |

---

## Files Created ✅
- [x] `PLANE/01_SCHEMAS/001_create_skills_tables.sql` — Supabase migrations
- [x] `PLANE/05_SCRIPTS/populate_skillsllm_skills.py` — Ingest script (Phase 2a)
- [x] `PLANE/05_SCRIPTS/match_ventures_to_skills.py` — Matching engine (Phase 2b)
- [x] `PLANE/04_AUTOMATION/plane_webhook_skills.py` — Plane webhook (Phase 3)
- [ ] Agent skill lookup function — Phase 4 (pending)

## Execution Sequence
1. **Apply Supabase migration**: Import `001_create_skills_tables.sql` into Supabase
2. **Test ingest**: `python3 populate_skillsllm_skills.py --sample` (test with 1 page)
3. **Test matching**: `python3 match_ventures_to_skills.py --ventures 1,2,3 --dry-run`
4. **Test webhook**: `python3 plane_webhook_skills.py --dry-run`
5. **Full run**: Execute all scripts with actual data (2,800 skills, 712 ventures)

---

## Next Action
→ **Ready for execution**: User can now:
  1. Apply Supabase migration
  2. Run test commands with --sample and --dry-run flags
  3. Deploy full pipeline once testing passes
