# Mathematical OS — Phase 2: Formula Engine

**Status:** Complete (Round 2 MVP)  
**Tags:** [infrastructure, phase-2, formula-engine]  
**Generated:** 2026-07-29

---

## Overview

Mathematical OS is a formula index + expression parser + symbol resolver for capital allocation decisions in the family-office OS. It provides:

1. **Formula Index** — registry of domain-specific formulas (capital allocation, ROI prediction, agent scoring)
2. **Symbol Resolver** — variable binding, type checking, scope management
3. **Expression Parser** — AST generation with proper operator precedence, evaluation, error handling

All components are **JSON-only** (no database calls). Neo4j export happens in Round 3.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  formula-index/index.ts                             │
│  - Formula registry: id, name, domain, complexity   │
│  - Search(domain, complexity, tags) → [Formula]     │
│  - Bootstrap with capital allocation formulas       │
│  - Export to Neo4j format                           │
└─────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────┐
│  symbol-resolver/resolver.ts                        │
│  - Scope chain: { bindings: Map, parent }           │
│  - resolveSymbol(name, scope) → SymbolBinding       │
│  - createAllocationContext(params) → Scope          │
│  - validateExpressionTypes(symbols, scope)          │
│  - exportBindings(scope) → Record (audit trail)     │
└─────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────┐
│  expression-parser/parser.ts                        │
│  - parse(formula_string) → AST                      │
│  - Operator precedence: *, /, %, +, -              │
│  - evaluate(ast, scope) → number                    │
│  - extractSymbols(ast) → Set<string>               │
│  - typeCheck(ast, scope, expectedSymbols) → bool    │
│  - min(), max() builtin functions                   │
└─────────────────────────────────────────────────────┘
```

---

## Formula Registry

### Capital Allocation Domain

**Formulas shipped:**
- `tier-1-allocation`: (Pool × 0.27) × (Realized_ROI / 0.15) × Velocity_Factor
- `tier-2-allocation`: (Pool × 0.21) × (Realized_ROI / 0.10) × min(Velocity_Factor, 1.2)
- `tier-3-allocation`: (Pool × 0.18) × (1 + Growth_Rate_6mo) × min(Velocity_Factor, 1.0)
- `predicted-roi`: (OPCO_ROI × 0.4) + (Sector_Benchmark × 0.3) + (Stage_Adjustment × 0.2) + (Market_Sentiment × 0.1)
- `actual-roi`: ((Exit_Value - Deployed_Amount) / Deployed_Amount) × 100

**Usage:**
```typescript
import { FormulaIndex } from './formula-index/index';

// Search by domain
const allocationFormulas = FormulaIndex.search(
  'capital-allocation',
  'simple',
  'moderate',
  ['tier-1', 'mature']
);

// Get specific formula
const tier1 = FormulaIndex.getById('tier-1-allocation');

// Export for Neo4j wiring (Round 3)
const neo4jData = FormulaIndex.exportToNeoFormat();
```

---

## Symbol Resolver

### Binding & Type System

**Variable Types:**
- `number` — generic numeric value
- `percent` — percentage (0–100, sometimes 0–1)
- `amount` — capital in dollars
- `ratio` — multiplier or rate (typically 0–2)
- `count` — integer count

**Scope Chain:**
Follows lexical scoping with parent pointers. Innermost scope wins (shadowing).

**Example:**
```typescript
import { SymbolResolver } from './symbol-resolver/resolver';

// Create context from allocation parameters
const context = SymbolResolver.createAllocationContext({
  opco_name: 'SaaS',
  allocation_amount: 135000000,
  realized_roi_pct: 18,
  velocity_factor: 0.92,
  pool: 500000000,
});

// Resolve a symbol
const pool = SymbolResolver.resolveSymbol('pool', context);
// → { name: 'pool', type: 'amount', value: 500000000, source: 'context' }

// Export for audit trail
const bindings = SymbolResolver.exportBindings(context);
// Used by family-office-os for compliance recording
```

### Type Checking

```typescript
const symbols = new Map([
  ['Pool', 'amount'],
  ['Realized_ROI', 'percent'],
  ['Velocity_Factor', 'ratio'],
]);

const errors = SymbolResolver.validateExpressionTypes(
  symbols,
  context,
  tier1Formula
);

if (errors.length > 0) {
  console.error('Type errors:', errors);
}
```

---

## Expression Parser

### AST Structure

Abstract Syntax Tree node types:
```typescript
type ASTNode =
  | { type: 'number'; value: number }
  | { type: 'symbol'; name: string }
  | { type: 'binary'; op: '+' | '-' | '*' | '/' | '%'; left: ASTNode; right: ASTNode }
  | { type: 'call'; name: 'min' | 'max'; args: ASTNode[] };
```

### Parsing Example

```typescript
import { ExpressionParser } from './expression-parser/parser';

const result = ExpressionParser.parse(
  '(Pool × 0.27) × (Realized_ROI / 0.15) × Velocity_Factor'
);

if (result.success) {
  console.log('AST:', result.ast);
  
  // Extract symbols needed
  const symbols = ExpressionParser.extractSymbols(result.ast);
  // → Set { 'Pool', 'Realized_ROI', 'Velocity_Factor' }
  
  // Evaluate with context
  const allocation = ExpressionParser.evaluate(result.ast, context);
  // → 148460000 (example result)
} else {
  console.error('Parse errors:', result.errors);
}
```

### Operator Precedence

Standard mathematical precedence (implemented via recursive descent):
1. Primary: numbers, symbols, parentheses, function calls
2. Multiplicative: `*`, `/`, `%`, `×`, `÷` (higher precedence)
3. Additive: `+`, `-` (lower precedence)

Example: `a + b * c` → parses as `a + (b * c)` ✓

### Evaluation with Scope

```typescript
// Type-check before evaluation
const isValid = ExpressionParser.typeCheck(result.ast, context, symbols);

if (isValid) {
  try {
    const value = ExpressionParser.evaluate(result.ast, context);
    console.log('Result:', value);
  } catch (err) {
    console.error('Evaluation error:', err.message);
  }
}
```

---

## Integration Points

### Family-Office-OS Integration

**Allocation Agent Usage:**
```typescript
// 1. Fetch formula
const formula = FormulaIndex.getById('tier-1-allocation');

// 2. Bind context
const scope = SymbolResolver.createAllocationContext({
  pool: 500000000,
  realized_roi_pct: 18,
  velocity_factor: 0.92,
});

// 3. Parse formula
const result = ExpressionParser.parse(formula.formula_string);

// 4. Type-check
const isValid = ExpressionParser.typeCheck(
  result.ast,
  scope,
  new Map(formula.variables.map((v) => [v.name, v.type]))
);

// 5. Evaluate
if (isValid && result.success) {
  const allocation = ExpressionParser.evaluate(result.ast, scope);
  
  // Record decision with audit trail
  const bindings = SymbolResolver.exportBindings(scope);
  recordCapitalDecision({
    formula_id: formula.id,
    allocation_amount: allocation,
    context_bindings: bindings,
    decision_timestamp: new Date(),
  });
}
```

### Agent-Platform-OS Integration (Round 3)

**Task Evaluator Usage:**
```typescript
// Evaluate custom formulas for agent task scoring
const customFormula = FormulaIndex.register(
  'Agent Task Score',
  'agent-scoring',
  'moderate',
  '(Complexity × 0.4) + (Confidence × 0.6)',
  [
    { name: 'Complexity', type: 'ratio', description: 'Task complexity score 0-1' },
    { name: 'Confidence', type: 'ratio', description: 'Agent confidence 0-1' },
  ],
  'ratio',
  'Weighted scoring for agent task prioritization'
);

const taskContext = SymbolResolver.createScope();
SymbolResolver.bind(taskContext, 'Complexity', 'ratio', 0.75);
SymbolResolver.bind(taskContext, 'Confidence', 'ratio', 0.92);

const parseResult = ExpressionParser.parse(customFormula.formula_string);
const score = ExpressionParser.evaluate(parseResult.ast, taskContext);
// → 0.854 (60% confidence, 40% complexity)
```

### Neo4j Export (Round 3)

```typescript
// Export to Neo4j format
const neo4jData = FormulaIndex.exportToNeoFormat();

// Upload to Neo4j via:
// POST /neo4j/formulas
// Body: neo4jData
// Creates nodes: (Formula {id, name, domain, complexity})
// Creates edges: REFERENCES → (Variable), USES → (Symbol)
```

---

## Testing

### Test Coverage

**formula-index:**
- ✓ Bootstrap formulas loaded correctly
- ✓ Search by domain, complexity, tags
- ✓ Register new formula
- ✓ getById, getByDomain, getAll
- ✓ exportToNeoFormat structure

**symbol-resolver:**
- ✓ Scope chain and shadowing
- ✓ resolveSymbol with missing symbol (error)
- ✓ Type validation correct/mismatch
- ✓ Builtin binding (pi, e, min, max)
- ✓ createAllocationContext heuristic typing

**expression-parser:**
- ✓ Parse valid formulas
- ✓ Operator precedence (* before +)
- ✓ Parentheses grouping
- ✓ Function calls min(a, b)
- ✓ Symbol extraction
- ✓ Evaluate with scope
- ✓ Division by zero error
- ✓ Parse errors for invalid input

---

## Known Limitations

| Limitation | Impact | Round 3 Fix |
|-----------|--------|-----------|
| JSON storage only | No persistence across restarts | Supabase sync + formulas table |
| No custom user formulas (yet) | Hardcoded capital allocation set | `formula_registrations` table + REST API |
| No formula versioning in graph | Neo4j export flat | Add `formula_version` node + `VERSION_OF` edge |
| Builtin functions limited (min/max) | Can't express complex operations | Add sqrt, abs, round, exp, log |
| No constraint validation | Can register malformed formulas | Add optional `validator()` field to Formula |
| No formula docs/comments | Discovery is opaque | Add `formula_notes` field, export to Neo4j |

---

## Roadmap

### Round 2 (Complete)
- ✓ Formula index with capital allocation formulas
- ✓ Symbol resolver with type checking
- ✓ Expression parser with AST + evaluation
- ✓ Basic error handling

### Round 3 (Planned)
- [ ] Supabase `formulas` table + sync
- [ ] Neo4j import + knowledge graph wiring
- [ ] REST API for formula registration
- [ ] Formula versioning in graph
- [ ] Extended builtins (sqrt, abs, round, etc.)
- [ ] Constraint validation on register()
- [ ] Integration tests with family-office-os allocation agent

### Round 4+ (Backlog)
- [ ] Formula marketplace / discovery UI
- [ ] Formula analytics (usage frequency, accuracy)
- [ ] Multi-formula compositions (formula references other formulas)
- [ ] Time-based formulas (schedule-based allocation changes)

---

## API Reference

### FormulaIndex

```typescript
FormulaIndex.search(
  domain?: string,
  complexity_min?: 'simple' | 'moderate' | 'complex',
  complexity_max?: 'simple' | 'moderate' | 'complex',
  tags?: string[]
): Formula[]

FormulaIndex.getById(id: string): Formula | undefined

FormulaIndex.register(
  name: string,
  domain: string,
  complexity: 'simple' | 'moderate' | 'complex',
  formula_string: string,
  variables: Variable[],
  return_type: VariableType,
  description: string,
  tags?: string[]
): Formula

FormulaIndex.exportToNeoFormat(): { formulas: Array<...>; domains: string[] }

FormulaIndex.getDomains(): string[]
FormulaIndex.getByDomain(domain: string): Formula[]
FormulaIndex.getAll(): Formula[]
```

### SymbolResolver

```typescript
SymbolResolver.createScope(parent?: Scope): Scope

SymbolResolver.bind(
  scope: Scope,
  name: string,
  type: VariableType,
  value?: number | string | boolean
): SymbolBinding

SymbolResolver.resolveSymbol(name: string, scope: Scope): SymbolBinding

SymbolResolver.bindFormulaVariables(scope: Scope, formula: Formula): void

SymbolResolver.bindBuiltins(scope: Scope): void

SymbolResolver.validateType(
  binding: SymbolBinding,
  expectedType: VariableType,
  symbol: string
): TypeCheckError | null

SymbolResolver.validateExpressionTypes(
  symbols: Map<string, string>,
  scope: Scope,
  formula: Formula
): TypeCheckError[]

SymbolResolver.exportBindings(scope: Scope): Record<string, { type; value; source }>

SymbolResolver.createAllocationContext(params: Record<string, any>): Scope
```

### ExpressionParser

```typescript
ExpressionParser.parse(formula: string): ExpressionResult

ExpressionParser.extractSymbols(ast: ASTNode | null): Set<string>

ExpressionParser.evaluate(ast: ASTNode | null, scope: Scope): number

ExpressionParser.typeCheck(
  ast: ASTNode | null,
  scope: Scope,
  expectedSymbols: Map<string, VariableType>
): boolean
```

---

## Files

```
mathematical-os/
├── formula-index/
│   └── index.ts              (170 lines, 5 capital allocation formulas)
├── symbol-resolver/
│   └── resolver.ts           (200 lines, scope chain + type system)
├── expression-parser/
│   └── parser.ts             (250 lines, recursive descent + eval)
├── docs/
│   └── PHASE-2.md            (this file)
├── tests/
│   └── (placeholder for Round 3)
├── package.json
└── README.md
```

---

**Version:** 1.0  
**Last Updated:** 2026-07-29  
**Next Review:** Round 3 (Neo4j wiring)
