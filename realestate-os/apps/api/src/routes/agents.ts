import { Router, Request, Response } from 'express';
import { getAllAgents, getAgentByName, invokeAgent } from '../registry/agents.js';

const router = Router();

/**
 * GET /api/agents
 * Returns JSON list of all 20 registered AI Agents.
 */
router.get('/', (req: Request, res: Response) => {
  try {
    const agents = getAllAgents();
    res.json({
      success: true,
      count: agents.length,
      agents,
    });
  } catch (err: any) {
    res.status(500).json({ success: false, error: String(err?.message || err) });
  }
});

/**
 * GET /api/agents/:agentName
 * Returns details for a specific AI Agent by name.
 */
router.get('/:agentName', (req: Request, res: Response) => {
  try {
    const { agentName } = req.params;
    const agent = getAgentByName(agentName);

    if (!agent) {
      return res.status(404).json({
        success: false,
        error: `Agent '${agentName}' not found in registry.`,
      });
    }

    res.json({
      success: true,
      agent,
    });
  } catch (err: any) {
    res.status(500).json({ success: false, error: String(err?.message || err) });
  }
});

/**
 * POST /api/agents/:agentName/invoke
 * Invokes an agent with a request payload, returning execution logs and outcome output.
 */
router.post('/:agentName/invoke', async (req: Request, res: Response) => {
  try {
    const { agentName } = req.params;
    const payload = req.body || {};

    const agent = getAgentByName(agentName);
    if (!agent) {
      return res.status(404).json({
        success: false,
        agentName,
        timestamp: new Date().toISOString(),
        executionTimeMs: 0,
        logs: [
          {
            timestamp: new Date().toISOString(),
            level: 'error',
            message: `Agent '${agentName}' not found in registry.`,
          },
        ],
        output: { error: `Agent '${agentName}' not found.` },
        error: `Agent '${agentName}' not found.`,
      });
    }

    const result = await invokeAgent(agentName, payload);
    res.status(200).json(result);
  } catch (err: any) {
    res.status(500).json({
      success: false,
      agentName: req.params.agentName,
      timestamp: new Date().toISOString(),
      executionTimeMs: 0,
      logs: [
        {
          timestamp: new Date().toISOString(),
          level: 'error',
          message: `Execution failed: ${String(err?.message || err)}`,
        },
      ],
      output: { error: String(err?.message || err) },
      error: String(err?.message || err),
    });
  }
});

export default router;
