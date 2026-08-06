/**
 * Phase 2 Qdrant Client: Vector database operations
 *
 * Connects to local Qdrant (default: http://localhost:6333)
 * Collection: task_memory (384-dim, COSINE distance)
 * PONYTAIL: Synchronous operations, minimal error handling, direct HTTP
 */
export class QdrantClient {
    constructor(baseUrl = 'http://localhost:6333') {
        this.collection = 'task_memory';
        this.dim = 384;
        this.baseUrl = baseUrl;
    }
    /**
     * Initialize collection if not exists
     * COSINE distance, 384 dimensions, HNSW index
     */
    async initCollection() {
        try {
            // Check if collection exists
            const res = await fetch(`${this.baseUrl}/collections/${this.collection}`);
            if (res.ok) {
                console.log(`✓ Qdrant collection "${this.collection}" already exists`);
                return;
            }
            // Create collection
            console.log(`Creating Qdrant collection "${this.collection}"...`);
            const createRes = await fetch(`${this.baseUrl}/collections/${this.collection}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    vectors: {
                        size: this.dim,
                        distance: 'Cosine',
                    },
                    optimizers_config: {
                        default_segment_number: 2,
                    },
                    shard_number: 1,
                }),
            });
            if (!createRes.ok) {
                throw new Error(`Failed to create collection: ${createRes.statusText}`);
            }
            console.log(`✓ Collection "${this.collection}" created`);
        }
        catch (err) {
            console.error('Qdrant init error:', err);
            throw err;
        }
    }
    /**
     * Store a point (task embedding) in Qdrant
     */
    async upsert(point) {
        try {
            const res = await fetch(`${this.baseUrl}/collections/${this.collection}/points?wait=true`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    points: [
                        {
                            id: this.hashIdToNum(point.id),
                            vector: point.vector,
                            payload: point.payload,
                        },
                    ],
                }),
            });
            if (!res.ok) {
                throw new Error(`Upsert failed: ${res.statusText}`);
            }
        }
        catch (err) {
            console.error('Qdrant upsert error:', err);
            throw err;
        }
    }
    /**
     * Batch upsert points
     */
    async upsertBatch(points) {
        try {
            const res = await fetch(`${this.baseUrl}/collections/${this.collection}/points?wait=true`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    points: points.map(p => ({
                        id: this.hashIdToNum(p.id),
                        vector: p.vector,
                        payload: p.payload,
                    })),
                }),
            });
            if (!res.ok) {
                throw new Error(`Batch upsert failed: ${res.statusText}`);
            }
        }
        catch (err) {
            console.error('Qdrant batch upsert error:', err);
            throw err;
        }
    }
    /**
     * Search by vector similarity
     * Returns top K results sorted by score (highest first)
     */
    async search(vector, limit = 5, scoreThreshold = 0.0) {
        try {
            const res = await fetch(`${this.baseUrl}/collections/${this.collection}/points/search`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    vector,
                    limit,
                    score_threshold: scoreThreshold,
                    with_payload: true,
                }),
            });
            if (!res.ok) {
                throw new Error(`Search failed: ${res.statusText}`);
            }
            const data = await res.json();
            return (data.result || []).map((hit) => ({
                id: hit.payload.task_id || hit.id.toString(),
                score: hit.score,
                payload: hit.payload,
            }));
        }
        catch (err) {
            console.error('Qdrant search error:', err);
            throw err;
        }
    }
    /**
     * Delete a point by task_id
     */
    async delete(taskId) {
        try {
            const res = await fetch(`${this.baseUrl}/collections/${this.collection}/points/delete?wait=true`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    filter: {
                        must: [
                            {
                                key: 'task_id',
                                match: { value: taskId },
                            },
                        ],
                    },
                }),
            });
            if (!res.ok) {
                throw new Error(`Delete failed: ${res.statusText}`);
            }
        }
        catch (err) {
            console.error('Qdrant delete error:', err);
            throw err;
        }
    }
    /**
     * Health check
     */
    async health() {
        try {
            // ponytail: Qdrant serves liveness at /healthz, not /health
            const res = await fetch(`${this.baseUrl}/healthz`);
            return res.ok;
        }
        catch {
            return false;
        }
    }
    /**
     * Convert string UUID to deterministic number for Qdrant point ID
     * Qdrant requires numeric point IDs; hash UUID to int64-safe range
     */
    hashIdToNum(id) {
        let hash = 0;
        for (let i = 0; i < id.length; i++) {
            hash = ((hash << 5) - hash) + id.charCodeAt(i);
            hash |= 0; // Convert to 32-bit int
        }
        // Map to positive safe range (0 to 9007199254740991)
        return Math.abs(hash) % 9007199254740991;
    }
}
export const qdrantClient = new QdrantClient();
//# sourceMappingURL=qdrant-client.js.map