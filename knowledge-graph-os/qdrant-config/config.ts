// Qdrant Configuration — Vector Collections for Semantic Search
// Collections: agent_embeddings, capability_embeddings, task_embeddings
// Vector size: 384 (nomic-embed or similar), Distance: cosine

export interface QdrantCollectionConfig {
  name: string;
  vector_size: number;
  distance: "cosine" | "euclidean" | "manhattan";
  payload_schema: Record<string, { type: string; description?: string }>;
  index_config?: {
    on_disk: boolean;
    hnsw_config?: {
      m: number;
      ef_construct: number;
      full_scan_threshold: number;
    };
  };
}

/**
 * Collection: agent_embeddings
 * Stores semantic embeddings for all agents in the system
 *
 * Payload fields:
 * - id: unique agent ID
 * - name: agent display name
 * - type: agent type (ai|human|system)
 * - org_id: organization ID (for org-scoped search)
 * - capabilities: array of capability IDs
 * - availability: float 0-1
 * - success_rate: float 0-1
 * - cost_per_hour: float
 * - embedding_model: which model generated this vector (nomic-embed-1.5)
 * - created_at: ISO timestamp
 * - updated_at: ISO timestamp
 */
export const agent_embeddings: QdrantCollectionConfig = {
  name: "agent_embeddings",
  vector_size: 384,
  distance: "cosine",
  payload_schema: {
    id: {
      type: "keyword",
      description: "Unique agent ID",
    },
    name: {
      type: "text",
      description: "Agent display name",
    },
    type: {
      type: "keyword",
      description: "Agent type: ai | human | system",
    },
    org_id: {
      type: "keyword",
      description: "Organization ID for scoped queries",
    },
    capabilities: {
      type: "array",
      description: "List of capability IDs",
    },
    availability: {
      type: "float",
      description: "Availability score 0-1",
    },
    success_rate: {
      type: "float",
      description: "Historical success rate 0-1",
    },
    cost_per_hour: {
      type: "float",
      description: "Cost per hour for pricing filters",
    },
    embedding_model: {
      type: "keyword",
      description: "Model used for embedding",
    },
    created_at: {
      type: "datetime",
      description: "Creation timestamp",
    },
    updated_at: {
      type: "datetime",
      description: "Last update timestamp",
    },
  },
  index_config: {
    on_disk: false,
    hnsw_config: {
      m: 16,
      ef_construct: 200,
      full_scan_threshold: 10000,
    },
  },
};

/**
 * Collection: capability_embeddings
 * Stores semantic embeddings for all capabilities in the system
 *
 * Payload fields:
 * - id: unique capability ID
 * - name: capability name (e.g., "code-review", "deploy")
 * - category: skill category (e.g., "engineering", "operations")
 * - description: long-form description
 * - complexity: low | medium | high
 * - success_baseline: baseline success rate 0-1
 * - cost_estimate: typical cost for this capability
 * - embedding_model: which model generated this vector
 * - created_at: ISO timestamp
 */
export const capability_embeddings: QdrantCollectionConfig = {
  name: "capability_embeddings",
  vector_size: 384,
  distance: "cosine",
  payload_schema: {
    id: {
      type: "keyword",
      description: "Unique capability ID",
    },
    name: {
      type: "text",
      description: "Capability name",
    },
    category: {
      type: "keyword",
      description: "Capability category",
    },
    description: {
      type: "text",
      description: "Long-form description",
    },
    complexity: {
      type: "keyword",
      description: "Complexity level: low | medium | high",
    },
    success_baseline: {
      type: "float",
      description: "Baseline success rate 0-1",
    },
    cost_estimate: {
      type: "float",
      description: "Typical cost estimate",
    },
    embedding_model: {
      type: "keyword",
      description: "Embedding model used",
    },
    created_at: {
      type: "datetime",
      description: "Creation timestamp",
    },
  },
  index_config: {
    on_disk: false,
    hnsw_config: {
      m: 16,
      ef_construct: 200,
      full_scan_threshold: 10000,
    },
  },
};

/**
 * Collection: task_embeddings
 * Stores semantic embeddings for task descriptions
 *
 * Payload fields:
 * - id: unique task ID
 * - name: task name
 * - status: pending | assigned | executing | completed | failed
 * - venture_id: associated venture
 * - priority: 0-5
 * - required_capabilities: array of capability IDs needed
 * - created_at: ISO timestamp
 */
export const task_embeddings: QdrantCollectionConfig = {
  name: "task_embeddings",
  vector_size: 384,
  distance: "cosine",
  payload_schema: {
    id: {
      type: "keyword",
      description: "Unique task ID",
    },
    name: {
      type: "text",
      description: "Task name",
    },
    status: {
      type: "keyword",
      description: "Task status",
    },
    venture_id: {
      type: "keyword",
      description: "Associated venture ID",
    },
    priority: {
      type: "integer",
      description: "Priority 0-5",
    },
    required_capabilities: {
      type: "array",
      description: "Array of required capability IDs",
    },
    created_at: {
      type: "datetime",
      description: "Creation timestamp",
    },
  },
  index_config: {
    on_disk: false,
    hnsw_config: {
      m: 16,
      ef_construct: 200,
      full_scan_threshold: 10000,
    },
  },
};

/**
 * All collections required for Phase 2
 */
export const ALL_COLLECTIONS = [agent_embeddings, capability_embeddings, task_embeddings];

/**
 * Qdrant setup helper — prepare collection configs for ingestion
 */
export function getCollectionConfig(collection_name: string): QdrantCollectionConfig | null {
  const configs: Record<string, QdrantCollectionConfig> = {
    agent_embeddings,
    capability_embeddings,
    task_embeddings,
  };
  return configs[collection_name] || null;
}
