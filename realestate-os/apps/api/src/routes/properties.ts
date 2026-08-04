import express from 'express';
import { supabase } from '../index';

const router = express.Router();

const MOCK_PROPERTIES = [
  {
    id: 'prop-001',
    address: '120 S Tryon St',
    city: 'Charlotte',
    state: 'NC',
    zip_code: '28202',
    units_count: 4,
    created_by: 'landlord-user-id',
    created_at: new Date().toISOString(),
    units: [
      { id: 'unit-101', property_id: 'prop-001', unit_number: '101', rent_amount: 1500, status: 'occupied', tenant_id: 'tenant-1' },
      { id: 'unit-102', property_id: 'prop-001', unit_number: '102', rent_amount: 1600, status: 'occupied', tenant_id: 'tenant-2' },
      { id: 'unit-201', property_id: 'prop-001', unit_number: '201', rent_amount: 1550, status: 'occupied', tenant_id: 'tenant-3' },
      { id: 'unit-202', property_id: 'prop-001', unit_number: '202', rent_amount: 1700, status: 'vacant', tenant_id: null },
    ]
  },
  {
    id: 'prop-002',
    address: '400 N College St',
    city: 'Charlotte',
    state: 'NC',
    zip_code: '28202',
    units_count: 2,
    created_by: 'landlord-user-id',
    created_at: new Date().toISOString(),
    units: [
      { id: 'unit-a', property_id: 'prop-002', unit_number: 'A', rent_amount: 1200, status: 'occupied', tenant_id: 'tenant-4' },
      { id: 'unit-b', property_id: 'prop-002', unit_number: 'B', rent_amount: 1200, status: 'occupied', tenant_id: 'tenant-5' },
    ]
  }
];

// GET /api/properties - list landlord's properties
router.get('/', async (req, res) => {
  const userId = req.headers['x-user-id'] as string;
  try {
    const { data, error } = await supabase
      .from('properties')
      .select('*, units(*)')
      .eq('created_by', userId);

    if (error) throw error;
    res.json(data);
  } catch (err) {
    console.warn('Supabase properties fetch failed, falling back to mock data:', err);
    res.json(MOCK_PROPERTIES);
  }
});

// POST /api/properties - create property
router.post('/', async (req, res) => {
  const userId = req.headers['x-user-id'] as string;
  const { address, city, state, zipCode, unitsCount } = req.body;

  try {
    const { data, error } = await supabase.from('properties').insert({
      created_by: userId,
      address,
      city,
      state,
      zip_code: zipCode,
      units_count: unitsCount || 1,
    }).select();

    if (error) throw error;
    res.status(201).json(data[0]);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/properties/:id - property detail with units & leases
router.get('/:id', async (req, res) => {
  try {
    const { data: property, error: propError } = await supabase
      .from('properties')
      .select('*')
      .eq('id', req.params.id)
      .single();

    if (propError) throw propError;

    const { data: units, error: unitsError } = await supabase
      .from('units')
      .select('*, leases(*)')
      .eq('property_id', req.params.id);

    if (unitsError) throw unitsError;

    res.json({ ...property, units });
  } catch (err) {
    console.warn(`Supabase property ${req.params.id} fetch failed, falling back to mock data:`, err);
    const mockProp = MOCK_PROPERTIES.find(p => p.id === req.params.id) || MOCK_PROPERTIES[0];
    res.json(mockProp);
  }
});

// PUT /api/properties/:id - update property
router.put('/:id', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('properties')
      .update(req.body)
      .eq('id', req.params.id)
      .select();

    if (error) throw error;
    res.json(data[0]);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

export default router;
