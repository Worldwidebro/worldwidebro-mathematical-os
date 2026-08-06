import pytest
from dispatch_engine import WorkflowEngine, Load, Location

@pytest.mark.asyncio
async def test_end_to_end_dispatch_workflow():
    # Setup test load
    test_load = Load(
        id="test-load-9901",
        shipper_id="shipper-uuid-1123",
        origin=Location(address="Charlotte, NC", latitude=35.227085, longitude=-80.843124),
        destination=Location(address="Atlanta, GA", latitude=33.748995, longitude=-84.387982),
        equipment_type="Dry Van",
        weight_lbs=42000.0,
        budget_usd=1650.0
    )

    engine = WorkflowEngine()
    final_state = await engine.execute(test_load)

    # 1. Assert successful transition path
    assert final_state.current_step == "completed"
    
    # 2. Assert carrier matching successfully populated selection
    assert final_state.selected_carrier is not None
    assert final_state.selected_carrier.id == "carrier-uuid-9812"  # matches the lowest avg rate
    
    # 3. Assert rate negotiator dynamically adjusted billing rate to make profit
    assert final_state.negotiated_rate < test_load.budget_usd
    assert final_state.negotiated_rate > 0
    assert final_state.gross_margin_usd > 0
    
    # 4. Assert delivery tracking coordinates populated
    assert len(final_state.tracking_coordinates) == 3
    assert final_state.pod_verified is True
    assert final_state.load.status == "COMPLETED"
    
    # 5. Assert trace logs captured in history
    assert any("validated" in log.lower() for log in final_state.history)
    assert any("payout" in log.lower() for log in final_state.history)
    assert any("score" in log.lower() for log in final_state.history)
