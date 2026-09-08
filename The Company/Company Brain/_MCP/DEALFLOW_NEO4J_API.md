# DealFlowOS Neo4j API

REST API wrapper for DealFlowOS dashboard that queries Neo4j knowledge graph for real company and deal pipeline data.

## Quick Start

```bash
# Start the API server (requires python3-neo4j)
python3 _MCP/dealflow_neo4j_api.py

# Server runs on http://localhost:8081
# Open dealflow-os.html in browser — it will load real data from Neo4j
```

## API Endpoints

### `GET /api/companies`
Returns all researched companies from Neo4j.

**Query Parameters:**
- `limit` (optional, default: 150) — max companies to return

**Response:**
```json
{
  "success": true,
  "count": 148,
  "data": [
    {
      "id": "VEN-000001",
      "name": "BuildRight Construction",
      "industry": "construction",
      "website": "https://buildright.com",
      "score": 92,
      "location": "Austin, TX",
      "sector": "Construction",
      "capabilities": 5,
      "stage": "researched"
    }
  ]
}
```

**Fields:**
- `id` — Venture/Company ID from Neo4j
- `name` — Company name
- `industry` — Industry classification
- `website` — Company website URL
- `score` — Research score (0-100, default 75)
- `location` — Company location
- `sector` — Business sector
- `capabilities` — Number of mapped capabilities
- `stage` — Deal stage (discovered, researched, qualified, contacted, negotiating, closed)

---

### `GET /api/companies/:id`
Returns detailed enrichment for a specific company.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "VEN-000001",
    "name": "BuildRight Construction",
    "industry": "construction",
    "website": "https://buildright.com",
    "founded": "2015",
    "employees": "250-500",
    "score": 92,
    "summary": "Regional construction company specializing in commercial builds",
    "location": "Austin, TX",
    "sector": "Construction",
    "stage": "researched",
    "capabilities": [
      {
        "name": "Project Management",
        "type": "core"
      },
      {
        "name": "Safety Compliance",
        "type": "support"
      }
    ],
    "contacts": [
      {
        "name": "John Smith",
        "email": "john@buildright.com",
        "title": "CEO"
      }
    ]
  }
}
```

---

### `GET /api/pipeline/by-stage`
Returns deal pipeline grouped by stage (discovered, researched, qualified, contacted, negotiating, closed).

**Response:**
```json
{
  "success": true,
  "data": {
    "discovered": {
      "count": 45,
      "companies": [
        {
          "id": "VEN-000001",
          "name": "BuildRight Construction",
          "score": 92,
          "industry": "construction"
        }
      ]
    },
    "researched": {
      "count": 38,
      "companies": [...]
    },
    "qualified": {
      "count": 24,
      "companies": [...]
    },
    "contacted": {
      "count": 18,
      "companies": [...]
    },
    "negotiating": {
      "count": 8,
      "companies": [...]
    },
    "closed": {
      "count": 15,
      "companies": [...]
    }
  }
}
```

---

### `GET /api/dashboard/summary`
Returns dashboard summary metrics.

**Response:**
```json
{
  "success": true,
  "data": {
    "total_companies": 148,
    "total_deals": 15,
    "avg_score": 78.5,
    "active_deals": 24,
    "pipeline_value": 4200000
  }
}
```

---

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "dealflow-neo4j-api"
}
```

## Configuration

Environment variables (optional):

```bash
export NEO4J_URI=bolt://100.87.214.70:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=changeme
```

Default values:
- `NEO4J_URI`: `bolt://100.87.214.70:7687`
- `NEO4J_USER`: `neo4j`
- `NEO4J_PASSWORD`: `changeme`

## How DealFlowOS Uses the API

The `dealflow-os.html` dashboard automatically:

1. **On load:** Fetches `/api/companies`, `/api/pipeline/by-stage`, and `/api/dashboard/summary`
2. **Dashboard view:** Displays summary cards with real metrics
3. **Pipeline view:** Shows kanban board with companies in each stage
4. **Companies view:** Lists all researched companies sorted by score
5. **Real-time:** All views update as Neo4j data changes

## Neo4j Query Details

### Companies Query
Matches all `Company` nodes and optionally joins with:
- `Capability` nodes (HAS_CAPABILITY relationship)
- `Location` nodes (LOCATED_IN relationship)
- `Sector` nodes (IN_SECTOR relationship)

Returns companies sorted by score (highest first).

### Pipeline Query
Groups companies by `stage` property with stage order:
1. discovered
2. researched
3. qualified
4. contacted
5. negotiating
6. closed

### Dashboard Summary
Counts distinct companies, deals, and sums pipeline values.

## Integration with ClickUp

When a deal is created in DealFlowOS:
1. Company is created/updated in Neo4j
2. Stage is set to `researched`
3. Task can be created in ClickUp via MCP bridge
4. Pipeline view updates automatically

## Troubleshooting

**Error: Connection refused**
- Ensure Neo4j is running: `docker --context macstudio ps`
- Verify connection: `curl http://100.87.214.70:7474`

**Error: Authentication failed**
- Check Neo4j credentials in environment variables
- Default password is `changeme` — consider changing it

**Empty data returned**
- Ensure companies exist in Neo4j
- Check: `cypher-shell -u neo4j -p changeme "MATCH (c:Company) RETURN COUNT(c)"`

**CORS errors in browser**
- API allows all origins (`Access-Control-Allow-Origin: *`)
- Check browser console for actual error

## File Locations

- **API Server:** `/Users/acebless/Documents/The Company/Company Brain/_MCP/dealflow_neo4j_api.py`
- **Dashboard:** `/Users/acebless/Documents/The Company/Company Brain/dealflow-os.html`
- **This doc:** `/Users/acebless/Documents/The Company/Company Brain/_MCP/DEALFLOW_NEO4J_API.md`
