# AI Boss OS

Unified operating system for managing 700+ ventures across multiple sectors.

## Quick Start

**First time?**
```bash
make bootstrap
```

**Already set up?**
```bash
make up
make health
```

## Common Commands

```bash
make up          # Start all services
make down        # Stop all services
make status      # See what's running
make health      # Validate services
make logs        # Tail service logs
make seed        # Populate initial data
make db-shell    # PostgreSQL psql
make neo4j-shell # Neo4j Cypher shell
```

## Services

- **Grafana** (dashboards): http://localhost:3001 — admin/ventures2026
- **Neo4j** (knowledge graph): http://localhost:7474 — neo4j/ventures2026
- **Qdrant** (vector search): http://localhost:6333
- **LiteLLM** (model router): http://localhost:4000
- **Langfuse** (observability): http://localhost:3003
- **Prometheus** (metrics): http://localhost:9090
- **n8n** (workflows): http://localhost:5678

## Bootstrap Flow (make bootstrap)

```
Phase 1: Check Docker, disk, RAM
Phase 2: Setup .env
Phase 3: Create directories
Phase 4: Pull Docker images (2-3 min)
Phase 5: Start postgres + redis, wait for health
Phase 6: Initialize PostgreSQL schema (7 tables, 5 indexes)
Phase 7: Start all 9 services
Phase 8: Initialize Neo4j schema (constraints, 4 sectors)
Phase 9: Run health checks
→ COMPLETE (3-5 min total)
```

Then run `make seed` to populate initial data.

## Troubleshooting

**Services won't start?**
```bash
make clean && make bootstrap
```

**Specific service broken?**
```bash
docker compose restart postgres
make logs service=postgres
```

**Everything down?**
```bash
make health
```

---

**AI Boss OS** — Multi-sector venture management platform.
