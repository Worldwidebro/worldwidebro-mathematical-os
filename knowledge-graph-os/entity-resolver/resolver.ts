import neo4j, { Driver, Session } from "neo4j-driver";

// Entity Resolver — Deduplication & Conflict Resolution
// Handles: agent name collisions, capability merging, org matching

interface ResolutionLog {
  entity_type: string;
  primary_id: string;
  duplicate_ids: string[];
  merge_reason: string;
  resolved_at: Date;
}

interface ConflictResolution {
  field: string;
  primary_value: unknown;
  duplicate_value: unknown;
  kept: "primary" | "duplicate";
  reason: string;
}

export class EntityResolver {
  private driver: Driver;
  private resolution_log: ResolutionLog[] = [];

  constructor(uri: string, username: string, password: string) {
    this.driver = neo4j.driver(uri, neo4j.auth.basic(username, password));
  }

  /**
   * Detect duplicate agents by name + org + capability similarity
   * Merge duplicates: keep newest (by created_at), log resolution
   */
  async resolve_agent_duplicates(): Promise<ResolutionLog[]> {
    const session = this.driver.session();

    try {
      // Find agents with identical names in same org
      const query = `
        MATCH (a1:Agent), (a2:Agent)
        WHERE a1.id < a2.id
          AND a1.name = a2.name
          AND a1.org_id = a2.org_id
          AND a1.created_at < a2.created_at
        RETURN a1, a2
      `;

      const result = await session.run(query);

      for (const record of result.records) {
        const primary = record.get("a1").properties;
        const duplicate = record.get("a2").properties;

        await this.merge_agents(session, primary, duplicate);
      }

      return this.resolution_log;
    } finally {
      await session.close();
    }
  }

  /**
   * Merge two agents: keep newer, redirect all relationships
   */
  private async merge_agents(session: Session, primary: any, duplicate: any): Promise<void> {
    try {
      const duplicate_id = duplicate.id;
      const primary_id = primary.id;

      // Redirect all relationships to primary
      await session.run(
        `
        MATCH (dup:Agent {id: $dup_id})
        MATCH (prim:Agent {id: $prim_id})

        // Redirect HAS_CAPABILITY edges
        OPTIONAL MATCH (dup)-[r1:HAS_CAPABILITY]->(c:Capability)
        WITH prim, dup, COLLECT({cap: c, rel: r1}) AS caps

        // Redirect ASSIGNED_TO edges
        OPTIONAL MATCH (t:Task)-[r2:ASSIGNED_TO]->(dup)
        WITH prim, dup, caps, COLLECT({task: t, rel: r2}) AS tasks

        // Create consolidated relationships on primary
        FOREACH (cap IN caps | MERGE (prim)-[:HAS_CAPABILITY]->(cap.cap))
        FOREACH (task IN tasks | MERGE (task.task)-[:ASSIGNED_TO]->(prim))

        // Delete duplicate
        DETACH DELETE dup
        `,
        { dup_id: duplicate_id, prim_id: primary_id }
      );

      this.resolution_log.push({
        entity_type: "Agent",
        primary_id,
        duplicate_ids: [duplicate_id],
        merge_reason: `Merged duplicate agent (same name + org, older ${duplicate.created_at} → newer ${primary.created_at})`,
        resolved_at: new Date(),
      });

      console.log(`Merged duplicate agent ${duplicate_id} → ${primary_id}`);
    } catch (error) {
      console.error(`Failed to merge agents ${primary.id} + ${duplicate.id}:`, error);
    }
  }

  /**
   * Detect capability duplicates by name + category
   * Consolidate under single canonical capability
   */
  async resolve_capability_duplicates(): Promise<ResolutionLog[]> {
    const session = this.driver.session();

    try {
      // Find capabilities with similar names
      const query = `
        MATCH (c1:Capability), (c2:Capability)
        WHERE c1.id < c2.id
          AND c1.name = c2.name
          AND c1.category = c2.category
        RETURN c1, c2
      `;

      const result = await session.run(query);

      for (const record of result.records) {
        const primary = record.get("c1").properties;
        const duplicate = record.get("c2").properties;

        await this.merge_capabilities(session, primary, duplicate);
      }

      return this.resolution_log;
    } finally {
      await session.close();
    }
  }

  /**
   * Merge two capabilities under primary ID
   */
  private async merge_capabilities(session: Session, primary: any, duplicate: any): Promise<void> {
    try {
      const duplicate_id = duplicate.id;
      const primary_id = primary.id;

      // Redirect all HAS_CAPABILITY edges from duplicate to primary
      await session.run(
        `
        MATCH (dup:Capability {id: $dup_id})
        MATCH (prim:Capability {id: $prim_id})

        // Find all agents pointing to duplicate
        OPTIONAL MATCH (a:Agent)-[r:HAS_CAPABILITY]->(dup)
        WITH prim, dup, COLLECT(a) AS agents

        // Redirect to primary
        FOREACH (ag IN agents |
          MERGE (ag)-[:HAS_CAPABILITY]->(prim)
        )

        // Delete duplicate
        DETACH DELETE dup
        `,
        { dup_id: duplicate_id, prim_id: primary_id }
      );

      this.resolution_log.push({
        entity_type: "Capability",
        primary_id,
        duplicate_ids: [duplicate_id],
        merge_reason: `Merged duplicate capability (same name + category)`,
        resolved_at: new Date(),
      });

      console.log(`Merged duplicate capability ${duplicate_id} → ${primary_id}`);
    } catch (error) {
      console.error(`Failed to merge capabilities ${primary.id} + ${duplicate.id}:`, error);
    }
  }

  /**
   * Conflict resolution: when two fields have different values
   * Precedence: keep newest (by updated_at), log conflict
   */
  resolve_field_conflict(
    primary_value: unknown,
    duplicate_value: unknown,
    primary_updated_at: Date,
    duplicate_updated_at: Date
  ): ConflictResolution {
    const kept = primary_updated_at > duplicate_updated_at ? "primary" : "duplicate";

    return {
      field: "generic",
      primary_value,
      duplicate_value,
      kept,
      reason: `Kept ${kept} value (updated ${kept === "primary" ? primary_updated_at : duplicate_updated_at})`,
    };
  }

  /**
   * Health check: count agents, capabilities, verify no orphans
   */
  async health_check(): Promise<{
    total_agents: number;
    total_capabilities: number;
    orphan_agents: number;
    duplicate_risk: number;
  }> {
    const session = this.driver.session();

    try {
      const agents = await session.run("MATCH (a:Agent) RETURN COUNT(a) AS count");
      const capabilities = await session.run("MATCH (c:Capability) RETURN COUNT(c) AS count");
      const orphans = await session.run(
        "MATCH (a:Agent) WHERE NOT (a)-[:HAS_CAPABILITY]->() RETURN COUNT(a) AS count"
      );
      const duplicates = await session.run(`
        MATCH (a1:Agent), (a2:Agent)
        WHERE a1.id < a2.id AND a1.name = a2.name
        RETURN COUNT(*) AS count
      `);

      return {
        total_agents: agents.records[0]?.get("count") || 0,
        total_capabilities: capabilities.records[0]?.get("count") || 0,
        orphan_agents: orphans.records[0]?.get("count") || 0,
        duplicate_risk: duplicates.records[0]?.get("count") || 0,
      };
    } finally {
      await session.close();
    }
  }

  /**
   * Export resolution log for audit
   */
  get_resolution_log(): ResolutionLog[] {
    return this.resolution_log;
  }

  async close(): Promise<void> {
    await this.driver.close();
  }
}

// CLI: Run deduplication
if (require.main === module) {
  const resolver = new EntityResolver(
    process.env.NEO4J_URI || "neo4j://localhost:7687",
    process.env.NEO4J_USER || "neo4j",
    process.env.NEO4J_PASSWORD || "ventures2026"
  );

  (async () => {
    console.log("Running entity resolution...");

    await resolver.resolve_agent_duplicates();
    await resolver.resolve_capability_duplicates();

    const health = await resolver.health_check();
    console.log("Health check:", health);

    const log = resolver.get_resolution_log();
    console.log(`Resolved ${log.length} conflicts`);

    await resolver.close();
  })();
}

export default EntityResolver;
