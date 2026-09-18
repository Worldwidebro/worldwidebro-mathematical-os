// ═══════════════════════════════════════════════════════════════════════════════
// COMPANY BRAIN GRAPH SCHEMA (Graph-Native, Neo4j 5.x)
// ═══════════════════════════════════════════════════════════════════════════════
// Authority: Knowledge Graph Engineer + Phase 2 Autonomy Architecture
// Updated: 2026-09-17
// Status: ACTIVE (migrating from YAML registries)
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
