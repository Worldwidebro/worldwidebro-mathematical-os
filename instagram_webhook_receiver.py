#!/usr/bin/env python3
"""Webhook receiver for Instagram captures"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pathlib import Path
from datetime import datetime

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            capture_dir = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw")
            capture_dir.mkdir(parents=True, exist_ok=True)
            capture_file = capture_dir / f"webhook_{datetime.now().timestamp()}.json"

            with open(capture_file, 'w') as f:
                json.dump(data, f, indent=2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "saved", "file": str(capture_file)}).encode())

            print(f"✅ Webhook capture saved: {capture_file}")

        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), WebhookHandler)
    print("🔌 Instagram webhook receiver listening on http://localhost:5000")
    server.serve_forever()
