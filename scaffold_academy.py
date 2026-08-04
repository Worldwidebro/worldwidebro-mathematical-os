#!/usr/bin/env python3
import os
from pathlib import Path

# Target directory
DOCS_DIR = Path("/Users/acebless/Documents/docs/agentic-systems")

# 12 Layers and their files
LAYERS = {
    "00-START-HERE": [
        "README.md",
        "AGENTIC-SYSTEMS-MAP.md",
        "LEARNING-PATH.md",
        "AGENTIC-VOCABULARY.md",
        "AGENTIC-ERA.md"
    ],
    "01-FUNDAMENTALS": [
        "WHAT-IS-AN-AGENT.md",
        "AGENT-VS-WORKFLOW.md",
        "AGENT-VS-AUTOMATION.md",
        "AGENT-VS-CHATBOT.md",
        "AGENT-VS-LLM-APPLICATION.md",
        "AUTONOMY-SPECTRUM.md",
        "AGENT-LOOP.md",
        "REACT-PATTERN.md",
        "PLAN-EXECUTE-PATTERN.md",
        "REFLECTION-PATTERN.md",
        "EVALUATOR-OPTIMIZER-PATTERN.md",
        "HUMAN-IN-THE-LOOP.md",
        "HUMAN-ON-THE-LOOP.md",
        "HUMAN-OUT-OF-THE-LOOP.md"
    ],
    "02-AGENT-ANATOMY": [
        "AGENT-ANATOMY.md",
        "AGENT-IDENTITY.md",
        "AGENT-INSTRUCTIONS.md",
        "AGENT-CONTEXT.md",
        "AGENT-STATE.md",
        "AGENT-MEMORY.md",
        "AGENT-GOALS.md",
        "AGENT-POLICIES.md",
        "AGENT-CAPABILITIES.md",
        "AGENT-TOOLS.md",
        "AGENT-LIFECYCLE.md"
    ],
    "03-WORKFLOW-PATTERNS": [
        "WORKFLOW-DESIGN.md",
        "SEQUENTIAL-WORKFLOW.md",
        "PARALLEL-WORKFLOW.md",
        "CONDITIONAL-WORKFLOW.md",
        "LOOP-WORKFLOW.md",
        "RETRY-WORKFLOW.md",
        "FALLBACK-WORKFLOW.md",
        "HUMAN-APPROVAL-WORKFLOW.md",
        "SUPERVISOR-WORKFLOW.md",
        "ROUTER-WORKFLOW.md",
        "PLANNER-WORKER-WORKFLOW.md",
        "HIERARCHICAL-WORKFLOW.md",
        "DYNAMIC-DELEGATION.md",
        "EVENT-DRIVEN-AGENTS.md",
        "LONG-RUNNING-AGENTS.md",
        "STATEFUL-WORKFLOWS.md",
        "DURABLE-EXECUTION.md"
    ],
    "04-MEMORY-KNOWLEDGE": [
        "MEMORY-ARCHITECTURE.md",
        "SHORT-TERM-MEMORY.md",
        "LONG-TERM-MEMORY.md",
        "EPISODIC-MEMORY.md",
        "SEMANTIC-MEMORY.md",
        "PROCEDURAL-MEMORY.md",
        "WORKING-MEMORY.md",
        "RAG-ARCHITECTURE.md",
        "VECTOR-SEARCH.md",
        "KNOWLEDGE-GRAPH.md",
        "GRAPH-RAG.md",
        "MEMORY-WRITE-POLICY.md",
        "MEMORY-RETRIEVAL-POLICY.md",
        "CONTEXT-ENGINEERING.md",
        "CONTEXT-COMPACTION.md",
        "KNOWLEDGE-LIFECYCLE.md"
    ],
    "05-TOOLS-MCP": [
        "TOOL-USE.md",
        "FUNCTION-CALLING.md",
        "TOOL-DESIGN.md",
        "TOOL-REGISTRY.md",
        "TOOL-PERMISSIONS.md",
        "TOOL-SELECTION.md",
        "MCP-FUNDAMENTALS.md",
        "MCP-ARCHITECTURE.md",
        "MCP-SERVERS.md",
        "MCP-CLIENTS.md",
        "MCP-TOOLS.md",
        "MCP-RESOURCES.md",
        "MCP-PROMPTS.md",
        "MCP-SECURITY.md",
        "MCP-GOVERNANCE.md"
    ],
    "06-MULTI-AGENT": [
        "MULTI-AGENT-FUNDAMENTALS.md",
        "AGENT-ROLES.md",
        "SPECIALIST-AGENTS.md",
        "SUPERVISOR-AGENTS.md",
        "AGENT-HANDOFFS.md",
        "AGENT-DELEGATION.md",
        "AGENT-NEGOTIATION.md",
        "AGENT-COLLABORATION.md",
        "AGENT-CONSENSUS.md",
        "AGENT-CONFLICT-RESOLUTION.md",
        "AGENT-MARKETPLACE.md",
        "AGENT-DISCOVERY.md",
        "A2A-FUNDAMENTALS.md",
        "A2A-ARCHITECTURE.md",
        "A2A-VS-MCP.md"
    ],
    "07-REASONING-DECISION": [
        "REASONING-ARCHITECTURE.md",
        "CHAIN-OF-THOUGHT-VS-ACTION.md",
        "PLANNING.md",
        "TASK-DECOMPOSITION.md",
        "SUBGOALS.md",
        "DECISION-ENGINE.md",
        "OPTION-GENERATION.md",
        "OPTION-EVALUATION.md",
        "RISK-ANALYSIS.md",
        "UNCERTAINTY.md",
        "CAUSAL-REASONING.md",
        "SCENARIO-PLANNING.md",
        "RESOURCE-ALLOCATION.md",
        "META-REASONING.md",
        "SELF-REFLECTION.md",
        "SELF-CORRECTION.md"
    ],
    "08-EXECUTION-AUTOMATION": [
        "AGENT-ACTION.md",
        "BROWSER-AUTOMATION.md",
        "CODE-EXECUTION.md",
        "SHELL-EXECUTION.md",
        "API-ACTIONS.md",
        "DATABASE-ACTIONS.md",
        "WORKFLOW-AUTOMATION.md",
        "EVENT-BUS.md",
        "QUEUES.md",
        "SCHEDULING.md",
        "JOB-ORCHESTRATION.md",
        "SANDBOXES.md",
        "COMPUTER-USE.md",
        "LONG-HORIZON-TASKS.md"
    ],
    "09-EVALUATION-OBSERVABILITY": [
        "AGENT-EVALUATION.md",
        "TASK-EVALUATION.md",
        "TRAJECTORY-EVALUATION.md",
        "TOOL-EVALUATION.md",
        "LLM-AS-JUDGE.md",
        "EVAL-DATASETS.md",
        "REGRESSION-TESTING.md",
        "AGENT-BENCHMARKS.md",
        "TRACING.md",
        "OBSERVABILITY.md",
        "COST-OBSERVABILITY.md",
        "LATENCY-OBSERVABILITY.md",
        "FAILURE-ANALYSIS.md",
        "AGENT-TELEMETRY.md",
        "FEEDBACK-LOOPS.md",
        "AGENT-IMPROVEMENT.md"
    ],
    "10-SECURITY-GOVERNANCE": [
        "AGENT-SECURITY.md",
        "PROMPT-INJECTION.md",
        "TOOL-INJECTION.md",
        "DATA-EXFILTRATION.md",
        "IDENTITY-AND-AUTHENTICATION.md",
        "AUTHORIZATION.md",
        "LEAST-PRIVILEGE.md",
        "AGENT-PERMISSIONS.md",
        "SECRETS-MANAGEMENT.md",
        "SANDBOX-SECURITY.md",
        "HUMAN-APPROVAL-POLICY.md",
        "AGENT-GOVERNANCE.md",
        "AUDIT-LOGGING.md",
        "POLICY-AS-CODE.md",
        "AGENT-INCIDENT-RESPONSE.md"
    ],
    "11-COMPANY-AGENTS": [
        "AGENTIC-COMPANY.md",
        "AGENTIC-OPERATING-MODEL.md",
        "AI-WORKFORCE.md",
        "HUMAN-AI-WORKFORCE.md",
        "DIGITAL-EMPLOYEE.md",
        "AGENT-DEPARTMENT-MODEL.md",
        "AGENT-ORG-CHART.md",
        "AGENT-ROLE-DESIGN.md",
        "AGENT-JOB-DESCRIPTIONS.md",
        "AGENT-CAPABILITY-MATRIX.md",
        "AGENT-SKILLS.md",
        "AGENT-PERFORMANCE-MANAGEMENT.md",
        "AGENT-RESOURCE-ALLOCATION.md",
        "AGENT-BUDGETING.md",
        "AGENT-PROCUREMENT.md",
        "AGENT-SALES.md",
        "AGENT-MARKETING.md",
        "AGENT-FINANCE.md",
        "AGENT-OPERATIONS.md",
        "AGENT-CUSTOMER-SERVICE.md",
        "AGENT-LEGAL.md",
        "AGENT-HR.md",
        "AGENT-IT.md",
        "AGENT-RD.md",
        "AGENT-EXECUTIVE-OFFICE.md"
    ],
    "12-CASE-STUDIES": [
        "INDUSTRY-AGENT-PATTERNS.md",
        "SOFTWARE-ENGINEERING-AGENTS.md",
        "RESEARCH-AGENTS.md",
        "CUSTOMER-SERVICE-AGENTS.md",
        "SALES-AGENTS.md",
        "MARKETING-AGENTS.md",
        "FINANCE-AGENTS.md",
        "HEALTHCARE-AGENTS.md",
        "LEGAL-AGENTS.md",
        "OPERATIONS-AGENTS.md",
        "DATA-ANALYST-AGENTS.md",
        "BROWSER-AGENTS.md",
        "CODING-AGENTS.md",
        "RESEARCH-TO-ACTION.md",
        "AGENTIC-STARTUP-PATTERNS.md",
        "ENTERPRISE-AGENT-PATTERNS.md",
        "AGENTIC-SOFTWARE-COMPANIES.md",
        "CASE-STUDY-LANGGRAPH.md",
        "CASE-STUDY-OPENAI-AGENTS.md",
        "CASE-STUDY-GOOGLE-ADK.md",
        "CASE-STUDY-MICROSOFT-AGENT-FRAMEWORK.md",
        "CASE-STUDY-PYDANTIC-AI.md",
        "CASE-STUDY-OPENHANDS.md"
    ]
}

AI_BOSS_FILES = [
    "AI-BOSS-AGENTIC-ARCHITECTURE.md",
    "AI-BOSS-AGENT-REGISTRY.md",
    "AI-BOSS-CAPABILITY-GRAPH.md",
    "AI-BOSS-AGENT-ORG-CHART.md",
    "AI-BOSS-AGENT-ROLE-SYSTEM.md",
    "AI-BOSS-AGENT-SKILL-SYSTEM.md",
    "AI-BOSS-AGENT-PERMISSIONS.md",
    "AI-BOSS-AGENT-MEMORY.md",
    "AI-BOSS-AGENT-PROTOCOLS.md",
    "AI-BOSS-MCP-REGISTRY.md",
    "AI-BOSS-A2A-REGISTRY.md",
    "AI-BOSS-TOOL-REGISTRY.md",
    "AI-BOSS-WORKFLOW-REGISTRY.md",
    "AI-BOSS-TASK-REGISTRY.md",
    "AI-BOSS-DECISION-ENGINE.md",
    "AI-BOSS-RESOURCE-ALLOCATION.md",
    "AI-BOSS-MISSING-CAPABILITY-DETECTOR.md",
    "AI-BOSS-SYNERGY-ENGINE.md",
    "AI-BOSS-VENTURE-AGENT-MODEL.md",
    "AI-BOSS-DEPARTMENT-AGENT-MODEL.md",
    "AI-BOSS-COMPANY-AGENT-MODEL.md",
    "AI-BOSS-AGENT-EVALUATION.md",
    "AI-BOSS-AGENT-OBSERVABILITY.md",
    "AI-BOSS-AGENT-SECURITY.md",
    "AI-BOSS-AGENT-GOVERNANCE.md",
    "AI-BOSS-AGENT-LEARNING-LOOP.md",
    "AI-BOSS-SELF-IMPROVEMENT.md",
    "AI-BOSS-VENTURE-FACTORY.md",
    "AI-BOSS-AGENTIC-COMPANY.md"
]

CORE_CONTENT = {
    "01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md": """
## Purpose
Define the fundamental building block of autonomous software: the Agent. Establish how it differs from traditional programs by using independent action loops rather than static input-output paths.

## Core Concept
An **Agent** is an autonomous entity that processes environmental observations through an LLM reasoning engine, decides on actions, and uses tools to execute those actions to achieve a long-horizon goal.

```mermaid
graph LR
    O[Observation] --> T[Reasoning Engine / LLM]
    T --> A[Action Decision]
    A --> E[Execution / Tool Use]
    E --> O
```

## Technical Details
Unlike structured code that follows:
`Input -> If/Else -> Output`
An agent operates on:
`Goal -> Sense -> Plan -> Act -> Reflect -> Loop`
Key properties of a true agent:
1. **Autonomy**: It controls its own execution path.
2. **Statefulness**: It remembers past attempts and context.
3. **Goal-Driven**: It evaluates outcomes against a target criteria.

## Examples/Reference
```python
# A simple agent loop conceptualization
class SimpleAgent:
    def __init__(self, model, tools, goal):
        self.model = model
        self.tools = tools
        self.goal = goal
        self.memory = []

    def run(self, initial_observation):
        obs = initial_observation
        while not self.is_goal_met(obs):
            self.memory.append(obs)
            plan = self.model.generate_plan(self.goal, self.memory)
            action = self.model.choose_action(plan, self.tools)
            obs = self.tools[action.name].execute(action.args)
        return "Goal Met"
```

## Relations
- Part of [[01-FUNDAMENTALS/AGENT-LOOP.md]]
- Distinct from [[01-FUNDAMENTALS/AGENT-VS-WORKFLOW.md]]
""",

    "01-FUNDAMENTALS/AGENT-VS-WORKFLOW.md": """
## Purpose
Differentiate between flexible agentic loops and structured agentic workflows. Help developers choose the correct architecture based on predictability requirements.

## Core Concept
- **Agent**: High autonomy, low predictability. The AI decides *how* to solve a task.
- **Workflow**: Low autonomy, high predictability. The developer dictates the exact steps; the AI simply handles node processing or routing.

```
Structured Workflow:  A --> B --> [AI Classifier] --> C or D
Agentic Loop:         Goal --> [Think -> Act -> Observe] --(Loop until complete)--> Done
```

## Technical Details
Use a **Workflow** when:
1. The business logic requires a deterministic compliance path.
2. The blast radius of a wrong decision is extremely high (e.g., executing transactions).
3. The steps of execution are well-known and static.

Use an **Agent** when:
1. The path to the solution is highly dynamic and multi-layered.
2. You need long-horizon problem solving (e.g., finding and fixing a bug in an arbitrary codebase).
3. The environment requires tool utilization, exploration, and self-correction.

## Examples/Reference
*LangGraph* allows mixing both: defining a structured state graph (Workflow) while letting individual nodes operate with tool-calling loops (Agents).

## Relations
- Composes [[01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md]]
- Leads to [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
""",

    "01-FUNDAMENTALS/AGENT-LOOP.md": """
## Purpose
Outline the fundamental control loop governing agentic action: OBSERVE -> THINK -> PLAN -> ACT -> OBSERVE.

## Core Concept
The **Agent Loop** is the repeating processor where external context is parsed, analyzed against goals, converted into executable steps, ran, and re-evaluated.

```
   ┌─── OBSERVE ◄───┐
   │        │       │
   │        ▼       │
   │     THINK      │
   │        │       │
   │        ▼       │
   │      PLAN      │
   │        │       │
   │        ▼       │
   └───── ACT ──────┘
```

## Technical Details
1. **Observe**: Retrieve input, system logs, environment state, and human feedback.
2. **Think**: Formulate a cognitive summary of current progress vs goal criteria.
3. **Plan**: Generate the immediate next step or sequence of tool calls.
4. **Act**: Execute the selected tools (e.g., run code, search web, call API).
5. **Repeat**: Loop back to observe changes in environment state.

## Examples/Reference
Our `agent_control_loop.py` script implements this exact sequence, logging inputs, outputs, and confidence intervals at each step to build audit trails.

## Relations
- Details [[01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md]]
- Implemented in [[01-FUNDAMENTALS/REACT-PATTERN.md]]
""",

    "02-AGENT-ANATOMY/AGENT-ANATOMY.md": """
## Purpose
Map the cognitive and physical components of an agent to technical abstractions (Model, Memory, Tools, Policies).

## Core Concept
An agent consists of a **Brain** (Model & Reasoning), a **Memory** (Context & Databases), and a **Body** (Tools & Actions), constrained by **Governance** (Policies).

```
                 AGENT
       ┌───────────┼───────────┐
       ▼           ▼           ▼
     MODEL      MEMORY       TOOLS
     (Brain)   (Context)    (Action)
       │           │           │
       ▼           ▼           ▼
   REASONING    HISTORY     MCP/APIs
       └───────────┬───────────┘
                   ▼
                POLICY (Governance)
```

## Technical Details
- **Model**: The core LLM responsible for reasoning, intent extraction, and choice generation.
- **Memory**: The short-term context window + long-term episodic/semantic stores.
- **Tools**: Executable functions (local shell, browser claw, database connections).
- **Policies**: System boundaries, guardrails, budget allocation limits, and permissions.

## Relations
- Governs [[02-AGENT-ANATOMY/AGENT-STATE.md]]
- Restricts [[02-AGENT-ANATOMY/AGENT-TOOLS.md]]
""",

    "02-AGENT-ANATOMY/AGENT-STATE.md": """
## Purpose
Explain state management in agentic systems, detailing how agents store and update execution facts across multi-turn runs.

## Core Concept
**State** is the persistent data schema that tracks inputs, outputs, execution paths, and intermediate context across the lifecycle of an agent task.

## Technical Details
In stateful systems like LangGraph, state is maintained as a thread or database record:
- **State Schema**: Define keys for variables (e.g., list of messages, current plan, active files, errors).
- **Reducers**: Define rules for how state properties append or overwrite (e.g., message list appends, budget decrements).
- **Persistence**: Save state snapshots at every step to allow error recovery, debugging, and human approval interventions.

## Examples/Reference
```typescript
interface AgentState {
  messages: Message[];
  currentTask: string;
  filesModified: string[];
  executionBudget: number;
}
```

## Relations
- Context input: [[02-AGENT-ANATOMY/AGENT-CONTEXT.md]]
- Backed by [[02-AGENT-ANATOMY/AGENT-MEMORY.md]]
""",

    "02-AGENT-ANATOMY/AGENT-CONTEXT.md": """
## Purpose
Define how short-term context is engineered, updated, and managed to prevent context window overflow while maximizing task relevance.

## Core Concept
**Context** is the set of inputs, instructions, files, and system parameters actively fed into the LLM context window during a single loop step.

## Technical Details
Context management requires:
1. **Dynamic Assembly**: Injecting system instructions, target workspace, open file buffers, and recent shell outputs.
2. **Context Compaction**: Summarizing long command logs, trimming repetitive stack traces, and retrieving only the relevant document chunks.
3. **Ontology Mapping**: Structuring context using standard metadata tags to allow the agent to traverse related systems.

## Relations
- Restricts [[02-AGENT-ANATOMY/AGENT-STATE.md]]
- Feed loop: [[01-FUNDAMENTALS/AGENT-LOOP.md]]
""",

    "02-AGENT-ANATOMY/AGENT-MEMORY.md": """
## Purpose
Establish the technical division of memory (short-term, long-term, episodic, semantic) in autonomous agent architectures.

## Core Concept
An agent requires different memory layers to maintain task-specific context (short-term) and remember historical outcomes to improve performance over time (long-term).

```
Short-Term Memory (Context Window, Redux State)
Long-Term Memory:
 ├── Episodic Memory (Database logs of past tasks, trial outcomes)
 └── Semantic Memory (Knowledge Graph, Vector embeddings, Ontologies)
```

## Technical Details
- **Short-Term**: Kept in-memory or in Postgres threads. Truncated or summarized when limits are reached.
- **Episodic**: Logged database trials where the outcome (success/fail) is indexed, letting the agent search past runs before tackling a similar goal.
- **Semantic**: Managed via vector databases (e.g., Qdrant) and graph databases (Neo4j) to map permanent business domains.

## Relations
- Detail: [[04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE.md]]
- Utilized in [[07-REASONING-DECISION/SELF-REFLECTION.md]]
""",

    "02-AGENT-ANATOMY/AGENT-TOOLS.md": """
## Purpose
Define tool integration boundaries, detailing how agents locate, bind, and execute functions.

## Core Concept
**Tools** are structured interfaces that expose system capabilities (e.g., database queries, web lookups, command lines) to the agent via function declarations.

## Technical Details
- **Declaration**: Schema defining name, description, and parameter types (JSON Schema).
- **Binding**: Handled by the framework (e.g., PydanticAI or OpenAI Agents SDK) which links schemas to executable code.
- **Security**: Sandboxed execution, argument validation, and rate limiting.

## Relations
- Details: [[05-TOOLS-MCP/TOOL-USE.md]]
- Under [[02-AGENT-ANATOMY/AGENT-ANATOMY.md]]
""",

    "05-TOOLS-MCP/TOOL-DESIGN.md": """
## Purpose
Provide best practices for design, schemas, and error boundaries of agent-facing tools.

## Core Concept
A tool should be designed with tight, descriptive scopes. An agent is only as capable as the clarity and error-resilience of its tools.

## Technical Details
1. **Descriptions**: Use clear, concise tool and parameter descriptions. The LLM uses these to decide *when* and *how* to call the tool.
2. **Error Recovery**: Tools should return verbose errors to the agent instead of throwing raw system exceptions (e.g., return "Error: Directory '/src' does not exist" instead of throwing `FileNotFoundError`).
3. **Granularity**: Keep tools focused (e.g., `view_file` and `replace_file_content` instead of a single `edit_code` tool).

## Relations
- Governed by [[02-AGENT-ANATOMY/AGENT-TOOLS.md]]
- Registered in [[05-TOOLS-MCP/TOOL-REGISTRY.md]]
""",

    "03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md": """
## Purpose
Introduce modular workflow design, showing how to compose complex systems using structured graph primitives.

## Core Concept
Complex agent systems are built by combining simple flow patterns (Sequential, Parallel, Conditional, Loops) into unified graphs with shared states.

```
       START ──► [Agent Node A] ──► [Router / Branch]
                                         │
                                ┌────────┴────────┐
                                ▼                 ▼
                         [Agent Node B]     [Agent Node C]
                                └────────┬────────┘
                                         ▼
                                       MERGE ──► END
```

## Technical Details
1. **Nodes**: Independent execution blocks (LLM calls, tool execution, human input).
2. **Edges**: Connections routing output from one node to the input of another.
3. **Shared State**: Read-write access across the graph with merge/reducer resolution.

## Relations
- Bridges [[01-FUNDAMENTALS/AGENT-VS-WORKFLOW.md]]
- Implements patterns: [[03-WORKFLOW-PATTERNS/SEQUENTIAL-WORKFLOW.md]]
""",

    "03-WORKFLOW-PATTERNS/SEQUENTIAL-WORKFLOW.md": """
## Purpose
Detail the sequential workflow pattern where outputs of one step feed directly into the next.

## Core Concept
`Node A -> Node B -> Node C`
A linear pipe where data is refined incrementally, reducing LLM context overhead by scoping each node to a single transformation.

## Technical Details
Ideal for pipeline operations:
1. **Step 1 (Ingest)**: Extract text from PDF.
2. **Step 2 (Analyze)**: Identify compliance violations.
3. **Step 3 (Format)**: Output compliance report.
If Step 2 fails, the system retries Step 2 without needing to repeat the ingestion phase.

## Relations
- Under [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
- Next: [[03-WORKFLOW-PATTERNS/PARALLEL-WORKFLOW.md]]
""",

    "03-WORKFLOW-PATTERNS/PARALLEL-WORKFLOW.md": """
## Purpose
Detail parallel execution models (Fork-Join / Map-Reduce) in workflow design.

## Core Concept
```
                 ┌──► Node A ──┐
        START ───┼──► Node B ──┼───► MERGE / JOIN ───► END
                 └──► Node C ──┘
```
Running independent processes concurrently to optimize system speed and distribute reasoning workloads.

## Technical Details
1. **Forking**: Branching the current execution state to multiple parallel tasks.
2. **Join / Merge**: Aggregating outputs. In stateful systems, this requires write-conflict resolution (e.g., combining lists of issues found by separate audit agents).

## Relations
- Composes [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
""",

    "03-WORKFLOW-PATTERNS/CONDITIONAL-WORKFLOW.md": """
## Purpose
Detail routing and branching in graph workflows using conditional logic.

## Core Concept
```
                          ┌──► Node A (Option 1)
        Node -> [Router] ─┼──► Node B (Option 2)
                          └──► Node C (Option 3)
```
Evaluating state values or LLM decisions to choose the next execution node.

## Technical Details
Conditional routing can be:
- **Deterministic**: Checked using code (e.g., if error rate > 5%, route to human rollback).
- **Cognitive**: Checked using LLM classifier (e.g., route query to either customer-support agent or tech-docs agent based on intent).

## Relations
- Under [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
""",

    "03-WORKFLOW-PATTERNS/LOOP-WORKFLOW.md": """
## Purpose
Detail cyclic workflow logic, allowing loops for validation, self-correction, and retry policies.

## Core Concept
```
                 ┌──► [Execution Node] ◄──┐
        START ───┘           │            │ (Fail Validation)
                             ▼            │
                     [Evaluator / Check] ─┘
                             │
                             ▼ (Pass Validation)
                            END
```

## Technical Details
Used for optimization and validation cycles:
1. **Actor Node**: Generates code/reports.
2. **Evaluator Node**: Runs tests or audits the output.
3. **Condition**: If checks pass, exit. If failed, compile logs, update instructions, and route back to actor.
*Critical Constraint*: Always implement a `max_iterations` counter to prevent infinite run loops and cost overruns.

## Relations
- Composes [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
- Foundation for [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
""",

    "03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md": """
## Purpose
Detail the Planner-Worker pattern for complex task decomposition and execution.

## Core Concept
A centralized **Planner** breaks down a large goal into structured sub-tasks, assigns them to individual **Workers** (specialist agents or sub-graphs), and merges the results.

```
       [Goal] ──► [Planner] ──► [Sub-task Checklist]
                                      │
                         ┌────────────┼────────────┐
                         ▼            ▼            ▼
                     Worker 1      Worker 2     Worker 3
                         │            │            │
                         └────────────┼────────────┘
                                      ▼
                               [Merge / Review]
```

## Technical Details
1. **Planner**: High-reasoning LLM (e.g., GPT-4o / Claude 3.5 Sonnet) focused on task breakdown.
2. **Workers**: Specialized agents with access to targeted tools.
3. **Task Tracking**: Shared checklist state (`task.md` model) where progress is updated.

## Relations
- Uses [[03-WORKFLOW-PATTERNS/LOOP-WORKFLOW.md]]
- Governs [[03-WORKFLOW-PATTERNS/SUPERVISOR-WORKFLOW.md]]
""",

    "03-WORKFLOW-PATTERNS/SUPERVISOR-WORKFLOW.md": """
## Purpose
Detail the Supervisor pattern for managing multi-agent teams.

## Core Concept
A **Supervisor** agent acts as a manager, holding conversation state with the user and dynamically routing sub-steps to specialized child agents, acting as the single source of truth for execution flow.

## Technical Details
- The supervisor is a router node that has child agents mapped as tools.
- It calls child agents via handoffs or sub-graph executions.
- Child agents execute tasks and return outputs to the supervisor, who decides if the task is complete or if further delegation is required.

## Relations
- Alternative to [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
- Implements [[06-MULTI-AGENT/AGENT-HANDOFFS.md]]
""",

    "05-TOOLS-MCP/MCP-FUNDAMENTALS.md": """
## Purpose
Introduce the Model Context Protocol (MCP), explaining why standardizing the client-server-tool link is critical for agent scalability.

## Core Concept
**MCP** (Model Context Protocol) is an open-standard protocol designed to link LLM applications (clients) to data sources and execution engines (servers) securely and consistently.

```
┌───────────────┐           Model Context Protocol           ┌──────────────┐
│  MCP Client   │◄──────────────────────────────────────────►│  MCP Server  │
│  (AI Agent)   │                                            │ (Files/APIs) │
└───────────────┘                                            └──────────────┘
```

## Technical Details
MCP solves the "custom tool integration" bottleneck:
- **Clients**: Frameworks/IDE layers (e.g., Claude Desktop, Antigravity IDE, vex-api) that handle orchestration.
- **Servers**: Lightweight services exposing resources, prompts, and tools.
- **JSON-RPC**: Protocol messaging format running over Stdio or SSE.

## Relations
- Details: [[05-TOOLS-MCP/MCP-ARCHITECTURE.md]]
- Implemented in [[05-TOOLS-MCP/MCP-SERVERS.md]]
""",

    "05-TOOLS-MCP/MCP-ARCHITECTURE.md": """
## Purpose
Provide a deep architectural dive into MCP specifications, detailing connection layers, JSON-RPC schemas, and message routing.

## Core Concept
MCP defines standard capabilities: **Prompts**, **Resources**, and **Tools**.

## Technical Details
- **Prompts**: Server-defined prompt templates the client can inject.
- **Resources**: Server-read-only data sources (logs, files, database records) requested via URIs (e.g., `gitnexus://repo/status`).
- **Tools**: Client-executable functions with arguments and JSON schemas.

## Relations
- Builds on [[05-TOOLS-MCP/MCP-FUNDAMENTALS.md]]
""",

    "06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md": """
## Purpose
Introduce Multi-Agent Systems (MAS), explaining coordination, communication, and state distribution.

## Core Concept
A **Multi-Agent System** consists of multiple specialized agents collaborating to solve complex, distributed problems that exceed the capability of a single agent.

```
       Agent 1 (Sales) ◄────[Handoff / A2A]────► Agent 2 (Legal)
             │                                        │
             ▼                                        ▼
      [Exposes Tools]                          [Exposes Tools]
```

## Technical Details
Key challenges in MAS:
1. **Communication Protocol**: Standardized message schemas (e.g., Agent-to-Agent/A2A).
2. **Cohesion & Alignment**: Defining roles, scopes of ownership, and conflict detection rules.
3. **State Syncing**: Sharing necessary data without cluttering individual context windows.

## Relations
- Uses [[06-MULTI-AGENT/AGENT-HANDOFFS.md]]
- Utilizes [[06-MULTI-AGENT/A2A-FUNDAMENTALS.md]]
""",

    "06-MULTI-AGENT/AGENT-HANDOFFS.md": """
## Purpose
Explain the Handoff pattern, showing how agents transfer state and execution control to another agent.

## Core Concept
A **Handoff** occurs when Agent A completes its scope of work (or detects a task out of its scope) and transfers execution control and state context to Agent B.

## Technical Details
Handoff implementation details:
- **Control Handover**: Agent A calls a special handoff tool containing Agent B's ID and the updated task parameters.
- **Context Preservation**: The conversation history (or state summaries) is packaged and forwarded, ensuring Agent B has all historical context needed.

## Relations
- Composes [[06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md]]
- Contrast with [[06-MULTI-AGENT/AGENT-DELEGATION.md]]
""",

    "06-MULTI-AGENT/AGENT-DELEGATION.md": """
## Purpose
Explain the Delegation pattern, showing how parent agents spawn and monitor child agents without losing control.

## Core Concept
**Delegation** occurs when a parent agent assigns a sub-task to a child agent, suspends execution (or works on parallel tasks), and waits for the child to return the completed result.

## Technical Details
- The child agent's state is scoped strictly to the sub-task.
- The parent agent defines success and failure thresholds.
- Safe delegation requires budget boundaries to ensure sub-steps don't loop endlessly.

## Relations
- Under [[06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md]]
- Implements [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
""",

    "06-MULTI-AGENT/A2A-FUNDAMENTALS.md": """
## Purpose
Introduce Agent-to-Agent (A2A) communication protocols and contrast them with tool connectivity standards.

## Core Concept
**A2A** handles conversational task lifecycle coordination between agents, whereas **MCP** focuses on connecting an agent to local tools/data.

```
Agent <──(A2A Protocol: stateful coordination)──► Agent
Agent <──(MCP Protocol: tool execution)──────────► Tool/Data
```

## Relations
- Part of [[06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md]]
""",

    "04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE.md": """
## Purpose
Provide a comprehensive blueprint of agent memory systems, outlining storage, indexing, and compaction layers.

## Core Concept
A robust memory architecture must balance immediate workspace context (Short-Term) with database stores containing historical tasks (Episodic) and structured domain facts (Semantic).

## Technical Details
1. **Short-Term Context**: Pruned via message truncation or summarized recursively using sliding windows.
2. **Episodic Logger**: Saves execution runs into a database (e.g., Supabase table), recording `query -> task -> tool calls -> success code`.
3. **Semantic Graph & Vectors**: Embeds documents using vector algorithms (Qdrant) and maps relationships using Cypher queries (Neo4j).

## Relations
- Governs [[02-AGENT-ANATOMY/AGENT-MEMORY.md]]
""",

    "09-EVALUATION-OBSERVABILITY/AGENT-EVALUATION.md": """
## Purpose
Outline evaluation methodologies for agent performance, planning quality, and tool selection accuracy.

## Core Concept
Evals ensure system changes don't cause regressions. Agent performance is evaluated using deterministic checks, unit test results, and LLM-as-a-judge scorers.

## Technical Details
Key evaluation criteria:
- **Goal Completion**: Does the final output solve the target prompt?
- **Trajectory Efficiency**: Did the agent use the minimum number of tool steps, or did it enter redundant loops?
- **Tool Correctness**: Did it pass valid JSON schemas and arguments to tools?
- **Cost/Latency**: Did it execute within the allowed budget and time boundaries?

## Relations
- Feeds [[09-EVALUATION-OBSERVABILITY/TRACING.md]]
- Relates to [[09-EVALUATION-OBSERVABILITY/TASK-EVALUATION.md]]
""",

    "10-SECURITY-GOVERNANCE/AGENT-SECURITY.md": """
## Purpose
Establish security guidelines for autonomous agents, focusing on data protection, injection prevention, and boundary sandboxing.

## Core Concept
Agents executing commands require tight security boundaries. A compromised agent can execute destructive commands, exfiltrate credentials, or delete databases.

## Technical Details
1. **Least Privilege**: Grant the narrowest system permissions required for the task.
2. **Execution Sandboxing**: Run execution code inside isolated virtual runtimes (e.g., Docker or sandboxed shell sessions) with no host network access unless whitelisted.
3. **Input Sanitization**: Block prompt injection and tool-argument poisoning by validating arguments against JSON schemas before execution.

## Relations
- Restricts [[08-EXECUTION-AUTOMATION/AGENT-ACTION.md]]
"""
}

AI_BOSS_CONTENT = {
    "AI-BOSS-AGENTIC-ARCHITECTURE.md": """
## Purpose
Document the core agentic architecture of the **AI Boss Operating System** (OS-001) used by Worldwidebro Holdings.

## Core Concept
The AI Boss OS is a meta-orchestrator that dynamically queries formulas from a registry of 1,600+ repositories, constructs multi-agent workflows, runs them, and updates its strategy logs based on the outcomes.

```
       User Request ──► [AI Boss Decision Engine]
                                │
                      (Query Repository Graph)
                                ▼
                       [Neo4j Registry]
                                │
                    (Select Formula & Config)
                                ▼
                   [spawn-agents.py Execution] ──► [Supabase Outcome Logger]
```

## Technical Details
- **Formula-Driven**: Zero custom reimplementation of starred formulas. Every capability is mapped to a specific repository in the Neo4j graph.
- **Auditable Decisions**: Every workflow records: Requesting Entity -> Selected Repository -> Formula Schema -> Execution Sandbox Log -> Financial/Performance Outcome.
- **Weekly Learning Loop**: A scheduled job runs to match predictions against actual results, updating capability scores in the graph.

## Relations
- Details [[OS-ARCHITECTURE.md]]
- Relates to [[AGENTS.md]]
""",

    "AI-BOSS-AGENT-REGISTRY.md": """
## Purpose
Define the schema, attributes, and tracking mechanisms of all active agents running on the Worldwidebro OS.

## Core Concept
The **Agent Registry** is the central catalog tracking agent metadata, lifecycle states, token budgets, and operational departments.

## Technical Details
Active agent metadata is stored in `agents_index.csv.stub` and registered in Supabase:
- `agent_id`: Canonical ID (e.g. `T3_CONTENT_STRATEGIST_001`).
- `role`: Domain specialty (e.g. Creator, Auditor, Coordinator).
- `department`: Linked department (e.g., Finance, Sales).
- `capabilities`: Linked capabilities (wiki-links in the ontology).
- `status`: Active, Paused, or Decommissioned.

## Relations
- Feeds [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
- Matches [[AI-BOSS/AI-BOSS-AGENT-ORG-CHART.md]]
""",

    "AI-BOSS-CAPABILITY-GRAPH.md": """
## Purpose
Document the Neo4j Graph schema mapping Repositories, Capabilities, and Ventures.

## Core Concept
The **Capability Graph** resolves the join: `Venture -> Sector -> Capability -> Tool -> Repository`. It ensures that when an agent asks to "calculate X", the OS finds the exact code asset that implements the logic.

```
(:Venture {id: 'CON-001'})-[:REQUIRES]->(:Capability {name: 'Estimating'})-[:IMPLEMENTED_BY]->(:Repository {url: 'github.com/...'})
```

## Technical Details
Graph updates are triggered by `build_kg.py` and `obsidian_graph_build.py` based on markdown files in the vault. Relationships are parsed from wiki-links in the `## Capabilities` and `## Dependencies` headers.

## Relations
- Built by [[build_kg.py]]
- Syncs to [[obsidian_graph_sync.py]]
""",

    "AI-BOSS-AGENT-ORG-CHART.md": """
## Purpose
Map the multi-agent organizational chart of Worldwidebro Holdings OpCos.

## Core Concept
The organization chart defines the delegation tree showing how parent supervisor agents command specialist department agents.

```
                        [AI BOSS OS (CEO)]
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
        [Operations OS (COO)]         [Finance OS (CFO)]
                 │                             │
        ┌────────┴────────┐           ┌────────┴────────┐
        ▼                 ▼           ▼                 ▼
   CON-001 Agent    LT-005 Agent  STA-001 Agent  Billing Agent
```

## Relations
- Links to [[ORG-CHART-OPERATIONAL.md]]
- Linked in [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
""",

    "AI-BOSS-AGENT-ROLE-SYSTEM.md": """
## Purpose
Define the roles, scopes, and instructions governing different tiers of agents.

## Core Concept
Agents are categorized into tiers:
1. **Tier 1 (CEO / AI Boss)**: Long-horizon strategy, venture factory triggering, capital allocation.
2. **Tier 2 (COO / Orchestrator)**: Operations routing, bottleneck detection, department supervision.
3. **Tier 3 (Specialist)**: Focused execution tasks (coding, auditing, content generation, math).

## Relations
- Details [[AI-BOSS/AI-BOSS-AGENT-ORG-CHART.md]]
""",

    "AI-BOSS-AGENT-SKILL-SYSTEM.md": """
## Purpose
Document the skill injection and dynamic plugin binding architecture of the OS.

## Core Concept
Skills are structured directories containing script hooks, prompts, and documentation under `~/.gemini/antigravity/skills/` that extend agent capabilities dynamically based on context.

## Relations
- Uses [[AI-BOSS/AI-BOSS-AGENT-REGISTRY.md]]
""",

    "AI-BOSS-AGENT-PERMISSIONS.md": """
## Purpose
Document the permissions and sandboxing policy of the OS.

## Core Concept
Permissions are structured as rules defining which directories, domains, and command prefixes an agent can access (as defined in `list_permissions`).

## Relations
- Restricts [[AI-BOSS/AI-BOSS-TOOL-REGISTRY.md]]
""",

    "AI-BOSS-AGENT-MEMORY.md": """
## Purpose
Define the storage format of memory logs in the Worldwidebro database.

## Core Concept
Memory is stored in `worldwidebro_os.duckdb` and synchronized to Supabase, indexing episodic runs and saving long-term reflection parameters.

## Relations
- Backs [[AI-BOSS/AI-BOSS-DECISION-ENGINE.md]]
""",

    "AI-BOSS-AGENT-PROTOCOLS.md": """
## Purpose
Define message envelopes and handshake schemas for Agent-to-Agent (A2A) communications.

## Core Concept
A2A communications use structured JSON envelopes sent via message queues, containing message IDs, routing targets, payloads, and state context.

## Relations
- Defines [[AI-BOSS/AI-BOSS-A2A-REGISTRY.md]]
""",

    "AI-BOSS-MCP-REGISTRY.md": """
## Purpose
Catalog all MCP servers currently linked to the Worldwidebro OS.

## Core Concept
The MCP Registry defines the connection parameters for active servers (e.g., BrowserClaw, DevTools, Supabase, GitNexus) in `mcp_config.json`.

## Relations
- Governs [[AI-BOSS/AI-BOSS-TOOL-REGISTRY.md]]
""",

    "AI-BOSS-A2A-REGISTRY.md": """
## Purpose
Catalog the active communication pathways and queues between operational agents.

## Relations
- Details [[AI-BOSS/AI-BOSS-AGENT-PROTOCOLS.md]]
""",

    "AI-BOSS-TOOL-REGISTRY.md": """
## Purpose
Catalog all core tools available to agents, mapping them to specific MCP servers or local scripts.

## Core Concept
The tool registry is managed via `agent_tools_registry.yaml` and lists names, layer groups, purposes, and bindings.

## Relations
- Bound to [[AI-BOSS/AI-BOSS-MCP-REGISTRY.md]]
""",

    "AI-BOSS-WORKFLOW-REGISTRY.md": """
## Purpose
Document the registered n8n, LangGraph, and local Python workflows.

## Relations
- Tracks [[AI-BOSS/AI-BOSS-TASK-REGISTRY.md]]
""",

    "AI-BOSS-TASK-REGISTRY.md": """
## Purpose
Document the task tracking database.

## Relations
- Feeds [[AI-BOSS/AI-BOSS-DECISION-ENGINE.md]]
""",

    "AI-BOSS-DECISION-ENGINE.md": """
## Purpose
Document the reasoning and execution processor of the AI Boss OS.

## Core Concept
The Decision Engine handles query processing, formula scoring, and risk checking. It reads the Capability Graph, checks permissions, executes sandboxed scripts, and logs the outcomes.

## Relations
- Heart of [[AI-BOSS/AI-BOSS-AGENTIC-ARCHITECTURE.md]]
""",

    "AI-BOSS-RESOURCE-ALLOCATION.md": """
## Purpose
Document the capital and computational resource allocation policies of the holdings network.

## Relations
- Governed by [[AI-BOSS/AI-BOSS-DECISION-ENGINE.md]]
""",

    "AI-BOSS-MISSING-CAPABILITY-DETECTOR.md": """
## Purpose
Explain the system that audits ventures to find missing skills or tools.

## Core Concept
The detector cross-checks the sector capability registry against repository metadata. If a venture is active in a sector but lacks repositories mapping to required capabilities, it flags a "missing capability task".

## Relations
- Triggers [[AI-BOSS/AI-BOSS-VENTURE-FACTORY.md]]
""",

    "AI-BOSS-SYNERGY-ENGINE.md": """
## Purpose
Explain how the Neo4j graph finds synergies (shared code, resources, or customers) between ventures.

## Relations
- Reads [[AI-BOSS/AI-BOSS-CAPABILITY-GRAPH.md]]
""",

    "AI-BOSS-VENTURE-AGENT-MODEL.md": """
## Purpose
Document the specialized agent profile assigned to manage a single venture.

## Relations
- Under [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
""",

    "AI-BOSS-DEPARTMENT-AGENT-MODEL.md": """
## Purpose
Document agents assigned to manage specific departments (e.g. Sales, HR).

## Relations
- Under [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
""",

    "AI-BOSS-COMPANY-AGENT-MODEL.md": """
## Purpose
Document the orchestrator profile that acts as the OpCo CEO.

## Relations
- Under [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
""",

    "AI-BOSS-AGENT-EVALUATION.md": """
## Purpose
Document the evaluation tests run on agents within the OS.

## Core Concept
Uses `agent_scores.jsonl` to track success rates, trajectory lengths, and accuracy.

## Relations
- Evaluates [[AI-BOSS/AI-BOSS-AGENT-REGISTRY.md]]
""",

    "AI-BOSS-AGENT-OBSERVABILITY.md": """
## Purpose
Document the telemetry, open telemetry (otel) collector, and tracing configuration.

## Relations
- Feeds [[AI-BOSS/AI-BOSS-AGENT-EVALUATION.md]]
""",

    "AI-BOSS-AGENT-SECURITY.md": """
## Purpose
Define the threat models and defense policies of the AI Boss OS.

## Relations
- Restricts [[AI-BOSS/AI-BOSS-AGENT-PERMISSIONS.md]]
""",

    "AI-BOSS-AGENT-GOVERNANCE.md": """
## Purpose
Document the audit logging, compliance tracking, and human-in-the-loop escalation rules.

## Relations
- Restricts [[AI-BOSS/AI-BOSS-DECISION-ENGINE.md]]
""",

    "AI-BOSS-AGENT-LEARNING-LOOP.md": """
## Purpose
Document the weekly feedback mechanism where formula predictions are updated.

## Relations
- Driven by [[AI-BOSS/AI-BOSS-AGENT-EVALUATION.md]]
""",

    "AI-BOSS-SELF-IMPROVEMENT.md": """
## Purpose
Document how agents modify their own prompt instructions and select better tool chains.

## Relations
- Powered by [[AI-BOSS/AI-BOSS-AGENT-LEARNING-LOOP.md]]
""",

    "AI-BOSS-VENTURE-FACTORY.md": """
## Purpose
Document the venture creation and bootstrapping logic.

## Core Concept
Spawns new ventures by generating github repositories, initializing environment configs, and deploying initial Vercel frontends.

## Relations
- Uses [[bootstrap_venture.py]]
""",

    "AI-BOSS-AGENTIC-COMPANY.md": """
## Purpose
Synthesize the operational rules of the multi-agent holdings network.

## Relations
- Governs [[AI-BOSS/AI-BOSS-AGENT-ORG-CHART.md]]
"""
}

TEMPLATE_CONTENT = """---
id: {slug}
type: document
name: {title}
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 0.8
freshness: unverified
tags:
  - status/active
  - knowledge/unverified
---

# {title}

## Purpose
This document provides the conceptual and technical details for **{title}** within the Agentic Systems Academy.

## Core Concept
*Drafting Phase*: The core parameters, definitions, and operational mechanisms for {title} are being compiled.

## Technical Details
- Under Construction: This topic will be elaborated during next curriculum updates.
- Conforms to the `AI-BRAIN/ONTOLOGY.md` specification.

## Relations
- Part of the [[00-START-HERE/README.md]] curriculum.
"""

CORE_ALIASES = {
    "01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md": ["AI Agent", "Autonomous Agent"],
    "01-FUNDAMENTALS/AGENT-LOOP.md": ["Cognitive Loop", "Sense-Plan-Act Loop"],
    "02-AGENT-ANATOMY/AGENT-ANATOMY.md": ["Agent Architecture", "Cognitive Anatomy"],
    "05-TOOLS-MCP/MCP-FUNDAMENTALS.md": ["Model Context Protocol", "MCP Standard"],
    "06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md": ["Multi-Agent Systems", "MAS"],
    "04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE.md": ["Episodic Memory", "Semantic Graph"],
    "09-EVALUATION-OBSERVABILITY/AGENT-EVALUATION.md": ["Agent Evals", "Trajectory Scoring"],
    "10-SECURITY-GOVERNANCE/AGENT-SECURITY.md": ["Agent Guardrails", "Least Privilege Sandbox"]
}

def main():
    print("Scaffolding Agentic Systems Academy & Operating Manual...")
    
    # 1. Create layers
    for layer, files in LAYERS.items():
        layer_path = DOCS_DIR / layer
        layer_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {layer_path}")
        
        for filename in files:
            file_path = layer_path / filename
            rel_path = f"{layer}/{filename}"
            slug = filename.replace(".md", "").lower()
            title = filename.replace(".md", "").replace("-", " ")
            
            # Check if we have custom core content
            if rel_path in CORE_CONTENT:
                aliases_str = ""
                if rel_path in CORE_ALIASES:
                    aliases_str = "aliases:\n" + "\n".join(f"  - \"{a}\"" for a in CORE_ALIASES[rel_path]) + "\n"
                
                # Add proper YAML frontmatter + content
                header = f"""---
id: {slug}
type: document
name: {title}
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 1.0
freshness: current
{aliases_str}tags:
  - status/active
  - knowledge/current
---

# {title}
"""
                content = header + CORE_CONTENT[rel_path].strip() + "\n"
                file_path.write_text(content, encoding="utf-8")
                print(f"  Written CORE file: {rel_path}")
            else:
                # Write placeholder template
                content = TEMPLATE_CONTENT.format(slug=slug, title=title)
                file_path.write_text(content, encoding="utf-8")
                print(f"  Written placeholder: {rel_path}")
                
    # 2. Create AI Boss proprietary folder
    boss_dir = DOCS_DIR / "ai-boss"
    boss_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {boss_dir}")
    
    for filename in AI_BOSS_FILES:
        file_path = boss_dir / filename
        slug = filename.replace(".md", "").lower()
        title = filename.replace(".md", "").replace("-", " ")
        
        if filename in AI_BOSS_CONTENT:
            header = f"""---
id: {slug}
type: document
name: {title}
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: proprietary
confidence: 1.0
freshness: current
tags:
  - status/active
  - knowledge/current
---

# {title}
"""
            content = header + AI_BOSS_CONTENT[filename].strip() + "\n"
            file_path.write_text(content, encoding="utf-8")
            print(f"  Written PROPRIETARY file: ai-boss/{filename}")
        else:
            # Write placeholder template
            content = TEMPLATE_CONTENT.format(slug=slug, title=title)
            file_path.write_text(content, encoding="utf-8")
            print(f"  Written PROPRIETARY placeholder: ai-boss/{filename}")
            
    print("\nScaffolding complete. 129 files generated successfully.")

if __name__ == "__main__":
    main()
