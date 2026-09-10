# Neo4j Capability Registry Graph

**Unit 9: Knowledge Graph Wiring for Capability Registry**

---

## Overview

This directory contains Cypher scripts to wire the Capability Registry into Neo4j as a knowledge graph.

**Graph Model:**
```
Capability ─BELONGS_TO→ Domain
Capability ─REQUIRES_MCP→ MCP
Capability ─ORCHESTRATES→ Capability (composition)
Capability ─INFORMS→ Capability (data flow)
Capability ─STORES_IN→ Capability (storage)
Capability ─AUDITED_BY→ Capability (governance)
```

---

## Files

| File | Purpose | Nodes | Edges |
|------|---------|-------|-------|
| `001_create_capability_nodes.cypher` | Create all nodes + relationships | 15 | 10+ |
| `002_verify_graph.cypher` | Validation queries (10 checks) | N/A | N/A |
| `README.md` | This file | N/A | N/A |

---

## Deployment

### Step 1: Connect to Neo4j

```bash
# Using Neo4j desktop or cloud
# Or via CLI:
neo4j-admin console  # Local
# OR
cypher-shell -u neo4j -p <password> -a bolt://<host>:7687
```

### Step 2: Run creation script

```cypher
// Copy-paste from 001_create_capability_nodes.cypher
// OR run via CLI:
cat 001_create_capability_nodes.cypher | cypher-shell -u neo4j -p <password>
```

### Step 3: Verify

```cypher
// Copy-paste queries from 002_verify_graph.cypher
// Expect 15 nodes (5 Capabilities, 6 Domains, 4 MCPs)
MATCH (n) RETURN labels(n)[0], COUNT(n)
```

---

## Nodes & Relationships

### Capability Nodes (5)

| ID | Name | Fit | Source |
|----|------|-----|--------|
| CAP-001 | Account Research | 95% | Anthropic |
| CAP-003 | Call Summary | 90% | Anthropic |
| CAP-101 | Agentic Patterns | 90% | awesome-claude-code |
| CAP-401 | Librarian MCP | 85% | awesome-claude-code |
| CAP-201 | HIPAA Compliance | 100% | Internal |

### Domain Nodes (6)

- DOM-SALES: Sales & Prospecting (CAP-001, CAP-003)
- DOM-OPS: Operations & Dispatch
- DOM-COMPLIANCE: HIPAA & Compliance (CAP-201)
- DOM-LEARNING: Learning & Training
- DOM-KNOWLEDGE: Knowledge & Memory (CAP-401)
- DOM-INFRA: Infrastructure & Security (CAP-101)

### MCP Nodes (4)

- MCP-SUPABASE: Required by CAP-003, CAP-201
- MCP-NEO4J: (reference)
- MCP-LIBRARIAN: (reference, CAP-401 is this MCP)
- MCP-ANTHROPIC-SALES: (reference, Anthropic plugin)

### Relationships (10+)

| Type | From | To | Count |
|------|------|-----|-------|
| BELONGS_TO | Capability | Domain | 5 |
| REQUIRES_MCP | Capability | MCP | 2 |
| ORCHESTRATES | CAP-101 | CAP-001, CAP-003 | 2 |
| INFORMS | CAP-001 | CAP-003 | 1 |
| STORES_IN | CAP-003 | CAP-401 | 1 |
| AUDITED_BY | CAP-003 | CAP-201 | 1 |

---

## Queries for Phase 1A

### Search by Domain

```cypher
// Find all capabilities in Sales domain
MATCH (c:Capability)-[:BELONGS_TO]->(d:Domain {id: 'DOM-SALES'})
RETURN c.ref_id, c.name, c.healthroute_fit
```

### Search by Fit Score

```cypher
// Find all capabilities with fit >= 80%
MATCH (c:Capability)
WHERE c.healthroute_fit >= 80
RETURN c.ref_id, c.name, c.healthroute_fit ORDER BY c.healthroute_fit DESC
```

### Find Capability Dependencies

```cypher
// What MCPs does CAP-003 require?
MATCH (cap:Capability {id: 'CAP-003'})-[:REQUIRES_MCP]->(mcp:MCP)
RETURN mcp.name, mcp.id
```

### Workflow Composition

```cypher
// Show workflow: research → summary → storage + audit
MATCH (research:Capability {id: 'CAP-001'}),
      (summary:Capability {id: 'CAP-003'}),
      (storage:Capability {id: 'CAP-401'}),
      (audit:Capability {id: 'CAP-201'})
RETURN {
  research: research.name,
  summary: summary.name,
  storage: storage.name,
  audit: audit.name
}
```

### Graph Statistics

```cypher
MATCH (c:Capability)
RETURN {
  total: COUNT(c),
  avg_fit: AVG(c.healthroute_fit),
  min_fit: MIN(c.healthroute_fit),
  max_fit: MAX(c.healthroute_fit)
}
```

---

## Integration with OpenWork MCP

Phase 1A Unit 10 (search_capabilities) will query this graph:

```python
# Pseudo-code for Unit 10
def search_capabilities(domain=None, fit_gte=80):
    cypher = """
        MATCH (c:Capability)
        WHERE ($domain IS NULL OR (c)-[:BELONGS_TO]->(:Domain {id: $domain}))
          AND c.healthroute_fit >= $fit_gte
        RETURN c.ref_id, c.name, c.healthroute_fit
        ORDER BY c.healthroute_fit DESC
    """
    return neo4j_query(cypher, domain=domain, fit_gte=fit_gte)
```

---

## Validation Checklist

- [ ] 15 nodes created (5 Cap, 6 Dom, 4 MCP)
- [ ] 5 Capability nodes exist
- [ ] All 5 have BELONGS_TO edges to domains
- [ ] CAP-003 and CAP-201 have REQUIRES_MCP edges to MCP-SUPABASE
- [ ] CAP-101 ORCHESTRATES CAP-001 and CAP-003
- [ ] CAP-001 INFORMS CAP-003
- [ ] CAP-003 STORES_IN CAP-401
- [ ] CAP-003 AUDITED_BY CAP-201
- [ ] All fit scores correct (95, 90, 90, 85, 100)
- [ ] 10 verification queries pass

---

## Next Steps

**Unit 10:** Implement `search_capabilities()` in OpenWork MCP
- Query this Neo4j graph
- Return capabilities matching domain + fit score + tags
- Cache results in Supabase for performance

**Unit 11:** Implement `execute_capability()`
- Route to correct MCP/tool based on capability type
- Log execution to Supabase + Neo4j

---

## Troubleshooting

**No nodes created?**
- Check Neo4j connection
- Verify credentials
- Run `MATCH (n) RETURN COUNT(n)` to confirm empty database

**Duplicate nodes?**
- Run queries in `002_verify_graph.cypher` (idempotent)
- If duplicates exist, delete and re-run: `MATCH (n) DETACH DELETE n`

**Missing relationships?**
- Check that MATCH clauses find the right nodes
- Verify node IDs match exactly (case-sensitive)

---

**Unit 9 Status:** ✅ Complete  
**Timeline:** Sep 16 (Phase 1A deployment)  
**Next:** Unit 10 — Implement search_capabilities() (Sep 17)

