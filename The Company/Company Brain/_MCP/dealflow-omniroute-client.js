/**
 * DealFlowOS OmniRoute Client
 * Streaming HTTP client for DealFlowOS agents via OmniRoute
 *
 * Authority: Agent Control Plane (CP-006)
 */

const OMNIROUTE_URL = 'http://100.87.214.70:20128';
const CHAT_ENDPOINT = `${OMNIROUTE_URL}/api/chat`;
const HEALTH_ENDPOINT = `${OMNIROUTE_URL}/health`;

class OmniRouteStreamingClient {
  constructor(baseUrl = OMNIROUTE_URL) {
    this.baseUrl = baseUrl;
    this.chatEndpoint = `${baseUrl}/api/chat`;
    this.healthEndpoint = `${baseUrl}/health`;
    this.activeRequests = new Map();
  }

  /**
   * Check OmniRoute health
   */
  async healthCheck() {
    try {
      const response = await fetch(this.healthEndpoint, { timeout: 5000 });
      if (response.ok) {
        return {
          status: 'online',
          url: this.baseUrl,
          timestamp: new Date().toISOString()
        };
      }
      return {
        status: 'error',
        code: response.status,
        message: await response.text()
      };
    } catch (error) {
      return {
        status: 'offline',
        error: error.message
      };
    }
  }

  /**
   * Streaming chat invocation
   *
   * @param {Object} options - Invocation options
   * @param {string} options.query - User query
   * @param {string} options.model - Model name (default/qwen-fast/qwen-heavy)
   * @param {number} options.temperature - Sampling temperature
   * @param {number} options.maxTokens - Max response tokens
   * @param {Object} options.context - Optional context dict
   * @param {Function} options.onChunk - Callback for each streamed chunk
   * @param {Function} options.onError - Error callback
   * @param {Function} options.onComplete - Completion callback
   */
  async invokeStream({
    query,
    model = 'default',
    temperature = 0.7,
    maxTokens = 2048,
    context = {},
    onChunk = () => {},
    onError = () => {},
    onComplete = () => {}
  }) {
    const requestId = `${Date.now()}-${Math.random()}`;

    const payload = {
      model,
      messages: [{ role: 'user', content: query }],
      temperature,
      max_tokens: maxTokens,
      stream: true,
      context
    };

    try {
      const response = await fetch(this.chatEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${await response.text()}`);
      }

      // Parse streaming response
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop(); // Keep incomplete line in buffer

        for (const line of lines) {
          if (line.trim()) {
            try {
              const chunk = JSON.parse(line);
              onChunk(chunk);
            } catch (e) {
              console.warn('Failed to parse chunk:', line, e);
            }
          }
        }
      }

      // Process any remaining buffer
      if (buffer.trim()) {
        try {
          const chunk = JSON.parse(buffer);
          onChunk(chunk);
        } catch (e) {
          console.warn('Failed to parse final chunk:', buffer, e);
        }
      }

      onComplete({ status: 'success', model, query });
      this.activeRequests.delete(requestId);
    } catch (error) {
      const errorMsg = error.message || 'Unknown error';
      onError({ status: 'error', error: errorMsg, model, query });
      this.activeRequests.delete(requestId);
    }
  }

  /**
   * Invoke research agent (streaming)
   */
  async invokeResearchAgent(
    query,
    companyContext = {},
    callbacks = {}
  ) {
    const systemPrompt = `You are a deal flow research agent. Your role is to:
1. Gather competitive intelligence
2. Identify market trends and opportunities
3. Research company financials, leadership, capabilities
4. Provide credible, sourced findings with confidence scores

Format findings as structured JSON with: finding, source, confidence (0-1), date.`;

    const fullQuery = `${systemPrompt}\n\nQuery: ${query}`;

    return this.invokeStream({
      query: fullQuery,
      model: 'qwen-heavy', // Research = complex
      temperature: 0.3,
      maxTokens: 3000,
      context: { type: 'research', company: companyContext },
      ...callbacks
    });
  }

  /**
   * Invoke qualification agent (streaming)
   */
  async invokeQualificationAgent(
    companyData,
    callbacks = {}
  ) {
    const systemPrompt = `You are a deal qualification agent. Score and qualify companies based on:
1. Market fit with target customer profile
2. Revenue/growth potential
3. Industry/vertical alignment
4. Competitive positioning
5. Decision urgency signals

Return JSON: {score: 0-100, fit: 0-1, decision: QUALIFY|MAYBE|REJECT, reasons: [str], next_steps: [str]}`;

    const fullQuery = `${systemPrompt}\n\nCompany: ${JSON.stringify(companyData, null, 2)}`;

    return this.invokeStream({
      query: fullQuery,
      model: 'qwen-fast', // Qualification = fast
      temperature: 0.5,
      maxTokens: 1500,
      context: { type: 'qualification', company: companyData },
      ...callbacks
    });
  }

  /**
   * Invoke outreach agent (streaming)
   */
  async invokeOutreachAgent(
    qualifiedLeads,
    campaignContext = {},
    callbacks = {}
  ) {
    const systemPrompt = `You are a deal outreach agent. For each qualified lead, generate:
1. Personalized email subject line (compelling, not salesy)
2. Email body (3-4 short paragraphs, specific to their company/role)
3. Best time to outreach (day/time)
4. Follow-up sequence (3 touches over 2 weeks)
5. LinkedIn engagement hooks (before/after outreach)

Return JSON array: [{lead_name, email_subject, email_body, timing, followups, engagement_hooks}]`;

    const leadsArray = Array.isArray(qualifiedLeads) ? qualifiedLeads : [qualifiedLeads];
    const fullQuery = `${systemPrompt}\n\nLeads:\n${JSON.stringify(leadsArray.slice(0, 5), null, 2)}\n\nContext: ${JSON.stringify(campaignContext, null, 2)}`;

    return this.invokeStream({
      query: fullQuery,
      model: 'default', // Outreach = balanced
      temperature: 0.7,
      maxTokens: 4000,
      context: { type: 'outreach', lead_count: leadsArray.length },
      ...callbacks
    });
  }
}

/**
 * DealFlowOS Terminal UI
 * Renders streaming agent responses to a live terminal
 */
class DealFlowOSTerminal {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.lines = [];
    this.maxLines = 500;
    this.autoScroll = true;
    this.isRunning = false;

    this.createUI();
  }

  createUI() {
    this.container.innerHTML = `
      <div class="dealflow-terminal">
        <div class="terminal-header">
          <div class="terminal-title">
            <span class="pulse-dot" id="status-dot"></span>
            <span id="terminal-title">DealFlowOS Command Center</span>
          </div>
          <div class="terminal-controls">
            <button id="clear-btn" onclick="dealflowTerminal.clear()" class="terminal-btn">Clear</button>
            <button id="pause-btn" onclick="dealflowTerminal.toggleAutoScroll()" class="terminal-btn">Pause</button>
          </div>
        </div>
        <div class="terminal-content" id="terminal-content"></div>
        <div class="terminal-input">
          <span class="terminal-prompt">$</span>
          <input id="terminal-input" type="text" placeholder="Type command..." autocomplete="off">
        </div>
      </div>
    `;

    this.contentDiv = document.getElementById('terminal-content');
    this.inputEl = document.getElementById('terminal-input');
    this.statusDot = document.getElementById('status-dot');

    // Bind enter key
    this.inputEl.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const query = this.inputEl.value;
        this.inputEl.value = '';
        this.onCommand(query);
      }
    });
  }

  addLine(text, className = '') {
    const line = document.createElement('div');
    line.className = `terminal-line ${className}`;
    line.textContent = text;
    this.contentDiv.appendChild(line);
    this.lines.push(text);

    if (this.lines.length > this.maxLines) {
      this.contentDiv.removeChild(this.contentDiv.firstChild);
      this.lines.shift();
    }

    if (this.autoScroll) {
      this.contentDiv.scrollTop = this.contentDiv.scrollHeight;
    }
  }

  setStatus(running, agentName = '') {
    this.isRunning = running;
    this.statusDot.style.animation = running ? 'pulse 0.6s infinite' : 'none';
    const title = running ? `Running: ${agentName}...` : 'DealFlowOS Command Center';
    document.getElementById('terminal-title').textContent = title;
  }

  clear() {
    this.contentDiv.innerHTML = '';
    this.lines = [];
  }

  toggleAutoScroll() {
    this.autoScroll = !this.autoScroll;
    const btn = document.getElementById('pause-btn');
    btn.textContent = this.autoScroll ? 'Pause' : 'Resume';
  }

  async onCommand(query) {
    // This will be hooked up to actual agent invocations
    this.addLine(`> ${query}`, 'command');
    // Placeholder - actual implementation depends on AI Command Center
  }
}

/**
 * DealFlowOS Agent Dashboard
 * Manages agent invocations, displays results, tracks status
 */
class DealFlowOSAgentDashboard {
  constructor(omnirouteClient, terminal) {
    this.client = omnirouteClient;
    this.terminal = terminal;
    this.agents = {
      research: { name: 'Research Agent', status: 'idle', lastRun: null },
      qualification: { name: 'Qualification Agent', status: 'idle', lastRun: null },
      outreach: { name: 'Outreach Agent', status: 'idle', lastRun: null }
    };
  }

  /**
   * Launch research agent from AI Command Center
   */
  async launchResearchAgent(query, companyContext = {}) {
    this.terminal.setStatus(true, 'Research Agent');
    this.terminal.addLine(`\n[Research Agent] Starting research: ${query}`, 'info');

    try {
      await this.client.invokeResearchAgent(query, companyContext, {
        onChunk: (chunk) => {
          if (chunk.choices?.[0]?.delta?.content) {
            const text = chunk.choices[0].delta.content;
            this.terminal.addLine(text, 'response');
          }
        },
        onError: (err) => {
          this.terminal.addLine(`[ERROR] ${err.error}`, 'error');
          this.agents.research.status = 'error';
          this.terminal.setStatus(false);
        },
        onComplete: (result) => {
          this.terminal.addLine(`\n[Research Agent] Complete`, 'success');
          this.agents.research.status = 'idle';
          this.agents.research.lastRun = new Date().toISOString();
          this.terminal.setStatus(false);
        }
      });
    } catch (error) {
      this.terminal.addLine(`[ERROR] ${error.message}`, 'error');
      this.terminal.setStatus(false);
    }
  }

  /**
   * Launch qualification agent from AI Command Center
   */
  async launchQualificationAgent(companyData) {
    this.terminal.setStatus(true, 'Qualification Agent');
    this.terminal.addLine(`\n[Qualification Agent] Scoring: ${companyData.name || 'Unknown'}`, 'info');

    try {
      await this.client.invokeQualificationAgent(companyData, {
        onChunk: (chunk) => {
          if (chunk.choices?.[0]?.delta?.content) {
            const text = chunk.choices[0].delta.content;
            this.terminal.addLine(text, 'response');
          }
        },
        onError: (err) => {
          this.terminal.addLine(`[ERROR] ${err.error}`, 'error');
          this.agents.qualification.status = 'error';
          this.terminal.setStatus(false);
        },
        onComplete: () => {
          this.terminal.addLine(`\n[Qualification Agent] Complete`, 'success');
          this.agents.qualification.status = 'idle';
          this.agents.qualification.lastRun = new Date().toISOString();
          this.terminal.setStatus(false);
        }
      });
    } catch (error) {
      this.terminal.addLine(`[ERROR] ${error.message}`, 'error');
      this.terminal.setStatus(false);
    }
  }

  /**
   * Launch outreach agent from AI Command Center
   */
  async launchOutreachAgent(qualifiedLeads, campaignContext = {}) {
    this.terminal.setStatus(true, 'Outreach Agent');
    this.terminal.addLine(`\n[Outreach Agent] Generating sequences for ${qualifiedLeads.length} leads...`, 'info');

    try {
      await this.client.invokeOutreachAgent(qualifiedLeads, campaignContext, {
        onChunk: (chunk) => {
          if (chunk.choices?.[0]?.delta?.content) {
            const text = chunk.choices[0].delta.content;
            this.terminal.addLine(text, 'response');
          }
        },
        onError: (err) => {
          this.terminal.addLine(`[ERROR] ${err.error}`, 'error');
          this.agents.outreach.status = 'error';
          this.terminal.setStatus(false);
        },
        onComplete: () => {
          this.terminal.addLine(`\n[Outreach Agent] Complete`, 'success');
          this.agents.outreach.status = 'idle';
          this.agents.outreach.lastRun = new Date().toISOString();
          this.terminal.setStatus(false);
        }
      });
    } catch (error) {
      this.terminal.addLine(`[ERROR] ${error.message}`, 'error');
      this.terminal.setStatus(false);
    }
  }

  /**
   * Get agent status display
   */
  getStatusDisplay() {
    const lines = [
      '═══════════════════════════════════════════',
      'DealFlowOS Agent Status',
      '═══════════════════════════════════════════'
    ];

    for (const [key, agent] of Object.entries(this.agents)) {
      const icon = agent.status === 'idle' ? '✓' : agent.status === 'running' ? '▶' : '✗';
      const lastRun = agent.lastRun ? `[${new Date(agent.lastRun).toLocaleTimeString()}]` : '[Never]';
      lines.push(`${icon} ${agent.name}: ${agent.status.toUpperCase()} ${lastRun}`);
    }

    lines.push('═══════════════════════════════════════════');
    return lines.join('\n');
  }
}

// Global instances (initialize after DOM ready)
let omnirouteClient = null;
let dealflowTerminal = null;
let dealflowDashboard = null;

document.addEventListener('DOMContentLoaded', async () => {
  omnirouteClient = new OmniRouteStreamingClient(OMNIROUTE_URL);

  if (document.getElementById('terminal-container')) {
    dealflowTerminal = new DealFlowOSTerminal('terminal-container');
    dealflowDashboard = new DealFlowOSAgentDashboard(omnirouteClient, dealflowTerminal);

    // Show startup message
    dealflowTerminal.addLine('DealFlowOS Command Center initialized', 'info');
    dealflowTerminal.addLine(dealflowDashboard.getStatusDisplay(), 'info');

    // Check OmniRoute health
    const health = await omnirouteClient.healthCheck();
    if (health.status === 'online') {
      dealflowTerminal.addLine(`✓ OmniRoute online: ${health.url}`, 'success');
    } else {
      dealflowTerminal.addLine(`✗ OmniRoute offline: ${health.error}`, 'error');
    }
  }
});
