# Framework → OmniRoute wiring cheat sheet
#
# Always set:
#   export OPENAI_BASE_URL=http://127.0.0.1:20128/v1
#   export OPENAI_API_KEY=<omniroute key>
# Optional direct AirLLM (bypass router):
#   export OPENAI_BASE_URL=http://100.87.214.70:8020/v1

## instructor
# pip install instructor openai
# client = instructor.from_openai(OpenAI(base_url=..., api_key=...))

## marvin
# pip install marvin
# marvin.settings.openai.api_base / api_key → OmniRoute

## langchain
# pip install langchain-openai
# ChatOpenAI(base_url=OPENAI_BASE_URL, api_key=..., model="qwen2.5-coder:14b")

## llamaindex
# pip install llama-index-llms-openai
# OpenAI(api_base=OPENAI_BASE_URL, api_key=..., model=...)

## haystack
# OpenAIChatGenerator(api_base_url=OPENAI_BASE_URL, api_key=..., model=...)

## dspy
# dspy.LM("openai/qwen2.5-coder:14b", api_base=OPENAI_BASE_URL, api_key=...)

## semantic-kernel
# OpenAIChatCompletion(ai_model_id=..., api_key=..., endpoint=OPENAI_BASE_URL)

## langflow / genkit
# Point OpenAI component / plugin base URL at OmniRoute /v1

## Prefer continuous-coding combo models
# 1) qwen2.5-coder:14b (Air/Studio Ollama)
# 2) llama3.1:8b (Studio Ollama)
# 3) AirLLM HF model (slow, huge)
# 4) exo MLX coder (Studio)
