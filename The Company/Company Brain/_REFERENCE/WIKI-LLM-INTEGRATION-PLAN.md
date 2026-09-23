# Wiki + LLM Integration Plan

**Date:** 2026-09-22  
**Status:** DESIGN PHASE  
**Authority:** [[TYPED-WIKILINKS-GUIDE|_DOCS/TYPED-WIKILINKS-GUIDE.md]] + [[WIKI-LINK-GAPS-ANALYSIS|20-DECISIONS/WIKI-LINK-GAPS-ANALYSIS.md]]  
**Purpose:** Use Claude to auto-generate typed wikilinks, resolve ambiguities, validate graph consistency

---

## THE PROBLEM

### Current State
- ✅ **71 markdown domains** (00-67 + 90) with partial wiki links
- ✅ **Typed wikilinks spec** exists: `relationship::[[Target]]`
- ✅ **Graph ingestion pipeline** converts markdown → Neo4j RDF triples
- ❌ **Manual wikilink authoring** — no LLM assistance
- ❌ **No semantic search** — just keyword search on link text
- ❌ **20+ wiki link gaps** identified (ventures, control planes, sectors)
- ❌ **Ambiguous references** — "[[Marketing]]" could be ClickUp, sector, capability, agent

### What We Need
1. **LLM entity extraction** — identify entities in markdown and suggest wikilinks
2. **LLM relationship inference** — propose typed relationships (`relationship::[[Target]]`)
3. **LLM reference resolution** — disambiguate "[[Marketing]]" → [[SEC-025-Marketing]] vs [[CP-023-Sales]]
4. **LLM consistency validation** — check that typed relationships are sensible
5. **Semantic wiki search** — embed wikilinks in Qdrant; query by meaning not just text
6. **Gap detection** — identify missing links from domain, sector, control plane perspectives

---

## THREE-LAYER SOLUTION

### Layer 1: Wikilink Validator Agent (L1 = Report Only)

**Purpose:** Scan markdown files, identify wikilinks, propose typed relationships

**Inputs:**
- Raw markdown file (e.g., `Logic-006-Revenue-Logic.md`)
- TYPED-WIKILINKS-GUIDE spec
- COMPANY-BRAIN-ONTOLOGY.xml (relationship vocab)
- NAVIGATION_ALIASES.yaml (resolve ambiguous names)

**Process:**
```
1. Parse markdown frontmatter (id, type, domain)
2. Extract all wikilinks: [[Target]], [[Alias]], [[Slug]]
3. For each wikilink:
   a. Resolve to canonical target using NAVIGATION_ALIASES
   b. Infer relationship type from context:
      - If target is Agent + this is LogicLayer → "executes-logic"?
      - If target is Venture + mentions revenue → "enables-venture"?
      - If target is Policy + mentions constraints → "constrained-by-policy"?
   c. Validate relationship is in TYPED-WIKILINKS vocabulary (15 families)
   d. Check if relationship exists in current Neo4j (via Cypher query)
4. Output: Report (proposal only, no commits)
   - Current wikilinks (with inferred types)
   - Proposed new wikilinks (with confidence scores)
   - Ambiguous references (needs human decision)
   - Missing expected wikilinks (e.g., sector for venture)
```

**Output Format:**
```markdown
# Wikilink Validation Report — Logic-006-Revenue-Logic.md

## Current Links (10 found)
✅ belongs-to-domain::[[Business Domain]] [INFERRED]
✅ governs::[[Agent: Revenue Loop Agent]] [PROPOSED, conf=0.92]
❓ references::[[Pricing Strategy Guide]] [AMBIGUOUS: Multiple matches]

## Gaps Detected
- ❌ Missing: enabled-by::[[Capability]]
- ❌ Missing: validated-by::[[Evaluation]]
- ❌ Missing: related-to::[[Logic-008]]

## Suggestions (Manual Review Required)
1. Add: "enables-venture::[[LT-005]]" (conf=0.88) — Revenue logic powers medical courier
2. Add: "measured-by::[[Metric: MRR]]" (conf=0.85) — Revenue measured by MRR
3. Clarify: "[[Pricing Strategy Guide]]" → Policy, Document, or Process?
```

**Implementation:**
- Tool: Claude API (or local Ollama with llama3.1)
- Deployed as: MCP tool (`mcp__claude-brain__validate-wikilinks`)
- Invoked via: `validate-wiki-links <file-path>`
- Output saved to: `_REFERENCE/WIKI-VALIDATION-REPORTS/`

---

### Layer 2: Wikilink Fixer Agent (L2 = Assisted Execution)

**Purpose:** Apply Layer 1 suggestions with human approval; commit to Git

**Trigger:** User approves Layer 1 report: `apply-wiki-fixes <report-id>`

**Process:**
```
1. Read Layer 1 report (proposals + confidence scores)
2. Filter proposals:
   - confidence >= 0.90 → auto-apply
   - 0.70-0.90 → ask user for approval
   - < 0.70 → human review only
3. For approved proposals:
   a. Update markdown file with typed wikilink
   b. Run TYPED-WIKILINKS ingestion pipeline
   c. Verify Neo4j triple created (Cypher query)
4. Commit to Git:
   docs(wikilinks): validate and type 10 links in Logic-006
   
   - Added 3 typed wikilinks (conf >= 0.90)
   - Flagged 2 ambiguous references for manual review
   - Detected 2 gaps (enabled-by, validated-by)
   
   Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
5. Report back with results
```

**Safeguards:**
- Never modify wikilinks in git-controlled files without approval
- Always validate Cypher query succeeds before committing
- Keep Layer 1 report as audit trail
- Flag breaking changes (deleting or renaming entities)

---

### Layer 3: Semantic Wiki Search (Vector Search)

**Purpose:** Query wikilinks by meaning, not just text match

**Data Pipeline:**
```
TYPED WIKILINKS (Markdown)
    ↓
Extract: subject, relationship-type, object
    ↓
Build context: "{{subject}} {{relationship}} {{object}}"
    ↓
Embed context vector in Qdrant
    ↓
Index: entity-id, relationship-type, context, embedding

Example:
  entity_id: "logic-006"
  relationship: "enables-venture"
  object: "LT-005"
  context: "Revenue Logic enables Medical Courier venture"
  embedding: [0.234, 0.891, ..., 0.456]
```

**Query Examples:**
```
Q: "Show me all ventures that Revenue Logic enables"
A: Query Qdrant for embeddings similar to "enables revenue ventures"
   → [[LT-005: Medical Courier]], [[OPS-001: Staffing]], [[RE-001: Real Estate]]

Q: "What policies constrain Dispatch Logic?"
A: Query for "constrained-by-policy" relationships on Logic-031
   → [[Policy: Driver Safety]], [[Policy: Maximum Distance]]

Q: "Which agents execute Revenue Logic?"
A: Query for "executes-logic::Logic-006"
   → [[Revenue Loop Agent]], [[Finance Control Agent]]
```

**Implementation:**
- Store: Qdrant collection `wiki_links` (one doc per relationship)
- Query: `search-wiki-semantically "your question"`
- Returns: Ranked results with confidence + context

---

## WHAT'S BROKEN RIGHT NOW

From audit findings + gap analysis:

| Gap | Current | With Wiki-LLM |
|-----|---------|----------------|
| **Ventures not linked to sectors** | Manual | Auto-detect: venture domain + sector |
| **Control planes → ventures** | Manual | Infer from venture metadata |
| **Policy references** | Manual | LLM suggests: "policy::" links |
| **Ambiguous [[Marketing]]** | Breaks queries | Resolved: [[SEC-025-Marketing]] vs [[CP-023-Sales]] |
| **Missing relationships** | 20+ gaps | LLM flags + suggests |
| **No semantic search** | Keyword only | Meaning-based search on relationships |
| **Graph validation** | No check | Cypher validation before commit |

---

## IMPLEMENTATION ROADMAP

### Week 1: Validator Agent (L1, Report Only)
**Effort:** 8 hours | **Tools:** Claude API + Cypher queries

1. **Core logic** (4h)
   - Parse markdown frontmatter + wikilinks
   - Resolve aliases via NAVIGATION_ALIASES.yaml
   - Infer relationship types from TYPED-WIKILINKS families
   - Query Neo4j to check if relationship exists

2. **Report generation** (2h)
   - Current links with inferred types
   - Proposed new links (with confidence)
   - Ambiguous references flagged
   - Gaps detected

3. **Testing** (2h)
   - Run on 5 test files (Logic layers, Agents, Ventures)
   - Validate relationship type inference accuracy
   - Check alias resolution edge cases

**Deployment:** 
```bash
mcp__claude-brain__validate-wikilinks <file-path> [--output <dir>]
```

---

### Week 2: Fixer Agent (L2, Assisted Execution)
**Effort:** 6 hours | **Tools:** Claude API + Git + Cypher

1. **Approval logic** (2h)
   - Read Layer 1 report
   - Confidence-based filtering (0.90 auto, 0.70-0.90 ask, <0.70 skip)
   - User approval via CLI or TUI

2. **Apply changes** (2h)
   - Update markdown with typed wikilinks
   - Run TYPED-WIKILINKS ingestion
   - Verify Cypher triple created
   - Check for breaking changes

3. **Git integration** (2h)
   - Atomic commits per file
   - Audit trail (Layer 1 report saved)
   - Rollback capability

**Deployment:**
```bash
apply-wiki-fixes <report-id> [--auto-confirm <threshold>]
```

---

### Week 3: Semantic Search (Layer 3, Full Vector Index)
**Effort:** 4 hours | **Tools:** Qdrant + OpenAI embeddings (or nomic-embed-text)

1. **Indexing** (2h)
   - Build Qdrant collection `wiki_links`
   - Embed each relationship: "(subject) (type) (object)"
   - Index: entity_id, relationship_type, object, embedding

2. **Query interface** (2h)
   - `search-wiki-semantically "query text"`
   - Returns top-k results with confidence + Neo4j context
   - CLI + API endpoint

**Deployment:**
```bash
search-wiki-semantically "Which agents execute Revenue Logic?"
# Returns:
# 1. Revenue Loop Agent [0.95 confidence]
# 2. Finance Control Agent [0.87 confidence]
```

---

## CURRENT STATE vs. TARGET

### Current (Sep 22, 2026)
```
Markdown Files
    ↓
Manual wikilinks [[Target]]
    ↓
Typed-wikilinks guidebook (spec only)
    ↓
Graph ingestion pipeline (working)
    ↓
Neo4j (20,363 edges, manually created)
    ↓
Keyword search only
```

### Target (Oct 6, 2026)
```
Markdown Files (71 domains)
    ↓
LLM validates + infers relationships
    ↓
Typed wikilinks: relationship::[[Target]]
    ↓
LLM fixer: apply with approval
    ↓
Git commits (atomic, audited)
    ↓
Graph ingestion pipeline
    ↓
Neo4j (30K+ edges, auto-maintained consistency)
    ↓
Semantic search (meaning-based queries)
    ↓
Gap detection + suggestions (continuous)
```

---

## ONTOLOGY MAPPING

### Relationship Types (15 Families)
Source: [[TYPED-WIKILINKS-GUIDE|_DOCS/TYPED-WIKILINKS-GUIDE.md]]

**Organization** (4):
- `belongs-to-domain`, `governed-by-control-plane`, `belongs-to`, `owns`

**Business** (3):
- `enables-venture`, `offers`, `targets`, `generates-revenue`

**Agent** (9):
- `executes-logic`, `capable-of`, `uses-tool`, `uses-model`, `reads-knowledge`, `writes-knowledge`, `delegates-to-agent`, `escalates-to-agent`, `collaborates-with-agent`

**And 11 more families...**

**LLM Task:** Given markdown content + entity type, predict best relationship type.
- Input: "This policy limits driver movements to 50 miles"
- Output: `constrained-by-policy::[[Driver Distance Limit Policy]]`

---

## KEY FILES TO UPDATE

| File | Change | Status |
|------|--------|--------|
| [[TYPED-WIKILINKS-GUIDE|_DOCS/TYPED-WIKILINKS-GUIDE.md]] | Add LLM inference section | TODO |
| [[WIKI-LINKS-VERIFICATION|_SYSTEMS/WIKI-LINKS-VERIFICATION.md]] | Refresh with Layer 1 results | TODO |
| [[WIKI-LINK-GAPS-ANALYSIS|20-DECISIONS/WIKI-LINK-GAPS-ANALYSIS.md]] | Track as Layer 1 closes gaps | TODO |
| NAVIGATION_ALIASES.yaml | Auto-extend for new entities | TODO |
| Graph ingestion pipeline | Accept LLM-proposed relationships | TODO |

---

## SUCCESS METRICS

| Metric | Target | Timeline |
|--------|--------|----------|
| Wiki link coverage | 90%+ of entities have wikilinks | Oct 6 |
| Typed wikilink ratio | 80%+ of links are typed | Oct 6 |
| Gap detection accuracy | 95%+ precision on missing links | Oct 6 |
| Relationship type inference | 92%+ confidence on auto-proposed | Oct 6 |
| Neo4j graph consistency | 100% (validated on every commit) | Oct 6 |
| Semantic search queries working | 50+ test queries pass | Oct 6 |

---

## RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|-----------|
| LLM suggests wrong relationship type | Corrupts graph | Confidence threshold + human approval |
| Deletes existing correct wikilinks | Data loss | Git audit trail + rollback |
| Ambiguous [[Term]] causes errors | Graph inconsistency | Flag for manual review |
| Semantic search returns false positives | User confusion | Threshold tuning + explicit Neo4j validation |

---

**Status:** Design complete, ready for Week 1 implementation  
**Owner:** Claude Haiku 4.5 (Agent) + User approval on Layer 2/3
**Next:** Create MCP tool specs for validator + fixer agents
