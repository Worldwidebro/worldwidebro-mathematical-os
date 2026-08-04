import { TaskMemoryStore } from '../memory/memory-store.js';
import { CapabilitiesRegistry } from './capabilities-registry.js';
/**
 * Phase 3 Capability Engine
 *
 * Task description → ranked list of (agent, capability, score)
 * PONYTAIL: Minimal scoring, sync text matching + semantic from taskMemoryStore
 */
export interface RankedCapability {
    agent: string;
    capability: string;
    score: number;
    source: 'text-match' | 'similar-task' | 'combined';
}
export declare class CapabilityEngine {
    private taskMemory;
    private registry;
    constructor(taskMemory: TaskMemoryStore, registry: CapabilitiesRegistry);
    /**
     * Main entry point: rank capabilities for a task description
     * Returns sorted list by descending score
     */
    rankCapabilities(taskDescription: string): Promise<RankedCapability[]>;
    /**
     * Simple text matching: word overlap + keyword matching
     * Returns 0-100 score
     */
    private scoreTextMatch;
    /**
     * Tiny string similarity: 1 - (edit_distance / max_length)
     * ponytail: 2 lines for levenshtein
     */
    private _similarity;
    /**
     * Extract capabilities from a stored task's metadata
     * Format: metadata.capabilities = ["venture-analysis", "market-research", ...]
     */
    private _extractCapabilitiesFromTask;
    /**
     * Map capability name to agent type
     * Simple mapping for Phase 3
     * Phase 4: Use Neo4j Agent nodes
     */
    private _mapCapabilityToAgent;
}
//# sourceMappingURL=engine.d.ts.map