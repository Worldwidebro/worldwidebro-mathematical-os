# Quick Reference: classifyTask() Method

## Setup (2 minutes)

```bash
# 1. Install SDK
npm install @anthropic-ai/sdk

# 2. Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Import and use
import { OrchestratorPrime } from "./orchestrator-prime";
const orchestrator = new OrchestratorPrime();
```

## Usage Patterns

### Pattern 1: Basic Classification
```typescript
const task = {
  description: "Send cold emails to prospects",
  venture: "OPS-001"
};

const classification = await orchestrator["classifyTask"](task);

console.log(classification.intent);                    // "outreach"
console.log(classification.required_capabilities);    // ["write-emails", ...]
console.log(classification.autonomy_suggested);       // "L2"
```

### Pattern 2: Full Task with Context
```typescript
const task = {
  description: "Schedule discovery calls with qualified leads",
  venture: "LT-005",
  urgency: "high",
  budget: 500,
  revenue_target: 5000
};

const classification = await orchestrator["classifyTask"](task);
// Returns: intent, logic_layers, required_capabilities, autonomy_suggested
```

### Pattern 3: In Agent Matching
```typescript
async findBestAgent(task: Task): Promise<MatchResult[]> {
  const classification = await this.classifyTask(task);  // Claude Haiku
  const readyAgents = this.getReadyAgents();

  const scored = readyAgents.map((agent) => {
    let score = 0;
    
    // Match by intent
    if (classification.intent === agent.category) {
      score += 40;
    }
    
    // Match by capabilities
    classification.required_capabilities.forEach((cap) => {
      if (agent.description.includes(cap)) {
        score += 20;
      }
    });
    
    // Match by autonomy
    if (agent.autonomy_level === classification.autonomy_suggested) {
      score += 10;
    }
    
    return { agent_id: agent.id, confidence_score: score, ... };
  });
  
  return scored.sort((a, b) => b.confidence_score - a.confidence_score);
}
```

## Response Format

```typescript
interface TaskClassification {
  intent: string;                    // "outreach" | "sales" | "support" | ...
  logic_layers: string[];            // ["LL-009", "LL-010", ...]
  required_capabilities: string[];   // ["write-emails", "personalize", ...]
  autonomy_suggested: "L1" | "L2" | "L3";
}
```

## Examples & Expected Output

### Example 1: Outreach Email
```typescript
Input: {
  description: "Send cold emails to 20 prospects in Charlotte, NC",
  venture: "OPS-001",
  urgency: "high"
}

Output: {
  intent: "outreach",
  logic_layers: ["LL-009", "LL-010"],
  required_capabilities: ["write-emails", "personalize", "track-opens"],
  autonomy_suggested: "L2"
}
```

### Example 2: Sales Call Scheduling
```typescript
Input: {
  description: "Schedule discovery calls for qualified leads",
  venture: "LT-005"
}

Output: {
  intent: "sales",
  logic_layers: ["LL-011"],
  required_capabilities: ["schedule-meetings", "handle-objections"],
  autonomy_suggested: "L2"
}
```

### Example 3: Deal Closing
```typescript
Input: {
  description: "Close deal and send contract",
  venture: "RE-001",
  revenue_target: 50000
}

Output: {
  intent: "sales",
  logic_layers: ["LL-012"],
  required_capabilities: ["document-generation", "e-signature"],
  autonomy_suggested: "L2"
}
```

## Error Handling

### What Happens If API Fails?

```typescript
try {
  const classification = await orchestrator["classifyTask"](task);
  // If Claude Haiku API fails, automatically falls back to keyword matching
  return classification;  // Still returns valid TaskClassification
} catch (error) {
  // Method handles errors internally - this won't throw
}
```

### Fallback Behavior

```typescript
// If Claude Haiku unavailable, uses keyword matching:
- "email" in task → intent: "outreach"
- "call" in task → intent: "sales"
- "book" in task → intent: "booking"
- "analysis" in task → intent: "analysis"
- etc.
```

## Performance

| Operation | Latency | Cost |
|-----------|---------|------|
| First call | 200-500ms | $0.001 |
| Subsequent calls | 200-500ms | $0.001 each |
| 100 classifications | 20-50 sec | ~$0.10 |
| 1,000 classifications | 200-500 sec | ~$1.00 |

## Logging & Monitoring

### Success Log
```
✅ Task classified: intent="outreach", autonomy="L2"
```

### Fallback Log
```
⚠️  No text in Claude response, falling back to keyword matching
⚠️  Could not extract JSON from Claude response, falling back...
⚠️  Invalid classification structure from Claude, falling back...
```

### Error Log
```
❌ Failed to classify task with Claude: Timeout
❌ Failed to classify task with Claude: Invalid API key
```

## Configuration

### Environment Variables
```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...

# Optional (has defaults)
SUPABASE_URL=https://...supabase.co
SUPABASE_ANON_KEY=...
```

### Client Options (Currently Fixed)
```typescript
const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  // Model: claude-haiku-4-5-20251001 (hardcoded)
  // Max tokens: 256 (hardcoded)
  // System prompt: Custom (see implementation)
});
```

## Troubleshooting

### Problem: "Failed to classify task with Claude: 401"
**Cause**: Invalid or missing API key
**Fix**:
```bash
export ANTHROPIC_API_KEY=sk-ant-...  # Check key is correct
```

### Problem: "Could not extract JSON from Claude response"
**Cause**: Claude returned unexpected format
**Fix**: Check logs; falls back to keyword matching automatically

### Problem: Slow classification (>1000ms)
**Cause**: API latency or network issues
**Fix**: Normal for high-latency networks; consider batching

### Problem: High fallback rate (>10%)
**Cause**: API errors or rate limiting
**Fix**: 
- Check API key
- Check rate limits
- Check network connectivity
- Consider exponential backoff

## Cost Calculator

```typescript
// Monthly cost estimate
const tasksPerDay = 100;
const costPerTask = 0.001;
const daysPerMonth = 30;

const monthlyCost = tasksPerDay * costPerTask * daysPerMonth;
// Example: 100 tasks/day = $3/month
```

## Best Practices

### 1. Always Provide Venture
```typescript
// Good
{ description: "...", venture: "OPS-001" }

// Works but less context
{ description: "...", venture: "" }
```

### 2. Include Optional Fields When Available
```typescript
// Better (more context)
{
  description: "...",
  venture: "LT-005",
  urgency: "high",
  budget: 500
}

// Still works (but less optimized matching)
{
  description: "...",
  venture: "LT-005"
}
```

### 3. Cache Orchestrator Instance
```typescript
// Good - reuse client
const orchestrator = new OrchestratorPrime();
for (const task of tasks) {
  const result = await orchestrator.classifyTask(task);
}

// Inefficient - creates new client each time
for (const task of tasks) {
  const o = new OrchestratorPrime();
  const result = await o.classifyTask(task);
}
```

### 4. Handle Async Properly
```typescript
// Good - await
const classification = await orchestrator["classifyTask"](task);

// Error - forgot await
const classification = orchestrator["classifyTask"](task);
// Returns Promise, not classification!
```

## API Reference

### Method Signature
```typescript
async classifyTask(task: Task): Promise<TaskClassification>
```

### Task Interface
```typescript
interface Task {
  id?: string;                          // Optional unique ID
  description: string;                  // Required: task description
  venture: string;                      // Required: venture ID
  urgency?: "high" | "medium" | "low";  // Optional
  budget?: number;                      // Optional: USD
  revenue_target?: number;              // Optional: USD
}
```

### TaskClassification Interface
```typescript
interface TaskClassification {
  intent: string;                          // Action type
  logic_layers: string[];                  // Relevant layers
  required_capabilities: string[];         // Required skills
  autonomy_suggested: "L1" | "L2" | "L3";  // Recommended autonomy
}
```

## Integration Checklist

- [ ] Install `@anthropic-ai/sdk`
- [ ] Set `ANTHROPIC_API_KEY` env variable
- [ ] Import `OrchestratorPrime`
- [ ] Create instance: `new OrchestratorPrime()`
- [ ] Call `await classifyTask(task)`
- [ ] Use result for agent routing
- [ ] Monitor logs for errors/fallbacks
- [ ] Test with real tasks
- [ ] Add to CI/CD pipeline
- [ ] Monitor API costs

## Support

For issues or questions:
1. Check logs for error messages
2. Verify API key is set
3. Review test cases for expected behavior
4. See full documentation: `ORCHESTRATOR-PRIME-CLAUDE-HAIKU-IMPLEMENTATION.md`
