import express from 'express';
import { supabase } from '../index';

const router = express.Router();

// POST /api/maintenance - tenant creates maintenance request
router.post('/', async (req, res) => {
  const tenantId = req.headers['x-user-id'] as string;
  const { propertyId, description, photoUrl } = req.body;

  try {
    const { data, error } = await supabase
      .from('maintenance_requests')
      .insert({
        property_id: propertyId,
        tenant_id: tenantId,
        description,
        photo_url: photoUrl,
        status: 'open',
      })
      .select();

    if (error) throw error;
    res.status(201).json(data[0]);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/maintenance - list requests (landlord/tenant)
router.get('/', async (req, res) => {
  const { propertyId } = req.query;

  try {
    const { data, error } = await supabase
      .from('maintenance_requests')
      .select('*')
      .eq('property_id', propertyId);

    if (error) throw error;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// PUT /api/maintenance/:id - update request status
router.put('/:id', async (req, res) => {
  const { status, assignedTo, completedDate } = req.body;

  try {
    const { data, error } = await supabase
      .from('maintenance_requests')
      .update({ status, assigned_to: assignedTo, completed_date: completedDate })
      .eq('id', req.params.id)
      .select();

    if (error) throw error;
    res.json(data[0]);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

export default router;
