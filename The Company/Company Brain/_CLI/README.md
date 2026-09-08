# Company Brain CLI — Unified Command Interface
**Deploy, configure, and verify complete Company Brain infrastructure via single CLI**

Authority: [[Infrastructure Control Plane]] (CP-027)  
Status: Production-ready  
Schema: `_CLI/schema.yaml` (auto-generated via [[CLI-Anything|https://github.com/HKUDS/CLI-Anything]])

---

## Installation

### Option 1: Using CLI-Anything (when available)
```bash
# Install CLI-Anything globally
npm install -g @hkuds/cli-anything

# Generate CLI from schema
cli-anything _CLI/schema.yaml

# Verify installation
cb --help
```

### Option 2: Using Bootstrap Script (always works)
```bash
# Navigate to project root
cd /Users/acebless/Documents/The\ Company/Company\ Brain

# Run bootstrap (generates _CLI/bin/cb)
bash _CLI/bootstrap.sh

# Use locally
_CLI/bin/cb --help

# Or install globally (requires sudo)
sudo cp _CLI/bin/cb /usr/local/bin/
cb --help
```

### Verify Installation
```bash
cb infrastructure status    # Should show all services ✅
cb test e2e                # Should pass all tests ✅
```

---

## Quick Commands

```bash
# 1️⃣ Check infrastructure status
cb infrastructure status

# 2️⃣ Deploy all phases (databases, models, services, observability)
cb infrastructure deploy --phase all

# 3️⃣ Setup OmniRoute AI gateway
cb omniroute setup --auto

# 4️⃣ Wire Neo4j ontology
cb neo4j wire-ontology

# 5️⃣ Run end-to-end test
cb test e2e

# 6️⃣ Sync all 6 control planes
cb control-planes sync
```

---

## Full Command Reference

### Infrastructure Commands

**Deploy infrastructure phases:**
```bash
cb infrastructure deploy --phase all      # All phases (1-4)
cb infrastructure deploy --phase 1        # Databases only
cb infrastructure deploy --phase 2        # Models only
cb infrastructure deploy --phase 3        # Exo distributed inference
cb infrastructure deploy --phase 4        # Observability stack
```

**Check health:**
```bash
cb infrastructure status                  # Full health report
```

### OmniRoute Commands

**Setup AI gateway:**
```bash
cb omniroute setup --auto                 # Auto-configure
cb omniroute login                        # Manual login
cb omniroute test --model qwen2.5-coder:14b  # Test inference
```

### Neo4j Commands

**Wire knowledge graph:**
```bash
cb neo4j wire-ontology                    # Create OmniRoute relationships
cb neo4j status                           # Show graph statistics
```

### MCP Commands

**Setup Claude Code integration:**
```bash
cb mcp setup                              # Configure MCP server
```

### Testing Commands

**Run tests:**
```bash
cb test e2e                               # End-to-end test
cb test models                            # Test all models
```

### Control Plane Commands

**Manage control planes:**
```bash
cb control-planes sync                    # Sync CP-006 through CP-029
cb control-planes status                  # Show readiness
```

### Documentation Commands

**View docs:**
```bash
cb docs infrastructure                    # Infrastructure guide
```

---

## Service Dashboards

| Service | URL | Login |
|---------|-----|-------|
| **OmniRoute** | http://100.87.214.70:20128/dashboard | admin@omniroute.local / _.Thewave12 |
| **Neo4j** | http://100.87.214.70:7474 | neo4j / changeme |
| **Grafana** | http://100.87.214.70:3010 | admin / admin |
| **Langfuse** | http://100.87.214.70:3003 | — |

---

## Architecture Reference

**Core Registries:**
- [[CLAUDE.md|Project Authority]] — Master infrastructure document
- [[INFRASTRUCTURE_REGISTRY.yaml|Device Inventory]] — Hardware + storage topology
- [[LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml|Model Routing]] — Compatibility matrix + benchmarks
- [[DEPLOYMENT_PHASES.md|Rollout Roadmap]] — Phase-by-phase timeline

**Control Planes (CP-006 to CP-029):**
- **CP-006** [[Agents]] — Agent routing and orchestration
- **CP-007** [[Models]] — Model selection and fallbacks
- **CP-013** [[Knowledge Control Plane]] — Qdrant + Neo4j semantic indexing
- **CP-020** [[Financial Control Plane]] — Cost tracking by venture
- **CP-027** [[Infrastructure Control Plane]] — This CLI
- **CP-029** [[Observability]] — Grafana dashboards + Langfuse tracing

---

## How It Works

1. **Schema Definition** (`_CLI/schema.yaml`) — Maps all 50 domains, 20 layers, 6 control planes to CLI commands
2. **Code Generation** (CLI-Anything) — Generates executable `cb` CLI from schema
3. **Deployment** (GitHub Actions + CLI) — Chains commands for repeatable, auditable infrastructure-as-code
4. **Verification** (Built-in checks) — Each command verifies success before proceeding

---

## Troubleshooting

**OmniRoute not responding?**
```bash
curl http://100.87.214.70:20128/dashboard
# If 404 or timeout, check Docker: docker ps | grep omniroute
```

**Models not loading?**
```bash
curl http://100.87.214.70:11434/api/tags
# No models? Run: ollama pull qwen2.5-coder:14b
```

**Neo4j connection failed?**
```bash
cypher-shell -u neo4j -p changeme "RETURN 1;"
# If fails, verify database: docker ps | grep neo4j
```

---

## Next Steps

1. Run `cb infrastructure deploy --phase all` to start deployment
2. Monitor progress with `cb infrastructure status`
3. Access dashboards via URLs above
4. Follow [[DEPLOYMENT_PHASES.md|deployment roadmap]] for detailed timeline

---

**Generated by:** CLI-Anything  
**Last Updated:** 2026-09-04  
**Authority:** [[Infrastructure Control Plane]] (CP-027)
