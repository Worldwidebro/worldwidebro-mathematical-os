# System Simplification: Stripping Away Jargon for Direct Execution

This document simplifies the holdings OS into its core working components. 

---

## 1. Demystifying the Terms

The system seems complicated because it has been wrapped in heavy terms. In reality, it is very simple:

| Strategic Term | What It Actually Is | How It Works |
| :--- | :--- | :--- |
| **Registry** | A spreadsheet list of what we own. | `ventures.csv` is just a list of companies. `repos-index.json` is just a list of directories. |
| **Agent** | A Python script or n8n loop with a prompt. | Reads a lead from the database, runs an API request, and posts to Slack. |
| **Decision Level** | A simple `if/else` budget gate. | If the task costs < $5K, the script runs automatically. If not, it pings your phone. |
| **VEX UI** | A React dashboard showing this data. | A simple web page that displays the database tables and lets you click "Approve". |

---

## 2. Why It Stalls: The Active Connection Gap

You have the hardware, the code, and the storage. The only reason the system is inactive is because **the data loop is broken**:

```
 [ Cloned Repos & Blueprints ] ────(Broken Connection)────→ [ Unreachable Databases on Mac Studio ]
```

Because your MacBook Air cannot connect to the Postgres and Neo4j containers running on the Mac Studio (`100.87.214.70`), the python scripts cannot load your spreadsheets into the database. Since the database is empty, the VEX UI displays nothing.

---

## 3. The 3 Steps to Run the Whole System

To turn this heap of code and files into a working, wealth-generating engine, we only need to do three things:

### Step 1: Start the Databases on the Mac Studio
Since SSH is timed out, you must run this command directly in the terminal of your **Mac Studio** (or enable "Remote Login" in macOS Sharing Settings to open port 22):
```bash
# On the Mac Studio host
cd ~/Documents/
docker compose up -d
```
*Verify*: Ensure you can open `http://100.87.214.70:7474` (Neo4j UI) from your MacBook Air browser.

### Step 2: Seed the Data from your MacBook Air
Once the databases are online and accessible over Tailscale, run the seeder scripts from your MacBook Air:
```bash
# Seeds the company list into Postgres/Twenty
python3 scripts/populate_twenty_ventures.py

# Seeds the sectors and agent dependencies into Neo4j
python3 scripts/loop_4_knowledge_graph.py
```

### Step 3: Run the VEX Dashboard
Once the data is seeded, run the VEX frontend client:
```bash
cd ~/Documents/vex-hero-site/
npm run dev
```
Open `http://localhost:5173` to see your live ventures, active agents, and lead queues in one visual workspace.
