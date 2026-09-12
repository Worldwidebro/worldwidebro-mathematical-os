# Infrastructure Device Inventory — Mac Studio + Mac Air + Tailscale

**Date:** 2026-09-12  
**Authority:** CP-027 (Infrastructure)  
**Tailscale Network:** Worldwidebro (6 devices, 4 active)

---

## DEVICE INVENTORY

### 1. MAC STUDIO (Primary Compute)

```yaml
device:
  name: "mac-studio"
  tailscale_ip: "100.87.214.70"
  status: "ACTIVE (direct connection 192.168.1.11:41641)"
  connection_type: "Direct LAN + Tailscale"
  
storage:
  internal_ssd:
    size: "228 GB"
    used: "200 GB (95% full) ⚠️"
    available: "641 MB (CRITICAL)"
  external_drive:
    name: "T7 Shield"
    size: "1.8 TB"
    used: "941 GB (51%)"
    available: "922 GB ✅ (plenty of headroom)"
  
docker_volumes:
  count: 70+
  key_volumes:
    - infra_neo4j_data
    - infra_qdrant_data
    - infra_redis_data
    - infra_omniroute_data
    - infra_minio_data
    - t7shield_neo4j_data
    - t7shield_qdrant_data
    
running_services:
  - Neo4j (bolt://100.87.214.70:7687)
  - Qdrant (http://100.87.214.70:6333)
  - PostgreSQL (port 5433)
  - Redis (port 6379)
  - OmniRoute (http://100.87.214.70:3000)
  - LiveKit (port 17880-17882)
  - Docker context: "macstudio"
```

### 2. MAC AIR (Secondary / This Machine)

```yaml
device:
  name: "aces-macbook-air-1"
  tailscale_ip: "100.121.17.63"
  status: "ACTIVE"
  connection_type: "Tailscale only (no direct LAN)"
  
storage:
  internal_ssd:
    size: "228 GB"
    used: "212 GB (95% full) ⚠️ CRITICAL"
    available: "641 MB (CRITICAL)"
  
docker_context: "Can access macstudio context remotely"
```

### 3. OTHER DEVICES (Tailscale)

| Device | IP | Status | Type | Last Seen |
|--------|--|----|------|-----------|
| dexterslab | 100.126.240.124 | — | iOS | Current |
| divines-imac | 100.126.240.61 | offline | macOS | 183 days ago |
| ipad-10th-gen | 100.110.180.123 | offline | iOS | 59 days ago |

---

## MODEL INVENTORY (LLM / Embeddings)

### Mac Studio Ollama Models

| Model | Size | Status | Purpose |
|-------|------|--------|---------|
| **qwen2.5-coder:14b** | 8.9 GB | ✅ Ready | Code generation + analysis |
| **hermes3:latest** | 4.6 GB | ✅ Ready | Reasoning + long context |
| **llama3.1:8b** | 4.9 GB | ✅ Ready | General-purpose inference |

**Total Model Size:** 18.5 GB (stored on Mac Studio)  
**Accessible via:** `curl http://100.87.214.70:11434/` (Tailscale)  
**Query endpoint:** `/api/tags` (list models), `/api/generate` (inference)

### Mac Air Ollama Models

| Model | Size | Status | Purpose |
|-------|------|--------|---------|
| **nomic-embed-text:latest** | 274 MB | ✅ Ready | Text embeddings |

**Total Model Size:** 274 MB  
**Status:** Minimal setup (embeddings only, offload reasoning to Mac Studio)

### exo Models (Mentioned in CLAUDE.md)

**Reference:** `100.87.214.70:52415` (MLX native models)  
**Catalog:** 120+ models available  
**Status:** ⚠️ Not currently responding (needs verification)

---

## PERSISTENCE & DATA FLOW

### Current State

```
Mac Air (This Machine)
├── Local storage: 641 MB available (95% full) ⚠️
├── Ollama: nomic-embed-text only
├── Docker: Can access macstudio context
└── Tailscale: Connected to Mac Studio

                    ↓
            [TAILSCALE VPN]
                    ↓

Mac Studio (Primary)
├── Internal storage: 641 MB available (95% full) ⚠️
├── External storage: 922 GB available ✅
├── Ollama: 3 models (18.5 GB)
├── Docker: 70+ volumes (Neo4j, Qdrant, PostgreSQL, Redis, OmniRoute)
├── Services: All databases + MCP routing
└── Backup volumes: T7 Shield (1.8 TB)
```

### Data Sync Mechanism

**CURRENTLY:** No persistent data sync between machines  
**NEEDED:** Shared storage setup for:
- Code repositories
- Claude memory files
- Scenario definitions
- Execution logs
- Model cache

---

## RECOMMENDATIONS: SHARED PERSISTENCE

### Option 1: NFS Mount (Recommended)

**Setup:**
```bash
# On Mac Studio: Enable NFS sharing
sudo vi /etc/exports
# Add: /Volumes/T7\ Shield -alldirs -mapall=acebless:staff 100.87.214.70/32

# On Mac Air: Mount via Tailscale
mkdir /Volumes/MacStudio-Shared
sudo mount -t nfs 100.87.214.70:/Volumes/T7\ Shield /Volumes/MacStudio-Shared
```

**Benefit:** Real-time file sync, transparent access  
**Cost:** Network latency (~1-10ms via Tailscale)  
**Capacity:** 922 GB available on T7 Shield

### Option 2: Syncthing (Peer-to-Peer)

**Setup:**
```bash
brew install syncthing
# Configure to sync:
# - ~/.claude/projects (memory + config)
# - ~/Documents/Company Brain (repos + docs)
# - ~/.ollama/models (model cache)
```

**Benefit:** Bidirectional sync, offline-capable  
**Cost:** Disk I/O on both machines  
**Latency:** Eventually consistent (seconds to minutes)

### Option 3: rsync + Cron

**Setup:**
```bash
# Sync Mac Air to Mac Studio every hour
crontab -e
# 0 * * * * rsync -azP ~/Documents/Company\ Brain/ 100.87.214.70:/Volumes/T7\ Shield/Company\ Brain/
```

**Benefit:** Simple, low overhead  
**Cost:** No real-time sync  
**Latency:** Hourly batches

---

## MODEL ACCESS STRATEGY

### Current Setup

**Mac Air → Mac Studio via Tailscale:**
```
Claude Code on Mac Air
    ↓
/mcp status (Make, Supabase, etc.)
    ↓
Claude Code requests inference
    ↓
curl http://100.87.214.70:11434/api/generate
    ↓
Mac Studio Ollama (qwen2.5-coder:14b, hermes3, llama3.1:8b)
    ↓
Response back to Mac Air
```

### Recommended Expansion

**Add local fallback on Mac Air:**
```
Before Mac Air offloads to Mac Studio:
├── Check if embedding only → use nomic-embed-text (local)
├── Check if code gen + reasoning → use qwen2.5-coder (Mac Studio)
└── Add mistral:7b or neural-chat locally for offline fallback
```

**Storage impact:** Add ~4-5 GB to Mac Air (currently 641 MB available ⚠️)

---

## CRITICAL ISSUES

### 🔴 **STORAGE CRITICAL ON BOTH MACHINES**

| Machine | Capacity | Used | Available | Status |
|---------|----------|------|-----------|--------|
| Mac Air (internal) | 228 GB | 212 GB | **641 MB** | 🔴 CRITICAL |
| Mac Studio (internal) | 228 GB | 200 GB | **641 MB** | 🔴 CRITICAL |
| Mac Studio (external T7) | 1.8 TB | 941 GB | 922 GB | ✅ OK |

**Action Required:**
1. Clear cache on Mac Air (Ollama, Docker, Xcode, etc.)
2. Move working data to Mac Studio T7 Shield
3. Set up NFS mount for shared access
4. Configure periodic cleanup (Homebrew, pip, npm cache)

### ⚠️ **Mac Air SSH Authentication Failed**

Error: "Too many authentication failures"  
Impact: Can't remotely query Mac Air Ollama via SSH  
Solution: Reset SSH config or use Tailscale VPN directly

---

## DOCKER CONTEXT USAGE

### Remote Mac Studio Context

```bash
# From Mac Air, control Mac Studio Docker
docker --context macstudio ps
docker --context macstudio logs omniroute-gateway
docker --context macstudio volume ls
docker --context macstudio exec -it neo4j bash

# Example: Start OmniRoute from Mac Air
docker --context macstudio start omniroute-gateway
```

### Advantages

- ✅ Centralized database management
- ✅ No need to SSH into Mac Studio
- ✅ Works over Tailscale VPN
- ✅ All volumes accessible remotely

---

## INTER-DEVICE CAPABILITIES

### What's Available Now

| Capability | Mac Air | Mac Studio | Via Tailscale |
|------------|---------|-----------|---------------|
| Ollama inference | ✅ (embeddings only) | ✅ (3 models) | ✅ |
| Docker control | Via remote context | Native | ✅ |
| Neo4j access | Via TCP | Native | ✅ |
| Qdrant access | Via TCP | Native | ✅ |
| OmniRoute MCP | Via TCP:3000 | Native | ✅ |
| File sync | None yet | — | Manual (rsync/SCP) |
| Model cache | 274 MB | 18.5 GB | Via NFS (TBD) |

### What's Missing

| Need | Why | Impact |
|------|-----|--------|
| **Shared NFS mount** | Real-time file sync | Can't easily share repos + memory |
| **Model cache sync** | No copy of qwen2.5-coder on Mac Air | Inference always remote latency |
| **SSH key setup** | Auth failures prevent direct connection | Can't use SSH-based remote tools |
| **Persistent volume backup** | T7 Shield not yet in automated backup | Data at risk |

---

## RECOMMENDED DEPLOYMENT

### Week 1 (Immediate)

```
✅ Completed:
- Make scenario #6252367 DEPLOYED
- Tailscale mesh ACTIVE
- OmniRoute running on Mac Studio
- Remote Docker context working

🔄 In Progress:
- LT-005 first execution (Sep 12, 23:46 UTC)

🟡 Pending:
- Clean up storage (both machines at 95%)
- Set up NFS mount for shared data
- Fix SSH key for direct Mac Air access
- Configure model fallback (offline capability)
```

### Week 2+

```
- Mirror Ollama models to Mac Air (backup + offline capability)
- Enable Syncthing for bidirectional repo sync
- Set up automated backups to T7 Shield
- Monitor execution logs across machines
- Expand to OPS-001, CON-001 scenarios
```

---

## QUICK REFERENCE: ACCESS FROM MAC AIR

**Query Mac Studio Ollama:**
```bash
curl -s http://100.87.214.70:11434/api/tags | jq '.models[].name'
```

**Connect to Neo4j:**
```bash
neo4j bolt://neo4j:changeme@100.87.214.70:7687
```

**Access Qdrant:**
```bash
curl http://100.87.214.70:6333/health
```

**Control Docker on Mac Studio:**
```bash
docker --context macstudio ps
```

**Access OmniRoute:**
```bash
curl http://100.87.214.70:3000/
```

---

**Last Updated:** 2026-09-12  
**Owner:** Divine (winnerscirclewcllc@gmail.com)  
**Next Review:** After storage cleanup
