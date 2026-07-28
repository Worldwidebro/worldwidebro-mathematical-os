# Repository Layer Mapping — Categorize 1,644 Repos to 19 Layers

**Source:** REPOSITORY-REGISTRY.json (1,644 repos)

**Goal:** Map every repo to architectural layer (0-19)

---

## Layer 0: Developer Experience
**Semantic code search + understanding + impact analysis**

Keywords: search, navigate, understand, explain, impact, codebase-tool

---

## Layer 1: Repository Intelligence
**Dependency graphs + visualization + pattern extraction**

Keywords: graph, dependency, visualization, pattern, code-analysis, gitnexus, graphify

---

## Layer 2: Knowledge Graph
**Entity + relationship management + semantic understanding**

Keywords: neo4j, graph-db, knowledge-graph, entity-management

---

## Layer 3: Vector Memory
**Embeddings + semantic search + clustering**

Keywords: vector, embedding, semantic-search, qdrant, similarity

---

## Layer 4: Document Intelligence
**PDF parsing + OCR + table extraction**

Keywords: pdf, document, ocr, stirling-pdf, extraction

---

## Layer 5: Model Runtime
**Local/distributed inference + model serving**

Keywords: ollama, inference, model-serving, colibri, exo

---

## Layer 6: Model Gateway
**Provider routing + fallback + quota management**

Keywords: gateway, router, model-selection, litellm, omniroute

---

## Layer 7: Agent Runtime
**Multi-agent orchestration + tool calling**

Keywords: agent, crewai, orchestration, agentic, multi-agent

---

## Layer 8: Skills
**Reusable capabilities (estimate, research, write, review, debug)**

Keywords: skill, estimate, forecast, research, write, review, code-review, capability

---

## Layer 9: Workflows
**Business processes (sales, construction, staffing, family, wealth)**

Keywords: workflow, process, automation, loop, pipeline, venture-bootstrap

---

## Layer 10: Event Bus
**Async messaging (NATS, Kafka, Redis Streams)**

Keywords: event-bus, message-queue, kafka, nats, redis-streams, pubsub

---

## Layer 11: APIs
**REST + GraphQL + gRPC interfaces**

Keywords: api, rest, graphql, grpc, fastapi, express, gateway

---

## Layer 12: Storage
**Databases + object storage + caching**

Keywords: database, postgres, storage, warehouse, redis, minio, duckdb, supabase

---

## Layer 13: Identity
**User management + OAuth + RBAC + multi-tenancy**

Keywords: identity, auth, oauth, keycloak, user-management, rbac

---

## Layer 14: Secrets + Policy
**Credential vaults + policy enforcement + audit**

Keywords: vault, secret, policy, cedar, audit, credential, compliance

---

## Layer 15: Observability
**Tracing + logging + metrics + dashboards**

Keywords: observability, tracing, logging, prometheus, grafana, jaeger, langfuse, otel

---

## Layer 16: Evaluation
**LLM evals + rubrics + A/B testing + benchmarks**

Keywords: evaluation, test, benchmark, rubric, deepeval, ragas, prompt-testing

---

## Layer 17: Security
**Safety + prompt injection + jailbreak detection + guardrails**

Keywords: security, safety, guardrails, injection-detection, jailbreak, filter

---

## Layer 18: Platform Services
**Notifications + search + scheduler + billing + audit + feature-flags + analytics**

Keywords: notification, email, sms, slack, push, search, scheduler, billing, audit, feature-flag, analytics, permission, registry, cache, platform-service

---

## Layer 19: Applications
**Venture-specific applications (Construction, Staffing, Real Estate, Family, Wealth)**

Keywords: -os, venture, app, application, con-ventures, staffing, real-estate, family, wealth, edu, fin, comm, tech, lt, re

---

## Categorization Algorithm

```python
def classify_repo(repo):
    """
    Classify repo into layer 0-19 based on keywords + tech stack
    """
    keywords = (
        repo['name'].lower() +
        ' ' +
        (repo['PURPOSE'] or '').lower() +
        ' ' +
        (repo['CATEGORY'] or '').lower() +
        ' ' +
        (repo['TECH_STACK'] or '').lower()
    )
    
    # Check each layer's keywords (in order)
    layers = {
        19: ['con-', 'staffing-', 'real-estate', 'family-', 'wealth-', '-os', 'venture-', 'edu-', 'fin-', 'comm-', 'tech-', 'lt-', 're-'],
        18: ['notification', 'email-service', 'sms', 'slack', 'push', 'search-', 'scheduler', 'billing', 'audit', 'feature-flag', 'analytics', 'permission', 'registry', 'cache', 'platform'],
        17: ['security', 'safety', 'guardrails', 'jailbreak', 'injection', 'filter'],
        16: ['evaluation', 'eval', 'test', 'benchmark', 'rubric', 'deepeval', 'ragas', 'prompt-test'],
        15: ['observability', 'tracing', 'logging', 'prometheus', 'grafana', 'jaeger', 'langfuse', 'otel', 'metrics'],
        14: ['vault', 'secret', 'policy', 'cedar', 'audit', 'credential', 'compliance'],
        13: ['identity', 'auth', 'oauth', 'keycloak', 'user-', 'rbac', 'multi-tenant'],
        12: ['database', 'postgres', 'storage', 'warehouse', 'redis', 'minio', 'duckdb', 'supabase', 'clickhouse'],
        11: ['api', 'rest', 'graphql', 'grpc', 'fastapi', 'express', 'gateway', 'endpoint'],
        10: ['event-bus', 'message-queue', 'kafka', 'nats', 'redis-streams', 'pubsub', 'event-driven'],
        9: ['workflow', 'process', 'automation', 'loop', 'pipeline', 'funnel', 'bootstrap'],
        8: ['skill', 'estimate', 'forecast', 'research', 'write', 'review', 'debug', 'capability'],
        7: ['agent', 'crewai', 'orchestration', 'agentic', 'multi-agent'],
        6: ['gateway', 'router', 'model-selection', 'litellm', 'omniroute', 'provider'],
        5: ['ollama', 'inference', 'model-serving', 'colibri', 'exo', 'llm-runtime'],
        4: ['pdf', 'document', 'ocr', 'stirling', 'extraction', 'table-extract'],
        3: ['vector', 'embedding', 'semantic-search', 'qdrant', 'similarity', 'cluster'],
        2: ['neo4j', 'graph-db', 'knowledge-graph', 'entity', 'relationship'],
        1: ['graph', 'dependency', 'visualization', 'pattern', 'gitnexus', 'graphify', 'socraticode'],
        0: ['search', 'navigate', 'understand', 'explain', 'impact', 'codebase-tool']
    }
    
    for layer in sorted(layers.keys(), reverse=True):
        if any(kw in keywords for kw in layers[layer]):
            return layer
    
    return None  # Unclassified
```

---

## Expected Distribution

| Layer | Category | Expected Count | Reason |
|-------|----------|----------------|--------|
| 0-2 | Knowledge Infrastructure | ~50 | Developer tools + graph |
| 3-6 | LLM Infrastructure | ~80 | Vector + runtime + gateway |
| 7-9 | Agent Layer | ~120 | Agents + skills + workflows |
| 10-14 | Platform Infrastructure | ~30 | Often outsourced/shared |
| 15-18 | Observability + Security | ~40 | Cross-cutting concerns |
| 19 | Applications | ~1,200+ | Venture-specific code |
| Unclassified | Unknown | ~30-50 | Need manual review |
| **Total** | | **~1,644** | |

---

## Scan Results (To Be Generated)

Run this to generate the mapping:

```bash
python /Users/acebless/Documents/01_AI_BRAIN/scripts/classify-repos.py \
  --input /Users/acebless/Documents/.claude/worktrees/*/WORLDWIDEBRO-OS/08-DATA/*/REPOSITORY-REGISTRY.json \
  --output /Users/acebless/Documents/01_AI_BRAIN/REPOSITORY-LAYER-SCAN.json
```

Output will show:
- Repos per layer (count + list)
- Unclassified repos (need manual categorization)
- High-value repos per layer (stars + strategic value)
- Gaps (layers with <5 repos)

---

**Status:** Ready to scan all 1,644 repos
