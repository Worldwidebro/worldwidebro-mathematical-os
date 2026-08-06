import { db } from './db';

async function check() {
  console.log("Testing live Supabase connection...");
  try {
    const { data, error } = await db.from('loads').select('*').limit(1);
    if (error) {
      console.log("❌ Query failed. Tables likely do not exist yet. Error:", error.message);
    } else {
      console.log("✅ Query succeeded! Connection is working. Found loads:", data.length);
    }
  } catch (err: any) {
    console.error("❌ Connection failed with unhandled exception:", err.message);
  }
}

check();
