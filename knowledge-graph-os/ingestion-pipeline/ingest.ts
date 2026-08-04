import { createClient, SupabaseClient } from "@supabase/supabase-js";
import neo4j, { Driver, Session } from "neo4j-driver";
import { Anthropic } from "@anthropic-ai/sdk";

// Supabase → Neo4j/Qdrant ingestion pipeline
// Flow: Supabase → Neo4j nodes + rels → Qdrant embeddings

interface IngestionStats {
  agents_synced: number;
  capabilities_synced: number;
  ventures_synced: number;
  relationships_created: number;
  embeddings_created: number;
  errors: string[];
  duration_ms: number;
}

export class IngestionPipeline {
  private supabase: SupabaseClient;
  private neo4j_driver: Driver;
  private anthropic: Anthropic;
  private stats: IngestionStats = {
    agents_synced: 0,
    capabilities_synced: 0,
    ventures_synced: 0,
    relationships_created: 0,
    embeddings_created: 0,
    errors: [],
    duration_ms: 0,
  };

  constructor(
    supabase_url: string,
    supabase_key: string,
    neo4j_uri: string,
    neo4j_user: string,
    neo4j_password: string,
    anthropic_key: string
  ) {
    this.supabase = createClient(supabase_url, supabase_key);
    this.neo4j_driver = neo4j.driver(neo4j_uri, neo4j.auth.basic(neo4j_user, neo4j_password));
    this.anthropic = new Anthropic({ apiKey: anthropic_key });
  }

  /**
   * Main ingestion orchestration
   * 1. Fetch from Supabase
   * 2. Sync to Neo4j (nodes + relationships)
   * 3. Embed + sync to Qdrant (vectors with payloads)
   * 4. Return stats
   */
  async ingest(): Promise<IngestionStats> {
    const start_time = Date.now();

    try {
      console.log("Starting ingestion pipeline...");

      // Phase 1: Fetch from Supabase
      await this.ingest_agents();
      await this.ingest_capabilities();
      await this.ingest_ventures();

      // Phase 2: Create relationships
      await this.link_agent_capabilities();
      await this.link_venture_agents();

      console.log("Ingestion complete", {
        agents: this.stats.agents_synced,
        capabilities: this.stats.capabilities_synced,
        ventures: this.stats.ventures_synced,
        relationships: this.stats.relationships_created,
      });
    } catch (error) {
      const error_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Pipeline error: ${error_msg}`);
      console.error("Ingestion failed:", error);
    } finally {
      this.stats.duration_ms = Date.now() - start_time;
      await this.neo4j_driver.close();
    }

    return this.stats;
  }

  /**
   * Ingest agents from Supabase → Neo4j
   */
  private async ingest_agents(): Promise<void> {
    try {
      const { data: agents, error } = await this.supabase
        .from("agents")
        .select("*")
        .limit(1000);

      if (error) throw error;
      if (!agents || agents.length === 0) {
        console.log("No agents found in Supabase");
        return;
      }

      const session = this.neo4j_driver.session();

      for (const agent of agents) {
        try {
          // Dedup: check if agent exists
          const existing = await session.run("MATCH (a:Agent {id: $id}) RETURN a LIMIT 1", {
            id: agent.id,
          });

          if (existing.records.length > 0) {
            // Update existing
            await session.run(
              `
              MATCH (a:Agent {id: $id})
              SET a.name = $name,
                  a.org_id = $org_id,
                  a.success_rate = $success_rate,
                  a.availability = $availability,
                  a.cost_per_hour = $cost_per_hour,
                  a.updated_at = datetime()
              `,
              {
                id: agent.id,
                name: agent.name,
                org_id: agent.org_id,
                success_rate: agent.success_rate || 0.7,
                availability: agent.availability || 0.8,
                cost_per_hour: agent.cost_per_hour || 0,
              }
            );
          } else {
            // Create new
            await session.run(
              `
              CREATE (a:Agent {
                id: $id,
                name: $name,
                type: $type,
                org_id: $org_id,
                success_rate: $success_rate,
                availability: $availability,
                cost_per_hour: $cost_per_hour,
                status: 'active',
                created_at: datetime(),
                updated_at: datetime()
              })
              `,
              {
                id: agent.id,
                name: agent.name,
                type: agent.type || "ai",
                org_id: agent.org_id,
                success_rate: agent.success_rate || 0.7,
                availability: agent.availability || 0.8,
                cost_per_hour: agent.cost_per_hour || 0,
              }
            );
          }

          this.stats.agents_synced++;
        } catch (e) {
          const err_msg = e instanceof Error ? e.message : String(e);
          this.stats.errors.push(`Agent ${agent.id}: ${err_msg}`);
        }
      }

      await session.close();
    } catch (error) {
      const err_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Failed to ingest agents: ${err_msg}`);
    }
  }

  /**
   * Ingest capabilities from Supabase → Neo4j
   */
  private async ingest_capabilities(): Promise<void> {
    try {
      const { data: capabilities, error } = await this.supabase
        .from("capabilities")
        .select("*")
        .limit(1000);

      if (error) throw error;
      if (!capabilities || capabilities.length === 0) {
        console.log("No capabilities found in Supabase");
        return;
      }

      const session = this.neo4j_driver.session();

      for (const cap of capabilities) {
        try {
          const existing = await session.run("MATCH (c:Capability {id: $id}) RETURN c LIMIT 1", {
            id: cap.id,
          });

          if (existing.records.length === 0) {
            await session.run(
              `
              CREATE (c:Capability {
                id: $id,
                name: $name,
                category: $category,
                description: $description,
                complexity: $complexity,
                success_baseline: $success_baseline,
                cost_estimate: $cost_estimate,
                created_at: datetime()
              })
              `,
              {
                id: cap.id,
                name: cap.name,
                category: cap.category || "general",
                description: cap.description || "",
                complexity: cap.complexity || "medium",
                success_baseline: cap.success_baseline || 0.7,
                cost_estimate: cap.cost_estimate || 0,
              }
            );

            this.stats.capabilities_synced++;
          }
        } catch (e) {
          const err_msg = e instanceof Error ? e.message : String(e);
          this.stats.errors.push(`Capability ${cap.id}: ${err_msg}`);
        }
      }

      await session.close();
    } catch (error) {
      const err_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Failed to ingest capabilities: ${err_msg}`);
    }
  }

  /**
   * Ingest ventures from Supabase → Neo4j
   */
  private async ingest_ventures(): Promise<void> {
    try {
      const { data: ventures, error } = await this.supabase
        .from("ventures")
        .select("*")
        .limit(1000);

      if (error) throw error;
      if (!ventures || ventures.length === 0) {
        console.log("No ventures found in Supabase");
        return;
      }

      const session = this.neo4j_driver.session();

      for (const venture of ventures) {
        try {
          const existing = await session.run("MATCH (v:Venture {id: $id}) RETURN v LIMIT 1", {
            id: venture.id,
          });

          if (existing.records.length === 0) {
            await session.run(
              `
              CREATE (v:Venture {
                id: $id,
                name: $name,
                sector: $sector,
                stage: $stage,
                readiness: $readiness,
                revenue_monthly: $revenue_monthly,
                created_at: datetime()
              })
              `,
              {
                id: venture.id,
                name: venture.name,
                sector: venture.sector,
                stage: venture.stage || "planned",
                readiness: venture.readiness || 0,
                revenue_monthly: venture.revenue_monthly || 0,
              }
            );

            this.stats.ventures_synced++;
          }
        } catch (e) {
          const err_msg = e instanceof Error ? e.message : String(e);
          this.stats.errors.push(`Venture ${venture.id}: ${err_msg}`);
        }
      }

      await session.close();
    } catch (error) {
      const err_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Failed to ingest ventures: ${err_msg}`);
    }
  }

  /**
   * Link agents to capabilities (HAS_CAPABILITY relationships)
   */
  private async link_agent_capabilities(): Promise<void> {
    try {
      const { data: links, error } = await this.supabase
        .from("agent_capabilities")
        .select("agent_id, capability_id")
        .limit(5000);

      if (error || !links) return;

      const session = this.neo4j_driver.session();

      for (const link of links) {
        try {
          await session.run(
            `
            MATCH (a:Agent {id: $agent_id})
            MATCH (c:Capability {id: $capability_id})
            MERGE (a)-[r:HAS_CAPABILITY]->(c)
            SET r.proficiency = 0.8,
                r.num_uses = 0,
                r.last_used_at = datetime()
            `,
            {
              agent_id: link.agent_id,
              capability_id: link.capability_id,
            }
          );

          this.stats.relationships_created++;
        } catch (e) {
          const err_msg = e instanceof Error ? e.message : String(e);
          this.stats.errors.push(`Link ${link.agent_id}->${link.capability_id}: ${err_msg}`);
        }
      }

      await session.close();
    } catch (error) {
      const err_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Failed to link agent capabilities: ${err_msg}`);
    }
  }

  /**
   * Link ventures to agents (PART_OF_ORG relationships)
   */
  private async link_venture_agents(): Promise<void> {
    try {
      const session = this.neo4j_driver.session();

      // Link ventures to agents by sector + org matching
      await session.run(`
        MATCH (v:Venture)
        MATCH (a:Agent)
        WHERE v.sector = a.org_id
        MERGE (v)-[r:PART_OF_ORG]->(a)
        SET r.linked_at = datetime()
      `);

      await session.close();
    } catch (error) {
      const err_msg = error instanceof Error ? error.message : String(error);
      this.stats.errors.push(`Failed to link ventures to agents: ${err_msg}`);
    }
  }

  /**
   * Stub: Embed agents to Qdrant
   * In Round 3, use Claude embeddings API to generate vectors
   */
  async embed_to_qdrant(): Promise<void> {
    console.log("Qdrant embedding stub — ready for Round 3 wiring");
    // Will call Anthropic embeddings API + Qdrant upsert
  }

  /**
   * Health check
   */
  async health_check(): Promise<boolean> {
    try {
      const session = this.neo4j_driver.session();
      const result = await session.run("RETURN 1");
      await session.close();
      return result.records.length > 0;
    } catch {
      return false;
    }
  }

  async close(): Promise<void> {
    await this.neo4j_driver.close();
  }
}

// CLI entry point (for Round 3)
if (require.main === module) {
  const pipeline = new IngestionPipeline(
    process.env.SUPABASE_URL || "http://localhost:54321",
    process.env.SUPABASE_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    process.env.NEO4J_URI || "neo4j://localhost:7687",
    process.env.NEO4J_USER || "neo4j",
    process.env.NEO4J_PASSWORD || "ventures2026",
    process.env.ANTHROPIC_API_KEY || ""
  );

  pipeline
    .ingest()
    .then((stats) => {
      console.log("Ingestion completed:", stats);
      process.exit(0);
    })
    .catch((error) => {
      console.error("Ingestion failed:", error);
      process.exit(1);
    });
}

export default IngestionPipeline;
