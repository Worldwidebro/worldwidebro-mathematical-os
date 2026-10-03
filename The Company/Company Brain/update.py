import re

# 1. Update SYSTEM_CONNECTIVITY_AUDIT.md
with open('SYSTEM_CONNECTIVITY_AUDIT.md', 'r') as f:
    audit = f.read()

audit = re.sub(
    r'(### Mac Studio \(Remote\)).*?(### OmniRoute)',
    r'\1\n```text\nHostname:        macstudio\nTailscale IP:    100.87.214.70\nLAN IP:          192.168.1.11\nConnection:      SSH (ssh macstudio)\nStatus:          ✅ ONLINE (Load: 6.04)\n\nStorage:\n- Internal SSD:  93% full (33 GB free)\n- LaCie Drive:   54% full (1.7 TB free)\n- T7 Shield:     60% full (758 GB free) [CURRENTLY MOUNTED HERE]\n\nDocker Services:\n- neo4j, qdrant, n8n, minio, redis: ✅ HEALTHY (Up 5 days)\n- omniroute: ❌ CRASH LOOPING (Restarting 7)\n```\n\n\2',
    audit, flags=re.DOTALL
)
with open('SYSTEM_CONNECTIVITY_AUDIT.md', 'w') as f:
    f.write(audit)

# 2. Update SYSTEM_CONNECTIVITY_WIRED.md
with open('SYSTEM_CONNECTIVITY_WIRED.md', 'r') as f:
    wired = f.read()

# Update the diagram
wired = re.sub(
    r'│  Docker Services:.*?│',
    r'│  Docker Services:                                            │\n│    ├─ Neo4j (7474) ─── 20,363 edges (Up 5 days)              │\n│    ├─ Qdrant (6333) ── 17,236 vectors (Up 5 days)            │\n│    ├─ n8n (5678) ───── Active (Up 45 hours)                  │\n│    └─ OmniRoute (3004) ─ ❌ CRASH LOOPING (Restarting)        │',
    wired, flags=re.DOTALL
)
# Update Mac Studio storage line
wired = re.sub(r'\*\*Mac Studio:\*\* 11 GB free \(95% full\)', r'**Mac Studio (Internal):** 33 GB free (93% full)\n- **LaCie:** 1.7 TB free\n- **T7 Shield:** 758 GB free (Currently mounted here)', wired)

with open('SYSTEM_CONNECTIVITY_WIRED.md', 'w') as f:
    f.write(wired)

# 3. Update WHERE_WE_ARE.md
with open('WHERE_WE_ARE.md', 'r') as f:
    where = f.read()

# Add to blockers
if "### Current Blockers" in where:
    where = where.replace("### Current Blockers", "### Current Blockers\n- 🚨 **OmniRoute Gateway Down**: The `omniroute` Docker container on the Mac Studio is currently in a crash loop (`Restarting (7)`). Needs immediate logs/triage.")
else:
    # Just append
    where += "\n\n## Current Blockers\n- 🚨 **OmniRoute Gateway Down**: The `omniroute` Docker container on the Mac Studio is currently in a crash loop (`Restarting (7)`). Needs immediate logs/triage."

with open('WHERE_WE_ARE.md', 'w') as f:
    f.write(where)

print("Updated audit, wired, and where_we_are.")
