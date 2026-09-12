-- LT-005 Charlotte Medical Facility Courier Automation
-- Tables for managing medical facility leads and outreach tracking

-- Table: lt005_charlotte_facilities
CREATE TABLE IF NOT EXISTS lt005_charlotte_facilities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  facility_type TEXT,
  address TEXT,
  city TEXT DEFAULT 'Charlotte',
  state TEXT DEFAULT 'NC',
  zip_code TEXT,
  contact_email TEXT,
  contact_phone TEXT,
  decision_maker_name TEXT,
  decision_maker_title TEXT,
  status TEXT DEFAULT 'not_contacted',
  contacted_at TIMESTAMPTZ,
  last_outreach_email TIMESTAMPTZ,
  last_outreach_call TIMESTAMPTZ,
  outreach_attempt INTEGER DEFAULT 0,
  booking_date TIMESTAMPTZ,
  booking_amount DECIMAL(10,2),
  revenue_logged BOOLEAN DEFAULT false,
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Table: lt005_outreach_log
CREATE TABLE IF NOT EXISTS lt005_outreach_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facility_id UUID REFERENCES lt005_charlotte_facilities(id) ON DELETE CASCADE,
  facility_name TEXT,
  email_sent_to TEXT,
  sent_at TIMESTAMPTZ,
  email_status TEXT,
  campaign TEXT,
  expected_revenue DECIMAL(10,2),
  response_status TEXT DEFAULT 'pending',
  response_date TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Table: lt005_bookings
CREATE TABLE IF NOT EXISTS lt005_bookings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facility_id UUID REFERENCES lt005_charlotte_facilities(id) ON DELETE CASCADE,
  facility_name TEXT,
  booking_date TIMESTAMPTZ,
  delivery_type TEXT,
  pickup_location TEXT,
  dropoff_location TEXT,
  amount DECIMAL(10,2),
  status TEXT DEFAULT 'pending',
  completed_at TIMESTAMPTZ,
  revenue_logged BOOLEAN DEFAULT false,
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_lt005_facilities_status ON lt005_charlotte_facilities(status);
CREATE INDEX IF NOT EXISTS idx_lt005_facilities_city ON lt005_charlotte_facilities(city);
CREATE INDEX IF NOT EXISTS idx_lt005_facilities_contacted ON lt005_charlotte_facilities(contacted_at);
CREATE INDEX IF NOT EXISTS idx_lt005_outreach_facility ON lt005_outreach_log(facility_id);
CREATE INDEX IF NOT EXISTS idx_lt005_outreach_sent_at ON lt005_outreach_log(sent_at);
CREATE INDEX IF NOT EXISTS idx_lt005_bookings_facility ON lt005_bookings(facility_id);
CREATE INDEX IF NOT EXISTS idx_lt005_bookings_status ON lt005_bookings(status);

-- Enable Row Level Security (optional but recommended)
ALTER TABLE lt005_charlotte_facilities ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_outreach_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_bookings ENABLE ROW LEVEL SECURITY;

-- Create RLS policies to allow authenticated users to access data
CREATE POLICY "Enable access for authenticated users" ON lt005_charlotte_facilities
  FOR SELECT USING (auth.role() = 'authenticated');

CREATE POLICY "Enable access for authenticated users" ON lt005_outreach_log
  FOR SELECT USING (auth.role() = 'authenticated');

CREATE POLICY "Enable access for authenticated users" ON lt005_bookings
  FOR SELECT USING (auth.role() = 'authenticated');
