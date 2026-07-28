import os
import sys
from supabase import create_client

SUPABASE_URL = "https://cyhzilqldouzgynacqpe.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5aHppbHFsZG91emd5bmFjcXBlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NDY2OTQwOCwiZXhwIjoyMDgwMjQ1NDA4fQ.1M6V3fR9rNxonIJvtNkV4isrZK9VIvy3J-gNLJGMp2k"

def main():
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Connected to Supabase successfully!")
        
        # Try fetching from staffing_prospects
        res = supabase.table("staffing_prospects").select("*").limit(5).execute()
        print("staffing_prospects data:")
        print(res.data)
        
    except Exception as e:
        print("Error connecting or querying:", e)

if __name__ == "__main__":
    main()
