#!/usr/bin/env python3
"""
OmniRoute — GitHub + LiteLLM + Neo4j Integration Gateway
Coordinates: GitHub webhooks → LiteLLM routing → Neo4j tracking → Supabase registry
"""

import os
import json
import logging
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
import httpx

logging.basicConfig(level=os.getenv("OMNIROUTE_LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LITELLM_API_BASE = os.getenv("LITELLM_API_BASE", "http://localhost:4001")
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")

app = FastAPI(title="OmniRoute", version="1.0.0")

# ============================================================
# GitHub Webhook Handler
# ============================================================

@app.post("/webhooks/github")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    """Route GitHub events to appropriate LiteLLM model"""
    payload = await request.json()
    event_type = request.headers.get("X-GitHub-Event", "unknown")

    logger.info(f"📨 GitHub webhook: {event_type}")
    background_tasks.add_task(process_github_event, event_type, payload)

    return JSONResponse({"status": "received", "event": event_type})


async def process_github_event(event_type: str, payload: dict):
    """Route GitHub events to appropriate model"""
    try:
        if event_type == "pull_request":
            await handle_pr_event(payload)
        elif event_type == "issues":
            await handle_issue_event(payload)
        elif event_type == "push":
            await handle_push_event(payload)
    except Exception as e:
        logger.error(f"Error processing event: {e}")


async def handle_pr_event(payload: dict):
    """Route PR events → local-coder model"""
    action = payload.get("action")
    pr = payload.get("pull_request", {})

    if action in ["opened", "reopened"]:
        logger.info(f"🔍 Routing PR #{pr.get('number')} to code-review")
        await route_to_model("local-coder", {
            "task": "review_pr",
            "pr_number": pr.get("number"),
            "title": pr.get("title"),
            "diff_url": pr.get("diff_url"),
        })


async def handle_issue_event(payload: dict):
    """Route issue events → local-small model"""
    action = payload.get("action")
    issue = payload.get("issue", {})

    if action == "opened":
        logger.info(f"📌 Routing issue #{issue.get('number')} to analysis")
        await route_to_model("local-small", {
            "task": "analyze_issue",
            "issue_number": issue.get("number"),
            "title": issue.get("title"),
            "body": issue.get("body"),
        })


async def handle_push_event(payload: dict):
    """Route push events → monitoring"""
    commits = payload.get("commits", [])
    ref = payload.get("ref", "")
    logger.info(f"📤 Push to {ref}: {len(commits)} commits")


# ============================================================
# LiteLLM Router
# ============================================================

async def route_to_model(model_name: str, task_data: dict):
    """Route task to specified LiteLLM model"""
    logger.info(f"🤖 Routing to {model_name}: {task_data.get('task')}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{LITELLM_API_BASE}/chat/completions",
                json={
                    "model": model_name,
                    "messages": [
                        {
                            "role": "system",
                            "content": f"You are helping with: {task_data.get('task')}"
                        },
                        {
                            "role": "user",
                            "content": json.dumps(task_data, indent=2)
                        }
                    ],
                    "temperature": 0.7,
                    "max_tokens": 2000,
                },
                timeout=60.0
            )

            if response.status_code == 200:
                result = response.json()
                logger.info(f"✅ Response received from {model_name}")
            else:
                logger.error(f"❌ {model_name} returned {response.status_code}")
        except Exception as e:
            logger.error(f"Error routing to {model_name}: {e}")


# ============================================================
# Health & Status
# ============================================================

@app.get("/health")
async def health_check():
    """Health check"""
    return {
        "status": "healthy",
        "service": "OmniRoute",
        "github_connected": bool(GITHUB_TOKEN),
        "litellm_base": LITELLM_API_BASE,
    }


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "OmniRoute",
        "version": "1.0.0",
        "purpose": "GitHub → LiteLLM → Neo4j Integration Gateway",
        "status": "running"
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("OMNIROUTE_PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
