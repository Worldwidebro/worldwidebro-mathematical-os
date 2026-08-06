import { Driver as Neo4jDriver } from 'neo4j-driver';
/**
 * Phase 3 Capabilities Registry
 *
 * Static seed capabilities + dynamic Neo4j lookup
 * PONYTAIL: Seeds from seed-graph.ts, minimal interface
 */
export interface Capability {
    name: string;
    description: string;
    keywords: string[];
    category?: string;
}
export declare class CapabilitiesRegistry {
    private driver;
    private seedCapabilities;
    constructor(driver: Neo4jDriver);
    /**
     * Get all seed capabilities
     */
    getSeedCapabilities(): Capability[];
    /**
     * Look up a capability by name
     */
    getCapability(name: string): Capability | undefined;
    /**
     * Get capabilities by category
     */
    getCapabilitiesByCategory(category: string): Capability[];
    /**
     * Query Neo4j for dynamic capabilities loaded from the graph
     */
    getDynamicCapabilities(): Promise<Capability[]>;
    /**
     * Search capabilities by keyword
     */
    searchByKeyword(keyword: string): Capability[];
}
//# sourceMappingURL=capabilities-registry.d.ts.map