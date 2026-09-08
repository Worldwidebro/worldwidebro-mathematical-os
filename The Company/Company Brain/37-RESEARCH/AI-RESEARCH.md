---
id: RES-AI-001
title: "AI-RESEARCH — Artificial Intelligence & Model Intelligence"
tags: [research, ai, models, benchmarks, omniroute, litellm, evaluation]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[37-RESEARCH/README|37-RESEARCH]] | [[17-MODELS/17-MODELS|17-MODELS]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[42-EVALUATION/README|42-EVALUATION]]

# AI-RESEARCH.md — Artificial Intelligence & Model Intelligence

> **Authority:** AI & Agent Control Plane (CP-006 / CP-007)  
> **Feeds:** Hugging Face (`SRC-HUGGINGFACE`), Papers with Code, Stanford AI Index (`SRC-AI-INDEX`), arXiv cs.AI/cs.LG/cs.CL  
> **Operational Integration:** OmniRoute (`:20128`), LiteLLM (`:4000`), Exo MLX Serving (`:52415`), FastMCP

---

## 1. Multi-Domain AI Research Taxonomy

```text
AI RESEARCH
├── Models & Architectures
│   ├── Large Language Models (Dense & MoE)
│   ├── Multimodal (Vision-Language, Audio, Video)
│   ├── Small Language Models (SLMs: 1B–8B edge execution)
│   └── Speculative Decoding & Draft Models
│
├── Agentic Systems & Reasoning
│   ├── Multi-Agent Orchestration (Antigravity, Agentlas, Swarms)
│   ├── Long-Horizon Planning & Tool Use
│   ├── Tree-of-Thought & Self-Correction Loops
│   └── Human-in-the-Loop Governance & Guardrails
│
├── Knowledge & Memory
│   ├── Graph-RAG & Hybrid Relational Retrieval (Neo4j + Qdrant)
│   ├── Bitemporal Context Windows & Context Compression
│   └── Persistent Agent Memory & Episodic Retrieval
│
├── Infrastructure & Hardware
│   ├── Native Apple Silicon MLX Serving (`exo`)
│   ├── Quantization (AWQ, GPTQ, GGUF, EXL2, MLX 4/5-bit)
│   ├── Distributed Tensor Parallelism over Tailscale Mesh
│   └── Low-Latency Prompt Caching (Redis / KV-Cache)
│
└── AI Economics
    ├── Token Cost vs. Task Value Analysis
    ├── Self-Hosted Local FLOPs vs. Frontier Cloud API Fallback
    └── Energy & Compute ROI per Economic Unit of Work
```

---

## 2. Benchmark Ground Truth (No Hype)

Every model evaluated for Company Brain must be scored on reproducible, standardized benchmarks before deployment into OmniRoute:

| Benchmark | Target Capability | Critical Threshold for Production |
| :--- | :--- | :--- |
| **SWE-bench Verified** | Autonomous software engineering | > 35% resolved |
| **LiveCodeBench** | Fresh, un-contaminated coding logic | > 45% pass@1 |
| **AgentBench** | Multi-step tool use & environment interaction | > 70% success |
| **GPQA Diamond** | Deep expert reasoning & factual accuracy | > 55% zero-shot |
| **Needle-in-a-Haystack** | 128k+ retrieval accuracy | 100% across all depth/length quadrants |

---

## 3. OmniRoute Dynamic Combo Pipeline

AI Research feeds directly into OmniRoute's model combo configs on Mac Studio:
1. **Fast Local Reasoning (Zero Cost):** `exo` MLX `Qwen3.6-35B-A3B-5bit` on Mac Studio (`100.87.214.70:52415`).
2. **Mobile Node Fallback:** Ollama `qwen2.5:32b` or `qwen3:8b` on T7 Shield (`100.121.17.63:11434`).
3. **Complex Frontier Escalation:** Anthropic Claude 3.5 Sonnet / Opus or OpenAI o3 for high-risk legal/architecture decisions when local confidence < 0.85.

---

## Connected Subsystems & Architecture
- **Models Gateway:** [[17-MODELS/17-MODELS|17-MODELS]]
- **OmniRoute Router:** [[_INFRASTRUCTURE/omniroute/README|OmniRoute Infrastructure]]
- **Evaluation & Benchmarks:** [[42-EVALUATION/README|42-EVALUATION]]
- **Relational Knowledge Graph:** [[08-KNOWLEDGE-GRAPH/Neo4j|Neo4j Graph]]
- **Vector Memory:** [[10-MEMORY/10-MEMORY|Qdrant Memory]]
