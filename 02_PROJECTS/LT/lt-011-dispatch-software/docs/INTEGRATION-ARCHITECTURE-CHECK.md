# OSS Integration Architecture Compatibility Check

This document audits the compatibility of the `oss_integration_pipeline` workflow against the rest of the Worldwidebro OS files, folders, sectors, and operational systems.

---

## 1. Directory & File Alignment

The pipeline maps directly to the standard repository layout:

| Pipeline Artifact | Target Directory | System Role |
| :--- | :--- | :--- |
| **Agent Prompt Harnesses** | `agents/` | System prompts, schemas, and eval guides in Markdown. |
| **Tool Adapter Code** | `mcp/` or `services/api/src/adapters/` | Executable code (e.g., calling Traccar or VROOM APIs). |
| **Tool Definitions** | `docs/mcp/` or `docs/tools/` | Informational Markdown definitions for the LLM. |
| **Event Traces** | Supabase `audit_logs` & `events` tables | Records LLM execution traces, token costs, and outcomes. |

---

## 2. OpCo & Sector Compatibility

In our database world model (`build_kg.py`), ventures are grouped by sectors under parent operating systems (OpCos):

```text
                  WORLDWIDEBRO HOLDINGS (worldwidebro)
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
      LOG-OS                     CON-OS                    STA-OS
   (Logistics)               (Construction)              (Staffing)
         │                         │                         │
  LT-011 (DispatchOS)       CON-001 (Bidding)        STA-001 (Staffing Agency)
```

The `oss_integration_pipeline` acts as a cross-cutting optimizer:
1.  **LOG-OS (Logistics Sector):** Automatically maps gaps (e.g., "geocoding") to OpenStreetMap Nominatim, deploying it as `mcp/maps`.
2.  **CON-OS (Construction Sector):** Automatically maps gaps (e.g., "project scheduling") to open-source Gantt chart engines, creating PRs to the `CON-001` repository.
3.  **STA-OS (Staffing Sector):** Maps roster scheduling constraints to open-source constraint solvers (like OptaPlanner) to match workers.

---

## 3. The Event-Driven Loop Verification

Each integrated tool outputs structured JSON, fitting our audit ledger specifications:

```
  [ Event: capability_gap_identified ]
                 │
                 ▼
  [ Execute: oss_integration_pipeline ] ──► writes code ──► creates GitHub PR
                                                                │
                                                                ▼
  [ Event: pr_created ] ◄───────────────────────────────────────┘
                 │
                 ▼
  [ CI/CD Pipeline (Automerge if eval > 0.95) ]
                 │
                 ▼
  [ Deploy tool to Vercel/Docker ] ──► update Neo4j Graph
```

No hardcoded routes are disrupted. The API gateway automatically loads new tools from the registry folder, making the system dynamic, scalable, and completely compatible.
