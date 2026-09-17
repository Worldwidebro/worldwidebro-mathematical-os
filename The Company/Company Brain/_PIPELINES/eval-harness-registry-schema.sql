-- Eval Harness Registry (PostgreSQL)
-- Purpose: Centralize evaluation configuration, test cases, and LangSmith integration
-- Status: Day 1 implementation (Sep 17, 2026)

CREATE SCHEMA IF NOT EXISTS eval;

-- 1. Eval Frameworks (deepeval, LangSmith, custom)
CREATE TABLE eval.frameworks (
  id SERIAL PRIMARY KEY,
  framework_id VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  provider VARCHAR(100),  -- "deepeval" | "langsmith" | "custom"
  version VARCHAR(50),
  api_endpoint VARCHAR(500),
  auth_method VARCHAR(50),  -- "api_key" | "oauth" | "none"
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 2. Evaluation Types (unit, integration, agent, trajectory, etc.)
CREATE TABLE eval.eval_types (
  id SERIAL PRIMARY KEY,
  type_id VARCHAR(100) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  framework_id VARCHAR(50) REFERENCES eval.frameworks(framework_id),
  rubric JSONB,  -- Scoring criteria per eval type
  created_at TIMESTAMP DEFAULT NOW()
);

-- 3. Test Cases (reusable test datasets)
CREATE TABLE eval.test_cases (
  id SERIAL PRIMARY KEY,
  test_case_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100),  -- Which agent (AGT-001, etc.) or null for general
  input TEXT NOT NULL,
  expected_output TEXT,
  eval_type_id VARCHAR(100) REFERENCES eval.eval_types(type_id),
  difficulty VARCHAR(20),  -- "easy" | "medium" | "hard"
  created_at TIMESTAMP DEFAULT NOW()
);

-- 4. Evaluation Runs (execution history + results)
CREATE TABLE eval.evaluation_runs (
  id SERIAL PRIMARY KEY,
  run_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100) NOT NULL,
  framework_id VARCHAR(50) REFERENCES eval.frameworks(framework_id),
  eval_type_id VARCHAR(100) REFERENCES eval.eval_types(type_id),
  test_cases_run INT,
  passed INT,
  failed INT,
  pass_rate DECIMAL(5, 2),  -- 0.00 to 100.00
  regression_detected BOOLEAN,
  langsmith_trace_url VARCHAR(500),
  execution_time_ms INT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- 5. Guardrails (thresholds for agent certification)
CREATE TABLE eval.guardrails (
  id SERIAL PRIMARY KEY,
  guardrail_id VARCHAR(100) UNIQUE NOT NULL,
  agent_id VARCHAR(100),  -- null = global default
  dimension VARCHAR(100),  -- "correctness" | "speed" | "safety" | "cost"
  min_pass_rate DECIMAL(5, 2),
  timeout_ms INT,
  max_cost_per_call DECIMAL(10, 4),
  is_blocking BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT NOW()
);

-- 6. Agent Eval Profiles (per-agent eval configuration)
CREATE TABLE eval.agent_profiles (
  id SERIAL PRIMARY KEY,
  agent_id VARCHAR(100) UNIQUE NOT NULL,
  eval_framework VARCHAR(50),  -- "deepeval" | "langsmith" | "both"
  last_eval_run_id VARCHAR(100) REFERENCES eval.evaluation_runs(run_id),
  last_eval_date TIMESTAMP,
  eval_frequency_hours INT,  -- Auto-run every N hours
  is_certified BOOLEAN DEFAULT false,
  certification_date TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_agent_eval ON eval.evaluation_runs(agent_id, created_at DESC);
CREATE INDEX idx_framework ON eval.frameworks(framework_id);
CREATE INDEX idx_eval_type ON eval.eval_types(type_id);
