# Agent Contracts and Capability Schema

This document details the interface schemas, constraints, and contracts governing how agents declare capabilities and tools within the **AI-BOSS-OS** integration registry.

## 1. Capability Declaration Schema

Every agent in the system must map its capabilities in the shared agent catalog (`/AI-CORE/agent-registry/agent_registry.yaml`). This ensures that the **Decision Engine** can resolve tasks to the correct agent node.

Capabilities follow this strict schema format:

```yaml
agent_contracts:
  CTO:
    role: "Chief Technology Officer"
    inputs:
      - repository_path: string
      - dependency_targets: array
    outputs:
      - call_graph: json
      - validation_report: markdown
    supported_protocols:
      - MCP
      - A2A
    required_permissions:
      - read_filesystem
      - execute_gitnexus
```

---

## 2. Escalation Protocol Contracts

When an agent hits a logic limit or a task requires critical authorizations (such as capital allocation, architectural redesigns, or compliance policy changes), it invokes the **Escalation Protocol**:

```text
               [ Agent Task Execution ]
                          |
               (Does task exceed limits?)
                          |
                +---------+---------+
                | Yes               | No
                v                   v
      [ Trigger Escalation ]  [ Complete Task ]
                |
        +-------+-------+
        | Council Target| (e.g. escalation: "council")
        +-------+-------+
                |
                v
      [ Dispatch to Council ]
```

### Escalation Configurations:
- **`escalation: council`**: The task is suspended and dispatched to the designated council defined in the `council_registry.yaml`.
- **`escalation: human`**: The task halts and prompts the developer console for manual approval or override.
- **`escalation: none`**: The task fails immediately, throwing a standard exception to the parent workflow.

---

## 3. Tool Execution Contracts

To ensure sandbox safety and trace operations under Langfuse, all agent tools must adhere to the following execution guarantees:

1. **Idempotency**: Whenever possible, read tools (e.g., repository scanning, vector DB searches) must be side-effect free.
2. **Resource Throttling**: Tool execution must not exceed 60 seconds. Long-running tasks must spawn asynchronous background tasks managed via standard status polling APIs.
3. **Execution Auditability**: Every tool call is saved in PostgreSQL (`iza_os_core.agent_execution_logs`) containing the executing agent ID, tool arguments, completion status, and stderr logs.
