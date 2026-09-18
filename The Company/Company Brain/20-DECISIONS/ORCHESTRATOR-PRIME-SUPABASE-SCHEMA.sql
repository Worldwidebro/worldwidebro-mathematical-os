-- ============================================================
-- ORCHESTRATOR PRIME SUPABASE SCHEMA
-- Tables to support task routing, execution, and revenue attribution
-- ============================================================

-- 1. AGENT REGISTRY (read-only copy of AGENTS_INVENTORY_318.yaml)
CREATE TABLE IF NOT EXISTS agent_registry (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  domain TEXT,
  description TEXT,
  autonomy_level TEXT CHECK(autonomy_level IN ('L1', 'L2', 'L3')),
  status TEXT CHECK(status IN ('READY', 'BUILDING', 'ARCHIVED')),
  deployed BOOLEAN DEFAULT false,
  capabilities TEXT[] DEFAULT ARRAY[]::TEXT[],
  cost_per_invocation DECIMAL(10, 4) DEFAULT 0,
  estimated_revenue DECIMAL(12, 2) DEFAULT 0,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_agent_registry_category ON agent_registry(category);
CREATE INDEX idx_agent_registry_status ON agent_registry(status);
CREATE INDEX idx_agent_registry_deployed ON agent_registry(deployed);

-- 2. TASK QUEUE (incoming tasks)
CREATE TABLE IF NOT EXISTS task_queue (
  id TEXT PRIMARY KEY,
  description TEXT NOT NULL,
  venture_id TEXT NOT NULL,
  urgency TEXT DEFAULT 'medium' CHECK(urgency IN ('high', 'medium', 'low')),
  budget DECIMAL(12, 2),
  revenue_target DECIMAL(12, 2),
  status TEXT DEFAULT 'queued' CHECK(status IN ('queued', 'processing', 'completed', 'failed')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_by TEXT,
  metadata JSONB DEFAULT '{}'
);

CREATE INDEX idx_task_queue_venture ON task_queue(venture_id);
CREATE INDEX idx_task_queue_status ON task_queue(status);
CREATE INDEX idx_task_queue_created_at ON task_queue(created_at DESC);

-- 3. TASK EXECUTIONS (who ran what, when, with what cost/outcome)
CREATE TABLE IF NOT EXISTS task_executions (
  id BIGSERIAL PRIMARY KEY,
  task_id TEXT NOT NULL REFERENCES task_queue(id),
  agent_id TEXT NOT NULL REFERENCES agent_registry(id),
  venture_id TEXT NOT NULL,
  status TEXT DEFAULT 'queued' CHECK(status IN ('queued', 'in_progress', 'completed', 'failed')),
  task_description TEXT,
  cost_estimated DECIMAL(10, 4),
  cost_actual DECIMAL(10, 4),
  revenue_estimated DECIMAL(12, 2),
  revenue_actual DECIMAL(12, 2),
  outcome JSONB DEFAULT '{}',
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  CONSTRAINT fk_task_id FOREIGN KEY(task_id) REFERENCES task_queue(id) ON DELETE CASCADE
);

CREATE INDEX idx_task_executions_task_id ON task_executions(task_id);
CREATE INDEX idx_task_executions_agent_id ON task_executions(agent_id);
CREATE INDEX idx_task_executions_venture_id ON task_executions(venture_id);
CREATE INDEX idx_task_executions_status ON task_executions(status);
CREATE INDEX idx_task_executions_created_at ON task_executions(created_at DESC);

-- 4. REVENUE LOG (revenue attribution per task/agent/venture)
CREATE TABLE IF NOT EXISTS revenue_log (
  id BIGSERIAL PRIMARY KEY,
  task_id TEXT NOT NULL,
  agent_id TEXT NOT NULL REFERENCES agent_registry(id),
  venture_id TEXT NOT NULL,
  revenue DECIMAL(12, 2) NOT NULL,
  cost DECIMAL(10, 4) NOT NULL,
  roi DECIMAL(8, 2), -- (revenue / cost)
  source TEXT DEFAULT 'execution', -- 'execution', 'manual', 'webhook'
  recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB DEFAULT '{}',
  CONSTRAINT fk_task_id_revenue FOREIGN KEY(task_id) REFERENCES task_queue(id) ON DELETE SET NULL
);

CREATE INDEX idx_revenue_log_task_id ON revenue_log(task_id);
CREATE INDEX idx_revenue_log_agent_id ON revenue_log(agent_id);
CREATE INDEX idx_revenue_log_venture_id ON revenue_log(venture_id);
CREATE INDEX idx_revenue_log_recorded_at ON revenue_log(recorded_at DESC);

-- 5. AGENT STATS (aggregated metrics per agent)
CREATE TABLE IF NOT EXISTS agent_stats (
  agent_id TEXT PRIMARY KEY REFERENCES agent_registry(id) ON DELETE CASCADE,
  tasks_completed INT DEFAULT 0,
  tasks_failed INT DEFAULT 0,
  total_revenue DECIMAL(14, 2) DEFAULT 0,
  total_cost DECIMAL(12, 4) DEFAULT 0,
  roi_average DECIMAL(8, 2), -- (total_revenue / total_cost)
  success_rate DECIMAL(5, 2), -- percentage 0-100
  avg_cost_per_task DECIMAL(10, 4),
  avg_revenue_per_task DECIMAL(12, 2),
  last_executed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_agent_stats_roi ON agent_stats(roi_average DESC);
CREATE INDEX idx_agent_stats_success_rate ON agent_stats(success_rate DESC);

-- 6. VENTURE SUMMARY (revenue by venture)
CREATE TABLE IF NOT EXISTS venture_revenue_summary (
  venture_id TEXT PRIMARY KEY,
  total_tasks INT DEFAULT 0,
  total_revenue DECIMAL(14, 2) DEFAULT 0,
  total_cost DECIMAL(12, 4) DEFAULT 0,
  roi DECIMAL(8, 2),
  agents_active INT DEFAULT 0,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_venture_revenue_summary_total_revenue ON venture_revenue_summary(total_revenue DESC);

-- ============================================================
-- VIEWS FOR DASHBOARD QUERIES
-- ============================================================

-- Agent leaderboard (best ROI)
CREATE OR REPLACE VIEW agent_leaderboard AS
SELECT
  ar.id,
  ar.name,
  ar.category,
  COALESCE(ast.tasks_completed, 0) as tasks_completed,
  COALESCE(ast.total_revenue, 0) as total_revenue,
  COALESCE(ast.roi_average, 0) as roi_average,
  COALESCE(ast.success_rate, 0) as success_rate,
  ar.cost_per_invocation,
  ast.last_executed_at,
  ast.updated_at
FROM agent_registry ar
LEFT JOIN agent_stats ast ON ar.id = ast.agent_id
WHERE ar.status = 'READY'
ORDER BY COALESCE(ast.roi_average, 0) DESC;

-- Revenue by venture (last 30 days)
CREATE OR REPLACE VIEW venture_revenue_30d AS
SELECT
  rl.venture_id,
  COUNT(DISTINCT rl.task_id) as tasks,
  COUNT(DISTINCT rl.agent_id) as agents_used,
  SUM(rl.revenue) as total_revenue,
  SUM(rl.cost) as total_cost,
  ROUND(SUM(rl.revenue) / NULLIF(SUM(rl.cost), 0), 2) as roi,
  MAX(rl.recorded_at) as last_revenue
FROM revenue_log rl
WHERE rl.recorded_at >= CURRENT_TIMESTAMP - INTERVAL '30 days'
GROUP BY rl.venture_id
ORDER BY total_revenue DESC;

-- Task execution summary (by status)
CREATE OR REPLACE VIEW task_execution_summary AS
SELECT
  te.status,
  COUNT(*) as count,
  COUNT(DISTINCT te.agent_id) as agents_involved,
  ROUND(AVG(te.cost_actual), 4) as avg_cost,
  ROUND(AVG(te.revenue_actual), 2) as avg_revenue,
  MIN(te.created_at) as first_execution,
  MAX(te.completed_at) as last_execution
FROM task_executions te
GROUP BY te.status;

-- ============================================================
-- FUNCTIONS FOR AUTOMATION
-- ============================================================

-- Update agent stats when revenue is logged
CREATE OR REPLACE FUNCTION update_agent_stats()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO agent_stats (agent_id)
  VALUES (NEW.agent_id)
  ON CONFLICT (agent_id) DO UPDATE SET
    total_revenue = total_revenue + NEW.revenue,
    total_cost = total_cost + NEW.cost,
    roi_average = CASE
      WHEN (total_cost + NEW.cost) > 0
      THEN (total_revenue + NEW.revenue) / (total_cost + NEW.cost)
      ELSE 0
    END,
    updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_agent_stats
AFTER INSERT ON revenue_log
FOR EACH ROW
EXECUTE FUNCTION update_agent_stats();

-- Update venture summary when revenue is logged
CREATE OR REPLACE FUNCTION update_venture_summary()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO venture_revenue_summary (venture_id)
  VALUES (NEW.venture_id)
  ON CONFLICT (venture_id) DO UPDATE SET
    total_revenue = total_revenue + NEW.revenue,
    total_cost = total_cost + NEW.cost,
    roi = CASE
      WHEN (total_cost + NEW.cost) > 0
      THEN (total_revenue + NEW.revenue) / (total_cost + NEW.cost)
      ELSE 0
    END,
    last_updated = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_venture_summary
AFTER INSERT ON revenue_log
FOR EACH ROW
EXECUTE FUNCTION update_venture_summary();

-- ============================================================
-- INITIAL DATA (Bootstrap with ready agents)
-- ============================================================

-- Insert key revenue agents (manually for now, auto-seed from AGENTS_INVENTORY_318.yaml later)
INSERT INTO agent_registry (
  id,
  name,
  category,
  domain,
  description,
  autonomy_level,
  status,
  cost_per_invocation,
  estimated_revenue
) VALUES
  (
    'agent-revenue-cold-email-writer-001',
    'Cold Email Writer',
    'sales',
    '14-CAPABILITIES',
    'Writes and personalizes cold email campaigns for lead generation',
    'L2',
    'READY',
    0.25,
    1500.00
  ),
  (
    'agent-revenue-discovery-caller-001',
    'Discovery Caller',
    'sales',
    '14-CAPABILITIES',
    'Qualifies leads and schedules discovery calls',
    'L2',
    'READY',
    0.50,
    2500.00
  ),
  (
    'agent-revenue-proposal-generator-001',
    'Proposal Generator',
    'sales',
    '14-CAPABILITIES',
    'Generates customized proposals based on discovery calls',
    'L2',
    'READY',
    0.75,
    3000.00
  ),
  (
    'agent-revenue-closer-001',
    'Deal Closer',
    'sales',
    '14-CAPABILITIES',
    'Closes deals and handles final negotiations',
    'L2',
    'READY',
    1.00,
    5000.00
  ),
  (
    'agent-revenue-invoice-tracker-001',
    'Invoice Tracker',
    'sales',
    '14-CAPABILITIES',
    'Sends invoices and tracks payment status',
    'L1',
    'READY',
    0.10,
    500.00
  )
ON CONFLICT (id) DO NOTHING;

-- ============================================================
-- ENABLE ROW LEVEL SECURITY (Optional)
-- ============================================================

-- Uncomment to enable RLS:
-- ALTER TABLE task_queue ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE task_executions ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE revenue_log ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE agent_stats ENABLE ROW LEVEL SECURITY;

-- CREATE POLICY "Users can see their own venture tasks"
-- ON task_queue FOR SELECT
-- USING (venture_id IN (SELECT venture_id FROM user_ventures WHERE user_id = auth.uid()));

-- ============================================================
-- SCHEMA SETUP COMPLETE
-- ============================================================
-- Run with: psql -U postgres -h localhost -d company_brain -f orchestrator-prime-supabase-schema.sql
