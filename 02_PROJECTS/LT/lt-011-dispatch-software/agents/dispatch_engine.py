import asyncio
import random
import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("DispatchOS")

# 1. Domain Models
class Location(BaseModel):
    address: str
    latitude: float
    longitude: float

class Load(BaseModel):
    id: str
    shipper_id: str
    origin: Location
    destination: Location
    equipment_type: str
    weight_lbs: float
    budget_usd: float
    status: str = "LOAD_CREATED"

class Carrier(BaseModel):
    id: str
    name: str
    on_time_rate: float
    claim_rate: float
    avg_rate_per_mile: float

class Truck(BaseModel):
    id: str
    carrier_id: str
    equipment_type: str
    status: str = "available"
    latitude: float
    longitude: float

class WorkflowState(BaseModel):
    load: Load
    current_step: str = "load_received"
    matched_carriers: List[Carrier] = Field(default_factory=list)
    selected_carrier: Optional[Carrier] = None
    negotiated_rate: float = 0.0
    tracking_coordinates: List[Dict[str, float]] = Field(default_factory=list)
    pod_verified: bool = False
    gross_margin_usd: float = 0.0
    evaluation_score: float = 0.0
    history: List[str] = Field(default_factory=list)

# 2. Mock Knowledge Graph Connection
class MockGraphContext:
    async def query(self, cypher: str, **kwargs) -> List[Dict[str, Any]]:
        # Simulates returning matched carriers near the pickup location
        logger.info(f"Querying graph: {cypher.strip().split('\n')[0]}...")
        return [
            {
                "c.id": "carrier-uuid-9811",
                "c.name": "Tarheel Express Trucking",
                "perf.on_time_rate": 0.96,
                "perf.claim_rate": 0.01,
                "perf.avg_rate_per_mile": 2.10
            },
            {
                "c.id": "carrier-uuid-9812",
                "c.name": "Blue Ridge Transport",
                "perf.on_time_rate": 0.92,
                "perf.claim_rate": 0.02,
                "perf.avg_rate_per_mile": 2.05
            },
            {
                "c.id": "carrier-uuid-9813",
                "c.name": "Metrolina LTL",
                "perf.on_time_rate": 0.89,
                "perf.claim_rate": 0.00,
                "perf.avg_rate_per_mile": 2.20
            }
        ]

    async def get_lane_rates(self, origin: str, dest: str, equipment: str) -> Dict[str, float]:
        # Return historical rates
        return {
            "avg_rate_per_mile": 2.15,
            "high_rate_per_mile": 2.40,
            "low_rate_per_mile": 1.95
        }

# 3. Agent Implementations
class LoadValidatorAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running LoadValidatorAgent for load: {state.load.id}")
        load = state.load
        if not load.origin.address or not load.destination.address:
            raise ValueError("Invalid origin/destination addresses.")
        if load.weight_lbs <= 0:
            raise ValueError("Cargo weight must be greater than zero.")
        load.status = "VALIDATED"
        return {"load": load, "history_update": "Load details validated."}

class CarrierMatcherAgent:
    def __init__(self, graph):
        self.graph = graph

    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running CarrierMatcherAgent for load: {state.load.id}")
        # Query matching carriers
        results = await self.graph.query(
            "MATCH (l:Load)-[:PICKS_UP_AT]->(pickup)...",
            load_id=state.load.id
        )
        
        candidates = []
        for r in results:
            candidates.append(Carrier(
                id=r["c.id"],
                name=r["c.name"],
                on_time_rate=r["perf.on_time_rate"],
                claim_rate=r["perf.claim_rate"],
                avg_rate_per_mile=r["perf.avg_rate_per_mile"]
            ))
            
        logger.info(f"Found {len(candidates)} candidate carriers near pickup.")
        return {"matched_carriers": candidates, "history_update": f"Matched {len(candidates)} carriers."}

class RateNegotiatorAgent:
    def __init__(self, graph):
        self.graph = graph

    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running RateNegotiatorAgent for load: {state.load.id}")
        load = state.load
        carriers = state.matched_carriers
        
        if not carriers:
            raise ValueError("No carriers matched to negotiate rates.")

        # Query lane records
        lane_stats = await self.graph.get_lane_rates(
            load.origin.address, load.destination.address, load.equipment_type
        )
        
        # Calculate dynamic price to maximize margin
        # Shipper budget sets our revenue cap
        shipper_max_per_mile = load.budget_usd / 250.0  # assume 250 mile trip
        carrier_target_per_mile = lane_stats["avg_rate_per_mile"]
        
        # Select target carrier (lowest historical rate with solid performance)
        target_carrier = min(carriers, key=lambda c: c.avg_rate_per_mile)
        
        # Negotiate optimal rate (splitting spread)
        negotiated_rate_per_mile = (shipper_max_per_mile + target_carrier.avg_rate_per_mile) / 2.0
        negotiated_rate = round(negotiated_rate_per_mile * 250.0, 2)
        
        logger.info(f"Negotiated billing rate: ${negotiated_rate} (vs budget: ${load.budget_usd})")
        return {
            "selected_carrier": target_carrier,
            "negotiated_rate": negotiated_rate,
            "history_update": f"Rate agreed at ${negotiated_rate} with {target_carrier.name}."
        }

class DispatchAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running DispatchAgent for carrier: {state.selected_carrier.name}")
        state.load.status = "ASSIGNED"
        return {"load": state.load, "history_update": f"Tender sent and accepted by carrier."}

class TrackingMonitorAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running TrackingMonitorAgent for load: {state.load.id}")
        state.load.status = "IN_TRANSIT"
        # Simulate tracking updates
        coords = [
            {"lat": state.load.origin.latitude, "lng": state.load.origin.longitude},
            {"lat": (state.load.origin.latitude + state.load.destination.latitude) / 2.0, "lng": (state.load.origin.longitude + state.load.destination.longitude) / 2.0},
            {"lat": state.load.destination.latitude, "lng": state.load.destination.longitude}
        ]
        return {"load": state.load, "tracking_coordinates": coords, "history_update": "Transit completed. GPS geofence verified."}

class ExceptionHandlerAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.warning(f"Exception triggered for load: {state.load.id}")
        return {"history_update": "Exception mitigated automatically."}

class ConfirmationAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running ConfirmationAgent for load: {state.load.id}")
        state.load.status = "DELIVERED"
        return {"load": state.load, "pod_verified": True, "history_update": "POD verified via OCR signature check."}

class BillingAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running BillingAgent for load: {state.load.id}")
        revenue = state.load.budget_usd
        cost = state.negotiated_rate
        margin = revenue - cost
        state.load.status = "COMPLETED"
        logger.info(f"Financial summary -> Revenue: ${revenue} | Cost: ${cost} | Net Margin: ${margin}")
        return {
            "load": state.load,
            "gross_margin_usd": margin,
            "history_update": f"Shipper invoiced ${revenue}. Payout of ${cost} released. Margin of ${margin} captured."
        }

class EvaluatorAgent:
    async def run(self, state: WorkflowState) -> Dict[str, Any]:
        logger.info(f"Running EvaluatorAgent for load: {state.load.id}")
        score = 0.95 if state.pod_verified else 0.50
        return {"evaluation_score": score, "history_update": f"Performance evaluation complete: score={score}"}

# 4. Workflow Engine State Machine
class WorkflowEngine:
    def __init__(self):
        graph = MockGraphContext()
        self.agents = {
            "load_validator": LoadValidatorAgent(),
            "carrier_matching": CarrierMatcherAgent(graph),
            "rate_negotiation": RateNegotiatorAgent(graph),
            "dispatch_offer": DispatchAgent(),
            "tracking": TrackingMonitorAgent(),
            "exception_handling": ExceptionHandlerAgent(),
            "delivery_confirmation": ConfirmationAgent(),
            "billing": BillingAgent(),
            "performance_evaluation": EvaluatorAgent()
        }
        
        self.transitions = {
            "load_received": {"success": "load_validator", "agent": "load_validator"},
            "load_validator": {"success": "carrier_matching", "agent": "carrier_matching"},
            "carrier_matching": {"success": "rate_negotiation", "agent": "rate_negotiation"},
            "rate_negotiation": {"success": "dispatch_offer", "agent": "dispatch_offer"},
            "dispatch_offer": {"success": "tracking", "agent": "tracking"},
            "tracking": {"success": "delivery_confirmation", "agent": "delivery_confirmation"},
            "delivery_confirmation": {"success": "billing", "agent": "billing"},
            "billing": {"success": "performance_evaluation", "agent": "billing"},
            "performance_evaluation": {"success": "completed", "agent": "performance_evaluation"}
        }

    async def execute(self, load: Load) -> WorkflowState:
        state = WorkflowState(load=load)
        logger.info(f"=== Starting dispatch workflow for load: {load.id} ===")
        
        while state.current_step != "completed":
            step = state.current_step
            transition = self.transitions.get(step)
            
            if not transition or not transition["agent"]:
                break
                
            agent_name = transition["agent"]
            agent = self.agents[agent_name]
            
            # Execute agent step
            try:
                result = await agent.run(state)
                # Update state attributes
                for key, val in result.items():
                    if key != "history_update" and hasattr(state, key):
                        setattr(state, key, val)
                
                # Record trace logs
                history_log = result.get("history_update", f"Executed step: {step}")
                state.history.append(history_log)
                logger.info(f"Trace: {history_log}")
                
                # Advance step
                state.current_step = transition["success"]
            except Exception as e:
                logger.error(f"Execution failed at step {step}: {e}")
                state.history.append(f"Failure in step {step}: {e}")
                state.current_step = "exception_handling"
                
        logger.info(f"=== Workflow finished at step: {state.current_step} ===")
        return state

# 5. Local Execution test helper
if __name__ == "__main__":
    dummy_load = Load(
        id="load-uuid-7712",
        shipper_id="shipper-uuid-1123",
        origin=Location(address="Charlotte, NC", latitude=35.227085, longitude=-80.843124),
        destination=Location(address="Atlanta, GA", latitude=33.748995, longitude=-84.387982),
        equipment_type="Dry Van",
        weight_lbs=42000.0,
        budget_usd=1650.0
    )
    
    engine = WorkflowEngine()
    asyncio.run(engine.execute(dummy_load))
