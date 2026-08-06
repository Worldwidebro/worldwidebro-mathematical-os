import pytest
from oss_scout_agent import OSSScoutAgent, OSSScoutDecision

@pytest.mark.asyncio
async def test_oss_scout_agent_parsing_and_evaluation():
    # 1. Initialize agent
    scout = OSSScoutAgent()
    
    # Assert markdown loading was successful
    assert "OSS Scout Agent" in scout.system_prompt
    assert "selected_repo_name" in scout.output_schema["properties"]
    
    # 2. Run simulation
    candidates = [
        {
            "name": "traccar/traccar",
            "stars": 4500,
            "license": "Apache-2.0",
            "pushed_at": "2026-07-30",
            "docker_files": ["Dockerfile", "docker-compose.yml"],
            "description": "Open-source GPS tracking system"
        },
        {
            "name": "random/hobby-tracker",
            "stars": 12,
            "license": "GPL-3.0",
            "pushed_at": "2021-02-01",
            "docker_files": [],
            "description": "Simple python tracking hobby code"
        }
    ]
    
    decision = await scout.scout_and_index("gps_tracking", candidates)
    
    # 3. Assert output shape compliance
    assert isinstance(decision, OSSScoutDecision)
    assert decision.selected_repo_name == "traccar/traccar"
    assert decision.suitability_score == 0.85
    assert decision.license_type == "Apache-2.0"
    assert decision.docker_available is True
    assert decision.integration_path == "REST"
    assert "Traccar is the most mature" in decision.reasoning
