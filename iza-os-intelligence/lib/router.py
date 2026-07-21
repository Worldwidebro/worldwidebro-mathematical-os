import os
import urllib.request
import json

class ModelRouter:
    def __init__(self, lite_llm_url=None, ollama_url=None, default_model=None, fallback_model=None):
        self.lite_llm_url = lite_llm_url or os.getenv("LITELLM_URL", "http://100.87.214.70:4000")
        self.ollama_url = ollama_url or os.getenv("OLLAMA_HOST", "http://100.87.214.70:11434")
        self.default_model = default_model or "qwen2.5:72b"
        self.fallback_model = fallback_model or "qwen2.5:7b"

    def route(self, prompt, model=None):
        target_model = model or self.default_model
        
        # 1. Try LiteLLM gateway
        try:
            print(f"[Router] Attempting LiteLLM gateway: {self.lite_llm_url} (Model: {target_model})")
            req = urllib.request.Request(
                f"{self.lite_llm_url}/v1/chat/completions",
                data=json.dumps({
                    "model": target_model,
                    "messages": [{"role": "user", "content": prompt}]
                }).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return data['choices'][0]['message']['content']
        except Exception as e:
            print(f"[Router] LiteLLM gateway failed: {e}. Falling back to Ollama.")

        # 2. Try Local Ollama fallback
        return self.fallback_to_ollama(prompt)

    def fallback_to_ollama(self, prompt):
        try:
            print(f"[Router] Attempting local Ollama: {self.ollama_url} (Model: {self.fallback_model})")
            req = urllib.request.Request(
                f"{self.ollama_url}/api/generate",
                data=json.dumps({
                    "model": self.fallback_model,
                    "prompt": prompt,
                    "stream": False
                }).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return data['response']
        except Exception as e:
            print(f"[Router] Offline fallback failed: {e}. Model route unreachable.")
            raise RuntimeError(f"No available LLM backend: {e}")
