---
id: CP-027
aliases: ['INFRASTRUCTURE', 'INFRA-001']
tags: ['infrastructure', 'control-plane', 'cp-027', 'engineering']
status: LIVE_AUDITED
updated: 2026-09-06
---

[[STARTHERE]] | [[REALITY]] | [[CLAUDE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[00-CONSTITUTION]] | [[56-ENGINEERING/INFRASTRUCTURE/START-HERE|START-HERE]]

# INFRASTRUCTURE

## ID INFRA-001

## Status LIVE / AUDITED

## Purpose Describe the infrastructure required to operate Company Brain.
This master control plane document provides the canonical map and authoritative control interface for all physical, virtual, network, compute, storage, data, runtime, deployment, security, resilience, observability, and governance infrastructure supporting the Company Brain autonomous corporate operating system.

---


## Infrastructure Domain Hubs (Obsidian Graph Nodes)
- Core: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] & [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY]]
- Compute: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|02_COMPUTE]]
- Storage: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|03_STORAGE]]
- Network: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|04_NETWORK]]
- Cloud: [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD|05_CLOUD]]
- Data: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|06_DATA]]
- Runtime: [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|07_RUNTIME]]
- Deployment: [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|08_DEPLOYMENT]]
- Observability: [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|09_OBSERVABILITY]]
- Security: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|10_SECURITY]]
- Resilience: [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|11_RESILIENCE]]
- Cost & Governance: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|12_COST-GOVERNANCE]]

---

## Current Reality

### Compute
- **Mac Studio M4 Max (`DEV-MAC-STUDIO-001`):** Primary inference server, database host, and control plane node. 12-core M4 Max (8 performance, 4 efficiency cores), 32-core GPU, 16-core Neural Engine, 36GB Unified Memory (410 GB/s bandwidth). Tailscale IP: `100.87.214.70`. Local LAN IP: `192.168.1.11`.
- **MacBook Air (`DEV-MACBOOK-AIR-001`):** Mobile engineering node and secondary inference worker. 8-core Apple Silicon (4 performance, 4 efficiency), 8-core GPU, 16GB Unified Memory. Tailscale IP: `100.121.17.63`.
- **OmniRoute Mesh Node (`DEV-OMNIROUTE-001`):** Tailscale-connected gateway node `omniroute-6da9315f` listening on `100.80.229.113:20128`.
- **Other hosts / Edge Compute:** Vercel serverless edge workers executing Node.js 22.x/24.x runtimes across global edge locations for 95 deployed venture sites.

### Storage
- **Internal SSD:**
  - Mac Studio: 512GB APFS internal SSD (194GB used, 318GB free) hosting macOS Sequoia 15.x, system runtime libraries, and Docker VM virtual disk (`~/.docker`).
  - MacBook Air: 228GB APFS internal SSD (194GB used, 34GB free) hosting primary engineering workspace and active Git repositories.
- **External storage:**
  - **LaCie 4TB Thunderbolt/USB-C HDD (`DEV-DRIVE-LACIE-4TB`):** Dedicated to Mac Studio at `/Volumes/LaCie`. Primary host for all production persistent databases (`/Volumes/LaCie/neo4j`, `/Volumes/LaCie/qdrant`, `/Volumes/LaCie/postgres`), database dumps, and model staging.
  - **Samsung T7 Shield 2TB External NVMe SSD (`DEV-DRIVE-T7-2TB`):** Dedicated to MacBook Air at `/Volumes/T7 Shield`. 1.8TB usable capacity (889GB used, 911GB free) hosting local model weights and layer cache.
- **Backup storage:**
  - Daily automated SQL/database dumps to `/Volumes/LaCie/postgres/backups` and `/Volumes/LaCie/backups/neo4j`.
  - Weekly off-device replication mirror to `/Volumes/T7 Shield/cold_archive`.

### Network
- **Internet:** High-speed residential fiber broadband with dynamic public IPv4, full IPv6 egress, and cellular failover tethering capability.
- **Tailscale:** WireGuard-based private mesh overlay network (v1.98.9) spanning CIDR `100.64.0.0/10`. Zero-trust point-to-point encrypted mesh connecting Mac Studio (`100.87.214.70`), MacBook Air (`100.121.17.63`), and OmniRoute node (`100.80.229.113`).
- **DNS:** Tailscale MagicDNS (`*.ts.net`) for internal service resolution; Cloudflare / Registrar for external DNS; Vercel DNS managing edge deployments.
- **Ports:** Canonical ports locked to local interfaces: Neo4j (`7474`, `7687`), Qdrant (`6333`), PostgreSQL (`5432`/`5433`), Redis (`6379`), LiteLLM (`4000`), Exo MLX (`52415`), OmniRoute (`20128`), Open WebUI (`3010`), Grafana (`3011`), Langfuse (`3003`).
- **Proxies:** FastMCP server bridge, Docker bridge routing (`172.18.0.0/16`), and LiteLLM OpenAI-compatible reverse proxy.

### Runtime
- **Docker:** Docker engine managed on Mac Studio via dedicated Docker context `macstudio` reached over SSH/Tailscale.
- **Compose:** Multi-service application compose projects on Mac Studio (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`).
- **Kubernetes/K3s:** Lightweight edge container orchestration planned for multi-node Apple Silicon failover.
- **Native services:** Native Apple Silicon MLX inference engine (`exo`) running as a standalone Python process on port `:52415`; Bitwarden CLI (`bw`) at `/opt/homebrew/bin/bw`.

### Databases
- **PostgreSQL:** PostgreSQL 16 operational database running in Docker container `postgres` on port `:5432`, persisted to `/Volumes/LaCie/postgres/data`.
- **Neo4j:** Neo4j Community/Enterprise 5.x graph database (`civos_neo4j`) on ports `:7474` (HTTP) and `:7687` (Bolt), persisted to `/Volumes/LaCie/neo4j/data`.
- **Qdrant:** Qdrant vector database running in Docker container `civos_qdrant` on port `:6333`, persisted to `/Volumes/LaCie/qdrant/storage`.
- **Redis:** Redis 7.x in-memory cache and state store on port `:6379`.
- **MinIO:** S3-compatible local object storage declared for cold asset archival and artifact staging.

### AI Infrastructure
- **Model serving:** Native MLX model execution via `exo` (`http://100.87.214.70:52415/v1`), serving `mlx-community/Qwen3.6-35B-A3B-5bit`. Ollama was decommissioned and replaced on 2026-07-17.
- **LiteLLM:** Proxy and model abstraction layer running in container `civos_litellm` on port `:4000`, providing provider routing, fallback chains (`qwen-heavy` -> `claude-sonnet`, `qwen-fast` -> `claude-haiku`), and token usage logging.
- **OmniRoute:** AI provider gateway, traffic controller, and MCP Hub (`DEV-OMNIROUTE-001`) listening on port `:20128`.
- **Inference nodes:** Mac Studio M4 Max (primary execution node); MacBook Air M-series (secondary execution worker).
- **Model registry:** Machine-readable catalog linking models to tasks, quantization levels, and memory footprints.

### Application Infrastructure
- **Vercel:** Cloud edge platform hosting 95 production sites across Node.js 22.x/24.x runtimes.
- **APIs:** REST, GraphQL, and MCP endpoints linking edge applications with local company graph and vector data.
- **Backend services:** FastMCP server (`_MCP/fastmcp_server.py`) running in virtualenv `~/.venv/company-brain` (Python 3.12).
- **Frontend services:** Open WebUI (`:3010`), Grafana dashboards (`:3011`), and venture web portals.

### Observability
- **Metrics:** Host and container telemetry, CPU/GPU utilization, and memory pressure monitoring.
- **Logs:** Docker container stdout/stderr JSON stream logging and system logs.
- **Traces:** Langfuse container `civos_langfuse` running on port `:3003` (currently idle pending callback enablement in LiteLLM).
- **Alerts:** Automated threshold checks for memory pressure, container health, and storage exhaustion.

### Security
- **Identity:** NIST SP 800-207 Zero Trust multi-subject architecture treating humans, devices, applications, servers, and agents as subjects.
- **Secrets:** Bitwarden CLI (`/opt/homebrew/bin/bw`) zero-trust ephemeral secret injection. Zero plaintext secrets in version control.
- **Certificates:** Automated Let's Encrypt certificates via Vercel edge; Tailscale TLS machine certificates; internal TLS.
- **Network security:** Strict firewall policies, zero unauthenticated public ingress ports, end-to-end WireGuard encryption.

### Backup
- **Backup locations:** Primary backup target `/Volumes/LaCie/backups/`; secondary target `/Volumes/T7 Shield/cold_archive/`.
- **Schedules:** Daily at 02:00 (Neo4j dump), 03:00 (PostgreSQL pg_dump), weekly on Sunday (Qdrant snapshots, cross-disk mirror).
- **Restore procedures:** Documented and verified container restoration scripts in `11_RESILIENCE/RESTORE.md`.

### Disaster Recovery
- **RTO (Recovery Time Objective):** < 60 minutes for complete cold-start service reconstitution.
- **RPO (Recovery Point Objective):** < 15 minutes for operational transaction databases; < 24 hours for cold analytical graphs.
- **Recovery sequence:** Hardware promotion -> Volume mount verification -> Core network/Tailscale -> Database containers -> Inference engines -> Gateways -> Health check probes.

### Costs
- **Hardware:** Amortized Mac Studio + MacBook Air + storage drives = $165.00/mo.
- **Hosting:** Vercel Pro ($20.00/mo) + GitHub Team ($4.00/mo) + Domains ($12.00/mo) = $36.00/mo.
- **Storage:** Amortized local physical media ($15.00/mo included in hardware).
- **Bandwidth & Power:** Residential electricity consumption ~120 kWh = $28.00/mo.
- **APIs & Inference:** Frontier model fallbacks (Claude 3.5 Sonnet / Haiku, OpenAI, DeepSeek) = ~$80.00/mo.
- **Total Monthly Infrastructure TCO:** **$309.00/mo**.

---

## Dependencies
- Tailscale mesh availability for multi-node communication.
- Docker daemon responsiveness on Mac Studio.
- Physical Thunderbolt connection to LaCie 4TB drive for database persistence.
- Apple Silicon Metal 3 drivers for MLX inference acceleration.
- Vercel API and Edge CDN for external web traffic delivery.

## Single Points of Failure
1. **Mac Studio Hardware (`DEV-MAC-STUDIO-001`):** Hosts all production databases and primary local LLM execution.
2. **LaCie 4TB Drive (`DEV-DRIVE-LACIE-4TB`):** Single physical drive storing Neo4j, Qdrant, and PostgreSQL active data directories.
3. **Sole Human Operator:** Bus factor of 1 for strategic authorization, secret unlocking, and physical hardware interventions.

## Known Failures
- **Crash-Looping Container:** Container `t7shield-neo4j-1` is crash-looping continuously due to an invalid Neo4j 4.x configuration parameter (`dbms.connectors.default.advertised.address`). The active canonical database is `civos_neo4j`.
- **LiteLLM Broken Route:** The legacy embeddings route pointing to Ollama nomic-embed-text is broken following the Ollama deprecation.
- **Disconnected Observability Callback:** Langfuse is running healthy on port `:3003` but receiving zero trace telemetry because the `success_callback: ["langfuse"]` setting is missing from LiteLLM's configuration.

## Technical Debt
- **Docker Compose Stack Clutter:** Four overlapping compose projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`) running concurrently on Mac Studio with duplicated service definitions.
- **Hardcoded Default Credentials:** Development credentials (`neo4j/changeme`, `admin/changeme`) in local compose definitions.
- **Absence of IaC Automation:** Infrastructure is currently maintained through semi-manual scripts rather than fully automated Terraform/OpenTofu declarations.

## Infrastructure Decisions
- **ADR-001:** Replaced Ollama with native Apple MLX `exo` for superior token generation throughput and unified memory bandwidth utilization.
- **ADR-002:** Designated Mac Studio + LaCie 4TB as the canonical database host; MacBook Air + T7 Shield as the mobile engineering worker.
- **ADR-003:** Standardized on Tailscale private mesh for all node-to-node communication, closing all public ingress ports.
- **ADR-004:** Adopted NIST SP 800-204C DevSecOps separation of concerns, decoupling IaC, PaC, and OaC into distinct layers.
- **ADR-005:** Implemented the Anti-Fake-Completion Reality Framework requiring empirical runtime verification before declaring systems operational.

## Infrastructure Risks
- **RSK-001 (Availability):** Unplanned downtime of Mac Studio halts internal agent reasoning and graph queries.
- **RSK-002 (Capacity):** Memory exhaustion on 36GB unified RAM when concurrently executing large LLMs and deep graph traversal queries.
- **RSK-003 (Security):** Credential compromise if unencrypted environment variables or Bitwarden session tokens leak.

## Owners
- **Infrastructure Authority:** Infrastructure Control Plane (`CP-027`).
- **Operating Executive:** Sovereign Operator / Founder.
- **Technical Custodian:** Antigravity Autonomous Infrastructure Engineering Agent.

## Evidence
- `CLAUDE.md`: Live-audited runtime state and Docker context verification.
- `REALITY.md`: Verified facts VF-001 through VF-008.
- `_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml`: 95 active deployed Vercel sites.
- `_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml`: Master registry declarations.

## Last Verified
- **Verification Timestamp:** `2026-09-05T10:45:00Z`
- **Verification Method:** Live Docker context probe via `docker --context macstudio`, Tailscale mesh status ping, and filesystem volume inspection.
- **Verification Status:** **AUDITED / LIVE REALITY**

---

## Machine-Readable Infrastructure Registries (`_REGISTRIES/`)

| Registry | Description | Link |
|---|---|---|
| `network_registry.json` | Network topology, IP allocations, Tailscale nodes, and ingress rules | [[_REGISTRIES/network_registry.json|network_registry.json]] |
| `database_registry.json` | Database instances, schemas, replication topology, and connection URIs | [[_REGISTRIES/database_registry.json|database_registry.json]] |
| `storage_registry.json` | Physical volumes, mount points, storage tiers, and capacity allocations | [[_REGISTRIES/storage_registry.json|storage_registry.json]] |
| `cloud_registry.json` | Cloud providers, accounts, regions, edge endpoints, and exit paths | [[_REGISTRIES/cloud_registry.json|cloud_registry.json]] |
| `infrastructure_registry.json` | Comprehensive physical and virtual machine inventory | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]] |
| `INFRASTRUCTURE_REGISTRY.yaml` | Canonical system infrastructure specification and deployment states | [[_REGISTRIES/INFRASTRUCTURE_REGISTRY.yaml|INFRASTRUCTURE_REGISTRY.yaml]] |
| `infrastructure_dependency_registry.json` | Cross-system service dependencies and critical path graphs | [[_REGISTRIES/infrastructure_dependency_registry.json|infrastructure_dependency_registry.json]] |
| `infrastructure_cost_registry.json` | Component-level hosting, hardware, and operational costs | [[_REGISTRIES/infrastructure_cost_registry.json|infrastructure_cost_registry.json]] |
| `infrastructure_risk_registry.json` | Single points of failure, failover risks, and disaster mitigations | [[_REGISTRIES/infrastructure_risk_registry.json|infrastructure_risk_registry.json]] |
