-- Query 3: Skill Execution Timing
-- Shows performance metrics for each skill across all ventures
-- Used by: Obsidian (slowest skills leaderboard) + Grafana (skill performance chart)

SELECT
  se.skill_name,
  st.skill_phase,
  st.category,
  COUNT(*) as total_executions,
  COUNT(CASE WHEN se.status = 'completed' THEN 1 END) as successful_executions,
  COUNT(CASE WHEN se.status = 'failed' THEN 1 END) as failed_executions,
  ROUND(
    COUNT(CASE WHEN se.status = 'failed' THEN 1 END)::FLOAT /
    NULLIF(COUNT(*), 0) * 100, 2
  ) as failure_rate_percent,
  ROUND(AVG(se.execution_time_ms) / 1000, 2) as avg_execution_seconds,
  ROUND(MAX(se.execution_time_ms) / 1000, 2) as max_execution_seconds,
  ROUND(MIN(se.execution_time_ms) / 1000, 2) as min_execution_seconds,
  ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY se.execution_time_ms) / 1000, 2) as median_execution_seconds,
  MAX(se.completed_at) as last_execution_time,
  COUNT(DISTINCT se.venture_id) as unique_ventures_using
FROM skill_executions se
LEFT JOIN skill_taxonomy st ON se.skill_name = st.skill_name
WHERE se.status IN ('completed', 'failed')
GROUP BY se.skill_name, st.skill_phase, st.category
ORDER BY avg_execution_seconds DESC, total_executions DESC;
