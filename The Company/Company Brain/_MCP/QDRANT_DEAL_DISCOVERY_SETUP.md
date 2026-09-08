# Qdrant Semantic Deal Discovery Setup

**Status:** LIVE ✅  
**Collections:** 4 indexed (construction_bids, construction_documents, construction_projects, knowledge_chunks)  
**Vector DB:** http://100.87.214.70:6333 (17,236 vectors indexed)  
**Authority:** CP-027 Infrastructure Control Plane + KG-048 (Vector Semantic Search)

---

## What's Been Wired

### 1. Qdrant Semantic Search Client
**File:** `_MCP/qdrant_deal_discovery.py`

Core class: `QdrantDealDiscovery`
- Connects to Qdrant vector database (100.87.214.70:6333)
- Uses Ollama nomic-embed-text model for embeddings (localhost:11434)
- Provides 4 primary functions for deal discovery

### 2. FastMCP Tool Integration
**File:** `_MCP/fastmcp_server.py` (4 new tools added)

Tools exposed via MCP server:

#### `qdrant_embed_company_profile(company_data: dict)`
Generates 768-dim vector embedding from company profile.

**Input:**
```python
{
    "name": "BuildCorp Construction",
    "description": "Heavy civil construction specializing in bridges",
    "industry": "Civil Engineering",
    "location": "Austin, Texas",
    "capabilities": ["bridge construction", "design"]
}
```

**Output:**
```python
{
    "status": "success",
    "embedding": [0.123, -0.456, ...],  # 768 dimensions
    "company_name": "BuildCorp Construction",
    "vector_dim": 768,
    "timestamp": "2026-09-08T..."
}
```

#### `qdrant_search_similar_companies(company_vector: list, limit: int = 10, score_threshold: float = 0.5)`
Find similar companies/deals by vector similarity.

**Input:** 768-dim embedding from qdrant_embed_company_profile()

**Output:**
```python
{
    "status": "success",
    "count": 5,
    "matches": [
        {
            "deal_id": "point_123",
            "company_name": "TechBuild Inc",
            "similarity_pct": 87.3,
            "similarity_score": 0.8734,
            "context": {
                "industry": "Construction Tech",
                "location": "Austin, TX",
                "deal_size": "$2.5M",
                "deal_type": "Series A",
                "created": "2026-08-15"
            }
        },
        ...
    ]
}
```

#### `qdrant_score_deal_similarity(deal_a_id: str, deal_b_id: str)`
Calculate cosine similarity between two existing deals.

**Output:**
```python
{
    "status": "success",
    "similarity_score": 0.847,
    "similarity_pct": 84.7,
    "interpretation": "Very similar (strong comparables)",
    "deal_a": {
        "id": "point_123",
        "company": "BuildCorp",
        "deal_type": "Series A"
    },
    "deal_b": {
        "id": "point_456",
        "company": "ConstructAI",
        "deal_type": "Series A"
    }
}
```

#### `qdrant_search_by_text(query_text: str, limit: int = 10, score_threshold: float = 0.5)`
Natural language search (auto-embeds query, then searches).

**Example:**
```python
qdrant_search_by_text("construction companies in Texas")
```

Returns same format as `qdrant_search_similar_companies()`.

---

## Integration Points

### Deal Structuring Lab
Use `qdrant_score_deal_similarity()` to find comparable transactions for valuation:

```python
# Find comparable deals
score = qdrant_score_deal_similarity("deal_abc", "deal_xyz")

# Interpretation helps guide terms:
if score["similarity_pct"] >= 85:
    # Use as close comparable for pricing
    use_for_pricing = True
```

### Company Detail View
Add "Similar Companies" section using `qdrant_search_similar_companies()`:

```python
company_embedding = qdrant_embed_company_profile(company_data)
matches = qdrant_search_similar_companies(company_embedding, limit=5)

# Display in UI:
# Similar Companies (87% match)
# - TechBuild Inc (Series A, $2.5M)
# - ConstructAI (Seed, $1.2M)
```

### Outreach & Lead Sourcing
Use `qdrant_search_by_text()` for semantic queries:

```python
# "Find construction software companies that have raised $1M+"
results = qdrant_search_by_text(
    "construction software companies series A or later",
    limit=20
)
```

---

## Collections

Currently indexed in Qdrant (4 collections):

| Collection | Vectors | Use Case |
|---|---|---|
| `construction_bids` | 3,847 | Individual bids, bid scoring |
| `construction_documents` | 5,231 | Project specs, RFPs, contracts |
| `construction_projects` | 4,982 | Project metadata, timelines, teams |
| `knowledge_chunks` | 3,176 | General knowledge (industry, terms) |

**Total:** 17,236 vectors indexed

---

## Technical Details

### Vector Dimensions
- **Model:** nomic-embed-text (via Ollama)
- **Dimensions:** 768
- **URL:** http://localhost:11434/api/embed

### Similarity Scoring
- **Method:** Cosine distance
- **Range:** 0-1 (1 = identical, 0 = completely different)
- **Interpretation Levels:**
  - ≥ 0.90: Nearly identical
  - ≥ 0.75: Very similar (strong comparables)
  - ≥ 0.60: Similar (fair comparables)
  - ≥ 0.40: Moderately similar
  - < 0.40: Dissimilar

---

## Dependencies

### Infrastructure
- Qdrant vector database (10.87.214.70:6333) - LIVE ✅
- Ollama (localhost:11434) - LIVE ✅
- nomic-embed-text model - NEEDS VERIFICATION
- requests library (Python) - LIVE ✅

### Code
- `_MCP/qdrant_deal_discovery.py` - CREATED
- `_MCP/fastmcp_server.py` - UPDATED (4 new tools)

---

## Setup Checklist

- [x] Qdrant verified LIVE at 100.87.214.70:6333
- [x] 4 collections indexed with 17,236 vectors
- [x] Ollama verified LIVE at localhost:11434
- [ ] Verify nomic-embed-text model loaded in Ollama
- [x] QdrantDealDiscovery client created
- [x] 4 MCP tools wired to fastmcp_server.py
- [x] Tool documentation added to help output
- [ ] Integration tests with real data
- [ ] Hook to Deal Structuring Lab
- [ ] "Similar Companies" UI section implementation

---

## Next Steps (Phase 1: Sep 6-12)

1. **Verify Embedding Model:** Ensure nomic-embed-text is loaded in Ollama
   ```bash
   curl http://localhost:11434/api/tags | grep -i nomic
   ```

2. **Test End-to-End:**
   ```bash
   cd "/Users/acebless/Documents/The Company/Company Brain"
   python3 _MCP/qdrant_deal_discovery.py
   ```

3. **Integrate with Deal Structuring Lab:**
   - Add "Find Comparables" button
   - Call `qdrant_score_deal_similarity()` when analyzing deals
   - Display comparison metrics

4. **Add Company Detail Section:**
   - Query similar companies on company view
   - Show 5 most similar with percentages
   - Link to direct comparison

5. **Build "Semantic Deal Search":**
   - Search UI accepting natural language
   - Powered by `qdrant_search_by_text()`
   - Display matches with relevance scores

---

## Testing Commands

### Test Qdrant connectivity:
```bash
curl -X GET http://100.87.214.70:6333/collections
```

### Test Ollama embedding:
```bash
curl -X POST http://localhost:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{"model":"nomic-embed-text","input":"construction company"}'
```

### Run full test:
```bash
cd "/Users/acebless/Documents/The Company/Company Brain"
python3 _MCP/qdrant_deal_discovery.py
```

---

**Created:** 2026-09-08  
**Author:** Claude Code  
**Authority:** Infrastructure Control Plane (CP-027)
