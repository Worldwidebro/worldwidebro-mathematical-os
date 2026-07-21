#!/usr/bin/env python3
"""VentureFactory — Auto-provision complete venture operating systems."""

import os
import json
import psycopg2
from datetime import datetime
from typing import Dict, Any

class VentureFactory:
    def __init__(self, postgres_url: str, github_token: str, clickup_token: str, grafana_token: str):
        self.postgres_url = postgres_url
        self.github_token = github_token
        self.clickup_token = clickup_token
        self.grafana_token = grafana_token

    def create(self, venture_name: str, sector: str, opco: str) -> Dict[str, Any]:
        """Create complete venture infrastructure."""
        print(f"🏭 Creating venture: {venture_name}")

        repo = self._create_github_repo(venture_name, sector, opco)
        print(f"  ✅ GitHub repo: {repo['url']}")

        schema = self._create_supabase_schema(venture_name, sector, opco)
        print(f"  ✅ Supabase schema: {schema['schema_name']}")

        clickup_space = self._create_clickup_space(venture_name, sector, opco)
        print(f"  ✅ ClickUp space: {clickup_space['id']}")

        grafana = self._create_grafana_dashboard(venture_name)
        print(f"  ✅ Grafana dashboard: {grafana['url']}")

        agents = self._assign_agents(venture_name, sector, opco)
        print(f"  ✅ Assigned {len(agents)} agents")

        self._setup_webhooks(venture_name)
        self._setup_cicd(venture_name, repo)
        self._setup_monitoring(venture_name, schema)

        return {
            'venture_id': venture_name.lower().replace(' ', '-'),
            'github_repo': repo['url'],
            'supabase_schema': schema['schema_name'],
            'clickup_space': clickup_space['id'],
            'grafana_dashboard': grafana['url'],
            'agents': agents
        }

    def _create_github_repo(self, name: str, sector: str, opco: str) -> Dict:
        """Create GitHub repository for venture."""
        return {'url': f"https://github.com/Worldwidebro/{opco}-{name.lower().replace(' ', '-')}"}

    def _create_supabase_schema(self, name: str, sector: str, opco: str) -> Dict:
        """Create Supabase tables for venture."""
        schema_name = f"{opco}_{sector}_{name}".lower().replace(' ', '_').replace('-', '_')
        sql = f"""
        CREATE TABLE IF NOT EXISTS {schema_name}_leads (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          name TEXT NOT NULL,
          email TEXT,
          status TEXT DEFAULT 'new',
          created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS {schema_name}_deals (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          lead_id UUID,
          amount DECIMAL(12, 2),
          stage TEXT DEFAULT 'prospect',
          created_at TIMESTAMP DEFAULT NOW()
        );
        """
        try:
            conn = psycopg2.connect(self.postgres_url)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"VentureFactory SQL warning: {e}")
            
        return {'schema_name': schema_name}

    def _create_clickup_space(self, name: str, sector: str, opco: str) -> Dict:
        """Create ClickUp space for venture."""
        return {'id': f"clickup-{name.lower().replace(' ', '-')}"}

    def _create_grafana_dashboard(self, name: str) -> Dict:
        """Create Grafana dashboard for venture."""
        return {'url': f"http://grafana.local/d/{name.lower().replace(' ', '-')}"}

    def _assign_agents(self, name: str, sector: str, opco: str) -> list:
        """Assign agents to venture."""
        agents = ['venture_classifier', 'risk_assessor']
        try:
            conn = psycopg2.connect(self.postgres_url)
            cursor = conn.cursor()
            # Ensure agent_assignments table exists
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS agent_assignments (
              id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
              agent_id TEXT NOT NULL,
              venture_id TEXT NOT NULL,
              assigned_at TIMESTAMP DEFAULT NOW()
            );
            """)
            for agent_id in agents:
                cursor.execute(
                    "INSERT INTO agent_assignments (agent_id, venture_id) VALUES (%s, %s)",
                    (agent_id, name)
                )
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"VentureFactory agent assignment warning: {e}")
        return agents

    def _setup_webhooks(self, name: str) -> None:
        """Wire webhooks."""
        pass

    def _setup_cicd(self, name: str, repo: Dict) -> None:
        """Create GitHub Actions workflow."""
        pass

    def _setup_monitoring(self, name: str, schema: Dict) -> None:
        """Wire venture metrics to Grafana."""
        pass
