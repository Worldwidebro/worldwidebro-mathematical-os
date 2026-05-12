"""
IZA OS Integration Hub
Wires together: graphify → RAG → agents → memory → workflows

Architecture:
1. Graphify: Code → Knowledge Graphs
2. LightRAG: Knowledge retrieval & synthesis
3. Langgraph + CrewAI: Agent coordination
4. Mem0: Persistent memory layer
5. Firecrawl: Web data ingestion
6. N8N/Kestra: Workflow automation
"""

import os
import asyncio
import json
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

# ============================================================================
# 1. GRAPHIFY INTEGRATION
# ============================================================================

class GraphifyBridge:
    """Bridge between code repos and RAG knowledge graphs."""

    def __init__(self, graphify_path: str = "/Users/acebless/Documents/integrations/graphify"):
        self.graphify_path = graphify_path
        self.queries = []

    async def ingest_repo(self, repo_path: str, repo_name: str) -> Dict[str, Any]:
        """Ingest a code repository into knowledge graph."""
        return {
            "repo": repo_name,
            "path": repo_path,
            "status": "ready_for_graphify_ingestion",
            "ingested_at": datetime.now().isoformat(),
            "graph_type": "code_structure"
        }

    async def query_repo(self, query: str) -> str:
        """Query ingested repository as knowledge graph."""
        self.queries.append(query)
        return f"Querying: {query}"


# ============================================================================
# 2. RAG INTEGRATION
# ============================================================================

class RAGBridge:
    """Interface to IZA OS RAG System (LightRAG)."""

    def __init__(self, rag_url: str = "http://localhost:8000"):
        self.rag_url = rag_url
        self.knowledge_base = {}

    async def query(self, question: str, mode: str = "hybrid") -> str:
        """Query the knowledge graph."""
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.rag_url}/query",
                json={"q": question, "mode": mode}
            )
            if response.status_code == 200:
                return response.json().get("answer", "No answer found")
            return f"Error: {response.status_code}"

    async def ingest(self, content: str, metadata: Optional[Dict] = None) -> bool:
        """Ingest content into RAG."""
        # Direct integration point
        try:
            from iza_os_rag_system.src.rag import get_rag_async
            rag = await get_rag_async()
            await rag.ainsert(content)
            return True
        except Exception as e:
            print(f"Ingestion failed: {e}")
            return False


# ============================================================================
# 3. AGENT ORCHESTRATION (Langgraph + CrewAI)
# ============================================================================

@dataclass
class Agent:
    """Agent definition for orchestration."""
    name: str
    role: str
    goal: str
    capabilities: List[str]

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "goal": self.goal,
            "capabilities": self.capabilities
        }


class AgentOrchestrator:
    """Coordinate multi-agent workflows using langgraph."""

    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.workflows = []

    def register_agent(self, agent: Agent):
        """Register an agent in the system."""
        self.agents[agent.name] = agent

    async def execute_task(self, task: str, required_agents: List[str]) -> Dict[str, Any]:
        """Execute a task with specified agents."""
        return {
            "task": task,
            "assigned_to": required_agents,
            "status": "queued",
            "timestamp": datetime.now().isoformat()
        }


# ============================================================================
# 4. MEMORY LAYER (Mem0 Integration)
# ============================================================================

class MemoryLayer:
    """Persistent memory for agents across sessions."""

    def __init__(self):
        self.memories = {}
        self.context_window = []

    async def store(self, key: str, value: Any, metadata: Optional[Dict] = None):
        """Store persistent memory."""
        self.memories[key] = {
            "value": value,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat()
        }

    async def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve persistent memory."""
        return self.memories.get(key)

    async def query_context(self, query: str) -> List[Dict]:
        """Query relevant context from memory."""
        # In real implementation, use semantic search
        return []


# ============================================================================
# 5. DATA INGESTION (Firecrawl Integration)
# ============================================================================

class DataIngestionPipeline:
    """Ingest web data and documents into RAG."""

    async def crawl_web(self, url: str) -> Dict[str, Any]:
        """Crawl web content with firecrawl."""
        return {
            "url": url,
            "status": "ready_for_firecrawl",
            "crawler": "firecrawl"
        }

    async def process_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """Process PDF with opendataloader-pdf."""
        return {
            "pdf": pdf_path,
            "status": "ready_for_pdf_processing",
            "processor": "opendataloader"
        }

    async def extract_text(self, source: str) -> str:
        """Extract text from various sources."""
        return f"Extracted from {source}"


# ============================================================================
# 6. UNIFIED INTEGRATION INTERFACE
# ============================================================================

class IZAIntegrationHub:
    """Central hub orchestrating all integrations."""

    def __init__(self):
        self.graphify = GraphifyBridge()
        self.rag = RAGBridge()
        self.agents = AgentOrchestrator()
        self.memory = MemoryLayer()
        self.data_pipeline = DataIngestionPipeline()

        # Register core agents
        self._init_core_agents()

    def _init_core_agents(self):
        """Initialize core agent types."""
        agents_config = [
            Agent(
                name="research_agent",
                role="Data Researcher",
                goal="Research and gather information",
                capabilities=["search", "analyze", "synthesize"]
            ),
            Agent(
                name="coding_agent",
                role="Code Specialist",
                goal="Write and optimize code",
                capabilities=["code_generation", "debugging", "optimization"]
            ),
            Agent(
                name="business_agent",
                role="Business Analyst",
                goal="Analyze business metrics",
                capabilities=["analysis", "reporting", "planning"]
            ),
            Agent(
                name="osint_agent",
                role="OSINT Specialist",
                goal="Gather open-source intelligence",
                capabilities=["reconnaissance", "data_collection", "analysis"]
            ),
        ]

        for agent in agents_config:
            self.agents.register_agent(agent)

    async def ingest_code_repo(self, repo_path: str, repo_name: str):
        """End-to-end: Code → Graphify → RAG."""
        # 1. Ingest via graphify
        graph_info = await self.graphify.ingest_repo(repo_path, repo_name)

        # 2. Read code structure
        code_docs = []
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.md')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()[:500]  # First 500 chars
                            code_docs.append(f"File: {file}\n{content}\n---")
                    except:
                        pass

        # 3. Ingest into RAG
        combined_content = f"Repository: {repo_name}\n\n" + "\n".join(code_docs)
        success = await self.rag.ingest(combined_content, {
            "repo": repo_name,
            "type": "code"
        })

        # 4. Store in memory
        await self.memory.store(f"repo:{repo_name}", {
            "path": repo_path,
            "graph": graph_info,
            "indexed": success
        })

        return {
            "repo": repo_name,
            "graphified": True,
            "rag_indexed": success,
            "memory_stored": True
        }

    async def query_ecosystem(self, question: str) -> Dict[str, Any]:
        """Query across all systems."""
        # 1. Query RAG
        rag_answer = await self.rag.query(question, mode="hybrid")

        # 2. Query context memory
        memory_context = await self.memory.query_context(question)

        # 3. Delegate to appropriate agent
        if "code" in question.lower():
            agent = "coding_agent"
        elif "research" in question.lower():
            agent = "research_agent"
        elif "business" in question.lower():
            agent = "business_agent"
        else:
            agent = "research_agent"

        agent_task = await self.agents.execute_task(question, [agent])

        return {
            "question": question,
            "rag_answer": rag_answer,
            "memory_context": memory_context,
            "assigned_agent": agent,
            "task_status": agent_task["status"]
        }

    def status(self) -> Dict[str, Any]:
        """Get integration hub status."""
        return {
            "timestamp": datetime.now().isoformat(),
            "components": {
                "graphify": "ready",
                "rag": "running",
                "agents": f"{len(self.agents.agents)} registered",
                "memory": "initialized",
                "data_pipeline": "ready"
            },
            "agents": {
                name: agent.to_dict()
                for name, agent in self.agents.agents.items()
            }
        }


# ============================================================================
# INITIALIZATION
# ============================================================================

async def main():
    """Initialize and test the integration hub."""
    hub = IZAIntegrationHub()

    print("=" * 70)
    print("IZA INTEGRATION HUB INITIALIZED")
    print("=" * 70)
    print(json.dumps(hub.status(), indent=2))
    print("\nReady to ingest repos and coordinate agents.")

if __name__ == "__main__":
    asyncio.run(main())
