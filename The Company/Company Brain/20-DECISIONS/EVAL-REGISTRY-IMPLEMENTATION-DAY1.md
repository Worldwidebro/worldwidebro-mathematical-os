# Eval Registry Implementation — Day 1 (Sep 17, 2026)

**Status:** 🚀 Ready to execute  
**Target:** Wired LangSmith + deepeval templates + Neo4j edges  
**Platform:** Supabase (aipehhzlsmfxxzwceppd.supabase.co)

---

## Deliverables

### 1. Eval Schema (Supabase PostgreSQL)

```sql
CREATE SCHEMA IF NOT EXISTS eval;

-- Frameworks (deepeval, LangSmith, custom)
CREATE TABLE eval.frameworks (
  id SERIAL PRIMARY KEY,
  framework_id VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  provider VARCHAR(100),
  version VARCHAR(50),
  api_endpoint VARCHAR(500),
  auth_method VARCHAR(50),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Evaluation types
CREATE TABLE eval.eval_types (
  id SERIAL PRIMARY KEY,
  type_id VARCHAR(100) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  framework_id VARCHAR(50) REFERENCES eval.frameworks(framework_id),
  rubric JSONB
);

-- Test cases
CREATE TABLE eval.test_cases (
  id SERIAL PRIMARY KEY,
  test_case_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100),
  input TEXT NOT NULL,
  expected_output TEXT,
  eval_type_id VARCHAR(100),
  difficulty VARCHAR(20)
);

-- Evaluation runs (execution history)
CREATE TABLE eval.evaluation_runs (
  id SERIAL PRIMARY KEY,
  run_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100) NOT NULL,
  framework_id VARCHAR(50),
  eval_type_id VARCHAR(100),
  test_cases_run INT,
  passed INT,
  failed INT,
  pass_rate DECIMAL(5, 2),
  regression_detected BOOLEAN,
  langsmith_trace_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Guardrails (certification thresholds)
CREATE TABLE eval.guardrails (
  id SERIAL PRIMARY KEY,
  guardrail_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100),
  dimension VARCHAR(100),
  min_pass_rate DECIMAL(5, 2),
  is_blocking BOOLEAN DEFAULT false
);

-- Agent profiles (per-agent eval config)
CREATE TABLE eval.agent_profiles (
  id SERIAL PRIMARY KEY,
  agent_id VARCHAR(100) UNIQUE NOT NULL,
  eval_framework VARCHAR(50),
  last_eval_run_id VARCHAR(100),
  last_eval_date TIMESTAMP,
  is_certified BOOLEAN DEFAULT false
);
```

**Action:** Apply via Supabase SQL editor or MCP `execute_sql`

---

### 2. LangSmith Integration Config

```yaml
# ~/.config/langsmith.env
LANGSMITH_API_KEY: <from Bitwarden>
LANGSMITH_ENDPOINT: https://api.smith.langchain.com
LANGSMITH_PROJECT: company-brain-evals

# In eval.frameworks table:
INSERT INTO eval.frameworks VALUES (
  framework_id='langsmith-001',
  name='LangSmith Cloud',
  provider='langsmith',
  version='0.1.0',
  api_endpoint='https://api.smith.langchain.com',
  auth_method='api_key',
  is_active=true
);
```

**Action:** Store API key in Bitwarden, load in eval agent

---

### 3. Deepeval Templates (Python)

```python
# _PIPELINES/deepeval-templates.py
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Template 1: Correctness (P0)
class CorrectnessEval:
    metric = AnswerRelevancyMetric(threshold=0.7)
    
    def test_case(self, agent_id, input_text, expected_output):
        return LLMTestCase(
            input=input_text,
            actual_output=expected_output,
            expected_output=expected_output,
        )

# Template 2: Speed (timeout check)
class SpeedEval:
    threshold_ms = 5000  # 5 second timeout
    
    def test(self, response_time_ms):
        return response_time_ms < self.threshold_ms

# Template 3: Safety (blocked terms, hallucinations)
class SafetyEval:
    blocked_patterns = [
        r"i don't know",
        r"cannot determine",
    ]
    
    def test(self, output_text):
        for pattern in self.blocked_patterns:
            if re.search(pattern, output_text, re.IGNORECASE):
                return False
        return True
```

**Action:** Wire to agent_profiles.eval_framework = 'deepeval'

---

### 4. Neo4j Edges (Knowledge Graph)

```cypher
-- Connect evaluation frameworks to capabilities
MATCH (cap:Capability {name: "Evaluation Engineering"})
MATCH (agent:Agent {agent_id: "AGT-001"})
CREATE (agent)-[:REQUIRES_EVAL {
  framework: "deepeval",
  min_pass_rate: 0.8,
  eval_type: "correctness",
  updated_at: datetime()
}]->(cap)

-- Mark evaluation loop as L2/L3 ready
MATCH (eval_cap:Capability {name: "Evaluation Engineering"})
SET eval_cap.loop_autonomy = "L2_SUPERVISED"
```

**Action:** Run Cypher queries via Neo4j browser or Bolt driver

---

### 5. VEX Component (Agent Harness Profile)

**Path:** `src/pages/CommandCenter/views/AgentHarnessProfile.tsx`

```typescript
export default function AgentHarnessProfile({ agentId }: Props) {
  const [evals, setEvals] = useState([]);
  const [status, setStatus] = useState('loading');

  useEffect(() => {
    // Query eval.evaluation_runs WHERE agent_id = agentId
    // Display: last_eval_date, pass_rate, is_certified, dimension scores
  }, [agentId]);

  return (
    <div className="harness-profile">
      <h2>{agentId} — Harness Profile</h2>
      <div className="grid grid-cols-7">
        {/* 7 dimensions from eval.guardrails */}
        <Dimension name="Correctness" score={...} />
        <Dimension name="Speed" score={...} />
        <Dimension name="Safety" score={...} />
        <Dimension name="Cost" score={...} />
        <Dimension name="Reliability" score={...} />
        <Dimension name="Observability" score={...} />
        <Dimension name="Certification" score={...} />
      </div>
      <div className="eval-history">
        {evals.map(run => (
          <EvalRun key={run.id} run={run} />
        ))}
      </div>
    </div>
  );
}
```

---

## Timeline

- **[ ] 15 min:** Apply Supabase schema (SQL)
- **[ ] 10 min:** Wire LangSmith API key
- **[ ] 20 min:** Create deepeval template library
- **[ ] 15 min:** Wire Neo4j edges (capability → agent → eval)
- **[ ] 20 min:** Build VEX AgentHarnessProfile component

**Total: ~80 min for full Day 1 Eval Registry**

---

## What's Next (Day 2–3)

- **Day 2:** Harness Profile component live in VEX
- **Day 3:** Auto-eval loop for 310 agents (L1 report-only)

---

## Dependencies

- ✅ Supabase live
- ✅ Neo4j live
- ✅ VEX dev server running
- ⏳ LangSmith API key (from Bitwarden)
- ⏳ deepeval Python library (install via pip)

