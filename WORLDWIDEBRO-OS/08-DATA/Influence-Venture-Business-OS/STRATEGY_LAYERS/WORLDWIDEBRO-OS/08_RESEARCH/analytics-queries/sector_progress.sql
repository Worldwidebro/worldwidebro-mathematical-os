-- Query 2: Sector Progress Summary
-- Aggregates venture completion metrics by sector
-- Used by: Obsidian (sector ranking chart) + Grafana (sector KPIs)

SELECT
  v.sector,
  COUNT(DISTINCT vsr.venture_id) as total_ventures,
  COUNT(DISTINCT CASE WHEN vsr.status = 'completed' THEN vsr.venture_id END) as ventures_completed,
  COUNT(DISTINCT CASE WHEN vsr.status = 'in_progress' THEN vsr.venture_id END) as ventures_in_progress,
  COUNT(DISTINCT CASE WHEN vsr.status = 'blocked' THEN vsr.venture_id END) as ventures_blocked,
  ROUND(
    AVG(CASE WHEN vsr.status = 'completed' THEN 1 ELSE 0 END) * 100, 2
  ) as avg_completion_percentage,
  ROUND(AVG(vsr.skill_phase), 1) as avg_current_phase,
  COUNT(CASE WHEN vsr.status = 'blocked' THEN 1 END) as total_blocked_skills,
  STRING_AGG(DISTINCT vsr.skill_name, ', ')
    FILTER (WHERE vsr.status = 'blocked' LIMIT 5) as top_blockers
FROM venture_skill_roadmap vsr
LEFT JOIN ventures v ON vsr.venture_id = v.venture_id
WHERE v.sector IS NOT NULL
GROUP BY v.sector
ORDER BY avg_completion_percentage DESC;
