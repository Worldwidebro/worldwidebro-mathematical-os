// 1. CONSTRAINTS (Ensure data integrity)
CREATE CONSTRAINT venture_id IF NOT EXISTS FOR (v:Venture) REQUIRE v.id IS UNIQUE;
CREATE CONSTRAINT agent_id IF NOT EXISTS FOR (a:Agent) REQUIRE a.id IS UNIQUE;
CREATE CONSTRAINT delegation_id IF NOT EXISTS FOR (d:Delegation) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT opportunity_id IF NOT EXISTS FOR (o:Opportunity) REQUIRE o.id IS UNIQUE;

// 2. CREATE TIER 1 VENTURES (Sample Data)
CREATE (sta:Venture {id: 'STA-001', name: 'Ace Staffing', sector: 'Staffing', location: 'Charlotte, NC', status: 'active'})
CREATE (con:Venture {id: 'CON-001', name: 'Ace Construction', sector: 'Construction', location: 'Charlotte, NC', status: 'active'})
CREATE (re:Venture {id: 'RE-001', name: 'Ace Properties', sector: 'Real Estate', location: 'Charlotte, NC', status: 'active'})
CREATE (fin:Venture {id: 'FIN-001', name: 'Ace Capital', sector: 'Financial', location: 'Charlotte, NC', status: 'active'})
CREATE (ops:Venture {id: 'OPS-001', name: 'Worldwidebro Ops', sector: 'Operations', location: 'Charlotte, NC', status: 'active'})

// 3. CREATE AGENTS
CREATE (agent_sourcing:Agent {id: 'AGT-001', role: 'Sourcing', venture_id: 'STA-001'})
CREATE (agent_pm:Agent {id: 'AGT-002', role: 'ProjectManager', venture_id: 'CON-001'})
CREATE (agent_deal:Agent {id: 'AGT-003', role: 'DealSourcing', venture_id: 'FIN-001'})

// 4. MAP THE DELEGATION NETWORK (How they need each other)
// STA provides labor to CON
CREATE (sta)-[:PROVIDES_LABOR {margin_pct: 0.35, sla_hours: 24}]->(con)
// CON builds assets for RE
CREATE (con)-[:DELIVERS_ASSET {margin_pct: 0.25, sla_hours: 72}]->(re)
// RE sources deals for FIN
CREATE (re)-[:SOURCES_DEAL {margin_pct: 0.02, sla_hours: 48}]->(fin)
// OPS serves everyone
CREATE (ops)-[:PROVIDES_BACKOFFICE {margin_pct: 0.05, sla_hours: 24}]->(sta)
CREATE (ops)-[:PROVIDES_BACKOFFICE {margin_pct: 0.05, sla_hours: 24}]->(con)
CREATE (ops)-[:PROVIDES_BACKOFFICE {margin_pct: 0.05, sla_hours: 24}]->(re)
CREATE (ops)-[:PROVIDES_BACKOFFICE {margin_pct: 0.05, sla_hours: 24}]->(fin)

// 5. SIMULATE A LIVE DELEGATION CYCLE (Monday Launch)
// Step A: CON needs an electrician
CREATE (opp:Opportunity {id: 'OPP-100', type: 'contractor_role', trade: 'electrician', value: 5000, urgency: 'high'})
CREATE (con)-[:GENERATES_OPPORTUNITY]->(opp)

// Step B: CON delegates to STA
CREATE (del:Delegation {id: 'DEL-100', status: 'completed', margin_captured: 1750, created_at: '2026-07-25T08:00:00Z', completed_at: '2026-07-25T14:00:00Z'})
CREATE (con)-[:DELEGATES_TO {type: 'labor_sourcing'}]->(del)
CREATE (del)-[:FULFILLED_BY]->(sta)
CREATE (opp)-[:RESOLVED_BY]->(del)

// Step C: Agents execute the delegation
CREATE (agent_sourcing)-[:EXECUTES]->(del);

// ============================================================================
// OPPORTUNITY GRAPH RELATIONSHIPS
// ============================================================================

// Constraints
CREATE CONSTRAINT company_id IF NOT EXISTS FOR (c:Company) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT deal_id IF NOT EXISTS FOR (dl:Deal) REQUIRE dl.id IS UNIQUE;

// Core B2B Opportunity mapping nodes
CREATE (co_seller:Company {id: 'COM-101', name: 'Queen City Excavation', industry: 'Construction', location: 'Charlotte, NC', size: 'Medium'})
CREATE (co_buyer:Company {id: 'COM-102', name: 'Metrolina Logistics Hub', industry: 'Transportation', location: 'Charlotte, NC', size: 'Large'})
CREATE (co_broker:Company {id: 'DEAL-001', name: 'Worldwidebro Deal Flow Agency', industry: 'Brokerage', location: 'Charlotte, NC'})

CREATE (excavator:Asset {id: 'AST-201', type: 'equipment', value: 200000, availability: 'immediate', description: 'Surplus Caterpillar 320 Excavator'})
CREATE (grading_need:Need {id: 'NED-301', requirement: 'site_grading_machinery', budget: 250000, deadline: '2026-09-01'})

// Connect company ownership and requirements
CREATE (co_seller)-[:OWNS]->(excavator)
CREATE (co_buyer)-[:HAS_NEED]->(grading_need)

// Matchmaker links assets to demands
CREATE (excavator)-[:MATCHES {score: 0.94, confidence: 'high'}]->(grading_need)

// Broker tracks the resulting deal
CREATE (deal_b2b:Deal {id: 'DL-501', value: 200000, commission_pct: 0.05, commission_fee: 10000, status: 'discovered'})
CREATE (co_broker)-[:BROKERS]->(deal_b2b)
CREATE (deal_b2b)-[:SELLER]->(co_seller)
CREATE (deal_b2b)-[:BUYER]->(co_buyer)
CREATE (deal_b2b)-[:ASSET]->(excavator)
CREATE (deal_b2b)-[:NEED]->(grading_need)

