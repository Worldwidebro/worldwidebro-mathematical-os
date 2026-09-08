// Company Brain - Neo4j Graph Import
// Schema: COMPANY → VENTURES → REPOSITORIES → DEPLOYMENTS

// Create company node
MERGE (cb:COMPANY {id: "CB-WORLDWIDEBRO", name: "Company Brain"})
SET cb.created_at = datetime()
SET cb.total_ventures = 789
SET cb.total_repos = 893
SET cb.synced = datetime();

// Create venture nodes + link to company
UNWIND $ventures AS v
MERGE (venture:VENTURE {id: v.id, name: v.name})
SET venture.sector = v.sector
SET venture.status = v.status
SET venture.repo_count = v.repo_count
MERGE (cb:COMPANY)-[:OPERATES]->(venture);

// Create repository nodes + link to ventures
UNWIND $repositories AS r
MERGE (repo:REPOSITORY {id: r.id, name: r.name})
SET repo.url = r.url
SET repo.language = r.language
SET repo.archived = r.archived
MERGE (cb:COMPANY)-[:OWNS]->(repo);

// Link ventures to repos (where known)
UNWIND $venture_repo_mappings AS vrm
MATCH (v:VENTURE {id: vrm.venture_id})
MATCH (r:REPOSITORY {id: vrm.repo_id})
MERGE (v)-[:IMPLEMENTED_BY]->(r);

// Create deployment nodes (Vercel)
UNWIND $deployments AS d
MERGE (dep:DEPLOYMENT {id: d.repo_id, url: d.vercel_url})
SET dep.platform = "VERCEL"
MATCH (r:REPOSITORY {id: d.repo_id})
MERGE (r)-[:DEPLOYED_AS]->(dep);

// Indexes for fast lookup
CREATE INDEX IF NOT EXISTS FOR (v:VENTURE) ON (v.id);
CREATE INDEX IF NOT EXISTS FOR (r:REPOSITORY) ON (r.id);
CREATE INDEX IF NOT EXISTS FOR (d:DEPLOYMENT) ON (d.id);
CREATE INDEX IF NOT EXISTS FOR (c:COMPANY) ON (c.id);

RETURN "✓ Company Brain graph created";
