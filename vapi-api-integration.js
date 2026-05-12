// VAPI API Integration
// Programmatically deploy and manage agents via VAPI API instead of dashboard

const axios = require('axios');

const VAPI_API_KEY = process.env.VAPI_API_KEY;
const VAPI_BASE_URL = 'https://api.vapi.ai/v1';

const vapiClient = axios.create({
  baseURL: VAPI_BASE_URL,
  headers: {
    'Authorization': `Bearer ${VAPI_API_KEY}`,
    'Content-Type': 'application/json'
  }
});

/**
 * Deploy a voice agent to VAPI
 * @param {Object} agentConfig - Agent configuration object
 * @returns {Object} Agent response with ID
 */
async function deployAgent(agentConfig) {
  try {
    const response = await vapiClient.post('/agents', agentConfig);
    console.log(`Agent deployed: ${response.data.id}`);
    return response.data;
  } catch (error) {
    console.error('Failed to deploy agent:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Update existing agent configuration
 * @param {String} agentId - VAPI agent ID
 * @param {Object} updates - Fields to update
 */
async function updateAgent(agentId, updates) {
  try {
    const response = await vapiClient.patch(`/agents/${agentId}`, updates);
    console.log(`Agent updated: ${agentId}`);
    return response.data;
  } catch (error) {
    console.error(`Failed to update agent ${agentId}:`, error.response?.data || error.message);
    throw error;
  }
}

/**
 * Get agent details
 * @param {String} agentId - VAPI agent ID
 */
async function getAgent(agentId) {
  try {
    const response = await vapiClient.get(`/agents/${agentId}`);
    return response.data;
  } catch (error) {
    console.error(`Failed to get agent ${agentId}:`, error.response?.data || error.message);
    throw error;
  }
}

/**
 * List all agents in account
 */
async function listAgents() {
  try {
    const response = await vapiClient.get('/agents');
    console.log(`Found ${response.data.agents.length} agents`);
    return response.data.agents;
  } catch (error) {
    console.error('Failed to list agents:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Make outbound call using agent
 * @param {String} agentId - VAPI agent ID
 * @param {String} prospectPhone - Phone number to call
 */
async function makeOutboundCall(agentId, prospectPhone) {
  try {
    const response = await vapiClient.post('/calls', {
      agentId: agentId,
      phoneNumberId: null, // Uses agent's configured phone
      customerNumber: prospectPhone,
      assistantOverrides: {
        rules: [
          {
            id: 'interrupt',
            conditions: [
              {
                param: 'prospectInterruption',
                operator: 'equals',
                value: 'true'
              }
            ],
            steps: [
              {
                id: 'listen',
                message: 'Let the prospect finish their thought'
              }
            ]
          }
        ]
      }
    });

    console.log(`Call initiated: ${response.data.id} to ${prospectPhone}`);
    return response.data;
  } catch (error) {
    console.error('Failed to make call:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Get call details and transcript
 * @param {String} callId - VAPI call ID
 */
async function getCallDetails(callId) {
  try {
    const response = await vapiClient.get(`/calls/${callId}`);
    return response.data;
  } catch (error) {
    console.error(`Failed to get call ${callId}:`, error.response?.data || error.message);
    throw error;
  }
}

/**
 * List recent calls
 * @param {Object} options - Filter options (limit, order, etc)
 */
async function listCalls(options = {}) {
  try {
    const params = new URLSearchParams();
    if (options.limit) params.append('limit', options.limit);
    if (options.order) params.append('order', options.order); // 'desc' for recent first

    const response = await vapiClient.get(`/calls?${params}`);
    return response.data.calls;
  } catch (error) {
    console.error('Failed to list calls:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Deploy all three agents programmatically
 */
async function deployAllAgents() {
  const agentConfigs = {
    echo: require('./vapi-agent-echo-config.json'),
    swift: require('./vapi-agent-swift-config.json'),
    bella: require('./vapi-agent-bella-config.json')
  };

  const deployedAgents = {};

  for (const [name, config] of Object.entries(agentConfigs)) {
    console.log(`Deploying ${name.toUpperCase()}...`);
    try {
      const agent = await deployAgent(config.agent);
      deployedAgents[name] = {
        id: agent.id,
        name: agent.name,
        phoneNumber: agent.phoneNumber,
        status: 'deployed'
      };
      console.log(`✓ ${name} deployed successfully\n`);
    } catch (error) {
      console.error(`✗ Failed to deploy ${name}\n`);
    }
  }

  return deployedAgents;
}

/**
 * Mass outbound calling campaign
 * @param {String} agentId - Agent to use for calls
 * @param {Array} prospectList - Array of phone numbers
 * @param {Number} callsPerMinute - Rate limit (default: 2)
 */
async function launchCampaign(agentId, prospectList, callsPerMinute = 2) {
  const delayMs = (60 * 1000) / callsPerMinute; // MS between calls

  console.log(`Launching campaign: ${prospectList.length} calls with ${callsPerMinute} calls/min`);

  const results = [];

  for (let i = 0; i < prospectList.length; i++) {
    const prospect = prospectList[i];

    try {
      const call = await makeOutboundCall(agentId, prospect.phoneNumber);
      results.push({
        prospect: prospect.name,
        phone: prospect.phoneNumber,
        callId: call.id,
        status: 'initiated',
        timestamp: new Date()
      });

      console.log(`[${i + 1}/${prospectList.length}] Call initiated to ${prospect.name}`);
    } catch (error) {
      results.push({
        prospect: prospect.name,
        phone: prospect.phoneNumber,
        status: 'failed',
        error: error.message,
        timestamp: new Date()
      });

      console.error(`[${i + 1}/${prospectList.length}] Failed to call ${prospect.name}`);
    }

    // Rate limiting: wait before next call
    if (i < prospectList.length - 1) {
      await new Promise(resolve => setTimeout(resolve, delayMs));
    }
  }

  return results;
}

/**
 * Monitor call progress and log outcomes
 * @param {Array} callIds - Array of call IDs to monitor
 */
async function monitorCalls(callIds) {
  const pollInterval = 5000; // Check every 5 seconds
  const completedCalls = {};

  console.log(`Monitoring ${callIds.length} calls...`);

  return new Promise((resolve) => {
    const checkInterval = setInterval(async () => {
      for (const callId of callIds) {
        if (completedCalls[callId]) continue;

        try {
          const callData = await getCallDetails(callId);

          if (callData.status === 'ended') {
            completedCalls[callId] = {
              duration: callData.duration,
              outcome: callData.outcome, // 'interested', 'not_interested', 'demo_booked', etc
              transcript: callData.transcript,
              timestamp: new Date()
            };

            console.log(`✓ Call ${callId} completed: ${callData.outcome}`);
          }
        } catch (error) {
          console.error(`Failed to get call ${callId}:`, error.message);
        }
      }

      // If all calls completed, stop monitoring
      if (Object.keys(completedCalls).length === callIds.length) {
        clearInterval(checkInterval);
        resolve(completedCalls);
      }
    }, pollInterval);
  });
}

module.exports = {
  deployAgent,
  updateAgent,
  getAgent,
  listAgents,
  makeOutboundCall,
  getCallDetails,
  listCalls,
  deployAllAgents,
  launchCampaign,
  monitorCalls
};
