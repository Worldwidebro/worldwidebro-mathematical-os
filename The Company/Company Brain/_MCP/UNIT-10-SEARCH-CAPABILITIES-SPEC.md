# Unit 10: search_capabilities() MCP Tool

**Specification & Validation Plan**

---

## Overview

Implement the first MCP tool for OpenWork: `search_capabilities()` 

This tool queries the Neo4j capability graph and Supabase metadata to discover capabilities by domain, fit score, tags, and MCP dependencies.

---

## Function Signature

```python
def search_capabilities(
    domain: Optional[str] = None,
    fit_gte: int = 80,
    tags: Optional[List[str]] = None,
    requires_mcp: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search Capability Registry by multiple dimensions.
    
    Returns:
    {
        'capabilities': [
            {'id', 'ref_id', 'name', 'fit', 'source', 'gap', 'use_case', ...}
        ],
        'count': int,
        'query_params': {...},
        'timestamp': str
    }
    """
```

---

## Test Cases (10)

| # | Test Name | Parameters | Expected Count | Expected Fits | Status |
|----|-----------|-----------|-----------------|----------------|--------|
| 1 | Search by domain (Sales) | `domain='DOM-SALES'` | 2 | [95, 90] | 🔲 |
| 2 | Search by fit >= 80 | `fit_gte=80` | 5 | [100, 95, 90, 90, 85] | 🔲 |
| 3 | Search by fit >= 90 | `fit_gte=90` | 3 | [100, 95, 90] | 🔲 |
| 4 | Search by MCP | `requires_mcp='MCP-SUPABASE'` | 2 | [100, 90] | 🔲 |
| 5 | Domain + fit filter | `domain='DOM-SALES', fit_gte=90` | 2 | [95, 90] | 🔲 |
| 6 | Domain + high fit | `domain='DOM-SALES', fit_gte=95` | 1 | [95] | 🔲 |
| 7 | Compliance domain | `domain='DOM-COMPLIANCE'` | 1 | [100] | 🔲 |
| 8 | Knowledge domain | `domain='DOM-KNOWLEDGE'` | 1 | [85] | 🔲 |
| 9 | Infra domain | `domain='DOM-INFRA'` | 1 | [90] | 🔲 |
| 10 | Empty search (all) | `{}` | 5 | [100, 95, 90, 90, 85] | 🔲 |

**Passing all 10 tests = ✅ Unit 10 DONE**

---

## Implementation Details

### Data Sources

**Neo4j Graph:**
- Capability nodes (5): CAP-001, CAP-003, CAP-101, CAP-401, CAP-201
- Domain nodes (6): DOM-SALES, DOM-COMPLIANCE, etc.
- MCP nodes (4): MCP-SUPABASE, MCP-NEO4J, etc.
- Relationships: BELONGS_TO, REQUIRES_MCP

**Supabase Table:**
- Enrichment: use_case, gap, owner, approval_status, tags

### Query Logic

```cypher
MATCH (c:Capability)
WHERE c.healthroute_fit >= $fit_gte
  AND (($domain IS NULL) OR (c)-[:BELONGS_TO]->(:Domain {id: $domain}))
  AND (($mcp IS NULL) OR (c)-[:REQUIRES_MCP]->(:MCP {id: $mcp}))
  AND (($tags IS NULL) OR ANY(tag IN $tags WHERE tag IN c.tags))
RETURN c.* ORDER BY c.healthroute_fit DESC
```

### Performance Notes

- Neo4j indexes on: `healthroute_fit`, `id`, relationships
- Supabase batch fetch (max 5 items per call)
- Cache results in Redis (optional, Phase 1B)

---

## Success Criteria

✅ **Functional:**
- All 10 test cases pass
- Results sorted by fit_score (descending)
- Enrichment from Supabase working
- Validation checks pass

✅ **Performance:**
- Query latency < 500ms (single query)
- Batch enrichment < 1s (5 items)
- No N+1 queries

✅ **Error Handling:**
- Graceful fallback if Supabase unavailable
- Clear error messages
- No crashes on invalid domain/mcp

---

## Integration Points

**Unit 11 (execute_capability):**
- Takes `capability_id` from search results
- Routes execution based on `source` (anthropic, awesome-claude-code, internal)

**Unit 13 (Orchestrator):**
- Uses search to populate `_extract_inputs()`
- Routes capabilities by ID

**Unit 14-15 (Testing):**
- Test workflows using search + execute chains

---

## Deployment

**Sep 17 (Phase 1A):**
1. Deploy Neo4j graph (Unit 9)
2. Deploy Supabase data (Unit 8)
3. Implement search_capabilities() (Unit 10)
4. Test against 10 test cases
5. If all pass → proceed to Unit 11

**Code location:** `_MCP/openwork_mcp_tools.py`

**Dependencies:**
- neo4j-driver
- supabase-py
- Python 3.9+

---

## Validation Checklist

Before marking Unit 10 complete:

- [ ] All 10 test cases pass
- [ ] Capabilities sorted by fit (descending)
- [ ] Enrichment working (use_case, gap, owner)
- [ ] Error handling for invalid params
- [ ] Latency < 500ms per query
- [ ] Code reviewed
- [ ] Unit 11 ready (execute_capability)

---

**Status:** Ready for implementation (Sep 17)  
**Est. time:** 30 min  
**Blockers:** None (Unit 9 complete)

