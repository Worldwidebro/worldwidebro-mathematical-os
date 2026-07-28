import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { initNeo4j, initSupabase } from './db.js';
import { networkRouter } from './routes/network.js';
import { ventureRouter } from './routes/venture.js';
import { agentRouter } from './routes/agent.js';

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

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Error handler
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
});

app.listen(PORT, () => {
  console.log(`🚀 vex-api listening on http://localhost:${PORT}`);
  console.log('📊 Neo4j: connected');
  console.log('🔵 Supabase: connected');
});
