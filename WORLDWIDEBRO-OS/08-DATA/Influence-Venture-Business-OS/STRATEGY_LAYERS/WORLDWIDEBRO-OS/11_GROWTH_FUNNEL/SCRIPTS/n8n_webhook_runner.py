#!/usr/bin/env python3
"""Local HTTP server so n8n Cloud can trigger funnel jobs without Execute Command."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

FUNNEL_ROOT = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL")
SCRIPTS = FUNNEL_ROOT / "SCRIPTS"
ORCHESTRATOR = FUNNEL_ROOT / "MASTER_ORCHESTRATOR.py"
SECRET = os.environ.get("N8N_WEBHOOK_SECRET", "")

ROUTES = (
    "/run-orchestrator",
    "/run-weekly",
    "/run-batch",
    "/run-opus-clip",
    "/sync-supabase",
)


class Handler(BaseHTTPRequestHandler):
    def _auth_ok(self) -> bool:
        if not SECRET:
            return True
        return self.headers.get("X-Funnel-Secret") == SECRET

    def _json(self, code: int, body: dict) -> None:
        raw = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        if urlparse(self.path).path == "/health":
            self._json(200, {"ok": True, "routes": list(ROUTES)})
            return
        self._json(404, {"error": "unknown path", "routes": list(ROUTES)})

    def do_POST(self) -> None:
        if not self._auth_ok():
            self._json(401, {"error": "unauthorized"})
            return
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length).decode() or "{}")
        path = urlparse(self.path).path

        if path == "/run-orchestrator":
            cmd = ["python3", str(ORCHESTRATOR), "run"]
            if body.get("auto"):
                cmd.append("--auto")
            elif body.get("batch"):
                cmd.append("--batch")
            elif body.get("venture_id"):
                cmd.extend(["--venture-id", body["venture_id"]])
            else:
                cmd.append("--auto")
            if body.get("render"):
                cmd.append("--render")
            if body.get("higgsfield"):
                cmd.append("--higgsfield")
            if body.get("opus_clip"):
                cmd.append("--opus-clip")
            if body.get("stage"):
                cmd.extend(["--stage", body["stage"]])
            if body.get("goal"):
                cmd.extend(["--goal", body["goal"]])
        elif path == "/run-weekly":
            vid = body.get("venture_id")
            day = body.get("day", "auto")
            render = ["--render"] if body.get("render") else []
            if not vid:
                self._json(400, {"error": "venture_id required"})
                return
            cmd = ["python3", str(SCRIPTS / "weekly_funnel_runner.py"), "--venture-id", vid, "--day", day, *render]
        elif path == "/run-batch":
            cmd = ["python3", str(SCRIPTS / "batch_weekly_all_ventures.py")]
            if body.get("render"):
                cmd.append("--render")
        elif path == "/run-opus-clip":
            vid = body.get("venture_id")
            if not vid:
                self._json(400, {"error": "venture_id required"})
                return
            cmd = [
                "python3",
                str(SCRIPTS / "opus_clip_runner.py"),
                "--venture-id",
                vid,
                "--stage",
                body.get("stage", "mof"),
                "--mode",
                body.get("mode", "auto"),
            ]
            if body.get("video_url"):
                cmd.extend(["--video-url", body["video_url"]])
        elif path == "/sync-supabase":
            cmd = ["python3", str(SCRIPTS / "sync_sqlite_to_supabase.py")]
        else:
            self._json(404, {"error": "unknown path", "routes": list(ROUTES)})
            return

        proc = subprocess.run(cmd, capture_output=True, text=True)
        self._json(
            200 if proc.returncode == 0 else 500,
            {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr, "cmd": cmd},
        )

    def log_message(self, fmt: str, *args) -> None:
        print(fmt % args)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    server = HTTPServer((args.host, args.port), Handler)
    print(f"Funnel webhook runner on http://{args.host}:{args.port}")
    print("GET  /health")
    print('POST /run-orchestrator {"auto":true,"render":true,"higgsfield":false,"opus_clip":true}')
    print('POST /run-weekly  {"venture_id":"...","day":"monday","render":false}')
    print("POST /run-batch    {}")
    print('POST /run-opus-clip {"venture_id":"...","stage":"mof","mode":"auto"}')
    print("POST /sync-supabase {}")
    server.serve_forever()


if __name__ == "__main__":
    main()
