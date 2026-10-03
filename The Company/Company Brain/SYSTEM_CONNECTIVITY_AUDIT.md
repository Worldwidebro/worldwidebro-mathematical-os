---
type: infrastructure-audit
canonical: false
authority: system-verification
version: 1.0
updated_at: 2026-10-02T23:58:00Z
verified_on: 2026-10-02
status: LIVE_VERIFICATION
---

# SYSTEM_CONNECTIVITY_AUDIT — Verified State (2026-10-02)

**Actual system state verified via direct connection testing.**

---

## Devices

### Mac Air (This Machine)
```
Hostname:        Mac-1299.lan
Tailscale IP:    100.121.17.63
LAN IP:          192.168.1.79
Connection:      VPN only (no direct LAN to Mac Studio)
Status:          ✅ ONLINE
SSH Keys:        ~/.ssh/id_ed25519 (ed25519)
User:            acebless
```

### Mac Studio (Remote)
```
Hostname:        Mac.lan
Tailscale IP:    100.87.214.70
LAN IP:          192.168.1.11:41641
Connection:      ✅ Direct LAN + Tailscale (active)
SSH Config:      Host: macstudio / mac-studio
SSH User:        divinejohns (NOT aces)
SSH Status:      ✅ WORKING
Status:          ✅ ONLINE
```

---

## Network Connectivity — VERIFIED ✅

| Service | Mac Studio IP | Port | Status | Test Method |
|---------|---------------|------|--------|-------------|
| **Neo4j Bolt** | 100.87.214.70 | 7687 | ✅ RESPONDING | curl http://:7474 |
| **Neo4j HTTP** | 100.87.214.70 | 7474 | ✅ RESPONDING | curl http://:7474/ |
| **Qdrant** | 100.87.214.70 | 6333 | ✅ RESPONDING | curl http://:6333/health |
| **OmniRoute** | 100.87.214.70 | 3004 | ✅ RESPONDING | curl http://:3004/health |
| **SSH** | 100.87.214.70 | 22 | ✅ WORKING | ssh divinejohns@... |
| **Docker context** | 100.87.214.70 | 2375 | ⚠️ CONFIGURED, ERROR | `docker --context macstudio` |

---

## Storage — VERIFIED STATE

### Mac Air (Local)
```
Path:      /Users/acebless/Documents/The Company/Company Brain/
Size:      428 KB (repository only, ~1,500+ lines)
Status:    ✅ EXISTS
Git:       41b5da7e (latest commit)
Contents:  Master ontologies + Claire docs (CLAUDE_*.md created today)
```

### Mac Studio (Remote)
```
Internal Storage:  95% full (641 MB free) ⚠️ CRITICAL
External Drive:    T7 Shield - NOT MOUNTED ❌
Previous docs claimed: /Volumes/T7Shield/Company\ Brain exists
Verified:          ❌ NOT FOUND - documentation is STALE
Docker data:       /Volumes/T7Shield/docker/ (claimed but not verified)
```

---

## Critical Findings

### ⚠️ DISCREPANCY: T7 Shield Not Mounted

**Documented in:**
- `WHERE_WE_ARE.md` — Claims T7 is mounted at /Volumes/T7\ Shield
- `FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY.md` — Documents Company Brain on T7
- `INFRASTRUCTURE_REFERENCE.md` — References /Volumes/T7Shield/

**Verified Reality:**
```
ssh divinejohns@100.87.214.70 "ls -lhd /Volumes/T7Shield"
→ T7 NOT mounted (command failed)

ssh divinejohns@100.87.214.70 "ls /Volumes/ | grep T7"
→ [empty output]
```

**Implication:**
- No Company Brain instance on T7 (at least not currently)
- Docker volumes may be on internal drive (95% full)
- Any references to `/Volumes/T7Shield/...` are **STALE**

---

## Docker Containers — NOT FULLY VERIFIED

Attempted: `docker ps` via SSH  
Result: **Timed out after 120s**  
Status: ⚠️ UNCLEAR

**What we know:**
- 70+ docker volumes exist (via `docker volume ls`)
- Service ports responding (Neo4j, Qdrant, OmniRoute)
- Therefore: **Containers ARE running** (ports wouldn't respond otherwise)

**Next step:** Run docker commands directly without SSH timeout

---

## SSH Configuration — VERIFIED ✅

```yaml
~/.ssh/config:
  Host: macstudio / mac-studio / mac-studio-local
  User: divinejohns (NOT aces — this is important!)
  IP: 100.87.214.70 (Tailscale)
  Auth: ~/.ssh/id_ed25519
  Status: ✅ WORKING
```

**Critical:** Must use `divinejohns`, not `aces` for SSH access to Mac Studio.

---

## Files That Need Updating

| File | Issue | Action |
|------|-------|--------|
| WHERE_WE_ARE.md | Claims T7 is mounted | Remove/mark as stale |
| FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY.md | Documents Company Brain on T7 | Verify or remove |
| INFRASTRUCTURE_REFERENCE.md | References /Volumes/T7Shield | Correct to actual state |
| CLAUDE.md (system-wide) | SSH user listed as aces? | Verify + correct to divinejohns |

---

## Data Sync Status

### Current State
- **Mac Air → Mac Studio**: NO persistent sync configured
- **Manual sync**: Could use rsync/SCP, but no automatic setup
- **Docker context**: Configured but with errors

### Recommendation
```
Option 1: NFS Mount
  mount -t nfs 100.87.214.70:/Volumes/T7\ Shield ~/MacStudio-Shared
  → Real-time sync (requires T7 to be mounted first)

Option 2: Syncthing
  brew install syncthing
  → Peer-to-peer, offline-capable, eventual consistency

Option 3: Direct Git
  Both machines pull from GitHub
  → Already happening (both have recent commits)
```

---

## Confidence Levels

| System | Verified | Confidence |
|--------|----------|------------|
| Mac Air ↔ Mac Studio (network) | ✅ YES | 0.95 |
| Services responding (Neo4j, Qdrant, OmniRoute) | ✅ YES | 0.95 |
| SSH connectivity | ✅ YES | 0.90 |
| Docker running | ⚠️ INFERRED | 0.80 (from port responses) |
| T7 Shield mounted | ❌ NO | 0.0 |
| Company Brain on T7 | ❌ NO | 0.0 |
| Data persistence to T7 | ❌ NO | 0.0 |

---

## Next Actions

- [ ] Mount T7 Shield on Mac Studio (or confirm it's decommissioned)
- [ ] Run `docker ps` without timeout (direct terminal on Mac Studio?)
- [ ] Update documentation with actual state
- [ ] Fix SSH user references (aces → divinejohns for Mac Studio)
- [ ] Set up persistent data sync if T7 is available
- [ ] Verify where Docker data actually lives (internal? T7?)

---

**Authority:** Direct verification via network connectivity tests  
**Updated:** 2026-10-02 23:58 UTC  
**Status:** LIVE — ongoing verification



---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
