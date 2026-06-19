-- ============================================================================
-- BOOK PUBLISHING SYSTEM - SUPABASE SCHEMA
-- ============================================================================

CREATE TABLE IF NOT EXISTS books (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id UUID REFERENCES ventures(id),
  title VARCHAR NOT NULL,
  author VARCHAR NOT NULL,
  description TEXT,
  target_audience VARCHAR,
  status VARCHAR DEFAULT 'draft',
  current_version VARCHAR DEFAULT 'v1',
  created_date TIMESTAMP DEFAULT NOW(),
  v1_release_date DATE,
  revenue_goal DECIMAL
);

CREATE TABLE IF NOT EXISTS book_versions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  book_id UUID NOT NULL REFERENCES books(id),
  version VARCHAR NOT NULL,
  version_type VARCHAR NOT NULL,
  release_date DATE,
  price DECIMAL NOT NULL,
  file_url VARCHAR,
  status VARCHAR DEFAULT 'draft'
);

CREATE TABLE IF NOT EXISTS book_campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  book_id UUID NOT NULL REFERENCES books(id),
  campaign_name VARCHAR NOT NULL,
  launch_date DATE,
  budget DECIMAL,
  target_revenue DECIMAL,
  status VARCHAR DEFAULT 'planned',
  primary_channel VARCHAR,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS book_platforms (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  book_id UUID NOT NULL REFERENCES books(id),
  platform_name VARCHAR NOT NULL,
  url VARCHAR,
  price DECIMAL,
  live_date DATE,
  status VARCHAR DEFAULT 'active',
  estimated_margin DECIMAL,
  UNIQUE(book_id, platform_name)
);

CREATE TABLE IF NOT EXISTS book_revenue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  book_id UUID NOT NULL REFERENCES books(id),
  platform_name VARCHAR NOT NULL,
  date DATE NOT NULL,
  copies_sold INT DEFAULT 0,
  price DECIMAL,
  gross_revenue DECIMAL DEFAULT 0,
  net_revenue DECIMAL DEFAULT 0,
  UNIQUE(book_id, platform_name, date)
);

CREATE TABLE IF NOT EXISTS book_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  book_id UUID NOT NULL REFERENCES books(id),
  date DATE NOT NULL,
  page_views INT DEFAULT 0,
  clicks INT DEFAULT 0,
  conversions INT DEFAULT 0,
  email_opened INT DEFAULT 0,
  social_impressions INT DEFAULT 0,
  roas DECIMAL,
  UNIQUE(book_id, date)
);

CREATE VIEW books_monthly_revenue AS
SELECT
  b.id,
  b.title,
  DATE_TRUNC('month', br.date)::DATE as month,
  SUM(br.net_revenue) as monthly_revenue,
  SUM(br.copies_sold) as copies_sold
FROM books b
LEFT JOIN book_revenue br ON b.id = br.book_id
GROUP BY b.id, b.title, DATE_TRUNC('month', br.date);

CREATE INDEX idx_books_venture_id ON books(venture_id);
CREATE INDEX idx_book_revenue_date ON book_revenue(date);
