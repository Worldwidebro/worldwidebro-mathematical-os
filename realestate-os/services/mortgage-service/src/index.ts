export const serviceName = 'mortgage-service';
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

export function calculateMortgagePayment(principal: number, annualRate: number, termYears: number) {
  const monthlyRate = annualRate / 100 / 12;
  const numberOfPayments = termYears * 12;
  const monthlyPayment = (principal * monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) /
    (Math.pow(1 + monthlyRate, numberOfPayments) - 1);
  return {
    principal,
    annualRate,
    termYears,
    monthlyPayment: Math.round(monthlyPayment * 100) / 100
  };
}

export function getLoanStatus(loanId: string) {
  return {
    loanId,
    status: 'approved',
    approvedAmount: 400000,
    lender: 'Wells Fargo'
  };
}
