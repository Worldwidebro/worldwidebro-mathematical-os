/**
 * Quarterly Recalibration Job
 * Fetches all founders, records assessments, updates tiers, aggregates metrics
 */
export class RecalibrationJob {
    constructor(neo4j) {
        this.neo4j = neo4j;
    }
    async run() {
        console.log('🔄 Starting quarterly recalibration job...');
        const session = this.neo4j.session();
        try {
            // Fetch all founders
            const founders = await session.run('MATCH (f:Founder) RETURN f.id as id, f.execution_success_rate as exec, f.learning_velocity as learn');
            console.log(`Found ${founders.records.length} founders to assess`);
            let updated = 0;
            for (const record of founders.records) {
                const founder_id = record.get('id');
                const exec_rate = record.get('exec') || 0;
                const learn_velocity = record.get('learn') || 0;
                // Calculate tier
                let tier = '<70% TRAINING';
                if (exec_rate >= 90 && learn_velocity <= 48) {
                    tier = '90%+ AUTONOMOUS';
                }
                else if ((exec_rate >= 70 && exec_rate < 90) || (learn_velocity > 48 && learn_velocity <= 72)) {
                    tier = '70-79% MONITORED';
                }
                // Record assessment in Neo4j
                await session.run(`MATCH (f:Founder {id: $id})
           SET f.governance_tier = $tier, f.last_assessment = datetime(), f.assessment_quarter = $quarter
           RETURN f`, { id: founder_id, tier, quarter: this.getCurrentQuarter() });
                updated++;
            }
            // Aggregate metrics per OPCO
            const opcos = await session.run(`
        MATCH (f:Founder)
        OPTIONAL MATCH (f)-[:BELONGS_TO]->(o:Organization)
        RETURN o.id as opco_id, o.name as opco_name,
               collect(f.governance_tier) as tiers,
               avg(f.execution_success_rate) as avg_exec,
               avg(f.learning_velocity) as avg_learn
      `);
            for (const record of opcos.records) {
                const opco_name = record.get('opco_name');
                const avg_exec = record.get('avg_exec') || 0;
                const avg_learn = record.get('avg_learn') || 0;
                const tiers = record.get('tiers') || [];
                console.log(`${opco_name}: exec=${avg_exec.toFixed(1)}%, learn=${avg_learn.toFixed(1)}h`);
            }
            console.log(`✅ Recalibration complete: ${updated} founders updated`);
        }
        catch (err) {
            console.error('Recalibration job failed:', err);
        }
        finally {
            await session.close();
        }
    }
    getCurrentQuarter() {
        const now = new Date();
        const q = Math.floor(now.getMonth() / 3) + 1;
        return `${now.getFullYear()}-Q${q}`;
    }
}
/**
 * To schedule: In index.ts, add:
 * import schedule from 'node-schedule';
 * const recalibJob = new RecalibrationJob(neo4jDriver);
 * schedule.scheduleJob('0 0 1 1,4,7,10 *', () => recalibJob.run());
 */
//# sourceMappingURL=recalibration.js.map