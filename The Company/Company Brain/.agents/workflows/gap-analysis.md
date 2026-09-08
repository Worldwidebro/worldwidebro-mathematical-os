# Workflow: Capability Gap Analysis (`/gap-analysis`)

**Objective:** Compare venture requirements and business capabilities against verified internal repository implementations and identify gaps to be filled by external/starred repositories.

## Steps

1. **Query Business Capabilities**:
   - Read `_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml` for `CAP-001` through `CAP-012`.
2. **Match Implemented Repositories**:
   - Inspect verified code repositories implementing each capability.
3. **Identify Deficits & Thin Capabilities**:
   - Flag any capability with fewer than 2 verified implementations.
4. **Scan External/Starred Repositories**:
   - Search starred repositories for capability candidates matching the deficit.
5. **Generate Decision Recommendations**:
   - Produce `CAPABILITY_GAP_REPORT.yaml` with explicit recommendations (`ADOPT`, `INTEGRATE`, `BUILD`, `WRAP`).
