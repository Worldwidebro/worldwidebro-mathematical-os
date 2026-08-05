-- Initial Database Migration for DispatchOS (LT-011)
-- Targets: PostgreSQL / Supabase Engine

-- 1. Base Core Directories
CREATE TABLE IF NOT EXISTS brokers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  dot_number TEXT UNIQUE,
  credit_score INT CHECK (credit_score BETWEEN 300 AND 850),
  contact_email TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS carriers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  mc_number TEXT UNIQUE,
  dot_number TEXT UNIQUE,
  insurance_expiry DATE NOT NULL,
  status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'SUSPENDED', 'PENDING_ONBOARD')),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS drivers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  phone_number TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  license_number TEXT UNIQUE NOT NULL,
  status TEXT NOT NULL DEFAULT 'OFF_DUTY' CHECK (status IN ('ACTIVE_SHIFT', 'OFF_DUTY', 'ON_BREAK')),
  carrier_id UUID REFERENCES carriers(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS vehicles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  unit_number TEXT NOT NULL,
  plate_number TEXT UNIQUE NOT NULL,
  vin TEXT UNIQUE NOT NULL,
  equipment_type TEXT NOT NULL, -- e.g., 'Dry Van', 'Reefer', 'Flatbed'
  status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'MAINTENANCE', 'OUT_OF_SERVICE')),
  carrier_id UUID REFERENCES carriers(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Freight & Logistics Management
CREATE TABLE IF NOT EXISTS loads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  reference_number TEXT UNIQUE NOT NULL,
  status TEXT NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT', 'TENDERED', 'ASSIGNED', 'DISPATCHED', 'IN_TRANSIT', 'DELIVERED', 'INVOICED', 'SETTLED', 'CANCELED')),
  origin JSONB NOT NULL, -- { address, lat, lng, contact_phone, scheduled_pickup_window }
  destination JSONB NOT NULL, -- { address, lat, lng, contact_phone, scheduled_delivery_window }
  weight_lbs NUMERIC(10, 2) NOT NULL,
  dimensions JSONB, -- { length_in, width_in, height_in }
  hazmat BOOLEAN DEFAULT false,
  carrier_id UUID REFERENCES carriers(id) ON DELETE SET NULL,
  driver_id UUID REFERENCES drivers(id) ON DELETE SET NULL,
  vehicle_id UUID REFERENCES vehicles(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS rate_confirmations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  broker_id UUID REFERENCES brokers(id) ON DELETE SET NULL,
  base_rate_usd NUMERIC(10, 2) NOT NULL CHECK (base_rate_usd >= 0.00),
  fuel_surcharge_usd NUMERIC(10, 2) DEFAULT 0.00 CHECK (fuel_surcharge_usd >= 0.00),
  detention_hourly_usd NUMERIC(10, 2) DEFAULT 0.00,
  layover_flat_usd NUMERIC(10, 2) DEFAULT 0.00,
  pdf_url TEXT,
  verified BOOLEAN DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tenders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  carrier_id UUID REFERENCES carriers(id) ON DELETE CASCADE,
  offer_price_usd NUMERIC(10, 2) NOT NULL,
  status TEXT DEFAULT 'SENT' CHECK (status IN ('SENT', 'ACCEPTED', 'REJECTED', 'EXPIRED')),
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Document Verification
CREATE TABLE IF NOT EXISTS shipment_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  doc_type TEXT NOT NULL CHECK (doc_type IN ('BOL', 'POD', 'LUMPER_RECEIPT', 'WEIGHT_TICKET')),
  file_url TEXT NOT NULL,
  ocr_extracted_text JSONB,
  signature_present BOOLEAN DEFAULT false,
  signed_by TEXT,
  signed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 4. Live Telemetry
CREATE TABLE IF NOT EXISTS gps_telemetry_logs (
  id BIGSERIAL PRIMARY KEY,
  driver_id UUID REFERENCES drivers(id) ON DELETE CASCADE,
  vehicle_id UUID REFERENCES vehicles(id) ON DELETE CASCADE,
  latitude NUMERIC(9, 6) NOT NULL,
  longitude NUMERIC(9, 6) NOT NULL,
  speed_mph NUMERIC(5, 2),
  recorded_at TIMESTAMPTZ DEFAULT now()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_loads_status ON loads(status);
CREATE INDEX IF NOT EXISTS idx_loads_ref ON loads(reference_number);
CREATE INDEX IF NOT EXISTS idx_gps_driver_time ON gps_telemetry_logs(driver_id, recorded_at DESC);
CREATE INDEX IF NOT EXISTS idx_tenders_load ON tenders(load_id);
