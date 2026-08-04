// vex-api/src/routes/api/matching.ts
// Track C: Partner Matching API

import { Router } from 'express';
import { MatchingEngine, seedCapabilityGraph } from '../../matching/engine';
import { neoDriver } from '../../db';

const router = Router();
const engine = new MatchingEngine(neoDriver);

/**
 * POST /api/matching/find-partners
 * Find best partners for opportunity
 */
router.post('/find-partners', async (req, res) => {
  try {
    const { opportunity_id, industry, value, products_needed, region } = req.body;

    if (!opportunity_id || !products_needed?.length || !region) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const partners = await engine.findBestPartners({
      id: opportunity_id,
      industry,
      value,
      products_needed,
      region,
    });

    res.json({
      opportunity_id,
      matches: partners,
      count: partners.length,
    });
  } catch (error) {
    console.error('Error finding partners:', error);
    res.status(500).json({ error: 'Failed to find partners' });
  }
});

/**
 * GET /api/matching/capabilities
 * List all capabilities
 */
router.get('/capabilities', async (req, res) => {
  try {
    const session = neoDriver.session();
    const result = await session.run(`
      MATCH (c:Capability)
      RETURN c.name as name, c.category as category
      ORDER BY c.category, c.name
    `);
    await session.close();

    const capabilities = result.records.map(r => ({
      name: r.get('name'),
      category: r.get('category'),
    }));

    res.json({ capabilities });
  } catch (error) {
    console.error('Error fetching capabilities:', error);
    res.status(500).json({ error: 'Failed to fetch capabilities' });
  }
});

/**
 * POST /api/matching/seed (admin only)
 */
router.post('/seed', async (req, res) => {
  try {
    const adminKey = req.headers['x-admin-key'];
    if (adminKey !== process.env.ADMIN_KEY) {
      return res.status(403).json({ error: 'Unauthorized' });
    }

    await seedCapabilityGraph(neoDriver);
    res.json({ message: 'Graph seeded' });
  } catch (error) {
    console.error('Error seeding:', error);
    res.status(500).json({ error: 'Failed to seed graph' });
  }
});

export default router;
