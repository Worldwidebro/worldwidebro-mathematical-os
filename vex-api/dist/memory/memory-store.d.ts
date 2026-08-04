/**
 * Phase 2 TaskMemoryStore: Semantic memory for agent context
 *
 * Stores task descriptions as 384-dim embeddings in Qdrant
 * Enables: "find tasks similar to X" for context routing
 * PONYTAIL: Minimal interface, synchronous, no cache (Redis Phase 3)
 */
export interface StoredTask {
    id: string;
    venture_id: string;
    agent_id: string;
    content: string;
    created_at: string;
    metadata?: Record<string, any>;
}
export interface TaskQuery {
    content: string;
    venture_id?: string;
    limit?: number;
}
export declare class TaskMemoryStore {
    private initialized;
    /**
     * Initialize Qdrant collection
     * Call once on app startup
     */
    initialize(): Promise<void>;
    /**
     * Remember a task: embed and store in Qdrant
     * Returns the stored task ID
     */
    rememberTask(task: Omit<StoredTask, 'id' | 'created_at'>): Promise<string>;
    /**
     * Remember multiple tasks (batch)
     * Returns array of stored task IDs
     */
    rememberTasksBatch(tasks: Array<Omit<StoredTask, 'id' | 'created_at'>>): Promise<string[]>;
    /**
     * Find tasks similar to a query
     * Returns top K matches by semantic similarity
     *
     * Phase 3: Add optional filter by venture_id, agent_id
     */
    findSimilarTasks(query: TaskQuery): Promise<StoredTask[]>;
    /**
     * Find tasks for a specific venture
     * Optional: filter by agent or similarity threshold
     *
     * Phase 3: Add caching
     */
    findTasksByVenture(ventureId: string, content?: string, limit?: number): Promise<StoredTask[]>;
    /**
     * Delete a task from memory
     */
    forgetTask(taskId: string): Promise<void>;
    /**
     * Health check: is Qdrant running?
     */
    health(): Promise<boolean>;
}
export declare const taskMemoryStore: TaskMemoryStore;
//# sourceMappingURL=memory-store.d.ts.map