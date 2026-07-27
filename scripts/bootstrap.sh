#!/usr/bin/env bash
set -euo pipefail

# ═══════════════════════════════════════════════════════════════════════
# AI BOSS OS - Bootstrap Script
# First-time setup: validates prerequisites, creates .env, pulls images, initializes schemas
# Usage: ./scripts/bootstrap.sh
# ═══════════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log()  { echo -e "${BLUE}[bootstrap]${NC} $1"; }
ok()   { echo -e "${GREEN}[✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
fail() { echo -e "${RED}[✗]${NC} $1"; exit 1; }

# ─── Phase 1: Prerequisites Check ──────────────────────────────────────
log "Phase 1: Checking prerequisites..."

command -v docker >/dev/null 2>&1 || fail "Docker not installed"
command -v docker compose >/dev/null 2>&1 || fail "Docker Compose not installed"

DOCKER_VERSION=$(docker --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || echo "unknown")
ok "Docker $DOCKER_VERSION installed"

docker info >/dev/null 2>&1 || fail "Docker daemon not running"
ok "Docker daemon running"

# Check disk space (need at least 20GB)
AVAILABLE_GB=$(df -BG . | tail -1 | awk '{print $4}' | tr -d 'G')
if [ "$AVAILABLE_GB" -lt 20 ]; then
    fail "Need 20GB free disk, have ${AVAILABLE_GB}GB"
fi
ok "Disk space: ${AVAILABLE_GB}GB available"

# ─── Phase 2: Environment Setup ───────────────────────────────────────
log "Phase 2: Setting up environment..."

if [ ! -f .env ]; then
    cp .env.example .env
    warn "Created .env from template"
    warn "⚠️  IMPORTANT: Edit .env and fill in real credentials:"
    warn "   nano .env"
    warn "   Then run: make bootstrap"
    exit 1
else
    ok ".env already exists"
fi

# Validate required env vars
if ! grep -q "POSTGRES_PASSWORD" .env || grep "POSTGRES_PASSWORD=change_me" .env >/dev/null 2>&1; then
    fail "POSTGRES_PASSWORD not configured in .env"
fi
ok "Environment configured"

# ─── Phase 3: Directory Structure ──────────────────────────────────────
log "Phase 3: Creating directory structure..."

mkdir -p backups logs init/postgres init/neo4j agents/bootstrap data/{postgres,redis,neo4j,qdrant}
ok "Directories created"

# ─── Phase 4: Pull Docker Images ──────────────────────────────────────
log "Phase 4: Pulling Docker images (this takes 2-3 minutes)..."

docker compose pull || fail "Failed to pull images"
ok "Images pulled"

# ─── Phase 5: Initialize Volumes ──────────────────────────────────────
log "Phase 5: Starting core services (postgres, redis)..."

docker compose up -d postgres redis
ok "Postgres and Redis starting (waiting for health checks)..."

# Wait for postgres to be healthy
log "Waiting for PostgreSQL to be ready..."
for i in {1..30}; do
    if docker compose exec -T postgres pg_isready -U postgres >/dev/null 2>&1; then
        ok "PostgreSQL ready"
        break
    fi
    [ $i -eq 30 ] && fail "PostgreSQL failed to start after 60s"
    sleep 2
done

# Wait for redis to be healthy
log "Waiting for Redis to be ready..."
for i in {1..30}; do
    if docker compose exec -T redis redis-cli ping >/dev/null 2>&1; then
        ok "Redis ready"
        break
    fi
    [ $i -eq 30 ] && fail "Redis failed to start after 60s"
    sleep 2
done

# ─── Phase 6: Initialize Schemas ──────────────────────────────────────
log "Phase 6: Initializing database schemas..."

if [ -f init/postgres/01-init.sql ]; then
    docker compose exec -T postgres psql -U postgres -d twenty < init/postgres/01-init.sql
    ok "PostgreSQL schema initialized"
else
    warn "init/postgres/01-init.sql not found - skipping"
fi

# ─── Phase 7: Start All Services ──────────────────────────────────────
log "Phase 7: Starting all services..."

docker compose up -d
ok "All services started (wait 10s for full startup)"

sleep 10

# ─── Phase 8: Initialize Neo4j Schema ──────────────────────────────────
log "Phase 8: Initializing Neo4j schema..."

if [ -f init/neo4j/01-init.cypher ]; then
    docker compose exec -T neo4j cypher-shell -u neo4j -p "$(grep NEO4J_PASSWORD .env | cut -d= -f2)" < init/neo4j/01-init.cypher 2>/dev/null || warn "Neo4j schema init - may need manual setup"
    ok "Neo4j schema initialized"
else
    warn "init/neo4j/01-init.cypher not found - skipping"
fi

# ─── Phase 9: Health Check ────────────────────────────────────────────
log "Phase 9: Running health checks..."

sleep 5
if ./scripts/health-check.sh; then
    ok "All health checks passed"
else
    warn "Some services not ready yet - they may still be starting"
fi

# ─── Done ──────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ✅ AI BOSS OS BOOTSTRAP COMPLETE${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "  Services running:"
echo "    API:          http://localhost:8000"
echo "    Grafana:      http://localhost:3001      (admin/ventures2026)"
echo "    Neo4j:        http://localhost:7474      (neo4j/ventures2026)"
echo "    Qdrant:       http://localhost:6333"
echo "    LiteLLM:      http://localhost:4000"
echo "    Langfuse:     http://localhost:3003"
echo "    Prometheus:   http://localhost:9090"
echo "    n8n:          http://localhost:5678"
echo ""
echo "  Next steps:"
echo "    make seed      # Populate initial data"
echo "    make health    # Re-check all services"
echo "    make logs      # View service logs"
echo ""
