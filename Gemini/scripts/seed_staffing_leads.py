import csv
import os
from supabase import create_client

CSV_PATH = "/Users/acebless/Documents/.claude/worktrees/agent-ac65ac3629807bab2/WORLDWIDEBRO-OS/03-PORTFOLIO/opcos/STAFFING/go-to-market/charlotte-employer-targets.csv"
SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV file not found at {CSV_PATH}")
        return

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Read CSV and build rows
    rows_to_insert = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Map fields safely, providing fallbacks for empty values
            rows_to_insert.append({
                "company": row.get("company", "").strip(),
                "sector": row.get("sector", "").strip() or None,
                "phone": row.get("phone", "").strip() or None,
                "city_state": row.get("city_state", "").strip() or None,
                "website": row.get("website", "").strip() or None,
                "priority": row.get("priority", "MEDIUM").strip().upper(),
                "notes": row.get("notes", "").strip() or None,
                "status": row.get("status", "not_contacted").strip() or "not_contacted",
                "last_touch": row.get("last_touch", "").strip() or None,
                "source": "charlotte_seed_list"
            })

    print(f"Parsed {len(rows_to_insert)} rows from CSV. Inserting into Supabase...")
    
    # Insert in batches of 50 to avoid hitting API size limits
    batch_size = 50
    inserted_count = 0
    for i in range(0, len(rows_to_insert), batch_size):
        batch = rows_to_insert[i:i + batch_size]
        try:
            res = supabase.table("staffing_prospects").insert(batch).execute()
            inserted_count += len(res.data)
            print(f"Successfully inserted batch {i//batch_size + 1} ({len(res.data)} rows)")
        except Exception as e:
            print(f"Error inserting batch starting at {i}: {e}")

    print(f"Done! Seeded total of {inserted_count} prospects into Supabase.")

if __name__ == "__main__":
    main()
