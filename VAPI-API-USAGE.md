---
name: VAPI-API-USAGE
title: 'VAPI API: Programmatic Agent Deployment & Calling'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# VAPI API: Programmatic Agent Deployment & Calling

**Purpose:** Deploy agents and execute campaigns via API instead of dashboard  
**Use Case:** Automate agent setup, mass calling campaigns, call monitoring  
**Documentation:** https://api.vapi.ai/docs

---

## Setup

### 1. Get VAPI API Key
```
1. Go to vapi.ai dashboard
2. Settings → API Keys
3. Create new API key
4. Copy and save (you'll only see it once)
```

### 2. Add to Environment
```bash
# Add to .env
VAPI_API_KEY=sk_your_api_key_here
```

### 3. Import Integration
```javascript
const vapi = require('./vapi-api-integration');
```

---

## Core Functions

### Deploy Single Agent

```javascript
const config = {
  name: "Echo - E-Commerce Agent",
  model: {
    provider: "openai",
    model: "gpt-4",
    temperature: 0.7
  },
  voice: {
    provider: "openai",
    voiceId: "echo"
  },
  systemPrompt: "You are Echo, an AI sales agent...",
  phoneNumber: "+1-XXX-ECOM-001"
};

const agent = await vapi.deployAgent(config);
console.log(`Deployed with ID: ${agent.id}`);
```

### Deploy All Three Agents

```javascript
const allAgents = await vapi.deployAllAgents();

console.log(allAgents);
// Output:
// {
//   echo: { id: 'agent_123', name: 'Echo...', status: 'deployed' },
//   swift: { id: 'agent_456', name: 'Swift...', status: 'deployed' },
//   bella: { id: 'agent_789', name: 'Bella...', status: 'deployed' }
// }
```

### Make Outbound Call

```javascript
const agentId = 'agent_123';
const prospectPhone = '+1-704-561-1396';

const call = await vapi.makeOutboundCall(agentId, prospectPhone);

console.log(`Call initiated: ${call.id}`);
// Call starts immediately, prospect's phone rings
```

### Get Call Details & Transcript

```javascript
const callId = call.id;
const callDetails = await vapi.getCallDetails(callId);

console.log({
  duration: callDetails.duration, // seconds
  outcome: callDetails.outcome, // 'interested', 'not_interested', etc
  transcript: callDetails.transcript, // Full conversation
  recordingUrl: callDetails.recordingUrl // Audio file
});
```

### List Recent Calls

```javascript
const recentCalls = await vapi.listCalls({ 
  limit: 10, 
  order: 'desc' // Most recent first
});

recentCalls.forEach(call => {
  console.log(`${call.id}: ${call.status} - ${call.outcome}`);
});
```

---

## Campaign Execution

### Launch Mass Calling Campaign

```javascript
const agentId = 'agent_123'; // Echo agent
const prospects = [
  { name: 'John Smith', phoneNumber: '+1-704-561-1396' },
  { name: 'Jane Doe', phoneNumber: '+1-704-561-1397' },
  { name: 'Bob Wilson', phoneNumber: '+1-704-561-1398' },
  // ... more prospects
];

// Make 2 calls per minute (rate limited)
const campaignResults = await vapi.launchCampaign(
  agentId, 
  prospects, 
  2 // callsPerMinute
);

campaignResults.forEach(result => {
  console.log(`${result.prospect}: ${result.status}`);
});
```

### Monitor Calls Until Complete

```javascript
const callIds = campaignResults.map(r => r.callId);

// Polls every 5 seconds until all calls end
const completedCalls = await vapi.monitorCalls(callIds);

completedCalls.forEach((callId, data) => {
  console.log({
    callId: callId,
    duration: data.duration,
    outcome: data.outcome, // 'interested', 'not_interested', 'demo_booked', etc
    transcript: data.transcript.substring(0, 100) + '...'
  });
});
```

---

## Real-World Example: Weekly Campaign

```javascript
const vapi = require('./vapi-api-integration');
const { createClient } = require('@supabase/supabase-js');

async function runWeeklyCampaign() {
  console.log('Starting weekly E-Commerce campaign...\n');

  // 1. Get agent ID (could be stored in Supabase)
  const agents = await vapi.listAgents();
  const echoAgent = agents.find(a => a.name.includes('Echo'));
  
  if (!echoAgent) {
    console.error('Echo agent not found');
    return;
  }

  // 2. Get prospect list from ClickUp or database
  const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);
  const { data: prospects } = await supabase
    .from('prospects')
    .select('name, phone')
    .eq('sector', 'e-commerce')
    .eq('contacted_this_week', false)
    .limit(50);

  console.log(`Calling ${prospects.length} prospects...\n`);

  // 3. Launch campaign with rate limiting
  const callResults = await vapi.launchCampaign(echoAgent.id, prospects, 3);

  // 4. Wait for calls to complete
  const callIds = callResults.map(r => r.callId);
  console.log(`Waiting for ${callIds.length} calls to complete...\n`);

  const completedCalls = await vapi.monitorCalls(callIds);

  // 5. Log results to Supabase
  for (const [callId, callData] of Object.entries(completedCalls)) {
    const prospectIndex = callResults.findIndex(r => r.callId === callId);
    const prospect = prospects[prospectIndex];

    await supabase.from('ai_calls').insert({
      prospect_name: prospect.name,
      prospect_phone: prospect.phone,
      call_id: callId,
      duration: callData.duration,
      outcome: callData.outcome,
      transcript: callData.transcript,
      contacted_at: new Date()
    });

    console.log(`✓ ${prospect.name}: ${callData.outcome}`);
  }

  // 6. Report results
  const outcomes = Object.values(completedCalls).reduce((acc, call) => {
    acc[call.outcome] = (acc[call.outcome] || 0) + 1;
    return acc;
  }, {});

  console.log('\nWeekly Results:');
  console.log(`Total calls: ${callIds.length}`);
  console.log(`Interested: ${outcomes.interested || 0}`);
  console.log(`Demos booked: ${outcomes.demo_booked || 0}`);
  console.log(`Not interested: ${outcomes.not_interested || 0}`);
}

// Run weekly (e.g., Mondays at 9am)
runWeeklyCampaign().catch(console.error);
```

---

## API Endpoints Reference

### Core Endpoints

```
POST   /agents                    Create agent
GET    /agents                    List agents
GET    /agents/{id}               Get agent details
PATCH  /agents/{id}               Update agent
DELETE /agents/{id}               Delete agent

POST   /calls                     Make outbound call
GET    /calls                     List calls
GET    /calls/{id}                Get call details
POST   /calls/{id}/transfer       Transfer to human
```

### Request/Response Examples

#### Create Agent
```bash
curl -X POST https://api.vapi.ai/v1/agents \
  -H "Authorization: Bearer sk_your_api_key" \
  -H "Content-Type: application/json" \
  -d @vapi-agent-echo-config.json
```

Response:
```json
{
  "id": "agent_123abc",
  "name": "Echo - E-Commerce Agent",
  "phoneNumber": "+1-XXX-ECOM-001",
  "model": { ... },
  "createdAt": "2026-05-10T14:30:00Z"
}
```

#### Make Outbound Call
```bash
curl -X POST https://api.vapi.ai/v1/calls \
  -H "Authorization: Bearer sk_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "agent_123abc",
    "customerNumber": "+1-704-561-1396"
  }'
```

Response:
```json
{
  "id": "call_xyz789",
  "status": "queued",
  "agentId": "agent_123abc",
  "customerNumber": "+1-704-561-1396",
  "createdAt": "2026-05-10T14:35:00Z"
}
```

#### Get Call Details
```bash
curl https://api.vapi.ai/v1/calls/call_xyz789 \
  -H "Authorization: Bearer sk_your_api_key"
```

Response:
```json
{
  "id": "call_xyz789",
  "status": "ended",
  "duration": 540,
  "outcome": "interested",
  "transcript": "Hi, this is Echo... I'd like to book a demo... Perfect, Tuesday 2pm works?",
  "recordingUrl": "https://api.vapi.ai/recordings/...",
  "createdAt": "2026-05-10T14:35:00Z",
  "endedAt": "2026-05-10T14:44:00Z"
}
```

---

## Error Handling

```javascript
try {
  const call = await vapi.makeOutboundCall(agentId, phoneNumber);
} catch (error) {
  if (error.response?.status === 400) {
    console.error('Invalid phone number format');
  } else if (error.response?.status === 401) {
    console.error('Invalid API key');
  } else if (error.response?.status === 429) {
    console.error('Rate limited - slow down call rate');
  } else {
    console.error('Unexpected error:', error.message);
  }
}
```

---

## Rate Limiting

VAPI applies rate limits:
- **Default:** 100 calls/min per API key
- **Calls/campaign:** Recommended 2-5 calls/min to avoid overwhelming prospects
- **Headers:** Returns `X-RateLimit-Remaining` and `X-RateLimit-Reset`

```javascript
// Example: Respect rate limits
const maxCallsPerMinute = 3;
const delayMs = (60 * 1000) / maxCallsPerMinute; // 20 seconds between calls

for (let i = 0; i < prospects.length; i++) {
  await vapi.makeOutboundCall(agentId, prospects[i].phone);
  if (i < prospects.length - 1) {
    await new Promise(r => setTimeout(r, delayMs));
  }
}
```

---

## Integration with Webhook System

The webhook handler and API integration work together:

```
VAPI API Call
    ↓
[Phone rings, agent talks to prospect]
    ↓
Call completes
    ↓
VAPI sends POST to webhook: /webhook/call-complete
    ↓
Webhook handler logs to Supabase + creates ClickUp task
```

---

## Monitoring & Analytics

```javascript
// Track campaign performance
async function getCampaignStats(campaignName, since = null) {
  const calls = await vapi.listCalls({ limit: 100 });

  const stats = {
    total: calls.length,
    completed: calls.filter(c => c.status === 'ended').length,
    interested: calls.filter(c => c.outcome === 'interested').length,
    demos_booked: calls.filter(c => c.outcome === 'demo_booked').length,
    not_interested: calls.filter(c => c.outcome === 'not_interested').length,
    avg_duration: Math.round(
      calls.reduce((sum, c) => sum + (c.duration || 0), 0) / calls.length
    )
  };

  const bookingRate = (stats.demos_booked / stats.completed * 100).toFixed(1);
  
  console.log(`Campaign: ${campaignName}`);
  console.log(`Calls: ${stats.completed}/${stats.total}`);
  console.log(`Interested: ${stats.interested}`);
  console.log(`Demos Booked: ${stats.demos_booked} (${bookingRate}%)`);
  console.log(`Avg Duration: ${stats.avg_duration}s`);
  
  return stats;
}
```

---

## Summary

**API Integration File:** `vapi-api-integration.js`  
**Usage Guide:** This file (VAPI-API-USAGE.md)

Key functions:
- ✅ `deployAgent()` - Deploy agent
- ✅ `makeOutboundCall()` - Call prospect
- ✅ `getCallDetails()` - Get transcript & outcome
- ✅ `launchCampaign()` - Mass calling with rate limiting
- ✅ `monitorCalls()` - Wait for calls to complete

This enables **fully automated calling campaigns** without manual VAPI dashboard intervention.
