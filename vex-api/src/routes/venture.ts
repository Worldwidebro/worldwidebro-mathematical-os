import { Router, Request, Response } from 'express';

export const ventureRouter = Router();

ventureRouter.get('/', async (req: Request, res: Response) => {
  try {
    const neo4j = req.app.locals.neo4j;
    const session = neo4j.session();
    const result = await session.run(`MATCH (v:Venture) RETURN v LIMIT 100`);
    await session.close();
    res.json({ ventures: result.records.map(r => r.get('v').properties) });
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch ventures' });
  }
});

ventureRouter.get('/:id', async (req: Request, res: Response) => {
  try {
    const { id } = req.params;
    const neo4j = req.app.locals.neo4j;
    const session = neo4j.session();
    const result = await session.run(`MATCH (v:Venture {id: $id}) RETURN v`, { id });
    await session.close();
    res.json(result.records[0]?.get('v').properties || null);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch venture' });
  }
});
