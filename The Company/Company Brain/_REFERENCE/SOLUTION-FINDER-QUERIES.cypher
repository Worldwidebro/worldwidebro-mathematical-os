// SOLUTION FINDER QUERIES — Ready to execute
// 2026-09-19

// ===== SETUP: Load existing solutions into Neo4j =====

// Add Cold Call Solution (from LT-005 baseline)
MERGE (s:Solution {
  id: "SOL-001",
  name: "Cold Call Automation",
  description: "Script + phone dialing for medical facilities",
  codePath: "repos/lt-005-healthroute-courier/src/api/cold-calls.ts",
  language: "TypeScript",
  repo: "LT-005",
  sector: "LT",
  tags: ["sales", "outreach", "automation", "medical"],
  created: datetime("2026-09-10"),
  confidence: 0.95,
  usageCount: 1
})

// Add Problem node
MERGE (p:Problem {
  id: "PROB-001",
  name: "Cold Call Dialing",
  domain: "sales",
  sector: "LT"
})

// Wire: Solution SOLVES Problem
WITH s, p
MATCH (s:Solution {id: "SOL-001"}), (p:Problem {id: "PROB-001"})
MERGE (s)-[r:SOLVES {confidence: 0.95, dateVerified: datetime("2026-09-19")}]->(p)

// ---

// Add Venture Readiness Scoring Solution
MERGE (s2:Solution {
  id: "SOL-002",
  name: "Venture Readiness Scoring",
  description: "Algorithm to calculate readiness % based on 12 factors",
  codePath: "repos/con-001-ace-construction/src/app/api/webhooks/jotform/route.ts",
  language: "TypeScript",
  repo: "CON-001",
  sector: "CON",
  tags: ["scoring", "metrics", "readiness"],
  created: datetime("2026-09-10"),
  confidence: 0.90,
  usageCount: 1
})

MERGE (p2:Problem {
  id: "PROB-002",
  name: "Venture Readiness Assessment",
  domain: "metrics",
  sector: "ALL"
})

WITH s2, p2
MATCH (s:Solution {id: "SOL-002"}), (p:Problem {id: "PROB-002"})
MERGE (s)-[r:SOLVES {confidence: 0.90}]->(p)

// ---

// Add Neo4j Sync Solution
MERGE (s3:Solution {
  id: "SOL-003",
  name: "Supabase → Neo4j Sync",
  description: "Pipeline to sync venture data from Supabase to Neo4j",
  codePath: "vex-wired/vex-neo4j-connector.ts",
  language: "TypeScript",
  repo: "VEX",
  sector: "INFRASTRUCTURE",
  tags: ["sync", "data-pipeline", "neo4j", "supabase"],
  created: datetime("2026-09-10"),
  confidence: 0.92,
  usageCount: 1
})

MERGE (p3:Problem {
  id: "PROB-003",
  name: "Keep Neo4j in Sync with Supabase",
  domain: "infrastructure",
  sector: "ALL"
})

WITH s3, p3
MATCH (s:Solution {id: "SOL-003"}), (p:Problem {id: "PROB-003"})
MERGE (s)-[r:SOLVES {confidence: 0.92}]->(p)

// ===== QUERY: Find Solution by Problem Name =====
MATCH (p:Problem {name: "Cold Call Dialing"})<-[r:SOLVES]-(s:Solution)
RETURN
  s.id as solutionId,
  s.name as solutionName,
  s.codePath as codePath,
  s.repo as repo,
  r.confidence as confidence
ORDER BY r.confidence DESC;

// ===== QUERY: Find All Solutions by Domain =====
MATCH (s:Solution)-[r:SOLVES]->(p:Problem)
WHERE p.domain = "sales"
RETURN
  s.name as solution,
  s.repo as repo,
  p.name as problem,
  r.confidence as confidence
ORDER BY r.confidence DESC;

// ===== QUERY: Find All Registered Solutions =====
MATCH (s:Solution)-[r:SOLVES]->(p:Problem)
RETURN
  s.id as solutionId,
  s.name as name,
  s.language as lang,
  s.repo as repo,
  p.name as solvesProblem,
  r.confidence as confidence,
  s.usageCount as usageCount
ORDER BY s.usageCount DESC;

// ===== QUERY: Increment solution usage when discovered =====
MATCH (s:Solution {id: "SOL-001"})
SET s.usageCount = s.usageCount + 1,
    s.lastUsed = datetime("2026-09-19")
RETURN s.name, s.usageCount;

// ===== QUERY: Find High-Reuse Solutions (MVP-worthy) =====
MATCH (s:Solution)
WHERE s.usageCount >= 1
RETURN
  s.name as solution,
  s.usageCount as reuses,
  s.codePath as implementation
ORDER BY s.usageCount DESC, s.confidence DESC
LIMIT 10;
