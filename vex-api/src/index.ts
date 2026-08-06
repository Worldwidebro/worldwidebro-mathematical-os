import dotenv from 'dotenv';
import express from 'express';
import cors from 'cors';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

import { initNeo4j, initSupabase } from './db.js';
import { taskMemoryStore } from './memory/memory-store.js';
import { CapabilityEngine } from './capability/engine.js';
import { CapabilitiesRegistry } from './capability/capabilities-registry.js';

// Route imports
import { dashboardRouter } from './routes/dashboard.js';
import { capabilityRouter } from './routes/capabilities.js';
import { capitalRoutingRouter } from './routes/capital-routing.js';
import { memoryRouter } from './routes/memory.js';
import matchingRouter from './routes/api/matching.js';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Log middleware
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// Initialize Datastores & Engines
let neoDriver: any;
let supabase: any;

try {
  neoDriver = initNeo4j();
  app.locals.neoDriver = neoDriver;
  console.log('Neo4j Driver initialized.');
  
  // Test Neo4j connection asynchronously
  neoDriver.verifyConnectivity()
    .then(() => console.log('✅ Connected to Neo4j Graph Database.'))
    .catch((err: any) => console.warn('⚠️ Neo4j offline. Graph queries will fail, falling back. Details:', err.message));
} catch (err: any) {
  console.warn('⚠️ Failed to initialize Neo4j driver:', err.message);
}

try {
  supabase = initSupabase();
  app.locals.supabase = supabase;
  console.log('Supabase Client initialized.');
} catch (err: any) {
  console.warn('⚠️ Failed to initialize Supabase client:', err.message);
}

// Initialize Capability Engine
try {
  if (neoDriver) {
    const registry = new CapabilitiesRegistry(neoDriver);
    const capabilityEngine = new CapabilityEngine(taskMemoryStore, registry);
    app.locals.capabilityEngine = capabilityEngine;
    console.log('Capability Engine initialized.');
  }
} catch (err: any) {
  console.warn('⚠️ Failed to initialize Capability Engine:', err.message);
}

// Add task memory store to locals
app.locals.taskMemoryStore = taskMemoryStore;

// Mount API routes
app.use('/api/dashboard', dashboardRouter);
app.use('/api/capabilities', capabilityRouter);
app.use('/api/capital', capitalRoutingRouter);
app.use('/api/memory', memoryRouter);
app.use('/api/matching', matchingRouter);

// Serve static dashboard page
// We will look for dashboard.html in __dirname/dashboard, process.cwd()/src/dashboard, or process.cwd()/vex-api/src/dashboard
let staticPath = path.join(__dirname, 'dashboard');
if (!fs.existsSync(path.join(staticPath, 'dashboard.html'))) {
  const devPath = path.resolve(process.cwd(), 'src/dashboard');
  if (fs.existsSync(path.join(devPath, 'dashboard.html'))) {
    staticPath = devPath;
  } else {
    const subfolderPath = path.resolve(process.cwd(), 'vex-api/src/dashboard');
    if (fs.existsSync(path.join(subfolderPath, 'dashboard.html'))) {
      staticPath = subfolderPath;
    }
  }
}

app.use('/dashboard', express.static(staticPath));
app.use('/static-dashboard', express.static(staticPath));

// Route "/" and "/dashboard" to serve the dashboard.html directly
app.get('/', (req, res) => {
  res.sendFile(path.join(staticPath, 'dashboard.html'));
});
app.get('/dashboard', (req, res) => {
  res.sendFile(path.join(staticPath, 'dashboard.html'));
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    services: {
      port: PORT,
      database: !!neoDriver,
      supabase: !!supabase,
    }
  });
});

// Global Error Handler
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error('Express Error:', err);
  res.status(500).json({ error: err.message || 'Internal Server Error' });
});

// Start Express server
app.listen(PORT, () => {
  console.log(`
  ==========================================
   VEX API & Hermes Command Center Started
  ==========================================
   Dashboard: http://localhost:${PORT}/dashboard
   Health:    http://localhost:${PORT}/health
   Port:      ${PORT}
  ==========================================
  `);
});
