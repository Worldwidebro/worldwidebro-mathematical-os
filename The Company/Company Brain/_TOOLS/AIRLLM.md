---
id: TOOL-AIRLLM-001
title: AirLLM — 70B+ Layer-by-Layer SSD Streaming Inference Engine
aliases: ["AirLLM", "airllm", "CAP-LARGE-MODEL-INFERENCE"]
tags: [tools, airllm, inference, 70b, offloading, ssd]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[13_ENGINEERING/INFRASTRUCTURE/03_COMPUTE/COMPUTE|COMPUTE]] | [[LOCAL_MODEL_AGENT_STACK_REGISTRY]] | [[INDEX]]

# AirLLM (`lyogavin/airllm`)

**Authority:** CP-027 (Infrastructure & Compute)  
**Status:** ✅ `INSTALLED & VERIFIED` (v4.0.0, script runner at `scripts/airllm_batch_runner.py`)  
**Gap Resolution:** Resolves `CAP-LARGE-MODEL-INFERENCE` utilizing starred repository [`lyogavin/airllm`](https://github.com/lyogavin/airllm) (33,466 ★).

---

## 1. System Overview
AirLLM allows running massive 70B+ parameter models (such as Llama 3 70B, Qwen 72B, or DeepSeek) on machines with limited VRAM by streaming transformer layers sequentially from high-speed SSD storage (`/Volumes/T7 Shield/` or internal NVMe) into RAM layer-by-layer.

## 2. Company Brain Execution Plan
- **Primary Use Case:** Offline deep codebase audits, patent filings, and venture legal review where latency is secondary to context size and parameter depth.
- **Hardware Integration:** Stores model weights on external 2TB T7 Shield / 4TB LaCie storage without starving Mac Studio unified memory needed for active live services.

## 3. CLI Invocations
```bash
python3 scripts/airllm_batch_runner.py --test
python3 scripts/airllm_batch_runner.py --model meta-llama/Meta-Llama-3-70B-Instruct --prompt "Audit venture compliance"
```
