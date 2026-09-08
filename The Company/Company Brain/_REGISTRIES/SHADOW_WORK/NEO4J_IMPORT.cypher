// ==============================================================================
// NEO4J IMPORT: Shadow Work Knowledge Graph (SW-KG)
// Version: 1.0.0
// Target: bolt://100.87.214.70:7687 (Mac Studio Canonical Neo4j)
// Authority: Knowledge Control Plane (CP-013) & System Infrastructure (CP-027)
// ==============================================================================

// ------------------------------------------------------------------------------
// PHASE 1: CONSTRAINTS & INDEXES
// ------------------------------------------------------------------------------
CREATE CONSTRAINT cst_sw_id IF NOT EXISTS FOR (s:ShadowWork) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT cst_cb_id IF NOT EXISTS FOR (b:CognitiveBias) REQUIRE b.id IS UNIQUE;
CREATE CONSTRAINT cst_op_id IF NOT EXISTS FOR (o:OperatingProblem) REQUIRE o.id IS UNIQUE;
CREATE CONSTRAINT cst_br_id IF NOT EXISTS FOR (r:BusinessRisk) REQUIRE r.id IS UNIQUE;
CREATE CONSTRAINT cst_opr_id IF NOT EXISTS FOR (m:OperatingResponse) REQUIRE m.id IS UNIQUE;
CREATE CONSTRAINT cst_domain_id IF NOT EXISTS FOR (d:AcademicDomain) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT cst_wikidata_qid IF NOT EXISTS FOR (w:WikidataEntity) REQUIRE w.qid IS UNIQUE;

// ------------------------------------------------------------------------------
// PHASE 2: ACADEMIC DOMAINS (WIKIPEDIA / WIKIDATA GROUNDING)
// ------------------------------------------------------------------------------
MERGE (d1:AcademicDomain {id: "DOM-01", name: "Psychology / Self", wikidata_qid: "Q1542159", wikipedia_url: "https://en.wikipedia.org/wiki/Self-determination_theory"})
MERGE (d2:AcademicDomain {id: "DOM-02", name: "Cognitive Science & Decision Theory", wikidata_qid: "Q849477", wikipedia_url: "https://en.wikipedia.org/wiki/Decision-making"})
MERGE (d3:AcademicDomain {id: "DOM-03", name: "Behavioral Economics & Capital Allocation", wikidata_qid: "Q625418", wikipedia_url: "https://en.wikipedia.org/wiki/Behavioral_economics"})
MERGE (d4:AcademicDomain {id: "DOM-04", name: "Organizational Behavior & Governance", wikidata_qid: "Q1417088", wikipedia_url: "https://en.wikipedia.org/wiki/Organizational_behavior"})
MERGE (d5:AcademicDomain {id: "DOM-05", name: "Operations Management & Lean Systems", wikidata_qid: "Q688941", wikipedia_url: "https://en.wikipedia.org/wiki/Theory_of_constraints"})
MERGE (d6:AcademicDomain {id: "DOM-06", name: "Philosophy & Existential Meaning", wikidata_qid: "Q48232", wikipedia_url: "https://en.wikipedia.org/wiki/Stoicism"})
MERGE (d7:AcademicDomain {id: "DOM-07", name: "Stress & Cognitive Performance", wikidata_qid: "Q5141203", wikipedia_url: "https://en.wikipedia.org/wiki/Cognitive_resource_theory"});

// ------------------------------------------------------------------------------
// PHASE 3: SHADOW WORK NODES (SW-*)
// ------------------------------------------------------------------------------
MERGE (sw1:ShadowWork {
  id: "SW-EGO-001",
  name: "Ego",
  slug: "ego",
  definition: "A person's sense of self-importance, identity, status, or self-concept that can distort judgment, prevent disconfirmation, or induce defensive behavior.",
  wikidata_qid: "Q484678",
  wikidata_uri: "https://www.wikidata.org/entity/Q484678",
  wikipedia_url: "https://en.wikipedia.org/wiki/Ego",
  dbpedia_uri: "http://dbpedia.org/resource/Ego",
  severity: "critical",
  timeframe: "daily"
});

MERGE (sw2:ShadowWork {
  id: "SW-COMP-001",
  name: "Complexity Addiction",
  slug: "complexity-addiction",
  definition: "The psychological compulsion to accumulate systems, repositories, architectures, and entities to simulate progress while avoiding direct market confrontation.",
  wikidata_qid: "Q1360677",
  wikidata_uri: "https://www.wikidata.org/entity/Q1360677",
  wikipedia_url: "https://en.wikipedia.org/wiki/Illusion_of_control",
  dbpedia_uri: "http://dbpedia.org/resource/Illusion_of_control",
  severity: "critical",
  timeframe: "daily"
});

MERGE (sw3:ShadowWork {
  id: "SW-FEAR-001",
  name: "Fear of Failure",
  slug: "fear-of-failure",
  definition: "Anticipatory anxiety regarding commercial, intellectual, or reputational defeat leading to paralysis, over-preparation, or risk-elimination behavior.",
  wikidata_qid: "Q1197479",
  wikidata_uri: "https://www.wikidata.org/entity/Q1197479",
  wikipedia_url: "https://en.wikipedia.org/wiki/Loss_aversion",
  dbpedia_uri: "http://dbpedia.org/resource/Loss_aversion",
  severity: "critical",
  timeframe: "daily"
});

MERGE (sw4:ShadowWork {
  id: "SW-MONEY-001",
  name: "Scarcity Mindset & Revenue Avoidance",
  slug: "scarcity-mindset",
  definition: "A fixation on zero-cost resources, free tiers, and penny-pinching compute that subverts high-leverage commercial sales, investment, and bold capital allocation.",
  wikidata_qid: "Q377858",
  wikidata_uri: "https://www.wikidata.org/entity/Q377858",
  wikipedia_url: "https://en.wikipedia.org/wiki/Prospect_theory",
  dbpedia_uri: "http://dbpedia.org/resource/Prospect_theory",
  severity: "high",
  timeframe: "weekly"
});

MERGE (sw5:ShadowWork {
  id: "SW-BOTTLENECK-001",
  name: "Founder Bottleneck & God-King Delusion",
  slug: "founder-bottleneck",
  definition: "The psychological refusal to delegate authority, context, and outcomes, forcing every technical and business decision through the founder's personal terminal.",
  wikidata_qid: "Q1424911",
  wikidata_uri: "https://www.wikidata.org/entity/Q1424911",
  wikipedia_url: "https://en.wikipedia.org/wiki/Span_of_control",
  dbpedia_uri: "http://dbpedia.org/resource/Span_of_control",
  severity: "critical",
  timeframe: "weekly"
});

// ------------------------------------------------------------------------------
// PHASE 4: COGNITIVE BIASES (CB-*)
// ------------------------------------------------------------------------------
MERGE (cb1:CognitiveBias {id: "CB-001", name: "Confirmation Bias", wikidata_qid: "Q189283", wikipedia_url: "https://en.wikipedia.org/wiki/Confirmation_bias"});
MERGE (cb2:CognitiveBias {id: "CB-002", name: "Anchoring Effect", wikidata_qid: "Q489110", wikipedia_url: "https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)"});
MERGE (cb5:CognitiveBias {id: "CB-005", name: "Loss Aversion", wikidata_qid: "Q1197479", wikipedia_url: "https://en.wikipedia.org/wiki/Loss_aversion"});
MERGE (cb6:CognitiveBias {id: "CB-006", name: "Overconfidence Effect", wikidata_qid: "Q1071295", wikipedia_url: "https://en.wikipedia.org/wiki/Overconfidence_effect"});
MERGE (cb9:CognitiveBias {id: "CB-009", name: "Sunk Cost Fallacy", wikidata_qid: "Q214430", wikipedia_url: "https://en.wikipedia.org/wiki/Sunk_cost"});
MERGE (cb10:CognitiveBias {id: "CB-010", name: "Escalation of Commitment", wikidata_qid: "Q1366914", wikipedia_url: "https://en.wikipedia.org/wiki/Escalation_of_commitment"});
MERGE (cb11:CognitiveBias {id: "CB-011", name: "Illusion of Control", wikidata_qid: "Q1360677", wikipedia_url: "https://en.wikipedia.org/wiki/Illusion_of_control"});
MERGE (cb12:CognitiveBias {id: "CB-012", name: "Self-Serving Bias", wikidata_qid: "Q1143892", wikipedia_url: "https://en.wikipedia.org/wiki/Self-serving_bias"});
MERGE (cb16:CognitiveBias {id: "CB-016", name: "Fundamental Attribution Error", wikidata_qid: "Q596541", wikipedia_url: "https://en.wikipedia.org/wiki/Fundamental_attribution_error"});
MERGE (cb30:CognitiveBias {id: "CB-030", name: "Decision Fatigue", wikidata_qid: "Q1182285", wikipedia_url: "https://en.wikipedia.org/wiki/Decision_fatigue"});

// ------------------------------------------------------------------------------
// PHASE 5: OPERATING PROBLEMS (OP-*)
// ------------------------------------------------------------------------------
MERGE (op1:OperatingProblem {id: "OP-001", name: "Complexity Addiction", description: "Confusing systems, repos, and agents with actual economic progress."});
MERGE (op2:OperatingProblem {id: "OP-002", name: "Tool Accumulation", description: "Collecting developer tools, APIs, and frameworks without clear workflows."});
MERGE (op3:OperatingProblem {id: "OP-003", name: "Repository Accumulation", description: "Accumulating hundreds of code repos with zero commercial velocity."});
MERGE (op11:OperatingProblem {id: "OP-011", name: "Execution Avoidance", description: "Hiding in internal development to avoid the vulnerability of customer contact."});
MERGE (op12:OperatingProblem {id: "OP-012", name: "Sales Avoidance", description: "Refusing to ask for money or propose commercial contracts."});
MERGE (op13:OperatingProblem {id: "OP-013", name: "Customer Avoidance", description: "Building in isolation without showing progress to real prospective buyers."});
MERGE (op14:OperatingProblem {id: "OP-014", name: "Delegation Resistance", description: "Believing nobody can execute tasks to the founder's subjective standard."});
MERGE (op15:OperatingProblem {id: "OP-015", name: "Founder Bottleneck", description: "All decisions, approvals, and credentials requiring founder manual intervention."});
MERGE (op17:OperatingProblem {id: "OP-017", name: "Failure to Kill Projects", description: "Protecting zombie projects because of past invested time or emotional pride."});
MERGE (op23:OperatingProblem {id: "OP-023", name: "Overengineering", description: "Designing enterprise-grade abstraction layers for simple disposable scripts."});
MERGE (op27:OperatingProblem {id: "OP-027", name: "Metrics Theater", description: "Displaying impressive technical counters that have zero relationship to cash flow."});

// ------------------------------------------------------------------------------
// PHASE 6: BUSINESS RISKS (BR-*)
// ------------------------------------------------------------------------------
MERGE (br1:BusinessRisk {id: "BR-001", name: "Bad Capital Allocation", severity: "CRITICAL"});
MERGE (br2:BusinessRisk {id: "BR-002", name: "Strategic Drift", severity: "HIGH"});
MERGE (br3:BusinessRisk {id: "BR-003", name: "Founder Bottleneck Paralysis", severity: "CRITICAL"});
MERGE (br4:BusinessRisk {id: "BR-004", name: "Slow Execution Velocity", severity: "HIGH"});
MERGE (br8:BusinessRisk {id: "BR-008", name: "Cash-Flow Insolvency", severity: "CRITICAL"});
MERGE (br10:BusinessRisk {id: "BR-010", name: "Operational Fragility", severity: "HIGH"});
MERGE (br14:BusinessRisk {id: "BR-014", name: "Massive Opportunity Cost", severity: "CRITICAL"});
MERGE (br16:BusinessRisk {id: "BR-016", name: "Excessive Structural Complexity", severity: "HIGH"});
MERGE (br22:BusinessRisk {id: "BR-022", name: "Capital Destruction", severity: "CRITICAL"});
MERGE (br23:BusinessRisk {id: "BR-023", name: "Extreme Founder Dependency", severity: "CRITICAL"});

// ------------------------------------------------------------------------------
// PHASE 7: COUNTERMEASURES / OPERATING RESPONSES (OPR-*)
// ------------------------------------------------------------------------------
MERGE (opr1:OperatingResponse {id: "OPR-001", name: "Mandatory Red-Team Review", cadence: "Pre-Decision"});
MERGE (opr2:OperatingResponse {id: "OPR-002", name: "Pre-Mortem Analysis", cadence: "Pre-Execution"});
MERGE (opr4:OperatingResponse {id: "OPR-004", name: "Decision Journaling Protocol", cadence: "Per-Major-Decision"});
MERGE (opr5:OperatingResponse {id: "OPR-005", name: "Explicit Kill Criteria", cadence: "Pre-Commitment"});
MERGE (opr6:OperatingResponse {id: "OPR-006", name: "Stop-Doing List", cadence: "Weekly"});
MERGE (opr7:OperatingResponse {id: "OPR-007", name: "Delegation & Authority Matrix", cadence: "Monthly"});
MERGE (opr9:OperatingResponse {id: "OPR-009", name: "Weekly Cadence Review", cadence: "Weekly"});
MERGE (opr12:OperatingResponse {id: "OPR-012", name: "Customer Feedback Interviews", cadence: "Weekly"});
MERGE (opr14:OperatingResponse {id: "OPR-014", name: "Unit Economics Audit", cadence: "Monthly"});
MERGE (opr18:OperatingResponse {id: "OPR-018", name: "Theory of Constraints Analysis", cadence: "Monthly"});
MERGE (opr24:OperatingResponse {id: "OPR-024", name: "Founder Dependency Audit", cadence: "Monthly"});
MERGE (opr25:OperatingResponse {id: "OPR-025", name: "Complexity Pruning Audit", cadence: "Monthly"});

// ------------------------------------------------------------------------------
// PHASE 9: WEIGHTS, ANCHORS, FOUNDATIONS & TRANSMUTATIONS
// ------------------------------------------------------------------------------
CREATE CONSTRAINT cst_weight_id IF NOT EXISTS FOR (w:OperationalWeight) REQUIRE w.id IS UNIQUE;
CREATE CONSTRAINT cst_anchor_id IF NOT EXISTS FOR (a:OperatingAnchor) REQUIRE a.id IS UNIQUE;
CREATE CONSTRAINT cst_foundation_id IF NOT EXISTS FOR (f:OperatingFoundation) REQUIRE f.id IS UNIQUE;
CREATE CONSTRAINT cst_transmutation_id IF NOT EXISTS FOR (t:TransmutationVector) REQUIRE t.id IS UNIQUE;

// SEED ANCHORS
MERGE (anc1:OperatingAnchor {id: "ANC-001", attachment: "I have to do everything myself.", release_condition: "I build systems and people that make me unnecessary."});
MERGE (anc2:OperatingAnchor {id: "ANC-002", attachment: "My value equals my productivity.", release_condition: "My value is not measured by how exhausted I am."});
MERGE (anc5:OperatingAnchor {id: "ANC-005", attachment: "More projects means more opportunity.", release_condition: "Focused execution creates more opportunity than scattered ambition."});
MERGE (anc9:OperatingAnchor {id: "ANC-009", attachment: "Attachment to complexity", release_condition: "Evidence outranks attachment."});
MERGE (anc26:OperatingAnchor {id: "ANC-026", attachment: "The Emperor's Infrastructure (100s repos, dozens systems)", release_condition: "Reduce to 5 systems -> 3 -> 1. Keep only what directly produces cash."});

// SEED WEIGHTS
MERGE (wgt9:OperationalWeight {id: "WGT-009", name: "Too many simultaneous priorities", category: "execution", drain_type: "attention"});
MERGE (wgt14:OperationalWeight {id: "WGT-014", name: "Overengineering", category: "execution", drain_type: "capital"});
MERGE (wgt17:OperationalWeight {id: "WGT-017", name: "Repository accumulation", category: "execution", drain_type: "attention"});
MERGE (wgt25:OperationalWeight {id: "WGT-025", name: "Founder dependency", category: "business", drain_type: "energy"});
MERGE (wgt35:OperationalWeight {id: "WGT-035", name: "Perfectionism", category: "mental", drain_type: "time"});

// SEED FOUNDATIONS (DO NOT RELEASE)
MERGE (fnd1:OperatingFoundation {id: "FND-001", name: "Values", role: "Uncompromising moral baseline"});
MERGE (fnd2:OperatingFoundation {id: "FND-002", name: "Ethics", role: "Fiduciary and human integrity"});
MERGE (fnd3:OperatingFoundation {id: "FND-003", name: "Health", role: "Biological and cognitive substrate"});
MERGE (fnd4:OperatingFoundation {id: "FND-004", name: "Family Responsibilities", role: "Relational duty and grounding"});
MERGE (fnd7:OperatingFoundation {id: "FND-007", name: "Customer Trust", role: "The ultimate commercial moat"});
MERGE (fnd11:OperatingFoundation {id: "FND-011", name: "Discipline", role: "Execution independent of motivation"});

// SEED TRANSMUTATIONS
MERGE (trn1:TransmutationVector {id: "TRN-001", from_state: "FEAR", to_state: "PRINCIPLE"});
MERGE (trn2:TransmutationVector {id: "TRN-002", from_state: "EGO", to_state: "EVIDENCE"});
MERGE (trn4:TransmutationVector {id: "TRN-004", from_state: "CONTROL", to_state: "TRUST + VERIFICATION"});
MERGE (trn5:TransmutationVector {id: "TRN-005", from_state: "COMPLEXITY", to_state: "SIMPLICITY"});
MERGE (trn7:TransmutationVector {id: "TRN-007", from_state: "BUSYNESS", to_state: "LEVERAGE"});
MERGE (trn9:TransmutationVector {id: "TRN-009", from_state: "FOMO", to_state: "FOCUS"});


// ------------------------------------------------------------------------------
// PHASE 10: RELATIONSHIP GRAPH WIRING (MATCH & MERGE)
// ------------------------------------------------------------------------------
// EGO WIRING
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (d:AcademicDomain {id: "DOM-01"}) MERGE (s)-[:GROUNDED_IN]->(d);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (cb:CognitiveBias {id: "CB-001"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (cb:CognitiveBias {id: "CB-012"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (op:OperatingProblem {id: "OP-015"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (br:BusinessRisk {id: "BR-001"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (br:BusinessRisk {id: "BR-002"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (opr:OperatingResponse {id: "OPR-001"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (opr:OperatingResponse {id: "OPR-004"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-EGO-001"}), (t:TransmutationVector {id: "TRN-002"}) MERGE (s)-[:TRANSMUTES_VIA]->(t);

// COMPLEXITY ADDICTION WIRING
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (d:AcademicDomain {id: "DOM-05"}) MERGE (s)-[:GROUNDED_IN]->(d);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (cb:CognitiveBias {id: "CB-011"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (cb:CognitiveBias {id: "CB-006"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (op:OperatingProblem {id: "OP-001"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (op:OperatingProblem {id: "OP-002"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (op:OperatingProblem {id: "OP-003"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (op:OperatingProblem {id: "OP-023"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (br:BusinessRisk {id: "BR-004"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (br:BusinessRisk {id: "BR-010"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (br:BusinessRisk {id: "BR-016"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (opr:OperatingResponse {id: "OPR-006"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (opr:OperatingResponse {id: "OPR-018"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (opr:OperatingResponse {id: "OPR-025"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (anc:OperatingAnchor {id: "ANC-009"}) MERGE (s)-[:HELD_BY_ANCHOR]->(anc);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (anc:OperatingAnchor {id: "ANC-026"}) MERGE (s)-[:HELD_BY_ANCHOR]->(anc);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (wgt:OperationalWeight {id: "WGT-014"}) MERGE (s)-[:EXERTS_WEIGHT]->(wgt);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (wgt:OperationalWeight {id: "WGT-017"}) MERGE (s)-[:EXERTS_WEIGHT]->(wgt);
MATCH (s:ShadowWork {id: "SW-COMP-001"}), (t:TransmutationVector {id: "TRN-005"}) MERGE (s)-[:TRANSMUTES_VIA]->(t);

// FEAR OF FAILURE WIRING
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (d:AcademicDomain {id: "DOM-02"}) MERGE (s)-[:GROUNDED_IN]->(d);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (cb:CognitiveBias {id: "CB-005"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (op:OperatingProblem {id: "OP-011"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (op:OperatingProblem {id: "OP-013"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (br:BusinessRisk {id: "BR-014"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (opr:OperatingResponse {id: "OPR-002"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-FEAR-001"}), (t:TransmutationVector {id: "TRN-001"}) MERGE (s)-[:TRANSMUTES_VIA]->(t);

// SCARCITY & REVENUE AVOIDANCE WIRING
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (d:AcademicDomain {id: "DOM-03"}) MERGE (s)-[:GROUNDED_IN]->(d);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (cb:CognitiveBias {id: "CB-005"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (op:OperatingProblem {id: "OP-012"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (op:OperatingProblem {id: "OP-013"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (br:BusinessRisk {id: "BR-008"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (br:BusinessRisk {id: "BR-022"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (opr:OperatingResponse {id: "OPR-012"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-MONEY-001"}), (opr:OperatingResponse {id: "OPR-014"}) MERGE (s)-[:MANAGED_BY]->(opr);

// FOUNDER BOTTLENECK WIRING
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (d:AcademicDomain {id: "DOM-04"}) MERGE (s)-[:GROUNDED_IN]->(d);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (cb:CognitiveBias {id: "CB-016"}) MERGE (s)-[:MANIFESTS_AS]->(cb);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (op:OperatingProblem {id: "OP-014"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (op:OperatingProblem {id: "OP-015"}) MERGE (s)-[:PRODUCES]->(op);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (br:BusinessRisk {id: "BR-003"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (br:BusinessRisk {id: "BR-023"}) MERGE (s)-[:CAUSES_RISK]->(br);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (opr:OperatingResponse {id: "OPR-007"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (opr:OperatingResponse {id: "OPR-024"}) MERGE (s)-[:MANAGED_BY]->(opr);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (anc:OperatingAnchor {id: "ANC-001"}) MERGE (s)-[:HELD_BY_ANCHOR]->(anc);
MATCH (s:ShadowWork {id: "SW-BOTTLENECK-001"}), (wgt:OperationalWeight {id: "WGT-025"}) MERGE (s)-[:EXERTS_WEIGHT]->(wgt);

