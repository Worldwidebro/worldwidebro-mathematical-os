import { Router } from 'express';
import { execSync } from 'child_process';
import { v4 as uuidv4 } from 'uuid';
export const capitalRoutingRouter = Router();
async function calculateTierAllocation(supabase, opco_name, allocation_amount) {
    // Query opco_12mo_rolling_roi view for OPCO performance
    const { data: roiData, error: roiError } = await supabase
        .from('opco_12mo_rolling_roi')
        .select('*')
        .eq('opco_name', opco_name)
        .single();
    if (roiError) {
        console.warn(`No ROI data found for ${opco_name}, using conservative defaults`);
    }
    const realized_roi = (roiData?.avg_actual_roi_12mo || 0) / 100;
    const deployment_count = roiData?.deployment_count_12mo || 0;
    const total_deployed = roiData?.total_deployed_12mo || 0;
    // Query deployment summary for velocity
    const { data: deploymentData, error: deployError } = await supabase
        .from('opco_monthly_deployment_summary')
        .select('*')
        .eq('opco_name', opco_name)
        .order('month', { ascending: false })
        .limit(1)
        .single();
    if (deployError) {
        console.warn(`No deployment data found for ${opco_name}`);
    }
    const target_deployments = total_deployed > 0 ? deployment_count * (allocation_amount / total_deployed) : 1;
    const actual_deployments = deploymentData?.deployment_count || 0;
    const velocity_factor = target_deployments > 0 ? actual_deployments / target_deployments : 0.75;
    // Determine tier and apply formula
    let tier = 'T3'; // Default
    let base_share = allocation_amount;
    let calculated_amount = allocation_amount;
    // Tier classification based on deployment rate and ROI
    if (realized_roi >= 0.15 && velocity_factor >= 0.9) {
        // Tier 1: Mature (27% of pool)
        tier = 'T1';
        const formula_result = (realized_roi / 0.15) * velocity_factor;
        calculated_amount = base_share * Math.max(0.75, Math.min(1.5, formula_result));
    }
    else if (realized_roi >= 0.1 && velocity_factor >= 0.7) {
        // Tier 2: Growth (21% of pool)
        tier = 'T2';
        const velocity_capped = Math.min(velocity_factor, 1.2);
        const formula_result = (realized_roi / 0.1) * velocity_capped;
        calculated_amount = base_share * Math.max(0.6, Math.min(1.5, formula_result));
    }
    else if (velocity_factor >= 0.5) {
        // Tier 3: Early-stage (18% of pool)
        tier = 'T3';
        const prior_roi = (roiData?.avg_actual_roi_12mo || 0) * 0.85; // Rough 6mo proxy
        const growth_rate = prior_roi > 0 ? (realized_roi - prior_roi) / prior_roi : 0;
        const velocity_capped = Math.min(velocity_factor, 1.0);
        const formula_result = (1 + growth_rate) * velocity_capped;
        calculated_amount = base_share * Math.max(0.4, Math.min(2.0, formula_result));
    }
    return { tier, calculated_amount, velocity_factor };
}
/**
 * POST /api/capital-allocation/allocate
 * Allocate capital to an OPCO based on tier-based formulas
 */
capitalRoutingRouter.post('/allocate', async (req, res) => {
    try {
        const { opco_name, allocation_amount, week_start_date } = req.body;
        // Validation
        if (!opco_name || !allocation_amount || !week_start_date) {
            return res.status(400).json({
                error: 'Missing required fields: opco_name, allocation_amount, week_start_date',
            });
        }
        if (allocation_amount <= 0) {
            return res.status(400).json({ error: 'allocation_amount must be positive' });
        }
        const supabase = req.app.locals.supabase;
        // Calculate tier-based allocation
        const { tier, calculated_amount, velocity_factor } = await calculateTierAllocation(supabase, opco_name, allocation_amount);
        // Determine approval status and SLA based on amount
        let approval_status = 'auto';
        let approval_sla = 'immediate';
        let confidence = 85; // Default confidence
        if (calculated_amount < 50000) {
            approval_status = 'auto';
            approval_sla = '0 (auto-approved)';
        }
        else if (calculated_amount < 100000) {
            approval_status = 'auto';
            approval_sla = '1h (high confidence)';
            confidence = 80;
        }
        else if (calculated_amount < 500000) {
            approval_status = 'pending';
            approval_sla = '2h (OPCO lead)';
            confidence = 72;
        }
        else if (calculated_amount < 1000000) {
            approval_status = 'pending';
            approval_sla = '6h (OPCO lead + CFO)';
            confidence = 68;
        }
        else {
            approval_status = 'pending';
            approval_sla = '24h (Board)';
            confidence = 60;
        }
        // Create capital_decisions record
        const decision_id = uuidv4();
        const reasoning = {
            formula_used: tier,
            calculated_amount,
            velocity_factor,
            confidence,
            week_start_date,
            allocation_timestamp: new Date().toISOString(),
        };
        const { data: decisionData, error: decisionError } = await supabase
            .from('capital_decisions')
            .insert({
            id: decision_id,
            decision_type: 'allocation',
            opco_name,
            amount: calculated_amount,
            decision_maker: 'capital_allocation_service',
            reasoning: JSON.stringify(reasoning),
            approval_status,
            decision_date: new Date().toISOString(),
        })
            .select()
            .single();
        if (decisionError) {
            console.error('Failed to create capital decision:', decisionError);
            return res.status(500).json({ error: 'Failed to store allocation decision' });
        }
        // Create opco_capital_allocations record
        const { error: allocError } = await supabase
            .from('opco_capital_allocations')
            .insert({
            opco_name,
            allocation_date: week_start_date,
            approved_amount: calculated_amount,
            allocated_amount: approval_status === 'auto' ? calculated_amount : null,
            status: approval_status === 'auto' ? 'approved' : 'pending',
            approved_by: approval_status === 'auto' ? 'capital_allocation_service' : null,
            approval_date: approval_status === 'auto' ? new Date() : null,
        });
        if (allocError) {
            console.error('Failed to create OPCO allocation:', allocError);
            return res.status(500).json({ error: 'Failed to store OPCO allocation' });
        }
        // Log for audit trail
        console.log(`[CAPITAL-ALLOCATION] ${opco_name} allocated ${calculated_amount} (${tier}, confidence: ${confidence}%)`);
        const response = {
            decision_id,
            opco_name,
            amount: calculated_amount,
            status: (approval_status === 'auto' ? 'approved' : 'pending'),
            approval_sla,
            confidence,
        };
        res.json(response);
    }
    catch (err) {
        console.error('Capital allocation error:', err);
        res.status(500).json({ error: 'Internal server error during allocation' });
    }
});
/**
 * POST /api/capital-allocation/deploy
 * Deploy allocated capital to ventures via venture_loop.py
 */
capitalRoutingRouter.post('/deploy', async (req, res) => {
    try {
        const { decision_id, venture_ids } = req.body;
        // Validation
        if (!decision_id || !Array.isArray(venture_ids) || venture_ids.length === 0) {
            return res.status(400).json({
                error: 'Missing required fields: decision_id (uuid), venture_ids (non-empty array)',
            });
        }
        const supabase = req.app.locals.supabase;
        // Retrieve capital_decisions record
        const { data: decision, error: decisionError } = await supabase
            .from('capital_decisions')
            .select('*')
            .eq('id', decision_id)
            .single();
        if (decisionError || !decision) {
            return res.status(404).json({ error: `Capital decision ${decision_id} not found` });
        }
        // Verify decision is approved
        if (decision.approval_status !== 'approved' && decision.approval_status !== 'auto') {
            return res.status(400).json({
                error: `Decision ${decision_id} is not approved. Current status: ${decision.approval_status}`,
            });
        }
        const total_allocation = decision.amount;
        const per_venture_amount = total_allocation / venture_ids.length;
        // Fetch 12-month ROI for predicted ROI calculation
        const { data: roiData } = await supabase
            .from('opco_12mo_rolling_roi')
            .select('*')
            .eq('opco_name', decision.opco_name)
            .single();
        const opco_roi = (roiData?.avg_actual_roi_12mo || 12) / 100;
        // Deploy to each venture
        const deployment_ids = [];
        const deployment_date = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
        for (const venture_id of venture_ids) {
            const deployment_record_id = uuidv4();
            // Calculate predicted ROI using CAPITAL-ALLOCATION formula
            // predicted_roi_pct = (OPCO_ROI × 0.4) + (Sector_Benchmark × 0.3) + (Stage_Adj × 0.2) + (Market × 0.1)
            const predicted_roi = opco_roi * 40 + 10 * 30 + 2 * 20 + 1.0 * 10; // Simplified; adjust with real data
            const { error: deployError } = await supabase
                .from('capital_deployment_log')
                .insert({
                id: deployment_record_id,
                opco_name: decision.opco_name,
                venture_id,
                amount_deployed: per_venture_amount,
                deployment_date,
                predicted_roi_pct: Math.round(predicted_roi * 100) / 100,
                formula_used: JSON.parse(decision.reasoning || '{}').formula_used || 'T3',
            });
            if (deployError) {
                console.error(`Failed to deploy to ${venture_id}:`, deployError);
                return res.status(500).json({ error: `Failed to deploy to venture ${venture_id}` });
            }
            deployment_ids.push(deployment_record_id);
            // Log deployment for audit
            console.log(`[CAPITAL-DEPLOY] ${decision.opco_name} → ${venture_id} ($${per_venture_amount.toFixed(2)})`);
        }
        // Trigger venture_loop.py via child process
        try {
            const loop_payload = {
                decision_id,
                opco_name: decision.opco_name,
                ventures: venture_ids,
                total_amount: total_allocation,
                per_venture_amount,
                deployment_ids,
                timestamp: new Date().toISOString(),
            };
            execSync(`python3 /Users/acebless/Documents/venture_loop.py --deploy '${JSON.stringify(loop_payload)}'`, { stdio: 'pipe' });
            console.log(`[VENTURE-LOOP] Triggered for decision ${decision_id}`);
        }
        catch (loopError) {
            console.warn(`venture_loop.py execution warning:`, loopError);
            // Don't fail the deployment if venture_loop fails; it's async
        }
        res.json({
            deployment_id: deployment_ids[0],
            ventures_funded: venture_ids,
            total_deployed: total_allocation,
            per_venture: per_venture_amount,
            status: 'deployed',
            deployment_records: deployment_ids,
            timestamp: new Date().toISOString(),
        });
    }
    catch (err) {
        console.error('Capital deployment error:', err);
        res.status(500).json({ error: 'Internal server error during deployment' });
    }
});
/**
 * GET /api/capital-allocation/status/:decision_id
 * Retrieve status of a capital decision and its deployments
 */
capitalRoutingRouter.get('/status/:decision_id', async (req, res) => {
    try {
        const { decision_id } = req.params;
        if (!decision_id) {
            return res.status(400).json({ error: 'decision_id is required' });
        }
        const supabase = req.app.locals.supabase;
        // Fetch decision
        const { data: decision, error: decisionError } = await supabase
            .from('capital_decisions')
            .select('*')
            .eq('id', decision_id)
            .single();
        if (decisionError || !decision) {
            return res.status(404).json({ error: `Decision ${decision_id} not found` });
        }
        // Fetch associated deployments
        const { data: deployments, error: deployError } = await supabase
            .from('capital_deployment_log')
            .select('*')
            .eq('id', decision_id); // This assumes deployments link back to decision_id (adjust query as needed)
        if (deployError) {
            console.warn('Failed to fetch deployments:', deployError);
        }
        res.json({
            decision_id,
            decision_type: decision.decision_type,
            opco_name: decision.opco_name,
            amount: decision.amount,
            status: decision.approval_status,
            approved_by: decision.approver_id || 'system',
            approval_date: decision.approval_timestamp,
            created_at: decision.created_at,
            reasoning: decision.reasoning ? JSON.parse(decision.reasoning) : null,
            deployments: deployments || [],
        });
    }
    catch (err) {
        console.error('Status lookup error:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});
/**
 * POST /api/capital-allocation/feedback
 * Record feedback on deployment outcomes (actual ROI, success/failure)
 */
capitalRoutingRouter.post('/feedback', async (req, res) => {
    try {
        const { deployment_id, actual_roi_pct, status, error_msg } = req.body;
        // Validation
        if (!deployment_id) {
            return res.status(400).json({ error: 'deployment_id is required' });
        }
        const supabase = req.app.locals.supabase;
        // Fetch deployment record
        const { data: deployment, error: fetchError } = await supabase
            .from('capital_deployment_log')
            .select('*')
            .eq('id', deployment_id)
            .single();
        if (fetchError || !deployment) {
            return res.status(404).json({ error: `Deployment ${deployment_id} not found` });
        }
        // Update deployment with actual ROI
        if (actual_roi_pct !== undefined && actual_roi_pct !== null) {
            const { error: updateError } = await supabase
                .from('capital_deployment_log')
                .update({ actual_roi_pct })
                .eq('id', deployment_id);
            if (updateError) {
                console.error('Failed to update deployment:', updateError);
                return res.status(500).json({ error: 'Failed to update deployment ROI' });
            }
        }
        // Calculate accuracy
        const predicted = deployment.predicted_roi_pct || 0;
        const actual = actual_roi_pct || 0;
        const accuracy_pct = predicted > 0 ? Math.max(0, 100 - Math.abs((actual - predicted) / predicted * 100)) : 0;
        // Call 01_loop_feedback_collector.py
        try {
            const feedback_payload = {
                deployment_id,
                venture_id: deployment.venture_id,
                opco_name: deployment.opco_name,
                amount_deployed: deployment.amount_deployed,
                predicted_roi_pct: predicted,
                actual_roi_pct: actual,
                accuracy_pct,
                status,
                error_msg,
                timestamp: new Date().toISOString(),
            };
            execSync(`python3 /Users/acebless/Documents/01_loop_feedback_collector.py --feedback '${JSON.stringify(feedback_payload)}'`, { stdio: 'pipe' });
            console.log(`[FEEDBACK] Recorded for ${deployment_id}: ${accuracy_pct.toFixed(1)}% accuracy`);
        }
        catch (feedbackError) {
            console.warn(`01_loop_feedback_collector.py execution warning:`, feedbackError);
            // Don't fail if feedback collection fails
        }
        res.json({
            deployment_id,
            venture_id: deployment.venture_id,
            predicted_roi_pct: predicted,
            actual_roi_pct: actual,
            accuracy_pct: Math.round(accuracy_pct * 10) / 10,
            formula_performance: {
                bias: actual - predicted,
                variance: actual > predicted ? 'conservative' : 'optimistic',
                recommendation: accuracy_pct > 85 ? 'maintain formula' : 'review and adjust',
            },
            status: 'feedback_recorded',
            timestamp: new Date().toISOString(),
        });
    }
    catch (err) {
        console.error('Feedback recording error:', err);
        res.status(500).json({ error: 'Internal server error during feedback' });
    }
});
/**
 * GET /api/capital-allocation/stats
 * Retrieve aggregate capital allocation statistics and performance
 */
capitalRoutingRouter.get('/stats', async (req, res) => {
    try {
        const supabase = req.app.locals.supabase;
        // Fetch SLA metrics
        const { data: slaMetrics, error: slaError } = await supabase
            .from('capital_decisions_sla_metrics')
            .select('*')
            .order('date', { ascending: false })
            .limit(30);
        if (slaError) {
            console.warn('Failed to fetch SLA metrics:', slaError);
        }
        // Fetch ROI reconciliation
        const { data: roiReconciliation, error: roiError } = await supabase
            .from('capital_deployment_roi_reconciliation')
            .select('*')
            .order('deployment_date', { ascending: false })
            .limit(100);
        if (roiError) {
            console.warn('Failed to fetch ROI reconciliation:', roiError);
        }
        res.json({
            sla_metrics: slaMetrics || [],
            roi_reconciliation: roiReconciliation || [],
            summary: {
                total_decisions: slaMetrics?.reduce((sum, m) => sum + m.total_decisions, 0) || 0,
                auto_approved: slaMetrics?.reduce((sum, m) => sum + m.auto_approved, 0) || 0,
                total_deployed: roiReconciliation?.reduce((sum, d) => sum + (d.amount_deployed || 0), 0) || 0,
            },
        });
    }
    catch (err) {
        console.error('Stats retrieval error:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});
//# sourceMappingURL=capital-routing.js.map