# Infrastructure Documentation Reference

**Master Document:** `_INFRASTRUCTURE/INFRASTRUCTURE.md`  
**Last Updated:** 2026-10-02  
**Status:** Production Ready

---

## Quick Links

- **[[INFRASTRUCTURE]]** — Master physical + network + compute + container + storage ontology
- **[[CLAUDE.md]]** — Global session context (includes outdated infrastructure notes)
- **[[REALITY]]** — Live audited truth ledger

---

## What's in INFRASTRUCTURE.md

The master infrastructure document is organized into these bracket sections:

```
[INFRASTRUCTURE]
├── [PHYSICAL_LAYER]          — Machines, storage, hardware
├── [COMPUTE_LAYER]           — CPU, GPU, Ollama, processes
├── [STORAGE_LAYER]           — Volumes, bind mounts, data locations
├── [DOCKER]                  — Containers, images, networks, volumes
├── [SERVICES]                — Neo4j, Qdrant, PostgreSQL, Redis, OmniRoute, etc.
├── [NETWORK]                 — Topology, routing, DNS
├── [TAILSCALE]              — VPN, nodes, connectivity
├── [CONNECTIVITY_TESTING]   — Evidence matrix with verified tests
├── [SECURITY]               — Auth, secrets, firewall
├── [OBSERVABILITY]          — Logging, metrics, health checks
├── [KNOWN_ISSUES_AND_FIXES] — Issue log with resolutions
└── [VERIFICATION_COMMANDS]  — Commands to re-verify infrastructure
```

---

## Key Findings (Oct 2, 2026)

**✅ Verified Working:**
- SSH: Passwordless auth to Mac Studio
- Neo4j: Port 7474, version 5.23.0
- Ollama: Port 11434, models available
- OmniRoute: **Port 3004** (not 20128 or 3000)
- Qdrant: Port 6333, accessible
- Redis: SSH tunnel (port 6379) — PONG verified
- PostgreSQL: SSH tunnel (port 5433) — port open, auth pending
- Tailscale: Direct LAN connection (100.87.214.70)

**🟡 Known Issues:**
- PostgreSQL: Role configuration needed
- Mac Air: Storage 98% full (5.3 GB available)
- NFS: Requires sudo (deferred to Syncthing)

**⚠️ Critical TODO:**
- Change Neo4j default password ("changeme" → Bitwarden)
- Clean Mac Air storage (target: 100+ GB free)
- Configure Syncthing for file sync

---

## Integration with Other Documents

**Update these documents to reference INFRASTRUCTURE.md:**

1. **CLAUDE.md**
   - Remove outdated port info (20128 → 3004)
   - Link to [[INFRASTRUCTURE]] for device inventory
   - Update device connectivity section

2. **Any onboarding guides**
   - Point to [[INFRASTRUCTURE]] for connectivity verification
   - Use verification commands from [VERIFICATION_COMMANDS]

3. **Service configuration docs**
   - Reference exact ports from [SERVICES] section
   - Link to connectivity evidence in [CONNECTIVITY_TESTING]

---

## How to Use This Document

### For Troubleshooting
→ Go to `[CONNECTIVITY_TESTING]` for evidence matrix  
→ Check `[KNOWN_ISSUES_AND_FIXES]` for known problems  
→ Run commands from `[VERIFICATION_COMMANDS]`

### For Architecture Decisions
→ Review `[NETWORK]` and `[DOCKER]` sections  
→ Understand service topology in `[SERVICES]`  
→ Check security model in `[SECURITY]`

### For Operations
→ Follow `[NEXT_ACTIONS]` for immediate/soon/planned work  
→ Use `[VERIFICATION_COMMANDS]` regularly  
→ Monitor `[OBSERVABILITY]` metrics

---

## Maintenance Cadence

- **Daily:** Run verification commands (health checks)
- **Weekly:** Review logs in OpenObserve
- **Monthly:** Update [KNOWN_ISSUES_AND_FIXES] with new findings
- **Quarterly:** Full infrastructure audit (update timestamps)

---

**Related:** [[CLAUDE.md]] · [[REALITY.md]] · [[SECURITY_CHECKLIST]] · [[DISASTER_RECOVERY]]
