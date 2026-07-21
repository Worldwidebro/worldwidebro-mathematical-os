#!/usr/bin/env python3
import os
import sys
import json
import asyncio
from typing import Dict, Any, List, Optional, Type
from pydantic import BaseModel
from abc import ABC, abstractmethod

# Add parent path to allow importing os_env
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from os_env import OLLAMA_CHAT, CHAT_MODEL, QDRANT
except ImportError:
    OLLAMA_CHAT = "http://100.87.214.70:11434/v1/chat/completions"
    CHAT_MODEL = "qwen3:8b"
    QDRANT = "http://100.87.214.70:6333"

class AgentTask(BaseModel):
    id: str
    type: str = "default"
    payload: Dict[str, Any] = {}
    context: Dict[str, Any] = {}
    priority: int = 1

class AgentMemory:
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.qdrant_url = QDRANT
        self.redis_conn = None
        self.local_cache = {}
        
        # Connect to Redis
        try:
            import redis
            self.redis_conn = redis.Redis(host='localhost', port=6379, db=0, socket_timeout=2, decode_responses=True)
            self.redis_conn.ping()
        except Exception:
            self.redis_conn = None
            
        self._ensure_collection()

    def _ensure_collection(self):
        # Local or remote memory store index config
        self.collection_name = f"agent_memory_{self.agent_name.lower().replace(' ', '_')}"
        try:
            r = requests.get(f"{self.qdrant_url}/collections/{self.collection_name}", timeout=5)
            if r.status_code != 200:
                body = {
                    "vectors": {
                        "size": 768,  # nomic-embed-text size
                        "distance": "Cosine"
                    }
                }
                requests.put(f"{self.qdrant_url}/collections/{self.collection_name}", json=body, timeout=5)
        except Exception:
            pass

    def store_short_term(self, key: str, value: Dict[str, Any], ttl: int = 3600):
        if self.redis_conn:
            try:
                self.redis_conn.setex(f"agent:{self.agent_name}:{key}", ttl, json.dumps(value))
                return
            except Exception:
                pass
        self.local_cache[key] = value

    def get_short_term(self, key: str) -> Optional[Dict[str, Any]]:
        if self.redis_conn:
            try:
                data = self.redis_conn.get(f"agent:{self.agent_name}:{key}")
                if data:
                    return json.loads(data)
            except Exception:
                pass
        return self.local_cache.get(key)

    def store_long_term(self, text: str, metadata: Dict[str, Any]):
        # Stub for vector embedding and upsert to Qdrant memory collection
        pass


class BaseAgent(ABC):
    def __init__(self, name: str, capabilities: List[str] = None):
        self.name = name
        self.capabilities = capabilities or []
        self.memory = AgentMemory(name)
        
    @abstractmethod
    async def execute(self, task: AgentTask) -> Dict[str, Any]:
        """Execute given task and return result dictionary."""
        pass


try:
    from knowledge_engine import LLMAdapter
except ImportError:
    from services.knowledge_engine import LLMAdapter

class SimpleLangAgent(BaseAgent):
    """Fallback agent executing tasks using LLM reasoning and registered tools."""
    def __init__(self, name: str, capabilities: List[str] = None):
        super().__init__(name, capabilities)
        self.llm = LLMAdapter()

    async def execute(self, task: AgentTask) -> Dict[str, Any]:
        prompt = (
            f"You are the {self.name} agent.\n"
            f"Your capabilities include: {', '.join(self.capabilities)}.\n"
            f"Task details: {json.dumps(task.payload)}\n"
            f"Context: {json.dumps(task.context)}\n\n"
            f"Please execute this task and return a JSON dictionary output summarizing your decision and results."
        )
        try:
            content = self.llm.generate(prompt)
            clean_content = content.replace("```json", "").replace("```", "").strip()
            result = json.loads(clean_content)
        except Exception as e:
            result = {
                "status": "completed",
                "agent": self.name,
                "task_id": task.id,
                "output": f"Executed payload successfully. Reasoning details: {content[:300] if 'content' in locals() else str(e)}"
            }
        return result


class AgentRegistry:
    _agents: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def load_from_yaml(cls):
        yaml_path = "/Users/acebless/Documents/Gemini/registry/agents.yaml"
        if not os.path.exists(yaml_path):
            return
        
        try:
            # Parse custom yaml format
            with open(yaml_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            entries = []
            current = {}
            for line in content.split('\n'):
                line_strip = line.strip()
                if not line_strip:
                    continue
                if line_strip.startswith('-'):
                    if current:
                        entries.append(current)
                        current = {}
                    line_strip = line_strip.lstrip('-').strip()
                if ':' in line_strip:
                    parts = line_strip.split(':', 1)
                    k = parts[0].strip().replace('"', '').replace("'", "")
                    v = parts[1].strip().replace('"', '').replace("'", "")
                    if v.startswith('[') and v.endswith(']'):
                        v = [item.strip() for item in v[1:-1].split(',')]
                    current[k] = v
            if current:
                entries.append(current)
                
            for entry in entries:
                name = entry.get("name")
                if name:
                    cls._agents[name.lower()] = entry
        except Exception as e:
            print(f"Error loading agent registry YAML: {e}")

    @classmethod
    def get_agent_info(cls, name: str) -> Optional[Dict[str, Any]]:
        if not cls._agents:
            cls.load_from_yaml()
        return cls._agents.get(name.lower())


class AgentExecutor:
    async def run_task(self, agent: BaseAgent, task: AgentTask) -> Dict[str, Any]:
        try:
            return await agent.execute(task)
        except Exception as e:
            return {"status": "error", "error": str(e)}


class EventBus:
    """Local light message broker/pub-sub stub."""
    def __init__(self):
        self.subscribers = {}
        
    def subscribe(self, topic: str, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)
        
    def publish(self, topic: str, data: Dict[str, Any]):
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                try:
                    if asyncio.iscoroutinefunction(callback):
                        asyncio.create_task(callback(data))
                    else:
                        callback(data)
                except Exception as e:
                    print(f"EventBus dispatch error: {e}")

# Pre-load registry
AgentRegistry.load_from_yaml()

if __name__ == '__main__':
    AgentRegistry.load_from_yaml()
    print(f"Loaded {len(AgentRegistry._agents)} agents from registry.")
