// Static seed capabilities from seed-graph.ts
const SEED_CAPABILITIES = [
    {
        name: 'venture-analysis',
        description: 'Analyze venture viability, market fit, and execution readiness',
        keywords: ['venture', 'analysis', 'viability', 'market', 'readiness'],
        category: 'strategy',
    },
    {
        name: 'financial-modeling',
        description: 'Build financial models, projections, and unit economics',
        keywords: ['financial', 'modeling', 'projections', 'economics', 'revenue'],
        category: 'finance',
    },
    {
        name: 'market-research',
        description: 'Research markets, competitors, and customer segments',
        keywords: ['market', 'research', 'competitors', 'customer', 'segments'],
        category: 'strategy',
    },
    {
        name: 'team-building',
        description: 'Recruit, hire, and build high-performing teams',
        keywords: ['team', 'building', 'hire', 'recruit', 'talent'],
        category: 'operations',
    },
    {
        name: 'process-optimization',
        description: 'Streamline operations, reduce waste, improve efficiency',
        keywords: ['process', 'optimization', 'efficiency', 'workflow', 'automation'],
        category: 'operations',
    },
    {
        name: 'risk-assessment',
        description: 'Identify, quantify, and mitigate business risks',
        keywords: ['risk', 'assessment', 'mitigation', 'compliance', 'security'],
        category: 'strategy',
    },
    {
        name: 'sales',
        description: 'Drive customer acquisition, pipeline management, and revenue',
        keywords: ['sales', 'customer', 'acquisition', 'pipeline', 'revenue'],
        category: 'revenue',
    },
    {
        name: 'operations',
        description: 'Manage day-to-day operations, vendor relations, and logistics',
        keywords: ['operations', 'vendor', 'logistics', 'supply', 'chain'],
        category: 'operations',
    },
    {
        name: 'technology',
        description: 'Build technical infrastructure, architecture, and systems',
        keywords: ['technology', 'infrastructure', 'architecture', 'engineering', 'systems'],
        category: 'technology',
    },
    {
        name: 'strategy',
        description: 'Define vision, roadmap, and strategic direction',
        keywords: ['strategy', 'vision', 'roadmap', 'direction', 'planning'],
        category: 'strategy',
    },
];
export class CapabilitiesRegistry {
    constructor(driver) {
        this.driver = driver;
        this.seedCapabilities = new Map(SEED_CAPABILITIES.map(cap => [cap.name.toLowerCase(), cap]));
    }
    /**
     * Get all seed capabilities
     */
    getSeedCapabilities() {
        return SEED_CAPABILITIES;
    }
    /**
     * Look up a capability by name
     */
    getCapability(name) {
        return this.seedCapabilities.get(name.toLowerCase());
    }
    /**
     * Get capabilities by category
     */
    getCapabilitiesByCategory(category) {
        return SEED_CAPABILITIES.filter(c => c.category === category.toLowerCase());
    }
    /**
     * Query Neo4j for dynamic capabilities loaded from the graph
     */
    async getDynamicCapabilities() {
        const session = this.driver.session();
        try {
            const result = await session.run(`MATCH (c:Capability)
         RETURN c.name as name, c.description as description, c.keywords as keywords, c.category as category`);
            if (result.records.length === 0) {
                return SEED_CAPABILITIES;
            }
            return result.records.map(r => ({
                name: r.get('name'),
                description: r.get('description') || '',
                keywords: r.get('keywords') || [],
                category: r.get('category') || 'general'
            }));
        }
        catch (err) {
            console.error('⚠️ Failed to get dynamic capabilities from Neo4j:', err);
            return SEED_CAPABILITIES;
        }
        finally {
            await session.close();
        }
    }
    /**
     * Search capabilities by keyword
     */
    searchByKeyword(keyword) {
        const lower = keyword.toLowerCase();
        return SEED_CAPABILITIES.filter(cap => cap.keywords.some(k => k.includes(lower) || lower.includes(k)) ||
            cap.name.toLowerCase().includes(lower) ||
            cap.description.toLowerCase().includes(lower));
    }
}
//# sourceMappingURL=capabilities-registry.js.map