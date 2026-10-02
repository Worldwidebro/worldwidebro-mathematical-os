---
type: infrastructure-control-ontology
canonical: true
authority: physical-storage-plane
version: 1.0
updated_at: 2026-10-02T00:00:00Z
source_of_truth: true
---

# FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY v1.0 — Physical Storage & Filesystem Control Plane

**The Company Brain lives on disk. This ontology models where digital material actually exists, how it moves, and what its physical dependencies are.**

The critical distinction:

```
[FILE_TREE]         [DISK_MAP]          [FILESYSTEM_REALITY]
    ↓                   ↓                       ↓
Logical              Physical                Verified
Organization         Topology                Actual State
```

---

## Core Principle: Path ≠ Disk ≠ Reality

```
[DECLARED_PATH]
        ≠
[OBSERVED_PATH]
        ≠
[VERIFIED_PATH]
```

Example:
- **Declared:** "CompanyBrain lives at /Volumes/LaCie/CompanyBrain"
- **Observed:** Mount command shows /Volumes/LaCie readable/writable
- **Verified:** File listing + integrity check confirms all data accessible

---

## [FILESYSTEM_COMPLETE_ARCHITECTURE] — 13 Domains

```
[FILESYSTEM_AND_DISKMAP]

├─ [FILESYSTEM]
│  ├── [FILE]
│  ├── [DIRECTORY]
│  ├── [SYMLINK]
│  ├── [MOUNT_POINT]
│  ├── [MOUNTED_VOLUME]
│  ├── [PERMISSIONS]
│  ├── [OWNER]
│  └── [GROUP]
│
├─ [FILE_TREE]
│  ├── [ROOT]
│  ├── [DIRECTORY_TREE]
│  ├── [PATH]
│  ├── [ABSOLUTE_PATH]
│  ├── [RELATIVE_PATH]
│  ├── [FILE_EXTENSION]
│  ├── [FILE_TYPE]
│  └── [TREE_DEPTH]
│
├─ [DISK]
│  ├── [PHYSICAL_DISK]
│  ├── [SSD]
│  ├── [HDD]
│  ├── [INTERNAL_STORAGE]
│  ├── [EXTERNAL_STORAGE]
│  └── [REMOVABLE_STORAGE]
│
├─ [VOLUME]
│  ├── [VOLUME]
│  ├── [APFS_VOLUME]
│  ├── [CONTAINER]
│  ├── [PARTITION]
│  ├── [MOUNTED_VOLUME]
│  └── [MOUNT_POINT]
│
├─ [STORAGE]
│  ├── [TOTAL_CAPACITY]
│  ├── [USED_SPACE]
│  ├── [FREE_SPACE]
│  ├── [AVAILABLE_SPACE]
│  ├── [ALLOCATED_SPACE]
│  ├── [RESERVED_SPACE]
│  ├── [SYSTEM_DATA]
│  └── [TEMPORARY_STORAGE]
│
├─ [DATA]
│  ├── [CODE]
│  ├── [KNOWLEDGE]
│  ├── [DOCUMENTS]
│  ├── [DATABASE]
│  ├── [MODELS]
│  ├── [CONTAINERS]
│  ├── [APPLICATION_DATA]
│  ├── [CONFIGURATION]
│  ├── [BACKUPS]
│  ├── [LOGS]
│  └── [ARTIFACTS]
│
├─ [DOCKER_STORAGE]
│  ├── [DOCKER_ENGINE]
│  ├── [IMAGE]
│  ├── [CONTAINER]
│  ├── [VOLUME]
│  ├── [BIND_MOUNT]
│  ├── [NETWORK]
│  ├── [LAYER]
│  └── [CONTAINER_DATA]
│
├─ [REPOSITORIES]
│  ├── [GITHUB_REPOSITORY]
│  ├── [LOCAL_REPOSITORY]
│  ├── [CLONE]
│  ├── [WORKTREE]
│  ├── [.GIT]
│  └── [BUILD_ARTIFACT]
│
├─ [KNOWLEDGE_STORAGE]
│  ├── [OBSIDIAN]
│  ├── [MARKDOWN]
│  ├── [WIKI_LINKS]
│  ├── [BRACKETED_FILES]
│  ├── [REGISTRIES]
│  └── [KNOWLEDGE_GRAPH_EXPORTS]
│
├─ [DATABASE_STORAGE]
│  ├── [NEO4J]
│  ├── [QDRANT]
│  ├── [SQL]
│  ├── [SUPABASE]
│  └── [DATABASE_BACKUPS]
│
├─ [FILE_INTELLIGENCE]
│  ├── [FILE_INDEX]
│  ├── [DIRECTORY_INDEX]
│  ├── [HASH]
│  ├── [METADATA]
│  ├── [DUPLICATE]
│  ├── [STALE_FILE]
│  ├── [ORPHAN_FILE]
│  └── [UNUSED_FILE]
│
├─ [FILE_LINEAGE]
│  ├── [CREATED_BY]
│  ├── [COPIED_FROM]
│  ├── [MOVED_FROM]
│  ├── [GENERATED_BY]
│  ├── [DERIVED_FROM]
│  ├── [SYNCED_FROM]
│  ├── [BACKED_UP_TO]
│  └── [RESTORED_FROM]
│
├─ [MIGRATION]
│  ├── [SOURCE]
│  ├── [DESTINATION]
│  ├── [TRANSFER]
│  ├── [SYNC]
│  ├── [VERIFICATION]
│  ├── [CHECKSUM]
│  └── [ROLLBACK]
│
└─ [REALITY]
   ├── [PATH_EXISTS]
   ├── [FILE_EXISTS]
   ├── [DIRECTORY_EXISTS]
   ├── [MOUNT_EXISTS]
   ├── [READABLE]
   ├── [WRITABLE]
   ├── [ACCESSIBLE]
   ├── [CHECKSUM_VERIFIED]
   ├── [BACKUP_VERIFIED]
   ├── [SYNC_VERIFIED]
   └── [STORAGE_STATE]
```

---

## [FILESYSTEM_HIERARCHY] — Logical vs Physical

```
[FILE_TREE]                         [DISK_MAP]
(Logical Organization)             (Physical Topology)

[[COMPANY_BRAIN]]                  [[MAC_STUDIO]]
    ├── /WHOAMI.md                     ├── [[INTERNAL_SSD]]
    ├── /INFRASTRUCTURE/               └── [[LACIE]]
    ├── /GITHUB/                           ├── [[COMPANY_BRAIN]]
    ├── /SECURITY/                        ├── [[DOCKER_DATA]]
    ├── /KNOWLEDGE/                       ├── [[REPOSITORIES]]
    └── /REGISTRIES/                      ├── [[MODELS]]
                                          ├── [[DATABASES]]
                                          └── [[BACKUPS]]

[[MAC_AIR]]
    ├── [[INTERNAL_SSD]]
    └── [[T7_SHIELD]]
        ├── [[COMPANY_BRAIN_WORKING]]
        ├── [[REPOSITORIES]]
        └── [[TRANSFER_STAGING]]
```

---

## [MOUNT_HIERARCHY] — Storage Path Resolution

```
[PHYSICAL_DISK]
      ↓
[VOLUME]
      ↓
[MOUNT_POINT]
      ↓
[PATH]
      ↓
[DIRECTORY]
      ↓
[FILE]
```

**Example:**

```
Physical Disk: T7 Shield (External USB)
      ↓
Volume: T7Shield
      ↓
Mount: /Volumes/T7Shield
      ↓
Path: /Volumes/T7Shield/Company\ Brain
      ↓
Directory: /Volumes/T7Shield/Company\ Brain/INFRASTRUCTURE
      ↓
File: /Volumes/T7Shield/Company\ Brain/INFRASTRUCTURE/OMNIROUTE.md
```

---

## [DOCKER_STORAGE_MAPPING] — Container Data Paths

```
[HOST_PATH]
      ↓
[BIND_MOUNT]
      ↓
[CONTAINER_PATH]
      ↓
[APPLICATION]
```

**Example:**

```
/Volumes/LaCie/omniroute
        ↓
    [BIND_MOUNT]
        ↓
     /app/data
        ↓
    [[OMNIROUTE]]
    (processes data in container at /app/data)
    (physically stored at /Volumes/LaCie/omniroute)
```

Separate from:

```
[DOCKER_VOLUME]
      ↓
[DOCKER_MANAGED_STORAGE]
      ↓
[CONTAINER]
```

---

## [REPOSITORY_STORAGE_GRAPH] — GitHub to Disk

```
[[GITHUB_REPOSITORY]]
        ↓
    [[GIT]]
        ↓
   [[CLONE]]
        ↓
[[LOCAL_REPOSITORY]]
        ↓
     [[PATH]]
        ↓
    [[DISK]]
```

**Example:**

```
GitHub: Worldwidebro-Vex
        ↓
Git clone
        ↓
Mac Studio: /Volumes/LaCie/Repositories/Worldwidebro-Vex
        ↓
[[SOURCE_CODE]]
[[DOCUMENTATION]]
[[TESTS]]
[[CONFIG]]
[[.GIT]]
[[BUILD_ARTIFACTS]]
```

---

## [FILE_METADATA_ONTOLOGY] — Per-File Reality

```yaml
file_id: FILE-WHOAMI-001

name: WHOAMI.md

path: /Volumes/LaCie/Company Brain/WHOAMI.md

type: markdown

category: identity

owner: Company Brain System

created_at: UNKNOWN
modified_at: 2026-10-02T18:43:00Z

size_bytes: 12457

hash:
  algorithm: SHA256
  value: NOT_STORED_IN_COMPANY_BRAIN

storage:
  device: [[MAC_STUDIO]]
  disk: [[LACIE]]
  volume: LaCie
  mount_point: /Volumes/LaCie

relationships:
  describes:
    - [[WHOAMI]]
  references:
    - [[WHERE_WE_ARE]]
    - [[SOURCE_OF_TRUTH]]
  created_by:
    - [[CLAUDE_CODE]]
  updated_by:
    - [[CLAUDE_CODE]]

backup:
  required: true
  backed_up_to: [[TIME_MACHINE]]
  last_backed_up: UNKNOWN
  verified: false

reality:
  exists: VERIFIED
  readable: VERIFIED
  writable: VERIFIED
  checksum_verified: NOT_TESTED
  backup_verified: NOT_TESTED
```

---

## [STORAGE_CAPACITY_MODEL] — Hierarchical Not Flat

```
[TOTAL_CAPACITY]
      │
      ├── [SYSTEM_DATA]
      │   ├── macOS
      │   ├── System Libraries
      │   └── Caches
      │
      ├── [APPLICATIONS]
      │   ├── Claude
      │   ├── Docker
      │   └── Tools
      │
      ├── [COMPANY_BRAIN]
      │   ├── Knowledge
      │   ├── Registries
      │   ├── Ontologies
      │   └── Exports
      │
      ├── [REPOSITORIES]
      │   ├── GitHub Clones
      │   ├── Forks
      │   └── Worktrees
      │
      ├── [DOCKER_DATA]
      │   ├── Images
      │   ├── Containers
      │   ├── Volumes
      │   └── Layers
      │
      ├── [DATABASES]
      │   ├── Neo4j
      │   ├── Qdrant
      │   ├── PostgreSQL
      │   └── Supabase
      │
      ├── [MODELS]
      │   ├── Ollama
      │   ├── qwen2.5-coder
      │   ├── hermes3
      │   └── llama3.1
      │
      ├── [BACKUPS]
      │   ├── Time Machine
      │   ├── External Backup
      │   ├── Snapshots
      │   └── Archives
      │
      └── [FREE]
```

---

## [FILE_LINEAGE_ONTOLOGY] — Prevents Accidental Destruction

Track every file's origin and copies:

```
[ORIGINAL]
    ↓
[COPY]
    ↓
[MODIFICATION]
    ↓
[DERIVATIVE]
    ↓
[BACKUP]
```

Relationships:

```
[[COPIED_FROM]]      — Exact copy
[[MOVED_FROM]]       — Relocated
[[GENERATED_BY]]     — Produced by agent/process
[[DERIVED_FROM]]     — Modified version
[[EXPORTED_FROM]]    — Exported to external format
[[IMPORTED_FROM]]    — Imported from external source
[[SYNCED_FROM]]      — Synchronized from another location
[[BACKED_UP_TO]]     — Backup copy location
[[RESTORED_FROM]]    — Restored from backup
[[DELETED_FROM]]     — Originally came from (deleted location)
```

**Example:**

```
Original: /Volumes/LaCie/Company Brain/WHOAMI.md
    ↓
Sync to: /Volumes/T7Shield/Company Brain/WHOAMI.md
    ↓
Backup to: Time Machine
    ↓
Export to: Obsidian Vault
    ↓
Retrieved from: GitHub Commit abc123def456
```

---

## [MIGRATION_ONTOLOGY] — Not Just "Copy Complete"

```
[MIGRATION]

SOURCE
   ↓
[DISCOVERY]
   ↓
[INVENTORY]
   ↓
[DEPENDENCY_ANALYSIS]
   ↓
[DESTINATION_PREPARATION]
   ↓
[TRANSFER]
   ↓
[CHECKSUM_VERIFICATION]
   ↓
[STRUCTURE_VERIFICATION]
   ↓
[APPLICATION_VERIFICATION]
   ↓
[CONNECTIVITY_TEST]
   ↓
[CUTOVER]
   ↓
[OLD_LOCATION_STATUS]
   ├── [KEPT_AS_BACKUP]
   ├── [ARCHIVED]
   └── [DESTROYED]
   ↓
[BACKUP_VERIFICATION]
   ↓
[ROLLBACK_PLAN]
   ↓
[MIGRATION_COMPLETE]
```

**Critical distinction:**

```
[FILES_COPIED]
      ≠
[MIGRATION_COMPLETE]
```

Migration only complete when:
- ✅ Files transferred with verified checksums
- ✅ Directory structure intact
- ✅ Permissions preserved
- ✅ All applications can access data
- ✅ Network connectivity verified
- ✅ Backups secured
- ✅ Rollback path prepared

---

## [DISK_INTELLIGENCE_AGENT] — Automated Scanning

```
[[DISK_INTELLIGENCE_AGENT]]

├── [[SCAN_DISKS]]
├── [[SCAN_VOLUMES]]
├── [[SCAN_MOUNTS]]
├── [[ENUMERATE_DIRECTORIES]]
├── [[ENUMERATE_FILES]]
├── [[CALCULATE_SIZES]]
├── [[COMPUTE_HASHES]]
├── [[FIND_DUPLICATES]]
├── [[FIND_ORPHANS]]
├── [[FIND_STALE_FILES]]
├── [[FIND_LARGE_FILES]]
├── [[FIND_UNUSED_DATA]]
├── [[MAP_APPLICATION_DATA]]
├── [[MAP_DOCKER_DATA]]
├── [[MAP_REPOSITORIES]]
├── [[MAP_KNOWLEDGE_STORAGE]]
├── [[MAP_DATABASE_STORAGE]]
└── [[UPDATE_DISK_MAP]]
```

Produces:

```
[[FILESYSTEM_REGISTRY]]
[[STORAGE_CAPACITY_REPORT]]
[[FILE_LINEAGE_GRAPH]]
[[DUPLICATE_MANIFEST]]
[[ORPHAN_FILES_LIST]]
[[DISK_HEALTH_REPORT]]
```

---

## [FILESYSTEM_CONNECTIVITY_TESTING] — Verification

Every critical path must have a test:

```yaml
test_id: FS-CONNECTIVITY-001

name: CompanyBrain LaCie Access

target_path: /Volumes/LaCie/Company Brain

operations:
  - read
  - write
  - list_directory
  - read_file
  - write_file

expected:
  mounted: true
  readable: true
  writable: true
  latency: < 100ms

actual:
  mounted: UNKNOWN
  readable: UNKNOWN
  writable: UNKNOWN
  latency: UNKNOWN

status: NOT_TESTED

verification:
  mount_check: []
  read_test: []
  write_test: []
  integrity_check: []

timestamp: UNKNOWN
evidence: UNKNOWN
```

---

## [MASTER_PHYSICAL_STORAGE_GRAPH] — Complete Picture

```
                         [[COMPANY_BRAIN]]
                                │
                                ↓
                         [[FILESYSTEM]]
                                │
                 ┌──────────────┴──────────────┐
                 ↓                             ↓
           [[FILE_TREE]]                 [[DISK_MAP]]
           (Logical)                    (Physical)
                 │                             │
                 ↓                         [[DISKS]]
          [[DIRECTORIES]]                     │
                 │                         [[VOLUMES]]
                 ↓                             │
              [[FILES]]                    [[MOUNTS]]
                 │                             │
                 └──────────────┬──────────────┘
                                ↓
                         [[STORAGE_PATH]]
                                │
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
        [[DOCKER]]        [[REPOSITORIES]]    [[KNOWLEDGE]]
        [[VOLUMES]]       [[GITHUB_CLONES]]    [[OBSIDIAN]]
        [[BIND_MOUNTS]]   [[WORKTREES]]       [[MARKDOWN]]
             │                  │                  │
        [[OMNIROUTE]]       [[GITHUB]]          [[WIKI]]
        [[CLAUDE_CODE]]     [[CODE]]          [[BRACKETS]]
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ↓
                         [[DATABASE_STORAGE]]
                         [[MODEL_STORAGE]]
                                ↓
                         [[FILE_LINEAGE]]
                                ↓
                           [[BACKUPS]]
                                ↓
                      [[FILESYSTEM_REALITY]]
                                ↓
                    [[KNOWLEDGE_GRAPH]]
                                ↓
                           [[CLAUDE]]
                                ↓
                         [[OMNIROUTE]]
                                ↓
                         [[GITHUB_ACTIONS]]
                                ↓
                      [[DEPLOYMENT]]
                                ↓
                    [[EXECUTABLE_EVIDENCE]]
                                ↓
                         [[REALITY]]
```

---

## [PHYSICAL_TO_KNOWLEDGE_CHAIN]

The complete chain from disk to intelligence:

```
PHYSICAL DISK
     ↓
VOLUME
     ↓
MOUNT_POINT
     ↓
FILESYSTEM_PATH
     ↓
DIRECTORY
     ↓
FILE
     ↓
CONTENT (bytes)
     ↓
PARSED (markdown/YAML/JSON)
     ↓
WIKI_LINK [[ENTITY]]
     ↓
KNOWLEDGE_GRAPH_NODE
     ↓
CLAUDE (reasoning)
     ↓
OMNIROUTE (model routing)
     ↓
AGENT (execution)
     ↓
TASK (work unit)
     ↓
CODE (GitHub)
     ↓
DEPLOYMENT (Docker/Vercel)
     ↓
EXECUTABLE_EVIDENCE
     ↓
VERIFIED_REALITY
     ↺ (feedback loop)
```

---

## [COMPANY_BRAIN_STORAGE_ONTOLOGY] — Your Actual Infrastructure

```
[[MAC_STUDIO]]
│
├── [[INTERNAL_SSD]]
│   ├── macOS
│   ├── Applications (Docker, CLI tools)
│   └── System Data
│
└── [[LACIE_EXTERNAL]]
    ├── [[COMPANY_BRAIN]]
    │   ├── [[KNOWLEDGE]] (Obsidian vault)
    │   ├── [[REGISTRIES]] (YAML registries)
    │   ├── [[ONTOLOGIES]] (master ontologies)
    │   └── [[EXPORTS]] (graph exports)
    │
    ├── [[DOCKER_DATA]]
    │   ├── Neo4j volumes
    │   ├── Qdrant volumes
    │   ├── PostgreSQL data
    │   ├── Redis persistence
    │   └── OmniRoute storage
    │
    ├── [[REPOSITORIES]]
    │   ├── GitHub clones (900+)
    │   ├── Worktrees
    │   └── Build artifacts
    │
    ├── [[MODELS]]
    │   ├── qwen2.5-coder:14b
    │   ├── hermes3
    │   ├── llama3.1:8b
    │   └── Custom models
    │
    └── [[BACKUPS]]
        ├── Time Machine
        ├── Manual snapshots
        └── Archives

[[MAC_AIR]]
│
├── [[INTERNAL_SSD]]
│   ├── macOS
│   └── Applications
│
└── [[T7_SHIELD_EXTERNAL]]
    ├── [[COMPANY_BRAIN_WORKING]] (active copy)
    ├── [[REPOSITORIES_STAGING]] (subset)
    └── [[TRANSFER_STAGING]] (sync intermediary)
```

---

## [FILESYSTEM_REALITY] — Source of Truth

Not a score. Observable facts:

```
[FILESYSTEM_REALITY]

├── [DIRECTORY_EXISTS]
├── [FILE_EXISTS]
├── [READABLE]
├── [WRITABLE]
├── [ACCESSIBLE]
├── [MOUNTED]
├── [TOTAL_SIZE]
├── [USED_SIZE]
├── [FREE_SIZE]
├── [FILE_COUNT]
├── [DIRECTORY_COUNT]
├── [HASH_VERIFIED]
├── [BACKUP_VERIFIED]
├── [SYNC_VERIFIED]
├── [LAST_SCANNED]
└── [LAST_MODIFIED]
```

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[OMNIROUTE_MASTER_ONTOLOGY.md]] · [[SECRETS_AND_AUTH_MASTER_ONTOLOGY.md]] · [[GITHUB_MASTER_ONTOLOGY.md]]

**Physical storage control plane v1.0: Where every file lives, how data moves, and what physical realities constrain the entire Company Brain.**

