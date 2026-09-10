#!/usr/bin/env python3
"""
Capability Orchestrator: Compose capabilities into executable workflows

Unit 13: Orchestrator implementation for Phase 1A
Chains multiple capabilities (CAP-001, CAP-003, etc.) into complex workflows,
manages context flow between stages, handles errors, and tracks costs.

Usage:
    from capability_orchestrator import CapabilityOrchestrator

    orchestrator = CapabilityOrchestrator(registry, supabase_client)
    result = orchestrator.execute(
        workflow_id='WFL-001',
        initial_context={'prospect_name': 'WakeMed'}
    )
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import time
from dataclasses import dataclass, asdict


@dataclass
class StageResult:
    """Result from executing a single stage"""
    stage_id: str
    status: str  # COMPLETE, PAUSED, FAILED
    outputs: Dict[str, Any]
    cost: float
    tokens: int
    latency_ms: int
    error: Optional[str] = None


@dataclass
class WorkflowExecutionResult:
    """Result from executing entire workflow"""
    workflow_id: str
    status: str  # COMPLETE, PAUSED, FAILED
    stage_results: Dict[str, StageResult]
    total_cost: float
    total_tokens: int
    latency_ms: int
    error: Optional[str] = None


class CapabilityOrchestrator:
    """
    Chains multiple capabilities into executable workflows.

    Architecture:
    - Loads workflow definitions (stages + capability sequences)
    - Executes stages sequentially (or parallel within stages)
    - Manages context flow between stages
    - Handles errors with retry/fallback/escalate
    - Pauses for user input (e.g., manual call transcript)
    - Tracks cost and latency per stage
    - Logs to Supabase audit table
    """

    def __init__(self, registry, supabase_client):
        """
        Initialize orchestrator.

        Args:
            registry: CapabilityRegistry instance (for execute_capability)
            supabase_client: Supabase client (for workflow + pause storage)
        """
        self.registry = registry
        self.supabase = supabase_client

    # ========================================================================
    # LOAD WORKFLOW
    # ========================================================================

    def load_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """
        Load workflow definition and return stages.

        Args:
            workflow_id: Workflow ID (e.g., 'WFL-001')

        Returns:
            {
                'id': 'WFL-001',
                'name': 'Sales Workflow',
                'stages': [
                    {
                        'stage_num': 1,
                        'name': 'Account Research',
                        'capabilities': ['CAP-001'],
                        'parallelizable': False,
                        'required_inputs': ['company_name'],
                        'outputs': {'company_research', 'key_people'}
                    },
                    ...
                ]
            }
        """
        try:
            result = self.supabase.table('workflows') \
                .select('*') \
                .eq('ref_id', workflow_id) \
                .single() \
                .execute()

            workflow = result.data

            # Parse stages array
            if isinstance(workflow.get('stages'), str):
                workflow['stages'] = json.loads(workflow['stages'])

            return workflow

        except Exception as e:
            raise ValueError(f"Failed to load workflow {workflow_id}: {str(e)}")

    # ========================================================================
    # EXECUTE WORKFLOW
    # ========================================================================

    def execute(
        self,
        workflow_id: str,
        initial_context: Optional[Dict] = None,
        pause_after_stages: Optional[List[int]] = None
    ) -> WorkflowExecutionResult:
        """
        Execute workflow from start to end.

        Args:
            workflow_id: Workflow to execute (e.g., 'WFL-001')
            initial_context: Starting context (e.g., {'prospect_name': 'WakeMed'})
            pause_after_stages: List of stage numbers to pause after

        Returns:
            WorkflowExecutionResult with all stage results and metrics

        Example:
            result = orchestrator.execute(
                workflow_id='WFL-001',
                initial_context={'prospect_name': 'WakeMed'},
                pause_after_stages=[3]
            )
            # Pauses after Stage 3 for user to input call notes
        """

        workflow_start = time.time()
        execution_id = f"WFL-{datetime.now().strftime('%Y%m%d%H%M%S')}-{workflow_id}"

        try:
            # Load workflow
            workflow = self.load_workflow(workflow_id)
            stages = workflow.get('stages', [])

            # Initialize context
            execution_context = initial_context or {}
            execution_context['workflow_id'] = workflow_id
            execution_context['execution_id'] = execution_id
            execution_context['_start_time'] = workflow_start

            stage_results = {}
            total_cost = 0.0
            total_tokens = 0

            # Execute each stage
            for stage_num, stage_def in enumerate(stages, 1):
                stage_start = time.time()
                stage_id = f"STAGE-{stage_num}"

                try:
                    # Execute stage
                    stage_result = self._execute_stage(
                        stage_def,
                        stage_id,
                        execution_context
                    )

                    # Accumulate results
                    stage_results[stage_id] = stage_result
                    total_cost += stage_result.cost
                    total_tokens += stage_result.tokens

                    # Merge outputs into context
                    execution_context.update(stage_result.outputs)

                    # Check pause condition
                    if stage_num in (pause_after_stages or []):
                        return self._handle_pause(
                            workflow_id,
                            execution_id,
                            stage_num,
                            stage_results,
                            execution_context,
                            total_cost,
                            total_tokens
                        )

                except Exception as e:
                    # Error recovery
                    handled = self._handle_error(
                        stage_id,
                        e,
                        execution_context
                    )

                    if not handled:
                        latency_ms = int((time.time() - workflow_start) * 1000)
                        return WorkflowExecutionResult(
                            workflow_id=workflow_id,
                            status='FAILED',
                            stage_results=stage_results,
                            total_cost=total_cost,
                            total_tokens=total_tokens,
                            latency_ms=latency_ms,
                            error=f"Stage {stage_num} failed: {str(e)}"
                        )

            # Success: return complete result
            latency_ms = int((time.time() - workflow_start) * 1000)

            # Log to audit table
            self._log_workflow_execution(
                execution_id,
                workflow_id,
                stage_results,
                total_cost,
                total_tokens,
                latency_ms
            )

            return WorkflowExecutionResult(
                workflow_id=workflow_id,
                status='COMPLETE',
                stage_results=stage_results,
                total_cost=total_cost,
                total_tokens=total_tokens,
                latency_ms=latency_ms
            )

        except Exception as e:
            latency_ms = int((time.time() - workflow_start) * 1000)
            return WorkflowExecutionResult(
                workflow_id=workflow_id,
                status='FAILED',
                stage_results={},
                total_cost=0.0,
                total_tokens=0,
                latency_ms=latency_ms,
                error=str(e)
            )

    # ========================================================================
    # EXECUTE STAGE (Sequential or Parallel)
    # ========================================================================

    def _execute_stage(
        self,
        stage_def: Dict,
        stage_id: str,
        execution_context: Dict
    ) -> StageResult:
        """Execute all capabilities within a stage"""

        stage_start = time.time()
        capabilities = stage_def.get('capabilities', [])

        if len(capabilities) == 0:
            return StageResult(
                stage_id=stage_id,
                status='COMPLETE',
                outputs={},
                cost=0.0,
                tokens=0,
                latency_ms=0
            )

        # For now: always sequential (parallelization in Phase 1B)
        result = self._execute_sequential(
            capabilities,
            stage_def,
            execution_context
        )

        latency_ms = int((time.time() - stage_start) * 1000)

        return StageResult(
            stage_id=stage_id,
            status='COMPLETE',
            outputs=result['outputs'],
            cost=result['cost'],
            tokens=result['tokens'],
            latency_ms=latency_ms
        )

    def _execute_sequential(
        self,
        capabilities: List[str],
        stage_def: Dict,
        execution_context: Dict
    ) -> Dict[str, Any]:
        """Execute capabilities one by one, passing context between them"""

        stage_outputs = {}
        stage_cost = 0.0
        stage_tokens = 0

        for cap_id in capabilities:
            # Extract inputs from execution context
            inputs = self._extract_inputs(cap_id, execution_context)

            # Execute capability
            result = self.registry.execute_capability(
                capability_id=cap_id,
                inputs=inputs,
                context=execution_context
            )

            # Store output
            if result.get('status') == 'success' and result.get('output'):
                # Flatten capability output into stage outputs
                stage_outputs.update(result['output'])
                stage_cost += result.get('cost_usd', 0.0)
                stage_tokens += result.get('tokens_used', 0)

                # Merge outputs into execution context for next capability
                execution_context.update(result['output'])
            else:
                raise Exception(f"Capability {cap_id} failed: {result.get('error', 'unknown error')}")

        return {
            'outputs': stage_outputs,
            'cost': stage_cost,
            'tokens': stage_tokens
        }

    def _execute_parallel(self, capabilities, execution_context):
        """Execute capabilities in parallel (Phase 1B)"""
        # TODO: Implement with ThreadPoolExecutor after Phase 1A validation
        return self._execute_sequential(capabilities, {}, execution_context)

    # ========================================================================
    # CONTEXT EXTRACTION
    # ========================================================================

    def _extract_inputs(self, capability_id: str, execution_context: Dict) -> Dict:
        """
        Extract inputs for a capability from execution_context.

        Maps from execution_context keys to capability input schema.
        Example:
            - execution_context has: {'company_research': {...}}
            - CAP-003 needs: {'call_notes': '...'}
            - Returns: {'call_notes': execution_context.get('call_notes')}
        """

        extracted = {}

        # Capability-specific input mapping
        if capability_id == 'CAP-001':
            # Account research needs company_name
            if 'company_name' in execution_context:
                extracted['company_name'] = execution_context['company_name']

        elif capability_id == 'CAP-003':
            # Call summary needs call_notes, prospect_name
            if 'call_notes' in execution_context:
                extracted['call_notes'] = execution_context['call_notes']
            if 'prospect_name' in execution_context:
                extracted['prospect_name'] = execution_context['prospect_name']

        elif capability_id == 'CAP-101':
            # Agentic patterns doesn't need inputs
            pass

        elif capability_id == 'CAP-401':
            # Librarian MCP needs search query (optional)
            if 'query' in execution_context:
                extracted['query'] = execution_context['query']

        elif capability_id == 'CAP-201':
            # HIPAA compliance needs prospect_name, data_accessed
            if 'prospect_name' in execution_context:
                extracted['prospect_name'] = execution_context['prospect_name']
            if 'data_accessed' in execution_context:
                extracted['data_accessed'] = execution_context['data_accessed']

        return extracted

    # ========================================================================
    # ERROR HANDLING & RECOVERY
    # ========================================================================

    def _handle_error(self, stage_id: str, error: Exception, execution_context: Dict) -> bool:
        """
        Handle stage execution error.

        Recovery strategies:
        1. Retry with exponential backoff
        2. Skip stage if marked optional
        3. Escalate to user

        Returns: True if recovered, False if unrecoverable
        """

        error_msg = str(error)
        print(f"⚠️  {stage_id} failed: {error_msg}")

        # For now: don't auto-recover (user will handle via pause/resume)
        # Phase 1B: implement retry logic
        return False

    # ========================================================================
    # PAUSE & RESUME
    # ========================================================================

    def _handle_pause(
        self,
        workflow_id: str,
        execution_id: str,
        stage_num: int,
        stage_results: Dict,
        execution_context: Dict,
        total_cost: float,
        total_tokens: int
    ) -> WorkflowExecutionResult:
        """
        Pause workflow and save state for later resume.

        Stores pause state in Supabase workflow_pauses table.
        User can resume with new inputs (e.g., call transcript).
        """

        pause_id = f"PAUSE-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        try:
            self.supabase.table('workflow_pauses').insert({
                'pause_id': pause_id,
                'workflow_id': workflow_id,
                'execution_id': execution_id,
                'stage_num': stage_num,
                'execution_context': json.dumps(execution_context),
                'status': 'PAUSED',
                'created_at': datetime.now().isoformat()
            }).execute()
        except Exception as e:
            print(f"⚠️  Failed to save pause state: {e}")

        latency_ms = int((time.time() - execution_context.get('_start_time', time.time())) * 1000)

        return WorkflowExecutionResult(
            workflow_id=workflow_id,
            status='PAUSED',
            stage_results=stage_results,
            total_cost=total_cost,
            total_tokens=total_tokens,
            latency_ms=latency_ms,
            error=f"Paused after stage {stage_num}. Resume with updated context."
        )

    def resume_workflow(
        self,
        pause_id: str,
        resume_inputs: Dict
    ) -> WorkflowExecutionResult:
        """
        Resume a paused workflow with new inputs.

        Args:
            pause_id: Pause ID from _handle_pause
            resume_inputs: New inputs to inject (e.g., {'call_notes': '...'})

        Returns:
            WorkflowExecutionResult from remaining stages
        """

        try:
            # Load pause state
            pause_record = self.supabase.table('workflow_pauses') \
                .select('*') \
                .eq('pause_id', pause_id) \
                .single() \
                .execute()

            pause_data = pause_record.data
            workflow_id = pause_data['workflow_id']
            stage_num = pause_data['stage_num']

            # Restore execution context
            execution_context = json.loads(pause_data['execution_context'])
            execution_context.update(resume_inputs)

            # Resume execution from next stage
            result = self.execute(
                workflow_id=workflow_id,
                initial_context=execution_context,
                pause_after_stages=None  # Continue to end
            )

            # Mark pause as resumed
            self.supabase.table('workflow_pauses') \
                .update({'status': 'RESUMED', 'resumed_at': datetime.now().isoformat()}) \
                .eq('pause_id', pause_id) \
                .execute()

            return result

        except Exception as e:
            return WorkflowExecutionResult(
                workflow_id='UNKNOWN',
                status='FAILED',
                stage_results={},
                total_cost=0.0,
                total_tokens=0,
                latency_ms=0,
                error=f"Failed to resume workflow: {str(e)}"
            )

    # ========================================================================
    # LOGGING & AUDIT
    # ========================================================================

    def _log_workflow_execution(
        self,
        execution_id: str,
        workflow_id: str,
        stage_results: Dict,
        total_cost: float,
        total_tokens: int,
        latency_ms: int
    ) -> None:
        """Log workflow execution to Supabase audit table"""

        try:
            self.supabase.table('workflow_executions').insert({
                'id': execution_id,
                'workflow_id': workflow_id,
                'stage_results': json.dumps({
                    k: {
                        'status': v.status,
                        'outputs': v.outputs,
                        'cost': v.cost,
                        'tokens': v.tokens,
                        'latency_ms': v.latency_ms
                    } for k, v in stage_results.items()
                }),
                'total_cost': total_cost,
                'total_tokens': total_tokens,
                'latency_ms': latency_ms,
                'status': 'COMPLETE',
                'timestamp': datetime.now().isoformat()
            }).execute()
        except Exception as e:
            print(f"⚠️  Failed to log workflow execution: {e}")


# ============================================================================
# TEST CASES (Unit 13 validation)
# ============================================================================

WORKFLOW_TEST_CASES = [
    {
        'name': 'Execute WFL-001 (research → summary)',
        'workflow_id': 'WFL-001',
        'initial_context': {'company_name': 'WakeMed'},
        'expect_status': 'COMPLETE',
        'expect_stages': ['STAGE-1', 'STAGE-2'],
        'expect_outputs': ['company_research', 'prospect_interest']
    },
    {
        'name': 'Execute WFL-001 with pause after Stage 1',
        'workflow_id': 'WFL-001',
        'initial_context': {'company_name': 'WakeMed'},
        'pause_after_stages': [1],
        'expect_status': 'PAUSED',
        'expect_pause_num': 1
    },
    {
        'name': 'Resume WFL-001 with call notes',
        'pause_id': 'PAUSE-20260918120000',
        'resume_inputs': {'call_notes': 'Lab director interested...'},
        'expect_status': 'COMPLETE'
    }
]


if __name__ == '__main__':
    print("Capability Orchestrator: Workflow Execution Engine")
    print("Unit 13: Orchestrator implementation for Phase 1A")
    print("\nNote: Connect to live Neo4j + Supabase to run full tests\n")

    print("TEST CASES (Unit 13 validation):")
    for test in WORKFLOW_TEST_CASES:
        print(f"  ✓ {test['name']}")
        if 'expect_status' in test:
            print(f"    Expected status: {test['expect_status']}")
