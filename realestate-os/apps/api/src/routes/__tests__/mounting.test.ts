import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import http from 'http';
import app from '../../index.js';

describe('API Gateway Router Mounting Integration Tests', () => {
  let server: http.Server;
  let baseUrl: string;

  beforeAll(async () => {
    await new Promise<void>((resolve) => {
      server = app.listen(0, () => {
        const addr = server.address();
        if (typeof addr === 'object' && addr !== null) {
          baseUrl = `http://localhost:${addr.port}`;
        }
        resolve();
      });
    });
  });

  afterAll(async () => {
    await new Promise<void>((resolve) => {
      server.close(() => resolve());
    });
  });

  it('GET /api/agents returns 20 agents', async () => {
    const res = await fetch(`${baseUrl}/api/agents`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.success).toBe(true);
    expect(data.count).toBe(20);
    expect(data.agents).toHaveLength(20);
  });

  it('GET /api/agents/AcquisitionAgent returns specific agent details', async () => {
    const res = await fetch(`${baseUrl}/api/agents/AcquisitionAgent`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.success).toBe(true);
    expect(data.agent.name).toBe('AcquisitionAgent');
  });

  it('POST /api/agents/AcquisitionAgent/invoke returns 200 OK with logs and output', async () => {
    const res = await fetch(`${baseUrl}/api/agents/AcquisitionAgent/invoke`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ targetMarket: 'Charlotte, NC', minCapRate: 7.5 }),
    });
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.success).toBe(true);
    expect(data.agentName).toBe('AcquisitionAgent');
    expect(Array.isArray(data.logs)).toBe(true);
    expect(data.logs.length).toBeGreaterThan(0);
    expect(data.output).toBeDefined();
    expect(data.output.targetMarket).toBe('Charlotte, NC');
  });

  it('GET /api/services returns catalog of all 35 services', async () => {
    const res = await fetch(`${baseUrl}/api/services`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.success).toBe(true);
    expect(data.totalServicesCount).toBe(35);
    expect(data.services).toHaveLength(35);
  });

  it('GET /api returns catalog of all 35 services', async () => {
    const res = await fetch(`${baseUrl}/api`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.success).toBe(true);
    expect(data.totalServicesCount).toBe(35);
  });

  it('GET /api/services/underwriting/calculate returns mock underwriting service response', async () => {
    const res = await fetch(`${baseUrl}/api/services/underwriting/calculate`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.service).toBe('underwriting-service');
    expect(data.status).toBe('active');
  });

  it('GET /api/identity returns mock identity service response via /api fallback', async () => {
    const res = await fetch(`${baseUrl}/api/identity`);
    expect(res.status).toBe(200);
    const data = (await res.json()) as any;
    expect(data.service).toBe('identity-service');
    expect(data.status).toBe('active');
  });
});
