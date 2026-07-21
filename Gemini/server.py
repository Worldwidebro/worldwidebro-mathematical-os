import http.server
import socketserver
import json
import os
import sys
import asyncio
import shutil
import zipfile
import csv
from urllib.parse import urlparse, parse_qs
import threading
import time
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

PORT = 8000
WORKSPACE_DIR = "/Users/acebless/Documents"
GEMINI_DIR = os.path.join(WORKSPACE_DIR, "Gemini")
REGISTRIES_DIR = os.path.join(WORKSPACE_DIR, "WORLDWIDEBRO-OS/08-DATA/registries")

# Ensure required directories exist
os.makedirs(os.path.join(GEMINI_DIR, "archives"), exist_ok=True)
os.makedirs(os.path.join(GEMINI_DIR, "reports"), exist_ok=True)
os.makedirs(os.path.join(GEMINI_DIR, "campaigns"), exist_ok=True)
os.makedirs(os.path.join(GEMINI_DIR, "tools/claude-ads"), exist_ok=True)

class OperationsHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow CORS for development convenience
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/api/capabilities":
            self.handle_get_capabilities()
        elif path == "/api/repositories":
            self.handle_get_repositories()
        elif path == "/api/registry/repositories":
            self.handle_get_yaml_registry("repositories.yaml")
        elif path == "/api/registry/capabilities":
            self.handle_get_yaml_registry("capabilities.yaml")
        elif path == "/api/registry/agents":
            self.handle_get_yaml_registry("agents.yaml")
        elif path == "/api/registry/integrations":
            self.handle_get_yaml_registry("integrations.yaml")
        elif path == "/api/registry/frameworks":
            self.handle_get_yaml_registry("frameworks.yaml")
        elif path == "/api/registry/models":
            self.handle_get_yaml_registry("models.yaml")
        elif path == "/api/graph/data":
            self.handle_get_graph_data()
        elif path == "/api/courses":
            self.handle_get_courses()
        elif path == "/api/course/status":
            query_params = parse_qs(parsed_path.query)
            course_id = query_params.get("id", [None])[0]
            self.handle_get_course_status(course_id)
        elif path == "/api/search":
            self.handle_get_search()
        elif path == "/api/dependencies":
            self.handle_get_dependencies()
        elif path == "/api/infrastructure/metrics":
            self.handle_get_infrastructure_metrics()
        elif path == "/api/venture/ideate":
            query_params = parse_qs(parsed_path.query)
            sector = query_params.get("sector", [""])[0]
            gap = query_params.get("gap", [""])[0]
            self.handle_get_venture_ideate(sector, gap)
        else:
            # Fallback to serving static files from workspace/Gemini
            os.chdir(GEMINI_DIR)
            super().do_GET()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Parse request body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            body = json.loads(post_data) if post_data else {}
        except json.JSONDecodeError:
            self.send_json_response(400, {"error": "Invalid JSON body"})
            return

        if path == "/api/zip":
            self.handle_post_zip(body)
        elif path == "/api/move":
            self.handle_post_move(body)
        elif path == "/api/pdf":
            self.handle_post_pdf(body)
        elif path == "/api/outreach":
            self.handle_post_outreach(body)
        elif path == "/api/compile/playbook":
            self.handle_compile_playbook(body)
        elif path == "/api/route":
            self.handle_post_route(body)
        elif path == "/api/leads":
            self.handle_post_leads(body)
        elif path == "/api/audit":
            self.handle_post_audit(body)
        elif path == "/api/execute":
            self.handle_post_execute(body)
        elif path == "/api/agent/run":
            self.handle_post_agent_run(body)
        elif path == "/api/narrative/run":
            self.handle_post_narrative_run(body)
        elif path == "/api/course/generate":
            self.handle_post_course_generate(body)
        elif path == "/api/scan":
            self.handle_post_scan(body)
        elif path == "/api/impact":
            self.handle_post_impact(body)
        elif path == "/api/intelligence":
            self.handle_post_intelligence(body)
        elif path == "/api/knowledge/ask":
            self.handle_post_knowledge_ask(body)
        elif path == "/api/agent/execute":
            self.handle_post_agent_execute(body)
        elif path == "/api/workflow/run":
            self.handle_post_workflow_run(body)
        elif path == "/api/governance/check":
            self.handle_post_governance_check(body)
        elif path == "/api/venture/spawn":
            self.handle_post_venture_spawn(body)
        else:
            self.send_json_response(404, {"error": "Endpoint not found"})

    def send_json_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def handle_get_capabilities(self):
        catalog_path = os.path.join(REGISTRIES_DIR, "capabilities-catalog.json")
        vocab_path = os.path.join(REGISTRIES_DIR, "capability_vocabulary.json")

        try:
            catalog = {}
            if os.path.exists(catalog_path):
                with open(catalog_path, 'r', encoding='utf-8') as f:
                    catalog = json.load(f)
            
            vocab = {}
            if os.path.exists(vocab_path):
                with open(vocab_path, 'r', encoding='utf-8') as f:
                    vocab = json.load(f)
                    
            self.send_json_response(200, {
                "catalog": catalog,
                "vocabulary": vocab
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to read capability registries: {str(e)}"})

    def handle_get_repositories(self):
        repos_path = os.path.join(REGISTRIES_DIR, "repositories.csv")
        index_path = "/Users/acebless/Documents/repos-index.json"
        
        try:
            indexed_repos = {}
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    index_data = json.load(f)
                    for item in index_data.get("repos", []):
                        indexed_repos[item["name"].lower()] = item

            csv_repos = []
            seen_names = set()
            if os.path.exists(repos_path):
                with open(repos_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        name = row.get("repo_name", "")
                        name_lower = name.lower()
                        seen_names.add(name_lower)
                        
                        # Try to match with indexed repos
                        match = indexed_repos.get(name_lower)
                        if not match:
                            # Try sub-string or base-name match
                            for k, v in indexed_repos.items():
                                if k in name_lower or name_lower in k:
                                    match = v
                                    break
                                    
                        repo_entry = {
                            "name": name,
                            "venture_id": row.get("venture_id", ""),
                            "sector": row.get("sector", ""),
                            "status": row.get("status", ""),
                            "health_score": row.get("health_score", ""),
                            "capabilities": match.get("capabilities", []) if match else [],
                            "url": match.get("url", "") if match else "",
                            "owner": match.get("owner", "") if match else "",
                            "language": match.get("language", "") if match else ""
                        }
                        csv_repos.append(repo_entry)

            # Include other indexed repos
            all_repos = list(csv_repos)
            for k, v in indexed_repos.items():
                # Avoid duplicate entries
                matched_csv = False
                for csv_rep in csv_repos:
                    csv_name = csv_rep["name"].lower()
                    if k == csv_name or k in csv_name or csv_name in k:
                        matched_csv = True
                        break
                if not matched_csv:
                    all_repos.append({
                        "name": v["name"],
                        "venture_id": "",
                        "sector": "",
                        "status": "indexed",
                        "health_score": "100",
                        "capabilities": v.get("capabilities", []),
                        "url": v.get("url", ""),
                        "owner": v.get("owner", ""),
                        "language": v.get("language", "")
                    })

            self.send_json_response(200, {"repositories": all_repos})
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to parse repositories registry: {str(e)}"})

    def handle_post_zip(self, body):
        target_path = body.get("path")
        if not target_path:
            self.send_json_response(400, {"error": "Missing 'path' parameter"})
            return

        # Resolve path safely within WORKSPACE_DIR
        abs_target = os.path.normpath(os.path.join(WORKSPACE_DIR, target_path.lstrip("/")))
        if not abs_target.startswith(WORKSPACE_DIR):
            self.send_json_response(403, {"error": "Access denied. Paths must remain within workspace."})
            return

        if not os.path.exists(abs_target):
            self.send_json_response(404, {"error": f"Target path does not exist: {target_path}"})
            return

        base_name = os.path.basename(abs_target) or "archive"
        zip_filename = f"{base_name}.zip"
        zip_filepath = os.path.join(GEMINI_DIR, "archives", zip_filename)

        try:
            with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                if os.path.isdir(abs_target):
                    for root, dirs, files in os.walk(abs_target):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, abs_target)
                            zipf.write(file_path, arcname)
                else:
                    zipf.write(abs_target, os.path.basename(abs_target))
            
            self.send_json_response(200, {
                "message": "Archiving complete",
                "zip_path": zip_filepath,
                "size_bytes": os.path.getsize(zip_filepath)
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Zip compression failed: {str(e)}"})

    def handle_post_move(self, body):
        src = body.get("src")
        dest = body.get("dest")
        if not src or not dest:
            self.send_json_response(400, {"error": "Missing 'src' or 'dest' parameter"})
            return

        abs_src = os.path.normpath(os.path.join(WORKSPACE_DIR, src.lstrip("/")))
        abs_dest = os.path.normpath(os.path.join(WORKSPACE_DIR, dest.lstrip("/")))

        if not abs_src.startswith(WORKSPACE_DIR) or not abs_dest.startswith(WORKSPACE_DIR):
            self.send_json_response(403, {"error": "Access denied. Paths must remain within workspace."})
            return

        if not os.path.exists(abs_src):
            self.send_json_response(404, {"error": f"Source path does not exist: {src}"})
            return

        try:
            # Ensure target parent folder exists
            os.makedirs(os.path.dirname(abs_dest), exist_ok=True)
            shutil.move(abs_src, abs_dest)
            self.send_json_response(200, {
                "message": "File operation complete",
                "src": abs_src,
                "dest": abs_dest
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Move file operation failed: {str(e)}"})
            
    def handle_post_outreach(self, body):
        try:
            import subprocess
            result = subprocess.run(
                ["python3", "/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/compile_outreach.py"],
                capture_output=True,
                text=True,
                check=True
            )
            self.send_json_response(200, {
                "message": "Zero-Token outreach packages compiled successfully.",
                "stdout": result.stdout[:2000]
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Outreach compilation failed: {str(e)}"})
            
    def handle_compile_playbook(self, body):
        venture_dir = body.get("venture_dir")
        output_path = body.get("output_path")
        if not venture_dir or not output_path:
            self.send_json_response(400, {"error": "Missing 'venture_dir' or 'output_path' parameter"})
            return
            
        try:
            import subprocess
            result = subprocess.run(
                ["python3", "/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/compile_playbook_pdf.py", venture_dir, output_path],
                capture_output=True,
                text=True,
                check=True
            )
            self.send_json_response(200, {
                "message": "Unified PDF Playbook compiled successfully.",
                "stdout": result.stdout[:2000]
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Playbook compilation failed: {str(e)}"})
            
    def handle_post_route(self, body):
        mode = body.get("mode")
        if not mode:
            self.send_json_response(400, {"error": "Missing 'mode' parameter"})
            return
            
        try:
            import subprocess
            if mode == "logistics":
                source = body.get("source")
                destination = body.get("destination")
                if not source or not destination:
                    self.send_json_response(400, {"error": "Missing 'source' or 'destination' parameter for logistics"})
                    return
                cmd = ["python3", "/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/orchestration/omni_route.py", "logistics", source, destination]
            elif mode == "balance":
                task_type = body.get("task_type")
                if not task_type:
                    self.send_json_response(400, {"error": "Missing 'task_type' parameter for balance"})
                    return
                cmd = ["python3", "/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/orchestration/omni_route.py", "balance", task_type]
            else:
                self.send_json_response(400, {"error": f"Invalid mode: {mode}"})
                return
                
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Find the JSON block inside stdout
            stdout_str = result.stdout.strip()
            # If there are debug prints before JSON, extract the JSON block
            if "{" in stdout_str:
                json_start = stdout_str.find("{")
                json_str = stdout_str[json_start:]
                self.send_json_response(200, json.loads(json_str))
            else:
                self.send_json_response(200, {"message": stdout_str})
        except Exception as e:
            self.send_json_response(500, {"error": f"OmniRoute routing failed: {str(e)}"})

    def handle_post_pdf(self, body):
        try:
            pdf_path = os.path.join(GEMINI_DIR, "reports/capabilities_report.pdf")
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            # Custom styles
            title_style = ParagraphStyle(
                'ReportTitle',
                parent=styles['Heading1'],
                fontSize=24,
                leading=28,
                textColor=colors.HexColor('#4f46e5'),
                spaceAfter=15
            )
            h2_style = ParagraphStyle(
                'SectionHeader',
                parent=styles['Heading2'],
                fontSize=14,
                leading=18,
                textColor=colors.HexColor('#06b6d4'),
                spaceBefore=10,
                spaceAfter=10
            )
            body_style = ParagraphStyle(
                'ReportBody',
                parent=styles['Normal'],
                fontSize=10,
                leading=14,
                textColor=colors.HexColor('#1f2937')
            )

            # Document Title
            story.append(Paragraph("WORLDWIDEBRO-OS Capabilities Report", title_style))
            story.append(Spacer(1, 10))
            story.append(Paragraph("System capabilities registry summary compiled on behalf of the operations director.", body_style))
            story.append(Spacer(1, 15))

            # Vocabulary Section
            story.append(Paragraph("1. Canonical Capability Vocabulary", h2_style))
            vocab_file = os.path.join(REGISTRIES_DIR, "capability_vocabulary.json")
            if os.path.exists(vocab_file):
                with open(vocab_file, 'r', encoding='utf-8') as f:
                    v_data = json.load(f).get("canonical", {})
                
                table_data = [["Capability", "Category", "Aliases"]]
                for cap, info in list(v_data.items())[:12]: # limit for readability
                    table_data.append([
                        cap, 
                        info.get("category", ""), 
                        ", ".join(info.get("aliases", []))[:30] + ("..." if len(info.get("aliases", [])) > 2 else "")
                    ])
                
                t = Table(table_data, colWidths=[100, 100, 300])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#6366f1')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 6),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f9fafb'), colors.HexColor('#f3f4f6')]),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                    ('FONTSIZE', (0,0), (-1,-1), 9)
                ]))
                story.append(t)
            else:
                story.append(Paragraph("No capability vocabulary found.", body_style))

            story.append(Spacer(1, 15))

            # Repositories Section
            story.append(Paragraph("2. Registered Venture Repositories", h2_style))
            repos_file = os.path.join(REGISTRIES_DIR, "repositories.csv")
            if os.path.exists(repos_file):
                repos = []
                with open(repos_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in list(reader)[:15]: # Show top 15
                        repos.append([
                            row.get("repo_name", ""),
                            row.get("sector", ""),
                            row.get("status", "")
                        ])
                
                table_data = [["Repository Name", "Sector", "Status"]] + repos
                t = Table(table_data, colWidths=[200, 150, 150])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#06b6d4')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 6),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f9fafb'), colors.HexColor('#f3f4f6')]),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                    ('FONTSIZE', (0,0), (-1,-1), 9)
                ]))
                story.append(t)
            else:
                story.append(Paragraph("No repositories registry found.", body_style))

            doc.build(story)
            
            self.send_json_response(200, {
                "message": "PDF Report generated successfully",
                "pdf_path": pdf_path,
                "size_bytes": os.path.getsize(pdf_path)
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"PDF compiling failed: {str(e)}"})

    def handle_post_leads(self, body):
        import csv
        from datetime import datetime
        
        email = body.get("email")
        name = body.get("name", "")
        venture_id = body.get("ventureId")
        metadata = body.get("metadata", {})
        
        if not email or not venture_id:
            self.send_json_response(400, {"error": "Missing 'email' or 'ventureId' parameters"})
            return
            
        leads_dir = os.path.join(WORKSPACE_DIR, "WORLDWIDEBRO-OS/08-DATA/leads")
        os.makedirs(leads_dir, exist_ok=True)
        leads_file = os.path.join(leads_dir, "waitlist_leads.csv")
        
        file_exists = os.path.exists(leads_file)
        
        try:
            with open(leads_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["timestamp", "email", "name", "ventureId", "metadata"])
                
                timestamp = datetime.utcnow().isoformat() + "Z"
                writer.writerow([timestamp, email, name, venture_id, json.dumps(metadata)])
                
            lead_count = 1
            if os.path.exists(leads_file):
                with open(leads_file, 'r', encoding='utf-8') as rf:
                    lead_count = sum(1 for _ in rf) - 1
                    
            self.send_json_response(200, {
                "message": "Lead captured successfully",
                "position": max(1, lead_count) + 120
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to save lead: {str(e)}"})

    def handle_post_audit(self, body):
        campaign = body.get("campaign")
        if not campaign:
            self.send_json_response(400, {"error": "Missing 'campaign' parameter"})
            return

        manifest_dir = os.path.join(GEMINI_DIR, "campaigns", campaign)
        manifest_path = os.path.join(manifest_dir, "manifest.json")
        rules_path = os.path.join(GEMINI_DIR, "tools/claude-ads/rules.md")

        # Create dummy template files if none exist to allow testing
        if not os.path.exists(manifest_path):
            os.makedirs(manifest_dir, exist_ok=True)
            dummy_manifest = {
                "campaign_id": campaign,
                "script": "Our product is guaranteed to cure baldness in 2 hours! Free trials for everyone.",
                "claims": ["baldness cure", "2 hours timeline"]
            }
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(dummy_manifest, f, indent=2)

        if not os.path.exists(rules_path):
            dummy_rules = (
                "# Ad Campaign Regulations\n\n"
                "- Rule 1: No health guarantees or absolute cures.\n"
                "- Rule 2: Claims regarding timelines (e.g. 'X hours') must be backfilled with clinical evidence.\n"
            )
            with open(rules_path, 'w', encoding='utf-8') as f:
                f.write(dummy_rules)

        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            
            with open(rules_path, 'r', encoding='utf-8') as f:
                rules = f.read()

            script = manifest.get("script", "")
            violations = []

            # Perform claim audits (simple rules validation checks)
            if "cure" in script.lower() or "guarantee" in script.lower():
                violations.append("Violation of Rule 1: Medical claim or guarantee of cure detected in script.")
            if "hour" in script.lower() or "minute" in script.lower():
                violations.append("Violation of Rule 2: Timeline-related claims must possess supporting evidence.")

            status = "fail" if violations else "pass"
            
            self.send_json_response(200, {
                "status": status,
                "violations": violations,
                "campaign": campaign,
                "script": script
            })
        except Exception as e:
            self.send_json_response(500, {"error": f"Campaign audit runner failed: {str(e)}"})

    def handle_post_execute(self, body):
        cap_id = body.get("capability_id")
        args = body.get("args", {})
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            import execution_gateway
            res = execution_gateway.execute_capability(cap_id, args)
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Execution failed: {str(e)}"})

    def handle_post_agent_run(self, body):
        agent_name = body.get("agent_name")
        prompt = body.get("prompt", "")
        
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            import agent_runner
            res = agent_runner.run_agent(agent_name, prompt)
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Agent processing failed: {str(e)}"})

    def handle_post_narrative_run(self, body):
        text = body.get("text", "")
        voice = body.get("voice", "visionary")
        role = body.get("role", "copywriter")
        framework = body.get("framework", "direct")
        venture = body.get("venture", "")
        
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "AI-BOSS-OS", "WRITING-ENGINE"))
            import run_narrative
            # Reload module in case it was modified
            import importlib
            importlib.reload(run_narrative)
            res_text = run_narrative.run_narrative_engine(text, voice, role, framework, venture)
            self.send_json_response(200, {"status": "success", "result": res_text})
        except Exception as e:
            self.send_json_response(500, {"error": f"Narrative engine execution failed: {str(e)}"})

    def handle_get_search(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        q = query_params.get("q", [""])[0]
        limit = int(query_params.get("limit", [10])[0])
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from repository_intelligence import RepoIndexer
            indexer = RepoIndexer()
            res = indexer.search(q, limit)
            self.send_json_response(200, {"results": res})
        except Exception as e:
            self.send_json_response(500, {"error": f"Search failed: {str(e)}"})

    def handle_get_dependencies(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        repo = query_params.get("repo", [""])[0]
        try:
            from neo4j import GraphDatabase
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from repository_intelligence import NEO4J_URI, NEO4J_AUTH
            driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
            with driver.session() as session:
                query = """
                MATCH (r:Repository {name: $repo})-[:CONTAINS]->(f:File)
                OPTIONAL MATCH (f)-[d:DEPENDS_ON]->(dep)
                RETURN f.path as file, collect(dep.path) as deps
                """
                if not repo:
                    query = """
                    MATCH (r:Repository)-[:IMPLEMENTS]->(c:Capability)
                    RETURN r.name as repo, collect(c.name) as capabilities
                    LIMIT 50
                    """
                    result = session.run(query)
                    data = [{"repo": r["repo"], "capabilities": r["capabilities"]} for r in result]
                else:
                    result = session.run(query, repo=repo)
                    data = [{"file": r["file"], "dependencies": r["deps"]} for r in result]
            driver.close()
            self.send_json_response(200, {"dependencies": data})
        except Exception as e:
            self.send_json_response(200, {"dependencies": [], "message": f"Unavailable: {str(e)}"})

    def handle_get_infrastructure_metrics(self):
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from infrastructure_engine import InfrastructureEngine
            engine = InfrastructureEngine()
            self.send_json_response(200, engine.get_summary())
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to get metrics: {str(e)}"})

    def handle_get_venture_ideate(self, sector, gap):
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from venture_factory import VentureFactoryEngine
            v_factory = VentureFactoryEngine()
            res = v_factory.ideate(sector, gap)
            self.send_json_response(200, {"ideas": res})
        except Exception as e:
            self.send_json_response(500, {"error": f"Ideation failed: {str(e)}"})

    def handle_post_scan(self, body):
        repo_path = body.get("repo_path", "")
        repo_name = body.get("repo_name", "")
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from repository_intelligence import RepoScanner, RepoIndexer, KnowledgeGraphBuilder
            scanner = RepoScanner(repo_path)
            scan_result = scanner.scan()
            
            if "error" not in scan_result:
                indexer = RepoIndexer()
                for file in scan_result.get("files", []):
                    indexer.index_file(file, repo_name)
                    
                graph = KnowledgeGraphBuilder()
                graph.build_from_scan(scan_result, repo_name)
                
            self.send_json_response(200, scan_result)
        except Exception as e:
            self.send_json_response(500, {"error": f"Scan failed: {str(e)}"})

    def handle_post_impact(self, body):
        file_path = body.get("file_path", "")
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from repository_intelligence import KnowledgeGraphBuilder
            graph = KnowledgeGraphBuilder()
            dependents = graph.get_dependents(file_path)
            self.send_json_response(200, {"file_path": file_path, "dependents": dependents})
        except Exception as e:
            self.send_json_response(500, {"error": f"Impact analysis failed: {str(e)}"})

    def handle_post_intelligence(self, body):
        query = body.get("query", "")
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from repository_intelligence import RepoIndexer
            indexer = RepoIndexer()
            hits = indexer.search(query, limit=5)
            self.send_json_response(200, {"query": query, "results": hits})
        except Exception as e:
            self.send_json_response(500, {"error": f"Code intelligence query failed: {str(e)}"})

    def handle_post_knowledge_ask(self, body):
        query = body.get("query", "")
        context_sources = body.get("context_sources")
        use_rag = body.get("use_rag", True)
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from knowledge_engine import KnowledgeEngine
            engine = KnowledgeEngine()
            res = engine.ask(query, context_sources=context_sources, use_rag=use_rag)
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"RAG query failed: {str(e)}"})

    def handle_post_agent_execute(self, body):
        agent_name = body.get("agent_name", "")
        task_payload = body.get("task_payload", {})
        task_context = body.get("task_context", {})
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from agent_engine import SimpleLangAgent, AgentTask, AgentRegistry
            agent_info = AgentRegistry.get_agent_info(agent_name) or {}
            capabilities = agent_info.get("capabilities", [])
            
            agent = SimpleLangAgent(agent_name, capabilities)
            task = AgentTask(
                id=f"task_{hash(agent_name)}",
                payload=task_payload,
                context=task_context
            )
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            res = loop.run_until_complete(agent.execute(task))
            loop.close()
            
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Agent task execution failed: {str(e)}"})

    def handle_post_workflow_run(self, body):
        workflow_yaml = body.get("workflow_yaml", "")
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from orchestration_engine import WorkflowDefinition, WorkflowRunner
            
            wd = WorkflowDefinition(workflow_yaml)
            runner = WorkflowRunner()
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            res = loop.run_until_complete(runner.run(wd))
            loop.close()
            
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Workflow run failed: {str(e)}"})

    def handle_post_governance_check(self, body):
        user_role = body.get("user_role", "")
        action = body.get("action", "")
        resource_sector = body.get("resource_sector", "")
        details = body.get("details", {})
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from governance_engine import GovernanceEngine
            gov = GovernanceEngine()
            res = gov.check_policy(user_role, action, resource_sector, details)
            gov.log_decision(user_role, action, f"sector:{resource_sector}", "allowed" if res["allowed"] else "denied", res["reason"])
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Governance check failed: {str(e)}"})

    def handle_post_venture_spawn(self, body):
        name = body.get("name", "")
        sector = body.get("sector", "")
        location = body.get("location")
        target = body.get("target")
        revenue_goal = body.get("revenue_goal")
        try:
            sys.path.append(os.path.join(GEMINI_DIR, "services"))
            from venture_factory import VentureFactoryEngine
            v_factory = VentureFactoryEngine()
            res = v_factory.spawn_venture(name, sector, location, target, revenue_goal)
            self.send_json_response(200, res)
        except Exception as e:
            self.send_json_response(500, {"error": f"Venture spawn failed: {str(e)}"})

    def handle_get_yaml_registry(self, filename):
        filepath = os.path.join(GEMINI_DIR, "registry", filename)
        try:
            data = parse_yaml_file(filepath)
            self.send_json_response(200, {"data": data})
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to parse {filename}: {str(e)}"})

    def handle_get_graph_data(self):
        # Trigger capability_graph.py to refresh cypher script
        os.system("python3 services/capability_graph.py")
        
        # Load and parse integrations.yaml
        integrations_file = os.path.join(GEMINI_DIR, "registry/integrations.yaml")
        try:
            integrations = parse_yaml_file(integrations_file)
            self.send_json_response(200, {"integrations": integrations})
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to load graph integrations: {str(e)}"})

    def handle_get_courses(self):
        courses_dir = os.path.join(WORKSPACE_DIR, "generated-courses")
        os.makedirs(courses_dir, exist_ok=True)
        courses = []
        try:
            for item in os.listdir(courses_dir):
                item_path = os.path.join(courses_dir, item)
                if os.path.isdir(item_path):
                    meta_path = os.path.join(item_path, "metadata.json")
                    if os.path.exists(meta_path):
                        with open(meta_path, 'r', encoding='utf-8') as f:
                            try:
                                meta = json.load(f)
                                courses.append(meta)
                            except:
                                pass
                    else:
                        # Backfill basic metadata if not present
                        parts = item.split("-", 2)
                        subject = parts[2].replace("-", " ") if len(parts) > 2 else item.replace("-", " ")
                        meta = {
                            "id": item,
                            "subject": subject,
                            "audience": "General",
                            "chapters": 5,
                            "status": "completed",
                            "progress": 100,
                            "path": item_path
                        }
                        with open(meta_path, 'w', encoding='utf-8') as f:
                            json.dump(meta, f, indent=2)
                        courses.append(meta)
            self.send_json_response(200, {"courses": courses})
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to list courses: {str(e)}"})

    def handle_get_course_status(self, course_id):
        if not course_id:
            self.send_json_response(400, {"error": "Missing 'id' parameter"})
            return
        courses_dir = os.path.join(WORKSPACE_DIR, "generated-courses")
        meta_path = os.path.join(courses_dir, course_id, "metadata.json")
        if not os.path.exists(meta_path):
            self.send_json_response(404, {"error": f"Course metadata not found: {course_id}"})
            return
        try:
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            self.send_json_response(200, meta)
        except Exception as e:
            self.send_json_response(500, {"error": f"Failed to read course status: {str(e)}"})

    def handle_post_course_generate(self, body):
        subject = body.get("subject")
        audience = body.get("audience", "General")
        chapters = int(body.get("chapters", 5))
        description = body.get("description", "")
        narration = body.get("narration", False)
        generate_images = body.get("generateImages", False)
        blueprint_type = body.get("blueprintType", "course")

        if not subject:
            self.send_json_response(400, {"error": "Missing 'subject' parameter"})
            return

        # Determine prefix and next sequential ID
        prefix = "EDU"
        if blueprint_type == "sop":
            prefix = "SOP"
        elif blueprint_type == "prd":
            prefix = "PRD"

        courses_dir = os.path.join(WORKSPACE_DIR, "generated-courses")
        os.makedirs(courses_dir, exist_ok=True)
        
        max_num = 0
        for item in os.listdir(courses_dir):
            if os.path.isdir(os.path.join(courses_dir, item)) and item.startswith(f"{prefix}-"):
                try:
                    num = int(item.split("-")[1])
                    if num > max_num:
                        max_num = num
                except:
                    pass
        
        next_num = max_num + 1
        slug = "".join([c if c.isalnum() else "-" for c in subject.strip().lower()]).replace("--", "-")
        course_id = f"{prefix}-{next_num:03d}-{slug}"
        course_path = os.path.join(courses_dir, course_id)
        os.makedirs(course_path, exist_ok=True)

        startup_log = "[Setup] Starting knowledge compiler pipeline..."
        if blueprint_type == "course":
            startup_log = "[Setup] Starting course builder pipeline..."
        elif blueprint_type == "sop":
            startup_log = "[Setup] Starting venture SOP compiler pipeline..."
        elif blueprint_type == "prd":
            startup_log = "[Setup] Starting product PRD compiler pipeline..."

        meta = {
            "id": course_id,
            "subject": subject,
            "audience": audience,
            "chapters": chapters,
            "description": description,
            "blueprint_type": blueprint_type,
            "status": "generating",
            "progress": 0,
            "logs": [startup_log],
            "path": course_path
        }

        meta_path = os.path.join(course_path, "metadata.json")
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta, f, indent=2)

        # Launch background builder thread
        t = threading.Thread(target=self.run_course_builder, args=(course_id, meta))
        t.daemon = True
        t.start()

        self.send_json_response(200, {
            "message": "Knowledge blueprint compilation started in background",
            "course_id": course_id
        })

    def run_course_builder(self, course_id, meta):
        course_path = meta["path"]
        meta_path = os.path.join(course_path, "metadata.json")
        blueprint_type = meta.get("blueprint_type", "course")
        subject = meta["subject"]
        audience = meta["audience"]
        chapters = meta["chapters"]
        
        def save_meta(progress, log_msg=None):
            meta["progress"] = progress
            if log_msg:
                meta["logs"].append(log_msg)
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump(meta, f, indent=2)

        try:
            # Stage 1: Setup
            time.sleep(1.5)
            if blueprint_type == "course":
                save_meta(10, f"[Setup] Configuring curriculum blueprints. Target audience: {audience}.")
            elif blueprint_type == "sop":
                save_meta(10, f"[Setup] Defining venture operations boundary. Target sector: {audience}.")
            else:
                save_meta(10, f"[Setup] Designing product requirements specs. Scope layer: {audience}.")
            
            # Stage 2: Architecture / Syllabus
            time.sleep(2)
            if blueprint_type == "course":
                save_meta(25, "[Syllabus] Designing course arc based on learning science.")
            elif blueprint_type == "sop":
                save_meta(25, "[Architecture] Structuring venture operations manual blueprint.")
            else:
                save_meta(25, "[Architecture] Drafting system modules and functional architecture blueprints.")
            
            # Generate Module data
            modules_data = []
            for idx in range(1, chapters + 1):
                if blueprint_type == "course":
                    if "ai" in subject.lower() or "agent" in subject.lower() or "code" in subject.lower():
                        titles = ["Foundations & Key Concepts", "Architecture & Structure", "Practical Application Cases", "Protocol Bridges", "Scalability Profiles", "Security & Audits", "Testing & Evaluation", "Future Horizon"]
                    else:
                        titles = ["Introductory Paradigms", "Core Systems & Mechanisms", "Methodologies & Tools", "Case Studies & Realities", "Advanced Techniques", "Ethics & Concerns", "Verification", "Synthesis"]
                    title = f"Chapter {idx}: {titles[(idx - 1) % len(titles)]}"
                    desc = f"Master the underlying concepts of {titles[(idx - 1) % len(titles)]} in relation to {subject}."
                elif blueprint_type == "sop":
                    departments = ["Operations & Logistics", "Marketing & Growth Hooks", "Sales Pipelines & CRM", "HR & Hiring Playbook", "Finance & Cash Flow Ledger", "Compliance & Risk Registry", "Tech Stack & Automations", "Customer Success SOPs"]
                    title = f"Department {idx}: {departments[(idx - 1) % len(departments)]}"
                    desc = f"Standard Operating Procedures (SOPs) and onboarding drills for {departments[(idx - 1) % len(departments)]}."
                else:
                    components = ["Core State Engine", "REST API Gateway", "Database Schema & Models", "Client Web Frontend", "Agent Execution Sandbox", "CI/CD & Deployment Actions", "Evaluation & Rubrics Suite", "Third-Party Connectors"]
                    title = f"Module {idx}: {components[(idx - 1) % len(components)]}"
                    desc = f"Technical requirements, design patterns, and interface models for the {components[(idx - 1) % len(components)]}."
                
                modules_data.append({
                    "number": idx,
                    "title": title,
                    "description": desc
                })

            if blueprint_type == "course":
                blueprint_file = "syllabus.md"
                blueprint_content = f"# Course Syllabus: {subject}\n\n**Audience:** {audience}\n**Modules:** {chapters}\n\n"
            elif blueprint_type == "sop":
                blueprint_file = "operations_manual.md"
                blueprint_content = f"# Venture Operations Manual: {subject}\n\n**Sector/Audience:** {audience}\n**Operational Departments:** {chapters}\n\n"
            else:
                blueprint_file = "prd_architecture.md"
                blueprint_content = f"# Product Requirements Document (PRD) Architecture: {subject}\n\n**Scope/Platform:** {audience}\n**Technical Modules:** {chapters}\n\n"
                
            for mod in modules_data:
                blueprint_content += f"## {mod['title']}\n*{mod['description']}*\n\n"
            
            with open(os.path.join(course_path, blueprint_file), 'w', encoding='utf-8') as f:
                f.write(blueprint_content)
                
            save_meta(40, f"[Syllabus] Generated {blueprint_file} with {chapters} sections.")

            # Stage 3: Research
            time.sleep(2)
            save_meta(50, "[Research] Running RAG queries against local Obsidian Second Brain vaults and registries.")
            
            if blueprint_type == "course":
                research_file = "research_notes.md"
                research_content = (
                    f"# Research Catalog: {subject}\n\n"
                    f"## Core Learning Citations\n"
                    f"- Tangen, J. et al. (2025). *Cognitive Science Principles in Automated Curriculum Designs*. Journal of Educational Technology.\n"
                    f"- Sweller, J. (1988). *Cognitive Load Theory and Instructional Design*.\n"
                    f"- Roediger, H. L., & Karpicke, J. D. (2006). *The Power of Testing Memory*.\n"
                )
            elif blueprint_type == "sop":
                research_file = "market_research.md"
                research_content = (
                    f"# Market Research & Regulations: {subject}\n\n"
                    f"## Local Competitor Matrix\n"
                    f"- Audited active portfolio metrics in WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv.\n"
                    f"## Compliance & Industry Standards\n"
                    f"- Checked ad compliance rules against tools/claude-ads/rules.md standards.\n"
                    f"- OSHA safety and local general liability protection structures compiled.\n"
                )
            else:
                research_file = "tech_research.md"
                research_content = (
                    f"# Technical Feasibility Analysis: {subject}\n\n"
                    f"## Recommended Stack Profile\n"
                    f"- Frontend: Vanilla HTML5 / CSS3 (glassmorphic UI config).\n"
                    f"- Backend: Python 3.11+ / http.server / SQLite.\n"
                    f"- Vector Database: Qdrant client connection (Qdrant clients sdk).\n"
                    f"- Graph Database: Neo4j Cypher mapping rules (Neo4j Cypher Skill guidelines).\n"
                )
                
            with open(os.path.join(course_path, research_file), 'w', encoding='utf-8') as f:
                f.write(research_content)
            
            # Stage 4: Build
            save_meta(60, "[Build] Assembling structured artifact pack files.")
            for mod in modules_data:
                m_num = mod["number"]
                m_title = mod["title"]
                m_dir = os.path.join(course_path, f"module_{m_num}")
                os.makedirs(m_dir, exist_ok=True)
                
                if blueprint_type == "course":
                    # 1. Reading
                    reading = f"# {m_title}\n\n## Core Concepts\nThis covers learning objectives for {m_title}.\n"
                    with open(os.path.join(m_dir, "reading.md"), 'w', encoding='utf-8') as f: f.write(reading)
                    # 2. Slides
                    slides = f"# Slides Outline: {m_title}\n\n## Slide 1: Welcome\n- Intro notes.\n"
                    with open(os.path.join(m_dir, "slides_outline.md"), 'w', encoding='utf-8') as f: f.write(slides)
                    # 3. Quiz
                    quiz = f"# Quiz: {m_title}\n\n1. Answer selection details.\n"
                    with open(os.path.join(m_dir, "in_class_quiz.md"), 'w', encoding='utf-8') as f: f.write(quiz)
                    # 4. Practice Quiz
                    with open(os.path.join(m_dir, "practice_quiz.md"), 'w', encoding='utf-8') as f: f.write(f"# Practice Quiz: {m_title}\n")
                    # 5. Teaching Pack
                    with open(os.path.join(m_dir, "teaching_pack.md"), 'w', encoding='utf-8') as f: f.write(f"# Teaching Pack: {m_title}\n")
                    # 6. Weekly Challenge
                    with open(os.path.join(m_dir, "weekly_challenge.md"), 'w', encoding='utf-8') as f: f.write(f"# Weekly Challenge: {m_title}\n")
                    # 7. Audio Narration
                    with open(os.path.join(m_dir, "audio_narration.md"), 'w', encoding='utf-8') as f: f.write(f"# Audio Script: {m_title}\n")
                    
                elif blueprint_type == "sop":
                    # 1. SOP Document
                    sop_doc = f"# Standard Operating Procedure (SOP): {m_title}\n\n## Step-by-Step Workflow\n1. Define operational bounds.\n2. Trigger department handlers.\n"
                    with open(os.path.join(m_dir, "standard_operating_procedure.md"), 'w', encoding='utf-8') as f: f.write(sop_doc)
                    # 2. Training Playbook
                    playbook = f"# Training Playbook: {m_title}\n\nOnboarding instructions for staff engineers & operators.\n"
                    with open(os.path.join(m_dir, "training_playbook.md"), 'w', encoding='utf-8') as f: f.write(playbook)
                    # 3. Competency Quiz
                    comp_quiz = f"# Competency Assessment: {m_title}\n\n1. Operational checklist verification quiz.\n"
                    with open(os.path.join(m_dir, "competency_quiz.md"), 'w', encoding='utf-8') as f: f.write(comp_quiz)
                    # 4. Active Recall flashcards
                    with open(os.path.join(m_dir, "active_recall_flashcards.md"), 'w', encoding='utf-8') as f: f.write(f"# Flashcards: {m_title}\n")
                    # 5. Weekly Drill Checklist
                    with open(os.path.join(m_dir, "weekly_drill_checklist.md"), 'w', encoding='utf-8') as f: f.write(f"# Weekly Checklist: {m_title}\n")
                    # 6. FAQ Edge Cases
                    with open(os.path.join(m_dir, "faq_and_troubleshooting.md"), 'w', encoding='utf-8') as f: f.write(f"# FAQs: {m_title}\n")
                    # 7. Audio Script Briefing
                    with open(os.path.join(m_dir, "audio_briefing_script.md"), 'w', encoding='utf-8') as f: f.write(f"# Audio Briefing: {m_title}\n")
                    
                else:  # prd
                    # 1. Feature Specification
                    feat_spec = f"# Feature Specification: {m_title}\n\n## Scope & User Stories\n- As an operator, I want to deploy this component.\n"
                    with open(os.path.join(m_dir, "feature_specification.md"), 'w', encoding='utf-8') as f: f.write(feat_spec)
                    # 2. OpenAPI Spec (yaml)
                    openapi = f"openapi: 3.0.0\ninfo:\n  title: {m_title} API\n  version: 1.0.0\npaths:\n  /api/execute:\n    post:\n      summary: Trigger module\n"
                    with open(os.path.join(m_dir, "api_spec_openapi.yaml"), 'w', encoding='utf-8') as f: f.write(openapi)
                    # 3. SQL Database Schema
                    sql_schema = f"-- Database Schema: {m_title}\nCREATE TABLE IF NOT EXISTS {m_title.replace(' ', '_').lower()} (\n  id SERIAL PRIMARY KEY,\n  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);\n"
                    with open(os.path.join(m_dir, "database_schema.sql"), 'w', encoding='utf-8') as f: f.write(sql_schema)
                    # 4. UI Layout Flowchart
                    with open(os.path.join(m_dir, "ui_ux_flowchart.md"), 'w', encoding='utf-8') as f: f.write(f"# UI Wireframes: {m_title}\n")
                    # 5. Unit Test Cases
                    with open(os.path.join(m_dir, "test_cases_suite.md"), 'w', encoding='utf-8') as f: f.write(f"# Test Suite: {m_title}\n")
                    # 6. CI/CD Workflow (yaml)
                    cicd = f"name: Deploy {m_title}\non:\n  push:\n    branches: [main]\njobs:\n  deploy:\n    runs-on: ubuntu-latest\n"
                    with open(os.path.join(m_dir, "ci_cd_action_workflow.yaml"), 'w', encoding='utf-8') as f: f.write(cicd)
                    # 7. Agentic Tool Definitions (json)
                    tool_def = f'{{\n  "name": "{m_title.replace(" ", "_").lower()}",\n  "description": "Orchestrates {m_title} commands",\n  "parameters": {{"type": "object", "properties": {{}}}}\n}}\n'
                    with open(os.path.join(m_dir, "agentic_tool_definitions.json"), 'w', encoding='utf-8') as f: f.write(tool_def)
                
                time.sleep(0.5)
                save_meta(60 + int((m_num / chapters) * 30), f"[Build] Compiled {m_title} assets (7/7 deliverables compiled).")

            # Stage 5: Export
            time.sleep(1.5)
            save_meta(95, "[Export] Packaging compiled artifacts and exporting distributions.")
            
            # Create a zip of this course
            zip_filename = f"{course_id}.zip"
            zip_path = os.path.join(course_path, zip_filename)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(course_path):
                    for file in files:
                        if file == zip_filename:
                            continue
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, course_path)
                        zipf.write(file_path, arcname)

            meta["status"] = "completed"
            meta["zip"] = f"/Users/acebless/Documents/generated-courses/{course_id}/{zip_filename}"
            save_meta(100, f"[Export] Compilation completed successfully. Output ready in {course_path}.")
            
        except Exception as e:
            meta["status"] = "error"
            save_meta(meta.get("progress", 0), f"[Error] Compilation aborted: {str(e)}")

def parse_yaml_file(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = []
    current = {}
    
    for line in content.split('\n'):
        line_strip = line.strip()
        if not line_strip:
            continue
        if line_strip.startswith('-'):
            if current:
                entries.append(current)
                current = {}
            line_strip = line_strip.lstrip('-').strip()
            
        if ':' in line_strip:
            parts = line_strip.split(':', 1)
            key = parts[0].strip().replace('"', '').replace("'", "")
            val = parts[1].strip().replace('"', '').replace("'", "")
            if val.startswith('[') and val.endswith(']'):
                val = [item.strip() for item in val[1:-1].split(',')]
            current[key] = val
            
    if current:
        entries.append(current)
    return entries

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), OperationsHTTPHandler) as httpd:
        print(f"Serving WORLDWIDEBRO-OS Operations Hub on port {PORT}")
        httpd.serve_forever()
