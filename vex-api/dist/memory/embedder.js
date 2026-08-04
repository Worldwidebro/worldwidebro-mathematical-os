import crypto from 'crypto';
export class LocalEmbedder {
    constructor() {
        this.dim = 384; // Target dim for Qdrant collection
        this.model = 'hash-stub'; // TODO: 'sentence-transformers/all-MiniLM-L6-v2'
    }
    /**
     * Embed text to fixed-dim vector
     * PONYTAIL: Hash-based stub respects "no new deps" constraint.
     * Real embeddings require: npm install @xenova/transformers
     */
    embed(text) {
        // Hash the text and spread into 384 dimensions
        // This is deterministic but NOT semantic - placeholder only
        const hash = crypto.createHash('sha256').update(text).digest();
        const vector = [];
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
    embedBatch(texts) {
        return texts.map(text => this.embed(text));
    }
    getDim() {
        return this.dim;
    }
    getModel() {
        return this.model;
    }
}
export const embedder = new LocalEmbedder();
//# sourceMappingURL=embedder.js.map