---
name: CROSS-DEVICE-PERSISTENCE
title: Cross-Device Persistence Architecture
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Cross-Device Persistence Architecture

**Updated**: 2026-07-30  
**Goal**: Work seamlessly across Mac Air, Mac Studio, iPhone, iPad with Ollama-powered Hermes agent

---

## Files That Must Be Shared (The Checklist)

| File/Folder | Location | Sync Method | All Devices? | Purpose |
|-------------|----------|-------------|--------------|---------|
| **CLAUDE.md** (root) | `~/Documents/CLAUDE.md` | Git commit | ✅ Yes | Core system instructions, invariants |
| **TOPOLOGY.md** | `~/Documents/TOPOLOGY.md` | Git commit | ✅ Yes | Hardware/network reference |
| **CROSS-DEVICE-PERSISTENCE.md** | `~/Documents/CROSS-DEVICE-PERSISTENCE.md` | Git commit | ✅ Yes | THIS FILE — sync strategy |
| **.claude/CLAUDE.md** | `~/.claude/CLAUDE.md` | Git commit | ⚠️ Macs only | Project-specific overrides |
| **.worldwidebro/** | `~/.worldwidebro/` | Symlinks to T7 | ✅ Yes | Registries, scripts, ventures |
| **vex-api/** | `~/Documents/vex-api/` | Git + T7 Shield | ✅ Yes | Hermes backend integration |
| **vex-engine/** | `~/Documents/vex-engine/` | Git + T7 Shield | ✅ Yes | Frontend (mobile-responsive) |
| **vex-hero-site/** | `~/Documents/vex-hero-site/` | Git + T7 Shield | ✅ Yes | Landing pages (all devices) |
| **.planning/** | `~/Documents/.planning/` | Git commit | ✅ Yes | Current work, blockers, roadmap |
| **.obsidian/** | `~/Documents/.obsidian/` | Git commit | ⚠️ Macs only | Vault config for offline access |
| **scripts/** | `~/Documents/scripts/` | Git commit | ✅ Yes | Automation, venture indexing |
| **memory/** | `~/.claude/projects/.../memory/` | Git commit | ✅ Yes | Persistent session context (this session + history) |

---

## Sync Strategy (3 Tiers)

### ✅ Tier 1: Git (Real-time via GitHub)
**What**: CLAUDE.md, TOPOLOGY.md, .planning/, scripts/, memory/, .obsidian/  
**Frequency**: After each work session or daily  
**Devices**: Mac Air + Mac Studio (push/pull), iPhone/iPad (pull/view only)

```bash
# Mac Air: After work
git add CLAUDE.md TOPOLOGY.md CROSS-DEVICE-PERSISTENCE.md .planning/ memory/
git commit -m "chore: update system architecture and work state"
git push origin 2026-06-19-os-consolidation

# Mac Studio: Before Hermes processing
git pull origin 2026-06-19-os-consolidation

# iPhone/iPad: View via GitHub web (auto-sync)
open https://github.com/worldwidebro/Documents/blob/2026-06-19-os-consolidation/CLAUDE.md
```

### ✅ Tier 2: T7 Shield (Hot Storage via USB-C)
**What**: vex-api/, vex-engine/, vex-hero-site/, .worldwidebro/, all working code  
**Access**: Direct USB-C mount (both Macs), network share (iPad/iPhone)  
**Devices**: Mac Air (fast symlink), Mac Studio (direct `/Volumes/T7\ Shield/`), iPhone/iPad (SMB mount)

```bash
# Mac Air: Everything under ~/Documents is on T7
cd ~/Documents/vex-api  # Actually /Volumes/T7\ Shield/.../Documents/vex-api
git status  # T7 is a git repo too

# Mac Studio: Direct access
cd /Volumes/T7\ Shield/00_COMMAND_CENTER/worldwidebro-os/WORLDWIDEBRO-OS/Documents/

# iPhone/iPad: Mount as network share
# Go to Files > Connect to Server > smb://mac-studio.local/T7Shield
# Browse ventures, read deployment status, check code
```

### ✅ Tier 3: Hermes Agent State (Redis + PostgreSQL)
**What**: Current venture context, task state, model state, session checkpoints  
**Where**: Redis (Mac Studio, port 6379) + PostgreSQL backup  
**Sync**: Real-time via Hermes API + Git commits for long-term history

```json
{
  "session_id": "hermes-mac-air-2026-07-30",
  "device": "mac-air",
  "venture_context": {
    "venture_id": "CON-001",
    "venture_name": "ACE Construction",
    "task": "Connect ventures to code functions",
    "models_loaded": ["qwen3:8b"],
    "status": "in_progress",
    "last_update": "2026-07-30T11:29:00Z"
  },
  "ollama_endpoint": "http://100.87.214.70:11434",
  "device_checkpoints": {
    "mac_air": {
      "branch": "2026-06-19-os-consolidation",
      "last_commit": "e754636f",
      "memory_loaded": true,
      "CLAUDE_md_version": "3.0"
    },
    "mac_studio": {
      "ollama_status": "running",
      "ollama_models": ["qwen3:8b"],
      "redis_connected": true
    },
    "ipad": {
      "last_sync": "2026-07-30T10:00:00Z",
      "access_level": "read-only"
    }
  }
}
```

---

## Device-Specific Setup

### Mac Air (Primary Developer)
**What you see**: Full read/write access to everything
```
CLAUDE.md (loaded in Claude Code)
├── ~/.claude/CLAUDE.md (root overrides)
├── TOPOLOGY.md (hardware reference)
├── CROSS-DEVICE-PERSISTENCE.md (this file)
├── .planning/ (current work)
├── memory/ (session context — auto-loaded)
├── ~/Documents/ → /Volumes/T7\ Shield/.../Documents/
│   ├── vex-api/ (edit, test, push)
│   ├── vex-engine/ (edit, deploy)
│   ├── vex-hero-site/ (edit, deploy)
│   └── scripts/ (run, edit)
└── Ollama via SSH tunnel
    ssh -N -L 11434:localhost:11434 acebless@mac-studio.local
    └── http://localhost:11434/api/chat (Hermes agent)
```

### Mac Studio (Services Hub)
**What it runs**: All services + Hermes agent
```
CLAUDE.md (via git pull)
├── TOPOLOGY.md (reference)
├── /Volumes/T7\ Shield/ (full access to code)
├── Ollama
│   ├── qwen3:8b model
│   ├── Port 11434 (exposed to Tailscale: 100.87.214.70:11434)
│   └── Hermes queries (localhost:11434)
├── Redis (6379)
│   └── Hermes session state + device checkpoints
├── PostgreSQL (5432)
│   └── Venture context, task history
└── Neo4j (7687)
    └── Venture graph, capabilities, relationships
```

### iPhone/iPad (Read-Only Access)
**What you can do**: Monitor, read, check dashboards
```
CLAUDE.md (via GitHub web)
├── GitHub view of CLAUDE.md + .planning/
├── T7 Shield (SMB/NFS mount)
│   ├── Read venture files
│   ├── Check deployment status
│   └── View code diffs
└── Hermes Dashboard (Tailscale)
    ├── http://100.87.214.70:8080 (Chat2DB)
    ├── http://100.87.214.70:3010 (Ollama WebUI)
    ├── http://100.87.214.70:7474 (Neo4j browser)
    └── Check task progress, venture status
```

---

## Hermes Agent (Ollama-Powered) Resume Workflow

### How It Works Across Devices

**Mac Air (current device):**
1. You ask: "Resume venture connection work"
2. Claude Code loads CLAUDE.md (root) + memory files
3. Claude Code connects to Hermes via SSH tunnel
4. Hermes fetches checkpoint from Redis:
   ```json
   {
     "venture_id": "CON-001",
     "last_task": "Connect ventures to code functions",
     "context_files": ["vex-api/venture-connector.py", "03-VENTURES/CON-001/"]
   }
   ```
5. Hermes uses qwen3:8b to continue: "CON-001 is a construction venture. Here's what we were doing..."
6. You work, save, commit

**Mac Studio (or later, on another device):**
```bash
git pull origin 2026-06-19-os-consolidation  # Get latest work
# CLAUDE.md memory auto-loads
# Ask Hermes the same question
# Hermes fetches updated checkpoint from Redis
# Continues seamlessly from where Mac Air left off
```

**iPhone (checking progress):**
```
1. Open GitHub app, view .planning/current-work.md
2. Open Chat2DB (100.87.214.70:8080)
3. Ask: "What ventures are we connecting?"
4. See live status + next steps
```

---

## Implementation Checklist

- [ ] **Git**: All core files committed (CLAUDE.md, TOPOLOGY.md, CROSS-DEVICE-PERSISTENCE.md, .planning/, memory/, scripts/)
- [ ] **T7 Shield**: Mounted on both Macs, ~/Documents symlinked on Mac Air
- [ ] **Ollama**: Running on Mac Studio, exposed via Tailscale (100.87.214.70:11434)
- [ ] **Redis**: Running on Mac Studio (6379), storing Hermes checkpoints
- [ ] **Hermes Agent**: Python script (hermes-agent.py) running on Mac Studio
- [ ] **SSH Tunnel**: Tested from Mac Air → Mac Studio:11434
- [ ] **Tailscale**: All devices on VPN (100.x.x.x subnet)
- [ ] **SMB/NFS**: T7 Shield accessible from iPhone/iPad (read-only)
- [ ] **CLAUDE.md**: Synced across all machines (identical root copy)

---

## The Flow (Summary)

```
T7 Shield (Master)
    ↓ (Git push/pull)
GitHub (Permanent record)
    ↓ (Every device pulls)
Mac Air ← → Mac Studio ← → iPhone/iPad
    ↑         ↑              ↓
  Code      Ollama        Dashboard
  Edit      Process       Monitor
  Commit    Hermes        Read
            Checkpoint
```

**Key insight**: T7 Shield is the source of truth. Git keeps history. Redis tracks session state. Every device can resume exactly where the last device left off.
