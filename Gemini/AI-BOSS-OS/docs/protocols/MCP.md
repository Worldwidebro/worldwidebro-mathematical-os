# Model Context Protocol (MCP) Integration Specification

This protocol document details how **Hermes** utilizes the **Model Context Protocol (MCP)** to interact with resources, databases, and filesystem systems in the AI-BOSS-OS workspace.

## 1. System Map

Hermes connects to local and remote MCP servers to access core company systems. The control plane uses three primary database connections:

```text
                     +--------------+
                     | Hermes Agent |
                     +------+-------+
                            |
                     +------v-------+
                     |  MCP Client  |
                     +------+-------+
                            |
         +------------------+------------------+
         |                  |                  |
         v                  v                  v
+--------+--------++--------+--------++--------+--------+
|   Filesystem    ||      Neo4j       ||     Qdrant     |
|   MCP Server    ||    MCP Server    ||   MCP Server   |
+--------+--------++--------+--------++--------+--------+
         |                  |                  |
         v                  v                  v
  [Local Workspace]  [Knowledge Graph]  [Vector Memory]
  (/AI-BOSS-OS)       (Tailscale Link)   (Local Host)
```

---

## 2. Server Configuration Templates

Hermes configures MCP servers in its global runtime configuration files.

### 2.1 Filesystem Server
Allows the agent to write files, examine logs, and perform workspace structural edits.

```yaml
mcp_servers:
  filesystem:
    command: npx
    args:
      - "-y"
      - "@modelcontextprotocol/server-filesystem"
      - "/Users/acebless/Documents/Gemini"
```

### 2.2 GitHub Server
Exposes tools to query issues, create PRs, commit code, and review history across git-nexus projects.

```yaml
mcp_servers:
  github:
    command: npx
    args:
      - "-y"
      - "@modelcontextprotocol/server-github"
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
```

### 2.3 Knowledge Graph (Neo4j) Server
Binds natural language capabilities to Cypher queries, reading and writing nodes directly into Neo4j.

```yaml
mcp_servers:
  neo4j-graph:
    command: python3
    args:
      - "-m"
      - "services.mcp_gateway"
    env:
      NEO4J_URI: "bolt://100.87.214.70:7687"
      NEO4J_USERNAME: "neo4j"
      NEO4J_PASSWORD: "ventures2026"
```

---

## 3. Tool Discovery and Execution Lifecycle

1. **Discovery**: Upon startup, Hermes connects to configured MCP endpoints via `stdio` or `Server-Sent Events (SSE)`, requesting available tools.
2. **Registration**: Tools are parsed and registered under the agent's action space (e.g., `github_create_pull_request`, `neo4j_run_cypher`).
3. **Execution**: When a model calls a tool:
   - Hermes verifies execution permissions against security policies.
   - The command executes, returning results back to the model context.
   - Operations and outputs are tracked in the observability pipeline (Langfuse).
