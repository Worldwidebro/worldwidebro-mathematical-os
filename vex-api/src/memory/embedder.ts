import crypto from 'crypto';

/**
 * Phase 2 Embedder: Semantic text vectorization
 *
 * CURRENT: Hash-based stub (deterministic but not ML-based)
 * TODO (Phase 3): Replace with @xenova/transformers for MiniLM-L6-v2 ONNX model
 *                 Once added to package.json, swap this for real sentence embeddings
 *
 * Interface: Synchronous embedding → 384-dim vector
 * Qdrant uses COSINE distance; hash stub uses normalized fixed dims
 */

export interface Embedding {
  vector: number[];
  model: string;
  dim: number;
}

export class LocalEmbedder {
  private dim = 384; // Target dim for Qdrant collection
  private model = 'hash-stub'; // TODO: 'sentence-transformers/all-MiniLM-L6-v2'

  /**
   * Embed text to fixed-dim vector
   * PONYTAIL: Hash-based stub respects "no new deps" constraint.
   * Real embeddings require: npm install @xenova/transformers
   */
  embed(text: string): Embedding {
    // Hash the text and spread into 384 dimensions
    // This is deterministic but NOT semantic - placeholder only
    const hash = crypto.createHash('sha256').update(text).digest();

    const vector: number[] = [];
    for (let i = 0; i < this.dim; i++) {
      const byte = hash[i % hash.length];
      // Normalize byte (0-255) to range (-1, 1) for COSINE distance
      vector.push((byte / 128) - 1);
    }

    return {
      vector,
      model: this.model,
      dim: this.dim,
    };
  }

  /**
   * Batch embed (optional optimization)
   * Current: Sequential. Phase 3 can parallelize.
   */
  embedBatch(texts: string[]): Embedding[] {
    return texts.map(text => this.embed(text));
  }

  getDim(): number {
    return this.dim;
  }

  getModel(): string {
    return this.model;
  }
}

export const embedder = new LocalEmbedder();
