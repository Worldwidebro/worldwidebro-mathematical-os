# Architecture Rules — Company Brain

1. **Layered Isolation**: Always follow `Presentation → Application → Domain → Infrastructure → Data`.
   - Never import infrastructure or presentation libraries directly into pure domain logic.
   - Keep third-party integrations (APIs, SaaS SDKs) isolated behind adapters and interfaces.

2. **Canonical Authorities**:
   - **Neo4j** (`:7687`) is the relationship authority.
   - **Qdrant** (`:6333`) is the semantic search / vector retrieval layer.
   - **_REGISTRIES/CANONICAL/** is the filesystem authority for entity IDs, capabilities, and repositories.
   - Never invent parallel stores or conflicting IDs.

3. **No Duplicate Infrastructure**:
   - Strictly respect `00-CONSTITUTION` #4: Do not run redundant, overlapping database instances or containers.
   - Mac Studio (`100.87.214.70`) is the canonical database host; local machines are development/mobile nodes.

4. **Reuse Over Reinvention**:
   - Always query existing capabilities in `CAPABILITY_REGISTRY.yaml` and code in the 177 code-backed repositories before creating new services or models.
