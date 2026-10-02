#!/bin/bash
# ingest_connectivity_graph.sh
# Ingests verified system connectivity into Neo4j
# Run this on Mac Studio where Neo4j is accessible
#
# Usage: ssh divinejohns@100.87.214.70 "bash < ingest_connectivity_graph.sh"
# Or: ./ingest_connectivity_graph.sh (if run locally on Mac Studio)

set -e

echo "=== Ingesting System Connectivity into Neo4j ==="
echo "Verified: 2026-10-02 23:58 UTC"
echo ""

# Use Docker exec to run cypher-shell inside neo4j container
docker exec neo4j cypher-shell \
  -u neo4j \
  -p changeme \
  -d neo4j << 'CYPHER_COMMANDS'

// ===========================================================================
// DEVICE NODES - Mac Air & Mac Studio
// ===========================================================================

MERGE (mac_air:Device {
  device_id: "DEV-MAC-AIR-001",
  hostname: "Mac-1299.lan",
  device_name: "MacBook Air 15\"",
  device_type: "workstation",
  tailscale_ip: "100.121.17.63",
  lan_ip: "192.168.1.79",
  cpu: "Apple M3",
  memory_gb: 16,
  storage_total_gb: 228,
  storage_used_gb: 223,
  storage_free_gb: 5,
  storage_pct_used: 98,
  os: "macOS Sequoia 15.x",
  status: "ONLINE"
})
SET mac_air.verified_date = "2026-10-02"
SET mac_air.health_status = "CRITICAL-STORAGE"
RETURN mac_air.hostname;

MERGE (mac_studio:Device {
  device_id: "DEV-MAC-STUDIO-001",
  hostname: "Mac.lan",
  device_name: "Mac Studio M2 Ultra",
  device_type: "compute-node",
  tailscale_ip: "100.87.214.70",
  lan_ip: "192.168.1.11",
  cpu: "Apple M2 Ultra (20-core)",
  memory_gb: 128,
  storage_total_gb: 228,
  storage_used_gb: 217,
  storage_free_gb: 11,
  storage_pct_used: 95,
  os: "macOS Sonoma 14.x",
  status: "ONLINE"
})
SET mac_studio.verified_date = "2026-10-02"
SET mac_studio.health_status = "CRITICAL-STORAGE"
RETURN mac_studio.hostname;

// ===========================================================================
// SERVICE NODES - Running on Mac Studio
// ===========================================================================

MERGE (neo4j:Service {
  service_id: "SVC-NEO4J-001",
  service_name: "Neo4j",
  service_type: "graph-database",
  version: "5.23.0",
  host: "100.87.214.70",
  port: 7474,
  status: "RUNNING",
  edge_count: 20363,
  verified_date: "2026-10-02"
})
RETURN neo4j.service_name;

MERGE (qdrant:Service {
  service_id: "SVC-QDRANT-001",
  service_name: "Qdrant",
  service_type: "vector-database",
  version: "latest",
  host: "100.87.214.70",
  port: 6333,
  status: "RUNNING",
  vector_count: 17236,
  verified_date: "2026-10-02"
})
RETURN qdrant.service_name;

MERGE (omniroute:Service {
  service_id: "SVC-OMNIROUTE-001",
  service_name: "OmniRoute",
  service_type: "ai-gateway",
  version: "16.3.1",
  host: "100.87.214.70",
  port: 3004,
  status: "RUNNING",
  tools_count: 110,
  verified_date: "2026-10-02"
})
RETURN omniroute.service_name;

// ===========================================================================
// NETWORK NODES
// ===========================================================================

MERGE (tailscale:Network {
  network_id: "NET-TAILSCALE-001",
  network_name: "Tailscale VPN",
  network_type: "vpn",
  status: "ONLINE",
  verified_date: "2026-10-02"
})
RETURN tailscale.network_name;

MERGE (lan:Network {
  network_id: "NET-LAN-001",
  network_name: "Local Area Network",
  network_type: "LAN",
  subnet: "192.168.1.0/24",
  status: "ONLINE",
  verified_date: "2026-10-02"
})
RETURN lan.network_name;

// ===========================================================================
// CONNECTIVITY RELATIONSHIPS
// ===========================================================================

// Mac Air <-> Mac Studio connection
MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MERGE (mac_air)-[r:CONNECTED_TO {
  via: "Tailscale",
  method: "SSH + HTTP",
  latency_ms: 50,
  verified_date: "2026-10-02"
}]->(mac_studio)
RETURN "Connection: Mac Air -> Mac Studio";

// Mac Studio runs services
MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (neo4j:Service {service_id: "SVC-NEO4J-001"})
MERGE (mac_studio)-[r:RUNS {
  status: "active",
  verified_date: "2026-10-02"
}]->(neo4j)
RETURN "Service: Mac Studio runs Neo4j";

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (qdrant:Service {service_id: "SVC-QDRANT-001"})
MERGE (mac_studio)-[r:RUNS {
  status: "active",
  verified_date: "2026-10-02"
}]->(qdrant)
RETURN "Service: Mac Studio runs Qdrant";

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (omniroute:Service {service_id: "SVC-OMNIROUTE-001"})
MERGE (mac_studio)-[r:RUNS {
  status: "active",
  verified_date: "2026-10-02"
}]->(omniroute)
RETURN "Service: Mac Studio runs OmniRoute";

// Mac Air can access services
MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (neo4j:Service {service_id: "SVC-NEO4J-001"})
MERGE (mac_air)-[r:CAN_ACCESS {
  method: "HTTP",
  status: "VERIFIED",
  url: "http://100.87.214.70:7474",
  verified_date: "2026-10-02"
}]->(neo4j)
RETURN "Access: Mac Air -> Neo4j";

MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (qdrant:Service {service_id: "SVC-QDRANT-001"})
MERGE (mac_air)-[r:CAN_ACCESS {
  method: "HTTP",
  status: "VERIFIED",
  url: "http://100.87.214.70:6333",
  verified_date: "2026-10-02"
}]->(qdrant)
RETURN "Access: Mac Air -> Qdrant";

MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (omniroute:Service {service_id: "SVC-OMNIROUTE-001"})
MERGE (mac_air)-[r:CAN_ACCESS {
  method: "HTTP",
  status: "VERIFIED",
  url: "http://100.87.214.70:3004",
  verified_date: "2026-10-02"
}]->(omniroute)
RETURN "Access: Mac Air -> OmniRoute";

// ===========================================================================
// VERIFICATION QUERIES
// ===========================================================================

MATCH (d:Device)
RETURN "Devices ingested: " + COUNT(d);

MATCH (s:Service)
RETURN "Services ingested: " + COUNT(s);

MATCH ()-[r:CONNECTED_TO|RUNS|CAN_ACCESS]->()
RETURN "Relationships ingested: " + COUNT(r);

MATCH (mac_air:Device)-[r:CONNECTED_TO]->(mac_studio:Device)
RETURN mac_air.hostname + " -> " + mac_studio.hostname + " via " + r.via;

MATCH (d:Device)-[r:RUNS]->(s:Service)
RETURN d.hostname + " RUNS " + s.service_name;

MATCH (mac_air:Device)-[r:CAN_ACCESS]->(s:Service)
RETURN mac_air.hostname + " CAN_ACCESS " + s.service_name + " at " + r.url;

CYPHER_COMMANDS

echo ""
echo "✅ Connectivity graph ingestion complete!"
echo "Verified: 2026-10-02 23:58 UTC"
echo ""
echo "Query examples:"
echo '  MATCH (d:Device)-[r:CONNECTED_TO]->(s:Device) RETURN d, r, s'
echo '  MATCH (d:Device)-[r:RUNS]->(s:Service) RETURN d, r, s'
echo '  MATCH (d:Device)-[r:CAN_ACCESS]->(s:Service) RETURN d, r, s'
