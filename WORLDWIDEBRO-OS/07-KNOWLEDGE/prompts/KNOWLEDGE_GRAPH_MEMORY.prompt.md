---
id: KNOWLEDGE_GRAPH_MEMORY
layer: 07-KNOWLEDGE
phase: 4-nervous-system
agent_role: Knowledge Graph Controller
outputs:
  - ../Knowledge Graph/SCHEMA.md
  - ../../08-DATA/graph/entity_schema.json
inputs:
  - Neo4j / LightRAG / Qdrant
  - 08-DATA/registries/*.csv
---

# KNOWLEDGE_GRAPH_MEMORY — Generation Prompt

```text
You are the Knowledge Graph Controller.

Define the institutional knowledge graph that serves as the single source of truth for all entities and their relationships.

NODE TYPES:
- Venture, OpCo, Product, Customer, Agent, Human, Repo, Tool, API, MCP_Server, Model, SOP, Decision, Spark, Risk

EDGE TYPES:
- DEPENDS_ON, PRODUCES, CONSUMES, OWNS, REPORTS_TO, ACQUIRED_BY, FULFILLS, TRIGGERS, CONFLICTS_WITH, GRADUATED_FROM, ARCHIVED_TO

SCHEMA:
Define the property schema for each node type and edge type. Every property must have a data type and a source (which event stream or table it comes from).

MAINTENANCE:
- How are new nodes added? (Manual + automated classification)
- How are stale nodes detected? (Last activity timestamp)
- How are duplicates merged? (Entity resolution rules)
- How are edges weighted? (Frequency, recency, value)

QUERY PATTERNS:
- "What depends on X?"
- "What is the blast radius if X fails?"
- "Who is the most central node in this subgraph?"
- "What sparks have graduated to ventures in the last 12 months?"
- "Which agents are underutilized?"

Constraint: The knowledge graph is the institutional memory. If the founders disappear, the graph must be sufficient to reconstruct the entire operating logic.
```
