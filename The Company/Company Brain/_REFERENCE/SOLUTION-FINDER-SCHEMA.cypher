// SOLUTION FINDER SCHEMA — Neo4j
// Enables discovery of existing solutions before re-solving problems
// Created: 2026-09-19

// ===== CONSTRAINTS & INDEXES =====

// Unique constraint on Solution names (no duplicate solutions)
CREATE CONSTRAINT solution_id IF NOT EXISTS
FOR (s:Solution) REQUIRE s.id IS UNIQUE;

// Unique constraint on Problem names
CREATE CONSTRAINT problem_id IF NOT EXISTS
FOR (p:Problem) REQUIRE p.id IS UNIQUE;

// Index for fast solution lookups by name
CREATE INDEX solution_name IF NOT EXISTS
FOR (s:Solution) ON (s.name);

// Index for fast problem lookups by domain
CREATE INDEX problem_domain IF NOT EXISTS
FOR (p:Problem) ON (p.domain);

// Index for relationships (faster traversal)
CREATE INDEX solves_relationship IF NOT EXISTS
FOR ()-[r:SOLVES]-() ON (r.confidence);

// ===== NODE TEMPLATES =====

// Solution Node
// MERGE (s:Solution {
//   id: "SOL-001",
//   name: "Cold Call Automation",
//   description: "Script + phone dialing for LT-005 medical",
//   codePath: "repos/lt-005-healthroute-courier/src/api/cold-calls.ts",
//   codeSnippet: "export const dialScript = ...",
//   language: "TypeScript",
//   repo: "LT-005",
//   sector: "LT",
//   tags: ["sales", "outreach", "automation"],
//   created: datetime("2026-09-19"),
//   confidence: 0.95,
//   usageCount: 0
// })

// Problem Node
// MERGE (p:Problem {
//   id: "PROB-001",
//   name: "Cold Call Dialing",
//   domain: "sales",
//   description: "How to automate cold calls",
//   sector: "LT",
//   difficulty: "medium",
//   created: datetime("2026-09-19")
// })

// ===== RELATIONSHIPS =====

// Solution SOLVES Problem
// MATCH (s:Solution {id: "SOL-001"}), (p:Problem {id: "PROB-001"})
// CREATE (s)-[r:SOLVES {
//   confidence: 0.95,
//   appliesTo: ["LT-005", "OPS-001"],
//   dateVerified: datetime("2026-09-19")
// }]->(p)

// Venture USES Solution
// MATCH (v:Venture {id: "LT-005"}), (s:Solution {id: "SOL-001"})
// CREATE (v)-[r:USES_SOLUTION {
//   status: "active",
//   dateImplemented: datetime("2026-09-10")
// }]->(s)

// Solution EXTENDS Solution (reuse hierarchy)
// MATCH (s1:Solution {id: "SOL-001"}), (s2:Solution {id: "SOL-003"})
// CREATE (s2)-[r:EXTENDS {
//   reason: "Adds Twilio integration to base script"
// }]->(s1)

// Agent DISCOVERED Solution
// MATCH (a:Agent {id: "AGT-005"}), (s:Solution {id: "SOL-001"})
// CREATE (a)-[r:DISCOVERED {
//   method: "graft_search",
//   score: 0.92,
//   timestamp: datetime("2026-09-19")
// }]->(s)

// ===== QUERY TEMPLATES =====

// Q1: Find solution by problem name (primary search)
// MATCH (p:Problem {name: "Cold Call Dialing"})<-[r:SOLVES]-(s:Solution)
// RETURN s.name, s.codePath, r.confidence
// ORDER BY r.confidence DESC
// LIMIT 5

// Q2: Find solutions by domain
// MATCH (s:Solution)-[r:SOLVES]->(p:Problem)
// WHERE p.domain = "sales"
// RETURN s.name, s.repo, p.name, r.confidence
// ORDER BY r.confidence DESC

// Q3: Find all solutions used by a venture
// MATCH (v:Venture {id: "LT-005"})-[r:USES_SOLUTION]->(s:Solution)
// RETURN s.name, s.codePath, r.status
// ORDER BY r.dateImplemented DESC

// Q4: Find solutions with high reuse (most useful)
// MATCH (s:Solution)
// WHERE s.usageCount > 2
// RETURN s.name, s.usageCount, s.codePath
// ORDER BY s.usageCount DESC

// Q5: Find similar solutions (by tags)
// MATCH (s1:Solution {id: "SOL-001"})-[r:SOLVES]->(p1:Problem)
// MATCH (p2:Problem)<-[r2:SOLVES]-(s2:Solution)
// WHERE p1.domain = p2.domain
// AND s1.id <> s2.id
// RETURN s2.name, p2.name, r2.confidence
// LIMIT 10
