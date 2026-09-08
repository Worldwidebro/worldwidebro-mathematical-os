[[STARTHERE]] | [[REALITY]] | [[ECONOMIC-REALITY]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

# SYSTEM-REALITY.md — The Technical Infrastructure Truth Ledger

> **Canonical Document ID:** `DOC-SYS-001`  
> **Authority:** Infrastructure Control Plane (CP-027) & Model Control Plane (CP-007)  
> **Rule:** *An infrastructure component does not exist because it is configured; it exists when it passes live network probes.*  
> **Parent Control Plane:** [[REALITY]]

---

```yaml
SYSTEM_REALITY:

  hardware_nodes:
    mac_studio_m4_max:
      ip: "100.87.214.70"
      status: "ONLINE"
      role: "Primary inference and canonical database host"
      memory: "36GB unified"
      storage: "512GB internal + 4TB LaCie external"
    macbook_air_m_series:
      ip: "100.121.17.63"
      status: "ONLINE"
      role: "Secondary engineering node"
      memory: "16GB unified"
      storage: "228GB internal + 1.8TB T7 Shield"

  model_serving:
    exo_native_mlx:
      endpoint: "http://100.87.214.70:52415/v1"
      active_model: "mlx-community/Qwen3.6-35B-A3B-5bit"
      status: "OPERATIONAL"
    litellm_gateway:
      endpoint: "http://100.87.214.70:4000"
      routing_strategy: "simple-shuffle"
      status: "OPERATIONAL_NAIVE"
    omniroute_gateway:
      endpoint: "http://localhost:20128"
      mcp_status: "401_UNAUTHORIZED"
      daemon_status: "LISTENING_PID_36691"
      active_providers: 352
      configured_clis: 0

  databases:
    neo4j:
      canonical_instance: "civos_neo4j"
      bolt_uri: "bolt://100.87.214.70:7687"
      http_uri: "http://100.87.214.70:7474"
      status: "HEALTHY"
      duplicate_instance: "t7shield-neo4j-1 (CRASH_LOOPING)"
    qdrant:
      http_uri: "http://100.87.214.70:6333"
      status: "HEALTHY"
    postgres:
      canonical_instance: "civos_postgres (:5433)"
      status: "HEALTHY"
      duplicate_instances: 2
    redis:
      canonical_instance: "civos_redis (:6379)"
      status: "HEALTHY"
      duplicate_instances: 2

  observability:
    langfuse:
      http_uri: "http://100.87.214.70:3003"
      status: "HEALTHY_RECEIVING_ZERO_TRAFFIC"
    grafana:
      http_uri: "http://100.87.214.70:3011"
      status: "HEALTHY"

  repositories:
    owned_cataloged: 887
    active_in_development: 7
    starred_analyzed: 910
```
