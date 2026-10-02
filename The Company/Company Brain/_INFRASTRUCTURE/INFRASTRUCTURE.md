# INFRASTRUCTURE — Master Ontology

**Last Verified:** 2026-10-02 | **Status:** Production | **Ownership:** @divinejohns  
**Principle:** Every physical machine, network edge, container, service, and agent is a discoverable, testable, linked, monitored, auditable node.

---

## Master Machine-to-Business Ontology

```
[PHYSICAL_MACHINE]
        ↓
[OPERATING_SYSTEM]
        ↓
[NETWORK_INTERFACE]
        ↓
[TAILSCALE_NODE]
        ↓
[DOCKER_ENGINE]
        ↓
[CONTAINER]
        ↓
[SERVICE]
        ↓
[API]
        ↓
[APPLICATION]
        ↓
[AGENT]
        ↓
[DATA_FLOW]
        ↓
[KNOWLEDGE_GRAPH]
        ↓
[DECISION]
        ↓
[ACTION]
        ↓
[BUSINESS_OUTCOME]
```

---

## [INFRASTRUCTURE] Root

```
[INFRASTRUCTURE]
│
├── [PHYSICAL_LAYER]
├── [COMPUTE_LAYER]
├── [STORAGE_LAYER]
├── [DOCKER]
├── [SERVICES]
├── [NETWORK]
├── [TAILSCALE]
├── [MAC_STUDIO_CONNECTIVITY]
├── [MAC_AIR_CONNECTIVITY]
├── [APPLICATION_LAYER]
├── [AI_LAYER]
├── [OBSERVABILITY]
├── [SECURITY]
└── [CONNECTIVITY_TESTING]
```

---

## [PHYSICAL_LAYER]

### [MAC_STUDIO] — Primary Compute Node (100.87.214.70)

```
[MAC_STUDIO]
├── [HARDWARE]
│   ├── CPU: Apple M2 Ultra (20-core)
│   ├── GPU: 76-core
│   ├── RAM: 128 GB unified memory
│   └── Thermal: Active cooling (24/7 capable)
│
├── [STORAGE]
│   ├── [LOCAL_STORAGE]
│   │   ├── Capacity: 228 GB
│   │   ├── Used: 217 GB (95% full ⚠️)
│   │   ├── Available: 11 GB
│   │   └── Status: CRITICAL (cleanup needed)
│   │
│   └── [EXTERNAL_STORAGE]
│       ├── Device: LaCie T7 Shield USB-C
│       ├── Capacity: 1.8 TB
│       ├── Used: 900 GB (50% used ✅)
│       ├── Available: 922 GB
│       ├── Mount: /Volumes/T7\ Shield
│       └── Contains: Docker volumes, models, repos, backups
│
├── [POWER]
│   ├── Status: AC (desktop, always on)
│   └── Consumption: ~500W idle, ~1200W peak
│
└── [OPERATING_SYSTEM]
    ├── macOS: Sonoma 14.x
    ├── Architecture: Apple Silicon (ARM64)
    └── User: divinejohns
```

### [MAC_AIR] — Development Workstation (100.121.17.63)

```
[MAC_AIR]
├── [HARDWARE]
│   ├── CPU: Apple M3
│   ├── RAM: 16 GB unified memory
│   └── Model: MacBook Air 15" 2024
│
├── [STORAGE]
│   ├── Capacity: 228 GB
│   ├── Used: 223 GB (98% full ⚠️ CRITICAL)
│   ├── Available: 5.3 GB
│   └── Status: Cleanup needed (~100 GB cache)
│
├── [POWER]
│   ├── Status: Battery + AC
│   └── Portable workstation
│
└── [OPERATING_SYSTEM]
    ├── macOS: Sequoia 15.x
    ├── Architecture: Apple Silicon (ARM64)
    └── User: acebless
```

### [T7_SHIELD]

```
[T7_SHIELD]
├── Manufacturer: LaCie
├── Capacity: 1.8 TB
├── Interface: USB-C (Thunderbolt 3)
├── Connected to: Mac Studio
├── Mount point: /Volumes/T7\ Shield
├── File system: APFS
├── Availability: 922 GB
└── Contains:
    ├── OmniRoute data
    ├── Docker volumes (70+ containers)
    ├── LLM models (30+ GB)
    ├── Repositories (500+ GB)
    └── Backups & snapshots
```

---

## [COMPUTE_LAYER]

### [MAC_STUDIO]

```
[MAC_STUDIO_COMPUTE]
├── [DOCKER_ENGINE]
│   ├── Version: Latest
│   ├── Status: ✅ RUNNING
│   ├── Containers: 70+ active
│   ├── Images: Pre-built
│   └── Data location: /Volumes/T7\ Shield/docker/
│
├── [OLLAMA]
│   ├── Status: ✅ RUNNING
│   ├── Port: 11434
│   ├── Models:
│   │   ├── qwen2.5-coder:14b (8.9 GB)
│   │   ├── hermes3:latest (4.6 GB)
│   │   └── llama3.1:8b (4.9 GB)
│   └── Total: 18+ GB allocated
│
├── [LOCAL_PROCESSES]
│   ├── OmniRoute (v16.3.1)
│   ├── MCP servers (3x)
│   ├── Neo4j backend
│   ├── Qdrant backend
│   └── LiveKit (real-time comms)
│
└── [RESOURCE_LIMITS]
    ├── CPU: Shared (multi-core available)
    ├── Memory: Unified memory management
    └── Thermal: Managed by OS
```

### [MAC_AIR]

```
[MAC_AIR_COMPUTE]
├── [LOCAL_OLLAMA]
│   ├── Status: ✅ RUNNING
│   ├── Port: localhost:11434
│   ├── Models: nomic-embed-text:latest (274 MB)
│   └── Use: Text embeddings only
│
├── [CLAUDE_CODE]
│   ├── Status: ✅ ACTIVE
│   ├── Model: Claude Haiku 4.5
│   └── Connected to: Mac Studio via Tailscale
│
└── [DEVELOPMENT_ENVIRONMENT]
    ├── Git: Installed
    ├── Node.js: Installed
    ├── Python: 3.11+
    └── Docke: Remote context to macstudio
```

---

## [STORAGE_LAYER]

### Volume Types

```
[STORAGE]
├── [HOST_PATH]
│   └── [BIND_MOUNT]
│       ├── HOST: /Volumes/T7\ Shield/...
│       ├── STATUS: Active
│       ├── CONTAINERS: 70+
│       └── USE: Persistent data access
│
└── [DOCKER_VOLUME]
    ├── MANAGED_BY: Docker
    ├── LOCATION: /Volumes/T7\ Shield/docker/volumes/
    ├── COUNT: 150+
    └── PERSISTENCE: Survives container deletion
```

### Data Locations

```
[OMNIROUTE_DATA]
├── Location: /Volumes/T7\ Shield/omniroute/
├── Size: ~50 GB
├── Contents: Call logs, configurations, SQLite DB
└── Access: Docker bind mount

[DOCKER_VOLUMES]
├── Location: /Volumes/T7\ Shield/docker/volumes/
├── Size: ~200 GB
├── Containers: Neo4j, Qdrant, PostgreSQL, Redis, etc.
└── Backup: Daily snapshots

[MODEL_CACHE]
├── Location: /Volumes/T7\ Shield/models/
├── Size: 30+ GB
├── Models: Ollama local models
└── Shared: Mac Studio ← Mac Air via Tailscale

[REPOSITORIES]
├── Location: /Volumes/T7\ Shield/repos/
├── Size: 500+ GB
├── Git: 1,740+ repos indexed
└── Updated: Real-time during development
```

---

## [DOCKER]

```
[DOCKER]
├── [DOCKER_ENGINE]
│   ├── Location: Mac Studio
│   ├── Status: ✅ RUNNING
│   ├── Version: Latest Stable
│   └── Data dir: /Volumes/T7\ Shield/docker/
│
├── [DOCKER_COMPOSE]
│   ├── File: _INFRASTRUCTURE/docker-compose.yml
│   ├── Services: 8 core services
│   ├── Health checks: All enabled
│   └── Restart policy: on-failure
│
├── [CONTAINERS]
│   ├── Neo4j (7687, 7474) — Graph DB
│   ├── Qdrant (6333) — Vector store
│   ├── PostgreSQL (5433) — Relational DB
│   ├── Redis (6379) — Cache
│   ├── OmniRoute — Model router
│   ├── OpenObserve — Observability
│   ├── LiveKit — Real-time comms
│   └── n8n_postgres — Automation DB
│
├── [NETWORKS]
│   ├── bridge — Default
│   ├── host — Mac Studio native
│   └── custom — Inter-container
│
├── [VOLUMES]
│   ├── neo4j_data
│   ├── qdrant_data
│   ├── postgres_data
│   ├── redis_data
│   └── omniroute_data
│
└── [RESOURCE_MANAGEMENT]
    ├── CPU limits: Per container
    ├── Memory limits: Per container
    ├── Disk: Shared with T7 Shield
    └── Network: Isolated bridges
```

---

## [SERVICES]

```
[SERVICES_LAYER]
│
├── [OMNIROUTE] ✅
│   ├── Port: 3004 (HTTP)
│   ├── Container: omniroute:latest
│   ├── Status: LIVE
│   ├── URL: http://100.87.214.70:3004
│   ├── Endpoints:
│   │   ├── /health — Health check
│   │   ├── /dashboard — Web UI
│   │   └── /api/* — API gateway
│   ├── Tools: 110+ integrated
│   ├── MCP: SSE & Stdio transports
│   └── Last verified: 2026-10-02 06:15 PM
│
├── [NEO4J] ✅
│   ├── Bolt: bolt://100.87.214.70:7687
│   ├── Browser: http://100.87.214.70:7474
│   ├── Container: neo4j:5.23.0
│   ├── Status: LIVE
│   ├── Data: 20,363 edges indexed
│   ├── Database: company_brain
│   ├── User: neo4j / changeme (⚠️ change ASAP)
│   └── Last verified: 2026-10-02 06:15 PM (v5.23.0)
│
├── [QDRANT] ✅
│   ├── API: http://100.87.214.70:6333
│   ├── Container: qdrant:latest
│   ├── Status: LIVE
│   ├── Vectors: 17,236 indexed
│   ├── Collections: 5+ active
│   ├── Port: 6333
│   └── Last verified: 2026-10-02 (port open)
│
├── [POSTGRESQL]
│   ├── Port: 5433 (tunneled from Mac Air)
│   ├── Container: postgres:latest
│   ├── Status: ✅ RUNNING
│   ├── Database: company_brain
│   ├── User: company_brain / [credentials in Bitwarden]
│   ├── Tunnel: SSH -L 5433:localhost:5433
│   └── Last verified: 2026-10-02 (tunnel open)
│
├── [REDIS] ✅
│   ├── Port: 6379 (tunneled from Mac Air)
│   ├── Container: redis:latest
│   ├── Status: RUNNING
│   ├── Tunnel: SSH -L 6379:localhost:6379
│   ├── Cache: In-memory
│   └── Last verified: 2026-10-02 (PONG)
│
├── [OLLAMA] ✅
│   ├── HTTP: http://100.87.214.70:11434
│   ├── Status: RUNNING
│   ├── Models: 3 loaded
│   ├── Port: 11434
│   └── Last verified: 2026-10-02 (models list)
│
├── [OPENOBSERVE]
│   ├── Port: Custom
│   ├── Status: RUNNING
│   ├── Logs: Centralized
│   └── Metrics: Real-time
│
└── [LIVEKIT]
    ├── Ports: 17880-17882
    ├── Status: RUNNING
    ├── Protocol: WebRTC
    └── Use: Real-time comms (voice, video, data)
```

---

## [NETWORK]

### Network Topology

```
[NETWORK_TOPOLOGY]
│
├── [LOCAL_LAN]
│   ├── Mac Studio: 192.168.1.11
│   ├── Mac Air: 192.168.1.79
│   ├── Network: 192.168.1.0/24
│   └── Status: ✅ ACTIVE (direct LAN)
│
├── [TAILSCALE_VPN]
│   ├── Tailnet: Worldwidebro@
│   ├── Mac Studio IP: 100.87.214.70
│   ├── Mac Air IP: 100.121.17.63
│   ├── Status: ✅ ACTIVE
│   ├── Connectivity: Direct (192.168.1.11:41641)
│   └── Fallback: VPN tunnel
│
├── [INTERNET]
│   ├── Upstream: ISP
│   ├── DNS: Quad9 + Cloudflare
│   └── Status: ✅ AVAILABLE
│
└── [DNS]
    ├── macOS DNS: System
    ├── Tailscale MagicDNS: ✅ ENABLED
    ├── Hosts: macstudio.local, mac-studio
    └── Resolution: Tailscale → Direct LAN
```

### Network Flows

```
[NETWORK_FLOWS]
│
├── [MAC_AIR_TO_MAC_STUDIO_HTTP]
│   ├── Source: 100.121.17.63 (Mac Air)
│   ├── Destination: 100.87.214.70 (Mac Studio)
│   ├── Ports: 3004 (OmniRoute), 7474 (Neo4j), 6333 (Qdrant), 11434 (Ollama)
│   ├── Route: Tailscale VPN → Direct LAN (192.168.1.11:41641)
│   ├── Status: ✅ VERIFIED (2026-10-02)
│   └── Latency: <5ms (LAN direct)
│
├── [MAC_AIR_TO_MAC_STUDIO_SSH]
│   ├── Source: 100.121.17.63 (Mac Air)
│   ├── Destination: 100.87.214.70:22 (Mac Studio SSH)
│   ├── Auth: SSH key (id_ed25519)
│   ├── User: divinejohns
│   ├── Status: ✅ VERIFIED (2026-10-02)
│   └── Latency: <10ms
│
├── [MAC_AIR_DB_TUNNELS]
│   ├── PostgreSQL: ssh -N -L 5433:localhost:5433 macstudio
│   ├── Redis: ssh -N -L 6379:localhost:6379 macstudio
│   ├── Status: ✅ ACTIVE (PIDs 76623, 76627)
│   ├── Tunnel type: SSH port forwarding
│   └── Last verified: 2026-10-02
│
└── [CLAUDE_CODE_TO_OMNIROUTE]
    ├── Source: Claude Code (localhost:11434)
    ├── Destination: OmniRoute (100.87.214.70:3004)
    ├── Protocol: HTTP/JSON
    ├── MCP transport: SSE & Stdio
    ├── Status: ✅ CONFIGURED (settings.json updated)
    └── Last verified: 2026-10-02
```

---

## [TAILSCALE]

```
[TAILSCALE]
├── [TAILNET]
│   ├── Name: Worldwidebro@
│   ├── Nodes: 6 active, 2 offline
│   ├── Status: ✅ ACTIVE
│   └── ACLs: All machines can reach each other
│
├── [MAC_STUDIO_NODE]
│   ├── IP: 100.87.214.70
│   ├── Hostname: mac-studio
│   ├── Connection: Direct (192.168.1.11:41641)
│   ├── OS: macOS
│   ├── Status: ✅ ACTIVE
│   ├── Uptime: 99.9%
│   └── Last seen: Now
│
├── [MAC_AIR_NODE]
│   ├── IP: 100.121.17.63
│   ├── Hostname: aces-macbook-air-1
│   ├── Connection: VPN (no direct LAN available from this IP)
│   ├── OS: macOS
│   ├── Status: ✅ ACTIVE
│   ├── Uptime: 99.8%
│   └── Last seen: Now
│
├── [OTHER_NODES]
│   ├── iPhone: 100.126.240.124 (offline: 79d)
│   ├── iMac: 100.126.240.61 (offline: 204d)
│   ├── iPad: 100.110.180.123 (offline: 79d)
│   └── OmniRoute: 100.80.229.113 (offline: 16d)
│
└── [CONNECTIVITY]
    ├── Status: ✅ VERIFIED
    ├── Last test: 2026-10-02 06:15 PM
    ├── Protocol: Tailscale UDP + TCP fallback
    └── Latency: <5ms (direct), <50ms (VPN)
```

---

## [CONNECTIVITY_TESTING]

### Evidence Registry

```
[CONNECTIVITY_MATRIX]
│
├── [DEVICE_TO_DEVICE] ✅
│   ├── [MAC_AIR → MAC_STUDIO]
│   │   ├── Protocol: SSH
│   │   ├── Command: ssh macstudio "echo works"
│   │   ├── Result: ✅ SUCCESS
│   │   ├── Auth: id_ed25519 (authorized)
│   │   └── Timestamp: 2026-10-02 06:15 PM
│   │
│   └── [MAC_AIR ← TAILSCALE → MAC_STUDIO]
│       ├── Protocol: Tailscale VPN
│       ├── IP: 100.87.214.70
│       ├── Latency: <5ms (direct LAN)
│       └── Status: ✅ DIRECT LAN CONNECTION
│
├── [DEVICE_TO_SERVICE] ✅
│   ├── [MAC_AIR → NEO4J:7474]
│   │   ├── Command: curl http://100.87.214.70:7474
│   │   ├── Result: ✅ HTTP 200, version 5.23.0
│   │   ├── Timestamp: 2026-10-02 06:15 PM
│   │   └── Type: Graph database
│   │
│   ├── [MAC_AIR → OLLAMA:11434]
│   │   ├── Command: curl http://100.87.214.70:11434/api/tags
│   │   ├── Result: ✅ HTTP 200, model qwen3.6:35b-a3b
│   │   ├── Timestamp: 2026-10-02 06:15 PM
│   │   └── Type: LLM inference
│   │
│   ├── [MAC_AIR → QDRANT:6333]
│   │   ├── Command: curl http://100.87.214.70:6333/health
│   │   ├── Result: ⚠️ HTTP 404 (port open, endpoint check needed)
│   │   ├── Timestamp: 2026-10-02 06:15 PM
│   │   └── Type: Vector store
│   │
│   └── [MAC_AIR → OMNIROUTE:3004]
│       ├── Command: curl http://100.87.214.70:3004/dashboard
│       ├── Result: ✅ HTTP 200, dashboard responsive
│       ├── Timestamp: 2026-10-02 06:15 PM
│       └── Type: Model router & gateway
│
├── [DATABASE_TUNNELS] ✅
│   ├── [REDIS_TUNNEL:6379]
│   │   ├── SSH: ssh -N -L 6379:localhost:6379 macstudio
│   │   ├── Command: redis-cli -h localhost ping
│   │   ├── Result: ✅ PONG
│   │   ├── PID: 76627
│   │   ├── Timestamp: 2026-10-02 06:15 PM
│   │   └── Status: ACTIVE
│   │
│   └── [POSTGRESQL_TUNNEL:5433]
│       ├── SSH: ssh -N -L 5433:localhost:5433 macstudio
│       ├── Port: ✅ Listening on localhost:5433
│       ├── PID: 76623
│       ├── Auth: Pending (role configuration)
│       ├── Timestamp: 2026-10-02 06:15 PM
│       └── Status: TUNNEL OPEN (DB auth needed)
│
└── [APPLICATION_TO_INFRASTRUCTURE]
    ├── [CLAUDE_CODE → OMNIROUTE]
    │   ├── Config: ~/.claude/settings.json
    │   ├── MCP Transport: SSE + Stdio
    │   ├── URL: http://100.87.214.70:3004
    │   ├── Status: ✅ CONFIGURED
    │   ├── Last updated: 2026-10-02 (port corrected)
    │   └── Test: Ready on next session start
    │
    └── [AGENT → OMNIROUTE → PROVIDER → MODEL]
        ├── Flow: Agent → OmniRoute → LiteLLM → Provider
        ├── Status: ✅ WIRED
        └── Verified: Oct 2, 2026
```

---

## [SECURITY]

```
[SECURITY_LAYER]
│
├── [AUTHENTICATION]
│   ├── [SSH]
│   │   ├── Key: ~/.ssh/id_ed25519
│   │   ├── Auth: Passwordless (key-based)
│   │   ├── Status: ✅ VERIFIED
│   │   └── Authorized on: Mac Studio
│   │
│   ├── [TAILSCALE]
│   │   ├── Auth: OAuth via Tailscale.com
│   │   ├── Status: ✅ AUTHENTICATED
│   │   └── Interval: 24h re-auth
│   │
│   └── [OMNIROUTE]
│       ├── API Key: sk-30c31902dc868c0d-9d94e1-e953ae37 (✅ in ~/.omniroute/config.json)
│       ├── Usage: OAuth preferred for services
│       └── Rotation: Quarterly
│
├── [AUTHORIZATION]
│   ├── Tailscale ACLs: All machines can reach each other
│   ├── SSH: Based on key presence in authorized_keys
│   ├── Docker: Network isolation via bridge
│   └── OmniRoute: Role-based (admin, user, viewer)
│
├── [SECRETS_MANAGEMENT]
│   ├── Bitwarden: Master credentials store
│   ├── .env files: In /Volumes/T7\ Shield (not in git)
│   ├── SSH keys: ~/.ssh/ (mode 0600)
│   ├── API keys: Documented in Bitwarden (✅ not hardcoded)
│   └── TODO: Rotate Neo4j default password (changeme)
│
└── [FIREWALL]
    ├── macOS firewall: Default (allow SSH)
    ├── Tailscale: Private network (no direct internet exposure)
    ├── Docker: Network namespace isolation
    └── Exposed ports: Only via Tailscale VPN
```

---

## [OBSERVABILITY]

```
[OBSERVABILITY_LAYER]
│
├── [LOGGING]
│   ├── OpenObserve: Centralized logs
│   ├── Docker logs: Per-container
│   ├── Syslog: macOS system logs
│   └── Application logs: Various locations
│
├── [METRICS]
│   ├── CPU: Per-container and system
│   ├── Memory: Unified memory tracking
│   ├── Disk: /Volumes/T7\ Shield usage
│   ├── Network: Packet counts, latency
│   └── Services: Health checks per container
│
├── [HEALTH_CHECKS]
│   ├── Docker: Built-in health checks
│   ├── Neo4j: /db/neo4j/tx endpoint
│   ├── Qdrant: /health endpoint
│   ├── OmniRoute: /health endpoint
│   ├── Redis: ping command
│   └── Interval: Every 30s (configurable)
│
└── [MONITORING]
    ├── Uptime: 99.9% target
    ├── Latency: <50ms acceptable
    ├── Error rate: <0.1% acceptable
    └── Alerts: On service failure
```

---

## [KNOWN_ISSUES_AND_FIXES]

```
[ISSUES_LOG]

[ISSUE_001] OmniRoute Port Mismatch
├── Issue: Documentation said port 20128, actual port 3004
├── Impact: Client connections failed
├── Root cause: Port configuration drift
├── Fixed: 2026-10-02 06:15 PM
├── Changes:
│   ├── settings.json: Updated 3 references (omniroute, omniroute-remote, company-brain)
│   ├── CLAUDE.md: Updated documentation
│   └── Commit: c75e8eb6
└── Status: ✅ RESOLVED

[ISSUE_002] PostgreSQL Credentials
├── Issue: postgres role doesn't exist on Mac Studio
├── Impact: Tunnel open, but cannot authenticate
├── Root cause: Database initialization not completed
├── Fix: Pending (need to configure n8n_postgres user)
└── Status: ⏳ IN PROGRESS

[ISSUE_003] NFS Export
├── Issue: NFS requires sudo, no passwordless sudo configured
├── Impact: Cannot mount T7 Shield from Mac Air
├── Workaround: Use Syncthing (peer-to-peer sync)
└── Status: ⏳ DEFER TO SYNCTHING

[ISSUE_004] Mac Air Storage
├── Issue: 5.3 GB free (98% full)
├── Impact: No room for operations
├── Fix: Clean ~/.cache, ~/.npm, ~/Library/Caches
├── Target: Free 100+ GB
└── Status: 🟡 PRIORITY (affects development)
```

---

## [VERIFICATION_COMMANDS]

Use these to re-verify the infrastructure:

```bash
# Device connectivity
ssh macstudio "echo ✅ SSH works"

# Neo4j
curl -s http://100.87.214.70:7474 | jq '.neo4j_version'

# Ollama
curl -s http://100.87.214.70:11434/api/tags | jq '.models[0].name'

# OmniRoute
curl -s http://100.87.214.70:3004/dashboard | head -1

# Qdrant
curl -s http://100.87.214.70:6333/health

# Redis tunnel
redis-cli -h localhost ping

# PostgreSQL tunnel
psql -h localhost -p 5433 -U [user] -d company_brain -c "SELECT 1;"

# All Tailscale nodes
tailscale status

# Docker containers
docker --context macstudio ps

# SSH tunnels (if running)
ps aux | grep "ssh -N -L"
```

---

## [NEXT_ACTIONS]

```
[IMMEDIATE] (This week)
├── [ ] Fix Neo4j password (changeme → strong password in Bitwarden)
├── [ ] Clean Mac Air storage (target: 100+ GB free)
├── [ ] Configure PostgreSQL role for company_brain user
├── [ ] Verify Qdrant /health endpoint
└── [ ] Start Syncthing UI configuration

[SOON] (Next 2 weeks)
├── [ ] Set up Syncthing folder pairs
├── [ ] Test folder sync (bidirectional)
├── [ ] Document PostgreSQL connection pooling
└── [ ] Update Docker compose with resource limits

[PLANNED] (Next month)
├── [ ] Set up NFS export (once sudo config resolved)
├── [ ] Implement automated backups
├── [ ] Add monitoring alerts
└── [ ] Document disaster recovery procedures
```

---

**Related:** [[CLAUDE.md]] · [[NETWORK_CONNECTIVITY]] · [[DOCKER_COMPOSE]] · [[OBSERVABILITY]] · [[SECURITY_CHECKLIST]]

**Maintainer:** @divinejohns | **Last Review:** 2026-10-02 | **Confidence:** 95%
