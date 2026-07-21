# OPCO Dependency Architecture

**Who needs what from [[IZA OS]]?**

All 6 OPCOs and their 712 ventures depend on [[TECH-SECTOR-CHARTER | Tech Sector]] infrastructure. This document maps the dependencies so we understand impact when systems are upgraded, down, or change.

---

## Dependency Matrix

### By Database/System

| SYSTEM | CRITICAL FOR | SLA | FAILURE IMPACT |
|--------|--------------|-----|----------------|
| **Supabase** | All OPCOs | 99.5%-99.9% | Can't read/write ventures, contacts, products |
| **Neo4j** | STA, RE, FIN | 99.9% | Matching fails; risk modeling breaks |
| **Redis** | STA, LOG | 99.9%, <100ms | Real-time features fail |
| **Qdrant** | RE, STA, FIN | 99% | Similarity search fails |
| **n8n** | All OPCOs | 95%+ | Manual work increases; automation stalls |
| **PostgreSQL** | FIN, All others | 100%, 1s latency | Ledger inconsistent; transactions fail |
| **LiteLLM** | All OPCOs | 95%+ | LLM features unavailable |
| **Langfuse** | Tech Sector | 90% | Can't see LLM performance |
| **Prometheus+Grafana** | Tech Sector | 90% | Can't see system metrics |

---

## By OPCO

### Construction (CON-*)

**Critical Systems:** Supabase (projects, vendors), n8n (job automation), document storage  
**SLA Requirements:** 99.5% Supabase, 99% n8n  
**Scaling:** Projects 5GB → 50GB; ventures table 1GB → 10GB; 10 → 100 n8n workflows

**Dependencies:**
```
CON ventures → Supabase (projects, vendors, contracts)
            → n8n (job auto-assignment)
            → Slack/Email (crew notifications)
```

**Downtime Impact:** Can't see/manage projects; crews can't get assignments

---

### Staffing (STA-*)

**Critical Systems:** Neo4j (candidate graph), Redis (availability), Supabase (contacts, jobs)  
**SLA Requirements:** 99.9% Neo4j, 99.9% Redis, 99.5% Supabase  
**Scaling:** Candidates 1M → 10M nodes; availability 10K → 100K per second; applications 5M+ /year

**Dependencies:**
```
STA ventures → Neo4j (candidate graph, matching)
            → Redis (real-time availability <100ms)
            → Supabase (contacts, jobs, applications)
            → Qdrant (resume semantic search)
            → n8n (auto-contact, interview scheduling)
            → LiteLLM (candidate scoring)
```

**Downtime Impact:** Neo4j down = can't match candidates to jobs; business stops

---

### Real Estate (RE-*)

**Critical Systems:** Supabase (listings), Qdrant (property similarity), market data  
**SLA Requirements:** 99.5% Supabase, 24h data freshness, 95% LiteLLM  
**Scaling:** Properties 10K → 1M; listings 100MB → 100GB; historical transactions 100M+

**Dependencies:**
```
RE ventures → Supabase (listings, prices, photos, buyers)
           → Qdrant (property similarity, recommendations)
           → Market data (daily price updates)
           → n8n (auto-publish listings, auto-contact leads)
           → LiteLLM (price prediction, buyer matching)
```

**Downtime Impact:** Supabase down = listings disappear; Qdrant down = similar properties not returned

---

### Education (EDU-*)

**Critical Systems:** Neo4j (course graph), Supabase (student progress), video storage  
**SLA Requirements:** 99% during school hours, 95% off-hours  
**Scaling:** Courses 100 → 10K; concepts 1K → 100K; students 10K → 1M; videos 100GB → 10TB

**Dependencies:**
```
EDU ventures → Neo4j (course structure, prerequisites, learning paths)
            → Supabase (student progress, grades, enrollment)
            → Video storage (lesson videos ~1GB/course)
            → n8n (enrollment workflows, certificate generation)
            → LiteLLM (personalized tutoring, explanations)
```

**Downtime Impact:** Neo4j down = students can't navigate curriculum; Supabase down = progress not tracked

---

### Finance (FIN-*)

**Critical Systems:** PostgreSQL (ledger), Neo4j (risk modeling), Supabase (accounts)  
**SLA Requirements:** 100% PostgreSQL uptime, 1s latency, 0 data loss  
**Scaling:** Transactions 10K → 1M/day; counterparties 100 → 10K; relationships 1K → 1M

**Dependencies:**
```
FIN ventures → PostgreSQL (general ledger, transaction log, audit trail)
            → Neo4j (counterparty relationships, risk exposure, portfolio network)
            → Supabase (accounts, balances, customers, transactions)
            → n8n (transaction settling, invoice generation, compliance)
            → LiteLLM (credit scoring, fraud detection)
```

**Downtime Impact:** PostgreSQL down = compliance violation; can't process transactions

---

### Logistics (LOG-*)

**Critical Systems:** Redis (real-time tracking), Neo4j (route optimization), Supabase (shipments)  
**SLA Requirements:** 99.9% Redis <100ms, 99.9% Neo4j, 99.5% Supabase  
**Scaling:** Shipments in transit 1K → 100K/second; route nodes 1K → 100K; daily shipments 10K → 100K

**Dependencies:**
```
LOG ventures → Redis (real-time shipment tracking <100ms)
            → Neo4j (route network, optimization)
            → Supabase (shipments, orders, customers, carriers)
            → n8n (pickup scheduling, delivery confirmation)
            → LiteLLM (dynamic routing, ETA prediction)
```

**Downtime Impact:** Redis down = can't track in real-time; Neo4j down = route optimization fails

---

## Impact Analysis: If X Goes Down

| System | Duration | OPCOs Affected | Ventures Affected | Revenue Impact | Mitigation |
|--------|----------|---|---|---|---|
| **Supabase** | 1h | ALL | All 712 | $50K-100K/h | Read-only replica; failover <5m |
| **Neo4j** | 1h | STA, RE, FIN | ~200 | $10K-20K/h | Cached queries; simple matching fallback |
| **Redis** | 1h | STA, LOG | ~50 | $5K-10K/h | In-memory cache; message queue |
| **n8n** | 8h | ALL | All 712 | $5K-15K | Manual workflows; job queuing |
| **PostgreSQL** | 1h | FIN | ~100 | $20K-50K/h | CRITICAL: compliance failure |

---

## Priority Tier by Impact

### Tier 1 (Highest)
- **Supabase:** All ventures depend on it
- **PostgreSQL:** Financial ledger; compliance critical
- **Neo4j:** Matching/recommendations; revenue-generating
- **Redis:** Real-time availability; timing-sensitive

### Tier 2 (Medium)
- **n8n:** Automation; manual workaround exists
- **Qdrant:** Recommendations; fallback to basic search
- **LiteLLM:** AI features; manual scoring possible

### Tier 3 (Low)
- **Langfuse:** Observability; doesn't affect users
- **Prometheus/Grafana:** Monitoring; indirect impact only
- **Ollama:** Local inference; fallback to cloud

---

## Capacity Planning

### Current State (Q3 2026)
- Supabase: ~500GB data, 1M queries/day
- Neo4j: ~1M nodes, 2M relationships
- Redis: ~10GB in-memory
- Qdrant: ~1M vectors, ~100GB storage
- n8n: ~100 workflows, 10K executions/day

### Q4 2026 Forecast (10x growth in ventures)
- Supabase: ~5TB data, 10M queries/day
- Neo4j: ~10M nodes, 20M relationships
- Redis: ~100GB in-memory, <50ms latency required
- Qdrant: ~10M vectors, ~1TB storage
- n8n: ~1K workflows, 100K executions/day

### Required Scaling
- **Supabase:** Add read replicas; partition large tables; optimize indexes
- **Neo4j:** Increase heap; consider federation if nodes exceed 10M
- **Redis:** Upgrade to Redis Cluster; increase max memory
- **Qdrant:** Distributed Qdrant; separate collections by OPCO
- **n8n:** Parallel execution tier; workflow queue optimization

---

## Related Documents

- [[TECH-SECTOR-CHARTER]] - Tech Sector responsibilities and SLAs
- [[CLAUDE.md]] - Operating System Architecture (Dependency Flow section)
- [[WHOAMI.md]] - System constitution (Organizational Role section)
- [[BUSINESS-ARCHITECTURE-REFERENCE.md]] (TBD) - File ownership and decision routing
