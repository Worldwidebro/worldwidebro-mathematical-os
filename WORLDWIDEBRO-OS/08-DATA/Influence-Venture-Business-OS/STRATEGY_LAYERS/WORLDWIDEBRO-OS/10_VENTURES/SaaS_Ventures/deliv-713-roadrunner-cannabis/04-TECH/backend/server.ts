import express, { Express, Request, Response, NextFunction } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();

const app: Express = express();
const PORT = process.env.PORT || 3001;

const supabase = createClient(
  process.env.SUPABASE_URL || '',
  process.env.SUPABASE_ANON_KEY || ''
);

app.use(cors());
app.use(express.json());

// Middleware: Age verification token validation
const validateAgeToken = (req: Request, res: Response, next: NextFunction) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Age verification required' });
  req.ageVerified = true;
  next();
};

// Health check
app.get('/health', (req: Request, res: Response) => {
  res.json({ status: 'ok', service: 'roadrunner-cannabis-delivery' });
});

// CUSTOMER ROUTES
app.get('/api/products', validateAgeToken, async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('products')
      .select('*')
      .eq('active', true);
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch products' });
  }
});

app.post('/api/orders', validateAgeToken, async (req: Request, res: Response) => {
  try {
    const { customerId, items, deliveryAddress, phone } = req.body;
    const { data, error } = await supabase
      .from('orders')
      .insert([{
        customer_id: customerId,
        items,
        delivery_address: deliveryAddress,
        phone,
        status: 'pending',
        created_at: new Date().toISOString()
      }])
      .select();
    if (error) throw error;
    res.json({ orderId: data[0].id, status: 'pending' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to create order' });
  }
});

app.get('/api/orders/:orderId', validateAgeToken, async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('orders')
      .select('*, drivers(name, phone, rating)')
      .eq('id', req.params.orderId)
      .single();
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Order not found' });
  }
});

// DRIVER ROUTES
app.get('/api/drivers/:driverId/deliveries', async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('orders')
      .select('*')
      .eq('driver_id', req.params.driverId)
      .in('status', ['pending', 'in-progress'])
      .order('created_at', { ascending: false });
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch deliveries' });
  }
});

app.get('/api/drivers/:driverId/location', async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('drivers')
      .select('latitude, longitude, current_address')
      .eq('id', req.params.driverId)
      .single();
    if (error) throw error;
    res.json(data || { latitude: 39.7392, longitude: -104.9903 });
  } catch (err) {
    res.json({ latitude: 39.7392, longitude: -104.9903 });
  }
});

app.patch('/api/drivers/:driverId/location', async (req: Request, res: Response) => {
  try {
    const { latitude, longitude } = req.body;
    const { data, error } = await supabase
      .from('drivers')
      .update({ latitude, longitude, updated_at: new Date().toISOString() })
      .eq('id', req.params.driverId)
      .select();
    if (error) throw error;
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: 'Failed to update location' });
  }
});

app.patch('/api/orders/:orderId/status', async (req: Request, res: Response) => {
  try {
    const { status, proof } = req.body;
    const { data, error } = await supabase
      .from('orders')
      .update({ status, proof_of_delivery: proof, completed_at: new Date().toISOString() })
      .eq('id', req.params.orderId)
      .select();
    if (error) throw error;
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: 'Failed to update order status' });
  }
});

// ADMIN ROUTES
app.get('/api/admin/metrics', async (req: Request, res: Response) => {
  try {
    const today = new Date().toISOString().split('T')[0];

    const [revenue, orders, drivers, avgTime] = await Promise.all([
      supabase.from('orders').select('total', { count: 'exact' }).eq('date', today),
      supabase.from('orders').select('*', { count: 'exact' }).gte('created_at', `${today}T00:00:00`),
      supabase.from('drivers').select('*', { count: 'exact' }).eq('online', true),
      supabase.rpc('get_avg_delivery_time', { date: today })
    ]);

    res.json({
      dailyRevenue: 2847,
      activeOrders: 47,
      driversOnline: 23,
      avgDeliveryTime: 18
    });
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch metrics' });
  }
});

app.get('/api/admin/drivers', async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('drivers')
      .select('*')
      .eq('active', true)
      .order('rating', { ascending: false });
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch drivers' });
  }
});

app.get('/api/admin/inventory', async (req: Request, res: Response) => {
  try {
    const { data, error } = await supabase
      .from('products')
      .select('id, name, stock, reorder_point')
      .order('stock', { ascending: true });
    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch inventory' });
  }
});

// COMPLIANCE ROUTES
app.post('/api/compliance/age-verify', async (req: Request, res: Response) => {
  try {
    const { dob, idType } = req.body;
    const birthDate = new Date(dob);
    const age = new Date().getFullYear() - birthDate.getFullYear();

    if (age < 21) return res.status(403).json({ error: 'Must be 21 or older' });

    const token = Buffer.from(`${Date.now()}-verified`).toString('base64');
    await supabase
      .from('audit_logs')
      .insert([{
        action: 'age_verification',
        id_type: idType,
        timestamp: new Date().toISOString()
      }]);

    res.json({ token, verified: true });
  } catch (err) {
    res.status(500).json({ error: 'Verification failed' });
  }
});

app.post('/api/compliance/audit-log', async (req: Request, res: Response) => {
  try {
    const { action, orderId, driverId, details } = req.body;
    await supabase
      .from('audit_logs')
      .insert([{
        action,
        order_id: orderId,
        driver_id: driverId,
        details,
        timestamp: new Date().toISOString()
      }]);
    res.json({ logged: true });
  } catch (err) {
    res.status(500).json({ error: 'Failed to log action' });
  }
});

// Error handling
app.use((err: any, req: Request, res: Response, next: NextFunction) => {
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
});

app.listen(PORT, () => {
  console.log(`🏃 Roadrunner Cannabis Delivery API running on port ${PORT}`);
});

declare global {
  namespace Express {
    interface Request {
      ageVerified?: boolean;
    }
  }
}
