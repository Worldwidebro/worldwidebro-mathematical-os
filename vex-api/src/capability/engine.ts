import { TaskMemoryStore } from '../memory/memory-store.js';
import { CapabilitiesRegistry, Capability } from './capabilities-registry.js';

/**
 * Phase 3 Capability Engine
 *
 * Task description → ranked list of (agent, capability, score)
 * PONYTAIL: Minimal scoring, sync text matching + semantic from taskMemoryStore
 */

export interface RankedCapability {
  agent: string;
  capability: string;
  score: number;
  source: 'text-match' | 'similar-task' | 'combined';
}

export class CapabilityEngine {
  private taskMemory: TaskMemoryStore;
  private registry: CapabilitiesRegistry;

  constructor(taskMemory: TaskMemoryStore, registry: CapabilitiesRegistry) {
    this.taskMemory = taskMemory;
    this.registry = registry;
  }

  /**
   * Main entry point: rank capabilities for a task description
   * Returns sorted list by descending score
   */
  async rankCapabilities(taskDescription: string): Promise<RankedCapability[]> {
    // Get all seed capabilities -> change to dynamic capabilities from Neo4j
    const capabilities = await this.registry.getDynamicCapabilities();

    // Score each capability via text match
    const textScores = new Map<string, number>();
    for (const cap of capabilities) {
      const score = this.scoreTextMatch(taskDescription, cap);
      textScores.set(cap.name, score);
    }

    // Find similar past tasks to extract historically-used capabilities
    const similarTasks = await this.taskMemory.findSimilarTasks({
      content: taskDescription,
      limit: 5,
    });

    // Build historical capability scores from similar tasks
    const historicalScores = new Map<string, { count: number; avgScore: number }>();
    for (const task of similarTasks) {
      const taskCaps = this._extractCapabilitiesFromTask(task);
      const weight = task.metadata?.similarity_score || 0.5;

      for (const cap of taskCaps) {
        const current = historicalScores.get(cap) || { count: 0, avgScore: 0 };
        current.count += 1;
        current.avgScore = (current.avgScore * (current.count - 1) + weight) / current.count;
        historicalScores.set(cap, current);
      }
    }

    // Combine scores: 70% text match + 30% historical usage
    const combinedScores: RankedCapability[] = [];
    for (const cap of capabilities) {
      const textScore = textScores.get(cap.name) || 0;
      const historical = historicalScores.get(cap.name);
      const historicalScore = historical ? historical.avgScore * 100 : 0;

      const combined = textScore * 0.7 + historicalScore * 0.3;
      combinedScores.push({
        agent: this._mapCapabilityToAgent(cap.name),
        capability: cap.name,
        score: Math.round(combined),
        source: historicalScore > 0 ? 'combined' : 'text-match',
      });
    }

    // Sort by score descending
    return combinedScores.sort((a, b) => b.score - a.score);
  }

  /**
   * Simple text matching: word overlap + keyword matching
   * Returns 0-100 score
   */
  private scoreTextMatch(taskDescription: string, capability: Capability): number {
    const taskWords = taskDescription.toLowerCase().split(/\s+/);
    const capName = capability.name.toLowerCase();
    const capDesc = capability.description.toLowerCase();

    // Word overlap with name and description
    let matches = 0;
    for (const word of taskWords) {
      if (
        capName.includes(word) ||
        capDesc.includes(word) ||
        capability.keywords.some(k => k.includes(word))
      ) {
        matches += 1;
      }
    }

    // Base score from word overlap
    let score = (matches / Math.max(taskWords.length, 1)) * 100;

    // Bonus if task words appear in capability name (higher relevance)
    for (const word of taskWords) {
      if (capName.includes(word)) {
        score += 15;
      }
    }

    // Bonus if capability keywords match task
    for (const kw of capability.keywords) {
      for (const taskWord of taskWords) {
        if (this._similarity(kw, taskWord) > 0.8) {
          score += 10;
        }
      }
    }

    return Math.min(score, 100);
  }

  /**
   * Tiny string similarity: 1 - (edit_distance / max_length)
   * ponytail: 2 lines for levenshtein
   */
  private _similarity(a: string, b: string): number {
    const s1 = a.toLowerCase();
    const s2 = b.toLowerCase();
    if (s1 === s2) return 1;

    // ponytail: ultra-minimal levenshtein
    const memo = new Map<string, number>();
    const lev = (i: number, j: number): number => {
      const key = `${i},${j}`;
      if (memo.has(key)) return memo.get(key)!;

      if (i === 0) return j;
      if (j === 0) return i;

      const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
      const result = Math.min(
        lev(i - 1, j) + 1,
        lev(i, j - 1) + 1,
        lev(i - 1, j - 1) + cost
      );

      memo.set(key, result);
      return result;
    };

    const distance = lev(s1.length, s2.length);
    return 1 - distance / Math.max(s1.length, s2.length);
  }

  /**
   * Extract capabilities from a stored task's metadata
   * Format: metadata.capabilities = ["venture-analysis", "market-research", ...]
   */
  private _extractCapabilitiesFromTask(task: any): string[] {
    const meta = task.metadata || {};
    if (Array.isArray(meta.capabilities)) {
      return meta.capabilities;
    }
    // Fallback: infer from agent_id if available
    if (meta.agent_id) {
      return [meta.agent_id]; // Simple: agent_id = capability
    }
    return [];
  }

  /**
   * Map capability name to agent type
   * Simple mapping for Phase 3
   * Phase 4: Use Neo4j Agent nodes
   */
  private _mapCapabilityToAgent(capabilityName: string): string {
    const mapping: Record<string, string> = {
      'venture-analysis': 'strategy-agent',
      'financial-modeling': 'finance-agent',
      'market-research': 'strategy-agent',
      'team-building': 'ops-agent',
      'process-optimization': 'ops-agent',
      'risk-assessment': 'strategy-agent',
      'sales': 'revenue-agent',
      'operations': 'ops-agent',
      'technology': 'tech-agent',
      'strategy': 'strategy-agent',
    };
    return mapping[capabilityName] || 'general-agent';
  }
}
