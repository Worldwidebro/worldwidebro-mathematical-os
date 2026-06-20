-- Query 1: Venture Progress Summary
-- Shows completion % by venture with current phase and blocker count
-- Used by: Obsidian (top 20) + Grafana (all ventures)

SELECT
  vsr.venture_id,
  v.venture_name,
  v.sector,
  v.stage as venture_stage,
  COUNT(*) as total_planned_skills,
  COUNT(CASE WHEN vsr.status = 'completed' THEN 1 END) as completed_skills,
  COUNT(CASE WHEN vsr.status = 'in_progress' THEN 1 END) as in_progress_skills,
  COUNT(CASE WHEN vsr.status = 'blocked' THEN 1 END) as blocked_skills,
  ROUND(
    COUNT(CASE WHEN vsr.status = 'completed' THEN 1 END)::FLOAT /
    NULLIF(COUNT(*), 0) * 100, 2
  ) as completion_percentage,
  MAX(vsr.skill_phase) as current_max_phase,
  ROUND(AVG(vsr.skill_phase), 1) as avg_phase,
  STRING_AGG(DISTINCT vsr.skill_name, ', ')
    FILTER (WHERE vsr.status = 'blocked') as blocked_skill_names,
  MAX(vsr.actual_completion_date) as last_completed_date
FROM venture_skill_roadmap vsr
LEFT JOIN ventures v ON vsr.venture_id = v.venture_id
GROUP BY vsr.venture_id, v.venture_name, v.sector, v.stage
ORDER BY completion_percentage DESC, v.venture_name ASC;
