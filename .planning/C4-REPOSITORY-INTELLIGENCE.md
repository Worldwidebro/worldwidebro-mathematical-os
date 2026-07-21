# C4: Repository Intelligence Dashboard

Graphify repository dependencies mapping and version monitoring dashboard.

## 1. Dashboards
Integrates Graphify nodes from Supabase to track outdated dependency codebases.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Graphify service running (established in Phase 3); `build_repo_intelligence_score.py` pipeline operational.
    *   **Dependencies:** Blocks venture creator's capability-to-repository lookup and dynamic mapping validation.
*   **Verification Gate:**
    *   **Success Criteria:** REST API call to `/api/graph/data` returns dependency health and integration maps for active tech repositories.
    *   **Blockers:** Deprecated libraries and security vulnerability drifts will go unnoticed, leading to silent build failures on new ventures.
