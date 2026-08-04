import { Formula, Variable, VariableType } from '../formula-index/index';

export interface SymbolBinding {
  name: string;
  type: VariableType;
  value?: number | string | boolean;
  source: 'context' | 'formula' | 'builtin';
}

export interface TypeCheckError {
  symbol: string;
  expected: VariableType;
  actual: VariableType;
  message: string;
}

export interface Scope {
  bindings: Map<string, SymbolBinding>;
  parent?: Scope;
}

class SymbolResolverImpl {
  /**
   * Resolve a symbol in the given context (scope chain)
   * Returns the binding if found, throws if not found
   */
  resolveSymbol(name: string, scope: Scope): SymbolBinding {
    let current: Scope | undefined = scope;
    while (current) {
      const binding = current.bindings.get(name);
      if (binding) return binding;
      current = current.parent;
    }
    throw new Error(`Symbol not found: ${name}`);
  }

  /**
   * Create a new scope with optional parent (for closures)
   */
  createScope(parent?: Scope): Scope {
    return { bindings: new Map(), parent };
  }

  /**
   * Bind a variable in a scope
   */
  bind(scope: Scope, name: string, type: VariableType, value?: number | string | boolean): SymbolBinding {
    const binding: SymbolBinding = {
      name,
      type,
      value,
      source: 'context',
    };
    scope.bindings.set(name, binding);
    return binding;
  }

  /**
   * Bind all variables from a formula into a scope
   */
  bindFormulaVariables(scope: Scope, formula: Formula): void {
    formula.variables.forEach((variable) => {
      this.bind(scope, variable.name, variable.type);
    });
  }

  /**
   * Add builtin constants (e.g., pi, e) to a scope
   */
  bindBuiltins(scope: Scope): void {
    const builtins = [
      { name: 'pi', type: 'number' as VariableType, value: Math.PI },
      { name: 'e', type: 'number' as VariableType, value: Math.E },
      { name: 'min', type: 'number' as VariableType, source: 'builtin' as const },
      { name: 'max', type: 'number' as VariableType, source: 'builtin' as const },
    ];

    builtins.forEach(({ name, type, value, source }) => {
      scope.bindings.set(name, {
        name,
        type,
        value,
        source: source || 'builtin',
      });
    });
  }

  /**
   * Validate that a symbol has the expected type
   */
  validateType(
    binding: SymbolBinding,
    expectedType: VariableType,
    symbol: string
  ): TypeCheckError | null {
    if (binding.type !== expectedType) {
      return {
        symbol,
        expected: expectedType,
        actual: binding.type,
        message: `Type mismatch: ${symbol} is ${binding.type} but expected ${expectedType}`,
      };
    }
    return null;
  }

  /**
   * Validate all symbols used in an expression against a formula's expected types
   * Returns errors array (empty = valid)
   */
  validateExpressionTypes(
    symbols: Map<string, string>, // symbol name -> expected type
    scope: Scope,
    formula: Formula
  ): TypeCheckError[] {
    const errors: TypeCheckError[] = [];

    for (const [symbol, expectedType] of symbols.entries()) {
      try {
        const binding = this.resolveSymbol(symbol, scope);
        const error = this.validateType(binding, expectedType as VariableType, symbol);
        if (error) errors.push(error);
      } catch {
        errors.push({
          symbol,
          expected: expectedType as VariableType,
          actual: 'number' as VariableType, // placeholder for missing symbol
          message: `Symbol not found: ${symbol}`,
        });
      }
    }

    return errors;
  }

  /**
   * Export scope bindings for audit/compliance (family-office-os integration)
   * Used to validate that allocation formula has all required context
   */
  exportBindings(scope: Scope): Record<string, { type: VariableType; value?: any; source: string }> {
    const exported: Record<string, { type: VariableType; value?: any; source: string }> = {};

    let current: Scope | undefined = scope;
    while (current) {
      for (const [name, binding] of current.bindings.entries()) {
        if (!exported[name]) {
          // Innermost scope wins (shadowing)
          exported[name] = {
            type: binding.type,
            value: binding.value,
            source: binding.source,
          };
        }
      }
      current = current.parent;
    }

    return exported;
  }

  /**
   * Create a scope from allocation context (family-office-os integration)
   * Example: { opco_name: "SaaS", allocation_amount: 135000000, velocity_factor: 0.92, roi_pct: 18 }
   */
  createAllocationContext(params: Record<string, any>): Scope {
    const scope = this.createScope();
    this.bindBuiltins(scope);

    // Map incoming params to typed bindings
    for (const [key, value] of Object.entries(params)) {
      let type: VariableType = 'number';

      // Heuristic type inference
      if (key.includes('amount') || key.includes('pool') || key.includes('capital')) {
        type = 'amount';
      } else if (key.includes('roi') || key.includes('return')) {
        type = 'percent';
      } else if (key.includes('factor') || key.includes('rate')) {
        type = 'ratio';
      } else if (key.includes('count') || key.includes('velocity')) {
        type = 'ratio';
      }

      this.bind(scope, key, type, value);
    }

    return scope;
  }
}

export const SymbolResolver = new SymbolResolverImpl();
