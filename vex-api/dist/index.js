import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { initNeo4j, initSupabase } from './db.js';
import { networkRouter } from './routes/network.js';
import { ventureRouter } from './routes/venture.js';
import { agentRouter } from './routes/agent.js';
import { founderRouter } from './routes/founder.js';
import { capitalRoutingRouter } from './routes/capital-routing.js';
import { seedHumanOS } from './seed-human-os.js';
import { initGraphSchema } from './knowledge-graph/neo4j-client.js';
import { seedGraph } from './knowledge-graph/seed-graph.js';
dotenv.config();
const app = express();
const PORT = process.env.PORT || 3001;
// Middleware
app.use(cors());
app.use(express.json());
// Initialize databases
const neo4j = initNeo4j();
const supabase = initSupabase();
// Store in app locals for route access
app.locals.neo4j = neo4j;
app.locals.supabase = supabase;
// Routes
app.use('/network', networkRouter);
app.use('/ventures', ventureRouter);
app.use('/agents', agentRouter);
app.use('/founders', founderRouter);
app.use('/capital-allocation', capitalRoutingRouter);
// Seed Human OS framework on startup
seedHumanOS().catch(err => console.warn('Human OS seeding failed:', err));
// Initialize knowledge graph schema and seed OPCOs
initGraphSchema(neo4j).catch(err => console.warn('Graph schema init failed:', err));
seedGraph(neo4j).catch(err => console.warn('Graph seeding failed:', err));
// Health check
app.get('/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
});
// Error handler
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
});
app.listen(PORT, () => {
    console.log(`🚀 vex-api listening on http://localhost:${PORT}`);
    console.log('📊 Neo4j: connected');
    console.log('🔵 Supabase: connected');
});
//# sourceMappingURL=index.js.map