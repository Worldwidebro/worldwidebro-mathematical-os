// CONNECTIVITY_SCHEMA.cypher — System topology + network connections
// Verified: 2026-10-02 23:58 UTC via SYSTEM_CONNECTIVITY_AUDIT

// ============================================================================
// CONSTRAINT & INDEX DEFINITIONS
// ============================================================================

CREATE CONSTRAINT IF NOT EXISTS FOR (d:Device) REQUIRE d.device_id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (s:Service) REQUIRE s.service_id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (n:Network) REQUIRE n.network_id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (p:Port) REQUIRE p.port_id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (i:IPAddress) REQUIRE i.ip_address IS UNIQUE;

CREATE INDEX IF NOT EXISTS FOR (d:Device) ON (d.hostname);
CREATE INDEX IF NOT EXISTS FOR (d:Device) ON (d.status);
CREATE INDEX IF NOT EXISTS FOR (s:Service) ON (s.service_name);
CREATE INDEX IF NOT EXISTS FOR (s:Service) ON (s.status);
CREATE INDEX IF NOT EXISTS FOR (i:IPAddress) ON (i.address);

// ============================================================================
// DEVICE NODES
// ============================================================================

MERGE (mac_air:Device {
  device_id: "DEV-MAC-AIR-001",
  hostname: "Mac-1299.lan",
  device_name: "MacBook Air 15\"",
  device_type: "workstation",
  manufacturer: "Apple",
  model: "MacBook Air M3",
  cpu: "Apple M3",
  memory_gb: 16,
  storage_total_gb: 228,
  storage_used_gb: 223,
  storage_free_gb: 5,
  storage_pct_used: 98,
  os_name: "macOS",
  os_version: "Sequoia 15.x",
  architecture: "ARM64",
  status: "ONLINE",
  role: "development-workstation",
  tailscale_ip: "100.121.17.63",
  tailscale_connection_type: "VPN-tunnel",
  lan_ip: "192.168.1.79",
  lan_connection: "wifi",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  criticality: "HIGH"
})
SET mac_air.last_seen = datetime()
SET mac_air.health_status = "CRITICAL-STORAGE"
RETURN mac_air;

MERGE (mac_studio:Device {
  device_id: "DEV-MAC-STUDIO-001",
  hostname: "Mac.lan",
  device_name: "Mac Studio",
  device_type: "compute-node",
  manufacturer: "Apple",
  model: "Mac Studio M2 Ultra",
  cpu: "Apple M2 Ultra (20-core)",
  gpu: "76-core",
  memory_gb: 128,
  storage_total_gb: 228,
  storage_used_gb: 217,
  storage_free_gb: 11,
  storage_pct_used: 95,
  os_name: "macOS",
  os_version: "Sonoma 14.x",
  architecture: "ARM64",
  status: "ONLINE",
  role: "primary-compute",
  tailscale_ip: "100.87.214.70",
  tailscale_connection_type: "direct-LAN",
  tailscale_latency_ms: 5,
  lan_ip: "192.168.1.11",
  lan_port: 41641,
  lan_connection: "ethernet",
  ssh_enabled: true,
  ssh_user: "divinejohns",
  ssh_key_type: "ed25519",
  ssh_authentication: "passwordless",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  criticality: "CRITICAL"
})
SET mac_studio.last_seen = datetime()
SET mac_studio.health_status = "CRITICAL-STORAGE"
RETURN mac_studio;

// ============================================================================
// NETWORK NODES
// ============================================================================

MERGE (tailscale:Network {
  network_id: "NET-TAILSCALE-001",
  network_name: "Tailscale VPN",
  network_type: "vpn",
  protocol: "WireGuard",
  tailnet: "Worldwidebro@",
  status: "ONLINE",
  verified_date: "2026-10-02",
  verified_time: "23:58:00"
})
SET tailscale.last_verified = datetime()
RETURN tailscale;

MERGE (lan:Network {
  network_id: "NET-LAN-001",
  network_name: "Local Area Network",
  network_type: "LAN",
  protocol: "Ethernet/WiFi",
  subnet: "192.168.1.0/24",
  status: "ONLINE",
  verified_date: "2026-10-02",
  verified_time: "23:58:00"
})
SET lan.last_verified = datetime()
RETURN lan;

// ============================================================================
// SERVICE NODES
// ============================================================================

MERGE (neo4j:Service {
  service_id: "SVC-NEO4J-001",
  service_name: "Neo4j",
  service_type: "graph-database",
  version: "5.23.0",
  container: "neo4j:5.23.0",
  host: "100.87.214.70",
  status: "RUNNING",
  bolt_port: 7687,
  http_port: 7474,
  database_name: "company_brain",
  node_count: 3000,
  edge_count: 20363,
  vector_dimension: 1536,
  url: "http://100.87.214.70:7474",
  credentials: "neo4j/*** (changeme-rotate-required)",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  verified_method: "HTTP_GET",
  health_status: "HEALTHY"
})
SET neo4j.last_ping = datetime()
RETURN neo4j;

MERGE (qdrant:Service {
  service_id: "SVC-QDRANT-001",
  service_name: "Qdrant",
  service_type: "vector-database",
  version: "latest",
  container: "qdrant:latest",
  host: "100.87.214.70",
  port: 6333,
  status: "RUNNING",
  vectors_indexed: 17236,
  collections: 5,
  url: "http://100.87.214.70:6333",
  health_endpoint: "/health",
  health_status_code: 200,
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  verified_method: "HTTP_GET"
})
SET qdrant.last_ping = datetime()
RETURN qdrant;

MERGE (omniroute:Service {
  service_id: "SVC-OMNIROUTE-001",
  service_name: "OmniRoute",
  service_type: "ai-gateway",
  version: "16.3.1",
  container: "omniroute:latest",
  host: "100.87.214.70",
  port: 3004,
  status: "RUNNING",
  tools_integrated: 110,
  mcp_transport: "SSE,Stdio",
  dashboard_url: "http://100.87.214.70:3004/dashboard",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  verified_method: "HTTP_GET"
})
SET omniroute.last_ping = datetime()
RETURN omniroute;

MERGE (docker:Service {
  service_id: "SVC-DOCKER-001",
  service_name: "Docker Engine",
  service_type: "container-runtime",
  host: "100.87.214.70",
  status: "RUNNING",
  containers_active: 70,
  volumes: 70,
  data_location: "UNKNOWN",
  data_location_claimed: "/Volumes/T7Shield/docker/",
  data_location_verified: false,
  note: "T7 Shield not mounted as of 2026-10-02 23:58",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  verification_method: "port-response"
})
SET docker.last_seen = datetime()
RETURN docker;

// ============================================================================
// CONNECTIVITY RELATIONSHIPS
// ============================================================================

// Mac Air connections
MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (tailscale:Network {network_id: "NET-TAILSCALE-001"})
MERGE (mac_air)-[r:CONNECTED_VIA {
  connection_type: "VPN-tunnel",
  ip_address: "100.121.17.63",
  latency_ms: 50,
  status: "ACTIVE",
  established: "2026-10-01T00:00:00Z",
  verified_date: "2026-10-02"
}]->(tailscale)
RETURN r;

MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (lan:Network {network_id: "NET-LAN-001"})
MERGE (mac_air)-[r:CONNECTED_VIA {
  connection_type: "WiFi",
  ip_address: "192.168.1.79",
  status: "ACTIVE",
  verified_date: "2026-10-02"
}]->(lan)
RETURN r;

// Mac Studio connections
MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (tailscale:Network {network_id: "NET-TAILSCALE-001"})
MERGE (mac_studio)-[r:CONNECTED_VIA {
  connection_type: "direct-LAN",
  ip_address: "100.87.214.70",
  latency_ms: 5,
  status: "ACTIVE",
  established: "2026-09-15T00:00:00Z",
  verified_date: "2026-10-02"
}]->(tailscale)
RETURN r;

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (lan:Network {network_id: "NET-LAN-001"})
MERGE (mac_studio)-[r:CONNECTED_VIA {
  connection_type: "Ethernet",
  ip_address: "192.168.1.11",
  port: 41641,
  status: "ACTIVE",
  verified_date: "2026-10-02"
}]->(lan)
RETURN r;

// Inter-device connectivity
MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MERGE (mac_air)-[r:CAN_REACH {
  method: "SSH",
  user: "divinejohns",
  auth_type: "ed25519-key",
  passwordless: true,
  status: "VERIFIED",
  verified_date: "2026-10-02",
  verified_time: "23:58:00",
  latency_ms: 50
}]->(mac_studio)
RETURN r;

// Mac Studio runs services
MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (neo4j:Service {service_id: "SVC-NEO4J-001"})
MERGE (mac_studio)-[r:RUNS {
  port: 7474,
  status: "RUNNING",
  verified_date: "2026-10-02"
}]->(neo4j)
RETURN r;

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (qdrant:Service {service_id: "SVC-QDRANT-001"})
MERGE (mac_studio)-[r:RUNS {
  port: 6333,
  status: "RUNNING",
  verified_date: "2026-10-02"
}]->(qdrant)
RETURN r;

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (omniroute:Service {service_id: "SVC-OMNIROUTE-001"})
MERGE (mac_studio)-[r:RUNS {
  port: 3004,
  status: "RUNNING",
  verified_date: "2026-10-02"
}]->(omniroute)
RETURN r;

MATCH (mac_studio:Device {device_id: "DEV-MAC-STUDIO-001"})
MATCH (docker:Service {service_id: "SVC-DOCKER-001"})
MERGE (mac_studio)-[r:RUNS {
  status: "RUNNING",
  verified_date: "2026-10-02"
}]->(docker)
RETURN r;

// Mac Air can access services
MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (neo4j:Service {service_id: "SVC-NEO4J-001"})
MERGE (mac_air)-[r:CAN_REACH {
  method: "HTTP",
  url: "http://100.87.214.70:7474",
  status: "VERIFIED",
  verified_date: "2026-10-02",
  latency_ms: 50
}]->(neo4j)
RETURN r;

MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (qdrant:Service {service_id: "SVC-QDRANT-001"})
MERGE (mac_air)-[r:CAN_REACH {
  method: "HTTP",
  url: "http://100.87.214.70:6333",
  status: "VERIFIED",
  verified_date: "2026-10-02"
}]->(qdrant)
RETURN r;

MATCH (mac_air:Device {device_id: "DEV-MAC-AIR-001"})
MATCH (omniroute:Service {service_id: "SVC-OMNIROUTE-001"})
MERGE (mac_air)-[r:CAN_REACH {
  method: "HTTP",
  url: "http://100.87.214.70:3004",
  status: "VERIFIED",
  verified_date: "2026-10-02"
}]->(omniroute)
RETURN r;

// ============================================================================
// VERIFICATION SUMMARY
// ============================================================================

MATCH (d:Device)
WITH d.hostname AS hostname, d.status AS status, d.health_status AS health
RETURN hostname, status, health;

MATCH (s:Service)
WITH s.service_name AS service, s.status AS status, s.health_status AS health
RETURN service, status, health;

MATCH (d:Device)-[r:CAN_REACH]->(s:Service)
RETURN d.hostname, s.service_name, r.status, COUNT(*) as connection_count;
