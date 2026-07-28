# Learning Feedback System

This document outlines the mechanics of memory, experience collection, and skill optimization loops.

---

## 1. The Feedback Pipeline

Every agent execution loop ends by writing a structured outcome log to Supabase:

```
[Agent Run] ──→ [Capture Output & Cost] ──→ [Evaluate Success/ROI] ──→ [Write to Mem0 / Qdrant]
```

### Stored Memory Types
- **Neo4j (Structural)**: Updates the success rate property on the `:USES` relationship edge between Agent and Skill nodes.
- **Qdrant (Semantic)**: Embeds the raw stack trace (in case of failures) or completion logs into the vector collection `corporate_memory`.
- **Mem0 (Conversational)**: Retains contextual preferences for downstream task prompts.

---

## 2. Dynamic Optimization Loop

When a task fails:
1. The system captures the error log and creates a vector search query against Qdrant.
2. The system identifies similar past failures and their associated resolution scripts.
3. The prompt is modified with "lessons learned" variables before re-execution.
4. If failures persist (> 3 consecutive runs), the pipeline is frozen and escalated to Level 2 human review.
