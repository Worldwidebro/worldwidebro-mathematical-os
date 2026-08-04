import { Router, Request, Response } from 'express';

export const memoryRouter = Router();

/**
 * POST /memories/remember
 * Body: { venture_id, agent_id, content, metadata? }
 */
memoryRouter.post('/remember', async (req: Request, res: Response) => {
  try {
    const { venture_id, agent_id, content, metadata } = req.body;
    if (!venture_id || !agent_id || !content) {
      return res.status(400).json({ error: 'Missing required fields: venture_id, agent_id, content' });
    }

    const taskMemoryStore = req.app.locals.taskMemoryStore;
    const taskId = await taskMemoryStore.rememberTask({ venture_id, agent_id, content, metadata });
    res.json({ id: taskId, status: 'remembered' });
  } catch (err) {
    console.error('Remember task error:', err);
    res.status(500).json({ error: 'Failed to remember task' });
  }
});

/**
 * POST /memories/search
 * Body: { query, limit? }
 */
memoryRouter.post('/search', async (req: Request, res: Response) => {
  try {
    const { query, limit } = req.body;
    if (!query) {
      return res.status(400).json({ error: 'Missing required field: query' });
    }

    const taskMemoryStore = req.app.locals.taskMemoryStore;
    const results = await taskMemoryStore.findSimilarTasks({ content: query, limit });
    res.json(results);
  } catch (err) {
    console.error('Search memory error:', err);
    res.status(500).json({ error: 'Failed to search memory' });
  }
});

/**
 * GET /memories/health
 */
memoryRouter.get('/health', async (req: Request, res: Response) => {
  try {
    const taskMemoryStore = req.app.locals.taskMemoryStore;
    const healthy = await taskMemoryStore.health();
    res.json({ qdrant: healthy ? 'ok' : 'down' });
  } catch (err) {
    res.status(500).json({ qdrant: 'down', error: 'Health check failed' });
  }
});
