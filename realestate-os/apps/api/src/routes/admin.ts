import express from 'express';
import { supabase } from '../index';

const router = express.Router();

// GET /api/admin/users - List all users with roles & suspension status
router.get('/users', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('users')
      .select('id, email, full_name, role, phone, is_suspended, suspension_reason, created_at')
      .order('created_at', { ascending: false });

    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/admin/users - Create new user (admin/landlord/tenant)
router.post('/users', async (req, res) => {
  const adminId = req.headers['x-user-id'] as string;
  const { email, password, fullName, role } = req.body;

  if (!['admin', 'landlord', 'tenant'].includes(role)) {
    return res.status(400).json({ error: 'Invalid role' });
  }

  try {
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({
      email,
      password,
      email_confirm: true,
    });

    if (authError) throw authError;

    const { data: user, error: userError } = await supabase
      .from('users')
      .insert({
        id: authData.user.id,
        email,
        full_name: fullName,
        role,
      })
      .select()
      .single();

    if (userError) throw userError;

    // Log admin action
    await supabase.from('admin_actions').insert({
      admin_id: adminId,
      action_type: 'user_created',
      target_user_id: user.id,
      notes: `Created new ${role}: ${email}`,
    });

    res.status(201).json(user);
  } catch (err) {
    res.status(400).json({ error: String(err) });
  }
});

// POST /api/admin/users/:id/suspend - Suspend a user
router.post('/users/:id/suspend', async (req, res) => {
  const adminId = req.headers['x-user-id'] as string;
  const { reason } = req.body;

  try {
    const { data, error } = await supabase
      .from('users')
      .update({
        is_suspended: true,
        suspension_reason: reason || 'Suspended by admin',
      })
      .eq('id', req.params.id)
      .select()
      .single();

    if (error) throw error;

    // Log admin action
    await supabase.from('admin_actions').insert({
      admin_id: adminId,
      action_type: 'user_suspended',
      target_user_id: req.params.id,
      notes: reason,
    });

    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/admin/users/:id/unsuspend - Unsuspend a user
router.post('/users/:id/unsuspend', async (req, res) => {
  const adminId = req.headers['x-user-id'] as string;

  try {
    const { data, error } = await supabase
      .from('users')
      .update({
        is_suspended: false,
        suspension_reason: null,
      })
      .eq('id', req.params.id)
      .select()
      .single();

    if (error) throw error;

    // Log admin action
    await supabase.from('admin_actions').insert({
      admin_id: adminId,
      action_type: 'user_suspended',
      target_user_id: req.params.id,
      notes: 'Unsuspended',
    });

    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/admin/disputes - List all payment disputes
router.get('/disputes', async (req, res) => {
  const { status } = req.query;

  try {
    let query = supabase
      .from('payment_disputes')
      .select('id, payment_id, tenant_id, reason, status, admin_notes, resolved_by, resolved_at, created_at, updated_at');

    if (status) {
      query = query.eq('status', status);
    }

    const { data, error } = await query.order('created_at', { ascending: false });

    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/admin/disputes/:id/resolve - Mark dispute as resolved
router.post('/disputes/:id/resolve', async (req, res) => {
  const adminId = req.headers['x-user-id'] as string;
  const { adminNotes, resolution } = req.body; // resolution: 'approved' or 'rejected'

  if (!['approved', 'rejected'].includes(resolution)) {
    return res.status(400).json({ error: 'Invalid resolution' });
  }

  try {
    const { data, error } = await supabase
      .from('payment_disputes')
      .update({
        status: resolution === 'approved' ? 'resolved' : 'rejected',
        admin_notes: adminNotes,
        resolved_by: adminId,
        resolved_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      })
      .eq('id', req.params.id)
      .select()
      .single();

    if (error) throw error;

    // Log admin action
    await supabase.from('admin_actions').insert({
      admin_id: adminId,
      action_type: 'payment_resolved',
      target_payment_id: data.payment_id,
      notes: `Dispute ${resolution}: ${adminNotes}`,
    });

    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/admin/reports/metrics - Get KPI metrics
router.get('/reports/metrics', async (req, res) => {
  try {
    // Total users by role
    const { data: userStats, error: userError } = await supabase
      .from('users')
      .select('role')
      .eq('is_suspended', false);

    if (userError) throw userError;

    const roleCount = (userStats || []).reduce(
      (acc: any, u: any) => {
        acc[u.role] = (acc[u.role] || 0) + 1;
        return acc;
      },
      { admin: 0, landlord: 0, tenant: 0 }
    );

    // MRR calculation
    const { data: paidPayments, error: paymentError } = await supabase
      .from('rent_payments')
      .select('amount, month')
      .eq('status', 'paid');

    if (paymentError) throw paymentError;

    // Group by month and sum
    const mrrTrend = (paidPayments || []).reduce((acc: any, p: any) => {
      const month = p.month.substring(0, 7); // YYYY-MM
      acc[month] = (acc[month] || 0) + Number(p.amount);
      return acc;
    }, {});

    // Occupancy stats
    const { data: units, error: unitError } = await supabase
      .from('units')
      .select('tenant_id');

    if (unitError) throw unitError;

    const totalUnits = (units || []).length;
    const occupiedUnits = (units || []).filter(u => u.tenant_id !== null).length;
    const occupancyRate = totalUnits > 0 ? Math.round((occupiedUnits / totalUnits) * 100) : 0;

    // Open support tickets (maintenance requests)
    const { data: openTickets, error: ticketError } = await supabase
      .from('maintenance_requests')
      .select('id')
      .in('status', ['open', 'assigned', 'in_progress']);

    if (ticketError) throw ticketError;

    res.json({
      userStats: roleCount,
      mrrTrend,
      occupancy: {
        occupied: occupiedUnits,
        total: totalUnits,
        rate: occupancyRate,
      },
      openTickets: (openTickets || []).length,
    });
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/admin/reports/churn - Get churn metrics
router.get('/reports/churn', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('leases')
      .select('end_date, tenant_id')
      .lt('end_date', new Date().toISOString())
      .order('end_date', { ascending: false })
      .limit(50);

    if (error) throw error;

    res.json({
      expiredLeases: (data || []).length,
      leases: data,
    });
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/admin/reports/payment-health - Payment collection health
router.get('/reports/payment-health', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('rent_payments')
      .select('status');

    if (error) throw error;

    const payments = data || [];
    const paid = payments.filter(p => p.status === 'paid').length;
    const pending = payments.filter(p => p.status === 'pending').length;
    const late = payments.filter(p => p.status === 'late').length;
    const total = payments.length;

    const health = {
      paid,
      pending,
      late,
      total,
      collectionRate: total > 0 ? Math.round((paid / total) * 100) : 0,
    };

    res.json(health);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

export default router;
