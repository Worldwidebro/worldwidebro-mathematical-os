import dotenv from 'dotenv';
import { initNeo4j } from './db.js';
import { taskMemoryStore } from './memory/memory-store.js';
import { CapabilityEngine } from './capability/engine.js';
import { CapabilitiesRegistry } from './capability/capabilities-registry.js';

/**
 * Standalone integration verify script.
 * Run manually: tsx src/integration-check.ts
 * Or in CI after `npm run build`: node dist/integration-check.js
 */

dotenv.config();

interface CheckResult {
  name: string;
  pass: boolean;
  detail: string;
}

async function checkQdrant(): Promise<CheckResult> {
  try {
    const healthy = await taskMemoryStore.health();
    return { name: 'Qdrant connectivity', pass: healthy, detail: healthy ? 'reachable' : 'not responding' };
  } catch (err: any) {
    return { name: 'Qdrant connectivity', pass: false, detail: err.message };
  }
}

async function checkNeo4j(): Promise<CheckResult> {
  const driver = initNeo4j();
  try {
    await driver.verifyConnectivity();
    return { name: 'Neo4j connectivity', pass: true, detail: 'reachable' };
  } catch (err: any) {
    return { name: 'Neo4j connectivity', pass: false, detail: err.message };
  } finally {
    await driver.close();
  }
}

async function checkCapabilityRanking(): Promise<CheckResult> {
  try {
    const driver = initNeo4j();
    const registry = new CapabilitiesRegistry(driver);
    const engine = new CapabilityEngine(taskMemoryStore, registry);
    const ranked = await engine.rankCapabilities('analyze venture market');
    await driver.close();
    const pass = Array.isArray(ranked) && ranked.length > 0;
    return { name: 'Capability ranking', pass, detail: pass ? `${ranked.length} capabilities ranked` : 'empty result' };
  } catch (err: any) {
    return { name: 'Capability ranking', pass: false, detail: err.message };
  }
}

async function checkMemoryRoundTrip(): Promise<CheckResult> {
  try {
    if (!(await taskMemoryStore.health())) {
      return { name: 'Memory round-trip', pass: false, detail: 'skipped — Qdrant unreachable' };
    }
    const id = await taskMemoryStore.rememberTask({
      venture_id: 'integration-check',
      agent_id: 'integration-check',
      content: 'integration check probe task',
    });
    const results = await taskMemoryStore.findSimilarTasks({ content: 'integration check probe task', limit: 1 });
    await taskMemoryStore.forgetTask(id);
    const pass = results.some(r => r.id === id);
    return { name: 'Memory round-trip', pass, detail: pass ? 'remember + search + forget ok' : 'search did not return stored task' };
  } catch (err: any) {
    return { name: 'Memory round-trip', pass: false, detail: err.message };
  }
}

export async function main(): Promise<boolean> {
  // Initialize once up front — checks below run concurrently and both
  // checkCapabilityRanking and checkMemoryRoundTrip depend on this.
  if (await taskMemoryStore.health()) {
    await taskMemoryStore.initialize().catch(err => console.warn('TaskMemoryStore init warning:', err.message));
  }

  const results = await Promise.all([
    checkQdrant(),
    checkNeo4j(),
    checkCapabilityRanking(),
    checkMemoryRoundTrip(),
  ]);

  console.log('\n=== vex-api Integration Check ===\n');
  for (const r of results) {
    console.log(`${r.pass ? '✅' : '❌'} ${r.name}: ${r.detail}`);
  }

  const allPass = results.every(r => r.pass);
  console.log(`\n${allPass ? '✅ All checks passed' : '❌ Some checks failed'}\n`);
  return allPass;
}

// Run directly: `tsx src/integration-check.ts`
if (import.meta.url === `file://${process.argv[1]}`) {
  main()
    .then(pass => process.exit(pass ? 0 : 1))
    .catch(err => {
      console.error('Integration check crashed:', err);
      process.exit(1);
    });
}
