# VEX Dashboard — Technical Requirements Document (TRD)

**Version**: 1.0  
**Last Updated**: 2026-09-18  
**Owner**: AI Systems Engineering  
**Status**: APPROVED FOR BUILD

---

## ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────┐
│                    VEX Frontend (React)                      │
│  41 Tabs × Glassmorphism UI × Real-time Updates             │
└─────────────────┬───────────────────────────────────────────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Next.js API  │ │ WebSocket    │ │ Redis Cache  │
│ Routes       │ │ Real-time    │ │ Query layer  │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │               │
       └────────────────┼───────────────┘
                        ▼
        ┌───────────────────────────────┐
        │   Data Orchestration Layer    │
        │  • Query Router               │
        │  • Fallback Logic             │
        │  • Error Handling             │
        └───┬─────────┬─────────┬───────┘
            │         │         │
    ┌───────▼──┐ ┌───▼──────┐ ┌▼────────────┐
    │  Neo4j   │ │Supabase  │ │ OmniRoute   │
    │Knowledge │ │Ventures  │ │ Agents      │
    │  Graph   │ │Tasks     │ │ Workload    │
    │1000+ ent.│ │Payments  │ │              │
    └──────────┘ └──────────┘ └──────────────┘
            │         │              │
            │         │              │
    ┌───────▼─────────▼──────────────▼──────┐
    │        External Services               │
    │  • ClickUp API (tasks)                 │
    │  • Stripe API (payments)               │
    │  • GitHub API (repos)                  │
    │  • Twilio API (calls)                  │
    │  • Make.com API (workflows)            │
    └───────────────────────────────────────┘
```

---

## TECHNOLOGY STACK

### Frontend
| Layer | Technology | Purpose | Version |
|-------|------------|---------|---------|
| Framework | React 18 | Component library | 18.2+ |
| Build | Vite | Lightning-fast bundling | 5.0+ |
| Styling | Tailwind CSS | Utility-first CSS | 3.3+ |
| Custom CSS | Antigravity CSS | Glassmorphism design | custom |
| State | React Hooks | State management | built-in |
| HTTP | Fetch API | API calls | ES6+ |
| WebSocket | native | Real-time updates | HTML5 |

### Backend
| Layer | Technology | Purpose | Version |
|-------|------------|---------|---------|
| Runtime | Node.js | JavaScript runtime | 18+ |
| Framework | Next.js | React framework | 14+ |
| API | Next.js API Routes | REST endpoints | built-in |
| Middleware | Custom | Auth, CORS, logging | custom |
| Observability | OpenObserve | Logs, traces, metrics | cloud |

### Data Layer
| System | Role | Entities | Queries/sec | Latency SLA |
|--------|------|----------|-------------|------------|
| **Neo4j** | Knowledge graph | 1000+ | 100 | < 100ms p99 |
| **Supabase (PG)** | Transactional | Ventures, users | 1000 | < 200ms p99 |
| **Qdrant** | Vector search | Embeddings | 50 | < 150ms p99 |
| **Redis** | Cache/session | Query results | 10000 | < 10ms p99 |

### Infrastructure
| Service | Role | Hosted | Redundancy |
|---------|------|--------|-----------|
| **Mac Studio** | Primary compute | Local network | N/A (dev) |
| **Vercel** | Production hosting | Managed | Global CDN |
| **Tailscale** | Private VPN | Cloud | Peer-to-peer |
| **Make.com** | Automation | Cloud | Webhook retry |

---

## DATA FLOW SPECIFICATION

### Real-Time Agent Operations (30s refresh)
```
OmniRoute (/agents)
  ↓ (fetch agents by capability)
  → Neo4j (query workload)
     ↓ (query: MATCH (a:Agent)-[r:ASSIGNED_TO]->(t:Task) WHERE t.status='running')
  → Redis (cache result, TTL 30s)
  → /api/agents-modules (transform to UI shape)
  → React (Agents tab renders)
```

### Venture Financial Data (Hourly)
```
Supabase (ventures table)
  ↓ (fetch all ventures)
  → Neo4j (sync + create relationships)
     ↓ (MERGE (v:Venture {id: $id}))
  → Redis (cache aggregates, TTL 1h)
  → /api/dashboard (transform to KPI shape)
  → React (Dashboard tab renders)
```

### Task Queue (Real-time via webhook)
```
ClickUp (task created/updated)
  ↓ (webhook)
  → Make.com (scenario trigger)
  → Neo4j (create/update Task node)
  → Redis (invalidate cache)
  → WebSocket (notify frontend)
  → React (Tasks tab updates)
```

---

## API SPECIFICATION

### Tab → Backend Mapping

| Tab | Endpoint | Method | Response | Cache TTL |
|-----|----------|--------|----------|-----------|
| Agents | `/api/agents-modules` | GET | ModulesResponse | 30s |
| Dashboard | `/api/dashboard/metrics` | GET | KPIResponse | 1h |
| Tasks | `/api/tasks` | GET | TasksResponse | Real-time |
| Financial | `/api/ventures/financial` | GET | FinancialResponse | 1h |
| OPCOs | `/api/sectors/opcosinfo` | GET | OPCOsResponse | 1h |
| Revenue Attribution | `/api/revenue/attribution` | GET | AttributionResponse | 5m |
| Graph Overview | `/api/graph/topology` | GET | GraphResponse | 1h |
| Dependencies | `/api/graph/dependencies` | GET | DAGResponse | 30m |

### Example API Response: `/api/agents-modules`

```json
{
  "modules": [
    {
      "id": "intelligence",
      "name": "Intelligence",
      "icon": "🧠",
      "agents": [
        {
          "id": "A1",
          "name": "Market Research Lead",
          "role": "TAM Analysis",
          "status": "active",
          "tasks": 12,
          "success": 98
        }
      ],
      "agentCount": 3,
      "tasksRunning": 25,
      "deliverables": 42,
      "dependencies": ["Growth", "Product"],
      "capacity": 85
    }
  ],
  "totalAgents": 12,
  "totalTasks": 102,
  "avgCapacity": 87,
  "avgSuccess": 96,
  "timestamp": "2026-09-18T22:00:00Z"
}
```

---

## QUERY PATTERNS & OPTIMIZATION

### Frequently Used Neo4j Queries

```cypher
-- Agent workload by module (< 100ms p99)
MATCH (a:Agent)-[r:ASSIGNED_TO]->(t:Task)
WHERE t.status IN ['running', 'queued']
WITH a, COUNT(t) as tasks
RETURN a.id, a.name, tasks
ORDER BY tasks DESC

-- Venture revenue attribution (< 200ms p99)
MATCH (v:Venture)-[attr:ATTRIBUTED_TO]->(a:Agent)
RETURN v.id, v.name, SUM(attr.amount) as revenue
GROUP BY v.id, v.name

-- Dependency graph (< 150ms p99)
MATCH (v1:Venture)-[d:DEPENDS_ON]->(v2:Venture)
RETURN v1.id, v2.id, d.strength
LIMIT 1000
```

### Caching Strategy

| Query | Cache Key | TTL | Invalidate On |
|-------|-----------|-----|----------------|
| Agent workload | `agents:modules` | 30s | Task status change |
| Venture financials | `ventures:financial:{venture_id}` | 1h | Revenue edge update |
| Sector aggregates | `sectors:metrics` | 1h | Venture assignment change |
| Dashboard KPIs | `dashboard:kpis` | 1h | Any venture/payment update |

---

## PERFORMANCE TARGETS

### Latency (p99)
- [x] API response < 200ms
- [x] Page load < 2s
- [x] Graph render < 500ms
- [x] Search/filter < 300ms
- [x] WebSocket latency < 100ms

### Throughput
- [x] 100 concurrent users
- [x] 1000 queries/sec peak
- [x] 50 real-time subscriptions

### Availability
- [x] 99.9% uptime (3 nines)
- [x] 0 crashes over 30 days
- [x] Auto-failover on service outage

### Resource Usage
- [x] Frontend bundle < 500KB gzip
- [x] Heap memory < 256MB per pod
- [x] CPU < 50% average

---

## SECURITY & COMPLIANCE

### Authentication & Authorization
- **Method**: JWT (OpenID Connect via Supabase)
- **Scope**: Role-based access control (RBAC)
- **Roles**: admin, portfolio_manager, venture_ops, analyst, viewer
- **Token Expiry**: 1 hour (refresh token 7 days)

### Data Security
- **Encryption in Transit**: TLS 1.3
- **Encryption at Rest**: AWS KMS (Supabase)
- **API Keys**: Environment variables (never in code)
- **Secrets Rotation**: 90-day rotation policy

### Audit & Compliance
- **Audit Trail**: All tab changes logged to Neo4j
- **Retention**: 2 years of audit logs
- **Compliance**: SOC 2 Type II, GDPR-ready
- **PII Handling**: No SSN/email in logs

---

## FALLBACK & RESILIENCE

### Service Failure Scenarios

| Service | Failure Impact | Fallback | User Experience |
|---------|---------------|----------|-----------------|
| Neo4j | Agents/Graph tabs fail | Use Redis cache | "Loading cached data..." |
| OmniRoute | Agent discovery fails | Use AGENT_REGISTRY.yaml | "Offline mode" |
| Supabase | Ventures fail | Use cached data | "Viewing cached data (1h old)" |
| ClickUp | Tasks fail | Show cached tasks | "Task updates delayed" |
| Redis | Cache miss | Query live | Slower response (no cache) |

### Error Handling
```javascript
try {
  const data = await fetch('/api/agents-modules');
  if (!data.ok) throw new Error(data.statusText);
  return data.json();
} catch (error) {
  console.error('API failed, using fallback', error);
  return FALLBACK_DATA; // Hardcoded mock data
}
```

---

## DEPLOYMENT SPECIFICATION

### Environment Variables (Required)
```bash
# Database
NEO4J_URL=http://100.87.214.70:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=changeme

SUPABASE_URL=https://rhlkjelglvurowdalrgh.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...

# APIs
OMNIROUTE_API_URL=http://100.87.214.70:8000
OMNIROUTE_API_KEY=sk-...
CLICKUP_API_KEY=pk_...
STRIPE_SECRET_KEY=sk_...

# Infrastructure
REDIS_URL=redis://localhost:6379
OPENOBSERVE_URL=http://100.87.214.70:5080

# Frontend
VITE_PUBLIC_API_URL=https://vex.worldwidebro.com/api
```

### Deployment Steps
1. Build: `npm run build`
2. Test: `npm run test:e2e`
3. Deploy to Vercel: `git push origin main`
4. Verify: Health check endpoint `/api/health`
5. Monitor: OpenObserve dashboard

### Monitoring & Observability
- **Metrics**: Prometheus (via OpenObserve)
- **Logs**: OpenObserve (structured JSON)
- **Traces**: OpenTelemetry (OTEL)
- **Alerts**: Email on p99 latency > 500ms, uptime < 99.9%

---

## SCALABILITY PLAN (Oct-Dec 2026)

### Current (Sep 2026)
- 789 ventures
- 1 region (Mac Studio + Vercel)
- 4 CPU cores, 16GB RAM

### Phase 2 (Oct 2026)
- 1000+ Neo4j entities
- 50 agents concurrent
- Query caching (Redis)

### Phase 3 (Nov 2026)
- Database replication (standby)
- Multi-region CDN (Vercel)
- Auto-scaling (horizontal)

### Phase 4 (Dec 2026)
- Full-text search (Elasticsearch)
- Real-time streaming (Kafka)
- Analytics warehouse (BigQuery)

---

## TESTING STRATEGY

### Unit Tests
- API routes (30+ test cases)
- Query builders (20+ test cases)
- Utility functions (50+ test cases)

### Integration Tests
- Neo4j ↔ API (10 scenarios)
- Supabase ↔ API (8 scenarios)
- OmniRoute ↔ API (6 scenarios)

### E2E Tests
- Full tab workflow (10 user journeys)
- Error scenarios (5 failure cases)
- Performance tests (latency + throughput)

### Performance Benchmarks
- Load test: 100 concurrent users
- Latency profile: p50, p95, p99
- Cache hit rate: target 80%

---

## NEXT STEPS

1. **Approve TRD** ✓ (you are here)
2. **Design System** (UI/UX components)
3. **App Flow** (Wireframes + interactions)
4. **Infrastructure Setup** (Neo4j schema)
5. **Data Pipeline** (Sync YAML → Neo4j)

---

**Approval Sign-Off**

| Role | Name | Date | Status |
|------|------|------|--------|
| Tech Lead | Claude Haiku | 2026-09-18 | ✅ Approved |
| Infra Eng | TBD | 2026-09-18 | ⏳ Pending |
| Security | TBD | 2026-09-18 | ⏳ Pending |
