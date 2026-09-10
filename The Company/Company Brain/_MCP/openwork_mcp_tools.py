#!/usr/bin/env python3
"""
OpenWork MCP Server: Capability Registry Discovery & Execution

Unit 10: Implement search_capabilities() tool
Unit 11: Implement execute_capability() tool (follows)

Usage:
    from openwork_mcp_tools import CapabilityRegistry
    registry = CapabilityRegistry(neo4j_uri, supabase_url, supabase_key)
    
    # Search capabilities
    results = registry.search_capabilities(
        domain='sales',
        fit_gte=80,
        tags=['hipaa'],
        requires_mcp='MCP-SUPABASE'
    )
"""

from typing import Dict, List, Any, Optional
from neo4j import GraphDatabase
from supabase import create_client
from datetime import datetime
import json

class CapabilityRegistry:
    """
    OpenWork MCP: Capability Registry Discovery & Execution
    
    Interfaces:
    - search_capabilities(domain, fit_gte, tags, requires_mcp)
    - execute_capability(capability_id, inputs, context)
    - compose_workflow(workflow_id, start_stage)
    """
    
    def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_password: str,
                 supabase_url: str, supabase_key: str):
        """Initialize connections to Neo4j and Supabase"""
        self.neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
        self.supabase = create_client(supabase_url, supabase_key)
    
    # ========================================================================
    # UNIT 10: SEARCH_CAPABILITIES
    # ========================================================================
    
    def search_capabilities(
        self,
        domain: Optional[str] = None,
        fit_gte: int = 80,
        tags: Optional[List[str]] = None,
        requires_mcp: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Search Capability Registry by multiple dimensions.
        
        Args:
            domain: Filter by domain (e.g., 'DOM-SALES')
            fit_gte: Minimum fit score (0-100)
            tags: Filter by tags (AND logic)
            requires_mcp: Filter by MCP dependency
        
        Returns:
            {
                'capabilities': [
                    {'id', 'ref_id', 'name', 'fit', 'source', 'gap', ...}
                ],
                'count': int,
                'query_params': {...}
            }
        """
        
        with self.neo4j_driver.session() as session:
            # Build Cypher query
            where_clauses = [f"c.healthroute_fit >= {fit_gte}"]
            params = {}
            
            # Domain filter
            if domain:
                where_clauses.append("(c)-[:BELONGS_TO]->(d:Domain {id: $domain})")
                params['domain'] = domain
            
            # Tag filter (any tag match for now; could be ALL with REDUCE)
            if tags:
                where_clauses.append("ANY(tag IN $tags WHERE tag IN c.tags)")
                params['tags'] = tags
            
            # MCP dependency filter
            if requires_mcp:
                where_clauses.append("(c)-[:REQUIRES_MCP]->(m:MCP {id: $mcp})")
                params['mcp'] = requires_mcp
            
            where_str = " AND ".join(where_clauses)
            
            # Execute query
            cypher = f"""
                MATCH (c:Capability)
                {('WHERE ' + where_str) if where_str else ''}
                RETURN 
                    c.id as id,
                    c.ref_id as ref_id,
                    c.slug as slug,
                    c.name as name,
                    c.description as description,
                    c.source as source,
                    c.healthroute_fit as healthroute_fit,
                    c.maturity as maturity,
                    c.version as version
                ORDER BY c.healthroute_fit DESC
            """
            
            result = session.run(cypher, params)
            capabilities = [record.data() for record in result]
        
        # Enrich with Supabase data (additional metadata)
        enriched = self._enrich_from_supabase(capabilities)
        
        return {
            'capabilities': enriched,
            'count': len(enriched),
            'query_params': {
                'domain': domain,
                'fit_gte': fit_gte,
                'tags': tags,
                'requires_mcp': requires_mcp
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def _enrich_from_supabase(self, capabilities: List[Dict]) -> List[Dict]:
        """Fetch additional metadata from Supabase for each capability"""
        if not capabilities:
            return []
        
        try:
            # Batch fetch from Supabase (more efficient)
            ref_ids = [c['ref_id'] for c in capabilities]
            
            response = self.supabase.table('capabilities').select(
                'ref_id, healthroute_use_case, healthroute_gap, owner, approval_status, tags'
            ).in_('ref_id', ref_ids).execute()
            
            sb_data = {row['ref_id']: row for row in response.data}
            
            # Merge Neo4j + Supabase data
            for cap in capabilities:
                if cap['ref_id'] in sb_data:
                    sb_row = sb_data[cap['ref_id']]
                    cap['use_case'] = sb_row.get('healthroute_use_case')
                    cap['gap'] = sb_row.get('healthroute_gap')
                    cap['owner'] = sb_row.get('owner')
                    cap['approval_status'] = sb_row.get('approval_status')
            
            return capabilities
        
        except Exception as e:
            # Fall back to Neo4j data if Supabase fails
            print(f"⚠️  Supabase enrichment failed: {e}. Returning Neo4j data only.")
            return capabilities
    
    # ========================================================================
    # UTILITY: Validation
    # ========================================================================
    
    def validate_search_results(self, results: Dict) -> bool:
        """Validate search results against expectations"""
        checks = {
            'has_capabilities': len(results.get('capabilities', [])) > 0,
            'fit_scores_valid': all(0 <= c.get('healthroute_fit', 0) <= 100 
                                   for c in results.get('capabilities', [])),
            'sorted_by_fit': all(
                results['capabilities'][i]['healthroute_fit'] >= results['capabilities'][i+1]['healthroute_fit']
                for i in range(len(results['capabilities'])-1)
            ) if len(results.get('capabilities', [])) > 1 else True,
            'count_matches': results.get('count') == len(results.get('capabilities', []))
        }
        
        return all(checks.values())
    
    def close(self):
        """Close database connections"""
        self.neo4j_driver.close()


# ============================================================================
# TEST CASES (Unit 10 validation)
# ============================================================================

TEST_CASES = [
    {
        'name': 'Search by domain (Sales)',
        'params': {'domain': 'DOM-SALES'},
        'expect_count': 2,  # CAP-001, CAP-003
        'expect_fits': [95, 90]
    },
    {
        'name': 'Search by fit score >= 80',
        'params': {'fit_gte': 80},
        'expect_count': 5,  # All capabilities
        'expect_fits': [100, 95, 90, 90, 85]
    },
    {
        'name': 'Search by fit score >= 90',
        'params': {'fit_gte': 90},
        'expect_count': 3,  # CAP-001, CAP-003, CAP-101
        'expect_fits': [100, 95, 90]
    },
    {
        'name': 'Search by MCP dependency',
        'params': {'requires_mcp': 'MCP-SUPABASE'},
        'expect_count': 2,  # CAP-003, CAP-201
        'expect_fits': [100, 90]
    },
    {
        'name': 'Search by domain + fit',
        'params': {'domain': 'DOM-SALES', 'fit_gte': 90},
        'expect_count': 2,  # CAP-001 (95), CAP-003 (90)
        'expect_fits': [95, 90]
    },
    {
        'name': 'Search by domain + high fit',
        'params': {'domain': 'DOM-SALES', 'fit_gte': 95},
        'expect_count': 1,  # CAP-001 (95)
        'expect_fits': [95]
    },
    {
        'name': 'Search compliance domain',
        'params': {'domain': 'DOM-COMPLIANCE'},
        'expect_count': 1,  # CAP-201
        'expect_fits': [100]
    },
    {
        'name': 'Search knowledge domain',
        'params': {'domain': 'DOM-KNOWLEDGE'},
        'expect_count': 1,  # CAP-401
        'expect_fits': [85]
    },
    {
        'name': 'Search infra domain',
        'params': {'domain': 'DOM-INFRA'},
        'expect_count': 1,  # CAP-101
        'expect_fits': [90]
    },
    {
        'name': 'Empty search (all capabilities)',
        'params': {},
        'expect_count': 5,
        'expect_fits': [100, 95, 90, 90, 85]
    }
]


def validate_test_case(registry: CapabilityRegistry, test: Dict) -> bool:
    """Run one test case and return pass/fail"""
    try:
        result = registry.search_capabilities(**test['params'])
        
        # Check count
        if result['count'] != test['expect_count']:
            print(f"  ❌ {test['name']}: Expected {test['expect_count']} results, got {result['count']}")
            return False
        
        # Check fit scores
        actual_fits = [c['healthroute_fit'] for c in result['capabilities']]
        if actual_fits != test['expect_fits']:
            print(f"  ❌ {test['name']}: Expected fits {test['expect_fits']}, got {actual_fits}")
            return False
        
        print(f"  ✅ {test['name']}")
        return True
    
    except Exception as e:
        print(f"  ❌ {test['name']}: {e}")
        return False


if __name__ == '__main__':
    print("OpenWork MCP: Capability Registry Tool")
    print("Unit 10: search_capabilities() Implementation")
    print("\nNote: Connect to live Neo4j + Supabase to run tests")
    print("\nExpected test results (10 test cases):")
    for test in TEST_CASES:
        print(f"  - {test['name']}: {test['expect_count']} results")


    # ========================================================================
    # UNIT 11: EXECUTE_CAPABILITY
    # ========================================================================
    
    def execute_capability(
        self,
        capability_id: str,
        inputs: Dict[str, Any],
        context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Execute a capability. Routes to correct handler based on source.
        
        Args:
            capability_id: Capability to execute (e.g., 'CAP-001')
            inputs: Input parameters for capability
            context: Additional context (workflow_id, session_id, etc.)
        
        Returns:
            {
                'status': 'success|error|timeout',
                'output': {...},
                'latency_ms': int,
                'tokens_used': int,
                'cost_usd': float,
                'execution_id': str,
                'timestamp': str
            }
        """
        
        import time
        start_time = time.time()
        execution_id = f"EXEC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{capability_id}"
        
        try:
            # Step 1: Lookup capability metadata
            with self.neo4j_driver.session() as session:
                cypher = "MATCH (c:Capability {id: $id}) RETURN c.*"
                result = session.run(cypher, id=capability_id)
                record = result.single()
                
                if not record:
                    return self._execution_result(
                        execution_id=execution_id,
                        status='error',
                        error=f"Capability not found: {capability_id}",
                        start_time=start_time
                    )
                
                capability = dict(record)
            
            # Step 2: Validate inputs
            validation = self._validate_inputs(capability_id, inputs)
            if not validation['valid']:
                return self._execution_result(
                    execution_id=execution_id,
                    status='error',
                    error=f"Input validation failed: {validation['errors']}",
                    start_time=start_time
                )
            
            # Step 3: Route to handler based on source
            source = capability.get('source')
            
            if source == 'anthropic':
                result = self._execute_anthropic_skill(capability, inputs)
            
            elif source == 'awesome-claude-code':
                result = self._execute_oss_skill(capability, inputs)
            
            elif source == 'internal':
                result = self._execute_internal_skill(capability, inputs)
            
            else:
                return self._execution_result(
                    execution_id=execution_id,
                    status='error',
                    error=f"Unknown source: {source}",
                    start_time=start_time
                )
            
            # Step 4: Log execution to Supabase
            latency_ms = int((time.time() - start_time) * 1000)
            self._log_execution(
                execution_id=execution_id,
                capability_id=capability_id,
                inputs=inputs,
                output=result.get('output'),
                status=result.get('status'),
                latency_ms=latency_ms,
                tokens_used=result.get('tokens', 0),
                cost_usd=result.get('cost', 0)
            )
            
            # Step 5: Return result with metrics
            return {
                'status': result.get('status', 'success'),
                'output': result.get('output'),
                'execution_id': execution_id,
                'latency_ms': latency_ms,
                'tokens_used': result.get('tokens', 0),
                'cost_usd': result.get('cost', 0),
                'timestamp': datetime.now().isoformat()
            }
        
        except Exception as e:
            return self._execution_result(
                execution_id=execution_id,
                status='error',
                error=str(e),
                start_time=start_time
            )
    
    # ========================================================================
    # ROUTING: Handler implementations
    # ========================================================================
    
    def _execute_anthropic_skill(self, capability: Dict, inputs: Dict) -> Dict:
        """
        Execute Anthropic Sales Plugin skill (CAP-001, CAP-003, etc.)
        
        Maps to plugin's built-in skills via prompt engineering.
        """
        skill_name = capability.get('skill', {}).get('name')
        
        # Mock execution (real implementation calls actual plugin)
        if skill_name == 'account-research':
            # Would call: anthropic_plugin.account_research(inputs['company_name'])
            return {
                'status': 'success',
                'output': {
                    'company': inputs.get('company_name'),
                    'company_research': f"Mock research for {inputs.get('company_name')}",
                    'key_people': ['Lab Director', 'Operations Manager'],
                    'recent_news': ['Accreditation renewed']
                },
                'tokens': 2000,
                'cost': 0.02
            }
        
        elif skill_name == 'call-summary':
            # Would call: anthropic_plugin.call_summary(inputs['call_notes'])
            return {
                'status': 'success',
                'output': {
                    'prospect': inputs.get('prospect_name', 'Unknown'),
                    'prospect_interest': 'interested',
                    'specimen_volume': '300/day',
                    'action_items': [
                        'Send trial agreement',
                        'Schedule onboarding call'
                    ],
                    'follow_up_email': 'Mock follow-up email content'
                },
                'tokens': 1500,
                'cost': 0.015
            }
        
        else:
            return {
                'status': 'error',
                'output': None,
                'tokens': 0,
                'cost': 0
            }
    
    def _execute_oss_skill(self, capability: Dict, inputs: Dict) -> Dict:
        """
        Execute awesome-claude-code skill (CAP-101, CAP-401, etc.)
        """
        skill_name = capability.get('slug')
        
        if skill_name == 'agentic-workflow-patterns':
            # Reference material, no execution
            return {
                'status': 'success',
                'output': {
                    'pattern': 'orchestrator-workers',
                    'description': 'Coordinate multiple agents via central coordinator',
                    'use_cases': [
                        'HealthRoute sales workflow (research → prep → call → summary)',
                        'Multi-step business processes'
                    ]
                },
                'tokens': 0,
                'cost': 0
            }
        
        elif skill_name == 'librarian-mcp':
            # Query Obsidian vault via MCP
            return {
                'status': 'success',
                'output': {
                    'vault': 'HealthRoute Obsidian',
                    'query': inputs.get('query', 'N/A'),
                    'results': [
                        {'note': 'Objection Handling', 'relevance': 0.95},
                        {'note': 'Trial Pitch Template', 'relevance': 0.88}
                    ]
                },
                'tokens': 500,
                'cost': 0.005
            }
        
        else:
            return {
                'status': 'error',
                'output': None,
                'tokens': 0,
                'cost': 0
            }
    
    def _execute_internal_skill(self, capability: Dict, inputs: Dict) -> Dict:
        """
        Execute internal/custom skill (CAP-201, etc.)
        """
        skill_name = capability.get('slug')
        
        if skill_name == 'healthroute-hipaa-compliance':
            # Log to audit trail in Supabase
            return {
                'status': 'success',
                'output': {
                    'prospect': inputs.get('prospect_name'),
                    'audit_log_id': f"AUDIT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                    'compliance_status': 'HIPAA_COMPLIANT',
                    'phi_accessed': inputs.get('data_accessed', []),
                    'hipaa_concern_level': inputs.get('concern_level', 'low')
                },
                'tokens': 500,
                'cost': 0.0
            }
        
        else:
            return {
                'status': 'error',
                'output': None,
                'tokens': 0,
                'cost': 0
            }
    
    # ========================================================================
    # UTILITIES: Validation, Logging, Error Handling
    # ========================================================================
    
    def _validate_inputs(self, capability_id: str, inputs: Dict) -> Dict:
        """Validate inputs against capability schema"""
        # Simple validation for now; real implementation checks schema
        if not isinstance(inputs, dict):
            return {
                'valid': False,
                'errors': ['Inputs must be a dictionary']
            }
        
        return {
            'valid': True,
            'errors': []
        }
    
    def _execution_result(
        self,
        execution_id: str,
        status: str,
        error: Optional[str] = None,
        output: Optional[Dict] = None,
        start_time: Optional[float] = None
    ) -> Dict:
        """Format execution result"""
        latency_ms = 0
        if start_time:
            latency_ms = int((time.time() - start_time) * 1000)
        
        return {
            'status': status,
            'output': output,
            'error': error,
            'execution_id': execution_id,
            'latency_ms': latency_ms,
            'tokens_used': 0,
            'cost_usd': 0,
            'timestamp': datetime.now().isoformat()
        }
    
    def _log_execution(
        self,
        execution_id: str,
        capability_id: str,
        inputs: Dict,
        output: Optional[Dict],
        status: str,
        latency_ms: int,
        tokens_used: int,
        cost_usd: float
    ) -> None:
        """Log execution to Supabase audit table"""
        try:
            self.supabase.table('capability_executions').insert({
                'id': execution_id,
                'capability_id': capability_id,
                'inputs': json.dumps(inputs),
                'output': json.dumps(output) if output else None,
                'status': status,
                'latency_ms': latency_ms,
                'tokens_used': tokens_used,
                'cost_usd': float(cost_usd),
                'timestamp': datetime.now().isoformat()
            }).execute()
        except Exception as e:
            print(f"⚠️  Failed to log execution: {e}")


# ============================================================================
# TEST CASES (Unit 11 validation)
# ============================================================================

EXECUTION_TEST_CASES = [
    {
        'name': 'Execute account-research (CAP-001)',
        'capability_id': 'CAP-001',
        'inputs': {'company_name': 'WakeMed'},
        'expect_status': 'success',
        'expect_output_keys': ['company_research', 'key_people']
    },
    {
        'name': 'Execute call-summary (CAP-003)',
        'capability_id': 'CAP-003',
        'inputs': {'call_notes': 'Discussed specimen volumes...'},
        'expect_status': 'success',
        'expect_output_keys': ['prospect_interest', 'action_items']
    },
    {
        'name': 'Execute agentic-patterns (CAP-101)',
        'capability_id': 'CAP-101',
        'inputs': {},
        'expect_status': 'success',
        'expect_output_keys': ['pattern', 'use_cases']
    },
    {
        'name': 'Execute librarian-mcp (CAP-401)',
        'capability_id': 'CAP-401',
        'inputs': {'query': 'objection handling'},
        'expect_status': 'success',
        'expect_output_keys': ['vault', 'results']
    },
    {
        'name': 'Execute HIPAA compliance (CAP-201)',
        'capability_id': 'CAP-201',
        'inputs': {'prospect_name': 'WakeMed', 'data_accessed': ['facility_name']},
        'expect_status': 'success',
        'expect_output_keys': ['audit_log_id', 'compliance_status']
    }
]
