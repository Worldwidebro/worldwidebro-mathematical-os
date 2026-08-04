export async function initGraphSchema(driver) {
    const session = driver.session();
    const constraints = [
        'CREATE CONSTRAINT IF NOT EXISTS FOR (o:Organization) REQUIRE o.id IS UNIQUE',
        'CREATE CONSTRAINT IF NOT EXISTS FOR (a:Agent) REQUIRE a.id IS UNIQUE',
        'CREATE CONSTRAINT IF NOT EXISTS FOR (c:Capability) REQUIRE c.name IS UNIQUE',
        'CREATE CONSTRAINT IF NOT EXISTS FOR (t:Tool) REQUIRE t.name IS UNIQUE',
        'CREATE CONSTRAINT IF NOT EXISTS FOR (v:Venture) REQUIRE v.id IS UNIQUE',
        'CREATE CONSTRAINT IF NOT EXISTS FOR (f:Founder) REQUIRE f.id IS UNIQUE',
    ];
    try {
        for (const query of constraints) {
            await session.run(query);
        }
        console.log('✅ Neo4j schema constraints initialized');
    }
    catch (err) {
        console.error('Schema initialization error:', err);
    }
    finally {
        await session.close();
    }
}
//# sourceMappingURL=neo4j-client.js.map