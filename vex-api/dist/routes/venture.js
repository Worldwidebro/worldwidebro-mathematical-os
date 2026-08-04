import { Router } from 'express';
export const ventureRouter = Router();
ventureRouter.get('/', async (req, res) => {
    try {
        const neo4j = req.app.locals.neo4j;
        const session = neo4j.session();
        const result = await session.run(`MATCH (v:Venture) RETURN v LIMIT 100`);
        await session.close();
        res.json({ ventures: result.records.map(r => r.get('v').properties) });
    }
    catch (err) {
        res.status(500).json({ error: 'Failed to fetch ventures' });
    }
});
ventureRouter.get('/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const neo4j = req.app.locals.neo4j;
        const session = neo4j.session();
        const result = await session.run(`MATCH (v:Venture {id: $id}) RETURN v`, { id });
        await session.close();
        res.json(result.records[0]?.get('v').properties || null);
    }
    catch (err) {
        res.status(500).json({ error: 'Failed to fetch venture' });
    }
});
ventureRouter.post('/', async (req, res) => {
    try {
        const { id, name, description, founder_id, sector, stage } = req.body;
        const neo4j = req.app.locals.neo4j;
        const session = neo4j.session();
        // Create venture node
        await session.run(`MERGE (v:Venture {id: $id})
       SET v.name = $name, v.description = $description, v.sector = $sector, v.stage = $stage, v.created_at = datetime()
       RETURN v`, { id, name, description, sector, stage });
        // Auto-create founder if provided
        if (founder_id) {
            await session.run(`MERGE (f:Founder {id: $founder_id})
         SET f.updated_at = datetime()
         WITH f
         MATCH (v:Venture {id: $venture_id})
         MERGE (f)-[:FOUNDED]->(v)`, { founder_id, venture_id: id });
        }
        await session.close();
        res.json({ success: true, venture_id: id });
    }
    catch (err) {
        console.error('Venture creation error:', err);
        res.status(500).json({ error: 'Failed to create venture' });
    }
});
//# sourceMappingURL=venture.js.map