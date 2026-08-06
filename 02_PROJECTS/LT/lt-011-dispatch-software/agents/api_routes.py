"""FastAPI: dispatch_engine + principal_enforcer → portals."""
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dispatch_engine import WorkflowEngine, Load, Location
import asyncio

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

active_workflows = {}
escalations_queue = []

class LoadRequest(BaseModel):
    id: str
    shipper_id: str
    origin_address: str
    destination_address: str
    equipment_type: str
    weight_lbs: float
    budget_usd: float

@app.post("/api/dispatch/run")
async def run_workflow(req: LoadRequest):
    """Trigger dispatch workflow."""
    load = Load(
        id=req.id, shipper_id=req.shipper_id,
        origin=Location(address=req.origin_address, latitude=35.2271, longitude=-80.8431),
        destination=Location(address=req.destination_address, latitude=33.7490, longitude=-84.3880),
        equipment_type=req.equipment_type, weight_lbs=req.weight_lbs, budget_usd=req.budget_usd
    )
    engine = WorkflowEngine()
    result = await engine.execute(load)
    active_workflows[req.id] = {
        "status": result.load.status,
        "margin": result.gross_margin_usd,
        "carrier": result.selected_carrier.name if result.selected_carrier else None,
        "history": result.history
    }
    return {"workflow_id": req.id, "margin": result.gross_margin_usd}

@app.get("/api/dispatch/leads")
async def get_leads():
    """Call center: get escalations."""
    return {"escalations": escalations_queue, "count": len(escalations_queue)}

@app.post("/api/dispatch/escalate")
async def post_escalation(metric: str, action: str):
    """Principal enforcer → call center."""
    escalations_queue.append({"metric": metric, "action": action})
    return {"queued": True}

@app.get("/api/dispatch/workflow/{workflow_id}")
async def get_workflow(workflow_id: str):
    """Client portal: load status."""
    return active_workflows.get(workflow_id, {"error": "Not found"})

@app.get("/api/dispatch/health")
async def health():
    """Admin portal: health check."""
    return {"status": "ok", "active": len(active_workflows), "escalations": len(escalations_queue)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
