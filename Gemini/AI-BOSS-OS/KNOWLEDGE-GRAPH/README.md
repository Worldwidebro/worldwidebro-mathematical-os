# KNOWLEDGE GRAPH LAYER
## Graph Databases & Semantic Query Registries for AI Agents

---

## 1. Purpose
This folder contains the schemas, constraints, and custom Cypher queries mapping relationships across the entire Civilization OS ecosystem.

## 2. Infrastructure Setup
The knowledge graph is hosted inside the Mac Studio Node:
- **Port**: `7687` (Bolt) / `7474` (HTTP UI)
- **Credentials**: `neo4j/ventures2026`
- **Volume Mount**: `/Volumes/LaCie/fast/AI/graph`

## 3. Dependency Path Hierarchy
To ensure correct GraphRAG retrieval patterns, all AI agents and scanners query dependencies sequentially:
```text
(Repository) -[:IMPLEMENTS]-> (Capability) -[:REQUIRES]-> (Skill) -[:RUNS_ON]-> (Agent) -[:EXECUTES]-> (Workflow) -[:PART_OF]-> (Venture) -[:FEEDS]-> (RevenueModel)
```

## 4. APOC & Cypher Plugins
- **apoc.export.json**: Exports graph states to registry files.
- **neo4j-graphrag-skill**: Python package v1.16.0+ hybrid vector and Cypher queries execution gateway.
