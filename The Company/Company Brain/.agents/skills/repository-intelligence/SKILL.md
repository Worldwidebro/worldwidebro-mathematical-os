---
name: repository-intelligence
description: Analyzes, verifies, and catalogs owned and starred repositories across Company Brain using GitHub GraphQL batching, manifest extraction, and code reality verification. Use when inspecting repos, evaluating external open source libraries, or syncing repository metadata.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Repository Intelligence Skill

This skill governs the systematic extraction, auditing, and classification of repositories across the WorldwideBro ecosystem.

## Protocols

1. **Verify Code Reality**:
   - Never rely solely on repository descriptions or GitHub topics.
   - Inspect true manifest files (`package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`).
   - Differentiate code-bearing repos from venture paperwork templates (`FORMATION.md`, `FUNDING.md`, etc.).

2. **GraphQL Batching Over REST/MCP**:
   - When auditing multiple repositories, batch queries via `gh api graphql` using aliased repository fields (e.g. 40 repos per request).
   - Fetch tree entries or blob text in single batched calls to avoid rate limiting and token exhaustion.

3. **External Decision Matrix**:
   - For external/starred repositories, evaluate against the 10 verdicts:
     `BUILD`, `ADOPT`, `INTEGRATE`, `EXTRACT`, `FORK`, `WRAP`, `REFERENCE`, `MONITOR`, `REJECT`, `IGNORE`.
   - Record license, maintenance frequency, security posture, and compatibility with the Company Brain architecture.
