import { Neo4jDriver } from 'neo4j-driver';

export async function seedGraph(driver: Neo4jDriver): Promise<void> {
  const session = driver.session();

  try {
    // Create organization
    await session.run(
      `MERGE (o:Organization {id: 'worldwidebro'})
       SET o.name = 'Worldwidebro Holdings', o.type = 'HOLDING'`
    );

    // Create OPCOs
    const opcos = ['CON', 'STA', 'FIN', 'RE', 'EDU', 'LOG'];
    for (const opco of opcos) {
      await session.run(
        `MERGE (o:Organization {id: $id})
         SET o.name = $name, o.type = 'OPCO'
         WITH o
         MATCH (parent:Organization {id: 'worldwidebro'})
         MERGE (o)-[:BELONGS_TO]->(parent)`,
        { id: opco + '-OS', name: opco + ' Operating System' }
      );
    }

    // Create capabilities
    const capabilities = [
      'venture-analysis', 'financial-modeling', 'market-research',
      'team-building', 'process-optimization', 'risk-assessment',
      'sales', 'operations', 'technology', 'strategy'
    ];
    for (const cap of capabilities) {
      await session.run(`MERGE (c:Capability {name: $name})`, { name: cap });
    }

    // Create tools
    const tools = ['fetch_venture', 'analyze_capability', 'record_metric', 'get_founders', 'calculate_tier'];
    for (const tool of tools) {
      await session.run(`MERGE (t:Tool {name: $name})`, { name: tool });
    }

    console.log('✅ Graph seeded: 1 org, 6 OPCOs, 10 capabilities, 5 tools');
  } catch (err) {
    console.error('Seeding error:', err);
  } finally {
    await session.close();
  }
}
