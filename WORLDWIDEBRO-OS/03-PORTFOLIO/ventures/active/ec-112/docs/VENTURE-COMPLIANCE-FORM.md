# Venture Compliance & Agent Governance Form: Cosmic Kitty

## 1. Credentials & Secrets Compliance
- All API tokens and passwords must be stored in the remote Supabase `agent_credentials` table (encrypted).
- No raw keys are permitted in repository code files or local workspace configs.

## 2. Agent Authorization Boundaries
- **Capital Deployments**: Auto-approved up to \$100,000. All higher allocations require manual OPCO/CFO review.
- **Workflow Autonomy**: Enabled for standard routines. Exceptions must be escalated to the Governance Council.

## 3. Auditing & Logging
- Every agent routine execution must log to `runs.jsonl`.
- Feedback outcomes must be logged using [01_loop_feedback_collector.py](file:///Users/acebless/Documents/01_loop_feedback_collector.py).
