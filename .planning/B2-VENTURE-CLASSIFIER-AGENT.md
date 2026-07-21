# B2: Venture Classifier Agent Setup

The `venture_classifier` automatically parses incoming venture leads and classifies them by sector type.

## 1. Setup & Configuration
Save config under `05-AGENTS/venture_classifier_agent.py`:

```python
from crewai import Agent

classifier_agent = Agent(
    role="Venture Sector Router",
    goal="Identify OPCO sectors (CON, STA, RE, EDU) for incoming leads",
    backstory="Expert business classifier sorting venture portfolios.",
    verbose=True
)
```

## 2. Wiring
Links to Slack webhook channel for real-time notifications when a new venture is created.

## Execution Gate & Verification

*   **Execution Sequence Lock:**
    *   **Prerequisites:** Phase A3 (Audit Log Instrumentation) and Phase B1 (AgentToolWiring Class) completed; Supabase database tables initialized.
    *   **Dependencies:** Blocks Venture OS template creation and auto-provisioning verification (B3A) and n8n workflows (D1).
*   **Verification Gate:**
    *   **Success Criteria:** Running `python3 05-AGENTS/venture_classifier_agent.py` correctly parses a mockup lead JSON, runs PolicyEngine checks, logs to audit tables, posts to Slack, and creates a ClickUp task.
    *   **Blockers:** Inbound venture leads will queue up without classification, halting downstream automated venture spawner pipelines.
