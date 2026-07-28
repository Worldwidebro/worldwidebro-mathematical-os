import { Router, Request, Response } from 'express';

export const agentRouter = Router();

agentRouter.get('/:id', async (req: Request, res: Response) => {
  try {
    const { id } = req.params;
    const neo4j = req.app.locals.neo4j;
    const session = neo4j.session();
    const result = await session.run(`MATCH (a:Agent {id: $id}) RETURN a`, { id });
    await session.close();
    res.json(result.records[0]?.get('a').properties || null);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch agent' });
  }
});

agentRouter.get('/:id/active-delegations', async (req: Request, res: Response) => {
  try {
    const { id } = req.params;
    const supabase = req.app.locals.supabase;
    const { data, error } = await supabase
      .from('delegations')
      .select('*')
      .eq('agent_id', id)
      .eq('status', 'in_progress');
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch delegations' });
  }
});
