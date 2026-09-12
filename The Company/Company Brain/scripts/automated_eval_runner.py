import yaml
import subprocess
import os
from datetime import datetime, timezone

REGISTRY_PATH = "/Users/acebless/Documents/The Company/Company Brain/_REGISTRIES/CANONICAL/TEST_REGISTRY.yaml"

def run_test(command):
    try:
        # Run command with a 5 second timeout
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        if result.returncode == 0:
            return "PASS", result.stdout.strip()
        else:
            return "FAIL", result.stderr.strip() or result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "FAIL", "Command timed out"
    except Exception as e:
        return "FAIL", str(e)

def main():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Registry not found at {REGISTRY_PATH}")
        return

    with open(REGISTRY_PATH, 'r') as f:
        registry = yaml.safe_load(f)

    tests_run = 0
    passed = 0
    failed = 0

    print("🚀 Starting Automated Eval Runner...")
    
    for test_id, test_data in registry.get('tests', {}).items():
        if test_data.get('status') == 'NOT_TESTED' and test_data.get('command'):
            print(f"Running {test_id}: {test_data['test']}...")
            
            status, evidence = run_test(test_data['command'])
            
            test_data['status'] = status
            test_data['actual_result'] = "Execution completed" if status == "PASS" else "Execution failed"
            test_data['evidence'] = evidence[:500] # Truncate evidence if too long
            test_data['timestamp'] = datetime.now(timezone.utc).isoformat()
            
            if status == "PASS":
                print(f"  ✅ PASS")
                passed += 1
            else:
                print(f"  ❌ FAIL: {evidence[:100]}...")
                failed += 1
                
            tests_run += 1

    # Update metadata
    if tests_run > 0:
        registry['metadata']['last_run'] = datetime.now(timezone.utc).isoformat()
        registry['metadata']['passed'] = registry['metadata'].get('passed', 0) + passed
        registry['metadata']['failed'] = registry['metadata'].get('failed', 0) + failed
        registry['metadata']['not_tested'] = max(0, registry['metadata'].get('not_tested', 500) - tests_run)

        # Write back to YAML
        with open(REGISTRY_PATH, 'w') as f:
            yaml.dump(registry, f, sort_keys=False)
            
        print(f"\n📊 Run Complete: {passed} Passed, {failed} Failed.")
        print(f"Registry updated at {REGISTRY_PATH}")
    else:
        print("\nNo pending tests with commands found.")

if __name__ == "__main__":
    main()
