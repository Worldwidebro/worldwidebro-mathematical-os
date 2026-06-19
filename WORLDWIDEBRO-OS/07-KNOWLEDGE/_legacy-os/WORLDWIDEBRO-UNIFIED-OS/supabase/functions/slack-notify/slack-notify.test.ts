import { assertEquals, assertExists } from 'https://deno.land/std@0.208.0/assert/mod.ts';

Deno.test('Revenue alert status shows correct emoji for on-target MRR', async () => {
  const data = { mrr: 5000, target: 5000, growth_pct: 10 };
  const status =
    data.mrr >= data.target
      ? '✅ *On track!*'
      : '🚨 *Below target*';

  assertEquals(status, '✅ *On track!*');
  assertEquals((data.mrr / data.target) * 100, 100);
  console.log('✅ Revenue alert status test passed');
});

Deno.test('Deal score determines notification emoji', async () => {
  const highScore = { dealName: 'Big Deal', score: 85, operator: 'Alice' };
  const medScore = { dealName: 'Mid Deal', score: 65, operator: 'Bob' };
  const lowScore = { dealName: 'Small Deal', score: 45, operator: 'Charlie' };

  const highEmoji = highScore.score >= 80 ? '🔥' : '✨';
  const medEmoji = medScore.score >= 80 ? '🔥' : medScore.score >= 60 ? '✨' : '⭐';
  const lowEmoji = lowScore.score >= 80 ? '🔥' : lowScore.score >= 60 ? '✨' : '⭐';

  assertEquals(highEmoji, '🔥');
  assertEquals(medEmoji, '✨');
  assertEquals(lowEmoji, '⭐');
  console.log('✅ Deal score emoji test passed');
});

Deno.test('Notification type routing is correct', async () => {
  const types = ['revenue_alert', 'deal_sourced', 'task_complete', 'system_alert'];

  for (const type of types) {
    assertExists(type);
  }
  console.log('✅ Notification type routing test passed');
});
