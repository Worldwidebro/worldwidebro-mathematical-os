import os
from supabase import create_client

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

def main():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Try inserting a minimal object to see if it succeeds or triggers an error showing the schema
    try:
        res = supabase.table("staffing_prospects").insert({"company": "Test Comp"}).execute()
        print("Success! Inserted dummy:", res.data)
        # Clean up
        supabase.table("staffing_prospects").delete().eq("company", "Test Comp").execute()
    except Exception as e:
        print("Insert failed with error:", e)

if __name__ == "__main__":
    main()
