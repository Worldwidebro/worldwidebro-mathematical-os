#!/usr/bin/env python3
"""
Composio Local Client - Interact with your local Composio instance
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def check_health():
    """Check if Composio server is running"""
    try:
        response = requests.get(f"{BASE_URL}/api/health", timeout=5)
        return response.json()
    except Exception as e:
        return {"error": f"Cannot reach server: {str(e)}"}

def get_tools():
    """Get list of available tools"""
    try:
        response = requests.get(f"{BASE_URL}/api/tools", timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def print_banner():
    print("\n" + "="*60)
    print("🎯 Composio Local Client")
    print("="*60 + "\n")

def main():
    print_banner()

    # Check health
    print("📍 Checking Composio Server Status...")
    health = check_health()
    print(json.dumps(health, indent=2))

    if "error" not in health:
        print("\n✅ Server is RUNNING")
        print(f"   Service: {health.get('service', 'unknown')}")
        print(f"   Version: {health.get('version', 'unknown')}")

        # Get tools
        print("\n📦 Available Tools:")
        tools = get_tools()
        print(json.dumps(tools, indent=2))

        print("\n" + "="*60)
        print("🌐 Access Points:")
        print("="*60)
        print(f"Dashboard: {BASE_URL}")
        print(f"API Docs:  {BASE_URL}/docs")
        print(f"Health:    {BASE_URL}/api/health")
        print(f"Tools:     {BASE_URL}/api/tools")
        print("="*60 + "\n")
    else:
        print(f"\n❌ Error: {health.get('error')}")
        print("Make sure the server is running: python3 composio_local_server.py\n")

if __name__ == "__main__":
    main()
