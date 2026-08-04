import { Router, Request, Response } from 'express';

export const capabilityRouter = Router();

/**
 * POST /capabilities/rank
 * Body: { taskDescription }
 * Returns: sorted list of { agent, capability, score, source }
 */
capabilityRouter.post('/rank', async (req: Request, res: Response) => {
  try {
    const { taskDescription } = req.body;
    if (!taskDescription) {
      return res.status(400).json({ error: 'Missing required field: taskDescription' });
    }

    const capabilityEngine = req.app.locals.capabilityEngine;
    const ranked = await capabilityEngine.rankCapabilities(taskDescription);
    res.json(ranked);
  } catch (err) {
    console.error('Capability ranking error:', err);
    res.status(500).json({ error: 'Failed to rank capabilities' });
  }
});
