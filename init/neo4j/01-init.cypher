// AI BOSS OS Neo4j Schema
CREATE CONSTRAINT venture_id IF NOT EXISTS FOR (v:Venture) REQUIRE v.id IS UNIQUE;
CREATE CONSTRAINT agent_id IF NOT EXISTS FOR (a:Agent) REQUIRE a.id IS UNIQUE;
CREATE CONSTRAINT sector_id IF NOT EXISTS FOR (s:Sector) REQUIRE s.name IS UNIQUE;

CREATE INDEX venture_name IF NOT EXISTS FOR (v:Venture) ON (v.name);
CREATE INDEX agent_status IF NOT EXISTS FOR (a:Agent) ON (a.status);

MERGE (os:System {name: 'AI Boss OS', version: '1.0.0'})
MERGE (con:Sector {name: 'Construction', id: 'CON'})
MERGE (fin:Sector {name: 'Finance', id: 'FIN'})
MERGE (lt:Sector {name: 'Logistics', id: 'LT'})
MERGE (re:Sector {name: 'Real Estate', id: 'RE'})
MERGE (os)-[:MANAGES]->(con)
MERGE (os)-[:MANAGES]->(fin)
MERGE (os)-[:MANAGES]->(lt)
MERGE (os)-[:MANAGES]->(re);
