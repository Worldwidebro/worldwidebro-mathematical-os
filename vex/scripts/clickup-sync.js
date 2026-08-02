#!/usr/bin/env node

/**
 * ClickUp → Supabase Sync
 * Runs automatically via GitHub Actions every 15 minutes
 *
 * Syncs business data from ClickUp to Supabase.
 * You don't run this manually - it's automated.
 *
 * Data flow:
 * ClickUp (real-time ops) → Supabase (live DB) → Dashboards (live displays)
 */

const axios = require('axios');
const { createClient } = require('@supabase/supabase-js');

const CLICKUP_API = 'https://api.clickup.com/api/v2';
const CLICKUP_TOKEN = process.env.CLICKUP_API_KEY;

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

async function syncClickUpToSupabase() {
  console.log('🔄 Auto-sync: ClickUp → Supabase');

  try {
    // Target Accounts (prospects to call)
    console.log('  ├─ Syncing prospects...');
    await syncList('1000210000002320', 'clickup_prospects', 'prospect_id');

    // Client Job Orders (active jobs)
    console.log('  ├─ Syncing job orders...');
    await syncList('1000210000002235', 'clickup_job_orders', 'job_id');

    // Candidate Pipeline (recruitment funnel)
    console.log('  ├─ Syncing candidates...');
    await syncList('1000210000002236', 'clickup_candidates', 'candidate_id');

    // Placements & Billing (revenue)
    console.log('  └─ Syncing placements...');
    await syncList('1000210000002237', 'clickup_placements', 'placement_id');

    console.log('✅ Auto-sync complete\n');
    return { success: true, timestamp: new Date().toISOString() };

  } catch (error) {
    console.error('❌ Sync failed:', error.message);
    process.exit(1);
  }
}

async function syncList(listId, supabaseTable, idField) {
  try {
    const response = await axios.get(`${CLICKUP_API}/list/${listId}/task`, {
      headers: { Authorization: CLICKUP_TOKEN },
      params: { include_subtasks: true }
    });

    const items = response.data.tasks.map(task => ({
      [idField]: task.id,
      name: task.name,
      status: task.status?.status || 'Open',
      description: task.description || null,
      custom_fields: task.custom_fields || [],
      last_updated: new Date().toISOString()
    }));

    const { error } = await supabase
      .from(supabaseTable)
      .upsert(items, { onConflict: idField });

    if (error) throw error;
    console.log(`    ✓ ${items.length} records`);

  } catch (error) {
    console.error(`    ✗ Failed: ${error.message}`);
    throw error;
  }
}

// Auto-run
if (require.main === module) {
  syncClickUpToSupabase().catch(err => process.exit(1));
}

module.exports = { syncClickUpToSupabase };
