import yaml

REGISTRY_PATH = "/Users/acebless/Documents/The Company/Company Brain/_REGISTRIES/CANONICAL/TEST_REGISTRY.yaml"

with open(REGISTRY_PATH, 'r') as f:
    registry = yaml.safe_load(f)

# Patch the commands to use the Tailscale IP
if 'TEST-351' in registry['tests']:
    registry['tests']['TEST-351']['command'] = "nc -vz 100.87.214.70 7687 && nc -vz 100.87.214.70 7474"
    registry['tests']['TEST-351']['status'] = "NOT_TESTED"

if 'TEST-376' in registry['tests']:
    registry['tests']['TEST-376']['command'] = "nc -vz 100.87.214.70 6333"
    registry['tests']['TEST-376']['status'] = "NOT_TESTED"

if 'TEST-103' in registry['tests']:
    registry['tests']['TEST-103']['status'] = "NOT_TESTED"

with open(REGISTRY_PATH, 'w') as f:
    yaml.dump(registry, f, sort_keys=False)
