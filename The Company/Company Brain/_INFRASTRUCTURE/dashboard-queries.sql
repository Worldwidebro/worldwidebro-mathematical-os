-- RESOURCE LINKING DASHBOARD QUERIES

-- Query 1: Which ventures share most code?
SELECT 
  v1.id as venture_1,
  v2.id as venture_2,
  COUNT(DISTINCT shared_repos.repo_id) as shared_repositories,
  STRING_AGG(DISTINCT shared_repos.repo_id, ', ') as repo_ids
FROM (
  SELECT venture_id, repo_id
  FROM venture_repositories
) v1_repos
JOIN (
  SELECT venture_id, repo_id
  FROM venture_repositories
) v2_repos ON v1_repos.repo_id = v2_repos.repo_id
JOIN ventures v1 ON v1_repos.venture_id = v1.id
JOIN ventures v2 ON v2_repos.venture_id = v2.id
WHERE v1.id < v2.id
GROUP BY v1.id, v2.id
ORDER BY shared_repositories DESC
LIMIT 20;

-- Query 2: What's the impact of changing a repository?
SELECT 
  r.id as repository_id,
  r.name,
  COUNT(DISTINCT v.id) as affected_ventures,
  COUNT(DISTINCT c.id) as affected_capabilities,
  COUNT(DISTINCT a.id) as affected_agents,
  STRING_AGG(DISTINCT v.id, ', ') as venture_ids
FROM repositories r
LEFT JOIN repository_capabilities rc ON r.id = rc.repository_id
LEFT JOIN capabilities c ON rc.capability_id = c.id
LEFT JOIN venture_capabilities vc ON c.id = vc.capability_id
LEFT JOIN ventures v ON vc.venture_id = v.id
LEFT JOIN agent_capabilities ac ON c.id = ac.capability_id
LEFT JOIN agents a ON ac.agent_id = a.id
GROUP BY r.id, r.name
ORDER BY affected_ventures DESC;

-- Query 3: Which capabilities are most used?
SELECT 
  c.id,
  c.name,
  COUNT(DISTINCT v.id) as venture_count,
  COUNT(DISTINCT a.id) as agent_count,
  COUNT(DISTINCT r.id) as repository_count,
  COUNT(DISTINCT t.id) as tool_count
FROM capabilities c
LEFT JOIN venture_capabilities vc ON c.id = vc.capability_id
LEFT JOIN ventures v ON vc.venture_id = v.id
LEFT JOIN agent_capabilities ac ON c.id = ac.capability_id
LEFT JOIN agents a ON ac.agent_id = a.id
LEFT JOIN repository_capabilities rc ON c.id = rc.capability_id
LEFT JOIN repositories r ON rc.repository_id = r.id
LEFT JOIN tool_capabilities tc ON c.id = tc.capability_id
LEFT JOIN tools t ON tc.tool_id = t.id
GROUP BY c.id, c.name
ORDER BY venture_count DESC;

-- Query 4: Agent toolbox - what can each agent do?
SELECT 
  a.id as agent_id,
  a.name,
  COUNT(DISTINCT c.id) as capability_count,
  STRING_AGG(DISTINCT c.id, ', ') as capabilities,
  COUNT(DISTINCT t.id) as tool_count,
  STRING_AGG(DISTINCT t.id, ', ') as tools
FROM agents a
LEFT JOIN agent_capabilities ac ON a.id = ac.agent_id
LEFT JOIN capabilities c ON ac.capability_id = c.id
LEFT JOIN agent_tools at ON a.id = at.agent_id
LEFT JOIN tools t ON at.tool_id = t.id
GROUP BY a.id, a.name
ORDER BY capability_count DESC;

-- Query 5: Venture completeness - which ventures have all their dependencies?
SELECT 
  v.id,
  v.name,
  v.status,
  COUNT(DISTINCT r.id) as repository_count,
  COUNT(DISTINCT c.id) as capability_count,
  COUNT(DISTINCT a.id) as agent_count,
  CASE 
    WHEN COUNT(DISTINCT r.id) > 0 AND COUNT(DISTINCT c.id) > 0 THEN 'complete'
    ELSE 'incomplete'
  END as completeness
FROM ventures v
LEFT JOIN venture_repositories vr ON v.id = vr.venture_id
LEFT JOIN repositories r ON vr.repository_id = r.id
LEFT JOIN venture_capabilities vc ON v.id = vc.venture_id
LEFT JOIN capabilities c ON vc.capability_id = c.id
LEFT JOIN venture_agents va ON v.id = va.venture_id
LEFT JOIN agents a ON va.agent_id = a.id
GROUP BY v.id, v.name, v.status
ORDER BY completeness, repository_count DESC;

-- Query 6: Learning outcomes by course
SELECT 
  co.course_id,
  c.title,
  c.venture_id,
  co.enrollment_count,
  ROUND(co.completion_rate::numeric, 2) as completion_rate,
  ROUND(co.average_quiz_score::numeric, 2) as average_quiz_score,
  ROUND(co.average_time_spent_hours::numeric, 2) as average_time_spent_hours
FROM course_outcomes co
JOIN courses c ON co.course_id = c.id
ORDER BY co.enrollment_count DESC;

-- Query 7: Resource overlap matrix (which tools do multiple agents share?)
SELECT 
  t.id as tool_id,
  t.name,
  COUNT(DISTINCT a.id) as agent_count,
  STRING_AGG(DISTINCT a.id, ', ') as agents,
  COUNT(DISTINCT c.id) as capability_count,
  COUNT(DISTINCT r.id) as repository_count
FROM tools t
LEFT JOIN agent_tools at ON t.id = at.tool_id
LEFT JOIN agents a ON at.agent_id = a.id
LEFT JOIN tool_capabilities tc ON t.id = tc.tool_id
LEFT JOIN capabilities c ON tc.capability_id = c.id
LEFT JOIN repository_tools rt ON t.id = rt.tool_id
LEFT JOIN repositories r ON rt.repository_id = r.id
GROUP BY t.id, t.name
ORDER BY agent_count DESC;
