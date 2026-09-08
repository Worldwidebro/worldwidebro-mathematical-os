"""
KG-028 FastMCP Tool Wrapper — Expose Agent Context Assembly to OmniRoute
"""

import json
from fastmcp import mcp
from _CONTEXT.agent_context_builder import AgentContextBuilder

# Initialize context builder
context_builder = AgentContextBuilder()


@mcp.tool()
def build_agent_context(
    agent_id: str,
    focal_entity_id: str,
    depth: int = 2,
    include_types: str = None,
    exclude_types: str = None,
) -> str:
    """
    Build task-specific context for an agent.

    Args:
        agent_id: Which agent (AGT-001, AGT-005, etc.)
        focal_entity_id: Primary entity to focus on (venture, repo, etc.)
        depth: Relationship hops (1-3)
        include_types: Comma-separated entity types to include
        exclude_types: Comma-separated entity types to exclude

    Returns:
        JSON with entities, relationships, risks, opportunities
    """
    include_list = None
    if include_types:
        include_list = [t.strip() for t in include_types.split(",")]

    exclude_list = None
    if exclude_types:
        exclude_list = [t.strip() for t in exclude_types.split(",")]

    try:
        context = context_builder.build_context(
            agent_id=agent_id,
            focal_entity_id=focal_entity_id,
            depth=depth,
            include_types=include_list,
            exclude_types=exclude_list,
        )

        response = {
            "success": True,
            "agent_id": context.agent_id,
            "focal_entity_id": context.focal_entity_id,
            "focal_entity_type": context.focal_entity_type,
            "depth_limit": context.depth_limit,
            "entity_count": len(context.entities),
            "relationship_count": len(context.relationships),
            "risk_count": len(context.risks),
            "opportunity_count": len(context.opportunities),
            "entities": [
                {
                    "entity_id": e.entity_id,
                    "entity_type": e.entity_type,
                    "distance_hops": e.distance_hops,
                    "confidence_score": e.confidence_score,
                    "properties": e.properties,
                }
                for e in context.entities
            ],
            "relationships": context.relationships,
            "risks": context.risks,
            "opportunities": context.opportunities,
        }

        return json.dumps(response, indent=2)

    except ValueError as e:
        return json.dumps(
            {"success": False, "error": f"Not found: {str(e)}"},
            indent=2,
        )
    except Exception as e:
        return json.dumps(
            {"success": False, "error": str(e)},
            indent=2,
        )


@mcp.resource("company-brain://context/doc")
def context_documentation() -> str:
    """Documentation for agent context assembly"""
    return """
    # KG-028: Agent Context Assembly

    Build relevant subgraph context for agent execution.

    ## What it does
    - Fetches the focal entity (venture, repo, customer)
    - Walks the graph N hops away
    - Filters by entity type
    - Detects risks (dependencies, single-points-of-failure)
    - Detects opportunities (partnerships, synergies)

    ## Example
    ```python
    context = build_agent_context(
        agent_id="AGT-001",  # Venture PM
        focal_entity_id="LT-005",  # HealthRoute Medical Courier
        depth=2,
        include_types="VENTURE,REPOSITORY,CUSTOMER"
    )
    ```

    ## Returns
    - Entities at different distances (with confidence scores)
    - Relationships and their types
    - Detected risks and opportunities
    - Metadata (timestamps, counts)

    ## Use Cases
    - AGT-001 (Venture PM): Context on venture + team + dependencies
    - AGT-002 (Financial): Context on revenue streams + contracts
    - AGT-003 (Technical): Context on tech stack + repos + integrations
    - AGT-004 (Sales): Context on customers + deals + churn signals
    - AGT-005 (Operations): Context on all operational dependencies
    """


if __name__ == "__main__":
    # Test
    print(
        build_agent_context(
            agent_id="AGT-001",
            focal_entity_id="LT-005",
            depth=2,
        )
    )
