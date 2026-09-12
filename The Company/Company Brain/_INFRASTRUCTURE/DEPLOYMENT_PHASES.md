[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

---
id: INFRA-DEPLOYMENT_PHASES
title: "Infrastructure Deployment Phases Specification"
tags: [infrastructure, deployment, phases, rollout]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_INFRASTRUCTURE/README|Operational Infrastructure]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[CLAUDE]]

# Company Brain Deployment Phases
**Status: IN PROGRESS (2026-09-02)**

## QUICK STATUS

| Phase | Task | Status | ETA |
|-------|------|--------|-----|
| 1 | Deploy Neo4j, Qdrant, PostgreSQL (Mac Studio) | **BLOCKED** - needs SSH | 30 min |
| 2 | Pull models to T7 Shield (MacBook Air) | **IN PROGRESS** ✅ | 13 hours |
| 3 | Install Exo distributed inference | **READY** | 20 min |
| 4 | Deploy observability stack | **READY** | 1 hour |

## OMNIROUTE DEEP DIVE

**GitHub**: https://github.com/diegosouzapw/OmniRoute

### What is OmniRoute?
- **Type**: API Service Router / Load Balancer
- **Purpose**: Routes requests to backend services intelligently
- **Running On**: 100.80.229.113:8080 (Tailscale network)
- **Status**: Online and responsive

### Why does Company Brain need OmniRoute?
- Route requests to different model runtimes (Ollama, Exo, AirLLM)
- Load balance across Mac Studio and MacBook Air
- Intelligent failover between services
- Gateway for agents to access models via single endpoint

### Configuration Needed:
```yaml
routes:
  /ollama:
    backend: http://100.87.214.70:11434  # Mac Studio Ollama
    method: round-robin
    
  /exo:
    backend: [100.87.214.70:5000, 100.121.17.63:5000]  # Exo nodes
    method: least-connections
    
  /airllm:
    backend: http://100.87.214.70:8001  # AirLLM batch
    method: static
```

## PHASE-BY-PHASE

### PHASE 1: Databases (Mac Studio)
**BLOCKED**: Need SSH access to Mac Studio
**Commands for you to run**:
```bash
ssh acebless@100.87.214.70
cd ~/Documents/The\ Company/Company\ Brain/_INFRASTRUCTURE
docker-compose up -d
docker-compose ps
```

### PHASE 2: Models (MacBook Air - T7 Shield)
**IN PROGRESS**: qwen2.5:32b pulling (~4.8 hours remaining)
**Status**: 0% → tracking in `/tmp/model_pull_32b.log`
**Next**: qwen2.5:72b (~10 hours after 32b completes)

### PHASE 3: Exo (Distributed Inference)
```bash
# Mac Studio
ssh acebless@100.87.214.70 "pip install exo && python -m exo --node-host 100.87.214.70 &"

# MacBook Air
pip install exo && python -m exo --node-host 100.121.17.63 &
```

### PHASE 4: Observability
```bash
# On Mac Studio
docker run -d -p 9090:9090 prom/prometheus
docker run -d -p 3000:3000 grafana/grafana
pip install langfuse && langfuse-server
```

## KEY PASSWORDS NEEDED

- [ ] Mac Studio SSH password / key
- [ ] Omniroute credentials
- [ ] Neo4j password (change from 'changeme')
- [ ] Grafana password (admin:admin)

## TAILSCALE ✅ VERIFIED

```
100.87.214.70    mac-studio         ✅ ACTIVE
100.121.17.63    macbook-air        ✅ ONLINE
100.80.229.113   omniroute          ✅ ONLINE
```

All devices connected and communicating via Tailscale private mesh network.

## STORAGE TOPOLOGY (T7 Shield for Models)

- **Mac Studio**: LaCie 4TB → Databases
- **MacBook Air**: T7 Shield 1.8TB → Large Models
- **Question**: Move entire Company Brain to T7 Shield for shared storage?

---

## Infrastructure Context & Links
- **Engineering Hub:** [[56-ENGINEERING/README|56-ENGINEERING]]
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Runtime State:** [[CLAUDE]]
- **Capabilities Matrix:** [[14-CAPABILITIES/CAPABILITIES_INDEX]]
