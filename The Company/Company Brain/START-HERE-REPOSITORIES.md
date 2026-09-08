[[STARTHERE]] | [[REALITY]] | [[00_RESPECT/RESPECT|RESPECT]] | [[13-REPOSITORIES]] | [[14-CAPABILITIES]] | [[INDEX]]

# Repository Intelligence & Capability Supply Chain

> **Canonical Guide ID:** `GUIDE-REP-001`  
> **Master Legend:** [[STARTHERE]]  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Status:** ACTIVE ORIENTATION — Updated 2026-09-06

## Purpose
Governs the discovery, AST code verification, dependency mapping, and capability extraction across the entire repository universe (893 owned repositories + 904 external capability supply chain repositories).

## Master Inventories & Canonical Registries
- **Owned Repositories Master Inventory:** [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY.md]] (893 repos audited for AST code reality)
- **External Capability Universe Master:** [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md]] (904 external starred repos organized across 10 layers)
- **Canonical External Capability Supply Chain:** [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] (Wikidata QID-grounded nodes: OpenObserve, AirLLM, Utopia, Needle, Vaultwarden)
- **Capability Gap Matrix:** [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml]] (Owned vs external vs venture gaps)
- **Owned Repositories by Sector:** [[_REGISTRIES/repositories-by-sector.yaml]] (893 owned repos mapped across 35 sectors)
- **External Capabilities by Sector:** [[_REGISTRIES/external-capabilities-by-sector.yaml]] (904 starred repos with 31.3M+ stars mapped across 35 sectors)
- **Code Reality Registry:** [[_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json]] (177 code-verified vs 618 venture paperwork)

## Key Anchor Technologies in Supply Chain
1. **OpenObserve (`EXT-OBS-001`)** — Rust-based cloud-native telemetry replacing Datadog at 140x lower cost.
2. **AirLLM (`EXT-INF-002`)** — Layer-wise local 70B+ inference streaming from SSD on Mac Studio.
3. **Needle (`EXT-RAG-003`)** — Ultra-fast multimodal retrieval engine and RAG pipeline.
4. **Utopia (`EXT-DEC-004`)** — Decentralized autonomous compute and peer-to-peer execution.
5. **Vaultwarden** — Lightweight zero-knowledge secrets vault compatible with Bitwarden CLI.

## Operational Rules for Repositories
1. **Reuse First (`ANTIGRAVITY.md` Rule #2)**: Never write new code without searching the 177 code-bearing repos or the 904 external capability universe.
2. **Code Reality Over Names**: Never assume a repository has working code from its title or README; check `OWNED_REPO_CODE_REALITY.json`.
3. **Keep Graph Current**: After modifying code files, run `graphify update .` to keep the AST knowledge graph synchronized.
