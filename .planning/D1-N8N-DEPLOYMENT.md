# D1: n8n Workflow Automation Setup

Self-hosted n8n deployment configurations and webhooks wiring.

## 1. Docker compose
Ensure n8n runs on port `5678`.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** n8n container running on port 5678 (established in Phase 1); Redis Event Bus (B4) and Venture Classifier Agent (B2) operational.
    *   **Dependencies:** Blocks lead intake pipelines and auto-billing workflows.
*   **Verification Gate:**
    *   **Success Criteria:** Posting a mockup webhook payload to the n8n endpoint triggers the workflow execution, classifies the lead, and saves details to Supabase.
    *   **Blockers:** Inbound leads processing remains entirely manual, limiting scale capacity.
