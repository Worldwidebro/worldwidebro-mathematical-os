import { useEffect, useState } from 'react';

interface Agent {
  id: string;
  name: string;
  role: string;
  status: 'active' | 'idle' | 'error';
  confidence: number;
}

export function useNeo4jAgents() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetch() {
      try {
        const res = await fetch('/api/neo4j/agents');
        const data = await res.json();
        setAgents(data.agents || []);
      } catch (err) {
        console.error('Neo4j agents fetch failed:', err);
      } finally {
        setLoading(false);
      }
    }
    fetch();
  }, []);

  return { agents, loading };
}
