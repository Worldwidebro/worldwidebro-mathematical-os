import express from 'express';
import { supabase } from '../index';

const router = express.Router();

// GET /api/reports/property/:id/plp - P&L report
router.get('/property/:id/plp', async (req, res) => {
  try {
    const { data: units } = await supabase.from('units').select('*').eq('property_id', req.params.id);
    const { data: payments } = await supabase.from('rent_payments').select('*');
    const { data: maintenance } = await supabase.from('maintenance_requests').select('*');

    let totalRent = 0;
    let totalMaintenance = 0;

    if (units) {
      totalRent = units.reduce((sum, u) => sum + (u.rent_amount || 0), 0);
    }

    if (maintenance) {
      // Mock maintenance cost (would come from invoices in production)
      totalMaintenance = maintenance.length * 100;
    }

    res.json({
      rentIn: totalRent,
      maintenanceOut: totalMaintenance,
      net: totalRent - totalMaintenance,
    });
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/reports/property/:id/tenants - tenant roster export
router.get('/property/:id/tenants', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('units')
      .select('*, users(full_name, email, phone), leases(start_date, end_date)')
      .eq('property_id', req.params.id);

    if (error) throw error;

    const csv = ['Unit,Tenant,Email,Phone,Lease Start,Lease End'];
    data?.forEach((unit: any) => {
      const tenant = unit.users || {};
      const lease = unit.leases?.[0] || {};
      csv.push(
        `${unit.unit_number},${tenant.full_name || 'Vacant'},${tenant.email || ''},${tenant.phone || ''},${lease.start_date || ''},${lease.end_date || ''}`
      );
    });

    res.header('Content-Type', 'text/csv');
    res.send(csv.join('\n'));
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

export default router;
