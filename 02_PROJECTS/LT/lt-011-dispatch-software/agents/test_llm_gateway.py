import pytest
from pydantic import BaseModel
from llm_gateway import LLMGateway

# Test Schema Definition
class CarrierMatchDecision(BaseModel):
    selected_carrier_id: str
    confidence: float
    reasoning: str

@pytest.mark.asyncio
async def test_llm_gateway_structured_generation_and_fallback():
    # 1. Initialize gateway with A/B shadow testing enabled
    gateway = LLMGateway(primary_model="gemini-1.5-flash", shadow_model="gpt-4o")
    
    system = "You are a carrier match expert."
    user = "Select a carrier for load test-load-9901"
    
    # 2. Run structured output parsing check
    decision = await gateway.generate_structured(
        load_id="test-load-9901",
        system_prompt=system,
        user_prompt=user,
        response_model=CarrierMatchDecision
    )
    
    assert isinstance(decision, CarrierMatchDecision)
    assert decision.selected_carrier_id == "carrier-uuid-9812"
    assert decision.confidence == 0.94
    
    # Verify trace audit log was written
    assert len(gateway.traces) == 1
    trace = gateway.traces[0]
    assert trace.primary_model == "gemini-1.5-flash"
    assert trace.shadow_model == "gpt-4o"
    assert trace.cost_usd > 0
    assert trace.latency_sec > 0
    assert trace.shadow_output is not None
    assert trace.parsing_fallback_triggered is False
