---
name: official-cloudflare-workers
description: Official Cloudflare Workers and edge computing skill covering V8 isolate runtimes, KV storage, D1 SQL, Queues, R2 object storage, and Wrangler configuration.
source: VoltAgent/awesome-agent-skills
origin: Cloudflare Official Developer Standards
---

[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# 🌐 Official Cloudflare Workers Skill

> Authoritative edge computing standards based on Cloudflare Workers, V8 isolate execution, KV/D1 persistence, and sub-millisecond global routing.

## 🧠 Core Principles

1. **Isolate Efficiency**: Avoid heavy Node.js standard libraries. Use web standard APIs (`fetch`, `Request`, `Response`, `Web Crypto`).
2. **Stateless Handlers**: Handle requests without relying on local in-memory persistence across isolates. Use Cloudflare KV, D1, or Durable Objects for state.
3. **Fail-Closed Security**: Validate environment secrets (`c.env`) and JWT headers before executing downstream routing.
4. **Zero Cold Start Mindset**: Keep script bundles small and bundle dependencies cleanly using `esbuild` / Wrangler.

---

## 🛠️ Implementation Patterns

### 1. Edge Router with KV & Response Cache

```typescript
export interface Env {
  VENTURE_KV: KVNamespace;
  API_SECRET: string;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    // Health check endpoint
    if (url.pathname === '/health') {
      return new Response(JSON.stringify({ status: 'ok', node: 'edge' }), {
        headers: { 'content-type': 'application/json' },
      });
    }

    // Read cached payload from KV
    const cacheKey = `cache:${url.pathname}`;
    const cachedData = await env.VENTURE_KV.get(cacheKey);

    if (cachedData) {
      return new Response(cachedData, {
        headers: {
          'content-type': 'application/json',
          'x-cache-status': 'HIT',
        },
      });
    }

    // Fallback: Fetch upstream and write-through cache asynchronously
    const upstreamRes = await fetch(`https://api.worldwidebro.com${url.pathname}`, {
      headers: { Authorization: `Bearer ${env.API_SECRET}` },
    });
    const responseData = await upstreamRes.text();

    ctx.waitUntil(
      env.VENTURE_KV.put(cacheKey, responseData, { expirationTtl: 3600 })
    );

    return new Response(responseData, {
      status: upstreamRes.status,
      headers: {
        'content-type': 'application/json',
        'x-cache-status': 'MISS',
      },
    });
  },
};
```

---

## 🔒 Edge Security Checklist

- [ ] Secrets are bound via `wrangler secret put` and never committed in `wrangler.toml`.
- [ ] CORS headers are restrictive and match production domains.
- [ ] Rate limiting is enforced via Cloudflare Rate Limiting Rules or KV counters.
