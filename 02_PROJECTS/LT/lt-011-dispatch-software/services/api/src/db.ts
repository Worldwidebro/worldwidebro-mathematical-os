import { createClient } from '@supabase/supabase-js';
import * as dotenv from 'dotenv';

dotenv.config();

const supabaseUrl = process.env.SUPABASE_URL || 'https://cyhzilqldouzgynacqpe.supabase.co';
const supabaseKey = process.env.SUPABASE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY || '';

if (!supabaseKey) {
  console.warn('⚠️ WARNING: SUPABASE_KEY/SUPABASE_SERVICE_ROLE_KEY is not defined. Database writes will fail.');
}

export const db = createClient(supabaseUrl, supabaseKey);
export default db;
