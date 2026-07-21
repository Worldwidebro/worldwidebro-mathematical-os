# B3b: IZA OS Dependency Mapping Guide

Details how to link individual business ventures to your shared technical infrastructure.

## 1. Mappings
*   **PostgreSQL**: Maps to `core.ventures` and operational logs database.
*   **Neo4j**: Maps to the organizational knowledge graph.
*   **Qdrant**: Maps to the vector embedding memory registries.

## 2. Dynamic Configuration
When a venture is created, automatically write to `venture_dependencies` table to track pinned dependency versions.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** B3A (Venture Factory) active; Neo4j and Qdrant instances running.
    *   **Dependencies:** Blocks C4 (Repository Intelligence) and capability mapping.
*   **Verification Gate:**
    *   **Success Criteria:** Venture creation successfully writes versions to `venture_dependencies` table and registers/links nodes in Neo4j.
    *   **Blockers:** Ventures lack version-locked dependency configurations and cannot trace capability maps.
