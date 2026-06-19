# Education Tech Stack Validation — ET-001 Pilot

**Goal:** Validate complete education tech stack using ET-001-Online-Tutoring-Platform as pilot venture  
**Venture:** ET-001-Online-Tutoring-Platform (MVP, education-training sector)  
**Scope:** Content creation → Publishing → Distribution → Automation  
**Created:** 2026-06-06  
**Status:** Starting Phase 1

---

## Venture Context

| Property | Value |
|----------|-------|
| Venture ID | ET-001 |
| Name | Online Tutoring Platform |
| Sector | education-training |
| Stage | MVP |
| Status | development |
| GitHub | https://github.com/Worldwidebro/et-001-online-tutoring-platform |

**Scope for this venture:** Build tutoring content library (books, courses, guides) → PDF export → Gumroad distribution → Student memory/personalization

---

## Core Question

**"Can we build & publish educational content for ET-001 using the 50+ tool stack, test the workflow end-to-end, and document what works?"**

---

## Phases

### Phase 1: Assess ET-001 Current State ⏳
**Status:** `pending`

- [ ] 1.1: Clone ET-001 repo locally
- [ ] 1.2: Audit existing code/content structure
- [ ] 1.3: Identify what content exists (if any)
- [ ] 1.4: Define content types needed (course modules, books, guides)
- [ ] 1.5: Map to tech stack requirements

**Output:** `et-001-audit.md`

---

### Phase 2: Build Sample Content (Tutoring Module) ⏳
**Status:** `pending`

**Content:** Create 1 complete tutoring module (e.g., "Intro to Algebra")

- [ ] 2.1: Write module outline (Markdown)
- [ ] 2.2: Create learning objectives + lesson plans
- [ ] 2.3: Add knowledge graph annotations (entities, relationships)
- [ ] 2.4: Test content structure in Quarto notebook
- [ ] 2.5: Validate with mdBook format

**Output:** `samples/algebra-module.md` + `samples/algebra-module.qmd`

---

### Phase 3: Test Publishing Workflow ⏳
**Status:** `pending`

**Tools:** Pandoc, Quarto, mdBook

- [ ] 3.1: Convert Markdown → PDF using Pandoc
- [ ] 3.2: Export as EPUB (ebook format)
- [ ] 3.3: Export as HTML (web format)
- [ ] 3.4: Build with mdBook (multi-chapter structure)
- [ ] 3.5: Validate all outputs render correctly

**Output:** `algebra-module.pdf`, `.epub`, `.html` + mdBook site

---

### Phase 4: Test Knowledge Graph + AI Layer ⏳
**Status:** `pending`

**Tools:** GraphRAG, Mem0, Neo4j, Claude API

- [ ] 4.1: Extract entities from tutoring module (concepts, topics, learning paths)
- [ ] 4.2: Build knowledge graph in Neo4j
- [ ] 4.3: Index with GraphRAG for semantic search
- [ ] 4.4: Test Mem0 for student progress tracking
- [ ] 4.5: Query: "What should this student learn next?"

**Output:** `et-001-knowledge-graph.md` + Neo4j dump

---

### Phase 5: Test Evaluation + Quality Gates ⏳
**Status:** `pending`

**Tools:** Langfuse, Promptfoo, DeepEval

- [ ] 5.1: Create rubric: "Is this tutoring content effective?"
- [ ] 5.2: Run Langfuse on sample student interactions
- [ ] 5.3: Evaluate with DeepEval (learning outcome quality)
- [ ] 5.4: Test Promptfoo on AI-generated explanations
- [ ] 5.5: Document quality gate results

**Output:** `evaluation-results.md`

---

### Phase 6: Test Distribution (Gumroad) ⏳
**Status:** `pending`

**Tools:** Gumroad API, BrowserOS

- [ ] 6.1: Create Gumroad product for algebra module
- [ ] 6.2: Upload PDF + EPUB artifacts
- [ ] 6.3: Set pricing model
- [ ] 6.4: Test browser flow (purchase → delivery)
- [ ] 6.5: Document Gumroad integration

**Output:** Live Gumroad product + test purchase

---

### Phase 7: Test Automation Workflow ⏳
**Status:** `pending`

**Tools:** n8n, Temporal, Make

**Workflow:** Create Course → Generate PDFs → Test Quality → Publish to Gumroad

- [ ] 7.1: Design workflow diagram
- [ ] 7.2: Set up n8n workflow (if available)
- [ ] 7.3: Test Temporal for multi-step orchestration
- [ ] 7.4: Create triggers (new course module → auto-publish)
- [ ] 7.5: Document workflow & error handling

**Output:** `et-001-automation-workflow.md` + n8n/Temporal config

---

### Phase 8: Create Complete Setup Checklist ⏳
**Status:** `pending`

**Operationalize:** What it takes to run education ventures at scale

- [ ] 8.1: Installation checklist (12 tools min)
- [ ] 8.2: Configuration checklist (integrations)
- [ ] 8.3: Local testing checklist (end-to-end)
- [ ] 8.4: Publishing checklist (Gumroad)
- [ ] 8.5: Maintenance checklist (ongoing)

**Output:** `EDUCATION-SETUP-CHECKLIST.md`

---

## Tech Stack by Phase

| Phase | Tools | Installed? | Tested? |
|-------|-------|-----------|---------|
| 2. Content | Markdown, Quarto | ? | ⏳ |
| 3. Publishing | Pandoc, mdBook | ? | ⏳ |
| 4. Knowledge Graph | Neo4j, GraphRAG, Mem0 | ? | ⏳ |
| 5. Evaluation | Langfuse, Promptfoo, DeepEval | ? | ⏳ |
| 6. Distribution | Gumroad (API) | ✅ Exists | ⏳ |
| 7. Automation | n8n, Temporal, Make | ? | ⏳ |

---

## Phase Completion Summary

| Phase | Status | Output |
|-------|--------|--------|
| 1. Assess ET-001 | ⏳ Pending | et-001-audit.md |
| 2. Build Content | ⏳ Pending | algebra-module.md + .qmd |
| 3. Test Publishing | ⏳ Pending | PDF, EPUB, HTML, mdBook site |
| 4. Knowledge Graph | ⏳ Pending | et-001-knowledge-graph.md |
| 5. Evaluation | ⏳ Pending | evaluation-results.md |
| 6. Distribution | ⏳ Pending | Live Gumroad product |
| 7. Automation | ⏳ Pending | et-001-automation-workflow.md |
| 8. Final Checklist | ⏳ Pending | EDUCATION-SETUP-CHECKLIST.md |

---

## Errors Encountered

| Error | Attempt | Resolution |
|-------|---------|------------|
| — | — | — |

---

## Success Criteria

✅ **Phase 1:** ET-001 audited, content types identified  
✅ **Phase 2:** 1 complete tutoring module written (algebra example)  
✅ **Phase 3:** All 4 export formats work (PDF, EPUB, HTML, mdBook)  
✅ **Phase 4:** Knowledge graph builds, semantic search works  
✅ **Phase 5:** Quality rubric evaluates content, gates pass  
✅ **Phase 6:** Gumroad product live, purchase flow tested  
✅ **Phase 7:** Automation workflow orchestrates end-to-end  
✅ **Phase 8:** Checklist enables 10+ education ventures

---

## Decisions

| Decision | Rationale |
|----------|-----------|
| Use ET-001 as pilot | Pure education venture, MVP stage, testable scope |
| Start with Algebra module | Concrete, measurable learning outcomes |
| Test ALL export formats | Different audiences (PDF books, EPUB readers, web learners) |
| Include knowledge graph | Essential for tutoring + next-lesson recommendations |
| Test Gumroad (not just theory) | Validate real distribution channel |
| Build automation last | Need to understand manual flow first |
