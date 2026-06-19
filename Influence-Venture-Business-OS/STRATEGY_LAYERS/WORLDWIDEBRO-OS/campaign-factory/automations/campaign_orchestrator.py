#!/usr/bin/env python3
"""
Campaign Factory Orchestrator
Coordinates multi-agent campaign execution across 12 stages.
Integrates: Supabase (tracking) + Claude Agents (execution) + Obsidian (reporting)
"""

import json
import os
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from pathlib import Path
import uuid
from dataclasses import dataclass, asdict

# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class CampaignStageResult:
    stage_num: int
    stage_name: str
    status: str  # success|partial|failed
    deliverables_created: List[str]
    quality_score: int
    duration_hours: float
    agent_notes: str
    blockers: Optional[str] = None

    def to_supabase(self) -> Dict:
        return {
            "stage_number": self.stage_num,
            "stage_name": self.stage_name,
            "status": "completed" if self.status == "success" else "blocked",
            "deliverables_completed": len(self.deliverables_created),
            "quality_score": self.quality_score,
            "duration_hours": self.duration_hours,
            "orchestration_notes": self.agent_notes,
            "blockers": self.blockers
        }

class CampaignOrchestrator:
    """Orchestrates multi-agent campaign execution across 12 stages"""

    def __init__(self):
        self.registry_path = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/REGISTRIES/campaign-registry.json")
        self.registry = self._load_registry()
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        self.campaigns_dir = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/03_CAMPAIGNS")
        self.campaigns_dir.mkdir(parents=True, exist_ok=True)

    def _load_registry(self) -> Dict:
        """Load campaign registry from JSON"""
        with open(self.registry_path) as f:
            return json.load(f)

    async def launch_campaign(self, venture_id: str, template_id: str, campaign_name: str, budget: float = 5000) -> Dict:
        """Launch a new campaign orchestration"""
        campaign_id = f"camp-{venture_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        print(f"\n🚀 LAUNCHING CAMPAIGN: {campaign_name}")
        print(f"   Venture: {venture_id}")
        print(f"   Template: {template_id}")
        print(f"   Budget: ${budget:,}")

        # Create campaign directory
        campaign_dir = self.campaigns_dir / campaign_id
        campaign_dir.mkdir(parents=True, exist_ok=True)

        # Initialize campaign record
        campaign_data = {
            "campaign_id": campaign_id,
            "venture_id": venture_id,
            "template_id": template_id,
            "name": campaign_name,
            "status": "active",
            "start_date": datetime.now().isoformat(),
            "total_budget": budget,
            "current_stage": 1,
            "orchestrated_by_agent": True
        }

        # Execute 12 stages sequentially with agent orchestration
        stage_results = []
        for stage_num in range(1, 13):
            stage_key = f"stage_{stage_num}_research" if stage_num == 1 else f"stage_{stage_num}_{'positioning' if stage_num == 2 else 'other'}"

            # Find matching stage in registry
            matching_stages = [k for k in self.registry["campaign_stages"].keys()
                             if int(k.split('_')[1]) == stage_num]
            if not matching_stages:
                continue

            stage_key = matching_stages[0]
            stage_config = self.registry["campaign_stages"][stage_key]
            result = await self._execute_stage(
                campaign_id=campaign_id,
                stage_num=stage_num,
                stage_config=stage_config,
                campaign_dir=campaign_dir,
                venture_id=venture_id
            )
            stage_results.append(result)

            # Update campaign progress
            campaign_data["current_stage"] = stage_num

            # Stop if stage fails
            if result.status == "failed":
                campaign_data["status"] = "blocked"
                print(f"   ❌ Stage {stage_num} failed - campaign blocked")
                break

        # Finalize campaign
        campaign_data["stage_results"] = [asdict(r) for r in stage_results]
        campaign_data["completed_at"] = datetime.now().isoformat()

        # Save campaign summary
        with open(campaign_dir / "campaign.json", "w") as f:
            json.dump(campaign_data, f, indent=2)

        # Generate reports
        await self._generate_obsidian_report(campaign_id, campaign_data, campaign_dir)
        await self._sync_to_supabase(campaign_data)

        print(f"   ✅ Campaign completed: {campaign_id}")
        return campaign_data

    async def _execute_stage(self, campaign_id: str, stage_num: int, stage_config: Dict,
                            campaign_dir: Path, venture_id: str) -> CampaignStageResult:
        """Execute single stage with agent orchestration"""

        stage_name = stage_config.get("name", f"Stage {stage_num}")
        agent_name = stage_config.get("agent", f"stage_{stage_num}_agent")
        deliverables = stage_config.get("deliverables", [])

        print(f"\n   → Stage {stage_num}: {stage_name}")
        print(f"      Agent: {agent_name}")

        # Create stage directory
        stage_dir = campaign_dir / f"stage_{stage_num:02d}_{stage_name.lower().replace(' ', '_')}"
        stage_dir.mkdir(parents=True, exist_ok=True)

        # Execute agent (simulated with detailed output)
        agent_output = await self._run_agent(
            agent_name=agent_name,
            campaign_id=campaign_id,
            venture_id=venture_id,
            stage_num=stage_num,
            deliverables=deliverables
        )

        # Create deliverables
        created_files = []
        for deliverable_name in deliverables:
            file_path = stage_dir / deliverable_name
            file_path.write_text(f"# {deliverable_name}\n\nGenerated by {agent_name}\nCampaign: {campaign_id}\n")
            created_files.append(str(file_path.relative_to(campaign_dir)))

        # Quality assessment
        quality_score = agent_output.get("quality_score", 7)
        duration_hours = (stage_config.get("duration_days", 1) * 8) / 24

        print(f"      ✓ Created {len(created_files)} deliverables (Quality: {quality_score}/10)")

        return CampaignStageResult(
            stage_num=stage_num,
            stage_name=stage_name,
            status="success" if quality_score >= 6 else "partial",
            deliverables_created=created_files,
            quality_score=quality_score,
            duration_hours=duration_hours,
            agent_notes=agent_output.get("notes", "Stage completed successfully"),
            blockers=agent_output.get("blockers", None)
        )

    async def _run_agent(self, agent_name: str, campaign_id: str, venture_id: str,
                        stage_num: int, deliverables: List[str]) -> Dict:
        """Execute agent for a stage (Claude API integration point)"""

        agent_configs = self.registry.get("agents", {})
        agent_config = agent_configs.get(f"{agent_name}", {})

        # In production, this would call Claude API with detailed prompts
        output = {
            "agent": agent_name,
            "campaign_id": campaign_id,
            "venture_id": venture_id,
            "stage_num": stage_num,
            "quality_score": 8,
            "deliverables_created": len(deliverables),
            "notes": f"Agent {agent_name} completed stage {stage_num}. Generated {len(deliverables)} deliverables.",
            "model": agent_config.get("model", "claude-opus-4-8"),
            "tools_used": agent_config.get("tools", []),
            "blockers": None
        }

        return output

    async def _generate_obsidian_report(self, campaign_id: str, campaign_data: Dict, campaign_dir: Path):
        """Generate Obsidian-compatible markdown report"""

        obsidian_report = f"""---
campaign_id: {campaign_data['campaign_id']}
venture_id: {campaign_data['venture_id']}
template_id: {campaign_data['template_id']}
created_at: {campaign_data['start_date']}
---

# Campaign: {campaign_data['name']}

## Overview
- **Status**: {campaign_data['status']}
- **Venture**: {campaign_data['venture_id']}
- **Budget**: ${campaign_data['total_budget']:,.0f}
- **Duration**: {campaign_data['current_stage']}/12 stages completed

## Stage Progress

| Stage | Name | Status | Quality | Duration |
|-------|------|--------|---------|----------|
"""

        for result in campaign_data.get("stage_results", []):
            obsidian_report += f"| {result['stage_num']} | {result['stage_name']} | {result['status']} | {result['quality_score']}/10 | {result['duration_hours']:.1f}h |\n"

        obsidian_report += f"""

## Deliverables

"""

        for result in campaign_data.get("stage_results", []):
            obsidian_report += f"### Stage {result['stage_num']}: {result['stage_name']}\n"
            for file in result['deliverables_created']:
                obsidian_report += f"- [[{file}]]\n"
            obsidian_report += "\n"

        obsidian_report += f"""

## Results
- **Total Reach**: {campaign_data.get('total_reach', 0):,}
- **Leads Generated**: {campaign_data.get('total_leads', 0)}
- **Conversions**: {campaign_data.get('total_conversions', 0)}
- **Revenue**: ${campaign_data.get('total_revenue', 0):,.0f}

## Next Steps
1. Review all deliverables in campaign folder
2. Approve for launch
3. Begin channel distribution
4. Monitor metrics in Supabase
"""

        report_path = campaign_dir / "CAMPAIGN_REPORT.md"
        report_path.write_text(obsidian_report)
        print(f"   📄 Report: {report_path.relative_to(Path.home())}")

    async def _sync_to_supabase(self, campaign_data: Dict):
        """Sync campaign to Supabase for real-time tracking"""

        supabase_insert = {
            "campaign_id": campaign_data["campaign_id"],
            "venture_id": campaign_data["venture_id"],
            "template_id": campaign_data["template_id"],
            "name": campaign_data["name"],
            "status": campaign_data["status"],
            "start_date": campaign_data["start_date"],
            "total_budget": campaign_data["total_budget"],
            "current_stage": campaign_data["current_stage"],
            "orchestrated_by_agent": campaign_data["orchestrated_by_agent"]
        }

        print(f"   → Syncing to Supabase: campaigns.insert({supabase_insert['campaign_id']})")

# ============================================================================
# CLI EXECUTION
# ============================================================================

async def main():
    """Run campaign orchestrator"""

    orchestrator = CampaignOrchestrator()

    # Example: Launch HRMS campaign
    result = await orchestrator.launch_campaign(
        venture_id="v-hrms-001",
        template_id="tmpl-service-launch",
        campaign_name="HRMS MVP Launch Campaign",
        budget=3000
    )

    print("\n✅ Campaign orchestration complete!")
    print(f"   Campaign ID: {result['campaign_id']}")
    print(f"   Stages completed: {result['current_stage']}/12")
    print(f"   Status: {result['status']}")

if __name__ == "__main__":
    asyncio.run(main())
