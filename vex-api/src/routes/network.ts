import { Router, Request, Response } from 'express';

export const networkRouter = Router();

networkRouter.get('/opportunities', async (req: Request, res: Response) => {
  try {
    const supabase = req.app.locals.supabase;
    const { data, error } = await supabase
      .from('opportunities')
      .select('*')
      .eq('status', 'open')
      .order('created_at', { ascending: false });
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch opportunities' });
  }
});

networkRouter.post('/opportunities/:id/accept', async (req: Request, res: Response) => {
  try {
    const { id } = req.params;
    const supabase = req.app.locals.supabase;
    const { data, error } = await supabase
      .from('opportunities')
      .update({ status: 'accepted', accepted_at: new Date() })
      .eq('id', id);
    if (error) throw error;
    res.json({ ok: true });
  } catch (err) {
    res.status(500).json({ error: 'Failed to accept opportunity' });
  }
});

networkRouter.get('/delegation', async (req: Request, res: Response) => {
  try {
    const supabase = req.app.locals.supabase;
    const { data, error } = await supabase
      .from('delegations')
      .select('*')
      .order('created_at', { ascending: false });
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch delegations' });
  }
});

networkRouter.get('/health', async (req: Request, res: Response) => {
  try {
    const neo4j = req.app.locals.neo4j;
    const session = neo4j.session();
    const result = await session.run(`
      MATCH (d:Delegation)
      RETURN COUNT(d) as total
    `);
    await session.close();
    res.json({ health_score: 85, total_delegations: result.records[0]?.get('total') || 0 });
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch health' });
  }
});
