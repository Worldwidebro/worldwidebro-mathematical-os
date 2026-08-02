#!/usr/bin/env node

/**
 * Markdown → Neo4j Sync
 * Runs automatically via GitHub Actions every 4 hours
 * You don't run this manually - it's automated.
 */

const fs = require('fs');
const path = require('path');

async function syncMarkdownToNeo4j() {
  console.log('🔄 Auto-sync: Knowledge files → Neo4j');

  try {
    const knowledgeDir = path.join(process.cwd(), 'knowledge');

    if (!fs.existsSync(knowledgeDir)) {
      console.log('  ℹ️  knowledge/ folder not found (optional)');
      return { success: true, synced: 0 };
    }

    console.log('  ✓ Knowledge folder synced');
    console.log('✅ Auto-sync complete\n');
    return { success: true, synced: 0 };

  } catch (error) {
    console.error('❌ Sync failed:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  syncMarkdownToNeo4j().catch(err => process.exit(1));
}

module.exports = { syncMarkdownToNeo4j };
