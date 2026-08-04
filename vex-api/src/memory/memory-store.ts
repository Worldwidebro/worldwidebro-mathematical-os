import { v4 as uuidv4 } from 'uuid';
import { embedder } from './embedder.js';
import { qdrantClient, QdrantPoint } from './qdrant-client.js';

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

export class TaskMemoryStore {
  private initialized = false;

  /**
   * Initialize Qdrant collection
   * Call once on app startup
   */
  async initialize(): Promise<void> {
    try {
      const healthy = await qdrantClient.health();
      if (!healthy) {
        throw new Error('Qdrant not responding at localhost:6333');
      }
      await qdrantClient.initCollection();
      this.initialized = true;
      console.log('✓ TaskMemoryStore initialized');
    } catch (err) {
      console.error('TaskMemoryStore init failed:', err);
      throw err;
    }
  }

  /**
   * Remember a task: embed and store in Qdrant
   * Returns the stored task ID
   */
  async rememberTask(task: Omit<StoredTask, 'id' | 'created_at'>): Promise<string> {
    if (!this.initialized) {
      throw new Error('TaskMemoryStore not initialized. Call .initialize() first');
    }

    const taskId = uuidv4();
    const createdAt = new Date().toISOString();

    // Embed task content
    const embedding = embedder.embed(task.content);

    // Build Qdrant point
    const point: QdrantPoint = {
      id: taskId,
      vector: embedding.vector,
      payload: {
        task_id: taskId,
        venture_id: task.venture_id,
        agent_id: task.agent_id,
        content: task.content,
        created_at: createdAt,
        metadata: task.metadata || {},
      },
    };

    // Store in Qdrant
    await qdrantClient.upsert(point);

    return taskId;
  }

  /**
   * Remember multiple tasks (batch)
   * Returns array of stored task IDs
   */
  async rememberTasksBatch(
    tasks: Array<Omit<StoredTask, 'id' | 'created_at'>>,
  ): Promise<string[]> {
    if (!this.initialized) {
      throw new Error('TaskMemoryStore not initialized. Call .initialize() first');
    }

    const points: QdrantPoint[] = [];
    const ids: string[] = [];

    for (const task of tasks) {
      const taskId = uuidv4();
      const createdAt = new Date().toISOString();
      const embedding = embedder.embed(task.content);

      ids.push(taskId);
      points.push({
        id: taskId,
        vector: embedding.vector,
        payload: {
          task_id: taskId,
          venture_id: task.venture_id,
          agent_id: task.agent_id,
          content: task.content,
          created_at: createdAt,
          metadata: task.metadata || {},
        },
      });
    }

    await qdrantClient.upsertBatch(points);
    return ids;
  }

  /**
   * Find tasks similar to a query
   * Returns top K matches by semantic similarity
   *
   * Phase 3: Add optional filter by venture_id, agent_id
   */
  async findSimilarTasks(query: TaskQuery): Promise<StoredTask[]> {
    if (!this.initialized) {
      throw new Error('TaskMemoryStore not initialized. Call .initialize() first');
    }

    const limit = query.limit || 5;

    // Embed query
    const queryEmbedding = embedder.embed(query.content);

    // Search Qdrant
    const results = await qdrantClient.search(queryEmbedding.vector, limit);

    // Map results back to StoredTask format
    const tasks: StoredTask[] = results.map(result => ({
      id: result.payload.task_id,
      venture_id: result.payload.venture_id,
      agent_id: result.payload.agent_id,
      content: result.payload.content,
      created_at: result.payload.created_at,
      metadata: {
        ...result.payload.metadata,
        similarity_score: result.score,
      },
    }));

    return tasks;
  }

  /**
   * Find tasks for a specific venture
   * Optional: filter by agent or similarity threshold
   *
   * Phase 3: Add caching
   */
  async findTasksByVenture(
    ventureId: string,
    content?: string,
    limit = 10,
  ): Promise<StoredTask[]> {
    if (!this.initialized) {
      throw new Error('TaskMemoryStore not initialized. Call .initialize() first');
    }

    // If content provided, use semantic search
    if (content) {
      const all = await this.findSimilarTasks({
        content,
        venture_id: ventureId,
        limit,
      });
      // Filter to venture
      return all.filter(t => t.venture_id === ventureId);
    }

    // Otherwise, return empty for now (Phase 3: add scroll-based list)
    console.warn(
      `Unfiltered task listing not implemented. Use findSimilarTasks() with content.`,
    );
    return [];
  }

  /**
   * Delete a task from memory
   */
  async forgetTask(taskId: string): Promise<void> {
    if (!this.initialized) {
      throw new Error('TaskMemoryStore not initialized. Call .initialize() first');
    }

    await qdrantClient.delete(taskId);
  }

  /**
   * Health check: is Qdrant running?
   */
  async health(): Promise<boolean> {
    return qdrantClient.health();
  }
}

// Export singleton instance for routes
export const taskMemoryStore = new TaskMemoryStore();
