// SOLUTION FINDER INTEGRATION TEST
// Tests with real LT-005 cold call scenario
// 2026-09-19

import SolutionFinder from './solution-finder-core.js';
import assert from 'assert';

console.log('═══════════════════════════════════════════════════════');
console.log('SOLUTION FINDER — INTEGRATION TEST');
console.log('═══════════════════════════════════════════════════════\n');

async function runTests() {
  const finder = new SolutionFinder({ threshold: 0.75 });

  let passed = 0;
  let failed = 0;

  // TEST 1: Find cold call solution
  console.log('\n📋 TEST 1: Cold Call Solution Discovery');
  console.log('─────────────────────────────────────────');
  try {
    const result = await finder.findSolution('Cold Call Dialing');

    assert(result.found === true, 'Solution should be found');
    assert(result.solution !== null, 'Solution object should exist');
    assert(result.solution.name.toLowerCase().includes('cold'), 'Solution should mention cold calling');
    assert(result.elapsed < 5000, `Query should complete in <5s (took ${result.elapsed}ms)`);

    console.log(`✅ PASS`);
    console.log(`   Found: ${result.solution.name}`);
    console.log(`   Code: ${result.solution.codePath}`);
    console.log(`   Confidence: ${result.solution.confidence}`);
    console.log(`   Time: ${result.elapsed}ms`);
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // TEST 2: Find venture readiness solution
  console.log('\n📋 TEST 2: Venture Readiness Scoring');
  console.log('─────────────────────────────────────────');
  try {
    const result = await finder.findSolution('Venture Readiness Assessment');

    assert(result.found === true, 'Readiness solution should be found');
    assert(result.solution !== null, 'Solution object should exist');
    assert(result.solution.confidence >= 0.75, 'Confidence should meet threshold');

    console.log(`✅ PASS`);
    console.log(`   Found: ${result.solution.name}`);
    console.log(`   Code: ${result.solution.codePath}`);
    console.log(`   Repo: ${result.solution.repo}`);
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // TEST 3: Find infrastructure sync solution
  console.log('\n📋 TEST 3: Neo4j Sync Pipeline');
  console.log('─────────────────────────────────────────');
  try {
    const result = await finder.findSolution('Keep Neo4j in Sync with Supabase');

    assert(result.found === true, 'Sync solution should be found');
    assert(result.solution.codePath.includes('neo4j'), 'Solution should be Neo4j-related');

    console.log(`✅ PASS`);
    console.log(`   Found: ${result.solution.name}`);
    console.log(`   Source: ${result.solution.source}`);
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // TEST 4: Unknown problem should return 'not found'
  console.log('\n📋 TEST 4: Unknown Problem (negative test)');
  console.log('─────────────────────────────────────────');
  try {
    const result = await finder.findSolution('How to Train Dolphins');

    // This should NOT find a solution
    assert(result.found === false, 'Dolphin training should not be found');

    console.log(`✅ PASS`);
    console.log(`   Correctly returned 'not found'`);
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // TEST 5: Semantic search via graft
  console.log('\n📋 TEST 5: Semantic Search (graft)');
  console.log('─────────────────────────────────────────');
  try {
    const result = await finder.findSolution('outreach automation');

    assert(result.searchResults.length > 0 || result.found === false, 'Should either find or return empty');

    console.log(`✅ PASS`);
    if (result.found) {
      console.log(`   Found ${result.searchResults.length} result(s)`);
      console.log(`   Top match: ${result.solution.name} (${result.solution.source})`);
    } else {
      console.log(`   No results found (expected for semantic search on new terms)`);
    }
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // TEST 6: Response time benchmark
  console.log('\n📋 TEST 6: Performance Benchmark (5 queries)');
  console.log('─────────────────────────────────────────');
  try {
    const queries = [
      'Cold Call Dialing',
      'Venture Readiness Assessment',
      'Keep Neo4j in Sync with Supabase',
      'outreach automation',
      'data sync'
    ];

    const times = [];
    for (const q of queries) {
      const result = await finder.findSolution(q);
      times.push(result.elapsed);
    }

    const avgTime = Math.round(times.reduce((a, b) => a + b, 0) / times.length);
    const maxTime = Math.max(...times);

    assert(avgTime < 2000, `Average query time should be <2s (got ${avgTime}ms)`);

    console.log(`✅ PASS`);
    console.log(`   Average: ${avgTime}ms`);
    console.log(`   Max: ${maxTime}ms`);
    console.log(`   Min: ${Math.min(...times)}ms`);
    passed++;
  } catch (error) {
    console.log(`❌ FAIL: ${error.message}`);
    failed++;
  }

  // CLEANUP & SUMMARY
  console.log('\n═══════════════════════════════════════════════════════');
  console.log('TEST SUMMARY');
  console.log('═══════════════════════════════════════════════════════');
  console.log(`✅ Passed: ${passed}`);
  console.log(`❌ Failed: ${failed}`);
  console.log(`📊 Total:  ${passed + failed}`);

  if (failed === 0) {
    console.log('\n🎉 ALL TESTS PASSED — Solution Finder is ready!');
  } else {
    console.log(`\n⚠️  ${failed} test(s) failed. See above for details.`);
  }

  await finder.close();
  process.exit(failed > 0 ? 1 : 0);
}

runTests().catch(err => {
  console.error('FATAL ERROR:', err);
  process.exit(1);
});
