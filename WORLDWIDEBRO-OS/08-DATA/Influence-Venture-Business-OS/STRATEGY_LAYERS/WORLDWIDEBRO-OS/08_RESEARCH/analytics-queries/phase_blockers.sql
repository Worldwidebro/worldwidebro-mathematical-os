-- Query 4: Phase & Skill Blockers
-- Shows which skills are blocking progress and what phase they're in
-- Used by: Obsidian (top blockers widget) + Grafana (blocker dashboard)

WITH blocker_summary AS (
  SELECT
    vsr.skill_name,
    st.skill_phase,
    st.category,
    COUNT(*) as total_blocked_instances,
    COUNT(DISTINCT vsr.venture_id) as distinct_ventures_blocked,
    STRING_AGG(DISTINCT vsr.venture_id, ', ') as venture_ids_blocked,
    ROUND(AVG(EXTRACT(DAY FROM (CURRENT_DATE - vsr.planned_start_date))), 1) as avg_days_blocked,
    MAX(vsr.planned_start_date) as first_blocked_date
  FROM venture_skill_roadmap vsr
  LEFT JOIN skill_taxonomy st ON vsr.skill_name = st.skill_name
  WHERE vsr.status = 'blocked'
  GROUP BY vsr.skill_name, st.skill_phase, st.category
),
phase_blockers AS (
  SELECT
    vsr.skill_phase,
    COUNT(*) as blocked_skills_in_phase,
    COUNT(DISTINCT vsr.venture_id) as distinct_ventures_affected,
    STRING_AGG(DISTINCT vsr.skill_name, ', ') as blocking_skill_names
  FROM venture_skill_roadmap vsr
  WHERE vsr.status = 'blocked'
  GROUP BY vsr.skill_phase
)
SELECT
  bs.skill_name,
  bs.skill_phase,
  bs.category,
  bs.total_blocked_instances,
  bs.distinct_ventures_blocked,
  bs.avg_days_blocked,
  bs.first_blocked_date,
  pb.blocked_skills_in_phase,
  pb.distinct_ventures_affected as ventures_affected_by_phase,
  CASE
    WHEN bs.total_blocked_instances > 10 THEN 'CRITICAL'
    WHEN bs.total_blocked_instances > 5 THEN 'HIGH'
    WHEN bs.total_blocked_instances > 2 THEN 'MEDIUM'
    ELSE 'LOW'
  END as severity
FROM blocker_summary bs
LEFT JOIN phase_blockers pb ON bs.skill_phase = pb.skill_phase
ORDER BY bs.total_blocked_instances DESC, bs.skill_phase ASC;
