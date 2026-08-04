import { initNeo4j } from './db';
/**
 * Seed Human OS framework into Neo4j
 *
 * Creates:
 * - HumanOS layers (L1-L10)
 * - Founder nodes with tier + metrics
 * - Relationships: Founder --DEVELOPS_LAYER--> Layer
 */
export async function seedHumanOS() {
    const driver = initNeo4j();
    const session = driver.session();
    try {
        // Create Human OS layers
        const layers = [
            { id: 'L1', name: 'Identity', description: 'Who am I' },
            { id: 'L2', name: 'Emotion', description: 'Signal processing' },
            { id: 'L3', name: 'Cognition', description: 'How I think' },
            { id: 'L4', name: 'Intuition', description: 'Compressed experience' },
            { id: 'L5', name: 'Energy', description: 'Capacity management' },
            { id: 'L6', name: 'Frequency', description: 'Observable state' },
            { id: 'L7', name: 'Network', description: 'Relationships' },
            { id: 'L8', name: 'Creativity', description: 'Transformation' },
            { id: 'L9', name: 'Character', description: 'Who under pressure' },
            { id: 'L10', name: 'Legacy', description: 'What outlasts me' },
        ];
        for (const layer of layers) {
            await session.run(`CREATE (l:HumanOSLayer {id: $id, name: $name, description: $description})`, layer);
        }
        console.log('✅ Seeded 10 Human OS layers into Neo4j');
    }
    catch (err) {
        console.error('Neo4j seeding failed:', err);
    }
    finally {
        await session.close();
        await driver.close();
    }
}
// Can be run directly with: node --loader ts-node/esm seed-human-os.ts
if (import.meta.url === `file://${process.argv[1]}`) {
    seedHumanOS().then(() => process.exit(0));
}
//# sourceMappingURL=seed-human-os.js.map