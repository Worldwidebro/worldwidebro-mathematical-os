/**
 * LiteLLM to Ollama fallback router for IZA OS Intelligence Core
 */

export interface RouterConfig {
  liteLlmUrl: string;
  ollamaUrl: string;
  defaultModel: string;
  fallbackModel: string;
}

export class ModelRouter {
  private config: RouterConfig;

  constructor(config?: Partial<RouterConfig>) {
    this.config = {
      liteLlmUrl: process.env.LITELLM_URL || 'http://100.87.214.70:4000',
      ollamaUrl: process.env.OLLAMA_HOST || 'http://100.87.214.70:11434',
      defaultModel: 'qwen2.5:72b',
      fallbackModel: 'qwen2.5:7b',
      ...config,
    };
  }

  /**
   * Route request to LiteLLM with automatic local Ollama fallback on failure
   */
  async route(prompt: string, options: { model?: string } = {}): Promise<string> {
    const model = options.model || this.config.defaultModel;
    
    // 1. Try LiteLLM gateway first
    try {
      console.log(`[Router] Attempting LiteLLM gateway: ${this.config.liteLlmUrl} (Model: ${model})`);
      const response = await fetch(`${this.config.liteLlmUrl}/v1/chat/completions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: model,
          messages: [{ role: 'user', content: prompt }]
        })
      });
      
      if (response.ok) {
        const data = await response.json();
        return data.choices[0].message.content;
      }
      throw new Error(`LiteLLM returned status ${response.status}`);
    } catch (err) {
      console.warn(`[Router] LiteLLM gateway failed: ${err.message}. Falling back to Ollama.`);
      
      // 2. Fallback to local Ollama runtime (cost-free, offline-ready)
      return this.fallbackToOllama(prompt);
    }
  }

  private async fallbackToOllama(prompt: string): Promise<string> {
    try {
      console.log(`[Router] Attempting local Ollama: ${this.config.ollamaUrl} (Model: ${this.config.fallbackModel})`);
      const response = await fetch(`${this.config.ollamaUrl}/api/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: this.config.fallbackModel,
          prompt: prompt,
          stream: false
        })
      });

      if (response.ok) {
        const data = await response.json();
        return data.response;
      }
      throw new Error(`Ollama returned status ${response.status}`);
    } catch (err) {
      console.error(`[Router] Offline fallback failed: ${err.message}. Model route unreachable.`);
      throw new Error(`No available LLM backend: ${err.message}`);
    }
  }
}
