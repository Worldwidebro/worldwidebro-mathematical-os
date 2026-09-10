-- PostgreSQL Encryption Setup
-- Generated: 2026-09-10T02:14:09Z
-- Purpose: Enable pgcrypto extension for contract encryption

-- Enable pgcrypto extension (required for AES encryption)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Verify installation
SELECT version() as postgres_version;
SELECT extname FROM pg_extension WHERE extname = 'pgcrypto';

-- Log encryption setup
-- This statement documents when encryption was enabled
DO $$
BEGIN
  RAISE NOTICE 'PostgreSQL encryption (pgcrypto) enabled at %', NOW();
END
$$;

