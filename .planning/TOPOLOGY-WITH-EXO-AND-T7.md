---
title: Complete Topology — Storage, Data, Network, Inference (with T7 & exo)
date: 2026-07-21
version: 2.0
status: ACTIVE
---

# Complete System Topology: Storage + Data + Network + Inference

**Master reference for complete infrastructure including T7 Shield, exo clustering, and data flows.**

---

## Physical & Network Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    Tailscale Network                        │
│                  (100.x.x.x private IPs)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐         ┌──────────────────────┐  │
│  │   MacBook Air        │         │   Mac Studio         │  │
│  │ 100.121.17.63        │◄───────►│ 100.87.214.70        │  │
│  │                      │ Tailscale                       │  │
│  │ ┌────────────────┐   │         │ ┌────────────────┐   │  │
│  │ │  T7 Shield     │   │         │ │ (storage TBD)  │   │  │
│  │ │ 1.8TB SSD      │   │         │ │                │   │  │
│  │ │ 1.1TB free     │   │         │ │ exo running    │   │  │
│  │ │ Thunderbolt    │   │         │ │ idle/no models │   │  │
│  │ └────────────────┘   │         │ └────────────────┘   │  │
│  │ (physically attached)│         │ (cluster node)      │  │
│  └──────────────────────┘         └──────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Storage Topology

| Machine | Device | Capacity | Used | Free | Type | Purpose |
|---------|--------|----------|------|------|------|---------|
| **MacBook Air** | /dev/disk0 | ~500GB | 480GB | 20GB | Internal SSD | System + code |
| **MacBook Air** | **T7 Shield** | **1.8TB** | **779GB** | **1.1TB** | **External SSD** | **Models + archives** |
| **Mac Studio** | /dev/disk3 | 460GB | 420GB | 29GB | Internal SSD | System |

**T7 = Primary model storage** (1.1TB free can hold 10-15 large models)

---

## Data Topology (Data Flows)

```
┌─────────────────────────────────────────────────────────────┐
│                   Source of Truth Layer                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PostgreSQL (localhost:5432)                                │
│  ├─ ventures, contacts, products                            │
│  ├─ venture_decisions, tasks, agent_logs                    │
│  └─ Mounted on: /Users/acebless/Documents (MacBook Air)     │
│                                                              │
│  ↓ (populate_venture_knowledge_graph.py)                    │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                 Knowledge Graph Layer                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Neo4j (localhost:7474)                                     │
│  ├─ Entities: Ventures, OPCOs, Skills, Repos                │
│  ├─ Relationships: belongs_to, has_capability, depends_on   │
│  └─ Docker container on: MacBook Air                        │
│                                                              │
│  Qdrant (localhost:6333)                                    │
│  ├─ Collections: notes (15K vectors), repositories (1.6K)   │
│  ├─ Embeddings: nomic-embed-text (768-dim, Ollama local)    │
│  └─ Docker container on: MacBook Air                        │
│                                                              │
│  ↓ (obsidian_graph_sync.py)                                 │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                    Retrieval Layer                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Ollama (inference models)                                  │
│  ├─ Location: T7 Shield (/Volumes/T7 Shield/ollama-models)  │
│  ├─ Models: qwen2.5:32b, qwen3:8b, nomic-embed-text         │
│  ├─ Served from: localhost:11434 (MacBook Air)              │
│  └─ OR from: 100.87.214.70:11434 (Mac Studio, not running)  │
│                                                              │
│  exo cluster (distributed inference)                        │
│  ├─ Mac Studio node: running, idle, unconfigured            │
│  ├─ MacBook Air node: NOT running yet                       │
│  ├─ Models: NONE loaded yet                                 │
│  └─ Cluster port: TBD (need configuration)                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Inference Network Topology (Current vs. Desired)

### CURRENT STATE (BROKEN)

```
Claude Code
    ↓
Hermes (~/.hermes/config.yaml)
    ├─ Primary: http://localhost:20128/v1 (OmniRoute)
    │   ├─ OmniRoute → ??? (not configured)
    │   └─ Falls through to fallback
    │
    └─ Fallback: http://100.87.214.70:11434/v1
        └─ Mac Studio Ollama (NOT RUNNING) ❌

Result: No inference possible
```

### DESIRED STATE (OPTION A: Ollama on T7)

```
Claude Code
    ↓
Hermes
    ├─ Primary: http://localhost:20128/v1 (OmniRoute)
    │   └─ OmniRoute → localhost:11434/v1 ✅
    │
    └─ Fallback: Anthropic API ✅
    
Ollama (localhost:11434)
    ├─ Models: /Volumes/T7\ Shield/ollama-models ✅
    ├─ Available: qwen2.5:32b, qwen3:8b, nomic-embed-text
    └─ Runs on: MacBook Air (this machine)

Result: Fast local inference + models on persistent T7 storage
```

### DESIRED STATE (OPTION B: exo Cluster)

```
Claude Code
    ↓
Hermes
    ├─ Primary: OmniRoute → exo cluster
    │
    └─ Fallback: Anthropic API
    
exo cluster (distributed inference across Tailscale)
    ├─ Node 1: Mac Studio (100.87.214.70)
    │   └─ Running, needs models loaded
    │
    ├─ Node 2: MacBook Air (100.121.17.63)
    │   └─ exo install + configure
    │
    └─ Shared storage: T7 Shield
        └─ Models: /Volumes/T7\ Shield/exo-models
        
exo cluster port: 8000 (or TBD based on config)

Result: Distributed inference across 2 Macs + shared model cache on T7
```

---

## T7 Integration

### Storage Path
```bash
/Volumes/T7\ Shield/
├─ ollama-models/          # Ollama model cache (19GB + 5GB + embeddings)
├─ exo-models/             # exo cluster model cache (if using exo)
└─ archives/               # Other data (currently ~779GB)
```

### Mounting
```bash
# Already mounted (auto-mount)
mount | grep T7
# Or: diskutil mount /Volumes/T7\ Shield

# Set Ollama models path
export OLLAMA_MODELS=/Volumes/T7\ Shield/ollama-models
ollama pull qwen2.5:32b
```

---

## Architecture Decision Matrix

| Approach | Storage | Compute | Network | Setup | Runtime |
|----------|---------|---------|---------|-------|---------|
| **Ollama on T7** | T7 (persistent) | MacBook Air | localhost | 5 min | Simplest |
| **exo cluster** | T7 (shared) | Both Macs | Tailscale | 20 min | Distributed |
| **Mac Studio Ollama** | Unknown | Mac Studio | Tailscale | 5 min | Unknown state |

---

## Network Flows (with T7)

### Data Ingestion
```
Supabase → PostgreSQL (local) → Neo4j + Qdrant (local) → Obsidian
```

### Inference Request
```
Claude Code
    ↓
Hermes (localhost)
    ↓
OmniRoute (localhost:20128)
    ↓
Ollama (localhost:11434, models from T7)
    ↓
Response back to Claude Code
```

### exo Cluster (if enabled)
```
Claude Code
    ↓
Hermes
    ↓
OmniRoute
    ↓
exo cluster API (port 8000?)
    ├─ Mac Studio node (100.87.214.70)
    ├─ MacBook Air node (100.121.17.63)
    └─ Models from: T7 Shield (shared via Tailscale?)
    ↓
Response back
```

---

## Implementation Roadmap

### Step 1: Ollama + T7 (Fastest, 5 min)
```bash
# 1. Create model directory on T7
mkdir -p /Volumes/T7\ Shield/ollama-models

# 2. Start Ollama with T7 storage
export OLLAMA_MODELS=/Volumes/T7\ Shield/ollama-models
ollama serve

# 3. Load models (in another terminal)
ollama pull qwen2.5:32b

# 4. Verify
curl http://localhost:11434/api/tags

# 5. Wire Hermes
# Already wired: ~/.hermes/config.yaml points to localhost:11434
```

### Step 2: exo Cluster (Advanced, 20 min)
```bash
# 1. Install exo on MacBook Air
git clone https://github.com/exo-explore/exo.git
cd exo && python -m venv .venv && source .venv/bin/activate
pip install -e .

# 2. Start exo node on MacBook Air
exo start --node-host 0.0.0.0 --node-port 8000

# 3. Configure cluster between both Macs
# (Requires exo cluster setup across Tailscale)

# 4. Load models into cluster
# (Models from T7 via shared mount)
```

---

## Status Summary

| Component | Location | Status | Notes |
|-----------|----------|--------|-------|
| **PostgreSQL** | MacBook Air | ✅ Running | Source of truth |
| **Neo4j** | MacBook Air (Docker) | ✅ Ready | Empty (needs populate) |
| **Qdrant** | MacBook Air (Docker) | ✅ Ready | 1.6K repo vectors |
| **T7 Shield** | MacBook Air (external) | ✅ Ready | 1.1TB free for models |
| **Ollama** | Not running | ⏳ Ready to start | Models can live on T7 |
| **exo Mac Studio** | Mac Studio | ⏳ Running, idle | No models, unconfigured |
| **exo MacBook Air** | Not running | ⏳ Can install | Needs setup |

---

## Recommendation

**Start with Ollama + T7 (Option A):**
- ✅ Simplest setup (5 min)
- ✅ Models persist on T7 (not lost if you restart)
- ✅ All inference stays local (fast)
- ✅ Hermes already configured to use it
- ⏳ exo can be added later if distributed inference needed

**Then scale to exo if needed** (but not urgent)

Execute Ollama + T7 now?
