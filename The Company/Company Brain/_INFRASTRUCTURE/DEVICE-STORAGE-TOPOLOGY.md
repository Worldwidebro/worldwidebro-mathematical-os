[[STARTHERE]] | [[REALITY]] | [[START-HERE-INFRASTRUCTURE]] | [[REPOSITORY-INTELLIGENCE-SYSTEM]] | [[OMNIROUTE-STATUS]]

# Device & Storage Topology — Physical & Virtual Architecture

**Authority:** CP-027 [[Infrastructure Control Plane|56-INFRASTRUCTURE]]

**Purpose:** Document the complete physical device network, storage mounting strategy, and Tailscale mesh topology that underpins the Company Brain.

---

## 1. PHYSICAL DEVICES (Tailscale Mesh)

### Mac Studio M4 Max (Primary Brain Node)
```
Device ID:       mac-studio
Tailscale IP:    100.87.214.70
Local Network:   192.168.1.11
Hostname:        mac-studio.tailba9617.ts.net
CPU:             12-core M4 Max
Memory:          36GB unified
Internal SSD:    512GB (system + work)
Status:          ✅ ONLINE (4+ days uptime)
Role:            Primary inference server + database host
SSH User:        acebless
SSH:             ssh macstudio (alias via Tailscale)
```

**Running services (verified 2026-09-06):**
- OmniRoute daemon (`:20128`)
- Neo4j Community Edition (`:7687`, `:7474`)
- Qdrant vector database (`:6333`)
- PostgreSQL 16 (`:5433`)
- Redis (`:6379`)
- Ollama LLM runtime (`:11434`)
- exo MLX inference (`:52415`)
- Langfuse tracing (`:3003`)
- OpenObserve observability (`:5080`)

---

### MacBook Air M-Series (Mobile Engineering Node)
```
Device ID:       macbook-air
Tailscale IP:    100.121.17.63
Local Network:   192.168.1.xxx
Hostname:        macbook-air.tailba9617.ts.net
CPU:             8-core M-series
Memory:          16GB unified
Internal SSD:    228GB
Status:          ✅ ONLINE
Role:            Secondary inference agent + development
SSH User:        acebless
SSH:             ssh macbookair (alias via Tailscale)

# Can SSH from Mac Studio to MacBook Air:
ssh acebless@100.121.17.63
# or
ssh acebless@macbook-air.tailba9617.ts.net
```

**Role:** 
- Local development (code editing, testing)
- Secondary model inference (when Mac Studio is loaded)
- Portable access to Company Brain systems

---

### Tailscale Network Configuration

```yaml
Tailscale Namespace: Worldwidebro@

Devices:
  mac-studio:      100.87.214.70   (always-on)
  macbook-air:     100.121.17.63   (when powered on)
  
DNS:
  Base:            ts.net (.ts.net is Tailscale's DNS)
  Namespace DNS:   tailba9617.ts.net
  
VPN:
  Type:            WireGuard (encrypted mesh)
  Encryption:      End-to-end
  
Access Control:
  - Mac Studio ↔ Mac Air: bidirectional (unrestricted)
  - Port access: All services on 100.87.214.70 reachable from 100.121.17.63

Network Commands:
  # List all Tailscale devices
  tailscale status
  
  # Get current device info
  tailscale ip -4
  
  # SSH via Tailscale (from any device)
  ssh acebless@macstudio    # Resolves to 100.87.214.70
  ssh acebless@macbookair   # Resolves to 100.121.17.63
```

---

## 2. STORAGE ARCHITECTURE

### Mac Studio Storage

```
/Volumes/LaCie (4TB external, mounted via USB-C)
├── repositories/           # Repository Intelligence System (Phase 7)
│   ├── raw/               # Phase 1: Raw GitHub ingestion (904 repos)
│   ├── normalized/        # Phase 2: Deduplicated (~880-900 valid)
│   ├── enriched/          # Phase 3: Deep metadata per repo
│   ├── classified/        # Phase 4: Classified by capability
│   ├── scored/            # Phase 5: Scored on 10 dimensions
│   ├── dispositioned/     # Phase 6: ADOPT/INTEGRATE/FORK decisions
│   ├── adoption/          # Phase 8: Adoption pipeline tracking
│   └── metadata/          # Canonical registries
│       ├── REPOSITORY_INTELLIGENCE_REGISTRY.yaml
│       ├── CAPABILITY_DEPENDENCY_MAP.yaml
│       ├── TECHNOLOGY_RADAR.yaml
│       └── DO_NOT_BUILD.yaml
│
├── databases/             # Persistent database storage
│   ├── neo4j/            # Neo4j data directory (20,363 edges)
│   ├── qdrant/           # Qdrant vector store (17,236 vectors)
│   ├── postgres/         # PostgreSQL data
│   └── redis/            # Redis persistence
│
├── mirrors/              # Local mirrors of critical repos (optional)
│   ├── omniroute/
│   ├── exo/
│   ├── ollama/
│   └── ...
│
├── config/               # Mounted configuration files
│   ├── litellm-config.yaml
│   ├── omniroute-config.json
│   └── docker-compose.yml
│
├── exports/              # Data exports for analysis
│   ├── venture-data.json
│   ├── capability-matrix.csv
│   └── venture-readiness.csv
│
└── backups/              # Weekly backups
    ├── neo4j-backup-2026-09-06.tar.gz
    ├── qdrant-backup-2026-09-06.tar.gz
    └── postgres-backup-2026-09-06.sql.gz
```

**Mount verification (Mac Studio):**
```bash
# Check LaCie mount
df -h | grep LaCie
# Should show: /Volumes/LaCie ... 4TB

# Verify mounted path
ls -la /Volumes/LaCie/repositories/
# Should list: raw/, normalized/, enriched/, classified/, scored/, ...

# Verify Docker can access it (if using Docker)
docker --context macstudio run -v /Volumes/LaCie:/data alpine ls /data/repositories/
```

---

### MacBook Air Storage

```
/Volumes/T7 Shield (2TB external, mounted via USB-C)
├── software-factory/      # OmniRoute source code, forks, experimental
│   ├── repositories/      # Cloned repos for development
│   ├── OmniRoute/        # OmniRoute source (bin/omniroute.mjs, bin/mcp-server.mjs)
│   ├── forks/            # Personal forks of external projects
│   └── experimental/      # Experiments before promoting to LaCie
│
├── working-capabilities/ # Active development on capabilities
│   ├── agents/
│   ├── models/
│   └── tools/
│
├── local-mirrors/        # Quick-access mirrors (subset of LaCie)
│   └── critical-repos/
│
└── backups/             # Local backups (synced from LaCie weekly)
    └── ...
```

**Mount verification (Mac Air):**
```bash
# Check T7 Shield mount
df -h | grep "T7 Shield" 
# or
df -h | grep Volumes
# Should show /Volumes/T7\ Shield

# Verify mounted path
ls -la /Volumes/T7\ Shield/
# Should list: software-factory/, working-capabilities/, local-mirrors/, ...
```

---

## 3. CROSS-DEVICE ACCESS PATTERNS

### Mac Studio → LaCie (Local Access)

```bash
# Direct filesystem access (fastest)
ls /Volumes/LaCie/repositories/raw/
cat /Volumes/LaCie/metadata/REPOSITORY_INTELLIGENCE_REGISTRY.yaml

# Docker access (if containerized)
docker run -v /Volumes/LaCie:/data myimage bash -c "ls /data/repositories/"
```

**Performance:** ~100MB/s (USB 3.0/3.1)

---

### Mac Air → LaCie (Remote Access via Tailscale)

```bash
# Option 1: SSH into Mac Studio, then access LaCie
ssh acebless@macstudio ls /Volumes/LaCie/repositories/

# Option 2: SSHFS mount LaCie on Mac Air (local convenience)
mkdir ~/mnt/lacie
sshfs acebless@macstudio:/Volumes/LaCie ~/mnt/lacie
ls ~/mnt/lacie/repositories/

# Option 3: SCP for one-time transfers
scp acebless@macstudio:/Volumes/LaCie/metadata/REPOSITORY_INTELLIGENCE_REGISTRY.yaml ~/local-copy/

# Option 4: Rsync for syncing (recommended for backups)
rsync -avz acebless@macstudio:/Volumes/LaCie/backups/ ~/mnt/lacie-backup/
```

**Performance:** ~10-50MB/s (network-limited, not disk-limited)

---

### Mac Air → T7 Shield (Local Access)

```bash
# Direct filesystem access (fastest on MacBook Air)
ls /Volumes/T7\ Shield/software-factory/
cat /Volumes/T7\ Shield/OmniRoute/bin/omniroute.mjs
```

**Performance:** ~100MB/s (USB 3.1)

---

### Mac Studio → T7 Shield (Remote Access via Tailscale)

```bash
# Option 1: SSH into Mac Air, then access T7 Shield
ssh acebless@macbookair ls /Volumes/T7\ Shield/software-factory/

# Option 2: SSHFS mount T7 Shield on Mac Studio (less common)
mkdir ~/mnt/t7
sshfs acebless@macbookair:/Volumes/T7\ Shield ~/mnt/t7
ls ~/mnt/t7/software-factory/
```

**Performance:** ~10-50MB/s (network-limited)

---

## 4. WHERE OMNIROUTE & EXOMCP SOURCE LIVES

### OmniRoute Source (Primary)

```
/Volumes/T7 Shield/05_SOFTWARE_FACTORY/Repositories/forks/OmniRoute/
├── bin/
│   ├── omniroute.mjs           # CLI entry point (v3.8.49)
│   ├── mcp-server.mjs          # MCP server adapter
│   └── antigravity-mcp.mjs     # FastMCP adapter (110 tools)
├── src/
│   └── ... (OmniRoute source)
├── config/
│   └── ... (routing rules, provider configs)
└── package.json
```

**Accessible from:**
- Mac Air (local): `/Volumes/T7 Shield/...`
- Mac Studio (remote): `ssh acebless@macbookair ls /Volumes/T7\ Shield/...`

**Installed globally:**
```bash
# Binary location (after npm install -g omniroute)
/opt/homebrew/bin/omniroute

# Can invoke from anywhere
omniroute --version   # v3.8.49
omniroute --mcp       # Start MCP server
```

---

### exo Source (Primary)

```
/Volumes/T7 Shield/05_SOFTWARE_FACTORY/Repositories/forks/exo/
├── exo/
│   ├── cli.py          # CLI interface
│   ├── inference.py    # Model inference
│   └── ... 
├── models/
│   └── qwen3.6-35b-a3b-5bit (native MLX, load-on-demand)
└── requirements.txt
```

**Running on Mac Studio:**
```bash
# exo daemon (native MLX)
exo serve --host 100.87.214.70 --port 52415

# Provides 120-model catalog
# Reachable from Mac Air at http://100.87.214.70:52415
```

---

## 5. DOCKER CONTEXT CONFIGURATION

**Mac Studio runs Docker natively via Tailscale SSH context:**

```bash
# Docker context name
docker --context macstudio ps

# This works because:
# - Mac Studio has Docker daemon running
# - Mac Air (or localhost via SSH) can reach it via Tailscale
# - SSH config has tailscale alias set up

# SSH config (in ~/.ssh/config or via Tailscale)
Host macstudio
    HostName 100.87.214.70
    User acebless
    Port 22
```

---

## 6. AWESOME LISTS INTEGRATION

The **Awesome ecosystem** is a curated meta-index that can enhance the Repository Intelligence System.

### Awesome Lists Ingestion Strategy

```
GitHub: sindresorhus/awesome
URL: https://github.com/sindresorhus/awesome
Status: ✅ Available

27 Top-Level Categories:
├── 01 Platforms
├── 02 Programming Languages
├── 03 Front-End Development
├── 04 Back-End Development
├── 05 Computer Science
├── 06 Big Data
├── 07 Theory
├── 08 Books
├── 09 Editors
├── 10 Gaming
├── 11 Development Environment
├── 12 Entertainment
├── 13 Databases              ← Directly relevant (Neo4j, Qdrant, Postgres)
├── 14 Media
├── 15 Learn
├── 16 Security               ← Directly relevant
├── 17 Content Management Systems
├── 18 Hardware               ← Relevant (Mac Studio, Raspberry Pi, etc.)
├── 19 Business               ← Directly relevant (ventures, startups)
├── 20 Work
├── 21 Networking
├── 22 Decentralized Systems
├── 23 Health & Social Science
├── 24 Events
├── 25 Testing                ← Relevant
├── 26 Miscellaneous
└── 27 Related
```

### How to Ingest Awesome Lists

**Phase A: Extract all Awesome lists**
```bash
# Clone the awesome repository
git clone https://github.com/sindresorhus/awesome /Volumes/LaCie/awesome-source/

# Extract all URLs from README.md (27 categories × N links each)
# Store in /Volumes/LaCie/repositories/awesome/
```

**Phase B: Parse each list's README**
```bash
# For each of 27 categories, there are sub-lists
# E.g., "13 Databases" → Neo4j, MongoDB, PostgreSQL, etc.

# Each sub-list is a separate GitHub repo
# Extract all repository URLs

# Map to our internal taxonomy:
Awesome List Category
  ↓
Company Brain Category
  ↓
Existing 904 starred repos (check for overlap)
  ↓
New repos (add to extended universe)
```

**Phase C: Deduplicate + Classify**
```
Awesome URLs
  ↓
Compare against existing 904 starred repos
  ↓
├─ 400+ overlap (already in our registry)
├─ 300+ new (add to extended registry)
└─ metadata enrichment
```

**Phase D: Store unified registry**
```yaml
/Volumes/LaCie/repositories/metadata/
├── REPOSITORY_INTELLIGENCE_REGISTRY.yaml (original 904)
├── AWESOME_LISTS_UNIVERSE.yaml           (27 categories)
└── UNIFIED_REPOSITORY_INTELLIGENCE.yaml  (904 + awesome overlap + new)
```

### Expected Results

```
Original 904 starred repos
        +
Awesome Lists Universe
        ↓
~1,200-1,500 total repositories mapped
        ↓
Organized by:
  ├── Company Brain category
  ├── Awesome category
  ├── Architecture layer
  ├── Technology stack
  └── Venture applicability
```

---

## 7. STORAGE QUICK REFERENCE

| Device | Storage | Mount | Capacity | Role | Access |
|--------|---------|-------|----------|------|--------|
| Mac Studio | Internal SSD | /Volumes/Macintosh HD | 512GB | System + active work | Local |
| Mac Studio | LaCie external | /Volumes/LaCie | **4TB** | Repository Intelligence + databases | Local (100MB/s) |
| Mac Air | Internal SSD | /Volumes/Macintosh HD | 228GB | System + active work | Local |
| Mac Air | T7 Shield external | /Volumes/T7 Shield | **2TB** | Source code + development | Local (100MB/s) |
| Network | Tailscale mesh | 100.87.214.70 (Mac Studio) | — | Remote service access | SSH/SSHFS (~50MB/s) |

---

## 8. DATA FLOW ARCHITECTURE

```
                    INTERNET / OSS
                          │
                    GitHub API
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    904 Starred      Awesome Lists    GitHub Topics
    (ingested)       (27 categories)    (metadata)
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                 ┌────────▼────────┐
                 │ /Volumes/LaCie  │
                 │ /repositories   │
                 │ /raw            │
                 └─────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    CLASSIFY          SCORE             DISPOSITION
    (agent)           (agent)           (agent)
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                 ┌────────▼────────┐
                 │   Neo4j Graph   │
                 │ 100.87.214.70   │
                 │ :7687           │
                 └─────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   CAPABILITY         VENTURE          AGENT
   MATCHING           ENABLEMENT       RECOMMENDATION
```

---

## 9. MOUNT VERIFICATION CHECKLIST

### Mac Studio

- [ ] `df -h | grep LaCie` shows /Volumes/LaCie (4TB)
- [ ] `ls /Volumes/LaCie/repositories/` lists: raw/, normalized/, enriched/, classified/, scored/, dispositioned/, adoption/, metadata/
- [ ] `docker --context macstudio ps` shows: civos_neo4j, civos_qdrant, civos_postgres, civos_redis
- [ ] `curl -s http://localhost:20128/health` returns OmniRoute status ✅
- [ ] `curl -s http://100.87.214.70:7687` reaches Neo4j (Bolt protocol)

### Mac Air

- [ ] `df -h | grep T7` shows /Volumes/T7\ Shield (2TB)
- [ ] `ls /Volumes/T7\ Shield/05_SOFTWARE_FACTORY/Repositories/forks/OmniRoute/bin/` shows omniroute.mjs ✅
- [ ] `ssh acebless@macstudio 'df -h | grep LaCie'` connects via Tailscale and shows remote LaCie
- [ ] `omniroute --version` shows v3.8.49 (installed globally)

---

## 10. TROUBLESHOOTING

### LaCie not mounting on Mac Studio
```bash
# Verify USB connection
system_profiler SPUSBDataType | grep LaCie

# Manual mount attempt
sudo mount -t exfat /dev/disk2s1 /Volumes/LaCie
```

### T7 Shield not accessible from Mac Studio
```bash
# Check Tailscale connectivity
tailscale status

# Verify SSH works
ssh acebless@100.121.17.63 'ls /Volumes/T7\ Shield/'

# If SSH fails, check firewall
ssh acebless@macbookair  # Try alias first
```

### Docker context not working
```bash
# Verify SSH context exists
docker context ls

# Re-create if needed
docker context create macstudio \
  --docker "host=ssh://acebless@100.87.214.70"

# Test
docker --context macstudio ps
```

---

**This topology enables:**
1. ✅ Local fast storage (LaCie on Mac Studio, T7 on Mac Air)
2. ✅ Remote access via Tailscale encrypted mesh
3. ✅ Unified repository intelligence system
4. ✅ Awesome lists integration into capability graph
5. ✅ Real-time data synchronization
6. ✅ Scalable adoption pipeline
