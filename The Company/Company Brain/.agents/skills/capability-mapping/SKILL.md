---
name: capability-mapping
description: Maps verified software libraries, components, and tools to business and technical capabilities across the canonical registries. Use when updating CAPABILITY_REGISTRY.yaml, calculating capability gaps, or linking venture requirements to code.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Capability Mapping Skill

This skill governs the canonical translation between venture business requirements and concrete code implementations.

## Rules of Capability Mapping

1. **Capabilities are Bridges, Not Repositories**:
   - Never treat a repository name or directory as a capability.
   - A repository *implements* one or more capabilities (e.g., `OWN-PUB-0875` implements `CAP-001 Strategy & Planning`).

2. **Ground Truth Dependency Mapping**:
   - Map technical capabilities from verified library dependencies:
     - `AI_ML`: `openai`, `langchain`, `anthropic`, `torch`, `transformers`, `llama-index`, `@google/genai`
     - `Frontend`: `react`, `next`, `vue`, `svelte`, `tailwindcss`, `vite`
     - `API_Backend`: `fastapi`, `flask`, `express`, `django`, `nestjs`
     - `Database`: `prisma`, `pg`, `sqlalchemy`, `mongodb`, `redis`, `supabase`
     - `Authentication`: `next-auth`, `jsonwebtoken`, `bcrypt`, `clerk`, `supabase-auth`
     - `DevOps_Infrastructure`: `@aws-sdk`, `docker`, `terraform`, `kubernetes`
     - `Data_Analytics`: `pandas`, `numpy`, `polars`, `dbt`, `scipy`
     - `Blockchain_Web3`: `ethers`, `web3`, `solana`, `viem`, `wagmi`

3. **Registry Synchronization**:
   - Update `_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml` and recalculate `CAPABILITY_GAP_REPORT.yaml` whenever dependencies change.
   - Maintain stable IDs (`CAP-001` through `CAP-012` for business, `CAP-TECH-*` for technical).
