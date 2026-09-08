#!/usr/bin/env python3
"""
DealFlowOS Neo4j API Server

REST API wrapper for DealFlowOS dashboard to query:
- Companies (148 researched)
- Deal pipeline by stage
- Company enrichment details
"""

import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from neo4j import GraphDatabase

# Neo4j connection
NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://100.87.214.70:7687')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'ventures2026')

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def get_companies(limit=150):
    """Query Neo4j for all researched ventures (companies)"""
    with driver.session() as session:
        result = session.run("""
            MATCH (v:Venture)
            OPTIONAL MATCH (v)-[r:HAS_CAPABILITY]->(cap:Capability)
            OPTIONAL MATCH (v)-[r2:IN_SECTOR]->(sec:Sector)
            RETURN
                v.id as id,
                v.name as name,
                v.sector_tags as industry,
                v.website as website,
                COALESCE(v.research_score, 75) as score,
                v.location as location,
                sec.name as sector,
                COUNT(DISTINCT cap) as capabilities,
                COALESCE(v.stage, 'discovered') as stage
            LIMIT $limit
        """, limit=limit)

        companies = []
        for record in result:
            companies.append({
                'id': record['id'],
                'name': record['name'],
                'industry': record['industry'] or 'unknown',
                'website': record['website'] or '',
                'score': int(record['score']) if record['score'] else 75,
                'location': record['location'] or 'Unknown',
                'sector': record['sector'] or 'General',
                'capabilities': record['capabilities'],
                'stage': record['stage'] or 'discovered'
            })

        return sorted(companies, key=lambda x: x['score'], reverse=True)

def get_company_details(company_id):
    """Get detailed enrichment for a single venture (company)"""
    with driver.session() as session:
        result = session.run("""
            MATCH (v:Venture {id: $id})
            OPTIONAL MATCH (v)-[r:HAS_CAPABILITY]->(cap:Capability)
            OPTIONAL MATCH (v)-[r2:IN_SECTOR]->(sec:Sector)
            OPTIONAL MATCH (v)-[r3:HAS_CONTACT]->(con)
            RETURN
                v.id as id,
                v.name as name,
                v.sector_tags as industry,
                v.website as website,
                v.founded_year as founded,
                v.employee_count as employees,
                COALESCE(v.research_score, 75) as score,
                v.description as summary,
                COLLECT(DISTINCT {name: cap.name, type: cap.type}) as capabilities,
                v.location as location,
                sec.name as sector,
                COLLECT(DISTINCT {name: con.name, email: con.email, title: con.title}) as contacts,
                COALESCE(v.stage, 'discovered') as stage
        """, id=company_id)

        record = result.single()
        if not record:
            return None

        return {
            'id': record['id'],
            'name': record['name'],
            'industry': record['industry'],
            'website': record['website'] or '',
            'founded': record['founded'],
            'employees': record['employees'],
            'score': int(record['score']) if record['score'] else 75,
            'summary': record['summary'] or '',
            'location': record['location'] or 'Unknown',
            'sector': record['sector'] or 'General',
            'capabilities': [c for c in record['capabilities'] if c['name']],
            'contacts': [c for c in record['contacts'] if c['name']],
            'stage': record['stage']
        }

def get_pipeline_by_stage():
    """Get deal pipeline grouped by stage"""
    with driver.session() as session:
        result = session.run("""
            MATCH (v:Venture)
            WITH COALESCE(v.stage, 'discovered') as stage, v
            RETURN
                stage,
                COUNT(v) as count,
                COLLECT({
                    id: v.id,
                    name: v.name,
                    score: COALESCE(v.research_score, 75),
                    industry: COALESCE(v.sector_tags, 'unknown')
                }) as ventures
            ORDER BY CASE stage
                WHEN 'discovered' THEN 1
                WHEN 'researched' THEN 2
                WHEN 'qualified' THEN 3
                WHEN 'contacted' THEN 4
                WHEN 'negotiating' THEN 5
                WHEN 'closed' THEN 6
                ELSE 0
            END
        """)

        stages = {}
        for record in result:
            stages[record['stage']] = {
                'count': record['count'],
                'companies': [
                    {
                        'id': v['id'],
                        'name': v['name'],
                        'score': int(v['score']),
                        'industry': v['industry']
                    }
                    for v in record['ventures']
                ]
            }

        return stages

def get_dashboard_summary():
    """Get dashboard summary stats"""
    with driver.session() as session:
        result = session.run("""
            MATCH (v:Venture)
            WITH COUNT(v) as total_ventures, AVG(COALESCE(v.research_score, 75)) as avg_score
            OPTIONAL MATCH (v:Venture {stage: 'qualified'})
            WITH total_ventures, avg_score, COUNT(v) as qualified_ventures
            OPTIONAL MATCH (v2:Venture {stage: 'contacted'})
            RETURN
                total_ventures,
                COUNT(DISTINCT v2) as active_deals,
                avg_score,
                qualified_ventures
        """)

        record = result.single()
        total = record['total_ventures'] or 0
        active = record['active_deals'] or 0
        avg = round(record['avg_score'] or 75, 1)

        return {
            'total_companies': total,
            'total_deals': total,
            'avg_score': avg,
            'active_deals': active,
            'pipeline_value': active * 350000  # Estimate $350K per active deal
        }

class DealFlowAPIHandler(BaseHTTPRequestHandler):
    """HTTP request handler for DealFlowOS API"""

    def do_GET(self):
        """Handle GET requests"""
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == '/api/companies':
                # Get all companies
                limit = int(query.get('limit', [150])[0])
                companies = get_companies(limit)
                self.send_json(200, {'success': True, 'data': companies, 'count': len(companies)})

            elif path.startswith('/api/companies/'):
                # Get company details
                company_id = path.split('/')[-1]
                company = get_company_details(company_id)
                if company:
                    self.send_json(200, {'success': True, 'data': company})
                else:
                    self.send_json(404, {'success': False, 'error': 'Company not found'})

            elif path == '/api/pipeline/by-stage':
                # Get pipeline grouped by stage
                pipeline = get_pipeline_by_stage()
                self.send_json(200, {'success': True, 'data': pipeline})

            elif path == '/api/dashboard/summary':
                # Get dashboard summary
                summary = get_dashboard_summary()
                self.send_json(200, {'success': True, 'data': summary})

            elif path == '/health':
                self.send_json(200, {'status': 'healthy', 'service': 'dealflow-neo4j-api'})

            else:
                self.send_json(404, {'success': False, 'error': 'Not found'})

        except Exception as e:
            self.send_json(500, {'success': False, 'error': str(e)})

    def send_json(self, status, data):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        """Suppress logging"""
        pass

def run_server(port=8081):
    """Start the API server"""
    server = HTTPServer(('localhost', port), DealFlowAPIHandler)
    print(f'DealFlowOS Neo4j API Server running on http://localhost:{port}')
    print(f'Endpoints:')
    print(f'  GET /api/companies — All companies')
    print(f'  GET /api/companies/:id — Company details')
    print(f'  GET /api/pipeline/by-stage — Pipeline by stage')
    print(f'  GET /api/dashboard/summary — Dashboard summary')
    print(f'  GET /health — Health check')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        driver.close()
        server.shutdown()

if __name__ == '__main__':
    run_server()
