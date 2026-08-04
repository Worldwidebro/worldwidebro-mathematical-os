import { Neo4jDriver } from 'neo4j-driver';
/**
 * Quarterly Recalibration Job
 * Fetches all founders, records assessments, updates tiers, aggregates metrics
 */
export declare class RecalibrationJob {
    private neo4j;
    constructor(neo4j: Neo4jDriver);
    run(): Promise<void>;
    private getCurrentQuarter;
}
/**
 * To schedule: In index.ts, add:
 * import schedule from 'node-schedule';
 * const recalibJob = new RecalibrationJob(neo4jDriver);
 * schedule.scheduleJob('0 0 1 1,4,7,10 *', () => recalibJob.run());
 */
//# sourceMappingURL=recalibration.d.ts.map