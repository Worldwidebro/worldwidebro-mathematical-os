// SOLUTION FINDER ORCHESTRATOR
// Queries Neo4j + Qdrant + graft to find existing solutions
// 2026-09-19

import neo4j from 'neo4j-driver';
import { execSync } from 'child_process';

// Initialize Neo4j driver
const driver = neo4j.driver(
  'bolt://100.87.214.70:7687',
  neo4j.auth.basic('neo4j', 'changeme')
);

// Qdrant API client
const qdrantHost = 'http://100.87.214.70:6333';

/**
 * SOLUTION FINDER LOOP
 * Input: task description or problem name
 * Output: { found: boolean, solution: Solution | null, searchResults: SearchResult[] }
 */

export class SolutionFinder {

  constructor(options = {}) {
    this.neoDriver = driver;
    this.qdrantUrl = options.qdrantHost || qdrantHost;
    this.confidenceThreshold = options.threshold || 0.75;
  }

  /**
   * Main orchestrator: find solution using all available sources
   */
  async findSolution(query) {
    console.log(`[SolutionFinder] Searching for: "${query}"`);

    const startTime = Date.now();
    const results = {
      query,
      found: false,
      solution: null,
      searchResults: [],
      sources: { neo4j: null, qdrant: null, graft: null },
      elapsed: 0
    };

    try {
      // 1. Query Neo4j by problem name
      console.log('  [1/3] Querying Neo4j...');
      const neoResult = await this.queryNeo4j(query);
      results.sources.neo4j = neoResult;

      if (neoResult && neoResult.confidence > this.confidenceThreshold) {
        results.found = true;
        results.solution = neoResult;
        results.searchResults.push(neoResult);
        console.log(`  ✅ Found via Neo4j: ${neoResult.name} (confidence: ${neoResult.confidence})`);
      }

      // 2. Query Qdrant for semantic similarity
      console.log('  [2/3] Querying Qdrant (semantic search)...');
      const qdrantResults = await this.queryQdrant(query);
      results.sources.qdrant = qdrantResults;

      if (qdrantResults && qdrantResults.length > 0) {
        const topResult = qdrantResults[0];
        if (topResult.confidence > this.confidenceThreshold) {
          if (!results.found) {
            results.found = true;
            results.solution = topResult;
          }
          results.searchResults.push(...qdrantResults);
          console.log(`  ✅ Found via Qdrant: ${topResult.name} (confidence: ${topResult.confidence})`);
        }
      }

      // 3. Query graft (code search)
      console.log('  [3/3] Querying graft (code patterns)...');
      const graftResults = await this.queryGraft(query);
      results.sources.graft = graftResults;

      if (graftResults && graftResults.length > 0) {
        if (!results.found) {
          results.found = true;
          results.solution = graftResults[0];
        }
        results.searchResults.push(...graftResults);
        console.log(`  ✅ Found via graft: ${graftResults[0].name}`);
      }

      // Record discovery in Neo4j (for feedback loop)
      if (results.found) {
        await this.recordDiscovery(query, results.solution);
      }

    } catch (error) {
      console.error(`[SolutionFinder] Error:`, error.message);
      results.error = error.message;
    }

    results.elapsed = Date.now() - startTime;
    console.log(`  ⏱️ Completed in ${results.elapsed}ms`);

    return results;
  }

  /**
   * Query 1: Neo4j by exact problem name
   */
  async queryNeo4j(problemName) {
    const session = this.neoDriver.session();

    try {
      const result = await session.run(
        `MATCH (p:Problem {name: $name})<-[r:SOLVES]-(s:Solution)
         RETURN s.id as id, s.name as name, s.codePath as codePath,
                s.repo as repo, s.language as language, r.confidence as confidence
         ORDER BY r.confidence DESC LIMIT 1`,
        { name: problemName }
      );

      if (result.records.length === 0) return null;

      const record = result.records[0];
      return {
        id: record.get('id'),
        name: record.get('name'),
        codePath: record.get('codePath'),
        repo: record.get('repo'),
        language: record.get('language'),
        confidence: record.get('confidence') || 0.85,
        source: 'neo4j'
      };
    } finally {
      await session.close();
    }
  }

  /**
   * Query 2: Qdrant semantic search
   */
  async queryQdrant(query) {
    // In production, embed the query using Ollama or a remote API
    // For MVP: use keyword-based search

    try {
      const response = await fetch(`${this.qdrantUrl}/collections/solutions/points/search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          // Use mock embedding for MVP (replace with real embeddings)
          vector: this.mockEmbedding(query),
          limit: 5,
          score_threshold: this.confidenceThreshold
        })
      });

      if (!response.ok) {
        console.warn(`  ⚠️  Qdrant query failed (${response.status}). Continuing...`);
        return [];
      }

      const data = await response.json();
      return data.result.map(hit => ({
        id: hit.payload.solution_id,
        name: hit.payload.solution_name,
        codePath: hit.payload.code_path,
        repo: hit.payload.repo,
        language: hit.payload.language,
        confidence: hit.score,
        source: 'qdrant'
      }));
    } catch (error) {
      console.warn(`  ⚠️  Qdrant error: ${error.message}`);
      return [];
    }
  }

  /**
   * Query 3: graft code search
   */
  async queryGraft(query) {
    try {
      // Use grep as fallback to graft (graft CLI may not be available in all envs)
      const cmd = `cd /Users/acebless/Documents/The\\ Company/Company\\ Brain && grep -r "${query}" --include="*.ts" --include="*.js" --include="*.md" | head -5`;
      const output = execSync(cmd, { encoding: 'utf-8', stdio: ['pipe', 'pipe', 'ignore'] });

      const matches = output.split('\n').filter(line => line.length > 0);

      if (matches.length === 0) return [];

      // Parse grep results
      return matches.slice(0, 3).map((match, idx) => {
        const [file, content] = match.split(':').slice(0, 2);
        return {
          id: `GRAFT-${idx}`,
          name: `Pattern: ${query}`,
          codePath: file || 'unknown',
          language: file?.endsWith('.ts') ? 'TypeScript' : file?.endsWith('.js') ? 'JavaScript' : 'Markdown',
          confidence: 0.80 - (idx * 0.05), // Lower confidence for subsequent results
          source: 'graft'
        };
      });
    } catch (error) {
      console.warn(`  ⚠️  graft search failed: ${error.message}`);
      return [];
    }
  }

  /**
   * Record that a solution was discovered (feedback loop)
   */
  async recordDiscovery(query, solution) {
    const session = this.neoDriver.session();

    try {
      // Increment usage counter
      await session.run(
        `MATCH (s:Solution {id: $solutionId})
         SET s.usageCount = s.usageCount + 1,
             s.lastUsed = datetime()
         RETURN s.name`,
        { solutionId: solution.id }
      );

      console.log(`  📝 Recorded discovery of ${solution.name}`);
    } catch (error) {
      console.warn(`  ⚠️  Failed to record discovery: ${error.message}`);
    } finally {
      await session.close();
    }
  }

  /**
   * Mock embedding generator (replace with real Ollama call in production)
   */
  mockEmbedding(text) {
    // Returns a 384-dim vector (mock)
    const vec = new Array(384).fill(0);
    for (let i = 0; i < text.length && i < 384; i++) {
      vec[i] = (text.charCodeAt(i) % 256) / 256;
    }
    return vec;
  }

  /**
   * Register a new solution (called after executing new task)
   */
  async registerSolution(solution) {
    const session = this.neoDriver.session();

    try {
      await session.run(
        `MERGE (s:Solution {
           id: $id,
           name: $name,
           description: $description,
           codePath: $codePath,
           repo: $repo,
           language: $language,
           created: datetime(),
           confidence: 0.90,
           usageCount: 0
         })

         MERGE (p:Problem {name: $solvesProblem, domain: $domain})

         MERGE (s)-[r:SOLVES {confidence: 0.90}]->(p)

         RETURN s.id`,
        {
          id: solution.id,
          name: solution.name,
          description: solution.description,
          codePath: solution.codePath,
          repo: solution.repo,
          language: solution.language,
          solvesProblem: solution.solvesProblem,
          domain: solution.domain
        }
      );

      console.log(`✅ Registered new solution: ${solution.name}`);
    } finally {
      await session.close();
    }
  }

  /**
   * Shutdown driver
   */
  async close() {
    await this.neoDriver.close();
  }
}

// Export for MCP integration
export default SolutionFinder;
