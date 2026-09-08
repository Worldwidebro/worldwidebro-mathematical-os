#!/usr/bin/env python3
"""
DealFlowOS PostgreSQL Persistence API

REST API for DealFlowOS deal storage and analytics.
- Persistent deal storage with PostgreSQL
- Deal lifecycle tracking (deals table)
- Deal notes and collaboration (deal_notes table)
- Agent execution tracking (agent_runs table)

Authority: DealFlowOS Engine
Database: PostgreSQL localhost:5433
"""

import os
import json
import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import traceback
import hashlib
from pathlib import Path

# PostgreSQL connection parameters
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5433')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'admin')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'changeme')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'company_brain')

def get_db_connection():
    """Establish PostgreSQL connection"""
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            database=POSTGRES_DB
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def init_schema():
    """Initialize PostgreSQL schema for DealFlowOS"""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to PostgreSQL")
        return False

    cursor = conn.cursor()
    try:
        # Create deals table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deals (
                id SERIAL PRIMARY KEY,
                company_id VARCHAR(100) UNIQUE NOT NULL,
                company_name VARCHAR(255) NOT NULL,
                stage VARCHAR(50) NOT NULL DEFAULT 'discovered',
                value DECIMAL(15, 2),
                structure_type VARCHAR(100),
                industry VARCHAR(100),
                location VARCHAR(255),
                contact_email VARCHAR(255),
                contact_phone VARCHAR(20),
                notes TEXT,
                score DECIMAL(5, 2) DEFAULT 75,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_by VARCHAR(100),
                source VARCHAR(100)
            );
        """)

        # Create deal_notes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deal_notes (
                id SERIAL PRIMARY KEY,
                deal_id INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
                content TEXT NOT NULL,
                note_type VARCHAR(50) DEFAULT 'general',
                created_by VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_pinned BOOLEAN DEFAULT FALSE
            );
        """)

        # Create agent_runs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agent_runs (
                id SERIAL PRIMARY KEY,
                deal_id INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
                agent_type VARCHAR(100) NOT NULL,
                agent_name VARCHAR(255),
                status VARCHAR(50) NOT NULL DEFAULT 'pending',
                input_data JSONB,
                results_json JSONB,
                error_message TEXT,
                execution_time_ms INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                started_at TIMESTAMP,
                completed_at TIMESTAMP
            );
        """)

        # Create deal_files table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deal_files (
                id SERIAL PRIMARY KEY,
                deal_id INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
                file_name VARCHAR(255) NOT NULL,
                file_path TEXT NOT NULL,
                file_size INTEGER,
                file_hash VARCHAR(64),
                version INTEGER DEFAULT 1,
                mime_type VARCHAR(100),
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                uploader VARCHAR(100),
                description TEXT
            );
        """)

        # Create cap_tables table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cap_tables (
                id SERIAL PRIMARY KEY,
                venture_id VARCHAR(50) UNIQUE NOT NULL,
                venture_name VARCHAR(255),
                cap_table_data JSONB,
                total_capitalization DECIMAL(15, 2),
                founder_pct DECIMAL(5, 2),
                employee_pool_pct DECIMAL(5, 2),
                investor_pct DECIMAL(5, 2),
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                source_file TEXT
            );
        """)

        # Create indexes for performance
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_deals_stage ON deals(stage);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_deals_created_at ON deals(created_at);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_deal_notes_deal_id ON deal_notes(deal_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_agent_runs_deal_id ON agent_runs(deal_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_deal_files_deal_id ON deal_files(deal_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_cap_tables_venture_id ON cap_tables(venture_id);
        """)

        conn.commit()
        print("✓ PostgreSQL schema initialized successfully")
        return True
    except psycopg2.Error as e:
        print(f"Schema initialization error: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# ============ DEAL OPERATIONS ============

def create_deal(company_id, company_name, stage='discovered', value=None, structure_type=None,
                industry=None, location=None, created_by=None, source=None):
    """Create a new deal in PostgreSQL"""
    conn = get_db_connection()
    if not conn:
        return {'success': False, 'error': 'Database connection failed'}

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO deals (company_id, company_name, stage, value, structure_type,
                              industry, location, created_by, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, created_at;
        """, (company_id, company_name, stage, value, structure_type, industry, location, created_by, source))

        result = cursor.fetchone()
        deal_id, created_at = result
        conn.commit()

        return {
            'success': True,
            'deal_id': deal_id,
            'company_id': company_id,
            'company_name': company_name,
            'created_at': created_at.isoformat()
        }
    except psycopg2.IntegrityError:
        conn.rollback()
        return {'success': False, 'error': 'Company already exists as a deal'}
    except psycopg2.Error as e:
        conn.rollback()
        return {'success': False, 'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def get_deal(deal_id):
    """Fetch a single deal by ID"""
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, company_id, company_name, stage, value, structure_type,
                   industry, location, contact_email, contact_phone, notes, score,
                   created_at, updated_at, created_by, source
            FROM deals
            WHERE id = %s;
        """, (deal_id,))

        row = cursor.fetchone()
        if not row:
            return None

        return {
            'id': row[0],
            'company_id': row[1],
            'company_name': row[2],
            'stage': row[3],
            'value': float(row[4]) if row[4] else None,
            'structure_type': row[5],
            'industry': row[6],
            'location': row[7],
            'contact_email': row[8],
            'contact_phone': row[9],
            'notes': row[10],
            'score': float(row[11]) if row[11] else 75,
            'created_at': row[12].isoformat(),
            'updated_at': row[13].isoformat(),
            'created_by': row[14],
            'source': row[15]
        }
    finally:
        cursor.close()
        conn.close()

def update_deal(deal_id, **kwargs):
    """Update deal fields"""
    conn = get_db_connection()
    if not conn:
        return {'success': False, 'error': 'Database connection failed'}

    allowed_fields = ['stage', 'value', 'structure_type', 'industry', 'location',
                      'contact_email', 'contact_phone', 'notes', 'score']

    # Filter to only allowed fields
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
    if not updates:
        return {'success': False, 'error': 'No valid fields to update'}

    # Build dynamic SQL
    set_clause = ', '.join([f"{k} = %s" for k in updates.keys()])
    values = list(updates.values()) + [deal_id]

    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            UPDATE deals
            SET {set_clause}, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, updated_at;
        """, values)

        result = cursor.fetchone()
        if not result:
            return {'success': False, 'error': 'Deal not found'}

        conn.commit()
        return {
            'success': True,
            'deal_id': result[0],
            'updated_at': result[1].isoformat(),
            'fields_updated': list(updates.keys())
        }
    except psycopg2.Error as e:
        conn.rollback()
        return {'success': False, 'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def get_all_deals(limit=100, offset=0, stage=None):
    """Get all deals with optional filtering"""
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        if stage:
            cursor.execute("""
                SELECT id, company_id, company_name, stage, value, score, created_at
                FROM deals
                WHERE stage = %s
                ORDER BY created_at DESC
                LIMIT %s OFFSET %s;
            """, (stage, limit, offset))
        else:
            cursor.execute("""
                SELECT id, company_id, company_name, stage, value, score, created_at
                FROM deals
                ORDER BY created_at DESC
                LIMIT %s OFFSET %s;
            """, (limit, offset))

        deals = []
        for row in cursor.fetchall():
            deals.append({
                'id': row[0],
                'company_id': row[1],
                'company_name': row[2],
                'stage': row[3],
                'value': float(row[4]) if row[4] else None,
                'score': float(row[5]) if row[5] else 75,
                'created_at': row[6].isoformat()
            })
        return deals
    finally:
        cursor.close()
        conn.close()

# ============ DEAL NOTES OPERATIONS ============

def add_deal_note(deal_id, content, note_type='general', created_by=None):
    """Add a note to a deal"""
    conn = get_db_connection()
    if not conn:
        return {'success': False, 'error': 'Database connection failed'}

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO deal_notes (deal_id, content, note_type, created_by)
            VALUES (%s, %s, %s, %s)
            RETURNING id, created_at;
        """, (deal_id, content, note_type, created_by))

        result = cursor.fetchone()
        note_id, created_at = result
        conn.commit()

        return {
            'success': True,
            'note_id': note_id,
            'deal_id': deal_id,
            'created_at': created_at.isoformat()
        }
    except psycopg2.Error as e:
        conn.rollback()
        return {'success': False, 'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def get_deal_notes(deal_id):
    """Get all notes for a deal"""
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, content, note_type, created_by, created_at, is_pinned
            FROM deal_notes
            WHERE deal_id = %s
            ORDER BY created_at DESC;
        """, (deal_id,))

        notes = []
        for row in cursor.fetchall():
            notes.append({
                'id': row[0],
                'content': row[1],
                'note_type': row[2],
                'created_by': row[3],
                'created_at': row[4].isoformat(),
                'is_pinned': row[5]
            })
        return notes
    finally:
        cursor.close()
        conn.close()

# ============ AGENT RUN OPERATIONS ============

def log_agent_run(deal_id, agent_type, agent_name=None, status='pending',
                  input_data=None, results_json=None):
    """Log an agent run for a deal"""
    conn = get_db_connection()
    if not conn:
        return {'success': False, 'error': 'Database connection failed'}

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO agent_runs (deal_id, agent_type, agent_name, status, input_data, results_json)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, created_at;
        """, (deal_id, agent_type, agent_name, status,
              json.dumps(input_data) if input_data else None,
              json.dumps(results_json) if results_json else None))

        result = cursor.fetchone()
        run_id, created_at = result
        conn.commit()

        return {
            'success': True,
            'run_id': run_id,
            'deal_id': deal_id,
            'created_at': created_at.isoformat()
        }
    except psycopg2.Error as e:
        conn.rollback()
        return {'success': False, 'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def get_agent_runs(deal_id):
    """Get all agent runs for a deal"""
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, agent_type, agent_name, status, started_at, completed_at, execution_time_ms, error_message
            FROM agent_runs
            WHERE deal_id = %s
            ORDER BY created_at DESC;
        """, (deal_id,))

        runs = []
        for row in cursor.fetchall():
            runs.append({
                'id': row[0],
                'agent_type': row[1],
                'agent_name': row[2],
                'status': row[3],
                'started_at': row[4].isoformat() if row[4] else None,
                'completed_at': row[5].isoformat() if row[5] else None,
                'execution_time_ms': row[6],
                'error_message': row[7]
            })
        return runs
    finally:
        cursor.close()
        conn.close()

# ============ DEAL FILE OPERATIONS ============

def add_deal_file(deal_id, file_name, file_path, file_size=None, mime_type=None, uploader=None, description=None):
    """Add a file to a deal"""
    conn = get_db_connection()
    if not conn:
        return {'success': False, 'error': 'Database connection failed'}

    # Calculate file hash
    file_hash = None
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO deal_files (deal_id, file_name, file_path, file_size, file_hash, mime_type, uploader, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, upload_date, version;
        """, (deal_id, file_name, file_path, file_size, file_hash, mime_type, uploader, description))

        result = cursor.fetchone()
        file_id, upload_date, version = result
        conn.commit()

        return {
            'success': True,
            'file_id': file_id,
            'deal_id': deal_id,
            'file_name': file_name,
            'version': version,
            'file_hash': file_hash,
            'upload_date': upload_date.isoformat()
        }
    except psycopg2.Error as e:
        conn.rollback()
        return {'success': False, 'error': str(e)}
    finally:
        cursor.close()
        conn.close()

def get_deal_files(deal_id):
    """Get all files for a deal"""
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, file_name, file_path, file_size, file_hash, version, mime_type, upload_date, uploader, description
            FROM deal_files
            WHERE deal_id = %s
            ORDER BY upload_date DESC;
        """, (deal_id,))

        files = []
        for row in cursor.fetchall():
            files.append({
                'id': row[0],
                'file_name': row[1],
                'file_path': row[2],
                'file_size': row[3],
                'file_hash': row[4],
                'version': row[5],
                'mime_type': row[6],
                'upload_date': row[7].isoformat(),
                'uploader': row[8],
                'description': row[9]
            })
        return files
    finally:
        cursor.close()
        conn.close()

# ============ CAP TABLE OPERATIONS ============

def load_cap_table_from_file(venture_id, venture_name, file_path):
    """Load cap table data from JSON file"""
    try:
        if not os.path.exists(file_path):
            return {'success': False, 'error': f'File not found: {file_path}'}

        with open(file_path, 'r') as f:
            cap_table_data = json.load(f)

        conn = get_db_connection()
        if not conn:
            return {'success': False, 'error': 'Database connection failed'}

        cursor = conn.cursor()

        # Parse cap table to extract percentages
        founder_pct = None
        employee_pool_pct = None
        investor_pct = None
        total_cap = None

        if 'cap_table' in cap_table_data:
            for row in cap_table_data['cap_table']:
                entity_name = row[0].lower()
                pct_str = row[4].strip('%')
                pct = float(pct_str)

                if 'founder' in entity_name or 'managing' in entity_name:
                    founder_pct = pct
                elif 'employee' in entity_name or 'incentive' in entity_name:
                    employee_pool_pct = pct
                elif 'investor' in entity_name or 'institutional' in entity_name or 'preferred' in entity_name:
                    investor_pct = pct
                elif 'total' in entity_name:
                    # Extract valuation from total capitalization row
                    if len(row) > 5:
                        valuation_str = row[5].strip('$').replace(',', '')
                        try:
                            total_cap = float(valuation_str)
                        except ValueError:
                            pass

        try:
            cursor.execute("""
                INSERT INTO cap_tables (venture_id, venture_name, cap_table_data, founder_pct, employee_pool_pct, investor_pct, total_capitalization, source_file)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (venture_id) DO UPDATE SET
                    cap_table_data = EXCLUDED.cap_table_data,
                    founder_pct = EXCLUDED.founder_pct,
                    employee_pool_pct = EXCLUDED.employee_pool_pct,
                    investor_pct = EXCLUDED.investor_pct,
                    total_capitalization = EXCLUDED.total_capitalization,
                    source_file = EXCLUDED.source_file,
                    last_updated = CURRENT_TIMESTAMP
                RETURNING id, venture_id;
            """, (venture_id, venture_name, json.dumps(cap_table_data), founder_pct, employee_pool_pct, investor_pct, total_cap, file_path))

            result = cursor.fetchone()
            conn.commit()

            return {
                'success': True,
                'venture_id': venture_id,
                'venture_name': venture_name,
                'founder_pct': founder_pct,
                'employee_pool_pct': employee_pool_pct,
                'investor_pct': investor_pct,
                'total_capitalization': total_cap
            }
        except psycopg2.Error as e:
            conn.rollback()
            return {'success': False, 'error': str(e)}
        finally:
            cursor.close()
            conn.close()

    except json.JSONDecodeError as e:
        return {'success': False, 'error': f'Invalid JSON in file: {str(e)}'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def get_cap_table(venture_id):
    """Get cap table for a venture"""
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, venture_id, venture_name, cap_table_data, founder_pct, employee_pool_pct, investor_pct, total_capitalization, last_updated
            FROM cap_tables
            WHERE venture_id = %s;
        """, (venture_id,))

        row = cursor.fetchone()
        if not row:
            return None

        return {
            'id': row[0],
            'venture_id': row[1],
            'venture_name': row[2],
            'cap_table_data': row[3],
            'founder_pct': float(row[4]) if row[4] else None,
            'employee_pool_pct': float(row[5]) if row[5] else None,
            'investor_pct': float(row[6]) if row[6] else None,
            'total_capitalization': float(row[7]) if row[7] else None,
            'last_updated': row[8].isoformat()
        }
    finally:
        cursor.close()
        conn.close()

def get_all_cap_tables():
    """Get all cap tables"""
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT venture_id, venture_name, cap_table_data, founder_pct, employee_pool_pct, investor_pct, total_capitalization
            FROM cap_tables
            ORDER BY venture_id;
        """)

        cap_tables = []
        for row in cursor.fetchall():
            cap_tables.append({
                'venture_id': row[0],
                'venture_name': row[1],
                'cap_table_data': row[2],
                'founder_pct': float(row[3]) if row[3] else None,
                'employee_pool_pct': float(row[4]) if row[4] else None,
                'investor_pct': float(row[5]) if row[5] else None,
                'total_capitalization': float(row[6]) if row[6] else None
            })
        return cap_tables
    finally:
        cursor.close()
        conn.close()

# ============ PORTFOLIO OPERATIONS ============

def get_portfolio_summary():
    """Get consolidated portfolio summary across all ventures"""
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    try:
        # Get total deals by stage
        cursor.execute("""
            SELECT stage, COUNT(*) as count, SUM(value) as total_value
            FROM deals
            GROUP BY stage
            ORDER BY stage;
        """)

        deals_by_stage = {}
        total_pipeline = 0
        for row in cursor.fetchall():
            stage = row[0]
            count = row[1]
            value = float(row[2]) if row[2] else 0
            deals_by_stage[stage] = {'count': count, 'value': value}
            total_pipeline += value

        # Get total deals and ventures
        cursor.execute("SELECT COUNT(*) FROM deals;")
        total_deals = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT company_id) FROM deals;")
        total_ventures = cursor.fetchone()[0]

        # Get average deal value
        cursor.execute("SELECT AVG(value) FROM deals WHERE value IS NOT NULL;")
        avg_deal_value = float(cursor.fetchone()[0]) if cursor.fetchone()[0] else 0

        return {
            'total_deals': total_deals,
            'total_ventures': total_ventures,
            'total_pipeline': total_pipeline,
            'avg_deal_value': avg_deal_value,
            'deals_by_stage': deals_by_stage
        }
    finally:
        cursor.close()
        conn.close()

# ============ HTTP REQUEST HANDLER ============

class DealFlowAPIHandler(BaseHTTPRequestHandler):
    """HTTP request handler for DealFlowOS PostgreSQL API"""

    def do_GET(self):
        """Handle GET requests"""
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == '/health':
                conn = get_db_connection()
                if conn:
                    conn.close()
                    self.send_json(200, {'status': 'healthy', 'service': 'dealflow-postgres-api'})
                else:
                    self.send_json(500, {'status': 'unhealthy', 'error': 'Database connection failed'})

            elif path == '/api/deals':
                # Get all deals
                limit = int(query.get('limit', [100])[0])
                offset = int(query.get('offset', [0])[0])
                stage = query.get('stage', [None])[0]
                deals = get_all_deals(limit=limit, offset=offset, stage=stage)
                self.send_json(200, {'success': True, 'data': deals, 'count': len(deals)})

            elif path.startswith('/api/cap-tables/'):
                venture_id = path.split('/')[-1]
                # Get cap table for venture
                cap_table = get_cap_table(venture_id)
                if cap_table:
                    self.send_json(200, {'success': True, 'data': cap_table})
                else:
                    self.send_json(404, {'success': False, 'error': 'Cap table not found'})

            elif path == '/api/cap-tables':
                # Get all cap tables
                cap_tables = get_all_cap_tables()
                self.send_json(200, {'success': True, 'data': cap_tables, 'count': len(cap_tables)})

            elif path == '/api/ventures/portfolio':
                # Get portfolio summary
                portfolio = get_portfolio_summary()
                if portfolio:
                    self.send_json(200, {'success': True, 'data': portfolio})
                else:
                    self.send_json(500, {'success': False, 'error': 'Failed to fetch portfolio summary'})

            elif path.startswith('/api/deals/'):
                parts = path.split('/')
                try:
                    deal_id = int(parts[-2]) if parts[-2].isdigit() else int(parts[-1])

                    # Get deal details
                    if path.endswith(f'/{deal_id}'):
                        deal = get_deal(deal_id)
                        if deal:
                            # Fetch associated notes, agent runs, and files
                            deal['notes_list'] = get_deal_notes(deal_id)
                            deal['agent_runs'] = get_agent_runs(deal_id)
                            deal['files'] = get_deal_files(deal_id)
                            self.send_json(200, {'success': True, 'data': deal})
                        else:
                            self.send_json(404, {'success': False, 'error': 'Deal not found'})

                    # Get deal notes
                    elif path.endswith(f'/{deal_id}/notes'):
                        notes = get_deal_notes(deal_id)
                        self.send_json(200, {'success': True, 'data': notes, 'count': len(notes)})

                    # Get agent runs
                    elif path.endswith(f'/{deal_id}/agent-runs'):
                        runs = get_agent_runs(deal_id)
                        self.send_json(200, {'success': True, 'data': runs, 'count': len(runs)})

                    # Get deal files
                    elif path.endswith(f'/{deal_id}/files'):
                        files = get_deal_files(deal_id)
                        self.send_json(200, {'success': True, 'data': files, 'count': len(files)})

                    else:
                        self.send_json(404, {'success': False, 'error': 'Endpoint not found'})
                except (ValueError, IndexError):
                    self.send_json(400, {'success': False, 'error': 'Invalid deal ID'})

            else:
                self.send_json(404, {'success': False, 'error': 'Not found'})

        except Exception as e:
            print(f"GET error: {traceback.format_exc()}")
            self.send_json(500, {'success': False, 'error': str(e)})

    def do_POST(self):
        """Handle POST requests"""
        parsed = urlparse(self.path)
        path = parsed.path

        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_json(400, {'success': False, 'error': 'Invalid JSON'})
            return

        try:
            if path == '/api/deals':
                # Create new deal
                company_id = data.get('company_id') or f"DEAL-{datetime.now().timestamp()}"
                company_name = data.get('company_name') or data.get('name', 'Unnamed')
                stage = data.get('stage', 'discovered')
                value = data.get('value')
                structure_type = data.get('structure_type')
                industry = data.get('industry')
                location = data.get('location')
                created_by = data.get('created_by')
                source = data.get('source', 'dealflow-os')

                result = create_deal(company_id, company_name, stage, value, structure_type,
                                   industry, location, created_by, source)
                status_code = 201 if result['success'] else 400
                self.send_json(status_code, result)

            elif path == '/api/cap-tables/init':
                # Initialize cap tables from BUSINESS-CAPITAL-DATA-ROOM
                ventures = ['CON-001', 'LT-005', 'LT-011', 'OPS-001', 'RE-001']
                base_path = '/Users/acebless/Documents/The Company/Company Brain/BUSINESS-CAPITAL-DATA-ROOM'
                results = []

                for venture_id in ventures:
                    cap_table_path = os.path.join(base_path, venture_id, '04_OWNERSHIP', 'CAP-TABLE.json')
                    if os.path.exists(cap_table_path):
                        result = load_cap_table_from_file(venture_id, venture_id, cap_table_path)
                        results.append(result)
                    else:
                        results.append({'venture_id': venture_id, 'success': False, 'error': 'File not found'})

                self.send_json(200, {'success': True, 'data': results})

            elif path.startswith('/api/deals/'):
                parts = path.split('/')
                try:
                    deal_id = int(parts[-2]) if parts[-2].isdigit() else int(parts[-1])

                    # Add note to deal
                    if path.endswith('/notes'):
                        content = data.get('content', '')
                        note_type = data.get('note_type', 'general')
                        created_by = data.get('created_by')

                        if not content:
                            self.send_json(400, {'success': False, 'error': 'Content is required'})
                            return

                        result = add_deal_note(deal_id, content, note_type, created_by)
                        status_code = 201 if result['success'] else 400
                        self.send_json(status_code, result)

                    # Log agent run
                    elif path.endswith('/agent-runs'):
                        agent_type = data.get('agent_type')
                        agent_name = data.get('agent_name')
                        status = data.get('status', 'pending')
                        input_data = data.get('input_data')
                        results_json = data.get('results_json')

                        if not agent_type:
                            self.send_json(400, {'success': False, 'error': 'agent_type is required'})
                            return

                        result = log_agent_run(deal_id, agent_type, agent_name, status,
                                             input_data, results_json)
                        status_code = 201 if result['success'] else 400
                        self.send_json(status_code, result)

                    # Add file to deal
                    elif path.endswith('/files'):
                        file_name = data.get('file_name')
                        file_path = data.get('file_path')
                        file_size = data.get('file_size')
                        mime_type = data.get('mime_type')
                        uploader = data.get('uploader')
                        description = data.get('description')

                        if not file_name or not file_path:
                            self.send_json(400, {'success': False, 'error': 'file_name and file_path are required'})
                            return

                        result = add_deal_file(deal_id, file_name, file_path, file_size, mime_type, uploader, description)
                        status_code = 201 if result['success'] else 400
                        self.send_json(status_code, result)

                    else:
                        self.send_json(404, {'success': False, 'error': 'Endpoint not found'})
                except (ValueError, IndexError):
                    self.send_json(400, {'success': False, 'error': 'Invalid deal ID'})

            else:
                self.send_json(404, {'success': False, 'error': 'Not found'})

        except Exception as e:
            print(f"POST error: {traceback.format_exc()}")
            self.send_json(500, {'success': False, 'error': str(e)})

    def do_PUT(self):
        """Handle PUT requests"""
        parsed = urlparse(self.path)
        path = parsed.path

        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_json(400, {'success': False, 'error': 'Invalid JSON'})
            return

        try:
            if path.startswith('/api/deals/'):
                deal_id = path.split('/')[-1]
                try:
                    deal_id = int(deal_id)
                    result = update_deal(deal_id, **data)
                    status_code = 200 if result['success'] else 400
                    self.send_json(status_code, result)
                except ValueError:
                    self.send_json(400, {'success': False, 'error': 'Invalid deal ID'})
            else:
                self.send_json(404, {'success': False, 'error': 'Not found'})

        except Exception as e:
            print(f"PUT error: {traceback.format_exc()}")
            self.send_json(500, {'success': False, 'error': str(e)})

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def send_json(self, status, data):
        """Send JSON response with CORS headers"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

def run_server(port=5432):
    """Start the API server"""
    # Initialize schema on startup
    init_schema()

    server = HTTPServer(('127.0.0.1', port), DealFlowAPIHandler)
    print(f'✓ DealFlowOS PostgreSQL API Server running on http://127.0.0.1:{port}')
    print(f'\nEndpoints:')
    print(f'  — DEAL OPERATIONS')
    print(f'  POST   /api/deals                 — Create new deal')
    print(f'  GET    /api/deals                 — List all deals')
    print(f'  GET    /api/deals/:id             — Get deal details')
    print(f'  PUT    /api/deals/:id             — Update deal')
    print(f'  POST   /api/deals/:id/notes       — Add deal note')
    print(f'  GET    /api/deals/:id/notes       — Get deal notes')
    print(f'  POST   /api/deals/:id/agent-runs  — Log agent run')
    print(f'  GET    /api/deals/:id/agent-runs  — Get agent runs')
    print(f'  POST   /api/deals/:id/files       — Add file to deal')
    print(f'  GET    /api/deals/:id/files       — Get deal files')
    print(f'  — CAP TABLE OPERATIONS')
    print(f'  POST   /api/cap-tables/init       — Initialize all cap tables from files')
    print(f'  GET    /api/cap-tables/:venture_id — Get cap table for venture')
    print(f'  GET    /api/cap-tables            — Get all cap tables')
    print(f'  — PORTFOLIO REPORTING')
    print(f'  GET    /api/ventures/portfolio    — Get portfolio summary')
    print(f'  GET    /health                    — Health check')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n✓ Shutting down gracefully...')
        server.shutdown()

if __name__ == '__main__':
    run_server()
