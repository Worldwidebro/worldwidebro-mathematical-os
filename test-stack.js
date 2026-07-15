#!/usr/bin/env node
const http = require('http');

const checks = [
  { name: 'neo4j', host: 'localhost', port: 7474, path: '/', allowStatuses: [301, 200, 404] },
  { name: 'grafana', host: 'localhost', port: 3001, path: '/api/health', allowStatuses: [200] },
  { name: 'qdrant', host: 'localhost', port: 6333, path: '/', allowStatuses: [200, 404, 302] },
];

function checkHttp({ name, host, port, path, allowStatuses = [] }) {
  return new Promise((resolve) => {
    const start = Date.now();
    const req = http.request({ host, port, path, method: 'GET', timeout: 5000 });
    req.on('error', () => resolve({ name, ok: false, status: 0, duration: Date.now() - start }));
    req.on('timeout', () => {
      req.destroy();
      resolve({ name, ok: false, status: 0, duration: Date.now() - start });
    });
    req.on('response', (res) => {
      const duration = Date.now() - start;
      const ok = allowStatuses.includes(res.statusCode);
      resolve({ name, ok, status: res.statusCode, duration });
    });
  });
}

async function main() {
  const checksToRun = checks.map(checkHttp);
  const results = await Promise.all(checksToRun);
  let failed = 0;
  for (const r of results) {
    const status = r.ok ? 'PASS' : 'FAIL';
    console.log(`[${status}] ${r.name}: ${r.status} (${r.duration}ms)`);
    if (!r.ok) failed++;
  }

  if (failed) {
    console.error(`\n${failed} check(s) failed.`);
    process.exit(1);
  }

  console.log('\nStack health checks passed.');
}

main();
