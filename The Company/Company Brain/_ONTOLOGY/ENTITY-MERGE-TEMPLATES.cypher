// ═══════════════════════════════════════════════════════════════════════════════
// COMPANY BRAIN ENTITY MERGE TEMPLATES
// ═══════════════════════════════════════════════════════════════════════════════
// Purpose: Standardized Cypher patterns for migrating YAML entities → Neo4j nodes
// Usage: Substitute parameters ($entity_id, $name, etc.) and execute via driver
// Authority: Phase 2 Graph-Native Migration
// Updated: 2026-09-17
// ═══════════════════════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 1: MERGE SECTOR
// ───────────────────────────────────────────────────────────────────────────────

MERGE (sector:Entity:Sector {entity_id: $entity_id})
ON CREATE SET
  sector.name = $name,
  sector.type = "Sector",
  sector.confidence = 0.8,
  sector.contested = false,
  sector.needs_review = false,
  sector.source_count = 1,
  sector.created = datetime(),
  sector.updated = datetime(),
  sector.description = $description,
  sector.sector_id = $sector_id
ON MATCH SET
  sector.updated = datetime(),
  sector.source_count = sector.source_count + 1,
  sector.needs_review = CASE WHEN sector.source_count < 2 THEN true ELSE false END

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (sector)-[:DERIVED_FROM]->(source)

RETURN sector.entity_id AS id, sector.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 2: MERGE VENTURE
// ───────────────────────────────────────────────────────────────────────────────

MERGE (venture:Entity:Venture {entity_id: $entity_id})
ON CREATE SET
  venture.name = $name,
  venture.type = "Venture",
  venture.confidence = 0.8,
  venture.contested = false,
  venture.needs_review = false,
  venture.source_count = 1,
  venture.created = datetime(),
  venture.updated = datetime(),
  venture.ref_id = $ref_id,
  venture.sector = $sector,
  venture.status = $status
ON MATCH SET
  venture.updated = datetime(),
  venture.source_count = venture.source_count + 1,
  venture.needs_review = CASE WHEN venture.source_count < 2 THEN true ELSE false END

// Link to sector
MERGE (sector:Entity:Sector {entity_id: "SEC-" + $sector})
MERGE (venture)-[:RELATES {type: "belongs_to", confidence: 0.95, source_sha: $source_sha256}]->(sector)

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (venture)-[:DERIVED_FROM]->(source)

RETURN venture.entity_id AS id, venture.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 3: MERGE TOOL
// ───────────────────────────────────────────────────────────────────────────────

MERGE (tool:Entity:Tool {entity_id: $entity_id})
ON CREATE SET
  tool.name = $name,
  tool.type = "Tool",
  tool.confidence = 0.7,
  tool.contested = false,
  tool.needs_review = false,
  tool.source_count = 1,
  tool.created = datetime(),
  tool.updated = datetime(),
  tool.category = $category,
  tool.cost_tier = $cost_tier,
  tool.risk_level = $risk_level
ON MATCH SET
  tool.updated = datetime(),
  tool.source_count = tool.source_count + 1,
  tool.needs_review = CASE WHEN tool.source_count < 2 THEN true ELSE false END

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (tool)-[:DERIVED_FROM]->(source)

RETURN tool.entity_id AS id, tool.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 4: MERGE AGENT
// ───────────────────────────────────────────────────────────────────────────────

MERGE (agent:Entity:Agent {entity_id: $entity_id})
ON CREATE SET
  agent.name = $name,
  agent.type = "Agent",
  agent.confidence = 0.75,
  agent.contested = false,
  agent.needs_review = false,
  agent.source_count = 1,
  agent.created = datetime(),
  agent.updated = datetime(),
  agent.purpose = $purpose,
  agent.autonomy_level = $autonomy_level,
  agent.status = $status
ON MATCH SET
  agent.updated = datetime(),
  agent.source_count = agent.source_count + 1,
  agent.needs_review = CASE WHEN agent.source_count < 2 THEN true ELSE false END

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (agent)-[:DERIVED_FROM]->(source)

RETURN agent.entity_id AS id, agent.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 5: MERGE CAPABILITY
// ───────────────────────────────────────────────────────────────────────────────

MERGE (capability:Entity:Capability {entity_id: $entity_id})
ON CREATE SET
  capability.name = $name,
  capability.type = "Capability",
  capability.confidence = 0.7,
  capability.contested = false,
  capability.needs_review = false,
  capability.source_count = 1,
  capability.created = datetime(),
  capability.updated = datetime(),
  capability.layer = $layer,
  capability.description = $description
ON MATCH SET
  capability.updated = datetime(),
  capability.source_count = capability.source_count + 1,
  capability.needs_review = CASE WHEN capability.source_count < 2 THEN true ELSE false END

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (capability)-[:DERIVED_FROM]->(source)

RETURN capability.entity_id AS id, capability.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 6: MERGE REPOSITORY
// ───────────────────────────────────────────────────────────────────────────────

MERGE (repo:Entity:Repository {entity_id: $entity_id})
ON CREATE SET
  repo.name = $name,
  repo.type = "Repository",
  repo.confidence = 0.85,
  repo.contested = false,
  repo.needs_review = false,
  repo.source_count = 1,
  repo.created = datetime(),
  repo.updated = datetime(),
  repo.url = $url,
  repo.stars = $stars,
  repo.language = $language,
  repo.description = $description
ON MATCH SET
  repo.updated = datetime(),
  repo.source_count = repo.source_count + 1,
  repo.stars = $stars,
  repo.needs_review = CASE WHEN repo.source_count < 2 THEN true ELSE false END

// Link to source
MERGE (source:Source {sha256: $source_sha256})
MERGE (repo)-[:DERIVED_FROM]->(source)

RETURN repo.entity_id AS id, repo.source_count AS sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 7: CREATE RELATIONSHIP (RELATES EDGE)
// ───────────────────────────────────────────────────────────────────────────────

// Assumes both entities already exist
MATCH (a:Entity {entity_id: $entity_a_id})
MATCH (b:Entity {entity_id: $entity_b_id})

MERGE (a)-[rel:RELATES {type: $relationship_type, source_sha: $source_sha256}]->(b)
ON CREATE SET
  rel.confidence = $confidence,
  rel.claim = $claim,
  rel.created = datetime()
ON MATCH SET
  rel.updated = datetime()

RETURN a.entity_id AS source, b.entity_id AS target, rel.type AS rel_type;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 8: DETECT CONTRADICTION
// ───────────────────────────────────────────────────────────────────────────────

// Match same entity pair with same relationship type but different claims
WITH $entity_a_id AS a_id, $entity_b_id AS b_id, $relationship_type AS rel_type

MATCH (a:Entity {entity_id: a_id})
MATCH (b:Entity {entity_id: b_id})
MATCH (a)-[rel1:RELATES {type: rel_type}]->(b)
WHERE rel1.source_sha <> $new_source_sha

WITH a, b, rel1, $new_claim AS new_claim
SET a.contested = true, b.contested = true

MERGE (a)-[conflict:CONTRADICTS {type: rel_type}]->(b)
ON CREATE SET
  conflict.sources = [rel1.source_sha, $new_source_sha],
  conflict.claims = [rel1.claim, new_claim],
  conflict.detected = datetime()

RETURN a.entity_id AS entity_a, b.entity_id AS entity_b, conflict.sources AS contradicting_sources;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 9: SOURCE NODE CREATION
// ───────────────────────────────────────────────────────────────────────────────

MERGE (source:Source {sha256: $sha256})
ON CREATE SET
  source.title = $title,
  source.type = $type,
  source.date = datetime(),
  source.url = $url,
  source.raw_path = $raw_path,
  source.metadata = $metadata
ON MATCH SET
  source.updated = datetime()

RETURN source.sha256 AS sha256, source.title AS title;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 10: THRESHOLD-GATED ENTITY PROMOTION
// ───────────────────────────────────────────────────────────────────────────────

// Only promote entity if ≥2 sources AND not contested
MATCH (e:Entity {entity_id: $entity_id})
WHERE e.source_count >= 2 AND NOT e.contested AND e.confidence > 0.7
SET e.needs_review = false, e.status = "PROMOTED"

RETURN e.entity_id AS entity, e.source_count AS sources, e.status AS status;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 11: INTEGRITY GATE - DANGLING REFERENCES
// ───────────────────────────────────────────────────────────────────────────────

MATCH (s:Source)-[r:MENTIONS]->(e)
WHERE NOT e:Entity
RETURN s.sha256 AS source, e AS dangling_target, COUNT(*) AS count
ORDER BY count DESC;

// ───────────────────────────────────────────────────────────────────────────────
// TEMPLATE 12: INTEGRITY GATE - PROVENANCE COMPLETENESS
// ───────────────────────────────────────────────────────────────────────────────

MATCH (e:Entity)
WHERE NOT (e)-[:DERIVED_FROM]->(:Source)
RETURN e.entity_id AS orphan_entity, e.type AS entity_type, e.source_count AS sources
ORDER BY e.source_count DESC;

// ═══════════════════════════════════════════════════════════════════════════════
// USAGE NOTES
// ═══════════════════════════════════════════════════════════════════════════════
// 1. All templates use MERGE (idempotent, safe for re-execution)
// 2. source_count tracks how many independent sources claim this entity
// 3. Single-source entities (source_count < 2) flagged needs_review: true
// 4. Contradictions detected and flagged contested: true
// 5. Every entity MUST have [:DERIVED_FROM]->(Source) edge
// 6. Confidence tiers: 0.95 (relationship certainty) → 0.7-0.85 (new entities)
// 7. Integrity gates run after bulk ingestion to catch errors
// ═══════════════════════════════════════════════════════════════════════════════
