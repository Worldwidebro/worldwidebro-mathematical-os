---
id: DOC-01-TOPO-001
aliases: ['INFRASTRUCTURE-TOPOLOGY']
tags: ['topology', 'network-map', 'hardware-topology', 'core']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] | [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]

# Infrastructure Topology

> **Authority:** CP-027  
> **Status:** LIVE  
> **Updated:** 2026-09-05

## 1. Physical & Network Topology Diagram
```mermaid
graph TD
    subgraph WAN [Public Edge]
        Internet((Public Internet))
        Cloudflare[Cloudflare DNS]
        VercelEdge[Vercel Edge Network - 95 Sites]
        Internet --> Cloudflare
        Cloudflare --> VercelEdge
    end

    subgraph Mesh [Tailscale WireGuard Mesh: 100.64.0.0/10]
        TS_Air[aces-macbook-air-1<br/>100.121.17.63]
        TS_Studio[mac-studio<br/>100.87.214.70]
        TS_Omni[omniroute-node<br/>100.80.229.113:20128]
        TS_Air <-->|Encrypted WireGuard| TS_Studio
        TS_Air <-->|Encrypted WireGuard| TS_Omni
        TS_Studio <-->|Encrypted WireGuard| TS_Omni
    end

    subgraph Studio_Node [Mac Studio M4 Max - Primary Host]
        DockerEngine[Docker Engine<br/>Context: macstudio]
        ExoNative[exo Native MLX<br/>Port 52415]
        LaCieStorage[(LaCie 4TB HDD<br/>/Volumes/LaCie)]
        
        DockerEngine --> CivosNeo4j[civos_neo4j<br/>Ports 7474/7687]
        DockerEngine --> CivosQdrant[civos_qdrant<br/>Port 6333]
        DockerEngine --> CivosPostgres[postgres<br/>Port 5432]
        DockerEngine --> CivosLiteLLM[civos_litellm<br/>Port 4000]
        DockerEngine --> CivosLangfuse[civos_langfuse<br/>Port 3003]
        DockerEngine --> T7Grafana[t7shield-grafana-1<br/>Port 3011]
        DockerEngine --> CivosWebUI[civos_webui<br/>Port 3010]
        
        CivosNeo4j --> LaCieStorage
        CivosQdrant --> LaCieStorage
        CivosPostgres --> LaCieStorage
    end

    subgraph Air_Node [MacBook Air - Mobile Workstation]
        T7Storage[(Samsung T7 Shield 2TB<br/>/Volumes/T7 Shield)]
        AntigravityIDE[Antigravity IDE]
        LocalRepos[Local Brain Repos]
    end

    TS_Studio --> DockerEngine
    TS_Studio --> ExoNative
    TS_Air --> AntigravityIDE
```

## Connected Documents & Registries
- Core Subsystem Hub: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Reality Verification: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY|INFRASTRUCTURE-REALITY.md]]
- Infrastructure Registry: [[_REGISTRIES/infrastructure_registry.json|infrastructure_registry.json]]
- Compute Architecture: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Storage Architecture: [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- Network Architecture: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
