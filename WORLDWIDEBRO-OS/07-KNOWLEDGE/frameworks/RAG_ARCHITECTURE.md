# RAG & Knowledge Retrieval Architecture: IZA OS

This document outlines the **Retrieval-Augmented Generation (RAG) Architecture** used by IZA OS to feed long-term context, codebase intelligence, and company playbooks to active agents.

---

## 1. The RAG pipeline Flow

```
[Data Sources] ──> [Ingestion & Processing] ──> [Embedding (Nomic)]
                                                       │
[Agent Action] <── [Hermes Query] <── [Qdrant (Vector) + Neo4j (Graph)]
```

---

## 2. Layer-by-Layer Implementation

### A. Data Sources
*   **Human Knowledge**: Local Markdown notes, SOPs, and playbooks stored in [07-KNOWLEDGE/Obsidian/](file:///Users/acebless/Documents/WORLDWIDEBRO-OS/07-KNOWLEDGE/Obsidian/).
*   **Engineering/Codebase**: Source code files, package manifests, and dependencies across 1,647 repositories (866 owned + 781 starred).
*   **Business Records**: Transactions, project ledgers, and subcontractor logs in PostgreSQL.

### B. Ingestion & Document Processing
*   **GitHub Ingestion**: [scan_repositories.py](file:///Users/acebless/Documents/scan_repositories.py) parses repository metadata, star counts, and primary languages.
*   **Note Ingestion**: [obsidian_graph_sync.py](file:///Users/acebless/Documents/obsidian_graph_sync.py) parses local Markdown files to extract entities and metadata.
*   **Parser & Cleaning**: Unstructured.io, PyMuPDF, and custom Regex parsers clean code docstrings and document text.

### C. Chunking & Embeddings
*   **Semantic Chunking**: Split documents into logical 500-to-1000 token blocks preserving headers, lists, and code blocks.
*   **Embedding Model**: Local text embedding layer using `nomic-embed-text` (via Ollama port `11434` or LiteLLM gateway).

### D. Double-Engine Storage (The Memory Layer)
*   **Vector Database (Qdrant)**:
    *   *Collections*: `notes` (Obsidian note embeddings) and `repositories` (codebase summaries).
    *   *Purpose*: High-speed semantic similarity searches.
*   **Graph Database (Neo4j)**:
    *   *Schema*: `(Repo:Repository)-[:IMPLEMENTS]->(Cap:Capability)<-[:NEEDS]-(Ven:Venture)`.
    *   *Purpose*: Resolving complex capability alignments, dependencies, and ownership linkages.

### E. Hybrid & Agentic Retrieval
*   **Retrieve Loop ([retrieve.py](file:///Users/acebless/Documents/retrieve.py))**:
    1.  Receives natural language query from Hermes / active agent.
    2.  Performs semantic vector search in Qdrant.
    3.  Queries Neo4j via Cypher to enrich search results with relational context (owner, sector, dependent repos).
    4.  Assembles final context window and feeds it to the LLM.

### F. Observability & Tracing
*   **Langfuse (Port 3003)**: Tracks agent execution runs, prompt latency, token costs, and retrieval success metrics.
*   **Neo4j Graph Dashboard**: Visualizes node-edge relationships in real-time.
