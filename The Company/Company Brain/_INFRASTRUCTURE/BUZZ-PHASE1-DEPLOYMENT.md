[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

---
id: INFRA-BUZZ-DEPLOY-001
title: "Buzz Phase 1 Deployment Guide"
aliases: ["Buzz Deployment", "Buzz Phase 1", "Buzz Relay Setup"]
tags: ["infrastructure", "deployment", "buzz", "relay", "postgres", "redis", "minio"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[_INFRASTRUCTURE/BUZZ-INTEGRATION-PLAN|Buzz Integration Plan]] | [[_INFRASTRUCTURE/DEPLOYMENT_PHASES|Deployment Phases]] | [[56-ENGINEERING/README|56-ENGINEERING]]

# Buzz Phase 1 Deployment Guide

**Scope:** Deploy Buzz infrastructure (relay, PostgreSQL, Redis, MinIO) on [[_INFRASTRUCTURE/README|Mac Studio]]  
**Timeline:** Week 1 (Sep 6-12, 2026)  
**Effort:** ~7 hours  
**Authority:** CP-027 (Infrastructure Control Plane)

---

## PREREQUISITES

### System Check
```bash
# Verify [[_INFRASTRUCTURE/README|Mac Studio]] has space and resources
df -h [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/LaCie]]                    # ✅ Need 20GB free for Buzz data
docker --context macstudio ps -a       # ✅ Verify Docker daemon accessible
docker --context macstudio version     # ✅ Show Docker version
```

### Repository Access
```bash
# Have Buzz source ready
cd [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/LaCie]]/projects
ls -la | grep buzz                      # Check if buzz/ exists

# If not cloned yet:
# git clone https://github.com/block/buzz.git
```

---

## STEP 1: CLONE & EXPLORE (1 hour)

### 1a. Clone Buzz Repository
```bash
cd [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|/Volumes/LaCie]]/projects
git clone https://github.com/block/buzz.git buzz
cd buzz
git log --oneline -5                    # Show recent commits
```

### 1b. Explore Structure
```bash
# Key directories
ls -la | grep -E "^d" | awk '{print $NF}'  # List all directories

# Look for deployment files
find . -name "docker-compose*.yml" | head -10
find . -name "Dockerfile*" | head -10
find . -name "justfile" -o -name "Makefile"
cat Justfile | head -30                 # Show available commands (if exists)
```

### 1c. Verify Rust Toolchain (if building from source)
```bash
rustc --version                         # Show Rust version (if installed)
cargo --version
```

---

## STEP 2: DOCKER COMPOSE CONFIGURATION (2 hours)

### 2a. Locate compose file
```bash
cd /Users/acebless/Documents/The\ Company/Company\ Brain/_INFRASTRUCTURE
ls -la *compose* | head -10              # Check existing docker-compose files
```

### 2b. Create Buzz docker-compose.yml
```yaml
# File: /Volumes/LaCie/projects/buzz/docker-compose.local.yml
version: '3.8'

services:
  # Buzz Relay (main application)
  buzz-relay:
    image: buzz:latest  # or build from ./crates/relay
    build:
      context: .
      dockerfile: crates/relay/Dockerfile
    container_name: buzz_relay
    ports:
      - "8080:8080"  # WebSocket relay API
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/buzz
      REDIS_URL: redis://redis:6379/0
      S3_BUCKET: buzz-media
      S3_ENDPOINT: http://minio:9000
      S3_ACCESS_KEY_ID: minioadmin
      S3_SECRET_ACCESS_KEY: minioadmin
      RUST_LOG: info
    depends_on:
      - db
      - redis
      - minio
    volumes:
      - ./data/relay:/app/data
    networks:
      - buzz-network
    restart: unless-stopped

  # PostgreSQL (event log storage)
  db:
    image: postgres:16-alpine
    container_name: buzz_postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: buzz
    ports:
      - "5433:5432"  # Map to 5433 (avoid conflict with other postgres)
    volumes:
      - /Volumes/LaCie/buzz-data/postgres:/var/lib/postgresql/data
    networks:
      - buzz-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis (pub/sub for real-time events)
  redis:
    image: redis:7-alpine
    container_name: buzz_redis
    ports:
      - "6380:6379"  # Map to 6380 (avoid conflict with existing redis)
    volumes:
      - /Volumes/LaCie/buzz-data/redis:/data
    networks:
      - buzz-network
    restart: unless-stopped
    command: redis-server --appendonly yes

  # MinIO (S3-compatible object storage for Blossom protocol)
  minio:
    image: minio/minio:latest
    container_name: buzz_minio
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"    # S3 API
      - "9001:9001"    # Console UI
    volumes:
      - /Volumes/LaCie/buzz-data/minio:/minio_root/data
    networks:
      - buzz-network
    restart: unless-stopped
    command: server /minio_root/data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  # Buzz Web UI (optional, for UI access)
  buzz-web:
    image: buzz-web:latest  # or build from ./web
    build:
      context: ./web
      dockerfile: Dockerfile
    container_name: buzz_web
    ports:
      - "3000:3000"
    environment:
      REACT_APP_API_URL: http://100.87.214.70:8080
    depends_on:
      - buzz-relay
    networks:
      - buzz-network
    restart: unless-stopped

networks:
  buzz-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

### 2c. Create data directories
```bash
mkdir -p /Volumes/LaCie/buzz-data/{postgres,redis,minio,relay}
chmod -R 755 /Volumes/LaCie/buzz-data
ls -lah /Volumes/LaCie/buzz-data/
```

---

## STEP 3: BUILD (1-2 hours)

### 3a. Build Buzz Relay (if not using pre-built image)
```bash
cd /Volumes/LaCie/projects/buzz
docker --context macstudio build -t buzz:latest \
  -f crates/relay/Dockerfile .
# This will take 15-30 minutes for Rust compilation
```

### 3b. Build Web UI (optional)
```bash
cd /Volumes/LaCie/projects/buzz/web
docker --context macstudio build -t buzz-web:latest .
```

---

## STEP 4: DEPLOY (1.5 hours)

### 4a. Start Services
```bash
cd /Volumes/LaCie/projects/buzz

# Use the local docker-compose
docker --context macstudio compose -f docker-compose.local.yml up -d

# Verify all services started
docker --context macstudio compose -f docker-compose.local.yml ps
```

### 4b. Wait for Initialization
```bash
# Check PostgreSQL is ready
docker --context macstudio compose -f docker-compose.local.yml logs db | tail -20

# Check Buzz relay is running
docker --context macstudio compose -f docker-compose.local.yml logs buzz-relay | tail -20

# Check MinIO is ready
docker --context macstudio compose -f docker-compose.local.yml logs minio | tail -20
```

### 4c. Verify Connectivity
```bash
# Test Buzz relay (should return 200 OK)
curl -I http://100.87.214.70:8080/health

# Test PostgreSQL
psql -h 100.87.214.70 -p 5433 -U postgres -d buzz -c "SELECT version();"

# Test Redis
redis-cli -h 100.87.214.70 -p 6380 ping

# Test MinIO
curl -I http://100.87.214.70:9000/minio/health/live

# Test Web UI
curl -I http://100.87.214.70:3000/
```

---

## STEP 5: NETWORK INTEGRATION (1 hour)

### 5a. Update Tailscale DNS
```bash
# Add to Tailscale magic DNS (if using Tailscale ACL)
# buzz.macstudio.local → 100.87.214.70:8080
```

### 5b. Document in CLAUDE.md
```bash
# Update infrastructure table with Buzz services
```

### 5c. Integration with Existing Services
```bash
# Buzz should be able to reach:
# - Neo4j at bolt://100.87.214.70:7687
# - OmniRoute at http://100.87.214.70:20128
# - Qdrant at http://100.87.214.70:6333

# Test connectivity from Buzz container
docker --context macstudio exec buzz_relay \
  curl -I http://100.87.214.70:7474  # Neo4j
```

---

## STEP 6: INITIAL WORKSPACE SETUP (1 hour)

### 6a. Access Web UI
```
Browser: http://100.87.214.70:3000
```

### 6b. Create Workspace
```
- Workspace name: company-brain
- Visibility: Private
- Members: Add admin user
```

### 6c. Create Channels
```
#repo-classification     (for AGT-013 findings)
#repo-scoring           (for AGT-014 findings)
#repo-disposition       (for AGT-015 decisions)
#repo-adoption-pipeline (for AGT-017 progress)
#general                (for meta-discussions)
```

### 6d. Create Service Keys
```bash
# Generate Nostr keys for agents
# AGT-013 key: <key-for-classifier>
# AGT-014 key: <key-for-scorer>
# AGT-015 key: <key-for-disposition>
# AGT-017 key: <key-for-adoption>
# AGT-019 key: <key-for-sync-agent>

# Store in ~/.env.buzz or secure vault
export BUZZ_AGT013_KEY="..."
export BUZZ_AGT014_KEY="..."
export BUZZ_AGT015_KEY="..."
export BUZZ_AGT017_KEY="..."
export BUZZ_AGT019_KEY="..."
```

---

## VERIFICATION CHECKLIST

### Infrastructure ✅
- [ ] All 5 containers running (relay, postgres, redis, minio, web)
- [ ] Buzz relay responds to `/health`
- [ ] PostgreSQL accessible on :5433
- [ ] Redis accessible on :6380
- [ ] MinIO accessible on :9000

### Networking ✅
- [ ] Buzz relay reachable from Mac Air via Tailscale IP
- [ ] Curl to `http://100.87.214.70:8080/health` returns 200
- [ ] Can ping Neo4j from Buzz container
- [ ] Can reach OmniRoute from Buzz

### Web UI ✅
- [ ] Web UI accessible at `http://100.87.214.70:3000`
- [ ] Can log in
- [ ] Can create workspace
- [ ] Can create channels

### Data Persistence ✅
- [ ] PostgreSQL data in `/Volumes/LaCie/buzz-data/postgres/`
- [ ] Redis data in `/Volumes/LaCie/buzz-data/redis/`
- [ ] MinIO data in `/Volumes/LaCie/buzz-data/minio/`

---

## TROUBLESHOOTING

### "Failed to connect to database"
```bash
# Check PostgreSQL logs
docker --context macstudio logs buzz_postgres

# Verify DATABASE_URL env var is correct
docker --context macstudio exec buzz_relay printenv | grep DATABASE_URL

# Test direct connection
psql postgresql://postgres:postgres@buzz_postgres:5432/buzz
```

### "Redis connection refused"
```bash
# Check Redis logs
docker --context macstudio logs buzz_redis

# Test from relay container
docker --context macstudio exec buzz_relay redis-cli -h redis ping
```

### "MinIO bucket not found"
```bash
# Create initial buckets
docker --context macstudio exec buzz_minio \
  mc mb minio/buzz-media
```

### "Web UI won't load"
```bash
# Check web container logs
docker --context macstudio logs buzz_web

# Check relay is responding (web depends on relay API)
curl http://100.87.214.70:8080/health
```

---

## NEXT STEPS (Phase 2)

Once Phase 1 is complete:
1. Create MCP bridge tools (buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j)
2. Wire AGT-013/014/015 to publish to Buzz channels
3. Test first repo through full Buzz workflow
4. Create buzz-sync-agent (AGT-019) for event-to-Neo4j sync

---

**Status:** 🟡 Ready to begin  
**Estimated Hours:** 7 hours  
**Start Date:** Sep 6, 2026  
**Target Completion:** Sep 12, 2026  
