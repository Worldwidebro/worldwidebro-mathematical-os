# OmniRoute Routing Rules and Fallbacks

This document outlines the operational routing rules, failover mechanisms, and metric-based targets handled by the **OmniRoute** traffic controller.

## 1. Routing Table Definitions

OmniRoute maps logical target tags to physical model endpoints. The system loads configurations from `/AI-CORE/policies/routing_policies.yaml`.

```text
Incoming Target: "auto/coding"
  |
  +--> Check Node Status: Anthropic Cloud Available?
         |
         +--> [Yes] -> Route to Claude-3-5-Sonnet (Direct API)
         |
         +--> [No]  -> Failover to DeepSeek Coder (Cloud)
                |
                +--> [No] -> Local Fallback: Qwen-2.5-Coder-32B (Ollama:11434)
```

The table below maps the routing rules:

| Logical Model Tag | Route Sequence | Target Provider | Failover Targets |
| :--- | :--- | :--- | :--- |
| `auto` | 1. Claude-3-5-Sonnet<br>2. GPT-4o | Anthropic<br>OpenAI | Qwen-2.5-32B (Local) |
| `auto/coding` | 1. Claude-3-5-Sonnet<br>2. DeepSeek-Coder | Anthropic<br>DeepSeek | Qwen-2.5-Coder-32B (Local) |
| `auto/smart` | 1. Claude-3-5-Sonnet<br>2. GPT-4o | Anthropic<br>OpenAI | DeepSeek-R1 (Local) |
| `auto/cheap` | 1. DeepSeek-V3<br>2. GPT-4o-Mini | DeepSeek<br>OpenAI | Llama-3-8B (Local) |
| `auto/fast` | 1. GPT-4o-Mini<br>2. Claude-3-5-Haiku | OpenAI<br>Anthropic | Qwen-2.5-7B (Local) |
| `auto/offline` | 1. Qwen-2.5-Coder-32B<br>2. Llama-3-8B | Ollama (Local)<br>Ollama (Local) | None |

---

## 2. Failover Trigger Conditions

OmniRoute will automatically route requests to the next fallback target in the sequence if any of the following triggers occur:

1. **HTTP Status Code**: Receipt of `429` (Rate Limited), `500`/`502`/`503` (Server Error) from the primary provider.
2. **Connection Failure**: Host unreachable, DNS resolution error, or TCP connection refused.
3. **TTFT (Time to First Token) Exceeded**: The primary provider fails to return the first token within **8 seconds** (streamed responses) or **15 seconds** (non-streamed responses).
4. **Context Window Exceeded**: The request length exceeds the primary model's token limits.

---

## 3. Policy Rebuild and Hot-Reloading

OmniRoute supports **zero-downtime hot-reloading** of routing configurations. When changes are saved to `/AI-CORE/policies/routing_policies.yaml`, the server re-parses the YAML file in-memory using file watchers, ensuring active agent conversations are never interrupted.
