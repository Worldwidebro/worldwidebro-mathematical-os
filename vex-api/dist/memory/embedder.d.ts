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
export declare class LocalEmbedder {
    private dim;
    private model;
    /**
     * Embed text to fixed-dim vector
     * PONYTAIL: Hash-based stub respects "no new deps" constraint.
     * Real embeddings require: npm install @xenova/transformers
     */
    embed(text: string): Embedding;
    /**
     * Batch embed (optional optimization)
     * Current: Sequential. Phase 3 can parallelize.
     */
    embedBatch(texts: string[]): Embedding[];
    getDim(): number;
    getModel(): string;
}
export declare const embedder: LocalEmbedder;
//# sourceMappingURL=embedder.d.ts.map