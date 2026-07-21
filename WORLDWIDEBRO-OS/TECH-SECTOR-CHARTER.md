# Tech Sector Charter

## Role: Infrastructure & Operating System for All Ventures

**Tech Sector is NOT a profit center.** It is the shared infrastructure foundation that enables all 6 OPCOs (Construction, Staffing, Real Estate, Education, Finance, Logistics) and all 712 ventures to operate.

---

## Mission

Build and operate the enterprise nervous system (IZA OS) that all ventures depend on — providing data integrity, automation, intelligence, and observability at the speed and scale ventures need.

---

## Responsibilities

### 1. Maintain IZA OS Infrastructure
- **Uptime:** 99.9%+ across all systems (Neo4j, Supabase, Qdrant, Redis, n8n, Ollama, Langfuse, Grafana)
- **Data Integrity:** Ensure Supabase (source of truth) stays consistent, clean, and synced across all connected systems
- **Performance:** <1s query latency for Neo4j, <100ms for Redis, <500ms for Supabase API calls
- **Security:** Encryption at rest, encryption in transit, role-based access control, audit trails

### 2. Provide APIs & Interfaces
- **Supabase API:** RESTful, real-time subscriptions, Row-Level Security for multi-tenant ventures
- **Neo4j Cypher:** Graph query interface for relationship queries (candidates, projects, contracts, risks)
- **Qdrant Vector Search:** Semantic similarity for listings, candidates, documents, recommendations
- **n8n Workflows:** Automation templates ventures can instantiate without code
- **LLM Router:** Unified interface to Ollama (local) and cloud providers (Anthropic, OpenAI, etc.)

### 3. Monitor System Health
- **Observability Layer:** Langfuse (LLM tracing), Prometheus (metrics), Grafana (dashboards), audit logs
- **Self-Awareness:** Real-time health checks, gap detection, orphan identification, metadata tracking (TECH-050)
- **Alerting:** Slack notifications for SLA violations, data inconsistencies, security events
- **Capacity Planning:** Monitor growth, plan scaling before hitting limits

### 4. Govern Data & Schemas
- **Schema Ownership:** Define and evolve tables in Supabase (ventures, contacts, products, capabilities, risks)
- **Data Migrations:** Plan migrations, communicate breaking changes to dependent OPCOs
- **Backup & Recovery:** 24h RPO (recovery point objective), 1h RTO (recovery time objective)
- **Compliance:** SOC 2 Type II controls, data residency, GDPR/CCPA compliance

### 5. Scale Infrastructure
- **Horizontal Scaling:** Add read replicas, partition large tables, optimize queries as data grows
- **Vertical Scaling:** Increase database memory, CPU, storage as needed
- **Cost Optimization:** Monitor spend, right-size instances, identify waste (TECH-050 helps here)
- **Disaster Recovery:** Cross-region backups, failover procedures tested quarterly

---

## Governance Model

### Funding Model
**Cost Center (NOT Profit Center)**

Tech Sector costs are allocated to all 6 OPCOs proportionally:
- **Allocation basis:** Number of ventures, data volume, or API call volume (TBD by CFO)
- **Monthly infrastructure budget:** Supabase ($1K-2K), Neo4j ($500), Redis ($200), n8n ($500), Ollama ($0 + compute), Langfuse ($200-500)
- **Capital:** Tailscale ($10/device), Mac Studio GPU, PostgreSQL backups

### Decision Authority
- **Platform Decisions:** Tech Sector CTO owns infrastructure decisions (which database, which provider, which patterns)
- **OPCO Dependencies:** OPCO Presidents communicate SLA requirements; CTO designs for those SLAs
- **Data Schema:** Tech Sector owns Supabase schema (table definitions, relationships, RLS policies)
- **Venture Usage:** Ventures access infrastructure through APIs; they don't own the infrastructure

### Escalation Path
1. **OPCO President** → Tech Sector CTO: "We need new feature, higher uptime, new capability"
2. **CTO Assessment:** Feasibility, cost, timeline
3. **Planning:** Add to roadmap or declare out-of-scope
4. **Implementation:** Tech Sector builds, OPCO validates
5. **Handoff:** OPCO owns usage; Tech Sector owns reliability

---

## Accountability

### SLA by OPCO

| OPCO | System | SLA | Max Downtime/month | Consequence |
|------|--------|-----|----------|-------------|
| **CON** | Supabase (projects) | 99.5% | 43 min | Can't manage jobs |
| **STA** | Neo4j (matching), Redis (availability) | 99.9% | 43 sec | Matching fails |
| **RE** | Supabase (listings) | 24h data freshness | — | Property info stale |
| **EDU** | Neo4j (course graph), Supabase (progress) | 99% | 7.2 hours | Access denied during peak |
| **FIN** | PostgreSQL (ledger) | 100%, 1s latency | 0 min | Transactions fail |
| **LOG** | Redis (tracking), Neo4j (routes) | 99.9%, <100ms | 43 sec | Shipments untraceable |

### Metrics to Track
- **Availability:** Uptime % (measured by Langfuse/Prometheus)
- **Latency:** P95 response time per system
- **Data Freshness:** Sync lag between Supabase and replicas
- **Cost:** $/venture, $/transaction, $/OPCO
- **Utilization:** Database CPU, memory, storage growth
- **Security:** 0 breaches, 0 unauthorized access

### Reporting
- **Monthly:** SLA compliance report to OPCO Presidents
- **Weekly:** Health check dashboard (TECH-050) visible to all OPCOs
- **Real-time:** Slack alerts for incidents

---

## Constraints & Limitations

### Tech Sector IS Accountable For
- Infrastructure uptime and performance
- Data consistency and backups
- Security and compliance
- API contracts (backwards compatibility)
- Capacity planning and scaling

### Tech Sector IS NOT Accountable For
- Business logic of ventures (OPCO President's job)
- Data quality (venture's job — garbage in, garbage out)
- Application performance (venture's responsibility)
- User experience (venture owns UI/UX)

### Requesting Changes
1. **New Table:** OPCO President submits schema + use case → CTO designs → rollout plan
2. **New API:** OPCO President specifies query pattern → CTO optimizes → documents
3. **Higher SLA:** OPCO quantifies business impact → CTO proposes cost/benefit → budget
4. **New Capability:** CTO proposes (e.g., Qdrant similarity) → OPCO tests → rollout if valuable

---

## Success Criteria (by Month 12)

- ✅ **Uptime:** 99.9%+ across all systems
- ✅ **Coverage:** All 712 ventures can reach platform APIs
- ✅ **Performance:** <1s Supabase queries, <100ms Redis, <500ms Neo4j for typical queries
- ✅ **Data Integrity:** Zero unplanned data losses; 24h RPO/1h RTO verified
- ✅ **Cost:** Infrastructure cost per venture trending down as scale increases
- ✅ **Self-Awareness:** TECH-050 dashboard shows real-time health, missing capabilities, cost allocation
- ✅ **Scalability:** Architecture can handle 10x growth in ventures without major redesign

---

## Related Documents

- **WHOAMI.md** - System constitution and functional roles
- **CLAUDE.md** - Operating System Architecture section (Layer 1 dependency model)
- **OPCO-DEPENDENCY-ARCHITECTURE.md** - Detailed matrix of which OPCO needs which system
- **BUSINESS-ARCHITECTURE-REFERENCE.md** (Task #14) - File ownership and decision routing
- **TECH-050 Specification** (TBD) - Venture OS Intelligence Engine
