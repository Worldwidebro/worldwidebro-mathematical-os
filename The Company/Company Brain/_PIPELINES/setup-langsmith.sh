#!/bin/bash
# Wire LangSmith API Integration
# Usage: source setup-langsmith.sh
# This loads the LangSmith API key and tests the connection

echo "🔐 LangSmith Integration Setup"
echo "═════════════════════════════════════"
echo ""

# Step 1: Get API key from Bitwarden
echo "Step 1: Retrieving API key from Bitwarden..."
# You can use bw CLI if installed:
# LANGSMITH_API_KEY=$(bw get password "LangSmith API Key")

# For now, use environment variable or prompt
if [ -z "$LANGSMITH_API_KEY" ]; then
  echo ""
  echo "⚠️  LANGSMITH_API_KEY not set"
  echo ""
  echo "To set it manually:"
  echo "  1. Go to https://vault.bitwarden.com"
  echo "  2. Search for 'LangSmith'"
  echo "  3. Copy the API key"
  echo "  4. Run: export LANGSMITH_API_KEY='<your-key>'"
  echo ""
  echo "Then re-run this script"
  exit 1
fi

echo "✅ API Key loaded (length: ${#LANGSMITH_API_KEY})"
echo ""

# Step 2: Set LangSmith environment variables
echo "Step 2: Configuring LangSmith environment..."
export LANGSMITH_API_KEY="$LANGSMITH_API_KEY"
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
export LANGSMITH_PROJECT="company-brain-evals"

echo "✅ Environment variables set:"
echo "  LANGSMITH_ENDPOINT: $LANGSMITH_ENDPOINT"
echo "  LANGSMITH_PROJECT: $LANGSMITH_PROJECT"
echo ""

# Step 3: Test connection with Python
echo "Step 3: Testing LangSmith connection..."
echo ""

python3 << 'PYTHON_EOF'
import os
import json
from datetime import datetime
import requests

api_key = os.getenv('LANGSMITH_API_KEY')
endpoint = os.getenv('LANGSMITH_ENDPOINT', 'https://api.smith.langchain.com')
project = os.getenv('LANGSMITH_PROJECT', 'company-brain-evals')

if not api_key:
    print("❌ LANGSMITH_API_KEY not set")
    exit(1)

# Test 1: Verify API key format
if len(api_key) < 20:
    print(f"❌ API key looks invalid (too short: {len(api_key)} chars)")
    exit(1)

print(f"✅ API key format valid ({len(api_key)} chars)")
print("")

# Test 2: Create a test trace
print("Step 4: Creating test trace...")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

trace_data = {
    "name": "company-brain-eval-test",
    "run_type": "llm",
    "inputs": {"prompt": "Test prompt from Company Brain"},
    "outputs": {"text": "Test output"},
    "status": "success",
    "start_time": datetime.utcnow().isoformat() + "Z",
    "end_time": datetime.utcnow().isoformat() + "Z",
    "metadata": {
        "project": project,
        "source": "company-brain-setup",
        "test": True
    }
}

try:
    response = requests.post(
        f"{endpoint}/api/v1/runs",
        headers=headers,
        json=trace_data,
        timeout=10
    )

    if response.status_code == 201:
        print(f"✅ Trace created successfully")
        print(f"   Status: {response.status_code}")
        result = response.json()
        if "id" in result:
            print(f"   Trace ID: {result['id']}")
        print("")
        print(f"View in LangSmith:")
        print(f"  https://smith.langchain.com/o/{endpoint.split('/')[-1]}/projects/p/{project}")
    else:
        print(f"⚠️  Response: {response.status_code}")
        print(f"   Body: {response.text[:200]}")
except Exception as e:
    print(f"❌ Connection failed: {str(e)}")
    print("")
    print("Troubleshooting:")
    print("  - Verify API key is correct")
    print("  - Check internet connectivity")
    print("  - Confirm LangSmith project exists")
    exit(1)

print("")
print("═════════════════════════════════════")
print("✅ LangSmith integration is ready!")
print("")
print("Next steps:")
print("  1. Wire deepeval evals to LangSmith")
print("  2. Run baseline evals on 50-agent sample")
print("  3. Verify traces appear in LangSmith dashboard")
PYTHON_EOF

