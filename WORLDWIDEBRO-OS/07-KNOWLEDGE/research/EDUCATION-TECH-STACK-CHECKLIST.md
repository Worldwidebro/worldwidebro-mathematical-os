# Education Tech Stack Setup Checklist

**Project:** ET-001 Online Tutoring Platform  
**Date:** 2026-06-06  
**Status:** Phase 2 Complete (Content Created) — Ready for Publishing Testing

---

## Executive Summary

✅ **What Works:** ET-001 has everything needed for education product workflow  
✅ **Venture Model:** Already includes Gumroad + Whop business model  
✅ **Content:** Complete Algebra tutoring module created (6-hour course)  
✅ **Next:** Test publishing tools (Pandoc, Quarto, mdBook) to create PDF/EPUB/HTML exports

---

## Flow Diagram: Content → Publishing → Distribution → Automation

```
┌─────────────────────────────────────────────────────────────────┐
│                   ET-001 EDUCATION WORKFLOW                      │
└─────────────────────────────────────────────────────────────────┘

1️⃣ CONTENT CREATION (✅ DONE)
   └─ Markdown module with YAML frontmatter
   └─ Learning objectives, prerequisites, assessments
   └─ File: modules/intro-to-algebra.md

2️⃣ PUBLISHING (⏳ NEXT)
   ├─ Pandoc: .md → .pdf, .epub, .html
   ├─ Quarto: Interactive notebook version
   └─ mdBook: Multi-chapter course site

3️⃣ KNOWLEDGE GRAPH (⏳ PHASE 4)
   ├─ Extract entities (Variable, Equation, etc.)
   ├─ Build Neo4j graph
   ├─ Index with GraphRAG
   └─ Track student progress with Mem0

4️⃣ EVALUATION (⏳ PHASE 5)
   ├─ DeepEval: Does this teach effectively?
   ├─ Langfuse: Track AI explanations
   └─ Promptfoo: Test explanation clarity

5️⃣ DISTRIBUTION (⏳ PHASE 6)
   ├─ Upload PDF/EPUB to Gumroad ($27)
   ├─ Upsell Whop community ($29/mo)
   └─ Scale to digital courses ($97-497)

6️⃣ AUTOMATION (⏳ PHASE 7)
   ├─ n8n: New module → auto-publish
   ├─ Temporal: Multi-step orchestration
   └─ Trigger: Create → Generate → Test → Publish
```

---

## Installation & Setup Checklist

### ✅ COMPLETED
- [x] ET-001 repo cloned locally
- [x] VENTURE.json reviewed (business model confirmed)
- [x] Markdown module written (intro-to-algebra.md)
- [x] YAML frontmatter created (metadata)
- [x] Planning files created (task_plan, findings, progress)

### ⏳ READY TO TEST (Next Session)

#### Publishing Tools Installation
- [ ] Check if Pandoc installed: `pandoc --version`
  - If not: `brew install pandoc` (macOS) or `apt-get install pandoc` (Linux)
- [ ] Check if Quarto installed: `quarto --version`
  - If not: `brew install quarto` (macOS)
- [ ] Check if mdBook installed: `mdbook --version`
  - If not: `cargo install mdbook` (requires Rust)

#### Knowledge Graph Tools
- [ ] Check Neo4j running: `curl http://localhost:7687` or desktop app
- [ ] Check GraphRAG installed: `pip list | grep graphrag`
- [ ] Check Mem0 installed: `pip list | grep mem0`

#### Evaluation Tools
- [ ] Check Langfuse available (cloud): https://langfuse.com
- [ ] Check Promptfoo installed: `promptfoo --version`
- [ ] Check DeepEval installed: `pip list | grep deepeval`

#### Automation Tools
- [ ] Check n8n running: `curl http://localhost:5678` or docker status
- [ ] Check Temporal: `temporal --version` or docker
- [ ] Check Make/Zapier available

---

## Test Execution Plan (Phase 3)

### 3.1 Pandoc Test
```bash
cd et-001-online-tutoring-platform

# Convert to PDF
pandoc modules/intro-to-algebra.md -o algebra-module.pdf

# Convert to EPUB
pandoc modules/intro-to-algebra.md -o algebra-module.epub

# Convert to HTML
pandoc modules/intro-to-algebra.md -o algebra-module.html
```

**Expected:** 3 files created, no errors

### 3.2 Quarto Test
```bash
# Create Quarto notebook version
cp modules/intro-to-algebra.md modules/intro-to-algebra.qmd

# Render
quarto render modules/intro-to-algebra.qmd --to html
```

**Expected:** Interactive HTML notebook with code cells

### 3.3 mdBook Test
```bash
# Create mdBook structure
mdbook init course-site
cp modules/intro-to-algebra.md course-site/src/chapter_1.md

# Build
mdbook build course-site

# Serve
mdbook serve course-site
# Visit: http://localhost:3000
```

**Expected:** Multi-chapter course site visible in browser

---

## Tech Stack Status Matrix

| Category | Tool | Installed? | Tested? | For ET-001 |
|----------|------|-----------|---------|-----------|
| **Content** | Markdown | ✅ Yes | ✅ Yes | Content writing |
| **Publishing** | Pandoc | ❓ TBD | ⏳ Next | PDF/EPUB/HTML |
| **Publishing** | Quarto | ❓ TBD | ⏳ Next | Interactive notebooks |
| **Publishing** | mdBook | ❓ TBD | ⏳ Next | Course website |
| **Knowledge Graph** | Neo4j | ❓ TBD | ⏳ Later | Learning paths |
| **Knowledge Graph** | GraphRAG | ❓ TBD | ⏳ Later | Semantic search |
| **Knowledge Graph** | Mem0 | ❓ TBD | ⏳ Later | Student memory |
| **Evaluation** | Langfuse | ✅ Cloud | ⏳ Later | LLM tracking |
| **Evaluation** | Promptfoo | ❓ TBD | ⏳ Later | Prompt evaluation |
| **Evaluation** | DeepEval | ❓ TBD | ⏳ Later | Learning outcome eval |
| **Distribution** | Gumroad | ✅ Available | ⏳ Later | $27 PDF sales |
| **Distribution** | Whop | ✅ Available | ⏳ Later | $29/mo community |
| **Automation** | n8n | ❓ TBD | ⏳ Later | Workflow orchestration |
| **Automation** | Temporal | ❓ TBD | ⏳ Later | Multi-step workflows |
| **AI** | Claude API | ✅ Yes | ✅ Yes | Generate content |
| **Browser** | BrowserOS | ✅ Yes | ✅ Yes | PDF capture |

---

## What Works for ET-001 ✅

| Component | Status | Evidence |
|-----------|--------|----------|
| Content Creation | ✅ Works | Algebra module written (2000+ lines) |
| Markdown Format | ✅ Works | YAML frontmatter + lesson structure proven |
| Learning Objectives | ✅ Works | Module has clear learning_objectives array |
| Knowledge Graph Ready | ✅ Works | knowledge_graph_entities array defined |
| Business Model | ✅ Works | $27 Gumroad + $29/mo Whop in VENTURE.json |
| First Dollar Path | ✅ Works | "PDF → Gumroad → Whop" already documented |
| Automation Ready | ✅ Readiness | n8n/Temporal can orchestrate the flow |

---

## Blockers & Solutions

| Blocker | Probability | Solution |
|---------|-------------|----------|
| Pandoc not installed | Medium | `brew install pandoc` |
| mdBook requires Rust | Medium | Install Rust first: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Neo4j not running | Medium | `brew services start neo4j` or use desktop app |
| Gumroad API limits | Low | Use web UI for manual upload |
| Evaluation tools misconfigured | High | Skip Phase 5, revisit later |

---

## Next Actions (Priority Order)

### Immediate (Phase 3: Publishing)
1. [ ] Install Pandoc (if needed)
2. [ ] Test Pandoc: .md → PDF, EPUB, HTML
3. [ ] Install mdBook (if needed)
4. [ ] Build mdBook course site
5. [ ] Document publishing results

### Short-term (Phase 4-5)
6. [ ] Start Neo4j instance
7. [ ] Extract entities from algebra module
8. [ ] Build knowledge graph in Neo4j
9. [ ] Index with GraphRAG
10. [ ] Set up Langfuse for evaluation

### Medium-term (Phase 6-7)
11. [ ] Create Gumroad product (manual or API)
12. [ ] Set up n8n workflow (Content → Publish)
13. [ ] Test Temporal orchestration
14. [ ] Create production checklist

### Long-term (Scale to all education ventures)
15. [ ] Replicate for ET-002 (Language Learning)
16. [ ] Replicate for ET-003 (Test Prep)
17. [ ] Replicate for MC-017 (Course Platform)
18. [ ] Replicate for BW-004 (Lash Training)

---

## File Structure Created

```
et-001-online-tutoring-platform/
├── VENTURE.json (business model)
├── README.md (overview)
├── modules/
│   └── intro-to-algebra.md (6-hour course content)
└── [TBD outputs after Phase 3]
    ├── algebra-module.pdf
    ├── algebra-module.epub
    ├── algebra-module.html
    └── course-site/ (mdBook)
```

---

## Success Criteria for Each Phase

| Phase | Success Metric | Target | Status |
|-------|----------------|--------|--------|
| 1. Assess | ET-001 audited | ✅ Complete | ✅ PASS |
| 2. Content | Module written | ✅ Algebra complete | ✅ PASS |
| 3. Publishing | All 4 formats export | ✅ PDF, EPUB, HTML, mdBook | ⏳ READY |
| 4. Knowledge Graph | Graph builds + queries work | ✅ Entities extracted | ⏳ READY |
| 5. Evaluation | Rubric evaluates content | ✅ Learning outcomes clear | ⏳ READY |
| 6. Distribution | Gumroad product live + purchase works | ✅ Pricing defined ($27) | ⏳ READY |
| 7. Automation | Workflow orchestrates end-to-end | ✅ Pipeline designed | ⏳ READY |
| 8. Final Checklist | Setup repeatable for 10+ ventures | ✅ Pattern proven | ⏳ READY |

---

## How to Use This Checklist

1. **For Phase 3 (Publishing):**
   - Run installation checklist
   - Execute each test in order
   - Mark ✅ when passing

2. **For Documentation:**
   - Capture errors in "Blockers" section
   - Document tool-specific quirks
   - Update Status column after testing

3. **For Scaling:**
   - Use same checklist for ET-002, ET-003, etc.
   - Adjust file paths only (module names differ)
   - Reuse automation workflows

---

## Links & Resources

- **ET-001 Repo:** https://github.com/Worldwidebro/et-001-online-tutoring-platform
- **Planning Files:**
  - `education-tech-stack-plan.md`
  - `education-tech-stack-progress.md`
  - `education-tech-stack-findings.md`
- **Pandoc Docs:** https://pandoc.org/
- **mdBook Docs:** https://rust-lang.github.io/mdBook/
- **Quarto Docs:** https://quarto.org/docs/guide/
- **Gumroad:** https://gumroad.com/
- **Whop:** https://whop.com/

---

*Created with ET-001 Online Tutoring Platform | Worldwidebro Holdings*  
*Phase 2 Complete — Ready for Phase 3 Publishing Tests*
