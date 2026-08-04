-- LT-005 Medical Courier Dispatch - Shared Civilization Tables
-- Schema: Generic tables used by LT-005 (and other LT ventures)
-- Note: Tables named generically; will specialize later as revenue scales

-- 1. CUSTOMERS (Pickup locations: hospitals, labs, clinics)
CREATE TABLE IF NOT EXISTS customers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  name TEXT NOT NULL,
  contact_email TEXT,
  contact_phone TEXT,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL,
  lat DECIMAL(10, 8),
  lng DECIMAL(11, 8),
  customer_type TEXT CHECK (customer_type IN ('hospital', 'lab', 'clinic', 'pharmacy', 'other')),
  billing_contact TEXT,
  contract_terms TEXT,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'pending')),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 2. DRIVERS (Employee couriers)
CREATE TABLE IF NOT EXISTS drivers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE,
  phone TEXT NOT NULL,
  license_number TEXT UNIQUE,
  license_state TEXT,
  license_expiry DATE,
  ssn_hash TEXT,
  background_check_status TEXT DEFAULT 'pending' CHECK (background_check_status IN ('pending', 'approved', 'rejected')),
  hipaa_certified BOOLEAN DEFAULT FALSE,
  hipaa_expiry DATE,
  bloodborne_certified BOOLEAN DEFAULT FALSE,
  bloodborne_expiry DATE,
  vehicle_id UUID REFERENCES vehicles(id),
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'on_break', 'suspended')),
  current_lat DECIMAL(10, 8),
  current_lng DECIMAL(11, 8),
  last_location_update TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 3. VEHICLES (Courier fleet)
CREATE TABLE IF NOT EXISTS vehicles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  vin TEXT UNIQUE NOT NULL,
  make TEXT NOT NULL,
  model TEXT NOT NULL,
  year INTEGER NOT NULL,
  license_plate TEXT UNIQUE NOT NULL,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'maintenance', 'retired')),
  temperature_controlled BOOLEAN DEFAULT FALSE,
  capacity_cubic_feet DECIMAL(8, 2),
  current_fuel_level DECIMAL(5, 2),
  mileage INTEGER,
  last_inspection DATE,
  inspection_expiry DATE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 4. PICKUPS (Service requests from customers)
CREATE TABLE IF NOT EXISTS pickups (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  customer_id UUID NOT NULL REFERENCES customers(id),
  pickup_type TEXT CHECK (pickup_type IN ('standard', 'stat', 'scheduled', 'recurring')) DEFAULT 'standard',
  specimen_type TEXT,
  pickup_address TEXT NOT NULL,
  pickup_city TEXT,
  pickup_state TEXT,
  pickup_zip TEXT,
  pickup_lat DECIMAL(10, 8),
  pickup_lng DECIMAL(11, 8),
  dropoff_address TEXT NOT NULL,
  dropoff_city TEXT,
  dropoff_state TEXT,
  dropoff_zip TEXT,
  dropoff_lat DECIMAL(10, 8),
  dropoff_lng DECIMAL(11, 8),
  pickup_time_window_start TIMESTAMP NOT NULL,
  pickup_time_window_end TIMESTAMP NOT NULL,
  special_instructions TEXT,
  chain_of_custody_required BOOLEAN DEFAULT TRUE,
  temperature_requirement TEXT CHECK (temperature_requirement IN ('ambient', 'refrigerated', 'frozen')) DEFAULT 'ambient',
  estimated_weight_kg DECIMAL(8, 2),
  hazmat_declared BOOLEAN DEFAULT FALSE,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'assigned', 'picked_up', 'in_transit', 'delivered', 'cancelled')),
  assigned_driver_id UUID REFERENCES drivers(id),
  assigned_route_id UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  scheduled_at TIMESTAMP,
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 5. ROUTES (Dispatch assignments + routing data)
CREATE TABLE IF NOT EXISTS routes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  driver_id UUID NOT NULL REFERENCES drivers(id),
  vehicle_id UUID REFERENCES vehicles(id),
  source_address TEXT NOT NULL,
  source_lat DECIMAL(10, 8),
  source_lng DECIMAL(11, 8),
  destination_address TEXT NOT NULL,
  destination_lat DECIMAL(10, 8),
  destination_lng DECIMAL(11, 8),
  distance_miles DECIMAL(8, 2),
  eta_minutes INTEGER,
  actual_duration_minutes INTEGER,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled')),
  polyline TEXT,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 6. DISPATCH ASSIGNMENTS (Real-time job assignments)
CREATE TABLE IF NOT EXISTS dispatch_assignments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  pickup_id UUID NOT NULL REFERENCES pickups(id),
  driver_id UUID NOT NULL REFERENCES drivers(id),
  vehicle_id UUID REFERENCES vehicles(id),
  route_id UUID REFERENCES routes(id),
  assignment_status TEXT DEFAULT 'assigned' CHECK (assignment_status IN ('assigned', 'accepted', 'declined', 'completed')),
  driver_response_time TIMESTAMP,
  assignment_time TIMESTAMP DEFAULT NOW(),
  completion_time TIMESTAMP,
  notes TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 7. TRACKING (GPS + real-time location updates)
CREATE TABLE IF NOT EXISTS tracking (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  driver_id UUID NOT NULL REFERENCES drivers(id),
  dispatch_assignment_id UUID REFERENCES dispatch_assignments(id),
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  heading DECIMAL(5, 2),
  speed_mph DECIMAL(5, 2),
  accuracy_meters DECIMAL(8, 2),
  timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 8. INVOICES (Billing records)
CREATE TABLE IF NOT EXISTS invoices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  customer_id UUID NOT NULL REFERENCES customers(id),
  invoice_number TEXT UNIQUE NOT NULL,
  invoice_date DATE NOT NULL,
  due_date DATE,
  subtotal DECIMAL(10, 2) NOT NULL,
  tax_amount DECIMAL(10, 2) DEFAULT 0,
  total_amount DECIMAL(10, 2) NOT NULL,
  status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'sent', 'viewed', 'paid', 'overdue', 'cancelled')),
  payment_method TEXT,
  payment_date TIMESTAMP,
  notes TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 9. INVOICE ITEMS (Line items for invoices)
CREATE TABLE IF NOT EXISTS invoice_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  invoice_id UUID NOT NULL REFERENCES invoices(id) ON DELETE CASCADE,
  pickup_id UUID REFERENCES pickups(id),
  description TEXT NOT NULL,
  quantity INTEGER DEFAULT 1,
  unit_price DECIMAL(10, 2) NOT NULL,
  line_total DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- 10. CERTIFICATIONS (Compliance tracking)
CREATE TABLE IF NOT EXISTS certifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  driver_id UUID NOT NULL REFERENCES drivers(id),
  cert_type TEXT NOT NULL CHECK (cert_type IN ('hipaa', 'bloodborne', 'specimen_handling', 'defensive_driving', 'background_check')),
  cert_name TEXT NOT NULL,
  issuer TEXT,
  issue_date DATE NOT NULL,
  expiry_date DATE,
  cert_number TEXT,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'expired', 'revoked')),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 11. COMPLIANCE_LOGS (Audit trail)
CREATE TABLE IF NOT EXISTS compliance_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL DEFAULT 'LT-005',
  pickup_id UUID REFERENCES pickups(id),
  driver_id UUID REFERENCES drivers(id),
  log_type TEXT NOT NULL CHECK (log_type IN ('chain_of_custody', 'temperature_violation', 'incident', 'audit')),
  details TEXT,
  severity TEXT CHECK (severity IN ('info', 'warning', 'critical')) DEFAULT 'info',
  created_at TIMESTAMP DEFAULT NOW()
);

-- INDEXES for performance
CREATE INDEX idx_customers_venture ON customers(venture_id);
CREATE INDEX idx_drivers_venture ON drivers(venture_id);
CREATE INDEX idx_pickups_venture ON pickups(venture_id);
CREATE INDEX idx_pickups_customer ON pickups(customer_id);
CREATE INDEX idx_pickups_driver ON pickups(assigned_driver_id);
CREATE INDEX idx_pickups_status ON pickups(status);
CREATE INDEX idx_routes_venture ON routes(venture_id);
CREATE INDEX idx_routes_driver ON routes(driver_id);
CREATE INDEX idx_dispatch_venture ON dispatch_assignments(venture_id);
CREATE INDEX idx_dispatch_pickup ON dispatch_assignments(pickup_id);
CREATE INDEX idx_dispatch_driver ON dispatch_assignments(driver_id);
CREATE INDEX idx_tracking_driver ON tracking(driver_id);
CREATE INDEX idx_tracking_timestamp ON tracking(timestamp);
CREATE INDEX idx_invoices_venture ON invoices(venture_id);
CREATE INDEX idx_invoices_customer ON invoices(customer_id);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_certifications_driver ON certifications(driver_id);
CREATE INDEX idx_compliance_logs_venture ON compliance_logs(venture_id);

-- TRIGGERS for updated_at timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER customers_updated_at BEFORE UPDATE ON customers FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER drivers_updated_at BEFORE UPDATE ON drivers FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER pickups_updated_at BEFORE UPDATE ON pickups FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER routes_updated_at BEFORE UPDATE ON routes FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER invoices_updated_at BEFORE UPDATE ON invoices FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER certifications_updated_at BEFORE UPDATE ON certifications FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
