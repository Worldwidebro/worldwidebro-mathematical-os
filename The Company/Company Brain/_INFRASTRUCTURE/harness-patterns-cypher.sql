-- Awesome Harness Engineering Pattern Indexing
-- Creates Neo4j nodes for harness patterns, research, and capabilities

-- Constraints (idempotent)
CREATE CONSTRAINT IF NOT EXISTS ON (p:HarnessPattern) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS ON (r:Research) ASSERT r.id IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS ON (h:HarnessLayer) ASSERT h.name IS UNIQUE;

-- Indexes for query performance
CREATE INDEX IF NOT EXISTS FOR (p:HarnessPattern) ON (p.category);
CREATE INDEX IF NOT EXISTS FOR (p:HarnessPattern) ON (p.maturity);
CREATE INDEX IF NOT EXISTS FOR (r:Research) ON (r.source);

-- Core Harness Layers (from awesome-harness-engineering repo)
MERGE (l1:HarnessLayer {name: "Context Delivery"}) SET l1.order = 1;
MERGE (l2:HarnessLayer {name: "Planning"}) SET l2.order = 2;
MERGE (l3:HarnessLayer {name: "Tool Design"}) SET l3.order = 3;
MERGE (l4:HarnessLayer {name: "Memory Management"}) SET l4.order = 4;
MERGE (l5:HarnessLayer {name: "Skills & MCP"}) SET l5.order = 5;
MERGE (l6:HarnessLayer {name: "Permissions & Auth"}) SET l6.order = 6;
MERGE (l7:HarnessLayer {name: "State Management"}) SET l7.order = 7;
MERGE (l8:HarnessLayer {name: "Orchestration"}) SET l8.order = 8;
MERGE (l9:HarnessLayer {name: "Verification & Recovery"}) SET l9.order = 9;
MERGE (l10:HarnessLayer {name: "Observability"}) SET l10.order = 10;

-- Example patterns (from awesome-harness-engineering)
MERGE (p1:HarnessPattern {
  id: "pattern-context-windowing",
  name: "Context Windowing",
  category: "Context Delivery",
  maturity: "production",
  description: "Sliding window over long contexts to stay within token limits",
  github_stars: 4200,
  source_url: "https://github.com/ai-boost/awesome-harness-engineering"
})
CREATE (p1)-[:PART_OF]->(l1);

MERGE (p2:HarnessPattern {
  id: "pattern-reflection-loop",
  name: "Reflection Loop",
  category: "Verification",
  maturity: "production",
  description: "Agent evaluates own outputs before returning, catches errors",
  github_stars: 3800,
  source_url: "https://github.com/ai-boost/awesome-harness-engineering"
})
CREATE (p2)-[:PART_OF]->(l9);

MERGE (p3:HarnessPattern {
  id: "pattern-hierarchical-planning",
  name: "Hierarchical Planning",
  category: "Planning",
  maturity: "production",
  description: "Multi-level planning: strategic → tactical → operational",
  github_stars: 3500,
  source_url: "https://github.com/ai-boost/awesome-harness-engineering"
})
CREATE (p3)-[:PART_OF]->(l2);

MERGE (p4:HarnessPattern {
  id: "pattern-tool-grounding",
  name: "Tool Grounding",
  category: "Tool Design",
  maturity: "production",
  description: "Agents discover tools dynamically, learn signatures, adapt calls",
  github_stars: 3200,
  source_url: "https://github.com/ai-boost/awesome-harness-engineering"
})
CREATE (p4)-[:PART_OF]->(l3);

MERGE (p5:HarnessPattern {
  id: "pattern-memory-hierarchy",
  name: "Memory Hierarchy",
  category: "Memory Management",
  maturity: "research",
  description: "Working memory (immediate), episodic (recent), semantic (permanent)",
  github_stars: 2800,
  source_url: "https://github.com/ai-boost/awesome-harness-engineering"
})
CREATE (p5)-[:PART_OF]->(l4);

-- Link patterns to agents (example)
MATCH (a:Agent {id: "agent-lt-005-dispatcher"})
MATCH (p:HarnessPattern {id: "pattern-hierarchical-planning"})
CREATE (a)-[:USES_PATTERN]->(p);

-- Research source tracking
MERGE (src:Research {
  id: "awesome-harness-engineering-repo",
  source: "GitHub",
  url: "https://github.com/ai-boost/awesome-harness-engineering",
  stars: 68000,
  indexed_date: datetime(),
  patterns_found: 50
});

-- Link patterns back to source
MATCH (p:HarnessPattern)
MATCH (src:Research {id: "awesome-harness-engineering-repo"})
CREATE (p)-[:FROM_SOURCE]->(src);

-- Adoption tracking
MERGE (adoption:AdoptionLog {
  id: "adoption-" + timestamp(),
  timestamp: datetime(),
  company: "Company Brain",
  patterns_adopted: 5,
  status: "active"
});
