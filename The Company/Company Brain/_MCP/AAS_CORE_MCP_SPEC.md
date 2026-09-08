# AAS Core MCP Integration Specification

> **Server Name:** `agentic-awesome-skills`  
> **Source Repository:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) (46,000+ stars)  
> **Package Version:** `agentic-awesome-skills@16.9.1`  
> **Authority:** Infrastructure Control Plane (CP-027) & Model Control Plane (CP-007)  
> **Role:** Dynamic, Read-Only Skill Discovery & Stack Composition Engine

---

## 1. Architectural Purpose

Company Brain maintains a lean local repository footprint to avoid context window degradation and token exhaustion. While core agent personas (from `agency-agents`) and official infrastructure skills (from `VoltAgent`) are resident in [`.agents/skills/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/.agents/skills), the wider universe of **2,113+ community skills** is made available dynamically via the **AAS Core local MCP server**.

```
Coding Agent (Antigravity / Claude Code)
  │
  ├─► Local Skills (Resident): .agents/skills/ (285 skills)
  │
  └─► Dynamic AAS Core MCP Server (Read-Only Stdio)
        ├─ search_skills(query, tags) ──► Search 2,113+ catalog entries
        ├─ get_skill(id) ──────────────► Read complete SKILL.md & assets
        └─ compose_stack(ids) ─────────► Validate & export aas-stack.json
```

---

## 2. MCP Tools Exposed

| Tool Name | Access Mode | Description | Parameters |
| :--- | :--- | :--- | :--- |
| `search_skills` | Read-Only | Search the 2,113+ catalog for skills matching text, domain tags, or outcomes. | `query` (string), `tags` (array), `limit` (number) |
| `get_skill` | Read-Only | Retrieve the complete markdown definition, frontmatter, and execution rules for a skill ID. | `skill_id` (string) |
| `list_skill_files` | Read-Only | List scripts, templates, and reference assets associated with a given skill ID. | `skill_id` (string) |
| `read_skill_file` | Read-Only | Read a specific script or template file within a skill bundle. | `skill_id` (string), `file_path` (string) |
| `compose_stack` | In-Memory | Validate a proposed list of skill IDs and generate an immutable `aas-stack.json` manifest. | `skill_ids` (array of strings) |

---

## 3. Configuration in `~/.mcp.json`

```json
{
  "mcpServers": {
    "agentic-awesome-skills": {
      "command": "npx",
      "args": [
        "-y",
        "--package=agentic-awesome-skills@16.9.1",
        "aas",
        "mcp",
        "serve"
      ],
      "description": "AAS Core — Read-only dynamic skill catalog search, inspect, and stack composition for 2,113+ agent skills"
    }
  }
}
```

---

## 4. Operational Guidelines

1. **Query on Demand:** When an agent encounters an unfamiliar library, esoteric protocol, or niche platform not covered in `.agents/skills/`, it should invoke `search_skills` via AAS Core MCP rather than guessing.
2. **No Persistent Bloat:** Agents read instructions in memory for the duration of the task. They do not write thousands of markdown files to disk unless explicitly approved.
3. **Artifact Plan Generation:** When building complex new venture stacks, agents can call `compose_stack` to output an immutable `aas-stack.json` file inside the venture repo.
