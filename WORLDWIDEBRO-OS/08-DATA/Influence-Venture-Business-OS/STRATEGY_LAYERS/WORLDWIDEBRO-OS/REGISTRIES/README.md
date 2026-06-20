# REGISTRIES: Master Data for Operating Brain

**Location:** `/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/`

This folder contains the **unified data layer** that enables agents to query "What do I need to build X?" and get a complete answer.

---

## Files in This Registry

### 1. **capabilities-taxonomy.json** 
**What:** Master list of all capabilities with adoption rates  
**Use:** Query which capabilities are mature, which need more repos, which ventures need what

### 2. **ventures-capabilities-parsed.json**
**What:** Each venture mapped to required capabilities  
**Use:** Query "What does Wave need?" → [api, database, authentication, dashboard, monitoring, payment]

### 3. **repos-by-capability.json**
**What:** Each capability to repos that provide it  
**Use:** Query "What repos provide authentication?" → [list of 200+ options, ranked by maturity]

### 4. **capability-component-repo-linkage.json** ⭐ MASTER FILE
**What:** Complete linkage of capability → repos → ventures  
**This is the KEY file agents use for "Build X" queries**

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Venture-level capabilities | 11 (api, database, auth, dashboard, monitoring, portfolio, security, workspace, knowledge-graph, payment, construction) |
| Repo-level capabilities | 1,276 (granular definitions) |
| Ventures mapped | 618 |
| Repos mapped | 536 |
| Mature capabilities (>100 ventures) | 8 |
| Established capabilities (20-100) | 2 |
| Emerging capabilities (<20) | 1,269 |

---

## How Agents Use This

**Query: "Build Wave Rideshare"**
1. Lookup Wave in `ventures-capabilities-parsed.json`
2. Find: required_capabilities: [api, database, auth, dashboard, monitoring, payment]
3. For each capability, lookup in `capability-component-repo-linkage.json`
4. Get: repos_providing (ranked by adoption) + maturity level
5. Return: Top 3 repos per capability + implementation docs + SOPs

---

## Key Findings

### 🟢 Mature Capabilities (Production-Ready)
- api (618 ventures, 100%)
- database (618 ventures, 100%)
- authentication (511 ventures, 83%)
- dashboard (389 ventures, 63%)
- monitoring (320 ventures, 52%)
- portfolio (209 ventures, 34%)
- security (157 ventures, 25%)
- workspace (104 ventures, 17%)

### 🟡 Established (Growing)
- knowledge-graph (72 ventures, 12%)
- payment (47 ventures, 8%)

### 🔵 Emerging (Needs Investment)
- construction (20 ventures, 3%)
- [1,269 other specialized capabilities]

### ⚠️ Single Points of Failure
**983 capabilities have only 1 repo solution** — if that repo breaks, no alternatives

### ✅ Well-Served
**293 capabilities have multiple repo options** — mature/redundant

---

## Integration Points

### Supabase
```sql
CREATE TABLE capabilities (
  capability_id VARCHAR,
  name VARCHAR,
  ventures_requiring INT,
  adoption_rate VARCHAR,
  maturity VARCHAR
);

CREATE TABLE venture_capabilities (
  venture_id VARCHAR,
  capability VARCHAR,
  FOREIGN KEY (venture_id) REFERENCES ventures(venture_id),
  FOREIGN KEY (capability) REFERENCES capabilities(name)
);
```

### DuckDB
```bash
# Import registries
duckdb worldwidebro_os.duckdb << 'SQL'
COPY (SELECT * FROM read_json_auto('capabilities-taxonomy.json'))
TO capabilities.parquet;
SQL
```

### Grafana Dashboards
- "Capability Maturity" (pie chart)
- "Repo Reusability by Ventures" (bar chart)
- "Capability Coverage by Sector" (heatmap)

### Agent Queries
```python
import json

# Load master
with open('capability-component-repo-linkage.json') as f:
    registry = json.load(f)

# Query: "What does authentication need?"
auth = next(l for l in registry['linkages'] if l['capability'] == 'authentication')
print(f"Authentication: {len(auth['repos_providing'])} repos, {auth['adoption']['ventures_requiring']} ventures")
```

---

## Governance

**Update procedure:**
1. Update CSVs in venture-hub/
2. Run: `python3 extract_capabilities_taxonomy.py`
3. Regenerates all 4 JSON files
4. Sync to Supabase/DuckDB/Grafana

**Version:** 2026-06-04 (11 venture-level capabilities, 618 ventures, 536 repos)
