export const serviceName = 'accounting-service';
export const version = '1.0.0';
export const status = 'active';

export interface HealthCheckResult {
  serviceName: string;
  version: string;
  status: 'healthy' | 'unhealthy';
  timestamp: string;
  uptime: number;
}

const startTime = Date.now();

export function getHealthStatus(): HealthCheckResult {
  return {
    serviceName,
    version,
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: Math.floor((Date.now() - startTime) / 1000)
  };
}

export function initializeService(): { serviceName: string; initialized: boolean; timestamp: string } {
  return {
    serviceName,
    initialized: true,
    timestamp: new Date().toISOString()
  };
}

export function getLedgerEntries(accountFilter?: string) {
  return [
    { id: 'entry-1', account: accountFilter || '1000-Cash', debit: 5000, credit: 0, date: new Date().toISOString() },
    { id: 'entry-2', account: accountFilter || '4000-RentalIncome', debit: 0, credit: 5000, date: new Date().toISOString() }
  ];
}

export function createJournalEntry(entry: { description: string; amount: number; type: 'debit' | 'credit' }) {
  return {
    id: `entry-${Date.now()}`,
    ...entry,
    createdAt: new Date().toISOString()
  };
}
