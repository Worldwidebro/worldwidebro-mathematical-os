/**
 * Phase 2 Qdrant Client: Vector database operations
 *
 * Connects to local Qdrant (default: http://localhost:6333)
 * Collection: task_memory (384-dim, COSINE distance)
 * PONYTAIL: Synchronous operations, minimal error handling, direct HTTP
 */
export interface QdrantPoint {
    id: string;
    vector: number[];
    payload: Record<string, any>;
}
export interface SearchResult {
    id: string;
    score: number;
    payload: Record<string, any>;
}
export declare class QdrantClient {
    private baseUrl;
    private collection;
    private dim;
    constructor(baseUrl?: string);
    /**
     * Initialize collection if not exists
     * COSINE distance, 384 dimensions, HNSW index
     */
    initCollection(): Promise<void>;
    /**
     * Store a point (task embedding) in Qdrant
     */
    upsert(point: QdrantPoint): Promise<void>;
    /**
     * Batch upsert points
     */
    upsertBatch(points: QdrantPoint[]): Promise<void>;
    /**
     * Search by vector similarity
     * Returns top K results sorted by score (highest first)
     */
    search(vector: number[], limit?: number, scoreThreshold?: number): Promise<SearchResult[]>;
    /**
     * Delete a point by task_id
     */
    delete(taskId: string): Promise<void>;
    /**
     * Health check
     */
    health(): Promise<boolean>;
    /**
     * Convert string UUID to deterministic number for Qdrant point ID
     * Qdrant requires numeric point IDs; hash UUID to int64-safe range
     */
    private hashIdToNum;
}
export declare const qdrantClient: QdrantClient;
//# sourceMappingURL=qdrant-client.d.ts.map