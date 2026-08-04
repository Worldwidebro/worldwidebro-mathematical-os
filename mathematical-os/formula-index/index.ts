import { randomUUID } from 'crypto';

export type FormulaComplexity = 'simple' | 'moderate' | 'complex';
export type VariableType = 'number' | 'percent' | 'amount' | 'ratio' | 'count';

export interface Variable {
  name: string;
  type: VariableType;
  description: string;
  unit?: string;
}

export interface Formula {
  id: string;
  name: string;
  domain: string; // e.g., 'capital-allocation', 'roi-calculation', 'agent-scoring'
  complexity: FormulaComplexity;
  formula_string: string; // e.g., 'T1_Allocation = (Pool × 0.27) × (Realized_ROI / 0.15) × Velocity_Factor'
  variables: Variable[];
  return_type: VariableType;
  description: string;
  formula_version: string;
  created_at: Date;
  updated_at: Date;
  tags?: string[];
}

export interface FormulaRegistry {
  formulas: Map<string, Formula>;
  domains: Set<string>;
}

class FormulaIndexImpl {
  private registry: FormulaRegistry = {
    formulas: new Map(),
    domains: new Set(),
  };

  // Bootstrap with capital allocation formulas
  private initializeCapitalAllocationFormulas() {
    const formulas: Formula[] = [
      {
        id: 'tier-1-allocation',
        name: 'Tier 1 (Mature) Allocation',
        domain: 'capital-allocation',
        complexity: 'moderate',
        formula_string: '(Pool × 0.27) × (Realized_ROI / 0.15) × Velocity_Factor',
        variables: [
          { name: 'Pool', type: 'amount', description: 'Total capital pool' },
          { name: 'Realized_ROI', type: 'percent', description: 'Average ROI last 12 months' },
          { name: 'Velocity_Factor', type: 'ratio', description: 'Deployments / Target Deployments' },
        ],
        return_type: 'amount',
        description: 'Allocates 27% of pool to mature OPCOs, adjusted by ROI and deployment velocity',
        formula_version: '1.0',
        created_at: new Date('2026-07-28'),
        updated_at: new Date('2026-07-28'),
        tags: ['tier-1', 'mature', 'guardrails-1.5x-0.75x'],
      },
      {
        id: 'tier-2-allocation',
        name: 'Tier 2 (Growth) Allocation',
        domain: 'capital-allocation',
        complexity: 'moderate',
        formula_string: '(Pool × 0.21) × (Realized_ROI / 0.10) × min(Velocity_Factor, 1.2)',
        variables: [
          { name: 'Pool', type: 'amount', description: 'Total capital pool' },
          { name: 'Realized_ROI', type: 'percent', description: 'Average ROI last 12 months or forecast' },
          { name: 'Velocity_Factor', type: 'ratio', description: 'Deployments / Target Deployments' },
        ],
        return_type: 'amount',
        description: 'Allocates 21% of pool to growth-stage OPCOs, capped velocity at 1.2',
        formula_version: '1.0',
        created_at: new Date('2026-07-28'),
        updated_at: new Date('2026-07-28'),
        tags: ['tier-2', 'growth', 'guardrails-1.5x-0.6x'],
      },
      {
        id: 'tier-3-allocation',
        name: 'Tier 3 (Early) Allocation',
        domain: 'capital-allocation',
        complexity: 'moderate',
        formula_string: '(Pool × 0.18) × (1 + Growth_Rate_6mo) × min(Velocity_Factor, 1.0)',
        variables: [
          { name: 'Pool', type: 'amount', description: 'Total capital pool' },
          { name: 'Growth_Rate_6mo', type: 'ratio', description: '(Current ROI - Prior 6mo ROI) / Prior 6mo ROI' },
          { name: 'Velocity_Factor', type: 'ratio', description: 'Deployments / Target Deployments' },
        ],
        return_type: 'amount',
        description: 'Allocates 18% of pool to early-stage OPCOs, capped velocity at 1.0 (conservative)',
        formula_version: '1.0',
        created_at: new Date('2026-07-28'),
        updated_at: new Date('2026-07-28'),
        tags: ['tier-3', 'early-stage', 'guardrails-2.0x-0.4x'],
      },
      {
        id: 'predicted-roi',
        name: 'Predicted ROI Calculation',
        domain: 'capital-allocation',
        complexity: 'simple',
        formula_string:
          '(OPCO_ROI × 0.4) + (Sector_Benchmark × 0.3) + (Stage_Adjustment × 0.2) + (Market_Sentiment × 0.1)',
        variables: [
          { name: 'OPCO_ROI', type: 'percent', description: 'Historical OPCO ROI' },
          { name: 'Sector_Benchmark', type: 'percent', description: 'Sector average ROI' },
          { name: 'Stage_Adjustment', type: 'percent', description: 'Venture stage adjustment' },
          { name: 'Market_Sentiment', type: 'ratio', description: 'Market sentiment multiplier (e.g., 1.0 = neutral)' },
        ],
        return_type: 'percent',
        description: 'Weighted prediction of venture ROI before deployment',
        formula_version: '1.0',
        created_at: new Date('2026-07-28'),
        updated_at: new Date('2026-07-28'),
        tags: ['deployment', 'prediction', 'weighted'],
      },
      {
        id: 'actual-roi',
        name: 'Actual ROI Calculation',
        domain: 'capital-allocation',
        complexity: 'simple',
        formula_string: '((Exit_Value - Deployed_Amount) / Deployed_Amount) × 100',
        variables: [
          { name: 'Exit_Value', type: 'amount', description: 'Final venture valuation or exit price' },
          { name: 'Deployed_Amount', type: 'amount', description: 'Initial capital deployment' },
        ],
        return_type: 'percent',
        description: 'Realized ROI after venture exit or significant milestone',
        formula_version: '1.0',
        created_at: new Date('2026-07-28'),
        updated_at: new Date('2026-07-28'),
        tags: ['deployment', 'post-exit', 'accounting'],
      },
    ];

    formulas.forEach((formula) => {
      this.registry.formulas.set(formula.id, formula);
      this.registry.domains.add(formula.domain);
    });
  }

  constructor() {
    this.initializeCapitalAllocationFormulas();
  }

  /**
   * Search formulas by domain, complexity, or other criteria
   */
  search(
    domain?: string,
    complexity_min?: FormulaComplexity,
    complexity_max?: FormulaComplexity,
    tags?: string[]
  ): Formula[] {
    const results: Formula[] = [];
    const complexityOrder = { simple: 0, moderate: 1, complex: 2 };

    for (const formula of this.registry.formulas.values()) {
      // Domain filter
      if (domain && formula.domain !== domain) continue;

      // Complexity filters
      if (complexity_min && complexityOrder[formula.complexity] < complexityOrder[complexity_min]) continue;
      if (complexity_max && complexityOrder[formula.complexity] > complexityOrder[complexity_max]) continue;

      // Tag filters
      if (tags && tags.length > 0) {
        const hasAnyTag = tags.some((tag) => formula.tags?.includes(tag));
        if (!hasAnyTag) continue;
      }

      results.push(formula);
    }

    return results;
  }

  /**
   * Get a single formula by ID
   */
  getById(id: string): Formula | undefined {
    return this.registry.formulas.get(id);
  }

  /**
   * Register a new formula
   */
  register(
    name: string,
    domain: string,
    complexity: FormulaComplexity,
    formula_string: string,
    variables: Variable[],
    return_type: VariableType,
    description: string,
    tags?: string[]
  ): Formula {
    const formula: Formula = {
      id: `${domain}-${randomUUID().substring(0, 8)}`,
      name,
      domain,
      complexity,
      formula_string,
      variables,
      return_type,
      description,
      formula_version: '1.0',
      created_at: new Date(),
      updated_at: new Date(),
      tags,
    };

    this.registry.formulas.set(formula.id, formula);
    this.registry.domains.add(domain);
    return formula;
  }

  /**
   * Export formulas to Neo4j format (for Round 3 wiring)
   * Returns JSON that can be imported into Neo4j knowledge graph
   */
  exportToNeoFormat(): {
    formulas: Array<{
      id: string;
      name: string;
      domain: string;
      complexity: string;
      formula_string: string;
      variables: Variable[];
      return_type: string;
      tags: string[];
    }>;
    domains: string[];
  } {
    return {
      formulas: Array.from(this.registry.formulas.values()).map((f) => ({
        id: f.id,
        name: f.name,
        domain: f.domain,
        complexity: f.complexity,
        formula_string: f.formula_string,
        variables: f.variables,
        return_type: f.return_type,
        tags: f.tags || [],
      })),
      domains: Array.from(this.registry.domains),
    };
  }

  /**
   * List all domains
   */
  getDomains(): string[] {
    return Array.from(this.registry.domains);
  }

  /**
   * List all formulas in a domain
   */
  getByDomain(domain: string): Formula[] {
    return Array.from(this.registry.formulas.values()).filter((f) => f.domain === domain);
  }

  /**
   * Get all formulas (for seeding/sync)
   */
  getAll(): Formula[] {
    return Array.from(this.registry.formulas.values());
  }
}

export const FormulaIndex = new FormulaIndexImpl();
