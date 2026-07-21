import neo4j from 'neo4j-driver';

const driver = neo4j.driver(
  process.env.NEO4J_URL || 'bolt://localhost:7687',
  neo4j.auth.basic(
    process.env.NEO4J_USER || 'neo4j',
    process.env.NEO4J_PASSWORD || 'ventures2026'
  )
);

export async function queryAgents() {
  const session = driver.session();
  try {
    const result = await session.run(
      `MATCH (a:Agent) RETURN a.id as id, a.name as name, a.role as role, a.status as status, a.confidence as confidence LIMIT 100`
    );
    return result.records.map(r => ({
      id: r.get('id'),
      name: r.get('name'),
      role: r.get('role'),
      status: r.get('status') || 'idle',
      confidence: parseFloat(r.get('confidence')) || 0.5,
    }));
  } catch (err) {
    console.error('Neo4j agents query failed:', err);
    return [];
  } finally {
    await session.close();
  }
}
