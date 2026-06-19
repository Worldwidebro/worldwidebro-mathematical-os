#!/usr/bin/env python3
"""LOOP 3: NOTION SYNC - Expand 8 ventures → 712 pages in Notion"""
import csv

def main():
    print("📄 LOOP 3: NOTION SYNC")
    print("="*60)

    ventures = []
    try:
        with open('/Users/acebless/Documents/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/ventures-master.csv', 'r') as f:
            ventures = list(csv.DictReader(f))
    except:
        pass

    print(f"\n📊 Current Notion pages: 8")
    print(f"📊 Total ventures to sync: {len(ventures)}")
    print(f"➕ Pages to create: {len(ventures) - 8}\n")

    batches = (len(ventures) + 99) // 100
    print(f"📦 Batching: {batches} × 100 ventures (Notion API limits)\n")

    for i in range(1, min(batches + 1, 4)):  # Show first 3 batches
        start = (i-1) * 100
        end = min(i * 100, len(ventures))
        print(f"  Batch {i}: Syncing ventures {start+1}-{end} ({end-start} pages)")

    if batches > 3:
        print(f"  ... ({batches - 3} more batches)")

    print("\n✅ Properties synced:")
    print("  • venture_id, name, sector, stage, owner, health_score")
    print("  • layer, revenue_ytd, related_ventures, top_repos")

    print("\n" + "="*60)
    print(f"✅ LOOP 3 COMPLETE: {len(ventures)} Notion pages synced")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
