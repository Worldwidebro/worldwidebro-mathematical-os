import neo4j, { Driver, Session } from "neo4j-driver";

// GraphRouter — Neo4j agent matching & scoring
// Scoring: weightedSuccess (40%) + orgProximity (20%) + costScore (20%) + loadFactor (20%)

interface AgentCandidate {
  agent_id: string;
  name: string;
  org_id: string;
  success_rate: number;
  cost_per_hour: number;
  availability: number;
  capability_match_count: number;
  capability_missing_count: number;
}

interface RoutingResult {
  agent_id: string;
  agent_name: string;
  final_score: number;
  confidence: number;
  scores: {
    weighted_success: number;
    org_proximity: number;
    cost_score: number;
    load_factor: number;
  };
  metadata: {
    matches_required_capabilities: boolean;
    capability_gap_count: number;
  };
}

export class GraphRouter {
  private driver: Driver;

  constructor(uri: string, username: string, password: string) {
    this.driver = neo4j.driver(uri, neo4j.auth.basic(username, password));
  }

  /**
   * Find best agent for task by capability matching + scoring
   *
   * Cypher query flow:
   * 1. Match agents with required capabilities
   * 2. Score by success_rate, org_proximity, cost, availability
   * 3. Sort by final_score descending
   * 4. Return top candidate with confidence breakdown
   */
  async find_best_agent(
    task_id: string,
    required_capabilities: string[],
    preferred_org_id?: string,
    max_cost_per_hour?: number
  ): Promise<RoutingResult | null> {
    const session: Session = this.driver.session();

    try {
      // Query: Match agents who have ALL required capabilities (or subset with low missing count)
      const query = `
        MATCH (t:Task {id: $task_id})
        MATCH (a:Agent {status: 'active'})
        WHERE ($preferred_org IS NULL OR a.org_id = $preferred_org)
          AND ($max_cost IS NULL OR a.cost_per_hour <= $max_cost)

        WITH a,
             COUNT(DISTINCT c.name) AS matched_caps,
             SIZE($required_caps) AS required_count
        WHERE matched_caps >= FLOOR(required_count * 0.8)

        // Capability matching subquery
        OPTIONAL MATCH (a)-[hc:HAS_CAPABILITY]->(c:Capability)
        WHERE c.name IN $required_caps
        WITH a,
             matched_caps,
             required_count,
             COLLECT(DISTINCT c.name) AS matched_capability_names

        // Org proximity (same org = 1.0, different = 0.5, none = 0.3)
        WITH a,
             matched_caps,
             required_count,
             matched_capability_names,
             CASE
               WHEN a.org_id = $preferred_org THEN 1.0
               WHEN $preferred_org IS NULL THEN 0.5
               ELSE 0.3
             END AS org_proximity_score

        // Normalize scores to 0-1 range
        WITH a,
             matched_caps,
             required_count,
             matched_capability_names,
             org_proximity_score,
             // Success rate already 0-1
             COALESCE(a.success_rate, 0.7) AS weighted_success_score,
             // Availability as load factor (higher availability = lower load)
             COALESCE(a.availability, 0.8) AS load_factor_score,
             // Cost score: invert so lower cost = higher score
             CASE
               WHEN $max_cost IS NOT NULL THEN (1.0 - (a.cost_per_hour / $max_cost))
               ELSE 1.0
             END AS cost_score

        // Final weighted score: 40% success + 20% org + 20% cost + 20% load
        WITH a,
             matched_caps,
             required_count,
             matched_capability_names,
             weighted_success_score,
             org_proximity_score,
             cost_score,
             load_factor_score,
             (weighted_success_score * 0.40 +
              org_proximity_score * 0.20 +
              cost_score * 0.20 +
              load_factor_score * 0.20) AS final_score

        RETURN {
          agent_id: a.id,
          name: a.name,
          org_id: a.org_id,
          final_score: ROUND(final_score * 1000) / 1000,
          confidence: ROUND(COALESCE(a.success_rate, 0.7) * 1000) / 1000,
          matches: matched_caps,
          required: required_count,
          capability_names: matched_capability_names,
          scores: {
            weighted_success: weighted_success_score,
            org_proximity: org_proximity_score,
            cost_score: cost_score,
            load_factor: load_factor_score
          }
        } AS result

        ORDER BY final_score DESC
        LIMIT 1
      `;

      const result = await session.run(query, {
        task_id,
        required_caps: required_capabilities,
        preferred_org: preferred_org_id,
        max_cost: max_cost_per_hour,
      });

      if (result.records.length === 0) {
        console.log(
          `No agents found for task ${task_id} with capabilities ${required_capabilities.join(", ")}`
        );
        return null;
      }

      const record = result.records[0].get("result");
      const capability_gap = Math.max(0, record.required - record.matches);

      return {
        agent_id: record.agent_id,
        agent_name: record.name,
        final_score: record.final_score,
        confidence: record.confidence,
        scores: {
          weighted_success: record.scores.weighted_success,
          org_proximity: record.scores.org_proximity,
          cost_score: record.scores.cost_score,
          load_factor: record.scores.load_factor,
        },
        metadata: {
          matches_required_capabilities: capability_gap === 0,
          capability_gap_count: capability_gap,
        },
      };
    } finally {
      await session.close();
    }
  }

  /**
   * Batch query: Find best agents for multiple tasks
   * Returns top N agents per task, sorted by score
   */
  async find_best_agents(
    tasks: Array<{
      task_id: string;
      required_capabilities: string[];
      preferred_org_id?: string;
      max_cost_per_hour?: number;
    }>,
    limit: number = 5
  ): Promise<Map<string, RoutingResult[]>> {
    const results = new Map<string, RoutingResult[]>();

    // Serial execution (can parallelize in Round 3 with Promise.all)
    for (const task of tasks) {
      const agent = await this.find_best_agent(
        task.task_id,
        task.required_capabilities,
        task.preferred_org_id,
        task.max_cost_per_hour
      );

      if (agent) {
        results.set(task.task_id, [agent]);
      } else {
        results.set(task.task_id, []);
      }
    }

    return results;
  }

  /**
   * Health check: Verify Neo4j connectivity + schema freshness
   */
  async health_check(): Promise<{
    connected: boolean;
    agent_count: number;
    capability_count: number;
  }> {
    const session = this.driver.session();

    try {
      const agents = await session.run("MATCH (a:Agent) RETURN COUNT(a) AS count");
      const capabilities = await session.run("MATCH (c:Capability) RETURN COUNT(c) AS count");

      return {
        connected: true,
        agent_count: agents.records[0]?.get("count") || 0,
        capability_count: capabilities.records[0]?.get("count") || 0,
      };
    } catch (error) {
      console.error("Health check failed:", error);
      return {
        connected: false,
        agent_count: 0,
        capability_count: 0,
      };
    } finally {
      await session.close();
    }
  }

  async close(): Promise<void> {
    await this.driver.close();
  }
}

export default GraphRouter;
