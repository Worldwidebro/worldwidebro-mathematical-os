#!/usr/bin/env python3
"""
OmniRoute AI Agent Invocation Layer for DealFlowOS
Enables DealFlowOS agents to invoke research, qualification, and outreach flows via OmniRoute

Authority: Agent Control Plane (CP-006) + Infrastructure Control Plane (CP-027)
"""

import asyncio
import json
import os
import sys
from typing import Optional, AsyncGenerator
from datetime import datetime
from pathlib import Path

OMNIROUTE_URL = os.environ.get("OMNIROUTE_URL", "http://100.87.214.70:20128")


class OmniRouteClient:
    """HTTP client for OmniRoute /chat endpoint with streaming support"""

    def __init__(self, base_url: str = OMNIROUTE_URL):
        self.base_url = base_url.rstrip('/')
        self.chat_endpoint = f"{self.base_url}/api/chat"
        self.health_endpoint = f"{self.base_url}/health"

    async def health_check(self) -> dict:
        """Check OmniRoute health status"""
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(self.health_endpoint, timeout=5) as resp:
                    if resp.status == 200:
                        return {
                            "status": "online",
                            "url": self.base_url,
                            "timestamp": datetime.now().isoformat()
                        }
                    return {
                        "status": "error",
                        "code": resp.status,
                        "message": await resp.text()
                    }
        except Exception as e:
            return {"status": "offline", "error": str(e)}

    async def invoke(
        self,
        query: str,
        model: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        stream: bool = False,
        context: Optional[dict] = None
    ) -> dict:
        """Invoke OmniRoute chat endpoint

        Args:
            query: User query/prompt
            model: Model name (default/qwen-fast/qwen-heavy/claude-sonnet/claude-haiku)
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum response tokens
            stream: Enable streaming responses
            context: Optional context dict with company_data, leads, etc.

        Returns:
            Response dict or async generator for streaming
        """
        try:
            import aiohttp
        except ImportError:
            print("❌ aiohttp not installed. Install with: pip install aiohttp")
            return {"error": "aiohttp required for async HTTP"}

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream
        }

        # Add context if provided
        if context:
            payload["context"] = context

        async with aiohttp.ClientSession() as session:
            if stream:
                return self._invoke_stream(session, payload)
            else:
                return await self._invoke_single(session, payload)

    async def _invoke_single(self, session, payload: dict) -> dict:
        """Single (non-streaming) invocation"""
        try:
            async with session.post(
                self.chat_endpoint,
                json=payload,
                timeout=60
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {
                        "status": "success",
                        "model": payload["model"],
                        "response": data.get("choices", [{}])[0].get("message", {}).get("content", ""),
                        "usage": data.get("usage", {}),
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    error_text = await resp.text()
                    return {
                        "status": "error",
                        "code": resp.status,
                        "message": error_text,
                        "model": payload["model"]
                    }
        except asyncio.TimeoutError:
            return {
                "status": "error",
                "message": "Request timeout",
                "model": payload["model"]
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "model": payload["model"]
            }

    async def _invoke_stream(self, session, payload: dict) -> AsyncGenerator:
        """Streaming invocation - yields chunks as they arrive"""
        try:
            async with session.post(
                self.chat_endpoint,
                json=payload,
                timeout=120
            ) as resp:
                if resp.status == 200:
                    async for line in resp.content:
                        if line:
                            try:
                                chunk = json.loads(line)
                                yield chunk
                            except json.JSONDecodeError:
                                # Skip non-JSON lines (keep-alives, etc.)
                                pass
                else:
                    error_text = await resp.text()
                    yield {
                        "status": "error",
                        "code": resp.status,
                        "message": error_text
                    }
        except Exception as e:
            yield {
                "status": "error",
                "error": str(e)
            }


class DealFlowOSAgents:
    """Agent invocation wrappers for DealFlowOS research, qualification, outreach"""

    def __init__(self, client: Optional[OmniRouteClient] = None):
        self.client = client or OmniRouteClient()
        self.status = {
            "research_agent": {"status": "idle", "last_run": None},
            "qualification_agent": {"status": "idle", "last_run": None},
            "outreach_agent": {"status": "idle", "last_run": None},
            "prospect_sourcing_agent": {"status": "idle", "last_run": None},
            "deal_analysis_agent": {"status": "idle", "last_run": None},
            "outreach_optimization_agent": {"status": "idle", "last_run": None}
        }

    async def invoke_research_agent(
        self,
        query: str,
        company_context: Optional[dict] = None,
        stream: bool = False
    ) -> dict:
        """Research Agent: Gather intelligence on companies, markets, competitors

        Args:
            query: Research question (e.g., "What are the top SaaS companies in healthcare?")
            company_context: Optional company/industry context
            stream: Enable streaming responses

        Returns:
            Research findings with sources and confidence scores
        """
        system_prompt = """You are a deal flow research agent. Your role is to:
1. Gather competitive intelligence
2. Identify market trends and opportunities
3. Research company financials, leadership, capabilities
4. Provide credible, sourced findings with confidence scores

Format findings as structured JSON with: finding, source, confidence (0-1), date."""

        full_query = f"{system_prompt}\n\nQuery: {query}"

        self.status["research_agent"]["status"] = "running"
        self.status["research_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="qwen-heavy",  # Research = complex, use larger model
            temperature=0.3,  # Lower temp for consistency
            max_tokens=3000,
            stream=stream,
            context={"type": "research", "company": company_context}
        )

        self.status["research_agent"]["status"] = "idle"
        return result

    async def invoke_qualification_agent(
        self,
        company_data: dict,
        stream: bool = False
    ) -> dict:
        """Qualification Agent: Score and qualify leads

        Args:
            company_data: Company information dict with: name, revenue, employees, industry, etc.
            stream: Enable streaming responses

        Returns:
            Qualification score (0-100), fit analysis, decision (QUALIFY/MAYBE/REJECT)
        """
        system_prompt = """You are a deal qualification agent. Score and qualify companies based on:
1. Market fit with target customer profile
2. Revenue/growth potential
3. Industry/vertical alignment
4. Competitive positioning
5. Decision urgency signals

Return JSON: {score: 0-100, fit: 0-1, decision: QUALIFY|MAYBE|REJECT, reasons: [str], next_steps: [str]}"""

        full_query = f"{system_prompt}\n\nCompany: {json.dumps(company_data, indent=2)}"

        self.status["qualification_agent"]["status"] = "running"
        self.status["qualification_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="qwen-fast",  # Qualification = fast scoring
            temperature=0.5,
            max_tokens=1500,
            stream=stream,
            context={"type": "qualification", "company": company_data}
        )

        self.status["qualification_agent"]["status"] = "idle"
        return result

    async def invoke_outreach_agent(
        self,
        qualified_leads: list,
        campaign_context: Optional[dict] = None,
        stream: bool = False
    ) -> dict:
        """Outreach Agent: Draft personalized outreach sequences

        Args:
            qualified_leads: List of qualified lead dicts {name, company, role, signals, ...}
            campaign_context: Campaign goals, value props, timeline
            stream: Enable streaming responses

        Returns:
            Outreach sequences with email copy, timing, follow-up cadence
        """
        system_prompt = """You are a deal outreach agent. For each qualified lead, generate:
1. Personalized email subject line (compelling, not salesy)
2. Email body (3-4 short paragraphs, specific to their company/role)
3. Best time to outreach (day/time)
4. Follow-up sequence (3 touches over 2 weeks)
5. LinkedIn engagement hooks (before/after outreach)

Return JSON array: [{lead_name, email_subject, email_body, timing, followups, engagement_hooks}]"""

        full_query = f"{system_prompt}\n\nLeads:\n{json.dumps(qualified_leads[:5], indent=2)}\n\nContext: {json.dumps(campaign_context or {}, indent=2)}"

        self.status["outreach_agent"]["status"] = "running"
        self.status["outreach_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="default",  # Outreach = balanced performance/cost
            temperature=0.7,  # Higher for creativity
            max_tokens=4000,
            stream=stream,
            context={"type": "outreach", "lead_count": len(qualified_leads)}
        )

        self.status["outreach_agent"]["status"] = "idle"
        return result

    async def invoke_prospect_sourcing_agent(
        self,
        ideal_customer_profile: dict,
        stream: bool = False
    ) -> dict:
        """Prospect Sourcing: Identify and list target companies

        Args:
            ideal_customer_profile: ICP dict with: industry, size, revenue_range, geography, etc.
            stream: Enable streaming responses

        Returns:
            List of 20-50 target companies with contact info and signals
        """
        system_prompt = """You are a prospect sourcing agent. Based on the ICP, identify:
1. Top 20-50 companies matching the profile
2. Key decision-makers (titles, names if available)
3. Buying signals (recent funding, acquisitions, partnerships, hiring)
4. Contact information (LinkedIn, email patterns)
5. Engagement hooks (recent news, industry trends relevant to them)

Return structured JSON with: company_name, website, employees, revenue, hq_location, contacts, signals"""

        full_query = f"{system_prompt}\n\nICP:\n{json.dumps(ideal_customer_profile, indent=2)}"

        self.status["prospect_sourcing_agent"]["status"] = "running"
        self.status["prospect_sourcing_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="qwen-heavy",
            temperature=0.6,
            max_tokens=5000,
            stream=stream,
            context={"type": "sourcing", "icp": ideal_customer_profile}
        )

        self.status["prospect_sourcing_agent"]["status"] = "idle"
        return result

    async def invoke_deal_analysis_agent(
        self,
        deal_data: dict,
        stream: bool = False
    ) -> dict:
        """Deal Analysis: Analyze deal health, risk, and trajectory

        Args:
            deal_data: Deal dict with: company, value, stage, timeline, competitors, etc.
            stream: Enable streaming responses

        Returns:
            Deal health score, risk assessment, probability forecast, recommended actions
        """
        system_prompt = """You are a deal analysis agent. Analyze the deal on:
1. Deal health (0-100 score)
2. Risk factors (competitive, technical, financial, organizational)
3. Win probability (0-100%)
4. Decision timeline and milestones
5. Recommended actions (by priority)

Return JSON: {health_score, risk_level, win_probability, risks: [{name, severity}], actions: [{priority, action}]}"""

        full_query = f"{system_prompt}\n\nDeal:\n{json.dumps(deal_data, indent=2)}"

        self.status["deal_analysis_agent"]["status"] = "running"
        self.status["deal_analysis_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="qwen-fast",
            temperature=0.4,
            max_tokens=2000,
            stream=stream,
            context={"type": "deal_analysis", "deal": deal_data}
        )

        self.status["deal_analysis_agent"]["status"] = "idle"
        return result

    async def invoke_outreach_optimization_agent(
        self,
        campaign_results: dict,
        stream: bool = False
    ) -> dict:
        """Outreach Optimization: Learn from campaign results, suggest improvements

        Args:
            campaign_results: Campaign metrics {opens, clicks, replies, conversions, timing_data, content_performance}
            stream: Enable streaming responses

        Returns:
            Optimization recommendations, A/B test ideas, timing insights, content improvements
        """
        system_prompt = """You are an outreach optimization agent. Analyze campaign performance and suggest:
1. Best performing elements (subject lines, body styles, timing, channels)
2. A/B test recommendations (what to test next)
3. Timing optimization (best days/times by segment)
4. Content improvements (tone, length, call-to-action)
5. Sequencing adjustments (follow-up cadence, touch count)

Return JSON: {winning_patterns: [str], ab_tests: [{control, variant, hypothesis}], timing_insights: {}, improvements: [str]}"""

        full_query = f"{system_prompt}\n\nCampaign Results:\n{json.dumps(campaign_results, indent=2)}"

        self.status["outreach_optimization_agent"]["status"] = "running"
        self.status["outreach_optimization_agent"]["last_run"] = datetime.now().isoformat()

        result = await self.client.invoke(
            query=full_query,
            model="qwen-fast",
            temperature=0.5,
            max_tokens=2000,
            stream=stream,
            context={"type": "optimization", "metrics": campaign_results}
        )

        self.status["outreach_optimization_agent"]["status"] = "idle"
        return result

    def get_agent_status(self) -> dict:
        """Get status of all 6 agents"""
        return {
            "timestamp": datetime.now().isoformat(),
            "omniroute_url": OMNIROUTE_URL,
            "agents": self.status,
            "agent_count": len(self.status),
            "online_agents": sum(1 for a in self.status.values() if a["status"] == "idle")
        }


async def main():
    """Demo: List agents and check health"""
    client = OmniRouteClient()
    agents = DealFlowOSAgents(client)

    # Check health
    health = await client.health_check()
    print(f"OmniRoute Health: {json.dumps(health, indent=2)}")

    # Show agent status
    status = agents.get_agent_status()
    print(f"\nAgent Status:\n{json.dumps(status, indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())
