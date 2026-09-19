// SOLUTION FINDER EVALUATION HARNESS
// Measures precision, recall, and performance
// 2026-09-19

import SolutionFinder from '../_MCP/solution-finder-core.js';

console.log('═══════════════════════════════════════════════════════');
console.log('SOLUTION FINDER EVALUATION');
console.log('═══════════════════════════════════════════════════════\n');

const testCases = [
  {
    query: 'Cold Call Dialing',
    expectedSolution: 'Cold Call Automation',
    expectedRepo: 'LT-005',
    expectedConfidence: 0.85,
    importance: 'HIGH',
    description: 'Critical for revenue operations'
  },
  {
    query: 'Venture Readiness Assessment',
    expectedSolution: 'Venture Readiness Scoring',
    expectedRepo: 'CON-001',
    expectedConfidence: 0.80,
    importance: 'HIGH',
    description: 'Used across portfolio evaluation'
  },
  {
    query: 'Keep Neo4j in Sync with Supabase',
    expectedSolution: 'Supabase to Neo4j Sync',
    expectedRepo: 'VEX',
    expectedConfidence: 0.85,
    importance: 'HIGH',
    description: 'Foundation for graph consistency'
  },
  {
    query: 'outreach automation',
    expectedSolution: 'Cold Call Automation',
    expectedRepo: 'LT-005',
    expectedConfidence: 0.70,
    importance: 'MEDIUM',
    description: 'Semantic match for sales workflows'
  },
  {
    query: 'scoring ventures',
    expectedSolution: 'Venture Readiness Scoring',
    expectedRepo: 'CON-001',
    expectedConfidence: 0.70,
    importance: 'MEDIUM',
    description: 'Semantic match for evaluation'
  },
  {
    query: 'data integration',
    expectedSolution: 'Supabase to Neo4j Sync',
    expectedRepo: 'VEX',
    expectedConfidence: 0.65,
    importance: 'MEDIUM',
    description: 'Semantic match for pipelines'
  },
  {
    query: 'How to train dolphins',
    expectedSolution: null,
    expectedRepo: null,
    expectedConfidence: 0,
    importance: 'MEDIUM',
    description: 'Negative test - should not find'
  },
  {
    query: 'Deploy machine learning models',
    expectedSolution: null,
    expectedRepo: null,
    expectedConfidence: 0,
    importance: 'LOW',
    description: 'Out of domain - should not find'
  }
];

async function runEvaluation() {
  const finder = new SolutionFinder({ threshold: 0.65 });

  const results = {
    total: testCases.length,
    passed: 0,
    failed: 0,
    precision: 0,
    recall: 0,
    averageLatency: 0,
    testResults: []
  };

  const latencies = [];
  let correctPositives = 0;
  let totalPositives = 0;
  let foundPositives = 0;

  console.log('Running evaluation across 8 test cases...\n');

  for (let i = 0; i < testCases.length; i++) {
    const testCase = testCases[i];
    console.log(`\n[Test ${i + 1}/${testCases.length}] ${testCase.query}`);
    console.log(`  Expected: ${testCase.expectedSolution || 'NOT FOUND'}`);
    console.log(`  Importance: ${testCase.importance}`);

    try {
      const result = await finder.findSolution(testCase.query);
      latencies.push(result.elapsed);

      let testPassed = false;
      let feedback = '';

      if (testCase.expectedSolution === null) {
        // Negative test - should NOT find
        if (!result.found) {
          testPassed = true;
          feedback = '✅ Correctly returned NOT FOUND';
          console.log(`  ${feedback}`);
        } else {
          feedback = `❌ Should not have found "${result.solution.name}"`;
          console.log(`  ${feedback}`);
        }
      } else {
        // Positive test - should find expected solution
        if (result.found && result.solution) {
          const nameMatch = result.solution.name.toLowerCase().includes(
            testCase.expectedSolution.toLowerCase().split(' ')[0]
          );
          const repoMatch = result.solution.repo === testCase.expectedRepo;
          const confidenceOk = result.solution.confidence >= testCase.expectedConfidence - 0.15;

          if (nameMatch && confidenceOk) {
            testPassed = true;
            correctPositives++;
            foundPositives++;
            feedback = `✅ Found "${result.solution.name}" (conf: ${result.solution.confidence.toFixed(2)})`;
            console.log(`  ${feedback}`);
            if (!repoMatch) {
              console.log(`  ⚠️  Repo mismatch: expected ${testCase.expectedRepo}, got ${result.solution.repo}`);
            }
          } else {
            feedback = `⚠️  Partial match: "${result.solution.name}" (conf: ${result.solution.confidence.toFixed(2)})`;
            console.log(`  ${feedback}`);
            foundPositives++;
          }
        } else {
          feedback = `❌ Failed to find solution`;
          console.log(`  ${feedback}`);
        }
        totalPositives++;
      }

      results.testResults.push({
        query: testCase.query,
        expected: testCase.expectedSolution,
        passed: testPassed,
        feedback,
        latency: result.elapsed,
        importance: testCase.importance
      });

      if (testPassed) {
        results.passed++;
      } else {
        results.failed++;
      }

    } catch (error) {
      console.log(`  ❌ ERROR: ${error.message}`);
      results.failed++;
      results.testResults.push({
        query: testCase.query,
        expected: testCase.expectedSolution,
        passed: false,
        feedback: error.message,
        importance: testCase.importance
      });
    }
  }

  // Calculate metrics
  results.averageLatency = Math.round(latencies.reduce((a, b) => a + b, 0) / latencies.length);
  results.precision = totalPositives > 0 ? (correctPositives / foundPositives * 100).toFixed(1) : 0;
  results.recall = totalPositives > 0 ? (foundPositives / totalPositives * 100).toFixed(1) : 0;

  // Print summary
  console.log('\n═══════════════════════════════════════════════════════');
  console.log('EVALUATION SUMMARY');
  console.log('═══════════════════════════════════════════════════════');
  console.log(`✅ Passed: ${results.passed}/${results.total}`);
  console.log(`❌ Failed: ${results.failed}/${results.total}`);
  console.log(`📊 Precision: ${results.precision}%`);
  console.log(`📊 Recall: ${results.recall}%`);
  console.log(`⏱️  Average Latency: ${results.averageLatency}ms`);
  console.log(`🚀 Max Latency: ${Math.max(...latencies)}ms`);

  // Success criteria
  console.log('\n═══════════════════════════════════════════════════════');
  console.log('SUCCESS CRITERIA');
  console.log('═══════════════════════════════════════════════════════');

  const criteria = [
    { name: 'Pass Rate ≥ 75%', met: (results.passed / results.total * 100) >= 75 },
    { name: 'Precision ≥ 85%', met: parseFloat(results.precision) >= 85 },
    { name: 'Recall ≥ 80%', met: parseFloat(results.recall) >= 80 },
    { name: 'Avg Latency < 2s', met: results.averageLatency < 2000 }
  ];

  let allMet = true;
  for (const c of criteria) {
    const symbol = c.met ? '✅' : '❌';
    console.log(`${symbol} ${c.name}`);
    if (!c.met) allMet = false;
  }

  console.log('\n═══════════════════════════════════════════════════════');
  if (allMet) {
    console.log('🎉 EVALUATION PASSED — Solution Finder is production-ready!');
  } else {
    console.log('⚠️  Some criteria not met. See failures above.');
  }

  // Save results to file
  const resultsFile = '/Users/acebless/Documents/The Company/Company Brain/_EVAL/solution-finder-results.json';
  require('fs').writeFileSync(resultsFile, JSON.stringify(results, null, 2));
  console.log(`\n📄 Results saved to: ${resultsFile}`);

  await finder.close();
  process.exit(allMet ? 0 : 1);
}

runEvaluation().catch(err => {
  console.error('FATAL ERROR:', err);
  process.exit(1);
});
