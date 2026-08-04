## 2026-07-29T14:15:11Z

You are a Worker subagent for realestate-os.

Your task is to fix the API Gateway router mounting in `apps/api`:

1. Check `/Users/acebless/Documents/realestate-os/apps/api/src/routes/services.ts`:
   - If it doesn't exist, create it: export an express router handling `GET /` (listing all 35 services with status and endpoints) and `GET /:serviceName/*` / `POST /:serviceName/*` (returning structured mock responses for all 34 domain services and ai-gateway).
2. Check `/Users/acebless/Documents/realestate-os/apps/api/src/routes/agents.ts`:
   - Ensure it exports an express router handling `GET /` (lists all 20 AI agents), `GET /:agentName` (gets specific agent), and `POST /:agentName/invoke` (invokes agent and returns 200 OK with trace logs and output data).
3. Check `/Users/acebless/Documents/realestate-os/apps/api/src/index.ts`:
   - Import `agentsRouter` from `./routes/agents`.
   - Import `servicesRouter` from `./routes/services`.
   - Explicitly mount `app.use('/api/agents', agentsRouter);`.
   - Explicitly mount `app.use('/api/services', servicesRouter);` and `app.use('/api', servicesRouter);`.
   - Ensure all routes (`/api/auth`, `/api/properties`, `/api/rent-payments`, `/api/maintenance`, `/api/reports`, `/api/email`, `/api/admin`, `/api/analytics`, `/api/agents`, `/api/services`) are mounted cleanly.
4. Run `npm run build -w apps/api` and `npm run build` from root `/Users/acebless/Documents/realestate-os` using run_command.
5. Create a verification script in Node.js or run unit tests to confirm `GET /api/agents` returns 20 agents and `POST /api/agents/AcquisitionAgent/invoke` returns 200 OK with logs.
6. Write report to `/Users/acebless/Documents/realestate-os/.agents/worker_routes_fix/changes.md`.
7. Send a message to parent when completed.
