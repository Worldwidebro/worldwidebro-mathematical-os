[[STARTHERE]] | [[AGENTS.md]] | [[ANTIGRAVITY.md]]

# Workflow: Repository Audit (`/repository-audit`)

**Objective:** Audit owned or external repositories to extract manifests, verify code reality, and update canonical registries.

## Steps

1. **Identify Target Repositories**:
   - Filter `_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml` for targeted IDs or URLs.
2. **Execute Batched Manifest Extraction**:
   - Run GitHub GraphQL queries for `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`.
3. **Parse Dependencies & Stack**:
   - Extract frameworks, languages, entrypoints, and library names.
4. **Update Code Reality & Registries**:
   - Update `OWNED_REPO_CODE_REALITY.json` and sync `REPOSITORY_REGISTRY.yaml`.
5. **Verify Output**:
   - Generate audit summary report documenting verified code vs paperwork templates.
