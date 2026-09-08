---
id: REG-LOCAL-MODEL-STACK
title: "Local Model & Agent Execution Stack Registry"
aliases: ["Local Model Agent Stack", "LOCAL_MODEL_AGENT_STACK_REGISTRY"]
tags: [registry, models, agents, execution-stack, macstudio, omniroute, litellm]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[17-MODELS/17-MODELS|17-MODELS]] | [[16-AGENTS/README|16-AGENTS]] | [[_INFRASTRUCTURE/omniroute/README|OmniRoute]] | [[CLAUDE]]

# Local Model & Agent Infrastructure Architecture Registry (LMA-REGISTRY)

> **Canonical Document ID:** `REG-LMA-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Status:** CANONICAL & RATIFIED  
> **Updated:** 2026-09-06  
> **North Star Metric:** *How much useful work can Company Brain complete per dollar, per second, and per token?*

[[STARTHERE]] | [[REALITY]] | [[INDEX]] | [[SECTOR_INDEX]] | [[ARCHITECTURE]] | [[CLAUDE]]

---

## 1. Executive Policy: The "No Duplicate Stacks" Rule

1. **Architecture Before Repositories:** Never clone or install repos to "see what they do." Architecture defines requirements; measurement exposes gaps; verified tools fill them.
2. **Single Responsibility per Layer:** We do not run 8 gateways, 6 inference engines, or 4 vector databases simultaneously. Every layer has **one primary adopted technology** and at most **one evaluated alternative**.
3. **Decoupled Business Applications:** Business applications (such as `ops-staff-001-staffing` and `lt-005-medical-courier-dispatch`) sit **on top** of this infrastructure via stable APIs/MCP. They must never be entangled with experimental infrastructure churn.
4. **Decision Taxonomy:** Every project evaluated in Company Brain must carry one of six explicit statuses:
   - **`ADOPT`**: Active production infrastructure. Deployed, monitored, and maintained.
   - **`EVALUATE`**: Active staging benchmark against an explicit hypothesis and token/latency metric.
   - **`REFERENCE`**: Architectural design pattern, algorithmic study, or code harvest source. Not deployed.
   - **`DEFER`**: Valid technology, but redundant or premature for current scale.
   - **`REJECT`**: Incompatible with our architecture (e.g., CUDA-only, cloud-monopolistic, heavy bloat).
   - **`REMOVE`**: Deprecated or superseded legacy components scheduled for decommissioning.

---

## 2. The Unified Local AI + Agent Operating Stack

```text
                           COMPANY BRAIN
                                 │
                   ┌─────────────▼─────────────┐
                   │  UNIFIED ROUTER & GATEWAY  │
                   │    OmniRoute (:20128)      │
                   │     LiteLLM (:4000)        │
                   └─────────────┬─────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             ▼                   ▼                   ▼
      LOCAL INFERENCE      REMOTE CLOUD        SPECIALIZED
     (Apple Silicon / T7) (Claude / Gemini / GPT) (NIM / Embeddings)
             │
       ┌─────┴──────────────────┐
       ▼                        ▼
  MLX / MLX-LM              OLLAMA (GGUF)
  (Mac Studio M4 Max)      (T7 Shield Storage)
       │                        │
       └───────────┬────────────┘
                   ▼
┌──────────────────────────────────────────────┐
│           TOKEN & CONTEXT CONTROLLER          │
│   RTK (Output Compression) · Caveman (Prompt)│
│       Redis (:6380) (Exact / Semantic Cache)  │
└──────────────────────┬───────────────────────┘
                       │
┌──────────────────────▼───────────────────────┐
│            AGENT ORCHESTRATION LAYER         │
│          LangGraph (State & Cycles)          │
│          FastMCP (Typed Tool Server)         │
└──────────────────────┬───────────────────────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
  QDRANT VECTOR DB             NEO4J GRAPH DB
  (:6333 / 768-dim)          (:7687 / 16,660 nodes)
  (Semantic Similarity)       (Structural Relationships)
         │                           │
         └─────────────┬─────────────┘
                       ▼
             KNOWLEDGE OS CONTEXT
                       │
       ┌───────────────▼───────────────┐
       │     BUSINESS APPLICATIONS     │
       ├───────────────────────────────┤
       │ • ops-staff-001-staffing      │
       │ • lt-005-medical-dispatch     │
       │ • 722 Canonical Ventures      │
       │ • 35 Business Sectors         │
       └───────────────┬───────────────┘
                       ▼
       ┌───────────────────────────────┐
       │   OBSERVABILITY & METRICS     │
       │ Langfuse (:3003) · Prometheus │
       │ Grafana (:3001) · OpenTelemetry│
       └───────────────────────────────┘
```

---

## 3. The 70-Project Decision Matrix

### Layer 1: Model Routing & Gateways (Single Endpoint)

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`diegosouzapw/OmniRoute`** | Universal AI router, combo aliases, Caveman/RTK token compression, Tailscale mesh | LiteLLM, TensorZero | **`ADOPT`** | **P0** | Primary local gateway (:20128). Native support for combos, auth, and token compression. |
| **`BerriAI/litellm`** | OpenAI-compatible proxy, multi-provider fallback chains | OmniRoute, TensorZero | **`ADOPT`** | **P0** | Containerized gateway (:4000) inside Mac Studio Docker. Connects Ollama, DeepSeek, and Anthropic fallback. |
| **`tensorzero/tensorzero`** | Model gateway with automated prompt optimization & evals | LiteLLM | **`EVALUATE`** | **P1** | Benchmark in staging for automated prompt optimization and routing evals. |
| **`Portkey-AI/gateway`** | Enterprise AI gateway | OmniRoute | **`REFERENCE`** | **P2** | Cloud-first. Use for fallback routing and retry architecture patterns only. |
| **`Bifrost`** | Fast LLM gateway | LiteLLM | **`DEFER`** | **P2** | Redundant while OmniRoute + LiteLLM fulfill 100% of routing needs. |
| **`9router`** | Early router fork | OmniRoute | **`REMOVE`** | **P3** | Upstream superseded and merged into OmniRoute. |
| **`llm-router`** | Lightweight semantic router | OmniRoute | **`REFERENCE`** | **P2** | Reference for cosine-similarity semantic routing algorithms. |
| **`CLIProxyAPI`** | CLI proxy bridge | OmniRoute | **`REJECT`** | **P3** | Obsolete; OmniRoute CLI targets handle all tool bridges natively. |

---

### Layer 2: Token & Context Compression (Highest Priority)

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`rtk-ai/rtk`** | CLI and tool-result token compression | Headroom | **`ADOPT`** | **P0** | Eliminates 60–90% of tool-call output tokens before they enter model context. |
| **`Caveman`** | Extreme user & system prompt compression | LLMLingua | **`ADOPT`** | **P0** | Built into OmniRoute (`cavemanConfig`). Prunes conversational boilerplate. |
| **`Headroom`** | Buffer compaction & context window management | RTK | **`EVALUATE`** | **P1** | Test for compaction of multi-turn conversational transcripts. |
| **`microsoft/LLMLingua`** | Small-model token pruning based on perplexity | Caveman | **`EVALUATE`** | **P1** | Benchmark token savings vs. answer degradation on code generation tasks. |
| **`microsoft/LLMLingua-2`** | Task-agnostic compressed representations | LLMLingua | **`EVALUATE`** | **P1** | Test fine-tuned BERT compression for RAG documents. |
| **`LongLLMLingua`** | Key-information retrieval compression for long contexts | LlamaIndex | **`EVALUATE`** | **P1** | Relevant when querying 50k+ token financial or legal documents. |
| **`openai/tiktoken`** | Exact BPE token measurement | TokenMonster | **`ADOPT`** | **P0** | Universal token counting standard across agents and billing ledgers. |
| **`TokenMonster`** | High-speed vocabulary tokenizer | tiktoken | **`REFERENCE`** | **P2** | Reference implementation for custom vocabulary training. |
| **`Selective Context`** | Lexical entropy pruning | LLMLingua | **`REFERENCE`** | **P2** | Algorithmic baseline for context pruning. |
| **`Prompt Compression`** | Generic category / papers | — | **`REFERENCE`** | **P2** | Literature archive. |

---

### Layer 3: Local Inference & Model Serving

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`ollama/ollama`** | Containerized/modular local GGUF serving | llama.cpp | **`ADOPT`** | **P0** | Production serving on T7 Shield storage (`/Volumes/T7 Shield/ollama-models`). |
| **`ggerganov/llama.cpp`** | C++ inference engine with Apple Silicon Metal acceleration | Ollama | **`ADOPT`** | **P0** | Low-level backbone of Ollama; verified ~70 tok/sec on Qwen 14B. |
| **`ml-explore/mlx` & `mlx-lm`** | Native Apple Silicon ML framework & LLM engine | llama.cpp, vLLM | **`ADOPT`** | **P0** | Peak throughput runtime for Mac Studio M4 Max unified memory. |
| **`vllm-project/vllm`** | Continuous batching & PagedAttention serving | SGLang | **`EVALUATE`** | **P1** | High-concurrency production serving benchmark. |
| **`vllm-mlx`** | Port of vLLM PagedAttention to Apple Silicon MLX | mlx-lm | **`EVALUATE`** | **P1** | Test continuous batching on Mac Studio M4 Max. |
| **`sgl-project/sglang`** | Fast serving with RadixAttention (KV cache sharing) | vLLM | **`EVALUATE`** | **P1** | RadixAttention optimizes repetitive agent system prompts. |
| **`mlx-serve`** | FastAPI wrapper for MLX models | mlx-lm | **`DEFER`** | **P2** | Redundant with `mlx-lm.server` and Exo. |
| **`mudler/LocalAI`** | Drop-in OpenAI replacement | Ollama, LiteLLM | **`REJECT`** | **P3** | Heavy monolithic footprint; redundant with Ollama + LiteLLM. |
| **`lmstudio-ai / lms`** | Local model desktop manager & CLI | Ollama | **`REFERENCE`** | **P2** | Excellent UI for manual model discovery; CLI installed for reference. |

---

### Layer 4: Multi-Machine & Distributed Inference

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`exo-explore/exo`** | P2P mesh cluster inference across Apple Silicon devices | Ray, Petals | **`ADOPT`** | **P0** | Connects Mac Studio M4 Max (`100.87.214.70`) + MacBook Air (`100.121.17.63`) over Tailscale. |
| **`llama.cpp RPC`** | Native distributed tensor sharding in llama.cpp | Exo | **`EVALUATE`** | **P1** | Simple, lightweight distributed inference without Python overhead. |
| **`PAIR`** | Personal AI Router P2P mesh | Exo | **`REFERENCE`** | **P2** | Study peer node discovery patterns. |
| **`bigscience-workshop/petals`** | BitTorrent-style distributed model swarm | Exo | **`DEFER`** | **P2** | High latency over WAN; unsuitable for tight local mesh. |
| **`ray-project/ray`** | Distributed Python cluster orchestration | Exo | **`DEFER`** | **P2** | Enterprise cluster overkill for a 2-machine local setup. |
| **`microsoft/DeepSpeed`** | Distributed training/inference for CUDA GPUs | — | **`REJECT`** | **P3** | CUDA-exclusive. Incompatible with Apple Silicon Metal/MLX. |
| **`NVIDIA/TensorRT-LLM`** | NVIDIA-specific compiler and serving runtime | — | **`REJECT`** | **P3** | Strictly NVIDIA hardware. |
| **`Speculative Decoding`** | Small draft model + large target model execution | — | **`ADOPT`** | **P1** | Pair local Qwen 0.5B draft with Qwen 14B/32B for 2–3x token speedup. |

---

### Layer 5: Retrieval & Knowledge Substrate

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`qdrant/qdrant`** | Production vector database (Cosine, HNSW, payload filtering) | Chroma, FAISS | **`ADOPT`** | **P0** | Verified live (:6333) with 768-dim `nomic-embed-text` vectors. |
| **`neo4j/neo4j`** | Enterprise property graph database (Cypher) | — | **`ADOPT`** | **P0** | Verified live (:7687) with 16,660 nodes and 722 ventures. |
| **`redis/redis`** | In-memory key-value cache, semantic cache, rate limiter | — | **`ADOPT`** | **P0** | Verified live (:6380) in Mac Studio Docker. Handles exact prompt deduplication. |
| **`langchain-ai/langgraph`** | Cyclic, stateful graph agent orchestrator | LangChain | **`ADOPT`** | **P0** | Standard for multi-agent loops, state checkpointing, and human-in-the-loop. |
| **`langchain-ai/langchain`** | Modular agent components & connectors | LlamaIndex | **`REFERENCE`** | **P1** | Harvest specific tool connectors without adopting the heavy core framework. |
| **`run-llama/llama_index`** | Document ingestion, chunking, and hierarchical indexing | LangChain | **`EVALUATE`** | **P1** | Test for parsing complex corporate PDFs and financial records. |
| **`stanford-futuredata/ColBERT`** | Token-level late-interaction vector retrieval | Qdrant | **`EVALUATE`** | **P1** | Superior accuracy for precision code search; benchmark memory cost. |
| **`FlashRank` / `bge-reranker`** | Ultra-light local neural reranker | — | **`ADOPT`** | **P0** | Condenses 50 vector candidates down to 5 high-precision tokens. |
| **`facebookresearch/faiss`** | Raw vector indexing library | Qdrant | **`REJECT`** | **P3** | Low-level C++ library; Qdrant already provides superior persistence and filtering. |
| **`chroma-core/chroma`** | Developer vector database | Qdrant | **`REJECT`** | **P3** | Redundant with Qdrant; Qdrant has higher production scale and Rust engine. |

---

### Layer 6: Agent Execution, Memory & Sandboxes

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`All-Hands-AI/OpenHands`** | Autonomous software development agent | SWE-agent | **`EVALUATE`** | **P1** | Evaluate for complex multi-file refactoring runs. |
| **`princeton-nlp/SWE-agent`** | Software engineering agent with ACI interface | OpenHands | **`REFERENCE`** | **P2** | Architectural benchmark for agent-computer interfaces. |
| **`e2b-dev/E2B`** | Secure cloud microVM sandbox for untrusted code execution | Daytona | **`EVALUATE`** | **P1** | Sandbox untrusted code execution when building external venture MVPs. |
| **`daytonaio/daytona`** | Self-hosted developer environment orchestrator | E2B | **`EVALUATE`** | **P1** | Self-hosted alternative to cloud microVMs on Mac Studio. |
| **`letta-ai/letta` (MemGPT)** | OS-style memory management (RAM vs. Disk context) | Mem0 | **`EVALUATE`** | **P1** | Architecture for infinite agent context paging. |
| **`mem0ai/mem0`** | Personalized, episodic graph memory for agents | Letta | **`EVALUATE`** | **P1** | Benchmark against Neo4j user-memory graph. |

---

### Layer 7: Protocols, Tooling & Infrastructure Automation

| Repo / Project | Primary Function | Overlap With | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`PrefectHQ/fastmcp`** | High-performance Python MCP server with FastAPI | mcp-go | **`ADOPT`** | **P0** | Standard protocol for Company Brain tools (`_MCP/fastmcp_server.py`). |
| **`mcp-go`** | High-concurrency Go MCP server | FastMCP | **`REFERENCE`** | **P2** | Reference if high-throughput daemon services require Go rewriting. |
| **`n8n/n8n`** | Visual workflow automation & webhook router | Activepieces | **`ADOPT`** | **P0** | Verified live (:5678) in Mac Studio Docker. Handles event triggers. |
| **`activepieces/activepieces`** | Open-source TypeScript automation engine | n8n | **`REFERENCE`** | **P2** | Alternative visual connector ecosystem. |
| **`docker/compose`** | Multi-container service specification | Kubernetes | **`ADOPT`** | **P0** | Core deployment format (`T7/docker-compose.yml`). |
| **`k3s-io/k3s` / `kubernetes`** | Container cluster orchestrator | Docker Compose | **`DEFER`** | **P2** | Premature complexity for 2 physical nodes; Docker Compose is sufficient. |
| **`hashicorp/terraform`** | Infrastructure as Code | Docker Compose | **`REFERENCE`** | **P2** | Retain for cloud edge deployments (Vercel/AWS). |
| **`actions/runner` (GitHub Actions)**| Automated CI/CD and repository linting | — | **`ADOPT`** | **P0** | Production verification pipelines. |
| **`open-telemetry/opentelemetry`** | Universal telemetry standard (traces, metrics, logs) | — | **`ADOPT`** | **P0** | OTel collector active (:4317/:4318) feeding Prometheus and Langfuse. |
| **`langfuse/langfuse`** | LLM tracing, prompt versioning, and cost tracking | — | **`ADOPT`** | **P0** | Verified live (:3003). Captures every prompt, token count, and latency trace. |

---

### Layer 8: Business Applications (Sits ON TOP of Infrastructure)

| Repo / Project | Primary Function | Layer | Decision | Priority | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Worldwidebro/ops-staff-001-staffing`** | Workforce & healthcare staffing operating system | Application | **`ADOPT`** | **P0** | Core revenue venture. Consumes inference, Qdrant, and Neo4j. |
| **`Worldwidebro/lt-005-medical-dispatch`** | Medical courier and route optimization dispatch | Application | **`ADOPT`** | **P0** | Core revenue venture. Uses local Qwen 14B for carrier matching. |
| **`career-ops-hq/career-ops`** | Candidate recruitment pipeline | Application | **`REFERENCE`** | **P1** | Harvest resume scoring and matching logic for `ops-staff-001`. |
| **`MadsLorentzen/ai-job-search`** | Job search aggregator & matcher | Application | **`REFERENCE`** | **P2** | Harvest scraping patterns. |
| **`KnockOutEZ/wigolo`** | Staffing platform workflows | Application | **`REFERENCE`** | **P2** | Workflow reference. |
| **`block/buzz`** | Hive-mind agent communication protocol | Protocol | **`REFERENCE`** | **P2** | Multi-agent signaling patterns. |

---

## 4. Summary of Decisions

* **ADOPT (22)**: The core operating system — OmniRoute, LiteLLM, RTK, Caveman, tiktoken, Ollama, llama.cpp, MLX/MLX-LM, Exo, Speculative Decoding, Qdrant, Neo4j, Redis, LangGraph, FlashRank, FastMCP, n8n, Docker Compose, GitHub Actions, OpenTelemetry, Langfuse, and core ventures (`ops-staff-001`, `lt-005`).
* **EVALUATE (15)**: Staging benchmarks — TensorZero, Headroom, LLMLingua-1/2, LongLLMLingua, vLLM/vLLM-mlx, SGLang, llama.cpp RPC, LlamaIndex, ColBERT, OpenHands, E2B, Daytona, Letta, Mem0.
* **REFERENCE (19)**: Architecture & code harvesting — Portkey, llm-router, TokenMonster, Selective Context, LM Studio, PAIR, LangChain, SWE-agent, mcp-go, Activepieces, Terraform, career-ops, buzz, etc.
* **DEFER (7)**: Valid but premature — Bifrost, Petals, Ray, mlx-serve, K3s/Kubernetes, Make.
* **REJECT (6)**: Incompatible or bloated — 9router, CLIProxyAPI, LocalAI, DeepSpeed, TensorRT-LLM, FAISS, Chroma.
* **REMOVE (1)**: Superseded legacy forks — 9router.

---

## Model & Agent Runtime Connections
- **Models Domain Hub:** [[17-MODELS/17-MODELS|17-MODELS]]
- **Agents Hub:** [[16-AGENTS/README|16-AGENTS]]
- **OmniRoute Router:** [[_INFRASTRUCTURE/omniroute/README|OmniRoute]]
- **Master Evaluation Hub:** [[42-EVALUATION/README|42-EVALUATION]]
- **Runtime Infrastructure State:** [[CLAUDE]]
