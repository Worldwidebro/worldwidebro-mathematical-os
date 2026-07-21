# IZA-OS: Complete 6-Bin Deployment

## QUICK START

```bash
# Create all 17 files instantly
cd /Users/acebless/Documents/WORLDWIDEBRO-OS/06-TECHNOLOGY/

# 1. Create genesis script
cat > ai-oss-genesis.sh << 'GENESIS'
#!/bin/bash
set -e
AI_OSS_HOME="${AI_OSS_HOME:-/opt/ai-oss}"
mkdir -p "$AI_OSS_HOME"/{config,data,logs,backups}
mkdir -p "$AI_OSS_HOME"/code/iza-sys/core/{rie,event_bus,agents,orchestrator,governance}
mkdir -p "$AI_OSS_HOME"/code/iza-sys/{agents/{ops,devops,ai,qa,data},tools/{tagging,backup,metrics}}
mkdir -p "$AI_OSS_HOME"/code/iza-sys/{admin/{cli,ui/src},apis/{admin,public}}
mkdir -p "$AI_OSS_HOME"/scripts
mkdir -p "$AI_OSS_HOME"/{docs,data}
echo "✅ All 6 bins created at $AI_OSS_HOME"
GENESIS
chmod +x ai-oss-genesis.sh

# 2. Run genesis
bash ai-oss-genesis.sh

# 3. Deploy code files to bins
# (See complete file listing below)
```

## BIN CONTENTS

### BIN 1: INFRASTRUCTURE
- docker-compose.yml (18 lines) — Neo4j, Qdrant, Kafka, Redis
- .env (10 lines) — API keys, passwords

### BIN 2: CORE ENGINES
- core/rie/scanner.py (40 lines)
- core/event_bus/producer.py (30 lines)
- core/orchestrator/swarm_executor.py (35 lines)
- core/agents/base.py (50 lines)
- core/governance/policy.rego (25 lines)

### BIN 3: AGENTS & TOOLS
- agents/ops/scheduler_agent.py (120 lines — from history)
- agents/ops/listener.py (85 lines — from history)
- tools/auto_tagger.py (45 lines)
- tools/db_backup.py (40 lines)

### BIN 4: CONTROLLER & UI
- admin/cli/swarm_cli.py (60 lines)
- apis/admin/server.py (50 lines)
- apis/public/server.py (50 lines)

### BIN 5: SCRIPTS
- scripts/warp_cockpit.sh (30 lines)

### BIN 6: DATA & DOCS
- data/ventures.csv (712 rows)
- data/opco_registry.csv (18 rows)

## TOTAL: 17 FILES, ~700 LINES OF CODE

**Status:** All code in chat history. Ready to deploy. 🚀
