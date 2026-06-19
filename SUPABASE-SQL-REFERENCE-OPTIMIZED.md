---
references:
  - [[SYSTEM-ENHANCEMENT-ROADMAP]]
  - [[populate_venture_knowledge_graph.py]]
---

# Supabase-Optimized SQL Reference

**Purpose:** Essential SQL commands for Worldwidebro OS knowledge graph + venture system  
**Updated:** 2026-06-14  
**Scope:** PostgreSQL + Supabase extensions optimized for 1504 ventures, 700 repos, 3362 entities

---

## Part 1: Most Important 30 to Master First

These 30 commands handle 95% of your graph operations.

### Core CRUD (5)

```sql
-- 1. INSERT with RETURNING (get IDs back immediately)
INSERT INTO graph_entities (id, name, entity_type, metadata)
VALUES (gen_uuid(), 'venture-name', 'VENTURE', '{"sector": "EDU"}'::jsonb)
RETURNING id, name;

-- 2. SELECT with filtering
SELECT id, name, entity_type FROM graph_entities 
WHERE entity_type = 'VENTURE' AND metadata->>'sector' = 'EDU';

-- 3. UPDATE with RETURNING
UPDATE graph_entities SET metadata = jsonb_set(metadata, '{status}', '"active"')
WHERE id = '...'
RETURNING id, metadata;

-- 4. DELETE with RETURNING
DELETE FROM graph_relationships WHERE source_id = '...'
RETURNING COUNT(*) as deleted_count;

-- 5. UPSERT (INSERT OR UPDATE)
INSERT INTO ventures (id, name, sector, status) 
VALUES ($1, $2, $3, $4)
ON CONFLICT (id) DO UPDATE SET 
  name = $2, 
  status = $4,
  updated_at = now()
RETURNING id;
```

### Relationships (5)

```sql
-- 6. Create relationship between venture and repo
INSERT INTO graph_relationships (id, source_id, target_id, relation_type, metadata)
VALUES (gen_uuid(), 'repo-id', 'venture-id', 'PROVIDES_CAPABILITY', '{"capability": "api"}'::jsonb);

-- 7. Find all repos providing a capability
SELECT r.id, r.name, r.metadata->>'language' as language
FROM graph_entities r
INNER JOIN graph_relationships gr ON gr.source_id = r.id
WHERE gr.relation_type = 'PROVIDES_CAPABILITY'
  AND gr.metadata->>'capability' = 'api'
  AND r.entity_type = 'REPO';

-- 8. Find ventures needing a capability (no matching repo yet)
SELECT DISTINCT v.id, v.name
FROM ventures v
WHERE v.required_capabilities::text LIKE '%api%'
  AND NOT EXISTS (
    SELECT 1 FROM graph_relationships 
    WHERE target_id = v.id AND metadata->>'capability' = 'api'
  );

-- 9. Count relationships by type
SELECT relation_type, COUNT(*) as count
FROM graph_relationships
GROUP BY relation_type
ORDER BY count DESC;

-- 10. Batch insert relationships (transactional)
BEGIN;
INSERT INTO graph_relationships (id, source_id, target_id, relation_type, metadata)
SELECT 
  gen_uuid(),
  'repo-' || repos.id,
  'venture-' || ventures.id,
  'AVAILABLE_FOR',
  ('{"match_score": ' || (random() * 100)::int || '}')::jsonb
FROM (SELECT id FROM repos LIMIT 100) repos
CROSS JOIN (SELECT id FROM ventures WHERE sector = 'EDU' LIMIT 50) ventures;
COMMIT;
```

### Aggregation (5)

```sql
-- 11. Count ventures by sector
SELECT sector, COUNT(*) as venture_count
FROM ventures
GROUP BY sector
ORDER BY venture_count DESC;

-- 12. Find repos with most connections
SELECT r.id, r.name, COUNT(DISTINCT gr.target_id) as venture_connections
FROM graph_entities r
LEFT JOIN graph_relationships gr ON gr.source_id = r.id
WHERE r.entity_type = 'REPO'
GROUP BY r.id, r.name
HAVING COUNT(DISTINCT gr.target_id) > 5
ORDER BY venture_connections DESC
LIMIT 20;

-- 13. Capability adoption rate (% of ventures with repo match)
SELECT 
  cap.name,
  COUNT(DISTINCT v.id) as ventures_needing,
  COUNT(DISTINCT CASE WHEN gr.id IS NOT NULL THEN v.id END) as ventures_matched,
  ROUND(100.0 * COUNT(DISTINCT CASE WHEN gr.id IS NOT NULL THEN v.id END) / 
        COUNT(DISTINCT v.id), 1) as adoption_rate
FROM capabilities cap
CROSS JOIN ventures v
LEFT JOIN graph_relationships gr ON 
  gr.target_id = v.id AND 
  gr.metadata->>'capability' = cap.name
GROUP BY cap.name
ORDER BY adoption_rate DESC;

-- 14. Entity type distribution
SELECT entity_type, COUNT(*) as count FROM graph_entities
GROUP BY entity_type
ORDER BY count DESC;

-- 15. Ventures by capability requirement (JSON extraction)
SELECT 
  id, 
  name,
  jsonb_array_length(required_capabilities::jsonb) as capability_count
FROM ventures
ORDER BY capability_count DESC;
```

### Batch Operations (5)

```sql
-- 16. Batch insert 100 ventures at a time
INSERT INTO ventures (id, name, sector, status, created_at)
SELECT 
  gen_uuid(),
  name,
  sector,
  'active',
  now()
FROM unnest(ARRAY[
  ('Venture A', 'EDU'),
  ('Venture B', 'FIN'),
  ('Venture C', 'EDU')
]) AS t(name, sector);

-- 17. Bulk update venture status by sector
UPDATE ventures SET status = 'validated'
WHERE sector = 'EDU' AND status = 'active'
RETURNING id, name, status;

-- 18. Delete old entities (cleanup)
DELETE FROM graph_entities 
WHERE created_at < now() - interval '90 days'
  AND entity_type = 'TEMP'
RETURNING COUNT(*) as deleted;

-- 19. Copy data between environments (backup/sync)
INSERT INTO ventures (id, name, sector, status)
SELECT id, name, sector, status FROM ventures@remote_db
WHERE id NOT IN (SELECT id FROM ventures)
ON CONFLICT DO NOTHING;

-- 20. Partition insert (for large tables)
INSERT INTO ventures PARTITION (sector = 'EDU') (id, name, status)
VALUES (gen_uuid(), 'New Venture', 'active');
```

### Window Functions (5)

```sql
-- 21. Rank repos by connection strength
SELECT 
  r.id,
  r.name,
  COUNT(DISTINCT gr.target_id) as connections,
  RANK() OVER (ORDER BY COUNT(DISTINCT gr.target_id) DESC) as repo_rank
FROM graph_entities r
LEFT JOIN graph_relationships gr ON gr.source_id = r.id
WHERE r.entity_type = 'REPO'
GROUP BY r.id, r.name;

-- 22. Running total of ventures created per month
SELECT 
  DATE_TRUNC('month', created_at) as month,
  COUNT(*) as created_this_month,
  SUM(COUNT(*)) OVER (ORDER BY DATE_TRUNC('month', created_at)) as cumulative
FROM ventures
GROUP BY DATE_TRUNC('month', created_at);

-- 23. Find top venture per sector (DISTINCT ON)
SELECT DISTINCT ON (sector)
  sector,
  id,
  name,
  mrr
FROM ventures
ORDER BY sector, mrr DESC;

-- 24. Calculate capability gaps (window function)
SELECT DISTINCT ON (v.id)
  v.id,
  v.name,
  COUNT(*) OVER (PARTITION BY v.id) as required_cap_count
FROM ventures v
LEFT JOIN graph_relationships gr ON 
  gr.target_id = v.id AND gr.relation_type = 'REQUIRES_CAPABILITY'
ORDER BY v.id;

-- 25. Venture growth trajectory (3-month moving average)
SELECT 
  v.id,
  DATE_TRUNC('week', created_at) as week,
  COUNT(*) as new_ventures,
  AVG(COUNT(*)) OVER (PARTITION BY v.sector ORDER BY DATE_TRUNC('week', created_at) 
                       ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
FROM ventures v
GROUP BY v.sector, DATE_TRUNC('week', created_at);
```

### JSON & Complex Queries (5)

```sql
-- 26. Extract nested JSON data
SELECT 
  id,
  name,
  metadata->>'language' as language,
  metadata->'stats'->>'stars' as stars,
  metadata#>>'{tags,0}' as primary_tag
FROM graph_entities
WHERE entity_type = 'REPO';

-- 27. Query array containment
SELECT id, name FROM ventures
WHERE required_capabilities::text LIKE '%api%'
  AND required_capabilities::text LIKE '%database%';

-- 28. Update nested JSON field
UPDATE graph_entities 
SET metadata = jsonb_set(
  metadata, 
  '{stats,updated_at}', 
  to_jsonb(now())
)
WHERE entity_type = 'REPO'
RETURNING id, metadata;

-- 29. Aggregate JSON arrays
SELECT 
  sector,
  jsonb_agg(DISTINCT metadata->>'language') as languages_used
FROM (
  SELECT sector, metadata FROM repos r
  INNER JOIN ventures v ON v.id = r.venture_id
) grouped
GROUP BY sector;

-- 30. Full-text search on JSON content
SELECT id, name, rank
FROM (
  SELECT 
    id, 
    name,
    ts_rank(
      to_tsvector('english', name || ' ' || metadata->>'description'),
      plainto_tsquery('english', 'graph database')
    ) as rank
  FROM graph_entities
) ranked
WHERE rank > 0
ORDER BY rank DESC;
```

---

## Part 2: Supabase-Specific Extensions

### UUID Operations (CRITICAL)

```sql
-- Generate UUID v4 (Supabase default)
gen_uuid()
gen_random_uuid()
uuid_generate_v4()

-- Example: Auto-generate in INSERT
INSERT INTO ventures (id, name) VALUES (gen_uuid(), 'New Venture')
RETURNING id;

-- Type casting
'550e8400-e29b-41d4-a716-446655440000'::uuid
```

### Vector Search (pgvector) — For Semantic Repo/Venture Matching

```sql
-- Enable extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create embedding column
ALTER TABLE graph_entities ADD COLUMN embedding vector(1536);

-- Index for fast search
CREATE INDEX ON graph_entities USING ivfflat (embedding vector_cosine_ops);

-- Find semantically similar repos
SELECT id, name, 1 - (embedding <=> $1::vector) as similarity
FROM graph_entities
WHERE entity_type = 'REPO'
ORDER BY embedding <-> $1::vector
LIMIT 10;
```

### Full-Text Search (tsvector)

```sql
-- Create search index
CREATE INDEX idx_entities_search ON graph_entities 
USING gin(to_tsvector('english', name || ' ' || COALESCE(metadata->>'description', '')));

-- Search query
SELECT id, name FROM graph_entities
WHERE to_tsvector('english', name || ' ' || COALESCE(metadata->>'description', '')) 
      @@ plainto_tsquery('english', 'authentication api')
ORDER BY ts_rank(to_tsvector('english', name), plainto_tsquery('english', 'authentication api')) DESC;
```

### Row Level Security (RLS) — Multi-Tenant Ventures

```sql
-- Enable RLS
ALTER TABLE ventures ENABLE ROW LEVEL SECURITY;

-- Policy: User can only see their own ventures
CREATE POLICY ventures_user_policy ON ventures
  FOR SELECT
  USING (user_id = auth.uid());

-- Policy: Admin can see all
CREATE POLICY ventures_admin_policy ON ventures
  FOR SELECT
  USING (
    (SELECT role FROM auth.users WHERE id = auth.uid()) = 'admin'
  );
```

### Real-Time Subscriptions (LISTEN/NOTIFY)

```sql
-- Notify when new entity is created
CREATE OR REPLACE FUNCTION notify_new_entity()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM pg_notify('graph_updates', json_build_object(
    'event', 'entity_created',
    'entity_id', NEW.id,
    'entity_type', NEW.entity_type,
    'timestamp', now()
  )::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_notify_entity AFTER INSERT ON graph_entities
FOR EACH ROW EXECUTE FUNCTION notify_new_entity();

-- Client side: LISTEN graph_updates;
```

### Array Operations

```sql
-- Store array of capabilities
ALTER TABLE ventures ADD COLUMN required_capabilities TEXT[] DEFAULT ARRAY[]::TEXT[];

-- Add to array
UPDATE ventures SET required_capabilities = array_append(required_capabilities, 'api')
WHERE id = $1;

-- Remove from array
UPDATE ventures SET required_capabilities = array_remove(required_capabilities, 'api')
WHERE id = $1;

-- Check containment
SELECT id, name FROM ventures WHERE 'api' = ANY(required_capabilities);

-- Unnest to individual rows
SELECT v.id, v.name, cap FROM ventures v, UNNEST(v.required_capabilities) cap;

-- Array aggregation
SELECT sector, array_agg(DISTINCT cap) as all_capabilities
FROM ventures v, UNNEST(v.required_capabilities) cap
GROUP BY sector;
```

### Crypto Functions (pgcrypto)

```sql
-- Hash venture ID for privacy
SELECT md5('venture-12345');

-- HMAC signature
SELECT hmac_sha256('venture-data', 'secret-key');

-- Encrypt sensitive fields
SELECT pgp_sym_encrypt('api-key', 'password');
```

---

## Part 3: Advanced PostgreSQL (Missing from Generic Lists)

### LATERAL Joins — Dynamic Venture-to-Repo Matching

```sql
-- Find best 3 repos for each venture
SELECT 
  v.id,
  v.name,
  r.repo_id,
  r.repo_name,
  r.match_score
FROM ventures v
CROSS JOIN LATERAL (
  SELECT 
    r.id as repo_id,
    r.name as repo_name,
    COUNT(DISTINCT gr.id) as match_score
  FROM repos r
  INNER JOIN graph_relationships gr ON gr.source_id = r.id
  WHERE gr.target_id = v.id
  ORDER BY match_score DESC
  LIMIT 3
) r;
```

### Materialized Views — Pre-compute Expensive Aggregations

```sql
-- Pre-compute venture health scores
CREATE MATERIALIZED VIEW venture_health_scores AS
SELECT 
  v.id,
  v.name,
  v.sector,
  COUNT(DISTINCT gr.id) as repo_connections,
  COUNT(DISTINCT CASE WHEN gr.relation_type = 'REQUIRES_CAPABILITY' THEN 1 END) as capability_gaps,
  ROUND(100.0 * COUNT(DISTINCT CASE WHEN gr.relation_type = 'PROVIDED_BY' THEN 1 END) / 
        NULLIF(COUNT(DISTINCT CASE WHEN gr.relation_type = 'REQUIRES_CAPABILITY' THEN 1 END), 0), 1) as coverage_pct
FROM ventures v
LEFT JOIN graph_relationships gr ON gr.target_id = v.id
GROUP BY v.id, v.name, v.sector;

-- Refresh when data changes
REFRESH MATERIALIZED VIEW venture_health_scores;

-- Query is instant
SELECT * FROM venture_health_scores WHERE coverage_pct < 80 ORDER BY coverage_pct;
```

### DISTINCT ON — Keep Only First Per Group

```sql
-- Most recent event per venture
SELECT DISTINCT ON (venture_id)
  venture_id,
  event_type,
  created_at
FROM venture_events
ORDER BY venture_id, created_at DESC;
```

### Recursive CTEs — Graph Traversal

```sql
-- Find all repos in dependency chain
WITH RECURSIVE repo_chain AS (
  -- Base case: start with repo
  SELECT id, name, 1 as depth FROM repos WHERE id = $1
  
  UNION ALL
  
  -- Recursive case: find repos this one depends on
  SELECT 
    r.id,
    r.name,
    rc.depth + 1
  FROM repos r
  INNER JOIN graph_relationships gr ON gr.target_id = r.id
  INNER JOIN repo_chain rc ON gr.source_id = rc.id
  WHERE rc.depth < 5  -- Limit depth
)
SELECT * FROM repo_chain ORDER BY depth;
```

### Generated Columns — Auto-compute Fields

```sql
-- Auto-compute venture health score
ALTER TABLE ventures ADD COLUMN health_score INT 
GENERATED ALWAYS AS (
  CASE 
    WHEN status = 'active' THEN 100
    WHEN status = 'paused' THEN 50
    ELSE 0
  END
) STORED;
```

---

## Part 4: Query Examples for Your System

### Phase 1: Wire 7 Capabilities

```sql
-- Find all ventures needing API capability but without repo
SELECT 
  v.id,
  v.name,
  v.sector,
  COUNT(DISTINCT cap) as missing_capabilities
FROM ventures v,
UNNEST(string_to_array(v.required_capabilities, '|')) cap
LEFT JOIN graph_relationships gr ON 
  gr.target_id = v.id AND 
  gr.metadata->>'capability' = cap
WHERE cap IN ('api', 'database', 'authentication', 'dashboard', 'monitoring', 'portfolio', 'security')
  AND gr.id IS NULL
GROUP BY v.id, v.name, v.sector
ORDER BY missing_capabilities DESC
LIMIT 100;

-- Create relationship: repo provides capability to venture
INSERT INTO graph_relationships (id, source_id, target_id, relation_type, metadata)
SELECT 
  gen_uuid(),
  (SELECT id FROM graph_entities WHERE name = 'apollo-server' AND entity_type = 'REPO'),
  v.id,
  'PROVIDES_CAPABILITY',
  ('{"capability": "api", "match_confidence": 0.95}')::jsonb
FROM ventures v
WHERE v.sector = 'EDU' AND v.status = 'active'
ON CONFLICT DO NOTHING;
```

### Phase 2: Workspace Platform Discovery

```sql
-- Ventures needing workspace (collaboration)
SELECT 
  id,
  name,
  sector,
  COUNT(DISTINCT gr.id) as current_capabilities
FROM ventures v
LEFT JOIN graph_relationships gr ON gr.target_id = v.id
WHERE v.required_capabilities::text LIKE '%workspace%'
  AND NOT EXISTS (
    SELECT 1 FROM graph_relationships 
    WHERE target_id = v.id AND relation_type = 'HAS_WORKSPACE'
  )
GROUP BY v.id, v.name, v.sector
ORDER BY COUNT(DISTINCT gr.id) ASC;
```

### Phase 3: Knowledge Graph & Payments

```sql
-- Ventures ready for knowledge graph integration
SELECT 
  id,
  name,
  sector,
  CASE WHEN capability_coverage > 0.8 THEN 'ready' ELSE 'not_ready' END as kg_readiness
FROM (
  SELECT 
    v.id,
    v.name,
    v.sector,
    COUNT(DISTINCT CASE WHEN gr.id IS NOT NULL THEN gr.source_id END)::FLOAT / 
    COUNT(DISTINCT CASE WHEN gr.relation_type = 'REQUIRES_CAPABILITY' THEN 1 END) as capability_coverage
  FROM ventures v
  LEFT JOIN graph_relationships gr ON gr.target_id = v.id
  GROUP BY v.id, v.name, v.sector
) coverage
WHERE capability_coverage > 0.5
ORDER BY capability_coverage DESC;

-- Ventures ready for payment integration
SELECT 
  id,
  name,
  sector,
  estimated_monthly_transactions
FROM ventures
WHERE mrr > 1000 AND status = 'validated'
  AND required_capabilities::text LIKE '%payment%'
ORDER BY mrr DESC;
```

---

## Part 5: Performance Tuning for Your Scale

### Index Strategy (1504 ventures, 700 repos, 3362 entities)

```sql
-- Entity lookups (frequent)
CREATE INDEX idx_entities_type ON graph_entities(entity_type);
CREATE INDEX idx_entities_name ON graph_entities USING gin(name gin_trgm_ops);

-- Relationship queries (most frequent)
CREATE INDEX idx_relationships_source ON graph_relationships(source_id);
CREATE INDEX idx_relationships_target ON graph_relationships(target_id);
CREATE INDEX idx_relationships_type ON graph_relationships(relation_type);

-- Venture queries
CREATE INDEX idx_ventures_sector ON ventures(sector);
CREATE INDEX idx_ventures_status ON ventures(status);

-- JSON queries (capability matching)
CREATE INDEX idx_entities_metadata_capability ON graph_entities USING gin(metadata jsonb_path_ops);
CREATE INDEX idx_relationships_metadata ON graph_relationships USING gin(metadata jsonb_path_ops);
```

### Query Planning

```sql
-- Analyze query cost before running
EXPLAIN ANALYZE
SELECT v.id, v.name, COUNT(DISTINCT r.id) as repo_count
FROM ventures v
LEFT JOIN graph_relationships gr ON gr.target_id = v.id
LEFT JOIN graph_entities r ON gr.source_id = r.id AND r.entity_type = 'REPO'
GROUP BY v.id, v.name;

-- Add ANALYZE BUFFERS for memory info
EXPLAIN (ANALYZE, BUFFERS)
SELECT ...;
```

### Batch Size Optimization

```sql
-- Good: batch 100-1000 rows
INSERT INTO ventures (...) VALUES (...), (...), ... -- 500 rows
RETURNING COUNT(*);

-- Bad: one at a time (1504 × slower)
INSERT INTO ventures (...) VALUES (...);

-- Best: transaction
BEGIN;
INSERT INTO ventures (...) SELECT ... FROM ...;
INSERT INTO graph_relationships (...) SELECT ... FROM ...;
COMMIT;
```

---

## Part 6: Quick Reference Card

| Task | Command | Notes |
|------|---------|-------|
| Generate ID | `gen_uuid()` | Always for new entities |
| Get ID back | `INSERT ... RETURNING id` | Immediate feedback |
| Find by capability | `INNER JOIN ... metadata->>'capability' = 'api'` | JSON extraction |
| Count relationships | `COUNT(DISTINCT target_id)` | Groups by source |
| Find gaps | `LEFT JOIN ... WHERE gr.id IS NULL` | Anti-join pattern |
| Batch insert | `INSERT ... SELECT FROM ... WHERE ...` | 100-1000 rows |
| Rank results | `RANK() OVER (ORDER BY ...)` | Window function |
| Search text | `@@ plainto_tsquery(...)` | Full-text search |
| Multi-tenant | Row Level Security policies | `USING (user_id = auth.uid())` |
| Real-time | `LISTEN channel_name` | Edge functions notify |

---

## Part 7: Execution Checklist for Phase 1

**Week 1: Wire 7 Capabilities**

- [ ] Create indexes (from Part 5)
- [ ] Run capability gap query (from Part 4)
- [ ] Batch insert relationships: API repos → ventures
- [ ] Batch insert relationships: Database repos → ventures
- [ ] Batch insert relationships: Auth repos → ventures
- [ ] Verify coverage with `venture_health_scores` materialized view
- [ ] Repeat for Dashboard, Monitoring, Portfolio, Security

**Commands to Run Each Day:**

```sql
-- Day 1: Check current state
SELECT relation_type, COUNT(*) FROM graph_relationships GROUP BY relation_type;

-- Day 2-7: Add relationships, then check progress
INSERT INTO graph_relationships (...) SELECT ... FROM ...;
SELECT COUNT(*) as relationships_added;

-- End of week: Verify Phase 1 complete
SELECT 
  relation_type,
  COUNT(*) as count,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM graph_relationships), 1) as pct
FROM graph_relationships
GROUP BY relation_type
ORDER BY count DESC;
```

---

**Next Step:** Ready to execute Phase 1. Use task_plan.md to track progress.
