# DispatchOS System Architecture

This document defines the interface bounds, service layers, and capability mappings for DispatchOS (LT-011).

## 1. System Topology
The platform decouples human client interfaces from structural backend processing and the agentic execution core.

```text
                         VEX / WORLDWIDEBRO OS
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │      LT-011         │
                       │    DISPATCH OS      │
                       └──────────┬──────────┘
                                  │
        ┌──────────────┬──────────┼───────────┬──────────────┐
        ▼              ▼          ▼           ▼              ▼
     Dispatch       Logistics   Freight      Fleet        Customer
        │              │          │           │              │
        └──────────────┴──────────┼───────────┴──────────────┘
                                  ▼
                         EVENT / DATA LAYER
                                  │
                                  ▼
                         AGENT ORCHESTRATOR
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
           AGENTS              SKILLS                MCPs
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                              ACTIONS
                                  │
                                  ▼
                            OPERATIONS
                                  │
                                  ▼
                              REVENUE
                                  │
                                  ▼
                           ACTION LEDGER
                                  │
                                  ▼
                         CAPABILITY GRAPH
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
          LT-005               LT-011              Future OpCos
        CourierOS           DispatchOS            Transportation
```

---

## 2. MCP Layer Contracts
Model Context Protocols (MCPs) expose standard capabilities without containing internal business logic. This allows the agents to remain decoupled from underlying platform providers (e.g. Google Maps vs Mapbox).

### Maps MCP (`mcp/maps`)
*   `maps.geocode(address)` $\rightarrow$ `{ lat, lng }`
*   `maps.calculate_route(origin, destination)` $\rightarrow$ `{ geometry, distance_mi, duration_sec }`
*   `maps.calculate_eta(origin, destination, traffic_conditions)` $\rightarrow$ `{ eta_timestamp }`

### GPS MCP (`mcp/gps`)
*   `gps.get_location(device_id)` $\rightarrow$ `{ lat, lng, speed, timestamp }`
*   `gps.get_history(device_id, start_time, end_time)` $\rightarrow$ `List<{ lat, lng, timestamp }>`

### Documents MCP (`mcp/documents`)
*   `documents.upload_file(blob, metadata)` $\rightarrow$ `{ doc_url }`
*   `documents.run_ocr(doc_url)` $\rightarrow$ `{ raw_text }`
*   `documents.verify_signature(doc_url)` $\rightarrow$ `{ signed: boolean, timestamp }`

---

## 3. Capability Graph Integration
Capabilities are declared in the Neo4j World Model. Multiple downstream ventures can inherit the same shared package skills:

```
  [ Capability: routing.optimize ]
                ▲
                ├── Inherited by ──► [ CourierOS / LT-005 ]
                ├── Inherited by ──► [ DispatchOS / LT-011 ]
                └── Inherited by ──► [ Future Freight OpCo ]
```

This ensures zero duplicate implementation of core routing/dispatch algorithms.
