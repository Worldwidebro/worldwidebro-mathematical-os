import { Router } from 'express';
export const founderRouter = Router();
/**
 * GET /founder/:id/human-os
 * Fetch founder's Human OS tier + dual-outcome metrics
 *
 * Returns:
 * - execution_success_rate (0-100)
 * - learning_velocity (hours to integrate feedback)
 * - governance_tier (90%+ AUTONOMOUS | 70-79% MONITORED | <70% TRAINING)
 * - layer_scores (L1-L10, 1-10 scale)
 * - last_assessment (date)
 */
founderRouter.get('/:id/human-os', async (req, res) => {
    try {
        const { id } = req.params;
        const neo4j = req.app.locals.neo4j;
        const session = neo4j.session();
        // Fetch founder + Human OS metrics
        const result = await session.run(`MATCH (f:Founder {id: $id})
       RETURN f`, { id });
        await session.close();
        const record = result.records[0];
        if (!record) {
            return res.status(404).json({ error: 'Founder not found' });
        }
        const founder = record.get('f').properties;
        const layers = founder.layer_scores_json ? JSON.parse(founder.layer_scores_json) : [];
        // Calculate governance tier from dual outcomes
        const tier_assignment = calculateTier(founder.execution_success_rate || 0, founder.learning_velocity || 0);
        res.json({
            founder_id: id,
            execution_success_rate: founder.execution_success_rate || 0,
            learning_velocity: founder.learning_velocity || 0,
            governance_tier: tier_assignment,
            layer_scores: layers,
            last_assessment: founder.last_assessment || null,
        });
    }
    catch (err) {
        res.status(500).json({ error: 'Failed to fetch Human OS metrics' });
    }
});
/**
 * POST /founder/:id/assessment
 * Record quarterly Human OS assessment
 * Updates: success_rate, learning_velocity, layer_scores, governance_tier
 */
founderRouter.post('/:id/assessment', async (req, res) => {
    try {
        const { id } = req.params;
        const { execution_success_rate, learning_velocity, layer_scores, } = req.body;
        const neo4j = req.app.locals.neo4j;
        const session = neo4j.session();
        // Update founder metrics + layer scores (atomic, stored as JSON)
        const tier = calculateTier(execution_success_rate, learning_velocity);
        await session.run(`MERGE (f:Founder {id: $id})
       SET f.execution_success_rate = $rate,
           f.learning_velocity = $velocity,
           f.governance_tier = $tier,
           f.layer_scores_json = $layerScoresJson,
           f.last_assessment = datetime()
       RETURN f`, {
            id,
            rate: execution_success_rate,
            velocity: learning_velocity,
            tier,
            layerScoresJson: JSON.stringify(layer_scores || []),
        });
        await session.close();
        res.json({ success: true, tier });
    }
    catch (err) {
        console.error('Assessment error:', err);
        res.status(500).json({ error: 'Failed to record assessment' });
    }
});
/**
 * Dual-outcome governance tier assignment
 *
 * 90%+ AUTONOMOUS: execution ≥90% AND learning_velocity ≤48h
 * 70-79% MONITORED: execution 70-79% OR learning_velocity 48-72h
 * <70% TRAINING: execution <70% OR learning_velocity >72h
 */
function calculateTier(successRate, learningVelocityHours) {
    if (successRate >= 90 && learningVelocityHours <= 48) {
        return '90%+ AUTONOMOUS';
    }
    if ((successRate >= 70 && successRate < 90) || (learningVelocityHours > 48 && learningVelocityHours <= 72)) {
        return '70-79% MONITORED';
    }
    return '<70% TRAINING';
}
//# sourceMappingURL=founder.js.map