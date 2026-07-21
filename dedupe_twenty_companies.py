#!/usr/bin/env python3
"""
dedupe_twenty_companies.py
Deduplicates company records in the Twenty CRM database by name.
Identifies duplicates, preserves the richest record, and soft-deletes the rest.
"""
import os
import sys
import argparse
import psycopg2

POSTGRES_URL = os.environ.get("PG_URL", "postgresql://twenty:twenty@localhost:5433/twenty")

def get_connection():
    try:
        conn = psycopg2.connect(POSTGRES_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def find_duplicates(cur, schema):
    query = f"""
    SELECT name, COUNT(*) 
    FROM "{schema}"."company"
    WHERE "deletedAt" IS NULL OR "deletedAt" IS NULL -- depending on twenty version
    GROUP BY name
    HAVING COUNT(*) > 1;
    """
    # Let's adjust table name if it has double quotes or is pluralized
    # First, let's detect if "company" table exists in this schema
    cur.execute(f"""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_schema = '{schema}' 
        AND table_name = 'company'
    );
    """)
    if not cur.fetchone()[0]:
        # Try plural 'companies'
        cur.execute(f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = '{schema}' 
            AND table_name = 'companies'
        );
        """)
        if not cur.fetchone()[0]:
            print(f"Error: Neither 'company' nor 'companies' table found in schema '{schema}'")
            return None
        table_name = "companies"
    else:
        table_name = "company"
        
    # Standard column checks
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = '{schema}' AND table_name = '{table_name}';")
    columns = [r[0] for r in cur.fetchall()]
    
    deleted_col = "deletedAt" if "deletedAt" in columns else ("deleted_at" if "deleted_at" in columns else None)
    
    where_clause = ""
    if deleted_col:
        where_clause = f'WHERE "{deleted_col}" IS NULL'
        
    query = f"""
    SELECT name, COUNT(*) 
    FROM "{schema}"."{table_name}"
    {where_clause}
    GROUP BY name
    HAVING COUNT(*) > 1;
    """
    
    cur.execute(query)
    duplicates = cur.fetchall()
    return duplicates, table_name, columns, deleted_col

def deduplicate_schema(conn, schema, dry_run=True):
    cur = conn.cursor()
    res = find_duplicates(cur, schema)
    if not res:
        cur.close()
        return
        
    duplicates, table_name, columns, deleted_col = res
    print(f"\n📂 Deduplicating table '{schema}.{table_name}'...")
    print(f"Found {len(duplicates)} duplicate names.")
    
    total_removed = 0
    
    for name, count in duplicates:
        if not name:
            continue
            
        # Fetch all records with this name
        where_clause = f'name = %s'
        if deleted_col:
            where_clause += f' AND "{deleted_col}" IS NULL'
            
        cur.execute(f"""
        SELECT id, {", ".join([f'"{c}"' for c in columns if c != "id"])}
        FROM "{schema}"."{table_name}"
        WHERE {where_clause}
        """, (name,))
        
        records = cur.fetchall()
        # Parse records to find the one with the most non-null columns
        # records is a list of tuples. We count non-null elements in each tuple
        best_record_idx = 0
        max_non_nulls = -1
        
        for idx, rec in enumerate(records):
            non_null_count = sum(1 for val in rec if val is not None and val != "")
            if non_null_count > max_non_nulls:
                max_non_nulls = non_null_count
                best_record_idx = idx
                
        best_id = records[best_record_idx][0]
        duplicate_ids = [rec[0] for idx, rec in enumerate(records) if idx != best_record_idx]
        
        print(f"🏢 Company: '{name}' | Keeping ID: {best_id} (non-nulls: {max_non_nulls}) | Removing duplicates: {duplicate_ids}")
        
        for dup_id in duplicate_ids:
            if not dry_run:
                if deleted_col:
                    # Soft delete
                    cur.execute(f"""
                    UPDATE "{schema}"."{table_name}"
                    SET "{deleted_col}" = NOW()
                    WHERE id = %s;
                    """, (dup_id,))
                else:
                    # Hard delete
                    cur.execute(f"""
                    DELETE FROM "{schema}"."{table_name}"
                    WHERE id = %s;
                    """, (dup_id,))
            total_removed += 1
            
    if not dry_run and total_removed > 0:
        conn.commit()
        print(f"✅ Successfully committed deduplication changes. Removed {total_removed} records.")
    else:
        print(f"[DRY RUN] Would remove {total_removed} duplicate records.")
        
    cur.close()

def main():
    parser = argparse.ArgumentParser(description="Deduplicate Twenty CRM Company Table")
    parser.add_argument("--execute", action="store_true", help="Execute the deletion (runs dry-run by default)")
    args = parser.parse_args()
    
    dry_run = not args.execute
    if dry_run:
        print("🔍 DRY RUN MODE (use --execute to commit changes)\n")
        
    conn = get_connection()
    cur = conn.cursor()
    
    # Query schemas
    cur.execute("SELECT schema_name FROM information_schema.schemata;")
    schemas = [r[0] for r in cur.fetchall()]
    cur.close()
    
    # Deduplicate core and public schemas
    for schema in ['public', 'core']:
        if schema in schemas:
            try:
                deduplicate_schema(conn, schema, dry_run)
            except Exception as e:
                print(f"Error processing schema '{schema}': {e}")
                conn.rollback()
                
    conn.close()

if __name__ == "__main__":
    main()
