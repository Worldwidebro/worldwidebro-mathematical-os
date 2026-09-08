# MEMORY-RELATIONSHIPS — Graph Associations and Neo4j Schema

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE]] | [[_PROMPTS/04_CONNECTION-REASONING|04_CONNECTION-REASONING]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-REL-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Graph Associative Memory

Simple vector stores retrieve documents based on text similarity, but cannot answer structural questions such as:
- *"What depends on this service?"*
- *"Who owns this venture, and what repository implements its backend?"*
- *"If this container crashes, which 12 ventures fail?"*

This capability is provided by the **Neo4j Relational Graph** (`bolt://100.87.214.70:7687`).

---

## 2. Core Node Labels

- `:Venture` (713 nodes, e.g. `{id: 'CON-001', name: 'Ace Construction', sector: 'SEC-002'}`)
- `:Sector` (35 nodes, `SEC-001` to `SEC-035`)
- `:Repository` (893 owned `:OwnedRepo`, 904 external `:ExternalRepo`)
- `:Capability` (~300 nodes, `CAP-*`)
- `:System` (OmniRoute, Neo4j, Qdrant, LiteLLM, Tailscale, Bitwarden)
- `:Host` (Mac Studio `100.87.214.70`, MacBook Air `100.121.17.63`)
- `:ControlPlane` (`CP-001` to `CP-034`)
- `:Decision` (ADR nodes)

---

## 3. Core Edge Predicates

```text
(:Venture)-[:BELONGS_TO_SECTOR]->(:Sector)
(:Venture)-[:IMPLEMENTED_BY]->(:OwnedRepo)
(:OwnedRepo)-[:DEPENDS_ON]->(:ExternalRepo)
(:ExternalRepo)-[:PROVIDES_CAPABILITY]->(:Capability)
(:Capability)-[:GOVERNED_BY]->(:ControlPlane)
(:System)-[:HOSTED_ON]->(:Host)
(:System)-[:SECURED_BY]->(:System {name: 'Bitwarden'})
(:Decision)-[:CAUSED]->(:Action)-[:PRODUCED]->(:Outcome)
```

---

## 4. Traversals

- **Blast Radius Analysis**: Find all ventures impacted by taking down an infrastructure system:
  ```cypher
  MATCH (s:System {name: 'Neo4j'})<-[:DEPENDS_ON*1..3]-(v:Venture)
  RETURN v.id, v.name, v.sector;
  ```
- **Capability Gap Resolution**: Find external starred repos that supply missing capabilities to owned ventures:
  ```cypher
  MATCH (v:Venture)-[:NEEDS_CAPABILITY]->(c:Capability)<-[:PROVIDES_CAPABILITY]-(ext:ExternalRepo)
  WHERE NOT (v)-[:IMPLEMENTED_BY]->()-[:PROVIDES_CAPABILITY]->(c)
  RETURN v.id, c.id, ext.name, ext.github_url;
  ```
