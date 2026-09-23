// ═══════════════════════════════════════════════════════════════════════════════
// COMPANY BRAIN GRAPH SCHEMA (Graph-Native, Neo4j 5.x)
// ═══════════════════════════════════════════════════════════════════════════════
// Authority: Knowledge Graph Engineer + Phase 2 Autonomy Architecture
// Updated: 2026-09-23
// Status: ACTIVE - Full Graph Engineering Implementation (Phase C: Schema Mapping)
// Principles: Every claim traces to source | Never silently overwrite | Surface contradictions
// ═══════════════════════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────────────────────────────────────
// UNIQUENESS CONSTRAINTS
// ───────────────────────────────────────────────────────────────────────────────

CREATE CONSTRAINT entity_unique IF NOT EXISTS
  FOR (e:Entity) REQUIRE e.entity_id IS UNIQUE;

CREATE CONSTRAINT source_unique IF NOT EXISTS
  FOR (s:Source) REQUIRE s.sha256 IS UNIQUE;

// ───────────────────────────────────────────────────────────────────────────────
// QUERY INDEXES
// ───────────────────────────────────────────────────────────────────────────────

CREATE INDEX entity_type IF NOT EXISTS FOR (e:Entity) ON (e.type);
CREATE INDEX entity_confidence IF NOT EXISTS FOR (e:Entity) ON (e.confidence);
CREATE INDEX entity_contested IF NOT EXISTS FOR (e:Entity) ON (e.contested);
CREATE INDEX entity_needs_review IF NOT EXISTS FOR (e:Entity) ON (e.needs_review);
CREATE INDEX source_date IF NOT EXISTS FOR (s:Source) ON (s.date);
CREATE INDEX source_type IF NOT EXISTS FOR (s:Source) ON (s.type);

// ───────────────────────────────────────────────────────────────────────────────
// CORE NODE TYPES
// ───────────────────────────────────────────────────────────────────────────────

// (:Entity {entity_id, name, type, confidence, contested, needs_review, created, updated, source_count})
//   Labels: Entity, + specific type (Venture, Sector, Tool, Agent, Gap, Capability, etc.)

// (:Source {sha256, title, type, date, url, raw_path, metadata})
//   types: registry, architecture, code, decision, audit

// ─────────────────────────────────────────────────────────────────────────────
// RELATIONSHIPS (Typed Edges)
// ─────────────────────────────────────────────────────────────────────────────

// [:MENTIONS {confidence}] — Source document mentions entity
// [:RELATES {type, confidence, claim, source_sha, created}] — Domain relationship (depends_on, enables, uses, contains, requires, conflicts_with)
// [:CONTRADICTS {sources, claims, detected}] — Conflict marker (same entity pair, different claims)
// [:SUPPORTS {type, strength}] — Evidence edge (empirical, theoretical, anecdotal)
// [:DERIVED_FROM] — Provenance (EVERY entity must have ≥1)
// [:SUPERSEDED_BY] — Append-only history
// [:MERGED_INTO] — Duplicate resolution

// ───────────────────────────────────────────────────────────────────────────────
// INTEGRITY GATES
// ───────────────────────────────────────────────────────────────────────────────

// Gate 1: Dangling references
// MATCH (s)-[r:MENTIONS]->(e) WHERE NOT e:Entity RETURN "FAIL: dangling mention" LIMIT 1;

// Gate 2: Provenance completeness
// MATCH (e:Entity) WHERE NOT (e)-[:DERIVED_FROM]->(:Source) RETURN "FAIL: entity without provenance" LIMIT 1;

// Gate 3: Contradiction consistency
// MATCH (e:Entity)-[c:CONTRADICTS]->() WHERE NOT e.contested RETURN "FAIL: contradicts edge but contested=false" LIMIT 1;

// Gate 4: Orphan detection
// MATCH (e:Entity) WHERE NOT ()-[:RELATES|:MENTIONS|:SUPPORTS|:DEPENDS_ON|:USES]->(e) RETURN e.entity_id AS orphan LIMIT 10;

// ───────────────────────────────────────────────────────────────────────────────
// AUDIT LOG
// ───────────────────────────────────────────────────────────────────────────────

// (:AuditLog {timestamp, action, user, entities_created, entities_updated, contradictions_detected, notes})
// CREATE CONSTRAINT audit_log_unique IF NOT EXISTS FOR (a:AuditLog) REQUIRE a.timestamp IS UNIQUE;

// ───────────────────────────────────────────────────────────────────────────────
// NAVIGATION VIEWS (Materialized Subsets)
// ───────────────────────────────────────────────────────────────────────────────

// View 1: promoted_entities (≥2 sources, confidence > 0.7, not contested)
// MATCH (e:Entity) WHERE e.source_count >= 2 AND e.confidence > 0.7 AND NOT e.contested
// RETURN e.entity_id, e.type, e.name, e.confidence, e.source_count;

// View 2: active_contradictions (contested entities)
// MATCH (a:Entity)-[c:CONTRADICTS]->(b:Entity) WHERE a.contested = true AND b.contested = true
// RETURN a.entity_id, b.entity_id, c.sources, c.claims;

// View 3: knowledge_gaps (entities with <2 sources or needs_review=true)
// MATCH (e:Entity) WHERE e.source_count < 2 OR e.needs_review = true
// RETURN DISTINCT e.type, COUNT(e) AS gap_count;

// ───────────────────────────────────────────────────────────────────────────────
// KNOWLEDGE GRAPH ENGINEERING RULES (2026-09-23)
// ───────────────────────────────────────────────────────────────────────────────

// Rule 1: PROVENANCE REQUIREMENT
// Every entity MUST have ≥1 [:DERIVED_FROM]->(Source) edge
// Enforcement: Verify gate #2 (see INTEGRITY GATES section)

// Rule 2: CONTRADICTION DETECTION & PRESERVATION
// When (a)-[:RELATES]->(b) exists from source X with claim "C1"
// AND (a)-[:RELATES]->(b) exists from source Y with claim "C2" where C1 ≠ C2:
//   - DO NOT delete or overwrite
//   - CREATE (a)-[:CONTRADICTS {sources, claims, detected}]->(b)
//   - SET a.contested=true, b.contested=true
//   - Preserve both edges with different source_sha properties
// Result: Contradictions surface for human review, not silently buried

// Rule 3: THRESHOLD-GATED PROMOTION
// Single-source entities (source_count=1) are MERGE'd as (:Entity) nodes
// BUT flagged needs_review=true and EXCLUDED from lookup views
// Promotion happens only after corroboration by 2+ independent sources
// Lookup view filters: WHERE source_count >= 2 AND contested=false AND needs_review=false

// Rule 4: SHA256 GUARDS DRIFT
// Every (:Source) node stores sha256 of its raw body
// Before trusting a derived claim, compare stored sha256 to current file hash
// Mismatch → SET needs_review=true on all (e)-[:DERIVED_FROM]->(source_with_drift) nodes
// Re-ingest source and re-validate all dependent claims

// Rule 5: APPEND-ONLY HISTORY
// Never DELETE entity or relationship history
// Updates ADD edges: OLD_VALUE -[:SUPERSEDED_BY]-> NEW_VALUE
// Relationship change: old_edge removed, new_edge added, but edge properties preserved
// Result: Complete audit trail, no data loss

// Rule 6: BIDIRECTIONAL CONSISTENCY
// (a)-[:RELATES]->(b) with type=ENABLES implies (b)-[:DEPENDS_ON]->(a)
// Query triggers should detect missing reverse edges
// Consistency check: bidirectional edges either both exist or both are absent

// ───────────────────────────────────────────────────────────────────────────────
// IMPACT ANALYSIS PROPAGATION (Depth Semantics)
// ───────────────────────────────────────────────────────────────────────────────

// When a source changes or an entity is updated:
// Depth 0 = source node only (no traversal)
// Depth 1 = (:Source)-[:MENTIONS]->(:Entity) [directly mentioned entities]
// Depth N = N-hop neighborhood via [:RELATES]/[:SUPPORTS]/[:CONTRADICTS]/[:DEPENDS_ON]
// Unbounded = * [entire reachable subgraph from changed source]
//
// Propagation: SET affected_node.needs_review=true on all nodes at traversal depth
// Re-evaluation: For each flagged node, re-validate against new source data
// Clearing: Remove needs_review only after explicit verification

// ───────────────────────────────────────────────────────────────────────────────
// ENTITY TYPES (Via OBJECTS_EXTENDED.yaml)
// ───────────────────────────────────────────────────────────────────────────────
// 60+ entity types across 13 categories:
// - ORG (Organization), VEN (Venture), OPC (OpCo), DIV (Division), TEA (Team), ROL (Role), PER (Person)
// - CAP (Capability), SKL (Skill), AGT (Agent), MOD (Model), TOL (Tool), MCP (MCP), WFL (Workflow), LOP (Loop)
// - DST (Dataset), ANL (Analysis), INS (Insight), RPT (Report), DAS (Dashboard)
// - DEC (Decision), APR (Approval), EXC (Execution), OUT (Outcome), LES (Lesson)
// - DOC (Document), GDE (Guide), PRC (Procedure), POL (Policy), STD (Standard)
// - SCH (Schema), TBL (Table), FLD (Field), REC (Record)
// - And 20+ more (see OBJECTS_EXTENDED.yaml for full taxonomy)

// ───────────────────────────────────────────────────────────────────────────────
// RELATIONSHIP TYPES (Via RELATIONSHIPS_EXTENDED.yaml)
// ───────────────────────────────────────────────────────────────────────────────
// 250+ predicates across 12 categories (USES, DEPENDS_ON, IMPLEMENTS, EXECUTES, PRODUCES, etc.)
// Each relationship carries:
//   - type (predicate name)
//   - confidence (0..1)
//   - claim (the specific assertion)
//   - source_sha (SHA256 of originating source)
//   - created (timestamp)

// When multiple sources claim different [:RELATES] types or confidence values:
//   Keep both edges. Let [:CONTRADICTS] marker flag the conflict.

// ───────────────────────────────────────────────────────────────────────────────
// SOURCE TYPES (Ingestion Categories)
// ───────────────────────────────────────────────────────────────────────────────
// registry: YAML/CSV registry files (ventures-by-sector.yaml, SECTOR-REGISTRY.yaml, etc.)
// database: Supabase/PostgreSQL extracts (ventures table, OpCos table, etc.)
// architecture: Cypher/Neo4j schema definition files
// code: Source code files (repo manifests, APIs, schema.sql)
// decision: Decision logs, ADRs, meeting notes
// audit: Audit reports, validation runs, ground truth ledgers
// document: Markdown wiki files, operational guides
// external: Third-party data feeds (market data, customer records)
