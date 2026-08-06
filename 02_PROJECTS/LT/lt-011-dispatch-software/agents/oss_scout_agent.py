import os
import re
import json
import asyncio
import logging
from typing import Dict, Any, List
from pydantic import BaseModel
from llm_gateway import LLMGateway
from neo4j import GraphDatabase

logger = logging.getLogger("OSSScoutAgent")

# 1. Pydantic structured output model matching output_schema.md
class OSSScoutDecision(BaseModel):
    selected_repo_name: str
    suitability_score: float
    license_type: str
    docker_available: bool
    integration_path: str
    reasoning: str

class OSSScoutAgent:
    def __init__(self, name: str = "oss_scout", model: str = "gemini-1.5-flash"):
        self.name = name
        self.model = model
        self.prompt_dir = os.path.join(os.path.dirname(__file__), "oss_scout")
        
        # Load markdown files
        self.system_prompt = self._load_md("system_prompt.md")
        self.output_schema = self._load_json_schema("output_schema.md")
        
        # Initialize gateway
        self.llm_gateway = LLMGateway(primary_model=self.model)

    def _load_md(self, filename: str) -> str:
        filepath = os.path.join(self.prompt_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def _load_json_schema(self, filename: str) -> Dict[str, Any]:
        content = self._load_md(filename)
        match = re.search(r"```json\s*\n(.*?)```", content, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        raise ValueError(f"Could not parse JSON block from {filename}")

    async def scout_and_index(self, capability_gap: str, candidates: List[Dict[str, Any]], db_driver: Optional[GraphDatabase] = None) -> OSSScoutDecision:
        logger.info(f"Scouting candidates for capability gap: '{capability_gap}'...")

        # Inject context into user prompt
        user_prompt = f"""
Target Capability Gap: "{capability_gap}"
Candidates List:
{json.dumps(candidates, indent=2)}
"""

        # Execute reasoning call via LLM Gateway harness
        # We override the mock endpoint in _call_llm_api inside llm_gateway dynamically by adding case matching
        decision = await self.llm_gateway.generate_structured(
            load_id=f"gap-{capability_gap}",
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
            response_model=OSSScoutDecision
        )

        logger.info(f"Scout evaluation finished. Selected: {decision.selected_repo_name} | Score: {decision.suitability_score}")

        # If a live Neo4j driver is passed, write the relationship node
        if db_driver and decision.selected_repo_name:
            await self._index_to_neo4j(db_driver, capability_gap, decision)

        return decision

    async def _index_to_neo4j(self, driver, gap: str, decision: OSSScoutDecision):
        logger.info(f"Indexing OSS project {decision.selected_repo_name} into Neo4j graph...")
        try:
            with driver.session() as session:
                session.run("""
                    MERGE (o:OpenSourceProject {id: $repo_name})
                    SET o.name = $repo_name,
                        o.suitability_score = $score,
                        o.license = $license,
                        o.docker = $docker,
                        o.integration = $integration,
                        o.updated_at = datetime()
                    WITH o
                    MERGE (c:Capability {name: $gap})
                    MERGE (o)-[r:PROVIDES]->(c)
                    SET r.updated_at = datetime()
                """, {
                    "repo_name": decision.selected_repo_name,
                    "score": decision.suitability_score,
                    "license": decision.license_type,
                    "docker": decision.docker_available,
                    "integration": decision.integration_path,
                    "gap": gap
                })
            logger.info("Successfully indexed in Neo4j.")
        except Exception as e:
            logger.warning(f"Neo4j indexing bypassed/failed: {e}")
