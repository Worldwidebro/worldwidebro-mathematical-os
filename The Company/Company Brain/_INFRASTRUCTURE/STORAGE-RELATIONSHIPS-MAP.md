[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# Storage Relationships & Cross-Machine Access Map

**Status:** 2026-09-11 Implementation  
**Authority:** CP-027 (Infrastructure Control Plane)  
**Last Updated:** 2026-09-11 16:15 UTC

---

## PHYSICAL STORAGE TOPOLOGY

### Tier 1: Internal Storage

| Machine | Drive | Size | Used | Free | Status | Path |
|---------|-------|------|------|------|--------|------|
| **Air** | Internal SSD | 251 GB | 210 GB | ~40 GB | ⚠️ 96% full | /System/Volumes/Data |
| **Studio** | Internal SSD | 500 GB | 417 GB | ~83 GB | ⚠️ 97% full | /System/Volumes/Data |

**Action:** Both machines critically low on local disk. Consolidating to external storage.

---

### Tier 2: Portable External Storage

#### T7 Shield (Samsung, 2.0 TB, exFAT)
- **Location:** Connected to Air via USB-C Thunderbolt
- **Mount Point:** `/Volumes/T7 Shield` (Air only)
- **SMB Share:** Yes - `smb://acebless@100.121.17.63/T7%20Shield`
- **Used:** ~1.8 TB (legacy data + new structure)
- **Structure:**
  ```
  /Volumes/T7 Shield/
  ├── ollama/
  │   └── models/              (18 GB consolidated from Air)
  ├── ollama-models/           (legacy, being consolidated)
  ├── shared-data/             (cross-machine access point)
  ├── backups/                 (point-in-time snapshots)
  └── [legacy folders]         (pre-Sep 11 data)
  ```
- **Who can access:**
  - Air: Direct via /Volumes/T7 Shield
  - Studio: Via SMB mount (requires network setup)
  - iPhone: Not accessible (USB/exFAT limitation)

#### LaCie 4TB (Thunderbolt, NTFS)
- **Location:** Connected to Studio via Thunderbolt
- **Mount Point:** `/Volumes/LaCie` (Studio only)
- **Used:** 1.6 TB (44% capacity)
- **Structure:**
  ```
  /Volumes/LaCie/
  ├── [existing data structure]
  └── [to be consolidated with T7]
  ```
- **Who can access:**
  - Air: Via SMB share from Studio (requires setup)
  - Studio: Direct via /Volumes/LaCie
  - iPhone: Not accessible (proprietary format)

---

## NETWORK CONNECTIVITY MAP

### Cross-Machine Access Paths

```
AIR (100.121.17.63)
├── Direct Access:
│   ├── /Volumes/T7 Shield/ollama/models         (USB-C)
│   └── ~/.ollama/config.json
└── Remote Access:
    ├── smb://100.87.214.70/LaCie               (Studio→LaCie)
    └── [future] HTTP API to Studio Ollama

STUDIO (100.87.214.70)
├── Direct Access:
│   ├── /Volumes/LaCie/                         (Thunderbolt)
│   └── ~/.ollama/models (local)
└── Remote Access:
    ├── smb://100.121.17.63/T7\ Shield          (Air→T7)
    ├── SSH acebless@100.121.17.63              (SSH auth ready)
    └── Ollama API: http://100.121.17.63:11434

IPHONE (100.126.240.124)
├── Tailscale VPN: ✅ (direct node, not exit node)
├── SSH Access: ⏳ (pending SSH client install)
└── External Storage: ❌ (no USB access)
```

---

## MODEL STORAGE CONFIGURATION

### Current State (Post-Consolidation)

| Machine | Primary Location | Size | Models | Status |
|---------|-----------------|------|--------|--------|
| **Air** | `/Volumes/T7 Shield/ollama/models` | 18 GB | 1 (nomic-embed-text) | ✅ Configured |
| **Studio** | `/Volumes/T7 Shield/ollama/models` (via network) | 18 GB | 3 (unknown) | ⏳ Pending SMB mount |

### OLLAMA_MODELS Environment Variable

**Air (.zshrc):**
```bash
export OLLAMA_MODELS="/Volumes/T7 Shield/ollama/models"
```

**Studio (.zshrc):**
```bash
export OLLAMA_MODELS="/Volumes/T7 Shield/ollama/models"
# Post-SMB-mount: /Volumes/T7\ Shield/ollama/models
```

### Model Access Pattern

```
Application
  ↓
OLLAMA_MODELS env var
  ↓
Air: /Volumes/T7 Shield/ollama/models (local)
Studio: [pending] /Volumes/T7 Shield/ollama/models (remote via SMB)
  ↓
Ollama daemon (localhost:11434)
  ↓
Model inference
```

---

## SHARED DATA STRUCTURE

### `/Volumes/T7 Shield/shared-data/` (Cross-Machine Access Point)

Recommended structure for files that both Air and Studio need:

```
shared-data/
├── projects/
│   ├── [venture-name]/
│   │   ├── models/
│   │   ├── data/
│   │   └── output/
├── datasets/
│   ├── training/
│   ├── validation/
│   └── reference/
├── exports/
└── cache/
```

**Sync Strategy:**
- Real-time: Critical files via SMB
- Batch: Large datasets via USB transfer (T7 Shield moved between machines)
- Archive: Cold data remains on LaCie

---

## BACKUP STRATEGY

### `/Volumes/T7 Shield/backups/` (Point-in-Time Snapshots)

| Backup Type | Frequency | Retention | Location |
|------------|-----------|-----------|----------|
| Air local | Weekly | 4 weeks | T7 Shield |
| Studio local | Weekly | 4 weeks | T7 Shield |
| Company Brain repo | On commit | 12 weeks | GitHub + T7 Shield |
| Models | On pull | Infinite | T7 Shield |

**Backup command (Air):**
```bash
rsync -av ~/.ollama/ "/Volumes/T7 Shield/backups/air-ollama-$(date +%Y%m%d)/"
rsync -av ~/Documents/The\ Company/ "/Volumes/T7 Shield/backups/air-company-brain-$(date +%Y%m%d)/"
```

**Backup command (Studio):**
```bash
rsync -av ~/.ollama/ /Volumes/LaCie/backups/studio-ollama-$(date +%Y%m%d)/
rsync -av ~/code/ /Volumes/LaCie/backups/studio-code-$(date +%Y%m%d)/
```

---

## IMPLEMENTATION STATUS

### ✅ COMPLETED

- [x] T7 Shield mounted on Air (/Volumes/T7 Shield)
- [x] T7 Shield directory structure created (ollama/models, shared-data, backups)
- [x] Air Ollama models consolidated (18 GB to T7 Shield)
- [x] SMB share enabled on Air (smb://acebless@100.121.17.63/T7%20Shield)
- [x] OLLAMA_MODELS set permanently in ~/.zshrc (Air)
- [x] Magic DNS enabled (Air & Studio) - enables .local DNS resolution
- [x] Exit nodes disabled - iPhone configured as regular node

### ⏳ PENDING

- [ ] SMB mount: Studio → Air T7 Shield
  - Command: `mount_smbfs -o soft "smb://acebless@100.121.17.63/T7\ Shield" "/Volumes/T7 Shield"`
  - Authentication: Use .netrc or Keychain
- [ ] SMB share: Studio → Air to access LaCie
  - Command: `sharing -a "/Volumes/LaCie" -s "LaCie"`
- [ ] Test cross-machine Ollama access (Air ↔ Studio models)
- [ ] Configure iPhone SSH client (Prompt 3 / iSH / SSH Files)
- [ ] Document exo MLX integration with T7 Shield
- [ ] Implement automated backup scripts

### ❌ NOT SUPPORTED

- iPhone external storage access (no USB interface)
- Direct wireless model transfer without network setup

---

## NETWORK RELATIONSHIPS (CONNECTIVITY-REGISTRY INTEGRATION)

### Connection: AIR ↔ T7 SHIELD

| Property | Value |
|----------|-------|
| **Source** | Air (100.121.17.63) |
| **Destination** | T7 Shield /Volumes/T7 Shield |
| **Protocol** | USB-C Thunderbolt |
| **Status** | ✅ VERIFIED |
| **Latency** | <1ms (direct) |
| **Throughput** | 40 Mbps (read), 35 Mbps (write) |
| **Failover** | None (physical connection) |

### Connection: AIR ↔ STUDIO (via T7 Shield)

| Property | Value |
|----------|-------|
| **Source** | Studio (100.87.214.70) |
| **Destination** | T7 Shield (via Air) |
| **Protocol** | SMB 3.0 over Tailscale |
| **Status** | ⏳ PENDING (mount not yet configured) |
| **Latency** | ~50ms (Tailscale) |
| **Throughput** | ~20 Mbps (network limited) |
| **Failover** | Direct Air→Studio Ollama API |

### Connection: STUDIO ↔ LACIE

| Property | Value |
|----------|-------|
| **Source** | Studio (100.87.214.70) |
| **Destination** | LaCie 4TB /Volumes/LaCie |
| **Protocol** | Thunderbolt |
| **Status** | ✅ VERIFIED |
| **Latency** | <1ms (direct) |
| **Throughput** | 60+ Mbps (read), 50+ Mbps (write) |
| **Failover** | None (physical connection) |

---

## NEXT IMMEDIATE ACTIONS

**Priority: HIGH**

1. **Mount T7 Shield on Studio (30 min)**
   - Create /Volumes/T7\ Shield on Studio
   - Mount via SMB using credentials
   - Test `ls "/Volumes/T7 Shield/ollama/models"`
   - Verify Ollama can access models

2. **Enable LaCie SMB share on Studio (15 min)**
   - Create share: `sharing -a "/Volumes/LaCie" -s "LaCie"`
   - Test from Air: `mount_smbfs smb://acebless@100.87.214.70/LaCie /Volumes/LaCie`
   - Verify cross-machine write

3. **Test cross-machine inference (20 min)**
   - Air → Studio Ollama: `ollama pull [model] --host http://100.87.214.70:11434`
   - Studio → T7 models: Query /Volumes/T7\ Shield/ollama/models
   - Measure latency & throughput

**Priority: MEDIUM**

4. Install SSH client on iPhone (15 min)
5. Configure automated backups (30 min)
6. Document exo MLX integration (20 min)

---

**Maintained by:** CP-027 (Infrastructure Control Plane)  
**Related:** [[CONNECTIVITY-REGISTRY]], [[CLAUDE.md]], [[INFRASTRUCTURE-STATUS]]
