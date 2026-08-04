import { Scope, SymbolResolver } from '../symbol-resolver/resolver';
import { VariableType } from '../formula-index/index';

export type ASTNode =
  | { type: 'number'; value: number }
  | { type: 'symbol'; name: string }
  | { type: 'binary'; op: string; left: ASTNode; right: ASTNode }
  | { type: 'call'; name: string; args: ASTNode[] };

export interface ParseError {
  message: string;
  position: number;
  token?: string;
}

export interface ExpressionResult {
  ast: ASTNode | null;
  errors: ParseError[];
  success: boolean;
}

class ExpressionParserImpl {
  private formula: string = '';
  private pos: number = 0;

  /**
   * Tokenize: split formula into tokens
   */
  private tokenize(formula: string): string[] {
    // Split on operators, parentheses, whitespace; preserve operators
    return formula
      .replace(/([+\-*/%()×÷,])/g, ' $1 ') // Normalize × and ÷ to operators
      .split(/\s+/)
      .filter((t) => t.length > 0);
  }

  /**
   * Peek at current token without consuming
   */
  private peek(tokens: string[], offset: number = 0): string | undefined {
    return tokens[this.pos + offset];
  }

  /**
   * Consume and return current token
   */
  private consume(tokens: string[]): string | undefined {
    return tokens[this.pos++];
  }

  /**
   * Parse primary expression: number, symbol, or parenthesized expression
   */
  private parsePrimary(tokens: string[]): ASTNode | null {
    const token = this.peek(tokens);
    if (!token) return null;

    // Number literal
    if (/^-?\d+(\.\d+)?$/.test(token)) {
      this.consume(tokens);
      return { type: 'number', value: parseFloat(token) };
    }

    // Parenthesized expression
    if (token === '(') {
      this.consume(tokens); // consume '('
      const expr = this.parseAdditive(tokens);
      if (this.peek(tokens) === ')') {
        this.consume(tokens); // consume ')'
      }
      return expr;
    }

    // Function call or symbol
    if (/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(token)) {
      const name = this.consume(tokens);
      if (this.peek(tokens) === '(') {
        // Function call
        this.consume(tokens); // consume '('
        const args: ASTNode[] = [];
        while (this.peek(tokens) && this.peek(tokens) !== ')') {
          const arg = this.parseAdditive(tokens);
          if (arg) args.push(arg);
          if (this.peek(tokens) === ',') {
            this.consume(tokens); // consume ','
          }
        }
        if (this.peek(tokens) === ')') {
          this.consume(tokens); // consume ')'
        }
        return { type: 'call', name: name!, args };
      } else {
        // Symbol reference
        return { type: 'symbol', name: name! };
      }
    }

    return null;
  }

  /**
   * Parse multiplicative expressions: * / % (higher precedence)
   */
  private parseMultiplicative(tokens: string[]): ASTNode | null {
    let left = this.parsePrimary(tokens);
    if (!left) return null;

    while (true) {
      const op = this.peek(tokens);
      if (!op || !['*', '/', '%', '×', '÷'].includes(op)) break;

      this.consume(tokens);
      const right = this.parsePrimary(tokens);
      if (!right) {
        // Error: missing right operand
        return left;
      }

      // Normalize operators
      const normalizedOp = op === '×' ? '*' : op === '÷' ? '/' : op;
      left = { type: 'binary', op: normalizedOp, left, right };
    }

    return left;
  }

  /**
   * Parse additive expressions: + - (lower precedence)
   */
  private parseAdditive(tokens: string[]): ASTNode | null {
    let left = this.parseMultiplicative(tokens);
    if (!left) return null;

    while (true) {
      const op = this.peek(tokens);
      if (!op || !['+', '-'].includes(op)) break;

      this.consume(tokens);
      const right = this.parseMultiplicative(tokens);
      if (!right) {
        return left;
      }

      left = { type: 'binary', op, left, right };
    }

    return left;
  }

  /**
   * Main parse entry point
   */
  private parseExpression(tokens: string[]): ASTNode | null {
    return this.parseAdditive(tokens);
  }

  /**
   * Parse a formula string into an AST
   * Handles errors gracefully
   */
  parse(formula: string): ExpressionResult {
    const errors: ParseError[] = [];
    this.formula = formula;
    this.pos = 0;

    try {
      const tokens = this.tokenize(formula);
      const ast = this.parseExpression(tokens);

      // Check if we consumed all tokens
      if (this.pos < tokens.length) {
        const unconsumed = tokens.slice(this.pos).join(' ');
        errors.push({
          message: `Unexpected tokens: ${unconsumed}`,
          position: formula.length - unconsumed.length,
          token: unconsumed,
        });
      }

      return {
        ast: ast || null,
        errors,
        success: errors.length === 0 && ast !== null,
      };
    } catch (err) {
      return {
        ast: null,
        errors: [
          {
            message: err instanceof Error ? err.message : 'Unknown parse error',
            position: this.pos,
          },
        ],
        success: false,
      };
    }
  }

  /**
   * Extract all symbols (variable references) from an AST
   */
  extractSymbols(ast: ASTNode | null): Set<string> {
    if (!ast) return new Set();

    const symbols = new Set<string>();

    const visit = (node: ASTNode) => {
      if (node.type === 'symbol') {
        symbols.add(node.name);
      } else if (node.type === 'binary') {
        visit(node.left);
        visit(node.right);
      } else if (node.type === 'call') {
        node.args.forEach(visit);
      }
    };

    visit(ast);
    return symbols;
  }

  /**
   * Evaluate an AST given a scope of variable bindings
   * Throws if a symbol is not bound
   */
  evaluate(ast: ASTNode | null, scope: Scope): number {
    if (!ast) throw new Error('Cannot evaluate null AST');

    if (ast.type === 'number') {
      return ast.value;
    }

    if (ast.type === 'symbol') {
      const binding = SymbolResolver.resolveSymbol(ast.name, scope);
      if (binding.value !== undefined && typeof binding.value === 'number') {
        return binding.value;
      }
      throw new Error(`Symbol ${ast.name} has no numeric value`);
    }

    if (ast.type === 'binary') {
      const left = this.evaluate(ast.left, scope);
      const right = this.evaluate(ast.right, scope);

      switch (ast.op) {
        case '+':
          return left + right;
        case '-':
          return left - right;
        case '*':
          return left * right;
        case '/':
          if (right === 0) throw new Error('Division by zero');
          return left / right;
        case '%':
          return left % right;
        default:
          throw new Error(`Unknown operator: ${ast.op}`);
      }
    }

    if (ast.type === 'call') {
      // Built-in functions
      if (ast.name === 'min') {
        const values = ast.args.map((arg) => this.evaluate(arg, scope));
        return Math.min(...values);
      }
      if (ast.name === 'max') {
        const values = ast.args.map((arg) => this.evaluate(arg, scope));
        return Math.max(...values);
      }
      throw new Error(`Unknown function: ${ast.name}`);
    }

    throw new Error(`Unknown AST node type`);
  }

  /**
   * Type-check an expression against expected symbols
   * Returns true if all symbols are bound and have correct types
   */
  typeCheck(ast: ASTNode | null, scope: Scope, expectedSymbols: Map<string, VariableType>): boolean {
    if (!ast) return false;

    const symbols = this.extractSymbols(ast);

    for (const symbol of symbols) {
      try {
        SymbolResolver.resolveSymbol(symbol, scope);
      } catch {
        return false;
      }
    }

    return true;
  }
}

export const ExpressionParser = new ExpressionParserImpl();
