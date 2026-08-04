/**
 * ontology.ts — Query helpers for the IZA OS Ontology (docs/ONTOLOGY.md, v2.1).
 *
 * Pattern reference, not a framework: loads the ontology doc, and gives
 * thin query/sync helpers over the two stores the ontology defines as
 * primary — Neo4j (graph/relationships) and Supabase (transactional).
 *
 * Wire up real drivers before use:
 *   npm install neo4j-driver @supabase/supabase-js
 *
 * Env vars expected:
 *   NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
 *   SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 */

import { readFileSync } from "fs";
import { join } from "path";

// ---- Types -----------------------------------------------------------

/** One of the 10 core entity types defined in ONTOLOGY.md. */
export type EntityType =
  | "Venture"
  | "Repository"
  | "Capability"
  | "Skill"
  | "MCP"
  | "OPCO"
  | "Sector"
  | "InfrastructureService"
  | "Entity"
  | "Chat2DB";

/** The 12 canonical relationship types from ONTOLOGY.md. */
export type RelationshipType =
  | "OWNS"
  | "OPERATES"
  | "USES"
  | "CREATED"
  | "MODIFIED"
  | "DEPENDS_ON"
  | "OPERATED_BY"
  | "GENERATES"
  | "EXECUTES"
  | "PRODUCES"
  | "CREATES"
  | "TOUCHES";

export interface OntologyDoc {
  version: string;
  raw: string;
}

export interface Relationship {
  sourceEntityId: string;
  relationshipType: RelationshipType;
  targetEntityId: string;
  properties?: Record<string, unknown>;
}

// ---- loadOntology ------------------------------------------------------

/**
 * Reads docs/ONTOLOGY.md (symlinked to the canonical Documents/ONTOLOGY.md)
 * and extracts the frontmatter version. Fails loudly if the doc is missing
 * or the symlink is broken — ontology_version drift is a silent-corruption
 * risk, so we don't swallow it.
 */
export function loadOntology(
  docsDir: string = join(__dirname, "..", "..", "docs")
): OntologyDoc {
  const path = join(docsDir, "ONTOLOGY.md");
  const raw = readFileSync(path, "utf-8");
  const match = raw.match(/^version:\s*([\d.]+)/m);
  if (!match) {
    throw new Error(`ONTOLOGY.md at ${path} has no frontmatter "version:" field`);
  }
  return { version: match[1], raw };
}

// ---- queryEntity ---------------------------------------------------------

/**
 * Fetches a single entity by type + id.
 * Per ONTOLOGY.md's Storage Map, Venture/Capability/OPCO/Sector read
 * primary from Supabase (Postgres); Repository reads primary from Qdrant
 * (not wired here — vector store, out of scope for this minimal helper).
 * ponytail: routes everything through Supabase for simplicity; add the
 * Qdrant path when Repository queries are actually needed.
 */
export async function queryEntity<T = Record<string, unknown>>(
  supabase: SupabaseLike,
  type: EntityType,
  id: string
): Promise<T | null> {
  const table = type.toLowerCase() + "s"; // Venture -> ventures, Skill -> skills, etc.
  const { data, error } = await supabase
    .from(table)
    .select("*")
    .eq("id", id)
    .maybeSingle();
  if (error) throw error;
  return (data as T) ?? null;
}

// ---- findRelationships -----------------------------------------------

/**
 * Graph traversal for relationships touching an entity, via Neo4j Cypher.
 * Direction "out" = entity is source, "in" = entity is target, "both" = either.
 */
export async function findRelationships(
  neo4j: Neo4jLike,
  entityId: string,
  direction: "out" | "in" | "both" = "both"
): Promise<Relationship[]> {
  const pattern =
    direction === "out"
      ? "(a {id: $id})-[r]->(b)"
      : direction === "in"
      ? "(a)-[r]->(b {id: $id})"
      : "(a)-[r]-(b {id: $id})";

  const session = neo4j.session();
  try {
    const result = await session.run(
      `MATCH ${pattern} RETURN a.id AS source, type(r) AS relType, b.id AS target, properties(r) AS props`,
      { id: entityId }
    );
    return result.records.map((rec) => ({
      sourceEntityId: rec.get("source"),
      relationshipType: rec.get("relType") as RelationshipType,
      targetEntityId: rec.get("target"),
      properties: rec.get("props"),
    }));
  } finally {
    await session.close();
  }
}

// ---- syncToSupabase ----------------------------------------------------

/**
 * Upserts a batch of entities into Supabase and mirrors each as a node
 * in Neo4j, matching ONTOLOGY.md's dual-storage model (Entity: Neo4j +
 * Supabase). Best-effort mirror: Supabase write is authoritative — if the
 * Neo4j mirror fails, the row is still synced and the failure is returned
 * for the caller to retry/alert on.
 */
export async function syncToSupabase(
  supabase: SupabaseLike,
  neo4j: Neo4jLike,
  type: EntityType,
  rows: Array<Record<string, unknown> & { id: string }>
): Promise<{ synced: string[]; failed: Array<{ id: string; error: unknown }> }> {
  const table = type.toLowerCase() + "s";
  const { error } = await supabase.from(table).upsert(rows);
  if (error) throw error;

  const synced: string[] = [];
  const failed: Array<{ id: string; error: unknown }> = [];
  const session = neo4j.session();
  try {
    for (const row of rows) {
      try {
        await session.run(
          `MERGE (n:${type} {id: $id}) SET n += $props`,
          { id: row.id, props: row }
        );
        synced.push(row.id);
      } catch (err) {
        failed.push({ id: row.id, error: err });
      }
    }
  } finally {
    await session.close();
  }
  return { synced, failed };
}

// ---- Minimal driver interfaces (swap for real neo4j-driver / supabase-js) --

export interface SupabaseLike {
  from(table: string): {
    select(cols: string): { eq(col: string, val: string): { maybeSingle(): Promise<{ data: unknown; error: unknown }> } };
    upsert(rows: unknown[]): Promise<{ error: unknown }>;
  };
}

export interface Neo4jLike {
  session(): {
    run(query: string, params?: Record<string, unknown>): Promise<{ records: Array<{ get(key: string): any }> }>;
    close(): Promise<void>;
  };
}
