import express from 'express';
// @ts-ignore
import cors from 'cors';
import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';
import Stripe from 'stripe';
import authRouter from './routes/auth';
import propertiesRouter from './routes/properties';
import rentPaymentsRouter from './routes/rent-payments';
import maintenanceRouter from './routes/maintenance';
import reportsRouter from './routes/reports';
import emailRouter from './routes/email';
import adminRouter from './routes/admin';
import analyticsRouter from './routes/analytics';
import agentsRouter from './routes/agents';
import servicesRouter from './routes/services';

dotenv.config();

const app = express();
const port = process.env.PORT || 3001;

// Middleware
app.use(cors({ origin: [process.env.FRONTEND_URL || 'http://localhost:3000', 'http://localhost:5173'] }));
app.use(express.json());

// Initialize Supabase & Stripe (with safe fallbacks for build & dev)
export const supabase = createClient(
  process.env.SUPABASE_URL || 'https://placeholder.supabase.co',
  process.env.SUPABASE_SERVICE_ROLE_KEY || 'placeholder-key'
);

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_placeholder', {
  apiVersion: '2023-08-16' as any,
});

// Health check endpoint
app.get('/api/health', async (req, res) => {
  try {
    const { error } = await supabase.from('users').select('id').limit(1);
    if (error) throw error;
    res.json({ status: 'ok', db: 'connected' });
  } catch (err) {
    res.json({ status: 'ok', db: 'mock_mode', message: String(err) });
  }
});

// AI Agents Registry API Gateway
app.use('/api/agents', agentsRouter);

// Feature & domain routers
app.use('/api/auth', authRouter);
app.use('/api/properties', propertiesRouter);
app.use('/api/rent-payments', rentPaymentsRouter);
app.use('/api/maintenance', maintenanceRouter);
app.use('/api/reports', reportsRouter);
app.use('/api/email', emailRouter);
app.use('/api/admin', adminRouter);
app.use('/api/analytics', analyticsRouter);

// Central Microservice Gateway Router for 35 Core Microservices
app.use('/api/services', servicesRouter);
app.use('/api', servicesRouter);

// Error handler
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err);
  res.status(err.status || 500).json({ error: err.message || String(err) });
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(port, () => {
    console.log(`Real Estate OS API Gateway running on port ${port}`);
  });
}

export default app;
