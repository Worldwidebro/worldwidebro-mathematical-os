-- Roadrunner Cannabis Delivery Platform - Database Schema

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  full_name VARCHAR(255) NOT NULL,
  delivery_addresses TEXT[],
  age_verified BOOLEAN DEFAULT FALSE,
  verified_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Products table
CREATE TABLE IF NOT EXISTS products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  category VARCHAR(50) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  description TEXT,
  thc_percentage DECIMAL(5, 2),
  cbd_percentage DECIMAL(5, 2),
  emoji VARCHAR(5),
  stock INT DEFAULT 0,
  reorder_point INT DEFAULT 50,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_number VARCHAR(50) UNIQUE NOT NULL,
  customer_id UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
  driver_id UUID REFERENCES drivers(id),
  items JSONB NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  delivery_address TEXT NOT NULL,
  phone VARCHAR(20) NOT NULL,
  status VARCHAR(50) DEFAULT 'pending',
  proof_of_delivery TEXT,
  completed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  date DATE DEFAULT CURRENT_DATE
);

-- Drivers table
CREATE TABLE IF NOT EXISTS drivers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  vehicle_type VARCHAR(100),
  license_number VARCHAR(100) UNIQUE NOT NULL,
  verified BOOLEAN DEFAULT FALSE,
  active BOOLEAN DEFAULT FALSE,
  online BOOLEAN DEFAULT FALSE,
  total_deliveries INT DEFAULT 0,
  completed_deliveries INT DEFAULT 0,
  rating DECIMAL(3, 1) DEFAULT 5.0,
  earnings_today DECIMAL(10, 2) DEFAULT 0,
  total_earnings DECIMAL(12, 2) DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Inventory table
CREATE TABLE IF NOT EXISTS inventory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  quantity INT NOT NULL,
  warehouse_location VARCHAR(100),
  last_restock TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Compliance logs table
CREATE TABLE IF NOT EXISTS audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  action VARCHAR(100) NOT NULL,
  order_id UUID REFERENCES orders(id),
  driver_id UUID REFERENCES drivers(id),
  customer_id UUID REFERENCES customers(id),
  id_type VARCHAR(50),
  details JSONB,
  timestamp TIMESTAMP DEFAULT NOW()
);

-- Payment records table
CREATE TABLE IF NOT EXISTS payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  customer_id UUID NOT NULL REFERENCES customers(id),
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50),
  status VARCHAR(50) DEFAULT 'pending',
  stripe_payment_id VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes for performance
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_driver_id ON orders(driver_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_date ON orders(date);
CREATE INDEX idx_drivers_online ON drivers(online);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(timestamp);
CREATE INDEX idx_audit_logs_customer_id ON audit_logs(customer_id);

-- Enable Row Level Security
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE drivers ENABLE ROW LEVEL SECURITY;

-- Sample data
INSERT INTO products (name, category, price, description, thc_percentage, emoji, stock) VALUES
  ('OG Kush', 'flower', 45.00, 'Classic strain - 28% THC', 28, '🌿', 247),
  ('Sour Diesel', 'flower', 50.00, 'Energetic - 24% THC', 24, '🌿', 89),
  ('Gummy Pack', 'edibles', 35.00, '10mg THC each - 10 count', 10, '🍬', 342),
  ('Chocolate Bar', 'edibles', 28.00, '100mg THC total', 100, '🍫', 156),
  ('Live Resin', 'concentrates', 65.00, 'Premium concentrate - 85% THC', 85, '💎', 52),
  ('Wellness Oil', 'wellness', 55.00, 'CBD dominant - 0.3% THC', 0.3, '🧴', 198)
ON CONFLICT DO NOTHING;
