import { loadEnv, defineConfig, Modules } from '@medusajs/framework/utils'

loadEnv(process.env.NODE_ENV || 'development', process.cwd())

const modules: Record<string, any> = {}

if (process.env.REDIS_URL) {
  modules[Modules.CACHE] = {
    resolve: '@medusajs/cache-redis',
    options: { redisUrl: process.env.REDIS_URL },
  }
  modules[Modules.EVENT_BUS] = {
    resolve: '@medusajs/event-bus-redis',
    options: { redisUrl: process.env.REDIS_URL },
  }
  modules[Modules.WORKFLOW_ENGINE] = {
    resolve: '@medusajs/workflow-engine-redis',
    options: { redis: { url: process.env.REDIS_URL } },
  }
  modules[Modules.LOCKING] = {
    resolve: '@medusajs/locking',
    options: {
      providers: [
        {
          resolve: '@medusajs/locking-redis',
          id: 'locking-redis',
          is_default: true,
          options: { redisUrl: process.env.REDIS_URL },
        },
      ],
    },
  }
}

if (process.env.STRIPE_API_KEY) {
  modules[Modules.PAYMENT] = {
    resolve: '@medusajs/payment',
    options: {
      providers: [
        {
          resolve: '@medusajs/payment-stripe',
          id: 'stripe',
          options: {
            apiKey: process.env.STRIPE_API_KEY,
            webhookSecret: process.env.STRIPE_WEBHOOK_SECRET,
          },
        },
      ],
    },
  }
}

module.exports = defineConfig({
  projectConfig: {
    databaseUrl: process.env.DATABASE_URL,
    http: {
      storeCors: process.env.STORE_CORS!,
      adminCors: process.env.ADMIN_CORS!,
      authCors: process.env.AUTH_CORS!,
      jwtSecret: process.env.JWT_SECRET,
      cookieSecret: process.env.COOKIE_SECRET,
    }
  },
  modules,
})
