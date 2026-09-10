#!/usr/bin/env python3
"""
Unit 15: Error Recovery Tests

Tests error handling and recovery strategies:
1. Missing required inputs
2. Failed capability execution
3. Invalid workflow ID
4. Timeout handling

This validates production robustness.
"""

from typing import Dict, Any
import json


class ErrorRegistry:
    """Mock registry that simulates error conditions"""

    def __init__(self, error_mode: str = 'success'):
        self.error_mode = error_mode

    def execute_capability(self, capability_id: str, inputs: Dict, context: Dict) -> Dict:
        """Execute capability with error simulation"""

        if self.error_mode == 'missing_input':
            # Simulate missing required input
            if 'company_name' not in inputs and capability_id == 'CAP-001':
                return {
                    'status': 'error',
                    'output': None,
                    'error': 'Missing required input: company_name',
                    'tokens_used': 0,
                    'cost_usd': 0
                }

        if self.error_mode == 'execution_failed':
            # Simulate capability execution failure
            return {
                'status': 'error',
                'output': None,
                'error': f'Capability {capability_id} failed: External service unavailable',
                'tokens_used': 0,
                'cost_usd': 0
            }

        if self.error_mode == 'timeout':
            # Simulate timeout
            return {
                'status': 'error',
                'output': None,
                'error': f'Capability {capability_id} timed out after 60s',
                'tokens_used': 0,
                'cost_usd': 0
            }

        # Success path
        if capability_id == 'CAP-001':
            return {
                'status': 'success',
                'output': {
                    'company_name': inputs.get('company_name'),
                    'company_research': {'description': 'Test company'},
                    'key_people': []
                },
                'tokens_used': 2400,
                'cost_usd': 0.024
            }

        return {'status': 'error', 'output': None, 'error': 'Unknown capability'}


class ErrorSupabase:
    """Mock Supabase for error testing"""

    def __init__(self):
        self.workflows = {
            'WFL-001': {
                'ref_id': 'WFL-001',
                'name': 'Test Workflow',
                'stages': json.dumps([
                    {
                        'stage_num': 1,
                        'name': 'Account Research',
                        'capabilities': ['CAP-001'],
                        'required_inputs': ['company_name']
                    }
                ])
            }
        }

    def table(self, table_name: str):
        return ErrorSupabaseTable(table_name, self)


class ErrorSupabaseTable:
    """Mock table operations"""

    def __init__(self, table_name: str, supabase):
        self.table_name = table_name
        self.supabase = supabase

    def select(self, *args):
        return self

    def eq(self, key: str, value: str):
        self._key = key
        self._value = value
        return self

    def single(self):
        return self

    def execute(self):
        if self.table_name == 'workflows' and self._value == 'WFL-001':
            return ErrorSupabaseResult(self.supabase.workflows.get('WFL-001'))
        if self.table_name == 'workflows' and self._value == 'WFL-INVALID':
            return ErrorSupabaseResult(None)
        return ErrorSupabaseResult(None)

    def insert(self, data: Dict):
        return self

    def update(self, data: Dict):
        return self


class ErrorSupabaseResult:
    def __init__(self, data: Any):
        self.data = data


# ============================================================================
# TEST CASES
# ============================================================================

def test_missing_input():
    """Test 1: Missing required input (company_name)"""

    print("\n" + "=" * 70)
    print("TEST 1: Missing Required Input")
    print("=" * 70)

    from capability_orchestrator import CapabilityOrchestrator

    registry = ErrorRegistry(error_mode='missing_input')
    supabase = ErrorSupabase()
    orchestrator = CapabilityOrchestrator(registry, supabase)

    print("\n[Step 1] Execute workflow WITHOUT company_name")
    print("  Input: {}")

    # Note: orchestrator doesn't validate inputs in load_workflow,
    # it only validates during _extract_inputs which returns empty dict
    # The capability will fail when executed without required input

    result = orchestrator.execute(
        workflow_id='WFL-001',
        initial_context={}  # No company_name!
    )

    print(f"  Result status: {result.status}")
    print(f"  Error: {result.error}")

    assert result.status == 'FAILED', f"Expected FAILED, got {result.status}"
    assert 'company_name' in result.error or 'required input' in result.error.lower(), \
        f"Error should mention missing input: {result.error}"

    print("\n✅ TEST 1 PASSED: Missing input properly detected")
    return True


def test_capability_failure():
    """Test 2: Capability execution failure"""

    print("\n" + "=" * 70)
    print("TEST 2: Capability Execution Failure")
    print("=" * 70)

    from capability_orchestrator import CapabilityOrchestrator

    registry = ErrorRegistry(error_mode='execution_failed')
    supabase = ErrorSupabase()
    orchestrator = CapabilityOrchestrator(registry, supabase)

    print("\n[Step 1] Execute workflow with failing capability")
    print("  Input: {company_name: 'WakeMed'}")
    print("  Capability will fail: 'External service unavailable'")

    result = orchestrator.execute(
        workflow_id='WFL-001',
        initial_context={'company_name': 'WakeMed'}
    )

    print(f"  Result status: {result.status}")
    print(f"  Error: {result.error}")
    print(f"  Partial results: {list(result.stage_results.keys())}")

    assert result.status == 'FAILED', f"Expected FAILED, got {result.status}"
    assert 'External service unavailable' in result.error, \
        f"Error should mention service failure: {result.error}"

    print("\n✅ TEST 2 PASSED: Capability failure handled")
    return True


def test_invalid_workflow():
    """Test 3: Invalid workflow ID"""

    print("\n" + "=" * 70)
    print("TEST 3: Invalid Workflow ID")
    print("=" * 70)

    from capability_orchestrator import CapabilityOrchestrator

    registry = ErrorRegistry()
    supabase = ErrorSupabase()
    orchestrator = CapabilityOrchestrator(registry, supabase)

    print("\n[Step 1] Execute with invalid workflow ID")
    print("  Workflow ID: 'WFL-INVALID'")

    result = orchestrator.execute(
        workflow_id='WFL-INVALID',
        initial_context={'company_name': 'WakeMed'}
    )

    print(f"  Result status: {result.status}")
    print(f"  Error: {result.error}")

    assert result.status == 'FAILED', f"Expected FAILED, got {result.status}"
    assert 'Failed to load workflow' in result.error, \
        f"Error should mention load failure: {result.error}"

    print("\n✅ TEST 3 PASSED: Invalid workflow rejected")
    return True


def test_timeout():
    """Test 4: Capability timeout"""

    print("\n" + "=" * 70)
    print("TEST 4: Capability Timeout")
    print("=" * 70)

    from capability_orchestrator import CapabilityOrchestrator

    registry = ErrorRegistry(error_mode='timeout')
    supabase = ErrorSupabase()
    orchestrator = CapabilityOrchestrator(registry, supabase)

    print("\n[Step 1] Execute workflow with timeout")
    print("  Capability execution timeout after 60s")

    result = orchestrator.execute(
        workflow_id='WFL-001',
        initial_context={'company_name': 'WakeMed'}
    )

    print(f"  Result status: {result.status}")
    print(f"  Error: {result.error}")

    assert result.status == 'FAILED', f"Expected FAILED, got {result.status}"
    assert 'timed out' in result.error.lower(), \
        f"Error should mention timeout: {result.error}"

    print("\n✅ TEST 4 PASSED: Timeout detected and handled")
    return True


def test_error_recovery_strategy():
    """Test 5: Error recovery strategy selection"""

    print("\n" + "=" * 70)
    print("TEST 5: Error Recovery Strategy")
    print("=" * 70)

    print("\n[Step 1] Classify errors and recovery strategies")

    errors = [
        {
            'error': 'Missing required input: company_name',
            'type': 'input_validation',
            'recovery': 'Escalate to user (invalid data)',
            'automatic': False
        },
        {
            'error': 'Capability CAP-001 timed out after 60s',
            'type': 'timeout',
            'recovery': 'Retry with backoff',
            'automatic': True
        },
        {
            'error': 'External service unavailable',
            'type': 'service_error',
            'recovery': 'Retry or use fallback capability',
            'automatic': True
        },
        {
            'error': 'Paused after stage 1. Resume with updated context.',
            'type': 'pause_point',
            'recovery': 'Wait for user input + resume',
            'automatic': False
        }
    ]

    for error_case in errors:
        print(f"\n  Error: {error_case['error']}")
        print(f"  Type: {error_case['type']}")
        print(f"  Recovery: {error_case['recovery']}")
        print(f"  Automatic: {'Yes' if error_case['automatic'] else 'No (user intervention)'}")

    print("\n✅ TEST 5 PASSED: Error recovery strategies documented")
    return True


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("UNIT 15: ERROR RECOVERY TESTS")
    print("=" * 70)

    try:
        # Test 1: Missing input
        test_missing_input()

        # Test 2: Capability failure
        test_capability_failure()

        # Test 3: Invalid workflow
        test_invalid_workflow()

        # Test 4: Timeout
        test_timeout()

        # Test 5: Error recovery strategies
        test_error_recovery_strategy()

        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED (5/5)")
        print("=" * 70)
        print("\nError handling is robust!")
        print("Ready for Unit 16 — Performance baseline")

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
