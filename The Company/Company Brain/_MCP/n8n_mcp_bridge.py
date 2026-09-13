#!/usr/bin/env python3
"""
Company Brain: n8n MCP Stdio-to-HTTP Bridge
Bridges standard input/output JSON-RPC to the n8n remote MCP HTTP endpoint.
Authority: Infrastructure Control Plane (CP-027)
"""

import sys
import os
import json
import urllib.request
import urllib.error

DEFAULT_URL = "http://100.87.214.70:5678/mcp-server/http"
DEFAULT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyZWU5OThiMi1iMjFkLTQyZGEtYmZlOC0xMWY2M2FlZDhmZDYiLCJpc3MiOiJuOG4iLCJhdWQiOiJtY3Atc2VydmVyLWFwaSIsImp0aSI6Ijg0OWU5OTQ3LWFlMTgtNDYwNi04YTUxLThhMTYyZDFkOTBlMyIsImlhdCI6MTc4OTI0NzQ5OH0.yBNN0lnccH0fAKEQjxL8J3fU1eg6fmKCjTwictbESt0"

URL = os.environ.get("N8N_MCP_URL", DEFAULT_URL)
TOKEN = os.environ.get("N8N_MCP_TOKEN", DEFAULT_TOKEN)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def main():
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            req_data = line.encode("utf-8")
            req = urllib.request.Request(URL, data=req_data, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as resp:
                if resp.status == 202:
                    continue
                resp_text = resp.read().decode("utf-8")
                for rline in resp_text.splitlines():
                    if rline.startswith("data: "):
                        data_payload = rline[6:].strip()
                        if data_payload:
                            sys.stdout.write(data_payload + "\n")
                            sys.stdout.flush()
                    elif rline.startswith("{") and rline.endswith("}"):
                        sys.stdout.write(rline + "\n")
                        sys.stdout.flush()
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8") if e.fp else str(e)
            try:
                parsed_in = json.loads(line)
                req_id = parsed_in.get("id")
            except Exception:
                req_id = None
            err_obj = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32000,
                    "message": f"HTTP {e.code}: {e.reason}",
                    "data": err_body,
                },
            }
            sys.stdout.write(json.dumps(err_obj) + "\n")
            sys.stdout.flush()
        except Exception as e:
            try:
                parsed_in = json.loads(line)
                req_id = parsed_in.get("id")
            except Exception:
                req_id = None
            err_obj = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32603,
                    "message": str(e),
                },
            }
            sys.stdout.write(json.dumps(err_obj) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
