#!/usr/bin/env python3
"""
Repo Discovery Engine
Agents query this to find best-fit repos for their gap
"""

from neo4j import GraphDatabase
import json

class RepoDiscoveryEngine:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://100.87.214.70:7687", auth=("neo4j", "changeme"))
    
    def find_repos_by_gap(self, gap_category: str, limit: int = 5):
        """Find top repos for a gap"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (g:Gap {category: $gap})<-[:SOLVES_GAP]-(r:Repository)
                RETURN r.name as name, r.url as url, r.description as description
                LIMIT $limit
            """, gap=gap_category, limit=limit)
            
            repos = []
            for record in result:
                repos.append({
                    "name": record["name"],
                    "url": record["url"],
                    "description": record["description"]
                })
            return repos
    
    def find_multi_gap_repos(self, gaps: list, limit: int = 3):
        """Find repos that solve multiple gaps (combo solutions)"""
        with self.driver.session() as session:
            gap_list = "', '".join(gaps)
            result = session.run(f"""
                MATCH (r:Repository)-[:SOLVES_GAP]->(g:Gap)
                WHERE g.category IN ['{gap_list}']
                WITH r, COUNT(DISTINCT g.category) as gap_count
                WHERE gap_count >= {len(gaps)}
                RETURN DISTINCT r.name as name, r.url as url
                LIMIT {limit}
            """)
            
            repos = []
            for record in result:
                repos.append({"name": record["name"], "url": record["url"]})
            return repos
    
    def get_gap_coverage(self):
        """Get all gap layers + repo counts"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (g:Gap)<-[:SOLVES_GAP]-(r:Repository)
                WITH g.category as gap_cat, g.name as gap_name, COUNT(DISTINCT r) as count
                RETURN gap_cat, gap_name, count
                ORDER BY count DESC
            """)
            
            gaps = {}
            for record in result:
                gaps[record["gap_cat"]] = {
                    "name": record["gap_name"],
                    "count": record["count"]
                }
            return gaps
    
    def close(self):
        self.driver.close()

# Test discovery
if __name__ == "__main__":
    engine = RepoDiscoveryEngine()
    
    print("🔍 REPO DISCOVERY ENGINE")
    print("=" * 60)
    print()
    
    # Show gap coverage
    gaps = engine.get_gap_coverage()
    print("Available Gaps:")
    for gap, info in sorted(gaps.items(), key=lambda x: -x[1]["count"]):
        print(f"  {info['name']:20} → {info['count']:3} repos")
    
    print()
    print("=" * 60)
    print()
    
    # Example discovery queries
    print("EXAMPLE QUERIES:")
    print()
    
    print("1. OPS-001: Find Loop Engineering repos")
    repos = engine.find_repos_by_gap("loop", limit=3)
    for i, repo in enumerate(repos, 1):
        print(f"   {i}. {repo['name']}")
    
    print()
    print("2. LT-005: Find Context Engineering repos")
    repos = engine.find_repos_by_gap("context", limit=3)
    for i, repo in enumerate(repos, 1):
        print(f"   {i}. {repo['name']}")
    
    print()
    print("3. CALLCENTER: Find Tool Engineering repos")
    repos = engine.find_repos_by_gap("tool", limit=3)
    for i, repo in enumerate(repos, 1):
        print(f"   {i}. {repo['name']}")
    
    print()
    print("✅ Discovery engine ready!")
    
    engine.close()
