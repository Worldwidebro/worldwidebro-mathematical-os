/**
 * Dispatch Router Integration Tests
 * Task 2.3: End-to-end testing across 10 Oct Tier 1 agents
 *
 * Test coverage:
 * - Phase 2.3a: Happy path (10 agents)
 * - Phase 2.3b: Failure modes (10 edge cases)
 * - Phase 2.3c: Performance (latency, throughput, memory)
 * - Phase 2.3d: Agent accuracy matrix
 */

import { expect } from 'chai';
import { DispatchRouter } from '../_MCP/AGENT_DISPATCH_ROUTER';
import { DispatcherIntegration } from '../_MCP/DISPATCH_ROUTER_INTEGRATION';

describe('DISPATCH ROUTER TESTS', () => {
  let dispatcher: DispatcherIntegration;
  let router: DispatchRouter;

  before(async () => {
    dispatcher = new DispatcherIntegration();
    router = dispatcher.getRouter();
    await dispatcher.connect();
  });

  after(async () => {
    await dispatcher.disconnect();
  });

  // ============================================================
  // PHASE 2.3a: HAPPY PATH TESTING (10 AGENTS)
  // ============================================================

  describe('Phase 2.3a: Happy Path (10 Oct Tier 1 Agents)', () => {
    const testCases = [
      {
        agent: 'Lead Qualifier',
        task: 'Score 100 inbound leads 1-100',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L2',
        expectedCost: 50,
      },
      {
        agent: 'Cold Email Writer',
        task: 'Write 50 personalized cold emails to prospects',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L2',
        expectedCost: 25,
      },
      {
        agent: 'Discovery Caller',
        task: 'Qualify 20 hot prospects over phone',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L1',
        expectedCost: 100,
      },
      {
        agent: 'Proposal Generator',
        task: 'Create customized proposals for 5 deals',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L2',
        expectedCost: 75,
      },
      {
        agent: 'Contract Reviewer',
        task: 'Flag risky contract terms in 10 agreements',
        expectedRank: 1,
        expectedDomain: '32-SECURITY',
        expectedAutonomy: 'L1',
        expectedCost: 150,
      },
      {
        agent: 'Invoice Tracker',
        task: 'Track unpaid invoices over 30 days',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L2',
        expectedCost: 25,
      },
      {
        agent: 'Support Ticket Router',
        task: 'Route 50 support tickets to right team',
        expectedRank: 1,
        expectedDomain: '05-OPERATIONS',
        expectedAutonomy: 'L2',
        expectedCost: 40,
      },
      {
        agent: 'Complaint Handler',
        task: 'Resolve 10 customer complaints escalated from support',
        expectedRank: 1,
        expectedDomain: '05-OPERATIONS',
        expectedAutonomy: 'L2',
        expectedCost: 60,
      },
      {
        agent: 'Pricing Optimizer',
        task: 'Optimize pricing for top 20 product SKUs',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L1',
        expectedCost: 200,
      },
      {
        agent: 'Revenue Forecaster',
        task: 'Predict Q4 revenue with confidence intervals',
        expectedRank: 1,
        expectedDomain: '30-REVENUE',
        expectedAutonomy: 'L1',
        expectedCost: 100,
      },
    ];

    testCases.forEach((tc) => {
      it(`${tc.agent}: "${tc.task}"`, async () => {
        const suggestion = await router.suggestAgent(tc.task);

        expect(suggestion).to.exist;
        expect(suggestion.agents[0].name).to.equal(tc.agent);
        expect(suggestion.agents[0].rank).to.equal(tc.expectedRank);
        expect(suggestion.domain).to.equal(tc.expectedDomain);
        expect(suggestion.autonomy_level).to.equal(tc.expectedAutonomy);
        expect(suggestion.cost).to.equal(tc.expectedCost);
        expect(suggestion.confidence).to.be.gte(0.85);
      });
    });

    it('Pass threshold: 9/10 agents ranked correctly', async () => {
      let passed = 0;
      for (const tc of testCases) {
        try {
          const suggestion = await router.suggestAgent(tc.task);
          if (suggestion.agents[0].name === tc.agent && suggestion.agents[0].rank === 1) {
            passed++;
          }
        } catch (e) {
          // Count as failure
        }
      }
      expect(passed).to.be.gte(9);
    });
  });

  // ============================================================
  // PHASE 2.3b: FAILURE MODE TESTING (10 EDGE CASES)
  // ============================================================

  describe('Phase 2.3b: Failure Modes (10 Edge Cases)', () => {
    const edgeCases = [
      {
        name: 'Vague task',
        task: 'This is very unclear',
        expectedBehavior: 'graceful_error',
      },
      {
        name: 'Unknown domain',
        task: 'Do quantum computing for my startup',
        expectedBehavior: 'escalate_to_human',
      },
      {
        name: 'Conflicting requirements',
        task: 'Write email AND code a feature',
        expectedBehavior: 'multi_agent_workflow',
      },
      {
        name: 'Tool permission denied',
        task: 'Transfer $1M to vendor account',
        expectedBehavior: 'escalate_to_human',
      },
      {
        name: 'Rate limit exceeded',
        task: 'Send 500 emails today',
        expectedBehavior: 'flag_warning',
      },
      {
        name: 'Missing skill',
        task: 'Code a neural network in COBOL',
        expectedBehavior: 'identify_gap',
      },
      {
        name: 'Cost threshold exceeded',
        task: 'Hire McKinsey for consulting ($2M project)',
        expectedBehavior: 'flag_overages',
      },
      {
        name: 'Agent unavailable',
        task: 'Use deprecated-agent-v1 for this task',
        expectedBehavior: 'skip_use_next',
      },
      {
        name: 'Malformed input',
        task: '',
        expectedBehavior: 'handle_gracefully',
      },
      {
        name: 'Extremely long task',
        task: 'a'.repeat(10000),
        expectedBehavior: 'handle_gracefully',
      },
    ];

    edgeCases.forEach((ec) => {
      it(`Handles: ${ec.name}`, async () => {
        let handled = false;
        try {
          const suggestion = await router.suggestAgent(ec.task);
          handled = suggestion && (suggestion.error || suggestion.escalation || suggestion.agents);
        } catch (e) {
          handled = false;
        }

        expect(handled).to.be.true;
      });
    });

    it('Pass threshold: All 10 edge cases handled without crashes', async () => {
      let handled = 0;
      for (const ec of edgeCases) {
        try {
          await router.suggestAgent(ec.task);
          handled++;
        } catch (e) {
          // Count as unhandled
        }
      }
      expect(handled).to.equal(10);
    });
  });

  // ============================================================
  // PHASE 2.3c: PERFORMANCE TESTING (LATENCY, THROUGHPUT, MEMORY)
  // ============================================================

  describe('Phase 2.3c: Performance Testing', () => {
    it('Latency: p95 < 500ms', async () => {
      const results = [];
      for (let i = 0; i < 20; i++) {
        const start = Date.now();
        await router.suggestAgent('Write 50 cold emails');
        const latency = Date.now() - start;
        results.push(latency);
      }

      results.sort((a, b) => a - b);
      const p95 = results[Math.floor(results.length * 0.95)];
      expect(p95).to.be.lessThan(500);
    });

    it('Ranking deterministic: Same task → same top agent', async () => {
      const results = [];
      for (let i = 0; i < 10; i++) {
        const suggestion = await router.suggestAgent('Write 50 cold emails');
        results.push(suggestion.agents[0].name);
      }

      const allSame = results.every((r) => r === results[0]);
      expect(allSame).to.be.true;
    });

    it('Memory stable: No leaks under 100 concurrent requests', async () => {
      const memBefore = process.memoryUsage().heapUsed;

      const promises = [];
      for (let i = 0; i < 100; i++) {
        promises.push(router.suggestAgent('Write 50 cold emails'));
      }
      await Promise.all(promises);

      const memAfter = process.memoryUsage().heapUsed;
      const memDelta = memAfter - memBefore;
      const memDeltaMB = memDelta / (1024 * 1024);

      // Allow up to 50MB delta (reasonable for temporary state)
      expect(memDeltaMB).to.be.lessThan(50);
    });
  });

  // ============================================================
  // PHASE 2.3d: AGENT ACCURACY MATRIX
  // ============================================================

  describe('Phase 2.3d: Agent Accuracy Matrix', () => {
    const agents = [
      'Lead Qualifier',
      'Cold Email Writer',
      'Discovery Caller',
      'Proposal Generator',
      'Contract Reviewer',
      'Invoice Tracker',
      'Support Ticket Router',
      'Complaint Handler',
      'Pricing Optimizer',
      'Revenue Forecaster',
    ];

    const agentTasks = {
      'Lead Qualifier': 'Score 100 inbound leads',
      'Cold Email Writer': 'Write 50 personalized cold emails',
      'Discovery Caller': 'Qualify 20 hot prospects over phone',
      'Proposal Generator': 'Create customized proposals for 5 deals',
      'Contract Reviewer': 'Flag risky contract terms in 10 agreements',
      'Invoice Tracker': 'Track unpaid invoices over 30 days',
      'Support Ticket Router': 'Route 50 support tickets to right team',
      'Complaint Handler': 'Resolve 10 customer complaints',
      'Pricing Optimizer': 'Optimize pricing for 20 product SKUs',
      'Revenue Forecaster': 'Predict Q4 revenue with confidence intervals',
    };

    it('Accuracy matrix: All 10 agents ranked #1 for their tasks', async () => {
      const matrix: { [key: string]: number } = {};

      for (const agent of agents) {
        const task = agentTasks[agent];
        const suggestion = await router.suggestAgent(task);
        const rank = suggestion.agents.findIndex((a) => a.name === agent) + 1;
        matrix[agent] = rank;
      }

      const allRank1 = Object.values(matrix).every((rank) => rank === 1);
      expect(allRank1).to.be.true;
    });
  });
});
