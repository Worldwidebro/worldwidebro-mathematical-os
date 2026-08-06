import neo4j from 'neo4j-driver';
import { createClient } from '@supabase/supabase-js';

export function initNeo4j() {
  const driver = neo4j.driver(
    process.env.NEO4J_URI || 'bolt://localhost:7687',
    neo4j.auth.basic(
      process.env.NEO4J_USER || 'neo4j',
      process.env.NEO4J_PASSWORD || 'ventures2026'
    )
  );
  return driver;
}

export function initSupabase() {
  return createClient(
    process.env.SUPABASE_URL || 'https://cyhzilqldouzgynacqpe.supabase.co',
    process.env.SUPABASE_ANON_KEY || ''
  );
}

// Named export for neoDriver which is imported by matching.ts and other endpoints
export const neoDriver = initNeo4j();
