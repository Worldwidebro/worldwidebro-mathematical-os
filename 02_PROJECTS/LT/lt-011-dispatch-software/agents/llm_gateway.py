import os
import json
import time
import random
import logging
import asyncio
from typing import Dict, Any, List, Optional, Type
from pydantic import BaseModel

logger = logging.getLogger("LLMGateway")

# 1. Performance Tracking Node Schema
class LLMExecutionTrace(BaseModel):
    load_id: str
    primary_model: str
    shadow_model: Optional[str] = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    latency_sec: float
    cost_usd: float
    primary_output: Dict[str, Any]
    shadow_output: Optional[Dict[str, Any]] = None
    parsing_fallback_triggered: bool = False

# 2. Structured Harness Gateway
class LLMGateway:
    def __init__(self, primary_model: str = "gemini-1.5-flash", shadow_model: Optional[str] = None):
        self.primary_model = primary_model
        self.shadow_model = shadow_model
        self.traces: List[LLMExecutionTrace] = []

        # Simulated pricing per 1K tokens
        self.pricing = {
            "gemini-1.5-flash": {"prompt": 0.000075, "completion": 0.0003},
            "gemini-1.5-pro": {"prompt": 0.00125, "completion": 0.00375},
            "gpt-4o": {"prompt": 0.005, "completion": 0.015},
            "claude-3-5-sonnet": {"prompt": 0.003, "completion": 0.015}
        }

    def _get_cost(self, model: str, prompt_tok: int, comp_tok: int) -> float:
        rate = self.pricing.get(model, {"prompt": 0.001, "completion": 0.003})
        return (prompt_tok * rate["prompt"]) + (comp_tok * rate["completion"])

    async def generate_structured(
        self,
        load_id: str,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[BaseModel],
        retries: int = 2
    ) -> BaseModel:
        start_time = time.time()
        fallback_triggered = False
        primary_output_dict = {}
        shadow_output_dict = None

        logger.info(f"Routing request to primary model: {self.primary_model}")

        # Attempt execution on primary model
        for attempt in range(retries + 1):
            try:
                raw_response, p_tokens, c_tokens = await self._call_llm_api(
                    self.primary_model, system_prompt, user_prompt, response_model, simulate_error=(attempt == 0 and fallback_triggered)
                )
                primary_output_dict = json.loads(raw_response)
                # Validate against target Pydantic schema
                validated_data = response_model.model_validate(primary_output_dict)
                break
            except Exception as err:
                logger.warning(f"Attempt {attempt} failed on {self.primary_model}: {err}")
                if attempt == retries:
                    logger.error(f"All retries failed. Triggering automatic model fallback to gemini-1.5-pro.")
                    fallback_triggered = True
                    # Fallback to a tier-1 reasoning model
                    raw_response, p_tokens, c_tokens = await self._call_llm_api(
                        "gemini-1.5-pro", system_prompt, user_prompt, response_model
                    )
                    primary_output_dict = json.loads(raw_response)
                    validated_data = response_model.model_validate(primary_output_dict)
                    break
                fallback_triggered = True

        # Run Shadow Testing in parallel (non-blocking) if configured
        if self.shadow_model:
            logger.info(f"Running A/B Shadow test on model: {self.shadow_model}")
            try:
                raw_shadow, _, _ = await self._call_llm_api(
                    self.shadow_model, system_prompt, user_prompt, response_model
                )
                shadow_output_dict = json.loads(raw_shadow)
            except Exception as shadow_err:
                logger.warning(f"Shadow test failed on {self.shadow_model}: {shadow_err}")

        latency = time.time() - start_time
        cost = self._get_cost(self.primary_model if not fallback_triggered else "gemini-1.5-pro", p_tokens, c_tokens)

        # Log audit trace
        trace = LLMExecutionTrace(
            load_id=load_id,
            primary_model=self.primary_model if not fallback_triggered else "gemini-1.5-pro-fallback",
            shadow_model=self.shadow_model,
            prompt_tokens=p_tokens,
            completion_tokens=c_tokens,
            latency_sec=round(latency, 3),
            cost_usd=round(cost, 6),
            primary_output=primary_output_dict,
            shadow_output=shadow_output_dict,
            parsing_fallback_triggered=fallback_triggered
        )
        self.traces.append(trace)
        logger.info(f"Decision logged -> Latency: {trace.latency_sec}s | Cost: ${trace.cost_usd} | Fallback: {trace.parsing_fallback_triggered}")

        return validated_data

    async def _call_llm_api(
        self,
        model: str,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[BaseModel],
        simulate_error: bool = False
    ) -> tuple[str, int, int]:
        """
        Simulates LLM API call, returning json matching the Pydantic schema structure.
        In production, this delegates to the google-genai or openai SDK.
        """
        await asyncio.sleep(0.1)  # simulate network latency

        if simulate_error:
            raise ValueError("Simulated parsing/network error.")

        # Simulate structured output matched to the schema
        schema_name = response_model.__name__
        p_tokens = len(system_prompt + user_prompt) // 4
        
        if schema_name == "CarrierMatchDecision":
            mock_json = {
                "selected_carrier_id": "carrier-uuid-9812",
                "confidence": 0.94,
                "reasoning": f"Carrier has best historical on-time rate (96%) in similar lanes."
            }
        elif schema_name == "RateNegotiationDecision":
            mock_json = {
                "offered_rate_per_mile": 2.12,
                "negotiation_message": "Rate established based on lane average $2.15 and carrier target $2.10."
            }
        elif schema_name == "OSSScoutDecision":
            mock_json = {
                "selected_repo_name": "traccar/traccar",
                "suitability_score": 0.85,
                "license_type": "Apache-2.0",
                "docker_available": True,
                "integration_path": "REST",
                "reasoning": "Traccar is the most mature open-source GPS tracking option, has an active Docker container, and exposes a clean REST API."
            }
        else:
            mock_json = {"status": "ok", "reasoning": "Standard response schema matches."}

        c_tokens = len(str(mock_json)) // 4
        return json.dumps(mock_json), p_tokens, c_tokens
